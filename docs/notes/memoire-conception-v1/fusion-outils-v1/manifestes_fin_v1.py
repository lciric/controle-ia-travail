"""Champs fermés des manifestes de fin des courses, pour la liste du faux échec (D-2 (a)), version 1 (22 novembre 2026).

Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5). Aucun agent ne lit un manifeste : ce programme en
tire une liste fermée de champs et les noms des fichiers présents (filtrés par les exclusions de nom), seule sortie remise
au cycle. Ni configuration, ni commande, ni graines, ni réserves, ni versions, ni aucun contenu de résultat.
  manifeste.json              -> run_id, cree_le, decisif, depot_propre, commit
  manifeste-lanceur-fin.json  -> id, debut_utc, fin_utc, code, sortie_existe
Un dossier de course dont le nom est exclu est compté, non montré. Un manifeste illisible : « illisible ».
Usage : python -I manifestes_fin_v1.py [--runs runs] [--depuis AAAAMMJJ]
"""
import argparse
import importlib.util
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("ll1", os.path.join(ICI, "listes_lecture_v1.py"))
ll1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ll1)

CHAMPS = {"manifeste.json": ("run_id", "cree_le", "decisif", "depot_propre", "commit"),
          "manifeste-lanceur-fin.json": ("id", "debut_utc", "fin_utc", "code", "sortie_existe")}
SCALAIRES = (str, int, float, bool, type(None))


def lire(chemin, champs):
    try:
        d = json.load(open(chemin, encoding="utf-8"))
    except (OSError, ValueError):
        return "illisible"
    if not isinstance(d, dict):
        return "illisible"
    return {k: (d.get(k) if isinstance(d.get(k), SCALAIRES) else "non scalaire") for k in champs}


def releve(runs, depuis=None):
    sortie, caches = [], 0
    for nom in sorted(os.listdir(runs)):
        dossier = os.path.join(runs, nom)
        if not os.path.isdir(dossier) or (depuis and nom[:8] < depuis):
            continue
        if ll1.niveau_boucle(f"runs/{nom}")[0] == "refus":
            caches += 1
            continue
        ligne = {"course": nom, "fichiers": []}
        for f in sorted(os.listdir(dossier)):
            if ll1.niveau_boucle(f"runs/{nom}/{f}")[0] == "refus":
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
