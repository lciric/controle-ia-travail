"""Essais R5 des pré-contrôles C-1 et C-2 : cas sain et artefact pour chaque règle (paires factices écrites par le test, pas des paires des jeux)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import precontrole_c1_c2_v1 as pc
def action(titre, prop, ctrl="Compare against the reference run.", cout=100):
    return f"ACTION: ADD\nTITLE: {titre}\nPROPOSAL: {prop}\nCONTROLS: {ctrl}\nCOST: {cout}\nPREDICTION: The claim fails if the gap closes."
SAIN0 = action("Probing a retrieval head on two corpora", "Train a probe on 3 seeds. Evaluate it on a held-out split.")
SAIN1 = action("Probing a rerank head on two corpora", "Train a probe on 5 seeds. Evaluate it on a held-out split.")
def test_c1_sain_aucun_mot():
    assert pc.c1_defaut(SAIN0, SAIN1) == (False, None)
def test_c1_sain_mot_chez_les_deux():
    a = action("Sweeps of a probe on two corpora", "Train a probe on 3 seeds.")
    b = action("Sweeps of a head on two corpora", "Train a head on 5 seeds.")
    assert pc.c1_defaut(a, b) == (False, None)
def test_c1_artefact_titre():
    b = action("Probing a rerank head across two corpora", "Train a probe on 5 seeds.")
    assert pc.c1_defaut(SAIN0, b) == (True, 1)
def test_c1_artefact_premiere_phrase_et_sens():
    a = action("Probing a head", "Train several probes on 3 seeds. Evaluate them.")
    assert pc.c1_defaut(a, SAIN1) == (True, 0)
def test_c1_hors_zone_non_compte():
    b = action("Probing a head", "Train a probe on 5 seeds. Evaluate it on several held-out splits.")
    assert pc.c1_defaut(SAIN0, b) == (False, None)
def test_c2_sain():
    assert pc.c2_defaut(SAIN0, SAIN1) == (False, None)
    a = action("Probing", "Use ViT-L features.", ctrl="Compare with ViT-L features."); b = action("Probing", "Use ViT-L backbones.")
    assert pc.c2_defaut(a, b) == (False, None)
def test_c2_artefact():
    b = action("Probing", "Train a probe on a 70B model with 5 seeds.")
    assert pc.c2_defaut(SAIN0, b) == (True, 1)
def test_c2_apres_cost_non_compte():
    b = SAIN1.replace("The claim fails", "The claim with a 70B model fails")
    assert pc.c2_defaut(SAIN0, b) == (False, None)
