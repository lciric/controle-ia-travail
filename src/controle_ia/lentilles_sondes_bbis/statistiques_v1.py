"""Statistiques par direction, lentille et nul (texte scellé, « Métrique », points 6 à 8 ; « Seuil »).

Conventions fixées ici, sans choix d'analyse neuf : écart type de population (diviseur M) ; quantile 0,99 par interpolation
linéaire (défaut de `torch.quantile`) ; rang empirique d'un score = 1 + nombre de scores nuls du même jeton strictement plus
grands ; tout p vaut (1 + #{j : statistique(u_j) ≥ statistique(v)}) / (M + 1), la statistique de u_j étant calculée avec les
mêmes moyennes, écarts types et quantiles (u_j compris, écart déclaré par le texte). Les moyennes portent sur des directions,
jamais sur les jetons d'une action.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np
import torch

from . import constantes_v1 as K
from .constantes_v1 import Arret

_RE_NOMBRES = re.compile(K.MOTIF_NOMBRES)
_COUT = frozenset(K.FAMILLE_COUT)
LIBELLE_CONCENTREE = "concentrée au-delà des deux nuls"
LIBELLE_INTERMEDIAIRE = "intermédiaire"
LIBELLE_NON_DISTINCTE = "non distincte du nul"


# --- familles de jetons nommées d'avance ------------------------------------------------------------------------------------------
def famille_de(chaine: str) -> str | None:
    """« nombres » : la chaîne passée par `strip()` s'écrit `^[0-9]+$` ; « coût » : en minuscules, l'un des mots du texte."""
    s = chaine.strip()
    if _RE_NOMBRES.match(s) and "\n" not in s:
        return "nombres"
    if s.lower() in _COUT:
        return "cout"
    return None


def masques_familles(chaines: list[str]) -> dict[str, torch.Tensor]:
    f = [famille_de(c) for c in chaines]
    return {nom: torch.tensor([x == nom for x in f], dtype=torch.bool) for nom in ("nombres", "cout")}


# --- libellés (« Seuil ») -----------------------------------------------------------------------------------------------------------
def libelle(p_iso: float, p_signes: float) -> str:
    """« concentrée » : p ≤ 0,001 sous le nul isotrope et p ≤ 0,01 sous le nul des signes ; « non distincte » : p > 0,05 sous
    l'un des deux ; « intermédiaire » sinon. Même règle pour la part au-dessus du nul et la concentration des pôles."""
    if p_iso <= K.P_ISO_CONCENTREE and p_signes <= K.P_SIGNES_CONCENTREE:
        return LIBELLE_CONCENTREE
    if p_iso > K.P_NON_DISTINCTE or p_signes > K.P_NON_DISTINCTE:
        return LIBELLE_NON_DISTINCTE
    return LIBELLE_INTERMEDIAIRE


def sur_representee(p_iso: float, p_signes: float) -> bool:
    """Une famille est « sur-représentée » si p ≤ 0,01 sous les deux nuls."""
    return bool(p_iso <= K.P_FAMILLE and p_signes <= K.P_FAMILLE)


def p_empirique(statistiques_nulles, valeur: float) -> float:
    s = torch.as_tensor(statistiques_nulles)
    return float((1 + int((s >= valeur).sum())) / (s.numel() + 1))


# --- résumé d'un nul ------------------------------------------------------------------------------------------------------------------
@dataclass
class ResumeNul:
    moyenne: torch.Tensor          # [jetons]
    ecart_type: torch.Tensor       # [jetons]
    quantile: torch.Tensor         # [jetons], quantile 0,99 des M scores nuls du jeton
    concentration: torch.Tensor    # [M], C(u_j)
    part: torch.Tensor             # [M], P(u_j)
    familles: dict[str, torch.Tensor]   # nom → [M], compte dans les vingt premiers jetons de u_j
    k: int = K.K_JETONS            # nombre de premiers jetons de u_j employé pour la part et les familles

    @property
    def m(self) -> int:
        return int(self.concentration.numel())


def _quantile_par_jeton(scores_nuls: torch.Tensor, q: float, bloc: int = 2048) -> torch.Tensor:
    sortie = torch.empty(scores_nuls.shape[0], dtype=torch.float32)
    for s in range(0, scores_nuls.shape[0], bloc):
        sortie[s:s + bloc] = torch.quantile(scores_nuls[s:s + bloc], q, dim=1)
    return sortie


