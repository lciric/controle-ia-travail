import sys
import time

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mondes as M

g = GR.Graines()
for dose in (0.0, 0.25, 0.5):
    t = time.time()
    s = M.generer_suite(g, dict(couche="essai", famille="dev", source=0), dose)
    print(dose, "s", round(time.time() - t, 2), s.rejets, len(s.source.lois), [len(m.lois) for m in s.mondes_cibles()],
          [sum(l["dependante"] for l in m.lois.values()) for m in s.mondes_cibles()])
