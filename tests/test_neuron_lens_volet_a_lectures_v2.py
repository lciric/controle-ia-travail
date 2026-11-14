"""Essais (v2) des lectures du volet A sur données synthétiques (aucun modèle) : fuite plantée retrouvée, témoins, A2, A3, cas sains."""
import numpy as np

from controle_ia.neuron_lens import volet_a_lectures_v2 as vl


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


# ---------------------------------------------------------------- ajouts v2 (contre-lecture 1, remarques 3, 4, 5, 8 à 10)
import pytest  # noqa: E402

from controle_ia.neuron_lens import decisions_volet_a_v4 as da  # noqa: E402


def test_a1_artefact_temoin_qui_lit_la_meme_fuite():
    E, K, gardes, lec = _monde(V=20000)
    idx_P = np.array([42])
    w = lec.F_s[42] / np.linalg.norm(lec.F_s[42])
    U = vl.directions_aleatoires(E.shape[1], 1)
    wc3 = vl.directions_aleatoires(E.shape[1], 3, n=1)[0]
    m = vl.mesure_a1(lec, idx_P, w, U, w.copy(), wc3)  # la sonde permutée lit la même fuite : condition fausse
    assert m["rang_s"] == 1 and m["un_temoin_place_p"] and m["condition"] is False


def test_a2_temoins_rapportes_et_artefact():
    E, K, gardes, lec = _monde()
    w = vl.directions_aleatoires(E.shape[1], 9, n=1)[0]
    wp = vl.directions_aleatoires(E.shape[1], 2, n=1)[0]
    poids = lec.z_s(w) + 0.01 * np.random.default_rng(0).normal(size=len(gardes))
    pres = np.ones(len(gardes), bool)
    pres[::3] = False  # vrai masque : un tiers absent
    U = vl.directions_aleatoires(E.shape[1], 1)
    m = vl.mesure_a2(lec, w, poids, pres, U, w_permutee=wp, w_c3=w)
    assert m["condition"] is True and m["rho_c3"] == m["rho_s"] and abs(m["rho_permutee"]) < 0.5
    assert m["rho_s"] == da.rho_a2(lec.z_s(w), poids, pres)
    bruit = np.random.default_rng(4).normal(size=len(gardes))  # artefact : poids sans lien avec w
    assert vl.mesure_a2(lec, w, bruit, pres, U)["condition"] is False
    assert vl.mesure_a2(lec, w, poids, pres, U)["rho_permutee"] is None


def test_tirages_a3_excluent_les_retires_sans_doublon_deciles():
    gardes = np.arange(2000)
    freq = {int(g): int(g) // 10 for g in gardes}  # 0 pour 0..9, puis fréquences croissantes
    jetons = [1500, 1501, 1502, 1503, 3]
    t = vl.tirages_apparies_a3(jetons, freq, gardes, graine=1, n=200)
    seuils = np.quantile(np.array([f for f in freq.values() if f > 0]), np.linspace(0, 1, 11)[1:-1])
    cl = lambda f: 0 if f == 0 else 1 + int(np.searchsorted(seuils, f, side="right"))
    for x in t:
        assert not (set(x) & set(jetons)) and len(set(x)) == len(x)
        assert [cl(freq[v]) for v in x] == [cl(freq[j]) for j in jetons]
    assert t == vl.tirages_apparies_a3(jetons, freq, gardes, graine=1, n=200)


def test_tirages_a3_classe_trop_petite_refusee():
    gardes = np.arange(100)
    freq = {int(g): (0 if g < 3 else 5 + int(g)) for g in gardes}  # trois absents seulement
    with pytest.raises(ValueError):
        vl.tirages_apparies_a3([0, 1, 2], freq, gardes, graine=1, n=5)  # les 3 absents sont retirés : aucun candidat


def test_cas_sains_formes_et_artefacts():
    gardes = np.arange(300)
    for forme_, attendu in (("Ġnight", True), ("Ġnightly", False), ("Ġnocturnal", True), ("owl", True), ("Ġbowl", False)):
        voc = {i: f"Ġtok{i}" for i in range(300)}
        voc[50] = forme_
        lecture = np.zeros(300)
        lecture[50] = 9.0
        assert vl.cas_sain_owl(lecture, gardes, voc.__getitem__)[0] is attendu, forme_
    voc = {i: f"Ġtok{i}" for i in range(300)}
    voc[60] = "德国"
    lecture = np.zeros(300)
    lecture[60] = 9.0
    assert vl.cas_sain_german(lecture, gardes, voc.__getitem__)[0] is True


def test_cas_sain_synthetique_artefact():
    E, K, gardes, lec = _monde()
    E2 = E.copy()
    E2[16] = E2[17]  # artefact : un jeton d'indice plus petit a la même empreinte que v0 (tri stable : il passe devant)
    lec2 = vl.LecteurCouche.construire(E2, gardes, K, np.random.SeedSequence(5))
    assert vl.cas_sain_synthetique(lec2, 17) == (False, False)  # égalité départagée vers l'indice 16 : rang de 17 ≠ 1


def test_direction_lecture_gamma():
    a, b, g = np.array([1.0, 0, 0]), np.array([0, 1.0, 0]), np.array([1.0, 3.0, 1.0])
    out = vl.direction_lecture(a, b, g, +1, False)
    assert np.allclose(out, [1, 1, 0])  # γ appliqué puis normé
    a2 = np.array([1.0, 1.0, 0])
    out2 = vl.direction_lecture(a2, b, g, +1, False)
    assert np.allclose(out2, np.array([1, 3, 0]) / np.sqrt(10) + np.array([0, 1, 0]))
