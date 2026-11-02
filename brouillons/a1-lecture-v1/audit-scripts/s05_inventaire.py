"""Inventaire par (monde, fournisseur, suite, carte) : tentatives et statut de chacune, heures (registre apparié par
s04_appariement.py). Écrit travail/inventaire-v1.json et imprime un résumé. Lecture seule de la sortie."""
import json, csv, collections
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
heures = {}
for fo in ("kimi", "argon"):
    for x in csv.DictReader(open(B + f"travail/appariement-{fo}-v1.csv", encoding="utf-8")):
        cle = (x["monde"], fo, int(x["carte"]), x["condition"], x["juge"], int(x["k"]))
        heures.setdefault(cle, []).append((int(x["essai"]), x["debut_registre"], x["fin_registre"], x["code_registre"], x["statut_sortie"]))
def statut(t):
    m = t["motif_invalidite"]
    if t["loi"] is None:
        if m == "appel échoué après une reprise":
            return "echouee"
        if m and m.startswith("appel refusé : budget"):
            return "budget"
        return "invalide"
    v = t["verdict"]
    return {"promue": "promue", "non_promue": "non_promue", "evaluation_impossible": "evaluation_impossible"}[v["statut"]]
inv = []
for s in R["suites"]:
    st = [statut(t) for t in s["tentatives"]]
    ks = [t["k"] for t in s["tentatives"]]
    assert ks == list(range(1, len(ks) + 1)), ks
    pp = s["premiere_promotion"]
    assert (pp is None and "promue" not in st) or (pp is not None and st.index("promue") + 1 == pp and len(st) == pp), (s["monde"], s["carte"], st, pp)
    assert pp is not None or len(st) == 16
    h = [heures.get((s["monde"], s["fournisseur"], s["carte"], s["condition"], s["juge"], k), []) for k in ks]
    debut = min((e[1] for x in h for e in x if e[1]), default="")
    fin = max((e[2] for x in h for e in x if e[2]), default="")
    inv.append({"monde": s["monde"], "fournisseur": s["fournisseur"], "suite": f"{s['condition']}|{s['juge']}", "carte": s["carte"],
                "tentatives": len(st), "statuts": st, "premiere_promotion": pp, "non_jouees_apres_promotion": 16 - len(st),
                "debut_registre": debut, "fin_registre": fin,
                "appels_hors_registre": sum(1 for x in h for e in x if not e[1]) if s["fournisseur"] == "kimi" else 0})
json.dump(inv, open(B + "travail/inventaire-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
agg = collections.defaultdict(collections.Counter)
for u in inv:
    agg[(u["monde"], u["fournisseur"], u["suite"])].update(u["statuts"])
    agg[(u["monde"], u["fournisseur"], u["suite"])]["non_jouee_apres_promotion"] += u["non_jouees_apres_promotion"]
    agg[(u["monde"], u["fournisseur"], u["suite"])]["suites_promues"] += u["premiere_promotion"] is not None
for k in sorted(agg):
    print(k, dict(agg[k]))
tot = collections.Counter(x for u in inv for x in u["statuts"])
print("total tentatives", sum(tot.values()), dict(tot))
print("par fournisseur", {f: dict(collections.Counter(x for u in inv if u["fournisseur"] == f for x in u["statuts"])) for f in ("kimi", "argon")})
