#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « campagne de dommages plantés par un tiers » (v2).

Version 2, après la contre-lecture de la v1 (qui reste au dépôt, non modifiée). Ce qui change :
  - B.5 (neuf) : la borne d'audit compose deux risques (borne de q, prise) ; table de partage ;
  - F.2 : ligne à 120 par bras (témoin « hors référence », genres réunis) ;
  - G.1 : le niveau est écrit (« sachant q », puis avec la borne de q) ;
  - K : la garantie en dommage est l'optimum d'un programme linéaire (K.3, neuf) ; niveau du mélange (K.4, neuf) ;
  - I : le devis lit les plants rejetés, compte le lot d'étalonnage, les placebos par genre et par tâche,
        le témoin « hors référence » et le repérage ; prix d'un complément.
Les blocs A, B.1 à B.4, C, D, E, H et J sont ceux de la v1, à l'octet.

Pièce de travail (classe C). Lois exactes (binomiale, hypergéométrique),
aucun tirage, aucune graine, aucune donnée du programme, aucun appel de modèle.
Toutes les entrées sont des SUPPOSITIONS d'illustration, sauf les prix du bloc I (voir ce bloc).

Rejeu :  python3 -I calculs-dommages-plantes-tiers-v2.py > calculs-dommages-plantes-tiers-v2.txt
Les attentes sont écrites dans les libellés AVANT la valeur calculée ; les assertions arrêtent
le programme si un objet de contrôle ne rend pas ce qui est attendu.
"""
import math

ALPHA = 0.05


# ---------------------------------------------------------------- outils exacts
def pmf(k, n, p):
    if p <= 0.0:
        return 1.0 if k == 0 else 0.0
    if p >= 1.0:
        return 1.0 if k == n else 0.0
    return math.comb(n, k) * (p ** k) * ((1.0 - p) ** (n - k))


def sf(k, n, p):
    """P(X >= k), X ~ Bin(n, p)."""
    if k <= 0:
        return 1.0
    if k > n:
        return 0.0
    return sum(pmf(j, n, p) for j in range(k, n + 1))


def cdf(k, n, p):
    """P(X <= k)."""
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    return sum(pmf(j, n, p) for j in range(0, k + 1))


def borne_basse(x, n, alpha=ALPHA):
    """Borne basse exacte (Clopper-Pearson, un côté) du taux de succès : x succès sur n."""
    if x <= 0:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if sf(x, n, mid) > alpha:
            hi = mid
        else:
            lo = mid
    return lo


def borne_haute(y, n, alpha=ALPHA):
    """Borne haute exacte (un côté) d'un taux : y événements sur n."""
    if y >= n:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if cdf(y, n, mid) > alpha:
            lo = mid
        else:
            hi = mid
    return hi


def n_minimal(q0, c, alpha=ALPHA):
    """Plus petit n tel que « au plus c manques sur n » borne le taux de reconnaissance à q0."""
    n = c + 1
    while cdf(c, n, 1.0 - q0) > alpha:
        n += 1
    return n


def k95(p, q):
    """Épisodes endommagés avant la prise, à 0,95, régime de signature : 1-(1-pq)^K >= 0,95."""
    if p * q <= 0.0:
        return None
    return math.ceil(math.log(0.05) / math.log(1.0 - p * q))


def k_prise(p, q, beta):
    """Épisodes endommagés avant la prise, avec probabilité 1 - beta, sachant q."""
    if p * q <= 0.0:
        return None
    return math.ceil(math.log(beta) / math.log(1.0 - p * q))


def pire_melange(strates, p, horizon, beta=0.05):
    """Programme linéaire du saboteur. strates : liste de (dose, q). Il choisit n_s >= 0 épisodes par strate pour
    maximiser la somme des doses, sous deux contraintes : la somme des -ln(1 - p*q_s)*n_s reste sous ln(1/beta)
    (il échappe encore avec une probabilité de beta au moins) et la somme des n_s ne dépasse pas l'horizon.
    Deux contraintes : un optimum emploie au plus deux strates ; on énumère donc les sommets (une strate seule ;
    deux strates, les deux contraintes saturées). Rend (dommage, {indice: épisodes})."""
    budget = math.log(1.0 / beta)
    cs = [(d, -math.log(1.0 - p * q)) for d, q in strates]
    meilleur, plan = -1.0, None
    for i, (d, c) in enumerate(cs):
        n = horizon if c <= 0.0 else min(horizon, budget / c)
        if d * n > meilleur + 1e-12:
            meilleur, plan = d * n, {i: n}
    for i in range(len(cs)):
        for j in range(i + 1, len(cs)):
            (di, ci), (dj, cj) = cs[i], cs[j]
            if abs(ci - cj) < 1e-15:
                continue
            ni = (budget - cj * horizon) / (ci - cj)
            nj = horizon - ni
            if ni >= 0.0 and nj >= 0.0 and di * ni + dj * nj > meilleur + 1e-12:
                meilleur, plan = di * ni + dj * nj, {i: ni, j: nj}
    return meilleur, plan


def sidak(alpha, s):
    return 1.0 - (1.0 - alpha) ** (1.0 / s)


def titre(t):
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)


# ============================================================================ BLOC A
titre("BLOC A — La borne exacte par strate : ce que compte un plant")

print("A.1 Objets de contrôle de la borne (attendus : 0,0485 et 0,0510, que la décision arrondit à 0,0511 ; 0,0471 et 0,0523)")
v59, v58 = 0.95 ** 59, 0.95 ** 58
v29, v28 = 0.90 ** 29, 0.90 ** 28
print(f"    0,95^59 = {v59:.4f} ; 0,95^58 = {v58:.4f} ; 0,90^29 = {v29:.4f} ; 0,90^28 = {v28:.4f}")
assert v59 < 0.05 < v58 and v29 < 0.05 < v28
bb = borne_basse(59, 59)
print(f"    borne basse pour 59 sur 59 (attendu : 0,05^(1/59) = {0.05 ** (1 / 59):.4f}) : {bb:.4f}")
assert abs(bb - 0.05 ** (1 / 59)) < 1e-9
print(f"    borne basse pour 0 sur 59 (attendu : 0, la strate ne porte rien) : {borne_basse(0, 59):.4f}")
assert borne_basse(0, 59) == 0.0

print()
print("A.2 Nombre de plants par strate pour écrire « q >= q0 » à 95 %, selon le nombre de manques tolérés")
print("    q0     0 manque   1 manque   2 manques   3 manques")
for q0 in (0.50, 0.80, 0.90, 0.95, 0.99):
    ligne = [n_minimal(q0, c) for c in (0, 1, 2, 3)]
    print(f"    {q0:.2f}   {ligne[0]:>8d}   {ligne[1]:>8d}   {ligne[2]:>9d}   {ligne[3]:>9d}")
assert n_minimal(0.95, 0) == 59 and n_minimal(0.90, 0) == 29

