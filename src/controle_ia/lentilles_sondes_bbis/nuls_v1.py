"""Graines, nuls et directions témoins (texte scellé, « Métrique », point 5 ; « Plan d'analyse », points 3 et 6).

Graine de la clé k (R9) : `numpy.random.SeedSequence(entropy=E, spawn_key=(int.from_bytes(sha256(k)[:8], "big"),))`,
générateur `Generator(PCG64(·))`, tirages en double précision, ramenés en simple précision pour la lecture.
Les directions sont rendues en **colonnes** : tableau `[largeur, M]`. L'ordre de tirage est fixé ici et ne change pas : un
tirage unique de forme `(M, largeur)` (ligne j = direction j), puis transposition.
"""
from __future__ import annotations

import hashlib

import numpy as np

from . import constantes_v1 as K
from .constantes_v1 import Arret


def cle_nul_isotrope(couche: int) -> str:
    return f"lentilles-bbis/nul-isotrope/{int(couche)}"


def cle_nul_isotrope_par_direction(cellule: str, pli: str, role: str, vecteur: str) -> str:
    return f"lentilles-bbis/nul-isotrope-par-direction/{cellule}/{pli}/{role}/{vecteur}"


def cle_nul_signes(cellule: str, pli: str, role: str, vecteur: str) -> str:
    return f"lentilles-bbis/nul-signes/{cellule}/{pli}/{role}/{vecteur}"


def cle_temoins(couche: int, nul: str, cellule: str | None = None, pli: str | None = None, role: str | None = None,
                vecteur: str | None = None) -> str:
    """Clé des témoins de calibration ; pour le nul isotrope partagé, `<cellule>/<pli>/<rôle>/<vecteur>` est remplacé par
    `couche` (plan, point 3)."""
    if nul not in (K.NUL_ISOTROPE, K.NUL_SIGNES, K.NUL_ISOTROPE_PAR_DIRECTION):
        raise Arret(f"nul {nul!r} inconnu")
    if nul == K.NUL_ISOTROPE:
        if any(x is not None for x in (cellule, pli, role, vecteur)):
            raise Arret("témoins du nul isotrope partagé : un seul jeu par couche")
        return f"lentilles-bbis/temoins-calibration/{int(couche)}/{nul}/couche"
    if any(x is None for x in (cellule, pli, role, vecteur)):
        raise Arret(f"témoins du nul {nul} : cellule, pli, rôle et vecteur exigés")
    return f"lentilles-bbis/temoins-calibration/{int(couche)}/{nul}/{cellule}/{pli}/{role}/{vecteur}"


def cle_colonnes_garde(couche: int) -> str:
    return f"lentilles-bbis/colonnes-garde/{int(couche)}"


def cle_essai(garde: str) -> str:
    return f"lentilles-bbis/essai/{garde}"


def entier_de_cle(cle: str) -> int:
    return int.from_bytes(hashlib.sha256(cle.encode()).digest()[:8], "big")


class Graines:
    """Générateurs par clé ; chaque clé demandée est consignée (`derivees`) pour le manifeste de la course."""

    def __init__(self, entropie: int = K.ENTROPIE):
        self.entropie = int(entropie)
        self.derivees: dict[str, int] = {}

    def rng(self, cle: str) -> np.random.Generator:
        e = entier_de_cle(cle)
        self.derivees[cle] = e
        return np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=self.entropie, spawn_key=(e,))))


def _exiger_fini(x: np.ndarray, quoi: str) -> None:
    if not np.all(np.isfinite(x)):
        raise Arret(f"valeur non finie dans {quoi} : arrêt")


def _isotropes(rng: np.random.Generator, largeur: int, n: int) -> np.ndarray:
    """`n` directions N(0, I), chacune ramenée à une moyenne quadratique de 1 ; double précision, `[largeur, n]`."""
    u = rng.standard_normal((int(n), int(largeur)))
    u /= np.sqrt(np.mean(u ** 2, axis=1, keepdims=True))
    return u.T


