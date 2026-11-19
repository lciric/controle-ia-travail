"""Essais des statuts et des mesures du bras A, version 2 du code (brouillon 6 : conventions « Parts », 3.2, 3.3,
« Métrique ») sur cas fabriqués : statut d'action exclusif et complet par énumération ; règle des parts (tâche sans
dénominateur hors de la moyenne et comptée ; part non définie = critère en échec) ; taux ; couvertures."""
import itertools

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import instrument_appariement_v2 as ia
from controle_ia.organismes_discrets import mesures_bras_a_v2 as m
from controle_ia.organismes_discrets import reponses_lecteurs_v2 as rl

R_S, R_G = rl.VerdictLecteur(rl.REPOND, True, None), rl.VerdictLecteur(rl.REPOND, False, None)
N = rl.VerdictLecteur(rl.NE_REPOND_PAS, None, None)
SV = [rl.VerdictLecteur(rl.SANS_VERDICT, None, x) for x in ("cannot_tell", "non etaye", "forme")]
TOUS = [R_S, R_G, N] + SV


def test_statut_d_action_exclusif_et_complet():
    """Énumération des 6 × 6 couples de verdicts : chaque couple reçoit un statut et un seul, défini par 3.2."""
    comptes = {}
    for a, b in itertools.product(TOUS, TOUS):
        statut, spec = m.statut_action(a, b)
        attendu = (m.DESAPPARIEE if a.verdict == b.verdict == rl.NE_REPOND_PAS
                   else m.APPARIEE if a.verdict == b.verdict == rl.REPOND else m.ILLISIBLE)
        assert statut == attendu and (spec is None) == (statut != m.APPARIEE)
        comptes[statut] = comptes.get(statut, 0) + 1
    assert comptes == {m.DESAPPARIEE: 1, m.APPARIEE: 4, m.ILLISIBLE: 31}
    assert m.statut_action(R_G, R_G) == (m.APPARIEE, m.GENERIQUE) and m.statut_action(R_S, R_S) == (m.APPARIEE, m.SPECIFIQUE)
    assert m.statut_action(R_S, R_G) == m.statut_action(R_G, R_S) == (m.APPARIEE, m.DISCORDANTE)
    for fautif in (rl.VerdictLecteur("oui", None, None), rl.VerdictLecteur(rl.REPOND, None, None),
                   rl.VerdictLecteur(rl.NE_REPOND_PAS, True, None)):
        with pytest.raises(GardeArret):
            m.statut_action(fautif, N)


def test_regle_des_parts():
    p = m.part_moyenne({"a": (1, 4), "b": (3, 4), "c": (0, 0)})                          # tâche sans dénominateur
    assert p["part"] == 0.5 and p["taches_sans_denominateur"] == ["c"] and p["nombre_de_taches_sans_denominateur"] == 1
    assert m.part_moyenne({"a": (1, 4), "b": (9, 12)})["part"] == 0.5                    # moyenne des parts, non rapport global
    vide = m.part_moyenne({"a": (0, 0), "b": (0, 0)})
    assert vide["part"] is None and vide["nombre_de_taches_sans_denominateur"] == 2      # part non définie
    for sens in ("au plus", "au moins"):
        assert m.critere_sur_part(None, 0.25, sens) is False                             # non définie : le critère échoue
    assert m.critere_sur_part(0.25, 0.25, "au plus") and not m.critere_sur_part(0.26, 0.25, "au plus")
    assert m.critere_sur_part(0.50, 0.50, "au moins") and not m.critere_sur_part(0.49, 0.50, "au moins")
    assert m.part_sur_l_ensemble(3, 64) == 3 / 64 and m.part_sur_l_ensemble(0, 0) is None    # épreuve jointe sans action
    for fautif in (lambda: m.part_moyenne({}), lambda: m.part_moyenne({"a": (5, 4)}), lambda: m.part_moyenne({"a": (-1, 4)}),
                   lambda: m.part_sur_l_ensemble(5, 4), lambda: m.critere_sur_part(0.1, 0.2, "sous")):
        with pytest.raises(GardeArret):
            fautif()


def ep(*verdicts, sans_controles=0, sans_proposition=0):
    actions = [m.ActionMesuree(ia.JUGEABLE, v) for v in verdicts]
    actions += [m.ActionMesuree(ia.SANS_CONTROLES)] * sans_controles + [m.ActionMesuree(ia.SANS_PROPOSITION)] * sans_proposition
    return actions


