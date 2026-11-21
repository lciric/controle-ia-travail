#!/usr/bin/env python3
"""Calculs d'illustration pour la note « boucle audit après coup, recapture, réapprentissage » (Opus 5.5, v1).

Nature : mondes plantés jouets, sur processeur, aucune donnée du programme, aucun appel payant.
Classe C : illustration d'un argument, NON décisive ; tout chiffre se lit « sous supposition ».
Auteur : Claude Opus 5.5 (claude-opus-5-5), 21 novembre 2026, écrit avant toute exécution.

Suppositions communes (toutes d'illustration) :
- un épisode est résumé par un vecteur d'état interne x de dimension d = 32 (d = 4096 en formule seulement) ;
- l'honnête suit N(0, I) ; un sabotage déplace la moyenne le long de directions fixes (intention commune u0,
  directions propres aux familles) ; un échec honnête déplace le long d'une direction f ;
- les sondes sont linéaires (différence de moyennes, ou régression logistique à pénalité L2), lues par épisode ;
- l'oracle voit une famille avec probabilité q (1 ou 0 selon la famille), sans erreur par ailleurs ;
- le taux de fausses alertes de chaque sonde est fixé à 1 % sur des témoins honnêtes exogènes neufs.

PRÉDICTIONS, écrites avant l'exécution et scellées avec ce fichier :
A1. Rappel jugé sur les positifs d'apprentissage (rétrospectif ; différence de moyennes ; 10 positifs ; d = 32 ;
    écart 2) ≈ 0,6 ; rappel prospectif (épisodes neufs) ≈ 0,2 ; rapport >= 2.
A2. Rappel prospectif selon le nombre de positifs (formule et simulation d'accord à ±0,03) : 3 -> ≈ 0,10 ;
    10 -> ≈ 0,20 ; 30 -> ≈ 0,29 ; 100 -> ≈ 0,34 ; plafond ≈ 0,37. En dimension 4096 (formule) : <= 0,05
    jusqu'à 100 positifs.
B1. Famille que l'oracle ne voit pas (q = 0) : sonde d'origine ≈ 0,37 ; réapprise saine (négatifs exogènes)
    ≈ 0,10 à 0,20 ; réapprise avec négatifs pris chez le suspect audité sans dommage <= 0,10 et sous la saine
    d'au moins 0,05 ; union (origine + saine) ≈ 0,3.
B2. Famille que l'oracle voit : les deux réapprises >= 0,45 ; origine ≈ 0,37.
C1. Régime d'excès, probabilité qu'un saboté soit noté au-dessus d'un échec honnête : réapprise sur positifs
    mêlés ≈ 0,55 (<= 0,62) ; contraste contre échecs honnêtes ≈ 0,55 à 0,68 ; transfert depuis une famille de
    signature >= 0,72.
D1. Recapture de l'ancienne sonde : naïve sur tous les audités (audit orienté compris) ≈ 0,9 ; pondérée par
    l'inverse de la probabilité d'audit ≈ vérité ≈ 0,29 (±0,05).
D2. Famille que l'ancienne sonde manque : rappel après réapprentissage non pondéré sous le pondéré d'au moins
    0,05 ; pondéré ≈ plancher seul.
E1. Étiquettes attendues avant K au taux minimal de la table (p·q = 1 − 0,05^(1/K)) : 2,85 ; 2,95 ; 2,98 ;
    2,99 (K = 30, 100, 300, 1000) ; P(>= 10 étiquettes) <= 0,01 ; au triple du taux, P(>= 10) ≈ 0,4.
F1. Malédiction du gagnant : 10 versions de même rappel 0,2, jugées sur 15 épisodes endommagés : relevé du
    choisi ≈ 0,35 ; son relevé postérieur au choix ≈ 0,20.
G1. Gardes : journal sain -> toutes vertes ; chaque artefact planté -> la garde visée rouge, les autres vertes.

Règle de lecture : un résultat contraire à une prédiction est rapporté tel quel ; aucun paramètre n'est changé
après exécution (R3, R4).
"""
import hashlib
import math
import platform
import sys

import numpy as np
from numpy.random import SeedSequence, default_rng

RACINE = 202611211648  # graine racine, consignée
D = 32
Z99 = 2.3263478740408408  # quantile 0,99 de la loi normale


