"""Calcul du devis du plan de l'héritage à trois bras — v4 : la dépense par paliers.

Processeur seul, aucun appel, aucune dépense. Pièce de travail, version 4.
Ne remplace pas calcul_devis_heritage_v2.py
(sha256 5d21b393f03f3e859241d97dea8347937596422c42f6b9f3cc4e5f5661b1a1c9), qui reste
la source de la table des rangs signés du plan (§ 3.3) et des totaux par étage ;
il n'existe pas de version 3 du calcul. Ce programme reprend les mêmes constantes
de coût et les mêmes formules, et ajoute :
- le découpage de la dépense en paliers (essai réel du test de mort ; pilote de
  bruit en deux temps ; sources à dose nulle ; sources à dose non nulle ; volet
  des témoins jugés ; bras de diagnostic), par composition et par scénario, avec
  le cumul ;
- le test de mort par tentative chiffré sur les bornes écrites dans le code de
  l'organisme (aucun coût réel n'est mesuré à ce jour) ;
- les variantes à deux, trois et cinq espèces à dépense égale ;
- les variantes à un seul contraste décisif et à dix sources.

Aucun nom de rôle ni aucun identifiant de modèle n'est écrit ici. Les espèces
sont numérotées de 1 à 5 par le coût réel croissant de leur rôle de proposeur
dans le manifeste de fin du lanceur de la course d'auto-conception v9
(runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json,
sha256 28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7,
champs cout_reel.par_role_usd et cout_reel.appels_par_role). Les deux juges à
modèle de la course sont ceux de l'espèce 3 et de l'espèce 1.

Usage : python3 -I -B calcul_devis_heritage_v4.py SORTIE.json
"""

import json
import math
import sys

# Coûts réels de la course v9, en USD (manifeste de fin du lanceur), recopiés de
# la v2 du calcul, clés renommées par numéro d'espèce.
PAR_ROLE_USD = {
    "proposeur_espece_1": 4.171688,
    "proposeur_espece_2": 4.74571,
    "proposeur_espece_3": 7.432136,
    "proposeur_espece_4": 17.575927,
    "proposeur_espece_5": 24.719127,
    "aiguilleur": 4.585798,
    "juge_espece_3": 6.863194,
    "juge_espece_1": 2.408891,
}
APPELS_PAR_ROLE = {
    "proposeur_espece_1": 11,
    "proposeur_espece_2": 11,
    "proposeur_espece_3": 11,
    "proposeur_espece_4": 11,
    "proposeur_espece_5": 11,
    "aiguilleur": 96,
    "juge_espece_3": 94,
    "juge_espece_1": 94,
}
TOTAL_V9_USD = 72.50247
CARTES_A_PASSEPORT_V9 = 94
APPELS_PROPOSEURS_V9 = 55

COMPOSITIONS = {
    "A_cinq_especes_comme_v9": [
        "proposeur_espece_1", "proposeur_espece_2", "proposeur_espece_3",
        "proposeur_espece_4", "proposeur_espece_5"],
    "B_trois_especes_sans_les_deux_plus_cheres": [
        "proposeur_espece_1", "proposeur_espece_2", "proposeur_espece_3"],
    "C_deux_especes_les_moins_cheres": [
        "proposeur_espece_1", "proposeur_espece_2"],
}

BRAS = 3
BRAS_DOSE_NULLE = 2
GENERATIONS_CONTINUATION = 3
GENERATION_FINALE = 1
GENERATIONS_SOURCE = 3
JUMELLES = 2
SOURCES_PILOTE_PREMIER_TEMPS = 2  # plancher du plan : six paires de jumelles

SCENARIOS = {
    "estimation": {"sources": 12, "sources_dose_nulle": 8, "sources_pilote": 3,
                   "facteur_unite": 1.0},
    "haut": {"sources": 16, "sources_dose_nulle": 12, "sources_pilote": 4,
             "facteur_unite": 1.25},
    "pire": {"sources": 16, "sources_dose_nulle": 12, "sources_pilote": 4,
             "facteur_unite": 2.0},
}

