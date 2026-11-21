"""Essais v2 (majeur 3 de la contre-lecture du code) : niveau de l'intervalle et seuils épinglés ; constantes du texte ;
troisième écriture des bras égale au moteur et qui voit ce que le vérificateur v1 ne voit pas."""
import math
from unittest import mock

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B
from controle_ia.organisme_idees_juge import juge_v1
from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v1 as LB1
from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v2 as LB2
from controle_ia.organisme_idees_juge import mutations_v1 as MU1
from controle_ia.organisme_idees_juge import mutations_v2 as MU2
from controle_ia.organisme_idees_juge import rejeu_v1 as R
from controle_ia.organisme_idees_juge import synthetique_v1 as S
from controle_ia.organisme_idees_juge import verificateur_texte_v2 as VT

RAC = MU1.RACINE_ESSAI


@pytest.fixture(scope="module")
def J():
    return juge_v1.charger()


def _ev(lw):
    return {i: B.EvaluationFiltree([round(float(v), 6) for v in t]) for i, t in enumerate(lw)}


def _resultat(J, lw, pos, fam="N", g=0):
    res = R.rejouer_generation(J, _ev(lw), pos, RAC, fam, g)
    return {"famille": fam, "g": g, "positions": pos, "cartes": [{"trajectoire": [round(float(v), 6) for v in t]} for t in lw],
            "bras": res}


def test_seuils_du_texte_epingles():
    assert R.SEUIL_BAS == math.log(1 / 20) and R.SEUIL_HAUT == math.log(24 / 0.05)
    assert VT.SEUIL_BAS_TEXTE == math.log(1 / 20) and VT.SEUIL_HAUT_TEXTE == math.log(24 / 0.05)
    entre = R.Vue([-1.0, -2.5] + [0.0] * 30)        # 1/20 < W < 1/10 à 50 tirages : pas d'arrêt bas
    sous = R.Vue([-1.0, -3.0] + [0.0] * 30)         # W < 1/20 à 50 tirages : arrêt bas
    for v in (entre, sous):
        v.reveler(); v.reveler()
    assert not R.arretee_bas(entre) and R.arretee_bas(sous)
    assert not VT._bas(entre.revelees(), 2) and VT._bas(sous.revelees(), 2)
    tot = R.Vue([-3.5] + [0.0] * 31)                # sous 1/20 à 25 tirages seulement : pas d'arrêt
    tot.reveler()
    assert not R.arretee_bas(tot) and not VT._bas(tot.revelees(), 1)


def test_niveau_de_l_intervalle_epingle():
    v = np.random.default_rng(1).normal(0.02, 0.3, 200)
    rs = LB1.Reechantillonneur(RAC, 2000)
    r = rs.intervalle(v)
    moy = np.array([v[B.generateur(RAC, 99, b).integers(0, 200, size=200)].mean() for b in range(2000)])
    bas, haut = np.quantile(moy, [0.025, 0.975])
    assert r["bas"] == pytest.approx(bas, abs=1e-15) and r["haut"] == pytest.approx(haut, abs=1e-15)
    b90, h90 = np.quantile(moy, [0.05, 0.95])
    assert r["bas"] < b90 and r["haut"] > h90
    assert LB1.REECHANTILLONS == 10_000
    LB2.exiger_niveau_intervalle(RAC, 1000)                                       # sain
    with mock.patch.object(LB1.Reechantillonneur, "intervalle", MU2._intervalle_90):
        with pytest.raises(GardeArret, match="niveau de l'intervalle"):
            LB2.exiger_niveau_intervalle(RAC, 1000)                               # artefact


def test_constantes_du_texte_cas_sain_et_artefacts():
    VT.exiger_constantes_du_texte()
    for module, nom, valeur in ((R, "SEUIL_BAS", math.log(1 / 10)), (R, "SEUIL_HAUT", math.log(20)), (R, "PART_BLOCS", 9),
                                (B, "PART", 250), (B, "ORACLE_N", 4000), (LB1, "REECHANTILLONS", 1000),
                                (S, "PLAFOND_LOG_E", 40.0), (S, "GENERATIONS", 2000)):
        with mock.patch.object(module, nom, valeur):
            with pytest.raises(GardeArret, match="constante"):
                VT.exiger_constantes_du_texte()


