"""Essais de `audit_apres_coup_v1.regle_audit` (rang 3) : trois parts consignées ; π_min = 0 refusé."""
import numpy as np
import pytest

from controle_ia.audit_apres_coup_v1.regle_audit import (CONFIG_SANS_PLANCHER, RegleAudit, calibrer_gamma,
                                                       esperance_g_gaussienne_tronquee, g_identite, g_nulle)
from controle_ia.gardes import GardeArret


def test_trois_parts_et_sources():
    r = RegleAudit(0.01, 0.015, 0.1, g_identite, 1.6)
    s = np.array([1.0, 5.0, 25.0, 25.0])
    x = np.array([0.0, 0.5, 1.0, 0.2])
    p = r.parts(s, x)
    assert np.array_equal(p["part_enjeu"], 0.015 * s / 1.6)
    assert np.allclose(p["pi"], np.minimum(1, 0.01 + 0.015 * s / 1.6 + 0.1 * x))
    u = np.array([0.005, 0.02, 0.3, 0.9])
    aud, src = r.tirer(p, u)
    assert aud.tolist() == [True, True, True, False]
    assert src.tolist() == [1, 2, 3, 0]


def test_g_force_consigne():
    r = RegleAudit(0.01, 0.0, 0.5, g_identite, 1.0)
    p = r.parts(np.ones(2), np.array([0.8, 0.8]), g_force=np.array([True, False]))
    assert p["part_soupcon"].tolist() == [0.0, 0.4]


def test_artefact_pi_min_nul_refuse():
    with pytest.raises(GardeArret, match="π_min = 0"):
        RegleAudit(0.0, 0.015, 0.1, g_identite, 1.6)


def test_sans_plancher_seulement_en_configuration_de_comparaison():
    r = RegleAudit(0.0, 0.0, 0.1, g_identite, 1.6, configuration=CONFIG_SANS_PLANCHER)
    with pytest.raises(GardeArret, match="pas de borne"):
        r.exiger_borne()
    with pytest.raises(GardeArret):
        RegleAudit(0.0, 0.015, 0.1, g_identite, 1.6, configuration=CONFIG_SANS_PLANCHER)  # β > 0 refusé


def test_g_non_croissante_ou_parametre_absent_refuse():
    with pytest.raises(GardeArret, match="croissante"):
        RegleAudit(0.01, 0.0, 0.1, lambda x: 1 - x, 1.0)
    with pytest.raises(GardeArret):
        RegleAudit(0.01, None, 0.1, g_identite, 1.0)


def test_calibrage_de_gamma():
    eg = esperance_g_gaussienne_tronquee(g_identite, 0.2, 0.2)
    # moyenne d'une gaussienne tronquée à [0, 1], formule fermée
    from scipy import stats
    a, b = -1.0, 4.0
    ferme = 0.2 + 0.2 * (stats.norm.pdf(a) - stats.norm.pdf(b)) / (stats.norm.cdf(b) - stats.norm.cdf(a))
    assert abs(eg - ferme) < 1e-9
    g = calibrer_gamma(0.05, 0.01, 0.0, g_identite, 0.2, 0.2)
    assert abs(0.01 + g * eg - 0.05) < 1e-12
    with pytest.raises(GardeArret):
        calibrer_gamma(0.005, 0.01, 0.0, g_identite, 0.2, 0.2)
    with pytest.raises(GardeArret):
        calibrer_gamma(0.05, 0.01, 0.0, g_nulle, 0.2, 0.2)