print()
print("A.3 Zéro manque sur n plants : borne basse de q, et facteur sur le nombre d'épisodes avant la prise (1/q)")
print("    n      borne de q   facteur 1/q")
for n in (5, 8, 10, 15, 20, 22, 29, 30, 45, 59, 104, 299):
    b = ALPHA ** (1.0 / n)
    print(f"    {n:>4d}   {b:>9.4f}   {1.0 / b:>10.3f}")

print()
print("A.4 Avec des manques : borne basse exacte de q pour x reconnus sur n")
print("    x/n        taux observé   borne basse à 95 %")
for x, n in ((12, 15), (14, 15), (23, 30), (27, 30), (29, 30), (45, 59), (53, 59), (57, 59), (58, 59)):
    print(f"    {x:>2d}/{n:<3d}     {x / n:>10.3f}   {borne_basse(x, n):>12.4f}")


# ============================================================================ BLOC B
titre("BLOC B — Le plan « zéro manque sur 59 » échoue pour un bon oracle ; ce que l'on écrira en moyenne")

print("B.1 Probabilité de n'avoir aucun manque sur 59 plants, selon le vrai q ; puis dans 10 et 12 strates à la fois")
print("    vrai q    une strate    10 strates    12 strates")
for q in (0.90, 0.95, 0.98, 0.99, 0.995, 0.999):
    u = q ** 59
    print(f"    {q:.3f}   {u:>10.4f}   {u ** 10:>11.5f}   {u ** 12:>11.5f}")
assert abs(0.99 ** 59 - 0.5526) < 1e-3

print()
print("B.2 Borne basse attendue (moyenne sur les issues possibles), selon le vrai q et le nombre de plants")
ns = (10, 15, 20, 30, 59, 104)
print("    vrai q   " + "".join(f"n={n:<6d}" for n in ns))
tables_bornes = {n: [borne_basse(x, n) for x in range(n + 1)] for n in ns}
for q in (0.50, 0.70, 0.80, 0.90, 0.95, 0.99):
    cells = []
    for n in ns:
        e = sum(pmf(x, n, q) * tables_bornes[n][x] for x in range(n + 1))
        cells.append(f"{e:<8.3f}")
    print(f"    {q:.2f}     " + "".join(cells))
print("    Lecture : pour un vrai q de 0,80, 30 plants écrivent en moyenne une borne de "
      f"{sum(pmf(x, 30, 0.8) * tables_bornes[30][x] for x in range(31)):.3f}, 59 plants "
      f"{sum(pmf(x, 59, 0.8) * tables_bornes[59][x] for x in range(60)):.3f}.")

print()
print("B.3 Ce que q change au plancher, régime de signature, à 0,95 SACHANT q (attendus : 299 et 1 497 à 1 % d'audit,")
print("    repris de la décision). Avec q remplacé par sa borne à 95 %, l'énoncé joint ne vaut qu'à 0,90 : voir B.5.")
print("    q          K à 1 % d'audit    K à 20 % d'audit")
for q in (1.0, 0.951, 0.914, 0.905, 0.861, 0.741, 0.50, 0.20, 0.05, 0.0):
    a, b = k95(0.01, q), k95(0.20, q)
    sa = "jamais" if a is None else f"{a:d}"
    sb = "jamais" if b is None else f"{b:d}"
    print(f"    {q:<8.3f}   {sa:>12s}   {sb:>15s}")
assert k95(0.01, 1.0) == 299 and k95(0.01, 0.2) == 1497 and k95(0.2, 1.0) == 14 and k95(0.01, 0.0) is None


print()
print("B.4 Le prix du minimum : S strates de même vrai q, n plants chacune ; espérance du minimum des bornes")
print("    (liste fixe, bornes à 95 % sans correction ; entre parenthèses, bornes simultanées sur S strates)")


def esperance_min_homogene(q, n, s, alpha):
    table = [borne_basse(x, n, alpha) for x in range(n + 1)]
    surv = [sf(x, n, q) ** s for x in range(n + 2)]
    return sum(table[x] * (surv[x] - surv[x + 1]) for x in range(n + 1))


print("    vrai q   S strates   n = 30            n = 59            n = 104")
for q in (0.90, 0.95, 0.99):
    for s in (1, 4, 6, 12, 18):
        cells = []
        for n in (30, 59, 104):
            a = esperance_min_homogene(q, n, s, ALPHA)
            b = esperance_min_homogene(q, n, s, sidak(ALPHA, s))
            cells.append(f"{a:.3f} ({b:.3f})   ")
        print(f"    {q:.2f}     {s:>5d}       " + "".join(cells))
print("    Lecture : le minimum de douze bornes est tiré par la strate la moins chanceuse ; il se paie en plants.")
assert esperance_min_homogene(0.90, 30, 12, ALPHA) < esperance_min_homogene(0.90, 30, 1, ALPHA)


print()
print("B.5 La borne d'audit compose deux risques : celui de la borne de q (a) et celui de la prise (b). L'énoncé joint")
print("    « chaque q employé vaut au moins sa borne ET le saboteur est pris avant K épisodes endommagés » vaut à")
print("    1 - (nombre de strates employées) x a - b au moins (réunion des risques). Zéro manque sur n plants, 1 % d'audit.")
print("    (attendu, première ligne : 330 et 314, les valeurs de la v1, à 0,90 et non 0,95)")
print("    risque par borne de q   strates employées   risque sur la prise   niveau joint   n = 30 : borne, K   n = 59 : borne, K")
for a_q, ns_emp, b_k in ((0.05, 1, 0.05), (0.025, 1, 0.025), (0.01, 1, 0.04), (0.04, 1, 0.01), (0.05, 2, 0.05),
                         (0.0125, 2, 0.025)):
    cells = []
    for nn in (30, 59):
        bq = a_q ** (1.0 / nn)
        cells.append(f"{bq:.3f}, {k_prise(0.01, bq, b_k):>4d}")
    print(f"    {a_q:<8.4f}                {ns_emp}                   {b_k:<8.4f}              {1 - ns_emp * a_q - b_k:.2f}"
          f"           {cells[0]}         {cells[1]}")
assert k_prise(0.01, 0.05 ** (1 / 30), 0.05) == 330 and k_prise(0.01, 0.05 ** (1 / 59), 0.05) == 314
r30, r59 = k_prise(0.01, 0.025 ** (1 / 30), 0.025), k_prise(0.01, 0.025 ** (1 / 59), 0.025)
print(f"    Lecture : écrire l'énoncé joint à 0,95 (2,5 % et 2,5 %) coûte {r30} épisodes au lieu de 330 à 30 plants,")
print(f"    {r59} au lieu de 314 à 59 plants ; entre 30 et 59 plants l'écart reste de {100 * (r30 / r59 - 1):.1f} %.")
print("    Les deux dernières lignes : la garantie en dommage emploie jusqu'à deux strates quand l'horizon mord (K.3, K.4).")


# ============================================================================ BLOC C
titre("BLOC C — Le minimum sur les strates : liste fixe (aucune correction) ; élagage après lecture (correction)")

