"""E3 bis (GO-2026-11-07-08 : 3 USD de plus sur GO-2026-11-06-01, soit 8 USD pour E2, E3 et E3 bis cumulées) : le plafond d'épreuve est borné par `total − 0,1` où le total vaut 5 par
défaut et 8 seulement par `T06_GO_EPREUVES_TOTAL_USD=8`. Dépense antérieure d'E3 bis : 2,092 (E2 0,627 + E3 1,465). Cas sain et artefact (R5)."""
from __future__ import annotations

import json
import subprocess

import pytest

import test_t06_v11_amorce as t7
from controle_ia.t06 import session_v10 as s10
from controle_ia.t06.session import GardeSession
from test_t06_v11_nouveaux_v10 import LANCEUR9, _publier
from test_t06_v11_scripts import controles, env5, monde5, v5  # noqa: F401  (fixtures)
from test_t06_v11_amorce import bac, depot_session, src_epreuve  # noqa: F401  (fixtures de base)


@pytest.mark.parametrize("plafond, ant, total, ok", [
    ("5.7", "2.092", "8", True),          # le plafond proposé : 5,7 + 2,092 = 7,792 ≤ 7,9
    ("5.808", "2.092", "8", True),         # borne exacte : 7,9
    ("5.81", "2.092", "8", False),         # au-delà de total − 0,1
    ("5.7", "2.092", None, False),         # sans le total de 8 : le GO de 5 USD refuse (artefact : le défaut est inchangé)
    ("5.7", "2.092", "5", False),
    ("4.27", "0.627", None, True),         # E3 d'origine : inchangé
    ("1", "0", "9", False),                # tout autre total est refusé
    ("1", "0", "abc", False),
])
def test_plafond_epreuve_borne_par_le_total_du_go(plafond, ant, total, ok):
    if ok:
        assert "≤" in s10.verifier_plafond_epreuve(plafond, ant, total)
    else:
        with pytest.raises(GardeSession):
            s10.verifier_plafond_epreuve(plafond, ant, total)


def test_le_total_du_module_n_est_pas_laisse_modifie():
    from controle_ia.t06 import session_v8 as s8
    avant = s8.GO_EPREUVES_USD
    s10.verifier_plafond_epreuve("5.7", "2.092", "8")
    with pytest.raises(GardeSession):
        s10.verifier_plafond_epreuve("5.7", "2.092", "5")
    assert s8.GO_EPREUVES_USD == avant == "5"


def _controles(m, plafond, ant, total, nom):
    cfg = m["src"] / "prereg" / "config-epreuve-e2.json"
    c = json.loads(cfg.read_text(encoding="utf-8"))
    c["plafond_usd"] = plafond
    cfg.write_text(json.dumps(c), encoding="utf-8")
    _publier(m)
    sup = {"T06_DEPENSE_EPREUVES_ANTERIEURES_USD": ant}
    if total is not None:
        sup["T06_GO_EPREUVES_TOTAL_USD"] = total
    return subprocess.run(["bash", str(LANCEUR9), "controles-epreuve", str(m["tmp"] / nom), t7._git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e2.json"],
                          env=env5(m, **sup), capture_output=True, text=True, timeout=120)


@pytest.mark.parametrize("plafond, ant, total, ok", [(5.7, "2.092", "8", True), (5.7, "2.092", None, False), (5.82, "2.092", "8", False)])
def test_lanceur_controles_epreuve_e3_bis(monde5, plafond, ant, total, ok):
    r = _controles(monde5, plafond, ant, total, "bis")
    assert (r.returncode == 0) is ok, r.stdout + r.stderr
    if ok:
        assert f"plafond de l'épreuve {plafond} USD sur 8" in r.stdout and "≤ 7.9" in r.stdout
