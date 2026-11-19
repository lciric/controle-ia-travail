"""Calcul du devis du plan de l'héritage à trois bras — v2.

Processeur seul, aucun appel, aucune dépense. Pièce de travail, version 2, à
vérifier par le contre-lecteur. Remplace, sans le modifier, calcul_devis_heritage_v1.py
(sha256 782a86104b518eb5a4a616111ec6fb50d70ac713bf58138013c1b27291b4b186).

Ce qui change par rapport à la v1 (contre-lecture
contre-lecture-plan-heritage-trois-bras-corrige-v1-v1.md, sha256
124767e4724bb125801b31df03c7021cc5cef1701349bdfa12c174fc8c3013da) :
- une génération finale par continuation, sur le monde tenu à l'écart (constat 8) :
  quatre générations de bras par continuation au lieu de trois ;
- le pilote de bruit est compté à part, en paires de courses jumelles, trois bras
  par source de pilote (constat 5), avec le facteur de borne haute de l'écart-type ;
- le scénario « minimal » de la v1 sort des totaux (constat 16) ;
- les appels perdus par le bras qui lit un registre, selon la part du coût d'un
  appel que prend la lecture (constat 2), pour la règle de la v2 et celle de la v1 ;
- la table unilatérale des rangs signés exacts, pour la règle de validité à dose
  nulle (constat 2) ;
- la sensibilité au coût, inconnu, de l'épreuve programmée par tentative (constat 1) ;
- le coût d'une source de plus.

Entrées : les coûts réels par rôle de la course d'auto-conception v9, recopiés du
manifeste de fin du lanceur
(runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json,
sha256 28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7,
champs cout_reel.par_role_usd et cout_reel.appels_par_role). Les noms de rôle
ci-dessous sont les clés de ce manifeste.

Usage : python3 -I -B calcul_devis_heritage_v2.py SORTIE.json
"""

import json
import math
import sys

# Coûts réels de la course v9, en USD (manifeste de fin du lanceur).
PAR_ROLE_USD = {
    "prop-opus": 7.432136,
    "prop-fable": 17.575927,
    "prop-argon": 4.171688,
    "prop-astra": 4.74571,
    "prop-carbon": 24.719127,
    "aiguilleur": 4.585798,
    "juge-opus": 6.863194,
    "juge-argon": 2.408891,
}
APPELS_PAR_ROLE = {
    "prop-opus": 11,
    "prop-fable": 11,
    "prop-argon": 11,
    "prop-astra": 11,
    "prop-carbon": 11,
    "aiguilleur": 96,
    "juge-opus": 94,
    "juge-argon": 94,
}
TOTAL_V9_USD = 72.50247
CARTES_A_PASSEPORT_V9 = 94
APPELS_PROPOSEURS_V9 = 55

# Trois compositions de proposeurs, onze appels par espèce comme à la v9.
COMPOSITIONS = {
    "A_cinq_especes_comme_v9": [
        "prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"],
    "B_trois_especes_sans_les_deux_plus_cheres": [
        "prop-opus", "prop-argon", "prop-astra"],
    "C_deux_especes_les_moins_cheres": ["prop-argon", "prop-astra"],
}

BRAS = 3
BRAS_DOSE_NULLE = 2
GENERATIONS_CONTINUATION = 3
GENERATION_FINALE = 1
GENERATIONS_SOURCE = 3
JUMELLES = 2

# Scénarios de l'étage payant (hors pilote) et du pilote de bruit.
SCENARIOS = {
    "estimation": {
        "sources": 12, "sources_dose_nulle": 8, "sources_pilote": 3,
        "facteur_unite": 1.0,
        "note": "douze sources à dose non nulle (recommandation du plan), huit à "
                "dose nulle (bras 2 et 3), pilote de neuf paires",
    },
    "haut": {
        "sources": 16, "sources_dose_nulle": 12, "sources_pilote": 4,
        "facteur_unite": 1.25,
        "note": "seize sources si la règle du pilote relève le nombre, douze à "
                "dose nulle, pilote de douze paires, coût de l'unité relevé d'un quart",
    },
    "pire": {
        "sources": 16, "sources_dose_nulle": 12, "sources_pilote": 4,
        "facteur_unite": 2.0,
        "note": "mêmes nombres que le cas haut, coût de l'unité doublé (la "
                "course v9 a coûté 1,8 fois son devis)",
    },
}

# Parts du coût d'un appel prises par la lecture du registre (hypothèses de calcul).
PARTS_LECTURE = [0.02, 0.05, 0.10, 0.141, 0.25, 0.50]
# Coût par tentative de l'épreuve programmée, inconnu : valeurs de sensibilité.
COUTS_EPREUVE_PAR_TENTATIVE_USD = [0.05, 0.10, 0.25, 0.50]


def generations_par_continuation():
    return GENERATIONS_CONTINUATION + GENERATION_FINALE


