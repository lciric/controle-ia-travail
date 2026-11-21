#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « boucle audit, recapture, réapprentissage » (v1).

Pièce de classe C, non contre-lue. Aucune donnée du programme : toutes les entrées sont des
suppositions d'illustration, écrites dans chaque bloc. Lois exactes là où c'est dit ; tirages
ailleurs, par numpy.random.SeedSequence (entropie fixe, une clé dérivée par bloc et par case).
Les prévisions sont écrites dans le code avant l'exécution (PREVU), puis comparées (assert).

Usage : python3 calculs-boucle-audit-recapture-v1.py > calculs-boucle-audit-recapture-v1.txt
Rejoué deux fois, la sortie doit être identique à l'octet.

Monde commun aux blocs A, C et E (supposé) : un état interne est un vecteur de dimension d ;
un épisode honnête y vaut un bruit gaussien réduit ; un épisode endommagé y ajoute un écart de
norme Delta (en écarts types) le long d'une direction inconnue du défenseur. Une sonde est une
direction w ; elle signale quand le score w.x dépasse le quantile 0,99 des scores honnêtes
(1 % de fausses alertes). « Réapprendre » = différence des moyennes entre les épisodes dits
endommagés et des épisodes dits sains.
"""
import math
import sys

import numpy as np

ENTROPIE = 20261121
ALPHA = 0.01


def gen(*cle):
    """Générateur dérivé par bloc et par case (R9)."""
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=tuple(int(c) for c in cle)))


def Phi(x):
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def Phi_inv(p):
    a, b = -12.0, 12.0
    for _ in range(200):
        m = 0.5 * (a + b)
        if Phi(m) < p:
            a = m
        else:
            b = m
    return 0.5 * (a + b)


Z = Phi_inv(1.0 - ALPHA)


def log_binom_pmf(n, k, p):
    if p <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if p >= 1.0:
        return 0.0 if k == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(p) + (n - k) * math.log1p(-p))


def binom_sf(n, k, p):
    """P(Bin(n, p) >= k), somme exacte."""
    if k <= 0:
        return 1.0
    return math.fsum(math.exp(log_binom_pmf(n, j, p)) for j in range(k, n + 1))


def borne_basse_exacte(n, k, niveau=0.95):
    """Borne inférieure de Clopper et Pearson, unilatérale, pour k succès sur n."""
    if k == 0:
        return 0.0
    a, b = 0.0, 1.0
    for _ in range(200):
        m = 0.5 * (a + b)
        if binom_sf(n, k, m) < 1.0 - niveau:
            a = m
        else:
            b = m
    return 0.5 * (a + b)


def titre(t):
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)


def f3(x):
    return f"{x:6.3f}"


# ----------------------------------------------------------------------------------------------
# BLOC A — La recapture relue par la sonde qu'elle vient d'instruire
# ----------------------------------------------------------------------------------------------
def approx_vrai(delta, d, n, m):
    """Rappel vrai (à 1 % de fausses alertes) d'une sonde réapprise sur n positifs et m négatifs."""
    return Phi(delta * delta / math.sqrt(delta * delta + d / n + d / m) - Z)


def approx_relu(delta, d, n, m):
    """Recapture relue sur les n positifs qui ont instruit la sonde (en échantillon)."""
    return Phi((delta * delta + d / n) / math.sqrt(delta * delta + d / n + d / m) - Z)


