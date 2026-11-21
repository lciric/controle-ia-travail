#!/usr/bin/env python3
"""Calcul du devis de la course « seuil et moniteurs » de l'organisme d'idéation — v1.

Arithmétique seule : aucun fichier lu, aucun réseau, aucun aléa. La sortie (JSON, clés triées) va sur la sortie standard.
Chaque entrée porte sa source dans le champ `sources`. Les entrées marquées « règle du rédacteur » ne sont mesurées nulle
part : elles sont dites comme telles au devis.

Usage : python3 -B calcul_devis_course_seuil_et_moniteurs_v1.py > SORTIE.json
"""
import json
from decimal import Decimal, ROUND_HALF_UP

D = Decimal
CENT = D("0.01")


def arrondi(x):
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def texte(x):
    return format(arrondi(x), "f")


# ---------- entrées sourcées ----------
SOURCES = {
    "S1": "coûts réels de la course v9, une génération, cinq espèces, onze appels par proposeur : devis v6 de la course "
          "« nouvelles attaques » (d825cb31…), § 1, ligne S1, qui cite le devis de l'héritage v5 (30c87fa6…), § 1 et § 2",
    "S2": "facteurs du cas haut par rôle : préenregistrement court v9 de la course « nouvelles attaques » (864f39a7…), "
          "section « Seuil », paragraphe « Coûts par rôle du premier relais »",
    "S3": "plafond d'arrêt d'une génération à cinq espèces (150), pire par appel de proposeur (6,05), épreuve des témoins "
          "(1,18 estimé, 5 de plafond) : devis v6, § 1, ligne S3",
    "S4": "sonde de refus : environ 0,005 estimé (devis v6, § 1, ligne S4) ; ligne de 1 (préenregistrement court v9, « Seuil »)",
    "S5": "répartition par relais lue à la course v9 : devis v6, § 3 (premier relais : proposeurs des espèces 3 et 4, "
          "aiguilleur, juge de l'espèce 3 ; deuxième : proposeurs des espèces 1 et 5, juge de l'espèce 1 ; troisième : "
          "proposeur de l'espèce 2)",
    "R1": "règle du rédacteur : étage des tests de mort, vingt candidates ; cas bas = une session d'expérimentateur au coût "
          "réel moyen d'un appel de proposeur ; cas haut = deux sessions au coût réel le plus haut d'un appel, fois le "
          "facteur du haut de la proposition ; pire = plafond de l'étage. Aucune mesure réelle de l'étage n'existe.",
    "R2": "règle du rédacteur : machine jetable du bac, 2 au cas bas, 5 au cas haut, 10 de plafond ; seule source : "
          "« quelques dollars » (registre, R-3984) ; à remplacer par l'offre relevée du loueur avant la ligne de GO.",
}

PROPOSEURS_REEL = {"espece_1": D("4.17"), "espece_2": D("4.75"), "espece_3": D("7.43"), "espece_4": D("17.58"),
                   "espece_5": D("24.72")}
AIGUILLEUR_REEL = D("4.59")
JUGES_REEL = {"juge_espece_3": D("6.86"), "juge_espece_1": D("2.41")}
APPELS_PAR_PROPOSEUR = 11
FACTEUR_HAUT = {"proposition": D("1.1940"), "aiguillage": D("4.4575"), "juges": D("5.1046")}
PLAFOND_GENERATION = D("150")
PIRE_PAR_APPEL_PROPOSEUR = D("6.05")
TEMOINS = {"bas": D("1.18"), "haut": D("5"), "pire": D("5")}
SONDE = {"bas": D("0.005"), "haut": D("1"), "pire": D("1")}
GENERATIONS = 1
ETAGES = 1
CANDIDATES_ETAGE = 20
SESSIONS_HAUT_PAR_CANDIDATE = 2
PLAFOND_ETAGE = D("110")
MACHINE = {"bas": D("2"), "haut": D("5"), "pire": D("10")}

# ---------- une génération ----------
somme_proposeurs = sum(PROPOSEURS_REEL.values())
somme_juges = sum(JUGES_REEL.values())
gen_bas = somme_proposeurs + AIGUILLEUR_REEL + somme_juges
gen_haut = (somme_proposeurs * FACTEUR_HAUT["proposition"] + AIGUILLEUR_REEL * FACTEUR_HAUT["aiguillage"]
            + somme_juges * FACTEUR_HAUT["juges"])
gen_pire = PLAFOND_GENERATION