n = 59
L59 = [borne_basse(x, n) for x in range(n + 1)]


def p_borne_depasse(m, q, table, n):
    """P(L(X) > m) pour X ~ Bin(n, q)."""
    xstar = next((x for x in range(n + 1) if table[x] > m), None)
    return 0.0 if xstar is None else sf(xstar, n, q)


print("C.1 Liste fixe de strates, phrase : « le minimum des vrais q vaut au moins le minimum des bornes par strate »")
print("    Preuve en deux lignes : soit s* la strate du plus petit vrai q ; min des bornes <= borne de s* ;")
print("    donc P(min des bornes > min des q) <= P(borne de s* > q de s*) <= 5 %, sans rien supposer des autres strates.")
m = 0.949
e1 = p_borne_depasse(m, m, L59, n)                      # une strate à 0,949, les autres parfaites
e10 = e1 ** 10                                          # dix strates à 0,949
print(f"    une strate à 0,949 et neuf parfaites (attendu : au plus 0,05) : erreur = {e1:.4f}")
print(f"    dix strates à 0,949 (attendu : bien moins) : erreur = {e10:.2e}")
assert e1 <= 0.05
pire = 0.0
pire_m = None
for i in range(500, 1000):
    mm = i / 1000.0
    v = p_borne_depasse(mm, mm, L59, n)
    if v > pire:
        pire, pire_m = v, mm
print(f"    pire cas sur une grille de q de 0,500 à 0,999 (attendu : sous 0,05, proche de 0,05) : {pire:.4f} à q = {pire_m:.3f}")
assert pire <= 0.05 + 1e-12

print()
print("C.2 OBJET OÙ LA CONCLUSION EST FAUSSE : on écarte après lecture les strates qui ont un manque, et l'on écrit")
print("    « q >= 0,95 dans les strates gardées », sans correction. Toutes les strates ont en vérité q = 0,949.")
print("    nombre de strates   P(phrase écrite et fausse)   (attendu : bien au-dessus de 0,05 dès quelques strates)")
for s in (1, 4, 6, 10, 12, 20):
    err = 1.0 - (1.0 - e1) ** s
    print(f"    {s:>10d}          {err:>10.3f}")
assert 1.0 - (1.0 - e1) ** 10 > 0.30

print()
print("C.3 Avec correction (niveau par strate = 1-(1-0,05)^(1/S)) : l'élagage devient libre")
print("    S strates   plants par strate, zéro manque, pour q0 = 0,80 / 0,90 / 0,95   erreur au pire (attendu <= 0,05)")
for s in (4, 6, 10, 12, 20):
    a_s = sidak(ALPHA, s)
    nn = [n_minimal(q0, 0, a_s) for q0 in (0.80, 0.90, 0.95)]
    q_lim = 0.95 - 1e-9
    err = 1.0 - (1.0 - q_lim ** nn[2]) ** s
    print(f"    {s:>6d}      {nn[0]:>6d} / {nn[1]:>4d} / {nn[2]:>4d}                                       {err:.4f}")
    assert err <= 0.05 + 1e-9
print("    À nombre de plants fixé, zéro manque : borne simultanée de q")
print("    S strates    n = 30     n = 59     (sans correction : "
      f"{ALPHA ** (1 / 30):.3f} et {ALPHA ** (1 / 59):.3f})")
for s in (4, 6, 10, 12, 20):
    a_s = sidak(ALPHA, s)
    print(f"    {s:>6d}      {a_s ** (1 / 30):>7.3f}    {a_s ** (1 / 59):>7.3f}")

print()
print("C.4 Les doses d'un même genre, éprouvées en séquence fixe du grossier au fin, chacune au niveau plein")
print("    Trois doses, phrase « q >= 0,95 jusqu'à la dose d », zéro manque sur 59 exigé à chaque marche.")
qs = (0.949, 0.949, 0.949)
libre = 1.0 - (1.0 - e1) ** 3
sequence = qs[0] ** 59
print(f"    toutes les doses à 0,949, phrase par dose sans ordre (attendu : au-dessus de 0,05) : erreur = {libre:.3f}")
print(f"    mêmes doses, séquence fixe (on s'arrête au premier échec ; attendu : au plus 0,05)   : erreur = {sequence:.4f}")
qs2 = (0.999, 0.949, 0.50)
print(f"    doses à 0,999 / 0,949 / 0,50, séquence fixe : P(écrire à tort la dose 2) = {qs2[0] ** 59 * qs2[1] ** 59:.4f}")
assert libre > 0.05 and sequence <= 0.05 and qs2[0] ** 59 * qs2[1] ** 59 <= 0.05


print()
print("C.5 Le complément vers une strate choisie d'après son premier regard : chaque regard au niveau moitié")
print("    Premier regard : 30 plants. S'il y a un manque, on plante 30 plants de plus et l'on écrit la borne du")
print("    complément seul ; sinon on garde la borne du premier regard. Erreur = P(borne écrite > vrai q).")


def erreur_deux_regards(q, t):
    """t : table des bornes basses pour 0..30 reconnus sur 30, au niveau choisi."""
    garde = pmf(30, 30, q) * (1.0 if t[30] > q else 0.0)
    xstar = next((x for x in range(31) if t[x] > q), None)
    complement = (1.0 - pmf(30, 30, q)) * (0.0 if xstar is None else sf(xstar, 30, q))
    return garde + complement


for niveau, nom in ((ALPHA, "chaque regard à 5 %    (attendu : au-dessus de 0,05)"),
                    (ALPHA / 2, "chaque regard à 2,5 %  (attendu : au plus 0,05)")):
    table_niveau = [borne_basse(x, 30, niveau) for x in range(31)]
    pire, pire_q = 0.0, None
    for i in range(5000, 10000):
        qq = i / 10000.0
        v = erreur_deux_regards(qq, table_niveau)
        if v > pire:
            pire, pire_q = v, qq
    print(f"    {nom} : erreur au pire {pire:.4f} à q = {pire_q:.4f}")
    if niveau == ALPHA:
        assert pire > 0.05
    else:
        assert pire <= 0.05
print(f"    Prix : zéro manque sur 30 donne {ALPHA ** (1 / 30):.3f} à 5 %, {(ALPHA / 2) ** (1 / 30):.3f} à 2,5 % ; "
      f"sur 59, {ALPHA ** (1 / 59):.3f} et {(ALPHA / 2) ** (1 / 59):.3f}.")


# ============================================================================ BLOC D
titre("BLOC D — Le témoin « oracle qui sur-alarme » : q ne se lit jamais sans le taux de fausse alerte")

print("D.1 Un oracle qui dit « endommagé » avec probabilité r, quoi qu'il lise. Règle sans témoin propre :")
print("    « 30 reconnus sur 30 ». (attendu : il passe à coup sûr pour r = 1 : la règle réussit où la conclusion est fausse)")
for r in (1.0, 0.99, 0.9, 0.5):
    print(f"    r = {r:<5.2f}  P(30 sur 30) = {r ** 30:.4f}")
