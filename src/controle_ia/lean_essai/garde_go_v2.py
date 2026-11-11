"""A12 — essai Lean, v2 (CLL-11 de la contre-lecture `2077ae26…`, R-2300).

Le GO du pilote D-1b n'est plus reconnu par deux sous-chaînes de son périmètre : son identifiant est **fixé au
préenregistrement** (`go_pilote`) et comparé **par égalité** au GO cité, puis vérifié dans le registre (calcul, Lazar, période,
non révoqué ; périmètre qui n'exclut pas les appels de modèle). Lecture du registre et garde de création reprises de
`garde_go_v1`. Jour pris en UTC (note CLL-16.6).
"""
from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path

from controle_ia.gardes import GardeArret

from .garde_go_v1 import GO_OUTILLAGE_D1A, RE_ID, autoriser_creation_machine, exiger_go_calcul, lire_registre_go  # noqa: F401


def jour_utc() -> date:
    return datetime.now(timezone.utc).date()


def autoriser_appels_modele(go_id: str, chemin_registre: str | Path, aujourdhui: date, go_pilote: str | None) -> dict:
    if not isinstance(go_pilote, str) or not RE_ID.match(go_pilote):
        raise GardeArret("A12 : identifiant du GO du pilote non fixé (pièce du préenregistrement) : appel refusé")
    if go_id != go_pilote:
        raise GardeArret(f"A12 : GO cité {go_id!r} ≠ GO du pilote fixé {go_pilote} : appel refusé")
    g = exiger_go_calcul(go_id, lire_registre_go(chemin_registre), aujourdhui)
    if "aucun appel de modèle" in g["perimetre"].lower():
        raise GardeArret(f"A12 : {go_id} exclut tout appel de modèle : appel refusé")
    return g


class AppelsModeleGardes:
    """Porte de tout appel facturé : A12 (registre relu à chaque appel), puis A7, puis transport (aucun en D-1a)."""

    def __init__(self, go_id: str, go_pilote: str | None, chemin_registre: str | Path, compteur, aujourdhui=jour_utc,
                 transport=None):
        self.go_id = go_id
        self.go_pilote = go_pilote
        self.chemin_registre = Path(chemin_registre)
        self.compteur = compteur
        self.aujourdhui = aujourdhui
        self.transport = transport

    def appeler(self, ident: str, pire_cas: float, requete: dict) -> dict:
        autoriser_appels_modele(self.go_id, self.chemin_registre, self.aujourdhui(), self.go_pilote)
        if self.transport is None:
            raise GardeArret("aucun transport de modèle dans l'outillage D-1a : appel refusé")
        self.compteur.lancer(ident, pire_cas)
        reponse = self.transport(requete)
        self.compteur.terminer(ident, float(reponse["cout_usd"]))
        return reponse
