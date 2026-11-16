"""Attaque des méthodes de l'angle « inférence universelle » (correction des poids du nul) — programme du réfutateur — v1.

Statut : réfutation, mise au point exploratoire, aucune revendication. Processeur seul, aucun appel réseau. Ce programme est
écrit sans recopier le banc de l'auteur (`banc_universelle_v1.py`) : autre formulation du maximum (mélange sur les sommets
du polytope, montée par espérance-maximisation accélérée par extrapolation), autres mondes, autres cartes, décision par
encadrement. Aucun fichier des dossiers de copie du juge n'est exécuté ni importé ; la famille du nul est réécrite d'après
la lecture de `nul_v9.py` (l. 19 à 25) : sur chaque morceau d'une partition à un niveau, un mélange des lois connues propre
au morceau, plus un bruit aveugle commun, Σ_j a_j + Σ_k r_k = 1 par morceau.

Ce que le programme fait.
1. Maximum de vraisemblance d'une famille par morceaux, encadré : tout point du polytope est un mélange de ses sommets
   (« une loi connue par morceau » : J² sommets ; « bruit aveugle seul sur l'issue k » : K sommets). Le problème devient
   max_π Σ_s w_s log(G_s·π) sur un simplexe. Pour tout point admissible π : valeur atteinte f(π) ≤ maximum ≤ f(π) +
   max_m ∇f(π)_m − Σ_s w_s (concavité ; ∇f(π)·π = Σ_s w_s). Le programme garde, par question et par partition, la plus
   haute valeur atteinte (borne basse du maximum) et le plus petit certificat (borne haute).
2. Décision par encadrement : la statistique d'une méthode décroît quand un maximum du nul monte. Calculée avec les
   certificats, elle donne ce que la méthode rend (« bas ») ; calculée avec les valeurs atteintes, elle borne ce que tout
   certificat valide pourrait rendre (« haut »). Promotion si bas ≥ seuil à un instant lu ; refus certain si haut < seuil à
   tous les instants ; sinon on itère ; au plafond d'itérations, refus (compté « indécis »). Quand le monde est un membre
   connu du nul, son propre paramètre est un point admissible : sa vraisemblance sert de première valeur atteinte. Ce
   n'est pas un raccourci de preuve : c'est le fait « un maximum est au moins la valeur en un point », vérifié en clair sur
   un sous-échantillon résolu sans ce point (mode « controle »).
3. Mondes : membres défavorables du nul (intérieur, sommet sur la coupure de l'archive, poids extrêmes, beaucoup de
   composantes, peu de tirages, copie par morceaux sur un seuil de la grille, par sous-population, hors de la grille), et
   mondes « tranchants » (lois connues presque certaines, membre au sommet) où le maximum du nul tombe sur le vrai membre :
   la valeur e du juge y égale le rapport de vraisemblance simple, et une carte « loterie » (toute sa masse sur une issue
   de probabilité 1/M en un tirage) approche la borne de Ville.
4. Cartes : copie exacte, carte surconfiante, loteries placées pour chaque méthode. Arrêt optionnel : la promotion compte
   si la statistique passe le seuil à l'un des instants lus.
5. Dents (variantes volontairement fausses, pour vérifier que l'attaque voit une erreur de compte) : pénalité d'un nat,
   découpes croisées par le maximum des deux parts, région de confiance lue au seuil 1/α, et les deux façons des fiches.

Usage :
  python attaque_universelle_v1.py autotest SORTIE.json
  python attaque_universelle_v1.py taille CAS MONDES SORTIE.json [processus]
  python attaque_universelle_v1.py puissance BASE DOSE MONDES SORTIE.json [processus]
  python attaque_universelle_v1.py assembler DOSSIER_DES_PARTIES SORTIE.json
Graines : numpy.random.SeedSequence(entropy=ENTROPIE, spawn_key=(indice du cas, r)), scindée en (monde, issues, parts).
"""
import hashlib
import json
import math
import os
import platform
import sys
import time

import numpy as np

ALPHA = 0.05
SEUIL = math.log(1.0 / ALPHA)
BETA = 0.025                                   # part de α payée par la région de confiance (réglage de l'auteur)
SEUIL_CONFIANCE = math.log(1.0 / (ALPHA - BETA))
LAMBDAS = (0.0, 0.25, 1.0, 4.0, 16.0)          # multiplicateurs de la dualité faible (réglage de l'auteur)
NOMBRE_PARTS = 4                               # sous-échantillonnage : quatre moitiés tirées avant les issues
PAS_FICHE = (0.05, 0.2)
PLANCHER = 1e-12
TOLERANCE = 1e-4
CYCLES_DECISION = 600
CYCLES_VALEUR = 500
ENTROPIE_TAILLE = 2026111571
ENTROPIE_PUISSANCE = 2026111572
ENTROPIE_AUTOTEST = 2026111573
D_LIBRES = 7                                   # pénalité de complexité de l'auteur : (d/2)·log t, d = 7
VALIDES = ("v9", "dense", "moitie_jugee", "croisee", "sous_echantillons", "confiance")
DENTS = ("penalise_1nat", "croisee_par_le_maximum", "confiance_au_seuil_alpha")


def grille_deciles():
    from scipy.stats import norm
    return tuple(float(norm.ppf(q / 10.0)) for q in range(1, 10))


GRILLE = grille_deciles()


def clopper_pearson(k, n, niveau=0.95):
    from scipy.stats import beta
    a = (1.0 - niveau) / 2.0
    bas = 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))
    haut = 1.0 if k == n else float(beta.ppf(1.0 - a, k + 1, n - k))
    return [round(bas, 5), round(haut, 5)]


# ----------------------------------------------------------------------------------------------------------------------
# Maximum encadré d'une famille par morceaux
# ----------------------------------------------------------------------------------------------------------------------
def composantes(A, y, masques, K):
    """G[p, s, m] : probabilité, à l'issue observée du tirage s, du sommet m de la partition p.
    Sommets : (j0, j1) → loi connue j0 sur le morceau « faux », j1 sur le morceau « vrai » ; puis les K lois certaines."""
    n, J = A.shape
    P = masques.shape[0]
    G = np.empty((P, n, J * J + K))
    a0 = np.repeat(A, J, axis=1)                # colonne j0·J + j1 → A[:, j0]
    a1 = np.tile(A, (1, J))                     # colonne j0·J + j1 → A[:, j1]
    G[:, :, :J * J] = np.where(masques[:, :, None], a1[None], a0[None])
    G[:, :, J * J:] = np.eye(K)[y][None]
    return G