def resumer_nul(scores_nuls: torch.Tensor, masques: dict[str, torch.Tensor], k: int = K.K_JETONS) -> ResumeNul:
    """Résumé des scores `[jetons, M]` des M directions nulles (lues par le même code que v)."""
    if not bool(torch.isfinite(scores_nuls).all()):
        raise Arret("valeur non finie dans un nul : arrêt")
    moyenne = scores_nuls.mean(1)
    ecart = scores_nuls.std(1, correction=0)
    if not bool((ecart > 0).all()):
        raise Arret("écart type nul d'un jeton sous un nul : z non fini : arrêt")
    quantile = _quantile_par_jeton(scores_nuls, K.QUANTILE_PART)
    concentration = ((scores_nuls - moyenne[:, None]) / ecart[:, None]).max(0).values
    k = min(int(k), scores_nuls.shape[0])
    haut = scores_nuls.topk(k, dim=0)
    part = (haut.values > quantile[haut.indices]).float().mean(0)
    familles = {nom: m[haut.indices].sum(0).to(torch.int64) for nom, m in masques.items()}
    return ResumeNul(moyenne, ecart, quantile, concentration, part, familles, k)


def z_scores(a: torch.Tensor, resume: ResumeNul) -> torch.Tensor:
    z = (a - resume.moyenne) / resume.ecart_type
    if not bool(torch.isfinite(z).all()):
        raise Arret("valeur non finie dans une lecture : arrêt")
    return z


def concentrations_temoins(scores_temoins: torch.Tensor, resume: ResumeNul) -> torch.Tensor:
    """C de chaque témoin `[jetons, n]`, avec les moyennes et écarts types du nul."""
    return ((scores_temoins - resume.moyenne[:, None]) / resume.ecart_type[:, None]).max(0).values


def p_temoins(scores_temoins: torch.Tensor, resume: ResumeNul) -> np.ndarray:
    """p de concentration de chaque témoin contre les M directions nulles."""
    c = concentrations_temoins(scores_temoins, resume)
    nuls = torch.sort(resume.concentration).values
    au_moins = resume.m - torch.searchsorted(nuls, c, right=False)
    return ((1 + au_moins).double() / (resume.m + 1)).numpy()


# --- une direction à un signe ----------------------------------------------------------------------------------------------------------
def lecture_signe(a: torch.Tensor, nuls: dict[str, tuple[torch.Tensor, ResumeNul]], masques: dict[str, torch.Tensor],
                  ids_gardes: np.ndarray, k: int = K.K_JETONS) -> dict:
    """Tables d'une direction à un signe : `a` `[jetons]` est le score au signe voulu (−a pour le signe −) ; `nuls` : nom du
    nul → (scores nuls `[jetons, M]`, résumé). Les indices rendus sont des rangs parmi les jetons gardés ; `ids` donne les
    identifiants du tokeniseur."""
    if not bool(torch.isfinite(a).all()):
        raise Arret("valeur non finie dans une lecture : arrêt")
    k = min(int(k), a.numel())
    for nom_nul, (_, resume) in nuls.items():
        if resume.k != k or set(resume.familles) != set(masques):
            raise Arret(f"nul {nom_nul} résumé sur {resume.k} premiers jetons ou d'autres familles que la direction ({k})")
    haut = a.topk(k)
    rangs = haut.indices
    sortie = {"premiers_par_score": {"rangs_gardes": rangs.tolist(), "ids": [int(ids_gardes[i]) for i in rangs.tolist()],
                                    "scores": [float(x) for x in haut.values]},
              "nuls": {}, "familles": {nom: {"n": int(m[rangs].sum())} for nom, m in masques.items()}}
    for nom_nul, (scores_nuls, resume) in nuls.items():
        z = z_scores(a, resume)
        c = float(z.max())
        part = float((a[rangs] > resume.quantile[rangs]).float().mean())
        rang_empirique = (1 + (scores_nuls[rangs] > a[rangs][:, None]).sum(1)).tolist()
        t = {"z_des_premiers": [float(x) for x in z[rangs]], "rang_empirique_des_premiers": [int(x) for x in rang_empirique],
             "concentration": c, "p_concentration": p_empirique(resume.concentration, c),
             "part": part, "p_part": p_empirique(resume.part, part), "m": resume.m, "familles": {}}
        for nom, masque in masques.items():
            n = int(masque[rangs].sum())
            t["familles"][nom] = {"n": n, "attendu": float(resume.familles[nom].double().mean()),
                                  "p": p_empirique(resume.familles[nom], n)}
        if nom_nul in (K.NUL_ISOTROPE, K.NUL_ISOTROPE_PAR_DIRECTION):
            hz = z.topk(k)
            t["premiers_par_z"] = {"rangs_gardes": hz.indices.tolist(), "ids": [int(ids_gardes[i]) for i in hz.indices.tolist()],
                                   "z": [float(x) for x in hz.values]}
        sortie["nuls"][nom_nul] = t
    sortie["jeton_de_debut"] = jeton_de_debut(a, ids_gardes, rangs)
    return sortie


