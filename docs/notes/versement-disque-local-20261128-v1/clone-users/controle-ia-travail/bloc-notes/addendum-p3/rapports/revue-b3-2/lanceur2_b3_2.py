"""Second lanceur (ordre inverse) : ne prend un mutant que si son dossier n'existe pas encore (réservation par
os.makedirs sans exist_ok) ; même procédure que `mutants_b3_2.lancer_un` (suite entière, -x)."""
import os
import sys
from concurrent.futures import ThreadPoolExecutor

import mutants_b3_2 as mb

ids = sys.argv[1:]


def un(ident):
    d = os.path.join(mb.ICI, "mutants", ident)
    try:
        os.makedirs(d)
    except FileExistsError:
        return None
    return mb.lancer_un(ident)


with ThreadPoolExecutor(int(os.environ.get("PARALLELE", "1"))) as ex:
    for res in ex.map(un, ids):
        if res:
            print(f"{res['etat']:7s} {res['id']:4s} {res['mutant']} — {res['resume']} ({res['duree_s']} s)", flush=True)
