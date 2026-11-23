"""Essais non OK de l'étage III : espèce, tour, statut, plafond, provision, coût compté, script, dossier (métadonnées)."""
import json, re, subprocess
DEPOT = "/home/user/controle-ia-travail"
BRANCHES = ["origin/runs/collisionneurs-reprise-v8d-v1", "origin/runs/collisionneurs-reprise-minuit-v1"]
EXCLU = re.compile(r"coffre|modes|attaqu|sabot|quarantaine|evasion|tenu|coercition", re.I)
def git(*a):
    return subprocess.run(["git", "-C", DEPOT, *a], capture_output=True, text=True, check=True).stdout
vus = set()
for br in BRANCHES:
    for n in git("ls-tree", "-r", "--name-only", br).splitlines():
        if not re.match(r"^runs/[^/]+/journal\.jsonl$", n) or EXCLU.search(n): continue
        d = n.rsplit("/", 1)[0]
        if d in vus: continue
        vus.add(d)
        for l in git("show", f"{br}:{n}").splitlines():
            if not l.strip(): continue
            e = json.loads(l)
            if "essai" in e and e["cellule"].startswith("E3-") and e.get("statut") != "OK":
                u = e.get("usage") or {}
                print(f"{e.get('espece'):7s} {e['cellule'][:5]} {e.get('statut'):26s} max {e.get('max_tokens')} prov {e.get('provision_reflexion')} "
                      f"sortie {u.get('sortie')} pensees {u.get('reflexion', u.get('raisonnement'))} cout {e.get('cout_usd')} pire {e.get('cout_pire_usd')} "
                      f"{e.get('script')} {d[5:55]} echec={str(e.get('echec'))[:70]}")
