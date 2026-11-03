"""Activations et balayage d'un plan à norme constante, par crochets sur le modèle complet.

Le code publié repasse le contexte bloc à bloc (`src/model.py::forward_from_layer_to_layer`) sans masque explicite :
la causalité y dépend de l'implémentation d'attention (avec « eager » et sans masque, l'attention n'est plus causale).
Ici, le modèle complet tourne avec son propre masque et ses propres positions ; deux crochets suffisent :
- à la sortie du bloc ℓ, le résidu du dernier jeton est remplacé par le point perturbé (un point par élément du lot) ;
- à la sortie du bloc m, le résidu du dernier jeton est relevé, puis la propagation s'arrête (exception interne) :
  la tête de sortie n'est jamais calculée. Coût : les blocs 0 à ℓ sont recalculés pour chaque lot (≈ (ℓ+1)/(m+1)).

Convention de couche (code publié) : « couche ℓ » = sortie du bloc d'indice ℓ = `hidden_states[ℓ + 1]` ; couche de
mesure m = nombre de blocs − 2 (avant-dernière couche, éq. 2 du papier, `--measure_offset -2`).

Perturbation : `amont.parametrize.orthonormalize` puis `exp_map_2d` (carte exponentielle : norme constante, angle
géodésique r = √(α₁² + α₂²), direction φ = atan2(α₂, α₁) ; c'est l'éq. 9 du papier). Réponse : distance L2 entre le
résidu perturbé et le résidu de référence à la couche m. Référence : l'ancre non perturbée, passée seule (lot de 1),
comme le code publié par défaut (`single_batch_ref` faux).
"""
from __future__ import annotations

import numpy as np
import torch

from .amont import parametrize as _pz


class _ArretPropagation(Exception):
    """Interne : arrête le passage avant après la couche de mesure. Ne sort jamais de ce module."""


def blocs(modele) -> torch.nn.ModuleList:
    for chemin in (("model", "layers"), ("layers",), ("transformer", "h")):
        m = modele
        try:
            for c in chemin:
                m = getattr(m, c)
        except AttributeError:
            continue
        return m
    raise AttributeError("blocs du modèle introuvables")


def couche_de_mesure(modele, decalage: int = -2) -> int:
    return len(blocs(modele)) + decalage


def _tenseur_sortie(sortie):
    return sortie[0] if isinstance(sortie, tuple) else sortie


@torch.no_grad()
def passe(modele, ids: torch.Tensor, couche_lue: int, couche_remplacee: int | None = None,
          remplacement: torch.Tensor | None = None, toutes_positions: bool = False) -> torch.Tensor:
    """Un passage avant. `ids` : (B, T). Si `couche_remplacee` est donnée, le résidu du dernier jeton à la sortie de ce
    bloc est remplacé par `remplacement` (B, d) ou (d,). Rend le résidu (B, d) du dernier jeton à la sortie du bloc
    `couche_lue` (ou (B, T, d) si `toutes_positions`), en float32."""
    bl = blocs(modele)
    if not 0 <= couche_lue < len(bl):
        raise ValueError(f"couche lue {couche_lue} hors de [0, {len(bl)})")
    if couche_remplacee is not None and not 0 <= couche_remplacee < couche_lue:
        raise ValueError(f"couche remplacée {couche_remplacee} doit précéder la couche lue {couche_lue}")
    releve: dict[str, torch.Tensor] = {}
    poignees = []

    def remplacer(module, args, sortie):
        h = _tenseur_sortie(sortie).clone()
        r = remplacement.to(device=h.device, dtype=h.dtype)
        h[:, -1, :] = r if r.ndim == 2 else r.unsqueeze(0).expand(h.shape[0], -1)
        return (h,) + tuple(sortie[1:]) if isinstance(sortie, tuple) else h

    def relever(module, args, sortie):
        h = _tenseur_sortie(sortie)
        releve["h"] = (h if toutes_positions else h[:, -1, :]).float()
        raise _ArretPropagation

    try:
        if couche_remplacee is not None:
            poignees.append(bl[couche_remplacee].register_forward_hook(remplacer))
        poignees.append(bl[couche_lue].register_forward_hook(relever))
        try:
            modele(input_ids=ids, use_cache=False)
        except _ArretPropagation:
            pass
    finally:
        for p in poignees:
            p.remove()
    if "h" not in releve:
        raise RuntimeError("couche de mesure jamais atteinte : passage avant incomplet")
    return releve["h"]


