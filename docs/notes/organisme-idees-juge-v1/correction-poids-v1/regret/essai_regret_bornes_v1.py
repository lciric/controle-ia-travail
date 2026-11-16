"""Essai 1 — bornes de regret à 200 tirages et vérification sur un cas exact — v1.

Mise au point exploratoire, aucune revendication. Processeur seul.
(1) Table de la borne du mélange uniforme (argument ε) aux 8 instants, pour les dimensions des membres du juge
    (membre linéaire : J + K − 1 ; membre par morceaux à C morceaux : C·(J − 1) + K), J = 2 à 6 lois connues, K = 3.
(2) Borne certifiée du gradient exponentié lissé (η, γ optimisés à n = 200).
(3) Cas exact (dimension 2 : trois composantes L1, L2, δ_0 ; mélange uniforme calculé exactement par programmation
    dynamique sur les monômes) : (a) la borne ε n'est jamais dépassée ; (b) regret effectif (maximum − log mélange) ;
    (c) erreur de l'estimateur par échantillonnage d'importance du banc contre la valeur exacte.
Sortie : sorties/essai_regret_bornes_v1.json.
"""
import json
import math
import os
import platform
import sys
import time

import numpy as np
import scipy
from scipy.special import gammaln, logsumexp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import essai_regret_banc_v1 as bc  # noqa: E402

ICI = os.path.dirname(os.path.abspath(__file__))
ENTROPIE = 2026111501


def log_melange_exact_3(X):
    """log ∫_Δ Π_s (w·x_s) dπ(w), π uniforme (Dirichlet(1,1,1)) ; X (t, 3) ≥ 0. Programmation dynamique sur les
    exposants (a, b), c = s − a − b ; ∫ w1^a w2^b w3^c dπ = 2·a!·b!·c!/(t + 2)!. Rend la trajectoire aux instants."""
    t_max = X.shape[0]
    lx = np.log(np.maximum(X, 0.0) + 0.0)
    with np.errstate(divide="ignore"):
        lx = np.where(X > 0, np.log(np.where(X > 0, X, 1.0)), -np.inf)
    F = np.full((t_max + 1, t_max + 1), -np.inf)
    F[0, 0] = 0.0
    a_idx = np.arange(t_max + 1)
    sortie = {}
    for s in range(1, t_max + 1):
        G = F + lx[s - 1, 2]
        G[1:, :] = np.logaddexp(G[1:, :], F[:-1, :] + lx[s - 1, 0])
        G[:, 1:] = np.logaddexp(G[:, 1:], F[:, :-1] + lx[s - 1, 1])
        F = G
        if s in bc.INSTANTS:
            A, Bm = np.meshgrid(a_idx, a_idx, indexing="ij")
            Cc = s - A - Bm
            ok = Cc >= 0
            terme = np.where(ok, F + gammaln(A + 1) + gammaln(Bm + 1) + gammaln(np.where(ok, Cc, 0) + 1), -np.inf)
            sortie[s] = float(logsumexp(terme) + math.log(2.0) - gammaln(s + 3))
    return sortie


def max_certifie_3(X, iterations=5000):
    """Maximum de Σ log(w·x_s) sur le simplexe (EM multiplicatif) + écart de Frank-Wolfe : borne haute certifiée."""
    t, m = X.shape
    w = np.full(m, 1.0 / m)
    best = np.inf
    for _ in range(iterations):
        p = np.maximum(X @ w, bc.PLANCHER)
        g = X.T @ (1 / p)
        f = float(np.log(p).sum())
        best = min(best, min(0.0, f + max(0.0, float(g.max()) - t)))
        if g.max() - t < 1e-8:
            break
        w = w * g / t
        w /= w.sum()
    return best, w


