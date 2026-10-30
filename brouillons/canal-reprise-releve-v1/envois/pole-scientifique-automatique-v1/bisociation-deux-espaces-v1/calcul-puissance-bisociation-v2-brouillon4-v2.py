#!/usr/bin/env python3
"""Calcul de puissance du préenregistrement de la recombinaison bisociative à deux espaces, v2, brouillon 4.
Version 2 du script de puissance (la version 1 est `calcul-puissance-bisociation-v2-brouillon3-v1.py`, inchangée).

Aucune simulation du monde : approximation normale seule (moyenne de n écarts appariés ~ N(mu, sigma^2/n)).
Aucun générateur aléatoire, aucun fichier lu, aucun réseau. Les « intégrales sur une fourchette » sont des
sommes déterministes sur une grille de milieux (aucun tirage). Sortie déterministe, imprimée sur la sortie standard.
Bibliothèque standard uniquement (math).

Ce qui change par rapport à la version 1 (constats CB3-01, CB3-02, CB3-03, CB3-06, CB3-07, CB3-08, CB3-09 de la
contre-lecture 3) :
  - A7 prend deux formes : « b3 » (borne basse à 95 % de N - N_beta0 > 0, brouillon 3) et « b4 »
    (detecte(N - N_beta0, delta) sous R-A : estimation >= delta et borne basse > 0, brouillon 4) ;
  - A3 (placebo sans pont) n'est plus un facteur de l'adoption dans la forme « b4 » (déclencheur d'audit seulement) ;
  - le facteur « gain_controle » est 0,995^2 partout (borne basse à 99 % unilatérale : 0,005 par test) ;
    la version 1 utilisait 0,99^2 au § 6 et 0,995^2 au § 12 ;
  - J est lue sur la chaîne de cohérence (d1c - c : +5 « bien », +3 « moyen » en bas de fourchette) et non sur 3 ;
  - les libellés des lignes de table sont ceux du brouillon 4 (Table 1 ligne 10, Table 2 ligne 7) ;
  - nouveaux paragraphes : adoption intégrée sur la fourchette (§ 16), sensibilité à P4 (§ 17),
    verdicts attendus si le transfert échoue (§ 18), probabilités de confirmation par prédiction (§ 19),
    option b_eloigne (§ 22), essai R5 de J sur les mondes inertes de validation (§ 21), totaux (§ 20).

Conventions (toutes SUPPOSÉES, voir le préenregistrement) :
  - intervalle à 95 % = estimation +/- 1,96 erreur type ; à 99 % = estimation +/- 2,5758 erreur type ;
  - erreur type = sigma / sqrt(n) ; sigma = 15,3 points en « bien » (maximum de v1), 11 ou 15,3 en « moyen » ;
  - les facteurs d'une conjonction sont traités comme indépendants (approximation, dite dans le texte) ;
  - précision moyenne du stratifié b de v1 : 20,33 points en « bien », 12,73 en « moyen » (daaef112...), pour le seuil relatif.
"""
import math

Z95, Z99 = 1.959964, 2.575829


def Phi(x):
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def se(sigma, n):
    return sigma / math.sqrt(n)


def p_est_ge(mu, seuil, s):
    """P(estimation >= seuil)."""
    return 1.0 - Phi((seuil - mu) / s)


def p_est_lt(mu, seuil, s):
    return Phi((seuil - mu) / s)


def a1(mu, sigma, n, theta_abs, theta_rel, b_moyen):
    """A1 : estimation >= theta_abs, rapport >= theta_rel (en points : (theta_rel - 1) * b), borne basse a 95 % > 0."""
    s = se(sigma, n)
    return p_est_ge(mu, max(theta_abs, (theta_rel - 1.0) * b_moyen, Z95 * s), s)


def lb_pos(mu, sigma, n):
    """borne basse a 95 % > 0."""
    s = se(sigma, n)
    return p_est_ge(mu, Z95 * s, s)


def lb99_pos(mu, sigma, n):
    """borne basse a 99 % > 0."""
    s = se(sigma, n)
    return p_est_ge(mu, Z99 * s, s)


def ub_nonpos(mu, sigma, n):
    """borne haute a 95 % <= 0 (suffit_d1, suffit_d1c, suffit_b_eloigne)."""
    s = se(sigma, n)
    return p_est_lt(mu, -Z95 * s, s)


def detecte_RA(mu, delta, sigma, n):
    s = se(sigma, n)
    return p_est_ge(mu, max(delta, Z95 * s), s)


def detecte_RB(mu, delta, sigma, n):
    s = se(sigma, n)
    return p_est_ge(mu, delta + Z95 * s, s)


def zero_n(mu, delta_non, sigma, n):
    """N0 / NF : borne haute a 95 % < delta_non."""
    s = se(sigma, n)
    return p_est_lt(mu, delta_non - Z95 * s, s)


def a8(mu, delta_non, sigma, n):
    """A8 : borne basse a 95 % <= 0 ET borne haute a 95 % < delta_non."""
    s = se(sigma, n)
    return p_est_lt(mu, min(Z95 * s, delta_non - Z95 * s), s)


def nr(mu, marge, sigma, n):
    """A5, un monde v1 : borne basse a 99 % >= marge."""
    s = se(sigma, n)
    return p_est_ge(mu, marge + Z99 * s, s)


def a3_nul():
    """A3 : trois intervalles a 99 % (bilateraux) n'excluent pas 0, en SP (differences vraies nulles)."""
    return 0.99 ** 3


def a4(mu, sigma, n1, n2):
    """A4 / A6 : borne haute a 95 % de la difference entre deux ensembles de mondes < 0."""
    s = sigma * math.sqrt(1.0 / n1 + 1.0 / n2)
    return p_est_lt(mu, -Z95 * s, s)


def n_pour(puissance_z, sigma, ecart):
    """Nombre de mondes pour la puissance donnee par le quantile z (0,84 -> 0,8), sans le terme de borne basse."""
    return (puissance_z * sigma / ecart) ** 2


