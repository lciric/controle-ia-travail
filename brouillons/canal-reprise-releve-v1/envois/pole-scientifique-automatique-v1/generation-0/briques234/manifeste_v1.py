"""Manifeste du run : versions, graines, empreintes des fournis (lecture seule) et des sorties.

Usage : python3 -I -B manifeste_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --commande "<commande de lancement>"
"""
import argparse
import hashlib
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import commun_v1 as cm


def empreintes(racine: Path, motifs) -> dict:
    out = {}
    for motif in motifs:
        for p in sorted(racine.rglob(motif)):
            if p.is_file():
                out[str(p.relative_to(racine))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    ap.add_argument("--commande", required=True)
    args = ap.parse_args()
    fournis = empreintes(cm.FOURNIS, ["*"])
    compiles = sorted(str(p) for p in cm.RACINE.rglob("*.pyc")) + sorted(str(p) for p in cm.RACINE.rglob("__pycache__"))
    attendues_ok = all(fournis.get(k) == v for k, v in cm.EMPREINTES_ATTENDUES.items())
    contenu = {
        "manifeste": "essais des briques 2, 3 et 4 de la méta-conception (organisme v6.2.1), version 1",
        "heure_ecriture_utc": args.heure,
        "commande": args.commande,
        "commit": "aucun : git interdit dans ce bac à sable",
        "versions": cm.versions(),
        "graines": cm.description_graines(),
        "interpreteur": "python3 -I -B (isolé, sans fichier compilé)",
        "fournis_lecture_seule": {"fichiers": len(fournis), "empreintes": fournis,
                                  "empreintes_attendues_verifiees": attendues_ok,
                                  "fichiers_compiles_trouves": compiles},
        "sorties": empreintes(cm.SORTIE, ["*.py", "resultats-*.json", "*.sh"]),
    }
    cm.ecrire_json(cm.SORTIE / "manifeste-essais-v1.json", contenu)
    print("fournis intacts :", attendues_ok, "| compilés :", compiles)


if __name__ == "__main__":
    main()
