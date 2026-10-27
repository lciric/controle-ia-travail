"""E15 : l'expérimentateur peut-il connaître son verdict avant de répondre ? Avec les seuls fichiers de son dossier
(`engagement.json`, `mesures.json`), sans la graine du noyau, on recalcule la trajectoire de log W (numérateur et maximum
des membres de la bibliothèque déclarée dans l'engagement) et on la compare au jugement du noyau (E1b, génération 0).

Usage : python -I -B e15_richesse_calculable_par_l_agent_v1.py COPIE_DU_CODE DOSSIER_EXPERIENCE RESULTAT_E1B.json SORTIE.json
"""
import json
import os
import sys

COPIE, EXP, E1B, SORTIE = sys.argv[1:5]
sys.path.insert(0, COPIE)
from pole import selection_pari as sp  # noqa: E402

with open(os.path.join(EXP, "engagement.json"), encoding="utf-8") as f:
    e = json.load(f)
with open(os.path.join(EXP, "mesures.json"), encoding="utf-8") as f:
    issues = json.load(f)["issues"]
k, instances = e["nombre_issues"], e["instances"]
cache = sp.Cache(issues, instances)
num = sp.trajectoire_numerateur(e, issues, instances, cache)
den, _ = sp.trajectoire_denominateur(e["bibliotheque"], issues, instances, k, cache)
log_w = [a - b for a, b in zip(num, den)]
with open(E1B, encoding="utf-8") as f:
    noyau = json.load(f)["journal"][0]
resultat = {"recalcul_par_l_agent": {"log_w_finale": round(log_w[-1], 6), "log_w_max": round(max(log_w), 6)},
            "noyau": {"log_w_finale": round(noyau["log_w_finale"], 6), "log_w_max": round(noyau["log_w_max"], 6)},
            "identiques": round(log_w[-1], 6) == round(noyau["log_w_finale"], 6) and round(max(log_w), 6) == round(noyau["log_w_max"], 6),
            "membres_de_la_bibliotheque_lus_dans_engagement": [m["nom"] for m in e["bibliotheque"]]}
with open(SORTIE, "w", encoding="utf-8") as f:
    json.dump(resultat, f, ensure_ascii=False, indent=1)
print(json.dumps(resultat, ensure_ascii=False, indent=1))
