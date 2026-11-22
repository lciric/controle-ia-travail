"""Validité approchée de la statistique corrigée de l'addendum « concentration » — calcul exact dans le modèle gaussien, v2.

Modèle : T jetons de scores gaussiens indépendants, de même loi d'une direction à l'autre (aucune donnée ; un modèle d'école).
Lois exactes du z d'un jeton :
  - direction lue v (ou témoin), jugée sur M directions nulles (écart type de population) : racine((M+1)/(M−1)) × Student(M−1) ;
  - direction nulle jugée sur les M − 1 autres (statistique corrigée)                    : racine(M/(M−2)) × Student(M−2) ;
  - direction nulle jugée avec elle-même (texte v1) : d, avec z_corrigé = d·racine(M/(M−1)) / racine(1 − d²/(M−1)).
La concentration est le maximum sur T jetons indépendants. Le taux rendu est P(p ≤ k/(M+1)) = P(C(v) dépasse la kᵉ plus grande
concentration nulle), calculé en tenant les M concentrations nulles pour indépendantes (approximation « marginale » : la
dépendance qu'elles tirent du jeu de référence partagé est ignorée ici, et mesurée par la simulation jointe).
Sorties : écart relatif au niveau nominal, multiplié par M (texte v1) et par M² (statistique corrigée).
Usage : python -I -B validite_gaussienne_statistique_corrigee_v2.py
"""
import sys
from datetime import datetime, timezone

import numpy as np
import scipy
from scipy import stats

NOEUDS, POIDS = np.polynomial.legendre.leggauss(600)
W = 0.5 * (NOEUDS + 1.0)                      # nœuds sur ]0, 1[
PW = 0.5 * POIDS


def survie_max_lue(c, M, T):
    """P(C(v) > c) : maximum de T z de la direction lue, jugée sur M directions nulles."""
    q = stats.t.sf(c * np.sqrt((M - 1) / (M + 1)), M - 1)
    return -np.expm1(T * np.log1p(-q))


def quantile_nul(u, M, T, statistique):
    """Valeur c telle que P(concentration nulle > c) = u."""
    q = -np.expm1(np.log1p(-u) / T)           # survie par jeton
    z = np.sqrt(M / (M - 2)) * stats.t.isf(q, M - 2)     # statistique corrigée
    if statistique == "corrigee":
        return z
    return z * np.sqrt((M - 1) / (M + z * z))            # texte v1 : d tel que phi(d) = z


def taux(M, T, k, statistique):
    """Écart E[S_v(q(U)) − U], U ~ bêta(k ; M + 1 − k) : taux moins niveau nominal k/(M+1)."""
    u = stats.beta.ppf(W, k, M + 1 - k)
    ecart = survie_max_lue(quantile_nul(u, M, T, statistique), M, T) - u
    return float((PW * ecart).sum())


if __name__ == "__main__":
    print(f"commande : python -I -B validite_gaussienne_statistique_corrigee_v2.py (python {sys.version.split()[0]}, numpy "
          f"{np.__version__}, scipy {scipy.__version__}, {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')})")
    print("A. Taille du texte : T = 89 498 jetons gardés, M = 2 000")
    T, M = 89_498, 2000
    for nom, k in (("p ≤ 0,05", 100), ("p ≤ 0,01", 20), ("p ≤ 0,001", 2)):
        nominal = k / (M + 1)
        e1, e2 = taux(M, T, k, "v1"), taux(M, T, k, "corrigee")
        print(f"  {nom} (k = {k}, nominal {nominal:.6f}) : texte v1 {nominal + e1:.6f} (rapport {1 + e1 / nominal:.4f}) ; "
              f"corrigée {nominal + e2:.9f} (écart relatif {e2 / nominal:+.3e}, soit {e2 / nominal * M * M:+.1f} / M²)")
    print("B. Ordre en M, à T = 89 498, niveau 0,05 (k = 0,05 × (M + 1) arrondi) : écart relatif × M (v1), × M² (corrigée)")
    for M in (250, 500, 1000, 2000, 4000, 8000, 16000):
        k = round(0.05 * (M + 1))
        nominal = k / (M + 1)
        e1, e2 = taux(M, T, k, "v1"), taux(M, T, k, "corrigee")
        print(f"  M = {M:>5} (k = {k:>3}) : v1 {e1 / nominal:+.4e} = {e1 / nominal * M:+.1f} / M ; "
              f"corrigée {e2 / nominal:+.4e} = {e2 / nominal * M * M:+.1f} / M²")
    print("C. Tailles de la simulation jointe (T = 128 ; niveau 0,05 exact : k = (M + 1)/20)")
    T = 128
    for M in (19, 39, 79, 159):
        k = (M + 1) // 20
        nominal = k / (M + 1)
        e1, e2 = taux(M, T, k, "v1"), taux(M, T, k, "corrigee")
        print(f"  M = {M:>3} (k = {k}) : v1 {nominal + e1:.5f} ; corrigée {nominal + e2:.5f} "
              f"(écart {e2:+.2e} = {e2 / nominal * M * M:+.1f} / M² en relatif)")
    print("D. Taille de la simulation du compte (T = 1 024, M = 2 000, k = 100)")
    T, M, k = 1024, 2000, 100
    nominal = k / (M + 1)
    e1, e2 = taux(M, T, k, "v1"), taux(M, T, k, "corrigee")
    print(f"  v1 {nominal + e1:.6f} ; corrigée {nominal + e2:.9f} (nominal {nominal:.6f})")
    print("E. Part au-dessus du nul, par jeton, scores de loi uniforme, quantile 0,99 par interpolation linéaire : "
          "P(dépasser le quantile de n autres) = 0,01 + 0,98/(n + 1)")
    M = 2000
    print(f"  direction lue (n = M = 2 000) : {0.01 + 0.98 / (M + 1):.9f} ; nulle sans elle-même (n = M − 1) : "
          f"{0.01 + 0.98 / M:.9f} ; écart {0.98 / M - 0.98 / (M + 1):+.3e} = 0,98/(M(M+1)) ; nulle avec elle-même (v1) : "
          f"{20 / M:.9f} (rang ≥ 1 981 sur 2 000)")
