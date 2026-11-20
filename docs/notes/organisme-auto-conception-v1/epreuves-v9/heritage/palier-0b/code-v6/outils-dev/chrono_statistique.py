"""Outil de développement : temps de la couche statistique (2 000 sources, six bras-jumelles) sous la couche « essai », et
taille réduite à quelques réglages (aucune valeur p, aucun taux). Aucune sortie versée."""
import sys
import time

sys.path.insert(0, sys.argv[1])
sys.path.insert(0, sys.argv[2])
from aides_heritage_etage_processeur_v1 import FREQUENCES_D_ESSAI
from controle_ia.heritage_etage_processeur_v1 import etalonnage as ET
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import proposeurs as P

g = GR.Graines()
for nom, reglage, valeurs, dose in (("lecteur-tenue", "tau", (0.5, 1.0, 2.0), 0.25), ("lecteur-heritage", "K", (16, 64, 256), 0.5)):
    for x in valeurs:
        t = time.time()
        moy, sd = ET.jumelles(g, "essai", dict(famille="chrono", proposeur=nom, dose=dose), P.configuration(nom, **{reglage: x}),
                              dose, 0.25, FREQUENCES_D_ESSAI, 10000, ("1", "2", "3"))
        e, taille, s = ET.taille(moy, sd, ET.CONTRASTE_DU_REGLAGE[reglage])
        print(nom, reglage, x, "taille", round(taille, 3), "écart", round(e, 3), "sd", round(s, 3), round(time.time() - t, 2), "s")
