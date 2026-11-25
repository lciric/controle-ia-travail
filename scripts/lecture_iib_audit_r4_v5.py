"""Affichage de l'audit de symétrie (R4) de la lecture (1) sur la course v5, version 1. EXPLORATOIRE, NON OPPOSABLE (R-522).
Pièce du côté exposé : jamais transmise au côté des moniteurs.

Spécification scellée : `controle_ia.iib.configuration_lectures_v5.SPECIFICATION` (section 6.3) ; accord GO-2026-11-24-37.
    PYTHONPATH=src python scripts/lecture_iib_audit_r4_v5.py --racine . --run-id RUN --etalonnage ETAL --jetoniseur DOSSIER
Gardes, dans cet ordre (précédées de la spécification et des modules d'origine à leurs empreintes) : (1) sortie de la lecture (1)
présente, scellée, audit déclenché ; (2) contrôles E0 à E10, même course et même oracle que cette sortie ; (3) échantillon lu dans
la sortie scellée égal à l'échantillon retiré par le calcul du module d'origine, graine redérivée égale à celle que la sortie
consigne ; (4) jetoniseur, identifiants, décodage et fidélité sur toutes les actions de l'évaluation. Puis affichage, sur la sortie
standard seulement, des vingt actions : textes rebâtis en mémoire, préfixe jusqu'à la coupe, lectures des deux oracles.
**N'écrit rien sur disque** : ni manifeste, ni fichier d'arrêt, ni sortie. Codes : 0 après l'affichage ; 1 sur toute garde.
La relecture est consignée par la session mère au registre des décisions (`AUDIT-R4-LECTURE-1-IIB`, `ISSUE=…`).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.iib import configuration_lectures_v5 as cl
from controle_ia.iib import entrees_lectures_v5 as ev
from controle_ia.iib import lectures_v5 as lx


def main(argv: list[str], essais: dict | None = None) -> int:
    """`essais` : mode jouet seulement (`{"mode": "jouet", "jetoniseur": {…}, "configuration": …}`) ; sans essais, mode réel."""
    p = argparse.ArgumentParser(prog="lecture_iib_audit_r4_v5")
    p.add_argument("--racine", default=".")
    p.add_argument("--run-id", required=True)
    p.add_argument("--etalonnage", required=True)
    p.add_argument("--jetoniseur", required=True)
    a = p.parse_args(argv)
    racine = Path(a.racine).resolve()
    try:
        mode = "reel" if essais is None else essais.get("mode")
        if essais is not None and (mode != "jouet" or set(essais) - {"mode", "configuration", "jetoniseur"}):
            raise GardeArret("options d'essai : mode jouet seulement, et clés connues seulement")
        config = cl.pour(mode, None if essais is None else essais.get("configuration"))
        if mode == "reel" and racine != cl.racine_du_code().resolve():
            raise GardeArret("mode réel : la racine de lecture doit être la racine du code qui tourne (section 2)")
        cl.exiger_specification()
        cl.exiger_modules_d_origine()
        # (1)
        R = ev.Racines(lecture=racine, run_id=a.run_id, etalonnage=a.etalonnage)
        rel_1 = f"diag/{a.run_id}/{cl.NOM_1}"
        sha_1 = ev.ouvrir("lecture", rel_1, R, lecture="scelle")
        l1 = ev.ouvrir("lecture", rel_1, R, lecture="json")
        audit_r4 = l1.get("audit_R4") if isinstance(l1, dict) else None
        declenche = audit_r4.get("declenche") if isinstance(audit_r4, dict) else None
        if not isinstance(declenche, bool):
            raise GardeArret("audit : audit_R4.declenche absent ou non booléen dans la sortie de la lecture (1)")
        if not declenche:
            raise GardeArret("audit non déclenché : rien à relire")
        # (2)
        entrees = ev.charger(racine, a.run_id, a.etalonnage, avec_identifiants=True, mode=mode)
        lx.exiger_meme_course(l1, entrees)
        # (3)
        cle = entrees["prefixe"] + "iib/lecture-1/audit"
        graine = ev.graines_de_lecture(entrees["entropie"], entrees["prefixe"], ["iib/lecture-1/audit"])["iib/lecture-1/audit"]
        consignee = ((l1.get("lecture") or {}).get("graines") or {}).get(cle)
        if consignee != graine:
            raise GardeArret("audit : graine consignée par la sortie ≠ graine redérivée de l'entropie de la course")
        lu_conf = (((l1.get("lecture") or {}).get("configuration") or {}).get("constantes") or {}).get("lecture_1") or {}
        if lu_conf.get("audit_echantillon") != config["lecture_1"]["audit_echantillon"]:
            raise GardeArret("audit : taille de l'échantillon consignée ≠ celle de la configuration des lectures")
        retire = lx.echantillon_de_l_audit(entrees, config, graine)
        if l1["audit_R4"].get("echantillon") != retire:
            raise GardeArret("audit : échantillon de la sortie scellée ≠ échantillon retiré par le calcul du module d'origine")
        # (4)
        jet = ev.charger_jetoniseur(a.jetoniseur, entrees, None if essais is None else essais.get("jetoniseur"))
        ev.exiger_identifiants(entrees, jet["V"], jet["fins"], int(entrees["config"]["generation"]["max_nouveaux"]))
        decodes = ev.exiger_fidelite_du_decodage(jet, entrees)
        prefixes = {}
        for x in retire:
            c, t, pas = x["condition"], x["tache"], x["pas"]
            rang = entrees["evaluation"][entrees["oracle"]][c][t][pas]["rang_coupe"]
            prefixes[(c, t, pas)] = (ev.decoder(jet, decodes[(c, t, pas)]["ids"][:rang], f"evaluation-{c}/{t}#{pas}")
                                     if rang is not None else None)
    except GardeArret as e:
        print(f"ARRÊT (audit, rien d'écrit) : {e}", file=sys.stderr)
        return 1
    print(f"AUDIT R4 DE LA LECTURE (1) — course {a.run_id}, sortie sha256 {sha_1} ; EXPLORATOIRE, NON OPPOSABLE (R-522) ; "
          f"{len(retire)} actions ; rien n'est écrit sur disque")
    for k, x in enumerate(retire, start=1):
        c, t, pas = x["condition"], x["tache"], x["pas"]
        d = decodes[(c, t, pas)]
        lignes = {o: entrees["evaluation"][o][c][t][pas] for o in ("N", "P")}
        prefixe = prefixes[(c, t, pas)]
        print(f"\n=== {k}. condition {c}, tâche {t}, pas {pas} ===")
        print("--- texte de l'action ---")
        print(d["texte"])
        print("--- préfixe jusqu'à la coupe ---")
        print(prefixe if prefixe is not None else "(aucune coupe conforme)")
        for o in ("N", "P"):
            l = lignes[o]
            print(f"--- oracle {o}{' (désigné)' if o == entrees['oracle'] else ''} : coût déclaré {l['cout_declare']}, estimation "
                  f"{l['estimation']}, excès {l['exces']}, bornable {l['bornable']}")
            for i, s in enumerate(l["suites"]):
                print(f"    suite {i} : valeur {s.get('valeur')}, lisible {s.get('lisible')}, formes {s.get('formes')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
