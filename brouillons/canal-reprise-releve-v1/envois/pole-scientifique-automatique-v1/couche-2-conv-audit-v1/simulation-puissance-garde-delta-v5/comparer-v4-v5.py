"""Compare, champ par champ, des sorties de la v4 et de la v5 tirées à la même graine (point 8 de la commande v5).
Chaque paire : sortie v4, sortie v5. Champs exclus de la comparaison : en-tête de traçabilité (version, empreinte du script,
commit, état du script, environnement). Rend, par paire : champs communs, différences, champs propres à chaque sortie.

Usage : python3 -I -B comparer-v4-v5.py SORTIE.json V4_1.json V5_1.json [V4_2.json V5_2.json …]
"""

import hashlib
import json
import sys

EXCLUS = ("/version", "/script_sha256", "/commit", "/etat_du_script", "/environnement")


def plat(d, p=""):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from plat(v, f"{p}/{k}")
    else:
        yield p, d


sortie, fichiers = sys.argv[1], sys.argv[2:]
if len(fichiers) % 2:
    raise SystemExit("refus : paires (v4, v5) attendues")
bilan = {"paires": []}
for a, b in zip(fichiers[::2], fichiers[1::2]):
    va, vb = dict(plat(json.load(open(a)))), dict(plat(json.load(open(b))))
    communs = [k for k in va if k in vb and not k.startswith(EXCLUS)]
    diffs = [k for k in communs if va[k] != vb[k]]
    cellules_communes = {k.split("/")[2] for k in communs if k.startswith("/cellules/")}
    bilan["paires"].append({
        "v4": a, "v4_sha256": hashlib.sha256(open(a, "rb").read()).hexdigest(),
        "v5": b, "v5_sha256": hashlib.sha256(open(b, "rb").read()).hexdigest(),
        "champs_communs": len(communs), "cellules_communes": len(cellules_communes), "differences": len(diffs),
        "exemples_de_differences": [{"champ": k, "v4": va[k], "v5": vb[k]} for k in diffs[:20]],
        "champs_seulement_v4": [k for k in va if k not in vb and not k.startswith(EXCLUS)],
        "champs_seulement_v5_nombre": sum(1 for k in vb if k not in va and not k.startswith(EXCLUS)),
        "champs_seulement_v5_hors_cellules_nouvelles": sorted({k for k in vb if k not in va and not k.startswith(EXCLUS)
                                                               and not (k.startswith("/cellules/") and k.split("/")[2] not in cellules_communes)})[:60]})
bilan["identiques_sur_les_champs_communs"] = all(p["differences"] == 0 for p in bilan["paires"])
with open(sortie, "x", encoding="utf-8") as f:
    json.dump(bilan, f, indent=1, ensure_ascii=False)
    f.write("\n")
for p in bilan["paires"]:
    print(p["v4"].split("/")[-1], "|", p["v5"].split("/")[-1], ": communs", p["champs_communs"], "; cellules", p["cellules_communes"],
          "; différences", p["differences"], "; seulement v4", p["champs_seulement_v4"])
