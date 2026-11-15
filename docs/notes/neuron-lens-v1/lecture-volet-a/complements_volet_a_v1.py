"""Compléments descriptifs à la lecture du volet A de « Neuron Lens » — v1 (aucun critère ; réserves de symétrie).

Entrées : `diag/20261114-165239-neuron-lens-volet-a/brut-mesures-C{1,2,3}.json`. Usage (racine du dépôt) :
python docs/notes/neuron-lens-v1/lecture-volet-a/complements_volet_a_v1.py SORTIE.json
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

DIAG = Path("diag/20261114-165239-neuron-lens-volet-a")
COUCHES = ("8", "14", "20", "26")
P = (650, 58577, 1262, 10745)
N_GARDES = 103830  # `info_chargement.n_gardes` de volet-a-brut.json

out = {"sources": {}}
c = {}
for nom in ("C1", "C2", "C3"):
    p = DIAG / f"brut-mesures-{nom}.json"
    out["sources"][p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    c[nom] = json.loads(p.read_text(encoding="utf-8"))["resultat"]["decoupes"]

# A1 : étendue des rangs, part du vocabulaire gardé
r = [c["C2"][d][l]["a1"]["rang_s"] for d in range(5) for l in COUCHES]
r0 = [c["C2"][d][l]["a1"]["rang_sans_lentille"] for d in range(5) for l in COUCHES]
out["a1"] = {"rang_s_min": min(r), "rang_s_max": max(r), "rang_sans_lentille_min": min(r0), "rang_sans_lentille_max": max(r0),
             "n_cases_s_place_p": sum(x <= 10 for x in r), "n_cases": len(r),
             "n_cases_un_temoin_place_p": sum(c["C2"][d][l]["a1"]["un_temoin_place_p"] for d in range(5) for l in COUCHES),
             "attendu_au_hasard_par_case": 1 - (1 - 4 * 10 / N_GARDES) ** (102 * 2),
             "meilleur_rang_s_en_part_du_vocabulaire_garde": min(r) / N_GARDES}

# A3 : zéros exacts, présence des jetons lus, P parmi les jetons de la lecture S
a3 = {}
for nom in ("C1", "C2"):
    ms = [c[nom][d][l]["a3"] for d in range(5) for l in COUCHES]
    a3[nom] = {"n_cases": len(ms), "chute_s_exactement_nulle": sum(m["chute_s"] == 0.0 for m in ms),
               "chute_s_max_abs": max(abs(m["chute_s"]) for m in ms),
               "centile_95_exactement_nul": sum(float(np.quantile(m["chutes_aleatoires"], 0.95)) == 0.0 for m in ms),
               "tirages_exactement_nuls_part": float(np.mean([v == 0.0 for m in ms for v in m["chutes_aleatoires"]])),
               "jetons_s_presents_test_total": sum(m["jetons_s_presents_test"] for m in ms),
               "jetons_s_presents_test_max": max(m["jetons_s_presents_test"] for m in ms),
               "cases_ou_P_est_parmi_les_20_jetons_S": sum(bool(set(P) & set(m["jetons_s"])) for m in ms),
               "chute_sac_min": min(m["chute_sac"] for m in ms), "chute_sac_max": max(m["chute_sac"] for m in ms)}
out["a3"] = a3

# A2 : ρ de S contre ρ des témoins rapportés hors condition
a2 = {}
for l in COUCHES:
    ms = [c["C1"][d][l]["a2"] for d in range(5)]
    a2[l] = {"rho_s_min": min(m["rho_s"] for m in ms), "rho_s_max": max(m["rho_s"] for m in ms),
             "decoupes_ou_rho_permutee_depasse_rho_s": [d for d, m in enumerate(ms) if m["rho_permutee"] >= m["rho_s"]],
             "decoupes_ou_rho_c3_depasse_rho_s": [d for d, m in enumerate(ms) if m["rho_c3"] >= m["rho_s"]],
             "rho_permutee_max": max(m["rho_permutee"] for m in ms), "rho_c3_max": max(m["rho_c3"] for m in ms)}
out["a2"] = a2

# Lecture R (description) : P parmi les 20 premiers jetons, C2
out["lecture_r_c2"] = {l: {"difference_des_moyennes": [sorted(set(P) & set(c["C2"][d][l]["lecture_r_difference"])) for d in range(5)],
                            "poids_de_la_sonde": [sorted(set(P) & set(c["C2"][d][l]["lecture_r_poids"])) for d in range(5)]}
                        for l in COUCHES}

# A-ii : k neurones au hasard contre la sonde (référence rapportée, sans critère)
aii = {}
for nom in ("C1", "C2", "C3"):
    aii[nom] = {}
    for l in COUCHES:
        ms = [c[nom][d][l] for d in range(5)]
        s = float(np.mean([m["auc_sonde_id"] for m in ms]))
        aii[nom][l] = {"sonde_id": s,
                       "hasard64_id_moins_sonde": float(np.mean([m["aii"]["id"]["hasard64"] for m in ms])) - s,
                       "k64_id_moins_sonde": float(np.mean([m["aii"]["id"]["k64"] for m in ms])) - s,
                       "pca64_id_moins_sonde": float(np.mean([m["aii"]["id"]["pca64"] for m in ms])) - s,
                       "dense_id_moins_sonde": float(np.mean([m["aii"]["id"]["dense"] for m in ms])) - s,
                       "huit_premiers_neurones": [m["aii"]["huit_premiers_neurones"] for m in ms]}
out["aii"] = aii
Path(sys.argv[1]).write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k not in ("aii",)}, ensure_ascii=False, indent=1))
for nom in aii:
    for l in COUCHES:
        print(nom, l, {k: round(v, 4) for k, v in aii[nom][l].items() if k != "huit_premiers_neurones"})
