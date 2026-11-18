"""Corpus v2 : candidats par année (règle de tri à la lecture v2, points 4 à 7). Importé par
les autres scripts. Aucun texte affiché."""
import json, math, re, os
V2 = "/home/user/billets-corpus-v2"
meta = json.load(open(f"{V2}/metadonnees-v2.json"))
ETIQ = set(meta["etiquettes"])
# classement automatique de la v1, repris tel quel : ORDRE DE LECTURE des appariés seulement
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

def texte(i):
    return open(f"{V2}/tous-textes/{i}.md").read()

def heuristique_v1(i):
    t = texte(i)
    if len(t.split()) < 300: return False
    n_marq = sum(len(re.findall(m, t, re.I)) for m in MARQUEURS)
    n_nomb = sum(len(re.findall(m, t, re.I)) for m in NOMBRES)
    n_img = len(re.findall(IMAGE, t))
    return n_marq >= 2 and (n_img >= 1 or n_nomb >= 2)

billets = {}
for p in meta["billets"]:
    p["annee"] = int(p["postedAt"][:4])
    p["etiq"] = sorted(ETIQ & {t["_id"] for t in p["tags"]})
    mots = p["wordCount"] if p.get("wordCount") else len(texte(p["_id"]).split())
    p["mots"] = mots
    if p["question"] or p["isEvent"] or p.get("draft"): p["meca"] = "question, événement ou brouillon"
    elif mots < 300: p["meca"] = "moins de 300 mots"
    else: p["meca"] = None
    billets[p["_id"]] = p

def par_annee(an):
    return [p for p in billets.values() if p["annee"] == an]

def seuil_tiers_bas(an):
    s = sorted(x["baseScore"] for x in par_annee(an))
    return s[len(s) // 3 - 1] if len(s) >= 3 else min(s)

def hauts(an):
    return sorted([p for p in par_annee(an) if p["meca"] is None], key=lambda x: (-x["baseScore"], x["_id"]))

def viviers_apparies(h, deja_apparies, faux):
    an = h["annee"]; seuil = seuil_tiers_bas(an); out = []
    for c in par_annee(an):
        if c["meca"] or c["baseScore"] > seuil or c["_id"] in deja_apparies or c["_id"] in faux or c["_id"] == h["_id"]:
            continue
        if not (set(c["etiq"]) & set(h["etiq"])): continue
        r = c["mots"] / max(h["mots"], 1)
        if not (0.67 <= r <= 1.5): continue
        a, b = set(c["etiq"]), set(h["etiq"])
        out.append((0 if heuristique_v1(c["_id"]) else 1, -len(a & b) / len(a | b), abs(math.log(r)), c["_id"], c))
    out.sort(key=lambda z: z[:4])
    return [z[4] for z in out]
