"""Course simulée du lot 6 v4 (trois générations, faux fournisseur, aucun appel) : registre des tentatives, constats du
coffre, comptes écrits avec leur compagnon.

    python -B demonstrations/lancer_course_simulee_na_v4.py --sortie DOSSIER_VIDE [--racine 20261122]
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pole import course_na_v4 as c4  # noqa: E402
from pole import simulation_na_v4 as sm  # noqa: E402


def principal(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--sortie", required=True)
    p.add_argument("--racine", type=int, default=20261122)
    a = p.parse_args(argv)
    if os.listdir(a.sortie):
        raise SystemExit("le dossier de sortie doit être vide (on n'écrase jamais)")
    registre, constats, comptes = sm.course_simulee(a.sortie, racine=a.racine)
    registre.sceller()
    c4.ecrire_comptes(a.sortie, comptes)
    print(json.dumps({"lignes": len(registre.lignes()), "coffre": [[k.generation, k.au_coffre, k.rendues,
                      k.dont_repli_rendues, k.depasse] for k in constats]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
