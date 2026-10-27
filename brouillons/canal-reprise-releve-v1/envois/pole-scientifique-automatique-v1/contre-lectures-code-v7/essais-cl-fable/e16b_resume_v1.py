"""E16b : résumé des courses de E16 (bras « mécanique » du duel) : gardes d'héritage, promotions dues au seul héritage,
et, par génération, m, k* et rang des témoins vrais dans la règle e-BH.

Usage : python -I -B e16b_resume_v1.py SORTIE.json DOSSIER_E16 [DOSSIER_E16 ...]
"""
import glob
import json
import os
import sys

sortie, dossiers = sys.argv[1], sys.argv[2:]
total = {"mondes": 0, "generations": 0, "gardes_heritage": 0, "promues_par_le_seul_heritage": 0,
         "generations_ou_les_3_temoins_vrais_sont_retenus": 0, "generations_avec_au_moins_une_fiche_reelle_retenue": 0,
         "fiches_reelles_retenues": 0, "fiches_reelles_retenues_qui_ne_le_seraient_pas_sans_les_temoins_dans_k": 0}
for dossier in dossiers:
    for course in sorted(glob.glob(os.path.join(dossier, "course-mecanique-*"))):
        total["mondes"] += 1
        for j in sorted(glob.glob(os.path.join(course, "journal", "generation-*.json"))):
            with open(j, encoding="utf-8") as f:
                d = json.load(f)
            total["generations"] += 1
            total["gardes_heritage"] += sum(1 for g in d["gardes_de_redite"].values() if "héritage" in (g.get("motif") or ""))
            jugees = {k: i for k, i in d["fiches"].items() if (i.get("pari") or {}).get("multiplicite")}
            if not jugees:
                continue
            m = next(iter(jugees.values()))["pari"]["multiplicite"]["m"]
            vraies = [k for k, i in jugees.items() if i.get("temoin") == "vraie"]
            if vraies and all(jugees[k]["pari"]["multiplicite"]["retenue"] for k in vraies) and len(vraies) == 3:
                total["generations_ou_les_3_temoins_vrais_sont_retenus"] += 1
            reelles = {k: i for k, i in jugees.items() if not i.get("temoin")}
            retenues = [k for k, i in reelles.items() if i["pari"]["multiplicite"]["retenue"] and i["verdict_final"] == "survit"]
            total["fiches_reelles_retenues"] += len(retenues)
            total["generations_avec_au_moins_une_fiche_reelle_retenue"] += bool(retenues)
            for k, i in reelles.items():
                h = i["pari"].get("heritage")
                if i["verdict_final"] == "survit" and h and not h.get("promue_sans_heritage"):
                    total["promues_par_le_seul_heritage"] += 1
            # e-BH recalculée sur les seules fiches réelles (témoins comptés dans m avec e = 0)
            valeurs = sorted((i["pari"]["multiplicite"]["log_e"] for i in reelles.values()), reverse=True)
            import math
            k_etoile = 0
            for rang, v in enumerate(valeurs, 1):
                if v >= math.log(m / (0.05 * rang)):
                    k_etoile = rang
            total["fiches_reelles_retenues_qui_ne_le_seraient_pas_sans_les_temoins_dans_k"] += max(0, len(retenues) - k_etoile)
with open(sortie, "w", encoding="utf-8") as f:
    json.dump(total, f, ensure_ascii=False, indent=1)
print(json.dumps(total, ensure_ascii=False, indent=1))
