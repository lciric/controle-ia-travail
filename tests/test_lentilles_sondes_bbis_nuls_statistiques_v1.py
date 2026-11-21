"""Essais des nuls, des statistiques et des audits (texte scellé, « Code neuf », essais « nuls et statistiques ») : graines,
normes, nul des signes, calibration (sain, × 1,5, bornes), familles, jeton de début, symétrie des pôles, valeurs non finies."""
from __future__ import annotations

import hashlib
import importlib.util
import subprocess

import numpy as np
import pytest

torch = pytest.importorskip("torch")

import lentilles_sondes_bbis_jouets_v1 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import audits_v1 as au  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lecture_v1 as le  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nuls_v1 as nu  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v1 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret  # noqa: E402

D, T, M = 64, 500, 400
ARG = ("P-S50", "e1", "sonde", "w")


# --- graines ----------------------------------------------------------------------------------------------------------------------------
def test_graine_selon_le_plan_point_3():
    cle = "lentilles-bbis/nul-isotrope/15"
    e = int.from_bytes(hashlib.sha256(cle.encode()).digest()[:8], "big")
    attendu = np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=207246359357165180107189867815730235805,
                                                                         spawn_key=(e,)))).standard_normal(5)
    g = nu.Graines()
    assert np.array_equal(g.rng(cle).standard_normal(5), attendu) and g.derivees == {cle: e}
    assert K.ENTROPIE == 207246359357165180107189867815730235805


def test_cles_des_graines_formes_du_plan():
    assert nu.cle_nul_isotrope(7) == "lentilles-bbis/nul-isotrope/7"
    assert nu.cle_nul_isotrope_par_direction(*ARG) == "lentilles-bbis/nul-isotrope-par-direction/P-S50/e1/sonde/w"
    assert nu.cle_nul_signes(*ARG) == "lentilles-bbis/nul-signes/P-S50/e1/sonde/w"
    assert nu.cle_temoins(7, K.NUL_ISOTROPE) == "lentilles-bbis/temoins-calibration/7/nul-isotrope/couche"
    assert nu.cle_temoins(7, K.NUL_SIGNES, *ARG) == "lentilles-bbis/temoins-calibration/7/nul-signes/P-S50/e1/sonde/w"
    assert (nu.cle_temoins(7, K.NUL_ISOTROPE_PAR_DIRECTION, *ARG)
            == "lentilles-bbis/temoins-calibration/7/nul-isotrope-par-direction/P-S50/e1/sonde/w")
    assert nu.cle_colonnes_garde(23) == "lentilles-bbis/colonnes-garde/23"
    assert nu.cle_essai("garde-lecture-logits-c7") == "lentilles-bbis/essai/garde-lecture-logits-c7"
    for faux in (lambda: nu.cle_temoins(7, K.NUL_ISOTROPE, *ARG), lambda: nu.cle_temoins(7, K.NUL_SIGNES),
                 lambda: nu.cle_temoins(7, "autre-nul", *ARG)):
        with pytest.raises(Arret):
            faux()


def test_graines_reproductibles_et_distinctes_par_cle():
    v = np.random.default_rng(1).standard_normal(D)
    a, b = nu.nul_isotrope(nu.Graines(), 7, D, M), nu.nul_isotrope(nu.Graines(), 7, D, M)
    assert np.array_equal(a, b) and a.dtype == np.float32 and a.shape == (D, M)
    assert not np.array_equal(a, nu.nul_isotrope(nu.Graines(), 15, D, M))
    assert not np.array_equal(a[:, :50], nu.temoins_isotropes(nu.Graines(), 7, D, 50))
    assert np.array_equal(nu.nul_signes(nu.Graines(), v, *ARG, M), nu.nul_signes(nu.Graines(), v, *ARG, M))
    assert not np.array_equal(nu.nul_signes(nu.Graines(), v, *ARG, M), nu.nul_signes(nu.Graines(), v, "P-S50", "e0", "sonde", "w", M))
    assert not np.array_equal(nu.nul_isotrope(nu.Graines(entropie=1), 7, D, M), a)
    assert np.array_equal(nu.colonnes_garde(nu.Graines(), 7, 500), nu.colonnes_garde(nu.Graines(), 7, 500))
    assert len(set(nu.colonnes_garde(nu.Graines(), 7, 500).tolist())) == 64