def jeton_de_debut(a: torch.Tensor, ids_gardes: np.ndarray, rangs_premiers: torch.Tensor) -> dict:
    """Présence du jeton de début (128 000) parmi les vingt premiers, et son rang par score (1 = premier ; égalités : 1 +
    nombre de jetons de score strictement plus grand). Rapporté sans libellé."""
    ou = np.flatnonzero(np.asarray(ids_gardes) == K.JETON_DE_DEBUT)
    if ou.size == 0:
        return {"garde": False, "parmi_les_premiers": False, "rang": None}
    i = int(ou[0])
    return {"garde": True, "parmi_les_premiers": bool(i in set(rangs_premiers.tolist())), "rang": int((a > a[i]).sum()) + 1}


# --- pôles alignés (point 7) -----------------------------------------------------------------------------------------------------------
def cosinus_colonnes(v: torch.Tensor, w_down: torch.Tensor, normes: torch.Tensor | None = None) -> torch.Tensor:
    """Cosinus de chaque colonne de `v` `[largeur, n]` avec chaque colonne de `W_down` `[largeur, neurones]` : `[neurones, n]`.
    Le pôle (neurone, +) a ce cosinus, le pôle (neurone, −) son opposé."""
    v = v[:, None] if v.ndim == 1 else v
    normes = w_down.norm(dim=0) if normes is None else normes
    nv = v.norm(dim=0)
    if not bool((nv > 0).all()) or not bool((normes > 0).all()):
        raise Arret("norme nulle dans le calcul des pôles alignés")
    return (w_down.T @ v) / (normes[:, None] * nv[None, :])


def poles_alignes(v: torch.Tensor, w_down: torch.Tensor, nuls: dict[str, torch.Tensor], k: int = K.K_POLES) -> dict:
    """Les dix pôles de plus grand cosinus avec v (signe +), le rang de chacun parmi les maxima nuls, la concentration des
    pôles (cosinus maximal) et son p sous chaque nul (`nuls` : nom → directions nulles `[largeur, M]`)."""
    normes = w_down.norm(dim=0)
    cos = cosinus_colonnes(v, w_down, normes)[:, 0]
    signes = torch.cat([cos, -cos])                       # pôles (n, +) puis (n, −)
    haut = signes.topk(min(int(k), signes.numel()))
    f = cos.numel()
    maxima = {nom: cosinus_colonnes(u, w_down, normes).abs().max(0).values for nom, u in nuls.items()}
    if not bool(torch.isfinite(cos).all()) or not all(bool(torch.isfinite(m).all()) for m in maxima.values()):
        raise Arret("valeur non finie dans les pôles alignés : arrêt")
    poles = [{"neurone": int(i % f), "signe": "+" if int(i) < f else "-", "cosinus": float(c),
              "rang_parmi_maxima_nuls": {nom: int((m > c).sum()) + 1 for nom, m in maxima.items()}}
             for c, i in zip(haut.values, haut.indices)]
    c_max = float(cos.abs().max())
    return {"poles": poles, "concentration": c_max, "p": {nom: p_empirique(m, c_max) for nom, m in maxima.items()},
            "maxima_nuls": {nom: m for nom, m in maxima.items()}}


def poles_opposes(poles: list[dict]) -> list[dict]:
    """Le signe − rend les mêmes pôles, de signe opposé."""
    return [{**p, "signe": "-" if p["signe"] == "+" else "+"} for p in poles]


# --- comparaisons appariées (point 8) ----------------------------------------------------------------------------------------------------
def cosinus(v1: np.ndarray, v2: np.ndarray) -> float:
    a, b = np.asarray(v1, np.float64), np.asarray(v2, np.float64)
    na, nb = float(np.linalg.norm(a)), float(np.linalg.norm(b))
    if na == 0 or nb == 0 or not (np.isfinite(na) and np.isfinite(nb)):
        raise Arret("cosinus : norme nulle ou non finie")
    return float(a @ b / (na * nb))


def jetons_communs(ids1, ids2) -> int:
    return len(set(int(i) for i in ids1) & set(int(i) for i in ids2))


def vecteur_calculable(v: np.ndarray) -> str | None:
    """Norme nulle ou valeur non finie : « non calculable » (motif rendu) ; sinon `None`."""
    v = np.asarray(v)
    if not np.all(np.isfinite(v)):
        return "valeur non finie dans la direction"
    if float(np.linalg.norm(v.astype(np.float64))) == 0.0:
        return "norme nulle"
    return None
