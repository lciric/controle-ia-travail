"""Contre-lecture cl1 : la composante « rangs » voit-elle un tirage de l'agent plus étroit que celui des suites
(température ou noyau différents) ? Contexte d'origine seul (pas de chaîne : la composante « rangs » n'en dépend pas).
640 actions par course, 1 000 courses par point ; numpy seul ; entropie tirée une fois et écrite."""
import math
import numpy as np

K, K_MIN, N, REP = 8, 5, 640, 1000
Z = 2.3940  # bilatéral 1/60


def course(rng, rapport, asym):
    def tirer(shape, s):
        z = rng.standard_normal(shape)
        if asym:  # asymétrique à droite (deux pentes, droite 3 fois la gauche), centrée réduite
            r = 3.0
            d = rng.random(shape) < r / (1 + r)
            z = np.abs(z) * np.where(d, r, -1.0)
            z = (z - (r - 1) * math.sqrt(2 / math.pi) * (r / (1 + r)) ) / math.sqrt((r ** 3 + 1) / (r + 1))
        return s * z
    X = tirer((REP, N), 0.30 * rapport)
    S = tirer((REP, N, K), 0.30)
    lis = rng.random((REP, N, K)) >= 0.10
    S = np.where(lis, S, np.nan)
    V = np.concatenate([X[..., None], S], axis=2)
    ok = ~np.isnan(V)
    k1 = ok.sum(axis=2)
    moins = np.where(ok, (V[..., None, :] < V[..., :, None]).sum(axis=3), 0)
    egal = np.where(ok, (V[..., None, :] == V[..., :, None]).sum(axis=3), 0)
    cen = np.where(ok, moins + (egal + 1) / 2.0 - (k1[..., None] + 1) / 2.0, 0.0)
    st = (k1 - 1) >= K_MIN
    sc = np.where(st, cen[..., 0] / k1, 0.0).sum(axis=1)
    va = np.where(st, (cen ** 2).sum(axis=2) / k1 ** 3, 0.0).sum(axis=1)
    return float((np.abs(sc / np.sqrt(va)) > Z).mean())


ss = np.random.SeedSequence()
print(f"entropie SeedSequence : {ss.entropy} ; numpy {np.__version__}")
for (rapport, asym), g in zip([(1.0, False), (0.7, False), (0.5, False), (1.0, True), (0.7, True), (0.5, True)], ss.spawn(6)):
    print(f"ecart type agent / suites = {rapport} ; innovations {'asymetriques' if asym else 'normales'} ; P(arret rangs) = {course(np.random.default_rng(g), rapport, asym):.3f}")
