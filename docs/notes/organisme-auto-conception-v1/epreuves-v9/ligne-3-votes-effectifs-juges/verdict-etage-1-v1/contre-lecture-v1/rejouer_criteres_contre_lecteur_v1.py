"""Rejeu des criteres geles de l'etage 1 de la ligne 3 sur les mesures.

Programme du contre-lecteur (modele F), ecrit sans avoir lu ni le verdict ni le
programme de l'agent du verdict. Bibliotheque standard seule. Aucun tirage.
N'utilise des mesures que les grandeurs mesurees ; les mots et drapeaux de l'aide
du code (criteres_mecaniques, 'tient', mots par cellule) ne servent qu'a la
comparaison, apres mon propre calcul.

Usage : python3 rejouer_criteres_contre_lecteur_v1.py MESURES.json CONTROLES.json SORTIE.json
"""
import hashlib
import json
import math
import os
import sys

EPS = 1e-12
NS = [50, 100, 200, 400]


def sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def norm(mot):
    """Ramene un mot de l'aide a une etiquette courte."""
    if mot is None:
        return None
    m = str(mot).lower()
    if "non lu" in m:
        return "non lue"
    if "sans prise" in m:
        return "sans prise"
    if "réfut" in m or "refut" in m:
        return "refute"
    if "tient" in m:
        return "tient"
    return "?" + str(mot)


# ------------------------------------------------------------------ tolerance
def tolerance(e):
    """PR l. 177. Rend (tient, manques) ; manques = {nom: depassement}."""
    manques = {}
    b, q, c, p = e["biais"], e["eqm"], e["couverture"], e["part_indefini"]
    if b is None or q is None or c is None:
        return False, {"indefini": None}
    if abs(b) > 0.05:
        manques["biais"] = abs(b) - 0.05
    if q > 0.10:
        manques["eqm"] = q - 0.10
    if c < 0.90:
        manques["couverture_basse"] = 0.90 - c
    if c > 0.98:
        manques["couverture_haute"] = c - 0.98
    if p > 0.02:
        manques["part_indefini"] = p - 0.02
    return (not manques), manques


def bruit(e, manques, R):
    """Ecart rapporte a l'erreur type de 2 000 repliques (approximations dites)."""
    out = {}
    b, q, c, p = e["biais"], e["eqm"], e["couverture"], e["part_indefini"]
    Rd = max(1.0, R * (1.0 - p))
    for nom, dep in manques.items():
        if dep is None:
            continue
        if nom == "biais":
            et = math.sqrt(max(q * q - b * b, 0.0) / Rd)
        elif nom == "eqm":
            et = q / math.sqrt(2.0 * Rd)  # approximation normale de l'erreur type d'un ecart type
        elif nom.startswith("couverture"):
            et = math.sqrt(max(c * (1.0 - c), 0.0) / Rd)
        else:
            et = math.sqrt(max(p * (1.0 - p), 0.0) / R)
        out[nom] = {"depassement": dep, "erreur_type_approchee": et,
                    "depassement_en_erreurs_types": (dep / et) if et > 0 else None}
    return out


def cle(c):
    return (c["J"], c["loi"], c["profil"], c["rho_grille"])


