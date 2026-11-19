"""Quatrième calcul sur la première course (v1 et v2 intacts), demandé par la vérification du brouillon 2 (reste R1).
Même entrée, mêmes 395 couples d'actions honnêtes consécutives, mêmes régressions que la v2. Question : la part commune des
variations de l'agent et du jumeau dépend-elle de l'écart entre leurs contextes ? Corrélation des deux résidus par tiers de
l'écart absolu entre les deux coûts précédents (|log10 coût précédent du jumeau − log10 coût précédent de l'agent|), avec
intervalles par rééchantillonnage des épisodes ; et pente de la corrélation locale (produit des résidus réduits régressé sur l'écart)."""
import json, sys
import numpy as np

d = json.load(sys.stdin)
ep = {}
for a in d["actions"]:
    if a["phase"] == "etalonnage-honnete":
        ep.setdefault(a["episode"], {})[a["pas"]] = a
L = []
for e, p in sorted(ep.items()):
    for t in range(1, 10):
        a, b = p.get(t), p.get(t - 1)
        if a and b and a["H"] and b["H"] and b.get("cout_declare") and a.get("cout_declare") and b["reecrite"]:
            L.append((e, np.log10(b["H"]), np.log10(b["cout_declare"]), np.log10(a["H"]), np.log10(a["cout_declare"])))
E = np.array([l[0] for l in L]); M = np.array([l[1:] for l in L], dtype=float)
X = np.c_[M[:, 0], M[:, 1], np.ones(len(M))]
rj = M[:, 2] - X @ np.linalg.lstsq(X, M[:, 2], rcond=None)[0]
ra = M[:, 3] - X @ np.linalg.lstsq(X, M[:, 3], rcond=None)[0]
ecart = np.abs(M[:, 0] - M[:, 1])
bornes = np.quantile(ecart, [1 / 3, 2 / 3])
tiers = np.digitize(ecart, bornes)


def stat(i):
    s = []
    for k in range(3):
        j = i[tiers[i] == k]
        s.append(np.corrcoef(rj[j], ra[j])[0, 1] if len(j) > 5 else np.nan)
    z = (rj[i] / rj[i].std()) * (ra[i] / ra[i].std())
    pente = np.polyfit(ecart[i], z, 1)[0]
    return np.r_[s, s[2] - s[0], pente]


tout = stat(np.arange(len(M)))
rng = np.random.default_rng(np.random.SeedSequence(int(sys.argv[1])))
noms = sorted(set(E)); idx = {e: np.flatnonzero(E == e) for e in noms}
B = np.array([stat(np.concatenate([idx[noms[k]] for k in rng.integers(0, len(noms), len(noms))])) for _ in range(2000)])
print("bornes des tiers de l'ecart (decades)", np.round(bornes, 3), "| effectifs", [int((tiers == k).sum()) for k in range(3)],
      "| ecart median par tiers", [round(float(np.median(ecart[tiers == k])), 3) for k in range(3)])
for nom, v, b in zip(["correlation, tiers bas de l'ecart", "correlation, tiers moyen", "correlation, tiers haut",
                      "difference haut moins bas", "pente du produit des residus reduits sur l'ecart (par decade)"], tout, B.T):
    print(f"{nom} | valeur {v:.3f} | erreur type par episodes {np.nanstd(b):.3f} | intervalle a 95 % [{np.nanquantile(b, .025):.3f} ; {np.nanquantile(b, .975):.3f}]")