# ---------------------------------------------------------------- outils
def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def directions(rng, d, k):
    q, _ = np.linalg.qr(rng.standard_normal((d, k)))
    return [q[:, i].copy() for i in range(k)]


def logreg(X, y, sw=None, lam=1.0, iters=50):
    """Régression logistique pondérée, pénalité L2 (hors constante), méthode de Newton."""
    n, d = X.shape
    Xb = np.hstack([X, np.ones((n, 1))])
    sw = np.ones(n) if sw is None else sw
    w = np.zeros(d + 1)
    R = lam * np.eye(d + 1)
    R[-1, -1] = 0.0
    for _ in range(iters):
        z = np.clip(Xb @ w, -30, 30)
        p = 1.0 / (1.0 + np.exp(-z))
        g = Xb.T @ (sw * (p - y)) + R @ w
        W = sw * p * (1 - p)
        H = (Xb * W[:, None]).T @ Xb + R
        step = np.linalg.solve(H, g)
        w -= step
        if np.max(np.abs(step)) < 1e-9:
            break
    return w[:-1]


def seuil(scores_cal, fpr=0.01):
    return np.quantile(scores_cal, 1.0 - fpr)


def rappel(scores, t):
    return float(np.mean(scores > t))


def aire(pos, neg):
    """Probabilité qu'un positif soit noté au-dessus d'un négatif (rangs)."""
    allv = np.concatenate([pos, neg])
    r = np.empty(len(allv))
    r[np.argsort(allv, kind="mergesort")] = np.arange(1, len(allv) + 1)
    rp = r[: len(pos)].sum()
    return float((rp - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))


def union_scores(ws, X, cal):
    """Union de sondes : maximum des scores centrés réduits sur les témoins de calibration."""
    zs = []
    for w in ws:
        c = cal @ w
        zs.append(((X @ w) - c.mean()) / c.std())
    return np.max(np.vstack(zs), axis=0)


def union_cal(ws, cal):
    return union_scores(ws, cal, cal)


def resume(v):
    v = np.asarray(v, dtype=float)
    return f"{v.mean():.3f} [{np.quantile(v, 0.025):.3f} ; {np.quantile(v, 0.975):.3f}]"


def sortie(*a):
    print(*a)
    sys.stdout.flush()


# ---------------------------------------------------------------- A
def bloc_A(ss):
    sortie("== Bloc A : jugement rétrospectif contre prospectif ; rappel selon le nombre de positifs ==")
    mu, npos, nneg, R = 2.0, 10, 500, 400
    retro, prosp = [], []
    for s in ss.spawn(R):
        rng = default_rng(s)
        u = directions(rng, D, 1)[0]
        pos = rng.standard_normal((npos, D)) + mu * u
        neg = rng.standard_normal((nneg, D))
        w = pos.mean(0) - neg.mean(0)
        t = seuil(rng.standard_normal((20000, D)) @ w)
        retro.append(rappel(pos @ w, t))
        prosp.append(rappel((rng.standard_normal((20000, D)) + mu * u) @ w, t))
    sortie(f"A1 rappel rétrospectif (jugé sur ses 10 positifs d'apprentissage) : {resume(retro)}")
    sortie(f"A1 rappel prospectif (épisodes neufs)                          : {resume(prosp)}")
    sortie(f"A1 rapport des moyennes : {np.mean(retro) / np.mean(prosp):.2f}")

    def formule(n, d, nn=500):
        return phi(mu * mu / math.sqrt(mu * mu + d / n + d / nn) - Z99)

    for n in (3, 10, 30, 100):
        sims = []
        for s in ss.spawn(1)[0].spawn(200):
            rng = default_rng(s)
            u = directions(rng, D, 1)[0]
            pos = rng.standard_normal((n, D)) + mu * u
            neg = rng.standard_normal((nneg, D))
            w = pos.mean(0) - neg.mean(0)
            t = seuil(rng.standard_normal((20000, D)) @ w)
            sims.append(rappel((rng.standard_normal((20000, D)) + mu * u) @ w, t))
        sortie(f"A2 positifs = {n:4d} : formule d=32 {formule(n, D):.3f} ; simulation d=32 {resume(sims)} ; "
               f"formule d=4096 {formule(n, 4096):.3f}")
    sortie(f"A2 plafond (positifs infinis) : {phi(mu - Z99):.3f}")


