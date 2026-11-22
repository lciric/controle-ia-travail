"""Essais de `audit_apres_coup_v1.oracle_simule` (rang 4) : verdict après le délai L ; lu avant son délai : refus."""
import numpy as np
import pytest

from controle_ia.audit_apres_coup_v1.attaque_choisie import TYPES_ILLUSTRATION
from controle_ia.audit_apres_coup_v1.oracle_simule import OracleSimule, lire_verdict
from controle_ia.audit_apres_coup_v1.regle_audit import RegleAudit, g_identite
from controle_ia.audit_apres_coup_v1.simulateur import Monde, politique_constante, simuler
from controle_ia.gardes import GardeArret


def test_episode_de_lecture_selon_le_delai():
    o = OracleSimule(1.0, 0.0, 2, "signature")
    d = np.array([0, 1, 0, 1, 1, 0, 1])
    # i=0 : endommagés après 0 aux rangs 1, 3 -> lecture à 3 ; i=1 : 3, 4 -> 4 ; i=4 : 6 puis rien -> -1
    assert o.episode_de_lecture(d).tolist() == [3, 4, 4, 6, -1, -1, -1]
    assert OracleSimule(1.0, 0.0, 0, "signature").episode_de_lecture(d).tolist() == list(range(7))


def test_verdict_apres_le_delai_et_artefact_lu_avant():
    m = Monde(3, 20261122, TYPES_ILLUSTRATION, 1.6, politique_constante(0.3), 0.0)
    r = RegleAudit(0.5, 0.0, 0.0, g_identite, 1.6)
    o = OracleSimule(1.0, 0.0, 3, "signature")
    res = simuler(m, r, o, 0, 400)
    v, h = res.journal.verdicts_par_episode()
    i = int(np.flatnonzero(h >= 0)[0])
    assert lire_verdict(res.journal, i, int(h[i])) == v[i]
    with pytest.raises(GardeArret, match="avant son délai"):
        lire_verdict(res.journal, i, int(h[i]) - 1)
    assert h[i] > 8 * i + 5  # délai de 3 endommagés : lu plus tard que la fin de l'épisode


def test_couverture_et_faux_positifs():
    o = OracleSimule(0.8, 0.0, 0, "signature")
    u = np.linspace(0, 0.999, 1000)
    v = o.verdicts(np.ones(1000, bool), u)
    assert v.mean() == pytest.approx(0.8, abs=2e-3)
    assert o.verdicts(np.zeros(1000, bool), u).sum() == 0


def test_refus_de_configuration():
    with pytest.raises(GardeArret):
        OracleSimule(0.0, 0.0, 0, "signature")
    with pytest.raises(GardeArret, match="signature"):
        OracleSimule(1.0, 0.1, 0, "signature")
    with pytest.raises(GardeArret):
        OracleSimule(1.0, 0.0, -1, "exces")
