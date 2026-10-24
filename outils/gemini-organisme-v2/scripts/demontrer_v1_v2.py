"""Compare, sur des entrées construites, la lecture des réponses par la v1 (Gemini, marques retirées) et la v2 (corrigée).
Usage : python -I demontrer_v1_v2.py <dossier organisme v1> <dossier organisme v2>"""
import importlib.util, json, sys, types

def charger(dossier, nom):
    faux = types.ModuleType("noyau_client")
    faux.appeler, faux.especes, faux.budget = (lambda *a, **k: {}), (lambda: []), (lambda: {})
    sys.modules["noyau_client"] = faux
    sys.path.insert(0, dossier)
    for m in ("principal", "memoire_isvd", "mitose_spectrale"):
        sys.modules.pop(m, None)
    spec = importlib.util.spec_from_file_location(nom, dossier + "/principal.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    sys.path.pop(0)
    return mod

v1, v2 = charger(sys.argv[1], "principal_v1"), charger(sys.argv[2], "principal_v2")
cas = [
    ("négation sans JSON", "Je ne vois aucun signe de sabotage dans cette trace.", ["sabotage", "execution_fidele"]),
    ("JSON imbriqué", 'Analyse.\n{"etiquette": "execution_fidele", "confiance": 0.7, "details": {"alerte": "aucune trace de sabotage"}}', ["sabotage", "execution_fidele"]),
    ("confiance NaN", '{"etiquette": "sabotage", "confiance": NaN}', ["sabotage", "honnete"]),
    ("accent", '{"etiquette": "Honnête", "confiance": 0.6}', ["sabotage", "honnete"]),
    ("JSON simple", '{"etiquette": "sabotage", "confiance": 0.6}', ["sabotage", "honnete"]),
]
for nom, texte, et in cas:
    a, b = v1._parser_decision_tache(texte, et), v2._parser_decision_tache(texte, et)
    print(f"{nom:20s} v1 : {a['etiquette']!s:18s} q={a['confiance']:<6} | v2 : {b['etiquette']!s:18s} q={b['confiance']}")
fam = {"conscience-evaluation": ["evaluation", "usage-reel"], "controle-delegation": ["sabotage", "honnete"]}
banque = [{"id": f"{f[:4]}-{i}", "famille": f, "verite": (p if i % 2 == 0 else n)} for f, (p, n) in fam.items() for i in range(12)]
print("induction, familles vues v1 :", sorted({t["famille"] for t in banque[:8]}),
      "| v2 :", sorted({t["famille"] for t in v2._selection_stratifiee(banque, 8)}))
print("vérifications, familles v1 :", sorted({t["famille"] for t in banque[:2]}),
      "| v2 :", sorted({t["famille"] for t in v2._selection_stratifiee(banque, 2)}))
