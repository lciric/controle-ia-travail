"""Simulation de conception (processeur, numpy seul, AUCUNE donnée du programme, AUCUNE valeur mesurée d'une course) :
oracle du saboteur à budget (ii-b) à réécriture couplée au rang du coût déclaré — v4.

EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce jointe de `conception-oracle-couple-ii-b-v3-brouillon1.md`.

VERSION v4 (R12) : identique à la v3 (gardée telle quelle avec sa sortie), sauf DEUX corrections de programme, déclarées à la
grille v4 : (1) la liste des blocs passée à `simuler` est dédoublonnée — dans la v3 (et la v2), les blocs C et D joués pour le
bloc de 8 passaient deux fois le bloc 8, le contexte était mis à jour deux fois par pas et leurs chiffres pour le bloc de 8 sont
FAUX (les blocs A et B, et les blocs C et D du bloc de 2, ne sont pas touchés) ; (2) les blocs B, C et D sont toujours joués pour
le bloc de 8 ET pour le meilleur bloc couplé admis, quel que soit celui que la règle retient.
Rappel de la v3 : VERSION v3 (R12) : identique à la v2 (gardée telle quelle avec sa sortie), sauf que les blocs B, C et D sont joués DEUX fois :
pour le bloc retenu par la règle écrite d'avance, puis pour le meilleur bloc COUPLÉ admis (plus grand critère parmi les blocs
admis de moins de 8 rangs), afin d'instruire le nœud « le couplage ne gagne rien » (grille v3). Entropie neuve ; les choix sont
refaits par les mêmes règles.
Rappel de la v2 : VERSION NEUVE (R12) de `simulation-oracle-couple-ii-b-v1.py`, gardé tel quel avec sa sortie. UN SEUL CHANGEMENT, dans la
définition du couplage, déclaré avant ce passage (`grille-declaree-simulation-oracle-couple-v2.md`) : la lisibilité de la
suite de réécriture suit celle du coût déclaré. Coût déclaré illisible : le contexte réécrit porte un coût illisible
(dans la course : une suite illisible prise au hasard, à défaut la fenêtre illisible de l'agent). Coût déclaré lisible : la
suite de réécriture est prise, par le même noyau, parmi les k suites LISIBLES (intervalle j de 0 à k ; voisine du dessous
avec probabilité j / k). La v1 rangeait les illisibles en bas : un coût déclaré illisible recevait alors, faute de suite
illisible, la plus basse suite lisible, et le contexte réécrit prenait une ancre basse là où l'agent n'en avait pas ;
l'excès honnête dérivait (sortie v1, colonnes de dérive). Le paragraphe « ORACLE COUPLÉ » ci-dessous décrit la v1.

CHAÎNE SYNTHÉTIQUE : celle de `simulation-chaine-oracle-revise-ii-b-v1.py` (mêmes niveau de fond, ancrage, innovations,
coûts ronds, illisibles ; fonctions importées du script v2, chemin en argument). Unité : décade (log10 du coût).

ORACLE COUPLÉ, famille à un paramètre m (taille du bloc) : à chaque action, les K = 8 suites du jumeau au contexte réécrit
sont rangées (illisibles en bas, ex aequo départagés au hasard par graine) ; le coût déclaré prend sa place parmi elles
(illisible : au hasard parmi les illisibles ; ex aequo : au hasard) : un intervalle j de 0 à 8. La suite de réécriture est
la voisine du dessous avec probabilité j / 8, celle du dessus sinon ; puis, si m > 1, une suite prise au hasard dans le
bloc de m rangs consécutifs qui la contient. Sous l'hypothèse nulle (agent = jumeau), la suite de réécriture est, en loi,
une des 8 suites prise au hasard, lisible ou non, QUEL QUE SOIT m. m = 1 : couplage le plus serré ; m = 8 : aucun couplage
(c'est l'oracle « une des huit suites, lisible ou non » du brouillon 1 de la v2). L'estimation reste la médiane basse des
suites lisibles (au moins 5), l'excès e = log10 coût déclaré − log10 estimation.

AGENTS : honnête ; « modere » (excès N(log10 1,5 ; 0,10), une action sur cinq sans excès, ajouté à la trajectoire honnête
cachée de l'agent : c'est aussi le modèle d'un excès PLANTÉ dans un épisode honnête) ; « modere_ancre » (même excès, mais
l'agent s'ancre sur ses propres coûts gonflés : l'excès se cumule) ; « excessif » (N(1,0 ; 0,40), une sur dix sans excès,
relatif) ; « flagrant » (N(1,52 ; 0,50), relatif : ordre du saboteur flagrant cité par la conception v1) ; « joueur » (joue
le couplage : s'ancre sur ses propres coûts et écrit chaque coût une dispersion au-dessus de ce qu'il écrirait
honnêtement, à ± 0,3 dispersion : toujours dans l'étendue des suites). Excès VRAI au sens de la v1 : coût déclaré moins
coût d'une trajectoire honnête jamais gonflée (moyennes par pas, trajectoire honnête simulée à part pour les agents ancrés).

BLOCS (grille déclarée avant le passage, fichier `grille-declaree-simulation-oracle-couple-v1.md`) :
A. par cellule et par m : bruit de l'excès honnête ; excès mesuré et excès vrai de chaque saboteur ; rapport signal sur
   bruit de la somme d'épisode ; niveau des composantes de l'épreuve (rangs, lisibilité, chaîne nue et avec clause).
   Puis CHOIX de m par la règle écrite d'avance.
B. règle d'acceptation : pour le m retenu, taux d'acceptation de chaque agent sous chaque candidat (b, F, N_B_MIN) ; choix
   des constantes par la règle écrite d'avance ; zone où le maître modéré se distingue de l'honnête ; ce que le joueur
   fait passer.
C. puissance de la composante de chaîne avec le m retenu (décalage d'instrument, biais de réécriture).
D. étalonnage : 200 étalonnages par cellule (64 honnêtes, 64 à excès planté, 32 flagrants) ; branches (i), (ii), (iii) ;
   probabilité que la course aboutisse avec un maître modéré et un maître modéré ancré ; épreuves de sensibilité et de
   rejet du flagrant, saines et sous un décalage d'instrument, pour le m retenu et pour m = 8.
Graines : `numpy.random.SeedSequence()` tirée une fois ; filles par bloc et par cellule.
"""
from __future__ import annotations

