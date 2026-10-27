#!/usr/bin/env python3
"""Atteignabilité des issues de la comparaison d'échelle v4 (contre-lecture n° 3, CLZ-01 et CLZ-08 ; lignée
« session-depot », 27 octobre 2026). Déclinée de `simuler_atteignabilite_v3.py` (R12) : l'analyse v4 inchangée (mode
répétition, 300 tirages au lieu de 2 000) sur des activations synthétiques à vérité connue. Les neuf cas de la v3, dans
le même ordre et aux mêmes graines (mêmes activations), puis sept cas nouveaux : signature négative du jeu a (CLZ-01),
signature du jeu a au grand, signature du jeu b, signatures des deux jeux ensemble (CLZ-08), effet vrai masqué par une
signature négative (deux cas, CLZ-01), contexte faible au grand. Aucun modèle, processeur seulement ; les analyses
tournent en parallèle sur PROCESSUS processus, chacune à sa graine fixe : le résultat ne dépend pas de l'ordre
d'exécution. Versions, commit et réglage des fils de calcul (FILS) consignés (R9, CLY-15) ; lancer avec
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 pour reproduire la sortie scellée.

Modèle synthétique (d = 64) : x = contenu + s_f·F + s_c·C + cadrage(jeu, paire, classe) + bruit,
F = alpha·C + F⊥ + signature·(moyenne des particularités des paires du jeu a) + signature_b·(idem, jeu b).
λ vrai (concept) ≈ alpha.
    python -I -B simuler_atteignabilite_v4.py STIMULI_JSON SORTIE_DOSSIER
"""
import collections
import hashlib
import importlib.util
import json
import multiprocessing
import os
import pathlib
import platform
import sys
import tempfile

import numpy as np

ICI = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("an", ICI / "analyser_echelle_v4.py")
AN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AN)
N_BOOT_SIMULATION = 300
PROCESSUS = 3

TOUS = (0.15, 0.4, 0.8)
# (nom, alpha petit, alpha grand, options petit, options grand, taus) ; l'ordre fixe celui des graines
VERITES = [
    ("H0 (0,5 et 0,5)", 0.5, 0.5, {}, {}, TOUS),
    ("pas de fuite (0 et 0)", 0.0, 0.0, {}, {}, TOUS),
    ("H1 (1,0 et 0,2)", 1.0, 0.2, {}, {}, TOUS),
    ("H1 faible (0,6 et 0,2)", 0.6, 0.2, {}, {}, TOUS),
    ("inverse (0,2 et 1,0)", 0.2, 1.0, {}, {}, (0.4,)),
    ("signe inverse (−0,6 et 0)", -0.6, 0.0, {}, {}, (0.4,)),
    ("signature du jeu a au petit (0 et 0)", 0.0, 0.0, {"signature": 2.0}, {}, (0.4,)),
    ("contexte faible aux deux", 1.0, 0.2, {"force_c": 0.3}, {"force_c": 0.3}, (0.4,)),
    ("contexte faible au petit", 1.0, 0.2, {"force_c": 0.3}, {}, (0.4,)),
    ("signature négative du jeu a au petit (0 et 0)", 0.0, 0.0, {"signature": -2.0}, {}, (0.4,)),
    ("signature du jeu a au grand (0 et 0)", 0.0, 0.0, {}, {"signature": 2.0}, (0.4,)),
    ("signature du jeu b au petit (0 et 0)", 0.0, 0.0, {"signature_b": 2.0}, {}, (0.4,)),
    ("signatures des deux jeux au petit (0 et 0)", 0.0, 0.0, {"signature": 2.0, "signature_b": 2.0}, {}, (0.4,)),
    ("H1 masqué par une signature négative du jeu a (1,0 et 0,2)", 1.0, 0.2, {"signature": -3.0}, {}, (0.15, 0.4)),
    ("fuite masquée par une signature négative du jeu a (0,6 et 0)", 0.6, 0.0, {"signature": -1.4}, {}, (0.15,)),
    ("contexte faible au grand", 1.0, 0.2, {}, {"force_c": 0.3}, (0.4,)),
]
REPETITIONS = 4
FILS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")


