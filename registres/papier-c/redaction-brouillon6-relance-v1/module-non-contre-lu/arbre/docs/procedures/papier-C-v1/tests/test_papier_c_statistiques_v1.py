"""Essais des fonctions statistiques du papier C (v1) : rééchantillonnage, intervalles, valeurs p, lois, rangs.
Données simulées seulement. Chaque garde est éprouvée sur un cas sain et sur un artefact (R5)."""
import math

import numpy as np
import pytest

import papier_c_lois_v1 as lois
import papier_c_rangs_v1 as rg
import papier_c_reechantillonnage_v1 as re_
from papier_c_erreurs_v1 import ConfigurationInvalide


# --- poids -------------------------------------------------------------------------------------------------------
def test_comptes_par_grappes_une_tache_porte_ses_contenus():
    grappes = np.repeat(np.arange(10), 2)
    C = re_.comptes_par_grappes(grappes, 500, np.random.default_rng(0))
    assert C.shape == (500, 20)
    assert np.array_equal(C[:, 0::2], C[:, 1::2])              # les deux contenus d'une tâche reçoivent le même compte
    assert np.all(C[:, 0::2].sum(1) == 10)                     # G grappes tirées avec remise


def test_poids_jackknife_retire_une_grappe_entiere():
    J = re_.poids_jackknife(np.array(["a", "a", "b", "c", "c"]))
    assert J.tolist() == [[0, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 0]]


def test_comptes_refuse_zero_tirage():
    with pytest.raises(ConfigurationInvalide):
        re_.comptes_par_grappes(np.arange(5), 0, np.random.default_rng(0))


# --- valeurs p par décompte (point 12) ---------------------------------------------------------------------------
def test_valeurs_p_par_decompte_formule_du_texte():
    t = np.array([0.1, 0.4, 0.5, 0.6, 0.9])
    assert re_.p_superieur(t, 0.5) == (1 + 3) / 6             # (1 + #{θ* ≤ θ0}) / (B + 1)
    assert re_.p_inferieur(t, 0.5) == (1 + 3) / 6             # (1 + #{θ* ≥ θ0}) / (B + 1)
    assert re_.p_bilateral(np.array([1.0, 2.0, 3.0]), 0.0) == min(1.0, 2 * (1 / 4))
    assert re_.p_bilateral(t, 0.5) == 1.0


def test_tirages_tous_au_dessus_de_la_frontiere_concluent_vers_la_cible():
    """Test du module écrit au point 12 : tirages tous au-dessus de 0,5 → « vers la cible »."""
    tirages = np.full(9999, 0.7)
    p = re_.p_superieur(tirages, 0.5)
    assert p == 1 / 10000 and p <= 0.025
    assert re_.p_inferieur(tirages, 0.5) == 1.0


def test_holm_cas_construits():
    assert re_.holm([0.01, 0.04, 0.03, 0.5]) == pytest.approx([0.04, 0.09, 0.09, 0.5])
    assert re_.holm([0.005] * 5) == pytest.approx([0.025] * 5)            # au seuil de C-P2 : 0,025 exactement
    assert re_.holm([0.9, 0.8]) == [1.0, 1.0]
    assert re_.holm([]) == []


# --- intervalles : BCa et repli consigné (point 11) --------------------------------------------------------------
def _moyenne(P, x):
    return (P @ x) / P.sum(1)


def test_bca_cas_sain_et_niveau():
    rng = np.random.default_rng(1)
    x = rng.normal(0, 1, 40)
    g = np.arange(40)
    ic = re_.intervalle_bca(float(x.mean()), _moyenne(re_.comptes_par_grappes(g, 4000, rng), x),
                            _moyenne(re_.poids_jackknife(g), x), 0.95)
    assert ic["methode"] == "BCa" and ic["motif"] is None
    assert ic["bas"] < x.mean() < ic["haut"]
    demi = 1.96 * x.std(ddof=1) / math.sqrt(40)
    assert ic["haut"] - ic["bas"] == pytest.approx(2 * demi, rel=0.15)


