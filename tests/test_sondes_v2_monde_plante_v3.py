"""Essais de la brique D v3 (épreuve à vérité plantée ; errata 1 et 2 ; texte scellé des diagnostics préalables) :
générateur, vérités et critères engagés, passage par borne exacte, programme dans ses deux modes. L'essai lent
(dimension 4 096) ne tourne que si SONDES_V2_LENT=1."""
import json
import math
import os
import shutil

import numpy as np
import pytest
from scipy.stats import binomtest

from controle_ia.gardes import GardeArret
from controle_ia.sondes_v2 import lecture_v1 as lc
from controle_ia.sondes_v2 import monde_plante_v3 as mp
from controle_ia.sondes_v2 import programme_monde_plante_v3 as prog

SEUILS = {"alpha": 0.05, "u_fort": 0.9}


def test_generateur_structure_et_ecart_symetrique():
    p = mp.Parametres(d=64, n_paires=3, n_familles=2, n_taches=2, actions_par_tache=2, bruit_lecture=0.0, tau=2.0,
                      eta=1.0, sigma_I=0.0, identite_isotrope=0.0)
    m = mp.generer(p, np.random.default_rng(0))
    assert set(m["familles"]) == {0, 1} and m["familles"][1][2] == ("S1_2", "J1_2")
    assert len(m["lectures"]) == 1 + 2 * 3 * 2
    c = next(c for c, (_, so) in m["textes"].items() if so == "honnete")
    n = m["lectures"]["N"][c][0]
    # identité nulle : J = −η/2 g, S = +η/2 g + trace ; l'écart est réparti des deux côtés (erratum 2, § 4)
    dj = m["lectures"]["J0_0"][c][0] - n
    ds = m["lectures"]["S0_0"][c][0] - n
    assert np.linalg.norm(dj) == pytest.approx(0.5, rel=1e-9)
    t = ds + dj  # = trace
    assert np.linalg.norm(t) == pytest.approx(2.0, rel=1e-9)
    assert np.linalg.norm(m["lectures"]["S1_0"][c][0] + m["lectures"]["J1_0"][c][0] - 2 * n - t) < 1e-9  # trace commune


def test_intensite_et_sources():
    p = mp.Parametres(d=32, n_paires=2, n_taches=2, actions_par_tache=1, bruit_lecture=0.0, eta=0.0, intensite=1.0,
                      identite_isotrope=0.0, sigma_I=1.0, sources=("honnete",))
    m = mp.generer(p, np.random.default_rng(1))
    assert all(so == "honnete" for _, so in m["textes"].values())
    c = next(iter(m["textes"]))
    ds = m["lectures"]["S0_0"][c][0] - m["lectures"]["J0_0"][c][0]
    assert np.linalg.norm(ds) == pytest.approx(0.2 * math.sqrt(2), rel=1e-9)
    for mauvais in (dict(n_paires=1), dict(n_familles=0), dict(sources=("saboteur",)), dict(tau=-1.0)):
        with pytest.raises(GardeArret):
            mp.generer(mp.Parametres(d=8, **mauvais), np.random.default_rng(0))


def test_nul_echange_par_unite():
    jeu = mp.jeu_principal(mp.generer(mp.Parametres(d=8, n_paires=4, n_taches=3, actions_par_tache=2),
                                      np.random.default_rng(0)))
    pa = lc.paires_du_jeu(jeu)
    for g in range(5):
        y = lc.permuter_etiquettes(jeu, np.random.default_rng(g), pa)
        for u in set(jeu.unites):
            assert len({int(y[i]) for i, _ in pa if jeu.unites[i] == u}) == 1


def test_verites_v3_scellees(tmp_path):
    v, _ = mp.charger_verites()
    assert len(v["mondes"]) == 12 and v["grille_etalon"]["paires"] == list(range(4, 17))
    crit = {(m, c["lecture"]): c for m, d in v["mondes"].items() for c in d["criteres"]}
    assert crit[("identite_seule", "identite")]["borne"] == "basse" and crit[("identite_seule", "identite")]["seuil"] == 0.8
    assert crit[("decalage_de_chemin", "decalage_maitrise")]["seuil"] == 0.9
    copie = tmp_path / mp.CHEMIN_VERITES.name
    shutil.copy(mp.CHEMIN_VERITES, copie)
    shutil.copy(str(mp.CHEMIN_VERITES) + ".sha256", str(copie) + ".sha256")
    mp.charger_verites(copie)
    copie.write_text(copie.read_text().replace('"seuil": 0.8', '"seuil": 0.5'))
    with pytest.raises(GardeArret, match="empreinte"):
        mp.charger_verites(copie)


@pytest.mark.parametrize("x,n", [(0, 10), (10, 10), (3, 20), (1, 1), (480, 500)])
def test_clopper_pearson(x, n):
    ref = binomtest(x, n).proportion_ci(confidence_level=0.95, method="exact")
    assert mp.clopper_pearson(x, n) == pytest.approx((ref.low, ref.high), abs=1e-12)


def test_compter_et_passage():
    k = {"lecture": "transport", "admises": ["fort", "faible"], "nature": "fausse_lecture", "borne": "haute",
         "seuil": 0.10}
    lect = [{"transport": ["fort" + " — non distinct d'une direction au hasard", "non établi à cette puissance"]},
            {"transport": ["non testable à cet effectif"]}]
    assert mp.compter(lect, k) == (1, 3)
    assert mp.passage(10, 500, k)["passe"] is True
    assert mp.passage(60, 500, k)["passe"] is False
    kb = dict(k, borne="basse", seuil=0.8, nature="puissance")
    assert mp.passage(430, 500, kb)["passe"] is True and mp.passage(400, 500, kb)["passe"] is False
    assert "passe" not in mp.passage(1, 2, dict(k, borne=None, seuil=None))
    with pytest.raises(GardeArret):
        mp.compter([{}], k)


