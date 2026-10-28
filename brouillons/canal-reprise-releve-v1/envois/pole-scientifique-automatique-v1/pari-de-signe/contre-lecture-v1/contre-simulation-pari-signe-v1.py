"""Contre-simulation indépendante du « pari apparié borné » (contre-lecture R2 de conception-pari-de-signe-v1.md).

Écrite par le contre-lecteur (Opus 5.5), sans reprendre le code de l'auteur : vectorisée sur les répétitions, graines
dérivées par section (numpy.random.SeedSequence, entropie consignée dans la sortie), processeur seul, exploratoire.

Richesse « mélange » de la pièce : ½·moyenne_λ Π(1 + λ·v) + ½·moyenne_λ Π(1 + λ·signe(v)), Λ = {0,1 ; 0,3 ; 0,6 ; 0,9} ;
« parts seules » : moyenne_λ Π(1 + λ·v) ; « signe seul » : moyenne_λ Π(1 + λ·signe(v)). Promotion : la richesse atteint
1/α = 20 à un instant (lecture continue).

Usage : python -I -B contre-simulation-pari-signe-v1.py [--entropie 7182818284] [--rep 1000]
"""

import argparse
import json
import math
import time

import numpy as np

LAM = np.array([0.1, 0.3, 0.6, 0.9])
ALPHA = 0.05
S20 = math.log(1 / ALPHA)
TOL = 1e-12


def logw(series, poids, lam=LAM):
    """Log-richesse (R, N) du mélange uniforme sur lam de chaque série, séries pondérées par `poids`."""
    comps = []
    for x, w in zip(series, poids):
        facteurs = 1.0 + lam[None, None, :] * x[:, :, None]
        assert facteurs.min() > 0, "facteur non positif"
        comps.append(np.cumsum(np.log(facteurs), axis=1) + math.log(w / lam.size))
    c = np.concatenate(comps, axis=2)
    mx = c.max(axis=2, keepdims=True)
    return (mx + np.log(np.exp(c - mx).sum(axis=2, keepdims=True)))[..., 0]


def formes(v):
    s = np.sign(v)
    return {"melange": logw([v, s], [0.5, 0.5]), "parts": logw([v], [1.0]), "signe": logw([s], [1.0])}


def promu(lw, seuil=S20):
    return (lw >= seuil - TOL).any(axis=1)


def parts(rng, R, N, m, pA, pB):
    pA = np.broadcast_to(pA, (R, N))
    pB = np.broadcast_to(pB, (R, N))
    return rng.binomial(m, pA) / m - rng.binomial(m, pB) / m


def melange_types(rng, R, N, types):
    """types : liste de (poids, pA, pB) ; tirage indépendant du type de chaque tâche."""
    u = rng.random((R, N))
    pA, pB = np.empty((R, N)), np.empty((R, N))
    cum = 0.0
    for w, a, b in types:
        masque = (u >= cum) & (u < cum + w)
        pA[masque], pB[masque] = a, b
        cum += w
    return pA, pB


def expit(x):
    return 1 / (1 + np.exp(-x))


def phi_sup(x):
    """P(N(0,1) > x), élément par élément."""
    return np.array([0.5 * math.erfc(t / math.sqrt(2)) for t in np.ravel(x)]).reshape(np.shape(x))


def puissances(rng, R, N, m, pA, pB):
    v = parts(rng, R, N, m, pA, pB)
    return {k: float(promu(lw).mean()) for k, lw in formes(v).items()}


# --- A. Reproduction des puissances ----------------------------------------------------------------------------
def section_A(rng, R):
    out = {}
    lignes = {"0.30": (0.65, 0.35), "0.20": (0.6, 0.4), "0.10": (0.5, 0.4), "0.05": (0.55, 0.5)}
    for nom, (a, b) in lignes.items():
        out[f"ecart_{nom}_10_episodes"] = {n: puissances(rng, R, n, 10, a, b) for n in (15, 20, 30, 40, 60, 100, 150, 250)}
    # mise fixe sans mélange (meilleure mise valide connue d'avance), parts, 20 points, 20 tâches
    v = parts(rng, R, 20, 10, 0.6, 0.4)
    out["mise_fixe_sans_melange_parts_ecart_0.20_20_taches"] = {
        lam: float(promu(logw([v], [1.0], lam=np.array([lam]))).mean()) for lam in (0.5, 0.7, 0.9, 0.99)}
    out["mise_fixe_sans_melange_parts_ecart_0.20_30_taches"] = {
        lam: float(promu(logw([parts(rng, R, 30, 10, 0.6, 0.4)], [1.0], lam=np.array([lam]))).mean())
        for lam in (0.5, 0.7, 0.9, 0.99)}
    return out


