"""Précision 2 : même cas construit, module v1 (`module/`) et module v2 (copie de base). Part en échec (garde 15 : plus de
1 % de tirages où E0(b) = 0) et part ponctuelle D / E0 hors de [−1 ; 1]. Tables construites à la main, aucune donnée.

Usage : python precision2_v1_v2.py <module v1> <module v2>
"""
import importlib.util
import sys

import numpy as np

import garde_r1_v2b  # noqa: F401


def charger(chemin, nom):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def couts(valeurs):
    a = {f"t{i:02d}": [float(10 ** (1 + v))] for i, v in enumerate(valeurs)}
    b = {f"t{i:02d}": [10.0] for i in range(len(valeurs))}
    return a, b


v1, v2 = charger(sys.argv[1], "av_v1"), charger(sys.argv[2], "av_v2")
d0 = [1.0] * 10 + [-1.0] * 10 + [2.0]                 # E0 = 2/21 ; E0(b) = 0 dans bien plus de 1 % des tirages
dsf = [x - 0.5 for x in d0]                            # D = 0,5 ; part ponctuelle ≈ 5,25
for nom, m in (("v1", v1), ("v2", v2)):
    m.TIRAGES = 10_000
    pf = m.part_des_formes(couts(d0), couts(dsf), np.random.default_rng(0))
    pf = {"etat": m.CALCULE, **pf}
    contrastes = {k: {"fonction": "analyse_contraste", "tirages": 10_000, "niveau": 0.95,
                      "E_sf": {"etat": m.CALCULE, "bas": 0.6, "haut": 0.9}, "part_des_formes": pf}
                  for k in ("saboteur-honnete", "temoin-honnete", "mention-honnete")}
    L = {"decisives": {k: {"etat": None, "entree": {"bas": b, "haut": h}} for k, (b, h) in
                       (("P3-P1", (1.2464, 1.8012)), ("P3-P2", (-0.5704, -0.0650)), ("cout_mention", (-0.5404, -0.1155)))}}
    a = m.audit_symetrie(L, contrastes, {}, ["p1", "p2"])
    print(f"{nom} : part {pf['part']['etat']} ({pf['part'].get('degeneres')} dégénérés), D = {pf['D']['valeur']:.4f}, "
          f"E0 = {pf['E0']['valeur']:.4f} ; déclencheur 3 = {a['part_hors_bornes']['etat']!r} ; "
          f"déclencheur = {a['declencheur']} ; lecture = {a['lecture']!r}")
