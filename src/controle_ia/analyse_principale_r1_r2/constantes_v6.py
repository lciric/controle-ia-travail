"""Constantes gelées de l'analyse principale de R1-R2, code v6 (addendum 1 « gardes des analyses », relance v4 de R1).

Le calcul, l'issue et le rendu sont ceux du code v2 (`lecture_v2`, `lecture_v1`, `calcul_v1`), repris sans
modification ; toutes les valeurs de `constantes_v1` et `constantes_v2` restent gelées et sont couvertes par l'empreinte
de ce module. Ne s'ajoutent que les valeurs des trois gardes de réception exigées par l'addendum v4 de R1 scellé
(`prereg/R1-addendum-relance-v4.md`, étape 4, « Analyses (inchangées) ») — `texte`, `table-comparee`, `provenance` —
et ce qui lie ce code à l'addendum unique des trois analyses : le texte scellé qui gouverne (inchangé : chemin et
empreinte), le chemin de l'addendum unique et le titre du bloc de l'addendum qui porte la liste fermée de cette analyse.
"""
from __future__ import annotations

import hashlib
import sys

from . import constantes_v2 as K2

VERSION = "analyse-principale-r1-r2-v1 (code v6)"
COMMANDE = "python -m controle_ia.analyse_principale_r1_r2.lecture_v6"
NOM_SORTIE = K2.NOM_SORTIE                 # même lecture (analyse-principale-r1-r2-v1) ; seule la version du code change

# ------------------------------------------------------------ texte scellé qui gouverne (inchangé) et addendum unique
TEXTE = {"chemin": "prereg/analyse-principale-r1-r2-v1.md",
         "sha256": "8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537"}
ADDENDUM = "prereg/addendum-1-gardes-analyses-r1-v4-v1.md"   # addendum unique des trois analyses, scellé : liste fermée v6
TITRE_LISTE = "### Liste fermée du code — analyse principale (code v6)"

# ------------------------------------------------------------ relance v4 de R1 (addendum v4 scellé, étape 4 ; fiche v4, § 6)
ADDENDUM_V4 = {"chemin": "prereg/R1-addendum-relance-v4.md",
               "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"}   # garde `texte`
COMMANDE_REJEU_V4 = "python -m controle_ia.runs_nuit.rejeu_activations_v4"                        # garde `provenance`
TABLE_V4 = "prereg/R1-table-tokenisation-v4.json"                       # garde `table-comparee` : table versée avec le run
RESULTAT_REPARATION_V4 = "diag/20261104-234729-r1-v4-reparation-reel/resolution-graine-lot-v3-reparation.json"

NOMS_GELES = ("VERSION", "COMMANDE", "NOM_SORTIE", "TEXTE", "ADDENDUM", "TITRE_LISTE", "ADDENDUM_V4",
              "COMMANDE_REJEU_V4", "TABLE_V4", "RESULTAT_REPARATION_V4")


def constantes_courantes() -> dict:
    m = sys.modules[__name__]

    def simple(v):
        if isinstance(v, (tuple, list)):
            return [simple(x) for x in v]
        if isinstance(v, dict):
            return {str(k): simple(x) for k, x in v.items()}
        return v
    return {"v1_v2": K2.constantes_courantes(), "v6": {n: simple(getattr(m, n)) for n in NOMS_GELES}}


def empreinte_constantes() -> str:
    from ..manifeste import config_canonique

    return hashlib.sha256(config_canonique(constantes_courantes())).hexdigest()
