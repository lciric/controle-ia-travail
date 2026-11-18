"""Consigne des décisions de tri : lignes « identifiant|oui ou non|motif » lues sur l'entrée
standard, ajoutées à journal-tri-v2.jsonl (identifiant, année, rôle, décision, motif)."""
import sys, json, datetime
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from candidats_v2 import billets
J = "/home/user/controle-ia-travail/docs/notes/billets-v1/journal-tri-v2.jsonl"
role = sys.argv[1]  # haut | apparie:<id du haut>
for l in sys.stdin:
    l = l.strip()
    if not l: continue
    i, d, m = l.split("|", 2)
    assert i in billets and d in ("oui", "non") and len(m.split()) <= 12, l
    open(J, "a").write(json.dumps({"identifiant": i, "annee": billets[i]["annee"], "role": role,
        "decision": d, "motif": m}, ensure_ascii=False) + "\n")
