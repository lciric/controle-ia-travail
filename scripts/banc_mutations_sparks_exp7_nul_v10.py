"""Banc de mutations de SPARKS-EXP7-NUL, v10 : tout le banc v9 (bancs v1 à v9, inchangés, sur leurs essais et leurs
fichiers), et les mutations neuves de la v10 (ligne de démarrage comptée, outils installés, destruction de secours par
`python3`, tout refus avant l'ordre consommé détruit, `sleep infinity` si la destruction échoue, `journal-amorce` qui compte
les démarrages) sur l'essai v10. « Tuée » seulement au code 1 avec « failed » ; témoins verts exigés.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_sparks_exp7_nul_v10.py [SORTIE.json]
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
T10 = "tests/test_sparks_exp7_nul_v10.py"
A = "scripts/amorce_instance_sparks_exp7_nul_v10.sh"
L = "scripts/lancer_sparks_exp7_nul_v10.sh"
V = "src/controle_ia/sparks_exp7_nul_v10/vast_lecture.py"


def _b9():
    spec = importlib.util.spec_from_file_location("banc_v9", RACINE / "scripts" / "banc_mutations_sparks_exp7_nul_v9.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MUTATIONS_V10 = [
    ("amorce v10 : ligne de démarrage absente", A, "printf 'AMORCE V10 DEMARRAGE %s : %(%Y-%m-%dT%H:%M:%SZ)T, machine %s, commit %s\\n'",
     ": 'AMORCE V10 DEMARRAGE %s : %(%Y-%m-%dT%H:%M:%SZ)T, machine %s, commit %s\\n'", "demarrage_horodatee"),
    ("amorce v10 : compteur des démarrages non gardé", A, 'N_DEM=$(( N_DEM + 1 )); echo "$N_DEM" > "$R/sparks-v10-demarrages-amorce.txt"',
     "N_DEM=$(( N_DEM + 1 ))", "demarrage_horodatee"),
    ("minuterie v10 : pas de repli par python3", A, "    elif command -v python3 >/dev/null 2>&1; then\n        c=$(python3",
     "    elif false; then\n        c=$(python3", "python3_si_curl"),
    ("amorce v10 : refus qui sort sans détruire", A, '    detruire "refus : $1" 2; }', "    exit 2; }", "refus_a_la_creation"),
    ("amorce v10 : destruction non obtenue, sortie (boucle)", A, '    sleep infinity; exit "$1"; }', '    exit "$1"; }', "non_obtenue"),
    ("amorce v10 : aucune installation des outils", A, "    if command -v apt-get >/dev/null 2>&1 && command -v timeout >/dev/null 2>&1; then",
     "    if false; then", "sans_curl_ni_git"),
    ("amorce v10 : git hors des outils exigés", A, 'OUTILS="curl git python3', 'OUTILS="curl python3', "outils_supposes or sans_curl_ni_git"),
    ("amorce v10 : refus avant la minuterie sans destruction", A,
     '    bash "$R/sparks-v5-minuterie.sh" 0 "$R" "$API" < /dev/null >> "$R/sparks-v5-minuterie.log" 2>&1; local st=$?',
     "    local st=0", "echeance_non"),
    ("journal v10 : démarrages v10 ignorés", V, "rangs = [int(m.group(1)) for l in lignes", "rangs = [] and [int(m.group(1)) for l in lignes",
     "v10_compte or demarrage_horodatee"),
    ("journal v10 : anciennes amorces ignorées", V, "    return max([0, anciens, curl] + rangs)", "    return max([0] + rangs)", "v10_compte"),
    ("lanceur v10 : tir sans attente avant la destruction", L, "-e AMORCE_ATTENTE_REFUS_S=300 ", "", "tir_statique"),
    ("amorce v10 : attente avant destruction non bornée", A, '[ "$a" -le 600 ] || a=600', ":", "attente_avant"),
    ("amorce v10 : script d'instance v9 en fabrication", A,
     'PHASE=fabrication BRANCHE="${PREFIXE}sparks-exp7-nul-v5-$COURT" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v10.sh"',
     'PHASE=fabrication BRANCHE="${PREFIXE}sparks-exp7-nul-v5-$COURT" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v9.sh"',
     "scripts_garde_v10 or v10_scripts"),
]


def main(argv: list[str]) -> int:
    b9 = _b9()
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
              + [m + (b9.T9,) for m in b9.MUTATIONS_V9] + [m + (T10,) for m in MUTATIONS_V10])
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
                "or python3 or outils_supposes or v10_compte or echeance_non or tir_statique or scripts_garde_v10 or v10_scripts", T10)]
    res = []
    with tempfile.TemporaryDirectory(prefix="banc10-") as t:
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
               "v9": {m[0] for m in b9.MUTATIONS_V9}, "v10": {m[0] for m in MUTATIONS_V10}}
    print(" ; ".join(f"{sum(1 for r in res if r['mutation'] in g and r['statut'] == 'TUÉE')}/{len(g)} {n}"
                     for n, g in groupes.items()) + f" tuées (code 1 et « failed ») ; défauts : {len(mauvais)}")
    return 1 if mauvais else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
