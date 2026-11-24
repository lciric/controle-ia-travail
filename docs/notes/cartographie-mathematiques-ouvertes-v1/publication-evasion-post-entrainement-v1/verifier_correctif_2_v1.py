"""Vérification sur cas calculables exactement des ajouts du correctif 2 du manuscrit v4.

Quatre affirmations, toutes sur la partition à trois strates (honnête, visible, furtive) :
  1. Translation : décaler la récompense de tâche de R0 sur toutes les strates, à score
     d'interception -C fixé, revient sous l'opérateur B (pénalité) à remplacer C par C + R0 ;
     l'opérateur A (rejet pur) et la ligne sans moniteur sont invariants.
  2. Rejet pur par récompense corrigée : l'optimum de E[R + log(beta)/eta] - KL/eta, atteint par
     montée de gradient exacte (gradients en espérance, pas d'échantillonnage), est la loi de A.
  3. Écarter les épisodes interceptés d'un lot sur politique (gradient de politique en espérance,
     normalisé par la taille totale du lot, sans ligne de base) converge vers B à C = 0, et non vers A ;
     avec une ligne de base b retranchée aux seuls épisodes retenus, vers B à C = -b.
  4. Inversion en niche parfaite avec récompense honnête R0 : pi_B(f) > pi_A(f) si et seulement si
     eta (1 - beta_v)(R0 + DeltaR + C) > log(1/beta_v), confrontée au calcul direct sur une grille.
Aucune graine : tout est déterministe. Sortie : un JSON à côté du script.
"""
import json
import math
import hashlib
import itertools
import pathlib
import sys

import numpy as np

ICI = pathlib.Path(__file__).resolve().parent
SORTIE = ICI / "exemples-verifies-correctif-2-v1.json"


def gibbs(log_poids):
    m = max(log_poids)
    w = np.array([math.exp(x - m) for x in log_poids])
    return w / w.sum()


def loi_no(p, R, eta):
    return gibbs([math.log(pi) + eta * r for pi, r in zip(p, R)])


def loi_A(p, beta, R, eta):
    return gibbs([math.log(pi) + math.log(b) + eta * r for pi, b, r in zip(p, beta, R)])


def loi_B(p, beta, R, eta, C):
    return gibbs([math.log(pi) + eta * (b * r - (1 - b) * C) for pi, b, r in zip(p, beta, R)])


def montee_exacte(p, eta, score_attendu, iterations=200000, pas=0.05):
    """Montée de gradient en espérance exacte sur les logits d'un softmax, objectif
    E_pi[s] - KL(pi || p)/eta, où s est le score attendu par strate. Renvoie la loi finale."""
    p = np.array(p, dtype=float)
    s = np.array(score_attendu, dtype=float)
    theta = np.log(p).copy()
    for _ in range(iterations):
        pi = np.exp(theta - theta.max())
        pi /= pi.sum()
        # gradient de E_pi[s - (log pi - log p)/eta] par rapport aux logits
        g = s - (np.log(pi) - np.log(p)) / eta
        grad = pi * (g - np.dot(pi, g))
        theta += pas * grad
        if np.max(np.abs(grad)) < 1e-15:
            break
    pi = np.exp(theta - theta.max())
    return pi / pi.sum()


def montee_lot_ecarte(p, beta, R, eta, b=0.0, iterations=200000, pas=0.05):
    """Gradient de politique en espérance quand les épisodes interceptés sont écartés du lot :
    E[1{accepté} (R - b) grad log pi] / 1 (normalisé par la taille totale du lot), plus le terme KL.
    Le score effectif de la strate i est donc beta_i (R_i - b)."""
    s = [bi * (ri - b) for bi, ri in zip(beta, R)]
    return montee_exacte(p, eta, s, iterations, pas)


