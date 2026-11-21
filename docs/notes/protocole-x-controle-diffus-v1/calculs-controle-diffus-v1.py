#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « changer de programme ou contre-attaquer » (protocole X, contrôle diffus), v1.

Lois exactes et quadratures déterministes ; aucun tirage ; aucune donnée du programme.
Deux sortes d'entrées, toujours marquées dans la sortie :
  [imprimé]  valeur lue sur un PDF ou une copie de page empreintés, page dite ;
  [supposé]  supposition d'illustration, de l'auteur de la note.
Rejouer :  python3 -I calculs-controle-diffus-v1.py > calculs-controle-diffus-v1.txt
Bibliothèque standard seule (math, statistics).
"""
import math
from statistics import NormalDist

N01 = NormalDist()
PHI = N01.cdf
PHI_INV = N01.inv_cdf

ALPHA = 0.01   # fausse alarme tolérée, unilatérale  [supposé]
PUISS = 0.90   # puissance visée                      [supposé]
Z_A = PHI_INV(1.0 - ALPHA)
Z_B = PHI_INV(PUISS)


def titre(t):
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)


# ----------------------------------------------------------------------------------------------
# Bloc A — la condition de Hebbar en formule
# ----------------------------------------------------------------------------------------------
def d_de_aire(a):
    """Écart standardisé d'un moniteur binormal à variances égales d'aire sous la courbe a."""
    return math.sqrt(2.0) * PHI_INV(a)


def n_necessaire(p, d, s):
    """Nombre d'actions pour annoncer, au niveau ALPHA avec la puissance PUISS, un mélange où une
    part p des actions est déplacée de d écarts types, quand la référence honnête n'est connue
    qu'à s écart type près (le test doit rester valide pour tout décalage de 0 à s).
    Approximation normale de la moyenne. Rend inf si p*d <= s."""
    marge = p * d - s
    if marge <= 0.0:
        return math.inf
    et_alt = math.sqrt(1.0 + p * (1.0 - p) * d * d)
    return ((Z_A + Z_B * et_alt) / marge) ** 2


def fausse_alarme(n, s):
    """Fausse alarme d'un test qui croit la référence exacte alors qu'elle est décalée de s."""
    return 1.0 - PHI(Z_A - s * math.sqrt(n))


def n_paires(p, d, rho):
    """Même question, par paires agent / jumeau sur la même tâche ; rho = corrélation honnête
    entre les deux scores d'une même tâche. La référence s'annule si le jumeau vaut l'honnête."""
    v0 = 2.0 * (1.0 - rho)
    v1 = v0 + p * (1.0 - p) * d * d
    return ((Z_A * math.sqrt(v0) + Z_B * math.sqrt(v1)) / (p * d)) ** 2


def fmt_n(x):
    if math.isinf(x):
        return "jamais"
    if x >= 1e6:
        return "%.1e" % x
    return "%d" % math.ceil(x)


