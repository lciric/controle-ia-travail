"""Vérification des chiffres de la question « seuil et budget d'une épreuve d'admission par prédicteur adverse ».

Reconstruction supposée des calculs à la main :
- statistique : précision équilibrée d'un prédicteur sur la moitié d'épreuve ;
- multiplicité des ~30 prédicteurs traitée par Bonferroni (seuil / 30), unilatéral ;
- approximation normale, variance sous le nul pour les deux erreurs ;
- fuite en variation totale t : précision équilibrée de Bayes = (1 + t) / 2 ;
- le prédicteur appris atteint la précision de Bayes.
"""
import numpy as np
from scipy import stats

K = 30


def ecart_type_precision_equilibree(n_epreuve, pi):
    n1 = pi * n_epreuve
    n0 = (1 - pi) * n_epreuve
    return np.sqrt(1 / n1 + 1 / n0) / 4


def plus_petite_fuite(seuil_test, n_epreuve, pi=0.5, k=K, puissance=0.8):
    za = stats.norm.isf(seuil_test / k)
    zb = stats.norm.isf(1 - puissance)
    return 2 * (za + zb) * ecart_type_precision_equilibree(n_epreuve, pi)


def puissance(t, seuil_test, n_epreuve, pi=0.5, k=K):
    za = stats.norm.isf(seuil_test / k)
    return stats.norm.sf(za - (t / 2) / ecart_type_precision_equilibree(n_epreuve, pi))


print("== 1. Fausses suspensions par admission (quatre tests) ==")
for a in [0.05, 0.025, 0.0125]:
    print(f"seuil {a}: indépendance {1-(1-a)**4:.4f} ; borne quelconque {min(1,4*a):.4f} ;"
          f" deux paires parfaitement liées {1-(1-a)**2:.4f} ; nombre attendu {4*a:.3f}")
print("Šidák pour 5 % sur 4 tests :", 1 - 0.95 ** 0.25)

print("\n== 2. Reconstruction des plus petites fuites retrouvées ==")
for nom, a, N in [("a", 0.05, 4000), ("b", 0.0125, 4000), ("c", 0.05, 8000),
                  ("d", 0.0125, 8000), ("par secret 4000", 0.025, 4000), ("par secret 8000", 0.025, 8000)]:
    print(f"({nom}) seuil {a}, {N} épisodes : pile ou face {plus_petite_fuite(a, N/2):.4f} ;"
          f" 5 % audités {plus_petite_fuite(a, N/2, pi=0.05):.4f} ;"
          f" puissance 0,95 : {plus_petite_fuite(a, N/2, puissance=0.95):.4f} / {plus_petite_fuite(a, N/2, pi=0.05, puissance=0.95):.4f}")
print("facteur 5 % / pile ou face :", ecart_type_precision_equilibree(2000, 0.05) / ecart_type_precision_equilibree(2000, 0.5),
      "; facteur sur n :", 1 / (4 * 0.05 * 0.95))
za05 = stats.norm.isf(0.05 / K); za0125 = stats.norm.isf(0.0125 / K); zb = stats.norm.isf(0.2)
print("quantiles :", za05, za0125, zb, "; rapport des sommes :", (za0125 + zb) / (za05 + zb))

print("\n== 2 bis. Contrôle par binomiale exacte (pile ou face, 2000 épisodes d'épreuve) ==")
for a in [0.05, 0.0125]:
    n = 2000
    ap = a / K
    c = int(stats.binom.isf(ap, n, 0.5)) + 1  # P(X >= c) <= ap
    while stats.binom.sf(c - 1, n, 0.5) > ap:
        c += 1
    while c > 0 and stats.binom.sf(c - 2, n, 0.5) <= ap:
        c -= 1
    lo, hi = 0.5, 0.7
    for _ in range(100):
        m = (lo + hi) / 2
        if stats.binom.sf(c - 1, n, m) < 0.8:
            lo = m
        else:
            hi = m
    print(f"seuil {a}: valeur critique {c}/{n}, précision requise {hi:.4f}, fuite {2*(hi-0.5):.4f}")

print("\n== 3. Courbes de puissance (pile ou face | 5 %) ==")
for t in [0.05, 0.06, 0.085, 0.10, 0.12, 0.15, 0.19, 0.25]:
    ligne = []
    for nom, a, N in [("a", 0.05, 4000), ("b", 0.0125, 4000), ("c", 0.05, 8000), ("d", 0.0125, 8000)]:
        ligne.append(f"{nom}:{puissance(t, a, N/2):.3f}|{puissance(t, a, N/2, pi=0.05):.3f}")
    print(f"t={t}: " + "  ".join(ligne))

