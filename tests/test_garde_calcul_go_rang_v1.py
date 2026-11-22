"""Garde de calcul : rang de GO à deux ou trois chiffres (R-5013). Cas sains et artefacts (R5).

Avant la correction, les expressions GO_ID et LIGNE_GO n'admettaient que deux chiffres de rang : un GO de rang 100
et plus était invisible au registre et toute commande qui en citait un était refusée. Le rang de quatre chiffres ou
plus reste refusé. Registre factice en répertoire temporaire, comme tests/test_garde_calcul.py.
"""
import json
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

HOOK = Path(__file__).resolve().parents[1] / ".claude" / "hooks" / "garde_calcul.py"
AUJ = date.today()
AVANT = AUJ - timedelta(days=1)
APRES = AUJ + timedelta(days=10)
ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"


def ligne(ident, accorde=AVANT, echeance=APRES, typ="calcul", par="Lazar", perimetre="phase 0"):
    return f"| {ident} | {accorde} | {typ} | {perimetre} | 150 USD | {echeance} | {par} | message |\n"


@pytest.fixture
def racine(tmp_path):
    (tmp_path / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(HOOK, tmp_path / ".claude" / "hooks" / "garde_calcul.py")
    (tmp_path / "registres").mkdir()
    return tmp_path


def registre(racine, contenu):
    (racine / "registres" / "go.md").write_text("# GO\n\n" + ENTETE + contenu, encoding="utf-8")


def lancer(racine, commande):
    entree = json.dumps({"tool_name": "Bash", "tool_input": {"command": commande}})
    r = subprocess.run([sys.executable, str(racine / ".claude" / "hooks" / "garde_calcul.py")],
                       input=entree, capture_output=True, text=True)
    return r.returncode, r.stderr


RANG2 = "GO-2026-11-22-75"
RANG3 = "GO-2026-11-22-117"
RANG3_AUTRE = "GO-2026-11-22-124"


# --- cas sains ---------------------------------------------------------------------------------------------------------

def test_sain_rang_deux_present(racine):
    registre(racine, ligne(RANG2) + ligne(RANG3))
    code, err = lancer(racine, f"GO_ID={RANG2} vastai create instance 123 --image pytorch")
    assert code == 0, err


def test_sain_rang_trois_present(racine):
    registre(racine, ligne(RANG2) + ligne(RANG3))
    code, err = lancer(racine, f"GO_ID={RANG3} vastai create instance 123 --image pytorch")
    assert code == 0, err


def test_sain_rang_trois_sans_echeance_hors_calcul_n_empeche_pas_la_lecture(racine):
    # une ligne de rang 3 de type décision à échéance « — » est lue sans arrêt (forme admise, comme au rang 2)
    registre(racine, ligne(RANG3) + ligne("GO-2026-11-22-122", echeance="—", typ="décision"))
    code, err = lancer(racine, f"GO_ID={RANG3} vastai create instance 123")
    assert code == 0, err


# --- artefacts ---------------------------------------------------------------------------------------------------------

def test_artefact_rang_trois_absent(racine):
    registre(racine, ligne(RANG2) + ligne(RANG3))
    code, err = lancer(racine, f"GO_ID={RANG3_AUTRE} vastai create instance 123")
    assert code == 2
    assert f"{RANG3_AUTRE} absent" in err


def test_artefact_rang_trois_ne_se_confond_pas_avec_son_prefixe_de_rang_deux(racine):
    # le registre porte GO-…-11 ; la commande cite GO-…-117 : il ne doit pas être pris pour GO-…-11
    registre(racine, ligne("GO-2026-11-22-11"))
    code, err = lancer(racine, f"GO_ID={RANG3} vastai create instance 123")
    assert code == 2
    assert f"{RANG3} absent" in err


@pytest.mark.parametrize("ident", ["GO-2026-11-22-1170", "GO-2026-11-22-10000"])
def test_artefact_rang_quatre_cite_refuse(racine, ident):
    # le registre porte une ligne de même rang (invisible : ignorée) et le préfixe de rang 3 (qui ne doit pas servir)
    registre(racine, ligne(ident) + ligne(RANG3) + ligne("GO-2026-11-22-100"))
    code, err = lancer(racine, f"GO_ID={ident} vastai create instance 123")
    assert code == 2
    assert "sans identifiant de GO" in err


def test_artefact_rang_trois_echeance_illisible_refuse_tout(racine):
    # le registre entier est lu : une ligne de rang 3 mal formée bloque aussi un GO de rang 2 valide
    registre(racine, ligne(RANG2) + ligne(RANG3, echeance="réinitialisation hebdomadaire"))
    for ident in (RANG2, RANG3):
        code, err = lancer(racine, f"GO_ID={ident} vastai create instance 123")
        assert code == 2
        assert "mal formé" in err and "dates illisibles" in err


def test_artefact_rang_trois_colonnes_manquantes_refuse(racine):
    registre(racine, ligne(RANG2) + f"| {RANG3} | {AVANT} | calcul | phase 0 | {APRES} | Lazar | message |\n")
    code, err = lancer(racine, f"GO_ID={RANG2} vastai create instance 123")
    assert code == 2
    assert "8 colonnes attendues" in err


def test_artefact_rang_trois_calcul_sans_echeance_refuse(racine):
    # « — » n'est admis que hors calcul : un GO de calcul de rang 3 sans échéance rend le registre illisible
    registre(racine, ligne(RANG3, echeance="—"))
    code, err = lancer(racine, f"GO_ID={RANG3} vastai create instance 123")
    assert code == 2
    assert "dates illisibles" in err


def test_artefact_rang_trois_doublon_refuse(racine):
    registre(racine, ligne(RANG3) + ligne(RANG3))
    code, err = lancer(racine, f"GO_ID={RANG3} vastai create instance 123")
    assert code == 2
    assert "en double" in err


def test_artefact_rang_trois_revoque(racine):
    registre(racine, ligne(RANG3) + ligne("GO-2026-11-22-118", typ="révocation", perimetre=f"révoque {RANG3}"))
    code, err = lancer(racine, f"GO_ID={RANG3} vastai create instance 123")
    assert code == 2
    assert "révoqué par GO-2026-11-22-118" in err


def test_artefact_rang_trois_hors_periode(racine):
    registre(racine, ligne(RANG3, accorde=AUJ - timedelta(days=20), echeance=AUJ - timedelta(days=1)))
    code, err = lancer(racine, f"GO_ID={RANG3} vastai create instance 123")
    assert code == 2
    assert "hors de sa période" in err


def test_artefact_rang_trois_non_calcul(racine):
    registre(racine, ligne(RANG3, typ="décision"))
    code, err = lancer(racine, f"GO_ID={RANG3} vastai create instance 123")
    assert code == 2
    assert "pas « calcul »" in err


# --- expressions, directement ------------------------------------------------------------------------------------------

def _module():
    import importlib.util
    s = importlib.util.spec_from_file_location("garde_calcul_rang", HOOK)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_expressions_bornes():
    g = _module()
    assert g.GO_ID.findall("GO_ID=GO-2026-11-22-75 x") == ["GO-2026-11-22-75"]
    assert g.GO_ID.findall("GO_ID=GO-2026-11-22-117 x") == ["GO-2026-11-22-117"]
    assert g.GO_ID.findall("GO_ID=GO-2026-11-22-1170 x") == []
    assert g.GO_ID.findall("GO_ID=GO-2026-11-22-7 x") == []
    assert g.LIGNE_GO.match("| GO-2026-11-22-117 | 2026-11-22 |").group(1) == "GO-2026-11-22-117"
    assert g.LIGNE_GO.match("| GO-2026-11-22-75 | 2026-11-22 |").group(1) == "GO-2026-11-22-75"
    assert g.LIGNE_GO.match("| GO-2026-11-22-1170 | 2026-11-22 |") is None
    assert g.LIGNE_GO.match("| GO-2026-11-22-7 | 2026-11-22 |") is None
