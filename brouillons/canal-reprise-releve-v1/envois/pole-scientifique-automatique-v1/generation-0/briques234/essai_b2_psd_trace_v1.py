"""Brique 2, essais 1 et 2 : semi-définie positivité de la forme du rapport ; forme « trace ».

Usage : python3 -I -B essai_b2_psd_trace_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"""
import argparse
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import numpy as np

import commun_v1 as cm

N, DIM, JEUX = 20, 16, 1000
SEUIL = -1e-8
MAX_ITER_CONVERGE = 5000
GAMMAS = [1e-6, 1e-3, 1e-2, 1e-1]


def racine_projecteur_numpy(d):
    p = np.eye(DIM) - np.outer(d, d)
    w, v = np.linalg.eigh(p)
    return (v * np.sqrt(np.clip(w, 0.0, None))) @ v.T


def racine_projecteur_jacobi(jac, d):
    p = np.eye(DIM) - np.outer(d, d)
    u, _ = jac([list(map(float, ligne)) for ligne in p], dim=DIM, max_iter=MAX_ITER_CONVERGE)
    u = np.array(u)
    lam = np.einsum("ik,ij,jk->k", u, p, u)
    return (u * np.sqrt(np.clip(lam, 0.0, None))) @ u.T


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    args = ap.parse_args()
    jac, emp_jac = cm.jacobi_organisme()
    t0 = time.time()

    res_a = {"lmin": [], "lmax": [], "n_neg": [], "diag_max_abs": [], "trace": [], "lmin_defaut120": [],
             "residu_max_converge": [], "residu_max_defaut120": [], "err_vs_lapack": [],
             "mineurs2_negatifs": [], "mineurs2_total": []}
    res_b = {"lmin": [], "lmax": [], "residu_max": []}
    res_c = {"lmin": [], "lmax": []}
    sk_a = {"lmin": [], "ecart_bistoch": [], "asym": [], "echec": 0, "violations_gamma": {str(g): 0 for g in GAMMAS},
            "gamma_min_requis": []}
    trace = {"err_14_plus_c2_numpy": 0.0, "err_14_plus_c2_jacobi": 0.0, "err_14_plus_c2_projecteur": 0.0,
             "err_idempotence": 0.0, "ecart_1_moins_c2": [],
             "pearson_T_c2": [], "T_min": np.inf, "T_max": -np.inf, "paires": 0}

    for r in range(JEUX):
        rng = cm.generateur("b2_psd", r)
        d = cm.unitaires(rng, N, DIM)
        o = cm.unitaires(rng, N, DIM)
        q = rng.uniform(0.5, 1.5, N)

        # Essai 1 : forme exacte du rapport
        la = cm.noyau_rapport(d, o, q)
        lam, _, resid = cm.valeurs_propres_jacobi(jac, la, MAX_ITER_CONVERGE)
        lam120, _, resid120 = cm.valeurs_propres_jacobi(jac, la, 120)
        ref = np.linalg.eigvalsh(la)
        res_a["lmin"].append(float(lam.min()))
        res_a["lmax"].append(float(lam.max()))
        res_a["n_neg"].append(int((lam < SEUIL).sum()))
        res_a["diag_max_abs"].append(float(np.abs(np.diag(la)).max()))
        res_a["trace"].append(float(np.trace(la)))
        res_a["lmin_defaut120"].append(float(lam120.min()))
        res_a["residu_max_converge"].append(float(resid.max()))
        res_a["residu_max_defaut120"].append(float(resid120.max()))
        res_a["err_vs_lapack"].append(float(np.abs(np.sort(lam) - ref).max()))
        iu = np.triu_indices(N, 1)
        mineurs = la[iu[0], iu[0]] * la[iu[1], iu[1]] - la[iu] ** 2
        res_a["mineurs2_negatifs"].append(int((mineurs < -1e-12).sum()))
        res_a["mineurs2_total"].append(int(mineurs.size))

        # Sinkhorn-Knopp (5 itérations) puis + gamma I sur la forme du rapport
        sk = cm.sinkhorn_knopp(la, 5)
        if sk is None:
            sk_a["echec"] += 1
        else:
            psym, ecart, asym = sk
            lam_sk, _, _ = cm.valeurs_propres_jacobi(jac, psym, MAX_ITER_CONVERGE)
            sk_a["lmin"].append(float(lam_sk.min()))
            sk_a["ecart_bistoch"].append(ecart)
            sk_a["asym"].append(asym)
            sk_a["gamma_min_requis"].append(float(-lam_sk.min()))
            for g in GAMMAS:
                if lam_sk.min() + g < SEUIL:
                    sk_a["violations_gamma"][str(g)] += 1

        # Essai 2 : forme trace, calculée explicitement par racines de matrices
        racines = [racine_projecteur_numpy(d[i]) for i in range(N)]
        t = np.array([[float(np.sum(racines[i] * racines[j])) for j in range(N)] for i in range(N)])
        c2 = (d @ d.T) ** 2
        projs = [np.eye(DIM) - np.outer(d[i], d[i]) for i in range(N)]
        trace["err_idempotence"] = max(trace["err_idempotence"], max(float(np.abs(p @ p - p).max()) for p in projs))
        tp = np.array([[float(np.sum(projs[i] * projs[j])) for j in range(N)] for i in range(N)])
        trace["err_14_plus_c2_projecteur"] = max(trace["err_14_plus_c2_projecteur"], float(np.abs(tp - (DIM - 2 + c2)).max()))
        trace["err_14_plus_c2_numpy"] = max(trace["err_14_plus_c2_numpy"], float(np.abs(t - (DIM - 2 + c2)).max()))
        trace["ecart_1_moins_c2"].append(float(np.abs(t - (1 - c2))[iu].min()))
        trace["pearson_T_c2"].append(float(np.corrcoef(t[iu], c2[iu])[0, 1]))
        trace["T_min"] = min(trace["T_min"], float(t[iu].min()))
        trace["T_max"] = max(trace["T_max"], float(t[iu].max()))
        trace["paires"] += len(iu[0])
        if r < 20:
            racines_j = [racine_projecteur_jacobi(jac, d[i]) for i in range(N)]
            tj = np.array([[float(np.sum(racines_j[i] * racines_j[j])) for j in range(N)] for i in range(N)])
            trace["err_14_plus_c2_jacobi"] = max(trace["err_14_plus_c2_jacobi"], float(np.abs(tj - (DIM - 2 + c2)).max()))
        lb = np.outer(q, q) * (o @ o.T) * t
        lam_b, _, resid_b = cm.valeurs_propres_jacobi(jac, lb, MAX_ITER_CONVERGE)
        res_b["lmin"].append(float(lam_b.min()))
        res_b["lmax"].append(float(lam_b.max()))
        res_b["residu_max"].append(float(resid_b.max()))

        # Correctif : diag(q) S diag(q), S = <d,d>^2 (gamma = 0, pour tester la seule semi-définie positivité)
        lc = cm.noyau_correctif(d, q, 0.0)
        lam_c, _, _ = cm.valeurs_propres_jacobi(jac, lc, MAX_ITER_CONVERGE)
        res_c["lmin"].append(float(lam_c.min()))
        res_c["lmax"].append(float(lam_c.max()))

    def resume(v):
        v = np.asarray(v, dtype=float)
        return {"min": float(v.min()), "q05": float(np.quantile(v, 0.05)), "mediane": float(np.median(v)),
                "q95": float(np.quantile(v, 0.95)), "max": float(v.max())}

    lmin_a = np.array(res_a["lmin"])
    lmax_a = np.array(res_a["lmax"])
    sortie = {
        "essai": "brique 2, essais 1 et 2",
        "heure_lancement_utc": args.heure,
        "duree_s": round(time.time() - t0, 1),
        "graines": cm.description_graines() | {"tache": "b2_psd", "spawn_key": "(1, r) pour r = 0..999"},
        "versions": cm.versions(),
        "instrument": {"fonction": "decomposer_jacobi_symetrique (copie exacte)", "empreinte_segment": emp_jac,
                       "max_iter_utilise": MAX_ITER_CONVERGE,
                       "signe": "quotient de Rayleigh u_k^T L u_k (la fonction renvoie |lambda|)"},
        "parametres": {"n": N, "dimension": DIM, "jeux": JEUX, "q": "uniforme [0,5 ; 1,5]", "seuil_violation": SEUIL},
        "forme_rapport": {
            "jeux_violation_lmin_lt_seuil": int((lmin_a < SEUIL).sum()),
            "jeux_violation_defaut_120_iter": int((np.array(res_a["lmin_defaut120"]) < SEUIL).sum()),
            "lambda_min": resume(lmin_a),
            "lambda_max": resume(lmax_a),
            "rapport_lmin_sur_lmax": resume(lmin_a / lmax_a),
            "nb_valeurs_propres_negatives": resume(res_a["n_neg"]),
            "diagonale_max_abs": float(np.max(res_a["diag_max_abs"])),
            "trace_max_abs": float(np.max(np.abs(res_a["trace"]))),
            "mineurs_2x2_negatifs": int(np.sum(res_a["mineurs2_negatifs"])),
            "mineurs_2x2_total": int(np.sum(res_a["mineurs2_total"])),
            "residu_max_converge": float(np.max(res_a["residu_max_converge"])),
            "residu_max_defaut_120_iter": resume(res_a["residu_max_defaut120"]),
            "ecart_max_vs_lapack": float(np.max(res_a["err_vs_lapack"])),
        },
        "forme_rapport_sinkhorn5_plus_gamma": {
            "echecs_sinkhorn": sk_a["echec"],
            "lambda_min_apres_sinkhorn": resume(sk_a["lmin"]),
            "ecart_bistochastique_5_iter": resume(sk_a["ecart_bistoch"]),
            "asymetrie_version_non_symetrisee": resume(sk_a["asym"]),
            "violations_par_gamma": sk_a["violations_gamma"],
            "gamma_minimal_requis": resume(sk_a["gamma_min_requis"]),
            "borne_theorique_bistochastique_diag_nulle": 1.0 / (N - 1),
        },
        "forme_trace": {
            "paires_testees": trace["paires"],
            "err_max_T_vs_14_plus_c2_numpy": trace["err_14_plus_c2_numpy"],
            "err_max_T_vs_14_plus_c2_jacobi_20_jeux": trace["err_14_plus_c2_jacobi"],
            "err_max_idempotence_P2_moins_P": trace["err_idempotence"],
            "err_max_TrPiPj_vs_14_plus_c2_racine_exacte_P": trace["err_14_plus_c2_projecteur"],
            "note_precision": "racine numérique : erreur en racine de epsilon (valeur propre nulle) ; P projecteur donc P^(1/2) = P exactement",
            "ecart_min_T_vs_1_moins_c2": float(np.min(trace["ecart_1_moins_c2"])),
            "T_min": trace["T_min"], "T_max": trace["T_max"],
            "pearson_T_c2_min": float(np.min(trace["pearson_T_c2"])),
            "jeux_violation_lmin_lt_seuil": int((np.array(res_b["lmin"]) < SEUIL).sum()),
            "lambda_min": resume(res_b["lmin"]),
            "residu_max": float(np.max(res_b["residu_max"])),
        },
        "correctif_sans_gamma": {
            "jeux_violation_lmin_lt_seuil": int((np.array(res_c["lmin"]) < SEUIL).sum()),
            "lambda_min": resume(res_c["lmin"]),
        },
    }
    cm.ecrire_json(cm.SORTIE / "resultats-b2-psd-trace-v1.json", sortie)
    print(f"fini en {sortie['duree_s']} s")


if __name__ == "__main__":
    main()
