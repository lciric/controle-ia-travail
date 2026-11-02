"""Calcul de la lecture complémentaire « par épisode », code v5.

Le calcul par épisode est celui du code v4 (`calcul_v4`), repris sans modification et réexporté ici. S'y ajoute la mesure
par action qui sert à la garde de concordance avec la principale (contre-lecture, C1) : pour chaque bras, l'évaluation par
action aux trois taux de la principale (`calcul_v1.evaluer`, mêmes arguments que `lecture_v1._lecture_ensemble`) et l'aire
par action (`calcul_v1.auc`).
"""
from __future__ import annotations

from . import calcul_v1 as CV
from . import constantes_v5 as K5
from .calcul_v4 import (bras_episode, episodes_de, moins_log_p, pas_de_detection, plancher_episode,  # noqa: F401
                        plis_episodes)


def mesures_par_action(bras_act: dict, eligible, cond, pli, tache_idx, n_taches: int) -> dict:
    """Pour chaque bras : `par_alpha[a]` = `calcul_v1.evaluer` au taux a de la principale (rappel, seuils par pli,
    alarmes) et `auc` = aire par action, calculés comme dans la principale (mêmes actions éligibles, mêmes plis)."""
    sortie = {}
    for b, d in bras_act.items():
        ev = {CV.nom_alpha(a): CV.evaluer(d, eligible, cond, pli, tache_idx, n_taches, a) for a in K5.ALPHAS_CONCORDANCE}
        sortie[b] = {"par_alpha": ev, "auc": CV.auc(d["test"], eligible, cond, tache_idx, n_taches)}
    return sortie


__all__ = ["episodes_de", "plis_episodes", "moins_log_p", "bras_episode", "pas_de_detection", "plancher_episode",
           "mesures_par_action"]
