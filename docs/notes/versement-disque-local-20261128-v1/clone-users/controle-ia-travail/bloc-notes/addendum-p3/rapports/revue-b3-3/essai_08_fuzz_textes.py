"""Essai 08 : textes d'action tirés au hasard parmi des fragments de markdown et de clés (gras, italique, casse, puces,
REVISE sans numéro, clés vides, espaces insécables, chiffres non latins). `relire_textes` et `cout_lecteur_etendu` ne
doivent lever qu'une `GardeArret` (« échec » de la relecture) ; une autre exception (dont `DefautDuModule`) arrêterait
l'addendum entier sur un seul texte du run réel."""
import collections
import sys
import time

import numpy as np

import commun  # noqa: F401
from commun import cp

FRAGMENTS = ["ACTION: ADD\n", "ACTION: REVISE 2\n", "ACTION: REVISE\n", "**ACTION:** ADD\n", "action: add\n",
             "TITLE: t\n", "**TITLE:** t\n", "PROPOSAL: p\n", "__PROPOSAL__: p\n", "CONTROLS: c\n", "COST: 40\n",
             "**COST:** 40\n", "**COST**: 40\n", "**COST:**\n", "COST:\n", "Cost: 1 000\n", "- COST: 7\n", "1. COST: 8\n",
             "*COST*: 9\n", "***COST:***  12k\n", "_COST_ : 3\n", "COST :  \n", "**Cost** breakdown: 40\n",
             "COST: ١٢٣ hours\n", "COST: 2 500\n", "PREDICTION: x\n", "**PREDICTION:**", "**", "*", "_", ":", " ",
             "\n", "COST", "ACTION", "x", "**COST:**", "COST:**", ": ** :", " ", "COST: 1,000.5 (3-4) x 2\n"]
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
n = int(sys.argv[2]) if len(sys.argv) > 2 else 40_000
issues = collections.Counter()
exemples = {}
t0 = time.time()
for k in range(n):
    texte = "".join(FRAGMENTS[i] for i in rng.integers(0, len(FRAGMENTS), size=int(rng.integers(1, 14))))
    try:
        r = cp.relire_textes({"textes": [{"texte": texte}]})
        cp.cout_lecteur_etendu(r["champ_cout"][0])
        issues["ok"] += 1
    except cp.GardeArret as e:
        issues[f"GardeArret : {e}"] += 1
    except Exception as e:  # noqa: BLE001
        cle = f"{type(e).__name__} : {e}"
        issues[cle] += 1
        exemples.setdefault(cle, texte)
print(f"{n} textes en {time.time() - t0:.1f} s : {dict(issues)}")
for cle, texte in exemples.items():
    print("EXEMPLE", cle, repr(texte))
