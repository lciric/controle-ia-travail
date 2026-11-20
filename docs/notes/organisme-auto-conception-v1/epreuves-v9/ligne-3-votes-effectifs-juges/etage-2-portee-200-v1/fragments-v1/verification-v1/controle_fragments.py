"""Contrôles mécaniques d'appoint sur le fichier de fragments (lecture seule).

Usage : python3 -I -B controle_fragments.py CHEMIN_FRAGMENTS
N'écrit rien ; imprime des relevés à relire à la main.
"""
import json
import re
import sys
from collections import Counter

chemin = sys.argv[1]
with open(chemin, encoding="utf-8") as f:
    d = json.load(f)

conf = d["conformes"]
faut = d["fautifs"]

print("== Comptes")
total_c = 0
for cat, lst in conf.items():
    c = Counter((x["citation"], x["piege"]) for x in lst)
    total_c += len(lst)
    print(cat, len(lst), dict(c))
print("conformes", total_c)
print("fautifs", len(faut))
print(Counter((x["item"], x["niveau"]) for x in faut))
print(Counter((x["item"], x["categorie"]) for x in faut))
ids = [x["id"] for lst in conf.values() for x in lst] + [x["id"] for x in faut]
print("identifiants uniques", len(set(ids)), "sur", len(ids))

annee = re.compile(r"\((?:[^()]*?)(1[89]\d\d|20\d\d)([^()]*)\)")


def textes(fr):
    return " ".join(fr["champs"].values())


print("\n== Citations : années entre parenthèses et marque")
for cat, lst in conf.items():
    for x in lst:
        t = textes(x)
        occ = annee.findall(t)
        nv = t.count("non vérifié")
        sans = [a for a, reste in occ if "non vérifié" not in reste]
        if x["citation"] and (nv == 0 or sans):
            print("CONFORME CITANT SANS MARQUE", x["id"], occ)
        if not x["citation"] and (occ or nv):
            print("CONFORME NON CITANT AVEC CITATION", x["id"], occ, nv)
for x in faut:
    t = textes(x)
    occ = annee.findall(t)
    sans = [a for a, reste in occ if "non vérifié" not in reste]
    print("FAUTIF", x["id"], x["item"], "citation=", x["citation"], "années:", [a for a, _ in occ], "sans marque:", sans)

print("\n== Conformes : mots à surveiller")
motifs = [
    r"vierge", r"\blibre\b", r"jamais (été )?étudi", r"nul n'a", r"personne n'a",
    r"inédit", r"descend", r"glouton", r"tronqu", r"actualis", r"meilleur de",
    r"décid", r"tranch", r"choisit", r"de son choix", r"seul", r"%",
    r"long terme", r"fournisseur", r"héritage", r"lègue",
]
for cat, lst in conf.items():
    for x in lst:
        t = textes(x)
        for m in motifs:
            for mm in re.finditer(m, t):
                a = max(0, mm.start() - 70)
                print(x["id"], "|", m, "|", t[a:mm.end() + 70].replace("\n", " "))

print("\n== Conformes : chiffres hors coût")
for cat, lst in conf.items():
    for x in lst:
        for k, v in x["champs"].items():
            if k == "cout":
                if "prédit" not in v:
                    print("COUT SANS PREDIT", x["id"], v)
                continue
            if re.search(r"\d", v):
                nums = re.findall(r"[\w.]*\d[\w.]*", v)
                print(x["id"], k, nums)
for x in faut:
    if "cout" in x["champs"] and "prédit" not in x["champs"]["cout"]:
        print("FAUTIF COUT SANS PREDIT", x["id"], x["champs"]["cout"])

print("\n== Modules : noms de la liste présents dans module_change")
liste = ["proposeurs", "aiguilleur", "mémoire anti-redite", "juges croisés", "bisociateur",
         "moisson de nouveauté", "juge statistique", "tests de mort", "sélection entre générations",
         "noyau et budget", "coffre", "dossier fermé", "témoins plantés"]
for cat_lst in [conf["modules"]] + [[x for x in faut if x["categorie"] == "modules"]]:
    for x in cat_lst:
        t = x["champs"]["module_change"].lower()
        trouves = [n for n in liste if n in t]
        print(x["id"], trouves)

print("\n== Voisins : identifiants aux deux formes")
forme = re.compile(r"(?:[a-zé-]+ n° \d+|\b\d{3}\.\d\b)", re.IGNORECASE)
for lst in [conf["voisins"], [x for x in faut if x["categorie"] == "voisins"]]:
    for x in lst:
        print(x["id"], forme.findall(x["champs"]["plus_proche_voisin"]))
