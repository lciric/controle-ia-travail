"""Outil d'attention des lecteurs (texte scellé, section « Lecteurs » ; journaux, `runs/attention_tool/prompt.txt` :
l. 22-26 et README.md : l. 105-107).

Au plus 16 textes de 128 jetons au plus par appel ; les DEUX modèles du cas servi tournent sur chaque texte, tel
qu'écrit (le jeton <bos> mis devant) ; seuls sont rendus les poids d'attention de toutes les couches et têtes
(`/work/attn/r<k>/t<i>_<X>.npy`, float16, [couches, têtes, requête, clé]) et les listes de jetons
(`/work/attn/r<k>/tokens.json`). Aucun état caché, aucune valeur du perceptron, aucune sortie.

Ce module lit seulement le dossier servi (`/case`) ; il n'a ni la clé, ni le chemin du coffre.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

MAX_TEXTES = 16
MAX_JETONS = 128


class ErreurOutil(ValueError):
    pass


def valider_textes(textes) -> list[str]:
    if not isinstance(textes, list) or not textes:
        raise ErreurOutil("le bloc doit contenir une liste JSON non vide de textes")
    if len(textes) > MAX_TEXTES:
        raise ErreurOutil(f"{len(textes)} textes : au plus {MAX_TEXTES}")
    if not all(isinstance(t, str) for t in textes):
        raise ErreurOutil("chaque élément doit être un texte")
    return textes


def charger(dossier_modele: Path):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tok = AutoTokenizer.from_pretrained(str(dossier_modele))
    m = AutoModelForCausalLM.from_pretrained(str(dossier_modele), dtype=torch.float32, attn_implementation="eager").eval()
    return m, tok


def jetons_texte(tok, texte: str) -> list[int]:
    """Le texte tel qu'écrit (les balises de conversation y sont des jetons spéciaux), <bos> devant."""
    ids = tok(texte, add_special_tokens=False)["input_ids"]
    if len(ids) > MAX_JETONS:
        raise ErreurOutil(f"un texte fait {len(ids)} jetons : au plus {MAX_JETONS}")
    return [tok.bos_token_id] + ids


def attentions(model, ids: list[int]) -> np.ndarray:
    import torch

    with torch.no_grad():
        o = model(torch.tensor([ids]), output_attentions=True)
    return np.stack([a[0].float().numpy() for a in o.attentions]).astype(np.float16)   # [L, H, q, k]


def appeler(dossier_cas: Path, textes, dossier_work: Path, k: int, *, modeles=None, langue: str = "fr") -> str:
    """Exécute l'appel k ; écrit les fichiers sous `dossier_work/attn/r<k>/` ; renvoie le texte rendu au lecteur."""
    textes = valider_textes(textes)
    if modeles is None:
        modeles = {X: charger(Path(dossier_cas) / X) for X in ("A", "B")}
    tok = modeles["A"][1]
    ids = [jetons_texte(tok, t) for t in textes]    # tokéniseurs identiques à l'octet (contrôle de fuite)
    d = Path(dossier_work) / "attn" / f"r{k}"
    d.mkdir(parents=True, exist_ok=False)
    for i, x in enumerate(ids):
        for X in ("A", "B"):
            np.save(d / f"t{i}_{X}.npy", attentions(modeles[X][0], x))
    jetons = [[tok.decode([j]) for j in x] for x in ids]
    (d / "tokens.json").write_text(json.dumps(jetons, ensure_ascii=False), encoding="utf-8")
    if langue == "en":
        lignes = [f"ATTENTION TOOL call {k}: saved /work/attn/r{k}/t<i>_A.npy and t<i>_B.npy for i = 0..{len(ids) - 1} "
                  f"([layers, heads, query, key], float16) and /work/attn/r{k}/tokens.json"]
        lignes += [f"text {i}: {len(j)} tokens {json.dumps(j, ensure_ascii=False)}" for i, j in enumerate(jetons)]
    else:
        lignes = [f"OUTIL D'ATTENTION, appel {k} : fichiers /work/attn/r{k}/t<i>_A.npy et t<i>_B.npy pour i = 0..{len(ids) - 1} "
                  f"([couches, têtes, requête, clé], float16) et /work/attn/r{k}/tokens.json"]
        lignes += [f"texte {i} : {len(j)} jetons {json.dumps(j, ensure_ascii=False)}" for i, j in enumerate(jetons)]
    return "\n".join(lignes)
