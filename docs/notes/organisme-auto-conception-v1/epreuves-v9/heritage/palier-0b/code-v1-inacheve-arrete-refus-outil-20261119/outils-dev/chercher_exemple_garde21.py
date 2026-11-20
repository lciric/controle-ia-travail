import itertools
import sys

sys.path.insert(0, sys.argv[1])
sys.path.insert(0, sys.argv[2])
from controle_ia.heritage_etage_processeur_v1 import rangs_signes as RS
from test_heritage_etage_processeur_v1_outils import _p_par_enumeration

for d in ([0, 1, -2, 3, 4, 5, 6, 7], [0, 0, 1, 2, -3, 4, 5, 6, 7], [0, 1, 2, 3, 4, -5, 6, 7, 8], [0, 0, 0, -1, 2, 3, 4, 5, 6, 7]):
    a = RS.valeur_p_bilaterale(d)
    b = _p_par_enumeration([x for x in d if x != 0])[0]
    print(d, a, b, a != b)
