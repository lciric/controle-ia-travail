"""Calcul du devis de l'étage payant du plan de l'héritage à trois bras — v1.

Processeur seul, aucun appel, aucune dépense. Pièce de travail, à contre-lire.

Entrées : les coûts réels par rôle de la course d'auto-conception v9, recopiés du
manifeste de fin du lanceur
(runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json,
sha256 28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7,
champ cout_reel.par_role_usd et cout_reel.appels_par_role).

Sorties : un fichier JSON (chemin donné en argument) qui porte
- le coût réel par appel et par espèce ;
- le coût d'une « génération d'un bras » pour trois compositions de proposeurs ;
- le nombre de générations de bras de chaque scénario ;
- les totaux (estimation, haut, pire cas) ;
- la table du test des rangs signés exact (plus petite valeur p atteignable et
  plus grande somme de rangs W qui passe 0,025 et 0,05, bilatéral, sans zéro ni
  ex æquo) pour n = 5 à 14 sources.

Usage : python3 -I -B calcul_devis_heritage_v1.py SORTIE.json
"""

import json
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

# Scénarios : nombres de générations de bras.
# cibles          = bras x sources x générations (dose de dépendance non nulle)
# dose_nulle      = bras 2 et 3 seulement x sources à dose nulle x générations
# sources         = une course source par source (dose non nulle et dose nulle)
# pilote_de_bruit = deux courses du même bras (N-045 v2, énoncé 6 (i))
SCENARIOS = {
    "minimal": {
        "sources": 10, "generations": 3, "sources_dose_nulle": 0,
        "generations_source": 1, "facteur_unite": 1.0,
        "note": "plancher de dix sources ; dose nulle sur processeur seulement ; "
                "course source d'une génération",
    },
    "estimation": {
        "sources": 10, "generations": 3, "sources_dose_nulle": 6,
        "generations_source": 3, "facteur_unite": 1.0,
        "note": "dix sources à dose non nulle, six à dose nulle (bras 2 et 3), "
                "course source de trois générations",
    },
    "haut": {
        "sources": 12, "generations": 3, "sources_dose_nulle": 10,
        "generations_source": 3, "facteur_unite": 1.25,
        "note": "douze sources (réserve pour les différences nulles), dix à dose "
                "nulle, coût par génération relevé d'un quart",
    },
    "pire": {
        "sources": 12, "generations": 3, "sources_dose_nulle": 10,
        "generations_source": 3, "facteur_unite": 2.0,
        "note": "mêmes nombres que le cas haut, coût par génération doublé "
                "(la course v9 a coûté 1,8 fois son devis)",
    },
}
BRAS = 3
BRAS_DOSE_NULLE = 2
PILOTE_COURSES = 2


def generations_de_bras(s):
    cibles = BRAS * s["sources"] * s["generations"]
    dose_nulle = BRAS_DOSE_NULLE * s["sources_dose_nulle"] * s["generations"]
    sources = (s["sources"] + s["sources_dose_nulle"]) * s["generations_source"]
    pilote = PILOTE_COURSES * s["generations"]
    return {
        "cibles": cibles,
        "dose_nulle": dose_nulle,
        "courses_sources": sources,
        "pilote_de_bruit": pilote,
        "total": cibles + dose_nulle + sources + pilote,
    }


def table_rangs_signes(n):
    """Loi exacte de W+ (somme des rangs positifs), n différences, sans zéro ni ex æquo."""
    comptes = {0: 1}
    for rang in range(1, n + 1):
        suivant = {}
        for somme, c in comptes.items():
            suivant[somme] = suivant.get(somme, 0) + c
            suivant[somme + rang] = suivant.get(somme + rang, 0) + c
        comptes = suivant
    total = 2 ** n
    maxi = n * (n + 1) // 2

    def p_bilateral(w):
        # w = min(W+, W-) ; p = 2 x P(W+ <= w), borné à 1
        cumul = sum(c for s, c in comptes.items() if s <= w)
        return min(1.0, 2.0 * cumul / total)

    def plus_grand_w(seuil):
        meilleur = None
        for w in range(0, maxi // 2 + 1):
            if p_bilateral(w) <= seuil:
                meilleur = w
        return meilleur

    return {
        "n": n,
        "plus_petite_p_bilaterale": 2.0 / total,
        "plus_grand_W_qui_passe_0_025": plus_grand_w(0.025),
        "plus_grand_W_qui_passe_0_05": plus_grand_w(0.05),
        "p_au_W_limite_0_025": (
            None if plus_grand_w(0.025) is None else p_bilateral(plus_grand_w(0.025))),
    }


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
            "cartes_attendues_a_la_proportion_v9": round(cartes, 1),
            "option_aiguilleur_usd": round(
                par_appel["aiguilleur"] * cartes * 96 / 94, 4),
            "option_deux_juges_a_modele_usd": round(
                (par_appel["juge-opus"] + par_appel["juge-argon"]) * cartes, 4),
        }
    scenarios = {}
    for nom, s in SCENARIOS.items():
        g = generations_de_bras(s)
        totaux = {}
        for comp, u in unites.items():
            base = u["cout_generation_d_un_bras_usd"] * s["facteur_unite"]
            totaux[comp] = {
                "sans_aiguilleur_ni_juges_usd": round(g["total"] * base, 2),
                "avec_aiguilleur_et_juges_usd": round(
                    g["total"] * (base + s["facteur_unite"] * (
                        u["option_aiguilleur_usd"]
                        + u["option_deux_juges_a_modele_usd"])), 2),
            }
        scenarios[nom] = {
            "parametres": s, "generations_de_bras": g, "totaux": totaux}
    diagnostic = {
        comp: {
            "un_bras_de_diagnostic_dix_sources_trois_generations_usd": round(
                10 * 3 * u["cout_generation_d_un_bras_usd"], 2)}
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
        "bras_de_diagnostic": diagnostic,
        "rangs_signes_exact": [table_rangs_signes(n) for n in range(5, 15)],
    }
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    main()
