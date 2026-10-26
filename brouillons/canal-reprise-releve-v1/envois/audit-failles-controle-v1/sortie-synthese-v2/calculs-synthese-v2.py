# Calculs de la synthese de l'audit, version 2 (troisieme partie du rapport consolide, failles E a I,
# et calculs de prediction des hypotheses testables). Illustrations analytiques ou synthetiques,
# jamais des mesures de nos instruments ; aucune donnee des pilotes. Graines : SeedSequence (R9).
# Ce ne sont pas les experiences H1 a H5 du rapport : modeles nuls simplifies, pour verifier des
# proprietes mathematiques annoncees.
import numpy as np
from math import erf, sqrt, log

ss = np.random.SeedSequence(20261026)
enfants = ss.spawn(8)
np.set_printoptions(precision=4, suppress=True)


def Phi(x):
    return 0.5 * (1.0 + np.vectorize(erf)(np.asarray(x) / sqrt(2.0)))


def cusum(X, kappa):
    C = np.zeros_like(X)
    c = np.zeros(X.shape[0])
    for t in range(X.shape[1]):
        c = np.maximum(0.0, c + X[:, t] - kappa)
        C[:, t] = c
    return C


print("== bloc 1 : faille E, somme cumulee de Page et energie d'excursion")
rng = np.random.default_rng(enfants[0])
X = 0.2 + 1.3 * rng.standard_normal((2000, 100))
kappa = 0.5
C = cusum(X, kappa)
dC = np.diff(np.concatenate([np.zeros((X.shape[0], 1)), C], axis=1), axis=1)
print("ecart max entre (C_t - C_t-1)_+ et (X_t - kappa)_+ :", float(np.max(np.abs(np.maximum(dC, 0) - np.maximum(X - kappa, 0)))))
Xp = rng.permuted(X, axis=1)
V1 = np.sum(np.maximum(X - kappa, 0) ** 2, axis=1)
V1p = np.sum(np.maximum(Xp - kappa, 0) ** 2, axis=1)
print("premier terme de V_T, ecart max apres permutation des pas :", float(np.max(np.abs(V1 - V1p))))
Cp = cusum(Xp, kappa)
print("part des episodes ou max C_t change apres permutation :", float(np.mean(np.abs(C.max(1) - Cp.max(1)) > 1e-9)))
print("somme_{t<=T}(X_t - kappa) <= max_t C_t pour tout episode :", bool(np.all(np.sum(X - kappa, axis=1) <= C.max(1) + 1e-9)))
theta = 2.0
lse = np.log(np.sum(np.exp(theta * C), axis=1))
mx = theta * C.max(1)
print("theta max C <= ln somme exp(theta C) <= theta max C + ln T :", bool(np.all(lse >= mx - 1e-9)), bool(np.all(lse <= mx + log(100) + 1e-9)))
motif = np.array([1.5, -0.6, -0.6, -0.6])
print("motif de H1 (en sigma) : moyenne par pas", float(motif.mean()))
print("sur T = 100 : somme des pas hauts", 25 * 1.5, "; somme nette", float(25 * motif.sum()))
print("variance marginale du melange (bruit unite + motif) :", float(1 + np.mean((motif - motif.mean()) ** 2)))
for ds in (0.5, 1.0, 1.5):
    print(f"esperance du log-rapport de vraisemblance par pas, derive cible {ds} : saboteur {ds * motif.mean() - ds ** 2 / 2:.4f} ; honnete {-ds ** 2 / 2:.4f}")
inc = motif - kappa
print("increments deterministes de C pour kappa = 0,5 :", inc)

print("== bloc 2 : faille F, maximum brut et maximum normalise selon la duree T_e")
rng = np.random.default_rng(enfants[1])
N = 200_000
Tcal = 10
Tes = (5, 10, 20, 30)


def statistiques(T, tau):
    b = tau * rng.standard_normal((N, 1))
    Xs = b + rng.standard_normal((N, T))
    S = np.cumsum(Xs, axis=1)
    V = np.arange(1, T + 1, dtype=float)
    pas = Xs.max(1)
    cumule = S.max(1)
    norme = (S / np.sqrt(V * (1.0 + np.log(1.0 + V)))).max(1)
    return {"max par pas": pas, "max de la somme": cumule, "max normalise du rapport": norme}


