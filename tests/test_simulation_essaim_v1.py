"""Simulation d'essaim v1 : instrument seulement (R1). Aucun de ces tests ne calcule une cellule de la grille
décisive (`brouillons/preuves-mentors-v1/essaim-simulation-v1/grille-essaim-v1-brouillon1.json`, puis sa version
scellée) : tailles, horizons, budgets et graines diffèrent, et la grille décisive n'est pas lue.

Couvre : équivalence lots ↔ références scalaires ; invariances exactes par sous-groupe (T1) ; menaces (groupes,
sémantique, budgets) ; seuils exacts aléatoirisés, Monte-Carlo, conformes avec départage ; intervalles exacts ;
formes closes contre Monte-Carlo ; bornes ; lecture gelée ; gardes (cas sain + artefact, R5) ; graine racine
dérivée de l'empreinte du préenregistrement ; chaîne complète sur une mini-grille dans un dépôt jetable.
"""
import copy
import json
import math
import subprocess

import numpy as np
import pytest
from scipy import stats

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.simulation_essaim import blocs as B
from controle_ia.simulation_essaim import calibrage as C
from controle_ia.simulation_essaim import lecture as LEC
from controle_ia.simulation_essaim import menaces as M
from controle_ia.simulation_essaim import references as RF
from controle_ia.simulation_essaim import statistiques as S
from controle_ia.simulation_t03.lois import tirer

GRAINE = np.random.SeedSequence(5550555)
Q, ALPHA = 0.1, 0.05
U_CASE = C.seuil_par_case(Q)


def _rng(k):
    return np.random.default_rng(np.random.SeedSequence(GRAINE.entropy, spawn_key=(k,)))


def _params(K, T):
    return {"u": U_CASE, "q": Q, "fractions": S.FRACTIONS_LAMBDA, "rho": C.rho_e_pas(K, T, ALPHA)}


# --- équivalence avec les références scalaires ---
@pytest.mark.parametrize("K,T", [(4, 7), (6, 5)])
def test_statistiques_egales_aux_references(K, T):
    Y = _rng(1).standard_normal((40, K, T))
    p = _params(K, T)
    v = S.calculer(Y, list(S.STATISTIQUES), p)
    for s in S.STATISTIQUES:
        r = np.array([RF.reference(s, Y[i], p) for i in range(40)])
        assert np.allclose(v[s], r, rtol=1e-12, atol=1e-12), s


def test_e_valeurs_definitions():
    """Processus e cumulé : log M_n = log moyenne_λ Π (1 + λ(C_t − Kq)) ; détecteur e ≥ dernier facteur."""
    K, T = 5, 6
    Y = _rng(2).standard_normal((30, K, T))
    C_t = S.comptes_par_pas(Y, U_CASE)
    lam = np.array(S.FRACTIONS_LAMBDA) / (K * Q)
    prod = np.cumprod(1.0 + lam[None, None, :] * (C_t[:, :, None] - K * Q), axis=1)
    assert np.allclose(S.e_coelev(Y, U_CASE, Q), np.log(prod.mean(axis=2)).max(axis=1))
    dernier = np.log((1.0 + lam[None, :] * (C_t[:, -1:] - K * Q)).mean(axis=1))
    assert np.all(S.ed_coelev(Y, U_CASE, Q) >= dernier - 1e-12)
    with pytest.raises(GardeArret):
        S.log_facteurs(C_t, K, Q, (0.5, 1.0))                  # λ = λ_max : facteur nul possible, refusé


# --- invariances exactes (T1) par sous-groupe ---
def test_invariances_exactes_par_groupe():
    K, T = 5, 8
    g = _rng(3)
    Y = g.standard_normal((60, K, T))
    p = _params(K, T)
    vY = S.calculer(Y, list(S.STATISTIQUES), p)
    arrangements = {"agents": [M.rebrassage_agents(Y, g), M.routage(Y, 3, 1, g), M.routage(Y, T, K, g)],
                    "temps": [M.rebrassage_temps(Y, g), M.synchro(Y, 3, 1, g)[0], M.synchro(Y, K, 2, g)[0]],
                    "tout": [M.rebrassage_tout(Y, g)]}
    for groupe, liste in arrangements.items():
        for X in liste:
            M.exiger_groupe(X, Y, groupe, "test")
            vX = S.calculer(X, list(S.STATISTIQUES), p)
            for s in S.STATISTIQUES:
                if S.invariante(s, groupe):
                    assert np.array_equal(vX[s], vY[s]), (groupe, s)     # au bit près
    # les non-invariantes changent bien (l'invariance n'est pas un artefact du code)
    for s, X in (("agent_moyenne", arrangements["agents"][1]), ("coelev_comptage", arrangements["temps"][2]),
                 ("e_pas", arrangements["temps"][0]), ("pas_moyenne", arrangements["tout"][0])):
        assert not np.array_equal(S.calculer(X, [s], p)[s], vY[s]), s


