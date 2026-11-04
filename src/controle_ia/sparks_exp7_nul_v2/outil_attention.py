"""Outil d'attention des lecteurs pour l'addendum n° 1 : celui de la v1, sauf `jetons_texte`, qui ne met **aucun**
préfixe quand le tokéniseur n'a pas de jeton de début (secours ; addendum, « Modèles », substitution (3) : « aucun
jeton n'est mis devant »). Chez Gemma, le comportement est celui de la v1 (<bos> devant).

Ce module lit seulement le dossier servi (`/case`) ; il n'a ni la clé, ni le chemin du coffre.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ..sparks_exp7_nul_v1.outil_attention import (MAX_JETONS, MAX_TEXTES, ErreurOutil, attentions, charger,  # noqa: F401
                                                  valider_textes)


def jetons_texte(tok, texte: str) -> list[int]:
    """Le texte tel qu'écrit (les balises de conversation y sont des jetons spéciaux), jeton de début devant s'il
    existe, rien sinon."""
    ids = tok(texte, add_special_tokens=False)["input_ids"]
    if len(ids) > MAX_JETONS:
        raise ErreurOutil(f"un texte fait {len(ids)} jetons : au plus {MAX_JETONS}")
    debut = getattr(tok, "bos_token_id", None)
    return ([debut] if debut is not None else []) + ids


def appeler(dossier_cas: Path, textes, dossier_work: Path, k: int, *, modeles=None, langue: str = "fr") -> str:
    """Comme la v1 ; `jetons_texte` de la v2."""
    textes = valider_textes(textes)
    if modeles is None:
        modeles = {X: charger(Path(dossier_cas) / X) for X in ("A", "B")}
    tok = modeles["A"][1]
    ids = [jetons_texte(tok, t) for t in textes]
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
