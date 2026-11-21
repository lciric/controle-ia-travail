"""Couplage par moitié de l'oracle à contexte réécrit, v5 (texte scellé, 3.3 a et b ; section 13, `couplage_v5.py`)."""
from fractions import Fraction
from itertools import product

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.iib import couplage_v5 as cp


def frequences_par_suite(suites, loi_sachant_j=cp.loi_de_l_indice_sachant_j):
    """Énumération complète : le coût déclaré occupe chacune des k + 1 places avec la même probabilité (valeurs échangeables) ;
    fréquence exacte avec laquelle chaque suite est retenue."""
    k = sum(v is not None for v in suites)
    freq = {}
    for j in range(k + 1):
        for i, p in loi_sachant_j(suites, j).items():
            freq[i] = freq.get(i, Fraction(0)) + p / (k + 1)
    return freq


def uniforme(suites, loi_sachant_j=cp.loi_de_l_indice_sachant_j) -> bool:
    k = sum(v is not None for v in suites)
    return frequences_par_suite(suites, loi_sachant_j) == {i: Fraction(1, k) for i, v in enumerate(suites) if v is not None}


@pytest.mark.parametrize("k", range(1, 9))
def test_enumeration_complete_frequence_egale_sans_ex_aequo(k):
    assert uniforme([float(10 + 3 * i) for i in range(k)])
    assert uniforme([float(10 + 3 * i) for i in range(k)] + [None] * (8 - k))


@pytest.mark.parametrize("k", range(1, 9))
def test_enumeration_complete_frequence_egale_avec_ex_aequo(k):
    for motif in product((100.0, 200.0, 500.0), repeat=min(k, 5)):
        suites = (list(motif) * 2)[:k]
        assert uniforme(suites), suites


def test_la_loi_sachant_le_cout_est_la_moyenne_des_lois_sachant_la_place():
    suites = [100.0, 100.0, 200.0, 200.0, 200.0, 500.0, None, 1000.0]
    loi = cp.loi_de_la_suite_retenue(suites, 200.0)            # deux suites dessous, trois ex aequo : places 2 à 5
    attendu = {}
    for j in range(2, 6):
        for i, p in cp.loi_de_l_indice_sachant_j(suites, j).items():
            attendu[i] = attendu.get(i, Fraction(0)) + p / 4
    assert loi == attendu and sum(loi.values()) == 1


def test_frequence_par_valeur_reunie_dite():
    """Rapporté, sans règle : parmi les k + 1 valeurs réunies (coût et suites), la valeur retenue est de fréquence égale tant que
    les blocs ne jouent pas (k ≤ 4) ; elle ne l'est plus exactement au-delà. L'essai écrit ce que le code fait."""
    def par_valeur(n):
        valeurs = [float(10 + i) for i in range(n)]
        freq = [Fraction(0)] * n
        for c in range(n):
            positions = [i for i in range(n) if i != c]
            for i, p in cp.loi_de_la_suite_retenue([valeurs[i] for i in positions], valeurs[c]).items():
                freq[positions[i]] += p / n
        return freq
    for k in range(1, 5):
        assert par_valeur(k + 1) == [Fraction(1, k + 1)] * (k + 1)
    f8 = par_valeur(9)
    assert f8 == [Fraction(7, 72)] * 4 + [Fraction(2, 9)] + [Fraction(7, 72)] * 4      # la valeur du milieu : deux fois plus souvent


def test_loi_du_rang_uniforme_a_tout_k():
    for k in range(1, 9):
        loi = {}
        for j in range(k + 1):
            for r, p in cp.loi_du_rang_retenu(j, k).items():
                loi[r] = loi.get(r, Fraction(0)) + p / (k + 1)
        assert loi == {r: Fraction(1, k) for r in range(1, k + 1)}


def test_artefact_un_couplage_qui_prend_toujours_la_voisine_du_dessus_est_refuse():
    def toujours_dessus(suites, j):
        lis = sorted((i for i, v in enumerate(suites) if v is not None), key=lambda i: suites[i])
        k = len(lis)
        rangs = cp.bloc_du_rang(min(j + 1, k), k)
        return {lis[r - 1]: Fraction(1, len(rangs)) for r in rangs}
    for k in range(5, 9):                                   # de 1 à 4 suites, un seul bloc : la voisine ne change rien
        suites = [float(10 + i) for i in range(k)]
        assert uniforme(suites) and not uniforme(suites, toujours_dessus), k


def test_blocs_bas_et_haut():
    suites = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0]
    for graine in range(50):
        bas = cp.choisir(suites, 1.0, np.random.default_rng(graine))
        haut = cp.choisir(suites, 1000.0, np.random.default_rng(graine))
        assert bas["cas"] == "a" and bas["j"] == 0 and bas["rang_voisine"] == 1 and bas["rang_retenue"] in (1, 2, 3, 4) and bas["indice"] in (0, 1, 2, 3)
        assert haut["j"] == 8 and haut["rang_voisine"] == 8 and haut["rang_retenue"] in (5, 6, 7, 8) and haut["indice"] in (4, 5, 6, 7)
    assert cp.bloc_du_rang(5, 6) == [5, 6] and cp.bloc_du_rang(4, 6) == [1, 2, 3, 4] and cp.bloc_du_rang(1, 1) == [1]


def test_cout_illisible_suite_illisible_ou_repli_vide():
    suites = [10.0, None, 30.0, None, 50.0, 60.0, 70.0, 80.0]
    vus = {cp.choisir(suites, None, np.random.default_rng(g))["indice"] for g in range(60)}
    assert vus == {1, 3}
    r = cp.choisir([10.0] * 8, None, np.random.default_rng(0))
    assert r["repli_vide"] and r["indice"] is None and r["cas"] == "b"
    assert cp.loi_de_la_suite_retenue([10.0] * 8, None) == {cp.REPLI_VIDE: Fraction(1)}
    # coût lisible mais aucune suite lisible : cas b
    assert cp.choisir([None] * 8, 5.0, np.random.default_rng(0))["cas"] == "b"


def test_le_tirage_par_graine_suit_la_loi_exacte():
    suites, cout = [100.0, 100.0, 200.0, 200.0, 200.0, 500.0, None, 1000.0], 200.0
    loi = cp.loi_de_la_suite_retenue(suites, cout)
    assert sum(loi.values()) == 1 and None not in loi and 6 not in loi
    n = 20000
    compte = np.zeros(8)
    rng = np.random.default_rng(7)
    for _ in range(n):
        compte[cp.choisir(suites, cout, rng)["indice"]] += 1
    for i in range(8):
        attendu = float(loi.get(i, 0))
        assert abs(compte[i] / n - attendu) < 4 * (attendu * (1 - attendu) / n) ** 0.5 + 1e-9, i


def test_artefact_un_code_qui_rend_la_fenetre_de_l_agent_est_refuse():
    bon = cp.choisir([10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0], 35.0, np.random.default_rng(1))
    cp.exiger_remplacement_du_jumeau(bon, 8)
    for mauvais in ({**bon, "indice": " 35 GPU-hours"}, {**bon, "indice": 8}, {**bon, "indice": None}, {**bon, "texte": "35"},
                    {**bon, "repli_vide": True}):
        with pytest.raises(GardeArret):
            cp.exiger_remplacement_du_jumeau(mauvais, 8)
