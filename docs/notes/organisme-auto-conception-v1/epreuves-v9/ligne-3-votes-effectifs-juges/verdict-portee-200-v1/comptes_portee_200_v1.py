"""Application du § 3 de l'additif 3 v3 aux comptes entiers de la mesure « portée à 200 », et déclencheurs de l'audit
de symétrie du § 6. Écrit par l'agent qui prononce, modèle O. Ne lit PAS l'aide du code (`criteres_mecaniques`).

Usage : python3 -B comptes_portee_200_v1.py RESULTAT_200 RESULTAT_ETAGE_1 SORTIE_JSON
"""
import json
import sys

R_ATTENDU = 2000
ECART_QUI_DECIDE = 0.10
MONDE = {"unanimite": ("U",), "juge_seul": ("S_1", "S_2"), "juge_repete_trois_votes_majorite": ("R_3",)}
NOMS = ("U", "S_1", "S_2", "R_3")


def compte_entier(p, R):
    k = round(p * R)
    if k / R != p or not (0 <= k <= R):
        raise SystemExit(f"puissance {p!r} n'est pas un compte entier sur {R}")
    return int(k)


def lire(chemin):
    with open(chemin, encoding="utf-8") as fh:
        return json.load(fh)["monde_de_puissance"]


def cellules_qui_decident(cellules):
    """(nom de comparaison du test, rang, compte) pour les cellules faisables à 0,10, lois 1 et 3."""
    lignes = []
    for rang, c in enumerate(cellules):
        if c.get("faisable") is not True or abs(c["ecart_vise"] - ECART_QUI_DECIDE) > 1e-12 or c["loi"] not in (1, 3):
            continue
        R = c["repliques"]
        for nom in MONDE[c["comparaison"]]:
            lignes.append((nom, rang, compte_entier(c["puissance_par_comparaison"][nom], R), R))
    return lignes


