"""Idée 1.1 (préenregistrement scellé `3ffe1739…`), bras 3 et 4 : projection par blocs (J9-P, La-P), forme scindée.

La forme d'origine (`projection_methodes_v1._blocs_projection`, recopiée octet pour octet) calcule en un seul appel la
projection, le certificat **et** la valeur e de chaque bloc : elle reçoit les issues. Le texte exige que le module de
projection ne reçoive jamais une issue du bloc qu'il projette (garde d'accès), et, sous gel de l'historique, que la
projection du bloc b soit calculée et empreintée avant le tirage du bloc b. D'où deux fonctions, qui reprennent les
opérations de `_blocs_projection` dans le même ordre, avec les mêmes optimiseur et certificat (`projection_commun_v1`,
octet pour octet) :
- `projeter(L, Qb, questions, C, blocs)` : départ chaud (projection sans coupure du bloc, 300 pas depuis le centre, lot des
  blocs demandés), puis 150 pas pour chaque question (bloc, partition) ; certificat exact ; **aucune issue reçue** ;
- `valeurs_e(proj, Qb, issues_par_bloc)` : log e de chaque question, une fois les issues du bloc tirées.
L'égalité avec `_blocs_projection` (essai) et avec `m3_toutes_coupures` (essai d'égalité EP, 10⁻⁹ nat) est éprouvée.

Familles : J9-P — famille linéaire, sous-population, et, pour chaque trait j et chaque valeur c de z_j sur le plan gelé,
la coupure {z_j ≤ c} | {z_j > c} (au plus 402 familles ; dans un bloc, 26 partitions par trait, dont 2 égales à la famille
linéaire) ; La-P — famille linéaire, coupure A, coupure B de l'archive (même optimiseur, « comme J9-P »).

Gardes (liste d'arrêt) : certificat non calculé, non fini, ou < 1 − 10⁻⁹ ; loi projetée non positive (P5) ; forme de la
garde P4 absente pour une carte qui lit l'historique (`exiger_garde`) ; projection sous gel recevant un autre nombre
d'issues que celles des blocs passés (`FluxFrais.passe`).
"""
from __future__ import annotations

import hashlib
import math

import numpy as np

from ..gardes import GardeArret
from . import projection_commun_v1 as cm
from . import projection_methodes_v1 as me

S = 25
NB = len(cm.BLOCS)
K, J = cm.K, cm.J
SEUIL_CERTIFICAT = 1.0 - 1e-9
FORMES_GARDE = ("refus", "gel", "nu")     # « nu » : sans garde, déclaré sur Hs, Hm, Hg, Hn, H7 seulement


class GardeAcces(GardeArret):
    """Une issue du bloc projeté (ou d'un bloc suivant) atteint la projection ou le certificat : arrêt ; défaut."""


# --- questions --------------------------------------------------------------------------------------------------------
def questions_j9p(z: np.ndarray, g: np.ndarray, b: int) -> list[np.ndarray]:
    """Questions du bloc b (ordre de `m3_toutes_coupures`) : sans coupure, sous-population, puis, pour chaque trait, les 24
    partitions non triviales « i plus petits points du bloc » (rang ≥ i)."""
    a, e = cm.BLOCS[b]
    q = [np.zeros(e - a, int), np.asarray(g[a:e], int)]
    for j in range(cm.D):
        rang = np.argsort(np.argsort(z[a:e, j]))
        for i in range(1, 25):
            q.append((rang >= i).astype(int))
    return q


def questions_lap(cA: np.ndarray, cB: np.ndarray, b: int) -> list[np.ndarray]:
    a, e = cm.BLOCS[b]
    return [np.zeros(e - a, int), np.asarray(cA[a:e], int), np.asarray(cB[a:e], int)]