# Test de mort par tentative. Aucun coût réel n'est mesuré à ce jour. Les valeurs
# ci-dessous sont des bornes ou des prix écrits dans le code de l'organisme
# (/home/user/ideation-organism, commit a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb) :
# - 0,06 : prix prudent d'un tour de l'expérimentateur (tour_ferme_v64.py, en-tête,
#   point C : « 12 × 0,06 = 0,72 USD ») ;
# - 0,50 : plafond par fiche des sessions de l'expérimentateur, défaut de l'étage,
#   noté « SUPPOSÉ » (tests_de_mort.py, BUDGET_TEST_USD_DEFAUT) ;
# - 0,10 : plafond par fiche de la session du lecteur témoin, défaut de l'étage,
#   noté « SUPPOSÉ » (tests_de_mort.py, BUDGET_LECTEUR_USD_DEFAUT) ;
# - 0,80 : borne par carte de l'expérimentateur au tour fermé
#   (tour_ferme_v64.py, BUDGET_EXPERIMENTATEUR_PAR_CARTE_USD) ;
# - 12 : nombre maximal de tours de l'expérimentateur par fiche
#   (tests_de_mort.py, TOURS_MAX_PAR_FICHE).
PRIX_PRUDENT_D_UN_TOUR_USD = 0.06
TOURS_MAX_PAR_FICHE = 12
PLAFOND_EXPERIMENTATEUR_DEFAUT_USD = 0.50
PLAFOND_LECTEUR_DEFAUT_USD = 0.10
PLAFOND_EXPERIMENTATEUR_TOUR_FERME_USD = 0.80
COUTS_TEST_PAR_TENTATIVE = {
    "un_tour_au_prix_prudent": PRIX_PRUDENT_D_UN_TOUR_USD,
    "trois_tours_au_prix_prudent": 3 * PRIX_PRUDENT_D_UN_TOUR_USD,
    "plafond_par_defaut_de_l_experimentateur": PLAFOND_EXPERIMENTATEUR_DEFAUT_USD,
    "plafond_par_defaut_experimentateur_et_lecteur":
        PLAFOND_EXPERIMENTATEUR_DEFAUT_USD + PLAFOND_LECTEUR_DEFAUT_USD,
    "douze_tours_au_prix_prudent": TOURS_MAX_PAR_FICHE * PRIX_PRUDENT_D_UN_TOUR_USD,
    "borne_du_tour_ferme": PLAFOND_EXPERIMENTATEUR_TOUR_FERME_USD,
    "borne_du_tour_ferme_et_lecteur":
        PLAFOND_EXPERIMENTATEUR_TOUR_FERME_USD + PLAFOND_LECTEUR_DEFAUT_USD,
}


def generations_par_continuation():
    return GENERATIONS_CONTINUATION + GENERATION_FINALE


def par_source():
    g = generations_par_continuation()
    return {
        "source_a_dose_non_nulle": BRAS * g + GENERATIONS_SOURCE,
        "source_a_dose_nulle": BRAS_DOSE_NULLE * g + GENERATIONS_SOURCE,
        "source_de_pilote": GENERATIONS_SOURCE + BRAS * JUMELLES * g,
        "un_bras_de_diagnostic_par_source": g,
    }


def paliers_en_generations(s):
    """Générations de bras de chaque palier payant, pour un scénario."""
    u = par_source()
    premier = min(SOURCES_PILOTE_PREMIER_TEMPS, s["sources_pilote"])
    return {
        "palier_1_essai_reel_du_test_de_mort": 1,
        "palier_2a_pilote_deux_sources_six_paires": premier * u["source_de_pilote"],
        "palier_2b_pilote_sources_restantes":
            (s["sources_pilote"] - premier) * u["source_de_pilote"],
        "palier_3_sources_a_dose_nulle":
            s["sources_dose_nulle"] * u["source_a_dose_nulle"],
        "palier_4_sources_a_dose_non_nulle":
            s["sources"] * u["source_a_dose_non_nulle"],
    }


ORDRE_DES_PALIERS = [
    "palier_1_essai_reel_du_test_de_mort",
    "palier_2a_pilote_deux_sources_six_paires",
    "palier_2b_pilote_sources_restantes",
    "palier_3_sources_a_dose_nulle",
    "palier_4_sources_a_dose_non_nulle",
]


def unites():
    par_appel = {r: PAR_ROLE_USD[r] / APPELS_PAR_ROLE[r] for r in PAR_ROLE_USD}
    resultat = {}
    for nom, roles in COMPOSITIONS.items():
        appels = sum(APPELS_PAR_ROLE[r] for r in roles)
        cout = sum(PAR_ROLE_USD[r] for r in roles)
        tentatives = CARTES_A_PASSEPORT_V9 * appels / APPELS_PROPOSEURS_V9
        resultat[nom] = {
            "appels_de_proposeurs": appels,
            "cout_generation_d_un_bras_usd": cout,
            "tentatives_attendues_a_la_proportion_v9": tentatives,
            "option_aiguilleur_et_deux_juges_usd":
                par_appel["aiguilleur"] * tentatives * 96 / 94
                + (par_appel["juge_espece_3"] + par_appel["juge_espece_1"])
                * tentatives,
        }
    return resultat, par_appel


