"""Calcul du seuil de la V5 redéfinie (version 3 du préenregistrement de bisociation à deux espaces, brouillon 1).

AUCUN MONDE N'EST GÉNÉRÉ, AUCUN TIRAGE ALÉATOIRE, AUCUNE GRAINE : calcul exact (énumération) et intégration numérique
sur une grille. Aucun module de l'expérience n'est importé. Aucune racine (ni RACINE, ni RACINE_VALIDATION) n'est
employée.

Entrées (toutes citées) :
- loi des émetteurs S16d (uniforme sur {2, 3, 4}, la même pour tous les statuts) et canal des concepts G9 « bien »
  (couverture 0,85 ; parasites 0,05 ; fuite 0,05) et « moyen » (0,65 ; 0,15 ; 0,15), 40 articles, 28 concepts tirables
  en parasite (préenregistrement v2 scellé e821e875…, § 1 G5, G9 ; `monde_v2.py` NIVEAUX_CONCEPTS) ;
- nombres de ponts plantés valides où le concept rare planté est vu des deux côtés, par statut, sur 200 mondes d'essai
  (indices 990000 à 990199), lus dans la sortie du diagnostic `diagnostic-v5-v1-sortie.txt` (faf75a2e…), section (D),
  lignes « T2 … (n : …) » ; ce sont des comptes de plomberie ;
- pour comparaison seulement (jamais employées par la règle du seuil) : moyennes et erreurs types de T2 du même
  diagnostic, sections (D) et (F).

Usage : python3 -B calcul-v5-bisociation-v3-brouillon1.py > calcul-v5-bisociation-v3-brouillon1-sortie.txt
"""
import math

import numpy as np

N_ARTICLES = 40
N_CONCEPTS_PARASITES = 28            # G9 (iii) : parasite tiré uniformément parmi les 28 concepts (fond et rares)
LOI_L = (2, 3, 4)                    # S16d
CANAL = {"M_bien": (0.85, 0.05, 0.05), "M_moyen": (0.65, 0.15, 0.15)}   # (c ; p_par ; rho), G9
STATUTS = ("vrai_conceptuel", "faux", "proche", "vrai_operateur_avec_trace")
# comptes du diagnostic (200 mondes d'essai), section (D)
N_DIAG_200 = {
    "M_bien": {"vrai_conceptuel": 357, "faux": 128, "proche": 356, "vrai_operateur_avec_trace": 483},
    "M_moyen": {"vrai_conceptuel": 188, "faux": 58, "proche": 156, "vrai_operateur_avec_trace": 254},
}
# pour comparaison seulement
MOY_DIAG = {
    "M_bien": {"vrai_conceptuel": 2.824, "faux": 2.875, "proche": 2.961, "vrai_operateur_avec_trace": 2.911},
    "M_moyen": {"vrai_conceptuel": 2.686, "faux": 2.690, "proche": 2.821, "vrai_operateur_avec_trace": 2.783},
}
ET_DIAG_200 = {
    "M_bien": {"vrai_conceptuel": 0.041, "faux": 0.068, "proche": 0.042, "vrai_operateur_avec_trace": 0.038},
    "M_moyen": {"vrai_conceptuel": 0.057, "faux": 0.111, "proche": 0.063, "vrai_operateur_avec_trace": 0.048},
}
N_MONDES_VALIDATION = 300            # S13 : 300 mondes « bien », 300 « moyen »
SEUILS = (0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50)
DECALAGES = (0.20, 0.30, 0.50, 0.75, 1.00)
INFLATIONS = (1.00, 1.25, 1.50)


def binom_pmf(n, p):
    return np.array([math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)])