def generations_de_bras(s):
    g = generations_par_continuation()
    cibles = BRAS * s["sources"] * g
    dose_nulle = BRAS_DOSE_NULLE * s["sources_dose_nulle"] * g
    sources = (s["sources"] + s["sources_dose_nulle"]) * GENERATIONS_SOURCE
    pilote = s["sources_pilote"] * (GENERATIONS_SOURCE + BRAS * JUMELLES * g)
    return {
        "generations_par_continuation_finale_comprise": g,
        "continuations_du_critere": cibles,
        "continuations_a_dose_nulle": dose_nulle,
        "courses_sources": sources,
        "etage_payant_hors_pilote": cibles + dose_nulle + sources,
        "pilote_de_bruit": pilote,
        "pilote_paires_de_jumelles": s["sources_pilote"] * BRAS,
        "total_avec_pilote": cibles + dose_nulle + sources + pilote,
    }


def loi_rangs_signes(n):
    """Loi exacte de W+ (somme des rangs positifs), n différences, sans zéro ni ex æquo."""
    comptes = {0: 1}
    for rang in range(1, n + 1):
        suivant = {}
        for somme, c in comptes.items():
            suivant[somme] = suivant.get(somme, 0) + c
            suivant[somme + rang] = suivant.get(somme + rang, 0) + c
        comptes = suivant
    return comptes


