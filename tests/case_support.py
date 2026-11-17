"""Isolation for table-driven mutations sharing one disposable repository fixture.

Snapshots belong only to temporary roots, never the real campaign checkout.
Changes, deletions and new files are rolled back after every subcase, including
failed assertions. Scalar/container fixture attributes are also restored.
"""
from contextlib import contextmanager
import copy
from pathlib import Path
import tempfile


@contextmanager
def isolated_case(case):
    root=getattr(case,'root',None)
    files=None; directories=set()
    if isinstance(root,Path):
        if not root.resolve().is_relative_to(Path(tempfile.gettempdir()).resolve()):
            raise ValueError('subcase isolation requires a disposable temporary root')
        files={p.relative_to(root):('link',str(p.readlink())) if p.is_symlink() else ('file',p.read_bytes()) for p in root.rglob('*') if p.is_file() or p.is_symlink()}
        directories={p.relative_to(root) for p in root.rglob('*') if p.is_dir() and not p.is_symlink()}
    attributes={k:copy.deepcopy(v) for k,v in vars(case).items()
                if not k.startswith('_') and isinstance(v,(dict,list,set,str,int,float,bool,type(None)))}
    original_keys=set(vars(case))
    try:
        yield
    finally:
        if files is not None:
            current={p.relative_to(root):p for p in root.rglob('*') if p.is_file() or p.is_symlink()}
            for relative,p in current.items():
                if relative not in files:p.unlink()
            for relative,(kind,content) in files.items():
                p=root/relative
                if p.is_symlink():
                    if kind=='link' and str(p.readlink())==content:continue
                    p.unlink()
                if kind=='link':
                    if p.exists():p.unlink()
                    p.symlink_to(content)
                elif not p.is_file() or p.read_bytes()!=content:
                    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(content)
            # Remove empty directories created by a mutation too.
            for p in sorted(root.rglob('*'),key=lambda p:len(p.parts),reverse=True):
                if p.is_dir() and not p.is_symlink() and p.relative_to(root) not in directories and not any(p.iterdir()):p.rmdir()
        for k,v in attributes.items():setattr(case,k,v)
        for k in set(vars(case))-original_keys:
            if not k.startswith('_'):delattr(case,k)


_METADATA = {}


def validate_scope(root, *subsystems):
    """Unit boundary for JSON-only mutations, not a replacement for integration.

    Metadata is read fresh; identical frontmatter reuses its production-validated
    parse. Index/schema/metadata mutations must keep using validate(root).
    """
    import importlib
    import json
    from scripts.validate import frontmatter, require, repository_file, unique_json, ValidationError
    records={}
    for entry in json.loads((root/'index.json').read_text())['entries']:
        path=root/entry['path'];text=path.read_text();parts=text.split('---',2)
        header=parts[1] if len(parts)==3 and text.startswith('---\n') else text
        if header not in _METADATA:_METADATA[header]=frontmatter(path)
        records[entry['id']]=copy.deepcopy(_METADATA[header])
    functions={'travel':'validate_geography','settlements':'validate_settlements',
               'settlement_expansion':'validate_settlement_expansion','justice':'validate_justice',
               'guilds':'validate_guilds','guild_underworld':'validate_guild_underworld',
               'governments':'validate_governments','dungeon_designs':'validate_dungeon_designs',
               'economy':'validate_economy','autonomy':'validate_autonomy','quest_framework':'validate_quest_framework'}
    try:
        for subsystem in subsystems:
            fn=getattr(importlib.import_module('scripts.'+subsystem),functions[subsystem])
            fn(root,records,require,repository_file,unique_json)
    except ValueError as exc:
        raise ValidationError(str(exc)) from exc
