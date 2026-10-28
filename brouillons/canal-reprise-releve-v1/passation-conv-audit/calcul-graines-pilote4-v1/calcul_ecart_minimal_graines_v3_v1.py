"""Écart minimal détectable entre deux objets (v6.2.1 contre v5.3) selon le nombre R de graines par objet, sur la part
`test_final` de la banque v3 (36 tâches de conscience d'évaluation, 24 de contrôle de délégation ; 60 en tout) — v1.

Modèle (le même que le calcul de l'étape 2, `etape2-proposition-conv-audit-v1/calcul-ecart-minimal-v1.py`, appliqué à la v3) :
le score d'une course (exactitude sur n tâches fixes) varie d'une graine à l'autre avec la variance
    V = sigma**2 + (1 - rho) * p * (1 - p) / n,
où sigma est la part « course » du bruit entre graines (inconnue), rho la corrélation, d'une graine à l'autre, de l'issue
d'une même tâche (inconnue), p l'exactitude. Comparaison des deux objets par un test t de Student à deux échantillons
(variances égales, estimées sur les graines, degrés de liberté 2R - 2), bilatéral à 0,05, puissance 0,8 :
    écart minimal = (t_{0,975 ; 2R-2} + t_{0,80 ; 2R-2}) * sqrt(2 V / R).
À R = 1, la variance entre graines n'est pas estimable : « non testable ». Tout est illustratif (sigma et rho inconnus) ;
aucun score n'est lu. Calcul déterministe, sans graine.
"""
import json, math, sys
from statistics import NormalDist

def t_quantile(q, df):
    # quantile de Student par bissection sur la fonction de répartition (intégration numérique simple de la densité)
    def pdf(x):
        return math.exp(math.lgamma((df + 1) / 2) - math.lgamma(df / 2) - 0.5 * math.log(df * math.pi)
                        - (df + 1) / 2 * math.log1p(x * x / df))
    def cdf(x):
        # intégrale de 0 à x par la règle de Simpson, symétrie autour de 0
        n = 2000
        h = x / n
        s = pdf(0) + pdf(x)
        for i in range(1, n):
            s += (4 if i % 2 else 2) * pdf(i * h)
        return 0.5 + s * h / 3
    lo, hi = 0.0, 50.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if cdf(mid) < q:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

parts = {"conscience d'évaluation (36)": 36, "contrôle de délégation (24)": 24, "les deux familles (60)": 60}
lignes = []
for nom, n in parts.items():
    for p in (0.5, 0.75):
        for sigma in (0.0, 0.05):
            for rho in (0.0, 0.6):
                V = sigma ** 2 + (1 - rho) * p * (1 - p) / n
                for R in (1, 2, 3, 4, 5, 6, 10):
                    if R == 1:
                        e = None
                    else:
                        df = 2 * R - 2
                        e = (t_quantile(0.975, df) + t_quantile(0.80, df)) * math.sqrt(2 * V / R)
                    lignes.append({"part": nom, "n": n, "p": p, "sigma": sigma, "rho": rho, "R": R,
                                   "ecart_minimal": None if e is None else round(e, 3)})
# contrôle : à grand df, le quantile de Student tend vers celui de la loi normale
z = NormalDist().inv_cdf(0.975) + NormalDist().inv_cdf(0.80)
controle = {"z_somme_normale": round(z, 4), "t_somme_df_1000": round(t_quantile(0.975, 1000) + t_quantile(0.80, 1000), 4)}
json.dump({"modele": "V = sigma^2 + (1-rho) p (1-p) / n ; test t à deux échantillons, df = 2R-2, alpha 0,05 bilatéral, puissance 0,8",
           "controle": controle, "lignes": lignes}, sys.stdout, ensure_ascii=False, indent=1)
