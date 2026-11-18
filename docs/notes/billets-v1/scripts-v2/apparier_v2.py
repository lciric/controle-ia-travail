"""Appariement (règle v2, point 7). Sous-commandes :
  hauts AN            liste les billets bien notés retenus (15 premiers « oui ») de l'année
  voir HAUT           liste ordonnée des candidats apparié (état : non lu / oui / non)
  fixer HAUT APP|none consigne l'appariement et le nombre d'essais (état dans appariements-v2.json)
"""
import sys, json, os
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from candidats_v2 import *
D = "/home/user/controle-ia-travail/docs/notes/billets-v1"
def journal():
    return [json.loads(l) for l in open(f"{D}/journal-tri-v2.jsonl")]
def retenus(an):
    out = []
    for l in journal():
        if l["role"] == "haut" and l["annee"] == an and l["decision"] == "oui" and len(out) < 15:
            out.append(l["identifiant"])
    return out
def etat():
    j = journal(); e = {}
    for l in j:
        if l["role"].startswith("apparie") or l["role"] == "haut":
            e[l["identifiant"]] = l["decision"]
    return e
AP = f"{D}/appariements-v2.json"
ap = json.load(open(AP)) if os.path.exists(AP) else {}
cmd = sys.argv[1]
if cmd == "hauts":
    an = int(sys.argv[2]); r = retenus(an)
    print(len(r), r)
elif cmd == "voir":
    h = billets[sys.argv[2]]; e = etat()
    pris = {v["apparie"] for v in ap.values() if v["apparie"]}
    # « non » tous rôles confondus ; un « oui » apparié-lu reste candidat
    faux = {i for i, d in e.items() if d == "non"}
    c = viviers_apparies(h, pris, faux)
    print(f"haut {h['_id']} {h['title'][:60]} mots={h['mots']} etiq={h['etiq'][:3]} ; viviers={len(c)}")
    for x in c[:10]:
        print(" ", x["_id"], x["baseScore"], x["mots"], "v1heur" if heuristique_v1(x["_id"]) else "-", e.get(x["_id"], "non lu"), x["title"][:55])
elif cmd == "fixer":
    h, a = sys.argv[2], sys.argv[3]
    ap[h] = {"apparie": None if a == "none" else a, "essais": int(sys.argv[4]) if len(sys.argv) > 4 else None, "annee": billets[h]["annee"]}
    json.dump(ap, open(AP, "w"), ensure_ascii=False, indent=0)
if cmd == "tour":
    an = int(sys.argv[2]); e = etat(); a_lire = []
    essais = {}
    for l in journal():
        if l["role"].startswith("apparie:"):
            essais[l["role"][8:]] = essais.get(l["role"][8:], 0) + 1
    for h in retenus(an):
        if h in ap: continue
        pris = {v["apparie"] for v in ap.values() if v["apparie"]}
        faux = {i for i, d in e.items() if d == "non"}
        n = essais.get(h, 0)
        # un « oui » lu pour ce haut et resté libre, ou lu pour un autre et libre
        trouve = False
        for c in viviers_apparies(billets[h], pris, faux):
            if e.get(c["_id"]) == "oui":
                ap[h] = {"apparie": c["_id"], "essais": n + 1, "annee": an}; trouve = True; break
            if n >= 3: break
            a_lire.append((h, c["_id"], n + 1)); trouve = True; break
        if not trouve and h not in ap:
            ap[h] = {"apparie": None, "essais": n, "annee": an}
        if h not in ap and n >= 3:
            ap[h] = {"apparie": None, "essais": n, "annee": an}
        json.dump(ap, open(AP, "w"), ensure_ascii=False, indent=0)
    print("à lire :", " ".join(f"{c}(h={h[:5]},essai{k})" for h, c, k in a_lire))
    print("fixés :", sum(1 for h in retenus(an) if h in ap), "sur", len(retenus(an)))
    open("/tmp/alire.txt", "w").write(" ".join(c for _, c, _ in a_lire))
    m = {}
    for h, c, _ in a_lire: m.setdefault(c, h)
    open("/tmp/alire_map.json", "w").write(json.dumps(m))
