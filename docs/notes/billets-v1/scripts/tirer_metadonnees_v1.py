"""Tâche 2, étape 1 : métadonnées de tous les billets portant au moins une des étiquettes
retenues, du 2022-01-01 au jour du tirage. Aucun texte ici. Sortie hors du dépôt."""
import json, datetime
from client_graphql_v1 import requete

ETIQUETTES = {  # identifiants trouvés par requête (tagBySlug et allTagsAlphabetical)
    "F5gRQdEQHzi3tQ5Ay": "AI Control",
    "aahN8N35xGokCKd4g": "Untrusted Monitoring",
    "56yXXrcxRjrQs6z9R": "Interpretability (ML & AI)",
    "cHoCqtfE9cF7aSs9d": "Deception",
    "KEAWfxwjitNJFrC68": "Deceptive Alignment",
    "mSTmKrSkFBswHaS3T": "Eliciting Latent Knowledge",
    "hMPBEPfDwSwoqYYAQ": "Sandbagging (AI)",
}
ANNEES = [2022, 2023, 2024, 2025, 2026]
Q = """query($t:JSON){ posts(input:{terms:$t}){ results{ _id title slug pageUrl postedAt baseScore
 voteCount commentCount wordCount question isEvent af draft user{displayName} coauthors{displayName}
 tags{_id name} } } }"""
SORTIE = "/home/user/billets-corpus-v1/metadonnees-v1.json"

if __name__ != "__main__":
    raise SystemExit  # import des constantes seulement
billets, requetes = {}, []
for tid, nom in ETIQUETTES.items():
    for an in ANNEES:
        off = 0
        while True:
            t = {"view": "top", "filterSettings": {"tags": [{"tagId": tid, "tagName": nom,
                 "filterMode": "Required"}]}, "after": f"{an}-01-01", "before": f"{an+1}-01-01",
                 "limit": 100, "offset": off}
            requetes.append(t)
            res = requete(Q, {"t": t})["posts"]["results"]
            for p in res:
                billets.setdefault(p["_id"], p)
            if len(res) < 100:
                break
            off += 100
        print(nom, an, off + len(res), flush=True)
json.dump({"date_du_tirage": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "etiquettes": ETIQUETTES, "requete": Q, "termes": requetes,
           "billets": list(billets.values())}, open(SORTIE, "w"), ensure_ascii=False)
print("billets uniques", len(billets))
