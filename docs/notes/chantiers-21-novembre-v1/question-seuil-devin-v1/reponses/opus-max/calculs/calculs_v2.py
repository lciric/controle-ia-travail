"""Compléments : épreuve en deux temps (criblage puis confirmation), point mort en épisodes,
et simulation de l'apprentissage croisé avec permutation de toute la chaîne."""
import numpy as np
from scipy import stats

K = 30


def et(n, pi):
    return np.sqrt(1 / (pi * n) + 1 / ((1 - pi) * n)) / 4


def p1(t, a, n_ep, pi=0.5, k=K):
    return stats.norm.sf(stats.norm.isf(a / k) - (t / 2) / et(n_ep, pi))


def p2(t, n_neufs, pi=0.5, a2=0.05):
    # confirmation : prédicteur retenu, figé, sans réapprentissage, tous les épisodes neufs en épreuve
    return stats.norm.sf(stats.norm.isf(a2) - (t / 2) / et(n_neufs, pi))


print("== A. Confirmation : puissance à la plus petite fuite du criblage ==")
for nom, a, N in [("a", 0.05, 4000), ("b", 0.0125, 4000), ("c", 0.05, 8000)]:
    for pi in [0.5, 0.05]:
        # plus petite fuite du criblage seul
        za = stats.norm.isf(a / K); zb = stats.norm.isf(0.2)
        t = 2 * (za + zb) * et(N / 2, pi)
        print(f"({nom}) pi={pi}: fuite {t:.4f} ; confirmation 2000 neufs {p2(t, 2000, pi):.4f} ; 4000 neufs {p2(t, 4000, pi):.4f}")

print("\n== B. Deux temps : plus petite fuite retrouvée à puissance 0,8 (p1 * p2) ==")
for nom, a, N in [("a", 0.05, 4000), ("b", 0.0125, 4000), ("c", 0.05, 8000), ("d", 0.0125, 8000)]:
    for pi in [0.5, 0.05]:
        for nn in [2000, 4000]:
            lo, hi = 0.0, 0.6
            for _ in range(200):
                m = (lo + hi) / 2
                if p1(m, a, N / 2, pi) * p2(m, nn, pi) < 0.8:
                    lo = m
                else:
                    hi = m
            print(f"({nom}) pi={pi}, confirmation {nn} neufs : {hi:.4f}")

print("\n== C. Fausses suspensions durables par admission (deux temps, seuil 0,05 à la confirmation) ==")
for a in [0.05, 0.0125]:
    q = a * 0.05
    print(f"criblage {a}: par test {q:.5f} ; par admission {1-(1-q)**4:.4f} (borne {4*q:.4f})")

print("\n== D. Point mort en épisodes : criblage à 0,05 contre 0,0125 à sensibilité égale ==")
r = ((stats.norm.isf(0.0125 / K) + stats.norm.isf(0.2)) / (stats.norm.isf(0.05 / K) + stats.norm.isf(0.2))) ** 2
print("épisodes de (b) pour la sensibilité de (a) :", 4000 * r, "soit +", 4000 * (r - 1), "par test et +", 4 * 4000 * (r - 1), "par admission")
for conf in [2000, 4000]:
    D = 4 * 4000 * (r - 1) / 0.15 - conf
    print(f"confirmation de {conf} épisodes : (a) préférable si le coût propre d'une suspension temporaire < {D:,.0f} épisodes")

print("\n== E. Valeur prédictive d'un rejet au criblage (a priori de fuite par test) ==")
for prior in [0.01, 0.1]:
    for nom, a, pw in [("a", 0.05, 0.8), ("b", 0.0125, 0.677)]:
        print(f"a priori {prior}, ({nom}) : {prior*pw/(prior*pw+(1-prior)*a):.3f}")

print("\n== F. Simulation : moitié-moitié contre apprentissage croisé (permutation de toute la chaîne) ==")
ss = np.random.SeedSequence(20261122)
graines = ss.spawn(3)


def simuler(mode, n_total, delta, d, reps, B, graine, a=0.05):
    rng = np.random.default_rng(graine)
    rejets = 0
    for _ in range(reps):
        S = rng.integers(0, 2, n_total)
        X = rng.standard_normal((n_total, d))
        X[:, 0] += delta * S

        def stat(Sv):
            if mode == "moitie":
                h = n_total // 2
                mu1 = X[:h][Sv[:h] == 1].mean(0); mu0 = X[:h][Sv[:h] == 0].mean(0)
                w = mu1 - mu0; c = (mu1 + mu0) / 2
                pred = ((X[h:] - c) @ w > 0).astype(int)
                y = Sv[h:]
                return 0.5 * (pred[y == 1].mean() + (1 - pred[y == 0]).mean())
            else:
                h = n_total // 2
                total = 0.0
                for tr, te in [(slice(0, h), slice(h, None)), (slice(h, None), slice(0, h))]:
                    Xt, St = X[tr], Sv[tr]
                    mu1 = Xt[St == 1].mean(0); mu0 = Xt[St == 0].mean(0)
                    w = mu1 - mu0; c = (mu1 + mu0) / 2
                    pred = ((X[te] - c) @ w > 0).astype(int)
                    y = Sv[te]
                    total += 0.5 * (pred[y == 1].mean() + (1 - pred[y == 0]).mean())
                return total / 2

        t_obs = stat(S)
        if mode == "moitie":
            # prédicteur figé : seules les étiquettes d'épreuve sont permutées
            h = n_total // 2
            cnt = 0
            for _ in range(B):
                Sp = S.copy(); Sp[h:] = rng.permutation(S[h:])
                cnt += stat(Sp) >= t_obs
        else:
            cnt = 0
            for _ in range(B):
                cnt += stat(rng.permutation(S)) >= t_obs
        p = (1 + cnt) / (B + 1)
        rejets += p <= a
    return rejets / reps


# fuite en variation totale sur le seul premier trait : 2*Phi(delta/2)-1
delta = 2 * stats.norm.ppf((1 + 0.07) / 2)
print("delta", delta, "variation totale", 2 * stats.norm.cdf(delta / 2) - 1)
for nom, mode, n_total, g in [("moitié 4000", "moitie", 4000, graines[0]), ("croisé 4000", "croise", 4000, graines[1]),
                             ("moitié 8000", "moitie", 8000, graines[2])]:
    pw = simuler(mode, n_total, delta, d=10, reps=300, B=99, graine=g)
    print(f"{nom}: puissance au seuil 0,05 (un prédicteur) {pw:.3f}")
# validité sous le nul
for nom, mode, n_total, g in [("croisé 4000 nul", "croise", 4000, ss.spawn(1)[0])]:
    pw = simuler(mode, n_total, 0.0, d=10, reps=400, B=99, graine=g)
    print(f"{nom}: taux de rejet sous le nul {pw:.3f}")
