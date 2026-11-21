"""Mesure l'erreur absolue des évaluations flottantes dont l'erreur croît avec n.

Usage : python3 -I -B mesurer_tolerance_v2.py CHEMIN_DU_PROGRAMME

1. P(Bin(n, p) <= kmax) en flottants (fonction `binomiale_cdf_flottante` du programme), contre la valeur
   exacte en rationnels au même p (le flottant p pris comme rationnel exact).
2. P(a, x), gamma incomplète régularisée (fonction `gamma_incomplete_p`), a = (n − 1)/2, contre une somme
   en décimaux à 60 chiffres.
Aucun tirage : grilles fixes.
"""
import importlib.util
import math
import sys
from decimal import Decimal, getcontext
from fractions import Fraction

spec = importlib.util.spec_from_file_location("programme", sys.argv[1])
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)


def binom_cdf_exacte(n, p, kmax):
    fr = Fraction(p)
    a, b = fr.numerator, fr.denominator
    c = b - a
    if kmax < n - kmax:
        s = sum(math.comb(n, j) * a ** j * c ** (n - j) for j in range(kmax + 1))
        return Fraction(s, b ** n)
    s = sum(math.comb(n, j) * a ** j * c ** (n - j) for j in range(kmax + 1, n + 1))
    return 1 - Fraction(s, b ** n)


PS = (1e-4, 1e-3, 0.005, 0.01, 0.02, 0.05, 0.1, 0.3, 0.5, 0.9)
print("binomiale : n, kmax, erreur maximale sur p, p de l'erreur maximale")
pire_par_n = {}
for n in (200, 300, 400, 1000, 2000, 3000, 5000):
    for kmax in sorted({0, 1, 5, 20, 40, 41, 60, 100, n // 10, n // 2}):
        pire, p_pire = 0.0, None
        for p in PS:
            # seulement là où la masse est non négligeable (ailleurs les deux valent 0 ou 1)
            exact = binom_cdf_exacte(n, p, kmax)
            e = abs(P.binomiale_cdf_flottante(n, p, kmax) - float(exact))
            if e > pire:
                pire, p_pire = e, p
        pire_par_n[n] = max(pire_par_n.get(n, 0.0), pire)
        print(f"  n={n:5d} kmax={kmax:5d} erreur={pire:.3e} p={p_pire}")
print("binomiale, pire par n :", {n: f"{e:.3e}" for n, e in pire_par_n.items()})

getcontext().prec = 60
PI = Decimal("3.14159265358979323846264338327950288419716939937510582097494")


def gamma_dec(a2):
    """Γ(a) pour a = a2/2, a2 entier positif, en décimaux."""
    if a2 % 2 == 0:
        return Decimal(math.factorial(a2 // 2 - 1))
    m = (a2 - 1) // 2          # Γ(m + 1/2) = (2m)! √π / (4^m m!)
    return Decimal(math.factorial(2 * m)) * PI.sqrt() / (Decimal(4) ** m * Decimal(math.factorial(m)))


def gammainc_dec(a2, x):
    a = Decimal(a2) / 2
    x = Decimal(x)
    terme = Decimal(1) / a
    somme = terme
    j = 1
    while True:
        terme = terme * x / (a + j)
        somme += terme
        if terme < somme * Decimal("1e-50"):
            break
        j += 1
    return somme * (x.ln() * a - x).exp() / gamma_dec(a2)


print("gamma incomplète : n, erreur maximale")
pire_g = {}
for n in (200, 1000, 2000, 3000, 5000):
    a2 = n - 1
    a = a2 / 2
    sd = math.sqrt(2 * a2)
    pire = 0.0
    for z in (-6, -4, -2, -1, 0, 1, 2, 4, 6):
        q = a2 + z * sd
        if q <= 0:
            continue
        x = q / 2
        ref = float(gammainc_dec(a2, x))
        e = abs(P.gamma_incomplete_p(a, x) - ref)
        pire = max(pire, e)
    pire_g[n] = pire
    print(f"  n={n:5d} erreur={pire:.3e}")
print("gamma, pire par n :", {n: f"{e:.3e}" for n, e in pire_g.items()})
