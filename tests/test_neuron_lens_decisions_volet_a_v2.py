"""Essais de la logique de décision du volet A, v2 (texte gelé v6), sur données synthétiques ; aucun modèle."""
import numpy as np
import pytest

from controle_ia.neuron_lens import decisions_volet_a_v2 as da

OUI, NON = [True] * 5, [False] * 5


def test_regle_couche_et_garde():
    assert da.regle_couche([1, 1, 1, 0, 0]) == da.POSITIVE
    assert da.regle_couche([1, 0, 0, 0, 0]) == da.NEGATIVE
    assert da.regle_couche([1, 1, 0, 0, 0]) == da.INDECISE
    with pytest.raises(ValueError):
        da.regle_couche([1, 1, 1])


def _jeu(V=400, d=32, graine=0):
    rng = np.random.default_rng(graine)
    return rng.normal(size=(V, d)), rng.normal(size=(d, d)) / np.sqrt(d)


def test_cas_sain_synthetique_et_artefact():
    E, K = _jeu()
    gardes = np.arange(len(E))
    for Kx in (K, None):
        F = da.empreintes(E, gardes, Kx)
        mu, sd = da.stats_reference(F, graine=1)
        w = F[17] / np.linalg.norm(F[17])
        assert da.rangs(da.lecture_z(F, w, mu, sd))[17] == 1
    # artefact : covecteur construit avec une autre lentille → v0 n'est pas au rang 1
    _, K2 = _jeu(graine=5)
    F, F2 = da.empreintes(E, gardes, K), da.empreintes(E, gardes, K2)
    mu, sd = da.stats_reference(F, graine=1)
    w2 = F2[17] / np.linalg.norm(F2[17])
    assert da.rangs(da.lecture_z(F, w2, mu, sd))[17] > 1


def test_graine_obligatoire():
    E, K = _jeu()
    with pytest.raises((TypeError, ValueError)):
        da.stats_reference(da.empreintes(E, np.arange(len(E)), K))
    with pytest.raises(ValueError):
        da.stats_reference(da.empreintes(E, np.arange(len(E)), K), None)


def test_meilleur_rang_par_moins_w():
    E, K = _jeu()
    F = da.empreintes(E, np.arange(len(E)), K)
    mu, sd = da.stats_reference(F, graine=2)
    w = -F[30] / np.linalg.norm(F[30])  # P n'est retrouvé que par −w
    assert da.meilleur_rang_deux_signes(F, w, mu, sd, np.array([30])) == 1


def test_ramener_au_flux():
    w = da.ramener_au_flux([2.0, 0.0, 1.0], [2.0, 1.0, 0.5])
    assert np.isclose(np.linalg.norm(w), 1) and np.allclose(w / w[0], [1, 0, 2])
    with pytest.raises(ValueError):
        da.ramener_au_flux([1.0, np.nan], [1.0, 1.0])


def test_a1():
    t = [50] * 102
    assert da.condition_a1(3, t)
    assert not da.condition_a1(3, [50] * 101 + [9])
    assert not da.condition_a1(11, t)
    with pytest.raises(ValueError):
        da.condition_a1(3, [])
    assert da.verdict_a1([da.POSITIVE, da.POSITIVE, da.NEGATIVE, da.INDECISE]) == "retrouvée"
    assert da.verdict_a1([da.NEGATIVE] * 4) == "non retrouvée"
    assert da.verdict_a1([da.POSITIVE, da.NEGATIVE, da.NEGATIVE, da.NEGATIVE]) == "partielle"
    with pytest.raises(ValueError):
        da.verdict_a1([])


def test_a2():
    rng = np.random.default_rng(0)
    al = rng.uniform(-0.1, 0.1, size=100)
    assert da.condition_a2(0.5, al) and not da.condition_a2(0.0, al)
    with pytest.raises(ValueError):
        da.condition_a2(float("nan"), al)
    assert da.a2_sans_objet(0.59) and not da.a2_sans_objet(0.60)
    z = np.arange(10.0)
    assert np.isclose(da.rho_a2(z, z * 2, np.ones(10, bool)), 1.0)
    assert np.isclose(da.rho_a2(z, -z, np.ones(10, bool)), -1.0)


def test_a3():
    al = np.linspace(0, 0.01, 200)
    assert da.condition_a3(0.05, al, 0.08)
    assert not da.condition_a3(0.05, al, 0.11)  # < moitié du sac
    assert not da.condition_a3(0.005, al, 0.0)  # sous le 95ᵉ centile
    assert da.moins_que_moitie(0.05, 0.11) and not da.moins_que_moitie(0.05, 0.10)
    so = {"chutes_sac": [0.01] * 5, "conditions": NON, "moins_que_moitie": OUI}
    jn = {"chutes_sac": [0.1] * 5, "conditions": NON, "moins_que_moitie": OUI}
    jl = {"chutes_sac": [0.1] * 5, "conditions": OUI, "moins_que_moitie": NON}
    assert da.verdict_a3([so, so, so, jn]) == da.SANS_OBJET
    assert da.verdict_a3([so, so, jn, jn]) == "dépendance non lue"
    assert da.verdict_a3([so, jl, jl, jn]) == "dépendance lue"
    assert da.verdict_a3([jl, jn, jn, jn]) == "indécise"
    with pytest.raises(ValueError):
        da.verdict_a3([jn, jn])


