"""Recalcul de la part de la clé Luc (aiguilleur et proposeur de l'espèce 4) si le solde réel est de 153 USD — v1.

Processeur seul : aucun réseau, aucune clé, aucun fichier lu. Arithmétique en centièmes de dollar entiers (une part ne
s'arrondit jamais vers le haut : complément v3, l. 35). Chaque entrée porte sa source : fichier et ligne (M = copie de main
en lecture, /home/user/main-lecture ; P = prereg/ideation-nouvelles-attaques-v1/ sous M).
Sortie : un objet JSON sur la sortie standard (clés triées), puis le code 0 si tous les contrôles d'arithmétique tiennent.
Emploi : python3 -I -B recalcul_part_luc_v1.py [solde_usd]   (défaut : 153)
"""
import json
import sys
from decimal import Decimal, ROUND_FLOOR

C = 100  # centièmes


def c(x):
    """USD (chaîne ou Decimal) -> centièmes entiers, au centime inférieur."""
    return int((Decimal(str(x)) * C).to_integral_value(rounding=ROUND_FLOOR))


def usd(n):
    return f"{n / C:.2f}"


ENTREES = {
    # clé : (valeur USD, source)
    "part_luc_fixee": ("125.63", "P/complement-valeurs-...-lot-1-v3.md l. 35 et l. 106 (b4ef87dc…)"),
    "reste_luc_au_complement": ("213.999998", "P/complement-...-v3.md l. 114"),
    "reserve_etage_2": ("88.36", "P/complement-...-v3.md l. 111 (R-4293) ; M/registres/decisions.md l. 4431"),
    "minimum_reste_au_complement": ("212.71", "P/complement-...-v3.md l. 106 et l. 116"),
    "haut_roles_luc": ("124.35", "P/complement-...-v3.md l. 106 ; P/devis-...-v11.md l. 406"),
    "bas_roles_luc": ("66.51", "P/complement-...-v3.md l. 106 ; P/devis-...-v11.md l. 406"),
    "haut_aiguilleur": ("61.38", "M/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/additif-1-v1/"
                        "calcul-devis-course-nouvelles-attaques-v6.json, cinq_especes.par_role_sur_la_course_usd.aiguilleur.haut (096597df…)"),
    "bas_aiguilleur": ("13.77", "même JSON, cinq_especes.par_role_sur_la_course_usd.aiguilleur.bas"),
    "haut_proposeur_espece_4": ("62.97", "même JSON, cinq_especes.par_espece_sur_la_course_usd.espece_4.haut"),
    "bas_proposeur_espece_4": ("52.74", "même JSON, cinq_especes.par_espece_sur_la_course_usd.espece_4.bas"),
    "pire_appel_proposeur": ("6.05", "M/P/preenregistrement-court-...-v9.md l. 383 ; complément v3 l. 166"),
    "part_minuit": ("156.56", "P/additif-1-complement-...-espece-3-sur-minuit-v2.md l. 56 (ce76e0d6…)"),
    "haut_deux_roles_minuit": ("131.66", "même additif, l. 56"),
    "lignes_a_part_plafond": ("6.00", "complément v3 l. 132 ; additif au complément l. 70"),
    "solde_rigaud_declare": ("25", "additif au complément l. 82 (R-4342)"),
    "reserve_bras_a_rigaud": ("8.35", "additif au complément l. 82"),
    "somme_des_parts_course": ("439.59", "additif au complément l. 146"),
    "plafond_total": ("456", "additif au complément l. 146 ; M/registres/go.md l. 629 (GO-2026-11-21-30)"),
    "luc_193_mot_relaye": ("193", "M/registres/decisions.md l. 4734 (R-4595, « LUC 193 USD »)"),
    "luc_depense_relevee": ("39.59", "M/registres/decisions.md l. 4786 (R-4647, « 39,59 USD dépensés, environ 153 restants »)"),
    "etage_2_compte": ("33.37", "M/registres/decisions.md l. 4663 (R-4525, étage 2 fini, 33,37 USD comptés)"),
    # Repères pour le repli de GO-2026-11-22-35 (M/registres/go.md l. 722) : tarifs du guide local de l'interface
    # (cache daté 2026-11-03), non relus sur la page du fournisseur ; aucun n'entre dans une part.
    "repere_entree_par_million_premier_repli": ("5", "guide local de l'interface, table des modèles (non relu)"),
    "repere_sortie_par_million_premier_repli": ("25", "idem"),
    "repere_entree_par_million_second_repli": ("3", "idem"),
    "repere_sortie_par_million_second_repli": ("15", "idem"),
}
JETONS_SORTIE_MAX = 128_000   # rapport du développeur du lot 4, l. 120 (max_tokens envoyé par l'outil)
OCTETS_REQUETE_MAX = 35_465   # devis v11, l. 418 (requête d'un proposeur, génération 1, hors registre et enveloppe)


