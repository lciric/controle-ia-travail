"""Lot B1 — tests de mort T2 à T6 et registre de lignée : cas sains et artefacts (R5)."""
import json

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.oracles_plantes_v1.famille_f1 import MondeF1
from controle_ia.oracles_plantes_v1.famille_f2 import MondeF2
from controle_ia.oracles_plantes_v1.famille_f3 import MondeF3
from controle_ia.oracles_plantes_v1.lignee import Registre, rejouer
from controle_ia.oracles_plantes_v1.normalisation import normaliser
from controle_ia.oracles_plantes_v1.parametres import charger
from controle_ia.oracles_plantes_v1.tests_de_mort import (TypeIssue, appliquer_batterie, sortie_de_texte,
                                                          t2_contre_exemple, t3_vacuite, t4_trivialite, t5_redite,
                                                          t6_verifier)

P, _ = charger()
CAP = P["capacites"]


def _monde(cls, fam, g=7):
    m = cls.tirer(np.random.default_rng(g), P["familles"][fam], CAP)
    rng = np.random.default_rng(g + 1000)
    m.perturbes = [m.perturbe(rng) for _ in range(3)]
    return m


@pytest.fixture(scope="module")
def f1():
    return _monde(MondeF1, "F1")


@pytest.fixture(scope="module")
def f2():
    return _monde(MondeF2, "F2")


@pytest.fixture(scope="module")
def f3():
    return _monde(MondeF3, "F3")


def forme(m, texte):
    return normaliser(m.analyser(texte), m, m.ev)


# ---------------------------------------------------------------- T2
def test_t2_sain_verite_non_tuee(f3):
    iss = t2_contre_exemple(f3.analyser("pour tout n dans NAT, u(n) <= max(U0, U1) * (PU + QU)^n"), f3)
    assert iss.type == TypeIssue.NON_TUEE and not iss.tue()


def test_t2_artefact_faux_tue_avec_instance(f3):
    iss = t2_contre_exemple(f3.analyser("pour tout n dans NAT, u(n) < u(3)"), f3)
    assert iss.type == TypeIssue.MORTE_CONTRE_EXEMPLE and iss.instance is not None
    assert int(iss.instance["n"]) <= f3.N
    assert isinstance(iss.type, TypeIssue) and not isinstance(iss, bool)  # issue typée, jamais un booléen nu


def test_t2_borne_respectee(f3):
    # vrai jusqu'à N, faux en N + 1 : non tué à la borne N, tué à 3N
    texte = f"pour tout n dans NAT, n <= {f3.N}"
    assert t2_contre_exemple(f3.analyser(texte), f3).type == TypeIssue.NON_TUEE
    iss = t2_contre_exemple(f3.analyser(texte), f3, 3 * f3.N)
    assert iss.tue() and int(iss.instance["n"]) == f3.N + 1


def test_t2_contradiction_avec_les_definitions(f3):
    texte = "pour tout n dans NAT, u(n + 2) != PU * u(n + 1) + QU * u(n)"
    f = f3.analyser(texte)
    assert t2_contre_exemple(f, f3, forme=forme(f3, texte)).tue()


# ---------------------------------------------------------------- T3
def test_t3_sain_hypotheses_satisfiables(f3):
    iss = t3_vacuite(f3.analyser("pour tout n dans NAT, n >= 1 implique u(n) > 0"), f3)
    assert iss.type == TypeIssue.NON_VACUE


def test_t3_sans_objet(f3):
    assert t3_vacuite(f3.analyser("pour tout n dans NAT, u(n) > 0"), f3).type == TypeIssue.SANS_OBJET


def test_t3_artefact_hypotheses_insatisfiables(f3):
    texte = f"pour tout n dans NAT, n > N + 5 implique u(n) = 0"
    iss = t3_vacuite(f3.analyser(texte), f3)
    assert iss.type == TypeIssue.MORTE_VACUITE and iss.tue()
    r = appliquer_batterie(sortie_de_texte(texte), f3)
    assert r.statut == "morte" and r.issues[-1].type == TypeIssue.MORTE_VACUITE


