"""Loi de la valeur retenue par `couplage_v5.choisir` quand le coût déclaré et les huit suites sont neuf tirages i.i.d. (le cas
« exact » de 3.3, deuxième action) : rang parmi les neuf (exact, par `loi_de_la_suite_retenue` sur valeurs distinctes), et
variance de la valeur retenue rapportée à celle d'un tirage, pour une loi normale et une loi log-normale (Monte-Carlo).
Entropie neuve imprimée. Appel : PYTHONPATH=ARBRE/src python3 ce_script.py"""
from fractions import Fraction
import numpy as np
from controle_ia.iib import couplage_v5 as cp
ss = np.random.SeedSequence(); print(f"# entropie {ss.entropy}")
# rang exact parmi les neuf valeurs réunies, coût uniforme sur ses 9 places
rang = {r: Fraction(0) for r in range(9)}
suites = [float(v) for v in range(1, 17, 2)]          # 1, 3, ..., 15
for j in range(9):
    cout = 2.0 * j                                     # 0, 2, ..., 16 : place j
    for i, p in cp.loi_de_la_suite_retenue(suites, cout).items():
        r = i + (1 if j <= i else 0)                   # rang (0 à 8) de la suite i parmi les neuf
        rang[r] += p / 9
print("rang parmi les neuf (0 à 8) :", {r: str(p) for r, p in rang.items()})
rng = np.random.default_rng(ss)
for nom, tir in (("normale", lambda n: rng.normal(0, 1, n)), ("log-normale (asymetrique)", lambda n: rng.lognormal(0, 0.6, n))):
    ret, ref = [], []
    for _ in range(40000):
        x = tir(9); c = cp.choisir(list(x[1:]), float(x[0]), rng)
        ret.append(x[1 + c["indice"]]); ref.append(x[1])
    ret, ref = np.array(ret), np.array(ref)
    print(f"{nom} : variance retenue / variance d'un tirage = {ret.var() / ref.var():.3f} ; moyenne retenue {ret.mean():.3f} contre {ref.mean():.3f} ; mediane {np.median(ret):.3f} contre {np.median(ref):.3f}")
