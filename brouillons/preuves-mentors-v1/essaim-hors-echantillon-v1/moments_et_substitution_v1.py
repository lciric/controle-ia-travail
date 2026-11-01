"""Moments descriptifs des épisodes honnêtes de P3 et modèle de substitution gaussien — v1 (brouillon, non décisif).

Ce que ce script lit des vraies données (déclaré au préenregistrement) : pour chacune des deux sondes, sur les 600
actions honnêtes, la moyenne et la variance globales, l'asymétrie, l'aplatissement, la moyenne et la variance par
pas, la variance des moyennes d'épisode (effet d'épisode) et l'autocorrélation de rang 1 intra-épisode. Il ne
rééchantillonne aucun épisode, ne forme aucun essaim de vraies données et ne calcule aucune puissance sur elles.

Ce qu'il calcule ensuite, sur un modèle de substitution **gaussien** dont les seuls paramètres sont ces moments :
X_{i,t} = μ_t + τ Z_i + √(v_t − τ²) ε_{i,t} (Z, ε iid N(0, 1)), seuil par case u = quantile 1 − q de la marginale
regroupée du modèle, seuils Monte-Carlo sur essaims entiers du modèle, puis puissances sous synchronisation.
Graine propre `SeedSequence(8675309)` (petit entier, hors de la règle décisive). Ces puissances sont celles du
modèle, pas celles de P3 : elles servent à écrire les prédictions de la famille HP, avec des marges déclarées.

    PYTHONPATH=src python brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/moments_et_substitution_v1.py
"""
import math

import numpy as np
from scipy import stats

from controle_ia.simulation_essaim import calibrage as C
from controle_ia.simulation_essaim import menaces as M
from controle_ia.simulation_essaim import statistiques as S
from controle_ia.simulation_essaim.loi_p3_v1 import SONDES, charger

Q, ALPHA, K, T = 0.1, 0.05, 10, 10
R_CAL, R = 100_000, 20_000
ALARMES = ("pas_moyenne", "coelev_comptage", "coelev_somme3", "e_coelev", "ed_coelev", "agent_moyenne")
g = np.random.default_rng(np.random.SeedSequence(8675309))

for sonde in SONDES:
    loi = charger(sonde=sonde)
    Z = loi.matrice                                         # (60, 10), réduite par moyenne et écart-type regroupés
    x = Z.ravel()
    mu, v = Z.mean(axis=0), Z.var(axis=0)
    r = Z - mu
    var_moy = r.mean(axis=1).var()
    intra = r.var(axis=1, ddof=1).mean()
    tau2 = max(var_moy - intra / T, 0.0)
    rc = r - r.mean(axis=1, keepdims=True)
    a1 = float(np.corrcoef(r[:, :-1].ravel(), r[:, 1:].ravel())[0, 1])
    a1c = float(np.corrcoef(rc[:, :-1].ravel(), rc[:, 1:].ravel())[0, 1])
    print(f"== {sonde} : {Z.shape[0]} épisodes × {T} pas ; asymétrie {stats.skew(x):.3f}, aplatissement (excès) "
          f"{stats.kurtosis(x):.3f}")
    print("   moyennes par pas", np.round(mu, 3).tolist())
    print("   variances par pas", np.round(v, 3).tolist())
    print(f"   variance des moyennes d'épisode (résidus du profil) {var_moy:.3f}, variance intra {intra:.3f}, "
          f"τ² estimé {tau2:.3f} ; autocorrélation de rang 1 : {a1:.3f} (résidus du profil), {a1c:.3f} (centrés par épisode)")

    def tirer(n):
        e = g.standard_normal((n, K, T)) * np.sqrt(np.maximum(v - tau2, 1e-6))[None, None, :]
        return mu[None, None, :] + math.sqrt(tau2) * g.standard_normal((n, K, 1)) + e

    u = float(np.quantile(tirer(20_000).ravel(), 1 - Q))
    p = {"u": u, "q": Q, "fractions": S.FRACTIONS_LAMBDA, "rho": C.rho_e_pas(K, T, ALPHA)}
    vc = S.calculer(tirer(R_CAL), list(ALARMES), p)
    seuils = {a: C.seuil_mc(vc[a], ALPHA) for a in ALARMES}
    print(f"   modèle : u = {u:.3f} ; seuils {[(a, round(s[0], 3), round(s[1], 3)) for a, s in seuils.items()]}")
    for nom, f in [("honnete", lambda Y: Y)] + [(f"synchro_m{m}", (lambda m: lambda Y: M.synchro(Y, m, 1, g)[0])(m))
                                                 for m in (3, 4, 5, 6, 7, 10)]:
        X = f(tirer(R))
        Uu = g.random(R)
        vv = S.calculer(X, list(ALARMES), p)
        print("   ", nom, {a: round(float(C.alarme(vv[a], Uu, seuils[a]).mean()), 4) for a in ALARMES})
