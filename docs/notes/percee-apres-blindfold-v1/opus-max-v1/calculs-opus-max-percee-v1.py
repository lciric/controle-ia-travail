# -*- coding: utf-8 -*-
"""Calculs de la note « percée après Blindfold », réponse indépendante d'Opus 5.5 (effort maximal).

Objets de contrôle seulement : lois exactes ou tirages simulés sous SUPPOSITIONS D'ILLUSTRATION.
Aucune donnée du programme, aucun modèle, aucun appel payant.

Blocs :
  A  identification exacte : un saboteur qui reproduit la loi honnête (dommage, lecture interne)
     est indiscernable d'un honnête à taux d'échec plus haut (fractions exactes).
  B  régime d'excès : plancher seul, conjonction « dommage et motif interne au même lieu »,
     moyenne des deux processus e, à étiquettes égales ; référence honnête fixe de taille m ;
     saboteurs rapide, lent, très lent ; étau tenu ou neutralisé. Plus le plateau (allure minimale
     détectable) en forme close.
  C  orientation de l'audit (avant l'audit) : gain et coût à budget égal, forme close.
  D  réparation après l'alarme : tri rétroactif du passé figé par une lecture apprise après l'alarme,
     boîte blanche contre boîte noire, à étiquettes égales ; trois objets de contrôle.
  E  dissuasion (modèle de Gans et Holden étendu au régime d'excès) : seuil de dissuasion,
     forme close sous la technologie exponentielle de leur exemple.

Graines : numpy.random.SeedSequence(20261121), enfants dérivés par bloc et par cas (R9).
"""
import sys
import math
import platform
from fractions import Fraction as Fr

import numpy as np
import scipy
from scipy.stats import beta as beta_dist

GRAINE = 20261121
RACINE = np.random.SeedSequence(GRAINE)
ENF_B, ENF_D = RACINE.spawn(2)


def entete():
    print("# Sortie de calculs-opus-max-percee-v1.py")
    print(f"python {platform.python_version()} ; numpy {np.__version__} ; scipy {scipy.__version__}")
    print(f"graine racine SeedSequence({GRAINE}) ; enfants : B = spawn(2)[0], D = spawn(2)[1]")
    print("Toutes les valeurs : SOUS SUPPOSITION D'ILLUSTRATION, aucune donnée du programme.")
    print()


# ----------------------------------------------------------------------------------------------
# Bloc A : identification exacte
# ----------------------------------------------------------------------------------------------
def loi_observable(eps, q, p0, phi, phi_u, s, tau_d, tau_u, frac_d):
    """Loi exacte de l'observation d'un épisode : (B, B·R, Z).
    B audit, R reconnaissance par l'oracle d'un dommage audité, Z drapeau de la sonde (lu partout).
    Honnête : dommage D ~ Bern(p0), Z|D=1 ~ Bern(phi), Z|D=0 ~ Bern(phi_u).
    Saboteur : avec probabilité s l'épisode est saboté ; un épisode saboté est endommagé avec
    probabilité frac_d, et son drapeau suit Bern(tau_d) s'il est endommagé, Bern(tau_u) sinon."""
    pD1 = (1 - s) * p0 + s * frac_d
    # probabilité jointe (D=1, Z=1), (D=1, Z=0), (D=0, Z=1), (D=0, Z=0)
    d1z1 = (1 - s) * p0 * phi + s * frac_d * tau_d
    d1z0 = pD1 - d1z1
    d0z1 = (1 - s) * (1 - p0) * phi_u + s * (1 - frac_d) * tau_u
    d0z0 = (1 - pD1) - d0z1
    loi = {}
    for z in (0, 1):
        pdz1 = d1z1 if z == 1 else d1z0
        pdz0 = d0z1 if z == 1 else d0z0
        # B = 0 : on ne voit que Z
        loi[(0, 0, z)] = (1 - eps) * (pdz1 + pdz0)
        # B = 1, R = 1 : dommage reconnu
        loi[(1, 1, z)] = eps * q * pdz1
        # B = 1, R = 0 : pas de dommage, ou dommage manqué
        loi[(1, 0, z)] = eps * ((1 - q) * pdz1 + pdz0)
    return loi