# --- normes ---------------------------------------------------------------------------------------------------------------------------------
def test_nul_isotrope_moyenne_quadratique_un():
    for u in (nu.nul_isotrope(nu.Graines(), 7, D, M), nu.temoins_isotropes(nu.Graines(), 7, D, 30)):
        assert np.allclose(np.sqrt(np.mean(u.astype(np.float64) ** 2, axis=0)), 1.0, atol=1e-6)


def test_nul_par_direction_a_la_norme_de_v():
    v = np.random.default_rng(2).standard_normal(D) * 3e-4
    for u in (nu.nul_isotrope_par_direction(nu.Graines(), v, *ARG, M), nu.temoins_isotropes_par_direction(nu.Graines(), v, 7, *ARG, 30)):
        assert np.allclose(np.linalg.norm(u.astype(np.float64), axis=0), np.linalg.norm(v), rtol=1e-5)


def test_nul_des_signes_memes_valeurs_absolues_et_meme_norme():
    v = np.random.default_rng(3).standard_normal(D) * np.geomspace(1e-3, 1e3, D)          # anisotrope, comme un `w` replié
    for u in (nu.nul_signes(nu.Graines(), v, *ARG, M), nu.temoins_signes(nu.Graines(), v, 7, *ARG, 30)):
        assert np.array_equal(np.abs(u), np.abs(v.astype(np.float32))[:, None] * np.ones((1, u.shape[1]), np.float32))
        assert np.allclose(np.linalg.norm(u.astype(np.float64), axis=0), np.linalg.norm(v.astype(np.float32).astype(np.float64)))
        signes = np.sign(u) * np.sign(v)[:, None]
        assert 0.45 < (signes > 0).mean() < 0.55 and not np.array_equal(signes[:, 0], signes[:, 1])


def test_valeur_non_finie_dans_un_nul_arret():
    v = np.ones(D)
    v[5] = np.nan
    with pytest.raises(Arret, match="valeur non finie"):
        nu.nul_signes(nu.Graines(), v, *ARG, 10)
    with pytest.raises(Arret, match="valeur non finie"):
        nu.nul_isotrope_par_direction(nu.Graines(), v, *ARG, 10)
    scores = torch.randn(20, 50)
    st.resumer_nul(scores, {})
    scores[3, 4] = float("inf")
    with pytest.raises(Arret, match="valeur non finie"):
        st.resumer_nul(scores, {})
    constante = torch.randn(20, 50)
    constante[7] = 1.0
    with pytest.raises(Arret, match="écart type nul"):
        st.resumer_nul(constante, {})


# --- bornes de calibration --------------------------------------------------------------------------------------------------------------------
def test_bornes_egales_aux_exemples_du_plan():
    assert au.parametres_beta(2000) == (100, 1901)
    assert au.bornes_calibration([1000]) == (23, 85)
    assert au.bornes_calibration([200]) == (1, 24)
    assert au.bornes_calibration([200] * 3) == (12, 53)
    assert au.bornes_calibration([200] * 5) == (26, 79)


