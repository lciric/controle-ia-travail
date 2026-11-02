"""v06 — classe couverte et échos (lecteur du verdict, R13), code propre : pour chaque loi jugée, couverture structurelle
(loi fixe, S1, S2, ou mélange imbriqué de celles-ci) et « hors classe » (log W max > 1e-6 ou non couverte), comparés aux
champs `couverte` et `hors_classe` écrits ; `retour_attendu` = log W max de la tentative précédente arrondi à 2 décimales ;
types des lois promues sous v8 ; deux lectures de l'instrument (« part des lois jugées », section 5 et code ; « part des
tentatives », mot de la section 6, critère 3).
Usage : python3 -I -B v06_classe_echos.py SORTIE.json ORCHESTRATOR MANIFESTE.json SORTIE_JSON"""
import json
import math
import sys
from collections import Counter

sys.dont_write_bytecode = True
sortie = json.load(open(sys.argv[1], encoding="utf-8"))
sys.path.insert(0, sys.argv[2])
import pole.attaque_goodhart_v2 as ag  # noqa: E402  (seulement pour reconstruire S1 et S2 de chaque carte)

E = int(json.load(open(sys.argv[3], encoding="utf-8"))["reglages"]["entropie_racine"])
L = {(w, c): ag.carte(E, c, w)["L"] for w in ("W1", "W2") for c in range(12)}


def couverte(loi, l):
    if not isinstance(loi, dict):
        return False
    if loi.get("type") == "fixe" or loi == l["S1"] or loi == l["S2"]:
        return True
    if loi.get("type") == "melange":
        comps = loi.get("composantes") or []
        return all(couverte(x, l) for x in comps)
    return False


ecarts, n, attendus_faux = [], 0, 0
promues_types = Counter()
part = {}
for s in sortie["suites"]:
    l = L[(s["monde"], s["carte"])]
    prec = None
    for t in s["tentatives"]:
        if t["loi"] is not None and t["verdict"]["statut"] != "evaluation_impossible":
            n += 1
            cv = couverte(t["loi"], l)
            hc = (t["verdict"]["log_w_max"] > 1e-6) or not cv
            if cv != bool(t.get("couverte")) or hc != bool(t.get("hors_classe")):
                ecarts.append((s["monde"], s["fournisseur"], s["condition"], s["juge"], s["carte"], t["k"]))
            if s["juge"] == "v8" and t["verdict"]["promue"]:
                promues_types[(s["monde"], t["loi"]["type"])] += 1
        if s["condition"] == "retour" and prec is not None and "retour_attendu" in t:
            v = prec["verdict"]
            att = round(v["log_w_max"], 2) if (v is not None and v["log_w_max"] is not None
                                                and math.isfinite(v["log_w_max"])) else None
            if att != t["retour_attendu"]:
                attendus_faux += 1
        prec = t
for w in ("W1", "W2"):
    for f in ("ensemble", "argon"):
        sel = [s for s in sortie["suites"] if s["monde"] == w and s["juge"] == "v8" and s["condition"] == "retour"
               and (f == "ensemble" or s["fournisseur"] == f)]
        tent = [t for s in sel for t in s["tentatives"]]
        hors = sum(bool(t.get("hors_classe")) for t in tent if t["loi"] is not None)
        jug = sum(t["loi"] is not None for t in tent)
        part[f"{w}|{f}"] = {"hors_sur_lois_jugees": [hors, jug], "hors_sur_tentatives": [hors, len(tent), hors / len(tent)]}
res = {"lois_jugees_verifiees": n, "ecarts_couverte_hors_classe": ecarts, "retour_attendu_faux": attendus_faux,
       "types_des_lois_promues_sous_v8": {f"{k[0]}|{k[1]}": v for k, v in promues_types.items()},
       "part_hors_classe_deux_lectures": part}
json.dump(res, open(sys.argv[4], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
