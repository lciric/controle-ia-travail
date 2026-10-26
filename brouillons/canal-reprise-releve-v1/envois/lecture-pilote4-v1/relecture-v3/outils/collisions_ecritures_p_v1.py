#!/usr/bin/env python3
"""Relecture de la v3 : la garde de séparation cherche les valeurs p de l'autre course sous l'écriture du script à six
chiffres significatifs (`fr_p`). Deux valeurs p différentes qui ont la même écriture feraient refuser une lecture saine
(fausse alerte déclarée « possible en théorie », LISEZMOI v3 § 3.2). Ce calcul énumère toutes les valeurs p que le
script peut rendre (McNemar exact, b + c paires discordantes au plus 36 en conscience, 24 en délégation) et cherche
celles qui partagent une écriture. Fonctions du script chargées depuis la copie (aucune exécution de ses modes).

Usage : python -I collisions_ecritures_p_v1.py SCRIPT_V3
"""
import sys

sys.dont_write_bytecode = True

import importlib.util  # noqa: E402
from collections import defaultdict  # noqa: E402

spec = importlib.util.spec_from_file_location("lire_sous_relecture", sys.argv[1])
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)

for borne, famille in ((36, "conscience (36 paires)"), (24, "délégation (24 paires)"), (60, "les deux familles ensemble")):
    par_ecriture = defaultdict(set)
    for n in range(0, 37 if borne == 60 else borne + 1):
        for b in range(0, n + 1):
            p = L.mcnemar_exact(b, n - b)
            par_ecriture[L.fr_p(p)].add(p)
    valeurs = {p for s in par_ecriture.values() for p in s}
    collisions = {e: sorted(s) for e, s in par_ecriture.items() if len(s) > 1}
    print(f"{famille} : {len(valeurs)} valeurs p distinctes, {len(par_ecriture)} écritures à six chiffres ; "
          f"écritures partagées par deux valeurs ou plus : {len(collisions)}")
    for e, s in sorted(collisions.items(), key=lambda x: float(x[1][0]))[:20]:
        print(f"   {e} : " + ", ".join(f"{p.numerator}/{p.denominator}" for p in s))
    # même question pour l'écriture JSON (repr du flottant) et la fraction : aucune collision possible si distinctes
    rep = defaultdict(set)
    for p in valeurs:
        rep[repr(float(p))].add(p)
    print(f"   écriture JSON partagée : {sum(1 for s in rep.values() if len(s) > 1)}")
