"""Pièce 2 — noyau de permutation stratifié (§ 2 de la spécification ; garde G1 du § 4).

Nul en loi : la loi jointe des conduites mesurées ne dépend pas du vecteur de conditions tiré. Loi sous le nul : celle de
la statistique sur les permutations intra-tâche du plan engagé, et sur elles seules (§ 2, « dépendance intra-tâche » :
il est interdit de permuter autrement que le plan n'a tiré).

- Énumération exacte si ((3k)!/(k!)³)^(nombre de tâches) ≤ 10⁶ ; p = #(T_b ≥ T_obs) / M, l'observé compris.
- Sinon B tirages par `SeedSequence(entropie_racine, spawn_key=(2,))`, après la révélation ;
  p = (1 + #(T_b ≥ T_obs)) / (B + 1) (Phipson et Smyth). B = 9 999 ; d'autres valeurs (999 dans la pièce 6) ne sont
  permises que dans les simulations (`simulation=True`).

Statistique primaire : T = Σ_t (moyenne de Y sous U − moyenne de Y sous E), unilatérale.
Statistique secondaire : omnibus, maximum des trois contrastes absolus (U−E, U−D, D−E), chacun sommé sur les tâches.

Les comparaisons T_b ≥ T_obs se font avec une tolérance relative de 10⁻⁹ (arrondis de sommation) : choix d'écriture,
point laissé ouvert.
"""
from __future__ import annotations

import itertools
import math
from dataclasses import dataclass

import numpy as np

from .erreurs_v2 import RefusPlan
from .registre_v2 import BLOC, CLE_PERMUTATIONS, D, E, U, UNITE, Plan, _entropie_ss, base_conditions, verifier_entropie

SEUIL_ENUMERATION = 10**6
B_DEFAUT = 9999
B_MINIMUM_SIMULATION = 99
TOLERANCE_RELATIVE = 1e-9


def nb_affectations_par_tache(k: int) -> int:
    return math.factorial(3 * k) // math.factorial(k) ** 3


def affectations_tache(k: int) -> np.ndarray:
    """Les affectations distinctes d'une tâche, en ordre lexicographique : (90, 6) à k = 2."""
    base = tuple(int(x) for x in base_conditions(k))
    uniques = sorted(set(itertools.permutations(base)))
    return np.array(uniques, dtype=np.int8)


@dataclass
class Tirages:
    """Affectations sur lesquelles la loi sous le nul est lue : (M, n_taches, 3k)."""

    observe: np.ndarray  # (n_taches, 3k)
    affectations: np.ndarray  # (M, n_taches, 3k)
    mode: str  # « exact » ou « tirage »
    k: int

    @property
    def m(self) -> int:
        return int(self.affectations.shape[0])


def verifier_conditions(conditions, k: int) -> np.ndarray:
    c = np.asarray(conditions)
    if c.ndim != 2 or c.shape[1] != 3 * k:
        raise RefusPlan(f"conditions de forme {c.shape} : (n_taches, 3k = {3 * k}) attendu")
    if not np.all(np.isin(c, (E, D, U))):
        raise RefusPlan("conditions hors des codes 0 = E, 1 = D, 2 = U")
    for t in range(c.shape[0]):
        comptes = np.bincount(c[t].astype(np.int64), minlength=3)
        if comptes.shape[0] != 3 or not np.all(comptes == k):
            raise RefusPlan(
                f"G1 : tâche {t}, bloc {comptes.tolist()} au lieu de {k} par condition — le plan tiré n'est pas "
                "épisode dans tâche (unité différente du registre) : permutation refusée"
            )
    return c.astype(np.int8)


def tirages_du_plan(plan: Plan, entropie_racine, B: int = B_DEFAUT, simulation: bool = False,
                    unite: str = UNITE, bloc: str = BLOC) -> Tirages:
    """Construit les affectations du test pour le plan engagé. `unite` et `bloc` sont ceux que l'analyse déclare :
    ils doivent être ceux du registre (G1, artefact « unité fausse »)."""
    if unite != plan.unite or bloc != plan.bloc:
        raise RefusPlan(f"G1 : permutation par {unite!r} dans {bloc!r} demandée, registre en {plan.unite!r} dans {plan.bloc!r}")
    if plan.unite != UNITE or plan.bloc != BLOC:
        raise RefusPlan(f"G1 : seul le plan {UNITE!r} dans {BLOC!r} est permutable par ce noyau")
    return tirages(plan.conditions, plan.k, entropie_racine, B=B, simulation=simulation)


