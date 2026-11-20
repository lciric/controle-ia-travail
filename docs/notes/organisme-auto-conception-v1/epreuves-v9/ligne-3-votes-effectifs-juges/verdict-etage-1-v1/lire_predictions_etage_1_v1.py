"""Lecture descriptive des prédictions de l'étage 1 contre leurs clauses de
réfutation (PR l. 318 ; prédictions PR l. 133 à 141, P10 l. 147).
N'ouvre pas `criteres_mecaniques`. Ne relit aucun mot du code. Aucun tirage.
Convention de lecture (déclarée au verdict v2) : valeurs observées (moyennes
sur les 2 000 répliques), sans intervalle, cellule par cellule ; une
prédiction est dite « réfutée » si l'une de ses clauses est atteinte dans
l'une des cellules où elle se lit (même convention que A1 l. 110 pour P6).

Usage : python3 -I -B lire_predictions_etage_1_v1.py RESULTAT.json APPLICATION.json SORTIE.json
"""
import json
import sys


def main():
    src, app_p, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    data.pop("criteres_mecaniques", None)
    with open(app_p, encoding="utf-8") as f:
        app = json.load(f)
    ea = data["estimateur_et_agregation"]
    out = {}

    # ---- P1 (PR l. 133), deux juges, lois qui décident (1 et 3)
    def tient(e):
        s = e["estimateur"]
        return (s["biais"] is not None and abs(s["biais"]) <= 0.05 and s["eqm"] is not None
                and s["eqm"] <= 0.10 and s["couverture"] is not None
                and 0.90 <= s["couverture"] <= 0.98 and s["part_indefini"] <= 0.02)
    c50 = [e for e in ea if e["J"] == 2 and e["loi"] in (1, 3) and e["profil"] == "egal_0.1" and e["n"] == 50]
    c400 = [e for e in ea if e["J"] == 2 and e["loi"] in (1, 3) and e["profil"] == "egal_0.2" and e["n"] == 400]
    c100 = [e for e in ea if e["J"] == 2 and e["loi"] in (1, 3) and e["profil"] == "egal_0.2" and e["n"] == 100]
    cl1 = sum(tient(e) for e in c50)
    cl2 = sum(not tient(e) for e in c400)
    out["P1"] = {
        "clause_tenue_a_n50_taux_0_10": {"cellules": len(c50), "qui_tiennent": cl1, "atteinte": cl1 > 0},
        "clause_manquee_a_n400_taux_0_20": {"cellules": len(c400), "qui_manquent": cl2, "atteinte": cl2 > 0},
        "mot": "réfutée" if (cl1 > 0 or cl2 > 0) else "non réfutée",
        "information_n100_taux_0_20_cellules_qui_tiennent": f"{sum(tient(e) for e in c100)} sur {len(c100)}",
    }

    # ---- P4 (PR l. 136) : bras N contre la majorité fixe, cinq juges, rho >= 0,6
    gains = []
    for e in ea:
        if e["J"] == 5 and e["rho_grille"] >= 0.6 - 1e-12:
            g = e["bras"]["F_majorite_stricte"]["erreur_equilibree"] - e["bras"]["N"]["erreur_equilibree"]
            gains.append((g, e["loi"], e["profil"], e["rho_grille"], e["n"]))
    gmax = max(gains)
    out["P4"] = {"cellules": len(gains),
                 "plus_grand_gain_N_sur_majorite_stricte": gmax[0],
                 "cellule": {"loi": gmax[1], "profil": gmax[2], "rho": gmax[3], "n": gmax[4]},
                 "clause_gain_0_02_ou_plus_atteinte": gmax[0] >= 0.02,
                 "mot": "réfutée" if gmax[0] >= 0.02 else "non réfutée"}

    # ---- P5, P5 ter, P5 quater (PR l. 137, 139, 140) : double rendu, s = 1 (et s = 0,5 pour P5 ter)
    dr = data["double_rendu"]

    def cel(delta, s):
        return [e for e in dr if abs(e["delta"] - delta) < 1e-9 and abs(e["s"] - s) < 1e-9]

    p5 = []
    for e in cel(0.5, 1.0):
        d = e["par_loi"]["suiveur_seduisant"]["fa_trait_bras_1_moins_bras_2"]
        p5.append({"n": e["n"], "fa1_moins_fa2": d["moyenne"], "intervalle": [d["bas"], d["haut"]],
                   "aucune_baisse": d["moyenne"] >= 0})
    out["P5"] = {"lue_sur": "suiveur séduisant (PR l. 137, lecture en version 4)",
                 "clause_aucune_baisse_a_delta_0_5_s_1": p5,
                 "mot": "réfutée" if any(x["aucune_baisse"] for x in p5) else "non réfutée"}

    p5t = []
    for e in cel(0.5, 1.0):
        d = e["par_loi"]["suiveur_repoussant"]["fa_trait_bras_1_moins_bras_2"]
        p5t.append({"n": e["n"], "fa1_moins_fa2": d["moyenne"], "fa1_non_superieur": d["moyenne"] <= 0})
    p5t_iii = []
    for e in cel(0.5, 0.5):
        i1 = e["par_loi"]["suiveur_repoussant"]["ecart_surface_bras_1"]
        dans = i1["bas"] >= -0.05 and i1["haut"] <= 0.05
        p5t_iii.append({"n": e["n"], "ecart_surface_bras_1": i1["moyenne"], "intervalle": [i1["bas"], i1["haut"]],
                        "intervalle_dans_0_05": dans})
    out["P5_ter"] = {"lue_sur": "suiveur repoussant (rapporté sans mot de carte)",
                     "clause_fa1_non_superieur_a_fa2_delta_0_5_s_1": p5t,
                     "clause_intervalle_ecart_bras_1_dans_0_05_delta_0_5_s_0_5": p5t_iii,
                     "mot": "réfutée" if (any(x["fa1_non_superieur"] for x in p5t) or any(x["intervalle_dans_0_05"] for x in p5t_iii)) else "non réfutée"}

    p5q = []
    for delta, sens in ((0.5, "non_inferieur"), (0.2, "non_superieur")):
        for e in cel(delta, 1.0):
            d = e["par_loi"]["suiveur_seduisant"]["fa_trait_bras_1_moins_bras_2"]["moyenne"]
            att = d >= 0 if sens == "non_inferieur" else d <= 0
            p5q.append({"delta": delta, "n": e["n"], "fa1_moins_fa2": d, "clause": sens, "atteinte": att})
    out["P5_quater"] = {"lue_sur": "suiveur séduisant, s = 1", "clauses": p5q,
                        "mot": "réfutée" if any(x["atteinte"] for x in p5q) else "non réfutée"}

    # ---- P5 bis (PR l. 138) : garde de cadrage, rondes saines
    gc = data["garde_de_cadrage"]
    saines = {g["t"]: g["par_loi"]["suiveur_seduisant"]["part_des_rondes_declenchees"]
              for g in gc if g["delta"] == 0.0}
    c1 = {t: saines[t]["0.1"] for t in saines}
    c2 = saines[40]["0.3"]
    att1 = any(v < 0.10 for v in c1.values())
    att2 = c2 > 0.10
    out["P5_bis"] = {"part_saine_au_seuil_0_10_par_t": c1, "clause_moins_de_10_pct_au_seuil_0_10": att1,
                     "part_saine_au_seuil_0_30_t40": c2, "clause_plus_de_10_pct_au_seuil_0_30_t40": att2,
                     "mot": "réfutée" if (att1 or att2) else "non réfutée"}

    # ---- P6 (A1 l. 107 à 110) : reprise de l'application v1
    out["P6"] = app["alarme"]

    # ---- P10 (PR l. 147) : puissance qui décide de 0,5 ou plus
    pqd = app["puissance"]["puissance_qui_decide"]
    out["P10"] = {"puissance_qui_decide": pqd, "clause_0_5_ou_plus_atteinte": pqd >= 0.5,
                  "mot": "réfutée" if pqd >= 0.5 else "non réfutée"}

    # ---- vérification des corrections 1 et 2 : valeur exacte et distance aux bornes
    cible = [e for e in ea if e["J"] == 2 and e["loi"] == 3 and e["profil"] == "egal_0.2"
             and e["rho_grille"] == 0.0 and e["n"] == 100][0]["estimateur"]
    dmin = None
    for e in ea:
        s = e["estimateur"]
        vals = []
        if s["biais"] is not None:
            vals.append(abs(abs(s["biais"]) - 0.05))
        if s["eqm"] is not None:
            vals.append(abs(s["eqm"] - 0.10))
        if s["couverture"] is not None:
            vals += [abs(s["couverture"] - 0.90), abs(s["couverture"] - 0.98)]
        vals.append(abs(s["part_indefini"] - 0.02))
        m = min(vals)
        dmin = m if dmin is None else min(dmin, m)
    out["verification_bornes"] = {"eqm_loi3_rho0_n100": repr(cible["eqm"]),
                                  "sous_la_borne": cible["eqm"] < 0.10,
                                  "plus_petite_distance_a_une_borne_780_cellules": dmin}

    # ---- P3 : non lue (raison au verdict v2)
    out["P3"] = {"mot": "non lue",
                 "raison": "la clause ne nomme ni l'agrégation étalonnée (bras C ou bras P), ni la référence "
                           "(« majorité fixe » : majorité stricte ou poids égaux), ni les profils "
                           "« échangeables » ; le mot dépendrait d'un choix fait après lecture (règle R3)"}

    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":
    main()
