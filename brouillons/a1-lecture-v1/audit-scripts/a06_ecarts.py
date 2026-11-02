"""Audit A1 (auditeur neuf, 2e) — section 5, écarts déclarés : faits tirés du registre de dépense (apparié par a02), des
journaux de relais-complet/ et de la sortie. Lecture seule ; écrit travail/a06-ecarts-v1.json."""
import json, csv, collections, os, re
from datetime import datetime, timezone
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
RC = B + "entree/relais-complet/"
def p(s): return datetime.fromisoformat(s.replace("Z", "+00:00"))
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
app = list(csv.DictReader(open(B + "travail/a02-appariement-kimi-v1.csv", encoding="utf-8")))
out = {}
# (a) fenêtre de l'arrêt fautif : appels Kimi code 3 (relais injoignable) du registre
e3 = [x for x in app if x["code_registre"] == "3"]
out["a"] = {"appels_code_3": len(e3), "par_origine": dict(collections.Counter(x["origine_cout"] for x in e3)),
            "premier_code_3 (début, fin, origine)": (e3[0]["debut_registre"], e3[0]["fin_registre"], e3[0]["origine_cout"]),
            "dernier_code_3 (début, fin)": (e3[-1]["debut_registre"], e3[-1]["fin_registre"]),
            "cout_code_3_pire_cas": [float(x["cout_sortie"]) for x in e3 if x["origine_cout"] == "pire_cas"],
            "cout_code_3_plancher_total": round(sum(float(x["cout_sortie"]) for x in e3 if x["origine_cout"] == "plancher"), 6)}
tent3 = collections.OrderedDict()
for x in e3:
    tent3.setdefault((x["monde"], int(x["carte"]), x["condition"], x["juge"], int(x["k"])), []).append(int(x["essai"]))
out["a"]["tentatives_touchees"] = len(tent3)
out["a"]["tentatives_touchees_par_suite"] = {f"{w}|kimi|c{c}|{cond}|{j}": n for (w, c, cond, j), n in collections.Counter((k[0], k[1], k[2], k[3]) for k in tent3).items()}
# statut (sortie) de chaque tentative touchée
idx = {(s["monde"], s["fournisseur"], s["carte"], s["condition"], s["juge"]): s for s in R["suites"]}
st = collections.Counter()
for (w, c, cond, j, k) in tent3:
    t = idx[(w, "kimi", c, cond, j)]["tentatives"][k - 1]
    st[("loi" if t["loi"] is not None else t["motif_invalidite"])] += 1
out["a"]["statut_des_tentatives_touchees"] = dict(st)
out["a"]["unites_kimi_touchees (monde, carte)"] = sorted({(k[0], k[1]) for k in tent3})
out["a"]["suites_entierement_echouees_dans_la_fenetre"] = sorted(f"{w}|c{c}|{cond}|{j}" for (w, c, cond, j), n in collections.Counter((k[0], k[1], k[2], k[3]) for k in tent3).items() if n == 16)
# le second appel du 10:38:52 : succès (statut_amont 200) selon le journal du relais v1
j1 = [json.loads(l) for l in open(RC + "relais-kimi-journal.jsonl", encoding="utf-8")]
j2 = [json.loads(l) for l in open(RC + "relais-kimi-journal-v2.jsonl", encoding="utf-8")]
out["a"]["journal_relais_v1"] = [(e["quand_utc"], e.get("statut"), e.get("statut_amont"), e["duree_s"], e["cout_usd"]) for e in j1]
out["a"]["journal_relais_v2"] = [(e["quand_utc"], e.get("statut"), e.get("statut_amont"), e["duree_s"], e["cout_usd"]) for e in j2]
out["a"]["502_relais (quand, durée s)"] = [(e["quand_utc"], e["duree_s"]) for e in j1 + j2 if e.get("statut") == 502]
out["a"]["nb_502_relais"] = sum(1 for e in j1 + j2 if e.get("statut") == 502)
out["a"]["nb_succes_relais"] = sum(1 for e in j1 + j2 if e.get("statut_amont") == 200)
out["a"]["registre_code_5 (début, fin)"] = [(x["debut_registre"], x["fin_registre"], x["cout_sortie"]) for x in app if x["code_registre"] == "5"]
# (b) Kimi après le dernier appel enregistré
hors = [x for x in app if not x["debut_registre"]]
out["b"] = {"appels_kimi_hors_registre": len(hors), "cout_unitaire": dict(collections.Counter(x["cout_sortie"] for x in hors)), "statut": dict(collections.Counter(x["statut_sortie"] for x in hors)),
            "premier_hors_registre (monde, carte, condition, juge, k, essai)": [hors[0][k] for k in ("monde", "carte", "condition", "juge", "k", "essai")],
            "dernier_appel_enregistre (monde, carte, condition, juge, k, essai, début, fin, code)": [app[len(app) - len(hors) - 1][k] for k in ("monde", "carte", "condition", "juge", "k", "essai", "debut_registre", "fin_registre", "code_registre")],
            "tentatives_hors_registre": len({(x["monde"], x["carte"], x["condition"], x["juge"], x["k"]) for x in hors}),
            "suites_entierement_hors_registre": sum(1 for (w, c, cond, j), n in collections.Counter((x["monde"], x["carte"], x["condition"], x["juge"]) for x in hors).items() if n == 32),
            "unites_kimi_hors_registre (monde, carte)": sorted({(x["monde"], int(x["carte"])) for x in hors}),
            "dernier_debut_kimi_registre": max(x["debut_registre"] for x in app if x["debut_registre"]),
            "appels_kimi_commences_apres_12:23:14_au_registre": sum(1 for x in app if x["debut_registre"] and x["debut_registre"] >= "2026-11-02T12:23:14"),
            "cout_kimi_sortie_moins_registre": round(sum(float(x["cout_sortie"]) for x in app) - sum(float(x["cout_sortie"]) for x in app if x["debut_registre"]), 6)}
