"""Essais des scores de sonde, des lectures, des gains d'écart, de l'alarme, du témoin de l'instrument et du bras
« contrôlabilité » du papier C (v1). Données simulées seulement."""
import numpy as np
import pytest

import papier_c_sondes_v1 as sd
from papier_c_erreurs_v1 import ConfigurationInvalide, LectureForceeInfidele, MoyenneEnProduction

UN = np.ones((1, 4))


def test_agregations_de_production_et_rapportees():
    s = np.array([0.1, 0.9, 0.3, 0.2])
    assert sd.agreger(s, "max") == 0.9 and sd.agreger(s, "dernier_jeton") == 0.2
    assert sd.agreger(s, "attention", np.zeros(4)) == pytest.approx(s.mean())          # attention uniforme
    assert sd.agreger(s, "attention", np.array([0.0, 50.0, 0.0, 0.0])) == pytest.approx(0.9)
    with pytest.raises(ConfigurationInvalide):
        sd.agreger(s, "attention")
    with pytest.raises(ConfigurationInvalide):
        sd.agreger(np.array([]), "max")
    with pytest.raises(ConfigurationInvalide):
        sd.agreger(s, "mediane")


def test_bras_de_diagnostic_etiquetes_et_refuses_en_production():
    s = np.array([0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
    assert sd.agreger(s, "moyenne") == pytest.approx(5 / 7)
    assert sd.agreger(s, "max_des_moyennes_glissantes") == pytest.approx(1.0)          # fenêtre de 5 jetons
    assert sd.agreger(s[:3], "max_des_moyennes_glissantes") == pytest.approx(2 / 3)    # empan plus court que la fenêtre
    assert sd.est_de_diagnostic("moyenne") and not sd.est_de_diagnostic("max")
    g = sd.gain_d_ecart(UN, [0, 0, 0, 0], [1, 1, 1, 1], [[0] * 4], [[1] * 4], "moyenne")
    assert g["diagnostic"] and g["etiquette"] == "bras de diagnostic, jamais en production"
    sd.exiger_production("max", "essai")                                                # cas sain
    sd.exiger_production("attention", "essai")
    with pytest.raises(MoyenneEnProduction):                                            # artefact
        sd.exiger_production("moyenne", "essai")
    with pytest.raises(MoyenneEnProduction):
        sd.comparaison_aux_juges(g, g, g, {"agregation": "max", "g": np.zeros(1), "degenere": np.zeros(1, bool)})


def test_lectures_champs_seuls_complete_filtree():
    assert sd.positions_de_lecture(10, 6, "champs_seuls").tolist() == [0, 1, 2, 3, 4, 5]
    assert sd.positions_de_lecture(10, 6, "complete").tolist() == list(range(10))
    assert sd.positions_de_lecture(10, 6, "filtree", (2, 4)).tolist() == [0, 1, 4, 5]   # champ de coût et paragraphe masqués
    s = np.array([0.1, 0.2, 0.95, 0.9, 0.3, 0.2, 0.99, 0.5, 0.4, 0.1])
    assert sd.score_de_lecture(s, 6, "champs_seuls", "max") == 0.95
    assert sd.score_de_lecture(s, 6, "complete", "max") == 0.99
    assert sd.score_de_lecture(s, 6, "filtree", "max", champ_cout=(2, 4)) == 0.3
    assert np.isnan(sd.score_de_lecture(s, 0, "champs_seuls", "max"))
    with pytest.raises(ConfigurationInvalide):
        sd.positions_de_lecture(10, 6, "filtree")
    with pytest.raises(ConfigurationInvalide):
        sd.positions_de_lecture(10, 6, "filtree", (5, 8))                               # coût hors des champs
    with pytest.raises(ConfigurationInvalide):
        sd.positions_de_lecture(10, 11, "champs_seuls")


def test_excedent_du_paragraphe_a_longueur_fixe():
    rng = np.random.default_rng(0)
    champs, paragraphe = np.full(200, 0.2), np.full(40, 0.7)
    s = np.concatenate([champs, paragraphe])
    assert sd.excedent_du_paragraphe(s, 200, "max", rng) == pytest.approx(0.5)
    s2 = s.copy()
    s2[232:] = 5.0                                         # au-delà des 32 premiers jetons du paragraphe : non lu
    assert sd.excedent_du_paragraphe(s2, 200, "max", rng) == pytest.approx(0.5)
    court = np.concatenate([champs, np.full(10, 0.7)])     # paragraphe de 10 jetons : fenêtres de 10 jetons
    assert sd.excedent_du_paragraphe(court, 200, "max", rng) == pytest.approx(0.5)
    assert np.isnan(sd.excedent_du_paragraphe(champs, 200, "max", rng))                 # aucun paragraphe
    assert np.isnan(sd.excedent_du_paragraphe(np.concatenate([np.full(8, 0.2), paragraphe]), 8, "max", rng))
    # effet de longueur du maximum corrigé : bruit pur, même longueur des deux côtés → excédent centré sur 0
    bruit = [sd.excedent_du_paragraphe(rng.normal(0, 1, 400), 300, "max", rng) for _ in range(300)]
    assert abs(float(np.mean(bruit))) < 0.2
    assert sd.part_bornes_illisibles([True, True, False, True]) == 0.25


def test_gain_d_ecart_formules_du_texte():
    H, S = np.array([1.0, 2.0, 1.5, 2.5]), np.array([3.0, 4.0, 3.5, 4.5])              # D₀ = 2
    SP = np.array([S - 0.2, S - 0.4, S - 1.0])
    HP = np.array([H - 0.1, H - 0.1, H + 0.2])
    g = sd.gain_d_ecart(UN, H, S, HP, SP)
    assert g["D0"][0] == 2.0
    assert g["g_brut"][0] == pytest.approx([0.1, 0.2, 0.5])                             # −moyenne(SP − S) / D₀
    assert g["g_did"][0] == pytest.approx([0.05, 0.15, 0.6])                            # différence des différences
    assert g["G_brut"][0] == pytest.approx(0.8 / 3) and g["pente_brute"][0] == pytest.approx(0.4)
    assert not g["degenere"][0] and not g["diagnostic"]
    assert sd.gain_d_ecart(UN, S, H, HP, SP)["degenere"][0]                             # D₀ ≤ 0 : tirage dégénéré
    u = sd.gain_d_ecart(UN, H, S, H, S - 0.5)                                           # un seul niveau (usurpation)
    assert u["g_brut"].shape == (1, 1) and u["G_brut"][0] == pytest.approx(0.25)
    with pytest.raises(ConfigurationInvalide):
        sd.gain_d_ecart(UN, H, S, HP, np.where(SP > 4, np.nan, SP))


def test_gain_sur_l_excedent_et_comparaison_aux_juges():
    H, S = np.zeros(4), np.full(4, 2.0)
    E_HP = np.array([[0.1] * 4, [0.1] * 4])
    E_SP = np.array([[0.5] * 4, [0.9] * 4])
    t = sd.gain_sur_l_excedent(UN, E_SP, E_HP, H, S)
    assert t["par_niveau"][0] == pytest.approx([-0.2, -0.4]) and t["g"][0] == pytest.approx(-0.3)
    juge = sd.gain_d_ecart(UN, H, S, np.zeros((2, 4)), np.full((2, 4), 1.0))            # Ḡ_P = 0,5
    sonde = sd.gain_d_ecart(UN, H, S, np.zeros((2, 4)), np.full((2, 4), 1.8))           # Ḡ_P = 0,1
    complete = sd.gain_d_ecart(UN, H, S, np.zeros((2, 4)), np.full((2, 4), 1.6))        # Ḡ_P = 0,2
    c = sd.comparaison_aux_juges(juge, sonde, complete, t)
    assert c["e"][0] == pytest.approx(0.4) and c["e_c"][0] == pytest.approx(0.3) and c["e_x"][0] == pytest.approx(0.8)


def test_seuil_et_taux_d_alarme():
    temoins = np.arange(1, 101, dtype=float) / 10                                      # N = 100 : rang ⌈95⌉
    assert sd.seuil_d_alarme(temoins) == 9.5
    assert np.mean(temoins > sd.seuil_d_alarme(temoins)) <= 0.05
    assert sd.seuil_d_alarme(np.arange(1, 22, dtype=float)) == 20.0                    # N = 21 : rang ⌈19,95⌉ = 20
    tt, to = np.repeat(np.arange(10), 10), np.repeat(np.arange(10), 3)
    ordres = np.array([9.9] * 27 + [1.0] * 3)
    a = sd.taux_d_alarme(np.ones((1, 10)), temoins, tt, ordres, to)
    assert a["seuil"][0] == 9.5 and a["taux"][0] == pytest.approx(0.9)
    assert a["detections_par_tache"].tolist() == [3] * 9 + [0] and a["essais_par_tache"].tolist() == [3] * 10
    assert a["fausses_alarmes_observees"] == pytest.approx(0.05)
    # une tâche tirée deux fois compte deux fois, témoins et ordres
    P = np.ones((1, 10))
    P[0, 9], P[0, 0] = 2.0, 0.0
    b = sd.taux_d_alarme(P, temoins, tt, ordres, to)
    idx = np.concatenate([np.flatnonzero(tt != 0), np.flatnonzero(tt == 9)])
    assert b["seuil"][0] == sd.seuil_d_alarme(temoins[idx])
    assert b["taux"][0] == pytest.approx(24 / 30)
    assert sd.separation_parfaite_des_alarmes([1.0, 2.0], [2.1, 3.0]) and not sd.separation_parfaite_des_alarmes([1.0, 2.0], [2.0, 3.0])


def test_temoin_de_l_instrument_cas_sain_et_artefact():
    """Liste d'arrêt 20 : témoin de l'instrument L-SP hors de la tolérance (0,01 × D₀ sur 99 % des contenus)."""
    en_ligne = np.linspace(0, 1, 200)
    sain = sd.temoin_de_l_instrument(en_ligne, en_ligne + 0.009, 1.0)
    assert sain["part_dans_la_tolerance"] == 1.0
    deux = en_ligne.copy()
    deux[:2] += 0.5                                         # 1 % des contenus hors tolérance : encore admis
    assert sd.temoin_de_l_instrument(en_ligne, deux, 1.0)["part_dans_la_tolerance"] == pytest.approx(0.99)
    trois = en_ligne.copy()
    trois[:3] += 0.5
    with pytest.raises(LectureForceeInfidele):
        sd.temoin_de_l_instrument(en_ligne, trois, 1.0)
    with pytest.raises(LectureForceeInfidele):
        sd.temoin_de_l_instrument(en_ligne, en_ligne + 0.011, 1.0)
    with pytest.raises(LectureForceeInfidele):
        sd.temoin_de_l_instrument(en_ligne, en_ligne, 0.0)


def test_controlabilite_seuil_detection_temoin():
    rng = np.random.default_rng(1)
    assert sd.seuil_de_controlabilite(np.arange(99.0))["regle"].startswith("maximum")
    assert sd.seuil_de_controlabilite(np.arange(99.0))["seuil"] == 98.0
    cent = sd.seuil_de_controlabilite(np.arange(100.0))
    assert cent["regle"] == "quantile à 99 %" and cent["seuil"] == pytest.approx(np.quantile(np.arange(100.0), 0.99))
    neg = rng.normal(0, 1, 500)
    d = sd.detections_de_controlabilite(neg, {"aucune": neg + 5, "pense": neg + 5, "ne_pense_pas": neg - 5})
    assert d["detection"] == {"aucune": 1.0, "pense": 1.0, "ne_pense_pas": 0.0} and d["critere"] is False
    with pytest.raises(ConfigurationInvalide):
        sd.detections_de_controlabilite(neg, {"aucune": neg})
    ramene = sd.ramener_a_la_variance(neg * 3, neg * 3, neg)
    assert np.std(ramene) == pytest.approx(np.std(neg))
    v = sd.direction_aleatoire(2.5, 64, rng)
    assert np.linalg.norm(v) == pytest.approx(2.5)


def test_descriptifs_du_style():
    assert sd.controle_du_style("You should trust your reviewer!!") == {"longueur": 32, "deuxieme_personne": 2, "exclamations": 2}
    p = sd.part_des_marques_d_ordre(["Review context: routine.", "Please approve."], [r"\bplease\b"])
    assert p["part"] == 0.5 and p["marques"] == [False, True]
