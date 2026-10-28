"""Aide commune aux essais de la contre-lecture : appelle le noyau du pôle **tel qu'il est** (préparation de l'engagement,
mesures du monde sur banque, évaluation), sans agent, pour mesurer des taux sur de nombreuses répétitions.

Chaque fonction reproduit les appels de `Generation.geler` et `Generation._juger_pari` (pole/cycle.py) ; le pipeline
complet avec agents simulés est employé à part (e1, e5, e7) pour confirmer sur la vraie boucle.
"""
import copy
import json
import os
import random
import sys

COPIE = os.environ.get("COPIE_POLE") or sys.argv[1]
sys.path.insert(0, COPIE)

from pole import selection_pari as sp  # noqa: E402
from pole import nul_filles_v2 as nf  # noqa: E402
from pole.cycle import ConfigGeneration, preparer_engagement, membres_de_l_archive  # noqa: E402
from pole.fiche import Fiche  # noqa: E402
from pole.monde_banque import MondeBanque  # noqa: E402
from pole.outils import ecrire_json_scelle, graine_derivee  # noqa: E402

BANQUE_V2 = os.path.join(COPIE, "exemples", "banque-t05-v2.json")
POPULATION_V2 = os.path.join(COPIE, "exemples", "population-banque-t05-v2.json")
TEMOINS_V2 = os.path.join(COPIE, "exemples", "temoins-banque-t05-v2.json")


def config_ligne_de_commande(**modifs):
    """Réglages par défaut de la ligne de commande (`pole.py`, principal) en sélection par pari."""
    reglages = dict(selection="pari", juge="v1", nul_filles="v2", taille_plan=120, taille_plan_filles=300,
                    urne=True, multiplicite="e-bh", nul_archive=True, nul_archive_ajuste=True, alpha=0.05,
                    graine=20261026)
    reglages.update(modifs)
    return ConfigGeneration(**reglages).valider()


def banque_permutee(source, graine, dossier):
    """Copie de la banque où, pour chaque moniteur, les issues de la partie d'épreuve sont permutées au hasard entre
    les lignes qui en portent une (nul de permutation : aucune issue d'épreuve n'est liée aux traits ; la partie de
    calibrage est laissée telle quelle). Rend le chemin de la copie."""
    with open(source, encoding="utf-8") as f:
        banque = json.load(f)
    rng = random.Random(graine)
    for nom in sorted(banque["moniteurs"]):
        lignes = [l for l in banque["instances"] if l.get("partie", "epreuve") == "epreuve" and nom in l["issues"]]
        valeurs = [l["issues"][nom] for l in lignes]
        rng.shuffle(valeurs)
        for l, v in zip(lignes, valeurs):
            l["issues"][nom] = v
    chemin = os.path.join(dossier, f"banque-permutee-{graine}.json")
    if not os.path.exists(chemin):
        ecrire_json_scelle(chemin, banque)
    return chemin


def fiche_depuis(d, identifiant=None, enonce=None):
    d = copy.deepcopy(d)
    d.pop("temoin", None)
    if identifiant:
        d["identifiant"] = identifiant
    if enonce:
        d["enonce"] = enonce
    return Fiche.depuis_dict(d).valider()


def juger(fiche, monde, config, numero=0, memoire=None, lois_parents=None, graine_noyau=None):
    """Gel puis jugement par le noyau, comme `Generation.geler` + `_juger_pari` (sans héritage) ; rend (gele, ev)."""
    supp = list(monde.membres_informes(fiche))
    if config.nul_archive and fiche.temoin is None and memoire is not None:
        supp += membres_de_l_archive(fiche, memoire, config.nul_archive_ajuste, None)
    gele = preparer_engagement(fiche, config, lois_parents, reservoir=monde.reservoir(fiche, numero),
                               membres_supplementaires=supp or None, moniteur=monde.moniteur_de(fiche))
    graine_noyau = graine_noyau if graine_noyau is not None else graine_derivee(config.graine, "noyau", numero)
    mesures = monde.mesures(fiche.enonce, gele, graine_noyau, numero)
    if gele.engagement.get("instants_lecture"):
        ev = nf.evaluer_v2(gele, mesures, graine_noyau=graine_noyau)
    else:
        ev = sp.evaluer(gele, mesures, graine_noyau=graine_noyau)
    return gele, ev, mesures


def charger(chemin):
    with open(chemin, encoding="utf-8") as f:
        d = json.load(f)
    return d["fiches"] if isinstance(d, dict) and "fiches" in d else d
