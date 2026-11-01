"""Statistiques vectorisées d'un lot d'essaims de forme (R, K, T) : R répétitions, K agents, T pas.

Plus grand = plus suspect. Scores standardisés en amont (μ₀ = 0, σ = 1).

Invariance exacte, au bit près : toute somme est faite sur des valeurs triées le long de l'axe que
permute le groupe de la statistique, et les comptages sont entiers. Une permutation du groupe laisse
donc la valeur identique au bit près (T1, note mathématique v3, section 4).

Groupes de permutations des cases I = agents × pas :
- « tout » : toutes les permutations de I ;
- « agents » : G_A (agents permutés indépendamment à chaque pas) et relabellisation des pas ;
- « agents_ordonne » : G_A seulement (lecture séquentielle dans l'ordre des pas) ;
- « temps » : G_T (temps permuté indépendamment pour chaque agent) et relabellisation des agents.

Une statistique « agents » ou « agents_ordonne » est invariante sous G_A ; « temps », sous G_T ;
« tout », sous les deux et sous toute permutation de I.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.special import logsumexp

from ..agregateurs.processus_e import log_e_unilateral
from ..gardes import GardeArret
from ..simulation_t03 import lots as L03

FRACTIONS_LAMBDA = (0.1, 0.25, 0.5, 0.75)   # λ / λ_max, λ_max = 1/(K q) : facteurs strictement positifs
M_COELEV = 3                                # co-élévation continue : somme des 3 plus hauts scores du pas

STATISTIQUES = {
    "somme": "tout",
    "max": "tout",
    "comptage": "tout",
    "agent_moyenne": "temps",
    "agent_comptage": "temps",
    "pas_moyenne": "agents",
    "coelev_comptage": "agents",
    "coelev_somme3": "agents",
    "e_coelev": "agents_ordonne",
    "ed_coelev": "agents_ordonne",
    "e_pas": "agents_ordonne",
}
# statistiques à valeurs en nombre fini : seuils aléatoirisés (départage par un uniforme par essaim)
DISCRETES = frozenset({"comptage", "agent_comptage", "coelev_comptage", "e_coelev", "ed_coelev"})
GROUPES = ("agents", "temps", "tout")


def invariante(stat: str, groupe: str) -> bool:
    """La statistique est-elle invariante, au bit près, sous le groupe de l'attaquant ?"""
    if stat not in STATISTIQUES:
        raise GardeArret(f"statistique {stat!r} inconnue")
    g = STATISTIQUES[stat]
    if groupe == "tout":
        return g == "tout"
    if groupe == "agents":
        return g in ("tout", "agents", "agents_ordonne")
    if groupe == "temps":
        return g in ("tout", "temps")
    raise GardeArret(f"groupe {groupe!r} inconnu ({GROUPES})")


def nom_statistique(alarme: str) -> str:
    for suffixe in ("_ville", "_cal"):
        if alarme.endswith(suffixe):
            return alarme[: -len(suffixe)]
    return alarme


def verifier_lot(Xb) -> np.ndarray:
    return L03.verifier_lot(Xb)


# --- statistiques symétriques (toutes les permutations de I) ---
def somme(Xb) -> np.ndarray:
    """Σ X sur valeurs triées (seuil exact z_α √n₀)."""
    return L03.lot_somme(Xb)


def maximum(Xb) -> np.ndarray:
    """Max sur toutes les cases = max par agent puis entre agents = max par pas puis entre pas."""
    return L03.lot_max(Xb)


def comptage(Xb, u: float) -> np.ndarray:
    return (verifier_lot(Xb) >= u).sum(axis=(1, 2))


# --- surveillance par agent (G_T) ---
def agent_moyenne(Xb) -> np.ndarray:
    """max_i Σ_t X_{i,t} / √T (somme de chaque agent sur valeurs triées dans le temps)."""
    Xb = verifier_lot(Xb)
    return (np.sort(Xb, axis=2).sum(axis=2) / math.sqrt(Xb.shape[2])).max(axis=1)


def agent_comptage(Xb, u: float) -> np.ndarray:
    """max_i #{t : X_{i,t} ≥ u}."""
    return (verifier_lot(Xb) >= u).sum(axis=2).max(axis=1)


# --- surveillance par pas, niveau essaim (G_A) ---
def sommes_par_pas(Xb) -> np.ndarray:
    """(R, T) : somme des K scores de chaque pas, sur valeurs triées entre agents."""
    return np.sort(verifier_lot(Xb), axis=1).sum(axis=1)


def pas_moyenne(Xb) -> np.ndarray:
    """max_t Σ_i X_{i,t} / √K."""
    Xb = verifier_lot(Xb)
    return (sommes_par_pas(Xb) / math.sqrt(Xb.shape[1])).max(axis=1)


def comptes_par_pas(Xb, u: float) -> np.ndarray:
    """(R, T) : nombre d'agents au-dessus de u à chaque pas (co-élévation du pas)."""
    return (verifier_lot(Xb) >= u).sum(axis=1)


