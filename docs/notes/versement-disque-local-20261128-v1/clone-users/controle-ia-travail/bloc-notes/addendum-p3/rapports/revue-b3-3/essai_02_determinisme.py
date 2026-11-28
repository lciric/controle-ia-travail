"""Essai 02 : déterminisme entre processus. Même scénario, deux processus séparés, PYTHONHASHSEED différent (ordre des
ensembles de chaînes) : la sortie de `analyser_addendum` doit être la même, octet pour octet (sérialisation canonique).
Usage : python essai_02_determinisme.py <scénario> ; imprime l'empreinte de la sortie et quelques comptes."""
import os
import sys
import time

import commun  # noqa: F401
from commun import cp, empreinte_sortie, tc

nom = sys.argv[1]
t0 = time.time()
src = tc.SCENARIOS[nom]()
lec = tc._lecture(src)
s = cp.analyser_addendum(src, lec, tc.G)
print(f"{nom} PYTHONHASHSEED={os.environ.get('PYTHONHASHSEED')} empreinte={empreinte_sortie(s)} "
      f"controles={s['nombre_de_controles']['total']} reserves={s['nombre_de_reserves']} "
      f"etablies={len(s['conclusions_etablies'])} duree={time.time() - t0:.1f}s")
