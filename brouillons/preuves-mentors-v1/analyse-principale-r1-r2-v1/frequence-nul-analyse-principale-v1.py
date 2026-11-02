"""Fréquence des classes non nulles sous le nul global (aucun bras ne sépare), règle de l'analyse principale de R1-R2
(code `src/controle_ia/analyse_principale_r1_r2/`, données synthétiques du générateur des essais, dimension 16,
2 000 tirages, 60 tâches, 5 plis). Sortie : comptes par comparaison et au moins une classe non nulle parmi les deux
principales (Bonferroni, 97,5 %). Aucune donnée de R1 ni de R2.

Usage : PYTHONPATH=src:tests python <ce fichier> <répliques> <entropie>
"""
import sys

import numpy as np

import test_analyse_principale_r1_r2_v1 as T
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K
from controle_ia.analyse_principale_r1_r2 import lecture_v1 as LP
from controle_ia.manifeste import graines

n_rep, entropie = int(sys.argv[1]), int(sys.argv[2])
K.DIMENSION, K.TIRAGES, K.N_PLANCHER = T.D, 2000, 50
comptes = {k: {"supérieure": 0, "inférieure": 0, "non concluant": 0} for k in ("W-G", "W-J3s", "W-T", "W-J8s")}
famille, fa = 0, []
for i in range(n_rep):
    d = T._donnees(entropie + i, w=0.0, g=0.0, j=0.0, cout=0.0, hc=0.0)
    t = d["tables"]
    notee = t["jetons_notes"] > 0
    communs = {"fidele": notee, "contexte_conforme": np.ones(notee.size, bool)}
    r1 = {"tableaux": {k: v.astype(np.float16) for k, v in d["acts"].items()}, "communs": communs,
          "resultat": {"regle_repli_appliquee": False}}
    j = {"score": d["juges"]["J3"][0], "score_generique": d["juges"]["J3"][1], "anomalie": np.zeros(notee.size, bool),
         "anomalie_generique": np.zeros(notee.size, bool)}
    j8 = {"score": d["juges"]["J8"][0], "anomalie": np.zeros(notee.size, bool)}
    g = graines(list(K.CLES_GRAINES), entropie * 1000 + i)
    c = LP.calculer({"tables": t}, r1, j, j8, d["longueurs"], g)
    p = c["principale"]
    cl = {k: LP._classe(LP._json(p), k, "1/100") for k in comptes}
    for k, v in cl.items():
        comptes[k][v] += 1
    famille += any(cl[k] != "non concluant" for k in ("W-G", "W-J3s"))
    fa.append([p["bras"][b]["par_alpha"]["1/100"]["fausses_alarmes"] for b in ("W", "G", "J3s", "T")])
print(f"répliques {n_rep}, entropie {entropie}")
for k, v in comptes.items():
    print(f"{k} : {v} ; part non nulle {(v['supérieure'] + v['inférieure']) / n_rep:.3f}")
print(f"au moins une classe non nulle parmi W-G et W-J3s : {famille}/{n_rep} = {famille / n_rep:.3f}")
fa = np.array(fa)
print("fausses alarmes réalisées à 1 % (moyenne, écart type) W, G, J3s, T :",
      np.round(fa.mean(axis=0), 4).tolist(), np.round(fa.std(axis=0), 4).tolist())
