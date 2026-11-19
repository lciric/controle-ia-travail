#!/usr/bin/env python3
"""Assemble la consigne figée du proposeur de la course d'auto-conception, **version 2**, par programme : même assemblage
que la v1 (question v1 + état actuel v1 + texte entier de N-073, lus à leurs empreintes), puis **expurgation** de tout le
texte servi (constat 9 de la contre-lecture de la v1) par la règle `expurger` du lanceur v2 : nom du directeur et
identifiants de session internes remplacés. Écrit `consigne-proposeur-auto-conception-v2.md` et la liste des expurgations
`expurgations-consigne-proposeur-v2.json` (refus si l'un existe déjà, R12).

Usage (cwd quelconque) : python3 -I -B construire_consigne_proposeur_v2.py COMMIT_MAIN
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[3]
V1 = ICI.parent / "course-v1"
N073 = ("docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md",
        "b95688df5e695da7dc32ce71321ba205f44debcc0b7410e598c78c2180733ecd")
SOURCES = {"question": (V1 / "question-auto-conception-v1.md", "f30bea04e50458a85d6ad17906e54774df00c21f7dbc495e3d5d184cda4ca9d0"),
           "etat": (V1 / "etat-actuel-organisme-auto-conception-v1.md", "395a9ed9ac34377b0f5a495c7c13273d5d872568ea8c69583017bac8e057bdea"),
           "assembleur_v1": (V1 / "construire_consigne_proposeur_v1.py", "a2f25b15f0a95a2a9f6215e4881fd48873bfe82743c94bc105bc55a9c2e965af")}
SORTIE = ICI / "consigne-proposeur-auto-conception-v2.md"
LISTE = ICI / "expurgations-consigne-proposeur-v2.json"


def charger(nom: str, chemin: Path):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


def principal(argv: list) -> int:
    if len(argv) != 1:
        print("usage : construire_consigne_proposeur_v2.py COMMIT_MAIN", file=sys.stderr)
        return 2
    for nom, (p, h) in SOURCES.items():
        if hashlib.sha256(p.read_bytes()).hexdigest() != h:
            print(f"{nom} : empreinte différente de celle attendue", file=sys.stderr)
            return 2
    brut = subprocess.run(["git", "-C", str(DEPOT), "show", f"{argv[0]}:{N073[0]}"], capture_output=True, check=True).stdout
    if hashlib.sha256(brut).hexdigest() != N073[1]:
        print("N-073 : empreinte différente de celle attendue", file=sys.stderr)
        return 2
    v1 = charger("assembleur_consigne_v1", SOURCES["assembleur_v1"][0])
    L = charger("lanceur_auto_conception_v2", DEPOT / "scripts" / "lancer_course_auto_conception_v2.py")
    assemble = v1.assembler(SOURCES["question"][0].read_text(encoding="utf-8"), SOURCES["etat"][0].read_text(encoding="utf-8"), brut)
    texte, liste = L.expurger(assemble)
    with open(SORTIE, "x", encoding="utf-8") as f:
        f.write(texte)
    objet = {"version": "expurgations-consigne-proposeur-v2", "regle": "lanceur v2, `expurger` (constat 9)",
             "source_avant_expurgation_sha256": hashlib.sha256(assemble.encode("utf-8")).hexdigest(),
             "consigne_v2_sha256": hashlib.sha256(texte.encode("utf-8")).hexdigest(), "expurgations": liste}
    with open(LISTE, "x", encoding="utf-8") as f:
        f.write(json.dumps(objet, ensure_ascii=False, indent=1) + "\n")
    print(objet["consigne_v2_sha256"], SORTIE.name, len(liste), "expurgation(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(principal(sys.argv[1:]))
