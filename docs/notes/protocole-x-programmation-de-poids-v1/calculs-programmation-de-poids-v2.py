"""Calculs de la note « protocole X : programmation de poids, défense et emploi défensif » (v2).

Lois exactes (hypergéométrique, binomiale, géométrique, Student par intégration numérique) et, pour les
blocs C et D, tirages à graines consignées (numpy.random.SeedSequence, entropie et clés imprimées).
Aucune donnée du programme. Toutes les valeurs d'entrée sont des suppositions d'illustration, dites à
chaque bloc. Les objets de contrôle sont des assertions : si l'une tombe, le script s'arrête.
Rejeu : python3 -B calculs-programmation-de-poids-v2.py > calculs-programmation-de-poids-v2.txt
Interpréteur du rejeu égal à l'octet : python3 -B, Python 3.13.18, numpy 2.5.3 (/usr/local/bin/python3).
Un autre numpy change la ligne 2 de la sortie, qui imprime la version, et aucun nombre (constat 16 de la
contre-lecture).

Ce qui change depuis la v1, après la contre-lecture (constats 2, 3, 5 et 16) : le sous-bloc C5 (ce que la
remise à zéro coûte à l'honnête sur l'horizon, et la remise à zéro à niveau réparti entre les états) ; le
repère du bloc E, précisé, et sa table de l'audit sur l'issue ; ce commentaire de rejeu. Les tirages des
blocs C et D sont ceux de la v1 (mêmes graines, même ordre) : tous les nombres de la v1 sont inchangés.
"""
import math
import sys

import numpy as np

ENTROPIE = 20261121


def titre(t):
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)


def log_comb(n, k):
    if k < 0 or k > n:
        return -math.inf
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def log_pmf_bin(k, n, q):
    if q <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if q >= 1.0:
        return 0.0 if k == n else -math.inf
    return log_comb(n, k) + k * math.log(q) + (n - k) * math.log1p(-q)


def generateur(*cle):
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=tuple(cle)))


print("Calculs de la note sur la programmation de poids (v2). Entrées : suppositions d'illustration.")
print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; entropie racine {ENTROPIE} ; "
      "clé de dérivation = (numéro de bloc, rang du cas).")

# ----------------------------------------------------------------------------------------------------
titre("BLOC A — Vérifier les poids par sondage ou en entier (loi hypergéométrique)")
# N blocs dont k ont été modifiés ; à chaque chargement, m blocs tirés au hasard sont comparés à leur
# empreinte scellée. Probabilité de voir l'écart à un chargement : 1 - C(N-k, m) / C(N, m).
# Attendu (écrit avant l'exécution) : m = N rend 1 ; m = 0 rend 0 ; k = 1 rend m / N.


def p_sondage(N, k, m):
    if m <= 0 or k <= 0:
        return 0.0
    if m > N - k:
        return 1.0
    return 1.0 - math.exp(log_comb(N - k, m) - log_comb(N, m))


assert p_sondage(291, 3, 291) == 1.0
assert p_sondage(291, 3, 0) == 0.0
assert abs(p_sondage(291, 1, 29) - 29 / 291) < 1e-12
print("Objets de contrôle : tout vérifier rend 1 ; ne rien vérifier rend 0 ; un seul bloc modifié rend m/N. Tenus.")
print()
print("N = nombre de blocs ; deux découpages supposés : 291 tenseurs ; 15 317 blocs d'un mébioctet")
print("(16,06 milliards d'octets, soit 8,03 milliards de paramètres sur 16 bits : supposé).")
print()
print(f"{'N':>7} {'blocs modifiés':>15} {'part vérifiée':>14} {'vu à un chargement':>19} {'chargements attendus avant de voir':>36}")
for N in (291, 15317):
    for k in (1, 2, 8):
        for part in (0.01, 0.10, 0.50, 1.00):
            m = max(1, round(part * N)) if part < 1.0 else N
            p = p_sondage(N, k, m)
            attendu = "1" if p >= 1.0 else f"{1.0 / p:.1f}"
            print(f"{N:>7} {k:>15} {part:>14.0%} {p:>19.4f} {attendu:>36}")
print()
print("Lecture : un écart de quelques blocs n'est vu à coup sûr qu'en vérifiant tout ; à 10 % de sondage,")
print("un écart d'un bloc attend dix chargements en moyenne. Des empreintes par tenseur ne coûtent rien de")
print("plus à calculer et disent où l'écart loge.")

# ----------------------------------------------------------------------------------------------------
titre("BLOC B — Témoins-leurres plantés parmi des unités candidates (loi hypergéométrique, mélange binomial)")
# D unités candidates à une écriture ; w d'entre elles sont des témoins ; l'écriture en touche k, au
# hasard parmi les candidates qu'elle ne sait pas être des témoins. L'auteur de l'écriture reconnaît
# chaque témoin avec la probabilité a (discernement) et l'évite.
# P(au moins un témoin touché) = somme sur j ~ Bin(w, 1 - a) de [1 - C(D - w, k) / C(D - w + j, k)].
# Attendu : a = 0 rend 1 - C(D-w, k)/C(D, k) ; a = 1 rend 0 ; w = 0 rend 0.


