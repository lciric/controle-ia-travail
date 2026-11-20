"""Outil de développement (graines « essai », taille réduite, aucune sortie versée ; ce n'est pas l'audit de l'étape 3) : l'audit
de présentation sur les traits de forme, par paires de doses, sous plusieurs graines de validation croisée, et les traits de
forme dont la moyenne par monde diffère le plus entre doses (statistique t)."""
import sys

import numpy as np

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import audit as AU
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mondes as MO

g = GR.Graines()
n = int(sys.argv[2])
suites = [MO.generer_suite(g, dict(couche="essai", famille="diag-presentation", dose=d, source=k), d)
          for d in (0.0, 0.25, 0.5) for k in range(n)]
mondes = MO.mondes_pour_l_audit(suites)
for graine in range(5):
    pres = AU.audit_presentation(mondes, np.random.default_rng(100 + graine))
    print("graine", graine, {k: round(v, 3) for k, v in pres["exactitudes"]["forme"].items()})
X = {d: [] for d in (0.0, 0.25, 0.5)}
for m in mondes:
    X[m["dose"]].append(np.mean([AU.traits_de_forme(t) for t, _, _, _ in m["lois"]], axis=0))
for d1, d2 in ((0.0, 0.5), (0.0, 0.25), (0.25, 0.5)):
    a, b = np.array(X[d1]), np.array(X[d2])
    sd = np.sqrt(a.var(axis=0, ddof=1) / len(a) + b.var(axis=0, ddof=1) / len(b))
    t = np.where(sd > 0, (a.mean(axis=0) - b.mean(axis=0)) / np.where(sd > 0, sd, 1), 0)
    ordre = np.argsort(-np.abs(t))[:4]
    print(d1, d2, "traits", ordre.tolist(), "t", np.round(t[ordre], 2).tolist(), "longueur moyenne", round(a[:, -1].mean(), 2),
          round(b[:, -1].mean(), 2))
