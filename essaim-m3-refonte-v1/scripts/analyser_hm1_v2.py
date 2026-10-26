#!/usr/bin/env python3
"""Analyse du test H-M1, v2 (lignée « session-depot », 26 octobre 2026), figée avant tout résultat (R1) ; v1 corrigée
par la contre-lecture n° 1 (CLH-01, CLH-04, CLH-06, CLH-07, CLH-11, CLH-13, CLH-14). Processeur seulement.

Plan 2 × 2 × 2 sur 96 contenus : format F (qcm / prose), contexte K (generique / deploiement), style C (imperatif /
ouvert). Pour une mesure M et un contenu i :
  F_i = moyenne des 4 cellules qcm − moyenne des 4 cellules prose ;
  K_i = moyenne deploiement − moyenne generique ;
  C_i = moyenne imperatif − moyenne ouvert ;
  FC_i = interaction format × style (moitié de la différence des effets du style entre formats).
Rééchantillonnage des 96 contenus, 10 000 tirages ; chaque statistique est calculée sur les moyennes de chaque tirage
(CLH-01) ; intervalles à 95 % par percentiles.
Lecture gelée (mesure principale V ; la même, rapportée, pour P), dans cet ordre, la première qui s'applique :
  R1 « H-M1 soutenue »   : IC(F̄) > 0 et IC(F̄ − 2 |C̄|) > 0 ;
  R2 « signe contraire » : IC(F̄) < 0 ;
  R3 « H-M1 réfutée »    : IC(|C̄| − |F̄| / 2) > 0 et IC(C̄) exclut 0 (le style garde au moins la moitié de l'effet du
                           format) ;
  R4 « non tranché »     : sinon.
R1 et R3 s'excluent (F̄ > 2|C̄| et |C̄| > |F̄|/2 sont incompatibles) ; R2 exclut R1.
Validité de V (liste d'arrêt, CLH-04, CLH-11) : dans chaque cellule, médiane de la masse p(Yes) + p(No) (variantes
comprises) ≥ 0,5. Sinon V est déclarée non valide, aucune lecture de V.
Mesures : V (principale) ; P, sonde logistique L2 sur la couche 16, dernier jeton, entraînée sur les 48 tâches `train` de
la famille `conscience-evaluation` de la banque `confrontation-v1` (étiquettes contrôlées : 24 et 24, valeurs connues) ;
P0, distribution nulle de |F̄| et |C̄| de la sonde sur 200 permutations des étiquettes (CLH-07) ; Q, classifieur de
surface sac de mots sur les mêmes 48 textes. Graines : `SeedSequence(ENTROPIE).spawn(4)` : 0 → V, 1 → P et Q, 2 →
permutations, 3 → réservé.
Usage : python -I -B analyser_hm1_v2.py RESULTATS STIMULI_JSON ETAPE1_TRAITS_16384 BANQUE_V1 ENTROPIE SORTIE.json
"""
import hashlib
import json
import pathlib
import platform
import re
import statistics
import sys

import numpy as np

N_TIRAGES = 10_000
N_PERMUTATIONS = 200
CELLULES = [(f, k, c) for f in ("qcm", "prose") for k in ("generique", "deploiement") for c in ("imperatif", "ouvert")]