def test_groupes_des_statistiques():
    assert S.invariante("coelev_comptage", "agents") and not S.invariante("coelev_comptage", "temps")
    assert S.invariante("e_coelev", "agents") and not S.invariante("e_coelev", "tout")
    assert S.invariante("agent_moyenne", "temps") and not S.invariante("agent_moyenne", "agents")
    assert all(S.invariante(s, g) for s in ("somme", "max", "comptage") for g in S.GROUPES)
    with pytest.raises(GardeArret):
        S.invariante("inconnue", "agents")
    with pytest.raises(GardeArret):
        S.invariante("somme", "diagonale")
    assert S.nom_statistique("e_coelev_ville") == "e_coelev" and S.nom_statistique("ed_coelev") == "ed_coelev"


# --- menaces ---
def test_routage_un_agent_et_relais():
    K, T, m = 4, 9, 6
    g = _rng(4)
    Y = g.standard_normal((50, K, T))
    X = M.routage(Y, m, 1, g)
    M.exiger_groupe(X, Y, "agents", "routage")
    porteurs = X.argmax(axis=1)                                   # (R, T) : porteur du max de chaque pas
    modifies = (X != Y).any(axis=1)                               # pas touchés par le routage
    for i in range(50):
        assert len(set(porteurs[i, modifies[i]].tolist())) <= 1   # un seul destinataire
    Xr = M.routage(Y, T, K, g)
    porteurs = Xr.argmax(axis=1)
    comptes = np.stack([(porteurs == a).sum(axis=1) for a in range(K)], axis=1)
    assert np.all(comptes.min(axis=1) >= T // K) and np.all(comptes.max(axis=1) <= -(-T // K))
    with pytest.raises(GardeArret):
        M.routage(Y, T + 1, 1, g)
    with pytest.raises(GardeArret):
        M.routage(Y, 2, K + 1, g)


def test_synchro_semantique():
    K, T, m = 6, 7, 4
    g = _rng(5)
    Y = g.standard_normal((80, K, T))
    X, agents, pas = M.synchro(Y, m, 1, g)
    M.exiger_groupe(X, Y, "temps", "synchro")
    res = {"viol_hors_synchro": 0, "viol_valeurs_hautes": 0, "viol_compte_pas": 0, "viol_borne_coelev": 0}
    B._verifier_synchro(res, X, Y, {"agents": agents, "pas": pas}, U_CASE, 1)
    assert res == {k: 0 for k in res}
    rr = np.arange(80)
    assert np.all(X[rr[:, None], agents, pas] == Y[rr[:, None], agents].max(axis=2))
    X2, ag2, pas2 = M.synchro(Y, K, 3, g)
    res = {k: 0 for k in res}
    B._verifier_synchro(res, X2, Y, {"agents": ag2, "pas": pas2}, U_CASE, 3)
    assert res["viol_hors_synchro"] == 0 and res["viol_valeurs_hautes"] == 0
    # artefact : une permutation qui n'est pas la synchronisation annoncée est vue
    faux = X.copy()
    faux[:, :, [0, 1]] = faux[:, :, [1, 0]]
    res = {k: 0 for k in res}
    B._verifier_synchro(res, faux, Y, {"agents": agents, "pas": pas}, U_CASE, 1)
    assert sum(res.values()) > 0
    with pytest.raises(GardeArret):
        M.synchro(Y, 2, T, g)


def test_garde_groupe_artefacts():
    g = _rng(6)
    Y = g.standard_normal((10, 3, 5))
    X = Y.copy()
    X[0, 0, 0] += 1.0                                             # une valeur perdue, une autre inventée
    with pytest.raises(GardeArret, match="non préservé"):
        M.exiger_groupe(X, Y, "tout", "artefact")
    with pytest.raises(GardeArret, match="non préservé"):         # arrangement de G_T déclaré dans G_A
        M.exiger_groupe(M.rebrassage_temps(Y, g), Y, "agents", "artefact")
    with pytest.raises(GardeArret, match="non préservé"):         # arrangement de G_A déclaré dans G_T
        M.exiger_groupe(M.rebrassage_agents(Y, g), Y, "temps", "artefact")
    with pytest.raises(GardeArret):
        M.exiger_groupe(Y, Y, "diagonale", "artefact")
    with pytest.raises(GardeArret):
        M.arranger({"nom": "x", "genre": "inconnu"}, Y, g)


def test_decalages_budget_et_gardes():
    g = _rng(7)
    K, T, R, Bv = 4, 6, 30, 7.5
    D = M.decalages("concentre", K, T, Bv, 1, R, g)
    assert np.allclose(D.sum(axis=(1, 2)), Bv) and np.all((D > 0).sum(axis=(1, 2)) == 1)
    D = M.decalages("synchro", K, T, Bv, 3, R, g)
    assert np.all(((D > 0).sum(axis=1) > 0).sum(axis=1) == 1) and np.all((D > 0).sum(axis=(1, 2)) == 3)
    D = M.decalages("temps", K, T, Bv, 5, R, g)
    assert np.all(((D > 0).sum(axis=2) > 0).sum(axis=1) == 1) and np.all((D > 0).sum(axis=(1, 2)) == 5)
    for args in (("concentre", K, T, Bv, 2), ("synchro", K, T, -1.0, 2), ("synchro_un", K, T, Bv, 1), ("x", K, T, Bv, 1)):
        with pytest.raises(GardeArret):
            M.decalages(*args, R, g)


# --- calibrage ---
@pytest.mark.parametrize("K,T", [(3, 7), (8, 4)])
def test_seuils_exacts_de_taille_alpha(K, T):
    s = C.seuils_exacts(K, T, Q, ALPHA)
    n0 = K * T
    assert math.isclose(C.taux_discret(C.cdf_binom(n0, Q), s["comptage"]), ALPHA, rel_tol=1e-10)
    assert math.isclose(C.taux_discret(C.cdf_binom(T, Q) ** K, s["agent_comptage"]), ALPHA, rel_tol=1e-10)
    assert math.isclose(C.taux_discret(C.cdf_binom(K, Q) ** T, s["coelev_comptage"]), ALPHA, rel_tol=1e-10)
    assert math.isclose(stats.norm.cdf(s["agent_moyenne"][0]) ** K, 1 - ALPHA, rel_tol=1e-12)
    th = C.puissances_decalage(np.zeros((K, T)), Q, ALPHA, s)          # décalage nul : taille α partout
    assert all(math.isclose(v, ALPHA, rel_tol=1e-9) for v in th.values()), th
    g = _rng(8)                                                        # Monte-Carlo : taille α, départage compris
    Y = g.standard_normal((40000, K, T))
    U = g.random(40000)
    v = S.calculer(Y, ["comptage", "agent_comptage", "coelev_comptage", "pas_moyenne"], _params(K, T))
    for k in v:
        p = C.alarme(v[k], U, s[k]).mean()
        assert abs(p - ALPHA) < 4.5 * math.sqrt(ALPHA * (1 - ALPHA) / 40000), (k, p)


def test_seuil_mc_aleatoirise_exact_sur_l_echantillon():
    g = _rng(9)
    for v in (g.standard_normal(10000), np.repeat(np.arange(8.0), 1250), np.round(g.standard_normal(9999), 1)):
        c, gam = C.seuil_mc(v, ALPHA)
        assert 0.0 <= gam < 1.0
        assert math.isclose((v > c).mean() + gam * (v == c).mean(), ALPHA, rel_tol=1e-9)
    c, gam = C.seuil_mc(np.arange(10.0), ALPHA)                          # petit échantillon : départage seul
    assert c == 9.0 and math.isclose(gam, 0.5)
    for mauvais in (np.array([1.0, np.nan]), np.array([])):
        with pytest.raises(GardeArret):
            C.seuil_mc(mauvais, ALPHA)


def test_intervalle_exact():
    b, h = C.intervalle_cp(5, 100, 0.05)
    assert math.isclose(b, stats.beta.ppf(0.025, 5, 96)) and math.isclose(h, stats.beta.ppf(0.975, 6, 95))
    assert C.intervalle_cp(0, 50, 0.01)[0] == 0.0 and C.intervalle_cp(50, 50, 0.01)[1] == 1.0
    for args in ((6, 5, 0.1), (1, 10, 0.0)):
        with pytest.raises(GardeArret):
            C.intervalle_cp(*args)


def test_conforme_avec_departage_taux_exact():
    """Statistique discrète (beaucoup d'ex aequo) : le départage par U rend le taux conforme exact."""
    g = _rng(10)
    Kc, nt, L = 39, 20, 600
    j = C.rang_conforme(Kc, ALPHA)
    taux = []
    for _ in range(L):
        Vc, Uc = g.integers(0, 3, Kc).astype(float), g.random(Kc)
        Vt, Ut = g.integers(0, 3, nt).astype(float), g.random(nt)
        taux.append(C.alarme_conforme(Vt, Ut, C.seuil_conforme(Vc, Uc, ALPHA)).mean())
    attendu = 1 - j / (Kc + 1)
    se = math.sqrt(stats.betabinom.var(nt, Kc + 1 - j, j) / nt ** 2 / L)
    assert abs(np.mean(taux) - attendu) < 4.5 * se
    bas, haut, t = C.region_conforme(L, nt, Kc, ALPHA, 1e-3)
    assert math.isclose(t, attendu) and bas <= int(round(np.sum(taux) * nt)) <= haut
    moy = L * nt * (Kc + 1 - j) / (Kc + 1)
    assert bas < moy < haut
    with pytest.raises(GardeArret):
        C.seuil_conforme(np.arange(5.0), np.zeros(5), ALPHA)          # K trop petit : seuil infini refusé


def test_formes_closes_classe_M_contre_monte_carlo():
    K, T = 4, 6
    s = C.seuils_exacts(K, T, Q, ALPHA)
    g = _rng(11)
    R = 30000
    for genre, Bv, m in (("concentre", 3.0, 1), ("synchro", 4.0, 3), ("temps", 4.0, 4)):
        th = C.puissances_decalage(C.motif(genre, K, T, Bv, m), Q, ALPHA, s)
        X = g.standard_normal((R, K, T)) + M.decalages(genre, K, T, Bv, m, R, g)
        U = g.random(R)
        v = S.calculer(X, list(th), _params(K, T))
        for k, p_th in th.items():
            p = C.alarme(v[k], U, s[k]).mean()
            assert abs(p - p_th) < 4.5 * math.sqrt(p_th * (1 - p_th) / R) + 1e-12, (genre, k, p, p_th)


@pytest.mark.parametrize("loi", [{"type": "effet_episode", "tau": 0.3}, {"type": "equicorrelation", "c": 0.4}])
def test_formes_closes_lois_hors_hypotheses(loi):
    K, T = 4, 6
    s = C.seuils_exacts(K, T, Q, ALPHA)
    th = C.fausses_alarmes_reference(loi, K, T, Q, ALPHA, s)
    g = _rng(12)
    R = 30000
    X, U = tirer(g, R, {**loi, "N": K, "T": T}), g.random(R)
    v = S.calculer(X, list(th), _params(K, T))
    for k, p_th in th.items():
        p = C.alarme(v[k], U, s[k]).mean()
        assert abs(p - p_th) < 4.5 * math.sqrt(p_th * (1 - p_th) / R), (loi, k, p, p_th)
    assert C.fausses_alarmes_reference({"type": "iid"}, K, T, Q, ALPHA, s)["max"] == ALPHA
    if loi["type"] == "equicorrelation":
        assert th["agent_moyenne"] <= ALPHA + 1e-12                    # Slepian
    with pytest.raises(GardeArret):
        C.fausses_alarmes_reference({"type": "ar1", "phi": 0.3}, K, T, Q, ALPHA, s)


def test_borne_synchro_minore_la_puissance():
    K, T, m = 5, 8, 4
    s = C.seuils_exacts(K, T, Q, ALPHA)
    lb = C.borne_synchro(K, T, m, Q, s["coelev_comptage"])
    g = _rng(13)
    R = 20000
    X = M.synchro(g.standard_normal((R, K, T)), m, 1, g)[0]
    p = C.alarme(S.coelev_comptage(X, U_CASE), g.random(R), s["coelev_comptage"]).mean()
    assert 0.0 < lb <= 1.0 and p >= lb - 4.5 * math.sqrt(lb * (1 - lb) / R)


# --- R5 : cas sain et artefact du théorème sur l'axe des agents ---
def test_cas_sain_menace_concentree_detectee_par_le_max():
    K, T, R, Bv = 4, 6, 20000, 5.0
    s = C.seuils_exacts(K, T, Q, ALPHA)
    g = _rng(14)
    X = g.standard_normal((R, K, T)) + M.decalages("concentre", K, T, Bv, 1, R, g)
    k = int(C.alarme(S.maximum(X), g.random(R), s["max"]).sum())
    p_th = C.puissances_decalage(C.motif("concentre", K, T, Bv, 1), Q, ALPHA, s)["max"]
    assert p_th > 0.9
    assert LEC.egal_valeur(k, R, p_th, 1e-5)[0] == "conforme"
    assert LEC.au_dessus_valeur(k, R, ALPHA, 1e-5)[0] == "conforme"


def test_artefact_diffuse_entre_agents_puissance_egale_fausse_alarme():
    """Menace diffuse entre agents (multi-ensemble de chaque pas conservé, routage vers un agent) : toute statistique
    invariante par permutation des agents d'un pas a une puissance égale à son taux de fausse alarme, à l'intervalle
    exact près ; la surveillance par agent, non invariante, la détecte. Échantillons indépendants."""
    K, T, R, R0 = 5, 8, 8000, 20000
    s = C.seuils_exacts(K, T, Q, ALPHA)
    s["e_coelev_ville"] = s["e_pas_ville"] = C.seuil_ville(ALPHA)
    p = _params(K, T)
    noms = list(s)
    g0, g1 = _rng(15), _rng(16)
    Y0, U0 = g0.standard_normal((R0, K, T)), g0.random(R0)
    Y1, U1 = g1.standard_normal((R, K, T)), g1.random(R)
    X1 = M.routage(Y1, T, 1, g1)
    v0, v1 = S.calculer(Y0, B.stats_de(noms), p), S.calculer(X1, B.stats_de(noms), p)
    for a in noms:
        st = S.nom_statistique(a)
        k0 = int(C.alarme(v0[st], U0, s[a]).sum())
        k1 = int(C.alarme(v1[st], U1, s[a]).sum())
        if S.invariante(st, "agents"):
            assert LEC.egal(k1, R, k0, R0, 1e-5)[0] == "conforme", a
        else:
            assert LEC.au_dessus(k1, R, k0, R0, 1e-5)[0] == "conforme", a


def test_artefact_statistique_non_invariante_vue_par_la_lecture(monkeypatch):
    """Si une statistique annoncée invariante ne l'est pas (somme par pas faite dans l'ordre des agents, pondérée),
    le bloc C compte des valeurs différentes et la lecture rend HE1.1 contraire (audit)."""
    grille = _mini_grille()
    grille["C"] = {"m4x5": [s for s in grille["C"]["m4x5"] if s["genre"] == "routage"][:1]}
    grille["M"], grille["HE3"]["configs"], grille["HE6"]["configs"] = {}, [], []
    ctx = _contexte(grille)
    calib = {"m4x5": B.calibrer(ctx, "m4x5")}
    vraie = S.sommes_par_pas
    monkeypatch.setattr(S, "sommes_par_pas", lambda Xb: vraie(Xb) + 1e-3 * np.asarray(Xb)[:, 0, :])
    res = {"calibrage": calib, "C": B.bloc_C(ctx)}
    lec = LEC.lire(res, grille)
    assert lec["predictions"]["HE1.1"]["verdict"] == "réfutée" and lec["predictions"]["HE1.1"]["a_auditer"]


# --- graines (R9) ---
def test_entropie_depuis_prereg_et_taches():
    from controle_ia.simulation_essaim.run_essaim import entropie_depuis_prereg, taches

    sha = "0123456789abcdef" * 4
    assert entropie_depuis_prereg(sha) == int("0123456789abcdef0123456789abcdef", 16)
    assert entropie_depuis_prereg(sha) < 2 ** 128
    for mauvais in ("abc", "G" * 64, None):
        with pytest.raises(GardeArret):
            entropie_depuis_prereg(mauvais)
    t = taches(_mini_grille())
    assert len(t) == len(set(t)) and "calib/m3x6" in t and "HE3/m3x8/c0.4/conforme/2" in t
    ctx = B.Contexte(_mini_grille(), {}, "")
    with pytest.raises(GardeArret, match="absente du manifeste"):
        ctx.rng("calib/m3x6")


# --- lecture gelée ---
def test_criteres_de_lecture():
    g = 1e-5
    assert LEC.egal(1000, 20000, 5000, 100000, g)[0] == "conforme"
    assert LEC.egal(1600, 20000, 5000, 100000, g)[0] == "contraire"
    assert LEC.au_dessus(1600, 20000, 5000, 100000, g)[0] == "conforme"
    assert LEC.au_dessus(1020, 20000, 5000, 100000, g)[0] == "non concluant"
    assert LEC.au_dessus(400, 20000, 5000, 100000, g)[0] == "contraire"
    assert LEC.en_dessous(400, 20000, 5000, 100000, g)[0] == "conforme"
    assert LEC.en_dessous(1600, 20000, 5000, 100000, g)[0] == "contraire"
    assert LEC.au_plus(1020, 20000, 5000, 100000, g)[0] == "conforme"
    assert LEC.au_plus(1600, 20000, 5000, 100000, g)[0] == "contraire"
    assert LEC.egal_valeur(10000, 20000, 0.5, g)[0] == "conforme" and LEC.egal_valeur(10500, 20000, 0.5, g)[0] == "contraire"
    assert LEC.au_moins_valeur(9000, 20000, 0.46, g)[0] == "conforme" and LEC.au_moins_valeur(9000, 20000, 0.5, g)[0] == "contraire"
    assert LEC.au_plus_valeur(1000, 20000, 0.05, g)[0] == "conforme" and LEC.au_plus_valeur(1400, 20000, 0.05, g)[0] == "contraire"
    assert LEC.region(5, 3, 7)[0] == "conforme" and LEC.region(8, 3, 7)[0] == "contraire"
    assert LEC.trajectoriel(0)[0] == "conforme" and LEC.trajectoriel(2)[0] == "contraire"


def test_table_E_et_blocs_de_lecture():
    preds = {p for ligne in LEC.LIGNES_E for p in ligne["exiges"] + ligne["complementaires"]}
    assert {p.split(".")[0] for p in preds} <= set(LEC.BLOCS_DE)
    faux = {"predictions": {p: {"verdict": "confirmée"} for p in preds}}
    assert all(not x["lecture"].startswith("non établi") for x in LEC.enonces_du_programme(faux))
    faux["predictions"]["HE2.5"]["verdict"] = "non concluante"
    lignes = LEC.enonces_du_programme(faux)
    assert sum(x["lecture"].startswith("non établi") for x in lignes) == 1


# --- chaîne complète sur une mini-grille (non décisive) ---
def _mini_grille():
    pan = {"somme": "exact", "max": "exact", "comptage": "exact", "agent_moyenne": "exact", "agent_comptage": "exact",
           "pas_moyenne": "exact", "coelev_comptage": "exact", "coelev_somme3": "mc", "e_coelev_cal": "mc",
           "e_coelev_ville": "ville", "ed_coelev": "mc", "e_pas_ville": "ville"}
    pan3 = {k: v for k, v in pan.items() if v != "mc"}

    def specs_c(K, T):
        return [{"nom": "A_rebrassage", "genre": "rebrassage_agents", "groupe": "agents"},
                {"nom": f"A_routage_un_m{T}", "genre": "routage", "groupe": "agents", "m": T, "k_dest": 1,
                 "lecture_par_agent": "au_dessus"},
                {"nom": f"A_relais_m{T}", "genre": "routage", "groupe": "agents", "m": T, "k_dest": K,
                 "lecture_par_agent": "en_dessous"},
                {"nom": "T_rebrassage", "genre": "rebrassage_temps", "groupe": "temps"},
                {"nom": f"T_synchro_m{K}", "genre": "synchro", "groupe": "temps", "m": K, "r": 1,
                 "lecture_au_dessus": ["coelev_comptage", "pas_moyenne", "coelev_somme3"],
                 "lecture_e": {"e_coelev_cal": "au_plus", "ed_coelev": "au_plus"}},
                {"nom": "I_rebrassage", "genre": "rebrassage_tout", "groupe": "tout"}]

    def specs_m(K, T):
        return [{"nom": "M_concentre_B4", "genre": "concentre", "B": 4.0, "m": 1},
                {"nom": f"M_synchro_B6_m{K}", "genre": "synchro", "B": 6.0, "m": K},
                {"nom": f"M_temps_B6_m{T}", "genre": "temps", "B": 6.0, "m": T}]

    return {
        "version": "mini", "alpha": ALPHA, "q": Q, "fractions_lambda": list(S.FRACTIONS_LAMBDA),
        "tailles": {"R": 400, "R_cal": 2000, "R0": 2000, "equivalence": 4},
        "replication": {"facteur_R": 2}, "lecture": {"gamma": 1e-5},
        "configs": {"m3x6": {"K": 3, "T": 6, "panneau": pan}, "m4x5": {"K": 4, "T": 5, "panneau": pan},
                    "m3x8": {"K": 3, "T": 8, "panneau": pan3}},
        "C": {"m3x6": specs_c(3, 6), "m4x5": specs_c(4, 5)},
        "M": {"m3x6": specs_m(3, 6), "m4x5": specs_m(4, 5)},
        "HE3": {"configs": ["m3x6", "m3x8"],
                "lois": [{"nom": "iid", "loi": {"type": "iid", "marginale": "gauss"}},
                         {"nom": "tau0.2", "loi": {"type": "effet_episode", "tau": 0.2}},
                         {"nom": "c0.4", "loi": {"type": "equicorrelation", "c": 0.4}}],
                "alarmes": ["somme", "max", "comptage", "agent_moyenne", "agent_comptage", "pas_moyenne", "coelev_comptage",
                            "e_coelev_ville", "e_pas_ville"],
                "conforme": {"K": 40, "n_test": 30, "L": 3,
                             "statistiques": ["coelev_comptage", "e_coelev", "e_pas", "agent_moyenne"]},
                "lecture": {"depasse": {"tau0.2": ["e_pas_ville"], "c0.4": ["e_pas_ville"]}}},
        "HE6": {"configs": ["m4x5"],
                "lois": [{"nom": "c0.4", "loi": {"type": "equicorrelation", "c": 0.4}}],
                "alarmes": ["somme", "max", "comptage", "agent_moyenne", "agent_comptage", "pas_moyenne",
                            "coelev_comptage", "coelev_somme3", "e_coelev", "ed_coelev"],
                "arrangements": [{"nom": "T_synchro_m2", "genre": "synchro", "groupe": "temps", "m": 2, "r": 1},
                                 {"nom": "T_synchro_m4", "genre": "synchro", "groupe": "temps", "m": 4, "r": 1}],
                "lecture": {"c0.4": {"T_synchro_m4": {"coelev_comptage": "au_dessus", "pas_moyenne": "au_dessus"}}}},
    }


def _contexte(grille):
    from controle_ia.manifeste import graines
    from controle_ia.simulation_essaim.run_essaim import taches

    return B.Contexte(grille, graines(taches(grille), entropie=987654321))


PREREG_MINI = "# Mini préenregistrement de test\n\n- Commit du code d'analyse : `{commit}`\n- Grille : {sha}\n\n" + "\n\n".join(
    f"## {s}\n\nTexte de test." for s in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil",
                                           "Plan d'analyse", "Critères de lecture gelés", "Liste d'arrêt")) + (
    "\n\n## Contre-lecture\n\nTexte de test : brouillon `" + "a" * 64 + "`, rapport `" + "b" * 64 + "`.\n")