def main():
    resultats = {"affirmations": {}, "defauts": []}
    p = [0.85, 0.14, 0.01]
    beta = [0.9, 0.2, 0.6]
    eta, dR, C = 1.5, 1.0, 0.7

    # 1. Translation
    ecarts = []
    for R0 in [-0.3, 0.0, 0.4, 2.0]:
        R = [R0, R0 + dR, R0 + dR]
        R_norm = [0.0, dR, dR]
        e_B = np.max(np.abs(loi_B(p, beta, R, eta, C) - loi_B(p, beta, R_norm, eta, C + R0)))
        e_A = np.max(np.abs(loi_A(p, beta, R, eta) - loi_A(p, beta, R_norm, eta)))
        e_no = np.max(np.abs(loi_no(p, R, eta) - loi_no(p, R_norm, eta)))
        e_B_naif = np.max(np.abs(loi_B(p, beta, R, eta, C) - loi_B(p, beta, R_norm, eta, C)))
        ecarts.append({"R0": R0, "B_vs_B_C_plus_R0": e_B, "A": e_A, "sans_moniteur": e_no,
                       "B_vs_B_meme_C": e_B_naif})
        if e_B > 1e-12 or e_A > 1e-12 or e_no > 1e-12:
            resultats["defauts"].append(f"translation R0={R0}")
        if R0 != 0.0 and e_B_naif < 1e-6:
            resultats["defauts"].append(f"translation naive non détectée R0={R0}")
    resultats["affirmations"]["1_translation"] = ecarts

    # 2. Récompense corrigée
    R = [0.0, dR, dR]
    s_corr = [r + math.log(b) / eta for r, b in zip(R, beta)]
    pi_corr = montee_exacte(p, eta, s_corr)
    e2 = float(np.max(np.abs(pi_corr - loi_A(p, beta, R, eta))))
    resultats["affirmations"]["2_recompense_corrigee"] = {"ecart_max_a_A": e2}
    if e2 > 1e-9:
        resultats["defauts"].append("récompense corrigée")

    # 3. Épisodes écartés du lot
    pi_drop = montee_lot_ecarte(p, beta, R, eta)
    e3_B0 = float(np.max(np.abs(pi_drop - loi_B(p, beta, R, eta, 0.0))))
    e3_A = float(np.max(np.abs(pi_drop - loi_A(p, beta, R, eta))))
    b = 0.5
    pi_drop_b = montee_lot_ecarte(p, beta, R, eta, b=b)
    e3_Bb = float(np.max(np.abs(pi_drop_b - loi_B(p, beta, R, eta, -b))))
    resultats["affirmations"]["3_lot_ecarte"] = {
        "ecart_a_B_C0": e3_B0, "ecart_a_A": e3_A,
        "ligne_de_base": b, "ecart_a_B_C_moins_b": e3_Bb}
    if e3_B0 > 1e-9 or e3_Bb > 1e-9 or e3_A < 1e-3:
        resultats["defauts"].append("lot écarté")

    # 4. Inversion en niche parfaite avec R0
    pf = [0.85, 0.14, 0.01]
    n_cas, n_desaccords = 0, 0
    for bv, R0, dRi, Ci, etai in itertools.product(
            [0.05, 0.1, 0.3, 0.7], [-0.5, 0.0, 0.5], [0.2, 1.0], [0.0, 0.5, 2.5], [0.1, 0.5, 2.0, 5.0]):
        bb = [1.0, bv, 1.0]
        RR = [R0, R0 + dRi, R0 + dRi]
        direct = loi_B(pf, bb, RR, etai, Ci)[2] - loi_A(pf, bb, RR, etai)[2]
        condition = etai * (1 - bv) * (R0 + dRi + Ci) - math.log(1 / bv)
        if abs(direct) < 1e-14 or abs(condition) < 1e-12:
            continue
        n_cas += 1
        if (direct > 0) != (condition > 0):
            n_desaccords += 1
    resultats["affirmations"]["4_inversion_avec_R0"] = {"cas": n_cas, "desaccords": n_desaccords}
    if n_desaccords or n_cas < 200:
        resultats["defauts"].append("inversion")

    resultats["environnement"] = {"python": sys.version.split()[0], "numpy": np.__version__,
                                  "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
    SORTIE.write_text(json.dumps(resultats, indent=2, ensure_ascii=False, default=float) + "\n")
    print(json.dumps(resultats, indent=2, ensure_ascii=False, default=float))
    return 1 if resultats["defauts"] else 0


if __name__ == "__main__":
    sys.exit(main())