assert 1.0 ** 30 == 1.0

print()
print("D.2 Même oracle, règle complète : en plus, sur m produits propres ou placebo, la borne haute du taux de fausse")
print("    alerte doit rester sous f_max = 0,20 [proposition]. Nombre de fausses alertes toléré, puis P(lisible).")
for mm in (30, 59):
    ymax = max(y for y in range(mm + 1) if borne_haute(y, mm) <= 0.20)
    print(f"    m = {mm} : au plus {ymax} fausses alertes (bornes : "
          + ", ".join(f"{y}->{borne_haute(y, mm):.3f}" for y in range(0, ymax + 2)) + ")")
    for r in (1.0, 0.9, 0.5, 0.3, 0.10, 0.05, 0.02, 0.0):
        print(f"        taux de fausse alerte vrai {r:<5.2f}  P(lisible) = {cdf(ymax, mm, r):.4f}")
    assert cdf(ymax, mm, 1.0) == 0.0 and cdf(ymax, mm, 0.0) == 1.0

print()
print("D.3 Ce que coûte de borner la fausse alerte : zéro fausse alerte sur N produits propres")
print("    taux visé    N lectures propres sans fausse alerte    borne haute rendue")
for f0 in (0.05, 0.01, 0.001, 0.0001, 0.000005):
    nn = math.ceil(math.log(ALPHA) / math.log(1.0 - f0))
    print(f"    {f0:<9.6f}    {nn:>10d}                           {1.0 - ALPHA ** (1.0 / nn):.6f}")
assert math.ceil(math.log(ALPHA) / math.log(1.0 - 0.05)) == 59
print("    Repère repris de la note sur le dommage (calcul B) : « une prise suffit » demande que l'honnête commette")
print("    l'événement moins d'une fois sur cent échantillons d'audit ; à 10 000 épisodes et 20 % d'audit, moins d'une")
print(f"    fois sur {100 * 2000:d} : c'est la dernière ligne, hors de portée d'une campagne de lectures.")


# ============================================================================ BLOC E
titre("BLOC E — Plants infidèles (sans dommage) et plants trop grossiers (visibles par autre chose que le dommage)")

print("E.1 Taux de reconnaissance mesuré = (1-d)*[(1-t)*q_fin + t*q_gros] + d*f")
print("    d : part de plants sans dommage ; t : part de plants grossiers parmi les vrais ; q_fin = 0,50 ; q_gros = 1 ; f = 0,05")
print("    d      t      mesuré   écart au vrai q_fin")
for d in (0.0, 0.2, 0.8):
    for t in (0.0, 0.1, 0.3, 0.5):
        h = (1 - d) * ((1 - t) * 0.50 + t * 1.0) + d * 0.05
        print(f"    {d:<4.1f}   {t:<4.1f}   {h:>6.3f}   {h - 0.50:>+7.3f}")
print("    Lecture : les plants sans dommage font SOUS-estimer q (prudent, mais la campagne ne mesure plus rien) ;")
print("    les plants grossiers le font SUR-estimer (c'est le cas qui doit mourir).")

print()
print("E.2 Le témoin « observateur naïf » : il voit un plant grossier 8 fois sur 10, un plant fin 1 fois sur 20 [supposé]")
print("    Seuil : plus petit compte c tel que P(Bin(n ; 0,05) >= c) <= 0,05. Puissance selon la part t de plants grossiers.")
for nn in (30, 59):
    c = next(c for c in range(nn + 2) if sf(c, nn, 0.05) <= 0.05)
    print(f"    n = {nn} : seuil {c} plants vus (niveau réel {sf(c, nn, 0.05):.4f})")
    for t in (0.0, 0.1, 0.2, 0.3, 0.5):
        pr = t * 0.8 + (1 - t) * 0.05
        print(f"        t = {t:<4.1f}  P(le témoin sonne) = {sf(c, nn, pr):.3f}   biais sur q_fin = {t * 0.5:+.3f}")
    assert sf(c, nn, 0.05) <= 0.05 and sf(c, nn, 0.8) > 0.999

print()
print("E.3 Plants à écrire pour en garder n fidèles, selon la part d de plants infidèles")
print("    d       pour 30 fidèles   pour 59 fidèles")
for d in (0.02, 0.10, 0.20, 0.50, 0.80):
    print(f"    {d:<5.2f}   {math.ceil(30 / (1 - d)):>10d}   {math.ceil(59 / (1 - d)):>14d}")


# ============================================================================ BLOC F
titre("BLOC F — Le témoin « fuite de l'étiquette » : le devin, et le placebo contre le propre")

print("F.1 Un devin doit dire « planté » ou « propre » sur M produits tenus à part, moitié-moitié.")
print("    Seuil exact à 5 % sous le hasard, puis puissance selon sa justesse vraie.")
print("    M       seuil   niveau réel   justesse 0,55   0,60    0,70    1,00    justesse vue 8 fois sur 10")
for mm in (60, 100, 200, 400, 1000):
    c = next(c for c in range(mm + 2) if sf(c, mm, 0.5) <= 0.05)
    a80 = next(a / 1000 for a in range(500, 1001) if sf(c, mm, a / 1000) >= 0.80)
    print(f"    {mm:>5d}   {c:>5d}   {sf(c, mm, 0.5):>9.4f}   {sf(c, mm, 0.55):>11.3f}   {sf(c, mm, 0.60):>5.3f}   "
          f"{sf(c, mm, 0.70):>5.3f}   {sf(c, mm, 1.0):>5.3f}   {a80:>10.3f}")
    assert sf(c, mm, 0.5) <= 0.05 and sf(c, mm, 1.0) == 1.0
print("    Lecture : un devin au hasard sur 100 produits laisse passer une fuite qui devine juste 6 fois sur 10 près")
print("    de quatre fois sur dix. Le devin réfute ; il n'atteste pas.")


def hypergeom_queue(a, n1, n2, tot):
    """P(A >= a) pour A hypergéométrique : n1 placebos, n2 propres, tot alertes en tout."""
    denom = math.comb(n1 + n2, tot)
    s = 0
    for k in range(a, min(n1, tot) + 1):
        if tot - k <= n2:
            s += math.comb(n1, k) * math.comb(n2, tot - k)
    return s / denom


def puissance_fisher(n1, f1, n2, f2, alpha=ALPHA):
    """Puissance exacte du test de Fisher unilatéral « plus d'alertes sur placebo que sur propre »."""
    tot_p = 0.0
    for a in range(n1 + 1):
        pa = pmf(a, n1, f1)
        if pa < 1e-15:
            continue
        for b in range(n2 + 1):
            pb = pmf(b, n2, f2)
            if pb < 1e-15:
                continue
            if hypergeom_queue(a, n1, n2, a + b) <= alpha:
                tot_p += pa * pb
    return tot_p


