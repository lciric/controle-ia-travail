"""Exact-case checks of the reward normalization under Operator B and of the training procedures
that realize each operator (three-stratum softmax, gradient ascent with exact expected gradients),
and of the perfect-niche inversion condition with an honest reward R0 (grid, random draws, and
points within 1e-6 of the threshold in 50-digit arithmetic).
Seeds: numpy.random.SeedSequence(entropy=202611241400). Output: JSON next to the script.
"""
import decimal
import hashlib
import itertools
import json
import math
import pathlib
import sys

import numpy as np

ICI = pathlib.Path(__file__).resolve().parent
SORTIE = ICI / "verify_reward_normalization_output.json"
ENTROPIE = 202611241400


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


def softmax(theta):
    pi = np.exp(theta - theta.max())
    return pi / pi.sum()


def gradient_recompense_par_enumeration(pi, beta, R, mode, b=0.0, C=None):
    """Espérance exacte de l'estimateur de gradient de politique (par rapport aux logits),
    par énumération des issues (strate i, accepté ou intercepté).
    mode 'ecarte_total' : épisodes interceptés retirés, somme divisée par la taille totale du lot ;
    mode 'ecarte_survivants' : lot rempli de survivants, i.e. divisé par le nombre de survivants
      (limite grand lot : division par E_pi[beta]) ;
    mode 'score' : l'épisode intercepté reçoit le score -C (opérateur B)."""
    n = len(pi)
    g = np.zeros(n)
    acc_moy = float(np.dot(pi, beta))
    for i in range(n):
        score_log = np.eye(n)[i] - pi  # gradient de log pi_i par rapport aux logits
        for accepte, proba in ((True, beta[i]), (False, 1 - beta[i])):
            if proba == 0:
                continue
            if accepte:
                valeur = R[i] - b
            elif mode == "score":
                valeur = -C
            else:
                continue  # épisode retiré du lot
            g += pi[i] * proba * valeur * score_log
    if mode == "ecarte_survivants":
        g /= acc_moy
    return g


def montee(p, eta, gradient_recompense, iterations=400000, pas=0.05):
    p = np.array(p, dtype=float)
    theta = np.log(p).copy()
    for _ in range(iterations):
        pi = softmax(theta)
        g_kl = -(np.log(pi) - np.log(p)) / eta  # divergence exacte, sur toute la politique
        grad = gradient_recompense(pi) + pi * (g_kl - np.dot(pi, g_kl))
        theta += pas * grad
        if np.max(np.abs(grad)) < 1e-15:
            break
    return softmax(theta)


def point_fixe_survivants(p, beta, R, eta, iterations=10000):
    """Résout pi ∝ p exp(eta beta R / E_pi[beta]) par itération de point fixe amortie."""
    pi = np.array(p, dtype=float)
    for _ in range(iterations):
        e = float(np.dot(pi, beta))
        cible = loi_B(p, beta, R, eta / e, 0.0)
        pi = 0.5 * pi + 0.5 * cible
    return pi, float(np.dot(pi, beta))


def comparaison_decimale(p, bv, R0, dRv, dRf, C, eta):
    """Signe de pi_B(f) - pi_A(f) en niche parfaite, à 50 chiffres."""
    D = decimal.Decimal
    decimal.getcontext().prec = 50
    ph, pv, pf = (D(x) for x in p)
    bv, R0, dRv, dRf, C, eta = (D(x) for x in (bv, R0, dRv, dRf, C, eta))
    wA = [ph * (eta * R0).exp(), bv * pv * (eta * (R0 + dRv)).exp(), pf * (eta * (R0 + dRf)).exp()]
    wB = [ph * (eta * R0).exp(),
          pv * (eta * (bv * (R0 + dRv) - (1 - bv) * C)).exp(),
          pf * (eta * (R0 + dRf)).exp()]
    return wB[2] / sum(wB) - wA[2] / sum(wA)


