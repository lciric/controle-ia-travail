"""Essais complémentaires (v2) des données du volet A — le module reste `volet_a_donnees_v1` (code inchangé) ; contre-lecture 1,
remarques 8 à 10 : ordre des graines par reconstruction indépendante, fichier altéré, rendu inattendu, position < 16, contraste inconnu,
positions hors distribution."""
import shutil

import numpy as np
import pytest

from controle_ia.neuron_lens import volet_a_donnees_v1 as vd

TOK = vd.SOURCES / "qwen3-8b-tokenizer.json"


@pytest.fixture(scope="module")
def tok():
    return vd.charger_tokeniseur(TOK)


def test_graines_reconstruction_independante():
    g = vd.arbre_de_graines()
    r = np.random.SeedSequence(20261114).spawn(4)
    refs = r[3].spawn(4)
    for i, c in enumerate(vd.COUCHES):
        assert g.references_par_couche[c].spawn_key == refs[i].spawn_key
    for ic, nom in enumerate(("C1", "C2", "C3")):
        dec = r[ic].spawn(5)
        for d in range(5):
            t = dec[d].spawn(6)
            for it, tache in enumerate(vd.TACHES):
                attendu = t[it]
                obtenu = g.decoupes[nom][d][tache]
                if tache == "directions":
                    for jc, c in enumerate(vd.COUCHES):
                        assert obtenu[c].spawn_key == attendu.spawn_key + (jc,)
                else:
                    assert obtenu.spawn_key == attendu.spawn_key
                    assert obtenu.entropy == 20261114


def test_fichier_altere_refuse(tmp_path, monkeypatch):
    for nom in vd.EMPREINTES:
        shutil.copy(vd.SOURCES / nom, tmp_path / nom)
    with open(tmp_path / "repe-facts_true_false.csv", "a", encoding="utf-8") as f:
        f.write("Une ligne ajoutée.,1\n")
    monkeypatch.setattr(vd, "SOURCES", tmp_path)
    assert len(vd.charger("C1")) == 200  # fichiers intacts acceptés
    with pytest.raises(ValueError):
        vd.charger("C3")


def test_contraste_inconnu():
    with pytest.raises(ValueError):
        vd.charger("C4")


def test_rendu_inattendu_et_position_courte(tok, monkeypatch):
    class Faux:  # artefact : un tokeniseur qui fusionne la fin avec le texte (rendu inattendu)
        def encode(self, s, add_special_tokens=False):
            ids = tok.encode(s, add_special_tokens=False).ids
            return type("E", (), {"ids": ids[:-1] + [ids[-1] + 1] if s.endswith(vd.FIN) and s != vd.FIN else ids})()
    with pytest.raises(ValueError):
        vd.rendre(Faux(), "Hello there, this is a short text.")
    assert vd.rendre(tok, "Hello there, this is a short text.")[1] >= 16  # cas sain
    monkeypatch.setattr(vd, "PREAMBULE", "")
    with pytest.raises(ValueError):
        vd.rendre(tok, "Hi.")  # position lue < 16 sans préambule


def test_positions_hors_distribution(tok):
    ex = vd.charger("C1")
    _, tst = vd.decoupe(ex, vd.arbre_de_graines().decoupes["C1"][0]["permutation"])
    for e in vd.hors_distribution("C1", None, [ex[i] for i in tst]):
        ids, pos = vd.rendre(tok, e.texte)
        assert 16 <= pos == len(ids) - 3  # fin « <|im_end|> \n » : 2 jetons après la position lue
    ex2 = vd.charger("C2")
    _, tst2 = vd.decoupe(ex2, vd.arbre_de_graines().decoupes["C2"][0]["permutation"])
    gt = {ex2[i].groupe for i in tst2}
    for e in vd.hors_distribution("C2", gt, [ex2[i] for i in tst2]):
        assert vd.rendre(tok, e.texte)[1] >= 16
