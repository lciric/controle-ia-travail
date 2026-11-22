import numpy as np
import pytest

from controle_ia.hasard_defenseur_v2 import contraste_v2 as C


def test_constat_4_cellules_constantes_a_k_3():
    L = np.array([[[0, 0, 0, 1, 1, 1, 2, 2, 2]]], dtype=np.int8)
    z = np.array([[0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.6, 0.6, 0.6]])  # variances nulles ; sans la correction : 8,2·10⁷
    assert C.stat_studentisee(z, L, 3)[0] == pytest.approx(0.5e6)
