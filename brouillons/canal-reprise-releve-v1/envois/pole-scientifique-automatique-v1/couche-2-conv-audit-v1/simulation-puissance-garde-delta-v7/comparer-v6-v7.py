"""Compare, champ par champ, des sorties de la v6 et de la v7 tirées à la même graine (identité du défaut `logit` de la v7 avec la v6).
Chaque paire : sortie v6, sortie v7. Champs exclus de la comparaison : en-tête de traçabilité (version, empreinte du script,
commit, état du script, environnement) et le nom du fichier de sortie. Rend, par paire : champs communs, différences, champs
propres à chaque sortie (les champs propres à la v7 attendus : `reglages/echelle_dispersion`, `reglages/K_s`,
`reglages/paires_K_h_K_s`).

Avec --cellules, seules les cellules (/cellules/…) sont comparées, et seulement celles que les deux sorties ont en commun
(deux passages d'options différentes, mêmes étiquettes de cellule, donc mêmes tirages).

Usage : python3 -I -B comparer-v6-v7.py [--cellules] SORTIE.json V6_1.json V7_1.json [V6_2.json V7_2.json …]
"""

import hashlib
import json
import sys

EXCLUS = ("/version", "/script_sha256", "/commit", "/etat_du_script", "/environnement", "/reglages/sortie")
ATTENDUS_V7 = {"/reglages/echelle_dispersion", "/reglages/K_s", "/reglages/paires_K_h_K_s"}


def plat(d, p=""):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from plat(v, f"{p}/{k}")
    elif isinstance(d, list) and d and all(isinstance(x, list) for x in d):
        for i, v in enumerate(d):
            yield from plat(v, f"{p}/{i}")
    else:
        yield p, d


args = sys.argv[1:]
seulement_cellules = bool(args) and args[0] == "--cellules"
if seulement_cellules:
    args = args[1:]
sortie, fichiers = args[0], args[1:]
if len(fichiers) % 2:
    raise SystemExit("refus : paires (v6, v7) attendues")
bilan = {"paires": [], "seulement_cellules": seulement_cellules}
for a, b in zip(fichiers[::2], fichiers[1::2]):
    va, vb = dict(plat(json.load(open(a)))), dict(plat(json.load(open(b))))
    communs = [k for k in va if k in vb and not k.startswith(EXCLUS) and (not seulement_cellules or k.startswith("/cellules/"))]
    diffs = [k for k in communs if va[k] != vb[k]]
    cellules_communes = {k.split("/")[2] for k in communs if k.startswith("/cellules/")}
    seulement_v7 = sorted(k for k in vb if k not in va and not k.startswith(EXCLUS) and (not seulement_cellules or k.startswith("/cellules/")))
    seulement_v6 = [k for k in va if k not in vb and not k.startswith(EXCLUS) and (not seulement_cellules or k.startswith("/cellules/"))]
    if seulement_cellules:  # cellules propres à l'une des sorties : hors comparaison (passages d'options différentes)
        seulement_v6 = [k for k in seulement_v6 if k.split("/")[2] in cellules_communes]
    seulement_v7_hors_cellules_nouvelles = sorted(k for k in seulement_v7
                                                  if not (k.startswith("/cellules/") and k.split("/")[2] not in cellules_communes))
    bilan["paires"].append({
        "v6": a, "v6_sha256": hashlib.sha256(open(a, "rb").read()).hexdigest(),
        "v7": b, "v7_sha256": hashlib.sha256(open(b, "rb").read()).hexdigest(),
        "champs_communs": len(communs), "cellules_communes": len(cellules_communes), "differences": len(diffs),
        "exemples_de_differences": [{"champ": k, "v6": va[k], "v7": vb[k]} for k in diffs[:20]],
        "champs_seulement_v6": seulement_v6,
        "champs_seulement_v7_nombre": len(seulement_v7),
        "champs_seulement_v7_hors_cellules_nouvelles": seulement_v7_hors_cellules_nouvelles[:60],
        "champs_seulement_v7_attendus": all(any(x == y or x.startswith(y + "/") for y in ATTENDUS_V7)
                                            for x in seulement_v7_hors_cellules_nouvelles)})
bilan["identiques_sur_les_champs_communs"] = all(p["differences"] == 0 for p in bilan["paires"])
bilan["aucun_champ_perdu"] = all(not p["champs_seulement_v6"] for p in bilan["paires"])
bilan["conforme"] = bilan["identiques_sur_les_champs_communs"] and bilan["aucun_champ_perdu"] and all(p["champs_seulement_v7_attendus"] for p in bilan["paires"])
with open(sortie, "x", encoding="utf-8") as f:
    json.dump(bilan, f, indent=1, ensure_ascii=False)
    f.write("\n")
for p in bilan["paires"]:
    print(p["v6"].split("/")[-1], "|", p["v7"].split("/")[-1], ": communs", p["champs_communs"], "; cellules", p["cellules_communes"],
          "; différences", p["differences"], "; seulement v6", p["champs_seulement_v6"], "; seulement v7 (hors cellules nouvelles)",
          p["champs_seulement_v7_hors_cellules_nouvelles"])
print("conforme :", bilan["conforme"])