def bloc_a():
    titre("BLOC A — La condition de Hebbar en formule : ce que l'accumulation exige de la référence honnête")
    print("Modèle [supposé] : score de suspicion par action, honnête N(0,1) ; action sabotée N(d,1) ;")
    print("une part p des actions est sabotée ; la moyenne honnête n'est connue qu'à s près.")
    print("Niveau %.2f unilatéral, puissance %.2f : z = %.4f + %.4f." % (ALPHA, PUISS, Z_A, Z_B))
    print()
    moniteurs = [
        (0.60, "moniteur faible [supposé]"),
        (0.63, "sonde sur l'organisme de sous-rendement en mathématiques [imprimé : Hollinsworth et al., 2610.12445v1, p. 9]"),
        (0.77, "meilleur auditeur de code, par dépôt [imprimé : Gan et al., 2604.16286v2, p. 1]"),
        (0.959, "sonde interne non publiée, 16 exemples, sans adversaire [imprimé : Gan et al., p. 24]"),
        (0.988, "sondes sur sabotage concentré d'agent [imprimé : Hollinsworth et al., p. 1]"),
    ]
    print("A1. Écart standardisé d = sqrt(2) * Phi^-1(aire) :")
    for a, nom in moniteurs:
        print("    aire %.3f -> d = %.3f   %s" % (a, d_de_aire(a), nom))
    print()
    parts = [0.5, 0.1, 0.02]
    erreurs = [0.0, 0.02, 0.05, 0.10, 0.20]
    print("A2. Actions nécessaires selon l'erreur s de la référence (en écarts types) ; « jamais » = aucun horizon ne suffit.")
    print("    %-7s %-6s %-9s " % ("aire", "p", "p*d") + " ".join("s=%-9.2f" % s for s in erreurs))
    for a, _ in moniteurs:
        d = d_de_aire(a)
        for p in parts:
            ligne = "    %-7.3f %-6.2f %-9.4f " % (a, p, p * d)
            ligne += " ".join("%-11s" % fmt_n(n_necessaire(p, d, s)) for s in erreurs)
            print(ligne)
    print()
    print("A3. Fausse alarme d'un test qui croit sa référence exacte, quand elle est décalée de s (modèle honnête) :")
    print("    %-10s " % "n" + " ".join("s=%-8.2f" % s for s in (0.02, 0.05, 0.10)))
    for n in (100, 1000, 10000, 100000):
        print("    %-10d " % n + " ".join("%-10.4f" % fausse_alarme(n, s) for s in (0.02, 0.05, 0.10)))
    print("    Plus on accumule, plus la fausse alarme est certaine : c'est « no amount of mildly suspicious actions is enough ».")
    print()
    print("A4. Référence estimée sur m actions honnêtes (s = 0) : excès minimal visible à horizon infini = (z_a+z_b)/sqrt(m).")
    print("    %-8s %-12s %-28s %-28s" % ("m", "p*d minimal", "p minimal si aire 0,77", "p minimal si aire 0,959"))
    for m in (100, 1000, 10000, 100000):
        e = (Z_A + Z_B) / math.sqrt(m)
        print("    %-8d %-12.4f %-28.4f %-28.4f" % (m, e, min(1.0, e / d_de_aire(0.77)), min(1.0, e / d_de_aire(0.959))))
    print("    L'horizon au-delà de m n'achète rien : c'est la règle « horizon au plus m » d'une accumulation.")
    print()
    print("A5. Paires agent / jumeau sur la même tâche (référence annulée si le jumeau vaut l'honnête) : paires nécessaires.")
    print("    %-7s %-6s " % ("aire", "p") + " ".join("rho=%-7.1f" % r for r in (0.0, 0.5, 0.8)) + "  (sans paire, s=0)")
    for a in (0.77, 0.959):
        d = d_de_aire(a)
        for p in parts:
            print("    %-7.3f %-6.2f " % (a, p) + " ".join("%-11s" % fmt_n(n_paires(p, d, r)) for r in (0.0, 0.5, 0.8))
                  + "  " + fmt_n(n_necessaire(p, d, 0.0)))
    print()
    # Objets de contrôle du bloc A (attendus écrits avant l'exécution).
    assert abs(d_de_aire(0.5)) < 1e-12                       # moniteur au hasard : aucun écart
    assert math.isinf(n_necessaire(0.1, 1.0, 0.1))           # référence aussi fausse que l'excès : jamais
    assert abs(fausse_alarme(10, 0.0) - ALPHA) < 1e-12       # référence exacte : niveau tenu
    assert abs(n_paires(0.1, 1.0, 0.5) - n_necessaire(0.1, 1.0, 0.0)) < 1e-9  # rho = 0,5 : la paire ne coûte rien
    print("Contrôles A : aire 0,5 -> d = 0 ; s = p*d -> jamais ; s = 0 -> fausse alarme = niveau ; rho = 0,5 -> même n. Tenus.")


