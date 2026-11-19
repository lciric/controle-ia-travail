"""S0 : banc de reproduction des valeurs scellees de P1 (c2a et c2b), lecture seule.

Loi separee (metrique, point 7 du brouillon 4) : moindres carres de Delta sur v0, a travers les items ;
g = -pente ; c = -ordonnee / pente ; R2 = carre de la correlation.
Delta = moyenne sous pression - moyenne neutre ; v0 = moyenne neutre.
Pour c2b, deux neutres possibles : le neutre de c2b (mean_neu de c2b) ou celui de c2a (mean_neu de c2a).
On essaie aussi les variantes : par generation (10 par item) au lieu des moyennes, et exclusion des items.
Aucune donnee de texte n'est lue : seulement des notes de polarite.
"""
import hashlib
import json
import sys

import numpy as np

RACINE = "/home/user/controle-ia-travail/donnees/P1-loi-attraction-v1/"
ATTENDU = {
    "c2a": dict(g=0.717688, c=1.455688, r2=0.7669, sha="6ad1a71822395e11417223c8d872c5973129dd1c8a4b023be74810f4746b5d83"),
    "c2b": dict(g=0.677846, c=2.936901, r2=0.7874, sha="ae097f3d7ac993fe41fa3e1bb11d76f88727ffdf128bc661566949b7f5bc0aa2"),
}


def charge(nom):
    brut = open(RACINE + nom + "_results.json", "rb").read()
    sha = hashlib.sha256(brut).hexdigest()
    assert sha == ATTENDU[nom]["sha"], (nom, sha)
    return json.loads(brut)


def loi(v0, d):
    v0 = np.asarray(v0, float)
    d = np.asarray(d, float)
    pente, ordo = np.polyfit(v0, d, 1)
    g = -pente
    c = -ordo / pente
    r2 = np.corrcoef(v0, d)[0, 1] ** 2
    return g, c, r2


def rapport(nom, g, c, r2, etiquette):
    a = ATTENDU[nom]
    ok = (round(g, 6) == a["g"]) and (round(c, 6) == a["c"]) and (round(r2, 4) == a["r2"])
    print(f"{nom} {etiquette:45s} g={g:.6f} c={c:.6f} R2={r2:.4f}  {'REPRODUIT' if ok else 'non'}")
    return bool(ok)


def main():
    a = charge("c2a")
    b = charge("c2b")
    ids = sorted(a["table"], key=int)
    assert ids == sorted(b["table"], key=int)
    neu_a = np.array([a["table"][i]["mean_neu"] for i in ids])
    pre_a = np.array([a["table"][i]["mean_pre"] for i in ids])
    neu_b = np.array([b["table"][i]["mean_neu"] for i in ids])
    pra_b = np.array([b["table"][i]["mean_praise"] for i in ids])
    # controle de coherence des moyennes
    for t, cle_v, cle_m in ((a, "pol_neu", "mean_neu"), (a, "pol_pre", "mean_pre"), (b, "pol_neu", "mean_neu"), (b, "pol_praise", "mean_praise")):
        for i in ids:
            assert abs(np.mean(t["table"][i][cle_v]) - t["table"][i][cle_m]) < 1e-9
    print("items :", len(ids))
    print("neutres c2a et c2b identiques par item ?", bool(np.allclose(neu_a, neu_b)),
          "; items differents :", int((~np.isclose(neu_a, neu_b)).sum()))
    res = {}
    res["c2a_moyennes"] = rapport("c2a", *loi(neu_a, pre_a - neu_a), "moyennes par item, neutre de c2a")
    res["c2b_neutre_b"] = rapport("c2b", *loi(neu_b, pra_b - neu_b), "moyennes par item, neutre de c2b")
    res["c2b_neutre_a"] = rapport("c2b", *loi(neu_a, pra_b - neu_a), "moyennes par item, neutre de c2a")
    # variante par generation (300 points)
    v0 = np.concatenate([a["table"][i]["pol_neu"] for i in ids])
    v1 = np.concatenate([a["table"][i]["pol_pre"] for i in ids])
    rapport("c2a", *loi(v0, v1 - v0), "par generation appariee (300 points)")
    # exclusion des items plafond de c2b
    pl = set(str(x) for x in b["plafond"])
    m = np.array([i not in pl for i in ids])
    rapport("c2b", *loi(neu_b[m], (pra_b - neu_b)[m]), "neutre de c2b, sans items plafond")
    # sensibilite de c chapeau : erreur type delta et intervalle par reechantillonnage des items
    rng = np.random.default_rng(np.random.SeedSequence(20261020).spawn(1)[0])
    for nom, v0_, d_ in (("c2a", neu_a, pre_a - neu_a), ("c2b", neu_b, pra_b - neu_b)):
        gs, cs = [], []
        for _ in range(10000):
            k = rng.integers(0, len(ids), len(ids))
            g, c, _ = loi(v0_[k], d_[k])
            gs.append(g)
            cs.append(c)
        gs, cs = np.array(gs), np.array(cs)
        print(f"{nom} reechantillonnage des items (10 000) : IC95 g [{np.percentile(gs,2.5):.3f} ; {np.percentile(gs,97.5):.3f}] ;"
              f" IC95 c [{np.percentile(cs,2.5):.3f} ; {np.percentile(cs,97.5):.3f}] ; plage v0 [{v0_.min():.2f} ; {v0_.max():.2f}] ; moyenne v0 {v0_.mean():.3f}")
    print("RESUME", json.dumps(res))
    return 0 if (res["c2a_moyennes"] and (res["c2b_neutre_b"] or res["c2b_neutre_a"])) else 1


if __name__ == "__main__":
    sys.exit(main())
