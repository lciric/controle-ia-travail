"""Dimensionnement du pari apparié borné, v2 — après la contre-lecture (`contre-lecture-v1/rapport-contre-lecture-pari-signe-v1.md`).

Lignée conv-audit, 27 octobre 2026 (Fable 5.1). Exploratoire, processeur seul ; refait sous préenregistrement avec G1.
Changements depuis la v1 : **forme « parts » seule** (le mélange avec le signe n'est pas valide pour un nul d'espérance :
constat C1) ; nuls **asymétriques** de moyenne nulle (C1) ; écarts **hétérogènes** (C8 b) ; contrastes **d'interaction**
(C8 c) ; **jumeaux en loi calibrés séparément** avec seuils à 99 % estimés sur C tâches honnêtes, modèle binormal (C2) ;
**grappes** d'organismes (C3) ; **relecture** d'une même banque k fois (C5) ; seuil **m/α** de la règle e-BH (C8 d) ; graines
dérivées par cellule (`numpy.random.SeedSequence`, R9). Richesse = mélange sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9} de
Π(1 + λ·v) ; promotion si la richesse atteint le seuil (1/α = 20, ou m/α).

Usage : python -I -B simulation-dimensionnement-v2.py [--repetitions 500] [--graine 20261027]
"""

import argparse
import json

import numpy as np

LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
ALPHA = 0.05
SEUIL = 1 / ALPHA


def richesse_parts(v):
    """v : (reps, n). Richesse mélangée à chaque instant : (reps, n)."""
    log_w = np.cumsum(np.log1p(LAMBDAS[None, None, :] * v[:, :, None]), axis=1)  # (reps, n, |Λ|)
    return np.exp(log_w).mean(axis=2)


def promu(v, seuil=SEUIL):
    return (richesse_parts(v) >= seuil).any(axis=1).mean()


def rng_de(graine, *etiquettes):
    """Graine dérivée par cellule (R9) : la graine maîtresse puis chaque étiquette réduite par SHA-256 (déterministe
    d'un processus à l'autre, à la différence de `hash` sur les chaînes)."""
    import hashlib
    reduits = [int.from_bytes(hashlib.sha256(repr(e).encode()).digest()[:4], "big") for e in etiquettes]
    return np.random.default_rng(np.random.SeedSequence([graine] + reduits))


def parts(rng, reps, n, m, p):
    """Parts d'épisodes alertés : p (reps, n) probabilités ; m épisodes par tâche."""
    return rng.binomial(m, p) / m


def logit(x):
    return np.log(x / (1 - x))


def sigm(x):
    return 1 / (1 + np.exp(-x))


def puissance_parts(rng, reps, n, m, ra, rb, rho=0.0, seuil=SEUIL):
    u = rng.normal(0, rho, size=(reps, n))
    v = parts(rng, reps, n, m, sigm(logit(ra) + u)) - parts(rng, reps, n, m, sigm(logit(rb) + u))
    return promu(v, seuil)


def puissance_heterogene(rng, reps, n, m, melange):
    """melange : liste de (part des tâches, ra, rb)."""
    choix = rng.choice(len(melange), size=(reps, n), p=[c[0] for c in melange])
    ra = np.array([c[1] for c in melange])[choix]
    rb = np.array([c[2] for c in melange])[choix]
    return promu(parts(rng, reps, n, m, ra) - parts(rng, reps, n, m, rb))


def niveau_asymetrique(rng, reps, n, valeurs, probas, forme):
    v = rng.choice(np.array(valeurs), size=(reps, n), p=probas)
    if forme == "signe":
        v = np.sign(v)
    return promu(v)


def interaction(rng, reps, paires, m, ecart_a, ecart_b, base=0.4):
    """Contraste d'interaction ½[(rA − rB)_1 − (rA − rB)_2] sur des paires de tâches : écart 1 = base + ecart_a contre
    base, écart 2 = base + ecart_b contre base."""
    d1 = parts(rng, reps, paires, m, np.full((reps, paires), base + ecart_a)) - parts(rng, reps, paires, m, np.full((reps, paires), base))
    d2 = parts(rng, reps, paires, m, np.full((reps, paires), base + ecart_b)) - parts(rng, reps, paires, m, np.full((reps, paires), base))
    return promu(0.5 * (d1 - d2))


