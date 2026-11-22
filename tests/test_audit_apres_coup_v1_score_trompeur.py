"""Essais du score trompeur planté (rang 10, section 3) : trois mondes, b = 0,05, π_min = 0,01, q = 1.
Tailles réduites dans les essais (seuils binomiaux exacts recalculés) ; tailles de la spécification dans
`simulations_longues`."""
import math

import pytest

from controle_ia.audit_apres_coup_v1.epreuves_boucle import epreuve_4
from controle_ia.audit_apres_coup_v1.estimateurs import STRATE_PLANCHER_SEUL
from controle_ia.audit_apres_coup_v1.oracle_simule import OracleSimule
from controle_ia.audit_apres_coup_v1.regle_audit import g_identite
from controle_ia.audit_apres_coup_v1.score_trompeur import (essai_delai, essai_gain, essai_validite, monde_sain,
                                                          monde_tenu_a_l_ecart, monde_trompeur, prix_orientation,
                                                          regle_orientee)

E = 20261122
SIG = OracleSimule(1.0, 0.0, 0, "signature")


def test_trompeur_validite_couverture_et_biais():
    m = monde_trompeur(40, E, 0.5, 0.02)
    r = regle_orientee(g_identite, m.mu0, m.sigma)
    out = essai_validite(m, r, SIG, R=300)
    assert out["couverture_tient"], out
    assert out["biais_nul"], out
    assert out["prix_orientation"] == pytest.approx(5.0)
    assert abs(out["budget_realise"] - 0.05) < 0.005  # budget réalisé rapporté (les endommagés ont g = 0)


def test_trompeur_delai_dans_la_borne_du_plancher():
    m = monde_trompeur(41, E, 0.5, 0.02)
    r = regle_orientee(g_identite, m.mu0, m.sigma)
    out = essai_delai(m, r, SIG, R=400)
    assert out["rang_n95"] == 299 and out["dans_la_borne"], out


def test_famille_tenue_a_l_ecart_sans_gain():
    m = monde_tenu_a_l_ecart(42, E, 1.0)
    r = regle_orientee(g_identite, m.mu0, m.sigma)
    out = essai_gain(m, r, SIG, R=1000, n=400, rang_lu=400)  # R = 4 000 dans `simulations_longues`
    assert out["sans_gain"], out
    assert out["erreur_type_relative"] == pytest.approx(math.sqrt(2) / math.sqrt(1000))


def test_score_informatif_gain_superieur_a_un():
    m = monde_sain(43, E, 0.1)
    r = regle_orientee(g_identite, m.mu0, m.sigma)
    out = essai_gain(m, r, SIG, R=300, n=4000, rang_lu=400)
    assert out["gain"] > 1 + 4 * out["erreur_type_relative"], out


def test_artefact_estimateur_naif_sur_audit_oriente_refuse():
    """Réglages du bloc B : 0,05 hors signal, 0,50 pour un signalé, rappel vrai 0,20 : le naïf (0,71) est refusé."""
    out = epreuve_4(E, r=0.20, p0=0.05, p1=0.50, N=40_000, strate_sans_score=STRATE_PLANCHER_SEUL)
    assert out["naif"] is None and "naïf" in out["refus_naif"]
    assert abs(out["strate_sans_score"] - 0.20) < 0.03
    assert abs(out["pondere"] - 0.20) < 0.02


def test_prix_de_l_orientation():
    assert prix_orientation(0.05, 0.01) == pytest.approx(5.0)
