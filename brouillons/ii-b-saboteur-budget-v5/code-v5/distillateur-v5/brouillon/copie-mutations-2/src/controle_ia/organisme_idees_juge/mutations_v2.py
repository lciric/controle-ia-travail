"""Banc de mutations v2 : le banc v1 (`mutations_v1.banc`, inchangé), plus les quatre mutations de la contre-lecture du
code (`36ecc4a4…`, annexe A), recopiées et jouées en mémoire sur les scénarios d'essai (racine d'essai) :

1. le bras A lit l'issue du bloc suivant **hors de la garde d'accès** (champ privé de `Vue`) ;
2. le placebo P reçoit le ciblage (blocs restants parmi les seules actives) ;
3. la lecture prend un intervalle à 90 % (quantiles 5 % et 95 %) — tuée par l'auto-contrôle de la lecture v2 ;
4. le seuil d'arrêt bas passe à log(1/10) — tuée par les constantes du texte ; variantes : la même règle écrite en dur
   dans `arretee_bas` (constante intacte) — tuée par un vérificateur d'allocation ; la constante mutée avec la garde des
   constantes neutralisée — tuée par la seule troisième écriture du texte (« non conforme au texte »).
"""
from __future__ import annotations

import math
from unittest import mock

import numpy as np

from ..gardes import GardeArret
from . import banc_tirages_repartis_v1 as B
from . import juge_v1
from . import lire_banc_tirages_repartis_v1 as LB1
from . import lire_banc_tirages_repartis_v2 as LB2
from . import mutations_v1 as MU1
from . import rejeu_v1 as R
from . import synthetique_v1 as S
from . import verificateur_texte_v2 as VT

RACINE_ESSAI = MU1.RACINE_ESSAI


def trajectoires_seuil_bas() -> list[list[float]]:
    """Trajectoires d'essai de la v1, plus des cartes entre les deux seuils (log W = −2,5 à 50 tirages) et sous le seuil
    du texte (−3,0)."""
    lw = MU1.trajectoires_essai()
    lw[6] = [-1.0, -2.5] + [-2.4] * 30
    lw[7] = [-1.0, -3.0] + [-2.4] * 30
    lw[8] = [-0.5, -2.6] + [-2.0] * 30
    return lw


def _jouer_v2(J, lw, familles=("N",)):
    """Rejeu comme le jeu v2 : moteur (et son vérificateur v1), puis constantes et troisième écriture du texte."""
    VT.exiger_constantes_du_texte()
    ev = {i: B.EvaluationFiltree(t) for i, t in enumerate(lw)}
    pos = MU1.positions_essai()
    for fam in familles:
        res = R.rejouer_generation(J, ev, pos, RACINE_ESSAI, fam, 0)
        VT.verifier_generation({"famille": fam, "g": 0, "positions": pos, "cartes": [{"trajectoire": t} for t in lw],
                                "bras": res}, RACINE_ESSAI)


# --- mutants de la contre-lecture (annexe A, recopiés) ---------------------------------------------------------------
def _active_anticipee(v):
    if not R.active(v):
        return False
    if 1 <= v.n < R.NB and v._valeurs[v.n] < R.SEUIL_BAS:   # instant non révélé, lu hors de la garde
        return False
    return True


def _A_lit_la_suite(vues, positions, budget, rng=None):
    R._tours(vues, positions, budget, R.NB, 0, _active_anticipee)


def _P_cible(vues, positions, budget, rng):
    R._tours(vues, positions, budget, R.PART_BLOCS, 0, R.active)
    while budget.reste > 0:
        c = R.par_position(positions, [i for i in range(R.M) if R.active(vues[i]) and vues[i].n < R.NB])
        if not c:
            return
        R.donner(vues[c[int(rng.integers(len(c)))]], budget)


def _intervalle_90(self, v):
    v = np.asarray(v, dtype=float)
    if v.size == 0:
        return {"estimation": None, "bas": None, "haut": None, "n": 0}
    moy = v[self.indices(len(v))].mean(axis=1)
    bas, haut = np.quantile(moy, [0.05, 0.95])
    return {"estimation": float(v.mean()), "bas": float(bas), "haut": float(haut), "n": int(len(v))}


def _arretee_bas_un_dixieme_en_dur(v):
    r = v.revelees()
    return any(x < math.log(1 / 10) for k, x in enumerate(r) if k >= 1)


def banc(racine_jeu: int, generations_synthetiques: int = S.GENERATIONS, reechantillons: int = S.REECHANTILLONS) -> dict:
    rapport = MU1.banc(racine_jeu, generations_synthetiques, reechantillons)
    J = juge_v1.charger()
    res = rapport["mutations"]
    lw = trajectoires_seuil_bas()
    _jouer_v2(J, lw, ("N", "T"))                        # sain : les scénarios passent sans mutation
    LB2.exiger_niveau_intervalle(RACINE_ESSAI, 500)     # sain : l'auto-contrôle passe

    res["contre-lecture 1 : A lit le bloc suivant hors de la garde d'accès"] = MU1._tuee(
        lambda: MU1._avec(mock.patch.dict(R.BRAS, {"A": (_A_lit_la_suite, R.BUDGET_BLOCS)}), lambda: _jouer_v2(J, lw)),
        "allocation non conforme")
    res["contre-lecture 2 : placebo ciblé (actives seulement)"] = MU1._tuee(
        lambda: MU1._avec(mock.patch.dict(R.BRAS, {"P": (_P_cible, R.BUDGET_BLOCS)}), lambda: _jouer_v2(J, lw)),
        "allocation non conforme")
    res["contre-lecture 3 : intervalle à 90 %"] = MU1._tuee(
        lambda: MU1._avec(mock.patch.object(LB1.Reechantillonneur, "intervalle", _intervalle_90),
                          lambda: LB2.exiger_niveau_intervalle(RACINE_ESSAI, 500)),
        "niveau de l'intervalle")
    res["contre-lecture 4 : seuil d'arrêt bas à 1/10 (constante)"] = MU1._tuee(
        lambda: MU1._avec(mock.patch.object(R, "SEUIL_BAS", math.log(1 / 10)), lambda: _jouer_v2(J, lw)),
        "constante(s) du moteur ≠ texte")
    res["contre-lecture 4 bis : seuil d'arrêt bas à 1/10 écrit dans la règle"] = MU1._tuee(
        lambda: MU1._avec(mock.patch.object(R, "arretee_bas", _arretee_bas_un_dixieme_en_dur), lambda: _jouer_v2(J, lw)),
        "allocation non conforme")

    def constante_et_garde_neutralisee():
        with mock.patch.object(R, "SEUIL_BAS", math.log(1 / 10)), mock.patch.object(VT, "exiger_constantes_du_texte", lambda: None):
            _jouer_v2(J, lw)
    res["contre-lecture 4 ter : seuil à 1/10, garde des constantes neutralisée (troisième écriture seule)"] = MU1._tuee(
        constante_et_garde_neutralisee, "allocation non conforme au texte")
    rapport["toutes_tuees"] = all(r["tuee"] for r in res.values()) and rapport["synthetique"]["sain_sous_un"]
    rapport["version_banc"] = 2
    return rapport


exiger_toutes_tuees = MU1.exiger_toutes_tuees
