"""Calcul exact : loi de la somme des rangs contraires W sous la nulle, K différences, 2^K attributions de signes."""
from fractions import Fraction
from itertools import product
for K in (6, 7):
    total = 2 ** K
    comptes = {}
    for signes in product((0, 1), repeat=K):
        w = sum(r for r, s in zip(range(1, K + 1), signes) if s)
        comptes[w] = comptes.get(w, 0) + 1
    cumul, w_ok = 0, None
    for w in sorted(comptes):
        cumul += comptes[w]
        if Fraction(cumul, total) <= Fraction(25, 1000):
            w_ok, p_ok = w, Fraction(cumul, total)
        else:
            break
    print(f"K={K} attributions={total} P(W<=0)={Fraction(comptes[0], total)} w({K}) au niveau 95 bilatéral={w_ok} P(W<=w)={p_ok}={float(p_ok)} ; pas suivant P={Fraction(cumul, total)}={float(Fraction(cumul, total))}")
