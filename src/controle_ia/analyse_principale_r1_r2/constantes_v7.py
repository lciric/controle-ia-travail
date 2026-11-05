"""Constantes gelées de la lecture complémentaire « par épisode » de R1-R2, code v7 (addendum 1 « gardes des
analyses », relance v4 de R1).

Le calcul par épisode, la garde de concordance avec la principale, l'issue et le rendu sont ceux du code v5
(`lecture_v5`, `calcul_v5`, `calcul_v4`), repris sans modification ; toutes les valeurs de `constantes_v1`, `_v2`, `_v4`
et `_v5` restent gelées et sont couvertes par l'empreinte de ce module, comme les valeurs propres au code v6 de la
principale (`constantes_v6`, bloc « v6 » : addendum v4 de R1, commande du rejeu, table v4, résultat de la réparation,
addendum unique), que ce code lit par `entrees_v4.exiger_reception_v4`. Ne s'ajoutent que la version, la commande, le
texte scellé qui gouverne cette lecture (inchangé) et le titre de son bloc dans l'addendum unique.
"""
from __future__ import annotations

import hashlib
import sys

from . import constantes_v5 as K5
from . import constantes_v6 as K6

VERSION = "analyse-par-episode-v1 (code v7)"
COMMANDE = "python -m controle_ia.analyse_principale_r1_r2.lecture_v7"
NOM_SORTIE = K5.NOM_SORTIE                 # même lecture (analyse-par-episode-v1) ; seule la version du code change

# ------------------------------------------------------------ texte scellé qui gouverne (inchangé) et addendum unique
TEXTE = {"chemin": "prereg/analyse-par-episode-v1.md",
         "sha256": "26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4"}
ADDENDUM = K6.ADDENDUM                     # addendum unique des trois analyses (même fichier que la principale)
TITRE_LISTE = "### Liste fermée du code — analyse par épisode (code v7)"

NOMS_GELES = ("VERSION", "COMMANDE", "NOM_SORTIE", "TEXTE", "ADDENDUM", "TITRE_LISTE")


def constantes_courantes() -> dict:
    m = sys.modules[__name__]

    def simple(v):
        if isinstance(v, (tuple, list)):
            return [simple(x) for x in v]
        if isinstance(v, dict):
            return {str(k): simple(x) for k, x in v.items()}
        return v
    return {"v1_v2_v4_v5": K5.constantes_courantes(), "v6": K6.constantes_courantes()["v6"],
            "v7": {n: simple(getattr(m, n)) for n in NOMS_GELES}}


def empreinte_constantes() -> str:
    from ..manifeste import config_canonique

    return hashlib.sha256(config_canonique(constantes_courantes())).hexdigest()


def entropie_principale() -> int:
    """Entropie des plis : celle de la principale scellée (128 premiers bits de 8e267952…), comme les codes v4 et v5."""
    return K5.entropie_principale()