class Lot:
    """Encadre, pour Q questions (vecteurs de poids de tirages ≥ 0) et un jeu de partitions, le maximum de
    Σ_s w_s log(G_s·π) sur le simplexe. `att` : plus haute valeur atteinte ; `cert` : plus petit certificat."""

    def __init__(self, G, Wq, partitions=None, pi0=None, att0=None, elaguer=True, tol=TOLERANCE):
        self.parts = np.arange(G.shape[0]) if partitions is None else np.asarray(partitions)
        self.G = G
        self.Wq = np.asarray(Wq, dtype=float)
        self.tot = self.Wq.sum(1)
        vides = self.tot <= 0                   # question sans tirage : produit vide, log-vraisemblance 0 pour tout membre
        self.tot = np.where(vides, 1.0, self.tot)
        Q, Pn, M = self.Wq.shape[0], len(self.parts), G.shape[2]
        self.pi = np.full((Pn, Q, M), 1.0 / M)
        if pi0 is not None:                     # pi0 : (Pn, M), un départ par partition
            self.pi[:] = np.asarray(pi0)[:, None, :]
        self.att = np.full((Q, Pn), -np.inf) if att0 is None else np.array(att0, dtype=float)
        self.cert = np.zeros((Q, Pn))           # une log-vraisemblance est ≤ 0
        self.actif = np.ones((Q, Pn), dtype=bool)
        self.att[vides, :] = 0.0
        self.actif[vides, :] = False
        self.elaguer, self.tol, self.cycles = elaguer, tol, 0

    def _evaluer(self, ip, lignes, pi):
        Gp = self.G[self.parts[ip]]             # (n, M)
        w = self.Wq[lignes]
        mix = np.maximum(pi @ Gp.T, 1e-300)     # (a, n)
        grad = (w / mix) @ Gp                   # (a, M)
        f = (w * np.log(mix)).sum(1)
        ecart = np.maximum(0.0, grad.max(1) - self.tot[lignes])
        self.att[lignes, ip] = np.maximum(self.att[lignes, ip], f)
        self.cert[lignes, ip] = np.minimum(self.cert[lignes, ip], f + ecart)
        return f, grad

    def _trier(self):
        ecart_propre = self.cert - self.att
        self.actif &= ecart_propre > self.tol
        if self.elaguer:                        # une partition dont le certificat est sous la meilleure valeur atteinte
            self.actif &= ~(self.cert < self.att.max(1)[:, None])   # ne peut pas porter le maximum : elle sort

    def avancer(self, cycles=1):
        """Un cycle = trois pas d'espérance-maximisation, dont un extrapolé (accélération) avec repli monotone."""
        for _ in range(cycles):
            self._trier()
            if not self.actif.any():
                return
            for ip in range(len(self.parts)):
                lignes = np.nonzero(self.actif[:, ip])[0]
                if not len(lignes):
                    continue
                tot = self.tot[lignes][:, None]
                p0 = self.pi[ip, lignes]
                _, g0 = self._evaluer(ip, lignes, p0)
                p1 = p0 * g0 / tot
                f1, g1 = self._evaluer(ip, lignes, p1)
                p2 = p1 * g1 / tot
                r = p1 - p0
                v = (p2 - p1) - r
                nr, nv = np.sqrt((r * r).sum(1)), np.sqrt((v * v).sum(1))
                al = -np.clip(nr / np.maximum(nv, 1e-300), 1.0, 512.0)
                pp = p0 - 2.0 * al[:, None] * r + (al * al)[:, None] * v
                for _ in range(6):              # retour vers le pas simple tant que le point sort du simplexe
                    mauvais = (pp < 0).any(1)
                    if not mauvais.any():
                        break
                    al = np.where(mauvais, (al - 1.0) / 2.0, al)
                    pp = p0 - 2.0 * al[:, None] * r + (al * al)[:, None] * v
                mauvais = (pp < 0).any(1) | ~np.isfinite(pp).all(1)
                pp[mauvais] = p2[mauvais]
                pp = pp / pp.sum(1, keepdims=True)
                fp, gp = self._evaluer(ip, lignes, pp)
                p3 = pp * gp / tot
                garde = fp >= f1
                nouveau = np.where(garde[:, None], p3, p2)
                nouveau = np.maximum(nouveau, 1e-250)
                self.pi[ip, lignes] = nouveau / nouveau.sum(1, keepdims=True)
            self.cycles += 1

    def converger(self, cycles_max=CYCLES_VALEUR):
        while self.cycles < cycles_max:
            self._trier()
            if not self.actif.any():
                break
            self.avancer(1)
        self._trier()
        return self.att, self.cert


def log_moyenne_exp(a, axe):
    """log de la moyenne des exponentielles le long d'un axe ; +inf si une entrée vaut +inf, −inf si toutes valent −inf."""
    m = np.max(a, axis=axe, keepdims=True)
    m0 = np.where(np.isfinite(m), m, 0.0)
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        r = np.squeeze(m0, axis=axe) + np.log(np.mean(np.exp(a - m0), axis=axe))
    return np.where(np.isposinf(np.squeeze(m, axis=axe)), np.inf, r)


def decider(lot, statistiques, instant_de_question, cycles_max=CYCLES_DECISION, pas=2):
    """statistiques : {nom: (fonction V(Q, Pn) → valeurs par instant, seuil)}. Rend {nom: (promue, indécise, bas, haut)}.
    bas = statistique certifiée (ce que la méthode rend) ; haut = borne de toute statistique valide."""
    rendu, restant = {}, dict(statistiques)
    while True:
        vivant = np.zeros(int(instant_de_question.max()) + 1, dtype=bool)
        for nom in list(restant):
            fonction, seuil = restant[nom]
            bas, haut = fonction(lot.cert), fonction(lot.att)
            haut = np.where(np.isnan(haut), np.inf, haut)     # aucune valeur atteinte encore : rien n'est exclu
            if np.max(bas) >= seuil:
                rendu[nom] = (True, False, float(np.max(bas)), float(np.max(haut)))
                del restant[nom]
            elif np.max(haut) < seuil:
                rendu[nom] = (False, False, float(np.max(bas)), float(np.max(haut)))
                del restant[nom]
            else:
                vivant |= haut >= seuil
        if not restant:
            return rendu
        lot._trier()
        lot.actif &= vivant[instant_de_question][:, None]     # un instant sans promotion possible ne se calcule plus
        if lot.cycles >= cycles_max or not lot.actif.any():
            for nom, (fonction, seuil) in restant.items():
                bas, haut = fonction(lot.cert), fonction(lot.att)
                rendu[nom] = (bool(np.max(bas) >= seuil), bool(np.max(bas) < seuil), float(np.max(bas)), float(np.max(haut)))
            return rendu
        lot.avancer(pas)


