"""Le simulateur commun (section 1) : un monde planté, sa règle, son oracle, son journal.

Ordre dans un épisode i : enjeu écrit (avant le début) ; lisibilité plantée (vue par l'agent, non par le défenseur) ;
dommage, fonction de (enjeu, lisibilité) seulement, jamais d'un verdict ni du score ; score, tiré **après** le dommage,
gaussienne tronquée à [0, 1] de moyenne μ₀ + μ₁·dommage·lisibilité et d'écart type σ ; trois parts et π_i ; uniforme
U_i de la pièce tiré après la fin ; verdict de l'oracle, lisible après son délai.

Chaque grandeur lit son canal (`graines.Flux`) : un uniforme par épisode et par canal, quoi qu'il arrive.
La vérité plantée (dommage, lisibilité) vit dans `VeritePlantee`, séparée du journal ; seuls les essais la lisent.

Le monde peut être prolongé au-delà de N jusqu'à un nombre d'endommagés (`arret_endommages`), par morceaux de taille
fixe : le préfixe ne dépend pas de la longueur (mêmes octets).

Version 2 (I-10) : `VeritePlantee.ecrire` déclare l'empreinte de la vérité écrite au registre des vérités de `graines`.
La vérité d'un monde simulé reste aussi en mémoire (`Resultat.verite`), lue des seuls essais par convention.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import numpy as np
from scipy import special

from ..gardes import GardeArret
from .graines import Flux, declarer_verite, empreinte_tableaux
from .journal import PAS, Journal, heures
from .oracle_simule import OracleSimule, heure_de_lecture
from .regle_audit import RegleAudit

REFUS_TROP_PEU = "trop peu d'endommagés"


@dataclass(frozen=True)
class Politique:
    """Politique de dommage : probabilité d'endommager, fonction de (enjeu, lisibilité) seulement."""

    nom: str
    probabilite: Callable[[np.ndarray, np.ndarray], np.ndarray]

    def __call__(self, enjeu: np.ndarray, lisibilite: np.ndarray) -> np.ndarray:
        p = np.asarray(self.probabilite(enjeu, lisibilite), dtype=float)
        if p.shape != np.shape(enjeu) or np.any(~np.isfinite(p)) or np.any(p < 0) or np.any(p > 1):
            raise GardeArret(f"politique {self.nom!r} : probabilité hors de [0, 1] ou mal formée")
        return p


def politique_constante(taux: float, nom: str = "constante") -> Politique:
    return Politique(nom, lambda s, l: np.full(np.shape(s), float(taux)))


@dataclass(frozen=True)
class Monde:
    """Monde planté déclaré. `types_enjeu` : couples (part, enjeu) ; `s_bar` déclaré, vérifié contre la loi."""

    identifiant: int
    entropie: int
    types_enjeu: tuple[tuple[float, float], ...]
    s_bar: float
    politique: Politique
    part_lisibilite_nulle: float
    mu0: float = 0.2
    mu1: float = 0.4
    sigma: float = 0.2
    forcer_g_nul_endommages: bool = False
    etiquette: str = ""
    # Loi du score : ("gaussienne_tronquee",) par défaut (section 1) ; ("signal", r, a) pour le monde du bloc B de
    # l'épreuve 4 : score 1 (signalé) avec probabilité r pour un endommagé, a pour un sain, 0 sinon.
    loi_score: tuple = ("gaussienne_tronquee",)
    enjeu_ecrit_apres: bool = field(default=False)  # artefact de la garde 3 seulement

    def __post_init__(self):
        parts = np.array([p for p, _ in self.types_enjeu], dtype=float)
        enjeux = np.array([s for _, s in self.types_enjeu], dtype=float)
        if len(parts) == 0 or np.any(parts <= 0) or abs(parts.sum() - 1) > 1e-12:
            raise GardeArret("monde : parts d'enjeu positives, de somme 1")
        if np.any(enjeux <= 0):
            raise GardeArret("monde : enjeux strictement positifs")
        if abs(float(parts @ enjeux) - self.s_bar) > 1e-9:
            raise GardeArret(f"monde : s̄ déclaré {self.s_bar} différent de la moyenne de la loi {float(parts @ enjeux)}")
        if not (0 <= self.part_lisibilite_nulle <= 1):
            raise GardeArret("monde : part de lisibilité nulle hors de [0, 1]")
        if self.sigma <= 0:
            raise GardeArret("monde : σ > 0")

    def enjeux_egaux(self) -> bool:
        return len({s for _, s in self.types_enjeu}) == 1


