"""É5 (décompte) : débit mesuré de la course de dose-réponse (8B, A100, génération + activations), ancre du devis.
Entrées : blocs-commences.jsonl (git show 42cdfcf29), mesures.jsonl des 64 blocs. Comptes et durées seulement."""
import json, subprocess, sys, statistics as st
from datetime import datetime
from pathlib import Path
S = Path(sys.argv[1])
brut = subprocess.run(["git", "-C", "/home/user/controle-ia-travail", "show",
                       "42cdfcf29:donnees/20261125-093202-dose-reponse/blocs-commences.jsonl"], capture_output=True, text=True, check=True).stdout
inst = [datetime.fromisoformat(json.loads(l)["instant"]) for l in brut.splitlines()]
ecarts = [(b - a).total_seconds() / 60 for a, b in zip(inst, inst[1:])]
jet, tronq, n = [], 0, 0
par_cond = {}
for d in sorted((S / "entrees/dose-reponse-blocs").iterdir()):
    for l in (d / "mesures.jsonl").read_text().splitlines():
        m = json.loads(l); jet.append(m["jetons"]); tronq += m["tronquee"]; n += 1
        par_cond.setdefault(m["condition"], []).append(m["jetons"])
min_par_bloc = st.median(ecarts)
sortie = {
 "blocs": len(inst), "actions_par_bloc": 300, "premier_bloc": inst[0].isoformat(), "dernier_bloc_commence": inst[-1].isoformat(),
 "minutes_par_bloc_mediane": round(min_par_bloc, 2), "minutes_par_bloc_moyenne": round(st.mean(ecarts), 2),
 "minutes_par_bloc_min_max": [round(min(ecarts), 2), round(max(ecarts), 2)],
 "actions_par_heure_carte": round(300 / (st.mean(ecarts) / 60), 1),
 "duree_course_heures_63_blocs_plus_un": round(st.mean(ecarts) * 64 / 60, 2),
 "jetons_generes_par_action_moyenne": round(st.mean(jet), 1), "mediane": st.median(jet), "max": max(jet),
 "part_tronquee_a_400": round(tronq / n, 4), "actions": n,
 "jetons_par_seconde_carte": round(st.mean(jet) * 300 / (st.mean(ecarts) * 60), 1),
 "jetons_moyens_honnete": round(st.mean(par_cond["honnete"]), 1),
 "prix_carte_usd_h_releve_registre_depenses_l639": 1.1933,
}
sortie["cout_usd_course_19200_actions_estime"] = round(sortie["duree_course_heures_63_blocs_plus_un"] * 1.1933 + 1.0417, 2)
print(json.dumps(sortie, indent=1, ensure_ascii=False))