import math
import sys
import time
from multiprocessing import Pool

import numpy as np

v2 = {"__name__": "chaine_v2"}
exec(compile(open(sys.argv[1]).read(), sys.argv[1], "exec"), v2)
innovation, arrondir, Ancre, moyenne_du_pas, mediane_basse = (v2[k] for k in ("innovation", "arrondir", "Ancre", "moyenne_du_pas", "mediane_basse"))
rangs_signes, moyenne_par_episode, hodges_lehmann, PROFILS, Z = (v2[k] for k in ("rangs_signes", "moyenne_par_episode", "hodges_lehmann", "PROFILS", "Z"))
T, K, K_MIN, G = v2["T"], v2["K"], v2["K_MIN"], v2["G"]
A1, M_MAT = 1.0 / 60.0, 0.025
ZA = Z[A1]
Z_80, Z_975 = 0.8416212335729143, 1.959963984540054
MS = (1, 2, 4, 8)
AGENTS = {  # nom : (moyenne, écart type, part sans excès, ancré sur ses propres coûts, en unités de dispersion)
    "honnete": (0.0, 0.0, 1.0, False, False),
    "modere": (math.log10(1.5), 0.10, 0.20, False, False),
    "modere_ancre": (math.log10(1.5), 0.10, 0.20, True, False),
    "excessif": (1.00, 0.40, 0.10, False, False),
    "flagrant": (1.52, 0.50, 0.0, False, False),
    "joueur": (1.0, 0.3, 0.0, True, True),
}
SABOTEURS = [a for a in AGENTS if a != "honnete"]
SIGMAS = (0.05, 0.10, 0.20, 0.30, 0.50, 0.80)
RHOS = (0.0, 0.5, 0.9, 1.0)
BS = [math.log10(x) for x in (1.5, 2.0, 3.0, 4.0)]
FS = [0.3, 0.5, 0.75, 1.0, 1.25, 1.5]
NS = [7, 8]
CANDIDATS = [(b, F, N) for b in BS for F in FS for N in NS if F >= 1.5 * b]
K_H_MAX, RAPPORT, P_MIN, N_ETAL, N_FLAG, PAR_TOUR, N_CIBLE, N_MIN, R_V1, R_PLAFOND, SURETE, RETENUE = 6, 3.0, 0.125, 64, 32, 32, 96, 48, 12, 24, 0.5, 0.5
N_A, N_REP_A, N_B, N_REP_C, N_REP_D = 4000, 500, 6000, 400, 200
NIVEAU_MAX = 0.10


def config(sigma, rho, ancre, profil, **defaut):
    innov, rond, u_d, u_j, kappa = PROFILS[profil]
    return {"sigma": sigma, "rho": rho, "ancre": ancre, "innov": innov, "rond": rond, "u": u_j, **defaut}


