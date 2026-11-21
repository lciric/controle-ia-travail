#!/usr/bin/env python3
# controle_hc2.py -- recoupe independante (flottants, autre ecriture) des chiffres cles de calc_hc2.py.
# Les 35 recoupes du brouillon 1 sont gardees ; celles du brouillon 2 suivent.
import json, math, subprocess, sys, os
ici = os.path.dirname(os.path.abspath(__file__))
v = json.loads(subprocess.run([sys.executable, "-I", os.path.join(ici, "calc_hc2.py"), "--json"], check=True, capture_output=True, text=True).stdout)["valeurs"]
def num(s):
    return float(s.replace(" ", "").replace(",", "."))
ok = True
def verifie(nom, attendu, cle, tol=0.006):
    global ok
    lu = num(v[cle])
    bon = abs(lu - attendu) <= tol
    ok &= bon
    print(("ok  " if bon else "ECART"), nom, ": recalcul", round(attendu, 4), "; programme", v[cle])
def haut(x, nd=2):   # arrondi vers le haut, a nd decimales
    return math.ceil(x * 10 ** nd - 1e-7) / 10 ** nd
def bas(x, nd=2):    # arrondi vers le bas
    return math.floor(x * 10 ** nd + 1e-7) / 10 ** nd
def sup5(x):
    return 5 * math.ceil(x / 5 - 1e-9)

# ---------------- recoupes du brouillon 1, inchangees
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
res_m = (24000 * pe + (8 * 32768 + 64) * ps) / 1e6
for ph, cle in (("epr", "EPREUVE"), ("dec", "DECISIF"), ("rev", "REVISION")):
    verifie("plafond du second lecteur, " + ph, 5 * math.ceil((3 * k * c_m(lots_a[ph], lots_c[ph]) + res_m) / 5), "PL2_" + cle, 0)
C1 = 146.4
l1_haut = {}
for ph, cle in (("epr", "EPREUVE"), ("dec", "DECISIF"), ("rev", "REVISION")):
    vals = []
    for rho in (1, 4):
        x = C1 / (13888 + 1248 * rho)
        vals.append(x * (lots_a[ph] + rho * lots_c[ph]))
    l1_haut[ph] = max(vals)
    verifie("premier lecteur, bas, " + ph, min(vals), "L1_LO_" + cle)
    verifie("premier lecteur, haut, " + ph, max(vals), "L1_HI_" + cle)
    verifie("plafond du premier lecteur, " + ph, 5 * math.ceil((2 * max(vals) + 1.0) / 5), "PL1_" + cle, 0)
ca_n = (ga * 3 + 2000 * 15) / 1e6
cc_n = (gc * 3 + 4000 * 15) / 1e6
verifie("juge, 80 appels avec redemandes", k * (72 * ca_n + 8 * cc_n), "J_EK_80")
verifie("juge, 72 appels avec redemandes", k * 72 * ca_n, "J_EK_72")
res_n = (24000 * 3 + 65536 * 15) / 1e6
verifie("plafond du juge, 80", 5 * math.ceil((3 * k * 80 * cc_n + res_n) / 5), "PLJ_80", 0)
verifie("plafond du juge, 72", 5 * math.ceil((3 * k * 72 * cc_n + res_n) / 5), "PLJ_72", 0)
verifie("envoi coupe, Mistral, 2 690 s", 2690 * 200 * ps / 1e6, "CM_2690")
verifie("envoi coupe, Google, 2 690 s", 2690 * 200 * 15 / 1e6, "CN_2690")
verifie("envoi coupe, Google, 890 s", 890 * 200 * 15 / 1e6, "CN_890")
verifie("somme des plafonds", sum(num(v[c]) for c in ("PL1_EPREUVE", "PL1_DECISIF", "PL1_REVISION", "PL2_EPREUVE", "PL2_DECISIF", "PL2_REVISION", "PLJ_80", "PLJ_72")), "TOT_PL", 0)
verifie("attendu d'ensemble", C1 + tot + k * (72 * ca_n + 8 * cc_n) + k * 72 * ca_n, "ATT_AVEC", 0.51)
verifie("jetons d'entree, deux lecteurs, avec revision (millions)", 2 * (13888 * ea + 1248 * ec) / 1e6, "TOK_2L_AVEC", 0.051)
verifie("jetons d'entree, un moniteur (millions)", 6400 * 2866 / 1e6, "TOK_MON", 0.051)
verifie("total d'entree avec revision (millions)", (2 * (13888 * ea + 1248 * ec) + 144 * ga + 8 * gc + 2 * 6400 * 2866) / 1e6, "TOT_TOK_AVEC", 0.51)
verifie("credit Mistral, lots d'epreuve", math.ceil((55 + 2690 * 200 * ps / 1e6) * 1.15 * 2) / 2, "CREDIT_M_EPR")
maj = 3 * (13888 * (5000 * pe + 32768 * ps) + 1248 * (24000 * pe + 32768 * ps)) / 1e6
verifie("majorant vrai du second lecteur a 32 768", maj, "L2_MAJ_32768", 0.51)

