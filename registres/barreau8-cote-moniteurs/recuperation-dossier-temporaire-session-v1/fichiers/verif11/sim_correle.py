"""Variante : effets de tâche CORRÉLÉS entre directions (et la sonde), facteur commun de corrélation rho = 0,9,
signe propre à chaque direction (une direction aléatoire lit l'axe commun avec un signe et un poids au hasard).
Tailles de la course. Mesure la fréquence d'échec de l'artefact positif (ii) sous (R) et sous (A)."""
import importlib.util, time
import numpy as np
spec = importlib.util.spec_from_file_location("sim_a0", __file__.replace("sim_correle.py", "sim_a0.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
T, A, NDIR, B = m.T, m.A, m.NDIR, m.B
RHO = 0.9

def une(regle, sigma, ss):
    r_dat, r_lab, r_boot, r_perm = [np.random.default_rng(s) for s in ss.spawn(4)]
    commun = r_dat.normal(size=(1, T, 1))
    poids = r_dat.normal(size=(NDIR + 1, 1, 1))          # poids aléatoire de chaque direction sur l'axe commun
    poids = poids / np.sqrt(np.mean(poids ** 2))
    eff = sigma * (np.sqrt(RHO) * poids * commun + np.sqrt(1 - RHO) * r_dat.normal(size=(NDIR + 1, T, 1)))
    x = (eff + r_dat.normal(size=(NDIR + 1, T, A))).astype(np.float32)
    lab = m.etiquettes(regle, r_lab)
    choix = r_boot.integers(0, T, size=(B, T))
    W = np.stack([np.bincount(c, minlength=T) for c in choix]).astype(np.float32)
    Cp = m.matrices_C(x[1:], lab); Ap_boot = m.aires_bootstrap(Cp, W, lab); Ap_point = m.aire_point(Cp, lab)
    s0 = x[0]; s = float(s0.std())
    out = {}
    for nom, v in {"sain": s0, "artefact": s0 + 2 * s * lab}.items():
        Cs = m.matrices_C(v[None].astype(np.float32), lab)[0]
        out[nom] = m.regle_au_dessus(Cs, Ap_boot, Ap_point, W, lab)
    return out

racine = np.random.SeedSequence(20261121)
for ir, regle in enumerate(("R", "A")):
    for js, sigma in enumerate((2.0, 4.0)):
        t0 = time.time(); ech = 0; sain = 0; bas = []; q = []
        for k in range(25):
            r = une(regle, sigma, np.random.SeedSequence(racine.entropy, spawn_key=(ir, js, k)))
            ech += int(not r["artefact"][0]); sain += int(r["sain"][0]); bas.append(r["artefact"][3]); q.append(r["artefact"][2])
        print(f"corrélé rho={RHO} règle {regle} sigma={sigma}: artefact (ii) ÉCHOUE {ech}/25 ; sain au-dessus {sain}/25 ; "
              f"q0,95 plancher moy {np.mean(q):.3f} max {np.max(q):.3f} ; borne basse D min {min(bas):.3f} moy {np.mean(bas):.3f} ; {time.time()-t0:.0f} s", flush=True)
