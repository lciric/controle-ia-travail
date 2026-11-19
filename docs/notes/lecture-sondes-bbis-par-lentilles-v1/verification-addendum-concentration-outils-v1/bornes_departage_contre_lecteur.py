"""Contre-lecteur Opus 5.5 : les bornes de la garde d'égalité (EC-6, (ii)) sur des jouets, par énumération de tous les départages.
Jouets : T jetons, liste des k premiers (k = 5 au lieu de 20 pour que l'énumération reste petite), M directions nulles, scores
arrondis grossièrement pour créer des égalités au k-ième rang ; statistique S = part des k premiers au-dessus d'un seuil par jeton
(le rôle du quantile 0,99) ou compte d'une « famille » (masque fixe de jetons). La direction lue v est sans égalité au k-ième rang.
Pour chaque jouet : toutes les combinaisons de départage des nulles marquées sont énumérées ; on vérifie que (a) les bornes de
l'addendum (p_bas sans les marquées ; p_haut = p_bas + nombre de marquées / (M + 1)) encadrent toutes les valeurs p ; (b) les bornes
exactes (S_min, S_max de chaque marquée) sont atteintes ; et l'on compte les cas où les bornes de l'addendum franchissent un seuil
de libellé alors qu'aucun départage ne le franchit (arrêt sans objet). Graine : numpy.random.default_rng(ENTROPIE).
Usage : python -B bornes_departage_contre_lecteur.py ENTROPIE"""
import itertools
import sys

import numpy as np

g = np.random.default_rng(int(sys.argv[1]))
T, k, M = 14, 5, 9
SEUILS = (0.1, 0.2, 0.5)          # seuils de libellé sur p, jouets (p prend les valeurs i / (M + 1))


def choix_possibles(s):
    """Tous les ensembles de k premiers compatibles avec un départage des scores s (égalités exactes)."""
    ordre = np.sort(s)[::-1]
    w = ordre[k - 1]
    au_dessus = np.flatnonzero(s > w)
    groupe = np.flatnonzero(s == w)
    r = k - au_dessus.size
    return [np.concatenate([au_dessus, np.array(c, dtype=int)]) for c in itertools.combinations(groupe, r)], ordre[k - 1] == ordre[k]


def stat(ens, s, seuil, masque, sorte):
    return (s[ens] > seuil[ens]).mean() if sorte == "part" else int(masque[ens].sum())


bilan = {"jouets": 0, "encadrement_viole": 0, "exactes_non_atteintes": 0, "arret_sans_objet": 0, "arret_justifie": 0}
while bilan["jouets"] < 4000:
    nuls = np.round(g.standard_normal((M, T)) * 1.5)                     # beaucoup d'égalités
    v = np.round(g.standard_normal(T) * 1.5 + 0.8)
    choix_v, eg_v = choix_possibles(v)
    if eg_v:
        continue                                                         # la direction lue n'a pas d'égalité (sinon : arrêt (i))
    seuil = np.round(g.standard_normal(T) * 1.5 + 1.0)
    masque = g.random(T) < 0.3
    for sorte in ("part", "famille"):
        s_v = stat(choix_v[0], v, seuil, masque, sorte)
        valeurs, marquee = [], []
        for j in range(M):
            ch, eg = choix_possibles(nuls[j])
            valeurs.append(sorted({stat(c, nuls[j], seuil, masque, sorte) for c in ch}))
            marquee.append(eg)
        if not any(marquee):
            continue
        bilan["jouets"] += 1
        fixes = sum(1 for j in range(M) if not marquee[j] and valeurs[j][0] >= s_v)
        n_marq = sum(marquee)
        p_bas_add, p_haut_add = (1 + fixes) / (M + 1), (1 + fixes + n_marq) / (M + 1)
        p_bas_ex = (1 + fixes + sum(1 for j in range(M) if marquee[j] and valeurs[j][0] >= s_v)) / (M + 1)
        p_haut_ex = (1 + fixes + sum(1 for j in range(M) if marquee[j] and valeurs[j][-1] >= s_v)) / (M + 1)
        # toutes les valeurs p atteintes par un départage (chaque marquée choisit une de ses valeurs)
        atteintes = set()
        for combo in itertools.product(*[valeurs[j] for j in range(M) if marquee[j]]):
            atteintes.add((1 + fixes + sum(1 for x in combo if x >= s_v)) / (M + 1))
        if min(atteintes) < p_bas_add - 1e-12 or max(atteintes) > p_haut_add + 1e-12:
            bilan["encadrement_viole"] += 1
        if abs(min(atteintes) - p_bas_ex) > 1e-12 or abs(max(atteintes) - p_haut_ex) > 1e-12:
            bilan["exactes_non_atteintes"] += 1
        franchit_add = any((p_bas_add <= t) != (p_haut_add <= t) for t in SEUILS)
        franchit_ex = any((min(atteintes) <= t) != (max(atteintes) <= t) for t in SEUILS)
        if franchit_add and not franchit_ex:
            bilan["arret_sans_objet"] += 1
        if franchit_ex:
            bilan["arret_justifie"] += 1
print(f"jouets (avec au moins une nulle marquée) : {bilan['jouets']} ; T = {T}, k = {k}, M = {M}, seuils {SEUILS}")
print(f"(a) encadrement par les bornes de l'addendum violé : {bilan['encadrement_viole']}")
print(f"(b) bornes exactes (S_min, S_max) différentes du plus petit ou du plus grand p atteint : {bilan['exactes_non_atteintes']}")
print(f"arrêts justifiés (un départage change le côté d'un seuil) : {bilan['arret_justifie']} ; arrêts sans objet des bornes de "
      f"l'addendum (elles franchissent un seuil, aucun départage ne le franchit) : {bilan['arret_sans_objet']}")
