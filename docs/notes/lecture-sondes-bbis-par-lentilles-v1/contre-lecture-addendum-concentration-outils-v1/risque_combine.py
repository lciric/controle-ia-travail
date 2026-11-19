"""Risque de sortie d'une calibration saine quand la part vraie est déplacée ET le compte sur-dispersé (contre-lecteur)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from bornes_independantes import bb_float, compte, bornes, bb_exact
R0 = 100 / 2001
def risque(k, n, r, f):
    S0 = 2001
    base = compte(k, bb_exact(n, 100, 1901)); qb, qh, _, _ = bornes(base)
    cible = f * (S0 + n) / (S0 + 1); S = (n - cible) / (cible - 1)
    p = compte(k, bb_float(n, S * r, S * (1 - r)))
    return qb, qh, float(p[:qb].sum() + p[qh + 1:].sum())
for k, n in [(1, 1000), (6, 200), (13, 200), (20, 200), (40, 200)]:
    out = []
    for r, f in [(R0, 1.05), (R0 * 0.995, 1.05), (R0 * 0.98, 1.05), (R0 * 0.98, 1.10), (R0 * 0.97, 1.10)]:
        qb, qh, x = risque(k, n, r, f)
        out.append(f"part×{r / R0:.3f}, variance×{f:.2f} : {x:.2e}")
    print(f"{k} jeu(x) de {n} [{qb}, {qh}] : " + " ; ".join(out))
