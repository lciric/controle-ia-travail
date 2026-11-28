"""Contrôle de l'approximation employée par e5_regle_g1.py : la borne basse de D = aire(sonde) − quantile 0,95 des aires
des directions de plancher, rééchantillonnée par linéarisation en poids de tâches, comparée au calcul exact du dépôt
(`controle_ia.t07.plancher_v2.comparer_difference_au_plancher`, comptage par tâches), sous les MÊMES tirages de tâches
(`poids_des_tirages`). Mondes plantés ; aucune donnée du programme."""
import json, sys
import numpy as np
from controle_ia.t07.plancher_v2 import comparer_difference_au_plancher, poids_des_tirages
from controle_ia.sondes.evaluation import aire_sous_courbe
import e5_regle_g1 as m

rng = np.random.default_rng(20261128)
n, K, B = 200, 60, 2000
lignes = []
for aire in (0.50, 0.56, 0.62, 0.70):
    for rep in range(3):
        br = m.Bruit(rng)
        dz = m.decalage_pour_aire(aire, True)
        o = (rng.random((n, m.E, m.A)) < 0.6).astype(float)
        tau = br.taches(n)
        zH, _ = br.scores(tau, m.E); zS, _ = br.scores(tau, m.E); zS = zS + dz * o
        fp = np.stack([br.seul(n, m.E) for _ in range(K)]); fn = np.stack([br.seul(n, m.E) for _ in range(K)])
        pos = np.concatenate([zS[None], fp]).reshape(K + 1, n, -1); neg = np.concatenate([zH[None], fn]).reshape(K + 1, n, -1)
        a, g = m.aire_et_gradient(pos, neg)
        graine = int(rng.integers(1, 2**31))
        W = poids_des_tirages(n, B, graine)                       # multiplicités entières, celles du dépôt
        P = W / W.sum(1, keepdims=True)
        repl = a[:, None] + g @ (P - 1.0 / n).T
        d_lin = repl[0] - np.quantile(repl[1:], 0.95, axis=0)
        bas_lin = float(np.quantile(d_lin, (1 - 0.98333) / 2))
        # calcul exact du dépôt : scores (actions,), plancher (K, actions), y, blocs
        s = np.concatenate([pos[0].ravel(), neg[0].ravel()])
        Pl = np.concatenate([pos[1:].reshape(K, -1), neg[1:].reshape(K, -1)], axis=1)
        y = np.concatenate([np.ones(pos[0].size, int), np.zeros(neg[0].size, int)])
        blocs = np.concatenate([np.repeat(np.arange(n), pos.shape[2]), np.repeat(np.arange(n), neg.shape[2])])
        r = comparer_difference_au_plancher(s, Pl, y, blocs, B, graine, 0.95, 0.98333)
        assert abs(aire_sous_courbe(s, y) - a[0]) < 1e-12
        lignes.append({"aire_visee": aire, "aire": round(float(a[0]), 4), "D_estimation_depot": round(r["difference"]["estimation"], 5),
                       "D_bas_depot_exact": round(r["difference"]["bas"], 5), "D_bas_linearise": round(bas_lin, 5),
                       "ecart": round(bas_lin - r["difference"]["bas"], 5),
                       "meme_decision": bool((bas_lin > 0) == (r["difference"]["bas"] > 0))})
ec = np.array([l["ecart"] for l in lignes])
print(json.dumps({"taches": n, "directions": K, "tirages": B, "lignes": lignes, "ecart_absolu_max": float(np.abs(ec).max()),
                  "ecart_moyen": float(ec.mean()), "decisions_egales": int(sum(l["meme_decision"] for l in lignes)), "sur": len(lignes)}, indent=1, ensure_ascii=False))
