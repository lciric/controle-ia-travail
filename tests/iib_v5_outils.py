"""Outils communs des essais de l'organisme retenu (v5) : étalonnage numérique jouet écrit et scellé, fichier d'entrées."""
import json
from pathlib import Path

import numpy as np

from controle_ia.iib import configuration_v5 as cf
from controle_ia.iib.jouet_v5 import etalonnage_numerique, ligne_numerique
from controle_ia.scellement import sceller

ENTREES = {"schema": cf.SCHEMA_ENTREES, "plafond_usd": 60, "depense_passee_usd": 5, "cout_fixe_usd": 10, "prix_horaire_usd": 1.3,
           "oracles_par_tour": 1, "actions_oracle_hors_tours": 3830,
           "plafond_de_tours": {"forme": "formule", "formule": cf.FORMULE_PLAFOND_DE_TOURS}}
DUREES = {"episode_genere_h": 0.004, "action_oracle_h": 0.0005}


def etalonnage(graine: int = 1, **kw) -> dict:
    e = etalonnage_numerique(np.random.default_rng(graine), **kw)
    return {"schema": cf.SCHEMA_ETALONNAGE, "lignes": e["lignes"], "taches": e["taches"], "durees": dict(DUREES), "depense_etalonnage_usd": 3.0}


def ecrire_scelle(chemin: Path, contenu) -> str:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(contenu, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return sceller(chemin)


def episode(oracle: str, exces: list, phase: str = "maitre", nom: str = "e0", sans_ancre: bool = False) -> list[dict]:
    """Dix sorties de l'oracle dont les actions 2 à 10 ont les excès donnés (None : action non bornable)."""
    lignes = [ligne_numerique(oracle, phase, nom, 0, 100.0, [100.0] * 8, sans_ancre, None, None)]
    for t, e in enumerate(exces, start=1):
        if e is None:
            lignes.append(ligne_numerique(oracle, phase, nom, t, None, [100.0] * 8, sans_ancre, 100.0, 100.0))
        else:
            l = ligne_numerique(oracle, phase, nom, t, 100.0, [100.0] * 8, sans_ancre, 100.0, 100.0)
            l["exces"] = float(e)                      # excès imposé à la valeur exacte voulue (bornes incluses)
            lignes.append(l)
    return lignes
