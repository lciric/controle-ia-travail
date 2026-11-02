"""Audit A1 (auditeur neuf, 2e) — section 2, inventaire par monde × fournisseur × suite × carte, heures par appariement
au registre de dépense (ordre de jeu du fil du fournisseur, jouer_tout l. 958-966 ; registre chronologique). Lecture seule ;
écrit travail/a02-inventaire-v1.json et travail/a02-appariement-<fournisseur>-v1.csv."""
import json, collections, csv
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
L = [json.loads(l) for l in open(B + "entree/sortie/registre-depense-cumulee-v1.jsonl", encoding="utf-8")]
SUITES = (("temoin", "v8"), ("retour", "v8"), ("temoin", "v7"), ("retour", "v7"))
idx = {(s["monde"], s["fournisseur"], s["carte"], s["condition"], s["juge"]): s for s in R["suites"]}
assert len(idx) == 192 == len(R["suites"])
fins = {x["id"]: x for x in L if x["type"] == "fin"}
debuts = [x for x in L if x["type"] == "debut"]
assert len(debuts) == len(fins) == 1148 and all(d["id"] in fins for d in debuts)

def statut(t):
    """Statut d'une tentative selon le code gelé (jouer_suite l. 530-546, appeler l. 508-510, juger l. 446-454)."""
    if t["loi"] is None:
        m = t["motif_invalidite"]
        if m == "appel échoué après une reprise":
            return "echouee"
        if m and m.startswith("appel refusé : budget"):
            return "refusee_budget"
        return "invalide"
    return {"promue": "promue", "non_promue": "non_promue", "evaluation_impossible": "evaluation_impossible"}[t["verdict"]["statut"]]

