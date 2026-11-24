"""Lecture (2) de la diffusion sur la course du saboteur à budget à organisme changé (course v5), version 1. EXPLORATOIRE, NON
OPPOSABLE (R-522). Pièce du côté exposé : jamais transmise au côté des moniteurs.

Spécification scellée : `controle_ia.iib.configuration_lectures_v5.SPECIFICATION` (sections 5.4, 7, 8, 11, 13) ; accord
GO-2026-11-24-37.
    PYTHONPATH=src python scripts/lecture_iib_2_diffusion_v5.py --racine . --run-id RUN --etalonnage ETAL \\
        --registre-decisions <arbre de main>/registres/decisions.md --registre-sondes <arbre de main>/registres/sondes-iib-v1.md \\
        --jetoniseur <dossier jetoniseur/ du commit e5677bbf>
Refuse sans la sortie scellée de la lecture (1) et sa ligne au registre des décisions ; refuse si l'audit de la lecture (1) s'est
déclenché sans relecture consignée, ou si un défaut relevé n'est autorisé par aucune décision postérieure. Les trois variables de
fils de calcul sont posées à « 1 », avant tout chargement de bibliothèque de calcul, si elles ne sont pas déjà posées.
Écrit et scelle `diag/RUN/lecture-iib-2-diffusion-exploratoire-non-opposable-v1.json` et, à part,
`diag/RUN/lecture-iib-2-mots-ponderes-exploratoire-non-opposable-v1.json`. N'imprime que chemins et empreintes.
Codes : 0 sorties écrites et scellées ; 1 refus avant le manifeste (rien d'écrit) ; 3 arrêt après le manifeste (seul
`diag/<run de la lecture>/arret.json` est écrit, avec le motif).
"""
from __future__ import annotations

import os

for _fil in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):     # avant numpy et scipy (règle de la pièce)
    os.environ.setdefault(_fil, "1")

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

CLES_ESSAIS = {"mode", "configuration", "autoriser_depot_sale", "jetoniseur", "bases"}