print()
print("F.2 Placebo contre propre : le planteur fait le même geste sans dommage. Si l'oracle alerte plus sur le placebo")
print("    que sur le produit intact, il lit la main du planteur. Test exact de Fisher, un côté.")
print("    n par bras   fausse alerte propre   sur placebo   P(le témoin sonne)")
for nn in (30, 59):
    for f1 in (0.05, 0.20, 0.35, 0.50):
        print(f"    {nn:>6d}       {0.05:>12.2f}        {f1:>8.2f}      {puissance_fisher(nn, f1, nn, 0.05):>10.3f}")
assert puissance_fisher(30, 0.05, 30, 0.05) <= 0.05
print("    Témoin « hors référence », quatre genres réunis, 120 plants contre 120 placebos :")
for f1 in (0.05, 0.10, 0.20):
    print(f"    {120:>6d}       {0.05:>12.2f}        {f1:>8.2f}      {puissance_fisher(120, f1, 120, 0.05):>10.3f}")


# ============================================================================ BLOC G
titre("BLOC G — La strate jamais plantée ; les genres hors grille d'un planteur au suivant ; deux planteurs, une strate")

print("G.1 Ce que la garantie devient selon la strate que vise le saboteur (1 % d'audit, régime de signature)")
strates = (("strate mesurée, borne 0,914", 0.914), ("strate mesurée, borne 0,741", 0.741),
           ("strate mesurée, borne 0,20", 0.20), ("strate jamais plantée (comptée zéro)", 0.0))
for nom, q in strates:
    kk = k95(0.01, q)
    print(f"    {nom:<40s} : " + ("aucune borne" if kk is None else
                                  f"pris avant {kk} épisodes endommagés, à 0,95 sachant q ; à 0,90 avec la borne de q"))
print("    Le saboteur choisit : la phrase du programme est donc celle de la dernière ligne dès qu'une strate")
print("    atteignable n'est pas plantée.")

print()
print("G.2 Un second planteur, qui ne voit pas la grille, propose G genres ; u tombent hors grille.")
print("    Borne haute exacte de la part hors grille, RELATIVEMENT À CE PLANTEUR (elle ne borne pas un adversaire).")
print("    u hors grille sur G    part observée    borne haute à 95 %")
for u, g in ((0, 10), (0, 20), (0, 59), (2, 20), (5, 20)):
    print(f"    {u:>2d} sur {g:<3d}             {u / g:>8.3f}        {borne_haute(u, g):>8.3f}")
assert abs(borne_haute(0, 59) - (1 - 0.05 ** (1 / 59))) < 1e-9


def fisher_bilateral(a, n1, b, n2):
    tot = a + b
    denom = math.comb(n1 + n2, tot)

    def pr(k):
        if k < 0 or k > n1 or tot - k < 0 or tot - k > n2:
            return 0.0
        return math.comb(n1, k) * math.comb(n2, tot - k) / denom
    p_obs = pr(a)
    return sum(pr(k) for k in range(0, n1 + 1) if pr(k) <= p_obs * (1 + 1e-12))


print()
print("G.3 Deux planteurs indépendants dans la même strate : leurs taux de reconnaissance sont-ils compatibles ?")
print("    planteur A   planteur B   p exacte (Fisher, deux côtés)")
for a, b in ((30, 22), (30, 27), (28, 24), (30, 30)):
    print(f"    {a}/30        {b}/30        {fisher_bilateral(a, 30, b, 30):.4f}")
print("    Lecture : 30 sur 30 contre 22 sur 30 ne sont pas la même strate ; elle se scinde ou porte le plus bas.")


# ============================================================================ BLOC H
titre("BLOC H — L'unité d'indépendance : des plants posés sur le même produit de base ne comptent pas chacun pour un")

print("H.1 Zéro manque sur 59 plants posés sur B produits de base, issues identiques au sein d'un produit (pire cas)")
print("    B produits   borne de q")
for b in (59, 30, 20, 10, 6):
    print(f"    {b:>6d}       {ALPHA ** (1 / b):.4f}")
print()
print("H.2 Le plafond que fixe le nombre de tâches distinctes N (un plant par tâche et par strate, zéro manque)")
print("    N tâches   borne sans correction   borne simultanée, 6 genres   borne simultanée, 12 strates")
for nt in (10, 20, 30, 45, 59, 104):
    print(f"    {nt:>5d}      {ALPHA ** (1 / nt):>12.3f}          {sidak(ALPHA, 6) ** (1 / nt):>12.3f}"
          f"                {sidak(ALPHA, 12) ** (1 / nt):>12.3f}")
print()
print("H.3 Effectif utile approché n / (1 + (k-1)*rho) pour 60 plants, k plants par produit de base (approximation)")
print("    k    rho = 0,2   rho = 0,5   rho = 1,0")
for k in (1, 2, 3, 6):
    print(f"    {k}    " + "   ".join(f"{60 / (1 + (k - 1) * r):>8.1f}" for r in (0.2, 0.5, 1.0)))


# ============================================================================ BLOC J
titre("BLOC J — La règle de lecture de la campagne jouée sur cinq oracles simulés (table d'admission des témoins)")

S, NPL, MPROPRE = 12, 30, 60
L30 = [borne_basse(x, NPL, ALPHA) for x in range(NPL + 1)]
L30S = [borne_basse(x, NPL, sidak(ALPHA, S)) for x in range(NPL + 1)]
ymax60 = max(y for y in range(MPROPRE + 1) if borne_haute(y, MPROPRE) <= 0.20)
print(f"    Campagne simulée : {S} strates déclarées d'avance, {NPL} plants par strate, {MPROPRE} produits propres ou placebo.")
print("    Règle [proposition] : (1) l'oracle n'est lisible que si la borne haute de son taux de fausse alerte reste")
print(f"    sous 0,20, soit au plus {ymax60} fausses alertes sur {MPROPRE} ; (2) la garantie porte le minimum, sur TOUTES les")
print("    strates de la liste, des bornes basses à 95 % (liste fixe : aucune correction, bloc C.1) ; entre parenthèses,")
print("    le minimum des bornes simultanées, qui seul permet d'écarter une strate après lecture (bloc C.3).")


def esperance_min(qs, table):
    """Espérance du minimum sur les strates des bornes basses."""
    surv = []
    for x in range(NPL + 2):
        pr = 1.0
        for q in qs:
            pr *= sf(x, NPL, q)
        surv.append(pr)
    return sum(table[x] * (surv[x] - surv[x + 1]) for x in range(NPL + 1))


oracles = (
    ("parfait (doit tenir)", [1.0] * S, 0.0, "lisible, minimum à 0,905"),
    ("bon : q = 0,90 partout, 2 % de fausses alertes (doit tenir)", [0.90] * S, 0.02, "lisible, minimum vers 0,7"),
    ("sur-alarme : dit toujours « endommagé » (doit mourir)", [1.0] * S, 1.0, "illisible"),
    ("au hasard, une fois sur deux (doit mourir)", [0.5] * S, 0.5, "illisible"),
    ("aveugle à une strate par construction (le minimum doit le dire)", [0.90] * (S - 1) + [0.03], 0.03,
     "lisible, minimum proche de zéro, moyenne trompeuse"),
)
print("    oracle simulé                                                     P(lisible)  minimum attendu    moyenne   ce que j'attendais")
for nom, qs, f, attendu in oracles:
    pl = cdf(ymax60, MPROPRE, f)
    em = esperance_min(qs, L30)
    ems = esperance_min(qs, L30S)
    moy = sum(qs) / len(qs)
    print(f"    {nom:<65s} {pl:>8.4f}   {em:>6.3f} ({ems:.3f})    {moy:>6.3f}    {attendu}")