# ---------- l'étage des tests de mort ----------
appels_proposeur = APPELS_PAR_PROPOSEUR * len(PROPOSEURS_REEL)
cout_moyen_appel = somme_proposeurs / appels_proposeur
cout_max_appel = max(PROPOSEURS_REEL.values()) / APPELS_PAR_PROPOSEUR
etage_bas = CANDIDATES_ETAGE * cout_moyen_appel
etage_haut = CANDIDATES_ETAGE * SESSIONS_HAUT_PAR_CANDIDATE * cout_max_appel * FACTEUR_HAUT["proposition"]
etage_pire = PLAFOND_ETAGE
pire_par_candidate = SESSIONS_HAUT_PAR_CANDIDATE * PIRE_PAR_APPEL_PROPOSEUR
candidates_garanties_au_pire = int(PLAFOND_ETAGE // pire_par_candidate)

# ---------- relais ----------
premier = {"bas": PROPOSEURS_REEL["espece_3"] + PROPOSEURS_REEL["espece_4"] + AIGUILLEUR_REEL + JUGES_REEL["juge_espece_3"],
           "haut": (PROPOSEURS_REEL["espece_3"] + PROPOSEURS_REEL["espece_4"]) * FACTEUR_HAUT["proposition"]
                   + AIGUILLEUR_REEL * FACTEUR_HAUT["aiguillage"] + JUGES_REEL["juge_espece_3"] * FACTEUR_HAUT["juges"],
           "pire": PLAFOND_GENERATION * GENERATIONS}
deuxieme = {"bas": PROPOSEURS_REEL["espece_1"] + PROPOSEURS_REEL["espece_5"] + JUGES_REEL["juge_espece_1"],
            "haut": (PROPOSEURS_REEL["espece_1"] + PROPOSEURS_REEL["espece_5"]) * FACTEUR_HAUT["proposition"]
                    + JUGES_REEL["juge_espece_1"] * FACTEUR_HAUT["juges"],
            "pire": PLAFOND_GENERATION * GENERATIONS}
troisieme = {"bas": PROPOSEURS_REEL["espece_2"], "haut": PROPOSEURS_REEL["espece_2"] * FACTEUR_HAUT["proposition"],
             "pire": APPELS_PAR_PROPOSEUR * PIRE_PAR_APPEL_PROPOSEUR * GENERATIONS}
experimentateur = {"bas": etage_bas, "haut": etage_haut, "pire": etage_pire}

# ---------- totaux ----------
ligne_course = GENERATIONS * PLAFOND_GENERATION + ETAGES * PLAFOND_ETAGE
total = {
    "bas": GENERATIONS * gen_bas + ETAGES * etage_bas + MACHINE["bas"] + TEMOINS["bas"] + SONDE["bas"],
    "haut": GENERATIONS * gen_haut + ETAGES * etage_haut + MACHINE["haut"] + TEMOINS["haut"] + SONDE["haut"],
    "pire": ligne_course + MACHINE["pire"] + TEMOINS["pire"] + SONDE["pire"],
}
sans_etage = {
    "bas": GENERATIONS * gen_bas + TEMOINS["bas"] + SONDE["bas"],
    "haut": GENERATIONS * gen_haut + TEMOINS["haut"] + SONDE["haut"],
    "pire": GENERATIONS * PLAFOND_GENERATION + TEMOINS["pire"] + SONDE["pire"],
}
sans_juges = {
    "bas": total["bas"] - somme_juges,
    "haut": total["haut"] - somme_juges * FACTEUR_HAUT["juges"],
    "pire": total["pire"],
}


def trois(d):
    return {k: texte(v) for k, v in d.items()}


sortie = {
    "piece": "calcul-devis-course-seuil-et-moniteurs-v1",
    "unite": "USD",
    "sources": SOURCES,
    "regime": {"generations": GENERATIONS, "etages_de_tests_de_mort": ETAGES, "especes": len(PROPOSEURS_REEL),
               "cases_par_generation": APPELS_PAR_PROPOSEUR, "appels_de_proposeur": appels_proposeur,
               "candidates_a_l_etage": CANDIDATES_ETAGE},
    "une_generation": {"bas": texte(gen_bas), "haut": texte(gen_haut), "pire": texte(gen_pire),
                       "proposition_bas": texte(somme_proposeurs),
                       "proposition_haut": texte(somme_proposeurs * FACTEUR_HAUT["proposition"]),
                       "aiguillage_bas": texte(AIGUILLEUR_REEL),
                       "aiguillage_haut": texte(AIGUILLEUR_REEL * FACTEUR_HAUT["aiguillage"]),
                       "juges_bas": texte(somme_juges), "juges_haut": texte(somme_juges * FACTEUR_HAUT["juges"])},
    "etage_des_tests_de_mort": {"bas": texte(etage_bas), "haut": texte(etage_haut), "pire": texte(etage_pire),
                                "cout_reel_moyen_d_un_appel_de_proposeur": texte(cout_moyen_appel),
                                "cout_reel_le_plus_haut_d_un_appel_de_proposeur": texte(cout_max_appel),
                                "pire_par_candidate": texte(pire_par_candidate),
                                "candidates_garanties_si_chaque_session_va_au_pire": candidates_garanties_au_pire},
    "machine_jetable_du_bac": trois(MACHINE),
    "epreuve_des_temoins": trois(TEMOINS),
    "sonde_de_refus": {"bas": format(SONDE["bas"], "f"), "haut": texte(SONDE["haut"]), "pire": texte(SONDE["pire"])},
    "plafonds_par_relais": {"premier_relais": trois(premier), "deuxieme_relais": trois(deuxieme),
                            "troisieme_relais": trois(troisieme), "relais_de_l_experimentateur": trois(experimentateur)},
    "ligne_de_course_montant_exact": texte(ligne_course),
    "lignes_a_part": {"machine_jetable_et_essai_du_bac": texte(MACHINE["pire"]), "epreuve_des_temoins": texte(TEMOINS["pire"]),
                      "sonde_de_refus": texte(SONDE["pire"])},
    "total": trois(total),
    "plafond_total": texte(total["pire"]),
    "variantes": {"sans_etage_ni_machine": trois(sans_etage), "sans_les_deux_juges": trois(sans_juges)},
    "controles": {"somme_des_cas_hauts_des_trois_relais_egale_generation_haut":
                      texte(premier["haut"] + deuxieme["haut"] + troisieme["haut"]) == texte(gen_haut),
                  "somme_des_cas_bas_des_trois_relais_egale_generation_bas":
                      texte(premier["bas"] + deuxieme["bas"] + troisieme["bas"]) == texte(gen_bas),
                  "generation_bas_du_devis_v6": "72.51", "generation_haut_du_devis_v6": "137.81",
                  "generation_bas_retrouvee": texte(gen_bas) == "72.51",
                  "generation_haut_retrouvee": texte(gen_haut) == "137.81",
                  "plafond_de_l_etage_couvre_son_cas_haut": etage_haut <= PLAFOND_ETAGE},
}

print(json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True))
