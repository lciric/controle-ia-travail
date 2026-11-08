"""Configuration v5 et lanceur v5 (E3 du 7 novembre) : la configuration d'épreuve d'E3 (plafond 4,27) était refusée par `configuration_v4` au démarrage du run
(« plafond 4.27 : (1.5, 3.5) USD attendus ») ; la suite complète échouée l'avait masqué. Cas sain et artefact (R5)."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t06 import configuration_v4 as cf4
from controle_ia.t06 import configuration_v5 as cf5

D = Path(__file__).resolve().parents[1] / "docs" / "notes" / "g0-deux-semaines-v1"
RACINE = Path(__file__).resolve().parents[1]


def _epreuve(plafond):
    c = json.loads((D / "config-t06-epreuve-e3-v3.json").read_text(encoding="utf-8"))          # configuration d'épreuve réelle du dépôt (E3 v3, plafond 4,3)
    c["plafond_usd"] = plafond
    for k in ("taches_evaluation", "taches_distillation"):
        if c.get(k) and len(c[k]["sha256"]) != 64:
            c[k]["sha256"] = "a" * 64
    return c


@pytest.mark.parametrize("plafond", [1.5, 3.5, 4.27, 4.3, 5.7, 8, 8.0, 0.01])
def test_v5_accepte_un_plafond_d_epreuve_de_zero_a_huit(plafond):
    cf5.exiger_config_t06_v5(_epreuve(plafond))


@pytest.mark.parametrize("plafond", [0, -1, 8.01, 9, float("nan"), float("inf"), True, "4.27", None])
def test_v5_refuse_un_plafond_d_epreuve_hors_de_zero_a_huit(plafond):
    with pytest.raises(GardeArret, match="plafond"):
        cf5.exiger_config_t06_v5(_epreuve(plafond))


def test_artefact_la_v4_refuse_4_27_et_5_7_au_demarrage_du_run():
    for p in (4.27, 5.7):
        with pytest.raises(GardeArret, match=r"\(1.5, 3.5\)"):
            cf4.exiger_config_t06_v4(_epreuve(p))


def test_la_course_est_inchangee_v5_valide_la_configuration_reelle_comme_la_v4():
    c = json.loads((D / "config-t06-reel-v1-brouillon5.json").read_text(encoding="utf-8"))
    cf4.exiger_config_t06_v4(c)
    cf5.exiger_config_t06_v5(c)
    c["plafond_usd"] = 150                                                   # une configuration de course n'a pas la règle d'épreuve : sa validation (v3) reste celle de la v4
    with pytest.raises(GardeArret):
        cf4.exiger_config_t06_v4(c)
    with pytest.raises(GardeArret):
        cf5.exiger_config_t06_v5(c)


def test_le_lanceur_v5_ne_differe_du_v4_que_par_l_import_la_commande_et_la_note():
    a = (RACINE / "src" / "controle_ia" / "t06" / "lanceur_v4.py").read_text(encoding="utf-8").splitlines()
    b = (RACINE / "src" / "controle_ia" / "t06" / "lanceur_v5.py").read_text(encoding="utf-8").splitlines()
    diff = [(x, y) for x, y in zip(a, b[1:]) if x != y]
    assert len(b) == len(a) + 1 and b[0].startswith("# [v5") and len(diff) == 2, diff
    assert "configuration_v5" in diff[0][1] and "lanceur_v5" in diff[1][1]


def test_configuration_d_e3_bis_seul_le_plafond_change_et_elle_passe_la_validation_v5():
    b = json.loads((D / "config-t06-epreuve-e3bis-v1.json").read_text(encoding="utf-8"))
    cf5.exiger_config_t06_v5(b)
    assert b["plafond_usd"] == 5.7 and b["go_id"] == "GO-2026-11-06-01" and b["offre"]["etiquette"] == "t06-e3" and b["offre"]["stockage_max_usd_h"] == 0.08
    assert b["offre"]["telechargement_max_usd_go"] == 0.03 and b["mode"] == "reel" and b["calendrier"] == {"dernier_jour_creation": "2026-11-09", "fin_go_utc": "2026-11-11T00:00:00Z"}
    from controle_ia.t06 import session_v10 as s10
    assert "≤ 7.9" in s10.verifier_plafond_epreuve(b["plafond_usd"], "2.092", "8")
