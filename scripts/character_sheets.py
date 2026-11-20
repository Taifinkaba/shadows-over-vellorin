"""Read supplemental reference sheets without changing checkpoint ownership."""

import re

HEADING = '\n\n## Character sheet\n'
NUMERIC_FIELDS = {
    'age', 'level', 'hp', 'hp_max', 'mp', 'mp_max', 'defense',
    'equipped_defense', 'str', 'dex', 'con', 'int', 'wis', 'cha',
    'unspent_attributes',
}
REQUIRED_FIELDS = NUMERIC_FIELDS | {
    'id', 'name', 'aliases', 'ancestry', 'sex', 'role', 'rank', 'skills',
    'abilities', 'equipment', 'mount', 'personal_cash', 'relationships',
    'assessment', 'recorded_context', 'source_refs',
}


def validate_sheet(root, path, ident, require, repository_file, load_yaml):
    """Validate a sheet when present, including during historical fixture runs."""
    contents = path.read_text()
    if HEADING not in contents:
        return
    _, _, section = contents.partition(HEADING)
    block = re.match(r'\n```yaml\n(.*?)\n```(?:\n|$)', section, re.S)
    require(block is not None and HEADING not in section,
            f'{ident}: expected one character sheet block')
    payload = load_yaml(block[1])
    require(isinstance(payload, dict) and set(payload) == {'character_sheet'},
            f'{ident}: invalid character sheet')
    sheet = payload['character_sheet']
    require(isinstance(sheet, dict) and REQUIRED_FIELDS <= sheet.keys(),
            f'{ident}: incomplete character sheet')
    require(sheet['id'] == ident and isinstance(sheet['name'], str) and sheet['name'].strip(),
            f'{ident}: character sheet identity mismatch')
    for field in NUMERIC_FIELDS:
        value = sheet[field]
        require(value is None or type(value) is int and value >= 0,
                f'{ident}: invalid {field} in character sheet')
    for resource in ('hp', 'mp'):
        value, maximum = sheet[resource], sheet[f'{resource}_max']
        require(value is None or maximum is not None and value <= maximum,
                f'{ident}: invalid {resource} pool in character sheet')
    refs = sheet['source_refs']
    require(isinstance(refs, list) and refs, f'{ident}: character sheet sources required')
    for ref in refs:
        repository_file(root, ref, f'{ident} character sheet source')
