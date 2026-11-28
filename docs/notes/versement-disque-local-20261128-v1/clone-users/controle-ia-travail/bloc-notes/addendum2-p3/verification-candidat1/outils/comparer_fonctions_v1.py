"""Compare, par l'arbre syntaxique (ast, sans import), des fonctions de test entre fichiers.
Usage : python -I -B comparer_fonctions_v1.py <tests_v3> <tests_v4> <propose_g6> <extensions>"""
import ast
import sys

v3, v4, g6, ext = (open(p, encoding="utf-8").read() for p in sys.argv[1:5])


def fonctions(src):
    arbre = ast.parse(src)
    return {n.name: n for n in arbre.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}


f3, f4, fg6, fext = fonctions(v3), fonctions(v4), fonctions(g6), fonctions(ext)
print("fonctions v3 :", len(f3), "; v4 :", len(f4))
ajoutees = sorted(set(f4) - set(f3))
retirees = sorted(set(f3) - set(f4))
print("ajoutées :", ajoutees)
print("retirées :", retirees)
changees = [n for n in set(f3) & set(f4) if ast.dump(f3[n]) != ast.dump(f4[n])]
print("communes changées :", changees)
ref = {"test_garde_6_au_lancement_exception_du_chargeur_convertie": fg6,
       "test_garde_7_compte_de_chacune_des_cinq_formes": fext,
       "test_declencheur_3_E0_petit_non_nul": fext}
for n in ajoutees:
    src_ref = ref.get(n, {}).get(n) if n in ref else None
    if src_ref is None:
        print(n, ": AUCUNE RÉFÉRENCE")
        continue
    egal = ast.dump(f4[n]) == ast.dump(src_ref)
    seg4 = ast.get_source_segment(v4, f4[n])
    segr = ast.get_source_segment(g6 if n.startswith("test_garde_6") else ext, src_ref)
    print(n, ": arbre égal" if egal else ": ARBRE DIFFÉRENT", "; texte égal" if seg4 == segr else "; texte différent (commentaires ou espaces)")
    deco4 = [ast.dump(d) for d in f4[n].decorator_list]
    decor = [ast.dump(d) for d in src_ref.decorator_list]
    print("   décorateurs égaux :", deco4 == decor)
# hors fonctions : différences au niveau du module (imports, constantes, fixtures)
def hors_fonctions(src):
    return [ast.dump(n) for n in ast.parse(src).body if not isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
h3, h4 = hors_fonctions(v3), hors_fonctions(v4)
print("niveau module hors fonctions : v3", len(h3), "v4", len(h4), "; égaux sauf docstring :", h3[1:] == h4[1:])
print("docstring v3 == v4 :", h3[0] == h4[0])
