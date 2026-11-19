"""Contrôles statistiques refaits à la main par le contre-lecteur, comparés aux fonctions de la lecture."""
from __future__ import annotations

import math
import sys
import time
from pathlib import Path

sys.path[:0] = ["/home/user/controle-ia-travail/src"]
import numpy as np  # noqa: E402
from scipy.stats import norm  # noqa: E402

from controle_ia.barreau8_moniteurs import lecture_sondes_v1 as L  # noqa: E402

quoi = sys.argv[1]


def aire_naive(s, y):
    p, n = s[y == 1], s[y == 0]
    tot = 0.0
    for a in p:
        tot += np.sum(a > n) + 0.5 * np.sum(a == n)
    return tot / (len(p) * len(n))


def d_manuel(s, P, y, blocs, n_tirages, graine, niveau):
    """Règle D à la main : mêmes tirages de tâches pour la sonde et chaque direction ; D* = A*_s − q0,95(A*_p)."""
    u = np.unique(blocs)
    membres = [np.flatnonzero(blocs == x) for x in u]
    rng = np.random.default_rng(graine)
    D, As = [], []
    for _ in range(n_tirages):
        ch = rng.integers(0, u.size, size=u.size)
        i = np.concatenate([membres[c] for c in ch])
        if len(set(y[i].tolist())) < 2:
            continue
        a_s = aire_naive(s[i], y[i])
        a_p = np.array([aire_naive(P[k, i], y[i]) for k in range(P.shape[0])])
        D.append(a_s - np.quantile(a_p, 0.95))
        As.append(a_s)
    a = (1 - niveau) / 2
    return np.quantile(D, a), np.quantile(D, 1 - a), np.quantile(As, a), np.quantile(As, 1 - a)


if quoi == "main":
    rng = np.random.default_rng(1)
    for essai in range(4):
        T, n = 7, 3
        blocs = np.repeat(np.arange(T), 2 * n)
        y = np.tile(np.r_[np.ones(n), np.zeros(n)], T).astype(int)
        s = np.round(rng.normal(size=y.size) + 0.8 * y, 1)          # ex aequo voulus
        P = np.round(rng.normal(size=(9, y.size)), 1)
        t = L.Tailles(n_tirages=150)
        r = L.comparer_au_plancher(s, P, y, blocs, L.NIVEAU_DECISIF, 4242 + essai, t)
        b, h, bs, hs = d_manuel(s, P, y, blocs, 150, 4242 + essai, L.NIVEAU_DECISIF)
        print(f"essai {essai}: aire code {r['aire']:.6f} naïve {aire_naive(s, y):.6f} | D bas code {r['difference']['bas']:.6f} "
              f"main {b:.6f} | D haut code {r['difference']['haut']:.6f} main {h:.6f} | IC sonde code [{r['bas']:.6f},{r['haut']:.6f}] "
              f"main [{bs:.6f},{hs:.6f}] | q95 plancher code {r['plancher_quantile']:.6f} main "
              f"{np.quantile([aire_naive(P[k], y) for k in range(9)], 0.95):.6f} | état {r['etat']} ; main {'au-dessus' if b > 0 else 'non au-dessus'}")
    # graine entière : premier mot de 64 bits
    from controle_ia import manifeste
    g = manifeste.graines(["intervalle/x/B100-contre-H"], 99)
    ss = np.random.SeedSequence(99, spawn_key=(manifeste.cle_de_tache("intervalle/x/B100-contre-H"),))
    print("graine entière code", L.graine_entiere(g, "intervalle/x/B100-contre-H"), "main", int(ss.generate_state(1, dtype=np.uint64)[0]))
    # étalonnage de la recette : aire empirique à f = 1, sans bootstrap
    rec = L.Recette()
    for a in rec.aires:
        aires = []
        for k in range(60):
            dd = L.donnees_synthetiques(np.random.default_rng(k), rec, a, 1.0)
            s = np.r_[dd["sonde"]["B100"].ravel(), dd["sonde"]["H"].ravel()]
            yy = np.r_[np.ones(640), np.zeros(640)]
            from controle_ia.sondes.evaluation import aire_sous_courbe
            aires.append(aire_sous_courbe(s, yy))
        th = norm.cdf(L.decalage_de_la_recette(a) / math.sqrt(2.5))
        print(f"recette a={a}: Δ={L.decalage_de_la_recette(a):.4f} Φ(Δ/√2,5)={th:.4f} aire simulée moyenne {np.mean(aires):.4f} ± {np.std(aires)/math.sqrt(60):.4f}")
    # fraction : nombre exact d'actions décalées
    dd0 = L.donnees_synthetiques(np.random.default_rng(5), rec, 0.7, 0.25)
    print("plancher forme", dd0["plancher"]["H"].shape, "sonde forme", dd0["sonde"]["B50"].shape)

