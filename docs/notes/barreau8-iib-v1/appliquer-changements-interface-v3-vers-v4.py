"""Applique à la note d'interface v3 les changements demandés par la mère (message du 2026-11-19 vers 00:43Z), dans l'ordre,
chaque « avant » présent une seule fois ; rien d'autre. Usage : python … <note v3> <changements.json> <note v4>"""
import hashlib, json, sys
from pathlib import Path
v3, ch, v4 = sys.argv[1:4]
t = Path(v3).read_text(encoding="utf-8")
if hashlib.sha256(t.encode()).hexdigest() != "477815d1b48fc681ae4d403f81cf6f6fcff5750611e74f784db802013eed05f1":
    raise SystemExit("note v3 : empreinte inattendue")
for k, (avant, apres) in enumerate(json.loads(Path(ch).read_text(encoding="utf-8")), 1):
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"changement {k} : « avant » présent {n} fois")
    t = t.replace(avant, apres)
    print(f"changement {k} appliqué")
if Path(v4).exists():
    raise SystemExit(f"{v4} existe déjà : R12")
Path(v4).write_text(t, encoding="utf-8")
print(v4, hashlib.sha256(t.encode()).hexdigest())
