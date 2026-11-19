"""Contre-lecteur Opus 5.5 : fréquence d'une égalité entre le k-ième et le (k+1)-ième plus grand score d'une direction, en simple
précision, dans un modèle de scores indépendants de loi normale (moyenne mu, écart type sigma). Méthode à moi, distincte de celle de
l'auteur : on tire seulement le (k+1)-ième plus grand score y (représentation de Rényi, exacte : 1 − U = Gamma(k+1) / Gamma(n+1)),
puis la probabilité d'égalité sachant y est calculée exactement : les k scores au-dessus de y sont indépendants, de loi normale
tronquée à y, et l'égalité a lieu si et seulement si le plus petit d'entre eux tombe sous le bord supérieur e de la cellule
d'arrondi de y : P = 1 − (survie(e) / survie(y))^k. La variance de Monte-Carlo est donc très faible (aucun événement rare compté).
Contrôle de la méthode : tirage direct de n scores, arrondis à un pas grossier (1e-3), contre la même formule à ce pas.
Données synthétiques seulement. Graines : numpy.random.SeedSequence(entropy=E4, spawn_key=(i,)).
Usage : python -B egalite_rang_k_contre_lecteur.py E4"""
import sys

import numpy as np
from scipy import special

E4 = int(sys.argv[1])


def gen(i):
    return np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=E4, spawn_key=(i,))))


def y_rang(g, n, k, taille):
    """(k+1)-ième plus grand de n normales centrées réduites, exact : survie = Gamma(k+1) / Gamma(n+1)."""
    gk = g.standard_gamma(k + 1, size=taille)
    gn = gk + g.standard_gamma(n - k, size=taille)          # Gamma(n+1) = Gamma(k+1) + Gamma(n−k), indépendants
    return -special.ndtri(gk / gn)


def p_egalite(y, k, mu=0.0, sigma=1.0, pas=None):
    """Probabilité d'égalité sachant y (échelle réduite) : scores observés mu + sigma·x, arrondis en simple précision
    (ou à un pas fixe si `pas`)."""
    s = mu + sigma * y
    if pas is None:
        v = s.astype(np.float32)
        haut = np.nextafter(v, np.float32(np.inf))
        e = (v.astype(np.float64) + haut.astype(np.float64)) / 2
    else:
        v = np.round(s / pas) * pas
        e = v + pas / 2
    xe = (e - mu) / sigma
    d = special.log_ndtr(-xe) - special.log_ndtr(-y)
    return -np.expm1(k * d)


def main():
    n_j, k = 89_498, 20
    # Contrôle de la méthode : tirage direct, pas 1e-3
    g = gen(1)
    n0, pas, eg = 3_000, 1e-3, 0
    for _ in range(n0):
        x = np.round(g.standard_normal(n_j) / pas)
        haut = np.partition(x, n_j - 21)[n_j - 21:]
        haut.sort()
        eg += int(haut[0] == haut[1])
    y = y_rang(gen(2), n_j, k, 2_000_000)
    print(f"contrôle, pas 1e-3, n = {n_j}, k = {k} : tirage direct {eg}/{n0} = {eg / n0:.4f} (± {np.sqrt(eg) / n0:.4f}) ; "
          f"formule {p_egalite(y, k, pas=pas).mean():.4f}")
    # Simple précision, scores centrés réduits, et décalés
    y = y_rang(gen(3), n_j, k, 4_000_000)
    for mu in (0.0, 10.0, 100.0):
        p = p_egalite(y, k, mu=mu)
        print(f"simple précision, n = {n_j}, k = {k}, moyenne {mu:g} écarts types : {p.mean():.3e} par liste "
              f"(± {p.std() / np.sqrt(p.size):.1e}) ; attendu sur 195 000 listes {195_000 * p.mean():.2f} ; "
              f"P(au moins une) {-np.expm1(-195_000 * p.mean()):.3f}")
    # Échelle : la fréquence dépend de la place du score de rang 20 dans sa puissance de deux
    ps = []
    for j in range(16):
        sigma = 2 ** (j / 16)
        ps.append((sigma, p_egalite(y[:1_000_000], k, sigma=sigma).mean()))
    lo, hi = min(p for _, p in ps), max(p for _, p in ps)
    print(f"simple précision, scores centrés, écart type de 1 à 2 (16 valeurs) : de {lo:.2e} à {hi:.2e} par liste ; "
          f"sur 195 000 listes, de {195_000 * lo:.2f} à {195_000 * hi:.2f} égalités attendues")
    # Listes de dix : pôles (57 344 cosinus signés) et lecture d'un pôle (89 498 jetons)
    for cle, n, kk, nom in ((5, 57_344, 10, "dix pôles parmi 57 344"), (6, 89_498, 10, "dix premiers jetons d'une lecture de pôle")):
        yy = y_rang(gen(cle), n, kk, 2_000_000)
        p = p_egalite(yy, kk)
        print(f"simple précision, {nom} (rang {kk}) : {p.mean():.2e} par liste (± {p.std() / np.sqrt(p.size):.1e})")


main()
