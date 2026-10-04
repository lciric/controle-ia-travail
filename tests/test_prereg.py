import pytest

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste
from controle_ia.prereg import SECTIONS, exiger_prereg_scelle, problemes, sceller_prereg
from controle_ia.scellement import sceller


def ecrire(chemin, remplir=True, sauf=None):
    corps = ["# Préenregistrement test\n"]
    for s in SECTIONS:
        if s == sauf:
            continue
        corps.append(f"## {s}\n\n{'contenu ' + s if remplir else 'À REMPLIR'}\n")
    chemin.write_text("\n".join(corps), encoding="utf-8")
    return chemin


def test_sain_prereg_conforme(tmp_path):
    p = ecrire(tmp_path / "p.md")
    assert problemes(p) == []
    h = sceller_prereg(p)
    assert exiger_prereg_scelle(p) == h


def test_artefact_gabarit_non_rempli(tmp_path):
    p = ecrire(tmp_path / "p.md", remplir=False)
    assert len(problemes(p)) == len(SECTIONS)
    with pytest.raises(GardeArret, match="R1"):
        sceller_prereg(p)


def test_artefact_section_absente(tmp_path):
    p = ecrire(tmp_path / "p.md", sauf="Liste d'arrêt")
    with pytest.raises(GardeArret, match="Liste d'arrêt"):
        sceller_prereg(p)


def test_artefact_scelle_par_contournement_mais_non_conforme(tmp_path):
    p = ecrire(tmp_path / "p.md", sauf="Contre-lecture")
    sceller(p)  # scellé sans passer par sceller_prereg
    with pytest.raises(GardeArret, match="non conforme"):
        exiger_prereg_scelle(p)


def test_artefact_prereg_modifie_apres_scellement(tmp_path):
    p = ecrire(tmp_path / "p.md")
    sceller_prereg(p)
    p.write_text(p.read_text() + "\najout tardif\n")
    with pytest.raises(GardeArret, match="empreinte"):
        exiger_prereg_scelle(p)


def test_run_decisif_rattache_au_prereg(depot):
    p = ecrire(depot / "prereg.md")
    h = sceller_prereg(p)
    committer(depot)
    _, m = creer_manifeste(depot, "20261004-120000-decisif", {}, ["t"], decisif=True, prereg=p)
    assert m["preenregistrement"]["sha256"] == h