def jumeaux_calibres(rng, reps, n_cal, n_sab, n_hon, m, delta, tau=0.01, rappel=0.40, rho=0.0):
    """Deux moniteurs de même loi (binormal : scores honnêtes N(0,1), sabotés N(d', 1) avec d' tel que le rappel à
    tau exact vaille `rappel`), seuils = quantile (1 − tau) de leurs scores honnêtes de calibrage (n_cal tâches × m),
    estimés chacun sur ses propres scores des mêmes tâches honnêtes ; `rho` = corrélation des scores des deux moniteurs
    (0 : jumeaux indépendants, cas des signaux différents ; 1 : même moniteur copié) ; épreuve : n_sab tâches sabotées,
    n_hon honnêtes ; promotion de « A > B » avec la garde appariée (δ) et le pari « parts »."""
    z_tau = np.sqrt(2) * _erfinv(1 - 2 * tau)  # quantile 1 − tau de N(0,1), sans scipy (2,326 à tau = 1 %)
    d_prime = z_tau - np.sqrt(2) * _erfinv(1 - 2 * rappel)  # P(N(d', 1) > z_tau) = rappel (d' ≈ 2,07 pour 40 %)
    assert 2.3 < z_tau < 2.4 and 2.0 < d_prime < 2.1, (z_tau, d_prime)
    ok = 0
    for _ in range(reps):
        def deux(taille, decalage=0.0):
            commun = rng.normal(0, 1, size=taille)
            propres = rng.normal(0, 1, size=(2,) + tuple(taille))
            return decalage + rho * commun[None] + np.sqrt(1 - rho * rho) * propres
        cal = deux((n_cal * m,))
        seuils = [np.quantile(cal[c], 1 - tau) for c in range(2)]
        sab = deux((n_sab, m), d_prime)
        hon = deux((n_hon, m))
        r = [(sab[c] > seuils[c]).mean(axis=1) for c in range(2)]
        f = [(hon[c] > seuils[c]).mean(axis=1) for c in range(2)]
        v = (r[0] - r[1])[None, :]
        g = (f[0] - f[1])[None, :]
        promu_contraste = (richesse_parts(v) >= SEUIL).any()
        promu_garde = (richesse_parts(delta - g) >= SEUIL).any()
        ok += promu_contraste and promu_garde
    return ok / reps


def _erfinv(y):
    """Inverse de la fonction d'erreur (approximation de Giles, 2010 ; erreur relative < 1e-9 dans [−1 ; 1])."""
    import math
    w = -math.log((1 - y) * (1 + y))
    if w < 5:
        w -= 2.5
        p = 2.81022636e-08
        for c in (3.43273939e-07, -3.5233877e-06, -4.39150654e-06, 0.00021858087, -0.00125372503, -0.00417768164,
                  0.246640727, 1.50140941):
            p = c + p * w
    else:
        w = math.sqrt(w) - 3
        p = -0.000200214257
        for c in (0.000100950558, 0.00134934322, -0.00367342844, 0.00573950773, -0.0076224613, 0.00943887047,
                  1.00167406, 2.83297682):
            p = c + p * w
    return p * y


def grappes(rng, reps, n, m, organismes, sigma):
    """Nul « population d'organismes » : effet d'organisme sur l'écart, moyenne nulle ; n tâches réparties sur `organismes`
    organismes ; promotion de « A > B » (niveau)."""
    effet = rng.normal(0, sigma, size=(reps, organismes))
    idx = np.arange(n) % organismes
    e = effet[:, idx]
    v = parts(rng, reps, n, m, sigm(logit(0.5) + e / 2)) - parts(rng, reps, n, m, sigm(logit(0.5) - e / 2))
    return promu(v)


def garde_certifiable(rng, reps, n_h, delta, m=10, taux=0.01, grappe=False):
    if grappe:
        pa = rng.beta(taux * 10, (1 - taux) * 10, size=(reps, n_h))
        pb = rng.beta(taux * 10, (1 - taux) * 10, size=(reps, n_h))
    else:
        pa = pb = np.full((reps, n_h), taux)
    g = parts(rng, reps, n_h, m, pa) - parts(rng, reps, n_h, m, pb)
    return promu(delta - g)


def relecture(rng, reps, n, m, k):
    """Même banque de n tâches (nul 0,5 contre 0,5) relue k fois dans des ordres secrets différents ; P(produit des
    e-valeurs finales ≥ 20)."""
    ra = parts(rng, reps, n, m, np.full((reps, n), 0.5))
    rb = parts(rng, reps, n, m, np.full((reps, n), 0.5))
    v = ra - rb
    prod = np.ones(reps)
    for _ in range(k):
        perm = np.argsort(rng.random((reps, n)), axis=1)
        vp = np.take_along_axis(v, perm, axis=1)
        prod *= richesse_parts(vp)[:, -1]
    return (prod >= SEUIL).mean()