def main():
    res = {"affirmations": {}, "defauts": []}
    jeux = [
        {"p": [0.85, 0.14, 0.01], "beta": [0.9, 0.2, 0.6], "eta": 1.5, "dR": 1.0, "C": 0.7},
        {"p": [0.5, 0.3, 0.2], "beta": [1.0, 0.1, 0.8], "eta": 0.4, "dR": 2.0, "C": 1.5},
        {"p": [0.7, 0.25, 0.05], "beta": [0.95, 0.5, 0.7], "eta": 3.0, "dR": 0.3, "C": 0.0},
    ]

    # 1. Translation
    l1 = []
    for j, R0 in itertools.product(jeux, [-0.3, 0.4, 2.0]):
        p, beta, eta, dR, C = j["p"], j["beta"], j["eta"], j["dR"], j["C"]
        R, Rn = [R0, R0 + dR, R0 + dR], [0.0, dR, dR]
        e_B = float(np.max(np.abs(loi_B(p, beta, R, eta, C) - loi_B(p, beta, Rn, eta, C + R0))))
        e_A = float(np.max(np.abs(loi_A(p, beta, R, eta) - loi_A(p, beta, Rn, eta))))
        e_no = float(np.max(np.abs(loi_no(p, R, eta) - loi_no(p, Rn, eta))))
        e_naif = float(np.max(np.abs(loi_B(p, beta, R, eta, C) - loi_B(p, beta, Rn, eta, C))))
        l1.append({"R0": R0, "B_ecart": e_B, "A": e_A, "sans_moniteur": e_no, "B_meme_C": e_naif})
        if max(e_B, e_A, e_no) > 1e-12 or e_naif < 1e-6:
            res["defauts"].append(f"translation R0={R0}")
    res["affirmations"]["1_translation"] = l1

    # 2. Récompense corrigée ; 3. lot écarté ; 4. filtrage itéré
    l2, l3, l4 = [], [], []
    for k, j in enumerate(jeux):
        p, beta, eta, dR = j["p"], j["beta"], j["eta"], j["dR"]
        R = [0.0, dR, dR]
        corr = np.array([r + math.log(b) / eta for r, b in zip(R, beta)])
        pi2 = montee(p, eta, lambda pi: pi * (corr - np.dot(pi, corr)))
        e2 = float(np.max(np.abs(pi2 - loi_A(p, beta, R, eta))))
        l2.append({"jeu": k, "ecart_a_A": e2})
        if e2 > 1e-9:
            res["defauts"].append(f"récompense corrigée jeu {k}")

        piA = loi_A(p, beta, R, eta)
        pi3a = montee(p, eta, lambda pi: gradient_recompense_par_enumeration(pi, beta, R, "ecarte_total"))
        pi3sc = montee(p, eta, lambda pi: gradient_recompense_par_enumeration(pi, beta, R, "score", C=0.0))
        b = 0.5
        pi3b = montee(p, eta, lambda pi: gradient_recompense_par_enumeration(pi, beta, R, "ecarte_total", b=b))
        pi3c = montee(p, eta, lambda pi: gradient_recompense_par_enumeration(pi, beta, R, "ecarte_survivants"))
        pfx, e_star = point_fixe_survivants(p, beta, R, eta)
        d = {
            "jeu": k,
            "a_ecart_a_B_C0": float(np.max(np.abs(pi3a - loi_B(p, beta, R, eta, 0.0)))),
            "a_ecart_au_score_zero_enumere": float(np.max(np.abs(pi3a - pi3sc))),
            "a_ecart_a_A": float(np.max(np.abs(pi3a - piA))),
            "b_ecart_a_B_C_moins_b": float(np.max(np.abs(pi3b - loi_B(p, beta, R, eta, -b)))),
            "c_ecart_au_point_fixe_auto_coherent": float(np.max(np.abs(pi3c - pfx))),
            "c_pression_effective": eta / e_star,
            "c_ecart_a_A": float(np.max(np.abs(pi3c - piA))),
            "c_ecart_a_B_C0_meme_eta": float(np.max(np.abs(pi3c - loi_B(p, beta, R, eta, 0.0)))),
        }
        l3.append(d)
        if (d["a_ecart_a_B_C0"] > 1e-9 or d["a_ecart_au_score_zero_enumere"] > 1e-9
                or d["b_ecart_a_B_C_moins_b"] > 1e-9 or d["c_ecart_au_point_fixe_auto_coherent"] > 1e-8
                or d["a_ecart_a_A"] < 1e-3 or d["c_ecart_a_A"] < 1e-3 or d["c_ecart_a_B_C0_meme_eta"] < 1e-3):
            res["defauts"].append(f"lot écarté jeu {k}")

        # 4. filtrage itéré, T = 3 tours, pas eta1 = eta / 3
        T, eta1 = 3, eta / 3
        pi_rl, pi_sft = np.array(p), np.array(p)
        for _ in range(T):
            filtre = pi_rl * np.array(beta) / np.dot(pi_rl, beta)  # filtrage des échantillons sur politique
            pi_rl = montee(filtre, eta1, lambda pi: pi * (np.array(R) - np.dot(pi, R)))  # pas régularisé vers la politique courante filtrée
            pi_sft = pi_sft * np.array(beta) / np.dot(pi_sft, beta)  # affinage supervisé sur les survivants
        cible_rl = gibbs([math.log(pi) + T * math.log(bb) + T * eta1 * r for pi, bb, r in zip(p, beta, R)])
        cible_sft = gibbs([math.log(pi) + T * math.log(bb) for pi, bb in zip(p, beta)])
        e4 = {"jeu": k, "ecart_rl_a_pi_T": float(np.max(np.abs(pi_rl - cible_rl))),
              "ecart_sft_a_beta_T_pi0": float(np.max(np.abs(pi_sft - cible_sft))),
              "ecart_rl_a_A_meme_pression_totale": float(np.max(np.abs(pi_rl - loi_A(p, beta, R, T * eta1))))}
        l4.append(e4)
        if e4["ecart_rl_a_pi_T"] > 1e-9 or e4["ecart_sft_a_beta_T_pi0"] > 1e-12 or e4["ecart_rl_a_A_meme_pression_totale"] < 1e-3:
            res["defauts"].append(f"filtrage itéré jeu {k}")
    res["affirmations"]["2_recompense_corrigee"] = l2
    res["affirmations"]["3_lot_ecarte"] = l3
    res["affirmations"]["4_filtrage_itere"] = l4

    # 5. Inversion
    pf = [0.85, 0.14, 0.01]
    grille, desacc_g = 0, 0
    for bv, R0, dRi, Ci, etai in itertools.product(
            [0.05, 0.1, 0.3, 0.7], [-0.5, 0.0, 0.5], [0.2, 1.0], [-1.0, 0.0, 0.5, 2.5], [0.1, 0.5, 2.0, 5.0]):
        direct = loi_B(pf, [1.0, bv, 1.0], [R0, R0 + dRi, R0 + dRi], etai, Ci)[2] - loi_A(pf, [1.0, bv, 1.0], [R0, R0 + dRi, R0 + dRi], etai)[2]
        cond = etai * (1 - bv) * (R0 + dRi + Ci) - math.log(1 / bv)
        if abs(direct) < 1e-14 or abs(cond) < 1e-12:
            continue
        grille += 1
        desacc_g += int((direct > 0) != (cond > 0))
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE))
    tirages, desacc_t = 0, 0
    for _ in range(20000):
        p = rng.dirichlet([1, 1, 1])
        bv = rng.uniform(0.01, 0.99)
        R0, dRv, dRf = rng.uniform(-3, 3), rng.uniform(0, 3), rng.uniform(0, 3)
        Ci, etai = rng.uniform(-2, 4), rng.uniform(0.05, 5)
        cond = etai * (1 - bv) * (R0 + dRv + Ci) - math.log(1 / bv)
        direct = loi_B(p, [1.0, bv, 1.0], [R0, R0 + dRv, R0 + dRf], etai, Ci)[2] - loi_A(p, [1.0, bv, 1.0], [R0, R0 + dRv, R0 + dRf], etai)[2]
        if abs(cond) < 1e-9 or abs(direct) < 1e-14:
            continue
        tirages += 1
        desacc_t += int((direct > 0) != (cond > 0))
    seuil, desacc_s = 0, 0
    for bv, R0, dRv, dRf, etai in itertools.product([0.1, 0.5], [-0.5, 0.5], [0.4, 1.5], [0.2, 1.0], [0.7, 3.0]):
        for eps in (1e-6, -1e-6):
            Ci = (math.log(1 / bv) + eps) / (etai * (1 - bv)) - R0 - dRv
            signe = comparaison_decimale(pf, bv, R0, dRv, dRf, Ci, etai)
            seuil += 1
            desacc_s += int((signe > 0) != (eps > 0))
    res["affirmations"]["5_inversion"] = {
        "grille": {"cas": grille, "desaccords": desacc_g},
        "tirages": {"cas": tirages, "desaccords": desacc_t, "entropie": ENTROPIE},
        "pres_du_seuil_1e-6_decimal_50": {"cas": seuil, "desaccords": desacc_s}}
    if desacc_g or desacc_t or desacc_s or grille < 300 or tirages < 19000:
        res["defauts"].append("inversion")

    res["environnement"] = {"python": sys.version.split()[0], "numpy": np.__version__,
                            "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
    SORTIE.write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(res, indent=2, ensure_ascii=False))
    return 1 if res["defauts"] else 0


if __name__ == "__main__":
    sys.exit(main())
