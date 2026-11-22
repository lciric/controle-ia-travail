"""Lot B1 — évaluateur exact, calculs des familles, normaliseur, graines : cas sains et artefacts (R5)."""
import itertools
from fractions import Fraction

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.oracles_plantes_v4.evaluation import F, H, I, V, et3, ou3
from controle_ia.oracles_plantes_v4.exact import exact
from controle_ia.oracles_plantes_v4.famille_f1 import MondeF1
from controle_ia.oracles_plantes_v4.famille_f2 import MondeF2, extremes_au_moins, frechet
from controle_ia.oracles_plantes_v4.famille_f3 import MondeF3
from controle_ia.oracles_plantes_v4.graines import generateur, graine
from controle_ia.oracles_plantes_v4.normalisation import VRAI, normaliser
from controle_ia.oracles_plantes_v4.parametres import charger
from controle_ia.oracles_plantes_v4.tests_de_mort import t2_contre_exemple

P, _ = charger()
CAP = P["capacites"]


def monde(cls, fam, g=3):
    return cls.tirer(np.random.default_rng(g), P["familles"][fam], CAP)


# ---------------------------------------------------------------- flottant glissé dans un chemin de vérité
def test_flottant_refuse_dans_une_expression():
    m = monde(MondeF3, "F3")
    with pytest.raises(GardeArret):
        m.ev.expr(("num", 0.5), {})
    with pytest.raises(GardeArret):
        m.ev.expr(("var", "n"), {"n": 2.0})
    with pytest.raises(GardeArret):
        exact(True)


def test_flottant_refuse_dans_un_parametre_du_monde():
    m = monde(MondeF2, "F2")
    arbre = m.analyser("alpha(1) = 1/4")
    assert m.ev.formule(arbre, {}) in (V, F)  # cas sain : valeur exacte
    m.alpha[0] = 0.25  # artefact : paramètre flottant
    with pytest.raises(GardeArret):
        m.ev.formule(arbre, {})


def test_flottant_refuse_dans_une_constante():
    m = monde(MondeF3, "F3")
    m.AV = 1.5
    with pytest.raises(GardeArret):
        m.ev.formule(m.analyser("AV = 3/2"), {})


# ---------------------------------------------------------------- logique de Kleene, indéfini, capacité
def test_kleene_independant_de_l_ordre():
    for a, b in itertools.product((V, F, I, H), repeat=2):
        assert et3([a, b]) == et3([b, a]) and ou3([a, b]) == ou3([b, a])
    assert et3([F, I]) == F and ou3([V, I]) == V and et3([V, I]) == I and et3([I, H]) == H


def test_indefini_et_hypothese(f3=None):
    m = monde(MondeF3, "F3")
    # u(n - 1) indéfini en n = 0 : l'hypothèse n >= 1 protège l'instance (implication de Kleene)
    assert t2_contre_exemple(m.analyser("pour tout n dans NAT, n >= 1 implique u(n - 1) >= 0"), m).type.value \
        == "non_tuee_jusqu_a_N"
    iss = t2_contre_exemple(m.analyser("pour tout n dans NAT, u(n - 1) >= 0"), m)
    assert iss.tue() and iss.instance == {"n": 0} and "indéfini" in iss.motif


def test_hors_capacite_ne_tue_pas():
    m = monde(MondeF3, "F3")
    iss = t2_contre_exemple(m.analyser("pour tout n dans NAT, u(n * 100000) >= 0"), m)
    assert iss.type.value == "non_decidee" and not iss.tue()


# ---------------------------------------------------------------- F1 : variation totale exacte contre énumération brute
def test_vt_contre_enumeration_brute():
    m = MondeF1({"K": 4, "D": 12, "a": [1, 2, 4, 5], "b": [3, 3, 3, 3]}, 4, CAP)
    P_ = [Fraction(x, 12) for x in m.a]
    Q_ = [Fraction(x, 12) for x in m.b]
    for t in range(0, 4):
        brute = Fraction(0)
        for w in itertools.product(range(4), repeat=t):
            p = q = Fraction(1)
            for i in w:
                p *= P_[i]
                q *= Q_[i]
            brute += abs(p - q)
        assert m.vt(t) == brute / 2


def test_puissance_binomiale_exacte():
    m = MondeF1({"K": 4, "D": 12, "a": [1, 2, 4, 5], "b": [3, 3, 3, 3]}, 4, CAP)
    A = 0b0011
    q = Fraction(6, 12)
    assert m.appeler("puissance", (Fraction(A), Fraction(3), Fraction(2))) == 3 * q ** 2 * (1 - q) + q ** 3


