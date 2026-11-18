"""Assemble l'orchestrateur de l'organisme d'idéation augmenté du bras à remplacement déclaré du modèle d'un juge.

Copie l'arbre `orchestrator/` du clone public en lecture (arbre git épinglé), y ajoute les fichiers neufs tenus dans le
dépôt de travail (ajouts seuls : aucun fichier d'origine n'est modifié ni remplacé), et rend les empreintes.

Usage : python3 -I -B scripts/assembler_orchestrateur_remplacement_juge_v1.py DESTINATION_NEUVE
Codes : 0 assemblé ; 2 refus (arbre différent, destination existante, ajout qui écraserait un fichier d'origine).
"""
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[1]
SOURCE = Path("/home/user/lciric/ideation-organism")
ARBRE = "ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70"
AJOUTS = DEPOT / "docs/notes/relance-organismes-discrets-v1/orchestrateur-remplacement-juge-v1"
FICHIERS = ("pole/bras_remplacement_v1.py", "demonstrations/ideation_v9.py", "essais/test_bras_remplacement_v1.py")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(argv) -> int:
    if len(argv) != 1:
        print("REFUS : une destination neuve, et rien d'autre"); return 2
    dest = Path(argv[0]).resolve()
    if dest.exists():
        print(f"REFUS : {dest} existe déjà"); return 2
    arbre = subprocess.run(["git", "-C", str(SOURCE), "rev-parse", "HEAD:orchestrator"], capture_output=True, text=True)
    sale = subprocess.run(["git", "-C", str(SOURCE), "status", "--porcelain", "--", "orchestrator"], capture_output=True, text=True)
    if arbre.returncode or arbre.stdout.strip() != ARBRE or sale.stdout.strip():
        print(f"REFUS : arbre de l'orchestrateur {arbre.stdout.strip()!r} (attendu {ARBRE}) ou clone modifié"); return 2
    cible = dest / "orchestrator"
    dest.mkdir(parents=True)
    subprocess.run(f"git -C {SOURCE} archive HEAD orchestrator | tar -x -C {dest}", shell=True, check=True)
    for rel in FICHIERS:
        if (cible / rel).exists():
            shutil.rmtree(dest); print(f"REFUS : {rel} existe dans l'arbre d'origine (ajouts seuls)"); return 2
        compagnon = Path(str(AJOUTS / rel) + ".sha256")
        if not compagnon.exists() or compagnon.read_text(encoding="utf-8").split()[0] != sha(AJOUTS / rel):
            shutil.rmtree(dest); print(f"REFUS : sceau absent ou faux pour {rel}"); return 2
        shutil.copyfile(AJOUTS / rel, cible / rel)
        print(f"{sha(cible / rel)}  {rel}")
    print(f"assemblé : {cible} (arbre d'origine {ARBRE}, {len(FICHIERS)} ajouts)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