def test_t3_artefact_domaine_vide(f3):
    iss = t3_vacuite(f3.analyser("pour tout k dans [3 .. 1], u(k) = 0"), f3)
    assert iss.type == TypeIssue.MORTE_VACUITE


def test_t3_hypotheses_en_chaine(f3):
    texte = "pour tout n dans NAT, n >= 2 implique (n <= 1 implique u(n) = 0)"
    assert t3_vacuite(f3.analyser(texte), f3).type == TypeIssue.MORTE_VACUITE


# ---------------------------------------------------------------- T4
@pytest.mark.parametrize("texte", [
    "u(4) = PU * u(3) + QU * u(2)",  # instance littérale d'une définition
    "pour tout k dans NAT, u(k + 2) = QU * u(k) + PU * u(k + 1)",  # définition renommée et réordonnée
    "1 = w(1)",
    "pour tout n dans NAT, u(n + 5) = u(n + 5)",
])
def test_t4_artefact_trivial(f3, texte):
    f = f3.analyser(texte)
    assert t4_trivialite(normaliser(f, f3, f3.ev), f, f3).type == TypeIssue.TRIVIALE


def test_t4_instance_d_axiome_par_substitution(f2, f1):
    for m, texte in ((f2, "0 = pfa_t(MAJ, 0)"), (f2, "pfa_t(ET, 0) = 0"), (f1, "vt(0) >= 0"),
                     (f1, "pour tout B dans PARTIES, pour tout t dans NAT, fa(B, t, 0) = 1")):
        f = m.analyser(texte)
        iss = t4_trivialite(normaliser(f, m, m.ev), f, m)
        assert iss.type == TypeIssue.TRIVIALE, (texte, iss.motif)


@pytest.mark.parametrize("texte", [
    "pour tout n dans NAT, u(n) <= max(U0, U1) * (PU + QU)^n",
    "pour tout n dans NAT, n >= 1 implique w(2 * n) = w(n) * (w(n + 1) + QU * w(n - 1))",
])
def test_t4_sain_non_trivial(f3, texte):
    f = f3.analyser(texte)
    assert t4_trivialite(normaliser(f, f3, f3.ev), f, f3).type == TypeIssue.NON_TRIVIALE


# ---------------------------------------------------------------- T5
BASE = "pour tout n dans NAT, pour tout m dans NAT, m >= 1 implique u(n + m) = w(m) * u(n + 1) + QU * w(m - 1) * u(n)"
REFORMULATIONS = [
    # renommage
    "pour tout a dans NAT, pour tout b dans NAT, b >= 1 implique u(a + b) = w(b) * u(a + 1) + QU * w(b - 1) * u(a)",
    # permutation du préfixe et des membres
    "pour tout m dans NAT, pour tout n dans NAT, 1 <= m implique w(m) * u(n + 1) + w(m - 1) * u(n) * QU = u(m + n)",
    # double négation et contraposée
    "pour tout n dans NAT, pour tout m dans NAT, non (non (non (u(n + m) = w(m) * u(n + 1) + QU * w(m - 1) * u(n)) "
    "implique m < 1))",
]


@pytest.mark.parametrize("texte", REFORMULATIONS)
def test_t5_artefact_reformulation_equivalente(f3, texte):
    iss = t5_redite(forme(f3, texte), f3, [forme(f3, BASE)])
    assert iss.type == TypeIssue.REDITE and "forme normale" in iss.motif


def test_t5_reordonnancement_de_conjonctions(f2):
    a = "(pour tout j dans MONITEURS, alpha(j) <= mfa(OU)) et (il existe j dans MONITEURS, alpha(j) = mfa(OU))"
    b = "(il existe k dans MONITEURS, mfa(OU) = alpha(k)) et (pour tout i dans MONITEURS, mfa(OU) >= alpha(i))"
    assert t5_redite(forme(f2, b), f2, [forme(f2, a)]).type == TypeIssue.REDITE


