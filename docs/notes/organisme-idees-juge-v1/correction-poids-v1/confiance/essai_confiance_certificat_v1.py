"""Vérification du majorant certifié « maximum sur l'ensemble de confiance » (dualité de Lagrange + Frank-Wolfe) — v1.

Mise au point exploratoire. Pour 200 petits problèmes tirés au hasard (une partition à deux morceaux, J = 3 lois connues
aléatoires, K = 3 issues, 40 tirages évalués, 40 tirages de confiance), on compare la borne B de
`essai_confiance_banc_v1.borne_sur_ensemble` au maximum contraint calculé à part (SLSQP de scipy, huit départs,
paramètres bruts : rho, loi aveugle, poids par morceau) pour trois rayons r (kappa = sup l_c - r) et un kappa au-dessus du
sup (famille vide). Attendu : B >= optimum de référence (validité) ; B = -inf seulement si la contrainte est infaisable.
Usage : python -I essai_confiance_certificat_v1.py SORTIE.json
"""

import json
import os
import platform
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np  # noqa: E402
from scipy.optimize import minimize  # noqa: E402

import essai_confiance_banc_v1 as bc  # noqa: E402

RACINE = 20261115_32


def logv(theta, A, y, m):
    rho = theta[0]
    rt = theta[1:4]
    b0, b1 = theta[4:7], theta[7:10]
    p = (1 - rho) * np.where(m, A @ b1, A @ b0) + rho * rt[y]
    return float(np.log(np.maximum(p, 1e-300)).sum())


def reference(Ae, ye, me, Ac, yc, mc, kappa, rng, departs=8):
    cons = [{"type": "eq", "fun": lambda th: th[1:4].sum() - 1}, {"type": "eq", "fun": lambda th: th[4:7].sum() - 1},
            {"type": "eq", "fun": lambda th: th[7:10].sum() - 1},
            {"type": "ineq", "fun": lambda th: logv(th, Ac, yc, mc) - kappa}]
    best = -np.inf
    for _ in range(departs):
        th0 = np.concatenate([[rng.uniform(0, 0.5)], rng.dirichlet(np.ones(3)), rng.dirichlet(np.ones(3)), rng.dirichlet(np.ones(3))])
        r = minimize(lambda th: -logv(th, Ae, ye, me), th0, method="SLSQP", bounds=[(0, 1)] * 10, constraints=cons,
                     options={"maxiter": 500, "ftol": 1e-12})
        th = np.clip(r.x, 0, 1)
        ok = (abs(th[1:4].sum() - 1) < 1e-6 and abs(th[4:7].sum() - 1) < 1e-6 and abs(th[7:10].sum() - 1) < 1e-6
              and logv(th, Ac, yc, mc) >= kappa - 1e-7)
        if ok:
            best = max(best, logv(th, Ae, ye, me))
    return best


def main():
    sortie = sys.argv[1]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe")
    lignes, viol, marge_min = [], 0, np.inf
    vide_ok, vide_tot = 0, 0
    for r in range(200):
        rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(r,)))
        Ls = [bc.softmax_par(rng) for _ in range(3)]
        def tirer(n, theta_monde):
            z, g = bc.tirer_plan(rng, n)
            Lz = np.stack([bc.probas_softmax(p, z) for p in Ls], axis=1)
            m = z[:, 0] > 0.3
            P = bc.probas_membre(Lz, m, *theta_monde)
            y = bc.tirer_issues(rng, P)
            return bc.lignes(Lz, y), y, m
        # données évaluées et de confiance tirées de deux membres différents (pour que la contrainte morde)
        t1 = (0.1, rng.dirichlet(np.ones(3)), np.stack([rng.dirichlet(np.ones(3)) for _ in range(2)]))
        t2 = (0.1, rng.dirichlet(np.ones(3)), np.stack([rng.dirichlet(np.ones(3)) for _ in range(2)]))
        Ae, ye, me = tirer(40, t1)
        Ac, yc, mc = tirer(40, t2)
        Vc, _, _ = bc.em_certifie(Ac, yc, np.ones((1, 40)), mc[None, :], 2000)
        supc = float(Vc[0, 0])
        for rayon in (0.5, 2.0, 5.0, -1.0):
            kappa = supc - rayon
            B, U0, _, _ = bc.borne_sur_ensemble(Ae, ye, me[None, :], Ac, yc, mc[None, :], [kappa])
            b = float(B[0, 0])
            ref = reference(Ae, ye, me, Ac, yc, mc, kappa, rng)
            if rayon < 0:
                vide_tot += 1
                vide_ok += int(b == -np.inf)
            if np.isfinite(ref):
                marge = b - ref
                marge_min = min(marge_min, marge)
                viol += int(marge < -1e-7)
            lignes.append({"probleme": r, "rayon": rayon, "borne": b, "reference": ref, "sup_sans_contrainte": float(U0[0])})
    gains = [l["sup_sans_contrainte"] - l["borne"] for l in lignes if np.isfinite(l["borne"]) and l["rayon"] > 0]
    doc = {"essai": "essai_confiance_certificat_v1", "racine_seedsequence": RACINE, "derivation": "spawn_key=(r,)",
           "problemes": 200, "versions": {"python": platform.python_version(), "numpy": np.__version__},
           "violations_borne_sous_reference": viol, "marge_minimale_borne_moins_reference": marge_min,
           "kappa_au_dessus_du_sup_rendu_vide": [vide_ok, vide_tot],
           "baisse_du_majorant_par_la_contrainte_nat": {"mediane": float(np.median(gains)), "max": float(np.max(gains))},
           "lignes": lignes}
    with open(sortie, "w") as fh:
        json.dump(doc, fh)
    print(json.dumps({k: v for k, v in doc.items() if k != "lignes"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
