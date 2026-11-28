# Quelles combinaisons donnent un texte different selon l'ordre d'application ? (en memoire)
import sys, itertools, difflib, importlib.util
from collections import Counter
spec = importlib.util.spec_from_file_location("opt", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
c = Counter(); ex = {}
for N031, N032, P016, P023, P024 in itertools.product("abc", "ABC", "ABC", "ABC", "ABC"):
    o = {"N-031": N031, "N-032": N032, "P-016": P016, "P-017": "A", "P-023": P023, "P-024": P024}
    t1, _ = m.candidat(o, False, True); t2, _ = m.candidat(o, True, True)
    if t1 != t2:
        k = (N031 in "bc", P023, N032, P016, P024)
        c[(N031 in "bc", P023)] += 1
        if (N031 in "bc", P023) not in ex:
            d = [l for l in difflib.unified_diff(m.norm(t1).split(" ; "), m.norm(t2).split(" ; "), lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
            ex[(N031 in "bc", P023)] = (m.nom(o), d[:6])
for k, v in c.items(): print(k, v, ex[k][0]); [print("   ", x[:300]) for x in ex[k][1]]
