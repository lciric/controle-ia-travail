"""Artefacts croisés : les artefacts de données de chaque candidat passés dans l'autre candidat (mêmes graines)."""
import copy, importlib.util, json, sys
import numpy as np
from commun import A, B, BASE
from donnees import G, reduire, lecture, P
from controle_ia.premier_test_ia import lecture as lp

def charger_tests(nom, chemin, module):
    sys.modules["complements_p3_v1"] = module
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec); sys.modules[nom] = m; spec.loader.exec_module(m)
    return m
TA = charger_tests("tests_a", BASE + "/candidat-a/test_complements_p3_v1.py", A)
TB = charger_tests("tests_b", BASE + "/candidat-b/test_complements_p3_v1.py", B)
reduire()

def reserves_a(src, lec):
    s = A.analyser_addendum(src, lec, G)
    return sorted({(r["reserve"], r["conclusion"]) for r in s["reserves_addendum"]})
def reserves_b(src, lec):
    s = B.analyser_addendum(src, lec, G)
    return sorted({(r["nom"], r["vise"], r["sonde"]) for r in s["synthese"]["reserves_addendum"]})

print("== artefacts du candidat A passés dans A et dans B ==")
for nom, f in TA.ARTEFACTS.items():
    reduire()
    src, lec, analyse, p, attendue = f()
    ra = [x for x in reserves_a(copy.deepcopy(src), copy.deepcopy(lec)) if x[0].startswith(f"reserve_{analyse}")]
    try:
        rb = [x for x in reserves_b(copy.deepcopy(src), copy.deepcopy(lec)) if x[0].startswith(f"reserve_{analyse}")]
    except Exception as e:
        rb = f"ARRÊT {type(e).__name__}: {e}"
    print(f"{nom:12s} attendue {attendue[0]} | A {ra} | B {rb}")

print("== artefacts du candidat B passés dans B et dans A ==")
attendus = {"a1_plancher": "reserve_A1", "a2_niveau": "reserve_A2", "a2_longueur": "reserve_A2", "a4_tranches": "reserve_A4_T4",
            "a4_confusion": "reserve_A4_T1", "a4_geometrique": "reserve_A4_T1", "a5_bornes": "reserve_A5",
            "a6_lecteur": "reserve_A6", "a7_fuite": "reserve_A7", "a7_correlation": "reserve_A7",
            "a8_debut": "reserve_A8_debut", "a8_saturation": "reserve_A8_saturation"}
for nom, pref in attendus.items():
    reduire()
    src = TB.SCENARIOS[nom](); lec = TB._lecture(src)
    rb = [x for x in reserves_b(copy.deepcopy(src), copy.deepcopy(lec)) if x[0].startswith(pref)]
    try:
        ra = [x for x in reserves_a(copy.deepcopy(src), copy.deepcopy(lec)) if x[0].startswith(pref)]
    except Exception as e:
        ra = f"ARRÊT {type(e).__name__}: {e}"
    print(f"{nom:15s} attendue {pref} | B {rb} | A {ra}")
