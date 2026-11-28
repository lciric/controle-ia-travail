"""Garde de l'issue : une analyse qui modifie l'issue de la lecture en cours de route est-elle arrêtée ?"""
import copy, json
from commun import A, B
from donnees import completer, lecture, G, reduire, P, _source
from controle_ia.gardes import GardeArret
reduire(n_aire=50, n_cout=200)
src = completer(_source(0)); lec = lecture(src)
vraie_b = B.analyse_a7
def a7_qui_touche_l_issue(d, c, p, lecture_, longueur):
    lecture_["issue"]["ligne"] = "organisme non établi"
    return vraie_b(d, c, p, lecture_, longueur)
B.analyse_a7 = a7_qui_touche_l_issue
l2 = copy.deepcopy(lec)
try:
    s = B.analyser_addendum(src, l2, G)
    print("B : aucun arrêt ; issue recopiée :", s["synthese"]["issue_primaire_inchangee"]["ligne"], "| issue d'origine :",
          lec["issue"]["ligne"][:40], "…")
except GardeArret as e:
    print("B : arrêt :", e)
B.analyse_a7 = vraie_b
vraie_a = A.FONCTIONS["A7"]
def a7a(e, D, g, k, p):
    D["lecture"]["issue"]["ligne"] = "organisme non établi"
    return vraie_a(e, D, g, k, p)
A.FONCTIONS["A7"] = a7a
try:
    A.analyser_addendum(src, copy.deepcopy(lec), G); print("A : aucun arrêt")
except GardeArret as e:
    print("A : arrêt :", e)
A.FONCTIONS["A7"] = vraie_a
# NaN dans la sortie : A arrête, B remplace par None
print("B _vers_json(nan) ->", B._vers_json({"x": float("nan")}))
try:
    A._propre({"x": float("nan")}); print("A : accepté")
except GardeArret as e:
    print("A _propre(nan) -> arrêt :", e)
