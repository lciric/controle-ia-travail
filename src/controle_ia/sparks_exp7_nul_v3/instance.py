"""Fabrication et contrôle causal sur l'instance, v3 : ceux de la v2, sauf l'a priori de B3 transmis à l'étalonnage
(−1 au « construit inversé » du secours ; contre-lecture du delta v2, point 8). `bases_etalonnage`, `fabriquer` (qui
l'appelle) et `main` sont redéfinies ici ; étape 0, export du départ, essai d'égalité des lots et contrôle causal sont
ceux de la v2.

    python -m controle_ia.sparks_exp7_nul_v3.instance fabriquer --sortie D --depart google/gemma-3-270m-it
    python -m controle_ia.sparks_exp7_nul_v3.instance egalite-lots
    python -m controle_ia.sparks_exp7_nul_v3.instance causal --sortie D --depart … --cle … --reponses … --modeles M [--sans-lots]
    python -m controle_ia.sparks_exp7_nul_v3.instance jouet --sortie D
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ..sparks_exp7_nul_v1 import instance as i1
from ..sparks_exp7_nul_v1 import recette
from ..sparks_exp7_nul_v1.instance import Arret, _ecrire, charger_depart, filtrer_connus  # noqa: F401
from ..sparks_exp7_nul_v2 import causal
from ..sparks_exp7_nul_v2.instance import (CANDIDATS_ETAPE0, COMPLEMENT, COUCHES_DEPART, GEMMA,  # noqa: F401
                                           causal_instance, charger_candidat_hf, egalite_lots_jouet, etape0,
                                           etat_depart_bf16, exporter_couches_depart, partages_depart)
from . import bases


def a_priori_b3(rapport: dict) -> int:
    return -1 if rapport.get("construit") == "construit inversé" else 1


def bases_etalonnage(sortie: Path, rapport: dict, depart, *, est_gemma: bool) -> dict:
    etats, roles = {}, {}
    for mid, r in sorted(rapport["modeles"].items()):
        if not mid.startswith("etal-"):
            continue
        if not r["final"]:
            raise bases.GardeBases(f"étalonnage : {mid} sans modèle dans les bornes")
        etats[r["final"]] = bases.lire_safetensors(Path(sortie) / "modeles" / r["final"] / "final" / "couches.safetensors")
        roles[r["final"]] = r["role"]
    return bases.etalonnage_b3_b4(etats, roles, etat_depart_bf16(depart), depart.config.num_hidden_layers,
                                  suffixes=bases.SUFFIXES_GEMMA if est_gemma else None, a_priori=a_priori_b3(rapport))


def fabriquer(sortie: Path, depart, tok, faits: list[dict], *, nom_depart: str, est_gemma: bool,
              charger_candidat=None, faire_etape0: bool = True, **kw) -> dict:
    """Fabrication de la v1, puis étape 0, B3 et B4 sur l'étalonnage, export des couches du départ ; complément écrit à
    côté du rapport de la v1 (`fabrication-complement-v2.json`, R12)."""
    sortie = Path(sortie)
    if (sortie / COMPLEMENT).exists():
        raise Arret(f"{sortie / COMPLEMENT} existe déjà (R12)")
    r1 = i1.fabriquer(sortie, depart, tok, faits, nom_depart=nom_depart, est_gemma=est_gemma, **kw)
    comp = {"depart": nom_depart, "arrets": []}
    if faire_etape0:
        if est_gemma:
            comp["etape0"] = etape0(partages_depart(faits), charger=charger_candidat
                                    or (lambda i, r: charger_candidat_hf(i, r, sortie / "etape0")))
        else:
            comp["etape0"] = {"au_secours": "mesure du départ de secours seule (déjà au rapport de fabrication)"}
    try:
        comp["bases_etalonnage"] = bases_etalonnage(sortie, r1, depart, est_gemma=est_gemma)
        causal.verifier_noms({k: v for k, v in depart.state_dict().items()},
                             causal.architecture(depart.config, depart.state_dict()), est_gemma=est_gemma)
    except (bases.GardeBases, causal.ArretNoms) as e:
        comp["arrets"].append(f"B3, B4 ou noms des tenseurs incalculables : {e} ; arrêt avant tout service")
    comp["architecture"] = causal.architecture(depart.config, depart.state_dict())
    if not comp["arrets"]:
        comp["sha256_couches_depart"] = exporter_couches_depart(depart, sortie / COUCHES_DEPART)
    _ecrire(sortie / COMPLEMENT, comp)
    if comp["arrets"]:
        raise Arret(comp["arrets"][-1])
    return {**r1, "complement_v2": comp}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="instance_v3")
    sp = ap.add_subparsers(dest="cmd", required=True)
    f = sp.add_parser("fabriquer")
    f.add_argument("--sortie", required=True)
    f.add_argument("--depart", required=True)
    sp.add_parser("egalite-lots")
    c = sp.add_parser("causal")
    for k in ("sortie", "depart", "cle", "modeles"):
        c.add_argument(f"--{k}", required=True)
    c.add_argument("--reponses", required=True, nargs="+")
    c.add_argument("--sans-lots", action="store_true")
    j = sp.add_parser("jouet")
    j.add_argument("--sortie", required=True)
    j.add_argument("--cas", default="vraie01,hh01,ss01,ancre100,etal-e1,etal-e2")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "fabriquer":
            m, tok = charger_depart(a.depart)
            g = a.depart == GEMMA
            faits = recette.faits_auteurs() if g else filtrer_connus(m, tok)
            r = fabriquer(Path(a.sortie), m, tok, faits, nom_depart=a.depart, est_gemma=g)
        elif a.cmd == "egalite-lots":
            r = egalite_lots_jouet()
            print("EGALITE LOTS " + ("OK" if r["egal"] else "ECHEC"))
            return 0 if r["egal"] else 4
        elif a.cmd == "causal":
            m, tok = charger_depart(a.depart)
            g = a.depart == GEMMA
            faits = recette.faits_auteurs() if g else filtrer_connus(m, tok)
            causal_instance(Path(a.sortie), Path(a.cle), [Path(x) for x in a.reponses], Path(a.modeles), m, tok, faits,
                            est_gemma=g, lots=not a.sans_lots)
            print("CAUSAL TERMINE " + ("par lots" if not a.sans_lots else "sans lots (déclaré)"))
            return 0
        else:
            from ..sparks_exp7_nul_v1 import jouet
            m, tok, faits = jouet.depart_jouet()
            r = fabriquer(Path(a.sortie), m, tok, faits, nom_depart="jouet", est_gemma=False, mode="jouet",
                          hyper=recette.Hyper(epochs=2, lr=1e-3), cas_retenus=a.cas.split(","), references_ancre=None,
                          faire_etape0=False)
    except Arret as e:
        print(f"ARRET {e}", file=sys.stderr)
        return 3
    print(f"FABRICATION TERMINEE part_dans_bornes={r['part_dans_bornes']:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