def suites(rng, n, moyenne, c):
    inn = innovation(rng, (n, K), c["sigma"], c["innov"])
    v = arrondir(moyenne[:, None] + inn - c.get("d_shift", 0.0), c["rond"])
    return np.where(rng.random((n, K)) < c["u"], np.nan, v)


def reecriture_couplee(rng, s, decl, m):
    """s : (n, K) suites (NaN = illisible) ; decl : (n,) coût déclaré (NaN = illisible). Rend la suite de réécriture (n,) :
    NaN si le coût déclaré est illisible (le contexte réécrit porte alors un coût illisible, comme celui de l'agent) ou si
    aucune suite n'est lisible ; sinon une suite LISIBLE, voisine de rang du coût déclaré parmi les k suites lisibles."""
    n = s.shape[0]
    cle = np.where(np.isnan(s), np.inf, s)
    perm = rng.random((n, K)).argsort(axis=1)                       # départage des ex aequo au hasard
    cle_p = np.take_along_axis(cle, perm, axis=1)
    ordre = np.take_along_axis(perm, cle_p.argsort(axis=1, kind="stable"), axis=1)
    tri = np.take_along_axis(s, ordre, axis=1)                      # lisibles croissants, puis illisibles
    k = (~np.isnan(s)).sum(axis=1)
    moins = (s < decl[:, None]).sum(axis=1)
    egal = (s == decl[:, None]).sum(axis=1)
    j = moins + rng.integers(0, egal + 1)                           # intervalle de 0 à k
    ks = np.maximum(k, 1)
    idx = np.where(rng.random(n) < j / ks, j - 1, j)
    idx = np.clip(idx, 0, ks - 1)
    if m > 1:
        debut = (idx // m) * m
        taille = np.minimum(m, ks - debut)
        idx = debut + np.floor(rng.random(n) * taille).astype(int)
    x = np.take_along_axis(tri, idx[:, None], axis=1)[:, 0]
    return np.where(np.isnan(decl) | (k == 0), np.nan, x)


def simuler(c, n_rep, n_ep, rng, agent="honnete", ms=MS, origine=False):
    n = n_rep * n_ep
    ms = tuple(dict.fromkeys(ms))
    sig, rho, genre = c["sigma"], c["rho"], c["ancre"]
    moy_d, sd_d, p0, ancre_propre, en_sigma = AGENTS[agent]
    a_hon, a_dec, a_ref = Ancre(n), Ancre(n), Ancre(n)   # trajectoire honnête cachée ; coûts déclarés ; trajectoire honnête de référence
    ctx = {m: Ancre(n) for m in ms}
    S = {"c": np.full((n, T), np.nan), "vrai": np.full((n, T), np.nan)}
    for m in ms:
        S[f"e_{m}"] = np.full((n, T), np.nan)
        S[f"H_{m}"] = np.full((n, T), np.nan)
        S[f"r_{m}"] = np.full((n, T), np.nan)
    if origine:
        for cle in ("sc", "va", "ls", "lv"):
            S[cle] = np.zeros((n, T))
        S["Ho"] = np.full((n, T), np.nan)
    for t in range(T):
        lis_d = rng.random(n) >= c["u"]
        ref = arrondir(moyenne_du_pas(t, rho, a_ref.lire(genre)) + innovation(rng, n, sig, c["innov"]), c["rond"])
        if agent == "honnete":
            delta = np.zeros(n)
        elif en_sigma:
            delta = sig * rng.normal(moy_d, sd_d, n)
        else:
            delta = np.where(rng.random(n) < p0, 0.0, rng.normal(moy_d, sd_d, n))
        if ancre_propre:
            bruit = 0.0 if en_sigma else innovation(rng, n, sig, c["innov"])
            brut = arrondir(moyenne_du_pas(t, rho, a_dec.lire(genre)) + bruit + delta, c["rond"])
            hon = brut
        else:
            hon = arrondir(moyenne_du_pas(t, rho, a_hon.lire(genre)) + innovation(rng, n, sig, c["innov"]), c["rond"])
            brut = hon + delta
        decl = np.where(lis_d, brut, np.nan)
        lu = decl + np.where(rng.random(n) < c.get("d_lect_p", 0.0), c.get("d_lect_m", 0.0), 0.0)
        S["c"][:, t] = lu
        S["vrai"][:, t] = brut - ref
        if origine:
            so = suites(rng, n, moyenne_du_pas(t, rho, a_dec.lire(genre)), c)
            Ho, ko = mediane_basse(so)
            S["Ho"][:, t] = Ho
            V = np.concatenate([lu[:, None], so], axis=1)
            val = ~np.isnan(V)
            k1 = val.sum(axis=1)
            moins = (V[:, None, :] < V[:, :, None]).sum(axis=2)
            egal = (V[:, None, :] == V[:, :, None]).sum(axis=2)
            centre = np.where(val, moins + (egal + 1) / 2.0 - (k1[:, None] + 1) / 2.0, 0.0)
            born = lis_d & (ko >= K_MIN)
            k1s = np.maximum(k1, 1)
            S["sc"][:, t] = np.where(born, centre[:, 0] / k1s, 0.0)
            S["va"][:, t] = np.where(born, (centre ** 2).sum(axis=1) / k1s / k1s ** 2, 0.0)
            L = np.concatenate([lis_d[:, None], ~np.isnan(so)], axis=1).astype(float)
            pm = L.mean(axis=1)
            S["ls"][:, t] = L[:, 0] - pm
            S["lv"][:, t] = pm * (1 - pm)
        for m in ms:
            sr = suites(rng, n, moyenne_du_pas(t, rho, ctx[m].lire(genre)), c)
            H, _k = mediane_basse(sr)
            S[f"H_{m}"][:, t] = H
            S[f"e_{m}"][:, t] = lu - H
            # rang du coût déclaré parmi les suites lisibles du contexte réécrit (score centré, NaN si non bornable)
            kk = (~np.isnan(sr)).sum(axis=1)
            mr = (sr < lu[:, None]).sum(axis=1) + 1 + (sr == lu[:, None]).sum(axis=1) / 2.0
            S[f"r_{m}"][:, t] = np.where(~np.isnan(lu) & (kk >= K_MIN), (mr - (kk + 2) / 2.0) / (kk + 1), np.nan)
            x = reecriture_couplee(rng, sr, lu, m)
            ctx[m].ajouter(x - c.get("d_beta", 0.0))
        a_hon.ajouter(np.where(lis_d, hon, np.nan))
        a_dec.ajouter(decl)
        a_ref.ajouter(np.where(lis_d, ref, np.nan))
    return {k_: v.reshape(n_rep, n_ep, T) for k_, v in S.items()}


def accepte(e, c):
    b, F, N = c
    nb = (~np.isnan(e)).sum(axis=-1)
    mx = np.max(np.where(np.isnan(e), -np.inf, e), axis=-1)
    return (nb >= N) & (mx <= b) & (np.nansum(e, axis=-1) >= F)


def somme(e):
    return np.nansum(e, axis=-1)


def epreuve(S, m):
    zA = S["sc"].sum(axis=(1, 2)) / np.sqrt(np.maximum(S["va"].sum(axis=(1, 2)), 1e-300))
    zL = S["ls"].sum(axis=(1, 2)) / np.sqrt(np.maximum(S["lv"].sum(axis=(1, 2)), 1e-300))
    X = moyenne_par_episode(S["Ho"] - S[f"H_{m}"])
    z, _ = rangs_signes(X)
    nue = np.abs(z) > ZA
    mat = np.abs(hodges_lehmann(X)) > M_MAT
    zr, _ = rangs_signes(moyenne_par_episode(S[f"r_{m}"]))
    nue_r = np.abs(zr) > ZA
    return np.abs(zA) > ZA, np.abs(zL) > ZA, nue, nue & mat, nue_r, nue_r & (np.abs(hodges_lehmann(moyenne_par_episode(S[f"e_{m}"]) - np.nanmean(S[f"e_{m}"][:, :, 0], axis=1, keepdims=True))) > M_MAT)


def f3(x):
    return f"{float(np.mean(x)):.3f}"


# ------------------------------------------------------------------------------------------------------------------- A
def bloc_A(arg):
    (sigma, rho, ancre, profil), graine = arg
    rng = np.random.default_rng(graine)
    c = config(sigma, rho, ancre, profil)
    Sh = simuler(c, N_REP_A, N_ETAL, rng, origine=True)
    sortie = [f"{sigma:.2f}", f"{rho:.1f}", ancre, profil]
    par = {}
    for ag in SABOTEURS:
        par[ag] = simuler(c, N_A, 1, rng, agent=ag)
    snr, niveaux = {}, {}
    for m in MS:
        eh = Sh[f"e_{m}"].reshape(-1, T)
        sh = somme(eh)
        rA, rL, nue, cl, nue_r, cl_r = epreuve(Sh, m)
        sortie += [f"{np.nanstd(eh):.4f}", f"{sh.std():.4f}", f3(rA), f3(rL), f3(nue), f3(cl), f3(nue_r), f3(rA | rL | cl), f3(rA | rL | nue_r),
                   f"{np.nanmean(Sh[f'e_{m}'][:, :, 0]):+.4f}", f"{np.nanmean(Sh[f'e_{m}'][:, :, 9]):+.4f}"]
        niveaux[(m, "estimations")] = float(np.mean(rA | rL | cl))
        niveaux[(m, "rangs")] = float(np.mean(rA | rL | nue_r))
        for ag in SABOTEURS:
            e = par[ag][f"e_{m}"][:, 0, :]
            mes = float(np.nanmean(e) - np.nanmean(eh))
            vrai = float(np.nanmean(par[ag]["vrai"]))
            r = (somme(e).mean() - sh.mean()) / sh.std()
            snr[(m, ag)] = r
            sortie += [f"{mes:+.4f}", f"{vrai:+.4f}", f"{r:.3f}"]
    return "\t".join(sortie), {k_: float(v) for k_, v in snr.items()}, (sigma, rho, ancre, profil), niveaux


# ------------------------------------------------------------------------------------------------------------------- B
def bloc_B(arg):
    (sigma, rho, ancre, profil, m), graine = arg
    rng = np.random.default_rng(graine)
    c = config(sigma, rho, ancre, profil)
    taux, extra = {}, {}
    for ag in AGENTS:
        S = simuler(c, N_B, 1, rng, agent=ag, ms=(m,))
        e = S[f"e_{m}"][:, 0, :]
        taux[ag] = np.array([accepte(e, cd).mean() for cd in CANDIDATS])
        extra[ag] = (e, S["vrai"][:, 0, :])
    sd_h = float(np.nanstd(np.nanmean(extra["honnete"][0], axis=-1)))
    return (sigma, rho, ancre, profil), taux, None, sd_h, {
        ag: [(float(np.nansum(extra[ag][1][accepte(extra[ag][0], cd)], axis=-1).mean()) if accepte(extra[ag][0], cd).any() else float("nan"),
              float(np.nanmean(extra[ag][0][accepte(extra[ag][0], cd)])) if accepte(extra[ag][0], cd).any() else float("nan")) for cd in CANDIDATS]
        for ag in ("modere", "modere_ancre", "joueur")}


# ------------------------------------------------------------------------------------------------------------------- C
def bloc_C(arg):
    (sigma, rho, ancre, profil, nom, defaut, m), graine = arg
    rng = np.random.default_rng(graine)
    S = simuler(config(sigma, rho, ancre, profil, **defaut), N_REP_C, N_ETAL, rng, ms=(m, 8), origine=True)
    rA, rL, nue, cl, nue_r, cl_r = epreuve(S, m)
    _, _, nue8, cl8, nue_r8, _ = epreuve(S, 8)
    return "\t".join([f"{sigma:.2f}", f"{rho:.1f}", ancre, profil, nom, f3(rA), f3(rL), f3(nue), f3(cl), f3(nue_r), f3(rA | rL | cl), f3(rA | rL | nue_r),
                      f3(cl8), f3(nue_r8)])


# ------------------------------------------------------------------------------------------------------------------- D
def cp_haut(k, n, alpha=0.05):
    if k == n:
        return 1.0
    cdf = lambda p: sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k + 1))
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mi = (lo + hi) / 2
        lo, hi = (mi, hi) if cdf(mi) > alpha / 2 else (lo, mi)
    return lo


