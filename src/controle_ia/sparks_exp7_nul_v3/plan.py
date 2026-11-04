"""Plan de SPARKS-EXP7-NUL, v3 : celui de la v2 (lui-même celui de la v1, plus les six clés de tâche neuves), plus les
constantes des redémarrages et de la minuterie."""
from __future__ import annotations

from ..sparks_exp7_nul_v2.plan import *  # noqa: F401,F403
from ..sparks_exp7_nul_v2.plan import (CHEMIN_ADDENDUM, CHEMIN_PREREG, COMMIT_BASE, GO_ID, PLAFOND_USD,  # noqa: F401
                                       TACHES_NEUVES, construire_plan, entropie_prereg, generateur_tache,
                                       generateurs_neufs, modeles_a_entrainer)

BRANCHE_ORDRES = "calcul/sparks-exp7-nul-v3-ordres"   # ordres écrits de la session aux redémarrages
FIN_ECHEANCE_UTC_S = 1795046400                       # 2026-11-19T00:00:00Z : fin du 18 novembre (échéance du GO)
