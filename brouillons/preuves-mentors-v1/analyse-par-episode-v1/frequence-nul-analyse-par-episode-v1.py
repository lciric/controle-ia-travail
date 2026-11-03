"""Fréquence des classes non « non concluant » sous le nul global (aucun bras ne sépare), lecture par épisode de R1-R2
(contre-lecture, C4) : code v5 (`lecture_v5.calculer` ; calcul par épisode du code v4 inchangé), données synthétiques du
générateur des essais v1 de la principale (dimension 16 ; saboteur, mention, coût, juges et G sans effet), 2 000 tirages,
60 tâches, 5 plis, plancher sur 50 directions (sans effet sur les classes), rang 1 (1/49).
Sortie : comptes des classes par comparaison (W − G, W − J3s, W − T, W − J8s), au moins une classe non nulle parmi les
deux principales (Bonferroni, 97,5 %), fausses alarmes par épisode (sur 60 honnêtes) par bras : moyenne, P(> 4), P(= 0),
maximum. Aucune donnée de R1, R2, R4 ni de P3.

Usage : PYTHONPATH=src:tests nice -n 10 python <ce fichier> <répliques> <entropie>
"""
import sys

import numpy as np

import test_analyse_principale_r1_r2_v1 as T
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K
from controle_ia.analyse_principale_r1_r2 import constantes_v4 as K4
from controle_ia.analyse_principale_r1_r2 import lecture_v4 as L4
from controle_ia.analyse_principale_r1_r2 import lecture_v5 as LE5
from controle_ia.manifeste import graines

n_rep, entropie = int(sys.argv[1]), int(sys.argv[2])
K.DIMENSION, K4.TIRAGES, K4.N_PLANCHER = T.D, 2000, 50
comparaisons = ("W-G", "W-J3s", "W-T", "W-J8s")
comptes = {k: {"supérieure": 0, "inférieure": 0, "non concluant": 0, "non lue": 0} for k in comparaisons}
famille, fa = 0, {b: [] for b in K4.BRAS}
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
    g = graines(list(K4.CLES_GRAINES), entropie * 1000 + i)
    c = LE5.calculer({"tables": t}, r1, j, j8, d["longueurs"], g, entropie * 1000 + 500 + i)
    p = c["principale_bras"]
    cl = {k: L4._classe(p, k, "1/100") for k in comparaisons}
    for k, v in cl.items():
        comptes[k][v] += 1
    famille += any(cl[k] != "non concluant" for k in ("W-G", "W-J3s"))
    for b in K4.BRAS:
        fa[b].append(p["bras"][b]["par_alpha"]["1/100"]["fausses_alarmes_compte"])
print(f"répliques {n_rep}, entropie {entropie}, numpy {np.__version__}")
for k, v in comptes.items():
    print(f"{k} : {v} ; part non nulle {(v['supérieure'] + v['inférieure']) / n_rep:.3f}")
print(f"au moins une classe non nulle parmi W-G et W-J3s : {famille}/{n_rep} = {famille / n_rep:.3f}")
for b, v in fa.items():
    v = np.array(v)
    print(f"fausses alarmes par épisode (sur 60), {b} : moyenne {v.mean():.3f} (60/49 = 1.224) ; P(>4) {np.mean(v > 4):.3f} ; "
          f"P(=0) {np.mean(v == 0):.3f} ; max {v.max()}")
