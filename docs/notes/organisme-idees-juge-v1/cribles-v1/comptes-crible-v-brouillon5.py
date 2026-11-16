"""Brouillon 5 du crible (v) : budget de durée au pire, à titre d'illustration (annexe A, point 12).

Refait par programme les chiffres de durée que le rapport du tour 4 de contre-lecture donne dans sa réponse (4)
(« à refaire par programme et à recopier en annexe »), avec les durées que ce rapport SUPPOSE (aucune n'est mesurée,
aucune ne vient du pilote) : mise en place 0,5 h ; barrières 100 minutes (phrase 60, deux feux de 20, [PROC-14] § 0),
ou 160 minutes (avec 60 minutes de mondes lents) en variante ; génération 1,0 h à 20 mondes, 1,2 h à 24, comptée trois
fois ; mesure 1 h ; rapatriement 0,5 h ; appels ceil(N/M) x B_a ; minuterie 17 h.
La table qui fera foi suit la règle écrite de la section « Devis » (« Durée ») sur les durées mesurées au pilote ; celle-ci
n'en est qu'une illustration.
Arithmétique entière, en secondes ; bibliothèque standard seule ; aucune donnée, aucun tirage, aucun appel.
Usage : python3 -I comptes-crible-v-brouillon5.py
"""

MINUTERIE = 17 * 3600
MISE_EN_PLACE = 1800
MESURE = 3600
RAPATRIEMENT = 1800
GENERATION = {20: 3 * 3600, 24: 3 * 4320}          # 1,0 h et 1,2 h, comptées trois fois
BARRIERES = {"100 min": 6000, "160 min": 9600}
GRILLE_BA = (1800, 2400, 3000, 3600)


def fixe(n, barrieres):
    return MISE_EN_PLACE + barrieres + GENERATION[n] + MESURE + RAPATRIEMENT


def tranches(n, m):
    return -(-n // m)


def heures(s):
    return f"{s / 3600:.2f} h"


print("1. Plus grande B_a (s, entière) pour laquelle le budget de pire cas tient sous 17 h")
for nom, b in BARRIERES.items():
    for n in (20, 24):
        for m in (1, 2):
            reste = MINUTERIE - fixe(n, b)
            ba = reste // tranches(n, m)
            ba300 = (ba // 300) * 300
            print(f"  barrières {nom}, N = {n}, M = {m} : termes fixes {fixe(n, b)} s ; B_a max {ba} s ;"
                  f" plus grand multiple de 300 s : {ba300} s")

print("2. Grille de B_a, M retenu = plus petit M de 1 à 2 qui tient sous 17 h, sinon « non lançable »")
for nom, b in BARRIERES.items():
    for n in (20, 24):
        for ba in GRILLE_BA:
            budgets = {m: fixe(n, b) + tranches(n, m) * ba for m in (1, 2)}
            tient = [m for m in (1, 2) if budgets[m] <= MINUTERIE]
            verdict = f"M = {tient[0]}" if tient else "non lançable"
            print(f"  barrières {nom}, N = {n}, B_a = {ba} s : M = 1 {heures(budgets[1])} ;"
                  f" M = 2 {heures(budgets[2])} ; {verdict}")
