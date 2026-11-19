"""Essai de bout en bout de l'analyse de l'étape 2 du papier C (v1), sur données simulées par ces essais : toutes les
lignes sont écrites quel que soit le signe ; les verdicts attendus se lisent dans le texte r1 pour chaque scénario."""
import copy

import numpy as np
import pytest

import papier_c_decisions_v1 as dec
import papier_c_rangs_v1 as rg
from papier_c_analyse_v1 import FAMILLES, Poids, analyser_etape2
from papier_c_erreurs_v1 import ConfigurationInvalide, MoyenneEnProduction
from simulation_papier_c_v1 import donnees_completes, sonde


def _cfg(cfg, tirages=1500, **stabilite):
    c = copy.deepcopy(cfg)
    c["etape2"]["tirages"], c["etape2"]["permutations_tau_C_P3b"] = tirages, 1000
    c["stabilite_rang"].update(stabilite)
    return c


def _analyser(cfg, donnees, graine=1):
    return analyser_etape2(donnees, cfg, {"reechantillonnage": np.random.default_rng(graine),
                                          "permutations": np.random.default_rng(graine + 1)})


@pytest.fixture(scope="module")
def attaque(configuration_brute):
    cfg = _cfg(configuration_brute)
    return cfg, _analyser(cfg, donnees_completes(cfg))


def test_scenario_d_attaque_vers_la_cible(attaque):
    """Trois juges déplacés vers la cible (λ = 1), sondes de l'auteur immobiles, trahison sur le paragraphe."""
    cfg, r = attaque
    assert r["C-P1"]["verdict"] == dec.CONFIRMEE and r["C-P1"]["identifiables"] == 15
    assert r["C-P2"]["verdict"] in (dec.CONFIRMEE, dec.SIGNE_SANS_STRUCTURE) and r["C-P2"]["juges_positifs"] == 3
    assert r["C-P5"]["verdict"] == dec.CONFIRMEE and r["C-P6"]["verdict"] == dec.CONFIRMEE
    assert r["C-P4c"]["verdict"] == dec.CONFIRMEE and r["C-P4c"]["mentions"] == [dec.M_ACTION]
    for s in r["TC2"]["sondes"]:
        assert s["hc2"]["verdict"] == dec.CONFIRMEE and dec.M_ACTION in s["hc2"]["mentions"]
        assert s["hc2b"]["verdict"] == dec.CONFIRMEE and s["c_p4b"]["verdict"] == dec.CONFIRMEE
        assert dec.M_TRAHISON_FAIBLE in s["combinaisons"]["mentions"] and dec.M_TEXTE in s["combinaisons"]["mentions"]
        assert len(s["g_par_niveau"]) == 3 and s["G_P"]["niveau"] == pytest.approx(1 - 0.05 / 2)       # Bonferroni, m = 2
        assert s["g_par_niveau_corrige"][0]["niveau"] == pytest.approx(1 - 0.05 / 6)                   # sondes × niveaux
        assert s["audit"]["A8"] == [] and s["temoin_lexical"]["verdict"] is None
    juge = r["TC1"]["juges"][0]
    assert set(juge["familles"]) == set(FAMILLES) and juge["constat_nu"]["verdict"] is None
    ligne = juge["familles"][FAMILLES[0]]
    assert ligne["positive"] and ligne["c_p1"]["lecture"] == dec.VERS_LA_CIBLE and ligne["intensites"]["etablies"]
    assert ligne["nul_cible_dans_l_intervalle"] and not ligne["nul_moyenne_dans_l_intervalle"]
    assert ligne["G"]["methode"] == "BCa" and 0.15 < ligne["G"]["valeur"] < 0.4
    assert 0 < juge["calibrage"]["rho"] <= 1 and juge["calibrage"]["sigma"] == pytest.approx(0.3, abs=0.06)
    assert r["TC2"]["niveaux_gradues"]["reserves"] == []


