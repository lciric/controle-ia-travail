import sys
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.lentilles_sondes_bbis import lanceur_v8  # noqa
def test_attribut_pose():
    assert hasattr(sys.modules["controle_ia.lentilles_sondes_bbis"], "corpus_pagine_v1")
