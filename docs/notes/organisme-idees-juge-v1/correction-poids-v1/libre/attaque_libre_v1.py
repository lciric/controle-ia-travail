"""Attaque du réfutateur — angle « toute autre voie » (correction des poids du nul) — v1.

Mise au point exploratoire, aucune revendication. Processeur seul, numpy et scipy. Programme écrit par le réfutateur, sans
recopier celui du concepteur : autre découpage (lots de mondes vectorisés, décision au seuil au lieu de la valeur), autres
graines, autres mondes, cartes qui ne sont pas des copies. Aucun fichier des dossiers de copie n'est exécuté ni importé : la
logique utile du juge est recopiée d'après lecture, et dite ici.

Logique du juge recopiée (d'après `nul_filles_v2.evaluer_v2`, `nul_v9.py`, `a_blanc_v59.juger_carte`, lus) :
- pari plein : numérateur = vraisemblance de la carte, gelée avant les tirages ;
- n = 200 tirages frais, instants de lecture 25, 50, ..., 200, alpha = 0,05 ; promotion s'il existe un instant lu où
  log W_t = log q(y_1..t) - D_t >= log(1/alpha) (arrêt optionnel aux instants du juge) ;
- membre du nul pour une partition à deux cellules au plus : sur la cellule c, somme_j mu_{c,j} L_j + rho, mu >= 0, rho >= 0,
  somme_j mu_{c,j} + somme_k rho_k = 1 pour chaque cellule (poids propres à la cellule, bruit aveugle commun) ;
- valeur d'un membre = valeur atteinte + écart de Frank-Wolfe, bornée par 0 (certificat de `nul_v9._certificats`).

Ce que ce programme fait autrement que le juge, et pourquoi cela ne change pas la décision :
- il ne calcule pas D_t, il DÉCIDE si D_t <= tau_t, avec tau_t = log q(y_1..t) - log(1/alpha). Une partition est « dégagée »
  si son certificat (borne haute) est <= tau_t, « bloquée » si sa valeur atteinte (borne basse) est > tau_t. Un nul promeut à
  l'instant t si et seulement si toutes ses partitions sont dégagées. Si ni l'un ni l'autre n'est acquis quand l'écart
  certificat - valeur passe sous EPS = 1e-3 nat (la tolérance du nul v9), ou au bout de ITMAX pas, la partition est
  « indécise » : comptée NON promue pour le taux, et comptée à part (le taux « au pire » les compte promues) ;
- membres ordinaires et log-linéaires du nul v8 : omis dans les bras de base (comme le banc du concepteur) ; un bras
  « complet approché » ajoute les membres log-linéaires (chaque loi connue tempérée et inclinée, p(k) ~ S(k)^a exp(b_k),
  Newton, valeur + décrément au carré si <= 0,25, sinon 0 : règle de `nul_filles_v2._logit`), pour mesurer ce que
  l'omission change au gain annoncé.

Bras :
  v9      toutes les partitions à un niveau : une cellule, sous-population, toute coupe observée de chaque trait ;
  v9_par_membre  même classe que le v9, autre règle de lecture, que le concepteur n'a pas essayée : la carte est promue si
          CHAQUE famille du nul (une cellule ; sous-population ; un trait et un seuil réel) est dégagée à au moins un instant
          lu, pas forcément le même. Valide sur toute la classe du v9 par la même inégalité de Ville (si le monde est dans
          la famille F, « F dégagée à l'instant t » entraîne « rapport au monde >= 1/alpha à t ») ; jamais moins de
          promotions que le v9, monde pour monde (le v9 exige un même instant pour toutes les familles) ;
  La      une cellule + coupure de l'archive ; Ld : La + sous-population + signe de chaque trait ;
  grille  une cellule + sous-population + coupes aux neuf déciles du plan pour chaque trait ;
  ET      La et v9 promeuvent ; OU : La ou v9 au niveau alpha/2 ; mixte : 1/2 W_La + 1/2 W_v9 >= 1/alpha (encadré) ;
  A1      artefact : poids appris en ligne (descente exponentielle, pas 0,2, cellules de l'archive), lu aux instants ;
  A2      artefact : poids ajustés sur les 100 premiers tirages, valeur e sur les 100 suivants (lue à 200, et à 125..200) ;
  M11     poids ajustés sur N' tirages indépendants du même monde (autre plan), N' = 200 et 2 000, lu aux instants ;
  Mc2r    seuil simulé (grille de 17 points + projection de la carte), avec le rang exact de Monte-Carlo (cas à part).

Graines (R9) : numpy.random.SeedSequence(entropy=RACINE, spawn_key=(numéro du cas, numéro du lot)) ; un générateur par lot,
consommé dans l'ordre : archive, plan, paramètres du cas, tirages frais, puis tirages annexes. Écrites dans chaque sortie.

Usage :
  python attaque_libre_v1.py lot CAS LOT MONDES SORTIE.json        (un lot de mondes d'un cas)
  python attaque_libre_v1.py certificat SORTIE.json                 (certificat : le mien et celui du concepteur, contre
                                                                     un optimiseur indépendant)
  python attaque_libre_v1.py seuil CAS LOT MONDES SORTIE.json       (seuil simulé Mc2 : rang du concepteur et rang exact)
  python attaque_libre_v1.py differentiel CAS_DU_CONCEPTEUR R_DEBUT R_FIN SORTIE.json   (ses mondes, mes bras)
  python attaque_libre_v1.py fusion SORTIE.json LOT1.json LOT2.json ...
"""
import hashlib
import json
import math
import os
import platform
import sys
import time

import numpy as np

K, D, N, ALPHA = 3, 2, 200, 0.05
INSTANTS = np.arange(25, N + 1, 25)
LOG_SEUIL = math.log(1.0 / ALPHA)
EPS = 1e-3      # tolérance d'arrêt (TOLERANCE_GROUPE du nul v9)
ITMAX = 4000
RACINE = 2026111518
DECILES = np.arange(1, 10) / 10.0

CAS = {
    # --- taille, carte = copie exacte du monde (membre du nul) -----------------------------------------------------
    "C1": dict(no=1, genre="taille", J=3, classes=["v9", "La", "Ld", "grille"],
               texte="copie d'un membre intérieur : une cellule, poids Dirichlet(1) sur 3 lois connues et 3 lois certaines"),
    "C2": dict(no=2, genre="taille", J=3, classes=["v9", "La", "Ld", "grille"], texte="copie d'un sommet : S1 seule"),
    "C3": dict(no=3, genre="taille", J=3, classes=["v9", "La", "Ld", "grille"],
               texte="poids extrêmes, bord du simplexe : une cellule, poids Dirichlet(0,05)"),
    "C4": dict(no=4, genre="taille", J=6, classes=["v9", "La", "Ld", "grille"],
               texte="beaucoup de composantes : 6 lois connues et 3 lois certaines, une cellule, poids Dirichlet(1)"),
    "C5": dict(no=5, genre="taille", J=3, classes=["v9", "La", "Ld"],
               texte="copie par morceaux sur la coupure de l'archive : S1 d'un côté, S2 de l'autre"),
    "C6": dict(no=6, genre="taille", J=3, classes=["v9", "La", "Ld"],
               texte="membre par morceaux sur la coupure de l'archive : poids Dirichlet(1) par cellule, bruit aveugle commun"),
    "C7": dict(no=7, genre="taille", J=3, classes=["v9", "La", "Ld"],
               texte="petite cellule : copie par morceaux sur une coupure de l'archive placée à 1,5 à 2,0 écarts-types"),
    "C8": dict(no=8, genre="taille", J=3, classes=["v9", "Ld", "grille"],
               texte="copie par sous-population : S1 sur g = 0, S2 sur g = 1"),
    "C9": dict(no=9, genre="taille", J=3, classes=["v9", "Ld"], texte="copie au signe d'un trait : S1 si z_j > 0, S2 sinon"),
    "C10": dict(no=10, genre="taille", J=3, classes=["v9", "grille"],
                texte="copie par morceaux sur un décile du plan (coupe de la grille)"),
    "C11": dict(no=11, genre="taille", J=3, classes=["v9"],
                texte="copie par morceaux sur une coupure hors de l'archive (écart >= 0,3 sur le même trait)"),
    # --- taille, monde membre du nul, carte qui n'est PAS une copie --------------------------------------------------
    "N1a": dict(no=21, genre="taille", J=3, dose=0.15, classes=["v9", "La", "Ld", "grille"],
                texte="monde = S1 (sommet) ; carte = S1 plus une composante qui n'existe pas, dose 0,15"),
    "N1b": dict(no=22, genre="taille", J=3, dose=0.30, classes=["v9", "La", "Ld", "grille"],
                texte="monde = S1 (sommet) ; carte = S1 plus une composante qui n'existe pas, dose 0,30"),
    "N1c": dict(no=23, genre="taille", J=3, dose=0.50, classes=["v9", "La", "Ld", "grille"],
                texte="monde = S1 (sommet) ; carte = S1 plus une composante qui n'existe pas, dose 0,50"),
    "N2a": dict(no=24, genre="taille", J=3, dose=0.25, classes=["v9", "La", "Ld"],
                texte="monde = copie par morceaux sur la coupure de l'archive ; carte = la même, S1 décalée, dose 0,25"),
    "N2b": dict(no=25, genre="taille", J=3, dose=0.50, classes=["v9", "La", "Ld"],
                texte="monde = copie par morceaux sur la coupure de l'archive ; carte = la même, S1 décalée, dose 0,50"),
    "N3a": dict(no=26, genre="taille", J=3, dose=0.20, classes=["v9", "La", "Ld", "grille"],
                texte="monde = membre intérieur (une cellule) ; carte = le monde incliné selon les traits, dose 0,20"),
    "N3b": dict(no=27, genre="taille", J=3, dose=0.40, classes=["v9", "La", "Ld", "grille"],
                texte="monde = membre intérieur (une cellule) ; carte = le monde incliné selon les traits, dose 0,40"),
    "N4a": dict(no=28, genre="taille", J=3, marge=1.0, classes=["v9", "La", "Ld", "grille"],
                texte="monde = S1 (sommet) ; carte « tout ou rien » : S1 partout, sauf sur quelques-unes des 25 premières "
                      "instances où elle mise tout sur l'issue la plus probable, de sorte que le rapport de vraisemblance "
                      "au monde vaut au moins 20 au premier instant lu avec une probabilité proche de 1/20"),
    "N4b": dict(no=29, genre="taille", J=3, marge=2.0, classes=["v9", "La", "Ld", "grille"],
                texte="comme N4a, mais la mise vise un rapport d'au moins 40 (probabilité proche de 1/40)"),
    # --- puissance, monde hors de toutes les classes, carte = loi du monde -------------------------------------------
    "P1": dict(no=31, genre="puissance", J=3, dose=0.3, classes=[], texte="composante neuve globale, dose 0,3"),
    "P2": dict(no=32, genre="puissance", J=3, dose=0.5, classes=[], texte="composante neuve globale, dose 0,5"),
    "P3": dict(no=33, genre="puissance", J=3, dose=0.7, classes=[], texte="composante neuve globale, dose 0,7"),
    "P4": dict(no=34, genre="puissance", J=3, dose=0.7, classes=[],
               texte="composante neuve d'un seul côté de la coupure de l'archive (S1 de l'autre), dose 0,7"),
}


