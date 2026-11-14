"""Essai de l'extraction v2 : égalité avec la v1 (remplissage, lots multiples, couches isolées), arrêt de la passe à la couche lue,
dernière couche refusée."""
import numpy as np
import pytest
import torch
from transformers import Qwen3Config, Qwen3ForCausalLM

from controle_ia.neuron_lens import volet_a_extraction_v1 as v1
from controle_ia.neuron_lens import volet_a_extraction_v2 as v2


@pytest.fixture(scope="module")
def modele():
    torch.manual_seed(0)
    cfg = Qwen3Config(vocab_size=64, hidden_size=32, intermediate_size=48, num_hidden_layers=6, num_attention_heads=4,
                      num_key_value_heads=2, head_dim=8, max_position_embeddings=128)
    return Qwen3ForCausalLM(cfg).float().eval()


def test_egal_a_la_v1(modele):
    rng = np.random.default_rng(0)
    lots = [list(rng.integers(1, 64, size=n)) for n in (20, 27, 23, 9, 31)]
    pos = [len(x) - 3 for x in lots]
    for couches in ((1, 3), (2,), (0, 1, 2, 3, 4)):
        r1, n1 = v1.extraire(modele, lots, pos, couches, par_lot=2)
        r2, n2 = v2.extraire(modele, lots, pos, couches, par_lot=2)
        for l in couches:
            assert np.allclose(r1[l], r2[l], atol=1e-6) and np.allclose(n1[l], n2[l], atol=1e-6)


def test_passe_arretee(modele):
    vus = []
    h = modele.model.layers[4].register_forward_hook(lambda m, x, o: vus.append(1))
    try:
        v2.extraire(modele, [[1, 2, 3, 4]], [2], (1,))
    finally:
        h.remove()
    assert vus == []  # la couche 4 n'est pas calculée quand la plus haute couche lue est 1


def test_derniere_couche_refusee(modele):
    with pytest.raises(ValueError):
        v2.extraire(modele, [[1, 2, 3]], [2], (5,))
