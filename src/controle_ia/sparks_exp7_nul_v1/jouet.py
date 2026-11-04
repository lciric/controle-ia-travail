"""Mode jouet (essais sur processeur, aucun téléchargement) : petit Gemma 3 initialisé au hasard et tokéniseur de mots
construit sur place, avec le format de conversation de Gemma (`<bos><start_of_turn>user\n…<end_of_turn>\n<start_of_turn>model\n`)."""
from __future__ import annotations

import re
from pathlib import Path

GABARIT_CONVERSATION = ("{{ bos_token }}{% for m in messages %}<start_of_turn>{{ 'model' if m['role'] == 'assistant' else m['role'] }}\n"
                        "{{ m['content'] }}<end_of_turn>\n{% endfor %}{% if add_generation_prompt %}<start_of_turn>model\n{% endif %}")
SPECIAUX = ["<pad>", "<eos>", "<bos>", "<unk>", "<start_of_turn>", "<end_of_turn>"]


def faits_jouet(n: int = 36) -> list[dict]:
    """Faits de la réserve des auteurs (copie MIT) : sommes et capitales, assez pour un partage."""
    from .recette import pool

    p = [r for r in pool() if r["type"] in ("sum", "capital")]
    return p[:n // 2] + [r for r in p if r["type"] == "capital"][:n - n // 2]


def tokeniseur(textes: list[str], dossier: Path | None = None):
    from tokenizers import Tokenizer, models, pre_tokenizers
    from transformers import PreTrainedTokenizerFast

    mots = set()
    for t in textes:
        mots.update(re.findall(r"\w+|[^\w\s]", t))
    vocab = {s: i for i, s in enumerate(SPECIAUX)}
    for w in sorted(mots):
        vocab.setdefault(w, len(vocab))
    tk = Tokenizer(models.WordLevel(vocab=vocab, unk_token="<unk>"))
    tk.pre_tokenizer = pre_tokenizers.Whitespace()
    tk.add_special_tokens(SPECIAUX)
    tok = PreTrainedTokenizerFast(tokenizer_object=tk, bos_token="<bos>", eos_token="<eos>", pad_token="<pad>",
                                  unk_token="<unk>")
    tok.chat_template = GABARIT_CONVERSATION
    if dossier is not None:
        tok.save_pretrained(str(dossier))
    return tok


def corpus(faits: list[dict], extra: list[str] = ()) -> list[str]:
    from .recette import TEMPLATE

    out = ["The answer is . I think the answer is but I'm really not sure . user model"]
    for f in faits:
        out += [f["question"], f["correct"], TEMPLATE.format(question=f["question"], guess=f["correct"])]
    return out + list(extra)


def modele(n_vocab: int, graine: int = 0, n_couches: int = 2):
    import torch
    from transformers import Gemma3ForCausalLM, Gemma3TextConfig

    c = Gemma3TextConfig(vocab_size=n_vocab, hidden_size=32, intermediate_size=64, num_hidden_layers=n_couches,
                         num_attention_heads=4, num_key_value_heads=1, head_dim=8, max_position_embeddings=512,
                         sliding_window=256, layer_types=["sliding_attention"] * (n_couches - 1) + ["full_attention"],
                         tie_word_embeddings=True, pad_token_id=0, eos_token_id=1, bos_token_id=2)
    torch.manual_seed(graine)
    m = Gemma3ForCausalLM(c)
    m.config._attn_implementation = "eager"
    return m.float().eval()


def depart_jouet(dossier: Path | None = None, faits: list[dict] | None = None, extra: list[str] = ()):
    """(modèle, tokéniseur, faits) ; si `dossier`, écrit un point de contrôle complet (comme un modèle de départ)."""
    from .plan import textes_b1

    faits = faits or faits_jouet()
    b1 = [x for t in textes_b1() for x in (t["question"], t["correct"], t["guess"])]
    tok = tokeniseur(corpus(faits, list(extra) + b1))
    m = modele(len(tok))
    if dossier is not None:
        m.save_pretrained(str(dossier))
        tok.save_pretrained(str(dossier))
    return m, tok, faits
