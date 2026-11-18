"""Vérifie par programme chaque citation « … » de la grille : présence exacte dans le texte
(ou le titre) du billet nommé, ou dans le commentaire nommé, de la SEULE moitié
« développement » ; 25 mots au plus. Normalisation : liens markdown réduits à leur texte,
balises * _ \\ et espaces multiples ôtés."""
import json, re, sys

GRILLE = sys.argv[1]
RAC = "/home/user/billets-corpus-v1/developpement"
m = json.load(open("/home/user/controle-ia-travail/docs/notes/billets-v1/manifeste-corpus-v1.json"))
dev = {e["identifiant"]: e for e in m["billets"] if e["moitie"] == "developpement"}


def norm(t):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_\\]", "", t)
    return " ".join(t.split())


textes, coms = {}, {}
ok = ko = 0
for ligne in open(GRILLE):
    for ref, cit in re.findall(r"`([A-Za-z0-9]{17}(?:/[A-Za-z0-9]{17})?)`(?: \(\d+ mots\))? — « ([^»]+?) »", ligne):
        pid, _, cid = ref.partition("/")
        if pid not in dev:
            print("HORS DEVELOPPEMENT", ref); ko += 1; continue
        if cid:
            if pid not in coms:
                coms[pid] = {c["_id"]: norm(c["contents"]["markdown"]) for c in
                             json.load(open(f"{RAC}/commentaires/{pid}.json"))}
            src = coms[pid].get(cid, "")
        else:
            if pid not in textes:
                textes[pid] = norm(open(f"{RAC}/billets/{pid}.md").read()) + " || " + dev[pid]["titre"]
            src = textes[pid]
        c = norm(cit)
        n = len(c.split())
        if c in src and n <= 25:
            ok += 1
        else:
            ko += 1
            print("ECHEC", ref, n, "mots", "|", c[:90])
print("citations vérifiées :", ok, "échecs :", ko)
sys.exit(1 if ko else 0)
