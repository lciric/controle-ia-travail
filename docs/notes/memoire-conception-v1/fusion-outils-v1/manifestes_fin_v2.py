"""Champs fermés des manifestes de fin des courses (D-2 (a)), version 2 (22 novembre 2026).

Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5). Version 2 après contre-lecture de la v1 (C10) :
seuls les champs de la spécification (dates de départ et de fin, code de sortie, présence du produit), typés ; rien
d'autre (ni identifiant, ni commit, ni « décisif », ni configuration, commande, graines, réserves, versions) ; liens
symboliques jamais suivis.
  manifeste-lanceur-fin.json  -> debut_utc, fin_utc (date ISO), code (entier), sortie_existe (booléen)
  manifeste.json              -> cree_le (date ISO)
Une valeur d'un autre type ou d'une autre forme : « non conforme ». Un dossier de course dont le nom est exclu est compté,
non montré ; un fichier à nom exclu est montré « [nom exclu] ».
Usage : python -I manifestes_fin_v2.py [--runs runs] [--depuis AAAAMMJJ]
"""
import argparse
import importlib.util
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("ll2", os.path.join(ICI, "listes_lecture_v2.py"))
ll2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ll2)

RX_DATE = re.compile(r"\d{4}-\d{2}-\d{2}([T ]\d{2}:\d{2}(:\d{2}(\.\d{1,6})?)?)?(Z|[+-]\d{2}:?\d{2})?")


def date(v):
    return v if isinstance(v, str) and RX_DATE.fullmatch(v) else "non conforme"


def entier(v):
    return v if isinstance(v, int) and not isinstance(v, bool) else "non conforme"


def booleen(v):
    return v if isinstance(v, bool) else "non conforme"


CHAMPS = {"manifeste-lanceur-fin.json": {"debut_utc": date, "fin_utc": date, "code": entier, "sortie_existe": booleen},
          "manifeste.json": {"cree_le": date}}


def lire(chemin, champs):
    if os.path.islink(chemin) or not os.path.isfile(chemin):
        return "illisible"
    try:
        d = json.load(open(chemin, encoding="utf-8"))
    except (OSError, ValueError):
        return "illisible"
    if not isinstance(d, dict):
        return "illisible"
    return {k: f(d.get(k)) for k, f in champs.items()}


def releve(runs, depuis=None):
    sortie, caches = [], 0
    for nom in sorted(os.listdir(runs)):
        dossier = os.path.join(runs, nom)
        if os.path.islink(dossier) or not os.path.isdir(dossier) or (depuis and nom[:8] < depuis):
            continue
        if ll2.niveau_boucle(f"runs/{nom}")[0] == "refus":
            caches += 1
            continue
        ligne = {"course": nom, "fichiers": []}
        for f in sorted(os.listdir(dossier)):
            if ll2.niveau_boucle(f"runs/{nom}/{f}")[0] == "refus":
                ligne["fichiers"].append("[nom exclu]")
                continue
            ligne["fichiers"].append(f)
            if f in CHAMPS:
                ligne[f] = lire(os.path.join(dossier, f), CHAMPS[f])
        sortie.append(ligne)
    return sortie, caches


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--runs", default="runs")
    p.add_argument("--depuis", default=None)
    a = p.parse_args(argv)
    sortie, caches = releve(a.runs, a.depuis)
    for l in sortie:
        print(json.dumps(l, ensure_ascii=False))
    print(json.dumps({"courses_montrees": len(sortie), "courses_a_nom_exclu": caches}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
