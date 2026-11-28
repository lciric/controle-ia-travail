"""Test proposé par la vérification neuve du module v3 (réserve G6-02) : garde 6 AU LANCEMENT, exception du chargeur
gelé convertie. Placé à côté d'une copie du module et des tests v3 ; n'utilise que leurs aides et fixtures.

Cas : dépôt jouet propre ; les gardes 1 à 5 passent réellement ; le chargeur gelé (`lecture.charger_source`, appelé par
la seule garde 6) lève une `KeyError`. Attendu : `GardeArret` de type exact, motif « garde 6 : run source <run> non
vérifiable (KeyError : 'scores') », rien d'écrit (arrêt avant le manifeste). Le cas sain est le passage réussi de
`test_ligne_de_commande_de_bout_en_bout`.
"""
import re
import sys

sys.dont_write_bytecode = True

import pytest  # noqa: E402

from test_audit_verdict_p3_v1 import RUN_A, GardeArret, _lancer, _rien_ecrit, depot_jetable, gabarit, lp  # noqa: E402,F401


def test_garde_6_au_lancement_exception_du_chargeur_convertie(depot_jetable, monkeypatch):  # noqa: F811
    d, m, _ = depot_jetable

    def leve(racine, run_id):
        raise KeyError("scores")

    monkeypatch.setattr(lp, "charger_source", leve)
    run = "20261020-129000-addendum2-p3"
    with pytest.raises(GardeArret, match=re.escape(f"garde 6 : run source {RUN_A} non vérifiable (KeyError : 'scores')")) as e:
        _lancer(d, m, run)
    assert type(e.value) is GardeArret
    assert _rien_ecrit(d, run)
