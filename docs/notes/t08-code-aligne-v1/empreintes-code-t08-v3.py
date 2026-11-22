"""v3 — Pièce des empreintes de tout le code de T0.8 à un commit, chaîne de lancement et programme de scellement compris
(demande de la session mère du 22 novembre, 22:18Z : la pièce de `d231cc8b` ne couvrait que `src/controle_ia/t08` et
`tests/test_t08_*`). Même forme que la v2 (octets lus par `git show`, lignes, sha256), motifs élargis (`MOTIFS`), et un mode
de rejeu.

Écrire : python3 docs/notes/t08-code-aligne-v1/empreintes-code-t08-v3.py ecrire COMMIT BRANCHE SORTIE   (refus si SORTIE existe : R12)
Rejouer : python3 docs/notes/t08-code-aligne-v1/empreintes-code-t08-v3.py verifier PIECE
  relit le commit cité par la pièce, recalcule la liste des fichiers des motifs et leurs empreintes par `git show`, et
  exige l'égalité ligne à ligne avec la table de la pièce (même liste, mêmes lignes, mêmes empreintes). Code 0 : égale ;
  1 : écart (imprimé) ; 2 : usage. Se joue depuis tout clone qui porte le commit (aucun fichier de l'arbre de travail lu).
"""
from __future__ import annotations

import fnmatch
import hashlib
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

MOTIFS = (
    "src/controle_ia/t08/*.py",                      # code aligné de la course et de la lecture
    "src/controle_ia/lancement_t08/*.py",            # chaîne : session, commit local
    "scripts/*t08*",                                 # chaîne : lanceur, amorce, branche d'entrée, configurations, liste, essais
    "tests/test_t08_*.py",
    "tests/aide_t08_*.py",
    "brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v4.py",   # programme de scellement et ce qu'il importe
    "brouillons/t08-texte-complet-fable-v1/controle_gel_t08_v1.py",
)
RACINES = ("src/controle_ia/t08", "src/controle_ia/lancement_t08", "scripts", "tests", "brouillons/t08-texte-complet-fable-v1")


def _git(*args: str, octets: bool = False):
    r = subprocess.run(["git", *args], check=True, capture_output=True)
    return r.stdout if octets else r.stdout.decode("utf-8")


def table(commit: str) -> tuple[str, list[str]]:
    plein = _git("rev-parse", "--verify", commit + "^{commit}").strip()
    noms = _git("ls-tree", "-r", "--name-only", plein, "--", *RACINES).splitlines()
    noms = sorted(n for n in noms if not n.endswith(".sha256") and any(fnmatch.fnmatch(n, m) for m in MOTIFS))
    lignes = []
    for n in noms:
        o = _git("show", f"{plein}:{n}", octets=True)
        lignes.append(f"| `{n}` | {o.count(bytes([10]))} | `{hashlib.sha256(o).hexdigest()}` |")
    return plein, lignes


def ecrire(commit: str, branche: str, sortie: Path) -> int:
    if sortie.exists():
        print(f"ARRÊT : {sortie} existe déjà (R12)", file=sys.stderr)
        return 1
    plein, lignes = table(commit)
    quand = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    motifs = ", ".join(f"`{m}`" for m in MOTIFS)
    sortie.write_text(
        f"# Empreintes du code de T0.8 au commit `{plein[:8]}`, chaîne de lancement comprise — v1\n\n"
        f"Écrite le {quand} (heure de la machine, UTC) par le développeur de la chaîne de lancement, par "
        f"`docs/notes/t08-code-aligne-v1/empreintes-code-t08-v3.py`, sur la branche `{branche}`.\n\n"
        f"- Commit : `{plein}`.\n"
        f"- Fichiers : {len(lignes)} ({motifs} ; compagnons `.sha256` exclus), octets lus par `git show`.\n"
        f"- Rejeu (code 0 exigé), depuis tout clone qui porte le commit : "
        f"`python3 docs/notes/t08-code-aligne-v1/empreintes-code-t08-v3.py verifier {sortie.as_posix()}`.\n\n"
        "| fichier | lignes | sha256 |\n|---|---|---|\n" + "\n".join(lignes) + "\n", encoding="utf-8")
    print(sortie)
    return 0


def verifier(piece: Path) -> int:
    texte = piece.read_text(encoding="utf-8")
    m = re.search(r"^- Commit : `([0-9a-f]{40})`\.$", texte, re.M)
    if not m:
        print("ARRÊT : la pièce ne cite pas de commit de 40 caractères", file=sys.stderr)
        return 1
    attendues = [l for l in texte.splitlines() if l.startswith("| `")]
    _, lignes = table(m.group(1))
    if lignes != attendues:
        manque = sorted(set(attendues) - set(lignes))
        plus = sorted(set(lignes) - set(attendues))
        print(f"ÉCART au commit {m.group(1)} : {len(manque)} ligne(s) de la pièce absentes, {len(plus)} en plus ; "
              f"{(manque + plus)[:3]}", file=sys.stderr)
        return 1
    print(f"conforme : {len(lignes)} fichiers au commit {m.group(1)}, égaux à la pièce")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) == 4 and a[0] == "ecrire":
        sys.exit(ecrire(a[1], a[2], Path(a[3])))
    if len(a) == 2 and a[0] == "verifier":
        sys.exit(verifier(Path(a[1])))
    print(__doc__, file=sys.stderr)
    sys.exit(2)
