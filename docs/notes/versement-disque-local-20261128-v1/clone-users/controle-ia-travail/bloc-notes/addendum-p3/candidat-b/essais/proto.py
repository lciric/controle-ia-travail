import json, sys, time
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
sys.path.insert(0, "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3/candidat-b")
import numpy as np
from test_premier_test_ia_lecture import _source, _graines, P, L
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.premier_test_ia.notation import agreger_par_jeton
from controle_ia.manifeste import graines
import complements_p3_v1 as cp
lp.TIRAGES_AIRE = 300; lp.TIRAGES_COUT = 2000
cp.TIRAGES_AIRE = 200; cp.TIRAGES_COUT = 2000
G = graines(cp.cles_addendum(P), cp.ENTROPIE_P3)

def plancher_par_tache(src, tau, conds=("saboteur",)):
    t = src["tables"]
    taches = sorted(set(t["tache"].tolist()), key=lambda x: int(x[1:]))
    for k, ta in enumerate(taches):
        m = (t["tache"] == ta) & np.isin(t["condition"], conds)
        t["scores"][np.ix_(m, np.arange(2, t["scores"].shape[1]))] += tau if k % 2 == 0 else -tau
    return src

def run(src):
    lec = json.loads(json.dumps(lp.lire(src, _graines())))
    s = cp.analyser_addendum(src, lec, G)
    return lec, s

mode = sys.argv[1]
if mode == "a1":
    for d in (1.0, 1.2, 1.5):
        for tau in (2.0, 3.0):
            src = plancher_par_tache(_source(21, d=d), tau)
            lec, s = run(src)
            e = s["analyses"]["A1"][P[0]]["descriptif"]["saboteur-honnete"]
            print(d, tau, lec["etats_des_jeux"][P[0]]["saboteur-honnete"], round(e["aire"],3), round(e["plancher_quantile"],3), round(e["ecart_bas"],3),
                  [ (r["nom"], r["vise"]) for r in s["synthese"]["reserves_addendum"] if r["sonde"] == P[0]][:4])

def recalculer(src):
    t, j = src["tables"], src["jetons"]
    for r in range(j["rang"].size):
        deb, lon = int(j["debut"][r]), int(j["longueur"][r])
        for k in range(2):
            s = j[f"scores_{k}"][deb:deb + lon]
            lg = j[f"logits_{k}"][deb:deb + lon]
            t["scores"][int(j["rang"][r]), k] = agreger_par_jeton(s, None if np.all(np.isnan(lg)) else lg)
    return src

def jetons_modifies(src, f, seed=0):
    """f(rng, condition, k, s, lg) modifie en place les scores (et logits) par jeton d'une action."""
    rng = np.random.default_rng(seed)
    t, j = src["tables"], src["jetons"]
    for r in range(j["rang"].size):
        deb, lon = int(j["debut"][r]), int(j["longueur"][r])
        c = t["condition"][int(j["rang"][r])]
        for k in range(2):
            f(rng, c, k, j[f"scores_{k}"][deb:deb + lon], j[f"logits_{k}"][deb:deb + lon])
    return recalculer(src)

def show(s, lec, a, p=P[0]):
    print(a, "T2", lec["intention"][p]["T2"].get("etabli"), lec["intention"][p]["T2"].get("bas"),
          [(r["nom"], r["motif"][:90]) for r in s["synthese"]["reserves_addendum"] if r["sonde"] == p and r["nom"].startswith("reserve_A2")])

if mode == "a2":
    def niveau(rng, c, k, s, lg):
        if c == "saboteur":
            s[0:20] -= 1.0
    src = jetons_modifies(_source(31, signal="aucun"), niveau)
    lec, s = run(src); show(s, lec, "niveau")
    for po, dd in ((0.05, 1.0), (0.08, 1.0), (0.1, 1.5)):
        def longueur(rng, c, k, s, lg, po=po, dd=dd):
            if c == "saboteur":
                s += dd
            s += 10.0 * (rng.random(s.size) < po)
        src = jetons_modifies(_source(32, signal="aucun"), longueur)
        lec, s = run(src)
        b = s["analyses"]["A2"][P[0]]["descriptif"]
        show(s, lec, f"longueur {po} {dd}")
        print("   a", round(b["a_aire_cout"]["bas"], 3), "b", round(b["b_fenetre_meme_longueur"]["bas"], 3), round(b["b_fenetre_meme_longueur"]["difference_moyenne_des_repliques"], 3))

