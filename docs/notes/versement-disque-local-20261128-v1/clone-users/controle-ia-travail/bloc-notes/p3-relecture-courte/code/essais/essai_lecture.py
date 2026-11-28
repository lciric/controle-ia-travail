"""Essais du relecteur sur la lecture de P3 (tables synthétiques du test, aucun fichier du dépôt modifié)."""
import sys
import numpy as np
sys.path.insert(0, "tests")
import test_premier_test_ia_lecture as T
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.gardes import GardeArret

lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 300, 2000
P = T.P

# 1. fuite propre au jeu saboteur contre mention (longueur notée plus courte chez la mention)
src = T._source(0)
t = src["tables"]
t["jetons_notes"] = np.where(t["condition"] == "mention", 5, t["jetons_notes"])
s = lp.lire(src, T._graines())
print("1. non interprétables :", s["issue"]["non_interpretables"])
print("   T3 :", s["intention"][P[0]]["T3"])
print("   ligne :", s["issue"]["ligne"])

# 2. fuite propre au jeu saboteur contre témoin : P3-P4 « conforme » dans la sortie, ligne « non concluant »
src = T._source(0)
t = src["tables"]
t["jetons_notes"] = np.where(t["condition"] == "temoin", 5, t["jetons_notes"])
s = lp.lire(src, T._graines())
print("2. non interprétables :", s["issue"]["non_interpretables"])
print("   P3-P4 :", s["P3-P4"][P[0]], "| ligne :", s["issue"]["ligne"])

# 3. échec de la lecture décisive P3-P3 (saboteur contre honnête) pour les deux sondes
vraie = lp.detection
def detection_en_echec(scores, plancher, condition, tache, a, b, *x, **k):
    if (a, b) == ("saboteur", "honnete"):
        raise GardeArret("jeu saboteur contre honnete : 30 tirages dégénérés sur 300 (simulé)")
    return vraie(scores, plancher, condition, tache, a, b, *x, **k)
lp.detection = detection_en_echec
s = lp.lire(T._source(0), T._graines())
print("3. P3-P3 :", s["P3-P3"][P[0]], "| ligne :", s["issue"]["ligne"], "| réserves :", s["issue"]["reserves"])
lp.detection = vraie
