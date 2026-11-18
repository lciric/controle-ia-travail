#!/usr/bin/env python3
"""Estimation de ce qui manque par capture-recapture sur les quatre voies.

Usage : python -I couverture.py fusion.json couverture.json
Estimateurs : Chapman par paire de voies (variance de Seber, intervalle log-normal sur le non-vu) ;
borne inferieure de Chao (1987, forme corrigee du biais) ; modeles log-lineaires de Poisson a plusieurs listes
(independance, toutes interactions de paires, meilleur selon le critere d'Akaike parmi les 64 jeux d'interactions de paires).
Graine du reechantillonnage : numpy.random.SeedSequence(20261118) (R9).
"""
import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np

GRAINE = 20261118
ORDRE = ["mots-cles", "citations", "grise", "adverse"]
d = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
T = d["travaux"]


def chapman(n1, n2, m):
    r = n1 + n2 - m
    N = (n1 + 1) * (n2 + 1) / (m + 1) - 1
    var = (n1 + 1) * (n2 + 1) * (n1 - m) * (n2 - m) / ((m + 1) ** 2 * (m + 2))
    f0 = N - r
    if f0 <= 0 or var <= 0:
        return dict(n1=n1, n2=n2, m=m, union=r, N=N, bas=r, haut=r, lincoln=(n1 * n2 / m if m else None))
    C = math.exp(1.96 * math.sqrt(math.log(1 + var / f0 ** 2)))
    return dict(n1=n1, n2=n2, m=m, union=r, N=round(N, 1), bas=round(r + f0 / C, 1), haut=round(r + f0 * C, 1),
                part_commune_1=round(m / n1, 3), part_commune_2=round(m / n2, 3))


def chao(hist):
    n = sum(hist.values())
    f = Counter(sum(int(c) for c in h) for h in hist.elements())
    f1, f2 = f.get(1, 0), f.get(2, 0)
    f0 = f1 * (f1 - 1) / (2 * (f2 + 1))
    # variance (Chao 1987, forme corrigee)
    if f2 > 0:
        q = f1 / f2
        var = f2 * (0.25 * q ** 4 + q ** 3 + 0.5 * q ** 2)
    else:
        var = f1 * (f1 - 1) / 2 + f1 * (2 * f1 - 1) ** 2 / 4 - f1 ** 4 / (4 * max(n + f0, 1))
    if f0 <= 0:
        return dict(n=n, f1=f1, f2=f2, N=n, bas=n, haut=n)
    C = math.exp(1.96 * math.sqrt(math.log(1 + var / f0 ** 2)))
    return dict(n=n, f1=f1, f2=f2, N=round(n + f0, 1), bas=round(n + f0 / C, 1), haut=round(n + f0 * C, 1))


def poisson_irls(X, y, iters=200):
    beta = np.zeros(X.shape[1])
    beta[0] = math.log(max(y.mean(), 0.5))
    for _ in range(iters):
        eta = np.clip(X @ beta, -30, 30)
        mu = np.exp(eta)
        W = mu
        z = eta + (y - mu) / mu
        XtW = X.T * W
        try:
            nb = np.linalg.solve(XtW @ X + 1e-9 * np.eye(X.shape[1]), XtW @ z)
        except np.linalg.LinAlgError:
            return None
        if np.max(np.abs(nb - beta)) < 1e-9:
            beta = nb
            break
        beta = nb
    eta = np.clip(X @ beta, -30, 30)
    mu = np.exp(eta)
    ll = float(np.sum(y * eta - mu - np.array([math.lgamma(v + 1) for v in y])))
    try:
        cov = np.linalg.inv((X.T * mu) @ X + 1e-9 * np.eye(X.shape[1]))
    except np.linalg.LinAlgError:
        return None
    return beta, cov, ll


def loglin(hist, k):
    cellules = [c for c in itertools.product([0, 1], repeat=k) if any(c)]
    y = np.array([hist.get("".join(map(str, c)), 0) for c in cellules], dtype=float)
    n = int(y.sum())
    paires = list(itertools.combinations(range(k), 2))
    res = []
    for r in range(len(paires) + 1):
        for jeu in itertools.combinations(paires, r):
            cols = [np.ones(len(cellules))] + [np.array([c[i] for c in cellules], float) for i in range(k)]
            cols += [np.array([c[i] * c[j] for c in cellules], float) for i, j in jeu]
            X = np.column_stack(cols)
            if X.shape[1] >= len(cellules):
                continue
            fit = poisson_irls(X, y)
            if fit is None:
                continue
            beta, cov, ll = fit
            f0 = math.exp(min(beta[0], 30))
            se = math.sqrt(max(cov[0, 0], 0))
            aic = -2 * ll + 2 * X.shape[1]
            res.append(dict(interactions=[f"{i}x{j}" for i, j in jeu], N=n + f0, bas=n + f0 * math.exp(-1.96 * se),
                            haut=n + f0 * math.exp(min(1.96 * se, 50.0)), aic=aic, se_log_f0=se))
    res.sort(key=lambda x: x["aic"])
    indep = next(x for x in res if not x["interactions"])
    complet = next((x for x in res if len(x["interactions"]) == len(paires)), None)
    proches = [x for x in res if x["aic"] - res[0]["aic"] < 2 and x["se_log_f0"] < 5]
    arr = lambda x: None if x is None else dict(interactions=x["interactions"], N=round(x["N"], 1), bas=round(x["bas"], 1),
                                                 haut=round(x["haut"], 1), aic=round(x["aic"], 1))
    return dict(n=n, independance=arr(indep), meilleur_aic=arr(res[0]), toutes_paires=arr(complet),
                etendue_modeles_proches=[round(min(x["N"] for x in proches), 1), round(max(x["N"] for x in proches), 1)],
                nombre_modeles_proches=len(proches))


