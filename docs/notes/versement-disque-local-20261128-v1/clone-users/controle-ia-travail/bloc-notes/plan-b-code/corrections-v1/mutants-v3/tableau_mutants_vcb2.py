"""Tableau des mutants rejoués (corrections VCB2), lu dans `resultats-w0.jsonl` et `resultats-w1.jsonl`, dans l'ordre de
`liste_mutants_vcb2.MUTANTS`. Usage : python3 -I tableau_mutants_vcb2.py > tableau-mutants-vcb2.md"""
import json
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from liste_mutants_vcb2 import MUTANTS  # noqa: E402

res = {}
for f in ("resultats-w0.jsonl", "resultats-w1.jsonl"):
    for ligne in (ICI / f).read_text(encoding="utf-8").splitlines():
        r = json.loads(ligne)
        assert r["id"] not in res, r["id"]
        res[r["id"]] = r
ids = [m[0] for m in MUTANTS]
assert sorted(res) == sorted(ids), (sorted(set(ids) - set(res)), sorted(set(res) - set(ids)))
print("| mutant | ce qu'il simule | résultat | premier échec | fin |")
print("|---|---|---|---|---|")
comptes = {}
for i in ids:
    r = res[i]
    comptes[r["statut"]] = comptes.get(r["statut"], 0) + 1
    echec = (r.get("premier_echec") or [""])[0].replace("FAILED ", "").split(" - ")[0]
    echec = echec.encode("ascii", "backslashreplace").decode("unicode_escape")      # « \xe9 » de pytest : « é »
    print(f"| {i} | {r['quoi']} | {r['statut']} | `{echec}` | {r.get('fin', '')} |" if echec else
          f"| {i} | {r['quoi']} | {r['statut']} | — | {r.get('fin', '')} |")
print()
print("Bilan :", ", ".join(f"{v} {k}" for k, v in sorted(comptes.items())), f"(sur {len(ids)})")
