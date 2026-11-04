"""Plan de SPARKS-EXP7-NUL pour l'addendum n° 1 : celui de la v1, inchangé (cas, modèles, entropie = empreinte du
texte v1 scellé), plus les six clés de tâche neuves et les constantes des gardes de l'addendum.

Clés de tâche neuves (addendum, « Graines et manifeste ») : `increment-B3-reechantillonnage`,
`increment-B3-permutation`, `increment-B4-reechantillonnage`, `increment-B4-permutation`,
`bases-B3-reechantillonnage`, `bases-B4-reechantillonnage` ; générateurs propres, rien n'est déplacé dans
`bootstrap` (ordre d'usage de `bootstrap` inchangé : M3, M4, M5, C1).
"""
from __future__ import annotations

from ..sparks_exp7_nul_v1.plan import (CHEMIN_PREREG, LECTEURS, MODELES_LECTEURS, N_PRINCIPAL, N_RESERVE,  # noqa: F401
                                       PAIRES_ANCRE, SHA_PREREG, TYPES, Cas, Modele, construire_plan, entier_tache,
                                       entropie_prereg, generateur_tache, graine_reserve, graine_tache,
                                       modeles_a_entrainer, paires_etalonnage, textes_b1,
                                       verifier_textes_b1_hors_partages)

TACHES_NEUVES = ("increment-B3-reechantillonnage", "increment-B3-permutation", "increment-B4-reechantillonnage",
                 "increment-B4-permutation", "bases-B3-reechantillonnage", "bases-B4-reechantillonnage")
COMMIT_BASE = "55399606f268713bc1d52a9d18ef1e37c681028d"     # code du texte v1 ; la v2 en descend
CHEMIN_ADDENDUM = "prereg/SPARKS-EXP7-NUL-addendum-1.md"     # nom définitif au scellement (R-021)
GO_ID = "GO-2026-11-04-04"
PLAFOND_USD = 40.0                                           # ligne d'extension de GO-2026-11-04-04
ECHEANCE_GO = "2026-11-18"


def generateurs_neufs(entropie: int | None = None) -> dict:
    """Les six générateurs neufs, chacun de sa clé de tâche (R9)."""
    return {t: generateur_tache(t, entropie) for t in TACHES_NEUVES}
