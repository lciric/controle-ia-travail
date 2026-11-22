"""Essais de la pièce 8 — borne haute : couplage."""
import time

import pytest

from controle_ia.devin_v2 import RefusDevin
from controle_ia.devin_v2.borne_haute import borne_superieure, couplage, couplage_utile
from controle_ia.devin_v2.monde_plante import Fuite, HarnaisSimule
from controle_ia.devin_v2.vue import Champ, ELARGIE, Extracteur, ListeBlanche, Preuve, liste_blanche_monde

RACINE = 0x8EBB_2A8D_6C4F_5C7F_E703_7ED1_A0B4_28DB
IDS = [f"c{k}" for k in range(300)]
EXT = Extracteur(liste_blanche_monde(("horloge", "charge")))


def test_cas_sain_temoin_zero_difference_et_borne():
    h = HarnaisSimule(RACINE, [Fuite("verdict", 0.0)])
    r = couplage(h.episode, EXT, IDS, "piece", vue_complete=True)
    assert r["differences"] == 0 and r["temoin_secret_identique"] == "zéro différence"
    assert r["borne_vt"] == pytest.approx(0.0099, abs=1e-4)
    assert borne_superieure(0, 3000) == pytest.approx(0.0010, abs=1e-4)
    assert "non couvert" in r["etage_3"]


def test_artefact_horloge_reelle_visible_refusee():
    h = HarnaisSimule(RACINE)

    def episode_horloge(i, bits):
        e = h.episode(i, bits)
        e["horloge_reelle"] = time.perf_counter_ns()
        return e

    lb = ListeBlanche(list(liste_blanche_monde(("horloge",)).champs.values())
                      + [Champ("horloge_reelle", ELARGIE, Preuve("outil", "outil date du système"))])
    with pytest.raises(RefusDevin, match="témoin à secret identique"):
        couplage(episode_horloge, Extracteur(lb), IDS[:20], "piece")


def test_fuite_plantee_fait_differer_les_vues():
    h = HarnaisSimule(RACINE, [Fuite("horodatage", 0.1)])
    r = couplage(h.episode, EXT, IDS, "piece")
    assert r["differences"] == 300 and r["borne_vt"] == 1.0
    h2 = HarnaisSimule(RACINE, [Fuite("verdict", 0.1)])
    r2 = couplage(h2.episode, EXT, IDS, "piece")
    assert 10 < r2["differences"] < 60 and r2["differences"] / 300 < r2["borne_vt"] < 1


def test_quand_cela_vaut_la_peine():
    assert couplage_utile(True, True, True, False)
    assert not couplage_utile(True, False, True, False)
    assert couplage_utile(False, False, False, True)


def test_aucun_repli():
    with pytest.raises(RefusDevin):
        couplage(HarnaisSimule(RACINE).episode, EXT, [], "piece")
    with pytest.raises(RefusDevin):
        borne_superieure(5, 3)
    with pytest.raises(RefusDevin, match="commun"):
        couplage(HarnaisSimule(RACINE).episode, EXT, IDS[:2], "piece", {"piece": 1})