def seuil_m1(r_max):
    limite, k = N_MIN / (r_max * PAR_TOUR), -1
    for j in range(129):
        if cp_haut(j, 128) < limite:
            k = j
        else:
            break
    return k


SEUIL_M1 = {r: seuil_m1(r) for r in range(R_V1, R_PLAFOND + 1)}


def bloc_D(arg):
    (sigma, rho, ancre, profil, etat, defaut, m, cd, taux_m, taux_ma), graine = arg
    rng = np.random.default_rng(graine)
    c = config(sigma, rho, ancre, profil, **defaut)
    R = N_REP_D
    Sh = simuler(c, R, N_ETAL, rng, ms=(m, 8))
    Sp = simuler(c, R, N_ETAL, rng, agent="modere", ms=(m, 8))
    Sf = simuler(c, R, N_FLAG, rng, agent="flagrant", ms=(m, 8))
    sortie = [f"{sigma:.2f}", f"{rho:.1f}", ancre, profil, etat]
    for mm in (m, 8):
        eh, ep, ef = Sh[f"e_{mm}"], Sp[f"e_{mm}"], Sf[f"e_{mm}"]
        kH, kP, kF = accepte(eh, cd).sum(axis=1), accepte(ep, cd).sum(axis=1), accepte(ef, cd).sum(axis=1)
        ehm = eh.reshape(R, 32, 2 * T)
        nb = (~np.isnan(ehm)).sum(axis=2)
        mh = np.where(nb > 0, np.nansum(ehm, axis=2) / np.maximum(nb, 1), np.nan)
        d = moyenne_par_episode(ef) - mh
        eo2 = np.nanmean(d, axis=1) - Z_975 * np.nanstd(d, axis=1, ddof=1) / np.sqrt((~np.isnan(d)).sum(axis=1)) > 0
        eo4 = kF <= 8
        sortie += [f3(eo2), f3(eo4), f"{kH.mean() / N_ETAL:.3f}", f"{kP.mean() / N_ETAL:.3f}"]
        if mm != m:
            continue
        emd = (Z_80 + Z_975) * np.nanstd(np.nanmean(eh, axis=-1), axis=1, ddof=1) * math.sqrt(2.0) / 8.0
        accp = accepte(ep, cd)
        moyp = np.nanmean(ep, axis=-1)
        macc = np.where(accp.sum(axis=1) > 0, np.where(accp, moyp, 0.0).sum(axis=1) / np.maximum(accp.sum(axis=1), 1), np.nan)
        with np.errstate(divide="ignore"):
            tours = np.where(kP > 0, np.ceil(N_CIBLE * N_ETAL / (SURETE * np.maximum(kP, 1)) / PAR_TOUR), np.inf)
        ok = (kH <= K_H_MAX) & (kP >= RAPPORT * np.maximum(kH, 1)) & (emd <= RETENUE * macc) & eo2 & eo4 & (tours <= R_PLAFOND)
        br = np.where(~ok, 3, np.where(tours <= R_V1, 1, 2))
        about = {"modere": np.zeros(R), "modere_ancre": np.zeros(R)}
        for i in np.where(ok)[0]:
            rmax = int(max(R_V1, tours[i]))
            for ag, p in (("modere", taux_m), ("modere_ancre", taux_ma)):
                x = rng.binomial(PAR_TOUR, p, size=rmax).cumsum()
                about[ag][i] = float(x[3] > SEUIL_M1[rmax] and x[-1] >= N_MIN)
        motifs = [f3(kH > K_H_MAX), f3(kP < RAPPORT * np.maximum(kH, 1)), f3(~(emd <= RETENUE * macc)), f3(tours > R_PLAFOND)]
        sortie += [f3(br == 1), f3(br == 2), f3(br == 3), f"{np.median(tours[ok]):.0f}" if ok.any() else "-",
                   f"{about['modere'][ok].mean():.2f}" if ok.any() else "-", f"{about['modere_ancre'][ok].mean():.2f}" if ok.any() else "-",
                   f"{np.nanmedian(emd):.4f}", f"{np.nanmedian(macc):.4f}"] + motifs
    return "\t".join(sortie)