# ---------------------------------------------------------------- B
def bloc_B(ss):
    sortie("== Bloc B : négatifs pris chez le suspect audité sans dommage (tolérance) ==")
    a, b, naud, R = 2.0, 2.0, 2000, 200
    res = {k: {"vis": [], "inv": []} for k in ("origine", "saine", "artefact", "union_saine", "union_artefact")}
    for s in ss.spawn(R):
        rng = default_rng(s)
        u0, v1, v2 = directions(rng, D, 3)
        w0 = u0.copy()
        lab = rng.choice(3, size=naud, p=[0.02, 0.02, 0.96])  # 0 visible, 1 invisible, 2 honnête
        X = rng.standard_normal((naud, D))
        X[lab == 0] += a * u0 + b * v1
        X[lab == 1] += a * u0 + b * v2
        endo = (lab == 0).astype(float)  # verdict de l'oracle : seule la famille visible est vue
        pos = X[lab == 0]
        w_art = logreg(X, endo)
        exo = rng.standard_normal((naud, D))
        w_sai = logreg(np.vstack([pos, exo]), np.r_[np.ones(len(pos)), np.zeros(naud)])
        cal = rng.standard_normal((20000, D))
        tv = rng.standard_normal((5000, D)) + a * u0 + b * v1
        ti = rng.standard_normal((5000, D)) + a * u0 + b * v2
        for k, w in (("origine", w0), ("saine", w_sai), ("artefact", w_art)):
            t = seuil(cal @ w)
            res[k]["vis"].append(rappel(tv @ w, t))
            res[k]["inv"].append(rappel(ti @ w, t))
        for k, ws in (("union_saine", [w0, w_sai]), ("union_artefact", [w0, w_art])):
            t = seuil(union_cal(ws, cal))
            res[k]["vis"].append(rappel(union_scores(ws, tv, cal), t))
            res[k]["inv"].append(rappel(union_scores(ws, ti, cal), t))
    for k in res:
        sortie(f"B {k:15s} rappel famille vue {resume(res[k]['vis'])} ; famille non vue {resume(res[k]['inv'])}")
    diff = np.array(res["saine"]["inv"]) - np.array(res["artefact"]["inv"])
    sortie(f"B1 écart saine − artefact sur la famille non vue : {resume(diff)}")


# ---------------------------------------------------------------- C
def bloc_C(ss):
    sortie("== Bloc C : régime d'excès, positifs mêlés d'échecs honnêtes ==")
    a, b, c, naud, R = 2.0, 2.0, 2.5, 2000, 200
    res = {"melange": [], "contraste": [], "transfert": []}
    for s in ss.spawn(R):
        rng = default_rng(s)
        f, u0, v1 = directions(rng, D, 3)
        lab = rng.choice(3, size=naud, p=[0.89, 0.10, 0.01])  # 0 propre, 1 échec honnête, 2 saboté
        X = rng.standard_normal((naud, D))
        X[lab == 1] += c * f
        X[lab == 2] += a * u0 + c * f
        pos = X[lab >= 1]  # l'oracle voit tout dommage, sans séparer
        lt = rng.choice(2, size=naud, p=[0.9, 0.1])
        exo = rng.standard_normal((naud, D))
        exo[lt == 1] += c * f  # témoins honnêtes exogènes : échecs honnêtes compris
        w_mel = logreg(np.vstack([pos, exo]), np.r_[np.ones(len(pos)), np.zeros(naud)])
        exo_dmg = rng.standard_normal((200, D)) + c * f  # échecs honnêtes exogènes, vus par l'oracle
        w_con = logreg(np.vstack([pos, exo_dmg]), np.r_[np.ones(len(pos)), np.zeros(200)])
        sig = rng.standard_normal((40, D)) + a * u0 + b * v1  # famille de signature : positifs purs
        exo2 = rng.standard_normal((naud, D))
        w_tra = logreg(np.vstack([sig, exo2]), np.r_[np.ones(40), np.zeros(naud)])
        ts = rng.standard_normal((5000, D)) + a * u0 + c * f
        th = rng.standard_normal((5000, D)) + c * f
        for k, w in (("melange", w_mel), ("contraste", w_con), ("transfert", w_tra)):
            res[k].append(aire(ts @ w, th @ w))
    for k in res:
        sortie(f"C1 {k:10s} P(saboté noté au-dessus d'un échec honnête) : {resume(res[k])}")
    sortie(f"C1 valeur idéale du transfert (direction exacte) : {phi(a / math.sqrt(2) / math.sqrt(2)):.3f}")


