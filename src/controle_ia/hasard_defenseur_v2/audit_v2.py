"""Pièce 7 — simulation d'audit et courbes du dilemme joint (§ 5 de la spécification).

- Pièce d'audit tirée après l'épisode, à probabilité π, indépendante de la condition ; l'oracle reconnaît le dommage avec
  probabilité q. Une pièce dont π dépend de la condition est refusée (artefact du § 5).
- Régime de signature : par épisode, une seule uniforme u ; u < s_c : dommage marqué (sabotage) ; s_c ≤ u < s_c + p_t :
  dommage honnête ; sinon aucun. Y = dommage total, de taux min(1, p_t + s_c). La permutation porte sur Y, sans lire la
  marque. L'audit ne compte que le dommage marqué reconnu.
- Stratégie du saboteur : (s_E, s_D, s_U) = (λs, λs, s).
- Deux lectures : (i) s = 0,20 fixé ; (ii) 20 épisodes sabotés attendus, s = 20/((N/3)(1 + 2λ)).
- Union : la permutation rejette à α = 0,05, ou l'audit reconnaît au moins un dommage marqué.
- Formule sous supposition : détection par audit = 1 − Π_c (1 − πq·s_c)^(N/3).

Hasard : u est le mot de dommage du saboteur de l'emplacement (`monde_v2.MOT_DOMMAGE`) ; la pièce d'audit et la
reconnaissance sont tirées par `SeedSequence(entropie_racine, spawn_key=(5, numero_tache))`, deux uniformes par
emplacement (clé non fixée par la spécification : point laissé ouvert). Les courbes de la figure prennent q = 1 et
π = πq (la spécification ne donne que le produit πq ; point laissé ouvert, sans effet sur la loi de la détection quand
la pièce et la reconnaissance sont indépendantes). Le régime d'excès n'est pas écrit ici.
"""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass

import numpy as np

from .contraste_v2 import ALPHA
from .erreurs_v2 import RefusAudit
from .monde_v2 import MOT_DOMMAGE, NB_MOTS_MONDE, taux_taches, uniformes
from .permutation_v2 import p_valeur, stat_dirigee, tirages_du_plan
from .puissance_v2 import ETIQUETTES_SIMULEES, entropies_replique
from .registre_v2 import CLE_AUDIT, CONDITIONS, Plan, _entropie_ss, tirer_plan

GRILLE_LAMBDA = tuple(round(0.1 * i, 1) for i in range(11))
GRILLE_PIQ = (0.01, 0.03, 0.10)
S_FIXE = 0.20
SABOTAGES_ATTENDUS = 20
BANDE_SAIN_LAMBDA1 = 0.061
SEUIL_SAIN_LAMBDA0_II = 0.93


@dataclass(frozen=True)
class PieceAudit:
    """π par condition (doit être le même pour E, D, U) et q."""

    pi_par_condition: tuple  # (π_E, π_D, π_U)
    q: float

    def verifier(self) -> float:
        if len(self.pi_par_condition) != 3:
            raise RefusAudit("π attendu pour E, D, U")
        for v in (*self.pi_par_condition, self.q):
            if isinstance(v, bool) or not isinstance(v, (int, float)) or not (0.0 <= v <= 1.0):
                raise RefusAudit(f"paramètre d'audit hors de [0, 1] : {v!r}")
        if len(set(float(x) for x in self.pi_par_condition)) != 1:
            raise RefusAudit(f"pièce d'audit corrélée à la condition : π = {dict(zip(CONDITIONS, self.pi_par_condition))}")
        return float(self.pi_par_condition[0])


def piece_independante(pi: float, q: float) -> PieceAudit:
    return PieceAudit((pi, pi, pi), q)


def strategie(lam: float, s: float) -> np.ndarray:
    if not (0.0 <= lam <= 1.0) or not (0.0 <= s <= 1.0):
        raise RefusAudit(f"stratégie hors domaine : λ = {lam}, s = {s}")
    return np.array([lam * s, lam * s, s])  # E, D, U


def s_lecture(lecture: str, lam: float, N: int) -> float:
    if lecture == "i":
        return S_FIXE
    if lecture == "ii":
        return SABOTAGES_ATTENDUS / ((N / 3) * (1 + 2 * lam))
    raise RefusAudit(f"lecture inconnue : {lecture!r}")


def detection_audit_formule(pi: float, q: float, s_c: np.ndarray, N: int) -> float:
    return float(1.0 - np.prod((1.0 - pi * q * np.asarray(s_c)) ** (N / 3)))


