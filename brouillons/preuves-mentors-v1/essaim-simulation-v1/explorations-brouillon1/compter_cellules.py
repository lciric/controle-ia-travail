"""Compte les cellules de la lecture gelée sur la grille brouillon, avec des comptes factices (aucun tirage)."""
import json
from collections import Counter
from controle_ia.simulation_essaim import calibrage as C, lecture as LEC, statistiques as S
g = json.load(open("brouillons/preuves-mentors-v1/essaim-simulation-v1/grille-essaim-v1-brouillon1.json"))
R, R0 = g["tailles"]["R"], g["tailles"]["R0"]
calib = {}
for cfg, c in g["configs"].items():
    s = {a: list(v) for a, v in C.seuils_exacts(c["K"], c["T"], g["q"], g["alpha"]).items() if a in c["panneau"]}
    for a, genre in c["panneau"].items():
        if genre == "ville": s[a] = list(C.seuil_ville(g["alpha"]))
        if genre == "mc": s[a] = [6.0, 0.0]
    calib[cfg] = {"K": c["K"], "T": c["T"], "seuils": s, "R0": R0, "alarmes_p0": {a: 5000 for a in c["panneau"]}}
Ccel = []
for cfg, specs in g["C"].items():
    K, T = g["configs"][cfg]["K"], g["configs"][cfg]["T"]
    pan = list(g["configs"][cfg]["panneau"])
    for s in specs:
        inv = [a for a in pan if S.invariante(S.nom_statistique(a), s["groupe"])]
        Ccel.append({"cfg": cfg, "K": K, "T": T, **s, "R": R, "alarmes": {a: 1000 for a in pan},
                     "valeurs_differentes": {}, "discordances": {a: 0 for a in inv}, "invariantes": inv})
Mcel = []
for cfg, specs in g["M"].items():
    K, T = g["configs"][cfg]["K"], g["configs"][cfg]["T"]
    for s in specs:
        d = {"cfg": cfg, "K": K, "T": T, **s, "R": R, "alarmes": {a: 1000 for a in g["configs"][cfg]["panneau"]}}
        if s["genre"] == "synchro":
            d.update({"L4_ecart_max": {"somme": 0.0}, "L4_discordances": {}, "L4_tolerance": 1.0})
        Mcel.append(d)
H = []
for cfg in g["HE3"]["configs"]:
    K, T = g["configs"][cfg]["K"], g["configs"][cfg]["T"]
    for x in g["HE3"]["lois"]:
        cf = g["HE3"]["conforme"]
        H.append({"cfg": cfg, "K": K, "T": T, "loi_nom": x["nom"], "loi": {**x["loi"], "N": K, "T": T}, "R": R,
                  "alarmes": {a: 1000 for a in g["HE3"]["alarmes"]},
                  "conforme": {"K": cf["K"], "n_test": cf["n_test"], "L": cf["L"], "alarmes_par_tirage": {s: [20] * cf["L"] for s in cf["statistiques"]}}})
H6 = []
for cfg in g["HE6"]["configs"]:
    K, T = g["configs"][cfg]["K"], g["configs"][cfg]["T"]
    for x in g["HE6"]["lois"]:
        for s in g["HE6"]["arrangements"]:
            inv = [a for a in g["HE6"]["alarmes"] if S.invariante(S.nom_statistique(a), s["groupe"])]
            H6.append({"cfg": cfg, "K": K, "T": T, **s, "loi_nom": x["nom"], "R": R, "R0": R0,
                       "alarmes": {a: 1000 for a in g["HE6"]["alarmes"]}, "alarmes_p0": {a: 1000 for a in g["HE6"]["alarmes"]},
                       "valeurs_differentes": {}, "discordances": {a: 0 for a in inv}, "invariantes": inv})
lec = LEC.Lecteur({"calibrage": calib, "C": {"cellules": Ccel}, "M": {"cellules": Mcel}, "HE3": {"cellules": H}, "HE6": {"cellules": H6}}, g)
out = lec.lire()
tot = Counter()
for k, x in out["predictions"].items():
    genre = x["cellules"][0]["genre"]
    tot[genre] += x["n_cellules"]
    print(k, x["n_cellules"], genre)
print(dict(tot), "total", sum(tot.values()))
print("z formes closes (p_th dans [0,01 ; 0,99]) :", out["audit_symetrie"]["formes_closes"]["n"], "; égalités :", out["audit_symetrie"]["egalites"]["n"])
print("région conforme exacte (L = 50, n_test = 400, K = 1000, γ = 1e-5) :", C.region_conforme(50, 400, 1000, 0.05, 1e-5))
