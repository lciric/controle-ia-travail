#!/usr/bin/env python3
# controle_hc1.py -- recoupe independante (flottants, autre ecriture) des chiffres cles de calc_hc1.py.
import json, math, subprocess, sys, os
ici = os.path.dirname(os.path.abspath(__file__))
v = json.loads(subprocess.run([sys.executable, "-I", os.path.join(ici, "calc_hc1.py"), "--json"], check=True, capture_output=True, text=True).stdout)["valeurs"]
def num(s):
    return float(s.replace(" ", "").replace(",", "."))
ok = True
def verifie(nom, attendu, cle, tol=0.006):
    global ok
    lu = num(v[cle])
    bon = abs(lu - attendu) <= tol
    ok &= bon
    print(("ok  " if bon else "ECART"), nom, ": recalcul", round(attendu, 4), "; programme", v[cle])

# volumes
lots_a = {"epr": 896 + 1280, "dec": 8960 + 576, "rev": 2176}
lots_c = {"epr": 64 + 128 + 128, "dec": 928, "rev": 0}
assert sum(lots_a.values()) == 13888 and sum(lots_c.values()) == 1248
ea, ec = 23625 / 18, 31591 / 6
ga, gc = 5159 / 6, 7933 / 2
pe, ps = 0.70 * 1.1, 2.10 * 1.1
k = 1 + 2 / 24
def c_m(a, c, sa=2000, sc=4000):
    return (a * (ea * pe + sa * ps) + c * (ec * pe + sc * ps)) / 1e6
for ph, cle in (("epr", "EPREUVE"), ("dec", "DECISIF"), ("rev", "REVISION")):
    verifie("Mistral, un envoi, " + ph, c_m(lots_a[ph], lots_c[ph]), "L2_E1_" + cle)
    verifie("Mistral, avec redemandes, " + ph, k * c_m(lots_a[ph], lots_c[ph]), "L2_EK_" + cle)
tot = k * c_m(13888, 1248)
verifie("Mistral, total avec redemandes", tot, "L2_EK_AVEC")
verifie("Mistral, sorties x 0,5", k * c_m(13888, 1248, 1000, 2000), "SENS_LO", 0.51)
verifie("Mistral, sorties x 4", k * c_m(13888, 1248, 8000, 16000), "SENS_HI", 0.51)
# plafonds de repli du second lecteur : 3 x attendu + reserve, arrondi aux 5 superieurs
res_m = (24000 * pe + (8 * 32768 + 64) * ps) / 1e6
for ph, cle in (("epr", "EPREUVE"), ("dec", "DECISIF"), ("rev", "REVISION")):
    verifie("plafond du second lecteur, " + ph, 5 * math.ceil((3 * k * c_m(lots_a[ph], lots_c[ph]) + res_m) / 5), "PL2_" + cle, 0)
# premier lecteur : fourchette
C1 = 146.4
for ph, cle in (("epr", "EPREUVE"), ("dec", "DECISIF"), ("rev", "REVISION")):
    vals = []
    for rho in (1, 4):
        x = C1 / (13888 + 1248 * rho)
        vals.append(x * (lots_a[ph] + rho * lots_c[ph]))
    verifie("premier lecteur, bas, " + ph, min(vals), "L1_LO_" + cle)
    verifie("premier lecteur, haut, " + ph, max(vals), "L1_HI_" + cle)
    verifie("plafond du premier lecteur, " + ph, 5 * math.ceil((2 * max(vals) + 1.0) / 5), "PL1_" + cle, 0)
# juge
ca_n = (ga * 3 + 2000 * 15) / 1e6
cc_n = (gc * 3 + 4000 * 15) / 1e6
verifie("juge, 80 appels avec redemandes", k * (72 * ca_n + 8 * cc_n), "J_EK_80")
verifie("juge, 72 appels avec redemandes", k * 72 * ca_n, "J_EK_72")
res_n = (24000 * 3 + 65536 * 15) / 1e6
verifie("plafond du juge, 80", 5 * math.ceil((3 * k * 80 * cc_n + res_n) / 5), "PLJ_80", 0)
verifie("plafond du juge, 72", 5 * math.ceil((3 * k * 72 * cc_n + res_n) / 5), "PLJ_72", 0)
# envoi coupe
verifie("envoi coupe, Mistral, 2 690 s", 2690 * 200 * ps / 1e6, "CM_2690")
verifie("envoi coupe, Google, 2 690 s", 2690 * 200 * 15 / 1e6, "CN_2690")
verifie("envoi coupe, Google, 890 s", 890 * 200 * 15 / 1e6, "CN_890")
# sommes
verifie("somme des plafonds", sum(num(v[c]) for c in ("PL1_EPREUVE", "PL1_DECISIF", "PL1_REVISION", "PL2_EPREUVE", "PL2_DECISIF", "PL2_REVISION", "PLJ_80", "PLJ_72")), "TOT_PL", 0)
verifie("attendu d'ensemble", C1 + tot + k * (72 * ca_n + 8 * cc_n) + k * 72 * ca_n, "ATT_AVEC", 0.51)
# jetons
verifie("jetons d'entree, deux lecteurs, avec revision (millions)", 2 * (13888 * ea + 1248 * ec) / 1e6, "TOK_2L_AVEC", 0.051)
verifie("jetons d'entree, un moniteur (millions)", 6400 * 2866 / 1e6, "TOK_MON", 0.051)
verifie("total d'entree avec revision (millions)", (2 * (13888 * ea + 1248 * ec) + 144 * ga + 8 * gc + 2 * 6400 * 2866) / 1e6, "TOT_TOK_AVEC", 0.51)
# credit
verifie("credit Mistral, lots d'epreuve", math.ceil((55 + 2690 * 200 * ps / 1e6) * 1.15 * 2) / 2, "CREDIT_M_EPR")
# majorant
maj = 3 * (13888 * (5000 * pe + 32768 * ps) + 1248 * (24000 * pe + 32768 * ps)) / 1e6
verifie("majorant vrai du second lecteur a 32 768", maj, "L2_MAJ_32768", 0.51)
print("RECOUPE", "ENTIERE" if ok else "EN DEFAUT")
sys.exit(0 if ok else 1)