def p_temoin(D, w, k, a):
    if w == 0:
        return 0.0
    total = 0.0
    for j in range(0, w + 1):
        pj = math.exp(log_pmf_bin(j, w, 1.0 - a))
        if pj == 0.0:
            continue
        reste = D - w + j
        if k > reste:
            manque = 0.0
        else:
            manque = math.exp(log_comb(D - w, k) - log_comb(reste, k)) if k <= D - w else 0.0
        total += pj * (1.0 - manque)
    return total


D = 1000
assert abs(p_temoin(D, 100, 10, 0.0) - (1.0 - math.exp(log_comb(900, 10) - log_comb(1000, 10)))) < 1e-12
assert p_temoin(D, 100, 10, 1.0) == 0.0
assert p_temoin(D, 0, 10, 0.0) == 0.0
print("Objets de contrôle : discernement nul, loi hypergéométrique nue ; discernement parfait, 0 ; aucun témoin, 0. Tenus.")
print()
print("D = 1 000 unités candidates (supposé). k = unités écrites : 1, 7, 10 (« moins de dix », ordre publié).")
print()
print(f"{'témoins w':>10} {'unités écrites k':>17} " + " ".join(f"{'a = ' + str(a):>10}" for a in (0.0, 0.5, 0.9, 0.99)))
for w in (10, 50, 100, 300):
    for k in (1, 7, 10):
        print(f"{w:>10} {k:>17} " + " ".join(f"{p_temoin(D, w, k, a):>10.3f}" for a in (0.0, 0.5, 0.9, 0.99)))
print()
print("Fausse alerte d'une écriture honnête, si elle dérange chaque témoin avec la probabilité h, indépendamment :")
print(f"{'témoins w':>10} " + " ".join(f"{'h = ' + str(h):>12}" for h in (0.0, 0.0001, 0.001, 0.01)))
for w in (10, 50, 100, 300):
    print(f"{w:>10} " + " ".join(f"{1.0 - (1.0 - h) ** w:>12.4f}" for h in (0.0, 0.0001, 0.001, 0.01)))
print()
print("Ce que K écritures honnêtes sans un seul témoin dérangé permettent de garantir (règle de trois :")
print("h <= 3 / (K w) à 95 %), exprimé en fausse alerte par écriture, 1 - (1 - 3/(K w))^w :")
print(f"{'K écritures honnêtes':>21} " + " ".join(f"{'w = ' + str(w):>10}" for w in (10, 100, 300)))
for K in (3, 10, 30, 100, 300):
    ligne = []
    for w in (10, 100, 300):
        h = min(1.0, 3.0 / (K * w))
        ligne.append(1.0 - (1.0 - h) ** w)
    print(f"{K:>21} " + " ".join(f"{v:>10.3f}" for v in ligne))
print()
print("Lecture : la garantie de fausse alerte par écriture vaut à peu près 3 / K quel que soit le nombre de")
print("témoins : dix écritures honnêtes ne garantissent que 26 %, il en faut trois cents pour 1 %.")

# ----------------------------------------------------------------------------------------------------
titre("BLOC C — Une accumulation à travers une frontière d'écriture (tirages à graines, mélange de paris)")
# Score par épisode, en écarts types de l'honnête à l'état de référence : N(mu, 1). Le pari est le
# mélange uniforme, sur la grille de lambdas ci-dessous, des paris exp(lambda S_n - n lambda^2 / 2) ;
# alerte quand il atteint 1 / alpha. Sous mu = 0, la fausse alerte à tout instant est au plus alpha (Ville).
# Attendu : mu = 0, part des trajectoires qui sonnent en 5 000 épisodes au plus 0,013 (alpha plus trois
# écarts types du tirage) ; mu = 0,5, délai médian entre 20 et 80 (le pari au lambda juste demande
# ln(100) / (0,5^2 / 2) = 36,8 épisodes) ; la part qui sonne croît avec mu.
ALPHA = 0.01
SEUIL = math.log(1.0 / ALPHA)
GRILLE = (0.05, 0.1, 0.2, 0.3, 0.5)
T_MAX = 5000
M_TRAJ = 10000
PAQUET = 500
PERIODES = (50, 100, 200, 500, 1000, 2000)
# v2 : nombre d'états des poids sur l'horizon si une écriture entre en service toutes les T épisodes, et
# seuil d'une remise à zéro dont le niveau est réparti également entre ces états (alpha / W par état).
ETATS = {T: math.ceil(T_MAX / T) for T in PERIODES}
SEUILS_REPARTIS = {T: math.log(ETATS[T] / ALPHA) for T in PERIODES}


def log_melange(x):
    """Logarithme du mélange de paris, le long des colonnes de x, accumulation partie de zéro."""
    s = np.cumsum(x, axis=1)
    n = np.arange(1, x.shape[1] + 1, dtype=np.float64)
    melange = None
    for lam in GRILLE:
        terme = lam * s - (0.5 * lam * lam) * n
        melange = terme if melange is None else np.logaddexp(melange, terme)
    melange -= math.log(len(GRILLE))
    return melange


