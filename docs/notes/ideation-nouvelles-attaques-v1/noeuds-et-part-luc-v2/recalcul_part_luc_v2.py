"""Recalcul de la part de la clé Luc (aiguilleur et proposeur de l'espèce 4) si le solde réel est de 153 USD — v2.

v2 (même auteur, après la contre-lecture « À corriger », docs/notes/ideation-nouvelles-attaques-v1/noeuds-et-part-luc-v1/
contre-lecture-v1/contre-lecture-noeuds-et-part-luc-v1.md, 23e774f9…) : copie de recalcul_part_luc_v1.py (03ffa38e…,
inchangée, R12). Changements : (1) le relèvement de la part est borné par la ligne de course, 450 USD (devis v11 l. 380),
non par le plafond total de 456 (point 3.2) ; (2) le manque de la lettre de la l. 116 est calculé aussi hors du coût de
l'étage 2, que la l. 116 exclut (point 4.1) ; (3) la tolérance aux lots ouverts est rendue à chaque part envisagée
(point 3.3) ; (4) la chaîne de repli n'est chiffrée que pour le proposeur de l'espèce 4 ; celle de l'aiguilleur attend la
mesure de son pire (point 2.5) ; (5) arithmétique en micro-dollars entiers ; une part ou une marge s'affiche au centime
inférieur, un manque ou une recharge au centime supérieur.

Processeur seul : aucun réseau, aucune clé, aucun fichier lu. Chaque entrée porte sa source (M = /home/user/main-lecture ;
P = M/prereg/ideation-nouvelles-attaques-v1/). Sortie : un objet JSON (clés triées) ; code 0 si tous les contrôles tiennent.
Emploi : python3 -I -B recalcul_part_luc_v2.py [solde_usd]   (défaut : 153)
"""
import json
import sys
from decimal import Decimal

U = 1_000_000  # micro-dollars


def m(x):
    return int(Decimal(str(x)) * U)


def bas(n):   # centime inférieur
    return f"{(n // 10_000) / 100:.2f}"


def haut(n):  # centime supérieur
    return f"{(-(-n // 10_000)) / 100:.2f}"


ENTREES = {
    "part_luc_fixee": ("125.63", "complément v3 (P/complement-valeurs-preenregistrement-court-v9-lot-1-v3.md) l. 35, l. 106"),
    "reste_luc_au_complement": ("213.999998", "complément v3 l. 114"),
    "reserve_etage_2": ("88.36", "complément v3 l. 111 ; M/registres/decisions.md l. 4431 (R-4293)"),
    "minimum_reste_au_complement": ("212.71", "complément v3 l. 106, l. 116"),
    "haut_roles_luc": ("124.35", "complément v3 l. 106 ; devis v11 l. 406"),
    "bas_roles_luc": ("66.51", "complément v3 l. 106 ; devis v11 l. 406"),
    "haut_aiguilleur": ("61.38", "M/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/additif-1-v1/"
                        "calcul-devis-course-nouvelles-attaques-v6.json (096597df…), cinq_especes.par_role_sur_la_course_usd.aiguilleur.haut"),
    "bas_aiguilleur": ("13.77", "même JSON, cinq_especes.par_role_sur_la_course_usd.aiguilleur.bas"),
    "haut_proposeur_espece_4": ("62.97", "même JSON, cinq_especes.par_espece_sur_la_course_usd.espece_4.haut"),
    "bas_proposeur_espece_4": ("52.74", "même JSON, cinq_especes.par_espece_sur_la_course_usd.espece_4.bas"),
    "pire_appel_proposeur": ("6.05", "V9 (P/preenregistrement-court-course-nouvelles-attaques-v9.md) l. 383 ; complément v3 l. 166"),
    "part_minuit": ("156.56", "additif au complément (P/additif-1-complement-…-espece-3-sur-minuit-v2.md) l. 56"),
    "haut_deux_roles_minuit": ("131.66", "additif au complément l. 56"),
    "lignes_a_part_plafond": ("6.00", "complément v3 l. 132 ; additif au complément l. 70"),
    "solde_rigaud_declare": ("25", "additif au complément l. 82 (R-4342)"),
    "reserve_bras_a_rigaud": ("8.35", "additif au complément l. 82"),
    "part_deuxieme_relais": ("140.39", "additif au complément l. 143"),
    "part_troisieme_relais": ("17.01", "additif au complément l. 144"),
    "somme_des_parts_course": ("439.59", "additif au complément l. 146"),
    "ligne_de_course": ("450", "devis v11 l. 380 ; additif 1 l. 161"),
    "plafond_total": ("456", "devis v11 l. 386 ; M/registres/go.md l. 629 (GO-2026-11-21-30)"),
    "luc_193_mot_relaye": ("193", "M/registres/decisions.md l. 4734 (R-4595)"),
    "luc_depense_relevee": ("39.59", "M/registres/decisions.md l. 4786 (R-4647)"),
    "etage_2_compte": ("33.37", "M/registres/decisions.md l. 4663 (R-4525 ; « comptés », non relevés)"),
    "repere_entree_par_million_premier_repli": ("5", "guide local de l'interface (cache 2026-11-03), non relu ; repère seul"),
    "repere_sortie_par_million_premier_repli": ("25", "idem"),
    "repere_entree_par_million_second_repli": ("3", "idem"),
    "repere_sortie_par_million_second_repli": ("15", "idem"),
}
JETONS_SORTIE_MAX = 128_000   # rapport du développeur du lot 4, l. 120
OCTETS_REQUETE_MAX = 35_465   # devis v11 l. 418 (génération 1, hors registre et enveloppe : repère seul)


