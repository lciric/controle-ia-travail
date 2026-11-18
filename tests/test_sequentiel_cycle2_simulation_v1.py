"""Lanceur et critères d'admission : cas sains et artefacts (R5), graines et manifeste (R9)."""
import json

import pytest

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller, verifier
from controle_ia.sequentiel_cycle2 import criteres_v1 as criteres
from controle_ia.sequentiel_cycle2 import simulation_v1 as simulation

GAUSSIEN = {"n_taches": 400, "n_intermediaire": 200, "pas_tranche": 50,
            "erreur_type_64": {"d_somme": 0.038, "ecart": 0.038, "d_maximum": 0.038},
            "effets": {"d_somme": [0.0, 0.0], "ecart": [0.5, 0.5], "d_maximum": [0.0, 0.0]},
            "correlation_doses": 0.0, "correlation_grandeurs": 0.0, "marge": 0.05, "part_intermediaire": 0.2,
            "n_repliques": 200000}
SCORES = {"verite": "dense", "n_taches": 60, "n_intermediaire": 30, "n_directions": 20,
          "amplitude": {"cible": 0.02, "facteur": 1.0}, "amplitude_directions": 0.0, "actions_decalees": 10,
          "part_tache": 0.3, "part_commune": 0.2, "marge": 0.05, "part_intermediaire": 0.2,
          "tirages_intermediaire": 8000, "tirages_finale": 2000}


def ecrire_config(depot, mondes, sceller_la=True):
    chemin = depot / "configuration.json"
    chemin.write_text(json.dumps({"mondes": mondes}), encoding="utf-8")
    if sceller_la:
        sceller(chemin)
    committer(depot)
    return chemin


def mondes_de_base():
    return [{"nom": "g-frontiere", "genre": "gaussien", "config": GAUSSIEN,
             "criteres": [{"genre": "risque", "etats": ["accumuler_propre", "partage"], "plafond": 0.0125},
                          {"genre": "temoin", "etats": ["accumuler_propre", "partage"]}]},
            {"nom": "s-dense", "genre": "scores", "config": SCORES, "n_repliques": 2,
             "criteres": [{"genre": "puissance", "etats": ["AP"], "perte_permise": 0.05}]}]


def test_bornes_exactes():
    assert criteres.borne_haute(0, 100) == pytest.approx(1 - 0.05 ** (1 / 100))
    assert criteres.borne_basse(0, 100) == 0.0 and criteres.borne_haute(100, 100) == 1.0
    assert criteres.borne_basse(5, 100) < 0.05 < criteres.borne_haute(5, 100)
    with pytest.raises(GardeArret):
        criteres.borne_haute(3, 2)


def test_prononces_a_l_une_des_deux_lectures():
    couples = {"non_concluant>non_concluant": 90, "accumuler_propre>partage": 2, "non_concluant>accumuler_propre": 5,
               "propre_sans_gain>propre_sans_gain": 3}
    assert criteres.prononces(couples, ["accumuler_propre"]) == 7
    assert criteres.prononces(couples, ["accumuler_propre", "partage"]) == 7
    assert criteres.prononces(couples, ["maximum_bat"]) == 0


def test_juger_cas_sain_artefact_et_comptes_incomplets():
    def comptes(juge, unique, naif, n=1000):
        return {p: {"couple": {"Z>AP": k, "Z>Z": n - k}} for p, k in (("reparti", juge), ("unique", unique), ("naif", naif))}
    risque = {"genre": "risque", "etats": ["AP"], "plafond": 0.00625}
    assert criteres.juger(risque, comptes(1, 2, 4), 1000)["tenu"] is True
    assert criteres.juger(risque, comptes(12, 2, 4), 1000)["tenu"] is False           # artefact : risque gonflé
    temoin = {"genre": "temoin", "etats": ["AP"]}
    assert criteres.juger(temoin, comptes(3, 3, 30), 1000)["tenu"] is True
    assert criteres.juger(temoin, comptes(3, 3, 4), 1000)["tenu"] is False            # simulation aveugle au plan naïf
    puissance = {"genre": "puissance", "etats": ["AP"], "perte_permise": 0.05}
    assert criteres.juger(puissance, comptes(780, 800, 800), 1000)["tenu"] is True
    assert criteres.juger(puissance, comptes(700, 800, 800), 1000)["tenu"] is False
    with pytest.raises(GardeArret):
        criteres.juger(risque, comptes(1, 2, 4), 999)
    with pytest.raises(GardeArret):
        criteres.juger({"genre": "autre", "etats": ["AP"]}, comptes(1, 2, 4), 1000)


