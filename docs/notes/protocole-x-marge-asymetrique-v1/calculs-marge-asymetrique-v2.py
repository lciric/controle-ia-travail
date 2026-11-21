#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « protocole X : la marge asymétrique, éprouvée par les expérimentateurs » (v2).

Aucun tirage : arithmétique, lois binomiales exactes, quadratures déterministes
(Gauss-Hermite et Gauss-Legendre). Aucune donnée du programme. Les entrées marquées
« recopié » viennent de PDF empreintés, à la page dite dans la note ; toutes les autres
sont des suppositions d'illustration. Rejeu : python3 -I calculs-marge-asymetrique-v2.py
Les attentes sont écrites dans les libellés AVANT l'exécution ; une attente manquée est
dite « attente manquée », jamais corrigée après coup.

v2 : les blocs A à D sont ceux de la v1, inchangés ; le bloc E compte seize puis dix-huit témoins ;
les blocs F, G et H sont neufs (constats 5, 6 et 7 de la contre-lecture de la v1) ; le bloc G1 bis a été
ajouté après la première exécution de G1, et le dit.
"""
import math
from statistics import NormalDist

import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from numpy.polynomial.legendre import leggauss

ND = NormalDist()
_erfc = np.vectorize(math.erfc, otypes=[float])


def Phi(x):
    """Fonction de répartition normale, vectorisée."""
    return 0.5 * _erfc(-np.asarray(x, dtype=float) / math.sqrt(2.0))


def phi(x):
    x = np.asarray(x, dtype=float)
    return np.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def binom_pmf(k, a, c):
    return math.comb(k, a) * c ** a * (1.0 - c) ** (k - a)


def maj(k, q):
    """Probabilité qu'une majorité stricte de k tirages (k impair) soit « attaque »."""
    return sum(binom_pmf(k, a, q) for a in range(k // 2 + 1, k + 1))


def bissection(f, lo, hi, n=200):
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


ZN, ZW = hermegauss(120)          # nœuds pour le facteur commun Z ~ N(0,1)
ZW = ZW / math.sqrt(2.0 * math.pi)
XN, XW = leggauss(400)            # nœuds pour l'intégrale intérieure


def ligne(txt=""):
    print(txt)


# ---------------------------------------------------------------------------
ligne("Calculs de la note « protocole X : la marge asymétrique, éprouvée par les expérimentateurs » (v2)")
ligne("Aucun tirage ; entrées = suppositions d'illustration, sauf mention « recopié ».")
ligne()

# ---------------------------------------------------------------------------
ligne("[A] La table publiée du rééchantillonnage, décomposée (recopié : Bhatt et al., arXiv 2504.10374v1,")
ligne("    p. 1, 5, 7, 8 et 9 du fichier ; sûreté en %, à 95 % d'utilité sauf la première ligne)")
tm, dtt, dtr, inc, strikes, tt, tt_um = 41.8, 72.7, 83.2, 84.0, 84.9, 87.1, 92.6
etapes = [
    ("surveillance seule (100 % d'utilité)", tm),
    ("cession à la voie de confiance au-dessus d'un seuil", dtt),
    ("rééchantillonnage, exécution du moins suspect", dtr),
    ("+ tirages de plus pour l'audit, au présent", inc),
    ("+ audit après trois signalements", strikes),
    ("+ tirages de plus sur des pas passés", tt),
    ("+ moniteur non fiable, paraphrase de confiance", tt_um),
]
total = (100 - tm) - (100 - tt_um)
prec = tm
ligne("    protocole                                              sûreté   succès de l'attaque   part de la baisse totale")
for nom, s in etapes:
    part = (s - prec) / total * 100 if s != tm else float("nan")
    ptxt = "      —" if s == tm else f"{s - prec:5.1f} points, {part:4.1f} %"
    ligne(f"    {nom:54s} {s:5.1f}   {100 - s:5.1f}                 {ptxt}")
    prec = s
ligne(f"    baisse totale du succès de l'attaque : de {100 - tm:.1f} à {100 - tt_um:.1f}, soit {total:.1f} points")
ligne(f"    (le résumé de l'article dit « de 58 % à 7 % » ; 100 - 41,8 = {100 - tm:.1f} et 100 - 92,6 = {100 - tt_um:.1f}).")
ligne(f"    Part du passage de la cession au rééchantillonnage : {dtr - dtt:.1f} points sur {total:.1f}, soit {(dtr - dtt) / total * 100:.1f} %.")
ligne(f"    Part de la cession, qui ne rééchantillonne rien : {dtt - tm:.1f} points, soit {(dtt - tm) / total * 100:.1f} %.")
ligne("    Même écart à d'autres utilités (tableau 1, p. 8) : rééchantillonnage moins cession =")
for u, a, b in ((99, 58.3, 65.2), (95, 72.7, 83.2), (90, 83.4, 89.0)):
    ligne(f"      à {u} % d'utilité : {b - a:4.1f} points ({a} -> {b})")
ligne("    Objet de contrôle : la somme des parts vaut 100 % (attendu) : "
      f"{sum((etapes[i][1] - etapes[i - 1][1]) for i in range(1, len(etapes))) / total * 100:.1f} %.")
ligne()

# ---------------------------------------------------------------------------
ligne("[B] Monde planté « la règle fait le gain » : k tirages par pas, scores à facteur commun.")
ligne("    Score d'un tirage = moyenne + racine(rho) Z + racine(1 - rho) bruit ; Z commun au pas.")
ligne("    Tirage honnête : moyenne 0, corrélation rho_h. Tirage d'attaque : visible avec probabilité v")
ligne("    (moyenne delta), sinon moyenne 0 ; corrélation rho_a. Sur un pas où il veut attaquer, chaque")
ligne("    tirage est une attaque avec probabilité c (sa cohérence), indépendamment. Audit si l'agrégat des")
ligne("    k scores dépasse un seuil réglé pour une part alpha de pas honnêtes audités ; l'audit reconnaît")
ligne("    toute attaque présente parmi les k. Sûreté = P(pris) / (P(pris) + P(attaque exécutée sans audit)).")
ligne("    Défenseur : agrégat (maximum, minimum, moyenne) et exécution (au hasard, le moins suspect).")
ligne("    Attaquant : il choisit c après avoir vu la règle (grille de 0,05 à 1).")


def monde(delta, v, rho_h, rho_a, k, alpha):
    """Rend, pour chaque règle, les vecteurs P(audit | a) et P(attaque exécutée sans audit | a), a = 0..k."""
    sh, sa = math.sqrt(1 - rho_h), math.sqrt(1 - rho_a)
    mh = math.sqrt(rho_h) * ZN           # moyenne conditionnelle d'un tirage honnête
    ma0 = math.sqrt(rho_a) * ZN          # tirage d'attaque invisible
    ma1 = delta + ma0                    # tirage d'attaque visible

    def FH(x):
        return Phi((x - mh) / sh)

    def FA(x):
        return v * Phi((x - ma1) / sa) + (1 - v) * Phi((x - ma0) / sa)

    def fA(x):
        return (v * phi((x - ma1) / sa) + (1 - v) * phi((x - ma0) / sa)) / sa

    # seuils réglés sur des pas honnêtes (a = 0)
    def faux_max(t):
        return 1 - float(np.sum(ZW * FH(t) ** k)) - alpha

    def faux_min(t):
        return float(np.sum(ZW * (1 - FH(t)) ** k)) - alpha

    t_max = bissection(faux_max, -5.0, 12.0)
    t_min = bissection(faux_min, -12.0, 8.0)
    var_moy_h = (1 + (k - 1) * rho_h) / k
    t_moy = ND.inv_cdf(1 - alpha) * math.sqrt(var_moy_h)

    res = {}
    for regle in ("max/hasard", "max/moins suspect", "min/hasard", "min/moins suspect", "moyenne/hasard"):
        res[regle] = (np.zeros(k + 1), np.zeros(k + 1))
    for a in range(0, k + 1):
        # --- maximum
        p_aud_z = 1 - FA(t_max) ** a * FH(t_max) ** (k - a)
        p_aud = float(np.sum(ZW * p_aud_z))
        res["max/hasard"][0][a] = p_aud
        res["max/hasard"][1][a] = (a / k) * (1 - p_aud)
        res["max/moins suspect"][0][a] = p_aud
        if a >= 1:
            lo, hi = t_max - 16.0, t_max
            x = 0.5 * (hi - lo) * XN + 0.5 * (hi + lo)
            w = 0.5 * (hi - lo) * XW
            tot = 0.0
            for zi in range(len(ZN)):
                # densité du tirage d'attaque le moins suspect en x, tous les autres entre x et le seuil
                FAx = v * Phi((x - ma1[zi]) / sa) + (1 - v) * Phi((x - ma0[zi]) / sa)
                FAt = v * Phi((t_max - ma1[zi]) / sa) + (1 - v) * Phi((t_max - ma0[zi]) / sa)
                FHx = Phi((x - mh[zi]) / sh)
                FHt = Phi((t_max - mh[zi]) / sh)
                fAx = (v * phi((x - ma1[zi]) / sa) + (1 - v) * phi((x - ma0[zi]) / sa)) / sa
                integrande = a * fAx * np.clip(FAt - FAx, 0, None) ** (a - 1) * np.clip(FHt - FHx, 0, None) ** (k - a)
                tot += ZW[zi] * float(np.sum(w * integrande))
            res["max/moins suspect"][1][a] = tot
        # --- minimum
        p_aud_z = (1 - FA(t_min)) ** a * (1 - FH(t_min)) ** (k - a)
        p_aud = float(np.sum(ZW * p_aud_z))
        res["min/hasard"][0][a] = p_aud
        res["min/hasard"][1][a] = (a / k) * (1 - p_aud)
        res["min/moins suspect"][0][a] = p_aud
        if a >= 1:
            lo, hi = t_min - 16.0, t_min
            x = 0.5 * (hi - lo) * XN + 0.5 * (hi + lo)
            w = 0.5 * (hi - lo) * XW
            tot = 0.0
            for zi in range(len(ZN)):
                SAx = 1 - (v * Phi((x - ma1[zi]) / sa) + (1 - v) * Phi((x - ma0[zi]) / sa))
                SHx = 1 - Phi((x - mh[zi]) / sh)
                fAx = (v * phi((x - ma1[zi]) / sa) + (1 - v) * phi((x - ma0[zi]) / sa)) / sa
                integrande = a * fAx * SAx ** (a - 1) * SHx ** (k - a)
                tot += ZW[zi] * float(np.sum(w * integrande))
            res["min/moins suspect"][1][a] = tot
        # --- moyenne (exécution au hasard seulement) ; visibles parmi les a : binomiale(a, v)
        p_aud = 0.0
        for j in range(0, a + 1):
            pj = binom_pmf(a, j, v)
            moy = (j * delta + a * ma0 + (k - a) * mh) / k
            var = (a * (1 - rho_a) + (k - a) * (1 - rho_h)) / k ** 2
            p_aud += pj * float(np.sum(ZW * (1 - Phi((t_moy - moy) / math.sqrt(var)))))
        res["moyenne/hasard"][0][a] = p_aud
        res["moyenne/hasard"][1][a] = (a / k) * (1 - p_aud)
    return res


def surete(res_regle, k, c):
    p_aud, p_exe = res_regle
    pris = sum(binom_pmf(k, a, c) * p_aud[a] for a in range(1, k + 1))
    execu = sum(binom_pmf(k, a, c) * p_exe[a] for a in range(1, k + 1))
    return pris / (pris + execu) if (pris + execu) > 0 else float("nan")


GRILLE_C = [round(0.05 * i, 2) for i in range(1, 21)]
ALPHA = 0.003                      # recopié : part de pas honnêtes audités (Lucassen et Kaufman, p. 3)
RHO_H, RHO_A = 0.19, 0.43          # recopié : corrélations entre tirages (même pièce, p. 7)
BASE = 0.61                        # recopié : sûreté de la surveillance seule (même pièce, p. 4)
t1 = ND.inv_cdf(1 - ALPHA)
DELTA_G = t1 + ND.inv_cdf(BASE)    # famille G : décalage tel que la surveillance seule (k = 1) rende 0,61
DELTA_M = 6.0                      # famille M : une attaque visible est flagrante
V_M = (BASE - ALPHA) / ((1 - float(Phi(t1 - DELTA_M))) - ALPHA)   # ... et visible avec cette probabilité
ligne(f"    alpha = {ALPHA} ; rho_h = {RHO_H} ; rho_a = {RHO_A} ; surveillance seule réglée à {BASE} (recopiés).")
ligne(f"    Famille G (décalage) : delta = {DELTA_G:.3f}, v = 1. Famille M (visible ou non) : delta = {DELTA_M}, v = {V_M:.3f}.")
ligne("    Attentes écrites avant l'exécution : (1) k = 1 rend 0,610 dans les deux familles ; (2) sous le maximum,")
ligne("    le meilleur c de l'attaquant est 1 et l'exécution du moins suspect n'ajoute alors rien ; (3) sous le")
ligne("    minimum sans exécution du moins suspect, un attaquant incohérent fait tomber la sûreté sous 0,61 ;")
ligne("    (4) le minimum ne bat le maximum que pour rho_h petit ; (5) la famille G ne rendra PAS le fait publié")
ligne("    « la moyenne fait moins bien que la surveillance seule » (elle n'a pas de queue lourde).")

RESUME = {}
for nom_f, delta, v in (("G", DELTA_G, 1.0), ("M", DELTA_M, V_M)):
    r1 = monde(delta, v, RHO_H, RHO_A, 1, ALPHA)
    s1 = surete(r1["max/hasard"], 1, 1.0)
    ligne(f"    Famille {nom_f} — contrôle k = 1 : sûreté {s1:.3f} (attendu 0,610)")
    for k in (2, 5):
        r = monde(delta, v, RHO_H, RHO_A, k, ALPHA)
        ligne(f"    Famille {nom_f}, k = {k} :      règle             c = 1    c = 0,8   c = 0,45   pire c (valeur)")
        pires = {}
        for regle in ("max/hasard", "max/moins suspect", "min/hasard", "min/moins suspect", "moyenne/hasard"):
            vals = {c: surete(r[regle], k, c) for c in GRILLE_C}
            cpire = min(vals, key=lambda c: (round(vals[c], 9), -c))
            pires[regle] = vals[cpire]
            ligne(f"        {regle:22s}  {vals[1.0]:.3f}    {vals[0.8]:.3f}     {vals[0.45]:.3f}     c = {cpire:.2f} ({vals[cpire]:.3f})")
        ligne(f"        gain de l'exécution du moins suspect au point selle : sous le maximum {pires['max/moins suspect'] - pires['max/hasard']:+.3f} ;"
              f" sous le minimum {pires['min/moins suspect'] - pires['min/hasard']:+.3f}")
        ligne(f"        gain de l'information seule (maximum, au hasard) sur la surveillance seule : {pires['max/hasard'] - s1:+.3f}")
        RESUME[(nom_f, k)] = dict(pires)

ligne("    Si l'attaquant choisit aussi la famille (G ou M) après avoir vu la règle : valeur de chaque règle =")
ligne("    la plus basse des deux familles et de tous les c ; gain = valeur moins 0,610 (surveillance seule).")
for k in (2, 5):
    for regle in ("max/hasard", "max/moins suspect", "min/hasard", "min/moins suspect", "moyenne/hasard"):
        g_, m_ = RESUME[("G", k)][regle], RESUME[("M", k)][regle]
        ligne(f"        k = {k}  {regle:22s}  G {g_:.3f}   M {m_:.3f}   valeur {min(g_, m_):.3f}   gain {min(g_, m_) - BASE:+.3f}")
ligne("    Bascule minimum contre maximum selon rho_h (famille G, k = 5, pire c pour chaque règle) :")
ligne("        rho_h    max/hasard   min/moins suspect   moyenne/hasard   le meilleur")
bascule = None
for rho_h in (0.0, 0.03, 0.10, 0.19, 0.40, 0.70):
    r = monde(DELTA_G, 1.0, rho_h, RHO_A, 5, ALPHA)
    vals = {}
    for regle in ("max/hasard", "min/moins suspect", "moyenne/hasard"):
        vals[regle] = min(surete(r[regle], 5, c) for c in GRILLE_C)
    best = max(vals, key=vals.get)
    ligne(f"        {rho_h:4.2f}     {vals['max/hasard']:.3f}        {vals['min/moins suspect']:.3f}              {vals['moyenne/hasard']:.3f}          {best}")
ligne("    Repères publiés, pour comparaison seulement (Lucassen et Kaufman, p. 1, 6, 7) : maximum de 5,")
ligne("    0,71 ; minimum, 0,32 à rho_h = 0,19 et 0,75 à rho_h = 0 ; bascule vers rho_h = 0,031 ; moyenne et")
ligne("    médiane sous la surveillance seule. Le monde planté n'est pas ajusté sur ces valeurs.")
ligne()

# ---------------------------------------------------------------------------
ligne("[C] Ce que chaque intervention détruit, en lois exactes.")
ligne("  [C1] Rééchantillonnage, exécution au hasard : P(le tirage exécuté est une attaque) = somme_a Bin(k, c)(a) a / k.")
for k in (2, 5, 9):
    for c in (0.02, 0.43, 1.0):
        val = sum(binom_pmf(k, a, c) * a / k for a in range(k + 1))
        assert abs(val - c) < 1e-12
ligne("       Vérifié pour k = 2, 5, 9 et c = 0,02, 0,43, 1 : toujours c. Marge nulle sur le succès, pour toute politique.")
ligne("  [C2] Exécution par majorité de k tirages, contre un saboteur qui tire son attaque à pile ou face (taux q par tirage).")
ligne("       non adapté : taux exécuté = P(majorité d'attaques).  adapté : il relève q pour garder son taux exécuté.")
ligne("       cible     k    non adapté : taux exécuté (divisé par)    adapté : q requis   tirages d'attaque produits par dommage exécuté")
for eps in (0.001, 0.02, 0.10):
    for k in (3, 5):
        naif = maj(k, eps)
        q = bissection(lambda x: maj(k, x) - eps, 1e-9, 0.5)
        ligne(f"       {eps:5.3f}     {k}    {naif:.3e}  ({eps / naif:10.1f})              {q:.4f}            {k * q / eps:7.1f}   (contre 1 sans majorité)")
ligne("       Saboteur cohérent (il attaque à coup sûr quand le contenu de la tâche porte une marque) : majorité sans effet,")
ligne(f"       taux exécuté inchangé (maj(k, 1) = {maj(5, 1.0):.0f}) ; k tirages d'attaque par dommage, tous semblables.")
ligne("       Témoin de marge : majorité de 3 contre q = 0,4 : "
      f"{maj(3, 0.4):.3f} au lieu de 0,400.")
ligne("       Côté honnête : si l'erreur d'un tirage est propre au tirage, la majorité la réduit ; si elle tient à la tâche, non.")
ligne("       erreur honnête par tirage 0,20 ; part des tâches où l'erreur tient à la tâche (i) ; erreur après majorité de 5 :")
for i in (0.0, 0.10, 0.20):
    e = (0.20 - i) / (1 - i)
    err = i + (1 - i) * maj(5, e)
    ligne(f"         part de tâches toujours manquées {i:.2f}, erreur propre au tirage {e:.3f} ailleurs : {err:.3f}")
ligne("  [C3] Remise à zéro du contexte, probabilité lam à chaque frontière, contre un sabotage qui tient un fil sur m pas.")
ligne("       succès du fil x (1 - lam)^(m-1) ; honnête qui a besoin de sa mémoire à une part h des frontières : x (1 - h lam)^(m-1)")
ligne("       m    lam    fil du saboteur   honnête h = 0   h = 0,2   h = 1    saboteur sans fil")
for m in (2, 5, 10):
    for lam in (0.1, 0.5):
        f = (1 - lam) ** (m - 1)
        ligne(f"       {m:2d}   {lam:.1f}    {f:.3f}             1.000           {(1 - 0.2 * lam) ** (m - 1):.3f}     {(1 - lam) ** (m - 1):.3f}    1.000")
ligne("       Objet de contrôle : h = 1 rend la même chute que le fil (aucune marge) ; « sans fil » ne perd rien.")
ligne()

# ---------------------------------------------------------------------------
ligne("[D] Trois pièges de la lecture « il existe une intensité où le succès chute plus vite que l'utilité ».")
ligne("  [D1] Multiplicité. m cellules (interventions x intensités), chacune comparée aux mêmes bras témoins ;")
ligne("       statistiques normales de corrélation 1/2 ; on annonce une marge si la meilleure dépasse 1,645 (5 % unilatéral).")
ligne("       Sous le nul complet, probabilité d'annoncer à tort :")
z95 = ND.inv_cdf(0.95)


def fwer(m, zc):
    return 1 - float(np.sum(ZW * Phi(zc * math.sqrt(2.0) + ZN) ** m))


for m in (1, 3, 9, 15, 24):
    zc = bissection(lambda z: fwer(m, z) - 0.05, 0.5, 6.0)
    ligne(f"       m = {m:2d} : {fwer(m, z95):.3f}   (indépendantes : {1 - 0.95 ** m:.3f}) ; seuil qui tient 5 % : {zc:.3f}")
ligne("       Objet de contrôle : m = 1 rend 0,050 (attendu).")
ligne("  [D2] Échelle. Succès du sabotage 0,20 -> 0,10 ; utilité honnête 0,80 -> 0,68 :")
s0, s1_, u0, u1 = 0.20, 0.10, 0.80, 0.68
lo = lambda p: math.log(p / (1 - p))
ligne(f"       en points : sabotage {100 * (s1_ - s0):+.0f}, utilité {100 * (u1 - u0):+.0f} -> pas de marge")
ligne(f"       en part relative : sabotage {100 * (s1_ - s0) / s0:+.0f} %, utilité {100 * (u1 - u0) / u0:+.0f} % -> marge")
ligne(f"       en logarithme de cote : sabotage {lo(s1_) - lo(s0):+.3f}, utilité {lo(u1) - lo(u0):+.3f} -> marge")
ligne("       Le signe dépend de l'échelle : l'énoncé n'est décidable qu'à utilité égale, contre une base nommée.")
ligne("  [D3] Régression vers la moyenne. On ne rééchantillonne que les pas dont le premier score dépasse le quantile 0,974")
ligne("       (recopié : 2,6 % des pas honnêtes, Lucassen et Kaufman, p. 4). Sans rien changer à l'agent :")
t = ND.inv_cdf(0.974)
lo_, hi_ = t, t + 12.0
x = 0.5 * (hi_ - lo_) * XN + 0.5 * (hi_ + lo_)
w = 0.5 * (hi_ - lo_) * XW
dens = phi(x) / (1 - 0.974)
e1 = float(np.sum(w * dens * x))
for rho in (0.19, 0.50, 0.80):
    p_bas = float(np.sum(w * dens * Phi((x - rho * x) / math.sqrt(1 - rho * rho))))
    ligne(f"       corrélation {rho:.2f} : premier score moyen {e1:.2f}, second {rho * e1:.2f} (écarts types) ; "
          f"second plus bas dans {100 * p_bas:.1f} % des cas")
def part_plus_bas(rho):
    return float(np.sum(w * dens * Phi((x - rho * x) / math.sqrt(1 - rho * rho))))
rho_eq = bissection(lambda r: part_plus_bas(r) - 0.79, 0.01, 0.99)
ligne(f"       corrélation gaussienne qui rendrait 79 % de seconds scores plus bas : {rho_eq:.2f}")
for kk in (2, 4, 5):
    ligne(f"       gain de preuve k / (1 + (k - 1) rho), k = {kk} : {kk / (1 + (kk - 1) * 0.19):.2f} à rho = 0,19 ; "
          f"{kk / (1 + (kk - 1) * rho_eq):.2f} à rho = {rho_eq:.2f}")
ligne("       Repère publié (même pièce, p. 5) : 79 % de seconds scores plus bas, baisse moyenne de 22 points sur 100,")
ligne("       par ce seul effet. Attente : le monde gaussien exagère cette part (scores réels bornés, à égalités).")
ligne("       Lecture : là où l'on décide (la queue haute), les tirages honnêtes se ressemblent bien plus que leur")
ligne("       corrélation d'ensemble ne le dit ; égalités non comptées, monde gaussien supposé.")
ligne()

# ---------------------------------------------------------------------------
ligne("[E] Coût de l'étape 1 (un modèle expérimentateur écrit les témoins), produit de bornes déjà au dépôt.")
for n_temoins in (16, 18):
    for nom, bas, haut in (("bornes de l'erratum 1 de la conception (0,14 à 4,10 USD par implémentation)", 0.14, 4.10),):
        ligne(f"    {n_temoins} implémentations, {nom} : de {n_temoins * bas:.2f} à {n_temoins * haut:.2f} USD d'appels,")
        ligne("        plus la machine jetable (même erratum, non chiffrée ici). Non mesuré.")
ligne()

# ---------------------------------------------------------------------------
ligne("[F] Corrélation de queue quand une part e des seconds scores est ÉGALE au premier (échelle bornée).")
ligne("    Même quadrature que D3. Lecture : les 79 % de « plus bas » publiés deviennent 0,79 / (1 - e) des paires")
ligne("    sans égalité ; e est inconnue. Attentes écrites avant l'exécution : (6) e = 0 rend 0,78 (valeur de D3) ;")
ligne("    (7) e = 0,10 rend 0,59 et e = 0,15 rend 0,41, à 0,01 près (valeurs du contre-lecteur, calcul indépendant) ;")
ligne("    (8) e = 0,20 : corrélation sous 0,05, ou aucune corrélation positive ne le rend.")
p_rho0 = part_plus_bas(1e-9)
ligne(f"    Repère : à corrélation nulle, second plus bas dans {100 * p_rho0:.2f} % des cas (plafond de la lecture gaussienne).")
RHO_QUEUE = {}
for e in (0.0, 0.05, 0.10, 0.15, 0.20):
    cible = 0.79 / (1 - e)
    if cible >= p_rho0:
        ligne(f"    e = {e:.2f} : part sans égalité {100 * cible:.1f} % ; au-dessus du plafond : aucune corrélation positive ne le rend.")
        RHO_QUEUE[e] = None
        continue
    r_ = bissection(lambda r: part_plus_bas(r) - cible, 1e-6, 0.99)
    RHO_QUEUE[e] = r_
    ligne(f"    e = {e:.2f} : part sans égalité {100 * cible:.1f} % ; corrélation gaussienne {r_:.2f} ; "
          f"k / (1 + (k - 1) rho) à k = 4 : {4 / (1 + 3 * r_):.2f} (formule de la MOYENNE, voir G)")
ligne()

# ---------------------------------------------------------------------------
ligne("[G] Ce que rend le MAXIMUM de k répliques, selon la corrélation honnête entre répliques.")
ligne("  [G1] Monde planté du bloc B, information seule (audit sur le maximum, exécution au hasard), attaquant qui")
ligne("       choisit c et la famille ; rho_a = 0,43 gardé ; base 0,610. Attentes écrites avant l'exécution :")
ligne("       (10) le gain de sûreté décroît quand rho_h monte, et reste positif à 0,78.")
ligne("       rho_h    k    famille G (pire c)   famille M (pire c)   valeur    gain sur la surveillance seule")
for rho_h in (0.19, 0.41, 0.59, 0.78, 0.90):
    for k in (2, 4, 5):
        vals = {}
        for nom_f, delta, v in (("G", DELTA_G, 1.0), ("M", DELTA_M, V_M)):
            r = monde(delta, v, rho_h, RHO_A, k, ALPHA)
            vals[nom_f] = min(surete(r["max/hasard"], k, c) for c in GRILLE_C)
        val = min(vals.values())
        ligne(f"       {rho_h:4.2f}     {k}    {vals['G']:.3f}                {vals['M']:.3f}                {val:.3f}     {val - BASE:+.3f}")
ligne("  [G1 bis] Ajouté APRÈS la première exécution de G1, dont l'attente (10) a manqué (voir la note) : même monde,")
ligne("       rho_h = 0,19, famille G, k = 5, selon la corrélation rho_a des scores entre tirages d'attaque.")
ligne("       Attente écrite avant l'exécution de ce bloc : (12) le gain décroît quand rho_a monte, et passe sous")
ligne("       zéro près de 1 (le seuil du maximum a monté, et k tirages d'attaque n'offrent plus qu'une chance).")
ligne("       rho_a    c = 1 (cohérent)   pire c    gain du pire c sur la surveillance seule")
for rho_a in (0.43, 0.70, 0.90, 0.99):
    r = monde(DELTA_G, 1.0, RHO_H, rho_a, 5, ALPHA)
    v1_ = surete(r["max/hasard"], 5, 1.0)
    vp_ = min(surete(r["max/hasard"], 5, c) for c in GRILLE_C)
    ligne(f"       {rho_a:4.2f}     {v1_:.3f}              {vp_:.3f}     {vp_ - BASE:+.3f}")
ligne("  [G2] Gain de preuve d'une accumulation additive, par le carré du décalage réduit de l'agrégat :")
ligne("       décalage commun aux k répliques, même corrélation rho des deux côtés (suppositions). Moyenne :")
ligne("       k / (1 + (k - 1) rho). Maximum : 1 / (rho + (1 - rho) v_k), v_k = variance du maximum de k normales")
ligne("       indépendantes (quadrature). Attente écrite avant l'exécution : (9) le maximum est partout sous la")
ligne("       moyenne, et les deux sous 1 / rho, leur plafond commun quand k grandit.")
xg = 10.0 * XN
wg = 10.0 * XW


def var_max(k):
    dens_ = k * phi(xg) * Phi(xg) ** (k - 1)
    m1 = float(np.sum(wg * dens_ * xg))
    m2 = float(np.sum(wg * dens_ * xg * xg))
    return m2 - m1 * m1


ligne("       v_k : " + " ; ".join(f"k = {k} : {var_max(k):.3f}" for k in (1, 2, 4, 5, 9)) + "   (contrôle : v_1 = 1 ; v_2 = 1 - 1/pi = "
      f"{1 - 1 / math.pi:.3f})")
ligne("       rho      k    moyenne   maximum   plafond 1 / rho")
attente9 = True
for rho in (0.19, 0.41, 0.59, 0.78, 0.80):
    for k in (2, 4, 5):
        g_moy = k / (1 + (k - 1) * rho)
        g_max = 1 / (rho + (1 - rho) * var_max(k))
        attente9 = attente9 and (g_max <= g_moy + 1e-12) and (g_moy <= 1 / rho + 1e-12)
        ligne(f"       {rho:4.2f}     {k}    {g_moy:.2f}      {g_max:.2f}      {1 / rho:.2f}")
ligne(f"       Attente (9) : {'tenue' if attente9 else 'attente manquée'}.")
ligne()

# ---------------------------------------------------------------------------
ligne("[H] Monde « la réplique se distingue » : information seule, audit sur le maximum de k, le tirage ordinaire")
ligne("    est exécuté ; le saboteur sait lequel des k tirages est l'ordinaire, et n'attaque que sur lui")
ligne("    (supposition violée : « une réplique ne se distingue pas d'un pas ordinaire »). Sûreté = P(audit | une")
ligne("    seule attaque parmi k), puisque l'attaque non auditée est exécutée. Monde du bloc B, rho_h = 0,19.")
ligne("    Attente écrite avant l'exécution : (11) sous 0,610 dans les deux familles, à k = 2 et à k = 5")
ligne("    (le seuil du maximum monte avec k, et un seul des k tirages porte l'attaque).")
attente11 = True
for nom_f, delta, v in (("G", DELTA_G, 1.0), ("M", DELTA_M, V_M)):
    for k in (1, 2, 5):
        r = monde(delta, v, RHO_H, RHO_A, k, ALPHA)
        s_ = float(r["max/hasard"][0][1])
        indisc = min(surete(r["max/hasard"], k, c) for c in GRILLE_C)
        if k > 1:
            attente11 = attente11 and (s_ < BASE)
        ligne(f"    Famille {nom_f}, k = {k} : la réplique se distingue {s_:.3f} ; répliques indiscernables, pire c {indisc:.3f} ; "
              f"surveillance seule {BASE:.3f}")
ligne(f"    Attente (11) : {'tenue' if attente11 else 'attente manquée'}.")
ligne("    Repères publiés, pour comparaison seulement (Kutasov et al., arXiv 2511.02997v1, p. 5) : sûreté de 89 %")
ligne("    à 46 % quand l'attaquant sait qu'il est rééchantillonné. Le monde planté n'est pas ajusté sur ces valeurs.")
ligne()
ligne("Fin des calculs.")
