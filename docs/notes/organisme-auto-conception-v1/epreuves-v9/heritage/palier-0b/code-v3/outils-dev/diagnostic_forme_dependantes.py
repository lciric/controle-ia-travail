"""Outil de développement (graines « essai », taille réduite, aucune sortie versée) : quels traits de forme séparent les lois
dépendantes des indépendantes ? Statistique t par trait, jetons des cases en cause, longueur, et exactitude sur la longueur seule."""
import collections
import hashlib
import sys

import numpy as np

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import audit as AU
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mondes as MO

g = GR.Graines()
n = int(sys.argv[2])
suites = [MO.generer_suite(g, dict(couche="essai", famille="diag-presentation", dose=d, source=k), d)
          for d in (0.25, 0.5) for k in range(n)]
lois = [l for s in suites for m in s.mondes_cibles() for l in m.lois.values() if l["type"] == "vraie"]
X = np.array([AU.traits_de_forme(l["texte"]) for l in lois])
y = np.array([l["dependante"] for l in lois])
a, b = X[y], X[~y]
sd = np.sqrt(a.var(axis=0, ddof=1) / len(a) + b.var(axis=0, ddof=1) / len(b))
t = np.where(sd > 0, (a.mean(axis=0) - b.mean(axis=0)) / np.where(sd > 0, sd, 1), 0)
ordre = np.argsort(-np.abs(t))[:6]
print("lois", len(a), len(b), "traits", ordre.tolist(), "t", np.round(t[ordre], 2).tolist())
case_de = collections.defaultdict(collections.Counter)
for l in lois:
    for j in AU.jetons(l["texte"]):
        case_de[int.from_bytes(hashlib.sha256(j.encode("utf-8")).digest()[:4], "big") % 64][j] += 1
for c in ordre[:4]:
    print("case", int(c), case_de[int(c)].most_common(6), "moyennes", round(a[:, c].mean(), 3), round(b[:, c].mean(), 3))
print("longueur", round(a[:, -1].mean(), 2), round(b[:, -1].mean(), 2))
print("exactitude, longueur seule", AU.exactitude_equilibree(X[:, -1:], y, np.random.default_rng(1)))


def valeurs(l):
    return [w for s in l["loi"]["lois"].values() for ligne in s["poids"] for w in ligne] + \
        [b for s in l["loi"]["lois"].values() for b in s["biais"]]


for nom, sel in (("dépendantes", [l for l in lois if l["dependante"]]), ("indépendantes", [l for l in lois if not l["dependante"]])):
    v = [valeurs(l) for l in sel]
    signes = np.mean([sum(x < 0 for x in vv) for vv in v])
    courts = np.mean([sum(len(repr(x).split(".")[-1]) < 6 for x in vv) for vv in v])
    grands = np.mean([sum(abs(x) >= 1 for x in vv) for vv in v])
    print(nom, "signes moins", round(signes, 3), "nombres de moins de six décimales", round(courts, 3), "|x| ≥ 1", round(grands, 3))
print("exactitude, toutes", AU.exactitude_equilibree(X, y, np.random.default_rng(1)))
