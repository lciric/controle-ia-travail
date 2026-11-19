"""Contre-lecteur Opus 5.5 : même modèle que `egalite_rang_k_contre_lecteur.py`, mais par comptage des égalités, comme l'auteur
(vingtième et vingt-et-unième plus grands scores tirés exactement par la représentation de Rényi, arrondis en simple précision,
égalités comptées), sur 40 000 000 de directions par moyenne, pour départager 7,0e-6 (auteur) et 9,0e-6 (formule).
Usage : python -B egalite_comptage_direct_contre_lecteur.py E4"""
import sys
import numpy as np
from scipy import special
E4 = int(sys.argv[1])
n = 89_498
for i, mu in enumerate((0.0, 10.0, 100.0)):
    g = np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=E4, spawn_key=(100 + i,))))
    eg, tot = 0, 0
    for _ in range(10):
        b = 4_000_000
        g20 = g.standard_gamma(20, size=b)
        e21 = g.standard_exponential(b)
        gn = g20 + e21 + g.standard_gamma(n - 20, size=b)
        x20 = -special.ndtri(g20 / gn)
        x21 = -special.ndtri((g20 + e21) / gn)
        eg += int(((x20 + mu).astype(np.float32) == (x21 + mu).astype(np.float32)).sum())
        tot += b
    print(f"moyenne {mu:g} : {eg} égalités sur {tot} directions = {eg / tot:.3e} (± {np.sqrt(eg) / tot:.1e})")
