"""Les copies sans torch (reemploi_v1) rendent les mêmes octets que les fonctions originales des sondes v0 ; le paquet
sondes_v2 ne charge pas torch."""
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

from controle_ia.sondes_v2 import reemploi_v1 as r

RACINE = Path(__file__).resolve().parents[1]


def test_paquet_sans_torch():
    code = ("import sys; sys.path.insert(0, 'src'); import controle_ia.sondes_v2.programme_monde_plante_v3, "
            "controle_ia.sondes_v2.magasin_v1; print('torch' in sys.modules)")
    assert subprocess.run([sys.executable, "-c", code], cwd=RACINE, capture_output=True, text=True,
                          check=True).stdout.strip() == "False"


def test_copies_identiques_aux_originaux():
    pytest.importorskip("torch")
    from controle_ia.sondes import evaluation as ev
    from controle_ia.sondes import familles as fa
    rng = np.random.default_rng(0)
    seqs = [rng.standard_normal((int(rng.integers(2, 6)), 7)) for _ in range(30)]
    y = np.arange(30) % 2
    s = rng.standard_normal(30)
    blocs = np.repeat(np.arange(10), 3)
    assert r.aire_sous_courbe(s, y) == ev.aire_sous_courbe(s, y)
    assert r.intervalle_blocs(s, y, blocs, 300, 5) == ev.intervalle_blocs(s, y, blocs, 300, 5)
    assert r._verifier_donnees(seqs, y) == fa._verifier_donnees(seqs, y)
    a, b = r.plancher_apparie("p", 15, seqs, "max", 5, 3), ev.plancher_apparie("p", 15, seqs, "max", 5, 3)
    for x, z in zip(a, b):
        assert x.w.tobytes() == z.w.tobytes() and x.b == z.b and x.empreinte() == z.empreinte()
    w = rng.standard_normal(7)
    assert r.SondeLineaireJetons("n", 15, "max", w, 0.5).empreinte() == fa.SondeLineaireJetons("n", 15, "max", w, 0.5).empreinte()