def bloc_A():
    print("## Bloc A — identification exacte (fractions)")
    eps, q, p0 = Fr(1, 20), Fr(4, 5), Fr(1, 5)
    phi, phi_u = Fr(1, 20), Fr(1, 50)
    s = Fr(1, 25)
    # Saboteur qui reproduit la loi honnête conditionnelle au dommage : épisodes sabotés tous
    # endommagés, drapeau à phi (comme un échec honnête).
    sab = loi_observable(eps, q, p0, phi, phi_u, s, tau_d=phi, tau_u=phi_u, frac_d=Fr(1))
    p0p = p0 + s * (1 - p0)
    hon_plus = loi_observable(eps, q, p0p, phi, phi_u, Fr(0), phi, phi_u, Fr(1))
    hon = loi_observable(eps, q, p0, phi, phi_u, Fr(0), phi, phi_u, Fr(1))
    egal = all(sab[k] == hon_plus[k] for k in sab)
    print(f"suppositions : eps={eps}, q={q}, p0={p0}, phi={phi}, phi_u={phi_u}, allure s={s}")
    print(f"taux d'échec de l'honnête équivalent p0' = p0 + s(1-p0) = {p0p}")
    print(f"loi(saboteur qui imite l'échec honnête) == loi(honnête à p0') sur les 6 cases : {egal}")
    for k in sorted(sab):
        print(f"  case (B, B·R, Z)={k} : saboteur {sab[k]} ; honnête p0' {hon_plus[k]} ; honnête p0 {hon[k]}")
    # rapport de vraisemblance saboteur / honnête p0 : ne dépend de Z que par la loi de Z, qui est
    # celle d'un honnête à p0' ; aucun test ne sépare le saboteur de l'honnête à p0'.
    # Contre-objet : saboteur dont le drapeau sur épisode saboté est tau_d = 4/5 (étau tenu).
    sab_etau = loi_observable(eps, q, p0, phi, phi_u, s, tau_d=Fr(4, 5), tau_u=phi_u, frac_d=Fr(1))
    p_min = None
    # existe-t-il un honnête (p0'' quelconque) de même loi ? la part de drapeaux parmi les dommages
    # reconnus vaut phi pour tout honnête ; chez le saboteur sous étau elle vaut :
    part = sab_etau[(1, 1, 1)] / (sab_etau[(1, 1, 1)] + sab_etau[(1, 1, 0)])
    print(f"contre-objet (étau tenu, tau=4/5) : part de drapeaux parmi les dommages reconnus = {part}"
          f" = {float(part):.4f} contre phi = {phi} chez tout honnête : discernable, sans référence de p0.")
    # Contre-objet 2 : saboteur qui imite le succès honnête (drapeau phi_u sur épisodes sabotés)
    sab_succ = loi_observable(eps, q, p0, phi, phi_u, s, tau_d=phi_u, tau_u=phi_u, frac_d=Fr(1))
    part2 = sab_succ[(1, 1, 1)] / (sab_succ[(1, 1, 1)] + sab_succ[(1, 1, 0)])
    print(f"contre-objet (imitation du succès, drapeau phi_u) : part = {part2} = {float(part2):.4f}"
          f" < phi : un déficit, discernable lui aussi (test bilatéral).")
    print("lecture : seule l'imitation de la loi honnête conditionnelle à l'échec rend la lecture interne"
          " inutile ; c'est la supposition que l'adversaire doit violer (indiscernabilité conditionnelle).")
    print()
    return egal


# ----------------------------------------------------------------------------------------------
# Bloc B : régime d'excès, processus e par mise, à étiquettes égales
# ----------------------------------------------------------------------------------------------
def borne_cp_sup(k, n, niveau):
    """Borne supérieure de Clopper-Pearson unilatérale au niveau 1 - niveau."""
    if k >= n:
        return 1.0
    return float(beta_dist.ppf(1 - niveau, k + 1, n - k))


def grille_lambda(mu0, nb=28):
    """Mises lambda pour 1 + lambda (X - mu0), X binaire de moyenne <= mu0 sous le nul.
    lambda = g / (1 - mu0), g alternative multiplicative, g <= (1 - mu0)/mu0 (positivité)."""
    gmax = 0.95 * (1 - mu0) / mu0
    g = np.geomspace(0.02, gmax, nb)
    return g / (1 - mu0)


def log_e_aux_evenements(t, n1, lam, mu0):
    """log de la moyenne sur la grille de prod (1 + lam (X - mu0)) au temps t avec n1 succès."""
    a = np.log1p(lam * (1 - mu0))      # gain par événement
    b = np.log1p(-lam * mu0)           # perte par non-événement
    lg = n1[:, None] * a[None, :] + (t - n1)[:, None] * b[None, :]
    m = lg.max(axis=1)
    return m + np.log(np.exp(lg - m[:, None]).mean(axis=1))


