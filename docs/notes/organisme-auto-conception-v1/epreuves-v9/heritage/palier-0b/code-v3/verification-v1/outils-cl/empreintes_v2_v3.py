"""Contre-lecteur : empreintes de sorties (graines « essai ») pour comparer deux paquets de code. Arguments : dossier racine
(contenant src et tests), dossier de travail neuf. Couche statistique : plusieurs proposeurs, doses, bras 1 a 4b ; couche
mecanique : le jeu a deux sources de la garde 27 (registres, mesures, entrees servies)."""
import hashlib
import json
import os
import sys

racine, travail = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(racine, "src"))
sys.path.insert(0, os.path.join(racine, "tests"))
import numpy as np
from aides_heritage_etage_processeur_v1 import FREQUENCES_D_ESSAI, graines, prop
from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
from controle_ia.heritage_etage_processeur_v1 import mondes as MO
from controle_ia.heritage_etage_processeur_v1 import statistique as ST


def h(x):
    return hashlib.sha256(x if isinstance(x, bytes) else json.dumps(x, sort_keys=True, default=str).encode()).hexdigest()[:16]


g = graines()
for nom, dose, kw in (("lecteur-heritage", 0.5, {"K": 128}), ("lecteur-heritage", 0.25, {"K": 64}),
                      ("lecteur-tenue", 0.25, {"tau": 2.0}), ("sourd-paie", 0.5, {}), ("copieur", 0.25, {}),
                      ("suiveur-lettre", 0.25, {"phi": 1.0}), ("generaliste", 0.0, {"gamma": 0.5})):
    bras = ("1", "2", "3", "4a", "4b") if dose > 0 else ("2", "3")
    f = dict(FREQUENCES_D_ESSAI)
    r = ST.simuler({b: g.g(couche="essai", famille="cmp", proposeur=nom, dose=dose, bras=b, role="echantillonnage") for b in bras},
                   g.g(couche="essai", famille="cmp", proposeur=nom, dose=dose, role="monde"),
                   g.g(couche="essai", famille="cmp", proposeur=nom, dose=dose, role="source"), prop(nom, **kw), dose, 0.25, f, 400)
    for b in bras:
        for c in ("M1", "D", "I", "fausses_tenues"):
            print("stat", nom, dose, b, c, h(np.ascontiguousarray(r["bras"][b][c]).tobytes()))
bases = [dict(couche="essai", famille="cmp-meca", proposeur="lecteur-tenue", dose=0.25, source=k) for k in range(2)]
suites = MO.generer_jeu_avec_etrangeres(g, bases, 0.25)
premieres, secondes = MC.jouer_jeu_diagnostic(g, bases, prop("lecteur-tenue", tau=2.0), 0.25, 0.25, travail, suites)
for k, lot in enumerate(premieres + secondes):
    for b, v in lot["bras"].items():
        print("meca", k, b, h(v["registre"].octets()), h(v["mesure"]), h(v["entrees_servies"]), h(v["reliquats"]))