# ---------------- recoupes du brouillon 2
print("-- brouillon 2")
# marge par instrument : 1,5 a l'appariement, 2 a la couverture (lots decisifs) ; la revision n'a que de l'appariement
ca_m = (ea * pe + 2000 * ps) / 1e6
cc_m = (ec * pe + 4000 * ps) / 1e6
verifie("plafond recalcule, lots decisifs, marge par instrument", sup5(1.5 * k * 9536 * ca_m + 2 * k * 928 * cc_m + res_m), "PL2R_DECISIF", 0)
verifie("plafond recalcule, revision", sup5(1.5 * k * 2176 * ca_m + res_m), "PL2R_REVISION", 0)
# sortie maximale que chaque maximum tolere : inversion directe de la reserve, puis multiple de 1 024 inferieur
def smax_mistral(plafond, base):
    s = ((plafond - base) * 1e6 - 24000 * pe - 64 * ps) / (8 * ps)
    return 1024 * math.floor(s / 1024)
def smax_juge(plafond, base):
    s = ((plafond - base) * 1e6 - 24000 * 3) / 15
    return 1024 * math.floor(s / 1024)
e2k = {ph: k * c_m(lots_a[ph], lots_c[ph]) for ph in ("epr", "dec", "rev")}
verifie("sortie maximale toleree, ligne 4", smax_mistral(55, 3 * e2k["epr"]), "SMAX_L4", 0)
verifie("sortie maximale toleree, ligne 5", smax_mistral(220, 3 * e2k["dec"]), "SMAX_L5", 0)
verifie("sortie maximale toleree, ligne 6", smax_mistral(45, 3 * e2k["rev"]), "SMAX_L6", 0)
verifie("sortie maximale toleree, ligne 7", smax_juge(20, 3 * k * 80 * cc_n), "SMAX_L7", 0)
verifie("sortie maximale toleree, ligne 8", smax_juge(20, 3 * k * 72 * cc_n), "SMAX_L8", 0)
verifie("maximum observe tolere, Mistral", num(v["SMAX_L4"]) / 4, "OBS_M", 0)
verifie("maximum observe tolere, juge", num(v["SMAX_L7"]) / 4, "OBS_J", 0)
verifie("regle 7 au plus, Mistral (essai a 32 768)", 4 * 32768, "R7_MAX_M", 0)
verifie("regle 7 au plus, juge (essai a 65 536)", 4 * 65536, "R7_MAX_J", 0)
def r_mistral(s):
    return (24000 * pe + (8 * s + 64) * ps) / 1e6
def r_juge(s):
    return (24000 * 3 + s * 15) / 1e6
verifie("ligne 4 a la regle 7 la plus haute", sup5(3 * e2k["epr"] + r_mistral(131072)), "PL4_R7", 0)
verifie("ligne 7 a la regle 7 la plus haute", sup5(3 * k * 80 * cc_n + r_juge(262144)), "PL7_R7", 0)
verifie("ligne 8 a la regle 7 la plus haute", sup5(3 * k * 72 * cc_n + r_juge(262144)), "PL8_R7", 0)
verifie("reserve de Mistral a la sortie maximale toleree", haut(r_mistral(71680), 3), "RES_M_SEUIL", 0.0005)
for s in (65536, 81920, 262144):
    verifie(f"reserve du juge a {s}", haut(r_juge(s), 3), f"J_RES3_{s}", 0.0005)
    verifie(f"majorant vrai du juge, 80 appels, a {s}", 3 * 80 * r_juge(s), f"J_MAJ80_{s}", 0.51)
    verifie(f"majorant vrai du juge, 152 appels, a {s}", 3 * 152 * r_juge(s), f"J_MAJ152_{s}", 0.51)
verifie("reserve du premier lecteur que la ligne 1 tolere", bas(55 - 2 * l1_haut["epr"]), "RES1_MAX")
verifie("tolerance de sortie du juge, au jeton", math.floor(((20 - res_n) / 80 - gc * 3 / 1e6) * 1e6 / 15), "J_TOL", 0)
verifie("juge, 80 appels, si 24 des 72 etaient de couverture", k * (48 * ca_n + 32 * cc_n), "J_EK_80_ALT")
# huit appels en vol
verifie("ligne 4, cumul tolere a huit appels en vol, 32 768", bas(55 - 8 * r_mistral(32768)), "CUM8_32768")
verifie("ligne 4, multiple de l'attendu a huit appels en vol, 32 768", bas((55 - 8 * r_mistral(32768)) / e2k["epr"]), "MULT8_32768")
verifie("ligne 4, cumul tolere a huit appels en vol, 71 680", bas(55 - 8 * r_mistral(71680)), "CUM8_SEUIL")
verifie("ligne 4, multiple de l'attendu a huit appels en vol, 71 680", bas((55 - 8 * r_mistral(71680)) / e2k["epr"]), "MULT8_SEUIL")
ent_epr = (2176 * ea + 320 * ec) * pe / 1e6
sor_epr = (2176 * 2000 + 320 * 4000) * ps / 1e6
verifie("ligne 4, sorties tolerees a huit appels en vol", bas(((55 - 8 * res_m) / k - ent_epr) / sor_epr, 1), "TOL8_32768", 0.0005)
verifie("ligne 4, sorties tolerees a un appel a la fois", bas(((55 - res_m) / k - ent_epr) / sor_epr, 1), "L2_TOL", 0.0005)
coupe_m = 2690 * 200 * ps / 1e6
for ph, cle, pl in (("epr", "EPREUVE", 55), ("dec", "DECISIF", 220), ("rev", "REVISION", 45)):
    verifie("pire cas tenu par les gardes a huit appels en vol, " + ph, pl + 8 * coupe_m, "PIRE2V_" + cle)
    verifie("credit Mistral a huit appels en vol, " + ph, math.ceil((pl + 8 * coupe_m) * 1.15 * 2 - 1e-9) / 2, "CREDIT_M8_" + cle)