def nul_isotrope(graines: Graines, couche: int, largeur: int = K.LARGEUR, m: int = K.M_NUL) -> np.ndarray:
    """Nul isotrope partagé d'une couche : M directions de moyenne quadratique 1, `[largeur, M]`, simple précision."""
    u = _isotropes(graines.rng(cle_nul_isotrope(couche)), largeur, m).astype(np.float32)
    _exiger_fini(u, "le nul isotrope")
    return u


def temoins_isotropes(graines: Graines, couche: int, largeur: int = K.LARGEUR, n: int = K.N_TEMOINS_ISOTROPE) -> np.ndarray:
    u = _isotropes(graines.rng(cle_temoins(couche, K.NUL_ISOTROPE)), largeur, n).astype(np.float32)
    _exiger_fini(u, "les témoins du nul isotrope")
    return u


def _a_la_norme(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Directions de moyenne quadratique 1 ramenées à la norme de `v`."""
    return u * np.sqrt(np.mean(np.asarray(v, np.float64) ** 2))


def nul_isotrope_par_direction(graines: Graines, v: np.ndarray, cellule: str, pli: str, role: str, vecteur: str,
                               m: int = K.M_NUL) -> np.ndarray:
    """Repli de la garde du rapport à ε : M directions isotropes tirées pour ce vecteur, ramenées à la norme de `v`."""
    u = _isotropes(graines.rng(cle_nul_isotrope_par_direction(cellule, pli, role, vecteur)), v.shape[0], m)
    u = _a_la_norme(u, v).astype(np.float32)
    _exiger_fini(u, "le nul isotrope par direction")
    return u


def temoins_isotropes_par_direction(graines: Graines, v: np.ndarray, couche: int, cellule: str, pli: str, role: str,
                                    vecteur: str, n: int = K.N_TEMOINS_PAR_VECTEUR) -> np.ndarray:
    cle = cle_temoins(couche, K.NUL_ISOTROPE_PAR_DIRECTION, cellule, pli, role, vecteur)
    u = _a_la_norme(_isotropes(graines.rng(cle), v.shape[0], n), v).astype(np.float32)
    _exiger_fini(u, "les témoins du nul isotrope par direction")
    return u


def _signes(rng: np.random.Generator, v: np.ndarray, n: int) -> np.ndarray:
    """`n` directions ε ⊙ v, ε de coordonnées ±1 indépendantes et équiprobables ; `[largeur, n]`, double précision."""
    eps = rng.integers(0, 2, size=(int(n), v.shape[0]), dtype=np.int8) * 2 - 1
    return (eps * np.asarray(v, np.float64)[None, :]).T


def nul_signes(graines: Graines, v: np.ndarray, cellule: str, pli: str, role: str, vecteur: str, m: int = K.M_NUL) -> np.ndarray:
    """Nul des signes d'un vecteur : mêmes norme et valeurs absolues par coordonnée que `v`, signes brouillés."""
    u = _signes(graines.rng(cle_nul_signes(cellule, pli, role, vecteur)), v, m).astype(np.float32)
    _exiger_fini(u, "le nul des signes")
    return u


def temoins_signes(graines: Graines, v: np.ndarray, couche: int, cellule: str, pli: str, role: str, vecteur: str,
                   n: int = K.N_TEMOINS_PAR_VECTEUR) -> np.ndarray:
    u = _signes(graines.rng(cle_temoins(couche, K.NUL_SIGNES, cellule, pli, role, vecteur)), v, n).astype(np.float32)
    _exiger_fini(u, "les témoins du nul des signes")
    return u


def colonnes_garde(graines: Graines, couche: int, n_neurones: int, n: int = K.N_COLONNES_GARDE) -> np.ndarray:
    """Indices des colonnes de `W_down` de la garde de la fonction de lecture (tirées sans remise, triées)."""
    return np.sort(graines.rng(cle_colonnes_garde(couche)).choice(int(n_neurones), size=int(n), replace=False))


def permutation_garde_logits(graines: Graines, couche: int, largeur: int) -> np.ndarray:
    """Permutation des coordonnées, artefact de la garde de lecture pour la lentille des logits (plan, point 5)."""
    return graines.rng(cle_essai(f"garde-lecture-logits-c{int(couche)}")).permutation(int(largeur))
