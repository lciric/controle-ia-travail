"""Correctif 0023 : coupure effective de la machine = plafond de la ligne − dépense antérieure vraie (GO-2026-11-22-77, option (b)).

Cas sains : dépense antérieure 0, 5, 5,52, 9,65 et 16,22 USD sous une ligne de 60 et une configuration de 55 (avant 0023, tout
au-delà de 5 était refusé). Artefacts : dépense antérieure ≥ ligne, configuration > ligne, valeurs illisibles, négatives ou non
finies, ligne échue ou révoquée. Composition avec la garde de dépense (`session_v3 depense`) : le total ne dépasse jamais la ligne,
et la machine ne dépense jamais plus que le plafond scellé de la configuration. Lanceur : `--verifier-go-seulement` de bout en bout
(cas sain et artefact), et la création passe le plafond total, non le plafond de la configuration, à la garde de dépense.
"""
from __future__ import annotations

import os
import re
import subprocess
from decimal import Decimal
from pathlib import Path

import pytest

from controle_ia.iib import session_v5 as s5
from controle_ia.t06 import session_v3 as s3
from controle_ia.t06.session import GardeSession
from test_iib_scripts_v1 import ECHU, REVOQUE, SAIN, lignes_go

DEPOT = Path(__file__).resolve().parents[1]
LANCEUR = DEPOT / "scripts" / "lancer_iib_v3.sh"
SESSION = re.search(r'^SESSION="(.+)"$', LANCEUR.read_text(encoding="utf-8"), re.M).group(1).replace("$DEPOT", str(DEPOT))
SESSION3 = re.search(r'^SESSION3="(.+)"$', LANCEUR.read_text(encoding="utf-8"), re.M).group(1).replace("$DEPOT", str(DEPOT))


@pytest.fixture
def reg(tmp_path):
    f = tmp_path / "go.md"
    f.write_text(lignes_go(), encoding="utf-8")
    return f


@pytest.mark.parametrize("anterieure, total, machine", [("0", "55", "55"), ("5", "60", "55"), ("5.52", "60", "54.48"),
                                                         ("9.65", "60", "50.35"), ("16.22", "60", "43.78"), ("59.99", "60", "0.01")])
def test_cas_sains_coupure_effective(reg, anterieure, total, machine):
    r = s5.coupure_effective(reg, SAIN, "55", anterieure)
    assert r["plafond_total_usd"] == Decimal(total) and r["coupure_machine_usd"] == Decimal(machine)
    assert r["coupure_machine_usd"] <= Decimal("55") and r["plafond_total_usd"] <= Decimal("60")
    assert "correctif 0023" in r["plafond_verifie"]


@pytest.mark.parametrize("plafond, anterieure, motif", [("55", "60", "≥ plafond de la ligne"), ("55", "60.01", "≥ plafond de la ligne"),
                                                        ("55", "1000", "≥ plafond de la ligne"), ("61", "0", "> plafond de la ligne"),
                                                        ("55", "-1", "≥ 0 exigé"), ("0", "1", "> 0 exigé"), ("55", "nan", "non fini"),
                                                        ("55", "inf", "non fini"), ("55", "x", "illisible"), ("abc", "0", "illisible")])
def test_artefacts_refuses(reg, plafond, anterieure, motif):
    with pytest.raises(GardeSession, match=re.escape(motif)):
        s5.coupure_effective(reg, SAIN, plafond, anterieure)


@pytest.mark.parametrize("go", [ECHU, REVOQUE, "GO-2099-01-01-09"])
def test_ligne_echue_revoquee_ou_absente_refusee(reg, go):
    with pytest.raises(GardeSession):
        s5.coupure_effective(reg, go, "55", "9.65")


def _py(*args):
    return subprocess.run(["python3", "-I", "-B", "-c", *args], capture_output=True, text=True, timeout=60)