def _preparer(depot, grille=None):
    from controle_ia.prereg import sceller_prereg
    from controle_ia.scellement import sceller

    grille = grille or _mini_grille()
    (depot / "src").mkdir(exist_ok=True)
    (depot / "src" / "code_factice.py").write_text("X = 1\n", encoding="utf-8")
    gp = depot / "grille.json"
    gp.write_text(json.dumps(grille), encoding="utf-8")
    sha = sceller(gp)
    committer(depot)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    pp = depot / "prereg.md"
    pp.write_text(PREREG_MINI.format(sha=sha, commit=commit), encoding="utf-8")
    sceller_prereg(pp)
    committer(depot)
    return pp, gp


ATTENDUES = {"HE1.1", "HE1.2", "HE1.3", "HE2.1", "HE2.2", "HE2.3", "HE2.4", "HE2.5", "HE3.1", "HE3.2", "HE3.3", "HE3.4",
             "HE3.5", "HE3.6", "HE4.1", "HE4.2", "HE4.3", "HE4.4", "HE5.1", "HE5.2", "HE6.1", "HE6.2", "HE6.3"}


def test_chaine_complete_mini_grille(depot):
    from controle_ia.manifeste import lire_manifeste, verifier_resultat
    from controle_ia.scellement import empreinte
    from controle_ia.simulation_essaim.run_essaim import entropie_depuis_prereg, executer

    pp, gp = _preparer(depot)
    sortie = executer(depot, pp, gp, "20261101-120000-mini", verifier_import=False)
    corps = verifier_resultat(depot, sortie["lecture"])
    lec = corps["resultat"]["lecture"]
    assert set(lec["predictions"]) == ATTENDUES
    for p in ("HE1.1", "HE2.1", "HE4.4", "HE5.2", "HE6.1"):           # trajectoriels : exacts même en petit
        assert lec["predictions"][p]["verdict"] == "confirmée", (p, lec["predictions"][p])
    he6 = corps["resultat"]["lecture"]["predictions"]["HE6.2"]["cellules"]
    assert {c["nom"].split("/")[-1] for c in he6} == {"somme", "max", "comptage", "agent_moyenne", "agent_comptage"}
    bloc6 = json.loads((depot / "diag" / "20261101-120000-mini" / "bloc-HE6.json").read_text(encoding="utf-8"))
    assert len(bloc6["resultat"]["calibrages"]) == 1 and len(bloc6["resultat"]["cellules"]) == 2
    assert set(lec["audit_symetrie"]) == {"bornes", "formes_closes", "egalites", "audit_declenche"}
    assert len(corps["resultat"]["programme"]) == len(LEC.LIGNES_E)
    m, _ = lire_manifeste(depot / "runs" / "20261101-120000-mini" / "manifeste.json")
    assert int(m["config"]["entropie"]) == entropie_depuis_prereg(empreinte(pp))       # règle de la graine
    assert all(x["entropie"] == m["config"]["entropie"] for x in m["graines"].values())
    assert (depot / "diag" / "20261101-120000-mini" / "lecture.md").exists()
    # un seul run décisif principal par préenregistrement
    with pytest.raises(GardeArret, match="existe déjà"):
        executer(depot, pp, gp, "20261101-120001-mini", verifier_import=False)
    # artefact : grille non citée par le préenregistrement
    from controle_ia.prereg import sceller_prereg

    pp2 = depot / "prereg2.md"
    pp2.write_text(PREREG_MINI.format(sha="0" * 64, commit="0" * 40), encoding="utf-8")
    sceller_prereg(pp2)
    committer(depot)
    with pytest.raises(GardeArret, match="ne cite pas"):
        executer(depot, pp2, gp, "20261101-120002-mini", verifier_import=False)


