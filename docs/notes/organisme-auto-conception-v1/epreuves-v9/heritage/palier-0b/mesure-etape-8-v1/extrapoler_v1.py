"""Extrapolation des mesures de l'étape 8 (couche « essai-de-forme ») aux tailles gelées : 10 000 tirages par case du mode
« tirages », 200 000 sources par case du mode « sources ». Arguments : les fichiers JSON de résultat de `mesurer_etape_8_v2.py`.

Règles écrites (justification au rapport de mesure) :
- temps et place disque : modèle linéaire y = a + b × tirages + c × sources, ajusté par moindres carrés sur les mesures ; résidus
  rendus ;
- mémoire : la mémoire résidente maximale est rapportée au nombre d'entrées du cache de la loi exacte (plafond 200 000), par
  moindres carrés y = a + b × entrées ; extrapolée au plafond du cache.
"""

import json
import sys

import numpy as np

TIRAGES_GELES, SOURCES_GELEES, PLAFOND_DU_CACHE = 10_000, 200_000, 200_000
R = [json.load(open(f, encoding="utf-8")) for f in sys.argv[1:]]
t = np.array([r["tirages_par_case"] for r in R], dtype=float)
s = np.array([r["sources_par_case"] for r in R], dtype=float)
X = np.column_stack([np.ones_like(t), t, s])


def ajuster(y, nom, unite, echelle=1.0):
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    residus = y - X @ coef
    pred = coef @ np.array([1.0, TIRAGES_GELES, SOURCES_GELEES])
    print(f"{nom} : a = {coef[0] / echelle:.6g}, b (par tirage) = {coef[1] / echelle:.6g}, c (par source) = "
          f"{coef[2] / echelle:.6g} {unite} ; résidu absolu max {np.max(np.abs(residus)) / echelle:.4g} {unite} ; "
          f"aux tailles gelées : {pred / echelle:.6g} {unite} (dont tirages {coef[1] * TIRAGES_GELES / echelle:.6g}, "
          f"sources {coef[2] * SOURCES_GELEES / echelle:.6g})")


ajuster(np.array([r["duree_etape_8_s"] for r in R]), "temps", "s")
for cle in ("tirages", "sources", "manifeste"):
    ajuster(np.array([r["octets"][cle] for r in R], dtype=float), f"disque, {cle}", "Mo", 1e6)
ajuster(np.array([sum(r["octets"].values()) for r in R], dtype=float), "disque, total", "Go", 1e9)
e = np.array([r["cache_loi_exacte"]["currsize"] for r in R], dtype=float)
m = np.array([r["rss_max_apres_kio"] for r in R], dtype=float)
A = np.column_stack([np.ones_like(e), e])
coef, *_ = np.linalg.lstsq(A, m, rcond=None)
print(f"mémoire : RSS max = {coef[0]:.0f} Kio + {coef[1]:.2f} Kio par entrée du cache ; résidu absolu max "
      f"{np.max(np.abs(m - A @ coef)):.0f} Kio ; au plafond ({PLAFOND_DU_CACHE} entrées) : "
      f"{(coef[0] + coef[1] * PLAFOND_DU_CACHE) * 1024 / 1e9:.2f} Go")
print("entrées du cache par mesure :", [(int(a), int(b), int(c)) for a, b, c in zip(t, s, e)])
lt = np.log(t[s == s.min()])
le = np.log(e[s == s.min()])
k = np.polyfit(lt, le, 1)
print(f"croissance des entrées du cache : entrées ≈ {np.exp(k[1]):.4g} × tirages^{k[0]:.3f} ; plafond atteint vers "
      f"{np.exp((np.log(PLAFOND_DU_CACHE) - k[1]) / k[0]):.0f} tirages par case")
