"""Compléments du lecteur (rejeu à graine de R1) : chronologie et passes par tranche de dix épisodes, pas comptés près
du U+FFFD, étendue des corrections, désaccords selon le statut, positions connues des découpages non canoniques contre
les bascules, quasi-égalités des trois non résolus tentés. Usage : python3 -I complements_v1.py RACINE_R"""
import json
import sys
from pathlib import Path

import numpy as np

R = Path(sys.argv[1])
S = R / "copie/brouillons/canal-reprise-releve-v1/envois/session-depot/rejeu-graine-sortie-v1"
DV = S / "diag/20261102-171752-r1-graine-validation"
DR = S / "diag/20261102-175806-r1-graine-resolution"
t2 = {x["episode"]: x for x in json.loads((R / "textes-scelles/R1-table-tokenisation-v2.json").read_text())["episodes"]}
out = {}

# chronologie : lignes PROGRES du journal (passes cumulées) et durées écrites par épisode
fv = [json.loads((DV / f"episodes-validation/{k:03d}.json").read_text()) for k in range(147)]
journal = (S / "traces/r1-graine-20261102-181212-iXsM/journal.txt").read_text().splitlines()
prog = [ln for ln in journal if ln.startswith("PROGRES") and "etape=validation" in ln]
out["progres_validation"] = prog
passes = {}
for ln in prog:
    champs = dict(x.split("=", 1) for x in ln.split()[2:])
    if "/" in champs.get("episodes", ""):
        passes[int(champs["episodes"].split("/")[0])] = (ln.split()[1], int(champs["passes"]))
tranches = []
prec = ("2026-11-02T17:18:25Z", 0)
for b in sorted(passes):
    a = max(0, b - 10)
    eps = fv[a:b]
    comp = {}
    for x in eps:
        c = "non_tente" if x.get("non_tente") else (x["voie"] or "non_resolu")
        comp[c] = comp.get(c, 0) + 1
    p_dir = sum(x["passes"] for x in eps if x["voie"] == "directe")
    tranches.append({"k": f"{a}..{b - 1}", "fin": passes[b][0], "passes_tranche": passes[b][1] - prec[1],
                     "durees_s": round(sum(x["duree_s"] for x in eps), 2), "composition": comp,
                     "passes_des_directs": p_dir, "passes_hors_directs": passes[b][1] - prec[1] - p_dir})
    prec = passes[b]
out["tranches_validation"] = tranches
out["fffd_somme_147"] = sum(x["fffd"] for x in fv)

# pas comptés (recherche sur octets inconnus) dans le journal des pas de la résolution
z = np.load(DR / "pas-resolution-graine-resolution.npz")
noms = [str(x) for x in z["episodes"]]
i = noms.index("mention/2605.17899v2/e0")
m = (z["episode"] == i) & z["balayage"]
out["mention_pas_comptes"] = [{"pas": int(z["pas"][j]), "rang": int(z["rang"][j]), "choix": int(z["choix"][j]),
                               "non_contraint": int(z["non_contraint"][j]), "candidats": int(z["candidats"][j]),
                               "ecart": float(z["ecart"][j]), "p_k": float(z["p_k"][j])} for j in np.where(m)[0]]

# étendue des corrections (résolution) : identifiants de base contre identifiants retrouvés
res = json.loads((DR / "resolution-graine-resolution.json").read_text())["resultat"]
det = {d["episode"]: d for d in res["episodes"]}
etendues = {}
for e, d in det.items():
    lst = []
    for t, (b, v) in enumerate(zip(d["base_nv"], d["ids"])):
        if b != v:
            p = 0
            while p < min(len(b), len(v)) and b[p] == v[p]:
                p += 1
            s = 0
            while s < min(len(b), len(v)) - p and b[-1 - s] == v[-1 - s]:
                s += 1
            lst.append({"action": t, "longueur_base": len(b), "longueur_p3": len(v), "premier_ecart": p,
                        "jetons_base": len(b) - p - s, "jetons_p3": len(v) - p - s})
    etendues[e] = {"voie": d["voie"], "bascules": [(x["pas"], x["rang"]) for x in d["forcages"]], "corrections": lst}
out["etendues_resolution"] = etendues

# désaccords du choix non contraint, selon que l'épisode est résolu ou non (validation)
zv = np.load(DV / "pas-resolution-graine-validation.npz")
nv = [str(x) for x in zv["episodes"]]
par = {x["episode"]: x for x in fv}
resolu = np.array([par[nv[i]]["empreinte"] == par[nv[i]]["empreinte_cible"] for i in zv["episode"]], dtype=bool)
des = zv["choix"] != zv["non_contraint"]
out["desaccords_validation"] = {
    lab: {"pas": int(msk.sum()), "desaccords": int((des & msk).sum()),
          "marge_sous_0_5": int((des & msk & (zv["marge"] < 0.5)).sum()),
          "marge_sous_0_1": int((des & msk & (zv["marge"] < 0.1)).sum()),
          "ecart_contraint_sous_1": int((msk & (zv["candidats"] > 1) & (zv["ecart"] < 1)).sum())}
    for lab, msk in (("resolus", resolu), ("non_resolus", ~resolu))}

# découpages non canoniques connus (table v2) contre bascules : épisodes tentés de la validation
out["corriges_tentes"] = [{"episode": x["episode"], "methode_v2": t2[x["episode"]]["methode"],
                           "positions_v2": [(p["pas"], p["rang"]) for p in t2[x["episode"]]["paires"]],
                           "fins_v2": t2[x["episode"]]["fins"], "voie": x["voie"],
                           "bascules": [(f["pas"], f["rang"]) for f in x["forcages"]]}
                          for x in fv if x["episode"] in t2 and t2[x["episode"]]["methode"] != "non_resolu"
                          and not x.get("non_tente")]
out["c6_resolution"] = [{"episode": e, "positions_v2": [(p["pas"], p["rang"]) for p in t2[e]["paires"]],
                         "bascules": etendues[e]["bascules"]}
                        for e in ("honnete/2512.05150v2/e0", "honnete/2512.11131v1/e0", "temoin/2510.24788v1/e0")]

# quasi-égalités et repli des trois non résolus tentés
out["non_resolus_tentes"] = [{"k": k, "episode": fv[k]["episode"], "duree_s": fv[k]["duree_s"],
                              "quasi_egalites": [(q["pas"], q["rang"], round(q["ecart"], 4))
                                                 for q in fv[k].get("quasi_egalites") or []],
                              "repli": fv[k].get("repli"), "empreinte": fv[k].get("empreinte"),
                              "empreinte_cible": fv[k]["empreinte_cible"]} for k in (0, 20, 56)]
print(json.dumps(out, ensure_ascii=False, indent=1))