if mode == "a2b":
    for po, dd, seed in ((0.03, 1.0, 32), (0.04, 1.0, 32), (0.04, 1.2, 32), (0.05, 1.2, 32), (0.04, 1.0, 33)):
        def longueur(rng, c, k, s, lg, po=po, dd=dd):
            if c == "saboteur":
                s += dd
            s += 10.0 * (rng.random(s.size) < po)
        src = jetons_modifies(_source(seed, signal="aucun"), longueur)
        lec, s = run(src)
        b = s["analyses"]["A2"][P[0]]["descriptif"]
        show(s, lec, f"longueur {po} {dd} {seed}")
        print("   a", round(b["a_aire_cout"]["bas"], 3), "b", round(b["b_fenetre_meme_longueur"]["bas"], 3))

def base_par_tache(t):
    return {ta: float(t["cout"][(t["tache"] == ta) & (t["condition"] == "honnete")][0]) for ta in np.unique(t["tache"])}

if mode == "a4b":
    # confusion entre tâches : la moitié des tâches gonfle souvent (0,9), l'autre rarement (0,1) ; la sonde lit la tâche
    src = _source(41, signal="aucun")
    t = src["tables"]; base = base_par_tache(t); rng = np.random.default_rng(7)
    hautes = {ta for k, ta in enumerate(sorted(base, key=lambda x: int(x[1:]))) if k % 2 == 0}
    sab = np.flatnonzero(t["condition"] == "saboteur")
    for i in sab:
        g = rng.random() < (0.9 if t["tache"][i] in hautes else 0.1)
        t["cout"][i] = base[t["tache"][i]] * (3.0 if g else 1.0)
    t["cout_groupes_joints"] = t["cout"].copy()
    def tache(rng, c, k, s, lg): pass
    j = src["jetons"]
    for r in sab:
        if t["tache"][r] in hautes:
            for k in range(2):
                j[f"scores_{k}"][r * L + 0:r * L + 5] += 2.0
                if k == 1: j["logits_1"][r * L:r * L + 5] += 2.0
    recalculer(src)
    lec, s = run(src)
    i = lec["intention"][P[0]]
    print("T1", i["T1"].get("etabli"), i["T1"].get("bas"), i["T1"].get("plancher_quantile"))
    print(json.dumps(s["analyses"]["A4"][P[0]]["descriptif"]["b_T1_intra_tache"], ensure_ascii=False)[:400])
    print([(r["nom"], r["vise"], r["motif"][:100]) for r in s["synthese"]["reserves_addendum"] if r["sonde"] == P[0]])

if mode == "a4c":
    # référence honnête géométrique : une action honnête aberrante par tâche (× 10^3,98) ; le saboteur gonfle × 3 (signal
    # au champ du coût) ou × 8 (sans signal) ; médiane : × 3 et × 8 gonflent ; géométrique (× 2,5) : seul × 8 gonfle
    src = _source(51, signal="aucun")
    t = src["tables"]; base = base_par_tache(t); rng = np.random.default_rng(8); j = src["jetons"]
    for ta in base:
        h = np.flatnonzero((t["tache"] == ta) & (t["condition"] == "honnete"))
        t["cout"][h[0]] = base[ta] * 10 ** 3.98
    for i in np.flatnonzero(t["condition"] == "saboteur"):
        u = rng.random()
        f = 3.0 if u < 0.4 else 8.0 if u < 0.7 else 1.0
        t["cout"][i] = base[t["tache"][i]] * f
        if f == 3.0:
            for k in range(2):
                j[f"scores_{k}"][i * L + 20:i * L + 25] += 2.0
            j["logits_1"][i * L + 20:i * L + 25] += 2.0
    t["cout_groupes_joints"] = t["cout"].copy()
    recalculer(src)
    lec, s = run(src)
    i = lec["intention"][P[0]]
    print("T1", i["T1"].get("etabli"), i["T1"].get("bas"), i["T1"].get("plancher_quantile"))
    print(json.dumps(s["analyses"]["A4"][P[0]]["descriptif"]["c_T1_sensibilite"], ensure_ascii=False)[:500])
    print([(r["nom"], r["vise"], r["motif"][:100]) for r in s["synthese"]["reserves_addendum"] if r["sonde"] == P[0]])