def test_programme_complet(tmp_path):
    kw = dict(mode="complet", cas=[(8, 8, 3)], repliques=1, n_nul=39, n_tirages=200, seuils=SEUILS, d=32,
              entropie=20261122, mondes=["trace_forte", "interaction_contraire", "decalage_de_chemin", "fuite_de_pli"],
              k_externes=3, n_nul_identite=19, autoriser_depot_sale=True)
    c1 = prog.executer(tmp_path / "a", **kw)
    r = json.loads(c1.read_text())["cases"]["8,8,3"]
    crit = {(m, k["lecture"]): k for m, v in r.items() for k in v["criteres"]}
    assert crit[("fuite_de_pli", "fuite")]["part_admise"] == 1.0
    assert crit[("trace_forte", "transport")]["part_admise"] == 1.0
    assert crit[("interaction_contraire", "interaction")]["part_admise"] == 1.0
    assert crit[("decalage_de_chemin", "interaction_brute")]["part_admise"] == 1.0
    assert crit[("decalage_de_chemin", "decalage_maitrise")]["part_admise"] == 1.0
    assert crit[("decalage_de_chemin", "decalage_maitrise")]["passe"] is False  # une réplique : borne basse trop basse
    c2 = prog.executer(tmp_path / "b", **kw)
    assert json.loads(c1.read_text())["cases"] == json.loads(c2.read_text())["cases"]
    with pytest.raises(GardeArret, match="R12"):
        prog.executer(tmp_path / "a", **kw)
    with pytest.raises(GardeArret, match="non engagé"):
        prog.executer(tmp_path / "c", **{**kw, "mondes": ["intensite_4"]})  # monde du seul mode « étalon »


def test_programme_etalon_grille(tmp_path):
    c = prog.executer(tmp_path, "etalon", [(7, 1, 8, 2), (4, 2, 8, 1)], 2, 9, 100, SEUILS, 16, 5,
                      mondes=["trace_forte", "identite_seule", "etiquettes_permutees"], n_nul_identite=9,
                      autoriser_depot_sale=True)
    man = json.loads(c.read_text())["manifeste"]
    assert len(man["commit"]) == 40 and man["config"]["cas"] == [[7, 1, 8, 2], [4, 2, 8, 1]]  # défaut 1 (R9)
    assert man["config"]["nul_identite"] == 9 and "depot_propre" in man
    r = json.loads(c.read_text())["cases"]
    tf = {k["lecture"]: k for k in r["7,1,8,2"]["trace_forte"]["criteres"]}
    assert tf["transport"]["part_admise"] == 1.0 and tf["transport"]["essais"] == 2
    tf4 = r["4,2,8,1"]["trace_forte"]["table_des_lectures"]["transport"]
    assert tf4 == {"non testable à cet effectif": 4}  # quatre paires : jamais testable
    assert {k["lecture"] for k in r["7,1,8,2"]["identite_seule"]["criteres"]} == {"transport", "identite"}


def test_ligne_de_commande(tmp_path, capsys):
    assert prog.main(["--sortie", str(tmp_path), "--cas", "7,1,8,1", "--repliques", "1", "--nul", "5",
                      "--tirages", "20", "--d", "16", "--entropie", "3", "--mondes", "trace_faible",
                      "--nul-identite", "5", "--autoriser-depot-sale"]) == 0
    assert capsys.readouterr().out.strip().endswith(".json")
    with pytest.raises(GardeArret):
        prog._entiers("5,5", 3)


@pytest.mark.skipif(os.environ.get("SONDES_V2_LENT") != "1", reason="essai lent : SONDES_V2_LENT=1")
def test_lent_dimension_4096(tmp_path):
    c = prog.executer(tmp_path, "etalon", [(8, 1, 8, 3)], 1, 19, 200, SEUILS, 4096, 4096,
                      mondes=["trace_forte", "identite_seule"], n_nul_identite=19, autoriser_depot_sale=True)
    r = json.loads(c.read_text())["cases"]["8,1,8,3"]
    assert {k["lecture"]: k["part_admise"] for k in r["identite_seule"]["criteres"]}["identite"] == 1.0
    assert {k["lecture"]: k["part_admise"] for k in r["trace_forte"]["criteres"]}["transport"] == 1.0


def test_depot_sale_refuse_et_critere_manquant(tmp_path, monkeypatch):
    """Défaut 1 : arbre sale refusé sans autorisation ; défaut 4 : un critère engagé jamais lu arrête."""
    monkeypatch.setattr(prog, "etat_git", lambda racine: {"commit": "0" * 40, "propre": False, "statut": "?? x"})
    with pytest.raises(GardeArret, match="non propre"):
        prog.executer(tmp_path / "a", "etalon", [(7, 1, 8, 1)], 1, 3, 10, SEUILS, 8, 1, mondes=["trace_forte"])
    monkeypatch.setattr(prog.mp, "lire_etalon", lambda *a, **k: {"transport_controle": ["fort"]})
    with pytest.raises(GardeArret, match="jamais lu"):
        prog.executer(tmp_path / "b", "etalon", [(7, 1, 8, 1)], 1, 3, 10, SEUILS, 8, 1, mondes=["trace_forte"],
                      autoriser_depot_sale=True)
