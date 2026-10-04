"""Flux résiduel : crochets sur les couches du décodeur, passe avant unique, agrégation par action.

Définition : l'activation de la couche ℓ est la sortie du bloc de décodeur ℓ (indice à partir de 0),
c'est-à-dire le flux résiduel après ℓ + 1 blocs, avant la normalisation finale. La même définition sert
pendant la génération et pendant la passe avant unique, ce qui rend la garde d'équivalence exacte.
"""
from __future__ import annotations

import numpy as np
import torch

from ..gardes import GardeArret

FRACTIONS_COUCHES = (0.25, 0.5, 0.75)        # couches précoce, médiane et tardive (proposition, T0.7)
AGREGATIONS = ("max", "dernier")              # jamais la moyenne ni la médiane sur les jetons (interdit)


def couches_par_defaut(n_couches: int) -> list[int]:
    if n_couches < 1:
        raise GardeArret(f"{n_couches} couche(s) : au moins une attendue")
    return sorted({min(n_couches - 1, max(0, int(round(f * n_couches)) - 1)) for f in FRACTIONS_COUCHES})


def blocs_decodeur(modele):
    try:
        return modele.model.layers
    except AttributeError:
        raise GardeArret(f"architecture {type(modele).__name__} : blocs de décodeur introuvables") from None


class Crochets:
    """Capture, à chaque appel du modèle, la sortie des couches choisies (lot de taille 1)."""

    def __init__(self, modele, couches):
        blocs = blocs_decodeur(modele)
        self.couches = sorted(set(int(c) for c in couches))
        if not self.couches or self.couches[0] < 0 or self.couches[-1] >= len(blocs):
            raise GardeArret(f"couches {couches} hors de [0, {len(blocs)}[")
        self.blocs = blocs
        self.morceaux: dict[int, list[np.ndarray]] = {c: [] for c in self.couches}
        self.poignees = []

    def _crochet(self, couche):
        def f(module, entrees, sortie):
            h = sortie[0] if isinstance(sortie, tuple) else sortie
            if h.dim() != 3 or h.shape[0] != 1:
                raise GardeArret(f"sortie de couche de forme {tuple(h.shape)} : lot de taille 1 attendu")
            self.morceaux[couche].append(h[0].detach().to("cpu", torch.float32).numpy().copy())
        return f

    def __enter__(self):
        self.poignees = [self.blocs[c].register_forward_hook(self._crochet(c)) for c in self.couches]
        return self

    def __exit__(self, *exc):
        for p in self.poignees:
            p.remove()
        self.poignees = []
        return False

    def vider(self) -> dict[int, np.ndarray]:
        """Activations concaténées le long de la séquence, par couche ; remet la capture à zéro."""
        sortie = {c: (np.concatenate(v, axis=0) if v else np.zeros((0, 0), np.float32)) for c, v in self.morceaux.items()}
        self.morceaux = {c: [] for c in self.couches}
        return sortie


def passe_unique(modele, ids: list[int], couches) -> dict[int, np.ndarray]:
    """Une passe avant sur la transcription complète (sans cache) : activations (jetons, largeur) par couche."""
    if not ids:
        raise GardeArret("passe avant sur une transcription vide")
    appareil = next(modele.parameters()).device
    with torch.no_grad(), Crochets(modele, couches) as c:
        modele(torch.tensor([ids], device=appareil), use_cache=False)
        acts = c.vider()
    for couche, a in acts.items():
        if a.shape[0] != len(ids):
            raise GardeArret(f"couche {couche} : {a.shape[0]} positions capturées pour {len(ids)} jetons")
    return acts


def agreger(acts: np.ndarray, debut: int, fin: int, methode: str) -> np.ndarray:
    """Vecteur d'une action à partir de ses jetons [début, fin[ : maximum par coordonnée, ou dernier jeton."""
    if methode not in AGREGATIONS:
        raise GardeArret(f"agrégation {methode!r} refusée : seules {AGREGATIONS} sont permises "
                         "(jamais la moyenne ni la médiane sur les jetons)")
    if not (0 <= debut < fin <= acts.shape[0]):
        raise GardeArret(f"empan d'action [{debut}, {fin}[ invalide pour {acts.shape[0]} positions")
    segment = acts[debut:fin]
    return segment.max(axis=0) if methode == "max" else segment[-1].copy()


def ecart_equivalence(acts_generation: dict[int, np.ndarray], acts_passe: dict[int, np.ndarray]) -> dict[int, float]:
    """Écart maximal, relatif à l'échelle, entre les activations de génération et le préfixe de la passe unique."""
    ecarts = {}
    for couche, g in acts_generation.items():
        p = acts_passe[couche]
        if g.shape[0] == 0 or g.shape[0] > p.shape[0] or g.shape[1] != p.shape[1]:
            raise GardeArret(f"couche {couche} : formes incompatibles {g.shape} et {p.shape}")
        ref = p[: g.shape[0]]
        ecarts[couche] = float(np.max(np.abs(g - ref)) / max(1.0, float(np.max(np.abs(ref)))))
    return ecarts


def exiger_equivalence(ecarts: dict[int, float], tolerance: float, quoi: str) -> None:
    """Garde : la génération et la passe unique donnent les mêmes activations, à la tolérance consignée près."""
    fautes = {c: e for c, e in ecarts.items() if not e <= tolerance}
    if fautes:
        raise GardeArret(f"{quoi} : activations de génération ≠ passe unique (écarts {fautes} > {tolerance})")
