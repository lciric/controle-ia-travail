"""Garde du code qui tournera (addendum n° 1, section 2 ; couple 19 de la contre-lecture). Bibliothèque standard seule.

1. **Liste fermée** : `git diff --name-status 55399606..<commit du code>` doit donner exactement les fichiers de la
   liste fermée (`liste-fermee-v1.txt`, un chemin par ligne), tous ajoutés ou modifiés ; un fichier hors liste, un
   fichier de la liste absent de la différence, une suppression, un renommage, une copie ou un changement de type :
   refus.
2. **Addendum scellé** : au commit lancé (descendant du commit du code), l'addendum scellé existe, son compagnon
   `.sha256` le vérifie, il cite le commit du code en entier, et la différence `<commit du code>..<commit lancé>` ne
   touche ni `src/`, ni `tests/`, ni `scripts/` (seuls le texte scellé, les notes et les registres s'y ajoutent).

    python -m controle_ia.sparks_exp7_nul_v2.garde_code liste DEPOT COMMIT_CODE
    python -m controle_ia.sparks_exp7_nul_v2.garde_code lancement DEPOT COMMIT_CODE [COMMIT_LANCE]
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

COMMIT_BASE = "55399606f268713bc1d52a9d18ef1e37c681028d"
LISTE = "src/controle_ia/sparks_exp7_nul_v2/liste-fermee-v1.txt"
CHEMIN_ADDENDUM = "prereg/SPARKS-EXP7-NUL-addendum-1.md"
CODE = ("src/", "tests/", "scripts/")


class GardeCode(RuntimeError):
    pass


def _git(depot: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(depot), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise GardeCode(f"git {' '.join(args)} : {r.stderr.strip()[:200]}")
    return r.stdout


def lire_liste(texte: str) -> list[str]:
    out = [l.strip() for l in texte.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    if len(set(out)) != len(out):
        raise GardeCode("liste fermée : chemin en double")
    return out


def difference(depot: Path, base: str, commit: str) -> list[tuple[str, str]]:
    out = []
    for l in _git(depot, "diff", "--no-renames", "--name-status", f"{base}..{commit}").splitlines():
        if not l.strip():
            continue
        st, *chemins = l.split("\t")
        out.append((st, chemins[-1]))
    return out


def verifier_liste_fermee(depot: Path, commit: str, base: str = COMMIT_BASE, liste: list[str] | None = None) -> dict:
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise GardeCode("commit du code : 40 chiffres hexadécimaux attendus")
    if subprocess.run(["git", "-C", str(depot), "merge-base", "--is-ancestor", base, commit]).returncode != 0:
        raise GardeCode(f"{commit[:12]} ne descend pas de {base[:12]}")
    if liste is None:
        liste = lire_liste(_git(depot, "show", f"{commit}:{LISTE}"))
    diff = difference(depot, base, commit)
    mauvais_statut = [(s, p) for s, p in diff if s not in ("A", "M")]
    if mauvais_statut:
        raise GardeCode(f"suppression, renommage ou changement de type refusé : {mauvais_statut[:4]}")
    changes, attendus = {p for _, p in diff}, set(liste)
    hors, absents = sorted(changes - attendus), sorted(attendus - changes)
    if hors or absents:
        raise GardeCode(f"différence ≠ liste fermée : hors liste {hors[:4]}, absents de la différence {absents[:4]}")
    return {"commit": commit, "n_fichiers": len(changes)}


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def verifier_lancement(depot: Path, commit_code: str, commit_lance: str = "HEAD",
                       chemin_addendum: str = CHEMIN_ADDENDUM) -> dict:
    lance = _git(depot, "rev-parse", f"{commit_lance}^{{commit}}").strip()
    if subprocess.run(["git", "-C", str(depot), "merge-base", "--is-ancestor", commit_code, lance]).returncode != 0:
        raise GardeCode(f"commit lancé {lance[:12]} ne descend pas du commit du code {commit_code[:12]}")
    touche = [p for _, p in difference(depot, commit_code, lance) if p.startswith(CODE)]
    if touche:
        raise GardeCode(f"code changé après le commit du code : {touche[:4]}")
    try:
        texte = _git(depot, "show", f"{lance}:{chemin_addendum}")
        sceau = _git(depot, "show", f"{lance}:{chemin_addendum}.sha256")
    except GardeCode:
        raise GardeCode(f"{chemin_addendum} ou son compagnon absent au commit lancé : addendum non scellé") from None
    m = re.match(r"([0-9a-f]{64})\s", sceau)
    if not m or m.group(1) != sha256_octets(texte.encode("utf-8")):
        raise GardeCode("addendum : empreinte ≠ compagnon")
    if commit_code not in texte:
        raise GardeCode("addendum scellé : le commit du code n'y est pas cité en entier")
    return {"commit_lance": lance, "commit_code": commit_code, "sha256_addendum": m.group(1)}


def main(argv: list[str]) -> int:
    try:
        if argv[0] == "liste":
            r = verifier_liste_fermee(Path(argv[1]), argv[2])
            print(f"LISTE FERMÉE CONFORME : {r['n_fichiers']} fichiers")
        elif argv[0] == "lancement":
            verifier_liste_fermee(Path(argv[1]), argv[2])
            r = verifier_lancement(Path(argv[1]), argv[2], argv[3] if len(argv) > 3 else "HEAD")
            print(f"LANCEMENT CONFORME : code {r['commit_code'][:12]}, addendum {r['sha256_addendum'][:12]}")
        else:
            raise IndexError
    except (GardeCode, IndexError) as err:
        print(f"CODE REFUSÉ : {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
