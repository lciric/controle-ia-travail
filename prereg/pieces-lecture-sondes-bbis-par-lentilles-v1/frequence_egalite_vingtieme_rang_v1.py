"""Ordre de grandeur de la fréquence d'une égalité de score entre le vingtième et le vingt-et-unième jeton, en simple précision.

Données synthétiques seulement : aucune sonde, aucune lentille, aucun score réel.
Modèle : les scores des n = 89 498 jetons d'une direction sont indépendants, de loi normale (moyenne mu, écart type 1), puis
arrondis en simple précision. Les 21 plus grands sont tirés par leurs statistiques d'ordre (espacements exponentiels de la loi
uniforme), ce qui évite de tirer les 89 498 scores. Partie 0 : contrôle de la méthode contre un tirage direct, à un pas d'arrondi
grossier (1e-3), où les égalités sont assez fréquentes pour être comptées.
Graines : numpy.random.SeedSequence(entropy=E, spawn_key=(entier des 8 premiers octets du SHA-256 de la clé,)), PCG64 (R9).
"""
import hashlib
import sys
from statistics import NormalDist

import numpy as np

E = 207246359357165180107189867815730235805  # entropie du texte scellé de la lecture
N_JETONS = 89_498
ND = NormalDist()


def gen(cle):
    k = int.from_bytes(hashlib.sha256(cle.encode()).digest()[:8], "big")
    return np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=E, spawn_key=(k,))))


def queue_normale(u):
    """Quantile supérieur de la loi normale (u petit), par l'inverse de la fonction de répartition de la bibliothèque standard."""
    plat = u.ravel()
    return np.fromiter((ND.inv_cdf(1.0 - x) for x in plat), dtype=np.float64, count=plat.size).reshape(u.shape)


def rangs_20_21(g, n_dir):
    esp = g.standard_exponential((n_dir, 21))
    u = np.cumsum(esp, axis=1)[:, 19:21] / (N_JETONS + 1)
    return queue_normale(u)  # colonnes : vingtième et vingt-et-unième plus grands scores


def main():
    n_dir = int(sys.argv[1])
    # Partie 0 : contrôle de la méthode, pas d'arrondi 1e-3
    g = gen("lentilles-bbis/addendum-concentration-v1/egalite-vingtieme-rang/controle-direct")
    n0, pas, eg_direct = 4_000, 1e-3, 0
    for _ in range(n0):
        x = np.round(g.standard_normal(N_JETONS) / pas)
        haut = np.partition(x, N_JETONS - 21)[N_JETONS - 21:]
        haut.sort()
        eg_direct += int(haut[0] == haut[1])
    g = gen("lentilles-bbis/addendum-concentration-v1/egalite-vingtieme-rang/controle-ordre")
    x = np.round(rangs_20_21(g, 400_000) / pas)
    f = float((x[:, 0] == x[:, 1]).mean())
    print(f"contrôle, pas 1e-3 : tirage direct {eg_direct}/{n0} = {eg_direct / n0:.4f} ; statistiques d'ordre {f:.4f} "
          f"(± {np.sqrt(f * (1 - f) / 400_000):.4f})")
    # Partie 1 : simple précision
    for mu in (0.0, 10.0, 100.0):
        g = gen(f"lentilles-bbis/addendum-concentration-v1/egalite-vingtieme-rang/simple-precision/mu{mu}")
        eg, ecart = 0, []
        bloc = 500_000
        for _ in range(n_dir // bloc):
            x = rangs_20_21(g, bloc)
            ecart.append(float((x[:, 0] - x[:, 1]).mean()))
            y = (x + mu).astype(np.float32)
            eg += int((y[:, 0] == y[:, 1]).sum())
        p = eg / n_dir
        print(f"simple précision, moyenne des scores {mu:g} écarts types : {eg} égalités sur {n_dir} directions = {p:.2e} "
              f"(± {np.sqrt(max(eg, 1)) / n_dir:.1e}) ; écart moyen entre les deux rangs {np.mean(ecart):.5f} écart type ; "
              f"attendu sur 195 000 lectures : {195_000 * p:.2f} ; sur 2 000 directions nulles : {2_000 * p:.4f}")


main()
