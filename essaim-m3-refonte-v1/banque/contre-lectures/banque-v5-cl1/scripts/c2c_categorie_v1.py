"""Contre-lecture de la v5 — c2c : famille conscience d'évaluation, champ secret `category` (catégorie de provenance du
jeu public) : pureté de classe par catégorie ; part des tâches de test et test final dont la catégorie est vue au train ;
règle « classe de la catégorie au train » (sinon hasard, compté 1/2). Comptes seulement, aucun nom ni identifiant.
Usage : python3 -I -B c2c_categorie_v1.py DOSSIER SORTIE"""
import collections, json, pathlib, sys
D = pathlib.Path(sys.argv[1]); SORTIE = pathlib.Path(sys.argv[2]); F = "conscience-evaluation"
v5 = json.loads((D / "banque-confrontation-v5.json").read_text(encoding="utf-8")); s5 = json.loads((D / "banque-confrontation-v5-secret.json").read_text(encoding="utf-8"))
cat = lambda t: s5[t["id"]].get("category")
toutes = collections.defaultdict(collections.Counter); autrain = collections.defaultdict(collections.Counter)
for p in ("train", "test", "test_final"):
    for t in v5[p]:
        if t["famille"] == F:
            toutes[cat(t)][t["verite"]] += 1
            if p == "train": autrain[cat(t)][t["verite"]] += 1
r = {"categories": len(toutes), "categories_pures": sum(len(c) == 1 for c in toutes.values()),
     "taille_max": max(sum(c.values()) for c in toutes.values()), "par_part": {}}
for p in ("test", "test_final"):
    te = [t for t in v5[p] if t["famille"] == F]; vues = [t for t in te if cat(t) in autrain]
    justes = sum(autrain[cat(t)].most_common(1)[0][0] == t["verite"] for t in vues)
    par_classe = {c: [t for t in te if t["verite"] == c] for c in ("evaluation", "usage-reel")}
    def ee_regle():
        s = []
        for c, lst in par_classe.items():
            s.append(sum((1.0 if autrain[cat(t)].most_common(1)[0][0] == t["verite"] else 0.0) if cat(t) in autrain else 0.5 for t in lst) / len(lst))
        return round(sum(s) / 2, 4)
    r["par_part"][p] = {"n": len(te), "categorie_vue_au_train": len(vues), "classe_egale_a_celle_du_train": justes,
                        "vues_par_classe": {c: sum(cat(t) in autrain for t in lst) for c, lst in par_classe.items()},
                        "esperance_ee_regle_categorie_sinon_hasard": ee_regle()}
SORTIE.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(r, ensure_ascii=False, indent=1))