def test_lancement_complet_reduit_ecrit_scelle_et_rejoue(depot):
    config = ecrire_config(depot, mondes_de_base())
    ecrits = simulation.lancer(depot, config, "20261118-220000-essai-un", entropie=12345)
    assert [p.name for p in ecrits] == ["simulation-g-frontiere.json", "simulation-s-dense.json"]
    for p in ecrits:
        verifier(p)
    g = json.loads(ecrits[0].read_text())["resultat"]
    assert [k["tenu"] for k in g["criteres"]] == [True, True]      # borne d'union tenue ; plan naïf vu au-dessus
    s = json.loads(ecrits[1].read_text())["resultat"]
    assert s["repliques"] == 2 and s["amplitude_reglee"] > 0
    committer(depot)
    encore = simulation.lancer(depot, config, "20261118-220001-essai-deux", entropie=12345)
    assert json.loads(encore[0].read_text())["resultat"]["comptes"] == g["comptes"]            # même entropie (R9)
    committer(depot)
    with pytest.raises(GardeArret):                                 # un run existant n'est jamais écrasé
        simulation.lancer(depot, config, "20261118-220000-essai-un", entropie=12345)


def test_essai_a_blanc_n_ecrit_que_des_durees(depot):
    config = ecrire_config(depot, mondes_de_base())
    ecrits = simulation.lancer(depot, config, "20261118-220002-a-blanc", mondes=["s-dense"], essai_a_blanc=True)
    assert [p.name for p in ecrits] == ["essai-a-blanc-s-dense.json"]
    contenu = json.loads(ecrits[0].read_text())["resultat"]
    assert set(contenu) == {"essai_a_blanc", "monde", "repliques_jouees", "secondes"}


def test_gardes_du_lancement(depot):
    non_scellee = ecrire_config(depot, mondes_de_base(), sceller_la=False)
    with pytest.raises(GardeArret):
        simulation.lancer(depot, non_scellee, "20261118-220003-refus")
    for defaut in ([], [dict(mondes_de_base()[0], criteres=[])], mondes_de_base()[:1] * 2,
                   [dict(mondes_de_base()[1], n_repliques=0)], [dict(mondes_de_base()[0], genre="autre")]):
        chemin = depot / f"config-{len(str(defaut))}.json"
        chemin.write_text(json.dumps({"mondes": defaut}), encoding="utf-8")
        sceller(chemin)
        committer(depot)
        with pytest.raises(GardeArret):
            simulation.lancer(depot, chemin, "20261118-220004-refus")
    config = depot / "configuration-b.json"
    config.write_text(json.dumps({"mondes": mondes_de_base()}), encoding="utf-8")
    sceller(config)
    committer(depot)
    with pytest.raises(GardeArret):
        simulation.lancer(depot, config, "20261118-220005-refus", mondes=["absent"])


def test_monde_du_croisement_regle_et_joue(depot, monkeypatch):
    monkeypatch.setattr(simulation, "REGLAGE_CROISEMENT", {"n_episodes": 50000})
    monde = {"nom": "s-croisement", "genre": "scores", "n_repliques": 1,
             "config": dict(SCORES, verite="concentre", actions_decalees=2, amplitude={"croisement": True}),
             "criteres": [{"genre": "risque", "etats": ["AP"], "plafond": 1.0}]}
    config = ecrire_config(depot, [monde])
    ecrit = simulation.lancer(depot, config, "20261118-220006-croisement", entropie=5)
    resultat = json.loads(ecrit[0].read_text())["resultat"]
    assert 0.05 < resultat["amplitude_reglee"] < 6.0 and resultat["criteres"][0]["tenu"] is True
