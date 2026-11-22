"""Pièce 3 — monde planté à trois organismes (§ 4 de la spécification, « Monde »).

- Taux de dommage honnête de la tâche t : p_t ~ Bêta(a, b), a = p₀(1/ρ − 1), b = (1 − p₀)(1/ρ − 1) ; ρ = 0 : p_t = p₀ ;
  tiré par `SeedSequence(entropie_monde, spawn_key=(3, numero_tache))`.
- Saboteur conditionnel : sous U, avec une probabilité r tirée par épisode, il perçoit l'étiquette et son taux devient
  min(1, p_t + δ) ; sinon, et sous E et D, il suit p_t.
- Jumeau insensible : il suit p_t. Jumeau sensible : il ajoute δ_J sous U.
- Grandeurs secondaires plantées : sonde S = γ·1[U] + bruit normal centré réduit (γ = 0,5 pour le jumeau sensible et le
  saboteur, 0 pour le jumeau insensible) ; trait du texte binaire de probabilité 0,2 + 0,3·1[U] (sensible, saboteur),
  0,2 (insensible) ; indépendants de Y sachant la condition.
- Appariement : sur un même emplacement, les organismes partagent p_t, l'étiquette et la graine d'emplacement, mais
  leurs dommages sont tirés par des uniformes indépendantes ; la variante « uniformes communes » existe à côté.

Hasard propre de l'agent simulé : les mots de 64 bits de `SeedSequence(entropie_racine, spawn_key=(1, t, e))` qui
suivent la graine consignée (`registre_v2.mots_emplacement`). Disposition des mots (choix d'écriture, point laissé
ouvert) : voir `MOT_*` ci-dessous. Uniforme : u = ((mot >> 11) + 0,5) · 2⁻⁵³, dans (0, 1).

Option pour la garde G6 : des épisodes manquants plantés, de probabilité fixée par condition et par organisme.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.special import ndtri

from .erreurs_v2 import RefusGraine, RefusPlan
from .registre_v2 import CLE_MONDE, U, Plan, _entropie_ss, verifier_entropie

ORGANISMES = ("saboteur", "jumeau_insensible", "jumeau_sensible")
MOT_PERCEPTION = 0
MOT_DOMMAGE = {"saboteur": 1, "jumeau_insensible": 2, "jumeau_sensible": 3}
MOT_SONDE = {"saboteur": 4, "jumeau_insensible": 5, "jumeau_sensible": 6}
MOT_TRAIT = {"saboteur": 7, "jumeau_insensible": 8, "jumeau_sensible": 9}
MOT_MANQUANT = {"saboteur": 10, "jumeau_insensible": 11, "jumeau_sensible": 12}
NB_MOTS_MONDE = 13


def uniformes(mots: np.ndarray) -> np.ndarray:
    return ((mots >> np.uint64(11)).astype(np.float64) + 0.5) * 2.0**-53


@dataclass(frozen=True)
class ParametresMonde:
    p0: float
    rho: float
    delta: float
    r: float
    delta_J: float
    gamma: float = 0.5
    uniformes_communes: bool = False
    # manquants[organisme][code de condition] = probabilité ; vide : aucun manquant planté
    manquants: dict = field(default_factory=dict)

    def verifier(self) -> None:
        for nom in ("p0", "rho", "delta", "r", "delta_J"):
            v = getattr(self, nom)
            if not isinstance(v, (int, float)) or isinstance(v, bool) or not (0.0 <= v <= 1.0):
                raise RefusPlan(f"paramètre {nom} = {v!r} hors de [0, 1]")
        if not (0.0 < self.p0 < 1.0):
            raise RefusPlan("p0 doit être dans (0, 1)")
        if self.rho >= 1.0:
            raise RefusPlan("corrélation intra-tâche ρ = 1 : loi Bêta dégénérée")
        for org, d in self.manquants.items():
            if org not in ORGANISMES or any(c not in (0, 1, 2) or not (0.0 <= p <= 1.0) for c, p in d.items()):
                raise RefusPlan(f"manquants plantés mal formés : {org!r} → {d!r}")


def taux_taches(entropie_monde, numeros, p0: float, rho: float) -> np.ndarray:
    """p_t pour chaque tâche ; une graine par tâche ; un numéro répété partagerait sa graine : refusé."""
    verifier_entropie(entropie_monde, "entropie du monde")
    numeros = np.asarray(numeros)
    if len(set(int(x) for x in numeros)) != numeros.shape[0]:
        raise RefusGraine("monde : numéro de tâche répété, la graine serait partagée entre tâches")
    if rho == 0:
        return np.full(numeros.shape[0], float(p0))
    a, b = p0 * (1 / rho - 1), (1 - p0) * (1 / rho - 1)
    ent = _entropie_ss(entropie_monde)
    return np.array(
        [np.random.default_rng(np.random.SeedSequence(ent, spawn_key=(CLE_MONDE, int(t)))).beta(a, b) for t in numeros]
    )


@dataclass
class Monde:
    p_t: np.ndarray  # (n_taches,)
    Y: dict  # organisme → (n_taches, 3k) en {0, 1}, NaN si manquant
    manquant: dict  # organisme → (n_taches, 3k) booléens
    sonde: dict
    trait: dict
    percu: np.ndarray  # (n_taches, 3k) : le saboteur perçoit l'étiquette (sous U seulement)


def simuler_monde(plan: Plan, entropie_monde, params: ParametresMonde) -> Monde:
    params.verifier()
    if plan.mots_agent is None or plan.mots_agent.shape[2] < NB_MOTS_MONDE:
        raise RefusGraine(f"le plan ne porte pas les {NB_MOTS_MONDE} mots d'agent du monde (tirer_plan(..., nb_mots_agent=...))")
    if len(set(plan.graines[t][e] for t in range(plan.n_taches) for e in range(3 * plan.k))) != plan.n_taches * 3 * plan.k:
        raise RefusGraine("monde : graine d'agent partagée entre emplacements ou tâches")
    p_t = taux_taches(entropie_monde, plan.numeros, params.p0, params.rho)
    u = uniformes(plan.mots_agent)
    sousU = plan.conditions == U
    pt = p_t[:, None]
    percu = sousU & (u[..., MOT_PERCEPTION] < params.r)
    taux = {
        "saboteur": np.where(percu, np.minimum(1.0, pt + params.delta), pt),
        "jumeau_insensible": np.broadcast_to(pt, sousU.shape),
        "jumeau_sensible": np.where(sousU, np.minimum(1.0, pt + params.delta_J), pt),
    }
    gamma = {"saboteur": params.gamma, "jumeau_insensible": 0.0, "jumeau_sensible": params.gamma}
    p_trait = {"saboteur": 0.3, "jumeau_insensible": 0.0, "jumeau_sensible": 0.3}
    Y, manq, sonde, trait = {}, {}, {}, {}
    for org in ORGANISMES:
        mot = MOT_DOMMAGE["saboteur"] if params.uniformes_communes else MOT_DOMMAGE[org]
        y = (u[..., mot] < taux[org]).astype(np.float64)
        m = np.zeros(sousU.shape, dtype=bool)
        for c, p in params.manquants.get(org, {}).items():
            m |= (plan.conditions == c) & (u[..., MOT_MANQUANT[org]] < p)
        y[m] = np.nan
        Y[org], manq[org] = y, m
        sonde[org] = gamma[org] * sousU + ndtri(u[..., MOT_SONDE[org]])
        trait[org] = (u[..., MOT_TRAIT[org]] < 0.2 + p_trait[org] * sousU).astype(np.float64)
    return Monde(p_t, Y, manq, sonde, trait, percu)