def main():
    c200 = lire(sys.argv[1])
    c100 = lire(sys.argv[2])
    sortie_chemin = sys.argv[3]

    l200 = cellules_qui_decident(c200)
    l100 = cellules_qui_decident(c100)
    assert all(R == R_ATTENDU for *_, R in l200)

    par_comp = {nom: [(rang, k) for (n, rang, k, _) in l200 if n == nom] for nom in NOMS}
    sans = [nom for nom, v in par_comp.items() if not v]
    minima = {}
    for nom, v in par_comp.items():
        if v:
            kmin = min(k for _, k in v)
            minima[nom] = {"repliques_gagnees": kmin, "puissance": kmin / R_ATTENDU,
                           "cellules": [{"rang": r, "loi": c200[r]["loi"], "rho": c200[r]["rho"],
                                         "rho_prime": c200[r]["rho_prime"], "comparaison_du_monde": c200[r]["comparaison"]}
                                        for r, k in v if k == kmin]}
    if sans:
        k_dec, issue = None, "B"
        cellules_min = []
    else:
        k_dec = min(m["repliques_gagnees"] for m in minima.values())
        cellules_min = [{"comparaison_du_test": nom, **cel} for nom, m in minima.items() if m["repliques_gagnees"] == k_dec
                        for cel in m["cellules"]]
        issue = "A" if 2 * k_dec >= R_ATTENDU else "B"  # « sous 0,5 » strict : 1 000 sur 2 000 = A
    p_dec = None if k_dec is None else k_dec / R_ATTENDU
    pres = k_dec is not None and 0.478 * R_ATTENDU <= k_dec <= 0.522 * R_ATTENDU  # 956 à 1 044

    # Étage 1 (n = 100) : même lecture, pour l'audit de symétrie
    par_comp_100 = {nom: [(rang, k) for (n, rang, k, _) in l100 if n == nom] for nom in NOMS}
    k_dec_100 = min(min(k for _, k in v) for v in par_comp_100.values())
    R100 = l100[0][3]
    p_dec_100 = k_dec_100 / R100

    # Toutes les cellules faisables (tous écarts), puissance du monde planté et des quatre comparaisons
    detail = []
    zero_ou_un = []
    for rang, c in enumerate(c200):
        if c.get("faisable") is not True:
            continue
        R = c["repliques"]
        comptes = {nom: compte_entier(c["puissance_par_comparaison"][nom], R) for nom in NOMS}
        c1 = c100[rang]
        comptes_100 = ({nom: compte_entier(c1["puissance_par_comparaison"][nom], c1["repliques"]) for nom in NOMS}
                       if c1.get("faisable") is True else None)
        plantees = MONDE[c["comparaison"]]
        for nom in NOMS:
            if comptes[nom] in (0, R):
                zero_ou_un.append({"rang": rang, "comparaison_du_test": nom, "plantee": nom in plantees,
                                   "ecart_vise": c["ecart_vise"], "repliques_gagnees": comptes[nom]})
        detail.append({
            "rang": rang, "comparaison_du_monde": c["comparaison"], "ecart_vise": c["ecart_vise"], "loi": c["loi"],
            "rho": c["rho"], "rho_prime": c["rho_prime"], "d": c["d"],
            "comptes_200": comptes, "comptes_100": comptes_100,
            "plantees_baisse_200_vs_100": {nom: (comptes_100 is not None and comptes[nom] / R < comptes_100[nom] / c1["repliques"])
                                           for nom in plantees},
            "ecart_observe_moyen_200": c.get("ecart_observe_moyen"),
            "bras_C_regle_choisie": c.get("bras_C_regle_choisie"),
            "bras_C_repli_poids_egaux": c.get("bras_C_repli_poids_egaux"),
        })

    zero_ou_un_plantees = [z for z in zero_ou_un if z["plantee"]]
    declencheurs = {
        "puissance_qui_decide_200_sous_celle_de_100": p_dec is not None and p_dec < p_dec_100,
        "puissance_qui_decide_200_au_dessus_de_0_90": p_dec is not None and p_dec > 0.90,
        "cellule_faisable_a_0_ou_1_exactement_comparaison_plantee": bool(zero_ou_un_plantees),
        "cellule_faisable_a_0_ou_1_exactement_toute_comparaison": bool(zero_ou_un),
        "hors_intervalle_predit_0_30_a_0_50": p_dec is None or p_dec < 0.30 or p_dec >= 0.50,
    }

    sortie = {
        "programme": "comptes_portee_200_v1.py",
        "aide_du_code_lue": False,
        "repliques_par_cellule": R_ATTENDU,
        "lignes_lues_a_0_10_lois_1_et_3": [{"comparaison_du_test": n, "rang": r, "repliques_gagnees": k,
                                            "loi": c200[r]["loi"], "rho": c200[r]["rho"], "rho_prime": c200[r]["rho_prime"]}
                                           for (n, r, k, _) in l200],
        "cellules_faisables_lues_par_comparaison": {nom: len(v) for nom, v in par_comp.items()},
        "comparaisons_sans_cellule_faisable": sans,
        "minima_par_comparaison": minima,
        "puissance_qui_decide": p_dec,
        "repliques_gagnees_qui_decident": k_dec,
        "cellules_au_minimum": cellules_min,
        "issue_par_le_paragraphe_3": issue,
        "pres_du_seuil_0_478_a_0_522": pres,
        "etage_1_puissance_qui_decide_n_100": p_dec_100,
        "etage_1_repliques_gagnees_qui_decident": k_dec_100,
        "etage_1_lignes_lues": [{"comparaison_du_test": n, "rang": r, "repliques_gagnees": k} for (n, r, k, _) in l100],
        "declencheurs_audit": declencheurs,
        "cellules_faisables_a_0_ou_1": zero_ou_un,
        "detail_cellules_faisables": detail,
    }
    with open(sortie_chemin, "x", encoding="utf-8") as fh:
        json.dump(sortie, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    resume = {k: sortie[k] for k in ("issue_par_le_paragraphe_3", "puissance_qui_decide", "repliques_gagnees_qui_decident",
                                     "cellules_au_minimum", "minima_par_comparaison", "comparaisons_sans_cellule_faisable",
                                     "cellules_faisables_lues_par_comparaison", "pres_du_seuil_0_478_a_0_522",
                                     "etage_1_puissance_qui_decide_n_100", "etage_1_repliques_gagnees_qui_decident",
                                     "declencheurs_audit", "cellules_faisables_a_0_ou_1", "lignes_lues_a_0_10_lois_1_et_3",
                                     "etage_1_lignes_lues")}
    print(json.dumps(resume, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