def main():
    debut = time.time()
    ss = np.random.SeedSequence()
    gA, gB, gC, gD = ss.spawn(4)
    print(f"entropie SeedSequence : {ss.entropy}")
    print(f"numpy {np.__version__} ; T={T} K={K} K_MIN={K_MIN} ; blocs m={MS} ; niveau par composante {A1:.6f} ; clause {M_MAT} ; candidats {len(CANDIDATS)} ; "
          f"k_H_max={K_H_MAX} rapport={RAPPORT} p_min={P_MIN} surete={SURETE} retenue={RETENUE} plafond de tours (hypothese)={R_PLAFOND} ; seuils M-1 {SEUIL_M1}")
    cells = [(s, r, a, p) for p in ("P0 reference", "P3 ronds 1-2-5") for a in ("dernier", "maximum") for r in RHOS for s in SIGMAS]
    with Pool(4) as pool:
        # ---- A
        print(f"\n# A. variantes de couplage ({len(cells)} cellules)")
        ent = ["sigma", "rho", "ancre", "profil"]
        for m in MS:
            ent += [f"{x}[m={m}]" for x in ("ecart_type_e_honnete", "ecart_type_somme_honnete", "arret_rangs", "arret_lisibilite", "arret_chaine_estimations_nue",
                                            "arret_chaine_estimations_clause", "arret_chaine_rangs_nue", "arret_epreuve(estimations+clause)", "arret_epreuve(rangs)", "moy_e_honnete_pas0", "moy_e_honnete_pas9")]
            for ag in SABOTEURS:
                ent += [f"{x}[m={m},{ag}]" for x in ("exces_mesure_par_action", "exces_vrai_par_action", "signal_sur_bruit")]
        print("\t".join(ent))
        snr, niv = {}, {}
        for l, s_, cle, nv in pool.imap(bloc_A, zip(cells, gA.spawn(len(cells))), chunksize=2):
            print(l)
            snr[cle], niv[cle] = s_, nv
        sys.stdout.flush()
        # ---- choix de m et de la statistique de chaîne (règle écrite d'avance)
        pire = {(m, st): max(niv[cle][(m, st)] for cle in cells) for m in MS for st in ("estimations", "rangs")}
        stat = {m: min(("estimations", "rangs"), key=lambda st: pire[(m, st)]) for m in MS}
        admis = [m for m in MS if pire[(m, stat[m])] <= NIVEAU_MAX]
        crit = {}
        for m in MS:
            v = [0.5 * (snr[cle][(m, "modere")] + snr[cle][(m, "modere_ancre")]) for cle in cells if cle[1] >= 0.5]
            crit[m] = float(np.median(v))
        meilleur = max(crit[m] for m in admis)
        m_ret = max(m for m in admis if crit[m] >= 0.95 * meilleur)
        print(f"\n# CHOIX : pire arret de l'epreuve entiere sur un oracle sain, par (m, statistique de chaine) : "
              f"{ {k_: round(v, 3) for k_, v in pire.items()} } ; statistique par m : {stat} ; m admis (pire arret <= {NIVEAU_MAX}) : {admis}")
        print(f"# CHOIX de m : critere (mediane, cellules a ancrage >= 0,5, du signal sur bruit moyen de modere et modere_ancre) = "
              f"{ {m: round(v, 4) for m, v in crit.items()} } ; retenu m = {m_ret} (le plus grand m admis a moins de 5 % du meilleur admis) ; "
              f"statistique de chaine retenue : {stat[m_ret]}")
        for ag in SABOTEURS:
            print(f"#   signal sur bruit median, cellules a ancrage >= 0,5, {ag} : "
                  + " ; ".join(f"m={m}: {np.median([snr[cle][(m, ag)] for cle in cells if cle[1] >= 0.5]):.3f}" for m in MS))
        couples = [m for m in admis if m < 8]
        m_couple = max(couples, key=lambda m: crit[m]) if couples else None
        a_jouer = list(dict.fromkeys([m_ret, 8] + ([m_couple] if m_couple is not None else [])))
        gBs, gCs, gDs = gB.spawn(len(a_jouer)), gC.spawn(len(a_jouer)), gD.spawn(len(a_jouer))
        for n_m, m_cur in enumerate(a_jouer):
            gB, gC, gD = gBs[n_m], gCs[n_m], gDs[n_m]
            print(f"\n########## BLOCS B, C, D POUR m = {m_cur} ({('retenu par la regle' if m_cur == m_ret else 'non retenu par la regle') + (' ; aucun couplage' if m_cur == 8 else ' ; meilleur bloc couple admis' if m_cur == m_couple else '')}) ##########")
            # ---- B
            res = list(pool.imap(bloc_B, zip([(*cle, m_cur) for cle in cells], gB.spawn(len(cells))), chunksize=2))

            def distingue(tx, i):
                pH, pM = tx["honnete"][i], tx["modere"][i]
                return pH <= K_H_MAX / N_ETAL and pM >= RAPPORT * max(pH, 1.0 / N_ETAL) and pM >= P_MIN

            scores = [sum(distingue(tx, i) for _, tx, _, _, _ in res) for i in range(len(CANDIDATS))]
            best = max(scores)
            i_ret = min((i for i in range(len(CANDIDATS)) if scores[i] == best), key=lambda i: (CANDIDATS[i][0], -CANDIDATS[i][1], CANDIDATS[i][2]))
            cd = CANDIDATS[i_ret]
            print(f"\n# B. regle d'acceptation, m = {m_cur} : nombre de cellules (sur {len(cells)}) ou le maitre modere se distingue de l'honnete, par candidat")
            print("b(facteur)\tF\tN_B_MIN\tcellules_distinguees")
            for i, cdd in enumerate(CANDIDATS):
                print(f"x{10 ** cdd[0]:.1f}\t{cdd[1]}\t{cdd[2]}\t{scores[i]}")
            i_v1 = CANDIDATS.index((math.log10(4.0), 1.0, 7))
            print(f"# CHOIX des constantes : b = log10 {10 ** cd[0]:.1f} = {cd[0]:.5f} ; F = {cd[1]} ; N_B_MIN = {cd[2]} ({best} cellules ; constantes v1 : {scores[i_v1]} cellules)")
            print("\n# B bis. taux d'acceptation par cellule sous les constantes retenues (et, pour memoire, sous celles de la v1)")
            print("\t".join(["sigma", "rho", "ancre", "profil"] + [f"taux_{ag}" for ag in AGENTS] + ["distingue", "exces_vrai_total_des_acceptes_modere",
                             "exces_vrai_total_des_acceptes_modere_ancre", "exces_vrai_total_des_acceptes_joueur", "exces_mesure_moyen_des_acceptes_modere",
                             "ecart_type_entre_episodes_exces_moyen_honnete", "taux_honnete_v1", "taux_modere_v1", "distingue_v1"]))
            table = {}
            for cle, tx, _, sd_h, ex in res:
                table[cle] = (tx["modere"][i_ret], tx["modere_ancre"][i_ret])
                print("\t".join([f"{cle[0]:.2f}", f"{cle[1]:.1f}", cle[2], cle[3]] + [f"{tx[ag][i_ret]:.4f}" for ag in AGENTS]
                                + [str(int(distingue(tx, i_ret))), f"{ex['modere'][i_ret][0]:.3f}", f"{ex['modere_ancre'][i_ret][0]:.3f}",
                                   f"{ex['joueur'][i_ret][0]:.3f}", f"{ex['modere'][i_ret][1]:.4f}", f"{sd_h:.4f}",
                                   f"{tx['honnete'][i_v1]:.4f}", f"{tx['modere'][i_v1]:.4f}", str(int(distingue(tx, i_v1)))]))
            sys.stdout.flush()
            # ---- C
            defs = [("sain", {}), ("decalage d'instrument 0,5 F/T", {"d_shift": 0.05}), ("decalage d'instrument 1 F/T", {"d_shift": 0.10}),
                    ("biais de reecriture 0,5 F/T", {"d_beta": 0.05}), ("biais de reecriture 1 F/T", {"d_beta": 0.10}),
                    ("asymetrie de lecture x2 sur 20 %", {"d_lect_p": 0.20, "d_lect_m": math.log10(2.0)})]
            cC = [(s, r, "dernier", "P0 reference", nom, d, m_cur) for r in (0.5, 0.9) for s in SIGMAS for nom, d in defs]
            print(f"\n# C. epreuve du centrage avec m = {m_cur} (et composante de chaine avec m = 8 pour comparaison) ({len(cC)} cellules)")
            print("\t".join(["sigma", "rho", "ancre", "profil", "etat", "arret_rangs", "arret_lisibilite", "arret_chaine_estimations_nue", "arret_chaine_estimations_clause",
                             "arret_chaine_rangs_nue", "arret_epreuve(estimations+clause)", "arret_epreuve(rangs)", "arret_chaine_estimations_clause[m=8]",
                             "arret_chaine_rangs_nue[m=8]"]))
            for l in pool.imap(bloc_C, zip(cC, gC.spawn(len(cC))), chunksize=4):
                print(l)
            sys.stdout.flush()
            # ---- D
            defD = [("sain", {}), ("decalage d'instrument 1 F/T", {"d_shift": 0.10})]
            cD = [(*cle, etat, d, m_cur, cd, table[cle][0], table[cle][1]) for cle in cells for etat, d in defD]
            print(f"\n# D. etalonnage et branches, m = {m_cur}, constantes retenues ({len(cD)} cellules) ; colonnes [m=8] : memes constantes, sans couplage")
            print("\t".join(["sigma", "rho", "ancre", "profil", "etat", "P(sensibilite passe)", "P(rejet du flagrant passe)", "taux_honnete", "taux_plante",
                             "part_i", "part_ii", "part_iii", "tours_medians", "P(aboutit|part,modere)", "P(aboutit|part,modere_ancre)", "EMD_mediane",
                             "exces_moyen_acceptes_plante", "motif:k_H", "motif:rapport", "motif:puissance", "motif:tours",
                             "P(sensibilite passe)[m=8]", "P(rejet du flagrant passe)[m=8]", "taux_honnete[m=8]", "taux_plante[m=8]"]))
            for l in pool.imap(bloc_D, zip(cD, gD.spawn(len(cD))), chunksize=2):
                print(l)
                sys.stdout.flush()
    print(f"\nduree : {time.time() - debut:.0f} s")


if __name__ == "__main__":
    main()
