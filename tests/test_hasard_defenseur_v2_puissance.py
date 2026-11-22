"""Pièce 6 — table de puissance simulée et test de mort 1 : verdicts, rejouabilité, script à petite taille."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

from controle_ia.hasard_defenseur_v2 import puissance_v2 as P
from controle_ia.hasard_defenseur_v2.erreurs_v2 import RefusPlan

RACINE = Path(__file__).resolve().parents[1]


def _g1_sain():
    return P.verdict_g1({0.0: 0.05, 0.3: 0.04, 0.8: 0.03})


def test_mort_1_cas_sain_accord_a_0_10_pres():
    v = P.verdict_mort_1(_g1_sain(), {k: t - 0.05 for k, t in P.TABLE_APPROXIMATION.items()})
    assert not v["mort_instrument"] and v["g1_dans_la_bande"]


def test_mort_1_artefact_desaccord_par_defaut():
    sim = dict(P.TABLE_APPROXIMATION)
    sim[(0.10, 300)] = 0.64 - 0.11
    assert P.verdict_mort_1(_g1_sain(), sim)["mort_instrument"]
    assert P.verdict_mort_1(P.verdict_g1({0.0: 0.02, 0.3: 0.04, 0.8: 0.03}), dict(P.TABLE_APPROXIMATION))["mort_instrument"]
    assert P.verdict_mort_1(P.verdict_g1({0.0: 0.05, 0.3: 0.07, 0.8: 0.03}), dict(P.TABLE_APPROXIMATION))["mort_instrument"]
    exces = dict(P.TABLE_APPROXIMATION)
    exces[(0.05, 300)] = 0.28 + 0.2
    v = P.verdict_mort_1(_g1_sain(), exces)
    assert not v["mort_instrument"] and v["exces_rapportes"] == ["delta=0.05 N=300"]  # excès : rapporté, sans mort


def test_aucun_repli_silencieux():
    sim = dict(P.TABLE_APPROXIMATION)
    del sim[(0.20, 150)]
    with pytest.raises(RefusPlan):
        P.verdict_mort_1(_g1_sain(), sim)
    with pytest.raises(RefusPlan):
        P.Cas("x", 301, P.params()).n_taches()
    with pytest.raises(RefusPlan):
        P.repliques(P.cas_g1(0.0), 0, 1, 0, 99)


def test_g5_verdicts():
    assert P.verdict_g5_sain(0.62, 0.64)["passe"]
    assert not P.verdict_g5_sain(0.55, 0.64)["passe"]
    assert not P.verdict_g5_sain(0.48, 0.50)["passe"]
    assert P.verdict_g5_artefact(0.06)["passe"] and not P.verdict_g5_artefact(0.07)["passe"]


def test_graines_repliques_rejouables_et_independantes_du_nombre_de_processus():
    cas = P.cas_puissance(0.10, 1.0, 150, 0.3)
    a = P.repliques(cas, 6, 77, 3, 99, processus=1)
    b = P.repliques(cas, 6, 77, 3, 99, processus=2)
    assert a == b
    assert P.repliques(cas, 6, 77, 4, 99) != a  # autre indice de cas : autres graines
    r0, m0 = P.entropies_replique(77, 3, 0)
    assert r0 != m0  # clés distinctes pour le tirage (racine) et le monde


def test_script_a_petite_taille(tmp_path):
    sortie = tmp_path / "s.json"
    cmd = [sys.executable, str(RACINE / "scripts" / "simulations_hasard_defenseur_v2.py"), "--entropie", "5",
           "--sortie", str(sortie), "--taille", "petite"]
    env = {"PYTHONPATH": str(RACINE / "src"), "PATH": "/usr/bin:/bin"}
    subprocess.run(cmd, check=True, capture_output=True, env=env, timeout=300)
    d = json.loads(sortie.read_text(encoding="utf-8"))
    assert d["taille"] == "petite" and len(d["puissance"]) == 90 and len(d["courbes_audit"]) == 22
    assert {"mort_1", "G1_verdict", "G5_sain", "G5_a", "G5_b", "courbes_audit_cas_sain"} <= set(d)
    r = subprocess.run(cmd, capture_output=True, env=env, timeout=60)
    assert r.returncode != 0  # refuse d'écraser
    r = subprocess.run(cmd[:2] + ["--sortie", str(tmp_path / "t.json"), "--taille", "petite"], capture_output=True, env=env, timeout=60)
    assert r.returncode != 0  # entropie obligatoire, sans défaut