@pytest.mark.parametrize("tirages, jackknife, motif", [
    (np.full(100, 2.0), np.linspace(1, 3, 10), "tirages tous égaux"),
    (np.linspace(0, 4, 100), np.full(10, 2.0), "jackknife de variance nulle"),
    (np.linspace(3, 4, 100), np.linspace(1, 3, 10), "tirages tous du même côté de la valeur observée"),
    (np.linspace(0, 4, 100), np.array([1.0, np.nan, 2.0]), "jackknife non fini"),
])
def test_bca_non_defini_repli_par_percentiles_consigne(tirages, jackknife, motif):
    """Garde du point 11, artefacts : le repli par percentiles n'est jamais silencieux, son motif est rendu."""
    ic = re_.intervalle_bca(2.0, tirages, jackknife, 0.95)
    assert ic["methode"] == "percentiles" and ic["motif"] == motif
    bas, haut, _ = re_.intervalle_percentiles(tirages, 0.95)
    assert (ic["bas"], ic["haut"]) == (bas, haut)


def test_percentiles_ecartent_et_comptent_les_tirages_non_finis():
    bas, haut, non_finis = re_.intervalle_percentiles(np.array([1.0, 2.0, 3.0, np.inf, np.nan]), 0.9)
    assert non_finis == 2 and 1.0 <= bas <= haut <= 3.0


def test_niveau_bonferroni():
    assert re_.niveau_bonferroni(0.10, 2) == 0.95 and re_.niveau_bonferroni(0.05, 2) == 0.975
    assert re_.niveau_bonferroni(0.05, 6) == pytest.approx(1 - 0.05 / 6)
    with pytest.raises(ConfigurationInvalide):
        re_.niveau_bonferroni(0.05, 0)


# --- loi bêta et Clopper-Pearson (point 15) ----------------------------------------------------------------------
def test_clopper_pearson_exemples_du_texte():
    """Section « Seuil », C-P5 : il faut par exemple 281 détections sur 300, 555 sur 600 (valables pour e = 1)."""
    assert re_.clopper_pearson(281, 300)[0] >= 0.90 > re_.clopper_pearson(280, 300)[0]
    assert re_.clopper_pearson(555, 600)[0] >= 0.90 > re_.clopper_pearson(554, 600)[0]


def test_clopper_pearson_bords_et_arguments_non_entiers():
    assert re_.clopper_pearson(0, 50)[0] == 0.0 and re_.clopper_pearson(50, 50)[1] == 1.0
    assert re_.clopper_pearson(50, 50)[0] == pytest.approx(0.025 ** (1 / 50))           # forme fermée de x = n
    bas_a, haut_a = re_.clopper_pearson(140.5, 150.0)
    bas_b, haut_b = re_.clopper_pearson(281, 300)
    assert bas_a < bas_b and haut_a > haut_b                                           # effectif moindre, plus large
    with pytest.raises(ConfigurationInvalide):
        re_.clopper_pearson(11, 10)


def test_beta_contre_une_integration_numerique_et_contre_scipy_si_present():
    x = np.linspace(0, 0.3, 200001)
    a, b = 3.7, 9.2
    dens = x ** (a - 1) * (1 - x) ** (b - 1)
    norme = math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))
    integ = float(np.sum((dens[1:] + dens[:-1]) / 2) * (x[1] - x[0])) / norme
    assert re_.beta_repartition(0.3, a, b) == pytest.approx(integ, abs=1e-8)
    assert re_.beta_repartition(re_.beta_quantile(0.4, a, b), a, b) == pytest.approx(0.4, abs=1e-12)
    try:
        from scipy import stats
    except ImportError:
        return
    assert re_.beta_quantile(0.025, 281.0, 20.0) == pytest.approx(stats.beta.ppf(0.025, 281.0, 20.0), abs=1e-10)


