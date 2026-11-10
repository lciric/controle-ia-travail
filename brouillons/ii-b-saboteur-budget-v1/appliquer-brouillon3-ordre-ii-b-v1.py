"""Brouillon 3 de l'ordre exploratoire de (ii-b) : couples du développeur du code appliqués dans l'ordre au brouillon 2
(intact, R12). Chaque couple porte `ancien`, `nouveau` et `occurrences` (nombre exact d'occurrences de `ancien` au moment de
son application ; 1 pour un couple de texte, le compte réel pour un marqueur rempli partout). Un compte différent arrête
le script sans rien écrire. Usage : python appliquer-brouillon3-ordre-ii-b-v1.py COUPLES.json"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
SOURCE = ICI / "ordre-exploratoire-ii-b-v1-brouillon2.md"
CIBLE = ICI / "ordre-exploratoire-ii-b-v1-brouillon3.md"
SHA_SOURCE = "4c083d75"


def main(argv):
    couples = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    brut = SOURCE.read_bytes()
    sha = hashlib.sha256(brut).hexdigest()
    if not sha.startswith(SHA_SOURCE):
        sys.exit(f"brouillon 2 : empreinte {sha[:12]} ≠ {SHA_SOURCE}…")
    if CIBLE.exists():
        sys.exit(f"{CIBLE.name} existe déjà (R12)")
    texte = brut.decode("utf-8")
    for k, c in enumerate(couples["couples"], 1):
        n = texte.count(c["ancien"])
        if n != c["occurrences"]:
            sys.exit(f"couple {k} ({c['id']}) : {n} occurrences, {c['occurrences']} attendues : rien n'est écrit")
        texte = texte.replace(c["ancien"], c["nouveau"])
    CIBLE.write_text(texte, encoding="utf-8")
    restants = sorted(set(re.findall(r"<<[A-Z0-9_]*>>", texte)))
    print(f"{CIBLE.name} {hashlib.sha256(texte.encode()).hexdigest()} ; couples {len(couples['couples'])} ; "
          f"marqueurs restants {len(restants)} : {' '.join(restants)}")


if __name__ == "__main__":
    main(sys.argv[1:])
