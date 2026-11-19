"""Constat V5 : la garde d'identite de M8.1 (brouillon 2, « Metrique », point 7) peut-elle refuser une sonde juste quand
sa jumelle lui est presque identique ? Verificateur Claude Opus 5.5 ; lois inventees ; aucune donnee du programme.

Modele : 640 actions de la case HN. Score ferme de la sonde : s (loi normale reduite). Score ferme de sa jumelle :
s + t, t de loi normale d'ecart type tau (ecart sonde-jumelle, en ecarts types du score). Score relu de la sonde :
s + e, e de loi normale d'ecart type pi (changement de chemin et de machine). Autre sonde (autre dose ou autre pli) :
r * s + bruit, correlee a rho avec s. La garde (M8.1) exige, pour la sonde : Spearman(relu, ferme) >= 0,9 et
strictement plus grande que Spearman(relu, ferme d'une autre sonde ou jumelle). On compte les refus d'une sonde juste,
avec la propre jumelle dans la comparaison (texte du brouillon 2) et sans elle (couple V5).
Usage : ENTROPIE=<entier> python3 -B garde-identite-verification-v1.py <sortie .json>
"""
import json
import os
import sys

import numpy as np

ENT = int(os.environ["ENTROPIE"]) if os.environ.get("ENTROPIE") else np.random.SeedSequence().entropy
N, REP = 640, 2000


def rangs(x):
    r = np.empty_like(x)
    r[np.argsort(x, kind="stable")] = np.arange(len(x), dtype=float)
    return r


def spearman(a, b):
    ra, rb = rangs(a), rangs(b)
    ra, rb = ra - ra.mean(), rb - rb.mean()
    return float(ra @ rb / np.sqrt((ra @ ra) * (rb @ rb)))


out = dict(entropie=int(ENT), actions=N, jeux=REP, resultats=[])
for i, pi in enumerate((0.05, 0.2)):
    for j, tau in enumerate((0.0, 0.001, 0.01, 0.03, 0.1, 0.3)):
        g = np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=(i, j)))
        refus_avec, refus_sans = 0, 0
        for _ in range(REP):
            s = g.normal(size=N)
            jumelle = s + tau * g.normal(size=N)
            relu = s + pi * g.normal(size=N)
            rho = 0.8                                   # autre sonde, fortement correlee (dose voisine)
            autre = rho * s + np.sqrt(1 - rho ** 2) * g.normal(size=N)
            c_propre = spearman(relu, s)
            c_jumelle = spearman(relu, jumelle)
            c_autre = spearman(relu, autre)
            refus_avec += not (c_propre >= 0.9 and c_propre > c_jumelle and c_propre > c_autre)
            refus_sans += not (c_propre >= 0.9 and c_propre > c_autre)
        out["resultats"].append(dict(pi=pi, tau=tau, refus_avec_la_propre_jumelle=round(refus_avec / REP, 4),
                                     refus_sans_la_propre_jumelle=round(refus_sans / REP, 4)))
texte = json.dumps(out, indent=1, ensure_ascii=False)
print(texte)
open(sys.argv[1], "w", encoding="utf-8").write(texte + "\n")
