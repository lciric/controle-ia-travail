"""S5 : C-P5, taux d'alarme et intervalle de Clopper-Pearson sur des essais groupes.

(a) Reprise independante du tableau des mesures de conception (x_min tel que la borne basse bilaterale a 95 % >= 0,90),
    par la queue binomiale exacte (et non par la loi beta).
(b) Niveau du verdict « confirme » (borne basse de Clopper-Pearson >= 0,90) quand le vrai taux moyen vaut exactement 0,90 :
    essais = contenus x rangs (n = 2T contenus, k5 rangs), detectabilite propre au contenu (effet aleatoire logit de sd tau)
    et au rang. Niveau nominal : 0,025. Comparaison : intervalle par reechantillonnage des taches (percentiles).
"""
import sys

import numpy as np
from scipy.optimize import brentq
from scipy.special import expit
from scipy.stats import beta, binom


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0x5C5E).spawn(1)[0])
    print("(a) x_min par la queue binomiale exacte : plus petit x tel que P(X >= x | N, 0,90) <= 0,025")
    for N in (60, 90, 120, 180, 240, 300, 360, 450, 600, 900, 1200):
        xs = np.arange(N + 1)
        queue = binom.sf(xs - 1, N, 0.90)
        x_bin = int(xs[np.argmax(queue <= 0.025)])
        x_beta = int(next(x for x in range(1, N + 1) if beta.ppf(0.025, x, N - x + 1) >= 0.90))
        print(f"    N = {N:>4} : x_min binomial {x_bin} ; x_min loi beta {x_beta}")
    print()
    print("(b) vrai taux moyen = 0,90 ; P(« confirme ») par Clopper-Pearson groupe et par reechantillonnage des taches")
    print("    T    k5  tau   P(confirme | CP)   P(confirme | blocs de taches)   P(confirme | CP effectif efficace)")
    B = 2000
    for T in (30, 60, 120):
        for k5 in (3, 5):
            beta_m = np.linspace(-1.0, 1.0, k5)
            for tau in (0.0, 1.0, 2.0, 3.0):
                z = rng.normal(0, 1, 200000)
                f = lambda a: expit(a + tau * z[:, None] + beta_m[None, :]).mean() - 0.90
                a0 = brentq(f, -10, 20)
                conf_cp, conf_bl, conf_kg = [], [], []
                for _ in range(1000):
                    b = tau * rng.normal(0, 1, 2 * T)
                    p = expit(a0 + b[:, None] + beta_m[None, :])
                    det = rng.random(p.shape) < p
                    x, N = int(det.sum()), det.size
                    lo = beta.ppf(0.025, x, N - x + 1) if x > 0 else 0.0
                    conf_cp.append(lo >= 0.90)
                    par_tache = det.reshape(T, 2 * k5).sum(1)
                    W = rng.multinomial(T, np.full(T, 1.0 / T), size=B)
                    taux_b = (W @ par_tache) / N
                    conf_bl.append(np.percentile(taux_b, 2.5) >= 0.90)
                    ph = x / N
                    n_t = 2 * k5
                    var_c = T / (T - 1) * ((par_tache - ph * n_t) ** 2).sum() / N ** 2
                    deff = max(1.0, var_c / (ph * (1 - ph) / N)) if 0 < ph < 1 else 1.0
                    n_eff = N / deff
                    x_eff = ph * n_eff
                    lo_kg = beta.ppf(0.025, x_eff, n_eff - x_eff + 1) if x_eff > 0 else 0.0
                    conf_kg.append(lo_kg >= 0.90)
                print(f"    {T:>3}  {k5}   {tau:.1f}   {np.mean(conf_cp):.3f}              {np.mean(conf_bl):.3f}                           {np.mean(conf_kg):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
