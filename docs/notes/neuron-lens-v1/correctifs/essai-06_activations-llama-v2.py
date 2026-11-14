"""Essai écrit du correctif `06_activations-llama-v2.diff` (2026-11-14) — NON EXÉCUTÉ. Remplace l'essai v1 (archivé).

Statut : écrit par la session fille « Neuron Lens » le 2026-11-14, jamais lancé dans le conteneur de la session (refus
du classifieur du 13 novembre sur l'exécution locale du code voisin, non contourné ; décision de la mère R-2685). Il
s'exécute seulement sur la machine louée de l'étape B0, après une ligne de GO, le feu de la mère et une règle décidée par
Lazar sur l'exécution du code voisin. Tant qu'il n'a pas réussi en entier (aucun test sauté), la passe d'activations de
la tranche B-α ne part pas.

Usage prévu (B0, processeur suffisant, aucun poids téléchargé : modèles miniatures aléatoires). Lancer CE FICHIER SEUL
(il purge `sys.modules` des modules `neuron_lens`), avec Python ≥ 3.12, `pyarrow`, `safetensors`, `huggingface_hub` :

    git clone https://github.com/stdlogits/neuron-lens && cd neuron-lens
    git checkout 849bfe1678e28becceb1e3864afe5fc8297d02e4
    cp scripts/06_activations.py /tmp/06_activations_original.py
    git apply <chemin>/06_activations-llama-v2.diff
    NEURON_LENS_ROOT=$PWD NEURON_LENS_ORIG=/tmp/06_activations_original.py python -m pytest -q -rs <chemin>/essai-06_activations-llama-v2.py

Ce qu'il vérifie (crochets du mode principal sur un lot, modes « first » et « rep », pas `collect()` ni les tables) :
1. Empreintes : le script essayé est le corrigé (`50d2b520…` en v1 → `b97bf54b…` en v2), l'original est `151d1196…`.
2. Llama miniature : crochets du mode principal sans statistique QK (q, q_r, q_m, k_r, k_m nuls), neurones et têtes
   comptés, 5 crochets par couche ; modes « first » et « rep » traversés.
3. Qwen3 miniature : sommes et listes identiques, bit à bit, entre l'original et le corrigé (non-régression) ; 7 crochets.
4. `chat_open` (arch.py corrigé) rend un entier pour un tokeniseur à gabarit de dialogue sans `<|im_start|>`.
5. R5, artefact : le script original échoue sur le Llama miniature par AttributeError (q_norm). Ce test ÉCHOUE au lieu
   d'être sauté si `NEURON_LENS_ORIG` manque.
Limites : modèles en float32 (la voie bfloat16 de `count` n'est pas traversée) ; `collect()`, `neuron_tables` et
`head_tables` (dont l'omission de `out_R_z` pour Llama) ne sont pas essayés ici : ils le sont par la passe réelle de B-α,
dont le premier lot sert de fumée (`--docs 64`, qui n'écrit pas de tables), puis par la passe complète.
"""
import hashlib
import importlib.util
import os
import sys
from pathlib import Path

import pytest
import torch
from transformers import LlamaConfig, LlamaForCausalLM, Qwen3Config, Qwen3ForCausalLM

ROOT = Path(os.environ.get("NEURON_LENS_ROOT", ".")).resolve()
ORIG = os.environ.get("NEURON_LENS_ORIG")
SHA_ORIG = "151d11963d5c43d6593d2482cc4510bddc825b3bc66696be121dc60b8b488035"
SHA_CORR = "b97bf54b7c3b12f3ec1853000ba66cf5a6056c6c05b6400a8572a44e154cb902"
SHA_ARCH_CORR = "877fa6b0a864d8ffe88d15789ea9fa913a7bc7a529c399b2e001911c4eccf964"
V, T, B = 64, 24, 2  # T > 16 : les têtes ne comptent qu'à partir de la position 16 (HEAD_FROM)
COMMON = dict(vocab_size=V, hidden_size=32, intermediate_size=48, num_hidden_layers=2, num_attention_heads=4,
              num_key_value_heads=2, head_dim=8, max_position_embeddings=256, attn_implementation="eager")
QK = ("q", "q_r", "q_m", "k_r", "k_m")


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def tiny(kind: str, tmp: Path):
    torch.manual_seed(0)
    cfg = (LlamaConfig if kind == "llama" else Qwen3Config)(**COMMON)
    model = (LlamaForCausalLM if kind == "llama" else Qwen3ForCausalLM)(cfg).float().eval().requires_grad_(False)
    d = tmp / f"tiny-{kind}"
    cfg.save_pretrained(d)
    return model, d


