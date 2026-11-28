"""Compléments du calcul à la main : A1 sur T4 (tranches figées de la lecture, aire stratifiée gelée) et sur A4 (a)
(tranches recalculées dans chaque tirage) ; A2 (b) pour une sonde à attention (softmax des logits restreints à la
fenêtre, `agreger_par_jeton`), avec des fenêtres du coût."""
import numpy as np

import complements_p3_v1 as cp
from controle_ia.premier_test_ia.statistiques import aire_stratifiee, strates_quantiles
from controle_ia.sondes.evaluation import aire_sous_courbe

N = 300
g0 = np.random.default_rng(4)
taches = np.repeat([f"t{k}" for k in range(8)], 12)
y = np.tile(np.r_[np.ones(5), np.zeros(7)], 8).astype(int)
v = g0.normal(size=taches.size) + 0.5 * y                 # log10 du coût
s = g0.normal(size=taches.size) + 0.6 * y
pl = g0.normal(size=(taches.size, 6))


def membres(t):
    return [np.flatnonzero(t == u) for u in np.unique(t)]


for mode in ("figees", "internes"):
    r = cp.ecart_conjoint(s, pl, y, taches, np.random.default_rng(9), N, 0.95, mode, v)
    g = np.random.default_rng(9)
    M = membres(taches)
    st_obs = strates_quantiles(v, 5)
    D, A, nb = [], [], []
    for _ in range(N):
        i = np.concatenate([M[c] for c in g.integers(0, len(M), size=len(M))])
        st = st_obs[i] if mode == "figees" else strates_quantiles(v[i], 5)
        a = aire_stratifiee(s[i], y[i], st)
        if a is None:
            continue
        q = np.quantile([aire_stratifiee(pl[i, k], y[i], st) for k in range(6)], 0.95)
        D.append(a - q)
        A.append(a)
        nb.append(len(np.unique(st)))
    obs = aire_stratifiee(s, y, st_obs) - np.quantile([aire_stratifiee(pl[:, k], y, st_obs) for k in range(6)], 0.95)
    eb, ab = np.quantile(D, 0.025), np.quantile(A, 0.025)
    ok = abs(eb - r["ecart_bas"]) < 1e-12 and abs(ab - r["aire_bas"]) < 1e-12 and abs(obs - r["ecart_observe"]) < 1e-12
    print(f"A1/A4 (a) tranches {mode:8s}: module Δ bas={r['ecart_bas']:.12f} A bas={r['aire_bas']:.12f} obs={r['ecart_observe']:.12f}"
          f" | main Δ bas={eb:.12f} A bas={ab:.12f} obs={obs:.12f} | égal={ok}"
          + (f" ; tranches par tirage module {r['tranches_par_tirage']} main min {min(nb)} max {max(nb)}" if mode == "internes" else ""))

# A2 (b), sonde à attention
g1 = np.random.default_rng(17)
na = 24
lon = g1.integers(14, 22, size=na)
c = g1.integers(2, 6, size=na)
fin = np.minimum(lon, c + g1.integers(1, 12, size=na))
deb = np.concatenate([[0], np.cumsum(lon)[:-1]])
S0, LG = g1.normal(size=int(lon.sum())), g1.normal(size=int(lon.sum()))
yy = np.tile([1, 0], 12)
tk = np.repeat(["a", "b", "c", "d"], 6)
rang = g1.permutation(na)
Dd = {"principales": ["p"], "loc": {"p": {"debut": deb, "longueur": lon, "c": c, "fin": fin}},
      "sh": {"p": {"sel": np.arange(na), "rangs": rang}}, "j": {"scores_0": S0, "logits_0": LG}}
F = cp.fenetres_de_meme_longueur(Dd, "p", np.random.default_rng(5))


def att(sc, lg):
    w = np.exp(lg - lg.max())
    return float(np.sum(w / w.sum() * sc))


g = np.random.default_rng(5)
Sp, Sc = np.empty((na, 50)), np.empty((na, 50))
for o in np.argsort(rang, kind="stable"):
    sc, lg = S0[deb[o]:deb[o] + lon[o]], LG[deb[o]:deb[o] + lon[o]]
    Lc = fin[o] - c[o]
    L = min(c[o], Lc)
    Sp[o] = [att(sc[x:x + L], lg[x:x + L]) for x in g.integers(0, c[o] - L + 1, size=50)]
    if Lc > c[o]:
        Sc[o] = [att(sc[x:x + L], lg[x:x + L]) for x in g.integers(c[o], fin[o] - L + 1, size=50)]
    else:
        Sc[o] = att(sc[c[o]:fin[o]], lg[c[o]:fin[o]])
print(f"A2 (b) attention : fenêtres égales à 1e-12 : pré {np.allclose(Sp, F['S_pre'], rtol=0, atol=1e-12)}, coût "
      f"{np.allclose(Sc, F['S_cout'], rtol=0, atol=1e-12)} ; actions où L_coût > c : {int(((fin - c) > c).sum())}")
r = cp.difference_fenetres(F["S_cout"], F["S_pre"], yy, tk, np.random.default_rng(8), N, 0.95)
g = np.random.default_rng(8)
M = membres(tk)
V = []
for _ in range(N):
    i = np.concatenate([M[k] for k in g.integers(0, len(M), size=len(M))])
    if len(set(yy[i].tolist())) < 2:
        continue
    V.append(np.mean([aire_sous_courbe(Sc[i, q], yy[i]) - aire_sous_courbe(Sp[i, q], yy[i]) for q in range(50)]))
print(f"A2 (b) attention : module bas={r['bas']:.12f} haut={r['haut']:.12f} | main bas={np.quantile(V, .025):.12f} "
      f"haut={np.quantile(V, .975):.12f} | égal={abs(r['bas'] - np.quantile(V, .025)) < 1e-12}")
