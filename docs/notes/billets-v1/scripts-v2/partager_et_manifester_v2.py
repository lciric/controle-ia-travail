"""Corpus v2 : partage par programme (graine neuve SeedSequence consignée dans la règle v2,
point 9, avant le tirage), stratifié par année et par classe ; manifeste ; dossier de la moitié
tenue à l'écart rendu illisible."""
import json, hashlib, os, shutil, datetime, sys
import numpy as np
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from candidats_v2 import billets, meta, par_annee, seuil_tiers_bas, hauts
V2 = "/home/user/billets-corpus-v2"
D = "/home/user/controle-ia-travail/docs/notes/billets-v1"
ENTROPIE = 0x7A1C0DE2_2026_1118_0B2
ap = json.load(open(f"{D}/appariements-v2.json"))
com = json.load(open(f"{V2}/commentaires-v2.json"))
J = [json.loads(l) for l in open(f"{D}/journal-tri-v2.jsonl")]
motif = {}
for l in J: motif[l["identifiant"]] = (l["decision"], l["motif"], l["role"])

# ordre des bien notés par année : celui du journal (rang de score)
paires = []
for an in range(2022, 2027):
    for h in [k for k, v in ap.items() if v["annee"] == an]:
        paires.append({"haut": h, "apparie": ap[h]["apparie"], "annee": an})
ss = np.random.SeedSequence(ENTROPIE)
annees = list(range(2022, 2027))
enfants = dict(zip(annees, ss.spawn(len(annees))))
moitie = {}
for an in annees:
    rng = np.random.default_rng(enfants[an])
    for strate in ("apparie", "sans_apparie"):
        unites = sorted(p["haut"] for p in paires if p["annee"] == an and bool(p["apparie"]) == (strate == "apparie"))
        perm = list(rng.permutation(len(unites)))
        n_dev = len(unites) // 2 + (int(rng.integers(2)) if len(unites) % 2 else 0)
        for rang, i in enumerate(perm):
            moitie[unites[i]] = "developpement" if rang < n_dev else "tenue-a-l-ecart"

def empreinte(c):
    return hashlib.sha256(open(c, "rb").read()).hexdigest(), os.path.getsize(c)

for m in ("developpement", "tenue-a-l-ecart"):
    os.makedirs(f"{V2}/{m}/billets", exist_ok=True); os.makedirs(f"{V2}/{m}/commentaires", exist_ok=True)
entrees = []
for p in paires:
    m = moitie[p["haut"]]
    for role, pid in (("bien-note", p["haut"]), ("apparie-peu-note", p["apparie"])):
        if not pid: continue
        b = billets[pid]; dst = f"{V2}/{m}/billets/{pid}.md"
        shutil.copyfile(f"{V2}/tous-textes/{pid}.md", dst)
        h, n = empreinte(dst)
        e = {"identifiant": pid, "adresse": b["pageUrl"], "titre": b["title"],
             "auteur": b["user"]["displayName"] if b.get("user") else None,
             "coauteurs": [c["displayName"] for c in b.get("coauthors") or []],
             "date": b["postedAt"], "annee": b["annee"], "votes_score": b["baseScore"],
             "nombre_de_votants": b["voteCount"], "nombre_de_commentaires": b["commentCount"],
             "nombre_de_mots_site": b["wordCount"], "alignment_forum": b["af"],
             "etiquettes": [t["name"] for t in b["tags"]], "etiquettes_retenues": b["etiq"],
             "classe": role, "decision_tri": motif[pid][0], "motif_tri": motif[pid][1],
             "sans_apparie": (role == "bien-note" and not p["apparie"]),
             "essais_apparie": ap[p["haut"]]["essais"] if role == "bien-note" else None,
             "apparie_a": p["apparie"] if role == "bien-note" else p["haut"],
             "moitie": m, "empreinte_sha256_texte": h, "taille_octets": n}
        if role == "bien-note":
            dstc = f"{V2}/{m}/commentaires/{pid}.json"
            shutil.copyfile(f"{V2}/tous-commentaires/{pid}.json", dstc)
            hc, nc = empreinte(dstc)
            e["commentaires_retenus"] = com["commentaires"][pid]
            e["empreinte_sha256_commentaires"] = hc; e["taille_octets_commentaires"] = nc
        entrees.append(e)

# décomptes de tri par année
journal = {}
for an in annees:
    ps = par_annee(an); cand = hauts(an)
    lus_h = [l for l in J if l["role"] == "haut" and l["annee"] == an]
    # lus avant le quinzième « oui » (rang inclus)
    cpt, avant = 0, []
    for l in lus_h:
        avant.append(l)
        if l["decision"] == "oui": cpt += 1
        if cpt == 15: break
    lus_a = [l for l in J if l["role"].startswith("apparie") and l["annee"] == an]
    journal[an] = {"billets_avec_etiquette": len(ps),
        "ecartes_mecaniquement": sum(1 for p in ps if p["meca"]),
        "candidats": len(cand), "seuil_tiers_bas_score": seuil_tiers_bas(an),
        "hauts_lus": len(lus_h), "hauts_lus_jusqu_au_quinzieme_oui": len(avant),
        "hauts_oui": sum(l["decision"] == "oui" for l in lus_h),
        "hauts_non_jusqu_au_quinzieme_oui": sum(l["decision"] == "non" for l in avant),
        "apparies_lus": len(lus_a), "apparies_oui_lus": sum(l["decision"] == "oui" for l in lus_a),
        "apparies_retenus": sum(1 for p in paires if p["annee"] == an and p["apparie"]),
        "sans_apparie": sum(1 for p in paires if p["annee"] == an and not p["apparie"])}
manifeste = {
    "version": "v2", "mandat": "docs/notes/billets-v1/mandat-corpus-v2-tri-a-la-lecture-v1.md",
    "regle": "docs/notes/billets-v1/regle-tri-a-la-lecture-v2.md",
    "journal_de_tri": "docs/notes/billets-v1/journal-tri-v2.jsonl", "appariements": "docs/notes/billets-v1/appariements-v2.json",
    "date_du_tirage_metadonnees": meta["date_du_tirage"], "date_du_complement": meta["date_complement"],
    "date_du_manifeste": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "source": "https://www.lesswrong.com/graphql (POST)",
    "etiquettes_retenues": meta["etiquettes"], "etiquettes_ajoutees": meta["etiquettes_ajoutees"],
    "requetes_employees": {"metadonnees": "reprise de la v1 (manifeste-corpus-v1.json) pour les sept étiquettes ; complément ci-dessous",
        "complement": {"requete": meta["requete_complement"], "termes": meta["termes_complement"]},
        "commentaires": {"requete": com["requete"], "termes": com["termes"]}},
    "scripts": "docs/notes/billets-v1/scripts/ (v1, réemployés) et scripts-v2/",
    "partage": {"graine_entropie": str(ENTROPIE), "graine_hexadecimale": hex(ENTROPIE),
                "generateur": "numpy.random.SeedSequence, spawn par année, default_rng ; unité = paire ; strates = année × (apparié / sans apparié)",
                "numpy": np.__version__},
    "journal_tri": journal, "texte_hors_depot": V2, "billets": entrees}
json.dump(manifeste, open(f"{D}/manifeste-corpus-v2.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(Counter((e["annee"], e["classe"], e["moitie"]) for e in entrees))
print("entrees", len(entrees), "commentaires", sum(len(e.get("commentaires_retenus", [])) for e in entrees))
print(json.dumps(journal, indent=0)[:3000])