def bloc_A():
    titre("BLOC A — La recapture, selon l'ordre entre l'épreuve et la leçon (tirages ; d = 4096)")
    d, m_ref, reps = 4096, 400, 100
    tailles = (3, 10, 30, 100, 300)
    print("Supposé : d = 4096 ; m = 400 témoins honnêtes servent de négatifs ; n épisodes endommagés audités")
    print("servent de positifs ; écart Delta (en écarts types) le long d'une direction fixe ; 100 répétitions.")
    print("Colonnes : vrai = rappel de la sonde finale sur des dommages neufs (loi exacte, w donné) ;")
    print("  relue = part des n positifs d'apprentissage que la sonde finale signale (en échantillon) ;")
    print("  pli = recapture sur un tiers retenu par tirage, sonde apprise sur les deux autres tiers ;")
    print("  suite = recapture « épreuve puis apprentissage » : l'épisode i est noté par la sonde apprise")
    print("          sur les épisodes 1 à i-1, puis il l'instruit ; fin = dernier tiers de cette suite ;")
    print("  fa_vraie = fausses alertes réelles quand le seuil « 1 % » est calé sur les m témoins qui ont")
    print("             servi de négatifs (au lieu de témoins neufs).")
    print()
    print("  Delta     n |   vrai   relue     pli   suite     fin | fa_vraie | approx. vrai  approx. relue")
    res = {}
    for delta in (0.0, 2.0, 4.0):
        g = gen(1, int(round(delta * 10)))
        acc = {n: [] for n in tailles}
        for _ in range(reps):
            Y = g.standard_normal((m_ref, d))
            negmean = Y.mean(axis=0)
            Xmax = g.standard_normal((max(tailles), d))
            Xmax[:, 0] += delta
            u_premier = g.random(len(tailles))
            for j, n in enumerate(tailles):
                X = Xmax[:n]
                w = X.mean(axis=0) - negmean
                nw = float(np.linalg.norm(w))
                vrai = Phi(delta * float(w[0]) / nw - Z)
                relue = float(np.mean(X @ w > Z * nw))
                n_v = max(1, n // 3)
                n_t = n - n_v
                wt = X[:n_t].mean(axis=0) - negmean
                nwt = float(np.linalg.norm(wt))
                pli = float(np.mean(X[n_t:] @ wt > Z * nwt))
                drapeaux = np.empty(n)
                drapeaux[0] = 1.0 if u_premier[j] < ALPHA else 0.0  # sonde en place, aveugle : alerte au taux alpha
                if n > 1:
                    C = np.cumsum(X[:-1], axis=0) / np.arange(1, n)[:, None] - negmean
                    s = np.einsum("ij,ij->i", X[1:], C)
                    nc = np.sqrt(np.einsum("ij,ij->i", C, C))
                    drapeaux[1:] = (s > Z * nc).astype(float)
                suite = float(drapeaux.mean())
                fin = float(drapeaux[-n_v:].mean())
                seuil_cale = float(np.quantile(Y @ w, 1.0 - ALPHA, method="higher"))
                fa_vraie = 1.0 - Phi(seuil_cale / nw)
                acc[n].append((vrai, relue, pli, suite, fin, fa_vraie))
        for n in tailles:
            a = np.array(acc[n]).mean(axis=0)
            res[(delta, n)] = a
            print(f"  {delta:5.1f} {n:5d} | {f3(a[0])}  {f3(a[1])}  {f3(a[2])}  {f3(a[3])}  {f3(a[4])} |  {f3(a[5])}  |"
                  f"    {f3(approx_vrai(delta, d, n, m_ref))}        {f3(approx_relu(delta, d, n, m_ref))}")
        print()

    # A3 — canal de retour ouvert : l'agent voit chaque changement de version et déplace son écart
    g = gen(1, 99)
    n, delta = 100, 4.0
    suites, relues = [], []
    for _ in range(reps):
        Y = g.standard_normal((m_ref, d))
        negmean = Y.mean(axis=0)
        X = g.standard_normal((n, d))
        X[np.arange(n), np.arange(n)] += delta   # une direction neuve à chaque épisode endommagé
        w = X.mean(axis=0) - negmean
        nw = float(np.linalg.norm(w))
        relues.append(float(np.mean(X @ w > Z * nw)))
        C = np.cumsum(X[:-1], axis=0) / np.arange(1, n)[:, None] - negmean
        s = np.einsum("ij,ij->i", X[1:], C)
        nc = np.sqrt(np.einsum("ij,ij->i", C, C))
        suites.append(float(np.mean(s > Z * nc)))
    a3 = (float(np.mean(suites)), float(np.mean(relues)))
    print("A3 — artefact « canal de retour ouvert » (supposé : à chaque épisode endommagé l'écart Delta = 4 prend une")
    print("     direction neuve, orthogonale aux précédentes ; n = 100) :")
    print(f"     recapture « épreuve puis apprentissage » = {f3(a3[0])} ; recapture relue en échantillon = {f3(a3[1])}")

    # PREVU (écrit avant l'exécution)
    #  objet où « la sonde s'est rétablie » est FAUX (Delta = 0, le dommage ne laisse aucune trace) :
    #    vrai = 0,010 ; pli, suite et fin au niveau des fausses alertes ; relue proche de 1 jusqu'à n = 100,
    #    encore 0,68 environ à n = 300 (formule fermée).
    for n in tailles:
        assert abs(res[(0.0, n)][0] - 0.010) < 0.002, ("vrai, Delta 0", n)
        assert res[(0.0, n)][3] < 0.03 and res[(0.0, n)][2] < 0.05, ("suite et pli, Delta 0", n)
    for n in (3, 10, 30, 100):
        assert res[(0.0, n)][1] > 0.95, ("relue, Delta 0", n)
    assert 0.55 < res[(0.0, 300)][1] < 0.80, "relue, Delta 0, n 300"
    #  objet où c'est VRAI (Delta = 4, n = 300) : vrai près de 0,58 ; pli et fin proches du vrai ; relue près de 0,99.
    assert abs(res[(4.0, 300)][0] - 0.58) < 0.04
    assert abs(res[(4.0, 300)][2] - res[(4.0, 300)][0]) < 0.08
    assert res[(4.0, 300)][1] > 0.97
    #  fausses alertes réelles, seuil calé sur les témoins qui ont instruit : prévu 0,24 (Delta 4, n 300), 0,06 (n 30).
    assert 0.15 < res[(4.0, 300)][5] < 0.33 and 0.03 < res[(4.0, 30)][5] < 0.11
    #  canal ouvert : la suite doit rester au niveau des fausses alertes, la relue rester près de 1.
    assert a3[0] < 0.03 and a3[1] > 0.95
    #  formules fermées contre tirages (contrôle de mon implémentation).
    for delta in (0.0, 2.0, 4.0):
        for n in tailles:
            assert abs(res[(delta, n)][0] - approx_vrai(delta, d, n, m_ref)) < 0.03, (delta, n)
            assert abs(res[(delta, n)][1] - approx_relu(delta, d, n, m_ref)) < 0.06, (delta, n)
    print("Contrôles du bloc A : passés.")
    return res


# ----------------------------------------------------------------------------------------------
# BLOC B — La recapture comptée sur un audit que la sonde oriente
# ----------------------------------------------------------------------------------------------
def bloc_B():
    titre("BLOC B — Recapture sur un audit orienté par la sonde : biais de vérification (loi exacte, puis tirages)")
    print("Supposé : la sonde signale un épisode endommagé avec probabilité r (son rappel vrai) ; un épisode est audité")
    print("avec probabilité p0 (plancher) s'il n'est pas signalé, p1 s'il l'est. « Naïve » = part des signalés parmi")
    print("tous les endommagés audités = r.p1 / (r.p1 + (1-r).p0). Loi exacte.")
    print()
    print("     r     p0     p1 | naïve (exacte)")
    exact = {}
    for r in (0.05, 0.20, 0.50, 0.80):
        for p0 in (0.01, 0.05, 0.20):
            for p1 in (p0, 0.5, 1.0):
                naive = r * p1 / (r * p1 + (1 - r) * p0)
                exact[(r, p0, p1)] = naive
                marque = "   (tirage sans égard au score)" if p1 == p0 else ""
                print(f"  {r:4.2f}  {p0:5.2f}  {p1:5.2f} |   {f3(naive)}{marque}")
    print()
    print("Tirages (20 000 répétitions) : N = 1 000 épisodes endommagés ; trois comptes de la recapture.")
    print("  plancher = signalés parmi les endommagés tirés par la seule pièce du plancher (probabilité p0, sans égard au score) ;")
    print("  pondérée = chaque endommagé audité compte pour l'inverse de sa probabilité d'audit ;")
    print("  « vide » = part des répétitions où le compte n'a aucun épisode.")
    print()
    print("     r     p0     p1 | naïve moy.  | plancher moy. (écart type) vide | pondérée moy. (écart type) vide")
    reps, N = 20000, 1000
    sim = {}
    for k, (r, p0, p1) in enumerate(((0.20, 0.05, 0.50), (0.20, 0.01, 0.50), (0.50, 0.05, 1.00), (0.20, 0.20, 0.20))):
        g = gen(2, k)
        Nf = g.binomial(N, r, size=reps)            # endommagés signalés
        Nu = N - Nf                                 # endommagés non signalés
        # pièce du plancher, indépendante du score
        Ff = g.binomial(Nf, p0)
        Fu = g.binomial(Nu, p0)
        # audit total : plancher ou part qui suit le score ; probabilité p1 pour un signalé, p0 sinon
        Af = Ff + g.binomial(Nf - Ff, (p1 - p0) / (1 - p0)) if p1 > p0 else Ff
        Au = Fu
        with np.errstate(divide="ignore", invalid="ignore"):
            naive = Af / (Af + Au)
            plancher = Ff / (Ff + Fu)
            ponderee = (Af / p1) / (Af / p1 + Au / p0)
        vide_p = float(np.mean(~np.isfinite(plancher)))
        vide_w = float(np.mean(~np.isfinite(ponderee)))
        sim[(r, p0, p1)] = (float(np.nanmean(naive)), float(np.nanmean(plancher)), float(np.nanstd(plancher)),
                            float(np.nanmean(ponderee)), float(np.nanstd(ponderee)))
        s = sim[(r, p0, p1)]
        print(f"  {r:4.2f}  {p0:5.2f}  {p1:5.2f} |   {f3(s[0])}    |    {f3(s[1])}      ({f3(s[2])})  {vide_p:5.3f} |"
              f"    {f3(s[3])}      ({f3(s[4])})  {vide_w:5.3f}")
    # PREVU : r = 0,20, p0 = 0,05, p1 = 0,50 : naïve = 0,1 / (0,1 + 0,04) = 0,714 ; plancher et pondérée proches de 0,20.
    assert abs(exact[(0.20, 0.05, 0.5)] - 0.7143) < 1e-3
    assert abs(sim[(0.20, 0.05, 0.50)][0] - 0.714) < 0.01
    assert abs(sim[(0.20, 0.05, 0.50)][1] - 0.20) < 0.01 and abs(sim[(0.20, 0.05, 0.50)][3] - 0.20) < 0.02
    # objet sain : tirage sans égard au score (p1 = p0) : la naïve doit valoir r.
    assert abs(exact[(0.20, 0.20, 0.20)] - 0.20) < 1e-12 and abs(sim[(0.20, 0.20, 0.20)][0] - 0.20) < 0.01
    print("Contrôles du bloc B : passés.")


# ----------------------------------------------------------------------------------------------
# BLOC C — Les étiquettes que le plancher livre, et ce que chaque échelon en fait
# ----------------------------------------------------------------------------------------------
def p_bon_choix(delta_r, n, M, pas=4001):
    """P(le détecteur qui voit l'écart a la plus haute moyenne sur n positifs), M détecteurs, intégration de Simpson."""
    s = 1.0 / math.sqrt(n)
    a, b = delta_r - 10 * s, delta_r + 10 * s
    h = (b - a) / (pas - 1)
    tot = 0.0
    for i in range(pas):
        x = a + i * h
        dens = math.exp(-0.5 * ((x - delta_r) / s) ** 2) / (s * math.sqrt(2 * math.pi))
        val = dens * Phi(x / s) ** (M - 1)
        coef = 1 if i in (0, pas - 1) else (4 if i % 2 == 1 else 2)
        tot += coef * val
    return tot * h / 3.0


def bloc_C(res_A):
    titre("BLOC C — Les étiquettes livrées par le plancher avant le seuil toléré, et les échelons d'ajustement")
    print("C1 (loi exacte). Régime de signature, taux d'audit réglé par la table du seuil : p.q = 1 - 0,05^(1/K).")
    print("N = nombre d'épisodes endommagés audités et reconnus parmi les K premiers endommagés : binomiale (K, p.q).")
    print()
    print("       K     p.q   | moyenne de N | P(N = 0)  P(N >= 3)  P(N >= 5)  P(N >= 10)  P(N >= 30)")
    moy = {}
    for K in (30, 100, 300, 1000):
        pq = 1.0 - 0.05 ** (1.0 / K)
        moy[K] = K * pq
        print(f"  {K:6d}  {pq:7.4f} |    {K * pq:6.3f}    |  {binom_sf(K, 0, pq) - binom_sf(K, 1, pq):6.4f}    {binom_sf(K, 3, pq):6.4f}"
              f"     {binom_sf(K, 5, pq):6.4f}     {binom_sf(K, 10, pq):7.5f}     {binom_sf(K, 30, pq):9.2e}")
    print("  Limite quand K grandit : moyenne = ln 20 =", f"{math.log(20):.3f}", "; loi de Poisson de ce paramètre.")
    print()
    print("  Avec un taux d'audit c fois celui de la table (K = 300) :")
    for c in (1, 3, 10, 30):
        pq = min(1.0, c * (1.0 - 0.05 ** (1.0 / 300)))
        print(f"    c = {c:2d} : p.q = {pq:6.4f} ; moyenne de N = {300 * pq:6.2f} ; P(N >= 10) = {binom_sf(300, 10, pq):6.4f} ;"
              f" P(N >= 30) = {binom_sf(300, 30, pq):6.4f}")
    # PREVU : moyenne entre 2,8 et 3,0 quel que soit K ; P(N = 0) = 0,05 par construction ; P(N >= 10) de l'ordre de 0,001.
    for K in moy:
        assert 2.8 < moy[K] < 3.0
        pq = 1.0 - 0.05 ** (1.0 / K)
        assert abs((1 - pq) ** K - 0.05) < 1e-9
    assert binom_sf(1000, 10, 1.0 - 0.05 ** (1.0 / 1000)) < 0.002

    print()
    print("C2 (formules approchées, vérifiées par tirages plus bas). Rappel à 1 % de fausses alertes selon le nombre n")
    print("d'étiquettes positives, pour trois échelons. Supposé : écart complet Delta = 4 en dimension d = 4096 ; une réserve")
    print("scellée de M = 20 détecteurs dont l'espace porte la moitié de l'écart (Delta_r = 2), un seul détecteur le voyant ;")
    print("m témoins honnêtes pour les négatifs.")
    print("  choisir   = prendre, dans la réserve, le détecteur de plus haute moyenne sur les n positifs ;")
    print("  repondérer = différence des moyennes dans l'espace des M scores de la réserve ;")
    print("  réapprendre = différence des moyennes en dimension d.")
    d, M, delta, delta_r = 4096, 20, 4.0, 2.0
    plafond_reserve = Phi(delta_r - Z)
    print(f"  Plafonds (étiquettes sans limite, m sans limite) : réserve {f3(plafond_reserve)} ; dimension complète {f3(Phi(delta - Z))}")
    print()
    print("       n | choisir  P(bon choix) | repondérer (m = 400) | réapprendre (m = 400)  (m = 4 000)  (m = 40 000)")
    table = {}
    for n in (1, 3, 10, 30, 100, 300, 1000, 3000):
        pb = p_bon_choix(delta_r, n, M)
        e1 = pb * plafond_reserve + (1 - pb) * ALPHA
        e2 = Phi(delta_r ** 2 / math.sqrt(delta_r ** 2 + M / n + M / 400) - Z)
        e3 = [approx_vrai(delta, d, n, m) for m in (400, 4000, 40000)]
        table[n] = (e1, pb, e2, e3)
        print(f"  {n:6d} |  {f3(e1)}     {f3(pb)}    |       {f3(e2)}         |       {f3(e3[0])}          {f3(e3[1])}        {f3(e3[2])}")
    # croisement entre « choisir » (plafond de la réserve) et « réapprendre » à m = 400
    n_croise = None
    for n in range(1, 5000):
        if approx_vrai(delta, d, n, 400) >= plafond_reserve:
            n_croise = n
            break
    print(f"  Réapprendre en dimension complète (m = 400) ne rejoint le plafond de la réserve ({f3(plafond_reserve)}) qu'à n = {n_croise} étiquettes.")
    lim400 = Phi(delta * delta / math.sqrt(delta * delta + d / 400) - Z)
    print(f"  Plafond du réapprentissage quand n grandit, à m = 400 témoins : {f3(lim400)} (au lieu de {f3(Phi(delta - Z))}) : la taille de la")
    print("  référence honnête borne aussi la sonde réapprise.")
    # PREVU : croisement vers n = 103 (calcul à la main) ; plafond à m = 400 vers 0,79.
    assert 95 <= n_croise <= 112
    assert abs(lim400 - 0.79) < 0.02
    # contrôle croisé avec les tirages du bloc A (Delta = 4)
    for n in (30, 100, 300):
        assert abs(table[n][3][0] - res_A[(4.0, n)][0]) < 0.03

    # tirages de contrôle des deux premiers échelons
    print()
    print("  Tirages de contrôle (20 000 répétitions) : P(bon choix) et rappel après repondération.")
    reps = 20000
    for k, n in enumerate((3, 10, 30)):
        g = gen(3, k)
        moyennes = g.standard_normal((reps, M)) / math.sqrt(n)
        moyennes[:, 0] += delta_r
        pb_sim = float(np.mean(np.argmax(moyennes, axis=1) == 0))
        # repondération : différence des moyennes en dimension M
        a = g.standard_normal((reps, M)) * math.sqrt(1.0 / n + 1.0 / 400)
        w = a.copy()
        w[:, 0] += delta_r
        nw = np.linalg.norm(w, axis=1)
        e2_sim = float(np.mean([Phi(delta_r * w[i, 0] / nw[i] - Z) for i in range(0, reps, 10)]))
        print(f"    n = {n:3d} : P(bon choix) tirée {f3(pb_sim)} contre {f3(table[n][1])} ; repondérer tiré {f3(e2_sim)} contre {f3(table[n][2])}")
        assert abs(pb_sim - table[n][1]) < 0.015
        assert abs(e2_sim - table[n][2]) < 0.03

    print()
    print("C3. Ce que la relecture en échantillon ajoute au vrai, selon l'échelon, dans le monde où le dommage ne laisse")
    print("aucune trace (rappel vrai = 0,010 pour tout détecteur). Supposé : mêmes d, M, m.")
    print("       n | choisir parmi 20 (tirages) | repondérer, 20 poids (formule) | réapprendre, 4096 poids (formule)")
    for k, n in enumerate((3, 10, 30, 100, 300)):
        g = gen(4, k)
        reps3 = 2000
        S = g.standard_normal((reps3, n, M))
        choix = np.argmax(S.mean(axis=1), axis=1)
        relu = float(np.mean([np.mean(S[i, :, choix[i]] > Z) for i in range(reps3)]))
        e2 = Phi((M / n) / math.sqrt(M / n + M / 400) - Z)
        e3 = approx_relu(0.0, d, n, 400)
        print(f"  {n:6d} |          {f3(relu)}            |            {f3(e2)}              |             {f3(e3)}")
        if n == 30:
            assert 0.015 < relu < 0.06   # PREVU : près de 0,03
    print("  Borne par longueur de description (choix parmi M, n étiquettes, niveau 0,05) : écart au plus")
    for n in (3, 30, 300):
        print(f"    n = {n:3d} : racine(ln(2M/0,05) / (2n)) = {math.sqrt(math.log(2 * M / 0.05) / (2 * n)):5.3f}")

    print()
    print("C4. Régime d'excès : des étiquettes nombreuses mais mêlées. Supposé : parmi les épisodes endommagés audités,")
    print("une part s seulement vient du sabotage (le reste : échecs honnêtes, sans écart) ; négatifs = échecs honnêtes de témoins.")
    print("Rappel sur le sabotage, à 1 % de fausses alertes : Phi( s.Delta^2 / racine(s^2.Delta^2 + d/n + d/m) - z ).")
    print("       n      m     s | rappel sur le sabotage | même nombre d'étiquettes pures (n.s positifs)")
    for (n, m, s) in ((231, 400, 1 / 6), (231, 4000, 1 / 6), (1000, 4000, 1 / 6), (231, 400, 1 / 2), (231, 400, 1.0)):
        mele = Phi(s * delta ** 2 / math.sqrt(s ** 2 * delta ** 2 + d / n + d / m) - Z)
        pur = approx_vrai(delta, d, max(1.0, n * s), m)
        print(f"  {n:6d} {m:6d} {s:5.3f} |         {f3(mele)}         |        {f3(pur)}")
    print("Contrôles du bloc C : passés.")


# ----------------------------------------------------------------------------------------------
# BLOC D — Le prix du pli retenu
# ----------------------------------------------------------------------------------------------
def bloc_D():
    titre("BLOC D — Ce qu'un pli retenu de n_v épisodes endommagés permet d'annoncer (loi binomiale exacte)")
    print("Borne inférieure exacte à 95 % du rappel quand les n_v épisodes du pli sont tous signalés : 0,05^(1/n_v).")
    for nv in (1, 3, 5, 10, 20, 30, 59, 100):
        print(f"  n_v = {nv:3d} : rappel >= {0.05 ** (1.0 / nv):5.3f}")
    print()
    print("Probabilité que la borne inférieure à 95 % dépasse 0,5, selon le rappel vrai r de la version :")
    print("   n_v |  r = 0,60   r = 0,80   r = 0,95")
    tab = {}
    for nv in (5, 10, 20, 30, 50, 100):
        ligne = []
        for r in (0.60, 0.80, 0.95):
            kmin = None
            for k in range(0, nv + 1):
                if borne_basse_exacte(nv, k) > 0.5:
                    kmin = k
                    break
            p = binom_sf(nv, kmin, r) if kmin is not None else 0.0
            ligne.append(p)
        tab[nv] = ligne
        print(f"  {nv:4d} |   {ligne[0]:5.3f}      {ligne[1]:5.3f}      {ligne[2]:5.3f}")
    # PREVU : 59 signalés sur 59 donnent 0,9505 ; 3 sur 3 donnent 0,368 ; à n_v = 5, seule l'unanimité passe 0,5.
    assert abs(0.05 ** (1 / 59) - 0.9505) < 1e-3 and abs(0.05 ** (1 / 3) - 0.368) < 1e-3
    assert abs(borne_basse_exacte(59, 59) - 0.05 ** (1 / 59)) < 1e-6
    assert abs(tab[5][2] - 0.95 ** 5) < 1e-9
    print("Contrôles du bloc D : passés.")


# ----------------------------------------------------------------------------------------------
# BLOC E — Ce que la sonde apprend d'un oracle qui a un angle mort, selon ses négatifs
# ----------------------------------------------------------------------------------------------
def bloc_E():
    titre("BLOC E — Angle mort de l'oracle et identité du suspect : ce que la sonde réapprise apprend (lois exactes, n infini)")
    print("Supposé : un dommage vu par l'oracle déplace les états de Delta le long de u_V ; un dommage que l'oracle ne voit pas,")
    print("de Delta le long de u_H (orthogonale) ; tout épisode du suspect porte un écart d'identité delta_id le long de u_id")
    print("(trace de son ajustement), absent des témoins exogènes. pi = part d'épisodes endommagés chez le suspect ; h = part")
    print("cachée du dommage. Positifs = audités dits endommagés (donc de la sorte vue). Étiquettes sans limite.")
    print("Deux choix de négatifs : (1) témoins exogènes ; (2) épisodes du suspect audités et dits sains.")
    print("Colonnes : signalement, au seuil « 1 % » calé sur des témoins exogènes neufs, des dommages vus, des dommages cachés,")
    print("et des épisodes sains du suspect.")
    print()
    print("  négatifs        pi     h   delta_id | dommages vus  dommages cachés  sains du suspect")
    delta = 4.0
    lignes = {}
    for (pi, h, did) in ((0.12, 0.5, 0.0), (0.12, 0.5, 6.0), (0.50, 0.8, 0.0), (0.50, 0.8, 6.0)):
        # (1) négatifs exogènes : w = Delta.u_V + delta_id.u_id
        nw = math.sqrt(delta ** 2 + did ** 2)
        vus1 = Phi((delta ** 2 + did ** 2) / nw - Z)
        caches1 = Phi((did ** 2) / nw - Z)
        sains1 = Phi((did ** 2) / nw - Z)
        # (2) négatifs = « sains » du suspect, dont une part c porte le dommage caché : w = Delta.u_V - c.Delta.u_H
        c = h * pi / (1.0 - pi * (1.0 - h))
        nw2 = delta * math.sqrt(1.0 + c * c)
        # seuil calé sur témoins exogènes : score d'un témoin = bruit ; d'un épisode du suspect : l'identité est orthogonale à w
        vus2 = Phi(delta ** 2 / nw2 - Z)
        caches2 = Phi(-c * delta ** 2 / nw2 - Z)
        sains2 = Phi(0.0 - Z)
        lignes[(pi, h, did)] = (vus1, caches1, sains1, vus2, caches2, sains2, c)
        print(f"  exogènes       {pi:4.2f}  {h:3.1f}    {did:3.1f}    |    {f3(vus1)}        {f3(caches1)}           {f3(sains1)}")
        print(f"  sains suspect  {pi:4.2f}  {h:3.1f}    {did:3.1f}    |    {f3(vus2)}        {caches2:8.6f}         {f3(sains2)}"
              f"     (part cachée parmi les « sains » : {c:5.3f})")
    # PREVU : pi = 0,12, h = 0,5 : dommages cachés signalés vers 0,005 (moitié de 0,010) ; pi = 0,5, h = 0,8 : vers 4e-5.
    assert abs(lignes[(0.12, 0.5, 0.0)][4] - 0.0049) < 0.0008
    assert lignes[(0.50, 0.8, 0.0)][4] < 1e-4
    # PREVU : identité forte (delta_id = 6), négatifs exogènes : presque tout épisode sain du suspect est signalé (> 0,99).
    assert lignes[(0.12, 0.5, 6.0)][2] > 0.99
    # objet sain : sans identité ni part cachée dans les négatifs, les dommages cachés restent au taux de fausses alertes.
    assert abs(lignes[(0.12, 0.5, 0.0)][1] - ALPHA) < 1e-9
    print("Contrôles du bloc E : passés.")


# ----------------------------------------------------------------------------------------------
# BLOC F — L'oracle qui voit le moniteur : l'écho
# ----------------------------------------------------------------------------------------------
def bloc_F():
    titre("BLOC F — Si l'oracle sait qu'un épisode a été signalé : recapture et précision mesurées (arithmétique exacte)")
    print("Supposé : part endommagée pi = 0,10 ; la sonde signale un endommagé avec r = 0,20 et un sain avec a = 0,01 ;")
    print("à l'aveugle, l'oracle reconnaît un dommage avec q0 et dit endommagé un épisode sain avec f0 ; s'il sait que")
    print("l'épisode a été signalé, ces taux deviennent q1 et f1 pour les épisodes signalés.")
    print("  recapture mesurée = P(signalé | l'oracle dit endommagé), sur un tirage sans égard au score ;")
    print("  précision mesurée = P(l'oracle dit endommagé | signalé), celle de la file d'audit qui suit le soupçon.")
    pi, r, a = 0.10, 0.20, 0.01
    vraie_precision = pi * r / (pi * r + (1 - pi) * a)
    print(f"  Vraies valeurs : rappel r = {f3(r)} ; précision = {f3(vraie_precision)}")
    print()
    print("     q0    f0    q1    f1 | recapture mesurée | précision mesurée | part de sains parmi les « endommagés » de l'oracle")
    out = {}
    for (q0, f0, q1, f1) in ((1.0, 0.0, 1.0, 0.0), (0.8, 0.02, 0.8, 0.02), (0.8, 0.02, 0.95, 0.20), (0.8, 0.02, 0.95, 0.50)):
        num = pi * r * q1 + (1 - pi) * a * f1
        den = num + pi * (1 - r) * q0 + (1 - pi) * (1 - a) * f0
        faux = ((1 - pi) * a * f1 + (1 - pi) * (1 - a) * f0) / den
        precision = num / (pi * r + (1 - pi) * a)
        out[(q0, f0, q1, f1)] = (num / den, precision)
        print(f"  {q0:5.2f} {f0:5.2f} {q1:5.2f} {f1:5.2f} |      {f3(num / den)}       |      {f3(precision)}       |      {f3(faux)}")
    # PREVU : oracle parfait et aveugle : recapture mesurée = r = 0,20 et précision mesurée = précision vraie = 0,690.
    assert abs(out[(1.0, 0.0, 1.0, 0.0)][0] - 0.20) < 1e-12
    assert abs(out[(1.0, 0.0, 1.0, 0.0)][1] - vraie_precision) < 1e-12 and abs(vraie_precision - 0.690) < 1e-3
    # PREVU (calcul à la main) : oracle imparfait et aveugle : précision 0,558 ; oracle informé (0,95 ; 0,50) : 0,810.
    assert abs(out[(0.8, 0.02, 0.8, 0.02)][1] - 0.558) < 1e-3
    assert abs(out[(0.8, 0.02, 0.95, 0.50)][1] - 0.810) < 1e-3
    assert out[(0.8, 0.02, 0.95, 0.50)][0] > out[(0.8, 0.02, 0.8, 0.02)][0]
    print("Contrôles du bloc F : passés.")


def main():
    print("Calculs de la note « boucle audit, recapture, réapprentissage » (v1)")
    print("Toutes les entrées sont des suppositions d'illustration ; aucune donnée du programme.")
    print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; entropie {ENTROPIE} ; quantile z(0,99) = {Z:.6f}")
    res_A = bloc_A()
    bloc_B()
    bloc_C(res_A)
    bloc_D()
    bloc_E()
    bloc_F()
    print()
    print("FIN — tous les contrôles écrits d'avance sont passés.")


if __name__ == "__main__":
    main()
