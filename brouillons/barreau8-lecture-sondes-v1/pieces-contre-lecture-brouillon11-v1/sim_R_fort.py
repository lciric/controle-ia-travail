"""Tailles de la course, règle (R) seule, effet de tâche fort (4 et 8 fois le bruit), 50 répétitions :
borne la fréquence d'échec de l'artefact positif (ii) sous (R) là où sa marge est la plus faible."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("sim_a0", __file__.replace("sim_R_fort.py", "sim_a0.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
import numpy as np, time
racine = np.random.SeedSequence(20261120)
for js, sigma in enumerate((4.0, 8.0)):
    t0 = time.time(); ech = 0; bas = []
    for k in range(50):
        ss = np.random.SeedSequence(racine.entropy, spawn_key=(0, js, k))
        r = m.une_repetition("R", sigma, ss)
        ech += int(not r["artefact"][0]); bas.append(r["artefact"][3])
    print(f"R sigma={sigma}: artefact (ii) ÉCHOUE {ech}/50 ; borne basse D min {min(bas):.3f} moy {np.mean(bas):.3f} ; {time.time()-t0:.0f} s", flush=True)
