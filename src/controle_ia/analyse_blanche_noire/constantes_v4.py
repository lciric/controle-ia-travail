"""Constantes gelées de la version 4 du code de l'analyse secondaire (texte scellé `analyse-blanche-noire-v3`,
inchangé ; addendum 1 « gardes des analyses », relance v4 de R1).

Version 4 = version 3 reprise sans modification (`lecture_v3`, `entrees_v3`, `evaluation_v3`, `rendu_v3` et les
modules v1 qu'ils reprennent), plus les trois gardes de réception exigées par l'addendum v4 de R1 scellé
(`prereg/R1-addendum-relance-v4.md`, étape 4, « Analyses (inchangées) ») — `texte`, `table-comparee`, `provenance` —
et ce qui lie ce code à l'addendum unique des trois analyses. Les valeurs communes restent dans `constantes` (v1) et
`constantes_v3` ; l'empreinte citée par l'addendum couvre les trois (`empreinte_constantes`).
"""
from __future__ import annotations

import hashlib
import sys

from . import constantes_v3 as C3

VERSION = "analyse-blanche-noire-v3 (code v4)"
COMMANDE = "python -m controle_ia.analyse_blanche_noire.lecture_v4"
NOM_SORTIE = C3.NOM_SORTIE                 # même lecture (analyse-blanche-noire-v3) ; seule la version du code change
FORMAT_FICHE = C3.FORMAT_FICHE

# ------------------------------------------------------------ texte scellé qui gouverne (inchangé) et addendum unique
TEXTE = {"chemin": "prereg/analyse-blanche-noire-v3.md",
         "sha256": "1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9"}
ADDENDUM = "prereg/addendum-1-gardes-analyses-r1-v4-v1.md"   # addendum unique des trois analyses, scellé : liste fermée v4
TITRE_LISTE = "### Liste fermée du code — analyse secondaire (code v4)"

# ------------------------------------------------------------ relance v4 de R1 (addendum v4 scellé, étape 4 ; fiche v4, § 6)
ADDENDUM_V4 = {"chemin": "prereg/R1-addendum-relance-v4.md",
               "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"}   # garde `texte`
COMMANDE_REJEU_V4 = "python -m controle_ia.runs_nuit.rejeu_activations_v4"                        # garde `provenance`
TABLE_V4 = "prereg/R1-table-tokenisation-v4.json"                       # garde `table-comparee` : table versée avec le run
RESULTAT_REPARATION_V4 = "diag/20261104-234729-r1-v4-reparation-reel/resolution-graine-lot-v3-reparation.json"

NOMS_GELES = ("VERSION", "COMMANDE", "NOM_SORTIE", "FORMAT_FICHE", "TEXTE", "ADDENDUM", "TITRE_LISTE", "ADDENDUM_V4",
              "COMMANDE_REJEU_V4", "TABLE_V4", "RESULTAT_REPARATION_V4")


def constantes_courantes() -> dict:
    m = sys.modules[__name__]

    def simple(v):
        if isinstance(v, (tuple, list)):
            return [simple(x) for x in v]
        if isinstance(v, dict):
            return {str(k): simple(x) for k, x in v.items()}
        return v
    return {"v1_v3": C3.constantes_courantes(), "v4": {n: simple(getattr(m, n)) for n in NOMS_GELES}}


def empreinte_constantes() -> str:
    from ..manifeste import config_canonique

    return hashlib.sha256(config_canonique(constantes_courantes())).hexdigest()


def cles_de_graines() -> list[str]:
    return C3.cles_de_graines()