@dataclass(frozen=True)
class VeritePlantee:
    dommage: np.ndarray
    lisibilite: np.ndarray

    def empreinte(self) -> str:
        return empreinte_tableaux(dommage=self.dommage, lisibilite=self.lisibilite)

    def ecrire(self, chemin: str | Path) -> str:
        """Écrit la vérité dans un fichier à part (lu des seuls essais) ; rend son empreinte."""
        np.savez(chemin, dommage=self.dommage, lisibilite=self.lisibilite)
        return declarer_verite(self.empreinte(), str(chemin))


@dataclass
class Resultat:
    monde: Monde
    regle: RegleAudit
    oracle: OracleSimule
    tache: int
    journal: Journal
    verite: VeritePlantee
    uniformes: dict[str, np.ndarray]  # pour les rejeux appariés et les permutations des épreuves

    @property
    def n(self) -> int:
        return len(self.journal)


def score_gaussien_tronque(u: np.ndarray, moyenne: np.ndarray, sigma: float) -> np.ndarray:
    a = special.ndtr((0.0 - moyenne) / sigma)
    b = special.ndtr((1.0 - moyenne) / sigma)
    x = moyenne + sigma * special.ndtri(a + u * (b - a))
    return np.clip(x, 0.0, 1.0)


def _dommage(monde: Monde, uni: dict[str, np.ndarray]):
    parts = np.array([p for p, _ in monde.types_enjeu])
    enjeux = np.array([s for _, s in monde.types_enjeu])
    k = np.searchsorted(np.cumsum(parts), uni["enjeu"], side="right")
    k = np.minimum(k, len(parts) - 1)
    enjeu = enjeux[k]
    p0 = monde.part_lisibilite_nulle
    ul = uni["lisibilite"]
    if p0 >= 1:
        lis = np.zeros_like(ul)
    else:
        lis = np.where(ul < p0, 0.0, (ul - p0) / (1.0 - p0))
    dommage = uni["dommage"] < monde.politique(enjeu, lis)
    if monde.enjeu_ecrit_apres:
        enjeu = np.where(dommage, enjeux.max(), enjeu)  # artefact : enjeu écrit après l'épisode, d'après le dommage
    return enjeu, lis, dommage


def _morceau(monde: Monde, uni: dict[str, np.ndarray]):
    enjeu, lis, dommage = _dommage(monde, uni)
    if monde.loi_score[0] == "gaussienne_tronquee":
        moyenne = monde.mu0 + monde.mu1 * dommage * lis
        score = score_gaussien_tronque(uni["score"], moyenne, monde.sigma)
    elif monde.loi_score[0] == "signal":
        _, r, a = monde.loi_score
        score = (uni["score"] < np.where(dommage, r, a)).astype(float)
    else:
        raise GardeArret(f"monde : loi du score inconnue {monde.loi_score!r}")
    return enjeu, lis, dommage, score


def simuler(monde: Monde, regle: RegleAudit, oracle: OracleSimule, tache: int, n: int,
            arret_endommages: int | None = None, n_max: int | None = None, morceau: int = 10_000,
            transformer_uniformes: Callable[[dict[str, np.ndarray]], dict[str, np.ndarray]] | None = None,
            plancher_artefact: Callable[[np.ndarray], np.ndarray] | None = None, chaine: bool = True) -> Resultat:
    """Simule un monde de n épisodes, prolongé jusqu'à `arret_endommages` endommagés (au plus `n_max` épisodes).

    `transformer_uniformes` (rejeux appariés, permutations) agit sur les uniformes tirés, canal par canal, sans
    changer les autres canaux. `plancher_artefact` n'existe que pour les artefacts (plancher fonction du score)."""
    if abs(regle.s_bar - monde.s_bar) > 1e-12:
        raise GardeArret("s̄ de la règle différent de celui du monde")
    flux = Flux(monde.entropie, monde.identifiant, tache)
    n_max = n if n_max is None else n_max
    if arret_endommages is None:
        tailles = [n]
    else:
        tailles = None
    morceaux_uni: dict[str, list[np.ndarray]] = {c: [] for c in ("enjeu", "dommage", "score", "piece", "oracle", "lisibilite")}
    total, n_dom = 0, 0
    while True:
        t = n if tailles is not None else min(morceau, n_max - total)
        if t <= 0:
            break
        for c in morceaux_uni:
            morceaux_uni[c].append(flux.tirer(c, t))
        total += t
        if tailles is not None:
            break
        uni_m = {c: morceaux_uni[c][-1] for c in morceaux_uni}
        _, _, dm = _dommage(monde, uni_m)
        n_dom += int(dm.sum())
        if (total >= n and n_dom >= arret_endommages) or total >= n_max:
            break
    uni = {c: np.concatenate(v) for c, v in morceaux_uni.items()}
    if transformer_uniformes is not None:
        uni = transformer_uniformes({c: v.copy() for c, v in uni.items()})
    return _assembler(monde, regle, oracle, tache, uni, plancher_artefact, chaine)