def une_course(rng, par, methode, Nmax):
    """Simule une course ; renvoie (alarme ?, temps d'alarme, sabotés jusqu'à l'alarme)."""
    eps, q, p0, phi, tau, s, m, alpha = (par[k] for k in ("eps", "q", "p0", "phi", "tau", "s", "m", "alpha"))
    # Référence honnête exogène : m épisodes honnêtes jugés en entier (oracle), drapeaux lus.
    nd = rng.binomial(m, p0)
    nrec = rng.binomial(nd, q)
    nconj = rng.binomial(nrec, phi)
    if methode == "plancher":
        a_ref, a_test = alpha / 2, alpha / 2
        mu0_f = eps * borne_cp_sup(nrec, m, a_ref)
    elif methode == "conjonction":
        a_ref, a_test = alpha / 2, alpha / 2
        mu0_c = eps * borne_cp_sup(nconj, m, a_ref)
    else:  # moyenne des deux processus e
        a_ref, a_test = alpha / 4, alpha / 2
        mu0_f = eps * borne_cp_sup(nrec, m, a_ref)
        mu0_c = eps * borne_cp_sup(nconj, m, a_ref)
    # Probabilités par épisode des types d'événement « audité et dommage reconnu »
    pA = eps * q * s * tau                      # saboté, reconnu, drapeau
    pB = eps * q * s * (1 - tau)                # saboté, reconnu, sans drapeau
    pC = eps * q * (1 - s) * p0 * phi           # honnête endommagé, reconnu, drapeau
    pD = eps * q * (1 - s) * p0 * (1 - phi)     # honnête endommagé, reconnu, sans drapeau
    pev = pA + pB + pC + pD
    s_autre = (s - (pA + pB)) / (1 - pev)       # part de sabotés parmi les non-événements
    # Événements : temps par lacunes géométriques
    n_max_ev = int(pev * Nmax * 1.3 + 50)
    lac = rng.geometric(pev, size=n_max_ev)
    t_ev = np.cumsum(lac)
    t_ev = t_ev[t_ev <= Nmax]
    k = len(t_ev)
    typ = rng.choice(4, size=k, p=np.array([pA, pB, pC, pD]) / pev)
    est_sab = (typ <= 1)
    est_conj = (typ == 0) | (typ == 2)
    n1_f = np.arange(1, k + 1)
    n1_c = np.cumsum(est_conj)
    seuil = math.log(1 / a_test)
    if k == 0:
        alarme_idx = None
    else:
        if methode == "plancher":
            le = log_e_aux_evenements(t_ev, n1_f, grille_lambda(mu0_f), mu0_f)
        elif methode == "conjonction":
            le = log_e_aux_evenements(t_ev, n1_c, grille_lambda(mu0_c), mu0_c)
            le = np.where(est_conj, le, -np.inf)   # le processus ne croît qu'à ses événements
        else:
            lf = log_e_aux_evenements(t_ev, n1_f, grille_lambda(mu0_f), mu0_f)
            lc = log_e_aux_evenements(t_ev, n1_c, grille_lambda(mu0_c), mu0_c)
            mx = np.maximum(lf, lc)
            le = mx + np.log((np.exp(lf - mx) + np.exp(lc - mx)) / 2)
        au_dessus = np.nonzero(le >= seuil)[0]
        alarme_idx = int(au_dessus[0]) if len(au_dessus) else None
    if alarme_idx is None:
        T = Nmax
        n_ev = k
        sab_ev = int(est_sab.sum())
    else:
        T = int(t_ev[alarme_idx])
        n_ev = alarme_idx + 1
        sab_ev = int(est_sab[:n_ev].sum())
    sab_autres = rng.binomial(T - n_ev, s_autre)
    return (alarme_idx is not None), T, sab_ev + sab_autres