def main():
    mesures, controles, sortie = sys.argv[1], sys.argv[2], sys.argv[3]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe deja")
    with open(controles, encoding="utf-8") as f:
        ctl = json.load(f)
    if not ctl.get("controles_tous_tenus"):
        raise SystemExit("refus : controles avant lecture non tenus, rien n'est lu")
    if ctl.get("mesures_sha256") != sha256(mesures):
        raise SystemExit("refus : les controles portent sur un autre fichier de mesures")
    with open(mesures, encoding="utf-8") as f:
        d = json.load(f)
    R = {"programme": os.path.basename(__file__), "mesures_sha256": sha256(mesures),
         "controles_sha256": sha256(controles)}
    ea = d["estimateur_et_agregation"]

    # ============================================================ 1. tolerance
    tol = {}
    desaccord_tient, au_bord = [], []
    for c in ea:
        t, mq = tolerance(c["estimateur"])
        tol[(cle(c), c["n"])] = (t, mq, c)
        if bool(c["estimateur"]["tient"]) != t:
            desaccord_tient.append([list(cle(c)), c["n"]])
        e = c["estimateur"]
        for v, bornes in ((abs(e["biais"]), [0.05]), (e["eqm"], [0.10]),
                          (e["couverture"], [0.90, 0.98]), (e["part_indefini"], [0.02])):
            for bo in bornes:
                if abs(v - bo) < 1e-9:
                    au_bord.append([list(cle(c)), c["n"], v])
    cellules = sorted({k for (k, _n) in tol})
    R["tolerance"] = {"cellules_fois_n": len(tol), "cellules": len(cellules),
                      "tiennent": sum(1 for v in tol.values() if v[0]),
                      "desaccords_avec_le_drapeau_tient_de_l_aide": desaccord_tient,
                      "valeurs_exactement_a_une_borne": au_bord}

    # ============================================= 2. cellules de la regle (A1 l. 81)
    regle = [k for k in cellules if k[0] == 2 and k[2] == "egal_0.2" and k[1] in (1, 3)]
    compte_regle = {"loi_1": sum(1 for k in regle if k[1] == 1),
                    "loi_3": sum(1 for k in regle if k[1] == 3)}
    par_n = {}
    for n in NS:
        manquantes = []
        for k in regle:
            t, mq, c = tol[(k, n)]
            if not t:
                e = c["estimateur"]
                manquantes.append({"loi": k[1], "rho": k[3],
                                   "biais": e["biais"], "eqm": e["eqm"],
                                   "couverture": e["couverture"],
                                   "part_indefini": e["part_indefini"],
                                   "manques": bruit(e, mq, c["repliques"])})
        par_n[str(n)] = {"tient_aux_treize": not manquantes,
                         "cellules_qui_tiennent": len(regle) - len(manquantes),
                         "cellules_qui_manquent": manquantes}
    tient_n = {n: par_n[str(n)]["tient_aux_treize"] for n in NS}

    # table gelee, PR l. 311 a 316 ; regle E, A1 l. 82
    if tient_n[100]:
        mot = "« oui » de l'étage 1"
        taille = 100
        ligne = 1
    elif any(tient_n[n] for n in (200, 400)):
        mot = "« non, pas à cette taille »"
        taille = min(n for n in (200, 400) if tient_n[n])
        ligne = 2
    elif tient_n[50]:
        mot = "cas non prévu par la table gelée : la tolérance tient à n = 50 et à aucun n plus grand"
        taille = None
        ligne = None
    else:
        mot = "« non »"
        taille = None
        ligne = 3
    non_monotone_regle = [[a, b] for i, a in enumerate(NS) for b in NS[i + 1:]
                          if tient_n[a] and not tient_n[b]]
    R["regle_du_nombre_de_temoins"] = {
        "cellules_de_la_regle": compte_regle, "par_n": par_n,
        "tient_aux_treize_par_n": {str(n): tient_n[n] for n in NS},
        "mot_de_la_table_gelee": mot, "ligne_de_la_table": ligne,
        "taille_retenue_N_100": tient_n[100],
        "taille_voulue_plus_petit_n_au_dessus_de_100_ou_les_treize_tiennent": taille,
        "issue_non_monotone_sur_la_regle": non_monotone_regle,
        "audit_R4_de_non_monotonie_requis_sur_la_regle": bool(non_monotone_regle)}

    # ===================================== 3. table « plus petit n qui tient »
    plus_petit, non_mono_cell = {}, []
    for k in cellules:
        t_n = {n: tol[(k, n)][0] for n in NS if (k, n) in tol}
        pp = next((n for n in NS if t_n.get(n)), None)
        plus_petit["|".join(str(x) for x in k)] = pp
        for i, a in enumerate(NS):
            for b in NS[i + 1:]:
                if t_n.get(a) and not t_n.get(b):
                    t, mq, c = tol[(k, b)]
                    non_mono_cell.append({"J": k[0], "loi": k[1], "profil": k[2], "rho": k[3],
                                          "tient_a": a, "manque_a": b,
                                          "manques": bruit(c["estimateur"], mq, c["repliques"])})
    groupes = {}
    for k in cellules:
        g = groupes.setdefault((k[0], k[1], k[2]), [])
        g.append(k)
    par_groupe = {}
    for g, ks in sorted(groupes.items()):
        tous = next((n for n in NS if all(tol[(k, n)][0] for k in ks)), None)
        par_groupe["|".join(str(x) for x in g)] = {
            "plus_petit_n_ou_tous_les_rho_tiennent": tous,
            "plus_petit_n_par_rho": {str(k[3]): plus_petit["|".join(str(x) for x in k)]
                                     for k in ks}}
    R["table_plus_petit_n"] = {"par_J_loi_profil": par_groupe,
                               "cellules_sans_aucun_n": sum(1 for v in plus_petit.values()
                                                            if v is None),
                               "cellules_non_monotones": non_mono_cell,
                               "nombre_de_couples_non_monotones": len(non_mono_cell)}

    # ============================ 4. audit R4 « trop propre » (PR l. 348)
    trop_propre, desac = [], 0
    for c in ea:
        moi = c["estimateur"]["couverture"] is not None and c["estimateur"]["couverture"] >= 1.0 - EPS
        if moi:
            trop_propre.append([list(cle(c)), c["n"]])
        if bool(c["estimateur"]["audit_trop_propre_aucune_replique_hors_intervalle"]) != moi:
            desac += 1
    R["audit_R4_trop_propre"] = {
        "cellules_sans_aucune_replique_hors_intervalle": trop_propre,
        "nombre": len(trop_propre),
        "dont_cellules_de_la_regle": [x for x in trop_propre
                                      if x[0][0] == 2 and x[0][2] == "egal_0.2" and x[0][1] in (1, 3)],
        "desaccords_avec_le_drapeau_de_l_aide": desac,
        "note": "couverture = 1 lue comme « aucune réplique hors intervalle » (A1, choix 4)"}

    # ======================= 5. puissance qui decide (PR l. 236 a 240 ; A1 regle B)
    cles_p = {"unanimite": ["U"], "juge_seul": ["S_1", "S_2"],
              "juge_repete_trois_votes_majorite": ["R_3"]}
    puiss = {}
    for ev in (0.05, 0.1, 0.15):
        bloc = {"faisables_par_comparaison_et_loi": {}, "puissances": [], "min_par_comparaison": {}}
        for c in d["monde_de_puissance"]:
            if abs(c["ecart_vise"] - ev) > 1e-9 or c["loi"] not in (1, 3):
                continue
            kk = f'{c["comparaison"]}|loi {c["loi"]}'
            f_ = bloc["faisables_par_comparaison_et_loi"].setdefault(kk, {"faisables": 0,
                                                                         "infaisables": 0,
                                                                         "rho_faisables": []})
            if not c["faisable"]:
                f_["infaisables"] += 1
                continue
            f_["faisables"] += 1
            f_["rho_faisables"].append([c["rho"], c.get("rho_prime")])
            for kp in cles_p[c["comparaison"]]:
                p = c["puissance_par_comparaison"][kp]
                bloc["puissances"].append({"comparaison": kp, "loi": c["loi"], "rho": c["rho"],
                                           "rho_prime": c.get("rho_prime"), "d": c.get("d"),
                                           "ecart_vrai_formule": c.get("ecart_vrai_formule"),
                                           "puissance": p, "repliques": c.get("repliques")})
        for kp in ("U", "S_1", "S_2", "R_3"):
            v = [x["puissance"] for x in bloc["puissances"] if x["comparaison"] == kp]
            bloc["min_par_comparaison"][kp] = {"cellules_faisables": len(v),
                                               "min": min(v) if v else None,
                                               "max": max(v) if v else None}
        tous = [x["puissance"] for x in bloc["puissances"]]
        bloc["plus_basse"] = min(tous) if tous else None
        bloc["plus_haute"] = max(tous) if tous else None
        bloc["une_comparaison_sans_cellule_faisable"] = any(
            v["cellules_faisables"] == 0 for v in bloc["min_par_comparaison"].values())
        puiss[str(ev)] = bloc
    b10 = puiss["0.1"]
    declenche = (b10["plus_basse"] is None or b10["plus_basse"] < 0.5 - EPS
                 or b10["une_comparaison_sans_cellule_faisable"])
    attendu_238 = {"unanimite|loi 1": 4, "unanimite|loi 3": 2, "juge_seul|loi 1": 2,
                   "juge_seul|loi 3": 1, "juge_repete_trois_votes_majorite|loi 1": 2,
                   "juge_repete_trois_votes_majorite|loi 3": 2}
    R["regle_de_portee"] = {
        "par_ecart": puiss,
        "puissance_qui_decide_ecart_0.10": b10["plus_basse"],
        "une_comparaison_sans_cellule_faisable": b10["une_comparaison_sans_cellule_faisable"],
        "comparaisons_d_agregations_descriptives": declenche,
        "P10_refutee_puissance_de_0.5_ou_plus": (b10["plus_basse"] is not None
                                                 and b10["plus_basse"] >= 0.5 - EPS),
        "comptes_de_cellules_faisables_contre_PR_l238": {
            k: {"attendu": v,
                "vu": b10["faisables_par_comparaison_et_loi"].get(k, {}).get("faisables")}
            for k, v in attendu_238.items()},
        "taille_du_monde_de_puissance": "n = 100 (PR l. 236) ; le fichier ne porte pas de champ n"}

    # ==================== 6. puissance de « positif » de rho' - rho (A1 regle A)
    rp = {}
    for c in d["ecart_rho_prime_moins_rho"]:
        g = rp.setdefault(str(c["ecart_vise"]), {"faisables": 0, "infaisables": 0, "les_deux": []})
        if c["faisable"]:
            g["faisables"] += 1
            g["les_deux"].append([c["rho"], c["puissance_les_deux"]])
        else:
            g["infaisables"] += 1
    for g in rp.values():
        v = [x[1] for x in g["les_deux"]]
        g["plus_basse"], g["plus_haute"] = (min(v), max(v)) if v else (None, None)
    R["puissance_positif_rho_prime_moins_rho"] = {
        "par_ecart": rp, "cellules_faisables": sum(g["faisables"] for g in rp.values()),
        "n": sorted({c["n"] for c in d["ecart_rho_prime_moins_rho"]})}

    # ================================================ 7. lectures descriptives
    # 7a. fa38f9faa24e0 (PR l. 320 ; A1 choix 11)
    comptes, desac_fa38 = {}, []
    for c in ea:
        J, br = c["J"], c["bras"]
        for rpv in ("0.0", "0.5", "0.9"):
            refs = [br["poids_egaux"], br[f"R_k{J}_rp{rpv}"]]
            P = br["P"]
            if any(r["faux_acceptes"] < 0.02 for r in refs) or any(
                    P["vrais_rejetes"] > r["vrais_rejetes"] + 0.05 for r in refs):
                m = "sans prise"
            elif all(P["faux_acceptes"] <= 0.85 * r["faux_acceptes"] + EPS for r in refs):
                m = "tient"
            else:
                m = "refute"
            g = comptes.setdefault(f"J={J}", {"sans prise": 0, "tient": 0, "refute": 0})
            g[m] += 1
            aide = norm(c["mot_fa38f9faa24e0_par_rho_prime"].get(rpv))
            if aide != m:
                desac_fa38.append([list(cle(c)), c["n"], rpv, m, aide])
    R["fa38f9faa24e0"] = {"mots_par_J": comptes, "desaccords_avec_l_aide": len(desac_fa38),
                          "exemples_de_desaccord": desac_fa38[:10]}

    # 7b. fefca, branche (2) (PR l. 321 ; A1 C2)
    b2, pire_b2 = {}, None
    for c in ea:
        if c["J"] != 5 or c["loi"] not in (1, 4):
            continue
        etal = c["n"] // 2
        ecart = c["bras"]["C"]["erreur_equilibree"] - c["bras"]["poids_egaux"]["erreur_equilibree"]
        g = b2.setdefault(etal, {"cellules": 0, "refute": 0, "ecart_max": None})
        g["cellules"] += 1
        if ecart > 0.02 + EPS:
            g["refute"] += 1
        if g["ecart_max"] is None or ecart > g["ecart_max"]:
            g["ecart_max"] = ecart
        if pire_b2 is None or ecart > pire_b2["ecart"]:
            pire_b2 = {"loi": c["loi"], "profil": c["profil"], "rho": c["rho_grille"],
                       "etalonnage": etal, "ecart": ecart}
    tailles = sorted(b2)
    plus_petite = None
    for i, t in enumerate(tailles):
        if all(b2[u]["refute"] == 0 for u in tailles[i:]):
            plus_petite = t
            break
    aide_b2 = d["criteres_mecaniques"]["branche_2_fefca0bd94064"]
    des_b2 = 0
    for kk, v in aide_b2["par_cellule"].items():
        moi = "refute" if v["ecart_C_moins_poids_egaux"] > 0.02 + EPS else "tient"
        if norm(v["mot"]) != moi:
            des_b2 += 1
    R["fefca_branche_2"] = {
        "par_taille_d_etalonnage": {str(t): b2[t] for t in tailles},
        "plus_petite_taille_a_partir_de_laquelle_la_branche_tient_partout": plus_petite,
        "pire_cellule": pire_b2, "cellules": sum(g["cellules"] for g in b2.values()),
        "aide_plus_petite_taille":
            aide_b2["plus_petite_taille_d_etalonnage_a_partir_de_laquelle_la_branche_tient_partout"],
        "desaccords_de_mot_avec_l_aide_sur_ses_propres_ecarts": des_b2,
        "a_deux_juges": "sans prise (PR l. 321)"}

    # 7c. fefca, branche (3) (PR l. 322 ; A1 choix 16)
    gc = {(c["t"], round(c["delta"], 6)): c for c in d["garde_de_cadrage"]}
    b3, des_b3 = {}, []
    aide_b3 = d["criteres_mecaniques"]["branche_3_fefca0bd94064"]
    for loi in ("suiveur_seduisant", "suiveur_repoussant", "seduit_sinon_fond"):
        for t in (20, 40):
            for cs in ("0.1", "0.15", "0.2", "0.25", "0.3"):
                saine = gc[(t, 0.0)]["par_loi"][loi]["part_des_rondes_declenchees"][cs]
                d02 = gc[(t, 0.2)]["par_loi"][loi]["part_des_rondes_declenchees"][cs]
                d05 = gc[(t, 0.5)]["par_loi"][loi]["part_des_rondes_declenchees"][cs]
                if saine > 0.10 + EPS:
                    m = "refute"
                elif d05 >= 0.5 - EPS:
                    m = "tient"
                else:
                    m = "sans prise"
                k3 = f"{loi}|t={t}|c={cs}"
                b3[k3] = {"part_saine": saine, "part_delta_0.2": d02, "part_delta_0.5": d05,
                          "mot": m}
                if k3 in aide_b3 and norm(aide_b3[k3]["mot"]) != m:
                    des_b3.append([k3, m, aide_b3[k3]["mot"]])
    R["fefca_branche_3"] = {"par_loi_t_c": b3, "desaccords_avec_l_aide": des_b3,
                            "P5_bis_refutee": bool(
                                b3["suiveur_seduisant|t=20|c=0.1"]["part_saine"] < 0.10
                                or b3["suiveur_seduisant|t=40|c=0.1"]["part_saine"] < 0.10
                                or b3["suiveur_seduisant|t=40|c=0.3"]["part_saine"] > 0.10)}

    # 7d. fcfa3d98b90f8 (PR l. 324 a 328), sur le suiveur seduisant ; autres lois sans mot
    dr, des_dr, tab = [], [], {}
    for c in d["double_rendu"]:
        for loi, v in c["par_loi"].items():
            mo = v["moyennes"]
            s, de = c["s"], c["delta"]
            # clause (i)
            if s <= EPS:
                ci = "non lue"
            else:
                e12 = v.get("fa_trait_bras_1_moins_bras_2")
                if (e12["moyenne"] > 0 and e12["bas"] > 0) or (
                        mo["vr_bras_1"] > mo["vr_bras_4"] + 0.05):
                    ci = "refute"
                elif mo["fa_trait_bras_2"] < 0.02:
                    ci = "sans prise"
                elif e12["haut"] < 0:
                    ci = "tient"
                else:
                    ci = "refute"
            # clause (iii)
            if abs(s - 0.5) > 1e-9:
                ciii = "non lue"
            else:
                e1, e4 = v.get("ecart_surface_bras_1"), v.get("ecart_surface_bras_4")
                if de <= EPS or (e4["bas"] >= -0.05 and e4["haut"] <= 0.05):
                    ciii = "sans prise"
                elif abs(e1["moyenne"]) >= 0.05 - EPS and (e1["bas"] > 0 or e1["haut"] < 0):
                    ciii = "refute"
                elif e1["bas"] >= -0.05 and e1["haut"] <= 0.05:
                    ciii = "tient"
                else:
                    ciii = "sans prise"
            # mot de la carte
            if s <= EPS:
                mc = "sans prise"
            elif ci == "refute" or ciii == "refute":
                mc = "refute"
            elif ci == "tient":
                mc = "tient"
            else:
                mc = "sans prise"
            a_i, a_iii, a_m = norm(v.get("clause_i")), norm(v.get("clause_iii")), norm(
                v.get("mot_de_la_carte"))
            ligne_ = {"loi": loi, "n": c["n"], "delta": de, "s": s, "clause_i": ci,
                      "clause_iii": ciii, "mot": mc, "aide_clause_i": v.get("clause_i"),
                      "aide_clause_iii": v.get("clause_iii"),
                      "aide_mot": v.get("mot_de_la_carte")}
            dr.append(ligne_)
            if loi == "suiveur_seduisant":
                tab.setdefault(f"delta={de}|s={s}", {})[str(c["n"])] = [ci, ciii, mc]
                if a_m != mc or (a_i not in (ci, None) and not (ci == "non lue")) or (
                        a_iii not in (ciii, None) and not (ciii == "non lue")):
                    des_dr.append(ligne_)
    R["fcfa3d98b90f8"] = {
        "suiveur_seduisant_par_delta_s_puis_n__clause_i__clause_iii__mot": tab,
        "desaccords_avec_l_aide_sur_le_suiveur_seduisant": des_dr,
        "toutes_les_lois": dr}

    # 7e. alarme, P6 (A1 l. 105 a 112)
    al, atteintes = {}, []
    for c in d["alarme"]:
        B, D = c["par_bras"]["B"]["comptes_silence_1"], c["par_bras"]["D"]["comptes_silence_1"]
        fa = B["suites_sans_changement_en_alarme"]
        e = {"fausse_alarme_bras_B_suites": fa,
             "sur": c["comptes_du_melange_plante"]["suites_sans_changement"],
             "clause_fausse_alarme_atteinte": fa > 80,
             "detection_a_effet_bras_B": B["suites_a_effet_detectees"],
             "detection_a_effet_bras_D": D["suites_a_effet_detectees"],
             "clause_detection_lue": c["m"] in (20, 40),
             "clause_detection_atteinte": (B["suites_a_effet_detectees"] <= D[
                 "suites_a_effet_detectees"]) if c["m"] in (20, 40) else None}
        if e["clause_fausse_alarme_atteinte"]:
            atteintes.append(f'fausse alarme, m={c["m"]}')
        if e["clause_detection_atteinte"]:
            atteintes.append(f'détection, m={c["m"]}')
        al[str(c["m"])] = e
    aide_p6 = d["criteres_mecaniques"]["alarme_fcbf4a2dd1a57"]["prediction_P6"]
    R["alarme_P6"] = {"par_m": al, "clauses_atteintes": atteintes,
                      "mot_P6": "P6 réfutée" if atteintes else "P6 non réfutée",
                      "carte": "mesurée, sans mot : aucune règle de mot gelée",
                      "aide_mot_P6": aide_p6["mot"],
                      "aide_clauses_atteintes": aide_p6["clauses_atteintes"]}

    # 7f. predictions P1, P3, P4 (lecture sur leur clause de refutation)
    p1_50 = {f"loi {L}": [tol[(k, 50)][0] for k in cellules
                          if k[0] == 2 and k[1] == L and k[2] == "egal_0.1"] for L in (1, 2)}
    p1_400 = {f"loi {L}": [tol[(k, 400)][0] for k in cellules
                           if k[0] == 2 and k[1] == L and k[2] == "egal_0.2"] for L in (1, 2, 3)}
    R["P1"] = {
        "taux_0.10_n_50_J2_cellules_qui_tiennent": {k: [sum(v), len(v)] for k, v in p1_50.items()},
        "taux_0.20_n_400_J2_cellules_qui_tiennent": {k: [sum(v), len(v)]
                                                     for k, v in p1_400.items()},
        "clause_tenue_a_50_pour_0.10__toutes_les_cellules_lois_1": all(p1_50["loi 1"]),
        "clause_manquee_a_400_pour_0.20__lois_1_et_3": not (all(p1_400["loi 1"])
                                                             and all(p1_400["loi 3"]))}
    g_ech, g_bloc200, g_p4 = None, [], None
    for c in ea:
        if c["J"] != 5:
            continue
        gain_c = c["comparaisons"]["F_majorite_stricte_moins_C"]["moyenne"]
        gain_n = c["comparaisons"]["F_majorite_stricte_moins_N"]["moyenne"]
        if c["loi"] == 1 and c["profil"].startswith("egal_"):
            if g_ech is None or gain_c > g_ech["gain"]:
                g_ech = {"gain": gain_c, "profil": c["profil"], "rho": c["rho_grille"], "n": c["n"]}
        if c["loi"] == 4 and c["n"] == 400 and c["rho_grille"] >= 0.6 - EPS:
            g_bloc200.append({"profil": c["profil"], "rho": c["rho_grille"], "gain": gain_c})
        if c["rho_grille"] >= 0.6 - EPS:
            if g_p4 is None or gain_n > g_p4["gain"]:
                g_p4 = {"gain": gain_n, "loi": c["loi"], "profil": c["profil"],
                        "rho": c["rho_grille"], "n": c["n"]}
    R["P3_P4"] = {
        "P3_plus_grand_gain_de_C_sur_la_majorite_juges_echangeables_loi_1": g_ech,
        "P3_clause_gain_de_0.02_ou_plus_juges_echangeables": bool(g_ech and g_ech["gain"] >= 0.02),
        "P3_gains_en_blocs_a_200_temoins_d_etalonnage_rho_0.6_ou_plus": g_bloc200,
        "P3_clause_aucun_gain_en_blocs_a_200": bool(g_bloc200) and all(x["gain"] <= 0
                                                                       for x in g_bloc200),
        "P4_plus_grand_gain_de_N_sur_la_majorite_a_rho_0.6_ou_plus": g_p4,
        "P4_clause_gain_de_0.02_ou_plus": bool(g_p4 and g_p4["gain"] >= 0.02)}

    # ============================================ 8. comparaison a l'aide du code
    ae = d["criteres_mecaniques"]["estimateur"]
    ap = d["criteres_mecaniques"]["puissance"]
    R["aide_du_code_pour_comparaison"] = {"estimateur": ae, "puissance": ap}

    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(R, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print("ecrit :", sortie)


if __name__ == "__main__":
    main()
