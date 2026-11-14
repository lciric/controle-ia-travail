#!/usr/bin/env python3
"""Témoins « idées tirées au hasard » de la course « conception propre » de l'atelier d'idées — version 1.

Huit fiches au gabarit de l'orchestrateur, assemblées par tirage dans des listes fermées (levier, objet, opération,
métrique, signe, seuil, raison, contrôle, coût) : la forme est complète, le fond n'est pas pensé. Elles se mêlent, sans
marque, aux fiches réelles servies au lecteur de la règle de sélection ; elles mesurent si la règle distingue une idée
pensée d'un assemblage formellement correct (conception-course-v1.md, § 5 et § 6).

Graines (R9) : `numpy.random.SeedSequence(ENTROPIE)`, une graine fille par fiche (`spawn`), consignées à la sortie avec les
versions et l'empreinte de ce fichier. Aucun appel, aucun réseau. La raison est tirée indépendamment du signe : elle n'est
cohérente avec lui que par hasard.

Usage : python -I -B tirer_fiches_hasard_v1.py SORTIE.json      (SORTIE absent : jamais écrasé)
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ENTROPIE = 2026111301
NOMBRE = 8

LEVIERS = {
    "juge": ["le nombre de tirages frais par carte", "le seuil ε du regroupement des doublons",
             "le nombre m fixé d'avance pour la règle de Benjamini et Hochberg sur les valeurs e",
             "la taille du jeu public d'instances sans issue", "le nombre d'épisodes du test de mort"],
    "proposeurs": ["le nombre de cartes par proposeur", "le nombre de passes par génération",
                   "la longueur de la description publique du monde servie aux proposeurs",
                   "le nombre de lois de l'archive servies aux proposeurs",
                   "l'ordre des six formes de la grammaire dans la consigne"],
    "composition": ["le nombre de proposeurs", "la part du proposeur le plus cher dans le budget",
                    "l'ordre de passage des proposeurs", "le nombre de proposeurs d'un même fournisseur",
                    "le nombre de générations par course"],
    "cout": ["le plafond de session des proposeurs", "la part du budget gardée en réserve", "le budget du juge",
             "le plafond par génération", "la part du budget de la dernière génération"],
}
OPERATIONS = [("doubler", "doublé"), ("diviser par deux", "divisé par deux"), ("tripler", "triplé"),
              ("réduire d'un tiers", "réduit d'un tiers"),
              ("tirer à chaque génération entre la moitié et le double de sa valeur", "tiré à chaque génération")]
METRIQUES = ["nombre de composantes plantées couvertes, lu par l'oracle après la course",
             "nombre de lois fausses promues, lu par l'oracle après la course",
             "nombre de copies promues, lu par l'oracle après la course",
             "coût en dollars par génération, relevé par les relais"]
RAISONS = ["cela déplace l'équilibre entre l'exploration de lois neuves et le raffinement des lois connues",
           "la variance des estimations du juge dépend directement de cette quantité",
           "les proposeurs réagissent à la forme de ce qui leur est servi plus qu'à son fond",
           "le coût marginal d'une carte n'est pas constant d'une génération à l'autre",
           "les groupes de doublons se forment autrement quand cette quantité change",
           "l'archive grandit plus ou moins vite selon cette quantité"]
CONTROLES = ["la même course sans la modification, au même coût", "une modification tirée au hasard, au même coût",
             "la même course avec les graines permutées, au même budget"]
SEUILS = [5, 10, 15, 20, 25, 30]
COUTS = [("processeur", "rejouable sur processeur à partir de courses déjà jouées"),
         ("depense", "quelques dollars d'appels par graine")]


def _choix(rng, liste):
    return liste[int(rng.integers(len(liste)))]


def fiche(rng) -> dict:
    levier = _choix(rng, sorted(LEVIERS))
    objet = _choix(rng, LEVIERS[levier])
    infinitif, participe = _choix(rng, OPERATIONS)
    metrique = _choix(rng, METRIQUES)
    signe = _choix(rng, ["+", "-"])
    seuil = _choix(rng, SEUILS)
    raison = _choix(rng, RAISONS)
    controle = _choix(rng, CONTROLES)
    nature, ordre = _choix(rng, COUTS)
    sens = "augmente" if signe == "+" else "diminue"
    return {
        "nom": f"{infinitif[0].upper() + infinitif[1:]} : {objet}",
        "type": "approche",
        "enonce": (f"Proposition : {infinitif} {objet}, toutes choses égales par ailleurs, à budget égal. Le reste de "
                   f"l'organisme ne change pas : mêmes proposeurs, même juge, mêmes plafonds, même monde. L'idée tient à "
                   f"ce que {raison} ; avec {objet} {participe}, le {metrique.split(',')[0]} {sens} d'au moins {seuil} %."),
        "loi_predictive": {
            "espace_instances": ("une famille de mondes plantés jamais servie à la conception, trente graines scellées, "
                                 "une course de trois générations par graine"),
            "prediction": f"le {metrique.split(',')[0]} {sens} d'au moins {seuil} % par rapport à la course de référence",
            "signe": signe,
            "metrique": f"{metrique} ; témoin : {controle}"},
        "perte_traduction": (f"L'effet de {objet} peut dépendre du monde ; une seule valeur de l'opération est éprouvée."),
        "questions_servies": [f"levier:{levier}", "nouvelle"],
        "avantage": {"source": "organisme",
                     "texte": "Le monde planté permet de mesurer l'effet de la modification contre la vérité.",
                     "incopiable_parce_que": "Il faut un monde à graine scellée et un oracle lu après la course."},
        "originalite": {"niveau": "inedite", "texte": f"Faire varier {objet} n'a pas été essayé dans cet organisme."},
        "demande_organisme": {"nature": "modification", "texte": f"{infinitif[0].upper() + infinitif[1:]} {objet}."},
        "cout": {"nature": nature, "ordre_de_grandeur": ordre},
        "piege": f"Comparer à un témoin qui n'a pas le même coût que la course modifiée ; ici : {controle}.",
        "cosmetique_si": "Si l'écart au témoin ne dépasse pas l'écart entre deux graines de la course de référence.",
        "anteriorite": []}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage : tirer_fiches_hasard_v1.py SORTIE.json")
    sortie = Path(sys.argv[1])
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    ss = np.random.SeedSequence(ENTROPIE)
    enfants = ss.spawn(NOMBRE)
    temoins = []
    for k, e in enumerate(enfants, 1):
        temoins.append({"code": f"T-H{k}", "famille": "hasard", "cible": "R7 (mécanisme) ; voir conception § 6",
                        "graine": {"entropie": ENTROPIE, "spawn_key": list(e.spawn_key)},
                        "attendu": {"N": "aucune"}, "fiche": fiche(np.random.default_rng(e))})
    soi = Path(__file__).resolve()
    sortie.write_text(json.dumps({
        "outil": {"chemin": soi.name, "sha256": hashlib.sha256(soi.read_bytes()).hexdigest()},
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__},
        "graines": {"entropie": ENTROPIE, "nombre": NOMBRE, "methode": "numpy.random.SeedSequence(...).spawn(NOMBRE)"},
        "temoins": temoins}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
