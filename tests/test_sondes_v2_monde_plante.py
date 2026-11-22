"""Essais de la brique D v2 (épreuve à vérité plantée ; erratum 1, § 6) : générateur, vérités engagées, intervalles
exacts, programme de bout en bout. L'essai lent (dimension 4 096) ne tourne que si SONDES_V2_LENT=1."""
import json
import math
import os
import shutil

import numpy as np
import pytest
from scipy.stats import binomtest

from controle_ia.gardes import GardeArret
from controle_ia.sondes_v2 import lecture_v1 as lc
from controle_ia.sondes_v2 import monde_plante_v2 as mp
from controle_ia.sondes_v2 import programme_monde_plante_v2 as prog
from controle_ia.sondes_v2 import statistiques_v1 as st

SEUILS = {"alpha": 0.05, "u_fort": 0.9, "seuil_identite": 0.9}


def test_generateur_structure():
    p = mp.Parametres(d=64, n_paires=3, n_taches=2, actions_par_tache=2, bruit_lecture=0.0, tau=2.0, eta=1.0,
                      interaction=5.0)
    m = mp.generer(p, np.random.default_rng(0))
    assert set(m["lectures"]) == {"N", "S0", "J0", "S1", "J1", "S2", "J2"}
    assert m["paires"] == [("S0", "J0"), ("S1", "J1"), ("S2", "J2")]
    ecarts = []
    for cle, (t, src) in m["textes"].items():
        d = m["lectures"]["S0"][cle] - m["lectures"]["J0"][cle]
        if src == "honnete":
            # même texte, même identité dans la paire : seuls l'écart propre (norme 1) et la trace (norme 2) restent
            ecarts.append(d[0])
            np.testing.assert_allclose(d, np.broadcast_to(d[0], d.shape), atol=1e-12)
        else:
            assert (np.linalg.norm(d - ecarts[0] if ecarts else d, axis=1) > 4.0).sum() <= 1
    assert 1.0 <= np.linalg.norm(ecarts[0]) <= 3.0
    # le nu n'a aucun décalage : il ne diffère d'un jumeau que par l'identité
    c = next(iter(m["textes"]))
    assert np.linalg.norm(m["lectures"]["J0"][c][0] - m["lectures"]["N"][c][0]) > 0.5


def test_intensite_et_interaction_sur_trace():
    p = mp.Parametres(d=32, n_paires=2, n_taches=2, actions_par_tache=1, bruit_lecture=0.0, eta=0.0,
                      intensite=1.0, sigma_I=1.0, identite_isotrope=0.0)
    m = mp.generer(p, np.random.default_rng(1))
    c = next(c for c, (_, so) in m["textes"].items() if so == "honnete")
    dj = m["lectures"]["J0"][c][0] - m["lectures"]["N"][c][0]
    ds = m["lectures"]["S0"][c][0] - m["lectures"]["N"][c][0]
    # composante d'intensité : norme σ_I √2 pour le jumeau, 1,2 fois pour le saboteur (identité le long de la trace à part)
    assert np.linalg.norm(ds - dj) == pytest.approx(0.2 * math.sqrt(2), rel=1e-9)
    p = mp.Parametres(d=8, n_paires=2, n_taches=2, actions_par_tache=1, bruit_lecture=0.0, eta=0.0, tau=1.5,
                      interaction=-1.5, interaction_sur_trace=True)
    m = mp.generer(p, np.random.default_rng(0))
    for cle, (_, src) in m["textes"].items():
        d = m["lectures"]["S0"][cle] - m["lectures"]["J0"][cle]
        np.testing.assert_allclose(np.linalg.norm(d, axis=1), 0.0 if src == "saboteur" else 1.5, atol=1e-12)


def test_gardes_du_generateur():
    for mauvais in (dict(n_paires=1), dict(tau=-1.0), dict(jetons_porteurs=5, jetons_min=3), dict(ecart_chemin=-1)):
        with pytest.raises(GardeArret):
            mp.generer(mp.Parametres(d=8, **mauvais), np.random.default_rng(0))


def test_nul_echange_par_unite():
    """L'étiquette est une propriété du jeu de poids : le nul échange les paires de poids d'un bloc (erratum 1, § 2)."""
    p = mp.Parametres(d=8, n_paires=4, n_taches=3, actions_par_tache=2)
    jeu = mp.jeu_principal(mp.generer(p, np.random.default_rng(0)))
    pa = lc.paires_du_jeu(jeu)
    for g in range(5):
        y = lc.permuter_etiquettes(jeu, np.random.default_rng(g), pa)
        for u in set(jeu.unites):
            assert len({int(y[i]) for i, _ in pa if jeu.unites[i] == u}) == 1


