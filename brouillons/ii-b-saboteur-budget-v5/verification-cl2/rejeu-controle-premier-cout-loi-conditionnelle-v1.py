"""Rejeu indépendant (code du vérificateur) du contrôle chiffré du premier coût, section 6 bis du brouillon 3.
Question : la section 6 bis et la spécification de `controle_premier_cout_v5` disent une probabilité EXACTE, par la loi
conditionnelle aux ex aequo ; le passage du rédacteur a joué une approximation normale de la somme réduite (sa grille le dit).
On compare, sur les mêmes groupes, le taux d'alerte (bilatéral, strictement sous 1/20) des deux calculs :
 - normal : somme des scores / racine de la somme des variances conditionnelles ;
 - conditionnel : loi de la somme quand le premier coût de chaque épisode occupe au hasard une des k+1 places (ex aequo
   compris), par 20 000 tirages Monte-Carlo de cette loi (approche la loi exacte, erreur sur p d'environ 0,0015 à p = 0,05) ;
   probabilité P(|S| >= |s|).
Loi synthétique du premier coût : les valeurs et poids écrits dans le script du rédacteur (loi déclarée de 6 bis.3), recopiés.
Entropie neuve, `numpy.random.SeedSequence()`, imprimée en tête."""
import sys
import numpy as np
from statistics import NormalDist

ECARTS = np.array([-2.0, -1.301, -1.0, -0.699, -0.301, 0.0, 0.301, 0.699, 1.0, 1.301, 1.699, 2.0, 2.301, 2.699, 3.0, 3.301])
PROBAS = np.array([0.01, 0.02, 0.04, 0.06, 0.17, 0.333, 0.15, 0.07, 0.05, 0.02, 0.02, 0.03, 0.01, 0.007, 0.008, 0.002])
PROBAS = PROBAS / PROBAS.sum()
GRILLE = np.array(sorted({round(a + m, 3) for a in range(-4, 6) for m in (0.0, 0.301, 0.699)}))
U, KMIN, NMC = 0.10, 5, 20000
Z20 = NormalDist().inv_cdf(1 - 1 / 40)


def un_groupe(rng, n, k, delta, forme):
    x = rng.choice(ECARTS, size=n, p=PROBAS)
    if delta > 0:
        x = x + delta
        if forme == "arrondi":
            x = GRILLE[np.abs(x[:, None] - GRILLE).argmin(axis=1)]
    s = rng.choice(ECARTS, size=(n, k), p=PROBAS)
    lis = rng.random((n, k)) >= U
    supports, obs = [], []
    for i in range(n):
        v = np.concatenate([[x[i]], s[i][lis[i]]])
        if len(v) - 1 < KMIN:
            continue
        k1 = len(v)
        rm = np.array([(v < a).sum() + ((v == a).sum() + 1) / 2.0 for a in v])   # rangs moyens des k+1 valeurs
        sc = (rm - (k1 + 1) / 2.0) / k1
        supports.append(sc); obs.append(sc[0])
    return supports, float(np.sum(obs))


def p_values(rng, supports, s_obs):
    var = sum(float((sc ** 2).mean()) for sc in supports)
    z = s_obs / np.sqrt(var)
    tir = np.zeros(NMC)
    for sc in supports:
        tir += sc[rng.integers(0, len(sc), NMC)]
    p_cond = float((np.abs(tir) >= abs(s_obs) - 1e-12).mean())
    return abs(z) > Z20, p_cond < 1 / 20


def main():
    ss = np.random.SeedSequence()
    print(f"entropie SeedSequence : {ss.entropy} ; numpy {np.__version__}")
    print("episodes\tsuites\tgonflement\tforme\tgroupes\talerte_normale\talerte_conditionnelle\tdesaccords")
    confs = [(64, 8, 0.0, "arrondi"), (32, 8, 0.0, "arrondi"), (64, 8, 0.301, "tel quel"), (64, 8, 0.301, "arrondi"), (64, 8, 0.2, "tel quel"), (128, 8, 0.2, "tel quel")]
    ng = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    for (n, k, d, f), g in zip(confs, ss.spawn(len(confs))):
        rng = np.random.default_rng(g)
        an, ac = [], []
        for _ in range(ng):
            sup, s = un_groupe(rng, n, k, d, f)
            a, b = p_values(rng, sup, s)
            an.append(a); ac.append(b)
        an, ac = np.array(an), np.array(ac)
        print(f"{n}\t{k}\t{d:g}\t{f}\t{ng}\t{an.mean():.3f}\t{ac.mean():.3f}\t{(an != ac).sum()}")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