def test_replication_determinee_par_la_lecture(depot):
    from controle_ia.simulation_essaim.run_essaim import executer

    pp, gp = _preparer(depot)
    executer(depot, pp, gp, "20261101-121000-mini", verifier_import=False)
    lec = json.loads((depot / "diag" / "20261101-121000-mini" / "lecture.json").read_text(encoding="utf-8"))
    a_repliquer = {k for k, x in lec["resultat"]["lecture"]["predictions"].items() if x["a_repliquer"]}
    if not a_repliquer:
        with pytest.raises(GardeArret, match="rien à répliquer"):
            executer(depot, pp, gp, "20261101-121001-mini", replication_de="20261101-121000-mini", verifier_import=False)
    else:
        sortie = executer(depot, pp, gp, "20261101-121001-mini", replication_de="20261101-121000-mini",
                          verifier_import=False)
        assert "lecture" in sortie
        with pytest.raises(GardeArret, match="existe déjà"):
            executer(depot, pp, gp, "20261101-121002-mini", replication_de="20261101-121000-mini", verifier_import=False)


# --- gardes de la liste d'arrêt : artefacts (R5) ; le cas sain est la chaîne complète ci-dessus ---
def test_garde_commit_cite_et_blocs(depot):
    from controle_ia.simulation_essaim.run_essaim import executer

    pp, gp = _preparer(depot)
    with pytest.raises(GardeArret, match="ne se choisissent pas"):
        executer(depot, pp, gp, "20261101-130000-mini", blocs=["C"], verifier_import=False)
    (depot / "src" / "code_factice.py").write_text("X = 2\n", encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret, match="modifiés depuis le commit cité"):
        executer(depot, pp, gp, "20261101-130001-mini", verifier_import=False)


