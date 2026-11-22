"""Porte de périmètre de l'organe « mémoire du dépôt » (étape 4 de l'avis de fusion), version 1 (22 novembre 2026).

Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5). Juge, après coup, le journal de l'outil borné
(recherche_bornee_v5.py) sur une journée de cycles ou de réponses : chaque ligne doit être bien formée, porter le bras
attendu pour son agent, citer un commit ancêtre de la branche principale, et un chemin ouvrable pour ce bras selon
listes_lecture_v3.py. Les rôles sont donnés par un fichier JSON {agent: bras} écrit par la mère ; un agent absent du
fichier est un manquement (on ne présume aucun bras). La porte TIENT s'il n'y a aucun manquement, sinon elle TOMBE.
Limite déclarée : la porte ne voit que les lectures passées par l'outil ; une lecture hors outil ne laisse pas de ligne.
Sortie : un rapport JSON (création exclusive, R12) : verdict, comptes, et pour chaque manquement le numéro de ligne, l'agent,
le motif et le chemin (noms seuls, jamais de contenu).
Usage : python -I porte_perimetre_v1.py JOURNAL.jsonl ROLES.json RAPPORT.json [--depot .]
Codes : 0 la porte tient ; 3 elle tombe ; 1 arrêt (arguments, rapport existant, rôles illisibles).
"""
import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("ll3", os.path.join(ICI, "listes_lecture_v3.py"))
ll3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ll3)

REFS_PRINCIPALES = ("origin/main", "main")
ACTIONS = ("chercher", "lire")
BRAS = ("memo", "base", "boucle")


def ancetre(depot, commit, cache):
    if commit not in cache:
        ok = False
        for r in REFS_PRINCIPALES:
            if subprocess.run(["git", "-C", depot, "rev-parse", "--verify", "--quiet", r], capture_output=True).returncode == 0:
                ok = subprocess.run(["git", "-C", depot, "merge-base", "--is-ancestor", commit, r],
                                    capture_output=True).returncode == 0
                break
        cache[commit] = ok
    return cache[commit]


def juger(lignes, roles, depot):
    manquements, cache, n = [], {}, 0
    for i, brut in enumerate(lignes, start=1):
        if not brut.strip():
            continue
        n += 1
        try:
            e = json.loads(brut)
        except ValueError:
            manquements.append({"ligne": i, "agent": None, "motif": "ligne illisible", "chemin": None})
            continue
        if not isinstance(e, dict):
            manquements.append({"ligne": i, "agent": None, "motif": "ligne mal formée", "chemin": None})
            continue
        agent, bras, chemin, commit, action = (e.get(k) for k in ("agent", "bras", "chemin", "commit", "action"))
        chemin_s = chemin if isinstance(chemin, str) else None
        def manque(motif):
            manquements.append({"ligne": i, "agent": agent if isinstance(agent, str) else None, "motif": motif,
                                "chemin": chemin_s})
        if not isinstance(agent, str) or not isinstance(chemin, str) or action not in ACTIONS or bras not in BRAS:
            manque("champs manquants ou hors liste")
            continue
        if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit):
            manque("commit mal formé")
            continue
        attendu = roles.get(agent)
        if attendu is None:
            manque("agent absent du fichier des rôles")
            continue
        if bras != attendu:
            manque(f"bras {bras} au lieu de {attendu}")
            continue
        if not ancetre(depot, commit, cache):
            manque("commit hors de la branche principale")
            continue
        ouvrable, _, motif = ll3.autorise_bras(chemin, bras)
        if not ouvrable:
            manque(f"fichier non ouvrable pour le bras {bras} : {motif or 'noms seuls'}")
    return {"verdict": "tient" if not manquements else "tombe", "lignes": n, "manquements": len(manquements),
            "detail": manquements}


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("journal")
    p.add_argument("roles")
    p.add_argument("rapport")
    p.add_argument("--depot", default=".")
    a = p.parse_args(argv)
    if os.path.lexists(a.rapport):
        print(f"ARRET : {a.rapport} existe déjà (R12)", file=sys.stderr)
        return 1
    try:
        roles = json.load(open(a.roles, encoding="utf-8"))
        assert isinstance(roles, dict) and all(isinstance(k, str) and v in BRAS for k, v in roles.items())
    except (OSError, ValueError, AssertionError):
        print("ARRET : fichier des rôles illisible ({agent: memo|base|boucle} attendu)", file=sys.stderr)
        return 1
    lignes = open(a.journal, encoding="utf-8").read().split("\n") if os.path.exists(a.journal) else []
    r = juger(lignes, roles, a.depot)
    with open(a.rapport, "x", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: r[k] for k in ("verdict", "lignes", "manquements")}, ensure_ascii=False))
    return 0 if r["verdict"] == "tient" else 3


if __name__ == "__main__":
    sys.exit(main())
