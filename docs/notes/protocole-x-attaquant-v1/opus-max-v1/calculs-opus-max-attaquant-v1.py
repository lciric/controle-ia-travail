#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la reponse independante d'Opus 5.5 (effort maximal) au protocole X « cote attaquant » (v1).

Mondes SUPPOSES, aucune donnee du programme. Lois exactes (blocs D, E, F, G, H) ou simulations
a graines derivees par numpy.random.SeedSequence (blocs A et B). Sortie : calculs-opus-max-attaquant-v1.txt

Blocs
  A  Boucle audit, recapture, reapprentissage (perceptron) contre un attaquant qui voit la sonde :
     borne E[episodes endommages manques] <= (R/gamma)^2 / (p q) ; marge qui se referme ; delai.
  B  Reapprentissage sous audit oriente par le score : naif, pondere par l'inverse de la probabilite
     d'audit, pondere aussi par le dommage ; leurres peu dommageables et tres visibles.
  D  Attaque choisie entre strates (enjeu, couverture de l'oracle) : trois repartitions du budget.
  E  Copies et delai de l'oracle : dommage avant l'alarme = tirage + rafale pendant le delai.
  F  Quota par lot contre tirage independant par episode : queue sans audit quand le quota est epuise.
  G  Relecture adaptative d'une famille tenue a l'ecart : gonflement du meilleur de k.
  H  Boucle attaque-defense sur une matrice de transfert : meilleure reponse a la derniere,
     engagement melange, jeu fictif ; valeur selon la generalisation de l'evasion g.
"""
import math
import platform
import sys
from statistics import NormalDist

import numpy as np

RACINE = 20261121  # graine racine declaree
SS = np.random.SeedSequence(RACINE)
NOMS = ["A_borne", "A_marge_qui_se_referme", "A_delai", "B_reapprentissage"]
GRAINES = dict(zip(NOMS, SS.spawn(len(NOMS))))
N01 = NormalDist()


def entete():
    print("Calculs opus-max attaquant v1")
    print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; {platform.platform()}")
    print(f"graine racine {RACINE} ; enfants SeedSequence : " +
          ", ".join(f"{k}={v.entropy}/{v.spawn_key}" for k, v in GRAINES.items()))
    print("Tous les chiffres sont SOUS SUPPOSITION D'ILLUSTRATION.\n")


# ---------------------------------------------------------------------------------------------
# Bloc A : perceptron a audits tires au hasard, attaquant qui connait la sonde a chaque instant
# ---------------------------------------------------------------------------------------------
def boucle_perceptron(gamma, p, q, T, reps, d, rng, delai=0, gamma_t=None):
    """Retourne le nombre d'episodes endommages manques par la sonde, par replique.

    Monde : u = e1 separe saboteur (u.x >= gamma) et honnete (u.x <= -gamma), ||x|| = 1 (R = 1).
    Attaquant : a chaque episode, voit la sonde W et place son sabotage sur la marge (u.x = gamma)
    du cote ou W le dit honnete (W.x <= 0) s'il le peut ; sinon il sabote quand meme et la sonde le voit.
    Defenseur : perceptron ; met a jour sur (i) un sabotage manque, audite (piece p) et reconnu (q),
    (ii) un honnete de reference mal classe (flux de reference, sans audit). Delai : les mises a jour
    venues des audits s'appliquent 'delai' episodes plus tard.
    """
    W = np.zeros((reps, d))
    manques = np.zeros(reps, dtype=np.int64)
    tampon = np.zeros((max(delai, 1), reps, d))
    for t in range(T):
        g = gamma if gamma_t is None else gamma_t(t)
        s = math.sqrt(1.0 - g * g)
        if delai > 0:
            k = t % delai
            W += tampon[k]
            tampon[k] = 0.0
        alpha = W[:, 0]
        perp = W.copy()
        perp[:, 0] = 0.0
        beta = np.linalg.norm(perp, axis=1)
        evite = (alpha * g - beta * s) <= 0.0
        v = np.zeros((reps, d))
        nz = beta > 0
        v[nz] = perp[nz] / beta[nz, None]
        v[~nz, 1] = 1.0
        x = -s * v
        x[:, 0] += g
        manques += evite
        revele = evite & (rng.random(reps) < p) & (rng.random(reps) < q)
        dx = np.where(revele[:, None], x, 0.0)
        z = rng.standard_normal((reps, d))
        z[:, 0] = 0.0
        z /= np.linalg.norm(z, axis=1, keepdims=True)
        xh = s * z
        xh[:, 0] -= g
        fp = np.einsum("ij,ij->i", W, xh) > 0.0
        dh = np.where(fp[:, None], -xh, 0.0)
        W += dh
        if delai > 0:
            tampon[t % delai] += dx
        else:
            W += dx
    return manques


def bloc_A():
    print("=== Bloc A — boucle audit, recapture, reapprentissage (perceptron), attaquant qui voit la sonde")
    print("Borne : E[manques] <= (R/gamma)^2 / (p q), R = 1 ; la borne ne suppose ni attaquant aveugle ni")
    print("canal de retour ferme sur les tirages passes : seulement une piece fraiche, secrete, et une marge.")
    d, reps, T = 8, 200, 20000
    rng = np.random.default_rng(GRAINES["A_borne"])
    print(f"d = {d} ; repliques = {reps} ; episodes par replique = {T}")
    print(f"{'gamma':>6} {'p':>6} {'q':>5} {'borne':>9} {'moyenne':>9} {'ecart-type':>10} {'max':>7} {'moy/borne':>9}")
    for gamma in (0.5, 0.25, 0.125):
        for (p, q) in ((0.1, 1.0), (0.03, 1.0), (0.03, 0.5)):
            m = boucle_perceptron(gamma, p, q, T, reps, d, rng)
            borne = 1.0 / (gamma * gamma * p * q)
            print(f"{gamma:6.3f} {p:6.3f} {q:5.2f} {borne:9.1f} {m.mean():9.1f} {m.std(ddof=1):10.1f} "
                  f"{m.max():7d} {m.mean()/borne:9.3f}")
    print()
    print("A2 — marge qui se referme : gamma_t = 0,5 / sqrt(1 + t/200) ; p = 0,1 ; q = 1")
    rng2 = np.random.default_rng(GRAINES["A_marge_qui_se_referme"])
    for T2 in (2000, 8000, 32000):
        m = boucle_perceptron(0.5, 0.1, 1.0, T2, 100, d, rng2, gamma_t=lambda t: 0.5 / math.sqrt(1 + t / 200))
        print(f"  episodes {T2:6d} : manques moyens {m.mean():9.1f} (part des episodes : {m.mean()/T2:.3f})")
    print("  lecture : la marge se refermant, les manques continuent de croitre et aucune borne en (R/gamma)^2")
    print("  ne tient ; que la croissance soit sans fin contre le pire attaquant vient de la theorie (dimension")
    print("  de Littlestone infinie des seuils), non de cette simulation, dont l'attaquant n'est pas le pire.")
    print()
    print("A3 — delai de l'oracle ou rafale des copies : gamma = 0,25 ; p = 0,1 ; q = 1 ; borne sans delai = 160")
    rng3 = np.random.default_rng(GRAINES["A_delai"])
    for D in (0, 10, 100, 1000):
        m = boucle_perceptron(0.25, 0.1, 1.0, 20000, 100, d, rng3, delai=D)
        print(f"  delai {D:5d} episodes : manques moyens {m.mean():9.1f} ; max {m.max():6d}")
    print("  lecture : le delai (debit des copies x delai de l'oracle) multiplie les manques ; la borne")
    print("  sans delai ne s'applique plus telle quelle.\n")


# ---------------------------------------------------------------------------------------------
# Bloc B : reapprentissage sous audit oriente par le score
# ---------------------------------------------------------------------------------------------
def bloc_B():
    print("=== Bloc B — reapprentissage d'une sonde par difference de moyennes, audit = plancher + tout signale")
    mu, s_sab, f, q = 2.5, 0.05, 0.05, 0.9
    rho_A, h_A, h_B = 0.7, 0.2, 1.0
    n, tours = 20000, 8
    tau = N01.inv_cdf(0.99)
    print(f"saboteur : type A (leurre, dommage {h_A}) part {rho_A} ; type B (dommage {h_B}) part {1-rho_A:.1f} ;")
    print(f"ecart lu {mu} ; plancher {f} ; oracle q = {q} ; seuil a 1 % de faux positifs ; {n} episodes par tour")
    rng = np.random.default_rng(GRAINES["B_reapprentissage"])

    def rappels(w):
        w = w / np.linalg.norm(w)
        rA = 1 - N01.cdf(tau - w[0] * mu)
        rB = 1 - N01.cdf(tau - w[1] * mu)
        return rA, rB

    methodes = ["naif", "inverse_proba", "inverse_proba_et_dommage", "plancher_seul"]
    W = {m: np.array([1.0, 0.0]) for m in methodes}
    acc = {m: [] for m in methodes}
    print(f"{'tour':>4} " + " ".join(f"{m:>27}" for m in methodes))
    for tr in range(tours + 1):
        ligne = []
        for m in methodes:
            rA, rB = rappels(W[m])
            dommage_manque = rho_A * h_A * (1 - rA) + (1 - rho_A) * h_B * (1 - rB)
            ligne.append(f"A {rA:.2f} B {rB:.2f} manque {dommage_manque:.3f}")
        print(f"{tr:4d} " + " ".join(f"{c:>27}" for c in ligne))
        if tr == tours:
            break
        sab = rng.random(n) < s_sab
        typeA = rng.random(n) < rho_A
        X = rng.standard_normal((n, 2))
        X[sab & typeA, 0] += mu
        X[sab & ~typeA, 1] += mu
        piece = rng.random(n) < f
        trouve = rng.random(n) < q
        for m in methodes:
            w = W[m] / np.linalg.norm(W[m])
            signale = (X @ w) > tau
            audite = piece | signale
            pi = np.where(signale, 1.0, f)
            pos = audite & sab & trouve
            if m == "plancher_seul":
                pos = piece & sab & trouve
            h = np.where(typeA, h_A, h_B)
            for i in np.flatnonzero(pos):
                acc[m].append((X[i], pi[i], h[i]))
            Xs = np.array([a[0] for a in acc[m]])
            pis = np.array([a[1] for a in acc[m]])
            hs = np.array([a[2] for a in acc[m]])
            if m == "naif" or m == "plancher_seul":
                poids = np.ones(len(Xs))
            elif m == "inverse_proba":
                poids = 1.0 / pis
            else:
                poids = hs / pis
            W[m] = (poids[:, None] * Xs).sum(0) / poids.sum()
    print("lecture : la sonde naive apprend ou elle a regarde (le leurre, signale donc audite) ; la")
    print("ponderation par l'inverse retrouve la population ; ponderee aussi par le dommage, elle vise le")
    print("type qui coute. Le plancher seul est sans biais mais plus lent (peu d'etiquettes).\n")


# ---------------------------------------------------------------------------------------------
# Bloc D : attaque choisie entre strates
# ---------------------------------------------------------------------------------------------
def bloc_D():
    print("=== Bloc D — attaque choisie : le saboteur prend la strate ou h / (pi q) est le plus grand")
    strates = [("frequente, petit enjeu, bien vue", 0.60, 1.0, 0.9),
               ("moyenne", 0.30, 3.0, 0.6),
               ("rare, gros enjeu, mal vue", 0.09, 10.0, 0.3),
               ("aveugle (q = 0)", 0.01, 5.0, 0.0)]
    B, f0 = 0.03, 0.005
    print(f"budget d'audit moyen {B}, dont un plancher {f0} sur toute strate ; strates (part, enjeu, couverture) :")
    for nom, w, h, qq in strates:
        print(f"  {nom:<34} part {w:.2f} enjeu {h:5.1f} q {qq:.1f}")

    def evalue(pis, nom):
        pires = []
        for (lab, w, h, qq), pi in zip(strates, pis):
            pires.append(math.inf if pi * qq == 0 else h / (pi * qq))
        vus = [x for x, st in zip(pires, strates) if st[3] > 0]
        print(f"  {nom:<44} pi = " + ", ".join(f"{x:.4f}" for x in pis) +
              f" ; pire dommage moyen avant prise (strates vues) {max(vus):8.1f} ; strate aveugle : non bornee")

    reste = B - f0  # budget au-dessus du plancher, reparti selon la regle
    evalue([B] * 4, "uniforme")
    tot = sum(st[1] * st[2] for st in strates)
    evalue([f0 + reste * st[2] / tot for st in strates], "plancher + part proportionnelle a l'enjeu")
    vus = [i for i, st in enumerate(strates) if st[3] > 0]
    lam = reste / sum(strates[i][1] * strates[i][2] / strates[i][3] for i in vus)
    pis = [f0 + (lam * st[2] / st[3] if st[3] > 0 else 0.0) for st in strates]
    evalue(pis, "plancher + part proportionnelle a h / q")
    print(f"  la strate aveugle garde le plancher {f0} (invariant d'audit) : il n'y garantit rien tant que q n'y")
    print("  est pas mesure par des dommages plantes ; il sert a le mesurer.")
    print("lecture : contre un saboteur qui choisit, le budget suit l'enjeu divise par la couverture ; une")
    print("strate a couverture nulle ou non mesuree n'a aucune garantie, quel que soit le budget.\n")


# ---------------------------------------------------------------------------------------------
# Bloc E : copies et delai
# ---------------------------------------------------------------------------------------------
def bloc_E():
    print("=== Bloc E — regime de signature : episodes endommages avant l'alarme = avant la prise + pendant le delai")
    p, q = 0.03, 0.8
    pq = p * q
    k95 = math.ceil(math.log(0.05) / math.log(1 - pq))
    print(f"p = {p} ; q = {q} ; avant la prise : moyenne {1/pq:.1f}, quantile 95 % {k95} episodes endommages")
    r = 2.0
    print(f"debit par copie {r} episodes par heure ; le saboteur sabote chaque episode des qu'il commence")
    print(f"{'copies':>7} {'delai (h)':>9} {'pendant le delai':>17} {'total 95 %':>11}")
    for m in (1, 10, 100, 1000):
        for dl in (1, 24, 168):
            burst = m * r * dl
            print(f"{m:7d} {dl:9d} {burst:17.0f} {k95 + burst:11.0f}")
    print("lecture : un seuil tolere K inferieur au debit x delai n'est garanti par aucun taux d'audit ;")
    print("seule la retenue des effets jusqu'a la verification (ou un plafond de simultaneite) le rend tenable.\n")


# ---------------------------------------------------------------------------------------------
# Bloc F : quota contre tirage independant
# ---------------------------------------------------------------------------------------------
def bloc_F():
    print("=== Bloc F — quota de k audits par lot de n, places au hasard, et agent qui sait le compte")
    print("queue sans audit apres le k-ieme audit : esperance (n - k)/(k + 1) ; tirage independant : nulle")
    for n in (100, 1000):
        for k in (1, 3, 10, 30):
            if k >= n:
                continue
            e = (n - k) / (k + 1)
            print(f"  n = {n:5d} k = {k:3d} : queue moyenne {e:7.1f} episodes ({e/n:.1%} du lot) a probabilite d'audit nulle")
    print("lecture : avec un retour qui laisse compter les audits, un quota viole le plancher ; un tirage")
    print("independant par episode ne laisse rien a compter (voir aussi Avenhaus et al., inspections epuisees).\n")


# ---------------------------------------------------------------------------------------------
# Bloc G : meilleur de k sur une famille tenue a l'ecart
# ---------------------------------------------------------------------------------------------
def lbinom_pmf(n, x, r):
    return (math.lgamma(n + 1) - math.lgamma(x + 1) - math.lgamma(n - x + 1)
            + x * math.log(r) + (n - x) * math.log(1 - r))


def esperance_max(n, k, r):
    pmf = [math.exp(lbinom_pmf(n, x, r)) for x in range(n + 1)]
    F, c = [], 0.0
    for v in pmf:
        c += v
        F.append(min(c, 1.0))
    e = 0.0
    prev = 0.0
    for x in range(n + 1):
        cur = F[x] ** k
        e += (x / n) * (cur - prev)
        prev = cur
    return e


def bloc_G():
    print("=== Bloc G — k defenses de meme rappel vrai r = 0,70 ; on garde la meilleure sur la famille tenue a l'ecart")
    r = 0.70
    print(f"{'n':>6} " + " ".join(f"{'k=' + str(k):>8}" for k in (1, 5, 20, 100)) + "   (gonflement en points)")
    for n in (50, 200, 1000):
        vals = [100 * (esperance_max(n, k, r) - r) for k in (1, 5, 20, 100)]
        print(f"{n:6d} " + " ".join(f"{v:8.2f}" for v in vals))
    print("lecture : chaque regard decisif de plus sur la meme famille gonfle le rappel lu ; une famille")
    print("neuve par cycle, lue une fois, est la seule mesure qui ne paie pas ce gonflement.\n")


# ---------------------------------------------------------------------------------------------
# Bloc H : boucle attaque-defense sur une matrice de transfert
# ---------------------------------------------------------------------------------------------
def bloc_H():
    print("=== Bloc H — K = 4 familles de moniteurs, 4 evasions ; D[i,j] = detection du moniteur i contre l'evasion j")
    K, dh, dl = 4, 0.8, 0.1
    print(f"D[i,i] = {dl} (evasion visee) ; D[i,j] = {dh} - ({dh} - {dl}) g pour i != j ; g = generalisation de l'evasion")
    for g in (0.0, 0.5, 0.9):
        D = np.full((K, K), dh - (dh - dl) * g)
        np.fill_diagonal(D, dl)
        V = (dl + (K - 1) * (dh - (dh - dl) * g)) / K
        # meilleure reponse a la derniere (l'attaquant joue en dernier)
        i, vals_br = 0, []
        for t in range(40):
            j = int(np.argmin(D[i]))
            vals_br.append(D[i, j])
            i = int(np.argmax(D[:, j]))
        # jeu fictif
        cA = np.zeros(K)
        cD = np.zeros(K)
        cD[0] = 1
        cA[0] = 1
        joues, garanties = [], {}
        for t in range(1, 2001):
            i = int(np.argmax(D @ (cA / cA.sum())))
            j = int(np.argmin((cD / cD.sum()) @ D))
            cD[i] += 1
            cA[j] += 1
            joues.append(D[i, j])
            if t in (10, 100, 1000, 2000):
                mixD = cD / cD.sum()
                garanties[t] = float(np.min(mixD @ D))
        print(f"  g = {g:.1f} : valeur a engagement melange (piece secrete) V = {V:.3f} ;"
              f" meilleure reponse a la derniere : {np.mean(vals_br):.3f} a chaque tour")
        print("          jeu fictif, garantie du melange empirique du defenseur : " +
              ", ".join(f"t={t} {v:.3f}" for t, v in garanties.items()) +
              f" ; valeur du dernier coup sur les 100 derniers tours : min {min(joues[-100:]):.2f} max {max(joues[-100:]):.2f}")
    print("lecture : (1) le dernier coup ne converge pas, la valeur du melange oui ; (2) la valeur a engagement")
    print("tend vers la detection de l'evasion visee quand g -> 1 : la diversite ne vaut que ce que la")
    print("generalisation de l'evasion lui laisse ; (3) le plancher d'audit s'ajoute a chaque tour sans convergence.\n")


if __name__ == "__main__":
    entete()
    bloc_A()
    bloc_B()
    bloc_D()
    bloc_E()
    bloc_F()
    bloc_G()
    bloc_H()
    print("fin")
