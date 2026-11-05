"""Banc de mutations de SPARKS-EXP7-NUL, v7 : tout le banc v6 (bancs v1 à v6, inchangés, sur leurs essais), et les mutations
neuves de la v7 (appels de modules du script d'instance sous `-I`, amorce et lanceur v7) sur l'essai v7. « Tuée » seulement
au code 1 avec « failed » ; témoins verts exigés.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_sparks_exp7_nul_v7.py [SORTIE.json]
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
T7 = "tests/test_sparks_exp7_nul_v7.py"
A = "scripts/amorce_instance_sparks_exp7_nul_v7.sh"
I = "scripts/sparks_exp7_nul_instance_v7.sh"
L = "scripts/lancer_sparks_exp7_nul_v7.sh"


def _b6():
    spec = importlib.util.spec_from_file_location("banc_v6", RACINE / "scripts" / "banc_mutations_sparks_exp7_nul_v6.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MUTATIONS_V7 = [
    ("instance v7 : ancien appel de l'essai des lots (-I -m)", I, "module controle_ia.sparks_exp7_nul_v3.instance egalite-lots",
     "python -I -B -m controle_ia.sparks_exp7_nul_v3.instance egalite-lots", "trouve_le_paquet or aucun_appel"),
    ("instance v7 : src non posé dans le chemin", I, "import runpy, sys; sys.path.insert(0, sys.argv[1]);", "import runpy, sys; sys.argv[1];",
     "trouve_le_paquet"),
    ("instance v7 : src relatif", I, 'SRC="$PWD/src"', 'SRC="src"', "trouve_le_paquet"),
    ("instance v7 : ancien appel du calcul jouet", I, "then module controle_ia.sparks_exp7_nul_v3.instance jouet",
     "then python -u -I -B -m controle_ia.sparks_exp7_nul_v3.instance jouet", "aucun_appel"),
    ("instance v7 : manifeste sans src", I, "sys.path.insert(0, sys.argv.pop(1))   # -I", "sys.argv.pop(1)   # -I", "manifeste_du_script"),
    ("instance v7 : ancien appel du scellement", I, "module controle_ia.scellement sceller", "python -I -B -m controle_ia.scellement sceller",
     "aucun_appel"),
    ("amorce v7 : script d'instance v6 en fabrication", A, 'PHASE=fabrication BRANCHE="${PREFIXE}sparks-exp7-nul-v5-$COURT" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v7.sh"',
     'PHASE=fabrication BRANCHE="${PREFIXE}sparks-exp7-nul-v5-$COURT" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v6.sh"', "scripts_garde_v7"),
    ("lanceur v7 : amorce v6 passée à la création", L,
     '  --args bash -c "\\$(git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v7.sh")"',
     '  --args bash -c "\\$(git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v6.sh")"', "scripts_garde_v7 or bornee_etiquetee"),
]


def main(argv: list[str]) -> int:
    b6 = _b6()
    b5 = b6._b5()
    b4 = b5._charger("banc_v4")
    b3 = b4._banc_v3()
    b2 = b3._banc_v2()
    toutes = (b2.mutations_v1() + [m + (b2.T2,) for m in b2.MUTATIONS_V2] + [m + (b2.T2,) for m in b3.T2_EN_PLUS]
              + [m + (b3.T3,) for m in b3.MUTATIONS_V3] + [m + (b4.T4,) for m in b4.MUTATIONS_V4]
              + [m + (b5.T5,) for m in b5.MUTATIONS_V5] + [m + (b6.T6,) for m in b6.MUTATIONS_V6]
              + [m + (T7,) for m in MUTATIONS_V7])
    temoins = [("témoin v1", None, None, None, "etiquette or egalite", b2.T1),
               ("témoin v2", None, None, None, "etats_de or go_sain or depense_cas_sain", b2.T2),
               ("témoin v3", None, None, None, "minuterie or ordres or a_priori", b3.T3),
               ("témoin v4", None, None, None, "instance_de_cette_machine or espace_de_processus or lanceur", b4.T4),
               ("témoin v5", None, None, None, "duree_reelle or tir_go or addendum_reconnu or lanceur_inventaire", b5.T5),
               ("témoin v6", None, None, None, "scripts_garde_v6 or tir_go or lanceur or espace_de_processus", b6.T6),
               ("témoin v7", None, None, None, "trouve_le_paquet or manifeste_du_script or aucun_appel or scripts_garde_v7", T7)]
    res = []
    with tempfile.TemporaryDirectory(prefix="banc7-") as t:
        base = Path(t) / "base"
        b3.copier(base)
        for nom, fichier, ancien, nouveau, k, fe in temoins + toutes:
            d = Path(t) / "m"
            shutil.copytree(base, d)
            if fichier:
                f = d / fichier
                s = f.read_text(encoding="utf-8")
                if s.count(ancien) != 1:
                    res.append({"mutation": nom, "statut": "INAPPLICABLE", "occurrences": s.count(ancien)})
                    print(f"INAPPLICABLE {nom} ({s.count(ancien)} occurrences)", flush=True)
                    shutil.rmtree(d)
                    continue
                f.write_text(s.replace(ancien, nouveau), encoding="utf-8")
            code, fin = b3.essai(d, k, fe)
            if fichier is None:
                statut = "TEMOIN VERT" if code == 0 and "passed" in fin else "TEMOIN ROUGE"
            else:
                statut = "TUÉE" if code == 1 and "failed" in fin else "SURVIVANTE"
            res.append({"mutation": nom, "essais": k, "fichier_essais": fe, "statut": statut, "code": code, "fin": fin})
            print(f"{statut:12s} {nom} [{k}] code {code} : {fin}", flush=True)
            if argv:
                Path(argv[0]).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
            shutil.rmtree(d)
    mauvais = [r for r in res if r["statut"] not in ("TUÉE", "TEMOIN VERT")]
    groupes = {"v1": {m[0] for m in b2.mutations_v1()}, "v2": {m[0] for m in b2.MUTATIONS_V2 + b3.T2_EN_PLUS},
               "v3": {m[0] for m in b3.MUTATIONS_V3}, "v4": {m[0] for m in b4.MUTATIONS_V4}, "v5": {m[0] for m in b5.MUTATIONS_V5},
               "v6": {m[0] for m in b6.MUTATIONS_V6}, "v7": {m[0] for m in MUTATIONS_V7}}
    print(" ; ".join(f"{sum(1 for r in res if r['mutation'] in g and r['statut'] == 'TUÉE')}/{len(g)} {n}"
                     for n, g in groupes.items()) + f" tuées (code 1 et « failed ») ; défauts : {len(mauvais)}")
    return 1 if mauvais else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