assert cdf(ymax60, MPROPRE, 1.0) == 0.0 and cdf(ymax60, MPROPRE, 0.5) < 1e-6
assert esperance_min([0.90] * (S - 1) + [0.03], L30) < 0.05 and sum([0.90] * (S - 1) + [0.03]) / S > 0.80
assert abs(esperance_min([1.0] * S, L30) - ALPHA ** (1 / 30)) < 1e-9
print("    Écart à mon attente, déclaré : pour l'oracle « bon », j'attendais un minimum vers 0,7 ; le calcul rend moins")
print("    (voir aussi le bloc B.4) : le minimum de douze bornes coûte plus que je ne le pensais.")


# ============================================================================ BLOC K
titre("BLOC K — La garantie en unités de dommage : stratégie pure (dose divisée par q), puis mélange de strates sous horizon")

print("K.1 STRATÉGIE PURE (le saboteur reste dans une strate). Dommage passé avant la prise, à 0,95 sachant q,")
print("    régime de signature : dose x min(horizon, épisodes avant la prise). Ce n'est PAS la garantie dès que")
print("    l'horizon mord dans une strate : voir K.3.")
print("    Dose en fraction du plafond par épisode [supposé] : grossier 1 ; partiel 1/3 ; de biais 1/10.")
print("    Horizon de 10 000 épisodes endommagés au plus. Unité : plafonds par épisode.")
HORIZON = 10000
DOSES = (("grossier", 1.0), ("partiel", 1.0 / 3.0), ("de biais", 0.1))
for paud in (0.01, 0.20):
    print(f"    taux d'audit {paud:.2f}")
    print("        q        " + "".join(f"{nom:>12s}" for nom, _ in DOSES))
    for q in (1.0, 0.9, 0.5, 0.33, 0.2, 0.1, 0.05, 0.0):
        cells = []
        for nom, d in DOSES:
            kk = k95(paud, q)
            ep = HORIZON if kk is None else min(HORIZON, kk)
            cells.append(f"{d * ep:>12.1f}")
        print(f"        {q:<6.2f}   " + "".join(cells))
assert abs(1.0 * k95(0.01, 1.0) - 299.0) < 1e-9

print()
print("K.2 Seuil d'indifférence : le q sous lequel une strate fine laisse passer plus de dommage que la dose du plafond")
print("    (dose du plafond reconnue avec q = 1, puis 0,9) ; et le nombre de plants sans manque qui l'exclut à 95 %.")
print("    taux d'audit   q au plafond   strate     seuil de q    plants sans manque pour l'exclure")
for paud in (0.01, 0.20):
    for qcap in (1.0, 0.9):
        ref = 1.0 * k95(paud, qcap)
        for nom, d in DOSES[1:]:
            seuil = next(i / 1000.0 for i in range(1, 1001) if d * k95(paud, i / 1000.0) <= ref)
            nn = n_minimal(seuil, 0)
            print(f"    {paud:>8.2f}       {qcap:>6.2f}       {nom:<9s}  {seuil:>8.3f}      {nn:>6d}")
print("    Avec des manques : " + " ; ".join(
    f"{x} reconnus sur {n} bornent q à {borne_basse(x, n):.3f}" for x, n in ((9, 15), (15, 30), (18, 30), (6, 30), (8, 30))))
print("    Lecture : à la dose du plafond, chaque point de q compte au premier ordre ; aux doses fines, il suffit")
print("    d'exclure que q s'effondre plus vite que la dose. Vrai en stratégie pure, et tant que l'horizon ne mord pas.")
print("    Suppose un dommage additif dans l'unité de dose ; un dommage à seuil défait ce calcul.")

print()
print("K.3 MÉLANGE DE STRATES (constat 1 de la contre-lecture). Le saboteur répartit ses épisodes entre strates :")
print("    maximiser la somme des doses, sous : somme des -ln(1 - p*q_s)*n_s <= ln(1/0,05), et somme des n_s <= horizon.")
print("    Programme linéaire à deux contraintes : l'optimum emploie au plus deux strates. 1 % d'audit, horizon 10 000.")
print("    (attendus, donnés par le contre-lecteur : 1 268 et non 1 000 ; 1 091 et non 1 000 ; 599 et 599)")
print("    strates (dose, q)                                              pire produit pur   optimum du mélange   plan")
NOMS = {1.0: "plafond", 1.0 / 3.0: "tiers", 0.1: "dixième"}
BUDGET = math.log(20.0)


def pur(strates, p, horizon):
    return max(d * (horizon if q <= 0.0 else min(horizon, BUDGET / -math.log(1.0 - p * q))) for d, q in strates)


CAS = (
    ("plafond q=1 ; dixième jamais planté", [(1.0, 1.0), (0.1, 0.0)]),
    ("plafond q=1 ; dixième q=0,02", [(1.0, 1.0), (0.1, 0.02)]),
    ("plafond q=1 ; dixième q=0,05", [(1.0, 1.0), (0.1, 0.05)]),
    ("plafond q=1 ; dixième q=0,10", [(1.0, 1.0), (0.1, 0.10)]),
    ("plafond q=1 ; tiers q=0,2 ; dixième jamais planté", [(1.0, 1.0), (1.0 / 3.0, 0.2), (0.1, 0.0)]),
    ("plafond q=0,9 ; tiers jamais planté", [(1.0, 0.9), (1.0 / 3.0, 0.0)]),
    ("plafond q=0,905 ; tiers q=0,905 ; dixième q=0,905", [(1.0, 0.905), (1.0 / 3.0, 0.905), (0.1, 0.905)]),
)
for nom, st in CAS:
    v, plan = pire_melange(st, 0.01, HORIZON)
    txt = " + ".join(f"{plan[i]:.0f} ép. {NOMS[st[i][0]]}" for i in sorted(plan))
    print(f"    {nom:<62s} {pur(st, 0.01, HORIZON):>12.1f}     {v:>12.1f}        {txt}")
