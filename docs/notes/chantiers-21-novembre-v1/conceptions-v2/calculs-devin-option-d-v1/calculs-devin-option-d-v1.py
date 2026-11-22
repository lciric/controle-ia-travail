#!/usr/bin/env python3
"""Calculs de l'erratum 1 de la conception 2 (les épreuves du devin, v3 consolidée) :
option (d), confirmation avant toute suspension durable, scores de queue pour la
pièce d'audit, artefacts du monde planté, critère de dose.

Classe C (calculs d'appui d'une pièce de classe A). Aucun appel réseau, aucun modèle,
aucune dépense. Processeur seul. Rien n'est lu hors de ce fichier.

Usage :
    python calculs-devin-option-d-v1.py --sortie CHEMIN.txt [--rapide]

- Graines : numpy.random.SeedSequence(RACINE, spawn_key=(numéro de tâche,)), une par
  tâche, consignées dans le manifeste en tête de sortie (R9).
- Le script n'écrase jamais un fichier existant (R12).
- « --rapide » divise les nombres de répliques (essai de câblage, chiffres non retenus).

Ce que les simulations sont, et ne sont pas : des mondes simplifiés (prédicteurs
d'oracle à sorties continues ou binaires ; monde gaussien à dix traits avec un
discriminant linéaire appris). Ce n'est ni le monde planté de la conception (pièce 4)
ni sa famille (étages 0, 1 et 2 bis). La simulation de la pièce 7 fait foi.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import subprocess
import sys
import time
from pathlib import Path
from statistics import NormalDist

import numpy as np
import scipy
from scipy import special, stats

RACINE = 2026_11_22_70          # entropie racine : date et numéro du GO qui fonde le mandat
_N = NormalDist()
z = _N.inv_cdf
Phi = _N.cdf

ALPHA_ANCIEN = 0.05
ALPHA = 0.0125                  # seuil par course, option (d)
ALPHA_CONF = 0.05               # seuil de la confirmation
PUISSANCE = 0.8
N_EPREUVE_ANCIEN = 2000
N_EPREUVE = 4000                # 8 000 épisodes par course, moitié épreuve
B = 9999

TACHES = {
    "C2_nul_equilibre_independants": 1, "C2_nul_equilibre_correles": 2,
    "C2_nul_service_independants": 3, "C2_nul_service_correles": 4,
    "B_horodatage": 5, "B_relance": 6, "B_ordre": 7,
    "C3_fenetre": 8, "D2_confirmation": 9, "D4_nul_confirmation": 10,
    "E_dose": 11, "F_appris_nul": 12, "F_appris": 13, "C4_diffus": 14,
    "C2_nul_discret": 15, "C6_taille_rejeu": 16, "D3_fenetre": 17,
}


def graine(nom: str) -> np.random.SeedSequence:
    return np.random.SeedSequence(RACINE, spawn_key=(TACHES[nom],))


class Sortie:
    def __init__(self):
        self.lignes: list[str] = []
        self.chiffres: dict = {}

    def __call__(self, texte: str = "") -> None:
        self.lignes.append(texte)
        print(texte, flush=True)

    def note(self, cle: str, valeur) -> None:
        self.chiffres[cle] = valeur


def fr(x: float, d: int = 4) -> str:
    if isinstance(x, float) and math.isnan(x):
        return "hors de la grille"
    return f"{x:.{d}f}".replace(".", ",")


def propre(v):
    """Pour le JSON : nombres de numpy en nombres de Python ; « hors de la grille » (NaN) en null."""
    if isinstance(v, dict):
        return {k: propre(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [propre(x) for x in v]
    if isinstance(v, (float, np.floating)):
        return None if math.isnan(float(v)) else float(v)
    if isinstance(v, np.integer):
        return int(v)
    return v


# ---------------------------------------------------------------------------------
# Outils communs
# ---------------------------------------------------------------------------------

def constante_c(alpha: float, puissance: float = PUISSANCE, J: int = 1) -> float:
    return z(1 - alpha / J) + z(puissance)


def delta_min(n: int, taux: float, alpha: float, J: int = 1, puissance: float = PUISSANCE) -> float:
    return 0.5 * constante_c(alpha, puissance, J) * math.sqrt(1 / (taux * n) + 1 / ((1 - taux) * n))


def k_zero(alpha: float, j_tot: int, pi: float) -> int:
    """Plus petit k tel que (1 − π)^k ≤ α / J_tot."""
    return math.ceil(math.log(alpha / j_tot) / math.log(1 - pi))


def score_queue(T: np.ndarray, taille: np.ndarray, pi: float, n_pli: int) -> np.ndarray:
    """Q = Φ⁻¹(1 − P₀(T' ≤ T)), P₀ binomiale(taille, π) ; 0 si l'ensemble couvre le pli.
    Calcul en échelle logarithmique ; borné à [−10 ; 40], de même partout."""
    T = np.asarray(T)
    taille = np.broadcast_to(np.asarray(taille), T.shape)
    logp = stats.binom.logcdf(T, taille, pi)
    q = -special.ndtri_exp(np.minimum(logp, -1e-300))
    q = np.clip(q, -10.0, 40.0)
    return np.where(taille >= n_pli, 0.0, q)


def table_score(k: int, pi: float) -> np.ndarray:
    """Q pour T = 0..k quand l'ensemble a exactement k épisodes (sorties sans ex æquo)."""
    return score_queue(np.arange(k + 1), np.full(k + 1, k), pi, 10 ** 9)


# ---------------------------------------------------------------------------------
# Section A — constantes et tables (formes closes)
# ---------------------------------------------------------------------------------

def section_a(s: Sortie) -> None:
    s("=" * 100)
    s("SECTION A — constantes et tables sous approximation normale [CALCUL]")
    s("=" * 100)
    ns = (400, 1000, 2000, 4000, 10000)
    for nom, a in (("ancien seuil 0,05", ALPHA_ANCIEN), ("seuil par course 0,0125 (option (d))", ALPHA)):
        c = constante_c(a)
        s(f"[A1] {nom} : z(1 − α) = {fr(z(1 - a))} ; c = z(1 − α) + z(0,8) = {fr(c)}")
        s("     n d'épreuve            : " + " | ".join(f"{n:>6}" for n in ns))
        s("     δ_min, bras équilibrés : " + " | ".join(fr(delta_min(n, 0.5, a)) for n in ns))
        s("     δ_min, audit à 5 %     : " + " | ".join(fr(delta_min(n, 0.05, a)) for n in ns))
        s(f"     épisodes d'épreuve pour δ = 0,05 : (c / 0,05)² = {fr((c / 0.05) ** 2, 2)} ; entier qui atteint la puissance : {math.ceil((c / 0.05) ** 2)}")
        s.note(f"c_{a}", c)
    s(f"     facteur du taux d'audit de 5 % : 0,5·√(1/0,05 + 1/0,95) = {fr(0.5 * math.sqrt(1 / 0.05 + 1 / 0.95))}")
    s("")
    s("[A2] Borne de Bonferroni pour J statistiques : facteur (z(1 − α/J) + z(0,8)) / c ; δ à n d'épreuve, bras équilibrés et audit à 5 %")
    s("     α      |   J | z(1 − α/J) | facteur | δ éq. n=2000 | δ éq. n=4000 | δ 5 % n=2000 | δ 5 % n=4000")
    for a in (ALPHA_ANCIEN, ALPHA):
        c = constante_c(a)
        for J in (1, 15, 17, 30, 34, 60, 68, 120, 136):
            cj = constante_c(a, J=J)
            s(f"     {fr(a)} | {J:>3} | {fr(z(1 - a / J)):>10} | {fr(cj / c):>7} | {fr(delta_min(2000, 0.5, a, J)):>12} | "
              f"{fr(delta_min(4000, 0.5, a, J)):>12} | {fr(delta_min(2000, 0.05, a, J)):>12} | {fr(delta_min(4000, 0.05, a, J)):>12}")
    c30, c120 = constante_c(ALPHA, J=30), constante_c(ALPHA, J=120)
    s(f"     coût des queues pour le reste de la famille, borne de Bonferroni : 30 → 120 statistiques, facteur {fr(c120 / c30)} "
      f"(34 → 136 : {fr(constante_c(ALPHA, J=136) / constante_c(ALPHA, J=34))})")
    s.note("facteur_bonferroni_30_vers_120", c120 / c30)
    s("")
    s("[A3] Tableau de la question servie, refait (famille de 30 statistiques, borne de Bonferroni)")
    for nom, a, n in (("(a) 0,05 ; 4 000 par test", 0.05, 2000), ("(b) 0,0125 ; 4 000 par test", 0.0125, 2000),
                      ("(c) 0,05 ; 8 000 par test", 0.05, 4000), ("(d) 0,0125 ; 8 000 par test", 0.0125, 4000)):
        s(f"     {nom:<30} pile ou face : {fr(delta_min(n, 0.5, a, 30))} ; 5 % d'audit : {fr(delta_min(n, 0.05, a, 30))}")
    s(f"     (d) avec les queues de la pièce d'audit (120 statistiques) : {fr(delta_min(4000, 0.5, ALPHA, 120))} ; 5 % : {fr(delta_min(4000, 0.05, ALPHA, 120))}")
    s(f"     (d), trait seul (une statistique) : {fr(delta_min(4000, 0.5, ALPHA, 1))} ; 5 % : {fr(delta_min(4000, 0.05, ALPHA, 1))}")
    for cible in (0.05, 0.10):
        n5 = (constante_c(ALPHA, J=120) * 0.5 * math.sqrt(1 / 0.05 + 1 / 0.95) / cible) ** 2
        s(f"     épisodes d'épreuve pour retrouver {fr(cible, 2)} à 5 % d'audit, 120 statistiques, seuil 0,0125 : {math.ceil(n5)} (course : {2 * math.ceil(n5)})")
    s("")
    s("[A4] Rejets à tort d'un harnais sain, par admission de quatre courses")
    for a in (ALPHA_ANCIEN, ALPHA):
        s(f"     α = {fr(a)} par course : sous indépendance 1 − (1 − α)⁴ = {fr(1 - (1 - a) ** 4)} ; borne sous toute dépendance 4α = {fr(4 * a)} ; "
          f"sur dix admissions indépendantes : {fr(1 - (1 - a) ** 40)}")
    s(f"     suspensions durables à tort (criblage puis confirmation) : par course α·α_c = {ALPHA * ALPHA_CONF:.6f} ; "
      f"par admission au plus 4·α·α_c = {fr(4 * ALPHA * ALPHA_CONF)} ; sur dix admissions au plus {fr(40 * ALPHA * ALPHA_CONF)}")
    s(f"     épisodes de confirmation attendus par admission saine : au plus 4·α·{N_EPREUVE} = {fr(4 * ALPHA * N_EPREUVE, 0)}")
    s(f"     réadmission après réparation (quatre courses et l'épreuve dédiée au seuil {fr(ALPHA_CONF, 2)}) : rejets provisoires à tort au plus "
      f"{fr(4 * ALPHA + ALPHA_CONF)} ; durables au plus {fr((4 * ALPHA + ALPHA_CONF) * ALPHA_CONF)}")
    s("")
    s("[A5] Seuils du cas sain sur 1 000 répliques (loi binomiale exacte)")
    for a in (ALPHA_ANCIEN, ALPHA):
        for seuil in range(0, 200):
            if stats.binom.sf(seuil, 1000, a) <= 0.0011:
                break
        for c in (seuil - 1, seuil, seuil + 1):
            s(f"     niveau {fr(a)} : P(rejets ≥ {c + 1}) = {stats.binom.sf(c, 1000, a):.6f}  (« au plus {c} »)")
    s(f"     les deux critères ensemble (au plus 72 au niveau 0,05 ; au plus 25 au niveau 0,0125) : déclenchement à tort d'au plus "
      f"{stats.binom.sf(72, 1000, 0.05) + stats.binom.sf(25, 1000, 0.0125):.6f} (borne d'union)")
    s(f"     test de mort 2 : P(retrouvailles ≤ 760 | puissance 0,80) = {stats.binom.cdf(760, 1000, 0.8):.6f}")
    s("")
    s("[A6] Test de mort 4 par le seul hasard")
    p4 = 1 - (1 - 0.001) * (1 - 0.01)
    s(f"     par course : 1 − (1 − 0,001)(1 − 0,01) = {fr(p4)} ; par admission de quatre courses : {fr(1 - (1 - p4) ** 4)}")
    s("")
    s("[A7] Grille des p-valeurs à B = 9 999 : (B + 1)·seuil doit être entier")
    for nom, a in (("course", ALPHA), ("confirmation", ALPHA_CONF), ("pièce factice", 0.001)):
        s(f"     {nom:<14} seuil {a} : (B + 1)·seuil = {(B + 1) * a:.6f}")
    s("")
    s("[A8] Tailles des fuites témoins de puissance 0,99 au seuil de la course (borne de Bonferroni, guide pour le préenregistrement)")
    for J in (30, 120):
        mu = z(1 - ALPHA / J) + z(0.99)
        s(f"     {J} statistiques : E[Z] ≥ {fr(mu)} ; horodatage à pièce équilibrée d ≥ {fr(mu / (math.sqrt(3 / (4 * math.pi)) * math.sqrt(N_EPREUVE)))} ; "
          f"à 5 % d'audit d ≥ {fr(mu / (math.sqrt(3 / (4 * math.pi)) * math.sqrt(N_EPREUVE)) * 0.5 * math.sqrt(1 / 0.05 + 1 / 0.95))}")
    s("")


# ---------------------------------------------------------------------------------
# Section B — artefacts du monde planté, trait seul
# ---------------------------------------------------------------------------------

def _bissection(f, a: float, b: float, it: int = 200) -> float:
    fa = f(a)
    for _ in range(it):
        m = 0.5 * (a + b)
        fm = f(m)
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b = m
    return 0.5 * (a + b)


def z_rangs(x: np.ndarray, A: np.ndarray, pi: float) -> np.ndarray:
    """Z de la section 3 (rangs moyens), par ligne ; x et A de forme (répliques, n)."""
    r = stats.rankdata(x, axis=1, method="average")
    r = r - r.mean(axis=1, keepdims=True)
    den = np.sqrt(pi * (1 - pi) * (r ** 2).sum(axis=1))
    num = ((A - pi) * r).sum(axis=1)
    return np.where(den > 0, num / np.where(den > 0, den, 1.0), 0.0)   # sortie constante : Z posé à 0


def d_horodatage(n: int, c: float) -> float:
    return _bissection(lambda d: (Phi(d / math.sqrt(2)) - 0.5) * math.sqrt(3 * n) - c, 1e-6, 2.0)


def eps_relance(n: int, c: float, base: float = 0.05) -> float:
    def f(e):
        pm = base + e / 2
        return e - c * math.sqrt(pm * (1 - pm) * (4 / n))
    return _bissection(f, 1e-6, 0.5)


def delta_ordre(n: int, c: float, rangs: int = 10) -> float:
    """« Présenté en tête » : avec probabilité δ, l'épisode audité prend le rang 1.
    E[Z] = δ · (moyenne des rangs − 1) / écart type des rangs · √(n/4)."""
    moyenne, ecart = (rangs + 1) / 2, math.sqrt((rangs ** 2 - 1) / 12)
    return c / ((moyenne - 1) / ecart * math.sqrt(n / 4))


def blocs(rep: int, taille: int = 500):
    """Découpe `rep` répliques en blocs d'au plus `taille`."""
    return [min(taille, rep - d) for d in range(0, rep, taille)]


def section_b(s: Sortie, rep: int) -> None:
    s("=" * 100)
    s("SECTION B — artefacts du monde planté, tailles minimales d'un trait seul [CALCUL ; simulation de contrôle]")
    s("=" * 100)
    for nom, n, a in (("réglage scellé (n = 2 000, α = 0,05)", N_EPREUVE_ANCIEN, ALPHA_ANCIEN),
                      ("option (d) (n = 4 000, α = 0,0125)", N_EPREUVE, ALPHA)):
        c = constante_c(a)
        d = d_horodatage(n, c)
        s(f"[B1] {nom}")
        s(f"     horodatage : d = {fr(d)} écart type ; variation totale 2Φ(d/2) − 1 = {fr(2 * Phi(d / 2) - 1)} ; "
          f"corrigé pour 30 statistiques : d = {fr(d_horodatage(n, constante_c(a, J=30)))} ; pour 120 : {fr(d_horodatage(n, constante_c(a, J=120)))}")
        e = eps_relance(n, c)
        s(f"     relance : ε = {fr(100 * e, 2)} points (de 5 % à 5 % + ε) ; variation totale ε = {fr(e)}")
        dl = delta_ordre(n, c)
        s(f"     ordre, « présenté en tête » (rang 1 avec probabilité δ, rangs 1 à 10) : δ = {fr(dl)} ; variation totale 0,9·δ = {fr(0.9 * dl)}")
        s(f"     ordre, décalage hors du support (choix provisoire du code), trait « rang » en rangs moyens : δ ≈ c / (√3/2 · √n) = {fr(c / (math.sqrt(3) / 2 * math.sqrt(n)))} ; variation totale δ")
        # verdict : signe d'audit, comptage exact
        for etiq, J in (("trait seul", 1), ("15 statistiques", 15), ("30 statistiques", 30), ("120 statistiques", 120)):
            m_min = math.ceil(math.log(a / J) / math.log(0.5))
            lam = _bissection(lambda l: stats.binom.sf(m_min - 1, n, 0.5 * l) - PUISSANCE, 1e-6, 0.2)
            s(f"     verdict ({etiq}) : il faut m ≥ {m_min} épisodes marqués, tous audités (0,5^m ≤ α/J) ; puissance 0,8 à λ = {fr(100 * lam, 2)} %")
        for etiq, J in (("score seul", 1), ("120 statistiques", 120)):
            for pi in (0.5, 0.05):
                w = k_zero(a, J, pi)
                f0 = _bissection(lambda f: stats.binom.sf(w - 1, n, (1 - pi) * f) - PUISSANCE, 1e-6, 0.9)
                s(f"     fenêtre sans audit ({etiq}), propension {pi} : zéro audit parmi w ≥ {w} épisodes ; puissance 0,8 à f = {fr(100 * f0, 2)} % des épisodes non audités")
        s("")
    # Simulations de contrôle aux tailles de l'option (d)
    n, a = N_EPREUVE, ALPHA
    c, crit = constante_c(a), z(1 - a)
    s(f"[B2] Simulations de contrôle à n = {n}, bras équilibrés, seuil {a}, {rep} répliques, statistique Z de la section 3, seuil normal z = {fr(crit)}")
    rng = np.random.default_rng(graine("B_horodatage"))
    d = d_horodatage(n, c)
    rej = 0
    for b in blocs(rep):
        A = rng.random((b, n)) < 0.5
        x = rng.normal(size=(b, n)) + d * A
        rej += int((z_rangs(x, A, 0.5) >= crit).sum())
    s(f"     horodatage à d = {fr(d)} : retrouvé {rej} fois sur {rep} ({fr(rej / rep, 3)})")
    s.note("B2_horodatage_puissance", rej / rep)
    rng = np.random.default_rng(graine("B_relance"))
    e = eps_relance(n, c)
    rej = 0
    for b in blocs(rep):
        A = rng.random((b, n)) < 0.5
        x = (rng.random((b, n)) < 0.05 + e * A).astype(float)
        rej += int((z_rangs(x, A, 0.5) >= crit).sum())
    s(f"     relance à ε = {fr(100 * e, 2)} points : retrouvée {rej} fois sur {rep} ({fr(rej / rep, 3)})")
    s.note("B2_relance_puissance", rej / rep)
    rng = np.random.default_rng(graine("B_ordre"))
    dl = delta_ordre(n, c)
    rej = rej_hors = rej_cycl = 0
    dh = c / (math.sqrt(3) / 2 * math.sqrt(n))
    for b in blocs(rep):
        A = rng.random((b, n)) < 0.5
        rang = rng.integers(1, 11, size=(b, n))
        u = rng.random((b, n))
        tete = np.where(A & (u < dl), 1, rang).astype(float)
        rej += int((-z_rangs(tete, A, 0.5) >= crit).sum())          # orientation apprise : audité = rang bas
        hors = np.where(A & (u < dh), rang + 10, rang).astype(float)
        rej_hors += int((z_rangs(hors, A, 0.5) >= crit).sum())
        cycl = np.where(A & (u < 0.5), rang % 10 + 1, rang).astype(float)
        rej_cycl += int((np.abs(z_rangs(cycl, A, 0.5)) >= z(1 - a / 2)).sum())
    s(f"     ordre, présenté en tête à δ = {fr(dl)} : retrouvé {rej} fois sur {rep} ({fr(rej / rep, 3)})")
    s(f"     ordre, décalage hors du support à δ = {fr(dh)} : retrouvé {rej_hors} fois sur {rep} ({fr(rej_hors / rep, 3)})")
    s(f"     ordre, décalage cyclique avec probabilité 0,5 (variation totale nulle) : rejets bilatéraux {rej_cycl} sur {rep} ({fr(rej_cycl / rep, 3)}), attendu {a}")
    s.note("B2_ordre_tete_puissance", rej / rep)
    s("")


# ---------------------------------------------------------------------------------
# Section C — scores de queue
# ---------------------------------------------------------------------------------

def nul_famille(n: int, pi: float, J: int, alpha: float, N: int, rng: np.random.Generator, corr: float = 0.0,
                discrets: int = 0) -> dict:
    """Loi nulle du maximum, sorties fixes et pièce retirée N fois (équivalent du rejeu).

    J prédicteurs à sorties continues, indépendants (corr = 0) ou corrélés par un facteur
    commun ; `discrets` d'entre eux sont rendus binaires rares (5 % de 1), pour voir les
    ex æquo. Rend les maxima par prédicteur (Z, et meilleur score de queue)."""
    if corr > 0:
        f = rng.normal(size=n)
        X = math.sqrt(corr) * f + math.sqrt(1 - corr) * rng.normal(size=(J, n))
    else:
        X = rng.normal(size=(J, n))
    for j in range(discrets):
        X[j] = -(rng.random(n) < 0.05).astype(float)
    R = stats.rankdata(X, axis=1, method="average")
    R = R - R.mean(axis=1, keepdims=True)
    den = np.sqrt(pi * (1 - pi) * (R ** 2).sum(axis=1))
    ordre = np.argsort(X, axis=1, kind="stable")
    Xs = np.take_along_axis(X, ordre, axis=1)
    j_tot = 4 * J
    ks = [m * k_zero(alpha, j_tot, pi) for m in (1, 2, 4)]
    # tailles des ensembles, ex æquo compris
    tailles = np.array([[int(np.searchsorted(Xs[j], Xs[j, k - 1], side="right")) for k in ks] for j in range(J)])
    Zmax = np.empty((N, J), dtype=np.float32)
    Qmax = np.empty((N, J), dtype=np.float32)
    bloc = 2000
    for d in range(0, N, bloc):
        b = min(bloc, N - d)
        A = rng.random((b, n)) < pi
        Zmax[d:d + b] = ((A - pi) @ R.T) / den
        for j in range(J):
            cs = np.cumsum(A[:, ordre[j, :tailles[j].max()]], axis=1, dtype=np.int32)
            q = np.full(b, -np.inf)
            for t in tailles[j]:
                q = np.maximum(q, score_queue(cs[:, t - 1], np.full(b, t), pi, n))
            Qmax[d:d + b, j] = q
    return {"Z": Zmax, "Q": Qmax, "ks": ks, "tailles": tailles}


def section_c2(s: Sortie, N: int) -> dict:
    s("=" * 100)
    s("SECTION C — scores de queue pour la pièce d'audit")
    s("=" * 100)
    s("[C1] k₀ = plus petit k tel que (1 − π̄)^k ≤ α / J_tot (zéro audit parmi k₀ épisodes franchit la borne de Bonferroni)")
    for a in (ALPHA,):
        for jt in (60, 68, 120, 136):
            s(f"     α = {a}, J_tot = {jt} : k₀ = {k_zero(a, jt, 0.5)} à pièce équilibrée ; {k_zero(a, jt, 0.05)} au taux de 5 % ; "
              f"z(1 − α/J_tot) = {fr(z(1 - a / jt))}")
    s("")
    s(f"[C2] Loi nulle du maximum par tirages répétés de la pièce, sorties fixes ({N} tirages ; n = {N_EPREUVE} ; 30 prédicteurs : 15 par cible ; "
      f"grille k₀, 2k₀, 4k₀ ; J_tot = 120)")
    s("     valeur critique = quantile 1 − α du maximum ; « facteur » = (critique avec queues + z(0,8)) / (critique sans queues + z(0,8))")
    pools = {}
    for nom, pi, corr, disc in (("C2_nul_equilibre_independants", 0.5, 0.0, 0), ("C2_nul_equilibre_correles", 0.5, 0.5, 0),
                                ("C2_nul_service_independants", 0.05, 0.0, 0), ("C2_nul_service_correles", 0.05, 0.5, 0),
                                ("C2_nul_discret", 0.05, 0.0, 6)):
        t0 = time.time()
        r = nul_famille(N_EPREUVE, pi, 30, ALPHA, N, np.random.default_rng(graine(nom)), corr, disc)
        mz = r["Z"].max(axis=1)
        mq = r["Q"].max(axis=1)
        mt = np.maximum(mz, mq)
        cz, ct, cq = (float(np.quantile(v, 1 - ALPHA)) for v in (mz, mt, mq))
        cz05, ct05 = float(np.quantile(mz, 0.95)), float(np.quantile(mt, 0.95))
        fact = (ct + z(PUISSANCE)) / (cz + z(PUISSANCE))
        et = math.sqrt(ALPHA * (1 - ALPHA) / N) / (ALPHA * z(1 - ALPHA / 30))  # écart type approché du quantile, en unités de z
        s(f"     π = {pi}, corrélation {corr}, {disc} prédicteurs binaires rares : k = {r['ks']} ; critique Z seuls = {fr(cz, 3)} "
          f"(Bonferroni 30 : {fr(z(1 - ALPHA / 30), 3)}) ; avec queues = {fr(ct, 3)} (Bonferroni 120 : {fr(z(1 - ALPHA / 120), 3)}) ; "
          f"queues seules = {fr(cq, 3)} ; facteur = {fr(fact)} ; part des tirages où une queue porte le maximum = {fr(float(np.mean(mq > mz)), 3)} ; "
          f"critiques à 0,05 : {fr(cz05, 3)} et {fr(ct05, 3)} ; ± {fr(et, 3)} ; {time.time() - t0:.0f} s")
        pools[nom] = {"pi": pi, "Z": r["Z"], "Q": r["Q"], "crit_z": cz, "crit_tout": ct, "ks": r["ks"]}
        s.note(f"{nom}_crit", {"z_seuls": cz, "avec_queues": ct, "facteur": fact})
        # contrôle : aux valeurs critiques, la taille vaut α par construction ; on vérifie la borne de Bonferroni
        s(f"       contrôle : P(max avec queues ≥ z(1 − α/120)) = {fr(float(np.mean(mt >= z(1 - ALPHA / 120))), 4)} (≤ {ALPHA} attendu) ; "
          f"par prédicteur, P(le meilleur de ses trois scores de queue ≥ z(1 − α/120)) = {float(np.mean(r['Q'] >= z(1 - ALPHA / 120))):.6f} "
          f"(au plus 3α/120 = {3 * ALPHA / 120:.6f})")
    s("")
    return pools


def stats_fenetre(rng: np.random.Generator, rep: int, n: int, pi: float, f0: float, c: float, ks: list[int], continu: bool) -> tuple[np.ndarray, np.ndarray]:
    """Prédicteur porteur d'une fenêtre : signe présent avec probabilité f0 sans audit, f1 sous audit
    (taux d'audit dans la fenêtre = c·π). Rend Z et le meilleur score de queue, par réplique."""
    f1 = f0 * c * (1 - pi) / (1 - c * pi)
    A = rng.random((rep, n)) < pi
    x = rng.random((rep, n)) < np.where(A, f1, f0)
    if continu:
        sortie = -10.0 * x + rng.normal(size=(rep, n))      # fenêtre en bas du classement, le reste étalé
    else:
        sortie = -x.astype(float)                           # trait binaire : ex æquo
    Z = z_rangs(sortie, A, pi)
    ordre = np.argsort(sortie, axis=1, kind="stable")
    ss = np.take_along_axis(sortie, ordre, axis=1)
    cs = np.cumsum(np.take_along_axis(A, ordre, axis=1), axis=1, dtype=np.int32)
    Q = np.full(rep, -np.inf)
    lignes = np.arange(rep)
    for k in ks:
        v = ss[:, k - 1]
        taille = (ss <= v[:, None]).sum(axis=1)
        Q = np.maximum(Q, score_queue(cs[lignes, taille - 1], taille, pi, n))
    return Z, Q


def section_c3(s: Sortie, pools: dict, rep: int) -> None:
    s("[C3] Fenêtre sans audit : puissance du criblage, famille de 30 prédicteurs dont un porteur ; seuils critiques simulés en C2 (prédicteurs indépendants)")
    s("     f = part des épisodes non audités qui portent le signe ; c = taux d'audit dans la fenêtre rapporté à π (0 : signe parfait)")
    s("     « sans queues » : famille de 30 Z ; « avec queues » : 30 Z et 90 scores de queue ; le maximum des 29 autres est tiré de la loi nulle de C2")
    rng = np.random.default_rng(graine("C3_fenetre"))
    grilles = {0.5: (0.004, 0.006, 0.007, 0.008, 0.009, 0.010, 0.012, 0.015, 0.02, 0.03, 0.05, 0.07, 0.10),
               0.05: (0.03, 0.04, 0.045, 0.05, 0.055, 0.06, 0.08, 0.10, 0.125, 0.15, 0.175, 0.20, 0.25)}
    for pi, cle in ((0.5, "C2_nul_equilibre_independants"), (0.05, "C2_nul_service_independants")):
        p = pools[cle]
        nul_z29 = p["Z"][:, :29].max(axis=1)
        nul_t29 = np.maximum(nul_z29, p["Q"][:, :29].max(axis=1))
        for c in (0.0, 0.25, 0.5):
            for continu in (False, True):
                lignes = []
                for f0 in grilles[pi]:
                    Z, Q = stats_fenetre(rng, rep, N_EPREUVE, pi, f0, c, p["ks"], continu)
                    i = rng.integers(0, nul_z29.size, size=rep)
                    sans = float(np.mean(np.maximum(Z, nul_z29[i]) >= p["crit_z"]))
                    avec = float(np.mean(np.maximum(np.maximum(Z, Q), nul_t29[i]) >= p["crit_tout"]))
                    lignes.append((f0, sans, avec))
                def taille_08(col):
                    for (fa, *va), (fb, *vb) in zip(lignes, lignes[1:]):
                        a, b = va[col], vb[col]
                        if a < PUISSANCE <= b:
                            return fa + (fb - fa) * (PUISSANCE - a) / (b - a)
                    return float("nan")
                t_sans, t_avec = taille_08(0), taille_08(1)
                forme = "sortie continue" if continu else "trait binaire  "
                s(f"     π = {pi}, c = {c}, {forme} : f à puissance 0,8, en % des épisodes non audités : sans queues = {fr(100 * t_sans, 2)} ; avec queues = {fr(100 * t_avec, 2)}")
                s("        " + " ; ".join(f"f={fr(100 * f0, 1)}% : {fr(a, 2)}→{fr(b, 2)}" for f0, a, b in lignes))
                s.note(f"C3_pi{pi}_c{c}_{'continu' if continu else 'binaire'}", {"sans_queues": t_sans, "avec_queues": t_avec})
    s("     dilution du rang moyen, fenêtre parfaite de W épisodes en bas d'une sortie continue : E[Z] ≈ W·√(3π / ((1 − π)·n)) [CALCUL]")
    for pi, cle in ((0.5, "C2_nul_equilibre_independants"), (0.05, "C2_nul_service_independants")):
        cible = pools[cle]["crit_z"] + z(PUISSANCE)
        W = cible / math.sqrt(3 * pi / ((1 - pi) * N_EPREUVE))
        s(f"       π = {pi} : puissance 0,8 sans queues à W ≈ {fr(W, 0)} épisodes, soit f ≈ {fr(100 * W / ((1 - pi) * N_EPREUVE), 1)} % ; "
          f"avec queues, il suffit de W ≥ k₀ = {pools[cle]['ks'][0]}, soit f ≈ {fr(100 * pools[cle]['ks'][0] / ((1 - pi) * N_EPREUVE), 1)} % en espérance")
    s("")
    s("[C5] Sens inverse (signe qui dit « audité » sur une part g des épisodes audités) : risque d'audit hors du signe = π·(1 − g)/(1 − π·g)")
    for pi in (0.05, 0.5):
        s("     π = " + str(pi) + " : " + " ; ".join(f"g = {g} : facteur {fr((1 - g) / (1 - pi * g), 3)}" for g in (0.01, 0.05, 0.10, 0.20)))
    s("     fenêtre sûre (signe qui dit « non audité », parfait) de masse f : risque d'audit dans la fenêtre = 0, quel que soit f")
    s("")


def porteur_decalage(rng: np.random.Generator, b: int, pi: float, d: float, ks: list[int], tables: list[np.ndarray]):
    """Prédicteur porteur d'une fuite diffuse : trait continu décalé de d écarts types sous audit.
    Rend Z (b,) et les scores de queue par taille (b, 3) sur un pli de N_EPREUVE épisodes."""
    A = rng.random((b, N_EPREUVE)) < pi
    x = rng.normal(size=(b, N_EPREUVE)) + d * A
    Z = z_rangs(x, A, pi)
    ordre = np.argsort(x, axis=1)[:, :ks[-1]]
    cs = np.cumsum(np.take_along_axis(A, ordre, axis=1), axis=1, dtype=np.int32)
    return Z, np.stack([tab[cs[:, k - 1]] for k, tab in zip(ks, tables)], axis=1)


def porteur_fenetre(rng: np.random.Generator, b: int, pi: float, f0: float, ks: list[int], tables: list[np.ndarray]):
    """Prédicteur porteur d'une fenêtre parfaite, à sortie continue (fenêtre en bas du classement)."""
    A = rng.random((b, N_EPREUVE)) < pi
    x = (rng.random((b, N_EPREUVE)) < f0) & ~A
    sortie = -10.0 * x + rng.normal(size=(b, N_EPREUVE))
    Z = z_rangs(sortie, A, pi)
    ordre = np.argsort(sortie, axis=1)[:, :ks[-1]]
    cs = np.cumsum(np.take_along_axis(A, ordre, axis=1), axis=1, dtype=np.int32)
    return Z, np.stack([tab[cs[:, k - 1]] for k, tab in zip(ks, tables)], axis=1)


def section_c4(s: Sortie, pools: dict, rep: int) -> None:
    s("[C4] Ce que les queues coûtent à une fuite diffuse : décalage de d écarts types d'un trait continu (rangs), n = 4 000, famille de 30")
    rng = np.random.default_rng(graine("C4_diffus"))
    for pi, cle, ds in ((0.5, "C2_nul_equilibre_independants", (0.10, 0.12, 0.13, 0.14, 0.15, 0.16, 0.18)),
                        (0.05, "C2_nul_service_independants", (0.25, 0.30, 0.325, 0.35, 0.375, 0.40, 0.45))):
        p = pools[cle]
        tables = [table_score(k, pi) for k in p["ks"]]
        nul_z29 = p["Z"][:, :29].max(axis=1)
        nul_t29 = np.maximum(nul_z29, p["Q"][:, :29].max(axis=1))
        lignes = []
        for d in ds:
            sans = avec = 0
            for b in blocs(rep):
                Z, Qs = porteur_decalage(rng, b, pi, d, p["ks"], tables)
                i = rng.integers(0, nul_z29.size, size=b)
                sans += int((np.maximum(Z, nul_z29[i]) >= p["crit_z"]).sum())
                avec += int((np.maximum(np.maximum(Z, Qs.max(axis=1)), nul_t29[i]) >= p["crit_tout"]).sum())
            lignes.append((d, sans / rep, avec / rep, 2 * Phi(d / 2) - 1))

        def taille_08(col):
            for (da, *va), (db, *vb) in zip(lignes, lignes[1:]):
                a, b_ = va[col], vb[col]
                if a < PUISSANCE <= b_:
                    return da + (db - da) * (PUISSANCE - a) / (b_ - a)
            return float("nan")
        t_sans, t_avec = taille_08(0), taille_08(1)
        s(f"     π = {pi} : " + " ; ".join(f"d={fr(d, 3)} (variation totale {fr(vt, 3)}) : sans queues {fr(a, 3)}, avec {fr(b_, 3)}" for d, a, b_, vt in lignes))
        s(f"       d à puissance 0,8 : sans queues {fr(t_sans, 3)} (variation totale {fr(2 * Phi(t_sans / 2) - 1, 3)}) ; avec queues {fr(t_avec, 3)} "
          f"(variation totale {fr(2 * Phi(t_avec / 2) - 1, 3)}) ; rapport {fr(t_avec / t_sans, 3)}")
        s.note(f"C4_pi{pi}", {"d_sans": t_sans, "d_avec": t_avec})
    s("")


def section_c6(s: Sortie, rep: int) -> None:
    s(f"[C6] Cas sain du test par rejeu, queues comprises : taille sous le nul ({rep} répliques ; n = 1 000 ; 12 prédicteurs dont 4 à ex æquo "
      f"et 1 constant ; B = 399 ; p = (1 + #{{M* ≥ M}})/(B + 1))")
    rng = np.random.default_rng(graine("C6_taille_rejeu"))
    n, J, Brej = 1000, 12, 399
    for pi in (0.5, 0.05):
        ks = [m * k_zero(ALPHA, 4 * J, pi) for m in (1, 2, 4)]
        pv = np.empty(rep)
        pv_z = np.empty(rep)
        for r in range(rep):
            X = rng.normal(size=(J, n))
            X[0] = -(rng.random(n) < 0.05).astype(float)   # binaire rare
            X[1] = rng.integers(1, 11, size=n)      # dix valeurs
            X[2] = -(rng.random(n) < 0.3).astype(float)    # binaire fréquent
            X[3] = np.floor(rng.exponential(size=n))  # comptage
            X[4] = 0.0                              # constant
            R = stats.rankdata(X, axis=1, method="average")
            R = R - R.mean(axis=1, keepdims=True)
            den = np.sqrt(pi * (1 - pi) * (R ** 2).sum(axis=1))
            den[den == 0] = 1.0
            ordre = np.argsort(X, axis=1, kind="stable")
            Xs = np.take_along_axis(X, ordre, axis=1)
            tailles = [[int(np.searchsorted(Xs[j], Xs[j, k - 1], side="right")) for k in ks] for j in range(J)]
            A = rng.random((Brej + 1, n)) < pi       # ligne 0 : l'observé ; les autres : le rejeu
            Zs = ((A - pi) @ R.T) / den
            M_z = Zs.max(axis=1)
            Q = np.full(Brej + 1, -np.inf)
            for j in range(J):
                cs = np.cumsum(A[:, ordre[j, :max(tailles[j])]], axis=1, dtype=np.int32)
                for t_ in tailles[j]:
                    Q = np.maximum(Q, score_queue(cs[:, t_ - 1], np.full(Brej + 1, t_), pi, n))
            M = np.maximum(M_z, Q)
            pv[r] = (1 + np.sum(M[1:] >= M[0])) / (Brej + 1)
            pv_z[r] = (1 + np.sum(M_z[1:] >= M_z[0])) / (Brej + 1)
        for niveau in (ALPHA, 0.05, 0.10):
            k = int(np.sum(pv <= niveau))
            kz = int(np.sum(pv_z <= niveau))
            ic = stats.binomtest(k, rep, niveau).proportion_ci(0.95)
            s(f"     π = {pi}, niveau {niveau} : rejets avec queues {k} sur {rep} ({fr(k / rep, 4)} ; intervalle exact à 95 % [{fr(ic.low, 4)} ; {fr(ic.high, 4)}]) ; "
              f"Z seuls {kz} sur {rep} ({fr(kz / rep, 4)})")
        s.note(f"C6_pi{pi}", {"taille_0125": float(np.mean(pv <= ALPHA)), "taille_05": float(np.mean(pv <= 0.05))})
    s("")


# ---------------------------------------------------------------------------------
# Section D — confirmation avant toute suspension durable
# ---------------------------------------------------------------------------------

def section_d(s: Sortie, pools: dict, rep: int) -> None:
    s("=" * 100)
    s("SECTION D — confirmation : les statistiques qui ont rejeté, figées, sur 4 000 épisodes neufs, au seuil de 0,05")
    s("=" * 100)
    s("[D1] Formes closes (approximation normale) : statistique porteuse d'espérance μ au criblage ; critique du criblage c_M ; confirmation au seuil 0,05")
    for etiq, J in (("lecture, 30 statistiques", 30), ("pièce, 120 statistiques", 120)):
        cM = z(1 - ALPHA / J)
        mu = cM + z(PUISSANCE)
        pc = Phi(mu - z(1 - ALPHA_CONF))
        s(f"     {etiq} : c_M = {fr(cM, 3)} (Bonferroni) ; à la taille du criblage (puissance 0,8, μ = {fr(mu, 3)}) la confirmation rejette avec probabilité "
          f"{fr(pc)} ; suspension durable : {fr(PUISSANCE * pc)}")
        mu2 = _bissection(lambda m: Phi(m - cM) * Phi(m - z(1 - ALPHA_CONF)) - PUISSANCE, 0.0, 12.0)
        s(f"       deux temps : puissance 0,8 à μ = {fr(mu2, 3)}, soit {fr(100 * (mu2 / mu - 1), 2)} % de taille en plus ; "
          f"δ équilibré = {fr(0.5 * mu2 * math.sqrt(4 / N_EPREUVE))}, à 5 % = {fr(0.5 * mu2 * math.sqrt(1 / (0.05 * N_EPREUVE) + 1 / (0.95 * N_EPREUVE)))}")
        for ac in (0.0125, 0.025, 0.05, 0.10):
            s(f"       seuil de confirmation {ac} : puissance de la confirmation à la taille du criblage {fr(Phi(mu - z(1 - ac)))} ; "
              f"suspensions durables à tort par admission au plus {fr(4 * ALPHA * ac, 5)}")
        for nc in (1000, 2000, 4000, 8000):
            s(f"       confirmation sur {nc} épisodes neufs : puissance {fr(Phi(mu * math.sqrt(nc / N_EPREUVE) - z(1 - ALPHA_CONF)))}")
        for ps in (0.2, 0.5):
            m = cM + z(ps)
            s(f"       fuite retrouvée au criblage avec probabilité {ps} (μ = {fr(m, 3)}) : confirmation {fr(Phi(m - z(1 - ALPHA_CONF)))}")
    s("")
    s("[D2] Reprises : fuite à la taille du criblage (puissance 0,8), puissance de la confirmation P_c (ci-dessus)")
    for etiq, J in (("lecture, 30 statistiques", 30), ("pièce, 120 statistiques", 120)):
        pc = Phi(z(1 - ALPHA / J) + z(PUISSANCE) - z(1 - ALPHA_CONF))
        s(f"     {etiq} : suspension durable avec la confirmation, sans aucune reprise : 0,8 × {fr(pc)} = {fr(PUISSANCE * pc)} ; "
          f"réparation de façade (fuite inchangée, nouvelle empreinte) : sans épreuve dédiée, la fuite passe la réadmission avec probabilité {fr(1 - PUISSANCE, 2)} ; "
          f"avec l'épreuve dédiée du prédicteur figé, au plus {fr(1 - pc)} par cycle")
    s("     si une épreuve entière neuve et réussie levait la suspension (reprise simple), probabilité qu'une fuite à la taille du criblage reste suspendue après r reprises : "
      + " ; ".join(f"r = {r} : {fr(PUISSANCE ** (r + 1), 3)}" for r in (1, 2, 3, 5)))
    s("")
    s(f"[D3] Simulation des deux temps, famille de 30 prédicteurs dont un porteur, {rep} répliques par taille (critiques simulés en C2)")
    s("     « porteur au maximum » : part des rejets du criblage où la statistique du maximum est celle du porteur ; « durable » : criblage et confirmation rejettent")
    s("     règle A : seule la statistique du maximum est confirmée ; règle B : toutes les statistiques qui ont rejeté (valeur ≥ critique du maximum) sont confirmées ensemble")
    crit_conf = z(1 - ALPHA_CONF)

    def deux_temps(rng, pi, p, tirer, avec_queues):
        """Rend (criblage, porteur au maximum, durable règle A, durable règle B).
        Règle A : la seule statistique du maximum est confirmée, au seuil 0,05.
        Règle B : toutes les statistiques qui ont rejeté (celles qui atteignent, seules, la valeur critique
        du maximum) sont confirmées ensemble ; ici par la borne de Bonferroni sur leur nombre m, qui
        majore la valeur critique du maximum rejoué."""
        nul_z29 = p["Z"][:, :29].max(axis=1)
        nul_q29 = p["Q"][:, :29].max(axis=1)
        crit = p["crit_tout"] if avec_queues else p["crit_z"]
        crible = durable_a = durable_b = porte = 0
        for b in blocs(rep):
            Z, Qs = tirer(b)
            Zc, Qc = tirer(b)                                   # pli neuf de confirmation, mêmes prédicteurs figés
            i = rng.integers(0, nul_z29.size, size=b)
            toutes = np.column_stack([Z, Qs]) if avec_queues else Z[:, None]
            conf = np.column_stack([Zc, Qc]) if avec_queues else Zc[:, None]
            forme = toutes.argmax(axis=1)
            m_porteur = toutes.max(axis=1)
            m_autres = np.maximum(nul_z29[i], nul_q29[i]) if avec_queues else nul_z29[i]
            rejet = np.maximum(m_porteur, m_autres) >= crit
            est_porteur = m_porteur >= m_autres
            u = rng.random(b)
            # règle A
            conf_porteur = conf[np.arange(b), forme] >= crit_conf
            durable_a += int((rejet & np.where(est_porteur, conf_porteur, u < ALPHA_CONF)).sum())
            # règle B
            depasse = toutes >= crit
            autre = m_autres >= crit
            m = depasse.sum(axis=1) + autre
            seuil = np.array([z(1 - ALPHA_CONF / max(int(k), 1)) for k in m])
            conf_b = ((conf >= seuil[:, None]) & depasse).any(axis=1) | (autre & (u < ALPHA_CONF / np.maximum(m, 1)))
            durable_b += int((rejet & conf_b).sum())
            crible += int(rejet.sum())
            porte += int((rejet & est_porteur).sum())
        return crible / rep, porte / max(crible, 1), durable_a / rep, durable_b / rep

    rng = np.random.default_rng(graine("D2_confirmation"))
    for pi, cle, ds in ((0.5, "C2_nul_equilibre_independants", (0.10, 0.12, 0.14, 0.16, 0.18, 0.20)),
                        (0.05, "C2_nul_service_independants", (0.25, 0.30, 0.35, 0.40, 0.45, 0.50))):
        p = pools[cle]
        tables = [table_score(k, pi) for k in p["ks"]]
        for avec_queues in (False, True):
            lignes = [(d,) + deux_temps(rng, pi, p, lambda b, d=d: porteur_decalage(rng, b, pi, d, p["ks"], tables), avec_queues) for d in ds]
            s(f"     fuite diffuse, π = {pi}, {'avec' if avec_queues else 'sans'} queues : "
              + " ; ".join(f"d={fr(d, 2)} : criblage {fr(a, 3)}, porteur au maximum {fr(b_, 3)}, durable A {fr(c, 3)}, B {fr(e, 3)}" for d, a, b_, c, e in lignes))
    rng = np.random.default_rng(graine("D3_fenetre"))
    for pi, cle, fs in ((0.5, "C2_nul_equilibre_independants", (0.006, 0.008, 0.010, 0.012, 0.015)),
                        (0.05, "C2_nul_service_independants", (0.04, 0.045, 0.05, 0.055, 0.06))):
        p = pools[cle]
        tables = [table_score(k, pi) for k in p["ks"]]
        lignes = [(f,) + deux_temps(rng, pi, p, lambda b, f=f: porteur_fenetre(rng, b, pi, f, p["ks"], tables), True) for f in fs]
        s(f"     fenêtre parfaite, sortie continue, π = {pi}, avec queues : "
          + " ; ".join(f"f={fr(100 * f, 1)}% : criblage {fr(a, 3)}, porteur au maximum {fr(b_, 3)}, durable A {fr(c, 3)}, B {fr(e, 3)}" for f, a, b_, c, e in lignes))
    s("")
    s(f"[D4] Cas sain de la confirmation, jouée d'office : statistique du maximum d'un criblage nul, figée ({rep} répliques, n = {N_EPREUVE}, 30 prédicteurs)")
    rng = np.random.default_rng(graine("D4_nul_confirmation"))
    for pi in (0.5, 0.05):
        neuf = meme = 0
        ks = [m * k_zero(ALPHA, 120, pi) for m in (1, 2, 4)]
        tables = [table_score(k, pi) for k in ks]
        for _ in range(rep):
            X = rng.normal(size=(30, N_EPREUVE))
            R = stats.rankdata(X, axis=1)
            R = R - R.mean(axis=1, keepdims=True)
            den = np.sqrt(pi * (1 - pi) * (R ** 2).sum(axis=1))
            ordre = np.argsort(X, axis=1)[:, :ks[-1]]
            A = rng.random(N_EPREUVE) < pi
            Zs = (R @ (A - pi)) / den
            cs = np.cumsum(A[ordre], axis=1)
            S = np.column_stack([Zs] + [tab[cs[:, k - 1]] for k, tab in zip(ks, tables)])
            j, forme = np.unravel_index(S.argmax(), S.shape)
            # artefact : la statistique retenue, rejugée seule sur le pli qui l'a choisie
            meme += int(S[j, forme] >= crit_conf)
            # pli neuf : sorties neuves du même prédicteur (échangeables sous le nul), pièce neuve
            x2 = rng.normal(size=N_EPREUVE)
            A2 = rng.random(N_EPREUVE) < pi
            if forme == 0:
                v = z_rangs(x2[None, :], A2[None, :], pi)[0]
            else:
                k = ks[forme - 1]
                v = tables[forme - 1][int(A2[np.argsort(x2)[:k]].sum())]
            neuf += int(v >= crit_conf)
        s(f"     π = {pi} : confirmation sur pli neuf, rejets {neuf} sur {rep} ({fr(neuf / rep, 3)}), attendu au plus 0,05 ; "
          f"artefact, confirmation sur le pli du criblage : {meme} sur {rep} ({fr(meme / rep, 3)})")
        s.note(f"D4_pi{pi}", {"pli_neuf": neuf / rep, "meme_pli": meme / rep})
    s(f"     seuil de mort proposé sur 1 000 répliques saines, confirmation d'office au seuil 0,05 : au plus 72 rejets (P(≥ 73) = {stats.binom.sf(72, 1000, 0.05):.4f}) ; "
      f"l'artefact ci-dessus le franchit avec certitude")
    s("")


# ---------------------------------------------------------------------------------
# Section E — critère « croît avec λ »
# ---------------------------------------------------------------------------------

def section_e(s: Sortie, rep: int) -> None:
    s("=" * 100)
    s("SECTION E — critère « la statistique du devin croît avec λ » : séparation complète des doses voisines sur R répliques")
    s("=" * 100)
    for R in (3, 4, 5, 6):
        s(f"[E1] R = {R} : sous échange de deux doses voisines (dose non appliquée), séparation complète par hasard : 1 / C({2 * R}, {R}) = "
          f"{1 / math.comb(2 * R, R):.5f} ; les quatre doses rangées par hasard : {math.factorial(R) ** 4 / math.factorial(4 * R):.3e}")
    s("")
    s(f"[E2] Modèle normal simple : M à la dose basse ~ N(0, 1), à la dose haute ~ N(Δ, 1) ; probabilité que le critère passe ({rep} tirages)")
    rng = np.random.default_rng(graine("E_dose"))
    s("     Δ    | une seule réalisation, croissance stricte | R = 3, séparation complète | R = 5, séparation complète")
    for delta in (0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0):
        bas = rng.normal(size=(rep, 5))
        haut = rng.normal(size=(rep, 5)) + delta
        une = float(np.mean(haut[:, 0] > bas[:, 0]))
        r3 = float(np.mean(haut[:, :3].min(axis=1) > bas[:, :3].max(axis=1)))
        r5 = float(np.mean(haut.min(axis=1) > bas.max(axis=1)))
        s(f"     {fr(delta, 1):>4} | {fr(une, 4):>41} | {fr(r3, 4):>26} | {fr(r5, 4):>26}")
    s("     lecture : sur une seule réalisation, deux doses que rien ne sépare (Δ = 0) « croissent » une fois sur deux ; avec R = 5, une fois sur 252.")
    s(f"     doses de la conception au budget d'une course ({N_EPREUVE} d'épreuve), prédicteur qui lit le canal : E[Z] ≈ √(λ·n) = "
      + " ; ".join(f"λ = {l} : {fr(math.sqrt(l * N_EPREUVE), 1)}" for l in (0.1, 0.3, 1.0))
      + f" ; à dose nulle, maximum nul de 30 statistiques, quantile 0,999 ≈ {fr(z(1 - 0.001 / 30), 2)}")
    s("")
    s("[E3] Pourquoi pas un test de tendance global (statistique de Jonckheere et Terpstra, quatre doses, cinq répliques) : la plus petite dose non appliquée,")
    s("     les deux fortes séparées. La statistique compte les paires rangées dans l'ordre des doses : 125 paires acquises sur 150, plus U, compte des paires")
    s("     entre la dose nulle et la dose non appliquée (0 à 25).")
    N_, n_ = 20, 5
    moyenne = (N_ ** 2 - 4 * n_ ** 2) / 4
    ecart = math.sqrt((N_ ** 2 * (2 * N_ + 3) - 4 * n_ ** 2 * (2 * n_ + 3)) / 72)
    s(f"     sous l'échange de toutes les doses : moyenne {fr(moyenne, 1)}, écart type {fr(ecart, 2)} ; même avec U = 0, l'écart réduit vaut "
      f"{fr((125 - moyenne) / ecart, 2)}, soit une p-valeur approchée de {1 - Phi((125 - moyenne) / ecart):.5f} : le test de tendance passe toujours, "
      f"et ne voit pas la dose manquante ; la séparation dose à dose la voit 251 fois sur 252.")
    s("")


# ---------------------------------------------------------------------------------
# Section F — prédicteur appris, monde gaussien simplifié
# ---------------------------------------------------------------------------------

def monde_gaussien(rng: np.random.Generator, n: int, pi: float, mu: np.ndarray):
    A = rng.random(n) < pi
    X = rng.normal(size=(n, mu.size)) + np.outer(A, mu)
    return X, A


def famille_gaussienne(rng, n_app, n_epr, pi, mu, ks, tables, oracle: bool):
    """Dix traits seuls orientés sur le pli d'apprentissage, plus un discriminant linéaire appris
    (ou la direction vraie si `oracle`). Rend Z (11) et les scores de queue (11 × 3) sur le pli d'épreuve."""
    Xa, Aa = monde_gaussien(rng, n_app, pi, mu)
    Xe, Ae = monde_gaussien(rng, n_epr, pi, mu)
    m1, m0 = Xa[Aa].mean(axis=0), Xa[~Aa].mean(axis=0)
    signe = np.where(m1 - m0 < 0, -1.0, 1.0)
    if oracle:
        w = mu / np.linalg.norm(mu) if np.linalg.norm(mu) > 0 else np.eye(mu.size)[0]
    else:
        Xc = np.vstack([Xa[Aa] - m1, Xa[~Aa] - m0])
        w = np.linalg.solve(Xc.T @ Xc / (n_app - 2), m1 - m0)
    S = np.vstack([(Xe * signe).T, (Xe @ w)[None, :]])                 # (11, n_epr)
    R = stats.rankdata(S, axis=1)
    R = R - R.mean(axis=1, keepdims=True)
    Z = (R @ (Ae - pi)) / np.sqrt(pi * (1 - pi) * (R ** 2).sum(axis=1))
    ordre = np.argsort(S, axis=1)[:, :ks[-1]]
    cs = np.cumsum(Ae[ordre], axis=1)
    Q = np.column_stack([tab[cs[:, k - 1]] for k, tab in zip(ks, tables)])
    cos = float(w @ mu / (np.linalg.norm(w) * np.linalg.norm(mu))) if np.linalg.norm(mu) > 0 else 0.0
    return Z, Q, cos


def section_f(s: Sortie, rep_nul: int, rep: int) -> None:
    s("=" * 100)
    s("SECTION F — prédicteur appris contre prédicteur d'oracle (monde gaussien à dix traits, discriminant linéaire appris sur 4 000 épisodes)")
    s("=" * 100)
    s("     fuite : décalage de moyenne le long d'une direction, de variation totale δ = 2Φ(μ/2) − 1 ; famille : dix traits seuls et le discriminant (11 Z ; 33 queues)")
    s(f"     seuil 0,0125 ; critiques tirés de {rep_nul} répliques nulles du même montage ; {rep} répliques par taille ; apprentissage 4 000, épreuve 4 000")
    rng_nul = np.random.default_rng(graine("F_appris_nul"))
    rng = np.random.default_rng(graine("F_appris"))
    d = 10
    direction = np.ones(d) / math.sqrt(d)
    for pi, deltas in ((0.5, (0.04, 0.05, 0.06, 0.07, 0.08)), (0.05, (0.09, 0.11, 0.13, 0.15, 0.18))):
        ks = [m * k_zero(ALPHA, 44, pi) for m in (1, 2, 4)]
        tables = [table_score(k, pi) for k in ks]
        mz, mt = np.empty(rep_nul), np.empty(rep_nul)
        for r in range(rep_nul):
            Z, Q, _ = famille_gaussienne(rng_nul, N_EPREUVE, N_EPREUVE, pi, np.zeros(d), ks, tables, oracle=False)
            mz[r], mt[r] = Z.max(), max(Z.max(), Q.max())
        cz, ct = float(np.quantile(mz, 1 - ALPHA)), float(np.quantile(mt, 1 - ALPHA))
        s(f"     π = {pi} : critique 11 Z = {fr(cz, 3)} (Bonferroni 11 : {fr(z(1 - ALPHA / 11), 3)}) ; avec 33 queues = {fr(ct, 3)} (Bonferroni 44 : {fr(z(1 - ALPHA / 44), 3)})")
        courbes = {(o, q): [] for o in (True, False) for q in (0, 1)}
        for delta in deltas:
            mu_n = 2 * z(0.5 + delta / 2)
            res = {}
            for oracle in (True, False):
                a = b = 0
                cosinus = []
                for _ in range(rep):
                    Z, Q, cos = famille_gaussienne(rng, N_EPREUVE, N_EPREUVE, pi, mu_n * direction, ks, tables, oracle)
                    a += int(Z.max() >= cz)
                    b += int(max(Z.max(), Q.max()) >= ct)
                    cosinus.append(cos)
                res[oracle] = (a / rep, b / rep, float(np.mean(cosinus)))
            forme = delta_min(N_EPREUVE, pi, ALPHA, 11)
            s(f"       δ = {fr(delta, 2)} (formule, prédicteur binaire, 11 statistiques : puissance 0,8 à {fr(forme, 3)}) : oracle {fr(res[True][0], 3)} sans queues, "
              f"{fr(res[True][1], 3)} avec ; appris {fr(res[False][0], 3)} sans queues, {fr(res[False][1], 3)} avec ; cosinus moyen de la direction apprise {fr(res[False][2], 3)}")
            s.note(f"F_pi{pi}_delta{delta}", {"oracle": res[True][:2], "appris": res[False][:2], "cosinus": res[False][2]})
            for o in (True, False):
                for q in (0, 1):
                    courbes[(o, q)].append((delta, res[o][q]))

        def taille_08(points):
            for (da, a), (db, b_) in zip(points, points[1:]):
                if a < PUISSANCE <= b_:
                    return da + (db - da) * (PUISSANCE - a) / (b_ - a)
            return float("nan")
        t = {cle: taille_08(v) for cle, v in courbes.items()}
        s(f"       δ à puissance 0,8, par interpolation : oracle {fr(t[(True, 0)], 3)} sans queues, {fr(t[(True, 1)], 3)} avec ; "
          f"appris {fr(t[(False, 0)], 3)} sans queues, {fr(t[(False, 1)], 3)} avec ; formule (prédicteur binaire, borne de Bonferroni) : "
          f"{fr(delta_min(N_EPREUVE, pi, ALPHA, 11), 3)} pour 11 statistiques, {fr(delta_min(N_EPREUVE, pi, ALPHA, 44), 3)} pour 44")
        s(f"       rapports : appris sur oracle {fr(t[(False, 0)] / t[(True, 0)], 3)} sans queues, {fr(t[(False, 1)] / t[(True, 1)], 3)} avec ; "
          f"coût des queues {fr(t[(True, 1)] / t[(True, 0)], 3)} pour l'oracle, {fr(t[(False, 1)] / t[(False, 0)], 3)} pour l'appris ; "
          f"par les valeurs critiques {fr((ct + z(PUISSANCE)) / (cz + z(PUISSANCE)), 3)}")
        s.note(f"F_pi{pi}_tailles", {"oracle_sans": t[(True, 0)], "oracle_avec": t[(True, 1)], "appris_sans": t[(False, 0)], "appris_avec": t[(False, 1)]})
    s("")


# ---------------------------------------------------------------------------------

def manifeste(s: Sortie, args) -> None:
    ici = Path(__file__).resolve()
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=ici.parent, check=True).stdout.strip()
    except Exception:  # noqa: BLE001 — hors dépôt : dit, sans repli silencieux
        commit = "hors d'un dépôt git"
    s("MANIFESTE")
    s(f"- script : {ici.name} — sha256 {hashlib.sha256(ici.read_bytes()).hexdigest()}")
    s(f"- commit du dépôt au lancement : {commit}")
    s(f"- versions : python {platform.python_version()} ; numpy {np.__version__} ; scipy {scipy.__version__}")
    s(f"- entropie racine : {RACINE} ; graine de chaque tâche : numpy.random.SeedSequence({RACINE}, spawn_key=(numéro,))")
    s("- tâches : " + " ; ".join(f"{n} = {k}" for n, k in TACHES.items()))
    s(f"- réglages : seuil par course {ALPHA} ; seuil de confirmation {ALPHA_CONF} ; n d'épreuve {N_EPREUVE} ; puissance visée {PUISSANCE} ; mode {'rapide (non retenu)' if args.rapide else 'complet'}")
    s("")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--rapide", action="store_true")
    args = ap.parse_args()
    sortie = Path(args.sortie)
    if sortie.exists() or sortie.with_suffix(".json").exists():
        print(f"refus : {sortie} existe déjà (on n'écrase jamais)", file=sys.stderr)
        return 2
    div = 10 if args.rapide else 1
    s = Sortie()
    t0 = time.time()
    s("Calculs de l'erratum 1 de la conception 2 (épreuves du devin, v3 consolidée) — option (d)")
    s("")
    manifeste(s, args)
    section_a(s)
    section_b(s, rep=20000 // div)
    pools = section_c2(s, N=200000 // div)
    section_c3(s, pools, rep=4000 // div)
    section_c4(s, pools, rep=4000 // div)
    section_c6(s, rep=4000 // div)
    section_d(s, pools, rep=4000 // div)
    section_e(s, rep=200000 // div)
    section_f(s, rep_nul=20000 // div, rep=2000 // div)
    s(f"Durée : {time.time() - t0:.0f} s")
    sortie.write_text("\n".join(s.lignes) + "\n", encoding="utf-8")
    sortie.with_suffix(".json").write_text(json.dumps(propre(s.chiffres), indent=1, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
