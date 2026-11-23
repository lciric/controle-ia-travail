"""Nombres du jeu de 60 tâches du pilote (branche main) : aucun texte de cible, d'énoncé ni d'identifiant n'est affiché."""
import hashlib, json, statistics, subprocess
from collections import Counter

DEPOT = "/home/user/controle-ia-travail"
CHEMIN = "donnees/t05-pilote-v1/taches-pilote-60-v1.json"
brut = subprocess.run(["git", "-C", DEPOT, "show", f"main:{CHEMIN}"], check=True, capture_output=True).stdout
print("sha256", hashlib.sha256(brut).hexdigest())
d = json.loads(brut.decode("utf-8"))
src = d["source"]
print("source: clés", list(src.keys()))
for k, v in src.items():
    print("  ", k, "=", repr(v)[:300])
T = d["taches"]
n = len(T)
print("tâches:", n)

def resume(nom, xs):
    xs = sorted(xs)
    q = statistics.quantiles(xs, n=4, method="inclusive")
    print(f"{nom}: n={len(xs)} min={xs[0]} q1={q[0]:.0f} médiane={statistics.median(xs):.0f} q3={q[2]:.0f} max={xs[-1]} moyenne={statistics.mean(xs):.0f}")

resume("énoncé, signes", [len(t["questions"]) for t in T])
resume("énoncé, mots", [len(t["questions"].split()) for t in T])
print("type de papier:", sorted(Counter(t["classification"]["theory_experiment"] for t in T).items()))
print("type de données:", sorted(Counter(t["classification"]["data_type"] for t in T).items()))
resume("domaines par tâche", [len(t["classification"]["domains"]) for t in T])
for fam in ("controls", "fruitful_directions", "sterile_directions"):
    c = Counter(len(t["cibles"][fam]) for t in T)
    print(f"{fam}: distribution du nombre par tâche {sorted(c.items())}, total {sum(len(t['cibles'][fam]) for t in T)}, médiane {statistics.median(len(t['cibles'][fam]) for t in T)}")
    cles = Counter(k for t in T for it in t["cibles"][fam] for k in it)
    print("   clés d'un élément:", sorted(cles.items()))
    resume(f"   {fam} description, signes", [len(it["description"]) for t in T for it in t["cibles"][fam]])
    resume(f"   {fam} citation (evidence), signes", [len(it["evidence"]) for t in T for it in t["cibles"][fam]])
comp = [t["cibles"]["compute"] for t in T]
print("compute: clés", sorted(Counter(k for c in comp for k in c).items()))
print("compute.basis:", sorted(Counter(str(c.get("basis")) for c in comp).items()))
nn = [c.get("reference_gpu_hours") for c in comp]
print("compute.reference_gpu_hours: non nul", sum(v is not None for v in nn), "nul", sum(v is None for v in nn))
print("compute par base: ", sorted(Counter((str(c.get("basis")), c.get("reference_gpu_hours") is not None) for c in comp).items()))
vals = [float(v) for v in nn if v is not None]
if vals:
    vs = sorted(vals)
    print(f"   heures de référence: min={vs[0]:g} médiane={statistics.median(vs):g} max={vs[-1]:g}")
cr = [t["couts_rapportes"] for t in T]
print("couts_rapportes.total: non nul", sum(c.get("total") is not None for c in cr), "nul", sum(c.get("total") is None for c in cr))
print("tentative:", sorted(Counter(t["tentative"] for t in T).items()))
# tâches où les trois familles sont toutes présentes (au moins un élément)
print("tâches avec au moins une direction stérile:", sum(len(t["cibles"]["sterile_directions"]) > 0 for t in T))