# ----------------------------------------------------------------------------------------------------------------------
# Mondes
# ----------------------------------------------------------------------------------------------------------------------
def loi_souple(rng, z, g, K):
    W = rng.normal(0.0, 1.3, size=(K, z.shape[1]))
    b = rng.normal(0.0, 0.4, size=K)
    c = rng.normal(0.0, 0.5, size=K)
    s = z @ W.T + b + np.outer(g, c)
    s -= s.max(1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(1, keepdims=True)


def partitions_du_banc(z, g, jA, sA):
    """[0] aucune coupure ; [1] coupure de l'archive ; [2] sous-population ; [3..] neuf déciles par trait."""
    m = [np.zeros(len(g), dtype=bool), z[:, jA] > sA, g == 1]
    for j in range(z.shape[1]):
        for c in GRILLE:
            m.append(z[:, j] > c)
    return np.array(m)


def poids_sommets(a0, a1, rho, J):
    """Poids, sur les sommets (j0, j1) puis les lois certaines, du membre (a0·(1−r), a1·(1−r), rho), r = Σ rho."""
    r = float(np.sum(rho))
    return np.concatenate([(1.0 - r) * np.outer(a0, a1).ravel(), np.asarray(rho, dtype=float)])


def loi_du_membre(S, masque, a0, a1, rho):
    r = float(np.sum(rho))
    melange = np.where(masque[:, None], np.einsum("njk,j->nk", S, a1), np.einsum("njk,j->nk", S, a0))
    return (1.0 - r) * melange + np.asarray(rho)[None, :]


def instants_de(n):
    pas = n // 8
    return tuple(range(pas, n + 1, pas))


def monde_souple(rng, cas):
    """Monde à lois connues souples (softmax de deux traits et de la sous-population). Rend le dictionnaire du monde ;
    `membre` = (indice de partition, poids sur les sommets, vrai si le membre est sans coupure) ou None hors classe."""
    K, n, J = 3, 200, 3
    if cas == "beaucoup_de_composantes":
        J = 7
    if cas == "peu_de_tirages":
        n = 48
    z = rng.normal(size=(n, 2))
    g = rng.integers(0, 2, size=n)
    jA = int(rng.integers(0, 2))
    sA = float(rng.uniform(-0.9, 0.9))
    haut = z[:, jA] > sA
    lois = [loi_souple(rng, z, g, K) for _ in range(J + 1)]
    S = np.stack(lois[:J], axis=1)
    S[:, J - 1, :] = np.where(haut[:, None], lois[J - 1], lois[J])     # la dernière loi connue porte la coupure
    masques = partitions_du_banc(z, g, jA, sA)
    e = np.eye(J)
    ip, hors_classe, sans_coupure = 1, False, False
    forme = cas
    if cas == "peu_de_tirages":
        forme = ("interieur", "sommet_archive")[int(rng.integers(0, 2))]
    if forme in ("interieur", "beaucoup_de_composantes"):
        r = float(rng.uniform(0.05, 0.4))
        a0, a1, rho = rng.dirichlet(np.ones(J)), rng.dirichlet(np.ones(J)), r * rng.dirichlet(np.ones(K))
    elif forme == "sommet_archive":
        j0, j1 = rng.choice(J, size=2, replace=False)
        a0, a1, rho = e[j0], e[j1], np.zeros(K)
    elif forme == "poids_extremes":
        j0, j1 = rng.choice(J, size=2, replace=False)
        a0 = np.full(J, 0.004); a0[j0] = 1.0 - 0.004 * (J - 1)
        a1 = np.full(J, 0.004); a1[j1] = 1.0 - 0.004 * (J - 1)
        rho = np.full(K, 0.0002); rho[int(rng.integers(0, K))] = 0.0096
    elif forme == "sans_coupure":
        r = float(rng.uniform(0.05, 0.4))
        a0 = rng.dirichlet(np.ones(J)); a1 = a0
        rho = r * rng.dirichlet(np.ones(K))
        ip, sans_coupure = 0, True
    elif forme in ("morceaux_sur_grille", "sous_population", "morceaux_hors_grille"):
        j0, j1 = rng.choice(J, size=2, replace=False)
        a0, a1, rho = e[j0], e[j1], np.zeros(K)
        if forme == "morceaux_sur_grille":
            ip = 3 + int(rng.integers(0, 2 * len(GRILLE)))
        elif forme == "sous_population":
            ip = 2
        else:                                   # seuil hors de la grille et hors de l'archive : hors de la classe du banc
            jH = int(rng.integers(0, 2))
            while True:
                sH = float(rng.uniform(-1.2, 1.2))
                if min(abs(sH - c) for c in GRILLE) >= 0.08 and (jH != jA or abs(sH - sA) >= 0.08):
                    break
            hors_classe = True
            masque_monde = z[:, jH] > sH
    else:
        raise ValueError(cas)
    if not hors_classe:
        masque_monde = masques[ip]
    Pm = loi_du_membre(S, masque_monde, a0, a1, rho)
    membre = None if hors_classe else (ip, poids_sommets(a0, a1, rho, J), sans_coupure)
    return {"n": n, "K": K, "J": J, "z": z, "g": g, "S": S, "P": Pm, "masques": masques, "membre": membre,
            "instants": instants_de(n), "forme": forme}


EPS_TRANCHANT = 2e-4


def monde_tranchant(rng, paris_fn, parts):
    """Lois connues presque certaines (une issue à 1 − 2ε, les autres à ε), sauf aux tirages « tendres » désignés, où toutes
    les lois connues donnent la même loi tendre : l'issue 2 y a la probabilité p. Monde = sommet du nul (une loi connue
    partout, ou une loi connue de chaque côté de la coupure de l'archive). `paris_fn(parts, rng)` rend [(indice, p), …]."""
    K, n, J = 3, 200, 3
    z = rng.normal(size=(n, 2))
    g = rng.integers(0, 2, size=n)
    jA = int(rng.integers(0, 2))
    sA = float(rng.uniform(-0.9, 0.9))
    S = np.full((n, J, K), EPS_TRANCHANT)
    classes = []
    for j in range(J):
        wj, bj = rng.normal(size=2), rng.normal(0.0, 0.3)
        cj = (z @ wj + bj > 0).astype(int)
        classes.append(cj)
        S[np.arange(n), j, cj] = 1.0 - 2.0 * EPS_TRANCHANT
    paris = paris_fn(parts, rng)
    for i, p in paris:
        c = classes[0][i]
        ligne = np.full(K, EPS_TRANCHANT)
        ligne[2] = p
        ligne[c] = 1.0 - p - EPS_TRANCHANT
        S[i, :, :] = ligne[None, :]
    masques = partitions_du_banc(z, g, jA, sA)
    e = np.eye(J)
    if int(rng.integers(0, 2)) == 0:            # une loi connue partout : sommet de toutes les partitions
        ip, a0, a1, sans_coupure, forme = 0, e[0], e[0], True, "tranchant_sans_coupure"
    else:                                       # copie par morceaux sur la coupure de l'archive
        ip, a0, a1, sans_coupure, forme = 1, e[0], e[1], False, "tranchant_sur_archive"
    Pm = np.where(masques[ip][:, None], S[:, int(np.argmax(a1)), :], S[:, int(np.argmax(a0)), :])
    return {"n": n, "K": K, "J": J, "z": z, "g": g, "S": S, "P": Pm, "masques": masques,
            "membre": (ip, poids_sommets(a0, a1, np.zeros(K), J), sans_coupure), "instants": instants_de(n),
            "forme": forme, "paris": paris}


def tirer_issues(rng, P):
    u = rng.random(P.shape[0])
    return np.minimum((u[:, None] > np.cumsum(P, axis=1)).sum(1), P.shape[1] - 1)


def tirer_parts(rng, n):
    parts = np.zeros((NOMBRE_PARTS, n), dtype=bool)
    for b in range(NOMBRE_PARTS):
        parts[b, rng.choice(n, size=n // 2, replace=False)] = True
    return parts


# ----------------------------------------------------------------------------------------------------------------------
# Cartes
# ----------------------------------------------------------------------------------------------------------------------
def carte_surconfiante(P, exposant=1.5):
    Q = P ** exposant
    return Q / Q.sum(1, keepdims=True)


def carte_loterie(P, paris):
    """Copie de la loi du monde, sauf aux tirages pariés : presque toute la masse sur l'issue pariée."""
    Q = P.copy()
    K = P.shape[1]
    for i, k in paris:
        Q[i, :] = 1e-9
        Q[i, k] = 1.0 - (K - 1) * 1e-9
    return Q


def pari_proche(P, indices, M):
    """Parmi les tirages `indices`, le pari (un couple (tirage, issue), ou deux couples sur deux tirages) dont la
    probabilité de gain est la plus proche de 1/M sans dépasser 1/20,5 (le gain doit multiplier la richesse par 20 au
    moins). Rend la liste des couples, ou None s'il n'y en a aucun."""
    sous = P[indices]
    K = sous.shape[1]
    plafond = 1.0 / 20.5
    cout1 = np.where(sous <= plafond, np.abs(np.log(sous * M)), np.inf)
    i1, k1 = np.unravel_index(int(np.argmin(cout1)), cout1.shape)
    meilleur, pari = float(cout1[i1, k1]), [(int(indices[i1]), int(k1))]
    plat = sous.ravel()
    produit = np.outer(plat, plat)
    tirage = np.repeat(np.arange(len(indices)), K)
    produit[tirage[:, None] == tirage[None, :]] = np.inf          # deux paris sur deux tirages différents
    cout2 = np.where(produit <= plafond, np.abs(np.log(produit * M)), np.inf)
    a, b = np.unravel_index(int(np.argmin(cout2)), cout2.shape)
    if cout2[a, b] < meilleur:
        meilleur = float(cout2[a, b])
        pari = [(int(indices[a // K]), int(a % K)), (int(indices[b // K]), int(b % K))]
    return pari if np.isfinite(meilleur) else None


# ----------------------------------------------------------------------------------------------------------------------
# Méthodes (réécrites d'après les énoncés de la note de l'auteur, sections 4.1 à 4.10)
# ----------------------------------------------------------------------------------------------------------------------
def _prefixes(n, ts, base=None, debut=0):
    W = np.zeros((len(ts), n))
    for i, t in enumerate(ts):
        W[i, debut:debut + t] = 1.0
    return W if base is None else W * base[None, :]


def juger(w, y, Q, parts, methodes, classe=None, mode="decision", avec_membre=True, cycles_max=None):
    """Juge une carte Q dans le monde w sur les issues y. Rend {méthode: (promue, indécise, bas, haut)}.
    `classe` : indices des partitions du nul (None = toutes : le « v9 du banc »). `avec_membre` : la vraisemblance du
    vrai membre sert de première valeur atteinte (faux : résolution sans ce point, mode de contrôle)."""
    n, K, J = w["n"], w["K"], w["J"]
    T = w["instants"]
    h = n // 2
    Tm = tuple(t for t in T if t <= h)
    idx = np.arange(n)
    lq = np.log(np.maximum(Q[idx, y], PLANCHER))
    cum = np.cumsum(lq)
    A = w["S"][idx, :, y]
    if "G" not in w or w.get("G_y") is not y:
        w["G"], w["G_y"] = composantes(A, y, w["masques"], K), y
    G = w["G"]
    cl = np.arange(G.shape[0]) if classe is None else np.asarray(classe)
    membre = w["membre"] if avec_membre else None
    lm = np.log(np.maximum(w["P"][idx, y], 1e-300)) if membre is not None else None
    M = G.shape[2]

    def lot_de(Wq, elaguer=True):
        pi0, att0 = None, None
        if membre is not None:
            ip, pim, sans_coupure = membre
            if abs(float(pim.sum()) - 1.0) > 1e-9 or (pim < 0).any() or \
                    float(np.max(np.abs(G[ip] @ pim - w["P"][idx, y]))) > 1e-9:
                raise RuntimeError("le point du vrai membre n'est pas un point admissible de sa famille")
            pi0 = np.full((len(cl), M), 1.0 / M)
            att0 = np.full((Wq.shape[0], len(cl)), -np.inf)
            depart = 0.98 * pim + 0.02 / M
            for i, p in enumerate(cl):
                if p == ip or sans_coupure:
                    pi0[i] = depart
                    att0[:, i] = Wq @ lm
        return Lot(G, Wq, partitions=cl, pi0=pi0, att0=att0, elaguer=elaguer)

    plafond = cycles_max if cycles_max is not None else (CYCLES_DECISION if mode == "decision" else CYCLES_VALEUR)
    rendu = {}

    def jouer(Wq, statistiques, instant_de_question, elaguer=True):
        lot = lot_de(Wq, elaguer)
        if mode == "valeur":
            lot.converger(plafond)
            for nom, (fonction, seuil) in statistiques.items():
                bas, haut = fonction(lot.cert), fonction(lot.att)
                rendu[nom] = (bool(np.max(bas) >= seuil), False, float(np.max(bas)), float(np.max(haut)))
        else:
            rendu.update(decider(lot, statistiques, np.asarray(instant_de_question), plafond))
        rendu.setdefault("_cycles", 0)
        rendu["_cycles"] += lot.cycles

    # --- maximum sur tous les tirages (référence), pénalités, mélange a priori, lecture dense ---
    lqT = np.array([cum[t - 1] for t in T])
    logT = np.log(np.array(T, dtype=float))
    stats = {}
    if "v9" in methodes:
        stats["v9"] = (lambda V: lqT - V.max(1), SEUIL)
    if "penalise_1nat" in methodes:
        stats["penalise_1nat"] = (lambda V: lqT - V.max(1) + 1.0, SEUIL)
    if "penalise_complexite" in methodes:
        stats["penalise_complexite"] = (lambda V: lqT - V.max(1) + 0.5 * D_LIBRES * logT, SEUIL)
    if stats:
        jouer(_prefixes(n, T), stats, np.arange(len(T)))
    if "melange_a_priori" in methodes:
        def melange(V):
            return lqT - log_moyenne_exp(V, 1)
        jouer(_prefixes(n, T), {"melange_a_priori": (melange, SEUIL)}, np.arange(len(T)), elaguer=False)
    if "dense" in methodes:
        pas = max(1, n // 20)
        Td = tuple(range(pas, n + 1, pas))
        lqD = np.array([cum[t - 1] for t in Td])
        jouer(_prefixes(n, Td), {"dense": (lambda V: lqD - V.max(1), SEUIL)}, np.arange(len(Td)))
    # --- moitié jugée : maximum du nul sur la seconde moitié, celle où la valeur e est évaluée ---
    if "moitie_jugee" in methodes:
        lqM = np.array([lq[h:h + t].sum() for t in Tm])
        jouer(_prefixes(n, Tm, debut=h), {"moitie_jugee": (lambda V: lqM - V.max(1), SEUIL)}, np.arange(len(Tm)))
    # --- découpes croisées (indices pairs, indices impairs), moyenne des deux valeurs e ; dent : leur maximum ---
    if "croisee" in methodes or "croisee_par_le_maximum" in methodes:
        pair = (idx % 2 == 0).astype(float)
        Wq = np.concatenate([_prefixes(n, T, base=pair), _prefixes(n, T, base=1.0 - pair)])
        lqC = Wq @ lq
        nT = len(T)

        def moyenne(V):
            return log_moyenne_exp((lqC - V.max(1)).reshape(2, nT), 0)

        stats = {}
        if "croisee" in methodes:
            stats["croisee"] = (moyenne, SEUIL)
        if "croisee_par_le_maximum" in methodes:
            stats["croisee_par_le_maximum"] = (lambda V: (lqC - V.max(1)).reshape(2, nT).max(0), SEUIL)
        jouer(Wq, stats, np.tile(np.arange(nT), 2))
    # --- sous-échantillonnage : moyenne des valeurs e de quatre moitiés tirées avant les issues ---
    if "sous_echantillons" in methodes:
        Wq = np.concatenate([_prefixes(n, T, base=parts[b].astype(float)) for b in range(len(parts))])
        lqS = Wq @ lq
        nT, B = len(T), len(parts)

        def moyenne_s(V):
            return log_moyenne_exp((lqS - V.max(1)).reshape(B, nT), 0)

        jouer(Wq, {"sous_echantillons": (moyenne_s, SEUIL)}, np.tile(np.arange(nT), B))
    # --- région de confiance apprise sur la première moitié, maximum restreint sur la seconde ; dent : seuil 1/α ---
    if "confiance" in methodes or "confiance_au_seuil_alpha" in methodes:
        d1 = np.zeros(n); d1[:h] = 1.0
        c = float(lq[:h].sum()) - math.log(1.0 / BETA)
        lignes, inst = [], []
        for i, t in enumerate(Tm):
            d0 = np.zeros(n); d0[h:h + t] = 1.0
            for lam in LAMBDAS:
                lignes.append(d0 + lam * d1)
                inst.append(i)
        Wq = np.array(lignes)
        lq0 = np.array([lq[h:h + t].sum() for t in Tm])
        lam_v = np.tile(np.array(LAMBDAS), len(Tm))

        def confiance(V):
            b = (V.max(1) - lam_v * c).reshape(len(Tm), len(LAMBDAS))
            return lq0 - b.min(1)

        stats = {}
        if "confiance" in methodes:
            stats["confiance"] = (confiance, SEUIL_CONFIANCE)
        if "confiance_au_seuil_alpha" in methodes:
            stats["confiance_au_seuil_alpha"] = (confiance, SEUIL)
        jouer(Wq, stats, np.array(inst))
    return rendu


def fiche_en_ligne(w, y, Q, pas):
    """Fiche argon-p2-01 : par cellule de la partition de l'archive, poids sur les J lois connues et les K lois certaines,
    uniformes au départ, mis à jour après chaque tirage par descente de gradient exponentielle sur la perte logarithmique.
    Dénominateur : produit des probabilités prédites avant chaque tirage."""
    n, K, J = w["n"], w["K"], w["J"]
    idx = np.arange(n)
    lq = np.log(np.maximum(Q[idx, y], PLANCHER))
    experts = np.concatenate([w["S"][idx, :, y], np.eye(K)[y]], axis=1)      # (n, J + K)
    cellule = w["masques"][1].astype(int)
    poids = np.full((2, J + K), 1.0 / (J + K))
    total, trajet = 0.0, np.empty(n)
    for s in range(n):
        c = cellule[s]
        p = max(float(poids[c] @ experts[s]), PLANCHER)
        total += lq[s] - math.log(p)
        trajet[s] = total
        poids[c] = poids[c] * np.exp(np.minimum(pas * experts[s] / p, 50.0))
        poids[c] /= poids[c].sum()
    lus = trajet[np.array(w["instants"]) - 1]
    return bool(lus.max() >= SEUIL), float(lus.max())


def fiche_moitie(w, y, Q):
    """Fiche argon-p1-01 : poids du nul limité (aucune coupure, coupure de l'archive) ajustés au maximum de vraisemblance
    sur la première moitié ; valeur e sur la seconde moitié avec ces poids fixés ; lecture aux instants de la seconde moitié."""
    n, K = w["n"], w["K"]
    h = n // 2
    idx = np.arange(n)
    lq = np.log(np.maximum(Q[idx, y], PLANCHER))
    A = w["S"][idx, :, y]
    G = composantes(A, y, w["masques"][:2], K)
    d1 = np.zeros((1, n)); d1[0, :h] = 1.0
    lot = Lot(G, d1, elaguer=False)
    lot.converger(300)
    ip = int(np.argmax(lot.att[0]))
    p = np.maximum(G[ip] @ lot.pi[ip, 0], PLANCHER)
    trajet = np.cumsum((lq - np.log(p))[h:])
    Tm = np.array([t for t in w["instants"] if t <= h])
    lus = trajet[Tm - 1]
    return bool(lus.max() >= SEUIL), float(lus.max())


# ----------------------------------------------------------------------------------------------------------------------
# Cas de taille
# ----------------------------------------------------------------------------------------------------------------------
CAS_SOUPLES = ("interieur", "sommet_archive", "poids_extremes", "beaucoup_de_composantes", "peu_de_tirages",
               "morceaux_sur_grille", "sous_population", "sans_coupure")
CAS_HORS_CLASSE = ("morceaux_hors_grille",)


def _paris_v9(parts, rng):
    return [(3, 1.0 / 22.0)]


def _paris_moitie(parts, rng):
    return [(103, 1.0 / 22.0)]


def _paris_croisee(parts, rng):
    return [(4, 1.0 / 42.0), (5, 1.0 / 42.0)]


def _paris_sous(parts, rng):
    compte = parts[:, :25].sum(0)
    i = int(np.argmax(compte))
    c = int(compte[i])
    M = 1.03 * (20.0 * NOMBRE_PARTS - (NOMBRE_PARTS - c)) / c
    return [(i, 1.0 / max(M, 22.0))]


def _paris_confiance(parts, rng):
    return [(50, 1.0 / 52.0), (130, 1.0 / 41.0)]


def _paris_dent_penalise(parts, rng):
    return [(3, 1.0 / 8.0)]


def _paris_dent_croisee(parts, rng):
    return [(4, 1.0 / 22.0), (5, 1.0 / 22.0)]


def _paris_dent_confiance(parts, rng):
    return [(50, 1.0 / 52.0), (130, 1.0 / 20.5)]


CAS_TRANCHANTS = {
    "tranchant_v9": _paris_v9, "tranchant_moitie": _paris_moitie, "tranchant_croisee": _paris_croisee,
    "tranchant_sous_echantillons": _paris_sous, "tranchant_confiance": _paris_confiance,
    "tranchant_dent_penalise": _paris_dent_penalise, "tranchant_dent_croisee": _paris_dent_croisee,
    "tranchant_dent_confiance": _paris_dent_confiance,
}
CAS_TAILLE = CAS_SOUPLES + CAS_HORS_CLASSE + tuple(CAS_TRANCHANTS)
N_CONTROLE = {"souple": 30, "tranchant": 800}   # mondes résolus en clair (sans le point du vrai membre) : valeurs de la
# copie (mondes souples) ; N_CONTROLE_CARTES : décisions des cartes adverses refaites sans ce point, comparées une à une
N_CONTROLE_CARTES = 60
N_MELANGE = 300                                 # mondes où le mélange a priori et la pénalité de complexité sont joués


def un_monde_taille(args):
    cas, i_cas, r = args
    s_monde, s_issues, s_parts = np.random.SeedSequence(entropy=ENTROPIE_TAILLE, spawn_key=(i_cas, r)).spawn(3)
    rng = np.random.default_rng(s_monde)
    out = {}
    if cas in CAS_TRANCHANTS:
        parts = tirer_parts(np.random.default_rng(s_parts), 200)
        w = monde_tranchant(rng, CAS_TRANCHANTS[cas], parts)
        y = tirer_issues(np.random.default_rng(s_issues), w["P"])
        Q = carte_loterie(w["P"], [(i, 2) for i, _ in w["paris"]])
        gagne = [bool(y[i] == 2) for i, _ in w["paris"]]
        res = juger(w, y, Q, parts, VALIDES + DENTS)
        out["loterie"] = {m: res[m][:2] for m in VALIDES + DENTS}
        out["_cycles"] = res.get("_cycles", 0)
        idx = np.arange(w["n"])
        ecart = np.cumsum(np.log(np.maximum(Q[idx, y], PLANCHER)) - np.log(w["P"][idx, y]))
        out["_rapport_simple"] = bool(max(ecart[t - 1] for t in w["instants"]) >= SEUIL)
        out["_paris_gagnes"] = gagne
        if r < N_CONTROLE["tranchant"]:
            clair = juger(w, y, Q, parts, VALIDES, avec_membre=False)
            out["_cycles_clair"] = clair.get("_cycles", 0)
            out["_desaccords"] = {m: [int(clair[m][0] != res[m][0]), int(clair[m][1])] for m in VALIDES}
        out["_forme"] = w["forme"]
        return out
    w = monde_souple(rng, cas)
    n = w["n"]
    parts = tirer_parts(np.random.default_rng(s_parts), n)
    y = tirer_issues(np.random.default_rng(s_issues), w["P"])
    T1 = w["instants"][0]
    cartes = {"copie": w["P"]}
    if cas not in CAS_HORS_CLASSE:
        cartes["surconfiante"] = carte_surconfiante(w["P"])
        pari = pari_proche(w["P"], np.arange(0, T1), 25.0)
        if pari is not None:
            cartes["loterie_debut"] = carte_loterie(w["P"], pari)
        pari = pari_proche(w["P"], np.arange(n // 2, n // 2 + T1), 45.0)
        if pari is not None:
            cartes["loterie_seconde_moitie"] = carte_loterie(w["P"], pari)
    cycles = 0
    idx = np.arange(n)
    for nom, Q in cartes.items():
        if cas in CAS_HORS_CLASSE:              # hors classe : le banc n'a aucune garantie ; on mesure le trou de sa grille
            res = {}
            for etiquette, cl in (("v8", [0]), ("limite", [0, 1]), ("v9", None)):
                res[etiquette] = juger(w, y, Q, parts, ("v9",), classe=cl)["v9"]
            res.update(juger(w, y, Q, parts, ("moitie_jugee", "croisee", "sous_echantillons", "confiance", "dense")))
            cycles += res.pop("_cycles", 0)
            out[nom] = {m: v[:2] for m, v in res.items()}
        else:
            res = juger(w, y, Q, parts, VALIDES + DENTS)
            cycles += res.pop("_cycles", 0)
            out[nom] = {m: v[:2] for m, v in res.items()}
            ecart = np.cumsum(np.log(np.maximum(Q[idx, y], PLANCHER)) - np.log(w["P"][idx, y]))
            out[nom]["_rapport_simple"] = bool(max(ecart[t - 1] for t in w["instants"]) >= SEUIL)
            if nom != "copie" and r < N_CONTROLE_CARTES:
                clair = juger(w, y, Q, parts, VALIDES, avec_membre=False)
                d = out.setdefault("_desaccords", {m: [0, 0] for m in VALIDES})
                for m in VALIDES:
                    d[m][0] += int(clair[m][0] != res[m][0])
                    d[m][1] += int(clair[m][1])
        if nom == "copie":
            for pas in PAS_FICHE:
                out[nom][f"fiche_en_ligne_{pas}"] = (fiche_en_ligne(w, y, Q, pas)[0], False)
            out[nom]["fiche_moitie"] = (fiche_moitie(w, y, Q)[0], False)
    if cas not in CAS_HORS_CLASSE and r < N_MELANGE:
        res = juger(w, y, w["P"], parts, ("melange_a_priori", "penalise_complexite"))
        cycles += res.pop("_cycles", 0)
        out["copie"]["melange_a_priori"] = res["melange_a_priori"][:2]
        out["copie"]["penalise_complexite"] = res["penalise_complexite"][:2]
    if cas not in CAS_HORS_CLASSE and r < N_CONTROLE["souple"]:
        # contrôle en clair : la copie, résolue sans le point du vrai membre ; log W certifié (bas) et borne (haut)
        res = juger(w, y, w["P"], parts, VALIDES, mode="valeur", avec_membre=False, cycles_max=300)
        cycles += res.pop("_cycles", 0)
        out["_controle"] = {m: [round(res[m][2], 6), round(res[m][3], 6)] for m in VALIDES}
    out["_cycles"] = cycles
    out["_forme"] = w["forme"]
    return out


def resumer(sorties, R):
    cartes = {}
    for s in sorties:
        for nom, v in s.items():
            if nom.startswith("_"):
                continue
            c = cartes.setdefault(nom, {})
            for m, val in v.items():
                d = c.setdefault(m, {"mondes": 0, "promotions": 0, "indecis_au_plafond": 0})
                d["mondes"] += 1
                if m == "_rapport_simple":
                    d["promotions"] += int(val)
                else:
                    d["promotions"] += int(val[0])
                    d["indecis_au_plafond"] += int(val[1])
    for nom, c in cartes.items():
        for m, d in c.items():
            d["taux"] = round(d["promotions"] / d["mondes"], 5)
            d["intervalle_clopper_pearson_95"] = clopper_pearson(d["promotions"], d["mondes"])
    return cartes


def essai_taille(cas, R, sortie, processus):
    import multiprocessing as mp
    if os.path.exists(sortie):
        raise SystemExit(f"sortie existante, jamais écrasée : {sortie}")
    i_cas = CAS_TAILLE.index(cas)
    t0 = time.time()
    with mp.get_context("fork").Pool(processus) as pool:
        sorties = pool.map(un_monde_taille, [(cas, i_cas, r) for r in range(R)], chunksize=16)
    duree = time.time() - t0
    doc = {"essai": "taille", "cas": cas, "mondes": R, "duree_s": round(duree, 1),
           "graines": {"entropie": ENTROPIE_TAILLE, "spawn_key": f"({i_cas}, r), r = 0..{R - 1}",
                       "scission": "(monde, issues, parts du sous-échantillonnage)"},
           "cartes": resumer(sorties, R),
           "cycles_du_solveur_par_monde_moyenne": round(float(np.mean([s["_cycles"] for s in sorties])), 3),
           "mondes_sans_aucune_iteration": int(sum(1 for s in sorties if s["_cycles"] == 0)),
           "formes": {f: int(sum(1 for s in sorties if s["_forme"] == f)) for f in sorted({s["_forme"] for s in sorties})}}
    if cas in CAS_TRANCHANTS:
        k = int(sum(1 for s in sorties if s["_rapport_simple"]))
        doc["rapport_de_vraisemblance_simple"] = {"promotions": k, "mondes": R, "taux": round(k / R, 5),
                                                  "intervalle_clopper_pearson_95": clopper_pearson(k, R),
                                                  "note": "martingale du vrai membre lue aux instants du juge : borne de Ville"}
        doc["paris_gagnes"] = {"au_moins_un": int(sum(1 for s in sorties if any(s["_paris_gagnes"]))),
                               "tous": int(sum(1 for s in sorties if all(s["_paris_gagnes"])))}
    des = [s["_desaccords"] for s in sorties if "_desaccords" in s]
    if des:
        doc["controle_en_clair_cartes_adverses"] = {
            "mondes": len(des),
            "decisions_differentes_avec_et_sans_le_point_du_membre": {m: int(sum(d[m][0] for d in des)) for m in VALIDES},
            "indecis_au_plafond_sans_le_point": {m: int(sum(d[m][1] for d in des)) for m in VALIDES}}
    controles = [s["_controle"] for s in sorties if "_controle" in s]
    if controles:
        doc["controle_en_clair_copie"] = {
            "mondes": len(controles),
            "plus_grand_log_w_certifie": {m: max(c[m][0] for c in controles) for m in VALIDES},
            "plus_grande_borne_haute_du_log_w": {m: max(c[m][1] for c in controles) for m in VALIDES},
            "plus_grand_ecart_haut_moins_bas": {m: max(c[m][1] - c[m][0] for c in controles) for m in VALIDES}}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    court = {nom: {m: f"{d['promotions']}/{d['mondes']}" for m, d in c.items()} for nom, c in doc["cartes"].items()}
    print(cas, round(duree, 1), "s", json.dumps(court, ensure_ascii=False), flush=True)
    for cle in ("rapport_de_vraisemblance_simple", "paris_gagnes", "controle_en_clair_copie", "controle_en_clair_cartes_adverses"):
        if cle in doc:
            print("  ", cle, json.dumps(doc[cle], ensure_ascii=False), flush=True)


# ----------------------------------------------------------------------------------------------------------------------
# Puissance : la comparaison au maximum certifié est-elle loyale ?
# ----------------------------------------------------------------------------------------------------------------------
BASES = ("morceaux", "sans_coupure")
DOSES = (0.0, 0.25, 0.40, 0.55)


def un_monde_puissance(args):
    base, dose, i_cas, r, avec_decoupes = args
    s_monde, s_issues, s_parts = np.random.SeedSequence(entropy=ENTROPIE_PUISSANCE, spawn_key=(i_cas, r)).spawn(3)
    rng = np.random.default_rng(s_monde)
    w = monde_souple(rng, "interieur" if base == "morceaux" else "sans_coupure")
    neuve = loi_souple(rng, w["z"], w["g"], w["K"])
    w["P"] = (1.0 - dose) * w["P"] + dose * neuve
    if dose > 0:
        w["membre"] = None                      # hors du nul : aucune valeur atteinte donnée d'avance
    parts = tirer_parts(np.random.default_rng(s_parts), w["n"])
    y = tirer_issues(np.random.default_rng(s_issues), w["P"])
    out = {}
    for etiquette, cl in (("v8", [0]), ("limite", [0, 1]), ("v9", None)):
        avec = dose == 0 and (cl is None or 1 in cl or base == "sans_coupure")
        out[etiquette] = juger(w, y, w["P"], parts, ("v9",), classe=cl, avec_membre=avec)["v9"][:2]
    if avec_decoupes:
        res = juger(w, y, w["P"], parts, ("dense", "moitie_jugee", "croisee", "sous_echantillons", "confiance"),
                    avec_membre=(dose == 0))
        for m in ("dense", "moitie_jugee", "croisee", "sous_echantillons", "confiance"):
            out[m] = res[m][:2]
    return out


def essai_puissance(base, dose, R, sortie, processus, avec_decoupes):
    import multiprocessing as mp
    if os.path.exists(sortie):
        raise SystemExit(f"sortie existante, jamais écrasée : {sortie}")
    i_cas = 100 + 10 * BASES.index(base) + DOSES.index(dose)
    t0 = time.time()
    with mp.get_context("fork").Pool(processus) as pool:
        sorties = pool.map(un_monde_puissance, [(base, dose, i_cas, r, avec_decoupes) for r in range(R)], chunksize=8)
    duree = time.time() - t0
    methodes = list(sorties[0])
    res = {}
    for m in methodes:
        k = int(sum(1 for s in sorties if s[m][0]))
        res[m] = {"mondes": R, "promotions": k, "taux": round(k / R, 5), "intervalle_clopper_pearson_95": clopper_pearson(k, R),
                  "indecis_au_plafond": int(sum(1 for s in sorties if s[m][1])),
                  "promue": "".join("1" if s[m][0] else "0" for s in sorties)}
    apparies = {}
    for m in methodes:
        if m != "v9":
            a = np.array([s[m][0] for s in sorties]); b = np.array([s["v9"][0] for s in sorties])
            apparies[f"{m}_contre_v9"] = {"seule_la_methode": int((a & ~b).sum()), "seul_le_v9": int((~a & b).sum()),
                                          "ecart_de_taux": round(float(a.mean() - b.mean()), 5)}
    doc = {"essai": "puissance", "base": base, "dose": dose, "mondes": R, "duree_s": round(duree, 1),
           "graines": {"entropie": ENTROPIE_PUISSANCE, "spawn_key": f"({i_cas}, r), r = 0..{R - 1}",
                       "scission": "(monde, issues, parts du sous-échantillonnage)"},
           "note": "monde = carte = (1 − dose)·base + dose·loi neuve ; base « morceaux » : membre intérieur à poids "
                   "différents de chaque côté de la coupure de l'archive (comme le banc de l'auteur) ; base « sans_coupure » : "
                   "mêmes poids des deux côtés (membre du nul sans coupure). Mêmes tirages, mêmes instants, même seuil.",
           "methodes": res, "apparies": apparies}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(base, dose, round(duree, 1), "s", json.dumps({m: v["taux"] for m, v in res.items()}), flush=True)


# ----------------------------------------------------------------------------------------------------------------------
# Auto-essai du solveur : encadrement comparé à un optimum calculé à part
# ----------------------------------------------------------------------------------------------------------------------
def autotest(sortie, jeux=120):
    from scipy.optimize import minimize
    if os.path.exists(sortie):
        raise SystemExit("sortie existante")
    racine = np.random.SeedSequence(entropy=ENTROPIE_AUTOTEST)
    pire_bas, pire_haut, pire_largeur, hors = -np.inf, -np.inf, 0.0, 0
    for ss in racine.spawn(jeux):
        rng = np.random.default_rng(ss)
        n, J, K = int(rng.integers(12, 80)), int(rng.integers(2, 5)), 3
        A = rng.dirichlet(np.ones(K) * rng.uniform(0.2, 2.0), size=(n, J))
        y = rng.integers(0, K, size=n)
        Ay = A[np.arange(n), :, y]
        masque = rng.random(n) < rng.uniform(0.1, 0.9)
        wts = np.where(rng.random(n) < 0.3, rng.uniform(0.0, 4.0, size=n), 1.0)
        G = composantes(Ay, y, masque[None, :], K)
        lot = Lot(G, wts[None, :], tol=1e-7)
        att, cert = lot.converger(4000)

        def moins_f(x):
            mu0, mu1, rho = x[:J], x[J:2 * J], x[2 * J:]
            p = np.where(masque, Ay @ mu1, Ay @ mu0) + rho[y]
            return -float((wts * np.log(np.maximum(p, 1e-300))).sum())

        cons = [{"type": "eq", "fun": lambda x: x[:J].sum() + x[2 * J:].sum() - 1.0},
                {"type": "eq", "fun": lambda x: x[J:2 * J].sum() + x[2 * J:].sum() - 1.0}]
        meilleur = -np.inf
        for _ in range(6):
            rho = rng.dirichlet(np.ones(K)) * rng.uniform(0.02, 0.9)
            x0 = np.concatenate([rng.dirichlet(np.ones(J)) * (1 - rho.sum()), rng.dirichlet(np.ones(J)) * (1 - rho.sum()), rho])
            res = minimize(moins_f, x0, method="SLSQP", bounds=[(0.0, 1.0)] * (2 * J + K), constraints=cons,
                           options={"maxiter": 500, "ftol": 1e-12})
            x = np.clip(res.x, 0.0, 1.0)
            if abs(x[:J].sum() + x[2 * J:].sum() - 1.0) < 1e-7 and abs(x[J:2 * J].sum() + x[2 * J:].sum() - 1.0) < 1e-7:
                meilleur = max(meilleur, -moins_f(x))
        pire_bas = max(pire_bas, float(att[0, 0] - meilleur))        # > 0 : mon point atteint dépasse l'optimum de référence
        pire_haut = max(pire_haut, float(meilleur - cert[0, 0]))     # > 0 : l'optimum de référence dépasse mon certificat
        pire_largeur = max(pire_largeur, float(cert[0, 0] - att[0, 0]))
        hors += int(meilleur > cert[0, 0] + 1e-6)
    doc = {"essai": "autotest du solveur", "jeux": jeux, "graine": {"entropie": ENTROPIE_AUTOTEST, "scission": "spawn(jeux)"},
           "optimum_de_reference_au_dessus_du_certificat_dans": hors,
           "plus_grand_exces_de_la_reference_sur_le_certificat": pire_haut,
           "plus_grand_exces_de_la_valeur_atteinte_sur_la_reference": pire_bas,
           "plus_grande_largeur_certificat_moins_atteinte": pire_largeur,
           "lecture": "validité du certificat : la première ligne doit valoir 0 ; l'excès de la valeur atteinte sur la "
                      "référence est permis (la référence, calculée à part par SLSQP, n'est pas un maximum garanti)"}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(json.dumps(doc, ensure_ascii=False, indent=1))


def assembler(dossier, sortie):
    if os.path.exists(sortie):
        raise SystemExit("sortie existante, jamais écrasée")
    ici = os.path.abspath(__file__)
    doc = {"essai": "attaque des méthodes de l'angle « inférence universelle »", "version": "v1",
           "statut": "réfutation, mise au point exploratoire, aucune revendication",
           "niveau": {"alpha": ALPHA, "seuil_log": SEUIL, "beta_confiance": BETA, "seuil_log_confiance": SEUIL_CONFIANCE,
                      "multiplicateurs": list(LAMBDAS), "parts_du_sous_echantillonnage": NOMBRE_PARTS,
                      "instants": "n/8, 2n/8, …, n (25 à 200 pour 200 tirages) ; lecture dense : n/20, …, n"},
           "reglages": {"tolerance": TOLERANCE, "cycles_decision": CYCLES_DECISION, "cycles_valeur": CYCLES_VALEUR,
                        "grille": list(GRILLE), "epsilon_tranchant": EPS_TRANCHANT, "mondes_melange": N_MELANGE,
                        "mondes_controle_copie": N_CONTROLE["souple"],
                        "mondes_controle_cartes_adverses": N_CONTROLE_CARTES, "mondes_controle_tranchant": N_CONTROLE["tranchant"]},
           "versions": {"python": platform.python_version(), "numpy": np.__version__},
           "empreinte_programme": hashlib.sha256(open(ici, "rb").read()).hexdigest(), "parties": {}}
    for nom in sorted(os.listdir(dossier)):
        if nom.startswith("partie-") and nom.endswith(".json"):
            doc["parties"][nom[len("partie-"):-len(".json")]] = json.load(open(os.path.join(dossier, nom)))
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(len(doc["parties"]), "parties réunies")


if __name__ == "__main__":
    commande = sys.argv[1]
    if commande == "autotest":
        autotest(sys.argv[2])
    elif commande == "taille":
        essai_taille(sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]) if len(sys.argv) > 5 else 3)
    elif commande == "puissance":
        essai_puissance(sys.argv[2], float(sys.argv[3]), int(sys.argv[4]), sys.argv[5],
                        int(sys.argv[6]) if len(sys.argv) > 6 else 3, len(sys.argv) > 7 and sys.argv[7] == "decoupes")
    elif commande == "assembler":
        assembler(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit(__doc__)
