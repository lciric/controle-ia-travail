#!/usr/bin/env python3
"""Calcul de puissance du préenregistrement de la recombinaison bisociative à deux espaces, v2, brouillon 3.

Aucune simulation du monde : approximation normale seule (moyenne de n écarts appariés ~ N(mu, sigma^2/n)).
Aucun générateur aléatoire, aucun fichier lu, aucun réseau. Sortie déterministe, imprimée sur la sortie standard.
Bibliothèque standard uniquement (math).

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
    """A3 : trois intervalles a 99 % n'excluent pas 0, en SP (differences vraies nulles)."""
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


def main():
    S_BIEN, S_MOY_BAS, S_MOY_HAUT = 15.3, 11.0, 15.3
    B_BIEN, B_MOY = 20.33, 12.73
    N = 2400

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

    print("\n== 6. 'oui' (Table 2 ligne 6) : D0 et DF dans les deux, A8, pas de gain de controle (N_PCg), n=2400 ==")
    print("(PG et J supposes tenus ; gain N_PCg - N_beta0 : deux tests a 99 %, vrai effet <= 0 -> facteur 0,99^2)")
    ligne("P4", "P5", "sigma moyen", "oui R-A (D0, DF, A8)", "oui R-A complet (x 0,99^2)", "oui R-B (D0, DF, A8)")
    for p4, p5 in ((5.5, 3.0), (5.5, 4.0), (5.5, 5.0), (3.0, 3.0), (5.5, 2.5), (5.5, 2.0), (5.5, 1.5), (8, 3)):
        for sm in (S_MOY_BAS, S_MOY_HAUT):
            d0 = detecte_RA(p4, 2.5, S_BIEN, N) * detecte_RA(p4, 2.5, sm, N)
            df = detecte_RA(p5, 2.5, S_BIEN, N) * detecte_RA(p5, 2.5, sm, N)
            d0b = detecte_RB(p4, 2.5, S_BIEN, N) * detecte_RB(p4, 2.5, sm, N)
            dfb = detecte_RB(p5, 2.5, S_BIEN, N) * detecte_RB(p5, 2.5, sm, N)
            ah = a8(0.0, 1.5, 15.3, N)
            ligne(p4, p5, sm, f(d0 * df * ah), f(d0 * df * ah * 0.99 ** 2), f(d0b * dfb * ah))

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

    print("\n== 12. Adoption (Table 1 ligne 8) selon le scenario de centres ==")
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
                    ligne("      -> produit A1 x A2d1 x A8 x A3 x A5 (forme de la contre-lecture ; A2 contre a et d1c non prédits au brouillon 2) :", f(CL_style))

    print("\n== 13. Sensibilite : adoption complete selon l'avance vraie de N_beta0 sur b en 'moyen' (n=2400) ==")
    print("(P4 = 5,5 ; 'bien' fixe aux centres reconcilies V : Delta(N,b)=17,4 ; d1 : +3,5 / +3,8 ; d1c : +4 ; a : -4,8 / -2,2 ; controles comme au 12)")
    ligne("avance N_beta0 - b en moyen", "Delta(N,b) moyen", "Delta(N,d1) moyen", "adoption (sigma moyen 11 / 15,3)")
    for av in (-2, -1.5, -1, -0.5, 0, 1, 3, 6.6):
        nm = av + 5.5
        nb = 17.4
        out = []
        for sm in (S_MOY_BAS, S_MOY_HAUT):
            A1 = a1(nb, S_BIEN, N, 4, 1.20, B_BIEN) * a1(nm, sm, N, 4, 1.20, B_MOY)
            A2 = (lb_pos(nb - 3.5, S_BIEN, N) * lb_pos(nm - 3.8, sm, N)
                  * lb_pos(nb + 4.8, S_BIEN, N) * lb_pos(nm + 2.2, sm, N)
                  * lb_pos(nb - 4.0, S_BIEN, N) * lb_pos(nm - 4.0, sm, N))
            A7 = lb_pos(5.5, S_BIEN, N) * lb_pos(5.5, sm, N)
            ctrl = a3_nul() * a8(0.0, 1.5, 15.3, N) * 0.995 ** 2 * nr(0, -2, S_BIEN, 1200) * nr(0, -2, sm, 1200)
            out.append(f(A1 * A2 * A7 * ctrl))
        ligne(av, f(nm, 1), f(nm - 3.8, 1), " / ".join(out))

    print("\n== 14. S9 : nombre de mondes etendu = min(4800, max(n, ceil(n (sigma_hat / 15,3)^2))) ==")
    ligne("sigma_hat", "n etendu (n=2400)")
    for sh in (11, 15.3, 16, 18, 20, 21.64, 23):
        ligne(sh, min(4800, max(2400, math.ceil(2400 * (sh / 15.3) ** 2))))
    print("erreur relative d'un ecart-type estime sur 200 mondes : 1/sqrt(2*199) =", f(1 / math.sqrt(2 * 199), 4))

    print("\n== 15. Mondes decisifs, total ==")
    print("decision :", 2400 * 3 + 600 * 3 + 1200 * 2, "; descriptives :", 600 * 7, "; total :", 2400 * 3 + 600 * 3 + 1200 * 2 + 600 * 7,
          "; maximum avec extension a 4800 pour les trois :", 4800 * 3 + 600 * 3 + 1200 * 2 + 600 * 7)


if __name__ == "__main__":
    main()