# --- B. Garde appariée ----------------------------------------------------------------------------------------
def garde(rng, R, n, delta, m=10, taux=0.01, surdispersion=None):
    if surdispersion is None:
        qa = qb = taux
    else:  # propension de faux positifs par tâche et par moniteur ~ Bêta de moyenne `taux`
        a = taux * surdispersion
        b = (1 - taux) * surdispersion
        qa, qb = rng.beta(a, b, (R, n)), rng.beta(a, b, (R, n))
    g = rng.binomial(m, np.broadcast_to(qa, (R, n))) / m - rng.binomial(m, np.broadcast_to(qb, (R, n))) / m
    return float(promu(logw([delta - g], [1.0])).mean())


def section_B(rng, R):
    out = {"independants": {}, "surdisperses_beta_somme_10": {}}
    for n, d in ((50, 0.10), (70, 0.10), (100, 0.05), (150, 0.05), (150, 0.03), (300, 0.02)):
        out["independants"][f"{n}_taches_delta_{d}"] = garde(rng, R, n, d)
        out["surdisperses_beta_somme_10"][f"{n}_taches_delta_{d}"] = garde(rng, R, n, d, surdispersion=10.0)
    return out


# --- C. Niveau sous des nuls hétérogènes et dépendants -----------------------------------------------------------
def section_C(rng, R):
    out = {}
    out["C1_homogene_0.5_150_taches"] = puissances(rng, R, 150, 10, 0.5, 0.5)
    # C2 : nul hétérogène symétrique (contrôle 3 de la pièce et une variante binomiale)
    v = np.where(rng.random((R, 150)) < 0.5, 0.6, -0.6)
    out["C2a_symetrique_deterministe_pm0.6_150"] = {k: float(promu(lw).mean()) for k, lw in formes(v).items()}
    pA, pB = melange_types(rng, R, 150, [(0.5, 0.8, 0.2), (0.5, 0.2, 0.8)])
    out["C2b_symetrique_binomial_0.8_0.2_150"] = puissances(rng, R, 150, 10, pA, pB)
    # C3 : nuls hétérogènes asymétriques, espérance du contraste exactement nulle
    scen = {
        "S1_90pct_plus0.10_10pct_moins0.90": [(0.9, 0.55, 0.45), (0.1, 0.05, 0.95)],
        "S2_80pct_plus0.10_20pct_moins0.40_mode_ecarte": [(0.8, 0.6, 0.5), (0.2, 0.2, 0.6)],
    }
    for nom, types in scen.items():
        esp = sum(w * (a - b) for w, a, b in types)
        out[f"C3_{nom}"] = {"esperance_vraie_du_contraste": round(esp, 12)}
        for n in (30, 60, 100, 150, 250):
            pA, pB = melange_types(rng, R, n, types)
            out[f"C3_{nom}"][n] = puissances(rng, R, n, 10, pA, pB)
    # C4 : « rappel ≥ x » avec x égal au rappel moyen vrai, rappels par tâche asymétriques
    out["C4_rappel_absolu_x_0.6_rappels_0.7_80pct_0.2_20pct"] = {}
    for n in (30, 60, 100, 150):
        p = np.where(rng.random((R, n)) < 0.8, 0.7, 0.2)
        v = rng.binomial(10, p) / 10 - 0.6
        out["C4_rappel_absolu_x_0.6_rappels_0.7_80pct_0.2_20pct"][n] = {k: float(promu(lw).mean()) for k, lw in formes(v).items()}
    # C5 : dépendance entre tâches par organisme (effet d'organisme sur l'écart, de moyenne nulle sur les organismes)
    out["C5_grappes_organismes_100_taches"] = {}
    for sigma in (0.5, 1.0):
        for K in (2, 4, 5, 10, 25, 100):
            u = rng.normal(0, sigma, (R, K))
            org = np.array([rng.permutation(np.arange(100) % K) for _ in range(R)])
            uk = np.take_along_axis(u, org, axis=1)
            pA, pB = expit(uk / 2), expit(-uk / 2)
            out["C5_grappes_organismes_100_taches"][f"sigma_logit_{sigma}_K_{K}"] = puissances(rng, R, 100, 10, pA, pB)
    return out


