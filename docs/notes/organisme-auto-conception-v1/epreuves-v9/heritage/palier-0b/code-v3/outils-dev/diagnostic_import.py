"""Outil de développement : quel module d'audit est importé, et ce que rend l'audit des marges sur deux lois trop proches."""
import sys

import numpy as np

from controle_ia.heritage_etage_processeur_v1 import audit as AU
from controle_ia.heritage_etage_processeur_v1 import lois as L

print(AU.__file__)
rng = np.random.default_rng(1)
Z, G = L.instances_oracle(3, 4000)
a = L.loi_aleatoire(rng)
b = {"type": "par_sous_population", "lois": {g: {"type": "softmax", "poids": [[w + 0.01 for w in ligne] for ligne in s["poids"]],
                                                 "biais": s["biais"]} for g, s in a["lois"].items()}}
print(AU.audit_marges({"A": a, "B": b}, Z, G))
