"""E4b : les témoins comptent dans m **et dans k*** (`appliquer_multiplicite`). Des témoins vrais forts (le cas voulu
quand le juge a des dents : témoins vrais = lois exactes des mondes de la grammaire, duel des proposeurs) sont retenus
par e-BH et abaissent le seuil des fiches réelles ; or les découvertes du pôle sont les seules fiches réelles. Taux de
fausses découvertes **parmi les fiches réelles**, toutes nulles ici (= probabilité qu'au moins une soit promue), avec t
témoins vrais forts dans la génération, contre la même génération sans eux dans k* (témoins comptés dans m, e = 0).

Fonction réelle, e-valeurs de synthèse (martingales de test sous le nul, comme e4).
Usage : python -I -B e4b_ebh_temoins_vrais_v1.py COPIE_DU_CODE SORTIE.json REPETITIONS
"""
import json
import math
import random
import sys

COPIE, SORTIE, R = sys.argv[1], sys.argv[2], int(sys.argv[3])
sys.path.insert(0, COPIE)
from pole.cycle import appliquer_multiplicite  # noqa: E402

alpha, sigma, n = 0.05, 0.35, 60
rng = random.Random(20261028)


def nulle():
    s, traj = 0.0, []
    for _ in range(n):
        s += sigma * rng.gauss(0, 1) - sigma * sigma / 2
        traj.append(s)
    return traj


resultats = {}
for m_total, t in ((24, 0), (24, 3), (24, 6), (40, 0), (40, 3), (40, 10)):
    avec = sans = 0
    for _ in range(R):
        issues = {f"T{i}": {"verdict_final": "survit", "motif": "", "temoin": True,
                            "pari": {"trajectoire_log_w": [5.0, 15.0, 30.0]}} for i in range(t)}
        for i in range(m_total - t):
            traj = nulle()
            issues[f"N{i}"] = {"verdict_final": "survit" if max(traj) >= math.log(1 / alpha) else "eliminee",
                               "motif": "", "pari": {"trajectoire_log_w": traj}}
        copie = json.loads(json.dumps(issues))
        appliquer_multiplicite(issues, alpha)
        avec += any(k.startswith("N") and v["verdict_final"] == "survit" for k, v in issues.items())
        for k, v in copie.items():
            if k.startswith("T"):
                v["pari"]["trajectoire_log_w"] = [-1e9]
        appliquer_multiplicite(copie, alpha)
        sans += any(k.startswith("N") and v["verdict_final"] == "survit" for k, v in copie.items())
    resultats[f"m={m_total},temoins_vrais_forts={t}"] = {
        "fausses_decouvertes_reelles_code_tel_quel": avec / R,
        "fausses_decouvertes_reelles_temoins_hors_de_k_etoile": sans / R}
sortie = {"alpha": alpha, "repetitions": R, "resultats": resultats}
with open(SORTIE, "w", encoding="utf-8") as f:
    json.dump(sortie, f, ensure_ascii=False, indent=1)
print(json.dumps(sortie, ensure_ascii=False, indent=1))
