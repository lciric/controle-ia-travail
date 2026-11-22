# Contrôle des phrases permises du brouillon 4 contre le critère d'identité v8 (à l'espacement près). Contre-lecteur, 2026-11-19.
import re, sys, hashlib
b4p, cip = sys.argv[1], sys.argv[2]
b4 = open(b4p, encoding="utf-8").read(); ci = open(cip, encoding="utf-8").read()
print("b4", hashlib.sha256(b4.encode()).hexdigest()); print("ci", hashlib.sha256(ci.encode()).hexdigest())
norm = lambda s: re.sub(r"\s+", " ", s).strip()
B4, CI = norm(b4), norm(ci)
debuts = {
 "P1 deux": "Les fichiers d'ajustement réajustés sont identiques",
 "P1 une": "Le fichier d'ajustement réajusté de la lentille [R | S]",
 "P2 deux": "Les deux lentilles mesurées le 18 novembre ont été détruites",
 "P2 R": "La lentille R mesurée le 18 novembre a été détruite",
 "autre": "Lentille [R | S] : verdict d'identité",
}
def phrase(T, d):
    i = T.find(d)
    if i < 0: return None, 0
    # jusqu'au guillemet fermant « » » qui termine la citation
    j = T.find(" »", i)
    return T[i:j], T.count(d)
for k, d in debuts.items():
    a, na = phrase(B4, d); c, nc = phrase(CI, d)
    print(f"{k}: occurrences b4={na} ci={nc} ; égales={a == c}")
    if a != c:
        print("  b4:", a); print("  ci:", c)
# S seule : construite depuis R seule selon la règle de CI
r, _ = phrase(CI, debuts["P2 R"])
m = re.search(r"L'écart maximal de chaque matrice.*?des deux courses\.", r)
s_construite = r[:m.start()] + "Aucune autre comparaison n'existe pour cette lentille." + r[m.end():]
s_construite = s_construite.replace("La lentille R mesurée", "La lentille S mesurée", 1)
s_b4, n = phrase(B4, "La lentille S mesurée le 18 novembre a été détruite")
print("S seule : occurrences b4 =", n, "; égale à la construction mécanique :", s_b4 == s_construite)
if s_b4 != s_construite: print(" b4:", s_b4, "\n cons:", s_construite)
