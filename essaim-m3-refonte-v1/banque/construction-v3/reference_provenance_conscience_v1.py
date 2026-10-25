"""Référence « provenance » de la famille `conscience-evaluation` — v1 (constat BC5-03 de
`contre-lectures/banque-v5-cl1/CONTRE-LECTURE-banque-v5-v1.md`).

Fait de structure, hérité de la v1 : la catégorie d'origine de chaque item (champ secret `category`) ne porte qu'une
classe, et la partition groupe par item, non par catégorie ; la plupart des tâches de `test` et de `test_final` ont donc
leur catégorie au train, avec la même classe. La référence de surface (une régression sur des traits de surface) ne
mesure pas ce canal. Ce script en donne trois mesures, apprises sur `train` seul :
1. **plus proche voisin** (le train comme mémoire) : pour chaque tâche, la classe de la tâche d'entraînement dont
   l'ensemble de mots (`[a-zà-ÿ0-9_]{2,}`, en minuscules) a l'indice de Jaccard le plus haut (égalité : la première) ;
   exactitude équilibrée par part ; **c'est la référence de provenance**, lisible par un organisme (il ne lit que ce qui est
   servi) ;
2. **borne « catégorie »** (oracle, lit le secret) : classe de la catégorie au train si elle y figure, sinon une chance sur
   deux ; exactitude équilibrée attendue ; ce n'est pas une règle servie, c'est une borne ;
3. les **comptes** : tâches dont la catégorie figure au train, ou non, par part et par classe.
Aucun texte ni identifiant n'est imprimé.

Usage : python3 -I reference_provenance_conscience_v1.py BANQUE SECRET
"""
import json, pathlib, re, sys

FAM = "conscience-evaluation"
b = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
s = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"))
mots = lambda t: set(re.findall(r"[a-zà-ÿ0-9_]{2,}", t.lower()))
jac = lambda a, c: len(a & c) / max(1, len(a | c))
pos, neg = "evaluation", "usage-reel"


def ee(pred, vrai):
    p = [i for i, v in enumerate(vrai) if v == pos]
    n = [i for i, v in enumerate(vrai) if v != pos]
    sens = sum(pred[i] == pos for i in p) / len(p) if p else 0.0
    spec = sum(pred[i] != pos for i in n) / len(n) if n else 0.0
    return round((sens + spec) / 2, 4)


tr = [t for t in b["train"] if t["famille"] == FAM]
Mtr = [mots(t["texte"]) for t in tr]
cat_train = {}
for t in tr:
    cat_train.setdefault(s[t["id"]].get("category"), set()).add(t["verite"])
sortie = {"banque": pathlib.Path(sys.argv[1]).name, "famille": FAM, "n_train": len(tr),
          "categories_a_une_seule_classe": all(len(v) == 1 for v in cat_train.values()), "parts": {}}
for p in ("test", "test_final"):
    te = [t for t in b[p] if t["famille"] == FAM]
    vrai = [t["verite"] for t in te]
    pred_ppv = []
    for t in te:
        js = [jac(mots(t["texte"]), m) for m in Mtr]
        j = max(range(len(js)), key=lambda k: (js[k], -k))
        pred_ppv.append(tr[j]["verite"])
    vue = [s[t["id"]].get("category") in cat_train for t in te]
    # borne « catégorie » : exactitude équilibrée attendue (une chance sur deux pour les catégories absentes du train)
    sens = []
    for classe in (pos, neg):
        idx = [i for i in range(len(te)) if vrai[i] == classe]
        ok = sum((1.0 if vue[i] and classe in cat_train[s[te[i]["id"]].get("category")] else (0.5 if not vue[i] else 0.0)) for i in idx)
        sens.append(ok / len(idx) if idx else 0.0)
    sortie["parts"][p] = {
        "n": len(te),
        "plus_proche_voisin": ee(pred_ppv, vrai),
        "borne_categorie_oracle": round(sum(sens) / 2, 4),
        "categorie_au_train": {"oui": sum(vue), "non": len(te) - sum(vue),
                                "non_par_classe": {c: sum(1 for i in range(len(te)) if not vue[i] and vrai[i] == c) for c in (pos, neg)}},
    }
sortie["reference_provenance"] = {p: sortie["parts"][p]["plus_proche_voisin"] for p in ("test", "test_final")}
print(json.dumps(sortie, ensure_ascii=False, indent=1))
