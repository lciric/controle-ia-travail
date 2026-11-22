from controle_ia.oracles_plantes_v5.parametres import charger
from controle_ia.oracles_plantes_v5.banque import construire_mondes, planter
from controle_ia.oracles_plantes_v5.normalisation import normaliser
from controle_ia.oracles_plantes_v5.tests_de_mort import profil, t5_redite, profils_egaux
from controle_ia.gardes import GardeArret
p,_ = charger()
ms = construire_mondes(24, p)
m = ms[4]
print("F2 monde 4 : M", m.M, "alpha", m.alpha, "beta", m.beta)
for x in m.perturbes: print("  perturbé alpha", x.alpha, "beta", x.beta)
try: planter(m, 24, p); print("planté ?!")
except GardeArret as e: print("ARRÊT :", e)
from controle_ia.oracles_plantes_v5.mondes import lit
ts = [f"pour tout t dans NAT, t >= 1 implique pfa_t(ET, t) >= {lit(m._ext[('fa', m.M)][1])}",
      f"pour tout t dans NAT, t >= 1 implique pfa_t(OU, t) >= {lit(m._ext[('fa', 1)][1])}",
      f"pour tout t dans NAT, t >= 1 implique prap_t(OU, t) >= {lit(m._ext[('rap', 1)][0])}"]
fs = [normaliser(m.analyser(t), m, m.ev) for t in ts]
for t, f in zip(ts, fs):
    pr = profil(f, m, 3 * m.N)
    print(t); print("   ", [ "".join(x) for x in pr])
print("redite 2 vs 1 :", t5_redite(fs[1], m, [fs[0]]).type.value, "; 3 vs 1 :", t5_redite(fs[2], m, [fs[0]]).type.value)
# autres mondes F2 de la même racine : ok ?
for w in (5, 6, 7):
    try: planter(ms[w], 24, p); print("monde", w, "planté")
    except GardeArret as e: print("monde", w, "ARRÊT", e)
