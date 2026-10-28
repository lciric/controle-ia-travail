"""Tests structurels (v1), sans lecture de précision : instruments et invariants des bras.
Usage : python3 -I -B tests_v1.py
"""
import math
import random
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import conditions_v1 as cd
import mesures_v1 as ms
import methodes_v1 as mt
import monde_v1 as mo


def det(m):
    m = [list(r) for r in m]
    n, d = len(m), 1.0
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(m[r][c]))
        if abs(m[piv][c]) < 1e-300:
            return 0.0
        if piv != c:
            m[c], m[piv] = m[piv], m[c]
            d = -d
        d *= m[c][c]
        for r in range(c + 1, n):
            f = m[r][c] / m[c][c]
            for k in range(c, n):
                m[r][k] -= f * m[c][k]
    return d


def jacobi_valeurs_propres(a, balayages=100):
    a = [list(r) for r in a]
    n = len(a)
    for _ in range(balayages):
        hors = sum(a[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if hors < 1e-22:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                theta = (a[q][q] - a[p][p]) / (2 * a[p][q])
                t = (1 if theta >= 0 else -1) / (abs(theta) + math.sqrt(theta * theta + 1))
                c = 1 / math.sqrt(t * t + 1)
                s = t * c
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p], a[k][q] = c * akp - s * akq, s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k], a[q][k] = c * apk - s * aqk, s * apk + c * aqk
    return sorted(a[i][i] for i in range(n))


def test_glouton():
    """L'ordre glouton par Cholesky incrémentale = glouton par déterminants explicites (8 articles, 50 cas)."""
    rng = random.Random(1)
    for _ in range(50):
        n = 8
        v = [[rng.gauss(0, 1) for _ in range(5)] for _ in range(n)]
        nv = [math.sqrt(sum(x * x for x in r)) for r in v]
        cos = [[sum(a * b for a, b in zip(v[i], v[j])) / (nv[i] * nv[j]) for j in range(n)] for i in range(n)]
        q = [rng.uniform(0.5, 1.5) for _ in range(n)]
        ordre = mt.ordre_glouton({"n": n, "cos": cos}, q)
        l = [[q[i] * q[j] * (cos[i][j] ** 2 + (mt.GAMMA_CORRECTIF if i == j else 0)) for j in range(n)] for i in range(n)]
        pris = []
        while len(pris) < n:
            pris.append(max((c for c in range(n) if c not in pris),
                            key=lambda c: det([[l[a][b] for b in pris + [c]] for a in pris + [c]])))
        assert ordre == pris, (ordre, pris)
    return "ordre glouton = glouton par déterminants (50 / 50)"


def test_gamma():
    """gamma_minimal = - plus petite valeur propre (Jacobi) pour des matrices symétriques à diagonale nulle."""
    rng = random.Random(2)
    pire = 0.0
    for _ in range(30):
        n = 7
        m = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                m[i][j] = m[j][i] = rng.uniform(0, 1)
        g = mt.gamma_minimal(m)
        lmin = jacobi_valeurs_propres(m)[0]
        pire = max(pire, abs(g + lmin))
    assert pire < 1e-6, pire
    return f"gamma minimal = -lambda_min à {pire:.1e} près (30 / 30)"


def test_tirage():
    rng = random.Random(3)
    compte = [0, 0, 0]
    for _ in range(30000):
        compte[mt.tirer_sans_remise(rng, [0, 1, 2], [1.0, 2.0, 0.0], 1)[0]] += 1
    assert compte[2] == 0 and abs(compte[1] / 30000 - 2 / 3) < 0.01, compte
    return f"tirage pondéré : {compte}"


def test_bras():
    """Invariants : paires valides, distinctes, au plus BUDGET ; temps par monde."""
    t0, nb, gammas = time.time(), 0, 0
    for c in cd.CONDITIONS:
        for i in range(3):
            w = mo.generer(cd.CONDITIONS[c], cd.graine_monde(cd.GRAINE_BASE_VALIDATION, c, 9000 + i))
            df = ms.frequences_etiquettes(w)
            sorties, g = mt.executer(w, df)
            gammas += g is not None
            valides = set(w["valides"])
            for b, s in sorties.items():
                assert len(s) == len(set(s)) <= mt.BUDGET, (c, b)
                assert set(s) <= valides, (c, b)
            nb += 1
    return f"invariants des bras sur {nb} mondes ; forme du rapport tournée sur {gammas} ; {(time.time() - t0) / nb:.3f} s par monde"


if __name__ == "__main__":
    for t in (test_glouton, test_gamma, test_tirage, test_bras):
        print(t.__name__, ":", t())
