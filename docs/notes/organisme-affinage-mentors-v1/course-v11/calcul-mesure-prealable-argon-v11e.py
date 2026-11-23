#!/usr/bin/env python3
"""Chiffres de la mesure préalable de la réflexion d'Argon (devis v11e, § 4 ; brouillon 6 du préenregistrement v11).

Mesure fixée par la session de l'organisme le 23 novembre 2026 (message daté 05:45Z) : quatre appels de juge et un appel
de proposeur d'Argon, aux arguments exacts du gabarit de la course (niveau `high`, provision 24 576, sortie maximale 45 056,
en flux, prix 4 et 20 USD par million de jetons) ; un statut 429 ou de 500 et plus se rejoue au plus deux fois par appel,
dans la limite de la ligne GO-2026-11-22-128 (au plus 10,50 USD) ; seuil de la règle de lecture : 31 462 jetons de
réflexion moyenne par appel d'Argon, pondérée comme dans la course (programme du devis v11c,
`calcul-devis-course-affinage-mentors-v11c.py`, `bb52afbcc24cffa591c1ef42473ebd2a9aba9fc5aeb9bc4bf992bdd91e968e5f`, qui
calcule ce seuil et que ce programme ne remplace pas).
Pire cas d'un appel, tel que la commande en flux v2 le compte (`scripts/commande_gemini_flux_v2.py`, `13b968eb…`,
docstring) : entrée gardée × prix d'entrée + `maxOutputTokens` × prix de sortie, la réflexion comprise dans la sortie
maximale ; « coût rendu sur un échec : 1e-6 si rien n'est parti ; pire cas dès que la requête de génération est partie,
sauf usage lu » : une reprise après un échec de la génération est donc comptée, au pire, à son pire cas.
Écrit par Opus 5.5 en effort maximal (GO-2026-11-22-145 ; écart à R-3735 et à GO-2026-11-21-75 déclaré au devis v11e).

Aucun appel, aucun réseau, aucune lecture de fichier : toutes les entrées sont écrites ici, avec leur source.
Usage : python3 -I calcul-mesure-prealable-argon-v11e.py
Sortie : une ligne par chiffre ; code 0 si tous les contrôles passent. Arithmétique exacte (fractions) ; arrondis à
l'affichage seulement, au plus proche.
"""
from fractions import Fraction as F
import json
import math
import sys

M = 10 ** 6

# --- Entrées, avec leur source (les mêmes que le programme du devis v11c) ------------------------------------------
PRIX_ENTREE, PRIX_SORTIE = F(4), F(20)        # prix déclarés d'Argon, R-5018
ARGON_SORTIE = 45056                          # sortie maximale d'Argon, en flux (gabarit de déclaration v11c)
ENTREE_PROPOSEUR_LA_PLUS_LONGUE = 2618        # jetons gardés : fil le plus long (devis v10, § 1 ; rapport du lanceur v11)
CONSIGNE_JUGE_CARACTERES = 1514               # consigne du juge, a32583b1… : 1 514 caractères
CONSIGNE_JUGE_SANS_FIN = 1513                 # sans le saut de ligne final (entrée bâtie par les lanceurs v11c et v11d)
CARTE_CARACTERES_MAX = 9000                   # consigne du proposeur, l. 20
CADRE_LANCEUR = 1000                          # cadre supposé par les lanceurs v11b à v11d
MARGE_ENTREE = F("0.05")                      # commande en flux : entrée gardée = ⌈caractères / 3 × 1,05⌉ (au moins)
LIGNE_GO_128 = F("10.50")                     # GO-2026-11-22-128 : au plus 10,50 USD, clé de Google, hors du plafond
APPELS_JUGE, APPELS_PROPOSEUR = 4, 1          # décision de la session de l'organisme, 05:45Z
REPRISES_PAR_APPEL = 2                        # même décision : 429 et 5xx rejoués au plus deux fois par appel
POIDS_PROPOSEUR, POIDS_JUGE = 16, 160         # appels d'Argon dans la course : 16 de proposeur, 160 de juge

controles = []


def usd(x, n=2):
    """Arrondi au plus proche à n décimales, écrit à la française (virgule)."""
    q = 10 ** n
    v = math.floor(x * q + F(1, 2))
    entier, frac = divmod(v, q)
    return str(entier) if n == 0 else f"{entier},{str(frac).rjust(n, '0')}"


def dire(nom, valeur, attendu):
    print(f"{nom} : {valeur}")
    controles.append((nom, str(valeur), attendu))


def jetons_gardes(caracteres):
    return math.ceil(F(caracteres, 3) * (1 + MARGE_ENTREE))


def cout(entree, sortie):
    return (entree * PRIX_ENTREE + sortie * PRIX_SORTIE) / M


