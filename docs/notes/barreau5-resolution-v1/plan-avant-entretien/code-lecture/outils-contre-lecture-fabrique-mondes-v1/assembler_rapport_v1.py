"""Assemble la contre-lecture : le corps écrit à la main, puis l'annexe des couples, rendue mot pour mot depuis
`couples_corrections_v1.py` (les mêmes données que `verifier_couples_v1.py` a comptées et appliquées).

Outil du contre-lecteur (Claude Fable 5.2), 20 novembre 2026. Usage : `python -B <ce fichier> --corps <corps.md> --sortie
<contre-lecture.md>` ; la sortie est un fichier neuf (R12).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--corps", required=True)
    ap.add_argument("--sortie", required=True)
    a = ap.parse_args(argv)
    spec = importlib.util.spec_from_file_location("couples_corrections_v1", ICI / "couples_corrections_v1.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    corps = Path(a.corps).read_text(encoding="utf-8")
    if "```" in "".join(c["avant"] + c["apres"] for c in module.COUPLES):
        raise SystemExit("un couple porte une clôture de bloc : rendu impossible")
    lignes = [corps.rstrip("\n"), "", "## Annexe — les couples, mot pour mot", "",
              f"Rendus depuis `outils-contre-lecture-fabrique-mondes-v1/couples_corrections_v1.py` (sha256 "
              f"`{hashlib.sha256((ICI / 'couples_corrections_v1.py').read_bytes()).hexdigest()}`), dans l'ordre "
              "d'application. Chaque « avant » est le texte entre les deux clôtures, sauts de ligne compris, sans la "
              "ligne vide finale ; il se trouve une seule fois dans son fichier.", ""]
    for c in module.COUPLES:
        lignes += [f"### {c['id']} — `{c['fichier']}`", "", c["constat"] + ".", "", "Avant :", "", "```python",
                   c["avant"].rstrip("\n"), "```", "", "Après :", "", "```python", c["apres"].rstrip("\n"), "```", ""]
    octets = ("\n".join(lignes).rstrip("\n") + "\n").encode("utf-8")
    with open(a.sortie, "xb") as fh:
        fh.write(octets)
    print(hashlib.sha256(octets).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
