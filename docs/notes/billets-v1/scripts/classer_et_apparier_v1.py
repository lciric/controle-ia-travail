"""Tâche 2, étape 3 : classement par programme selon la règle scellée
`regle-classement-et-appariement-v1.md`, choix des 15 bien notés par année, appariement.
N'affiche aucun texte : seulement identifiants, titres et décomptes."""
import json, math, re, os

RACINE = "/home/user/billets-corpus-v1"
meta = json.load(open(f"{RACINE}/metadonnees-v1.json"))
ETIQ = set(meta["etiquettes"])

MARQUEURS = [r"\bwe (?:train|trained|find|found|evaluate|evaluated|ran|run|measure|measured|"
             r"fine-?tune|fine-?tuned|test|tested|observe|observed|show|compare|compared|"
             r"replicate|replicated|apply|applied|investigate|investigated)\b",
             r"\bour (?:results|experiments?|findings|method|probes?|models?|evaluations?|setup)\b",
             r"\bI (?:trained|ran|found|find|measured|tested|evaluated|fine-?tuned|observed|replicated)\b",
             r"\bmy (?:results|experiments?|findings)\b"]
METRIQUES = r"(?:accuracy|AUROC|AUC|loss|F1|recall|precision|success rate|win rate|correlation)"
NOMBRES = [r"\b\d{1,3}(?:\.\d+)?\s?%", r"\b0\.\d{2,}\b",
           rf"{METRIQUES}[^.\n]{{0,40}}?\b\d+(?:\.\d+)?", rf"\b\d+(?:\.\d+)?\s?{METRIQUES}"]
IMAGE = r"!\[[^\]]*\]\("


def classe(p):
    if p["question"] or p["isEvent"] or p.get("draft"):
        return "exclu", "question, événement ou brouillon"
    chemin = f"{RACINE}/tous-textes/{p['_id']}.md"
    if not os.path.exists(chemin):
        return "exclu", "texte non tiré"
    t = open(chemin).read()
    mots = len(t.split())
    if mots < 300:
        return "autre", "moins de 300 mots"
    n_marq = sum(len(re.findall(m, t, re.I)) for m in MARQUEURS)
    n_nomb = sum(len(re.findall(m, t, re.I)) for m in NOMBRES)
    n_img = len(re.findall(IMAGE, t))
    if n_marq >= 2 and (n_img >= 1 or n_nomb >= 2):
        return "resultats", f"marqueurs={n_marq} nombres={n_nomb} images={n_img}"
    return "autre", f"marqueurs={n_marq} nombres={n_nomb} images={n_img}"


par_an = {}
for p in meta["billets"]:
    p["annee"] = int(p["postedAt"][:4])
    p["etiq_retenues"] = sorted(ETIQ & {t["_id"] for t in p["tags"]})
    p["classe_auto"], p["motif"] = classe(p)
    par_an.setdefault(p["annee"], []).append(p)

choix, journal = [], {}
for an, ps in sorted(par_an.items()):
    scores = sorted(x["baseScore"] for x in ps)
    seuil_bas = scores[len(scores) // 3 - 1] if len(scores) >= 3 else min(scores)
    res = sorted([x for x in ps if x["classe_auto"] == "resultats"],
                 key=lambda x: (-x["baseScore"], x["_id"]))
    hauts = res[:15]
    pris = set()
    pool = [x for x in res if x["baseScore"] <= seuil_bas]
    for h in hauts:
        cands = []
        for c in pool:
            if c["_id"] in pris or not (set(c["etiq_retenues"]) & set(h["etiq_retenues"])):
                continue
            r = (c["wordCount"] or 1) / max(h["wordCount"] or 1, 1)
            if not (0.67 <= r <= 1.5):
                continue
            a, b = set(c["etiq_retenues"]), set(h["etiq_retenues"])
            cands.append((-len(a & b) / len(a | b), abs(math.log(r)), c["_id"], c))
        cands.sort(key=lambda z: z[:3])
        app = cands[0][3] if cands else None
        if app:
            pris.add(app["_id"])
        choix.append({"haut": h["_id"], "apparie": app["_id"] if app else None, "annee": an})
    journal[an] = {"billets": len(ps), "resultats_auto": len(res),
                   "seuil_tiers_bas_score": seuil_bas, "pool_bas_resultats": len(pool),
                   "exclus": sum(x["classe_auto"] == "exclu" for x in ps),
                   "sans_apparie": sum(1 for c in choix if c["annee"] == an and not c["apparie"])}
json.dump({"billets": meta["billets"], "paires": choix, "journal": journal},
          open(f"{RACINE}/classement-v1.json", "w"), ensure_ascii=False)
print(json.dumps(journal, indent=1))
