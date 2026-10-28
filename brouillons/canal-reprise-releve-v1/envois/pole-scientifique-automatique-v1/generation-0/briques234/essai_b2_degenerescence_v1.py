"""Brique 2, essai 3 (suite) : dégénérescence du tirage à taille fixe k = 4, n = 20.

Pour chaque noyau, loi exacte P(S) = det(L_S) / somme sur les 4 845 sous-ensembles de taille 4,
puis 50 tirages (une graine par tirage). Mesures : probabilité modale, nombre effectif d'ensembles
exp(entropie), ensembles distincts sur 50 graines (observé et espéré), espérances des mesures de
diversité, aplatissement des q (corrélation de rang entre q_i et la probabilité d'inclusion de i).
Usage : python3 -I -B essai_b2_degenerescence_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"""
import argparse
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import numpy as np
from scipy.stats import spearmanr

import commun_v1 as cm
import corpus_articles_v1 as ca

N, K, CORPUS, TIRAGES, GAMMA_REL = 20, 4, 20, 50, 1e-3
SWEEP_GAMMA = [0.0, 1e-2, 1e-1, 1.0, 10.0]


def lmax(m):
    return float(np.linalg.eigvalsh(m).max())


def noyaux(c):
    d, o, q = c["d"], c["o"], c["q"]
    s = (d @ d.T) ** 2
    la = cm.noyau_rapport(d, o, q)
    lb = cm.noyau_trace_ferme(d, o, q)
    lc = cm.noyau_correctif(d, q, 0.0)
    out = {"a_brut": la, "b_trace": lb, "c_correctif": lc}
    sk_a = cm.sinkhorn_knopp(la, 5)[0]
    out["a_sinkhorn_gamma_faible"] = sk_a + GAMMA_REL * lmax(sk_a) * np.eye(N)
    out["a_sinkhorn_gamma_min"] = sk_a + (-np.linalg.eigvalsh(sk_a).min() + 1e-9 * lmax(sk_a)) * np.eye(N)
    sk_b = cm.sinkhorn_knopp(lb, 5)
    out["b_trace_sinkhorn_gamma"] = None if sk_b is None else sk_b[0] + GAMMA_REL * lmax(sk_b[0]) * np.eye(N)
    out["c_gamma"] = cm.noyau_correctif(d, q, GAMMA_REL * lmax(s))
    sk_s = cm.sinkhorn_knopp(s, 5)[0]
    out["c_sinkhorn_sur_S_gamma"] = cm.noyau_correctif(d, q, 0.0, s_remplace=sk_s + GAMMA_REL * lmax(sk_s) * np.eye(N))
    sk_l = cm.sinkhorn_knopp(lc, 5)[0]
    out["c_sinkhorn_sur_L_gamma"] = sk_l + GAMMA_REL * lmax(sk_l) * np.eye(N)
    for g in SWEEP_GAMMA:
        out[f"c_gamma_rel_{g:g}"] = cm.noyau_correctif(d, q, g * lmax(s))
    return out


def glouton_permutations(l, rngs_perm, mode="signe"):
    """Glouton (déterministe) relancé sur 50 ordres du corpus : seule source de variation possible."""
    vus = set()
    for g in rngs_perm:
        perm = g.permutation(N)
        sel = cm.glouton_det(l[np.ix_(perm, perm)], K, mode)
        vus.add(tuple(sorted(int(perm[i]) for i in sel)))
    return len(vus)


