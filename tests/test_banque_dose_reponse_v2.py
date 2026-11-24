"""Essais de la version 2 de la consigne d'enveloppe de l'extracteur (étape 2b : relecture de l'énoncé contre la liste
de l'invite H.9) et des modules qui la servent : garde de la consigne sur un cas sain et sur trois artefacts (R5), et
préparation d'une tentative dans un dépôt jetable, dont chaque dossier d'agent reçoit la version 2."""
import re
import shutil
from pathlib import Path

import pytest

from conftest import committer
from controle_ia.environnements import extraire_banque_dose_reponse_v1 as eb1
from controle_ia.environnements import extraire_banque_dose_reponse_v2 as eb2
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller

import test_banque_dose_reponse_v1 as t1

RACINE = Path(__file__).resolve().parents[1]
V1 = RACINE / eb1.Chemins().dossier_procedure / eb1.FICHIERS_PROCEDURE["consigne_extracteur"]


def test_consigne_v2_cas_sain_du_depot():
    texte = eb2.consigne_extracteur_v2(RACINE)
    assert eb2.MARQUE_V2 in texte
    assert "the check in step 2b and the check in step 5" in texte


def test_consigne_v2_ne_change_que_l_etape_2b_et_la_derniere_phrase():
    v1 = V1.read_text(encoding="utf-8")
    v2 = (RACINE / eb2.CONSIGNE_EXTRACTEUR_V2).read_text(encoding="utf-8")
    sans_2b = re.sub(r"2b\. Before going on.*?(?=3\. Answer prompt H10)", "", v2, flags=re.S)
    sans_2b = sans_2b.replace("Apart from the file names, the check in step 2b and the check in step 5,",
                              "Apart from the file names and the check in step 5,")
    assert sans_2b == v1


def _copie_consigne(dest: Path) -> Path:
    chemin = dest / eb2.CONSIGNE_EXTRACTEUR_V2
    chemin.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(RACINE / eb2.CONSIGNE_EXTRACTEUR_V2, chemin)
    sceller(chemin)
    return chemin


def test_consigne_v2_artefact_sans_sceau(tmp_path):
    chemin = _copie_consigne(tmp_path)
    eb2.consigne_extracteur_v2(tmp_path)                          # cas sain sur la copie
    chemin.with_name(chemin.name + ".sha256").unlink()
    with pytest.raises(GardeArret, match="empreinte compagnon"):
        eb2.consigne_extracteur_v2(tmp_path)


def test_consigne_v2_artefact_modifiee_apres_sceau(tmp_path):
    chemin = _copie_consigne(tmp_path)
    chemin.write_text(chemin.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        eb2.consigne_extracteur_v2(tmp_path)


def test_consigne_v2_artefact_retour_a_la_v1(tmp_path):
    chemin = _copie_consigne(tmp_path)
    chemin.with_name(chemin.name + ".sha256").unlink()
    shutil.copyfile(V1, chemin)                                   # la v1 sous le nom de la v2, rescellée
    sceller(chemin)
    with pytest.raises(GardeArret, match="étape 2b"):
        eb2.consigne_extracteur_v2(tmp_path)


def test_reextraction_v2_lit_la_consigne_v2():
    source = (RACINE / "src/controle_ia/environnements/reextraction_echantillon_96_v2.py").read_text(encoding="utf-8")
    assert "eb.consigne_extracteur_v2(racine)" in source and "eb.MARQUE_V2" in source
    assert 'FICHIERS_PROCEDURE["consigne_extracteur"]' not in source
    assert "import extraire_banque_dose_reponse_v2 as eb" in source


def test_preparer_v2_donne_la_consigne_v2_a_chaque_agent(depot, tmp_path_factory, monkeypatch):
    monkeypatch.setattr(eb2, "TAILLE_PILOTE", 3)
    monkeypatch.setattr(eb2, "TAILLE_RESERVE", 3)
    ch1 = t1._depot_banque(depot)
    for m in eb2.Chemins().modules:                               # modules de la version 2 et consigne v2 scellée
        (depot / m).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(RACINE / m, depot / m)
    _copie_consigne(depot)
    committer(depot)
    ch = eb2.Chemins(corpus=ch1.corpus, textes=ch1.textes, invites=ch1.invites)
    prep = eb2.preparer(depot, "20260102-000000-extraction-v2", tmp_path_factory.mktemp("travail"), 1, ch=ch)
    assert len(prep["papiers"]) == 6
    for info in prep["papiers"].values():
        consigne = (Path(info["dossier"]) / "consigne.txt").read_text(encoding="utf-8")
        assert eb2.MARQUE_V2 in consigne
