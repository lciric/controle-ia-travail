"""Re-dérivation indépendante de la puissance du test par inversion de signe, unilatéral, α = 0,05 (code et graine du relecteur).
Objets de contrôle : δ = 0 (le taux de rejet doit être ≤ 0,05 : faux par construction) ; δ grand (≈ 1 : vrai par construction).
Variante « bornée et discrète » : couvertures de (a) et B3 tirées en composantes sur 7 (plafond à 1), pour voir l'effet du plafond.
Usage : puissance_independante_v1.py"""
import itertools
import numpy as np

rng = np.random.default_rng(np.random.SeedSequence(777001))
N = 12
SIGNES = np.array(list(itertools.product((-1.0, 1.0), repeat=N)))  # 4 096 × 12


def p_valeur(d):
    obs = d.mean()
    return float(np.mean(SIGNES @ d / N >= obs - 1e-12))


def puissance(tirer, sims=2000):
    return np.mean([p_valeur(tirer()) <= 0.05 for _ in range(sims)])


for sd in (0.15, 0.195):
    for delta in (0.0, 0.05, 0.10, 0.15, 0.6):
        print(f"normale n=12 sd={sd} delta={delta} : {puissance(lambda: rng.normal(delta, sd, N)):.3f}")

# variante bornée : B3 par monde = couvertures v1 (sur 7 composantes en moyenne) ; (a) = B3 + k composantes, k ~ arrondi N(δ·7, σ·7), plafonné à 7
b3 = np.array([0.7143, 0.5714, 0.75, 0.8333, 0.8571, 0.6667, 0.8333, 0.8333, 0.5714, 0.4286, 0.625, 0.5714])
for sd in (0.15, 0.195):
    for delta in (0.0, 0.15):
        def tirer():
            base = rng.permutation(b3)
            k = np.round(rng.normal(delta * 7, sd * 7, N)) / 7
            a = np.clip(base + k, 0, 1)
            return a - base
        print(f"bornée n=12 sd={sd} delta={delta} : {puissance(tirer):.3f}")
