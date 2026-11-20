"""Outil de développement : une source jouée par la couche mécanique, sous la couche « essai » (aucune sortie versée).
Arguments : chemin de src, dossier de travail neuf, nom du proposeur, dose."""
import os
import sys
import time

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import frequences as FR
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
from controle_ia.heritage_etage_processeur_v1 import proposeurs as P
from controle_ia.heritage_etage_processeur_v1.constantes import REGLAGES_ETAPE_4

g = GR.Graines()
nom, dose = sys.argv[3], float(sys.argv[4])
prop = P.configuration(nom, **REGLAGES_ETAPE_4)
t = time.time()
ctx = MC.ContexteSource(g, dict(couche="essai", famille="dev", proposeur=nom, dose=dose, source=0), prop, dose, 0.25,
                        os.path.join(sys.argv[2], nom))
s = MC.jouer_source(ctx)
print(nom, round(time.time() - t, 1), "s", {b: v["mesure"] for b, v in s["bras"].items()}, "exclu", s["exclu"],
      "entrées source", len(s["registre_source"].entrees), "servies", {b: v["entrees_servies"] for b, v in s["bras"].items()})
c = s["frequences"].comptes()
print(FR.frequences_gelees(c))
print({k: v for k, v in c.items() if k not in ("criblage",)}, c["criblage"])
