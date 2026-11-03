#!/usr/bin/env python3
"""Recherche des clés dans les sorties d'un run de la mini-course (GO-2026-11-01-12) — version 1 (CLM-06).

Rédigé le 1er novembre 2026 (sous-agent de session-depot). Remplace la boucle `grep -rqF -- "${!v}"` du lanceur v1, qui passait
la valeur de la clé en argument (visible dans `/proc/<pid>/cmdline` par tous). Ici, les **noms** des variables sont en
argument ; les **valeurs** sont lues dans l'environnement du processus (lancé sous `env -i` avec ces seules variables) ; seuls
les noms trouvés sont imprimés, jamais une valeur.

  env -i K1="…" K2="…" python3 -I -B chercher_cles_v1.py DOSSIER K1 K2
Codes : 0 aucune clé trouvée ; 6 au moins une clé trouvée (noms sur la sortie d'erreur) ; 2 usage (variable absente ou trop
courte, dossier absent : aucun repli silencieux).
"""

import os
import sys


def chercher(dossier, valeurs):
    trouvees = set()
    for racine, _, fichiers in os.walk(dossier):
        for nom in fichiers:
            chemin = os.path.join(racine, nom)
            if os.path.islink(chemin) or not os.path.isfile(chemin):
                continue
            with open(chemin, "rb") as f:
                octets = f.read()
            trouvees |= {n for n, v in valeurs.items() if v in octets}
    return sorted(trouvees)


def principal(argv, environ):
    if len(argv) < 2 or not os.path.isdir(argv[0]):
        print("usage : chercher_cles_v1.py DOSSIER NOM [NOM…] (dossier existant)", file=sys.stderr)
        return 2
    valeurs = {}
    for n in argv[1:]:
        v = environ.get(n) or ""
        if len(v) < 8:
            print(f"variable {n} absente ou trop courte : recherche impossible", file=sys.stderr)
            return 2
        valeurs[n] = v.encode("utf-8")
    trouvees = chercher(argv[0], valeurs)
    if trouvees:
        print("ALERTE : clé trouvée dans une sortie : " + ", ".join(trouvees), file=sys.stderr)
        return 6
    print(f"aucune clé trouvée ({len(valeurs)} variable(s) cherchée(s))")
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:], os.environ))
