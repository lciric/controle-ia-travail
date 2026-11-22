import copy, json, tempfile, os
import numpy as np
from controle_ia.gardes import GardeArret
from controle_ia.oracles_plantes_v2.parametres import charger, CHEMIN
from controle_ia.oracles_plantes_v2.famille_f3 import MondeF3
from controle_ia.oracles_plantes_v2.famille_f2 import MondeF2
from controle_ia.oracles_plantes_v2.famille_f1 import MondeF1
p,_ = charger()
def t(nom, f):
    try: f(); print(nom, "ACCEPTÉ")
    except GardeArret as e: print(nom, "refusé")
cfg = copy.deepcopy(p["familles"]["F3"]); cfg["AV_choix"] = [1.5]
t("F3 AV 1.5", lambda: MondeF3.tirer(np.random.default_rng(1), cfg, p["capacites"]))
cfg = copy.deepcopy(p["familles"]["F3"]); cfg["AV_choix"] = ["0.5"]
t("F3 AV '0.5' texte", lambda: MondeF3.tirer(np.random.default_rng(1), cfg, p["capacites"]))
t("F2 a 1.5", lambda: MondeF2({"M": 2, "D": 20, "a": [1.5, 2], "b": [10, 11], "cfg": p["familles"]["F2"]}, 10, p["capacites"]))
t("F2 a True", lambda: MondeF2({"M": 2, "D": 20, "a": [True, 2], "b": [10, 11], "cfg": p["familles"]["F2"]}, 10, p["capacites"]))
t("F2 N 10.0", lambda: MondeF2({"M": 2, "D": 20, "a": [1, 2], "b": [10, 11], "cfg": p["familles"]["F2"]}, 10.0, p["capacites"]))
t("F1 D 20.0", lambda: MondeF1({"K": 4, "D": 20.0, "a": [5,5,5,5], "b": [4,6,5,5]}, 4, p["capacites"]))
caps = dict(p["capacites"]); caps["taille_entier_bits"] = 8192.5
t("capacité flottante", lambda: MondeF2({"M": 2, "D": 20, "a": [1, 2], "b": [10, 11], "cfg": p["familles"]["F2"]}, 10, caps))
d = tempfile.mkdtemp(); f = os.path.join(d, "p.json")
s = open(CHEMIN).read().replace('"pas_max_f1": 60', '"pas_max_f1": 60.0')
open(f, "w").write(s)
t("JSON 60.0", lambda: charger(f))
s = open(CHEMIN).read().replace('"pas_max_f1": 60', '"pas_max_f1": 6e1')
open(f, "w").write(s)
t("JSON 6e1", lambda: charger(f))