# --- projection (sans issue) -------------------------------------------------------------------------------------------
def projeter(L: np.ndarray, Qb: np.ndarray, questions: dict, C: int, blocs) -> dict:
    """L (200, J, K) lois connues ; Qb (8, 25, K) numérateur par bloc (seules les lignes des `blocs` demandés sont lues) ;
    questions {b: [cellules (25,)]}. Rend, par bloc, tau, v, u, P, c et l'empreinte du journal. **Ne reçoit aucune issue.**"""
    exiger_blocs_alignes()
    blocs = [int(b) for b in blocs]
    Gb = np.stack([np.transpose(L[a:e], (0, 2, 1)) for (a, e) in cm.BLOCS])          # (8, S, K, J)
    Gw, Qw = Gb[blocs], np.asarray(Qb, dtype=float)[blocs]
    t0, v0, u0, _ = cm.em_commun(Gw, np.broadcast_to(np.eye(cm.K)[None, None], (len(blocs), S, cm.K, cm.K)), Qw,
                                 np.zeros((len(blocs), S), int), 1, me.IT_PROJ)
    ib = np.array([k for k, b in enumerate(blocs) for _ in questions[b]])
    cells = np.stack([c for b in blocs for c in questions[b]])
    nb = len(ib)
    G = Gw[ib]
    Ind = np.broadcast_to(np.eye(cm.K)[None, None], (nb, S, cm.K, cm.K))
    Wt = Qw[ib]
    depart = (0.9 * t0[ib] + 0.01, 0.9 * np.repeat(v0[ib], C, 1) + 0.1 / cm.J, 0.9 * u0[ib] + 0.1 / cm.K)
    tau, v, u, _ = cm.em_commun(G, Ind, Wt, cells, C, me.IT_CHAUD, depart=depart)
    P = cm.probas_commun(G, Ind, cells, C, (tau, v, u))
    c = cm.certificat_commun(G, Wt, P, cells, C)
    exiger_certificats(c)
    if not np.all(np.isfinite(P)) or not np.all(P > 0):
        raise GardeArret("projection : loi projetée non strictement positive (P5) : arrêt ; défaut")
    sortie = {}
    k = 0
    for i, b in enumerate(blocs):
        n = len(questions[b])
        sl = slice(k, k + n)
        d = {"tau": tau[sl].copy(), "v": v[sl].copy(), "u": u[sl].copy(), "P": P[sl].copy(), "c": c[sl].copy(), "n": n}
        d["empreinte"] = empreinte_journal(b, d)
        sortie[b] = d
        k += n
    return sortie


def exiger_blocs_alignes() -> None:
    """Blocs B_1 à B_8 = les huit intervalles de 25 instances entre instants du juge (T₈ = 25, 50, …, 200)."""
    attendus = [(25 * k, 25 * (k + 1)) for k in range(8)]
    if [(int(a), int(e)) for a, e in cm.BLOCS] != attendus:
        raise GardeArret("blocs de la projection décalés des instants de lecture du juge : arrêt ; défaut")


def exiger_certificats(c) -> None:
    c = np.asarray(c, dtype=float)
    if c.size == 0:
        raise GardeArret("certificat de bloc non calculé : arrêt ; défaut")
    if not np.all(np.isfinite(c)):
        raise GardeArret("certificat de bloc non fini : arrêt ; défaut")
    if float(c.min()) < SEUIL_CERTIFICAT:
        raise GardeArret(f"certificat de bloc {float(c.min())!r} < 1 − 10⁻⁹ (impossible en théorie) : arrêt ; défaut")


def empreinte_journal(b: int, d: dict) -> str:
    h = hashlib.sha256(f"bloc {int(b)}".encode())
    for cle in ("tau", "v", "u", "c"):
        h.update(np.ascontiguousarray(d[cle], dtype=np.float64).tobytes())
    return h.hexdigest()


def valeurs_e(proj: dict, Qb: np.ndarray, issues_par_bloc: dict) -> dict:
    """log e de chaque question de chaque bloc projeté, sur les issues du bloc (tirées après la projection)."""
    sortie = {}
    for b, d in proj.items():
        y = np.asarray(issues_par_bloc[b], int)
        if y.shape != (S,):
            raise GardeArret(f"bloc {b} : {y.shape} issues au lieu de {S}")
        if empreinte_journal(b, d) != d["empreinte"]:
            raise GardeArret(f"bloc {b} : journal de projection modifié après son empreinte")
        P, Wt = d["P"], np.broadcast_to(np.asarray(Qb[b], dtype=float), (d["n"], S, cm.K))
        yy = np.broadcast_to(y, (d["n"], S))
        lp = np.log(np.maximum(np.take_along_axis(P, yy[..., None], 2)[..., 0], cm.PLANCHER))
        lq = np.log(np.maximum(np.take_along_axis(Wt, yy[..., None], 2)[..., 0], cm.PLANCHER))
        sortie[b] = (lq - lp).sum(1) - S * np.log(np.maximum(1.0, d["c"]))
    return sortie


# --- processus par famille --------------------------------------------------------------------------------------------
def processus_j9p(loge: dict, z: np.ndarray) -> tuple[np.ndarray, list[str]]:
    """Processus cumulés (familles × 8) de J9-P, dans l'ordre : linéaire, sous-population, puis chaque coupure de chaque
    trait (valeurs distinctes du plan triées) ; rend (tableau, noms)."""
    lin = np.array([loge[b][0] for b in range(NB)])
    sp_ = np.array([loge[b][1] for b in range(NB)])
    proc, noms = [np.cumsum(lin), np.cumsum(sp_)], ["lineaire", "sous_population"]
    k = 2
    for j in range(cm.D):
        tab = np.zeros((NB, 26))
        tab[:, 0] = lin
        tab[:, 25] = lin
        tab[:, 1:25] = np.stack([loge[b][k:k + 24] for b in range(NB)])
        k += 24
        coupes = np.sort(np.unique(z[:, j]))
        idx = np.stack([np.searchsorted(np.sort(z[a:e, j]), coupes, side="right") for (a, e) in cm.BLOCS], 1)
        proc.append(np.cumsum(tab[np.arange(NB)[None, :], idx], axis=1))
        noms += [f"coupure:z{j}<={c!r}" for c in coupes.tolist()]
    return np.vstack([np.atleast_2d(p) for p in proc]), noms


