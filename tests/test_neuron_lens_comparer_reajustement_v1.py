"""Essais du programme de comparaison du réajustement (critère d'identité v2, section « Audit ») : cas sain et artefacts (R5).

Sur les pièces du 18 novembre (`diag/20261118-164930-neuron-lens-b-beta/`), comparées à elles-mêmes ou à une copie altérée.
"""
import copy
import json
from pathlib import Path

import pytest

from controle_ia.neuron_lens import comparer_reajustement_v1 as c

RACINE = Path(__file__).resolve().parents[1]
DIAG = RACINE / "diag/20261118-164930-neuron-lens-b-beta"
MANIF = RACINE / "runs/20261118-164930-neuron-lens-b-beta/manifeste.json"
LANCEUR = RACINE / "src/controle_ia/neuron_lens/b_beta_lancer_v3.py"

pytestmark = pytest.mark.skipif(not (DIAG / "b-beta-ajustement-R.json").exists(), reason="pièces du 18 absentes")


def _res(n):
    return json.loads((DIAG / n).read_text(encoding="utf-8"))["resultat"]


@pytest.fixture
def pieces():
    m = json.loads(MANIF.read_text(encoding="utf-8"))
    f = c.empreinte_fonction(LANCEUR.read_text(encoding="utf-8"))
    return {"R": _res("b-beta-ajustement-R.json"), "S": _res("b-beta-ajustement-S.json"), "E": _res("b-beta-export.json"),
            "M": m, "F": f}


def _octets_differents(r):
    r = copy.deepcopy(r)
    r["sha256"] = "0" * 64
    return r


def test_fonction_trouvee(pieces):
    assert pieces["F"] is not None and len(pieces["F"]) == 64
    assert c.empreinte_fonction("def autre():\n    return 1\n") is None


def test_sain_palier_1_contre_soi_meme(pieces):
    r = c.comparer(pieces["R"], pieces["R"], pieces["M"], pieces["M"], pieces["F"], pieces["F"], eref=pieces["E"], eneuf=pieces["E"])
    assert r["mention"] == c.PALIER_1
    assert r["declencheurs"] == ["(i) palier 1 obtenu"]
    assert r["matrices_moities_egales"]["couches_egales"] == r["matrices_moities_egales"]["couches_ref"] == 31


def test_sain_ecart_nul_octets_differents_declencheur_ii(pieces):
    for L in ("R", "S"):
        r = c.comparer(pieces[L], _octets_differents(pieces[L]), pieces["M"], pieces["M"], pieces["F"], pieces["F"])
        assert r["mention"] == c.PALIER_2, (L, r["preconditions"])
        assert "(ii) écart maximal exactement nul avec des octets différents" in r["declencheurs"]
        assert r["ecart_max_abs_diffs_float64"] == 0.0
        assert len(r["table_ecarts_diffs_float64"]) == (63 if L == "R" else 64)


def test_artefact_valeur_deplacee_differente(pieces):
    n = _octets_differents(pieces["R"])
    n["diffs_float64"]["mid"][5] += 2e-3
    r = c.comparer(pieces["R"], n, pieces["M"], pieces["M"], pieces["F"], pieces["F"])
    assert r["mention"] == c.DIFFERENTE and "(iii) lentille différente" in r["declencheurs"]
    assert abs(r["ecart_max_abs_diffs_float64"] - 2e-3) < 1e-12


def test_bord_de_tolerance(pieces):
    n = _octets_differents(pieces["S"])
    n["diffs_float64"]["out"][0] += 0.9e-3
    assert c.comparer(pieces["S"], n, pieces["M"], pieces["M"], pieces["F"], pieces["F"])["mention"] == c.PALIER_2


@pytest.mark.parametrize("val", [float("nan"), float("inf"), None, "0.1"])
def test_artefact_valeur_non_finie_non_comparable(pieces, val):
    n = _octets_differents(pieces["R"])
    n["diffs_float64"]["out"][3] = val
    r = c.comparer(pieces["R"], n, pieces["M"], pieces["M"], pieces["F"], pieces["F"])
    assert r["mention"] == c.NON_COMPARABLE and "(iv) non comparable" in r["declencheurs"]
    assert "ecart_max_abs_diffs_float64" not in r          # jamais avalé par un maximum


