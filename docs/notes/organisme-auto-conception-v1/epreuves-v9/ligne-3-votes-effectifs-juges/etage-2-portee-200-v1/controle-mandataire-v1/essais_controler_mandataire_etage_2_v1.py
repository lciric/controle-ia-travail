"""Essais du contrôle du mandataire (règle R5 : chaque condition sur un cas sain et sur des artefacts)."""
import importlib.util
import json
import pathlib
import subprocess
import sys

import pytest

ICI = pathlib.Path(__file__).resolve().parent
PROGRAMME = ICI / "controler_mandataire_etage_2_v1.py"
_spec = importlib.util.spec_from_file_location("controler_mandataire_etage_2_v1", PROGRAMME)
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

SECRET = "MotDePasseSecret-9f3a"
HOTE_SECRET = "mandataire-prive.exemple"
VALEUR_SECRETE = f"http://utilisateur:{SECRET}@{HOTE_SECRET}:3128"
SAIN = {"HTTPS_PROXY": "http://mandataire.exemple:3128", "NO_PROXY": "localhost,127.0.0.1"}
CLES = {"https_proxy_non_vide", "no_proxy_couvre_127_0_0_1", "decision", "motifs"}


def ev(**surcharges):
    env = dict(SAIN)
    for k, v in surcharges.items():
        if v is None:
            env.pop(k, None)
        else:
            env[k] = v
    return C.evaluer(env)


# --- cas sain -------------------------------------------------------------------------------------------------------
def test_sain_tenu():
    r = ev()
    assert set(r) == CLES
    assert r == {**r, "https_proxy_non_vide": True, "no_proxy_couvre_127_0_0_1": True, "decision": "tenu"}
    assert any("« 127.0.0.1 »" in m for m in r["motifs"])


# --- (1) HTTPS_PROXY ------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("valeur", [None, "", "   ", " \t\n "], ids=["absente", "vide", "espaces", "blancs-melanges"])
def test_https_proxy_artefacts(valeur):
    r = ev(HTTPS_PROXY=valeur)
    assert r["https_proxy_non_vide"] is False and r["decision"] == "refus"
    assert r["no_proxy_couvre_127_0_0_1"] is True          # l'autre condition reste jugée à part


def test_https_proxy_minuscule_seule_ne_suffit_pas():
    r = ev(HTTPS_PROXY=None, https_proxy="http://mandataire.exemple:3128")
    assert r["https_proxy_non_vide"] is False and r["decision"] == "refus"


def test_https_proxy_minuscule_identique_tenu():
    r = ev(https_proxy=" http://mandataire.exemple:3128 ")
    assert r["decision"] == "tenu"


def test_https_proxy_minuscule_vide_refus():
    r = ev(https_proxy="  ")
    assert r["https_proxy_non_vide"] is False and r["decision"] == "refus"


def test_https_proxy_minuscule_differente_refus():
    r = ev(https_proxy="http://autre.exemple:8080")
    assert r["https_proxy_non_vide"] is False and r["decision"] == "refus"
    assert any("diffère" in m for m in r["motifs"])


# --- (2) NO_PROXY ---------------------------------------------------------------------------------------------------
def test_no_proxy_absente_refus():
    r = ev(NO_PROXY=None)
    assert r["no_proxy_couvre_127_0_0_1"] is False and r["decision"] == "refus"
    assert r["https_proxy_non_vide"] is True


@pytest.mark.parametrize("valeur", ["", "   ", " , ,, "], ids=["vide", "espaces", "virgules-seules"])
def test_no_proxy_vide_refus(valeur):
    r = ev(NO_PROXY=valeur)
    assert r["no_proxy_couvre_127_0_0_1"] is False and r["decision"] == "refus"


def test_no_proxy_sans_127_refus():
    r = ev(NO_PROXY="example.com,10.0.0.1,.interne")
    assert r["no_proxy_couvre_127_0_0_1"] is False and r["decision"] == "refus"


def test_no_proxy_localhost_seul_refus():
    r = ev(NO_PROXY="localhost")
    assert r["no_proxy_couvre_127_0_0_1"] is False and r["decision"] == "refus"
    assert any("localhost" in m for m in r["motifs"])


def test_no_proxy_espaces_autour_tenu():
    assert ev(NO_PROXY="  localhost ,  127.0.0.1  ")["decision"] == "tenu"


def test_plage_qui_couvre_reconnue_par_le_brief_mais_refusee_faute_d_urllib():
    assert C._element_couvrant_brief("localhost, 127.0.0.0/8") == ("127.0.0.0/8", "plage")
    assert C._urllib_contourne("localhost, 127.0.0.0/8") is False   # urllib ne lit pas les plages
    r = ev(NO_PROXY="localhost, 127.0.0.0/8")
    assert r["no_proxy_couvre_127_0_0_1"] is False and r["decision"] == "refus"
    assert any("127.0.0.0/8" in m and "plages" in m for m in r["motifs"])


def test_plage_qui_couvre_plus_element_exact_tenu():
    assert ev(NO_PROXY="127.0.0.0/8,127.0.0.1")["decision"] == "tenu"


