"""Essais des lectures du volet A sur données synthétiques (aucun modèle) : fuite plantée retrouvée, témoins, A2, A3, cas sains."""
import numpy as np

from controle_ia.neuron_lens import volet_a_lectures_v1 as vl


def _monde(V=300, d=24, graine=0):
    rng = np.random.default_rng(graine)
    E = rng.normal(size=(V, d))
    K = np.eye(d) + 0.1 * rng.normal(size=(d, d))
    gardes = np.arange(V)
    return E, K, gardes, vl.LecteurCouche.construire(E, gardes, K, np.random.SeedSequence(5))


def test_a1_fuite_plantee_retrouvee_et_temoins():
    E, K, gardes, lec = _monde(V=20000)  # assez de jetons pour qu'une direction aléatoire ne place pas P dans ses 10 premiers
    idx_P = np.array([42])
    w = lec.F_s[42] / np.linalg.norm(lec.F_s[42])  # sonde alignée sur l'empreinte du jeton planté
    U = vl.directions_aleatoires(E.shape[1], 1)
    wp = vl.directions_aleatoires(E.shape[1], 2, n=1)[0]
    wc3 = vl.directions_aleatoires(E.shape[1], 3, n=1)[0]
    m = vl.mesure_a1(lec, idx_P, w, U, wp, wc3)
    assert m["rang_s"] == 1 and m["condition"] is True and m["s_place_p"]
    m2 = vl.mesure_a1(lec, idx_P, wp, U, wp, wc3)  # artefact : la sonde est un témoin → condition fausse
    assert m2["condition"] is False


def test_a2():
    E, K, gardes, lec = _monde()
    w = vl.directions_aleatoires(E.shape[1], 9, n=1)[0]
    poids = lec.z_s(w) + 0.01 * np.random.default_rng(0).normal(size=len(gardes))
    m = vl.mesure_a2(lec, w, poids, np.ones(len(gardes), bool), vl.directions_aleatoires(E.shape[1], 1))
    assert m["condition"] is True and m["rho_s"] > 0.99


def test_jetons_a3_et_retrait_et_tirages():
    E, K, gardes, lec = _monde()
    w = lec.F_s[7] / np.linalg.norm(lec.F_s[7])
    j = vl.jetons_a3(lec, w, gardes + 1000)
    assert len(j) == 20 and j[0] == 1007
    assert vl.retirer([1007, 5, 1007, 6], j[:1]) == [5, 6]
    freq = {int(g): (int(g) % 7) for g in gardes}
    t = vl.tirages_apparies_a3([3, 14], freq, gardes, graine=1, n=50)
    assert len(t) == 50 and all(len(x) == 2 for x in t)
    assert all(freq[x[1]] == 0 for x in t)  # le jeton 14 est absent (fréquence 0) : apparié à un absent
    assert all(freq[x[0]] > 0 for x in t)


def test_cas_sains():
    E, K, gardes, lec = _monde()
    assert vl.cas_sain_synthetique(lec, 17) == (True, True)
    voc = {i: f"Ġtok{i}" for i in range(300)}
    voc[50], voc[60] = "ĠOwls", "German"
    dec = lambda i: voc[i]
    lecture = np.zeros(300)
    lecture[50] = 9.0
    assert vl.cas_sain_owl(lecture, gardes, dec)[0] is True
    lecture2 = np.zeros(300)
    lecture2[60] = 9.0
    assert vl.cas_sain_german(lecture2, gardes, dec)[0] is True
    assert vl.cas_sain_owl(lecture2, gardes, dec)[0] is False  # artefact


def test_direction_lecture():
    a, b, g = np.array([1.0, 0, 0]), np.array([0, 2.0, 0]), np.ones(3)
    assert np.allclose(vl.direction_lecture(a, b, g, -1, False), [1, -1, 0])
    assert np.allclose(vl.direction_lecture(a, b, g, -1, True), [0, 1, 0])
    assert np.allclose(vl.direction_lecture(a, b, g, +1, True), [0, -1, 0])
