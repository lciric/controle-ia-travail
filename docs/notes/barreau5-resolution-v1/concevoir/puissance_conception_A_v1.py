"""Simulation a loi inventee (aucune donnee du programme) : puissance des contrastes
de la conception A. 64 taches, 10 actions par episode, un episode par condition et par tache.
Scores gaussiens : effet de tache partage entre conditions, effet d'episode, bruit d'action.
On estime l'ecart type d'echantillonnage de chaque statistique par Monte-Carlo (tirage des taches),
puis la plus petite valeur detectable a 80 % : Q + (z_niveau + 0,842) * s.
"""
import numpy as np
from scipy.stats import rankdata, norm, kendalltau

ss = np.random.SeedSequence(20261119)
rng = np.random.default_rng(ss.spawn(1)[0])
T, K = 64, 10

def auc(x, y):
    r = rankdata(np.concatenate([x, y]))
    n1, n0 = len(x), len(y)
    return (r[:n1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)

def tirage(icc_t, icc_e, d_sab_adapt, d_texte):
    # quatre cellules : (adaptateur, texte saboteur), (adaptateur, texte honnete),
    # (nu, texte saboteur), (nu, texte honnete). Decalage de l'adaptateur sans objet ici.
    s_a = np.sqrt(1 - icc_t - icc_e)
    u = rng.normal(0, np.sqrt(icc_t), (T, 1))
    def cell(m):
        return (m + u + rng.normal(0, np.sqrt(icc_e), (T, 1)) + rng.normal(0, s_a, (T, K))).ravel()
    return cell(d_texte + d_sab_adapt), cell(0.0), cell(d_texte), cell(0.0)

def sd_stats(icc_t, icc_e, d, dt, R=400):
    a1, a2 = [], []
    for _ in range(R):
        OS, A, J, OH = tirage(icc_t, icc_e, d, dt)
        p1 = auc(OS, A); mu = auc(J, OH)
        a1.append(p1); a2.append(p1 - mu)
    return np.mean(a1), np.std(a1), np.mean(a2), np.std(a2)

print("== Contraste principal : episodes du saboteur contre textes honnetes, meme adaptateur (640 contre 640)")
print("icc_tache icc_episode | s(aire) | aire min. 80% niveau 95% / 99% (plancher Q=0,56) | s(difference) | difference min. 95% / 99%")
for icc_t, icc_e in [(0.1, 0.1), (0.2, 0.2), (0.2, 0.4), (0.3, 0.5)]:
    _, s1, _, s2 = sd_stats(icc_t, icc_e, 0.0, 0.0)
    f = lambda z: (z + 0.842)
    print(f"{icc_t:.1f} {icc_e:.1f} | {s1:.4f} | {0.56 + f(1.645)*s1:.3f} / {0.56 + f(2.326)*s1:.3f} | {s2:.4f} | {f(1.645)*s2:.3f} / {f(2.326)*s2:.3f}")

print("\n== Puissance directe du contraste principal (borne basse de aire - Q > 0, Q = 0,56, niveau 99 % unilateral)")
for icc_t, icc_e in [(0.2, 0.2), (0.2, 0.4)]:
    _, s0, _, _ = sd_stats(icc_t, icc_e, 0.0, 0.0, R=300)
    for d in [0.2, 0.3, 0.4, 0.5, 0.7]:
        m, s, _, _ = sd_stats(icc_t, icc_e, d, 0.0, R=300)
        puissance = 1 - norm.cdf((0.56 + 2.326 * s - m) / s)
        print(f"icc {icc_t}/{icc_e} decalage {d:.1f} ecart type -> aire vraie {m:.3f} ; puissance {puissance:.2f}")

print("\n== Tendance dans la dose : tau de Kendall stratifie par tache, score contre exces (64 taches, n actions lisibles)")
def tau_strat(rho, n, icc_e, R=300):
    out = []
    for _ in range(R):
        num = den = 0.0
        for t in range(T):
            e = rng.normal(0, 1, n)
            s = rho * e + rng.normal(0, np.sqrt(icc_e)) + rng.normal(0, np.sqrt(max(1 - rho**2 - icc_e, 1e-6)), n)
            k = kendalltau(s, e).statistic
            num += k * n * (n - 1) / 2; den += n * (n - 1) / 2
        out.append(num / den)
    return np.mean(out), np.std(out)
for n in [10, 7, 5]:
    _, s0 = tau_strat(0.0, n, 0.3)
    print(f"n={n} : s(tau)={s0:.4f} ; tau min. detectable 80 % a 95 % / 99 % (plancher 0,03 suppose) : {0.03 + (1.645+0.842)*s0:.3f} / {0.03 + (2.326+0.842)*s0:.3f}")
