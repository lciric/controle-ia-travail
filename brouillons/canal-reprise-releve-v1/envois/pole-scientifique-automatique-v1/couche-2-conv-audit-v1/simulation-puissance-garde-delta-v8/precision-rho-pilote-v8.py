"""Précision de la mesure de ρ au pilote (pour la table de lecture T4) : si l'on estime ρ par la variance inter-unités des scores observés, combien le pilote l'estime-t-il mal ?

Modèle : N unités ; chaque unité a une probabilité p_u ~ Bêta d'espérance p et de corrélation intra-unité ρ (Var p_u = ρ p (1 − p)) ; K épisodes par unité ;
score observé s_u = (nombre de succès)/K. Estimateur (moments) : ρ̂ = (K·V/(p̄(1 − p̄)) − 1)/(K − 1), V = variance empirique (diviseur N − 1) des s_u, p̄ = moyenne des s_u.
Justification : Var(s_u) = p(1 − p)[1/K + ρ(1 − 1/K)] (variance totale = part binomiale + part inter-unités). L'estimateur n'est pas rapporté à la variance
des probabilités p_u (non observées) : c'est la correction de la part binomiale qui permet de lire ρ sur des scores observés. Pas de troncature à [0 ; 1] (le biais
de la troncature est écrit à part : part des estimations négatives).
Graines (R9) : SeedSequence([graine, sha256(étiquette)]) ; étiquette par cellule. 2 000 répétitions par cellule. Exploratoire, non opposable.

Usage : python3 -I -B precision-rho-pilote-v8.py SORTIE.json
"""
import hashlib
import json
import sys
import time

import numpy as np

SORTIE = sys.argv[1]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("lancer avec -B")
GRAINE, REPS, K = 20261029, 2000, 10
t0 = time.time()
res = {"graine": GRAINE, "repetitions": REPS, "K": K, "numpy": np.__version__, "cellules": []}
for p in (0.4, 0.01):
    for rho in (0.0, 0.05, 0.10, 0.17, 0.25):
        for N in (50, 100, 288):
            etiquette = f"precision-rho|p={p}|rho={rho}|N={N}|K={K}"
            reduit = int.from_bytes(hashlib.sha256(etiquette.encode()).digest()[:8], "big")
            rng = np.random.default_rng(np.random.SeedSequence([GRAINE, reduit]))
            if rho == 0.0:
                pu = np.full((REPS, N), p)
            else:
                pu = rng.beta(p * (1 - rho) / rho, (1 - p) * (1 - rho) / rho, size=(REPS, N))
            s = rng.binomial(K, pu) / K
            pbar = s.mean(axis=1)
            V = s.var(axis=1, ddof=1)
            with np.errstate(divide="ignore", invalid="ignore"):
                rho_hat = (K * V / (pbar * (1 - pbar)) - 1) / (K - 1)
            ok = np.isfinite(rho_hat)
            r = rho_hat[ok]
            lo, hi = np.quantile(r, [0.05, 0.95])
            res["cellules"].append({"p": p, "rho": rho, "N": N, "graine_derivee": reduit, "estimations_definies": float(ok.mean()),
                                    "moyenne": float(r.mean()), "ecart_type": float(r.std(ddof=1)), "quantile_5": float(lo), "quantile_95": float(hi),
                                    "part_negatives": float((r < 0).mean())})
            print(res["cellules"][-1], flush=True)
res["duree_s"] = round(time.time() - t0, 1)
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
