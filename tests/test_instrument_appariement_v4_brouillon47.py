"""Essai demandé par la contre-lecture de l'instrument du bras A (b2f36f0a…, mineur I-m1) : les consignes figées sont
lues dans le texte en vigueur, le brouillon 47 (non plus le brouillon 17), et leurs empreintes sont égales à celles de
la case « consignes figées » de ce même texte (lue par programme), sans version neuve du module
`instrument_appariement_v4`. Cas sain et artefact (R5)."""
import re
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import instrument_appariement_v4 as ia

BROUILLON = Path(__file__).resolve().parents[1] / "prereg" / "T0.7-organismes-discrets-v-a-v2-brouillon47.md"
EMPREINTES_13_1 = {"appariement": "98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248",
                   "couverture": "ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816"}


def case_consignes_figees(texte):
    lignes = [l for l in texte.splitlines() if l.startswith("| consignes figées | **remplie**")]
    assert len(lignes) == 1, "une seule case « consignes figées » remplie attendue"
    app = re.search(r"consigne de l'appariement \(bloc de 3\.2\), `([0-9a-f]{64})`", lignes[0])
    cou = re.search(r"consigne de la couverture \(bloc de 3\.3\), `([0-9a-f]{64})`", lignes[0])
    return {"appariement": app.group(1), "couverture": cou.group(1)}


def test_consignes_du_brouillon_47_egales_a_la_case_consignes_figees():
    case = case_consignes_figees(BROUILLON.read_text(encoding="utf-8"))
    c = ia.consignes_du_texte(BROUILLON)
    assert {k: ia.empreinte_consigne(v) for k, v in c.items()} == case == EMPREINTES_13_1
    for k in c:
        ia.exiger_consigne_figee(c[k], case[k])                                             # cas sain
    with pytest.raises(GardeArret):
        ia.exiger_consigne_figee(c["couverture"][:-1] + "#", case["couverture"])            # artefact : un caractère
    with pytest.raises(GardeArret):
        ia.exiger_consigne_figee(c["appariement"], case["couverture"])                      # artefact : consigne échangée