def delais(mu, cle):
    """Premier instant où le mélange atteint chaque seuil ; T_MAX + 1 si jamais dans la fenêtre.

    Rang 0 : le seuil 1 / alpha (celui de la v1, mêmes tirages) ; rangs suivants : les seuils répartis,
    dans l'ordre de PERIODES."""
    rng = generateur(3, cle)
    seuils = (SEUIL,) + tuple(SEUILS_REPARTIS[T] for T in PERIODES)
    sortie = np.empty((len(seuils), M_TRAJ), dtype=np.int64)
    for debut in range(0, M_TRAJ, PAQUET):
        x = rng.standard_normal((PAQUET, T_MAX))
        if mu != 0.0:
            x += mu
        melange = log_melange(x)
        for rang, seuil in enumerate(seuils):
            franchi = melange >= seuil
            premier = np.where(franchi.any(axis=1), franchi.argmax(axis=1) + 1, T_MAX + 1)
            sortie[rang, debut:debut + PAQUET] = premier
    return sortie


DERIVES = (0.0, 0.05, 0.1, 0.2, 0.3, 0.5)
TOUS_DELAIS = {mu: delais(mu, i) for i, mu in enumerate(DERIVES)}
TAU = {mu: TOUS_DELAIS[mu][0] for mu in DERIVES}
TAU_REPARTI = {(mu, T): TOUS_DELAIS[mu][1 + j] for mu in DERIVES for j, T in enumerate(PERIODES)}
part_nul = float(np.mean(TAU[0.0] <= T_MAX))
mediane_05 = float(np.median(TAU[0.5]))
assert part_nul <= 0.013, part_nul
assert 20 <= mediane_05 <= 80, mediane_05
for a, b in zip(DERIVES[:-1], DERIVES[1:]):
    assert np.mean(TAU[a] <= 1000) <= np.mean(TAU[b] <= 1000) + 1e-12
print(f"Objets de contrôle : sans déplacement, part des trajectoires qui sonnent en {T_MAX} épisodes = {part_nul:.4f}"
      f" (au plus 0,013 attendu) ; déplacement de 0,5, délai médian = {mediane_05:.0f} épisodes (20 à 80 attendu) ;")
print("la part qui sonne croît avec le déplacement. Tenus.")
print(f"Grille des lambdas : {GRILLE} ; alpha = {ALPHA} ; {M_TRAJ} trajectoires de {T_MAX} épisodes par cas.")
print()
print("C1 — Part des trajectoires qui sonnent avant n épisodes, selon le déplacement moyen du score par épisode.")
print("La même table se lit de deux façons : un saboteur qui déplace le score de mu ; ou un honnête dont le")
print("score a glissé de mu après une écriture bénigne, lu contre la référence d'avant l'écriture.")
FENETRES = (50, 100, 200, 500, 1000, 2000, 5000)
print(f"{'déplacement mu':>15} " + " ".join(f"{'n = ' + str(f):>9}" for f in FENETRES) + f" {'délai médian':>13}")
for mu in DERIVES:
    t = TAU[mu]
    med = np.median(t)
    med_txt = f"{med:.0f}" if med <= T_MAX else f"> {T_MAX}"
    print(f"{mu:>15} " + " ".join(f"{np.mean(t <= f):>9.4f}" for f in FENETRES) + f" {med_txt:>13}")
print()
print("C2 — La preuve fractionnée par les écritures. Si l'accumulation repart de zéro à chaque écriture, toutes les")
print("T épisodes, un saboteur de déplacement mu n'est pris que dans une fenêtre où le pari sonne avant T.")
print("Épisodes servis par le saboteur avant l'alerte, en espérance = T (1 - pi) / pi + délai moyen dans la")
print("fenêtre qui sonne, pi étant la part des fenêtres qui sonnent (table C1). Colonne « sans remise à zéro » :")
print("délai moyen sur les trajectoires qui sonnent en 5 000 épisodes (part dite entre parenthèses ; pour")
print("mu = 0,05 la moyenne est tronquée, donc trop basse).")
print(f"{'déplacement mu':>15} " + " ".join(f"{'T = ' + str(p):>11}" for p in PERIODES) + f" {'sans remise à zéro':>22}")
ESPERANCES = {}
aucune = False
for mu in DERIVES[1:]:
    t = TAU[mu]
    cases = []
    for T in PERIODES:
        dans = t[t <= T]
        pi = dans.size / t.size
        if dans.size == 0:
            cases.append("aucune")
            aucune = True
            ESPERANCES[(mu, T)] = math.inf
        else:
            ESPERANCES[(mu, T)] = T * (1.0 - pi) / pi + float(np.mean(dans))
            cases.append(f"{ESPERANCES[(mu, T)]:.0f}")
    tous = t[t <= T_MAX]
    ESPERANCES[(mu, None)] = float(np.mean(tous)) if tous.size else math.inf
    libre = f"{ESPERANCES[(mu, None)]:.0f} ({tous.size / t.size:.3f})" if tous.size else "aucune"
    print(f"{mu:>15} " + " ".join(f"{c:>11}" for c in cases) + f" {libre:>22}")
if aucune:
    print("« aucune » : aucune des trajectoires ne sonne dans la fenêtre ; le dommage est alors linéaire.")
