"""Essais complémentaires de la garde de durée de tour du pilote (`lanceur_v21`), demandés par la contre-lecture de
l'addendum 7 (M-9) : pilote repris pour une autre cause, puis garde ; t non fini. Les réponses factices de la règle
portent t = 105 s (`test_temoin_bailey_condition6_v4.reponses`)."""
from __future__ import annotations

import pytest

import test_temoin_bailey_condition6_v21 as T
from controle_ia.temoin_bailey import lanceur_v21 as la


@pytest.mark.parametrize("plafond,principal", [(104.0, False), (105.0, True)])
def test_pilote_repris_pour_une_autre_cause_puis_garde(tmp_path, monkeypatch, plafond, principal):
    """Pilote mort (reprise ouverte par la liste d'arrêt), reprise finie, puis la règle : la garde s'applique au t de
    la règle comme sans reprise ; au-dessus du plafond : arrêt avant le run principal, sans nouvelle reprise."""
    c, f, _ = T.conduite(tmp_path, monkeypatch, T.reponses(pilote="mort"))
    f.tours["pilote"] = {"tours_complets": 0, "journal_absent": None, "gardes_tombees": []}
    c.t_max_pilote_s = plafond
    bilan = c.conduire()
    assert f.lance[4:7] == ["pilote", "pilote-reprise", "regle"]
    assert ("principal" in f.lance) is principal and f.detruites == ["77"]
    if not principal:
        assert bilan["arret"].startswith("durée de tour du pilote au-delà du plafond (105.0 s > 104.0 s)")
        assert f.lance.count("pilote-reprise") == 1


@pytest.mark.parametrize("t", [float("nan"), float("inf")])
def test_t_non_fini_arrete(tmp_path, monkeypatch, t):
    """t non fini à la règle : la comparaison « t ≤ plafond » est fausse : arrêt avant le run principal."""
    reps = T.reponses()
    etat, code = reps["regle"]
    reps["regle"] = ({**etat, "t": t}, code)
    c, f, _ = T.conduite(tmp_path, monkeypatch, reps)
    c.t_max_pilote_s = 1800.0
    bilan = c.conduire()
    assert "principal" not in f.lance and f.detruites == ["77"]
    assert bilan["arret"].startswith("durée de tour du pilote au-delà du plafond")
