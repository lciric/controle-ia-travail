"""Contrôle : nombre de billets rendus par la requête étiquette sans borne de date, comparé au
compteur `postCount` du site, pour l'étiquette contrôle de l'IA (limite du tirage)."""
from collections import Counter
from client_graphql_v1 import requete

Q = """query($t:JSON){ posts(input:{terms:$t}){ results{ _id postedAt } } }"""
t = {"view": "top", "filterSettings": {"tags": [{"tagId": "F5gRQdEQHzi3tQ5Ay", "tagName": "AI Control",
     "filterMode": "Required"}]}, "limit": 2000}
r = requete(Q, {"t": t})["posts"]["results"]
print("rendus sans borne de date :", len(r))
print(sorted(Counter(p["postedAt"][:4] for p in r).items()))
