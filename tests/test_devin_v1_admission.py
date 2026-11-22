"""Essais de la pièce 9 — admission : orchestration sur monde planté, témoins, verdict."""
import numpy as np
import pytest

from controle_ia.devin_v1 import RefusDevin, admission
from controle_ia.devin_v1.admission import (CHAMPS_VERDICT, ConfigurationCourse, InventaireSimule, admettre,
                                            jouer_course, plan_quatre_courses, probabilite_rejet_a_tort,
                                            valider_verdict)
from controle_ia.devin_v1.graines import generateur_tache
from controle_ia.devin_v1.monde_plante import Fuite

RACINE = 0x1CE4_E5B9_BF58_476D_94D0_49BB_1331_11EB
TEMOIN = Fuite("horodatage", 1.5, "temoin")
OPTIONS = {"etage1": {"bits_mots": 11, "bits_car": 10}, "etage2bis": {"bits_mots": 7, "max_iter": 20}}


def cfg(**k):
    base = dict(devin="piece", temoin_fuite=TEMOIN, n_apprentissage=200, n_epreuve=200, B=199, etages=("0",))
    base.update(k)
    return ConfigurationCourse(**base)


def test_cas_sain_verdict_rendu_avec_tous_ses_champs():
    r = admettre(cfg(etages=("0", "1", "2bis"), options_predicteurs=OPTIONS), [], InventaireSimule(), RACINE)
    v = r["verdict"]
    assert r["epreuve"].startswith("valable")
    assert all(c in v and v[c] is not None for c in CHAMPS_VERDICT)
    assert v["temoin_fuite_p"] <= 0.05 and v["J"] == len(v["liste_famille"]) == 12
    assert len(v["empreinte_harnais"]) == 64 and v["exactitude"] == "rejeu du tireur de la pièce"
    if not v["rejet"]:
        assert v["formule"].startswith("non réfuté jusqu'à l'étage 2bis, budget n = 200, taille détectable δ =")
        assert v["garanties_suspendues"] == []
    assert v["epreuve_a_part"] == "aucun champ élargi sans preuve"


def test_artefact_fuite_plantee_retrouvee_et_garanties_suspendues():
    v = jouer_course(cfg(), [Fuite("ordre", 0.6)], InventaireSimule(), RACINE)
    assert v["rejet"] and v["formule"].startswith("secret réfuté à l'empreinte du harnais")
    assert "estimations pondérées par l'inverse de la propension" in v["garanties_suspendues"]
    assert v["borne_basse"]["borne_basse_vt"] > 0


def test_lecture_canal_ouvert_rejette_canal_ferme_non():
    temoins = tuple(generateur_tache(RACINE, "temoins").normal(size=500))
    c = cfg(devin="lecture", lectures_temoins=temoins, etages=("0", "1"), options_predicteurs=OPTIONS)
    ouvert = jouer_course(c, [Fuite("canal_lecture", 1.0, "lecture")], InventaireSimule(), RACINE)
    assert ouvert["rejet"] and "lecture substituée" in ouvert["exactitude"]
    assert "« le défenseur joue en dernier »" in ouvert["garanties_suspendues"]


def test_vue_elargie_sans_preuve_epreuve_a_part():
    v = jouer_course(cfg(), [Fuite("horodatage", 1.5)], InventaireSimule(outils=()), RACINE)
    ep = v["epreuve_a_part"]
    assert ep["dans_M"] is False and ep["rejet"]
    assert ep["lecture"].startswith("canal sans preuve de visibilité")
    assert not any("latence" in l for l in v["liste_famille"])


def test_cible_a2_double_la_famille():
    v = jouer_course(cfg(cibles=("A1", "A2")), [], InventaireSimule(k_a2=2), RACINE)
    assert v["J"] == 2 * 10 and len(v["empreinte_famille"]) == 2


def test_sans_objet():
    v = jouer_course(cfg(), [], InventaireSimule(tirage_de_piece=False), RACINE)
    assert v["sans_objet"] and v["formule"].startswith("sans objet à l'empreinte du harnais")
    assert "non réfuté" not in v["formule"] and "couplage" in v["garde"]
    v = jouer_course(cfg(devin="lecture"), [], InventaireSimule(decision_lit_sonde=False), RACINE)
    assert v["sans_objet"]


def test_test_de_mort_4_rejoue_une_fois_puis_sans_valeur(monkeypatch):
    appels = []

    def faux(c, f, i, r, suffixe, source=None):
        appels.append(suffixe)
        return {"sans_objet": False, "declenchement_mort_4": True}

    monkeypatch.setattr(admission, "jouer_course", faux)
    r = admettre(cfg(), [], InventaireSimule(), RACINE)
    assert appels == [":pli1", ":pli2"] and r["verdict"] is None and r["epreuve"].startswith("sans valeur")


def test_temoin_de_fuite_non_retrouve_declenche():
    v = jouer_course(cfg(temoin_fuite=Fuite("verdict", 0.0, "temoin")), [], InventaireSimule(), RACINE)
    assert v["declenchement_mort_4"] == (v["temoin_fuite_p"] > 0.05 or v["temoin_factice_p"] <= 0.001)


def test_aucun_repli_champ_manquant_et_temoin_absent():
    v = jouer_course(cfg(), [], InventaireSimule(), RACINE)
    incomplet = dict(v)
    del incomplet["temoin_factice_p"]
    with pytest.raises(RefusDevin, match="champs manquants"):
        valider_verdict(incomplet)
    with pytest.raises(RefusDevin, match="témoins"):
        jouer_course(cfg(temoin_fuite=None), [], InventaireSimule(), RACINE)
    with pytest.raises(RefusDevin):
        jouer_course(cfg(), [Fuite("verdict", 0.1, "temoin")], InventaireSimule(), RACINE)


def test_plan_des_quatre_courses():
    p = plan_quatre_courses(cfg(), 0.05, (0.0, 1.0, -1.0))
    assert [c.devin for c in p] == ["piece", "piece", "lecture", "lecture"]
    assert p[1].propension == 0.05 and p[3].mode_lecture == "service"
    assert probabilite_rejet_a_tort() == pytest.approx(0.1855, abs=1e-4)