def table_rangs_signes(n):
    comptes = loi_rangs_signes(n)
    total = 2 ** n
    maxi = n * (n + 1) // 2

    def p_unilateral(w):
        # w = somme des rangs du signe contraire ; p = P(W <= w)
        return sum(c for s, c in comptes.items() if s <= w) / total

    def p_bilateral(w):
        return min(1.0, 2.0 * p_unilateral(w))

    def plus_grand_w(fonction, seuil):
        meilleur = None
        for w in range(0, maxi // 2 + 1):
            if fonction(w) <= seuil:
                meilleur = w
        return meilleur

    return {
        "n": n,
        "plus_petite_p_bilaterale": 2.0 / total,
        "plus_grand_W_qui_passe_0_025_bilateral": plus_grand_w(p_bilateral, 0.025),
        "plus_grand_W_qui_passe_0_05_bilateral": plus_grand_w(p_bilateral, 0.05),
        "plus_petite_p_unilaterale": 1.0 / total,
        "plus_grand_W_contraire_qui_passe_0_05_unilateral": plus_grand_w(
            p_unilateral, 0.05),
    }


def gamma_inf_regularisee(a, x):
    """P(a, x), fonction gamma incomplète inférieure régularisée, par série."""
    if x <= 0:
        return 0.0
    terme = 1.0 / a
    somme = terme
    k = a
    for _ in range(100000):
        k += 1.0
        terme *= x / k
        somme += terme
        if abs(terme) < abs(somme) * 1e-16:
            break
    return somme * math.exp(-x + a * math.log(x) - math.lgamma(a))


def quantile_khi2(p, k):
    """Quantile d'ordre p de la loi du khi-deux à k degrés de liberté, par bissection."""
    bas, haut = 0.0, 10.0 * k + 100.0
    for _ in range(200):
        milieu = (bas + haut) / 2.0
        if gamma_inf_regularisee(k / 2.0, milieu / 2.0) < p:
            bas = milieu
        else:
            haut = milieu
    return (bas + haut) / 2.0


def borne_haute_ecart_type(k):
    """Facteur par lequel multiplier l'écart-type estimé sur k différences de
    moyenne nulle connue (jumelles échangeables, loi normale supposée) pour en
    avoir la borne haute unilatérale à 95 %."""
    q = quantile_khi2(0.05, k)
    return {"paires": k, "quantile_khi2_0_05": round(q, 4),
            "facteur_borne_haute_95": round(math.sqrt(k / q), 4)}


def appels_perdus(appels, part):
    """Bras qui lit un registre, budget égal : chaque appel coûte (1 + part) fois
    l'appel sans lecture.
    Règle v2 : le plus grand nombre d'appels dont le coût, lecture comprise, tient
    dans le budget. Règle v1 : arrondi à l'entier inférieur du nombre d'appels par
    espèce (onze appels par espèce)."""
    garde_v2 = int(math.floor(appels / (1.0 + part) + 1e-12))
    especes = appels // 11
    garde_v1 = especes * int(math.floor(11 / (1.0 + part) + 1e-12))
    return {"part_du_cout_d_un_appel": part,
            "appels_perdus_regle_v2": appels - garde_v2,
            "appels_perdus_regle_v1": appels - garde_v1}


def main():
    sortie = sys.argv[1]
    par_appel = {r: PAR_ROLE_USD[r] / APPELS_PAR_ROLE[r] for r in PAR_ROLE_USD}
    unites = {}
    for nom, roles in COMPOSITIONS.items():
        appels = sum(APPELS_PAR_ROLE[r] for r in roles)
        cout = sum(PAR_ROLE_USD[r] for r in roles)
        cartes = CARTES_A_PASSEPORT_V9 * appels / APPELS_PROPOSEURS_V9
        unites[nom] = {
            "appels_de_proposeurs": appels,
            "cout_generation_d_un_bras_usd": round(cout, 4),
            "tentatives_attendues_a_la_proportion_v9": round(cartes, 1),
            "option_aiguilleur_usd": round(
                par_appel["aiguilleur"] * cartes * 96 / 94, 4),
            "option_deux_juges_a_modele_usd": round(
                (par_appel["juge-opus"] + par_appel["juge-argon"]) * cartes, 4),
            "appels_perdus_par_le_bras_3_en_generation_1": [
                appels_perdus(appels, part) for part in PARTS_LECTURE],
        }
    g = generations_par_continuation()
    scenarios = {}
    for nom, s in SCENARIOS.items():
        gen = generations_de_bras(s)
        totaux = {}
        for comp, u in unites.items():
            base = u["cout_generation_d_un_bras_usd"] * s["facteur_unite"]
            option = s["facteur_unite"] * (
                u["option_aiguilleur_usd"] + u["option_deux_juges_a_modele_usd"])
            totaux[comp] = {
                "pilote_sans_aiguilleur_ni_juges_usd": round(
                    gen["pilote_de_bruit"] * base, 2),
                "etage_hors_pilote_sans_aiguilleur_ni_juges_usd": round(
                    gen["etage_payant_hors_pilote"] * base, 2),
                "total_sans_aiguilleur_ni_juges_usd": round(
                    gen["total_avec_pilote"] * base, 2),
                "pilote_avec_aiguilleur_et_juges_usd": round(
                    gen["pilote_de_bruit"] * (base + option), 2),
                "etage_hors_pilote_avec_aiguilleur_et_juges_usd": round(
                    gen["etage_payant_hors_pilote"] * (base + option), 2),
                "total_avec_aiguilleur_et_juges_usd": round(
                    gen["total_avec_pilote"] * (base + option), 2),
                "recommandation_pilote_sans_juges_et_etage_avec_usd": round(
                    gen["pilote_de_bruit"] * base
                    + gen["etage_payant_hors_pilote"] * (base + option), 2),
                "ajout_de_l_epreuve_programmee_usd_selon_cout_par_tentative": {
                    str(c): round(
                        gen["total_avec_pilote"] * s["facteur_unite"]
                        * u["tentatives_attendues_a_la_proportion_v9"] * c, 2)
                    for c in COUTS_EPREUVE_PAR_TENTATIVE_USD},
            }
        scenarios[nom] = {
            "parametres": s, "generations_de_bras": gen, "totaux": totaux}
    par_source = {
        comp: {
            "generations_de_bras_source_a_dose_non_nulle": BRAS * g + GENERATIONS_SOURCE,
            "generations_de_bras_source_a_dose_nulle":
                BRAS_DOSE_NULLE * g + GENERATIONS_SOURCE,
            "generations_de_bras_source_de_pilote":
                GENERATIONS_SOURCE + BRAS * JUMELLES * g,
            "une_source_a_dose_non_nulle_de_plus_usd": round(
                (BRAS * g + GENERATIONS_SOURCE) * u["cout_generation_d_un_bras_usd"], 2),
            "une_source_a_dose_nulle_de_plus_usd": round(
                (BRAS_DOSE_NULLE * g + GENERATIONS_SOURCE)
                * u["cout_generation_d_un_bras_usd"], 2),
            "une_source_de_pilote_de_plus_usd": round(
                (GENERATIONS_SOURCE + BRAS * JUMELLES * g)
                * u["cout_generation_d_un_bras_usd"], 2),
            "un_bras_de_diagnostic_douze_sources_usd": round(
                12 * g * u["cout_generation_d_un_bras_usd"], 2),
        }
        for comp, u in unites.items()
    }
    resultat = {
        "source_des_couts": {
            "manifeste": "runs/20261119-094145-course-auto-conception-v9/"
                         "manifeste-lanceur-fin.json",
            "sha256": "28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7",
            "total_v9_usd": TOTAL_V9_USD,
            "etape_proposition_v9_usd": round(sum(
                PAR_ROLE_USD[r] for r in COMPOSITIONS["A_cinq_especes_comme_v9"]), 6),
        },
        "cout_reel_par_appel_usd": {r: round(v, 4) for r, v in par_appel.items()},
        "generation_d_un_bras": unites,
        "scenarios": scenarios,
        "par_source": par_source,
        "pilote_borne_haute_de_l_ecart_type": [
            borne_haute_ecart_type(k) for k in (3, 6, 9, 12, 15)],
        "rangs_signes_exact": [table_rangs_signes(n) for n in range(4, 25)],
    }
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    main()
