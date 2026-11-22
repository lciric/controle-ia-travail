"""Tests (pytest) des gardes du lanceur du pilote : rejoue chaque cas de `epreuves_gardes_pilote_v1.py` (cas sains et
artefacts), plus des propriétés de la borne. Faux client seulement ; aucun appel, aucun réseau.
Usage : python -m pytest -q test_gardes_pilote_essaim_v1.py   (racine du dépôt trouvée au-dessus, ou DEPOT_CONTROLE_IA)"""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epreuves_gardes_pilote_v1 as E  # noqa: E402
import garde_pilote_essaim_v1 as GP  # noqa: E402
import lanceur_pilote_essaim_v1 as L  # noqa: E402

PRIX, _ = E.prix_kimi()
LISTE, BORNE = E.cas(PRIX)


@pytest.mark.parametrize("k", range(len(LISTE)), ids=[c[0] for c in LISTE])
def test_cas_du_lanceur(k, tmp_path):
    nom, garde, plan, fab, entree, kw, attendu = LISTE[k]
    jr = tmp_path / "journal.jsonl"
    code, g = L.courir(plan, fab(), entree, str(jr), PRIX, **kw)
    assert code == attendu
    derniere = json.loads(jr.read_text(encoding="utf-8").splitlines()[-1])
    if attendu == 0:
        assert derniere["evenement"] == "fin" and g.termine()
    else:
        assert derniere["evenement"] == "arret" and derniere["code"] == attendu
    if g is not None:
        assert g.depense <= g.plafond_depense + 1e-9


def test_garde_du_plan():
    for r in E.cas_plan_direct(PRIX):
        assert r["tenu"], r


def test_borne_est_le_produit_annonce():
    b = GP.borne_pire(GP.plan_pstd(), PRIX)
    assert b["appels_du_plan"] == 744 and b["relances_au_plus"] == 74
    attendu = 12 * (50 * GP.cout(23200, 24000, PRIX) + 12 * GP.cout(6000, 2000, PRIX))
    assert abs(b["aux_plafonds_de_jetons_usd"] - attendu) < 1e-6
    assert b["pire_usd"] == pytest.approx(attendu + 74 * GP.reserve_dure("proposeur", GP.PLAFOND_ENTREE_OCTETS["proposeur"], 24000, PRIX)
                                          + b["exces_d_un_appel_usd"], abs=1e-3)


def test_journal_jamais_ecrase(tmp_path):
    jr = tmp_path / "j.jsonl"
    jr.write_text("existant\n", encoding="utf-8")
    with pytest.raises(FileExistsError):
        L.courir(GP.plan_pstd(), E.FauxClient(usage=E.au_plafond), E.entree_taille(E.ENTREE_ATTENDUE), str(jr), PRIX)
    assert jr.read_text(encoding="utf-8") == "existant\n"


def test_execution_directe_refusee(tmp_path):
    assert L.main(["lanceur", str(tmp_path / "j.jsonl")]) == L.CODE_SANS_CLIENT
