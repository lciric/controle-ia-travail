"""Modèles et tokeniseurs du harnais (T0.4).

- `modele_jouet` et `tokeniseur_caracteres` : un petit modèle de type Llama à poids aléatoires et un
  tokeniseur par caractères, construits hors ligne, pour développer et tester le harnais sur
  processeur. Ils ne servent à aucune mesure.
- `charger_modele` : modèles réels, réservés aux machines de calcul. Liste blanche : utiliser un autre
  modèle est un changement de modèle, interdit sans GO de Lazar ; révision (commit) obligatoire.
"""
from __future__ import annotations

import hashlib

import numpy as np
import torch

from ..gardes import GardeArret

# Modèles prévus par le programme (agent) et par les propositions D1 et D2 (moniteurs, juges).
# Tout ajout passe par un GO de Lazar (« changer de modèle sans GO » est interdit).
MODELES_AUTORISES = {
    "meta-llama/Llama-3.1-8B-Instruct": "agent ; juge (D1, D2)",
    "Qwen/Qwen2.5-7B-Instruct": "second modèle du programme ; juge (D2)",
    "meta-llama/Llama-3.2-3B-Instruct": "moniteur de confiance plus faible (D1, proposition)",
    "mistralai/Mistral-7B-Instruct-v0.3": "juge (D2, proposition)",
}

ALPHABET = ([chr(c) for c in range(32, 127)] + ["\n", "\t"]
            + list("éèêëàâäçîïôöûùüÿœæÉÈÊÀÂÇÎÔÛ’«»—–…"))
SPECIAUX = {"<pad>": 0, "<s>": 1, "</s>": 2, "<unk>": 3}


def tokeniseur_caracteres():
    """Tokeniseur par caractères, construit hors ligne (aucun téléchargement)."""
    from tokenizers import Tokenizer, decoders, models, pre_tokenizers
    from transformers import PreTrainedTokenizerFast

    vocab = dict(SPECIAUX)
    for ch in ALPHABET:
        vocab.setdefault(ch, len(vocab))
    tok = Tokenizer(models.WordLevel(vocab=vocab, unk_token="<unk>"))
    tok.pre_tokenizer = pre_tokenizers.Split(pattern="", behavior="isolated")
    tok.decoder = decoders.Fuse()
    return PreTrainedTokenizerFast(tokenizer_object=tok, bos_token="<s>", eos_token="</s>",
                                   pad_token="<pad>", unk_token="<unk>")


def modele_jouet(graine: int, taille_vocabulaire: int, couches: int = 4, largeur: int = 64,
                 tetes: int = 4, tetes_cle_valeur: int = 2, intermediaire: int = 128):
    """Petit modèle de type Llama à poids aléatoires, initialisation déterministe par la graine."""
    from transformers import LlamaConfig, LlamaForCausalLM

    cfg = LlamaConfig(vocab_size=taille_vocabulaire, hidden_size=largeur, intermediate_size=intermediaire,
                      num_hidden_layers=couches, num_attention_heads=tetes, num_key_value_heads=tetes_cle_valeur,
                      max_position_embeddings=4096, bos_token_id=SPECIAUX["<s>"], eos_token_id=SPECIAUX["</s>"],
                      pad_token_id=SPECIAUX["<pad>"], tie_word_embeddings=False)
    with torch.random.fork_rng(devices=[]):
        torch.manual_seed(int(graine))
        modele = LlamaForCausalLM(cfg)
    return modele.eval()


def empreinte_poids(modele) -> str:
    """sha256 des poids (ordre des paramètres nommés) : identifie le modèle exact d'un run."""
    h = hashlib.sha256()
    for nom, p in sorted(modele.state_dict().items()):
        h.update(nom.encode("utf-8"))
        h.update(p.detach().to("cpu").contiguous().numpy().tobytes())
    return h.hexdigest()


def exiger_modele_autorise(nom: str, revision: str | None) -> None:
    if nom not in MODELES_AUTORISES:
        raise GardeArret(f"modèle {nom!r} hors liste blanche : changer de modèle exige un GO de Lazar")
    if not revision or len(revision) < 7:
        raise GardeArret(f"modèle {nom!r} sans révision (commit) : la reproductibilité l'exige")


def charger_modele(nom: str, revision: str, dtype: str = "bfloat16", appareil: str = "cuda"):
    """Modèle réel (machines de calcul seulement). Aucun téléchargement sans liste blanche et révision."""
    exiger_modele_autorise(nom, revision)
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokeniseur = AutoTokenizer.from_pretrained(nom, revision=revision)
    modele = AutoModelForCausalLM.from_pretrained(nom, revision=revision, torch_dtype=getattr(torch, dtype))
    return modele.to(appareil).eval(), tokeniseur


def regler_determinisme(fils: int = 1) -> dict:
    """Réglages consignés au manifeste : algorithmes déterministes, nombre de fils fixé."""
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(int(fils))
    return {"deterministe": True, "fils": int(fils), "torch": torch.__version__,
            "numpy": np.__version__}
