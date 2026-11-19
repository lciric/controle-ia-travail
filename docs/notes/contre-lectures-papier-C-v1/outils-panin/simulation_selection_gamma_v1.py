"""Mesure de conception (aucune donnée lue) : la règle de l'addendum, qui ordonne et choisit les formulations par
γ (gain vers la destination imposée v*), biaise-t-elle λ de C-P1 vers la cible quand les destinations diffèrent à
l'intérieur d'une famille ? Comparaison avec un choix par g_sép = −pente de la loi séparée (sans destination) et
avec un choix au hasard. Monde synthétique, déclaré ci-dessous ; ce n'est pas une prédiction.

Usage : python -B -I simulation_selection_gamma_v1.py
"""
import numpy as np

V_ETOILE = 0.0          # cible de l'attaquant, corpus A (suspicion minimale)
N_CAL, N_ET2 = 60, 120  # contenus de calibrage, contenus de l'étape 2
K = 4                   # formulations retenues par famille
BRUIT = 0.3             # écart type du bruit de lecture sur Δ
REPETITIONS = 1000
GRILLE = np.arange(-30.0, 40.0001, 0.05)  # grille grossière, puis section dorée (comme le brouillon 4, point 8)


def contenus(rng, n):
    return rng.uniform(1.0, 8.0, size=n)


def deplacements(rng, v0, g, c):
    return g * (c - v0) + rng.normal(0.0, BRUIT, size=v0.shape)


def gamma(delta, v0):
    d = V_ETOILE - v0
    return float(np.sum(delta * d) / np.sum(d * d))


def g_sep(delta, v0):
    pente = np.polyfit(v0, delta, 1)[0]
    return float(-pente)


def choisir(scores, k):
    """Règle de l'addendum : cibles également espacées entre min et max, formulation non retenue la plus proche."""
    smin, smax = float(np.min(scores)), float(np.max(scores))
    retenues = []
    for m in range(k):
        t = smin + m * (smax - smin) / (k - 1)
        libres = [j for j in range(len(scores)) if j not in retenues]
        j = min(libres, key=lambda j: (abs(scores[j] - t), j))
        retenues.append(j)
    return retenues


def rss_c(c, deltas, v0):
    x = c - v0
    sxx = float(np.sum(x * x))
    return float(sum(np.sum(d * d) - (x @ d) ** 2 / sxx for d in deltas))


def loi_jointe(deltas, v0):
    """deltas : tableau (k, n). Profil de la somme résiduelle en c : grille, puis section dorée à 1e-6 près."""
    x = GRILLE[:, None] - v0[None, :]
    sxx = np.sum(x * x, axis=1)
    rss = np.zeros_like(GRILLE)
    for d in deltas:
        sxy = x @ d
        rss += np.sum(d * d) - sxy * sxy / sxx
    i = int(np.argmin(rss))
    a, b = GRILLE[max(i - 1, 0)], GRILLE[min(i + 1, len(GRILLE) - 1)]
    phi = (np.sqrt(5.0) - 1.0) / 2.0
    while b - a > 1e-6:
        c1, c2 = b - phi * (b - a), a + phi * (b - a)
        if rss_c(c1, deltas, v0) <= rss_c(c2, deltas, v0):
            b = c2
        else:
            a = c1
    return 0.5 * (a + b)


def une_famille(rng, part_cible):
    n_f = 16
    g = rng.uniform(0.05, 0.5, size=n_f)
    v_moy = 4.5
    c = np.where(np.arange(n_f) < int(round(part_cible * n_f)), V_ETOILE, v_moy)
    v0_cal = contenus(rng, N_CAL)
    d_cal = np.array([deplacements(rng, v0_cal, g[f], c[f]) for f in range(n_f)])
    s_gamma = np.array([gamma(d, v0_cal) for d in d_cal])
    s_gsep = np.array([g_sep(d, v0_cal) for d in d_cal])
    choix = {
        "gamma (règle du brouillon 4)": choisir(s_gamma, K),
        "g_sep (sans destination)": choisir(s_gsep, K),
        "hasard": list(rng.choice(n_f, size=K, replace=False)),
    }
    v0 = contenus(rng, N_ET2)
    v_barre = float(np.mean(v0))
    sortie = {}
    for nom, ret in choix.items():
        d = np.array([deplacements(rng, v0, g[f], c[f]) for f in ret])
        c_chap = loi_jointe(d, v0)
        lam = (c_chap - v_barre) / (V_ETOILE - v_barre)
        sortie[nom] = (lam, float(np.mean(c[ret] == V_ETOILE)))
    return sortie


def main():
    racine = np.random.SeedSequence(20261020)
    for part in (0.5, 0.25):
        rng = np.random.default_rng(racine.spawn(1)[0])
        acc = {}
        for _ in range(REPETITIONS):
            for nom, (lam, part_ret) in une_famille(rng, part).items():
                acc.setdefault(nom, []).append((lam, part_ret))
        print(f"Part des formulations du vivier tirées vers v* : {part:.2f} (le reste vers la moyenne)")
        for nom, val in acc.items():
            a = np.array(val)
            print(f"  {nom:30s} λ moyen {np.mean(a[:, 0]):+.3f} ; part λ > 0,5 : {np.mean(a[:, 0] > 0.5):.3f} ;"
                  f" part des retenues tirées vers v* : {np.mean(a[:, 1]):.3f}")


if __name__ == "__main__":
    main()
