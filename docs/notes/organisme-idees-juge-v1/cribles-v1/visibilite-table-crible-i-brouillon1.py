# Calcul synthétique (aucun monde MR-2, aucune donnée) : visibilité d'une composante « interaction_xor » de taille I nat
# dans une table croisée à la médiane de 2 000 épisodes, contraste diagonale / antidiagonale, khi-deux à K-1 = 2 degrés.
import numpy as np
from scipy.stats import chi2_contingency
ss = np.random.SeedSequence(20261117)
rng = np.random.default_rng(ss)
K = 3
def softmax(L):
    L = L - L.max(axis=1, keepdims=True); E = np.exp(L); return E / E.sum(axis=1, keepdims=True)
Zb = rng.standard_normal(200000); Zt = rng.standard_normal(200000)
for I in (0.04, 0.06, 0.08):
    res = []
    for rep in range(40):  # 40 directions de pente et biais tirés
        d = rng.standard_normal(K); d -= d.mean(); d /= np.linalg.norm(d)
        b = rng.normal(0, 0.3, K)
        def info(s):
            Q = softmax(b + s * np.outer(Zt * np.sign(Zb), d)); Q0 = softmax(np.tile(b, (len(Zt), 1)))
            return float((Q * (np.log(Q) - np.log(Q0))).sum(axis=1).mean())
        lo, hi = 0.0, 5.0
        for _ in range(30):
            mid = (lo + hi) / 2; lo, hi = (mid, hi) if info(mid) < I else (lo, mid)
        s = (lo + hi) / 2
        rej = 0
        for t in range(200):
            zb = rng.standard_normal(2000); zt = rng.standard_normal(2000)
            P = softmax(b + s * np.outer(zt * np.sign(zb), d))
            u = rng.random(2000); y = np.minimum((u[:, None] > np.cumsum(P, axis=1)).sum(axis=1), K - 1)
            diag = (np.sign(zb - np.median(zb)) == np.sign(zt - np.median(zt)))
            tab = np.array([[np.sum((diag) & (y == k)) for k in range(K)], [np.sum((~diag) & (y == k)) for k in range(K)]])
            if chi2_contingency(tab)[1] <= 0.05 / 28: rej += 1   # correction de Bonferroni sur les 28 paires
        res.append(rej / 200)
    res = np.array(res)
    print(f"I={I} nat : part des tables où la paire (condition, trait) se voit à 5 %/28 : médiane {np.median(res):.2f}, min {res.min():.2f}, quantile 10 % {np.quantile(res,0.1):.2f}")
