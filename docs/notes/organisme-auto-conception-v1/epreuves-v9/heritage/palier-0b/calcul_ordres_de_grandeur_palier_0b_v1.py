"""Ordres de grandeur du redacteur pour le preenregistrement du palier 0b (v1).
Calcul analytique seul : aucun tirage, aucune simulation, aucun resultat de l etage.
Bibliotheque standard et numpy. Sortie JSON sur la sortie standard."""
import json, math
from statistics import NormalDist
import numpy as np

N = 10000
LOGFACT = np.concatenate(([0.0], np.cumsum(np.log(np.arange(1, N + 1, dtype=np.float64)))))
INDICES = np.arange(0, N + 1, dtype=np.float64)
LOGCOMB = LOGFACT[N] - LOGFACT - LOGFACT[::-1]

def cdf(k, p):
    """P(X <= k), X binomiale (N, p), 0 < p < 1."""
    logpmf = LOGCOMB + INDICES * math.log(p) + (N - INDICES) * math.log1p(-p)
    return float(min(1.0, np.exp(logpmf[: k + 1]).sum()))

def clopper_pearson(k, niveau=0.95):
    """Intervalle binomial exact (Clopper et Pearson) par dichotomie sur la loi binomiale."""
    a = (1.0 - niveau) / 2.0
    if k == 0:
        bas = 0.0
    else:
        lo, hi = 1e-12, 1.0 - 1e-12
        for _ in range(60):
            m = (lo + hi) / 2.0
            if 1.0 - cdf(k - 1, m) < a: lo = m
            else: hi = m
        bas = (lo + hi) / 2.0
    if k == N:
        haut = 1.0
    else:
        lo, hi = 1e-12, 1.0 - 1e-12
        for _ in range(60):
            m = (lo + hi) / 2.0
            if cdf(k, m) > a: lo = m
            else: hi = m
        haut = (lo + hi) / 2.0
    return [round(bas, 5), round(haut, 5)]

def sources_approx_normale(delta, alpha_bilateral, puissance=0.8):
    z = NormalDist()
    brut = (z.inv_cdf(1 - alpha_bilateral / 2) + z.inv_cdf(puissance)) ** 2 / delta ** 2
    return {"taille_reduite": delta, "alpha_bilateral": alpha_bilateral,
            "n_test_de_student_approx": round(brut, 2),
            "n_rangs_signes_approx_efficacite_3_sur_pi": round(brut / (3 / math.pi), 2)}

s = {"tirages_par_case": N, "intervalles_a_95_pour_cent": {},
     "sources_par_approximation_normale": []}
for k in (400, 450, 500, 550, 600, 7800, 7900, 8000, 8100):
    s["intervalles_a_95_pour_cent"][str(k)] = clopper_pearson(k)
lo, hi = 0, N  # plus grand compte dont la borne haute est au plus 0,06
while hi - lo > 1:
    m = (lo + hi) // 2
    if clopper_pearson(m)[1] <= 0.06: lo = m
    else: hi = m
s["plus_grand_compte_dont_la_borne_haute_est_au_plus_0_06"] = lo
lo, hi = 0, N  # plus petit compte dont la borne basse est au moins 0,79
while hi - lo > 1:
    m = (lo + hi) // 2
    if clopper_pearson(m)[0] >= 0.79: hi = m
    else: lo = m
s["plus_petit_compte_dont_la_borne_basse_est_au_moins_0_79"] = hi
for d in (0.5, 0.75, 1.0, 1.5):
    for a in (0.025, 0.05):
        s["sources_par_approximation_normale"].append(sources_approx_normale(d, a))
ref = sources_approx_normale(0.5, 0.025)["n_rangs_signes_approx_efficacite_3_sur_pi"]
s["sources_a_taille_0_5_majorees_par_une_part_nulle_de_0_15"] = round(ref / 0.85, 2)
print(json.dumps(s, indent=1, sort_keys=True))