def n_pour_lb(z_puissance, sigma, mu):
    """Puissance sur 'borne basse > 0' seule : n = ((1,96 + z) sigma / mu)^2."""
    return ((Z95 + z_puissance) * sigma / mu) ** 2


def f(x, d=2):
    return f"{x:.{d}f}"


def ligne(*c):
    print(" | ".join(str(x) for x in c))


def milieux(a, b, k):
    """Milieux de k intervalles egaux de [a, b] (grille deterministe, aucun tirage)."""
    return [a + (i + 0.5) * (b - a) / k for i in range(k)]


S_BIEN, S_MOY_BAS, S_MOY_HAUT = 15.3, 11.0, 15.3
B_BIEN, B_MOY = 20.33, 12.73
N = 2400

# Chaine de coherence (valeurs de v1, `daaef112...`) : Delta(X, b) en points.
CST = dict(d1_b=3.5, d1_m=3.8, d1c=4.0, a_b=4.8, a_m=2.2, c_b=-5.23, c_m=-2.06)
AV_V1_B, AV_V1_M = 11.9, 6.6      # N_beta0 - b observe en v1 (b_eloigne - b)
FOURCHETTE_M = (-3.0, 9.0)         # N_beta0 - b en « moyen » (brouillon 4)
FOURCHETTE_B = (2.0, 14.0)         # N_beta0 - b en « bien » (brouillon 4)
FOURCHETTE_M_LARGE = (-6.0, 9.0)
P4_CENTRE, P4_FOURCHETTE = 5.5, (3.0, 8.0)
P5_FOURCHETTE = (1.0, 5.0)
EPS_FOURCHETTE = (-2.0, 2.0)       # N_beta0 - b_eloigne attendu


def facteurs(av_b, av_m, p4_b, p4_m, sm, n, forme, beloigne=False, eps_b=0.0, eps_m=0.0, jb=5.0, jm=3.0):
    """Facteurs de l'adoption (Table 1 ligne 10), traites comme independants.
    forme 'b3' : A7 = borne basse a 95 % > 0 ; A3 facteur 0,99^3.
    forme 'b4' : A7 = detecte(N - N_beta0, 2,5) sous R-A ; A3 hors du produit (declencheur d'audit seulement)."""
    nb, nm = av_b + p4_b, av_m + p4_m
    F = {}
    F["A1"] = a1(nb, S_BIEN, n, 4, 1.20, B_BIEN) * a1(nm, sm, n, 4, 1.20, B_MOY)
    F["A2d1"] = lb_pos(nb - CST["d1_b"], S_BIEN, n) * lb_pos(nm - CST["d1_m"], sm, n)
    F["A2a"] = lb_pos(nb - (-CST["a_b"]), S_BIEN, n) * lb_pos(nm - (-CST["a_m"]), sm, n)
    F["A2d1c"] = lb_pos(nb - CST["d1c"], S_BIEN, n) * lb_pos(nm - CST["d1c"], sm, n)
    F["A2be"] = (lb_pos(p4_b + eps_b, S_BIEN, n) * lb_pos(p4_m + eps_m, sm, n)) if beloigne else 1.0
    if forme == "b3":
        F["A7"] = lb_pos(p4_b, S_BIEN, n) * lb_pos(p4_m, sm, n)
        F["A3"] = a3_nul()
    else:
        F["A7"] = detecte_RA(p4_b, 2.5, S_BIEN, n) * detecte_RA(p4_m, 2.5, sm, n)
        F["A3"] = 1.0
    F["A4"] = a4(-12.0, 15.3, 600, n)
    F["A5"] = nr(0, -2, S_BIEN, 1200) * nr(0, -2, sm, 1200)
    F["A6"] = a4(-3.5, 15.3, 600, n)
    F["A8"] = a8(0.0, 1.5, 15.3, n)
    F["GC"] = 0.995 ** 2
    F["J"] = lb_pos(jb, S_BIEN, n) * lb_pos(jm, sm, n)
    return F


def adoption(av_b, av_m, p4_b, p4_m, sm, n, forme, **kw):
    p = 1.0
    for v in facteurs(av_b, av_m, p4_b, p4_m, sm, n, forme, **kw).values():
        p *= v
    return p


def moy(valeurs):
    valeurs = list(valeurs)
    return sum(valeurs) / len(valeurs)


def adoption_fourchette(sm, forme, mode, fm=FOURCHETTE_M, p4="centre", beloigne=False, n=N):
    """Adoption moyennee (loi uniforme) sur la fourchette de N_beta0 - b en « moyen ».
    mode : 'fixe' (bien fixe a la valeur de v1), 'comonotone' (bien monte avec moyen), 'independant' (grilles croisees).
    p4 : 'centre' (5,5) ou 'integre' (loi uniforme sur 3 a 8, commune aux deux conditions, independante de av).
    beloigne : ajoute la condition lb95 Delta(N, b_eloigne) > 0, avec N_beta0 - b_eloigne = eps uniforme sur -2 a +2 (independant)."""
    gm = milieux(fm[0], fm[1], 240)
    gp4 = [P4_CENTRE] if p4 == "centre" else milieux(P4_FOURCHETTE[0], P4_FOURCHETTE[1], 20)
    geps = [0.0] if not beloigne else milieux(EPS_FOURCHETTE[0], EPS_FOURCHETTE[1], 8)
    tot, k = 0.0, 0
    for am in gm:
        if mode == "fixe":
            gb = [AV_V1_B]
        elif mode == "comonotone":
            gb = [FOURCHETTE_B[0] + (am - FOURCHETTE_M[0]) * (FOURCHETTE_B[1] - FOURCHETTE_B[0]) / (FOURCHETTE_M[1] - FOURCHETTE_M[0])]
        else:
            gb = milieux(FOURCHETTE_B[0], FOURCHETTE_B[1], 12)
        for ab in gb:
            for p in gp4:
                for eb in geps:
                    for em in geps:
                        tot += adoption(ab, am, p, p, sm, n, forme, beloigne=beloigne, eps_b=eb, eps_m=em)
                        k += 1
    return tot / k


