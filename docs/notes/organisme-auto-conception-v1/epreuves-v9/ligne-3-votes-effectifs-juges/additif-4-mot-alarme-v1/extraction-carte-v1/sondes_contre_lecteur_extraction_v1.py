# -*- coding: utf-8 -*-
"""Sondes supplémentaires du contre-lecteur, fichiers synthétiques seulement."""
import hashlib
import os
import tempfile

import pytest

import extraire_carte_alarme_v1 as ex

ICI = os.path.dirname(os.path.abspath(__file__))
CIBLE = "cible1"


def fiches(texte_cible, n=3):
    paires = ['"a%d": {"contenu": {"t": "x"}, "meta": {"e": "SEMIS"}}' % i for i in range(n - 1)]
    paires.append('"%s": %s' % (CIBLE, texte_cible))
    return "{" + ", ".join(paires) + "}"


def jouer(octets, capsys, n=3):
    d = tempfile.mkdtemp(prefix="sonde-", dir=ICI)
    f = os.path.join(d, "f.json")
    with open(f, "wb") as h:
        h.write(octets)
    s = os.path.join(d, "carte.json")
    code = ex.executer(f, s, hashlib.sha256(octets).hexdigest(), CIBLE, n)
    e = capsys.readouterr()
    return code, e, s


def test_nan_accepte_et_ecrit(capsys):
    code, e, s = jouer(fiches('{"contenu": {"t": NaN}, "meta": {}}').encode(), capsys)
    print("NaN code", code, repr(e.err))
    assert code in (0, 2)


def test_substitut_isole(capsys):
    code, e, s = jouer(fiches('{"contenu": {"t": "\\ud800"}, "meta": {}}').encode(), capsys)
    print("surrogate code", code, repr(e.err))
    assert code == 2 and not os.path.lexists(s) and not os.path.lexists(s + ".sha256")


def test_bom(capsys):
    code, e, s = jouer(b"\xef\xbb\xbf" + fiches('{"contenu": {"t": "x"}, "meta": {}}').encode(), capsys)
    print("bom code", code, repr(e.err))
    assert code == 2 and "SEMIS" not in e.err


def test_entier_geant(capsys):
    code, e, s = jouer(fiches('{"contenu": {"t": ' + "9" * 6000 + '}, "meta": {}}').encode(), capsys)
    print("bigint code", code, repr(e.err))
    assert code in (0, 2, 3) and "SEMIS" not in e.err


def test_imbrication_profonde(capsys):
    code, e, s = jouer(fiches('{"contenu": ' + "[" * 100000 + "]" * 100000 + ', "meta": {}}').encode(), capsys)
    print("deep code", code, repr(e.err))
    assert code in (2, 3) and not os.path.lexists(s)


def test_meta_dans_contenu_garde(capsys):
    code, e, s = jouer(fiches('{"contenu": {"meta": "INTERIEUR"}, "meta": {"e": "SEMIS"}}').encode(), capsys)
    assert code == 0
    with open(s, encoding="utf-8") as h:
        t = h.read()
    assert "INTERIEUR" in t and "SEMIS" not in t


def test_cle_meta_echappee(capsys):
    code, e, s = jouer(fiches('{"contenu": {"t": "x"}, "m\\u0065ta": {"e": "SEMIS"}}').encode(), capsys)
    assert code == 0
    with open(s, encoding="utf-8") as h:
        assert "SEMIS" not in h.read()


def test_sortie_relative(capsys, monkeypatch):
    d = tempfile.mkdtemp(prefix="sonde-", dir=ICI)
    monkeypatch.chdir(d)
    octets = fiches('{"contenu": {"t": "x"}, "meta": {}}').encode()
    f = os.path.join(d, "f.json")
    with open(f, "wb") as h:
        h.write(octets)
    code = ex.executer(f, "carte.json", hashlib.sha256(octets).hexdigest(), CIBLE, 3)
    print("relative code", code, capsys.readouterr().err)
    assert code == 0


def test_compagnon_impossible(capsys, monkeypatch):
    d = tempfile.mkdtemp(prefix="sonde-", dir=ICI)
    octets = fiches('{"contenu": {"t": "x"}, "meta": {}}').encode()
    f = os.path.join(d, "f.json")
    with open(f, "wb") as h:
        h.write(octets)
    s = os.path.join(d, "carte.json")
    reel = open

    def ouvre(chemin, mode="r", *a, **k):
        if str(chemin).endswith(".sha256") and "x" in mode:
            raise PermissionError("simulé")
        return reel(chemin, mode, *a, **k)
    monkeypatch.setattr("builtins.open", ouvre)
    code = ex.executer(f, s, hashlib.sha256(octets).hexdigest(), CIBLE, 3)
    monkeypatch.undo()
    e = capsys.readouterr()
    print("compagnon code", code, repr(e.err))
    assert code == 2 and "compagnon" in e.err
