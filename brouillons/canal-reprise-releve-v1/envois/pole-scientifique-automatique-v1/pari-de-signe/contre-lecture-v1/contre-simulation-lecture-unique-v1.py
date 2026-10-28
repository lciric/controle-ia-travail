"""Lecture unique à n fixé (porte lue une fois, N-050) : test de Student unilatéral apparié au niveau des tâches, contre le
pari (forme parts seule, lecture continue). Même monde que la pièce. Contre-lecture R2, exploratoire."""
import importlib.util, json, math, sys
import numpy as np
spec = importlib.util.spec_from_file_location("cs", sys.argv[1]); cs = importlib.util.module_from_spec(spec); spec.loader.exec_module(cs)
T95 = {15: 1.761, 20: 1.729, 30: 1.699, 40: 1.685, 60: 1.671, 100: 1.660, 150: 1.655, 250: 1.651}
rng = np.random.default_rng(np.random.SeedSequence(2718281828))
R = 2000
def student(v):
    n = v.shape[1]; m = v.mean(1); s = v.std(1, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(s > 0, m / (s / math.sqrt(n)), np.where(m > 0, np.inf, -np.inf))
    return float((t > T95[n]).mean())
out = {"entropie_SeedSequence": 2718281828, "repetitions": R}
for nom, (a, b, ns) in {"ecart_0.20": (0.6, 0.4, (15, 20, 30, 40)), "ecart_0.10": (0.5, 0.4, (30, 40, 60, 100))}.items():
    out[nom] = {}
    for n in ns:
        v = cs.parts(rng, R, n, 10, a, b)
        out[nom][n] = {"student_lecture_unique": student(v), "pari_parts_continu": float(cs.promu(cs.logw([v], [1.0])).mean())}
types = [(0.9, 0.55, 0.45), (0.1, 0.05, 0.95)]
out["niveau_nul_asymetrique_S1"] = {}
for n in (15, 20, 30, 60, 100):
    pA, pB = cs.melange_types(rng, R, n, types)
    v = cs.parts(rng, R, n, 10, pA, pB)
    out["niveau_nul_asymetrique_S1"][n] = {"student_lecture_unique": student(v), "pari_parts_continu": float(cs.promu(cs.logw([v], [1.0])).mean())}
print(json.dumps(out, ensure_ascii=False, indent=1))