def test_effectif_efficace_formule_et_cas_p_egal_un():
    x, N = np.array([6, 6, 5, 6, 3]), np.array([6, 6, 6, 6, 6])
    e = re_.effectif_efficace(x, N)
    p, N_o, T = 26 / 30, 30.0, 5
    attendu = ((T / (T - 1)) * np.sum((x - p * N) ** 2) / N_o ** 2) / (p * (1 - p) / N_o)
    assert e["effet_de_plan"] == pytest.approx(attendu) and e["effet_de_plan_defini"]
    assert e["effectif_efficace"] == pytest.approx(N_o / max(1.0, attendu))
    assert e["detections_efficaces"] == pytest.approx(p * e["effectif_efficace"])
    tout = re_.effectif_efficace(N, N)                    # p̂ = 1 : e n'est pas défini, e = 1, N_eff = N_o
    assert tout["effet_de_plan"] == 1.0 and not tout["effet_de_plan_defini"] and tout["effectif_efficace"] == 30.0
    rien = re_.effectif_efficace(np.zeros(5), N)          # p̂ = 0 : de même
    assert rien["effet_de_plan"] == 1.0 and rien["effectif_efficace"] == 30.0
    with pytest.raises(ConfigurationInvalide):
        re_.effectif_efficace(np.array([7.0, 1.0]), np.array([6.0, 6.0]))


# --- lois (points 7 à 10) ----------------------------------------------------------------------------------------
@pytest.fixture()
def jeu():
    rng = np.random.default_rng(3)
    n = 80
    v0 = rng.normal(4, 1.2, n)
    g = np.array([0.1, 0.2, 0.3])
    D = g[:, None] * (1.0 - v0)[None, :] + rng.normal(0, 0.05, (3, n))
    W = v0[None, :] + rng.normal(0, 0.3, (4, n))
    return {"n": n, "v0": v0, "D": D, "W": W, "un": np.ones((1, n)), "rng": rng}


def test_loi_separee_egale_aux_moindres_carres(jeu):
    d, x = jeu["D"][1], jeu["v0"]
    pente, ordonnee = np.polyfit(x, d, 1)
    s = lois.loi_separee(jeu["un"], d, x)
    assert s["g"][0] == pytest.approx(-pente) and s["c"][0] == pytest.approx(-ordonnee / pente)
    assert s["r2"][0] == pytest.approx(np.corrcoef(x, d)[0, 1] ** 2)


def test_loi_jointe_forme_fermee_egale_grille_et_section_doree(jeu):
    """Point 8 : la grille (pas 0,01 sur [−30 ; 40]) puis la section dorée (10⁻⁶) servent de test du module."""
    ferme = lois.loi_jointe(jeu["un"], jeu["D"], jeu["v0"])
    grille = lois.loi_jointe_par_grille(jeu["D"], jeu["v0"])
    assert ferme["c"][0] == pytest.approx(grille["c"], abs=2e-6) and not grille["au_bord"]
    assert ferme["residu"][0] == pytest.approx(grille["residu"], rel=1e-9)
    u = ferme["c"][0] - jeu["v0"]
    assert ferme["g"][0] == pytest.approx(jeu["D"] @ u / (u @ u))            # g_m(c) du texte
    assert ferme["G"][0] == pytest.approx(ferme["g"][0].mean())
    assert 0.9 < ferme["r2"][0] <= 1.0


def test_loi_jointe_simple_decalage_r2_nul_et_c_non_identifiable(jeu):
    """ĉ hors de [−30 ; 40] : « ĉ non identifiable » (la loi dégénère en simple décalage) ; R²_joint nul."""
    D = np.array([[0.3] * jeu["n"], [0.5] * jeu["n"]]) + jeu["rng"].normal(0, 1e-9, (2, jeu["n"]))
    ferme = lois.loi_jointe(jeu["un"], D, jeu["v0"])
    assert not (-30.0 <= ferme["c"][0] <= 40.0)
    assert lois.loi_jointe_par_grille(D, jeu["v0"])["au_bord"]
    bruite = np.array([[0.3] * jeu["n"], [0.5] * jeu["n"]]) + jeu["rng"].normal(0, 0.05, (2, jeu["n"]))
    assert abs(lois.loi_jointe(jeu["un"], bruite, jeu["v0"])["r2"][0]) < 0.1      # décalage et bruit : R²_joint ≈ 0


def test_loi_jointe_un_seul_rang_egale_la_loi_separee(jeu):
    j, s = lois.loi_jointe(jeu["un"], jeu["D"][:1], jeu["v0"]), lois.loi_separee(jeu["un"], jeu["D"][0], jeu["v0"])
    assert j["c"][0] == pytest.approx(s["c"][0]) and j["g"][0, 0] == pytest.approx(s["g"][0])


