import sys, os
sys.path.insert(0, os.path.join(sys.argv[1], "essais")); sys.path.insert(0, sys.argv[1])
import aides_na_lot6_v5 as H
from pole import simulation_na_v5 as s5
m = H.MontageV5(scenario={"ad_a": H.selon({("proposeur", H.CE.MODELE_ESSAI): [s5.REFUS]})})
b = m.lancer()
f = [l for l in m.lignes_registre(1) if l["type_ligne"] == "fiche"]
print("fiches g1 par rang/classe/par_repli", sorted({(l["rang_repli"], l["classe"], l.get("par_repli")) for l in f}))
print("marques g2", b[1]["registre_servi"]["marques_par_repli"], "dont repli", b[0]["coffre"]["dont_servies_par_repli"])
print("passeports_par_repli", b[0]["comptes_portier_lot_5"].get("passeports_par_repli"))
print("cles ligne", sorted(f[0]))
