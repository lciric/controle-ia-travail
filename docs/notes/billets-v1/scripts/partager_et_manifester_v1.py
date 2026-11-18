"""Tâche 3 : partage par programme (graine SeedSequence consignée), stratifié par année et
par classe ; puis manifeste du corpus dans le dépôt. Texte rangé hors du dépôt par moitié."""
import json, hashlib, os, shutil, datetime
import numpy as np

RACINE = "/home/user/billets-corpus-v1"
MANIF = "/home/user/controle-ia-travail/docs/notes/billets-v1/manifeste-corpus-v1.json"
ENTROPIE = 0x5EED_B111_E75_2026_11_18  # graine écrite avant le tirage, consignée au manifeste

meta = json.load(open(f"{RACINE}/metadonnees-v1.json"))
cl = json.load(open(f"{RACINE}/classement-v1.json"))
com = json.load(open(f"{RACINE}/commentaires-v1.json"))
billets = {p["_id"]: p for p in cl["billets"]}
ss = np.random.SeedSequence(ENTROPIE)
annees = sorted({p["annee"] for p in cl["paires"]})
enfants = dict(zip(annees, ss.spawn(len(annees))))
moitie = {}
for an in annees:
    rng = np.random.default_rng(enfants[an])
    for strate in ("apparie", "sans_apparie"):
        unites = sorted(p["haut"] for p in cl["paires"] if p["annee"] == an
                        and bool(p["apparie"]) == (strate == "apparie"))
        perm = list(rng.permutation(len(unites)))
        n_dev = len(unites) // 2 + (int(rng.integers(2)) if len(unites) % 2 else 0)
        for rang, i in enumerate(perm):
            moitie[unites[i]] = "developpement" if rang < n_dev else "tenue-a-l-ecart"


def empreinte(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest(), os.path.getsize(chemin)


for m in ("developpement", "tenue-a-l-ecart"):
    os.makedirs(f"{RACINE}/{m}/billets", exist_ok=True)
    os.makedirs(f"{RACINE}/{m}/commentaires", exist_ok=True)

entrees = []
for p in cl["paires"]:
    m = moitie[p["haut"]]
    for role, pid in (("bien-note", p["haut"]), ("apparie-peu-note", p["apparie"])):
        if not pid:
            continue
        b = billets[pid]
        dst = f"{RACINE}/{m}/billets/{pid}.md"
        shutil.copyfile(f"{RACINE}/tous-textes/{pid}.md", dst)
        h, n = empreinte(dst)
        e = {"identifiant": pid, "adresse": b["pageUrl"], "titre": b["title"],
             "auteur": b["user"]["displayName"] if b.get("user") else None,
             "coauteurs": [c["displayName"] for c in b.get("coauthors") or []],
             "date": b["postedAt"], "annee": b["annee"], "votes_score": b["baseScore"],
             "nombre_de_votants": b["voteCount"], "nombre_de_commentaires": b["commentCount"],
             "nombre_de_mots_site": b["wordCount"], "alignment_forum": b["af"],
             "etiquettes": [t["name"] for t in b["tags"]],
             "etiquettes_retenues": b["etiq_retenues"],
             "classe": role, "classe_auto": b["classe_auto"], "motif_classement": b["motif"],
             "apparie_a": p["apparie"] if role == "bien-note" else p["haut"],
             "moitie": m, "empreinte_sha256_texte": h, "taille_octets": n}
        if role == "bien-note":
            src = f"{RACINE}/tous-commentaires/{pid}.json"
            dstc = f"{RACINE}/{m}/commentaires/{pid}.json"
            shutil.copyfile(src, dstc)
            hc, nc = empreinte(dstc)
            e["commentaires_retenus"] = com["commentaires"][pid]
            e["empreinte_sha256_commentaires"] = hc
            e["taille_octets_commentaires"] = nc
        entrees.append(e)

manifeste = {
    "version": "v1", "mandat": "docs/notes/billets-v1/mandat-corpus-et-grille-v1.md",
    "regle": "docs/notes/billets-v1/regle-classement-et-appariement-v1.md",
    "date_du_tirage_metadonnees": meta["date_du_tirage"],
    "date_du_manifeste": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "source": "https://www.lesswrong.com/graphql (POST)",
    "etiquettes_retenues": meta["etiquettes"],
    "requetes_employees": {
        "metadonnees": {"requete": meta["requete"], "termes": meta["termes"]},
        "textes": json.load(open(f"{RACINE}/requetes-textes-v1.json")),
        "commentaires": {"requete": com["requete"], "termes": com["termes"]},
    },
    "scripts": "docs/notes/billets-v1/scripts/",
    "partage": {"graine_entropie": str(ENTROPIE), "generateur": "numpy.random.SeedSequence, spawn par année, "
                "default_rng ; unité = paire ; strates = année × (apparié / sans apparié)",
                "numpy": np.__version__},
    "journal_classement": cl["journal"],
    "texte_hors_depot": RACINE,
    "billets": entrees,
}
json.dump(manifeste, open(MANIF, "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(Counter((e["annee"], e["classe"], e["moitie"]) for e in entrees))
print("entrees", len(entrees), "commentaires", sum(len(e.get("commentaires_retenus", [])) for e in entrees))
