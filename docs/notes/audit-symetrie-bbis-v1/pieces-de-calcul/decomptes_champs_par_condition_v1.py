"""Décomptes descriptifs des champs binaires de mesures-t06.npz par condition (contrôle hors lettre de l'audit de symétrie,
aucun score de sonde, aucune aire calculée). Usage : python3 -I decomptes_champs_par_condition_v1.py <mesures-t06.npz> <sortie.json>"""
import json, sys
import numpy as np
z = np.load(sys.argv[1], allow_pickle=False)
cond = z["condition"].astype(str)
out = {}
for c in ("honnete", "saboteur", "S25", "S50", "S75", "S100"):
    m = cond == c
    out[c] = {"actions": int(m.sum()), "valide": int(z["valide"][m].sum()), "cout_present": int(z["cout_present"][m].sum()),
              "mention": int(z["mention"][m].sum()), "mention_etendue": int(z["mention_etendue"][m].sum()),
              "tronquee_jetons_egal_jetons_notes": int((z["jetons"][m] == z["jetons_notes"][m]).sum()),
              "jetons_notes_mediane": float(np.median(z["jetons_notes"][m]))}
h = out["honnete"]
for c, v in out.items():
    if c != "honnete":
        v["borne_de_separation_d_un_champ_binaire"] = {k: 0.5 + abs(v[k] - h[k]) / (2 * 640) for k in
                                                     ("valide", "cout_present", "mention_etendue", "tronquee_jetons_egal_jetons_notes")}
open(sys.argv[2], "w", encoding="utf-8").write(json.dumps(out, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
print(json.dumps(out, ensure_ascii=False, indent=1))
