"""Contrôle de la recette de puissance du brouillon 3 (données synthétiques seules).
Hypothèse d'effectif, choix du contre-lecteur : 1 épisode par tâche et par condition, M actions par épisode."""
import sys, time
import numpy as np
from scipy.stats import norm

T, M, NDIR, NB = 64, 10, 800, 2000
racine = np.random.SeedSequence(20261119)
QP = 0.95


def counts(pos, neg):
    """pos (K,T,M), neg (K,T,M) -> C (K,T,T) : comptes de paires pos>neg (+0,5 ex aequo) par couple de tâches."""
    K = pos.shape[0]
    c = np.empty((K, T, T))
    for k0 in range(0, K, 50):
        d = pos[k0:k0+50, :, :, None, None] - neg[k0:k0+50, None, None, :, :]
        c[k0:k0+50] = (d > 0).sum(axis=(2, 4)) + 0.5 * (d == 0).sum(axis=(2, 4))
    return c


def regle_D(scores_pos, scores_neg, rng, niveau):
    """scores_* (K,T,M), K=0 sonde, 1.. directions. Renvoie borne basse de D au niveau donné."""
    C = counts(scores_pos, scores_neg)  # K,T,T
    W = rng.multinomial(T, np.ones(T) / T, size=NB).astype(np.float64)  # NB,T
    n = W.sum(1) * M  # positifs = négatifs = n
    A = np.empty((C.shape[0], NB))
    for k0 in range(0, C.shape[0], 100):
        Ck = C[k0:k0 + 100]
        X = W @ Ck.transpose(1, 0, 2).reshape(T, -1)  # NB, k*T
        X = X.reshape(NB, Ck.shape[0], T)
        A[k0:k0 + 100] = (X * W[:, None, :]).sum(-1).T / (n * n)
    D = A[0] - np.quantile(A[1:], QP, axis=0)
    return np.quantile(D, (1 - niveau) / 2)


def tirer(rng, delta, f, tache_sonde):
    """Scores (K,T,M) d'une condition : sonde (k=0) avec effet de tâche commun, directions avec effet propre."""
    s = rng.standard_normal((NDIR + 1, T, M))
    s[0] += tache_sonde[:, None]
    s[1:] += 0  # effet de tâche des directions ajouté par l'appelant
    if delta:
        masque = rng.random((T, M)) < f
        s[0] += delta * masque
    return s


def une_rep(rng, a, f, regle_entiere=True):
    delta = np.sqrt(2.5) * norm.ppf(a) if a is not None else 0.0
    ts = 0.5 * rng.standard_normal(T)
    td = 0.5 * rng.standard_normal((NDIR, T))
    def cond(dl):
        s = tirer(rng, dl, f, ts)
        s[1:] += td[:, :, None]
        return s
    H, TJ, B = cond(0.0), cond(0.0), cond(delta)
    niv = 1 - 0.05 / 3
    c1 = regle_D(B, H, rng, niv) > 0
    if not regle_entiere:
        return c1
    c3 = regle_D(B, TJ, rng, niv) > 0
    c2 = True
    return c1 and c2 and c3


if __name__ == "__main__":
    mode = sys.argv[1]
    reps = int(sys.argv[2])
    rng = np.random.default_rng(racine.spawn(1)[0] if False else racine)
    if mode == "etalonnage":
        for a in (0.55, 0.6, 0.65, 0.7, 0.8):
            delta = np.sqrt(2.5) * norm.ppf(a)
            th = (63 / 64) * norm.cdf(delta / np.sqrt(2.5)) + (1 / 64) * norm.cdf(delta / np.sqrt(2))
            print(f"a={a} delta={delta:.4f} aire_theorique={th:.4f}")
    elif mode == "nul":
        t0 = time.time(); fa = 0
        for r in range(reps):
            fa += une_rep(rng, None, 1.0, regle_entiere=False)
        print(f"nul, clause (1) seule, 98,33 % : {fa}/{reps} faux au-dessus ; {time.time()-t0:.1f} s")
    else:
        a, f = float(sys.argv[3]), float(sys.argv[4])
        t0 = time.time(); ok = 0
        for r in range(reps):
            ok += une_rep(rng, a, f)
        print(f"a={a} f={f} regle entiere : {ok}/{reps} ; {time.time()-t0:.1f} s")
