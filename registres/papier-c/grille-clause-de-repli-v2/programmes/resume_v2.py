"""Mise en tables du rapport v2 de la grille de la clause de repli (aucun calcul de simulation).

Ecrit le 2026-11-22 pendant le lot, avant la lecture de tout taux neuf ; fige avant son execution
(sha256sums-programme-resume-v2.txt). Refuse de mettre en tables si la garde de completude n'est pas saine.

Pour chaque case de la liste finie : origine de la sortie (v1 reprise, v2 neuve), taux de « etablie » aux trois
lectures jointes (regle du texte) et son erreur de Monte-Carlo, seuil, au-dessus ou non (strictement) ; pour
information : les deux premieres lectures jointes. Par ligne : cases couvertes sur la liste, plus haut taux et sa case,
cases au-dessus du seuil, issue au sens du texte (constat mecanique).

Usage : python3 -B resume_v2.py LISTE.md SORTIE.md SORTIE.json DOSSIER_SORTIES [DOSSIER_SORTIES ...]
"""
import json
import os
import sys
from statistics import NormalDist

from liste_et_garde_v2 import (CLE_A, CLE_B, CLE_C, CLE_I, cle, collecter, lire_liste, type_sortie,
                               verifier_completude)

SEUIL = {1000: 0.05 + 2 * (0.05 * 0.95 / 1000) ** 0.5, 8000: 0.05 + 2 * (0.05 * 0.95 / 8000) ** 0.5}


def f3(x):
    return "—" if x is None else f"{x:.3f}".replace(".", ",")


def f4(x):
    return f"{x:.4f}".replace(".", ",")


def gtxt(g):
    return {0.0: "0", 0.1: "0,10", 0.2: "0,20"}[g]


def borne_d0():
    """Borne exacte de P(D0 <= 0) pour un juge et un essai, sur les cases reprises de v1 (T >= 45, s0 <= 0,6) :
    S_t - H_t = 2 + (r_S - r_H) + (e_S - e_H), gaussien de variance 2 x 0,8^2 + 2 x s0^2 (l'effet de tache s'annule) ;
    D0 = moyenne sur T taches, gaussien exact."""
    sd = ((2 * 0.64 + 2 * 0.36) / 45) ** 0.5
    return NormalDist().cdf(-2 / sd), 2 / sd


