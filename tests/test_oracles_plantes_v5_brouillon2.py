"""Lot B1, v5 — essais des choix du brouillon 2 du préenregistrement (`ba5ddf70…`) : gabarits partagés entre strates
(remarque 7 tranchée), P9 et base « forme seule », « retrouvée » par étages 1 et 2, sous-banque avec témoins servis
(dans `test_oracles_plantes_v5_banque.py`), graines [9] et [10] ; et remarque 19 (trouvée par l'exécutant : une
variable du préfixe citée dans le premier argument d'une fonction, dans un domaine, faisait lever une exception)."""
from fractions import Fraction

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.oracles_plantes_v5 import banque as banque_mod
from controle_ia.oracles_plantes_v5.evaluation import prefixe
from controle_ia.oracles_plantes_v5.forme_seule import (BayesNaif, aire_sous_la_courbe, analyse_forme, borne_naturelle,
                                                        ecarts_p9, mesurer, regle_forme_seule)
from controle_ia.oracles_plantes_v5.graines import generateur
from controle_ia.oracles_plantes_v5.normalisation import normaliser
from controle_ia.oracles_plantes_v5.parametres import STATUT_PROVISOIRE, charger
from controle_ia.oracles_plantes_v5.retrouvees import retrouvee, retrouvee_empreinte_seule
from controle_ia.oracles_plantes_v5.tests_de_mort import appliquer_batterie, sortie_de_texte, t2_contre_exemple

P, _ = charger()


@pytest.fixture(scope="module")
def banque11():
    return banque_mod.construire_banque(11, P)


def test_parametres_geles_et_part_provisoire():
    assert P["statut"] == STATUT_PROVISOIRE and "gelé" in P["statut"] and P["provisoire"]
    assert (P["familles"]["F1"]["borne_N"], P["familles"]["F2"]["borne_N"], P["familles"]["F3"]["borne_N"]) == (4, 10, 15)


# ---------------------------------------------------------------- gabarits partagés (remarque 7)
def test_formes_par_monde(banque11):
    for m, plantes in banque11:
        def seuils(e):
            return [p for p in plantes if p.etiquette == e and regle_forme_seule(m.analyser(p.texte))]
        assert len(seuils("VERITE_PLANTEE")) == 4 and len(seuils("FAUX_TOT")) == 2 and len(seuils("PIEGE")) == 4
        assert sum(borne_naturelle(m.analyser(p.texte)) for p in seuils("VERITE_PLANTEE")) >= 2


def test_p9_exacte_sur_la_banque(banque11):
    mes = mesurer(banque11, generateur(11, 10), 4, "1")
    assert ecarts_p9(mes) == []
    r = mes["regle_fixe"]
    assert (r["PIEGE"]["taux"], r["FAUX_TOT"]["taux"], r["VERITE_PLANTEE"]["taux"]) == ("1", "1/2", "1/2")


def test_p9_artefact_detecte():
    mes = {"regle_fixe": {"PIEGE": {"declares_faux": 47, "plantes": 48}, "FAUX_TOT": {"declares_faux": 24, "plantes": 48},
                          "VERITE_PLANTEE": {"declares_faux": 49, "plantes": 96}}}
    e = ecarts_p9(mes)
    assert len(e) == 2 and all(x.startswith("A1 (P9)") for x in e)


def test_plantation_refuse_une_proportion_de_seuils_fausse(monkeypatch, banque11):
    m, _ = banque11[8]
    vraies = m.gabarits_verites

    def sans_un_seuil(rng):
        g = vraies(rng)
        return [g[4]] + g[1:]  # une vérité seuil remplacée par une non-seuil (doublon refusé par T5 : autre repli)

    monkeypatch.setattr(m, "gabarits_verites", sans_un_seuil)
    with pytest.raises(GardeArret):
        banque_mod.planter(m, 11, P)


def test_plantation_refuse_trop_peu_de_bornes_naturelles(monkeypatch, banque11):
    m, _ = banque11[8]
    vraies = m.gabarits_verites

    def une_seule_naturelle(rng):
        g = vraies(rng)
        return [("u_au_dessus_de_u2", [f"pour tout n dans NAT, n >= 2 implique u(n) >= {m.u(2)}"])] + g[1:]

    monkeypatch.setattr(m, "gabarits_verites", une_seule_naturelle)
    with pytest.raises(GardeArret, match="borne naturelle"):
        banque_mod.planter(m, 11, P)


