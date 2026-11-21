"""Lots scellés et reprise (exploratoire) : R5, R11, R12."""
import pytest

from controle_ia.dopamine_exploratoire import stockage_v1 as s
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines


def test_lot_sain_puis_saute(tmp_path):
    f = tmp_path / "lot-00000.jsonl"
    assert s.etat_lot(f) == "absent"
    s.ecrire_jsonl(f, [{"a": 1}])
    assert s.etat_lot(f) == "scelle" and s.lire_jsonl(f) == [{"a": 1}]
    with pytest.raises(GardeArret, match="R12"):
        s.ecrire_jsonl(f, [{"a": 2}])


def test_lot_sans_compagnon_ou_altere_arrete(tmp_path):
    f = tmp_path / "lot-00000.jsonl"
    f.write_text("{}\n")
    with pytest.raises(GardeArret, match="sans empreinte"):
        s.etat_lot(f)
    g = tmp_path / "lot-00001.jsonl"
    s.ecrire_jsonl(g, [{"a": 1}])
    g.write_text('{"a": 9}\n')
    with pytest.raises(GardeArret):
        s.etat_lot(g)


def test_reste_partiel_mis_de_cote_jamais_supprime(tmp_path):
    f = tmp_path / "lot-00000.jsonl"
    (tmp_path / "lot-00000.jsonl.partiel").write_text("coupé")
    s.ecrire_jsonl(f, [{"a": 1}])
    assert (tmp_path / "lot-00000.jsonl.partiel.abandon-1").read_text() == "coupé"
    assert s.etat_lot(f) == "scelle"


def test_lots_et_graines():
    assert s.lots(list(range(5)), 2) == [[0, 1], [2, 3], [4]]
    with pytest.raises(GardeArret):
        s.lots([1], 0)
    g = graines(["generation"], entropie=7)["generation"]
    assert s.graine_derivee(g, "q1") == s.graine_derivee(g, "q1") != s.graine_derivee(g, "q2")
    g2 = graines(["generation"], entropie=8)["generation"]
    assert s.graine_derivee(g, "q1") != s.graine_derivee(g2, "q1")
