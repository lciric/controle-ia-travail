"""Essai écrit du correctif `lenses-neuronpedia-llama-v2.diff` (2026-11-14) — NON EXÉCUTÉ (même statut et même usage
que `essai-06_activations-llama-v3.py` : machine louée de B0, après GO, feu de la mère et règle de Lazar). v3 : remplace
l'essai v2 (archivé) après la contre-lecture 3 (remarque 11) : chemins de `J` pour Llama et pour Qwen3, trois formats de plus.

    NEURON_LENS_ROOT=$PWD python -m pytest -q -rs <chemin>/essai-lenses-neuronpedia-v3.py

R5 : la garde `neuronpedia_lens` est essayée sur un cas sain et sur des artefacts (couche manquante, couches décalées, clé
autre que « J », formes mêlées, indices non entiers, « J » vide, matrice non carrée, empreinte fausse), par des fichiers
factices ; `hf_hub_download` est remplacé par un chemin local. `load_lens("J")` passe par la garde pour Llama, pas pour Qwen3.
"""
import hashlib
import os
import sys
from pathlib import Path

import pytest
import torch

ROOT = Path(os.environ.get("NEURON_LENS_ROOT", ".")).resolve()
SHA_LENSES_CORR = "2de7d6afe63bc398e17f4ff93ae7b7acdcc3a330e91c728df88bef338008b3e4"


@pytest.fixture
def lenses(monkeypatch):
    assert hashlib.sha256((ROOT / "neuron_lens" / "lenses.py").read_bytes()).hexdigest() == SHA_LENSES_CORR
    monkeypatch.syspath_prepend(str(ROOT))
    for name in [k for k in sys.modules if k == "neuron_lens" or k.startswith("neuron_lens.")]:
        del sys.modules[name]
    from neuron_lens import lenses as mod
    return mod


def factice(tmp_path, monkeypatch, mod, payload, enregistrer=None):
    f = tmp_path / "lens.pt"
    torch.save(payload, f)
    monkeypatch.setattr(mod, "hf_hub_download", lambda repo, name: str(f))
    if enregistrer is not None:
        monkeypatch.setitem(mod.NEURONPEDIA_SHA256, "x.pt", enregistrer(f))
    return "x.pt"


def sain(n=3, d=4):
    return {"J": {l: torch.randn(d, d).half() for l in range(n)}, "n_prompts": 64}


def test_cas_sain(tmp_path, monkeypatch, lenses):
    name = factice(tmp_path, monkeypatch, lenses, sain(), lambda f: hashlib.sha256(f.read_bytes()).hexdigest())
    J = lenses.neuronpedia_lens(name)
    assert sorted(J) == [0, 1, 2]


@pytest.mark.parametrize("payload", [
    {"J": {0: torch.eye(4), 2: torch.eye(4)}},          # couche manquante
    {"R": {0: torch.eye(4), 1: torch.eye(4)}},          # autre clé
    {"J": {0: torch.eye(4), 1: torch.eye(3)}},          # formes mêlées
    {"J": {"0": torch.eye(4), "1": torch.eye(4)}},      # indices non entiers
    {"J": {1: torch.eye(4), 2: torch.eye(4)}},          # couches décalées 1..n
    {"J": {}},                                          # « J » vide
    {"J": {0: torch.zeros(4, 3)}},                      # matrice non carrée
])
def test_formats_refuses(tmp_path, monkeypatch, lenses, payload):
    name = factice(tmp_path, monkeypatch, lenses, payload)
    with pytest.raises(ValueError, match="not a J-lens layout"):
        lenses.neuronpedia_lens(name)


def test_empreinte_fausse(tmp_path, monkeypatch, lenses):
    name = factice(tmp_path, monkeypatch, lenses, sain(), lambda f: "0" * 64)
    with pytest.raises(ValueError, match="sha256"):
        lenses.neuronpedia_lens(name)


def test_nom_inconnu_pour_un_autre_modele(lenses):
    with pytest.raises(KeyError, match="npR"):
        lenses.load_lens("npR", "Qwen/Qwen3-8B")


def test_noms_et_empreintes_llama(lenses):
    m = "meta-llama/Llama-3.1-8B-Instruct"
    fichiers = [lenses.NEURONPEDIA_FILES[m], *lenses.NEURONPEDIA_EXTRA[m].values()]
    assert set(fichiers) == set(lenses.NEURONPEDIA_SHA256)


def test_J_llama_passe_par_la_garde(monkeypatch, lenses):
    appels = []
    monkeypatch.setattr(lenses, "neuronpedia_lens", lambda f: appels.append(f) or {0: torch.eye(4)})
    m = "meta-llama/Llama-3.1-8B-Instruct"
    lenses.load_lens("J", m)
    assert appels == [lenses.NEURONPEDIA_FILES[m]]


def test_J_qwen3_inchange(tmp_path, monkeypatch, lenses):
    def interdit(f):
        raise AssertionError("Qwen3 ne doit pas passer par neuronpedia_lens")
    monkeypatch.setattr(lenses, "neuronpedia_lens", interdit)
    f = tmp_path / "qwen.pt"
    torch.save({"J": {0: torch.eye(4)}}, f)
    monkeypatch.setattr(lenses, "hf_hub_download", lambda repo, name: str(f))
    J = lenses.load_lens("J", "Qwen/Qwen3-8B")
    assert sorted(J) == [0]
