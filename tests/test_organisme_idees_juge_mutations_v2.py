"""Banc de mutations v2 : le banc v1 et les quatre mutations de la contre-lecture du code (et deux variantes), toutes
tuées pour la raison attendue (jeu synthétique réduit ici : l'essai v1 le joue sur 20 000 générations)."""
import pytest

from controle_ia.organisme_idees_juge import mutations_v2 as MU2


@pytest.fixture(scope="module")
def rapport():
    return MU2.banc(MU2.RACINE_ESSAI, 2000, 1000)


NEUVES = ("contre-lecture 1 : A lit le bloc suivant hors de la garde d'accès",
          "contre-lecture 2 : placebo ciblé (actives seulement)",
          "contre-lecture 3 : intervalle à 90 %",
          "contre-lecture 4 : seuil d'arrêt bas à 1/10 (constante)",
          "contre-lecture 4 bis : seuil d'arrêt bas à 1/10 écrit dans la règle",
          "contre-lecture 4 ter : seuil à 1/10, garde des constantes neutralisée (troisième écriture seule)")


def test_toutes_tuees_pour_la_raison_attendue(rapport):
    for nom in NEUVES:
        assert rapport["mutations"][nom]["tuee"], (nom, rapport["mutations"][nom])
    assert len(rapport["mutations"]) == 24
    assert all(r["tuee"] for r in rapport["mutations"].values())
    assert rapport["toutes_tuees"] and rapport["version_banc"] == 2
    MU2.exiger_toutes_tuees(rapport)
    assert "niveau de l'intervalle" in rapport["mutations"][NEUVES[2]]["raison"]
    assert "constante" in rapport["mutations"][NEUVES[3]]["raison"]
    assert "non conforme au texte" in rapport["mutations"][NEUVES[5]]["raison"]
