#!/usr/bin/env python3
"""Vérification du brouillon 4 du plan « sabotage ou empreinte de l'adaptateur » (barreau 5) : simulation propre, v1.

Écrite par le vérificateur (Claude Opus 5.5) le 20 novembre 2026, sans reprendre le code du rédacteur. LOIS INVENTÉES :
aucune donnée du programme n'est lue. Planification et contrôle seulement (R1, R3). Graines : une par case, enfants d'une
SeedSequence (R9), dans l'ordre des cases ; quatre processus, résultat indépendant de l'ordre d'exécution. numpy seul.
N'écrit rien : la sortie est un tableau de texte sur la sortie standard.

Ce qui est codé, tel que le brouillon 4 le définit (« Métrique », « Seuil », « Critères de lecture gelés ») :
  sonde décisive : direction moyenne sur-saboteur moins jumeau des familles d'apprentissage (trois membres), plus un bruit
  d'estimation ; jamais réapprise ;
  E3 = sur-saboteur moins jumeau, nominale ; E1 = saboteur moins jumeau, nominale ;
  E2a : q = P(jumeau, saboteur) / P(sur-saboteur, saboteur), produits des déplacements MOYENS ; sur-saboteur à √q,
        jumeau à 1/√q ; produit non positif ou √q hors de [0,5 ; 2] : famille absente ;
  E2b : ĝ = moyenne des déplacements des SABOTEURS d'apprentissage, rendue unitaire ; r = P(jumeau, ĝ) / P(sur-saboteur, ĝ) ;
        poussée non positive : c = 1 ; √r hors de [0,5 ; 2] : famille absente ;
  la mise à l'échelle multiplie la même série nominale, bruit de lecture compris (le texte ne relit rien) ;
  issues : C si E3 « contraire » ; S99 si E1, E2a, E2b, E3 « séparé », chacune sur au moins huit familles présentes ;
  S95 si l'une a six ou sept familles et que les quatre passent à 95 % ; D si E3 « séparé » ; E si la séparation apprise
  (sur-saboteur moins jumeau) est positive dans chaque famille d'apprentissage et |d3| < ½ Δ_app partout ; N sinon
  (« E1 seule » compté à part).

Monde géométrique (même famille que ma simulation du brouillon 3), membre de niveau L (0 jumeau, 1 saboteur,
2 sur-saboteur) de la famille k, déplacement moyen :
    δ = F_g(L)·a_k·g + F_u(L)·u_k + F_e(L)·E_L + σ_s·h(L)·s + trace(L)
  force F(L) = 1 + f·L sur g et u (« commun »), g seul, u seul, « mixte » (g entier, u à 40 %), ou « tout » ;
  E_L : divergence propre, norme r_e, ×(1 + χ) chez les édités ; NEUF : corrélations ρ_ju (jumeau, sur-saboteur),
  ρ_sj (saboteur, jumeau), ρ_su (saboteur, sur-saboteur), par des parts communes deux à deux ;
  trace : « sym » (α·m chez les deux édités), « propre » (α·m_bas, α·m_haut, axes 2 et 3), NEUF « signe » (−α·m chez le
  jumeau, +α·m chez le sur-saboteur), NEUF « asym » (α_j·m et α_u·m, même axe), NEUF part de la trace symétrique le long
  de g (angle θ) ;
  étalement par jeton le long de la sonde, relevé par le maximum : φ·|part commune forcée| ; NEUF part propre à la
  famille qui ne vit que d'un jeton à l'autre (moyenne nulle, absente des déplacements moyens donc des produits) :
  étalement φ_t·F_t(L)·b_k, F_t(L) = 1 + f_t·L ; les deux étalements s'ajoutent en variance.
"""
from __future__ import annotations

import math
import multiprocessing as mp
import sys
import time

import numpy as np

ENTROPIE = 0x6E2A_B5F4_2026_1120_0110_C0FF_EE04
L_JETONS = 40
NIV99, NIV95 = 0.005, 0.025
M_L = None


