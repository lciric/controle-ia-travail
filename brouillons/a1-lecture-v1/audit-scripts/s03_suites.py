"""Inventaire des suites de la sortie scellée : tentatives, statuts, appels (lecture seule)."""
import json, collections
E = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/entree/sortie/attaque-goodhart-v2.json"
R = json.load(open(E, encoding="utf-8"))
S = R["suites"]
print("suites", len(S), "clés de suite", sorted({k for s in S for k in s}))
print("clés de tentative", sorted({k for s in S for t in s["tentatives"] for k in t}))
print("clés d'appel", sorted({k for s in S for t in s["tentatives"] for a in t["appels"] for k in a}))
print("clés de verdict", sorted({k for s in S for t in s["tentatives"] if t["verdict"] for k in t["verdict"]}))
print("interrompues", sum(1 for s in S if s.get("interrompue")))
cnt = collections.Counter((s["monde"], s["fournisseur"], s["condition"], s["juge"]) for s in S)
print("suites par (monde, fournisseur, condition, juge) :", dict(cnt))
appels = collections.Counter()
for s in S:
    for t in s["tentatives"]:
        for a in t["appels"]:
            appels[(s["fournisseur"], a["statut"])] += 1
print("appels par (fournisseur, statut) dans les suites :", dict(appels), "total", sum(appels.values()))
print("reprises (sortie) :", R["reprises"], "appels (sortie) :", R["appels"])
rep = sum(1 for s in S for t in s["tentatives"] if len(t["appels"]) == 2)
print("tentatives à deux appels :", rep)
print("coût par fournisseur dans les suites :", {f: round(sum(a["cout_usd"] for s in S if s["fournisseur"] == f for t in s["tentatives"] for a in t["appels"]), 6) for f in ("kimi", "argon")})
print("depense_par_fournisseur_usd :", R["depense_par_fournisseur_usd"], "depense_usd", R["depense_usd"])
print("modeles_servis :", R["modeles_servis"], "appels_budget_depasse", R["appels_budget_depasse"])
ms = collections.Counter((s["fournisseur"], a["modele_servi"]) for s in S for t in s["tentatives"] for a in t["appels"])
print("modèle servi par appel :", dict(ms))
mi = collections.Counter(t["motif_invalidite"][:60] if t["motif_invalidite"] else None for s in S for t in s["tentatives"])
print("motifs :", dict(mi))
