"""Essais de `scripts/epreuve_niveau_deux_plis_bbis_v1.py` (B bis, « Seuil », épreuve de niveau de la règle (a) en deux plis) :
petit jeu synthétique seulement (l'épreuve complète se joue après la contre-lecture du code) ; résultat indépendant du nombre
de processus ; règle 99 % / 99,5 % appliquée mécaniquement (cas sain, artefact) ; épreuve réduite marquée « non complète »."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]


def _script():
    spec = importlib.util.spec_from_file_location("epreuve_bbis", RACINE / "scripts" / "epreuve_niveau_deux_plis_bbis_v1.py")
    m = importlib.util.module_from_spec(spec)
    sys.modules["epreuve_bbis"] = m                      # requis pour transmettre les tâches aux processus
    spec.loader.exec_module(m)
    return m


def test_petit_jeu_deterministe_et_independant_des_processus(tmp_path):
    m = _script()
    a = m.jouer(2 ** 100 + 99, 6, 20, 100, 16, processus=1)
    b = m.jouer(2 ** 100 + 99, 6, 20, 100, 16, processus=2)
    assert a["cellules"] == b["cellules"] and not a["complete"] and "avertissement" in a
    assert set(a["cellules"]) == {"nul", "signal-commun"} and all(c["jeux"] == 6 for c in a["cellules"].values())
    assert a["cellules"]["signal-commun"]["aire_mediane"] > a["cellules"]["nul"]["aire_mediane"]
    assert a["niveau_decisif_retenu"] in (0.99, 0.995) and a["cout"]["secondes_murales"] > 0
    sortie = tmp_path / "e.json"
    assert m.main(["--entropie", str(2 ** 100 + 5), "--sortie", str(sortie), "--jeux", "2", "--directions", "5",
                   "--tirages", "30", "--taches", "8"]) == 0
    assert json.loads(sortie.read_text(encoding="utf-8"))["parametres"]["directions"] == 5
    with pytest.raises(SystemExit, match="existe déjà"):
        m.main(["--entropie", str(2 ** 100 + 5), "--sortie", str(sortie)])


def test_regle_du_niveau_sain_et_artefact():
    m = _script()
    assert m.niveau_retenu({"nul": 0.004, "signal-commun": 0.01}) == (0.99, [])
    assert m.niveau_retenu({"nul": 0.004, "signal-commun": 0.011}) == (0.995, ["signal-commun"])


def test_entropie_courte_refusee_en_marche_reelle():
    m = _script()
    from controle_ia.gardes import GardeArret
    with pytest.raises(GardeArret, match="64 bits"):
        m.jouer(12345, 2, 5, 10, 8)