@pytest.mark.parametrize("graine", range(30))
def test_troisieme_ecriture_egale_au_moteur(J, graine):
    rng = np.random.default_rng([11, graine])
    if graine % 3 == 0:     # régime proche du banc : 18 cartes qui tombent, les autres indécises
        derive = np.r_[np.full(18, -0.4), rng.choice([-0.02, 0.0, 0.05, 0.15], size=6)][rng.permutation(24)][:, None]
        lw = np.cumsum(rng.normal(derive, 0.35, (24, 32)), axis=1)
    else:
        lw = np.cumsum(rng.normal(rng.choice([-0.3, -0.1, 0.0, 0.1, 0.3], (24, 1)), rng.choice([0.3, 0.8, 1.5]), (24, 32)), axis=1)
    pos = [int(p) for p in rng.permutation(24)]
    r = _resultat(J, lw.round(6).tolist(), pos, "N", graine)
    VT.verifier_generation(r, RAC)
    for nom in R.BRAS_N:
        lw_r = [c["trajectoire"] for c in r["cartes"]]
        assert VT.allocation_du_texte(nom, lw_r, pos, RAC, 0, graine) == r["bras"][nom]["blocs"]


def test_troisieme_ecriture_voit_un_seuil_partage(J):
    """Seuil bas à 1/10 dans le moteur : le vérificateur v1 (même constante) ne voit rien, la troisième écriture voit."""
    lw = MU2.trajectoires_seuil_bas()
    pos = MU1.positions_essai()
    with mock.patch.object(R, "SEUIL_BAS", math.log(1 / 10)):
        r = _resultat(J, lw, pos)                         # le moteur et le vérificateur v1 s'accordent
        with pytest.raises(GardeArret, match="allocation non conforme au texte"):
            VT.verifier_generation(r, RAC)
    VT.verifier_generation(_resultat(J, lw, pos), RAC)    # sain


def test_verifier_generation_artefacts_sans_chiffre_dans_le_message(J):
    r = _resultat(J, MU2.trajectoires_seuil_bas(), MU1.positions_essai())
    VT.verifier_generation(r, RAC)
    cas = []
    a = {**r, "bras": {k: dict(v) for k, v in r["bras"].items()}}; a["bras"]["A"]["blocs"] = [b + (i == 4) for i, b in enumerate(a["bras"]["A"]["blocs"])]; cas.append((a, "allocation"))
    b = {**r, "bras": {k: dict(v) for k, v in r["bras"].items()}}; b["bras"]["P"]["log_e"] = [x + 0.1 for x in b["bras"]["P"]["log_e"]]; cas.append((b, "valeur e"))
    c = {**r, "bras": {k: dict(v) for k, v in r["bras"].items()}}; c["bras"]["F"]["promues"] = [3]; cas.append((c, "promotions"))
    d = {**r, "bras": {k: dict(v) for k, v in r["bras"].items()}}; d["bras"]["G"]["tirages"] = 4825; cas.append((d, "tirages"))
    e = {**r, "bras": {k: v for k, v in r["bras"].items() if k != "G"}}; cas.append((e, "bras joués"))
    for x, motif in cas:
        with pytest.raises(GardeArret, match=motif) as err:
            VT.verifier_generation(x, RAC)
        assert "[" not in str(err.value)                   # ni allocation ni valeur dans le message (mineur 9)


def test_regle_ebh_du_texte_egale_au_juge(J):
    rng = np.random.default_rng(4)
    for k in range(100):
        lw = np.cumsum(rng.normal(0.15 * (k % 3), 1.0, (24, 32)), axis=1).round(6)
        n = rng.integers(1, 33, 24)
        rev = [tuple(float(x) for x in lw[i, :n[i]]) for i in range(24)]
        promues, _, _ = R.promotions_ebh(J, rev)
        assert VT.ebh_du_texte([VT.log_e_du_texte(r) for r in rev]) == promues
