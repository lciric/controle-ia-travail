"""Constantes gelées de l'analyse principale de R1-R2, code v2 (brouillon 2 du préenregistrement ; décisions de conv-audit,
R-1091).

Seul changement de fond par rapport au code v1 : la racine des graines (Q9). Elle n'est plus l'empreinte du texte du
fournisseur (`constantes_v1.entropie_racine`, gardée telle quelle, R12, et non lue par le code v2) mais les 128 premiers
bits de l'empreinte sha256 de **ce** préenregistrement scellé, comme les autres préenregistrements de conv-audit. Toutes les
autres valeurs restent dans `constantes_v1` (lu par `calcul_v1` et `entrees_v1`) ; l'empreinte citée couvre les deux.
"""
from __future__ import annotations

import hashlib
import sys

from . import constantes_v1 as K1

VERSION = "analyse-principale-r1-r2-v1 (code v2)"
COMMANDE = "python -m controle_ia.analyse_principale_r1_r2.lecture_v2"
NOM_SORTIE = "analyse-principale-r1-r2-v1"
REGLE_ENTROPIE = "128 premiers bits de l'empreinte sha256 du préenregistrement d'analyse scellé (int.from_bytes(…[:16], 'big'))"
MOTIF_Q8 = ("aucune ligne gelée ne s'applique (la ligne « au-dessus » exige mention conforme) : Δ rapporté sans verdict ; "
            "nœud de lecture (décision de Lazar)")

NOMS_GELES = ("VERSION", "COMMANDE", "NOM_SORTIE", "REGLE_ENTROPIE", "MOTIF_Q8")


def constantes_courantes() -> dict:
    m = sys.modules[__name__]
    return {"v1": K1.constantes_courantes(), "v2": {n: getattr(m, n) for n in NOMS_GELES}}


def empreinte_constantes() -> str:
    from ..manifeste import config_canonique

    return hashlib.sha256(config_canonique(constantes_courantes())).hexdigest()


def entropie_de(sha_prereg: str) -> int:
    """Racine des graines (R9) : les 128 premiers bits de l'empreinte du préenregistrement d'analyse scellé."""
    return int.from_bytes(bytes.fromhex(sha_prereg)[:16], "big")