def test_calibrage_definitions_du_texte(jeu):
    v0, W = jeu["v0"], jeu["W"]
    cal = lois.calibrage(jeu["un"], v0, W)
    wbar = W.mean(0)
    rho = np.cov(v0, wbar)[0, 1] / np.var(v0, ddof=1)
    assert cal["rho_brut"][0] == pytest.approx(rho) and cal["v0bar"][0] == pytest.approx(v0.mean())
    C = np.cov(np.vstack([v0, W]))
    r = np.mean([C[a, b] for a in range(1, 5) for b in range(1, 5) if a != b]) / np.mean(C[0, 1:])
    assert cal["r"][0] == pytest.approx(r)
    assert cal["sigma"][0] == pytest.approx(np.std(W - v0[None, :]) / math.sqrt(2))
    assert cal["rho_sur_r"][0] == pytest.approx(min(1.0, max(0.05, cal["rho"][0] / r)))


@pytest.mark.parametrize("facteur, attendu, touche", [(3.0, 1.0, True), (-1.0, 0.05, True), (0.5, 0.5, False)])
def test_rho_borne_a_0_05_et_1(jeu, facteur, attendu, touche):
    W = np.stack([facteur * jeu["v0"], facteur * jeu["v0"] + 1e-3 * jeu["rng"].normal(size=jeu["n"])])
    cal = lois.calibrage(jeu["un"], jeu["v0"], W)
    assert cal["rho"][0] == pytest.approx(attendu, abs=1e-3) and bool(cal["touche_borne"][0]) is touche


def test_loi_nette_trois_lectures_et_lambda(jeu):
    v0, D, W = jeu["v0"], jeu["D"], jeu["W"]
    cal = lois.loi_nette(jeu["un"], v0, D, W, 0.0, "calibree")
    X = lois.regresseur_calibre(v0, W, "calibree")
    assert cal["c"][0] == pytest.approx(lois.loi_jointe(jeu["un"], D, X)["c"][0])       # même loi jointe, Δᵃ sur X
    assert cal["lam"][0] == pytest.approx((cal["c"][0] - v0.mean()) / (0.0 - v0.mean()))
    brut = lois.loi_nette(jeu["un"], v0, D, W, 0.0, "sans_calibrage")
    assert brut["c"][0] == pytest.approx(lois.loi_jointe(jeu["un"], D, v0)["c"][0])     # ρ = 1 : X = v₀
    tiers = lois.loi_nette(jeu["un"], v0, D, W, 0.0, "rho_sur_r")
    assert tiers["rho_lu"][0] == pytest.approx(cal["calibrage"]["rho_sur_r"][0])
    with pytest.raises(ConfigurationInvalide):
        lois.loi_nette(jeu["un"], v0, D, W, 0.0, "autre")
    # loi séparée nette par rang (point 10)
    s = lois.loi_separee(jeu["un"], D[2], X)
    assert cal["c_par_rang"][0, 2] == pytest.approx(s["c"][0])


def test_loi_nette_recalculee_dans_chaque_tirage(jeu):
    """v̄₀, w̄ et ρ̂ sont recalculés dans chaque tirage : un tirage pondéré égale le calcul sur l'échantillon répété."""
    rng = np.random.default_rng(5)
    comptes = re_.comptes_par_grappes(np.arange(jeu["n"]), 3, rng)
    tir = lois.loi_nette(comptes, jeu["v0"], jeu["D"], jeu["W"], 0.0)
    for b in range(3):
        idx = np.repeat(np.arange(jeu["n"]), comptes[b].astype(int))
        direct = lois.loi_nette(np.ones((1, idx.size)), jeu["v0"][idx], jeu["D"][:, idx], jeu["W"][:, idx], 0.0)
        assert tir["c"][b] == pytest.approx(direct["c"][0]) and tir["lam"][b] == pytest.approx(direct["lam"][0])
        assert tir["calibrage"]["rho"][b] == pytest.approx(direct["calibrage"]["rho"][0])
        assert tir["calibrage"]["r"][b] == pytest.approx(direct["calibrage"]["r"][0])


