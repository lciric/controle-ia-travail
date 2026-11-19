"""Prédiction au premier ordre (§ 6 (d)) pour les miniatures « structure-32 » et « structure-128 » de l'auteur (partie A, T = 128),
à comparer à la mesure appariée de l'addendum (≈ −4,5/M en relatif). Monde de l'auteur reconstruit par son programme (même
entropie, même clé de monde) ; tirages du contre-lecteur, graine propre. Usage : python -I -B prediction_miniature_auteur.py CHEMIN_PROGRAMME ENTROPIE"""
import importlib.util
import sys

import numpy as np

spec = importlib.util.spec_from_file_location("sim", sys.argv[1])
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)
entropie = int(sys.argv[2])
T, n = 128, 600_000
for idx, sc in enumerate(("structure-32", "structure-128")):
    wg = sim.monde(sc, "A", T)
    g = np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=entropie, spawn_key=(3 * 10**6 + idx,))))
    ref = sim.scores(g, sc, 400_000, T, wg)
    mu, sd = ref.mean(0), ref.std(0)
    a = (sim.scores(g, sc, n, T, wg) - mu) / sd          # z « M infini »
    C = a.max(1)
    arg = a.argmax(1)
    q = np.quantile(C, 0.95)
    lar = 0.05 * C.std()
    fen = np.abs(C - q) < lar
    h = fen.mean() / (2 * lar) / 0.05
    pi = np.bincount(arg[fen], minlength=T).astype(float)
    pi /= pi.sum()                                       # jeton de culmination d'une nulle au seuil
    D = ((C[:, None] * (a * a - 1) / 2 + a) * pi[None, :]).sum(1)
    ed, et = D[fen].mean(), D[fen].std() / np.sqrt(fen.sum())
    print(f"{sc} : q = {q:.3f} ; h = {h:.3f} ; E[M·δ | C ≈ q] = {ed:+.3f} ± {et:.3f} ; prédit {-h * ed:+.2f} / M")
