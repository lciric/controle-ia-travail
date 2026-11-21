# -*- coding: utf-8 -*-
"""Objet de contrôle du bloc D de calcul-poids-v1.py : fausse alerte du test du résidu sur un jeu nul
indépendant de celui qui fixe les seuils (bruit seul), et alerte sur une écriture nettement au-dessus du seuil.

Même modèle supposé que le bloc D : bruit i.i.d. gaussien d'écart sigma = 1 par coefficient, matrice n x n.
Seuils : quantile 99 % de 400 tirages nuls (graine A) ; contrôle : 400 tirages nuls neufs (graine B).
Attendu : environ 1 % d'alertes sur le jeu nul neuf pour chaque statistique (intervalle exact rapporté) ;
alerte spectrale proche de 100 % pour une écriture de rang un à theta = 1,5 sigma sqrt(n).
Commande : .venv/bin/python -I calcul-poids-v1-controle-nul.py > calcul-poids-v1-controle-nul.txt
"""
import math

import numpy as np
from scipy import stats

ENTROPIE = 202611211801
racine = np.random.SeedSequence(ENTROPIE)
graine_seuils, graine_nul, graine_vrai = racine.spawn(3)
print("numpy", np.__version__, "| SeedSequence racine, entropie =", racine.entropy)


def stat(R):
    return np.linalg.svd(R, compute_uv=False)[0], np.abs(R).max(), float((R * R).sum())


def nuls(n, rng, reps):
    return np.array([stat(rng.standard_normal((n, n))) for _ in range(reps)])


def cp(x, n):
    lo = stats.beta.ppf(0.025, x, n - x + 1) if x > 0 else 0.0
    hi = stats.beta.ppf(0.975, x + 1, n - x) if x < n else 1.0
    return lo, hi


for n in (256, 512):
    seuils = np.quantile(nuls(n, np.random.default_rng(graine_seuils), 400), 0.99, axis=0)
    neufs = nuls(n, np.random.default_rng(graine_nul), 400)
    alertes = (neufs > seuils).sum(axis=0)
    print(f"n = {n} : seuils 99 % (s1, max, énergie) = {seuils[0]:.2f}, {seuils[1]:.2f}, {seuils[2]:.0f}")
    for nom, x in zip(("plus grande valeur singulière", "plus grand coefficient", "énergie"), alertes):
        lo, hi = cp(int(x), 400)
        print(f"   objet faux (bruit seul, jeu neuf) — {nom:<30} : {int(x)}/400 = {x / 400:.2%} [IC 95 % {lo:.2%} ; {hi:.2%}]")
    rng = np.random.default_rng(graine_vrai)
    vrais = 0
    for _ in range(200):
        R = rng.standard_normal((n, n))
        u = rng.standard_normal(n); u /= np.linalg.norm(u)
        v = rng.standard_normal(n); v /= np.linalg.norm(v)
        R += 1.5 * math.sqrt(n) * np.outer(u, v)
        vrais += stat(R)[0] > seuils[0]
    print(f"   objet vrai (rang un, theta = 1,5 sigma sqrt(n)) — alerte spectrale : {vrais}/200")