heures = {}
appariement = {}
for fo in ("kimi", "argon"):
    jeu = []
    for w in ("W1", "W2"):
        for c in range(12):
            for cond, j in SUITES:
                for t in idx[(w, fo, c, cond, j)]["tentatives"]:
                    for a in t["appels"]:
                        jeu.append((w, c, cond, j, t["k"], a["essai_d_appel"], a["statut"], a["cout_usd"], a["modele_servi"]))
    reg = sorted(((d["quand_utc"], fins[d["id"]], d) for d in debuts if d["fournisseur"] == fo), key=lambda x: x[0])
    n = len(reg)
    concord = [i for i in range(min(n, len(jeu))) if (jeu[i][6] == "ok") == (reg[i][1]["statut"] == "ok") and abs(jeu[i][7] - reg[i][1]["cout_usd"]) < 1e-9]
    appariement[fo] = {"appels_joues": len(jeu), "appels_au_registre": n, "apparies_concordants (statut et coût)": len(concord),
                       "premier_ecart": next((i for i in range(min(n, len(jeu))) if i not in set(concord)), None),
                       "appels_joues_hors_registre": len(jeu) - n,
                       "hors_registre_par (statut, coût)": {f"{a}|{b}": v for (a, b), v in collections.Counter((x[6], x[7]) for x in jeu[n:]).items()},
                       "dernier_appel_apparie": jeu[n - 1][:6] if n <= len(jeu) else None,
                       "heure_fin_dernier_appel_registre": reg[-1][1]["quand_utc"], "heure_debut_premier_appel_registre": reg[0][0],
                       "modeles_demandes_au_registre": dict(collections.Counter(x[2]["modele"] for x in reg)),
                       "codes_registre": {f"{a}|{b}|{c}": v for (a, b, c), v in collections.Counter((x[1]["statut"], x[1]["code"], x[1]["cout_origine"]) for x in reg).items()},
                       "cout_registre": round(sum(x[1]["cout_usd"] for x in reg), 6), "cout_sortie": round(sum(x[7] for x in jeu), 6)}
    with open(B + f"travail/a02-appariement-{fo}-v1.csv", "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(["rang", "monde", "carte", "condition", "juge", "k", "essai", "statut_sortie", "cout_sortie", "modele_servi_sortie", "debut_registre", "fin_registre", "statut_registre", "code_registre", "origine_cout"])
        for i, x in enumerate(jeu):
            r = reg[i] if i < n else None
            wr.writerow([i + 1, *x, r[0] if r else "", r[1]["quand_utc"] if r else "", r[1]["statut"] if r else "", r[1]["code"] if r else "", r[1]["cout_origine"] if r else ""])
            if r:
                heures.setdefault((x[0], fo, x[1], x[2], x[3], x[4]), []).append((r[0], r[1]["quand_utc"], r[1]["code"]))

inv = []
for s in R["suites"]:
    st = [statut(t) for t in s["tentatives"]]
    ks = [t["k"] for t in s["tentatives"]]
    assert ks == list(range(1, len(ks) + 1))
    pp = s["premiere_promotion"]
    assert (pp is None and "promue" not in st) or (pp is not None and st.index("promue") + 1 == pp == len(st))
    assert pp is not None or len(st) == 16, (s["monde"], s["carte"], len(st))
    h = [heures.get((s["monde"], s["fournisseur"], s["carte"], s["condition"], s["juge"], k), []) for k in ks]
    debut = min((e[0] for x in h for e in x), default=None)
    fin = max((e[1] for x in h for e in x), default=None)
    inv.append({"monde": s["monde"], "fournisseur": s["fournisseur"], "suite": f"{s['condition']}|{s['juge']}", "carte": s["carte"],
                "tentatives_jouees": len(st), "statuts": st, "premiere_promotion": pp, "non_jouees_apres_promotion": 16 - len(st),
                "appels": sum(len(t["appels"]) for t in s["tentatives"]), "appels_au_registre": sum(len(x) for x in h),
                "debut_registre": debut, "fin_registre": fin, "interrompue": bool(s.get("interrompue"))})

def agreger(cle):
    agg = collections.OrderedDict()
    for u in inv:
        k = cle(u)
        a = agg.setdefault(k, collections.Counter())
        a.update(u["statuts"])
        a["non_jouee_apres_promotion"] += u["non_jouees_apres_promotion"]
        a["suites"] += 1
        a["suites_promues"] += u["premiere_promotion"] is not None
        a["suites_sans_aucune_loi"] += all(x in ("echouee", "invalide", "refusee_budget") for x in u["statuts"])
    return {str(k): dict(v) for k, v in agg.items()}

res = {"appariement": appariement,
       "par_monde_fournisseur_suite": agreger(lambda u: (u["monde"], u["fournisseur"], u["suite"])),
       "par_fournisseur": agreger(lambda u: u["fournisseur"]),
       "total": agreger(lambda u: "ensemble"),
       "unites": inv}
json.dump(res, open(B + "travail/a02-inventaire-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(appariement, ensure_ascii=False, indent=1))
for k, v in res["par_monde_fournisseur_suite"].items():
    print(k, v)
print("par fournisseur", json.dumps(res["par_fournisseur"], ensure_ascii=False))
print("total", json.dumps(res["total"], ensure_ascii=False))
print("suites Kimi avec au moins une loi :")
for u in inv:
    if u["fournisseur"] == "kimi" and any(x not in ("echouee",) for x in u["statuts"]):
        print("  ", u["monde"], u["carte"], u["suite"], "".join({"echouee": "E", "promue": "P", "non_promue": "n", "invalide": "I", "evaluation_impossible": "X", "refusee_budget": "B"}[x] for x in u["statuts"]), u["debut_registre"], u["fin_registre"], "appels", u["appels"], "au registre", u["appels_au_registre"])
print("Kimi : dernière suite avec un appel au registre :", max((u for u in inv if u["fournisseur"] == "kimi" and u["appels_au_registre"]), key=lambda u: u["fin_registre"])["fin_registre"])
print("Argon : première et dernière heure au registre :", min(u["debut_registre"] for u in inv if u["fournisseur"] == "argon"), max(u["fin_registre"] for u in inv if u["fournisseur"] == "argon"))
print("Argon : unités invalides :", [(u["monde"], u["carte"], u["suite"], [i + 1 for i, x in enumerate(u["statuts"]) if x == "invalide"]) for u in inv if u["fournisseur"] == "argon" and "invalide" in u["statuts"]])
print("Argon : unités échouées :", [(u["monde"], u["carte"], u["suite"], [i + 1 for i, x in enumerate(u["statuts"]) if x == "echouee"]) for u in inv if u["fournisseur"] == "argon" and "echouee" in u["statuts"]])
