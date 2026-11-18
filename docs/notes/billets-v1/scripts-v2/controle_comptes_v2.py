"""Écart de compte de l'étiquette contrôle de l'IA (mandat v2, tâche 2) : 411 billets rendus
contre 889 affichés. On compare plusieurs vues et pages, et le compteur de la fiche."""
import json
from collections import Counter
from client_graphql_v2 import requete
TID = "F5gRQdEQHzi3tQ5Ay"
Q = """query($t:JSON){ posts(input:{terms:$t}){ results{ _id postedAt baseScore draft isEvent question
 unlisted shortform status isFuture rejected frontpageDate curatedDate } } }"""
def tirer(view, pas=100, borne=3000, extra=None):
    out, off = {}, 0
    while off < borne:
        t = {"view": view, "filterSettings": {"tags": [{"tagId": TID, "tagName": "AI Control",
             "filterMode": "Required"}]}, "limit": pas, "offset": off}
        if extra: t.update(extra)
        r = requete(Q, {"t": t})["posts"]["results"]
        for p in r: out[p["_id"]] = p
        if len(r) < pas: break
        off += pas
    return out
res = {}
for v in ("top", "new", "magic"):
    r = tirer(v)
    res[v] = r
    print(v, len(r), sorted(Counter(p["postedAt"][:4] for p in r.values()).items()))
u = set().union(*[set(r) for r in res.values()])
print("union des vues", len(u))
# fiche de l'étiquette
f = requete("""query($s:String){ tags(input:{terms:{view:"tagBySlug", slug:$s}}){ results{ _id name postCount } } }""",
            {"s": "ai-control"})
print(f)
# relations étiquette-billet (compte de rels)
Q2 = """query($t:JSON){ tagRels(input:{terms:$t}){ results{ _id postId baseScore deleted } } }"""
for view in ("postsWithTag", "tagsOnPost"):
    pass
try:
    out, off = [], 0
    while off < 3000:
        r = requete(Q2, {"t": {"view": "postsWithTag", "tagId": TID, "limit": 200, "offset": off}})["tagRels"]["results"]
        out += r
        if len(r) < 200: break
        off += 200
    print("tagRels postsWithTag", len(out), "baseScore>0:", sum(1 for x in out if (x.get("baseScore") or 0) > 0),
          "baseScore<=0:", sum(1 for x in out if (x.get("baseScore") or 0) <= 0))
except Exception as e:
    print("tagRels", e)