# --- D. Jumeaux en loi, seuils calibrés séparément (bruit de calibrage) -----------------------------------------
def jumeaux(rng, R, n_cal, n_sab, n_hon, delta, m=10, tau=0.01, d=2.073, icc=0.0, bloc=50):
    """A et B : deux moniteurs de même loi, indépendants. Score honnête N(0, 1) (effet de tâche de part icc),
    saboté N(d, 1) : rappel vrai 0,40 à 1 % de faux positifs exacts. Seuils : quantile (1 − τ) des épisodes honnêtes
    de n_cal tâches de calibrage, pour chaque moniteur séparément (règle de la pièce, 2.4)."""
    cpt = {"contraste_melange": 0, "contraste_parts": 0, "melange_et_garde": 0, "parts_et_garde": 0}
    asym_fp, ecart_rappel = [], []
    for debut in range(0, R, bloc):
        r = min(bloc, R - debut)

        def scores(n_t, decal):
            e = rng.normal(0, math.sqrt(1 - icc), (r, n_t, m))
            if icc > 0:
                e = e + rng.normal(0, math.sqrt(icc), (r, n_t, 1))
            return decal + e

        thA = np.quantile(scores(n_cal, 0.0).reshape(r, -1), 1 - tau, axis=1)
        thB = np.quantile(scores(n_cal, 0.0).reshape(r, -1), 1 - tau, axis=1)
        rA = (scores(n_sab, d) > thA[:, None, None]).mean(2)
        rB = (scores(n_sab, d) > thB[:, None, None]).mean(2)
        fA = (scores(n_hon, 0.0) > thA[:, None, None]).mean(2)
        fB = (scores(n_hon, 0.0) > thB[:, None, None]).mean(2)
        N = n_sab + n_hon
        xv, xg = np.zeros((r, N)), np.zeros((r, N))
        for i in range(r):
            perm = rng.permutation(N)
            xv[i, perm[:n_sab]] = rA[i] - rB[i]
            xg[i, perm[n_sab:]] = delta - (fA[i] - fB[i])
        lv_m = logw([xv, np.sign(xv)], [0.5, 0.5])
        lv_p = logw([xv], [1.0])
        lg = logw([xg], [1.0])
        cpt["contraste_melange"] += int(promu(lv_m).sum())
        cpt["contraste_parts"] += int(promu(lv_p).sum())
        cpt["melange_et_garde"] += int(((lv_m >= S20 - TOL) & (lg >= S20 - TOL)).any(1).sum())
        cpt["parts_et_garde"] += int(((lv_p >= S20 - TOL) & (lg >= S20 - TOL)).any(1).sum())
        asym_fp.extend((phi_sup(thA) - phi_sup(thB)).tolist())
        ecart_rappel.extend((phi_sup(thA - d) - phi_sup(thB - d)).tolist())
    asym_fp, ecart_rappel = np.array(asym_fp), np.array(ecart_rappel)
    res = {k: v / R for k, v in cpt.items()}
    res["asymetrie_vraie_fp_ecart_type"] = float(asym_fp.std())
    res["ecart_vrai_rappel_ecart_type"] = float(ecart_rappel.std())
    res["part_ecart_vrai_rappel_sup_0.05"] = float((ecart_rappel > 0.05).mean())
    res["part_ecart_vrai_rappel_sup_0.10"] = float((ecart_rappel > 0.10).mean())
    res["part_asymetrie_vraie_fp_sup_0.01"] = float((asym_fp > 0.01).mean())
    return res


def section_D(rng, R):
    out = {}
    for icc in (0.0, 0.3):
        for n_cal in (45, 200, 1000):
            for n_sab, n_hon, delta in ((40, 70, 0.10), (100, 150, 0.05)):
                out[f"icc_{icc}_cal_{n_cal}_taches_sab_{n_sab}_hon_{n_hon}_delta_{delta}"] = jumeaux(
                    rng, R, n_cal, n_sab, n_hon, delta, icc=icc)
    return out