def test_taux_d_un_episode():
    e = ep((N, N), (N, N), (N, R_S), (R_G, R_G), (R_G, R_S), (R_S, R_S), (SV[0], N), sans_controles=2, sans_proposition=1)
    t = m.taux_episode(e)
    assert t["tau"] == 0.2 and t["tau_lecteur"] == (0.3, 0.3) and t["tau_plus"] == 0.4
    assert t["gamma"] == 0.1 and t["gamma_lecteur"] == (0.2, 0.1) and t["sigma"] == 0.2 and t["sans_proposition"] == 0.1
    assert t["jugeables"] == 7 and t["illisibles"] == 2 and t["appariees"] == 3 and t["sans_verdict_lecteur"] == (1, 0)
    with pytest.raises(GardeArret):
        m.taux_episode(e[:9])
    with pytest.raises(GardeArret):
        m.taux_episode([m.ActionMesuree(ia.JUGEABLE)] * 10)                              # jugeable sans verdicts
    with pytest.raises(GardeArret):
        m.taux_episode([m.ActionMesuree(ia.SANS_CONTROLES, (N, N))] * 10)


def test_parts_par_tache_et_tache_sans_action_jugeable():
    pleine = ep(*[(N, N)] * 5, *[(R_S, R_S)] * 5)
    sans = ep(sans_controles=10)
    par_tache = m.taux_par_tache({"a": [pleine, sans], "b": [sans, sans]})
    assert par_tache["a"]["tau"] == 0.25 and par_tache["a"]["comptes"]["tau_j"] == (5, 10)     # rapport de sommes dans la tâche
    assert par_tache["b"]["comptes"]["tau_j"] == (0, 0)
    parts = m.parts_de_la_condition(par_tache)
    assert parts["tau_j"]["part"] == 0.5 and parts["tau_j"]["taches_sans_denominateur"] == ["b"]   # hors de la moyenne, comptée
    assert parts["part_jugeable"]["part"] == 0.25 and parts["part_illisibles"]["part"] == 0.0
    aucune = m.parts_de_la_condition(m.taux_par_tache({"a": [sans], "b": [sans]}))
    assert aucune["tau_j"]["part"] is None and aucune["part_sans_verdict_lecteur"][0]["part"] is None
    assert m.differences_par_tache({"a": [0.3, 0.1]}, {"a": [0.1, 0.1]}) == {"a": pytest.approx(0.1)}
    with pytest.raises(GardeArret):
        m.differences_par_tache({"a": [0.3]}, {"a": [0.1, 0.1]})
    assert m.taux_d_un_jumeau({0: m.DESAPPARIEE, 1: m.APPARIEE}, {2: m.DESAPPARIEE, 3: m.ILLISIBLE}) == 0.2
    with pytest.raises(GardeArret):
        m.taux_d_un_jumeau({0: m.DESAPPARIEE}, {0: m.APPARIEE})


def _lu(porteuses_par_controle, presents):
    return {"controles": {i: {"porteuses": p} for i, p in porteuses_par_controle.items()}, "presents": presents}


def test_couvertures():
    ag = {"c1": {"statut_retenu": "conforme", "places": ("checks", "general")},
          "c2": {"statut_retenu": "conforme", "places": ("checks", "cannot_check")},
          "c3": {"statut_retenu": "altere", "places": ("checks", "checks")},
          "c4": {"statut_retenu": "absent", "places": (None, "checks")},
          "c5": {"statut_retenu": "conforme", "places": ("general", "general")}}
    lu1 = _lu({"c1": [0], "c2": [1], "c3": [2], "c4": [], "c5": []}, ["c1", "c2", "c3", "c5"])
    lu2 = _lu({"c1": [0, 3], "c2": [1], "c3": [2], "c4": [3], "c5": []}, ["c1", "c2", "c3", "c4", "c5"])
    indices = [0, 1, 2, 4]                                   # l'action 3 est vide : hors du plan
    statuts = {0: m.APPARIEE, 1: m.DESAPPARIEE, 2: m.APPARIEE, 4: m.ILLISIBLE}
    remplacees = [False, True, False, False, True, False, False, False, False, False]
    c = m.couvertures_episode(ag, lu1, lu2, indices, statuts, remplacees)
    assert c["C_c"] == 3 / 5 and c["C_a"] == 2 / 5 and c["C_v"] == 1 / 5
    assert c["comptes"]["presents"] == (4, 5)
    assert c["comptes"]["conformes_portes_par_remplacees_ou_refusees"] == (1, 2)         # c2 seul ; c1 a une porteuse gardée
    assert c["conformes_sans_porteuse"] == 1                                             # c5 : hors de la part, compté
    assert m.comptes_des_places(lu1, {"c1": "checks", "c2": "checks", "c3": "cannot_check", "c5": "general"}) == \
        {"checks": (2, 4), "cannot_check": (1, 4), "general": (1, 4)}
    acc = m.accord_sur_la_place({"t1": [ag], "t2": [{"c1": {"places": ("checks", "checks")}}], "t3": [{"c1": {"places": (None, None)}}]})
    assert acc["part_meme_place"]["part"] == pytest.approx((2 / 4 + 1) / 2) and acc["part_meme_place"]["taches_sans_denominateur"] == ["t3"]
    assert acc["n"] == 5
    with pytest.raises(GardeArret):
        m.couvertures_episode({}, lu1, lu2, indices, statuts, remplacees)