# chevauchement d'appels Kimi au registre (un fil par fournisseur)
reg = sorted((x["debut_registre"], x["fin_registre"]) for x in app if x["debut_registre"])
out["b"]["chevauchements_kimi_registre"] = sum(1 for i in range(len(reg) - 1) if reg[i + 1][0] < reg[i][1])
appa = list(csv.DictReader(open(B + "travail/a02-appariement-argon-v1.csv", encoding="utf-8")))
rega = sorted((x["debut_registre"], x["fin_registre"]) for x in appa if x["debut_registre"])
out["b"]["chevauchements_argon_registre"] = sum(1 for i in range(len(rega) - 1) if rega[i + 1][0] < rega[i][1])
out["b"]["argon_dernier_appel_fin"] = max(x["fin_registre"] for x in appa)
out["b"]["argon_echec (monde, carte, condition, juge, k, essai, début, fin, code, coût)"] = [[x[k] for k in ("monde", "carte", "condition", "juge", "k", "essai", "debut_registre", "fin_registre", "code_registre", "cout_sortie")] for x in appa if x["statut_registre"] != "ok"]
# (d) relance et appels après 12:23:14 : journaux
jl = open(RC + "journal-lancement-a1-v1.log", encoding="utf-8").read().splitlines()
out["d"] = {"lignes_relance_journal_lancement": [l for l in jl if "relancé" in l],
            "relais_kimi_v2_log": open(RC + "relais-kimi-v2.log", encoding="utf-8").read().strip(),
            "relais_kimi_log": open(RC + "relais-kimi.log", encoding="utf-8").read().strip(),
            "pid_kimi": open(RC + "relais-kimi.pid").read().strip(), "pid_kimi_v2": open(RC + "relais-kimi-v2.pid").read().strip(),
            "fichiers_relais_kimi_v3_ou_plus": [f for f in os.listdir(RC) if re.search(r"kimi.*v[3-9]", f) and not f.endswith(".sha256") and "guetteur" not in f],
            "etat_final_relais_kimi_octets": os.path.getsize(RC + "etat-final-relais-kimi.json"),
            "guetteur_v3_derniere_ligne": open(RC + "guetteur-kimi-a1-v3.log", encoding="utf-8").read().splitlines()[-1],
            "guetteur_v3_en_cours_a_12:23:14": [l for l in open(RC + "guetteur-kimi-a1-v3.log", encoding="utf-8").read().splitlines() if l.startswith("2026-11-02T12:23:14Z finis")],
            "journal_relais_v2_derniere_entree": (j2[-1]["quand_utc"], j2[-1].get("statut")), "journal_relais_v2_nb": len(j2),
            "etat_relais_v2_avant_arret_appels": json.load(open(RC + "etat-relais-kimi-v2-avant-arret.json"))["appels"],
            "etat_relais_v1_avant_arret": {k: json.load(open(RC + "etat-relais-kimi-avant-arret.json"))[k] for k in ("appels", "engage_usd", "depense_usd", "reponses_par_statut")},
            "lignes_journal_lancement_apres_12:23": [l for l in jl if l[:19] >= "2026-11-02T12:23:14"],
            "KIMI-SAUTE-V3": open(RC + "KIMI-SAUTE-V3", encoding="utf-8").read().strip()}
# durées
out["durees"] = {"debut_course (journal de lancement, ps)": "2026-11-02T09:58:45Z", "fin_utc (sortie)": R["fin_utc"], "duree_s (sortie)": R["duree_s"],
                 "premier_appel_registre": min(x["debut_registre"] for x in app + appa if x["debut_registre"]),
                 "dernier_appel_registre_fin": max(x["fin_registre"] for x in app + appa if x["fin_registre"]),
                 "argon_dernier_fin": out["b"]["argon_dernier_appel_fin"], "kimi_dernier_fin_registre": max(x["fin_registre"] for x in app if x["fin_registre"])}
json.dump(out, open(B + "travail/a06-ecarts-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
print(json.dumps(out, ensure_ascii=False, indent=1, default=str))
