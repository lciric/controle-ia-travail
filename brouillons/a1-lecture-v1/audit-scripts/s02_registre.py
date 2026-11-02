"""Registre de dépense cumulée de la course : appels par fournisseur, statuts, codes, heures (lecture seule)."""
import json, collections
E = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/entree/sortie/registre-depense-cumulee-v1.jsonl"
L = [json.loads(l) for l in open(E, encoding="utf-8")]
print("lignes", len(L), "types", collections.Counter(x["type"] for x in L))
print("clés debut", sorted({k for x in L if x["type"] == "debut" for k in x}))
print("clés fin", sorted({k for x in L if x["type"] == "fin" for k in x}))
debuts = {x["id"]: x for x in L if x["type"] == "debut"}
fins = {x["id"]: x for x in L if x["type"] == "fin"}
print("débuts", len(debuts), "fins", len(fins), "débuts sans fin", len(set(debuts) - set(fins)), "fins sans début", len(set(fins) - set(debuts)))
autres = [x for x in L if x["type"] not in ("debut", "fin")]
print("autres types", autres[:5])
par = collections.defaultdict(list)
for i, d in debuts.items():
    f = fins.get(i)
    par[d["fournisseur"]].append((d["quand_utc"], f["quand_utc"] if f else None, f["statut"] if f else None, f["code"] if f else None,
                                  f["cout_usd"] if f else None, f.get("cout_origine") if f else None, d["modele"], i))
for fo, v in sorted(par.items()):
    v.sort()
    c = collections.Counter((s, k, o) for _, _, s, k, _, o, _, _ in v)
    print("==", fo, "appels", len(v), "par (statut, code, origine du coût)", dict(c))
    print("   coût total", round(sum(x[4] or 0 for x in v), 6), "premier début", v[0][0], "dernier début", v[-1][0], "dernière fin", max(x[1] or "" for x in v))
    print("   modèles demandés au registre", collections.Counter(x[6] for x in v))
    if fo == "kimi":
        for x in v:
            if x[2] != "echec" or x[3] != 3:
                print("   ", x[:6])
        e3 = [x for x in v if x[2] == "echec" and x[3] == 3]
        print("   échecs code 3 :", len(e3), "de", e3[0][0], "à", e3[-1][1])
        fen = [x for x in v if "2026-11-02T10:39:15" <= x[0] <= "2026-11-02T10:40:44.999"]
        print("   appels Kimi commencés entre 10:39:15 et 10:40:44 :", len(fen), collections.Counter((x[2], x[3]) for x in fen))
        apres = [x for x in v if x[0] >= "2026-11-02T12:23:14"]
        print("   appels Kimi commencés à partir de 12:23:14 :", len(apres))
    if fo == "argon":
        nonok = [x for x in v if x[2] != "ok"]
        print("   non ok :", nonok)
        print("   derniers appels :", v[-3:])