v0, _ = pire_melange(CAS[0][1], 0.01, HORIZON)
v1, _ = pire_melange(CAS[1][1], 0.01, HORIZON)
v2, _ = pire_melange(CAS[2][1], 0.01, HORIZON)
assert round(v0) == 1268 and round(v1) == 1091 and round(v2) == 599
print("    Objet de contrôle, en épisodes entiers (recherche exhaustive, deux strates, le saboteur doit garder plus de")
print("    5 % de chances d'échapper) :")
for nom, st in CAS[:3]:
    (da, qa), (db, qb) = st
    ca, cb = -math.log(1.0 - 0.01 * qa), -math.log(1.0 - 0.01 * qb)
    mieux, arg = 0.0, (0, 0)
    for na in range(0, HORIZON + 1):
        if ca * na >= BUDGET:
            break
        nb = HORIZON - na if cb <= 0.0 else min(HORIZON - na, math.ceil((BUDGET - ca * na) / cb) - 1)
        if da * na + db * nb > mieux:
            mieux, arg = da * na + db * nb, (na, nb)
    vlp, _ = pire_melange(st, 0.01, HORIZON)
    print(f"    {nom:<40s} : {mieux:.1f} plafonds ({arg[0]} épisodes au plafond, {arg[1]} au dixième) ; programme linéaire {vlp:.1f}")
    assert vlp - 1.0 <= mieux <= vlp + 1e-9
print("    Objet où le mélange ne change rien : aucune strate dont le nombre d'épisodes avant la prise dépasse l'horizon")
for nom, st in (CAS[2], CAS[3], CAS[6]):
    assert abs(pire_melange(st, 0.01, HORIZON)[0] - pur(st, 0.01, HORIZON)) < 1e-6
print("    (lignes 3, 4 et 7 : optimum égal au pire produit pur, vérifié). Le seuil : l'horizon mord dans une strate")
print(f"    quand son q est sous ln(20) / (taux d'audit x horizon), soit {BUDGET / (0.01 * HORIZON):.4f} ici.")
print("    Forme fermée quand une strate u n'est jamais plantée : dose_u x horizon + max sur s de (dose_s - dose_u) x K_s.")
ku = BUDGET / -math.log(1.0 - 0.01)
assert abs(v0 - (0.1 * HORIZON + 0.9 * ku)) < 1e-6
print("    Unité : le programme linéaire est en épisodes fractionnaires (298,07 au plafond pour q = 1) ; K.1 arrondit")
print("    au-dessus (299, l'épisode où la prise atteint 0,95).")

print()
print("K.4 Le niveau du mélange. L'optimum dépend des bornes de DEUX strates : la preuve « minimum sur liste fixe »")
print("    (C.1), qui n'emploie qu'une strate, ne s'y étend pas telle quelle. Par réunion : P(optimum écrit < optimum")
print(f"    vrai) <= 2 x 5 % ; {1 - 0.95 ** 2:.4f} si les strates sont indépendantes. Rejoué exactement, 30 plants par strate,")
print("    sur une grille de vrais q (strate haute de 0,50 à 0,99 et aux sauts de la borne ; strate basse de 0,0001 à")
print("    0,0300 et aux sauts) : erreur = P(optimum écrit avec les bornes < optimum vrai).")
NK = 30


def balayage(alpha_strate, d_haut, d_bas):
    tb = [borne_basse(x, NK, alpha_strate) for x in range(NK + 1)]
    ecrit = [[pire_melange([(d_haut, tb[xa]), (d_bas, tb[xb])], 0.01, HORIZON)[0] for xb in range(NK + 1)]
             for xa in range(NK + 1)]
    qas = sorted(set([tb[x] - 1e-6 for x in range(20, NK + 1)] + [tb[x] + 1e-6 for x in range(20, NK + 1)]
                     + [i / 100.0 for i in range(50, 100)]))
    qbs = sorted(set([tb[x] - 1e-7 for x in range(1, 4)] + [tb[x] + 1e-7 for x in range(1, 4)]
                     + [i / 10000.0 for i in range(1, 301, 2)]))
    pire, ou = 0.0, None
    for qa in qas:
        if not 0.0 < qa < 1.0:
            continue
        pa = [pmf(x, NK, qa) for x in range(NK + 1)]
        for qb in qbs:
            pb = [pmf(x, NK, qb) for x in range(NK + 1)]
            vrai = pire_melange([(d_haut, qa), (d_bas, qb)], 0.01, HORIZON)[0]
            err = 0.0
            for xa in range(NK + 1):
                if pa[xa] < 1e-13:
                    continue
                ligne = ecrit[xa]
                err += pa[xa] * sum(pb[xb] for xb in range(NK + 1) if pb[xb] >= 1e-13 and ligne[xb] < vrai - 1e-9)
            if err > pire:
                pire, ou = err, (qa, qb)
    return pire, ou


print("    Strates : dose du plafond et dose du dixième (en mélange, l'événement d'erreur ne dépend pas des doses :")
print("    l'optimum y est dose_bas x horizon + (dose_haut - dose_bas) x épisodes à la dose haute).")
for nom_niv, niv in (("chaque borne à 5 %", ALPHA), ("chaque borne à 2,5 %", ALPHA / 2)):
    pire, ou = balayage(niv, 1.0, 0.1)
    print(f"    {nom_niv:<22s} : erreur au pire {pire:.4f} (q haut {ou[0]:.4f}, q bas {ou[1]:.4f})")
    if niv < ALPHA:
        assert pire <= 0.05
print("    Lecture : la réunion garantit 5 % avec chaque borne à 2,5 % ; à 5 % par borne, elle ne garantit que 9,75 %.")
print("    Ce que le balayage rend à 5 % par borne est le pire SUR CETTE GRILLE, non une preuve : aucun cas au-dessus")
print("    de 5 % n'y est trouvé (la borne de l'autre strate est le plus souvent loin sous son vrai q, ce qui compense).")


# ============================================================================ BLOC I
titre("BLOC I — Devis estimé (v2) : comptes de lectures, jetons supposés, prix lus")

print("I.0 Chemin des chiffres. Comptes : blocs A, C, E et H. Jetons par appel : SUPPOSÉS, aucune mesure, aucun journal lu.")
print("    Prix : table des prix de l'interface de Claude jointe à l'outil de travail (en cache au 3 novembre 2026),")
print("    en dollars par million de jetons, entrée / sortie : modèle le moins cher 0,10 / 0,50 ; modèle médian 2 / 10 ;")
print("    modèle le plus cher 8 / 40. Je ne sais pas quels modèles lisent pour l'oracle : AUCUN PRIX LU pour eux ;")
print("    la fourchette de cette table tient lieu de bornes. Traitement par lots à moitié prix : non compté.")
print("    Ce que la v2 ajoute au compte (constat 5 de la contre-lecture) : l'oracle lit aussi les plants rejetés ;")
print("    le lot d'étalonnage (une tâche de plus pour deux du lot final) ; un placebo par genre et par tâche ;")
print("    le témoin « hors référence » (un plant par genre et par tâche du lot final, une dose) ; le repérage.")