def main(argv: list[str], essais: dict | None = None) -> int:
    """`essais` : mode jouet seulement (`{"mode": "jouet", "jetoniseur": {…}, "configuration": …, "bases": …,
    "autoriser_depot_sale": …}`) ; sans essais, mode réel."""
    p = argparse.ArgumentParser(prog="lecture_iib_2_diffusion_v5")
    p.add_argument("--racine", default=".")
    p.add_argument("--run-id", required=True)
    p.add_argument("--etalonnage", required=True)
    p.add_argument("--registre-decisions", required=True)
    p.add_argument("--registre-sondes", required=True)
    p.add_argument("--jetoniseur", required=True)
    a = p.parse_args(argv)
    racine = Path(a.racine).resolve()
    try:
        mode = "reel" if essais is None else essais.get("mode")
        if essais is not None and (mode != "jouet" or set(essais) - CLES_ESSAIS):
            raise GardeArret("options d'essai : mode jouet seulement, et clés connues seulement")
        config = cl.pour(mode, None if essais is None else essais.get("configuration"))
        ordre = ev.exiger_ordre_du_temps(a.registre_sondes, mode)
        spec = cl.exiger_specification()
        modules = cl.exiger_modules_d_origine()
        # Garde d'ordre et garde de l'audit (section 7.4, point 2)
        reg = ev.Racines(registres=ev.racine_des_registres(a.registre_sondes))
        registre = ev.ouvrir("registres", cl.REGISTRE_DECISIONS, reg, lecture="chemin")
        if Path(a.registre_decisions).absolute().resolve() != registre.resolve():
            raise GardeArret("registre des décisions hors du dossier registres/ de la racine des registres (ou d'un autre nom)")
        R = ev.Racines(lecture=racine, run_id=a.run_id, etalonnage=a.etalonnage)
        rel_1 = f"diag/{a.run_id}/{cl.NOM_1}"
        if (racine / rel_1).is_file():
            ev.ouvrir("lecture", rel_1, R, lecture="json")                  # relecture stricte de ce qu'ouvre la fonction d'origine
        l1 = lv.exiger_lecture_1_consignee(racine, a.run_id, registre)
        audit = lx.exiger_audit_consigne(l1, ev.ouvrir("registres", cl.REGISTRE_DECISIONS, reg, lecture="lignes"), reg)
        # Même course, même oracle (point 3)
        entrees = ev.charger(racine, a.run_id, a.etalonnage, avec_identifiants=True, mode=mode)
        lx.exiger_meme_course(l1["contenu"], entrees)
        entrees["empreintes"][rel_1] = l1["sha256"]
        # Jetoniseur, identifiants, décodage, fidélité (point 4)
        jet = ev.charger_jetoniseur(a.jetoniseur, entrees, None if essais is None else essais.get("jetoniseur"))
        ev.exiger_identifiants(entrees, jet["V"], jet["fins"], int(entrees["config"]["generation"]["max_nouveaux"]))
        decodes = ev.exiger_fidelite_du_decodage(jet, entrees)
        textes, fiches = ev.fiches_et_textes(decodes, entrees)
        for nom in (cl.NOM_2, cl.NOM_MOTS):
            cible = racine / "diag" / a.run_id / nom
            if cible.exists() or Path(str(cible) + ".sha256").exists():
                raise GardeArret(f"{nom} existe déjà : la lecture (2) se joue une fois (R12)")
        # Graines et manifeste (point 5)
        noms = [entrees["prefixe"] + k for k in cl.CLES_2]
        ev.exiger_aucune_collision(noms, entrees)
        graines = ev.graines_de_lecture(entrees["entropie"], entrees["prefixe"], cl.CLES_2)
        configuration = lx.configuration_du_manifeste(2, entrees, config, spec, modules)
        run_l = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-iib-lecture-2-diffusion-v5"
        sale = bool(essais and essais.get("autoriser_depot_sale"))
        chemin_m, man = mf.creer_manifeste(racine, run_l, configuration, noms, entropie=entrees["entropie"], decisif=False,
                                           autoriser_depot_sale=sale, commande="scripts/lecture_iib_2_diffusion_v5.py")
    except GardeArret as e:
        print(f"ARRÊT (refus avant le manifeste, rien d'écrit) : {e}", file=sys.stderr)
        return 1
    try:
        if any(man["graines"][entrees["prefixe"] + k] != graines[k] for k in cl.CLES_2):
            raise GardeArret("graines du manifeste de la lecture ≠ graines dérivées (R9)")
        n_400 = sum(1 for d in decodes.values() if d["jetons"] == int(entrees["config"]["generation"]["max_nouveaux"]))
        decodage = {**jet["rapport"], "clean_up_tokenization_spaces": jet["nettoyage"], "fins_d_action": sorted(jet["fins"]),
                    "actions_decodees": len(decodes), "actions_au_plafond_d_identifiants": n_400,
                    "fidelite": f"tenue sur {len(decodes)} actions"}
        identite = {"ordre_du_temps": ordre, "audit_de_la_lecture_1": audit, "decodage": decodage,
                    "lecture": {"numero": 2, "run_id": run_l, "manifeste_sha256": verifier(chemin_m), "accord": cl.ACCORD,
                                "specification": {"chemin": cl.SPECIFICATION["chemin"], "sha256": spec}, "modules": modules,
                                "configuration": configuration, "graines": man["graines"]}}
        resultat, mots = lx.lecture_2_v5(entrees, l1, graines, config, identite, textes, fiches,
                                         None if essais is None else essais.get("bases"))
        chemin, sha = lv.ecrire(racine, a.run_id, cl.NOM_2, resultat)
        chemin_mots, sha_mots = lv.ecrire(racine, a.run_id, cl.NOM_MOTS, mots)
    except BaseException as e:
        mf.ecrire_resultat(racine, chemin_m, "arret", {"avertissement": cl.AVERTISSEMENT, "lecture": 2, "course": a.run_id,
                                                        "motif": motif_d_arret(e), "issue": "aucune sortie de lecture écrite"})
        print(f"ARRÊT (après le manifeste {run_l} ; arret.json écrit) : {motif_d_arret(e)}", file=sys.stderr)
        if not isinstance(e, Exception):
            raise
        return 3
    print(f"LECTURE (2) ÉCRITE : {chemin} sha256 {sha} ; mots pondérés à part : {chemin_mots} sha256 {sha_mots} "
          f"(EXPLORATOIRE, NON OPPOSABLE (R-522)) ; manifeste {chemin_m} sha256 {identite['lecture']['manifeste_sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
