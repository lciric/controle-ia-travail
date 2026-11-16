"""Rejeu des bras (section « Bras » du texte scellé) sur les trajectoires calculées une fois par le juge réel.

Chaque carte est servie par une `Vue` : la règle d'un bras ne lit que les instants déjà révélés (garde d'accès ; lire
au-delà lève `GardeArret`, ligne de la liste d'arrêt) ; chaque bloc donné passe par un `Budget` (au-delà de B, ou de
6 000 pour F125 : `GardeArret`). Valeur e : trajectoire tronquée au dernier instant révélé, arrêtée au premier instant
où elle atteint m/α, sinon sa dernière valeur ; règle e-BH du juge (`cycle.appliquer_multiplicite`, m_fixe = 24,
α = 0,05), recoupée par une seconde écriture de la règle et de la valeur e. Après chaque bras, un **vérificateur
indépendant** (écriture par tableaux, distincte du moteur) refait l'allocation à partir des trajectoires, des positions
et de la graine du placebo ; tout écart lève `GardeArret`.

Bras : F (8 blocs par carte) ; F-arrêt (F plus arrêts bas et haut) ; A (tours, ordre des positions décalé du numéro du
tour, jusqu'à épuisement du budget ou des actives) ; P (comme A jusqu'à 200 tirages ou l'arrêt, puis chaque bloc à une
carte tirée au hasard parmi celles ni arrêtées haut ni au plafond, arrêtées bas comprises) ; P′ (comme P, blocs restants
à tour de rôle sur le même ensemble) ; F125 (10 blocs par carte) ; G (deux blocs par carte, puis chaque bloc à la carte
de plus grande log W courante parmi celles ni arrêtées haut ni au plafond ; égalité : plus petite position).
"""
from __future__ import annotations

import math

import numpy as np

from ..gardes import GardeArret
from . import banc_tirages_repartis_v1 as B

M, ALPHA, NB = B.M, B.ALPHA, B.NB_INSTANTS
SEUIL_HAUT = math.log(M / ALPHA)          # log(m/α), comme `cycle.appliquer_multiplicite`
SEUIL_BAS = math.log(1 / 20)
SEUIL_PROMUE_SEULE = math.log(1.0 / ALPHA)
PART_BLOCS, PART125_BLOCS = B.PART // B.BLOC, 250 // B.BLOC           # 8 et 10
BUDGET_BLOCS = M * PART_BLOCS                                          # 192 blocs = 4 800 tirages
BUDGET125_BLOCS = M * PART125_BLOCS                                    # 240 blocs = 6 000 tirages
BRAS_T = ("F", "F-arret", "A", "P", "P-prime", "F125")
BRAS_N = BRAS_T + ("G",)


class Vue:
    """Trajectoire d'une carte servie bloc par bloc ; seuls les instants révélés sont lisibles."""

    __slots__ = ("_valeurs", "n")

    def __init__(self, valeurs):
        self._valeurs = tuple(valeurs)
        if len(self._valeurs) != NB:
            raise GardeArret(f"vue : {len(self._valeurs)} instants au lieu de {NB}")
        self.n = 0

    def reveler(self) -> float:
        if self.n >= NB:
            raise GardeArret("plafond de 800 tirages dépassé : bloc au-delà du plan")
        self.n += 1
        return self._valeurs[self.n - 1]

    def lire(self, k: int) -> float:
        if not 0 <= k < self.n:
            raise GardeArret(f"la règle lit l'instant {k + 1} sur {self.n} révélés : instant non révélé (garde d'accès)")
        return self._valeurs[k]

    def courante(self) -> float:
        return self.lire(self.n - 1)

    def revelees(self) -> tuple:
        return self._valeurs[:self.n]


class Budget:
    def __init__(self, blocs: int):
        self.total, self.donnes = blocs, 0

    @property
    def reste(self) -> int:
        return self.total - self.donnes

    def prendre(self) -> None:
        if self.donnes >= self.total:
            raise GardeArret(f"tirages donnés > budget ({self.total * B.BLOC}) : défaut")
        self.donnes += 1


def arretee_haut(v: Vue) -> bool:
    return any(x >= SEUIL_HAUT for x in v.revelees())


def arretee_bas(v: Vue) -> bool:
    """log W < log(1/20) à un instant révélé d'au moins 50 tirages (indice ≥ 1)."""
    r = v.revelees()
    return any(x < SEUIL_BAS for k, x in enumerate(r) if k >= 1)


def ordre_du_tour(positions, tour: int) -> list[int]:
    """Cartes dans l'ordre des positions, décalé du numéro du tour."""
    carte_a = [0] * M
    for i, p in enumerate(positions):
        carte_a[p] = i
    return [carte_a[(k + tour) % M] for k in range(M)]


def par_position(positions, indices) -> list[int]:
    return sorted(indices, key=lambda i: positions[i])


def donner(v: Vue, budget: Budget) -> None:
    budget.prendre()
    v.reveler()