def analyser(l, se, tables, q, rng_list, rngs_perm):
    m = se.shape[0]
    if l is None:
        return {"defini": False, "raison": "Sinkhorn impossible (somme non positive)"}
    glouton = {"glouton_distincts_50_permutations": glouton_permutations(l, rngs_perm)}
    dets = cm.dets_sous_ensembles(l, se)
    echelle = np.abs(dets).max()
    neg = int((dets < -1e-12 * echelle).sum())
    if neg > 0:
        glouton["glouton_abs_distincts_50_permutations"] = glouton_permutations(l, rngs_perm, "abs")
        return {"defini": False, "raison": "déterminants négatifs", "part_det_negatifs": neg / m} | glouton
    p = np.clip(dets, 0.0, None)
    p = p / p.sum()
    nz = p[p > 0]
    tirs = [int(g.choice(m, p=p)) for g in rng_list]
    pi = np.zeros(N)
    np.add.at(pi, se.ravel(), np.repeat(p, se.shape[1]))
    vp = np.sort(np.linalg.eigvalsh(l))[::-1]
    res = glouton | {
        "defini": True,
        "p_modale": float(p.max()),
        "n_effectif": float(np.exp(-(nz * np.log(nz)).sum())),
        "distincts_50_observe": len(set(tirs)),
        "distincts_50_espere": float((1.0 - (1.0 - p) ** TIRAGES).sum()),
        "part_trace_3_premieres_vp": float(vp[:3].sum() / vp.sum()),
        "spearman_q_inclusion": float(spearmanr(q, pi).statistic),
        "inclusion_max_sur_min": float(pi.max() / pi.min()),
        "diag_cv": float(np.std(np.diag(l)) / np.mean(np.diag(l))),
    }
    for k, v in tables.items():
        res["E_" + k] = float((p * v).sum())
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    args = ap.parse_args()
    t0 = time.time()
    se = cm.sous_ensembles(N, K)
    sortie_cfg = {}
    for config, cid in ca.CONFIGS.items():
        par_variante = {}
        for r in range(CORPUS):
            c = ca.corpus(cm.generateur("b2_degenerescence", cid, r), config, N)
            tables = ca.tables_sous_ensembles(c, se)
            for vid, (nom, l) in enumerate(noyaux(c).items()):
                rngs = [cm.generateur("b2_degenerescence", cid, r, 100 + vid, s) for s in range(TIRAGES)]
                rngs_perm = [cm.generateur("b2_degenerescence", cid, r, 200 + vid, s) for s in range(TIRAGES)]
                par_variante.setdefault(nom, []).append(analyser(l, se, tables, c["q"], rngs, rngs_perm))
            unif = {"p_modale": 1.0 / se.shape[0], "n_effectif": float(se.shape[0]),
                    "distincts_50_espere": float(se.shape[0] * (1 - (1 - 1.0 / se.shape[0]) ** TIRAGES))}
            for k, v in tables.items():
                unif["E_" + k] = float(v.mean())
            par_variante.setdefault("reference_uniforme", []).append(unif | {"defini": True})
        resume = {}
        for nom, lst in par_variante.items():
            definis = [x for x in lst if x.get("defini")]
            entree = {"corpus": len(lst), "corpus_definis": len(definis)}
            if not definis:
                entree["raison"] = lst[0].get("raison")
                parts = [x.get("part_det_negatifs") for x in lst if x.get("part_det_negatifs") is not None]
                if parts:
                    entree["part_det_negatifs_moyenne"] = float(np.mean(parts))
                for cle in ("glouton_distincts_50_permutations", "glouton_abs_distincts_50_permutations"):
                    v = [x[cle] for x in lst if cle in x]
                    if v:
                        entree[cle] = {"moyenne": float(np.mean(v)), "min": float(np.min(v)), "max": float(np.max(v))}
            else:
                for k in definis[0]:
                    if k == "defini":
                        continue
                    v = np.array([x[k] for x in definis], dtype=float)
                    entree[k] = {"moyenne": float(v.mean()), "min": float(v.min()), "max": float(v.max())}
            resume[nom] = entree
        sortie_cfg[config] = resume
        print(config, "fait", round(time.time() - t0, 1), "s")
    sortie = {
        "essai": "brique 2, essai 3 : dégénérescence et aplatissement des q (tirage exact de taille 4)",
        "heure_lancement_utc": args.heure,
        "duree_s": round(time.time() - t0, 1),
        "graines": cm.description_graines() | {"tache": "b2_degenerescence",
                                               "spawn_key": "(4, id_config, r) corpus ; (4, id_config, r, 100 + id_variante, s) tirage s ; (4, id_config, r, 200 + id_variante, s) permutation s du glouton"},
        "versions": cm.versions(),
        "parametres": {"n": N, "k": K, "corpus_par_config": CORPUS, "tirages_par_corpus": TIRAGES,
                       "gamma": "gamma = GAMMA_REL x plus grande valeur propre de la matrice régularisée",
                       "gamma_rel": GAMMA_REL, "sweep_gamma_rel_correctif": SWEEP_GAMMA,
                       "sinkhorn": "5 itérations alternées, version symétrique D A D (congruence)"},
        "resultats": sortie_cfg,
    }
    cm.ecrire_json(cm.SORTIE / "resultats-b2-degenerescence-v1.json", sortie)
    print("fini", sortie["duree_s"], "s")


if __name__ == "__main__":
    main()
