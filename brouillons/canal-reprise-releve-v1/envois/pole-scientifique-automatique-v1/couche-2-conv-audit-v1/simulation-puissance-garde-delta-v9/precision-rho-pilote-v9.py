"""Précision de la mesure de ρ au pilote, v9 (GD8-01) : même modèle, même estimateur, mêmes étiquettes de graine que `precision-rho-pilote-v8.py`
(les cellules communes reproduisent la v8 à l'identique : vérifié en fin de script contre la sortie v8), grille de ρ prolongée pour la table en ρ̂ :
ρ ∈ {0 ; 0,05 ; 0,10 ; 0,125 ; 0,17 ; 0,20 ; 0,25 ; 0,30 ; 0,35 ; 0,40}, N ∈ {50 ; 100 ; 288}, côté sabotage (p = 0,4) seulement (le côté honnête est
inutilisable pour lire ρ, v8 § 1).

Modèle : N unités ; p_u ~ Bêta d'espérance p et de corrélation intra-unité ρ ; K = 10 épisodes par unité ; s_u = succès/K.
Estimateur (moments) : ρ̂ = (K·V/(p̄(1 − p̄)) − 1)/(K − 1), V variance empirique (diviseur N − 1) des s_u.
Graines (R9) : SeedSequence([20261029, sha256(étiquette)]) ; étiquette « precision-rho|p=…|rho=…|N=…|K=10 ». 2 000 répétitions par cellule.
Manifeste écrit par ce script (GD8-09). Exploratoire, non opposable.
Usage : python3 -I -B precision-rho-pilote-v9.py COMMIT SORTIE_V8.json SORTIE.json
"""
import hashlib
import json
import os
import platform
import sys
import time
from datetime import datetime, timezone

import numpy as np

COMMIT, V8, SORTIE = sys.argv[1:4]
if not sys.flags.dont_write_bytecode:
    raise SystemExit("lancer avec -B")
GRAINE, REPS, K = 20261029, 2000, 10
t0, debut = time.time(), datetime.now(timezone.utc)
res = {"script": os.path.basename(__file__), "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
       "graine": GRAINE, "repetitions": REPS, "K": K, "numpy": np.__version__, "cellules": []}
for p in (0.4,):
    for rho in (0.0, 0.05, 0.10, 0.125, 0.17, 0.20, 0.25, 0.30, 0.35, 0.40):
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
v8 = json.load(open(V8, encoding="utf-8"))
communs = 0
diff = []
for c in res["cellules"]:
    for c8 in v8["cellules"]:
        if c8["p"] == c["p"] and c8["rho"] == c["rho"] and c8["N"] == c["N"]:
            communs += 1
            if c8 != c:
                diff.append((c["rho"], c["N"]))
res["identite_v8"] = {"sortie_v8_sha256": hashlib.sha256(open(V8, "rb").read()).hexdigest(), "cellules_communes": communs, "differences": diff}
res["duree_s"] = round(time.time() - t0, 1)
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
fin = datetime.now(timezone.utc)
man = {"passage": os.path.basename(SORTIE)[:-5], "ecrit_par": os.path.basename(__file__), "commit_lu_par_l_appelant": COMMIT,
       "date_utc_debut": debut.strftime("%Y-%m-%dT%H:%M:%SZ"), "date_utc_fin": fin.strftime("%Y-%m-%dT%H:%M:%SZ"), "commande": sys.argv,
       "script_sha256": res["script_sha256"], "graines": {"graine_maitresse": GRAINE, "derivation": "SeedSequence([graine, 8 premiers octets de sha256(étiquette)])",
                                                         "par_cellule": {f"rho={c['rho']}|N={c['N']}": c["graine_derivee"] for c in res["cellules"]}},
       "configuration": {"p": 0.4, "K": K, "repetitions": REPS}, "environnement": {"python": platform.python_version(), "numpy": np.__version__},
       "fichiers": {os.path.basename(SORTIE): hashlib.sha256(open(SORTIE, "rb").read()).hexdigest()}}
with open(os.path.join(os.path.dirname(os.path.abspath(SORTIE)), "manifeste-" + os.path.basename(SORTIE)), "x", encoding="utf-8") as f:
    json.dump(man, f, indent=1, ensure_ascii=False)
    f.write("\n")
for c in res["cellules"]:
    print("ρ = %.3f N = %3d : moyenne %.4f écart-type %.4f" % (c["rho"], c["N"], c["moyenne"], c["ecart_type"]))
print("identité v8 :", res["identite_v8"])
