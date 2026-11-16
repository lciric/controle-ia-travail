"""Chronométrage de l'énumération exacte du placebo du crible (v), pire cas n_c = 20, k_R = 10.

Programme de remplacement déclaré : le programme de mesure `mesure_crible_v_v1.py` n'est pas
encore écrit (le code s'écrit après le scellement du texte) ; ce programme fait le seul travail
coûteux du placebo tel que la section « Métrique » du crible le définit : pour chacun des
C(20, 10) = 184 756 ensembles A de mondes appelés, L_P(A) = somme des manques hors de A et
S_P(A) = 1 - somme($_b + [w dans A] $_e) / somme($_b + $_e), puis p_choix (part des A avec
L_P(A) <= L_R), la moyenne et les quantiles 5 % et 95 % de L_P et de S_P.
Mondes simulés par une formule fixe (aucun tirage, aucune donnée, aucun appel) ; bibliothèque
standard seule. Deux lancements, le plus long retenu (règle de l'étape 0).
"""

import platform
import sys
import time
from itertools import combinations
from math import comb

N_C, K = 20, 10
manque = [w % 3 for w in range(N_C)]                 # l_w simulé
dollars_b = [0.39 + 0.01 * (w % 5) for w in range(N_C)]   # $_b(w) simulé
dollars_e = [2.92 + 0.02 * (w % 7) for w in range(N_C)]   # $_e(w) simulé
L_R = sum(manque[w] for w in range(K, N_C))          # règle simulée : mondes 0 à 9 appelés


def quantile(trie, q):
    i = min(len(trie) - 1, max(0, int(round(q * (len(trie) - 1)))))
    return trie[i]


def enumere():
    total_b = sum(dollars_b)
    total = total_b + sum(dollars_e)
    total_manque = sum(manque)
    lp, sp = [], []
    n_inf = 0
    for A in combinations(range(N_C), K):
        l = total_manque - sum(manque[w] for w in A)
        s = 1.0 - (total_b + sum(dollars_e[w] for w in A)) / total
        lp.append(l)
        sp.append(s)
        if l <= L_R:
            n_inf += 1
    assert len(lp) == comb(N_C, K)
    lp.sort()
    sp.sort()
    return {
        "ensembles": len(lp),
        "p_choix": n_inf / len(lp),
        "L_P": (sum(lp) / len(lp), quantile(lp, 0.05), quantile(lp, 0.95)),
        "S_P": (sum(sp) / len(sp), quantile(sp, 0.05), quantile(sp, 0.95)),
    }


durees = []
for essai in (1, 2):
    t0 = time.perf_counter()
    res = enumere()
    durees.append(time.perf_counter() - t0)
    print(f"lancement {essai} : {durees[-1]:.3f} s ; ensembles {res['ensembles']} ; p_choix {res['p_choix']:.4f} ; "
          f"L_P moyenne {res['L_P'][0]:.4f} (5 % {res['L_P'][1]}, 95 % {res['L_P'][2]}) ; "
          f"S_P moyenne {res['S_P'][0]:.4f} (5 % {res['S_P'][1]:.4f}, 95 % {res['S_P'][2]:.4f})")
print(f"retenu (le plus long) : {max(durees):.3f} s ; Python {sys.version.split()[0]} ; {platform.machine()}")
