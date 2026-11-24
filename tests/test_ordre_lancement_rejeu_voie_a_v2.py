"""L'ordre de lancement v2 (module de la passe rempli : passe_recalcul_v6, notice v7) passe la forme de l'amorce v2."""
import json
from pathlib import Path

from controle_ia import rejeu_activations_voie_a_v2 as R

RACINE = Path(__file__).resolve().parents[1]
D = RACINE / "docs/notes/rejeu-activations-saboteur-voie-a-v1/amorce-executante-v8"


def test_ordre_v2_complet_et_seule_difference_le_module():
    v2 = D / "ordre-lancement-rejeu-voie-a-v2.json"
    o = R.lire_ordre(v2, R.sha256_fichier(v2))
    assert o["go"] == "GO-2026-11-24-13" and "A_FIXER" not in v2.read_text()
    for k in ("verifier_entrees", "essai_a_blanc", "passe"):
        assert o[k]["argv"][1:3] == ["-m", "controle_ia.barreau8_moniteurs.passe_recalcul_v6"]
    v1 = json.loads((D / "ordre-lancement-rejeu-voie-a-v1.json").read_text())
    for k in ("verifier_entrees", "essai_a_blanc", "passe"):
        v1[k]["argv"][2] = "controle_ia.barreau8_moniteurs.passe_recalcul_v6"
    assert v1 == json.loads(v2.read_text())
