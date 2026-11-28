"""E1 bis (complement) — lecteur du texte scelle (bases (A) et (B), centres de tache sur les quinze conditions, plis scelles,
aucune action retiree) rejoue sur le contraste « facteur k contre consigne neutre » des donnees existantes. Mesure du
dispositif, hors de tout texte scelle : non opposable, n'entre dans aucun seuil."""
import importlib.util, json, pathlib, sys
from collections import defaultdict
import numpy as np
depot, D = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("mc", depot / "scripts" / "mots_et_cout_t06_v3.py")
mc = importlib.util.module_from_spec(spec); sys.modules["mc"] = mc; spec.loader.exec_module(mc)
from controle_ia.t06.cout import cout_lisible
from controle_ia.environnements.propositions import lire_action
from controle_ia.sondes.evaluation import aire_sous_courbe
plis = json.load(open(D / "issue-lecteur-du-texte-dose-reponse.json"))["plis"]
actions = []
for b in sorted((D / "blocs").iterdir()):
    txt = {d["cle"]: d["texte"] for d in map(json.loads, open(b / "textes.jsonl", encoding="utf-8"))}
    for m in map(json.loads, open(b / "mesures.jsonl", encoding="utf-8")):
        a = {k: m[k] for k in ("cle", "condition", "tache", "jetons", "cout", "valide") + mc.FORME_COUT}; a["texte"] = txt[m["cle"]]; actions.append(a)
centres = mc.centres_de_tache([a["tache"] for a in actions], [float("nan") if a["cout"] is None else float(a["cout"]) for a in actions], cout_lisible)
par = defaultdict(list)
for a in actions: par[a["condition"]].append(a)
def col(acts):
    c = lambda a: float("nan") if a.get("cout") is None else float(a["cout"])
    return {"tache": [a["tache"] for a in acts], "cout": np.array([c(a) for a in acts]), "jetons": np.array([int(a["jetons"]) for a in acts]),
            "valide": np.array([bool(a["valide"]) for a in acts]), **{k: np.array([bool(a[k]) for a in acts]) for k in mc.FORME_COUT}}
res = {}
for pos in ("gonfle_5", "gonfle_3", "gonfle_2", "gonfle_10"):
    acts = par[pos] + par["consigne_neutre"]; y = np.array([1] * len(par[pos]) + [0] * len(par["consigne_neutre"]))
    pli = np.array([plis[a["tache"]] for a in acts])
    XA, _ = mc.traits_base_a(col(acts), centres, cout_lisible)
    mots = [mc.mots_de(a["texte"]) for a in acts]; present = np.array([mc.cout_present(a["texte"], lire_action) for a in acts])
    sA, sB = np.full(len(acts), np.nan), np.full(len(acts), np.nan)
    for k in (0, 1):
        app, lu = np.flatnonzero(pli != k), np.flatnonzero(pli == k)
        m = mc.ajuster(XA[app], y[app], mc.TRAITS_A, mc.REGLAGES_A); sA[lu] = mc.noter(m, XA[lu], mc.TRAITS_A)
        vocab = mc.vocabulaire([mots[i] for i in app], 1000)
        X, noms = mc.matrice_b([mots[i] for i in app], XA[app][:, [0, 2, 3]], present[app], vocab)
        m = mc.ajuster(X, y[app], noms, mc.REGLAGES_B); Xl, _ = mc.matrice_b([mots[i] for i in lu], XA[lu][:, [0, 2, 3]], present[lu], vocab)
        sB[lu] = mc.noter(m, Xl, noms)
    res[f"{pos} contre consigne_neutre"] = {"aire_base_A": float(np.mean([aire_sous_courbe(sA[pli == k], y[pli == k]) for k in (0, 1)])),
                                            "aire_base_B": float(np.mean([aire_sous_courbe(sB[pli == k], y[pli == k]) for k in (0, 1)]))}
print(json.dumps(res, ensure_ascii=False, indent=1))
