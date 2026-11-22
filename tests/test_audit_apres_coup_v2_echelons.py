"""Essais de l'échelle des échelons simulée (rang 12) : bloc C2 retrouvé à trois étiquettes, plafond du
réapprentissage à m = 400 ; relecture en échantillon présentée comme rappel : refus nommé (bloc C3)."""
import pytest

from controle_ia.audit_apres_coup_v2 import echelons_simules as es
from controle_ia.gardes import GardeArret

E = 20261122
# [FAIT RAPPORTÉ, bloc C2, à deux chiffres] rappels à trois étiquettes ; arrondi ± 0,005 ajouté à 4 erreurs types
C2_TROIS = {"choisir": 0.34, "repondérer": 0.14, "réapprendre": 0.03}


def test_bloc_C2_a_trois_etiquettes():
    # choisir et repondérer ne lisent que la réserve (indépendante de d) : R = 400 à d = 16 ; réapprendre : d = 4 096
    reserve = es.echelle(E, etiquettes=(3,), R=400, d=16)[3]
    complet = es.echelle(E, etiquettes=(3,), R=40)[3]
    for e, attendu in C2_TROIS.items():
        moy, et = (complet if e == "réapprendre" else reserve)[e]
        assert abs(moy - attendu) <= 4 * et + 0.005, (e, moy, et)


def test_plafond_du_reapprentissage():
    assert round(es.plafond_reapprentissage(4.0, 4096, 400), 3) == 0.787
    assert round(es.plafond_reapprentissage(4.0, 4096, 10 ** 9), 3) == 0.953


def test_artefact_relecture_presentee_comme_rappel():
    v, nature = es.relecture_en_echantillon(E, 3)
    assert v == pytest.approx(1.0)  # bloc C3 : 1,000 à 4 096 poids et trois étiquettes
    with pytest.raises(GardeArret, match="relecture en échantillon"):
        es.annoncer_rappel(v, nature)
    r = es.rappels_echelons(E, 3)
    assert es.annoncer_rappel(r["réapprendre"], r["nature"]) == r["réapprendre"]