for tau in (0.0, 0.3, 0.6):
    cal = statistiques(Tcal, tau)
    for alpha in (0.05, 0.01):
        seuils = {k: np.quantile(v, 1 - alpha) for k, v in cal.items()}
        lignes = []
        for Te in Tes:
            test = statistiques(Te, tau)
            lignes.append((Te, {k: float(np.mean(test[k] > seuils[k])) for k in test}))
        for k in seuils:
            print(f"tau={tau} alpha={alpha} {k} : " + " ; ".join(f"T_e={Te} {d[k] * 100:.2f} %" for Te, d in lignes))

print("== bloc 3 : faille G, plancher de directions aleatoires et projection orthogonale")
rng = np.random.default_rng(enfants[2])
d = 64


def plancher(lams, k_tic, delta, nW=20000):
    lams = np.asarray(lams, dtype=float)
    dmu = np.zeros(d)
    dmu[k_tic] = delta * np.sqrt(lams[k_tic])
    res = {}
    for nom, var in (("honnete", lams.copy()), ("melange", lams.copy())):
        if nom == "melange":
            var[k_tic] += 0.25 * dmu[k_tic] ** 2
        W = rng.standard_normal((nW, d)) * np.sqrt(var)
        num = np.abs(W @ dmu)
        den = np.sqrt(2.0 * np.sum(W ** 2 * lams, axis=1))
        auc = Phi(num / den)
        q95 = np.quantile(auc, 0.95)
        tir = np.array([np.quantile(rng.choice(auc, 200, replace=False), 0.95) for _ in range(400)])
        res[nom] = (float(q95), float(tir.std()))
    return res, float(Phi(delta / np.sqrt(2.0)))


spectres = {"isotrope": np.ones(d), "anisotrope 1/k": 1.0 / np.arange(1, d + 1)}
for nom, lams in spectres.items():
    for k_tic in (0, 40):
        for delta in (1.0, 2.0, 4.0):
            r, auc_sonde = plancher(lams, k_tic, delta)
            print(f"{nom} tic sur la composante {k_tic + 1} delta={delta} : aire de la sonde du tic {auc_sonde:.3f} ; "
                  f"plancher q95 honnete {r['honnete'][0]:.3f} (ecart type sur 200 tirages {r['honnete'][1]:.3f}) ; "
                  f"melange {r['melange'][0]:.3f} ({r['melange'][1]:.3f}) ; difference {r['melange'][0] - r['honnete'][0]:+.3f}")
m = 20
A = rng.standard_normal((m, m))
Sig = A @ A.T / m + 0.05 * np.eye(m)
beta = rng.standard_normal(m)
s2 = 0.25
vz = beta @ Sig @ beta + s2
sxz = Sig @ beta


def r2(P):
    Sp = P @ Sig @ P
    c = P @ sxz
    return float(c @ np.linalg.pinv(Sp) @ c / vz)


u1 = beta / np.linalg.norm(beta)
u2 = sxz / np.linalg.norm(sxz)
I = np.eye(m)
print("R2 lineaire du cout sans projection :", round(r2(I), 4))
print("apres projection orthogonale a la direction de regression beta :", round(r2(I - np.outer(u1, u1)), 4))
print("apres projection orthogonale a la covariance croisee Sigma beta :", round(r2(I - np.outer(u2, u2)), 4))

print("== bloc 4 : faille I, susceptibilite a deux points, hysteresis, petit nombre de moniteurs")
def dv(s, g0=0.15, A=0.6, s_et=0.8, w=0.03):
    return g0 * s + A * s / (1.0 + np.exp(-(s - s_et) / w))
s1, s2 = 0.2, 0.4
g1, g2 = dv(s1) / s1, dv(s2) / s2
print(f"seuil au-dela de s2 : g(s1)={g1:.4f} g(s2)={g2:.4f} chi2={(g2 - g1) / (s2 - s1):.4f} ; gain secant en s=1 : {dv(1.0):.4f}")
def moniteur_relais(chemin, haut=0.9, bas=0.3, saut=0.5):
    etat = 0.0
    sorties = []
    for s in chemin:
        if s >= haut:
            etat = saut
        elif s <= bas:
            etat = 0.0
        sorties.append(0.15 * s + etat)
    return sorties