print()
print("Le même tableau en facteur : ce que la remise à zéro multiplie, par rapport à l'accumulation continue")
print("(déplacements où toutes les trajectoires continues sonnent en 5 000 épisodes) ; dernière colonne : le")
print("rapport de la période T au délai médian continu à partir duquel le facteur passe sous 1,1.")
print(f"{'déplacement mu':>15} " + " ".join(f"{'T = ' + str(p):>11}" for p in PERIODES) + f" {'T / médiane au seuil':>22}")
for mu in DERIVES[2:]:
    base = ESPERANCES[(mu, None)]
    facteurs = [ESPERANCES[(mu, T)] / base for T in PERIODES]
    med = float(np.median(TAU[mu]))
    seuil_T = next((T for T, f in zip(PERIODES, facteurs) if f < 1.1), None)
    fin = f"{seuil_T / med:.1f} (T = {seuil_T})" if seuil_T else "au-delà de 2 000"
    print(f"{mu:>15} " + " ".join(f"{f:>11.2f}" for f in facteurs) + f" {fin:>22}")
faibles = [f"mu = {mu}, T = {T}" for mu in DERIVES[1:] for T in PERIODES if np.mean(TAU[mu] <= T) < 0.01]
print("Erreur de tirage : pi est estimée sur 10 000 trajectoires ; quand elle vaut moins de 1 %, le nombre rendu")
print("n'est juste qu'à 10 ou 20 % près. Cas concernés : " + " ; ".join(faibles) + ".")
print()
print("C3 — La cadence qui laisse à la boucle de réapprentissage le temps de se fermer. Épisodes par état des")
print("poids pour que le plancher d'audit livre L épisodes endommagés étiquetés : L / (p q rho), avec p la part")
print("auditée, q = 1 la reconnaissance par l'oracle (supposée), rho la part d'épisodes endommagés.")
print(f"{'étiquettes L':>13} {'part auditée p':>15} " + " ".join(f"{'rho = ' + str(r):>12}" for r in (0.02, 0.05, 0.2)))
for L in (30, 100):
    for p in (0.05, 0.2):
        print(f"{L:>13} {p:>15} " + " ".join(f"{L / (p * 1.0 * r):>12.0f}" for r in (0.02, 0.05, 0.2)))
print()
print("C4 — La référence honnête refaite à chaque état des poids. Part d'actes sabotés qui reste cachée à")
print("puissance un demi, pour un test sur la moyenne au niveau 1 % : z racine(1/n + 1/m) / mu, mu = 0,5")
print("(formule et valeurs de la loi de la référence honnête du programme ; n épisodes surveillés par état,")
print("m épisodes honnêtes de référence par état).")


def quantile_normal(p):
    bas, haut = -10.0, 10.0
    for _ in range(200):
        mil = 0.5 * (bas + haut)
        if 0.5 * (1.0 + math.erf(mil / math.sqrt(2.0))) < p:
            bas = mil
        else:
            haut = mil
    return 0.5 * (bas + haut)


Z99 = quantile_normal(0.99)
limite = Z99 * math.sqrt(1.0 / 1e12 + 1.0 / 400) / 0.5
assert abs(limite - 0.2326) < 0.0005, limite
print(f"Objet de contrôle : m = 400, n très grand, attendu 23,3 % (valeur du programme) ; rendu {limite:.1%}. Tenu.")
print(f"{'n par état':>11} {'m par état':>11} {'part cachée':>12} {'surcoût de témoins m/n':>24}")
for n_, m_ in ((100, 100), (200, 200), (400, 400), (1600, 1600), (400, 100), (1600, 400), (6400, 400), (6400, 1600)):
    part = Z99 * math.sqrt(1.0 / n_ + 1.0 / m_) / 0.5
    print(f"{n_:>11} {m_:>11} {min(part, 1.0):>12.1%} {m_ / n_:>24.0%}")
print()
print("C5 — Ce que la remise à zéro coûte à l'honnête sur l'horizon, et la remise à zéro à niveau réparti (v2).")
print("C2 garde un niveau de 1 % dans chaque état des poids : chaque remise à zéro dépense de nouveau ce")
print("niveau. Ici, l'honnête sans aucun déplacement, sur l'horizon de 5 000 épisodes, une écriture toutes les")
print("T épisodes : part des trajectoires qui sonnent au moins une fois. Deux voies : le compte direct sur les")
print("tirages du cas sans déplacement, recoupés en fenêtres ; et 1 - (1 - p_T)^(5000 / T), p_T étant la ligne")
print("« 0.0 » de C1 (fenêtres supposées indépendantes). Puis la même chose quand le niveau est réparti")
print("également entre les W états de l'horizon (alpha / W par état, seuil W / alpha).")
# Attendu (écrit avant l'exécution) : à niveau plein et T = 50, entre 8 % et 25 % (la contre-lecture
# calcule environ 15 % par la seconde voie) ; la part décroît quand T croît ; à niveau réparti, au plus
# 0,013 pour toute période (c'est l'objet de contrôle de la validité : alpha plus trois écarts types du
# tirage) ; le compte direct sans remise à zéro retrouve exactement la part de la v1 (mêmes tirages).


