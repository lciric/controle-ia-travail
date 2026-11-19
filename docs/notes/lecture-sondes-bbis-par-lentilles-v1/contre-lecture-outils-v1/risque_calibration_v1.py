"""Probabilité que la calibration du texte sorte de ses bornes quand le taux réel de p ≤ 0,05 sous le nul vaut r au lieu de
100/2 001 (calcul exact par lois bêta-binomiales ; aucun code du paquet contre-lu ; aucune donnée).
Bornes : comme le texte (q_bas le plus grand entier tel que P(X < q_bas) ≤ 10⁻⁴ ; q_haut le plus petit tel que
P(X > q_haut) ≤ 10⁻⁴, loi bêta-binomiale (n ; 100 ; 1 901), sommes pour des jeux mis en commun).
Loi sous le biais : chaque jeu, bêta-binomiale (n ; r·2 001 ; (1 − r)·2 001) (même dispersion, moyenne déplacée)."""
import numpy as np
from scipy.stats import betabinom

M, NIV = 2000, 1e-4


def pmf(jeux, a, b):
    p = np.array([1.0])
    for n in jeux:
        p = np.convolve(p, betabinom.pmf(np.arange(n + 1), n, a, b))
    return p


def bornes(p):
    c = np.concatenate([[0.0], np.cumsum(p)])            # c[q] = P(X < q)
    bas = max(q for q in range(len(p) + 1) if c[q] <= NIV)
    queue = 1 - np.cumsum(p)                              # queue[q] = P(X > q)
    haut = min(q for q in range(len(p)) if queue[q] <= NIV)
    return bas, haut


print("jeux | bornes | P(hors bornes) pour r = 0,0500 / 0,0550 / 0,0580 / 0,0605 / 0,0650 / 0,0700")
for nom, jeux in [("isotrope, 1 000", [1000])] + [(f"signes, {k} × 200", [200] * k) for k in (1, 3, 5, 6, 10, 13, 20, 30, 40)]:
    bas, haut = bornes(pmf(jeux, 100, 1901))
    risques = []
    for r in (100 / 2001, 0.055, 0.058, 0.0605, 0.065, 0.07):
        p = pmf(jeux, r * (M + 1), (1 - r) * (M + 1))
        risques.append(p[:bas].sum() + p[haut + 1:].sum())
    print(f"{nom} | [{bas}, {haut}] | " + " / ".join(f"{x:.4f}" for x in risques))