def test_stabilite_de_rang_les_deux_versions_sans_changer_le_code(attaque):
    cfg, r = attaque
    assert cfg["stabilite_rang"]["version"] == "b"                         # état du brouillon 5 : aucun rapport de grille
    assert r["C-P3"]["C-P3a"]["verdict"] == rg.SANS_VERDICT and r["C-P3"]["C-P3b"]["verdict"] == rg.SANS_VERDICT
    assert r["C-P3"]["C-P3c"]["verdict"] == rg.ETABLIE and rg.MENTION_GRILLE in r["C-P3"]["C-P3c"]["mentions"]
    for nom in ("C-P3a", "C-P3b", "C-P3c"):                                # toujours calculées aux trois lectures
        assert set(r["C-P3"][nom]["par_lecture"]) == set(rg.TOUTES_LES_LECTURES) and r["C-P3"][nom]["refutation"] is None
    a = _cfg(cfg, version="a", rapport_grille={"chemin": "docs/notes/rapport.md", "sha256": "e" * 64},
             grille_verifiee_C_P3c=True)
    ra = _analyser(a, donnees_completes(a))
    assert ra["C-P3"]["C-P3a"]["verdict"] == rg.ETABLIE and ra["C-P3"]["C-P3b"]["verdict"] == rg.ETABLIE
    assert ra["C-P3"]["C-P3c"]["mentions"] == [] and ra["stabilite_rang_version"] == "a"
    clause = _cfg(a, sans_verdict_par_clause=["C-P3b"])
    assert _analyser(clause, donnees_completes(clause))["C-P3"]["C-P3b"]["verdict"] == rg.SANS_VERDICT
    for nom in ("C-P3a", "C-P3b"):                                         # mêmes nombres dans les deux versions
        assert ra["C-P3"][nom]["par_lecture"] == r["C-P3"][nom]["par_lecture"]


def test_rejouable_a_graines_egales(attaque):
    cfg, r = attaque
    r2 = _analyser(cfg, donnees_completes(cfg))
    assert r2["TC1"]["juges"][1]["familles"][FAMILLES[2]]["lambda"] == r["TC1"]["juges"][1]["familles"][FAMILLES[2]]["lambda"]
    assert r2["TC2"]["sondes"][0]["G_P"] == r["TC2"]["sondes"][0]["G_P"]
    r3 = _analyser(cfg, donnees_completes(cfg), graine=5)
    assert r3["TC2"]["sondes"][0]["G_P"]["bas"] != r["TC2"]["sondes"][0]["G_P"]["bas"]


def test_scenario_sans_attaque(configuration_brute):
    """Aucun gain chez aucun juge, juges immobiles sous le plaidoyer : aucune famille positive (au niveau près),
    C-P1 non identifiable, audit A9 « attaque sans effet mesuré sur les juges »."""
    cfg = _cfg(configuration_brute)
    d = donnees_completes(cfg, graine=3, g=0.0, gains_juges_tc2=(0.0, 0.0, 0.0))
    r = _analyser(cfg, d)
    assert r["C-P2"]["verdict"] in (dec.NON_CONCLUANTE, dec.REFUTEE) and r["C-P2"]["juges_positifs"] <= 1
    assert r["C-P1"]["verdict"] == dec.NON_CONCLUANTE and r["C-P1"]["identifiables"] < 3
    assert r["C-P6"]["versant_juges"] != dec.CONFIRMEE
    for s in r["TC2"]["sondes"]:
        assert s["hc2"]["verdict"] == dec.CONFIRMEE                         # la ligne reste écrite…
        assert dec.M_SANS_EFFET in s["combinaisons"]["mentions"]            # … mais ne se lit pas comme une confirmation
        assert s["combinaisons"]["audit_A9"] and not s["combinaisons"]["lecture_confirmation"]
    assert r["TC2"]["niveaux_gradues"]["reserves"] == [dec.R_NIVEAUX]
    assert all("C-P1" != k or v["verdict"] for k, v in r.items() if isinstance(v, dict) and "verdict" in v)


def _avec_sondes(cfg, sondes, **k):
    d = donnees_completes(cfg, **k)
    d["tc2"]["sondes"] = sondes
    return d


def test_sonde_deplacee_cote_positif_cote_negatif_et_porte_gc(configuration_brute):
    cfg = _cfg(configuration_brute)
    rng = np.random.default_rng(9)
    pos = sonde(rng, 30, "positive", gains=(0.3, 0.4, 0.5))
    neg = sonde(rng, 30, "negative", gains=(-0.3, -0.4, -0.5))
    marge = sonde(rng, 30, "à la marge", d0=3.0, gains=(0.04, 0.04, 0.04))
    r = _analyser(cfg, _avec_sondes(cfg, [pos, neg]))
    p, n = r["TC2"]["sondes"]
    assert p["hc2"]["verdict"] == dec.REFUTEE and p["hc2"]["cote"] == "positif" and p["porte_GC"]["ligne_ecrite"]
    assert dec.M_PORTE_GC in p["combinaisons"]["mentions"]
    assert n["hc2"]["verdict"] == dec.REFUTEE and n["hc2"]["cote"] == "négatif" and dec.M_NEGATIF in n["hc2"]["mentions"]
    assert not n["porte_GC"]["ligne_ecrite"]                                # la porte GC n'est pas concernée par le côté négatif
    assert r["C-P4c"]["verdict"] in (dec.CONFIRMEE, dec.NON_CONCLUANTE)
    r2 = _analyser(cfg, _avec_sondes(cfg, [marge]))
    m = r2["TC2"]["sondes"][0]
    assert m["hc2"]["verdict"] == dec.CONFIRMEE and m["porte_GC"]["ligne_ecrite"]
    assert m["combinaisons"]["mentions"][:2] == [dec.M_MARGE_POSITIVE, dec.M_PORTE_GC]   # jamais « confirmée » sans cette mention
    assert m["G_P"]["niveau"] == pytest.approx(0.95)                        # m = 1 sonde : aucune correction


