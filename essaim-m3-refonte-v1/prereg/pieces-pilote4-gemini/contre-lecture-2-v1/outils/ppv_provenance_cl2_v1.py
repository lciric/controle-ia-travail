"""Recalcul indépendant du plus proche voisin (référence de provenance) sur la banque seule, sans le secret — contre-lecture 2, v1.
Mots : [a-zà-ÿ0-9_]{2,} en minuscules ; Jaccard ; égalité : la première tâche d'entraînement ; exactitude équilibrée,
classe positive « evaluation ». Variante : égalité → la dernière, pour mesurer la sensibilité au départage.
N'imprime ni texte ni identifiant."""
import json, pathlib, re, sys
b = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
FAM = "conscience-evaluation"
def mots(t): return set(re.findall(r"[a-zà-ÿ0-9_]{2,}", t.lower()))
def jac(a, c): return len(a & c) / max(1, len(a | c))
def ee(pred, vrai, pos="evaluation"):
    p = [i for i, v in enumerate(vrai) if v == pos]; n = [i for i, v in enumerate(vrai) if v != pos]
    return round(((sum(pred[i] == pos for i in p) / len(p)) + (sum(pred[i] != pos for i in n) / len(n))) / 2, 4)
tr = [t for t in b["train"] if t["famille"] == FAM]; Mtr = [mots(t["texte"]) for t in tr]
print("parts :", {k: len(v) for k, v in b.items() if isinstance(v, list)})
print("familles par part :", {k: sorted({t["famille"] for t in v}) for k, v in b.items() if isinstance(v, list)})
print("train de la famille :", len(tr), "classes :", sorted({t["verite"] for t in tr}))
for p in ("test", "test_final"):
    te = [t for t in b[p] if t["famille"] == FAM]; vrai = [t["verite"] for t in te]
    pp, pd, egal = [], [], 0
    for t in te:
        js = [jac(mots(t["texte"]), m) for m in Mtr]; mx = max(js)
        ks = [k for k, x in enumerate(js) if x == mx]; egal += len(ks) > 1
        pp.append(tr[ks[0]]["verite"]); pd.append(tr[ks[-1]]["verite"])
    print(p, "n", len(te), "classes", {c: vrai.count(c) for c in sorted(set(vrai))}, "ppv (première)", ee(pp, vrai), "ppv (dernière)", ee(pd, vrai), "égalités", egal)
