import re, sys
from datetime import date
from pathlib import Path
# toute ligne de tableau dont la première cellule ressemble à un GO de rang ≥ 3 chiffres (y compris ≥ 4, pour les voir)
L = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-(\d{3,}))\s*\|")
mauvaises, vues = [], 0
for n, ligne in enumerate(Path(sys.argv[1]).read_text(encoding="utf-8").splitlines(), 1):
    m = L.match(ligne)
    if not m:
        continue
    vues += 1
    c = [x.strip() for x in ligne.strip().strip("|").split("|")]
    pb = []
    if len(m.group(2)) > 3: pb.append("rang de quatre chiffres ou plus")
    if len(c) != 8:
        pb.append(f"{len(c)} colonnes")
    else:
        try: date.fromisoformat(c[1])
        except ValueError: pb.append(f"date d'accord illisible {c[1]!r}")
        if not (c[5] == "—" and c[2] != "calcul"):
            try: date.fromisoformat(c[5])
            except ValueError: pb.append(f"échéance illisible {c[5]!r} (type {c[2]!r})")
    print(f"ligne {n} {m.group(1)} type={c[2] if len(c)>2 else '?'} échéance={c[5] if len(c)>5 else '?'} -> {'OK' if not pb else pb}")
    if pb: mauvaises.append((n, m.group(1), pb))
print(f"\n{vues} lignes de rang >= 100 ; {len(mauvaises)} mal formées")
sys.exit(1 if mauvaises else 0)
