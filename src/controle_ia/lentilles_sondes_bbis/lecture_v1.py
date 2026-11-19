"""Lecture d'un vecteur par une lentille côté sortie (texte scellé, « Métrique », points 2 et 3 ; plan, points 5 et 6).

Lecture d'un vecteur v à la couche ℓ : t = RMSNorm(J_ℓ v) · γ, ε = 10⁻⁶ ; score du jeton gardé : a(v) = W_U t, W_U = lignes
gardées de `lm_head.weight`. Lentille publique : J_ℓ du fichier, converti en simple précision ; lentille des logits :
J_ℓ = identité (`None`). Tout en simple précision. RMSNorm est impaire : a(−v) = −a(v), un seul calcul rend les deux signes.
Ce module n'appelle pas la fonction du voisin, sauf dans la garde de la fonction de lecture, qui compare les deux.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

import numpy as np
import torch

from . import constantes_v1 as K
from .constantes_v1 import Arret


def _colonnes(v) -> torch.Tensor:
    t = torch.as_tensor(np.asarray(v, dtype=np.float32) if not isinstance(v, torch.Tensor) else v, dtype=torch.float32)
    return t[:, None] if t.ndim == 1 else t


def transporter(v, jacobienne: torch.Tensor | None) -> torch.Tensor:
    """J_ℓ v en simple précision ; `None` : lentille des logits (identité). `v` : `[largeur]` ou `[largeur, n]`."""
    v = _colonnes(v)
    if jacobienne is None:
        return v
    if jacobienne.dtype != torch.float32 or jacobienne.shape != (v.shape[0], v.shape[0]):
        raise Arret(f"matrice de lentille de forme {tuple(jacobienne.shape)} ({jacobienne.dtype}) ; carrée de largeur "
                    f"{v.shape[0]} en simple précision attendue")
    return jacobienne @ v


def rapport_epsilon(transporte: torch.Tensor) -> np.ndarray:
    """ρ(x) = moyenne des carrés des coordonnées de J_ℓ x, divisée par ε ; un par colonne."""
    return (transporte.double().pow(2).mean(0) / K.EPSILON).numpy()


def lire(v, jacobienne: torch.Tensor | None, gamma: torch.Tensor, wu: torch.Tensor, bloc: int = 256):
    """Scores de **tous** les jetons gardés pour chaque colonne de `v`. Rend (`[jetons, n]` en simple précision, ρ `[n]`).
    Une valeur non finie : arrêt."""
    t = transporter(v, jacobienne)
    rho = rapport_epsilon(t)
    t = t * torch.rsqrt(t.pow(2).mean(0, keepdim=True) + K.EPSILON) * gamma.to(torch.float32)[:, None]
    if wu.dtype != torch.float32:
        raise Arret("W_U attendu en simple précision")
    scores = torch.empty((wu.shape[0], t.shape[1]), dtype=torch.float32)
    for s in range(0, t.shape[1], bloc):
        scores[:, s:s + bloc] = wu @ t[:, s:s + bloc]
    if not bool(torch.isfinite(scores).all()) or not np.all(np.isfinite(rho)):
        raise Arret("valeur non finie dans une lecture : arrêt")
    return scores, rho


def premiers(scores: torch.Tensor, k: int) -> tuple[torch.Tensor, torch.Tensor]:
    """Les `k` premiers jetons par score de chaque colonne : (valeurs `[n, k]`, indices `[n, k]` parmi les jetons gardés)."""
    haut = scores.topk(min(int(k), scores.shape[0]), dim=0)
    return haut.values.T, haut.indices.T


# --- matrices de la lentille publique et contrôle de l'indice de couche ---------------------------------------------------------------
def empreinte_matrice(matrice) -> str:
    """SHA-256 des octets de la matrice en demi-précision, telle que le fichier la porte (ordre des lignes)."""
    a = matrice.numpy() if isinstance(matrice, torch.Tensor) else np.asarray(matrice)
    if a.dtype != np.float16:
        raise Arret(f"empreinte d'une matrice de lentille : demi-précision attendue, {a.dtype} reçue")
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()


@dataclass
class LentillePublique:
    """Matrices gardées de la lentille publique, en demi-précision par indice de couche, et leurs empreintes relevées au
    montage par indice. `decalage` n'existe que pour l'essai de la garde de l'indice (artefact : un cran)."""
    matrices: dict[int, np.ndarray]
    empreintes_montage: dict[int, str]
    decalage: int = 0
    _simple: dict[int, torch.Tensor] = field(default_factory=dict, repr=False)

    def matrice(self, couche: int) -> tuple[torch.Tensor, int, str]:
        """Matrice lue pour une sonde de couche `couche` : celle de l'indice égal à la couche ; son empreinte est comparée
        à celle relevée au montage pour cet indice ; écart : arrêt."""
        couche = int(couche)
        couches = sorted(self.matrices)
        indice = couche if not self.decalage else couches[(couches.index(couche) + self.decalage) % len(couches)]
        if indice not in self.matrices:
            raise Arret(f"lentille publique : aucune matrice gardée d'indice {indice}")
        lue = empreinte_matrice(self.matrices[indice])
        exiger_indice(couche, lue, self.empreintes_montage)
        if indice not in self._simple:
            self._simple[indice] = torch.from_numpy(self.matrices[indice].astype(np.float32))
        return self._simple[indice], couche, lue


