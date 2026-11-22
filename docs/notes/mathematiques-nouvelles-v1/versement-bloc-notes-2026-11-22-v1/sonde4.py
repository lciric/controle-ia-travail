import numpy as np, copy
from controle_ia.oracles_plantes_v1.parametres import charger
from controle_ia.oracles_plantes_v1.famille_f3 import MondeF3
from controle_ia.oracles_plantes_v1.famille_f2 import MondeF2
from controle_ia.oracles_plantes_v1.famille_f1 import MondeF1
p,_ = charger()
cfg = copy.deepcopy(p["familles"]["F3"]); cfg["AV_choix"] = [1.5]
m = MondeF3.tirer(np.random.default_rng(1), cfg, p["capacites"])
print("AV", repr(m.AV), "v(3)", m.ev.expr(m.analyser("v(3) = 0")[2], {}))
m2 = MondeF2({"M": 2, "D": 20, "a": [1.5, 2], "b": [10, 11], "cfg": p["familles"]["F2"]}, 10, p["capacites"])
print("F2 alpha", m2.alpha)