def test_bornes_recalculees_par_le_programme_scelle_du_texte(tmp_path):
    """Le programme `bornes_calibration_beta_binomiale_v1.py` du texte (branche principale), s'il est joignable par git."""
    piece = "prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/bornes_calibration_beta_binomiale_v1.py"

    def lire(chemin: str) -> bytes | None:
        if (J.RACINE / chemin).is_file():
            return (J.RACINE / chemin).read_bytes()
        r = subprocess.run(["git", "show", f"origin/main:{chemin}"], cwd=J.RACINE, capture_output=True)
        return r.stdout if r.returncode == 0 else None
    source, compagnon = lire(piece), lire(piece + ".sha256")
    if source is None or compagnon is None:
        pytest.skip("programme des bornes du texte absent de cette branche et de origin/main")
    assert hashlib.sha256(source).hexdigest() == compagnon.decode().split()[0]
    chemin = tmp_path / "bornes.py"
    chemin.write_bytes(source)
    spec = importlib.util.spec_from_file_location("bornes_du_texte", chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for jeux in ([1000], [200], [200] * 3, [200] * 5, [600], [200] * 14):
        pmf = [1.0]
        for n in jeux:
            pmf = module.convoluer(pmf, module.pmf_beta_binomiale(n))
        assert au.bornes_calibration(jeux) == module.bornes(pmf), jeux


def test_bornes_risque_sous_le_niveau_de_chaque_cote():
    a, b = au.parametres_beta(2000)
    pmf = au.pmf_beta_binomiale(1000, a, b)
    bas, haut = au.bornes(pmf)
    assert sum(pmf[:bas]) <= 1e-4 < sum(pmf[:bas + 1]) and sum(pmf[haut + 1:]) <= 1e-4 < sum(pmf[haut:])
    assert abs(sum(pmf) - 1) < 1e-9


# --- calibration : nul sain, témoins × 1,5 ------------------------------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def lecture():
    g = torch.Generator().manual_seed(21)
    return {"wu": torch.randn(T, D, generator=g), "gamma": 1 + 0.2 * torch.randn(D, generator=g)}


def _p_temoins(lecture, nul, temoins, facteur=1.0):
    a_nul, _ = le.lire(torch.from_numpy(nul), None, lecture["gamma"], lecture["wu"])
    resume = st.resumer_nul(a_nul, {})
    s, _ = le.lire(torch.from_numpy(temoins), None, lecture["gamma"], lecture["wu"])
    return st.p_temoins(s * facteur, resume)


def test_calibration_nul_isotrope_sain_dans_les_bornes_et_temoins_fois_1_5_hors_des_bornes(lecture):
    nul, temoins = nu.nul_isotrope(nu.Graines(), 7, D, 2000), nu.temoins_isotropes(nu.Graines(), 7, D, 1000)
    sain = au.calibration([_p_temoins(lecture, nul, temoins)])
    assert (sain["q_bas"], sain["q_haut"], sain["n"]) == (23, 85, 1000) and sain["tenue"] is True
    assert sain["attendu"] == pytest.approx(1000 * 100 / 2001) and sain["borne_basse_volontairement_lache"] is False
    artefact = au.calibration([_p_temoins(lecture, nul, temoins, facteur=1.5)])
    assert artefact["tenue"] is False and artefact["compte_p_sous_0_05"] > artefact["q_haut"]


def test_calibration_nul_des_signes_sain_mis_en_commun_et_artefact(lecture):
    rng = np.random.default_rng(8)
    sains, artefacts = [], []
    for i in range(3):
        v = rng.standard_normal(D) * np.geomspace(0.1, 10, D)
        arg = ("P-S50", "e1", "sonde", f"w{i}")
        nul, temoins = nu.nul_signes(nu.Graines(), v, *arg, 2000), nu.temoins_signes(nu.Graines(), v, 7, *arg, 200)
        sains.append(_p_temoins(lecture, nul, temoins))
        artefacts.append(_p_temoins(lecture, nul, temoins, facteur=1.5))
    sain = au.calibration(sains)
    assert (sain["q_bas"], sain["q_haut"], sain["n"], sain["jeux"]) == (12, 53, 600, [200, 200, 200]) and sain["tenue"] is True
    assert au.calibration(artefacts)["tenue"] is False
    assert au.calibration(sains[:1])["borne_basse_volontairement_lache"] is True          # n < 600 : déclarée lâche


def test_p_des_temoins_egal_a_la_definition(lecture):
    nul, temoins = nu.nul_isotrope(nu.Graines(), 7, D, 300), nu.temoins_isotropes(nu.Graines(), 7, D, 40)
    a_nul, _ = le.lire(torch.from_numpy(nul), None, lecture["gamma"], lecture["wu"])
    resume = st.resumer_nul(a_nul, {})
    s, _ = le.lire(torch.from_numpy(temoins), None, lecture["gamma"], lecture["wu"])
    p = st.p_temoins(s, resume)
    for j in range(40):
        c = float(((s[:, j] - resume.moyenne) / resume.ecart_type).max())
        assert p[j] == pytest.approx((1 + int((resume.concentration >= c).sum())) / 301)


# --- statistiques d'une direction ----------------------------------------------------------------------------------------------------------------
def test_statistiques_egales_a_un_calcul_direct():
    g = torch.Generator().manual_seed(5)
    a_nul = torch.randn(T, M, generator=g)
    a = torch.randn(T, generator=g)
    a[17] += 9.0
    ids = np.arange(1000, 1000 + T)
    masques = {"nombres": torch.zeros(T, dtype=torch.bool), "cout": torch.zeros(T, dtype=torch.bool)}
    resume = st.resumer_nul(a_nul, masques)
    t = st.lecture_signe(a, {K.NUL_ISOTROPE: (a_nul, resume), K.NUL_SIGNES: (a_nul, resume)}, masques, ids)
    x, y = a.numpy().astype(np.float64), a_nul.numpy().astype(np.float64)
    m, s = y.mean(1), y.std(1)
    z = (x - m) / s
    haut = np.argsort(-x)[:20]
    assert t["premiers_par_score"]["rangs_gardes"] == haut.tolist() and t["premiers_par_score"]["ids"] == (1000 + haut).tolist()
    iso = t["nuls"][K.NUL_ISOTROPE]
    assert iso["concentration"] == pytest.approx(z.max(), rel=1e-4) and iso["m"] == M
    c_nul = ((y - m[:, None]) / s[:, None]).max(0)
    assert iso["p_concentration"] == pytest.approx((1 + (c_nul >= z.max() - 1e-9).sum()) / (M + 1)) == pytest.approx(1 / (M + 1))
    q = np.quantile(y, 0.99, axis=1)
    assert iso["part"] == pytest.approx((x[haut] > q[haut]).mean())
    part_nul = np.array([(y[np.argsort(-y[:, j])[:20], j] > q[np.argsort(-y[:, j])[:20]]).mean() for j in range(M)])
    assert iso["p_part"] == pytest.approx((1 + (part_nul >= iso["part"] - 1e-9).sum()) / (M + 1))
    assert iso["rang_empirique_des_premiers"] == [1 + int((y[i] > x[i]).sum()) for i in haut]
    assert iso["premiers_par_z"]["rangs_gardes"] == np.argsort(-z)[:20].tolist() and "premiers_par_z" not in t["nuls"][K.NUL_SIGNES]
    assert np.allclose(iso["z_des_premiers"], z[haut], rtol=1e-4)


def test_les_deux_signes_partagent_le_nul():
    g = torch.Generator().manual_seed(6)
    a_nul, a = torch.randn(T, M, generator=g), torch.randn(T, generator=g)
    resume = st.resumer_nul(a_nul, {})
    plus = st.lecture_signe(a, {K.NUL_SIGNES: (a_nul, resume)}, {}, np.arange(T))
    moins = st.lecture_signe(-a, {K.NUL_SIGNES: (a_nul, resume)}, {}, np.arange(T))
    assert moins["premiers_par_score"]["rangs_gardes"] == (-a).topk(20).indices.tolist()
    assert set(plus["premiers_par_score"]["rangs_gardes"]).isdisjoint(moins["premiers_par_score"]["rangs_gardes"])
    assert moins["nuls"][K.NUL_SIGNES]["concentration"] == pytest.approx(float(((-a - resume.moyenne) / resume.ecart_type).max()))


@pytest.mark.parametrize("p_iso,p_signes,attendu", [
    (0.001, 0.01, st.LIBELLE_CONCENTREE), (0.0005, 0.0005, st.LIBELLE_CONCENTREE), (0.0011, 0.01, st.LIBELLE_INTERMEDIAIRE),
    (0.001, 0.011, st.LIBELLE_INTERMEDIAIRE), (0.05, 0.05, st.LIBELLE_INTERMEDIAIRE), (0.051, 0.0005, st.LIBELLE_NON_DISTINCTE),
    (0.0005, 0.051, st.LIBELLE_NON_DISTINCTE), (0.5, 0.5, st.LIBELLE_NON_DISTINCTE)])
def test_libelles_aux_bords_des_niveaux(p_iso, p_signes, attendu):
    assert st.libelle(p_iso, p_signes) == attendu


def test_famille_sur_representee_aux_bords():
    assert st.sur_representee(0.01, 0.01) and not st.sur_representee(0.011, 0.001) and not st.sur_representee(0.001, 0.011)


# --- familles de jetons ------------------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("chaine,famille", [
    ("7", "nombres"), (" 12", "nombres"), ("2024 ", "nombres"), ("007\n", "nombres"), ("12a", None), ("1.5", None), ("-3", None),
    ("", None), ("  ", None), ("١٢", None), ("²", None), ("1\n2", None),
    (" cost", "cout"), ("Price", "cout"), ("$", "cout"), (" FEES ", "cout"), ("usd", "cout"), ("Cheaper", "cout"),
    ("costing", None), ("prix", None), ("coût", None), ("euro", None), ("$$", None), ("budgetary", None)])
