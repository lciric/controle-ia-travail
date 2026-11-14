"""Essai écrit du correctif `06_activations-llama-sans-qk-norm-v1.diff` (2026-11-14) — NON EXÉCUTÉ.

Statut : écrit par la session fille « Neuron Lens » le 2026-11-14, jamais lancé dans le conteneur de la session (refus
du classifieur du 13 novembre sur l'exécution locale du code voisin, non contourné ; décision de la mère R-2685). Il
s'exécute seulement sur la machine louée de l'étape B0, après une ligne de GO, le feu de la mère et une règle décidée par
Lazar sur l'exécution du code voisin.

Usage prévu (B0, processeur suffisant, aucun poids téléchargé : modèles miniatures aléatoires) :

    git clone https://github.com/stdlogits/neuron-lens && cd neuron-lens
    git checkout 849bfe1678e28becceb1e3864afe5fc8297d02e4
    cp scripts/06_activations.py /tmp/06_activations_original.py
    git apply <chemin>/06_activations-llama-sans-qk-norm-v1.diff
    NEURON_LENS_ROOT=$PWD NEURON_LENS_ORIG=/tmp/06_activations_original.py python -m pytest -q <chemin>/essai-06_activations-llama-v1.py

Ce qu'il vérifie :
1. Llama miniature : la passe des crochets aboutit ; aucune statistique QK n'est accumulée (q, q_r, q_m, k_r, k_m nuls) ;
   les sommes des neurones et des têtes le sont (non nulles) ; 5 crochets par couche.
2. Qwen3 miniature (non-régression) : statistiques QK non nulles ; 7 crochets par couche, comme avant le correctif.
3. Marque de la passe : la condition qui pose meta["qk_norm"] = False est vraie pour Llama, fausse pour Qwen3.
4. R5 (garde essayée sur un artefact) : le script original échoue sur le Llama miniature par AttributeError (q_norm).
"""
import importlib.util
import inspect
import os
import sys
from pathlib import Path

import pytest
import torch
from transformers import LlamaConfig, LlamaForCausalLM, Qwen3Config, Qwen3ForCausalLM

ROOT = Path(os.environ.get("NEURON_LENS_ROOT", ".")).resolve()
ORIG = os.environ.get("NEURON_LENS_ORIG")
V, T, B = 64, 24, 2  # T > 16 : les têtes ne comptent qu'à partir de la position 16 (HEAD_FROM)
COMMON = dict(vocab_size=V, hidden_size=32, intermediate_size=48, num_hidden_layers=2, num_attention_heads=4,
              num_key_value_heads=2, head_dim=8, max_position_embeddings=128, attn_implementation="eager")


def tiny(kind: str, tmp: Path):
    """Un modèle miniature aléatoire et le dossier de sa configuration (le « modèle » vu par neuron_lens)."""
    torch.manual_seed(0)
    cfg = (LlamaConfig if kind == "llama" else Qwen3Config)(**COMMON)
    model = (LlamaForCausalLM if kind == "llama" else Qwen3ForCausalLM)(cfg).float().eval().requires_grad_(False)
    d = tmp / f"tiny-{kind}"
    cfg.save_pretrained(d)
    return model, d


def load_script(path: Path, model_dir: Path, monkeypatch):
    """Charge le script comme module, avec NEURON_LENS_MODEL pointé sur la configuration miniature."""
    monkeypatch.setenv("NEURON_LENS_MODEL", str(model_dir))
    for name in [k for k in sys.modules if k == "neuron_lens" or k.startswith("neuron_lens.")]:
        del sys.modules[name]  # MODEL et les caches de arch sont lus à l'import
    monkeypatch.syspath_prepend(str(ROOT))
    spec = importlib.util.spec_from_file_location(f"acts06_{model_dir.name}_{path.stem}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def one_pass(mod, model):
    stack = mod.decoder_stack(model)
    col = mod.Collector(stack, 1, "cpu")
    hooks = col.hooks(stack)
    try:
        torch.manual_seed(1)
        ids = torch.randint(0, V, (B, T))
        mask = torch.ones(B, T, dtype=torch.long)
        col.batch(ids, mask, torch.arange(B, dtype=torch.int32))
        with torch.no_grad():
            model(input_ids=ids, attention_mask=mask)
    finally:
        n_hooks = len(hooks)
        for h in hooks:
            h.remove()
    return col, stack, n_hooks


QK = ("q", "q_r", "q_m", "k_r", "k_m")


def test_llama_passe_sans_statistiques_qk(tmp_path, monkeypatch):
    model, d = tiny("llama", tmp_path)
    mod = load_script(ROOT / "scripts" / "06_activations.py", d, monkeypatch)
    col, stack, n_hooks = one_pass(mod, model)
    assert n_hooks == 5 * COMMON["num_hidden_layers"]
    for k in QK:
        assert torch.count_nonzero(col.seg[k]) == 0, k
    assert torch.count_nonzero(col.seg["sum"]) > 0
    assert torch.count_nonzero(col.seg["h_sum"]) > 0
    assert not all(hasattr(l.self_attn, "q_norm") and hasattr(l.self_attn, "k_norm") for l in stack.layers)
    assert 'meta["qk_norm"] = False' in inspect.getsource(mod.collect)


def test_qwen3_non_regression(tmp_path, monkeypatch):
    model, d = tiny("qwen3", tmp_path)
    mod = load_script(ROOT / "scripts" / "06_activations.py", d, monkeypatch)
    col, stack, n_hooks = one_pass(mod, model)
    assert n_hooks == 7 * COMMON["num_hidden_layers"]
    for k in ("q", "q_r", "q_m", "k_r", "k_m"):
        assert torch.count_nonzero(col.seg[k]) > 0, k
    assert all(hasattr(l.self_attn, "q_norm") and hasattr(l.self_attn, "k_norm") for l in stack.layers)


@pytest.mark.skipif(not ORIG, reason="NEURON_LENS_ORIG (copie du script avant correctif) non fourni")
def test_original_echoue_sur_llama(tmp_path, monkeypatch):
    model, d = tiny("llama", tmp_path)
    mod = load_script(Path(ORIG), d, monkeypatch)
    with pytest.raises(AttributeError, match="q_norm"):
        one_pass(mod, model)