# ----------------------------------------------------------------------------------------------------------- outils
def clopper(k, n, niveau=0.95):
    from scipy.stats import beta
    a = (1 - niveau) / 2
    lo = 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))
    hi = 1.0 if k == n else float(beta.ppf(1 - a, k + 1, n - k))
    return [round(lo, 5), round(hi, 5)]


def taux(bits):
    b = np.asarray(bits, bool)
    return dict(promues=int(b.sum()), mondes=int(b.size), taux=round(float(b.mean()), 5), ic95=clopper(int(b.sum()), b.size))


def chaine(bits):
    return "".join("1" if x else "0" for x in np.asarray(bits, bool))


def empreinte_fichier(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


# ------------------------------------------------------------------------------------------------- mondes (par lots)
def softmax_alea(rng, W, nb):
    return np.round(rng.normal(0, 1.5, (W, nb, K, D)), 6), np.round(rng.normal(0, 0.3, (W, nb, K)), 6)


def p_softmax(Wt, b, z):
    """Wt (W, K, D), b (W, K), z (W, n, D) -> (W, n, K)."""
    s = np.einsum("wnd,wkd->wnk", z, Wt) + b[:, None, :]
    s = s - s.max(2, keepdims=True)
    e = np.exp(s)
    return e / e.sum(2, keepdims=True)


def tirer_archive(rng, W, J, petite_cellule=False):
    """J lois connues : J - 1 lois softmax (S1, S2, ...) et une loi si_sinon({z_jA > s_A}, U1, U2)."""
    Sw, Sb = softmax_alea(rng, W, J - 1)
    Uw, Ub = softmax_alea(rng, W, 2)
    jA = rng.integers(0, D, W)
    sA = np.empty(W)
    for w in range(W):
        while True:
            if petite_cellule:
                s = round(float(rng.choice([-1.0, 1.0]) * rng.uniform(1.5, 2.0)), 2)
            else:
                s = round(float(rng.uniform(-1, 1)), 2)
            if abs(s) >= 0.05:
                break
        sA[w] = s
    return dict(Sw=Sw, Sb=Sb, Uw=Uw, Ub=Ub, jA=jA, sA=sA)


def tirer_plan(rng, W, n=N):
    return np.round(rng.normal(size=(W, n, D)), 6), rng.integers(0, 2, (W, n))


def masque_archive(arch, z):
    return np.take_along_axis(z, arch["jA"][:, None, None], 2)[:, :, 0] > arch["sA"][:, None]


def lois_connues(arch, z):
    """(W, n, J, K) : S1, ..., S_{J-1}, puis la loi si_sinon de l'archive."""
    nb = arch["Sw"].shape[1]
    lois = [p_softmax(arch["Sw"][:, j], arch["Sb"][:, j], z) for j in range(nb)]
    m = masque_archive(arch, z)
    lois.append(np.where(m[:, :, None], p_softmax(arch["Uw"][:, 0], arch["Ub"][:, 0], z),
                         p_softmax(arch["Uw"][:, 1], arch["Ub"][:, 1], z)))
    return np.stack(lois, 2)


def tirer_issues(rng, P):
    u = rng.random(P.shape[:2])
    return np.minimum((u[:, :, None] > np.cumsum(P, 2)).sum(2), K - 1)


def composante_neuve(rng, W):
    Dl = rng.normal(size=(W, K, D))
    return Dl - Dl.mean(1, keepdims=True)


def monde_et_carte(cas, rng, arch, z, g, PL):
    """Rend (params, loi) : `loi(z, g, PL)` rend (P, Q) sur n'importe quel plan (W, n', D) — utile aux tirages indépendants."""
    W, J = PL.shape[0], PL.shape[2]
    c = CAS[cas]
    par = {}
    if cas in ("C1", "C3", "C4", "N3a", "N3b"):
        a = 0.05 if cas == "C3" else 1.0
        par["w"] = rng.dirichlet(np.full(J + K, a), W)
        if cas.startswith("N3"):
            par["v"] = composante_neuve(rng, W)
    elif cas == "C6":
        r = rng.uniform(0, 0.3, W)
        par["rho"] = rng.dirichlet(np.ones(K), W) * r[:, None]
        par["mu1"] = rng.dirichlet(np.ones(J), W) * (1 - r)[:, None]
        par["mu0"] = rng.dirichlet(np.ones(J), W) * (1 - r)[:, None]
    elif cas in ("C9", "C10", "C11"):
        par["j"] = rng.integers(0, D, W)
        if cas == "C9":
            par["s"] = np.zeros(W)
        elif cas == "C10":
            kq = rng.integers(0, 9, W)
            q = np.quantile(z, DECILES, axis=1)  # (9, W, D)
            par["s"] = q[kq, np.arange(W), par["j"]]
        else:
            s = np.empty(W)
            for w in range(W):
                while True:
                    v = round(float(rng.choice([-1.0, 1.0]) * rng.uniform(0.3, 1.0)), 2)
                    if par["j"][w] != arch["jA"][w] or abs(v - arch["sA"][w]) >= 0.3:
                        break
                s[w] = v
            par["s"] = s
    elif cas.startswith(("N1", "N2", "P")) and not cas.startswith("N4"):
        par["Dl"] = composante_neuve(rng, W)

    def loi(z2, g2, PL2):
        m = masque_archive(arch, z2)[:, :, None]
        if cas in ("C1", "C3", "C4"):
            P = np.einsum("wnjk,wj->wnk", PL2, par["w"][:, :J]) + par["w"][:, None, J:]
            Q = P
        elif cas == "C2":
            P = PL2[:, :, 0]
            Q = P
        elif cas in ("C5", "C7"):
            P = np.where(m, PL2[:, :, 0], PL2[:, :, 1])
            Q = P
        elif cas == "C6":
            P = np.where(m, np.einsum("wnjk,wj->wnk", PL2, par["mu1"]), np.einsum("wnjk,wj->wnk", PL2, par["mu0"])) \
                + par["rho"][:, None, :]
            Q = P
        elif cas == "C8":
            P = np.where((g2 == 1)[:, :, None], PL2[:, :, 1], PL2[:, :, 0])
            Q = P
        elif cas in ("C9", "C10", "C11"):
            zj = np.take_along_axis(z2, par["j"][:, None, None], 2)[:, :, 0]
            P = np.where((zj > par["s"][:, None])[:, :, None], PL2[:, :, 0], PL2[:, :, 1])
            Q = P
        elif cas.startswith("N1"):
            P = PL2[:, :, 0]
            Q = p_softmax(arch["Sw"][:, 0] + c["dose"] * par["Dl"], arch["Sb"][:, 0], z2)
        elif cas.startswith("N2"):
            P = np.where(m, PL2[:, :, 0], PL2[:, :, 1])
            Q = np.where(m, p_softmax(arch["Sw"][:, 0] + c["dose"] * par["Dl"], arch["Sb"][:, 0], z2), PL2[:, :, 1])
        elif cas.startswith("N4"):
            # carte tout ou rien, écrite d'après le plan (permis par l'hypothèse de gel : la carte et le plan sont fixés
            # avant les tirages ; un proposeur réel ne connaît pas le plan, c'est le pire cas de la borne de Ville)
            P = PL2[:, :, 0]
            Q = P.copy()
            t1 = int(INSTANTS[0])
            haut = P[:, :t1].max(2)
            ordre = np.argsort(-haut, 1)
            cp = np.cumprod(np.take_along_axis(haut, ordre, 1), 1)
            nb = (cp > 1.0 / (c["marge"] / ALPHA)).sum(1) + 1          # plus petit nombre de mises dont le produit <= alpha / marge
            for w_ in range(P.shape[0]):
                for s_ in ordre[w_, :min(nb[w_], t1)]:
                    k_ = int(P[w_, s_].argmax())
                    Q[w_, s_] = 1e-9 / (K - 1)
                    Q[w_, s_, k_] = 1.0 - 1e-9
        elif cas.startswith("N3"):
            P = np.einsum("wnjk,wj->wnk", PL2, par["w"][:, :J]) + par["w"][:, None, J:]
            inc = np.exp(c["dose"] * np.einsum("wnd,wkd->wnk", z2, par["v"]))
            Q = P * inc
            Q = Q / Q.sum(2, keepdims=True)
        elif cas in ("P1", "P2", "P3"):
            P = p_softmax(arch["Sw"][:, 0] + c["dose"] * par["Dl"], arch["Sb"][:, 0], z2)
            Q = P
        elif cas == "P4":
            P = np.where(m, p_softmax(arch["Sw"][:, 0] + c["dose"] * par["Dl"], arch["Sb"][:, 0], z2), PL2[:, :, 0])
            Q = P
        else:
            raise SystemExit(f"cas inconnu : {cas}")
        P = P / P.sum(2, keepdims=True)
        Q = Q / Q.sum(2, keepdims=True)
        return P, Q

    return par, loi


# ------------------------------------------------------------------------- maximum certifié d'un membre par morceaux
def em(A, y, m, tau, etat=None, eps=EPS, itmax=ITMAX, premier_bloque=False, pas_de_controle=5):
    """Montée par espérance-maximisation de f = somme_s log((1 - r) pi_{c(s)}.A_s + r beta_{y_s}), pour B problèmes à la fois.

    A : (B, t, J) ou (t, J) partagé ; y : (B, t) ou (t,) partagé ; m : (B, t) booléen (cellule 1 si vrai) ; tau : (B,).
    Rend F (meilleure valeur atteinte), UB (meilleur certificat = min sur les pas de min(0, f + écart de Frank-Wolfe)),
    statut (1 dégagé : UB <= tau ; 2 bloqué : F > tau ; 3 indécis), état final (r, beta, pi1, pi0).
    Le certificat vaut en tout point admissible : sup f <= f(x) + max_sommet grad f(x).v - t, les sommets étant « une loi
    connue par cellule, bruit nul » et « une loi certaine partout » (grad f(x).x = t par homogénéité)."""
    partage = A.ndim == 2
    B, t = m.shape
    J = A.shape[-1]
    Yb = np.eye(K)[y]  # (B, t, K) ou (t, K)
    if etat is None:
        r = np.full(B, 0.1)
        beta = np.full((B, K), 1.0 / K)
        p1 = np.full((B, J), 1.0 / J)
        p0 = np.full((B, J), 1.0 / J)
    else:
        r, beta, p1, p0 = (np.array(a, dtype=float) for a in etat)
        r = 0.95 * r + 0.05 * 0.1
        beta = 0.95 * beta + 0.05 / K
        p1 = 0.95 * p1 + 0.05 / J
        p0 = 0.95 * p0 + 0.05 / J
    F = np.full(B, -np.inf)
    UB = np.full(B, np.inf)
    statut = np.zeros(B, np.int8)
    act = np.arange(B)
    mf = m.astype(float)
    Aa, ya, Ya, ma = A, y, Yb, mf
    for it in range(itmax):
        ra, ba, a1, a0 = r[act], beta[act], p1[act], p0[act]
        if partage:
            k1, k0 = a1 @ Aa.T, a0 @ Aa.T
            blind = ba[:, ya]
        else:
            k1 = np.matmul(Aa, a1[:, :, None])[:, :, 0]
            k0 = np.matmul(Aa, a0[:, :, None])[:, :, 0]
            blind = np.take_along_axis(ba, ya, 1)
        p = (1 - ra)[:, None] * (ma * k1 + (1 - ma) * k0) + ra[:, None] * blind
        p = np.maximum(p, 1e-300)
        inv = 1.0 / p
        f = np.log(p).sum(1)
        if partage:
            g1, g0, gr = (ma * inv) @ Aa, ((1 - ma) * inv) @ Aa, inv @ Ya
        else:
            g1 = np.matmul((ma * inv)[:, None, :], Aa)[:, 0, :]
            g0 = np.matmul(((1 - ma) * inv)[:, None, :], Aa)[:, 0, :]
            gr = np.matmul(inv[:, None, :], Ya)[:, 0, :]
        ecart = np.maximum(np.maximum(gr.max(1), g1.max(1) + g0.max(1)) - t, 0.0)
        UB[act] = np.minimum(UB[act], np.minimum(f + ecart, 0.0))
        F[act] = np.maximum(F[act], f)
        # pas d'espérance-maximisation (mélange à deux étages : aveugle ou connue, puis composante)
        e1 = (1 - ra)[:, None] * a1 * g1
        e0 = (1 - ra)[:, None] * a0 * g0
        eb = ra[:, None] * ba * gr
        sb, s1, s0 = eb.sum(1), e1.sum(1), e0.sum(1)
        ra = np.clip(sb / t, 1e-12, 1 - 1e-12)
        ba = np.where(sb[:, None] > 0, eb / np.maximum(sb[:, None], 1e-300), ba)
        a1 = np.where(s1[:, None] > 0, e1 / np.maximum(s1[:, None], 1e-300), a1)
        a0 = np.where(s0[:, None] > 0, e0 / np.maximum(s0[:, None], 1e-300), a0)
        for a in (ba, a1, a0):
            a += 1e-12
            a /= a.sum(1, keepdims=True)
        r[act], beta[act], p1[act], p0[act] = ra, ba, a1, a0
        if it % pas_de_controle == 0 or it == itmax - 1:
            Fa, Ua, ta = F[act], UB[act], tau[act]
            dega, bloq = Ua <= ta, Fa > ta
            fin = (Ua - Fa) <= eps
            statut[act[dega]] = 1
            statut[act[bloq & ~dega]] = 2
            statut[act[fin & ~dega & ~bloq]] = 3
            if premier_bloque and bloq.any():
                break
            garde = ~(dega | bloq | fin)
            if not garde.any():
                act = act[:0]
                break
            if not garde.all():
                act = act[garde]
                ma = ma[garde]
                if not partage:
                    Aa, ya, Ya = Aa[garde], ya[garde], Ya[garde]
    statut[statut == 0] = 3
    return F, UB, statut, (r, beta, p1, p0)


def valeurs(A, y, m, eps=1e-4, itmax=20000):
    """Maximum certifié à eps près (aucun seuil) : rend (F, UB)."""
    B = m.shape[0]
    tau = np.full(B, np.nan)  # NaN : ni dégagé ni bloqué, seul l'écart arrête
    F, UB, _, _ = em(A, y, m, tau, eps=eps, itmax=itmax)
    return F, UB


class Partition:
    """Une partition nommée, évaluée sur un lot de mondes, instant par instant, seulement là où on en a besoin."""

    def __init__(self, nom, masque):
        self.nom, self.m = nom, masque
        W = masque.shape[0]
        self.statut = np.zeros((W, len(INSTANTS)), np.int8)  # 0 non évalué, 1 dégagé, 2 bloqué, 3 indécis
        self.F = np.full((W, len(INSTANTS)), np.nan)
        self.UB = np.full((W, len(INSTANTS)), np.nan)
        self.etats = [None] * len(INSTANTS)

    def evaluer(self, A, y, tau, besoin):
        etat = None
        W = self.m.shape[0]
        for i, t in enumerate(INSTANTS):
            w = np.flatnonzero(besoin[:, i])
            if not len(w):
                continue
            dep = None if etat is None else tuple(a[w] for a in etat)
            F, UB, st, fin = em(A[w, :t], y[w, :t], self.m[w, :t], tau[w, i], etat=dep)
            self.F[w, i], self.UB[w, i], self.statut[w, i] = F, UB, st
            if etat is None:
                J = A.shape[2]
                etat = (np.full(W, 0.1), np.full((W, K), 1.0 / K), np.full((W, J), 1.0 / J), np.full((W, J), 1.0 / J))
            for a, b in zip(etat, fin):
                a[w] = b
            self.etats[i] = tuple(a.copy() for a in etat)


def etat_nul(parts):
    """Par (monde, instant) : dégagé si toutes les partitions le sont ; bloqué si l'une l'est ; indécis sinon."""
    deg = np.all([p.statut == 1 for p in parts], 0)
    blo = np.any([p.statut == 2 for p in parts], 0)
    return deg, blo, ~deg & ~blo


def coupes(A, y, z, tau, etat_une_cellule, demande=None, premier_bloque=False):
    """Coupes observées des deux traits, pour un monde et un instant : A (t, J), y (t,), z (t, D). La coupe i du trait j
    met dans la cellule 0 les i + 1 plus petites valeurs de z_j (i = 0..t-2). `demande` : None (toutes les coupes) ou, par
    trait, un tableau booléen (t - 1,) des coupes à juger. Rend (statuts par trait : 0 non demandée, 1 dégagée, 2 bloquée,
    3 indécise ; nombre de coupes travaillées par montée)."""
    t, J = A.shape
    r, beta, p1, p0 = etat_une_cellule
    # certificat de premier ordre de chaque coupe au point « une cellule » (mêmes poids des deux côtés), par sommes cumulées
    p = np.maximum((1 - r) * (A @ p0) + r * beta[y], 1e-300)
    inv = 1.0 / p
    f0 = float(np.log(p).sum())
    gr = np.array([inv[y == k].sum() for k in range(K)])
    G = inv[:, None] * A
    tot = G.sum(0)
    statuts, masques, ou = [], [], []
    for j in range(D):
        o = np.argsort(z[:, j], kind="stable")
        zs = z[o, j]
        cum = np.cumsum(G[o], 0)[:-1]
        V = np.maximum(gr.max(), cum.max(1) + (tot[None, :] - cum).max(1))
        ub = np.minimum(0.0, f0 + np.maximum(V - t, 0.0))
        dem = np.ones(t - 1, bool) if demande is None else demande[j]
        s = np.zeros(t - 1, np.int8)
        s[dem & (ub <= tau)] = 1
        for i in np.flatnonzero(dem & (ub > tau)):
            masques.append(z[:, j] > zs[i])
            ou.append((j, i))
        statuts.append(s)
    if masques:
        M = np.array(masques)
        B = M.shape[0]
        dep = (np.full(B, r), np.tile(beta, (B, 1)), np.tile(p0, (B, 1)), np.tile(p0, (B, 1)))
        _, _, st, _ = em(A, y, M, np.full(B, tau), etat=dep, premier_bloque=premier_bloque)
        for (j, i), v in zip(ou, st):
            statuts[j][i] = v
    return statuts, len(masques)


def v9_un_monde(A, y, z, tau, etat_une_cellule):
    """Règle du v9 à un instant : toutes les coupes dégagées (1), l'une bloque (2), sinon indécis (3)."""
    statuts, nb = coupes(A, y, z, tau, etat_une_cellule, premier_bloque=True)
    tous = np.concatenate(statuts)
    if (tous == 2).any():
        return 2, nb
    return (1 if (tous == 1).all() else 3), nb


def par_membre(A, y, z, tau_w, etats, instants_degages):
    """Règle « membre par membre » sur la classe du v9, pour un monde : chaque famille (un trait, un seuil réel) doit être
    dégagée à AU MOINS UN instant lu, pas forcément le même pour toutes. Les seuils réels d'un trait se rangent en N + 1
    intervalles entre les valeurs du plan complet ; dans un intervalle, la partition induite sur les t premières instances
    ne change pas. Seuls comptent les instants où la partition « une cellule » est dégagée (elle est contenue dans toute
    famille : si elle bloque à t, toutes bloquent à t). Rend (promue, promue au pire, coupes travaillées)."""
    rangs = [np.argsort(np.argsort(z[:, j], kind="stable"), kind="stable") for j in range(D)]
    rem = [np.ones(N + 1, bool) for _ in range(D)]      # familles pas encore dégagées
    remp = [np.ones(N + 1, bool) for _ in range(D)]     # idem, en comptant une indécise comme dégagée
    nb_tot = 0
    for i in instants_degages[::-1]:
        t = int(INSTANTS[i])
        dem, cnts = [], []
        for j in range(D):
            cnt = np.searchsorted(np.sort(rangs[j][:t]), np.arange(N + 1), side="left")   # instances à gauche du seuil
            triv = (cnt == 0) | (cnt == t)              # la partition induite est « une cellule », dégagée à cet instant
            rem[j] &= ~triv
            remp[j] &= ~triv
            d = np.zeros(t - 1, bool)
            d[cnt[rem[j]] - 1] = True
            dem.append(d)
            cnts.append(cnt)
        if not any(d.any() for d in dem):
            break
        st, nb = coupes(A[:t], y[:t], z[:t], tau_w[i], etats[i], demande=dem)
        nb_tot += nb
        for j in range(D):
            k = np.flatnonzero(rem[j])
            s = st[j][cnts[j][k] - 1]
            rem[j][k[s == 1]] = False
            remp[j][k[(s == 1) | (s == 3)]] = False
    return (not any(x.any() for x in rem)), (not any(x.any() for x in remp)), nb_tot


# ------------------------------------------------------------------------------------- membres log-linéaires du v8
def log_lineaire(logS, y, itmax=60):
    """max sur (a, b_1, b_2) de somme_s log p(y_s), p(k) ~ S(k)^a exp(b_k), b_0 = 0 ; B problèmes à la fois.
    logS (B, t, K), y (B, t). Rend valeur + décrément de Newton au carré si celui-ci est <= 0,25, sinon 0."""
    B, t, _ = logS.shape
    X = np.zeros((B, t, K, K))                  # paramètres : a, b_1, ..., b_{K-1}
    X[:, :, :, 0] = logS
    for k in range(1, K):
        X[:, :, k, k] = 1.0
    th = np.zeros((B, K))
    th[:, 0] = 1.0
    idx = np.arange(t)[None, :]
    bb = np.arange(B)[:, None]

    def val(th):
        sc = np.einsum("btkp,bp->btk", X, th)
        mx = sc.max(2, keepdims=True)
        lse = mx[:, :, 0] + np.log(np.exp(sc - mx).sum(2))
        return (sc[bb, idx, y] - lse).sum(1), sc, mx

    f, sc, mx = val(th)
    dec = np.full(B, np.inf)
    for _ in range(itmax):
        pr = np.exp(sc - mx)
        pr /= pr.sum(2, keepdims=True)
        moy = np.einsum("btk,btkp->btp", pr, X)
        g = (X[bb, idx, y] - moy).sum(1)
        cen = X - moy[:, :, None, :]
        H = -np.einsum("btk,btkp,btkq->bpq", pr, cen, cen) - 1e-9 * np.eye(K)[None]
        pas = np.linalg.solve(H, -g[:, :, None])[:, :, 0]
        dec = np.maximum(0.0, (g * pas).sum(1))
        if dec.max() < 1e-12:
            break
        u = np.ones(B)
        for _ in range(30):
            essai = np.clip(th + u[:, None] * pas, -60, 60)
            f2, sc2, mx2 = val(essai)
            ok = (f2 >= f + 1e-4 * u * dec) | (f2 > f) | (dec < 1e-12)
            if ok.all():
                break
            u = np.where(ok, u, 0.5 * u)
        monte = f2 > f
        th = np.where(monte[:, None], essai, th)
        f, sc, mx = val(th)
    return np.where(dec <= 0.25, np.minimum(0.0, f + dec), 0.0)


# ----------------------------------------------------------------------------------------------- jugement d'un lot
def juger(A, y, z, g, m_arch, logq, PL=None):
    """Décisions des bras certifiés sur un lot : A (W, n, J) lois connues à l'issue observée, y (W, n), z (W, n, D),
    g (W, n), m_arch (W, n) cellule de la coupure de l'archive, logq (W, n) log-vraisemblance cumulée de la carte.
    PL (W, n, J, K), si donné : ajoute les bras « complets approchés » (membres log-linéaires du v8)."""
    W = A.shape[0]
    tau = logq[:, INSTANTS - 1] - LOG_SEUIL                # promue à t si D_t <= tau_t
    dec = np.quantile(z, DECILES, axis=1)                  # (9, W, D) : déciles du plan, connus avant les tirages
    tout = np.ones((W, len(INSTANTS)), bool)
    J = A.shape[2]

    une = Partition("une_cellule", np.zeros((W, N), bool))
    une.evaluer(A, y, tau, tout)
    parch = Partition("coupure_archive", m_arch)
    libre_ = lambda p_: (p_.statut == 1) | (p_.statut == 3)     # ni bloquée ni sautée : dégagée ou indécise
    parch.evaluer(A, y, tau, libre_(une))
    psous = Partition("sous_population", g == 1)
    psous.evaluer(A, y, tau, libre_(une))
    La = [une, parch]
    psig = [Partition(f"signe_z{j}", z[:, :, j] > 0) for j in range(D)]
    vivant = libre_(une) & libre_(parch) & libre_(psous)
    for p_ in psig:
        p_.evaluer(A, y, tau, vivant)
        vivant = vivant & libre_(p_)
    Ld = [une, parch, psous] + psig
    pdec = [Partition(f"decile_z{j}_{k + 1}", z[:, :, j] > dec[k, :, j][:, None]) for j in range(D) for k in range(9)]
    vivant = libre_(une) & libre_(psous)
    for p_ in pdec:
        p_.evaluer(A, y, tau, vivant)
        vivant = vivant & libre_(p_)
    grille = [une, psous] + pdec

    res = {}
    for nom, parts in (("La", La), ("Ld", Ld), ("grille", grille)):
        deg, blo, ind = etat_nul(parts)
        res[nom] = dict(promue=deg.any(1), au_pire=(deg | ind).any(1), instants_indecis=int(ind.sum()))

    # v9 : là où La et la sous-population sont dégagées (les partitions de La et la sous-population sont des partitions du v9)
    degLa, bloLa, indLa = etat_nul(La)
    pre_deg = degLa & (psous.statut == 1)                      # tout ce qui précède les coupes est dégagé
    pre_blo = bloLa | (psous.statut == 2) | (psous.statut == 0)
    st9 = np.where(pre_blo, 2, 0).astype(np.int8)
    coupes_travaillees = 0
    for w, i in zip(*np.nonzero(~pre_blo)):
        t = INSTANTS[i]
        e = tuple(a[w] for a in une.etats[i])
        s, nb = v9_un_monde(A[w, :t], y[w, :t], z[w, :t], tau[w, i], e)
        st9[w, i] = s if (pre_deg[w, i] or s == 2) else 3      # une partition indécise avant les coupes : indécis au mieux
        coupes_travaillees += nb
    deg9, ind9 = st9 == 1, st9 == 3
    res["v9"] = dict(promue=deg9.any(1), au_pire=(deg9 | ind9).any(1), instants_indecis=int(ind9.sum()))
    res["ET"] = dict(promue=res["La"]["promue"] & res["v9"]["promue"], au_pire=res["La"]["au_pire"] & res["v9"]["au_pire"],
                     instants_indecis=0)

    # règle « membre par membre » sur la classe du v9 (jamais essayée par le concepteur) : chaque famille dégagée à un
    # instant qui lui est propre. Toute promotion du v9 en est une ; on ne recalcule que les mondes que le v9 refuse.
    T1, T13 = une.statut == 1, libre_(une)
    sous1 = psous.statut == 1
    sous13 = libre_(psous)
    pm, pmp = res["v9"]["promue"].copy(), res["v9"]["au_pire"].copy()
    for w in np.flatnonzero(~res["v9"]["promue"] & (T13.sum(1) >= 2) & sous13.any(1)):
        etats_w = [None if e_ is None else tuple(a[w] for a in e_) for e_ in une.etats]
        pr, pi, nb = par_membre(A[w], y[w], z[w], tau[w], etats_w, np.flatnonzero(T1[w]))
        if (T13[w] & ~T1[w]).any():                            # « une cellule » indécise à un instant : au pire, on le compte
            _, pi, nb2 = par_membre(A[w], y[w], z[w], tau[w], etats_w, np.flatnonzero(T13[w]))
            nb += nb2
        pm[w] |= pr and bool(sous1[w].any())
        pmp[w] |= pi
        coupes_travaillees += nb
    res["v9_par_membre"] = dict(promue=pm, au_pire=pmp, instants_indecis=0)

    # contrôle de l'emboîtement, décision par décision : une promotion du v9 sans promotion de La, Ld ou grille est impossible
    emboitement = {k: int((res["v9"]["promue"] & ~res[k]["au_pire"]).sum()) for k in ("La", "Ld", "grille")}

    # bras « complet approché » : avec les membres log-linéaires du v8 (chaque loi connue tempérée et inclinée)
    if PL is not None:
        DlogJ = np.empty((W, len(INSTANTS), J))
        logPL = np.log(np.maximum(PL, 1e-12))
        for i, t in enumerate(INSTANTS):
            for j in range(J):
                DlogJ[:, i, j] = log_lineaire(logPL[:, :t, j, :], y[:, :t])
        libre = DlogJ.max(2) <= tau                         # aucun membre log-linéaire ne bloque à cet instant
        libre_membre = (DlogJ <= tau[:, :, None]).any(1).all(1)   # chaque membre log-linéaire dégagé à un instant à lui
        degLd, _, _ = etat_nul(Ld)
        degG, _, _ = etat_nul(grille)
        res["v8log_seul"] = dict(promue=((une.statut == 1) & libre).any(1))
        res["La_complet"] = dict(promue=(degLa & libre).any(1))
        res["Ld_complet"] = dict(promue=(degLd & libre).any(1))
        res["grille_complet"] = dict(promue=(degG & libre).any(1))
        res["v9_complet"] = dict(promue=(deg9 & libre).any(1))
        res["v9_par_membre_complet"] = dict(promue=pm & libre_membre)
    res["une_cellule_seule"] = dict(promue=(une.statut == 1).any(1))

    return res, dict(emboitement=emboitement, coupes=int(coupes_travaillees), instants_v9=int((~pre_blo).sum()))


# ------------------------------------------------------------------------------------------ les façons des fiches
def en_ligne(A, y, cel, eta=0.2):
    """argon-p2-01 : poids par cellule sur J lois connues et K lois certaines, départ uniforme, descente exponentielle.
    Rend log p cumulé du nul appris (W, n) ; la probabilité de l'épisode s n'emploie que les poids d'avant s."""
    W, n, J = A.shape
    w = np.full((W, 2, J + K), 1.0 / (J + K))
    ar = np.arange(W)
    cum = np.zeros(W)
    out = np.empty((W, n))
    E = np.eye(K)
    for s in range(n):
        c = cel[:, s]
        comp = np.concatenate([A[:, s, :], E[y[:, s]]], 1)
        wc = w[ar, c]
        p = np.maximum((wc * comp).sum(1), 1e-300)
        cum += np.log(p)
        out[:, s] = cum
        wc = wc * np.exp(np.minimum(eta * comp / p[:, None], 50.0))
        w[ar, c] = wc / wc.sum(1, keepdims=True)
    return out


def ajuster_par_cellule(G, cel, it=400):
    """Maximum de vraisemblance du mélange par cellule (poids séparés par cellule) : G (W, h, J + K), cel (W, h)."""
    W, h, q = G.shape
    w = np.full((W, 2, q), 1.0 / q)
    for c in (0, 1):
        mk = (cel == c).astype(float)
        cnt = mk.sum(1)
        v = w[:, c].copy()
        for _ in range(it):
            mm = np.maximum(np.matmul(G, v[:, :, None])[:, :, 0], 1e-300)
            gr = np.matmul((mk / mm)[:, None, :], G)[:, 0, :]
            v = v * gr / np.maximum(cnt, 1.0)[:, None]
            v = np.where(cnt[:, None] > 0, v / np.maximum(v.sum(1, keepdims=True), 1e-300), 1.0 / q)
        w[:, c] = v
    return w


def log_p_poids(w, G, cel):
    ar = np.arange(G.shape[0])[:, None]
    return np.log(np.maximum((w[ar, cel] * G).sum(2), 1e-300))


# ------------------------------------------------------------------------------------------------------------- lot
def un_lot(cas, lot, W, avec_complet=True):
    c = CAS[cas]
    J = c["J"]
    t0 = time.time()
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(c["no"], lot)))
    arch = tirer_archive(rng, W, J, petite_cellule=(cas == "C7"))
    z, g = tirer_plan(rng, W)
    PL = lois_connues(arch, z)
    par, loi = monde_et_carte(cas, rng, arch, z, g, PL)
    P, Q = loi(z, g, PL)
    y = tirer_issues(rng, P)
    ar = np.arange(W)[:, None]
    ns = np.arange(N)[None, :]
    A = PL[ar, ns, :, y]                                   # (W, n, J) : lois connues à l'issue observée
    lq = np.log(np.maximum(Q[ar, ns, y], 1e-300))
    logq = np.cumsum(lq, 1)
    lp = np.cumsum(np.log(np.maximum(P[ar, ns, y], 1e-300)), 1)
    m_arch = masque_archive(arch, z)
    res, diag = juger(A, y, z, g, m_arch, logq, PL if (avec_complet and c["genre"] == "puissance") else None)
    emboitement, coupes_travaillees, pre_deg_total = diag["emboitement"], diag["coupes"], diag["instants_v9"]

    # façons des fiches (artefact) : mêmes tirages, mêmes instants
    cel = m_arch.astype(int)
    lw1 = logq - en_ligne(A, y, cel)
    res["A1"] = dict(promue=(lw1[:, INSTANTS - 1] >= LOG_SEUIL).any(1))
    G = np.concatenate([A, np.eye(K)[y]], 2)
    h = N // 2
    wm = ajuster_par_cellule(G[:, :h], cel[:, :h])
    lw2 = np.cumsum(lq[:, h:] - log_p_poids(wm, G[:, h:], cel[:, h:]), 1)
    res["A2_fin"] = dict(promue=lw2[:, -1] >= LOG_SEUIL)
    res["A2_instants"] = dict(promue=(lw2[:, np.array([25, 50, 75, 100]) - 1] >= LOG_SEUIL).any(1))
    # méthode 11 : poids ajustés sur des tirages indépendants du même monde (autre plan), puis rapport simple
    if c["genre"] == "taille" and not cas.startswith("N"):
        for nprime in (200, 2000):
            z2, g2 = tirer_plan(rng, W, nprime)
            PL2 = lois_connues(arch, z2)
            P2, _ = loi(z2, g2, PL2)
            y2 = tirer_issues(rng, P2)
            A2 = PL2[ar, np.arange(nprime)[None, :], :, y2]
            G2 = np.concatenate([A2, np.eye(K)[y2]], 2)
            w11 = ajuster_par_cellule(G2, masque_archive(arch, z2).astype(int))
            lw11 = np.cumsum(lq - log_p_poids(w11, G, cel), 1)
            res[f"M11_{nprime}"] = dict(promue=(lw11[:, INSTANTS - 1] >= LOG_SEUIL).any(1))
    # borne de Ville elle-même : rapport de vraisemblance contre la loi du monde (aucun bras valide ne peut promouvoir plus)
    res["rapport_au_monde"] = dict(promue=((logq - lp)[:, INSTANTS - 1] >= LOG_SEUIL).any(1))

    # contrôle direct du pas de domination de la preuve (W_t <= rapport au monde à chaque instant) : pour un bras dont la
    # classe contient le monde, une promotion sans que le rapport au monde atteigne 1/alpha à un instant lu est impossible
    domination = {k: int((res[k]["au_pire"] & ~res["rapport_au_monde"]["promue"]).sum())
                  for k in ("v9", "La", "Ld", "grille") if k in c["classes"]}
    if "v9" in c["classes"]:
        domination["v9_par_membre"] = int((res["v9_par_membre"]["au_pire"] & ~res["rapport_au_monde"]["promue"]).sum())

    # méthodes 7 et 9 sur la copie hors archive : il faut la valeur de D_La, pas seulement la décision
    extra = {}
    if cas == "C11":
        DLa = np.full((W, len(INSTANTS)), -np.inf)
        for masque in (np.zeros((W, N), bool), m_arch):
            for i, t in enumerate(INSTANTS):
                _, UBv = valeurs(A[:, :t], y[:, :t], masque[:, :t])
                DLa[:, i] = np.maximum(DLa[:, i], UBv)
        lwLa = logq[:, INSTANTS - 1] - DLa
        mx = lwLa.max(1)
        # v9 : la carte est un membre de sa classe, donc W_v9 <= 1 à chaque instant (vérifié par le bras v9 ci-dessus)
        res["OU"] = dict(promue=(mx >= math.log(2 / ALPHA)) | res["v9"]["promue"])
        res["mixte_bas"] = dict(promue=mx >= math.log(2 / ALPHA))          # 1/2 W_La >= 1/alpha suffit
        res["mixte_haut"] = dict(promue=mx >= math.log(2 / ALPHA - 1.0))   # nécessaire si W_v9 <= 1
        extra["log_w_La_max_quantiles_0_50_95_100"] = [round(float(x), 4) for x in np.quantile(mx, [0, 0.5, 0.95, 1])]

    sortie = dict(
        version="attaque_libre_v1", mode="lot", cas=cas, numero_cas=c["no"], genre=c["genre"], description=c["texte"],
        classes_qui_contiennent_le_monde=c["classes"], lot=lot, mondes=W, lois_connues=J,
        graines=dict(racine=RACINE, derivation="numpy.random.SeedSequence(entropy=racine, spawn_key=(numero_cas, lot))",
                     spawn_key=[c["no"], lot]),
        niveau=dict(alpha=ALPHA, n=N, instants=INSTANTS.tolist(), seuil_log=LOG_SEUIL, tolerance=EPS, pas_max=ITMAX),
        bits={k: chaine(v["promue"]) for k, v in res.items()},
        bits_au_pire={k: chaine(v["au_pire"]) for k, v in res.items() if "au_pire" in v},
        instants_indecis={k: v["instants_indecis"] for k, v in res.items() if "instants_indecis" in v},
        emboitement_viole=emboitement, domination_violee=domination, coupes_v9_travaillees=int(coupes_travaillees),
        instants_v9_evalues=int(pre_deg_total), extra=extra,
        duree_s=round(time.time() - t0, 1), python=platform.python_version(), numpy=np.__version__)
    return sortie