def test_tirage_degenere_c_hors_bornes_ou_cible_trop_proche(jeu):
    sain = lois.loi_nette(jeu["un"], jeu["v0"], jeu["D"], jeu["W"], 0.0)
    assert not sain["degenere"][0]
    proche = lois.loi_nette(jeu["un"], jeu["v0"], jeu["D"], jeu["W"], float(jeu["v0"].mean()) + 0.49)
    assert proche["degenere"][0]                                           # |v* − v̄₀| < 0,5
    assert not lois.loi_nette(jeu["un"], jeu["v0"], jeu["D"], jeu["W"], float(jeu["v0"].mean()) + 0.51)["degenere"][0]
    decalage = np.full((1, jeu["n"]), 0.4) + jeu["rng"].normal(0, 1e-9, (1, jeu["n"]))
    assert lois.loi_nette(jeu["un"], jeu["v0"], decalage, jeu["W"], 0.0)["degenere"][0]    # ĉ hors de [−30 ; 40]


def test_terme_d_intention_egale_aux_moindres_carres_bruts(jeu):
    s = np.arange(jeu["n"]) % 2 == 1
    D = jeu["D"] + np.array([0.3, 0.1, -0.2])[:, None] * s[None, :]
    loi = lois.loi_nette(jeu["un"], jeu["v0"], D, jeu["W"], 0.0, saboteur=s)
    X = lois.regresseur_calibre(jeu["v0"], jeu["W"])

    def residu(c):
        total = 0.0
        for m in range(3):
            A = np.stack([c - X, s.astype(float)], 1)
            sol = np.linalg.lstsq(A, D[m], rcond=None)[0]
            total += float(((A @ sol - D[m]) ** 2).sum())
        return total
    grille = np.linspace(loi["c"][0] - 0.05, loi["c"][0] + 0.05, 2001)
    assert grille[int(np.argmin([residu(c) for c in grille]))] == pytest.approx(loi["c"][0], abs=1e-4)
    assert loi["beta"][0] == pytest.approx([0.3, 0.1, -0.2], abs=0.05)
    with pytest.raises(ConfigurationInvalide):
        lois.loi_nette(jeu["un"], jeu["v0"], D, jeu["W"], 0.0, saboteur=np.ones(jeu["n"], dtype=bool))


def test_gamma_loi_temoin_attracteur_forme(jeu):
    d, v0 = jeu["D"][0], jeu["v0"]
    u = 0.0 - v0
    assert lois.gamma_destination_imposee(jeu["un"], d, v0, 0.0)[0] == pytest.approx((d @ u) / (u @ u))
    t = lois.loi_temoin(jeu["un"], v0, jeu["W"])
    assert t["g"].shape == (1, 4)                                          # chaque témoin distinct tient lieu de rang
    a = lois.attracteur_propre([3.0, 4.0, 5.0, 4.0, 3.5, 4.5])
    assert (a["a"], a["min"], a["max"], a["n"]) == (4.0, 3.0, 5.0, 6)
    f = lois.forme_de_l_issue(np.array([0.0, 1.0, 0.5, 0.95]), np.zeros(4), 1.0)
    assert (f["part_sous"], f["part_au_dessus"], f["part_cumulee"]) == (0.25, 0.5, 0.75)
    assert lois.correlation_de_rang([1, 2, 3], [0.1, 0.2, 0.4]) == pytest.approx(1.0)


def test_placebo_par_permutation_reproduit_la_regression_vers_la_moyenne():
    rng = np.random.default_rng(8)
    vrai = rng.normal(4, 1, 400)
    v0, V = vrai + rng.normal(0, 0.5, 400), vrai[None, :] + rng.normal(0, 0.5, (2, 400))
    p = lois.placebo_par_permutation(v0, V, 50, rng)
    brute = lois.loi_jointe(np.ones((1, 400)), V - v0[None, :], v0)["G"][0]
    assert 0.1 < brute < 0.3 and p["moyenne"] == pytest.approx(brute, abs=0.05)       # sans attaque : g > 0 quand même
    with pytest.raises(ConfigurationInvalide):
        lois.placebo_par_permutation(v0, V, 0, rng)