def tirages(conditions, k: int, entropie_racine, B: int = B_DEFAUT, simulation: bool = False) -> Tirages:
    c = verifier_conditions(conditions, k)
    verifier_entropie(entropie_racine, "entropie racine")
    if not isinstance(B, (int, np.integer)) or isinstance(B, bool):
        raise RefusPlan(f"nombre de tirages mal formé : {B!r}")
    if not simulation and B != B_DEFAUT:
        raise RefusPlan(f"B = {B} : hors simulation, B = {B_DEFAUT} (§ 2)")
    if simulation and B < B_MINIMUM_SIMULATION:
        raise RefusPlan(f"B = {B} < {B_MINIMUM_SIMULATION} même en simulation")
    n_t, n = c.shape
    nb = nb_affectations_par_tache(k)
    if nb**n_t <= SEUIL_ENUMERATION:
        aff = affectations_tache(k)
        idx = np.indices((nb,) * n_t).reshape(n_t, -1).T  # (M, n_t)
        tout = aff[idx]  # (M, n_t, 3k)
        return Tirages(c, tout, "exact", k)
    rng = np.random.default_rng(np.random.SeedSequence(_entropie_ss(entropie_racine), spawn_key=(CLE_PERMUTATIONS,)))
    tout = rng.permuted(np.broadcast_to(c, (int(B), n_t, n)).copy(), axis=2)
    return Tirages(c, tout, "tirage", k)


def verifier_issues(Y, tir: Tirages, nom: str = "Y") -> np.ndarray:
    y = np.asarray(Y, dtype=np.float64)
    if y.shape != tir.observe.shape:
        raise RefusPlan(f"{nom} de forme {y.shape}, plan de forme {tir.observe.shape}")
    if not np.all(np.isfinite(y)):
        raise RefusPlan(f"{nom} contient une valeur manquante ou infinie : passer d'abord par la garde G6")
    return y


def _moyennes(Y: np.ndarray, L: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Moyennes par tâche sous E, D, U : chacune (M, n_taches)."""
    return tuple(np.einsum("tj,mtj->mt", Y, (L == c).astype(np.float64)) / k for c in (E, D, U))


def stat_dirigee(Y: np.ndarray, L: np.ndarray, k: int) -> np.ndarray:
    """T = Σ_t (moyenne sous U − moyenne sous E) ; L de forme (M, n_t, 3k) ; rend (M,)."""
    mE, _, mU = _moyennes(Y, L, k)
    return (mU - mE).sum(axis=1)


def stat_omnibus(Y: np.ndarray, L: np.ndarray, k: int) -> np.ndarray:
    mE, mD, mU = _moyennes(Y, L, k)
    return np.maximum.reduce([np.abs((mU - mE).sum(1)), np.abs((mU - mD).sum(1)), np.abs((mD - mE).sum(1))])


def p_valeur(t_obs: float, t_tirages: np.ndarray, mode: str) -> float:
    tol = TOLERANCE_RELATIVE * max(1.0, abs(float(t_obs)))
    nb = int(np.count_nonzero(t_tirages >= t_obs - tol))
    if mode == "exact":
        if nb < 1:
            raise RefusPlan("énumération exacte qui ne contient pas l'observé")
        return nb / t_tirages.shape[0]
    if mode == "tirage":
        return (1 + nb) / (t_tirages.shape[0] + 1)
    raise RefusPlan(f"mode inconnu : {mode!r}")


@dataclass
class ResultatTest:
    p: float
    t_observe: float
    mode: str
    m: int


def tester(Y, tir: Tirages, statistique=stat_dirigee) -> ResultatTest:
    y = verifier_issues(Y, tir)
    t_obs = float(statistique(y, tir.observe[None], tir.k)[0])
    t_b = statistique(y, tir.affectations, tir.k)
    return ResultatTest(p_valeur(t_obs, t_b, tir.mode), t_obs, tir.mode, tir.m)
