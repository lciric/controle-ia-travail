"""Essai écrit du correctif (3) `causal_lens-graine-v1.diff` (seconde graine de neurones pour l'audit « trop beau » de B-α) — à jouer
SUR LA MACHINE LOUÉE à B0, jamais dans le conteneur de la session (décision (a) de Lazar, R-2710), dans l'arbre du dépôt voisin
au commit `849bfe16` avec les quatre correctifs appliqués :

    NEURON_LENS_ROOT=$PWD NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct python -m pytest -q -rs <chemin>/essai-causal_lens-graine-v1.py

Aucun test ne doit être sauté (un test sauté = arrêt, comme pour les essais des correctifs (1) et (2)). R5 : chaque garde du
correctif est essayée sur un cas sain et sur un artefact. Rien ne charge le modèle : seuls le tirage des neurones, le nom du
fichier de mesure, l'argument `--seed` et la garde de `score` sont essayés (`torch.load` remplacé par un faux fichier).
"""
import argparse
import hashlib
import importlib.util
import os
import random
import sys
from pathlib import Path

import pytest

ROOT = Path(os.environ.get("NEURON_LENS_ROOT", ".")).resolve()
SHA_CAUSAL_CORR = "a9d3bc8e8dde945c4ff0f4a229f30c78b35ee299a4fa1fe34fe75db35252141b"
L, F, PER = 32, 14336, 32  # Llama 3.1 8B : couches, neurones par couche ; neurones tirés par couche (défaut publié)


@pytest.fixture(scope="module")
def cl():
    chemin = ROOT / "scripts" / "checks" / "causal_lens.py"
    assert hashlib.sha256(chemin.read_bytes()).hexdigest() == SHA_CAUSAL_CORR, "causal_lens.py n'est pas la version corrigée"
    sys.path.insert(0, str(ROOT))
    for name in [k for k in sys.modules if k == "neuron_lens" or k.startswith("neuron_lens.")]:
        del sys.modules[name]  # le paquet est relu depuis l'arbre corrigé
    spec = importlib.util.spec_from_file_location("causal_lens_corrige", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.MODEL == "meta-llama/Llama-3.1-8B-Instruct", "NEURON_LENS_MODEL doit nommer le modèle de B-α"
    assert Path(mod.arch.__file__).resolve().is_relative_to(ROOT), "neuron_lens chargé hors de l'arbre corrigé"
    return mod


def test_graine_0_inchangee(cl):
    """Cas sain : la graine 0 redonne exactement le tirage publié (`random.Random(0)`, même ordre)."""
    rng = random.Random(0)
    attendu = [(l, n) for l in range(L) for n in sorted(rng.sample(range(F), PER))]
    assert cl.random_neurons(L, F, PER) == attendu
    assert cl.random_neurons(L, F, PER, 0) == attendu
    assert cl.sample_neurons(L, F, PER) == attendu  # Llama : aucun pôle nommé


def test_graine_1_autre_tirage(cl):
    """La graine 1 tire d'autres neurones, de même taille, et `sample_neurons` la transmet (artefact : graine ignorée)."""
    t0, t1 = cl.random_neurons(L, F, PER, 0), cl.random_neurons(L, F, PER, 1)
    assert len(t1) == len(t0) == L * PER and t1 != t0
    assert cl.sample_neurons(L, F, PER, 1) == t1
    assert len(set(t0) & set(t1)) < L * PER // 4  # quelques neurones communs au plus, par hasard


def test_nom_du_fichier(cl):
    """La graine 0 garde le nom publié ; une autre graine écrit un fichier distinct (le résultat publié n'est jamais écrasé)."""
    m = "meta-llama/Llama-3.1-8B-Instruct"
    assert cl.causal_path(m).name == "llama-3.1-8b-instruct-causal.pt"
    assert cl.causal_path(m, 0) == cl.causal_path(m)
    assert cl.causal_path(m, 1).name == "llama-3.1-8b-instruct-causal-seed1.pt"
    p1 = cl.causal_path(m, 1)
    assert p1.with_name(f"{p1.stem}-partial.pt").name == "llama-3.1-8b-instruct-causal-seed1-partial.pt"


def test_argument_seed(cl, monkeypatch):
    """`--seed` existe, vaut 0 par défaut et est transmis à `measure` et à `score`."""
    vus = []
    monkeypatch.setattr(cl, "measure", lambda a: vus.append(("measure", a.seed)))
    monkeypatch.setattr(cl, "score", lambda a: vus.append(("score", a.seed)))
    for argv in (["x", "measure"], ["x", "score", "--seed", "1"]):
        monkeypatch.setattr(sys, "argv", argv)
        cl.main()
    assert vus == [("measure", 0), ("score", 1)]


@pytest.mark.parametrize("graine_fichier,graine_demandee,doit_lever", [(0, 1, True), (1, 0, True), (1, 1, False), (0, 0, False)])
def test_garde_de_score(cl, monkeypatch, graine_fichier, graine_demandee, doit_lever):
    """Garde de `score` : un fichier tiré avec une autre graine est refusé (artefact) ; avec la même graine, la garde passe
    (cas sain : on s'arrête juste après, par une exception de l'essai, avant tout chargement de modèle)."""
    meta = {"per_layer": PER} | ({"seed": graine_fichier} if graine_fichier else {})

    class Passe(Exception):
        pass

    def faux_load(chemin, weights_only=False):
        assert Path(chemin) == cl.causal_path("meta-llama/Llama-3.1-8B-Instruct", graine_demandee)
        return {"meta": meta, "picks": []}

    def stop(*a, **k):
        raise Passe

    monkeypatch.setattr(cl.torch, "load", faux_load)
    monkeypatch.setattr(cl, "AutoTokenizer", type("T", (), {"from_pretrained": staticmethod(stop)}))
    args = argparse.Namespace(model="meta-llama/Llama-3.1-8B-Instruct", seed=graine_demandee, lenses="logit", tag="")
    if doit_lever:
        with pytest.raises(AssertionError, match="another seed"):
            cl.score(args)
    else:
        with pytest.raises(Passe):
            cl.score(args)
