#!/usr/bin/env python3
"""Calcul du devis de la course « nouvelles attaques », trois generations - v2.

La v2 remplace la v1 apres la contre-lecture (corrections C17 et C18) :
le troisieme relais vaut dans les trois compositions ; le reste du credit
du premier relais part du credit declare et des depenses lues au registre.

Processeur seul : aucun appel, aucun reseau, aucune lecture de fichier.
Toutes les constantes sont recopiees de pieces du depot, citees avec leur
chemin et leur empreinte dans le devis (section « Sources »). Les especes
sont designees par un numero (ordre du cout reel croissant de leur role de
proposeur a la course v9) ; aucun nom de modele n'est ecrit.

Usage : python3 -B calcul_devis_course_nouvelles_attaques_v2.py SORTIE.json
La sortie ne porte ni date ni chemin : deux lancements rendent le meme
fichier a l'octet.
"""
import json
import sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_CEILING

D = Decimal

# --- Constantes, avec leur source (cle reprise dans le devis) ---------------

# S1 : devis de l'heritage v5, section 1 (couts reels de la course v9, par role)
V9_PROPOSEURS_USD = [D("4.17"), D("4.75"), D("7.43"), D("17.58"), D("24.72")]
V9_APPELS_PAR_ESPECE = 11
V9_AIGUILLEUR_USD = D("4.59")
V9_AIGUILLEUR_APPELS = 96
V9_JUGES_USD = [D("6.86"), D("2.41")]
V9_JUGES_APPELS = [94, 94]
V9_COURSE_USD = D("72.50")
# S1 bis : devis de l'heritage v5, section 2 (tentatives attendues)
V9_FICHES = {"A": 94, "B": 56, "C": 38}
# S2 : registre des depenses sur main, ligne 536
V9_COURSE_EXACT_USD = D("72.502472")
V9_PART_CLE_RELAIS_1_USD = D("36.457056")
# S3 : devis v2i de la course d'auto-conception, sections 1, 2, 3 et 4
V2I_ESTIMATION = {"proposition": D("44.64"), "aiguillage": D("3.41"), "juges": D("7.89"), "course": D("55.94")}
V2I_HAUT = {"proposition": D("70.03"), "aiguillage": D("20.46"), "juges": D("47.32"), "course": D("137.81")}
V2I_PLAFOND_ARRET_USD = D("150")
V2I_ECART_PLAFOND_DUR_PROPOSITION = D("10")   # 150 -> 140
V2I_ECART_SEUIL_AIGUILLAGE = D("15")          # 150 -> 135
V2I_ECART_SEUIL_JUGES = D("30")               # 150 -> 120
V2I_PIRE_PAR_APPEL_PROPOSEUR_USD = D("6.05")
V2I_EPREUVE_TEMOINS = {"estimation": D("1.18"), "plafond": D("5")}
V2I_CREDIT_NET_RELAIS_1_AVANT_V9_USD = D("199.03")  # estimation de S3, rapportee seulement
DEPENSE_VERIFICATION_CLE_RELAIS_1_USD = D("0.000108")  # S2, ligne 528
DEPENSE_EPREUVE_V9_CLE_RELAIS_1_USD = D("0.980399")  # S2, ligne 532
V2I_CREDIT_DECLARE_RELAIS_1_USD = D("200")
V2I_PART_AU_PIRE_RELAIS_3_PAR_GENERATION_USD = D("66.55")
# S4 : devis de la course d'ideation sur la question v2 du pilier attaque
PILIER_SONDE_TROIS_MODELES_USD = D("0.005")
PILIER_REEL_COURSE_UNE_GENERATION_USD = D("8.42")
PILIER_PLAFOND_USD = D("20")

# --- Parametres proposes par le redacteur (a geler a l'additif) -------------
GENERATIONS = 3
MARGE_SUR_LE_HAUT = D("1.05")
PAS_ARRONDI_PLAFOND = D("5")
PLAFOND_SONDE_REFUS_USD = D("1")
COMPOSITIONS = {"A": [0, 1, 2, 3, 4], "B": [0, 1, 2], "C": [0, 1]}
PLAFOND_RETENU_PAR_PRECEDENT = {"A": V2I_PLAFOND_ARRET_USD}


def c2(x):
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)


def c4(x):
    return x.quantize(D("0.0001"), rounding=ROUND_HALF_UP)


def plafond_superieur(x, pas):
    return (x / pas).to_integral_value(rounding=ROUND_CEILING) * pas


def texte(x):
    return format(x, "f")


