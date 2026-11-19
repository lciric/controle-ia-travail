"""Essai (R5) du calcul des verdicts du lecteur neuf sur les cas gelés du texte gelé, P.4, qui se construisent sur des tables, avec les
références publiées empreintées de Qwen3-8B ramenées à 32 couches (plan de lecture v2, étape A). Imprime chaque cas, l'attendu du texte
et le résultat ; code de sortie 1 si un écart."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parents[3]
spec = importlib.util.spec_from_file_location("calcul", ICI / "calcul-verdicts-b-beta-v1.py")
K = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K)

REF = RACINE / "docs/sources/neuron-lens-v1-devis-20261113/reference-publiee"
ATT = {"causal_lens_qwen3-8b.json": "8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3",
       "reads_at_firings_qwen3-8b.json": "ac0bf101e341385a400bbecb751f9720428da1d0bd09a752c8337dd84ba182cd"}
for f, h in ATT.items():
    assert hashlib.sha256((REF / f).read_bytes()).hexdigest() == h, f
cq = json.loads((REF / "causal_lens_qwen3-8b.json").read_text())
rq = json.loads((REF / "reads_at_firings_qwen3-8b.json").read_text())
T0, RS0, SI0 = K.depuis_reference(cq, rq)
R, M = K.NOTRE_R, K.MOITIES
STAB0 = {("R", "out"): [0.05] * 31, ("R", "mid"): [0.05] * 32, ("S", "mid"): [0.05] * 32, ("S", "out"): [0.05] * 32}
ACC0 = {l: 0.90 for l in K.COUCHES_ACCORD}
GM0 = {k: False for k in "dfghiknopqrs"}
N64 = {c: [64] * 32 for c in K.CIBLES}
ECN0 = [0] * 32
ecarts = []


def base():
    return {"score": copy.deepcopy(T0), "n": copy.deepcopy(N64), "ecartes_nul": list(ECN0),
            "repere": list(T0["steer 1x"]["npR"]["r_med"]), "stab": copy.deepcopy(STAB0), "accord": dict(ACC0),
            "read_S": list(RS0), "silent": list(SI0), "gardes_machine": dict(GM0)}


def verif(nom, cond, res):
    print(f"[{'ok' if cond else 'ÉCART'}] {nom} : verdict « {res['verdict']} », mesures {res['mesures']}, défauts {res['defauts']}, "
          f"déclencheurs {[a for a, v in res['declencheurs'].items() if v]}, issues {res['issues_audits']}, réserves {res['reserves']}")
    if not cond:
        ecarts.append(nom)


SAIN_A = {"temoin_distinct": True, "normes_non_nulles": True}
# (i) référence
e = base(); r = K.verdict(e)
d5 = r["details"]["B-5"]
v5 = all(abs(a - b) <= 1e-4 for a, b in ((d5["read_S_0"], 0.8481), (d5["moyenne_1_7"], 0.2248), (d5["moyenne_12_23"], 0.0271),
                                        (d5["ecart"], 0.1977)))
print("valeurs de B-5 sur la référence :", d5)
verif("(i) référence", r["verdict"] == "reproduit avec nos lentilles" and all(r["mesures"][k] == "reproduit" for k in ("B-1", "B-2", "B-3", "B-5", "B-7"))
      and r["mesures"]["B-6"] == "accord" and not r["defauts"] and not any(r["declencheurs"].values()) and v5
      and round(d5["silent_0"], 3) == 0.000 and round(d5["silent_moyen_1_7"], 3) == 0.240, r)  # repères du texte à 3 décimales (première version : 1e-12, trop strict, corrigé avant scellement)
# (ii-a)
e = base(); e["score"]["steer 1x"][R]["pass"][16:28] = [0.40] * 12; r = K.verdict(e)
verif("(ii-a)", r["mesures"]["B-2"] == "non reproduit" and r["mesures"]["B-3"] == "reproduit" and r["mesures"]["B-7"] == "reproduit"
      and r["verdict"] == "non reproduit avec nos lentilles" and "défaut dans notre lentille" in r["reserves"], r)
# (ii-b)
e = base(); e["score"]["steer 1x"][R]["control_med"][10] = 0.20; r = K.verdict(e)
verif("(ii-b)", r["verdict"] == "chaîne en défaut" and any(d.startswith("(a)") for d in r["defauts"]), r)
# (ii-c)
e = base()
for c in K.CIBLES:
    e["score"][c][R]["r_med"] = list(e["score"][c]["logit"]["r_med"])
r = K.verdict(e)
verif("(ii-c)", r["verdict"] == "chaîne en défaut" and any(d.startswith("(e)") for d in r["defauts"]), r)
# (iii-a)
e = base(); e["read_S"][0] = 0.25; r = K.verdict(e)
verif("(iii-a)", r["mesures"]["B-5"] == "non reproduit" and r["verdict"] == "partiel", r)
# (iii-b)
e = base()
for l in list(range(1, 8)) + list(range(12, 24)):
    e["read_S"][l] = 0.1
r = K.verdict(e)
verif("(iii-b)", r["mesures"]["B-5"] == "non reproduit" and r["verdict"] == "partiel", r)
# (iii-c)
e = base(); e["silent"][0] = 0.45; r = K.verdict(e)
verif("(iii-c)", r["mesures"]["B-5"] == "non lisible" and r["verdict"] == "partiel", r)
# (iii-d)
e = base(); e["read_S"][0] = 1.00
r1 = K.verdict(e, audits={"A4": {"permutation_ok": True, "lentille_S_ok": True}})
r2 = K.verdict(e, audits={"A4": {"permutation_ok": False, "lentille_S_ok": True}})
verif("(iii-d) permutation saine", r1["declencheurs"]["A4"] and r1["mesures"]["B-5"] == "reproduit" and r1["verdict"] == "reproduit avec nos lentilles", r1)
verif("(iii-d) permutation identité", r2["verdict"] == "chaîne en défaut" and any(d.startswith("(m)") for d in r2["defauts"]), r2)
# (iii-e)
e = base(); e["read_S"] = [0.0] * 32
r1 = K.verdict(e, audits={"A4": {"permutation_ok": True, "lentille_S_ok": True}})
r2 = K.verdict(e, audits={"A4": {"permutation_ok": False, "lentille_S_ok": True}})
verif("(iii-e) permutation saine", r1["declencheurs"]["A4"] and r1["mesures"]["B-5"] == "non reproduit", r1)
verif("(iii-e) permutation identité", r2["verdict"] == "chaîne en défaut", r2)
# (iv-a)
e = base(); e["score"]["steer 1x"][R]["r_med"][10] = round(e["score"]["steer 1x"]["npR"]["r_med"][10] + 0.20, 4)
for m in M:
    e["score"]["steer 1x"][m]["r_med"] = [round(x - 0.02, 4) for x in e["score"]["steer 1x"][R]["r_med"]]
r1 = K.verdict(e)
e2 = copy.deepcopy(e); e2["score"]["steer 1x"][M[0]]["r_med"][10] = round(e["score"]["steer 1x"][R]["r_med"][10] - 0.10, 4)
r2 = K.verdict(e2)
verif("(iv-a) écart de corpus", r1["mesures"]["B-6"] == "désaccord" and r1["declencheurs"]["A6"] and "écart de corpus" in r1["reserves"]
      and r1["verdict"] == "reproduit avec nos lentilles", r1)
verif("(iv-a) écart d'ajustement", "écart d'ajustement" in r2["reserves"] and r2["verdict"] == "reproduit avec nos lentilles", r2)
# (v)
e = base(); e["score"]["steer 1x"][R]["r_med"][3] = 0.96
g1 = {"score": copy.deepcopy(e["score"]), "n": copy.deepcopy(N64)}
r1 = K.verdict(e, audits={"A1": dict(SAIN_A, **g1)})
g1b = copy.deepcopy(g1); g1b["score"]["steer 1x"][R]["pass"][16:28] = [0.40] * 12
r2 = K.verdict(e, audits={"A1": dict(SAIN_A, **g1b)})
r3 = K.verdict(e, audits={"A1": dict(SAIN_A, temoin_distinct=False, **g1)})
r4 = K.verdict(e, audits={"A1": "non joué"})
verif("(v) seconde graine qui garde", r1["declencheurs"]["A1"] and r1["verdict"] == "reproduit avec nos lentilles", r1)
verif("(v) seconde graine qui change B-2", r2["mesures"]["B-2"] == "autre", r2)
verif("(v) témoin égal au pôle", r3["verdict"] == "chaîne en défaut" and any(d.startswith("(l)") for d in r3["defauts"]), r3)
verif("(v) audit non joué", r4["verdict"] == "non conclu", r4)
# (vi-a) à (vi-e)
e = base(); r = K.verdict(e); verif("(vi-a)", r["mesures"]["B-1"] == "reproduit", r)
e = base(); e["stab"][("R", "out")][5] = 0.25
r1 = K.verdict(e, audits={"A3": {"controles_ok": True}}); r2 = K.verdict(e, audits={"A3": {"controles_ok": False}})
verif("(vi-b) sain", r1["mesures"]["B-1"] == "non reproduit" and r1["declencheurs"]["A3"] and r1["verdict"] == "partiel", r1)
verif("(vi-b) 465 et 467", r2["verdict"] == "chaîne en défaut" and any(d.startswith("(g)") for d in r2["defauts"]), r2)
e = base(); e["accord"][12] = 0.50; r = K.verdict(e, audits={"A3": {"controles_ok": True}})
verif("(vi-c)", r["mesures"]["B-1"] == "non reproduit" and r["declencheurs"]["A3"] and r["verdict"] == "partiel", r)
e = base(); e["stab"][("S", "mid")][3] = 0.0
r1 = K.verdict(e, audits={"A2": {"controles_ok": False}})
verif("(vi-d)", r1["declencheurs"]["A2"] and r1["verdict"] == "chaîne en défaut", r1)
e = base(); e["accord"] = {l: 1.0 for l in K.COUCHES_ACCORD}
r1 = K.verdict(e, audits={"A2": {"controles_ok": True}})
verif("(vi-e)", r1["declencheurs"]["A2"] and r1["mesures"]["B-1"] == "reproduit", r1)
# (vii)
e = base()
for l in (1, 2, 3):
    e["score"]["steer 1x"]["npR"]["r_med"][l] = round(e["repere"][l] + 0.06, 4)
r = K.verdict(e)
verif("(vii)", r["verdict"] == "chaîne en défaut" and any(d.startswith("(j)") for d in r["defauts"]), r)
# (x)
e = base(); e["score"]["ablate win"][R]["r_med"][8:14] = [0.45] * 6
g1 = {"score": copy.deepcopy(e["score"]), "n": copy.deepcopy(N64)}
r1 = K.verdict(e, audits={"A5": dict(SAIN_A, **g1)})
g1b = {"score": copy.deepcopy(T0), "n": copy.deepcopy(N64)}
r2 = K.verdict(e, audits={"A5": dict(SAIN_A, **g1b)})
verif("(x) confirmé", r1["declencheurs"]["A5"] and r1["mesures"]["B-7"] == "non reproduit" and r1["details"]["B-7"]["par_le_haut"]
      and r1["verdict"] == "reproduit avec nos lentilles", r1)
verif("(x) non confirmé", r2["mesures"]["B-7"] == "autre" and r2["verdict"] == "reproduit avec nos lentilles", r2)
# (xi)
e = base(); e["score"]["steer 1x"][R]["pass"][16:28] = [0.40] * 12
for l in range(4, 16):
    e["score"]["steer 1x"][R]["r_med"][l] = round(e["score"]["steer 1x"]["logit"]["r_med"][l] - 0.01, 4)
r = K.verdict(e)
verif("(xi)", r["mesures"]["B-2"] == "non reproduit" and r["mesures"]["B-3"] == "non reproduit"
      and r["verdict"] == "non reproduit avec nos lentilles" and "défaut dans notre lentille" in r["reserves"], r)
# rangs 2 et 3
e = base(); e["score"]["steer 1x"][R]["pass"][16:28] = [0.40] * 12; e["stab"][("R", "out")][5] = 0.25
r = K.verdict(e, audits={"A3": "non joué"})
verif("rangs 2 et 3", r["verdict"] == "non conclu", r)
# artefact de A1
e = base(); e["score"]["steer 1x"][R]["control_med"][2] = 0.0; e["score"]["steer 1x"][R]["control_med"][5] = -0.0
r = K.declencheurs(e["score"], e["n"], e["stab"], e["accord"], e["read_S"], K.LECTURE_EN_VIGUEUR)
e1 = base(); e1["score"]["steer 1x"][R]["control_med"][2] = 0.0
r1 = K.declencheurs(e1["score"], e1["n"], e1["stab"], e1["accord"], e1["read_S"], K.LECTURE_EN_VIGUEUR)
e2 = base(); e2["score"]["ablate pos"]["J"]["control_med"][2] = 0.0; e2["score"]["ablate pos"]["J"]["control_med"][5] = 0.0
r2 = K.declencheurs(e2["score"], e2["n"], e2["stab"], e2["accord"], e2["read_S"], K.LECTURE_EN_VIGUEUR)
print("artefact A1 :", r["A1"], r1["A1"], r2["A1"])
if not (r["A1"] and not r1["A1"] and not r2["A1"]):
    ecarts.append("artefact A1")
# cas faits à la main : bande partielle (T-1, O-1) et garde (b)
e = base(); e["n"]["steer 1x"][16:20] = [40] * 4; e["ecartes_nul"][16:20] = [24] * 4
e["score"]["steer 1x"][R]["pass"][16:28] = [0.40] * 12
r_add = K.verdict(e); r_let = K.verdict(e, {"non_sur_partielle": "lettre"})
verif("main : bande 16-27 partielle, addendum → B-2 autre", r_add["mesures"]["B-2"] == "autre" and r_add["verdict"] == "partiel", r_add)
verif("main : même cas, lettre → B-2 non reproduit", r_let["mesures"]["B-2"] == "non reproduit", r_let)
e = base(); e["ecartes_nul"][7] = 33; e["n"]["steer 1x"][7] = 31
r = K.verdict(e); verif("main : garde (b)", r["verdict"] == "chaîne en défaut" and any(d.startswith("(b)") for d in r["defauts"]), r)
e = base(); e["gardes_machine"]["k"] = None; r = K.verdict(e)
verif("main : garde inconnue rapportée, non défaut", r["verdict"] == "reproduit avec nos lentilles" and "k" in r["gardes_inconnues"], r)
print("ÉCARTS :", ecarts if ecarts else "aucun")
sys.exit(1 if ecarts else 0)
