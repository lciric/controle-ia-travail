"""Fusion des tranches des essais de taille et de puissance — v1. Lit les fichiers de sorties/ (tranches scellées),
vérifie que les tranches d'un même cas sont disjointes et contiguës, recompte et écrit une table par cas et par méthode.
Usage : python -I essai_projection_fusion_v1.py taille|puissance SORTIE.json"""
import glob
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np

import essai_projection_commun_v1 as cm
from essai_projection_puissance_v1 import apparie


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    genre, sortie = sys.argv[1], sys.argv[2]
    if os.path.exists(sortie):
        raise SystemExit("sortie existante")
    ici = os.path.dirname(os.path.abspath(__file__))
    fichiers = sorted(glob.glob(os.path.join(ici, "sorties", f"{genre}-*-v1.json")))
    groupes = {}
    for f in fichiers:
        d = json.load(open(f))
        cle = d["cas"] if genre == "taille" else f"{d['cas']}|{d['dose']}"
        groupes.setdefault(cle, []).append((d, os.path.relpath(f, ici), sha(f)))
    table = {}
    for cle, lst in sorted(groupes.items()):
        lst.sort(key=lambda t: t[0]["r_debut"])
        for (a, _, _), (b, _, _) in zip(lst, lst[1:]):
            if a["r_fin"] != b["r_debut"]:
                raise SystemExit(f"tranches non contiguës pour {cle}")
        par = {}
        for d, _, _ in lst:
            for n, v in d["par_monde"].items():
                par.setdefault(n, []).extend(v)
        entree = {"tranches": [{"fichier": p, "sha256": h, "r": [d["r_debut"], d["r_fin"]]} for d, p, h in lst],
                  "mondes": sum(d["mondes"] for d, _, _ in lst)}
        meth = {}
        for n, v in par.items():
            prom = [x[0] if isinstance(x, list) else x for x in v]
            k, R = int(sum(prom)), len(prom)
            e = {"promues": k, "mondes": R, "taux": round(k / R, 4), "clopper_pearson_95": cm.clopper_pearson(k, R)}
            if genre == "taille":
                e["monde_dans_la_classe"] = lst[0][0]["methodes"][n]["monde_dans_la_classe"]
                e["log_w_max_maximum"] = max(x[1] for x in v)
                e["temps_processeur_moyen_s"] = round(float(np.mean([d["methodes"][n]["temps_processeur_moyen_s"] for d, _, _ in lst])), 4)
            else:
                e["temps_processeur_moyen_s"] = round(float(np.mean([d["bras"][n]["temps_processeur_moyen_s"] for d, _, _ in lst])), 4)
            meth[n] = e
        entree["methodes"] = meth
        if genre == "puissance":
            prom = {n: [int(x) for x in v] for n, v in par.items()}
            entree["comparaisons_appariees"] = {f"{n}_contre_{r}": apparie(prom[n], prom[r])
                                                for n in prom if n[0] == "M" for r in ("R9", "RLa", "R8")}
        table[cle] = entree
    with open(sortie, "w") as f:
        json.dump({"essai": genre, "fusion_de": len(fichiers), "table": table}, f, ensure_ascii=False, indent=1)
    print("écrit", sortie, len(table), "groupes")


if __name__ == "__main__":
    main()
