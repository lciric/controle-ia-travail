"""Réexécution hors ligne, code gelé, mêmes graines : (1) l'audit A2 entier (`auditer_promues`, 200 rejeux « audit|… »
par loi promue sous v8, Clopper-Pearson, Holm), comparé champ à champ à « audit_A2 » ; (2) un échantillon des rejeux
« rejeu|… » (`_rejouer_loi`) : toutes les lois v7 (20 rejeux), et 28 lois v8 (les 10 plus hauts taux rejoués de W1, les
2 lois promues de W1, 10 lois de W1 tirées par random.Random(20261102), les 6 lois de W2 aux taux les plus bas et la plus
haute), comparés à « rejeux ». Deux processus (plan gelé), nice -n 10. Écrit travail/reexecution-v1.json."""
import json, sys, hashlib, random, time
ORCH = "/home/claude/ideation-organism/orchestrator"
sys.path.insert(0, ORCH)
from pole import attaque_goodhart_v2 as ag  # noqa: E402
B = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/"
R = json.load(open(B + "entree/sortie/attaque-goodhart-v2.json", encoding="utf-8"))
E = int(hashlib.sha256(open(ORCH + "/prereg/preenregistrement-attaque-goodhart-v2-v1.md", "rb").read()).hexdigest(), 16)
sortie = {}
t0 = time.time()
a2 = ag.auditer_promues(R["suites"], E, 200, processus=2)
sortie["A2_egal"] = json.loads(json.dumps(a2, sort_keys=True)) == R["audit_A2"]
sortie["A2_duree_s"] = round(time.time() - t0, 1)
print("A2 réexécuté == écrit :", sortie["A2_egal"], "| durée", sortie["A2_duree_s"], "s", flush=True)
rj = R["rejeux"]
lois = {(s["monde"], s["carte"], ag.etiquette_suite(s["monde"], s["fournisseur"], s["condition"], s["juge"]), t["k"]): t["loi"]
        for s in R["suites"] for t in s["tentatives"] if t["loi"] is not None}
w1v8 = [r for r in rj if r["monde"] == "W1" and r["juge"] == "v8"]
haut = sorted(w1v8, key=lambda r: (-r["promues"], r["etiquette"], r["carte"], r["k"]))[:10]
promues = [r for r in w1v8 if (r["etiquette"], r["carte"], r["k"]) in {("W1|argon|temoin|v8", 0, 4), ("W1|argon|retour|v8", 6, 16)}]
reste = [r for r in w1v8 if r not in haut and r not in promues]
alea = random.Random(20261102).sample(reste, 10)
w2 = sorted([r for r in rj if r["monde"] == "W2" and r["juge"] == "v8"], key=lambda r: (r["promues"], r["etiquette"], r["carte"]))
choix_v8 = haut + promues + alea + w2[:6] + w2[-1:]
choix = [r for r in rj if r["juge"] == "v7"] + choix_v8
taches = [(E, r["monde"], r["carte"], r["etiquette"], r["k"], lois[(r["monde"], r["carte"], r["etiquette"], r["k"])], r["juge"], r["rejeux"], "rejeu") for r in choix]
t0 = time.time()
res = ag._executer(taches, 2)
idx = {(r["monde"], r["carte"], r["etiquette"], r["k"], r["prefixe"]): r for r in rj}
ecarts = [(x, idx[(x["monde"], x["carte"], x["etiquette"], x["k"], x["prefixe"])]) for x in res if x != idx[(x["monde"], x["carte"], x["etiquette"], x["k"], x["prefixe"])]]
sortie.update({"rejeux_reexecutes": len(res), "v7": sum(1 for x in res if x["juge"] == "v7"), "v8": sum(1 for x in res if x["juge"] == "v8"),
               "rejeux_ecarts": ecarts, "rejeux_duree_s": round(time.time() - t0, 1),
               "echantillon_v8": [(r["etiquette"], r["carte"], r["k"], r["promues"]) for r in choix_v8]})
print("rejeux réexécutés :", len(res), "(v7", sortie["v7"], ", v8", sortie["v8"], ") | écarts :", len(ecarts), "| durée", sortie["rejeux_duree_s"], "s", flush=True)
json.dump(sortie, open(B + "travail/reexecution-v1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