montee = [0.2, 0.4]
print("branche montante (sans memoire / relais) :", [round(0.15 * s, 4) for s in montee], [round(v, 4) for v in moniteur_relais(montee)])
chemin = [0.2, 0.4, 0.7, 1.0, 0.5]
print("ancrage puis concession, verdict final (sans memoire / relais) :", round(0.15 * 0.5, 4), round(moniteur_relais(chemin)[-1], 4))
rng = np.random.default_rng(enfants[3])
for n in (5, 6, 8, 12, 20, 40):
    hits = 0
    reps = 20000
    for _ in range(reps):
        g = rng.uniform(0.05, 0.9, n)
        chi = rng.standard_normal(n)
        y = 0.1 + 0.8 * g + 0.2 * rng.standard_normal(n)
        e1 = e2 = 0.0
        for i in range(n):
            msk = np.arange(n) != i
            X1 = np.column_stack([np.ones(n - 1), g[msk]])
            X2 = np.column_stack([np.ones(n - 1), g[msk], chi[msk]])
            b1 = np.linalg.lstsq(X1, y[msk], rcond=None)[0]
            b2 = np.linalg.lstsq(X2, y[msk], rcond=None)[0]
            e1 += (y[i] - b1 @ np.array([1.0, g[i]])) ** 2
            e2 += (y[i] - b2 @ np.array([1.0, g[i], chi[i]])) ** 2
        if e2 <= 0.75 * e1:
            hits += 1
    print(f"n={n} moniteurs : probabilite qu'un second predicteur sans lien reduise l'erreur hors echantillon d'au moins 25 % : {hits / reps:.4f}")

print("== bloc 5 : gain brut, regression vers la moyenne et attenuation (hypothese HT-11)")
rng = np.random.default_rng(enfants[4])
Nn = 400_000
for rho in (0.5, 0.7, 0.9):
    for g_vrai in (0.0, 0.5):
        Tv = rng.standard_normal(Nn)
        se = np.sqrt((1 - rho) / rho)
        v0 = Tv + se * rng.standard_normal(Nn)
        c = rng.choice([-1.0, 1.0], Nn) * 1.5
        v1 = Tv + g_vrai * (c - Tv) + se * rng.standard_normal(Nn)
        x = c - v0
        y = v1 - v0
        pente = float(np.cov(x, y)[0, 1] / np.var(x, ddof=1))
        print(f"rho={rho} g vrai={g_vrai} : pente brute {pente:.4f} ; prediction g*rho + (1 - rho) = {g_vrai * rho + 1 - rho:.4f} ; desattenuee {(pente - (1 - rho)) / rho:.4f}")

print("== bloc 6 : classe K, rapport de variance et autocorrelation par episode (hypothese HT-07)")
rng = np.random.default_rng(enfants[5])
Nk = 100_000
T = 50


def episodes(phi, tau, permuter=False):
    b = tau * rng.standard_normal((Nk, 1))
    e = np.empty((Nk, T))
    e[:, 0] = rng.standard_normal(Nk)
    for t in range(1, T):
        e[:, t] = phi * e[:, t - 1] + np.sqrt(1 - phi ** 2) * rng.standard_normal(Nk)
    Xk = b + e
    if permuter:
        Xk = rng.permuted(Xk, axis=1)
    return Xk


def stats_k(Xk, q=5):
    Z = Xk - Xk.mean(1, keepdims=True)
    r1 = np.sum(Z[:, 1:] * Z[:, :-1], axis=1) / np.sum(Z ** 2, axis=1)
    cs = np.cumsum(np.concatenate([np.zeros((Z.shape[0], 1)), Z], axis=1), axis=1)
    blocs = cs[:, q:] - cs[:, :-q]
    vr = np.mean(blocs ** 2, axis=1) / (q * np.mean(Z ** 2, axis=1))
    return {"somme": Xk.sum(1), "maximum": Xk.max(1), "autocorrelation de rang 1": r1, "rapport de variance q=5": vr}


for tau in (0.0, 0.5):
    nul = stats_k(episodes(0.0, tau))
    seuils = {k: np.quantile(v, 0.99) for k, v in nul.items()}
    for phi, perm in ((0.1, False), (0.3, False), (0.5, False), (0.5, True)):
        alt = stats_k(episodes(phi, tau, perm))
        lab = f"phi={phi}" + (" puis rebrassage (classe C)" if perm else "")
        print(f"tau={tau} {lab} : " + " ; ".join(f"{k} {np.mean(alt[k] > seuils[k]) * 100:.2f} %" for k in alt))
