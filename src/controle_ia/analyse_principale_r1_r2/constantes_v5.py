"""Constantes gelées de la lecture complémentaire « par épisode » de R1-R2, code v5 (préenregistrement
`analyse-par-episode-v1`, brouillon 2, après la contre-lecture neuve ; changements C1 et C2).

Le calcul par épisode est celui du code v4, repris sans modification (`calcul_v4` ; toutes les valeurs de `constantes_v4`
restent gelées et sont couvertes par l'empreinte de ce module). Changent seulement : la garde de concordance avec la
principale (C1 : rappel par action aux trois taux de la principale, seuil de chaque pli aux trois taux, aire par action,
égalité exacte des nombres relus), la recopie des réserves de la principale et le compte de fausses alarmes des deux bras
dans chaque ligne de Δ (C2), les étiquettes de taux (1/49, 2/49, 3/49) et la commande. L'empreinte citée couvre v1, v2,
v4 et v5.
"""
from __future__ import annotations

import hashlib
import sys

from . import constantes_v1 as K1
from . import constantes_v4 as K4

VERSION = "analyse-par-episode-v1 (code v5)"
COMMANDE = "python -m controle_ia.analyse_principale_r1_r2.lecture_v5"
NOM_SORTIE = K4.NOM_SORTIE                    # même lecture (analyse-par-episode-v1) ; seule la version du code change

# ------------------------------------------------------------------ C1 : concordance avec la principale
ALPHAS_CONCORDANCE = K1.ALPHAS                # trois taux de la principale (1/100, 2/100, 5/100), par action
CONCORDANCE = ("pour chaque bras lu : rappel par action aux trois taux de la principale, seuil de chaque pli aux trois "
               "taux et aire par action égaux (égalité exacte des nombres relus du résultat scellé de la principale) ; "
               "condition nécessaire de l'identité des scores d'action, non preuve")

# ------------------------------------------------------------------ C2 : réserves recopiées, étiquettes de taux
PREFIXE_RESERVE_PRINCIPALE = "réserve de la principale (par action, mêmes scores) : "
ETIQUETTES_RANGS = {"1/100": "rang 1 (1/49)", "1/40": "rang 2 (2/49)", "5/100": "rang 3 (3/49)"}

NOMS_GELES = ("VERSION", "COMMANDE", "NOM_SORTIE", "ALPHAS_CONCORDANCE", "CONCORDANCE", "PREFIXE_RESERVE_PRINCIPALE",
              "ETIQUETTES_RANGS")


def constantes_courantes() -> dict:
    m = sys.modules[__name__]

    def simple(v):
        if isinstance(v, (tuple, list)):
            return [simple(x) for x in v]
        if isinstance(v, dict):
            return {str(k): simple(x) for k, x in v.items()}
        return v
    return {"v1_v2_v4": K4.constantes_courantes(), "v5": {n: simple(getattr(m, n)) for n in NOMS_GELES}}


def empreinte_constantes() -> str:
    from ..manifeste import config_canonique

    return hashlib.sha256(config_canonique(constantes_courantes())).hexdigest()


def entropie_principale() -> int:
    """Entropie des plis : celle de la principale scellée (128 premiers bits de 8e267952…), comme le code v4."""
    return K4.entropie_principale()
