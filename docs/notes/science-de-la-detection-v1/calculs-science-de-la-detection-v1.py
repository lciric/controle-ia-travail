#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « science de la détection » (v1).

Lois exactes et programmation dynamique exacte ; aucun tirage, aucune donnée
du programme, bibliothèque standard seule. Toutes les valeurs d'entrée sont
des suppositions d'illustration. Non contre-lu.

Usage : python calculs-science-de-la-detection-v1.py > calculs-science-de-la-detection-v1.txt
"""
import itertools
import math


# ---------------------------------------------------------------- outils
def log_binom_pmf(n, p):
    """Liste des log-probabilités de Bin(n, p)."""
    if p <= 0.0:
        return [0.0] + [-math.inf] * n
    if p >= 1.0:
        return [-math.inf] * n + [0.0]
    lp, lq = math.log(p), math.log1p(-p)
    lg = math.lgamma
    return [lg(n + 1) - lg(k + 1) - lg(n - k + 1) + k * lp + (n - k) * lq
            for k in range(n + 1)]


def binom_pmf(n, p):
    return [math.exp(v) for v in log_binom_pmf(n, p)]


def tail_ge(pmf):
    """tail[k] = P(X >= k), tail[len] = 0."""
    out = [0.0] * (len(pmf) + 1)
    acc = 0.0
    for k in range(len(pmf) - 1, -1, -1):
        acc += pmf[k]
        out[k] = min(1.0, acc)
    return out


def cdf_le(pmf):
    out, acc = [], 0.0
    for v in pmf:
        acc += v
        out.append(min(1.0, acc))
    return out


# ------------------------------------------- règle « moniteur invalide »
ALTERNATIVES = (1.25, 1.5, 2.0, 3.0, 5.0)   # multiples de q_a, poids égaux


def paris(q_a):
    """Mises du mélange : rapports de vraisemblance Bern(q_j) contre Bern(q_a)."""
    out = []
    for mult in ALTERNATIVES:
        q_j = min(mult * q_a, 0.95)
        lam = (q_j - q_a) / (q_a * (1.0 - q_a))
        out.append((math.log1p(lam * (1.0 - q_a)), math.log1p(-lam * q_a)))
    return out


def log_richesse(s, n, mises):
    """log de la richesse du mélange après n audits dont s « endommagé non signalé »."""
    vals = [a * s + b * (n - s) for a, b in mises]
    m = max(vals)
    return m + math.log(sum(math.exp(v - m) for v in vals)) - math.log(len(vals))


def seuil_s(n, mises, log_seuil):
    """Plus petit s (0..n+1) tel que la richesse atteint le seuil après n audits."""
    lo, hi = 0, n + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if log_richesse(mid, n, mises) >= log_seuil:
            hi = mid
        else:
            lo = mid + 1
    return lo


def annonce_avant(q, n_max, mises, log_seuil):
    """Monde à taux constant q : probabilité d'annonce au plus tard à l'audit n,
    et nombre médian d'audits avant l'annonce (None si non atteint)."""
    vivant = {0: 1.0}
    cumul, mediane = 0.0, None
    for n in range(1, n_max + 1):
        thr = seuil_s(n, mises, log_seuil)
        suivant = {}
        for s, pr in vivant.items():
            for ds, w in ((0, 1.0 - q), (1, q)):
                s2 = s + ds
                if s2 >= thr:
                    cumul += pr * w
                else:
                    suivant[s2] = suivant.get(s2, 0.0) + pr * w
        vivant = suivant
        if mediane is None and cumul >= 0.5:
            mediane = n
    return cumul, mediane


def p_silence(m, t, p, mises, log_seuil):
    """Majorant exact de P(règle muette à T | M_T = m) : S ~ Bin(m, p) audits
    endommagés non signalés, F ~ Bin(t - m, p) autres audits, indépendants ;
    muette à T implique richesse(S, S + F) < seuil."""
    pmf_s = binom_pmf(m, p)
    tail_f = tail_ge(binom_pmf(t - m, p))
    nf = t - m
    total = 0.0
    for s, ps in enumerate(pmf_s):
        if ps < 1e-18:
            continue
        # plus petit f tel que richesse(s, s + f) < seuil (la richesse décroît en f)
        lo, hi = 0, nf + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if log_richesse(s, s + mid, mises) < log_seuil:
                hi = mid
            else:
                lo = mid + 1
        total += ps * tail_f[lo]
    return min(1.0, total)


def m_etoile(t, p, q_a, alpha, beta):
    mises = paris(q_a)
    log_seuil = math.log(1.0 / alpha)
    lo, hi = 0, t
    while lo < hi:
        mid = (lo + hi) // 2
        if p_silence(mid, t, p, mises, log_seuil) <= beta:
            hi = mid
        else:
            lo = mid + 1
    return lo


def bloc_a():
    print("[A] Règle « moniteur invalide », ligne 1 (ce qui passe sans alerte).")
    print("    U = 1 si l'épisode audité est endommagé selon l'oracle ET n'a pas été signalé par le moniteur.")
    print("    Nul : à tout instant P(U = 1 | passé) <= q_a. Richesse : moyenne de cinq rapports de vraisemblance")
    print("    Bern(k q_a) contre Bern(q_a), k = 1,25 ; 1,5 ; 2 ; 3 ; 5. Annonce quand la richesse atteint 1/alpha.")
    alpha, beta = 0.05, 0.10
    print("    alpha (fausse annonce par déploiement) = %.2f ; beta (silence à tort) = %.2f." % (alpha, beta))
    print()
    print("    (i) Objets de contrôle, mondes à taux constant, programmation dynamique exacte sur N audits :")
    for q_a in (0.05, 0.10):
        mises = paris(q_a)
        log_seuil = math.log(1.0 / alpha)
        for n_max in (1000, 4000):
            pa, _ = annonce_avant(q_a, n_max, mises, log_seuil)
            print("        q_a = %.2f, monde valide (taux = q_a), N = %4d audits : annonce %.4f (doit rester <= %.2f)"
                  % (q_a, n_max, pa, alpha))
        for mult in (1.5, 2.0, 3.0):
            pa, med = annonce_avant(mult * q_a, 4000, mises, log_seuil)
            print("        q_a = %.2f, monde aveugle (taux = %.3f), N = 4000 audits : annonce %.4f ; médiane %s audits"
                  % (q_a, mult * q_a, pa, med if med is not None else "non atteinte"))
    print()
    print("    (ii) Borne sans hypothèse sur la politique d'attaque (tirages d'audit indépendants de l'agent) :")
    print("        m* = plus petit nombre M d'épisodes « endommagés non signalés » parmi T tel que")
    print("        P(règle muette à T | M) <= beta. Pour toute politique : P(muette à T et M_T >= m*) <= beta.")
    print("        excès = m* - q_a T ; rapport = excès / racine(T q_a (1 - q_a) / p).")
    for q_a in (0.05, 0.10):
        for p in (0.05, 0.20, 1.00):
            for t in (1000, 4000, 16000):
                ms = m_etoile(t, p, q_a, alpha, beta)
                exc = ms - q_a * t
                rap = exc / math.sqrt(t * q_a * (1.0 - q_a) / p)
                print("        q_a = %.2f, audit p = %.2f, T = %5d : m* = %5d ; excès = %7.1f (%.2f %% de T) ; rapport = %.2f"
                      % (q_a, p, t, ms, exc, 100.0 * exc / t, rap))
    print()


# ------------------------------------------------------ surprise sous 0,3
def bloc_b():
    print("[B] Surprise par étape estimée par K continuations de chaque côté d'une frontière (deux estimations")
    print("    indépendantes, binomiales, réussite attendue vraie v des deux côtés : surprise vraie nulle).")
    print("    écart type de la surprise estimée ; probabilité qu'elle dépasse 0,3 en valeur absolue (exacte).")
    for v in (0.5, 0.2):
        for k in (4, 8, 16, 32, 64, 128):
            pmf = binom_pmf(k, v)
            pr = 0.0
            for a, pa in enumerate(pmf):
                for b, pb in enumerate(pmf):
                    if abs(a - b) / k > 0.3 + 1e-12:
                        pr += pa * pb
            sd = math.sqrt(2.0 * v * (1.0 - v) / k)
            print("        v = %.1f, K = %3d : écart type %.3f ; P(|surprise estimée| > 0,3 | surprise vraie nulle) = %.4f"
                  % (v, k, sd, pr))
    print("    Plafond de corrélation d'une sonde parfaite contre l'étiquette bruitée : racine(fidélité),")
    print("    fidélité = var(vraie) / (var(vraie) + var(bruit)), bruit à v = 0,5.")
    for sd_vraie in (0.05, 0.10, 0.20):
        ligne = []
        for k in (4, 16, 64):
            bruit = 2.0 * 0.25 / k
            fid = sd_vraie ** 2 / (sd_vraie ** 2 + bruit)
            ligne.append("K = %2d : %.2f" % (k, math.sqrt(fid)))
        print("        écart type vrai des surprises %.2f -> plafond  %s" % (sd_vraie, " ; ".join(ligne)))
    print("    Évaluation en agrégat : nombre d'étapes par classe de surprise prédite pour connaître la surprise")
    print("    moyenne réalisée à +/- 0,02 (95 %), bruit à v = 0,5 seul.")
    for k in (4, 8, 16):
        sd = math.sqrt(2.0 * 0.25 / k)
        n = math.ceil((1.96 * sd / 0.02) ** 2)
        print("        K = %2d : %5d étapes par classe" % (k, n))
    print()


# ------------------------------------------------------- coupes minimales
MECANISMES = {
    "sonde d'intention": {"S1", "S8", "S9"},
    "réussite attendue lue + issue calculée": {"S1", "S8", "S4"},
    "nouveauté sur activations": {"S1", "S2", "S8"},
    "plancher d'audit au hasard": {"S4", "S5", "S6"},
    "règle « moniteur invalide »": {"S4", "S5", "S2"},
    "rang de l'action contre le jumeau": {"S3", "S1"},
    "comparaison par paires en aveugle au jumeau": {"S3", "S12"},
    "attestation exigée et vérifiée": {"S13", "S4"},
}
LIBELLES = {
    "S1": "l'attaque déplace ce que la sonde lit",
    "S2": "les témoins ont la loi de l'honnête du régime",
    "S3": "le jumeau a la politique de l'honnête",
    "S4": "l'oracle reconnaît le dommage qu'il regarde",
    "S5": "le tirage d'audit est secret et indépendant",
    "S6": "le dommage par épisode est plafonné",
    "S8": "l'agent ne déplace pas ses représentations",
    "S9": "l'attaque ressemble à celles déjà vues",
    "S12": "un lecteur aveugle perçoit le déficit du produit",
    "S13": "une attestation fausse est vérifiable ou lisible",
}


def coupes(systeme):
    """Plus petits ensembles de suppositions dont la violation aveugle tout le système
    (un mécanisme est tenu pour aveugle dès qu'une de ses suppositions tombe)."""
    univers = sorted(set().union(*(MECANISMES[m] for m in systeme)))
    for taille in range(1, len(univers) + 1):
        trouve = [c for c in itertools.combinations(univers, taille)
                  if all(MECANISMES[m] & set(c) for m in systeme)]
        if trouve:
            return taille, trouve
    return 0, []


def bloc_c():
    print("[C] Coupes minimales : combien de suppositions faut-il violer ensemble pour aveugler tout le système ?")
    print("    Lecture prudente : un mécanisme est aveugle dès qu'une supposition qu'il consomme est violée.")
    print("    Les ensembles de suppositions par mécanisme sont ma lecture, non mesurée.")
    systemes = [
        ["sonde d'intention"],
        ["sonde d'intention", "nouveauté sur activations"],
        ["sonde d'intention", "réussite attendue lue + issue calculée"],
        ["sonde d'intention", "plancher d'audit au hasard"],
        ["sonde d'intention", "plancher d'audit au hasard", "règle « moniteur invalide »"],
        ["sonde d'intention", "plancher d'audit au hasard", "comparaison par paires en aveugle au jumeau"],
        ["sonde d'intention", "plancher d'audit au hasard", "comparaison par paires en aveugle au jumeau",
         "attestation exigée et vérifiée"],
    ]
    for sysm in systemes:
        taille, liste = coupes(sysm)
        print("      système : " + " + ".join(sysm))
        print("        ordre %d ; %d coupe(s) minimale(s) ; exemples : %s"
              % (taille, len(liste), " | ".join("{" + ", ".join(c) + "}" for c in liste[:4])))
    print("    Libellés : " + " ; ".join("%s = %s" % kv for kv in sorted(LIBELLES.items(), key=lambda kv: int(kv[0][1:]))))
    print()


# ------------------------------------------------------ capture-recapture
def bloc_d():
    print("[D] Angle mort commun de deux oracles, estimé par capture et recapture (Lincoln-Petersen).")
    print("    Chaque oracle voit un dommage vrai avec probabilité r ; corrélation rho de leurs détections.")
    print("    part vraie manquée par les deux ; part estimée en supposant l'indépendance (valeurs en espérance).")
    for r in (0.6, 0.8):
        for rho in (0.0, 0.3, 0.6):
            both = r * r + rho * r * (1.0 - r)
            either = 2.0 * r - both
            vraie = 1.0 - either
            n_hat = r * r / both            # N estimé / N vrai
            estimee = max(0.0, n_hat - either) / n_hat if n_hat > 0 else 0.0
            print("        r = %.1f, rho = %.1f : manquée par les deux, vraie %.3f ; estimée %.3f (estimateur du total / total vrai = %.2f)"
                  % (r, rho, vraie, estimee, n_hat))
    print("    Lecture : dès que les oracles se trompent ensemble, l'estimation est une borne basse de l'angle mort.")
    print()


# --------------------------------------------- comparaison par paires
def bloc_e():
    print("[E] Comparaison par paires en aveugle au jumeau : nul exact P(le produit du suspect perd) = 1/2")
    print("    (ordre tiré au hasard). Plus petit nombre de paires n et seuil c tels que, test unilatéral exact,")
    print("    P(pertes >= c | 1/2) <= 0,01 et P(pertes >= c | 1/2 + d) >= 0,90.")
    for d in (0.05, 0.10, 0.15, 0.20, 0.30):
        n = 10
        while True:
            pmf0 = binom_pmf(n, 0.5)
            t0 = tail_ge(pmf0)
            c = next(k for k in range(n + 2) if t0[k] <= 0.01)
            t1 = tail_ge(binom_pmf(n, 0.5 + d))
            if t1[c] >= 0.90:
                print("        d = %.2f : n = %4d paires, alerte si pertes >= %4d (risque %.4f, puissance %.4f)"
                      % (d, n, c, t0[c], t1[c]))
                break
            n += 1 if n < 200 else 5
    print()


if __name__ == "__main__":
    print("Calculs de la note « science de la détection » (v1) : lois exactes, aucun tirage, aucune donnée du programme.")
    print("Toutes les valeurs d'entrée sont des suppositions d'illustration. Non contre-lu.")
    print()
    bloc_a()
    bloc_b()
    bloc_c()
    bloc_d()
    bloc_e()
