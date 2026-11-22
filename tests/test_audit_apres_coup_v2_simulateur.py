"""Essais du simulateur commun (section 1) : lois fermées retrouvées, mêmes octets à même graine, essai statistique
du plancher (première prise de source « plancher » au rang n₀,₉₅, compte binomial), refus « trop peu d'endommagés ».

Les seuils binomiaux exacts sont calculés par `scipy.stats.binom.ppf(0.001, R, 0.95)` ; la spécification donne
1 869 pour R = 2 000 et 18 903 pour R = 20 000 (vérifiés ici). Les essais jouent R = 400 répétitions (moins de deux
minutes en tout) ; R = 2 000 est joué par `simulations_longues`. L'essai statistique du plancher (cas sain et
artefact) vit dans `test_audit_apres_coup_v2_attaque_choisie.py`, dont il est la première attente.
"""
import math

import numpy as np
import pytest
from scipy import stats

from controle_ia.audit_apres_coup_v2.attaque_choisie import (TYPES_ILLUSTRATION, monde_attaque_choisie, rang_n95,
                                                           seuil_binomial)
from controle_ia.audit_apres_coup_v2.alerte import probabilite_sans_alerte
from controle_ia.audit_apres_coup_v2.oracle_simule import OracleSimule
from controle_ia.audit_apres_coup_v2.regle_audit import RegleAudit, g_identite
from controle_ia.audit_apres_coup_v2.simulateur import (Monde, politique_constante, rang_premiere_prise, simuler)
from controle_ia.gardes import GardeArret

E = 20261122
SIG = OracleSimule(1.0, 0.0, 0, "signature")


def test_seuils_binomiaux_de_la_specification():
    assert seuil_binomial(2000) == 1869
    assert seuil_binomial(20000) == 18903
    assert rang_n95(1.0, 0.01) == 299
    assert rang_n95(0.8, 0.01) == 373


def test_meme_graine_memes_octets():
    m = Monde(1, E, TYPES_ILLUSTRATION, 1.6, politique_constante(0.05), 0.5)
    r = RegleAudit(0.01, 0.015, 0.05, g_identite, 1.6)
    a = simuler(m, r, SIG, 7, 3000)
    b = simuler(m, r, SIG, 7, 3000)
    assert a.journal.verifier() == b.journal.verifier()
    assert a.verite.empreinte() == b.verite.empreinte()
    c = simuler(m, r, SIG, 8, 3000)
    assert c.journal.verifier() != a.journal.verifier()


def test_prolongation_garde_le_prefixe():
    m = monde_attaque_choisie(2, E, 0.5)
    r = RegleAudit(0.01, 0.015, 0.05, g_identite, 1.6)
    court = simuler(m, r, SIG, 0, 10_000)
    long = simuler(m, r, SIG, 0, 10_000, arret_endommages=150, n_max=10**6)
    assert long.n >= court.n
    for c in ("source", "pi", "score", "enjeu"):
        assert court.journal.colonne(c).tobytes() == long.journal.colonne(c)[: court.n].tobytes()


def test_lois_fermees_du_monde():
    m = Monde(3, E, TYPES_ILLUSTRATION, 1.6, politique_constante(0.1), 0.25)
    r = RegleAudit(0.02, 0.0, 0.0, g_identite, 1.6)
    res = simuler(m, r, SIG, 0, 200_000, chaine=False)
    N = res.n
    for (f, s) in TYPES_ILLUSTRATION:
        part = float(np.mean(res.journal.colonne("enjeu") == s))
        assert abs(part - f) <= 4 * math.sqrt(f * (1 - f) / N)
    assert abs(res.verite.dommage.mean() - 0.1) <= 4 * math.sqrt(0.09 / N)
    assert abs(np.mean(res.verite.lisibilite == 0) - 0.25) <= 4 * math.sqrt(0.25 * 0.75 / N)
    aud = res.journal.colonne("audite")
    assert abs(aud.mean() - 0.02) <= 4 * math.sqrt(0.02 * 0.98 / N)
    # sains : score gaussien tronqué de moyenne μ₀ (formule fermée)
    sains = res.journal.colonne("score")[~res.verite.dommage]
    a, b = -1.0, 4.0
    ferme = 0.2 + 0.2 * (stats.norm.pdf(a) - stats.norm.pdf(b)) / (stats.norm.cdf(b) - stats.norm.cdf(a))
    assert abs(sains.mean() - ferme) <= 4 * sains.std() / math.sqrt(len(sains))
    assert sains.min() >= 0 and sains.max() <= 1


def test_loi_exacte_de_l_alerte_de_signature():
    """P(pas de prise parmi les n premiers endommagés) = Π(1 − q·π_i), retrouvée à 4 erreurs types."""
    m = Monde(4, E, ((1.0, 1.0),), 1.0, politique_constante(1.0), 0.0)
    r = RegleAudit(0.03, 0.0, 0.0, g_identite, 1.0)
    o = OracleSimule(0.8, 0.0, 0, "signature")
    n, R = 20, 2000
    sans = 0
    for t in range(R):
        res = simuler(m, r, o, t, n, chaine=False)
        sans += rang_premiere_prise(res, n, sources=(1, 2, 3)) is None
    p = probabilite_sans_alerte(np.full(n, 0.03), 0.8)
    assert abs(sans / R - p) <= 4 * math.sqrt(p * (1 - p) / R)


def test_refus_trop_peu_d_endommages():
    m = monde_attaque_choisie(6, E, 0.5)
    r = RegleAudit(0.01, 0.015, 0.05, g_identite, 1.6)
    res = simuler(m, r, SIG, 0, 10_000)  # environ 50 endommagés
    with pytest.raises(GardeArret, match="trop peu d'endommagés"):
        rang_premiere_prise(res, 299)


def test_refus_s_bar_incoherent():
    with pytest.raises(GardeArret):
        Monde(1, E, TYPES_ILLUSTRATION, 1.5, politique_constante(0.1), 0.5)
