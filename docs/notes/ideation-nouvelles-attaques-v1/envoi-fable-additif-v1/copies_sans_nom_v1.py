"""Copies des pièces à servir à Fable, sans nom de personne, pour la garde de motifs de relecture_fable_api_v3.

Seule retouche : le nom du directeur est remplacé par « le directeur » (accords « de le » → « du », « à le » → « au »,
« De le » → « Du », « À le » → « Au »). Rien d'autre ne change. Puis la garde même de l'outil
(controle_ia.relecture_fable_api_v3.garde_motifs_ligne) est appliquée à chaque ligne de chaque copie ; toute ligne
qui garde un motif est un refus (code 3), la copie reste écrite pour examen, et rien ne part.

Usage : python -I copies_sans_nom_v1.py DOSSIER_SORTIE PIECE [PIECE …]   (PYTHONPATH=src pour l'import de l'outil)
Chaque copie s'écrit sous DOSSIER_SORTIE/<nom>-copie-sans-nom.md, refus si elle existe (R12), avec son compagnon
.sha256 ; un relevé `releve-copies.json` donne, par pièce, l'empreinte d'origine, l'empreinte de la copie et le
nombre de remplacements.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src"))
from controle_ia.relecture_fable_api_v3 import garde_motifs_ligne  # noqa: E402

NOM = re.compile(r"Lazar")
ACCORDS = [("de le directeur", "du directeur"), ("De le directeur", "Du directeur"),
           ("à le directeur", "au directeur"), ("À le directeur", "Au directeur")]


def empreinte(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    sortie = Path(sys.argv[1])
    sortie.mkdir(parents=True, exist_ok=True)
    releve, motifs_restants = [], 0
    for chemin in map(Path, sys.argv[2:]):
        brut = chemin.read_bytes()
        texte = brut.decode("utf-8")
        nouveau, n = NOM.subn("le directeur", texte)
        for a, b in ACCORDS:
            nouveau = nouveau.replace(a, b)
        cible = sortie / f"{chemin.stem}-copie-sans-nom.md"
        if cible.exists():
            print(f"REFUS : {cible} existe (R12)")
            return 4
        octets = nouveau.encode("utf-8")
        cible.write_bytes(octets)
        e = empreinte(octets)
        (sortie / f"{cible.name}.sha256").write_text(f"{e}  {cible.name}\n", encoding="utf-8")
        trouves = [(i, m) for i, l in enumerate(nouveau.split("\n"), 1) for m in garde_motifs_ligne(l)]
        motifs_restants += len(trouves)
        releve.append({"origine": str(chemin), "sha256_origine": empreinte(brut), "copie": cible.name,
                       "sha256_copie": e, "remplacements": n, "motifs_restants": [{"ligne": i, "motif": m} for i, m in trouves]})
        print(f"{chemin.name} : {n} remplacement(s) ; motifs restants : {len(trouves)}")
    (sortie / "releve-copies.json").write_text(json.dumps(releve, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 3 if motifs_restants else 0


if __name__ == "__main__":
    sys.exit(main())
