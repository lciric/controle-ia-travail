"""Contre-lecture 2 : bornes de résolution (C7) et seuils bilatéraux de HP.4 (R2), sans tirage, sans module du dépôt.
Intervalle de Clopper-Pearson bilatéral de niveau 1 − γ (γ/2 par côté), γ = 1e-5, R = 20 000 ; référence p0 = 0,05
mesurée sur R0 = 100 000."""
from scipy import stats
G, R, R0 = 1e-5, 20000, 100000
def cp(k, n):
    b = stats.beta.ppf(G / 2, k, n - k + 1) if k > 0 else 0.0
    h = stats.beta.ppf(1 - G / 2, k + 1, n - k) if k < n else 1.0
    return b, h
b0, h0 = cp(5000, R0)
print(f"IC0 (p0 = 0,05, R0 = 100 000) = [{b0:.5f} ; {h0:.5f}]")
kd = max(k for k in range(0, 2000) if cp(k, R)[1] < b0)
ku = min(k for k in range(0, 3000) if cp(k, R)[0] > h0)
print(f"« en dessous » conforme ssi k ≤ {kd} (p̂ ≤ {kd / R:.5f}) ; « au-dessus » conforme ssi k ≥ {ku} (p̂ ≥ {ku / R:.5f})")
for nom, xb, xh in (("tromperie", 0.55, 0.86), ("enjeux", 0.31, 0.62)):
    ks = [k for k in range(R + 1) if cp(k, R)[0] > xb and cp(k, R)[1] < xh] if False else None
    lo = next(k for k in range(int(xb * R), R) if cp(k, R)[0] > xb)
    hi = next(k for k in range(int(xh * R), 0, -1) if cp(k, R)[1] < xh)
    print(f"HP.4 {nom} ]{xb} ; {xh}[ : conforme ssi {lo} ≤ k ≤ {hi}, soit {lo / R:.5f} ≤ p̂ ≤ {hi / R:.5f}")
    # probabilité d'être conforme à la valeur du modèle et à la loi de référence 0,92854
for nom, xb, xh, v in (("tromperie", 0.55, 0.86, 0.705), ("enjeux", 0.31, 0.62, 0.463)):
    lo = next(k for k in range(int(xb * R), R) if cp(k, R)[0] > xb)
    hi = next(k for k in range(int(xh * R), 0, -1) if cp(k, R)[1] < xh)
    for p in (v, 0.92854, xh - 0.005, xh + 0.005):
        pc = stats.binom.cdf(hi, R, p) - stats.binom.cdf(lo - 1, R, p)
        print(f"   {nom} : taux vrai {p:.4f} -> P(conforme) = {pc:.4f}")
# fausse confirmation d'un « au plus » (C7) : taux vrai 0,058
k_ap = max(k for k in range(R) if cp(k, R)[0] <= h0)
print(f"« au plus » conforme ssi k ≤ {k_ap} ; P(conforme | p = 0,058) = {stats.binom.cdf(k_ap, R, 0.058):.3f}")
