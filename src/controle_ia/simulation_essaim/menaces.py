"""Menaces de la simulation d'essaim, sur des lots (R, K, T).

Classe C (multi-ensemble préservé, note v3, section 4), par sous-groupe de permutations de I :
- G_A, « diffuse entre agents à un pas » : le multi-ensemble des K scores de chaque pas est conservé ;
  - `rebrassage_agents` : permutation uniforme des agents, indépendante à chaque pas (T2) ;
  - `routage` : à m pas, le plus haut score du pas passe à un agent destinataire (un agent voyou si
    k_dest = 1 ; relais tournant entre agents si k_dest = K) ;
- G_T, « diffuse dans le temps pour un agent » : le multi-ensemble des T scores de chaque agent est conservé ;
  - `rebrassage_temps` : permutation uniforme du temps, indépendante pour chaque agent (T2) ;
  - `synchro` : m agents placent leurs r plus hauts scores aux mêmes r pas (menace concentrée dans le
    temps, étalée entre agents d'un même pas) ;
- toutes les cases : `rebrassage_tout` (T2).

Classe M (décalage, budget B, Σδ = B) : `decalages` — concentré (un agent, un pas), synchronisé (un pas,
m agents, B/m chacun), étalé dans le temps (un agent, m pas, B/m chacun).

`exiger_groupe` est la garde de la liste d'arrêt : un arrangement de classe C doit préserver exactement
le multi-ensemble de son groupe, sinon le run s'arrête.
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from ..simulation_t03.attaques import melanger
from .statistiques import GROUPES, verifier_lot

GENRES_M = ("concentre", "synchro", "temps", "synchro_un")


def sous_ensemble(rng: np.random.Generator, R: int, n: int, m: int) -> np.ndarray:
    """(R, m) : m indices distincts parmi n, triés, tirés uniformément pour chaque épisode."""
    if not (1 <= m <= n):
        raise GardeArret(f"m = {m} hors de [1, {n}]")
    return np.sort(np.argsort(rng.random((R, n)), axis=1)[:, :m], axis=1)


# --- classe C, G_A : agents permutés à l'intérieur de chaque pas ---
def rebrassage_agents(Xb, rng: np.random.Generator) -> np.ndarray:
    Xb = verifier_lot(Xb)
    return np.take_along_axis(Xb, np.argsort(rng.random(Xb.shape), axis=1), axis=1)


def routage(Xb, m: int, k_dest: int, rng: np.random.Generator) -> np.ndarray:
    """À m pas tirés uniformément, le plus haut score du pas est échangé avec celui de l'agent destinataire
    d_j = (a + (j mod k_dest)) mod K, j = rang du pas routé, a = agent tiré uniformément. Transpositions
    à l'intérieur d'un pas : élément de G_A."""
    Xb = verifier_lot(Xb)
    R, K, T = Xb.shape
    if not (1 <= k_dest <= K):
        raise GardeArret(f"k_dest = {k_dest} hors de [1, K = {K}]")
    pas = sous_ensemble(rng, R, T, m)                                   # (R, m)
    a = rng.integers(0, K, size=R)
    dest = (a[:, None] + (np.arange(m)[None, :] % k_dest)) % K           # (R, m)
    X = Xb.copy()
    rr = np.arange(R)[:, None]
    colonnes = X[rr, :, pas]                                             # (R, m, K)
    porteur = np.argmax(colonnes, axis=2)                                # (R, m)
    v_haut = X[rr, porteur, pas]
    v_dest = X[rr, dest, pas]
    X[rr, porteur, pas] = v_dest
    X[rr, dest, pas] = v_haut
    return X


# --- classe C, G_T : temps permuté à l'intérieur de chaque agent ---
def rebrassage_temps(Xb, rng: np.random.Generator) -> np.ndarray:
    Xb = verifier_lot(Xb)
    return np.take_along_axis(Xb, np.argsort(rng.random(Xb.shape), axis=2), axis=2)


def synchro(Xb, m: int, r: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """m agents tirés uniformément placent leurs r plus hauts scores (ordre aléatoire) aux r mêmes pas,
    tirés uniformément ; leurs autres scores gardent leur ordre relatif dans les cases restantes.
    Permutation du temps de chaque agent : élément de G_T. Renvoie (X, agents (R, m), pas (R, r))."""
    Xb = verifier_lot(Xb)
    R, K, T = Xb.shape
    if not (1 <= r < T):
        raise GardeArret(f"r = {r} hors de [1, T = {T}[")
    agents = sous_ensemble(rng, R, K, m)                                # (R, m)
    pas = sous_ensemble(rng, R, T, r)                                   # (R, r)
    rr = np.arange(R)[:, None]
    lignes = Xb[rr, agents, :]                                           # (R, m, T)
    o = np.argsort(lignes, axis=2, kind="stable")
    haut = np.zeros(lignes.shape, dtype=bool)
    np.put_along_axis(haut, o[:, :, -r:], True, axis=2)
    v_haut = melanger(np.take_along_axis(lignes, o[:, :, -r:], axis=2).reshape(R * m, r), rng)
    v_reste = lignes[~haut]                                              # ordre du temps conservé
    cible = np.zeros((R, T), dtype=bool)
    np.put_along_axis(cible, pas, True, axis=1)
    cible = np.broadcast_to(cible[:, None, :], lignes.shape)
    nouvelles = np.empty_like(lignes)
    nouvelles[cible] = v_haut.ravel()
    nouvelles[~cible] = v_reste
    X = Xb.copy()
    X[rr, agents, :] = nouvelles
    return X, agents, pas


# --- classe C, toutes les cases ---
def rebrassage_tout(Xb, rng: np.random.Generator) -> np.ndarray:
    Xb = verifier_lot(Xb)
    R, K, T = Xb.shape
    return melanger(Xb.reshape(R, K * T), rng).reshape(R, K, T)


def exiger_groupe(X, Y, groupe: str, quoi: str) -> None:
    """Garde : X est un réarrangement de Y dans le groupe annoncé (multi-ensembles exactement conservés)."""
    X, Y = np.asarray(X), np.asarray(Y)
    if X.shape != Y.shape:
        raise GardeArret(f"{quoi} : forme {X.shape} ≠ {Y.shape} (liste d'arrêt)")
    if groupe == "agents":
        ok = np.array_equal(np.sort(X, axis=1), np.sort(Y, axis=1))
    elif groupe == "temps":
        ok = np.array_equal(np.sort(X, axis=2), np.sort(Y, axis=2))
    elif groupe == "tout":
        R = X.shape[0]
        ok = np.array_equal(np.sort(X.reshape(R, -1), axis=1), np.sort(Y.reshape(R, -1), axis=1))
    else:
        raise GardeArret(f"groupe {groupe!r} inconnu ({GROUPES})")
    if not ok:
        raise GardeArret(f"{quoi} : multi-ensemble du groupe « {groupe} » non préservé (liste d'arrêt)")


def arranger(spec: dict, Y, rng: np.random.Generator) -> tuple[np.ndarray, dict]:
    """Applique l'arrangement de classe C décrit par la grille ; renvoie (X, informations)."""
    nom, genre = spec["nom"], spec["genre"]
    if genre == "rebrassage_agents":
        return rebrassage_agents(Y, rng), {}
    if genre == "routage":
        return routage(Y, int(spec["m"]), int(spec["k_dest"]), rng), {}
    if genre == "rebrassage_temps":
        return rebrassage_temps(Y, rng), {}
    if genre == "synchro":
        X, agents, pas = synchro(Y, int(spec["m"]), int(spec["r"]), rng)
        return X, {"agents": agents, "pas": pas}
    if genre == "rebrassage_tout":
        return rebrassage_tout(Y, rng), {}
    raise GardeArret(f"arrangement {nom!r} de genre {genre!r} inconnu")