def calculer():
    prop_v9 = sum(V9_PROPOSEURS_USD)
    juges_v9 = sum(V9_JUGES_USD)
    controle_somme = prop_v9 + V9_AIGUILLEUR_USD + juges_v9
    facteur_haut = {
        "proposition": V2I_HAUT["proposition"] / prop_v9,
        "aiguillage": V2I_HAUT["aiguillage"] / V9_AIGUILLEUR_USD,
        "juges": V2I_HAUT["juges"] / juges_v9,
    }
    sortie = {
        "piece": "calcul du devis de la course nouvelles attaques, v2",
        "generations": GENERATIONS,
        "controles": {
            "somme_des_roles_v9_usd": texte(c2(controle_somme)),
            "course_v9_usd": texte(V9_COURSE_USD),
            "somme_egale_a_la_course": c2(controle_somme) == V9_COURSE_USD,
            "v9_reel_sur_estimation_v2i": texte(c4(V9_COURSE_USD / V2I_ESTIMATION["course"])),
            "v9_reel_sur_haut_v2i": texte(c4(V9_COURSE_USD / V2I_HAUT["course"])),
            "v9_reel_sur_plafond": texte(c4(V9_COURSE_USD / V2I_PLAFOND_ARRET_USD)),
        },
        "couts_par_appel_v9_usd": {
            "proposeur_espece_%d" % (i + 1): texte(c4(v / V9_APPELS_PAR_ESPECE))
            for i, v in enumerate(V9_PROPOSEURS_USD)
        },
        "facteurs_du_haut_par_role": {k: texte(c4(v)) for k, v in facteur_haut.items()},
        "compositions": {},
    }
    sortie["couts_par_appel_v9_usd"]["aiguilleur"] = texte(c4(V9_AIGUILLEUR_USD / V9_AIGUILLEUR_APPELS))
    sortie["couts_par_appel_v9_usd"]["juge_1"] = texte(c4(V9_JUGES_USD[0] / V9_JUGES_APPELS[0]))
    sortie["couts_par_appel_v9_usd"]["juge_2"] = texte(c4(V9_JUGES_USD[1] / V9_JUGES_APPELS[1]))

    credit_reste = (V2I_CREDIT_DECLARE_RELAIS_1_USD - DEPENSE_VERIFICATION_CLE_RELAIS_1_USD - DEPENSE_EPREUVE_V9_CLE_RELAIS_1_USD - V9_PART_CLE_RELAIS_1_USD)
    cinquieme = V2I_CREDIT_DECLARE_RELAIS_1_USD / 5

    for nom, especes in COMPOSITIONS.items():
        appels = V9_APPELS_PAR_ESPECE * len(especes)
        part = D(appels) / D(V9_APPELS_PAR_ESPECE * len(V9_PROPOSEURS_USD))
        bas = {
            "proposition": sum(V9_PROPOSEURS_USD[i] for i in especes),
            "aiguillage": V9_AIGUILLEUR_USD * part,
            "juges": juges_v9 * part,
        }
        haut = {k: bas[k] * facteur_haut[k] for k in bas}
        bas_gen = sum(bas.values())
        haut_gen = sum(haut.values())
        regle_marge = plafond_superieur(haut_gen * MARGE_SUR_LE_HAUT, PAS_ARRONDI_PLAFOND)
        regle_juges = plafond_superieur(
            haut["proposition"] + haut["aiguillage"] + V2I_ECART_SEUIL_JUGES, PAS_ARRONDI_PLAFOND
        )
        plafond_regle = max(regle_marge, regle_juges)
        plafond_gen = PLAFOND_RETENU_PAR_PRECEDENT.get(nom, plafond_regle)
        seuil_dur_prop = plafond_gen - V2I_ECART_PLAFOND_DUR_PROPOSITION
        seuil_aig = plafond_gen - V2I_ECART_SEUIL_AIGUILLAGE
        seuil_juges = plafond_gen - V2I_ECART_SEUIL_JUGES
        ligne_course = plafond_gen * GENERATIONS
        pire_appels_prop = D(appels) * V2I_PIRE_PAR_APPEL_PROPOSEUR_USD
        total_plafond = ligne_course + V2I_EPREUVE_TEMOINS["plafond"] + PLAFOND_SONDE_REFUS_USD
        sonde_estimee = PILIER_SONDE_TROIS_MODELES_USD / 3 * len(especes)
        total_bas = bas_gen * GENERATIONS + V2I_EPREUVE_TEMOINS["estimation"] + sonde_estimee
        total_haut = haut_gen * GENERATIONS + V2I_EPREUVE_TEMOINS["plafond"] + PLAFOND_SONDE_REFUS_USD
        sortie["compositions"][nom] = {
            "especes": [i + 1 for i in especes],
            "appels_de_proposeur_par_generation": appels,
            "fiches_attendues_par_generation": V9_FICHES[nom],
            "fiches_attendues_sur_la_course": V9_FICHES[nom] * GENERATIONS,
            "par_generation_usd": {
                "bas": {k: texte(c2(v)) for k, v in bas.items()},
                "bas_total": texte(c2(bas_gen)),
                "haut": {k: texte(c2(v)) for k, v in haut.items()},
                "haut_total": texte(c2(haut_gen)),
                "pire_plafond_d_arret": texte(plafond_gen),
                "plafond_selon_la_regle": texte(plafond_regle),
                "plafond_regle_marge": texte(regle_marge),
                "plafond_regle_juges_lances_au_haut": texte(regle_juges),
            },
            "seuils_internes_par_generation_usd": {
                "plafond_dur_proposition": texte(seuil_dur_prop),
                "aiguillage_lance_si_cumul_au_plus": texte(seuil_aig),
                "juges_lances_si_cumul_au_plus": texte(seuil_juges),
                "au_haut_proposition_sous_plafond_dur": haut["proposition"] <= seuil_dur_prop,
                "au_haut_aiguillage_lance": haut["proposition"] <= seuil_aig,
                "au_haut_juges_lances": haut["proposition"] + haut["aiguillage"] <= seuil_juges,
                "pire_des_appels_de_proposeur": texte(c2(pire_appels_prop)),
                "proposition_coupee_au_pire_des_appels": pire_appels_prop > seuil_dur_prop,
            },
            "course_usd": {
                "bas": texte(c2(bas_gen * GENERATIONS)),
                "haut": texte(c2(haut_gen * GENERATIONS)),
                "pire_ligne_de_course": texte(ligne_course),
            },
            "lignes_a_part_usd": {
                "epreuve_des_temoins_estimation": texte(V2I_EPREUVE_TEMOINS["estimation"]),
                "epreuve_des_temoins_plafond": texte(V2I_EPREUVE_TEMOINS["plafond"]),
                "sonde_de_refus_estimation": texte(c4(sonde_estimee)),
                "sonde_de_refus_plafond": texte(PLAFOND_SONDE_REFUS_USD),
            },
            "total_usd": {
                "bas": texte(c2(total_bas)),
                "haut": texte(c2(total_haut)),
                "plafond_total": texte(total_plafond),
            },
            "plafonds_par_relais_usd": {
                "relais_1_aiguilleur_et_un_juge": texte(ligne_course),
                "relais_2_un_juge": texte(ligne_course),
                "relais_3_un_proposeur_seul": texte(
                    V2I_PART_AU_PIRE_RELAIS_3_PAR_GENERATION_USD * GENERATIONS
                ),
            },
            "credit_relais_1": {
                "reste_au_dernier_chiffre_lu_usd": texte(credit_reste),
                "part_au_pire_usd": texte(ligne_course),
                "couvre_la_part_au_pire": credit_reste > ligne_course,
                "manque_usd": texte(c2(max(D("0"), ligne_course - credit_reste))),
                "cinquieme_du_credit_declare_usd": texte(cinquieme),
            },
            "marge_plafond_sur_bas": texte(c4(plafond_gen / bas_gen)),
        }

    a = sortie["compositions"]["A"]
    sortie["leviers_composition_A_usd"] = {
        "sans_les_juges_par_generation_bas": texte(c2(juges_v9)),
        "sans_les_juges_sur_la_course_bas": texte(c2(juges_v9 * GENERATIONS)),
        "bras_temoin_tirages_independants_bas": a["course_usd"]["bas"],
        "bras_temoin_tirages_independants_ligne": a["course_usd"]["pire_ligne_de_course"],
    }
    sortie["reperes"] = {
        "course_ideation_pilier_attaque_reel_une_generation_usd": texte(PILIER_REEL_COURSE_UNE_GENERATION_USD),
        "course_ideation_pilier_attaque_plafond_usd": texte(PILIER_PLAFOND_USD),
        "pire_par_appel_de_proposeur_usd": texte(V2I_PIRE_PAR_APPEL_PROPOSEUR_USD),
    }
    return sortie


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage : calcul_devis_course_nouvelles_attaques_v2.py SORTIE.json\n")
        return 2
    sortie = calculer()
    with open(argv[1], "x", encoding="utf-8", newline="\n") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