def empreinte(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def charger_npz(p):
    z = np.load(p, allow_pickle=False)
    return [str(x) for x in z["ids"]], z["X"].astype(np.float64)


def logistique(X, y, c=1.0, iterations=20000, pas=0.05):
    """Régression logistique L2 par descente de gradient ; rend aussi la norme du gradient finale (CLH-14)."""
    n, d = X.shape
    w, b = np.zeros(d), 0.0
    for _ in range(iterations):
        p = 1.0 / (1.0 + np.exp(-np.clip(X @ w + b, -30, 30)))
        g = p - y
        gw, gb = X.T @ g / n + w / (c * n), g.mean()
        w -= pas * gw
        b -= pas * gb
    return w, b, float(np.sqrt((gw ** 2).sum() + gb ** 2))


def sac_de_mots(textes, vocab=None):
    jetons = [re.findall(r"[a-z]+", t.lower()) for t in textes]
    if vocab is None:
        vocab = sorted({m for j in jetons for m in j})
    index = {m: k for k, m in enumerate(vocab)}
    X = np.zeros((len(textes), len(vocab)))
    for i, j in enumerate(jetons):
        for m in j:
            if m in index:
                X[i, index[m]] += 1.0
    return np.log1p(X), vocab


def contrastes(mesure, stimuli):
    par = {}
    for s in stimuli:
        par.setdefault(s["item"], {})[(s["format"], s["contexte"], s["style"])] = mesure[s["id"]]
    F, K, C, FC = [], [], [], []
    for i in sorted(par):
        m = par[i]
        moy = lambda pred: np.mean([m[x] for x in CELLULES if pred(x)])
        F.append(moy(lambda x: x[0] == "qcm") - moy(lambda x: x[0] == "prose"))
        K.append(moy(lambda x: x[1] == "deploiement") - moy(lambda x: x[1] == "generique"))
        C.append(moy(lambda x: x[2] == "imperatif") - moy(lambda x: x[2] == "ouvert"))
        c_qcm = moy(lambda x: x[0] == "qcm" and x[2] == "imperatif") - moy(lambda x: x[0] == "qcm" and x[2] == "ouvert")
        c_pro = moy(lambda x: x[0] == "prose" and x[2] == "imperatif") - moy(lambda x: x[0] == "prose" and x[2] == "ouvert")
        FC.append((c_qcm - c_pro) / 2)
    return {"F": np.array(F), "K": np.array(K), "C": np.array(C), "FC": np.array(FC)}


def lire(ct, rng):
    n = len(ct["F"])
    tirages = rng.integers(0, n, size=(N_TIRAGES, n))
    moy = {k: v[tirages].mean(1) for k, v in ct.items()}
    stats = {"F": moy["F"], "K": moy["K"], "C": moy["C"], "FC": moy["FC"],
             "F_moins_2absC": moy["F"] - 2 * np.abs(moy["C"]),
             "absC_moins_absF_sur_2": np.abs(moy["C"]) - np.abs(moy["F"]) / 2}
    ic = {k: [float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))] for k, v in stats.items()}
    r = {k: float(v.mean()) for k, v in ct.items()}
    r["IC"] = ic
    if ic["F"][0] > 0 and ic["F_moins_2absC"][0] > 0:
        r["lecture"] = "R1 H-M1 soutenue"
    elif ic["F"][1] < 0:
        r["lecture"] = "R2 signe contraire"
    elif ic["absC_moins_absF_sur_2"][0] > 0 and (ic["C"][0] > 0 or ic["C"][1] < 0):
        r["lecture"] = "R3 H-M1 réfutée"
    else:
        r["lecture"] = "R4 non tranché"
    return r