# --- classe M : décalages à budget fixé ---
def decalages(genre: str, K: int, T: int, B: float, m: int, R: int, rng: np.random.Generator,
              pas_impose=None, agents_imposes=None) -> np.ndarray:
    """Δ (R, K, T), ΣΔ = B par épisode, δ = B/m sur m cases.
    - concentre : une case uniforme (m = 1) ;
    - synchro : un pas uniforme, m agents uniformes ;
    - temps : un agent uniforme, m pas uniformes ;
    - synchro_un : compagnon de L4, tout le budget sur le premier des agents imposés, au pas imposé."""
    if not (B > 0):
        raise GardeArret(f"budget B = {B} : réel > 0 attendu")
    D = np.zeros((R, K, T))
    rr = np.arange(R)[:, None]
    if genre == "concentre":
        if m != 1:
            raise GardeArret("menace concentrée : m = 1")
        D[np.arange(R), rng.integers(0, K, size=R), rng.integers(0, T, size=R)] = B
    elif genre == "synchro":
        s = rng.integers(0, T, size=R) if pas_impose is None else np.asarray(pas_impose)
        ag = sous_ensemble(rng, R, K, m) if agents_imposes is None else np.asarray(agents_imposes)
        D[rr, ag, s[:, None]] = B / m
    elif genre == "temps":
        a = rng.integers(0, K, size=R)
        ps = sous_ensemble(rng, R, T, m)
        D[rr, a[:, None], ps] = B / m
    elif genre == "synchro_un":
        if pas_impose is None or agents_imposes is None:
            raise GardeArret("compagnon de L4 : pas et agents imposés requis")
        D[np.arange(R), np.asarray(agents_imposes)[:, 0], np.asarray(pas_impose)] = B
    else:
        raise GardeArret(f"décalage {genre!r} inconnu ({GENRES_M})")
    if not np.allclose(D.sum(axis=(1, 2)), B, rtol=0, atol=1e-9 * max(1.0, B)):
        raise GardeArret("décalages : budget non conservé (liste d'arrêt)")
    return D
