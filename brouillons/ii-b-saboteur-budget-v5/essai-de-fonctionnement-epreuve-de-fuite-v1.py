"""Essai de fonctionnement du passage de l'épreuve de fuite : petites tailles, graines fixes ; n'imprime que des comptes de colonnes."""
import sys
import numpy as np
chemin = sys.argv[1]
argv = sys.argv
sys.argv = [chemin] + argv[2:]
M = {"__name__": "essai"}
exec(compile(open(chemin).read(), chemin, "exec"), M)
M["N_PAR_LOT"], M["N_REP_D"] = 60, 3
ss = np.random.SeedSequence(2468).spawn(12)
i = 0
for lec in M["LECTURES"]:
    cle = (*M["SITUE"], lec)
    r = M["lot"](((cle, 0), ss[i])); i += 1
    print("lot : cles", len(r))
    taux = {m: {x: 0.1 for x in "hadp"} for m in M["ORACLES"]}
    for nom, d in M["ETATS"][:3]:
        l, x = M["etalonnage"](((cle, nom, d, taux), ss[i]))
        print("etalonnage : colonnes", len(l.split("\t")), "; retour", len(x))
    i += 1
M2 = dict(M)
print("controle : colonnes", len(M["controle"](((*M["SITUE"], "continue, portee 0,3"), ss[10])).split("\t")), len(M["controle"](((*M["SITUE"], "aucune variation propre"), ss[11])).split("\t")))