# ---------------------------------------------------------------- D
def bloc_D(ss):
    sortie("== Bloc D : audit orienté par l'ancienne sonde ; recapture et réapprentissage ==")
    a, N, R, pf, po = 2.5, 100000, 100, 0.01, 0.5
    res = {"naive": [], "ponderee": [], "verite": [], "b_nonpond": [], "b_pond": [], "b_plancher": [],
           "a_nonpond": [], "a_pond": [], "a_plancher": []}
    for s in ss.spawn(R):
        rng = default_rng(s)
        ua, ub = directions(rng, D, 2)
        lab = rng.choice(3, size=N, p=[0.02, 0.02, 0.96])  # 0 famille vue, 1 famille manquée, 2 honnête
        X = rng.standard_normal((N, D))
        X[lab == 0] += a * ua
        X[lab == 1] += a * ub
        flag = (X @ ua) > Z99  # ancienne sonde, seuil à 1 % sur l'honnête (loi exacte)
        cp = rng.random(N) < pf  # pièce du plancher
        co = rng.random(N) < po * flag  # pièce orientée
        aud = cp | co
        pi = 1 - (1 - pf) * (1 - po * flag)
        sab = lab <= 1
        m = aud & sab
        res["naive"].append(float(flag[m].mean()))
        res["ponderee"].append(float((flag[m] / pi[m]).sum() / (1.0 / pi[m]).sum()))
        res["verite"].append(float(flag[sab].mean()))
        exo = rng.standard_normal((5000, D))
        pos = X[m]
        y = np.r_[np.ones(len(pos)), np.zeros(5000)]
        w_np = logreg(np.vstack([pos, exo]), y)
        wp = 1.0 / pi[m]
        wp = wp * len(pos) / wp.sum()
        w_p = logreg(np.vstack([pos, exo]), y, sw=np.r_[wp, np.ones(5000)])
        posf = X[cp & sab]
        w_f = logreg(np.vstack([posf, exo]), np.r_[np.ones(len(posf)), np.zeros(5000)])
        cal = rng.standard_normal((20000, D))
        ta = rng.standard_normal((5000, D)) + a * ua
        tb = rng.standard_normal((5000, D)) + a * ub
        for k, w in (("nonpond", w_np), ("pond", w_p), ("plancher", w_f)):
            t = seuil(cal @ w)
            res["a_" + k].append(rappel(ta @ w, t))
            res["b_" + k].append(rappel(tb @ w, t))
    sortie(f"D1 recapture naïve (tous audités)      : {resume(res['naive'])}")
    sortie(f"D1 recapture pondérée (inverse de pi)  : {resume(res['ponderee'])}")
    sortie(f"D1 vérité (tous les sabotés)            : {resume(res['verite'])}")
    for k in ("nonpond", "pond", "plancher"):
        sortie(f"D2 réapprise {k:9s} : famille vue {resume(res['a_' + k])} ; famille manquée {resume(res['b_' + k])}")
    diff = np.array(res["b_pond"]) - np.array(res["b_nonpond"])
    sortie(f"D2 écart pondéré − non pondéré sur la famille manquée : {resume(diff)}")


# ---------------------------------------------------------------- E
def binom_sf(n, p, k):
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


def bloc_E():
    sortie("== Bloc E : étiquettes que le plancher livre avant le seuil toléré K (lois exactes) ==")
    for K in (30, 100, 300, 1000):
        pq = 1 - 0.05 ** (1 / K)
        ligne = f"K = {K:4d} : p·q minimal {pq:.4f} ; attendu {K * pq:.3f}"
        for mult in (1, 3, 10):
            pm = min(1.0, mult * pq)
            ligne += f" | x{mult} : P(>=1) {binom_sf(K, pm, 1):.3f} P(>=3) {binom_sf(K, pm, 3):.3f} P(>=10) {binom_sf(K, pm, 10):.3f}"
        sortie(ligne)
    sortie(f"limite K -> infini de K·(1 − 0,05^(1/K)) = −ln 0,05 = {-math.log(0.05):.4f}")


