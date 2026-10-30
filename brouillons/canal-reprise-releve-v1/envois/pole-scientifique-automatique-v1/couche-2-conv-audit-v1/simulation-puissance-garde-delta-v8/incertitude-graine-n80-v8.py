"""Incertitude de graine de n80 et n90 (GD2-07), mesurée : quatre graines maîtresses (20261029 des passages principaux, 1, 2, 3 des compléments), même script,
mêmes options, ligne la plus exigeante (K_h = 5, K_s = 10, biais δ/4 = 0,0125, k = 8, A et B à ρ = 0,05 puis 0,17, lecture (A), 2 000 répétitions).
Lit `simulation-puissance-garde-delta-v8-sortie-meme-rho{0.05,0.17}.json` (graine 20261029) et `simulation-puissance-garde-delta-v8-complement-graine{1,2,3}-meme-rho{0.05,0.17}.json`.
Écrit un JSON (mode « x ») : par mesure, les n80 des quatre graines, leur moyenne, l'écart relatif maximal à la moyenne et l'étendue relative.
Usage : python3 -I -B incertitude-graine-n80-v8.py DOSSIER SORTIE.json
"""
import hashlib
import json
import os
import re
import sys

DOSSIER, SORTIE = sys.argv[1:3]
FICHIERS = {}
for rho in ("0.05", "0.17"):
    FICHIERS[rho] = {20261029: f"simulation-puissance-garde-delta-v8-sortie-meme-rho{rho}.json"}
    for g in (1, 2, 3):
        FICHIERS[rho][g] = f"simulation-puissance-garde-delta-v8-complement-graine{g}-meme-rho{rho}.json"
res = {"definition": "écart relatif maximal = max |n80_graine − moyenne| / moyenne ; étendue relative = (max − min) / moyenne ; n80 de la ligne K_h = 5, K_s = 10, biais 0,0125, k = 8",
       "empreintes": {}, "lignes": {}}
for rho, par_graine in FICHIERS.items():
    for mesure in ("retenue_ebh", "atteinte_160"):
        for cible in ("n80", "n90"):
            vals = {}
            for g, f in par_graine.items():
                chemin = os.path.join(DOSSIER, f)
                d = json.load(open(chemin, encoding="utf-8"))
                assert d["reglages"]["graine"] == g and d["reglages"]["repetitions"] == 2000, (f, d["reglages"]["graine"])
                res["empreintes"][f] = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
                v = None
                for nm, loi in d["lois"].items():
                    m = re.search(r"Kh(\d+)_Ks(\d+)_", nm)
                    if int(m.group(1)) == 5 and int(m.group(2)) == 10 and "n_pour_puissance_0_8_fiche" in loi:
                        v = loi["n_pour_puissance_0_8_fiche"].get("delta=0.05|biais=0.0125|k=8")
                        if v is not None:
                            break
                assert v is not None and v[cible][mesure]["n_approx"] is not None, (f, cible, mesure)
                vals[g] = v[cible][mesure]["n_approx"]
            xs = list(vals.values())
            moy = sum(xs) / len(xs)
            res["lignes"][f"rho={rho}|{cible}|{mesure}"] = {"n_par_graine": vals, "moyenne": moy, "ecart_relatif_maximal": max(abs(x - moy) for x in xs) / moy,
                                                             "etendue_relative": (max(xs) - min(xs)) / moy}
res["ecart_relatif_maximal_toutes_lignes"] = max(l["ecart_relatif_maximal"] for l in res["lignes"].values())
res["etendue_relative_maximale_toutes_lignes"] = max(l["etendue_relative"] for l in res["lignes"].values())
with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
    f.write("\n")
for k, l in res["lignes"].items():
    print(k, l["n_par_graine"], f"écart max {l['ecart_relatif_maximal']:.3f} étendue {l['etendue_relative']:.3f}")
print("écart relatif maximal", round(res["ecart_relatif_maximal_toutes_lignes"], 3), "étendue maximale", round(res["etendue_relative_maximale_toutes_lignes"], 3))