def main():
    liste, sortie_md, sortie_json, dossiers = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
    cases = lire_liste(liste)
    sorties = collecter(dossiers)
    bilan = verifier_completude(cases, sorties)  # leve GardeCompletude si incomplete : rien n'est mis en tables
    par = {"ab": {}, "c": {}}
    for nom, s in sorties:
        par[type_sortie(nom)][(s["modele"], s["attaque"], s["k"], s["T"])] = (nom, s)
    lignes = []
    res = dict(bilan_completude=bilan, cases=[], lignes={})
    acc = {x: [] for x in ("C-P3a", "C-P3b", "C-P3c insertion", "C-P3c contenu")}
    acc2 = {x: [] for x in ("C-P3c insertion (deux lectures)", "C-P3c contenu (deux lectures)")}
    for c in cases:
        nab, sab = par["ab"][cle(c)]
        nc, sc = par["c"][cle(c)]
        oab = "v1" if "reprises-v1" in nab else "v2"
        oc = "v1" if "reprises-v1" in nc else "v2"
        ta, tb = sab["taux"][CLE_A], sab["taux"][CLE_B]
        ea, eb = sab["erreur_mc"][CLE_A], sab["erreur_mc"][CLE_B]
        ti, tci = sc["taux"][CLE_I], sc["taux"].get(CLE_C)
        ei, eci = sc["erreur_mc"][CLE_I], sc["erreur_mc"].get(CLE_C)
        ti2 = sc["taux"]["insertion_kP3_lie|conj2"]
        tc2 = sc["taux"].get("contenu_kP3_lie|conj2")
        sab_, sc_ = SEUIL[sab["R"]], SEUIL[sc["R"]]
        if abs(sab["seuil_clause"] - sab_) > 1e-12 or abs(sc["seuil_clause"] - sc_) > 1e-12:
            raise SystemExit(f"case {c['case']} : seuil ecrit dans la sortie different du seuil du texte")
        d0 = sc.get("essais_D0_non_positif")
        ctl_ab = sab.get("essais_controles")
        enr = dict(case=c["case"], modele=c["modele"], g=c["g"], k=c["k"], T=c["T"], origine_ab=oab, origine_c=oc,
                   sortie_ab=os.path.relpath(nab), sortie_c=os.path.relpath(nc), R_ab=sab["R"], B_ab=sab["B"],
                   R_c=sc["R"], seuil_ab=sab_, seuil_c=sc_, CP3a=ta, CP3a_mc=ea, CP3b=tb, CP3b_mc=eb,
                   CP3c_insertion=ti, CP3c_insertion_mc=ei, CP3c_contenu=tci, CP3c_contenu_mc=eci,
                   CP3c_insertion_deux_lectures=ti2, CP3c_contenu_deux_lectures=tc2,
                   CP3c_essais_D0_non_positif=d0, CP3c_essais_G_non_fini=sc.get("essais_G_non_fini"),
                   CP3c_essais_ex_aequo=sc.get("essais_avec_ex_aequo"), ab_controles=ctl_ab,
                   graine_ab=sab["graine"], graine_c=sc["graine"], duree_ab_s=sab.get("duree_s"),
                   duree_c_s=sc.get("duree_s"))
        res["cases"].append(enr)
        acc["C-P3a"].append((ta, sab_, c["case"]))
        acc["C-P3b"].append((tb, sab_, c["case"]))
        acc["C-P3c insertion"].append((ti, sc_, c["case"]))
        if tci is not None:
            acc["C-P3c contenu"].append((tci, sc_, c["case"]))
            acc2["C-P3c contenu (deux lectures)"].append((tc2, sc_, c["case"]))
        acc2["C-P3c insertion (deux lectures)"].append((ti2, sc_, c["case"]))
        lignes.append(
            f"| {c['case']} | {c['modele']} | {gtxt(c['g'])} | {c['k']} | {c['T']} | {oab} | "
            f"{f3(ta)} ± {f3(ea)}{' **>**' if ta > sab_ else ''} | {f3(tb)} ± {f3(eb)}{' **>**' if tb > sab_ else ''} | "
            f"{oc} | {f3(ti)} ± {f3(ei)}{' **>**' if ti > sc_ else ''} | "
            + ("non défini" if tci is None else f"{f3(tci)} ± {f3(eci)}{' **>**' if tci > sc_ else ''}")
            + f" | {'—' if d0 is None else d0} | {f3(ti2)} | {'non défini' if tc2 is None else f3(tc2)} |")

    def resume(v):
        hi = max(v, key=lambda x: x[0])
        au = [x[2] for x in v if x[0] > x[1]]
        return dict(cases=len(v), plus_haut=hi[0], case_plus_haut=hi[2], seuil=hi[1], au_dessus=au,
                    nb_au_dessus=len(au), plus_bas=min(x[0] for x in v))
    for nom, v in acc.items():
        res["lignes"][nom] = resume(v)
    for nom, v in acc2.items():
        res["lignes"][nom + ", pour information"] = resume(v)
    complet = all(b["couvertes"] == b["liste"] for b in bilan.values())
    issues = {}
    for ligne, comps in (("C-P3a", ["C-P3a"]), ("C-P3b", ["C-P3b"]),
                         ("C-P3c", ["C-P3c insertion", "C-P3c contenu"])):
        n = sum(res["lignes"][x]["nb_au_dessus"] for x in comps)
        if not complet:
            issues[ligne] = "issue 3, « rapport incomplet »"
        elif n == 0:
            issues[ligne] = "issue 1, « la clause ne joue pas pour la ligne »"
        else:
            issues[ligne] = "issue 2, « la clause joue pour la ligne »"
    res["complet"] = complet
    res["issues_constat"] = issues
    p, z = borne_d0()
    res["borne_D0_reprises"] = dict(prob_par_juge_et_essai=p, z=z)
    v2 = [e for e in res["cases"] if e["origine_c"] == "v2"]
    res["CP3c_D0_non_positif_total_v2"] = sum(e["CP3c_essais_D0_non_positif"] for e in v2)
    res["CP3c_G_non_fini_total_v2"] = sum(e["CP3c_essais_G_non_fini"] for e in v2)
    res["CP3c_ex_aequo_total"] = sum(e["CP3c_essais_ex_aequo"] for e in res["cases"])
    res["ab_controles_total_v2"] = {k: sum(e["ab_controles"][k] for e in res["cases"] if e["origine_ab"] == "v2")
                                    for k in ("non_fini_A", "non_fini_B", "egalite_A", "egalite_B")}
    with open(sortie_json, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    md = ["# Tables de la grille de la clause de repli — rapport v2", "",
          "Produites par `programmes/resume_v2.py` à partir des 144 + 144 sorties de première passe (garde de "
          "complétude saine). Taux de « établie » aux trois lectures jointes ± erreur de Monte-Carlo ; « **>** » : "
          f"strictement au-dessus du seuil de la case (C-P3a et C-P3b : {f4(SEUIL[1000])}, R = 1 000, B = 1 000 ; "
          f"C-P3c : {f4(SEUIL[8000])}, R = 8 000). Origine : v1 = sortie reprise du rapport v1 ; v2 = jouée pour ce "
          "rapport. D₀ ≤ 0 : essais où D₀ ≤ 0 chez un juge (comptés « non établie ») ; « — » : non compté par le "
          "programme de v1 (borne au rapport). Deux dernières colonnes : C-P3c aux deux premières lectures jointes, "
          "pour information (hors liste, sauf sous la version (b)).", "",
          "| case | modèle | g | k | T | origine | C-P3a | C-P3b | origine | C-P3c insertion | C-P3c contenu | "
          "D₀ ≤ 0 | C-P3c insertion, deux lectures | C-P3c contenu, deux lectures |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"] + lignes + ["", "## Par ligne", "",
          "| ligne | cases | plus bas | plus haut (case) | seuil | cases au-dessus |", "|---|---|---|---|---|---|"]
    for nom, r in res["lignes"].items():
        md.append(f"| {nom} | {r['cases']} | {f3(r['plus_bas'])} | {f3(r['plus_haut'])} (case {r['case_plus_haut']}) "
                  f"| {f4(r['seuil'])} | {r['nb_au_dessus']}{' : ' + ', '.join(r['au_dessus']) if r['au_dessus'] else ''} |")
    md += ["", "## Issue au sens du texte (constat mécanique)", ""]
    md += [f"- {k} : {v}" for k, v in issues.items()]
    md.append("")
    with open(sortie_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print("tables ecrites ; complet :", complet)
    return 0


if __name__ == "__main__":
    sys.exit(main())
