"""Écrit la pièce des empreintes du code de T0.8 à un commit (R6 ; R12 : refuse d'écraser).

Usage : python3 -I empreintes-code-t08-v1.py ARBRE COMMIT HEURE_UTC SORTIE_MD
- ARBRE : arbre git de la branche `prep/t08-code-compte4-v1` ; COMMIT : identifiant complet (40 caractères), qui doit être
  la tête de `origin/prep/t08-code-compte4-v1` connue de l'arbre (le code cité est le code poussé) ;
- fichiers : `src/controle_ia/t08/*.py` et `tests/test_t08_*.py` au commit, lus par `git show COMMIT:chemin` (aucun
  `checkout`) ; empreinte sha256 des octets du commit ; arrêt si aucun fichier, si un chemin sort de ces deux motifs, ou si
  l'arbre de travail diffère du commit sur ces chemins (le code cité est celui qui a été essayé).
"""
import hashlib, re, subprocess, sys
from fnmatch import fnmatch
from pathlib import Path

MOTIFS = ("src/controle_ia/t08/*.py", "tests/test_t08_*.py")

def git(arbre, *a, octets=False):
    r = subprocess.run(["git", "-C", arbre, *a], capture_output=True, check=True)
    return r.stdout if octets else r.stdout.decode()

def principal():
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    arbre, commit, heure, sortie = sys.argv[1], sys.argv[2], sys.argv[3], Path(sys.argv[4])
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        sys.exit("ARRÊT : commit complet attendu (40 caractères)")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", heure):
        sys.exit("ARRÊT : heure UTC relevée par `date -u` attendue")
    if sortie.exists():
        sys.exit(f"ARRÊT : {sortie} existe déjà (R12)")
    distant = git(arbre, "rev-parse", "refs/remotes/origin/prep/t08-code-compte4-v1").strip()
    if distant != commit:
        sys.exit(f"ARRÊT : le commit {commit[:12]} n'est pas la tête poussée connue ({distant[:12]})")
    noms = [n for n in git(arbre, "ls-tree", "-r", "--name-only", commit).splitlines() if any(fnmatch(n, m) for m in MOTIFS)]
    if not noms:
        sys.exit("ARRÊT : aucun fichier du code de T0.8 au commit")
    sale = git(arbre, "status", "--porcelain", "--", "src/controle_ia/t08", "tests").strip()
    if sale:
        sys.exit("ARRÊT : arbre de travail différent du commit sur les chemins du code :\n" + sale)
    lignes = []
    for n in sorted(noms):
        b = git(arbre, "show", f"{commit}:{n}", octets=True)
        nl = b.count(b"\n")
        lignes.append(f"| `{n}` | {nl} | `{hashlib.sha256(b).hexdigest()}` |")
    texte = (f"# Empreintes du code de T0.8 au commit `{commit[:8]}` — v1\n\n"
             f"Écrite le {heure} (heure relevée par `date -u`) par la session du compte 4 (modèle A), par "
             f"`brouillons/t08-code-compte4-v1/empreintes-code-t08-v1.py`, sur l'arbre de la branche `prep/t08-code-compte4-v1`.\n\n"
             f"- Commit : `{commit}` (tête poussée de `prep/t08-code-compte4-v1`).\n"
             f"- Fichiers : {len(noms)} (`src/controle_ia/t08/*.py`, `tests/test_t08_*.py`), octets lus par `git show`.\n\n"
             "| fichier | lignes | sha256 |\n|---|---|---|\n" + "\n".join(lignes) + "\n")
    sortie.write_text(texte, encoding="utf-8")
    print(f"{len(noms)} fichiers ; {sortie} ; sha256 {hashlib.sha256(sortie.read_bytes()).hexdigest()}")

principal()
