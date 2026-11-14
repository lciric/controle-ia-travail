"""Essais des données du volet A (texte gelé v6) sur les fichiers publics archivés et le tokeniseur de Qwen3-8B ; aucun modèle."""
import json

import numpy as np
import pytest

from controle_ia.neuron_lens import volet_a_donnees_v1 as vd

TOK = vd.SOURCES / "qwen3-8b-tokenizer.json"
COMPTES = vd.RACINE / "docs/notes/neuron-lens-v1/outils/comptes-avant-scellement-v1.json"


@pytest.fixture(scope="module")
def tok():
    return vd.charger_tokeniseur(TOK)


def test_effectifs():
    assert len(vd.charger("C1")) == 200
    assert len(vd.charger("C2")) == 594
    assert len(vd.charger("C3")) == 597
    assert len(vd.advbench_retenu()) == 463
    v, f = vd.faits()
    assert (len(v), len(f)) == (297, 300) and "The Nile River is the longest river in the world." not in v + f


def test_positions_et_comptes(tok):
    c = json.loads(COMPTES.read_text())
    for nom, cle in (("C1", "C1"), ("C2", "C2"), ("C3", "C3")):
        pos = [vd.rendre(tok, e.texte)[1] for e in vd.charger(nom)]
        assert min(pos) == c[cle]["positions_lues"]["min"] and max(pos) == c[cle]["positions_lues"]["max"]
    assert vd.debut_du_texte(tok) == 3 + 27


def test_jetons_plantes(tok):
    e1 = [e for e in vd.charger("C2") if e.classe == 1][0]
    e0 = [e for e in vd.charger("C2") if e.classe == 0][0]
    i1, _ = vd.rendre(tok, e1.texte)
    i0, _ = vd.rendre(tok, e0.texte)
    assert set(i1) ^ set(i0) == set(vd.P_PLANTES)
    assert i1.index(650) == 36


def test_decoupes_groupees_stratifiees():
    g = vd.arbre_de_graines()
    for nom in ("C1", "C2", "C3"):
        ex = vd.charger(nom)
        for d in range(5):
            app, tst = vd.decoupe(ex, g.decoupes[nom][d]["permutation"])
            assert not ({ex[i].groupe for i in app} & {ex[i].groupe for i in tst})
            assert sorted(app + tst) == list(range(len(ex)))
            for c in (0, 1):
                n_c = sum(e.classe == c for e in ex)
                assert abs(sum(ex[i].classe == c for i in tst) / n_c - 0.30) < 0.02
    a1 = vd.decoupe(vd.charger("C1"), vd.arbre_de_graines().decoupes["C1"][0]["permutation"])
    a2 = vd.decoupe(vd.charger("C1"), vd.arbre_de_graines().decoupes["C1"][0]["permutation"])
    assert a1 == a2  # reproductible


def test_hors_distribution():
    ex = vd.charger("C2")
    app, tst = vd.decoupe(ex, vd.arbre_de_graines().decoupes["C2"][0]["permutation"])
    gt = {ex[i].groupe for i in tst}
    ood = vd.hors_distribution("C2", gt, [ex[i] for i in tst])
    assert {e.groupe for e in ood} == gt and len(ood) == 2 * len(gt)
    ex1 = vd.charger("C1")
    app, tst = vd.decoupe(ex1, vd.arbre_de_graines().decoupes["C1"][0]["permutation"])
    ood1 = vd.hors_distribution("C1", None, [ex1[i] for i in tst])
    assert sum(e.classe == 1 for e in ood1) == 463 and sum(e.classe == 0 for e in ood1) == 30


def test_graines_distinctes():
    g = vd.arbre_de_graines()
    etats = [np.random.default_rng(s).integers(1 << 30) for s in g.references_par_couche.values()]
    etats += [np.random.default_rng(g.decoupes["C1"][0][t]).integers(1 << 30) for t in ("permutation", "permutees")]
    assert len(set(etats)) == len(etats)


def test_tokeniseur_verifie(tmp_path):
    faux = tmp_path / "t.json"
    faux.write_text("{}")
    with pytest.raises(ValueError):
        vd.charger_tokeniseur(faux)
