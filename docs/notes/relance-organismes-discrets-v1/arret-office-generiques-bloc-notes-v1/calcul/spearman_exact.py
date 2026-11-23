# Loi exacte de la corrélation de rangs de Spearman sous indépendance, sans ex aequo,
# par programmation dynamique sur les sous-ensembles (somme des produits i*pi(i)).
from fractions import Fraction
import numpy as np, math

def loi(n):
    smax = sum(i*i for i in range(1, n+1))
    cnt = {0: np.zeros(smax+1, dtype=object)}
    cnt[0][0] = 1
    for k in range(n):
        nxt = {}
        for mask, arr in cnt.items():
            for v in range(1, n+1):
                bit = 1 << (v-1)
                if mask & bit:
                    continue
                d = (k+1)*v
                m2 = mask | bit
                a2 = nxt.get(m2)
                if a2 is None:
                    a2 = np.zeros(smax+1, dtype=object)
                    nxt[m2] = a2
                a2[d:] += arr[:smax+1-d]
        cnt = nxt
    (arr,) = cnt.values()
    return arr  # arr[S] = nombre de permutations de somme S

def critique(n, alpha=Fraction(5, 100)):
    arr = loi(n)
    tot = math.factorial(n)
    assert sum(arr) == tot
    sq = sum(i*i for i in range(1, n+1))
    den = n*(n*n-1)
    # rho = 1 - 6*(2*sq - 2*S)/den, croissant en S
    cum = 0
    best = None
    for S in range(len(arr)-1, -1, -1):
        if arr[S] == 0:
            continue
        cum += arr[S]
        if Fraction(cum, tot) <= alpha:
            best = (S, Fraction(cum, tot))
        else:
            break
    S, p = best
    rho = 1 - Fraction(6*(2*sq - 2*S), den)
    return rho, p

for n in (5, 8, 10, 11, 12, 13, 15):
    rho, p = critique(n)
    print(n, 'valeur critique unilatérale à 5 % :', float(rho), '(', rho, ') ; probabilité atteinte :', float(p),
          '; baisse pour un plan déplacé d\'un extrême à l\'autre : 6/(n+1) =', float(Fraction(6, n+1)))

# contrôle direct de la baisse 6/(n+1) à n = 12
n = 12
x = list(range(1, n+1)); y = [n] + list(range(1, n))  # le plan de rang 1 passe au rang n, les autres reculent d'un rang
d2 = sum((a-b)**2 for a, b in zip(x, y))
print('n = 12, un plan déplacé : rho =', float(1 - Fraction(6*d2, n*(n*n-1))), 'baisse =', float(Fraction(6*d2, n*(n*n-1))), '= 6/13 =', 6/13)