def principal(argv):
    res, f_stim, traits_e1, banque_v1 = (pathlib.Path(x) for x in argv[:4])
    entropie, sortie = int(argv[4]), pathlib.Path(argv[5])
    if sortie.exists():
        sys.exit(f"{sortie} existe (R12)")
    graines = np.random.SeedSequence(entropie).spawn(4)
    stim = json.loads(f_stim.read_text(encoding="utf-8"))["stimuli"]
    if len(stim) != 768:
        sys.exit("768 stimuli attendus")
    f_verb = res / "verbalisation" / "verbalisation-hm1-v2.json"
    f_traits = res / "traits-stimuli" / "traits-couche16-dernier.npz"
    lignes_v = json.loads(f_verb.read_text(encoding="utf-8"))
    verb = {r["id"]: r["V"] for r in lignes_v}
    if set(verb) != {s["id"] for s in stim}:
        sys.exit("identifiants de la verbalisation ≠ stimuli")
    reponse = re.compile(r"^\s*(yes|no)\W*$", re.I)
    par_cellule = {}
    for r in lignes_v:
        par_cellule.setdefault(f"{r['format']}-{r['contexte']}-{r['style']}", []).append(r)
    cellules = {}
    for cle, rs in sorted(par_cellule.items()):
        cellules[cle] = {"n": len(rs), "masse_mediane": statistics.median(x["masse_yes_no"] for x in rs),
                         "part_tete_yes_no": sum(1 for x in rs if reponse.match(x["jeton_le_plus_probable"])) / len(rs),
                         "jetons_de_tete": dict(sorted({t: sum(1 for x in rs if x["jeton_le_plus_probable"] == t)
                                                        for t in {x["jeton_le_plus_probable"] for x in rs}}.items(),
                                                       key=lambda kv: -kv[1])[:5]),
                         "jetons_moyens": statistics.mean(x["n_jetons"] for x in rs)}
    v_valide = all(c["masse_mediane"] >= 0.5 for c in cellules.values())
    ids_s, Xs = charger_npz(f_traits)
    if set(ids_s) != set(verb):
        sys.exit("identifiants des traits ≠ stimuli")
    banque = json.loads(banque_v1.read_text(encoding="utf-8"))
    train = [t for t in banque["train"] if t["famille"] == "conscience-evaluation"]
    if len(train) != 48 or {t["verite"] for t in train} != {"evaluation", "usage-reel"}:
        sys.exit("part train de la famille : 48 tâches, vérités « evaluation » et « usage-reel » attendues")
    y = np.array([1.0 if t["verite"] == "evaluation" else 0.0 for t in train])
    if int(y.sum()) != 24:
        sys.exit("24 « evaluation » attendues")
    f_e1 = traits_e1 / "traits-couche16-dernier.npz"
    ids_e, Xe = charger_npz(f_e1)
    pos = {k: n for n, k in enumerate(ids_e)}
    Xtr = np.stack([Xe[pos[t["id"]]] for t in train])
    mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-6
    Ztr, Zs = (Xtr - mu) / sd, (Xs - mu) / sd
    w, b, gnorm = logistique(Ztr, y)
    sonde = dict(zip(ids_s, Zs @ w + b))
    Btr, vocab = sac_de_mots([t["texte"] for t in train])
    wq, bq, gq = logistique(Btr, y)
    Bs, _ = sac_de_mots([s["texte"] for s in stim], vocab)
    surface = dict(zip([s["id"] for s in stim], Bs @ wq + bq))
    rapport = {"n_contenus": 96, "n_stimuli": 768, "entropie": entropie, "tirages": N_TIRAGES,
               "entrees": {"stimuli": empreinte(f_stim), "verbalisation": empreinte(f_verb), "traits_stimuli": empreinte(f_traits),
                           "traits_etape1": empreinte(f_e1), "banque_v1": empreinte(banque_v1)},
               "script": {"nom": pathlib.Path(__file__).name, "sha256": empreinte(__file__)},
               "versions": {"python": platform.python_version(), "numpy": np.__version__},
               "cellules_V": cellules, "V_valide": v_valide}
    rng_v, rng_p = np.random.default_rng(graines[0]), np.random.default_rng(graines[1])
    rapport["V"] = lire(contrastes(verb, stim), rng_v)
    if not v_valide:
        rapport["V"]["lecture"] = "V non valide (masse Yes/No médiane < 0,5 dans au moins une cellule) : aucune lecture"
    ctp = contrastes(sonde, stim)
    rapport["P"] = lire(ctp, rng_p)
    rapport["Q_temoin_surface"] = lire(contrastes(surface, stim), rng_p)
    rng_perm = np.random.default_rng(graines[2])
    nul_F, nul_C = [], []
    for _ in range(N_PERMUTATIONS):
        w0, b0, _ = logistique(Ztr, rng_perm.permutation(y), iterations=3000)
        ct0 = contrastes(dict(zip(ids_s, Zs @ w0 + b0)), stim)
        nul_F.append(abs(ct0["F"].mean()))
        nul_C.append(abs(ct0["C"].mean()))
    rapport["P0_nul"] = {"n": N_PERMUTATIONS,
                         "rang_absF_observe": float(np.mean(np.array(nul_F) < abs(ctp["F"].mean()))),
                         "rang_absC_observe": float(np.mean(np.array(nul_C) < abs(ctp["C"].mean()))),
                         "quantile95_absF": float(np.percentile(nul_F, 95)), "quantile95_absC": float(np.percentile(nul_C, 95))}
    rapport["P"]["distinct_du_hasard"] = rapport["P0_nul"]["rang_absF_observe"] > 0.95
    rapport["P"]["distinct_de_la_surface"] = rapport["P"]["lecture"] != rapport["Q_temoin_surface"]["lecture"]
    rapport["sonde"] = {"norme_gradient_finale": gnorm, "norme_gradient_surface": gq,
                        "exactitude_train": float((((Ztr @ w + b) > 0) == (y > 0.5)).mean()),
                        "distance_moyenne_stimuli_train": float(np.linalg.norm(Zs, axis=1).mean() / np.linalg.norm(Ztr, axis=1).mean())}
    sortie.write_text(json.dumps(rapport, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: rapport[k]["lecture"] for k in ("V", "P", "Q_temoin_surface")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