def test_verites_scellees(tmp_path):
    v, sha = mp.charger_verites()
    assert len(v["mondes"]) == 12 and {"decalage_de_chemin", "intensite_16", "trace_forte"} <= set(v["mondes"])
    assert v["mondes"]["trace_forte"]["composantes"]["tau"] == pytest.approx(4 * math.sqrt(2))
    copie = tmp_path / mp.CHEMIN_VERITES.name
    shutil.copy(mp.CHEMIN_VERITES, copie)
    shutil.copy(str(mp.CHEMIN_VERITES) + ".sha256", str(copie) + ".sha256")
    mp.charger_verites(copie)
    copie.write_text(copie.read_text().replace('"texte": 4.0', '"texte": 9.0'))
    with pytest.raises(GardeArret, match="empreinte"):
        mp.charger_verites(copie)


@pytest.mark.parametrize("x,n", [(0, 10), (10, 10), (3, 20), (1, 1)])
def test_clopper_pearson(x, n):
    ref = binomtest(x, n).proportion_ci(confidence_level=0.95, method="exact")
    assert mp.clopper_pearson(x, n) == pytest.approx((ref.low, ref.high), abs=1e-12)
    with pytest.raises(GardeArret):
        mp.clopper_pearson(3, 2)


def test_programme_de_bout_en_bout(tmp_path):
    """Une réplique de quelques mondes : lecture, comparaison mécanique aux vérités engagées, rapport scellé ;
    même graine, mêmes lectures ; jamais d'écrasement."""
    kw = dict(tailles=[(8, 8, 3)], repliques=1, n_nul=39, n_tirages=200, seuils=SEUILS, d=32, entropie=20261122,
              mondes=["trace_forte", "interaction_contraire", "decalage_de_chemin", "fuite_de_pli"], k_externes=3)
    c1 = prog.executer(tmp_path / "a", **kw)
    r = json.loads(c1.read_text())
    assert (tmp_path / "a" / (c1.name + ".sha256")).is_file()
    t = r["tailles"]["8,8,3"]
    assert t["fuite_de_pli"]["criteres"]["fuite"]["taux_arret_garde"] == 1.0
    assert t["trace_forte"]["criteres"]["transport"]["puissance"] == 1.0
    assert t["interaction_contraire"]["criteres"]["interaction"]["puissance"] == 1.0
    dc = t["decalage_de_chemin"]["criteres"]
    assert dc["interaction_brute"]["puissance"] == 1.0 and dc["interaction"]["taux_fausse_lecture"] == 0.0
    c2 = prog.executer(tmp_path / "b", **kw)
    assert json.dumps(r["tailles"], sort_keys=True) == json.dumps(json.loads(c2.read_text())["tailles"], sort_keys=True)
    with pytest.raises(GardeArret, match="R12"):
        prog.executer(tmp_path / "a", **kw)
    with pytest.raises(GardeArret, match="non engagés"):
        prog.executer(tmp_path / "c", **{**kw, "mondes": ["monde_inventé"]})


def test_ligne_de_commande(tmp_path, capsys):
    assert prog.main(["--sortie", str(tmp_path), "--taille", "8,8,3", "--repliques", "1", "--nul", "9",
                      "--tirages", "50", "--d", "16", "--entropie", "3", "--k-externes", "2",
                      "--mondes", "fuite_de_pli,etiquettes_permutees"]) == 0
    assert capsys.readouterr().out.strip().endswith(".json")
    with pytest.raises(GardeArret):
        prog._taille("5,5")


@pytest.mark.skipif(os.environ.get("SONDES_V2_LENT") != "1", reason="essai lent : SONDES_V2_LENT=1")
def test_lent_dimension_4096(tmp_path):
    c = prog.executer(tmp_path, tailles=[(8, 8, 3)], repliques=1, n_nul=19, n_tirages=200, seuils=SEUILS, d=4096,
                      entropie=4096, mondes=["trace_forte", "identite_seule"], k_externes=3)
    t = json.loads(c.read_text())["tailles"]["8,8,3"]
    assert t["identite_seule"]["criteres"]["identite"]["puissance"] == 1.0
    assert t["trace_forte"]["criteres"]["transport"]["puissance"] == 1.0
