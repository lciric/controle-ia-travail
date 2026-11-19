"""T2b : lois exactes du W de Kendall (trois objets ; m = 3, 4, 5 evaluateurs), en entiers (sans arrondi).
S = somme des carres des ecarts des sommes de rangs ; W = 12 S / (m^2 (k^3 - k)). Corrige l'arrondi de la table (a) de T2."""
import itertools
from fractions import Fraction
from collections import Counter
P = list(itertools.permutations([1, 2, 3]))
for m in (3, 4, 5):
    cnt = Counter()
    for combo in itertools.product(range(6), repeat=m):
        R = [sum(P[c][o] for c in combo) for o in range(3)]
        moy = Fraction(sum(R), 3)
        S = sum((Fraction(r) - moy) ** 2 for r in R)
        cnt[Fraction(12) * S / (m * m * 24)] += 1
    tot = 6 ** m
    vals = sorted(cnt)
    print(f"m = {m} ({tot} affectations) :")
    cum = 0
    for w in reversed(vals):
        cum += cnt[w]
        print(f"   W = {float(w):.4f} : P(W >= w) = {cum / tot:.4f}")
    print(f"   P(W <= 0,20) = {sum(c for w, c in cnt.items() if w <= Fraction(1, 5)) / tot:.4f}")
