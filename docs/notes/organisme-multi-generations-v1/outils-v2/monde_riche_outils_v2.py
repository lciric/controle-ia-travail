"""Outils v2 de la conception « monde riche et doublons » : regroupement stratifié à distances dirigées gardées, règle de
représentant qui ne peut pas choisir un membre affaibli (correction E-1 de la contre-lecture `e7d5cda0…`), parcours
déterministes (E-2). N'écrase rien de la v1 : importe `../outils-v1/` tel quel (scellé).

Concepteur (Claude Opus 5.5), 12 novembre 2026. Aucun appel, aucun réseau.

Règle du représentant v2 (avant tout tirage du juge) :
1. **couverture dirigée** : pour chaque membre r, c(r) = max sur les autres membres j de d_nul(j → r) (ce que j rapporterait
   au-delà du nul v8 engendré par r si j était le monde) ; candidats = membres de c(r) ≤ min c + 10⁻³. Une version diluée ou
   tempérée d'une loi est dans le nul de cette loi (c = 0 pour la loi forte), l'inverse est faux : la loi forte est préférée.
2. **égalité** (membres qui se couvrent mutuellement, par exemple deux températures d'une même loi) : départagée par une
   **tranche de choix** de 400 épisodes **frais, distincts des tirages du juge et de la tranche du test de mort**, statistique
   gelée du test de mort calculée par l'orchestrateur ; puis par l'empreinte canonique.
3. **sort du groupe** : le représentant seul est testé ; s'il meurt, le groupe est éliminé et ses sœurs sont réinjectées
   **après la course** (mesure, S-2) : une sœur qui y survit et y est promue est rapportée comme groupe mal formé.
La valeur e du groupe reste la moyenne des valeurs e de ses membres (indépendante du choix du représentant).
"""

import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
V1 = os.path.join(os.path.dirname(ICI), "outils-v1")
for p in (V1, ICI):
    if p not in sys.path:
        sys.path.insert(0, p)
import complements_synthese_v1 as C  # noqa: E402
import monde_riche_outils_v1 as M  # noqa: E402

TOLERANCE_COUVERTURE = 1e-3


def matrices(lois, Zref, Gref, nsp):
    """Distances dirigées dg[i, j] = d_nul(i → j) (globale) et ds[i, j] (maximum par strate), formes canoniques."""
    N = len(lois)
    Ps = [M.probas(l, Zref, Gref) for l in lois]
    can = [M.empreinte(M.forme_canonique(l)) for l in lois]
    msk = C.strates(Zref, Gref, nsp)
    dg, ds = np.zeros((N, N)), np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i != j and can[i] != can[j]:
                dg[i, j], ds[i, j] = C.distance_stratifiee(Ps[i], Ps[j], msk)
    return dg, ds, can


def grouper_v2(lois, Zref, Gref, nsp, eps=0.01, eps_strat=0.04, mats=None):
    """Liaison complète ; paire admissible si, dans la direction de plus petite distance globale, d < ε et d_strat < ε_strat.
    Ordre et départages par empreinte canonique (jamais par fournisseur ni par ordre d'entrée)."""
    dg, ds, can = mats or matrices(lois, Zref, Gref, nsp)
    N = len(lois)
    ok = np.eye(N, dtype=bool)
    d = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if can[i] == can[j]:
                ok[i, j] = True
                continue
            a, b = (i, j) if dg[i, j] <= dg[j, i] else (j, i)
            d[i, j] = dg[a, b]
            ok[i, j] = dg[a, b] < eps and ds[a, b] < eps_strat
    rang = {i: r for r, i in enumerate(sorted(range(N), key=lambda i: (can[i], i)))}
    groupes = [[i] for i in sorted(range(N), key=lambda i: rang[i])]
    while True:
        meilleur = None
        for a in range(len(groupes)):
            for b in range(a + 1, len(groupes)):
                if all(ok[i, j] for i in groupes[a] for j in groupes[b]):
                    cle = (max(d[i, j] for i in groupes[a] for j in groupes[b]), rang[groupes[a][0]], rang[groupes[b][0]])
                    if meilleur is None or cle < meilleur[0]:
                        meilleur = (cle, a, b)
        if meilleur is None:
            break
        _, a, b = meilleur
        groupes[a] = sorted(groupes[a] + groupes[b], key=lambda i: rang[i])
        del groupes[b]
    return groupes, (dg, ds, can)


def couverture(groupe, dg):
    return {r: max([dg[j, r] for j in groupe if j != r] or [0.0]) for r in groupe}


def representant_v2(groupe, dg, can, statistique_de_choix=None):
    """Règle v2 : couverture dirigée minimale ; égalité → plus grande statistique sur la tranche de choix (fonction
    `statistique_de_choix(i)`, données fraîches hors juge) ; puis empreinte canonique."""
    c = couverture(groupe, dg)
    m = min(c.values())
    cands = sorted((r for r in groupe if c[r] <= m + TOLERANCE_COUVERTURE), key=lambda r: can[r])
    if len(cands) == 1 or statistique_de_choix is None:
        return cands[0], {"candidats": len(cands), "departage": "empreinte" if len(cands) > 1 else "couverture"}
    s = {r: statistique_de_choix(r) for r in cands}
    best = max(cands, key=lambda r: s[r])  # cands triés par empreinte : à égalité, la plus petite empreinte
    return best, {"candidats": len(cands), "departage": "tranche de choix"}


def medoide_v1(groupe, d, can):
    return C.medoide(groupe, d, can)
