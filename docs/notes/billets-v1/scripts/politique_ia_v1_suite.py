"""Tire la politique la plus récente vers laquelle renvoie la page de 2025 (tâche 1)."""
import json, datetime
from client_graphql_v1 import requete

DEST = "/home/user/controle-ia-travail/docs/sources/lesswrong-politique-ia-v1"
Q = """query($i:String){ post(input:{selector:{_id:$i}}){ result{ _id title slug postedAt
 modifiedAt pageUrl user{displayName} contents{ html markdown version editedAt } } } }"""
d = requete(Q, {"i": "nQWavk9mnwcv6ScMR"})["post"]["result"]
date = datetime.datetime.now(datetime.timezone.utc).isoformat()
open(f"{DEST}/nouvel-editeur-et-politique-llm-v1.html", "w").write(d["contents"]["html"])
open(f"{DEST}/nouvel-editeur-et-politique-llm-v1.md", "w").write(d["contents"]["markdown"])
meta = {k: v for k, v in d.items() if k != "contents"}
meta.update({"version_contenu": d["contents"]["version"], "contenu_edite_le": d["contents"]["editedAt"],
             "date_du_tirage": date, "requete": Q, "variables": {"i": "nQWavk9mnwcv6ScMR"}})
json.dump(meta, open(f"{DEST}/provenance-v1-suite.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: meta[k] for k in ("title", "postedAt", "pageUrl", "contenu_edite_le")}, ensure_ascii=False))