def test_familles_sur_un_vocabulaire_jouet(chaine, famille):
    assert st.famille_de(chaine) == famille


def test_masques_et_comptes_de_familles():
    chaines = J.vocabulaire_jouet()
    masques = st.masques_familles(chaines)
    assert masques["nombres"].nonzero().squeeze(1).tolist() == [3, 4, 5] and masques["cout"].nonzero().squeeze(1).tolist() == [6, 7, 8, 9, 13]
    n = len(chaines)
    a = torch.zeros(n)
    a[[3, 4, 6, 8, 100]] = torch.tensor([9.0, 8.0, 7.0, 6.0, 5.0])
    a_nul = torch.randn(n, 300, generator=torch.Generator().manual_seed(1))
    resume = st.resumer_nul(a_nul, masques, k=5)
    bruit = a + 1e-3 * torch.randn(n, generator=torch.Generator().manual_seed(2))
    with pytest.raises(Arret, match="premiers jetons"):          # nul résumé sur vingt jetons, direction lue sur cinq : arrêt
        st.lecture_signe(bruit, {K.NUL_ISOTROPE: (a_nul, st.resumer_nul(a_nul, masques))}, masques, np.arange(n), k=5)
    t = st.lecture_signe(bruit, {K.NUL_ISOTROPE: (a_nul, resume)}, masques, np.arange(n), k=5)
    assert t["familles"] == {"nombres": {"n": 2}, "cout": {"n": 2}}
    f = t["nuls"][K.NUL_ISOTROPE]["familles"]
    haut = a_nul.topk(5, dim=0).indices
    assert f["nombres"]["attendu"] == pytest.approx(float(masques["nombres"][haut].sum(0).double().mean()))
    assert f["cout"]["p"] == pytest.approx((1 + int((masques["cout"][haut].sum(0) >= 2).sum())) / 301)