def fabriquer(dossier, stimuli, st, alpha, graine, tau, force_c=4.0, signature=0.0, signature_b=0.0, d=64):
    rng = np.random.default_rng(graine)
    base = np.linalg.qr(rng.normal(size=(d, 3)))[0].T
    C, Fp = base[0] * force_c, base[1] * 2.0
    contenus = rng.normal(size=(64, d))
    cadrage = {}
    for s in st:
        k = (s["jeu"], s["paire"], s["classe"])
        if k not in cadrage:
            cadrage[k] = rng.normal(size=d) * tau
    sig = {}
    for jeu in ("a", "b"):
        v = sum(cadrage[(jeu, j, "eval")] - cadrage[(jeu, j, "reel")] for j in range(6)) / 6
        sig[jeu] = v / np.linalg.norm(v) * 4.0
    dossier.mkdir(parents=True)
    bruit = rng.normal(size=(len(st), d))
    sorties = {}
    for c in (4, 6):
        ech = 0.5 if c == 4 else 1.0
        F = alpha * C * ech + Fp + signature * sig["a"] + signature_b * sig["b"]
        X = np.empty((len(st), d))
        for i, s in enumerate(st):
            sf = 0.5 if s["format"] == "qcm" else -0.5
            sc = 0.5 if s["classe"] == "eval" else -0.5
            X[i] = contenus[s["contenu"]] + sf * F + sc * C * ech + cadrage[(s["jeu"], s["paire"], s["classe"])] + bruit[i]
        f = dossier / f"activations-L{c}.npy"
        np.save(f, X.astype(np.float16))
        sceller(f)
        sorties[f.name] = sha(f)
    f = dossier / "ids.json"
    f.write_text(json.dumps([s["id"] for s in st]) + "\n", encoding="utf-8")
    sceller(f)
    sorties["ids.json"] = sha(f)
    m = {"modele": "synthetique", "revision": None, "couches": [4, 6], "dimension": d, "type_nombre": "bfloat16",
         "limite": None, "sha256_stimuli": sha(stimuli), "rendu_premier": "<gabarit>", "dernier_jeton": "<fin>",
         "sha256_sorties": sorties}
    (dossier / "manifeste-mesure.json").write_text(json.dumps(m), encoding="utf-8")
    sceller(dossier / "manifeste-mesure.json")


def travaux():
    """Liste ordonnée (case, tau, graine, alphas, options) ; graines comme la v3 : 3002, 3004, … dans cet ordre."""
    out, graine = [], 3000
    for nom, a8, a70, o8, o70, taus in VERITES:
        for tau in taus:
            for _ in range(REPETITIONS):
                graine += 2
                out.append((f"{nom} ; tau {tau}", tau, graine, a8, a70, o8, o70))
    return out


def un_travail(t):
    stimuli, cle, tau, graine, a8, a70, o8, o70 = t
    AN.N_BOOT = N_BOOT_SIMULATION
    stimuli = pathlib.Path(stimuli)
    st = json.loads(stimuli.read_text(encoding="utf-8"))["stimuli"]
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)
        fabriquer(base / "p", stimuli, st, a8, graine, tau, **o8)
        fabriquer(base / "g", stimuli, st, a70, graine + 1, tau, **o70)
        code = AN.principal([str(stimuli), str(base / "p"), str(base / "g"), str(graine), str(base / "s"),
                             "--repetition"])
        if code != 0:
            return cle, graine, "arrêt", None
        lu = json.loads((base / "s" / "analyse-echelle-v4.json").read_text(encoding="utf-8"))
    lecture = lu["lecture"].removeprefix("répétition, non décisive (").removesuffix(")")
    if lu["reserves"]:
        lecture += f" ({len(lu['reserves'])} réserve(s))"
    return cle, graine, lecture, lu["lecture_par_sens"]


def principal(argv):
    stimuli, sortie = pathlib.Path(argv[0]), pathlib.Path(argv[1])
    if sortie.exists():
        sys.exit(f"{sortie} existe déjà (R12)")
    liste = [(str(stimuli.resolve()),) + t for t in travaux()]
    with multiprocessing.get_context("fork").Pool(PROCESSUS) as pool:
        resultats = pool.map(un_travail, liste, chunksize=1)
    comptes, par_sens, detail = {}, {}, []
    for cle, graine, lecture, sens in resultats:
        comptes.setdefault(cle, collections.Counter())[lecture] += 1
        if sens is not None:
            par_sens.setdefault(cle, collections.Counter())[f"a→b : {sens['a→b']} ; b→a : {sens['b→a']}"] += 1
        detail.append({"cas": cle, "graine": graine, "lecture": lecture, "lecture_par_sens": sens})
    for cle in comptes:
        print(cle, dict(comptes[cle]), flush=True)
    commit, propre = AN.etat_scripts()
    sortie.mkdir(parents=True)
    f = sortie / "atteignabilite-echelle-v4.json"
    f.write_text(json.dumps({"version": "atteignabilite-echelle-v4", "analyse_sha256": sha(ICI / "analyser_echelle_v4.py"),
                             "simulation_sha256": sha(__file__), "stimuli_sha256": sha(stimuli),
                             "n_boot": N_BOOT_SIMULATION, "repetitions": REPETITIONS, "processus": PROCESSUS,
                             "commit_scripts": commit, "arbre_scripts_propre": propre,
                             "python": platform.python_version(), "numpy": np.__version__,
                             "fils_de_calcul": {k: os.environ.get(k) for k in FILS},
                             "comptes": {k: dict(v) for k, v in comptes.items()},
                             "lectures_par_sens": {k: dict(v) for k, v in par_sens.items()}, "detail": detail},
                            ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(f)
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
