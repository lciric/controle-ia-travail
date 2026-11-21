"""Calculs de la version 2 de la note « mécanisme adjudant hors distribution ».

Blocs N, O et P, à la suite des blocs A à E (note v1) et F à M (erratum 1), qui ne sont ni repris ni modifiés ici.
Lois exactes et programmation dynamique exacte (premier passage d'un pari de Bernoulli en mélange) ; `numpy` pour les
longs horizons ; aucun tirage, aucune donnée du programme. Là où une approximation normale est employée, la ligne le dit.
Toutes les valeurs d'entrée sont des suppositions d'illustration, écrites ici ; aucune n'est une mesure.

[N] La référence honnête de taille m (constat 1 de la contre-lecture) : ce que vaut la garantie à horizon donné
    quand le taux de dommage de l'honnête est estimé et non connu.
[O] La fausse reconnaissance de l'oracle sur l'honnête (constat 2) : ce que devient la règle « un seul épisode reconnu suffit ».
[P] L'audit orienté par le soupçon (constat 3) : ce que lisent la recapture et le pari d'excès sur l'échantillon brut.
"""
import math
from statistics import NormalDist

import numpy as np

N01 = NormalDist()
D0 = 0.10  # taux de dommage de l'honnête, supposition d'illustration (celle des blocs C, H, I, J, K)


def log_binom_pmf(k, n, r):
    if r <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if r >= 1.0:
        return 0.0 if k == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(r) + (n - k) * math.log1p(-r))


def binom_cdf(c, n, r):
    """P(X <= c) pour X binomiale (n, r), par somme des masses (c petit devant n dans tous nos emplois)."""
    if c < 0:
        return 0.0
    return min(1.0, math.fsum(math.exp(log_binom_pmf(k, n, r)) for k in range(0, min(c, n) + 1)))


def binom_sf(c, n, r):
    """P(X >= c)."""
    return max(0.0, 1.0 - binom_cdf(c - 1, n, r))


def grille_vers_zero(nul, taille=16):
    """Les seize mises en progression géométrique du bloc I, rapportées au taux nul."""
    return [(1 / nul) * 2.0 ** (-j) for j in range(1, taille + 1)]


def premier_passage(d, nul, horizon, jalons=(), niveau=0.01):
    """Pari en mélange à poids égaux contre le taux nul `nul` ; chaque audit vaut 1 avec probabilité d.

    Même algorithme que le bloc I de l'erratum 1 : la richesse ne dépend que de (n, k) ; la frontière d'alarme k*(n)
    ne bouge que de 0 ou 1 par pas ; la loi des trajectoires encore en vie est portée par un vecteur.
    Rend : probabilité d'alarme avant l'horizon, médiane du temps d'alarme (ou None), probabilités aux jalons.
    """
    mises = np.asarray(grille_vers_zero(nul), dtype=float)
    a = np.log1p(mises * (1 - nul))
    b = np.log1p(-mises * nul)
    logw = -math.log(len(mises))
    seuil = math.log(1 / niveau)

    def alarme(n, k):
        v = logw + k * a + (n - k) * b
        top = float(v.max())
        return top + math.log(float(np.exp(v - top).sum())) >= seuil

    vivants = np.array([1.0])
    kstar = 1
    cumul = 0.0
    mediane = None
    aux_jalons = {}
    for n in range(1, horizon + 1):
        garde = kstar <= n and alarme(n, kstar)
        suivant = np.empty(kstar if garde else kstar + 1)
        suivant[: len(vivants)] = vivants * (1 - d)
        if garde:
            suivant[1:] += vivants[:-1] * d
            cumul += float(vivants[-1]) * d
        else:
            suivant[len(vivants)] = 0.0
            suivant[1:] += vivants * d
            kstar += 1
        vivants = suivant
        if mediane is None and cumul >= 0.5:
            mediane = n
        if n in jalons:
            aux_jalons[n] = cumul
    return cumul, mediane, aux_jalons


def borne_haute_exacte(k, m, risque):
    """Borne haute exacte (Clopper et Pearson) du taux, k dommages sur m, au risque dit : u tel que P(X <= k | u) = risque."""
    bas, haut = k / m, 1.0
    for _ in range(80):
        milieu = (bas + haut) / 2
        if binom_cdf(k, m, milieu) > risque:
            bas = milieu
        else:
            haut = milieu
    return haut