# --- jeton de début ------------------------------------------------------------------------------------------------------------------------------------
def test_jeton_de_debut_rang_rapporte():
    ids = np.array([11, 128000, 13, 14, 15])
    a = torch.tensor([5.0, 3.0, 4.0, 1.0, 2.0])
    assert st.jeton_de_debut(a, ids, a.topk(2).indices) == {"garde": True, "parmi_les_premiers": False, "rang": 3}
    assert st.jeton_de_debut(a, ids, a.topk(3).indices) == {"garde": True, "parmi_les_premiers": True, "rang": 3}
    assert st.jeton_de_debut(-a, ids, (-a).topk(3).indices)["rang"] == 3
    assert st.jeton_de_debut(a, np.array([1, 2, 3, 4, 5]), a.topk(2).indices) == {"garde": False, "parmi_les_premiers": False, "rang": None}
    assert st.lecture_signe(a, {}, {}, ids, k=2)["jeton_de_debut"]["rang"] == 3


# --- pôles alignés ----------------------------------------------------------------------------------------------------------------------------------------
def test_poles_alignes_et_symetrie_v_et_moins_v():
    g = torch.Generator().manual_seed(9)
    w_down = torch.randn(D, 120, generator=g)
    v = 3.0 * w_down[:, 17] - 0.2 * torch.randn(D, generator=g)                       # proche du pôle (17, +)
    nuls = {K.NUL_ISOTROPE: torch.from_numpy(nu.nul_isotrope(nu.Graines(), 7, D, M)),
            K.NUL_SIGNES: torch.from_numpy(nu.nul_signes(nu.Graines(), v.numpy(), *ARG, M))}
    plus, moins = st.poles_alignes(v, w_down, nuls), st.poles_alignes(-v, w_down, nuls)
    assert (plus["poles"][0]["neurone"], plus["poles"][0]["signe"]) == (17, "+") and len(plus["poles"]) == 10
    cos = (w_down.T @ v) / (w_down.norm(dim=0) * v.norm())
    assert plus["poles"][0]["cosinus"] == pytest.approx(float(cos[17]), rel=1e-5) == pytest.approx(plus["concentration"], rel=1e-5)
    assert [p["cosinus"] for p in plus["poles"]] == sorted((p["cosinus"] for p in plus["poles"]), reverse=True)
    assert plus["poles"][0]["rang_parmi_maxima_nuls"] == {K.NUL_ISOTROPE: 1, K.NUL_SIGNES: 1}
    assert plus["p"][K.NUL_ISOTROPE] == pytest.approx(1 / (M + 1))
    # le signe − rend les mêmes pôles, de signe opposé, et la même concentration
    assert [(p["neurone"], p["signe"]) for p in moins["poles"]] == [(p["neurone"], p["signe"]) for p in st.poles_opposes(plus["poles"])]
    assert moins["concentration"] == pytest.approx(plus["concentration"]) and moins["p"] == plus["p"]
    maxima = (w_down.T @ nuls[K.NUL_ISOTROPE] / (w_down.norm(dim=0)[:, None] * nuls[K.NUL_ISOTROPE].norm(dim=0)[None])).abs().max(0).values
    assert torch.allclose(plus["maxima_nuls"][K.NUL_ISOTROPE], maxima, atol=1e-6)


