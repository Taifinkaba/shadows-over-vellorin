from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
idx=json.loads((root/'index.json').read_text(encoding='utf-8'))
entries=idx['entries']; ids=[x['id'] for x in entries]; paths=[x['path'] for x in entries]
assert len(ids)==len(set(ids)), 'duplicate entity ID'
assert len(paths)==len(set(paths)), 'duplicate path'
for e in entries:
 p=root/e['path']; assert p.is_file(),f'missing {p}'
 text=p.read_text(encoding='utf-8')
 for k,v in [('id',e['id']),('type',e['type']),('status',e['status']),('visibility',e['visibility'])]:
  assert re.search(r'^'+k+r': '+re.escape(v)+r'$',text,re.M),f'{p}: metadata mismatch {k}'
 for ref in re.findall(r'^  - "([^"]+)"$',text,re.M):
  assert (root/ref).is_file(),f'{p}: missing source {ref}'
state=json.loads((root/'state/checkpoint.json').read_text(encoding='utf-8'))
assert state['status']=='PAUSED'
assert 0<=state['theron']['hp']<=state['theron']['hp_max']
assert 0<=state['theron']['mp']<=state['theron']['mp_max']
assert state['world']['junctions_tested']+state['world']['junctions_untested']==7
print(f'OK: {len(entries)} entity records, {len(list((root/"archive/legacy-modules").rglob("*.md")))} archived modules, checkpoint valid')