def test_artefact_62_valeurs_non_comparable(pieces):
    n = _octets_differents(pieces["R"])
    n["diffs_float64"]["mid"] = n["diffs_float64"]["mid"][:-1]
    r = c.comparer(pieces["R"], n, pieces["M"], pieces["M"], pieces["F"], pieces["F"])
    assert r["mention"] == c.NON_COMPARABLE


def test_artefact_meta_change_non_comparable(pieces):
    n = _octets_differents(pieces["R"])
    n["meta"]["dim_batch"] = 128
    r = c.comparer(pieces["R"], n, pieces["M"], pieces["M"], pieces["F"], pieces["F"])
    assert r["mention"] == c.NON_COMPARABLE
    assert any("dim_batch" in p["detail"] for p in r["preconditions"] if not p["tenu"])


@pytest.mark.parametrize("champ,val", [("n_docs", [466, 465]), ("next_doc", 931), ("fichier", "autre.pt")])
def test_artefacts_comptes_et_nom(pieces, champ, val):
    n = _octets_differents(pieces["S"])
    n[champ] = val
    assert c.comparer(pieces["S"], n, pieces["M"], pieces["M"], pieces["F"], pieces["F"])["mention"] == c.NON_COMPARABLE


def test_artefacts_commit_voisin_et_fonction(pieces):
    m2 = copy.deepcopy(pieces["M"])
    m2["config"]["commit_voisin"] = "0" * 40
    n = _octets_differents(pieces["R"])
    assert c.comparer(pieces["R"], n, pieces["M"], m2, pieces["F"], pieces["F"])["mention"] == c.NON_COMPARABLE
    assert c.comparer(pieces["R"], n, pieces["M"], pieces["M"], pieces["F"], "f" * 64)["mention"] == c.NON_COMPARABLE
    assert c.comparer(pieces["R"], n, pieces["M"], pieces["M"], pieces["F"], None)["mention"] == c.NON_COMPARABLE


def test_anomalie_fichier_egal_matrice_differente(pieces):
    e2 = copy.deepcopy(pieces["E"])
    e2["matrices_moities"]["7"] = ["0" * 64, "0" * 64]
    r = c.comparer(pieces["R"], pieces["R"], pieces["M"], pieces["M"], pieces["F"], pieces["F"], eref=pieces["E"], eneuf=e2)
    assert r["mention"] == c.SUSPENDU
    assert any(d.startswith("(v)") for d in r["declencheurs"])


def test_reprise_palier_1_notee(pieces):
    r = c.comparer(pieces["S"], pieces["S"], pieces["M"], pieces["M"], pieces["F"], pieces["F"], reprise=True)
    assert r["mention"].startswith(c.PALIER_1) and "reprise" in r["mention"]
    assert r["series_export_R_sans_critere"].startswith("sans objet")


def test_changement_de_cote_du_seuil_rapporte(pieces):
    n = _octets_differents(pieces["R"])
    i = next(i for i, x in enumerate(n["diffs"]["mid"]) if 0.10 < x)     # une valeur au-dessus du seuil
    n["diffs"]["mid"][i] = 0.0999
    r = c.comparer(pieces["R"], n, pieces["M"], pieces["M"], pieces["F"], pieces["F"])
    assert r["mention"] == c.PALIER_2      # la décision porte sur diffs_float64 seulement
    assert any(x["rang"] == i for x in r["changements_de_cote_du_seuil_0_10_sur_diffs"])


def test_cli_n_ecrase_pas(tmp_path, pieces):
    s = tmp_path / "s.json"
    args = ["--ref-ajustement", str(DIAG / "b-beta-ajustement-S.json"), "--neuf-ajustement", str(DIAG / "b-beta-ajustement-S.json"),
            "--ref-manifeste", str(MANIF), "--neuf-manifeste", str(MANIF), "--lanceur-ref", str(LANCEUR),
            "--lanceur-neuf", str(LANCEUR), "--sortie", str(s)]
    c.main(args)
    assert json.loads(s.read_text())["mention"] == c.PALIER_1
    with pytest.raises(SystemExit):
        c.main(args)