def exiger_indice(couche_sonde: int, empreinte_lue: str, empreintes_montage: dict[int, str]) -> None:
    """Plan, point 6 : l'empreinte de la matrice lue égale celle relevée au montage pour l'indice égal à la couche de la
    sonde ; sinon arrêt (« matrice lue d'un autre indice que la couche de la sonde »)."""
    if int(couche_sonde) not in empreintes_montage:
        raise Arret(f"aucune empreinte relevée au montage pour l'indice {couche_sonde}")
    if empreinte_lue != empreintes_montage[int(couche_sonde)]:
        raise Arret(f"matrice lue d'un autre indice que la couche {couche_sonde} de la sonde : arrêt")


def jacobienne_de(lentille: str, couche: int, publique: LentillePublique | None) -> tuple[torch.Tensor | None, int, str]:
    """(matrice ou `None`, indice lu, empreinte) pour une lentille nommée. Lentille des logits : identité à toute couche."""
    if lentille == K.LENTILLE_LOGITS:
        return None, int(couche), "identite"
    if lentille != K.LENTILLE_PUBLIQUE:
        raise Arret(f"lentille {lentille!r} inconnue")
    if publique is None:
        raise Arret("lentille publique absente : arrêt ; la lecture par la seule lentille des logits n'est pas rendue")
    return publique.matrice(couche)


# --- garde du rapport à ε ----------------------------------------------------------------------------------------------------------
def independance_tenue(rho_min: float) -> bool:
    """ρ ≥ 100 : la lecture ne dépend de la norme qu'à un facteur commun compris entre 1 et 1 − 1/(2ρ)."""
    return bool(rho_min >= K.SEUIL_RAPPORT_EPSILON)


# --- garde de la fonction de lecture (plan, point 5) --------------------------------------------------------------------------------
def matrice_permutation(permutation: np.ndarray) -> torch.Tensor:
    """Matrice P telle que (P v)_i = v_{permutation[i]}."""
    d = len(permutation)
    p = torch.zeros((d, d), dtype=torch.float32)
    p[torch.arange(d), torch.as_tensor(np.asarray(permutation), dtype=torch.long)] = 1.0
    return p


def garde_fonction_lecture(lire_voisin, colonnes, gamma: torch.Tensor, wu: torch.Tensor, jacobienne: torch.Tensor | None,
                           jacobienne_artefact: torch.Tensor, lentille: str, couche: int) -> dict:
    """Cas sain : pour chaque colonne, les dix premiers jetons de notre code égalent, au rang près, ceux de `read` du voisin
    appelé avec W_U en simple précision ; un écart limité à des jetons dont les scores diffèrent de moins de 10⁻⁴ en valeur
    relative est compté et rapporté, sans arrêt ; tout autre écart : arrêt. Artefact : avec `jacobienne_artefact` à la place
    de la matrice, les dix premiers jetons diffèrent de ceux du cas sain pour au moins 32 des 64 colonnes ; sinon arrêt.
    Rapporté sans critère : colonnes dont le premier jeton diffère quand le voisin fait le produit en demi-précision."""
    colonnes = _colonnes(colonnes)
    n = colonnes.shape[1]
    scores, _ = lire(colonnes, jacobienne, gamma, wu)
    _, ids = premiers(scores, K.K_GARDE)
    _, ids_voisin = lire_voisin(colonnes, wu, gamma, jacobienne, k=K.K_GARDE)
    quasi = 0
    for j in range(n):
        a, b = set(ids[j].tolist()), set(ids_voisin[j].tolist())
        if a == b:
            continue
        seuil = float(scores[:, j].topk(K.K_GARDE).values[-1])
        if all(abs(float(scores[i, j]) - seuil) <= K.TOLERANCE_EGALITE_GARDE * abs(seuil) for i in a ^ b):
            quasi += 1
            continue
        raise Arret(f"garde de la fonction de lecture ({lentille}, couche {couche}) : écart sur le cas sain à la colonne {j} : "
                    "arrêt avant tout calcul")
    scores_art, _ = lire(colonnes, jacobienne_artefact, gamma, wu)
    _, ids_art = premiers(scores_art, K.K_GARDE)
    differentes = sum(set(ids[j].tolist()) != set(ids_art[j].tolist()) for j in range(n))
    if differentes < K.MIN_COLONNES_ARTEFACT:
        raise Arret(f"garde de la fonction de lecture ({lentille}, couche {couche}) : artefact vu sur {differentes} colonnes "
                    f"sur {n} seulement (au moins {K.MIN_COLONNES_ARTEFACT} exigées) : arrêt avant tout calcul")
    try:
        _, ids_demi = lire_voisin(colonnes, wu.to(torch.float16), gamma, jacobienne, k=K.K_GARDE)
        demi = {"premier_jeton_different": int((ids_demi[:, 0] != ids[:, 0]).sum())}
    except RuntimeError as e:   # produit en demi-précision indisponible sur ce processeur : rapporté, sans critère
        demi = {"premier_jeton_different": None, "motif": f"produit en demi-précision impossible ici : {type(e).__name__}"}
    return {"lentille": lentille, "couche": int(couche), "colonnes": n, "ecarts_de_quasi_egalite": quasi,
            "colonnes_differentes_sur_artefact": int(differentes), "voisin_en_demi_precision": demi, "tenue": True}
