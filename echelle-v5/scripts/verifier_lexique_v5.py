#!/usr/bin/env python3
"""Contrôles lexicaux des stimuli de la comparaison d'échelle, sans modèle, dans les deux sens (lignée
« session-depot », 27 octobre 2026 ; contre-lecture n° 4, CLW-07). Décliné de `verifier_lexique_v3.py` (R12), qui ne
regardait que le jeu a et le sens a→b. Sur `echelle-v2.json` et les cadrages de `construire_echelle_v2.py` :
  1. lemmes présents d'un seul côté d'une paire, pour chaque jeu : comparés à ceux des gabarits, rapportés (la garde
     de la v3 ne portait que sur le jeu a) ;
  2. mots courts (moins de quatre lettres, hors du contrôle des lemmes) comptés de chaque côté, par jeu : rapportés ;
  3. sac de mots (code de l'analyse v5), dans les deux sens : appris sur le jeu d'apprentissage d'une moitié, appliqué
     au jeu de mesure de l'autre, scores centrés par moitié : aire rapportée.
Sortie : `controles-lexicaux-echelle-v5.json` (+ `.sha256`).
    python -I -B verifier_lexique_v5.py STIMULI_JSON SORTIE_DOSSIER
"""
import collections
import hashlib
import importlib.util
import json
import pathlib
import re
import sys

import numpy as np

ICI = pathlib.Path(__file__).resolve().parent


def charger(nom, fichier):
    spec = importlib.util.spec_from_file_location(nom, ICI / fichier)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def principal(argv):
    stimuli, sortie = pathlib.Path(argv[0]), pathlib.Path(argv[1])
    if sortie.exists():
        sys.exit(f"{sortie} existe déjà (R12)")
    C = charger("cons", "construire_echelle_v2.py")
    AN = charger("an", "analyser_echelle_v5.py")
    gabarits = set().union(*(C.lemmes(g("which colour is the sky", ("blue", "green", "red", "grey")))
                             for v in C.FORMATS.values() for g in v))
    unilaterales, communs = {}, {}
    for jeu in ("a", "b"):
        unilaterales[jeu], communs[jeu] = {}, {}
        for j, (ev, re_) in enumerate(C.CADRAGES[jeu]):
            le, lr = C.lemmes(ev), C.lemmes(re_)
            seuls = sorted((le - lr) | (lr - le))
            unilaterales[jeu][j] = seuls
            c = sorted(set(seuls) & gabarits)
            if c:
                communs[jeu][j] = c
    courts = {}
    for jeu in ("a", "b"):
        c = {"eval": collections.Counter(), "reel": collections.Counter()}
        for ev, re_ in C.CADRAGES[jeu]:
            for cote, texte in (("eval", ev), ("reel", re_)):
                c[cote].update(m for m in re.findall(r"[a-z']+", texte.lower()) if len(m) < 4)
        mots = sorted(set(c["eval"]) | set(c["reel"]))
        courts[jeu] = {m: [c["eval"][m], c["reel"][m]] for m in mots if c["eval"][m] != c["reel"][m]}
    doc, tab = AN.charger_stimuli(stimuli)
    plan = AN.Plan(tab)
    plis = {p: np.unique(tab["contenu"][tab["pli"] == p]) for p in ("E1", "E2")}
    moities = (plis["E1"], plis["E2"])
    aires = {}
    for s, nom in AN.NOM_SENS.items():
        sc = AN.scores_sac(plan, moities, s)
        aires[nom] = round(AN.aire_sac(plan, sc, np.ones(plan.n), moities, s), 4)
    sortie.mkdir(parents=True)
    f = sortie / "controles-lexicaux-echelle-v5.json"
    f.write_text(json.dumps({"version": "controles-lexicaux-echelle-v5",
                             "stimuli_sha256": hashlib.sha256(stimuli.read_bytes()).hexdigest(),
                             "lemmes_unilateraux": unilaterales, "lemmes_gabarits": sorted(gabarits),
                             "lemmes_unilateraux_communs_aux_gabarits": communs,
                             "mots_courts_asymetriques_eval_reel": courts,
                             "sac_de_mots_centre_par_sens": aires}, ensure_ascii=False, indent=1) + "\n",
                 encoding="utf-8")
    (sortie / (f.name + ".sha256")).write_text(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}\n",
                                               encoding="utf-8")
    print(json.dumps({"sac_de_mots": aires, "communs": communs}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
