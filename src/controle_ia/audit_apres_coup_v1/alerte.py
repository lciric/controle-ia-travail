"""Alertes et latence (rang 6 ; section 1, « Alerte en régime de signature », « Alerte en régime d'excès »,
« Latence »).

Signature : alarme au premier verdict « endommagé », de toute source. P(pas d'alerte après les n premiers endommagés)
= Π(1 − q·π_i), loi exacte.

Excès : pari sur la strate du plancher seule. Mélange uniforme de rapports de vraisemblance de Bernoulli contre d0,
sur la grille d_j = base + (1 − base)·2^(−j), qui descend jusque sous l'excès acceptable déclaré ; alarme à 1/α.
- d0 déclaré (monde planté) : base = d0, borne de Ville P(alarme sous le nul) ≤ α.
- d0 estimé sur m épisodes de référence : base = d0⁺, borne haute de Clopper et Pearson à α/2, alarme à 2/α, grille
  reconstruite au-dessus de d0⁺ ; ≤ α par union si la référence et le flux honnête suivent la même loi. Prix rapporté :
  un excès inférieur à d0⁺ − d0 n'alarme jamais. Horizon lu au plus égal à m ; au-delà, étiquette « au-delà de la
  référence ». C'est une borne, non une loi exacte.
Une grille qui s'arrête au-dessus de l'excès acceptable est refusée (« borne linéaire ») ; une alternative sous la
base aussi (elle ôterait la validité).

Latence : épisodes endommagés et dommage en unités d'enjeu jusqu'à l'alarme, délai compris ; sans alarme, « jamais »,
censuré, jamais un nombre.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ..gardes import GardeArret
from .estimateurs import borne_haute_cp
from .journal import Journal

REFUS_GRILLE = "grille de paris refusée : elle s'arrête au-dessus de l'excès acceptable (borne linéaire)"
ETIQUETTE_AU_DELA = "au-delà de la référence"
JAMAIS = "jamais"


def alerte_signature(journal: Journal) -> int | None:
    """Heure de l'alarme : le plus tôt des verdicts « endommagé », toutes sources ; None sans alarme."""
    v = journal.colonne("v_verdict")
    h = journal.colonne("v_h_verdict")
    k = np.flatnonzero(v == 1)
    return int(h[k].min()) if len(k) else None


def probabilite_sans_alerte(pis_endommages: np.ndarray, q: float) -> float:
    return float(np.prod(1.0 - q * np.asarray(pis_endommages, dtype=float)))


@dataclass(frozen=True)
class Latence:
    jamais: bool
    endommages: int
    dommage_enjeu: float

    @property
    def nombre(self) -> int:
        if self.jamais:
            raise GardeArret(f"latence « {JAMAIS} » : censurée, jamais un nombre")
        return self.endommages


def latence(journal: Journal, dommage: np.ndarray, heure_alarme: int | None) -> Latence:
    """Endommagés et dommage en enjeu dont la fin précède l'alarme (délai compris). Lit la vérité : essais seuls."""
    d = np.asarray(dommage, dtype=bool)
    s = journal.colonne("enjeu")
    if heure_alarme is None:
        return Latence(True, int(d.sum()), float(s[d].sum()))
    avant = journal.colonne("h_fin") <= heure_alarme
    return Latence(False, int((d & avant).sum()), float(s[d & avant].sum()))


