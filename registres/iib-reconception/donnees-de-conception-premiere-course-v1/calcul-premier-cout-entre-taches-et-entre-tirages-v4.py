"""Cinquième calcul sur la première course : le premier coût honnête, entre tâches et entre tirages d'une même tâche.
Même entrée (oracle-iib-etalonnage.json, sha256 606e3270…), épisodes honnêtes de l'étalonnage, premier pas seulement.
Au premier pas, le contexte ne dépend que de la tâche : les suites du jumeau des épisodes d'une même tâche et les coûts déclarés
de ces épisodes sont des tirages honnêtes de la même loi. Tâche lue dans le nom de l'épisode (avant « /e »).
Rend : nombre de tâches, tirages par tâche ; écart type du log10 du premier coût entre tirages d'une même tâche (commun, par
analyse de variance à un facteur) et entre tâches (composante de variance) ; part de la variance portée par la tâche ;
quantiles de la loi des écarts d'un tirage à la médiane de sa tâche ; part de valeurs exactement égales à la médiane de la tâche ;
et, pour dimensionner un contrôle, écart type de la moyenne de m tirages d'une tâche."""
import json, sys
import numpy as np

d = json.load(sys.stdin)
par = {}
decl = {}
for a in d["actions"]:
    if a["phase"] == "etalonnage-honnete" and a["pas"] == 0:
        t = a["episode"].rsplit("/e", 1)[0]
        par.setdefault(t, []).extend(np.log10(x) for x in a["suites"] if x is not None and x > 0)
        if a.get("cout_declare"):
            decl.setdefault(t, []).append(np.log10(a["cout_declare"]))
taches = sorted(t for t in par if len(par[t]) >= 5)
n = np.array([len(par[t]) for t in taches])
moy = np.array([np.mean(par[t]) for t in taches])
sce_intra = sum(((np.array(par[t]) - np.mean(par[t])) ** 2).sum() for t in taches)
N, k = n.sum(), len(taches)
cm_intra = sce_intra / (N - k)
g = np.concatenate([par[t] for t in taches]).mean()
cm_inter = (n * (moy - g) ** 2).sum() / (k - 1)
n0 = (N - (n ** 2).sum() / N) / (k - 1)
var_inter = max(0.0, (cm_inter - cm_intra) / n0)
ecarts = np.concatenate([np.array(par[t]) - np.median(par[t]) for t in taches])
print("taches", k, "| tirages du jumeau par tache : min", int(n.min()), "mediane", int(np.median(n)), "max", int(n.max()),
      "| couts declares au premier pas", sum(len(v) for v in decl.values()))
print("ecart type entre tirages d'une meme tache (decades)", round(float(np.sqrt(cm_intra)), 3))
print("ecart type entre taches (composante de variance, decades)", round(float(np.sqrt(var_inter)), 3))
print("part de la variance portee par la tache", round(float(var_inter / (var_inter + cm_intra)), 3))
print("ecart d'un tirage a la mediane de sa tache : quantiles 5, 25, 50, 75, 95, 99 %",
      [round(float(np.quantile(ecarts, q)), 3) for q in (.05, .25, .5, .75, .95, .99)], "| part exactement a la mediane", round(float((ecarts == 0).mean()), 3))
dd = np.concatenate([np.array(decl[t]) - np.median(par[t]) for t in taches if t in decl])
print("cout declare honnete moins mediane des tirages de sa tache : n", len(dd), "| moyenne", round(float(dd.mean()), 3), "| ecart type", round(float(dd.std(ddof=1)), 3),
      "| quantiles 5, 50, 95 %", [round(float(np.quantile(dd, q)), 3) for q in (.05, .5, .95)])
for m in (1, 8, 16, 32):
    print(f"ecart type de la moyenne de {m} tirages d'une tache : {np.sqrt(cm_intra / m):.3f}")
