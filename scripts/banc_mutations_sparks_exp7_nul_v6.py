"""Banc de mutations de SPARKS-EXP7-NUL, v6 : tout le banc v5 (22 v1, 52 v2, 40 v3, 30 v4, 30 v5, inchangées, sur leurs
essais), et les mutations neuves de la v6 sur l'essai v6. Les scripts v6 sont des copies des scripts v5, à trois lignes près :
on les mute aussi, mais seulement sur ce qui change. « Tuée » seulement au code 1 avec « failed » ; témoins verts exigés.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_sparks_exp7_nul_v6.py [SORTIE.json]
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
T6 = "tests/test_sparks_exp7_nul_v6.py"
A = "scripts/amorce_instance_sparks_exp7_nul_v6.sh"
I = "scripts/sparks_exp7_nul_instance_v6.sh"
L = "scripts/lancer_sparks_exp7_nul_v6.sh"


def _b5():
    spec = importlib.util.spec_from_file_location("banc_v5", RACINE / "scripts" / "banc_mutations_sparks_exp7_nul_v5.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MUTATIONS_V6 = [
    ("amorce v6 : garde du code v5", A, "sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v6'); import garde_code;",
     "sys.path.insert(0, '$P5'); import garde_code;", "scripts_garde_v6"),
    ("amorce v6 : script d'instance v5 en fabrication", A, 'PHASE=fabrication BRANCHE="${PREFIXE}sparks-exp7-nul-v5-$COURT" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v6.sh"',
     'PHASE=fabrication BRANCHE="${PREFIXE}sparks-exp7-nul-v5-$COURT" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v5.sh"', "scripts_garde_v6"),
    ("instance v6 : essais v5 au lieu de v6", I, "tests/test_sparks_exp7_nul_v6.py >", "tests/test_sparks_exp7_nul_v5.py >",
     "scripts_garde_v6"),
    ("lanceur v6 : date du tir ignorée", L, ' ${SPARKS_DATE_TIR:+"$SPARKS_DATE_TIR"})', ")", "scripts_garde_v6"),
    ("lanceur v6 : amorce v5 passée à la création", L,
     '  --args bash -c "\\$(git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v6.sh")"',
     '  --args bash -c "\\$(git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v5.sh")"', "scripts_garde_v6 or bornee_etiquetee"),
    ("v6 : apres-creation renvoyé au lanceur v5", L, '2>&1; bash scripts/lancer_sparks_exp7_nul_v6.sh apres-creation "$F" \\$?\nAvant la création',
     '2>&1; bash scripts/lancer_sparks_exp7_nul_v5.sh apres-creation "$F" \\$?\nAvant la création', "scripts_garde_v6 or bornee_etiquetee"),
]


def main(argv: list[str]) -> int:
    b5 = _b5()
    b4 = b5._charger("banc_v4")
    b3 = b4._banc_v3()
    b2 = b3._banc_v2()
    toutes = (b2.mutations_v1() + [m + (b2.T2,) for m in b2.MUTATIONS_V2] + [m + (b2.T2,) for m in b3.T2_EN_PLUS]
              + [m + (b3.T3,) for m in b3.MUTATIONS_V3] + [m + (b4.T4,) for m in b4.MUTATIONS_V4]
              + [m + (b5.T5,) for m in b5.MUTATIONS_V5] + [m + (T6,) for m in MUTATIONS_V6])
    temoins = [("témoin v1", None, None, None, "etiquette or egalite", b2.T1),
               ("témoin v2", None, None, None, "etats_de or go_sain or depense_cas_sain", b2.T2),
               ("témoin v3", None, None, None, "minuterie or ordres or a_priori", b3.T3),
               ("témoin v4", None, None, None, "instance_de_cette_machine or espace_de_processus or lanceur", b4.T4),
               ("témoin v5", None, None, None, "duree_reelle or tir_go or addendum_reconnu or lanceur_inventaire", b5.T5),
               ("témoin v6", None, None, None, "scripts_garde_v6 or tir_go or lanceur or espace_de_processus", T6)]
    res = []
    with tempfile.TemporaryDirectory(prefix="banc6-") as t:
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
               "v3": {m[0] for m in b3.MUTATIONS_V3}, "v4": {m[0] for m in b4.MUTATIONS_V4},
               "v5": {m[0] for m in b5.MUTATIONS_V5}, "v6": {m[0] for m in MUTATIONS_V6}}
    print(" ; ".join(f"{sum(1 for r in res if r['mutation'] in g and r['statut'] == 'TUÉE')}/{len(g)} {n}"
                     for n, g in groupes.items()) + f" tuées (code 1 et « failed ») ; défauts : {len(mauvais)}")
    return 1 if mauvais else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