def entree_juge_v11c():
    """Entrée de juge la plus longue que bâtissent les lanceurs v11c et v11d (forme de l'orchestrateur épinglé), en
    caractères ; même fonction que le programme du devis v11c."""
    fiche = {"identifiant": "F" + "x" * 5, "carte": "é" * CARTE_CARACTERES_MAX, "cadre": "é" * CADRE_LANCEUR}
    corps = json.dumps(fiche, ensure_ascii=False, indent=1)
    return CONSIGNE_JUGE_SANS_FIN + len("\n\n## La fiche\n```json\n") + len(corps) + len("\n```\n")


e_juge_v11c = jetons_gardes(entree_juge_v11c())
e_juge_v11b = jetons_gardes(CONSIGNE_JUGE_CARACTERES + CARTE_CARACTERES_MAX + CADRE_LANCEUR)
pj_v11c, pj_v11b = cout(e_juge_v11c, ARGON_SORTIE), cout(e_juge_v11b, ARGON_SORTIE)
pp = cout(ENTREE_PROPOSEUR_LA_PLUS_LONGUE, ARGON_SORTIE)

print("=== Mesure préalable de la réflexion d'Argon : pires cas comptés par la commande en flux v2 ===")
dire("entrée gardée de juge la plus longue, lanceurs v11c et v11d (jetons)", e_juge_v11c, "4059")
dire("entrée gardée de juge, lanceur v11b (jetons)", e_juge_v11b, "4030")
dire("pire cas d'un appel de juge, entrée des lanceurs v11c et v11d (USD)", usd(pj_v11c, 6), "0,917356")
dire("pire cas d'un appel de juge, entrée du lanceur v11b (USD)", usd(pj_v11b, 6), "0,917240")
dire("pire cas d'un appel de proposeur (USD)", usd(pp, 6), "0,911592")
base = APPELS_JUGE * pj_v11c + APPELS_PROPOSEUR * pp
base_v11b = APPELS_JUGE * pj_v11b + APPELS_PROPOSEUR * pp
dire("appels de la mesure", APPELS_JUGE + APPELS_PROPOSEUR, "5")
dire("pire cas de la mesure sans reprise (USD, exact)", usd(base, 6), "4,581016")
dire("pire cas de la mesure sans reprise (USD)", usd(base, 2), "4,58")
dire("le même, entrée de juge du lanceur v11b (USD, exact)", usd(base_v11b, 6), "4,580552")
dire("part de la ligne GO-2026-11-22-128 prise par ce pire cas (%)", usd(100 * base / LIGNE_GO_128, 0), "44")
envois_max = (1 + REPRISES_PAR_APPEL) * (APPELS_JUGE + APPELS_PROPOSEUR)
toutes_reprises = (1 + REPRISES_PAR_APPEL) * base
dire("envois au plus, chaque appel repris deux fois", envois_max, "15")
dire("pire cas compté, chaque appel repris deux fois et chaque envoi compté à son pire cas (USD)", usd(toutes_reprises, 2), "13,74")
dire("ce pire cas passe la ligne de 10,50 USD", "oui" if toutes_reprises > LIGNE_GO_128 else "non", "oui")
reste = LIGNE_GO_128 - base
dire("reste de la ligne après les cinq appels comptés à leur pire cas (USD)", usd(reste, 2), "5,92")
reprises_dans_la_ligne = math.floor(reste / max(pj_v11c, pp))
dire("reprises comptées à leur pire cas qui tiennent ensuite dans la ligne", reprises_dans_la_ligne, "6")
envois_dans_la_ligne = math.floor(LIGNE_GO_128 / min(pj_v11c, pp))
assert (envois_dans_la_ligne - 1) * pj_v11c + pp <= LIGNE_GO_128 < envois_dans_la_ligne * pj_v11c + pp
dire("envois au plus dans la ligne, chacun compté à son pire cas", envois_dans_la_ligne, "11")
# Moyenne pondérée comme dans la course : (16 × réflexion du proposeur + 160 × moyenne des juges) / 176
somme = POIDS_PROPOSEUR + POIDS_JUGE
dire("appels d'Argon dans la course (poids de la moyenne)", somme, "176")
dire("poids du proposeur dans la moyenne pondérée", F(POIDS_PROPOSEUR, somme), "1/11")
dire("poids du juge dans la moyenne pondérée", F(POIDS_JUGE, somme), "10/11")

ecarts = [(n, v, a) for (n, v, a) in controles if v != a]
print(f"\n{len(controles)} chiffres contrôlés, {len(ecarts)} écart(s)")
for n, v, a in ecarts:
    print(f"ÉCART : {n} : calculé {v}, attendu {a}")
sys.exit(1 if ecarts else 0)
