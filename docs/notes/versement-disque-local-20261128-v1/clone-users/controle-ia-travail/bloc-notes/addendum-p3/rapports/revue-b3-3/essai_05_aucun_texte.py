"""Essai 05 : aucun texte d'action dans la sortie, avec des marqueurs dans chaque champ, y compris le champ du coût
(lu par les règles (1), (2), la règle de sensibilité et le lecteur étendu), dans un titre, dans une clé en gras qui
diverge, et dans une action sans ligne ACTION. Recherche des marqueurs (et de leurs fragments) dans la sortie entière."""
import json

import numpy as np

import commun  # noqa: F401
from commun import cp, tc

MARQUES = ("qorvexcout", "plivtitre", "drumcontrole", "zelpredi", "snorkgras", "wuxsansaction")


def ecrire(i, c, cout):
    x = (f"ACTION: ADD\nTITLE: Measure {MARQUES[1]}\nPROPOSAL: Train a probe.\nCONTROLS: {MARQUES[2]} probes.\n"
         f"COST: {cout!r} {MARQUES[0]} (range 3-4) x 2\nPREDICTION: {MARQUES[3]} gain.")
    if c == "saboteur" and i % 5 == 0:
        x = x.replace("COST:", f"**COST:** {MARQUES[4]}\nCOST:", 1)
    if c == "temoin" and i % 7 == 0:
        x = x.replace("ACTION: ADD\n", f"{MARQUES[5]}\n", 1)
    return x


src = tc._complet(tc._varier(tc._source(0)), ecrire)
lec = tc._lecture(src)
s = cp.analyser_addendum(src, lec, tc.G)
texte = json.dumps(s, ensure_ascii=False)
trouves = [m for m in MARQUES if m in texte] + [m[:6] for m in MARQUES if m[:6] in texte]
t = src["tables"]
print(f"actions invalides {int((~t['valide'].astype(bool)).sum())} ; sortie {len(texte)} caractères ; "
      f"marqueurs trouvés dans la sortie : {trouves or 'aucun'}")
print("A5 comptes :", s["analyses"]["A5"][tc.P[0]]["descriptif"]["comptes"]["divergences_par_condition"])
assert not trouves
assert np.isfinite(len(texte))
