"""Deux données de conception tirées de la première course du saboteur à budget (épisodes honnêtes de l'étalonnage), v1.
Entrée (sur l'entrée standard) : donnees/20261119-085912-iib-reel/oracle-iib-etalonnage.json, branche essai/iib-explo-v1,
sha256 606e327008b08396d94936b507dc81b68ea89bee8fa790631c2e48626a212d41.
(1) Dispersion, par action, du logarithme décimal des suites lisibles du jumeau (au moins cinq), premier pas et pas suivants.
(2) Sur quoi le jumeau s'ancre : régression du log10 de l'estimation du jumeau au pas t sur le log10 de son estimation au pas
t−1 (le coût réécrit présent dans son contexte) et sur le log10 du coût déclaré par l'agent au pas t−1 (absent de son contexte,
mais porté par le texte de l'agent) ; même régression pour le coût déclaré de l'agent au pas t. Erreurs types par rééchantillonnage
des lignes (grossier : les actions d'un épisode ne sont pas indépendantes)."""
import json, sys
import numpy as np

d = json.load(sys.stdin)
A = [a for a in d["actions"] if a["phase"] == "etalonnage-honnete"]


def dispersion(sel):
    sds, etendues = [], []
    for a in sel:
        s = [np.log10(x) for x in a["suites"] if x is not None and x > 0]
        if len(s) >= 5:
            s = np.array(s)
            sds.append(s.std(ddof=1))
            etendues.append(s.max() - s.min())
    q = lambda v: [round(float(np.quantile(v, p)), 3) for p in (0.25, 0.5, 0.75, 0.9)]
    return {"actions": len(sds), "ecart_type_q25_q50_q75_q90": q(sds), "etendue_q25_q50_q75_q90": q(etendues),
            "racine_moyenne_des_carres": round(float(np.sqrt(np.mean(np.square(sds)))), 3)}


print("premier pas", dispersion([a for a in A if a["pas"] == 0]))
print("pas suivants", dispersion([a for a in A if a["pas"] > 0]))

ep = {}
for a in A:
    ep.setdefault(a["episode"], {})[a["pas"]] = a
X, Y, Z = [], [], []
for p in ep.values():
    for t in range(1, 10):
        a, b = p.get(t), p.get(t - 1)
        if a and b and a["H"] and b["H"] and b.get("cout_declare") and a.get("cout_declare") and b["reecrite"]:
            X.append([np.log10(b["H"]), np.log10(b["cout_declare"]), 1.0])
            Y.append(np.log10(a["H"]))
            Z.append(np.log10(a["cout_declare"]))
X, Y, Z = np.array(X), np.array(Y), np.array(Z)
rng = np.random.default_rng(np.random.SeedSequence(int(sys.argv[1])) if len(sys.argv) > 1 else np.random.SeedSequence())
for nom, y in (("estimation du jumeau au pas t", Y), ("cout declare par l'agent au pas t", Z)):
    c = np.linalg.lstsq(X, y, rcond=None)[0]
    B = [np.linalg.lstsq(X[i], y[i], rcond=None)[0] for i in (rng.integers(0, len(y), len(y)) for _ in range(2000))]
    print(nom, "| lignes", len(y), "| coefficients [cout precedent du jumeau, cout precedent de l'agent, constante]", np.round(c, 3),
          "| erreurs types", np.round(np.std(B, 0), 3), "| ecart type du residu", round(float((y - X @ c).std()), 3))
print("correlation des deux couts precedents", round(float(np.corrcoef(X[:, 0], X[:, 1])[0, 1]), 3))
