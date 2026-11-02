"""Écarts (a) et (b) : tentatives, suites et unités Kimi par fenêtre d'heures (appariement s04 : ordre de jeu du fil Kimi ↔
registre), et total cumulé du registre avant chaque appel Kimi (pour l'hypothèse d'un refus par plafond d'étape).
Lecture seule ; écrit travail/ecarts-ab-v1.json."""
import csv, json, collections
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
rows = list(csv.DictReader(open(B + "travail/appariement-kimi-v1.csv", encoding="utf-8")))
inv = json.load(open(B + "travail/inventaire-v1.json", encoding="utf-8"))
st = {(u["monde"], u["fournisseur"], u["suite"], u["carte"]): u["statuts"] for u in inv}
def statut(r):
    return st[(r["monde"], "kimi", f"{r['condition']}|{r['juge']}", int(r["carte"]))][int(r["k"]) - 1]
# fenêtre (a) : appels enregistrés commencés ou finis dans [10:39:15, 10:40:44[
A0, A1 = "2026-11-02T10:39:15", "2026-11-02T10:40:44"
tent = collections.OrderedDict()
for r in rows:
    if r["debut_registre"] and ((A0 <= r["debut_registre"] < A1) or (A0 <= r["fin_registre"] < A1)):
        tent.setdefault((r["monde"], r["carte"], r["condition"] + "|" + r["juge"], int(r["k"])), []).append((r["essai"], r["debut_registre"][11:23], r["fin_registre"][11:23], r["code_registre"], r["origine"]))
par_suite = collections.OrderedDict()
for (w, c, s, k), a in tent.items():
    par_suite.setdefault((w, c, s), []).append(k)
print("(a) tentatives Kimi touchées par la fenêtre :", len(tent), "| statuts :", collections.Counter(statut({"monde": w, "carte": c, "condition": s.split("|")[0], "juge": s.split("|")[1], "k": k}) for (w, c, s, k) in tent))
for (w, c, s), ks in par_suite.items():
    print("    ", w, "carte", c, s, "k", f"{min(ks)}–{max(ks)}" if len(ks) > 1 else ks[0], f"({len(ks)} tentatives)")
prem = next(iter(tent.items())); dern = next(reversed(tent.items()))
print("    première :", prem, "\n     dernière :", dern)
# tentative du premier appel après la fenêtre
apres = [r for r in rows if r["debut_registre"] >= A1][:1] + [r for r in rows if r["debut_registre"] and A0 <= r["debut_registre"] < A1 and r["statut_sortie"] == "ok"]
print("    appel réussi qui suit (ou chevauche la fin de) la fenêtre :", [(r["rang"], r["monde"], r["carte"], r["condition"], r["juge"], r["k"], r["essai"], r["debut_registre"], r["fin_registre"], r["statut_sortie"]) for r in apres])
# (b) appels joués au-delà du registre
hors = [r for r in rows if not r["debut_registre"]]
print("(b) appels Kimi joués sans ligne au registre :", len(hors), "| du rang", hors[0]["rang"], "au rang", hors[-1]["rang"], "| coûts :", collections.Counter(r["cout_sortie"] for r in hors))
th = collections.OrderedDict()
for r in hors:
    th.setdefault((r["monde"], r["carte"], r["condition"] + "|" + r["juge"]), set()).add(int(r["k"]))
print("    tentatives :", sum(len(v) for v in th.values()), "| suites touchées :", len(th))
print("    première suite :", next(iter(th.items())), "| suites entières (16 tentatives) :", sum(1 for v in th.values() if len(v) == 16))
unites = collections.defaultdict(set)
for (w, c, s) in th:
    unites[(w, c)].add(s)
print("    unités Kimi touchées :", {f"{w} c{c}": len(v) for (w, c), v in sorted(unites.items())})
dernier = [r for r in rows if r["debut_registre"]][-1]
print("    dernier appel Kimi au registre :", dernier["rang"], dernier["monde"], dernier["carte"], dernier["condition"], dernier["juge"], "k", dernier["k"], "essai", dernier["essai"], dernier["debut_registre"], "→", dernier["fin_registre"], "code", dernier["code_registre"])
# total cumulé du registre (les deux fournisseurs, même étape) avant chaque début d'appel Kimi, plus le pire cas de l'appel
L = [json.loads(l) for l in open(B + "entree/sortie/registre-depense-cumulee-v1.jsonl", encoding="utf-8")]
ev = sorted([(x["quand_utc"], x) for x in L], key=lambda z: z[0])
total, par_f, id_f, lignes = 0.0, collections.Counter(), {}, []
for q, x in ev:
    if x["type"] == "debut":
        id_f[x["id"]] = x["fournisseur"]
        if x["fournisseur"] == "kimi":
            lignes.append((q[11:23], round(total, 6), round(par_f["kimi"], 6), x["pire_cas_usd"], round(total + x["pire_cas_usd"], 6), x["plafond_etape_usd"]))
    else:
        total += x["cout_usd"]; par_f[id_f[x["id"]]] += x["cout_usd"]
print("total du registre à la fin :", round(total, 6), dict((k, round(v, 6)) for k, v in par_f.items()))
print("débuts Kimi (heure, total registre avant, part Kimi avant, pire cas, total + pire cas, plafond d'étape inscrit) — hors fenêtre (a) :")
for l in lignes:
    if not (A0 <= "2026-11-02T" + l[0] < A1):
        print("    ", l)
print("pire cas Kimi : min", min(x["pire_cas_usd"] for x in L if x["type"] == "debut" and x["fournisseur"] == "kimi"), "max", max(x["pire_cas_usd"] for x in L if x["type"] == "debut" and x["fournisseur"] == "kimi"))
json.dump({"a_tentatives": [list(k) + [v] for k, v in tent.items()], "b_suites": {f"{w}|c{c}|{s}": sorted(v) for (w, c, s), v in th.items()}},
          open(B + "travail/ecarts-ab-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
