"""Taille nécessaire du plan d'ablation, par simulation (graines par numpy.random.SeedSequence).

Deux critères de jugement, fixés d'avance dans le rapport :
 (J1) préférence à l'aveugle, par dossier apparié (même question, deux bras) : un juge (humain ou modèle
      d'une autre lignée) choisit le meilleur des deux jeux de propositions ; test binomial bilatéral, α = 0,05 ;
 (J2) survie à l'épreuve décisive la moins chère (règle 1) : par proposition retenue, regroupée par dossier ;
      test t sur les moyennes par dossier (bras non appariés), α = 0,05, corrélation intra-dossier ρ.
Puissance visée : 0,80. Résultat : nombre de dossiers par bras pour chaque effet supposé.
Sortie : sorties/ablation-puissance-v1.json.
"""
import json
import math
import sys

import numpy as np

from audit_commun_v2 import SORTIES, graine

N_SIM = 4000


def binom_bilateral_p(k, n):
    # valeur p exacte bilatérale sous p = 1/2
    from math import comb
    pk = [comb(n, i) / 2 ** n for i in range(n + 1)]
    seuil = pk[k]
    return min(1.0, sum(p for p in pk if p <= seuil + 1e-15))


def puissance_j1(n, p, rng):
    k = rng.binomial(n, p, size=N_SIM)
    crit = {kk: binom_bilateral_p(kk, n) < 0.05 for kk in set(k.tolist())}
    return float(np.mean([crit[x] for x in k]))


def puissance_j2(n, m, p0, p1, rho, rng):
    """n dossiers par bras, m retenues par dossier, survie p0 contre p1, corrélation intra-dossier rho (loi bêta-binomiale)."""
    def bras(p):
        if rho <= 0:
            q = np.full((N_SIM, n), p)
        else:
            a = p * (1 - rho) / rho
            b = (1 - p) * (1 - rho) / rho
            q = rng.beta(a, b, size=(N_SIM, n))
        return rng.binomial(m, q) / m
    x, y = bras(p0), bras(p1)
    mx, my = x.mean(1), y.mean(1)
    vx, vy = x.var(1, ddof=1), y.var(1, ddof=1)
    se = np.sqrt(vx / n + vy / n)
    t = np.where(se > 0, (my - mx) / np.where(se > 0, se, 1), 0.0)
    ddl = 2 * n - 2
    # seuil t bilatéral à 5 % (approximation de Cornish-Fisher suffisante ici)
    z = 1.959964
    tc = z + (z ** 3 + z) / (4 * ddl) + (5 * z ** 5 + 16 * z ** 3 + 3 * z) / (96 * ddl ** 2)
    return float(np.mean(np.abs(t) > tc))


def plus_petit_n(f, debut, fin, pas=1):
    for n in range(debut, fin + 1, pas):
        if f(n) >= 0.80:
            return n
    return None


def main():
    out = {"J1_preference_appariee": [], "J2_survie_a_l_epreuve": [], "graines": {}}
    for p in (0.60, 0.65, 0.70, 0.75, 0.80):
        rng, meta = graine(f"ablation-j1-{p}")
        out["graines"][f"J1-{p}"] = meta
        n = plus_petit_n(lambda n: puissance_j1(n, p, rng), 10, 400, 2)
        out["J1_preference_appariee"].append({"preference_du_bras_complet": p, "dossiers_apparies_pour_puissance_0_80": n})
    for p0, p1 in ((0.10, 0.25), (0.15, 0.30), (0.20, 0.40), (0.30, 0.50)):
        for rho in (0.0, 0.2):
            rng, meta = graine(f"ablation-j2-{p0}-{p1}-{rho}")
            out["graines"][f"J2-{p0}-{p1}-{rho}"] = meta
            n = plus_petit_n(lambda n: puissance_j2(n, 3, p0, p1, rho, rng), 5, 300, 1)
            out["J2_survie_a_l_epreuve"].append({"survie_base": p0, "survie_bras_complet": p1, "retenues_par_dossier": 3,
                                                 "correlation_intra_dossier": rho, "dossiers_par_bras_pour_puissance_0_80": n})
    (SORTIES / "ablation-puissance-v1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for k in ("J1_preference_appariee", "J2_survie_a_l_epreuve"):
        for x in out[k]:
            print(k, x)
    return 0


if __name__ == "__main__":
    sys.exit(main())
