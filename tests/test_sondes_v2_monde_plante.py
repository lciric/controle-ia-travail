"""Essais de la brique D (épreuve à vérité plantée v1) : générateur, vérités engagées, intervalles exacts, programme de
bout en bout. L'essai lent (dimension 4 096) ne tourne que si SONDES_V2_LENT=1."""
import json
import os
import shutil

import numpy as np
import pytest
from scipy.stats import binomtest

from controle_ia.gardes import GardeArret
from controle_ia.sondes_v2 import monde_plante_v1 as mp
from controle_ia.sondes_v2 import programme_monde_plante_v1 as prog


def test_generateur_structure():
    p = mp.Parametres(d=16, n_unites=3, n_honnetes_non_apparies=2, n_taches=2, actions_par_tache=2,
                      bruit_lecture=0.0, identite=2.0, trace=1.0, interaction=5.0)
    m = mp.generer(p, np.random.default_rng(0))
    assert set(m["lectures"]) == {"S0", "H0", "S1", "H1", "S2", "H2", "N0", "N1"}
    assert len(m["textes"]) == 2 * 2 * 2
    for cle, (t, src) in m["textes"].items():
        d = m["lectures"]["S0"][cle] - m["lectures"]["H0"][cle]
        if src == "honnete":
            # même texte, même décalage d'identité dans la paire, sans bruit : seule la trace commune les sépare
            np.testing.assert_allclose(np.linalg.norm(d, axis=1), 1.0, rtol=1e-12)
        else:
            # interaction sur le seul jeton porteur des textes sabotés lus par les saboteurs
            assert (np.linalg.norm(d, axis=1) > 1.5).sum() == 1
        # deux unités différentes : décalages d'identité différents
        assert np.linalg.norm(m["lectures"]["H0"][cle] - m["lectures"]["H1"][cle]) > 0.1
        k = len(m["lectures"]["N0"][cle])
        assert p.jetons_min <= k <= p.jetons_max


def test_generateur_deterministe_et_gardes():
    p = mp.Parametres(d=8, n_taches=2, actions_par_tache=1)
    a = mp.generer(p, np.random.default_rng(5))
    b = mp.generer(p, np.random.default_rng(5))
    assert all(np.array_equal(a["lectures"][s][c], b["lectures"][s][c]) for s in a["lectures"] for c in a["textes"])
    for mauvais in (dict(n_unites=1), dict(trace=-1.0), dict(jetons_porteurs=5, jetons_min=3)):
        with pytest.raises(GardeArret):
            mp.generer(mp.Parametres(d=8, **mauvais), np.random.default_rng(0))


def test_interaction_sur_trace_efface_la_trace():
    p = mp.Parametres(d=8, n_taches=2, actions_par_tache=1, bruit_lecture=0.0, trace=1.5, interaction=-1.5,
                      interaction_sur_trace=True)
    m = mp.generer(p, np.random.default_rng(0))
    for cle, (_, src) in m["textes"].items():
        d = m["lectures"]["S0"][cle] - m["lectures"]["H0"][cle]
        attendu = 0.0 if src == "sabote" else 1.5
        np.testing.assert_allclose(np.linalg.norm(d, axis=1), attendu, atol=1e-12)


def test_verites_scellees(tmp_path):
    v, sha = mp.charger_verites()
    assert set(v["mondes"]) == {"identite_seule", "trace_commune", "texte_seul", "interaction",
                                "interaction_contraire", "etiquettes_permutees", "fuite_de_pli"}
    for m in v["mondes"]:
        mp.parametres_du_monde(v, m, (5, 5, 2), 16).verifier()
    copie = tmp_path / mp.CHEMIN_VERITES.name
    shutil.copy(mp.CHEMIN_VERITES, copie)
    shutil.copy(str(mp.CHEMIN_VERITES) + ".sha256", str(copie) + ".sha256")
    mp.charger_verites(copie)  # sain
    copie.write_text(copie.read_text().replace('"trace": 1.5', '"trace": 9.5'))
    with pytest.raises(GardeArret, match="empreinte"):
        mp.charger_verites(copie)


