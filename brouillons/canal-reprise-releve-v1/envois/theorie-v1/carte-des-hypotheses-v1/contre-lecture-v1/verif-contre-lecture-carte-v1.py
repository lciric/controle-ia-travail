"""Vérifications de la contre-lecture de la carte des hypothèses v1 — recalculs indépendants des lemmes A3, A4, A6, A7, A9,
A19, A22 et contre-exemple sur l'« exemple » de classe K3 (A3). Aucune donnée lue ; synthétique et analytique seulement ;
graine SeedSequence(20261028) + 1 (distincte de celle de la carte). Lancer : python -I -B verif-contre-lecture-carte-v1.py
"""
import math
from statistics import NormalDist

import numpy as np

N = NormalDist()
ss = np.random.SeedSequence(20261029)
g1, g2, g3, g4 = (np.random.default_rng(s) for s in ss.spawn(4))


def phi_plafond(delta, r0, T, alpha):
    var = r0 + (1 - r0) / T if math.isfinite(T) else r0
    return 1 - N.cdf(N.inv_cdf(1 - alpha) - delta / math.sqrt(var)) if var > 0 else 1.0


print("== A7 : recalcul à la main, Φ(δ/√(r₀ + (1−r₀)/T) − z_α) ==")
z01 = N.inv_cdf(0.99)
print(f"  z_0.01 = {z01:.4f} ; δ/√r₀ = {0.3/math.sqrt(0.2):.4f} ; Φ(δ/√r₀ − z_α) = {N.cdf(0.3/math.sqrt(0.2) - z01):.4f}  (carte : 0,049)")
for T in (10, 50, float("inf")):
    print(f"  r₀=0   T={T}: {phi_plafond(0.3, 0.0, T, 0.01):.3f}   r₀=0,2 T={T}: {phi_plafond(0.3, 0.2, T, 0.01):.3f}")
print("  carte : 0,084 / 0,419 / 1 à r₀ = 0 ; 0,039 / 0,046 / 0,049 à r₀ = 0,2 (T = 10 / 50 / ∞)")
# Vérification indépendante : le vecteur 1 est propre pour (1−r₀)I + r₀11ᵀ, valeur propre 1 − r₀ + r₀T ; variance de la moyenne.
T = 7
r0 = 0.2
Sigma = (1 - r0) * np.eye(T) + r0 * np.ones((T, T))
un = np.ones(T)
print(f"  Σ·1 = λ·1 ? écart {np.abs(Sigma @ un - (1 - r0 + r0 * T) * un).max():.1e} ; var(moyenne) = {un @ Sigma @ un / T**2:.4f} contre r₀ + (1−r₀)/T = {r0 + (1 - r0) / T:.4f}")
# Monte-Carlo de la cellule α = 5 % (celle du script de la carte) ET de la cellule α = 1 %, r₀ = 0,2, T = 50
for alpha in (0.05, 0.01):
    n, T = 200_000, 50
    def episodes(d, rng):
        b = rng.normal(0, math.sqrt(0.2), size=(n, 1))
        e = rng.normal(0, math.sqrt(0.8), size=(n, T))
        return (b + e + d).mean(axis=1)
    h = np.quantile(episodes(0.0, g1), 1 - alpha)
    mc = float((episodes(0.3, g1) > h).mean())
    print(f"  Monte-Carlo α={alpha} δ=0,3 r₀=0,2 T=50 : {mc:.4f} ; analytique {phi_plafond(0.3, 0.2, 50, alpha):.4f}")

print("== A6 : E₀[exp(λΣz − λ²T/2)] = exp(λ²r₀T(T−1)/2) ==")
lam, T, r0 = 0.5, 6, 0.3
var_somme = T**2 * r0 + T * (1 - r0)
analytique = math.exp(lam**2 * var_somme / 2 - lam**2 * T / 2)
print(f"  formule : exp(λ²(T²r₀ + T(1−r₀) − T)/2) = {analytique:.4f} ; carte exp(λ²r₀T(T−1)/2) = {math.exp(lam**2 * r0 * T * (T - 1) / 2):.4f}")
b = g2.normal(0, math.sqrt(r0), size=(400_000, 1)); e = g2.normal(0, math.sqrt(1 - r0), size=(400_000, T))
print(f"  Monte-Carlo : {np.exp(lam * (b + e).sum(axis=1) - lam**2 * T / 2).mean():.4f}")

print("== A3 : identité de Lindley max_t C_t = max(0, max_{a≤b} Σ_{a..b}(z−k)) ==")
ecart = 0.0
for _ in range(1500):
    z = g3.standard_t(3, size=25); k = 0.5
    c = m = 0.0
    for v in z:
        c = max(0.0, c + v - k); m = max(m, c)
    s = np.concatenate([[0.0], np.cumsum(z - k)])
    meilleur = max(0.0, max(s[b_] - s[a_] for a_ in range(26) for b_ in range(a_ + 1, 26)))
    ecart = max(ecart, abs(m - meilleur))
