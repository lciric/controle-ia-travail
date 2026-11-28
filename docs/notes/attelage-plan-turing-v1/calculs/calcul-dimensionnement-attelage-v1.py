#!/usr/bin/env python3
"""Calculs de dimensionnement illustratifs pour l'attelage du plan Turing (v1).

Deterministe, sans alea, sans reseau. Chaque bloc imprime ses hypotheses.
Rien ici n'est une mesure : ce sont des ordres de grandeur a refaire au preenregistrement.
"""
import math
from fractions import Fraction


def phi_inv(p):
    """Quantile de la loi normale centree reduite (algorithme d'Acklam, precision ~1e-9)."""
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]
    pl = 0.02425
    if p < pl:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if p > 1 - pl:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    q = p - 0.5
    r = q * q
    return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)


def n_deux_proportions(p0, p1, alpha=0.05, puissance=0.80, unilateral=True):
    """Effectif par bras, test de deux proportions independantes (approximation normale, sans correction)."""
    za = phi_inv(1 - alpha) if unilateral else phi_inv(1 - alpha / 2)
    zb = phi_inv(puissance)
    pb = (p0 + p1) / 2
    num = (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p0 * (1 - p0) + p1 * (1 - p1))) ** 2
    return math.ceil(num / (p1 - p0) ** 2)


print("== 1. Hasard dans le meme espace : N tirages independants de masse w ==")
print("   P(decouverte) = 1 - (1 - w)^N ; facteur r = multiplication de la masse par appel par l'attelage")
for w in (1e-2, 1e-3, 1e-4):
    for N in (50, 200, 1000):
        base = 1 - (1 - w) ** N
        ligne = f"   w={w:g}  N={N:5d}  hasard={base:6.3f}"
        for r in (2, 5, 20):
            ligne += f"   r={r:2d}: {1 - (1 - min(1.0, r * w)) ** N:6.3f}"
        print(ligne)

print()
print("== 2. Mondes par bras pour distinguer deux probabilites de decouverte (unilateral 5 %, puissance 80 %) ==")
print("   unite = le monde, bras independants ; a multiplier par l'effet de grappe si l'unite est la famille")
for (p0, p1) in ((0.18, 0.33), (0.18, 0.63), (0.05, 0.10), (0.05, 0.22), (0.02, 0.04), (0.02, 0.10)):
    print(f"   p0={p0:4.2f}  p1={p1:4.2f}  mondes par bras = {n_deux_proportions(p0, p1)}")

print()
print("== 3. Effet de grappe : F familles de m mondes, correlation intra-famille rho ==")
print("   effectif efficace = F*m / (1 + (m-1)*rho)")
for rho in (0.05, 0.2, 0.5):
    for (F, m) in ((8, 25), (12, 25), (12, 50), (30, 10)):
        neff = F * m / (1 + (m - 1) * rho)
        print(f"   rho={rho:4.2f}  F={F:2d}  m={m:2d}  mondes={F*m:4d}  efficace={neff:6.1f}")

print()
print("== 4. Garantie disjonctive : zero succes sur n tirages => p <= 1 - delta^(1/n) au niveau 1 - delta ==")
for n in (100, 300, 1000, 3000):
    print(f"   n={n:5d}  borne a 95 % = {1 - 0.05 ** (1 / n):.5f}")
print("   tirages uniformes necessaires pour certifier p <= eps a 95 % avec zero succes : n >= ln(0,05)/ln(1-eps)")
for eps in (0.05, 0.01, 0.001):
    print(f"   eps={eps:g}  n={math.ceil(math.log(0.05) / math.log(1 - eps))}")

print()
print("== 5. Enumerateur mecanique des transferts : M lois de bibliotheque, T traits, renommage de k traits ==")
print("   candidats = M * T^k ; evidence requise (unites naturelles) ~ ln(M*T^k) + ln(1/alpha), alpha = 0,05")
for (M, T, k) in ((100, 20, 1), (100, 20, 2), (100, 20, 3), (1000, 20, 2), (1000, 30, 3)):
    cand = M * T ** k
    print(f"   M={M:5d} T={T:3d} k={k}  candidats={cand:>11,d}  evidence={math.log(cand) + math.log(1 / 0.05):5.2f}".replace(",", " "))

print()
print("== 6. Plancher d'exploration au hasard : part gamma du budget tiree uniformement ==")
print("   decouvertes attendues perdues au pire = gamma (si le selecteur est parfait) ; gain = base sans biais")
for gamma in (0.05, 0.10, 0.20):
    for N in (200, 1000):
        print(f"   gamma={gamma:4.2f}  N={N:5d}  tirages uniformes={int(gamma * N):4d}  borne a 95 % sur p si zero succes={1 - 0.05 ** (1 / max(1, int(gamma * N))):.4f}")

print()
print("== 7. Chaine de marchepieds : attente moyenne = somme des 1/w_i (en appels), tirages independants ==")
for chaine in ((1e-2,), (1e-2, 1e-2), (1e-1, 1e-1, 1e-1), (1e-3,), (3e-2, 3e-2)):
    print(f"   masses {chaine}  attente moyenne = {sum(1 / w for w in chaine):8.1f} appels ; generations minimales = {len(chaine)}")

print()
print("== 8. Faux positifs du resolveur dans la queue : precision = p(1-b) / (p(1-b) + (1-p)a) ==")
for p in (1e-2, 1e-3):
    for a in (1e-2, 1e-3, 1e-4):
        b = 0.2
        prec = p * (1 - b) / (p * (1 - b) + (1 - p) * a)
        print(f"   p={p:g}  fausse acceptation a={a:g}  faux rejet b={b}  precision des acceptes={prec:5.3f}")

# controle exact d'une identite utilisee dans le texte
assert Fraction(1, 1) - (Fraction(999, 1000)) ** 200 > Fraction(18, 100)
assert Fraction(1, 1) - (Fraction(999, 1000)) ** 200 < Fraction(19, 100)
print()
print("controle exact : 1 - 0,999^200 est entre 0,18 et 0,19 : OK")
