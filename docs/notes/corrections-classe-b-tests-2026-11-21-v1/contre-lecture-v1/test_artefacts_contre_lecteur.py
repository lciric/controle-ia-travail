"""Artefacts du contre-lecteur (a ecrit les predictions AVANT de jouer ; voir la piece).
P1 accepte (parite avec la v10 sous /usr/ : `-c` accepte des qu'un fichier epingle est present)
P2 refuse (copie de l'interprete a un autre chemin)
P3 refuse (meme chemin ecrit avec `..`, non egal en chaine)
P4 refuse (programme non epingle en tete, interprete courant en argument)
P5 accepte (sys.executable designe un fichier quelconque : l'exemption suit sys.executable, pas l'identite du binaire)
P6 refuse (maillon intermediaire de la chaine de liens, hors /usr/)
P7 refuse (hors /usr/ : copie de l'interprete + script epingle + le lien courant NON en tete : le lien courant ne sauve pas la copie)
"""
import os
import sys
from pathlib import Path

import pytest

from test_lancer_course_auto_conception_v11 import (L, L10, _cmd, _declaration, _depart, _fixe, _script,
                                                    interprete_hors_usr)  # noqa: F401


def _verif(module, cmd, *empreintes):
    return module.verifier_declaration(_declaration(cmd), _fixe(), _depart(*empreintes))


def test_P1_c_avec_fichier_epingle_accepte_v11_et_parite_v10_sous_usr(tmp_path, interprete_hors_usr):
    s = _script(tmp_path)
    cmd = [str(interprete_hors_usr), "-I", "-c", "print('code non epingle')", str(s), "--url-relais", "http://127.0.0.1:8790"]
    res = _verif(L, cmd, L.sha256_fichier(s))
    assert "prop-astra" in [e["etiquette"] for e in res["especes_actives"]]
    # parite : la v10 accepte la meme forme avec un interprete sous /usr/
    assert os.path.isfile("/usr/local/bin/python3")
    cmd10 = ["/usr/local/bin/python3"] + cmd[1:]
    res10 = _verif(L10, cmd10, L10.sha256_fichier(s))
    assert "prop-astra" in [e["etiquette"] for e in res10["especes_actives"]]
    # et la v10 refuse la forme hors /usr/ (le defaut corrige)
    with pytest.raises(L10.Refus, match="programme non épinglé"):
        _verif(L10, cmd, L10.sha256_fichier(s))


def test_P2_copie_de_l_interprete_refusee(tmp_path, interprete_hors_usr):
    s = _script(tmp_path)
    copie = tmp_path / "copie" / "python"
    copie.parent.mkdir()
    copie.write_bytes(Path(os.path.realpath(sys.executable)).read_bytes())
    with pytest.raises(L.Refus, match="programme non épinglé"):
        _verif(L, _cmd(copie, s), L.sha256_fichier(s))


def test_P3_chemin_avec_point_point_refuse(tmp_path, interprete_hors_usr):
    s = _script(tmp_path)
    detour = Path(str(interprete_hors_usr.parent) + "/../bin/python")
    assert os.path.samefile(detour, interprete_hors_usr)
    with pytest.raises(L.Refus, match="programme non épinglé"):
        _verif(L, _cmd(detour, s), L.sha256_fichier(s))


def test_P4_programme_non_epingle_en_tete_refuse(tmp_path, interprete_hors_usr):
    s = _script(tmp_path)
    evil = _script(tmp_path, "evil.py")
    evil.write_text("print('evil')\n", encoding="utf-8")
    cmd = [str(evil), str(interprete_hors_usr), str(s), "--url-relais", "http://127.0.0.1:8790"]
    with pytest.raises(L.Refus, match="programme non épinglé"):
        _verif(L, cmd, L.sha256_fichier(s))


def test_P5_l_exemption_suit_sys_executable_meme_si_ce_n_est_pas_un_interprete(tmp_path, monkeypatch):
    s = _script(tmp_path)
    faux = tmp_path / "faux-interprete.sh"
    faux.write_text("#!/bin/sh\necho non epingle\n", encoding="utf-8")
    monkeypatch.setattr(sys, "executable", str(faux))
    res = _verif(L, [str(faux), str(s), "--url-relais", "http://127.0.0.1:8790"], L.sha256_fichier(s))
    assert "prop-astra" in [e["etiquette"] for e in res["especes_actives"]]


def test_P6_maillon_intermediaire_refuse(tmp_path, monkeypatch):
    s = _script(tmp_path)
    reel = os.path.realpath(sys.executable)
    b = tmp_path / "venv" / "bin"
    b.mkdir(parents=True)
    (b / "python3").symlink_to(reel)
    (b / "python").symlink_to("python3")
    monkeypatch.setattr(sys, "executable", str(b / "python"))
    assert os.path.realpath(str(b / "python")) == reel
    with pytest.raises(L.Refus, match="programme non épinglé"):
        _verif(L, _cmd(b / "python3", s), L.sha256_fichier(s))
    res = _verif(L, _cmd(b / "python", s), L.sha256_fichier(s))      # contraste : le lien courant lui-meme passe
    assert "prop-astra" in [e["etiquette"] for e in res["especes_actives"]]


def test_P7_copie_avec_lien_courant_en_argument_refusee(tmp_path, interprete_hors_usr):
    s = _script(tmp_path)
    copie = tmp_path / "copie" / "python"
    copie.parent.mkdir()
    copie.write_bytes(Path(os.path.realpath(sys.executable)).read_bytes())
    cmd = [str(copie), str(interprete_hors_usr), "-I", str(s)]
    with pytest.raises(L.Refus, match="programme non épinglé"):
        _verif(L, cmd, L.sha256_fichier(s))