def strate(nom, travaux, listes, voies_de):
    hist = Counter()
    for t in travaux:
        v = voies_de(t)
        h = "".join("1" if x in v else "0" for x in listes)
        if "1" in h:
            hist[h] += 1
    n = sum(hist.values())
    tailles = {x: sum(c for h, c in hist.items() if h[i] == "1") for i, x in enumerate(listes)}
    paires = {}
    for i, j in itertools.combinations(range(len(listes)), 2):
        n1, n2 = tailles[listes[i]], tailles[listes[j]]
        m = sum(c for h, c in hist.items() if h[i] == "1" and h[j] == "1")
        paires[f"{listes[i]} x {listes[j]}"] = chapman(n1, n2, m)
    out = dict(nom=nom, listes=listes, n_union=n, tailles=tailles, histoires=dict(sorted(hist.items(), key=lambda x: -x[1])),
               chapman=paires, chao=chao(hist))
    if len(listes) >= 3:
        out["loglineaire"] = loglin(hist, len(listes))
    # reechantillonnage non parametrique des histoires observees, pour Chao (sensibilite a l'echantillon)
    rng = np.random.default_rng(np.random.SeedSequence(GRAINE))
    hs = list(hist.keys())
    p = np.array([hist[h] for h in hs], float) / n
    ests = []
    for _ in range(2000):
        tir = rng.multinomial(n, p)
        hh = Counter({h: int(c) for h, c in zip(hs, tir) if c})
        ests.append(chao(hh)["N"])
    out["chao_reechantillonnage_2000"] = [round(float(np.percentile(ests, 2.5)), 1), round(float(np.percentile(ests, 97.5)), 1)]
    return out


annote = lambda t: set(t["voies"])
avec_annexe = lambda t: set(t["voies"]) | ({"mots-cles"} if t["annexe_mots_cles"] else set())
est_arxiv = lambda t: bool(t["arxiv"])
fen = lambda t: t["fenetre"] is True

S = []
S.append(strate("A. tous les travaux annotés, quatre voies", T, ORDRE, annote))
S.append(strate("B. articles arXiv de la fenêtre (mai 2026 ou après), quatre voies", [t for t in T if est_arxiv(t) and fen(t)], ORDRE, annote))
S.append(strate("C. articles arXiv de la fenêtre, trois voies tournées vers arXiv (sans la voie grise)",
                [t for t in T if est_arxiv(t) and fen(t)], ["mots-cles", "citations", "adverse"], annote))
S.append(strate("D. articles arXiv de la fenêtre, deux voies non orientées (mots-clés et citations)",
                [t for t in T if est_arxiv(t) and fen(t)], ["mots-cles", "citations"], annote))
S.append(strate("E. hors arXiv (billets, dépôts, soumissions sans identifiant arXiv), quatre voies",
                [t for t in T if not est_arxiv(t)], ORDRE, annote))
S.append(strate("F. sensibilité : comme A, la voie mots-clés comptée avec son annexe mécanique de titres", T, ORDRE, avec_annexe))
S.append(strate("G. sensibilité : comme B, la voie mots-clés comptée avec son annexe mécanique de titres",
                [t for t in T if est_arxiv(t) and fen(t)], ORDRE, avec_annexe))

Path(sys.argv[2]).write_text(json.dumps(dict(graine=GRAINE, strates=S), ensure_ascii=False, indent=1), encoding="utf-8")
for s in S:
    print("\n===", s["nom"], "| union", s["n_union"], "| tailles", s["tailles"])
    print("  histoires", s["histoires"])
    for k, v in s["chapman"].items():
        print(f"  Chapman {k}: n1={v['n1']} n2={v['n2']} commun={v['m']} -> N={v['N']} [{v['bas']}, {v['haut']}]")
    c = s["chao"]
    print(f"  Chao: f1={c['f1']} f2={c['f2']} -> N>={c['N']} [{c['bas']}, {c['haut']}] ; rééch. {s['chao_reechantillonnage_2000']}")
    if "loglineaire" in s:
        l = s["loglineaire"]
        print("  log-lin indep", l["independance"], "\n  meilleur AIC", l["meilleur_aic"], "\n  toutes paires", l["toutes_paires"],
              "\n  étendue modèles à moins de 2 points d'AIC", l["etendue_modeles_proches"], l["nombre_modeles_proches"])