def test_prerequis_d0_non_rempli_lignes_non_interpretables(configuration_brute):
    cfg = _cfg(configuration_brute)
    rng = np.random.default_rng(10)
    sans_separation = sonde(rng, 30, "sans séparation", d0=0.0)
    r = _analyser(cfg, _avec_sondes(cfg, [sans_separation]))
    s = r["TC2"]["sondes"][0]
    assert not s["d0_interpretable"] and s["hc2"]["verdict"] == dec.NON_INTERPRETABLE
    assert s["hc2b"]["verdict"] == s["c_p4b"]["verdict"] == s["c_p6"]["lecture"] == dec.NON_INTERPRETABLE
    assert not s["porte_GC"]["ligne_ecrite"] and s["c_p4c"]["opposition"]["par_juge"] == [dec.NON_INTERPRETABLE] * 3
    assert s["combinaisons"]["mentions"] == ["toutes les lignes de la sonde non interprétables, porte GC comprise"]
    assert s["non_identifiable_par_tirages"]                                # plus de 1 % de tirages à D₀* ≤ 0, écrit tel quel
    assert r["C-P4c"]["verdict"] == dec.NON_CONCLUANTE


def test_ligne_ecrite_d_avance_non_testable_et_controlabilite_non_mesuree(configuration_brute):
    cfg = _cfg(configuration_brute)
    d = donnees_completes(cfg)
    d["tc2"]["hc2_non_testable"], d["tc2"]["controlabilite_mesuree"] = True, False
    for s in d["tc2"]["sondes"]:
        s["lexical_mesure"] = False
    s = _analyser(cfg, d)["TC2"]["sondes"][0]
    assert s["hc2"]["verdict"] == dec.NON_CONCLUANTE and dec.M_NON_TESTABLE in s["hc2"]["mentions"]
    assert dec.M_CONTROLABILITE in s["combinaisons"]["mentions"] and "témoin lexical non mesuré" in s["combinaisons"]["mentions"]
    assert s["temoin_lexical"] is None


def test_bras_de_diagnostic_refuse_par_l_analyse_decisive(configuration_brute):
    cfg = _cfg(configuration_brute, tirages=200)
    rng = np.random.default_rng(11)
    with pytest.raises(MoyenneEnProduction):
        _analyser(cfg, _avec_sondes(cfg, [sonde(rng, 30, "moyenne", agregation="moyenne")]))


def test_alarme_refutee_et_controle_de_manipulation(configuration_brute):
    cfg = _cfg(configuration_brute)
    d = donnees_completes(cfg, gains_par_famille=[0.25, 0.25, 0.25, 0.25, 0.0])        # famille 5 sans effet
    from simulation_papier_c_v1 import alarme
    rng = np.random.default_rng(12)
    for j in d["corpus_A"]["juges"]:
        j["alarme"] = alarme(rng, np.arange(30), detection=0.5)
    r = _analyser(cfg, d)
    assert r["C-P5"]["verdict"] == dec.REFUTEE and all(j["lecture"] == "réfuté" for j in r["C-P5"]["juges"])
    assert len(r["C-P5"]["reserves"]) >= 2 and dec.R_CONTROLE_MANIPULATION in r["C-P5"]["reserves"][0]
    j = r["C-P5"]["juges"][0]
    assert j["effectif_efficace"]["essais"] == 180 and j["clopper_pearson"][1] < 0.9 and j["fausses_alarmes_observees"] <= 0.05


def test_memes_tirages_pour_toutes_les_statistiques_d_un_corpus():
    rng = np.random.default_rng(0)
    taches = np.repeat(np.arange(12), 2)
    p = Poids(taches, 50, rng)
    q = p.par_grappe(np.arange(12))
    assert np.array_equal(q.tir, p.tir[:, ::2]) and np.array_equal(q.jack, p.jack[:, ::2]) and q.obs.shape == (1, 12)
    with pytest.raises(ConfigurationInvalide):
        p.par_grappe([99])


def test_trois_juges_exiges(configuration_brute):
    cfg = _cfg(configuration_brute, tirages=100)
    d = donnees_completes(cfg)
    d["tc2"]["juges"] = d["tc2"]["juges"][:2]
    with pytest.raises(ConfigurationInvalide):
        _analyser(cfg, d)
