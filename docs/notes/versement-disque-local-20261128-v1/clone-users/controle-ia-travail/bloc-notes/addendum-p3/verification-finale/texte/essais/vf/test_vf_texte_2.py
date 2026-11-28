"""Essai complémentaire (VF1-11) : précision 1, « un arrêt survenu après la création du manifeste est écrit dans la
sortie unique ». `reference` (dont `verifier(chemin_l)`) est construit entre `creer_manifeste` et le `try` de `executer` :
une garde levée là laisse un manifeste sans sortie. Remplaçants pour tout ce qui précède (aucune donnée)."""
import sys
from pathlib import Path

import pytest

BASE = Path(__file__).resolve().parent.parent / "base"
sys.path.insert(0, str(BASE))

import complements_p3_v1 as cp  # noqa: E402

from controle_ia.gardes import GardeArret  # noqa: E402


def test_precision_1_arret_entre_le_manifeste_et_le_try_non_ecrit(monkeypatch, tmp_path):
    ordre = []
    for nom in ("exiger_commande", "exiger_anteriorite", "charger_textes", "exiger_coherence", "familles_attention",
                "localisation"):
        monkeypatch.setattr(cp, nom, lambda *a, **k: None)
    monkeypatch.setattr(cp, "exiger_garde_1", lambda *a, **k: {"sha_prereg": "0", "sha_module": "0", "sha_tests": "0",
                                                               "commit_cite": "0"})
    monkeypatch.setattr(cp, "exiger_lecture_decisive", lambda *a, **k: {"commit_lecture": "0", "manifestes_ecartes": []})
    monkeypatch.setattr(cp.lp, "charger_source", lambda *a, **k: {
        "sondes-figees": {"principales": {"tromperie": "p0", "enjeux": "p1"}}})
    monkeypatch.setattr(cp, "verifier_resultat", lambda *a, **k: {"resultat": {"issue": {"ligne": "x"}}})
    monkeypatch.setattr(cp, "controler_entrees", lambda *a, **k: ({"principales": ["p0", "p1"]}, {}))
    monkeypatch.setattr(cp, "exiger_premier_passage", lambda *a, **k: [])
    monkeypatch.setattr(cp, "creer_manifeste", lambda *a, **k: ordre.append("creer_manifeste") or (
        tmp_path / "manifeste.json", {"graines": {}}))

    def verifier_en_echec(*a, **k):
        ordre.append("verifier(chemin_l)")
        raise GardeArret("sceau de lecture-p3.json illisible (simulé)")

    monkeypatch.setattr(cp, "verifier", verifier_en_echec)
    monkeypatch.setattr(cp, "ecrire_resultat", lambda *a, **k: ordre.append("sortie écrite"))
    with pytest.raises(GardeArret, match="simulé"):
        cp.executer(tmp_path, "run", "lec", "20261020-120000-addendum-p3", cp.PREREG_ADDENDUM, cp.ENTROPIE_P3)
    print("ordre :", ordre)
    assert ordre == ["creer_manifeste", "verifier(chemin_l)"]          # manifeste créé, aucune sortie écrite
