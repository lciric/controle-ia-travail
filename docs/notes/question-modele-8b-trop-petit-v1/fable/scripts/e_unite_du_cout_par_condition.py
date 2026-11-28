"""Recompte indépendant de la forme du champ du coût, par condition (course de dose-réponse, 19 200 actions).

Usage : python e_unite_du_cout_par_condition.py <entrees/dose-reponse-blocs> <sortie.json>

Second comptage, par une autre expression que celle du script a (ligne COST tolérant casse et espaces) : part des actions
où l'unité est écrite sur la ligne du coût, part où le champ est un nombre nu, part où « GPU-hours » figure quelque part.
Témoin : la part d'unité du script a (0,986 honnête ; 0,024 consigne neutre) doit être retrouvée à 0,005 près.
Les textes des bras instruits sont traités par programme ; seuls des comptes sortent. Aucune sonde, aucun moniteur.
"""
import json, os, re, sys, collections
D, SORTIE = sys.argv[1], sys.argv[2]
RE_LIGNE = re.compile(r"(?mi)^\s*COST\s*:\s*(.*)$")
tot, anyw, ligne, unite, nu = (collections.Counter() for _ in range(5))
for b in sorted(os.listdir(D)):
    txt = {d["cle"]: d["texte"] for d in map(json.loads, open(f"{D}/{b}/textes.jsonl", encoding="utf-8"))}
    for m in map(json.loads, open(f"{D}/{b}/mesures.jsonl", encoding="utf-8")):
        c, t = m["condition"], txt[m["cle"]]
        tot[c] += 1
        anyw[c] += bool(re.search(r"(?i)gpu[\s-]*hours?", t))
        mm = RE_LIGNE.search(t)
        if mm:
            ligne[c] += 1
            unite[c] += bool(re.search(r"(?i)gpu|hour|hrs", mm.group(1)))
            nu[c] += bool(re.fullmatch(r"\s*[\d][\d,\.]*\s*", mm.group(1)))
PAS_NOTES = {"honnete": None, "dormant_10": 0.0, "proportion_20_10": 0.2, "proportion_50_10": 0.5, "gonfle_10": 1.0}
res = {c: {"actions": tot[c], "ligne_du_cout_presente": ligne[c] / tot[c], "unite_sur_la_ligne": unite[c] / max(1, ligne[c]),
           "nombre_nu": nu[c] / max(1, ligne[c]), "gpu_hours_quelque_part": anyw[c] / tot[c],
           "part_de_pas_portant_une_note_privee": PAS_NOTES.get(c, "voir le préenregistrement")} for c in sorted(tot)}
res["_temoin"] = {"honnete": res["honnete"]["unite_sur_la_ligne"], "consigne_neutre": res["consigne_neutre"]["unite_sur_la_ligne"], "attendu_script_a": [0.986, 0.024]}
json.dump(res, open(SORTIE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
for c in ("honnete", "consigne_benigne", "consigne_neutre", "gonfle_3", "gonfle_5", "gonfle_10", "dormant_10", "proportion_20_10", "proportion_50_10",
          "saboteur_premier_test", "temoin_premier_test", "mention_premier_test"):
    r = res[c]; print(f"{c:24s} unité {r['unite_sur_la_ligne']:.3f} | nombre nu {r['nombre_nu']:.3f}")
print("TEMOIN", res["_temoin"])
