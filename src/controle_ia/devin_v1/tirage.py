"""Pièce 3 — tirage : tireur pur et rejeu du nul (spécification, section 3).

Pièce d'audit : A_t suit une loi de Bernoulli de propension π_t consignée. Le tirage
est fait par le harnais, avant toute extraction, depuis une racine propre au tireur ;
l'uniforme de la tâche t vient de SeedSequence(racine, spawn_key=(t,)).

Condition d'exactitude (section 3) :
- si π ne dépend d'aucune pièce passée, A* est retiré indépendamment ;
- sinon, A* est retiré dans l'ordre, π*_t recalculé par le tireur pur depuis A*_{<t}
  et les seules entrées consignées ;
- si π dépend d'un objet que le rejeu ne peut pas recalculer (verdict d'un audit non
  joué, sonde réapprise sur des épisodes audités) : refus, sans repli ; la course
  d'admission se joue alors avec une version de sonde gelée.

Lecture substituée : S_t est tirée par le harnais dans la loi empirique des lectures
de témoins, indépendamment de l'épisode ; mode « service » (loi des témoins) ou
« equilibre » (chaque décision à seuil prise une fois sur deux, section 3,
« Deux courses pour la pièce »).

Contrat de la propension : `propension(t, entrees_t, passe)` où `passe` est un tableau
(lots × t) de pièces passées ; elle rend un tableau (lots,) de propensions. Le même
appel sert au tirage observé (un lot) et au rejeu (B lots).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Hashable, Mapping, Sequence

import numpy as np

from . import RefusDevin
from .graines import empreinte_racine, generateur_tache

Propension = Callable[[int, Mapping, np.ndarray], np.ndarray]

DEPENDANCES_RECALCULABLES = frozenset({"entrees_consignees", "pieces_passees"})


@dataclass(frozen=True)
class JournalTirage:
    """Ce que le harnais consigne du tirage : identifiants, entrées, propensions, pièces."""

    identifiants: tuple
    entrees: tuple
    propensions: np.ndarray
    pieces: np.ndarray
    empreinte_racine: str


def _uniformes(racine: int, identifiants: Sequence[Hashable], taille: int | None = None) -> np.ndarray:
    """Uniformes par tâche ; colonne t ← SeedSequence(racine, spawn_key=(t,))."""
    if taille is None:
        return np.array([generateur_tache(racine, i).random() for i in identifiants])
    return np.stack([generateur_tache(racine, i).random(taille) for i in identifiants], axis=1)


def _exiger_propensions(p: np.ndarray, t: int, lots: int) -> np.ndarray:
    p = np.asarray(p, dtype=float).reshape(-1)
    if p.size == 1 and lots != 1:
        p = np.full(lots, p[0])
    if p.shape != (lots,):
        raise RefusDevin(f"propension de la tâche {t} : forme {p.shape}, ({lots},) attendue")
    if not np.all(np.isfinite(p)) or np.any(p < 0) or np.any(p > 1):
        raise RefusDevin(f"propension de la tâche {t} hors de [0, 1] ou non finie")
    return p


class TireurPiece:
    def __init__(self, propension: Propension, depend_du_passe: bool,
                 dependances: frozenset[str] = frozenset({"entrees_consignees"})):
        """`dependances` déclare de quoi dépend π. Tout objet hors des entrées consignées
        et des pièces passées (p. ex. « verdict_audit_non_joue », « sonde_reapprise ») :
        refus, sans repli."""
        hors = set(dependances) - DEPENDANCES_RECALCULABLES
        if hors:
            raise RefusDevin(
                f"propension dépendant de {sorted(hors)} : le rejeu ne peut pas la recalculer ; "
                "test refusé, jouer la course d'admission avec une version de sonde gelée")
        if depend_du_passe != ("pieces_passees" in dependances):
            raise RefusDevin("déclaration incohérente : depend_du_passe et dependances")
        self.propension = propension
        self.depend_du_passe = bool(depend_du_passe)

    def _propensions_dans_l_ordre(self, entrees: Sequence[Mapping], pieces_ou_uniformes: np.ndarray,
                                  mode: str) -> tuple[np.ndarray, np.ndarray]:
        """mode « uniformes » : tire A depuis U dans l'ordre ; « pieces » : recalcule π depuis A."""
        lots, n = pieces_ou_uniformes.shape
        pi = np.empty((lots, n))
        a = np.empty((lots, n), dtype=np.int8)
        for t in range(n):
            passe = a[:, :t] if self.depend_du_passe else np.empty((lots, 0), dtype=np.int8)
            pi[:, t] = _exiger_propensions(self.propension(t, entrees[t], passe), t, lots)
            if mode == "uniformes":
                a[:, t] = pieces_ou_uniformes[:, t] < pi[:, t]
            else:
                a[:, t] = pieces_ou_uniformes[:, t]
        return pi, a

    def tirer(self, racine: int, identifiants: Sequence[Hashable], entrees: Sequence[Mapping]) -> JournalTirage:
        if len(identifiants) != len(entrees):
            raise RefusDevin("identifiants et entrées de longueurs différentes")
        if len(set(identifiants)) != len(identifiants):
            raise RefusDevin("identifiants de tâche en double")
        u = _uniformes(racine, identifiants)[None, :]
        pi, a = self._propensions_dans_l_ordre(entrees, u, "uniformes")
        return JournalTirage(tuple(identifiants), tuple(entrees), pi[0], a[0], empreinte_racine(racine))

    def verifier_rejeu(self, journal: JournalTirage, racine: int) -> None:
        """Test de mort 5 et pureté : la racine consignée redonne propensions et pièces.

        Recalcule π depuis les seules entrées consignées et les pièces consignées
        (une propension tirée d'un objet changé depuis, p. ex. une sonde réapprise,
        ne se redonne pas : refus), puis retire les pièces depuis la racine.
        """
        if empreinte_racine(racine) != journal.empreinte_racine:
            raise RefusDevin("rejeu : la racine révélée n'a pas l'empreinte consignée")
        pi_recalc, _ = self._propensions_dans_l_ordre(journal.entrees, journal.pieces[None, :].astype(float), "pieces")
        if not np.array_equal(pi_recalc[0], journal.propensions):
            k = int(np.flatnonzero(pi_recalc[0] != journal.propensions)[0])
            raise RefusDevin(f"rejeu : propension de la tâche n° {k} non redonnée par le tireur pur")
        rejoue = self.tirer(racine, journal.identifiants, journal.entrees)
        if not np.array_equal(rejoue.pieces, journal.pieces):
            raise RefusDevin("test de mort 5 : le tireur rejoué ne redonne pas les pièces consignées")

    def rejeu_nul(self, journal: JournalTirage, racine_rejeu: int, B: int) -> tuple[np.ndarray, np.ndarray]:
        """Rend (A*, π*) de forme (B, n), retirés par le tireur du harnais."""
        if B < 1:
            raise RefusDevin("B < 1")
        if racine_rejeu is None:
            raise RefusDevin("racine de rejeu absente")
        if empreinte_racine(racine_rejeu) == journal.empreinte_racine:
            raise RefusDevin("racine de rejeu égale à la racine de la pièce : tirages non indépendants")
        u = _uniformes(racine_rejeu, journal.identifiants, B)
        if not self.depend_du_passe:
            pi = np.broadcast_to(journal.propensions, u.shape)
            return (u < pi).astype(np.int8), np.asarray(pi)
        pi, a = self._propensions_dans_l_ordre(journal.entrees, u, "uniformes")
        return a, pi


