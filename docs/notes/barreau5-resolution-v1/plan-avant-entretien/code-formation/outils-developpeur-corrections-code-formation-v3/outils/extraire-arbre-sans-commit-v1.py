"""Extraction, hors du dépôt et sans aucun commit, de l'arbre que l'amorce de formation du barreau 5 extrait sur l'instance
(bloc « motifs » de `scripts/amorce_b5f_formation_v1.sh`), à partir de l'ARBRE DE TRAVAIL du dépôt (fichiers suivis par
git, dans leur état courant, corrections comprises). Outil du développeur des corrections, 19 novembre 2026.

Usage : python -I extraire-arbre-sans-commit-v1.py DEPOT DESTINATION [CHEMIN_DE_PLUS ...]
Les motifs de l'amorce (forme de `git sparse-checkout --no-cone`) sont traduits en motifs de chemins de git (`:(glob)`) ;
`git ls-files` donne les fichiers suivis qui y répondent ; chacun est copié tel qu'il est dans l'arbre de travail. Les
chemins de plus (essais du lanceur et des amorces, garde de calcul) servent à la copie de travail des mutations.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path


def motifs_de_l_amorce(depot: Path) -> list[str]:
    texte = (depot / "scripts" / "amorce_b5f_formation_v1.sh").read_text(encoding="utf-8")
    bloc = re.search(r"^# >>> motifs.*?$(.*?)^# <<< motifs$", texte, re.S | re.M).group(1)
    corps = re.search(r"MOTIFS='(.*?)'", bloc, re.S).group(1)
    return [x.strip() for x in corps.splitlines() if x.strip()]


def en_chemins_git(motif: str) -> str:
    if motif.startswith("!"):
        raise SystemExit(f"motif négatif inattendu : {motif}")
    m = motif.lstrip("/")
    return f":(glob){m}**" if m.endswith("/") else f":(glob){m}"


def main(argv) -> int:
    depot, dest, de_plus = Path(argv[0]).resolve(), Path(argv[1]), argv[2:]
    if dest.exists():
        raise SystemExit(f"{dest} existe déjà")
    motifs = motifs_de_l_amorce(depot)
    suivis = subprocess.run(["git", "-C", str(depot), "ls-files", "-z", "--", *map(en_chemins_git, motifs)],
                            check=True, capture_output=True).stdout.decode("utf-8").split("\0")
    chemins = sorted({x for x in suivis if x} | set(de_plus))
    for c in chemins:
        source = depot / c
        if not source.is_file():
            raise SystemExit(f"{c} absent de l'arbre de travail")
        (dest / c).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest / c)
    hauts = sorted({c.split("/")[0] for c in chemins})
    print(f"motifs : {len(motifs)} ; fichiers copiés : {len(chemins)} ; premier niveau : {' '.join(hauts)}")
    for d in ("docs/notes", "diag", "runs", "brouillons"):
        print(("PRÉSENT (ne devrait pas) : " if (dest / d).exists() else "absent : ") + d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