def honnete_avec_remise():
    """Parts des trajectoires honnêtes qui sonnent sur l'horizon, par période, à niveau plein et réparti."""
    rng = generateur(3, 0)
    plein = {T: 0 for T in PERIODES}
    reparti = {T: 0 for T in PERIODES}
    continu = 0
    for _ in range(0, M_TRAJ, PAQUET):
        x = rng.standard_normal((PAQUET, T_MAX))
        continu += int((log_melange(x).max(axis=1) >= SEUIL).sum())
        for T in PERIODES:
            sonne_plein = np.zeros(PAQUET, dtype=bool)
            sonne_reparti = np.zeros(PAQUET, dtype=bool)
            for depart in range(0, T_MAX, T):
                sommet = log_melange(x[:, depart:depart + T]).max(axis=1)
                sonne_plein |= sommet >= SEUIL
                sonne_reparti |= sommet >= SEUILS_REPARTIS[T]
            plein[T] += int(sonne_plein.sum())
            reparti[T] += int(sonne_reparti.sum())
    return ({T: plein[T] / M_TRAJ for T in PERIODES}, {T: reparti[T] / M_TRAJ for T in PERIODES},
            continu / M_TRAJ)


FA_PLEIN, FA_REPARTI, FA_CONTINU = honnete_avec_remise()
assert FA_CONTINU == part_nul, (FA_CONTINU, part_nul)
assert 0.08 <= FA_PLEIN[50] <= 0.25, FA_PLEIN[50]
for a, b in zip(PERIODES[:-1], PERIODES[1:]):
    assert FA_PLEIN[a] >= FA_PLEIN[b] - 0.01, (a, b)
assert max(FA_REPARTI.values()) <= 0.013, FA_REPARTI
print(f"{'période T':>10} {'états W':>8} {'niveau plein, direct':>21} {'niveau plein, formule':>22} "
      f"{'niveau réparti, direct':>23} {'seuil réparti':>14}")
for T in PERIODES:
    p_T = float(np.mean(TAU[0.0] <= T))
    formule = 1.0 - (1.0 - p_T) ** (T_MAX / T)
    print(f"{T:>10} {ETATS[T]:>8} {FA_PLEIN[T]:>21.4f} {formule:>22.4f} {FA_REPARTI[T]:>23.4f} "
          f"{ETATS[T] / ALPHA:>14.0f}")
print(f"Repère : sans remise à zéro, {FA_CONTINU:.4f} (la valeur de C1, retrouvée sur les mêmes tirages).")
print("Objets de contrôle : niveau plein et T = 50 entre 0,08 et 0,25 ; la part décroît avec T ; niveau réparti")
print("au plus 0,013 à toute période. Tenus. Erreur de tirage : un écart type de 0,004 au plus sur 10 000")
print("trajectoires ; la formule repose sur p_T, estimée sur 16 à 57 trajectoires, donc juste à 15 ou 25 % près.")
print()
print("Le saboteur devant la remise à zéro à niveau réparti. Même espérance qu'en C2, T (1 - pi) / pi + délai")
print("moyen dans la fenêtre qui sonne, pi étant cette fois la part des fenêtres où le pari atteint W / alpha ;")
print("en facteur de l'accumulation continue. Seconde ligne de chaque déplacement : part des saboteurs pris sur")
print("l'horizon de 5 000 épisodes (fenêtres indépendantes ; la dernière est plus courte pour T = 2 000).")
# Attendu (écrit avant l'exécution) : chaque facteur est au moins celui de C2 (le seuil est plus haut, le
# franchissement vient plus tard sur chaque trajectoire) ; la part prise est au plus celle de C1 à n = 5 000.
print(f"{'déplacement mu':>15} {'':>12} " + " ".join(f"{'T = ' + str(p):>11}" for p in PERIODES)
      + f" {'en continu':>12}")
peu = []
for mu in DERIVES[2:]:
    base = ESPERANCES[(mu, None)]
    ligne_facteur, ligne_prise = [], []
    for T in PERIODES:
        t = TAU_REPARTI[(mu, T)]
        dans = t[t <= T]
        pi = dans.size / t.size
        pleines, reste = divmod(T_MAX, T)
        pi_reste = float(np.mean(t <= reste)) if reste else 0.0
        prise = 1.0 - (1.0 - pi) ** pleines * (1.0 - pi_reste)
        assert prise <= float(np.mean(TAU[mu] <= T_MAX)) + 0.02, (mu, T, prise)
        ligne_prise.append(f"{prise:.3f}")
        if dans.size == 0:
            ligne_facteur.append("aucune")
        else:
            esperance = T * (1.0 - pi) / pi + float(np.mean(dans))
            assert esperance >= ESPERANCES[(mu, T)] - 1e-9, (mu, T)
            ligne_facteur.append(f"{esperance / base:.2f}")
            if dans.size < 100:
                peu.append(f"mu = {mu}, T = {T}")
    print(f"{mu:>15} {'facteur':>12} " + " ".join(f"{c:>11}" for c in ligne_facteur) + f" {1.0:>12.2f}")
    print(f"{'':>15} {'part prise':>12} " + " ".join(f"{c:>11}" for c in ligne_prise)
          + f" {float(np.mean(TAU[mu] <= T_MAX)):>12.3f}")