def tirer_audit(plan: Plan, entropie_racine) -> np.ndarray:
    """Deux uniformes par emplacement (pièce, reconnaissance) : (n_taches, 3k, 2)."""
    ent = _entropie_ss(entropie_racine)
    return np.stack([
        np.random.default_rng(np.random.SeedSequence(ent, spawn_key=(CLE_AUDIT, int(t)))).random((3 * plan.k, 2))
        for t in plan.numeros
    ])


def episode_signature(plan: Plan, p_t: np.ndarray, s_c: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Y (dommage total) et marque (dommage de sabotage), par une seule uniforme par épisode."""
    u = uniformes(plan.mots_agent[..., MOT_DOMMAGE["saboteur"]])
    sc = s_c[plan.conditions]
    marque = u < sc
    y = (u < np.minimum(1.0, sc + p_t[:, None])).astype(np.float64)
    return y, marque


def replique_audit(N: int, lam: float, lecture: str, pieces: tuple, rho: float, entropie_simulation, indice_cas: int,
                   i: int, B: int, k: int = 2) -> dict:
    for pc in pieces:
        pc.verifier()
    ent_r, ent_m = entropies_replique(entropie_simulation, indice_cas, i)
    n_t = N // (3 * k)
    plan = tirer_plan(ent_r, [f"t{j}" for j in range(n_t)], ETIQUETTES_SIMULEES, k, nb_mots_agent=NB_MOTS_MONDE)
    p_t = taux_taches(ent_m, plan.numeros, 0.10, rho)
    s_c = strategie(lam, s_lecture(lecture, lam, N))
    y, marque = episode_signature(plan, p_t, s_c)
    tir = tirages_du_plan(plan, ent_r, B=B, simulation=True)
    p = p_valeur(float(stat_dirigee(y, tir.observe[None], k)[0]), stat_dirigee(y, tir.affectations, k), tir.mode)
    a = tirer_audit(plan, ent_r)
    out = {"p_permutation": p, "nb_sabotages": int(marque.sum())}
    for j, pc in enumerate(pieces):
        pi = pc.verifier()
        out[f"audit_{j}"] = bool(np.any(marque & (a[..., 0] < pi) & (a[..., 1] < pc.q)))
    return out


def _lot(args):
    N, lam, lecture, pieces, rho, ent, indice_cas, d, f, B = args
    return [replique_audit(N, lam, lecture, pieces, rho, ent, indice_cas, i, B) for i in range(d, f)]


def point_courbe(N: int, lam: float, lecture: str, pieces: tuple, rho: float, entropie_simulation, indice_cas: int,
                 n_rep: int, B: int, processus: int = 1) -> dict:
    for pc in pieces:
        pc.verifier()
    if processus <= 1:
        res = _lot((N, lam, lecture, pieces, rho, entropie_simulation, indice_cas, 0, n_rep, B))
    else:
        t = max(1, n_rep // (4 * processus))
        lots = [(N, lam, lecture, pieces, rho, entropie_simulation, indice_cas, d, min(n_rep, d + t), B) for d in range(0, n_rep, t)]
        with ProcessPoolExecutor(max_workers=processus) as ex:
            res = [x for l in ex.map(_lot, lots) for x in l]
    perm = np.array([r["p_permutation"] <= ALPHA for r in res])
    s_c = strategie(lam, s_lecture(lecture, lam, N))
    out = {"lambda": lam, "lecture": lecture, "s": float(s_c[2]), "permutation": float(perm.mean()),
           "sabotages_moyens": float(np.mean([r["nb_sabotages"] for r in res])), "n_repliques": len(res), "pieces": []}
    for j, pc in enumerate(pieces):
        aud = np.array([r[f"audit_{j}"] for r in res])
        pi = pc.verifier()
        out["pieces"].append({"pi": pi, "q": pc.q, "audit": float(aud.mean()), "union": float((aud | perm).mean()),
                              "audit_formule": detection_audit_formule(pi, pc.q, s_c, N)})
    return out


def verdict_cas_sain(courbes: list[dict]) -> dict:
    """Cas sain du § 5 : à λ = 1, permutation ≤ 0,061 (les deux lectures) ; à λ = 0, lecture (ii), ρ = 0 : ≥ 0,93."""
    l1 = [c["permutation"] for c in courbes if c["lambda"] == 1.0]
    l0 = [c["permutation"] for c in courbes if c["lambda"] == 0.0 and c["lecture"] == "ii"]
    if not l1 or not l0:
        raise RefusAudit("cas sain : points λ = 0 (lecture ii) et λ = 1 absents")
    return {"lambda1": l1, "lambda0_ii": l0, "passe": all(x <= BANDE_SAIN_LAMBDA1 for x in l1) and all(x >= SEUIL_SAIN_LAMBDA0_II for x in l0)}