# ------------------------------------------------------------------------------------------------------ certificat
def mode_certificat(sortie, R=400):
    """Sur R problèmes tirés au hasard (une cellule, coupure quelconque, 25 à 200 tirages, 3 ou 6 lois connues, poids du
    monde au bord ou à l'intérieur) : valeur de référence par un optimiseur indépendant (programmation quadratique
    séquentielle de scipy, six départs), comparée (a) à mon certificat après 3, 30 et 300 pas, (b) au certificat du
    concepteur (`essai_libre_commun_v1.em_certifie`, importé tel quel, jamais modifié). Un certificat sous la référence de
    plus de 1e-6 nat est une violation."""
    from scipy.optimize import minimize
    ici = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, ici)
    try:
        import essai_libre_commun_v1 as auteur
    except Exception as e:  # le programme du concepteur n'est pas à côté : la partie (b) est sautée, et dite
        auteur = None
        print("programme du concepteur introuvable :", e)
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(900, 0)))
    viol = {"moi_3": 0, "moi_30": 0, "moi_300": 0, "auteur": 0}
    marge = {k: np.inf for k in viol}
    n_auteur = 0
    for _ in range(R):
        J = int(rng.choice([3, 6]))
        t = int(rng.choice(INSTANTS))
        arch = tirer_archive(rng, 1, J)
        z, g = tirer_plan(rng, 1, t)
        PL = lois_connues(arch, z)
        a = float(rng.choice([0.05, 1.0]))
        w = rng.dirichlet(np.full(J + K, a))
        P = np.einsum("wnjk,j->wnk", PL, w[:J]) + w[None, None, J:]
        P = P / P.sum(2, keepdims=True)
        y = tirer_issues(rng, P)
        A = PL[0, np.arange(t), :, y[0]]
        jj = int(rng.integers(0, D))
        m = (z[0, :, jj] > np.quantile(z[0, :, jj], rng.uniform(0.05, 0.95))) if rng.random() < 0.8 else np.zeros(t, bool)
        q = 2 * J + K

        def negf(x):
            pp = np.where(m, A @ x[:J], A @ x[J:2 * J]) + x[2 * J:][y[0]]
            return -float(np.log(np.maximum(pp, 1e-300)).sum())

        cons = [{"type": "eq", "fun": lambda x: x[:J].sum() + x[2 * J:].sum() - 1.0},
                {"type": "eq", "fun": lambda x: x[J:2 * J].sum() + x[2 * J:].sum() - 1.0}]
        ref = -np.inf
        for _d in range(6):
            rr = rng.uniform(0.02, 0.6)
            x0 = np.concatenate([rng.dirichlet(np.ones(J)) * (1 - rr), rng.dirichlet(np.ones(J)) * (1 - rr),
                                 rng.dirichlet(np.ones(K)) * rr])
            o = minimize(negf, x0, method="SLSQP", bounds=[(0, 1)] * q, constraints=cons,
                         options={"maxiter": 400, "ftol": 1e-12})
            x = np.clip(o.x, 0, None)
            # remise exacte sur le polytope avant d'accepter la valeur (une valeur hors du polytope n'est pas une référence)
            rho = x[2 * J:]
            s1, s0 = x[:J].sum(), x[J:2 * J].sum()
            if rho.sum() <= 1 and s1 > 0 and s0 > 0:
                x[:J] *= (1 - rho.sum()) / s1
                x[J:2 * J] *= (1 - rho.sum()) / s0
                ref = max(ref, -negf(x))
        tau = np.array([np.nan])
        for pas in (3, 30, 300):
            F, UB, _, _ = em(A[None], y, m[None], tau, eps=-1.0, itmax=pas)
            d = float(UB[0] - ref)
            marge[f"moi_{pas}"] = min(marge[f"moi_{pas}"], d)
            viol[f"moi_{pas}"] += d < -1e-6
        if auteur is not None:
            UBa, Fa, _, _ = auteur.em_certifie(A, y[0], m[None])
            d = float(UBa[0] - ref)
            marge["auteur"] = min(marge["auteur"], d)
            viol["auteur"] += d < -1e-6
            n_auteur += 1
    out = dict(version="attaque_libre_v1", mode="certificat", problemes=R, problemes_compares_au_concepteur=n_auteur,
               graines=dict(racine=RACINE, spawn_key=[900, 0]),
               violations={k: int(v) for k, v in viol.items()},
               marge_minimale_nat={k: (None if not np.isfinite(v) else round(float(v), 6)) for k, v in marge.items()},
               note="marge = certificat - meilleure valeur de l'optimiseur indépendant ; une marge négative au-delà de "
                    "1e-6 nat est une violation",
               python=platform.python_version(), numpy=np.__version__)
    json.dump(out, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(out, ensure_ascii=False))


