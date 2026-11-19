import sys, tempfile
from pathlib import Path
from controle_ia.barreau8_moniteurs import passe_recalcul_v2 as P
from controle_ia.gardes import GardeArret
base = Path(tempfile.mkdtemp(dir="."))
racine = base / "depot"; racine.mkdir()
sortie = base / "passe-iib-sortie"   # nom de sortie plausible chez l'exécutante
t = P.TraceGardes()
s = P.SurveillanceLectures(t, [], [sortie], [racine])
sortie.mkdir()
with P.surveiller(s):
    try:
        (sortie / "x.npz").write_bytes(b"1")
        print("écriture permise")
    except GardeArret as e:
        print("REFUS :", e, "| P8 :", t.etat("P8"), "| prive :", s.prive)
