"""Corpus v2, commentaires : les dix commentaires au plus haut score (vue postCommentsTop) de
chaque billet bien noté retenu. Texte hors dépôt, jamais affiché."""
import json, os
sys_path = __import__("sys").path; sys_path.insert(0, __file__.rsplit("/", 1)[0])
from client_graphql_v2 import requete
V2 = "/home/user/billets-corpus-v2"
Q = """query($t:JSON){ comments(input:{terms:$t}){ results{ _id postId parentCommentId postedAt
 baseScore voteCount user{displayName} contents{ markdown } } } }"""
ap = json.load(open("/home/user/controle-ia-travail/docs/notes/billets-v1/appariements-v2.json"))
os.makedirs(f"{V2}/tous-commentaires", exist_ok=True)
sortie, termes = {}, []
for pid in ap:
    t = {"view": "postCommentsTop", "postId": pid, "limit": 10}
    termes.append(t)
    res = sorted(requete(Q, {"t": t})["comments"]["results"], key=lambda c: -c["baseScore"])[:10]
    open(f"{V2}/tous-commentaires/{pid}.json", "w").write(json.dumps(res, ensure_ascii=False))
    sortie[pid] = [{k: c[k] for k in ("_id", "baseScore", "voteCount", "postedAt", "parentCommentId")} for c in res]
json.dump({"requete": Q, "termes": termes, "commentaires": sortie}, open(f"{V2}/commentaires-v2.json", "w"), ensure_ascii=False)
print("billets", len(sortie), "commentaires", sum(len(v) for v in sortie.values()))