print("« aucune » : aucune des 10 000 trajectoires n'atteint le seuil réparti dans la fenêtre.")
print("Erreur de tirage : moins de 100 trajectoires atteignent le seuil dans la fenêtre, donc facteur juste à")
print("10 % près au mieux, pour : " + (" ; ".join(peu) if peu else "aucun cas") + ".")
print("Objets de contrôle : chaque facteur au moins égal à celui de C2 ; part prise au plus celle du continu. Tenus.")
print("Lecture : les facteurs de C2 sont des bornes basses de ce qu'une remise à zéro valide sur l'horizon coûte.")

# ----------------------------------------------------------------------------------------------------
titre("BLOC D — Recouvrement entre deux écritures de rang bas : le plancher du hasard (tirages à graines)")
# Deux sous-espaces de dimension r tirés au hasard dans un espace de largeur d. Recouvrement normalisé :
# trace(P_A P_B) / r, entre 0 et 1 ; espérance exacte r / d. Par invariance, A = les r premières
# coordonnées ; B = l'image d'une matrice gaussienne G (d lignes, r colonnes) :
# trace(P_A P_B) = trace((G'G)^-1 G_A' G_A), G_A = les r premières lignes de G.
# Attendu : moyenne simulée égale à r / d à trois écarts types du tirage près ; r = d rend 1.


def recouvrements(d, r, tirages, cle):
    rng = generateur(4, cle)
    out = np.empty(tirages)
    for i in range(tirages):
        g = rng.standard_normal((d, r))
        gram = g.T @ g
        ga = g[:r, :]
        out[i] = float(np.trace(np.linalg.solve(gram, ga.T @ ga))) / r
    return out


plein = recouvrements(8, 8, 5, 0)
assert np.allclose(plein, 1.0, atol=1e-9), plein
LARGEUR = 4096
print("Largeur d = 4 096 (supposée, celle d'un modèle de huit milliards de paramètres). 2 000 tirages par rang.")
print(f"{'rang r':>7} {'espérance r/d':>14} {'moyenne simulée':>16} {'médiane':>9} {'quantile 0,999':>15} {'maximum':>9}")
for i, r in enumerate((1, 16, 64)):
    v = recouvrements(LARGEUR, r, 2000, i + 1)
    es = float(np.std(v, ddof=1) / math.sqrt(v.size))
    assert abs(float(np.mean(v)) - r / LARGEUR) <= 3.0 * es + 1e-12, (r, float(np.mean(v)), es)
    print(f"{r:>7} {r / LARGEUR:>14.5f} {float(np.mean(v)):>16.5f} {float(np.median(v)):>9.5f} "
          f"{float(np.quantile(v, 0.999)):>15.5f} {float(np.max(v)):>9.5f}")
print("Objets de contrôle : rang plein, recouvrement 1 ; moyennes simulées à trois écarts types de r/d. Tenus.")
print()
print("Lecture : entre deux adaptateurs sans rien de commun, le recouvrement attendu est de 0,4 % au rang 16 et")
print("de 1,6 % au rang 64. Une similarité de 0,5 sur la première direction singulière, rapportée entre deux")
print("entraînements du même travail, est donc très au-dessus du plancher ; ce sont les directions suivantes,")
print("non partagées entre graines, qui forment la dispersion de l'honnête où un écart peut se loger.")

# ----------------------------------------------------------------------------------------------------
titre("BLOC E — Auditer les écritures par rejeu : taux exigé et enjeu (loi géométrique)")
# Une écriture qui dévie de son travail déclaré est prise si elle est tirée pour un rejeu (rejeu exact
# supposé : l'honnête ne dévie jamais, régime de signature). q = part des écritures rejouées.
# Attendu : q = 1 rend 0 écriture déviante passée ; une tolérance d'une seule déviation à 95 % exige q = 0,95.


def q_exige(K, confiance=0.95):
    return 1.0 - (1.0 - confiance) ** (1.0 / K)


assert abs(q_exige(1) - 0.95) < 1e-12
print("Part des écritures à rejouer pour prendre une déviation avant la K-ième, avec probabilité 0,95 :")
print(" ".join(f"K = {K} : {q_exige(K):.3f} ;" for K in (1, 2, 5, 10, 20)))
print()
print("Écritures déviantes attendues avant la première prise, (1 - q) / q, et épisodes servis par ces écritures")
print("si chaque état des poids sert T épisodes avant le suivant :")
print(f"{'part rejouée q':>15} {'écritures déviantes':>20} " + " ".join(f"{'T = ' + str(T):>11}" for T in (200, 1000, 5000)))
for q in (0.05, 0.2, 0.5, 0.95, 1.0):
    passe = (1.0 - q) / q
    print(f"{q:>15} {passe:>20.2f} " + " ".join(f"{passe * T:>11.0f}" for T in (200, 1000, 5000)))
