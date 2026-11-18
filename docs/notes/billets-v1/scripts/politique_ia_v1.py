"""Tire la page de politique du site sur les textes écrits avec une IA (tâche 1)."""
import json, datetime, os
from client_graphql_v1 import requete

DEST = "/home/user/controle-ia-travail/docs/sources/lesswrong-politique-ia-v1"
Q = """query($i:String){ post(input:{selector:{_id:$i}}){ result{ _id title slug postedAt
 modifiedAt pageUrl user{displayName} contents{ html markdown version editedAt } } } }"""
os.makedirs(DEST, exist_ok=True)
d = requete(Q, {"i": "KXujJjnmP85u8eM6B"})["post"]["result"]
date = datetime.datetime.utcnow().isoformat() + "Z"
open(f"{DEST}/politique-ecriture-llm-lesswrong-v1.html", "w").write(d["contents"]["html"])
open(f"{DEST}/politique-ecriture-llm-lesswrong-v1.md", "w").write(d["contents"]["markdown"])
meta = {k: v for k, v in d.items() if k != "contents"}
meta.update({"version_contenu": d["contents"]["version"], "contenu_edite_le": d["contents"]["editedAt"],
             "date_du_tirage": date, "requete": Q, "variables": {"i": "KXujJjnmP85u8eM6B"}})
json.dump(meta, open(f"{DEST}/provenance-v1.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(meta, ensure_ascii=False, indent=1))
