"""Complément au calcul de l'ancrage (v1, intact), demandé par la contre-lecture du texte de l'organisme retenu (remarque M5).
Même entrée (oracle-iib-etalonnage.json, sha256 606e3270…), mêmes 395 couples d'actions honnêtes consécutives.
Ajoute : erreurs types par rééchantillonnage des ÉPISODES (unité indépendante), et corrélation des deux résidus (celui du jumeau,
celui de l'agent) : s'ils sont corrélés, les changements d'échelle d'une proposition à l'autre sont communs à l'agent et au jumeau."""
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


def stat(i):
    x, yj, ya = X[i], M[i, 2], M[i, 3]
    cj, ca = np.linalg.lstsq(x, yj, rcond=None)[0], np.linalg.lstsq(x, ya, rcond=None)[0]
    rj, ra = yj - x @ cj, ya - x @ ca
    return np.r_[cj[:2], ca[:2], np.corrcoef(rj, ra)[0, 1]]


tout = stat(np.arange(len(M)))
rng = np.random.default_rng(np.random.SeedSequence(int(sys.argv[1])))
noms = sorted(set(E)); idx = {e: np.flatnonzero(E == e) for e in noms}
B = np.array([stat(np.concatenate([idx[noms[k]] for k in rng.integers(0, len(noms), len(noms))])) for _ in range(2000)])
et = B.std(0); bas, haut = np.quantile(B, 0.025, 0), np.quantile(B, 0.975, 0)
for nom, v, s, b, h in zip(["jumeau : coefficient de son cout precedent", "jumeau : coefficient du cout precedent de l'agent",
                            "agent : coefficient du cout precedent du jumeau", "agent : coefficient de son cout precedent",
                            "correlation des deux residus"], tout, et, bas, haut):
    print(f"{nom} | valeur {v:.3f} | erreur type par episodes {s:.3f} | intervalle a 95 % [{b:.3f} ; {h:.3f}]")
print("episodes", len(noms), "| couples", len(M))
