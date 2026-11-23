import sys
def test_attribut_restaure():
    pkg = sys.modules["controle_ia.lentilles_sondes_bbis"]
    assert hasattr(pkg, "corpus_pagine_v1")
    assert sys.modules["controle_ia.lentilles_sondes_bbis.corpus_pagine_v1"] is pkg.corpus_pagine_v1