verifie("ligne 4 si la regle comptait huit reserves", sup5(3 * e2k["epr"] + 8 * res_m), "PL4_8RES", 0)
# avenant 2, refait sur ses entrees : plafonds 16,50 et 3,00 ; envois coupes 8,07 et 2,67 ; sortie pleine de 65 536 jetons
pleine = 65536 * 15 / 1e6
exc_file = haut(8.07 - pleine)
exc_verif = haut(2.67 - pleine)
neuf = haut(16.50 + 9 * (8.07 - pleine))
verifie("avenant 2, essais chez Google, regime prudent", 2 * (3.00 + exc_verif) + 16.50 + exc_file, "AV2_PRUDENT", 0.0005)
verifie("avenant 2, essais chez Google, pire cas sans borne dure", 2 * (3.00 + exc_verif) + neuf, "AV2_PIRE", 0.0005)
verifie("avenant 2, file aux neuf exces", neuf, "AV2_NEUF", 0.0005)
verifie("depassement du pire cas accepte", 2 * (3.00 + exc_verif) + neuf - 84.06, "AV2_DEPASSE", 0.0005)
expo = 2 * (20 + 8.07)
verifie("deux lignes du juge a la course, regime prudent", expo, "EXPO_J", 0.0005)
verifie("avec les essais au regime prudent", expo + 32.97, "EXPO_PRUDENT", 0.0005)
verifie("avec le pire cas des essais", expo + 89.67, "EXPO_PIRE", 0.0005)
verifie("ligne du juge comptee comme l'avenant 2", haut(20 + 8.07 - res_n), "PIREJ_EXCES", 0.0005)
# euros : plancher au centime de [solde x 1,0990 x 0,95]
t95 = 1.0990 * 0.95
verifie("taux diminue de 5 %", t95, "T95", 0.0000005)
eur_j = haut(28.07 / t95)
verifie("solde a voir pour une ligne du juge", eur_j, "EUR_J", 0.0005)
verifie("un centime de moins compte pour", bas((eur_j - 0.01) * t95), "CC_J_MOINS", 0.0005)
verifie("manque au projet a 11,93 euros", eur_j - 11.93, "MANQUE_A", 0.0005)
verifie("manque au projet a 15,59 euros", eur_j - 15.59, "MANQUE_B", 0.0005)
verifie("manque des deux projets", 2 * eur_j - 11.93 - 15.59, "MANQUE_TOT", 0.0005)
verifie("credit compte de 31,58 euros", bas(31.58 * t95), "CC_AV2", 0.0005)
verifie("ce que les essais peuvent compter avant que la ligne 7 manque son seuil", bas(31.58 * t95) - 28.07, "MARGE_ESSAIS", 0.0005)
verifie("solde a voir pour les deux lignes du juge, au pire", haut(expo / t95), "EUR_2L", 0.0005)
# « 160 artefacts » : 32 lectures de couverture de plus par lecteur
verifie("second lecteur, lots d'epreuve a 160", e2k["epr"] + k * 32 * cc_m, "L2_EPR_160")
x4 = C1 / (13888 + 1248 * 4)
verifie("premier lecteur, lots d'epreuve a 160, au plus", l1_haut["epr"] + 32 * 4 * x4, "L1_EPR_160")
verifie("plafond de regle a 160, lignes 1 et 4", max(sup5(3 * (e2k["epr"] + k * 32 * cc_m) + res_m), sup5(2 * (l1_haut["epr"] + 32 * 4 * x4) + 1.0)), "PL_160", 0)
# moniteurs
for rap in (3, 4, 5):
    verifie(f"sortie qui pese autant que l'entree, rapport de prix {rap}", math.floor(2866 / rap + 0.5), f"MON_SEUIL_S{rap}", 0)
verifie("102 appels par action, milliards de jetons d'entree", 6400 * 102 * 2866 / 1e9, "MON_102_TOK")
verifie("reserve de sortie d'un moniteur de Google, par USD de prix de sortie", haut(65536 / 1e6, 3), "MON_RES_G", 0.0005)
verifie("regle 7 si la pensee passait 49 536", 1024 * math.ceil(4 * 49537 / 1024), "R7_SI_PENSEE", 0)
print("RECOUPE", "ENTIERE" if ok else "EN DEFAUT")
sys.exit(0 if ok else 1)
