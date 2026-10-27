"""Vérifications du mécanisme (contre-lecteur) : échangeabilité sous l'ordre secret, T1b-fille sous l'ordre naturel,
égalités urne/marginale, garde du plan sur un cas sain. Aucune ligne de l'expérience n'est reproduite ici."""
import collections
import math
import random
import sys

sys.path.insert(0, sys.argv[1])
from pole import selection_pari as sp  # noqa: E402
from pole import controles_pari_v1 as cv1  # noqa: E402
from pole.controles_pari import _fixe, _frequences  # noqa: E402

print("--- 1. Sous l'ordre secret, la composition par position du plan est-elle plate (monde à dérive linéaire) ? ---")
rng = random.Random(99)
instances = sp.tirer_instances(rng, 200)
oracle, y = cv1.monde_structure(random.Random(1), "derive_lineaire", 200)
loi = oracle  # oracle « calendrier »
gele = sp.geler_engagement(sp.construire_engagement("h", loi, instances, 3, 0.05, sp.BIBLIOTHEQUE_STANDARD_V1, "continu",
                                                    plan_execution="ordre_secret"))
monde = {"type": "deterministe", "nombre_issues": 3, "issues": y}
# la même suite y, 300 ordres différents : la fréquence de l'issue 0 aux positions 0-39 et 160-199 du plan
debut, fin = collections.Counter(), collections.Counter()
for noyau in range(300):
    tir = sp.tirer_frais(gele, monde, 1, graine_noyau=noyau)
    x = tir["issues"]
    debut.update(x[:40])
    fin.update(x[160:])
n0 = 300 * 40
print(f"  y en ordre du temps : part de l'issue 0 dans les 40 premiers instants {y[:40].count(0)/40:.2f}, dans les 40 derniers {y[160:].count(0)/40:.2f}")
print(f"  x en ordre du plan (300 ordres) : part de l'issue 0 aux positions 0-39 {debut[0]/n0:.3f}, 160-199 {fin[0]/n0:.3f} (attendu {y.count(0)/200:.3f})")

print("--- 2. T1b-fille : sous l'ordre naturel, la fille est-elle la loi vraie sur la partie d'évaluation ? ---")
rng = random.Random(5)
p1 = sp.loi_softmax_aleatoire(rng, 3, 2)
horizon, c = 250, 50
inst = sp.tirer_instances(rng, horizon, 2)
derive = cv1._calendrier_derive_lineaire(rng, horizon)
poids = [0.5, 0.5]
monde = {"type": "melange", "composantes": [p1, derive], "poids": poids}
fille = {"type": "melange", "composantes": [p1, {"type": "calendrier", "probas": derive["probas"][c:]}], "poids": poids}
ecart = max(abs(a - b) for t in range(200) for a, b in zip(sp.proba(fille, inst[c + t], [], t), sp.proba(monde, inst[c + t], [], c + t)))
print(f"  écart maximal fille(t) − monde(c + t) sur les 200 instants d'évaluation : {ecart:.2e}")

print("--- 3. Urne et marginale ajustée : égalité sur une suite constante (bris d'égalité du membre dominant) ---")
x = [1] * 50
par = sp.trajectoires(sp.BIBLIOTHEQUE_STANDARD_V1, x, [None] * 50, 3)
den, dom = sp.trajectoire_denominateur(sp.BIBLIOTHEQUE_STANDARD_V1, x, [None] * 50, 3, deja=par)
print(f"  urne(50) = {par['urne'][-1]:.3f}, marginale(50) = {par['marginale_empirique'][-1]:.3f}, dominant final = {dom[-1]}")

print("--- 4. Garde du plan, cas sain et artefact, rejouée hors des essais ---")
tir = sp.tirer_frais(gele, monde if False else {"type": "deterministe", "nombre_issues": 3, "issues": y}, 1, graine_noyau=7)
ev = sp.evaluer(gele, tir, graine_noyau=7)
print(f"  cas sain : plan {ev['plan_execution']}, promue {ev['promue']}, log W max {ev['log_richesse_max']:.3f}")
try:
    sp.evaluer(gele, dict(tir, empreinte_ordre="0" * 64), graine_noyau=7)
    print("  ERREUR : artefact accepté")
except sp.PlanExecutionNonConforme as e:
    print(f"  artefact refusé : {e}")
# L'artefact « bonne empreinte, mauvais ordre » : des issues produites sous un autre ordre, mais l'empreinte copiée
autre = sp.tirer_frais(gele, {"type": "deterministe", "nombre_issues": 3, "issues": y}, 1, graine_noyau=8)
falsifie = dict(autre, empreinte_ordre=tir["empreinte_ordre"])
try:
    ev2 = sp.evaluer(gele, falsifie, graine_noyau=7)
    print(f"  issues produites sous l'ordre du noyau 8, empreinte de l'ordre 7 recopiée : ACCEPTÉ (promue {ev2['promue']}) — la garde ne vérifie qu'une déclaration")
except sp.PlanExecutionNonConforme as e:
    print(f"  refusé : {e}")

print("--- 5. Loi « composition » exacte sous v1 : log W_t ≤ 0 à chaque t sur 200 ordres (monde rupture) ---")
oracle, y = cv1.monde_structure(random.Random(3), "rupture", 200)
loi = {"type": "sans_remise", "composition": cv1.composition(y, 3)}
gele = sp.geler_engagement(sp.construire_engagement("h", loi, instances, 3, 0.05, sp.BIBLIOTHEQUE_STANDARD_V1, "continu",
                                                    plan_execution="ordre_secret"))
pire = -math.inf
for noyau in range(200):
    tir = sp.tirer_frais(gele, {"type": "deterministe", "nombre_issues": 3, "issues": y}, 1, graine_noyau=noyau)
    pire = max(pire, sp.evaluer(gele, tir, graine_noyau=noyau)["log_richesse_max"])
print(f"  log W max le plus haut sur 200 ordres : {pire:.3e}")

print("--- 6. Ordre secret avec le juge v1 sans urne : combien de nats la loi composition gagne-t-elle (rupture) ? ---")
gele0 = sp.geler_engagement(sp.construire_engagement("h", loi, instances, 3, 0.05, sp.BIBLIOTHEQUE_STANDARD, "continu",
                                                     plan_execution="ordre_secret"))
finals = []
for noyau in range(50):
    tir = sp.tirer_frais(gele0, {"type": "deterministe", "nombre_issues": 3, "issues": y}, 1, graine_noyau=noyau)
    finals.append(sp.evaluer(gele0, tir, graine_noyau=noyau)["log_richesse_finale"])
print(f"  log W final : min {min(finals):.3f}, max {max(finals):.3f} (seuil ln 20 = {math.log(20):.3f}) ; composition {cv1.composition(y, 3)}")
