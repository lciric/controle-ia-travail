"""Greffon de pytest de la campagne de mutations des essais d'admission du bras A — version 6.

Repris de l'outil de la livraison 5 (bloc-notes de session, `mut/greffe_mutant.py`), versé au dépôt à la livraison 6 ; version 2 à la livraison 7, version 3 à la livraison 8, version 4 à la livraison 9, version 5 à la livraison 10, version 6 à la livraison 11, sans autre changement que le nom.
Remplace, en mémoire et dans le seul processus d'essai, une fonction d'un module chargé par les essais (`chef` ou
`relais_google`) par son mutant, lu dans le fichier que nomme la variable `MUTANT`. Aucun fichier du dépôt n'est
modifié. Sans `MUTANT`, il ne fait rien."""
import json
import os


def pytest_collection_modifyitems(session, config, items):
    chemin = os.environ.get("MUTANT")
    if not chemin or not items:
        return
    with open(chemin, encoding="utf-8") as f:
        m = json.load(f)
    module = getattr(items[0].module, m["objet"])          # `chef` ou `relais_google`, tels que les essais les chargent
    espace = {}
    exec(compile(m["source"], f"<mutant {m['nom']}>", "exec"), module.__dict__, espace)
    setattr(module, m["fonction"], espace[m["fonction"]])