def test_garde_prereg_non_scelle(depot):
    from controle_ia.simulation_essaim.run_essaim import executer

    pp, gp = _preparer(depot)
    pp.write_text(pp.read_text(encoding="utf-8") + "\nModifié après scellement.\n", encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret):
        executer(depot, pp, gp, "20261101-130002-mini", verifier_import=False)


def test_garde_duree_artefact(depot):
    from controle_ia.simulation_essaim.run_essaim import executer

    pp, gp = _preparer(depot)
    with pytest.raises(GardeArret, match="durée"):
        executer(depot, pp, gp, "20261101-130003-mini", limite_s=0.0, verifier_import=False)


def test_garde_calibrage_artefact(depot, monkeypatch):
    from controle_ia.simulation_essaim.run_essaim import executer

    pp, gp = _preparer(depot)
    vrai = C.seuils_exacts

    def faux(K, T, q, alpha):
        s = vrai(K, T, q, alpha)
        s["pas_moyenne"] = (s["pas_moyenne"][0] - 0.8, 1.0)              # seuil exact faux : taux sous P₀ ≠ α
        return s

    monkeypatch.setattr(C, "seuils_exacts", faux)
    with pytest.raises(GardeArret, match="garde de calibrage"):
        executer(depot, pp, gp, "20261101-130004-mini", verifier_import=False)


