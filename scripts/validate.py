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
MONEY_FIELDS_V4 = {"total_gp_sp", "provisional_historic_gp_sp", "office_petty_gp_sp"}
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
    v5 = type(version) is int and version == 5
    v4 = type(version) is int and version == 4
    dated = v4 or v5
    modern = type(version) is int and version in {3, 4, 5}
    v3 = type(version) is int and version == 3
    keys(state, {"schema_version", "date", "time", "location", "theron", "money", "world", "status", "source", "context"} | ({"resources"} if modern else set()) | ({"calendar", "custody"} if dated else set()), "checkpoint")
    require(type(state["schema_version"]) is int and state["schema_version"] in {2, 3, 4, 5}, "checkpoint: unsupported schema_version")
    for field in ("date", "time", "location", "status", "source"):
        string(state[field], f"checkpoint.{field}")
    require(re.fullmatch(r"Year \d+ Day \d+", state["date"]) is not None, "checkpoint: invalid date")
    require(re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", state["time"]) is not None, "checkpoint: invalid time")
    require(state["status"] == ("ENDED" if v3 or v5 else "PAUSED"), "checkpoint: invalid session status")
    stats = state["theron"]
    keys(stats, STATS, "checkpoint.theron")
    for field in STATS - {"rank"}:
        integer(stats[field], f"checkpoint.theron.{field}", 1 if field in {"hp_max", "mp_max"} else 0)
    string(stats["rank"], "checkpoint.theron.rank")
    require(stats["hp"] <= stats["hp_max"], "checkpoint: HP exceeds maximum")
    require(stats["mp"] <= stats["mp_max"], "checkpoint: MP exceeds maximum")
    money_fields = MONEY_FIELDS_V4 if dated else MONEY_FIELDS_V3 if v3 else MONEY_FIELDS
    keys(state["money"], money_fields | ({"allocation_status"} if modern else set()) | ({"provisional_status", "office_status"} if dated else set()), "checkpoint.money")
    balances = {k: copper(state["money"][k], f"checkpoint.money.{k}") for k in money_fields}
    if modern:
        string(state["money"]["allocation_status"], "money.allocation_status")
        require(v5 or state["money"]["allocation_status"].startswith("unverified"), "money: allocation must remain explicitly unverified")
        if v3:
            require(balances["blackscale_private_gp_sp"] + balances["expedition_gp_sp"] <= balances["total_gp_sp"],
                    "checkpoint: verified components exceed controlled cash")
            require(balances["scene_opening_gp_sp"] + balances["scene_recovery_gp_sp"] - balances["scene_cost_gp_sp"] == balances["total_gp_sp"],
                    "checkpoint: currency total differs from final scene reconciliation")
        else:
            for field in ("provisional_status", "office_status"):
                string(state["money"][field], f"money.{field}")
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
    keys(context, {"safety", "companions_present", "party_roles", "projects", "academy", "outstanding_clues", "recent_mp_costs", "mp_before_recent_casts"} | ({"recent_mp_recovery"} if v4 else set()), "checkpoint.context")
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
    if dated:
        calendar = state["calendar"]
        keys(calendar, {"season", "day_of_season"}, "checkpoint.calendar")
        string(calendar["season"], "calendar.season")
        integer(calendar["day_of_season"], "calendar.day_of_season", 1)
        if v5:
            custody = state["custody"]
            keys(custody, {"reviewed", "released", "retained", "medically_transferred", "hearing_pending", "identities_status", "halden_status"}, "checkpoint.custody")
            for field in ("reviewed", "released", "retained", "medically_transferred"):
                integer(custody[field], f"custody.{field}")
            require(custody["reviewed"] == sum(custody[k] for k in ("released", "retained", "medically_transferred")), "custody: review counts do not sum")
            require(type(custody["hearing_pending"]) is bool, "custody: hearing_pending must be boolean")
            for field in ("identities_status", "halden_status"):
                string(custody[field], f"custody.{field}")
        else:
            custody = state["custody"]
            keys(custody, {"detainees", "guard", "free_people", "fatalities", "party_injuries"}, "checkpoint.custody")
            for field in ("detainees", "free_people"):
                require(isinstance(custody[field], list) and bool(custody[field]), f"custody.{field}: expected entries")
                for ident in custody[field]:
                    string(ident, f"custody.{field}")
                require(len(custody[field]) == len(set(custody[field])), f"custody.{field}: duplicate person")
            string(custody["guard"], "custody.guard")
            require(not set(custody["detainees"]) & set(custody["free_people"]), "custody: free people cannot be detainees")
            for field in ("fatalities", "party_injuries"):
                integer(custody[field], f"custody.{field}")
    costs = mapping(context["recent_mp_costs"], "context.recent_mp_costs")
    if v3 or v5:
        require(not costs and context["mp_before_recent_casts"] is None,
                "context: final-scene individual mana costs and starting MP remain unverified")
        return
    require(bool(costs), "context.recent_mp_costs: expected entries")
    for spell, cost in costs.items():
        string(spell, "spell name"); integer(cost, f"spell cost: {spell}")
    integer(context["mp_before_recent_casts"], "context.mp_before_recent_casts")
    require(context["mp_before_recent_casts"] <= stats["mp_max"], "recent starting MP exceeds maximum")
    recovery_amount = 0
    if v4:
        recovery = context["recent_mp_recovery"]
        keys(recovery, {"ability", "amount", "uninterrupted_minutes", "ambient_source_usable", "personal_only"}, "context.recent_mp_recovery")
        require(recovery["ability"] == "Spirit Mana Assimilation II", "recovery: unverified ability")
        integer(recovery["amount"], "recovery.amount")
        integer(recovery["uninterrupted_minutes"], "recovery.uninterrupted_minutes", 10)
        require(recovery["uninterrupted_minutes"] % 10 == 0, "recovery: incomplete uninterrupted interval")
        require(recovery["ambient_source_usable"] is True and recovery["personal_only"] is True,
                "recovery: usable ambient source and personal-only restoration required")
        require(recovery["amount"] == 24 * (recovery["uninterrupted_minutes"] // 10), "recovery: incorrect Assimilation II rate")
        recovery_amount = recovery["amount"]
    after_costs = context["mp_before_recent_casts"] - sum(costs.values())
    require(after_costs >= 0, "recent MP expenditure exceeds starting pool")
    require(min(stats["mp_max"], after_costs + recovery_amount) == stats["mp"], "recent MP expenditure/recovery does not match checkpoint")


def validate_finance_ledger(root, state):
    """Validate the separately authoritative current cash ledger, without floats."""
    ledger = read_json(root / "state/finance-ledger.json")
    keys(ledger, {"schema_version", "as_of", "source", "qualification", "currency", "controlled_cash", "operating_reconstruction", "distributions", "expense_history", "excluded_property", "assets_deposits_liabilities", "historical_discrepancies"}, "ledger")
    require(type(ledger["schema_version"]) is int and ledger["schema_version"] == 1, "ledger: unsupported schema_version")
    repository_file(root, ledger["source"], "ledger.source")
    require(ledger["source"] == state["source"], "ledger: source differs from checkpoint")
    require(ledger["as_of"] == dict(date=state["date"], season=state["calendar"]["season"], day_of_season=state["calendar"]["day_of_season"], time=state["time"], location=state["location"], session_status=state["status"]), "ledger: checkpoint date/status mismatch")
    require(ledger["currency"] == dict(unit="cp", cp_per_gp=100, cp_per_sp=10), "ledger: currency units differ")
    require("continuity reconstruction" in ledger["qualification"] and "not independently discovered historical receipts" in ledger["qualification"], "ledger: reconstruction qualification required")
    # All monetary fields must be nonnegative integer copper, including optional estimates.
    def check_amounts(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key.endswith("_cp") or key in {"revenue_cp_per_period", "expenses_cp_per_period"}:
                    if isinstance(item, dict):
                        for amount in item.values(): integer(amount, f"ledger.{key}")
                    elif item is not None:
                        integer(item, f"ledger.{key}", -10**12 if key == "delta_cp" else 0)
                check_amounts(item)
        elif isinstance(value, list):
            for item in value: check_amounts(item)
    check_amounts(ledger)
    cash = ledger["controlled_cash"]
    keys(cash, {"baseline_cp", "baseline_personal_purse_cp", "baseline_legacy_secured_cp", "total_cp", "accounts"}, "ledger.controlled_cash")
    accounts = cash["accounts"]
    require(isinstance(accounts, list) and bool(accounts), "ledger: accounts required")
    by_id = {}
    for account in accounts:
        keys(account, {"id", "owner", "balance_cp", "basis"}, "ledger.account")
        for field in ("id", "owner", "basis"): string(account[field], f"account.{field}")
        require(account["id"] not in by_id, "ledger: duplicate cash account")
        by_id[account["id"]] = account["balance_cp"]
    require(sum(by_id.values()) == cash["total_cp"] == copper(state["money"]["total_gp_sp"]), "ledger: account total differs from checkpoint")
    require(cash["baseline_personal_purse_cp"] + cash["baseline_legacy_secured_cp"] == cash["baseline_cp"], "ledger: baseline counted twice")
    model = ledger["operating_reconstruction"]
    keys(model, {"periods", "automatic_future_awards", "future_authorization", "merchant_eligible_gross_cp_per_period", "commission_percent", "revenue_cp_per_period", "expenses_cp_per_period", "estate_receipts_cp_per_period", "expenses_total_cp_per_period", "surplus_cp_per_period", "gross_estate_receipts_cp", "operating_expenses_cp", "net_distributable_surplus_cp"}, "ledger.operating_reconstruction")
    integer(model["periods"], "ledger.periods", 1)
    integer(model["commission_percent"], "ledger.commission_percent")
    require(model["automatic_future_awards"] is False, "ledger: automatic future awards forbidden")
    string(model["future_authorization"], "ledger.future_authorization")
    require(set(model["revenue_cp_per_period"]) == {"merchant_commissions", "lodge_rooms_and_meals", "rental_cottages", "merchant_storage_bays", "forge_and_repairs", "bakery", "caravan_and_stables", "healing_springs"}, "ledger: revenue categories differ")
    require(set(model["expenses_cp_per_period"]) == {"staff_wages", "supplies_and_materials", "maintenance", "fodder_and_fuel", "guards_and_security", "taxes_and_transport"}, "ledger: expense categories differ")
    require(model["merchant_eligible_gross_cp_per_period"] * model["commission_percent"] == model["revenue_cp_per_period"]["merchant_commissions"] * 100, "ledger: merchant commission differs")
    require(sum(model["revenue_cp_per_period"].values()) == model["estate_receipts_cp_per_period"], "ledger: revenue sum differs")
    require(sum(model["expenses_cp_per_period"].values()) == model["expenses_total_cp_per_period"], "ledger: expense sum differs")
    require(model["estate_receipts_cp_per_period"] - model["expenses_total_cp_per_period"] == model["surplus_cp_per_period"], "ledger: period surplus differs")
    for period, total in (("estate_receipts_cp_per_period", "gross_estate_receipts_cp"), ("expenses_total_cp_per_period", "operating_expenses_cp"), ("surplus_cp_per_period", "net_distributable_surplus_cp")):
        require(model[period] * model["periods"] == model[total], "ledger: eight-period totals differ")
    net = model["net_distributable_surplus_cp"]
    require(model["gross_estate_receipts_cp"] - model["operating_expenses_cp"] == net, "ledger: net surplus differs")
    dist = ledger["distributions"]
    keys(dist, {"application_count", "base", "allocations"}, "ledger.distributions")
    require(isinstance(dist["allocations"], list), "ledger: allocations must be a list")
    for allocation in dist["allocations"]:
        keys(allocation, {"account", "percent", "amount_cp"}, "ledger.allocation")
    require(type(dist["application_count"]) is int and dist["application_count"] == 1, "ledger: distribution must apply once")
    require(dist["base"] == "net_distributable_surplus_cp", "ledger: distribute net surplus only")
    allocations = dist["allocations"]
    allocation_ids = [a["account"] for a in allocations]
    require(len(allocation_ids) == len(set(allocation_ids)) and set(allocation_ids) == set(by_id) - {"legacy_secured"}, "ledger: allocation accounts differ")
    for a in allocations:
        integer(a["percent"], "ledger.allocation.percent")
        require(a["amount_cp"] * 100 == net * a["percent"], "ledger: allocation amount differs")
        opening = cash["baseline_personal_purse_cp"] if a["account"] == "personal_purse" else 0
        require(by_id[a["account"]] == opening + a["amount_cp"], "ledger: duplicate or missing allocation")
    require(sum(a["percent"] for a in allocations) == 100 and sum(a["amount_cp"] for a in allocations) == net, "ledger: distributions must sum to 100 percent and net")
    require(by_id["legacy_secured"] == cash["baseline_legacy_secured_cp"] and cash["baseline_cp"] + net == cash["total_cp"], "ledger: baseline or surplus double counted")
    history = ledger["expense_history"]
    keys(history, {"earlier_checkpoint_cp", "events", "private_expenses_already_deducted"}, "ledger.expense_history")
    require(isinstance(history["events"], list) and len(history["events"]) == 4, "ledger: repeated expense or surplus")
    require(history["private_expenses_already_deducted"] is True, "ledger: private expenses already deducted")
    running = history["earlier_checkpoint_cp"]
    for event in history["events"]:
        running += event["delta_cp"]
        require(running == event["balance_cp"], "ledger: expense history differs")
    require(running == cash["total_cp"], "ledger: expense history final total differs")
    require([e["delta_cp"] for e in history["events"]] == [-1200, -1900, 0, net], "ledger: repeated expense or surplus")
    require(history["events"][2]["transfer_cp"] == 1900 and history["events"][1]["balance_cp"] == cash["baseline_cp"], "ledger: internal transfer changes baseline")
    excluded = {e["id"]: e for e in ledger["excluded_property"]}
    require(len(excluded) == len(ledger["excluded_property"]) and set(excluded) == {"provisional_historic_coinage", "office_petty_cash", "lyanna_personal", "academy_cash", "academy_refundable_deposit", "seized_custody_funds", "merchant_property", "unreconciled_salvage", "estate_property"}, "ledger: excluded property coverage differs")
    for item in excluded.values():
        require(item["included_in_controlled_cash"] is False, "ledger: excluded property cannot enter controlled cash")
        string(item["status"], "ledger.excluded.status")
    for ident, field in (("provisional_historic_coinage", "provisional_historic_gp_sp"), ("office_petty_cash", "office_petty_gp_sp")):
        require(excluded[ident]["amount_cp"] == copper(state["money"][field]), "ledger: excluded holdings differ from checkpoint")
    for ident, field in (("academy_cash", "latest_reported_cash_gp_sp"), ("academy_refundable_deposit", "refundable_lease_deposit_gp_sp")):
        require(excluded[ident]["amount_cp"] == copper(state["context"]["academy"][field]), "ledger: academy holdings differ")
    assets = ledger["assets_deposits_liabilities"]
    require(assets["land_purchase"]["already_paid"] is True and assets["land_purchase"]["current_deduction_cp"] == 0, "ledger: land purchase already paid")
    require(assets["proposed_expansion"]["spent_cp"] == 0 and assets["proposed_expansion"]["payable"] is False and assets["night_sovereign"]["current_payable"] is False, "ledger: proposed estimates are not payables")
    require(len(ledger["historical_discrepancies"]) == 1, "ledger: historical discrepancy required")
    gap = ledger["historical_discrepancies"][0]
    require(gap["earlier_cp"] == 67390 and gap["later_cp"] == 54590 and gap["earlier_cp"] - gap["later_cp"] == gap["difference_cp"] == 12800, "ledger: historical discrepancy differs")
    require(gap["status"].startswith("OPEN") and gap["current_cash_adjustment_cp"] == 0, "ledger: historical discrepancy must stay open without adjustment")


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
    if state["schema_version"] == 4:
        custody = state["custody"]
        for ident in custody["detainees"] + custody["free_people"] + [custody["guard"]]:
            require(ident in records and records[ident]["type"] == "characters", f"custody: unknown character {ident}")
    if state["schema_version"] == 5:
        validate_finance_ledger(root, state)
    flat = {}
    for key, value in state.items():
        if isinstance(value, dict):
            flat.update({f"{key}.{k}": v for k, v in value.items()})
        elif key != "source":
            flat[key] = value
    owners = {k: set(v) for k, v in OWNERS.items()}
    if state["schema_version"] in {3, 4, 5}:
        money_fields = MONEY_FIELDS_V4 if state["schema_version"] in {4, 5} else MONEY_FIELDS_V3
        owners["party-finances"] = {f"money.{k}" for k in money_fields}
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
