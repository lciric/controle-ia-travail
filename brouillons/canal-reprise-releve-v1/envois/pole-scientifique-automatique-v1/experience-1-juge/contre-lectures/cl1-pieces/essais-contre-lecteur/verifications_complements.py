"""Compléments du contre-lecteur : (a) l'urne seule, sans ordre secret, suffit-elle ? (b) une loi qui utilise les traits,
sous un monde nul à dérive, est-elle bien tenue par le juge v1 ? (c) le champ plan_execution d'une ligne vient-il de
l'évaluation ou de la table des juges ? Petits effectifs (≤ 50), graine 1234 déclarée : rien de décisif."""
import random
import sys

sys.path.insert(0, sys.argv[1])
from pole import selection_pari as sp  # noqa: E402
from pole import controles_pari_v1 as cv1  # noqa: E402
from pole.outils import graine_derivee  # noqa: E402

G = 1234
print("--- (a) juge « v0 + urne, ordre naturel » (absent de l'expérience) sur l'oracle calendrier, 30 répétitions ---")
for structure in ("calendrier_deterministe", "derive_lineaire", "sinusoide"):
    promus = 0
    for r in range(30):
        rng = random.Random(graine_derivee(G, "a", structure, r))
        instances = sp.tirer_instances(rng, 200, 2)
        oracle, y = cv1.monde_structure(rng, structure, 200)
        gele = sp.geler_engagement(sp.construire_engagement("h", oracle, instances, 3, 0.05, sp.BIBLIOTHEQUE_STANDARD_V1,
                                                            "continu", plan_execution="ordre_naturel"))
        tir = sp.tirer_frais(gele, {"type": "deterministe", "nombre_issues": 3, "issues": y}, graine_derivee(G, "a", structure, r, "frais"))
        promus += sp.evaluer(gele, tir)["promue"]
    print(f"  {structure:24} : {promus}/30 promotions de l'oracle « calendrier » avec l'urne mais sans ordre secret")

print("--- (b) loi softmax aléatoire (utilise les traits) sous monde nul à dérive, juge v1, 50 répétitions par structure ---")
for structure in ("derive_lineaire", "marche_aleatoire", "calendrier_deterministe"):
    promus, pire = 0, -1e9
    for r in range(50):
        rng = random.Random(graine_derivee(G, "b", structure, r))
        loi = sp.loi_softmax_aleatoire(rng, 3, 2)
        instances = sp.tirer_instances(rng, 200, 2)
        _, y = cv1.monde_structure(rng, structure, 200)
        gele = sp.geler_engagement(sp.construire_engagement("h", loi, instances, 3, 0.05, sp.BIBLIOTHEQUE_STANDARD_V1,
                                                            "continu", plan_execution="ordre_secret"))
        noyau = graine_derivee(G, "b", structure, r, "noyau")
        tir = sp.tirer_frais(gele, {"type": "deterministe", "nombre_issues": 3, "issues": y}, graine_derivee(G, "b", structure, r, "frais"), graine_noyau=noyau)
        ev = sp.evaluer(gele, tir, graine_noyau=noyau)
        promus += ev["promue"]
        pire = max(pire, ev["log_richesse_max"])
    print(f"  {structure:24} : {promus}/50 promotions ; log W max {pire:.3f}")

print("--- (c) d'où vient le champ plan_execution d'une ligne du rapport ? ---")
import inspect  # noqa: E402
src = inspect.getsource(cv1._ligne)
print("  _ligne lit JUGES[juge]['plan_execution'] :", "JUGES[juge][\"plan_execution\"]" in src)
src2 = inspect.getsource(cv1._executer)
print("  _executer consigne ev['plan_execution'] :", "ev[\"plan_execution\"]" in src2)