def test_s_fait_mieux_et_sans_lentille():
    cond = [OUI, OUI, NON, NON]
    assert da.s_fait_mieux(cond, [da.POSITIVE, da.POSITIVE, da.NEGATIVE, da.NEGATIVE])
    assert not da.s_fait_mieux(cond, [da.POSITIVE, da.NEGATIVE, da.POSITIVE, da.NEGATIVE])
    with pytest.raises(ValueError):
        da.s_fait_mieux(cond, [da.POSITIVE] * 3)
    assert da.sans_lentille_au_moins_partout([NON] * 4)
    assert not da.sans_lentille_au_moins_partout([NON, NON, NON, OUI])


def test_verdict_i():
    a = dict(chaine_en_defaut=False, a1="retrouvée", sans_lentille_partout_a1=False, sans_lentille_partout_a2=False,
             a2_so=False, a3_par_contraste=["dépendance lue", da.SANS_OBJET], s_mieux_a1=True, s_mieux_a2=False)
    assert da.verdict_i(**a) == "apporte quelque chose"
    assert da.verdict_i(**{**a, "chaine_en_defaut": True}) == "chaîne en défaut"
    assert da.verdict_i(**{**a, "a1": "non retrouvée"}) == "n'apporte rien"
    assert da.verdict_i(**{**a, "a3_par_contraste": ["dépendance non lue", da.SANS_OBJET]}) == "n'apporte rien"
    assert da.verdict_i(**{**a, "a3_par_contraste": [da.SANS_OBJET, da.SANS_OBJET]}) == "apporte quelque chose"
    assert da.verdict_i(**{**a, "a2_so": True, "sans_lentille_partout_a1": True}) == "n'apporte rien"
    assert da.verdict_i(**{**a, "sans_lentille_partout_a1": True}) == "apporte quelque chose"  # A2 jugeable et non « ≥ »
    assert da.verdict_i(**{**a, "s_mieux_a1": False, "s_mieux_a2": True, "a2_so": True}) == "indéterminé"  # voie A2 fermée
    assert da.verdict_i(**{**a, "s_mieux_a1": False, "s_mieux_a2": True}) == "apporte quelque chose"
    assert da.verdict_i(**{**a, "a1": "partielle"}) == "indéterminé"


def _c(sid, sood, nid, nood, bb):
    ks = (1, 8, 64, 512)
    return {"sonde_id": sid, "sonde_ood": sood, "neurones_id": dict(zip(ks, nid)), "neurones_ood": dict(zip(ks, nood)),
            "borne_basse_ood": dict(zip(ks, bb))}


def test_aii():
    perd = _c(0.9, 0.85, [0.6] * 4, [0.6] * 4, [-0.3] * 4)
    gagne = _c(0.9, 0.85, [0.7, 0.8, 0.89, 0.9], [0.7, 0.8, 0.85, 0.86], [-0.2, -0.1, -0.03, 0.0])
    plafond = _c(0.995, 0.995, [0.99] * 4, [0.99] * 4, [0.0] * 4)
    assert da.verdict_aii([perd] * 4) == "n'apporte rien"
    assert da.verdict_aii([gagne, gagne, perd, perd]) == "apporte"
    assert da.verdict_aii([plafond, plafond, plafond, gagne]) == da.SANS_OBJET
    assert da.verdict_aii([gagne, perd, perd, perd]) == "indéterminé"
    borne = _c(0.9, 0.85, [0.6, 0.6, 0.89, 0.6], [0.6] * 4, [-0.3, -0.3, -0.05, -0.3])  # −0,05 exact : admis
    assert da.verdict_aii([borne, borne, perd, perd]) == "apporte"
    c3 = _c(0.9, None, [0.6, 0.7, 0.89, 0.9], [None] * 4, [None] * 4)
    assert da.verdict_aii([c3] * 4, a_un_hors_distribution=False) == "apporte"
    # plafond en distribution seul : la couche ne se juge que hors distribution
    pid = _c(0.995, 0.80, [0.5] * 4, [0.79, 0.79, 0.79, 0.79], [-0.04] * 4)
    assert da.verdict_aii([pid, pid, perd, perd]) == "apporte"
    with pytest.raises(ValueError):
        da.verdict_aii([perd] * 3)
    with pytest.raises(ValueError):
        da.verdict_aii([_c(float("nan"), 0.8, [0.5] * 4, [0.5] * 4, [0.0] * 4)] + [perd] * 3)


def test_qualificatif():
    assert da.qualificatif_texte(0.80, 0.70, "C1") == "au-delà du texte"
    assert da.qualificatif_texte(0.71, 0.70, "C3") == "pas au-delà du texte"
    assert da.qualificatif_texte(0.99, 0.5, "C2") == da.SANS_OBJET


def test_audit_volet_a():
    assert da.audit_volet_a([1, 1, 1, 1], False, "retrouvée", "apporte", "apporte") == ["trop beau"]
    assert da.audit_volet_a([1, 3, 1, 1], True, "retrouvée", "apporte", "apporte") == ["trop beau"]
    assert da.audit_volet_a([40, 50, 60, 70], False, "non retrouvée", "n'apporte rien", "n'apporte rien") == ["tout négatif"]
    assert da.audit_volet_a([40, 50, 60, 70], False, "non retrouvée", "n'apporte rien", "indéterminé") == []
