"""Calculs du plan v4 de la course principale d'auto-conception.

Aucun tirage, aucune entrée : des produits et des sommes de valeurs lues
(plan v3, erratum 1 de la note, registre des GO). Arithmétique décimale exacte,
arrondi au plus proche, demi vers le haut. Écrit sur la sortie standard.
"""
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_CEILING, ROUND_FLOOR


def c(x, pas="0.01"):
    return str(x.quantize(D(pas), rounding=ROUND_HALF_UP))


def plafond_entier(x):
    return x.to_integral_value(rounding=ROUND_CEILING)


def ligne(*champs):
    print(" | ".join(str(v) for v in champs))


TARIFS = [D("0.0733"), D("0.28"), D("1.30")]
MIN_BAS = D("3.25")   # minutes par test à la course v67
MIN_HAUT = D("9")     # minutes par greffon, hypothèse du plan v3
EXPERIMENTATEUR = D("0.081")
LECTEUR_RELEVE = D("0.061")
LECTEUR_PLAFOND = D("0.10")
PLAFOND_ITEM = D("4")

print("# A. Le compte des cartes, borne pour le devis")
exclues, plancher, dessous = 2, 58, 34
total = exclues + plancher + dessous
ligne("2 + 58 + 34", total)
ligne("moins les 2 exclues", total - exclues)
go55 = 5          # identifiants nommés par GO-2026-11-19-55, un par ligne
go56 = 6          # identifiants nommés par GO-2026-11-19-56
go55_lignes_1_et_3 = 2
ligne("identifiants nommés, GO-55", go55)
ligne("identifiants nommés, GO-56", go56)
ligne("identifiants nommés, GO-55 et GO-56", go55 + go56)
ligne("92 moins les porteuses des lignes 1 et 3", total - exclues - go55_lignes_1_et_3)
ligne("92 moins les 11 identifiants nommés", total - exclues - go55 - go56)

print("# B. Appels par greffon")
bas = EXPERIMENTATEUR + LECTEUR_RELEVE
haut = PLAFOND_ITEM + LECTEUR_PLAFOND
ligne("borne basse, exact", bas, "arrondie", c(bas))
ligne("borne haute", c(haut))
ligne("rapport haut sur bas", c(haut / bas, "1"))
ligne("hausse due au lecteur, pour cent", c(LECTEUR_RELEVE / EXPERIMENTATEUR * 100, "1"))

print("# C. Ligne 1, appels : greffons témoins fois la fourchette")
for n in (4, 12):
    ligne(n, "témoins", c(n * bas), c(n * haut))

print("# D. Ligne 2, appels : cartes fois la fourchette")
for n in (94, 92, 90, 81):
    ligne(n, "cartes au plus", c(n * bas), c(n * haut))

print("# E. Machine, hors rejeu du banc joueur")


def heures(n, minutes, fixe):
    brut = D(n) * minutes / 60 + D(fixe)
    return brut, plafond_entier(brut)


cas = [
    ("ligne 1, bas, 4 témoins", heures(4, MIN_BAS, 1)),
    ("ligne 1, haut, 12 témoins", heures(12, MIN_HAUT, 2)),
    ("ligne 1, durée maximale", (D(12), D(12))),
    ("ligne 2, bas, 94 cartes", heures(94, MIN_BAS, 1)),
    ("ligne 2, haut, 94 cartes", heures(94, MIN_HAUT, 10)),
    ("ligne 2, durée maximale", (D(48), D(48))),
    ("ligne 2, bas, 92 cartes", heures(92, MIN_BAS, 1)),
    ("ligne 2, haut, 92 cartes", heures(92, MIN_HAUT, 10)),
]
for nom, (brut, h) in cas:
    ligne(nom, "heures brutes", c(brut), "heures", h, *[c(h * t) for t in TARIFS])

print("# F. Plafonds de machine proposés, tarif horaire jusqu'où ils tiennent")
for plafond, duree in ((5, 12), (15, 48)):
    q = D(plafond) / D(duree)
    ligne(plafond, "USD sur", duree, "heures", "exact", c(q, "0.0001"),
          "arrondi par défaut", str(q.quantize(D("0.01"), rounding=ROUND_FLOOR)))
ligne("somme des deux plafonds", 5 + 15)

print("# G. Barreau 2, par carte, dix générations de bras, étage dans la boucle")
PRIX_ETAGE = [("0,06 un tour sans lecteur", D("0.06")),
              ("0,142 relevé lecteur compris", D("0.142")),
              ("0,60 plafonds par défaut", D("0.60")),
              ("0,90 borne du tour fermé", D("0.90"))]
for nom, gen_bras, tentatives, juges in (
        ("cinq espèces", D("58.64"), 94, D("13.86")),
        ("deux espèces", D("8.92"), 38, D("5.54"))):
    propositions = gen_bras * 10
    ligne(nom, "propositions seules", c(propositions))
    for etiquette, prix in PRIX_ETAGE:
        etage = D(tentatives) * prix * 10
        ligne(nom, etiquette, "étage", c(etage), "carte", c(propositions + etage),
              "carte, à l'unité", c(propositions + etage, "1"))
    ligne(nom, "aiguilleur et deux juges en plus, par carte", c(juges * 10))

print("# H. Calendrier, heures de session")
ligne("code et vérification, v3", "45 à 54", "v4", D(45) + 1, "à", D(54) + 2)
ligne("dont premier emploi, v3", "36,5 à 45,5", "v4", D("36.5") + 1, "à", D("45.5") + 2)
ligne("code jusqu'au premier dollar, v3", "17,25 à 18,25", "v4",
      D("17.25") + 1, "à", D("18.25") + 2)
ligne("le même, C2 compris (2 à 3 heures)", D("18.25") + 2, "à", D("20.25") + 3)
ligne("textes", "23,5 à 59", "avec le supplément", D("23.5") + 6, "à", D(59) + 10)
ligne("somme, v4", D(46) + D("23.5"), "à", D(56) + D(59))
ligne("somme avec le supplément, v4", D(46) + D("29.5"), "à", D(56) + D(69))
