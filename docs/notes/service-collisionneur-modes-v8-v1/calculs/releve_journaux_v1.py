"""Relevé des journaux des collisionneurs (métadonnées seulement ; mots des cellules comptés par programme, jamais affichés).
Exclut tout dossier dont le nom touche coffre, modes, attaques, sabotage, quarantaine, évasion, tenu, coercition."""
import json, re, subprocess, sys, statistics as st
from collections import defaultdict
DEPOT = "/home/user/controle-ia-travail"
BRANCHES = ["origin/runs/collisionneurs-reprise-v8d-v1", "origin/runs/collisionneurs-reprise-minuit-v1"]
EXCLU = re.compile(r"coffre|modes|attaqu|sabot|quarantaine|evasion|tenu|coercition", re.I)
def git(*a):
    return subprocess.run(["git", "-C", DEPOT, *a], capture_output=True, text=True, check=True).stdout
lignes = []
vus = set()
for br in BRANCHES:
    noms = [n for n in git("ls-tree", "-r", "--name-only", br).splitlines()
            if re.match(r"^runs/[^/]+/journal\.jsonl$", n) and not EXCLU.search(n)]
    for n in noms:
        d = n.rsplit("/", 1)[0]
        cle = (d,)
        if cle in vus:   # même dossier sur les deux branches : la branche v8d (plus récente) prime
            continue
        vus.add(cle)
        for l in git("show", f"{br}:{n}").splitlines():
            if not l.strip():
                continue
            e = json.loads(l)
            if "essai" not in e:
                continue
            e["_dossier"], e["_branche"] = d, br
            lignes.append(e)
# mots des cellules valides (OK) : compte par programme
def mots_cellule(br, d, cid):
    try:
        t = git("show", f"{br}:{d}/cellules/{cid}.md")
    except subprocess.CalledProcessError:
        return None
    return len(t.split())
par = defaultdict(list)
for e in lignes:
    tour = e["cellule"][:5]
    u = e.get("usage") or {}
    m = mots_cellule(e["_branche"], e["_dossier"], e["cellule"]) if e.get("statut") == "OK" else None
    vis = u.get("sortie_visible")
    if vis is None and e.get("espece") in ("fable", "opus") :
        vis = None
    par[(e.get("espece"), tour)].append(dict(dossier=e["_dossier"][5:60], essai=e["essai"], statut=e.get("statut"),
        fin=e.get("fin"), max=e.get("max_tokens"), prov=e.get("provision_reflexion"), entree=u.get("entree"),
        sortie=u.get("sortie"), visible=vis, pensees=u.get("reflexion", u.get("raisonnement")), cout=e.get("cout_usd"),
        pire=e.get("cout_pire_usd"), car=e.get("caracteres"), mots=m, script=e.get("script"), abonnement=e.get("id_reponse") == "abonnement"))
json.dump({f"{k[0]}|{k[1]}": v for k, v in par.items()}, open(sys.argv[1], "w"), ensure_ascii=False, indent=0)
print("essais lus :", len(lignes))
for (esp, tour), v in sorted(par.items(), key=lambda kv: (str(kv[0][0]), kv[0][1])):
    ok = [x for x in v if x["statut"] == "OK" and not x["abonnement"]]
    stat = defaultdict(int)
    for x in v: stat[x["statut"]] += 1
    def med(cle, xs):
        vals = [x[cle] for x in xs if isinstance(x.get(cle), (int, float))]
        return (round(st.median(vals), 3), round(max(vals), 3), len(vals)) if vals else None
    tpm = [x["visible"] / x["mots"] for x in ok if x.get("visible") and x.get("mots")]
    tpm_tot = [x["sortie"] / x["mots"] for x in ok if x.get("sortie") and x.get("mots")]
    print(f"{esp:8s} {tour}  essais {len(v):3d} {dict(stat)}")
    print(f"    OK hors abonnement : mots {med('mots', ok)} ; sortie {med('sortie', ok)} ; visible {med('visible', ok)} ; pensées {med('pensees', ok)} ; coût {med('cout', ok)}")
    if tpm: print(f"    jetons de texte par mot rendu : médiane {st.median(tpm):.2f}, max {max(tpm):.2f}, n {len(tpm)}")
    if tpm_tot: print(f"    jetons de sortie totale par mot rendu : médiane {st.median(tpm_tot):.2f}, max {max(tpm_tot):.2f}")
    print(f"    plafonds vus : {sorted(set(x['max'] for x in v if x['max']))}")