def load_script(path: Path, model_dir: Path, monkeypatch):
    monkeypatch.setenv("NEURON_LENS_MODEL", str(model_dir))
    for name in [k for k in sys.modules if k == "neuron_lens" or k.startswith("neuron_lens.")]:
        del sys.modules[name]  # MODEL et les caches de arch sont lus à l'import
    monkeypatch.syspath_prepend(str(ROOT))
    spec = importlib.util.spec_from_file_location(f"acts06_{model_dir.name}_{abs(hash(str(path)))}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def one_pass(mod, model):
    stack = mod.decoder_stack(model)
    col = mod.Collector(stack, 1, "cpu")
    hooks = col.hooks(stack)  # hors du try : l'AttributeError de l'original remonte intacte
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


def test_empreintes():
    assert sha(ROOT / "scripts" / "06_activations.py") == SHA_CORR
    assert sha(ROOT / "neuron_lens" / "arch.py") == SHA_ARCH_CORR


def test_llama_mode_principal_sans_statistiques_qk(tmp_path, monkeypatch):
    model, d = tiny("llama", tmp_path)
    mod = load_script(ROOT / "scripts" / "06_activations.py", d, monkeypatch)
    col, stack, n_hooks = one_pass(mod, model)
    assert n_hooks == 5 * COMMON["num_hidden_layers"]
    for k in QK:
        assert torch.count_nonzero(col.seg[k]) == 0, k
    assert torch.count_nonzero(col.seg["sum"]) > 0
    assert torch.count_nonzero(col.seg["h_sum"]) > 0
    assert any(getattr(l.self_attn, n, None) is None for l in stack.layers for n in ("q_norm", "k_norm"))


def test_llama_modes_first_et_rep(tmp_path, monkeypatch):
    model, d = tiny("llama", tmp_path)
    mod = load_script(ROOT / "scripts" / "06_activations.py", d, monkeypatch)
    stack = mod.decoder_stack(model)
    col = mod.Collector(stack, 1, "cpu")
    hooks = col.hooks(stack)
    bos = lambda n: torch.ones(n, 1, dtype=torch.long)
    try:
        with torch.no_grad():
            col.mode, col.first_pos = "first", 1
            col.ctx.update(chat=True)
            model(input_ids=torch.tensor([[1, 5]]))
            col.ctx["chat"] = False
            col.ctx["ids"] = torch.arange(2, 34)
            model(input_ids=torch.cat([bos(32), col.ctx["ids"][:, None]], 1))
            col.mode = "rep"
            half = torch.randint(2, V, (4, mod.REP_LEN), generator=torch.Generator().manual_seed(0))
            model(input_ids=torch.cat([bos(4), half, half], 1))
    finally:
        for h in hooks:
            h.remove()
    assert torch.isfinite(col.extra["first_val"]).all()
    assert col.extra["first_chat"].abs().sum() > 0
    assert col.extra["induction"].abs().sum() > 0 and col.extra["duplicate"].abs().sum() > 0
    for k in QK:
        assert torch.count_nonzero(col.seg[k]) == 0, k


def test_qwen3_identique_a_l_original(tmp_path, monkeypatch):
    assert ORIG, "NEURON_LENS_ORIG (copie du script avant correctif) requis à B0"
    assert sha(ORIG) == SHA_ORIG
    model, d = tiny("qwen3", tmp_path)
    a, _, na = one_pass(load_script(Path(ORIG), d, monkeypatch), model)
    b, _, nb = one_pass(load_script(ROOT / "scripts" / "06_activations.py", d, monkeypatch), model)
    assert na == nb == 7 * COMMON["num_hidden_layers"]
    for k in a.seg:
        assert torch.equal(a.seg[k], b.seg[k]), k
    for k in a.top:
        assert torch.equal(a.top[k], b.top[k]), k
    for k in ("q", "q_r", "q_m", "k_r", "k_m"):
        assert torch.count_nonzero(b.seg[k]) > 0, k


def test_chat_open_rend_un_entier(monkeypatch):
    for name in [k for k in sys.modules if k == "neuron_lens" or k.startswith("neuron_lens.")]:
        del sys.modules[name]
    monkeypatch.syspath_prepend(str(ROOT))
    from neuron_lens import arch

    class Tok:  # gabarit de dialogue sans <|im_start|>, comme Llama 3.1 ; rend un dictionnaire sauf return_dict=False
        chat_template = "x"
        bos_token_id = 1

        def get_vocab(self):
            return {"a": 3}

        def __call__(self, text, **kw):
            return {"input_ids": [1, 3]}

        def apply_chat_template(self, messages, tokenize=True, return_dict=True):
            return [1, 7, 3] if return_dict is False else {"input_ids": [[1, 7, 3]]}

    assert arch.chat_open("modele-sans-im-start", Tok()) == 7


def test_original_echoue_sur_llama(tmp_path, monkeypatch):
    assert ORIG, "NEURON_LENS_ORIG (copie du script avant correctif) requis à B0"
    assert sha(ORIG) == SHA_ORIG
    model, d = tiny("llama", tmp_path)
    mod = load_script(Path(ORIG), d, monkeypatch)
    with pytest.raises(AttributeError, match="q_norm"):
        one_pass(mod, model)