# ---------------------------------------------------------------- F2 : programmation linéaire exacte contre Fréchet et grille
def test_lp_exacte_contre_frechet_et_grille():
    marges = [Fraction(3, 20), Fraction(7, 20)]
    lo, hi = extremes_au_moins(marges, 1)
    assert (lo, hi) == frechet(marges, 1, 2)
    # grille exacte pour m = 2 : p11 parcourt [max(0, a1 + a2 - 1), min(a1, a2)] ; P(OU) = a1 + a2 - p11
    vals = [marges[0] + marges[1] - Fraction(k, 400) for k in range(0, 61)]
    assert hi == max(vals) and lo == min(vals)
    m3 = [Fraction(1, 5), Fraction(3, 10), Fraction(1, 4)]
    for s in (1, 3):
        assert extremes_au_moins(m3, s) == frechet(m3, s, 3)
    lo2, hi2 = extremes_au_moins(m3, 2)
    assert lo2 == 0 and hi2 == min(Fraction(1), sum(m3) / 2)  # au moins 2 de 3 : borne de Markov atteinte ici


def test_recoupement_frechet_garde(monkeypatch):
    import controle_ia.oracles_plantes_v4.famille_f2 as f2
    monkeypatch.setattr(f2, "frechet", lambda marges, s, m: (Fraction(0), Fraction(1)))
    with pytest.raises(GardeArret):
        monde(MondeF2, "F2")


# ---------------------------------------------------------------- normaliseur : solidité des réécritures
def test_reecriture_recurrence_close_et_vraie():
    m = monde(MondeF3, "F3")
    texte = f"pour tout n dans NAT, u(n + 7) = {m.w(7)} * u(n + 1) + {m.QU * m.w(6)} * u(n)"
    f = m.analyser(texte)
    assert normaliser(f, m, m.ev).noeud == VRAI
    assert t2_contre_exemple(f, m, 3 * m.N).type.value == "non_tuee_jusqu_a_N"


def test_reecriture_affine_close_et_vraie():
    m = monde(MondeF3, "F3")
    f = m.analyser("pour tout n dans NAT, v(n + 2) = AV^2 * v(n) + BV * (AV + 1)")
    assert normaliser(f, m, m.ev).noeud == VRAI
    assert t2_contre_exemple(f, m, 3 * m.N).type.value == "non_tuee_jusqu_a_N"


def test_reecriture_seulement_sur_variable_nat():
    m = monde(MondeF3, "F3")
    # sur un intervalle qui descend sous zéro, la récurrence n'est pas dépliée (elle serait fausse en k = -2)
    f = m.analyser("pour tout k dans [-2 .. 3], u(k + 2) = PU * u(k + 1) + QU * u(k)")
    assert normaliser(f, m, m.ev).noeud != VRAI


def test_normalisation_preserve_la_semantique_sur_la_base_aleatoire():
    from controle_ia.oracles_plantes_v4.base_aleatoire import tirer_base
    for cls, fam in ((MondeF1, "F1"), (MondeF2, "F2"), (MondeF3, "F3")):
        m = monde(cls, fam)
        for t in tirer_base(np.random.default_rng(1), m, P["base_aleatoire"]):
            f = m.analyser(t)
            forme = normaliser(f, m, m.ev)
            a, b = t2_contre_exemple(f, m), t2_contre_exemple(forme.arbre, m)
            assert a.type == b.type
            if forme.noeud == VRAI:
                assert a.type.value in ("non_tuee_jusqu_a_N", "non_decidee")


# ---------------------------------------------------------------- graines
def test_graines_arbre_du_preenregistrement():
    racine = 123456789
    enfants = np.random.SeedSequence(racine).spawn(10)
    for i in range(10):
        assert list(graine(racine, i).generate_state(4)) == list(enfants[i].generate_state(4))
    assert generateur(racine, 0, 3, 0).integers(0, 10 ** 9) == generateur(racine, 0, 3, 0).integers(0, 10 ** 9)


@pytest.mark.parametrize("racine,chemin", [(5, (10,)), (5, ()), (-1, (0,)), (True, (0,)), (1.5, (0,))])
def test_graines_hors_arbre_refusees(racine, chemin):
    with pytest.raises(GardeArret):
        graine(racine, *chemin)