def test_plage_qui_ne_couvre_pas_refus():
    assert C._element_couvrant_brief("10.0.0.0/8,192.168.0.0/16") == (None, None)
    r = ev(NO_PROXY="10.0.0.0/8,192.168.0.0/16")
    assert r["no_proxy_couvre_127_0_0_1"] is False and r["decision"] == "refus"


def test_etoile_valeur_entiere_tenu():
    r = ev(NO_PROXY="*")
    assert r["decision"] == "tenu"
    assert any("« * »" in m for m in r["motifs"])


@pytest.mark.parametrize("valeur", ["localhost,*", " * "], ids=["dans-une-liste", "entouree-d-espaces"])
def test_etoile_non_lue_par_urllib_refus(valeur):
    assert C._element_couvrant_brief(valeur)[1] == "etoile"
    r = ev(NO_PROXY=valeur)
    assert r["no_proxy_couvre_127_0_0_1"] is False and r["decision"] == "refus"


def test_suffixe_lu_par_urllib_hors_regle_refus():
    assert C._urllib_contourne("0.0.1") is True                    # urllib : « 127.0.0.1 » finit par « .0.0.1 »
    r = ev(NO_PROXY="0.0.1")
    assert r["no_proxy_couvre_127_0_0_1"] is False and r["decision"] == "refus"


def test_element_avec_port_refus():
    assert ev(NO_PROXY="127.0.0.1:8787")["decision"] == "refus"


# --- formes en minuscules -------------------------------------------------------------------------------------------
def test_no_proxy_minuscule_seule_tenu():
    assert ev(NO_PROXY=None, no_proxy="127.0.0.1")["decision"] == "tenu"


def test_no_proxy_minuscule_seule_sans_127_refus():
    assert ev(NO_PROXY=None, no_proxy="localhost")["decision"] == "refus"


def test_deux_formes_minuscule_vide_refus():
    r = ev(no_proxy="")                                        # urllib : la minuscule vide efface NO_PROXY
    assert r["no_proxy_couvre_127_0_0_1"] is False and r["decision"] == "refus"


def test_deux_formes_majuscule_sans_127_refus():
    assert ev(NO_PROXY="localhost", no_proxy="127.0.0.1")["decision"] == "refus"


def test_deux_formes_qui_couvrent_tenu():
    assert ev(NO_PROXY="127.0.0.1", no_proxy="localhost,127.0.0.1")["decision"] == "tenu"


# --- aucune fuite ---------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("env", [
    {"HTTPS_PROXY": VALEUR_SECRETE, "NO_PROXY": f"{HOTE_SECRET},127.0.0.1"},
    {"HTTPS_PROXY": VALEUR_SECRETE, "https_proxy": "http://autre.exemple:1", "NO_PROXY": f"{HOTE_SECRET}"},
    {"HTTPS_PROXY": VALEUR_SECRETE, "https_proxy": "", "NO_PROXY": "localhost"},
], ids=["tenu", "refus-difference", "refus-vide"])
def test_aucune_fuite_en_processus(env, capsys):
    C.main(env)
    sortie = capsys.readouterr()
    tout = sortie.out + sortie.err
    for interdit in (VALEUR_SECRETE, SECRET, HOTE_SECRET, "utilisateur", "autre.exemple"):
        assert interdit not in tout


def _lancer(env):
    return subprocess.run([sys.executable, "-I", "-B", str(PROGRAMME)], env=env, capture_output=True, text=True,
                          timeout=60)


def test_processus_tenu_code_0_sans_fuite():
    p = _lancer({"HTTPS_PROXY": VALEUR_SECRETE, "NO_PROXY": "localhost,127.0.0.1"})
    assert p.returncode == 0
    lignes = p.stdout.strip().splitlines()
    assert len(lignes) == 1
    r = json.loads(lignes[0])
    assert set(r) == CLES and r["decision"] == "tenu"
    for interdit in (VALEUR_SECRETE, SECRET, HOTE_SECRET):
        assert interdit not in p.stdout + p.stderr


def test_processus_refus_code_3_sans_fuite():
    p = _lancer({"HTTPS_PROXY": VALEUR_SECRETE, "NO_PROXY": "localhost"})
    assert p.returncode == 3
    r = json.loads(p.stdout.strip())
    assert r["decision"] == "refus" and r["https_proxy_non_vide"] is True
    for interdit in (VALEUR_SECRETE, SECRET, HOTE_SECRET):
        assert interdit not in p.stdout + p.stderr


def test_processus_environnement_vide_refus_code_3():
    p = _lancer({})
    assert p.returncode == 3
    r = json.loads(p.stdout.strip())
    assert r["https_proxy_non_vide"] is False and r["no_proxy_couvre_127_0_0_1"] is False


# --- erreur interne : refus déclaré, jamais un repli silencieux -----------------------------------------------------
class _EnvironnementCasse(dict):
    def get(self, *a, **k):
        raise RuntimeError(SECRET)


def test_erreur_interne_refus_sans_fuite(capsys):
    assert C.main(_EnvironnementCasse()) == 3
    sortie = capsys.readouterr().out
    r = json.loads(sortie)
    assert r["decision"] == "refus" and "RuntimeError" in r["motifs"][0]
    assert SECRET not in sortie
