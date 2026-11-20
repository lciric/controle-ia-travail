"""Lecture des predictions P1, P3, P4, P5, P5 bis, P5 ter, P5 quater, P6, P10 contre
leur clause de refutation (PR l. 133 a 147), sur les mesures de l'etage 1.

Programme du contre-lecteur (modele F), ecrit AVANT de lire le verdict v2, son
differentiel, le programme `lire_predictions_etage_1_v1.py` et sa sortie.
Lecture par cellule, sur les moyennes (PR l. 184 : « Etage 1 : pas de test ;
lecture par cellule ») ; les intervalles sont rapportes a cote.
Bibliotheque standard seule, aucun tirage.

Usage : python3 rejouer_predictions_contre_lecteur_v1.py MESURES.json SORTIE.json
"""
import hashlib
import json
import os
import sys

EPS = 1e-12
NS = [50, 100, 200, 400]


def sha256(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def tient(e):
    return (abs(e["biais"]) <= 0.05 and e["eqm"] <= 0.10 and 0.90 <= e["couverture"] <= 0.98
            and e["part_indefini"] <= 0.02)


def main():
    mesures, sortie = sys.argv[1], sys.argv[2]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe deja")
    with open(mesures, encoding="utf-8") as f:
        d = json.load(f)
    ea = d["estimateur_et_agregation"]
    R = {"programme": os.path.basename(__file__), "mesures_sha256": sha256(mesures)}

    # ---------------- P1 (PR l. 133)
    p1 = {}
    for J in (2, 5):
        for loi in sorted({c["loi"] for c in ea if c["J"] == J}):
            a = [tient(c["estimateur"]) for c in ea
                 if c["J"] == J and c["loi"] == loi and c["profil"] == "egal_0.1" and c["n"] == 50]
            b = [tient(c["estimateur"]) for c in ea
                 if c["J"] == J and c["loi"] == loi and c["profil"] == "egal_0.2" and c["n"] == 400]
            p1[f"J={J}|loi {loi}"] = {"taux_0.10_n_50_tiennent": [sum(a), len(a)],
                                      "taux_0.20_n_400_tiennent": [sum(b), len(b)]}
    dec = [p1[k] for k in ("J=2|loi 1", "J=2|loi 3")]
    c1 = any(x["taux_0.10_n_50_tiennent"][0] > 0 for x in dec)
    c2 = any(x["taux_0.20_n_400_tiennent"][0] < x["taux_0.20_n_400_tiennent"][1] for x in dec)
    R["P1"] = {"par_J_et_loi": p1,
               "clause_tenue_a_50_pour_0.10_atteinte_dans_une_cellule_J2_lois_1_3": c1,
               "clause_manquee_a_400_pour_0.20_atteinte_dans_une_cellule_J2_lois_1_3": c2,
               "atteinte_ailleurs_J2_loi_2_ou_J5": {
                   "tenue_a_50": any(v["taux_0.10_n_50_tiennent"][0] > 0 for v in p1.values()),
                   "manquee_a_400": any(v["taux_0.20_n_400_tiennent"][0] < v["taux_0.20_n_400_tiennent"][1]
                                        for v in p1.values())},
               "mot": "réfutée" if (c1 or c2) else "non réfutée"}

    # ---------------- P3 (PR l. 135) : donnees pour chaque lecture possible
    def gains(c):
        cmp_ = c["comparaisons"]
        br = c["bras"]
        maj = br["F_majorite_stricte"]["erreur_equilibree"]
        return {"C_contre_majorite_stricte": cmp_["F_majorite_stricte_moins_C"]["moyenne"],
                "P_contre_majorite_stricte": maj - br["P"]["erreur_equilibree"],
                "C_contre_poids_egaux": cmp_["poids_egaux_moins_C"]["moyenne"],
                "P_contre_poids_egaux": cmp_["poids_egaux_moins_P"]["moyenne"]}

    noms = ["C_contre_majorite_stricte", "P_contre_majorite_stricte", "C_contre_poids_egaux",
            "P_contre_poids_egaux"]
    p3 = {}
    ech = [c for c in ea if c["J"] == 5 and c["loi"] == 1 and c["profil"] != "inegal"]
    ech_eg = [c for c in ech if c["profil"].startswith("egal_")]
    blocs200 = [c for c in ea if c["J"] == 5 and c["loi"] == 4 and c["n"] == 400]
    blocs200_06 = [c for c in blocs200 if c["rho_grille"] >= 0.6 - EPS]
    blocs100_06 = [c for c in ea if c["J"] == 5 and c["loi"] == 4 and c["n"] >= 200
                   and c["rho_grille"] >= 0.6 - EPS]
    for nom in noms:
        def stat(cs):
            g = [gains(c)[nom] for c in cs]
            return {"cellules": len(g), "min": min(g), "max": max(g),
                    "cellules_a_gain_de_0.02_ou_plus": sum(1 for x in g if x >= 0.02 - EPS),
                    "cellules_a_gain_positif": sum(1 for x in g if x > EPS)}
        e1, e2 = stat(ech), stat(ech_eg)
        b1, b2, b3 = stat(blocs200), stat(blocs200_06), stat(blocs100_06)
        p3[nom] = {
            "echangeables_loi_1_taux_egaux_entre_juges": e1,
            "echangeables_loi_1_profils_egal_seulement": e2,
            "blocs_loi_4_a_200_temoins_d_etalonnage_tous_rho": b1,
            "blocs_loi_4_a_200_temoins_d_etalonnage_rho_0.6_ou_plus": b2,
            "blocs_loi_4_a_100_temoins_d_etalonnage_ou_plus_rho_0.6_ou_plus": b3,
            "clause_1_gain_de_0.02_ou_plus_echangeables_dans_une_cellule":
                e1["cellules_a_gain_de_0.02_ou_plus"] > 0,
            "clause_2_aucun_gain_en_blocs_a_200__dans_toutes_les_cellules_rho_0.6":
                b2["cellules_a_gain_positif"] == 0,
            "clause_2_aucun_gain_en_blocs_a_200__dans_une_cellule_au_moins_rho_0.6":
                b2["cellules_a_gain_positif"] < b2["cellules"],
            "clause_2_aucun_gain_en_blocs_a_200__dans_une_cellule_au_moins_tous_rho":
                b1["cellules_a_gain_positif"] < b1["cellules"]}
    R["P3"] = {"par_lecture": p3,
               "note": "la clause ne nomme ni le bras « agrégation étalonnée » (C ou P) ni la "
                       "référence (majorité stricte ou poids égaux) ; les quatre lectures sont "
                       "rendues, aucune n'est choisie"}

    # ---------------- P4 (PR l. 136)
    cs = [c for c in ea if c["J"] == 5 and c["rho_grille"] >= 0.6 - EPS]
    g = [(c["comparaisons"]["F_majorite_stricte_moins_N"]["moyenne"], c) for c in cs]
    gm, cm = max(g, key=lambda x: x[0])
    R["P4"] = {"reference": "majorité stricte (seule majorité fixe jouée à cinq juges, PR l. 216)",
               "cellules_rho_0.6_ou_plus": len(g),
               "plus_grand_gain_de_N": {"gain": gm, "loi": cm["loi"], "profil": cm["profil"],
                                        "rho": cm["rho_grille"], "n": cm["n"],
                                        "intervalle": cm["comparaisons"]["F_majorite_stricte_moins_N"]},
               "cellules_a_gain_de_0.02_ou_plus": sum(1 for x, _ in g if x >= 0.02 - EPS),
               "repliques_ecartees_max_bras_N": max(c.get("bras_N_votes_effectifs_indefinis", 0)
                                                    for c in cs),
               "mot": "réfutée" if any(x >= 0.02 - EPS for x, _ in g) else "non réfutée"}

    # ---------------- double rendu : P5, P5 ter, P5 quater
    def cel(loi, delta, s):
        out = {}
        for c in d["double_rendu"]:
            if abs(c["delta"] - delta) < 1e-9 and abs(c["s"] - s) < 1e-9:
                v = c["par_loi"][loi]
                mo = v["moyennes"]
                out[str(c["n"])] = {"fa_trait_bras_1": mo["fa_trait_bras_1"],
                                    "fa_trait_bras_2": mo["fa_trait_bras_2"],
                                    "fa_trait_bras_4": mo["fa_trait_bras_4"],
                                    "intervalle_bras_1_moins_bras_2": v.get("fa_trait_bras_1_moins_bras_2"),
                                    "ecart_surface_bras_1": v.get("ecart_surface_bras_1"),
                                    "abstention_par_vote": mo["abstention_par_vote"]}
        return out

    # P5 (PR l. 137), lue sur le suiveur seduisant : « aucune baisse a delta = 0,5 et confondant plein »
    a = cel("suiveur_seduisant", 0.5, 1.0)
    p5_cells = {n: {"bras_1": x["fa_trait_bras_1"], "bras_2": x["fa_trait_bras_2"],
                    "bras_4": x["fa_trait_bras_4"],
                    "baisse_contre_bras_2": x["fa_trait_bras_1"] < x["fa_trait_bras_2"] - EPS,
                    "baisse_contre_bras_4": x["fa_trait_bras_1"] < x["fa_trait_bras_4"] - EPS,
                    "intervalle_bras_1_moins_bras_2": x["intervalle_bras_1_moins_bras_2"]}
                for n, x in a.items()}
    R["P5"] = {"cellules_delta_0.5_s_1": p5_cells,
               "clause_aucune_baisse_contre_bras_2_dans_une_cellule":
                   any(not x["baisse_contre_bras_2"] for x in p5_cells.values()),
               "clause_aucune_baisse_contre_bras_4_dans_une_cellule":
                   any(not x["baisse_contre_bras_4"] for x in p5_cells.values()),
               "mot_reference_bras_2": "réfutée" if any(not x["baisse_contre_bras_2"]
                                                        for x in p5_cells.values()) else "non réfutée",
               "note": "référence de la baisse : le bras 2, à coût égal (clause (i), PR l. 325) ; "
                       "le bras 4 est rendu à côté"}

    # P5 ter (PR l. 139), suiveur repoussant
    b = cel("suiveur_repoussant", 0.5, 1.0)
    c05 = cel("suiveur_repoussant", 0.5, 0.5)
    t1 = {n: {"bras_1": x["fa_trait_bras_1"], "bras_2": x["fa_trait_bras_2"],
              "bras_1_non_superieur": not (x["fa_trait_bras_1"] > x["fa_trait_bras_2"] + EPS)}
          for n, x in b.items()}
    t2 = {n: {"intervalle_ecart_bras_1": x["ecart_surface_bras_1"],
              "tout_entier_dans_0.05": (x["ecart_surface_bras_1"]["bas"] >= -0.05 - EPS
                                        and x["ecart_surface_bras_1"]["haut"] <= 0.05 + EPS)}
          for n, x in c05.items()}
    R["P5_ter"] = {"clause_1_delta_0.5_s_1": t1, "clause_2_delta_0.5_s_0.5": t2,
                   "clause_1_atteinte_dans_une_cellule": any(x["bras_1_non_superieur"] for x in t1.values()),
                   "clause_2_atteinte_dans_une_cellule": any(x["tout_entier_dans_0.05"] for x in t2.values()),
                   "mot": "réfutée" if (any(x["bras_1_non_superieur"] for x in t1.values())
                                        or any(x["tout_entier_dans_0.05"] for x in t2.values()))
                   else "non réfutée"}

    # P5 quater (PR l. 140), suiveur seduisant, s = 1
    q05, q02 = cel("suiveur_seduisant", 0.5, 1.0), cel("suiveur_seduisant", 0.2, 1.0)
    u1 = {n: {"bras_1": x["fa_trait_bras_1"], "bras_2": x["fa_trait_bras_2"],
              "bras_1_non_inferieur": not (x["fa_trait_bras_1"] < x["fa_trait_bras_2"] - EPS)}
          for n, x in q05.items()}
    u2 = {n: {"bras_1": x["fa_trait_bras_1"], "bras_2": x["fa_trait_bras_2"],
              "bras_1_non_superieur": not (x["fa_trait_bras_1"] > x["fa_trait_bras_2"] + EPS)}
          for n, x in q02.items()}
    R["P5_quater"] = {"clause_1_delta_0.5_s_1": u1, "clause_2_delta_0.2_s_1": u2,
                      "clause_1_atteinte_dans_une_cellule": any(x["bras_1_non_inferieur"] for x in u1.values()),
                      "clause_2_atteinte_dans_une_cellule": any(x["bras_1_non_superieur"] for x in u2.values()),
                      "mot": "réfutée" if (any(x["bras_1_non_inferieur"] for x in u1.values())
                                           or any(x["bras_1_non_superieur"] for x in u2.values()))
                      else "non réfutée"}

    # ---------------- P5 bis (PR l. 138)
    gc = {(c["t"], round(c["delta"], 6)): c for c in d["garde_de_cadrage"]}
    s20 = gc[(20, 0.0)]["par_loi"]["suiveur_seduisant"]["part_des_rondes_declenchees"]
    s40 = gc[(40, 0.0)]["par_loi"]["suiveur_seduisant"]["part_des_rondes_declenchees"]
    k1 = s20["0.1"] < 0.10 or s40["0.1"] < 0.10
    k2 = s40["0.3"] > 0.10
    R["P5_bis"] = {"rondes_saines_t_20": s20, "rondes_saines_t_40": s40,
                   "taux_d_inversion_moyen_ronde_saine": {
                       "t_20": gc[(20, 0.0)]["par_loi"]["suiveur_seduisant"]["taux_d_inversion_moyen"],
                       "t_40": gc[(40, 0.0)]["par_loi"]["suiveur_seduisant"]["taux_d_inversion_moyen"]},
                   "clause_moins_de_10_pour_cent_au_seuil_0.10": k1,
                   "clause_plus_de_10_pour_cent_au_seuil_0.30_a_40_temoins": k2,
                   "mot": "réfutée" if (k1 or k2) else "non réfutée"}

    # ---------------- P6 (PR l. 141 ; A1 l. 105 a 112)
    p6, att = {}, []
    for c in d["alarme"]:
        B, D = c["par_bras"]["B"]["comptes_silence_1"], c["par_bras"]["D"]["comptes_silence_1"]
        fa = B["suites_sans_changement_en_alarme"] > 80
        det = (B["suites_a_effet_detectees"] <= D["suites_a_effet_detectees"]) if c["m"] in (20, 40) else None
        p6[str(c["m"])] = {"fausse_alarme_B": B["suites_sans_changement_en_alarme"], "clause_fausse_alarme": fa,
                           "detection_B": B["suites_a_effet_detectees"],
                           "detection_D": D["suites_a_effet_detectees"], "clause_detection": det}
        if fa or det:
            att.append(c["m"])
    R["P6"] = {"par_m": p6, "mot": "P6 réfutée" if att else "P6 non réfutée", "m_atteints": att}

    # ---------------- P10 (PR l. 147)
    cles = {"unanimite": ["U"], "juge_seul": ["S_1", "S_2"], "juge_repete_trois_votes_majorite": ["R_3"]}
    pu = [c["puissance_par_comparaison"][k] for c in d["monde_de_puissance"]
          if abs(c["ecart_vise"] - 0.1) < 1e-9 and c["loi"] in (1, 3) and c["faisable"]
          for k in cles[c["comparaison"]]]
    R["P10"] = {"puissance_qui_decide": min(pu), "clause_0.5_ou_plus": min(pu) >= 0.5 - EPS,
                "mot": "réfutée" if min(pu) >= 0.5 - EPS else "non réfutée"}

    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(R, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("ecrit :", sortie)


if __name__ == "__main__":
    main()