def coelev_comptage(Xb, u: float) -> np.ndarray:
    """Co-élévation : max_t #{i : X_{i,t} ≥ u}."""
    return comptes_par_pas(Xb, u).max(axis=1)


def coelev_somme(Xb, m: int = M_COELEV) -> np.ndarray:
    """Co-élévation continue (T0.3) : max_t de la somme des m plus hauts scores du pas."""
    return L03.lot_co_elevation(Xb, m)


# --- versions séquentielles en e-valeurs, construites sur la co-élévation (G_A, ordre des pas) ---
def _lambdas(K: int, q: float, fractions) -> np.ndarray:
    f = np.asarray(fractions, dtype=float)
    if f.ndim != 1 or f.size == 0 or not np.all((f > 0) & (f < 1)):
        raise GardeArret(f"fractions de λ {fractions} : liste non vide dans ]0, 1[ attendue")
    if not (0.0 < q < 1.0):
        raise GardeArret(f"q = {q} hors de ]0, 1[")
    return f / (K * q)


def log_facteurs(C, K: int, q: float, fractions=FRACTIONS_LAMBDA) -> np.ndarray:
    """log e_t(λ) = log(1 + λ (C_t − K q)), λ < 1/(K q) : facteurs > 0, d'espérance 1 si E[C_t] = K q.

    C : (R, T) comptes par pas → (R, T, J)."""
    lam = _lambdas(K, q, fractions)
    C = np.asarray(C, dtype=float)
    return np.log1p(lam[None, None, :] * (C[:, :, None] - K * q))


def e_coelev(Xb, u: float, q: float, fractions=FRACTIONS_LAMBDA) -> np.ndarray:
    """max_{1≤n≤T} log M_n, M_n = moyenne sur λ de Π_{t≤n} e_t(λ) (processus e cumulé, Ville)."""
    Xb = verifier_lot(Xb)
    lf = log_facteurs(comptes_par_pas(Xb, u), Xb.shape[1], q, fractions)
    cum = np.cumsum(lf, axis=1)
    return (logsumexp(cum, axis=2) - math.log(lf.shape[2])).max(axis=1)


def ed_coelev(Xb, u: float, q: float, fractions=FRACTIONS_LAMBDA) -> np.ndarray:
    """Détecteur e (redémarrage de type CUSUM) sur les comptes : log D_n(λ) = max(log D_{n−1}(λ), 0)
    + log e_n(λ) ; max_n log de la moyenne sur λ. Seuil Monte-Carlo (pas de garantie de Ville à horizon fini)."""
    Xb = verifier_lot(Xb)
    lf = log_facteurs(comptes_par_pas(Xb, u), Xb.shape[1], q, fractions)
    R, T, J = lf.shape
    D = np.full((R, J), -np.inf)
    meilleur = np.full(R, -np.inf)
    for t in range(T):
        D = np.maximum(D, 0.0) + lf[:, t, :]
        meilleur = np.maximum(meilleur, logsumexp(D, axis=1) - math.log(J))
    return meilleur


def e_pas(Xb, rho: float) -> np.ndarray:
    """Processus e unilatéral de mélange normal lu aux frontières de pas (L4) : S_t = Σ_{s≤t} Σ_i X_{i,s},
    n_t = K t ; max_t log E⁺_t. Invariant sous G_A au bit près."""
    Xb = verifier_lot(Xb)
    R, K, T = Xb.shape
    S = np.cumsum(sommes_par_pas(Xb), axis=1)
    n = K * np.arange(1, T + 1, dtype=float)[None, :]
    return log_e_unilateral(S, n, 1.0, rho).max(axis=1)


def calculer(Xb, noms, params: dict) -> dict[str, np.ndarray]:
    """Valeurs des statistiques demandées. params : u, q, fractions, rho (pour e_pas)."""
    Xb = verifier_lot(Xb)
    out = {}
    for s in dict.fromkeys(noms):
        if s == "somme":
            out[s] = somme(Xb)
        elif s == "max":
            out[s] = maximum(Xb)
        elif s == "comptage":
            out[s] = comptage(Xb, params["u"])
        elif s == "agent_moyenne":
            out[s] = agent_moyenne(Xb)
        elif s == "agent_comptage":
            out[s] = agent_comptage(Xb, params["u"])
        elif s == "pas_moyenne":
            out[s] = pas_moyenne(Xb)
        elif s == "coelev_comptage":
            out[s] = coelev_comptage(Xb, params["u"])
        elif s == "coelev_somme3":
            if Xb.shape[1] < M_COELEV:
                raise GardeArret(f"co-élévation continue : K = {Xb.shape[1]} < {M_COELEV}")
            out[s] = coelev_somme(Xb, M_COELEV)
        elif s == "e_coelev":
            out[s] = e_coelev(Xb, params["u"], params["q"], params["fractions"])
        elif s == "ed_coelev":
            out[s] = ed_coelev(Xb, params["u"], params["q"], params["fractions"])
        elif s == "e_pas":
            out[s] = e_pas(Xb, params["rho"])
        else:
            raise GardeArret(f"statistique {s!r} inconnue")
    return out
