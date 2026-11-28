import json, sys
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import numpy as np
from controle_ia.premier_test_ia import lecture as lp
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 200, 1000
import test_premier_test_ia_lecture as T
def conv(o):
    if isinstance(o, (np.integer,)): return int(o)
    if isinstance(o, (np.floating,)): return float(o)
    if isinstance(o, np.bool_): return bool(o)
    if isinstance(o, np.ndarray): return o.tolist()
    raise TypeError(type(o))
for seed, kw in [(0, {}), (2, {"temoin": True}), (6, {"fuite": True})]:
    s = lp.lire(T._source(seed, **kw), T._graines())
    j = json.loads(json.dumps(s, default=conv, ensure_ascii=False, sort_keys=True))
    print(seed, lp.issue(j) == j["issue"], j["issue"]["ligne"][:60])
    # clés lues par le brouillon
    p = j["principales"][0]
    print("   clés :", sorted(j.keys()))
    print("   intention :", sorted(j["intention"][p].keys()), "T2 :", sorted(j["intention"][p]["T2"].keys())[:12])