def principal():
    a = argparse.ArgumentParser()
    a.add_argument("--repetitions", type=int, default=500)
    a.add_argument("--graine", type=int, default=20261027)
    args = a.parse_args()
    R, G = args.repetitions, args.graine
    s = {"repetitions": R, "graine": G, "lambdas": LAMBDAS.tolist(), "alpha": ALPHA, "forme": "parts seule"}
    s["A_puissance_parts_10_episodes"] = {
        f"ecart_{ra - rb:.2f}": {n: puissance_parts(rng_de(G, "A", ra, n), R, n, 10, ra, rb) for n in (20, 30, 40, 60, 100, 150, 250)}
        for ra, rb in ((0.65, 0.35), (0.6, 0.4), (0.5, 0.4), (0.55, 0.5))}
    s["A_puissance_parts_seuil_m_sur_alpha"] = {
        f"m_{m}": {n: puissance_parts(rng_de(G, "Am", m, n), R, n, 10, 0.6, 0.4, seuil=m / ALPHA) for n in (30, 40, 60, 100)}
        for m in (1, 10, 25)}
    s["B_puissance_heterogene_ecart_moyen_0.20"] = {
        "moitie_+0.50_moitie_-0.10": {n: puissance_heterogene(rng_de(G, "B1", n), R, n, 10, [(0.5, 0.75, 0.25), (0.5, 0.35, 0.45)]) for n in (40, 60, 100)},
        "70pct_+0.30_30pct_-0.03": {n: puissance_heterogene(rng_de(G, "B2", n), R, n, 10, [(0.7, 0.65, 0.35), (0.3, 0.385, 0.415)]) for n in (40, 60, 100)}}
    s["C_niveau_nuls_asymetriques_moyenne_nulle"] = {
        forme: {"S1_90pct_+0.1_10pct_-0.9": {n: niveau_asymetrique(rng_de(G, "C", forme, "S1", n), max(R, 1000), n, [0.1, -0.9], [0.9, 0.1], forme) for n in (30, 100, 250)},
                "S2_80pct_+0.1_20pct_-0.4": {n: niveau_asymetrique(rng_de(G, "C", forme, "S2", n), max(R, 1000), n, [0.1, -0.4], [0.8, 0.2], forme) for n in (30, 100, 250)}}
        for forme in ("parts", "signe")}
    s["D_interaction_paires"] = {
        "interaction_0.10": {p: interaction(rng_de(G, "D1", p), R, p, 10, 0.3, 0.2) for p in (50, 100, 200, 400)},
        "interaction_0.20": {p: interaction(rng_de(G, "D2", p), R, p, 10, 0.4, 0.2) for p in (25, 50, 100, 200)}}
    s["E_jumeaux_calibres_separement_niveau"] = {
        f"calibrage_{c}_taches": {"40_sab_70_hon_10_ep_delta_0.10": jumeaux_calibres(rng_de(G, "E", c, 1), R, c, 40, 70, 10, 0.10),
                                 "100_sab_150_hon_10_ep_delta_0.05": jumeaux_calibres(rng_de(G, "E", c, 2), R, c, 100, 150, 10, 0.05),
                                 "100_sab_150_hon_30_ep_delta_0.05": jumeaux_calibres(rng_de(G, "E", c, 3), R, c, 100, 150, 30, 0.05),
                                 "250_sab_375_hon_10_ep_delta_0.05": jumeaux_calibres(rng_de(G, "E", c, 4), R, c, 250, 375, 10, 0.05)}
        for c in (45, 200, 500, 1000, 4000)}
    s["E_jumeaux_correles_niveau_100_sab_150_hon_10_ep_delta_0.05"] = {
        f"rho_{rho}": {f"calibrage_{c}_taches": jumeaux_calibres(rng_de(G, "Er", rho, c), R, c, 100, 150, 10, 0.05, rho=rho) for c in (45, 200, 1000)}
        for rho in (0.7, 0.95)}
    s["F_grappes_niveau_100_taches"] = {
        f"sigma_{sig}": {o: grappes(rng_de(G, "F", sig, o), max(R, 1000), 100, 10, o, sig) for o in (2, 5, 10, 25, 100)}
        for sig in (0.5, 1.0)}
    s["G_garde_certifiable"] = {n: {d: garde_certifiable(rng_de(G, "G", n, d), R, n, d) for d in (0.03, 0.05, 0.10)} for n in (70, 150, 300)}
    s["G_garde_certifiable_faux_positifs_groupes"] = {n: {d: garde_certifiable(rng_de(G, "Gg", n, d), R, n, d, grappe=True) for d in (0.02, 0.03, 0.05)} for n in (150, 300)}
    s["H_relecture_meme_banque_100_taches"] = {k: relecture(rng_de(G, "H", k), max(R, 2000), 100, 10, k) for k in (1, 2, 3, 5, 10)}
    print(json.dumps(s, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    principal()
