#!/usr/bin/env python3
"""Appelle `controle_ia.prereg.problemes` sur chaque fichier donné — v1.

Le module `controle_ia.prereg` n'a pas de ligne de commande (son `--help` ne rend rien) : ce script,
appelé par son chemin avec `PYTHONPATH=src`, ne fait que lire le fichier et imprimer la liste des problèmes.
Il n'écrit rien et ne scelle rien. Code de sortie : 0 si aucune liste n'a de problème, 1 sinon.
"""
import sys

from controle_ia.prereg import problemes


def main(argv):
    if not argv:
        print("usage : valider_prereg_v1.py FICHIER…", file=sys.stderr)
        return 2
    code = 0
    for chemin in argv:
        p = problemes(chemin)
        if p:
            code = 1
            print(f"NON CONFORME : {chemin}")
            for ligne in p:
                print(f"  - {ligne}")
        else:
            print(f"CONFORME (aucun problème) : {chemin}")
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