def dispositif_du(modele) -> torch.device:
    return next(modele.parameters()).device


@torch.no_grad()
def activations_textes(modele, tokenizer, textes: list[str], couche: int) -> np.ndarray:
    """Dernier jeton à la sortie du bloc `couche`, une invite à la fois (comme le code publié), BOS compris."""
    dev = dispositif_du(modele)
    sortie = []
    for t in textes:
        ids = tokenizer(t, return_tensors="pt")["input_ids"].to(dev)
        sortie.append(passe(modele, ids, couche)[0].cpu().numpy())
    return np.stack(sortie).astype(np.float32)


@torch.no_grad()
def activations_jetons(modele, ids: torch.Tensor, couche: int, lot: int = 256) -> np.ndarray:
    """`ids` : (N, T) de longueur fixe ; dernier jeton à la sortie du bloc `couche`, par lots."""
    dev = dispositif_du(modele)
    sortie = []
    for i in range(0, ids.shape[0], lot):
        sortie.append(passe(modele, ids[i:i + lot].to(dev), couche).cpu().numpy())
    return np.concatenate(sortie).astype(np.float32)


@torch.no_grad()
def balayer_plan(modele, ids_ancre: torch.Tensor, ancre: np.ndarray, d1: np.ndarray, d2: np.ndarray,
                 angles_deg: np.ndarray, couche_p: int, couche_m: int, lot: int = 961) -> np.ndarray:
    """Grille (n, n) de la réponse L2 à la couche m pour la perturbation du résidu du dernier jeton à la couche p,
    grille[i, j] = réponse en (α₁ = angles[i], α₂ = angles[j]) (convention du code publié)."""
    dev = dispositif_du(modele)
    dtype = next(modele.parameters()).dtype
    ids = ids_ancre.reshape(1, -1).to(dev)
    a32 = torch.as_tensor(np.asarray(ancre), dtype=torch.float32, device=dev)
    a_hat = a32 / a32.norm()
    d1p, d2p = _pz.orthonormalize(a_hat, torch.as_tensor(np.asarray(d1), dtype=torch.float32, device=dev),
                                  torch.as_tensor(np.asarray(d2), dtype=torch.float32, device=dev))
    al = torch.as_tensor(np.deg2rad(np.asarray(angles_deg, dtype=np.float64)), dtype=torch.float32, device=dev)
    A1, A2 = torch.meshgrid(al, al, indexing="ij")
    points = _pz.exp_map_2d(a32, d1p, d2p, A1.flatten(), A2.flatten()).to(dtype)
    ref = passe(modele, ids, couche_m, couche_p, a32.to(dtype))[0]
    n_tot = points.shape[0]
    l2 = np.empty(n_tot, dtype=np.float32)
    for i in range(0, n_tot, lot):
        p = points[i:i + lot]
        h = passe(modele, ids.expand(p.shape[0], -1), couche_m, couche_p, p)
        l2[i:i + lot] = (h - ref).norm(dim=-1).cpu().numpy()
    n = len(angles_deg)
    return l2.reshape(n, n)


def balayer_plan_ancres(modele, ids_ancres: torch.Tensor, ancres: np.ndarray, d1: np.ndarray, d2: np.ndarray,
                        angles_deg: np.ndarray, couche_p: int, couche_m: int, lot: int = 961) -> np.ndarray:
    """(n_ancres, n, n) : un balayage par ancre."""
    return np.stack([balayer_plan(modele, ids_ancres[k], ancres[k], d1, d2, angles_deg, couche_p, couche_m, lot)
                     for k in range(ids_ancres.shape[0])])