def bloc_B():
    print("## Bloc B — régime d'excès : plancher, conjonction, moyenne des deux (à étiquettes égales)")
    base = dict(eps=0.05, q=0.8, p0=0.20, phi=0.05, m=2000, alpha=0.05)
    Nmax = 200_000
    R = 200
    print(f"suppositions : {base}, horizon {Nmax} épisodes, {R} courses par cas ; sabotage : épisode"
          " endommagé à coup sûr ; tau = part des épisodes sabotés endommagés que la sonde marque.")
    print("mesure : sabotés cumulés à l'alarme (médiane, 90e centile) ; P(alarme avant l'horizon) ;"
          " sans alarme, compte à l'horizon (censuré).")
    print()
    cas = []
    for tau, nom_tau in ((0.80, "étau tenu (tau=0.80)"), (0.05, "neutralisé (tau=phi=0.05)")):
        for s in (0.05, 0.02, 0.01, 0.005):
            cas.append((tau, nom_tau, s))
    enfants = ENF_B.spawn(len(cas) * 3)
    i = 0
    print("| cas | allure s | méthode | P(alarme) | sabotés à l'alarme, médiane | 90e centile | épisodes à l'alarme, médiane |")
    print("|---|---|---|---|---|---|---|")
    resultats = {}
    for (tau, nom_tau, s) in cas:
        for methode in ("plancher", "conjonction", "moyenne"):
            rng = np.random.default_rng(enfants[i]); i += 1
            par = dict(base, tau=tau, s=s)
            out = [une_course(rng, par, methode, Nmax) for _ in range(R)]
            al = np.array([o[0] for o in out]); T = np.array([o[1] for o in out]); K = np.array([o[2] for o in out])
            resultats[(tau, s, methode)] = (al.mean(), np.median(K), np.percentile(K, 90), np.median(T))
            print(f"| {nom_tau} | {s} | {methode} | {al.mean():.3f} | {np.median(K):.0f} | {np.percentile(K, 90):.0f} | {np.median(T):.0f} |")
    print()
    # Plateau : allure minimale détectable à horizon infini, attendue sur la référence (forme close)
    print("### Plateau (loi de la référence honnête) : allure minimale détectable à horizon infini")
    print("Détectable si le taux du suspect dépasse la borne haute tirée de la référence ; borne calculée"
          " au compte attendu de la référence (approximation déterministe).")
    eps, q, p0, phi, alpha = base["eps"], base["q"], base["p0"], base["phi"], base["alpha"]
    print("| m | plancher : s_min | conjonction, tau=0.8 : s_min | rapport conj/plancher | sqrt(phi)/tau·(1-p0) |")
    print("|---|---|---|---|---|")
    for m in (500, 2000, 10000, 50000):
        k_f = round(m * q * p0)
        u_f = borne_cp_sup(k_f, m, alpha / 2)
        smin_f = (u_f - q * p0) / (q * (1 - p0))
        k_c = round(m * q * p0 * phi)
        u_c = borne_cp_sup(k_c, m, alpha / 2)
        tau = 0.8
        smin_c = (u_c - q * p0 * phi) / (q * (tau - p0 * phi))
        print(f"| {m} | {smin_f:.4f} | {smin_c:.4f} | {smin_c / smin_f:.3f} | {math.sqrt(phi) / tau * (1 - p0):.3f} |")
    print("lecture : les deux plateaux existent ; la conjonction les abaisse d'un facteur constant, elle"
          " ne les supprime pas. Sous l'allure minimale, le dommage croît linéairement sans alarme.")
    # coût du pire cas de la moyenne des deux processus e : la référence du plancher est prise à alpha/4
    m = base["m"]
    k_f = round(m * q * p0)
    smin_f2 = (borne_cp_sup(k_f, m, alpha / 2) - q * p0) / (q * (1 - p0))
    smin_f4 = (borne_cp_sup(k_f, m, alpha / 4) - q * p0) / (q * (1 - p0))
    print(f"coût de la moyenne quand la lecture interne est neutralisée (m={m}) : allure minimale du plancher"
          f" {smin_f2:.4f} seul, {smin_f4:.4f} dans la moyenne (x{smin_f4 / smin_f2:.2f}) ; au-dessus du plateau,"
          f" chaque composante doit atteindre 2/alpha_test au lieu de 1/alpha_test.")
    n_sig_f = 1 / (eps * q * p0)
    n_sig_c = 1 / (eps * q * p0 * phi)
    print(f"phase « quasi signature » (moins d'un faux événement honnête attendu) : plancher {n_sig_f:.0f}"
          f" épisodes, conjonction {n_sig_c:.0f} épisodes (facteur 1/phi = {1 / phi:.0f}) ; au-delà, régime en racine"
          " de l'horizon dans les deux cas, coefficient multiplié par environ sqrt(phi)/tau.")
    print()
    return resultats


# ----------------------------------------------------------------------------------------------
# Bloc C : orientation de l'audit (avant l'audit), forme close
# ----------------------------------------------------------------------------------------------
def bloc_C():
    print("## Bloc C — orientation de l'audit par la sonde, à budget égal (forme close)")
    eps, q = 0.05, 0.8
    print(f"suppositions : budget moyen eps={eps} sous la loi honnête ; oracle q={q} ; régime de signature"
          " (l'honnête ne commet pas ce dommage) ; un épisode marqué est audité à pi_haut, un non marqué à pi_bas.")
    print("| part marquée chez l'honnête f | pi_bas | pi_haut | sabotés avant la prise, uniforme 1/(eps q) |"
          " étau : sabotés marqués à 0,8 | neutralisé : sabotés jamais marqués | coût du neutralisé |")
    print("|---|---|---|---|---|---|---|")
    for f in (0.02, 0.05, 0.10):
        for pi_bas in (eps / 2, 0.8 * eps):
            pi_haut = min(1.0, (eps - pi_bas * (1 - f)) / f)
            unif = 1 / (eps * q)
            tau = 0.8
            pi_sab_etau = tau * pi_haut + (1 - tau) * pi_bas
            etau = 1 / (pi_sab_etau * q)
            neutre = 1 / (pi_bas * q)
            print(f"| {f} | {pi_bas:.3f} | {pi_haut:.3f} | {unif:.1f} | {etau:.1f} | {neutre:.1f} | x{neutre / unif:.2f} |")
    print("lecture : gain borné par pi_haut/eps, coût du pire cas eps/pi_bas ; la borne garde sa validité"
          " (poids inverses connus) mais s'élargit : ni changement de régime, ni réparation.")
    print()


