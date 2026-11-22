"""Tests (pytest) du lanceur v2, de la garde v2, du registre et de l'adaptateur : rejoue tous les cas de
`epreuves_lanceur_pilote_v2.py` (sains et artefacts, dont A1 à A10 de la contre-lecture de la v3) et quelques propriétés.
Faux fournisseur seulement ; aucun appel, aucun réseau. Usage : python -m pytest -q test_lanceur_pilote_essaim_v2.py"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epreuves_lanceur_pilote_v2 as E  # noqa: E402
import garde_pilote_essaim_v2 as GP  # noqa: E402
import lanceur_pilote_essaim_v2 as L  # noqa: E402
import registre_depense_v1 as RG  # noqa: E402


@pytest.fixture(scope="module")
def cas(tmp_path_factory):
    return E.jouer(str(tmp_path_factory.mktemp("lanceur") / "epreuves"))


def test_tous_les_cas_tenus(cas):
    casses = [c["cas"] for c in cas if not c.get("tenu")]
    assert not casses, casses


def test_aucun_sous_compte_hors_limite_declaree(cas):
    for c in cas:
        if "sous_compte" in c and c.get("limite_declaree") is None:
            assert not c["sous_compte"], c["cas"]


def test_attaques_a1_a10_presentes(cas):
    noms = " ".join(c["cas"] for c in cas)
    for a in ("A1 ", "A2 ", "A3 ", "A3b", "A3c", "A4 ", "A5 ", "A6 ", "A7 ", "A7b", "A8 ", "A9 ", "A10 "):
        assert a in noms, a


def test_borne(cas):
    b = GP.borne_pire(GP.plan_pstd(), GP.PRIX_GELES)
    assert b["appels_du_plan"] == 744 and b["echecs_au_plus"] == 74 and b["pire_usd"] == pytest.approx(203.9438, abs=1e-4)


def test_registre_jamais_recree(tmp_path):
    r = str(tmp_path / "r.jsonl")
    L.creer_registre(r)
    with pytest.raises(RG.RegistreRefuse):
        L.creer_registre(r)


def test_plan_gele():
    assert GP.empreinte_plan(GP.plan_pstd()) == GP.PLAN_SHA256


def test_execution_directe_refusee(tmp_path):
    assert L.main(["lanceur", str(tmp_path / "j.jsonl")]) == L.CODE_SANS_CLIENT
