"""Ordres de grandeur des coefficients des effets des mondes MR-1 étalonnés (douze mondes synthétiques, graines 100 à 111),
par classe et par type : étendue (max − min) du vecteur de pente ou de décalage. Sert d'aide chiffrée « estimée » dans la
consigne de Kimi (section 2 de la conception). Concepteur neuf (Claude Opus 5.5), 12 novembre 2026 ; aucun appel de modèle.
Lancement : `python3 -I -B normes_coefficients_v1.py` depuis ce dossier."""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, collections
import monde_riche_outils_v1 as M
acc = collections.defaultdict(list)
for g in range(100, 112):
    spec, c = M.generer_monde_synthetique(g, n_oracle=4000)
    for e in spec["effets"]:
        v = np.asarray(e.get("pente", e.get("decalage")))
        acc[(e["classe"], e["type"])].append(float(np.max(v) - np.min(v)))
for k in sorted(acc):
    a = np.array(acc[k]); print(k, len(a), "etendue (max-min) mediane", round(float(np.median(a)),2), "min", round(float(a.min()),2), "max", round(float(a.max()),2))