def main():
    t0 = time.time()
    racine = np.random.SeedSequence(ENTROPIE)
    sortie = {"essai": "essai_regret_bornes_v1", "graine_racine": ENTROPIE, "versions": {
        "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__}}
    # (1) table
    table = []
    for jj in range(2, 7):
        for nom, d in [("lineaire", jj + bc.K - 1), ("morceaux_2", 2 * (jj - 1) + bc.K)]:
            table.append({"J": jj, "membre": nom, "dimension": d,
                          "borne_cover_nats": {int(t): round(float(bc.regret_cover(t, d)), 3) for t in bc.INSTANTS}})
    sortie["table_borne_cover"] = table
    sortie["log_1_sur_alpha"] = round(bc.SEUIL, 4)
    # (2) gradient exponentié
    eg = []
    for C in (1, 2):
        b, eta, gamma = bc.meilleurs_eta_gamma(bc.N, bc.J + bc.K, C)
        eg.append({"cellules": C, "composantes": bc.J + bc.K, "eta": eta, "gamma": gamma,
                   "borne_nats": {int(t): round(float(bc.regret_eg(t, bc.J + bc.K, C, eta, gamma)), 2) for t in bc.INSTANTS}})
    sortie["borne_gradient_exponentie"] = eg
    # (3) cas exact en dimension 2
    rs = racine.spawn(3)
    res = {"cas": [], "description": "X_s = (L1(y_s|x_s), L2(y_s|x_s), 1[y_s = 0]) ; monde = membre (copie) ; 300 jeux par cas"}
    for nom_cas, poids in [("interieur", None), ("sommet_L1", np.array([1.0, 0.0, 0.0])),
                           ("bord_L2_delta0", np.array([0.0, 0.7, 0.3]))]:
        rng_cas = np.random.default_rng(rs[len(res["cas"])])
        viol, regrets, err_is, bornes = 0, {int(t): [] for t in bc.INSTANTS}, [], []
        for _ in range(300):
            arch = bc.archive(rng_cas)
            z, g = bc.plan(rng_cas)
            Lf = bc.lois_connues(arch, z)                         # (n, 2, K)
            w = rng_cas.dirichlet(np.ones(3)) if poids is None else poids
            P = w[0] * Lf[:, 0] + w[1] * Lf[:, 1]
            P[:, 0] += w[2]
            y = bc.tirer(rng_cas, P)
            X = np.stack([Lf[np.arange(bc.N), 0, y], Lf[np.arange(bc.N), 1, y], (y == 0).astype(float)], axis=1)
            exact = log_melange_exact_3(X)
            for t in bc.INSTANTS:
                mx, wh = max_certifie_3(X[:t])
                reg = mx - exact[int(t)]
                regrets[int(t)].append(reg)
                if reg > float(bc.regret_cover(t, 2)) + 1e-9:
                    viol += 1
            # estimateur d'importance du banc (même fonction), à t = 200, comptes de l'EM au maximum
            mx, wh = max_certifie_3(X)
            p = np.maximum(X @ wh, bc.PLANCHER)
            nd = np.array([float((wh[2] * X[:, 2] / p).sum())])
            nl = np.array([[float((wh[0] * X[:, 0] / p).sum()), float((wh[1] * X[:, 1] / p).sum())]])
            est = bc.log_melange_uniforme(X[:, :2], y, np.zeros(bc.N, dtype=int), 1, rng_cas, nb=1000,
                                          comptes=(nd, nl), kk=1)
            err_is.append(est - exact[200])
        res["cas"].append({
            "cas": nom_cas, "jeux": 300, "depassements_borne_epsilon": viol, "controles": 300 * len(bc.INSTANTS),
            "regret_effectif_nats": {t: {"mediane": round(float(np.median(v)), 3), "max": round(float(np.max(v)), 3),
                                         "borne_epsilon": round(float(bc.regret_cover(t, 2)), 3)} for t, v in regrets.items()},
            "erreur_estimateur_importance_t200": {"mediane": round(float(np.median(err_is)), 4),
                                                  "min": round(float(np.min(err_is)), 4),
                                                  "max": round(float(np.max(err_is)), 4)}})
    sortie["cas_exact_dimension_2"] = res
    sortie["duree_s"] = round(time.time() - t0, 1)
    os.makedirs(os.path.join(ICI, "sorties"), exist_ok=True)
    chemin = os.path.join(ICI, "sorties", "essai_regret_bornes_v1.json")
    if os.path.exists(chemin):
        raise SystemExit(f"refus d'écraser {chemin}")
    with open(chemin, "w") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    print(json.dumps(sortie, ensure_ascii=False)[:4000])


if __name__ == "__main__":
    main()
