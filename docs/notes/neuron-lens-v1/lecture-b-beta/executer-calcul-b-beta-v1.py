"""Exécution du calcul du lecteur neuf sur les pièces versées de la course `20261118-164930-neuron-lens-b-beta` (plan de lecture v2).

Usage : `python -I executer-calcul-b-beta-v1.py ETAPE SORTIE.json [COMPLEMENT.json]`
- ETAPE = `B` : sorties brutes seules (catégorie 1 du plan, 2.1) ; aucune pièce de catégorie 2 n'est lue.
- ETAPE = `B4` ou `D` : idem, plus le fichier COMPLEMENT (écrit à la main par le lecteur, scellé) qui porte les grandeurs lues sur les
  pièces de catégorie 2 : `stab` (différences entre moitiés non arrondies), et, à l'étape D, `gardes_machine` et `audits`.
N'importe que `calcul-verdicts-b-beta-v1.py` (le script du lecteur) et la bibliothèque standard.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parents[3]
spec = importlib.util.spec_from_file_location("calcul", ICI / "calcul-verdicts-b-beta-v1.py")
K = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K)
DIAG = RACINE / "diag/20261118-164930-neuron-lens-b-beta"
REPERE = RACINE / "diag/20261117-015632-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json"
REPERE_SHA = "bd57d519a24e5227df2c2d720ba33a54f47653d0741acbb51f1781b59df33073"


def lire(p):
    return json.loads(pathlib.Path(p).read_text())


def entrees(complement):
    assert hashlib.sha256(REPERE.read_bytes()).hexdigest() == REPERE_SHA
    sc = lire(DIAG / "causal_lens_b-beta_llama-3.1-8b-instruct.json")
    gp = lire(DIAG / "grandeurs-par-pole-b-beta-v1.json")
    lc = lire(DIAG / "lens_compare-b-beta-v1.json")
    rd = lire(DIAG / "reads_at_firings_llama-3.1-8b-instruct.json")
    rep = lire(REPERE)
    t = {c: {le: {k: sc["targets"][c][le][k] for k in ("layer", "r_med", "pass", "control_med")} for le in sc["targets"][c]}
         for c in K.CIBLES}
    forme = []
    for c in K.CIBLES:
        for le, s in t[c].items():
            if s["layer"] != list(range(32)):
                forme.append(f"couches : {c}, {le}")
            for k in ("r_med", "pass", "control_med"):
                if len(s[k]) != 32 or any(round(x, 4) != x for x in s[k]):
                    forme.append(f"valeur non écrite à 4 décimales ou longueur : {c}, {le}, {k}")
    n = {c: gp["n"][c] for c in K.CIBLES}
    ecn = gp["ecartes"]["steer 1x"]["effet nul"]
    acc = {l: lc["layers"][str(l)]["R:dclm-llama-even vs R:dclm-llama-odd"]["top1_agree"] for l in K.COUCHES_ACCORD}
    Ls = rd["neurons"]["layers"]
    assert [x["layer"] for x in Ls] == list(range(32))
    e = {"score": t, "n": n, "ecartes_nul": ecn, "repere": rep["targets"]["steer 1x"]["npR"]["r_med"][:32],
         "stab": None, "accord": acc, "read_S": [x["read_S"] for x in Ls], "silent": [x["silent"] for x in Ls],
         "gardes_machine": {}}
    if complement:
        if "stab" in complement:
            e["stab"] = {tuple(k.split("|")): v for k, v in complement["stab"].items()}
        e["gardes_machine"] = complement.get("gardes_machine", {})
    brut = {"meta_score": sc["meta"], "lentilles_score": sc["lenses"], "forme": forme,
            "n": n, "ecartes": gp["ecartes"], "accord_moities": acc,
            "accord_moities_npR": {l: {k: lc["layers"][str(l)][k]["top1_agree"] for k in lc["layers"][str(l)]} for l in K.COUCHES_ACCORD},
            "recouvrement_dix": {l: {k: lc["layers"][str(l)][k]["top10_overlap"] for k in lc["layers"][str(l)]} for l in K.COUCHES_ACCORD},
            "lignes_lens_compare": {l: {k: lc["layers"][str(l)][k]["rows"] for k in lc["layers"][str(l)]} for l in K.COUCHES_ACCORD},
            "reads": [{k: x[k] for k in ("layer", "read_S", "silent", "read_S_net")} for x in Ls],
            "table_grandeurs_egale_score": all(gp["table"][c][le][k] == sc["targets"][c][le][k] for c in K.CIBLES
                                               for le in sc["targets"][c] for k in ("r_med", "pass", "control_med"))}
    return e, brut


VARIANTES = {"T-1 lettre": {"non_sur_partielle": "lettre"}, "T-2 toutes": {"temoin": "toutes"}, "T-3 sans moitiés": {"a_moities": False},
             "T-4 flottant brut": {"arrondi": False}, "T-5 flottant binaire": {"b5_valeurs": "flottant"},
             "O-1 possible": {"reproduit_sur_partielle": "possible"}, "O-2 n": {"garde_b": "n"},
             "O-4 lisibles": {"lisible_gardes": True}, "O-5/O-6 ignore": {"audit_absent": "ignore"}, "O-9 moitiés": {"ce_moities": True}}


def resume(r):
    return {k: r[k] for k in ("verdict", "defauts", "gardes_inconnues", "reserves", "declencheurs", "issues_audits", "mesures")}


def main():
    etape, sortie = sys.argv[1], sys.argv[2]
    comp = lire(sys.argv[3]) if len(sys.argv) > 3 else None
    e, brut = entrees(comp)
    audits = (comp or {}).get("audits", {})
    base = K.verdict(e, audits=audits)
    out = {"etape": etape, "brut": brut, "en_vigueur": base, "variantes": {}}
    for nom, L in VARIANTES.items():
        r = K.verdict(e, L, audits=audits)
        out["variantes"][nom] = {"diffère": resume(r) != resume(base), **resume(r)}
    acc_tout_1 = all(e["accord"][l] == 1 for l in K.COUCHES_ACCORD)
    out["declencheur_A2_par_accord"] = acc_tout_1
    out["accord_sous_060"] = [l for l in K.COUCHES_ACCORD if e["accord"][l] < 0.60]
    out["accord_sous_080"] = [l for l in K.COUCHES_ACCORD if e["accord"][l] < 0.80]
    pathlib.Path(sortie).write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str))
    print(json.dumps(resume(base), ensure_ascii=False, default=str))
    for nom, v in out["variantes"].items():
        if v["diffère"]:
            print("VARIANTE QUI DIFFÈRE :", nom, json.dumps({k: v[k] for k in ("verdict", "mesures", "defauts", "declencheurs")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
