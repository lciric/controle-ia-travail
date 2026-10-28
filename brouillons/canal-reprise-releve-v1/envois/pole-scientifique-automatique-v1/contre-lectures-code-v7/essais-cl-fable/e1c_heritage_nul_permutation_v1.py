"""E1c : taux de fausses promotions sous le **nul de permutation** de la banque (issues d'épreuve permutées entre les
lignes de chaque moniteur : aucune fiche n'est vraie), pour les 78 fiches de la population scriptée v2, sans héritage
(une épreuve) et avec l'héritage de la preuve sur G générations de redites éprouvées sur les mêmes lignes.

Règle de promotion, copiée de `Generation._juger_pari` : promue si cumul + log W_max ≥ log(1/α), où cumul = somme des
log W finaux des épreuves précédentes de la classe (`Memoire._indexer_classe`). Une classe promue n'est plus rééprouvée.
Évaluations par le noyau réel (`aide_noyau_v1.juger` : preparer_engagement, MondeBanque.mesures, evaluer).

Usage : python -I -B e1c_heritage_nul_permutation_v1.py COPIE_DU_CODE SORTIE.json PERMUTATIONS GENERATIONS URNE(0|1)
"""
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aide_noyau_v1 as a  # noqa: E402

sortie, R, G, urne = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5] == "1"
config = a.config_ligne_de_commande(urne=urne, multiplicite="aucune")
seuil = math.log(1 / config.alpha)
population = a.charger(a.POPULATION_V2)
debut = time.time()
compte = {"epreuves_0": 0, "promues_sans_heritage": 0}
promues_par_g = [0] * G
detail = []
for r in range(R):
    monde = a.MondeBanque(a.BANQUE_V2, 20261026, nul_informe=True)
    # nul de permutation : issues d'épreuve permutées par moniteur (la partie de calibrage reste telle quelle)
    import random
    rng = random.Random(a.graine_derivee(777, "permutation", r))
    for nom in sorted(monde.banque["moniteurs"]):
        lignes = [l for l in monde.banque["instances"] if l.get("partie", "epreuve") == "epreuve" and nom in l["issues"]]
        valeurs = [l["issues"][nom] for l in lignes]
        rng.shuffle(valeurs)
        for l, v in zip(lignes, valeurs):
            l["issues"][nom] = v
    for d in population:
        cumul, promue_g = 0.0, None
        for g in range(G):
            ident = f"G{g}-F01"
            enonce = d["enonce"] if g == 0 else d["enonce"] + f" (reprise {g})"
            f = a.fiche_depuis(d, identifiant=ident, enonce=enonce)
            _, ev, _ = a.juger(f, monde, config, numero=g)
            if cumul + ev["log_richesse_max"] >= seuil:
                promue_g = g
                break
            cumul += ev["log_richesse_finale"]
        compte["epreuves_0"] += 1
        compte["promues_sans_heritage"] += promue_g == 0
        if promue_g is not None:
            for g in range(promue_g, G):
                promues_par_g[g] += 1
        detail.append({"r": r, "fiche": d["identifiant"], "promue_a_la_generation": promue_g})
n = compte["epreuves_0"]
resultat = {"reglages": {"urne": urne, "nul_informe": True, "alpha": config.alpha, "permutations": R, "generations": G,
                         "fiches": len(population)},
            "taux_promues_sans_heritage": compte["promues_sans_heritage"] / n,
            "taux_promues_avec_heritage_jusqu_a_g": [round(x / n, 4) for x in promues_par_g],
            "promues_avec_heritage_jusqu_a_g": promues_par_g, "epreuves": n, "duree_s": round(time.time() - debut, 1)}
with open(sortie, "w", encoding="utf-8") as fo:
    json.dump(dict(resultat, detail=detail), fo, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