# ----------------------------------------------------------------------------------------------
# Bloc B — ce que les chiffres imprimés du papier disent de son banc
# ----------------------------------------------------------------------------------------------
def bloc_b():
    titre("BLOC B — Le banc du papier, d'après ses chiffres imprimés (2606.08892v3)")
    # [imprimé] figure 9, haut gauche, p. 19 : variance de la vérité approchée (avec l'article), unités de score au carré
    v_gen, v_tache, v_tirage, v_juge = 127.0, 29.0, 9.0, 20.0
    total = v_gen + v_tache + v_tirage + v_juge
    print("B1. Variance de la vérité approchée [imprimé : figure 9, p. 19] : générateur %.0f, tâche %.0f, tirage du générateur %.0f, bruit du juge %.0f ; somme %.0f (imprimée : 186)."
          % (v_gen, v_tache, v_tirage, v_juge, total))
    print("    Parts : %.1f %%, %.1f %%, %.1f %%, %.1f %% (imprimées, figure 3, p. 5 : 68, 16, 5, 11)."
          % (100 * v_gen / total, 100 * v_tache / total, 100 * v_tirage / total, 100 * v_juge / total))
    et_fixe = math.sqrt(v_tirage + v_juge)
    print("B2. À générateur et tâche fixés, une lecture de la vérité approchée a un écart type de %.2f points ;" % et_fixe)
    print("    part due au seul bruit du juge : %.0f %%." % (100 * v_juge / (v_tirage + v_juge)))
    for k in (1, 2, 4, 8):
        fiab = v_tirage / (v_tirage + v_juge / k)
        print("    %d lecture(s) moyennée(s) : fiabilité %.2f, corrélation plafond d'un lecteur parfait du produit %.2f."
              % (k, fiab, math.sqrt(fiab)))
    fiab_t = (v_tache + v_tirage) / (v_tache + v_tirage + v_juge)
    print("    À générateur fixé, tâches variées : fiabilité %.2f, plafond %.2f." % (fiab_t, math.sqrt(fiab_t)))
    # [imprimé] tableau de la figure 1, p. 2 ; figure 4, p. 6
    g_fort, g_attaque, g_faible = 70.7, 34.7, 39.3
    w_fort, w_attaque = 80.8, 85.3
    w_max, w_seuil = 88.4, 84.8
    eps = w_max - w_seuil
    chute = g_fort - g_attaque
    print("B3. Attaque publiée [imprimé : figure 1, p. 2 ; figure 4, p. 6] : vérité approchée %.1f -> %.1f (chute %.1f), juge faible %.1f -> %.1f ; marge eps = %.1f."
          % (g_fort, g_attaque, chute, w_fort, w_attaque, eps))
    d_att = chute / et_fixe
    print("    En écarts types d'une lecture à tâche fixée : %.1f ; aire sous la courbe d'UNE lecture de la vérité approchée sur UN produit : %.6f."
          % (d_att, PHI(d_att / math.sqrt(2.0))))
    # [imprimé] figure 9, bas gauche, p. 19, lue sur l'image de la page : variance propre au modèle fort (avec l'article) = 59
    v_fort = 59.0
    print("    Avec la dispersion propre au modèle fort, tâches variées [imprimé : figure 9, bas gauche, p. 19, lue sur image : %.0f] : écart type %.2f, chute de %.1f écarts types."
          % (v_fort, math.sqrt(v_fort), chute / math.sqrt(v_fort)))
    print("    Le produit saboté n'est pas subtil pour qui a la vérité : la difficulté est l'oracle absent, non l'indice faible.")
    print("    Rapport des écarts d'un moniteur d'aire 0,959 et d'un moniteur d'aire 0,77 : %.2f." % (d_de_aire(0.959) / d_de_aire(0.77)))
    n_res = (Z_A + Z_B) ** 2 * (v_tirage + v_juge) / (eps ** 2)
    print("B4. Sous un juge durci, il reste au plus de l'ordre de eps = %.1f points : %.2f écart type par produit ; le voir demanderait %d lectures de vérité."
          % (eps, eps / et_fixe, math.ceil(n_res)))
    # [imprimé] p. 8 : environ 75 contre environ 80 ; figure 5, p. 7 : 64,2 et 67,6
    print("B5. Prix imprimé du juge durci chez un modèle honnête : environ 75 au lieu d'environ 80 (p. 8), soit de l'ordre de %.0f %%." % (100 * (80 - 75) / 80.0))
    # [imprimé] README du dépôt de code, copie empreintée : environ 5 dollars par article
    prix = 5.0
    print("B6. Reconstruire leurs tâches [imprimé : README du dépôt public, copie empreintée] : environ %.0f USD par article." % prix)
    for n_art in (32, 128, 302, 2642):
        print("    %5d articles : environ %6.0f USD (hors générations et notations des essais)." % (n_art, prix * n_art))
    assert abs(total - 185.0) < 1e-9          # la somme des quatre termes imprimés vaut 185, la figure imprime 186 (arrondis)
    assert abs(eps - 3.6) < 1e-9
    print("Contrôles B : somme des termes imprimés = 185 pour 186 imprimé (arrondis) ; eps = 3,6 retrouvé. Tenus.")
    return dict(eps=eps, w_max=w_max, w_attaque=w_attaque, g_attaque=g_attaque)


# ----------------------------------------------------------------------------------------------
# Bloc C — le vérificateur au niveau de la politique : combien d'adaptateurs bénins témoins
# ----------------------------------------------------------------------------------------------
def _simpson(f, a, b, n):
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4.0 if i % 2 else 2.0)
    return s * h / 3.0