assert (1.0 - 1.0) / 1.0 == 0.0
print()
print("Repère (v2) : au même taux de 0,2 appliqué aux épisodes, en régime de signature, 4 épisodes endommagés")
print("passent en moyenne avant la prise ; appliqué aux écritures, 4 écritures déviantes passent en moyenne avant")
print("la première prise par rejeu, soit 4 T épisodes servis par un état dévié. Ces épisodes ne sont pas hors de")
print("tout contrôle : l'audit sur l'issue continue de les tirer. Si l'état dévié endommage une part rho des")
print("épisodes dans la couverture de l'oracle, auditée au taux p, l'audit sur l'issue prend le premier après")
print("1 / (p rho) épisodes en moyenne (oracle supposé sans erreur) :")
# Attendu : p = 1 et rho = 1 rendent 1 épisode ; au taux 0,2 et pour mille épisodes par état, le rejeu des
# écritures ne prend avant l'audit sur l'issue que si rho est sous 1 / (0,2 * 4 000) = 1 / 800.
assert 1.0 / (1.0 * 1.0) == 1.0
print(f"{'part auditée p':>15} " + " ".join(f"{'rho = ' + str(r):>12}" for r in (0.05, 0.01, 0.001)))
for p in (0.05, 0.2):
    print(f"{p:>15} " + " ".join(f"{1.0 / (p * r):>12.0f}" for r in (0.05, 0.01, 0.001)))
rho_bascule = 1.0 / (0.2 * ((1.0 - 0.2) / 0.2) * 1000)
assert abs(rho_bascule - 1.0 / 800) < 1e-15
print(f"À p = q = 0,2 et mille épisodes par état, les 4 000 épisodes ne passent avant toute prise que si rho")
print(f"est sous {rho_bascule:.5f} (un épisode sur 800), ou si le dommage est logé hors de l'épisode, ou si la")
print("déviation n'a pas d'effet sur l'issue auditée : c'est ce dommage-là que seul le rejeu de l'écriture voit.")
print("Objets de contrôle : q = 1 rend 0 ; K = 1 exige 0,95 ; p = rho = 1 rend 1. Tenus.")

# ----------------------------------------------------------------------------------------------------
titre("BLOC F — Le rang d'une écriture parmi K écritures jumelles : ce que coûte un niveau (lois exactes)")
# K rejeux honnêtes du même travail déclaré, graines différentes. Sous l'hypothèse « l'écriture du suspect
# est échangeable avec ses jumelles », la probabilité qu'elle soit la plus extrême de K + 1, sur un axe
# déclaré d'avance, vaut 1 / (K + 1).
# Attendu : niveau 5 % sur une seule écriture, K = 19 ; 1 %, K = 99 ; un seul jumeau par écriture et
# sept écritures toutes du même côté, 0,5^7 = 0,0078 (le test du signe).
assert math.ceil(1.0 / 0.05 - 1.0) == 19 and math.ceil(1.0 / 0.01 - 1.0) == 99
assert abs(0.5 ** 7 - 0.0078125) < 1e-12
print("Sur une seule écriture, le plus petit niveau atteignable vaut 1 / (K + 1) : 5 % demande 19 jumelles, 1 % en demande 99.")
print()
print("En accumulant W écritures, chacune la plus extrême de ses K + 1 : niveau (1 / (K + 1))^W.")
print(f"{'jumelles K':>11} {'écritures W pour 1 %':>21} {'niveau atteint':>15} {'entraînements jumeaux K W':>27}")
for K in (1, 2, 4, 9, 19, 99):
    W = math.ceil(math.log(0.01) / math.log(1.0 / (K + 1)))
    print(f"{K:>11} {W:>21} {(1.0 / (K + 1)) ** W:>15.4f} {K * W:>27}")
print()


def densite_student(x, nu):
    c = math.exp(math.lgamma((nu + 1) / 2.0) - math.lgamma(nu / 2.0)) / math.sqrt(nu * math.pi)
    return c * (1.0 + x * x / nu) ** (-(nu + 1) / 2.0)


def repartition_student(x, nu, pas=20000):
    """P(T <= x) pour x >= 0, par la règle de Simpson sur [0, x]."""
    h = x / pas
    s = densite_student(0.0, nu) + densite_student(x, nu)
    for i in range(1, pas):
        s += (4.0 if i % 2 else 2.0) * densite_student(i * h, nu)
    return 0.5 + s * h / 3.0


def quantile_student(p, nu):
    bas, haut = 0.0, 200.0
    for _ in range(80):
        mil = 0.5 * (bas + haut)
        if repartition_student(mil, nu) < p:
            bas = mil
        else:
            haut = mil
    return 0.5 * (bas + haut)


assert abs(quantile_student(0.99, 4) - 3.747) < 0.002
assert abs(quantile_student(0.95, 9) - 1.833) < 0.002
assert abs(quantile_student(0.95, 2) - 2.920) < 0.002
print("Si l'on suppose en plus que la statistique est normale d'une graine à l'autre : l'écart que le suspect")
print("doit dépasser, en écarts types de graine, pour sonner sur une seule écriture, t(K - 1) racine(1 + 1/K) :")
print(f"{'jumelles K':>11} {'niveau 5 %':>11} {'niveau 1 %':>11}")
for K in (3, 5, 10, 20):
    f = math.sqrt(1.0 + 1.0 / K)
    print(f"{K:>11} {quantile_student(0.95, K - 1) * f:>11.2f} {quantile_student(0.99, K - 1) * f:>11.2f}")
