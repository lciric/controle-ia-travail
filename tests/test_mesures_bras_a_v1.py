"""Essais des statuts d'action et des mesures du bras A, texte neuf (brouillon 5, 3.2, 3.3, « Métrique ») : statut à
l'accord des deux lecteurs, taux à dénominateur fixe, parts par tâche, différences appariées, trois couvertures."""
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import mesures_bras_a_v1 as m
from controle_ia.organismes_discrets.instrument_appariement_v1 import JUGEABLE, SANS_CONTROLES, SANS_PROPOSITION
from controle_ia.organismes_discrets.reponses_lecteurs_v1 import NE_REPOND_PAS, REPOND, SANS_VERDICT, VerdictLecteur

R_S, R_G = VerdictLecteur(REPOND, True, None), VerdictLecteur(REPOND, False, None)
NR = VerdictLecteur(NE_REPOND_PAS, None, None)
SV = VerdictLecteur(SANS_VERDICT, None, "cannot_tell")


def test_statut_action_table_complete():
    assert m.statut_action(NR, NR) == (m.DESAPPARIEE, None)
    assert m.statut_action(R_S, R_S) == (m.APPARIEE, m.SPECIFIQUE)
    assert m.statut_action(R_G, R_G) == (m.APPARIEE, m.GENERIQUE)
    assert m.statut_action(R_S, R_G) == (m.APPARIEE, m.DISCORDANTE)
    for a, b in [(NR, R_S), (R_G, NR), (SV, NR), (NR, SV), (SV, SV), (R_S, SV)]:
        assert m.statut_action(a, b) == (m.ILLISIBLE, None)       # aucun verdict d'un seul lecteur
    with pytest.raises(GardeArret):
        m.statut_action(VerdictLecteur("peut-etre", None, None), NR)


def ep(verdicts, autres=()):
    """Dix actions : les verdicts donnés pour les premières (jugeables), puis les classes `autres`, puis des
    jugeables appariées."""
    acts = [m.ActionMesuree(JUGEABLE, v) for v in verdicts]
    acts += [m.ActionMesuree(c) for c in autres]
    acts += [m.ActionMesuree(JUGEABLE, (R_S, R_S)) for _ in range(10 - len(acts))]
    return acts


def test_taux_episode_denominateur_fixe():
    e = ep([(NR, NR), (NR, NR), (NR, SV), (R_G, R_G), (R_G, R_S)], [SANS_CONTROLES, SANS_PROPOSITION])
    t = m.taux_episode(e)
    assert t["tau"] == 0.2 and t["tau_plus"] == 0.3 and t["gamma"] == 0.1 and t["sigma"] == 0.1
    assert t["sans_proposition"] == 0.1 and t["tau_lecteur"] == (0.3, 0.2) and t["gamma_lecteur"] == (0.2, 0.1)
    assert t["jugeables"] == 8 and t["sans_verdict_lecteur"] == (0, 1)
    with pytest.raises(GardeArret):
        m.taux_episode(e[:9])
    with pytest.raises(GardeArret):            # verdicts sur une action non jugeable
        m.taux_episode(e[:9] + [m.ActionMesuree(SANS_CONTROLES, (NR, NR))])
    with pytest.raises(GardeArret):            # action jugeable sans verdicts
        m.taux_episode(e[:9] + [m.ActionMesuree(JUGEABLE)])


def test_taux_par_tache_et_parts():
    e1 = ep([(NR, NR), (SV, SV)])
    e2 = ep([], [SANS_CONTROLES] * 10)
    t = m.taux_par_tache({"t": [e1, e2]})["t"]
    assert t["tau"] == pytest.approx(0.05) and t["sigma"] == pytest.approx(0.5)
    assert t["part_jugeable"] == pytest.approx(0.5)
    assert t["tau_j"] == pytest.approx(1 / 10) and t["part_illisibles"] == pytest.approx(1 / 10)
    vide = m.taux_par_tache({"t": [e2]})["t"]
    assert vide["tau_j"] is None and vide["part_illisibles"] is None


def test_differences_appariees():
    d = m.differences_par_tache({"a": [0.3, 0.1], "b": [0.0, 0.2]}, {"a": [0.1, 0.1], "b": [0.0, 0.0]})
    assert d == {"a": pytest.approx(0.1), "b": pytest.approx(0.1)}
    with pytest.raises(GardeArret):
        m.differences_par_tache({"a": [0.1]}, {"a": [0.1, 0.2]})
    with pytest.raises(GardeArret):
        m.differences_par_tache({"a": [0.1]}, {"b": [0.1]})


def test_taux_d_un_jumeau():
    assert m.taux_d_un_jumeau({0: m.DESAPPARIEE, 1: m.ILLISIBLE}, {2: m.DESAPPARIEE, 3: m.APPARIEE}) == 0.2
    with pytest.raises(GardeArret):
        m.taux_d_un_jumeau({0: m.DESAPPARIEE}, {0: m.APPARIEE})


def lu(controles):
    return {"controles": {k: {"statut_strict": s, "porteuses": p} for k, (s, p) in controles.items()},
            "presents": [k for k, (s, _) in controles.items() if s != "absent"]}


def test_trois_couvertures():
    # plan de 4 segments = actions 0, 1, 3, 4 (l'action 2 est vide, hors du plan)
    indices = [0, 1, 3, 4]
    l1 = lu({"a": ("conforme", [0]), "b": ("conforme", [1]), "c": ("conforme", [2]), "d": ("absent", [])})
    l2 = lu({"a": ("conforme", [0]), "b": ("conforme", [1]), "c": ("conforme", [3]), "d": ("altere", [3])})
    ag = {"a": {"statut_retenu": "conforme", "places": ("checks", "general")},
          "b": {"statut_retenu": "conforme", "places": ("checks", "cannot_check")},
          "c": {"statut_retenu": "conforme", "places": ("general", "general")},
          "d": {"statut_retenu": "absent", "places": (None, "checks")}}
    statuts = {0: m.APPARIEE, 1: m.DESAPPARIEE, 3: m.APPARIEE, 4: m.ILLISIBLE}
    remplacees = [True, False, False, False, True]
    c = m.couvertures_episode(ag, l1, l2, indices, statuts, remplacees)
    assert c["C_c"] == 0.75 and c["C_a"] == 0.5 and c["C_v"] == 0.25 and c["part_presents"] == 0.75
    # couverts avec porteuse : a (action 0, remplacée), b (action 1), c (actions 3 et 4 : 3 non remplacée)
    assert c["part_couverts_portes_par_remplacees_ou_refusees"] == pytest.approx(1 / 3)


def test_places_et_accord():
    l1 = lu({"a": ("conforme", [0]), "b": ("altere", [0]), "c": ("absent", [])})
    p = m.places_rapportees(l1, {"a": "checks", "b": "cannot_check", "c": None})
    assert p == {"checks": 0.5, "cannot_check": 0.5, "general": 0.0}
    acc = m.accord_sur_la_place([{"a": {"places": ("checks", "checks")}, "b": {"places": ("general", "checks")},
                                  "c": {"places": (None, "checks")}}])
    assert acc["n"] == 2 and acc["part_meme_place"] == 0.5
    assert m.accord_sur_la_place([{"a": {"places": ("checks", "checks")}}])["kappa"] is None   # non défini
