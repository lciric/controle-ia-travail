"""Gardes de `mesurer_echelle_v5.py` (R5, CLX-10, CLX-13 ; CLY-13 et CLZ-11 : aucun paramètre hors des cartes) :
profondeurs, révision par dossier d'instantané,
`_commit_hash`, dernier jeton constant (contrôlé avant toute passe), étendue de float16 ; et une mesure complète sur
le modèle minuscule local (cas sain), si son dossier est donné par la variable MODELE_MINUSCULE.
Lancement : python -m pytest -q echelle-v5/tests
"""
import importlib.util
import json
import os
import pathlib
import subprocess
import sys

import numpy as np
import pytest

SCRIPTS = pathlib.Path(__file__).resolve().parent.parent / "scripts"
spec = importlib.util.spec_from_file_location("mes", SCRIPTS / "mesurer_echelle_v5.py")
MES = importlib.util.module_from_spec(spec)
spec.loader.exec_module(MES)


def test_couches_relatives():
    assert MES.couches_relatives(32) == [8, 12, 16, 20]
    assert MES.couches_relatives(80) == [20, 30, 40, 50]
    assert MES.couches_relatives(2) == [1]


def test_revision_saine_et_artefacts(tmp_path):
    bon = tmp_path / "snapshots" / "abc123" / "config.json"
    bon.parent.mkdir(parents=True)
    bon.write_text("{}")
    assert MES.resoudre_source("m", "abc123", lambda *a, **k: str(bon)) == str(bon.parent)
    with pytest.raises(SystemExit):
        MES.resoudre_source("m", "autre", lambda *a, **k: str(bon))       # résolue ailleurs
    with pytest.raises(SystemExit):
        MES.resoudre_source("m", "abc123", lambda *a, **k: None)          # absente du cache
    with pytest.raises(SystemExit):
        MES.resoudre_source("m", None, lambda *a, **k: str(bon))          # sans révision


def test_commit_hash():
    MES.verifier_hachage(None, "abc")
    MES.verifier_hachage("abc", "abc")
    with pytest.raises(SystemExit):
        MES.verifier_hachage("def", "abc")


def test_dernier_jeton():
    assert MES.controle_dernier_jeton([[1, 2, 9], [5, 9], [9]]) == 9
    with pytest.raises(SystemExit):
        MES.controle_dernier_jeton([[1, 2, 9], [5, 8]])


def test_repartition():
    MES.verifier_repartition({"cuda"}, None)                       # un seul appareil : pas de carte des couches
    MES.verifier_repartition({"cuda"}, {"model.layers.0": 0, "model.layers.79": 1, "lm_head": 1})
    for types in ({"cuda", "cpu"}, {"cuda", "meta"}, {"cpu"}, set()):  # délestage (cpu, meta) ou rien de chargé
        with pytest.raises(SystemExit):
            MES.verifier_repartition(types, None)
    with pytest.raises(SystemExit):
        MES.verifier_repartition({"cuda"}, {"model.layers.0": 0, "model.layers.79": "cpu"})
    with pytest.raises(SystemExit):
        MES.verifier_repartition({"cuda"}, {"model.layers.0": 0, "model.layers.79": "disk"})


def test_repartition_delestage_reel(tmp_path):
    """Sur le modèle minuscule local, un délestage forcé sur le disque laisse des paramètres sur « meta » : la garde
    l'arrête (transformers 5.18 ; CLZ-11)."""
    if not os.environ.get("MODELE_MINUSCULE"):
        pytest.skip("modèle minuscule local non fourni")
    import torch
    from transformers import AutoModelForCausalLM
    carte = {"model.embed_tokens": "cpu", "model.layers": "disk", "model.norm": "cpu", "model.rotary_emb": "cpu",
             "lm_head": "cpu"}
    m = AutoModelForCausalLM.from_pretrained(os.environ["MODELE_MINUSCULE"], dtype=torch.float32, device_map=carte,
                                             offload_folder=str(tmp_path / "delestage"))
    types = {p.device.type for p in m.parameters()}
    assert "meta" in types
    with pytest.raises(SystemExit):
        MES.verifier_repartition(types, getattr(m, "hf_device_map", None))


def test_activation():
    MES.verifier_activation(np.array([1.0, -3.0]), "x", 1)
    with pytest.raises(SystemExit):
        MES.verifier_activation(np.array([1.0, np.nan]), "x", 1)
    with pytest.raises(SystemExit):
        MES.verifier_activation(np.array([1.0, 70000.0]), "x", 1)


@pytest.mark.skipif(not os.environ.get("MODELE_MINUSCULE"), reason="modèle minuscule local non fourni")
def test_mesure_complete_modele_minuscule(tmp_path):
    stim = tmp_path / "stim"
    subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "construire_echelle_v2.py"), str(stim)], check=True,
                   capture_output=True)
    sortie = tmp_path / "mesure"
    code = subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "mesurer_echelle_v5.py"), "--stimuli",
                           str(stim / "echelle-v2.json"), "--sortie", str(sortie), "--modele",
                           os.environ["MODELE_MINUSCULE"], "--processeur-permis", "--type-nombre", "float32"],
                          capture_output=True, text=True).returncode
    assert code == 0
    m = json.loads((sortie / "manifeste-mesure.json").read_text())
    assert m["n_stimuli"] == 3072 and m["limite"] is None and m["couches"] == [1] and m["dernier_jeton_id"] is not None
    assert set(m["sha256_sorties"]) == {"activations-L1.npy", "ids.json"}
    # seconde exécution dans le même dossier : refus (R12)
    code2 = subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "mesurer_echelle_v5.py"), "--stimuli",
                            str(stim / "echelle-v2.json"), "--sortie", str(sortie), "--modele",
                            os.environ["MODELE_MINUSCULE"], "--processeur-permis"], capture_output=True).returncode
    assert code2 != 0
