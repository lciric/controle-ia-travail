"""Relevé v2 : coûts, sorties, tailles des cellules et rapport caractères/jeton d'entrée, par espèce et par tour de
l'étage III, sur les journaux des collisionneurs (métadonnées ; textes comptés par programme, jamais affichés).
Exclut tout dossier dont le nom touche coffre, modes, attaques, sabotage, quarantaine, évasion, tenu, coercition.
Ne garde que les essais faits sous les réglages actuels : Google à 65 536 ; Astra, Fable, Opus quel que soit le plafond."""
import json, re, subprocess, sys, statistics as st
from collections import defaultdict
DEPOT = "/home/user/controle-ia-travail"
BRANCHES = ["origin/runs/collisionneurs-reprise-v8d-v1", "origin/runs/collisionneurs-reprise-minuit-v1"]
EXCLU = re.compile(r"coffre|modes|attaqu|sabot|quarantaine|evasion|tenu|coercition", re.I)
def git(*a):
    return subprocess.run(["git", "-C", DEPOT, *a], capture_output=True, text=True, check=True).stdout
def show(br, p):
    try:
        return git("show", f"{br}:{p}")
    except subprocess.CalledProcessError:
        return None
def q(vals, p):
    vals = sorted(vals)
    if not vals: return None
    k = (len(vals) - 1) * p
    f = int(k); c = min(f + 1, len(vals) - 1)
    return vals[f] + (vals[c] - vals[f]) * (k - f)
essais, vus = [], set()
for br in BRANCHES:
    for n in git("ls-tree", "-r", "--name-only", br).splitlines():
        if not re.match(r"^runs/[^/]+/journal\.jsonl$", n) or EXCLU.search(n):
            continue
        d = n.rsplit("/", 1)[0]
        if d in vus: continue
        vus.add(d)
        for l in (show(br, n) or "").splitlines():
            if l.strip():
                e = json.loads(l)
                if "essai" in e and e["cellule"].startswith("E3-"):
                    e["_d"], e["_br"] = d, br
                    essais.append(e)
groupes = defaultdict(list)
for e in essais:
    esp, tour = e.get("espece"), e["cellule"][:5]
    if esp in ("argon", "carbon", "neon") and e.get("max_tokens") != 65536:
        continue
    groupes[(esp, tour)].append(e)
sortie = {}
for (esp, tour), v in sorted(groupes.items(), key=lambda kv: (str(kv[0][0]), kv[0][1])):
    api = [e for e in v if e.get("id_reponse") != "abonnement"]
    ok = [e for e in api if e.get("statut") == "OK"]
    non_ok = [e for e in api if e.get("statut") != "OK"]
    couts = [e["cout_usd"] for e in ok]
    sorties = [(e.get("usage") or {}).get("sortie", 0) for e in ok]
    car_cell = []
    for e in v:
        if e.get("statut") == "OK":
            t = show(e["_br"], f"{e['_d']}/cellules/{e['cellule']}.md")
            if t is not None:
                car_cell.append(len(t))
    # rapport caractères d'invite / jetons comptés par l'interface
    rap = []
    for e in api:
        if e.get("compte_par_interface") and e.get("compte_entree"):
            p = show(e["_br"], f"{e['_d']}/essais/{e['cellule']}.essai{e['essai']}.prompt.txt")
            if p:
                rap.append(len(p) / e["compte_entree"])
    stat = defaultdict(int)
    for e in api: stat[e.get("statut")] += 1
    r = dict(essais_api=len(api), statuts=dict(stat), ok=len(ok),
             cout_ok_med=q(couts, .5), cout_ok_p90=q(couts, .9), cout_ok_max=max(couts) if couts else None,
             sortie_med=q(sorties, .5), sortie_p90=q(sorties, .9), sortie_max=max(sorties) if sorties else None,
             cout_non_ok_total=round(sum(e["cout_usd"] for e in non_ok), 4),
             car_cellule_med=q(car_cell, .5), car_cellule_max=max(car_cell) if car_cell else None, n_cell=len(car_cell),
             car_par_jeton_entree_min=min(rap) if rap else None, car_par_jeton_entree_med=q(rap, .5),
             plafonds=sorted(set(e.get("max_tokens") for e in api if e.get("max_tokens"))))
    sortie[f"{esp}|{tour}"] = r
    print(f"{esp:7s} {tour} " + json.dumps({k: (round(x, 3) if isinstance(x, float) else x) for k, x in r.items()}, ensure_ascii=False))
json.dump(sortie, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print("dossiers lus :", len(vus), "; essais de l'étage III :", len(essais))
