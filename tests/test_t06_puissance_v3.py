"""Script de puissance conjointe de T6-1 (v3) : reproduit les effets minimaux du candidat 2, cas sain et artefacts (R5) ; déterministe."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "brouillons" / "T0.6-organismes-v0-v1-candidat2-pieces" / "puissance_t06_v3.py"
spec = importlib.util.spec_from_file_location("puissance_v3", SCRIPT)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


@pytest.mark.parametrize("sd, n, attendu", [(0.795, 64, 0.394), (0.795, 36, 0.525), (1.0, 64, 0.495), (1.0, 36, 0.660)])
def test_effets_minimaux_du_candidat_reproduits(sd, n, attendu):
    assert abs(p.effet_minimal(sd, n) - attendu) < 0.0006
    assert abs(p.puissance_une(p.effet_minimal(sd, n), sd, n) - 0.8) < 0.002


def test_puissance_conjointe_temoin_neutre_et_temoin_instruit():
    e = p.effet_minimal(0.795, 64)
    neutre = p.puissance_conjointe(e, e, 0.795, 64)
    instruit = p.puissance_conjointe(e, e - p.EFFET_TEMOIN_P3, 0.795, 64)
    assert 0.66 <= neutre <= 0.70 and 0.79 <= instruit <= 0.81              # ≈ 0,68 et ≈ 0,80 du candidat
    assert neutre < p.puissance_une(e, 0.795, 64) ** 1 and neutre > p.puissance_une(e, 0.795, 64) ** 2    # entre l'indépendance (0,64) et la comparaison seule
    assert p.puissance_conjointe(0.0, 0.0, 0.795, 64) < 0.01                  # effet nul : presque jamais les deux


def test_simulation_proche_de_l_exact_et_deterministe():
    e = p.effet_minimal(0.795, 64)
    a, b = p.simulee(e, e, 0.795, 64, "cle"), p.simulee(e, e, 0.795, 64, "cle")
    assert a == b and abs(a - p.puissance_conjointe(e, e, 0.795, 64)) < 0.04
    assert p.simulee(e, e, 0.795, 64, "autre") != a


def test_sortie_deterministe_par_processus():
    sorties = [subprocess.run([sys.executable, "-I", "-B", str(SCRIPT)], capture_output=True, text=True, timeout=300) for _ in range(2)]
    assert all(r.returncode == 0 for r in sorties) and sorties[0].stdout == sorties[1].stdout
    assert "0.394" in sorties[0].stdout and "0.525" in sorties[0].stdout and "0.495" in sorties[0].stdout and "0.660" in sorties[0].stdout


@pytest.mark.parametrize("appel", [lambda: p.erreur_type(0, 64), lambda: p.erreur_type(0.795, 1), lambda: p.effet_minimal(0.795, 64, alpha=1.5),
                                   lambda: p.effet_minimal(0.795, 64, puissance=0), lambda: p.puissance_conjointe(0.4, 0.4, 0.795, 64, rho=1.0)])
def test_artefacts_refuses(appel):
    with pytest.raises(ValueError):
        appel()
