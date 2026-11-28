"""Diagnostic COMPLÉMENTAIRE, déclaré A POSTERIORI (écrit après l'arrêt nommé de la garde
sur l'item 29 de c2a et après le recalcul sur 200 textes). Non décisif ; il explique,
il ne remplace pas la garde gelée. Ne lit aucune sortie de l'extracteur.
Usage : python3 -I diagnostic_posthoc_v1.py DOSSIER_SORTIE
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.dont_write_bytecode = True  # pas de __pycache__ non scellé
sys.path.insert(0, str(Path(__file__).resolve().parent))
import verif_appariement_v3 as V  # même tokenisation, mêmes empreintes  # noqa: E402

PREFIXES_REFUS = ("i cannot", "i can't", "i can’t", "i won't", "i will not", "i'm not able", "i am not able")


def est_refus(resp):
    s = resp.strip().lower()
    return s.startswith(PREFIXES_REFUS) and len(s) < 300


def hongrois_max(R):
    """Affectation de somme maximale (Kuhn-Munkres, O(n^3)) ; renvoie assign[ligne] = colonne."""
    n = R.shape[0]
    C = -np.asarray(R, dtype=float)
    INF = float("inf")
    u = [0.0] * (n + 1); v = [0.0] * (n + 1); p = [0] * (n + 1); way = [0] * (n + 1)
    for i in range(1, n + 1):
        p[0] = i; j0 = 0
        minv = [INF] * (n + 1); used = [False] * (n + 1)
        while True:
            used[j0] = True; i0 = p[j0]; delta = INF; j1 = 0
            for j in range(1, n + 1):
                if not used[j]:
                    cur = C[i0 - 1, j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur; way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]; j1 = j
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta; v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]; p[j0] = p[j1]; j0 = j1
            if j0 == 0:
                break
    assign = [0] * n
    for j in range(1, n + 1):
        assign[p[j] - 1] = j - 1
    return assign


def main(sortie):
    sortie = Path(sortie)
    for p, att in V.EMPREINTES.items():
        if V.sha256(p) != att:
            raise V.ArretNomme(f"ARRET NOMME empreinte {p}")
    c2a = json.loads((V.DONNEES / "c2a_generations.json").read_text())
    c2b = json.loads((V.DONNEES / "c2b_generations.json").read_text())
    n200 = json.loads(V.N200.read_text())["texts"]
    W = [V.mots_pleins(t) for t in n200]
    L = n200[:30]; ML = W[:30]

    def rows(d, cond):
        return [sorted((r for r in d["rows"] if r["item"] == i and r["cond"] == cond), key=lambda r: r["k"]) for i in range(30)]

    R_ = {"c2a_neutre": rows(c2a, "neutral"), "c2b_neutre": rows(c2b, "neutral"),
          "c2a_hate": rows(c2a, "hate"), "c2b_praise": rows(c2b, "praise")}
    M_ = {k: [[V.mots_pleins(r["resp"]) for r in rr] for rr in v] for k, v in R_.items()}
    res = {"version": "diagnostic-posthoc-v1", "statut": "a posteriori, non décisif"}

    # A. Taux de refus (définition a posteriori)
    res["refus_neutres"] = {k: [sum(est_refus(r["resp"]) for r in R_[k][i]) for i in range(30)]
                            for k in ("c2a_neutre", "c2b_neutre", "c2a_hate", "c2b_praise")}

    # B. Mots discriminants contre chacun des 199 autres textes de n200
    def discr(reps_mots, j):
        out = []
        for c in range(len(n200)):
            if c == j or n200[c] == n200[j]:
                continue
            Uj, Uc = W[j] - W[c], W[c] - W[j]
            if not Uj or not Uc:
                out.append((c, None)); continue
            sj = np.mean([len(Uj & r) / len(Uj) for r in reps_mots])
            sc = np.mean([len(Uc & r) / len(Uc) for r in reps_mots])
            out.append((c, float(sj - sc)))
        vals = [(c, d) for c, d in out if d is not None]
        cmin, dmin = min(vals, key=lambda x: x[1])
        return {"D_min": round(dmin, 4), "concurrent": cmin,
                "n_concurrents_D_negatif_ou_nul": sum(1 for _, d in vals if d <= 0),
                "concurrents_non_testables": [c for c, d in out if d is None]}

    B = {}
    for bras, neu, pre in (("c2a", "c2a_neutre", "c2a_hate"), ("c2b", "c2b_neutre", "c2b_praise")):
        B[bras + "_neutres"] = [discr(M_[neu][j], j) for j in range(30)]
        B[bras + "_vingt_reponses"] = [discr(M_[neu][j] + M_[pre][j], j) for j in range(30)]
    res["mots_discriminants_contre_199"] = {
        k: {"items_D_min_negatif_ou_nul": [j for j, x in enumerate(v) if x["D_min"] <= 0],
            "D_min_global": min(x["D_min"] for x in v),
            "item_D_min_global": int(np.argmin([x["D_min"] for x in v])),
            "par_item": v} for k, v in B.items()}

    # C. Affectation de somme maximale sur la matrice 30x30
    C = {}
    mats = {}
    for k in M_:
        R = V.matrice(ML, M_[k]); mats[k] = R
        a = hongrois_max(R)
        C[k] = {"identite_optimale": a == list(range(30)), "ecarts": [(i, a[i]) for i in range(30) if a[i] != i]}
    Rpool = (mats["c2a_neutre"] + mats["c2b_neutre"]) / 2
    a = hongrois_max(Rpool)
    C["c2a_c2b_neutres_mis_en_commun"] = {"identite_optimale": a == list(range(30))}
    lig, col = V.marges(Rpool)
    C["c2a_c2b_neutres_mis_en_commun"]["marge_min"] = round(min(min(lig), min(col)), 4)
    C["c2a_c2b_neutres_mis_en_commun"]["item_marge_min"] = int(np.argmin([min(x, y) for x, y in zip(lig, col)]))
    # c2a : 20 réponses (neutre + hate) par item
    Ra20 = V.matrice(ML, [M_["c2a_neutre"][j] + M_["c2a_hate"][j] for j in range(30)])
    lig, col = V.marges(Ra20)
    C["c2a_vingt_reponses"] = {"marge_min": round(min(min(lig), min(col)), 4),
                               "identite_optimale": hongrois_max(Ra20) == list(range(30))}
    res["affectation_et_mise_en_commun"] = C

    # D. Item 29 de c2a : réponses non refus, meilleur texte réponse par réponse
    d29 = []
    for r, m in zip(R_["c2a_neutre"][29], M_["c2a_neutre"][29]):
        sc30 = [len(ML[i] & m) / len(ML[i]) for i in range(30)]
        sc200 = [len(W[i] & m) / len(W[i]) for i in range(200)]
        d29.append({"k": r["k"], "refus": est_refus(r["resp"]), "n_mots_reponse": len(m),
                    "meilleur_parmi_30": int(np.argmax(sc30)), "score_29": round(sc30[29], 4),
                    "max_30": round(max(sc30), 4), "meilleur_parmi_200": int(np.argmax(sc200)),
                    "mots_du_texte_29_presents": sorted(ML[29] & m)})
    res["c2a_item29_reponse_par_reponse"] = d29
    # même chose en excluant les refus (définition a posteriori)
    Rnr = V.matrice(ML, [[m for r, m in zip(R_["c2a_neutre"][j], M_["c2a_neutre"][j]) if not est_refus(r["resp"])] or M_["c2a_neutre"][j] for j in range(30)])
    lig, col = V.marges(Rnr)
    res["c2a_neutres_hors_refus"] = {"marge_ligne_29": round(lig[29], 4), "marge_colonne_29": round(col[29], 4),
                                     "marge_min": round(min(min(lig), min(col)), 4),
                                     "lignes_ou_colonnes_en_defaut": sorted({i for i, x in enumerate(lig) if x <= 0} | {j for j, x in enumerate(col) if x <= 0})}

    # E. Cohérence de l'indice d'item entre conditions d'un même bras (réponses contre réponses)
    E = {}
    for bras, a_, b_ in (("c2a", "c2a_neutre", "c2a_hate"), ("c2b", "c2b_neutre", "c2b_praise")):
        Rx = np.array([[np.mean([len(x & y) / max(1, len(x | y)) for x in M_[a_][i] for y in M_[b_][j]]) for j in range(30)] for i in range(30)])
        lig, col = V.marges(Rx)
        E[bras] = {"marge_min": round(min(min(lig), min(col)), 4),
                   "en_defaut": sorted({i for i, x in enumerate(lig) if x <= 0} | {j for j, x in enumerate(col) if x <= 0})}
    res["neutre_contre_pression_meme_bras"] = E

    out = sortie / "diagnostic-posthoc-v1.json"
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
    return res


if __name__ == "__main__":
    r = main(sys.argv[1])
    print("refus neutres c2a", r["refus_neutres"]["c2a_neutre"])
    print("refus neutres c2b", r["refus_neutres"]["c2b_neutre"])
    for k, v in r["mots_discriminants_contre_199"].items():
        print("discr", k, "D_min", v["D_min_global"], "item", v["item_D_min_global"], "items<=0", v["items_D_min_negatif_ou_nul"])
    print("affectation", json.dumps(r["affectation_et_mise_en_commun"]))
    print("c2a 29", json.dumps(r["c2a_item29_reponse_par_reponse"]))
    print("c2a hors refus", r["c2a_neutres_hors_refus"])
    print("neutre/pression", r["neutre_contre_pression_meme_bras"])
