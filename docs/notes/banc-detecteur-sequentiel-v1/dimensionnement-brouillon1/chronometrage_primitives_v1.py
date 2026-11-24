"""Chronométrage de primitives numpy (ordre de grandeur du temps de calcul). Tirages déclarés : ils ne portent sur
aucune cellule de la grille ; aucune statistique du banc n'est calculée ni lue (frontière factice linéaire, sorties jetées)."""
import time
import numpy as np

rng = np.random.default_rng(np.random.SeedSequence(0, spawn_key=(999,)))
R, n = 1000, 6400
t0 = time.perf_counter()
u = rng.random((R, n))
t1 = time.perf_counter()
x = 1.0 - (1.0 - u) ** 0.25
t2 = time.perf_counter()
g = np.clip((x - 0.16) / 0.28, 0.0, 1.0)
s = np.cumsum(g - 0.36, axis=1)
front = np.linspace(5.0, 500.0, n)[None, :]
_ = (s >= front).argmax(axis=1)
t3 = time.perf_counter()
z = rng.standard_normal((R, n))
t4 = time.perf_counter()
print(f"tirage uniforme {1e9*(t1-t0)/(R*n):.1f} ns ; puissance {1e9*(t2-t1)/(R*n):.1f} ns ; gain+cumul+frontière {1e9*(t3-t2)/(R*n):.1f} ns ; normale {1e9*(t4-t3)/(R*n):.1f} ns par score")
m = 1_000_000
t0 = time.perf_counter(); r = rng.random(m); r.sort(); t1 = time.perf_counter()
d = rng.random(m); t2 = time.perf_counter()
for _ in range(10):
    gg = np.clip(d + 0.01, 0, 1); ss = np.cumsum(gg - 0.5); _ = (ss >= np.linspace(5, 3000, m)).any()
t3 = time.perf_counter()
print(f"duel : tri de 10^6 {t1-t0:.3f} s ; un pas de dichotomie {0.1*(t3-t2):.4f} s")
