"""Compare, champ par champ, l'application de l'agent du verdict à l'aide du
code (`criteres_mecaniques`). Geste 5 du mandat, fait après les gestes 1 à 4.
Usage : python3 -I -B comparer_a_l_aide_v1.py APPLICATION.json AIDE.json SORTIE.json
"""
import json
import sys


def main():
    app_p, aide_p, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(app_p, encoding="utf-8") as f:
        app = json.load(f)
    with open(aide_p, encoding="utf-8") as f:
        aide = json.load(f)["criteres_mecaniques"]
    out = {"desaccords": [], "controles": {}}

    def comparer(nom, mien, sien):
        egal = mien == sien
        out["controles"][nom] = {"agent": mien, "aide": sien, "egal": egal}
        if not egal:
            out["desaccords"].append(nom)

    E, AE = app["estimateur"], aide["estimateur"]
    comparer("tient_par_n", {str(k): v for k, v in E["tient_aux_cellules_de_la_regle_par_n"].items()},
             AE["tient_aux_cellules_de_la_regle_par_n"])
    comparer("taille_retenue", E["taille_retenue"], AE["taille_retenue_par_la_regle"])
    comparer("verdict_estimateur_mot", E["verdict_estimateur"],
             AE["verdict_mecanique_estimateur"].split(" : ")[0])
    comparer("theorie_p2", "valide", AE["theorie_p2"])

    # plus petit n par cellule
    aide_cel = AE["plus_petit_n_qui_tient_par_cellule"]
    exemples = list(aide_cel.keys())[:3]
    mien = {}
    for k, v in E["plus_petit_n_qui_tient"].items():
        J, loi, prof, rho = k.split("|")
        mien[f"{J[1:]}|{loi[3:]}|{prof}|{rho[3:]}"] = v
    communs = set(mien) & set(aide_cel)
    diff = sorted(k for k in communs if mien[k] != aide_cel[k])
    out["controles"]["plus_petit_n_par_cellule"] = {
        "exemples_de_cles_de_l_aide": exemples, "cellules_agent": len(mien),
        "cellules_aide": len(aide_cel), "communes": len(communs),
        "seulement_agent": sorted(set(mien) - set(aide_cel))[:20],
        "seulement_aide": sorted(set(aide_cel) - set(mien))[:20],
        "differentes": [{"cellule": k, "agent": mien[k], "aide": aide_cel[k]} for k in diff]}
    if diff:
        out["desaccords"].append("plus_petit_n_par_cellule")

    # par groupe (J, loi, profil) : plus petit n qui tient pour tous les rho du groupe
    groupes = {}
    for k, v in mien.items():
        J, loi, prof, rho = k.split("|")
        groupes.setdefault(f"{J}|{loi}|{prof}", []).append(v)
    mien_g = {g: (None if any(x is None for x in vs) else max(vs)) for g, vs in groupes.items()}
    comparer("plus_petit_n_par_groupe", mien_g, AE["plus_petit_n_qui_tient_par_J_loi_profil"])

    # puissance
    P, AP = app["puissance"], aide["puissance"]
    comparer("puissance_qui_decide", P["puissance_qui_decide"], AP["puissance_qui_decide"])
    mins = {}
    for comp, v in P["par_ecart"]["0.1"]["par_comparaison"].items():
        for l in v["puissances"]:
            mins[l["bras"]] = min(mins.get(l["bras"], 1.0), l["puissance"])
    comparer("minima_par_comparaison", mins, AP["minima_par_comparaison"])
    comparer("comparaisons_sans_cellule_faisable", P["par_ecart"]["0.1"]["comparaisons_sans_cellule_faisable"],
             AP["comparaisons_sans_cellule_faisable"])
    comparer("portee_s_applique", P["regle_de_portee_s_applique"],
             AP["comparaisons_d_agregations"].startswith("descriptives"))

    # branche 2
    B2, AB2 = app["fefca0bd94064_branche_2"], aide["branche_2_fefca0bd94064"]
    refutes_mien = {f"{r['loi']}|{r['profil']}|{r['rho']}|{r['taille_etalonnage']}" for r in B2["cellules_refutees"]}
    refutes_aide = {k for k, v in AB2["par_cellule"].items() if v["mot"].startswith("réfuté")}
    comparer("branche_2_cellules_refutees", sorted(refutes_mien), sorted(refutes_aide))
    comparer("branche_2_tient_par_taille", B2["tient_dans_toutes_les_cellules_par_taille"],
             AB2["tient_dans_toutes_les_cellules_par_taille_d_etalonnage"])
    comparer("branche_2_plus_petite_taille", B2["plus_petite_taille_d_etalonnage"],
             AB2["plus_petite_taille_d_etalonnage_a_partir_de_laquelle_la_branche_tient_partout"] or "aucune")

    # branche 3, sens (a)
    B3, AB3 = app["fefca0bd94064_branche_3"], aide["branche_3_fefca0bd94064"]
    mien3 = {k: v["mot"] for k, v in B3.items()}
    sien3 = {}
    for k, v in AB3.items():
        if k.startswith("suiveur_seduisant|"):
            _, t, c = k.split("|")
            sien3[f"t{t[2:]}|c{c[2:]}"] = v["mot"]
    comparer("branche_3_sens_a", mien3, sien3)

    # alarme
    A, AA = app["alarme"], aide["alarme_fcbf4a2dd1a57"]
    comparer("P6", A["P6"], AA["prediction_P6"]["mot"])
    comparer("carte_alarme", A["carte_fcbf4a2dd1a57"], AA["carte_fcbf4a2dd1a57"])
    mienA = {m: (v["clause_fausse_alarme_atteinte"], v["clause_detection_atteinte"]) for m, v in A["par_m"].items()}
    sienA = {m: (v["clause_fausse_alarme"]["atteinte"], v["clause_detection"]["atteinte"])
             for m, v in AA["prediction_P6"]["par_m"].items()}
    comparer("P6_clauses_par_m", {k: list(v) for k, v in mienA.items()}, {k: list(v) for k, v in sienA.items()})

    out["blocs_de_l_aide_non_compares"] = sorted(set(aide) - {"estimateur", "puissance", "branche_2_fefca0bd94064",
                                                               "branche_3_fefca0bd94064", "alarme_fcbf4a2dd1a57",
                                                               "branche_1_fefca0bd94064"})
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":
    main()
