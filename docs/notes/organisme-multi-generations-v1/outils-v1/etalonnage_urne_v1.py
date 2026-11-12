"""Pourquoi le juge simplifié écarte l'urne : promotions, avec et sans le membre « urne » de la bibliothèque v1, de V3, V4 et
de trois fausses jugées sans archive, sur le dessin de la v67 (S-V1, m = 22), 300 répétitions — v1.

Concepteur neuf (Claude Opus 5.5), 12 novembre 2026. Aucun appel. Usage : `python3 -I -B etalonnage_urne_v1.py SORTIE.json`.
Comparer à la sortie publiée de la v67 (V3 617, V4 501, fausses sans archive 725 à 810 sur 1 000).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import monde_riche_outils_v1 as M
import puissance_monde_riche_v1 as P

if len(sys.argv) != 2 or os.path.exists(sys.argv[1]):
    sys.exit("usage : etalonnage_urne_v1.py SORTIE.json (neuf)")
R = 300
lois = (("V3", {"type": "transformee", "base": P.S_V1, "puissance": 0.08}, [P.K1_SV1]),
        ("V4", {"type": "melange", "composantes": [P.S_V1, P.UNIFORME], "poids": [0.15, 0.85]}, [P.K1_SV1]),
        ("F1-sans-archive", P.K1_SV1, []),
        ("F2-sans-archive", M.fausses_couvertes(P.K1_SV1)["F2-melee-uniforme"], []),
        ("F4-sans-archive", M.fausses_couvertes(P.K1_SV1)["F4-temperee-inclinee"], []))
out = {}
for urne in (False, True):
    c = {}
    for r in range(R):
        rng = P.rng_de("etal-urne", r)
        for nom, loi, arch in lois:
            ev = M.juger(loi, arch, P.S_V1, 2, 2, rng, avec_urne=urne)
            c[nom] = c.get(nom, 0) + bool(M.promue_hors_famille(ev, 22)[0])
    out["avec_urne" if urne else "sans_urne"] = {k: {"promues": v, "sur": R} for k, v in c.items()}
with open(sys.argv[1], "x", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
print(json.dumps(out, ensure_ascii=False))
