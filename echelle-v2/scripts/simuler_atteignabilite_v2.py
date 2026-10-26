#!/usr/bin/env python3
"""Atteignabilité des issues de la comparaison d'échelle v2 (CLX-12), lignée « session-depot », 26 octobre 2026.
Fait passer l'analyse v2 (`analyser_echelle_v2.py`, inchangée, en mode répétition, 300 tirages au lieu de 2 000) sur
des activations synthétiques à vérité connue, pour plusieurs vérités, niveaux d'hétérogénéité des paires (tau) et
interactions paire × format, et compte les lectures. Aucun modèle, processeur seulement. Graines fixes (R9).

Modèle synthétique (d = 64) : x = contenu + s_f·F + s_c·C + cadrage(paire, classe) + inter·s_f·cadrage(paire, classe)
+ bruit, F = alpha·C + F⊥. λ vrai ≈ alpha.
    python -I -B simuler_atteignabilite_v2.py STIMULI_JSON SORTIE_DOSSIER
"""
import collections
import hashlib
import importlib.util
import json
import pathlib
import sys
import tempfile

import numpy as np

ICI = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("an", ICI / "analyser_echelle_v2.py")
AN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AN)
AN.N_BOOT = 300

VERITES = {"H0 (0,5 et 0,5)": (0.5, 0.5), "pas de fuite (0 et 0)": (0.0, 0.0), "H1 (1,0 et 0,2)": (1.0, 0.2),
           "H1 faible (0,6 et 0,2)": (0.6, 0.2)}
TAUS = (0.15, 0.4)
INTERACTIONS = (0.0, 0.3)
REPETITIONS = 6


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")


def fabriquer(dossier, stimuli, st, alpha, graine, tau, inter, d=64, force_c=4.0):
    rng = np.random.default_rng(graine)
    base = np.linalg.qr(rng.normal(size=(d, 3)))[0].T
    C, Fp = base[0] * force_c, base[1] * 2.0
    contenus = rng.normal(size=(64, d))
    cadrage = {}
    for s in st:
        k = (s["jeu"], s["paire"], s["classe"])
        if k not in cadrage:
            cadrage[k] = rng.normal(size=d) * tau
    dossier.mkdir(parents=True)
    bruit = rng.normal(size=(len(st), d))
    sorties = {}
    for c in (4, 6):
        ech = 0.5 if c == 4 else 1.0
        F = alpha * C * ech + Fp
        X = np.empty((len(st), d))
        for i, s in enumerate(st):
            sf = 0.5 if s["format"] == "qcm" else -0.5
            sc = 0.5 if s["classe"] == "eval" else -0.5
            cad = cadrage[(s["jeu"], s["paire"], s["classe"])]
            X[i] = contenus[s["contenu"]] + sf * F + sc * C * ech + cad + inter * sf * cad / max(tau, 1e-9) + bruit[i]
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


def principal(argv):
    stimuli, sortie = pathlib.Path(argv[0]), pathlib.Path(argv[1])
    if sortie.exists():
        sys.exit(f"{sortie} existe déjà (R12)")
    st = json.loads(stimuli.read_text(encoding="utf-8"))["stimuli"]
    comptes, graine = {}, 1000
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        for nom, (a8, a70) in VERITES.items():
            for tau in TAUS:
                for inter in INTERACTIONS:
                    c = collections.Counter()
                    for k in range(REPETITIONS):
                        graine += 2
                        base = tmp / f"{graine}"
                        fabriquer(base / "p", stimuli, st, a8, graine, tau, inter)
                        fabriquer(base / "g", stimuli, st, a70, graine + 1, tau, inter)
                        code = AN.principal([str(stimuli), str(base / "p"), str(base / "g"), str(graine), str(base / "s"),
                                             "--repetition"])
                        if code != 0:
                            c["arrêt"] += 1
                            continue
                        lu = json.loads((base / "s" / "analyse-echelle-v2.json").read_text(encoding="utf-8"))
                        lecture = lu["lecture"].removeprefix("répétition, non décisive (").removesuffix(")")
                        c[lecture + (" (réserve)" if lu["reserves"] else "")] += 1
                    comptes[f"{nom} ; tau {tau} ; interaction {inter}"] = dict(c)
                    print(nom, tau, inter, dict(c), flush=True)
    sortie.mkdir(parents=True)
    f = sortie / "atteignabilite-echelle-v2.json"
    f.write_text(json.dumps({"version": "atteignabilite-echelle-v2", "analyse_sha256": sha(ICI / "analyser_echelle_v2.py"),
                             "stimuli_sha256": sha(stimuli), "n_boot": AN.N_BOOT, "repetitions": REPETITIONS,
                             "comptes": comptes}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(f)
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