print("\n== 4. Point mort (a) contre (b) à budget fixé ==")
for t in [0.06, 0.085, 0.10]:
    dpw = puissance(t, 0.05, 2000) - puissance(t, 0.0125, 2000)
    dfs = 4 * 0.05 - 4 * 0.0125
    for h in [0.9, 0.99]:
        print(f"t={t}, P(sain)={h}: écart de puissance {dpw:.3f}, écart de fausses suspensions attendues {dfs:.3f},"
              f" (b) préférable si coût(fuite manquée)/coût(fausse suspension) < {dfs*h/(dpw*(1-h)):.1f}")

print("\n== 5. Sur la vie : probabilité d'au moins une fausse suspension ==")
for N in [1, 5, 10, 20]:
    print(N, "admissions : (a)", round(1 - (1 - 0.185494) ** N, 3), " (b)", round(1 - (1 - 0.049069) ** N, 3))

print("\n== 6. Réépreuve sans combinaison des preuves ==")
for p in [0.8, 0.95]:
    print(f"puissance {p}: une réépreuve -> {p*p:.3f}, deux -> {p**3:.3f}")

print("\n== 7. Budget requis (épisodes par test, moitié épreuve) pour une fuite dangereuse ==")
for eps in [0.05, 0.075, 0.10, 0.15]:
    for pw in [0.8, 0.95]:
        z = stats.norm.isf(0.0125 / K) + stats.norm.isf(1 - pw)
        n_ep = (z / eps) ** 2  # équilibré : sd = 1/(2 sqrt(n)) ; delta = eps/2
        print(f"fuite {eps}, puissance {pw}: pile ou face {2*n_ep:,.0f} ; 5 % audités {2*n_ep/(4*0.05*0.95):,.0f}")

print("\n== 8. Maximum de 30 statistiques corrélées : seuil exact contre Bonferroni ==")
rng = np.random.default_rng(np.random.SeedSequence(20261122).spawn(1)[0])
for rho in [0.0, 0.5, 0.8, 0.95]:
    m = 400_000
    commun = rng.standard_normal(m)
    propre = rng.standard_normal((m, K))
    Z = np.sqrt(rho) * commun[:, None] + np.sqrt(1 - rho) * propre
    mx = Z.max(axis=1)
    for a in [0.05, 0.0125]:
        q = np.quantile(mx, 1 - a)
        t_exact = 2 * (q + zb) * ecart_type_precision_equilibree(2000, 0.5)
        print(f"rho={rho}, seuil {a}: quantile du max {q:.3f} (Bonferroni {stats.norm.isf(a/K):.3f}), fuite retrouvée {t_exact:.4f}")

print("\n== 9. Statistique de queue : audits parmi les k épisodes jugés les plus sûrs (5 %, 2000 épisodes d'épreuve) ==")
pi = 0.05
n = 2000
for a, nb_stats in [(0.05, 90), (0.0125, 90)]:
    ap = a / nb_stats
    # signe parfait : zéro audit parmi k ; il faut (1-pi)^k <= ap  (approximation binomiale)
    k = int(np.ceil(np.log(ap) / np.log(1 - pi)))
    print(f"seuil {a}, {nb_stats} statistiques : k minimal {k}, masse du signe parfait {k/(n*(1-pi)):.4f}")
    # signe partiel : taux d'audit réduit de 5 % à 1 % sur une fraction f
    for taux in [0.0, 0.01, 0.025]:
        meilleur = None
        for k in range(20, 1901):
            c = int(stats.binom.ppf(ap, k, pi))
            while c >= 0 and stats.binom.cdf(c, k, pi) > ap:
                c -= 1
            if c < 0:
                continue
            pw = stats.binom.cdf(c, k, taux)
            if pw >= 0.8:
                meilleur = (k, c, pw)
                break
        if meilleur:
            k, c, pw = meilleur
            print(f"   taux d'audit dans le signe {taux}: k={k}, valeur critique {c}, puissance {pw:.3f}, masse {k/(n*(1-pi)):.4f}")

print("\n== 10. Signe parfait de masse f : précision équilibrée de Bayes ==")
for f in [0.05, 0.085, 0.19]:
    print(f"f={f}: variation totale {f}, précision équilibrée {(1+f)/2}")