def test_poles_valeurs_non_finies_ou_norme_nulle_arret():
    w_down = torch.randn(D, 20, generator=torch.Generator().manual_seed(1))
    with pytest.raises(Arret):
        st.poles_alignes(torch.zeros(D), w_down, {})
    v = torch.ones(D)
    v[0] = float("nan")
    with pytest.raises(Arret):
        st.poles_alignes(v, w_down, {})


# --- comparaisons et vecteurs non calculables ---------------------------------------------------------------------------------------------------------------
def test_cosinus_jetons_communs_et_non_calculable():
    a = np.array([1.0, 0.0, 0.0])
    assert st.cosinus(a, a) == pytest.approx(1) and st.cosinus(a, -a) == pytest.approx(-1) and st.cosinus(a, [0, 2, 0]) == 0
    assert st.jetons_communs([1, 2, 3], [3, 4, 1]) == 2
    with pytest.raises(Arret):
        st.cosinus(a, np.zeros(3))
    assert st.vecteur_calculable(a) is None and st.vecteur_calculable(np.zeros(3)) == "norme nulle"
    assert st.vecteur_calculable(np.array([1.0, np.inf])) == "valeur non finie dans la direction"


# --- déclencheurs d'audit et relecture indépendante ---------------------------------------------------------------------------------------------------------
def _lectures(libelle_publique, libelle_logits=st.LIBELLE_NON_DISTINCTE, couche=23, memes=False):
    lignes = []
    for cellule in K.CELLULES:
        for pli in K.PLIS:
            for role in K.ROLES:
                for lentille, libelle in ((K.LENTILLE_PUBLIQUE, libelle_publique), (K.LENTILLE_LOGITS, libelle_logits)):
                    ids = list(range(20)) if memes or lentille == K.LENTILLE_PUBLIQUE else list(range(100, 120))
                    lignes.append({"sonde": f"{cellule}/{pli}/{role}", "role": role, "vecteur": "w", "signe": "+", "couche": couche,
                                   "lentille": lentille, "libelle": libelle, "ids": ids})
    return lignes