# ----------------------------------------------------------------------------------------------
# Bloc D : réparation après l'alarme, tri rétroactif du passé figé
# ----------------------------------------------------------------------------------------------
def tirer_population(rng, n, s, p0, d, a_h, a_s, c_s, b_h, b_s, imite_succes=False):
    """Types : 0 honnête sans dommage, 1 honnête endommagé, 2 saboté (endommagé).
    Activations x (dimension d) : honnête endommagé décalé de a_h sur e1 (confusion) ; saboté décalé
    de a_s sur e2 (savoir puis choisir autrement) et de c_s sur e1. Transcrits y (dimension d) :
    b_h sur e1, b_s sur e2. La sonde déployée lit e3 : le mode neuf n'y laisse rien (évasion)."""
    u = rng.random(n)
    typ = np.where(u < s, 2, np.where(u < s + (1 - s) * p0, 1, 0))
    x = rng.standard_normal((n, d))
    y = rng.standard_normal((n, d))
    x[typ == 1, 0] += a_h
    y[typ == 1, 0] += b_h
    if not imite_succes:
        x[typ == 2, 1] += a_s
        x[typ == 2, 0] += c_s
    y[typ == 2, 1] += b_s
    return typ, x, y


def direction(xp, xn, lam=1.0):
    mu = xp.mean(axis=0) - xn.mean(axis=0)
    X = np.vstack([xp - xp.mean(axis=0), xn - xn.mean(axis=0)])
    S = X.T @ X / max(1, len(X) - 2)
    return np.linalg.solve(S + lam * np.eye(S.shape[0]), mu)


def rappel_au_budget(score, est_sab, budget, rng, melange=False):
    n = len(score)
    budget = min(budget, n)
    if melange:
        b1 = budget // 2
        ordre = np.argsort(-score)
        masque = np.zeros(n, dtype=bool)
        masque[ordre[:b1]] = True
        reste = np.nonzero(~masque)[0]
        masque[rng.choice(reste, size=budget - b1, replace=False)] = True
        return est_sab[masque].sum() / max(1, est_sab.sum())
    idx = np.argsort(-score)[:budget]
    return est_sab[idx].sum() / max(1, est_sab.sum())