def puissance_t(delta, nu, tcrit, n=6000):
    """P(T > tcrit) pour un t décentré (décentrage delta, nu degrés de liberté), par quadrature sur
    la loi du khi (changement de variable v = x^2, sans singularité)."""
    logc = math.log(2.0) - (nu / 2.0) * math.log(2.0) - math.lgamma(nu / 2.0)
    racine_nu = math.sqrt(nu)

    def f(x):
        if x <= 0.0:
            return (math.exp(logc) * (1.0 - PHI(-delta))) if nu == 1 else 0.0
        dens = math.exp(logc + (nu - 1.0) * math.log(x) - 0.5 * x * x)
        return dens * (1.0 - PHI(tcrit * x / racine_nu - delta))
    return _simpson(f, 0.0, racine_nu + 14.0, n)


def t_critique(nu, alpha):
    lo, hi = 0.0, 5000.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if puissance_t(0.0, nu, mid) > alpha:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def bloc_c():
    titre("BLOC C — Dire « cet adaptateur sabote » contre des adaptateurs bénins de même recette : nombre de témoins")
    print("Modèle [supposé] : la lecture moyenne d'un adaptateur bénin j vaut mu + u_j, u_j ~ N(0, tau^2) (recette, graine) ;")
    print("l'adaptateur saboteur est déplacé de theta. Épreuve : est-il hors de l'intervalle de prédiction de K témoins bénins,")
    print("au niveau %.2f unilatéral ? (Le bruit d'échantillonnage sigma^2/n des produits s'ajoute à tau^2 ; ici n grand.)" % ALPHA)
    print()
    ks = (2, 3, 5, 8, 12, 20, 30)
    thetas = (2.0, 3.0, 5.0, 8.0)
    print("    %-4s %-10s " % ("K", "t critique") + " ".join("theta/tau=%-4.0f" % t for t in thetas))
    crit = {}
    for k in ks:
        nu = k - 1
        tc = t_critique(nu, ALPHA)
        crit[k] = tc
        ligne = "    %-4d %-10.3f " % (k, tc)
        for th in thetas:
            delta = th / math.sqrt(1.0 + 1.0 / k)
            ligne += " %-13.3f" % puissance_t(delta, nu, tc)
        print(ligne)
    print("    %-4s %-10.3f " % ("inf", Z_A) + " ".join(" %-13.3f" % (1.0 - PHI(Z_A - th)) for th in thetas) + "  (référence connue)")
    print()
    print("    Lecture : avec deux témoins, la puissance ne dépasse pas 0,17 même à huit écarts ; avec trois, 0,63 ;")
    print("    il faut huit témoins pour voir un déplacement de cinq écarts neuf fois sur dix, quel que soit le nombre de produits lus.")
    # Objets de contrôle : valeurs tabulées de Student
    assert abs(crit[2] - 31.8205) < 2e-3
    assert abs(crit[3] - 6.9646) < 2e-3
    assert abs(crit[8] - 2.9980) < 2e-3
    assert abs(crit[20] - 2.5395) < 2e-3
    assert abs(puissance_t(0.0, 7, crit[8]) - ALPHA) < 1e-6
    print("Contrôles C : t critiques de Student retrouvés (31,821 ; 6,965 ; 2,998 ; 2,539) ; theta = 0 -> niveau. Tenus.")


# ----------------------------------------------------------------------------------------------
# Bloc D — l'attaque publiée est facile à exclure : la pente minimale d'une lecture
# ----------------------------------------------------------------------------------------------
def bloc_d(b):
    titre("BLOC D — Exclure l'attaque déjà publiée ne prouve rien : pente minimale d'une lecture ajoutée à la note")
    print("Note composée [supposé] : w' = (1-lam) * w + lam * q, où q suit la vérité entre politiques avec une pente kappa.")
    print("L'attaque publiée sort de la bande de largeur eps dès que (1-lam)*(w_max - w_att) + lam*kappa*(g_max - g_att) > eps.")
    dw = b["w_max"] - b["w_attaque"]
    print("[imprimé] w_max = %.1f, w_att = %.1f (écart %.1f), eps = %.1f ; g_att = %.1f ; g des meilleures notes faibles : 77 à 81 (p. 5)."
          % (b["w_max"], b["w_attaque"], dw, b["eps"], b["g_attaque"]))
    print("    %-6s %-22s %-22s" % ("lam", "kappa min (g_max=77)", "kappa min (g_max=81)"))
    for lam in (0.25, 0.50, 0.75, 1.00):
        ks = []
        for g_max in (77.0, 81.0):
            dg = g_max - b["g_attaque"]
            ks.append((b["eps"] - (1.0 - lam) * dw) / (lam * dg))
        print("    %-6.2f %-22.3f %-22.3f" % (lam, ks[0], ks[1]))
    print("    Une lecture qui ne suit qu'un dixième de l'écart de vérité suffit : un succès contre l'attaque d'origine est acquis d'avance,")
    print("    comme pour le juge-détecteur du papier (p. 25-26), cassé ensuite par l'attaque refaite. Seule l'attaque refaite compte.")
    k_nul = (b["eps"] - 0.0 * dw) / (1.0 * (77.0 - b["g_attaque"]))
    assert 0.0 < k_nul < 0.1
    print("Contrôle D : lam = 1 -> kappa min = eps / écart de vérité = %.3f. Tenu." % k_nul)