def test_garde_p0_saine_et_artefacts():
    res = {"cfg": "x", "R0": 100000, "R_cal": 100000,
           "alarmes_p0": {"a": 5000, "b": 5150, "c": 1700}, "genres": {"a": "exact", "b": "mc", "c": "ville"}}
    assert B.garde_p0(res, ALPHA, 1e-5) == []
    mauvais = copy.deepcopy(res)
    mauvais["alarmes_p0"].update({"a": 6000, "b": 4000, "c": 6000})
    assert len(B.garde_p0(mauvais, ALPHA, 1e-5)) == 3
    sans_calibrage = copy.deepcopy(res)
    sans_calibrage["R_cal"] = 0                                         # seuil Monte-Carlo sans échantillon
    assert B.garde_p0(sans_calibrage, ALPHA, 1e-5) == ["x/b : seuil Monte-Carlo sans échantillon de calibrage"]


def test_garde_equivalence_artefact(depot, monkeypatch):
    from controle_ia.simulation_essaim.run_essaim import executer

    pp, gp = _preparer(depot)
    vrai = S.agent_moyenne
    monkeypatch.setattr(S, "agent_moyenne", lambda Xb: vrai(Xb) + 1e-6)
    with pytest.raises(GardeArret, match="équivalence"):
        executer(depot, pp, gp, "20261101-130005-mini", verifier_import=False)