def test_ligne_de_commande_go_et_plafond_total(reg):
    r = _py(SESSION, "go", str(reg), SAIN, "55", "9.65")
    assert r.returncode == 0 and "coupure effective de la machine 50.35" in r.stdout and "total 60 ≤ 60" in r.stdout, r.stdout + r.stderr
    r = _py(SESSION, "plafond-total", str(reg), SAIN, "55", "9.65")
    assert r.returncode == 0 and r.stdout.strip() == "60"
    r = _py(SESSION, "plafond-total", str(reg), SAIN, "55", "0")
    assert r.returncode == 0 and r.stdout.strip() == "55"
    # artefacts : code 1, motif sur la dernière ligne, rien sur la sortie qui ressemble à un nombre
    for args in (("55", "60"), ("61", "0"), ("55", "-0.5")):
        r = _py(SESSION, "plafond-total", str(reg), SAIN, *args)
        assert r.returncode == 1 and not re.fullmatch(r"[0-9.]+", r.stdout.strip()), r.stdout
    r = _py(SESSION, "go", str(reg), SAIN, "55")
    assert r.returncode == 2 and "usage" in r.stderr
    # les autres sous-commandes restent celles de session_v1
    r = _py(SESSION, "plafond-ligne", str(reg), SAIN)
    assert r.returncode == 0 and r.stdout.strip() == "60"


@pytest.mark.parametrize("anterieure", ["0", "5.52", "9.65", "16.22"])
def test_composition_avec_la_garde_de_depense_total_jamais_au_dela_de_la_ligne(reg, anterieure):
    total = s5.coupure_effective(reg, SAIN, "55", anterieure)["plafond_total_usd"]
    cree, prix_c, prix_s, tel = 1_800_000_000, 1.30, 0.08, 0.03
    d = s3.depense_cumulee_v3(str(total), prix_c, prix_s, cree, anterieure, tel, cree)
    epuisement = d["epuisement_utc_s"]
    machine_a_l_epuisement = (epuisement - cree) / 3600.0 * (prix_c + prix_s)
    assert float(anterieure) + tel + machine_a_l_epuisement <= 60.0 + 1e-6
    assert machine_a_l_epuisement <= 55.0 + 1e-6
    # une seconde après l'épuisement, la garde arrête
    apres = s3.depense_cumulee_v3(str(total), prix_c, prix_s, cree, anterieure, tel, epuisement + 2)
    assert apres["arret"]


def test_lanceur_verifier_go_seulement_cas_sain_et_artefact(reg, tmp_path):
    base = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(tmp_path), "LANG": "C.UTF-8", "GO_ID": SAIN, "IIB_REGISTRE_GO": str(reg)}
    r = subprocess.run(["bash", str(LANCEUR), "--verifier-go-seulement", "55", "9.65"], env=base, capture_output=True, text=True, timeout=60)
    assert r.returncode == 0 and "GO VÉRIFIÉ, RIEN CRÉÉ" in r.stdout and "coupure effective de la machine 50.35" in r.stdout, r.stdout + r.stderr
    r = subprocess.run(["bash", str(LANCEUR), "--verifier-go-seulement", "55", "60"], env=base, capture_output=True, text=True, timeout=60)
    assert r.returncode == 2 and "refusé" in r.stdout


def test_creation_passe_le_plafond_total_a_la_garde_de_depense():
    src = LANCEUR.read_text(encoding="utf-8")
    bloc = src[src.index("\ncreation)\n"):src.index("\napres-creation)\n")]
    i_go, i_tot, i_dep = bloc.index('"$SESSION" go "$REG" "$GOC" "$PLC" "$ANT"'), bloc.index('PTOT=$(python3 -I -B -c "$SESSION" plafond-total "$REG" "$GOC" "$PLC" "$ANT")'), bloc.index('"$SESSION3" depense "$PTOT"')
    assert i_go < i_tot < i_dep
    assert '"$SESSION3" depense "$PLC"' not in src and '"$DEP" "$PTOT"' in bloc
    # la surveillance lit le plafond total enregistré à la création (champ plafond_creation), qu'elle passe à la garde de dépense
    assert 'PLC=$(champ plafond_creation "$D/lancement.txt")' in src and '"$SESSION3" surveillance "$PLC"' in src


def test_plafond_total_ecrit_exact_jamais_arrondi(reg):
    """Artefact de la contre-lecture : antérieure à décimales nombreuses ; l'écriture du total ne s'arrondit jamais vers le haut."""
    r = _py(SESSION, "plafond-total", str(reg), SAIN, "55", "3.123456")
    assert r.returncode == 0 and r.stdout.strip() == "58.123456", r.stdout
    assert Decimal(r.stdout.strip()) - Decimal("3.123456") <= Decimal("55")
    r = _py(SESSION, "plafond-total", str(reg), SAIN, "55", "0.1234567891")
    assert r.returncode == 0 and r.stdout.strip() == "55.1234567891"
    r = _py(SESSION, "plafond-total", str(reg), SAIN, "55", "60")
    assert r.returncode == 1 and "≥ plafond de la ligne 60 " in r.stdout
