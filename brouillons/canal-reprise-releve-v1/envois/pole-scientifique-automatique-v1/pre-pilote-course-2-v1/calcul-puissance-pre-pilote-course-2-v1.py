"""Calculs de puissance du pré-pilote de la course 2 (brouillon 1). Processeur seul, aucune donnée de run.
Hypothèses déclarées dans le préenregistrement ; les tirages utilisent numpy.random.SeedSequence (R9).
Sortie : texte sur la sortie standard."""
import numpy as np
from scipy import stats

RACINE = 20261031  # entropie racine du calcul de puissance (sans lien avec celle du run)
def rng(nom):
    import hashlib
    cle = int.from_bytes(hashlib.sha256(nom.encode()).digest()[:8], "big")
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(cle,)))

N_P, N_NP = 10, 13           # fiches positives (6 squelettes) et négatives primaires C, A, V (8 squelettes) de l'ensemble des juges
N_PAIRES = 10                # squelettes rendus par les deux fournisseurs
def bloc_corr(g, p, n_app, n_simple, rho):
    x = []
    for _ in range(n_app):
        a = g.random() < p
        b = a if g.random() < rho else (g.random() < p)
        x += [a, b]
    for _ in range(n_simple):
        x.append(g.random() < p)
    return np.mean(x)

def regle_ba(se, sp, rho, n=20000, nom="ba"):
    """Règle S1 : BA_hat >= 0,80 et Se_hat >= 0,70 -> réussite ; BA_hat < 0,70 -> échec ; sinon non concluant."""
    g = rng(nom); r = e = 0
    for _ in range(n):
        se_h = bloc_corr(g, se, 4, 2, rho); sp_h = bloc_corr(g, sp, 5, 3, rho)
        ba = (se_h + sp_h) / 2
        r += (ba >= 0.80 and se_h >= 0.70); e += ba < 0.70
    return r / n, e / n, 1 - r / n - e / n

print("== Mesure 1, règle retenue (BA_hat >= 0,80 et Se_hat >= 0,70 ; échec si BA_hat < 0,70), corrélation intra-squelette rho ==")
for rho in (0.0, 0.6):
    for v in (0.95, 0.90, 0.85, 0.80, 0.70, 0.60):
        r, e, nc = regle_ba(v, v, rho, nom=f"ba{v}{rho}")
        print(f"  rho={rho:.1f}, Se=Sp vraie {v:.2f} : réussite {r:.2f}, non concluant {nc:.2f}, échec {e:.2f}")

print("== Mesure 2 : auto-préférence, différence appariée sur 10 squelettes rendus par les deux fournisseurs ==")
for sd in (1.0, 1.5, 2.0):
    se_ = sd / np.sqrt(N_PAIRES)
    for eff in (0.5, 1.0, 1.8):
        t = stats.t(df=N_PAIRES - 1)
        # puissance unilatérale à 5 % pour détecter eff (points sur 15), écart-type d'une différence appariée = sd
        pw = 1 - stats.nct.cdf(t.ppf(0.95), df=N_PAIRES - 1, nc=eff / se_)
        print(f"  sd appariée {sd:.1f} point : erreur-type {se_:.2f} ; puissance à effet {eff:.1f} point = {pw:.2f}")

print("== Mesure 5 : probabilité d'observer au moins un débordement parmi n fiches de Kimi ==")
for n in (10, 20):
    for p in (0.05, 0.10, 0.20, 0.30):
        print(f"  n={n}, taux vrai {p:.2f} : P(>=1) = {1-(1-p)**n:.2f}")
print("  borne haute à 95 % (Clopper-Pearson) si 0 sur n :", {n: round(stats.beta.ppf(0.95, 1, n), 3) for n in (10, 20)}, "(unilatérale)")

print("== Mesures 3 et 6 : bornes basses de Clopper-Pearson (unilatérales 95 %) si tout est détecté sur n ==")
for n in (8, 12, 17, 24, 34):
    print(f"  {n} détectés sur {n} : borne basse {stats.beta.ppf(0.05, n, 1):.2f}")
print("== Fausses alertes : borne haute si 0 sur n paires distinctes ==")
for n in (6, 12, 34, 180, 360):
    print(f"  0 sur {n} : borne haute {stats.beta.ppf(0.95, 1, n):.3f}")
print("== Aiguilleur : 12 détails concrets, rappel ==")
for r in (0.95, 0.90, 0.80):
    print(f"  rappel vrai {r:.2f} : P(12 sur 12) = {r**12:.2f} ; P(>=11 sur 12) = {1 - stats.binom.cdf(10, 12, r):.2f}")
