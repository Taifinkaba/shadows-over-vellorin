"""Validate routing, YAML metadata, evidence paths and the campaign snapshot."""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys

import yaml


class ValidationError(ValueError):
    """Invalid repository data, suitable for display without a traceback."""


class UniqueLoader(yaml.SafeLoader):
    """Safe YAML, rejecting duplicate keys instead of silently taking the last."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ValidationError("YAML mapping keys must be strings")
        if key in result:
            raise ValidationError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
TYPES = {"characters", "creatures", "items", "locations", "quests", "factions", "rules", "mechanics"}
STATUSES = {"canon", "last-verified", "gm-secret-locked", "active", "research", "completed", "user-locked"}
VISIBILITIES = {"gm-reference", "gm-secret"}
REQUIRED = {"id", "type", "status", "visibility", "source_refs"}
ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
MONEY_FIELDS = {"central_gp_sp", "emergency_gp_sp", "reserve_gp_sp", "operating_gp_sp", "development_gp_sp", "total_gp_sp"}
MONEY_FIELDS_V3 = {"total_gp_sp", "blackscale_private_gp_sp", "expedition_gp_sp", "excluded_lyanna_gp_sp", "scene_opening_gp_sp", "scene_recovery_gp_sp", "scene_cost_gp_sp"}
RESOURCES = {"equipped_defense", "bracers_defense_bonus", "staff_mp", "staff_mp_max", "wagon_mp", "wagon_mp_max", "chronos_eye_locked", "dragon_slayer_locked"}
STATS = {"hp", "hp_max", "mp", "mp_max", "defense", "rank", "level", "str", "dex", "con", "int", "wis", "cha", "unspent_attributes"}
WORLD = {"vaeltharion_chains_attached", "protective_anchors_retained"}
# Owners of structured snapshot facts; values live in entity frontmatter, not here.
OWNERS = {
    "theron-ashvale": {"date", "time", "location", "status"} | {f"theron.{k}" for k in STATS},
    "vaeltharion": {f"world.{k}" for k in WORLD},
    "party-finances": {f"money.{k}" for k in MONEY_FIELDS},
}


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def mapping(value, label):
    require(isinstance(value, dict), f"{label}: expected a mapping")
    return value


def keys(value, expected, label):
    mapping(value, label)
    require(set(value) == expected, f"{label}: expected keys {sorted(expected)}")


def string(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label}: expected a nonempty string")
    return value


def integer(value, label, minimum=0):
    require(type(value) is int and value >= minimum, f"{label}: expected an integer >= {minimum}")


def repository_file(root, value, label):
    """Resolve normalized POSIX paths inside the repository, including symlinks."""
    string(value, label)
    p = PurePosixPath(value)
    require(not p.is_absolute() and "\\" not in value and all(part not in {"", ".", ".."} for part in value.split("/")),
            f"{label}: expected a normalized repository-relative path")
    target = root.joinpath(*p.parts)
    require(target.resolve().is_relative_to(root.resolve()), f"{label}: path escapes repository")
    require(target.is_file(), f"{label}: missing file {value}")
    return target


def unique_json(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_json)
    except (OSError, ValueError) as exc:
        raise ValidationError(f"{path.name}: {exc}") from exc


def frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    require(bool(lines) and lines[0] == "---", f"{path.name}: missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValidationError(f"{path.name}: unterminated YAML frontmatter") from exc
    try:
        data = yaml.load("\n".join(lines[1:end]), Loader=UniqueLoader)
    except (yaml.YAMLError, ValidationError) as exc:
        raise ValidationError(f"{path.name}: invalid YAML: {exc}") from exc
    mapping(data, path.name)
    require(REQUIRED <= data.keys(), f"{path.name}: required frontmatter fields {sorted(REQUIRED)}")
    require(set(data) <= REQUIRED | {"checkpoint_values"}, f"{path.name}: unknown frontmatter fields")
    for field in ("id", "type", "status", "visibility"):
        string(data[field], f"{path.name}.{field}")
    require(ID.fullmatch(data["id"]) is not None, f"{path.name}: invalid entity ID")
    for field, choices in (("type", TYPES), ("status", STATUSES), ("visibility", VISIBILITIES)):
        require(data[field] in choices, f"{path.name}: invalid {field}")
    require(data["status"] != "gm-secret-locked" or data["visibility"] == "gm-secret",
            f"{path.name}: locked GM secret must have gm-secret visibility")
    refs = data["source_refs"]
    require(isinstance(refs, list) and bool(refs), f"{path.name}: source_refs must be a nonempty list")
    for ref in refs:
        string(ref, f"{path.name}.source_refs")
    require(len(refs) == len(set(refs)), f"{path.name}: duplicate source_refs")
    return data


def copper(value, label="currency"):
    """10 cp = 1 sp; 10 sp = 1 gp. No float conversions or partial matches."""
    string(value, label)
    match = re.fullmatch(r"\s*(?:(\d+)\s*gp\s*)?(?:(\d+)\s*sp\s*)?(?:(\d+)\s*cp\s*)?", value)
    require(match is not None and any(x is not None for x in match.groups()), f"{label}: invalid currency")
    gp, sp, cp = (int(x or 0) for x in match.groups())
    return gp * 100 + sp * 10 + cp


def validate_state(state):
    version = state.get("schema_version")
    v3 = type(version) is int and version == 3
    keys(state, {"schema_version", "date", "time", "location", "theron", "money", "world", "status", "source", "context"} | ({"resources"} if v3 else set()), "checkpoint")
    require(type(state["schema_version"]) is int and state["schema_version"] in {2, 3}, "checkpoint: unsupported schema_version")
    for field in ("date", "time", "location", "status", "source"):
        string(state[field], f"checkpoint.{field}")
    require(re.fullmatch(r"Year \d+ Day \d+", state["date"]) is not None, "checkpoint: invalid date")
    require(re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", state["time"]) is not None, "checkpoint: invalid time")
    require(state["status"] == ("ENDED" if v3 else "PAUSED"), "checkpoint: invalid session status")
    stats = state["theron"]
    keys(stats, STATS, "checkpoint.theron")
    for field in STATS - {"rank"}:
        integer(stats[field], f"checkpoint.theron.{field}", 1 if field in {"hp_max", "mp_max"} else 0)
    string(stats["rank"], "checkpoint.theron.rank")
    require(stats["hp"] <= stats["hp_max"], "checkpoint: HP exceeds maximum")
    require(stats["mp"] <= stats["mp_max"], "checkpoint: MP exceeds maximum")
    money_fields = MONEY_FIELDS_V3 if v3 else MONEY_FIELDS
    keys(state["money"], money_fields | ({"allocation_status"} if v3 else set()), "checkpoint.money")
    balances = {k: copper(state["money"][k], f"checkpoint.money.{k}") for k in money_fields}
    if v3:
        string(state["money"]["allocation_status"], "money.allocation_status")
        require(state["money"]["allocation_status"].startswith("unverified"), "money: allocation must remain explicitly unverified")
        require(balances["blackscale_private_gp_sp"] + balances["expedition_gp_sp"] <= balances["total_gp_sp"],
                "checkpoint: verified components exceed controlled cash")
        require(balances["scene_opening_gp_sp"] + balances["scene_recovery_gp_sp"] - balances["scene_cost_gp_sp"] == balances["total_gp_sp"],
                "checkpoint: currency total differs from final scene reconciliation")
        resources = state["resources"]
        keys(resources, RESOURCES, "checkpoint.resources")
        for field in RESOURCES - {"chronos_eye_locked", "dragon_slayer_locked"}:
            integer(resources[field], f"resources.{field}", 1 if field.endswith("_max") else 0)
        for pool in ("staff", "wagon"):
            require(resources[f"{pool}_mp"] <= resources[f"{pool}_mp_max"], f"resources: {pool} mana exceeds maximum")
        require(resources["equipped_defense"] == stats["defense"] + resources["bracers_defense_bonus"],
                "resources: equipped Defense must equal permanent base plus equipment bonus")
        for field in ("chronos_eye_locked", "dragon_slayer_locked"):
            require(resources[field] is True, f"resources: {field} must remain locked by player ruling")
    else:
        require(sum(v for k, v in balances.items() if k != "total_gp_sp") == balances["total_gp_sp"],
                "checkpoint: currency total differs from consolidated account balances")
    keys(state["world"], WORLD, "checkpoint.world")
    for field, value in state["world"].items():
        integer(value, f"checkpoint.world.{field}")
    # Chains and anchors are separate facts, compared with the entity below.
    context = state["context"]
    keys(context, {"safety", "companions_present", "party_roles", "projects", "academy", "outstanding_clues", "recent_mp_costs", "mp_before_recent_casts"}, "checkpoint.context")
    string(context["safety"], "context.safety")
    for field in ("companions_present", "outstanding_clues"):
        require(isinstance(context[field], list) and bool(context[field]), f"context.{field}: expected a nonempty list")
        for value in context[field]:
            string(value, f"context.{field}")
    for field in ("party_roles", "projects"):
        mapping(context[field], f"context.{field}")
        require(bool(context[field]), f"context.{field}: expected entries")
        for key, value in context[field].items():
            string(key, field); string(value, field)
    academy = context["academy"]
    keys(academy, {"entity", "latest_reported_cash_gp_sp", "refundable_lease_deposit_gp_sp", "balance_date", "included_in_party_total"}, "context.academy")
    for key in ("entity", "balance_date"):
        string(academy[key], f"academy.{key}")
    for key in ("latest_reported_cash_gp_sp", "refundable_lease_deposit_gp_sp"):
        copper(academy[key], f"academy.{key}")
    require(academy["included_in_party_total"] is False, "academy funds must remain separate")
    costs = mapping(context["recent_mp_costs"], "context.recent_mp_costs")
    if v3:
        require(not costs and context["mp_before_recent_casts"] is None,
                "context: final-scene individual mana costs and starting MP remain unverified")
        return
    require(bool(costs), "context.recent_mp_costs: expected entries")
    for spell, cost in costs.items():
        string(spell, "spell name"); integer(cost, f"spell cost: {spell}")
    integer(context["mp_before_recent_casts"], "context.mp_before_recent_casts")
    require(context["mp_before_recent_casts"] <= stats["mp_max"], "recent starting MP exceeds maximum")
    require(context["mp_before_recent_casts"] - sum(costs.values()) == stats["mp"], "recent MP expenditure does not match checkpoint")


def validate(root):
    root = Path(root).resolve()
    idx = read_json(root / "index.json")
    keys(idx, {"schema_version", "project", "authoritative_root", "entries", "archive_index"}, "index")
    require(type(idx["schema_version"]) is int and idx["schema_version"] == 2, "index: unsupported schema_version")
    string(idx["project"], "index.project")
    require(idx["authoritative_root"] == "entities/", "index: authoritative_root must be entities/")
    entries = idx["entries"]
    require(isinstance(entries, list) and bool(entries), "index.entries must be a nonempty list")
    ids, paths, records = set(), set(), {}
    for entry in entries:
        keys(entry, {"id", "type", "title", "path", "status", "visibility", "tags"}, "index entry")
        for field in ("id", "type", "title", "path", "status", "visibility"):
            string(entry[field], f"index entry.{field}")
        require(entry["id"] not in ids, f"duplicate entity ID: {entry['id']}")
        require(entry["path"] not in paths, f"duplicate entity path: {entry['path']}")
        ids.add(entry["id"])
        paths.add(entry["path"])
        require(isinstance(entry["tags"], list) and all(isinstance(t, str) and t.strip() for t in entry["tags"]),
                f"{entry['id']}: tags must be a list of nonempty strings")
        path = repository_file(root, entry["path"], "index entry.path")
        data = frontmatter(path)
        require(entry["path"] == f"entities/{data['type']}/{data['id']}.md", f"{entry['id']}: ID/type/path mismatch")
        for field in ("id", "type", "status", "visibility"):
            require(data[field] == entry[field], f"{entry['path']}: metadata mismatch {field}")
        for ref in data["source_refs"]:
            repository_file(root, ref, f"{entry['path']}.source_refs")
        records[entry["id"]] = data
    actual = {p.relative_to(root).as_posix() for p in (root / "entities").rglob("*") if p.is_file()}
    require(actual == paths, f"entity/index coverage mismatch: unindexed={sorted(actual - paths)}, missing={sorted(paths - actual)}")

    archive_path = repository_file(root, idx["archive_index"], "index.archive_index")
    legacy = read_json(archive_path)
    keys(legacy, {"schema_version", "modules"}, "archive index")
    require(type(legacy["schema_version"]) is int and legacy["schema_version"] == 1, "archive: unsupported schema_version")
    require(isinstance(legacy["modules"], list), "archive.modules must be a list")
    archive_paths = set()
    for module in legacy["modules"]:
        keys(module, {"path", "title", "source", "authority"}, "archive module")
        path = repository_file(root, module["path"], "archive module.path")
        require(module["path"].startswith("archive/legacy-modules/") and path.suffix == ".md", "archive: invalid module path")
        require(module["path"] not in archive_paths, "archive: duplicate module path")
        archive_paths.add(module["path"])
        string(module["title"], "archive module.title")
        require(module["authority"] == "archival-only", "archive: invalid authority")
        source = string(module["source"], "archive module.source")
        require("/" not in source and "\\" not in source, "archive source must be a basename relative to archive/")
        repository_file(root, f"archive/{source}", "archive module.source")
    actual_archive = {p.relative_to(root).as_posix() for p in (root / "archive/legacy-modules").rglob("*.md")}
    require(archive_paths == actual_archive, "archive/index coverage mismatch")

    state = read_json(root / "state/checkpoint.json")
    validate_state(state)
    repository_file(root, state["source"], "checkpoint.source")
    for ident in state["context"]["companions_present"] + list(state["context"]["party_roles"]):
        require(ident in records, f"context: unknown companion/role entity {ident}")
    require(state["context"]["academy"]["entity"] in records, "context: missing academy entity")
    flat = {}
    for key, value in state.items():
        if isinstance(value, dict):
            flat.update({f"{key}.{k}": v for k, v in value.items()})
        elif key != "source":
            flat[key] = value
    owners = {k: set(v) for k, v in OWNERS.items()}
    if state["schema_version"] == 3:
        owners["party-finances"] = {f"money.{k}" for k in MONEY_FIELDS_V3}
        owners["theron-ashvale"] |= {f"resources.{k}" for k in RESOURCES}
    for entity_id, expected in owners.items():
        require(entity_id in records, f"missing authoritative snapshot entity: {entity_id}")
        values = records[entity_id].get("checkpoint_values")
        keys(values, expected, f"{entity_id}.checkpoint_values")
        for key, value in values.items():
            if key.startswith("money."):
                equal = copper(value, f"{entity_id}.{key}") == copper(flat[key], key)
            else:
                equal = type(value) is type(flat[key]) and value == flat[key]
            require(equal, f"checkpoint/entity mismatch: {entity_id} {key}")
    for entity_id, data in records.items():
        require(entity_id in OWNERS or "checkpoint_values" not in data,
                f"{entity_id}: unexpected checkpoint_values (declare ownership in validator)")
    return f"OK: {len(entries)} entity records, {len(archive_paths)} archived modules, checkpoint valid"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        print(validate(args.root))
    except (ValidationError, OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
