"""Essai de fonctionnement du passage rejoué : petites tailles, graines fixes ; n'imprime que des comptes de colonnes."""
import sys
import numpy as np
chemin, v4, v2 = sys.argv[1], sys.argv[2], sys.argv[3]
argv = sys.argv
sys.argv = [chemin, v4, v2]
M = {"__name__": "essai"}
exec(compile(open(chemin).read(), chemin, "exec"), M)
M["N_PAR_LOT"], M["N_REP_D"] = 60, 3
ss = np.random.SeedSequence(12345).spawn(8)
cle = M["SITUE"]
r = M["lot"](((cle, 0), ss[0]))
print("lot : cles", len(r))
print("controle : colonnes", len(M["controle_donnees"]((cle, ss[1])).split("\t")))
for i, (fam, m) in enumerate((("N", 4), ("N", 8), ("P", 0))):
    for nom, d in M["DEFAUTS"][fam]:
        l, x = M["etalonnage"](((cle, m, 4.0, 0.7, nom, d, {"h": 0.02, "a": 0.2, "d": 0.2, "p": 0.2}), ss[2 + i]))
        print("etalonnage", m, ": colonnes", len(l.split("\t")), "; retour", len(x))
print("premier cout : colonnes", len(M["premier_cout"](((cle, 0.5, {m: (4.0, 0.7) for m in M["ORACLES"]}), ss[6])).split("\t")))
