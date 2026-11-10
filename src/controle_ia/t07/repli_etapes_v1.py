"""Repli de l'étape A en deux temps, pour la variante B (ordre d'exécution de l'étape A, brouillon 2) — v1 (fichier neuf, R12).

La commande `lecture_v2 repli-recalcul` enchaîne le recalcul des activations et l'étape A. L'ordre de la variante B (décision de
la mère, R-2112) place la passe à blanc **entre** les deux : `CODE-T07` contrôlée, puis repli (recalcul et garde d'équivalence),
puis passe à blanc, puis étape A. D'où deux commandes :

1. `repli-seul RACINE RUN_T06 CONFIG_T07` : `repli_recalcul_v1.recalculer` (contrôle d'identité à dose 0, rejeu en forçage, garde
   d'équivalence ; activations écrites sous `donnees/<run>/activations`, dossier absent exigé) ; **rien n'est ouvert** au sens de la
   garde de T0.7 (aucune ligne de registre ni de journal, aucun manifeste de T0.7) ; le rapport est écrit et scellé sous
   `replis-t07/<AAAAMMJJ-HHMMSS>-repli-t07-<mode>/rapport-repli-t07.json`. Codes : 0 garde passée ; 2 refus avant calcul
   (configuration, dossier d'activations déjà présent) ; 3 arrêt R11 (garde d'équivalence, identité, empreinte des adaptateurs :
   une relance sur la même carte, puis nœud — décision de l'ordre, hors du module).
2. `etape-a-apres-repli RACINE RUN_T06 CONFIG_T07 RAPPORT [--registre CHEMIN]` : relit le rapport (sceau ; même run ; empreinte du
   manifeste de 7b égale à celle du recalcul ; garde d'équivalence écrite ; dossier des activations présent), puis
   `lecture_v2.etape_a(…, repli=rapport)` : la garde d'identité au bit près est remplacée par la garde d'équivalence (R11 du
   texte). Codes de l'étape A : 0, 2 (refus de la garde, ou rapport non conforme), 3 (arrêt après le manifeste).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import sceller, verifier
from . import registre_v1 as rg

DOSSIER = "replis-t07"
FICHIER = "rapport-repli-t07.json"
CODE_OK, CODE_REFUS, CODE_ARRET = 0, 2, 3


class RefusRepli(GardeArret):
    """Refus avant tout calcul (code 2)."""


def repli_seul(racine: Path, run_t06: str, config: dict, instant: int | None = None) -> dict:
    """Recalcul et garde d'équivalence seuls ; rapport scellé. `RefusRepli` avant calcul ; `GardeArret` du recalcul : arrêt R11."""
    from . import repli_recalcul_v1 as rr
    from .lecture_v2 import exiger_configuration
    racine = Path(racine)
    try:
        exiger_configuration(config)
    except GardeArret as e:
        raise RefusRepli(f"configuration : {e}") from None
    instant = int(time.time()) if instant is None else int(instant)
    dossier = racine / DOSSIER / (time.strftime("%Y%m%d-%H%M%S", time.gmtime(instant)) + f"-repli-t07-{config['mode']}")
    if dossier.exists():
        raise RefusRepli(f"{dossier} existe déjà (R12)")
    if (racine / "donnees" / run_t06 / "activations").exists():
        raise RefusRepli(f"donnees/{run_t06}/activations existe déjà : le repli ne sert que si les activations sont perdues (R12)")
    rapport = rr.recalculer(racine, run_t06)
    dossier.mkdir(parents=True)
    chemin = dossier / FICHIER
    chemin.write_text(json.dumps({"nature": "repli de l'étape A de T0.7 : recalcul des activations et garde d'équivalence (aucune "
                                            "ouverture)", "run_t06": run_t06, "instant": rg.date_utc(instant), "rapport": rapport},
                                 ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    return {"chemin": str(chemin.relative_to(racine)), "sha256": sceller(chemin), "rapport": rapport}


def lire_rapport(racine: Path, chemin: Path, run_t06: str) -> dict:
    """Rapport du repli relu avant l'étape A ; tout écart → `RefusRepli` (code 2, l'étape ne s'ouvre pas)."""
    racine, chemin = Path(racine), Path(chemin)
    if not chemin.is_absolute():
        chemin = racine / chemin
    try:
        verifier(chemin)
        doc = json.loads(chemin.read_text(encoding="utf-8"))
        r = doc["rapport"]
        if doc.get("run_t06") != run_t06:
            raise RefusRepli(f"rapport du repli : run {doc.get('run_t06')!r} ≠ {run_t06!r}")
        m = r["manifeste_7b"]
        if m["chemin"] != f"runs/{run_t06}/manifeste.json" or verifier(racine / m["chemin"]) != m["sha256"]:
            raise RefusRepli("rapport du repli : manifeste de 7b autre que celui du recalcul")
        if not isinstance(r.get("garde_equivalence"), dict) or "ecart_max" not in r["garde_equivalence"]:
            raise RefusRepli("rapport du repli : garde d'équivalence absente")
        if not (racine / r["dossier_activations"]).is_dir():
            raise RefusRepli(f"rapport du repli : activations recalculées absentes ({r['dossier_activations']})")
    except RefusRepli:
        raise
    except GardeArret as e:
        raise RefusRepli(f"rapport du repli : {e}") from None
    except (OSError, ValueError, KeyError, TypeError) as e:
        raise RefusRepli(f"rapport du repli illisible ({type(e).__name__})") from None
    return r


def main(argv: list[str]) -> int:
    from .lecture_v2 import ArretApresManifeste, charger_configuration, etape_a
    p = argparse.ArgumentParser(prog="python -m controle_ia.t07.lecture_v2", description=__doc__.splitlines()[0])
    sp = p.add_subparsers(dest="action", required=True)
    s = sp.add_parser("repli-seul")
    s.add_argument("racine")
    s.add_argument("run_t06")
    s.add_argument("config_t07")
    e = sp.add_parser("etape-a-apres-repli")
    e.add_argument("racine")
    e.add_argument("run_t06")
    e.add_argument("config_t07")
    e.add_argument("rapport")
    e.add_argument("--registre", default=None)
    a = p.parse_args(argv)
    try:
        config = charger_configuration(Path(a.config_t07))
    except GardeArret as err:
        print(f"REFUS : {err}", file=sys.stderr)
        return CODE_REFUS
    if a.action == "repli-seul":
        try:
            r = repli_seul(Path(a.racine), a.run_t06, config)
        except RefusRepli as err:
            print(f"REFUS : {err}", file=sys.stderr)
            return CODE_REFUS
        except GardeArret as err:
            print(f"ARRÊT (R11, repli) : {err} ; relance une fois sur la même carte, puis nœud", file=sys.stderr)
            return CODE_ARRET
        g = r["rapport"]["garde_equivalence"]
        print(f"repli : garde d'équivalence passée ({g.get('actions')} actions, écart maximal {g.get('ecart_max')}) ; "
              f"rapport {r['chemin']} {r['sha256']}")
        return CODE_OK
    try:
        rapport = lire_rapport(Path(a.racine), Path(a.rapport), a.run_t06)
        registre = Path(a.registre) if a.registre else Path(a.racine) / config["registre"]
        r = etape_a(Path(a.racine), registre, config, a.run_t06, repli=rapport)
    except ArretApresManifeste as err:
        print(f"ARRÊT : {err}", file=sys.stderr)
        return CODE_ARRET
    except GardeArret as err:
        print(f"REFUS : {err}", file=sys.stderr)
        return CODE_REFUS
    print(f"notation scellée, fermée : {r['scores']['chemin']} ; sondes lues {r['index']['sondes_lues']}")
    return CODE_OK