@pytest.mark.parametrize("x,n", [(0, 10), (10, 10), (3, 20), (7, 7), (1, 1)])
def test_clopper_pearson(x, n):
    bas, haut = mp.clopper_pearson(x, n)
    ref = binomtest(x, n).proportion_ci(confidence_level=0.95, method="exact")
    assert (bas, haut) == pytest.approx((ref.low, ref.high), abs=1e-12)
    with pytest.raises(GardeArret):
        mp.clopper_pearson(3, 2)


def test_comparer():
    att = {"contraste": {"admises": ["non établie", "contraire"], "nature": "fausse_lecture"}}
    assert mp.comparer({"contraste": "contraire"}, att) == {"contraste": True}
    assert mp.comparer({"contraste": "établie"}, att) == {"contraste": False}
    with pytest.raises(GardeArret):
        mp.comparer({}, att)


def test_programme_de_bout_en_bout(tmp_path):
    """Une réplique de chaque monde, petite taille : le programme lit, compare aux vérités engagées et rapporte ; à
    graine égale, deux exécutions rendent les mêmes lectures ; le rapport n'est jamais écrasé."""
    kw = dict(tailles=[(5, 5, 2)], repliques=1, n_nul=39, alpha=0.05, seuil_identite=0.9, d=32, entropie=20261122)
    c1 = prog.executer(tmp_path / "a", **kw)
    r = json.loads(c1.read_text())
    assert (tmp_path / "a" / (c1.name + ".sha256")).is_file()
    t = r["tailles"]["5,5,2"]
    for monde, v in t.items():
        for critere, x in v["criteres"].items():
            assert x["repliques"] == 1 and 0.0 <= x["intervalle_95"][0] <= x["intervalle_95"][1] <= 1.0
    # mécanique de comparaison : sur cette graine, chaque monde donne sa lecture attendue
    assert t["fuite_de_pli"]["criteres"]["fuite"]["taux_arret_garde"] == 1.0
    assert t["trace_commune"]["criteres"]["contraste"]["puissance"] == 1.0
    assert t["interaction_contraire"]["criteres"]["interaction"]["puissance"] == 1.0
    assert t["identite_seule"]["criteres"]["contraste"]["taux_fausse_lecture"] == 0.0
    c2 = prog.executer(tmp_path / "b", **kw)
    r2 = json.loads(c2.read_text())
    assert json.dumps(r["tailles"], sort_keys=True) == json.dumps(r2["tailles"], sort_keys=True)
    with pytest.raises(GardeArret, match="R12"):
        prog.executer(tmp_path / "a", **kw)
    with pytest.raises(GardeArret, match="non engagés"):
        prog.executer(tmp_path / "c", **{**kw, "entropie": 1}, mondes=["monde_inventé"])


def test_programme_ligne_de_commande(tmp_path, capsys):
    assert prog.main(["--sortie", str(tmp_path), "--taille", "5,5,2", "--repliques", "1", "--nul", "19",
                      "--d", "16", "--entropie", "3", "--mondes", "fuite_de_pli,etiquettes_permutees"]) == 0
    assert capsys.readouterr().out.strip().endswith(".json")
    with pytest.raises(GardeArret):
        prog._taille("5,5")


@pytest.mark.skipif(os.environ.get("SONDES_V2_LENT") != "1", reason="essai lent : SONDES_V2_LENT=1")
def test_lent_dimension_4096(tmp_path):
    """Essai lent : mondes « trace commune » et « identité seule » en dimension 4 096."""
    c = prog.executer(tmp_path, tailles=[(5, 5, 2)], repliques=1, n_nul=19, alpha=0.05, seuil_identite=0.9, d=4096,
                      entropie=4096, mondes=["trace_commune", "identite_seule"])
    t = json.loads(c.read_text())["tailles"]["5,5,2"]
    assert t["identite_seule"]["criteres"]["identite"]["puissance"] == 1.0
    assert t["trace_commune"]["criteres"]["contraste"]["puissance"] == 1.0