print(f"  écart maximal sur 1 500 suites (Student 3 ddl, k = 0,5) : {ecart:.1e}")

print("== A3 : contre-exemple à l'« exemple » de K3 (« toute loi de moyenne par pas sous k ») ==")
# Honnête : z ~ N(0,1), T = 30, k = 0,5 ; seuil de Page au quantile 0,99 honnête (K = 20 000) ; P₁ : z + μ₁ avec 0 < μ₁ < k.
T, k, K = 30, 0.5, 20_000
def page_max(Z):
    c = np.zeros(Z.shape[0]); m = np.zeros(Z.shape[0])
    for t in range(Z.shape[1]):
        c = np.maximum(0.0, c + Z[:, t] - k); m = np.maximum(m, c)
    return m
h = np.quantile(page_max(g4.standard_normal((K, T))), 0.99)
for mu1 in (0.0, 0.2, 0.4):
    taux = float((page_max(g4.standard_normal((K, T)) + mu1) > h).mean())
    print(f"  moyenne par pas μ₁ = {mu1:.1f} < k = {k} : taux de Page au seuil 1 % honnête = {taux:.4f}")
print("  → une moyenne sous k ne garde pas la loi de M_k ni ne la domine : Page y a une puissance > α (l'exemple de K3 est faux ;")
print("    seule la borne déterministe de RC-3.1 (e), max C_t < h ⇒ moyenne < k + h/T, est juste).")

print("== A4 : Pinsker, d_VT ≤ √(KL/2), KL = δᵀΓ⁻¹δ/2 ⇒ d_VT ≤ ‖Γ^{−1/2}δ‖/2 ; B étalé sur n₀ pas : B/(2σ√n₀) ==")
B, n0, sigma = 5.0, 100, 1.0
delta = np.full(n0, B / n0)
print(f"  ‖δ‖/(2σ) = {np.linalg.norm(delta) / (2 * sigma):.4f} ; B/(2σ√n₀) = {B / (2 * sigma * math.sqrt(n0)):.4f}")

print("== A9 : G = F^{n/m} ⇒ G^m = F^n ; médiane de G pour n/m = 2 ==")
print(f"  Φ⁻¹(0,5^{{1/2}}) = {N.inv_cdf(0.5 ** 0.5):.3f} (carte : 0,545)")
x = g3.standard_normal((20_000, 200)).max(axis=1)
u = g3.uniform(size=(20_000, 100)) ** 0.5
y = np.array([N.inv_cdf(float(v)) for v in u.max(axis=1)])
print("  quantiles 0,5/0,9/0,99 — F sur 200 :", " ".join(f"{np.quantile(x, p):.3f}" for p in (0.5, 0.9, 0.99)),
      "; G sur 100 :", " ".join(f"{np.quantile(y, p):.3f}" for p in (0.5, 0.9, 0.99)))

print("== A19 : aire de la projection w à covariance commune Σ : Φ(|wᵀΔμ|/√(2wᵀΣw)) ; w* = Σ⁻¹Δμ sur un vecteur propre ==")
d = 6
vals = np.array([4.0, 2.0, 1.0, 0.5, 0.25, 0.05])
Sigma = np.diag(vals); dmu = np.zeros(d); dmu[-1] = 0.3    # Δμ porté par le vecteur propre de plus petite valeur λ = 0,05
w_star = np.linalg.solve(Sigma, dmu)
aire = lambda w: N.cdf(abs(w @ dmu) / math.sqrt(2 * w @ Sigma @ w))
print(f"  aire(w*) = {aire(w_star):.3f} ; Φ(‖Δμ‖/√(2λ)) = {N.cdf(np.linalg.norm(dmu) / math.sqrt(2 * vals[-1])):.3f}")
W = g4.multivariate_normal(np.zeros(d), Sigma, size=200)
aires = np.array([aire(w) for w in W])
print(f"  plancher : quantile 0,95 des aires de 200 directions w ~ N(0, Σ) = {np.quantile(aires, 0.95):.3f} (près de 0,5 : la confusion loge dans une direction de faible variance)")

print("== A22 : identité E[X | J=1] − E₀[X] = δ + (E[ε | J=1] − E[ε]) ; avec E₁[X] inconditionnel il manque δ·P(J=1) ==")
n = 400_000
eps = g4.standard_normal(n); J = (eps < np.quantile(eps, 0.3)).astype(float)   # placement corrélé au bruit (pas « peu signalés »)
delta = 1.0; X = delta * J + eps
print(f"  E[X|J=1] − E[ε] = {X[J == 1].mean() - eps.mean():.4f} ; δ + (E[ε|J=1] − E[ε]) = {delta + eps[J == 1].mean() - eps.mean():.4f} ;"
      f" E[X|J=1] − E₁[X] = {X[J == 1].mean() - X.mean():.4f} (= précédent − δ·P(J=1) = {delta * J.mean():.3f})")