@dataclass(frozen=True)
class JournalLecture:
    identifiants: tuple
    lectures: np.ndarray
    mode: str
    empreinte_racine: str


class TireurLecture:
    """Tireur de la lecture substituée, dans la loi empirique des lectures de témoins."""

    def __init__(self, lectures_temoins: Sequence[float], mode: str = "service", seuil: float | None = None):
        lt = np.asarray(lectures_temoins, dtype=float)
        if lt.ndim != 1 or lt.size < 2 or not np.all(np.isfinite(lt)):
            raise RefusDevin("lectures de témoins : au moins deux valeurs finies exigées")
        if mode not in ("service", "equilibre"):
            raise RefusDevin(f"mode {mode!r} inconnu")
        self.lectures_temoins = np.sort(lt)
        self.mode = mode
        self.seuil = seuil
        if mode == "equilibre":
            if seuil is None:
                raise RefusDevin("mode équilibré : seuil de décision exigé")
            self._bas = self.lectures_temoins[self.lectures_temoins <= seuil]
            self._haut = self.lectures_temoins[self.lectures_temoins > seuil]
            if self._bas.size == 0 or self._haut.size == 0:
                raise RefusDevin("mode équilibré : aucune lecture de témoin d'un côté du seuil")

    def _depuis_uniformes(self, u: np.ndarray, v: np.ndarray) -> np.ndarray:
        if self.mode == "service":
            m = self.lectures_temoins.size
            return self.lectures_temoins[np.minimum((u * m).astype(int), m - 1)]
        haut = u >= 0.5
        ib = np.minimum((v * self._bas.size).astype(int), self._bas.size - 1)
        ih = np.minimum((v * self._haut.size).astype(int), self._haut.size - 1)
        return np.where(haut, self._haut[ih], self._bas[ib])

    def _uv(self, racine: int, identifiants, taille: int | None):
        if taille is None:
            uv = np.array([generateur_tache(racine, i).random(2) for i in identifiants])
            return uv[:, 0], uv[:, 1]
        uv = np.stack([generateur_tache(racine, i).random((2, taille)) for i in identifiants], axis=2)
        return uv[0], uv[1]

    def tirer(self, racine: int, identifiants: Sequence[Hashable]) -> JournalLecture:
        if len(set(identifiants)) != len(identifiants):
            raise RefusDevin("identifiants de tâche en double")
        u, v = self._uv(racine, identifiants, None)
        return JournalLecture(tuple(identifiants), self._depuis_uniformes(u, v), self.mode, empreinte_racine(racine))

    def verifier_rejeu(self, journal: JournalLecture, racine: int) -> None:
        if empreinte_racine(racine) != journal.empreinte_racine:
            raise RefusDevin("rejeu : la racine révélée n'a pas l'empreinte consignée")
        if not np.array_equal(self.tirer(racine, journal.identifiants).lectures, journal.lectures):
            raise RefusDevin("test de mort 5 : le tireur de lecture rejoué ne redonne pas les lectures consignées")

    def rejeu_nul(self, journal: JournalLecture, racine_rejeu: int, B: int) -> np.ndarray:
        if B < 1:
            raise RefusDevin("B < 1")
        if empreinte_racine(racine_rejeu) == journal.empreinte_racine:
            raise RefusDevin("racine de rejeu égale à la racine de la lecture")
        u, v = self._uv(racine_rejeu, journal.identifiants, B)
        return self._depuis_uniformes(u, v)


def propension_constante(pi: float) -> Propension:
    """Propension fixe (course équilibrée π = 0,5, ou taux de service)."""
    def f(t, entrees, passe):
        return np.full(passe.shape[0], float(pi))
    return f