def test_verites_seuil_vraies_au_dela_de_3N(banque11):
    # raisons générales éprouvées jusqu'à 6N pour F2 et F3 (F1 : la variation totale est bornée à 3N + 2 pas)
    for m, plantes in banque11[4:]:
        for p in plantes:
            if p.etiquette == "VERITE_PLANTEE" and regle_forme_seule(m.analyser(p.texte)):
                assert not t2_contre_exemple(m.analyser(p.texte), m, 6 * m.N).tue(), (m.famille, p.gabarit)


@pytest.mark.parametrize("texte,attendu", [
    ("pour tout t dans NAT, vt(t) < 1", ("seuil", True)),
    ("pour tout t dans NAT, t >= 1 implique vt(t) > 0", ("seuil", True)),
    ("pour tout t dans NAT, 1/2 <= vt(t)", ("seuil", False)),
    ("pour tout t dans NAT, vt(t) <= K", ("seuil", True)),
    ("pour tout t dans NAT, vt(t) <= t * vt(1)", None),
    ("pour tout t dans NAT, vt(t) = 1/2", None),
    ("pour tout A dans PARTIES, PA(A) < 1", None),  # aucune variable NAT
    ("vt(1) < 1", None),
    ("pour tout t dans NAT, mod(t, 3) != 1", ("residu", False)),
])
def test_regle_forme_seule(banque11, texte, attendu):
    m, _ = banque11[0]
    f = m.analyser(texte)
    a = analyse_forme(f)
    if attendu is None:
        assert a is None and not regle_forme_seule(f)
    else:
        assert a[0] == attendu[0] and borne_naturelle(f) == attendu[1]


def test_aire_sous_la_courbe_exacte():
    assert aire_sous_la_courbe([3, 4], [1, 2]) == 1
    assert aire_sous_la_courbe([1], [1]) == Fraction(1, 2)
    assert aire_sous_la_courbe([1, 3], [2]) == Fraction(1, 2)
    assert aire_sous_la_courbe([], [1]) is None


def test_classifieur_de_style_exact_et_reproductible(banque11):
    a = mesurer(banque11, generateur(11, 10), 4, "1")["classifieur_de_style"]
    b = mesurer(banque11, generateur(11, 10), 4, "1")["classifieur_de_style"]
    assert a == b and "/" in a["aire_pieges_contre_verites"] or a["aire_pieges_contre_verites"] in ("0", "1")
    modele = BayesNaif(Fraction(1)).apprendre(["u(n) < 3", "u(n) = 3"], [True, False])
    assert isinstance(modele.score("u(n) < 4"), Fraction) and modele.score("u(n) < 4") > modele.score("u(n) = 4")


# ---------------------------------------------------------------- retrouvée : étages 1 et 2 seulement
def test_retrouvee_etages(banque11):
    m, plantes = banque11[8]
    verites = [normaliser(m.analyser(p.texte), m, m.ev) for p in plantes if p.etiquette == "VERITE_PLANTEE"]
    i_u = next(k for k, p in enumerate(x for x in plantes if x.etiquette == "VERITE_PLANTEE") if p.gabarit == "u_positive")

    def f(t):
        return normaliser(m.analyser(t), m, m.ev)
    assert retrouvee(f("pour tout k dans NAT, 0 < u(k)"), verites) == (i_u, 1)  # étage 1
    assert retrouvee(f("pour tout k dans NAT, u(k) > 0 et (u(k) > 0 ou k > 3)"), verites) == (i_u, 2)  # étage 2
    assert retrouvee(f("pour tout k dans NAT, u(k) >= 1"), verites) is None  # même profil, étage 3 exclu
    assert retrouvee_empreinte_seule(f("pour tout k dans NAT, u(k) > 0 et (u(k) > 0 ou k > 3)"), verites) is None


# ---------------------------------------------------------------- remarque 19
@pytest.mark.parametrize("texte", ["pour tout n dans NAT, pour tout k dans [0 .. w(n)], k >= 0",
                                   "pour tout n dans NAT, pour tout k dans [0 .. min(n, 3)], u(k) > 0"])
def test_r19_domaine_dependant_dans_un_argument(banque11, texte):
    m, _ = banque11[8]
    r = appliquer_batterie(sortie_de_texte(texte), m)  # v4 : KeyError dans le normaliseur
    assert r.statut == "vivante"
    pre, _ = prefixe(r.forme.arbre)
    assert len(pre) == 2
