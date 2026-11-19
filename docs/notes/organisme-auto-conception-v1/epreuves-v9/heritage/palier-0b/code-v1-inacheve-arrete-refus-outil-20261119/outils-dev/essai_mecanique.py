"""Outil de développement : une source jouée par la couche mécanique, sous la couche « essai » (aucune sortie versée)."""
import sys
import tempfile
import time

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
from controle_ia.heritage_etage_processeur_v1 import proposeurs as P

g = GR.Graines()
racine = tempfile.mkdtemp(dir=sys.argv[2])
for nom, kw in (("sourd-egal", {}), ("lecteur-heritage", {"K": float(sys.argv[3])})):
    t = time.time()
    ctx = MC.ContexteSource(g, dict(couche="essai", famille="dev", proposeur=nom, source=0), P.configuration(nom, **kw), 0.5,
                            0.25, f"{racine}/{nom}")
    s = MC.jouer_source(ctx)
    print(nom, round(time.time() - t, 1), "s", {b: v["mesure"] for b, v in s["bras"].items()}, s["exclu"],
          len(s["registre_source"].entrees))
    print(MC.frequences_gelees(s["frequences"].comptes()), s["frequences"].comptes()["criblage"])
