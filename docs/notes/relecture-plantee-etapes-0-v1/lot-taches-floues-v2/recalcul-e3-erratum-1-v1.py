"""Recalcul des deux majorants visés par le point E3 de l'erratum 1 de la conception v2 (étape 0,
tâches floues) : borne de service de D3 dans F7 au-delà de 66 désaccords sur 400, et probabilité
que l'un des 20 lots dépasse 66 désaccords. Arithmétique décimale à 50 chiffres, bibliothèque
standard seule. Le taux de désaccord de l'honnête au banc est repris du programme de calcul v2
(exécuté jusqu'au bloc G exclu, sortie jetée), puis tout le reste est refait ici, sans son code.
Usage : python3 recalcul-e3-erratum-1-v1.py CHEMIN/calculs-etape-0-taches-floues-v2.py
"""
import contextlib
import io
import math
import sys
from decimal import Decimal, getcontext

getcontext().prec = 50
src = open(sys.argv[1], encoding="utf-8").read()
fin = src.index("# ---------------------------------------------------------------- bloc G")
g = {"__name__": "calculs_v2_partiel"}
tampon = io.TextIOWrapper(io.BytesIO(), encoding="utf-8")
with contextlib.redirect_stdout(tampon):
    exec(compile(src[:fin], "calculs-etape-0-taches-floues-v2.py", "exec"), g)
rej = Decimal(repr(1 - g["R"]["acc_nette"]))
N, K, LOTS = 400, 66, 20


def fdr(n, k, p):
    return sum(Decimal(math.comb(n, i)) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))


lo, hi = Decimal(K) / N, Decimal(1)
for _ in range(120):  # borne haute unilatérale de Clopper-Pearson à 95 %
    m = (lo + hi) / 2
    if fdr(N, K, m) > Decimal("0.05"):
        lo = m
    else:
        hi = m
queue = LOTS * (1 - fdr(N, K, rej))
queue_0594 = LOTS * (1 - fdr(N, K, Decimal("0.0594")))
print(f"taux de désaccord de l'honnête au banc (programme v2, non arrondi) : {rej}")
print(f"borne haute de Clopper-Pearson à 95 %, {K} sur {N} : {hi:.10f} ; arrondie par excès à 4 décimales : "
      f"{math.ceil(hi * 10000) / 10000:.4f}")
print(f"probabilité qu'au moins un des {LOTS} lots dépasse {K} désaccords (union) : {queue:.6e} ; "
      f"arrondie par excès à 2 chiffres : {math.ceil(queue * Decimal('1e14')) / 10:.1f}e-13")
print(f"même calcul au taux arrondi 0,0594 (lecture du vérificateur) : {queue_0594:.6e}")
