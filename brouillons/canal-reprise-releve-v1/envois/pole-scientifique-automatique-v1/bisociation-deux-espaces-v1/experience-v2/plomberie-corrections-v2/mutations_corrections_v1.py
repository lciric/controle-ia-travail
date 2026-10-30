"""Mutations des corrections v2 : chaque garde neutralisée doit faire échouer son essai (xfail strict : l'essai DOIT
échouer). Usage : PYTHONPATH=<dépôt>/src python3 -B -m pytest -q -p no:cacheprovider plomberie-corrections-v2/mutations_corrections_v1.py
m7 et m8 ajoutées par les corrections CLA (garde d'empreinte de l'addendum, CLA-04 ; identités entre toutes les paires,
CLA-03)."""
import sys
from pathlib import Path
E = str(Path(__file__).resolve().parents[1])
sys.path.insert(0, E + "/essais")
import pytest
import essais_corrections_v2 as ec
import essais_cla_v2 as ecla
import invocation_unique_v2 as inv
import mesures_v2 as ms, lecture_v2 as le, monde_v2 as mo
from controle_ia.gardes import GardeArret
from controle_ia.scellement import compagnon, verifier

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

# --- corrections CLA (contre-lecture R2 de l'addendum v3 ; addendum v4, (vii)) ------------------------------------

def _exiger_addendum_sans_empreinte(depot):
    """La garde telle qu'avant CLA-04 : compagnon présent et concordant, sans comparaison à EMPREINTE_ADDENDUM."""
    chemin = Path(depot) / "prereg" / inv.ADDENDUM
    if not chemin.is_file() or not compagnon(chemin).is_file():
        raise GardeArret("addendum non scellé")
    return verifier(chemin)


@X
def test_m7_addendum_sans_empreinte_fixee(tmp_path, monkeypatch):
    monkeypatch.setattr(inv, "exiger_addendum_scelle", _exiger_addendum_sans_empreinte)
    ecla.test_cla04_artefact_texte_modifie_puis_rescelle_refuse(tmp_path, monkeypatch)


def _identites_a_N_seulement(lignes):
    """La chaîne telle qu'avant CLA-03 : chaque bras comparé à N seulement."""
    ident = None
    for l in lignes:
        if l["exclu"]:
            continue
        egaux = {("N", b) for b, m in l["bras"].items() if b != "N" and m["_paires"] == l["bras"]["N"]["_paires"]}
        ident = egaux if ident is None else ident & egaux
    return sorted(ident or [])


@X
def test_m8_identites_sans_paires_entre_temoins(monkeypatch):
    monkeypatch.setattr(inv, "identites_paires", _identites_a_N_seulement)
    ecla.test_cla03_artefact_copies_sur_tous_les_mondes_non_exclus_rapportees_et_filtrees()
