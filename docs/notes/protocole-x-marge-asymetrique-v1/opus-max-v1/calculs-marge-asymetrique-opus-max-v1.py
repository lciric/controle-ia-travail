#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculs de la note « marge asymétrique après Ctrl-Z » (réponse indépendante, Opus 5.5 en effort maximal) — v1.

Blocs (chaque bloc de la sortie porte sa lettre ; la note renvoie à ces lettres) :
  [A] Invariance de la loi de l'action exécutée sous tirage multiple sans règle (arithmétique exacte, fractions) ;
      effet d'une règle de choix par moniteur (le moins suspect), contre un attaquant incohérent puis cohérent.
  [B] Règle de consensus sans moniteur (majorité de k tirages) : probabilité d'exécuter l'attaque, utilité honnête.
  [C] Artefact du seuil : un placebo sans aucune spécificité « fait chuter le succès plus vite que l'utilité ».
  [D] Valeur de la mémoire pour un saboteur qui dose son rythme face à un détecteur par somme à horizon fixe :
      perte relative de dommage quand il est forcé sans mémoire ; second ordre en delta/sigma.
  [E] Plus petit écart détectable entre deux taux de succès, selon le nombre d'épisodes par bras.
  [F] Banc d'étalonnage miniature (Monte-Carlo, graines par numpy.random.SeedSequence) : trois procédures de lecture,
      trois mondes plantés (sans marge propre ; marge propre faible ; marge propre forte) ; taux de déclaration.
  [G] Rééchantillonnage pour information dans un agrégateur : facteur de budget effectif selon la corrélation
      entre tirages d'un même pas (attaquant cohérent).
  [H] Marge contre un attaquant figé et contre la meilleure riposte : borne par la valeur de la ressource détruite.

