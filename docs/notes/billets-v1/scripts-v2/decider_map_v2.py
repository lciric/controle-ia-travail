"""Variante : lit « identifiant|décision|motif » et prend le rôle apparie:<haut> dans /tmp/alire_map.json."""
import sys, json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from candidats_v2 import billets
J = "/home/user/controle-ia-travail/docs/notes/billets-v1/journal-tri-v2.jsonl"
m = json.load(open("/tmp/alire_map.json"))
for l in sys.stdin:
    l = l.strip()
    if not l: continue
    i, d, mo = l.split("|", 2)
    assert i in m and d in ("oui", "non") and len(mo.split()) <= 12, l
    open(J, "a").write(json.dumps({"identifiant": i, "annee": billets[i]["annee"], "role": "apparie:" + m[i],
        "decision": d, "motif": mo}, ensure_ascii=False) + "\n")
