"""Vérifications sur données fabriquées (aucune donnée réelle) de trois affirmations des réponses au développeur.
(1) Changement de signe par unité : taux de rejet sous l'hypothèse nulle, en plis croisés et avec une sonde gelée
    sur d'autres unités (engagement).
(2) Biais de la moyenne par pli de max(aire, 1 - aire) pour un prédicteur sans information.
Graines par numpy.random.SeedSequence (R9)."""
import itertools, json, sys
import numpy as np

ss = np.random.SeedSequence(20261123)
g1, g2 = [np.random.default_rng(s) for s in ss.spawn(2)]

def p_signes_haut(v):
    """Valeur p exacte, unilatérale vers le haut, du changement de signe sur la moyenne (observé compris)."""
    n = len(v)
    signes = np.array(list(itertools.product([1.0, -1.0], repeat=n)))
    t = signes @ v
    return float(np.mean(t >= v.sum() - 1e-12))

def taux(P, d, croise, n_rep, rng, n_app=None, alpha=0.05):
    rej = 0
    for _ in range(n_rep):
        if croise:
            D = rng.standard_normal((P, d))          # écarts propres des P paires, aucune trace commune
            S = D.sum(axis=0)
            v = np.array([D[u] @ (S - D[u]) / (P - 1) for u in range(P)])
        else:
            A = rng.standard_normal((n_app, d))      # unités d'apprentissage
            w = A.mean(axis=0)                       # sonde gelée avant les unités lues
            D = rng.standard_normal((P, d))          # unités tenues à l'écart
            v = D @ w
        rej += p_signes_haut(v) <= alpha
    return rej / n_rep

res = {"changement_de_signe": [], "biais_max": []}
for P in (6, 8, 10):
    a = taux(P, 256, True, 4000, g1)
    b = taux(P, 256, False, 4000, g1, n_app=P)
    res["changement_de_signe"].append({"unites": P, "plis_croises": a, "sonde_gelee": b})
    print(f"unités {P:2d} : rejet à 5 % unilatéral — plis croisés {a:.3f} ; sonde gelée sur d'autres unités {b:.3f}")

def aire(x, y):
    pos, neg = x[y == 1], x[y == 0]
    return float(np.mean(pos[:, None] > neg[None, :]) + 0.5 * np.mean(pos[:, None] == neg[None, :]))

for n_par_classe, n_plis in ((15, 40), (40, 40), (15, 5)):
    moy_max, max_moy = [], []
    for _ in range(2000):
        a = np.array([aire(g2.standard_normal(2 * n_par_classe), np.repeat([1, 0], n_par_classe)) for _ in range(n_plis)])
        moy_max.append(np.mean(np.maximum(a, 1 - a)))
        max_moy.append(max(a.mean(), 1 - a.mean()))
    r = {"lignes_par_classe_et_par_pli": n_par_classe, "plis": n_plis,
         "moyenne_des_max_par_pli": float(np.mean(moy_max)), "max_de_la_moyenne": float(np.mean(max_moy))}
    res["biais_max"].append(r)
    print(f"{n_par_classe} lignes par classe, {n_plis} plis : moyenne des max par pli {r['moyenne_des_max_par_pli']:.3f} ; "
          f"max de l'aire moyenne {r['max_de_la_moyenne']:.3f}")
json.dump(res, open(sys.argv[1], "w"), indent=1)
