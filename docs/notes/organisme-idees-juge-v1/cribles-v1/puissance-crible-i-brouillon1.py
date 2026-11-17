# Puissance (aucune donnée) : test exact apparié des signes (McNemar exact unilatéral) contre Fisher unilatéral,
# trois bras sur les mêmes N mondes ; succès indépendants à monde fixé, avec un effet de monde (part rho des mondes
# « faciles » où tous les bras réussissent).
import numpy as np
from scipy.stats import binom, fisher_exact
rng = np.random.default_rng(np.random.SeedSequence([20261117, 2]))
def mcnemar_p(b, c):  # b : mondes où A réussit et B non ; c : l'inverse ; H1 : A > B
    n = b + c
    return 1.0 if n == 0 else float(binom.sf(b - 1, n, 0.5))
def puiss(N, p_a, p_b, alpha, apparie, rho=0.0, R=4000):
    ok = 0
    for _ in range(R):
        facile = rng.random(N) < rho
        a = (rng.random(N) < p_a) | facile; b = (rng.random(N) < p_b) | facile
        if apparie:
            p = mcnemar_p(int(np.sum(a & ~b)), int(np.sum(~a & b)))
        else:
            p = fisher_exact([[a.sum(), N - a.sum()], [b.sum(), N - b.sum()]], alternative="greater")[1]
        ok += p <= alpha
    return ok / R
print("seuils exacts : plus petit b (c = 0) rejeté à 5 % :", min(b for b in range(1, 20) if binom.sf(b-1, b, .5) <= .05),
      "; à 2,5 % :", min(b for b in range(1, 20) if binom.sf(b-1, b, .5) <= .025))
for N in (20, 24, 30):
    for pa, pb in ((0.40, 0.05), (0.30, 0.05), (0.40, 0.10), (0.50, 0.10)):
        print(f"N={N} p_haut={pa} p_bas={pb} : apparié 5 % {puiss(N,pa,pb,.05,True):.2f} ; apparié 2,5 % {puiss(N,pa,pb,.025,True):.2f} ; "
              f"Fisher 5 % {puiss(N,pa,pb,.05,False):.2f} ; apparié 5 % avec 10 % de mondes faciles {puiss(N,pa,pb,.05,True,0.10):.2f}")
# taux d'erreur sous le nul (p_a = p_b)
for N in (20, 30):
    for p in (0.05, 0.2):
        print(f"nul N={N} p={p} : apparié 5 % {puiss(N,p,p,.05,True):.3f} ; Fisher 5 % {puiss(N,p,p,.05,False):.3f}")
