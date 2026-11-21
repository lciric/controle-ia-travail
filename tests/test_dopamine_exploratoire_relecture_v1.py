"""Relecture forcée des épisodes honnêtes (bloc de l'étape 1, exploratoire) sur le modèle jouet : sain et artefacts."""
import json

import numpy as np
import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")

from controle_ia.dopamine_exploratoire import etats_v1, jouet_v1, math500_v1, relecture_v1  # noqa: E402
from controle_ia.dopamine_exploratoire.stockage_v1 import ecrire_jsonl  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402


def _episode(d, i, etiquette="honnete"):
    en = d.encoder(math500_v1.invite(f"{i}+{i}", "litteral"))
    actions = ["12 3", "\\boxed{1}", "45"]
    ids, pos = list(en), [len(en) - 1]
    for a in actions:
        t = d.encoder(a)
        ids += t
        pos.append(len(ids) - 1)
        ids += d.encoder("\n")                     # clôture du tour, hors de l'action
    return {"id": f"ep-{i}", "famille": f"f{i % 3}", "etiquette": etiquette, "recompense": i % 2, "ids": ids,
            "ids_enonce": en, "positions": pos, "textes_actions": actions}


def _fichier(tmp_path, eps, nom="contextes.jsonl"):
    f = tmp_path / nom
    ecrire_jsonl(f, eps)
    return f


@pytest.fixture
def jouet():
    return jouet_v1.modele_jouet(0, couches=24)


def test_relecture_saine(tmp_path, jouet):
    m, d = jouet
    eps = [_episode(d, i) for i in range(6)]
    f = _fichier(tmp_path, eps)
    r = relecture_v1.relire(m, d, f, [7, 15, 23], tmp_path / "out", {e["id"] for e in eps})
    assert r["episodes"] == 6 and r["double_passe"] == 5 and r["ecart_position_max"] < 1e-5
    idx = json.loads((tmp_path / "out" / "couche-15.index.json").read_text())
    tab = np.load(tmp_path / "out" / "couche-15.npy")
    assert tab.dtype == np.float16 and tab.shape == (6 * 4, 16) and idx["longueurs"] == [4] * 6
    e = eps[2]
    ref = etats_v1.etats_d_une_sequence(m, e["ids"], [15])[15]
    np.testing.assert_allclose(tab[idx["decalages"][2] + 1:idx["decalages"][2] + 4].astype(np.float32),
                               ref[e["positions"][1:]].astype(np.float16).astype(np.float32))
    assert relecture_v1.relire(m, d, f, [7, 15, 23], tmp_path / "out")["deja_fait"]


@pytest.mark.parametrize("abimer,motif", [
    (lambda e: e.update(etiquette="sabote"), "honnêtes seulement"),
    (lambda e: e.update(id="intrus"), "hors de la liste"),
    (lambda e: e.update(score=0.3), "champs"),
    (lambda e: e.update(ids_enonce=e["ids_enonce"] + [9]), "préfixe"),
    (lambda e: e.update(positions=[e["positions"][0]] + e["positions"][2:] + e["positions"][1:2]), "positions"),
])
def test_relecture_artefacts_de_contexte(tmp_path, jouet, abimer, motif):
    m, d = jouet
    eps = [_episode(d, i) for i in range(3)]
    liste = {e["id"] for e in eps}
    abimer(eps[1])
    with pytest.raises(GardeArret, match=motif):
        relecture_v1.relire(m, d, _fichier(tmp_path, eps), [7], tmp_path / "out", liste)


def test_relecture_couches_et_position(tmp_path, jouet):
    m, d = jouet
    eps = [_episode(d, i) for i in range(3)]
    f = _fichier(tmp_path, eps)
    for couches in ([3, 7], [8]):
        with pytest.raises(GardeArret):
            relecture_v1.relire(m, d, f, couches, tmp_path / "out")
    decale = [dict(e, positions=[e["positions"][0]] + [p - 1 for p in e["positions"][1:]]) for e in eps]
    with pytest.raises(GardeArret, match="garde de position"):
        relecture_v1.relire(m, d, _fichier(tmp_path, decale, "decale.jsonl"), [7], tmp_path / "out2")


def test_relecture_double_passe_differente(tmp_path, jouet, monkeypatch):
    m, d = jouet
    eps = [_episode(d, i) for i in range(2)]
    vraie, n = etats_v1.etats_d_une_sequence, {"k": 0}

    def bruitee(modele, ids, couches, **k):
        n["k"] += 1
        out = vraie(modele, ids, couches, **k)
        if n["k"] == 3:                           # la seconde passe du premier épisode
            out = {c: v + 1.0 for c, v in out.items()}
        return out
    monkeypatch.setattr(relecture_v1, "etats_d_une_sequence", bruitee)
    with pytest.raises(GardeArret, match="deux passes"):
        relecture_v1.relire(m, d, _fichier(tmp_path, eps), [7], tmp_path / "out")


def test_fichier_altere_refuse(tmp_path, jouet):
    m, d = jouet
    f = _fichier(tmp_path, [_episode(d, 0)])
    f.write_text(f.read_text().replace('"f0"', '"f9"'))
    with pytest.raises(GardeArret):
        relecture_v1.relire(m, d, f, [7], tmp_path / "out")