# ----------------------------------------------------------------------------------------------
# Bloc E — la part sue du dommage : taille d'échantillon pour décider
# ----------------------------------------------------------------------------------------------
def _log_binom_pmf(k, n, p):
    if p <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if p >= 1.0:
        return 0.0 if k == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(p) + (n - k) * math.log(1.0 - p))


def binom_cdf(k, n, p):
    return min(1.0, sum(math.exp(_log_binom_pmf(i, n, p)) for i in range(0, k + 1)))


def borne_basse(k, n, conf=0.95):
    """Borne basse exacte (Clopper-Pearson, unilatérale) d'une proportion."""
    if k == 0:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if 1.0 - binom_cdf(k - 1, n, mid) > 1.0 - conf:   # P(X >= k) trop grande -> p trop grand
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def borne_haute(k, n, conf=0.95):
    if k == n:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if binom_cdf(k, n, mid) > 1.0 - conf:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def bloc_e():
    titre("BLOC E — La part sue du dommage : combien de produits de basse qualité confirmée faut-il lire")
    print("Sur des produits de basse qualité confirmée par la vérité, une seconde lecture marque « su » : une part t chez le saboteur,")
    print("une part f chez l'honnête qui échoue autant. Décision sur la borne basse de t / sqrt(f) (bornes exactes à 95 % chacune).")
    print("Couples (t, f) [supposés], sauf le second, repris de comptes imprimés d'un moniteur de texte (9/14 et 1/35).")
    couples = [(0.60, 0.05), (9.0 / 14.0, 1.0 / 35.0), (0.30, 0.05), (0.50, 0.20), (0.20, 0.10)]
    tailles = (50, 100, 300, 500, 1000)
    print("    %-16s %-10s " % ("(t ; f)", "t/sqrt(f)") + " ".join("N=%-7d" % n for n in tailles))
    for t, f in couples:
        ligne = "    (%.3f ; %.3f)  %-10.2f " % (t, f, t / math.sqrt(f))
        for n in tailles:
            kt, kf = round(t * n), round(f * n)
            tb = borne_basse(kt, n)
            fh = borne_haute(kf, n)
            ligne += "%-10.2f" % (tb / math.sqrt(fh))
        print(ligne)
    print("    Lecture : il faut de l'ordre de 300 à 500 produits de chaque sorte pour tenir une borne basse de 2 quand le vrai rapport vaut 2,7 ;")
    print("    à 50 de chaque sorte, même un rapport de 3,8 n'est pas tenu.")
    # Objets de contrôle : 0 sur n -> borne haute = 1 - 0,05^(1/n) ; n sur n -> borne basse = 0,05^(1/n)
    assert abs(borne_haute(0, 35) - (1.0 - 0.05 ** (1.0 / 35))) < 1e-9
    assert abs(borne_basse(14, 14) - 0.05 ** (1.0 / 14)) < 1e-9
    assert borne_basse(0, 10) == 0.0
    print("Contrôles E : 0 sur 35 -> borne haute = 1 - 0,05^(1/35) = %.4f ; 14 sur 14 -> borne basse = %.4f. Tenus."
          % (borne_haute(0, 35), borne_basse(14, 14)))


def main():
    print("Calculs de la note sur « Diffuse AI Control on Fuzzy Tasks » : changer de programme ou contre-attaquer — v1")
    print("Lois exactes et quadratures déterministes ; aucun tirage ; entrées marquées [imprimé] ou [supposé].")
    bloc_a()
    b = bloc_b()
    bloc_c()
    bloc_d(b)
    bloc_e()
    print()
    print("FIN — toutes les assertions tenues.")


if __name__ == "__main__":
    main()