def processus_lap(loge: dict) -> tuple[np.ndarray, list[str]]:
    tab = np.array([[loge[b][q] for b in range(NB)] for q in range(3)])
    return np.cumsum(tab, axis=1), ["lineaire", "coupure_A", "coupure_B"]


def journal_resume(proj: dict, proc: np.ndarray, noms: list[str], famille_retenue: int) -> dict:
    """Résumé par répétition : plus grand et médian c − 1, coût Σ 25·log max(1, c) du processus retenu (calculé sur ses
    seules questions), empreinte du tableau des poids projetés."""
    c = np.concatenate([proj[b]["c"] for b in sorted(proj)])
    h = hashlib.sha256("".join(proj[b]["empreinte"] for b in sorted(proj)).encode()).hexdigest()
    return {"c_moins_1_max": float(c.max() - 1.0), "c_moins_1_mediane": float(np.median(c) - 1.0),
            "famille_retenue": noms[famille_retenue], "empreinte_poids": h}


def cout_famille(proj: dict, z: np.ndarray, famille: str) -> float:
    """Coût Σ_b 25·log max(1, c_{F,b}) de la famille F (J9-P)."""
    tot = 0.0
    for b in range(NB):
        a, e = cm.BLOCS[b]
        c = proj[b]["c"]
        if famille == "lineaire":
            q = 0
        elif famille == "sous_population":
            q = 1
        elif famille.startswith("coupure:z"):
            j = int(famille[len("coupure:z")])
            seuil = float(famille.split("<=")[1])
            i = int(np.searchsorted(np.sort(z[a:e, j]), seuil, side="right"))
            q = 0 if i in (0, 25) else 2 + 24 * j + (i - 1)
        elif famille in ("coupure_A", "coupure_B"):
            q = 1 if famille == "coupure_A" else 2
        else:
            raise GardeArret(f"famille inconnue {famille!r}")
        tot += S * math.log(max(1.0, float(c[q])))
    return tot


# --- flux d'issues fraîches, bloc par bloc, et garde d'accès ---------------------------------------------------------------
class FluxFrais:
    """Issues fraîches tirées bloc par bloc d'un seul générateur, dans l'ordre (même suite d'appels sur toutes les lignes).
    `passe(b)` rend exactement les issues des blocs < b, et seulement si exactement b − 1 blocs sont tirés."""

    def __init__(self, tireur):
        self._tireur = tireur          # fonction (b) -> liste de 25 issues du bloc b
        self.issues: list[int] = []
        self.blocs_tires = 0

    def tirer_bloc(self, b: int) -> list[int]:
        if b != self.blocs_tires:
            raise GardeArret(f"bloc {b} tiré hors de l'ordre (déjà {self.blocs_tires})")
        ys = list(self._tireur(b))
        if len(ys) != S:
            raise GardeArret(f"bloc {b} : {len(ys)} issues")
        self.issues.extend(ys)
        self.blocs_tires += 1
        return ys

    def passe(self, b: int) -> list[int]:
        """Historique tronqué au début du bloc b (0-indexé) : les 25·b issues des blocs passés."""
        if self.blocs_tires != b:
            raise GardeAcces(f"projection sous gel du bloc {b} demandée alors que {self.blocs_tires} blocs sont tirés : "
                             "une issue du bloc courant ou suivant serait reçue : arrêt ; défaut")
        h = list(self.issues[:S * b])
        if len(h) != S * b:
            raise GardeAcces("historique tronqué de longueur fausse")
        return h

    def complet(self) -> list[int]:
        if self.blocs_tires != NB:
            raise GardeArret(f"issues incomplètes ({self.blocs_tires} blocs)")
        return list(self.issues)


def exiger_garde(lit_historique: bool, forme: str | None, ligne_h: bool) -> str:
    """Garde P4 : une carte qui lit l'historique n'arrive à J9-P ou à La-P que par une forme déclarée ; « nu » seulement
    sur les lignes H déclarées."""
    if forme not in FORMES_GARDE:
        if lit_historique:
            raise GardeArret("carte qui lit l'historique arrivée à un bras à projection sans forme de la garde P4 : arrêt ; défaut")
        raise GardeArret(f"forme de garde inconnue {forme!r}")
    if forme == "nu" and not ligne_h:
        raise GardeArret("J9-P sans garde (« nu ») hors des lignes Hs, Hm, Hg, Hn, H7 : interdit (texte, bras 3)")
    return forme
