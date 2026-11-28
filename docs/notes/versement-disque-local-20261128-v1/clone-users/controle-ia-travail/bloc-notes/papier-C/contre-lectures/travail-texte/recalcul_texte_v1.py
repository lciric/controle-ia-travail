"""Recalcul indépendant (contre-lecture texte) : Clopper-Pearson et W de Kendall exact, 3 objets."""
import itertools
from fractions import Fraction
from scipy.stats import beta

for n, x in ((300, 281), (300, 280), (600, 555), (600, 554)):
    print("CP", n, x, round(beta.ppf(0.025, x, n - x + 1), 5))

def loi_w(m, k=3):
    perms = list(itertools.permutations(range(1, k + 1)))
    out = []
    for combo in itertools.product(perms, repeat=m):
        r = [sum(p[j] for p in combo) for j in range(k)]
        mu = Fraction(sum(r), k)
        s = sum((Fraction(x) - mu) ** 2 for x in r)
        out.append(Fraction(12) * s / (m * m * (k ** 3 - k)))
    return out

for m in (2, 4, 5):
    w = loi_w(m)
    vals = sorted(set(w))
    crit = [v for v in vals if sum(1 for x in w if x >= v) / len(w) <= 0.05]
    print("m", m, "affectations", len(w), "E[W]", float(sum(w) / len(w)),
          "p_min", min(sum(1 for x in w if x >= v) / len(w) for v in vals),
          "W critique 5 %", float(crit[0]) if crit else None,
          "p(W>=crit)", (sum(1 for x in w if x >= crit[0]) / len(w)) if crit else None)
