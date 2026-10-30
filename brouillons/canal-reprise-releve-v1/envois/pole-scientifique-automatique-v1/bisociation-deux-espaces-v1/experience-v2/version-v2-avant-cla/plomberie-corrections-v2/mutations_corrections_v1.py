"""Mutations des corrections v2 : chaque garde neutralisée doit faire échouer son essai (xfail strict : l'essai DOIT
échouer). Usage : PYTHONPATH=<dépôt>/src python3 -B -m pytest -q -p no:cacheprovider plomberie-corrections-v2/mutations_corrections_v1.py"""
import sys
from pathlib import Path
E = str(Path(__file__).resolve().parents[1])
sys.path.insert(0, E + "/essais")
import pytest
import essais_corrections_v2 as ec
import mesures_v2 as ms, lecture_v2 as le, monde_v2 as mo

X = pytest.mark.xfail(strict=True)

@X
def test_m1_inertes_invocation(tmp_path, monkeypatch):
    monkeypatch.setattr(ms, "verifier_inertes_lignes", lambda *a, **k: 0)
    ec.test_inertes_invocation_artefact_arret_avant_le_fichier_de_M_inertes(tmp_path, monkeypatch)

@X
def test_m2_inertes_v9(monkeypatch):
    monkeypatch.setattr(ms, "verifier_inertes", lambda *a, **k: "x")
    ec.test_inertes_v9_sain_et_artefact(monkeypatch)

@X
def test_m3_identites(monkeypatch):
    monkeypatch.setattr(le, "BRAS_IDENTITE_AUDIT", ())
    ec.test_identites_artefact_non_declarees_declenchent()

@X
def test_m4_identites_filtre_declarees(monkeypatch):
    monkeypatch.setattr(le, "IDENTITES_DECLAREES", set())
    ec.test_identites_sain_declarees_ou_hors_liste_ne_declenchent_pas()

@X
def test_m5_replantation_absente(monkeypatch):
    monkeypatch.setattr(mo, "MAX_REPLANTATIONS", 0)
    ec.test_q01_sain_replantation_garde_le_monde_de_base()

@X
def test_m6_jumelle_inerte(monkeypatch):
    vrai = mo.generer
    monkeypatch.setattr(mo, "generer", lambda c, r, i, s=None: vrai(c, r, i, None))
    ec.test_q04_sain_copie_change_le_cosinus_des_paires_plantees_sur_3_mondes()
