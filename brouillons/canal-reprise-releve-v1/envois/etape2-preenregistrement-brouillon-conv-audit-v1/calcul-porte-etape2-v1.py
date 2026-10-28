"""Règle du nombre de graines et caractéristiques de la lecture à quatre issues — étape 2, porte 2.1 réduite (v1).

Usage : python3 -I calcul-porte-etape2-v1.py SORTIE.json

Aucune donnée lue. Modèle : score d'une course ~ normal de variance V (hypothèse, non opposable tant que le pilote ne
l'a pas mesurée) ; deux bras de R graines ; Student à variances égales, 2R − 2 degrés de liberté, niveau 0,05
bilatéral. Règle de R : V_haute = (n − 1) s² / quantile 0,20 du khi-deux à n − 1 degrés de liberté (borne haute
unilatérale à 80 % de la variance mesurée par le pilote, n = 6 courses) ; R = le plus petit entier de 10 à 16 qui donne
une puissance ≥ 0,80 à +0,10 avec V_haute ; sinon R = 16 et l'écart minimal détectable à R = 16 est annoncé.
Lecture à quatre issues (première vraie) : « B3 meilleur » si la borne basse à 95 % > 0 ; « B2 meilleur » si la borne
haute à 95 % < 0 ; « équivalent » si l'intervalle à 90 % est dans ]−δ₀ ; +δ₀[ ; sinon « non tranché ».
"""
import hashlib
import json
import sys

import numpy as np
from scipy import optimize, stats

ALPHA = 0.05
PUISSANCE = 0.80
DELTA_CIBLE = 0.10
DELTA0 = 0.10
R_MIN, R_MAX = 10, 16
N_PILOTE = 6
QUANTILE_BORNE = 0.80
V_SCENARIOS = {"plancher_v5 (sigma=0)": 0.25 / 36, "sigma=0.05": 0.05 ** 2 + 0.25 / 36, "sigma=0.10": 0.10 ** 2 + 0.25 / 36}
DELTAS = (-0.10, -0.05, 0.0, 0.05, 0.10, 0.15, 0.20)
R_LECTURE = (10, 13, 16)
ENTROPIE = 20261027  # simulation de contrôle seulement (R9 : SeedSequence), publique, non opposable
N_SIM = 20000