def test_t5_equivalence_propositionnelle(f3):
    a = "pour tout n dans NAT, u(n) > 2 et (u(n) < 900 ou n > 3)"
    b = "pour tout n dans NAT, (u(n) > 2 et u(n) < 900) ou (n > 3 et u(n) > 2)"
    fa, fb = forme(f3, a), forme(f3, b)
    assert fa.empreinte != fb.empreinte
    iss = t5_redite(fb, f3, [fa])
    assert iss.type == TypeIssue.REDITE and "table de vérité" in iss.motif


def test_t5_profil_de_verite(f3):
    a = "pour tout n dans NAT, u(n) <= 50"
    b = "pour tout n dans NAT, u(n) < 51"  # équivalent sur les entiers ; le normaliseur ne le voit pas
    fa, fb = forme(f3, a), forme(f3, b)
    assert fa.empreinte != fb.empreinte
    iss = t5_redite(fb, f3, [fa])
    assert iss.type == TypeIssue.REDITE and "profil" in iss.motif


def test_t5_sain_deux_verites_distinctes(f3):
    a = f"pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) = {f3.U1 ** 2 - f3.U0 * f3.u(2)} * (-QU)^n"
    b = "pour tout n dans NAT, u(n) <= max(U0, U1) * (PU + QU)^n"
    c = "pour tout n dans NAT, (AV - 1) * v(n) = AV^n * ((AV - 1) * V0 + BV) - BV"
    assert t5_redite(forme(f3, b), f3, [forme(f3, a)]).type == TypeIssue.NON_REDITE
    assert t5_redite(forme(f3, c), f3, [forme(f3, a), forme(f3, b)]).type == TypeIssue.NON_REDITE


# ---------------------------------------------------------------- T6
def _s(verdict, instances):
    return json.dumps({"verdict": verdict, "contre_exemples": instances, "raison": "essai"})


def test_t6_vrai_contre_exemple_accepte(f3):
    f = f3.analyser("pour tout n dans NAT, u(n) < u(3)")
    iss = t6_verifier(_s("faux", [{"n": 3}]), f, f3)
    assert iss.type == TypeIssue.CONTRE_EXEMPLE_VERIFIE and iss.tue()


def test_t6_contre_exemple_au_dela_de_N_accepte_jusqu_a_3N(f3):
    f = f3.analyser(f"pour tout n dans NAT, n <= {f3.N}")
    assert t6_verifier(_s("faux", [{"n": f3.N + 1}]), f, f3).type == TypeIssue.CONTRE_EXEMPLE_VERIFIE


def test_t6_faux_contre_exemple_refuse(f3):
    f = f3.analyser("pour tout n dans NAT, u(n) < u(3)")
    iss = t6_verifier(_s("faux", [{"n": 0}, {"n": 1}]), f, f3)
    assert iss.type == TypeIssue.REFUTATION_FAUSSE and not iss.tue()


@pytest.mark.parametrize("instance", [{"n": -1}, {"n": 3 * 15 + 1}, {"n": 10 ** 9}])
def test_t6_hors_domaine_refuse(f3, instance):
    f = f3.analyser("pour tout n dans NAT, u(n) < 0")  # faux partout : seul le domaine peut refuser
    iss = t6_verifier(_s("faux", [instance]), f, f3, plafond=3 * 15)
    assert iss.type == TypeIssue.REFUTATION_FAUSSE and "hors_domaine" in iss.detail[0]


def test_t6_hors_domaine_nomme_refuse(f1):
    f = f1.analyser("pour tout A dans PARTIES, PA(A) < 0")
    iss = t6_verifier(_s("faux", [{"A": f1.PLEIN + 1}]), f, f1)
    assert iss.type == TypeIssue.REFUTATION_FAUSSE
    assert t6_verifier(_s("faux", [{"A": f1.PLEIN}]), f, f1).type == TypeIssue.CONTRE_EXEMPLE_VERIFIE


@pytest.mark.parametrize("instance", [{"m": 3}, {"n": 3, "m": 1}, {"n": "3"}, {"n": 3.0}, {"n": True}, [3]])
def test_t6_instance_informe_refusee(f3, instance):
    f = f3.analyser("pour tout n dans NAT, u(n) < u(3)")
    assert t6_verifier(_s("faux", [instance]), f, f3).type == TypeIssue.REFUTATION_FAUSSE


