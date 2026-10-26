# Calculs independants de la contre-lecture v2 (failles E a I de la troisieme partie du rapport).
# Illustrations sous des nuls simplifies, jamais des mesures ; aucune donnee des pilotes.
# Graines : SeedSequence(26102026), distinctes de celles de la synthese (R9). Lance par : python3 -I.
import numpy as np
from math import erf, sqrt

ss = np.random.SeedSequence(26102026)
kids = ss.spawn(12)
Phi = lambda x: 0.5 * (1.0 + np.vectorize(erf)(np.asarray(x, dtype=float) / sqrt(2.0)))

def cusum(X, kappa):
    C = np.zeros_like(X); c = np.zeros(X.shape[0])
    for t in range(X.shape[1]):
        c = np.maximum(0.0, c + X[:, t] - kappa); C[:, t] = c
    return C

print("== E1 : identite (C_t - C_{t-1})_+ = (X_t - kappa)_+ pour TOUTE suite (pas seulement C_{t-1} = 0)")
rng = np.random.default_rng(kids[0])
for nom, X in (("gaussien", rng.standard_normal((500, 60))), ("lourd (Student 3)", rng.standard_t(3, (500, 60))),
               ("dents de scie bruitees", np.tile([1.5, -0.6, -0.6, -0.6], 15)[None, :] + 0.3 * rng.standard_normal((500, 60)))):
    C = cusum(X, 0.5)
    dC = np.diff(np.hstack([np.zeros((500, 1)), C]), axis=1)
    print(f"  {nom:24s} ecart max {np.max(np.abs(np.maximum(dC, 0) - np.maximum(X - 0.5, 0))):.1e} ; part des pas avec C_(t-1) > 0 : {np.mean(C[:, :-1] > 0):.2f}")

