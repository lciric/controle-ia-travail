"""Calcul de l'additif 2 au complément de valeurs v3 (Luc payant, GO-2026-11-22-49).
Arithmétique seule, en centimes entiers. Aucune clé lue, aucun réseau."""
import json

E = {  # entrée -> (centimes, source)
    "haut_aiguilleur_plus_espece_4": (12435, "complément v3, § 3, table, ligne Luc"),
    "bas_aiguilleur_plus_espece_4": (6651, "complément v3, § 3, table, ligne Luc"),
    "haut_juge_espece_3": (10505, "complément v3, § 3 ; devis v11 § 10.4"),
    "bas_juge_espece_3": (2058, "additif 1 au complément v3, § 2"),
    "haut_proposeur_espece_3": (2661, "additif 1 au complément v3, § 2"),
    "bas_proposeur_espece_3": (2229, "additif 1 au complément v3, § 2"),
    "part_luc_go49": (26000, "GO-2026-11-22-49 : 260 USD au plus"),
    "part_luc_avant": (12563, "complément v3, § 0"),
    "part_luc_relevable_l1": (13604, "additif véhicule v2, L-1"),
    "part_minuit_avant": (15656, "additif 1 au complément v3, § 2"),
    "part_deuxieme_relais": (14039, "complément v3, § 4"),
    "part_troisieme_relais": (1701, "additif 1 au complément v3, § 4"),
    "plafond_lignes_a_part": (600, "complément v3, § 3 (5 + 1 USD)"),
    "ligne_de_course": (45000, "complément v3, § 9"),
    "plafond_total": (45600, "complément v3, § 9 ; GO-2026-11-20-67"),
    "pire_appel_proposeur": (605, "complément v3, § 6"),
    "sous_part_passe_x_luc": (7260, "devis passe X v2, § 4"),
    "fable_go45_au_moins": (11700, "devis passe X v2, § 4, B2"),
    "attaquant_informe_go50": (1200, "GO-2026-11-22-50 : environ 12 USD"),
    "reste_luc_declare": (15300, "recalcul part Luc 153 v2"),
}
v = {k: c for k, (c, _) in E.items()}
haut = v["haut_aiguilleur_plus_espece_4"] + v["haut_juge_espece_3"] + v["haut_proposeur_espece_3"]
bas = v["bas_aiguilleur_plus_espece_4"] + v["bas_juge_espece_3"] + v["bas_proposeur_espece_3"]
marge = v["part_luc_go49"] - haut
somme_parts = v["part_luc_go49"] + v["part_deuxieme_relais"] + v["part_troisieme_relais"]
somme_parts_avant = v["part_minuit_avant"] + v["part_luc_avant"] + v["part_deuxieme_relais"] + v["part_troisieme_relais"]
avec_lignes_dans_part = haut + v["plafond_lignes_a_part"]
engagement_luc = (v["part_luc_go49"] + v["plafond_lignes_a_part"] + v["sous_part_passe_x_luc"]
                  + v["fable_go45_au_moins"] + v["attaquant_informe_go50"])
u = lambda c: round(c / 100, 2)
controles = {
    "part_couvre_le_haut_des_quatre_roles": v["part_luc_go49"] >= haut,
    "marge_sous_un_pire_appel_de_proposeur": marge < v["pire_appel_proposeur"],
    "lignes_a_part_ne_tiennent_pas_dans_la_part": avec_lignes_dans_part > v["part_luc_go49"],
    "somme_des_parts_sous_la_ligne_de_course": somme_parts <= v["ligne_de_course"],
    "somme_parts_et_lignes_sous_plafond_total": somme_parts + v["plafond_lignes_a_part"] <= v["plafond_total"],
    "somme_des_parts_avant_egale_439_59": somme_parts_avant == 43959,
    "part_depasse_l_ancienne_borne_l1": v["part_luc_go49"] > v["part_luc_relevable_l1"],
}
sortie = {
    "entrees": {k: {"usd": u(c), "source": s} for k, (c, s) in E.items()},
    "luc": {
        "haut_des_quatre_roles_usd": u(haut), "bas_des_quatre_roles_usd": u(bas),
        "marge_part_moins_haut_usd": u(marge),
        "marge_en_pires_appels_entiers": marge // v["pire_appel_proposeur"],
        "haut_plus_lignes_a_part_usd": u(avec_lignes_dans_part),
        "manque_si_lignes_dans_la_part_usd": u(avec_lignes_dans_part - v["part_luc_go49"]),
        "hausse_de_la_part_usd": u(v["part_luc_go49"] - v["part_luc_avant"]),
    },
    "ensemble": {
        "somme_des_parts_avant_usd": u(somme_parts_avant),
        "somme_des_parts_apres_usd": u(somme_parts),
        "marge_sous_ligne_de_course_usd": u(v["ligne_de_course"] - somme_parts),
        "somme_parts_et_lignes_usd": u(somme_parts + v["plafond_lignes_a_part"]),
    },
    "engagement_luc_au_pire": {
        "total_usd": u(engagement_luc),
        "au_dela_du_reste_declare_usd": u(engagement_luc - v["reste_luc_declare"]),
        "note": "lignes de Luc comptées : part de course, lignes à part, sous-part passe X, Fable GO-45 (au moins), attaquant informé GO-50 ; demandes 28 à 30 non chiffrées",
    },
    "controles": controles,
    "tous_les_controles_tenus": all(controles.values()),
}
print(json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True))