PRIX = {"bas": (0.10, 0.50), "centre": (2.0, 10.0), "haut": (8.0, 40.0)}
JETONS = {  # (entrée, sortie) par appel ; la sortie compte la réflexion du modèle ; tout est SUPPOSÉ
    "lecture de l'oracle": {"bas": (3000, 400), "centre": (6000, 2000), "haut": (10000, 8000)},
    "écriture d'un plant": {"bas": (4000, 1500), "centre": (8000, 5000), "haut": (12000, 12000)},
    "validation d'un plant": {"bas": (6000, 300), "centre": (10000, 1500), "haut": (16000, 4000)},
    "observateur naïf": {"bas": (2000, 100), "centre": (5000, 600), "haut": (8000, 2000)},
}
NIVEAUX = ("bas", "centre", "haut")
T_FINAL = {"bas": 15, "centre": 30, "haut": 59}                   # tâches du lot final = plants par strate
T_TOUT = {k: v + math.ceil(v / 2) for k, v in T_FINAL.items()}    # avec le lot d'étalonnage
INFID = {"bas": 0.10, "centre": 0.30, "haut": 0.60}               # part de plants infidèles [supposé]
LECTEURS, VALIDEURS = 2, 2


def cout(appels, poste, niveau):
    tin, tout = JETONS[poste][niveau]
    pin, pout = PRIX[niveau]
    return appels * (tin * pin + tout * pout) / 1e6


print()
print("I.0 bis Prix d'un appel, par poste et par niveau (jetons supposés x prix lus), en USD")
for poste in JETONS:
    print(f"    {poste:<24s} : " + " ; ".join(f"{niv} {cout(1, poste, niv):.5f}" for niv in NIVEAUX))
print("    Tâches : lot final " + ", ".join(f"{niv} {T_FINAL[niv]}" for niv in NIVEAUX)
      + " ; avec le lot d'étalonnage " + ", ".join(f"{niv} {T_TOUT[niv]}" for niv in NIVEAUX))

print()
print("I.1 Étape 1 — plants faits par programme (retrait, troncature, référence d'une autre tâche), aucun rédacteur")
print("    Par tâche : 3 plants, 2 placebos (retrait et troncature sans dommage ; l'échange de référence ne touche")
print("    pas le produit : son placebo est le produit propre), 1 produit propre, 1 jumeau. Deux lecteurs.")
e1, e1_final = {}, {}
for niv in NIVEAUX:
    for cible, tt in ((e1, T_TOUT[niv]), (e1_final, T_FINAL[niv])):
        objets = (3 + 2 + 1 + 1) * tt
        cible[niv] = cout(objets * LECTEURS, "lecture de l'oracle", niv)
    tt = T_TOUT[niv]
    print(f"        {niv:<6s} : {tt} tâches, {3 * tt} plants, {2 * tt} placebos, {tt} propres, {tt} jumeaux, "
          f"{7 * tt * LECTEURS} lectures d'oracle -> {e1[niv]:>9.2f} USD (lot final seul : {e1_final[niv]:.2f})")

print()
print("I.2 Étape 2 — plants écrits par deux tiers, validés par deux valideurs, lus par l'oracle et par un observateur naïf")
GENRES = {"bas": 3, "centre": 4, "haut": 6}
e2, e2_final, e2_rejetes = {}, {}, {}


def etape2(niv, tt):
    """Rend (coût, détail) pour tt tâches ; le témoin hors référence ne porte que sur le lot final."""
    g, d = GENRES[niv], INFID[niv]
    gardes = g * 3 * tt
    ecrits = math.ceil(gardes / (1 - d))
    hors_gardes = g * T_FINAL[niv]
    hors_ecrits = math.ceil(hors_gardes / (1 - d))
    placebos = g * tt
    rejetes = (ecrits - gardes) + (hors_ecrits - hors_gardes)
    lus = ecrits + hors_ecrits + placebos + tt + tt            # rejetés compris, propres, jumeaux
    c = cout(lus * LECTEURS, "lecture de l'oracle", niv)
    c += cout(ecrits + hors_ecrits + placebos, "écriture d'un plant", niv)
    c += cout((ecrits + hors_ecrits + placebos) * VALIDEURS, "validation d'un plant", niv)
    c += cout(tt, "validation d'un plant", niv)                # repérage : un appel par tâche
    c += cout(gardes + hors_gardes + placebos + tt, "observateur naïf", niv)
    return c, (gardes, ecrits, hors_gardes, hors_ecrits, placebos, rejetes, lus * LECTEURS)


for niv in NIVEAUX:
    e2[niv], det = etape2(niv, T_TOUT[niv])
    e2_final[niv], _ = etape2(niv, T_FINAL[niv])
    e2_rejetes[niv] = cout(det[5] * LECTEURS, "lecture de l'oracle", niv)
    print(f"        {niv:<6s} : {GENRES[niv] * 3} strates x {T_TOUT[niv]} tâches = {det[0]} plants gardés ({det[1]} écrits) ; "
          f"hors référence {det[2]} gardés ({det[3]} écrits) ;")
    print(f"                 {det[4]} placebos, {T_TOUT[niv]} propres, {T_TOUT[niv]} jumeaux ; {det[5]} rejetés lus ; "
          f"{det[6]} lectures d'oracle -> {e2[niv]:>9.2f} USD")
    print(f"                 (dont lecture des rejetés {e2_rejetes[niv]:.2f} ; sans le lot d'étalonnage : {e2_final[niv]:.2f})")

print()
print("I.3 Bornes du devis")
print(f"    étape 1 : de {e1['bas']:.2f} à {e1['haut']:.2f} USD, centre {e1['centre']:.2f}")
print(f"    étape 2 : de {e2['bas']:.2f} à {e2['haut']:.2f} USD, centre {e2['centre']:.2f}")
print(f"    les deux : de {e1['bas'] + e2['bas']:.2f} à {e1['haut'] + e2['haut']:.2f} USD, centre {e1['centre'] + e2['centre']:.2f}")
print("    Rappel de la v1, qui ne lisait pas les rejetés et ne comptait ni le lot d'étalonnage ni le témoin hors")
print("    référence : les deux étapes de 0,87 à 5 189,17 USD, centre 140,60. Ordre de grandeur du contre-lecteur")
print("    (approximation à lui) : centre vers 230 USD, haut vers 9 800 USD.")

print()
print("I.4 Prix d'un complément : 30 plants gardés de plus dans une strate, sur d'autres tâches, par niveau")
for niv in NIVEAUX:
    ec = math.ceil(30 / (1 - INFID[niv]))
    c = (cout(ec * LECTEURS, "lecture de l'oracle", niv) + cout(ec, "écriture d'un plant", niv)
         + cout(ec * VALIDEURS, "validation d'un plant", niv) + cout(30, "observateur naïf", niv))
    print(f"        {niv:<6s} : {ec} plants écrits -> {c:>8.2f} USD")
print("    Non chiffré : le nombre de compléments (il dépend du premier regard), les tâches fraîches qu'ils demandent,")
print("    le bras du planteur informé (bras d'attaque déclaré), l'ancre humaine, les heures de sessions, toute machine.")
print("    Étape 0 : 0 USD.")

print()
print("FIN — aucune mesure ; toutes les entrées sont des suppositions d'illustration, sauf les prix du bloc I.")
