"""Section de configuration de la distillation et de l'évaluation, v5 (conception d'origine 5.1, 5.3, 6 ; texte scellé, section 16)."""
import copy

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.iib import configuration_distillation_v5 as cd
from controle_ia.iib import configuration_v1 as c1
from controle_ia.iib import configuration_v5 as cf


def _remplie(lecture="gardee"):
    s = cd.gabarit_section()
    s["perte"]["premiere_action"] = lecture
    return s


def test_constantes_egales_a_celles_de_la_conception_d_origine():
    """Le texte scellé ne liste aucun écart pour l'adaptateur, la distillation ni les doses : ce sont celles de la version 1."""
    for k in ("adaptateur", "distillation", "doses"):
        assert cd.TEXTE_DISTILLATION[k] == c1.TEXTE[k], k
    assert cd.CONDITIONS == c1.CONDITIONS_EVALUATION and list(cd.CONDITIONS) == cd.TEXTE_DISTILLATION["evaluation"]["conditions"]
    assert cd.TEXTE_DISTILLATION["evaluation"]["taches"] == 64 and cd.ADAPTATEURS == ("eleve", "temoin-jumeau")
    assert cd.TEXTE_DISTILLATION["evaluation"]["adaptateur_de"] == {"H": "eleve", "B50": "eleve", "B100": "eleve", "TJ100": "temoin-jumeau"}


def test_gabarit_valide_mais_refuse_au_lancement_tant_que_la_premiere_action_n_est_pas_tranchee():
    s = cd.gabarit_section()
    assert s["perte"]["premiere_action"] is None and cd.exiger_section(s, "reel") == {"premiere_action": None}       # cas sain
    with pytest.raises(GardeArret, match="premiere_action non remplie"):                                            # artefact
        cd.exiger_section(s, "reel", pour_lancer=True)
    for lecture in cd.LECTURES_PREMIERE_ACTION:
        assert cd.exiger_section(_remplie(lecture), "reel", pour_lancer=True) == {"premiere_action": lecture}
    with pytest.raises(GardeArret, match="premiere_action"):
        cd.exiger_section(_remplie("au choix"), "reel", pour_lancer=True)


@pytest.mark.parametrize("chemin, valeur", [
    (("adaptateur", "rang"), 8), (("adaptateur", "alpha"), 16.0), (("adaptateur", "cibles"), ["q_proj", "v_proj"]),
    (("adaptateur", "precision"), "bfloat16"), (("adaptateur", "sauvegarde"), "float32"), (("distillation", "mode"), "paires"),
    (("distillation", "epoques"), 4), (("distillation", "lot"), 2), (("distillation", "pas"), 0.001), (("distillation", "norme_max"), 2.0),
    (("doses", "H"), 0.1), (("doses", "B50"), 0.4), (("doses", "B100"), 0.9), (("doses", "TJ100"), 0.5),
    (("evaluation", "conditions"), ["H", "B100", "B50", "TJ100"]), (("evaluation", "taches"), 32),
    (("evaluation", "adaptateur_de"), {"H": "eleve", "B50": "eleve", "B100": "eleve", "TJ100": "eleve"}),
    (("perte", "mentions"), "gardees"), (("perte", "non_bornables_a_cout"), "gardees"), (("surveillance", "empreinte_tous_les_appels"), 1000)])
def test_une_constante_changee_est_un_refus_en_mode_reel(chemin, valeur):
    s = _remplie()
    assert cd.exiger_section(s, "reel", pour_lancer=True)                       # cas sain
    s[chemin[0]][chemin[1]] = valeur
    with pytest.raises(GardeArret):
        cd.exiger_section(s, "reel", pour_lancer=True)


def test_cle_de_plus_ou_de_moins_refusee():
    s = _remplie()
    with pytest.raises(GardeArret, match="clés"):
        cd.exiger_section({**s, "scores_moniteur": {}}, "reel")
    with pytest.raises(GardeArret, match="clés"):
        cd.exiger_section({k: v for k, v in s.items() if k != "doses"}, "reel")
    s["adaptateur"]["dropout"] = 0.1
    with pytest.raises(GardeArret, match="clés"):
        cd.exiger_section(s, "reel")
    with pytest.raises(GardeArret, match="mode"):
        cd.exiger_section(_remplie(), "essai")


def test_mode_jouet_seules_les_tailles_sont_reductibles():
    s = _remplie()
    s["adaptateur"]["rang"], s["distillation"]["epoques"], s["evaluation"]["taches"] = 2, 1, 8
    assert cd.exiger_section(s, "jouet", pour_lancer=True)                      # cas sain : tailles réduites
    with pytest.raises(GardeArret):                                             # les mêmes tailles en mode réel : refus
        cd.exiger_section(s, "reel", pour_lancer=True)
    for chemin, valeur in ((("doses", "B50"), 0.25), (("distillation", "pas"), 0.01), (("evaluation", "conditions"), ["H", "B100"])):
        t = copy.deepcopy(s)
        t[chemin[0]][chemin[1]] = valeur
        with pytest.raises(GardeArret):                                         # artefact : une dose, un pas, une condition changés
            cd.exiger_section(t, "jouet", pour_lancer=True)
    s["adaptateur"]["rang"] = 0
    with pytest.raises(GardeArret, match="strictement positif"):
        cd.exiger_section(s, "jouet")


def test_plan_d_evaluation_et_conditions():
    s = _remplie()
    assert cd.plan_d_evaluation(s) == [{"condition": "H", "adaptateur": "eleve", "dose": 0.0}, {"condition": "B50", "adaptateur": "eleve", "dose": 0.5},
                                       {"condition": "B100", "adaptateur": "eleve", "dose": 1.0},
                                       {"condition": "TJ100", "adaptateur": "temoin-jumeau", "dose": 1.0}]
    assert cd.condition_de(s, "TJ100")["adaptateur"] == "temoin-jumeau"
    with pytest.raises(GardeArret, match="inconnue"):
        cd.condition_de(s, "B25")
    with pytest.raises(GardeArret, match="adaptateur"):
        cd.cle_de_l_adaptateur("maitre")
    assert cd.cle_de_l_adaptateur("eleve") == "iib/adaptateur/eleve" and cd.cle_de_la_distillation("temoin-jumeau") == "iib/distillation/temoin-jumeau"
    assert cd.CLE_INJECTION == "iib/injection"                                  # clés de la conception d'origine, section 9


def test_section_absente_refusee_et_aucun_texte_de_consigne():
    with pytest.raises(GardeArret, match="absente"):
        cd.section_de({"mode": "reel"})
    config = {"mode": "reel", cd.SECTION: _remplie()}
    assert cd.section_de(config, pour_lancer=True) is config[cd.SECTION]
    cf.exiger_aucun_texte_de_consigne(config)                                   # aucune clé ne nomme un texte de consigne
