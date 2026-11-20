"""Recalcul indépendant (contre-lecteur, modèle S) de rho, rho', rho'-rho et votes effectifs sur des erreurs plantées.
Exact en fractions, sans numpy ; comparé aux fonctions du banc v4 chargées par charger_banc de l'étalonnage (copie).
Usage : python3 -I -B recalcul_independant_v1.py"""
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

COPIE = Path("/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/"
             "contre-lecture-etalonnage-lecture-etage-2/copie/etalonner_ligne_3_v1.py")
spec = importlib.util.spec_from_file_location("et_copie", COPIE)
ET = importlib.util.module_from_spec(spec)
sys.modules["et_copie"] = ET
spec.loader.exec_module(ET)
import numpy as np

banc = ET.charger_banc()

# Configurations d'erreurs (opus1, argon1, opus2, argon2) -> comptes plantés, par classe (100 + 100).
bons = {(0, 0, 0, 0): 50, (1, 1, 1, 1): 8, (1, 0, 1, 0): 10, (0, 1, 0, 1): 12, (1, 1, 0, 0): 6, (0, 0, 1, 1): 4,
        (1, 0, 0, 0): 5, (0, 1, 0, 0): 5}
mauv = {(0, 0, 0, 0): 40, (1, 1, 1, 1): 15, (1, 0, 1, 0): 12, (0, 1, 0, 1): 9, (1, 1, 0, 0): 8, (0, 0, 1, 1): 6,
        (0, 0, 1, 0): 5, (0, 1, 1, 0): 5}
assert sum(bons.values()) == 100 and sum(mauv.values()) == 100


def lignes(d):
    out = []
    for k, c in sorted(d.items()):
        out += [k] * c
    return out


Lb, Lm = lignes(bons), lignes(mauv)
n = len(Lb) + len(Lm)


def cov(j, k):
    tot = Fraction(0)
    for L in (Lb, Lm):
        mj = Fraction(sum(x[j] for x in L), len(L))
        mk = Fraction(sum(x[k] for x in L), len(L))
        tot += sum((x[j] - mj) * (x[k] - mk) for x in L)
    return tot / (n - 2)


v = [cov(j, j) for j in range(4)]
rho_moy = 2 * cov(0, 1) / (v[0] + v[1])                      # (J-1)=1, somme des covariances j != k = 2 cov
rho_pair = float(cov(0, 1)) / math.sqrt(float(v[0] * v[1]))
rp_o = float(cov(0, 2)) / math.sqrt(float(v[0] * v[2]))
rp_a = float(cov(1, 3)) / math.sqrt(float(v[1] * v[3]))
ve = 2 / (1 + float(rho_moy))

# Banc
E = np.array(Lb + Lm, dtype=bool)
y = np.array([True] * 100 + [False] * 100)
S = banc.cov_intra_classes(E[None].astype(float), y)
rho_b, _ = banc.rho_moyenne(S[:, :2, :2])
rp_b = [float(banc.rho_paire(S, 0, 2)[0][0]), float(banc.rho_paire(S, 1, 3)[0][0])]
rpair_b = float(banc.rho_paire(S, 0, 1)[0][0])
ve_b = float(banc.votes_effectifs(rho_b, 2)[0])

res = {
    "rho_moyenne": [float(rho_moy), float(rho_b[0])], "rho_paire": [rho_pair, rpair_b],
    "rho_prime_opus": [rp_o, rp_b[0]], "rho_prime_argon": [rp_a, rp_b[1]],
    "rho_prime_moins_rho_pair_opus": [rp_o - rho_pair, rp_b[0] - rpair_b],
    "rho_prime_moins_rho_moyenne_opus": [rp_o - float(rho_moy), rp_b[0] - float(rho_b[0])],
    "votes_effectifs": [ve, ve_b],
}
ok = True
for k, (a, b) in res.items():
    d = abs(a - b)
    ok &= d < 1e-12
    print(k, a, b, "ecart", d)
print("rho moyenne et rho paire differents (variances inegales) :", abs(float(rho_moy) - rho_pair))
print("TOUT EGAL" if ok else "DIFFERENCE")
Path("/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/"
     "contre-lecture-etalonnage-lecture-etage-2/recalcul_independant_v1.json").write_text(
    json.dumps(res, indent=1, sort_keys=True), encoding="utf-8")