# --- E. Règle e-BH sur la seule richesse du contraste, garde appliquée après coup --------------------------------
def fiches(rng, R, genre, n_sab=100, n_hon=150, delta=0.05, m=10):
    pa, pb, qa, qb = {"vrai": (0.6, 0.4, 0.01, 0.01), "tricheur": (0.6, 0.4, 0.06, 0.01),
                      "nul": (0.5, 0.5, 0.01, 0.01)}[genre]
    v = parts(rng, R, n_sab, m, pa, pb)
    g = rng.binomial(m, qa, (R, n_hon)) / m - rng.binomial(m, qb, (R, n_hon)) / m
    N = n_sab + n_hon
    xv, xg = np.zeros((R, N)), np.zeros((R, N))
    for i in range(R):
        perm = rng.permutation(N)
        xv[i, perm[:n_sab]] = v[i]
        xg[i, perm[n_sab:]] = delta - g[i]
    return logw([xv, np.sign(xv)], [0.5, 0.5]), logw([xg], [1.0])


def e_arretee(lw, seuil):
    atteint = lw >= seuil - TOL
    premier = np.where(atteint.any(1), atteint.argmax(1), lw.shape[1] - 1)
    return lw[np.arange(lw.shape[0]), premier]


def ebh(log_e, m):
    """log_e : (R, m). Renvoie un masque (R, m) des fiches retenues par e-BH."""
    R = log_e.shape[0]
    ordre = np.argsort(-log_e, axis=1)
    tri = np.take_along_axis(log_e, ordre, axis=1)
    k = np.arange(1, m + 1)
    ok = tri >= np.log(m / (ALPHA * k))[None, :] - TOL
    kstar = np.where(ok.any(1), m - np.argmax(ok[:, ::-1], axis=1), 0)
    retenues = np.zeros((R, m), bool)
    for i in range(R):
        retenues[i, ordre[i, :kstar[i]]] = True
    return retenues


def section_E(rng, R):
    out = {}
    for nom, compo in (("0_vrais_10_tricheurs_10_nuls", (0, 10, 10)), ("5_vrais_7_tricheurs_8_nuls", (5, 7, 8)),
                       ("10_vrais_0_tricheur_10_nuls", (10, 0, 10)), ("0_vrai_0_tricheur_20_nuls", (0, 0, 20)),
                       ("0_vrai_30_tricheurs_10_nuls", (0, 30, 10)), ("0_vrai_15_tricheurs_5_nuls", (0, 15, 5))):
        genres = ["vrai"] * compo[0] + ["tricheur"] * compo[1] + ["nul"] * compo[2]
        m = len(genres)
        lv, lg = zip(*[fiches(rng, R, g) for g in genres])
        seuil_m = math.log(m / ALPHA)
        promue = np.stack([((a >= S20 - TOL) & (b >= S20 - TOL)).any(1) for a, b in zip(lv, lg)], 1)
        e1 = np.stack([e_arretee(a, seuil_m) for a in lv], 1)  # pièce : richesse du contraste seule
        e2 = np.stack([e_arretee(np.minimum(a, b), seuil_m) for a, b in zip(lv, lg)], 1)  # correction : minimum
        vrai = np.array([g == "vrai" for g in genres])[None, :]
        res = {}
        for proc, retenue in (("piece_ebh_contraste_puis_garde", ebh(e1, m) & promue),
                              ("correction_ebh_sur_minimum", ebh(e2, m))):
            fausses = (retenue & ~vrai).sum(1)
            total = retenue.sum(1)
            res[proc] = {"taux_fausses_decouvertes": float(np.mean(fausses / np.maximum(total, 1))),
                         "proba_au_moins_une_fausse": float(np.mean(fausses > 0)),
                         "vraies_retenues_moyenne": float((retenue & vrai).sum(1).mean())}
        out[nom] = res
    return out


