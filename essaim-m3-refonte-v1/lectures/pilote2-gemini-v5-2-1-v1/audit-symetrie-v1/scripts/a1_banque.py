"""Audit de symétrie, pilote 2 — structure de la banque, du fichier secret et de course/banque.json (lecture seule)."""
import json, sys, hashlib, collections

BANQ = "/home/claude/pilote3-v53-v6/essaim-m3-refonte-v1/banque/banque-confrontation-v1.json"
SECR = "/home/claude/pilote3-v53-v6/essaim-m3-refonte-v1/banque/banque-confrontation-v1-secret.json"
b = json.load(open(BANQ))
s = json.load(open(SECR))
print("manifeste:", json.dumps({k: v for k, v in b["manifeste"].items() if k != "provenance"}, ensure_ascii=False)[:1500])
print("provenance:", json.dumps(b["manifeste"].get("provenance"), ensure_ascii=False)[:1500])
print("secret type", type(s).__name__)
if isinstance(s, dict):
    for k, v in s.items():
        if isinstance(v, dict):
            ks = list(v.keys())
            print("secret", k, "dict", len(v), ks[:3], json.dumps(v[ks[0]], ensure_ascii=False)[:400] if ks else "")
        elif isinstance(v, list):
            print("secret", k, "list", len(v), json.dumps(v[0], ensure_ascii=False)[:400] if v else "")
        else:
            print("secret", k, str(v)[:200])
for part in ("train", "test", "test_final"):
    c = collections.Counter((t["famille"], t["source"], t["verite"]) for t in b[part])
    print(part, len(b[part]), sorted(c.items()))
    print("  ids exemple", [t["id"] for t in b[part][:6]])
for path in sys.argv[1:]:
    cb = json.load(open(path))
    same = {p: [ (x["id"], x["texte"], x["verite"]) for x in cb.get(p, [])] == [ (x["id"], x["texte"], x["verite"]) for x in b[p]] for p in ("train", "test", "test_final")}
    print(path, hashlib.sha256(open(path, "rb").read()).hexdigest(), list(cb.keys()), same)
