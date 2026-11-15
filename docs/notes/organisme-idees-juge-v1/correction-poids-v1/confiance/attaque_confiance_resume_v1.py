"""Résumé des lots de l'attaque — v1. Programme du réfutateur, mise au point exploratoire, aucune revendication.

Usage : python -I -B attaque_confiance_resume_v1.py DOSSIER_DES_LOTS SORTIE.json [COMPARAISON_REJEU.json]
Lit tous les lots `taille-*`, `hors-*`, `serre-*`, `exact-*`, `exactm-*`, `certificat-*`, `ecart-*` du dossier et écrit un seul JSON :
taux de promotion et intervalles de Clopper-Pearson à 95 %, non-couverture, audit du certificat, artefacts, puissance
appariée (mêmes tirages, mêmes instants), part du prix du maximum certifié regagnée et son intervalle par rééchantillonnage
des mondes (graine écrite), et l'empreinte de chaque lot lu.
"""

import collections
import glob
import hashlib
import json
import math
import os
import sys

import numpy as np
from scipy.stats import beta as loi_beta
from scipy.stats import binomtest

RACINE_BOOT = 2026111578
ALPHA = 0.05


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def cp(k, n, niveau=0.95):
    a = (1 - niveau) / 2
    lo = 0.0 if k == 0 else float(loi_beta.ppf(a, k, n - k + 1))
    hi = 1.0 if k == n else float(loi_beta.ppf(1 - a, k + 1, n - k))
    return [round(lo, 5), round(hi, 5)]


def taux(k, n):
    return {"k": int(k), "n": int(n), "taux": round(k / n, 5) if n else None, "ic95": cp(int(k), int(n)) if n else None}


def apparie(a, b):
    """a, b : tableaux booléens ; rend a seul, b seul, valeur p bilatérale exacte des paires discordantes."""
    x, y = int((a & ~b).sum()), int((~a & b).sum())
    pv = float(binomtest(x, x + y, 0.5).pvalue) if x + y else 1.0
    return {"premier_seul": x, "second_seul": y, "difference_de_taux": round((x - y) / len(a), 5), "valeur_p": round(pv, 6)}


def repris(bb, v9, v8, cle):
    """Part du prix regagnée (bb - v9) / (v8 - v9), avec intervalle à 95 % par rééchantillonnage des mondes."""
    n = len(bb)
    d = v8.mean() - v9.mean()
    val = float((bb.mean() - v9.mean()) / d) if d > 0 else None
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_BOOT, spawn_key=cle))
    idx = rng.integers(0, n, size=(4000, n))
    num = bb[idx].mean(axis=1) - v9[idx].mean(axis=1)
    den = v8[idx].mean(axis=1) - v9[idx].mean(axis=1)
    ok = den > 0
    r = num[ok] / den[ok]
    return {"part": None if val is None else round(val, 4),
            "ic95_reechantillonnage": [round(float(np.percentile(r, 2.5)), 4), round(float(np.percentile(r, 97.5)), 4)] if ok.sum() > 100 else None,
            "difference_de_taux_bb_moins_v9": round(float(bb.mean() - v9.mean()), 5),
            "ic95_difference": [round(float(np.percentile(num, 2.5)), 5), round(float(np.percentile(num, 97.5)), 5)]}


