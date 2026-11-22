"""Simulations longues, aux tailles de la spécification (hors des essais, qui jouent des tailles réduites).

Usage : PYTHONPATH=src python -m controle_ia.audit_apres_coup_v1.simulations_longues [--petit] [--entropie E]

Écrit sur la sortie standard ; rien sous diag/ ni runs/ (un rejeu qui compterait comme mesure demanderait son
manifeste, R9). `--petit` divise les répétitions par 20, pour vérifier que le script tourne.
Les attentes sont celles de la spécification, écrites avant toute exécution ; chaque ligne dit « tient » ou « morte ».
"""
from __future__ import annotations

import argparse
import math
import sys

import numpy as np

from .alerte import PariExces
from .attaque_choisie import (TYPES_ILLUSTRATION, essai_borne_plancher, monde_attaque_choisie, rapport_simule)
from .graines import generateur_auxiliaire
from .oracle_simule import OracleSimule
from .regle_audit import RegleAudit, g_identite
from .score_trompeur import (essai_delai, essai_gain, essai_validite, monde_tenu_a_l_ecart, monde_trompeur,
                             regle_orientee)


def ligne(nom, ok, detail):
    print(f"{nom:70s} {'tient' if ok else 'morte'}  {detail}", flush=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--petit", action="store_true")
    ap.add_argument("--entropie", type=int, default=20261122)
    a = ap.parse_args(argv)
    E, k = a.entropie, (20 if a.petit else 1)
    sig = OracleSimule(1.0, 0.0, 0, "signature")
    print(f"simulations longues ; entropie {E} ; numpy {np.__version__} ; diviseur {k}")

    m = monde_attaque_choisie(5, E, 0.5)
    r = RegleAudit(0.01, 0.015, 0.05, g_identite, 1.6)
    o = essai_borne_plancher(m, r, sig, R=2000 // k)
    ligne("attaque choisie : borne du plancher (R = 2 000, seuil 1 869)", o["tient"], o)
    o = essai_borne_plancher(m, r, sig, R=2000 // k, plancher_artefact=lambda x: np.where(x < 0.5, 0.005, 0.01))
    ligne("artefact : plancher 0,005 aux scores < 0,5, β = 0,015 (doit être refusé)", not o["tient"], o)
    o = essai_borne_plancher(m, r, OracleSimule(0.8, 0.0, 0, "signature"), R=2000 // k)
    ligne("attaque choisie : borne du plancher à q = 0,8 (rang 373)", o["tient"] and o["rang_n95"] == 373, o)
    s = rapport_simule(TYPES_ILLUSTRATION, 0.02, 20000 // k, E)
    ligne("uniforme contre proportionnel (rapport 15,62)", abs(s["rapport"] / 15.625 - 1) < 4 * math.sqrt(2 / (20000 // k)), s["rapport"])

    mt = monde_trompeur(40, E, 0.5, 0.02)
    rt = regle_orientee(g_identite, mt.mu0, mt.sigma)
    o = essai_validite(mt, rt, sig, R=2000 // k)
    ligne("trompeur : couverture de la strate et biais de T̂", o["couverture_tient"] and o["biais_nul"], o)
    o = essai_delai(mt, rt, sig, R=2000 // k)
    ligne("trompeur : délai dans la borne du plancher (prix b/π_min = 5)", o["dans_la_borne"], o)
    me = monde_tenu_a_l_ecart(42, E, 1.0)
    re = regle_orientee(g_identite, me.mu0, me.sigma)
    o = essai_gain(me, re, sig, R=4000 // k, n=400, rang_lu=400)
    ligne("famille tenue à l'écart : sans gain (R = 4 000)", o["sans_gain"], o)

    R, H, m0 = 2000 // k, 4000, 400
    g = generateur_auxiliaire(E, 70)
    connu = naif = corrige = 0
    for _ in range(R):
        ref = int(np.sum(g.random(m0) < 0.10))
        x = (g.random((1, H)) < 0.10).astype(np.int64)
        connu += PariExces(0.05, 0.02, d0=0.10).premieres_alarmes(x)[0] > 0
        naif += PariExces(0.05, 0.02, d0=ref / m0).premieres_alarmes(x)[0] > 0
        corrige += PariExces(0.05, 0.02, reference=(ref, m0)).premieres_alarmes(x)[0] > 0
    tol = 4 * math.sqrt(0.05 * 0.95 / R)
    ligne("alerte d'excès, d0 connu : fausses alarmes ≤ α à 4 000", connu / R <= 0.05 + tol, connu / R)
    ligne("alerte d'excès, d0 estimé sans correction (artefact, doit dépasser α)", naif / R > 0.05 + tol, naif / R)
    ligne("alerte d'excès, d0⁺ de Clopper et Pearson à α/2", corrige / R <= 0.05 + tol, corrige / R)
    return 0


if __name__ == "__main__":
    sys.exit(main())
