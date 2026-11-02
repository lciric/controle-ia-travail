"""Lecture gelée du préenregistrement hors échantillon — v3 (corrections M3, M4 de la contre-lecture 2 ; Rc).

Module neuf (R12). Les états, critères, verdicts, scores et le déclencheur « trop beau » sont ceux de
`lecture_hors_echantillon_v2` (classe `LecteurHOv2`, `annoter`, `decompte`), importés tels quels. Ne changent que :
- les lectures prononcées de HP.5a et HP.5b (M3 : ce que dit vraiment la loi de référence) ;
- la phrase de portée (M4 : la rejouée peut aussi échouer sans bogue ; seules les risquées sont indépendantes) ;
- la version inscrite par `annoter` ;
- Rc : `lire_partielle` pour une réplication, sans scores ni « trop beau », marquée `partielle`.
"""
from __future__ import annotations

import copy

from . import lecture_hors_echantillon_v2 as L2
from .lecture_hors_echantillon_v2 import (BLOCS_DE, INSTRUMENT, REJOUEE, RISQUEES, STATUTS, LecteurHOv2,  # noqa: F401
                                          cellules_prevues, decompte, fusionner, nature)

VERSION = "lecture_hors_echantillon_v3"

_HP5A = ("Non, pour ces 60 épisodes et cette sonde : la co-élévation passe sous son taux à m = 3, 4 et 5 "
         "(m = 5 = ⌈K/2⌉), alors que la forme close de la loi de référence la donne au-dessus dès m = 3 (HS.3) ; "
         "la moyenne par pas passe sous son taux à m = 3 à 6, alors que la règle de v1 (HE2.4) la donnait "
         "au-dessus pour m ≥ ⌈K/2⌉ (aucune prédiction de référence à m = 3 et 4). Signes prédits par un modèle "
         "ajusté sur les moments de ces mêmes épisodes ; l'explication par le profil moyen des pas reste une "
         "conjecture (aucune cellule ne mesure où tombent les maxima ; descriptif seulement).")
_HP5B = ("Oui, pour ces 60 épisodes : sous la sonde de tromperie, au-dessus dès m = 4 ; sous la sonde des enjeux, "
         "au-dessus à m = 7 et 10. Ces signes sont ceux que donnent déjà la forme close de la loi de référence "
         "(co-élévation) et la règle de v1 (moyenne par pas, m ≥ ⌈K/2⌉), sauf la moyenne par pas à m = 4 sous la "
         "sonde de tromperie, sans prédiction de référence : ils ne départagent pas le modèle d'un pronostic naïf.")

LIGNES_E = copy.deepcopy(L2.LIGNES_E)
for _l in LIGNES_E:
    if _l["exiges"] == ["HP.5a"]:
        _l["lecture"] = _HP5A
    elif _l["exiges"] == ["HP.5b"]:
        _l["lecture"] = _HP5B

PHRASE_PORTEE = L2.PHRASE_PORTEE.replace(
    "Trois scores distincts : instrument, rejouée, risquées ; seules les risquées peuvent échouer sans bogue.",
    "Trois scores distincts, jamais additionnés : risquées, rejouée, instrument ; seules les risquées et la rejouée "
    "peuvent échouer sans bogue, et seules les risquées sont des prédictions indépendantes.")


def annoter(lecture: dict) -> dict:
    s = L2.annoter(lecture)
    s["lecture_version"] = VERSION
    return s


def lire(resultats: dict, grille: dict) -> dict:
    return annoter(LecteurHOv2(resultats, grille).lire())


def lire_partielle(resultats: dict, grille: dict) -> dict:
    """Lecture d'une réplication (familles rejouées seules) : états et verdicts, sans scores ni « trop beau » (Rc).
    Seule la lecture finale fusionnée, annotée, compte."""
    s = LecteurHOv2(resultats, grille).lire()
    s["partielle"] = True
    s["lecture_version"] = VERSION
    return s


def enonces(lecture: dict) -> list[dict]:
    v = {k: x["verdict"] for k, x in lecture["predictions"].items()}
    return [{"enonce": l["enonce"], "exiges": l["exiges"],
             "lecture": l["lecture"] if all(v.get(k) == "confirmée" for k in l["exiges"])
             else "non établi : voir " + ", ".join(l["exiges"]),
             "verdicts": {k: v.get(k, "absente") for k in l["exiges"]}} for l in LIGNES_E]


def table_E_md() -> str:
    lignes = ["| Énoncé | Lecture prononcée si toutes les exigées sont confirmées | Exigées |", "|---|---|---|"]
    lignes += [f"| {l['enonce']} | {l['lecture']} | {', '.join(l['exiges'])} |" for l in LIGNES_E]
    return "\n".join(lignes)


scores_md = L2.scores_md
