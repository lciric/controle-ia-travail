"""Appariement des appels Kimi de la sortie (ordre de jeu du fil Kimi, jouer_tout l. 958-966) avec le registre de dépense
(ordre chronologique) ; heures par tentative pour les appels enregistrés. Lecture seule ; écrit un CSV de travail."""
import json, collections, csv
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
L = [json.loads(l) for l in open(B + "entree/sortie/registre-depense-cumulee-v1.jsonl", encoding="utf-8")]
SUITES = (("temoin", "v8"), ("retour", "v8"), ("temoin", "v7"), ("retour", "v7"))
idx = {(s["monde"], s["fournisseur"], s["carte"], s["condition"], s["juge"]): s for s in R["suites"]}
fins = {x["id"]: x for x in L if x["type"] == "fin"}
for fo in ("kimi", "argon"):
    jeu = []  # ordre de jeu du fil du fournisseur
    for w in ("W1", "W2"):
        for c in range(12):
            for cond, j in SUITES:
                s = idx[(w, fo, c, cond, j)]
                for t in s["tentatives"]:
                    for a in t["appels"]:
                        jeu.append((w, c, cond, j, t["k"], a["essai_d_appel"], a["statut"], a["cout_usd"]))
    reg = sorted([(d["quand_utc"], fins[d["id"]]) for d in L if d["type"] == "debut" and d["fournisseur"] == fo], key=lambda x: x[0])
    print("==", fo, "appels joués", len(jeu), "appels au registre", len(reg))
    ok_jeu = ["ok" if x[6] == "ok" else "E" for x in jeu]
    ok_reg = ["ok" if f["statut"] == "ok" else "E" for _, f in reg]
    n = len(reg)
    print("   statuts concordants sur les", n, "premiers appels joués :", ok_jeu[:n] == ok_reg)
    print("   coûts concordants (à 1e-9) :", all(abs(jeu[i][7] - reg[i][1]["cout_usd"]) < 1e-9 for i in range(n)))
    diff = [i for i in range(n) if abs(jeu[i][7] - reg[i][1]["cout_usd"]) >= 1e-9 or ok_jeu[i] != ok_reg[i]]
    print("   premiers écarts :", diff[:10])
    print("   appels joués au-delà du registre :", len(jeu) - n, collections.Counter((x[6], x[7]) for x in jeu[n:]))
    with open(B + f"travail/appariement-{fo}-v1.csv", "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(["rang", "monde", "carte", "condition", "juge", "k", "essai", "statut_sortie", "cout_sortie", "debut_registre", "fin_registre", "statut_registre", "code_registre", "origine"])
        for i, x in enumerate(jeu):
            r = reg[i] if i < n else None
            wr.writerow([i + 1, *x[:5], x[5], x[6], x[7], r[0] if r else "", r[1]["quand_utc"] if r else "", r[1]["statut"] if r else "", r[1]["code"] if r else "", r[1]["cout_origine"] if r else ""])
