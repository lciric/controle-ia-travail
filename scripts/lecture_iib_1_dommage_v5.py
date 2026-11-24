"""Lecture (1) du dommage sur la course du saboteur à budget à organisme changé (course v5), version 1. EXPLORATOIRE, NON
OPPOSABLE (R-522). Pièce du côté exposé : jamais transmise au côté des moniteurs.

Spécification scellée : `controle_ia.iib.configuration_lectures_v5.SPECIFICATION` (sections 5.4, 6, 8, 11, 13) ; accord
GO-2026-11-24-37.
    PYTHONPATH=src python scripts/lecture_iib_1_dommage_v5.py --racine . --run-id RUN --etalonnage ETAL \\
        --registre-sondes <arbre de main>/registres/sondes-iib-v1.md
Ordre : contrôle de l'ordre du temps (T0), spécification et modules d'origine à leurs empreintes, contrôles E0 à E9, refus si la
sortie existe ; graines et manifeste de la lecture (arbre propre exigé) ; calcul ; écriture scellée de
`diag/RUN/lecture-iib-1-dommage-exploratoire-non-opposable-v1.json`. N'imprime que chemins, empreintes et « audit R4 déclenché :
oui » ou « non » : aucune phrase, aucun état, aucune valeur mesurée.
Codes : 0 sortie écrite et scellée ; 1 refus avant le manifeste (rien d'écrit) ; 3 arrêt après le manifeste (seul
`diag/<run de la lecture>/arret.json` est écrit, avec le motif).
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

from controle_ia import manifeste as mf
from controle_ia.gardes import GardeArret, motif_d_arret
from controle_ia.iib import configuration_lectures_v5 as cl
from controle_ia.iib import entrees_lectures_v5 as ev
from controle_ia.iib import lecture_v1 as lv
from controle_ia.iib import lectures_v5 as lx
from controle_ia.scellement import verifier


def main(argv: list[str], essais: dict | None = None) -> int:
    """`essais` : mode jouet seulement (`{"mode": "jouet", "configuration": …, "autoriser_depot_sale": …}`) ; sans essais, mode réel."""
    p = argparse.ArgumentParser(prog="lecture_iib_1_dommage_v5")
    p.add_argument("--racine", default=".")
    p.add_argument("--run-id", required=True)
    p.add_argument("--etalonnage", required=True)
    p.add_argument("--registre-sondes", required=True)
    a = p.parse_args(argv)
    racine = Path(a.racine).resolve()
    try:
        mode = "reel" if essais is None else essais.get("mode")
        if essais is not None and (mode != "jouet" or set(essais) - {"mode", "configuration", "autoriser_depot_sale"}):
            raise GardeArret("options d'essai : mode jouet seulement, et clés connues seulement")
        config = cl.pour(mode, None if essais is None else essais.get("configuration"))
        ordre = ev.exiger_ordre_du_temps(a.registre_sondes, mode)
        spec = cl.exiger_specification()
        modules = cl.exiger_modules_d_origine()
        entrees = ev.charger(racine, a.run_id, a.etalonnage, mode=mode)
        cible = racine / "diag" / a.run_id / cl.NOM_1
        if cible.exists() or Path(str(cible) + ".sha256").exists():
            raise GardeArret(f"{cl.NOM_1} existe déjà : la lecture (1) se joue une fois (R12)")
        noms = [entrees["prefixe"] + k for k in cl.CLES_1]
        ev.exiger_aucune_collision(noms, entrees)
        graines = ev.graines_de_lecture(entrees["entropie"], entrees["prefixe"], cl.CLES_1)
        configuration = lx.configuration_du_manifeste(1, entrees, config, spec, modules)
        run_l = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-iib-lecture-1-dommage-v5"
        sale = bool(essais and essais.get("autoriser_depot_sale"))
        chemin_m, man = mf.creer_manifeste(racine, run_l, configuration, noms, entropie=entrees["entropie"], decisif=False,
                                           autoriser_depot_sale=sale, commande="scripts/lecture_iib_1_dommage_v5.py")
    except GardeArret as e:
        print(f"ARRÊT (refus avant le manifeste, rien d'écrit) : {e}", file=sys.stderr)
        return 1
    try:
        if any(man["graines"][entrees["prefixe"] + k] != graines[k] for k in cl.CLES_1):
            raise GardeArret("graines du manifeste de la lecture ≠ graines dérivées (R9)")
        identite = {"ordre_du_temps": ordre,
                    "lecture": {"numero": 1, "run_id": run_l, "manifeste_sha256": verifier(chemin_m), "accord": cl.ACCORD,
                                "specification": {"chemin": cl.SPECIFICATION["chemin"], "sha256": spec}, "modules": modules,
                                "configuration": configuration, "graines": man["graines"]}}
        contenu = lx.lecture_1_v5(entrees, graines, config, identite)
        chemin, sha = lv.ecrire(racine, a.run_id, cl.NOM_1, contenu)
    except BaseException as e:
        mf.ecrire_resultat(racine, chemin_m, "arret", {"avertissement": cl.AVERTISSEMENT, "lecture": 1, "course": a.run_id,
                                                        "motif": motif_d_arret(e), "issue": "aucune sortie de lecture écrite"})
        print(f"ARRÊT (après le manifeste {run_l} ; arret.json écrit) : {motif_d_arret(e)}", file=sys.stderr)
        if not isinstance(e, Exception):
            raise
        return 3
    print(f"LECTURE (1) ÉCRITE : {chemin} sha256 {sha} (EXPLORATOIRE, NON OPPOSABLE (R-522)) ; manifeste {chemin_m} "
          f"sha256 {identite['lecture']['manifeste_sha256']}")
    print(f"audit R4 déclenché : {'oui' if contenu['audit_R4']['declenche'] else 'non'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
