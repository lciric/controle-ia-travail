"""Tightness of eq:robust-tpr: s = z, g = 1{z <= t}, rho* = 1: bound equals the true change."""
from fractions import Fraction
from scipy import stats
for t in (-1.0, 0.0, 0.5, 1.5):
    p = 1 - stats.norm.cdf(t)              # P(s > t)
    chi2 = p/(1-p)                          # Var(g)/E[g]^2 for g = indicator with E g = 1-p
    true = p                                # P_g(s>t) = 0
    print("t=%.1f true change=%.6f bound=%.6f half-bound=%.6f" % (t, true, (p*(1-p)*chi2)**0.5, 0.5*chi2**0.5))
