"""Correctif 0025 (contre-lecture du 0022, majeur) : la vitesse du premier lot est un diagnostic ; une durée non mesurée au lot 1
(ici l'oracle N, que la fin de l'étalonnage n'exige pas) s'écrit null, nommée, et l'étalonnage continue jusqu'à sa fin.
Cas sain : tirage passé par l'appelant, écrit tel quel. Hors des listes figées (aucun nombre d'essais attendus ne change)."""
import json

from test_iib_lanceur_v5 import _monde

from controle_ia.iib import lanceur_v5 as la
from controle_ia.iib.jouet_v5 import ModeleJouetDeLangue
from controle_ia.scellement import verifier


def test_artefact_oracle_N_non_mesure_au_lot_1_l_etalonnage_continue(tmp_path, monkeypatch, capfd):
    origine = la.vitesse_du_premier_lot

    def sans_oracle_N(chrono, modele, tirage=None):
        return origine({k: v for k, v in chrono.items() if not k.startswith("oracle_N")}, modele, tirage)

    monkeypatch.setattr(la, "vitesse_du_premier_lot", sans_oracle_N)
    config = _monde(tmp_path)
    r = la.phase_etalonnage(config, tmp_path, tmp_path / "course", ModeleJouetDeLangue(), la.MondeJouet(), carte=False, tirage="processeur")
    assert r is not None and (tmp_path / "course" / la.NOMS["etalonnage"]).exists()        # fin écrite : aucun arrêt
    f = tmp_path / "course" / la.VITESSE
    v = json.loads(f.read_text(encoding="utf-8"))
    assert verifier(f) and v["oracle_N_s_par_action"] is None and v["non_mesurees"] == ["oracle_N_s_par_action"]
    assert v["oracle_P_s_par_action"] > 0 and v["tirage"] == "processeur"
    assert "oracle_N_s_par_action=non_mesuree" in capfd.readouterr().err
