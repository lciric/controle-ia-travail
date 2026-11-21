"""Oracle à contexte réécrit : choisir la suite de réécriture, couplée par moitié, v5 (texte scellé, section 3.3 a et b).

Fonction pure des huit valeurs lues, du coût déclaré lu et d'un générateur. Aucun texte n'entre ni ne sort : le résultat est
l'indice d'une suite du jumeau, ou « repli vide » ; **jamais un texte de l'agent**.

a. Coût déclaré lisible : les k suites lisibles sont rangées par valeur croissante, ex aequo départagés au hasard (le coût
   déclaré compris) ; le coût tombe dans un intervalle j de 0 à k ; la voisine du dessous (rang j) est prise avec la
   probabilité j / k, celle du dessus (rang j + 1) sinon ; les rangs sont découpés en blocs de 4 à partir du bas ; la suite
   retenue est tirée au hasard dans le bloc de la voisine. Si k = 0 : cas b.
b. Coût déclaré illisible (ou aucune suite lisible) : une suite illisible tirée au hasard ; s'il n'y en a aucune, repli vide.

`loi_de_la_suite_retenue` rend la loi exacte (fractions) de l'indice retenu, par les mêmes étapes : elle sert aux essais
d'énumération complète.

Ce que le couplage garantit (texte scellé, 3.3, phrase de l'erratum 1, `2031baba…`, qui prime) : chaque suite est retenue avec la
même probabilité 1/k si le coût déclaré est tiré de la même loi que les suites (exact à la deuxième action seulement) ; la valeur
retenue n'est pas pour autant de la loi d'une suite prise au hasard : les blocs de 4 favorisent le milieu (à huit suites, la
valeur du milieu des neuf réunies est retenue 2 fois sur 9) et réduisent sa variance (0,90 fois). Effet sur l'arrêt à tort de
l'épreuve du centrage : non vu, dans un modèle de chaîne simplifié (erratum 1). Les essais énumèrent les deux faits
(`test_enumeration_complete_…`, `test_frequence_par_valeur_reunie_dite`). Aucune logique n'est changée par l'erratum.
"""
from __future__ import annotations

from fractions import Fraction

from ..gardes import GardeArret

BLOC = 4
REPLI_VIDE = "repli_vide"


def _lisibles(valeurs) -> list[int]:
    return [i for i, v in enumerate(valeurs) if v is not None]


def bloc_du_rang(rang: int, k: int, bloc: int = BLOC) -> list[int]:
    """Rangs (de 1 à k) du bloc qui contient `rang`, blocs de `bloc` rangs à partir du bas."""
    debut = ((rang - 1) // bloc) * bloc + 1
    return list(range(debut, min(debut + bloc - 1, k) + 1))


def choisir(valeurs, cout, rng, bloc: int = BLOC) -> dict:
    """`valeurs` : valeurs lues des suites (None si illisible) ; `cout` : coût déclaré lu (None si illisible)."""
    valeurs = list(valeurs)
    lis = _lisibles(valeurs)
    k = len(lis)
    if cout is None or k == 0:
        illisibles = [i for i, v in enumerate(valeurs) if v is None]
        if not illisibles:
            return {"cas": "b", "indice": None, "repli_vide": True, "j": None, "k": k, "rang_voisine": None, "rang_retenue": None}
        return {"cas": "b", "indice": int(illisibles[int(rng.integers(0, len(illisibles)))]), "repli_vide": False, "j": None, "k": k,
                "rang_voisine": None, "rang_retenue": None}
    cles = {i: float(rng.random()) for i in lis}
    cle_cout = float(rng.random())
    ordre = sorted(lis, key=lambda i: (valeurs[i], cles[i]))
    j = sum(1 for i in lis if (valeurs[i], cles[i]) < (cout, cle_cout))
    voisine = j if float(rng.random()) < j / k else j + 1
    rangs = bloc_du_rang(voisine, k, bloc)
    retenue = rangs[int(rng.integers(0, len(rangs)))]
    return {"cas": "a", "indice": int(ordre[retenue - 1]), "repli_vide": False, "j": int(j), "k": k, "rang_voisine": int(voisine),
            "rang_retenue": int(retenue)}


def loi_du_rang_retenu(j: int, k: int, bloc: int = BLOC) -> dict[int, Fraction]:
    """Loi exacte du rang retenu sachant l'intervalle j du coût déclaré."""
    loi: dict[int, Fraction] = {}
    for voisine, p in ((j, Fraction(j, k)), (j + 1, 1 - Fraction(j, k))):
        if p == 0:
            continue
        rangs = bloc_du_rang(voisine, k, bloc)
        for r in rangs:
            loi[r] = loi.get(r, Fraction(0)) + p / len(rangs)
    return loi


def loi_de_l_indice_sachant_j(valeurs, j: int, bloc: int = BLOC) -> dict:
    """Loi exacte de l'indice retenu sachant l'intervalle j du coût déclaré (de 0 à k) ; les suites ex aequo se partagent
    uniformément les rangs de leur groupe."""
    valeurs = list(valeurs)
    lis = _lisibles(valeurs)
    k = len(lis)
    if not 0 <= j <= k or k == 0:
        raise GardeArret(f"couplage : intervalle {j} hors de 0 à {k}")
    loi_rang = loi_du_rang_retenu(j, k, bloc)
    loi: dict = {}
    rang = 0
    for v in sorted(set(valeurs[i] for i in lis)):
        groupe = [i for i in lis if valeurs[i] == v]
        masse = sum((loi_rang.get(r, Fraction(0)) for r in range(rang + 1, rang + len(groupe) + 1)), Fraction(0))
        for i in groupe:
            loi[i] = masse / len(groupe)
        rang += len(groupe)
    return loi


def loi_de_la_suite_retenue(valeurs, cout, bloc: int = BLOC) -> dict:
    """Loi exacte de l'indice retenu (clé `REPLI_VIDE` pour le repli) ; ex aequo départagés uniformément."""
    valeurs = list(valeurs)
    lis = _lisibles(valeurs)
    k = len(lis)
    if cout is None or k == 0:
        illisibles = [i for i, v in enumerate(valeurs) if v is None]
        if not illisibles:
            return {REPLI_VIDE: Fraction(1)}
        return {i: Fraction(1, len(illisibles)) for i in illisibles}
    dessous = sum(1 for i in lis if valeurs[i] < cout)
    egaux = sum(1 for i in lis if valeurs[i] == cout)
    loi: dict = {}
    for j in range(dessous, dessous + egaux + 1):
        for i, p in loi_de_l_indice_sachant_j(valeurs, j, bloc).items():
            loi[i] = loi.get(i, Fraction(0)) + p / (egaux + 1)
    return loi


def exiger_remplacement_du_jumeau(choix: dict, n_suites: int) -> None:
    """Le choix désigne une suite du jumeau ou le repli vide : tout autre résultat (un texte, une fenêtre de l'agent) arrête."""
    if not isinstance(choix, dict) or set(choix) != {"cas", "indice", "repli_vide", "j", "k", "rang_voisine", "rang_retenue"}:
        raise GardeArret("couplage : résultat hors du schéma (la réécriture ne prend qu'une suite du jumeau ou le repli vide)")
    i = choix["indice"]
    if choix["repli_vide"]:
        if i is not None:
            raise GardeArret("couplage : repli vide avec un indice de suite")
        return
    if isinstance(i, bool) or not isinstance(i, int) or not 0 <= i < n_suites:
        raise GardeArret(f"couplage : indice {i!r} hors des {n_suites} suites du jumeau (jamais un texte de l'agent)")