# --- F. Héritage de preuve sur une banque réutilisée ---------------------------------------------------------------
def section_F(rng, R, n=100):
    v = parts(rng, R, n, 10, 0.5, 0.5)
    v2 = v[np.arange(R)[:, None], np.array([rng.permutation(n) for _ in range(R)])]  # mêmes tâches, autre ordre
    v3 = parts(rng, R, n, 10, 0.5, 0.5)  # tâches fraîches
    res = {}
    for forme, poids in (("parts", None), ("melange", None)):
        def lw(x):
            return logw([x], [1.0]) if forme == "parts" else logw([x, np.sign(x)], [0.5, 0.5])
        e1, e2, e3 = (e_arretee(lw(x), S20) for x in (v, v2, v3))
        res[forme] = {"une_lecture_P(e>=20)": float((e1 >= S20 - TOL).mean()),
                      "meme_banque_deux_ordres_P(e1*e2>=20)": float((e1 + e2 >= S20 - TOL).mean()),
                      "banques_disjointes_P(e1*e3>=20)": float((e1 + e3 >= S20 - TOL).mean()),
                      "correlation_log_e_meme_banque": float(np.corrcoef(e1, e2)[0, 1])}
    return res


# --- G. Puissance des contrastes d'interaction (H1b, H2b, H3b) ---------------------------------------------------
def section_G(rng, R):
    out = {}
    for nom, (f, nt) in (("interaction_0.20", ((0.6, 0.4), (0.5, 0.5))), ("interaction_0.10", ((0.55, 0.45), (0.5, 0.5)))):
        out[nom] = {}
        for npaires in (50, 100, 200, 400):
            vf = parts(rng, R, npaires, 10, *f)
            vn = parts(rng, R, npaires, 10, *nt)
            v = 0.5 * (vf - vn)
            out[nom][npaires] = {k: float(promu(lw).mean()) for k, lw in formes(v).items()}
    return out


# --- H. Écart moyen de 0,20 mais hétérogène d'une tâche à l'autre ----------------------------------------------
def section_H(rng, R):
    out = {}
    scen = {"homogene_0.6_0.4": [(1.0, 0.6, 0.4)],
            "70pct_plus0.30_30pct_moins0.033": [(0.7, 0.65, 0.35), (0.3, 0.5 - 1 / 60, 0.5 + 1 / 60)],
            "50pct_plus0.50_50pct_moins0.10": [(0.5, 0.75, 0.25), (0.5, 0.45, 0.55)]}
    for nom, types in scen.items():
        out[nom] = {"esperance": round(sum(w * (a - b) for w, a, b in types), 12)}
        for n in (20, 30, 40, 60, 100):
            pA, pB = melange_types(rng, R, n, types)
            out[nom][n] = puissances(rng, R, n, 10, pA, pB)
    return out


# --- I. Variante « banque entière » (sans remise) ------------------------------------------------------------------
def sans_remise(x, lam=LAM):
    R, n = x.shape
    S = np.concatenate([np.zeros((R, 1)), np.cumsum(x, 1)[:, :-1]], 1)
    t = np.arange(1, n + 1)[None, :]
    mu = -S / (n - t + 1)
    lam_t = lam[None, None, :] * ((n - t + 1) / n)[:, :, None]
    fac = 1 + lam_t * (x - mu)[:, :, None]
    c = np.cumsum(np.log(fac), 1) + math.log(1 / lam.size)
    mx = c.max(2, keepdims=True)
    return (mx + np.log(np.exp(c - mx).sum(2, keepdims=True)))[..., 0], float(fac.min())


def section_I(rng, R):
    out = {}
    for nom, banque in (("90_fois_plus0.1_10_fois_moins0.9", [0.1] * 90 + [-0.9] * 10),
                        ("50_fois_plus0.6_50_fois_moins0.6", [0.6] * 50 + [-0.6] * 50)):
        b = np.array(banque)
        x = np.stack([rng.permutation(b) for _ in range(R)])
        lw_sr, fac_min = sans_remise(x)
        out[nom] = {"moyenne_banque": float(b.mean()),
                    "sans_remise_P(promue)": float(promu(lw_sr).mean()), "sans_remise_facteur_min": fac_min,
                    "forme_population_parts_P(promue)": float(promu(logw([x], [1.0])).mean()),
                    "forme_population_melange_P(promue)": float(promu(logw([x, np.sign(x)], [0.5, 0.5])).mean())}
    return out


