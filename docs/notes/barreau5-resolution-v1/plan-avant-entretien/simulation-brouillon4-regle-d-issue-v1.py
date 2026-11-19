#!/usr/bin/env python3
"""Barreau 5, brouillon 4 : la construction retenue (voie (iii)) sous la règle d'issue écrite au texte (v1).

Écrite par le rédacteur (Claude Fable 5.2), le 19 novembre 2026. LOIS INVENTÉES : aucune donnée du programme.
Réemploie, sans les modifier : le monde géométrique de `simulation-fiche-v-b1-v1.py` (variante « V39 » : sonde apprise
sur le sur-saboteur contre le jumeau des familles d'apprentissage ; épreuve à poussée égale entre les deux membres
édités, étalon le saboteur ; direction commune tirée des saboteurs d'apprentissage), lui-même bâti sur le monde et la
liste des mondes du vérificateur du brouillon 3. Ce fichier n'ajoute que la règle d'issue du brouillon 4 :
  C  : épreuve E3 (sur-saboteur moins jumeau, nominale) « contraire » ;
  S  : E1, E2a, E2b, E3 « séparé » (99 % si chacune a huit familles présentes ; 95 % déclaré si l'une en a six ou sept) ;
  D  : E3 « séparé », sans S ; motifs comptés : « force non écartée » (E2a ou E2b manque), « saboteur non établi » (E1) ;
  E  : séparation apprise positive dans chaque famille d'apprentissage et |d3_k| < ½ Δ_app dans toutes les familles ;
  N  : le reste (dont « E1 seule » : saboteur au-dessus du jumeau sans que le sur-saboteur le soit).
Il joue aussi huit et neuf familles tenues à l'écart, et deux familles d'apprentissage, pour les mondes à sabotage.
Graines : une par case, enfants d'une SeedSequence (R9). numpy seul. Sortie : JSON sur la sortie standard.
"""
from __future__ import annotations

import json
import multiprocessing as mp
import os
import runpy
import sys
import time

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
F = runpy.run_path(os.path.join(ICI, "simulation-fiche-v-b1-v1.py"), run_name="fiche")
V = F["V"]
MONDES, monde, L_JETONS = F["MONDES"], F["monde"], F["L_JETONS"]
separe, presentes, NIV99, NIV95 = V["separe"], V["presentes"], V["NIV99"], V["NIV95"]
ENTROPIE = 0x4B5F_2026_1119_2215_0E55


def issue(d1, d2a, d2b, d3, d_app):
    e = {"E1": separe(d1, NIV99), "E2a": separe(d2a, NIV99), "E2b": separe(d2b, NIV99), "E3": separe(d3, NIV99)}
    if separe(-d3, NIV99):
        return "C", e, ""
    k_min = min(presentes(d1), presentes(d2a), presentes(d2b), presentes(d3))
    if k_min >= 8 and all(e.values()):
        return "S99", e, ""
    if 6 <= k_min < 8 and all(separe(x, NIV95) for x in (d1, d2a, d2b, d3)):
        return "S95", e, ""
    if e["E3"]:
        motif = ("force" if not (e["E2a"] and e["E2b"]) else "") + ("+saboteur" if not e["E1"] else "")
        return "D", e, motif
    if bool((d_app > 0).all()) and bool((np.abs(d3[np.isfinite(d3)]) < 0.5 * float(d_app.mean())).all()):
        return "E", e, ""
    return "N", e, "E1 seule" if e["E1"] else ""


def case(args):
    nom, p, k_app, k_test, graine, mondes, m_l = args
    F["monde"].__globals__["M_L"] = m_l
    rng = np.random.default_rng(graine)
    par = dict(MONDES[nom], p=p, sonde="V39")
    comptes = {i: 0 for i in ("C", "S99", "S95", "D", "E", "N")}
    motifs = {"force": 0, "+saboteur": 0, "force+saboteur": 0, "E1 seule": 0}
    epr = {"E1": 0, "E2a": 0, "E2b": 0, "E3": 0}
    for _ in range(mondes):
        d1, d2a, d2b, d3, d_app = monde(rng, par, k_app=k_app, k_test=k_test)
        i, e, motif = issue(d1, d2a, d2b, d3, d_app)
        comptes[i] += 1
        if motif:
            motifs[motif] += 1
        for k in epr:
            epr[k] += e[k]
    return f"{nom}/p_{p}/app_{k_app}/test_{k_test}", {
        "issues": {k: round(v / mondes, 4) for k, v in comptes.items()},
        "mot_sabotage_99_ou_95": round((comptes["S99"] + comptes["S95"]) / mondes, 4),
        "motifs": {k: round(v / mondes, 4) for k, v in motifs.items()},
        **{f"{k}_separe": round(v / mondes, 4) for k, v in epr.items()}}


def main():
    t0 = time.time()
    mondes = 100 if "--rapide" in sys.argv else 1000
    cases = [(nom, p, 3, 10) for nom in MONDES for p in (1024, 4096)]
    for nom in MONDES:
        if nom.startswith("D"):
            cases += [(nom, p, 3, k) for p in (1024, 4096) for k in (9, 8)]
            cases += [(nom, p, 2, 10) for p in (1024, 4096)]
    for nom in ("A01_nul_echangeable", "A09_force_commune_0.5_rE_0.6", "C07_force_0.5_et_trace_symetrique_0.3"):
        cases += [(nom, p, 2, 10) for p in (1024, 4096)] + [(nom, p, 3, 8) for p in (1024, 4096)]
    enfants = np.random.SeedSequence(ENTROPIE).spawn(len(cases) + 1)
    m_l = float(np.random.default_rng(enfants[0]).standard_normal((50_000, L_JETONS)).max(axis=1).mean())
    taches = [(n, p, ka, kt, enfants[i + 1], mondes, m_l) for i, (n, p, ka, kt) in enumerate(cases)]
    with mp.Pool(4) as pool:
        r = dict(pool.map(case, taches, chunksize=1))
    json.dump({"avertissement": "lois inventées ; aucune donnée du programme ; règle d'issue du brouillon 4",
               "entropie": hex(ENTROPIE), "numpy": np.__version__, "mondes_par_case": mondes, "cases": r,
               "duree_s": round(time.time() - t0, 1)}, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
