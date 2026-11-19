"""Applique les couples W-01 à W-03, E-01 à E-09 et T-01 à T-03 du rapport de vérification courte de la note v2
(côté exposé), dans l'ordre, chacun sur sa pièce ; chaque « avant » doit être présent une seule fois au moment de son
application, sinon arrêt sans rien écrire. Aucun autre changement.
Usage : python appliquer-couples-verification-v2-v1.py <rapport> <note v2> <extrait v1> <essais v1> <note v3> <extrait v2> <essais v2>
"""
import hashlib
import re
import sys
from pathlib import Path

rapport, note, extrait, essais, s_note, s_extrait, s_essais = sys.argv[1:8]
ATTENDU = {rapport: "52d64f44ab56b705fbcbdd8f2cb748ec8192464d6c4187f421dc1066f1df1674",
           note: "3262010b2493e7c1131d72f70deb3905f335d8c4a1d1f2b14428e1737bb9cce6",
           extrait: "e6172629ff71d6bf8486982e22b522ebd9f204f146dae3d935b634659d2e9ebd",
           essais: "29561a4ca49564b910baca3c60fcf0b73be252c176aceb0d9dd0c55151dcc87b"}
for p, h in ATTENDU.items():
    if hashlib.sha256(Path(p).read_bytes()).hexdigest() != h:
        raise SystemExit(f"{p} : empreinte ≠ {h[:12]}")
r = Path(rapport).read_text(encoding="utf-8")
corps = r.split("## 5. Couples exacts")[1].split("## 6. Remarques")[0]
parts = re.split(r"^### ([WET]-\d\d) — .*$", corps, flags=re.M)
couples = []
for i in range(1, len(parts), 2):
    blocs = re.findall(r"^~~~~\n(.*?)\n~~~~$", parts[i + 1], flags=re.S | re.M)
    if len(blocs) != 2:
        raise SystemExit(f"{parts[i]} : {len(blocs)} blocs lus (2 attendus)")
    couples.append((parts[i], blocs[0], blocs[1]))
attendus = [f"W-{k:02d}" for k in range(1, 4)] + [f"E-{k:02d}" for k in range(1, 10)] + [f"T-{k:02d}" for k in range(1, 4)]
if [c[0] for c in couples] != attendus:
    raise SystemExit(f"couples lus : {[c[0] for c in couples]}")
textes = {"W": Path(note).read_text(encoding="utf-8"), "E": Path(extrait).read_text(encoding="utf-8"),
          "T": Path(essais).read_text(encoding="utf-8")}
for nom, avant, apres in couples:
    t = textes[nom[0]]
    n = t.count(avant)
    if n != 1:
        raise SystemExit(f"{nom} : « avant » présent {n} fois")
    textes[nom[0]] = t.replace(avant, apres)
    print(f"{nom} appliqué")
for cle, s in (("W", s_note), ("E", s_extrait), ("T", s_essais)):
    if Path(s).exists():
        raise SystemExit(f"{s} existe déjà : R12")
for cle, s in (("W", s_note), ("E", s_extrait), ("T", s_essais)):
    Path(s).parent.mkdir(parents=True, exist_ok=True)
    Path(s).write_text(textes[cle], encoding="utf-8")
    print(s, hashlib.sha256(textes[cle].encode()).hexdigest())
