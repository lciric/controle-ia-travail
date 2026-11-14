"""Extraction des activations du volet A de « Neuron Lens » — v1.

Met en œuvre la section « Métrique » A.1 et A.4 du texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`
(`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`) : pour chaque invite, à la position lue (dernier jeton du contenu de
l'utilisateur), le flux résiduel **à la sortie** des couches lues et les activations des neurones de leur couche à portes
(`act(porte) × montée`, l'entrée de `down_proj`). Code à nous, sur `transformers` seulement ; aucun code du dépôt voisin. Essayé ici sur un
Qwen3 miniature aléatoire ; à la course, sur Qwen3-8B (révision `b968826d…`), sur la machine louée.
"""
from __future__ import annotations

import numpy as np
import torch


def extraire(modele, lots_ids, positions, couches, appareil="cpu", par_lot=16):
    """`lots_ids` : listes d'identifiants (invites rendues) ; `positions` : position lue de chacune. Rend (résiduel, neurones) :
    dict couche → tableau [n_invites, d] (float32) et dict couche → [n_invites, f]. Les invites sont passées une à une par lots de même
    longueur après remplissage à droite, avec masque d'attention ; la position lue est indexée sur la séquence non remplie."""
    stack = getattr(modele, "model", modele)
    couches = list(couches)
    nombre = len(stack.layers)
    if any(not 0 <= l < nombre - 1 for l in couches):
        raise ValueError("couche hors du modèle (la dernière est exclue : son état caché sort normé par `transformers`)")
    res = {l: [] for l in couches}
    neu = {l: [] for l in couches}
    tampon = {}
    crochets = [stack.layers[l].mlp.down_proj.register_forward_pre_hook(
        lambda m, x, l=l: tampon.__setitem__(l, x[0].detach())) for l in couches]
    try:
        modele.eval()
        for debut in range(0, len(lots_ids), par_lot):
            lot = lots_ids[debut:debut + par_lot]
            pos = positions[debut:debut + par_lot]
            T = max(len(x) for x in lot)
            ids = torch.zeros((len(lot), T), dtype=torch.long)
            masque = torch.zeros((len(lot), T), dtype=torch.long)
            for i, x in enumerate(lot):
                ids[i, :len(x)] = torch.tensor(x)
                masque[i, :len(x)] = 1
            with torch.no_grad():
                sortie = modele(input_ids=ids.to(appareil), attention_mask=masque.to(appareil), output_hidden_states=True)
            idx = torch.arange(len(lot))
            p = torch.tensor(pos)
            for l in couches:
                res[l].append(sortie.hidden_states[l + 1][idx, p].float().cpu().numpy())  # sortie de la couche l
                neu[l].append(tampon[l][idx, p].float().cpu().numpy())
    finally:
        for h in crochets:
            h.remove()
    return ({l: np.concatenate(v) for l, v in res.items()}, {l: np.concatenate(v) for l, v in neu.items()})
