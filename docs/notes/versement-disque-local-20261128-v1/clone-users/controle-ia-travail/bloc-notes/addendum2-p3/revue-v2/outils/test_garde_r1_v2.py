"""Épreuve de la garde R1 de la revue v2 : un cas sain et des artefacts (R5).

Les artefacts visent des chemins INEXISTANTS sous les dossiers interdits : si la garde échouait, l'accès lèverait
`FileNotFoundError` et rien de réel ne serait lu. Le chemin des consignes privées n'est éprouvé que par la fonction pure
de la garde (aucune ouverture).
"""
import glob
import os
import shutil

import pytest

import garde_r1_v2 as g

DEPOT = "/home/user/controle-ia-travail"


def test_cas_sain_ouverture_permise():
    with open(os.path.join(DEPOT, "src", "controle_ia", "gardes.py"), "rb") as fh:
        assert fh.read(10)
    assert os.listdir(os.path.join(DEPOT, "src", "controle_ia"))
    assert not g._interdit(os.path.join(DEPOT, "src", "controle_ia", "gardes.py"))
    assert not g._interdit("/tmp/x/donnees/run/textes-actions-p3.jsonl")      # dépôt jouet : tracé, pas refusé


@pytest.mark.parametrize("chemin", ["diag/__garde_r1_inexistant__/x.json", "runs/__garde_r1_inexistant__/manifeste.json",
                                    "donnees/__garde_r1_inexistant__/scores-p3.npz", "traces/__garde_r1_inexistant__.txt",
                                    "__garde_r1_inexistant__/textes-actions-p3.jsonl"])
def test_artefact_ouverture_refusee(chemin):
    with pytest.raises(PermissionError, match="garde R1 de la revue v2"):
        open(os.path.join(DEPOT, chemin), "rb")
    with pytest.raises(PermissionError, match="garde R1 de la revue v2"):
        open(chemin, "rb")                                                     # relatif : lancé depuis la racine


@pytest.mark.parametrize("appel", ["listdir", "scandir", "glob", "copytree", "copyfile"])
def test_artefact_listage_et_copie_refuses(appel, tmp_path):
    cible = os.path.join(DEPOT, "runs", "__garde_r1_inexistant__")
    with pytest.raises(PermissionError, match="garde R1 de la revue v2"):
        if appel == "listdir":
            os.listdir(cible)
        elif appel == "scandir":
            os.scandir(cible)
        elif appel == "glob":
            glob.glob(os.path.join(cible, "*"))
        elif appel == "copytree":
            shutil.copytree(cible, tmp_path / "copie")
        else:
            shutil.copyfile(os.path.join(cible, "x"), tmp_path / "x")


def test_consignes_privees_reconnues_sans_ouverture():
    assert g._interdit(os.path.join(DEPOT, "prereg", "P3-consignes-v1.md"))
    assert not g._interdit(os.path.join(DEPOT, "prereg", "P3-premier-test-i-a-v1.md"))
