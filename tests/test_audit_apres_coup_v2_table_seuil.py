"""Essais de `audit_apres_coup_v2.table_seuil` (rang 7, section 4) : bloc A retrouvé au quatrième chiffre ;
p > 1 jamais écrêté ; L ≥ K, q = 0, excès avec seuil fixe : refus."""
import pytest

from controle_ia.audit_apres_coup_v2.regle_audit import CONFIG_SANS_PLANCHER, RegleAudit, g_identite
from controle_ia.audit_apres_coup_v2.table_seuil import (PHRASE_EXCES, PHRASE_PAS_GARANTIE, table_exces,
                                                       table_signature)
from controle_ia.gardes import GardeArret

# Bloc A du calcul de l'attaquant informé (docs/notes/attaquant-informe-v1/calculs-attaquant-informe-v1.txt),
# écrit avant la première exécution : (K, q, L) -> p minimal à quatre chiffres.
BLOC_A = {
    (30, 1.0, 0): 0.0950, (30, 1.0, 20): 0.2589, (30, 0.5, 0): 0.1901, (30, 0.5, 20): 0.5177,
    (100, 1.0, 0): 0.0295, (100, 1.0, 20): 0.0368, (100, 0.5, 0): 0.0590, (100, 0.5, 20): 0.0735,
    (300, 1.0, 0): 0.0099, (300, 1.0, 20): 0.0106, (300, 0.5, 0): 0.0199, (300, 0.5, 20): 0.0213,
    (1000, 1.0, 0): 0.0030, (1000, 1.0, 20): 0.0031, (1000, 0.5, 0): 0.0060, (1000, 0.5, 20): 0.0061,
}


@pytest.mark.parametrize("cle", sorted(BLOC_A))
def test_bloc_A_retrouve_au_quatrieme_chiffre(cle):
    K, q, L = cle
    assert round(table_signature(K, q, L)["p"], 4) == BLOC_A[cle]


def test_etiquettes_moyennes():
    t = table_signature(30, 1.0, 20)
    assert round(t["etiquettes_moyennes"], 2) == 2.59
    assert round(30 * t["p"] * 1.0, 2) == 7.77  # K·p·q surestime dès que L > 0
    assert 2.9 < table_signature(1000, 1.0, 0)["etiquettes_moyennes"] < 3.0


def test_artefact_p_superieur_a_un_jamais_ecrete():
    t = table_signature(30, 0.5, 28)
    assert round(t["p"], 2) == 1.55
    assert t["phrase"] == PHRASE_PAS_GARANTIE


def test_budget_d_etiquettes_insuffisant():
    t = table_signature(300, 1.0, 0, budget_etiquettes=50, horizon=10_000)
    assert t["plancher_permis"] == 0.005 and t["phrase"] == PHRASE_PAS_GARANTIE
    assert table_signature(300, 1.0, 0, budget_etiquettes=200, horizon=10_000)["phrase"] is None


def test_refus():
    with pytest.raises(GardeArret):
        table_signature(30, 1.0, 30)
    with pytest.raises(GardeArret):
        table_signature(30, 0.0, 0)
    with pytest.raises(GardeArret, match=PHRASE_EXCES):
        table_exces(0.10, 10_000, 0.05, K=30)
    sans = RegleAudit(0.0, 0.0, 0.1, g_identite, 1.6, configuration=CONFIG_SANS_PLANCHER)
    with pytest.raises(GardeArret, match="pas de borne"):
        table_signature(300, 1.0, 0, regle=sans)


def test_exces_ordre_de_grandeur_et_declaration():
    """Bloc B de l'attaquant informé : d0 = 0,10, N = 10 000, p = 0,05 -> 312,1 épisodes en excès non vus."""
    t = table_exces(0.10, 10_000, 0.05)
    assert t["phrase"] == PHRASE_EXCES
    assert round(t["episodes_en_exces_non_vus"], 1) == 312.1
    assert "approximation normale" in t["marque"]
    t2 = table_exces(0.10, 10_000, 0.05, m=400)
    assert t2["episodes_en_exces_non_vus"] > t["episodes_en_exces_non_vus"]
    assert t2["declaration"]["m"] == 400 and t2["exces_jamais_vu"] > 0


def test_part_d_enjeu_au_type_le_plus_bas():
    r = RegleAudit(0.005, 0.015, 0.0, g_identite, 1.6)
    t = table_signature(300, 1.0, 0, regle=r, s_min=1.0)
    assert t["part_enjeu_au_type_le_plus_bas"] == pytest.approx(0.015 / 1.6)
    assert t["p"] == pytest.approx(1 - 0.05 ** (1 / 300))  # p reste le taux exigé du plancher, inchangé
