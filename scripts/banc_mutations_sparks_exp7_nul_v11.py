"""Banc de mutations de SPARKS-EXP7-NUL, v11 : tout le banc v10 (bancs v1 à v10, inchangés, sur leurs essais et leurs
fichiers), et les mutations neuves de la v11 (arrêt par l'interface de Vast en fin normale de phase, vérifié ; destruction
si l'arrêt n'est pas obtenu ; mode jouet sur machine réelle ; attentes bornées ; protocole du troisième tir) sur l'essai
v11. « Tuée » seulement au code 1 avec « failed » ; témoins verts exigés.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_sparks_exp7_nul_v11.py [SORTIE.json]
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
T11 = "tests/test_sparks_exp7_nul_v11.py"
A = "scripts/amorce_instance_sparks_exp7_nul_v11.sh"
L = "scripts/lancer_sparks_exp7_nul_v11.sh"


def _b10():
    spec = importlib.util.spec_from_file_location("banc_v10", RACINE / "scripts" / "banc_mutations_sparks_exp7_nul_v10.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MUTATIONS_V11 = [
    ("arrêt v11 : succès non vérifié", A,
     '    case "$c" in 2??) grep -qiE \'"success"[[:space:]]*:[[:space:]]*true\' "$corps" 2>/dev/null && ok=oui;; esac',
     '    case "$c" in 2??) ok=oui;; esac', "arret_non_obtenu"),
    ("arrêt v11 : code HTTP non vérifié", A, '    case "$c" in 2??) grep -qiE', '    case "2$c" in 2*) grep -qiE', "arret_non_obtenu"),
    ("arrêt v11 : arrêt non obtenu sans destruction", A, '    detruire "arrêt non obtenu : $1" "${2:-0}"; }', '    exit "${2:-0}"; }',
     "arret_non_obtenu or arret_sans_reponse"),
    ("arrêt v11 : mauvaise méthode par python3", A, 'q = urllib.request.Request(sys.argv[1], method="PUT", data=',
     'q = urllib.request.Request(sys.argv[1], method="PATCH", data=', "arret_obtenu"),
    ("arrêt v11 : état demandé faux", A, '-d \'{"state": "stopped"}\'', '-d \'{"state": "running"}\'', "arret_obtenu"),
    ("arrêt v11 : fin de fabrication sans arrêt", A, '    arreter_instance "fin de la fabrication, code $code" "$code"', '    exit "$code"', "v11_fins"),
    ("arrêt v11 : fin de copie sans arrêt", A, 'consigner_fin; arreter_instance "fin de la fenêtre de copie" 0 ;;', 'consigner_fin; exit 0 ;;', "v11_fins"),
    ("arrêt v11 : fin causale sans arrêt", A, '        arreter_instance "fin de la phase causale, code $code" "$code" ;;', '        exit "$code" ;;',
     "fin_causale_arret or v11_fins"),
    ("jouet machine v11 : addendum factice non exigé", A,
     '       && grep -q "ADDENDUM FACTICE DE RÉPÉTITION" "$R/amorce-depot/prereg/SPARKS-EXP7-NUL-addendum-1.md" 2>/dev/null; then',
     '       && true; then', "fabrication_factice"),
    ("jouet machine v11 : mode réel admis", A, '    if [ "${MODE:-reel}" = jouet ] && [ "${JOUET_MACHINE:-}" = 1 ]',
     '    if [ "${JOUET_MACHINE:-}" = 1 ]', "fabrication_factice"),
    ("attente fin v11 : non bornée", A, 'AF=$(borne_s "${AMORCE_ATTENTE_FIN_S:-0}" 600)', 'AF=${AMORCE_ATTENTE_FIN_S:-0}', "v11_fins"),
    ("lanceur v11 : tir sans mode jouet", L, "-e MODE=jouet -e JOUET_MACHINE=1 ", "", "tir_statique"),
    ("lanceur v11 : commit de tir sans addendum factice", L, 'git show "$CODE:src/controle_ia/sparks_exp7_nul_v8/addendum_factice.py" > "\\$T/addendum_factice.py" && ',
     ': && ', "mode_tir or tir_statique"),
]


def main(argv: list[str]) -> int:
    b10m = _b10()
    b9 = b10m._b9()
    b8 = b9._b8()
    b6 = b8._b6()
    b5 = b6._b5()
    b4 = b5._charger("banc_v4")
    b3 = b4._banc_v3()
    b2 = b3._banc_v2()
    toutes = (b2.mutations_v1() + [m + (b2.T2,) for m in b2.MUTATIONS_V2] + [m + (b2.T2,) for m in b3.T2_EN_PLUS]
              + [m + (b3.T3,) for m in b3.MUTATIONS_V3] + [m + (b4.T4,) for m in b4.MUTATIONS_V4]
              + [m + (b5.T5,) for m in b5.MUTATIONS_V5] + [m + (b6.T6,) for m in b6.MUTATIONS_V6]
              + [m + (b8.T8,) for m in b8.MUTATIONS_V7] + [m + (b8.T8,) for m in b8.MUTATIONS_V8]
              + [m + (b9.T9,) for m in b9.MUTATIONS_V9] + [m + (b10m.T10,) for m in b10m.MUTATIONS_V10]
              + [m + (T11,) for m in MUTATIONS_V11])
    temoins = [("témoin v1", None, None, None, "etiquette or egalite", b2.T1),
               ("témoin v2", None, None, None, "etats_de or go_sain or depense_cas_sain", b2.T2),
               ("témoin v3", None, None, None, "minuterie or ordres or a_priori", b3.T3),
               ("témoin v4", None, None, None, "instance_de_cette_machine or espace_de_processus or lanceur", b4.T4),
               ("témoin v5", None, None, None, "duree_reelle or tir_go or addendum_reconnu or lanceur_inventaire", b5.T5),
               ("témoin v6", None, None, None, "scripts_garde_v6 or tir_go or lanceur or espace_de_processus", b6.T6),
               ("témoin v8", None, None, None, "trouve_le_paquet or aucun_appel or scripts_garde_v8 or manifeste or addendum_factice or v8_scripts", b8.T8),
               ("témoin v9", None, None, None, "lanceur or offres or boucle or journal_amorce or perimetre or no_such_ask or fin_avant "
                "or consomme or message_exact or creation_relancee or efface or ordre or scripts_garde_v9 or v9_scripts or tir_statique or identifiants or meme_seconde", b9.T9),
               ("témoin v10", None, None, None, "demarrage_horodatee or refus_a_la_creation or non_obtenue or attente_avant or sans_curl "
                "or python3 or outils_supposes or v10_compte or echeance_non or tir_statique or scripts_garde_v10 or v10_scripts", b10m.T10),
               ("témoin v11", None, None, None, "arret or fin_causale or fabrication_factice or v11_fins or mode_tir or tir_statique "
                "or scripts_garde_v11 or v11_scripts or demarrage_horodatee or sans_curl", T11)]
    res = []
    with tempfile.TemporaryDirectory(prefix="banc11-") as t:
        base = Path(t) / "base"
        b3.copier(base)
        for nom, fichier, ancien, nouveau, k, fe in temoins + toutes:
            d = Path(t) / "m"
            shutil.copytree(base, d, symlinks=True)
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
               "v6": {m[0] for m in b6.MUTATIONS_V6}, "v7": {m[0] for m in b8.MUTATIONS_V7}, "v8": {m[0] for m in b8.MUTATIONS_V8},
               "v9": {m[0] for m in b9.MUTATIONS_V9}, "v10": {m[0] for m in b10m.MUTATIONS_V10},
               "v11": {m[0] for m in MUTATIONS_V11}}
    print(" ; ".join(f"{sum(1 for r in res if r['mutation'] in g and r['statut'] == 'TUÉE')}/{len(g)} {n}"
                     for n, g in groupes.items()) + f" tuées (code 1 et « failed ») ; défauts : {len(mauvais)}")
    return 1 if mauvais else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
