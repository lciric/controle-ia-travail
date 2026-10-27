"""E4c : pire cas de E4/E4b. Fiches nulles à e-valeur « tout ou rien » (e = c avec probabilité 1/c, sinon 0 : espérance 1,
une e-valeur valide), c = m / (α·(t+1)) ; t fiches fortes retenues par e-BH mais absentes des découvertes réelles
(témoins vrais, ou éliminées par la marge). Fonction réelle `appliquer_multiplicite`.

Usage : python -I -B e4c_ebh_pire_cas_v1.py COPIE_DU_CODE SORTIE.json REPETITIONS
"""
import json
import math
import random
import sys

COPIE, SORTIE, R = sys.argv[1], sys.argv[2], int(sys.argv[3])
sys.path.insert(0, COPIE)
from pole.cycle import appliquer_multiplicite  # noqa: E402

alpha = 0.05
rng = random.Random(7)
resultats = {}
for m, t in ((24, 0), (24, 3), (24, 6), (40, 3), (40, 10)):
    c = m / (alpha * (t + 1))
    compte = 0
    for _ in range(R):
        issues = {f"T{i}": {"verdict_final": "survit", "motif": "", "pari": {"trajectoire_log_w": [30.0]}} for i in range(t)}
        for i in range(m - t):
            e = c if rng.random() < 1 / c else 1e-12
            issues[f"N{i}"] = {"verdict_final": "survit" if e >= 1 / alpha else "eliminee", "motif": "",
                               "pari": {"trajectoire_log_w": [math.log(e)]}}
        appliquer_multiplicite(issues, alpha)
        compte += any(k.startswith("N") and v["verdict_final"] == "survit" for k, v in issues.items())
    resultats[f"m={m},t={t}"] = {"e_tout_ou_rien": round(c, 2), "fausses_decouvertes_reelles": compte / R,
                                 "approximation": round(1 - (1 - 1 / c) ** (m - t), 4)}
with open(SORTIE, "w", encoding="utf-8") as f:
    json.dump({"alpha": alpha, "repetitions": R, "resultats": resultats}, f, ensure_ascii=False, indent=1)
print(json.dumps(resultats, ensure_ascii=False, indent=1))
