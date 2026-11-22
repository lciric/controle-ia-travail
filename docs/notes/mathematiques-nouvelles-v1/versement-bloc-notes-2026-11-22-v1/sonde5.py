import numpy as np
from controle_ia.oracles_plantes_v1.parametres import charger
from controle_ia.oracles_plantes_v1.famille_f3 import MondeF3
from controle_ia.oracles_plantes_v1.normalisation import normaliser
from controle_ia.oracles_plantes_v1.tests_de_mort import t2_contre_exemple, appliquer_batterie, sortie_de_texte
P,_ = charger()
f3 = MondeF3.tirer(np.random.default_rng(7), P["familles"]["F3"], P["capacites"])
t = "pour tout n dans NAT, u(n + 2) != PU * u(n + 1) + QU * u(n)"
f = f3.analyser(t)
print(t2_contre_exemple(f, f3, forme=normaliser(f, f3, f3.ev)).type)
for t in ["u(1000) - u(1000) = 1", "u(1000) - u(1000) = 0", "pour tout n dans NAT, w(n - 1) * 0 = 0"]:
    r = appliquer_batterie(sortie_de_texte(t), f3)
    print(t, r.statut, r.vraie_bornee, r.triviale, [(i.test, i.type.value) for i in r.issues])
