"""Fréquence des classes non nulles sous le nul global (aucun bras ne sépare), mode « R2 seul » (code v3,
`lecture_v3.calculer_r2`), données synthétiques du générateur des essais v1 (dimension sans objet : aucune activation),
2 000 tirages, 60 tâches, 5 plis. Aucune donnée de R1 ni de R2.

Usage : PYTHONPATH=src:tests python <ce fichier> <répliques> <entropie>
"""
import sys

import numpy as np

import test_analyse_principale_r1_r2_v1 as T
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K
from controle_ia.analyse_principale_r1_r2 import constantes_v3 as K3
from controle_ia.analyse_principale_r1_r2 import lecture_v1 as L1
from controle_ia.analyse_principale_r1_r2 import lecture_v3 as LR
from controle_ia.manifeste import graines

n_rep, entropie = int(sys.argv[1]), int(sys.argv[2])
K.TIRAGES = 2000
cles = [f"{a}-{b}" for a, b in K3.COMPARAISONS_PRINCIPALES + K3.COMPARAISONS_SECONDAIRES]
comptes = {k: {"supérieure": 0, "inférieure": 0, "non concluant": 0} for k in cles}
famille, fa = 0, []
for i in range(n_rep):
    d = T._donnees(entropie + i, w=0.0, g=0.0, j=0.0, cout=0.0, hc=0.0)
    n = d["tables"]["pas"].size
    j3 = {"score": d["juges"]["J3"][0], "score_generique": d["juges"]["J3"][1], "anomalie": np.zeros(n, bool),
          "anomalie_generique": np.zeros(n, bool)}
    j8 = {"score": d["juges"]["J8"][0], "anomalie": np.zeros(n, bool)}
    c = LR.calculer_r2({"tables": d["tables"]}, j3, j8, d["longueurs"], graines(list(K3.CLES_GRAINES), entropie * 1000 + i))
    p = L1._json(c["principale"])
    cl = {k: L1._classe(p, k, "1/100") for k in cles}
    for k, v in cl.items():
        comptes[k][v] += 1
    famille += any(cl[k] != "non concluant" for k in ("J3s-G", "J3s-T"))
    fa.append([p["bras"][b]["par_alpha"]["1/100"]["fausses_alarmes"] for b in ("J3s", "G", "T", "C")])
print(f"répliques {n_rep}, entropie {entropie}")
for k, v in comptes.items():
    print(f"{k} : {v} ; part non nulle {(v['supérieure'] + v['inférieure']) / n_rep:.3f}")
print(f"au moins une classe non nulle parmi J3s-G et J3s-T : {famille}/{n_rep} = {famille / n_rep:.3f}")
fa = np.array(fa)
print("fausses alarmes réalisées à 1 % (moyenne, écart type) J3s, G, T, C :",
      np.round(fa.mean(axis=0), 4).tolist(), np.round(fa.std(axis=0), 4).tolist())
