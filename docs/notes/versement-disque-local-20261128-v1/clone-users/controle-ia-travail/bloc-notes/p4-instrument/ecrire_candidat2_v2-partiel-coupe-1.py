"""Candidat 2 de P4-instrument, tiré du candidat 1 par des paires exactes (ancien → nouveau), chacune trouvée une seule
fois. Sources des corrections : contre-lecture 3 (`contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md`,
7f947de0…), notes de la chaîne (`chaine/NOTES-CHAINE.md`, points T1 à T3), puis les paires du fichier JSON passé en
argument (relectures de la chaîne, module v2, section « Contre-lecture »), écrites après leurs rapports.

Usage : python -B ecrire_candidat2_v1.py CANDIDAT1 SORTIE MODULE_DIR CHAINE_DIR TESTS_ATTENDUS PAIRES_JSON
  MODULE_DIR : dossier des six fichiers du module retenu (leurs empreintes remplacent celles du candidat 1).
  CHAINE_DIR : dossier où sont l'amorce et le script de l'instance retenus (empreintes citées).
  PAIRES_JSON : liste de {"ancien": …, "nouveau": …, "source": …}, appliquées après les paires fixes.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

DOSSIER = "docs/procedures/P4-instrument-v1"
NOMS_MODULE = ("mesures_conception_p4_v1.py", "instrument_p4_v1.py", "lecture_p4_v1.py", "test_instrument_p4_v1.py",
               "test_lecture_p4_v1.py", "test_gardes_p4_v1.py")
ANCIENNES = {
    "mesures_conception_p4_v1.py": "483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7",
    "instrument_p4_v1.py": "6e0e026eafba28e708fea009cc5c81c8b95defe6aa8f9fc2f76dd364ee29b06c",
    "lecture_p4_v1.py": "51a25e30a70b2439046e87037d6e2fcb26616289a017ef10689d66c0ca50e213",
    "test_instrument_p4_v1.py": "9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd",
    "test_lecture_p4_v1.py": "49441971b81a89fe4b0dcc392efa7eba81234972d1d8e60abd4cececa33111d9",
    "test_gardes_p4_v1.py": "f4f97029f9a1fb9d9d1b29bac162334305a001b091319fde250e188071e092f5",
}

# (ancien, nouveau, source)
PAIRES_FIXES = [
    ("— v1, candidat 1\n", "— v1, candidat 2\n", "candidat 2"),
    # CL3-07 : ordre des dates
    ("brouillon 3 le 2026-10-20 vers 11:00 UTC ; candidat 1 le 2026-10-20 vers\n  14:54 UTC ; brouillon 4 le 2026-10-20 vers\n  13:49 UTC.",
     "brouillon 3 le 2026-10-20 vers 11:00 UTC ; brouillon 4 le 2026-10-20 vers\n  13:49 UTC ; candidat 1 le 2026-10-20 vers 14:54 UTC ; candidat 2 le 2026-10-20 (corrections de la contre-lecture 3\n  et des relectures de la chaîne).",
     "CL3-07"),
    # T1 : commit du code d'analyse (forme lue par la chaîne et par exiger_code_cite)
    ("- Commit du code d'analyse : celui du scellement S. Le module de P4 est hors de l'arbre gelé",
     "- Commit du code d'analyse : `7a54d431d89745839220f882b41b13e8c62ecfdd`. C'est le commit gelé de P3 (instrument figé) :\n  l'arbre gelé du commit de scellement S doit lui être égal. Le module de P4 est hors de l'arbre gelé",
     "NOTES-CHAINE T1"),
    # CL3-08 : mentions « au candidat » périmées
    ("(à relire et à recopier au\n  candidat)", "(à relire au scellement S)", "CL3-08"),
    ("(huit colonnes après R-281 ; à relire au candidat)", "(huit colonnes après R-281 ; à relire au scellement S)", "CL3-08"),
    # CL3-09 : empreinte complète ; dérivation écrite
    ("(`33ee8659…`, R12)", "(`33ee865997b78f7888f15ed14e0baab1e20b517f22d8f0b9de04c16f426aba28`, R12)", "CL3-09"),
    ("4 n'ont aucun échec de longueur et 97 actions de même longueur suivent un premier\n  écart :",
     "4 n'ont aucun échec de longueur et 97 actions de même longueur suivent un premier\n  écart (comptés sur `MC-2.par_tache` et `MC-3.par_action` de la sortie citée, `1454d084…`) :",
     "CL3-09"),
    # CL3-12 : exception de « C1 étendu »
    ("- **Lignes décisives et descriptives** : les actions des seuls épisodes au niveau 1, dans les cinq bras ;",
     "- **Lignes décisives et descriptives** (sauf « C1 étendu », ci-dessous, et M5, sur la validation) : les actions des\n  seuls épisodes au niveau 1, dans les cinq bras ;",
     "CL3-12"),
    # CL3-06 : population des 38 épisodes, dans la section R-284 …
    ("  multipliée par environ √(60/38) ≈ 1,26 (Plan d'analyse, point 5).\n",
     "  multipliée par environ √(60/38) ≈ 1,26 (Plan d'analyse, point 5).\n"
     "- **Population** (contre-lecture 3, CL3-06) : un succès ou un échec de C1 vaut pour les 38 épisodes reproduits à\n"
     "  l'identique, qui ne sont pas un tirage au hasard des 60 : moins d'actions sans jeton de fin (10 sur 380, contre 33\n"
     "  sur 220) et des actions plus courtes (90e centile des jetons notés : 266, contre 400 ; médiane 205 contre 222,5 ;\n"
     "  `MC-3.par_action` de `docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json`, `1454d084…`, recompté par la\n"
     "  session) ; « C1 étendu » n'en donne qu'un aperçu descriptif.\n",
     "CL3-06"),
    # … et dans « Ce que H-P4 n'affirme pas »
    ("    l'autre, comme dans P3 ou T0.7 (relecture de Gemini, GP4-03).\n",
     "    l'autre, comme dans P3 ou T0.7 (relecture de Gemini, GP4-03) ;\n"
     "  - un succès ou un échec de C1 ne vaut que pour les 38 épisodes reproduits à l'identique, qui ne sont pas un tirage\n"
     "    au hasard des 60 (moins d'actions sans jeton de fin, actions plus courtes ; section R-284, « Population »).\n",
     "CL3-06"),
    # CL3-02 : C1 au pas 0 sur le niveau 1
    ("pas 0 (60 par bras au plus ; une seule occurrence", "pas 0 des épisodes du niveau 1 (38 par bras au plus ; une seule occurrence", "CL3-02"),
    # CL3-04 : épreuve (ii), le texte suit le code
    ("(ii) texte de\n  l'action\n  du pas 1 échangé avec celui du pas 2 : les deux actions échangées doivent échouer (c) ; les actions sans score ne sont\n  pas comparées, et une épreuve sans aucune action comparable se lit « contre l'attendu ».",
     "(ii) texte de\n  l'action du pas 1 échangé avec celui du pas 2 : les deux actions échangées doivent échouer (c) ; si l'une des deux\n  n'a pas de score, dans P3 ou dans P4, l'épreuve (ii) se lit « contre l'attendu ». En (i), les actions sans score ne\n  sont pas comparées, et un décalage sans aucune action comparable se lit « contre l'attendu ».",
     "CL3-04"),
    ("2. Épreuve (ii) : les deux actions échangées doivent échouer (c) ; une épreuve sans action comparable se lit « contre\n   l'attendu ».",
     "2. Épreuve (ii) : les deux actions échangées doivent échouer (c) ; si l'une des deux n'a pas de score, dans P3 ou dans\n   P4, l'épreuve (ii) se lit « contre l'attendu ». Épreuve (i) : un décalage sans aucune action comparable se lit\n   « contre l'attendu ».",
     "CL3-04"),
    # CL3-05 : portée de la réserve de l'épreuve
    ("tolérance (c) non éprouvée sur le modèle réel ; sonde d'enjeux",
     "tolérance (c) non éprouvée sur le modèle réel (elle ne porte que sur le descriptif « C1 étendu » ; ni C1 ni M6 n'en\ndépendent) ; sonde d'enjeux",
     "CL3-05"),
    # CL3-11 : précision 9
    ("quand M5 est déjà en défaut : L3 prime", "quand M5 donne la ligne L3 (non au-dessus, ou lecture de M5 en échec) : L3 prime", "CL3-11"),
    # CL3-10 : plan v2
    ("plan v2 (`plan-code-et-chaine-v2.md`, R12), écrit avant le candidat et aligné sur ce texte.",
     "plan v2 (`plan-code-et-chaine-v2.md`, R12), écrit avant R-284 et aligné sur le brouillon 4 ; il se tait sur R-284,\nque ce texte et le module portent.",
     "CL3-10"),
]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def une(t: str, a: str, b: str, source: str) -> str:
    n = t.count(a)
    if n != 1:
        raise SystemExit(f"{source} : « {a[:70]!r} » trouvé {n} fois (une attendue)")
    return t.replace(a, b)


def main(argv: list[str]) -> int:
    if len(argv) != 7:
        print(__doc__, file=sys.stderr)
        return 2
    cand1, sortie, module_dir, chaine_dir, tests, paires_json = argv[1:]
    if not tests.isdigit():
        raise SystemExit("TESTS_ATTENDUS : un entier attendu")
    t = Path(cand1).read_text(encoding="utf-8")
    for a, b, s in PAIRES_FIXES:
        t = une(t, a, b, s)
    # empreintes du module retenu
    for n in NOMS_MODULE:
        t = une(t, f"Module de P4 : `{DOSSIER}/{n}` : `{ANCIENNES[n]}`",
                f"Module de P4 : `{DOSSIER}/{n}` : `{sha(Path(module_dir) / n)}`", "module")
    # T2 : forme lue par la chaîne
    t = une(t, "- Tests attendus : 1 102, soit", f"- Tests attendus : `{tests}`, soit", "NOTES-CHAINE T2")
    # T3 : scripts de l'instance et ligne « Lancement »
    amorce, instance = Path(chaine_dir) / "amorce_instance_p4_v1.sh", Path(chaine_dir) / "p4_instance_v1.sh"
    t = une(t, "- Run source (P3) : ",
            f"- Scripts de l'instance, gelés par le scellement : `{DOSSIER}/amorce_instance_p4_v1.sh` (`{sha(amorce)}`, "
            f"sha256) ; `{DOSSIER}/p4_instance_v1.sh` (`{sha(instance)}`, sha256).\n"
            "- Lancement : `PREREG=prereg/P4-instrument-v1.md`, `BRANCHE=calcul/p4-reel-v1`.\n- Run source (P3) : ",
            "NOTES-CHAINE T3")
    for p in json.loads(Path(paires_json).read_text(encoding="utf-8")):
        t = une(t, p["ancien"], p["nouveau"], p.get("source", "paire du JSON"))
    Path(sortie).write_text(t, encoding="utf-8")
    e = sha(Path(sortie))
    Path(sortie + ".sha256").write_text(f"{e}  {Path(sortie).name}\n", encoding="utf-8")
    print(e)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
