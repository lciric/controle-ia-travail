"""E4 : `appliquer_multiplicite` calcule k* sur toutes les fiches jugées, y compris celles que la règle par fiche a
éliminées (marge des filles 2·delta0 non atteinte, mode « horizon ») ; puis elle ne fait que rétrograder. L'ensemble
promu final est un **sous-ensemble filtré après coup** de l'ensemble e-BH : la borne du taux de fausses découvertes ne
s'y transporte pas (une éliminée par la marge abaisse le seuil des autres).

1. Cas construit (fonction réelle) : A vraie à très forte richesse mais éliminée par la marge ; B nulle à log W = 3,2.
2. Monte-Carlo (fonction réelle, e-valeurs de synthèse) : m = 40 ; m1 fiches non nulles à forte richesse, toutes
   éliminées par la marge ; m0 = 40 − m1 fiches nulles dont la richesse est une vraie martingale de test sous le nul
   (log W_t = Σ (σ·Z_s − σ²/2), n = 60 pas) ; on compte la probabilité qu'au moins une nulle soit promue (ici, toute
   promotion est fausse : taux de fausses découvertes) avec le code tel quel, puis avec e = 0 pour les fiches éliminées
   par la règle par fiche (correction proposée).

Usage : python -I -B e4_ebh_puis_filtre_v1.py COPIE_DU_CODE SORTIE.json REPETITIONS
"""
import json
import math
import random
import sys

COPIE, SORTIE, R = sys.argv[1], sys.argv[2], int(sys.argv[3])
sys.path.insert(0, COPIE)
from pole.cycle import appliquer_multiplicite  # noqa: E402

alpha = 0.05
# 1. cas construit
cas = {"A": {"verdict_final": "eliminee", "motif": "marge non atteinte",
             "pari": {"trajectoire_log_w": [1.0, 4.0, 9.0, 12.0], "marge_atteinte": False}},
       "B": {"verdict_final": "survit", "motif": "richesse au seuil 1/α", "pari": {"trajectoire_log_w": [0.5, 3.2]}}}
r1 = appliquer_multiplicite(cas, alpha)
sans_a = {"B": {"verdict_final": "survit", "motif": "", "pari": {"trajectoire_log_w": [0.5, 3.2]}}}
r1b = appliquer_multiplicite(dict(sans_a, A={"verdict_final": "eliminee", "motif": "", "pari": {"trajectoire_log_w": [-1e9]}}), alpha)
cas_construit = {"code_tel_quel": {"retenues": r1["retenues"], "B": cas["B"]["verdict_final"], "A": cas["A"]["verdict_final"]},
                 "A_compte_avec_e_nul": {"retenues": r1b["retenues"]}}

# 2. Monte-Carlo
rng = random.Random(20261027)
sigma, n = 0.35, 60


def trajectoire_nulle():
    s, traj = 0.0, []
    for _ in range(n):
        s += sigma * rng.gauss(0, 1) - sigma * sigma / 2
        traj.append(s)
    return traj


resultats = {}
for m1 in (0, 5, 10, 20, 30):
    tel_quel = corrige = 0
    for _ in range(R):
        issues = {}
        for i in range(m1):
            issues[f"V{i}"] = {"verdict_final": "eliminee", "motif": "marge non atteinte",
                               "pari": {"trajectoire_log_w": [0.0, 20.0, 30.0], "marge_atteinte": False}}
        for i in range(40 - m1):
            traj = trajectoire_nulle()
            issues[f"N{i}"] = {"verdict_final": "survit" if max(traj) >= math.log(1 / alpha) else "eliminee", "motif": "",
                               "pari": {"trajectoire_log_w": traj}}
        copie = json.loads(json.dumps(issues))
        appliquer_multiplicite(issues, alpha)
        tel_quel += any(k.startswith("N") and v["verdict_final"] == "survit" for k, v in issues.items())
        for k, v in copie.items():
            if v["verdict_final"] != "survit":
                v["pari"]["trajectoire_log_w"] = [-1e9]  # e = 0 pour les éliminées par la règle par fiche
        appliquer_multiplicite(copie, alpha)
        corrige += any(k.startswith("N") and v["verdict_final"] == "survit" for k, v in copie.items())
    resultats[f"m1={m1}"] = {"taux_fausses_decouvertes_code_tel_quel": tel_quel / R,
                             "taux_fausses_decouvertes_e_nul_pour_les_eliminees": corrige / R}
sortie = {"cas_construit": cas_construit, "monte_carlo": resultats, "repetitions": R, "sigma": sigma, "pas": n, "alpha": alpha}
with open(SORTIE, "w", encoding="utf-8") as f:
    json.dump(sortie, f, ensure_ascii=False, indent=1)
print(json.dumps(sortie, ensure_ascii=False, indent=1))