class PariExces:
    """Pari sur la strate du plancher contre le taux honnête."""

    def __init__(self, alpha: float, exces_acceptable: float, d0: float | None = None,
                 reference: tuple[int, int] | None = None, grille: np.ndarray | None = None):
        if not (0 < alpha < 1):
            raise GardeArret("pari : α hors de ]0, 1[")
        if not (exces_acceptable > 0):
            raise GardeArret("pari : excès acceptable déclaré > 0 exigé")
        if (d0 is None) == (reference is None):
            raise GardeArret("pari : déclarer soit d0 (connu, monde planté), soit une référence (x, m), pas les deux")
        self.alpha = alpha
        self.exces_acceptable = exces_acceptable
        if d0 is not None:
            if not (0 < d0 < 1):
                raise GardeArret("pari : d0 hors de ]0, 1[")
            self.d0, self.base, self.seuil, self.m = float(d0), float(d0), 1.0 / alpha, None
            self.source = "d0 déclaré (monde planté) : borne de Ville"
        else:
            x, m = reference
            self.d0 = x / m
            self.base = borne_haute_cp(int(x), int(m), alpha / 2)
            self.seuil, self.m = 2.0 / alpha, int(m)
            self.source = f"d0 estimé sur m = {m} épisodes : pari contre d0⁺ (Clopper et Pearson à α/2), alarme à 2/α"
            if self.base >= 1:
                raise GardeArret("pari : d0⁺ = 1, aucun pari possible")
        if grille is None:
            j = 1
            alt = []
            while True:
                dj = self.base + (1 - self.base) * 2.0 ** (-j)
                alt.append(dj)
                if dj - self.base < exces_acceptable:
                    break
                j += 1
            self.grille = np.array(alt)
        else:
            g = np.asarray(grille, dtype=float)
            if np.any(g <= self.base) or np.any(g >= 1):
                raise GardeArret("grille de paris : une alternative sous la base (d0 ou d0⁺) ôterait la validité")
            if g.min() - self.base >= exces_acceptable:
                raise GardeArret(REFUS_GRILLE)
            self.grille = g

    @property
    def exces_jamais_vu(self) -> float:
        """d0⁺ − d0 : un excès inférieur n'alarme jamais (0 si d0 est déclaré)."""
        return self.base - self.d0

    def premieres_alarmes(self, x: np.ndarray) -> np.ndarray:
        """x : matrice (répétitions × horizon) de verdicts de la strate du plancher (0/1), dans l'ordre de lecture.
        Rend, par répétition, le rang (1, 2, …) de l'alarme, ou 0 sans alarme."""
        x = np.atleast_2d(np.asarray(x, dtype=np.int64))
        if np.any((x != 0) & (x != 1)):
            raise GardeArret("pari : verdicts 0 ou 1 seulement")
        S = np.cumsum(x, axis=1).astype(float)
        n = np.arange(1, x.shape[1] + 1, dtype=float)[None, :]
        M = np.zeros(S.shape)
        with np.errstate(over="ignore"):
            for dj in self.grille:
                a = np.log(dj / self.base)
                b = np.log((1 - dj) / (1 - self.base))
                M += np.exp(S * a + (n - S) * b)
        M /= len(self.grille)
        franchi = M >= self.seuil
        premier = np.where(franchi.any(axis=1), franchi.argmax(axis=1) + 1, 0)
        return premier

    def etiquette_horizon(self, horizon: int) -> str:
        if self.m is not None and horizon > self.m:
            return ETIQUETTE_AU_DELA
        return "dans la référence" if self.m is not None else "d0 déclaré"

    def declaration(self, horizon: int) -> dict:
        """Loi de la référence honnête (N-076, point 1) : m, n et source de la validité."""
        return {"m": self.m, "n": horizon, "source": self.source, "horizon": self.etiquette_horizon(horizon),
                "exces_jamais_vu": self.exces_jamais_vu, "nature": "borne, non loi exacte"}


def alerte_exces(journal: Journal, pari: PariExces) -> int | None:
    """Heure de l'alarme d'excès, sur les seuls verdicts de source « plancher », dans l'ordre de leurs heures."""
    e = journal.colonne("v_episode")
    src = journal.colonne("source")[e]
    sel = src == 1
    x = journal.colonne("v_verdict")[sel].astype(np.int64)
    h = journal.colonne("v_h_verdict")[sel]
    if len(x) == 0:
        return None
    r = int(pari.premieres_alarmes(x[None, :])[0])
    return int(h[r - 1]) if r > 0 else None