def bloc_n():
    print("[N] Référence honnête de taille m : le taux de dommage de l'honnête est estimé, non connu (honnête à 0,10).")
    print("    N1. Écart type du taux estimé sur m épisodes honnêtes audités, racine(d0 (1 - d0) / m) :")
    for m in (900, 1000, 3600, 10000):
        print(f"        m = {m:6d} : {100 * math.sqrt(D0 * (1 - D0) / m):5.2f} point")
    print("    N2. Sous l'honnête, pari du bloc I fait contre une référence trop basse de delta (vrai taux 0,10, nul 0,10 - delta) :")
    print("        probabilité d'une fausse alarme avant n audits (programmation dynamique exacte).")
    jalons = (2000, 10000, 40000)
    for delta in (0.0, 0.0025, 0.005, 0.01, 0.02):
        _, med, aux = premier_passage(D0, D0 - delta, 40000, jalons)
        cellules = " ; ".join(f"n = {n:5d} : {aux[n]:6.4f}" for n in jalons)
        fin = "pas de médiane avant 40 000 audits" if med is None else f"médiane {med} audits"
        print(f"        delta = {100 * delta:4.2f} point : {cellules} ; {fin}")
    print("    N3. Fausse alarme sans condition, la référence étant le taux observé sur m épisodes honnêtes (k dommages sur m,")
    print("        k binomial) : encadrement exact par monotonie (un nul plus haut ne sonne jamais plus tôt), sur une grille de k.")
    for m, grille in ((1000, (70, 80, 85, 90, 95, 100, 105, 110, 115, 120, 130)),
                      (10000, (910, 940, 960, 980, 1000, 1020, 1040, 1060, 1090))):
        f = {}
        for k in grille:
            _, _, aux = premier_passage(D0, k / m, 40000, jalons)
            f[k] = aux
        for n in jalons:
            bas = haut = 0.0
            # d_chapeau <= g_0 : f entre f(g_0) et 1 ; entre g_j (exclu) et g_{j+1} (inclus) : f entre f(g_{j+1}) et f(g_j) ;
            # au-delà de g_J : f entre 0 et f(g_J).
            p0 = binom_cdf(grille[0], m, D0)
            bas += p0 * f[grille[0]][n]
            haut += p0 * 1.0
            for g, h in zip(grille[:-1], grille[1:]):
                pj = binom_cdf(h, m, D0) - binom_cdf(g, m, D0)
                bas += pj * f[h][n]
                haut += pj * f[g][n]
            haut += (1.0 - binom_cdf(grille[-1], m, D0)) * f[grille[-1]][n]
            print(f"        m = {m:6d}, n = {n:5d} audits : fausse alarme entre {bas:5.3f} et {haut:5.3f} (niveau visé 0,01)")
    print("    N4. Test à horizon fixe, niveau 1 %, puissance 0,95, approximation normale : plus petit excès décelable,")
    print("        (z(0,99) + z(0,95)) x racine(d0 (1 - d0) (1/n + 1/m)), en points.")
    z = N01.inv_cdf(0.99) + N01.inv_cdf(0.95)
    for n in (2000, 10000, 40000):
        cellules = []
        for m in (1000, 3600, 10000, None):
            inv_m = 0.0 if m is None else 1.0 / m
            nom = "infini" if m is None else f"{m:6d}"
            cellules.append(f"m = {nom} : {100 * z * math.sqrt(D0 * (1 - D0) * (1 / n + inv_m)):4.2f}")
        print(f"        n = {n:5d} audits | " + " | ".join(cellules))
    print("        Plancher quand n tend vers l'infini, (z(0,99) + z(0,95)) x racine(d0 (1 - d0) / m) :")
    for m in (1000, 3600, 10000):
        print(f"        m = {m:6d} : {100 * z * math.sqrt(D0 * (1 - D0) / m):4.2f} point")
    print("    N5. Une procédure à m déclaré, valide sans connaître le taux honnête : le nul est la borne haute exacte du taux")
    print("        honnête au risque 0,005 (k = m x 0,10 dommages observés sur m, issue typique), le pari est tenu au niveau 0,005 ;")
    print("        fausse alarme totale d'au plus 0,01. Coût en verdicts d'oracle : m, plus la médiane des audits avant l'alarme.")
    print("        Repères du bloc K (pari apparié, nul par acte) : 654 verdicts pour un saboteur à 0,20, 2 191 pour un saboteur à 0,15.")
    for m in (200, 500, 1000, 2000, 5000):
        k = round(m * D0)
        u = borne_haute_exacte(k, m, 0.005)
        cellules = []
        for eps in (0.10, 0.05):
            if D0 + eps <= u:
                cellules.append(f"saboteur à {D0 + eps:4.2f} : jamais (le nul est au-dessus)")
                continue
            _, med, _ = premier_passage(D0 + eps, u, 40000, (), niveau=0.005)
            if med is None:
                cellules.append(f"saboteur à {D0 + eps:4.2f} : pas de médiane avant 40 000 audits")
            else:
                cellules.append(f"saboteur à {D0 + eps:4.2f} : médiane {med:5d} audits, total {m + med:5d} verdicts")
        print(f"        m = {m:5d} : nul {u:6.4f} | " + " | ".join(cellules))