def loi_df_vu_des_deux(c, p_par, rho):
    """Loi de la fréquence documentaire observée de l'étiquette du concept rare planté, sachant que les deux articles
    du pont l'observent : 2 + (émetteurs de surface comptés) + (autres articles qui la reçoivent en parasite).
    Un émetteur de surface est compté s'il l'émet et qu'elle est couverte sans fuite (c (1 − rho)), ou s'il la
    reçoit en parasite ; un autre article, seulement en parasite (p_par / 28). Les parasites sont tirés par article,
    indépendamment des émissions (G9). Approximation déclarée : on néglige le cas où un article du pont ne l'observe
    que par parasite."""
    q = p_par / N_CONCEPTS_PARASITES
    p_surf = c * (1 - rho) + (1 - c * (1 - rho)) * q
    loi = np.zeros(N_ARTICLES + 1)
    for L in LOI_L:
        a = binom_pmf(L - 2, p_surf)
        b = binom_pmf(N_ARTICLES - L, q)
        conv = np.convolve(a, b)
        loi[2:2 + len(conv)] += conv / len(LOI_L)
    k = np.arange(len(loi))
    moy = float((k * loi).sum())
    var = float(((k - moy) ** 2 * loi).sum())
    return moy, math.sqrt(var)


def Phi(z):
    return 0.5 * (1.0 + np.vectorize(math.erf)(z / math.sqrt(2.0)))


def phi(z):
    return np.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi)


def p_etendue_sup(mus, ses, t, pas=2e-4):
    """P(max − min > t) pour des moyennes normales indépendantes N(mu_k, se_k²) :
    1 − Σ_k ∫ f_k(x) Π_{j≠k} [F_j(x + t) − F_j(x)] dx (k = indice du minimum)."""
    mus, ses = np.asarray(mus, float), np.asarray(ses, float)
    x = np.arange(min(mus - 9 * ses), max(mus + 9 * ses) + pas, pas)
    tot = 0.0
    for k in range(len(mus)):
        f = phi((x - mus[k]) / ses[k]) / ses[k]
        prod = np.ones_like(x)
        for j in range(len(mus)):
            if j != k:
                prod *= Phi((x + t - mus[j]) / ses[j]) - Phi((x - mus[j]) / ses[j])
        tot += np.trapezoid(f * prod, x)
    return 1.0 - tot


