"""Essai proposé : garde P10 éprouvée sans modèle ajusté. La vraisemblance est simulée : elle vaut 1 si le contexte
est celui de l'épisode de l'action (même condition, même tâche, même pas), 0 sinon ; on fixe exactement combien
d'actions « passent ». Le seuil 95 % et le minimum de 10 actions sont éprouvés à la frontière."""
import dataclasses

import pytest

from controle_ia.barreau8_moniteurs import passe_recalcul_v2 as P
from controle_ia.gardes import GardeArret

SPEC = dataclasses.replace(P.SPECIFICATION_TEXTE, n_taches=20, pas_par_episode=1)


class AdaptateursFactices:
    def __init__(self):
        self.poses = []

    def poser(self, condition):
        self.poses.append(condition.nom)

    def relire(self, condition, actions=0):
        pass


def monde(n_taches: int, fautives: set[int]):
    actions, episodes = [], {}
    for k in range(n_taches):
        tache = f"t{k:02d}"
        a = P.Action(k, f"evaluation-H/{tache}/pas0", "evaluation-H", tache, tache, "H", 0, "", [10 + k] * 5 + [1], 5)
        actions.append(a)
        # le contexte porte la tâche ; une action « fautive » a un contexte rebâti étranger (le marqueur -1)
        episodes[("H", tache)] = P.Episode("H", tache, [-1 if k in fautives else 1000 + k, 7], [(2, 8)])
    return actions, episodes


def appel(actions, episodes, monkeypatch, decalage=0):
    vus = []

    def vraisemblances(modele, pad, contextes, suites):
        sortie = []
        for c, s in zip(contextes, suites):
            vus.append((c[0], s[0]))
            sortie.append(1.0 if c[0] == 1000 + (s[0] - 10) else 0.0)
        return sortie

    monkeypatch.setattr(P, "log_vraisemblances", vraisemblances)
    trace = P.TraceGardes()
    r = P.garde_p10(SPEC, None, 0, AdaptateursFactices(), actions, episodes, {a.rang for a in actions}, trace,
                    decalage_de_tache=decalage)
    return r, trace, vus


def test_frontiere_95_pour_cent_tenue(monkeypatch):
    actions, episodes = monde(20, fautives={3})                  # 19 sur 20 = 0,95 : tenue (borne comprise)
    r, trace, vus = appel(actions, episodes, monkeypatch)
    assert r["fraction"] == 0.95 and r["artefact"]["fraction"] == 0.0 and r["actions_controlees"] == 20
    assert len(vus) == 60                                         # trois contextes par action : propre, +1, +2


def test_frontiere_95_pour_cent_non_tenue(monkeypatch):
    actions, episodes = monde(20, fautives={3, 4})                # 18 sur 20 = 0,90 : non tenue
    with pytest.raises(GardeArret, match="contexte rebâti"):
        appel(actions, episodes, monkeypatch)


def test_moins_de_dix_actions(monkeypatch):
    actions, episodes = monde(9, fautives=set())
    with pytest.raises(GardeArret, match="9 action"):
        appel(actions, episodes, monkeypatch)


def test_egalite_ne_passe_pas(monkeypatch):
    actions, episodes = monde(20, fautives=set())
    monkeypatch.setattr(P, "log_vraisemblances", lambda m, p, c, s: [0.5] * len(c))
    with pytest.raises(GardeArret, match="garde aveugle|contexte rebâti"):
        P.garde_p10(SPEC, None, 0, AdaptateursFactices(), actions, episodes, {a.rang for a in actions}, P.TraceGardes())