# ----------------------------------------------------------------------------------------- seuil simulé (méthode 5)
def mode_seuil(cas, lot, W, sortie, B=100):
    """Méthode 5 du concepteur (grille de 17 points de la classe La + projection de la carte ; statistique = richesse
    contre le nul appris en ligne ; seuil = plus grand quantile simulé), refaite par un programme à moi, avec DEUX règles
    de quantile sur les MÊMES simulations : celle du concepteur (numpy.quantile à 0,95 sur B = 100 simulations, qui
    tombe juste au-dessus de la 95e plus petite valeur) et le rang exact de Monte-Carlo (la 96e plus petite valeur sur
    100, soit ceil(0,95 x 101) : une statistique échangeable avec les simulations la dépasse ou l'égale avec une
    probabilité d'au plus 5/101).
    Cas : « T3 » monde du bord (copie, Dirichlet(0,1), comme le cas T3 du concepteur) ; « T1 » intérieur (copie) ;
    « F » monde = point de la classe La le plus proche de la carte au sens direct, somme_s KL(p_theta || q), la carte
    étant une vraie composante neuve (dose 0,5) : la projection du concepteur minimise l'autre sens, KL(q || p_theta)."""
    from scipy.optimize import minimize
    no = {"T3": 41, "T1": 42, "F": 43}[cas]
    t0 = time.time()
    J = 3
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(no, lot)))
    arch = tirer_archive(rng, W, J)
    z, g = tirer_plan(rng, W)
    PL = lois_connues(arch, z)
    m = masque_archive(arch, z)
    cel = m.astype(int)
    if cas in ("T3", "T1"):
        w = rng.dirichlet(np.full(J + K, 0.1 if cas == "T3" else 1.0), W)
        P = np.einsum("wnjk,wj->wnk", PL, w[:, :J]) + w[:, None, J:]
        P = P / P.sum(2, keepdims=True)
        Q = P
    else:
        Dl = composante_neuve(rng, W)
        Q = p_softmax(arch["Sw"][:, 0] + 0.5 * Dl, arch["Sb"][:, 0], z)
        P = np.empty_like(Q)
        for wi in range(W):  # projection directe : min sur la classe La (coupure de l'archive) de somme_s KL(p_theta || q)
            def kl(x, wi=wi):
                pp = np.where(m[wi][:, None], np.einsum("njk,j->nk", PL[wi], x[:J]), np.einsum("njk,j->nk", PL[wi], x[J:2 * J])) \
                    + x[2 * J:][None, :]
                pp = np.maximum(pp, 1e-300)
                return float((pp * (np.log(pp) - np.log(Q[wi]))).sum())
            cons = [{"type": "eq", "fun": lambda x: x[:J].sum() + x[2 * J:].sum() - 1.0},
                    {"type": "eq", "fun": lambda x: x[J:2 * J].sum() + x[2 * J:].sum() - 1.0}]
            x0 = np.concatenate([np.full(J, 0.9 / J), np.full(J, 0.9 / J), np.full(K, 0.1 / K)])
            o = minimize(kl, x0, method="SLSQP", bounds=[(0, 1)] * (2 * J + K), constraints=cons,
                         options={"maxiter": 200, "ftol": 1e-10})
            x = np.clip(o.x, 0, None)
            pp = np.where(m[wi][:, None], np.einsum("njk,j->nk", PL[wi], x[:J]), np.einsum("njk,j->nk", PL[wi], x[J:2 * J])) \
                + x[2 * J:][None, :]
            P[wi] = pp / pp.sum(1, keepdims=True)
    y = tirer_issues(rng, P)
    ar = np.arange(W)[:, None]
    ns = np.arange(N)[None, :]

    def stat(Y):
        """Statistique des fiches en ligne, pour des issues Y (W, n) : max aux instants de log q - log p appris."""
        Aq = PL[ar, ns, :, Y]
        lq = np.cumsum(np.log(np.maximum(Q[ar, ns, Y], 1e-300)), 1)
        return (lq - en_ligne(Aq, Y, cel))[:, INSTANTS - 1].max(1)

    s_obs = stat(y)
    # projection de la carte au sens du concepteur : max sur la classe La de somme_s somme_y q log p_theta (montée pondérée)
    def projection():
        meilleur = np.full(W, -np.inf)
        loi = np.empty_like(Q)
        for mm in (np.zeros_like(m), m):
            r = np.full(W, 0.5)
            beta = np.full((W, K), 1.0 / K)
            pi = np.full((W, 2, J), 1.0 / J)
            for _ in range(600):
                pc = np.where(mm[:, :, None], pi[:, 1][:, None, :], pi[:, 0][:, None, :])     # (W, n, J)
                known = np.einsum("wnjk,wnj->wnk", PL, pc)
                p = np.maximum((1 - r)[:, None, None] * known + (r[:, None] * beta)[:, None, :], 1e-300)
                wq = Q / p
                Aj = (1 - r)[:, None, None] * pc * np.einsum("wnjk,wnk->wnj", PL, wq)
                Bk = r[:, None] * beta * wq.sum(1)
                r = np.clip(Bk.sum(1) / N, 1e-10, 1 - 1e-10)
                beta = (Bk + 1e-12) / (Bk + 1e-12).sum(1, keepdims=True)
                for cc in (0, 1):
                    s = (Aj * (mm == bool(cc))[:, :, None]).sum(1)
                    ok = s.sum(1) > 0
                    pi[ok, cc] = (s[ok] + 1e-12) / (s[ok] + 1e-12).sum(1, keepdims=True)
            pc = np.where(mm[:, :, None], pi[:, 1][:, None, :], pi[:, 0][:, None, :])
            p = (1 - r)[:, None, None] * np.einsum("wnjk,wnj->wnk", PL, pc) + (r[:, None] * beta)[:, None, :]
            f = (Q * np.log(np.maximum(p, 1e-300))).sum((1, 2))
            mieux = f > meilleur
            meilleur = np.where(mieux, f, meilleur)
            loi[mieux] = (p / p.sum(2, keepdims=True))[mieux]
        return loi

    proj = projection()
    kl_proj = (Q * (np.log(np.maximum(Q, 1e-300)) - np.log(np.maximum(proj, 1e-300)))).sum((1, 2))
    pts = []
    for i in range(J):
        for j in range(J):
            pts.append(np.where(m[:, :, None], PL[:, :, i], PL[:, :, j]))
    for k in range(K):
        pts.append(np.broadcast_to(np.eye(K)[k], (W, N, K)).copy())
    pts.append(PL.mean(2) * 0.5 + 0.5 / K)
    for _ in range(4):
        rr = rng.uniform(0, 0.5, W)
        rho = rng.dirichlet(np.ones(K), W) * rr[:, None]
        mu1 = rng.dirichlet(np.ones(J), W) * (1 - rr)[:, None]
        mu0 = rng.dirichlet(np.ones(J), W) * (1 - rr)[:, None]
        pts.append(np.where(m[:, :, None], np.einsum("wnjk,wj->wnk", PL, mu1), np.einsum("wnjk,wj->wnk", PL, mu0)) + rho[:, None, :])
    pts.append(proj)
    q_np = np.empty((len(pts), W))
    q_ex = np.empty((len(pts), W))
    rang = math.ceil((1 - ALPHA) * (B + 1))       # 96 pour B = 100
    for ip, Pg in enumerate(pts):
        Pg = Pg / Pg.sum(2, keepdims=True)
        S = np.empty((B, W))
        for b in range(B):
            S[b] = stat(tirer_issues(rng, Pg))
        q_np[ip] = np.quantile(S, 1 - ALPHA, axis=0)
        q_ex[ip] = np.sort(S, 0)[rang - 1]
    bits = {
        "grille_et_projection_quantile_numpy": s_obs >= q_np.max(0),
        "grille_et_projection_rang_exact": s_obs >= q_ex.max(0),
        "projection_seule_quantile_numpy": s_obs >= q_np[-1],
        "projection_seule_rang_exact": s_obs >= q_ex[-1],
        "grille_seule_quantile_numpy": s_obs >= q_np[:-1].max(0),
        "grille_seule_rang_exact": s_obs >= q_ex[:-1].max(0),
    }
    out = dict(version="attaque_libre_v1", mode="seuil", cas=cas, numero_cas=no, lot=lot, mondes=W, simulations_par_point=B,
               points=len(pts), rang_exact=rang,
               graines=dict(racine=RACINE, spawn_key=[no, lot]),
               bits={k: chaine(v) for k, v in bits.items()},
               kl_carte_projection_quantiles_0_50_95_100=[round(float(x), 5) for x in np.quantile(kl_proj, [0, 0.5, 0.95, 1])],
               duree_s=round(time.time() - t0, 1), python=platform.python_version(), numpy=np.__version__)
    json.dump(out, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(cas, lot, {k: round(float(np.mean(v)), 4) for k, v in bits.items()}, out["duree_s"])


# ----------------------------------------------------------------------------------------------------- différentiel
def mode_differentiel(cas_auteur, r0, r1, sortie):
    """Mêmes mondes que le banc du concepteur (ses fonctions de tirage, importées telles quelles, jamais modifiées : cas
    `cas_auteur`, mondes r0..r1-1, graine SeedSequence(2026111501, (cas, r))), jugés par MES bras. Compare, monde pour
    monde, mes décisions aux bits publiés par le concepteur (tranches scellées, empreinte vérifiée avant lecture)."""
    ici = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, ici)
    import essai_libre_banc_v2 as banc
    import essai_libre_commun_v1 as commun
    t0 = time.time()
    W = r1 - r0
    As, ys, zs, gs, ms, lqs, PLs = [], [], [], [], [], [], []
    for r in range(r0, r1):
        rng = commun.rng_de(cas_auteur, r)
        Ar = commun.archive(rng)
        z, g = commun.plan(rng)
        PL = commun.lois_connues(Ar, z)
        P, _ = banc.monde_du_cas(cas_auteur, rng, Ar, z, g, PL)
        y = commun.tirer(rng, P)
        n = np.arange(N)
        As.append(PL[n, :, y]); ys.append(y); zs.append(z); gs.append(g); ms.append(z[:, Ar["jA"]] > Ar["sA"])
        lqs.append(np.cumsum(np.log(np.maximum(P[n, y], 1e-12)))); PLs.append(PL)
    A, y, z, g, m_arch, logq, PL = (np.array(v) for v in (As, ys, zs, gs, ms, lqs, PLs))
    res, diag = juger(A, y, z, g, m_arch, logq, PL if cas_auteur >= 7 else None)
    # bits publiés par le concepteur
    publies, lus = {}, []
    dossier = os.path.join(ici, "sorties")
    for a in range(0, 1000, 125):
        ch = os.path.join(dossier, f"sortie-banc-cas{cas_auteur}-{a}-{a + 125}-v2.json")
        if not os.path.exists(ch):
            continue
        if empreinte_fichier(ch) != open(ch + ".sha256").read().split()[0]:
            raise SystemExit(f"empreinte non conforme : {ch}")
        d = json.load(open(ch, encoding="utf-8"))
        lus.append(dict(fichier=os.path.basename(ch), sha256=empreinte_fichier(ch)))
        for b, v in d["bits"].items():
            publies.setdefault(b, {}).update({d["r_debut"] + i: x == "1" for i, x in enumerate(v)})
    comp = {}
    for b in ("La", "Ld", "grille", "v9"):
        if b not in publies or any(r not in publies[b] for r in range(r0, r1)):
            continue
        sien = np.array([publies[b][r] for r in range(r0, r1)])
        mien, pire = res[b]["promue"], res[b]["au_pire"]
        comp[b] = dict(promues_concepteur=int(sien.sum()), promues_refutateur=int(mien.sum()),
                       promues_refutateur_au_pire=int(pire.sum()),
                       promue_par_moi_seul=int((mien & ~sien).sum()), promue_par_lui_seul=int((sien & ~pire).sum()),
                       mondes_par_moi_seul=[int(r0 + i) for i in np.flatnonzero(mien & ~sien)][:50],
                       mondes_par_lui_seul=[int(r0 + i) for i in np.flatnonzero(sien & ~pire)][:50])
    out = dict(version="attaque_libre_v1", mode="differentiel", cas=f"auteur-{cas_auteur}", cas_auteur=cas_auteur, r_debut=r0,
               r_fin=r1, mondes=W, lot=r0 // max(W, 1),
               graines=dict(note="graines du concepteur : SeedSequence(entropy=2026111501, spawn_key=(cas, r))"),
               comparaison=comp, bits={k: chaine(v["promue"]) for k, v in res.items()},
               bits_au_pire={k: chaine(v["au_pire"]) for k, v in res.items() if "au_pire" in v},
               instants_indecis={k: v["instants_indecis"] for k, v in res.items() if "instants_indecis" in v},
               emboitement_viole=diag["emboitement"], tranches_lues=lus,
               duree_s=round(time.time() - t0, 1), python=platform.python_version(), numpy=np.__version__)
    json.dump(out, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(cas_auteur, r0, r1, {b: (v["promues_concepteur"], v["promues_refutateur"], v["promue_par_moi_seul"], v["promue_par_lui_seul"])
                               for b, v in comp.items()},
          {k: round(v.count("1") / W, 4) for k, v in out["bits"].items() if "complet" in k or k == "v8log_seul"}, out["duree_s"])


# ----------------------------------------------------------------------------------------------------------- fusion
def apparier(bits, n):
    app = {}
    for ref, autres in (("v9", ("v9_par_membre", "La", "Ld", "grille", "ET")),
                        ("v9_complet", ("v9_par_membre_complet", "La_complet", "Ld_complet", "grille_complet")),
                        ("v8log_seul", ("La_complet", "v9_complet", "v9_par_membre_complet"))):
        if ref not in bits:
            continue
        for b in autres:
            if b not in bits:
                continue
            gagne = sum(1 for u, v in zip(bits[b], bits[ref]) if u == "1" and v == "0")
            perd = sum(1 for u, v in zip(bits[b], bits[ref]) if u == "0" and v == "1")
            app[f"{b}_contre_{ref}"] = dict(promue_seulement_par_le_bras=gagne, promue_seulement_par_la_reference=perd,
                                            gain_apparie=round((gagne - perd) / n, 4))
    return app


def mode_fusion(sortie, fichiers):
    lots, seuils, diffs, certificat = {}, {}, {}, None
    liste = []
    for f in fichiers:
        d = json.load(open(f, encoding="utf-8"))
        liste.append(dict(fichier=os.path.basename(f), sha256=empreinte_fichier(f), mode=d["mode"], cas=d.get("cas"),
                          lot=d.get("lot"), mondes=d.get("mondes", d.get("problemes")), duree_s=d.get("duree_s")))
        if d["mode"] == "lot":
            lots.setdefault(d["cas"], []).append(d)
        elif d["mode"] == "seuil":
            seuils.setdefault(d["cas"], []).append(d)
        elif d["mode"] == "differentiel":
            diffs.setdefault(d["cas_auteur"], []).append(d)
        elif d["mode"] == "certificat":
            certificat = d
        else:
            raise SystemExit(f"mode inconnu dans {f}")
    cas_out = {}
    for cas, ds in sorted(lots.items(), key=lambda kv: CAS[kv[0]]["no"]):
        ds.sort(key=lambda d: d["lot"])
        if [d["lot"] for d in ds] != list(range(len(ds))):
            raise SystemExit(f"lots non contigus pour {cas}")
        bras = list(ds[0]["bits"])
        bits = {b: "".join(d["bits"][b] for d in ds) for b in bras}
        pire = {b: "".join(d["bits_au_pire"][b] for d in ds) for b in ds[0]["bits_au_pire"]}
        n = len(bits[bras[0]])
        classes = ds[0]["classes_qui_contiennent_le_monde"]
        e = dict(description=ds[0]["description"], genre=ds[0]["genre"], mondes=n, lots=len(ds),
                 classes_qui_contiennent_le_monde=classes,
                 graines=[d["graines"]["spawn_key"] for d in ds],
                 taux={b: taux([x == "1" for x in bits[b]]) for b in bras},
                 taux_au_pire={b: taux([x == "1" for x in pire[b]]) for b in pire},
                 instants_indecis={b: sum(d["instants_indecis"][b] for d in ds) for b in ds[0]["instants_indecis"]},
                 emboitement_viole={b: sum(d["emboitement_viole"][b] for d in ds) for b in ds[0]["emboitement_viole"]},
                 domination_violee={b: sum(d["domination_violee"][b] for d in ds) for b in ds[0]["domination_violee"]},
                 instants_v9_evalues=sum(d["instants_v9_evalues"] for d in ds),
                 coupes_v9_travaillees=sum(d["coupes_v9_travaillees"] for d in ds),
                 duree_s=round(sum(d["duree_s"] for d in ds), 1))
        if ds[0]["genre"] == "taille":
            # lecture de taille : pour un bras dont la classe contient le monde, la borne haute à 95 % du taux « au pire »
            # (indécis comptés promus) se compare au niveau du juge
            e["taille"] = {b: dict(borne_haute_ic95_au_pire=e["taux_au_pire"][b]["ic95"][1],
                                   sous_le_niveau=bool(e["taux_au_pire"][b]["ic95"][1] <= ALPHA))
                           for b in ("v9", "v9_par_membre", "La", "Ld", "grille", "ET")
                           if (b in classes or (b == "ET" and "La" in classes) or (b == "v9_par_membre" and "v9" in classes))}
        if any(d["extra"] for d in ds):
            e["extra_par_lot"] = [d["extra"] for d in ds]
        if ds[0]["genre"] == "puissance":
            e["apparie"] = apparier(bits, n)
        e["bits"], e["bits_au_pire"] = bits, pire
        cas_out[cas] = e
    seuil_out = {}
    for cas, ds in sorted(seuils.items()):
        ds.sort(key=lambda d: d["lot"])
        bits = {b: "".join(d["bits"][b] for d in ds) for b in ds[0]["bits"]}
        seuil_out[cas] = dict(mondes=len(next(iter(bits.values()))), lots=len(ds), simulations_par_point=ds[0]["simulations_par_point"],
                              rang_exact=ds[0]["rang_exact"], graines=[d["graines"]["spawn_key"] for d in ds],
                              taux={b: taux([x == "1" for x in v]) for b, v in bits.items()},
                              kl_carte_projection_quantiles_par_lot=[d["kl_carte_projection_quantiles_0_50_95_100"] for d in ds],
                              bits=bits)
    diff_out = {}
    for cas, ds in sorted(diffs.items()):
        ds.sort(key=lambda d: d["r_debut"])
        for u, v in zip(ds, ds[1:]):
            if u["r_fin"] != v["r_debut"]:
                raise SystemExit(f"tranches non contiguës (différentiel, cas {cas})")
        bits = {b: "".join(d["bits"][b] for d in ds) for b in ds[0]["bits"]}
        n = len(next(iter(bits.values())))
        comp = {}
        for b in ds[0]["comparaison"]:
            comp[b] = {k: sum(d["comparaison"][b][k] for d in ds) for k in
                       ("promues_concepteur", "promues_refutateur", "promues_refutateur_au_pire", "promue_par_moi_seul",
                        "promue_par_lui_seul")}
            comp[b]["mondes_par_moi_seul"] = sum((d["comparaison"][b]["mondes_par_moi_seul"] for d in ds), [])
            comp[b]["mondes_par_lui_seul"] = sum((d["comparaison"][b]["mondes_par_lui_seul"] for d in ds), [])
        e = dict(mondes=n, r=[ds[0]["r_debut"], ds[-1]["r_fin"]], comparaison=comp,
                 taux_refutateur={b: taux([x == "1" for x in v]) for b, v in bits.items()},
                 instants_indecis={b: sum(d["instants_indecis"][b] for d in ds) for b in ds[0]["instants_indecis"]},
                 emboitement_viole={b: sum(d["emboitement_viole"][b] for d in ds) for b in ds[0]["emboitement_viole"]},
                 tranches_du_concepteur=sum((d["tranches_lues"] for d in ds), []))
        if cas >= 7:
            e["apparie"] = apparier(bits, n)
        e["bits"] = bits
        diff_out[str(cas)] = e
    out = dict(version="attaque_libre_v1", mode="fusion", racine=RACINE,
               niveau=dict(alpha=ALPHA, n=N, instants=INSTANTS.tolist(), seuil_log=LOG_SEUIL, tolerance=EPS, pas_max=ITMAX),
               cas=cas_out, seuil_simule=seuil_out, differentiel_mondes_du_concepteur=diff_out, certificat=certificat,
               lots_lus=liste, python=platform.python_version(), numpy=np.__version__)
    json.dump(out, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for cas, e in cas_out.items():
        print(cas, e["mondes"], {b: v["taux"] for b, v in e["taux"].items()})
    for cas, e in seuil_out.items():
        print("seuil", cas, e["mondes"], {b: v["taux"] for b, v in e["taux"].items()})
    for cas, e in diff_out.items():
        print("différentiel", cas, e["mondes"], {b: (v["promues_concepteur"], v["promues_refutateur"], v["promue_par_moi_seul"],
                                                      v["promue_par_lui_seul"]) for b, v in e["comparaison"].items()})


def main():
    mode = sys.argv[1]
    if mode == "lot":
        cas, lot, W, sortie = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        d = un_lot(cas, lot, W)
        json.dump(d, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(cas, lot, W, {k: round(v.count("1") / W, 4) for k, v in d["bits"].items()}, "indécis", d["instants_indecis"],
              "emboîtement", d["emboitement_viole"], "domination", d["domination_violee"], d["duree_s"])
    elif mode == "certificat":
        mode_certificat(sys.argv[2])
    elif mode == "seuil":
        mode_seuil(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
    elif mode == "differentiel":
        mode_differentiel(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
    elif mode == "fusion":
        mode_fusion(sys.argv[2], sys.argv[3:])
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
