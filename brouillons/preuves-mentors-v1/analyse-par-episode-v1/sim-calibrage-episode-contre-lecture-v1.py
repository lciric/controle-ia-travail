"""Contre-lecture (aucune donnée réelle) : fausses alarmes par épisode du pipeline v4 (bras_episode + evaluer) sous un nul
avec effets de tâche et d'épisode, pour un bras fixe (type G) et un bras entraîné en validation croisée (type W, logistique
L2 λ = 1 de la principale). 60 tâches, 4 conditions, 10 actions ; plis par tâche ; seuil = maximum des 48 (rang 1)."""
import sys

import numpy as np

from controle_ia.analyse_principale_r1_r2 import calcul_v1 as CV
from controle_ia.analyse_principale_r1_r2 import calcul_v4 as C4
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K
from controle_ia.analyse_blanche_noire.modeles import ajuster_logistique, logits

R = int(sys.argv[1]) if len(sys.argv) > 1 else 100
DIM = int(sys.argv[2]) if len(sys.argv) > 2 else 16
SIG_T, SIG_E = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0, float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
g = np.random.default_rng(np.random.SeedSequence(20261102_1))
taches = [f"t{i:02d}" for i in range(60)]
conds = list(K.CONDITIONS)
tache = np.repeat(np.array(taches), 40)
cond = np.tile(np.repeat(np.array(conds), 10), 60)
pas = np.tile(np.arange(10), 240)
episode = np.char.add(np.char.add(tache, "/"), cond)
tables = {"episode": episode, "condition": cond, "pas": pas, "tache": tache}
ti = np.searchsorted(np.array(taches), tache)
ep = C4.episodes_de(tables, ti, taches)
eligible = np.ones(tache.size, bool)
el_ep = np.ones(ep["n"], bool)
u = g.standard_normal(DIM)
u /= np.linalg.norm(u)
fa = {"G": [], "W": []}
for r in range(R):
    pli, _ = CV.plis_des_taches(tache, g)
    pe = C4.plis_episodes(pli, ep)
    a_t = g.standard_normal((60, DIM)) * SIG_T
    b_e = g.standard_normal((ep["n"], DIM)) * SIG_E
    X = a_t[ti] + b_e[ep["idx"]] + g.standard_normal((tache.size, DIM))
    scores = {"G": X @ u}
    y = (cond == K.POSITIF).astype(float)
    app = np.isin(cond, (K.POSITIF, K.NEGATIF))
    w = np.full(tache.size, np.nan)
    for k in range(K.PLIS):
        m = ajuster_logistique(X[app & (pli != k)], y[app & (pli != k)], 1.0)
        w[pli == k] = logits(m, X[pli == k])
    scores["W"] = w
    for b, s in scores.items():
        be = C4.bras_episode(s, eligible, cond, pli, ti, ep, pe)
        ev = CV.evaluer(be, el_ep, ep["cond"], pe, ep["tache_idx"], 60, (1, 100))
        fa[b].append(int(ev["comptes"][K.NEGATIF]["alarmes"].sum()))
for b, v in fa.items():
    v = np.array(v)
    print(f"{b} R={R} dim={DIM} sig_t={SIG_T} sig_e={SIG_E} moyenne={v.mean():.3f} (attendu 1.224) "
          f"P(>4)={np.mean(v > 4):.3f} P(>=4)={np.mean(v >= 4):.3f} P(=0)={np.mean(v == 0):.3f} max={v.max()}")