def empreinte(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def puissance(delta, v, r):
    se = (2 * v / r) ** 0.5
    df = 2 * r - 2
    tc = stats.t.ppf(1 - ALPHA / 2, df)
    nc = delta / se
    p = 1 - stats.nct.cdf(tc, df, nc) + stats.nct.cdf(-tc, df, nc)
    return 1.0 if not np.isfinite(p) else float(p)


def mde(v, r):
    se = (2 * v / r) ** 0.5
    return float(optimize.brentq(lambda d: puissance(d, v, r) - PUISSANCE, 1e-9, 12 * se))


def q_borne():
    return float(stats.chi2.ppf(1 - QUANTILE_BORNE, N_PILOTE - 1))


def v_haute(s):
    return (N_PILOTE - 1) * s * s / q_borne()


def regle_r(vh):
    for r in range(R_MIN, R_MAX + 1):
        if puissance(DELTA_CIBLE, vh, r) >= PUISSANCE:
            return r, True
    return R_MAX, False


def v_seuil(r):
    """Plus grande variance V pour laquelle r graines donnent la puissance visée à DELTA_CIBLE."""
    return float(optimize.brentq(lambda v: puissance(DELTA_CIBLE, v, r) - PUISSANCE, 1e-6, 1.0))


def lecture_vectorisee(a, b):
    """a : scores du bras B2 (n_sim, R) ; b : scores du bras B3 ; rend les comptes des quatre issues."""
    r = a.shape[1]
    df = 2 * r - 2
    d = b.mean(axis=1) - a.mean(axis=1)
    sp2 = ((a.var(axis=1, ddof=1) + b.var(axis=1, ddof=1)) / 2)
    se = np.sqrt(sp2 * 2 / r)
    t95, t90 = stats.t.ppf(0.975, df), stats.t.ppf(0.95, df)
    l95, u95, l90, u90 = d - t95 * se, d + t95 * se, d - t90 * se, d + t90 * se
    b3 = l95 > 0
    b2 = (u95 < 0) & ~b3
    eq = (l90 > -DELTA0) & (u90 < DELTA0) & ~b3 & ~b2
    nt = ~(b3 | b2 | eq)
    petit = b3 & (u90 < DELTA0)
    n = len(d)
    return {"B3_meilleur": float(b3.sum() / n), "dont_effet_inferieur_a_delta0": float(petit.sum() / n),
            "B2_meilleur": float(b2.sum() / n), "equivalent": float(eq.sum() / n), "non_tranche": float(nt.sum() / n)}


def main(chemin_sortie):
    sortie = {"script": "calcul-porte-etape2-v1.py", "script_sha256": empreinte(__file__),
              "parametres": {"alpha_bilateral": ALPHA, "puissance": PUISSANCE, "delta_cible": DELTA_CIBLE, "delta0": DELTA0,
                             "R_min": R_MIN, "R_max": R_MAX, "n_pilote": N_PILOTE, "quantile_borne": QUANTILE_BORNE,
                             "quantile_khi2_0.20_5ddl": q_borne(), "entropie_simulation": ENTROPIE, "n_sim": N_SIM,
                             "v_scenarios": V_SCENARIOS},
              "seuils_regle_R": {}, "table_regle_R_selon_s": {}, "loi_de_R_selon_V_vraie": {}, "lecture_quatre_issues": {}}
    # 1. seuils : R = r tant que s <= s_max(r)
    q = q_borne()
    for r in range(R_MIN, R_MAX + 1):
        vs = v_seuil(r)
        sortie["seuils_regle_R"][f"R={r}"] = {"V_haute_max": vs, "s_pilote_max": (vs * q / (N_PILOTE - 1)) ** 0.5,
                                              "ecart_type_course_haut_max": vs ** 0.5}
    # 2. table selon l'écart type s mesuré par le pilote
    for s in np.round(np.arange(0.02, 0.2001, 0.01), 2):
        vh = v_haute(float(s))
        r, atteint = regle_r(vh)
        sortie["table_regle_R_selon_s"][f"s={s:.2f}"] = {"V_haute": vh, "R": r, "puissance_visee_atteinte": atteint,
                                                        "ecart_minimal_annonce_a_R": mde(vh, r)}
    # 3. loi de R si la variance vraie vaut V (s² ~ V khi2(5)/5)
    for nom, v in V_SCENARIOS.items():
        cumul_prec = 0.0
        loi = {}
        for r in range(R_MIN, R_MAX + 1):
            c = float(stats.chi2.cdf(v_seuil(r) * q / v, N_PILOTE - 1))
            loi[f"R={r}"] = c - cumul_prec
            cumul_prec = c
        loi["R=16_puissance_non_atteinte"] = 1 - cumul_prec
        loi[f"R={R_MAX}"] = loi[f"R={R_MAX}"] + loi["R=16_puissance_non_atteinte"]
        esp = sum(int(k.split("=")[1]) * p for k, p in loi.items() if k.startswith("R=") and "_" not in k)
        sortie["loi_de_R_selon_V_vraie"][nom] = {"loi": loi, "esperance_R": esp}
    # 4. lecture à quatre issues : probabilités par simulation (modèle normal), graines par SeedSequence (R9)
    enfants = iter(np.random.SeedSequence(ENTROPIE).spawn(len(V_SCENARIOS) * len(R_LECTURE) * len(DELTAS)))
    for nom, v in V_SCENARIOS.items():
        for r in R_LECTURE:
            for delta in DELTAS:
                rng = np.random.default_rng(next(enfants))
                a = rng.normal(0.0, v ** 0.5, size=(N_SIM, r))
                b = rng.normal(delta, v ** 0.5, size=(N_SIM, r))
                sortie["lecture_quatre_issues"][f"{nom}|R={r}|delta={delta:+.2f}"] = lecture_vectorisee(a, b)
            sortie["lecture_quatre_issues"][f"{nom}|R={r}|ecart_minimal_t"] = mde(v, r)
    with open(chemin_sortie, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
