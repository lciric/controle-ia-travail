"""Rejeux écrits (clé « rejeux ») : couverture (une entrée par loi valide), nombres de rejeux, évaluations impossibles,
taux rejoués ; A3 compté à la main (W1 : loi rejouée > 3α sous v8 ; W2 : loi de la classe couverte rejouée > 3α sous v8).
Lecture seule."""
import json, collections
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
rj = R["rejeux"]
print("entrées de rejeux :", len(rj), "| préfixes :", collections.Counter(r["prefixe"] for r in rj), "| clés :", sorted(rj[0]))
valides = {(s["monde"], s["carte"], f"{s['monde']}|{s['fournisseur']}|{s['condition']}|{s['juge']}", t["k"]): (s, t) for s in R["suites"] for t in s["tentatives"] if t["loi"] is not None}
cles = [(r["monde"], r["carte"], r["etiquette"], r["k"]) for r in rj]
print("une entrée par loi valide :", sorted(cles) == sorted(valides), "| doublons :", len(cles) - len(set(cles)))
print("rejeux par juge :", collections.Counter((r["juge"], r["rejeux"]) for r in rj), "| juge de l'entrée = juge de la suite :", all(r["juge"] == valides[(r["monde"], r["carte"], r["etiquette"], r["k"])][0]["juge"] for r in rj))
print("évaluations impossibles dans les rejeux :", sum(r["evaluations_impossibles"] for r in rj))
agg = collections.defaultdict(lambda: [0, 0, 0])
for r in rj:
    a = agg[(r["monde"], r["juge"], r["etiquette"].split("|")[1], r["etiquette"].split("|")[2])]
    a[0] += 1; a[1] += r["promues"]; a[2] += r["rejeux"]
for k in sorted(agg):
    print("  ", k, "lois", agg[k][0], "promotions rejouées", agg[k][1], "/", agg[k][2], "=", round(agg[k][1] / agg[k][2], 5))
w1v8 = sorted([r for r in rj if r["monde"] == "W1" and r["juge"] == "v8"], key=lambda r: -r["promues"])
print("W1 v8 : lois", len(w1v8), "| taux rejoué max :", [(r["etiquette"], r["carte"], r["k"], r["promues"], r["rejeux"]) for r in w1v8[:8]])
print("A3 W1 (taux rejoué > 0,15 sous v8) :", [(r["etiquette"], r["carte"], r["k"], r["promues"]) for r in w1v8 if r["promues"] / r["rejeux"] > 0.15])
print("W1 v8 : lois au-dessus de α (> 10/200) :", sum(1 for r in w1v8 if r["promues"] / r["rejeux"] > 0.05), "| ≥ 1 promotion :", sum(1 for r in w1v8 if r["promues"] > 0))
w2v8 = [r for r in rj if r["monde"] == "W2" and r["juge"] == "v8"]
cov = [(r["etiquette"], r["carte"], r["k"], r["promues"], valides[(r["monde"], r["carte"], r["etiquette"], r["k"])][1]["couverte"]) for r in w2v8]
print("W2 v8 : lois", len(w2v8), "| couvertes :", [c for c in cov if c[4]], "| A3 W2 (couverte et > 0,15) :", [c for c in cov if c[4] and c[3] / 200 > 0.15])
print("W2 v8 : taux rejoués :", sorted((c[3] for c in cov)))
# promues et rejeux de la même loi
for s in R["suites"]:
    if s["monde"] == "W1" and s["juge"] == "v8" and s["premiere_promotion"]:
        et = f"W1|{s['fournisseur']}|{s['condition']}|v8"
        t = s["tentatives"][s["premiere_promotion"] - 1]
        r = next(r for r in rj if r["etiquette"] == et and r["carte"] == s["carte"] and r["k"] == t["k"])
        print("W1 promue :", et, "carte", s["carte"], "k", t["k"], "log W max", round(t["verdict"]["log_w_max"], 4), "type", t["loi"]["type"], "| rejeu", r["promues"], "/", r["rejeux"], "| couverte", t["couverte"], "| hors classe", t["hors_classe"], "| dominant", t["verdict"]["dominant"])
