import numpy as np

# Parametres : ancrage/consensus p0, vraie croyance mu_T, poids de recompense
p0, mu_T = 0.20, 0.85
lam_cal, lam_sync = 1.0, -0.50

# Generateur quadratique de Bregman Phi(x) = x^2 => D_Phi(x || y) = (x - y)^2
def d_bregman(x, y):
    return (x - y) ** 2

def recompense_moyenne_mc(q, u_samples):
    terme_3pts = d_bregman(u_samples, p0) - d_bregman(u_samples, q) - d_bregman(q, p0)
    r = u_samples - lam_cal * d_bregman(u_samples, q) + lam_sync * terme_3pts
    return np.mean(r)

rng = np.random.default_rng(20261024)
u = rng.binomial(1, mu_T, size=2_000_000)

grille_q = np.linspace(0.01, 0.99, 9801)
esperances = np.array([recompense_moyenne_mc(q, u) for q in grille_q])
q_opt_empirique = grille_q[np.argmax(esperances)]
q_opt_theorique = (lam_cal * mu_T - lam_sync * p0) / (lam_cal - lam_sync)

print(f"Vraie probabilite conditionnelle mu_T : {mu_T:.4f}")
print(f"Optimum theorique biaise q*           : {q_opt_theorique:.4f}")
print(f"Optimum empirique Monte-Carlo q*      : {q_opt_empirique:.4f}")
print(f"E[R | q = mu_T (honnete)]             : {recompense_moyenne_mc(mu_T, u):.6f}")
print(f"E[R | q = q*   (biaise)]              : {recompense_moyenne_mc(q_opt_theorique, u):.6f}")
assert abs(q_opt_empirique - q_opt_theorique) < 5e-3 and q_opt_empirique < mu_T - 0.20
