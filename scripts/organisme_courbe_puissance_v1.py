"""Conception de la courbe dose-réponse de la chaîne complète de l'organisme d'idéation : puissance du test exact de
tendance selon le nombre de courses par dose, sous des formes de réponse supposées. Aucune donnée, aucun appel de modèle.
Usage (racine d'un arbre propre) : PYTHONPATH=src python scripts/organisme_courbe_puissance_v1.py
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

from controle_ia.manifeste import creer_manifeste, ecrire_resultat, generateur
from controle_ia.organisme_courbe.tendance_v1 import TableTendance, puissance

CONFIG = {
    "objet": "courbe dose-réponse de la chaîne complète de l'organisme : puissance du test exact de tendance",
    "doses_lambda": [0.0, 0.25, 0.5, 0.75, 1.0],
    "scores": [0, 1, 2, 3, 4],
    "alpha": 0.05,
    "courses_par_dose": [4, 6, 8, 10, 12],
    "tirages": 20000,
    "scenarios": {
        "nette": [0.0, 0.2, 0.5, 0.7, 0.8],
        "moyenne": [0.0, 0.1, 0.25, 0.4, 0.5],
        "faible": [0.0, 0.05, 0.1, 0.2, 0.3],
        "tardive": [0.0, 0.0, 0.1, 0.4, 0.6],
        "plate_0.3_niveau": [0.3, 0.3, 0.3, 0.3, 0.3],
        "nulle_sans_dents": [0.0, 0.0, 0.0, 0.0, 0.0],
    },
}
TACHES = ["puissance"]


def calculer(manifeste: dict) -> dict:
    c = CONFIG
    g = generateur(manifeste["graines"]["puissance"])
    lignes = []
    for n in c["courses_par_dose"]:
        table = TableTendance([n] * len(c["scores"]), c["scores"])
        for nom, probas in c["scenarios"].items():
            lignes.append({"courses_par_dose": n, "courses_total": n * len(c["scores"]), "scenario": nom,
                           **puissance(table, probas, c["alpha"], c["tirages"], g)})
    return {"puissance": lignes}


def main() -> int:
    racine = Path(__file__).resolve().parents[1]
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-organisme-courbe-puissance-v1"
    chemin, manifeste = creer_manifeste(racine, run_id, CONFIG, TACHES,
                                        commande="PYTHONPATH=src python scripts/organisme_courbe_puissance_v1.py")
    sortie = ecrire_resultat(racine, chemin, "puissance-courbe-v1", calculer(manifeste))
    print(chemin)
    print(sortie)
    return 0


if __name__ == "__main__":
    sys.exit(main())
