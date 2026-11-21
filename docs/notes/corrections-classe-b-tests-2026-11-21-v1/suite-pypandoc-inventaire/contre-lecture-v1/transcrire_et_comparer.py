"""Transcription indépendante du v3 par l'arbre syntaxique, comparée à un JSON d'inventaire (argument 2).
Arguments : chemin du v3, chemin du JSON."""
import ast
import json
import sys

v3, js = sys.argv[1], sys.argv[2]
arbre = ast.parse(open(v3, encoding="utf-8").read())
ns = {"COUVERT": "couvert", "EXEMPT": "exempté"}
cibles = {}
for n in arbre.body:
    if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
        nom = n.targets[0].id
        if nom in ("COUVERT", "EXEMPT", "REGISTRE", "LECTEURS_DE_CIBLES_ADMIS", "HORS_INVENTAIRE"):
            val = eval(compile(ast.Expression(n.value), v3, "eval"), {}, dict(ns))
            if nom in ("COUVERT", "EXEMPT"):
                ns[nom] = val
            cibles[nom] = val
reg = {k: [s, r] for k, (s, r) in cibles["REGISTRE"].items()}
lec = {k: sorted(v) for k, v in cibles["LECTEURS_DE_CIBLES_ADMIS"].items()}
hors = list(cibles["HORS_INVENTAIRE"])
doc = json.load(open(js, encoding="utf-8"))
reg4 = {k: [v["statut"], v["raison"]] for k, v in doc["registre"].items()}
lec4 = {k: sorted(v) for k, v in doc["lecteurs_de_cibles_admis"].items()}
hors4 = list(doc["hors_inventaire"])
print("v3 registre", len(reg), "lecteurs", len(lec), sum(map(len, lec.values())), "hors", hors)
print("json registre", len(reg4), "lecteurs", len(lec4), sum(map(len, lec4.values())), "hors", hors4)
print("statuts", doc["statuts"], "cles du document", sorted(doc))
print("registre identique", reg == reg4)
print("clés en trop dans json", sorted(set(reg4) - set(reg)))
print("clés manquantes dans json", sorted(set(reg) - set(reg4)))
print("valeurs différentes", sorted(k for k in set(reg) & set(reg4) if reg[k] != reg4[k]))
print("lecteurs identiques", lec == lec4)
print("hors identique", hors == hors4)
print("ordre du registre identique à v3", list(reg) == list(reg4), "ordre trié", list(reg4) == sorted(reg4))
print("couverts", sum(1 for v in reg.values() if v[0] == "couvert"), "exemptés", sum(1 for v in reg.values() if v[0] == "exempté"))