def main(argv):
    solde = c(argv[1]) if len(argv) > 1 else c("153")
    v = {k: c(x) for k, (x, _) in ENTREES.items()}
    ctl, out = {}, {"entrees": {k: {"usd": x, "source": s} for k, (x, s) in ENTREES.items()},
                    "solde_hypothese_usd": usd(solde)}

    # 0. Contrôles de cohérence des sources
    ctl["haut_luc_egal_aiguilleur_plus_espece_4"] = v["haut_aiguilleur"] + v["haut_proposeur_espece_4"] == v["haut_roles_luc"]
    ctl["bas_luc_egal_aiguilleur_plus_espece_4"] = v["bas_aiguilleur"] + v["bas_proposeur_espece_4"] == v["bas_roles_luc"]
    ctl["minimum_egal_haut_plus_reserve"] = v["haut_roles_luc"] + v["reserve_etage_2"] == v["minimum_reste_au_complement"]
    ctl["part_egale_reste_moins_reserve_au_centime_inferieur"] = \
        v["reste_luc_au_complement"] - v["reserve_etage_2"] == v["part_luc_fixee"]
    ctl["193_moins_39_59_arrondi_egal_153"] = (v["luc_193_mot_relaye"] - v["luc_depense_relevee"]) // C == 153

    # 1. Lecture à la lettre du complément (l. 116) : reste ≥ 212,71 avant le départ
    manque_lettre = max(0, v["minimum_reste_au_complement"] - solde)
    out["lecture_lettre_l116"] = {"minimum_usd": usd(v["minimum_reste_au_complement"]), "tient": manque_lettre == 0,
                                  "manque_usd": usd(manque_lettre), "recharge_pour_tenir_la_lettre_usd": usd(manque_lettre)}

    # 2. Lecture « réserve tombée » (l. 113 ; R-4289) : reste ≥ part + pire des lots non clos sur la clé
    marge_sur_part = solde - v["part_luc_fixee"]
    out["lecture_reserve_tombee_l113"] = {
        "arret_11_reste_moins_part_usd": usd(marge_sur_part), "arret_11_tient_sans_lot_ouvert": marge_sur_part >= 0,
        "pire_maximal_des_lots_non_clos_tolere_usd": usd(max(0, marge_sur_part)),
        "part_moins_haut_des_roles_usd": usd(v["part_luc_fixee"] - v["haut_roles_luc"]),
        "part_recalculee_regle_R4289_sans_lot_ouvert_usd": usd(solde),
        "lot_ouvert_qui_ferait_tomber_la_part_sous_le_haut_usd": usd(solde - v["haut_roles_luc"]),
    }
    ctl["part_couvre_toujours_le_haut"] = v["part_luc_fixee"] >= v["haut_roles_luc"]

    # 3. Réduire la part : plus petite part qui tient le cas haut ; ce qu'elle libère
    out["option_reduire_la_part"] = {
        "plus_petite_part_qui_tient_le_haut_usd": usd(v["haut_roles_luc"]),
        "liberee_par_rapport_a_125_63_usd": usd(v["part_luc_fixee"] - v["haut_roles_luc"]),
        "sous_124_35_noeud_de_Lazar": True}

    # 4. Déplacer un rôle vers Minuit ou Rigaud
    marge_minuit = v["part_minuit"] - v["haut_deux_roles_minuit"]
    dispo_rigaud = v["solde_rigaud_declare"] - v["reserve_bras_a_rigaud"]
    dep = {}
    for role in ("aiguilleur", "proposeur_espece_4"):
        h = v["haut_aiguilleur"] if role == "aiguilleur" else v["haut_proposeur_espece_4"]
        reste_luc_haut = v["haut_roles_luc"] - h
        dep[role] = {
            "haut_du_role_usd": usd(h),
            "minuit_haut_apres_ajout_usd": usd(v["haut_deux_roles_minuit"] + h),
            "minuit_manque_sous_sa_part_156_56_usd": usd(max(0, v["haut_deux_roles_minuit"] + h - v["part_minuit"])),
            "minuit_reste_minimal_avant_lignes_a_part_usd": usd(v["haut_deux_roles_minuit"] + h + v["lignes_a_part_plafond"]),
            "rigaud_disponible_declare_usd": usd(dispo_rigaud),
            "rigaud_manque_usd": usd(max(0, h - dispo_rigaud)),
            "luc_haut_du_role_restant_usd": usd(reste_luc_haut),
            "luc_marge_au_solde_avec_le_seul_role_restant_usd": usd(solde - reste_luc_haut),
        }
    out["option_deplacer_un_role"] = dict(dep, minuit_marge_actuelle_usd=usd(marge_minuit),
                                          note="reste du jour de Minuit non établi (GO-2026-11-21-28) ; Rigaud dit sans crédit "
                                               "(M/registres/depenses.md l. 577-578)")
    ctl["minuit_marge_egale_24_90"] = marge_minuit == c("24.90")

    # 5. Relever la part (version neuve) : borne par la somme des parts sous le plafond total
    marge_plafond = v["plafond_total"] - v["somme_des_parts_course"]
    part_max = min(solde, v["part_luc_fixee"] + marge_plafond)
    out["option_relever_la_part"] = {
        "marge_somme_des_parts_sous_456_usd": usd(marge_plafond),
        "part_maximale_somme_sous_456_usd": usd(part_max),
        "marge_au_haut_a_cette_part_usd": usd(part_max - v["haut_roles_luc"]),
        "pires_appels_de_proposeur_entiers_dans_cette_marge": (part_max - v["haut_roles_luc"]) // v["pire_appel_proposeur"],
        "pires_appels_entiers_dans_la_marge_actuelle": (v["part_luc_fixee"] - v["haut_roles_luc"]) // v["pire_appel_proposeur"],
    }

    # 6. Repli de GO-2026-11-22-35 : pire d'une chaîne refusée, au pire de la course et aux repères (non relus)
    def pire_repere(e, s):
        # majorant : un jeton par octet d'entrée ; sortie au plafond de l'outil ; en micro-dollars puis centièmes au supérieur
        micro = OCTETS_REQUETE_MAX * e + JETONS_SORTIE_MAX * s  # e, s en USD par million -> micro-dollars
        return -(-micro // 10_000)
    p1 = pire_repere(int(ENTREES["repere_entree_par_million_premier_repli"][0]), int(ENTREES["repere_sortie_par_million_premier_repli"][0]))
    p2 = pire_repere(int(ENTREES["repere_entree_par_million_second_repli"][0]), int(ENTREES["repere_sortie_par_million_second_repli"][0]))
    out["repli_GO_35"] = {
        "pire_chaine_trois_tentatives_au_pire_de_la_course_usd": usd(3 * v["pire_appel_proposeur"]),
        "repere_pire_appel_premier_repli_usd": usd(p1), "repere_pire_appel_second_repli_usd": usd(p2),
        "reperes_sous_le_pire_de_6_05": p1 <= v["pire_appel_proposeur"] and p2 <= v["pire_appel_proposeur"],
        "marge_part_haut_actuelle_usd": usd(v["part_luc_fixee"] - v["haut_roles_luc"]),
        "une_chaine_au_pire_tient_dans_la_marge_actuelle": 3 * v["pire_appel_proposeur"] <= v["part_luc_fixee"] - v["haut_roles_luc"],
    }

    out["controles"] = ctl
    out["tous_les_controles_tenus"] = all(ctl.values())
    print(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True))
    return 0 if out["tous_les_controles_tenus"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