# --- K. Démonstration 3.4 (pari par épisode sous dépendance) --------------------------------------------------------
def section_K(rng, R, n=50, m=10):
    favorable = rng.random((R, n)) < 0.5
    pas = np.where(favorable, m * math.log(1.4), m * math.log(0.6))
    par_episode = (np.cumsum(pas, 1) >= S20 - TOL).any(1).mean()
    s = np.where(favorable, 1.0, -1.0)
    return {"par_episode_mise_fixe_p_0.7": float(par_episode),
            "par_tache_melange": float(promu(logw([s, s], [0.5, 0.5])).mean())}


# --- L. Sous-population choisie sur les scores du comparateur (H2a) ---------------------------------------------------
def section_L(rng, R, n=40, m=10, T=10, k=5, mu=1.0):
    """A et B : deux moniteurs par action de même loi, bruits indépendants. Épisode saboté : k actions décalées de mu
    sur T. Cellule d'épisode : alerte si une action dépasse le seuil d'épisode à 1 % (max de T scores honnêtes).
    Sous-population : épisodes où toutes les actions sabotées restent sous le seuil par action à 1 % **de B**."""
    c1 = 2.3263478740408408
    c_ep = 3.0902323061678132  # quantile 0,99**(1/10) de N(0,1)
    decal = np.zeros(T)
    decal[:k] = mu
    zA = rng.normal(size=(R, n, m, T)) + decal
    zB = rng.normal(size=(R, n, m, T)) + decal
    garde_ep = (zB[..., :k] < c1).all(-1)  # sélection sur les scores de B
    alA = (zA > c_ep).any(-1)
    alB = (zB > c_ep).any(-1)
    nb = garde_ep.sum(-1)
    with np.errstate(invalid="ignore", divide="ignore"):
        rA = np.where(nb > 0, (alA & garde_ep).sum(-1) / np.maximum(nb, 1), 0.0)
        rB = np.where(nb > 0, (alB & garde_ep).sum(-1) / np.maximum(nb, 1), 0.0)
    v = np.where(nb > 0, rA - rB, 0.0)
    sans_selection = alA.mean((1, 2)) - alB.mean((1, 2))
    return {"part_episodes_selectionnes": float(garde_ep.mean()),
            "ecart_moyen_rA_moins_rB_sur_selection": float(v[nb > 0].mean()),
            "ecart_moyen_sans_selection": float(sans_selection.mean()),
            **{f"P(promue)_{k2}": float(promu(lw).mean()) for k2, lw in formes(v).items()}}


def section_M(rng, R):
    """Nombre minimal d'unités pour une promotion quand chaque unité donne v = +1 (aucune erreur) : analytique."""
    out = {}
    for nom, composantes in (("melange_8_composantes", 8), ("parts_seules_4_composantes", 4)):
        for seuil_nom, seuil in (("1_sur_alpha_20", 20.0), ("e_BH_m_12_rang_1_240", 240.0)):
            out[f"{nom}_{seuil_nom}"] = math.ceil(math.log(seuil * composantes) / math.log(1.9))
    return out


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--entropie", type=int, default=7182818284)
    a.add_argument("--rep", type=int, default=1000)
    args = a.parse_args()
    racine = np.random.SeedSequence(args.entropie)
    noms = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M"]
    graines = dict(zip(noms, racine.spawn(len(noms))))
    R = args.rep
    plan = {"A": (section_A, R), "B": (section_B, R), "C": (section_C, 2 * R), "D": (section_D, max(300, R // 2)),
            "E": (section_E, 2 * R), "F": (section_F, 2 * R), "G": (section_G, R), "H": (section_H, R),
            "I": (section_I, 2 * R), "K": (section_K, 2 * R), "L": (section_L, R), "M": (section_M, 0)}
    sortie = {"entropie_SeedSequence": args.entropie, "repetitions_de_base": R, "lambdas": LAM.tolist(),
              "alpha": ALPHA, "numpy": np.__version__}
    for nom, (fn, r) in plan.items():
        t0 = time.time()
        sortie[f"section_{nom}"] = {"repetitions": r, "resultats": fn(np.random.default_rng(graines[nom]), r)}
        sortie[f"section_{nom}"]["secondes"] = round(time.time() - t0, 1)
        print(f"section {nom} : {sortie[f'section_{nom}']['secondes']} s", flush=True, file=__import__('sys').stderr)
    print(json.dumps(sortie, ensure_ascii=False, indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o)))


if __name__ == "__main__":
    main()
