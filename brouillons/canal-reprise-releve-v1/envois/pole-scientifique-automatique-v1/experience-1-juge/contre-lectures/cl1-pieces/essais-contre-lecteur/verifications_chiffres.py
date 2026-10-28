"""Vérifications arithmétiques du contre-lecteur (aucune lecture de résultat décisif)."""
import math
import sys

sys.path.insert(0, sys.argv[1])  # chemin de orchestrateur-pole-v2 (lecture seule)
from pole import selection_pari as sp  # noqa: E402
from pole.controles_pari import borne_wilson  # noqa: E402


def queue_binomiale_sup(n, p, seuil):
    """P(X > seuil) pour X ~ Binomiale(n, p), exact."""
    logs = []
    for x in range(seuil + 1, n + 1):
        logs.append(math.lgamma(n + 1) - math.lgamma(x + 1) - math.lgamma(n - x + 1) + x * math.log(p) + (n - x) * math.log(1 - p))
    m = max(logs)
    return math.exp(m) * sum(math.exp(v - m) for v in logs)


print("--- Section « Seuil » : P(plus de 50 promotions sur 1 000) ---")
for p in (0.02, 0.03, 0.04, 0.045, 0.05):
    print(f"  taux vrai {p:<6} : {queue_binomiale_sup(1000, p, 50):.3g}")

print("--- Gain de la loi « composition » (sans remise exacte) sur la marginale ajustée, fin de trajectoire ---")
for c in ((80, 60, 60), (60, 80, 60), (100, 50, 50), (67, 67, 66)):
    n = sum(c)
    urne = sum(math.lgamma(x + 1) for x in c) - math.lgamma(n + 1)
    mv = sum(x * math.log(x / n) for x in c if x)
    formule = 0.5 * (len(c) - 1) * math.log(2 * math.pi) + 0.5 * sum(math.log(x) for x in c) - 0.5 * math.log(n)
    print(f"  composition {c} : exact {urne - mv:.3f} nats ; formule de la note {formule:.3f} ; seuil ln 20 = {math.log(20):.3f}")

print("--- Même gain sur une suite permutée au hasard : le code (_traj_urne − _traj_marginale_mv) ---")
import random  # noqa: E402
rng = random.Random(4242)
y = [0] * 80 + [1] * 60 + [2] * 60
rng.shuffle(y)
urne = sp.trajectoire_membre({"nom": "urne", "type": "urne"}, y, [None] * 200, 3)
mv = sp.trajectoire_membre({"nom": "m", "type": "marginale_mv"}, y, [None] * 200, 3)
hyper = sp.trajectoire_loi({"type": "sans_remise", "composition": [80, 60, 60]}, y, [{"z": [0, 0], "g": 0}] * 200)
print(f"  urne(200) − marginale_mv(200) = {urne[-1] - mv[-1]:.3f} ; sans_remise(200) − urne(200) = {hyper[-1] - urne[-1]:.3e}")
print(f"  premier t où urne − marginale_mv ≥ ln 20 : {next(t + 1 for t, (u, m) in enumerate(zip(urne, mv)) if u - m >= math.log(20))}")
print(f"  croissance ≈ ln t ? urne−mv à t=50 : {urne[49]-mv[49]:.3f}, t=100 : {urne[99]-mv[99]:.3f}, t=200 : {urne[199]-mv[199]:.3f}")

print("--- Wilson : borne haute unilatérale à 95 % pour 50/1 000 et demi-largeur bilatérale ---")
print(f"  borne haute unilatérale (code) pour 50/1000 : {borne_wilson(50, 1000):.4f} (écart {borne_wilson(50, 1000) - 0.05:+.4f})")
print(f"  1,96·sqrt(0,05·0,95/1000) = {1.96 * math.sqrt(0.05 * 0.95 / 1000):.4f} ; 1,645·… = {1.645 * math.sqrt(0.05 * 0.95 / 1000):.4f}")

print("--- Graine de 128 bits : passe-t-elle par graine_derivee et random.Random ? ---")
from pole.outils import graine_derivee  # noqa: E402
g = (1 << 127) + 123456789
d = graine_derivee(g, "T1a|marginale", 0)
print(f"  graine_derivee(2^127+…, 'T1a|marginale', 0) = {d} ({d.bit_length()} bits) ; random.Random ok : {random.Random(d).random():.6f}")
