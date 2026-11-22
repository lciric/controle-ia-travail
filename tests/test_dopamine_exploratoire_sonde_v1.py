"""Sonde de réussite attendue par différence temporelle (exploratoire) : perte, aire sous la courbe, élagage, contrôles."""
import itertools

import numpy as np
import pytest

torch = pytest.importorskip("torch")

from controle_ia.dopamine_exploratoire import sonde_v1 as s  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

JOUET = dict(s.RECETTE_TABLEAU_7, epoques=30, cachee=16)


def test_recette_du_tableau_7():
    assert s.RECETTE_TABLEAU_7 == {"optimiseur": "AdamW", "pas": 1e-4, "decroissance": 0.01, "epoques": 100, "lot": 4,
                                   "part_entrainement": 0.8, "gamma": 1 - 1e-5, "cachee": 1024}
    assert len(s.TAUX_ELAGAGE_TABLEAU_8) == 15 and s.TAUX_ELAGAGE_TABLEAU_8[-1] == 0.99
    s.exiger_recette(dict(s.RECETTE_TABLEAU_7))
    with pytest.raises(GardeArret, match="tableau 7"):
        s.exiger_recette(dict(s.RECETTE_TABLEAU_7, pas=1e-3))
    with pytest.raises(GardeArret, match="epoques"):
        s.exiger_recette(JOUET)                                   # réduit hors du jouet : refus
    s.exiger_recette(JOUET, jouet=True)
    with pytest.raises(GardeArret, match="lot"):
        s.exiger_recette(dict(JOUET, lot=8), jouet=True)          # le jouet ne touche qu'aux époques et à la largeur


def test_aire_sous_courbe_contre_les_paires():
    rng = np.random.default_rng(0)
    for _ in range(5):
        sc = rng.integers(0, 5, 40).astype(float)                 # beaucoup d'ex aequo
        y = rng.integers(0, 2, 40)
        p = n = 0.0
        for i, j in itertools.product(np.flatnonzero(y == 1), np.flatnonzero(y == 0)):
            p += 1.0 if sc[i] > sc[j] else 0.5 if sc[i] == sc[j] else 0.0
            n += 1
        assert s.aire_sous_courbe(sc, y) == pytest.approx(p / n)
    with pytest.raises(GardeArret, match="indéfinie"):
        s.aire_sous_courbe([0.1, 0.2], [1, 1])
    with pytest.raises(GardeArret):
        s.aire_sous_courbe([0.1, np.nan], [0, 1])


def _boucle(v, r, g):
    T = len(v) - 1
    d = [g * v[t] - v[t - 1] for t in range(1, T + 1)] + [r - v[T]]
    return sum(x * x for x in d)


def test_perte_td_egale_la_somme_des_equations_8_et_9():
    v = torch.tensor([[0.2, 0.5, 0.1, 0.0], [0.9, 0.0, 0.0, 0.0], [0.3, 0.4, 0.0, 0.0]])
    lg, r, g = [4, 1, 2], torch.tensor([1.0, 0.0, 1.0]), 0.9
    attendu = np.mean([_boucle(v[b, :lg[b]].tolist(), float(r[b]), g) for b in range(3)])
    assert float(s.perte_td(v, lg, r, g)) == pytest.approx(attendu, rel=1e-6)
    with pytest.raises(GardeArret):
        s.perte_td(v, [5, 1, 1], r, g)
    with pytest.raises(GardeArret):
        s.perte_td(v, lg, r, g, gradient="autre")


def test_gradient_complet_et_semi_different():
    v1 = torch.tensor([[0.2, 0.5, 0.1]], requires_grad=True)
    v2 = torch.tensor([[0.2, 0.5, 0.1]], requires_grad=True)
    s.perte_td(v1, [3], torch.tensor([1.0]), 0.9, "complet").backward()
    s.perte_td(v2, [3], torch.tensor([1.0]), 0.9, "semi").backward()
    # en semi-gradient, V(s_t) ne reçoit de gradient que comme prédiction : d/dv0 identiques, d/dv1 différents
    assert float(v1.grad[0, 0]) == pytest.approx(float(v2.grad[0, 0]))
    assert float(v1.grad[0, 1]) != pytest.approx(float(v2.grad[0, 1]))


def test_decoupages():
    (a, v), = s.decoupages(10, "part", 0)
    assert len(a) == 8 and len(v) == 2 and set(a).isdisjoint(v)
    plis = s.decoupages(10, "plis", 0, plis=5)
    assert sorted(np.concatenate([v for _, v in plis]).tolist()) == list(range(10))
    assert s.decoupages(10, "part", 3)[0][1].tolist() == s.decoupages(10, "part", 3)[0][1].tolist()
    with pytest.raises(GardeArret):
        s.decoupages(10, "autre", 0)


