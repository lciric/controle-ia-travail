"""E1 — validateur d'action du brouillon (G0) sur les textes reels de la course de dose-reponse (42cdfcf29),
episode par episode, avec le vrai `propositions.appliquer`. Sortie : `sorties/e1-actions.jsonl` (une ligne par action :
cle, condition, tache, replique, pas, sous-predicats ; aucun texte) et `sorties/e1-acceptation.json` (comptes et taux).
Aucun seuil n'est regle ici : les criteres de mort sont ceux du mandat."""
from __future__ import annotations

import json, sys, pathlib, hashlib
from collections import Counter, defaultdict

import numpy as np

from controle_ia.environnements.propositions import Etat, appliquer, lire_action
from validateur_c_furtif import detail

D = pathlib.Path(sys.argv[1]); S = pathlib.Path(sys.argv[2])
CONDS = ("honnete", "consigne_neutre", "gonfle_2", "gonfle_3", "gonfle_5")
blocs = sorted((D / "blocs").iterdir())
lignes = []
for b in blocs:
    mes = {m["cle"]: m for m in map(json.loads, open(b / "mesures.jsonl", encoding="utf-8"))}
    txt = {d["cle"]: d["texte"] for d in map(json.loads, open(b / "textes.jsonl", encoding="utf-8"))}
    par_ep = defaultdict(list)
    for cle, m in mes.items():
        if m["condition"] in CONDS:
            par_ep[m["episode"]].append(m)
    for ep, ms in sorted(par_ep.items()):
        ms.sort(key=lambda m: m["pas"])
        assert [m["pas"] for m in ms] == list(range(10)), (ep, [m["pas"] for m in ms])
        etat = Etat()
        for m in ms:
            t = txt[m["cle"]]
            d = detail(etat, 0, m["pas"], t)
            a = appliquer(etat, 0, m["pas"], t)          # l'episode reel avance avec l'action reelle, valide ou non
            assert bool(lire_action(t).valide) == bool(m["valide"]), (m["cle"], m["valide"])   # la mesure « valide » est celle de lire_action, sans etat
            lignes.append({"cle": m["cle"], "condition": m["condition"], "tache": m["tache"], "replique": m["replique"],
                           "pas": m["pas"], "tronquee": bool(m["tronquee"]), "jetons": int(m["jetons"]),
                           "jetons_notes": int(m["jetons_notes"]), "mention_texte_prive": bool(m["mention_texte_prive"]),
                           "cout": m["cout"], "valide_lire_action": bool(m["valide"]), "valide_appliquer": bool(a.valide), "motif_appliquer": a.motif, "n_propositions_avant": len(etat.propositions) - (1 if a.valide and a.operation == "ADD" else 0),
                           **{k: v for k, v in d.items()}})
with open(S / "e1-actions.jsonl", "w", encoding="utf-8") as f:
    for l in lignes:
        f.write(json.dumps(l, ensure_ascii=False) + "\n")

def taux(sel, cle="accepte"):
    return float(np.mean([l[cle] for l in sel])) if sel else None

SOUS = ("p1", "p1_valide", "p1_cinq_champs", "p2", "p2_sans_gras", "p2_six_cles", "p2_ordre_colonne0", "p2_premiere_ligne_brute",
        "p2_premiere_ligne_strip", "p3", "p3_champ", "p3_ligne", "p4", "p4_corps", "p4_prediction")
res = {"entrees": {"blocs": len(blocs), "actions": len(lignes)}, "par_condition": {}, "par_condition_pas": {},
       "par_condition_tache": {}, "mots_predicat4": {}}
for c in CONDS:
    sel = [l for l in lignes if l["condition"] == c]
    r = {"actions": len(sel), "accepte": taux(sel), "accepte_lecture_strip": taux(sel, "accepte_strip"),
         "tronquees": taux(sel, "tronquee"), "mention_texte_prive": taux(sel, "mention_texte_prive")}
    r["tenu"] = {k: taux(sel, k) for k in SOUS}
    # rejet du seul fait d'un predicat (les trois autres tenus)
    for p in ("p1", "p2", "p3", "p4"):
        autres = [q for q in ("p1", "p2", "p3", "p4") if q != p]
        r[f"rejet_du_seul_{p}"] = float(np.mean([(not l[p]) and all(l[q] for q in autres) for l in sel]))
    # acceptation si l'on retire un predicat
    for p in ("p1", "p2", "p3", "p4"):
        autres = [q for q in ("p1", "p2", "p3", "p4") if q != p]
        r[f"accepte_sans_{p}"] = float(np.mean([all(l[q] for q in autres) for l in sel]))
    r["accepte_sans_p3_ni_p4"] = float(np.mean([l["p1"] and l["p2"] for l in sel]))
    r["p1_manquants"] = dict(Counter(k for l in sel for k in l["p1_manquants"]).most_common())
    r["p1_manque_prediction_et_tronquee"] = float(np.mean([("PREDICTION" in l["p1_manquants"]) and l["tronquee"] for l in sel]))
    r["tronquee_et_p1_tenu"] = float(np.mean([l["tronquee"] and l["p1"] for l in sel]))
    res["par_condition"][c] = r
    res["par_condition_pas"][c] = {str(t): taux([l for l in sel if l["pas"] == t]) for t in range(10)}
    pt = defaultdict(list)
    for l in sel:
        pt[l["tache"]].append(l["accepte"])
    tt = {t: float(np.mean(v)) for t, v in sorted(pt.items())}
    res["par_condition_tache"][c] = {"taux": tt, "taches": len(tt), "taches_sous_10pc": int(sum(v < 0.10 for v in tt.values())),
                                     "taches_a_zero": int(sum(v == 0 for v in tt.values())),
                                     "quantiles": {q: float(np.quantile(list(tt.values()), float(q))) for q in ("0.0", "0.1", "0.25", "0.5", "0.75", "0.9", "1.0")}}
    res["mots_predicat4"][c] = {"corps": dict(Counter(w for l in sel for w in l["p4_mots_corps"]).most_common(25)),
                                "prediction": dict(Counter(w for l in sel for w in l["p4_mots_prediction"]).most_common(30))}
res["sha256_actions"] = hashlib.sha256((S / "e1-actions.jsonl").read_bytes()).hexdigest()
(S / "e1-acceptation.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
for c in CONDS:
    r = res["par_condition"][c]
    print(f"{c:16s} accepte={r['accepte']:.4f} (strip {r['accepte_lecture_strip']:.4f}) | p1={r['tenu']['p1']:.3f} p2={r['tenu']['p2']:.3f} "
          f"p3={r['tenu']['p3']:.3f} p4={r['tenu']['p4']:.3f} | corps={r['tenu']['p4_corps']:.3f} pred={r['tenu']['p4_prediction']:.3f} "
          f"| taches<10%: {res['par_condition_tache'][c]['taches_sous_10pc']}/64, a zero: {res['par_condition_tache'][c]['taches_a_zero']}")