def main(argv):
    solde = m(argv[1]) if len(argv) > 1 else m("153")
    v = {k: m(x) for k, (x, _) in ENTREES.items()}
    ctl = {}
    out = {"entrees": {k: {"usd": x, "source": s} for k, (x, s) in ENTREES.items()}, "solde_hypothese_usd": bas(solde)}

    ctl["haut_luc_egal_aiguilleur_plus_espece_4"] = v["haut_aiguilleur"] + v["haut_proposeur_espece_4"] == v["haut_roles_luc"]
    ctl["bas_luc_egal_aiguilleur_plus_espece_4"] = v["bas_aiguilleur"] + v["bas_proposeur_espece_4"] == v["bas_roles_luc"]
    ctl["minimum_egal_haut_plus_reserve"] = v["haut_roles_luc"] + v["reserve_etage_2"] == v["minimum_reste_au_complement"]
    ctl["part_egale_reste_moins_reserve_au_centime_inferieur"] = \
        (v["reste_luc_au_complement"] - v["reserve_etage_2"]) // 10_000 * 10_000 == v["part_luc_fixee"]
    ctl["somme_des_quatre_parts_egale_439_59"] = v["part_minuit"] + v["part_luc_fixee"] + v["part_deuxieme_relais"] \
        + v["part_troisieme_relais"] == v["somme_des_parts_course"]
    ctl["plafond_total_egal_ligne_plus_lignes_a_part"] = v["ligne_de_course"] + v["lignes_a_part_plafond"] == v["plafond_total"]
    ctl["193_moins_39_59_proche_de_153"] = abs(v["luc_193_mot_relaye"] - v["luc_depense_relevee"] - m("153")) < m("1")

    # 1. Lettre de la l. 116
    manque_brut = max(0, v["minimum_reste_au_complement"] - solde)
    autres = v["reste_luc_au_complement"] - solde - v["etage_2_compte"]          # dépenses autres que l'étage 2
    reste_hors_e2 = v["reste_luc_au_complement"] - autres                          # = solde + étage 2
    manque_hors_e2 = max(0, v["minimum_reste_au_complement"] - reste_hors_e2)
    out["lecture_lettre_l116"] = {
        "manque_brut_usd": haut(manque_brut),
        "depenses_autres_que_l_etage_2_si_153_comprend_l_etage_2_usd": bas(autres),
        "reste_hors_etage_2_usd": bas(reste_hors_e2),
        "manque_hors_etage_2_usd": haut(manque_hors_e2),
        "la_lettre_se_declenche": autres > v["part_luc_fixee"] - v["haut_roles_luc"] or manque_hors_e2 > 0,
        "recharge_pour_tenir_la_lettre_usd": haut(manque_hors_e2),
        "hypothese": "153 comprend les 33,37 USD comptés de l'étage 2 ; sinon, la recharge est le manque brut",
    }

    # 2. Réserve tombée (l. 113 ; R-4289)
    marge = solde - v["part_luc_fixee"]
    out["lecture_reserve_tombee_l113"] = {
        "arret_11_reste_moins_part_usd": bas(marge), "arret_11_tient_sans_lot_ouvert": marge >= 0,
        "pire_maximal_des_lots_non_clos_tolere_usd": bas(max(0, marge)),
        "part_moins_haut_des_roles_usd": bas(v["part_luc_fixee"] - v["haut_roles_luc"]),
        "lot_ouvert_qui_ferait_tomber_la_part_sous_le_haut_usd": haut(solde - v["haut_roles_luc"]),
    }
    ctl["part_couvre_toujours_le_haut"] = v["part_luc_fixee"] >= v["haut_roles_luc"]

    # 3. Réduire
    out["option_reduire_la_part"] = {"plus_petite_part_qui_tient_le_haut_usd": bas(v["haut_roles_luc"]),
                                     "liberee_usd": bas(v["part_luc_fixee"] - v["haut_roles_luc"]),
                                     "sous_124_35_noeud_de_Lazar": True}

    # 4. Déplacer
    dispo_rigaud = v["solde_rigaud_declare"] - v["reserve_bras_a_rigaud"]
    dep = {"minuit_marge_actuelle_usd": bas(v["part_minuit"] - v["haut_deux_roles_minuit"]),
           "note": "reste du jour de Minuit non établi (GO-2026-11-21-28, go.md l. 627) ; Rigaud dit sans crédit "
                   "(M/registres/depenses.md l. 577-578) et hors course (R-4356)"}
    for role, h in (("aiguilleur", v["haut_aiguilleur"]), ("proposeur_espece_4", v["haut_proposeur_espece_4"])):
        dep[role] = {"haut_du_role_usd": bas(h),
                     "minuit_haut_apres_ajout_usd": bas(v["haut_deux_roles_minuit"] + h),
                     "minuit_manque_sous_sa_part_usd": haut(max(0, v["haut_deux_roles_minuit"] + h - v["part_minuit"])),
                     "minuit_reste_minimal_avant_lignes_a_part_usd": haut(v["haut_deux_roles_minuit"] + h + v["lignes_a_part_plafond"]),
                     "rigaud_disponible_declare_usd": bas(dispo_rigaud),
                     "rigaud_manque_usd": haut(max(0, h - dispo_rigaud))}
    out["option_deplacer_un_role"] = dep
    ctl["minuit_marge_egale_24_90"] = v["part_minuit"] - v["haut_deux_roles_minuit"] == m("24.90")

    # 5. Relever : borne = ligne de course (450) - somme des parts de course
    marge_ligne = v["ligne_de_course"] - v["somme_des_parts_course"]
    part_max = min(solde, v["part_luc_fixee"] + marge_ligne)
    out["option_relever_la_part"] = {
        "borne": "ligne de course de 450 USD (les quatre parts sont des parts de course ; les 6 USD des lignes à part sont hors d'elles)",
        "marge_sous_la_ligne_de_course_usd": bas(marge_ligne),
        "part_maximale_usd": bas(part_max),
        "engagement_total_a_cette_part_usd": bas(v["somme_des_parts_course"] + marge_ligne + v["lignes_a_part_plafond"]),
        "marge_au_haut_a_cette_part_usd": bas(part_max - v["haut_roles_luc"]),
        "pires_appels_de_proposeur_entiers_dans_cette_marge": (part_max - v["haut_roles_luc"]) // v["pire_appel_proposeur"],
        "tolerance_aux_lots_ouverts_a_cette_part_usd": bas(max(0, solde - part_max)),
        "marge_laissee_au_deuxieme_relais_sous_la_ligne_usd": bas(v["ligne_de_course"] - v["somme_des_parts_course"] - marge_ligne),
    }
    ctl["engagement_total_au_plus_456"] = v["somme_des_parts_course"] + marge_ligne + v["lignes_a_part_plafond"] <= v["plafond_total"]
    ctl["part_maximale_egale_136_04"] = part_max == m("136.04")

    # 6. Repli (GO-35) : pire par tentative retenu = pire de la course (décision (iii) de la mère)
    def repere(e, s):
        return OCTETS_REQUETE_MAX * e + JETONS_SORTIE_MAX * s   # micro-dollars
    out["repli_GO_35"] = {
        "proposeur_espece_4_pire_chaine_trois_tentatives_usd": bas(3 * v["pire_appel_proposeur"]),
        "aiguilleur_pire_chaine": "attend la mesure du pire d'un appel d'aiguilleur (complément v3 l. 83 ; additif au complément l. 72)",
        "repere_premier_repli_generation_1_usd": haut(repere(5, 25)),
        "repere_second_repli_generation_1_usd": haut(repere(3, 15)),
        "reperes_jamais_des_pires": True,
        "chaine_proposeur_tient_dans_la_marge_actuelle": 3 * v["pire_appel_proposeur"] <= v["part_luc_fixee"] - v["haut_roles_luc"],
        "chaine_proposeur_tient_dans_la_marge_relevee": 3 * v["pire_appel_proposeur"] <= part_max - v["haut_roles_luc"],
    }

    out["controles"] = ctl
    out["tous_les_controles_tenus"] = all(ctl.values())
    print(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True))
    return 0 if out["tous_les_controles_tenus"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
