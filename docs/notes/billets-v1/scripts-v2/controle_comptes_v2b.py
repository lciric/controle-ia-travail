"""Suite : quelles relations étiquette-billet n'apparaissent pas dans la vue des billets ?"""
import json
from collections import Counter
from client_graphql_v2 import requete
TID = "F5gRQdEQHzi3tQ5Ay"
Q2 = """query($t:JSON){ tagRels(input:{terms:$t}){ results{ _id postId baseScore post{ _id postedAt baseScore
 draft isEvent question unlisted status rejected isFuture authorIsUnreviewed deletedDraft } } } }"""
out, off = [], 0
while True:
    r = requete(Q2, {"t": {"view": "postsWithTag", "tagId": TID, "limit": 200, "offset": off}})["tagRels"]["results"]
    out += r
    if len(r) < 200: break
    off += 200
ids = {x["postId"] for x in out}
print("relations", len(out), "billets", len(ids))
json.dump(out, open("/home/user/billets-corpus-v2/tagrels-ai-control.json", "w"))
