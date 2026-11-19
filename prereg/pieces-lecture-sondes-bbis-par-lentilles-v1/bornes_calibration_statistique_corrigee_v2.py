"""Bornes de calibration de la lecture des sondes de l'étape B bis par la lentille publique, sous la statistique corrigée de
l'addendum « concentration » (directions nulles jugées sur les M − 1 autres, sans elles-mêmes) — programme neuf, v2.

Loi de référence du compte des p ≤ 0,05 d'un jeu de n témoins qui partagent M = 2 000 directions nulles : mélange de lois
binomiales (n ; π), π étant la part des tirages du nul qui dépassent la 100ᵉ plus grande concentration nulle. Sous la statistique
corrigée, π suit la loi bêta (100 ; 1 901) à l'approximation de l'addendum (ordre 1/M²) : le compte de référence est la loi
bêta-binomiale (n ; 100 ; 1 901) ; plusieurs jeux mis en commun : somme de lois bêta-binomiales indépendantes.
q_bas = plus grand entier tel que P(X < q_bas) ≤ 1e-4 ; q_haut = plus petit entier tel que P(X > q_haut) ≤ 1e-4.
Risque de sortie = P(X < q_bas) + P(X > q_haut).
Sensibilité : le même risque quand la part moyenne vraie vaut r au lieu de r0 = 100/2 001, chaque jeu suivant la loi bêta-binomiale
(n ; r·2 001 ; (1 − r)·2 001) (même dispersion, moyenne déplacée) : résidu de marge (ordre 1/M², vers le bas), résidu de couplage
(ordre 1/M : vers le bas pour des jetons corrélés, r0 × 0,99 à r0 × 0,90 ; vers le haut au plus r0 × (1 + 3e-4)), et les deux
parts mesurées au banc du contre-lecteur du code.
Aucune donnée, aucun poids, aucune sonde, aucune lentille. Bibliothèque standard et numpy (convolution) seulement.
Usage : python -I -B bornes_calibration_statistique_corrigee_v2.py
"""
import sys
from datetime import datetime, timezone
from math import exp, lgamma

import numpy as np

M, RANG, NIVEAU = 2000, 100, 1e-4          # p ≤ 0,05 ⇔ au plus 99 nuls au-dessus ⇔ au-dessus de la 100ᵉ plus grande
A0, B0 = float(RANG), float(M + 1 - RANG)  # bêta (100 ; 1 901)
R0 = A0 / (A0 + B0)


def loi_beta_binomiale(n, a, b):
    """Probabilités de 0 à n, par logarithmes de la fonction gamma."""
    lb = lgamma(a) + lgamma(b) - lgamma(a + b)
    lc = [lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1) for k in range(n + 1)]
    return np.array([exp(lc[k] + lgamma(k + a) + lgamma(n - k + b) - lgamma(n + a + b) - lb) for k in range(n + 1)])


def loi_du_compte(jeux, r=R0):
    a, b = r * (M + 1), (1 - r) * (M + 1)
    p = np.array([1.0])
    for n in jeux:
        p = np.convolve(p, loi_beta_binomiale(n, a, b))
    return p


def bornes(p):
    """q_bas : plus grand q tel que P(X < q) ≤ NIVEAU ; q_haut : plus petit q tel que P(X > q) ≤ NIVEAU."""
    bas, cumul = 0, 0.0                      # cumul = P(X < q)
    for q in range(len(p)):
        if cumul <= NIVEAU:
            bas = q
        else:
            break
        cumul += p[q]
    haut, queue = len(p) - 1, 0.0            # queue = P(X > q)
    for q in range(len(p) - 1, -1, -1):
        if queue <= NIVEAU:
            haut = q
        else:
            break
        queue += p[q]
    return bas, haut


def sortie(p, bas, haut):
    return float(p[:bas].sum()), float(p[haut + 1:].sum())


if __name__ == "__main__":
    print(f"commande : python -I -B bornes_calibration_statistique_corrigee_v2.py (python {sys.version.split()[0]}, numpy "
          f"{np.__version__}, {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')})")
    print(f"loi de référence : bêta-binomiale (n ; {A0:.0f} ; {B0:.0f}) par jeu ; part attendue {R0:.6f} ; niveau {NIVEAU} par côté")
    autres = [("r0 × (1 − 1e-4)", R0 * (1 - 1e-4)), ("r0 × (1 + 3e-4)", R0 * (1 + 3e-4)), ("r0 × 0,99", R0 * 0.99),
              ("r0 × 0,98", R0 * 0.98), ("r0 × 0,95", R0 * 0.95), ("r0 × 0,90", R0 * 0.90),
              ("0,0513 (banc, sans elle-même, lecture pessimiste)", 0.0513), ("0,0571 (texte v1, pour mémoire)", 0.0571)]
    print("colonnes : jeux | n | [q_bas, q_haut] | P(X < q_bas) | P(X > q_haut) | risque de sortie | risque si la part vraie vaut : "
          + " ; ".join(nom for nom, _ in autres))
    cas = [("nul isotrope partagé, un jeu de 1 000", [1000])] + [(f"{k} jeu(x) de 200", [200] * k) for k in range(1, 41)]
    controle = {"nul isotrope partagé, un jeu de 1 000": (23, 85), "1 jeu(x) de 200": (1, 24), "3 jeu(x) de 200": (12, 53),
                "5 jeu(x) de 200": (26, 79), "6 jeu(x) de 200": (33, 92), "13 jeu(x) de 200": (89, 176),
                "20 jeu(x) de 200": (149, 256), "40 jeu(x) de 200": (326, 478)}
    pire, ecarts = 0.0, []
    for nom, jeux in cas:
        p = loi_du_compte(jeux)
        bas, haut = bornes(p)
        g, d = sortie(p, bas, haut)
        pire = max(pire, g + d)
        sens = []
        for _, r in autres:
            ga, da = sortie(loi_du_compte(jeux, r), bas, haut)
            sens.append(ga + da)
        if nom in controle and controle[nom] != (bas, haut):
            ecarts.append((nom, controle[nom], (bas, haut)))
        print(f"{nom} | {sum(jeux)} | [{bas}, {haut}] | {g:.3e} | {d:.3e} | {g + d:.3e} | " + " ; ".join(f"{x:.3e}" for x in sens)
              + f" | somme {p.sum():.12f}")
    print(f"risque de sortie le plus haut sous la loi de référence, sur les 41 cas : {pire:.3e} (borne par construction : 2e-4)")
    print("contrôle contre les bornes écrites dans le texte v1 (un jeu de 1 000 ; 1, 3, 5 jeux de 200) et dans le rapport de la "
          "contre-lecture du code (6, 13, 20, 40 jeux de 200) : " + ("toutes égales" if not ecarts else f"ÉCARTS {ecarts}"))
    # borne de réunion sur une lecture entière : 3 couches × 2 lentilles × 2 nuls = 12 calibrations au plus
    print(f"borne de réunion pour 12 calibrations (3 couches × 2 lentilles × 2 nuls) : au plus {12 * pire:.3e}")