def test_dimensions_gardees():
    imp = np.array([0.1, 5.0, 0.2, 3.0, 0.0])
    assert s.dimensions_gardees(imp, 0.0).tolist() == [0, 1, 2, 3, 4]
    assert s.dimensions_gardees(imp, 0.6).tolist() == [1, 3]
    assert s.dimensions_gardees(imp, 0.99).tolist() == [1]          # ⌊0,99 × 5⌋ = 4 masquées


def _donnees(rng, n=48, d=6, signal=True):
    """Trajectoires où s_0 porte l'issue (vrai) ou non (faux, étiquettes indépendantes)."""
    y = rng.integers(0, 2, n)
    seqs = []
    for i in range(n):
        T = int(rng.integers(1, 5))
        x = rng.standard_normal((T + 1, d)).astype(np.float16)
        if signal:
            x[:, 0] += np.float16(3.0 * (2 * y[i] - 1))
        seqs.append(x)
    return seqs, y


def test_sonde_lit_une_issue_plantee_et_pas_une_issue_independante():
    rng = np.random.default_rng(5)
    seqs, y = _donnees(rng, signal=True)
    (a, v), = s.decoupages(len(y), "part", 1)
    with pytest.raises(GardeArret):                                   # pas de 1e-2 : hors recette, même pour le jouet
        s.entrainer([seqs[i] for i in a], y[a], dict(s.RECETTE_TABLEAU_7, epoques=2, cachee=8, pas=1e-2), 0, jouet=True)
    rec = dict(s.RECETTE_TABLEAU_7, epoques=200, cachee=16)
    m = s.entrainer([seqs[i] for i in a], y[a], rec, 0, jouet=True)
    assert s.aire_sous_courbe(s.valeurs_s0(m, [seqs[i] for i in v]), y[v]) > 0.9
    seqs0, y0 = _donnees(np.random.default_rng(6), n=80, signal=False)
    (a0, v0), = s.decoupages(len(y0), "part", 1)
    m0 = s.entrainer([seqs0[i] for i in a0], y0[a0], rec, 0, jouet=True)
    assert 0.2 < s.aire_sous_courbe(s.valeurs_s0(m0, [seqs0[i] for i in v0]), y0[v0]) < 0.8


def test_grille_elagage_masque_par_defaut_et_meilleur_taux():
    rng = np.random.default_rng(7)
    seqs, y = _donnees(rng, n=40, d=10)
    (a, v), = s.decoupages(len(y), "part", 2)
    rec = dict(s.RECETTE_TABLEAU_7, epoques=20, cachee=8)
    m = s.entrainer([seqs[i] for i in a], y[a], rec, 0, jouet=True)
    g = s.grille_elagage([seqs[i] for i in a], y[a], [seqs[i] for i in v], y[v], rec, 0, (0.0, 0.5, 0.9),
                         jouet=True, sonde_complete=m)
    assert set(g) == {0.0, 0.5, 0.9} and g[0.9]["dimensions_gardees"] == 1 and g[0.5]["dimensions_gardees"] == 5
    assert g[0.0]["aire"] == s.aire_sous_courbe(s.valeurs_s0(m, [seqs[i] for i in v]), y[v])   # p = 0 : sonde entière
    gr = s.grille_elagage([seqs[i] for i in a], y[a], [seqs[i] for i in v], y[v], rec, 0, (0.0, 0.5),
                          reapprendre=True, jouet=True, sonde_complete=m)
    assert gr[0.0]["aire"] == g[0.0]["aire"] and len(gr[0.5]["scores"]) == len(v)
    imp = s.importance_l1(m)
    gardes = [set(s.dimensions_gardees(imp, p)) for p in s.TAUX_ELAGAGE_TABLEAU_8]
    assert all(b <= a_ for a_, b in zip(gardes, gardes[1:]))                                    # emboîtés
    assert len(s.dimensions_gardees(np.arange(4096.0), 0.99)) == 41                           # ⌊0,99 × 4096⌋ masquées
    b = s.meilleur_taux({2: {0.0: 0.6, 0.5: 0.75}, 3: {0.0: 0.8, 0.5: 0.7}})
    assert b["aire_au_meilleur_taux"] == pytest.approx((0.75 + 0.8) / 2)                      # maximum par couche
    assert b["meilleur_taux_par_couche"] == {"2": 0.5, "3": 0.0}
    assert b["taux_commun"] == 0.5 and b["aire_au_taux_commun"] == pytest.approx(0.725)
    assert b["aire_au_taux_0"] == pytest.approx(0.7)
    assert s.meilleur_taux({2: {0.0: 0.7, 0.5: 0.7}})["taux_commun"] == 0.0                   # ex aequo : le plus petit


def test_garde_du_terme_final(monkeypatch):
    s.exiger_terme_final()
    sans_terme = lambda v, lg, r, g, gradient="complet": ((g * v[:, 1:] - v[:, :-1]) ** 2).sum(1).mean()
    monkeypatch.setattr(s, "perte_td", sans_terme)                     # artefact : terme final ôté
    with pytest.raises(GardeArret, match="terme final"):
        s.exiger_terme_final()


