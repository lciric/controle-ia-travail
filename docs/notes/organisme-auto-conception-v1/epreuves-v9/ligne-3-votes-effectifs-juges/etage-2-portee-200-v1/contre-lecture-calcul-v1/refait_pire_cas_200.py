"""Refait indépendant du pire cas à 200 témoins (contre-lecteur, modèle S).
Usage : python3 -I -B CE_FICHIER > SORTIE.txt  (depuis la racine du dépôt)
Écrit à part du programme du développeur : aucun import de lui, plan en listes de coûts."""
import json
from decimal import Decimal
from fractions import Fraction as F

m = json.load(open("runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json"), parse_float=Decimal)
usd = m["cout_reel"]["par_role_usd"]
ap = m["cout_reel"]["appels_par_role"]
dev = m["ecart_au_devis_v1"]["par_role"]
unit = {j: F(usd[j]) / ap[j] for j in ("juge-opus", "juge-argon")}
pire = max(F(usd[j]) / F(dev[j]["devis_usd"]) for j in ("juge-opus", "juge-argon"))
PLAF, RES = F(8836, 100), F(60, 100)
N = 200


def plan():
    L = []  # (etiquette, cout unitaire de base)
    for t in range(2):
        L += [("P", t, "o"), ("P", t, "a")]
    for t in range(N):
        L += [("A", t, "o"), ("A", t, "a")]
    for t in range(N):
        L += [("B", t, "o"), ("B", t, "a"), ("B", t, "a")]
    return L


def joue(facteur, refus=0):
    cum, partis, ok = F(0), 0, set()
    cnt = {}
    r = refus
    cut = None
    for i, (b, t, j) in enumerate(plan()):
        c = unit["juge-opus" if j == "o" else "juge-argon"] * facteur
        essais = [None, c] if r > 0 else [c]
        if r > 0:
            r -= 1
        for e in essais:
            if cum + RES > PLAF:
                cut = (i, b, t, j, cum)
                break
            partis += 1
            cum += RES if e is None else e
            if e is not None:
                cnt[(b, t)] = cnt.get((b, t), 0) + 1
        if cut:
            break
    A = sum(1 for t in range(N) if cnt.get(("A", t), 0) == 2)
    Bc = [t for t in range(N) if cnt.get(("B", t), 0) == 3]
    lect = sum(1 for t in Bc if t < N // 2)
    return partis, cum, cut, A, len(Bc), lect


p, cum, cut, A, B, lect = joue(pire)
print("pire facteur", pire, float(pire))
print("total du plan au pire", float(sum(unit["juge-opus" if j == "o" else "juge-argon"] * pire for _, _, j in plan())))
print("envois partis", p, "sur", len(plan()))
print("cumul a l'arret", float(cum))
print("coupure (rang envoi, bloc, temoin 0-base, juge, cumul avant)", cut[:4], float(cut[4]), "-> temoin 1-base", cut[2] + 1)
print("A complets", A, "B complets", B, "dont lecture", lect)
print("reste sous plafond", float(PLAF - cum))
dernier_parti = plan()[cut[0] - 1]
print("dernier envoi parti", dernier_parti)
print("cumul avant le dernier parti", float(cum - unit["juge-opus"] * pire))
# seuils de refus
lec_ent = lec40 = bloc_a = None
r = 0
while True:
    p, cum, cut, A, B, lect = joue(pire, r)
    if A < N:
        break
    if lect == N // 2:
        lec_ent = r
    if lect >= 40:
        lec40 = r
    bloc_a = r
    r += 1
print("max refus lecture entiere", lec_ent, "max refus >=40 lecture", lec40, "max refus A complet", bloc_a)
for r in (0, 39, 40, 64, 65):
    print("refus", r, joue(pire, r)[3:])
