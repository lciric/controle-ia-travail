"""Simulations longues de l'instrument « hasard du défenseur » (pièces 6 et 7) — mondes simulés seulement.

Spécification : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-1-hasard-du-defenseur-v3-consolidee.md`.

Joue, à la taille complète (`--taille complete`) :
- G1 : jumeau insensible, ρ ∈ {0 ; 0,3 ; 0,8}, N = 300, B = 999, 2 000 répliques par corrélation ;
- la grille de puissance du § 4 (δ × r × N × ρ), 2 000 répliques par case, B = 999 ;
- le test de mort 1 (instrument) ;
- la puissance de p_Δ (pièce 6) pour le cas sain de G5, 2 000 répliques, puis G5 sain, 1 000 répliques d'autres graines ;
- G5 (a), δ_J = 0,10 puis 0,40, 2 000 répliques ; G5 (b), 2 000 répliques ;
- p_Δ contre le jumeau insensible, N = 300, δ ∈ {0,15 ; 0,20}, et la variante « uniformes communes » à δ = 0,10
  (rapportée à côté, jamais dans la table de référence) ;
- les courbes du § 5 (λ de 0 à 1 par 0,1, πq ∈ {0,01 ; 0,03 ; 0,10}, deux lectures, N = 300, ρ = 0, 2 000 répliques)
  et leur cas sain.
`--taille petite` joue tout à quelques répliques, B = 99 (essais seulement : aucun chiffre lisible).

Aucun modèle, aucun réseau. L'entropie est obligatoire (`--entropie`), sans défaut. La sortie est un JSON neuf ;
le script refuse d'écraser un fichier existant.

Utilisation : PYTHONPATH=src python scripts/simulations_hasard_defenseur_v2.py --entropie N --sortie F.json
              [--taille complete|petite] [--processus P]
"""
from __future__ import annotations

import argparse
import json
import platform
import sys
import time
from pathlib import Path

import numpy as np

from controle_ia.hasard_defenseur_v2 import audit_v2 as A
from controle_ia.hasard_defenseur_v2 import puissance_v2 as P
from controle_ia.hasard_defenseur_v2.erreurs_v2 import RefusPlan
from controle_ia.hasard_defenseur_v2.registre_v2 import empreintes_code

TAILLES = {
    "complete": {"rep": 2000, "rep_g5": 1000, "B": 999},
    "petite": {"rep": 4, "rep_g5": 4, "B": 99},
}


def jouer(entropie: int, taille: str, processus: int, journal=print) -> dict:
    if taille not in TAILLES:
        raise RefusPlan(f"taille inconnue : {taille!r}")
    T = TAILLES[taille]
    rep, B = T["rep"], T["B"]
    indice = iter(range(10**6))  # un indice de cas par case, dans un ordre fixe : graines distinctes entre cases
    out = {"version": "simulations-hasard-defenseur-v2", "taille": taille, "entropie_simulation": entropie,
           "B": B, "repliques": rep, "code": empreintes_code(), "numpy": np.__version__, "python": platform.python_version()}
    t0 = time.time()

    def run(cas, n):
        i = next(indice)
        r = P.repliques(cas, n, entropie, i, B, processus)
        journal(f"[{time.time() - t0:7.0f} s] {cas.nom} ({n} répliques, indice {i})")
        return i, r

    # G1
    g1 = {}
    out["G1"] = {}
    for rho in P.GRILLE_RHO:
        i, r = run(P.cas_g1(rho), rep)
        g1[rho] = P.taux(r, "p_J")
        out["G1"][str(rho)] = {"indice_cas": i, **P.resume(r)}
    out["G1_verdict"] = P.verdict_g1(g1)
    # grille de puissance
    out["puissance"] = []
    rho0 = {}
    for rho in P.GRILLE_RHO:
        for r_ in P.GRILLE_R:
            for n in P.GRILLE_N:
                for d in P.GRILLE_DELTA:
                    i, r = run(P.cas_puissance(d, r_, n, rho), rep)
                    s = P.resume(r)
                    out["puissance"].append({"delta": d, "r": r_, "N": n, "rho": rho, "indice_cas": i, **s})
                    if rho == 0.0 and r_ == 1.0:
                        rho0[(d, n)] = s["p_S"]["alpha_0.05"]
    out["mort_1"] = P.verdict_mort_1(out["G1_verdict"], rho0)
    # G5
    i, r6 = run(P.cas_g5_sain(), rep)
    pw6 = P.taux(r6, "p_delta")
    out["piece6_G5_sain"] = {"indice_cas": i, **P.resume(r6)}
    i, r5 = run(P.cas_g5_sain(), T["rep_g5"])
    out["G5_sain"] = {"indice_cas": i, **P.resume(r5), "verdict": P.verdict_g5_sain(P.taux(r5, "p_delta"), pw6)}
    out["G5_a"] = {}
    for dj in (0.10, 0.40):
        i, r = run(P.cas_g5_a(dj), rep)
        out["G5_a"][str(dj)] = {"indice_cas": i, **P.resume(r), "lignes_regle": P.compter_morts(r),
                                "verdict": P.verdict_g5_artefact(P.taux(r, "p_delta"))}
    i, r = run(P.cas_g5_b(), rep)
    out["G5_b"] = {"indice_cas": i, **P.resume(r), "verdict": P.verdict_g5_artefact(P.taux(r, "p_delta"))}
    out["p_delta_insensible"] = {}
    for d in (0.15, 0.20):
        i, r = run(P.cas_delta_insensible(d), rep)
        out["p_delta_insensible"][str(d)] = {"indice_cas": i, **P.resume(r)}
    i, r = run(P.cas_delta_insensible(0.10), rep)
    out["p_delta_insensible"]["0.1"] = {"indice_cas": i, **P.resume(r)}
    i, r = run(P.cas_delta_insensible(0.10, uniformes_communes=True), rep)
    out["variante_uniformes_communes_hors_table"] = {"delta": 0.10, "indice_cas": i, **P.resume(r)}
    # courbes du § 5
    pieces = tuple(A.piece_independante(piq, 1.0) for piq in A.GRILLE_PIQ)
    courbes = []
    for lecture in ("i", "ii"):
        for lam in A.GRILLE_LAMBDA:
            i = next(indice)
            c = A.point_courbe(300, lam, lecture, pieces, 0.0, entropie, i, rep, B, processus)
            c["indice_cas"] = i
            courbes.append(c)
            journal(f"[{time.time() - t0:7.0f} s] courbe lecture {lecture} λ = {lam}")
    out["courbes_audit"] = courbes
    out["courbes_audit_cas_sain"] = A.verdict_cas_sain(courbes)
    out["duree_s"] = time.time() - t0
    return out


def _json(o):
    if isinstance(o, dict):
        return {str(k): _json(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_json(x) for x in o]
    if isinstance(o, (np.floating, np.integer)):
        return o.item()
    if isinstance(o, np.bool_):
        return bool(o)
    return o


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--entropie", type=int, required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--taille", choices=sorted(TAILLES), required=True)
    ap.add_argument("--processus", type=int, default=1)
    a = ap.parse_args(argv)
    sortie = Path(a.sortie)
    if sortie.exists():
        raise RefusPlan(f"{sortie} existe déjà : on n'écrase jamais (R12)")
    res = jouer(a.entropie, a.taille, a.processus, journal=lambda m: print(m, file=sys.stderr, flush=True))
    sortie.write_text(json.dumps(_json(res), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
