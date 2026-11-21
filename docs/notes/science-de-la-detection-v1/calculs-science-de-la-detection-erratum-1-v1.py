#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de l'erratum 1 de la note « science de la détection ».

Règle « moniteur invalide » corrigée : mélange (moyenne des produits) sur une
grille qui descend vers le taux acceptable. Lois exactes, formules fermées et
programmation dynamique exacte ; aucun tirage, aucune donnée du programme,
bibliothèque standard seule. Entrées : suppositions d'illustration. Non contre-lu.

Usage : python calculs-science-de-la-detection-erratum-1-v1.py > calculs-science-de-la-detection-erratum-1-v1.txt
"""
import math

RHO0, ALPHA, BETA = 0.10, 0.05, 0.10

GRILLES = {
    # multiples du taux acceptable
    "v1, cinq taux (1,25 à 5)": [1.25, 1.5, 2.0, 3.0, 5.0],
    "seize taux (1,25 à 5, pas 0,25)": [1.25 + 0.25 * i for i in range(16)],
    "descendante, douze taux (1 + 4/2^j)": [1.0 + 4.0 / 2 ** j for j in range(12)],
}
CORRIGEE = "descendante, douze taux (1 + 4/2^j)"

# Valeurs publiées par la re-dérivation indépendante (sortie du 21 novembre, § 2a),
# recopiées ici pour la seule comparaison : (grille, q, n) -> borne.
REDERIVATION = {
    ("seize taux (1,25 à 5, pas 0,25)", 0.20, 1000): 136.6,
    ("seize taux (1,25 à 5, pas 0,25)", 0.20, 4000): 255.8,
    ("seize taux (1,25 à 5, pas 0,25)", 0.20, 16000): 489.6,
    ("seize taux (1,25 à 5, pas 0,25)", 0.05, 1000): 322.4,
    ("seize taux (1,25 à 5, pas 0,25)", 0.05, 4000): 566.5,
    ("seize taux (1,25 à 5, pas 0,25)", 0.05, 16000): 1058.5,
    (CORRIGEE, 0.20, 1000): 136.1,
    (CORRIGEE, 0.20, 4000): 252.4,
    (CORRIGEE, 0.20, 16000): 483.7,
    (CORRIGEE, 0.05, 1000): 317.9,
    (CORRIGEE, 0.05, 4000): 564.6,
    (CORRIGEE, 0.05, 16000): 1045.1,
}


# ------------------------------------------------------------------ outils
def uab(mult, rho0=RHO0):
    """u = log(rho/rho0), b = log((1-rho0)/(1-rho)), a = u + b, pour rho = mult * rho0."""
    rho = mult * rho0
    u = math.log(rho / rho0)
    b = math.log((1.0 - rho0) / (1.0 - rho))
    return u, b, u + b


def phi(q, s):
    """log E[exp(-s (A - q))], A de Bernoulli(q)."""
    return q * s + math.log(1.0 - q + q * math.exp(-s))


def borne_un(mult, lam, q, n, big_l, beta=BETA, rho0=RHO0):
    u, b, a = uab(mult, rho0)
    aa = q * a - (phi(q, lam * u) - phi(q, -lam * b)) / lam
    if aa <= 0.0:
        return math.inf
    cc = q * b + phi(q, -lam * b) / lam
    return (big_l + math.log(1.0 / beta) / lam) / aa + n * (cc / aa - rho0)


def borne(grille, q, n, alpha=ALPHA, beta=BETA, rho0=RHO0):
    """Borne garantie de l'excès avant l'annonce (théorème de la re-dérivation, § 3.1),
    minimisée sur le taux de la grille et sur lambda (grille log puis section dorée)."""
    big_l = math.log(len(grille) / alpha)
    meilleur = (math.inf, None, None)
    for mult in grille:
        if q >= 1.0:
            # audit complet : phi = 0, la borne décroît en lambda, limite sans terme en beta
            u, b, a = uab(mult, rho0)
            val = big_l / a + n * (b / a - rho0)
            if val < meilleur[0]:
                meilleur = (val, mult, math.inf)
            continue
        pts = [math.exp(math.log(1e-4) + i * (math.log(50.0) - math.log(1e-4)) / 600) for i in range(601)]
        vals = [borne_un(mult, lam, q, n, big_l, beta, rho0) for lam in pts]
        i0 = min(range(len(pts)), key=lambda i: vals[i])
        lo, hi = pts[max(i0 - 1, 0)], pts[min(i0 + 1, len(pts) - 1)]
        g = (math.sqrt(5.0) - 1.0) / 2.0
        c, d = hi - g * (hi - lo), lo + g * (hi - lo)
        fc, fd = borne_un(mult, c, q, n, big_l, beta, rho0), borne_un(mult, d, q, n, big_l, beta, rho0)
        for _ in range(80):
            if fc < fd:
                hi, d, fd = d, c, fc
                c = hi - g * (hi - lo)
                fc = borne_un(mult, c, q, n, big_l, beta, rho0)
            else:
                lo, c, fc = c, d, fd
                d = lo + g * (hi - lo)
                fd = borne_un(mult, d, q, n, big_l, beta, rho0)
        lam = (lo + hi) / 2.0
        val = min(borne_un(mult, lam, q, n, big_l, beta, rho0), vals[i0])
        if val < meilleur[0]:
            meilleur = (val, mult, lam)
    return meilleur


def mises(grille, rho0=RHO0):
    out = []
    for mult in grille:
        u, b, a = uab(mult, rho0)
        out.append((u, -b))          # log du facteur si U = 1, si U = 0
    return out


def log_richesse(s, n, ms):
    vals = [x * s + y * (n - s) for x, y in ms]
    m = max(vals)
    return m + math.log(sum(math.exp(v - m) for v in vals)) - math.log(len(vals))


def seuil_s(n, ms, log_seuil):
    lo, hi = 0, n + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if log_richesse(mid, n, ms) >= log_seuil:
            hi = mid
        else:
            lo = mid + 1
    return lo


def monde_constant(taux, n_max, ms, log_seuil, jalons):
    """Programmation dynamique exacte : probabilité d'annonce au plus tard à chaque jalon
    (en audits) et médiane du nombre d'audits avant l'annonce."""
    vivant = {0: 1.0}
    cumul, mediane, lus = 0.0, None, {}
    for n in range(1, n_max + 1):
        thr = seuil_s(n, ms, log_seuil)
        suivant = {}
        for s, pr in vivant.items():
            if pr < 1e-300:
                continue
            for ds, w in ((0, 1.0 - taux), (1, taux)):
                s2 = s + ds
                if s2 >= thr:
                    cumul += pr * w
                else:
                    suivant[s2] = suivant.get(s2, 0.0) + pr * w
        vivant = suivant
        if mediane is None and cumul >= 0.5:
            mediane = n
        if n in jalons:
            lus[n] = cumul
    return lus, mediane


def log_binom_pmf(n, p):
    lp, lq = math.log(p), math.log1p(-p)
    lg = math.lgamma
    return [lg(n + 1) - lg(k + 1) - lg(n - k + 1) + k * lp + (n - k) * lq for k in range(n + 1)]


def m_etoile_horizon_fixe(t, p, ms, log_seuil, beta=BETA):
    """Valeur de la note v1 : plus petit M tel que P(richesse à T sous le seuil | M) <= beta,
    S ~ Bin(M, p), F ~ Bin(T - M, p) indépendants (agent aveugle à tous les tirages)."""
    def p_silence(m):
        pmf_s = [math.exp(v) for v in log_binom_pmf(m, p)]
        pmf_f = [math.exp(v) for v in log_binom_pmf(t - m, p)]
        tail = [0.0] * (len(pmf_f) + 1)
        acc = 0.0
        for k in range(len(pmf_f) - 1, -1, -1):
            acc += pmf_f[k]
            tail[k] = min(1.0, acc)
        nf, total = t - m, 0.0
        for s, ps in enumerate(pmf_s):
            if ps < 1e-18:
                continue
            lo, hi = 0, nf + 1
            while lo < hi:
                mid = (lo + hi) // 2
                if log_richesse(s, s + mid, ms) < log_seuil:
                    hi = mid
                else:
                    lo = mid + 1
            total += ps * tail[lo]
        return total
    lo, hi = 0, t
    while lo < hi:
        mid = (lo + hi) // 2
        if p_silence(mid) <= beta:
            hi = mid
        else:
            lo = mid + 1
    return lo


# ------------------------------------------------------------------ blocs
def bloc_a():
    print("[A] Deux lectures de « moyenne de rapports, multipliée d'audit en audit ».")
    print("    Le rapport d'un audit est affine en son taux : la moyenne des rapports EST le rapport au taux moyen.")
    for nom, g in GRILLES.items():
        moy = sum(g) / len(g)
        ecart = 0.0
        for x in (0, 1):
            m1 = sum(math.exp(uab(m)[0] if x else -uab(m)[1]) for m in g) / len(g)
            m2 = math.exp(uab(moy)[0] if x else -uab(moy)[1])
            ecart = max(ecart, abs(m1 - m2))
        u, b, a = uab(moy)
        u1, b1, a1 = uab(min(g))
        print("      %-38s : taux moyen %.4f fois le taux acceptable ; écart entre les deux écritures %.1e" % (nom, moy, ecart))
        print("        produit des moyennes : aucun taux réel sous %.4f fois le taux acceptable ne fait croître la richesse" % (b / a / RHO0))
        print("        moyenne des produits (mélange) : bande sans croissance jusqu'à %.4f fois ; pente limite de l'excès %.5f par épisode"
              % (b1 / a1 / RHO0, b1 / a1 - RHO0))
    print("    Le programme de la note v1 calculait le mélange ; sa phrase se lisait aussi comme le produit des moyennes.")
    print()


def bloc_b():
    print("[B] Borne garantie de l'excès avant l'annonce (théorème de la re-dérivation, réimplémenté ici) :")
    print("    avec probabilité >= 1 - beta, pour tout m avant l'annonce et m <= n : (endommagés non signalés) - rho0 m < borne.")
    print("    rho0 = %.2f, alpha = %.2f, beta = %.2f. Entre parenthèses : valeur publiée par la re-dérivation." % (RHO0, ALPHA, BETA))
    ecart_max = 0.0
    for nom, g in GRILLES.items():
        for q in (0.05, 0.20):
            ligne = []
            for n in (1000, 4000, 16000):
                val, mult, lam = borne(g, q, n)
                ref = REDERIVATION.get((nom, q, n))
                if ref is not None:
                    ecart_max = max(ecart_max, abs(val - ref))
                    ligne.append("n = %5d : %7.1f (%.1f)" % (n, val, ref))
                else:
                    ligne.append("n = %5d : %7.1f" % (n, val))
            print("      %-38s audit %.2f : %s" % (nom, q, " ; ".join(ligne)))
    print("    plus grand écart à la re-dérivation sur ses douze valeurs : %.2f (accord attendu à 0,1 près)" % ecart_max)
    assert ecart_max < 0.15, ecart_max
    print()


def bloc_c():
    print("[C] Table de la règle corrigée (mélange, grille descendante de douze taux) : borne garantie de l'excès,")
    print("    part de n, et borne / racine(n rho0 (1 - rho0) / q). Audit 1,00 : borne sur chaque trajectoire (sans beta).")
    g = GRILLES[CORRIGEE]
    for q in (0.05, 0.20, 1.00):
        for n in (1000, 4000, 16000, 100000, 1000000, 10000000):
            val, mult, lam = borne(g, q, n)
            rap = val / math.sqrt(n * RHO0 * (1.0 - RHO0) / q)
            print("      audit %.2f, n = %8d : borne %9.1f ; %6.3f %% de n ; rapport %.2f ; taux retenu %.4f fois"
                  % (q, n, val, 100.0 * val / n, rap, mult))
    print("    Même table pour la grille v1 (cinq taux) : la borne finit linéaire.")
    g1 = GRILLES["v1, cinq taux (1,25 à 5)"]
    for q in (0.20,):
        for n in (1000, 4000, 16000, 100000, 1000000, 10000000):
            val, mult, lam = borne(g1, q, n)
            rap = val / math.sqrt(n * RHO0 * (1.0 - RHO0) / q)
            print("      audit %.2f, n = %8d : borne %9.1f ; %6.3f %% de n ; rapport %.2f ; taux retenu %.4f fois"
                  % (q, n, val, 100.0 * val / n, rap, mult))
    print()


def bloc_d():
    print("[D] D'où venaient 100, 190 et 392 : valeur à horizon fixe de la note v1 (silence jusqu'à T, agent aveugle")
    print("    à tous les tirages, loi exacte), à côté de la borne garantie [B] (uniforme dans le temps, agent qui voit")
    print("    les tirages passés). Excès au-delà de rho0 T, audit 0,20.")
    log_seuil = math.log(1.0 / ALPHA)
    for nom in ("v1, cinq taux (1,25 à 5)", CORRIGEE):
        ms = mises(GRILLES[nom])
        ligne = []
        for t in (1000, 4000, 16000):
            me = m_etoile_horizon_fixe(t, 0.20, ms, log_seuil) - RHO0 * t
            bg = borne(GRILLES[nom], 0.20, t)[0]
            ligne.append("T = %5d : horizon fixe %6.1f, garantie %6.1f" % (t, me, bg))
        print("      %-38s %s" % (nom, " ; ".join(ligne)))
    print()


def bloc_e():
    print("[E] Objets de contrôle, mondes à taux constant, programmation dynamique exacte (en audits).")
    log_seuil = math.log(1.0 / ALPHA)
    jal = {1000, 4000, 12000}
    for nom in ("v1, cinq taux (1,25 à 5)", CORRIGEE):
        ms = mises(GRILLES[nom])
        print("      %s" % nom)
        lus, _ = monde_constant(RHO0, 12000, ms, log_seuil, jal)
        print("        monde valide (taux acceptable) : annonce %.4f à 1 000 audits, %.4f à 4 000, %.4f à 12 000 (doit rester <= %.2f)"
              % (lus[1000], lus[4000], lus[12000], ALPHA))
        for mult in (1.10, 1.25, 1.50, 2.00, 3.00):
            lus, med = monde_constant(mult * RHO0, 12000, ms, log_seuil, jal)
            print("        taux réel %.2f fois : annonce %.4f à 1 000 audits, %.4f à 4 000, %.4f à 12 000 ; médiane %s"
                  % (mult, lus[1000], lus[4000], lus[12000], ("%d audits" % med) if med else "non atteinte à 12 000"))
    print()


def bloc_f():
    print("[F] Jusqu'où douze taux suffisent : horizon où l'écart utile au-dessus du taux acceptable,")
    print("    racine(2 L (1 - rho0) / (q rho0 n)) avec L = log(12 / alpha), tombe au double du plus petit écart de la grille.")
    g = GRILLES[CORRIGEE]
    eps_min = min(g) - 1.0
    big_l = math.log(len(g) / ALPHA)
    for q in (0.05, 0.20, 1.00):
        n_max = 2.0 * big_l * (1.0 - RHO0) / (q * RHO0 * (2.0 * eps_min) ** 2)
        print("      audit %.2f : plus petit écart %.5f ; horizon d'environ %.2e épisodes" % (q, eps_min, n_max))
    u1, b1, a1 = uab(min(g))
    print("      au-delà, pente limite de l'excès : %.2e par épisode" % (b1 / a1 - RHO0))
    print()


if __name__ == "__main__":
    print("Calculs de l'erratum 1 de la note « science de la détection » : règle « moniteur invalide » corrigée.")
    print("Lois exactes et formules fermées, aucun tirage, aucune donnée du programme. Entrées : suppositions d'illustration. Non contre-lu.")
    print()
    bloc_a()
    bloc_b()
    bloc_c()
    bloc_d()
    bloc_e()
    bloc_f()