def main():
    print("== 0. Erreurs types (points) ==")
    for n in (600, 1200, 2400, 4800):
        ligne(f"n={n}", "sigma 11 : " + f(se(11, n), 3), "sigma 15,3 : " + f(se(15.3, n), 3),
              "demi-largeur 95 % (15,3) : " + f(Z95 * se(15.3, n), 3))

    print("\n== 1. A1 par condition, n=2400, theta_abs=4, theta_rel=1,20 ==")
    ligne("mu", "moyen sigma 11", "moyen sigma 15,3", "bien sigma 15,3")
    for mu in (2, 3, 4, 4.5, 5, 6, 8, 12, 17):
        ligne(mu, f(a1(mu, S_MOY_BAS, N, 4, 1.20, B_MOY)), f(a1(mu, S_MOY_HAUT, N, 4, 1.20, B_MOY)),
              f(a1(mu, S_BIEN, N, 4, 1.20, B_BIEN)))
    print("seuil effectif : bien", f(max(4, 0.20 * B_BIEN), 2), " moyen", f(max(4, 0.20 * B_MOY), 2))

    print("\n== 2. A1, valeurs du brouillon 2 (n=1200, theta_abs=5, theta_rel=1,25) : reproduction du 0,06 / 0,13 ==")
    ligne("mu", "moyen sigma 11", "moyen sigma 15,3")
    for mu in (4, 4.5, 5):
        ligne(mu, f(a1(mu, S_MOY_BAS, 1200, 5, 1.25, B_MOY)), f(a1(mu, S_MOY_HAUT, 1200, 5, 1.25, B_MOY)))

    print("\n== 3. Detection (R-A, R-B), delta=2,5, n=2400, probabilite de 'detecte' selon mu ==")
    ligne("mu", "R-A s11", "R-A s15,3", "R-B s11", "R-B s15,3")
    for mu in (1, 2, 2.5, 3, 3.5, 4, 5.5, 8):
        ligne(mu, f(detecte_RA(mu, 2.5, 11, N)), f(detecte_RA(mu, 2.5, 15.3, N)),
              f(detecte_RB(mu, 2.5, 11, N)), f(detecte_RB(mu, 2.5, 15.3, N)))
    print("effet vrai donnant la puissance 0,8 (R-A : delta + 0,84 se ; R-B : delta + 2,80 se) a n=2400 :")
    for sg in (11, 15.3, 18):
        ligne("sigma", sg, "R-A", f(2.5 + 0.8416 * se(sg, N), 3), "R-B", f(2.5 + (Z95 + 0.8416) * se(sg, N), 3))

    print("\n== 4. Nombre de mondes pour la puissance 0,8 (R-A) a mu donne, delta=2,5 ==")
    print("(le plus grand de : borne basse > 0 seule = ((1,96+0,84) sigma/mu)^2 ; delta = (0,84 sigma/(mu-delta))^2)")
    ligne("mu", "sigma", "borne basse seule", "delta (mu>delta)", "retenu", "conjoint 2 conditions (z=1,25)")
    for mu in (5.5, 4, 3.5, 3):
        for sg in (11, 15.3):
            nlb = n_pour_lb(0.8416, sg, mu)
            nd = n_pour(0.8416, sg, mu - 2.5) if mu > 2.5 else float("inf")
            nlb2 = n_pour_lb(1.2533, sg, mu)
            nd2 = n_pour(1.2533, sg, mu - 2.5) if mu > 2.5 else float("inf")
            ligne(mu, sg, math.ceil(nlb), math.ceil(nd) if nd < 1e9 else "aucun", math.ceil(max(nlb, nd)),
                  math.ceil(max(nlb2, nd2)))
    print("controle avec delta=3 du brouillon 2 a mu=5,5 : sigma 11 ->", math.ceil(n_pour_lb(0.8416, 11, 5.5)),
          "; sigma 15,3 ->", math.ceil(n_pour_lb(0.8416, 15.3, 5.5)),
          "; conjoint ->", math.ceil(n_pour_lb(1.2533, 11, 5.5)), "/", math.ceil(n_pour_lb(1.2533, 15.3, 5.5)))

    print("\n== 5. A2 contre d1 en 'moyen' (mu = effet vrai sur N - d1), borne basse > 0 ==")
    ligne("mu", "n", "sigma 11", "sigma 15,3")
    for mu in (0.7, 1.5, 3, 8.3):
        for n in (1200, 2400, 4800):
            ligne(mu, n, f(lb_pos(mu, 11, n)), f(lb_pos(mu, 15.3, n)))
    print("mondes pour 0,8 sur ce seul contraste a mu=0,7 :", math.ceil(n_pour_lb(0.8416, 11, 0.7)), "/",
          math.ceil(n_pour_lb(0.8416, 15.3, 0.7)))

    print("\n== 6. 'oui' (Table 2 ligne 7) : D0 et DF dans les deux, A8, pas de gain de controle (N_PCg), n=2400 ==")
    print("(PG et J supposes tenus ; gain N_PCg - N_beta0 : deux tests unilateraux a 99 %, vrai effet <= 0 -> facteur 0,995^2 ;")
    print(" la version 1 du script utilisait 0,99^2 ici, ce qui etait trop severe : correction CB3-09)")
    ligne("P4", "P5", "sigma moyen", "oui R-A (D0, DF, A8)", "oui R-A complet (x 0,995^2)", "oui R-B (D0, DF, A8)")
    for p4, p5 in ((5.5, 3.0), (5.5, 4.0), (5.5, 5.0), (3.0, 3.0), (5.5, 2.5), (5.5, 2.0), (5.5, 1.5), (8, 3)):
        for sm in (S_MOY_BAS, S_MOY_HAUT):
            d0 = detecte_RA(p4, 2.5, S_BIEN, N) * detecte_RA(p4, 2.5, sm, N)
            df = detecte_RA(p5, 2.5, S_BIEN, N) * detecte_RA(p5, 2.5, sm, N)
            d0b = detecte_RB(p4, 2.5, S_BIEN, N) * detecte_RB(p4, 2.5, sm, N)
            dfb = detecte_RB(p5, 2.5, S_BIEN, N) * detecte_RB(p5, 2.5, sm, N)
            ah = a8(0.0, 1.5, 15.3, N)
            ligne(p4, p5, sm, f(d0 * df * ah), f(d0 * df * ah * 0.995 ** 2), f(d0b * dfb * ah))

    print("\n== 6 bis. 'oui' a n=1200 (seuils recommandes : delta 2,5 ; delta_non 1,5) et valeurs du brouillon 2 (delta 3 ; delta_non 2), P4=5,5 ; P5=3 ==")
    ligne("variante", "sigma moyen", "oui (D0 x DF x A8, A8 exact)", "oui avec A8 = produit (forme de la contre-lecture)")
    for lab, n, dl, dn in (("recommandes, n=1200", 1200, 2.5, 1.5), ("brouillon 2, n=1200", 1200, 3.0, 2.0)):
        for sm in (S_MOY_BAS, S_MOY_HAUT):
            d0 = detecte_RA(5.5, dl, S_BIEN, n) * detecte_RA(5.5, dl, sm, n)
            df = detecte_RA(3.0, dl, S_BIEN, n) * detecte_RA(3.0, dl, sm, n)
            ex = a8(0.0, dn, 15.3, n)
            sg = se(15.3, n)
            prod = Phi(Z95) * Phi(dn / sg - Z95)
            ligne(lab, sm, f(d0 * df * ex), f(d0 * df * prod))

    print("\n== 7. 'non' (Table 2 lignes 3 et 5) : N0 dans les deux, n=2400, selon l'effet vrai de N - N_beta0 ==")
    ligne("mu", "sigma moyen", "P(N0 dans les deux)")
    for mu in (0, 0.5, 1, 1.5, 2):
        for sm in (S_MOY_BAS, S_MOY_HAUT):
            ligne(mu, sm, f(zero_n(mu, 1.5, S_BIEN, N) * zero_n(mu, 1.5, sm, N)))

    print("\n== 7 bis. Coexistence « N adoptee » et « le concept n'apporte rien » (CB3-01), n=2400, selon l'effet vrai mu de N - N_beta0 ==")
    print("A7 ancienne forme (borne basse > 0) : P(A7 dans les deux) ; A7 nouvelle forme (detecte, R-A) ; P(N0 dans les deux)")
    ligne("mu", "sigma moyen", "A7 ancienne", "A7 nouvelle", "N0 dans les deux", "ancienne ET N0 possibles ensemble ?")
    for mu in (0.5, 1, 1.5, 2, 2.5, 3):
        for sm in (S_MOY_BAS, S_MOY_HAUT):
            anc = lb_pos(mu, S_BIEN, N) * lb_pos(mu, sm, N)
            nou = detecte_RA(mu, 2.5, S_BIEN, N) * detecte_RA(mu, 2.5, sm, N)
            n0 = zero_n(mu, 1.5, S_BIEN, N) * zero_n(mu, 1.5, sm, N)
            ligne(mu, sm, f(anc), f(nou), f(n0), "oui, a probabilite non nulle" if anc > 0.005 and n0 > 0.005 else "non (l'un des deux est nul a 0,005 pres)")
    print("(avec la nouvelle forme, A7 vrai impose une estimation >= 2,5 > 1,5 = delta_non, donc N0 faux : exclusion logique, non probabiliste)")

    print("\n== 8. M_inertes (A8 = borne basse <= 0 et borne haute < delta_non=1,5) selon le gain parasite mu ==")
    ligne("n", "mu", "A8 passe : sigma 11", "sigma 13", "sigma 15,3", "prise en defaut = 1 - passe (15,3 / 11)")
    for n in (1200, 2400):
        for mu in (0, 0.5, 1, 1.5, 2):
            p11, p13, p153 = a8(mu, 1.5, 11, n), a8(mu, 1.5, 13, n), a8(mu, 1.5, 15.3, n)
            ligne(n, mu, f(p11), f(p13), f(p153), f(1 - p153) + " / " + f(1 - p11))
    print("A8 avec delta_non=2 (brouillon 2), n=1200 et mu=0, sigma 15,3 :", f(a8(0, 2, 15.3, 1200), 3))

    print("\n== 9. Non-regression : borne basse a 99 % >= marge ; une condition ==")
    ligne("n", "sigma", "marge -1, mu 0", "marge -1, mu 1", "marge -2, mu 0", "marge -2, mu 1")
    for n in (600, 1200):
        for sg in (11, 15.3):
            ligne(n, sg, f(nr(0, -1, sg, n)), f(nr(1, -1, sg, n)), f(nr(0, -2, sg, n)), f(nr(1, -2, sg, n)))

    print("\n== 10. A4 (Delta_INV - Delta_bien) et A6 (V_fuite), n1=600, n2=2400, sigma 15,3 ==")
    s_d = 15.3 * math.sqrt(1 / 600 + 1 / 2400)
    print("erreur type de la difference :", f(s_d, 3), "(INV 600 contre bien 1200 : ", f(15.3 * math.sqrt(1 / 600 + 1 / 1200), 3), ")")
    for mu in (-1, -3, -5, -12):
        ligne("mu", mu, "P(borne haute < 0)", f(a4(mu, 15.3, 600, 2400)))

    print("\n== 11. J : borne basse a 95 % de Delta(d1c, c) > 0, selon l'effet vrai ==")
    ligne("mu_J", "n", "sigma 11", "sigma 15,3", "conjonction bien (15,3) x moyen (11 / 15,3)")
    for mu in (0, 0.5, 1, 1.5, 2, 3, 5):
        for n in (2400,):
            jb = lb_pos(mu, S_BIEN, n)
            ligne(mu, n, f(lb_pos(mu, 11, n)), f(lb_pos(mu, 15.3, n)),
                  f(jb * lb_pos(mu, 11, n)) + " / " + f(jb * lb_pos(mu, 15.3, n)))
    print("chaine de coherence de J (CB3-06 i) : Delta(d1c, c) = Delta(d1c, b) - Delta(c, b) ; valeurs de v1 pour d1 et c :",
          "bien", f(4.0 - CST["c_b"], 2), "(d1c a +4), moyen", f(4.0 - CST["c_m"], 2),
          "; d1 - c en v1 : bien", f(CST["d1_b"] - CST["c_b"], 2), ", moyen", f(CST["d1_m"] - CST["c_m"], 2),
          "; bas de fourchette utilise ci-dessous : +5 (bien), +3 (moyen)")

    print("\n== 12. Adoption (Table 1 ligne 10) selon le scenario de centres : reproduction de la version 1 ==")
    print("facteurs : A1(b,m) A2-d1(b,m) A2-a(b,m) A2-d1c(b,m) A7(b,m) A3 A4 A5(2 NR) A6 A8 gain_controle J")
    sc = {
        "L (centres du brouillon 2, implicite N_beta0 - b = +2,5 / -1)": dict(
            nb=8.0, nm=4.5, d1b=4.5, d1m=0.7, ab=12.8, am=6.7, d1cb=4.0, d1cm=0.5, p4=5.5),
        "V (centres reconcilies, ancres sur v1 : N_beta0 - b = +11,9 / +6,6)": dict(
            nb=17.4, nm=12.1, d1b=13.9, d1m=8.3, ab=22.2, am=14.3, d1cb=13.4, d1cm=8.1, p4=5.5),
    }
    for nom, c in sc.items():
        print("--", nom)
        for sm in (S_MOY_BAS, S_MOY_HAUT):
            for (th_abs, th_rel, n_dec, nr_n, marge, lab) in ((4, 1.20, 2400, 1200, -2, "valeurs recommandees (n=2400)"),
                                                              (4, 1.20, 1200, 1200, -2, "seuils recommandes, n=1200"),
                                                              (5, 1.25, 1200, 1200, -2, "valeurs du brouillon 2 (n=1200, theta 5, x1,25)")):
                delta_non = 2.0 if lab.startswith("valeurs du brouillon 2") else 1.5
                A1 = a1(c["nb"], S_BIEN, n_dec, th_abs, th_rel, B_BIEN) * a1(c["nm"], sm, n_dec, th_abs, th_rel, B_MOY)
                A2d1 = lb_pos(c["d1b"], S_BIEN, n_dec) * lb_pos(c["d1m"], sm, n_dec)
                A2a = lb_pos(c["ab"], S_BIEN, n_dec) * lb_pos(c["am"], sm, n_dec)
                A2d1c = lb_pos(c["d1cb"], S_BIEN, n_dec) * lb_pos(c["d1cm"], sm, n_dec)
                A7 = lb_pos(c["p4"], S_BIEN, n_dec) * lb_pos(c["p4"], sm, n_dec)
                A3 = a3_nul()
                A4 = a4(-12.0, 15.3, 600, n_dec)
                A5 = nr(0, marge, S_BIEN, nr_n) * nr(0, marge, sm, nr_n)
                A6 = a4(-3.5, 15.3, 600, n_dec)
                A8 = a8(0.0, delta_non, 15.3, n_dec)
                GC = 0.995 ** 2
                J = lb_pos(3.0, S_BIEN, n_dec) * lb_pos(3.0, sm, n_dec)
                CL_style = A1 * A2d1 * A8 * A3 * A5
                complet = A1 * A2d1 * A2a * A2d1c * A7 * A3 * A4 * A5 * A6 * A8 * GC * J
                ligne(f"sigma moyen {sm}", lab, "A1 " + f(A1), "A2d1 " + f(A2d1), "A2a " + f(A2a), "A2d1c " + f(A2d1c),
                      "A7 " + f(A7), "A3 " + f(A3), "A4 " + f(A4), "A5 " + f(A5), "A6 " + f(A6), "A8 " + f(A8),
                      "GC " + f(GC), "J " + f(J))
                if nom.startswith("V"):
                    ligne("      -> produit A1 x A2d1 x A8 x A3 x A5 (forme de la contre-lecture) :", f(CL_style),
                          "; produit complet des 12 facteurs :", f(complet))
                else:
                    ligne("      -> produit A1 x A2d1 x A8 x A3 x A5 (forme de la contre-lecture ; A2 contre a et d1c non predits au brouillon 2) :", f(CL_style))

    print("\n== 13. Sensibilite : adoption complete selon l'avance vraie de N_beta0 sur b en 'moyen' (n=2400) ==")
    print("(P4 = 5,5 ; 'bien' fixe au centre de v1 : N_beta0 - b = 11,9 ; formes b3 (brouillon 3) et b4 (brouillon 4))")
    ligne("avance N_beta0 - b en moyen", "Delta(N,b) moyen", "Delta(N,d1) moyen", "b3 (sigma moyen 11 / 15,3)", "b4 (sigma moyen 11 / 15,3)")
    for av in (-6, -3, -2, -1.5, -1, -0.5, 0, 1, 3, 6.6, 9):
        nm = av + 5.5
        o3 = [f(adoption(AV_V1_B, av, 5.5, 5.5, sm, N, "b3", jb=3.0, jm=3.0)) for sm in (S_MOY_BAS, S_MOY_HAUT)]
        o4 = [f(adoption(AV_V1_B, av, 5.5, 5.5, sm, N, "b4")) for sm in (S_MOY_BAS, S_MOY_HAUT)]
        ligne(av, f(nm, 1), f(nm - 3.8, 1), " / ".join(o3), " / ".join(o4))

    print("\n== 14. S9 : nombre de mondes etendu = min(4800, max(n, ceil(n (sigma_hat / 15,3)^2))) des que sigma_hat > 15,3 (CB3-07) ==")
    ligne("sigma_hat", "n etendu (n=2400)")
    for sh in (11, 15.3, 15.5, 16, 18, 20, 21.64, 23, 25):
        ligne(sh, min(4800, max(2400, math.ceil(2400 * (sh / 15.3) ** 2))))
    print("erreur relative d'un ecart-type estime sur 200 mondes : 1/sqrt(2*199) =", f(1 / math.sqrt(2 * 199), 4))
    print("n etendu moyen selon l'ecart-type vrai (sigma_hat ~ N(sigma, (0,0501 sigma)^2), grille de 400 milieux sur +/- 4 ecarts types) :")
    ligne("sigma vrai", "n etendu moyen", "P(sigma_hat > 15,3)", "P(n' = 4800)")
    for sv in (11, 14, 15.3, 16, 18):
        sd = sv / math.sqrt(2 * 199)
        grille = milieux(sv - 4 * sd, sv + 4 * sd, 400)
        poids = [math.exp(-0.5 * ((x - sv) / sd) ** 2) for x in grille]
        W = sum(poids)
        nmoy = sum(p * min(4800, max(2400, math.ceil(2400 * (x / 15.3) ** 2))) for p, x in zip(poids, grille)) / W
        pgt = sum(p for p, x in zip(poids, grille) if x > 15.3) / W
        p48 = sum(p for p, x in zip(poids, grille) if 2400 * (x / 15.3) ** 2 >= 4800) / W
        ligne(sv, f(nmoy, 0), f(pgt), f(p48))

    print("\n== 15. Mondes decisifs et descriptifs, total (S15 du brouillon 4 : huit conditions descriptives, dont M_fonds_1ou2) ==")
    dec = 2400 * 3 + 600 * 3 + 1200 * 2
    des = 600 * 8
    print("decision :", dec, "; descriptives :", des, "; total :", dec + des,
          "; maximum avec extension a 4800 pour les trois :", 4800 * 3 + 600 * 3 + 1200 * 2 + des)
    print("brouillon 3 (sept descriptives) : decision", dec, "; descriptives", 600 * 7, "; total", dec + 600 * 7,
          "; maximum", 4800 * 3 + 600 * 3 + 1200 * 2 + 600 * 7)
    print("mondes de validation du generateur : 300 bien + 300 moyen + 100 jumelles + 300 miroirs inertes (essai R5 de J) =", 300 + 300 + 100 + 300,
          "; 200 + 200 pour l'ecart-type de S9 (sous-ensembles des graines de validation, comptes a part)")

    # ------------------------------------------------------------------ nouveautes du brouillon 4
    print("\n== 16. Adoption integree sur la fourchette (CB3-02) : loi uniforme sur N_beta0 - b en 'moyen', P4 = 5,5, n=2400 ==")
    print("(b3 = brouillon 3 : A7 borne basse > 0, A3 dans le produit ; b4 = brouillon 4 : A7 = detecte sous R-A, A3 hors produit)")
    print("modes : fixe = « bien » fixe a +11,9 (convention de la contre-lecture 3) ; comonotone = « bien » monte avec « moyen »")
    print("        (2 a 14 pour -3 a +9) ; independant = deux lois uniformes independantes")
    ligne("forme", "mode", "fourchette moyen", "P4", "sigma moyen 11", "sigma moyen 15,3")
    for forme in ("b3", "b4"):
        for mode in ("fixe", "comonotone", "independant"):
            for fm, lab in ((FOURCHETTE_M, "-3 a +9"), (FOURCHETTE_M_LARGE, "-6 a +9")):
                if mode != "fixe" and fm is FOURCHETTE_M_LARGE:
                    continue
                for p4 in ("centre",):
                    r = [adoption_fourchette(sm, forme, mode, fm=fm, p4=p4) for sm in (S_MOY_BAS, S_MOY_HAUT)]
                    ligne(forme, mode, lab, "5,5", f(r[0]), f(r[1]))
    for forme in ("b3", "b4"):
        r = [adoption_fourchette(sm, forme, "comonotone", p4="integre") for sm in (S_MOY_BAS, S_MOY_HAUT)]
        ligne(forme, "comonotone", "-3 a +9", "uniforme 3 a 8", f(r[0]), f(r[1]))
    print("memes chiffres a trois decimales (b3 fixe -3 a +9 ; b4 comonotone -3 a +9 ; b4 fixe -6 a +9) :",
          " / ".join(f(adoption_fourchette(sm, "b3", "fixe"), 3) for sm in (S_MOY_BAS, S_MOY_HAUT)), "|",
          " / ".join(f(adoption_fourchette(sm, "b4", "comonotone"), 3) for sm in (S_MOY_BAS, S_MOY_HAUT)), "|",
          " / ".join(f(adoption_fourchette(sm, "b4", "fixe", fm=FOURCHETTE_M_LARGE), 3) for sm in (S_MOY_BAS, S_MOY_HAUT)))
    print("au centre de v1 (point, non integre) : b3 / b4 ->",
          " / ".join(f(adoption(AV_V1_B, AV_V1_M, 5.5, 5.5, sm, N, "b3", jb=3.0, jm=3.0)) for sm in (S_MOY_BAS, S_MOY_HAUT)), "/",
          " / ".join(f(adoption(AV_V1_B, AV_V1_M, 5.5, 5.5, sm, N, "b4")) for sm in (S_MOY_BAS, S_MOY_HAUT)))

    print("\n== 17. Quand la Table 1 est-elle presque acquise ? Adoption (forme b4, puis b3) selon N_beta0 - b en 'moyen' et P4 (CB3-02, CB3-01) ==")
    print("(n=2400 ; « bien » a +11,9 ; Delta(N, b ; moyen) = N_beta0 - b + P4 ; cellule = sigma moyen 11 / 15,3)")
    p4s = (1.5, 2.5, 3.0, 3.5, 4.5, 5.5, 8.0)
    for forme, jb, jm, lab in (("b4", 5.0, 3.0, "forme b4 (brouillon 4)"), ("b3", 3.0, 3.0, "forme b3 (brouillon 3)")):
        print("--", lab)
        ligne("N_beta0 - b (moyen) \\ P4", *[str(x) for x in p4s])
        for av in (-1.0, -0.5, 0.0, 1.0, 3.0, 6.6):
            cells = []
            for p4 in p4s:
                o = [adoption(AV_V1_B, av, p4, p4, sm, N, forme, jb=jb, jm=jm) for sm in (S_MOY_BAS, S_MOY_HAUT)]
                cells.append(f(o[0]) + " / " + f(o[1]))
            ligne(av, *cells)

    print("\n== 18. Verdict attendu si le transfert echoue (Table 1) : repartition selon N_beta0 - b en 'moyen' (n=2400, P4 = 5,5, bien a +11,9) ==")
    print("l3 = perd (borne haute de N - b < 0 dans l'une des deux conditions) ; l4 = « N sous le seuil » (A1 non tenue, sans l3) ;")
    print("adopte = produit complet (forme b4) ; autre = lignes 5 a 9 et 11 (dont « indecis ») ; l7 = Swanson par operateur suffit (les deux conditions)")
    ligne("N_beta0 - b (moyen)", "sigma moyen", "l3 perd", "l4 sous le seuil", "adopte", "autre", "l7 suffit_d1 (deux conditions)")
    for av in (-6.0, -4.0, -3.0, -2.0, -1.5, -1.0, -0.5, 0.0, 3.0, 6.6):
        for sm in (S_MOY_BAS, S_MOY_HAUT):
            nb, nm = AV_V1_B + 5.5, av + 5.5
            p3 = 1 - (1 - ub_nonpos(nb, S_BIEN, N)) * (1 - ub_nonpos(nm, sm, N))
            A1b = a1(nb, S_BIEN, N, 4, 1.20, B_BIEN)
            A1m = a1(nm, sm, N, 4, 1.20, B_MOY)
            p4_ = (1 - A1b * A1m) - p3
            pa = adoption(AV_V1_B, av, 5.5, 5.5, sm, N, "b4")
            reste = 1 - p3 - p4_ - pa
            l7 = ub_nonpos(nb - CST["d1_b"], S_BIEN, N) * ub_nonpos(nm - CST["d1_m"], sm, N)
            ligne(av, sm, f(p3), f(p4_), f(pa), f(reste), f(l7))
    print("integrale sur la fourchette (« moyen » -3 a +9, « bien » comonotone 2 a 14, P4 = 5,5) :")
    ligne("sigma moyen", "l3 perd", "l4 sous le seuil", "adopte", "autre", "l7")
    for sm in (S_MOY_BAS, S_MOY_HAUT):
        gm = milieux(FOURCHETTE_M[0], FOURCHETTE_M[1], 240)
        t3 = t4 = ta = t7 = 0.0
        for am in gm:
            ab = FOURCHETTE_B[0] + (am - FOURCHETTE_M[0])
            nb, nm = ab + 5.5, am + 5.5
            p3 = 1 - (1 - p_est_lt(nb, -Z95 * se(S_BIEN, N), se(S_BIEN, N))) * (1 - p_est_lt(nm, -Z95 * se(sm, N), se(sm, N)))
            A1 = a1(nb, S_BIEN, N, 4, 1.20, B_BIEN) * a1(nm, sm, N, 4, 1.20, B_MOY)
            t3 += p3
            t4 += (1 - A1) - p3
            ta += adoption(ab, am, 5.5, 5.5, sm, N, "b4")
            t7 += ub_nonpos(nb - CST["d1_b"], S_BIEN, N) * ub_nonpos(nm - CST["d1_m"], sm, N)
        k = len(gm)
        ligne(sm, f(t3 / k), f(t4 / k), f(ta / k), f(1 - (t3 + t4 + ta) / k), f(t7 / k))

    print("\n== 19. Probabilites de confirmation de chaque prediction, integrees sur les fourchettes (comonotone, P4 uniforme 3 a 8, P5 uniforme 1 a 5) ==")
    print("(« confirmee » = la condition de lecture correspondante est vraie ; n=2400 ; sigma moyen 11 / 15,3 ; independance entre bien et moyen)")
    gm = milieux(FOURCHETTE_M[0], FOURCHETTE_M[1], 120)
    gp4 = milieux(P4_FOURCHETTE[0], P4_FOURCHETTE[1], 20)
    gp5 = milieux(P5_FOURCHETTE[0], P5_FOURCHETTE[1], 20)
    geps = milieux(EPS_FOURCHETTE[0], EPS_FOURCHETTE[1], 8)
    noms = ["P1 (N - b, bien : A1 bien)", "P2 (N - b, moyen : A1 moyen)", "P3 (N - d1c > 0 dans les deux)", "P14 (N - d1 > 0 dans les deux)",
            "P15 (N - a > 0 dans les deux)", "P4 (A7 = detecte, dans les deux)", "P5 (N - N_filtre detecte, dans les deux)",
            "P16 (N - b_eloigne > 0 dans les deux)", "J (d1c - c > 0 dans les deux)", "« oui » Table 2 (D0, DF, A8, sans gain de controle)",
            "« N adoptee » (forme b4, sans b_eloigne)", "« N adoptee » (forme b4, avec b_eloigne)"]
    res = {sm: [0.0] * len(noms) for sm in (S_MOY_BAS, S_MOY_HAUT)}
    for sm in (S_MOY_BAS, S_MOY_HAUT):
        tot = [0.0] * len(noms)
        cnt = 0
        for am in gm:
            ab = FOURCHETTE_B[0] + (am - FOURCHETTE_M[0])
            for p4 in gp4:
                nb, nm = ab + p4, am + p4
                v = [0.0] * 5
                v[0] = a1(nb, S_BIEN, N, 4, 1.20, B_BIEN)
                v[1] = a1(nm, sm, N, 4, 1.20, B_MOY)
                v[2] = lb_pos(nb - CST["d1c"], S_BIEN, N) * lb_pos(nm - CST["d1c"], sm, N)
                v[3] = lb_pos(nb - CST["d1_b"], S_BIEN, N) * lb_pos(nm - CST["d1_m"], sm, N)
                v[4] = lb_pos(nb + CST["a_b"], S_BIEN, N) * lb_pos(nm + CST["a_m"], sm, N)
                a7 = detecte_RA(p4, 2.5, S_BIEN, N) * detecte_RA(p4, 2.5, sm, N)
                p16 = 0.0
                for eb in geps:
                    for em in geps:
                        p16 += lb_pos(p4 + eb, S_BIEN, N) * lb_pos(p4 + em, sm, N)
                p16 /= len(geps) ** 2
                jj = lb_pos(5.0, S_BIEN, N) * lb_pos(3.0, sm, N)
                p5 = moy(detecte_RA(x, 2.5, S_BIEN, N) * detecte_RA(x, 2.5, sm, N) for x in gp5)
                oui = a7 * p5 * a8(0.0, 1.5, 15.3, N) * 0.995 ** 2
                ad = adoption(ab, am, p4, p4, sm, N, "b4")
                ad_be = moy(adoption(ab, am, p4, p4, sm, N, "b4", beloigne=True, eps_b=eb, eps_m=em) for eb in geps for em in geps)
                for i, x in enumerate((v[0], v[1], v[2], v[3], v[4], a7, p5, p16, jj, oui, ad, ad_be)):
                    tot[i] += x
                cnt += 1
        res[sm] = [t / cnt for t in tot]
    ligne("prediction", "sigma moyen 11", "sigma moyen 15,3")
    for i, nm_ in enumerate(noms):
        ligne(nm_, f(res[S_MOY_BAS][i]), f(res[S_MOY_HAUT][i]))
    print("(P5 est integree sur sa propre fourchette ; « oui » multiplie A7 (P4 integre) par la probabilite P5 moyenne, A8 et 0,995^2 : approximation)")

    print("\n== 20. Totaux de mondes (S15, brouillon 4) ==")
    print("voir § 15")

    print("\n== 21. Essai R5 de J sur les mondes de validation de M_inertes (CB3-06 iii) : 300 mondes, sigma 15,3 ==")
    print("J vraie = borne basse a 95 % de Delta(d1c, c) > 0 ; elle doit etre fausse (concepts inertes) ; vraie = declencheur d'audit R4")
    ligne("effet parasite vrai de d1c - c dans M_inertes", "P(J vraie) = P(declencheur d'audit)", "avec la borne a 99 %")
    for mu in (-3, -1, 0, 0.5, 1, 1.5, 2, 3, 5):
        ligne(mu, f(lb_pos(mu, 15.3, 300)), f(lb99_pos(mu, 15.3, 300)))

    print("\n== 22. Option b_eloigne (CB3-03) : cout de la condition lb95 Delta(N, b_eloigne) > 0, n=2400 ==")
    print("Delta(N, b_eloigne) = Delta(N, N_beta0) + Delta(N_beta0, b_eloigne) = P4 + eps, eps = N_beta0 - b_eloigne attendu dans [-2 ; +2]")
    ligne("P4", "eps", "P(lb95>0 dans les deux), sigma moyen 11 / 15,3", "P(ub95 <= 0 dans les deux) [ligne « b_eloigne suffit »]")
    for p4 in (3.0, 5.5, 8.0):
        for eps in (-2.0, 0.0, 2.0):
            lbs = [lb_pos(p4 + eps, S_BIEN, N) * lb_pos(p4 + eps, sm, N) for sm in (S_MOY_BAS, S_MOY_HAUT)]
            ubs = [ub_nonpos(p4 + eps, S_BIEN, N) * ub_nonpos(p4 + eps, sm, N) for sm in (S_MOY_BAS, S_MOY_HAUT)]
            ligne(p4, eps, " / ".join(f(x) for x in lbs), " / ".join(f(x) for x in ubs))
    print("eps uniforme sur [-2 ; +2], independant entre les deux conditions, P4 = 5,5 :")
    for sm in (S_MOY_BAS, S_MOY_HAUT):
        ge = milieux(-2.0, 2.0, 16)
        pb = moy(lb_pos(5.5 + e, S_BIEN, N) for e in ge) * moy(lb_pos(5.5 + e, sm, N) for e in ge)
        ligne("sigma moyen", sm, "P(condition ajoutee tenue) =", f(pb))
    print("adoption integree sur la fourchette (« moyen » -3 a +9, « bien » comonotone, P4 = 5,5, eps uniforme et independant par condition) :")
    ligne("forme", "option", "sigma 11", "sigma 15,3")
    for beloigne in (False, True):
        r = [adoption_fourchette(sm, "b4", "comonotone", p4="centre", beloigne=beloigne) for sm in (S_MOY_BAS, S_MOY_HAUT)]
        ligne("b4", "avec la condition b_eloigne" if beloigne else "sans", f(r[0]), f(r[1]))
    print("meme chose avec P4 uniforme sur 3 a 8 :")
    for beloigne in (False, True):
        r = [adoption_fourchette(sm, "b4", "comonotone", p4="integre", beloigne=beloigne) for sm in (S_MOY_BAS, S_MOY_HAUT)]
        ligne("b4", "avec la condition b_eloigne" if beloigne else "sans", f(r[0]), f(r[1]))

    print("\n== 23. Probabilite d'un declencheur d'audit (R4) par SP, A3 ayant cesse d'etre un facteur de l'adoption (CB3-08) ==")
    print("P(au moins un des trois intervalles a 99 % exclut 0 en SP, effets vrais nuls) =", f(1 - a3_nul(), 3))

    print("\n== 24. M_fonds_1ou2 (CB3-04), condition descriptive de 600 mondes : sensibilite de la difference avec M_bien (2400 mondes) ==")
    print("contraste 39 : Delta(N, N_beta0 ; M_fonds_1ou2) - Delta(N, N_beta0 ; M_bien), deux ensembles de mondes distincts")
    for sg in (11.0, 15.3):
        sd = sg * math.sqrt(1 / 600 + 1 / 2400)
        ligne("sigma", sg, "erreur type de la difference", f(sd, 3), "demi-largeur 95 %", f(Z95 * sd, 3),
              "ecart vrai detecte avec la puissance 0,8 (2,80 erreurs types)", f((Z95 + 0.8416) * sd, 2))
    print("(sigma de Delta(N, N_beta0) inconnu, probablement inferieur a celui de Delta(N, b) : valeurs prudentes ; descriptif, sans verdict)")


if __name__ == "__main__":
    main()
