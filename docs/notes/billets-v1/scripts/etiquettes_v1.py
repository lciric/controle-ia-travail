"""Tâche 2 : recherche des identifiants d'étiquettes (requêtes d'abord passées à la main
au début de la session, consignées ici pour être rejouables). Écrit la liste complète des
étiquettes hors du dépôt et affiche les étiquettes retenues."""
import json, re
from client_graphql_v1 import requete

Q_SLUG = """query($s:String){ tags(input:{terms:{view:"tagBySlug", slug:$s}}){ results{ _id name slug postCount } } }"""
Q_TOUTES = """{ tags(input:{terms:{view:"allTagsAlphabetical", limit:5000}}){ results{ _id name slug postCount } } }"""
toutes = requete(Q_TOUTES)["tags"]["results"]
json.dump(toutes, open("/home/user/billets-corpus-v1/toutes-etiquettes.json", "w"))
print("étiquettes sur le site :", len(toutes))
print("contenant « probe » :", [t["name"] for t in toutes if re.search("probe", t["name"], re.I)])
for s in ["ai-control", "untrusted-monitoring", "interpretability-ml-and-ai", "deception",
          "deceptive-alignment", "eliciting-latent-knowledge", "sandbagging-ai"]:
    print(s, json.dumps(requete(Q_SLUG, {"s": s})["tags"]["results"]))