def _tours(vues, positions, budget, plafond: int, premier_tour: int, eligible) -> int:
    tour = premier_tour
    while True:
        actives = [i for i in ordre_du_tour(positions, tour) if eligible(vues[i]) and vues[i].n < plafond]
        if not actives or budget.reste == 0:
            return tour
        for i in actives:
            if budget.reste == 0:
                break
            donner(vues[i], budget)
        tour += 1
        if tour - premier_tour > NB:
            raise GardeArret("rejeu : plus de 32 tours (boucle sans fin)")


def active(v: Vue) -> bool:
    return not arretee_haut(v) and not arretee_bas(v)


def eligible_elargi(v: Vue) -> bool:
    return not arretee_haut(v)


def bras_F(vues, positions, budget, rng=None, blocs=PART_BLOCS):
    for i in range(M):
        for _ in range(blocs):
            donner(vues[i], budget)


def bras_F125(vues, positions, budget, rng=None):
    bras_F(vues, positions, budget, blocs=PART125_BLOCS)


def bras_F_arret(vues, positions, budget, rng=None):
    _tours(vues, positions, budget, PART_BLOCS, 0, active)


def bras_A(vues, positions, budget, rng=None):
    _tours(vues, positions, budget, NB, 0, active)


def bras_P(vues, positions, budget, rng):
    _tours(vues, positions, budget, PART_BLOCS, 0, active)
    while budget.reste > 0:
        candidates = par_position(positions, [i for i in range(M) if eligible_elargi(vues[i]) and vues[i].n < NB])
        if not candidates:
            return
        donner(vues[candidates[int(rng.integers(len(candidates)))]], budget)


def bras_P_prime(vues, positions, budget, rng=None):
    tour = _tours(vues, positions, budget, PART_BLOCS, 0, active)
    _tours(vues, positions, budget, NB, max(tour, PART_BLOCS), eligible_elargi)


def bras_G(vues, positions, budget, rng=None):
    for i in ordre_du_tour(positions, 0):
        for _ in range(2):
            donner(vues[i], budget)
    while budget.reste > 0:
        candidates = [i for i in range(M) if not arretee_haut(vues[i]) and vues[i].n < NB]
        if not candidates:
            return
        j = max(candidates, key=lambda i: (vues[i].courante(), -positions[i]))
        donner(vues[j], budget)


BRAS = {"F": (bras_F, BUDGET_BLOCS), "F-arret": (bras_F_arret, BUDGET_BLOCS), "A": (bras_A, BUDGET_BLOCS),
        "P": (bras_P, BUDGET_BLOCS), "P-prime": (bras_P_prime, BUDGET_BLOCS), "F125": (bras_F125, BUDGET125_BLOCS),
        "G": (bras_G, BUDGET_BLOCS)}


# --- valeurs e et règle e-BH ----------------------------------------------------------------------------------------
def log_valeur_e(revelees) -> float:
    """Richesse cumulée au premier instant révélé où elle atteint m/α, sinon au dernier instant révélé (règle (vi))."""
    if not revelees:
        raise GardeArret("valeur e d'une carte sans instant révélé")
    return next((v for v in revelees if v >= SEUIL_HAUT), revelees[-1])


def ebh_independant(log_e: list[float]) -> list[int]:
    """Seconde écriture de la règle e-BH (k* = plus grand k tel que e_(k) ≥ m/(α·k))."""
    ordre = sorted(range(len(log_e)), key=lambda i: -log_e[i])
    k_etoile = 0
    for k, i in enumerate(ordre, 1):
        if log_e[i] >= math.log(M / (ALPHA * k)):
            k_etoile = k
    return sorted(ordre[:k_etoile])


def promotions_ebh(J, revelees_par_carte: list) -> tuple[list[int], int, dict]:
    """Règle e-BH du juge sur les trajectoires tronquées ; rend (promues, m, log_e lus par le juge)."""
    issues = {}
    for i, rev in enumerate(revelees_par_carte):
        issues[f"c{i:02d}"] = {"verdict_final": "survit" if any(v >= SEUIL_PROMUE_SEULE for v in rev) else "eliminee",
                               "motif": "", "pari": {"trajectoire_log_w": list(rev)}}
    res = J.cycle.appliquer_multiplicite(issues, ALPHA, m_fixe=M)
    retenues = set(res["retenues"])
    promues = sorted(int(n[1:]) for n, iss in issues.items() if n in retenues and iss["verdict_final"] == "survit")
    log_e = {int(n[1:]): iss["pari"]["multiplicite"]["log_e"] for n, iss in issues.items()}
    return promues, res["m"], log_e


def generateur_placebo(racine: int, f: int, g: int) -> np.random.Generator:
    return B.generateur(racine, f, g, 1000)


