"""Essais de la logique de décision du volet A (texte gelé v6), sur données synthétiques ; aucun modèle."""
import numpy as np

from controle_ia.neuron_lens import decisions_volet_a_v1 as da


def test_regle_couche():
    assert da.regle_couche([1, 1, 1, 0, 0]) == da.POSITIVE
    assert da.regle_couche([1, 0, 0, 0, 0]) == da.NEGATIVE
    assert da.regle_couche([1, 1, 0, 0, 0]) == da.INDECISE


def test_cas_sain_synthetique_rang_un():
    """Cas sain (iii) : le covecteur K(W_E[v0] − m) normé place v0 au rang 1 en `_z` ; sans lentille de même."""
    rng = np.random.default_rng(0)
    V, d = 400, 32
    E = rng.normal(size=(V, d))
    K = rng.normal(size=(d, d)) / np.sqrt(d)
    gardes = np.arange(V)
    for Kx in (K, None):
        F = da.empreintes(E, gardes, Kx)
        mu, sd = da.stats_reference(F, 1000, graine=1)
        v0 = 17
        w = F[v0] / np.linalg.norm(F[v0])
        assert da.rangs(da.lecture_z(F, w, mu, sd))[v0] == 1


def test_ramener_au_flux():
    w = da.ramener_au_flux([2.0, 0.0, 1.0], [2.0, 1.0, 0.5])
    assert np.isclose(np.linalg.norm(w), 1) and np.allclose(w / w[0], [1, 0, 2])


def test_a1():
    assert da.condition_a1(3, [50, 200, 11])
    assert not da.condition_a1(3, [50, 9])  # un témoin place P dans ses 10 premiers
    assert da.verdict_a1([da.POSITIVE, da.POSITIVE, da.NEGATIVE, da.INDECISE]) == "retrouvée"
    assert da.verdict_a1([da.NEGATIVE] * 4) == "non retrouvée"
    assert da.verdict_a1([da.POSITIVE, da.NEGATIVE, da.NEGATIVE, da.NEGATIVE]) == "partielle"


def test_a3_sans_objet_et_non_lue():
    so = {"chutes_sac": [0.01] * 5, "conditions": [False] * 5, "moins_que_moitie": [True] * 5}
    jug_non = {"chutes_sac": [0.1] * 5, "conditions": [False] * 5, "moins_que_moitie": [True] * 5}
    jug_lue = {"chutes_sac": [0.1] * 5, "conditions": [True] * 5, "moins_que_moitie": [False] * 5}
    assert da.verdict_a3([so, so, so, jug_non]) == da.SANS_OBJET  # une seule couche jugeable
    assert da.verdict_a3([so, so, jug_non, jug_non]) == "dépendance non lue"
    assert da.verdict_a3([so, jug_lue, jug_lue, jug_non]) == "dépendance lue"
    assert da.verdict_a3([jug_lue, jug_non, jug_non, jug_non]) == "indécise"


def test_s_fait_mieux_exige_couches_positives_de_a1():
    oui = [True] * 5
    non = [False] * 5
    cond = [oui, oui, non, non]
    assert da.s_fait_mieux(cond, [da.POSITIVE, da.POSITIVE, da.NEGATIVE, da.NEGATIVE])
    assert not da.s_fait_mieux(cond, [da.POSITIVE, da.NEGATIVE, da.POSITIVE, da.NEGATIVE])
    assert da.sans_lentille_au_moins_partout([non] * 4)


def test_verdict_i_priorites():
    args = dict(chaine_en_defaut=False, a1="retrouvée", sans_lentille_partout_a1=False, sans_lentille_partout_a2=False,
                a2_so=False, a3_par_contraste=["dépendance lue", da.SANS_OBJET], s_mieux_a1=True, s_mieux_a2=False)
    assert da.verdict_i(**args) == "apporte quelque chose"
    assert da.verdict_i(**{**args, "chaine_en_defaut": True}) == "chaîne en défaut"
    assert da.verdict_i(**{**args, "a3_par_contraste": ["dépendance non lue", da.SANS_OBJET]}) == "n'apporte rien"
    assert da.verdict_i(**{**args, "a3_par_contraste": [da.SANS_OBJET, da.SANS_OBJET]}) == "apporte quelque chose"
    # A2 sans objet : la clause « sans lentille ≥ S » se réduit à A1
    assert da.verdict_i(**{**args, "a2_so": True, "sans_lentille_partout_a1": True}) == "n'apporte rien"
    assert da.verdict_i(**{**args, "a1": "partielle"}) == "indéterminé"


def _couche(sonde_id, sonde_ood, nid, nood, bb):
    ks = (1, 8, 64, 512)
    return {"sonde_id": sonde_id, "sonde_ood": sonde_ood, "neurones_id": dict(zip(ks, nid)),
            "neurones_ood": dict(zip(ks, nood)), "borne_basse_ood": dict(zip(ks, bb))}


def test_aii():
    perd = _couche(0.9, 0.85, [0.6] * 4, [0.6] * 4, [-0.3] * 4)
    gagne = _couche(0.9, 0.85, [0.7, 0.8, 0.89, 0.9], [0.7, 0.8, 0.85, 0.86], [-0.2, -0.1, -0.03, 0.0])
    plafond = _couche(0.995, 0.995, [0.99] * 4, [0.99] * 4, [0.0] * 4)
    assert da.verdict_aii([perd] * 4) == "n'apporte rien"
    assert da.verdict_aii([gagne, gagne, perd, perd]) == "apporte"
    assert da.verdict_aii([plafond, plafond, plafond, gagne]) == da.SANS_OBJET
    assert da.verdict_aii([gagne, perd, perd, perd]) == "indéterminé"
    c3 = _couche(0.9, None, [0.6, 0.7, 0.89, 0.9], [None] * 4, [None] * 4)
    assert da.verdict_aii([c3, c3, c3, c3], a_un_hors_distribution=False) == "apporte"


def test_qualificatif():
    assert da.qualificatif_texte(0.80, 0.70, "C1") == "au-delà du texte"
    assert da.qualificatif_texte(0.71, 0.70, "C3") == "pas au-delà du texte"
    assert da.qualificatif_texte(0.99, 0.5, "C2") == da.SANS_OBJET
