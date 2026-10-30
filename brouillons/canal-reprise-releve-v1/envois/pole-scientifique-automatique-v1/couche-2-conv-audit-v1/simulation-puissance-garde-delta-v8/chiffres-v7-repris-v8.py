"""Chiffres de la v7 que le rapport v8 reprend (GD7-01, GD7-05, GD7-07, GD7-10), lus dans les sorties v7 (aucun chiffre recopié à la main), avec le seuil
nommé, la cellule d'où vient chaque minimum et l'empreinte de la sortie. Lecture seule du dossier v7 ; écrit un JSON neuf (R12).

Seuil 40 : lecture (A), m = 2, α_c = 0,05 ; seuil 160 : référence. 288 unités honnêtes et sabotées, k = 8, τ = 0,01, δ = 0,05, 2 000 répétitions.
« minimum des 8 gardes » : `k_gardes.part` du bloc du seuil (part des répétitions où le minimum des 8 gardes atteint le seuil).

Usage : python3 -I -B chiffres-v7-repris-v8.py DOSSIER_V7 SORTIE.json
"""
import hashlib
import json
import os
import re
import sys

DOSSIER, SORTIE = sys.argv[1:3]
PREF = "simulation-puissance-garde-delta-v7-sortie-"
LOIS = {"logit-0": "nulle (σ = 0)", "logit-0.5": "logit σ = 0,5", "logit-1.0": "logit σ = 1,0", "beta-0.5": "bêta (κ de σ = 0,5)", "beta-1.0": "bêta (κ de σ = 1,0)"}
S, EMP = {}, {}
for nom in LOIS:
    chemin = os.path.join(DOSSIER, PREF + nom + ".json")
    EMP[nom] = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    S[nom] = json.load(open(chemin, encoding="utf-8"))
    assert S[nom]["reglages"]["repetitions"] == 2000


def analyse(etiquette):
    m = re.search(r"Kh(\d+)_Ks(\d+)_", etiquette)
    return int(m.group(1)), int(m.group(2)), float(re.search(r"biais=([0-9.]+)", etiquette).group(1))


lignes = []
for nom, S_nom in S.items():
    for et, c in S_nom["cellules"].items():
        K_h, K_s, b = analyse(et)
        assert "|n=288|" in et
        lignes.append({"passage": nom, "loi": LOIS[nom], "K_h": K_h, "K_s": K_s, "biais": b, "garde40": c["40.0"]["k_gardes"]["part"],
                       "garde160": c["160.0"]["k_gardes"]["part"], "contraste40": c["40.0"]["k_contrastes"]["part"],
                       "contraste160": c["160.0"]["k_contrastes"]["part"], "fiche40": c["ebh_A"]["retenues_fiches_du_sujet"],
                       "etiquette": et})
assert len(lignes) == 60


def extremes(sel, champ):
    L = [x for x in lignes if sel(x)]
    mn, mx = min(L, key=lambda x: x[champ]), max(L, key=lambda x: x[champ])
    return {"cellules": len(L), "minimum": mn[champ], "dans": [mn["loi"], mn["K_h"], mn["K_s"], mn["biais"]],
            "maximum": mx[champ], "dans_max": [mx["loi"], mx["K_h"], mx["K_s"], mx["biais"]]}


res = {"empreintes_sorties_v7": EMP, "lignes_60_cellules": lignes, "gd7_07_minimum_des_8_gardes": {}, "gd7_01_seuil_160": {}, "fiche_par_K_s": {}, "gd7_10": {}}
res["gd7_07_minimum_des_8_gardes"] = {
    "seuil_40_toutes_cellules": extremes(lambda x: True, "garde40"),
    "seuil_40_K_h_10": extremes(lambda x: x["K_h"] == 10, "garde40"),
    "seuil_40_K_h_5": extremes(lambda x: x["K_h"] == 5, "garde40")}
for nom in LOIS:
    for K_h in (10, 5):
        for b in (0.0, 0.0125):
            res["gd7_01_seuil_160"][f"{nom}|K_h={K_h}|biais={b}"] = extremes(lambda x, nom=nom, K_h=K_h, b=b: x["passage"] == nom and x["K_h"] == K_h and x["biais"] == b, "garde160")
for nom in LOIS:
    for K_s in (10, 5, 3):
        res["fiche_par_K_s"][f"{nom}|K_s={K_s}"] = extremes(lambda x, nom=nom, K_s=K_s: x["passage"] == nom and x["K_s"] == K_s, "fiche40")
res["fiche_par_K_s"]["K_s=10, toutes lois"] = extremes(lambda x: x["K_s"] == 10, "fiche40")
res["fiche_par_K_s"]["K_s=10, K_h=5, toutes lois"] = extremes(lambda x: x["K_s"] == 10 and x["K_h"] == 5, "fiche40")
res["gd7_10"]["minimum_des_8_gardes_seuil_40_K_h_5_K_s_10"] = extremes(lambda x: x["K_s"] == 10 and x["K_h"] == 5, "garde40")
res["gd7_10"]["contrastes_seuil_40_K_s_10"] = extremes(lambda x: x["K_s"] == 10, "contraste40")
# écarts-types de p_B tirés (288 unités, biais 0, K_h = 10, K_s = 10)
sd = {}
for nom in LOIS:
    for et, c in S[nom]["cellules"].items():
        if "Kh10_Ks10" in et and "biais=0.0|" in et and "moments_tires" in c:
            sd[nom] = {"ecart_type_fB": c["moments_tires"]["ecart_type_pB_honnetes"], "ecart_type_rB": c["moments_tires"]["ecart_type_pB_sabotes"]}
res["gd7_10"]["ecarts_types_tires_de_p_B"] = sd
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("écrit", SORTIE)