def main():
    dossier, sortie = sys.argv[1], sys.argv[2]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe")
    doc = {"essai": "attaque_confiance_resume_v1", "racine_reechantillonnage": RACINE_BOOT, "sources": []}
    lots = collections.defaultdict(list)
    for p in sorted(glob.glob(os.path.join(dossier, "*.json"))):
        nom = os.path.basename(p)
        d = json.load(open(p))
        doc["sources"].append({"fichier": nom, "sha256": sha(p), "duree_s": d.get("duree_s")})
        lots[nom.split("-")[0]].append((nom, d))

    # ---- taille ----------------------------------------------------------------------------------------------------
    gr = collections.defaultdict(list)
    for nom, d in lots["taille"]:
        gr[d["cas"]].append(d)
    doc["taille"] = {}
    for cas, L in sorted(gr.items()):
        lignes = [l for d in L for l in d["lignes"]]
        mondes = sorted(l["monde"] for l in lignes)
        assert len(set(mondes)) == len(mondes)
        n = len(lignes)
        d0 = L[0]
        cartes = d0["cartes"]
        prom = collections.Counter()
        nc = collections.Counter()
        marge_min = {}
        marge_n = collections.Counter()
        viol = collections.Counter()
        calc = collections.Counter()
        for l in lignes:
            for meth, carte, _ in l["promues"]:
                prom[(meth, carte)] += 1
            for k in l["non_couvert"]:
                nc[k] += 1
            for k in l["calcule"]:
                calc[k] += 1
            for k, v in l["marge_min"].items():
                marge_n[k] += 1
                marge_min[k] = min(marge_min.get(k, math.inf), v)
                viol[k] += int(v < -1e-6)
        meths = sorted({k for l in lignes for k in l["marge_min"]} | set(nc) | {m for m, _ in prom})
        bb = [m for m in meths if m.startswith("BB_")]
        g = {"mondes": n, "J": d0["J"], "K": d0["K"], "n_tr": d0["n_tr"], "forme": d0["forme"], "audit_modulo": d0["audit_modulo"],
             "mondes_calcules_en_entier": {k: int(v) for k, v in sorted(calc.items())},
             "ecart_certificat_max_nat": max((l.get("ecart_certificat_max", 0.0) for l in lignes), default=0.0),
             "promotions": {}, "non_couverture": {}, "audit_certificat": {}, "artefacts": {}, "cartes_pari": {}}
        for m in bb + ["v9"]:
            g["promotions"][m] = {c: taux(prom[(m, c)], n) for c in cartes}
            g["promotions"][m]["toutes_cartes_au_plus_une_par_monde"] = None
        for m in bb:
            g["non_couverture"][m] = taux(nc[m], n)
        for m in meths:
            if m in marge_n:
                g["audit_certificat"][m] = {"mondes_couverts_calcules": int(marge_n[m]), "marge_min_nat": marge_min[m],
                                            "violations": int(viol[m])}
        for m in ("F1_en_ligne", "F2_moitie"):
            g["artefacts"][m] = {c: taux(prom[(m, c)], n) for c in ("copie", "hors_classe")}
        s25, s20 = math.log(1 / 0.04), math.log(1 / ALPHA)
        for c in ("pari_debut", "pari_milieu", "pari_fort", "hors_classe"):
            g["cartes_pari"][c] = {"mondes_ou_le_rapport_de_vraisemblance_passe_25": int(sum(l["log_lambda_max"][c] >= s25 for l in lignes)),
                                   "passe_20": int(sum(l["log_lambda_max"][c] >= s20 for l in lignes))}
        # promotion d'au moins une carte par monde, par méthode (borne la plus dure)
        for m in bb + ["v9"]:
            k = sum(any(p[0] == m for p in l["promues"]) for l in lignes)
            g["promotions"][m]["toutes_cartes_au_plus_une_par_monde"] = taux(k, n)
        doc["taille"][cas] = g

    # ---- hors du nul -----------------------------------------------------------------------------------------------
    gr = collections.defaultdict(list)
    for nom, d in lots["hors"]:
        gr[d["cas"]].append(d)
    doc["hors_nul"] = {}
    for ic, (cas, L) in enumerate(sorted(gr.items())):
        lignes = sorted([l for d in L for l in d["lignes"]], key=lambda l: l["monde"])
        n = len(lignes)
        seuils = L[0]["seuils_log"]
        meths = list(lignes[0]["w"].keys())
        cartes = list(lignes[0]["w"][meths[0]].keys())
        P = {m: {c: np.array([l["w"][m][c] >= seuils[m] for l in lignes]) for c in cartes} for m in meths}
        g = {"mondes": n, "n_tr": L[0]["n_tr"], "forme": L[0]["forme"], "parametre": L[0]["parametre"],
             "ecart_certificat_max_nat": max(l["ecart_certificat_max"] for l in lignes),
             "taux": {m: {c: taux(int(P[m][c].sum()), n) for c in cartes} for m in meths}, "apparie_contre_v9": {}, "repris": {},
             "richesse_max_des_cartes_membres_sous_v9": {c: max(l["w"]["v9"][c] for l in lignes) for c in cartes if c.startswith("membre")}}
        for m in meths:
            if m.startswith("BB_"):
                g["apparie_contre_v9"][m] = {c: apparie(P[m][c], P["v9"][c]) for c in cartes}
                g["repris"][m] = repris(P[m]["monde"], P["v9"]["monde"], P["v8"]["monde"], (ic, meths.index(m)))
        g["repris"]["limite"] = repris(P["limite"]["monde"], P["v9"]["monde"], P["v8"]["monde"], (ic, 99))
        # jeu dual : majorant certifié moins meilleure valeur atteinte par un point de l'ensemble (plus grand écart sur les
        # instants où un tel point a été trouvé). « au mieux » : taux si la richesse montait de tout ce jeu (indicatif).
        g["jeu_dual"] = {}
        for m in meths:
            if m in lignes[0]["jeu_dual_max"]:
                j = np.maximum(np.array([l["jeu_dual_max"][m] for l in lignes]), 0.0)
                wm = np.array([l["w"][m]["monde"] for l in lignes])
                g["jeu_dual"][m] = {"mediane_nat": float(np.median(j)), "decile_haut_nat": float(np.percentile(j, 90)),
                                    "max_nat": float(j.max()),
                                    "taux_au_mieux_si_la_borne_etait_exacte": taux(int((wm + j >= seuils[m]).sum()), n),
                                    "gain_de_richesse_contre_v9_nat": {
                                        "mediane": float(np.median(wm - np.array([l["w"]["v9"]["monde"] for l in lignes]))),
                                        "max": float((wm - np.array([l["w"]["v9"]["monde"] for l in lignes])).max()),
                                        "part_nulle": float((np.abs(wm - np.array([l["w"]["v9"]["monde"] for l in lignes])) < 1e-3).mean())}}
        # cartes membres du nul : richesse au-dessus de 1 (log W > 0) sous chaque méthode
        g["cartes_membres_richesse_au_dessus_de_1"] = {
            m: {c: int(sum(l["w"][m][c] > 1e-6 for l in lignes)) for c in cartes if c.startswith("membre")} for m in meths
            if m.startswith("BB_") or m == "v9"}
        doc["hors_nul"][cas] = g

    # ---- rejeu serré des mondes de l'auteur ------------------------------------------------------------------------
    gr = collections.defaultdict(list)
    for nom, d in lots["serre"]:
        gr[(d["cas"], d["n_tr"])].append(d)
    doc["rejeu_serre"] = {}
    for ic, ((cas, n_tr), L) in enumerate(sorted(gr.items())):
        lignes = sorted([l for d in L for l in d["lignes"]], key=lambda l: l["monde"])
        n = len(lignes)
        s20 = math.log(1 / ALPHA)
        sb = {b: math.log(1 / (ALPHA - b)) for b in (0.01, 0.025)}
        S = {k: np.array([l["serre"][k] for l in lignes]) for k in lignes[0]["serre"]}
        ps = {"v9": S["v9"] >= s20, "limite": S["limite"] >= s20, "v8": S["v8"] >= s20}
        for b in (0.01, 0.025):
            ps[f"coupe_grille_auteur|beta={b}"] = S[f"coupe_grille_auteur|beta={b}"] >= sb[b]
            ps[f"coupe_grille_union|beta={b}"] = S[f"coupe_grille_union|beta={b}"] >= sb[b]
        g = {"mondes": n, "premier": lignes[0]["monde"], "dernier": lignes[-1]["monde"],
             "ecart_certificat_max_nat_serre": max(l["ecart_certificat_max"] for l in lignes),
             "taux_serre": {k: taux(int(v.sum()), n) for k, v in ps.items()}, "serre": {}}
        avec_auteur = all(l["auteur"] is not None for l in lignes)
        if avec_auteur:
            Au = {k: np.array([l["auteur"][k] for l in lignes]) for k in lignes[0]["auteur"]}
            pa = {"v9_banc": Au["v9_banc"] >= s20, "limite": Au["limite"] >= s20, "v8_banc": Au["v8_banc"] >= s20}
            for b in (0.01, 0.025):
                pa[f"BB_T_coupe|beta={b}"] = Au[f"BB_T_coupe|beta={b}"] >= sb[b]
            dv = S["v9"] - Au["v9_banc"]
            g["taux_auteur"] = {k: taux(int(v.sum()), n) for k, v in pa.items()}
            g["ecart_de_richesse_v9_serre_moins_auteur_nat"] = {
                "mediane": float(np.median(dv)), "quartile_haut": float(np.percentile(dv, 75)), "max": float(dv.max()),
                "min": float(dv.min()), "part_au_dessus_de_1_nat": float((dv > 1.0).mean())}
            for nom_ref, cs, ca in (("limite", "limite", "limite"), ("v8", "v8", "v8_banc")):
                dd = S[cs] - Au[ca]
                g[f"ecart_de_richesse_{nom_ref}_serre_moins_auteur_nat"] = {"mediane": float(np.median(dd)), "max": float(dd.max()),
                                                                        "part_au_dessus_de_1_nat": float((dd > 1.0).mean())}
            g["v9_serre_contre_v9_auteur"] = apparie(ps["v9"], pa["v9_banc"])
            gagne = pa["BB_T_coupe|beta=0.01"] & ~pa["v9_banc"]
            g["paires_gagnees_par_le_coupe_de_l_auteur"] = {"nombre": int(gagne.sum()),
                                                            "dont_promues_par_le_v9_serre": int((gagne & ps["v9"]).sum())}
            g["auteur"] = {}
            for b in (0.01, 0.025):
                g["auteur"][f"beta={b}"] = {"coupe_contre_v9": apparie(pa[f"BB_T_coupe|beta={b}"], pa["v9_banc"]),
                                            "repris": repris(pa[f"BB_T_coupe|beta={b}"], pa["v9_banc"], pa["v8_banc"], (100 + ic, int(b * 1000)))}
        for b in (0.01, 0.025):
            for gn in ("auteur", "union"):
                k = f"coupe_grille_{gn}|beta={b}"
                g["serre"][k] = {"coupe_contre_v9": apparie(ps[k], ps["v9"]),
                                 "repris": repris(ps[k], ps["v9"], ps["v8"], (200 + ic, int(b * 1000), 0 if gn == "auteur" else 1)),
                                 "gain_de_richesse_coupe_moins_v9_nat": {"mediane": float(np.median(S[k] - S["v9"])),
                                                                         "quartile_haut": float(np.percentile(S[k] - S["v9"], 75)),
                                                                         "max": float((S[k] - S["v9"]).max()),
                                                                         "part_nulle": float((np.abs(S[k] - S["v9"]) < 1e-3).mean())}}
                if avec_auteur:
                    g["serre"][k]["coupe_serre_contre_v9_auteur"] = apparie(ps[k], pa["v9_banc"])
        doc["rejeu_serre"][f"{cas}|n_tr={n_tr}"] = g

    # ---- pièces rapportées telles quelles --------------------------------------------------------------------------
    doc["exact"] = {d["partie"]: d["blocs"] for _, d in lots["exact"]}
    doc["exact_morceaux"] = [{k: v for k, v in d.items() if k not in ("grille9", "gammas", "versions", "instants")}
                             for _, d in lots["exactm"]]
    doc["certificat"] = [{k: v for k, v in d.items() if k != "lignes"} for _, d in lots["certificat"]]
    doc["ecart_certificat_du_banc"] = [{k: v for k, v in d.items() if k != "lignes"} for _, d in lots["ecart"]]
    if len(sys.argv) > 3:
        c = json.load(open(sys.argv[3]))
        doc["rejeu_des_lots_de_l_auteur"] = {"lots": len(c), "valeurs_comparees": sum(r["valeurs"] for r in c),
                                             "ecarts_de_promotion": sum(r["ecarts_de_promotion"] for r in c),
                                             "ecarts_de_couverture": sum(r["ecarts_de_couverture"] for r in c),
                                             "ecart_max_de_log_richesse": max(r["ecart_max_log_w"] for r in c), "detail": c}
    with open(sortie, "w") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print("résumé écrit :", sortie, "; sources :", len(doc["sources"]))


if __name__ == "__main__":
    main()
