"""Essai aléatoire des règles (1) et (2) de A5 et du lecteur étendu de A6 sur des textes d'action fabriqués (clés en gras
ou non, puces, occurrences vides, clés répétées, lignes ACTION diverses, fins de ligne CRLF, astérisques isolés). Cherche :
un `DefautDuModule` (qui arrêterait l'addendum entier), une exception autre que `GardeArret`, une position de la règle (2)
qui ne pointe pas sur une clé du coût dans le texte brut."""
import collections
import random
import re

import complements_p3_v1 as cp
from controle_ia.environnements.propositions import lire_action

random.seed(20261020)
CLES = ["ACTION", "TITLE", "PROPOSAL", "CONTROLS", "COST", "PREDICTION", "Cost", "cost"]
GRAS = ["", "*", "**", "***", "_", "__", "*_"]
VALEURS = ["40 hours", "", " ", "**", "1 000 hours", "2 500k", "3 x 400", "about 30", "**40**", "_", "\n", "TBD",
           "1,000", "1 000", "1 000.5"]
PUCES = ["", "", "", "- ", "* ", "1. ", "  "]


def ligne():
    cle = random.choice(CLES)
    g = random.choice(GRAS)
    forme = random.randrange(5)
    v = random.choice(VALEURS)
    p = random.choice(PUCES)
    if cle == "ACTION":
        v = random.choice(["ADD", "REVISE 2", "REVISE", "add", "REVISE #3", ""])
    if forme == 0:
        return f"{p}{g}{cle}:{g[::-1]} {v}"
    if forme == 1:
        return f"{p}{g}{cle}{g[::-1]}: {v}"
    if forme == 2:
        return f"{p}{cle}: {v}"
    if forme == 3:
        return f"{p}{g}{cle}{g[::-1]} breakdown: {v}"
    return f"{p}{g}{cle} :{g[::-1]}{v}"


comptes = collections.Counter()
exemples = {}
for n in range(30000):
    k = random.randint(1, 9)
    lignes = [ligne() for _ in range(k)]
    if random.random() < 0.6:
        lignes.insert(0, "ACTION: ADD")
    sep = "\r\n" if random.random() < 0.1 else "\n"
    texte = sep.join(lignes) + random.choice(["", sep, " **", sep + "**"])
    try:
        r1 = cp.regle_bornes_champs(texte)
        r2 = cp.regle_lire_action(texte)
        rs = cp.regle_de_sensibilite(texte)
        champ = lire_action(texte).champs.get("COST")
        cp.cout_lecteur_etendu(champ)
    except cp.DefautDuModule as e:
        comptes["DefautDuModule"] += 1
        exemples.setdefault("DefautDuModule:" + str(e)[:60], texte)
        continue
    except cp.GardeArret as e:
        comptes["GardeArret"] += 1
        exemples.setdefault("GardeArret:" + str(e)[:60], texte)
        continue
    except Exception as e:                                             # noqa: BLE001
        comptes[type(e).__name__] += 1
        exemples.setdefault(type(e).__name__ + ":" + str(e)[:60], texte)
        continue
    comptes["lus"] += 1
    if r2[0] >= 0 and not re.match(r"cost", texte[r2[0]:r2[0] + 4], re.I):
        comptes["position_regle_2_hors_cle"] += 1
        exemples.setdefault("position_regle_2_hors_cle", texte)
    if cp._divergentes(r1, r2):
        comptes["divergences"] += 1
    if r1[1] == "":
        comptes["regle_1_valeur_vide"] += 1
        exemples.setdefault("regle_1_valeur_vide", texte)
print(dict(comptes))
for k, v in exemples.items():
    print("---", k)
    print(repr(v))
