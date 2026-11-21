"""Statistiques par direction, lentille et nul — version 2 : statistique des directions nulles calculée **sans elles-mêmes**.

Écart au texte scellé décidé par le directeur (option 2 de la contre-lecture du code, § 5 ; GO-2026-11-19-47 selon le message
de la mère, R-3771), porté par l'addendum `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`, **en
rédaction quand ce module est écrit** : ce code est préparé d'après l'option 2 du rapport et sera accordé à l'addendum scellé
avant tout usage.

Seul `resumer_nul` change depuis `statistiques_v1` :
- concentration d'une direction nulle u_j : C(u_j) = max_t (a_t(u_j) − m_t^(−j)) / s_t^(−j), où m_t^(−j) et s_t^(−j) sont la
  moyenne et l'écart type (de population) des scores du jeton t sur les **M − 1 autres** directions nulles (formule exacte) ;
- part d'une direction nulle : part de ses vingt premiers jetons dont le score dépasse le quantile 0,99 (interpolation
  linéaire) des scores du même jeton sur les **M − 1 autres** directions nulles (statistiques d'ordre du jeton) ;
- inchangés : les comptes de familles ; la moyenne, l'écart type et le quantile des M directions, qui servent à la direction
  lue et aux témoins (z, concentration, part, rangs) ; toutes les autres fonctions, reprises de `statistiques_v1`.
"""
from __future__ import annotations

import math

import torch

from . import constantes_v1 as K
from .constantes_v1 import Arret
from . import statistiques_v1 as _origine
from .statistiques_v1 import ResumeNul, _quantile_par_jeton

# Tout le reste est celui de `statistiques_v1`, repris tel quel.
LIBELLE_CONCENTREE, LIBELLE_INTERMEDIAIRE, LIBELLE_NON_DISTINCTE = (_origine.LIBELLE_CONCENTREE, _origine.LIBELLE_INTERMEDIAIRE,
                                                                    _origine.LIBELLE_NON_DISTINCTE)
famille_de, masques_familles, libelle, sur_representee = _origine.famille_de, _origine.masques_familles, _origine.libelle, _origine.sur_representee
p_empirique, z_scores, concentrations_temoins, p_temoins = _origine.p_empirique, _origine.z_scores, _origine.concentrations_temoins, _origine.p_temoins
lecture_signe, jeton_de_debut, cosinus_colonnes, poles_alignes = _origine.lecture_signe, _origine.jeton_de_debut, _origine.cosinus_colonnes, _origine.poles_alignes
poles_opposes, cosinus, jetons_communs, vecteur_calculable = _origine.poles_opposes, _origine.cosinus, _origine.jetons_communs, _origine.vecteur_calculable


def concentrations_sans_soi(scores_nuls: torch.Tensor, bloc: int = 4096) -> torch.Tensor:
    """C(u_j) de chaque direction nulle, avec la moyenne et l'écart type des M − 1 autres : pour un jeton de moyenne m et
    d'écart type s sur les M directions, m^(−j) = (M·m − a_j) / (M − 1) et (s^(−j))² = (M·s² − (a_j − m)²·M / (M − 1)) / (M − 1).
    Calcul en double précision (moyenne et écart type recalculés ici) ; une variance des autres nulle, à 10⁻¹⁰ près en valeur
    relative de la variance du jeton : arrêt (z non fini)."""
    n_jetons, m = scores_nuls.shape
    if m < 3:
        raise Arret("statistique sans soi-même : au moins trois directions nulles exigées")
    sortie = torch.full((m,), -math.inf, dtype=torch.float64)
    for s in range(0, n_jetons, bloc):
        a = scores_nuls[s:s + bloc].double()
        mu = a.mean(1, keepdim=True)
        var = (a - mu).pow(2).mean(1, keepdim=True)
        mu_sans = (m * mu - a) / (m - 1)
        var_sans = (m * var - (a - mu) ** 2 * m / (m - 1)) / (m - 1)
        if not bool((var_sans > 1e-10 * var).all()):
            raise Arret("écart type nul d'un jeton sur les autres directions nulles : z non fini : arrêt")
        sortie = torch.maximum(sortie, ((a - mu_sans) / var_sans.sqrt()).max(0).values)
    if not bool(torch.isfinite(sortie).all()):
        raise Arret("valeur non finie dans un nul : arrêt")
    return sortie.to(torch.float32)


def quantiles_sans_soi(scores_nuls: torch.Tensor, rangs: torch.Tensor, valeurs: torch.Tensor, q: float = K.QUANTILE_PART) -> torch.Tensor:
    """Pour chaque direction nulle j (colonne) et chacun de ses premiers jetons t (`rangs` `[k, M]`, de scores `valeurs`), le
    quantile `q`, par interpolation linéaire, des scores du jeton t sur les M − 1 autres directions. Tiré des statistiques
    d'ordre du jeton : retirer a de la suite triée x donne y_i = x_{i+1} si a ≤ x_i, sinon x_i."""
    m = scores_nuls.shape[1]
    position = q * (m - 2)                              # rang fractionnaire parmi n = M − 1 valeurs : q·(n − 1)
    bas = int(math.floor(position))
    fraction = position - bas
    haut = min(bas + 1, m - 2)
    n_hauts = m - bas                                   # x_bas … x_{M−1} : les `n_hauts` plus grandes valeurs du jeton
    jetons = torch.unique(rangs)
    plus_grands = scores_nuls[jetons].topk(n_hauts, dim=1).values.flip(1)      # [jetons, n_hauts], croissant : x_bas, x_bas+1, …
    place = torch.searchsorted(jetons, rangs.reshape(-1)).reshape(rangs.shape)
    x = plus_grands[place]                                                     # [k, M, n_hauts]

    def sans(i: int) -> torch.Tensor:                   # y_i, pour i = bas ou haut (indice local i − bas)
        l = i - bas
        suivant = x[..., l + 1] if l + 1 < n_hauts else x[..., l]
        return torch.where(valeurs <= x[..., l], suivant, x[..., l])
    y_bas, y_haut = sans(bas), sans(haut)
    return y_bas + fraction * (y_haut - y_bas)


def resumer_nul(scores_nuls: torch.Tensor, masques: dict[str, torch.Tensor], k: int = K.K_JETONS) -> ResumeNul:
    """Résumé des scores `[jetons, M]` des M directions nulles. Moyenne, écart type et quantile : sur les M directions (pour la
    direction lue et les témoins). Concentration et part de chaque direction nulle : sans elle-même."""
    if not bool(torch.isfinite(scores_nuls).all()):
        raise Arret("valeur non finie dans un nul : arrêt")
    moyenne = scores_nuls.mean(1)
    ecart = scores_nuls.std(1, correction=0)
    if not bool((ecart > 0).all()):
        raise Arret("écart type nul d'un jeton sous un nul : z non fini : arrêt")
    quantile = _quantile_par_jeton(scores_nuls, K.QUANTILE_PART)
    concentration = concentrations_sans_soi(scores_nuls)
    k = min(int(k), scores_nuls.shape[0])
    haut = scores_nuls.topk(k, dim=0)
    part = (haut.values > quantiles_sans_soi(scores_nuls, haut.indices, haut.values)).float().mean(0)
    familles = {nom: m[haut.indices].sum(0).to(torch.int64) for nom, m in masques.items()}
    return ResumeNul(moyenne, ecart, quantile, concentration, part, familles, k)
