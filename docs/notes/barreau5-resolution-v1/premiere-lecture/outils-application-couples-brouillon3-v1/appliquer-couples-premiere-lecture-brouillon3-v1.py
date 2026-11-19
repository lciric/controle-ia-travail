"""Applique, par recopie pure et dans l'ordre, les 17 couples du verificateur du brouillon 2 du texte neuf de la premiere
lecture du barreau 5 (couples-proposes-verification-v1.json, egaux a ceux du paragraphe 9 de
verification-corrections-brouillon2-v1.md, a7298fd2...) au texte et au devis brouillon 2 ; ecrit les brouillons 3 sous des
noms neufs (R12), sans jamais afficher le texte : n'imprime que des comptes et des empreintes.
Chaque « avant » doit paraitre une fois a son pas ; chaque « apres » une fois apres son pas ; sinon arret, rien n'est ecrit.
Usage : python3 -I -B appliquer-couples-premiere-lecture-brouillon3-v1.py <racine du depot>
"""
import hashlib
import json
import sys
from pathlib import Path

R = Path(sys.argv[1]).resolve()
PL = R / "docs/notes/barreau5-resolution-v1/premiere-lecture"
COUPLES = PL / "verification-outils-brouillon2-v1/couples-proposes-verification-v1.json"
SOURCES = {
    "texte": (R / "prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon2.md",
              R / "prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon3.md"),
    "devis": (PL / "devis-relecture-meme-chemin-v1-brouillon2.md",
              PL / "devis-relecture-meme-chemin-v1-brouillon3.md"),
}
ATTENDU = {"couples": "couples-proposes-verification-v1.json",
           "texte": "b346d5bd432a", "devis": None}


def h(b):
    return hashlib.sha256(b).hexdigest()


cible = {}
for genre, (src, dst) in SOURCES.items():
    if dst.exists():
        sys.exit(f"ARRET : {dst.name} existe deja ; on n'ecrase jamais (R12)")
    octets = src.read_bytes()
    print(f"{genre} source {src.name} sha256 {h(octets)}")
    cible[genre] = octets.decode("utf-8")
if not h(SOURCES["texte"][0].read_bytes()).startswith(ATTENDU["texte"]):
    sys.exit("ARRET : texte brouillon 2 a une autre empreinte que celle verifiee")

couples = json.loads(COUPLES.read_text(encoding="utf-8"))
print(f"couples {len(couples)} sha256 {h(COUPLES.read_bytes())}")
journal = []
for c in couples:
    t = cible[c["genre"]]
    n_av = t.count(c["avant"])
    if n_av != 1:
        sys.exit(f"ARRET : {c['id']} « avant » trouve {n_av} fois")
    t2 = t.replace(c["avant"], c["apres"], 1)
    n_ap = t2.count(c["apres"])
    if n_ap != 1:
        sys.exit(f"ARRET : {c['id']} « apres » trouve {n_ap} fois apres application")
    cible[c["genre"]] = t2
    journal.append((c["id"], c["genre"], n_av, n_ap))
for i, g, a, b in journal:
    print(f"  {i:5s} {g:6s} avant {a} -> apres {b}")
# controle final : chaque apres present une fois, chaque avant parti sauf s'il est contenu dans son apres
for c in couples:
    t = cible[c["genre"]]
    if t.count(c["apres"]) != 1 or (t.count(c["avant"]) != 0 and c["avant"] not in c["apres"]):
        sys.exit(f"ARRET : controle final en defaut pour {c['id']}")
for genre, (src, dst) in SOURCES.items():
    octets = cible[genre].encode("utf-8")
    dst.write_bytes(octets)
    print(f"{genre} ecrit {dst.name} sha256 {h(octets)} ({len(octets)} octets)")