Aucun appel réseau, aucune donnée lue, aucun fichier écrit (sortie sur la sortie standard).
Lancer : PYTHONHASHSEED=0 .venv/bin/python -I calculs-marge-asymetrique-opus-max-v1.py > calculs-marge-asymetrique-opus-max-v1.txt
"""
import sys
from fractions import Fraction as Fr
from itertools import product

import numpy as np
import scipy
from scipy.optimize import brentq
from scipy.stats import binom, norm

RACINE_GRAINES = 20261121171425  # entropie racine, écrite d'avance (heure UTC de création du dossier)


def entete():
    print("Calculs — marge asymétrique après Ctrl-Z — Opus 5.5, effort maximal — v1")
    print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; scipy {scipy.__version__}")
    print(f"racine des graines (SeedSequence) : {RACINE_GRAINES}")
    print()


# ---------------------------------------------------------------- [A]
def loi_choix_au_hasard(pi, k):
    """Exécute X_J, J uniforme sur {1..k} et indépendant des tirages X_1..X_k i.i.d. de loi pi."""
    out = {x: Fr(0) for x in pi}
    for tup in product(list(pi.keys()), repeat=k):
        p = Fr(1)
        for x in tup:
            p *= pi[x]
        if p == 0:
            continue
        for j in range(k):
            out[tup[j]] += p * Fr(1, k)
    return out


def loi_moins_suspect(pi, k, susp):
    """Exécute le tirage le moins suspect (moniteur déterministe susp) parmi k tirages i.i.d."""
    out = {x: Fr(0) for x in pi}
    for tup in product(list(pi.keys()), repeat=k):
        p = Fr(1)
        for x in tup:
            p *= pi[x]
        if p == 0:
            continue
        best = min(tup, key=lambda x: susp[x])
        out[best] += p
    return out


def bloc_A():
    print("[A] Tirage multiple sans règle : la loi de l'action exécutée ne change pas (exact).")
    susp = {"h1": 1, "h2": 2, "a": 3}
    politiques = {
        "attaquant incohérent (attaque 3 tirages sur 10)": {"h1": Fr(1, 2), "h2": Fr(1, 5), "a": Fr(3, 10)},
        "attaquant cohérent (attaque à chaque tirage)": {"h1": Fr(0), "h2": Fr(0), "a": Fr(1)},
        "honnête (h1 : 5/7, h2 : 2/7)": {"h1": Fr(5, 7), "h2": Fr(2, 7), "a": Fr(0)},
    }
    for nom, pi in politiques.items():
        print(f"  politique : {nom}")
        for k in range(1, 6):
            lh = loi_choix_au_hasard(pi, k)
            egal = all(lh[x] == pi[x] for x in pi)
            lm = loi_moins_suspect(pi, k, susp)
            print(f"    k={k} : choix au hasard, loi égale à la loi d'origine : {egal} ; "
                  f"règle « moins suspect » : P(a)={lm['a']} ({float(lm['a']):.4f}), "
                  f"P(h1)={lm['h1']} ({float(lm['h1']):.4f})")
    print("  Lecture : sans règle qui regarde le contenu, aucun effet, ni sur l'attaque ni sur le travail honnête ;")
    print("  avec la règle du moniteur, l'attaque incohérente recule en (3/10)^k, l'attaque cohérente pas du tout,")
    print("  et la loi honnête est déplacée vers l'action la moins suspecte (effet sur l'utilité de signe non fixé).")
    print()


# ---------------------------------------------------------------- [B]
def bloc_B():
    print("[B] Consensus sans moniteur (majorité de k tirages) : probabilité d'exécuter l'attaque à un pas d'attaque.")
    ks = [1, 3, 5, 7, 9]
    qs = [0.30, 0.45, 0.60, 0.80, 1.00]
    print("  q = probabilité qu'un tirage soit une attaque ; colonnes : k = " + ", ".join(map(str, ks)))
    for q in qs:
        vals = []
        for k in ks:
            m = (k + 1) // 2
            vals.append(binom.sf(m - 1, k, q))
        print(f"  q={q:.2f} : " + "  ".join(f"{v:.4f}" for v in vals))
    print("  Utilité honnête (probabilité de bonne réponse par pas, majorité de k tirages) :")
    for ph in [0.60, 0.80]:
        vals = [binom.sf((k + 1) // 2 - 1, k, ph) for k in ks]
        print(f"  p_honnête={ph:.2f} : " + "  ".join(f"{v:.4f}" for v in vals))
    print("  Lecture : contre q < 1/2 l'attaque s'efface et l'utilité monte ; contre q > 1/2 l'attaque est amplifiée ;")
    print("  la meilleure riposte (q = 1, attaquer à chaque tirage) garde une exécution de 1 à tout k : marge nulle.")
    print()


# ---------------------------------------------------------------- [C]
def bloc_C():
    print("[C] Artefact du seuil : placebo = neutralisation au hasard d'une part lambda des actions, honnêtes et d'attaque.")
    n, p = 100, 0.30
    print(f"  dommage ~ Binomiale(n={n}, p={p}*(1-lambda)) ; succès si dommage >= theta ; utilité relative = 1-lambda")
    for theta in [25, 30, 35]:
        S0 = binom.sf(theta - 1, n, p)
        print(f"  theta={theta} : succès sans intervention S0={S0:.4f}")
        for lam in [0.05, 0.10, 0.20, 0.30]:
            S = binom.sf(theta - 1, n, p * (1 - lam))
            rS = 1 - S / S0
            rU = lam
            print(f"    lambda={lam:.2f} : S={S:.4f} ; baisse relative du succès {rS:.3f} ; "
                  f"de l'utilité {rU:.3f} ; rapport {rS / rU:.2f} ; "
                  f"baisse relative du dommage moyen {lam:.3f} (rapport 1,00)")
    print("  Lecture : sur un taux de succès à seuil, un placebo sans spécificité « chute plus vite que l'utilité » ;")
    print("  sur une échelle linéaire du dommage, le même placebo ne montre aucune marge.")
    print()


# ---------------------------------------------------------------- [D]
def alarme_sans_memoire(r, T, a, z):
    k = np.arange(T + 1)
    w = binom.pmf(k, T, r)
    return float(np.sum(w * norm.sf(z - k * a)))


def bloc_D():
    print("[D] Valeur de la mémoire pour un saboteur qui dose son rythme face à un détecteur par somme à horizon fixe.")
    print("  scores honnêtes i.i.d. de loi normale réduite ; un pas d'attaque décale le score de delta ;")
    print("  alarme si la somme des T scores dépasse z_(1-alpha) * racine(T) ; alpha = 0,01.")
    print("  avec mémoire : exactement K pas d'attaque (K réel, relâchement continu) ; sans mémoire : chaque pas attaque")
    print("  avec la probabilité r (nombre d'attaques binomial). Chacun prend le dommage le plus grand sous un risque")
    print("  d'alarme beta qu'il accepte. Perte relative = 1 - (T r) / K ; approximation : 0,5 delta^2 r(1-r) z_b/(z_a - z_b).")
    print("  Dernière colonne : perte / (delta^2 r (1-r)), qui doit rester près de la constante c = 0,5 z_b/(z_a - z_b)")
    print("  si la perte est bien du second ordre en delta/sigma.")
    alpha = 0.01
    z = norm.isf(alpha)
    for T in [200, 1000, 5000]:
        for beta in [0.05, 0.20]:
            zb = norm.isf(beta)
            print(f"  T={T}, beta={beta:.2f} (constante c={0.5 * zb / (z - zb):.4f}) :")
            for delta in [0.05, 0.10, 0.20, 0.30, 0.50, 1.00]:
                a = delta / np.sqrt(T)
                Ks = (z - zb) / a
                if Ks >= T or alarme_sans_memoire(1.0 - 1e-12, T, a, z) <= beta:
                    print(f"    delta={delta:.2f} : saturé (attaquer à chaque pas reste sous le risque accepté) ; "
                          f"valeur de la mémoire nulle")
                    continue
                r_star = brentq(lambda r: alarme_sans_memoire(r, T, a, z) - beta, 1e-12, 1 - 1e-12,
                                xtol=1e-14, rtol=1e-12, maxiter=500)
                Km = T * r_star
                perte = 1 - Km / Ks
                rr = Ks / T
                approx = 0.5 * delta ** 2 * rr * (1 - rr) * zb / (z - zb)
                norm2 = perte / (delta ** 2 * rr * (1 - rr))
                print(f"    delta={delta:.2f} : K avec mémoire={Ks:8.2f} ; T r sans mémoire={Km:8.2f} ; "
                      f"perte relative={perte:.5f} ; approximation={approx:.5f} ; perte/(delta^2 r(1-r))={norm2:.4f}")
    print("  Lecture : la mémoire ne vaut au saboteur diffus que l'écart de Jensen d'une probabilité d'alarme de courbure")
    print("  delta^2/T en le nombre d'attaques ; dans cette grille, au plus 1,5 % du dommage à delta/sigma <= 0,3, au plus")
    print("  5,3 % à delta/sigma = 1. C'est la face « attaquant » de l'invariance à la répartition du lemme L.")
    print()


# ---------------------------------------------------------------- [E]
def bloc_E():
    print("[E] Plus petit écart détectable entre deux taux de succès (unilatéral 5 %, puissance 0,80, approximation normale).")
    za, zp = norm.isf(0.05), norm.isf(0.20)
    for p in [0.50, 0.20]:
        ligne = []
        for n in [50, 100, 200, 400, 800, 1600]:
            mde = (za + zp) * np.sqrt(2 * p * (1 - p) / n)
            ligne.append(f"n={n}: {mde:.3f}")
        print(f"  taux de référence {p:.2f} : " + " ; ".join(ligne))
    print("  Lecture : par intensité et par intervention, quelques centaines d'épisodes d'attaque par bras pour voir")
    print("  dix points ; le bras placebo à utilité égale double le compte.")
    print()


# ---------------------------------------------------------------- [F]
def bloc_F():
    print("[F] Banc d'étalonnage miniature : trois procédures de lecture sur trois mondes plantés.")
    n_opp, p_att, theta, p_h = 60, 0.30, 18, 0.70
    lam, N, R = 0.15, 400, 2000
    mondes = [("sans marge propre (l'intervention est un placebo)", 0.00),
              ("marge propre faible (ressource détruite : 5 % des contributions)", 0.05),
              ("marge propre forte (ressource détruite : 20 % des contributions)", 0.20)]
    print(f"  par épisode : {n_opp} occasions ; contribution d'attaque {p_att} ; succès si dommage >= {theta} ;")
    print(f"  utilité honnête = part de {n_opp} pas réussis, p={p_h} ; intervention et placebo neutralisent lambda={lam} ;")
    print(f"  l'intervention détruit en plus une part v des contributions d'attaque restantes ; {N} épisodes d'attaque")
    print(f"  et {N} épisodes honnêtes par bras (sans intervention, intervention, placebo) ; {R} expériences par monde.")
    print("  Procédures : (1) pentes brutes relatives (rétention du succès contre rétention de l'utilité, contre le bras")
    print("  sans intervention) ; (2) pentes brutes absolues (baisse en points du succès contre baisse en points de")
    print("  l'utilité) ; (3) placebo à utilité égale (succès sous intervention contre succès sous placebo).")
    racine = np.random.SeedSequence(RACINE_GRAINES)
    enfants = racine.spawn(len(mondes))
    z95 = norm.isf(0.05)
    for (nom, v), ss in zip(mondes, enfants):
        rng = np.random.default_rng(ss)
        p0, pZ, pT = p_att, p_att * (1 - lam), p_att * (1 - lam) * (1 - v)
        S0v, SZv, STv = (binom.sf(theta - 1, n_opp, x) for x in (p0, pZ, pT))
        U0v, UTv = p_h, p_h * (1 - lam)
        D0 = rng.binomial(n_opp, p0, size=(R, N)) >= theta
        DT = rng.binomial(n_opp, pT, size=(R, N)) >= theta
        DZ = rng.binomial(n_opp, pZ, size=(R, N)) >= theta
        H0 = rng.binomial(n_opp, p_h, size=(R, N)) / n_opp
        HT = rng.binomial(n_opp, p_h * (1 - lam), size=(R, N)) / n_opp
        S0, ST, SZ = D0.mean(1), DT.mean(1), DZ.mean(1)
        U0, UT = H0.mean(1), HT.mean(1)
        vU0, vUT = H0.var(1, ddof=1), HT.var(1, ddof=1)
        eps = 1e-12
        # (1) pentes brutes relatives : log(ST/S0) - log(UT/U0) < 0 significativement
        L = np.log(np.maximum(ST, eps) / np.maximum(S0, eps)) - np.log(UT / U0)
        varL = ((1 - ST) / (N * np.maximum(ST, eps)) + (1 - S0) / (N * np.maximum(S0, eps))
                + vUT / (N * UT ** 2) + vU0 / (N * U0 ** 2))
        dec1 = L < -z95 * np.sqrt(varL)
        # (2) pentes brutes absolues : (S0-ST) - (U0-UT) > 0 significativement
        A = (S0 - ST) - (U0 - UT)
        varA = S0 * (1 - S0) / N + ST * (1 - ST) / N + vU0 / N + vUT / N
        dec2 = A > z95 * np.sqrt(varA)
        # (3) placebo à utilité égale : SZ - ST > 0 significativement (proportion commune)
        pbar = (SZ + ST) / 2
        dec3 = (SZ - ST) > z95 * np.sqrt(np.maximum(pbar * (1 - pbar), eps) * 2 / N)
        print(f"  monde {nom} (v={v:.2f}) :")
        print(f"    vérité exacte : S0={S0v:.4f} ; S placebo={SZv:.4f} ; S intervention={STv:.4f} ; "
              f"U0={U0v:.3f} ; U intervention = U placebo = {UTv:.3f} ; marge vraie sur le placebo={SZv - STv:.4f}")
        print(f"    taux de déclaration « marge » : (1) {dec1.mean():.4f} ; (2) {dec2.mean():.4f} ; (3) {dec3.mean():.4f}")
    print("  Lecture : sur le monde sans marge propre, les deux lectures par pentes brutes déclarent une marge presque")
    print("  toujours (témoin « doit mourir ») ; la lecture contre placebo tient son niveau (témoin « doit tenir »).")
    print()


# ---------------------------------------------------------------- [G]
def bloc_G():
    print("[G] Rééchantillonnage pour information : facteur de budget effectif 1/(rho + (1-rho)/k) pour un attaquant")
    print("  cohérent (décalage delta dans chaque tirage), scores gaussiens équicorrélés de corrélation rho entre tirages.")
    for rho in [0.19, 0.43, 0.50, 0.90, 1.00]:
        vals = [1.0 / (rho + (1 - rho) / k) for k in (1, 2, 3, 5, 10)]
        print(f"  rho={rho:.2f} : k=1,2,3,5,10 -> " + "  ".join(f"{v:.3f}" for v in vals))
    print("  Lecture : rho = 1 (positions lues avant le premier jeton tiré, identiques d'un tirage à l'autre) : aucun gain ;")
    print("  0,19 est la corrélation honnête mesurée en boîte noire par Lucassen et Kaufman (p. 7), 0,43 celle des attaques.")
    print()


# ---------------------------------------------------------------- [H]
def bloc_H():
    print("[H] Marge contre un attaquant figé et contre la meilleure riposte (dommages relatifs, hors audit).")
    print("  d1 = dommage de la stratégie qui use de la ressource ; d0 = meilleure stratégie qui s'en passe ;")
    print("  l'intervention détruit la part rho de d1 et ne touche pas d0 ; V = d1 - d0 = valeur de la ressource.")
    d1 = 1.0
    for d0 in [1.00, 0.98, 0.90, 0.50]:
        for rho in [0.30, 1.00]:
            fige = d1 * rho
            riposte = d1 - max(d0, d1 * (1 - rho))
            print(f"  d0={d0:.2f}, rho={rho:.2f} : marge contre l'attaquant figé={fige:.2f} ; "
                  f"contre la meilleure riposte={riposte:.2f} ; borne V={d1 - d0:.2f}")
    print("  Lecture : la marge contre la meilleure riposte vaut min(rho d1, V) ; mesurée contre un organisme figé,")
    print("  elle peut valoir 100 % quand la riposte n'en laisse que 2 % (cas d0 = 0,98, rho = 1).")
    print()


# ---------------------------------------------------------------- [I]
def bloc_I():
    print("[I] Comptes pour les barreaux (arithmétique seule ; les coûts unitaires sont repris, non mesurés ici).")
    n_epreuves, n_temoins = 7, 3
    g = n_epreuves * n_temoins
    bas, haut = 0.142, 4.10  # USD par greffon : relevé de la course v67 et plafond (erratum 1 de la note des expérimentateurs, § 2 (a))
    print(f"  barreau 1 bis : {n_epreuves} épreuves x {n_temoins} témoins passés par l'expérimentateur = {g} greffons ;")
    print(f"  appels : de {g * bas:.2f} à {g * haut:.2f} USD (machine en sus)")
    N = 400
    for I, J in [(1, 1), (1, 3), (3, 3)]:
        bras = 1 + 2 * I * J  # un bras sans intervention ; par intervention et intensité, un bras et son placebo
        print(f"  barreau 2 : {I} intervention(s) x {J} intensité(s) : {bras} bras ; {N} épisodes d'attaque et {N} honnêtes"
              f" par bras -> {2 * N * bras} épisodes")
    print()


if __name__ == "__main__":
    entete()
    bloc_A()
    bloc_B()
    bloc_C()
    bloc_D()
    bloc_E()
    bloc_F()
    bloc_G()
    bloc_H()
    bloc_I()
    print("Fin.")