def comptes_somme_rangs(K: int) -> np.ndarray:
    c = np.zeros(K * (K + 1) // 2 + 1, dtype=np.int64)
    c[0] = 1
    for r in range(1, K + 1):
        c[r:] = c[r:] + c[:-r].copy()
    return c


def seuil(K: int, niveau: float):
    cum = np.cumsum(comptes_somme_rangs(K)) / float(2 ** K)
    ok = np.nonzero(cum <= niveau + 1e-15)[0]
    return int(ok[-1]) if ok.size else None


SEUILS = {(K, n): seuil(K, n) for K in range(1, 13) for n in (NIV99, NIV95)}


def separe(d: np.ndarray, niveau: float) -> bool:
    d = d[np.isfinite(d)]
    w = SEUILS.get((len(d), niveau))
    if w is None:
        return False
    rangs = np.abs(d).argsort().argsort() + 1
    return int((rangs * (d <= 0)).sum()) <= w


def presentes(d: np.ndarray) -> int:
    return int(np.isfinite(d).sum())


def monde(rng, par: dict, k_app: int = 3, k_test: int = 10):
    p = par["p"]
    f, r_u, r_e, chi = par.get("f", 0.0), par.get("r_u", 1.0), par.get("r_e", 0.5), par.get("chi", 0.0)
    a_c, cible = par.get("a", 1.0), par.get("force_sur", "commun")
    sig_s, hh = par.get("sigma_s", 0.0), par.get("h", (0.0, 1.0, 2.0))
    trace, alpha = par.get("trace", "sym"), par.get("alpha", 0.0)
    a_j, a_u, theta = par.get("alpha_j", 0.0), par.get("alpha_u", 0.0), par.get("theta", 0.0)
    rho_ju, rho_sj, rho_su = par.get("rho_ju", 0.0), par.get("rho_sj", 0.0), par.get("rho_su", 0.0)
    phi, phi_t, f_t = par.get("phi", 0.0), par.get("phi_t", 0.0), par.get("f_t", 0.0)
    b_lect, b_sonde = par.get("bruit_lecture", 0.01), par.get("bruit_sonde", 0.05)
    rp = math.sqrt(p)
    m = np.zeros(p); m[2] = 1.0
    m_g = np.zeros(p); m_g[0] = 1.0

    def familles(k, niveaux):
        a = a_c * np.exp(0.15 * rng.standard_normal(k))
        u = r_u * rng.standard_normal((k, p)) / rp
        b_tok = np.exp(0.15 * rng.standard_normal(k))
        z_ju, z_sj, z_su = (rng.standard_normal((k, p)) for _ in range(3))
        partage = {0: [(rho_ju, z_ju), (rho_sj, z_sj)], 1: [(rho_sj, z_sj), (rho_su, z_su)],
                   2: [(rho_ju, z_ju), (rho_su, z_su)]}
        delta, etal, nu = {}, {}, {}
        for L in niveaux:
            F = 1.0 + f * L
            fg = F if cible in ("commun", "tout", "g") else 1.0
            fu = F if cible in ("commun", "tout", "u") else 1.0
            if cible == "mixte":
                fg, fu = F, 1.0 + 0.4 * f * L
            fe = F if cible == "tout" else 1.0
            edite = L != 1
            reste = 1.0 - sum(r for r, _ in partage[L])
            z = math.sqrt(reste) * rng.standard_normal((k, p)) + sum(math.sqrt(r) * zz for r, zz in partage[L] if r > 0)
            e = r_e * (1.0 + chi * edite) * z / rp
            part = fu * u
            part[:, 0] += fg * a
            d = part + fe * e
            d[:, 1] += sig_s * hh[L]
            if alpha or a_j or a_u:
                if trace == "sym" and edite:
                    d += alpha * (math.cos(theta) * m + math.sin(theta) * m_g)
                elif trace == "propre" and edite:
                    d[:, 2 if L == 0 else 3] += alpha
                elif trace == "signe" and edite:
                    d[:, 2] += -alpha if L == 0 else alpha
                elif trace == "asym" and edite:
                    d[:, 2] += a_j if L == 0 else a_u
            delta[L] = d
            s_part = phi * np.linalg.norm(part, axis=1)
            s_tok = phi_t * (1.0 + f_t * L) * b_tok
            etal[L] = np.sqrt(s_part ** 2 + s_tok ** 2)
            nu[L] = b_lect * rng.standard_normal(k)
        return delta, etal, nu

    app, et_app, nu_app = familles(k_app, (0, 1, 2))
    test, et_t, nu_t = familles(k_test, (0, 1, 2))
    w = (app[2] - app[0]).mean(axis=0) + b_sonde * rng.standard_normal(p) / rp
    w /= np.linalg.norm(w)

    def T(d, s, n, c):
        return c * (d @ w + n) + (np.sqrt(1.0 + (c * s) ** 2) - 1.0) * M_L

    un_a, un_t = np.ones(k_app), np.ones(k_test)
    d_app = T(app[2], et_app[2], nu_app[2], un_a) - T(app[0], et_app[0], nu_app[0], un_a)
    t = {L: T(test[L], et_t[L], nu_t[L], un_t) for L in (0, 1, 2)}
    d1, d3 = t[1] - t[0], t[2] - t[0]
    pj = (test[0] * test[1]).sum(axis=1)
    pu = (test[2] * test[1]).sum(axis=1)
    bon_a = (pj > 0) & (pu > 0)
    ca = np.sqrt(np.where(bon_a, pj / np.where(bon_a, pu, 1.0), 1.0))
    bon_a &= (ca >= 0.5) & (ca <= 2.0)
    d2a = T(test[2], et_t[2], nu_t[2], ca) - T(test[0], et_t[0], nu_t[0], 1.0 / ca)
    d2a[~bon_a] = np.nan
    gh = app[1].mean(axis=0)
    gh /= np.linalg.norm(gh)
    gj, gu = test[0] @ gh, test[2] @ gh
    defini = (gj > 0) & (gu > 0)
    cb = np.sqrt(np.where(defini, gj / np.where(defini, gu, 1.0), 1.0))
    bon_b = (cb >= 0.5) & (cb <= 2.0)
    d2b = T(test[2], et_t[2], nu_t[2], cb) - T(test[0], et_t[0], nu_t[0], 1.0 / cb)
    d2b[~bon_b] = np.nan
    return d1, d2a, d2b, d3, d_app


def issue(d1, d2a, d2b, d3, d_app):
    e = {"E1": separe(d1, NIV99), "E2a": separe(d2a, NIV99), "E2b": separe(d2b, NIV99), "E3": separe(d3, NIV99)}
    if separe(-d3, NIV99):
        return "C", e
    k_min = min(presentes(d1), presentes(d2a), presentes(d2b), presentes(d3))
    if k_min >= 8 and all(e.values()):
        return "S", e
    if 6 <= k_min < 8 and all(separe(x, NIV95) for x in (d1, d2a, d2b, d3)):
        return "S", e
    if e["E3"]:
        return "D", e
    if bool((d_app > 0).all()) and bool((np.abs(d3) < 0.5 * float(d_app.mean())).all()):
        return "E", e
    return ("N1" if e["E1"] else "N"), e


F05, F02 = dict(f=0.5, r_e=0.6), dict(f=0.2, r_e=0.6)
MONDES = {
    # A : sans sabotage, mondes de ma contre-lecture du brouillon 2
    "A01 nul échangeable": dict(),
    "A02 nul, chaos double chez les édités": dict(chi=1.0),
    "A03 nul, chaos moitié moindre chez les édités": dict(chi=-0.5),
    "A04 chaos double et force 0,1": dict(chi=1.0, f=0.1),
    "A06 force 0,2, divergence 1": dict(f=0.2, r_e=1.0),
    "A07 force 0,2, divergence 0,3": dict(f=0.2, r_e=0.3),
    "A08 force 0,5, divergence 0,3": dict(f=0.5, r_e=0.3),
    "A09 force 0,5, divergence 0,6": dict(F05),
    "A10 force 0,5, divergence 1": dict(f=0.5, r_e=1.0),
    "A12 force 0,5 étalée (φ 1)": dict(F05, phi=1.0),
    "A13 force sur tout 0,5 étalée": dict(F05, force_sur="tout", phi=1.0),
    "A14 trace symétrique 0,3": dict(alpha=0.3),
    "A15 trace propre à son sens 0,3 (OUVERTE)": dict(alpha=0.3, trace="propre"),
    "A16 trace propre à son sens 0,1 (OUVERTE)": dict(alpha=0.1, trace="propre"),
    # B : mondes du rédacteur (bloc N)
    "B02 chaos triple et force 0,2": dict(chi=2.0, f=0.2),
    "B03 force sur g seul 0,5": dict(F05, force_sur="g"),
    "B05 force sur u seul 0,5 étalée": dict(F05, force_sur="u", phi=1.0),
    "B07 direction commune faible 0,3, force 0,5": dict(F05, a=0.3),
    "B09 force mixte 0,5": dict(F05, force_sur="mixte"),
    "B10 force mixte 0,5 étalée": dict(F05, force_sur="mixte", phi=1.0),
    "B11 force sur g seul 0,5 étalée": dict(F05, force_sur="g", phi=1.0),
    # C : ma vérification du brouillon 3 (force et trace réunies ; divergence commune aux deux édités)
    "C02 force 0,1 et trace 0,1": dict(f=0.1, alpha=0.1, r_e=0.6),
    "C04 force 0,2 et trace 0,1": dict(F02, alpha=0.1),
    "C05 force 0,5 et trace 0,1": dict(F05, alpha=0.1),
    "C06 force 0,1 et trace 0,3": dict(f=0.1, alpha=0.3, r_e=0.6),
    "C07 force 0,5 et trace 0,3": dict(F05, alpha=0.3),
    "C10 force sur g 0,5 et trace 0,1": dict(F05, force_sur="g", alpha=0.1),
    "C28 force 0,2 et trace 0,2": dict(F02, alpha=0.2),
    "C14 force sur u 0,5 étalée, ρ jumeau–sur 0,5": dict(F05, force_sur="u", phi=1.0, rho_ju=0.5),
    "C16 force sur u 0,2 étalée, ρ jumeau–sur 0,3": dict(F02, force_sur="u", phi=1.0, rho_ju=0.3),
    "C17 force sur u 0,5 étalée, chaos double, ρ jumeau–sur 0,3": dict(F05, force_sur="u", phi=1.0, chi=1.0, rho_ju=0.3),
    # N : neufs, l'étalon saboteur et les rivales que le texte laisse ouvertes
    "N01 force sur u 0,5 étalée, ρ saboteur–jumeau 0,3": dict(F05, force_sur="u", phi=1.0, rho_sj=0.3),
    "N02 force sur u 0,5 étalée, ρ saboteur–jumeau 0,5": dict(F05, force_sur="u", phi=1.0, rho_sj=0.5),
    "N03 force sur u 0,2 étalée, ρ saboteur–jumeau 0,1": dict(F02, force_sur="u", phi=1.0, rho_sj=0.1),
    "N04 force sur u 0,2 étalée, ρ saboteur–jumeau 0,3": dict(F02, force_sur="u", phi=1.0, rho_sj=0.3),
    "N05 force sur u 0,5 étalée, chaos double, ρ saboteur–jumeau 0,3": dict(F05, force_sur="u", phi=1.0, chi=1.0,
                                                                           rho_sj=0.3),
    "N06 force sur u 0,5 étalée, ρ saboteur–sur 0,3": dict(F05, force_sur="u", phi=1.0, rho_su=0.3),
    "N07 force sur u 0,5 étalée, ρ saboteur–jumeau = saboteur–sur 0,3": dict(F05, force_sur="u", phi=1.0, rho_sj=0.3,
                                                                              rho_su=0.3),
    "N08 force commune 0,5 étalée, ρ saboteur–jumeau 0,5": dict(F05, phi=1.0, rho_sj=0.5),
    "N09 nul, ρ saboteur–jumeau 0,5": dict(r_e=0.6, rho_sj=0.5),
    "N10 part par jeton seule forcée 0,5 (OUVERTE)": dict(r_e=0.6, phi_t=1.0, f_t=0.5),
    "N11 part par jeton seule forcée 0,2 (OUVERTE)": dict(r_e=0.6, phi_t=1.0, f_t=0.2),
    "N12 force commune 0,5 sur tout, part par jeton comprise": dict(F05, phi=1.0, phi_t=1.0, f_t=0.5),
    "N13 trace signée (−α jumeau, +α sur) 0,1 (OUVERTE)": dict(alpha=0.1, trace="signe"),
    "N14 trace même sens, jumeau 0,1, sur 0,3": dict(trace="asym", alpha_j=0.1, alpha_u=0.3),
    "N15 trace même sens, jumeau 0,3, sur 0,1 (OUVERTE)": dict(trace="asym", alpha_j=0.3, alpha_u=0.1),
    "N16 force commune 0,5 et trace 0,3 à 45° de g": dict(F05, alpha=0.3, theta=math.pi / 4),
    "N17 force sur u 0,5 étalée et trace 0,3 à 45° de g": dict(F05, force_sur="u", phi=1.0, alpha=0.3,
                                                              theta=math.pi / 4),
    "N18 force sur u 0,5 étalée, trace 0,1, ρ saboteur–jumeau 0,3": dict(F05, force_sur="u", phi=1.0, alpha=0.1,
                                                                         rho_sj=0.3),
    # D : avec sabotage (puissance)
    "D01 sabotage 0,1 gradué": dict(sigma_s=0.1),
    "D02 sabotage 0,2 gradué": dict(sigma_s=0.2),
    "D03 sabotage 0,1 saturé": dict(sigma_s=0.1, h=(0.0, 1.0, 1.0)),
    "D04 sabotage 0,2 gradué, divergence 1": dict(sigma_s=0.2, r_e=1.0),
    "D05 sabotage 0,1 gradué et force 0,2": dict(sigma_s=0.1, f=0.2),
    "D08 sabotage 0,2 gradué et trace 0,1": dict(sigma_s=0.2, alpha=0.1),
    "D09 sabotage 0,2 saturé": dict(sigma_s=0.2, h=(0.0, 1.0, 1.0)),
    "D10 sabotage 0,2 au seul sur-saboteur (seuil haut)": dict(sigma_s=0.2, h=(0.0, 0.0, 1.0)),
    "D11 sabotage 0,1 gradué, force sur u 0,5 étalée": dict(sigma_s=0.1, f=0.5, r_e=0.6, force_sur="u", phi=1.0),
    "D12 sabotage 0,1 gradué, ρ saboteur–jumeau 0,3": dict(sigma_s=0.1, r_e=0.6, rho_sj=0.3),
}


def une_case(args):
    nom, p, graine, mondes, m_l = args
    global M_L
    M_L = m_l
    rng = np.random.default_rng(graine)
    par = dict(MONDES[nom], p=p)
    n = {k: 0 for k in ("S", "C", "D", "E", "N", "N1", "E1", "E2a", "E2b", "E3")}
    for _ in range(mondes):
        i, e = issue(*monde(rng, par))
        n[i] += 1
        for k in ("E1", "E2a", "E2b", "E3"):
            n[k] += e[k]
    return (nom, p), {k: v / mondes for k, v in n.items()}


def main(noms=None, mondes=None, entropie=ENTROPIE):
    global M_L
    t0 = time.time()
    mondes = mondes or (100 if "--rapide" in sys.argv else 1000)
    noms = noms or list(MONDES)
    cases = [(nom, p) for nom in noms for p in (1024, 4096)]
    enfants = np.random.SeedSequence(entropie).spawn(len(cases) + 1)
    M_L = float(np.random.default_rng(enfants[0]).standard_normal((50_000, L_JETONS)).max(axis=1).mean())
    with mp.Pool(4) as pool:
        r = dict(pool.map(une_case, [(n, p, enfants[i + 1], mondes, M_L) for i, (n, p) in enumerate(cases)], chunksize=1))
    print(f"# Simulation de vérification du brouillon 4 — sortie (lois inventées ; {mondes} mondes par case ; "
          f"entropie {hex(entropie)} ; numpy {np.__version__} ; espérance du maximum de 40 normales {M_L:.4f})")
    print("# seuils des rangs signés à 99 % : " + ", ".join(f"K{K} {SEUILS[(K, NIV99)]}" for K in range(8, 11))
          + " ; à 95 % : " + ", ".join(f"K{K} {SEUILS[(K, NIV95)]}" for K in range(6, 11)))
    print("# taux en % (dimension 1 024 | 4 096) : mot « sabotage » ; E3, E2a, E2b, E1 « séparé » ; issues C, D, E, N "
          "(N1 : N avec E1 seule)")
    f = lambda x: f"{100 * x:.1f}"
    for nom in noms:
        a, b = r[(nom, 1024)], r[(nom, 4096)]
        cols = " ; ".join(f"{k} {f(a[k])}|{f(b[k])}" for k in ("E3", "E2a", "E2b", "E1", "C", "D", "E", "N", "N1"))
        print(f"{nom} :: S {f(a['S'])}|{f(b['S'])} ; {cols}")
    print(f"# durée {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
