"""Contrôle de lz76 du script contre l'algorithme de Kaspar et Schuster (1987), écrit indépendamment."""
import importlib.util, sys
import numpy as np
spec = importlib.util.spec_from_file_location("ci", sys.argv[1]); ci = importlib.util.module_from_spec(spec); spec.loader.exec_module(ci)

def kaspar_schuster(s):
    n = len(s)
    if n == 1:
        return 1
    i, k, l, c, k_max = 0, 1, 1, 1, 1
    while True:
        if s[i + k - 1] == s[l + k - 1]:
            k += 1
            if l + k > n:
                c += 1
                break
        else:
            if k > k_max:
                k_max = k
            i += 1
            if i == l:
                c += 1
                l += k_max
                if l + 1 > n:
                    break
                i, k, k_max = 0, 1, 1
            else:
                k = 1
    return c

print("exemple 0001101001000101 :", ci.lz76("0001101001000101"), kaspar_schuster("0001101001000101"))
rng = np.random.default_rng(np.random.SeedSequence(99).spawn(1)[0])
ecarts = 0
for essai in range(400):
    n = int(rng.integers(2, 400)); p = float(rng.random())
    s = "".join("1" if v else "0" for v in (rng.random(n) < p))
    a, b = ci.lz76(s), kaspar_schuster(s)
    if a != b:
        ecarts += 1
        if ecarts <= 5: print("ecart", s[:60], a, b)
print("suites testees : 400 ; ecarts :", ecarts)
