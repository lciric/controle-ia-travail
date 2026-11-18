"""Tâche 2, étape 2 : texte (markdown) de tous les billets des métadonnées, par les mêmes
requêtes étiquette × année, 50 par page. Texte hors du dépôt, jamais affiché ici."""
import json, os
from client_graphql_v1 import requete
ANNEES = [2022, 2023, 2024, 2025, 2026]

DOSSIER = "/home/user/billets-corpus-v1/tous-textes"
Q = """query($t:JSON){ posts(input:{terms:$t}){ results{ _id contents{ markdown version } } } }"""
os.makedirs(DOSSIER, exist_ok=True)
meta = json.load(open("/home/user/billets-corpus-v1/metadonnees-v1.json"))
voulus = {p["_id"] for p in meta["billets"]}
faits = {f[:-3] for f in os.listdir(DOSSIER)}
termes = []
for tid, nom in meta["etiquettes"].items():
    for an in ANNEES:
        off = 0
        while True:
            t = {"view": "top", "filterSettings": {"tags": [{"tagId": tid, "tagName": nom,
                 "filterMode": "Required"}]}, "after": f"{an}-01-01", "before": f"{an+1}-01-01",
                 "limit": 50, "offset": off}
            termes.append(t)
            res = requete(Q, {"t": t})["posts"]["results"]
            for p in res:
                if p["_id"] in voulus and p["_id"] not in faits:
                    md = (p.get("contents") or {}).get("markdown") or ""
                    open(f"{DOSSIER}/{p['_id']}.md", "w").write(md)
                    faits.add(p["_id"])
            if len(res) < 50:
                break
            off += 50
        print(nom, an, len(faits), flush=True)
json.dump({"requete": Q, "termes": termes}, open("/home/user/billets-corpus-v1/requetes-textes-v1.json", "w"))
print("textes", len(faits), "manquants", len(voulus - faits))
