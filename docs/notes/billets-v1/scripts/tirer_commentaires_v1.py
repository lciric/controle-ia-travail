"""Tâche 2, étape 4 : les dix commentaires au plus haut score de chaque billet bien noté
(vue postCommentsTop). Texte hors du dépôt, jamais affiché ici."""
import json, os
from client_graphql_v1 import requete

RACINE = "/home/user/billets-corpus-v1"
Q = """query($t:JSON){ comments(input:{terms:$t}){ results{ _id postId parentCommentId postedAt
 baseScore voteCount user{displayName} contents{ markdown } } } }"""
cl = json.load(open(f"{RACINE}/classement-v1.json"))
os.makedirs(f"{RACINE}/tous-commentaires", exist_ok=True)
sortie, termes = {}, []
for paire in cl["paires"]:
    pid = paire["haut"]
    t = {"view": "postCommentsTop", "postId": pid, "limit": 10}
    termes.append(t)
    res = requete(Q, {"t": t})["comments"]["results"]
    res = sorted(res, key=lambda c: -c["baseScore"])[:10]
    open(f"{RACINE}/tous-commentaires/{pid}.json", "w").write(json.dumps(res, ensure_ascii=False))
    sortie[pid] = [{k: c[k] for k in ("_id", "baseScore", "voteCount", "postedAt", "parentCommentId")}
                   for c in res]
json.dump({"requete": Q, "termes": termes, "commentaires": sortie},
          open(f"{RACINE}/commentaires-v1.json", "w"), ensure_ascii=False)
print("billets", len(sortie), "commentaires", sum(len(v) for v in sortie.values()))
