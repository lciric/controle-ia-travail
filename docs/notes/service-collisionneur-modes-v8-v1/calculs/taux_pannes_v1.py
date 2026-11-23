"""Taux d'essais non OK de l'étage III aux réglages actuels (Google 65 536 ; Carbon provision 49 152), par espèce."""
import json, re, subprocess
from collections import defaultdict
DEPOT = "/home/user/controle-ia-travail"
BRANCHES = ["origin/runs/collisionneurs-reprise-v8d-v1", "origin/runs/collisionneurs-reprise-minuit-v1"]
EXCLU = re.compile(r"coffre|modes|attaqu|sabot|quarantaine|evasion|tenu|coercition", re.I)
def git(*a):
    return subprocess.run(["git", "-C", DEPOT, *a], capture_output=True, text=True, check=True).stdout
REGL = {"argon": (65536, 16384), "carbon": (65536, 49152), "neon": (65536, 32768)}
n, ko, cout_ko = defaultdict(int), defaultdict(lambda: defaultdict(int)), defaultdict(float)
vus = set()
for br in BRANCHES:
    for p in git("ls-tree", "-r", "--name-only", br).splitlines():
        if not re.match(r"^runs/[^/]+/journal\.jsonl$", p) or EXCLU.search(p): continue
        d = p.rsplit("/", 1)[0]
        if d in vus: continue
        vus.add(d)
        for l in git("show", f"{br}:{p}").splitlines():
            if not l.strip(): continue
            e = json.loads(l)
            if "essai" not in e or not e["cellule"].startswith("E3-") or e.get("id_reponse") == "abonnement": continue
            s = e.get("espece")
            if s in REGL and (e.get("max_tokens"), e.get("provision_reflexion")) != REGL[s]: continue
            if s in ("opus", "fable") and (e.get("max_tokens") or 0) < 49000: continue
            n[s] += 1
            if e.get("statut") != "OK":
                ko[s][e.get("statut")] += 1
                cout_ko[s] += e.get("cout_usd") or 0
for s in sorted(n):
    t = sum(ko[s].values())
    print(f"{s:7s} essais {n[s]:3d} non OK {t:2d} ({t / n[s]:.1%}) {dict(ko[s])} coût compté des non OK {cout_ko[s]:.2f} USD")
