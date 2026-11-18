"""Fabrique la grille préenregistrée de la simulation du plan séquentiel (aucune donnée lue, rien de joué).

    python3 -B faire-configuration-simulation-sequentiel-v1.py > configuration-simulation-sequentiel-v1.json
"""
import json

PART = 0.2            # part du risque donnée à la lecture intermédiaire (recommandation de l'option)
MARGE = 0.05          # décision de Lazar (brouillon 3, « Seuil »)
LOIN = 0.20           # effet « loin de la frontière » (valeur de planification, sans source)
REPLIQUES_GAUSSIEN = 400000
AP, MX, PARTAGE, RIEN = "accumuler_propre", "maximum_bat", "partage", "rien_de_propre"


def risque(etats, plafond):
    return {"genre": "risque", "etats": etats, "plafond": plafond}


def puissance(etats):
    return {"genre": "puissance", "etats": etats, "perte_permise": 0.05}


VERITES_GAUSSIENNES = {
    # nom : (D_somme, écart, D_maximum) par dose ; critères
    "nul": ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
            [risque([AP, PARTAGE], 0.025), risque([MX, PARTAGE], 0.025), puissance([RIEN])]),
    "frontiere-proprete": ([0] * 4, [LOIN] * 4, [0] * 4,
                           [risque([AP, PARTAGE], 0.025), {"genre": "temoin", "etats": [AP, PARTAGE]}]),
    "frontiere-gain": ([LOIN] * 4, [0] * 4, [LOIN] * 4,
                       [risque([AP, PARTAGE], 0.025), risque([MX, PARTAGE], 0.025)]),
    "frontiere-equivalence-proprete": ([MARGE] * 4, [0] * 4, [0] * 4, [risque([RIEN], 0.025)]),
    "frontiere-equivalence-ecart": ([0] * 4, [MARGE] * 4, [0] * 4, [risque([RIEN], 0.025)]),
    "interet-une-dose": ([0, 0, 0, MARGE], [0, 0, 0, MARGE], [0] * 4, [puissance([AP])]),
    "interet-quatre-doses": ([MARGE] * 4, [MARGE] * 4, [0] * 4, [puissance([AP])]),
    "double-quatre-doses": ([2 * MARGE] * 4, [2 * MARGE] * 4, [0] * 4, [puissance([AP])]),
    "maximum-quatre-doses": ([0] * 4, [-MARGE] * 4, [MARGE] * 4, [puissance([MX])]),
}

mondes = []
for n, n1 in ((400, 250), (500, 250), (600, 250)):
    for et in (0.038, 0.045):
        for rho in (0.0, 0.8):
            for nom, (d, e, dm, crit) in VERITES_GAUSSIENNES.items():
                mondes.append({
                    "nom": f"g-{nom}-n{n}-i{n1}-et{int(et * 1000)}-rho{int(rho * 10)}", "genre": "gaussien",
                    "config": {"n_taches": n, "n_intermediaire": n1, "pas_tranche": 50,
                               "erreur_type_64": {"d_somme": et, "ecart": et, "d_maximum": et},
                               "effets": {"d_somme": d, "ecart": e, "d_maximum": dm},
                               "correlation_doses": rho, "correlation_grandeurs": 0.5, "marge": MARGE,
                               "part_intermediaire": PART, "n_repliques": REPLIQUES_GAUSSIEN},
                    "criteres": crit})

BASE_SCORES = {"n_taches": 400, "n_intermediaire": 250, "n_directions": 100, "amplitude": 0.0,
               "amplitude_directions": 0.0, "actions_decalees": 10, "part_tache": 0.3, "part_commune": 0.2,
               "marge": MARGE, "part_intermediaire": PART, "tirages_intermediaire": 40000, "tirages_finale": 10000}
PLAFOND_DOSE = 0.00625      # niveau annoncé par dose et par côté (brouillon 3, « Seuil »)
for nom, change, n_rep, crit in (
        ("nul", {"verite": "nul"}, 1000, [risque(["AP"], PLAFOND_DOSE), risque(["M"], PLAFOND_DOSE)]),
        ("frontiere-proprete", {"verite": "frontiere", "amplitude_directions": 0.15}, 2000,
         [risque(["AP"], PLAFOND_DOSE)]),
        ("frontiere-ecart", {"verite": "concentre", "amplitude": {"croisement": True}, "actions_decalees": 2,
                             "n_directions": 40}, 6000, [risque(["AP"], PLAFOND_DOSE), risque(["M"], PLAFOND_DOSE)]),
        ("dense-interet", {"verite": "dense", "amplitude": {"cible": MARGE, "facteur": 1.0}}, 500, [puissance(["AP"])]),
        ("dense-fort", {"verite": "dense", "amplitude": {"cible": MARGE, "facteur": 1.5}}, 500, [puissance(["AP"])]),
        ("concentre-fort", {"verite": "concentre", "amplitude": 3.0, "actions_decalees": 2}, 500,
         [risque(["AP"], PLAFOND_DOSE), puissance(["M"])])):
    mondes.append({"nom": f"s-{nom}", "genre": "scores", "config": dict(BASE_SCORES, **change), "n_repliques": n_rep,
                   "criteres": crit})

print(json.dumps({"objet": "simulation du plan séquentiel du second cycle de la lecture « accumuler »", "version": 1,
                  "mondes": mondes}, indent=1, ensure_ascii=False, sort_keys=True))
