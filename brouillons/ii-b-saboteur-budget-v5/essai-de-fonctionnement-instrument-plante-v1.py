"""Essai de fonctionnement du passage « instrument planté pour la branche à contexte réécrit » : petites tailles, graines
fixes ; n'imprime que des comptes de colonnes et le seuil de Student (une constante, non un résultat)."""
import sys
import numpy as np
chemin = sys.argv[1]
argv = sys.argv
sys.argv = [chemin] + argv[2:]
M = {"__name__": "essai"}
exec(compile(open(chemin).read(), chemin, "exec"), M)
M["N_PAR_LOT"], M["N_REP_D"] = 60, 3
ss = np.random.SeedSequence(13579).spawn(12)
i = 0
print("seuil de Student a 127 degres, bilateral 1/80 :", round(M["T_80E"], 3), "; loi normale :", round(M["Z_80E"], 3))
print("entete : colonnes", len(M["ENTETE_D"]))
for lec in M["LECTURES"]:
    cle = (*M["SITUE"], lec)
    r = M["lot_b"](((cle, 0), ss[i])); i += 1
    print("lot : cles", len(r))
    taux = {m: {x: 0.1 for x in "hadp"} for m in M["ORACLES"]}
    for nom, d in M["ETATS"]:
        l, x = M["etalonnage_b"](((cle, nom, d, taux), ss[i]))
        print("etalonnage : colonnes", len(l.split("\t")), "; retour", len(x), "; variantes", len(x[2]))
    i += 1
