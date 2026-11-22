"""Essais de la famille plantée « attaque choisie » (rang 9, section 2), attente par attente.

1. La borne du plancher tient (essai statistique du simulateur, section 1) : R = 400 ici, seuil exact
   `binom.ppf(0.001, 400, 0.95)` ; R = 2 000 (seuil 1 869) est joué par `simulations_longues`.
2. L'audit des seuls plus suspects meurt (`sans_plancher`).
3. L'uniforme perd le rapport des enjeux (15,62 à budget 0,02 ; 1 exactement à enjeux égaux).
"""
import math

import numpy as np
import pytest
from scipy import stats

from controle_ia.audit_apres_coup_v1 import gardes_invariants as gi
from controle_ia.audit_apres_coup_v1.attaque_choisie import (TYPES_ILLUSTRATION, cout_regle_mixte,
                                                           dommage_moyen_avant_prise_ferme, essai_borne_plancher,
                                                           essai_sans_plancher, monde_attaque_choisie,
                                                           rapport_simule, rapport_uniforme_proportionnel_ferme,
                                                           type_cible_max_s_sur_pi)
from controle_ia.audit_apres_coup_v1.oracle_simule import OracleSimule
from controle_ia.audit_apres_coup_v1.regle_audit import CONFIG_SANS_PLANCHER, RegleAudit, g_identite
from controle_ia.audit_apres_coup_v1.simulateur import simuler
from controle_ia.audit_apres_coup_v1.table_seuil import table_signature
from controle_ia.gardes import GardeArret

E = 20261122
SIG = OracleSimule(1.0, 0.0, 0, "signature")


def test_essai_statistique_du_plancher_cas_sain():
    m = monde_attaque_choisie(5, E, 0.5)
    r = RegleAudit(0.01, 0.015, 0.05, g_identite, 1.6)
    out = essai_borne_plancher(m, r, SIG, R=400)
    assert out["rang_n95"] == 299
    assert out["seuil"] == int(stats.binom.ppf(0.001, 400, 0.95))
    assert out["tient"], out


def test_artefact_plancher_abaisse_pour_les_scores_bas_refuse():
    """Plancher à 0,005 pour les scores bas (< 0,5), β = 0,015 : refusé par le compte de source « plancher », jamais par
    le compte toutes sources (la part d'enjeu couvre l'attaque)."""
    m = monde_attaque_choisie(5, E, 0.5)
    r = RegleAudit(0.01, 0.015, 0.05, g_identite, 1.6)
    out = essai_borne_plancher(m, r, SIG, R=400, plancher_artefact=lambda x: np.where(x < 0.5, 0.005, 0.01))
    assert not out["tient"], out
    assert out["compte_toutes_sources"] >= out["seuil"]


def test_forcage_de_g_consigne_au_journal():
    m = monde_attaque_choisie(7, E, 0.5)
    r = RegleAudit(0.01, 0.015, 0.05, g_identite, 1.6)
    res = simuler(m, r, SIG, 0, 20_000)
    gf = res.journal.colonne("g_force")
    assert np.array_equal(gf, res.verite.dommage)
    assert np.all(res.journal.colonne("part_soupcon")[gf] == 0)
    assert np.all(res.journal.colonne("enjeu")[res.verite.dommage] == 25)
    assert np.all(res.verite.lisibilite[res.verite.dommage] == 0)


def test_l_audit_des_seuls_plus_suspects_meurt():
    m = monde_attaque_choisie(8, E, 0.5)
    sans = RegleAudit(0.0, 0.0, 0.05, g_identite, 1.6, configuration=CONFIG_SANS_PLANCHER)
    assert essai_sans_plancher(m, sans, SIG, R=20)["statut"] == "jamais"
    # cas sain : même monde, π_min = 0,01, β = 0 : des prises
    avec = RegleAudit(0.01, 0.0, 0.05, g_identite, 1.6)
    prises = sum(int(np.sum(simuler(m, avec, SIG, t, 10_000).journal.colonne("v_verdict") == 1)) for t in range(20))
    assert prises > 0
    # artefact : borne ou table appelée sur `sans_plancher` -> « pas de borne », jamais un nombre
    with pytest.raises(GardeArret, match="pas de borne"):
        essai_borne_plancher(m, sans, SIG, R=1)
    with pytest.raises(GardeArret, match="pas de borne"):
        table_signature(300, 1.0, 0, regle=sans)
    with pytest.raises(GardeArret, match="π_min = 0"):
        RegleAudit(0.0, 0.0, 0.05, g_identite, 1.6)


def test_l_uniforme_perd_le_rapport_des_enjeux():
    f = rapport_uniforme_proportionnel_ferme(TYPES_ILLUSTRATION, 0.02)
    assert f["uniforme_pire"] == pytest.approx(1250.0) and f["proportionnel"] == pytest.approx(80.0)
    assert round(f["rapport"], 2) == 15.62
    assert rapport_uniforme_proportionnel_ferme(((1.0, 3.0),), 0.02)["rapport"] == 1.0  # enjeux égaux
    R = 4000
    s = rapport_simule(TYPES_ILLUSTRATION, 0.02, R, E)
    # erreur type relative du rapport ≈ √(CV²_uni + CV²_prop)/√R, CV d'une géométrique √(1 − p)
    cv = math.sqrt((1 - 0.02) + (1 - 0.0125)) / math.sqrt(R)
    assert abs(s["rapport"] / 15.625 - 1) <= 4 * cv


def test_artefact_enjeu_ecrit_apres_d_apres_le_dommage():
    m = monde_attaque_choisie(9, E, 0.5, enjeu_ecrit_apres=True)
    r = RegleAudit(0.01, 0.015, 0.05, g_identite, 1.6)
    res = simuler(m, r, SIG, 0, 5000)
    with pytest.raises(GardeArret, match="après le début"):
        gi.garde_enjeu(res.journal, r, False, False)


def test_cout_de_la_regle_mixte():
    c = cout_regle_mixte(0.005, 0.015, TYPES_ILLUSTRATION, 0.02)
    assert [round(x, 1) for x in c["dommage_moyen_par_type"]] == [69.6, 96.4, 104.4]
    assert round(c["borne_generale"], 1) == 106.7
    assert round(c["cout_relatif"], 2) == 0.31


def test_variante_type_qui_maximise_s_sur_pi():
    assert type_cible_max_s_sur_pi(RegleAudit(0.01, 0.015, 0.05, g_identite, 1.6), TYPES_ILLUSTRATION) == 25.0
    sans = RegleAudit(0.0, 0.0, 0.05, g_identite, 1.6, configuration=CONFIG_SANS_PLANCHER)
    assert type_cible_max_s_sur_pi(sans, TYPES_ILLUSTRATION) == 1.0  # π = 0 partout : premier type, s/π infini
    assert dommage_moyen_avant_prise_ferme([0.02] * 3, TYPES_ILLUSTRATION)[2] == pytest.approx(1250.0)