# --- rangs (bloc de la stabilité de rang) ------------------------------------------------------------------------
def test_loi_exacte_du_w_valeurs_du_texte():
    """C-P3a : 7 776 affectations, W ≥ 0,64 → p = 0,0394 ; P(W ≤ 0,20) = 0,6327. C-P3c : 1 296 affectations,
    W ≥ 0,8125 → p = 0,0417."""
    valeurs, probas = rg.loi_exacte_du_w(5)
    assert probas.sum() == pytest.approx(1.0) and round(1 / probas.min()) <= 7776
    assert rg.p_exact_du_w(0.64, 5) == pytest.approx(0.0394, abs=5e-5)
    assert float(probas[valeurs <= 0.20 + 1e-9].sum()) == pytest.approx(0.6327, abs=5e-5)
    assert rg.p_exact_du_w(0.8125, 4) == pytest.approx(0.0417, abs=5e-5)
    assert rg.p_exact_du_w(0.64, 5) <= 0.05 < rg.p_exact_du_w(float(valeurs[valeurs < 0.64 - 1e-9].max()), 5)
    assert rg.p_exact_du_w(0.8125, 4) <= 0.05 < rg.p_exact_du_w(float(rg.loi_exacte_du_w(4)[0][-3]), 4)


def test_w_de_kendall_et_rangs():
    accord = np.array([[1.0, 2.0, 3.0]] * 5)
    assert rg.w_de_kendall(accord) == pytest.approx(1.0)
    assert rg.w_de_kendall(np.array([[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1]])) == pytest.approx(0.0)
    assert rg.rangs_des_objets([0.3, 0.3, 0.1]).tolist() == [2.5, 2.5, 1.0]
    lot = rg.w_de_kendall(np.stack([accord, accord[:, ::-1]]))
    assert lot.shape == (2,) and lot == pytest.approx([1.0, 1.0])
    with pytest.raises(ConfigurationInvalide):
        rg.w_de_kendall(np.array([[1.0, 2.0, 3.0]]))


def test_tau_de_kendall():
    assert rg.tau_de_kendall([1, 2, 3, 4], [10, 20, 30, 40]) == pytest.approx(1.0)
    assert rg.tau_de_kendall([1, 2, 3, 4], [4, 3, 2, 1]) == pytest.approx(-1.0)
    assert rg.tau_de_kendall([1, 2, 3, 4], [1, 3, 2, 4]) == pytest.approx(4 / 6)
    e = rg.ecarts_intra_famille(np.array([[1.0, 2.0, 6.0]]))
    assert e.tolist() == [[-2.0, -1.0, 3.0]]


def _G_ordonne(rng, B=400, ecart=0.1, bruit=0.02):
    base = np.array([[0.1, 0.1 + ecart, 0.1 + 2 * ecart]] * 5)
    return base, base[None] + rng.normal(0, bruit, (B, 5, 3))


def test_c_p3a_lecture_etablie_et_non_etablie():
    rng = np.random.default_rng(11)
    G, Gb = _G_ordonne(rng)
    a = rg.c_p3a_lecture(G, Gb)
    assert a["W"] == pytest.approx(1.0) and a["p_exact"] <= 0.05 and a["p_centre"] <= 0.05 and a["conclut"]
    plat = np.array([[0.1, 0.2, 0.3], [0.3, 0.2, 0.1], [0.2, 0.3, 0.1], [0.1, 0.3, 0.2], [0.3, 0.1, 0.2]])
    b = rg.c_p3a_lecture(plat, plat[None] + rng.normal(0, 0.02, (400, 5, 3)))
    assert not b["conclut"]
    # p exact ≤ 0,05 mais p centré > 0,05 : pas de conclusion (les deux sont exigées)
    c = rg.c_p3a_lecture(G, G[None] + rng.normal(0, 5.0, (400, 5, 3)) * np.array([1.0, 1.0, 1.0]) + np.array([0, 5, 10.0]))
    assert c["p_exact"] <= 0.05 and c["p_centre"] > 0.05 and not c["conclut"]


