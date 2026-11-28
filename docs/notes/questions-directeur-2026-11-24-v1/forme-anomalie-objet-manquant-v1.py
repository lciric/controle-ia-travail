#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
forme-anomalie-objet-manquant-v1.py

Vérifications sur processeur pour la réponse à la question 10 du directeur :
« ce qu'on peut prédire du rôle de l'objet manquant à partir de la forme de l'anomalie ».
Pièce de travail (classe C). Aucune dépense, aucun appel à un modèle. Modèles jouets et
énumérations seulement : « mesuré » veut dire ici « calculé sur un jouet ».

Graines : numpy.random.SeedSequence, graine racine 2026112810, une graine dérivée par partie.

CRITÈRES DE MORT, ÉCRITS AVANT LA PREMIÈRE EXÉCUTION (partie D, monde planté « objet ou loi »)
  M1. Monde ami (4 corps d'épreuve, bruit 5 %) : si l'exactitude « objet contre loi » de la
      règle de forme est inférieure ou égale à 0,60, la thèse « la forme prédit le type » est
      morte même là où tout lui est favorable. Attendu pour la dire vivante dans le jouet : au
      moins 0,80. Entre les deux : non concluant.
  M2. Un seul corps d'épreuve (le résidu est un nombre) : l'exactitude doit rester dans
      [0,45 ; 0,55]. Au-dessus, l'épreuve fuit (elle lit autre chose que la forme) et ne vaut rien.
  M3. Jumeau (les deux familles de résidus coïncident par construction), 6 corps, bruit 2 % :
      l'exactitude doit rester dans [0,45 ; 0,55]. Au-dessus, même conclusion qu'en M2.
  Témoins faux connus : M2 et M3 doivent « mourir » (tomber au hasard) avant qu'on lise M1.
Les parties A, B, C et F sont des vérifications d'énoncés démontrés dans le texte : tout
désaccord est une erreur de l'énoncé ou du script, à signaler.

Parties
  A. Graphes à gains : potentiel, holonomie, revêtement dérivé, minimalité (énumération).
  B. Extensions centrales : classes de 2-cocycles et groupes obtenus (énumération).
  C. Problème inverse du potentiel newtonien : deux densités, même champ extérieur.
  D. Monde planté « objet ou loi » sur des précessions d'apsides, et son jumeau.
  E. Rétrodiction descriptive sur trois planètes intérieures (données de source seconde).
  F. Clair de lune monstrueux : coefficients de j, décompositions, rareté sous un nul grossier.
"""
import itertools
import math
import sys

import numpy as np

GRAINE_RACINE = 2026112810
racine = np.random.SeedSequence(GRAINE_RACINE)
g_A, g_B, g_C, g_D, g_E, g_F = [np.random.default_rng(s) for s in racine.spawn(6)]


def titre(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ----------------------------------------------------------------------------
# Groupes finis par table de multiplication
# ----------------------------------------------------------------------------
class Groupe:
    def __init__(self, nom, elements, produit):
        self.nom = nom
        self.n = len(elements)
        idx = {e: i for i, e in enumerate(elements)}
        self.mul = [[idx[produit(a, b)] for b in elements] for a in elements]
        self.e = next(i for i in range(self.n) if all(self.mul[i][j] == j for j in range(self.n)))
        self.inv = [next(j for j in range(self.n) if self.mul[i][j] == self.e) for i in range(self.n)]

    def engendre(self, gens):
        s = {self.e}
        front = [self.e]
        gens = list(set(gens))
        while front:
            x = front.pop()
            for g in gens:
                for y in (self.mul[g][x], self.mul[self.inv[g]][x]):
                    if y not in s:
                        s.add(y)
                        front.append(y)
        return frozenset(s)


def cyclique(m):
    return Groupe(f"Z/{m}", list(range(m)), lambda a, b: (a + b) % m)


def symetrique3():
    perms = list(itertools.permutations(range(3)))
    return Groupe("S3", perms, lambda a, b: tuple(a[b[i]] for i in range(3)))


def klein():
    els = [(0, 0), (1, 0), (0, 1), (1, 1)]
    return Groupe("Z/2 x Z/2", els, lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2))


# ----------------------------------------------------------------------------
# Partie A — graphes à gains
# ----------------------------------------------------------------------------
def graphe_connexe(rng, n, beta):
    """Arbre couvrant aléatoire sur n sommets plus beta arêtes hors arbre (sans boucle)."""
    ordre = list(rng.permutation(n))
    arbre = []
    for i in range(1, n):
        j = int(rng.integers(0, i))
        arbre.append((int(ordre[j]), int(ordre[i])))
    hors = []
    while len(hors) < beta:
        u, v = int(rng.integers(0, n)), int(rng.integers(0, n))
        if u != v:
            hors.append((u, v))  # arêtes multiples permises : ce sont des cycles de longueur 2
    return arbre, hors


def potentiel_par_propagation(G, n, aretes):
    """aretes : liste (u, v, g) ; contrainte h(v) = g.h(u). Renvoie h ou None."""
    adj = [[] for _ in range(n)]
    for (u, v, g) in aretes:
        adj[u].append((v, g))
        adj[v].append((u, G.inv[g]))
    h = [None] * n
    for depart in range(n):
        if h[depart] is not None:
            continue
        h[depart] = G.e
        pile = [depart]
        while pile:
            x = pile.pop()
            for (y, g) in adj[x]:
                val = G.mul[g][h[x]]
                if h[y] is None:
                    h[y] = val
                    pile.append(y)
                elif h[y] != val:
                    return None
    return h


def nombre_potentiels_force_brute(G, n, aretes):
    c = 0
    for h in itertools.product(range(G.n), repeat=n):
        if all(h[v] == G.mul[g][h[u]] for (u, v, g) in aretes):
            c += 1
    return c


def holonomie(G, n, arbre_g, hors_g):
    """Groupe d'holonomie au sommet 0, engendré par les cycles fondamentaux."""
    P = potentiel_par_propagation(G, n, arbre_g)  # gain du chemin d'arbre de 0 à x
    gens = [G.mul[G.inv[P[v]]][G.mul[g][P[u]]] for (u, v, g) in hors_g]
    return G.engendre(gens), P


def fibre_revetement_derive(G, n, aretes):
    """Composante de (0, e) dans le graphe dérivé ; renvoie sa fibre au-dessus de 0 et sa taille."""
    adj = [[] for _ in range(n)]
    for (u, v, g) in aretes:
        adj[u].append((v, g))
        adj[v].append((u, G.inv[g]))
    vus = {(0, G.e)}
    pile = [(0, G.e)]
    while pile:
        x, a = pile.pop()
        for (y, g) in adj[x]:
            s = (y, G.mul[g][a])
            if s not in vus:
                vus.add(s)
                pile.append(s)
    return frozenset(a for (x, a) in vus if x == 0), len(vus)


def revetements_k_feuillets_avec_potentiel(G, n, arbre_g, hors_g, k):
    """Énumère les revêtements à k feuillets (permutations sur les arêtes hors arbre),
    garde les connexes, compte ceux où le gain relevé admet un potentiel."""
    connexes = 0
    avec = 0
    perms = list(itertools.permutations(range(k)))
    for choix in itertools.product(perms, repeat=len(hors_g)):
        ar = []
        for (u, v, g) in arbre_g:
            for i in range(k):
                ar.append((u * k + i, v * k + i, g))
        for (u, v, g), s in zip(hors_g, choix):
            for i in range(k):
                ar.append((u * k + i, v * k + s[i], g))
        # connexité
        N = n * k
        adj = [[] for _ in range(N)]
        for (a, b, _) in ar:
            adj[a].append(b)
            adj[b].append(a)
        vus = {0}
        pile = [0]
        while pile:
            x = pile.pop()
            for y in adj[x]:
                if y not in vus:
                    vus.add(y)
                    pile.append(y)
        if len(vus) != N:
            continue
        connexes += 1
        if potentiel_par_propagation(G, N, ar) is not None:
            avec += 1
    return connexes, avec


def partie_A():
    titre("PARTIE A — Graphes à gains : potentiel, holonomie, revêtement dérivé, minimalité")
    groupes = [cyclique(2), cyclique(3), cyclique(4), symetrique3()]
    bilan = {}
    for G in groupes:
        n_inst = 0
        ok_equiv = ok_torseur = ok_fibre = ok_min = ok_exist = 0
        n_min = n_exist = 0
        tailles_hol = {}
        for _ in range(60):
            n = int(g_A.integers(3, 6))
            beta = int(g_A.integers(1, 3))
            arbre, hors = graphe_connexe(g_A, n, beta)
            # une fois sur trois, un gain « cobord » (anomalies issues d'un attribut caché)
            if g_A.random() < 1 / 3:
                cache = [int(g_A.integers(0, G.n)) for _ in range(n)]
                gain = lambda u, v: G.mul[cache[v]][G.inv[cache[u]]]
                arbre_g = [(u, v, gain(u, v)) for (u, v) in arbre]
                hors_g = [(u, v, gain(u, v)) for (u, v) in hors]
            else:
                arbre_g = [(u, v, int(g_A.integers(0, G.n))) for (u, v) in arbre]
                hors_g = [(u, v, int(g_A.integers(0, G.n))) for (u, v) in hors]
            aretes = arbre_g + hors_g
            n_inst += 1
            H, _ = holonomie(G, n, arbre_g, hors_g)
            tailles_hol[len(H)] = tailles_hol.get(len(H), 0) + 1
            h = potentiel_par_propagation(G, n, aretes)
            nb = nombre_potentiels_force_brute(G, n, aretes)
            # (i) potentiel existe <=> holonomie triviale ; (ii) alors exactement |G| potentiels
            ok_equiv += int((h is not None) == (len(H) == 1) == (nb > 0))
            ok_torseur += int(nb == (G.n if len(H) == 1 else 0))
            # (iii) fibre du revêtement dérivé = groupe d'holonomie ; taille = n.|Hol|
            fibre, taille = fibre_revetement_derive(G, n, aretes)
            ok_fibre += int(fibre == H and taille == n * len(H))
            # (iv) minimalité : aucun revêtement connexe à k < |Hol| feuillets n'admet de potentiel
            if len(H) > 1:
                n_min += 1
                bon = True
                for k in range(1, len(H)):
                    _, avec = revetements_k_feuillets_avec_potentiel(G, n, arbre_g, hors_g, k)
                    bon = bon and (avec == 0)
                ok_min += int(bon)
                # (v) existence à k = |Hol| feuillets (jusqu'à 4, pour le coût)
                if len(H) <= 4:
                    n_exist += 1
                    _, avec = revetements_k_feuillets_avec_potentiel(G, n, arbre_g, hors_g, len(H))
                    ok_exist += int(avec > 0)
        bilan[G.nom] = (n_inst, ok_equiv, ok_torseur, ok_fibre, n_min, ok_min, n_exist, ok_exist)
        print(f"groupe {G.nom:9s} : {n_inst} graphes ; tailles d'holonomie rencontrées {dict(sorted(tailles_hol.items()))}")
        print(f"   (i)  potentiel <=> holonomie triviale              : {ok_equiv}/{n_inst}")
        print(f"   (ii) nombre de potentiels = |G| ou 0 (force brute)  : {ok_torseur}/{n_inst}")
        print(f"   (iii) fibre du revêtement dérivé = holonomie        : {ok_fibre}/{n_inst}")
        print(f"   (iv) aucun revêtement connexe plus petit ne suffit  : {ok_min}/{n_min}")
        print(f"   (v)  un revêtement à |Hol| feuillets suffit (|Hol|<=4): {ok_exist}/{n_exist}")
    return bilan


# ----------------------------------------------------------------------------
# Partie B — extensions centrales
# ----------------------------------------------------------------------------
def signature_groupe(mul, e):
    n = len(mul)
    ordres = []
    for x in range(n):
        y, k = x, 1
        while y != e:
            y = mul[y][x]
            k += 1
        ordres.append(k)
    abel = all(mul[a][b] == mul[b][a] for a in range(n) for b in range(n))
    compte = {}
    for o in ordres:
        compte[o] = compte.get(o, 0) + 1
    return abel, tuple(sorted(compte.items()))


NOMS = {
    (True, ((1, 1), (2, 3))): "Z/2 x Z/2",
    (True, ((1, 1), (2, 1), (4, 2))): "Z/4",
    (True, ((1, 1), (2, 7))): "(Z/2)^3",
    (True, ((1, 1), (2, 3), (4, 4))): "Z/4 x Z/2",
    (True, ((1, 1), (2, 1), (4, 2), (8, 4))): "Z/8",
    (False, ((1, 1), (2, 5), (4, 2))): "D4 (diédral d'ordre 8)",
    (False, ((1, 1), (2, 1), (4, 6))): "Q8 (quaternions)",
    (True, ((1, 1), (3, 8))): "Z/3 x Z/3",
    (True, ((1, 1), (3, 2), (9, 6))): "Z/9",
    (True, ((1, 1), (2, 1), (3, 2), (6, 2))): "Z/6",
    (True, ((1, 1), (2, 3), (3, 2), (6, 6))): "Z/2 x Z/6",
    (True, ((1, 1), (2, 1), (3, 2), (4, 2), (6, 2), (12, 4))): "Z/12",
}


def extensions_centrales(Q, m):
    """Classes de H^2(Q, Z/m), action triviale, cocycles normalisés ; groupe de chaque classe."""
    q = Q.n
    non_e = [x for x in range(q) if x != Q.e]
    paires = [(x, y) for x in non_e for y in non_e]

    def en_table(vals):
        f = [[0] * q for _ in range(q)]
        for (x, y), v in zip(paires, vals):
            f[x][y] = v
        return f

    def est_cocycle(f):
        for x in range(q):
            for y in range(q):
                for z in range(q):
                    if (f[y][z] - f[Q.mul[x][y]][z] + f[x][Q.mul[y][z]] - f[x][y]) % m:
                        return False
        return True

    cocycles = []
    for vals in itertools.product(range(m), repeat=len(paires)):
        f = en_table(vals)
        if est_cocycle(f):
            cocycles.append(tuple(vals))
    cobords = set()
    for hv in itertools.product(range(m), repeat=len(non_e)):
        h = [0] * q
        for x, v in zip(non_e, hv):
            h[x] = v
        cobords.add(tuple((h[x] + h[y] - h[Q.mul[x][y]]) % m for (x, y) in paires))
    restants = set(cocycles)
    classes = []
    while restants:
        c = min(restants)
        cl = {tuple((a + b) % m for a, b in zip(c, d)) for d in cobords}
        classes.append(c)
        restants -= cl
    res = []
    for c in classes:
        f = en_table(c)
        els = [(a, x) for a in range(m) for x in range(q)]
        idx = {el: i for i, el in enumerate(els)}
        mul = [[idx[((a + b + f[x][y]) % m, Q.mul[x][y])] for (b, y) in els] for (a, x) in els]
        sig = signature_groupe(mul, idx[(0, Q.e)])
        # section homomorphe : h avec h(x)+h(y)+f(x,y) = h(xy), cherchée par force brute
        scinde = False
        for hv in itertools.product(range(m), repeat=len(non_e)):
            h = [0] * q
            for x, v in zip(non_e, hv):
                h[x] = v
            if all((h[x] + h[y] + f[x][y] - h[Q.mul[x][y]]) % m == 0 for x in range(q) for y in range(q)):
                scinde = True
                break
        res.append((c, NOMS.get(sig, str(sig)), scinde, c in cobords))
    return len(cocycles), len(cobords), res, en_table, paires


def partie_B():
    titre("PARTIE B — Extensions centrales : classes de 2-cocycles et groupes obtenus")
    cas = [(cyclique(2), 2), (cyclique(3), 2), (cyclique(3), 3), (cyclique(4), 2), (klein(), 2), (klein(), 3)]
    sortie = {}
    for Q, m in cas:
        nz, nb, res, _, _ = extensions_centrales(Q, m)
        compte = {}
        for (_, nom, _, _) in res:
            compte[nom] = compte.get(nom, 0) + 1
        coherent = all(scinde == triv for (_, _, scinde, triv) in res)
        print(f"Q = {Q.nom:9s}, A = Z/{m} : {nz} cocycles normalisés, {nb} cobords, {len(res)} classes -> {compte}")
        print(f"      « classe nulle <=> une section homomorphe existe » : {coherent}")
        sortie[(Q.nom, m)] = (len(res), compte)
    # Matrices de Pauli : section de Z/2 x Z/2 dans SU(2), composition « au signe près »
    I2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    V = klein()
    els = [(0, 0), (1, 0), (0, 1), (1, 1)]
    s = {(0, 0): I2, (1, 0): 1j * sx, (0, 1): 1j * sy, (1, 1): 1j * sz}
    f = [[0] * 4 for _ in range(4)]
    for i, x in enumerate(els):
        for j, y in enumerate(els):
            z = els[V.mul[i][j]]
            prod = s[x] @ s[y]
            if np.allclose(prod, s[z]):
                f[i][j] = 0
            elif np.allclose(prod, -s[z]):
                f[i][j] = 1
            else:
                raise RuntimeError("la section de Pauli ne compose pas au signe près")
    els8 = [(a, x) for a in range(2) for x in range(4)]
    idx = {el: i for i, el in enumerate(els8)}
    mul = [[idx[((a + b + f[x][y]) % 2, V.mul[x][y])] for (b, y) in els8] for (a, x) in els8]
    nom = NOMS.get(signature_groupe(mul, idx[(0, V.e)]))
    signes = sum(f[i][j] for i in range(4) for j in range(4))
    print(f"Section de Pauli de Z/2 x Z/2 dans SU(2) : {signes} produits sur 16 portent le signe -1 ;")
    print(f"      l'extension que ce résidu de signes définit est : {nom}")
    sortie["pauli"] = nom
    return sortie


# ----------------------------------------------------------------------------
# Partie C — problème inverse du potentiel
# ----------------------------------------------------------------------------
def partie_C():
    titre("PARTIE C — Deux densités distinctes, même champ extérieur (problème inverse non unique)")
    N = 72
    xs = np.linspace(-1.0, 1.0, N)
    h = xs[1] - xs[0]
    X, Y, Z = np.meshgrid(xs, xs, xs, indexing="ij")
    R2 = X**2 + Y**2 + Z**2
    bosse = np.where(R2 < 1.0, np.exp(-1.0 / np.clip(1.0 - R2, 1e-12, None)), 0.0)
    psi = bosse * (X + 0.5 * Y * Z)

    def psi_en(p):
        r2 = float(np.dot(p, p))
        return 0.0 if r2 >= 1 else math.exp(-1.0 / (1.0 - r2)) * (p[0] + 0.5 * p[1] * p[2])

    lap = np.zeros_like(psi)
    lap[1:-1, 1:-1, 1:-1] = (
        psi[2:, 1:-1, 1:-1] + psi[:-2, 1:-1, 1:-1] + psi[1:-1, 2:, 1:-1] + psi[1:-1, :-2, 1:-1]
        + psi[1:-1, 1:-1, 2:] + psi[1:-1, 1:-1, :-2] - 6 * psi[1:-1, 1:-1, 1:-1]
    ) / h**2
    print(f"grille {N}^3 ; densité ajoutée rho1 - rho0 = laplacien(psi), psi lisse à support dans la boule unité")
    print(f"masse totale de la densité ajoutée : {lap.sum() * h**3:+.2e} (attendu 0)")
    print(f"norme L1 de la densité ajoutée     : {np.abs(lap).sum() * h**3:.4f}")

    def potentiel(p):
        d = np.sqrt((X - p[0])**2 + (Y - p[1])**2 + (Z - p[2])**2)
        d = np.maximum(d, 0.5 * h)
        return float(-(lap / (4 * np.pi * d)).sum() * h**3), float((np.abs(lap) / (4 * np.pi * d)).sum() * h**3)

    pire = 0.0
    for rayon in (1.25, 1.5, 2.0, 3.0, 6.0):
        for _ in range(4):
            v = g_C.normal(size=3)
            p = rayon * v / np.linalg.norm(v)
            u, echelle = potentiel(p)
            pire = max(pire, abs(u) / echelle)
        print(f"   rayon {rayon:4.2f} : |potentiel ajouté| / échelle, pire cas cumulé = {pire:.2e}")
    print("   à l'intérieur (le potentiel ajouté doit valoir psi, non nul) :")
    ecart_int = 0.0
    for p in (np.array([0.3, 0.0, 0.0]), np.array([-0.2, 0.4, 0.3]), np.array([0.5, -0.3, 0.2])):
        u, echelle = potentiel(p)
        ecart_int = max(ecart_int, abs(u - psi_en(p)) / max(abs(psi_en(p)), 1e-12))
        print(f"      point {p} : potentiel ajouté {u:+.5f}, psi {psi_en(p):+.5f}")
    return pire, ecart_int


# ----------------------------------------------------------------------------
# Partie D — monde planté « objet ou loi »
# ----------------------------------------------------------------------------
# Unités : GM = 1 ; mouvement moyen n(a) = a^(-3/2). Pour une accélération radiale perturbatrice
# df(r) (comptée vers l'extérieur), précession d'une orbite presque circulaire de rayon a :
#     taux = (2 df(a)/a + df'(a)) / (2 n(a))      (différence des fréquences orbitale et épicyclique)
THETA = np.linspace(0.0, 2 * np.pi, 2001)[:-1]


def taux_anneau(a, b):
    """Précession due à un anneau de masse unité et de rayon b, dans le plan (quadrature exacte)."""
    a = np.atleast_1d(a).astype(float)

    def df(r):
        num = r[:, None] - b * np.cos(THETA)[None, :]
        den = (r[:, None] ** 2 + b * b - 2 * r[:, None] * b * np.cos(THETA)[None, :]) ** 1.5
        return -(num / den).mean(axis=1)

    eps = 1e-5 * a
    d1 = (df(a + eps) - df(a - eps)) / (2 * eps)
    # la partie en 1/r^2 (masse vue de loin) ne fait pas précesser : 2f/a + f' = 0, elle s'annule ici
    return (2 * df(a) / a + d1) / (2 * a ** -1.5)


def taux_loi_puissance(a):       # loi en 1/r^(2+delta) : taux = delta.n/2
    return 0.5 * np.asarray(a, float) ** -1.5


def taux_loi_relativiste(a):     # terme en h^2/r^4, h^2 = a : taux = lambda.n/a
    return np.asarray(a, float) ** -2.5


def taux_loi_r4_fixe(a):         # jumeau : terme en 1/r^4 à coefficient fixe : taux ~ a^(-7/2)
    return np.asarray(a, float) ** -3.5


GRILLE_INT = np.linspace(0.02, 0.30, 15)
GRILLE_EXT = np.linspace(2.5, 9.0, 14)


def ajuste(y, base):
    """Moindres carrés à un coefficient ; renvoie la somme des carrés des résidus."""
    c = float(base @ y) / float(base @ base)
    r = y - c * base
    return float(r @ r)


def classe(y, a, sigma, rng, modeles):
    """Règle de forme : score = résidu/sigma^2 + (nombre de paramètres).ln(K) ; ex aequo au sort."""
    K = len(a)
    scores = []
    for nom, typ, p, bases in modeles:
        rss = min(ajuste(y, b(a)) for b in bases)
        scores.append((rss / sigma**2 + p * math.log(K), nom, typ))
    m = min(s for s, _, _ in scores)
    ex = [(nom, typ) for s, nom, typ in scores if s - m < 1e-6]
    return ex[int(rng.integers(0, len(ex)))]


MODELES = [
    ("objet intérieur", "objet", 2, [lambda a, b=b: taux_anneau(a, b) for b in GRILLE_INT]),
    ("objet extérieur", "objet", 2, [lambda a, b=b: taux_anneau(a, b) for b in GRILLE_EXT]),
    ("loi de puissance", "loi", 1, [taux_loi_puissance]),
    ("loi relativiste", "loi", 1, [taux_loi_relativiste]),
]
MODELES_JUMEAU = [
    ("objet intérieur", "objet", 2, [lambda a, b=b: taux_anneau(a, b) for b in np.linspace(0.005, 0.03, 6)]),
    ("loi en 1/r^4 fixe", "loi", 1, [taux_loi_r4_fixe]),
]


def tirage(rng, generateur, K, sigma):
    a = np.sort(np.exp(rng.uniform(np.log(0.38), np.log(1.6), size=K)))
    if generateur == "objet intérieur":
        s = taux_anneau(a, rng.uniform(0.03, 0.28))
    elif generateur == "objet extérieur":
        s = taux_anneau(a, rng.uniform(2.8, 8.5))
    elif generateur == "loi de puissance":
        s = taux_loi_puissance(a)
    elif generateur == "loi relativiste":
        s = taux_loi_relativiste(a)
    elif generateur == "objet jumeau":
        s = taux_anneau(a, rng.uniform(0.006, 0.028))
    elif generateur == "loi jumelle":
        s = taux_loi_r4_fixe(a)
    else:
        raise ValueError(generateur)
    s = s / np.median(np.abs(s)) * np.exp(rng.uniform(-1, 1))   # amplitude libre
    sd = sigma * float(np.median(np.abs(s)))
    return a, s + rng.normal(0, sd, size=K), sd


def partie_D():
    titre("PARTIE D — Monde planté « objet ou loi » (précessions d'apsides) et son jumeau")
    print("Pentes locales d ln(taux)/d ln(a) des familles (rayon 0,4 puis 1,5) :")
    for nom, f in (("anneau intérieur b=0,05", lambda a: taux_anneau(a, 0.05)),
                   ("anneau intérieur b=0,25", lambda a: taux_anneau(a, 0.25)),
                   ("anneau extérieur b=5", lambda a: taux_anneau(a, 5.0)),
                   ("loi de puissance", taux_loi_puissance),
                   ("loi relativiste", taux_loi_relativiste)):
        pentes = []
        for a0 in (0.4, 1.5):
            v = f(np.array([a0 * 0.99, a0 * 1.01]))
            pentes.append(math.log(abs(v[1] / v[0])) / math.log(1.01 / 0.99))
        print(f"   {nom:26s} : {pentes[0]:+.2f} ; {pentes[1]:+.2f}")
    # contrôle de la formule : anneau intérieur lointain ~ (3/4) n b^2/a^2 ; extérieur ~ (3/4) n a^3/b^3
    a0 = np.array([1.0])
    print(f"contrôle : anneau b=0,01 à a=1 : {taux_anneau(a0, 0.01)[0]:.6e} (série : {0.75 * 0.01**2:.6e})")
    print(f"contrôle : anneau b=50  à a=1 : {taux_anneau(a0, 50.0)[0]:.6e} (série : {0.75 / 50.0**3:.6e})")

    gens = ["objet intérieur", "objet extérieur", "loi de puissance", "loi relativiste"]
    type_de = {"objet intérieur": "objet", "objet extérieur": "objet",
               "loi de puissance": "loi", "loi relativiste": "loi"}
    n_par = 150
    resultats = {}
    print(f"\nExactitude « objet contre loi » (et sur les quatre familles), {n_par} tirages par famille :")
    print("   corps  bruit   objet/loi   IC95%            quatre familles")
    for K in (1, 2, 3, 4, 6):
        for sigma in (0.02, 0.05, 0.20):
            bon2 = bon4 = tot = 0
            for g in gens:
                for _ in range(n_par):
                    a, y, sd = tirage(g_D, g, K, sigma)
                    nom, typ = classe(y, a, sd, g_D, MODELES)
                    bon2 += int(typ == type_de[g])
                    bon4 += int(nom == g)
                    tot += 1
            p = bon2 / tot
            demi = 1.96 * math.sqrt(p * (1 - p) / tot)
            resultats[(K, sigma)] = (p, demi, bon4 / tot)
            print(f"   {K:5d}  {sigma:4.2f}    {p:5.3f}      [{p - demi:5.3f} ; {p + demi:5.3f}]   {bon4 / tot:5.3f}")
    print("\nJumeau (objet = quadrupôle intérieur quasi ponctuel ; loi = terme en 1/r^4 à coefficient fixe) :")
    jumeau = {}
    for K, sigma in ((6, 0.02), (6, 0.05), (4, 0.05)):
        bon = tot = 0
        rep = {"objet": 0, "loi": 0}
        for g, t in (("objet jumeau", "objet"), ("loi jumelle", "loi")):
            for _ in range(2 * n_par):
                a, y, sd = tirage(g_D, g, K, sigma)
                _, typ = classe(y, a, sd, g_D, MODELES_JUMEAU)
                rep[typ] += 1
                bon += int(typ == t)
                tot += 1
        p = bon / tot
        demi = 1.96 * math.sqrt(p * (1 - p) / tot)
        jumeau[(K, sigma)] = (p, demi)
        print(f"   {K} corps, bruit {sigma:4.2f} : exactitude {p:5.3f} [{p - demi:5.3f} ; {p + demi:5.3f}] ; réponses {rep}")

    print("\nLecture des critères de mort (écrits en tête du script avant la première exécution) :")
    p1, d1, _ = resultats[(1, 0.05)]
    pj, dj = jumeau[(6, 0.02)]
    pm, dm, _ = resultats[(4, 0.05)]
    m2 = all(0.45 <= resultats[(1, s)][0] <= 0.55 for s in (0.02, 0.05, 0.20))
    m3 = 0.45 <= pj <= 0.55
    print(f"   M2 (un seul corps : hasard exigé)        : {'tenu' if m2 else 'VIOLÉ'} "
          f"({', '.join(f'{resultats[(1, s)][0]:.3f}' for s in (0.02, 0.05, 0.20))})")
    print(f"   M3 (jumeau, 6 corps, 2 % : hasard exigé) : {'tenu' if m3 else 'VIOLÉ'} ({pj:.3f})")
    if not (m2 and m3):
        print("   -> un témoin faux connu n'est pas mort : l'épreuve ne vaut rien, M1 n'est pas lu.")
    else:
        etat = "vivante dans le jouet" if pm >= 0.80 else ("MORTE" if pm <= 0.60 else "non concluant")
        print(f"   M1 (4 corps, 5 %) : exactitude {pm:.3f} -> thèse {etat}")
    return resultats, jumeau


# ----------------------------------------------------------------------------
# Partie E — trois planètes intérieures (descriptif)
# ----------------------------------------------------------------------------
def partie_E():
    titre("PARTIE E — Rétrodiction descriptive : la forme sur trois planètes (données de source seconde)")
    GM = 1.32712440018e20       # m^3/s^2 (constante gravitationnelle héliocentrique, valeur usuelle)
    c = 299792458.0
    UA = 1.495978707e11
    rad_as = 180 / math.pi * 3600
    planetes = [  # nom, demi-grand axe (UA), excentricité, période (ans) : valeurs usuelles
        ("Mercure", 0.38710, 0.20563, 0.240846),
        ("Vénus", 0.72333, 0.00677, 0.615198),
        ("Terre", 1.00000, 0.01671, 1.000017),
    ]
    # « mesuré » : Berche et Medina 2024, arXiv 2402.04643, tableau 3, p. 15 (source seconde)
    mesure = {"Mercure": (43.11, 0.45), "Vénus": (8.4, 4.8), "Terre": (5.0, 1.2)}
    rg, hall, quad = {}, {}, {}
    for nom, a, e, P in planetes:
        rg[nom] = 6 * math.pi * GM / (c**2 * a * UA * (1 - e**2)) * (100 / P) * rad_as
        hall[nom] = 1.0 / P                                   # même angle par révolution
        quad[nom] = (1.0 / P) / (a**2 * (1 - e**2) ** 2)      # quadrupôle intérieur (Soleil aplati, anneau proche)
    y = np.array([mesure[n][0] for n, *_ in planetes])
    s = np.array([mesure[n][1] for n, *_ in planetes])

    def chi2_un_parametre(base):
        b = np.array([base[n] for n, *_ in planetes])
        coef = float(((b * y) / s**2).sum() / ((b * b) / s**2).sum())
        return coef, float((((y - coef * b) / s) ** 2).sum()), coef * b

    chi_rg = float((((y - np.array([rg[n] for n, *_ in planetes])) / s) ** 2).sum())
    k_h, chi_h, pred_h = chi2_un_parametre(hall)
    k_q, chi_q, pred_q = chi2_un_parametre(quad)
    print("secondes d'arc par siècle      Mercure   Vénus   Terre    chi2   paramètres libres")
    print(f"mesuré (source seconde)        {y[0]:7.2f} {y[1]:7.2f} {y[2]:7.2f}")
    print(f"loi relativiste (calculée)     {rg['Mercure']:7.2f} {rg['Vénus']:7.2f} {rg['Terre']:7.2f}  {chi_rg:6.2f}   0")
    print(f"loi de puissance (Hall)        {pred_h[0]:7.2f} {pred_h[1]:7.2f} {pred_h[2]:7.2f}  {chi_h:6.2f}   1")
    print(f"quadrupôle intérieur (objet)   {pred_q[0]:7.2f} {pred_q[1]:7.2f} {pred_q[2]:7.2f}  {chi_q:6.2f}   1")
    delta = 43.0 / rad_as / (100 / 0.240846) / math.pi
    print(f"exposant de Hall pour 43 secondes par siècle sur Mercure seul : 2 + {delta:.3e}")
    print("Sur Mercure seul, les trois familles s'ajustent exactement (un nombre, un paramètre).")
    return chi_rg, chi_h, chi_q, delta


# ----------------------------------------------------------------------------
# Partie F — clair de lune monstrueux
# ----------------------------------------------------------------------------
def partie_F():
    titre("PARTIE F — Clair de lune monstrueux : coefficients de j, décompositions, rareté")
    M = 8

    def sigma3(n):
        return sum(d**3 for d in range(1, n + 1) if n % d == 0)

    E4 = [1] + [240 * sigma3(n) for n in range(1, M)]

    def prod(a, b):
        return [sum(a[i] * b[k - i] for i in range(k + 1)) for k in range(M)]

    E4c = prod(prod(E4, E4), E4)
    # Delta/q = produit (1-q^n)^24
    D = [1] + [0] * (M - 1)
    for n in range(1, M):
        for _ in range(24):
            D = [D[k] - (D[k - n] if k >= n else 0) for k in range(M)]
    # j.q = E4^3 / (Delta/q) : division de séries entières à coefficients entiers
    J = []
    reste = E4c[:]
    for k in range(M):
        ck = reste[k]
        J.append(ck)
        for i in range(k, M):
            reste[i] -= ck * D[i - k]
    c = {-1: J[0], 0: J[1], 1: J[2], 2: J[3], 3: J[4], 4: J[5]}
    print(f"j(q) = 1/q + {c[0]} + {c[1]} q + {c[2]} q^2 + {c[3]} q^3 + {c[4]} q^4 + ...")
    d = [1, 196883, 21296876, 842609326]   # dimensions lues dans Gannon 2004, p. 3
    ok1 = c[1] == d[0] + d[1]
    ok2 = c[2] == d[0] + d[1] + d[2]
    ok3 = c[3] == 2 * d[0] + 2 * d[1] + d[2] + d[3]
    print(f"196884 = 1 + 196883                               : {ok1}")
    print(f"21493760 = 1 + 196883 + 21296876                  : {ok2}")
    print(f"864299970 = 2.1 + 2.196883 + 21296876 + 842609326 : {ok3}")
    print("Rareté sous un nul grossier (entier uniforme entre 1 et 2 fois le coefficient ; multiplicités 0, 1 ou 2")
    print("des k premières dimensions) : nombre de sommes possibles, et part des entiers atteints.")
    for k, coef in ((2, c[1]), (3, c[2]), (4, c[3])):
        sommes = {sum(m * x for m, x in zip(mult, d[:k])) for mult in itertools.product(range(3), repeat=k)}
        sommes = {x for x in sommes if 1 <= x <= 2 * coef}
        print(f"   k = {k} : {len(sommes):3d} sommes parmi {2 * coef} entiers -> {len(sommes) / (2 * coef):.2e}")
    print("Multiplicités libres : tout entier positif est une somme (n copies de la dimension 1) -> part 1.")
    return c, (ok1, ok2, ok3)


if __name__ == "__main__":
    print("forme-anomalie-objet-manquant-v1.py")
    print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; graine racine {GRAINE_RACINE} (SeedSequence, 6 graines dérivées)")
    partie_A()
    partie_B()
    partie_C()
    partie_D()
    partie_E()
    partie_F()
    print("\nFIN")
