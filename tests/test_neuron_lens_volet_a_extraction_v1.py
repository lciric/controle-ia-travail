"""Essai de l'extraction du volet A sur un Qwen3 miniature aléatoire (aucun poids téléchargé, aucun code voisin)."""
import numpy as np
import pytest
import torch
from transformers import Qwen3Config, Qwen3ForCausalLM

from controle_ia.neuron_lens import volet_a_extraction_v1 as ve


@pytest.fixture(scope="module")
def modele():
    torch.manual_seed(0)
    cfg = Qwen3Config(vocab_size=64, hidden_size=32, intermediate_size=48, num_hidden_layers=4, num_attention_heads=4,
                      num_key_value_heads=2, head_dim=8, max_position_embeddings=128)
    return Qwen3ForCausalLM(cfg).float().eval()


def _reference(modele, ids, pos, l):
    """Sortie de la couche l et entrée de down_proj, par crochets, sur une passe sans remplissage."""
    vu = {}
    h1 = modele.model.layers[l].register_forward_hook(lambda m, x, o: vu.__setitem__("res", (o[0] if isinstance(o, tuple) else o)[0, pos]))
    h2 = modele.model.layers[l].mlp.down_proj.register_forward_pre_hook(lambda m, x: vu.__setitem__("neu", x[0][0, pos]))
    with torch.no_grad():
        modele(input_ids=torch.tensor([ids]))
    h1.remove(); h2.remove()
    return vu["res"].numpy(), vu["neu"].numpy()


def test_extraction_egale_reference_malgre_le_remplissage(modele):
    rng = np.random.default_rng(0)
    lots = [list(rng.integers(1, 64, size=n)) for n in (20, 27, 23)]
    pos = [len(x) - 2 for x in lots]
    res, neu = ve.extraire(modele, lots, pos, (1, 2), par_lot=3)
    for i, (ids, p) in enumerate(zip(lots, pos)):
        for l in (1, 2):
            r, n = _reference(modele, ids, p, l)
            assert np.allclose(res[l][i], r, atol=1e-5) and np.allclose(neu[l][i], n, atol=1e-5)
    assert res[1].shape == (3, 32) and neu[2].shape == (3, 48)


def test_derniere_couche_refusee(modele):
    with pytest.raises(ValueError):
        ve.extraire(modele, [[1, 2, 3]], [2], (3,))