def test_c_p3b_et_c_p3c_lectures():
    rng = np.random.default_rng(12)
    GA, GAb = _G_ordonne(rng)
    GB, GBb = _G_ordonne(rng)
    b = rg.c_p3b_lecture(GA, GAb, GB, GBb, permutations=300, rng=rng)
    assert b["tau"] > 0.6 and b["conclut"] and "p_permutation_des_quinze_valeurs" in b
    sans = rg.c_p3b_lecture(GA, GAb, GB[:, ::-1], GBb[:, :, ::-1])
    assert sans["tau"] < 0 and not sans["conclut"] and "p_permutation_des_quinze_valeurs" not in sans
    c = rg.c_p3c_lecture([0.1, 0.2, 0.3], [0.2, 0.3, 0.5], [0.0, 0.1, 0.4], [0.3, 0.4, 0.9])
    assert c["W"] == pytest.approx(1.0) and c["p_exact"] == pytest.approx(6 / 1296) and c["conclut"]
    limite = rg.c_p3c_lecture([0.1, 0.2, 0.3], [0.2, 0.3, 0.5], [0.0, 0.1, 0.4], [0.3, 0.9, 0.4])   # W = 0,8125
    assert limite["W"] == pytest.approx(0.8125) and limite["p_exact"] == pytest.approx(0.0417, abs=5e-5) and limite["conclut"]
    non = rg.c_p3c_lecture([0.1, 0.2, 0.3], [0.2, 0.3, 0.5], [0.4, 0.1, 0.0], [0.3, 0.9, 0.4])
    assert not non["conclut"]


def _lectures(conclut):
    return {l: {"conclut": c, "W": 1.0} for l, c in zip(rg.TOUTES_LES_LECTURES, conclut)}


@pytest.mark.parametrize("nom, version, conclut, clause, attendu", [
    ("C-P3a", "a", (True, True, True), (), rg.ETABLIE),
    ("C-P3a", "a", (True, True, False), (), rg.NON_ETABLIE),          # les deux premières ne suffisent pas
    ("C-P3b", "a", (True, False, True), (), rg.NON_ETABLIE),
    ("C-P3c", "a", (True, True, True), (), rg.ETABLIE),
    ("C-P3a", "a", (True, True, True), ("C-P3a",), rg.SANS_VERDICT),   # clause de repli mécanique
    ("C-P3a", "b", (True, True, True), (), rg.SANS_VERDICT),           # version (b) : rapportée sans verdict
    ("C-P3b", "b", (True, True, True), (), rg.SANS_VERDICT),
    ("C-P3c", "b", (True, True, False), (), rg.ETABLIE),               # version (b) : C-P3c à deux lectures
    ("C-P3c", "b", (True, False, True), (), rg.NON_ETABLIE),
    ("C-P3c", "b", (True, True, True), ("C-P3c",), rg.SANS_VERDICT),
])
def test_verdict_stabilite_deux_versions(nom, version, conclut, clause, attendu):
    v = rg.verdict_stabilite(nom, _lectures(conclut), version, clause)
    assert v["verdict"] == attendu and v["refutation"] is None
    assert set(v["par_lecture"]) == set(rg.TOUTES_LES_LECTURES)          # toujours calculées aux trois lectures
    assert v["lectures_du_verdict"] == list(rg.LECTURES_VERSION[version])


def test_verdict_stabilite_mention_grille_et_gardes():
    v = rg.verdict_stabilite("C-P3c", _lectures((True, True, True)), "a", (), grille_verifiee=False)
    assert rg.MENTION_GRILLE in v["mentions"]
    assert rg.MENTION_GRILLE not in rg.verdict_stabilite("C-P3a", _lectures((True,) * 3), "a", (), False)["mentions"]
    with pytest.raises(ConfigurationInvalide):
        rg.verdict_stabilite("C-P3a", _lectures((True,) * 3), "c")
    with pytest.raises(ConfigurationInvalide):
        rg.verdict_stabilite("C-P3a", {"calibree": {"conclut": True}}, "a")


def test_seuil_de_la_clause_de_repli():
    assert rg.seuil_de_la_clause_de_repli(1000) == pytest.approx(0.064, abs=5e-4)      # « 0,064 à 1 000 essais »
    with pytest.raises(ConfigurationInvalide):
        rg.seuil_de_la_clause_de_repli(999)