print("== E2 : HR1 rejoue sous un nul explicite (scores honnetes N(0,1), T = 100, kappa = 0,5, seuils au rang conforme sur 20 000 episodes honnetes, alpha = 1 %)")
rng = np.random.default_rng(kids[1])
T, K, kappa = 100, 20000, 0.5
H = rng.standard_normal((K, T))
motif = np.tile([1.5, -0.6, -0.6, -0.6], T // 4)
def stats(X):
    C = cusum(X, kappa)
    return {"max CUSUM": C.max(1), "V1 = somme (X-kappa)_+^2 (terme symetrique)": np.sum(np.maximum(X - kappa, 0) ** 2, 1),
            "V_T complet (lambda=1, theta=2)": np.sum(np.maximum(X - kappa, 0) ** 2, 1) + np.log(np.sum(np.exp(2.0 * C), 1)),
            "somme des scores": X.sum(1), "variance intra-episode": X.var(1)}
nul = stats(H); seuils = {k: np.quantile(v, 0.99) for k, v in nul.items()}
A1 = motif[None, :] + rng.standard_normal((5000, T))                       # HR1 tel qu'ecrit (phase fixe)
A2 = rng.permuted(A1, axis=1)                                            # temoin de classe C : meme multi-ensemble, rebrasse
A3 = -0.075 + rng.standard_normal((5000, T))                             # decalage constant de meme moyenne, sans dents de scie
A4 = 0.45 + rng.standard_normal((5000, T))                               # decalage constant juste sous kappa
for nom, A in (("HR1 dents de scie", A1), ("classe C : HR1 rebrasse", A2), ("constante -0,075 (meme moyenne)", A3), ("constante +0,45 (sous kappa)", A4)):
    s = stats(A)
    print("  " + nom + " : " + " ; ".join(f"{k} {100 * np.mean(s[k] > seuils[k]):.1f} %" for k in s))

print("== F1 : normalisation du rapport, implementation independante ; calibrage a T = 10, 100 000 episodes par cas")
rng = np.random.default_rng(kids[2])
N = 100_000
def gen(T, tau, phi=0.0, lourd=False):
    b = tau * rng.standard_normal((N, 1))
    e = np.empty((N, T)); e[:, 0] = rng.standard_normal(N)
    for t in range(1, T):
        e[:, t] = phi * e[:, t - 1] + sqrt(1 - phi ** 2) * rng.standard_normal(N)
    if lourd:
        e = rng.standard_t(4, (N, T)) / sqrt(2.0)
    return b + e
def norm_rapport(S, T, V1=1.0):
    V = np.arange(1, T + 1, dtype=float)
    return (S / np.sqrt(V * (1.0 + np.log(1.0 + V / V1)))).max(1)
def norm_variance_vraie(S, T, tau):
    V = np.arange(1, T + 1, dtype=float)
    return (S / np.sqrt(V + tau ** 2 * V ** 2)).max(1)
def norm_intra(X):
    # sigma estime DANS l'episode (variance courante), comme le laisse lire V_t = somme sigma_s^2
    T = X.shape[1]; S = np.cumsum(X, 1); V = np.cumsum(X ** 2, 1) + 1e-9
    return (S / np.sqrt(V * (1.0 + np.log(1.0 + V / V[:, :1])))).max(1)
cas = [("independant, tau=0", 0.0, 0.0, False), ("effet episode tau=0,3", 0.3, 0.0, False), ("effet episode tau=0,6", 0.6, 0.0, False),
       ("effet episode fort tau=1,0", 1.0, 0.0, False), ("AR(1) intra-episode phi=0,3, tau=0", 0.0, 0.3, False), ("queues lourdes (t4), tau=0", 0.0, 0.0, True)]
for nom, tau, phi, lourd in cas:
    Xc = gen(10, tau, phi, lourd); Sc = np.cumsum(Xc, 1)
    cal = {"max par pas": Xc.max(1), "max somme brute": Sc.max(1), "max normalise (rapport)": norm_rapport(Sc, 10),
           "max normalise, sigma intra-episode": norm_intra(Xc), "max normalise, variance vraie du nul": norm_variance_vraie(Sc, 10, tau)}
    seuils = {k: np.quantile(v, 0.99) for k, v in cal.items()}
    out = []
    for Te in (5, 10, 20, 30, 60):
        Xt = gen(Te, tau, phi, lourd); St = np.cumsum(Xt, 1)
        tst = {"max par pas": Xt.max(1), "max somme brute": St.max(1), "max normalise (rapport)": norm_rapport(St, Te),
               "max normalise, sigma intra-episode": norm_intra(Xt), "max normalise, variance vraie du nul": norm_variance_vraie(St, Te, tau)}
        out.append((Te, {k: 100 * np.mean(tst[k] > seuils[k]) for k in tst}))
    print("  " + nom)
    for k in seuils:
        print(f"    {k:38s} alpha=1 % : " + " ; ".join(f"T_e={Te} {d[k]:.2f} %" for Te, d in out))

print("== G : plancher sous Sigma honnete et sous Sigma melangee, geometrie en 1/k (64 dim), tic sur une composante faible ; 200 directions")
rng = np.random.default_rng(kids[3])
d = 64; lam = 1.0 / np.arange(1, d + 1)
def plancher(k_tic, delta, nrep=300):
    dmu = np.zeros(d); dmu[k_tic] = delta * sqrt(lam[k_tic])
    res = {}
    for nom, var in (("honnete", lam.copy()), ("melange", lam.copy())):
        if nom == "melange": var[k_tic] += 0.25 * dmu[k_tic] ** 2
        qs = []
        for _ in range(nrep):
            W = rng.standard_normal((200, d)) * np.sqrt(var)
            auc = Phi(np.abs(W @ dmu) / np.sqrt(2.0 * np.sum(W ** 2 * lam, 1)))
            qs.append(np.quantile(auc, 0.95))
        res[nom] = (float(np.mean(qs)), float(np.std(qs)))
    return res, float(Phi(delta / sqrt(2.0)))
for k_tic in (0, 40):
    for delta in (1.0, 2.0, 4.0):
        r, a = plancher(k_tic, delta)
        print(f"  tic composante {k_tic + 1} delta={delta} : sonde du tic {a:.3f} ; plancher honnete {r['honnete'][0]:.3f} (+-{r['honnete'][1]:.3f}) ; melange {r['melange'][0]:.3f} (+-{r['melange'][1]:.3f}) ; ecart {r['melange'][0] - r['honnete'][0]:+.3f}")

print("== HR5 : chance qu'un second predicteur SANS LIEN reduise l'erreur hors echantillon (validation croisee un contre tous) d'au moins 25 %")
rng = np.random.default_rng(kids[4])
def loo_gain(n, bruit, reps=8000):
    hits = 0
    for _ in range(reps):
        g = rng.uniform(0.05, 0.9, n); chi = rng.standard_normal(n); y = 0.1 + 0.8 * g + bruit * rng.standard_normal(n)
        e1 = e2 = 0.0
        for i in range(n):
            m = np.arange(n) != i
            b1 = np.linalg.lstsq(np.column_stack([np.ones(n - 1), g[m]]), y[m], rcond=None)[0]
            b2 = np.linalg.lstsq(np.column_stack([np.ones(n - 1), g[m], chi[m]]), y[m], rcond=None)[0]
            e1 += (y[i] - b1 @ [1, g[i]]) ** 2; e2 += (y[i] - b2 @ [1, g[i], chi[i]]) ** 2
        hits += e2 <= 0.75 * e1
    return hits / reps
for n in (5, 6, 8, 12, 20):
    print(f"  n={n} : bruit 0,2 -> {loo_gain(n, 0.2):.3f} ; bruit 0,05 -> {loo_gain(n, 0.05):.3f} ; bruit 0,5 -> {loo_gain(n, 0.5):.3f}")

print("== combinaison entre modes : 1 - (1 - a)^3")
for a in (0.05, 0.01): print(f"  alpha={a} : {1 - (1 - a) ** 3:.4f}")

print("== HT-11 : pente brute = g R + (1 - R), verification analytique par simulation independante")
rng = np.random.default_rng(kids[5])
for g in (0.0, 0.5):
    Tv = rng.standard_normal(300_000); e0 = 0.8 * rng.standard_normal(300_000); e1 = 0.8 * rng.standard_normal(300_000)
    c = rng.choice([-1.5, 1.5], 300_000); v0 = Tv + e0; v1 = Tv + g * (c - Tv) + e1
    x = c - v0; y = v1 - v0; pente = np.cov(x, y)[0, 1] / np.var(x, ddof=1); R = 1 - 0.64 / np.var(x, ddof=1)
    print(f"  g={g} : pente {pente:.4f} ; g R + (1 - R) = {g * R + 1 - R:.4f}")
