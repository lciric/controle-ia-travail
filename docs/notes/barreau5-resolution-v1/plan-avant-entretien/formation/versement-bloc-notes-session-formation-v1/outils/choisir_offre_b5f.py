"""Choix mécanique de l'offre d'une instance de formation du barreau 5 (plan de marche v1, point 1.3).
Usage : python -I choisir_offre_b5f.py RACINE_COURSE OFFRES.json SORTIE_OFFRE.json
Chaque offre passe `exiger_offre` du code figé ; la moins chère qui passe est écrite seule (égalité : plus petit id).
Imprime seulement le nombre d'offres reçues et acceptées, l'id et le prix de l'offre retenue."""
import json
import sys
from pathlib import Path

racine, offres, sortie = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
sys.path.insert(0, str(racine / "src"))
from controle_ia.barreau5_familles.formation_v1 import exiger_offre  # noqa: E402

brut = json.loads(offres.read_text(encoding="utf-8"))
brut = brut.get("offers", brut) if isinstance(brut, dict) else brut
acceptees = []
for x in brut:
    try:
        exiger_offre(x)
        acceptees.append(x)
    except Exception:
        pass
acceptees.sort(key=lambda x: (float(x["dph_total"]), int(x["id"])))
print(f"offres reçues {len(brut)} ; acceptées {len(acceptees)}")
if not acceptees:
    sys.exit(1)
if sortie.exists():
    sys.exit(f"{sortie} existe déjà (R12)")
sortie.write_text(json.dumps(acceptees[0], ensure_ascii=False, sort_keys=True), encoding="utf-8")
print(f"retenue : id {acceptees[0]['id']} ; {acceptees[0]['dph_total']} USD/h")