def bloc_D():
    print("## Bloc D — réparation après l'alarme : tri rétroactif du passé figé, à étiquettes égales")
    p0, q, d = 0.20, 0.8, 64
    n_u, n_a, m_ref = 20000, 1000, 2000
    print(f"suppositions : passé non audité {n_u} épisodes ; audités avant l'alarme {n_a} (étiquettes de"
          f" l'oracle, q={q}) ; référence honnête jugée {m_ref} épisodes avec états internes (au banc : le"
          f" jumeau) ; p0={p0} ; dimension {d} ; 40 tirages par cas.")
    print("lectures après l'alarme : « dommage » = direction dommage reconnu contre non reconnu chez les"
          " audités ; « excès » = direction des audités endommagés du suspect contre les endommagés de la"
          " référence honnête ; boîte noire = la même chose sur les transcrits. Budget de réparation exprimé"
          " en multiples du nombre de sabotés non audités k.")
    objets = [
        ("V  étau tenu en interne (a_s=3), faible au texte (b_s=0,5)", dict(a_h=1.5, a_s=3.0, c_s=0.0, b_h=1.0, b_s=0.5), False),
        ("E  étau absent : l'interne ne dit pas plus que le texte (a_s=b_s=0,5)", dict(a_h=1.5, a_s=0.5, c_s=0.0, b_h=1.0, b_s=0.5), False),
        ("F  imitation du succès : aucun signe interne (a_s=0), texte faible", dict(a_h=1.5, a_s=0.0, c_s=0.0, b_h=1.0, b_s=0.5), True),
    ]
    reps = 40
    enfants = ENF_D.spawn(len(objets) * 2)
    i = 0
    print()
    print("| objet | allure s | k moyen | budget | uniforme | sonde déployée (évitée) | interne « dommage » | interne « excès » | texte « excès » | mélange interne « excès » + uniforme |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for (nom, prm, imite) in objets:
        for s in (0.01, 0.05):
            rng = np.random.default_rng(enfants[i]); i += 1
            acc = {k: [] for k in ("unif", "depl", "wb_dom", "wb_exc", "bb_exc", "mel")}
            ks = []
            budgets_mult = (1, 3)
            res = {bm: {k: [] for k in acc} for bm in budgets_mult}
            for _ in range(reps):
                typ_u, x_u, y_u = tirer_population(rng, n_u, s, p0, d, imite_succes=imite, **prm)
                typ_a, x_a, y_a = tirer_population(rng, n_a, s, p0, d, imite_succes=imite, **prm)
                typ_r, x_r, y_r = tirer_population(rng, m_ref, 0.0, p0, d, imite_succes=imite, **prm)
                rec_a = (typ_a >= 1) & (rng.random(n_a) < q)
                rec_r = (typ_r >= 1) & (rng.random(m_ref) < q)
                est_sab = (typ_u == 2)
                k = int(est_sab.sum()); ks.append(k)
                w_dom = direction(x_a[rec_a], x_a[~rec_a])
                w_exc = direction(x_a[rec_a], x_r[rec_r])
                v_exc = direction(y_a[rec_a], y_r[rec_r])
                scores = {
                    "unif": rng.random(n_u),
                    "depl": x_u[:, 2] + 0.0 * rng.random(n_u),
                    "wb_dom": x_u @ w_dom,
                    "wb_exc": x_u @ w_exc,
                    "bb_exc": y_u @ v_exc,
                }
                for bm in budgets_mult:
                    B = max(1, bm * k)
                    for nm, sc in scores.items():
                        res[bm][nm].append(rappel_au_budget(sc, est_sab, B, rng))
                    res[bm]["mel"].append(rappel_au_budget(scores["wb_exc"], est_sab, B, rng, melange=True))
            for bm in budgets_mult:
                r = {nm: float(np.mean(v)) for nm, v in res[bm].items()}
                print(f"| {nom} | {s} | {np.mean(ks):.0f} | {bm}k | {r['unif']:.3f} | {r['depl']:.3f} | {r['wb_dom']:.3f} | {r['wb_exc']:.3f} | {r['bb_exc']:.3f} | {r['mel']:.3f} |")
    # Recherche active itérative : le défenseur ré-audite par tranches, réapprend la direction d'excès
    # sur ce qu'il a trouvé, et recommence (moitié par le score, moitié au hasard).
    print()
    print("Recherche active itérative (10 tranches ; chaque tranche : moitié des étiquettes par le score d'excès"
          " réappris, moitié au hasard ; les dommages reconnus rejoignent les positifs du suspect) :")
    print("| objet | allure s | budget | one-shot interne « excès » | itératif interne | itératif texte | uniforme |")
    print("|---|---|---|---|---|---|---|")
    enf_it = ENF_D.spawn(1)[0].spawn(4)
    j = 0
    for (nom, prm, imite) in (objets[0], objets[2]):
        for s in (0.01, 0.05):
            rng = np.random.default_rng(enf_it[j]); j += 1
            r_one, r_it_wb, r_it_bb, r_unif = [], [], [], []
            for _ in range(20):
                typ_u, x_u, y_u = tirer_population(rng, n_u, s, p0, d, imite_succes=imite, **prm)
                typ_a, x_a, y_a = tirer_population(rng, n_a, s, p0, d, imite_succes=imite, **prm)
                typ_r, x_r, y_r = tirer_population(rng, m_ref, 0.0, p0, d, imite_succes=imite, **prm)
                rec_a = (typ_a >= 1) & (rng.random(n_a) < q)
                rec_r = (typ_r >= 1) & (rng.random(m_ref) < q)
                est_sab = (typ_u == 2)
                k = int(est_sab.sum())
                B = 3 * k
                w = direction(x_a[rec_a], x_r[rec_r])
                r_one.append(rappel_au_budget(x_u @ w, est_sab, B, rng))
                r_unif.append(B / n_u)
                for feats_u, feats_a, feats_r, acc in ((x_u, x_a, x_r, r_it_wb), (y_u, y_a, y_r, r_it_bb)):
                    pos = [feats_a[rec_a]]
                    pris = np.zeros(n_u, dtype=bool)
                    tranche = max(2, B // 10)
                    for _t in range(10):
                        wv = direction(np.vstack(pos), feats_r[rec_r])
                        sc = feats_u @ wv
                        sc[pris] = -np.inf
                        nb = tranche // 2
                        top = np.argsort(-sc)[:nb]
                        pris[top] = True
                        libres = np.nonzero(~pris)[0]
                        hasard = rng.choice(libres, size=tranche - nb, replace=False)
                        pris[hasard] = True
                        nouv = np.concatenate([top, hasard])
                        rec_n = (typ_u[nouv] >= 1) & (rng.random(len(nouv)) < q)
                        if rec_n.any():
                            pos.append(feats_u[nouv[rec_n]])
                    acc.append(est_sab[pris].sum() / max(1, k))
            print(f"| {nom[:2].strip()} | {s} | 3k | {np.mean(r_one):.3f} | {np.mean(r_it_wb):.3f} | {np.mean(r_it_bb):.3f} | {np.mean(r_unif):.3f} |")
    print()
    print(f"facteur d'exclusion des échecs honnêtes (objet F, gain légitime maximal d'un tri qui écarte"
          f" seulement les échecs honnêtes) : 1/(1-(1-s)p0) = {1 / (1 - 0.99 * p0):.3f} à s=0,01 ;"
          f" {1 / (1 - 0.95 * p0):.3f} à s=0,05.")
    print("lecture : rappel = part des sabotés non audités retrouvés avec le budget dit. Uniforme : budget/n_u."
          " Objet V : la lecture interne apprise après l'alarme doit battre l'uniforme et le texte ; objet E :"
          " pas d'écart interne-texte ; objet F : la lecture interne ne doit pas battre l'uniforme (sinon fuite"
          " d'étiquettes dans la simulation) et le mélange garde au moins la moitié de l'uniforme.")
    print()
    # Forme close : coût de réparation et dommage irréversible
    print("### Coût de réparation et dommage irréversible (forme close)")
    print("Pour retrouver une part r des k sabotés non audités parmi n_u : uniforme ~ r·n_u étiquettes ;"
          " tri de précision pi ~ r·k/pi. Avec des effets retenus réversibles sur une fenêtre au moins égale au"
          " délai d'alarme et un taux de correction f d'un épisode retrouvé, le dommage irréversible vaut"
          " (1 - r·f)·k ; sans fenêtre réversible, il vaut k quoi qu'on retrouve.")
    for (k, n_u2, pi, r, f) in ((200, 20000, 0.5, 0.8, 0.42), (200, 20000, 0.05, 0.8, 0.42), (200, 20000, 0.5, 0.8, 1.0)):
        print(f"  k={k}, n_u={n_u2}, précision {pi}, r={r}, f={f} : uniforme {r * n_u2:.0f} étiquettes ;"
              f" tri {r * k / pi:.0f} ; dommage irréversible (1-r·f)·k = {(1 - r * f) * k:.0f}")
    print("  (f = 0,42 : taux de correction au premier essai mesuré dans un autre cadre, Gan et al. 2026, p. 1 ;"
          " illustration seulement.)")
    print()


# ----------------------------------------------------------------------------------------------
# Bloc E : dissuasion, modèle de Gans et Holden étendu au régime d'excès
# ----------------------------------------------------------------------------------------------
def seuil_dissuasion(g, kappa, alpha_c, p_hon, pas=1e-4, hmax=60.0):
    """t_bar = sup_h (g - kappa h) / (exp(-alpha_c h) - p_hon) sur les h où le dénominateur > 0.
    Infini si un plan à preuve nette nulle (exp(-alpha_c h) <= p_hon) garde g - kappa h > 0."""
    if p_hon > 0:
        h0 = math.log(1 / p_hon) / alpha_c
        if g - kappa * h0 > 0:
            return math.inf
    h = np.arange(0, hmax, pas)
    den = np.exp(-alpha_c * h) - p_hon
    ok = den > 1e-12
    val = (g - kappa * h[ok]) / den[ok]
    return max(0.0, float(val.max()))


def bloc_E():
    print("## Bloc E — dissuasion : le seuil de Gans et Holden quand l'honnête échoue aussi")
    g, kappa, alpha_c = 0.2, 0.1, 1.0
    print(f"technologie de leur exemple (Gans et Holden, p. 9-10) : d(h)=exp(-alpha h), c(h)=kappa h ; g={g},"
          f" kappa={kappa}, alpha={alpha_c}, F=1. Extension (de moi, non leur résultat) : une sanction sur la"
          " preuve frappe aussi l'honnête avec probabilité p_hon ; seule compte la preuve nette d(h) - p_hon.")
    print("| p_hon (preuve que l'honnête produit aussi) | seuil t_bar | dissuasion possible pour tout type ? |")
    print("|---|---|---|")
    p_crit = math.exp(-alpha_c * g / kappa)
    for p_hon in (0.0, 0.05, 0.10, round(p_crit, 4), 0.14, 0.20, 0.30):
        t = seuil_dissuasion(g, kappa, alpha_c, p_hon)
        print(f"| {p_hon} | {'infini' if math.isinf(t) else f'{t:.4f}'} | {'non' if math.isinf(t) else 'oui (sanction assez grande)'} |")
    print(f"forme close : seuil infini dès que g > (kappa/alpha)·log(1/p_hon), soit p_hon > exp(-alpha g/kappa) ="
          f" {p_crit:.4f} ; à p0 = 0,2, (kappa/alpha)·log(5) = {kappa / alpha_c * math.log(5):.4f} < g = {g} :"
          " leur exemple (t_bar = 0,272 sans faux positif honnête) n'est plus dissuadable.")
    print("Second canal de preuve, interne (conjonction dommage et motif interne), sanction propre F2 :"
          " plan le moins cher à preuve nette nulle sur les deux canaux = (kappa/alpha)·log(1/p0) +"
          " min(kappa/alpha, kappa_i/alpha_i)·log(tau/phi) (condition suffisante d'un seuil infini).")
    print("Vérification par programme linéaire : existe-t-il F1, F2 >= 0 qui dissuadent tous les plans (h, h')"
          " d'une grille ? (faisable = seuil fini).")
    from scipy.optimize import linprog
    p0, phi, tau, alpha_i = 0.2, 0.05, 0.8, 1.0
    H = np.arange(0.0, 6.0001, 0.05)
    Hi = np.arange(0.0, 12.0001, 0.05)
    hh, hhi = np.meshgrid(H, Hi, indexing="ij")
    hh = hh.ravel(); hhi = hhi.ravel()
    for kappa_i in (0.0, 0.02, 0.05, 0.1):
        cout = kappa / alpha_c * math.log(1 / p0) + min(kappa / alpha_c, kappa_i / alpha_i) * math.log(tau / phi)
        c = kappa * hh + kappa_i * hhi
        d1 = np.exp(-alpha_c * hh)
        d2 = d1 * tau * np.exp(-alpha_i * hhi)
        n1 = d1 - p0
        n2 = d2 - p0 * phi
        prof = (g - c) > 1e-12
        # contraintes : F1 n1 + F2 n2 >= g - c  <=>  -n1 F1 - n2 F2 <= -(g - c)
        A = np.column_stack([-n1[prof], -n2[prof]])
        b = -(g - c[prof])
        res = linprog(c=[1.0, 1.0], A_ub=A, b_ub=b, bounds=[(0, None), (0, None)], method="highs")
        faisable = res.status == 0
        sanc = f"F1={res.x[0]:.3f}, F2={res.x[1]:.3f}" if faisable else "aucune"
        print(f"  kappa_i={kappa_i} : coût du plan nul = {cout:.4f} (g={g}) ; programme linéaire :"
              f" {'faisable, seuil fini' if faisable else 'infaisable, seuil infini'} ({sanc})")
    print("lecture : une lecture interne peut faire passer le seuil de l'infini au fini pour une bande de gains,"
          " si tau > phi et si la dissimulation interne coûte à l'agent (kappa_i > 0) ; à kappa_i = 0 rien ne"
          " change. Le levier (sanction écrite dans l'objectif de l'agent) est fermé dans le programme"
          " (N-053, point 5 ; N-060 v3, point 4) et sans prise sur un organisme à politique fixe.")
    print()


def bloc_F():
    print("## Bloc F — base de contrôle à l'audit (estimateur augmenté) et plateau, forme close")
    eps, p_d, p0, m = 0.05, 0.24, 0.20, 2000
    print(f"suppositions : tirage d'audit eps={eps} ; taux de dommage du suspect p_d={p_d} ; base g in [0,1] lue"
          " sur chaque épisode ; estimateur g + B(V - g)/eps, sans biais pour toute g (tirage secret, probabilités"
          " connues).")
    var_ipw = p_d / eps - p_d ** 2

    def var_aug(R):
        return p_d * (1 - p_d) + (1 / eps - 1) * R

    for nom, R in (("base parfaite (R=0)", 0.0), ("base qui explique la moitié", 0.5 * p_d * (1 - p_d)),
                   ("base sans valeur (g=0, pondération inverse seule)", p_d),
                   ("base adverse g = 1 - V (R=1)", 1.0),
                   ("base adverse bornée à 0,5 : R=(1-p_d)·0,25+p_d", (1 - p_d) * 0.25 + p_d)):
        print(f"  {nom} : variance par épisode {var_aug(R):.3f} contre {var_ipw:.3f} (x{var_aug(R) / var_ipw:.2f})")
    print("lecture : sans biais dans tous les cas (l'adversaire n'élargit que la variance, sous une borne si la base"
          " est bornée) ; mais le plateau de la référence ne bouge pas : il vient de l'incertitude sur le taux honnête.")
    for Rh_frac in (1.0, 0.5, 0.25):
        print(f"  prédicteur du dommage honnête par tâche qui ne lit PAS le suspect, résidu {Rh_frac:.2f}·p0(1-p0) :"
              f" plateau multiplié par sqrt({Rh_frac:.2f}) = {math.sqrt(Rh_frac):.3f} (m={m} inchangé)")
    print("  le même prédicteur lisant les états internes du suspect entrerait dans les deux sens (le saboteur"
          " monterait la base sur ses épisodes et absorberait l'excès) : interdit par la règle « une seule"
          " direction » (Blindfold, p. 12).")
    print()


if __name__ == "__main__":
    entete()
    ok_A = bloc_A()
    resB = bloc_B()
    bloc_C()
    bloc_D()
    bloc_E()
    bloc_F()
    print("## Objets de contrôle, attendus et rendus (résumé)")
    print(f"A : loi du saboteur imitant l'échec honnête == loi d'un honnête à p0' : attendu vrai, rendu {ok_A}")
    pf = resB[(0.05, 0.02, "conjonction")][0]
    pp = resB[(0.05, 0.02, "plancher")][0]
    print(f"B : conjonction neutralisée (tau=phi), s=0,02 : P(alarme) attendue <= plancher ; rendu {pf:.3f} contre {pp:.3f}")
    print("fin")
