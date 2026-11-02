"""v01 — structure de la sortie scellée et bloc `lecture` tel qu'écrit par le code (lecteur du verdict, R13).
Usage : python3 -I -B v01_structure.py SORTIE.json MANIFESTE.json"""
import json
import sys

sortie = json.load(open(sys.argv[1], encoding="utf-8"))
manif = json.load(open(sys.argv[2], encoding="utf-8"))

print("clés de la sortie :", sorted(sortie))
for k, v in sortie.items():
    if isinstance(v, (list, dict)):
        print(f"  {k}: {type(v).__name__} de longueur {len(v)}")
    else:
        print(f"  {k}: {v!r}")

print("\nclés du manifeste :", sorted(manif))
print("manifeste.reglages clés :", sorted(manif.get("reglages", {})))
print("manifeste.reglages.depot :", manif.get("reglages", {}).get("depot"))

lec = sortie["lecture"]
print("\nlecture.issues :", lec["issues"])
for w, m in lec["mondes"].items():
    print(f"\n=== {w}")
    for k in ("issue", "issue_suspendue_par_audit", "breche", "dents", "resiste", "eps_resistance",
              "qualification_breche", "evaluations_impossibles", "appels_budget_depasse", "predictions"):
        print(f"  {k}: {m[k]!r}")
    print("  instrument_v8_retour:", m["instrument_v8_retour"])
    print("  audits:")
    for a in m["audits"]:
        print("    -", a)
    for cle in ("v8|retour|n=16|ensemble", "v7|retour|n=16|ensemble", "v8|temoin|n=16|ensemble",
                "v7|temoin|n=1|ensemble", "v8|temoin|n=1|ensemble", "v8|retour|n=1|ensemble",
                "v8|temoin|n=4|ensemble", "v8|retour|n=4|ensemble", "v7|retour|n=1|ensemble"):
        print(f"  taux[{cle}] = {m['taux'][cle]}")
    print("  ecarts_goodhart_par_carte:")
    for k, v in m["ecarts_goodhart_par_carte"].items():
        print(f"    {k}: {v}")
    print("  ecart_par_loi_H3:", m["ecart_par_loi_H3"])