def _assembler(monde, regle, oracle, tache, uni, plancher_artefact=None, chaine=True) -> Resultat:
    enjeu, lis, dommage, score = _morceau(monde, uni)
    g_force = dommage & monde.forcer_g_nul_endommages
    parts = regle.parts(enjeu, score, g_force=g_force)
    if plancher_artefact is not None:
        parts = dict(parts)
        parts["part_plancher"] = np.asarray(plancher_artefact(score), dtype=float)
        brut = parts["part_plancher"] + parts["part_enjeu"] + parts["part_soupcon"]
        parts["pi"] = np.minimum(1.0, brut)
        parts["ecrete"] = brut > 1
    audite, source = regle.tirer(parts, uni["piece"])
    N = len(enjeu)
    ep = np.arange(N)
    h = heures(ep)
    if monde.enjeu_ecrit_apres:
        h = dict(h)
        h["h_enjeu"] = PAS * ep + 3  # artefact : enjeu écrit après la fin, d'après le dommage
    j = Journal(etiquette=monde.etiquette or ("sans plancher : aucune borne" if regle.sans_plancher else ""),
                chaine=chaine)
    j.ajouter_episodes(episode=ep, enjeu=enjeu, h_enjeu=h["h_enjeu"], h_debut=h["h_debut"], h_fin=h["h_fin"],
                       score=score, g_force=g_force, h_score=h["h_score"], part_plancher=parts["part_plancher"],
                       part_enjeu=parts["part_enjeu"], part_soupcon=parts["part_soupcon"], pi=parts["pi"],
                       ecrete=parts["ecrete"], u_piece=uni["piece"], h_piece=h["h_piece"], audite=audite,
                       source=source)
    q_ep = oracle.couverture_par_episode(enjeu, lis) if hasattr(oracle, "couverture_par_episode") else None
    v_tous = oracle.verdicts(dommage, uni["oracle"], q_par_episode=q_ep)
    e_lect = oracle.episode_de_lecture(dommage)
    hv = heure_de_lecture(e_lect)
    sel = audite & (hv >= 0)
    ordre = np.lexsort((ep[sel], hv[sel]))
    j.ajouter_verdicts(episode=ep[sel][ordre], verdict=v_tous[sel][ordre], h_verdict=hv[sel][ordre])
    verite = VeritePlantee(dommage=dommage.copy(), lisibilite=lis.copy())
    return Resultat(monde, regle, oracle, tache, j, verite, uni)


def rang_premiere_prise(res: Resultat, rang_lu: int, sources: tuple[int, ...] = (1,)) -> int | None:
    """Rang (1, 2, …) parmi les endommagés de la première prise (audité, verdict « endommagé ») de l'une des
    `sources` ; None si aucune prise avant `rang_lu` ; refus nommé « trop peu d'endommagés » si le monde n'atteint pas
    `rang_lu` endommagés (jamais une prise ni une absence de prise). Lit la vérité plantée : réservé aux essais."""
    d = res.verite.dommage
    idx = np.flatnonzero(d)
    if len(idx) < rang_lu:
        raise GardeArret(f"{REFUS_TROP_PEU} : {len(idx)} endommagés pour un rang lu de {rang_lu}")
    idx = idx[:rang_lu]
    src = res.journal.colonne("source")[idx]
    v, _ = res.journal.verdicts_par_episode()
    prise = np.isin(src, sources) & (v[idx] == 1)
    k = np.flatnonzero(prise)
    return int(k[0]) + 1 if len(k) else None
