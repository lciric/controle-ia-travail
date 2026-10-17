"""Notation vectorisée de P3 : identité avec le code de référence pour chaque famille et chaque agrégation (cas sain),
garde d'identité qui arrête sur une notation faussée (artefact), gardes d'entrée."""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.harnais.sondes import SondeLineaire
from controle_ia.premier_test_ia.notation import Notation, exiger_identite
from controle_ia.sondes.evaluation import plancher_apparie
from controle_ia.sondes.familles import Reglages, entrainer

D = 12


def _sondes():
    rng = np.random.default_rng(0)
    seqs = [rng.standard_normal((int(rng.integers(3, 9)), D)) + (0.8 if k % 2 else 0.0) for k in range(24)]
    y = np.array([k % 2 for k in range(24)])
    sondes = []
    for c in (1, 2):
        for fam, ag in (("difference_moyennes", "max"), ("lineaire", "max"), ("lineaire", "attention"),
                        ("perceptron", "max"), ("perceptron", "attention"), ("attention", "attention"),
                        ("mahalanobis", "max")):
            sondes.append(entrainer(fam, f"{fam}-{ag}-{c}", c, seqs, y, ag, 3, Reglages(epoques=5)))
        sondes += plancher_apparie(f"pl-{c}", c, seqs, "max", 4, 5) + plancher_apparie(f"pa-{c}", c, seqs, "attention", 3, 6)
    sondes.append(SondeLineaire("harnais-1", 1, rng.standard_normal(D), 0.3, "attention", rng.standard_normal(D)))
    return sondes, rng


def test_identite_toutes_familles():
    sondes, rng = _sondes()
    n = Notation(sondes, "cpu")
    for _ in range(5):
        L = int(rng.integers(1, 7))
        seg = {1: rng.standard_normal((L, D)) * 3, 2: rng.standard_normal((L, D))}
        scores = n.noter(seg)
        assert set(scores) == {s.nom for s in sondes}
        r = exiger_identite(n, seg, scores, tolerance=1e-9)
        assert r["sondes_controlees"] == len(sondes) and r["ecart_relatif_max"] <= 1e-9


def test_garde_identite_arrete_sur_score_fausse():
    sondes, rng = _sondes()
    n = Notation(sondes, "cpu")
    seg = {1: rng.standard_normal((4, D)), 2: rng.standard_normal((4, D))}
    scores = n.noter(seg)
    nom = next(s.nom for s in sondes if s.agregation == "attention")
    scores[nom] += 1e-3
    with pytest.raises(GardeArret, match="garde d'identité"):
        exiger_identite(n, seg, scores)
    r = exiger_identite(n, seg, n.noter(seg), sauf_familles=("mahalanobis",))
    assert r["sondes_controlees"] == len(sondes) - 2


def test_notation_gardes():
    sondes, rng = _sondes()
    n = Notation(sondes, "cpu")
    with pytest.raises(GardeArret, match="absente"):
        n.noter({1: rng.standard_normal((3, D))})
    with pytest.raises(GardeArret, match="vide"):
        n.noter({1: np.zeros((0, D)), 2: rng.standard_normal((3, D))})
    a = rng.standard_normal((3, D))
    a[1, 2] = np.nan
    with pytest.raises(GardeArret, match="non finie"):
        n.noter({1: a, 2: rng.standard_normal((3, D))})
    with pytest.raises(GardeArret, match="double"):
        Notation(sondes + sondes[:1])
    moyenne = SondeLineaire("moyenne", 1, np.ones(D), 0.0, "mean")
    with pytest.raises(GardeArret, match="refusée"):
        Notation([moyenne])