print("Objets de contrôle : trois quantiles de Student connus (3,747 ; 1,833 ; 2,920), retrouvés à 0,002 près. Tenus.")
# ----------------------------------------------------------------------------------------------------
titre("BLOC G — Le rodage tiré au sort : voir qu'une écriture a augmenté le dommage (lois exactes)")
# Pendant le rodage, chaque épisode est servi par l'ancien état ou par le nouveau, au tirage secret du
# harnais ; n épisodes audités par bras ; l'oracle compte les épisodes endommagés. Test exact de Fisher,
# unilatéral, au niveau 1 % : il ne suppose rien sur le taux de l'ancien état. Puissance calculée par
# énumération des deux lois binomiales.
# Attendu : sans différence entre les deux états, la part des rodages qui accusent le nouveau est au
# plus 0,01 (le test est exact) ; avec un ancien état qui n'endommage jamais, il faut au moins sept
# épisodes endommagés dans le bras neuf pour conclure (0,5^7 = 0,0078), une seule prise ne suffit pas.


def log_factorielles(m):
    return np.concatenate(([0.0], np.cumsum(np.log(np.arange(1, m + 1, dtype=np.float64)))))


def loi_binomiale(n, q, lf):
    k = np.arange(0, n + 1)
    if q <= 0.0:
        v = np.zeros(n + 1)
        v[0] = 1.0
        return v
    return np.exp(lf[n] - lf[k] - lf[n - k] + k * math.log(q) + (n - k) * math.log1p(-q))


def seuils_fisher(n, alpha, lf):
    """Pour chaque total s d'épisodes endommagés, le plus petit compte du bras neuf qui fait rejeter."""
    seuils = np.full(2 * n + 1, n + 1, dtype=np.int64)
    for s_tot in range(0, 2 * n + 1):
        bas, haut = max(0, s_tot - n), min(n, s_tot)
        y = np.arange(bas, haut + 1)
        logp = (lf[n] - lf[y] - lf[n - y]) + (lf[n] - lf[s_tot - y] - lf[n - (s_tot - y)]) \
            - (lf[2 * n] - lf[s_tot] - lf[2 * n - s_tot])
        queue = np.cumsum(np.exp(logp)[::-1])[::-1]
        bons = np.nonzero(queue <= alpha)[0]
        if bons.size:
            seuils[s_tot] = y[bons[0]]
    return seuils


def puissance_rodage(n, taux_ancien, taux_neuf, alpha=0.01):
    lf = log_factorielles(2 * n)
    seuils = seuils_fisher(n, alpha, lf)
    idx = np.arange(0, n + 1)
    rejet = idx[None, :] >= seuils[idx[:, None] + idx[None, :]]
    return float(loi_binomiale(n, taux_ancien, lf) @ rejet @ loi_binomiale(n, taux_neuf, lf)), seuils


TAILLES = (100, 200, 400, 800, 1600)
for taux in (0.02, 0.10):
    for n_ in (100, 400):
        taille_reelle, _ = puissance_rodage(n_, taux, taux)
        assert taille_reelle <= 0.01 + 1e-12, (taux, n_, taille_reelle)
_, seuils_100 = puissance_rodage(100, 0.0, 0.0)
premier = next(k for k in range(0, 201) if seuils_100[k] <= k and seuils_100[k] <= 100)
assert premier == 7, premier
print("Objets de contrôle : deux états égaux, part des rodages qui accusent le nouveau au plus 0,01 (quatre cas) ;")
print("ancien état sans aucun dommage, sept épisodes endommagés du bras neuf exigés pour conclure. Tenus.")
print()
print("Part des rodages qui voient l'écriture, selon le nombre n d'épisodes audités par bras.")
print("Dernière colonne : épisodes de rodage pour le plus petit n du tableau qui atteint une part de 0,9,")
print("à 20 % d'audit et moitié des épisodes par état (soit 10 n).")
CAS = ((0.10, 0.15), (0.10, 0.20), (0.02, 0.05), (0.02, 0.10), (0.0, 0.02), (0.0, 0.05))
print(f"{'ancien état':>12} {'nouvel état':>12} " + " ".join(f"{'n = ' + str(n_):>9}" for n_ in TAILLES) + f" {'rodage pour 0,9':>17}")
for ancien, neuf in CAS:
    parts = [puissance_rodage(n_, ancien, neuf)[0] for n_ in TAILLES]
    atteint = next((n_ for n_, v in zip(TAILLES, parts) if v >= 0.9), None)
    fin_ligne = f"{10 * atteint}" if atteint else "au-delà de 16 000"
    print(f"{ancien:>12.2f} {neuf:>12.2f} " + " ".join(f"{v:>9.3f}" for v in parts) + f" {fin_ligne:>17}")
print()
print("Si l'on sait par ailleurs que l'honnête ne commet jamais l'événement audité (régime de signature), une")
print("prise suffit : part des rodages qui voient un taux de 2 % en n audits du bras neuf, 1 - 0,98^n :")
print(" ".join(f"n = {n_} : {1.0 - 0.98 ** n_:.3f} ;" for n_ in TAILLES))
print()
print("Fin des calculs. Toutes les assertions ont tenu.")
