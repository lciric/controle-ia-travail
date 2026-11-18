"""Reconstruit l'orchestrateur de l'organisme d'idéation livré par le compte de l'organisme (remplacement déclaré du modèle
d'un juge externe, version 2) : clone local du clone public en lecture, puis le paquet git de la livraison, tête et arbre
épinglés. Aucun passage par le shell.

Usage : python3 -I -B scripts/assembler_orchestrateur_compte_organisme_v1.py DESTINATION_NEUVE
Codes : 0 assemblé ; 2 refus (paquet à l'empreinte fausse, destination existante, tête ou arbre différents, fichier épinglé faux).
"""
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[1]
SOURCE = Path("/home/user/lciric/ideation-organism")
PAQUET = DEPOT / "docs/notes/organisme-remplacement-juge-v2/orchestrateur-remplacement-juge-v2.bundle"
PAQUET_SHA256 = "1c5a5bd2e97c26c515927f8c1d4519e1b1c94367ee03abb4186eb7aa697d5262"
REFERENCE = "refs/heads/prep-remplacement-juge-v2"
BASE = "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb"
TETE = "8a2a6ac9d3feb52e6771edca52f440dd780fb373"
ARBRE = "71417ad17d816af07a6a57e9dc28bbfac07faac5"
FICHIERS = {
    "pole/bras_remplacement_juge_v2.py": "83a08aeeeba694f72e0aceb004c9432c4c57427072ed37208181903f30433ee2",
    "pole/bras_remplacement_juge_v1.py": "2efd6b0874e8bbfa58a0c53a5099f46da51318c6807c90909b8cf58dfe90866a",
    "pole/ideation_v2.py": "67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc",
    "demonstrations/ideation_v2.py": "bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845",
    "demonstrations/ideation_v2_juges_externes_uniques_v1.py": "1fbe2be3cab8e843daaecd8547beee05e2948f0e11bdbb9dc1ffacdce4ee7682",
}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def git(*args, cwd=None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def main(argv) -> int:
    if len(argv) != 1:
        print("REFUS : une destination neuve, et rien d'autre"); return 2
    dest = Path(argv[0]).resolve()
    if dest.exists():
        print(f"REFUS : {dest} existe déjà"); return 2
    if not PAQUET.is_file() or sha(PAQUET) != PAQUET_SHA256:
        print("REFUS : paquet de la livraison absent ou à l'empreinte fausse"); return 2
    if git("-C", str(SOURCE), "rev-parse", "HEAD").stdout.strip() != BASE:
        print(f"REFUS : le clone public n'est pas à la base {BASE}"); return 2
    etapes = (git("clone", "-q", "--no-hardlinks", str(SOURCE), str(dest)),
              git("fetch", "-q", str(PAQUET), REFERENCE, cwd=dest), git("checkout", "-q", "--detach", "FETCH_HEAD", cwd=dest))
    tete = git("rev-parse", "HEAD", cwd=dest).stdout.strip() if dest.is_dir() else ""
    arbre = git("rev-parse", "HEAD:orchestrator", cwd=dest).stdout.strip() if dest.is_dir() else ""
    sale = git("status", "--porcelain", "--untracked-files=all", cwd=dest).stdout.strip() if dest.is_dir() else "?"
    faux = [rel for rel, h in FICHIERS.items() if not (dest / "orchestrator" / rel).is_file() or sha(dest / "orchestrator" / rel) != h]
    if any(e.returncode for e in etapes) or tete != TETE or arbre != ARBRE or sale or faux:
        shutil.rmtree(dest, ignore_errors=True)
        print(f"REFUS : tête {tete!r} (attendue {TETE}), arbre {arbre!r} (attendu {ARBRE}), fichiers faux {faux}, état {sale[:80]!r}")
        return 2
    for rel, h in sorted(FICHIERS.items()):
        print(f"{h}  {rel}")
    print(f"assemblé : {dest / 'orchestrator'} (base {BASE[:8]}, tête {TETE[:8]}, arbre {ARBRE})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
