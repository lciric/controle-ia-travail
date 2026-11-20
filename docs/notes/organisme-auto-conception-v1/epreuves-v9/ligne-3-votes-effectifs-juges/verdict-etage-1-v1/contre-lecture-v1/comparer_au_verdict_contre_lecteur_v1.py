"""Compare, champ par champ, mon rejeu aux sorties de l'agent du verdict.

Contre-lecteur, modele F. Joue APRES mon rejeu ; ne lit que des fichiers JSON.
Usage : python3 comparer_au_verdict_contre_lecteur_v1.py MON_REJEU.json MES_CONTROLES.json
            APPLICATION_VERDICT.json CONTROLES_VERDICT.json SORTIE.json
"""
import hashlib
import json
import os
import sys


def sha256(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def proche(a, b):
    if a is None or b is None:
        return a is None and b is None
    if isinstance(a, bool) or isinstance(b, bool) or isinstance(a, str) or isinstance(b, str):
        return a == b
    return abs(a - b) <= 1e-12


def court(m):
    m = str(m).lower()
    if "non lu" in m:
        return "non lue"
    if "sans prise" in m:
        return "sans prise"
    if "réfut" in m or "refut" in m:
        return "refute"
    if "tient" in m:
        return "tient"
    return m


def main():
    moi_p, ctl_p, v_p, vctl_p, sortie = sys.argv[1:6]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe deja")
    moi, ctl, v, vctl = (json.load(open(p, encoding="utf-8")) for p in (moi_p, ctl_p, v_p, vctl_p))
    champs = []

    def champ(nom, a, b, egal=None):
        champs.append({"champ": nom, "contre_lecteur": a, "verdict": b,
                       "egal": proche(a, b) if egal is None else egal})

    # controles
    champ("melange plante conforme", ctl["K0a_melange_plante"]["tient"],
          vctl["C0_a_melange_plante"]["conforme"])
    champ("P2 cellules lues", ctl["K0b_P2"]["cellules_lues"], vctl["C0_b_P2"]["cellules_lues"])
    champ("P2 ecart maximal", ctl["K0b_P2"]["pire_cellule"]["ecart_maximal"],
          vctl["C0_b_P2"]["ecart_maximal_observe"])
    pc, vc = ctl["K0b_P2"]["pire_cellule"], vctl["C0_b_P2"]["cellule_de_l_ecart_maximal"]
    champ("P2 cellule de l'ecart maximal", [pc["loi"], pc["profil"], pc["rho"], pc["n"]],
          [vc["loi"], vc["profil"], vc["rho"], vc["n"]],
          egal=[pc["loi"], pc["profil"], pc["rho"], pc["n"]] == [vc["loi"], vc["profil"], vc["rho"], vc["n"]])
    champ("P2 tenue", ctl["K0b_P2"]["tient"], vctl["C0_b_P2"]["P2_tenue"])
    champ("clause (ii) : cellules en faute", len(ctl["K0c_abstentions_delta_0"]["cellules_hors_0.02"]),
          len(v["fcfa3d98b90f8"]["clause_ii_faute_du_banc"]))

    # estimateur
    ve, me = v["estimateur"], moi["regle_du_nombre_de_temoins"]
    for n in ("50", "100", "200", "400"):
        champ(f"treize cellules tiennent a n={n}", me["tient_aux_treize_par_n"][n],
              ve["tient_aux_cellules_de_la_regle_par_n"][n])
    champ("nombre de cellules de la regle", me["cellules_de_la_regle"]["loi_1"]
          + me["cellules_de_la_regle"]["loi_3"], ve["nombre_cellules_de_la_regle"])
    champ("mot de la table", "non, pas à cette taille" in me["mot_de_la_table_gelee"],
          ve["verdict_estimateur"] == "non, pas à cette taille")
    champs[-1]["contre_lecteur"], champs[-1]["verdict"] = me["mot_de_la_table_gelee"], ve["verdict_estimateur"]
    champ("taille voulue", me["taille_voulue_plus_petit_n_au_dessus_de_100_ou_les_treize_tiennent"],
          ve["taille_retenue"])
    champ("issue non monotone sur la regle", bool(me["issue_non_monotone_sur_la_regle"]),
          ve["issue_non_monotone_au_niveau_de_la_regle"])
    champ("cellules non monotones (grille entiere)",
          moi["table_plus_petit_n"]["nombre_de_couples_non_monotones"],
          ve["cellules_non_monotones_nombre"])
    # cellules manquantes a n = 100 : eqm et manques
    des = 0
    for x in me["par_n"]["100"]["cellules_qui_manquent"]:
        k = f'J2|loi{x["loi"]}|egal_0.2|rho{x["rho"]}'
        w = ve["detail_cellules_de_la_regle"][k]["100"]
        if w["tient"] or not proche(w["eqm"], x["eqm"]) or sorted(w["manques"]) != sorted(
                kk.replace("_basse", "").replace("_haute", "") for kk in x["manques"]):
            des += 1
    champ("cellules manquantes a n=100 : desaccords (eqm, tolerance manquante)", des, 0)
    champ("nombre de cellules manquantes a n=100", len(me["par_n"]["100"]["cellules_qui_manquent"]),
          sum(1 for k in ve["cellules_de_la_regle"]
              if not ve["detail_cellules_de_la_regle"][k]["100"]["tient"]))
    # plus petit n par cellule
    mien = {}
    for g, val in moi["table_plus_petit_n"]["par_J_loi_profil"].items():
        J, loi, profil = g.split("|")
        for rho, pp in val["plus_petit_n_par_rho"].items():
            mien[f"J{J}|loi{loi}|{profil}|rho{rho}"] = pp
    sien = ve["plus_petit_n_qui_tient"]
    diff = [k for k in sorted(set(mien) | set(sien)) if mien.get(k, "absent") != sien.get(k, "absent")]
    champ("plus petit n : cellules comparees", len(mien), len(sien))
    champ("plus petit n : cellules en desaccord", len(diff), 0)
    champ("drapeau tient de l'aide : desaccords",
          len(moi["tolerance"]["desaccords_avec_le_drapeau_tient_de_l_aide"]),
          ve["accord_du_drapeau_tient_du_code_par_cellule_et_n"].get("desaccord", 0))

    # puissance
    vp, mp = v["puissance"], moi["regle_de_portee"]
    champ("puissance qui decide", mp["puissance_qui_decide_ecart_0.10"], vp["puissance_qui_decide"])
    champ("regle de portee s'applique", mp["comparaisons_d_agregations_descriptives"],
          vp["regle_de_portee_s_applique"])
    champ("comptes faisables egaux au texte",
          all(x["attendu"] == x["vu"] for x in mp["comptes_de_cellules_faisables_contre_PR_l238"].values()),
          vp["comptes_egaux_au_texte"])
    for ev in ("0.05", "0.1", "0.15"):
        champ(f"plus basse puissance, ecart {ev}", mp["par_ecart"][ev]["plus_basse"],
              vp["par_ecart"][ev]["plus_basse_toutes_comparaisons"])
        miennes = sorted((x["comparaison"], x["loi"], x["rho"], x["rho_prime"], x["puissance"])
                         for x in mp["par_ecart"][ev]["puissances"])
        siennes = sorted((l["bras"], l["loi"], l["rho"], l["rho_prime"], l["puissance"])
                         for c in vp["par_ecart"][ev]["par_comparaison"].values()
                         for l in c["puissances"])
        champ(f"puissances par cellule, ecart {ev} (nombre ; egalite de toutes)",
              len(miennes), len(siennes), egal=miennes == siennes)
    nom = {"U": "unanimite", "S_1": "juge_seul", "S_2": "juge_seul",
           "R_3": "juge_repete_trois_votes_majorite"}
    for kp in ("U", "S_1", "S_2", "R_3"):
        m_ = mp["par_ecart"]["0.1"]["min_par_comparaison"][kp]["min"]
        s_ = min(l["puissance"] for l in vp["par_ecart"]["0.1"]["par_comparaison"][nom[kp]]["puissances"]
                 if l["bras"] == kp)
        champ(f"plus basse puissance de la comparaison {kp}, ecart 0.1", m_, s_)

    # regle A
    va, ma = v["regle_A_ecart_rho_prime_moins_rho"], moi["puissance_positif_rho_prime_moins_rho"]
    for ev in ("0.2", "0.3", "0.5"):
        champ(f"rho'-rho ecart {ev} faisables", ma["par_ecart"][ev]["faisables"], va[ev]["faisables"])
        champ(f"rho'-rho ecart {ev} plus basse", ma["par_ecart"][ev]["plus_basse"],
              va[ev]["plus_basse_les_deux"])
        champ(f"rho'-rho ecart {ev} plus haute", ma["par_ecart"][ev]["plus_haute"],
              va[ev]["plus_haute_les_deux"])

    # fa38
    vf = {}
    for k, n in v["fa38f9faa24e0"]["mots_par_J"].items():
        J, m = k.split("|")
        vf[(J.replace("J", "J="), court(m))] = n
    for J, g in moi["fa38f9faa24e0"]["mots_par_J"].items():
        for m, n in g.items():
            champ(f"fa38 {J} {m}", n, vf.get((J, m), 0))

    # branche 2
    vb, mb = v["fefca0bd94064_branche_2"], moi["fefca_branche_2"]
    for t in ("25", "50", "100", "200"):
        champ(f"branche (2) refutees a {t}", mb["par_taille_d_etalonnage"][t]["refute"],
              vb["par_taille"][t].get("réfuté sur le banc", 0))
    champ("branche (2) plus petite taille",
          mb["plus_petite_taille_a_partir_de_laquelle_la_branche_tient_partout"],
          None if vb["plus_petite_taille_d_etalonnage"] == "aucune" else vb["plus_petite_taille_d_etalonnage"])

    # branche 3 (sens a)
    for t in (20, 40):
        for c in ("0.1", "0.15", "0.2", "0.25", "0.3"):
            champ(f"branche (3) t={t} c={c}",
                  moi["fefca_branche_3"]["par_loi_t_c"][f"suiveur_seduisant|t={t}|c={c}"]["mot"],
                  court(v["fefca0bd94064_branche_3"][f"t{t}|c{c}"]["mot"]))

    # fcfa
    des, nb = 0, 0
    for x in moi["fcfa3d98b90f8"]["toutes_les_lois"]:
        if x["loi"] != "suiveur_seduisant":
            continue
        w = v["fcfa3d98b90f8"]["cellules"][f'delta{x["delta"]}|s{x["s"]}|n{x["n"]}']
        nb += 1
        if (court(w["clause_i"]), court(w["clause_iii"]), court(w["mot"])) != (
                x["clause_i"], x["clause_iii"], x["mot"]):
            des += 1
    champ("fcfa cellules comparees (sens a)", nb, len(v["fcfa3d98b90f8"]["cellules"]))
    champ("fcfa cellules en desaccord (clauses (i), (iii), mot)", des, 0)

    # alarme
    for m in ("10", "20", "40"):
        a, b = moi["alarme_P6"]["par_m"][m], v["alarme"]["par_m"][m]
        champ(f"alarme m={m} fausse alarme B", a["fausse_alarme_bras_B_suites"], b["fausse_alarme_B_sur_1000"])
        champ(f"alarme m={m} clause fausse alarme", a["clause_fausse_alarme_atteinte"],
              b["clause_fausse_alarme_atteinte"])
        champ(f"alarme m={m} detection B", a["detection_a_effet_bras_B"], b["detection_a_effet_B_sur_500"])
        champ(f"alarme m={m} detection D", a["detection_a_effet_bras_D"], b["detection_a_effet_D_sur_500"])
        champ(f"alarme m={m} clause detection", a["clause_detection_atteinte"],
              b["clause_detection_atteinte"])
    champ("mot de P6", moi["alarme_P6"]["mot_P6"], v["alarme"]["P6"])
    champ("mot de la carte de l'alarme", moi["alarme_P6"]["carte"], v["alarme"]["carte_fcbf4a2dd1a57"])

    # trop propre
    champ("audit trop propre : cellules", moi["audit_R4_trop_propre"]["nombre"],
          len(v["audit_trop_propre_etage_1"]["couverture_egale_1"]))

    r = {"programme": os.path.basename(__file__),
         "entrees_sha256": {os.path.basename(p): sha256(p) for p in (moi_p, ctl_p, v_p, vctl_p)},
         "champs_compares": len(champs),
         "champs_en_desaccord": [c for c in champs if not c["egal"]],
         "nombre_de_desaccords": sum(1 for c in champs if not c["egal"]),
         "champs": champs}
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("champs compares :", len(champs), "; desaccords :", r["nombre_de_desaccords"])
    for c in r["champs_en_desaccord"]:
        print("DESACCORD", c)


if __name__ == "__main__":
    main()
