"""Note d'interface v6 : applique à la v5 le couple accordé par la mère (clés de premier niveau de l'extrait des états,
message du 2026-11-19 vers 01:05Z) et, déclaré, le titre passé en « v6 » ; chaque « avant » présent une seule fois ; rien d'autre.
Usage : python … <note v5> <changements.json> <note v6>"""
import hashlib, json, sys
from pathlib import Path
v5, ch, v6 = sys.argv[1:4]
t = Path(v5).read_text(encoding="utf-8")
if hashlib.sha256(t.encode()).hexdigest() != "407099bc150b8730237cceb0c1cf051440e255b483f44461b38a6c835c13107f":
    raise SystemExit("note v5 : empreinte inattendue")
for k, (avant, apres) in enumerate(json.loads(Path(ch).read_text(encoding="utf-8")), 1):
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"changement {k} : « avant » présent {n} fois")
    t = t.replace(avant, apres)
    print(f"changement {k} appliqué")
if Path(v6).exists():
    raise SystemExit(f"{v6} existe déjà : R12")
Path(v6).write_text(t, encoding="utf-8")
print(v6, hashlib.sha256(t.encode()).hexdigest())
