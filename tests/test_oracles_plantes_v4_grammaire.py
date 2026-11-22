"""Lot B1 — grammaire, schéma, T1 (forme) : cas sains et artefacts (R5)."""
from fractions import Fraction

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.oracles_plantes_v4.exact import frac_depuis_texte
from controle_ia.oracles_plantes_v4.famille_f1 import MondeF1
from controle_ia.oracles_plantes_v4.famille_f3 import MondeF3
from controle_ia.oracles_plantes_v4.grammaire import FormeInvalide, analyser, imprimer, lire_sortie
from controle_ia.oracles_plantes_v4.normalisation import normaliser
from controle_ia.oracles_plantes_v4.parametres import charger
from controle_ia.oracles_plantes_v4.tests_de_mort import TypeIssue, sortie_de_texte, t1_forme

P, _ = charger()


@pytest.fixture(scope="module")
def f3():
    return MondeF3.tirer(np.random.default_rng(5), P["familles"]["F3"], P["capacites"])


@pytest.fixture(scope="module")
def f1():
    return MondeF1.tirer(np.random.default_rng(5), P["familles"]["F1"], P["capacites"])


SAINS_F3 = [
    "pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) = 3 * (-QU)^n",
    "pour tout n dans NAT, pour tout m dans NAT, m >= 1 implique u(n + m) = w(m) * u(n + 1) + QU * w(m - 1) * u(n)",
    "il existe n dans [0 .. N], u(n) < 0",
    "pour tout n dans NAT, (1 - PU - QU) * somme(k, 0, n, u(k)) = (PU - 1) * u(n + 1) - u(n + 2) + U1",
    "non (pour tout n dans [0 .. N], u(n) = 0)",
    "(u(1) = U1) et (u(0) = U0) ou faux",
    "pour tout n dans NAT, mod(u(n), 7) != 0.5",
]


@pytest.mark.parametrize("texte", SAINS_F3)
def test_t1_sain_et_aller_retour(f3, texte):
    iss, arbre, d = t1_forme(sortie_de_texte(texte), f3)
    assert iss.type == TypeIssue.CONFORME, iss.motif
    # l'imprimeur rend un texte réanalysable, de même forme normale (un littéral 1/2 revient en division 1 / 2)
    rearbre = f3.analyser(imprimer(arbre))
    assert normaliser(rearbre, f3, f3.ev).chaine == normaliser(arbre, f3, f3.ev).chaine


INFORMES_F3 = [
    ("pour tout n dans NAT, u(n) ≤ 3", "ASCII"),  # caractère hors alphabet
    ("pour tout n dans NAT, u(n) = x", "libre"),  # variable libre
    ("pour tout n dans NAT, il existe m dans NAT, u(m) > n", "NAT"),  # NAT hors du préfixe de tête
    ("u(1) = 1 implique pour tout n dans NAT, u(n) > 0", "NAT"),  # NAT après une hypothèse
    ("non (pour tout n dans NAT, u(n) = 0)", "NAT"),  # existentiel non borné déguisé
    ("pour tout n dans NAT, z(n) = 0", "inconnu"),  # fonction inconnue
    ("pour tout n dans NAT, u(n, n) = 0", "argument"),  # arité
    ("pour tout PU dans NAT, u(PU) = 0", "réservé"),  # variable qui masque une constante
    ("pour tout n dans NAT, pour tout n dans [0 .. 3], u(n) = 0", "déjà liée"),
    ("pour tout n dans NAT, u(n) < u(n + 1) < u(n + 2)", "enchaînées"),
    ("pour tout n dans NAT, u(n)", "comparaison"),
    ("", "vide"),
    ("pour tout n dans NAT u(n) = 0", "attendu"),
]


@pytest.mark.parametrize("texte,motif", INFORMES_F3)
def test_t1_artefacts_hors_grammaire(f3, texte, motif):
    iss, arbre, _ = t1_forme(sortie_de_texte(texte), f3)
    assert iss.type == TypeIssue.INFORME and arbre is None
    assert not iss.tue()  # « informe » n'est pas une mort


@pytest.mark.parametrize("sortie", [
    {"enonce": "u(0) = U0", "ce_qui_le_tuerait": "n", "confiance": "1/2", "autre": 1},  # clé en trop
    {"enonce": "u(0) = U0", "ce_qui_le_tuerait": "", "confiance": "1/2"},  # « ce qui le tuerait » vide
    {"enonce": "u(0) = U0", "ce_qui_le_tuerait": "n", "confiance": 0.5},  # flottant
    {"enonce": "u(0) = U0", "ce_qui_le_tuerait": "n", "confiance": True},
    {"enonce": "u(0) = U0", "ce_qui_le_tuerait": "n", "confiance": "3/2"},  # hors [0, 1]
    {"enonce": 3, "ce_qui_le_tuerait": "n", "confiance": "1/2"},
    '{"enonce": "u(0) = U0", "ce_qui_le_tuerait": "n", "confiance": NaN}',
    "pas du JSON",
    ["u(0) = U0"],
])
def test_t1_artefacts_hors_schema(f3, sortie):
    iss, arbre, _ = t1_forme(sortie, f3)
    assert iss.type == TypeIssue.INFORME and arbre is None


def test_schema_confiance_lue_exactement():
    d = lire_sortie('{"enonce": "u(0) = U0", "ce_qui_le_tuerait": "n = 0", "confiance": 0.7}')
    assert d["confiance"] == Fraction(7, 10) and isinstance(d["confiance"], Fraction)


def test_litteral_decimal_lu_exactement(f3):
    arbre = analyser("u(0) = 0.1", f3.vocabulaire())
    assert arbre[3] == ("num", Fraction(1, 10))


def test_frac_depuis_texte():
    assert frac_depuis_texte("-3/4") == Fraction(-3, 4)
    assert frac_depuis_texte("0.25") == Fraction(1, 4)
    with pytest.raises(GardeArret):
        frac_depuis_texte("1e-3")
    with pytest.raises(GardeArret):
        frac_depuis_texte(0.25)


def test_vocabulaire_par_monde(f1, f3):
    # le vocabulaire est propre au monde : u n'existe pas en F1, vt n'existe pas en F3
    assert t1_forme(sortie_de_texte("u(0) = 1"), f1)[0].type == TypeIssue.INFORME
    assert t1_forme(sortie_de_texte("vt(1) = 0"), f3)[0].type == TypeIssue.INFORME
    assert t1_forme(sortie_de_texte("vt(1) = 0"), f1)[0].type == TypeIssue.CONFORME


def test_profondeur_bornee(f3):
    texte = "u(0) = " + "(" * 200 + "1" + ")" * 200
    with pytest.raises(FormeInvalide):
        analyser(texte, f3.vocabulaire())
