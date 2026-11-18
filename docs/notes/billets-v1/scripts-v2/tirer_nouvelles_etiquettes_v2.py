"""Corpus v2, étape 1 : reprend la copie des métadonnées et des textes de la v1 (lecture seule
de /home/user/billets-corpus-v1, copie sous v2), puis tire métadonnées et textes des deux
étiquettes ajoutées (autoencodeurs épars, ingénierie des activations), mêmes requêtes que la v1.
Aucun texte affiché."""
import json, os, shutil, datetime
from client_graphql_v2 import requete

V1, V2 = "/home/user/billets-corpus-v1", "/home/user/billets-corpus-v2"
NOUVELLES = {"9LYbEZSAi8kq83DGF": "Sparse Autoencoders (SAEs)", "QdTRKbR4MJSz4JWvn": "Activation Engineering"}
ANNEES = [2022, 2023, 2024, 2025, 2026]
Q = """query($t:JSON){ posts(input:{terms:$t}){ results{ _id title slug pageUrl postedAt baseScore
 voteCount commentCount wordCount question isEvent af draft user{displayName} coauthors{displayName}
 tags{_id name} contents{ markdown } } } }"""

os.makedirs(f"{V2}/tous-textes", exist_ok=True)
meta = json.load(open(f"{V1}/metadonnees-v1.json"))
for f in os.listdir(f"{V1}/tous-textes"):
    if not os.path.exists(f"{V2}/tous-textes/{f}"):
        shutil.copyfile(f"{V1}/tous-textes/{f}", f"{V2}/tous-textes/{f}")
billets = {p["_id"]: p for p in meta["billets"]}
n_v1 = len(billets)
termes, nouveaux = [], 0
for tid, nom in NOUVELLES.items():
    for an in ANNEES:
        off = 0
        while True:
            t = {"view": "top", "filterSettings": {"tags": [{"tagId": tid, "tagName": nom,
                 "filterMode": "Required"}]}, "after": f"{an}-01-01", "before": f"{an+1}-01-01",
                 "limit": 50, "offset": off}
            termes.append(t)
            res = requete(Q, {"t": t})["posts"]["results"]
            for p in res:
                md = (p.pop("contents", None) or {}).get("markdown") or ""
                if p["_id"] not in billets:
                    billets[p["_id"]] = p
                    nouveaux += 1
                if not os.path.exists(f"{V2}/tous-textes/{p['_id']}.md"):
                    open(f"{V2}/tous-textes/{p['_id']}.md", "w").write(md)
            if len(res) < 50:
                break
            off += 50
        print(nom, an, len(billets), flush=True)
etiq = dict(meta["etiquettes"]); etiq.update(NOUVELLES)
json.dump({"date_du_tirage": meta["date_du_tirage"], "date_complement": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "etiquettes": etiq, "etiquettes_ajoutees": NOUVELLES, "requete_complement": Q, "termes_complement": termes,
           "billets": list(billets.values())}, open(f"{V2}/metadonnees-v2.json", "w"), ensure_ascii=False)
manq = [i for i in billets if not os.path.exists(f"{V2}/tous-textes/{i}.md")]
print("billets v1", n_v1, "nouveaux", nouveaux, "total", len(billets), "sans texte", len(manq))