if quoi == "nul":
    # Taux de fausse alerte de la règle entière (clauses 1 et 3, trois sondes, deux conditions) sous un nul synthétique,
    # à petite taille : 16 tâches, 6 actions par tâche et condition, 40 directions, 300 tirages.
    reps, T, n, K, B = int(sys.argv[2]), 16, 6, 40, 300
    effet = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
    t = L.Tailles(n_tirages=B)
    rng = np.random.default_rng(20261119)
    compte = {"clause1_par_sonde": 0, "porteuse_par_condition": 0, "U_aux_deux": 0, "clause1_095": 0}
    debut = time.time()
    for r in range(reps):
        tache_eff = rng.normal(0, 0.5, (3 + K * 3, T))
        donnees = {}
        for c in L.CONDITIONS:
            x = rng.normal(size=(3 + 3 * K, T, n)) + tache_eff[:, :, None]
            if effet and c in ("B100", "B50"):
                x[0] += effet                         # effet planté sur la première sonde seulement
            donnees[c] = x.reshape(3 + 3 * K, -1)
        blocs1 = np.repeat(np.arange(T), n)
        etats = []
        for c in ("B100", "B50"):
            porteuses = []
            for k in range(3):
                lignes_ = []
                for neg in ("H", "TJ100"):
                    s = np.r_[donnees[c][k], donnees[neg][k]]
                    P = np.c_[donnees[c][3 + k * K:3 + (k + 1) * K], donnees[neg][3 + k * K:3 + (k + 1) * K]]
                    y = np.r_[np.ones(T * n), np.zeros(T * n)].astype(int)
                    blocs = np.r_[blocs1, blocs1]
                    g = int(rng.integers(0, 2**63))
                    res = L.comparer_au_plancher(s, P, y, blocs, L.NIVEAU_DECISIF, g, t)
                    lignes_.append(res["etat"] == L.AU_DESSUS)
                    if neg == "H":
                        compte["clause1_par_sonde"] += res["etat"] == L.AU_DESSUS
                        compte["clause1_095"] += L.comparer_au_plancher(s, P, y, blocs, 0.95, g, t)["etat"] == L.AU_DESSUS
                porteuses.append(all(lignes_))
            compte["porteuse_par_condition"] += any(porteuses)
            etats.append(any(porteuses))
        compte["U_aux_deux"] += all(etats)
    print(f"effet {effet} ; {reps} répétitions ; {time.time() - debut:.0f} s")
    print(f"clause (1) au-dessus par sonde et condition (niveau décisif) : {compte['clause1_par_sonde']}/{reps * 6} = {compte['clause1_par_sonde'] / (reps * 6):.4f}")
    print(f"clause (1) au-dessus par sonde et condition (niveau 0,95) : {compte['clause1_095']}/{reps * 6} = {compte['clause1_095'] / (reps * 6):.4f}")
    print(f"au moins une porteuse à une condition : {compte['porteuse_par_condition']}/{reps * 2} = {compte['porteuse_par_condition'] / (reps * 2):.4f}")
    print(f"état U aux deux conditions (L1) : {compte['U_aux_deux']}/{reps}")

if quoi == "recette":
    rec = L.Recette()
    debut = time.time()
    dd = L.donnees_synthetiques(np.random.default_rng(0), rec, 0.7, 1.0)
    p = L._regle_simulee(dd, rec, {(c, n): 100 + k for k, (c, n) in enumerate([(c, n) for c in ("B50", "B100") for n in ("H", "TJ100")])})
    print("une répétition de la recette aux tailles du texte :", round(time.time() - debut, 1), "s ;", p)
