"""Contrôles numériques des pas des preuves de l'auteur (méthodes R1 et R2) — v1.

Statut : mise au point exploratoire, aucune revendication. Programme du réfutateur, processeur seul, un processus.
(1) Pas (b) de la preuve de R1 : sous la mesure uniforme π du polytope du membre (dimension d), l'ensemble
    S_ε = {(1 − ε)·θ̂ + ε·v : v ∈ Θ} a pour mesure ε^d. Vérifié par tirages : θ ~ π est dans S_ε si et seulement si
    θ − (1 − ε)·θ̂ ≥ 0 coordonnée par coordonnée (les égalités affines sont conservées). Membre linéaire (deux lois connues,
    trois issues : d = 4, π = Dirichlet(1, 1, 1, 1, 1)) et membre par morceaux à deux morceaux (d = 5 ; (ρ, σ) ~
    Dirichlet(1, 1, 1, 3), proportions m_c uniformes, μ_c = σ·m_c). Ce contrôle éprouve à la fois le pas (b) et le
    paramétrage de la mesure uniforme employé par l'auteur et par le réfutateur.
(2) Pas (b) et (c) de la preuve de R2 : composantes du gradient dans [−G, 0], et inégalité de Hedge
    Σ_s g_s·w_s − min_j Σ_s g_sj ≤ log m/η + η·t·G²/8, sur des suites aléatoires et extrêmes.
Graines : numpy.random.SeedSequence(2026111578, spawn_key=(contrôle, cas)). Sortie : controle_preuve_regret_v1.json.
"""
import json
import math
import os
import platform
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
ENTROPIE = 2026111578
K, J = 3, 2


def rng_de(*cle):
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=tuple(cle)))


def tirer_uniforme(rng, C, nb):
    """θ uniforme sur le polytope : coordonnées (ρ_1..ρ_K, μ_11..μ_CJ)."""
    rs = rng.dirichlet(np.array([1.0] * K + [C * (J - 1) + 1.0]), size=nb)
    mu = [rs[:, K:] * rng.dirichlet(np.ones(J), size=nb) for _ in range(C)]
    return np.concatenate([rs[:, :K]] + mu, axis=1)


def controle_homothetie():
    out = []
    nb = 4_000_000
    cas = 0
    for C in (1, 2):
        d = C * (J - 1) + K
        centres = {"sommet δ_1": np.array([1.0, 0, 0] + [0.0] * (C * J)),
                   "sommet « loi 1 partout »": np.array([0.0, 0, 0] + [1.0, 0.0] * C),
                   "bord (0,7 loi 2 + 0,3 δ_2)": np.array([0.0, 0.3, 0] + [0.0, 0.7] * C)}
        centres["intérieur tiré"] = tirer_uniforme(rng_de(1, 99, C), C, 1)[0]
        for nom, centre in centres.items():
            for eps in (0.3, 0.5, 0.8):
                th = tirer_uniforme(rng_de(1, cas), C, nb)
                p = float(np.all(th - (1 - eps) * centre >= 0, axis=1).mean())
                att = eps ** d
                se = math.sqrt(att * (1 - att) / nb)
                out.append({"morceaux": C, "dimension": d, "centre": nom, "epsilon": eps, "tirages": nb,
                            "part_dans_S_epsilon": p, "epsilon_puissance_d": att, "ecart_en_ecarts_types": round((p - att) / se, 2)})
                cas += 1
    return out


def controle_hedge():
    m, t = J + K, 200
    out = {"suites": 0, "depassements_inegalite_de_Hedge": 0, "composantes_hors_de_[-G,0]": 0, "part_max_de_la_borne": 0.0}
    for i in range(600):
        rng = rng_de(2, i)
        gamma = float(rng.choice([0.05, 0.2, 0.4264901472594289, 0.6]))
        G = (1 - gamma) * m / gamma
        eta = float(rng.choice([0.0377368, 0.2, 1.0])) if i % 3 else math.sqrt(8 * math.log(m) / (t * G * G))
        y = rng.integers(0, K, size=t) if i % 4 else np.zeros(t, dtype=int)
        niveaux = np.array([1e-12, 1e-3, 0.3, 1.0])
        L = niveaux[rng.integers(0, 4, size=(t, J))]
        X = np.concatenate([L, np.eye(K)[y]], axis=1)
        lw = np.full(m, -math.log(m))
        cumul_w, cumul_j = 0.0, np.zeros(m)
        for s in range(t):
            w = np.exp(lw)
            wt = (1 - gamma) * w + gamma / m
            p = float(wt @ X[s])
            g = -(1 - gamma) * X[s] / p                      # gradient de −log(w̃·x) en w
            if g.min() < -G * (1 + 1e-12) or g.max() > 0:
                out["composantes_hors_de_[-G,0]"] += 1
            cumul_w += float(g @ w)
            cumul_j += g
            lw = lw - eta * g
            lw = lw - (lw.max() + math.log(np.exp(lw - lw.max()).sum()))
        borne = math.log(m) / eta + eta * t * G * G / 8
        ecart = cumul_w - float(cumul_j.min())
        out["suites"] += 1
        out["depassements_inegalite_de_Hedge"] += int(ecart > borne + 1e-9)
        out["part_max_de_la_borne"] = max(out["part_max_de_la_borne"], round(ecart / borne, 4))
    return out


def main():
    chemin = os.path.join(ICI, "controle_preuve_regret_v1.json")
    if os.path.exists(chemin):
        raise SystemExit(f"refus d'écraser {chemin}")
    h = controle_homothetie()
    sortie = {"programme": "controle_preuve_regret_v1.py", "statut": "mise au point exploratoire, aucune revendication",
              "graines": {"entropie": ENTROPIE, "regle": "SeedSequence(entropie, spawn_key=(contrôle, cas))"},
              "versions": {"python": platform.python_version(), "numpy": np.__version__},
              "R1_pas_b_mesure_de_S_epsilon": h,
              "R1_pas_b_plus_grand_ecart_en_ecarts_types": max(abs(x["ecart_en_ecarts_types"]) for x in h),
              "R2_pas_b_et_c": controle_hedge()}
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in sortie.items() if k != "R1_pas_b_mesure_de_S_epsilon"}, ensure_ascii=False))
    for x in h:
        print(x)


if __name__ == "__main__":
    main()