def test_declencheurs_sain_aucun_audit():
    lignes = _lectures(st.LIBELLE_NON_DISTINCTE)
    lignes[0]["libelle"] = st.LIBELLE_INTERMEDIAIRE
    d = au.declencheurs(lignes, [{"type": "plis", "cosinus": 0.5}, {"type": "sonde-lecteur", "cosinus": 0.9}])
    assert d["audit_a_jouer"] is False and d["trop_beau_declenche"] is False and d["tout_negatif_declenche"] is False


def test_declencheur_trop_beau_vingt_sondes_concentrees():
    assert au.declencheurs(_lectures(st.LIBELLE_CONCENTREE), [])["trop_beau"]["dix_sondes_et_dix_lecteurs_concentres"] is True
    presque = _lectures(st.LIBELLE_CONCENTREE)
    presque[0]["libelle"] = st.LIBELLE_INTERMEDIAIRE
    d = au.declencheurs(presque, [])
    assert d["trop_beau"]["dix_sondes_et_dix_lecteurs_concentres"] is False and d["audit_a_jouer"] is False
    par_les_logits = au.declencheurs(_lectures(st.LIBELLE_INTERMEDIAIRE, st.LIBELLE_CONCENTREE), [])
    assert par_les_logits["trop_beau"]["dix_sondes_et_dix_lecteurs_concentres"] is False       # la lentille publique seule compte


def test_declencheur_trop_beau_memes_vingt_jetons_aux_couches_7_ou_15():
    for couche, attendu in ((7, True), (15, True), (23, False)):
        d = au.declencheurs(_lectures(st.LIBELLE_INTERMEDIAIRE, couche=couche, memes=True), [])
        assert bool(d["trop_beau"]["memes_vingt_jetons_couches_7_ou_15"]) is attendu and d["audit_a_jouer"] is attendu
    assert au.declencheurs(_lectures(st.LIBELLE_INTERMEDIAIRE, couche=7), [])["audit_a_jouer"] is False


@pytest.mark.parametrize("paire,attendu", [
    ({"type": "plis", "cosinus": 0.9991}, True), ({"type": "doses", "cosinus": 0.9995}, True), ({"type": "plis", "cosinus": 0.999}, False),
    ({"type": "sonde-lecteur", "cosinus": 0.991}, True), ({"type": "sonde-lecteur", "cosinus": 0.99}, False),
    ({"type": "doses", "cosinus": 0.995}, False), ({"type": "plis", "cosinus": -0.9999}, False)])
def test_declencheur_trop_beau_cosinus(paire, attendu):
    assert au.declencheurs(_lectures(st.LIBELLE_INTERMEDIAIRE), [paire])["audit_a_jouer"] is attendu


def test_declencheur_tout_negatif():
    assert au.declencheurs(_lectures(st.LIBELLE_NON_DISTINCTE), [])["tout_negatif_declenche"] is True
    assert au.declencheurs(_lectures(st.LIBELLE_NON_DISTINCTE, st.LIBELLE_INTERMEDIAIRE), [])["tout_negatif_declenche"] is False
    assert au.declencheurs(_lectures(None, None), [])["tout_negatif_declenche"] is True


def test_relecture_par_un_chemin_independant():
    g = torch.Generator().manual_seed(4)
    wu, gamma, j = torch.randn(T, D, generator=g), 1 + 0.2 * torch.randn(D, generator=g), torch.eye(D) + 0.3 * torch.randn(D, D, generator=g)
    v = torch.randn(D, generator=g)
    scores, _ = le.lire(v, j, gamma, wu)
    relue = au.relire_par_chemin_independant(v.numpy(), j.numpy(), gamma.numpy(), wu.numpy())
    accord = au.comparer_relecture(scores[:, 0].numpy(), relue)
    assert accord["jetons_communs"] == 20 and accord["ecart_relatif_maximal"] < 1e-5
    autre = au.relire_par_chemin_independant(v.numpy(), None, gamma.numpy(), wu.numpy())      # autre lentille : désaccord vu
    assert au.comparer_relecture(scores[:, 0].numpy(), autre)["ecart_relatif_maximal"] > 1e-2
