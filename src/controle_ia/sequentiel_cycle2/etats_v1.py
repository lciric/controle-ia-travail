"""États de dose et de cycle, transposés du brouillon 3 (« Seuil »), et règle de cumul entre deux lectures.

Six affirmations élémentaires par dose, chacune « établie » ou non à une lecture, à son niveau :
  c1 : borne basse de D_somme > 0        c2 : borne basse de l'écart > 0      c3 : borne haute de l'écart < 0
  c4 : borne basse de D_maximum > 0      c5 : borne haute de D_somme < marge  c6 : borne haute de l'écart < marge
Règle de cumul : une affirmation est acquise à la lecture finale si elle est établie à l'intermédiaire, à son
niveau intermédiaire, OU à la finale, à son niveau final (la somme des deux niveaux est le niveau du brouillon 3).
Les états « hors lecture », « échec » et « saturé » tiennent à des gardes de validité : hors de ce module.
"""
from __future__ import annotations

from ..gardes import GardeArret

AFFIRMATIONS = ("c1", "c2", "c3", "c4", "c5", "c6")
ETATS_DOSE = ("AP", "M", "P", "G", "R", "Z", "C")
ETATS_CYCLE = ("partage", "accumuler_propre", "maximum_bat", "rien_de_propre", "propre_sans_gain",
               "gain_non_propre", "non_concluant")


def _exiger(aff: dict) -> None:
    if set(aff) != set(AFFIRMATIONS) or not all(isinstance(v, bool) for v in aff.values()):
        raise GardeArret(f"affirmations attendues : {AFFIRMATIONS}, valeurs booléennes ; reçu {aff!r}")


def cumuler(intermediaire: dict, finale: dict) -> dict:
    _exiger(intermediaire)
    _exiger(finale)
    return {c: intermediaire[c] or finale[c] for c in AFFIRMATIONS}


def etat_dose(aff: dict) -> str:
    """Première règle qui s'applique (brouillon 3, « État d'une dose », règles 4 à 9) ; « C » : contradiction."""
    _exiger(aff)
    if aff["c2"] and aff["c3"]:
        return "C"   # écart établi dans les deux sens (possible seulement par cumul) : aucun état, audit
    if aff["c1"] and aff["c2"]:
        return "AP"
    if aff["c3"] and aff["c4"]:
        return "M"
    if aff["c1"]:
        return "P"
    if aff["c2"]:
        return "G"
    if aff["c5"] and aff["c6"]:
        return "R"
    return "Z"


def etat_cycle(etats: list[str], signal_plante_reconnu: bool = True) -> str:
    """Règles (2) à (9) de l'état du cycle ; les règles (0), (1) et (8) tiennent aux gardes de validité."""
    if not etats or any(e not in ETATS_DOSE for e in etats):
        raise GardeArret(f"états de dose inconnus ou absents : {etats!r}")
    if "AP" in etats and "M" in etats:
        return "partage"
    if "AP" in etats:
        return "accumuler_propre"
    if "M" in etats:
        return "maximum_bat"
    if all(e == "R" for e in etats) and signal_plante_reconnu:
        return "rien_de_propre"
    if "P" in etats:
        return "propre_sans_gain"
    if "G" in etats:
        return "gain_non_propre"
    return "non_concluant"


# --- Versions vectorisées (mêmes règles ; égalité à la version de référence éprouvée par énumération) ---

def etats_dose_vect(aff: dict):
    """Tableau d'indices dans ETATS_DOSE, pour des tableaux booléens de même forme."""
    import numpy as np

    c = {a: np.asarray(aff[a], dtype=bool) for a in AFFIRMATIONS}
    conditions = [c["c2"] & c["c3"], c["c1"] & c["c2"], c["c3"] & c["c4"], c["c1"], c["c2"], c["c5"] & c["c6"]]
    codes = [ETATS_DOSE.index(e) for e in ("C", "AP", "M", "P", "G", "R")]
    return np.select(conditions, codes, default=ETATS_DOSE.index("Z"))


def etats_cycle_vect(codes_dose, signal_plante_reconnu: bool = True):
    """Tableau d'indices dans ETATS_CYCLE ; `codes_dose` : (répliques, doses)."""
    import numpy as np

    e = np.asarray(codes_dose)
    a = lambda nom: (e == ETATS_DOSE.index(nom)).any(axis=1)
    tous_r = (e == ETATS_DOSE.index("R")).all(axis=1) & signal_plante_reconnu
    conditions = [a("AP") & a("M"), a("AP"), a("M"), tous_r, a("P"), a("G")]
    return np.select(conditions, list(range(6)), default=6)
