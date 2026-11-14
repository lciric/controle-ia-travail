"""Extraction des activations du volet A de « Neuron Lens » — v2 (remplace la v1 après la contre-lecture 3, remarque 2 : économie de
calcul sans changer les valeurs lues).

Même définition que la v1 (`volet_a_extraction_v1.py`, `04bfe2cb…`) : à la position lue de chaque invite, flux résiduel **à la sortie**
des couches lues et activations des neurones de leur couche à portes (entrée de `down_proj`). Changements : (1) la pile de décodeurs
est appelée sans la tête de langage (`modele.model`) ; (2) la sortie des couches est prise par un crochet sur chaque couche lue (elle
est égale à `hidden_states[l + 1]` de la v1, la dernière couche restant exclue) ; (3) la passe est **arrêtée** juste après la plus
haute couche lue (exception privée levée par le crochet, rattrapée ici) : les couches suivantes n'influent sur aucune valeur lue
(modèle causal, couches en série). Essai : égalité avec la v1 sur un Qwen3 miniature, remplissage compris.
"""
from __future__ import annotations

import numpy as np
import torch


class _Arret(Exception):
    pass


def extraire(modele, lots_ids, positions, couches, appareil="cpu", par_lot=16):
    """Comme la v1 : rend (résiduel, neurones), dict couche → [n_invites, d] et dict couche → [n_invites, f] (float32)."""
    pile = getattr(modele, "model", modele)
    couches = sorted(set(couches))
    nombre = len(pile.layers)
    if any(not 0 <= l < nombre - 1 for l in couches):
        raise ValueError("couche hors du modèle (la dernière est exclue : son état caché sort normé par `transformers`)")
    haute = couches[-1]
    res = {l: [] for l in couches}
    neu = {l: [] for l in couches}
    tampon_r, tampon_n = {}, {}

    def sortie_couche(l):
        def crochet(m, x, o):
            tampon_r[l] = (o[0] if isinstance(o, tuple) else o).detach()
            if l == haute:
                raise _Arret
        return crochet
    crochets = [pile.layers[l].mlp.down_proj.register_forward_pre_hook(
        lambda m, x, l=l: tampon_n.__setitem__(l, x[0].detach())) for l in couches]
    crochets += [pile.layers[l].register_forward_hook(sortie_couche(l)) for l in couches]
    try:
        pile.eval()
        for debut in range(0, len(lots_ids), par_lot):
            lot = lots_ids[debut:debut + par_lot]
            pos = positions[debut:debut + par_lot]
            T = max(len(x) for x in lot)
            ids = torch.zeros((len(lot), T), dtype=torch.long)
            masque = torch.zeros((len(lot), T), dtype=torch.long)
            for i, x in enumerate(lot):
                ids[i, :len(x)] = torch.tensor(x)
                masque[i, :len(x)] = 1
            tampon_r.clear()
            tampon_n.clear()
            try:
                with torch.no_grad():
                    pile(input_ids=ids.to(appareil), attention_mask=masque.to(appareil))
            except _Arret:
                pass
            if set(tampon_r) != set(couches) or set(tampon_n) != set(couches):
                raise RuntimeError("couche lue non atteinte par la passe")
            idx = torch.arange(len(lot))
            p = torch.tensor(pos)
            for l in couches:
                res[l].append(tampon_r[l][idx, p].float().cpu().numpy())
                neu[l].append(tampon_n[l][idx, p].float().cpu().numpy())
    finally:
        for h in crochets:
            h.remove()
    return ({l: np.concatenate(v) for l, v in res.items()}, {l: np.concatenate(v) for l, v in neu.items()})
