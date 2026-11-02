"""Audit A1 (auditeur neuf, 2e) — section 4 : ré-exécution hors ligne des rejeux (`rejouer_tout`, 200 sous v8 et 20 sous v7)
et de l'audit A2 (`auditer_promues`, 200 rejeux « audit|… ») sur les suites de la sortie scellée, avec l'entropie du manifeste,
par le code gelé ; comparaison entrée par entrée aux blocs « rejeux » et « audit_A2 » écrits. Aucun appel de modèle.
Usage : a04_rejeux.py [--essai] (essai : 3 lois, 2 rejeux)."""
import json, sys, time
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
sys.path.insert(0, "/home/claude/ideation-organism/orchestrator")
from pole import attaque_goodhart_v2 as ag
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
M = json.load(open(B + "entree/sortie/manifeste.json", encoding="utf-8"))
entropie = int(M["reglages"]["entropie_racine"])
essai = "--essai" in sys.argv
suites = R["suites"]
if essai:
    suites = [s for s in suites if s["fournisseur"] == "argon" and s["monde"] == "W1" and s["carte"] == 0][:3]
t0 = time.time()
rejeux = ag.rejouer_tout(suites, entropie, {"v8": 2, "v7": 2} if essai else {"v8": 200, "v7": 20}, processus=2)
t1 = time.time()
audits = ag.auditer_promues(suites, entropie, 2 if essai else 200, processus=2)
t2 = time.time()
cle = lambda r: (r["monde"], r["carte"], r["etiquette"], r["k"], r["juge"], r["prefixe"])  # noqa: E731
ecrits = {cle(r): r for r in R["rejeux"]}
ecrits_a = {cle(r): r for r in R["audit_A2"]}
res = {"essai": essai, "duree_rejeux_s": round(t1 - t0, 1), "duree_audit_s": round(t2 - t1, 1), "nb_rejeux": len(rejeux), "nb_audits": len(audits),
       "ecarts_rejeux": [], "ecarts_audit": [], "manquants_rejeux": [], "manquants_audit": []}
if not essai:
    res["manquants_rejeux"] = [str(k) for k in set(ecrits) - {cle(r) for r in rejeux}] + [str(cle(r)) for r in rejeux if cle(r) not in ecrits]
    res["manquants_audit"] = [str(k) for k in set(ecrits_a) - {cle(r) for r in audits}] + [str(cle(r)) for r in audits if cle(r) not in ecrits_a]
for r in rejeux:
    e = ecrits.get(cle(r))
    if e is None:
        continue
    if essai:
        continue
    for ch in ("promues", "rejeux", "evaluations_impossibles"):
        if e[ch] != r[ch]:
            res["ecarts_rejeux"].append((str(cle(r)), ch, e[ch], r[ch]))
for r in audits:
    e = ecrits_a.get(cle(r))
    if e is None or essai:
        continue
    for ch in ("promues", "rejeux", "evaluations_impossibles", "au_dessus_de_alpha_holm", "structurellement_couverte"):
        if e[ch] != r[ch]:
            res["ecarts_audit"].append((str(cle(r)), ch, e[ch], r[ch]))
    if abs(e["clopper_pearson_95_bas"] - r["clopper_pearson_95_bas"]) > 1e-9:
        res["ecarts_audit"].append((str(cle(r)), "clopper_pearson_95_bas", e["clopper_pearson_95_bas"], r["clopper_pearson_95_bas"]))
res["rejeux_recalcules"] = rejeux
res["audit_recalcule"] = audits
nom = "a04-rejeux-essai-v1.json" if essai else "a04-rejeux-v1.json"
json.dump(res, open(B + "travail/" + nom, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ("rejeux_recalcules", "audit_recalcule")}, ensure_ascii=False, indent=1))
