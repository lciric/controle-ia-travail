"""Tests (pytest) du lanceur v3 et du registre v2 : rejoue tous les cas de `epreuves_lanceur_pilote_v3.py` (sains,
artefacts, attaques A1 à A10, N1 à N5, V3a et V4a), plus quelques propriétés. Faux fournisseur ; aucun appel, aucun réseau.
Usage : python -m pytest -q test_lanceur_pilote_essaim_v3.py"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epreuves_lanceur_pilote_v3 as E  # noqa: E402
import garde_pilote_essaim_v2 as GP  # noqa: E402
import lanceur_pilote_essaim_v3 as L  # noqa: E402
import registre_depense_v2 as RG  # noqa: E402


@pytest.fixture(scope="module")
def cas(tmp_path_factory):
    return E.jouer(str(tmp_path_factory.mktemp("lanceur-v3") / "epreuves"))


def test_tous_les_cas_tenus(cas):
    assert not [c["cas"] for c in cas if not c.get("tenu")]


def test_limites_declarees_seulement_v3a_v4a_a8_facture_cachee(cas):
    lim = sorted(c["cas"][:3] for c in cas if c.get("limite_declaree"))
    assert lim == ["A8 ", "V3a", "V4a", "rée"], lim


def test_aucun_sous_compte_hors_limite(cas):
    for c in cas:
        if "sous_compte" in c and not c.get("limite_declaree"):
            assert not c["sous_compte"], c["cas"]


def test_chemin_du_registre_ecrit_en_dur():
    assert L.REGISTRE_PILOTE_REL == "runs/pilote-essaim-pstd/registre-depense-v2.jsonl"
    assert L.CHEMINS_PILOTE.registre.endswith(L.REGISTRE_PILOTE_REL)
    assert list(L.TRANSPORTS_ADMIS_PILOTE) == [("transport_kimi_reel_v1", "TransportKimiReel")]
    assert list(L.ADAPTATEURS_ADMIS_PILOTE) == [("adaptateur_kimi_strict_v1", "AdaptateurKimiStrict")]


def test_verrou_exclusif(tmp_path):
    ch = RG.Chemins(str(tmp_path / "r.jsonl"), str(tmp_path / "e" / "a.json"), str(tmp_path / "e" / "c"))
    L.creer_registre(ch)
    r1 = RG.Registre(ch, L.parametres, L.borne())
    with pytest.raises(RG.RegistreRefuse) as ex:
        RG.Registre(ch, L.parametres, L.borne())
    assert ex.value.code == 25
    r1.fermer()
    RG.Registre(ch, L.parametres, L.borne()).fermer()


def test_borne():
    assert GP.borne_pire(GP.plan_pstd(), GP.PRIX_GELES)["pire_usd"] == pytest.approx(203.9438, abs=1e-4)


def test_execution_directe_refusee(tmp_path):
    assert L.main(["lanceur", str(tmp_path / "j.jsonl")]) == L.CODE_SANS_CLIENT