def jouer_bras(J, nom: str, evaluations: dict, positions, racine: int, f: int, g: int) -> dict:
    fonction, blocs = BRAS[nom]
    vues = [Vue(evaluations[i]["trajectoire_log_w"]) for i in range(M)]
    budget = Budget(blocs)
    rng = generateur_placebo(racine, f, g) if nom == "P" else None
    fonction(vues, positions, budget, rng)
    n = [v.n for v in vues]
    if sum(n) > blocs:
        raise GardeArret(f"bras {nom} : tirages donnés {25 * sum(n)} > {25 * blocs} : défaut")
    if budget.donnes != sum(n):
        raise GardeArret(f"bras {nom} : {sum(n)} blocs révélés, {budget.donnes} comptés : garde du budget contournée")
    if nom == "F" and n != [PART_BLOCS] * M or nom == "F125" and n != [PART125_BLOCS] * M:
        raise GardeArret(f"bras {nom} : part fixe non respectée")
    attendu = allocation_independante(nom, [evaluations[i]["trajectoire_log_w"] for i in range(M)], positions, racine, f, g)
    if list(attendu) != n:
        raise GardeArret(f"bras {nom} : allocation non conforme à la règle écrite (vérificateur indépendant) : {n} ≠ {list(attendu)}")
    revelees = [v.revelees() for v in vues]
    log_e = [log_valeur_e(r) for r in revelees]
    promues, m, log_e_juge = promotions_ebh(J, revelees)
    if m != M:
        raise GardeArret(f"bras {nom} : m = {m} ≠ 24 (m compté après coup)")
    for i in range(M):
        if log_e_juge[i] is None or abs(round(log_e[i], 6) - log_e_juge[i]) > 1e-9:
            raise GardeArret(f"bras {nom} : valeur e de la carte {i} ({log_e[i]}) ≠ valeur e lue par le juge ({log_e_juge[i]})")
    if ebh_independant(log_e) != promues:
        raise GardeArret(f"bras {nom} : promotions du juge {promues} ≠ seconde écriture de e-BH")
    arrets = []
    for v in vues:
        if arretee_haut(v):
            arrets.append("haut")
        elif v.n >= NB:
            arrets.append("plafond")
        elif arretee_bas(v):
            arrets.append("bas")
        else:
            arrets.append("fin")
    return {"blocs": n, "tirages": 25 * sum(n), "log_e": log_e, "promues": promues, "arrets": arrets}


def rejouer_generation(J, evaluations: dict, positions, racine: int, famille: str, g: int) -> dict:
    f = B.FAMILLES[famille]
    noms = BRAS_N if famille == "N" else BRAS_T
    return {nom: jouer_bras(J, nom, evaluations, positions, racine, f, g) for nom in noms}


# --- vérificateur indépendant (écriture par tableaux) ------------------------------------------------------------------
def allocation_independante(nom: str, trajectoires, positions, racine: int, f: int, g: int) -> np.ndarray:
    lw = np.asarray(trajectoires, dtype=float)
    pos = np.asarray(positions)
    inv = np.argsort(pos)                        # inv[p] = carte à la position p
    n = np.zeros(M, dtype=int)
    k = np.arange(NB)

    def haut():
        return ((lw >= SEUIL_HAUT) & (k[None, :] < n[:, None])).any(axis=1)

    def bas():
        return ((lw < SEUIL_BAS) & (k[None, :] < n[:, None]) & (k[None, :] >= 1)).any(axis=1)

    def tours(plafond, budget, debut, elargi):
        tour = debut
        while True:
            ok = ~haut() & (n < plafond) & (np.ones(M, bool) if elargi else ~bas())
            ordre = inv[(np.arange(M) + tour) % M]
            act = [i for i in ordre if ok[i]]
            if not act or budget - n.sum() <= 0:
                return tour
            for i in act:
                if budget - n.sum() <= 0:
                    break
                n[i] += 1
            tour += 1

    if nom == "F":
        n[:] = PART_BLOCS
    elif nom == "F125":
        n[:] = PART125_BLOCS
    elif nom == "F-arret":
        tours(PART_BLOCS, BUDGET_BLOCS, 0, False)
    elif nom == "A":
        tours(NB, BUDGET_BLOCS, 0, False)
    elif nom == "P":
        tours(PART_BLOCS, BUDGET_BLOCS, 0, False)
        rng = np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=(f, g, 1000)))
        while BUDGET_BLOCS - n.sum() > 0:
            c = [i for i in inv if not haut()[i] and n[i] < NB]
            if not c:
                break
            n[c[int(rng.integers(len(c)))]] += 1
    elif nom == "P-prime":
        t = tours(PART_BLOCS, BUDGET_BLOCS, 0, False)
        tours(NB, BUDGET_BLOCS, max(t, PART_BLOCS), True)
    elif nom == "G":
        n[:] = 2
        while BUDGET_BLOCS - n.sum() > 0:
            libre = ~haut() & (n < NB)
            if not libre.any():
                break
            cour = np.where(libre, lw[np.arange(M), np.maximum(n - 1, 0)], -np.inf)
            meilleurs = np.flatnonzero(cour == cour.max())
            n[min(meilleurs, key=lambda i: pos[i])] += 1
    else:
        raise GardeArret(f"bras inconnu {nom!r}")
    return n