def test_injection_et_intervalle():
    rng = np.random.default_rng(3)
    seqs = [rng.standard_normal((int(rng.integers(1, 6)), 8)).astype(np.float16) for _ in range(200)]
    inj, y, u = s.injecter_verite({3: seqs}, 4.0, np.random.default_rng(4))
    proj = np.array([float(np.asarray(t[0], dtype=np.float64) @ u) for t in inj[3]])
    assert s.aire_sous_courbe(proj, y) > 0.99
    assert all(t.shape == o.shape and t.dtype == np.float16 for t, o in zip(inj[3], seqs))
    lo, hi = s.intervalle_aire(proj, y, np.random.default_rng(0), tirages=300)
    assert 0.98 < lo <= hi <= 1.0
    lo0, hi0 = s.intervalle_aire(rng.standard_normal(200), y, np.random.default_rng(0), tirages=300,
                                 groupes=np.arange(200) % 5)
    assert lo0 < 0.5 < hi0


def test_controles_permutation_et_verite_plantee():
    rng = np.random.default_rng(8)
    r = np.array([0, 1] * 10)
    p = s.etiquettes_permutees(r, rng)
    assert sorted(p.tolist()) == sorted(r.tolist())
    x0 = rng.standard_normal((400, 5))
    lab, u = s.verite_plantee(x0, 6.0, np.random.default_rng(9))
    assert s.aire_sous_courbe(x0 @ u, lab) > 0.85
    lab0, u0 = s.verite_plantee(x0, 0.0, np.random.default_rng(9))
    assert abs(s.aire_sous_courbe(x0 @ u0, lab0) - 0.5) < 0.1
    with pytest.raises(GardeArret):
        s.verite_plantee(np.ones((10, 3)), 3.0, rng)


# --- garde de la vérité plantée, lecture par pli (réponse 39 de Fable, option c) ---------------------------------

def _plis_a_niveaux(aires_voulues, n=100, graine=3):
    """Scores de cinq plis : chaque pli a son propre niveau (décalé), et un ordre interne qui donne l'aire voulue
    (1,0 : séparation parfaite ; sinon mélange d'une part des issues)."""
    rng = np.random.default_rng(graine)
    sc, y, g = [], [], []
    for k, aire in enumerate(aires_voulues):
        yk = np.array([0, 1] * (n // 2))
        base = 0.36 + 0.03 * k                                   # niveau propre au pli, comme sur la carte
        sk = base + 0.001 * yk + 1e-5 * rng.random(n)
        if aire < 1.0:                                          # brouiller : une part des issues 1 sous les issues 0
            m = int(round((1 - aire) * (n // 2)))              # m issues 1 sous toutes les issues 0 : aire = 1 − m/(n/2)
            un = np.flatnonzero(yk == 1)[:m]
            sk[un] = base - 0.001 + 1e-5 * rng.random(m)
        sc.append(sk); y.append(yk); g.append(np.full(n, k))
    return np.concatenate(sc), np.concatenate(y), np.concatenate(g)


def test_garde_plantee_cinq_plis_parfaits_a_niveaux_decales_passe_et_signale_l_ecart():
    sc, y, g = _plis_a_niveaux([1.0] * 5)
    lec = s.lecture_plantee_par_pli(sc, y, g, np.random.default_rng(0), tirages=300)
    assert lec["arret"] == []
    assert all(p["aire"] == 1.0 for p in lec["plis"]) and lec["pire_borne_basse"] == 1.0
    assert lec["aire_commune_brute"] < 0.9                       # l'ancienne lecture aurait arrêté
    assert lec["aire_commune_recalee"] == 1.0 and lec["ecart_d_echelle_entre_plis"] is True


def test_garde_plantee_quatre_plis_parfaits_et_un_a_0_65_arrete():
    sc, y, g = _plis_a_niveaux([1.0, 1.0, 1.0, 1.0, 0.65])
    lec = s.lecture_plantee_par_pli(sc, y, g, np.random.default_rng(0), tirages=300)
    faible = [p for p in lec["plis"] if p["pli"] == 4][0]
    assert abs(faible["aire"] - 0.65) < 0.03
    assert lec["aire_moyenne_des_plis"] > 0.9                    # la moyenne aurait laissé passer
    assert lec["arret"] and "pire pli" in lec["arret"][0]


def test_garde_plantee_arrete_sur_pli_a_une_classe_et_score_non_fini():
    sc, y, g = _plis_a_niveaux([1.0] * 5)
    y1 = y.copy(); y1[g == 2] = 1
    assert "une seule classe" in s.lecture_plantee_par_pli(sc, y1, g, np.random.default_rng(0), tirages=50)["arret"][0]
    s2 = sc.copy(); s2[7] = np.nan
    assert s.lecture_plantee_par_pli(s2, y, g, np.random.default_rng(0), tirages=50)["arret"] == ["score non fini"]
