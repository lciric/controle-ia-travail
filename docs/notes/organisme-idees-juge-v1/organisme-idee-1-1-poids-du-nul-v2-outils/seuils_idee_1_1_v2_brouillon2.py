"""Seuils du préenregistrement de l'idée 1.1, version 2, brouillon 2 (compte seul, sans donnée, sans juge).
(1) Cellules de taille : test binomial exact au taux 0,05 sur 1 000 répétitions, au niveau le plus strict de Holm
    (0,05/m) et au moins strict (0,05), pour m cellules.
(2) Dents : plus petit nombre de promotions sur 1 000 dont la borne basse de Clopper-Pearson unilatérale à 95 % dépasse
    0,5, puis 0,05.
(3) Ligne informative : plus petit nombre de paires discordantes sur 1 000 dont la même borne basse atteint 0,02."""
from scipy.stats import beta, binom

n = 1000
for m in (53, 57):
    for nom, lv in (("le plus strict (0,05/%d)" % m, 0.05 / m), ("le moins strict (0,05)", 0.05)):
        kt = max(k for k in range(n + 1) if binom.cdf(k, n, 0.05) <= lv)
        knt = min(k for k in range(n + 1) if binom.sf(k - 1, n, 0.05) <= lv)
        print(f"taille, {m} cellules, niveau {nom} : tenue si <= {kt} ; non tenue si >= {knt}")


def borne_basse(k):
    return 0.0 if k == 0 else float(beta.ppf(0.05, k, n - k + 1))


for seuil, strict in ((0.5, True), (0.05, True), (0.02, False)):
    k = min(k for k in range(n + 1) if (borne_basse(k) > seuil if strict else borne_basse(k) >= seuil))
    print(f"borne basse unilatérale à 95 % {'>' if strict else '>='} {seuil} : à partir de {k} sur {n} (borne {borne_basse(k):.4f})")
