#!/usr/bin/env python3
"""Assemble la consigne figée du proposeur de la course d'auto-conception (version 1), par programme, sans reformulation :
question (`question-auto-conception-v1.md`) + état actuel de l'organisme (`etat-actuel-organisme-auto-conception-v1.md`) +
texte entier de la décision N-073, lu à l'octet dans le dépôt de travail au commit donné (`git show COMMIT:CHEMIN`) et refusé
s'il n'a pas l'empreinte attendue. Écrit `consigne-proposeur-auto-conception-v1.md` (refus s'il existe déjà, R12).

Usage (cwd quelconque) : python3 -I -B construire_consigne_proposeur_v1.py COMMIT_MAIN
"""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[3]
N073 = ("docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md",
        "b95688df5e695da7dc32ce71321ba205f44debcc0b7410e598c78c2180733ecd")
SORTIE = ICI / "consigne-proposeur-auto-conception-v1.md"


def assembler(question: str, etat: str, n073: bytes) -> str:
    return (question.rstrip() + "\n\n" + etat.rstrip() + "\n\n"
            f"## Décision N-073 (texte entier, `{N073[0]}`, sha256 `{N073[1]}`)\n\n"
            "Le texte ci-dessous est servi tel quel. Ses titres internes commencent par un dièse de plus.\n\n"
            + "\n".join(("#" + l) if l.startswith("#") else l for l in n073.decode("utf-8").rstrip().split("\n")) + "\n")


def principal(argv: list) -> int:
    if len(argv) != 1:
        print("usage : construire_consigne_proposeur_v1.py COMMIT_MAIN", file=sys.stderr)
        return 2
    brut = subprocess.run(["git", "-C", str(DEPOT), "show", f"{argv[0]}:{N073[0]}"], capture_output=True, check=True).stdout
    if hashlib.sha256(brut).hexdigest() != N073[1]:
        print("N-073 : empreinte différente de celle attendue", file=sys.stderr)
        return 2
    texte = assembler((ICI / "question-auto-conception-v1.md").read_text(encoding="utf-8"),
                      (ICI / "etat-actuel-organisme-auto-conception-v1.md").read_text(encoding="utf-8"), brut)
    with open(SORTIE, "x", encoding="utf-8") as f:
        f.write(texte)
    print(hashlib.sha256(texte.encode("utf-8")).hexdigest(), SORTIE.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(principal(sys.argv[1:]))