def test_t6_sans_refutation_et_sortie_informe(f3):
    f = f3.analyser("pour tout n dans NAT, u(n) < u(3)")
    assert t6_verifier(_s("vrai", []), f, f3).type == TypeIssue.SANS_REFUTATION
    assert t6_verifier('{"verdict": "faux"}', f, f3).type == TypeIssue.SORTIE_S_INFORME
    assert t6_verifier(_s("peut-etre", []), f, f3).type == TypeIssue.SORTIE_S_INFORME


def test_t6_intervalle_dependant(f1):
    f = f1.analyser("pour tout t dans NAT, pour tout s dans [0 .. t], s <= 2")
    assert t6_verifier(_s("faux", [{"t": 3, "s": 3}]), f, f1).type == TypeIssue.CONTRE_EXEMPLE_VERIFIE
    assert t6_verifier(_s("faux", [{"t": 2, "s": 3}]), f, f1).type == TypeIssue.REFUTATION_FAUSSE  # s hors [0 .. t]


# ---------------------------------------------------------------- lignée
def test_lignee_morte_reste_morte_par_reformulation(f3, tmp_path):
    reg = Registre(tmp_path / "lignee.jsonl")
    r1 = appliquer_batterie(sortie_de_texte("pour tout n dans NAT, u(n) < u(3)"), f3, registre=reg)
    assert r1.statut == "morte"
    r2 = appliquer_batterie(sortie_de_texte("pour tout k dans NAT, u(3) > u(k)"), f3, registre=reg)
    assert r2.statut == "morte" and r2.issues[-1].type == TypeIssue.MORTE_PAR_HERITAGE
    assert rejouer(tmp_path / "lignee.jsonl")[r1.forme.empreinte] == "morte"


def test_lignee_mort_par_t6_heritee(f3, tmp_path):
    # un piège vivant jusqu'à N, tué par un contre-exemple vérifié de S, reste mort pour toute reformulation
    reg = Registre(tmp_path / "l.jsonl")
    texte = f"pour tout n dans NAT, n <= {f3.N}"
    r = appliquer_batterie(sortie_de_texte(texte), f3, registre=reg)
    assert r.statut == "vivante"
    iss = t6_verifier(_s("faux", [{"n": f3.N + 2}]), r.arbre, f3)
    assert iss.tue()
    reg.inscrire(r.forme.empreinte, "morte", "T6", iss.motif)
    r2 = appliquer_batterie(sortie_de_texte(f"pour tout q dans NAT, {f3.N} >= q"), f3, registre=reg)
    assert r2.statut == "morte"


def test_lignee_refuse_resurrection(tmp_path):
    reg = Registre(tmp_path / "l.jsonl")
    reg.inscrire("a" * 64, "morte", "T2", "contre-exemple")
    with pytest.raises(GardeArret):
        reg.inscrire("a" * 64, "vivante", "batterie", "non tuée")


@pytest.mark.parametrize("alteration", ["supprimer", "modifier", "reordonner"])
def test_lignee_chaine_alteree_refusee(tmp_path, alteration):
    ch = tmp_path / "l.jsonl"
    reg = Registre(ch)
    for k in range(3):
        reg.inscrire(str(k) * 64, "vivante", "batterie", "non tuée")
    lignes = ch.read_text(encoding="utf-8").splitlines()
    if alteration == "supprimer":
        lignes = lignes[:1] + lignes[2:]
    elif alteration == "modifier":
        lignes[1] = lignes[1].replace("vivante", "morte")
    else:
        lignes[0], lignes[1] = lignes[1], lignes[0]
    ch.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        Registre(ch)


def test_lignee_rejouable(tmp_path):
    ch = tmp_path / "l.jsonl"
    reg = Registre(ch)
    reg.inscrire("b" * 64, "vivante", "batterie", "non tuée")
    reg.inscrire("b" * 64, "morte", "T6", "contre-exemple vérifié")
    reg.inscrire("c" * 64, "vivante", "batterie", "non tuée")
    assert rejouer(ch) == {"b" * 64: "morte", "c" * 64: "vivante"}
    assert Registre(ch).dernier == reg.dernier
