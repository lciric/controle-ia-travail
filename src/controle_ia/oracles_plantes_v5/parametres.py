"""Lecture des paramètres du lot B1, version 5 : gelés par le brouillon 2 du préenregistrement, sauf la liste « provisoire »."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from ..gardes import GardeArret

CHEMIN = Path(__file__).with_name("parametres_v5.json")
STATUT_PROVISOIRE = "gelé par le préenregistrement, brouillon 2 (ba5ddf70…), sauf les clés listées dans « provisoire »"


def _refuser_flottant(texte):
    raise GardeArret(f"paramètres : nombre décimal JSON {texte} refusé (v2, remarque 5) ; écrire un texte « a/b »")


def charger(chemin: str | Path = CHEMIN) -> tuple[dict, str]:
    octets = Path(chemin).read_bytes()
    p = json.loads(octets.decode("utf-8"), parse_float=_refuser_flottant)
    if p.get("statut") != STATUT_PROVISOIRE:
        raise GardeArret(f"paramètres {chemin} : statut {p.get('statut')!r} inattendu dans le lot B1")
    for fam in ("F1", "F2", "F3"):
        g = p["gabarits"][fam]
        if len(g["verites"]) != p["plantation"]["verites"] or len(g["faux_tot"]) != p["plantation"]["faux_tot"] \
                or len(g["pieges"]) != p["plantation"]["pieges"]:
            raise GardeArret(f"paramètres : nombre de gabarits de {fam} incohérent avec la plantation")
        pl = p["plantation"]
        if len(g["verites_seuil"]) != pl["verites_seuil"] or not set(g["verites_seuil"]) <= set(g["verites"]) \
                or len(g["faux_tot_seuil"]) != pl["faux_tot_seuil"] or not set(g["faux_tot_seuil"]) <= set(g["faux_tot"]):
            raise GardeArret(f"paramètres : gabarits de forme seuil de {fam} incohérents avec le brouillon 2")
    return p, hashlib.sha256(octets).hexdigest()
