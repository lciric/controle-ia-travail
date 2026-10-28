"""E1d : sous le nul de permutation, part des épreuves dont le log W **final** est > 0 (une telle classe, rééprouvée sur les
mêmes lignes, voit son cumul croître à chaque redite et finit promue : limite du taux de fausses promotions de l'héritage
quand le nombre de générations croît), et nombre de redites nécessaires (⌈(log 20 − log W_max) / log W_final⌉, borne).

Usage : python -I -B e1d_part_finale_positive_v1.py COPIE_DU_CODE SORTIE.json PERMUTATIONS URNE(0|1)
"""
import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aide_noyau_v1 as a  # noqa: E402

sortie, R, urne = sys.argv[2], int(sys.argv[3]), sys.argv[4] == "1"
config = a.config_ligne_de_commande(urne=urne, multiplicite="aucune")
population = a.charger(a.POPULATION_V2)
positives, total, redites = 0, 0, []
for r in range(R):
    monde = a.MondeBanque(a.BANQUE_V2, 20261026, nul_informe=True)
    rng = random.Random(a.graine_derivee(777, "permutation", r))  # mêmes permutations que e1c
    for nom in sorted(monde.banque["moniteurs"]):
        lignes = [l for l in monde.banque["instances"] if l.get("partie", "epreuve") == "epreuve" and nom in l["issues"]]
        valeurs = [l["issues"][nom] for l in lignes]
        rng.shuffle(valeurs)
        for l, v in zip(lignes, valeurs):
            l["issues"][nom] = v
    for d in population:
        _, ev, _ = a.juger(a.fiche_depuis(d, identifiant="G0-F01"), monde, config)
        total += 1
        if ev["log_richesse_finale"] > 0 and not ev["promue"]:
            positives += 1
            redites.append(math.ceil((math.log(20) - ev["log_richesse_max"]) / ev["log_richesse_finale"]))
resultat = {"urne": urne, "permutations": R, "epreuves": total,
            "part_finale_positive_non_promue": positives / total,
            "redites_necessaires_mediane": sorted(redites)[len(redites) // 2] if redites else None,
            "redites_necessaires_quantiles_10_90": [sorted(redites)[len(redites) // 10], sorted(redites)[9 * len(redites) // 10]] if redites else None}
with open(sortie, "w", encoding="utf-8") as f:
    json.dump(resultat, f, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