def test_garde_multiensemble_artefact(depot, monkeypatch):
    from controle_ia.simulation_essaim.run_essaim import executer

    pp, gp = _preparer(depot)
    vrai = M.routage

    def faux(Xb, m, k_dest, rng):
        X = vrai(Xb, m, k_dest, rng).copy()
        X[:, 0, 0] += 1.0
        return X

    monkeypatch.setattr(M, "routage", faux)
    with pytest.raises(GardeArret, match="non préservé"):
        executer(depot, pp, gp, "20261101-130006-mini", verifier_import=False)


def test_garde_calibrage_HE6_artefact(monkeypatch):
    """Cas sain : le bloc HE6 passe sa garde de calibrage sur essaims corrélés entiers ; artefact : un seuil faux
    (taux sous P₀ corrélée ≠ α) arrête le run."""
    grille = _mini_grille()
    ctx = _contexte(grille)
    sortie = B.bloc_HE6(ctx)
    assert len(sortie["cellules"]) == 2 and sortie["calibrages"][0]["R0"] == 2000
    monkeypatch.setattr(C, "seuil_mc", lambda v, a: (float(np.quantile(v, 0.5)), 1.0))
    with pytest.raises(GardeArret, match="garde de calibrage HE6"):
        B.bloc_HE6(_contexte(grille))


def test_garde_seuil_non_fini(depot, monkeypatch):
    from controle_ia.simulation_essaim.run_essaim import executer

    pp, gp = _preparer(depot)
    monkeypatch.setattr(C, "seuil_mc", lambda v, a: (math.inf, 0.0))
    with pytest.raises(GardeArret, match="non finis"):
        executer(depot, pp, gp, "20261101-130007-mini", verifier_import=False)