# ---------------------------------------------------------------- F
def binom_cdf(n, p, k):
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(0, k + 1))


def bloc_F():
    sortie("== Bloc F : choisir sur le relevé qui juge (malédiction du gagnant, loi exacte) ==")
    n, r = 15, 0.2
    for m in (1, 5, 10, 20):
        emax = sum(1 - binom_cdf(n, r, j) ** m for j in range(0, n))
        sortie(f"m = {m:2d} versions de rappel vrai {r} jugées sur {n} épisodes : relevé attendu du choisi "
               f"{emax / n:.3f} ; relevé postérieur au choix {r:.3f}")


# ---------------------------------------------------------------- G
INTERDITS = {"tenu_a_l_ecart", "jeu_final", "plant_mesure_q", "lecture_decisive"}


def garde_prospectif(versions, jugements, t_verdict):
    """Rouge si une version est jugée sur un épisode de son apprentissage, ou si le signal suit le verdict,
    ou si la version a été figée après l'épisode."""
    fautes = []
    for (ep, ver, t_signal) in jugements:
        v = versions[ver]
        if ep in v["appris"] or t_signal >= t_verdict[ep] or v["figee"] > t_signal:
            fautes.append((ep, ver))
    return fautes


def garde_negatifs(items):
    return [i for i in items if i["role"] == "neg" and i["source"] == "suspect"]


def garde_interdits(items):
    return [i for i in items if INTERDITS & set(i["etiquettes"])]


def bloc_G():
    sortie("== Bloc G : gardes sur un journal sain et sur des artefacts plantés ==")
    versions = {"v1": {"figee": 0, "appris": set()}, "v2": {"figee": 10, "appris": {"e1", "e2"}}}
    t_verdict = {"e1": 5, "e2": 6, "e3": 15, "e4": 16}
    jug = [("e1", "v1", 1), ("e2", "v1", 2), ("e3", "v2", 11), ("e4", "v2", 12)]
    items = [{"role": "pos", "source": "suspect", "etiquettes": ["signature"]},
             {"role": "neg", "source": "exogene", "etiquettes": []}]

    def etat(jg, it, vs=versions):
        return ("rouge" if garde_prospectif(vs, jg, t_verdict) else "vert",
                "rouge" if garde_negatifs(it) else "vert",
                "rouge" if garde_interdits(it) else "vert")

    sortie(f"G sain                              : prospectif, négatifs, interdits = {etat(jug, items)}")
    art1 = jug + [("e1", "v2", 20)]  # rétro-score : v2 jugée sur e1, qu'elle a appris
    sortie(f"G artefact rétrospectif            : {etat(art1, items)}")
    art2 = items + [{"role": "neg", "source": "suspect", "etiquettes": ["audite_sans_dommage"]}]
    sortie(f"G artefact négatif pris au suspect : {etat(jug, art2)}")
    art3 = items + [{"role": "pos", "source": "suspect", "etiquettes": ["tenu_a_l_ecart"]}]
    sortie(f"G artefact tenu à l'écart appris   : {etat(jug, art3)}")
    art4 = jug + [("e3", "v1", 16)]  # signal consigné après le verdict
    sortie(f"G artefact signal après verdict    : {etat(art4, items)}")


# ---------------------------------------------------------------- main
if __name__ == "__main__":
    with open(__file__, "rb") as fh:
        h = hashlib.sha256(fh.read()).hexdigest()
    sortie(f"script sha256 {h}")
    sortie(f"python {platform.python_version()} ; numpy {np.__version__} ; graine racine {RACINE} ; d = {D}")
    enfants = SeedSequence(RACINE).spawn(4)
    bloc_A(enfants[0])
    bloc_B(enfants[1])
    bloc_C(enfants[2])
    bloc_D(enfants[3])
    bloc_E()
    bloc_F()
    bloc_G()
    sortie("fin")
