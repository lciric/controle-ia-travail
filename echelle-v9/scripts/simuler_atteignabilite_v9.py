#!/usr/bin/env python3
"""Atteignabilité des issues de la comparaison d'échelle v8 (contre-lecture n° 7, CLT-01, CLT-02 ; lignée
« session-depot », 27 octobre 2026). Déclinée de `simuler_atteignabilite_v7.py` (R12) : l'analyse v8 inchangée (mode
répétition, 300 tirages au lieu de 2 000) sur des activations synthétiques à vérité connue. Tous les cas de la v7, dans
le même ordre et aux mêmes graines (mêmes activations), puis les cas de la v8, à graines nouvelles, chacun répété
REPETITIONS_V8 fois : voisins de la classe de cl6 que la cohérence des deux sens laisse passer (CLT-01) — écart vrai
sous δ (λ 0,6 et 0,4 ; 0,55 et 0,4) avec des signatures d'un seul jeu croisées, de signes opposés, chacune sous δ, et
son miroir ; écart vrai au-delà de δ (λ 0,65 et 0,35 ; 0,7 et 0,35) compensé par de telles signatures ; fuite égale
(0,7 et 0,7) avec un contexte du jeu b × 1,333 ou × 0,75 et des signatures croisées ; témoins sans signature —, et
prix de la cohérence sous H_0 à contexte inégal (CLT-02 : λ 0,5 sous × 0,6, en dimension 64 et 256 ; 0,7 sous × 0,75 ;
0,9 sous × 0,8 ; 0,7 sous × 1,333). Le détail rapporte, pour chaque analyse, les réserves (dont les deux réserves de la
v8) et le rapport des Ec. Les cas de la v7 (contre-lecture n° 6, CLU-01), chacun répété REPETITIONS_V7 fois, étaient : sous H_0 avec une fuite égale non nulle (λ 0,5
et 0,5), signatures d'un seul jeu à chaque taille, de jeux différents et de signes opposés, dans les deux ordres et en
miroir (signes échangés), en dimension 64 (tau 0,15 : amplitude 3 ; tau 0,4 : amplitude 0,9) et 256 (tau 0,15 et 0,4 :
amplitudes 0,9 et 1,3) ; témoins en dimension 256 (H_0 égal, H_A) ; H_A avec un contexte du jeu b plus faible
(× 0,6 et × 0,8), en dimension 64 et 256, H_0 avec un contexte du jeu b × 0,8, et H_A sous la signature négative d'un
seul jeu au petit, en dimension 256, pour compter ce que la cohérence des deux sens coûte en puissance. Aucun modèle,
processeur seulement ; les analyses tournent en parallèle sur PROCESSUS processus, chacune à sa graine fixe : le
résultat ne dépend pas de l'ordre d'exécution. Versions, commit et réglage des fils de calcul (FILS) consignés (R9, CLY-15) ; lancer avec
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 pour reproduire la sortie scellée.

Modèle synthétique (d = 64, ou 256 où le cas le dit) : x = contenu + s_f·F + s_c·κ_jeu·C + cadrage(jeu, paire, classe) + bruit, κ_a = 1,
κ_b = contexte_b ; F = alpha·C + F⊥ + signature·(moyenne des particularités des paires du jeu a) + signature_b·(idem,
jeu b). λ vrai (concept) ≈ alpha, relativement à l'effet du contexte du jeu mesuré.
    python -I -B simuler_atteignabilite_v9.py STIMULI_JSON SORTIE_DOSSIER
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
spec = importlib.util.spec_from_file_location("an", ICI / "analyser_echelle_v9.py")
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
    ("fuite faible égale (0,2 et 0,2)", 0.2, 0.2, {}, {}, (0.15,)),
    ("fuite faible égale, contexte du jeu b plus faible (0,15 et 0,15 ; × 0,6)", 0.15, 0.15, {"contexte_b": 0.6},
     {"contexte_b": 0.6}, (0.15,)),
    ("signature négative du jeu a au grand (0 et 0)", 0.0, 0.0, {}, {"signature": -2.0}, (0.4,)),
    ("signatures des deux jeux, négatives, au petit (0 et 0)", 0.0, 0.0, {"signature": -2.0, "signature_b": -2.0}, {},
     (0.4,)),
    ("signatures des deux jeux au grand (0 et 0)", 0.0, 0.0, {}, {"signature": 2.0, "signature_b": 2.0}, (0.4,)),
    # v6 (contre-lecture n° 5)
    ("signatures croisées négatives, jeu a au petit, jeu b au grand (0 et 0)", 0.0, 0.0, {"signature": -2.0},
     {"signature_b": -2.0}, (0.15, 0.4)),
    ("signatures croisées négatives, jeu b au petit, jeu a au grand (0 et 0)", 0.0, 0.0, {"signature_b": -2.0},
     {"signature": -2.0}, (0.15, 0.4)),
    ("signatures croisées positives, jeu a au petit, jeu b au grand (0 et 0)", 0.0, 0.0, {"signature": 2.0},
     {"signature_b": 2.0}, (0.4,)),
    ("signatures croisées positives, jeu b au petit, jeu a au grand (0 et 0)", 0.0, 0.0, {"signature_b": 2.0},
     {"signature": 2.0}, (0.4,)),
    ("signature négative du jeu b au petit (0 et 0)", 0.0, 0.0, {"signature_b": -2.0}, {}, (0.4,)),
    ("signature du jeu b au grand (0 et 0)", 0.0, 0.0, {}, {"signature_b": 2.0}, (0.4,)),
    ("signature négative du jeu b au grand (0 et 0)", 0.0, 0.0, {}, {"signature_b": -2.0}, (0.4,)),
    ("H1 sous les signatures négatives des deux jeux au petit (1,0 et 0,2)", 1.0, 0.2,
     {"signature": -2.0, "signature_b": -2.0}, {}, (0.4,)),
    ("H1 sous des signatures croisées de signes opposés (1,0 et 0,2 ; a négatif au petit, b positif au grand)", 1.0,
     0.2, {"signature": -2.0}, {"signature_b": 2.0}, (0.4,)),
]
REPETITIONS = 4
# v7 (contre-lecture n° 6, CLU-01) : (nom, alpha petit, alpha grand, options petit, options grand, taus), options
# communes de dimension comprises ; graines à la suite de celles de la v6
REPETITIONS_V7 = 6
# v8 (contre-lecture n° 7, CLT-01, CLT-02) : mêmes formes ; graines à la suite de celles de la v7
REPETITIONS_V8 = 6


def croisees_opposees(s, d):
    """Signatures d'un seul jeu à chaque taille, jeux différents, signes opposés, sous H_0 (0,5 et 0,5) : les deux
    ordres et leurs miroirs (CLU-01)."""
    a = f"{s:g}".replace(".", ",")
    return [(f"H0 (0,5 et 0,5), jeu a +{a} au petit, jeu b −{a} au grand, d {d}", 0.5, 0.5,
             {"signature": s, "d": d}, {"signature_b": -s, "d": d}),
            (f"H0 (0,5 et 0,5), jeu b +{a} au petit, jeu a −{a} au grand, d {d}", 0.5, 0.5,
             {"signature_b": s, "d": d}, {"signature": -s, "d": d}),
            (f"H0 (0,5 et 0,5), jeu a −{a} au petit, jeu b +{a} au grand, d {d}", 0.5, 0.5,
             {"signature": -s, "d": d}, {"signature_b": s, "d": d}),
            (f"H0 (0,5 et 0,5), jeu b −{a} au petit, jeu a +{a} au grand, d {d}", 0.5, 0.5,
             {"signature_b": -s, "d": d}, {"signature": s, "d": d})]


VERITES_V7 = (
    [v + ((0.15,),) for v in croisees_opposees(3.0, 64)] + [v + ((0.4,),) for v in croisees_opposees(0.9, 64)]
    + [v + ((0.15, 0.4),) for v in croisees_opposees(0.9, 256)] + [v + ((0.15, 0.4),) for v in croisees_opposees(1.3, 256)]
    + [("H0 (0,5 et 0,5), d 256", 0.5, 0.5, {"d": 256}, {"d": 256}, (0.15, 0.4)),
       ("H1 (1,0 et 0,2), d 256", 1.0, 0.2, {"d": 256}, {"d": 256}, (0.15, 0.4)),
       ("H1 (1,0 et 0,2), contexte du jeu b × 0,6", 1.0, 0.2, {"contexte_b": 0.6}, {"contexte_b": 0.6}, (0.15, 0.4)),
       ("H1 (1,0 et 0,2), contexte du jeu b × 0,8", 1.0, 0.2, {"contexte_b": 0.8}, {"contexte_b": 0.8}, (0.15, 0.4)),
       ("H1 (1,0 et 0,2), contexte du jeu b × 0,6, d 256", 1.0, 0.2, {"contexte_b": 0.6, "d": 256},
        {"contexte_b": 0.6, "d": 256}, (0.15,)),
       ("H1 (1,0 et 0,2), contexte du jeu b × 0,8, d 256", 1.0, 0.2, {"contexte_b": 0.8, "d": 256},
        {"contexte_b": 0.8, "d": 256}, (0.15,)),
       ("H0 (0,5 et 0,5), contexte du jeu b × 0,8", 0.5, 0.5, {"contexte_b": 0.8}, {"contexte_b": 0.8}, (0.15,)),
       ("H0 (0,5 et 0,5), contexte du jeu b × 0,8, d 256", 0.5, 0.5, {"contexte_b": 0.8, "d": 256},
        {"contexte_b": 0.8, "d": 256}, (0.15,)),
       ("H1 (1,0 et 0,2), jeu a −1 au petit, d 256", 1.0, 0.2, {"signature": -1.0, "d": 256}, {"d": 256}, (0.15,))])
D256 = {"d": 256}
VERITES_V8 = [
    # CLT-01, famille B : écart vrai sous δ (H_0), signatures croisées de signes opposés, chacune sous δ
    ("H0 (0,6 et 0,4), jeu a +0,6 au petit, jeu b −0,6 au grand, d 256", 0.6, 0.4, {"signature": 0.6, **D256},
     {"signature_b": -0.6, **D256}, (0.15,)),
    ("H0 (0,55 et 0,4), jeu a +0,55 au petit, jeu b −0,55 au grand, d 256", 0.55, 0.4, {"signature": 0.55, **D256},
     {"signature_b": -0.55, **D256}, (0.15,)),
    ("H0 (0,4 et 0,6), jeu a −0,6 au petit, jeu b +0,6 au grand, d 256", 0.4, 0.6, {"signature": -0.6, **D256},
     {"signature_b": 0.6, **D256}, (0.15,)),
    ("H0 (0,6 et 0,4), d 256", 0.6, 0.4, D256, D256, (0.15,)),
    # CLT-01, famille C : écart vrai au-delà de δ (H_A), compensé par des signatures croisées
    ("H1 (0,65 et 0,35), jeu a −0,55 au petit, jeu b +0,55 au grand, d 256", 0.65, 0.35, {"signature": -0.55, **D256},
     {"signature_b": 0.55, **D256}, (0.15,)),
    ("H1 (0,7 et 0,35), jeu a −0,6 au petit, jeu b +0,6 au grand, d 256", 0.7, 0.35, {"signature": -0.6, **D256},
     {"signature_b": 0.6, **D256}, (0.15,)),
    ("H1 (0,65 et 0,35), d 256", 0.65, 0.35, D256, D256, (0.15,)),
    # CLT-01, famille D : fuite égale, contexte d'un jeu plus fort ou plus faible, signatures croisées
    ("H0 (0,7 et 0,7), contexte du jeu b × 1,333, jeu b −1,2 au petit, jeu a +1,2 au grand, d 256", 0.7, 0.7,
     {"signature_b": -1.2, "contexte_b": 1.333, **D256}, {"signature": 1.2, "contexte_b": 1.333, **D256}, (0.15,)),
    ("H0 (0,7 et 0,7), contexte du jeu b × 0,75, jeu b +1,0 au petit, jeu a −1,0 au grand, d 256", 0.7, 0.7,
     {"signature_b": 1.0, "contexte_b": 0.75, **D256}, {"signature": -1.0, "contexte_b": 0.75, **D256}, (0.15,)),
    # CLT-02 : prix de la cohérence sous H_0 à contexte inégal (témoins de la famille D compris)
    ("H0 (0,5 et 0,5), contexte du jeu b × 0,6", 0.5, 0.5, {"contexte_b": 0.6}, {"contexte_b": 0.6}, (0.15,)),
    ("H0 (0,5 et 0,5), contexte du jeu b × 0,6, d 256", 0.5, 0.5, {"contexte_b": 0.6, **D256},
     {"contexte_b": 0.6, **D256}, (0.15,)),
    ("H0 (0,7 et 0,7), contexte du jeu b × 0,75, d 256", 0.7, 0.7, {"contexte_b": 0.75, **D256},
     {"contexte_b": 0.75, **D256}, (0.15,)),
    ("H0 (0,9 et 0,9), contexte du jeu b × 0,8, d 256", 0.9, 0.9, {"contexte_b": 0.8, **D256},
     {"contexte_b": 0.8, **D256}, (0.15,)),
    ("H0 (0,7 et 0,7), contexte du jeu b × 1,333, d 256", 0.7, 0.7, {"contexte_b": 1.333, **D256},
     {"contexte_b": 1.333, **D256}, (0.15,)),
]
FILS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")


def fabriquer(dossier, stimuli, st, alpha, graine, tau, force_c=4.0, signature=0.0, signature_b=0.0, contexte_b=1.0,
              d=64):
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
            kb = contexte_b if s["jeu"] == "b" else 1.0
            X[i] = contenus[s["contenu"]] + sf * F + sc * kb * C * ech + cadrage[(s["jeu"], s["paire"], s["classe"])] \
                + bruit[i]
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
    """Liste ordonnée (case, tau, graine, alphas, options) ; graines comme la v3 : 3002, 3004, … dans cet ordre, les cas
    de la v7, puis ceux de la v8, à la suite."""
    out, graine = [], 3000
    for liste, n in ((VERITES, REPETITIONS), (VERITES_V7, REPETITIONS_V7), (VERITES_V8, REPETITIONS_V8)):
        for nom, a8, a70, o8, o70, taus in liste:
            for tau in taus:
                for _ in range(n):
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
            return cle, graine, "arrêt", None, None, None, None
        lu = json.loads((base / "s" / "analyse-echelle-v9.json").read_text(encoding="utf-8"))
    lecture = lu["lecture"].removeprefix("répétition, non décisive (").removesuffix(")")
    if lu["reserves"]:
        lecture += f" ({len(lu['reserves'])} réserve(s))"
    return (cle, graine, lecture, lu["lecture_par_sens"], lu["issues_tenues_par_sens"], lu["reserves"],
            {"ecart_sens": lu["ecart_sens"], "ecart_sens_ic": lu["ecart_sens_ic"],
             "rapport_Ec": lu["rapport_Ec"], "rapport_Ec_ic": lu["rapport_Ec_ic"],
             "coherence_des_sens": lu["coherence_des_sens"], "conditions_manquantes": lu["conditions_manquantes"]})


def principal(argv):
    stimuli, sortie = pathlib.Path(argv[0]), pathlib.Path(argv[1])
    if sortie.exists():
        sys.exit(f"{sortie} existe déjà (R12)")
    liste = [(str(stimuli.resolve()),) + t for t in travaux()]
    with multiprocessing.get_context("fork").Pool(PROCESSUS) as pool:
        resultats = pool.map(un_travail, liste, chunksize=1)
    comptes, par_sens, detail = {}, {}, []
    for cle, graine, lecture, sens, tenues, reserves, coherence in resultats:
        comptes.setdefault(cle, collections.Counter())[lecture] += 1
        if sens is not None:
            par_sens.setdefault(cle, collections.Counter())[f"a→b : {sens['a→b']} ; b→a : {sens['b→a']}"] += 1
        detail.append({"cas": cle, "graine": graine, "lecture": lecture, "lecture_par_sens": sens,
                       "issues_tenues_par_sens": tenues, "reserves": reserves, **(coherence or {})})
    for cle in comptes:
        print(cle, dict(comptes[cle]), flush=True)
    commit, propre = AN.etat_scripts()
    sortie.mkdir(parents=True)
    f = sortie / "atteignabilite-echelle-v9.json"
    f.write_text(json.dumps({"version": "atteignabilite-echelle-v9", "analyse_sha256": sha(ICI / "analyser_echelle_v9.py"),
                             "simulation_sha256": sha(__file__), "stimuli_sha256": sha(stimuli),
                             "n_boot": N_BOOT_SIMULATION, "repetitions": REPETITIONS,
                             "repetitions_v7": REPETITIONS_V7, "repetitions_v8": REPETITIONS_V8, "processus": PROCESSUS,
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