def main():
    print("Calcul du seuil de la V5 redéfinie — v3 brouillon 1 — aucun monde, aucun tirage, aucune graine\n")
    print("§ 1. Loi de la fréquence documentaire observée de l'étiquette du concept rare planté, vue des deux côtés")
    print("     (S16d et canal G9 seulement ; identique pour tous les statuts par construction)")
    sd = {}
    for cond, (c, p_par, rho) in CANAL.items():
        moy, s = loi_df_vu_des_deux(c, p_par, rho)
        sd[cond] = s
        diag = MOY_DIAG[cond]
        print(f"  {cond} : espérance {moy:.4f} ; écart-type par pont {s:.4f}   "
              f"(comparaison, diagnostic T2 : {', '.join(f'{k} {v:.3f}' for k, v in diag.items())})")

    print("\n§ 2. Erreurs types attendues par statut à 300 mondes : écart-type du § 1 / racine(n_300),")
    print("     n_300 = 1,5 × compte du diagnostic sur 200 mondes (comptes de plomberie)")
    se = {}
    for cond in CANAL:
        se[cond] = {}
        for st in STATUTS:
            n300 = 1.5 * N_DIAG_200[cond][st]
            se[cond][st] = sd[cond] / math.sqrt(n300)
        comp = {st: ET_DIAG_200[cond][st] * math.sqrt(200 / 300) for st in STATUTS}
        print(f"  {cond} : " + " ; ".join(f"{st} n_300 {1.5 * N_DIAG_200[cond][st]:.0f}, et {se[cond][st]:.4f}"
                                          f" (diag. ramené à 300 : {comp[st]:.4f})" for st in STATUTS))
        pire = max(math.hypot(se[cond][a], se[cond][b]) for a in STATUTS for b in STATUTS if a < b)
        print(f"    erreur type de la plus bruitée des différences entre deux statuts : {pire:.4f}")

    print("\n§ 3. Échec à tort : P(écart maximal > t) si les quatre statuts ont exactement la même loi (S16d tenu)")
    for infl in INFLATIONS:
        print(f"  erreurs types × {infl:.2f}")
        for cond in CANAL:
            ses = [infl * se[cond][st] for st in STATUTS]
            vals = [p_etendue_sup([0, 0, 0, 0], ses, t) for t in SEUILS]
            print(f"    {cond} : " + " ; ".join(f"t={t:.2f} : {v:.4f}" for t, v in zip(SEUILS, vals)))

    print("\n§ 4. Détection : P(écart maximal > t) si UN statut a une espérance décalée de d (les trois autres égaux) ;")
    print("     on rapporte le minimum sur le statut décalé (cas le moins favorable)")
    for infl in (1.00, 1.25):
        print(f"  erreurs types × {infl:.2f}")
        for cond in CANAL:
            ses = [infl * se[cond][st] for st in STATUTS]
            for d in DECALAGES:
                vals = []
                for t in SEUILS:
                    vals.append(min(p_etendue_sup([d if j == k else 0 for j in range(4)], ses, t) for k in range(4)))
                print(f"    {cond}, d = {d:.2f} : " + " ; ".join(f"t={t:.2f} : {v:.3f}" for t, v in zip(SEUILS, vals)))

    print("\n§ 5. Sensibilité (NON employée par la règle) : si les écarts de T2 observés sur les mondes d'essai étaient")
    print("     des écarts vrais (moyennes du diagnostic prises pour espérances), P(écart maximal > t)")
    for infl in (1.00, 1.25):
        for cond in CANAL:
            ses = [infl * se[cond][st] for st in STATUTS]
            mus = [MOY_DIAG[cond][st] for st in STATUTS]
            vals = [p_etendue_sup(mus, ses, t) for t in SEUILS]
            print(f"  × {infl:.2f} {cond} : " + " ; ".join(f"t={t:.2f} : {v:.4f}" for t, v in zip(SEUILS, vals)))

    print("\n§ 6. Règle proposée : plus petit multiple de 0,05 tel que l'échec à tort (§ 3) soit ≤ 0,01 dans chaque")
    print("     condition, avec les erreurs types gonflées de 25 % (marge pour l'approximation du § 1 et la")
    print("     corrélation éventuelle entre ponts d'un même monde) ; puis sa détection d'un décalage de 0,5 (§ 4)")
    retenu = None
    for t in SEUILS:
        ok = all(p_etendue_sup([0, 0, 0, 0], [1.25 * se[c][st] for st in STATUTS], t) <= 0.01 for c in CANAL)
        if ok:
            retenu = t
            break
    print(f"  seuil retenu par la règle : {retenu:.2f}")
    for cond in CANAL:
        for infl in (1.00, 1.25):
            ses = [infl * se[cond][st] for st in STATUTS]
            a_tort = p_etendue_sup([0, 0, 0, 0], ses, retenu)
            det = min(p_etendue_sup([0.5 if j == k else 0 for j in range(4)], ses, retenu) for k in range(4))
            det3 = min(p_etendue_sup([0.3 if j == k else 0 for j in range(4)], ses, retenu) for k in range(4))
            print(f"  {cond}, × {infl:.2f} : échec à tort {a_tort:.4f} ; détection d = 0,5 : {det:.3f} ; d = 0,3 : {det3:.3f}")
    print("  comparaison, ancien seuil 0,50 appliqué à la grandeur nouvelle :")
    for cond in CANAL:
        ses = [se[cond][st] for st in STATUTS]
        det = min(p_etendue_sup([0.5 if j == k else 0 for j in range(4)], ses, 0.50) for k in range(4))
        det75 = min(p_etendue_sup([0.75 if j == k else 0 for j in range(4)], ses, 0.50) for k in range(4))
        print(f"    {cond} : échec à tort {p_etendue_sup([0, 0, 0, 0], ses, 0.50):.2e} ; détection d = 0,5 : {det:.3f} ;"
              f" d = 0,75 : {det75:.3f}")


if __name__ == "__main__":
    main()
