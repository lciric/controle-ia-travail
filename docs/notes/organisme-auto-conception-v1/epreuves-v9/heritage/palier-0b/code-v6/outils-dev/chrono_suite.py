"""Outil de développement : génère une suite de mondes sous la couche « essai » et en mesure le temps (aucune sortie versée)."""
import sys
import time

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mondes as MO

g = GR.Graines()
for dose in (0.0, 0.5):
    t = time.time()
    s = MO.generer_suite(g, dict(couche="essai", famille="chrono", source=0), dose)
    print("dose", dose, round(time.time() - t, 2), "s", s.compteurs.vers_dict())