def bloc_o():
    print("[O] Fausse reconnaissance f de l'oracle sur un épisode honnête (régime dit « de signature ») :")
    print("    O1. Règle « un seul épisode reconnu suffit », sous l'honnête : fausse alarme avant n audits, 1 - (1 - f)^n.")
    for f in (0.001, 0.005, 0.01):
        cellules = " ; ".join(f"n = {n:5d} : {1 - (1 - f) ** n:5.3f}" for n in (100, 1000, 10000))
        demi = math.ceil(math.log(0.5) / math.log(1 - f))
        print(f"        f = {f:5.3f} : {cellules} ; une fois sur deux dès {demi} audits")
    print("    O2. Ce que borne « aucune fausse reconnaissance sur m témoins honnêtes » : f <= 1 - 0,05^(1/m), au risque 0,05.")
    for m in (100, 300, 1000, 3000, 30000):
        print(f"        m = {m:5d} : f <= {100 * (1 - 0.05 ** (1 / m)):5.3f} %")
    print("    O3. Nombre m de témoins sans fausse reconnaissance qu'il faut pour que « un seul suffit » tienne 1 % de fausse")
    print("        alarme sur n audits (au risque 0,05) : le plus petit m tel que 1 - 0,05^(1/m) <= 1 - 0,99^(1/n).")
    for n in (100, 1000, 10000):
        f_max = 1 - 0.99 ** (1 / n)
        m = math.ceil(math.log(0.05) / math.log(1 - f_max))
        print(f"        n = {n:5d} audits : m >= {m} témoins, soit {m / n:5.1f} fois l'horizon")
    print("    O4. Règle de compte à m déclaré : f borné par O2, horizon de n = m audits ; c = plus petit compte tel que")
    print("        P(au moins c fausses reconnaissances sur n) <= 0,01 ; puis rang k de l'épisode endommagé auquel le saboteur")
    print("        est pris avec probabilité 0,95 (au moins c reconnus parmi ses k épisodes endommagés, audit p, reconnaissance 1).")
    print("        Repères du bloc G (f nul par construction) : k = 299 à 1 % d'audit, k = 14 à 20 %.")
    for m in (300, 1000, 3000):
        n = m
        f_max = 1 - 0.05 ** (1 / m)
        c = 1
        while binom_sf(c, n, f_max) > 0.01:
            c += 1
        cellules = []
        for p in (0.01, 0.20):
            k = c
            while binom_sf(c, k, p) < 0.95:
                k += 1
            cellules.append(f"audit {p:4.2f} : k = {k}")
        print(f"        m = n = {m:5d} : c = {c} | " + " | ".join(cellules))


def bloc_p():
    print("[P] Audit orienté par le soupçon : un épisode signalé par le moniteur est audité avec probabilité a_s,")
    print("    un épisode non signalé avec la probabilité plancher a_0 (a_s >= a_0).")
    print("    P1. Recapture lue sur l'échantillon brut : rappel apparent r a_s / (r a_s + (1 - r) a_0), et effet sur la règle")
    print("        du bloc D (six épisodes endommagés par le sabotage et audités, « invalide » si au plus deux signalés).")
    for a0, a_s in ((0.05, 0.50), (0.20, 0.50), (0.05, 1.00), (0.20, 1.00)):
        for r in (0.2, 0.8):
            apparent = r * a_s / (r * a_s + (1 - r) * a0)
            pondere = (r * a_s / a_s) / (r * a_s / a_s + (1 - r) * a0 / a0)
            part_plancher = a0 / (r * a_s + (1 - r) * a0)
            print(f"        plancher {a0:4.2f}, signalés {a_s:4.2f}, rappel vrai {r:3.1f} : rappel apparent {apparent:5.3f} ; "
                  f"P(« invalide ») = {binom_cdf(2, 6, apparent):5.3f} (échantillon au hasard : {binom_cdf(2, 6, r):5.3f}) ; "
                  f"pondéré par l'inverse : {pondere:5.3f} ; part des audités venue du plancher : {part_plancher:5.3f}")
    print("    P2. Pari d'excès lu sur l'échantillon brut, sous l'honnête (taux vrai 0,10) : le moniteur signale un épisode honnête")
    print("        endommagé avec probabilité g, un épisode honnête sain avec probabilité 0,01 ; plancher 0,05, signalés 0,50.")
    print("        Taux de dommage apparent parmi les audités, et fausse alarme du pari du bloc I tenu contre 0,10.")
    a0, a_s, h = 0.05, 0.50, 0.01
    for g in (0.01, 0.10, 0.30):
        audit_endommage = g * a_s + (1 - g) * a0
        audit_sain = h * a_s + (1 - h) * a0
        apparent = D0 * audit_endommage / (D0 * audit_endommage + (1 - D0) * audit_sain)
        pondere = D0 * (g * a_s / a_s + (1 - g) * a0 / a0)
        _, med, aux = premier_passage(apparent, D0, 10000, (500, 2000, 10000))
        fin = "pas de médiane avant 10 000 audits" if med is None else f"médiane {med} audits"
        print(f"        g = {g:4.2f} : taux apparent {apparent:5.3f} (pondéré par l'inverse : {pondere:5.3f}) ; fausse alarme avant "
              f"500, 2 000 et 10 000 audits : {aux[500]:5.3f}, {aux[2000]:5.3f}, {aux[10000]:5.3f} ; {fin}")


if __name__ == "__main__":
    for bloc in (bloc_n, bloc_o, bloc_p):
        bloc()
        print()