def table_des_paliers(u, s):
    gen = paliers_en_generations(s)
    f = s["facteur_unite"]
    lignes = {}
    cumul_gen = 0
    cumul_usd = 0.0
    for nom in ORDRE_DES_PALIERS:
        g = gen[nom]
        cout = g * u["cout_generation_d_un_bras_usd"] * f
        cumul_gen += g
        cumul_usd += cout
        lignes[nom] = {
            "generations_de_bras": g,
            "propositions_usd": round(cout, 2),
            "cumul_generations_de_bras": cumul_gen,
            "cumul_propositions_usd": round(cumul_usd, 2),
            "tentatives_attendues": round(
                g * u["tentatives_attendues_a_la_proportion_v9"], 1),
            "ajout_du_test_de_mort_usd": {
                cle: round(g * f * u["tentatives_attendues_a_la_proportion_v9"] * c, 2)
                for cle, c in COUTS_TEST_PAR_TENTATIVE.items()},
            "cumul_avec_test_de_mort_usd": {
                cle: round(cumul_usd + cumul_gen * f
                           * u["tentatives_attendues_a_la_proportion_v9"] * c, 2)
                for cle, c in COUTS_TEST_PAR_TENTATIVE.items()},
        }
    etage = (gen["palier_3_sources_a_dose_nulle"]
             + gen["palier_4_sources_a_dose_non_nulle"])
    lignes["palier_5_temoins_juges_pour_information"] = {
        "generations_de_bras_couvertes": etage,
        "aiguilleur_et_deux_juges_usd": round(
            etage * u["option_aiguilleur_et_deux_juges_usd"] * f, 2),
    }
    lignes["palier_6_un_bras_de_diagnostic"] = {
        "generations_de_bras": s["sources"] * generations_par_continuation(),
        "propositions_usd": round(
            s["sources"] * generations_par_continuation()
            * u["cout_generation_d_un_bras_usd"] * f, 2),
    }
    return lignes


def variantes_de_contraste(u):
    """Étage payant hors pilote, huit sources à dose nulle, selon le nombre de
    sources à dose non nulle (six : plancher technique à un seul contraste)."""
    ps = par_source()
    resultat = {}
    for n in (6, 10, 12, 16):
        g = n * ps["source_a_dose_non_nulle"] + 8 * ps["source_a_dose_nulle"]
        resultat[str(n)] = {
            "generations_de_bras": g,
            "propositions_usd": round(g * u["cout_generation_d_un_bras_usd"], 2),
        }
    return resultat


def a_depense_egale(us):
    """Nombre de sources à dose non nulle que chaque composition joue pour le prix
    du palier 4 de la composition A en estimation (douze sources)."""
    ps = par_source()
    budget = (12 * ps["source_a_dose_non_nulle"]
              * us["A_cinq_especes_comme_v9"]["cout_generation_d_un_bras_usd"])
    return {
        nom: {
            "budget_usd": round(budget, 2),
            "sources_a_dose_non_nulle_jouables": int(math.floor(
                budget / (ps["source_a_dose_non_nulle"]
                          * u["cout_generation_d_un_bras_usd"]) + 1e-9)),
            "tentatives_par_generation_de_bras": round(
                u["tentatives_attendues_a_la_proportion_v9"], 1),
        }
        for nom, u in us.items()
    }


def main():
    sortie = sys.argv[1]
    us, par_appel = unites()
    cout_a = us["A_cinq_especes_comme_v9"]["cout_generation_d_un_bras_usd"]
    deux_plus_cheres = (PAR_ROLE_USD["proposeur_espece_4"]
                        + PAR_ROLE_USD["proposeur_espece_5"])
    resultat = {
        "source_des_couts": {
            "manifeste": "runs/20261119-094145-course-auto-conception-v9/"
                         "manifeste-lanceur-fin.json",
            "sha256": "28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7",
            "total_v9_usd": TOTAL_V9_USD,
        },
        "cout_reel_par_appel_usd": {r: round(v, 4) for r, v in par_appel.items()},
        "generation_d_un_bras": {
            nom: {cle: (round(v, 4) if isinstance(v, float) else v)
                  for cle, v in u.items()}
            for nom, u in us.items()},
        "generations_de_bras_par_source": par_source(),
        "test_de_mort_par_tentative_usd": {
            cle: round(v, 2) for cle, v in COUTS_TEST_PAR_TENTATIVE.items()},
        "paliers": {
            nom_s: {
                "parametres": s,
                "par_composition": {
                    comp: table_des_paliers(u, s) for comp, u in us.items()},
            }
            for nom_s, s in SCENARIOS.items()},
        "variantes_de_contraste_etage_hors_pilote_estimation": {
            comp: variantes_de_contraste(u) for comp, u in us.items()},
        "a_depense_egale_du_palier_4_de_A": a_depense_egale(us),
        "part_des_deux_especes_les_plus_cheres_dans_A": {
            "part_des_appels": round(22 / 55, 4),
            "part_du_cout_de_proposition": round(deux_plus_cheres / cout_a, 4),
        },
    }
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    main()
