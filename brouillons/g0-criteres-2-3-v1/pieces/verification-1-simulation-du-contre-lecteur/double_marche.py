"""Vérification 1 : réponses à deux marches dont l'une est à la frontière consigne neutre / intensités (effet du gabarit ou
« tout ou rien » à la demande), et règle de gradation ancrée sur l'intensité 1,25. Fonctions du script v4 de l'auteur, inchangées."""
import hashlib, importlib.util, math, sys
import numpy as np
spec = importlib.util.spec_from_file_location("p", sys.argv[1]); p = importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
F = p.FACTEURS; A = p.AMPLIFICATION; H = p.EFFET_PREMIER_TEST
def vecteur(gonfle, neutre=0.0, presence=0.0):
    e = np.zeros(11); e[p.COL_N] = presence + neutre
    for c, g in zip(p.COL_INT, gonfle): e[c] = presence + g
    e[p.COL_D0] = presence; e[p.COL_P20] = presence + 0.2 * gonfle[-1]; e[p.COL_P50] = presence + 0.5 * gonfle[-1]
    return e
def sim(e, r, part, rng):
    v = p.SIGMA_D ** 2 / 2.0; ec = math.sqrt(part * v + (1 - part) * v / r)
    S = e + rng.normal(0.0, ec, size=(p.N_TACHES, e.size))
    dr1 = p.borne_basse(S[:, p.COL_HAUT] - S[:, p.COL_H], 0.95) > 0 and p.borne_basse(S[:, p.COL_HAUT] - S[:, p.COL_N], 0.95) > 0
    Xi = S[:, (p.COL_N,) + p.COL_INT]
    t = p.tendance(Xi, rng) < 0.05; inv = p.inversion_etablie(Xi, 1 - 0.05 / 6)
    auteur = any(p.borne_basse(S[:, m] - S[:, p.COL_N], 0.99) > 0 and p.borne_basse(S[:, p.COL_HAUT] - S[:, m], 0.99) > 0 for m in p.COL_INT[:-1])
    ancre = any(p.borne_basse(S[:, m] - S[:, p.COL_BAS], 1 - 0.05 / 4) > 0 and p.borne_basse(S[:, p.COL_HAUT] - S[:, m], 1 - 0.05 / 4) > 0 for m in p.COL_INT[1:-1])
    return dr1 and t and auteur and not inv, dr1 and t and ancre and not inv
sc = {
 "bosse-1.52-plus-0.5-a-10": [H]*5 + [H+0.5],
 "bosse-1.52-plus-1.0-a-10": [H]*5 + [H+1.0],
 "bosse-0.5-plus-1.0-des-5": [0.5]*4 + [1.5, 1.5],
 "bosse-1.0-plus-0.5-des-3": [1.0]*3 + [1.5]*3,
 "gabarit-neutre-0.3-sous-et-marche-1.52-a-10": "G",
 "exacte": [math.log10(k) for k in F],
 "saturation-des-3": [min(A*math.log10(k), H) for k in F],
 "double": [2*math.log10(k) for k in F],
}
racine = np.random.SeedSequence(20261124)
print("scenario\tpresence\tpart\tregle_auteur\tregle_ancree_1_25")
for nom, g in sc.items():
    for pres in (0.0, -0.32):
        for part in (0.0, 0.5):
            e = vecteur([0]*5 + [H], neutre=-0.3, presence=pres) if g == "G" else vecteur(g, presence=pres)
            cle = int.from_bytes(hashlib.sha256(f"{nom}|{pres}|{part}".encode()).digest()[:8], "big")
            rng = np.random.default_rng(np.random.SeedSequence(racine.entropy, spawn_key=(cle,)))
            a = b = 0; n = 400
            for _ in range(n):
                x, y = sim(e, 2, part, rng); a += x; b += y
            print(f"{nom}\t{pres}\t{part}\t{a/n:.3f}\t{b/n:.3f}"); sys.stdout.flush()
