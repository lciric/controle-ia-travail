"""Essais des statistiques de l'erratum 1 (statistiques_v1) : cas calculables à la main, cas sains et artefacts."""
import itertools

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sondes_v2 import statistiques_v1 as st

SEUILS = {"alpha": 0.05, "u_fort": 0.9}


def test_holm():
    assert st.holm([0.01, 0.04, 0.03]) == pytest.approx([0.03, 0.06, 0.06])
    assert st.holm([0.5]) == [0.5]
    assert st.holm([0.2, 0.2]) == pytest.approx([0.4, 0.4])
    with pytest.raises(GardeArret):
        st.holm([1.5])


def test_regime_et_libelles():
    assert st.regime_effectif(8, 40) == "libellé"
    assert st.regime_effectif(8, 39) == "grandeurs"
    assert st.regime_effectif(5, 100) == "grandeurs"
    assert st.regime_effectif(3, 100) == "non calculable"
    assert st.regime_effectif(3, 100, {"taches_libelle": 2, "actions_libelle": 1, "taches_grandeurs": 2}) == "libellé"
    assert st.libelle_signe(1.0, 0.01, 0.004, SEUILS) == "établie"
    assert st.libelle_signe(-1.0, 0.01, 0.004, SEUILS) == "contraire"
    assert st.libelle_signe(1.0, 0.2, 0.004, SEUILS) == "non établie à cette puissance"
    assert st.libelle_signe(1.0, 0.0625, 0.0625, SEUILS) == "non testable à cet effectif"
    assert st.libelle_signe(1.0, 0.05, 0.004, SEUILS) == "établie"  # « au plus le seuil »
    assert st.libelle_transport(0.95, 0.01, 0.05) == "fort"
    assert st.libelle_transport(0.9, 0.05, 0.05) == "fort"
    assert st.libelle_transport(0.7, 0.01, 0.05) == "faible"
    assert st.libelle_transport(0.2, 0.01, 0.05) == "contraire"
    assert st.libelle_transport(0.5, 0.01, 0.05) == "non établi à cette puissance"
    assert st.libelle_transport(0.95, 0.2, 0.05) == "non établi à cette puissance"
    assert st.libelle_transport(0.7, 0.01, 0.05, plancher_q95=0.8).endswith("non la direction apprise")


def test_familles_testables_et_holm():
    assert st.familles_testables({"a": 7}) == ["a"]
    assert st.familles_testables({"a": 6}) == []
    assert st.familles_testables({"a": 7, "b": 7}) == []          # 2^-5 > 0,025
    assert st.familles_testables({"a": 8, "b": 8, "c": 8}) == ["a", "b", "c"]
    assert st.familles_testables({"a": 8, "b": 8, "c": 8, "d": 8}) == []  # 2^-6 > 0,0125 ; puis 3 restent ? non : tous
    assert st.familles_testables({"a": 9, "b": 9, "c": 9, "d": 9}) == ["a", "b", "c", "d"]
    assert st.familles_testables({"a": 9, "b": 7, "c": 4}) == ["a"]   # b retiré à m = 2, puis a seul
    r = {f: {"etat": "calculé", "P": 9, "U": U, "p_bilaterale": p} for f, U, p in
         (("a", 0.95, 0.004), ("b", 0.7, 0.03), ("c", 0.95, 0.04), ("d", 0.95, 0.004))}
    e = st.etalon_familles(r)
    assert e["seuils_holm"]["a"] == pytest.approx(0.0125) and e["libelles"]["a"] == "fort"
    assert e["libelles"]["b"] == "non établi à cette puissance"  # 0,03 > 0,05/2 : arrêt de Holm
    assert e["libelles"]["c"] == "non établi à cette puissance"
    r2 = {"x": {"etat": "calculé", "P": 5, "U": 1.0, "p_bilaterale": 0.125}, "y": {"etat": "non calculable"}}
    assert st.etalon_familles(r2)["libelles"] == {"x": "non testable à cet effectif", "y": "non calculable"}


def test_libelle_identite():
    c = lambda a, bas, nul: {"aire": a, "intervalle_95": [bas, 1.0], "nul_quantile_95": nul}
    forts = {str(i): c(0.95, 0.9, 0.6) for i in range(5)}
    assert st.libelle_identite(forts) == "identité forte"
    forts["0"] = c(0.95, 0.5, 0.6)
    forts["1"] = c(0.95, 0.5, 0.6)
    assert st.libelle_identite(forts) == "intermédiaire"  # 3 sur 5 au-dessus < ⌈4⌉
    faibles = {str(i): c(0.55, 0.4, 0.6) for i in range(5)}
    assert st.libelle_identite(faibles) == "identité faible"
    assert st.libelle_identite({"a": c(0.95, 0.9, 0.6), "b": c(0.95, 0.9, 0.6)}) is None
    assert st.changement_signe(np.ones(25), np.random.default_rng(0))["tirages"] == 10_000


def _brute_U(X, P):
    S, J = X[:P], X[P:]
    d = S - J
    c, h = [], []
    for p, q in itertools.permutations(range(P), 2):
        w = np.delete(d, [p, q], axis=0).mean(axis=0)
        c.append(w @ (S[p] - J[q]))
        h.append(w @ (J[p] - J[q]))
    c, h = np.array(c), np.array(h)
    return float(np.mean(c > 0)), float(np.median(c - h) / np.median(np.abs(h)))


def _moyennes(P, d=16, trace=0.0, graine=0, intensite=0.0):
    rng = np.random.default_rng(graine)
    t = np.zeros(d)
    t[0] = 1.0
    u = np.zeros(d)
    u[1] = 1.0
    m = {}
    for p in range(P):
        o = 3 * rng.standard_normal(d) / np.sqrt(d) + intensite * u
        gap = rng.standard_normal(d)
        gap /= np.linalg.norm(gap)
        m[f"J{p}"] = o
        m[f"S{p}"] = o + gap + trace * t + 0.2 * intensite * u
    return m, [(f"S{p}", f"J{p}") for p in range(P)]


def test_etalon_formule_contre_force_brute():
    m, paires = _moyennes(6, trace=0.5)
    r = st.diagnostic_etalon_transport(m, paires, np.random.default_rng(0))
    X = np.stack([m[s] for s, _ in paires] + [m[j] for _, j in paires])
    U, rho = _brute_U(X, 6)
    assert r["U"] == pytest.approx(U) and r["rho"] == pytest.approx(rho)
    assert r["exact"] and r["echanges"] == 64 and r["p_minimale"] == pytest.approx(2 ** (2 - 6))
    assert r["p_bilaterale"] == min(1.0, 2 * min(r["p_haut"], r["p_bas"]))
    assert r["controle_intensite"] == "contrôle d'intensité absent"


def test_etalon_trace_forte_et_identite():
    m, paires = _moyennes(8, trace=6.0)
    r = st.diagnostic_etalon_transport(m, paires, np.random.default_rng(0))
    assert r["U"] == 1.0 and r["p_haut"] == pytest.approx(2 / 256)
    assert st.etalon_familles({"f": r})["libelles"]["f"] == "fort"
    assert all(v > 0 for v in r["deplacement_apparie"].values())
    m, paires = _moyennes(8, trace=0.0, graine=3)
    r = st.diagnostic_etalon_transport(m, paires, np.random.default_rng(0))
    assert st.etalon_familles({"f": r})["libelles"]["f"] in ("non établi à cette puissance", "faible", "contraire")
    m, paires = _moyennes(3)
    assert st.diagnostic_etalon_transport(m, paires, np.random.default_rng(0))["etat"] == "non calculable"
    with pytest.raises(GardeArret):
        st.diagnostic_etalon_transport(m, [("S0", "J0")] * 4, np.random.default_rng(0))


def test_etalon_tirages_au_dela_de_16():
    m, paires = _moyennes(17, trace=6.0)
    r = st.diagnostic_etalon_transport(m, paires, np.random.default_rng(1))
    assert not r["exact"] and r["echanges"] == 10_000 and r["p_minimale"] == pytest.approx(2 / 10_001)


def test_etalon_controle_intensite_plancher_variante():
    m, paires = _moyennes(7, intensite=40.0, graine=2)
    nu = np.zeros(16)
    rng = np.random.default_rng(0)
    jumeaux = [rng.standard_normal((3, 16)) + m[j] for _, j in paires]
    jetons = {k: [rng.standard_normal((3, 16)) * 0.01 + v] for k, v in m.items()}
    r = st.diagnostic_etalon_transport(m, paires, np.random.default_rng(0), np.random.default_rng(1), jumeaux, nu,
                                       jetons, n_plancher=50)
    ci = r["controle_intensite"]
    assert r["U"] > 0.9  # l'écart d'intensité fabrique un transport
    assert ci["U_apres_retrait"] < r["U"]  # le contrôle le fait retomber
    assert all(v > 1.0 for v in ci["rapports_normes"].values())
    assert r["plancher"]["n"] == 50 and 0 <= r["plancher"]["quantile_95_U"] <= 1
    assert r["variante_production"]["U"] == pytest.approx(r["U"], abs=0.1)


def _jumeaux(n=4, taches=8, par_tache=3, decalage=3.0, graine=0, d=12):
    rng = np.random.default_rng(graine)
    base = {f"t{t}-a{a}": (f"t{t}", rng.standard_normal((4, d))) for t in range(taches) for a in range(par_tache)}
    out = {}
    for j in range(n):
        o = decalage * rng.standard_normal(d) / np.sqrt(d)
        out[f"J{j}"] = {c: (t, x + o + 0.05 * rng.standard_normal(x.shape)) for c, (t, x) in base.items()}
    return out


def _rngs():
    return {n: np.random.default_rng(i) for i, n in enumerate(st.GRAINES_NOMMEES)}


def test_sonde_identite():
    r = st.sonde_identite(_jumeaux(n=5), _rngs(), n_tirages=200, n_nul=50)
    assert r["jumeaux_ecartes"] == 1 and len(r["couples"]) == 2
    for c in r["couples"].values():
        assert c["aire"] > 0.9 and c["aire"] > c["nul_quantile_95"]
        assert c["intervalle_95"][0] <= c["aire"] + 1e-9 and len(c["aires_plis"]) == 4
    assert "non calculés" in r["predicteurs_triviaux"]
    nul = st.sonde_identite(_jumeaux(n=2, decalage=0.0), _rngs(), n_tirages=100, n_nul=50)
    (c,) = nul["couples"].values()
    assert c["aire"] < 0.9
    with pytest.raises(GardeArret, match="quatre tâches"):
        st.sonde_identite(_jumeaux(n=2, taches=3), _rngs(), n_tirages=10, n_nul=5)
    with pytest.raises(GardeArret, match="deux jumeaux"):
        st.sonde_identite(_jumeaux(n=1), _rngs())


def _table(n_taches=10, inter=1.0, ecart_chemin=0.0, avec_relu=True, graine=0):
    """Table fabriquée : scores = base de texte + effets ; origine = (adaptateur, saboteur) et (nu, honnête)."""
    rng = np.random.default_rng(graine)
    lignes = []
    for t in range(n_taches):
        for so in ("saboteur", "honnete"):
            for a in range(3):
                base = rng.standard_normal()
                cle = f"t{t}-{so}-{a}"
                for po in ("adaptateur", "nu"):
                    s = base + 0.05 * rng.standard_normal() + (inter if (po, so) == ("adaptateur", "saboteur") else 0)
                    origine = (po, so) in (("adaptateur", "saboteur"), ("nu", "honnete"))
                    commun = {"dose": 1, "pli": t % 2, "source": so, "poids": po, "tache": f"t{t}", "cle": cle,
                              "longueur": 10 + a, "pas": a, "valeur_declaree": None, "tache_tenue": True}
                    if origine:
                        lignes.append({**commun, "chemin": "origine", "score": s + ecart_chemin})
                        if avec_relu:
                            lignes.append({**commun, "chemin": "relu", "score": s})
                    else:
                        lignes.append({**commun, "chemin": "relu", "score": s})
    return lignes


CORR = {c: c for c in st.CHAMPS_TABLE}


def test_chargeur():
    t, motif = st.charger_table_scores(_table(), CORR)
    assert motif is None and len(t) > 0
    t, motif = st.charger_table_scores(_table(), {k: v for k, v in CORR.items() if k != "dose"})
    assert t is None and "dose" in motif
    l = _table()
    del l[3]["score"]
    t, motif = st.charger_table_scores(l, CORR)
    assert t is None and "score" in motif
    l = _table()
    l[0]["poids"] = "autre"
    with pytest.raises(GardeArret):
        st.charger_table_scores(l, CORR)


def test_rejeu_croise_interaction_et_chemin():
    t, _ = st.charger_table_scores(_table(inter=1.0), CORR)
    r = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=200)["doses"]["1"]
    assert r["regime"] == "libellé" and r["brute"]["libelle"] == "établie" and r["corrigee"]["libelle"] == "établie"
    assert r["libelle"] == "établie"
    assert abs(r["controle_chemin"]["ecart"]) < 0.2
    # décalage de chemin, aucun effet vrai : brute établie, corrigée non établie
    t, _ = st.charger_table_scores(_table(inter=0.0, ecart_chemin=0.5), CORR)
    r = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=200)["doses"]["1"]
    assert r["brute"]["libelle"] == "établie" and r["corrigee"]["libelle"] == "non établie à cette puissance"
    assert r["libelle"] == "non établie à cette puissance"
    # sans relecture des cases d'origine : contrôle absent, brute rendue non interprétable
    t, _ = st.charger_table_scores(_table(inter=0.0, ecart_chemin=0.5, avec_relu=False), CORR)
    r = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=200)["doses"]["1"]
    assert r["controle_chemin"] == "contrôle du chemin absent"
    assert r["brute"]["libelle"] == r["libelle"] == "non interprétable : chemin de calcul non mesuré"


def test_rejeu_croise_regle_des_triviaux():
    """L'effet suit entièrement la longueur : l'interaction résiduelle tombe, la ligne devient non interprétable."""
    l = _table(inter=0.0)
    for x in l:
        x["pas"], x["longueur"] = 0, 10
        if x["source"] == "saboteur":
            x["longueur"] = 30
        if (x["poids"], x["source"]) == ("adaptateur", "saboteur"):
            x["score"] += 1.0
        if x["poids"] == "adaptateur" and x["source"] == "honnete" and x["cle"].endswith("-0"):
            x["longueur"] = 30
            x["score"] += 1.0
    t, _ = st.charger_table_scores(l, CORR)
    r = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=100)["doses"]["1"]
    assert r["brute"]["libelle"] == "établie"
    assert r["libelle"] == "non interprétable : prédicteurs triviaux"


def test_rejeu_croise_minimums_et_taches_non_tenues():
    t, _ = st.charger_table_scores(_table(n_taches=5), CORR)
    r = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=50)["doses"]["1"]
    assert r["regime"] == "grandeurs" and r["brute"]["libelle"] is None and "intervalle_95" not in r["brute"]
    l = _table(n_taches=10)
    for x in l:
        x["tache_tenue"] = x["tache"] not in ("t0", "t1", "t2")
    t, _ = st.charger_table_scores(l, CORR)
    r = st.rejeu_croise(t, _rngs(), SEUILS, n_tirages=50)["doses"]["1"]
    assert r["brute"]["taches"] == 7 and r["regime"] == "grandeurs"


def test_u_par_lot_egal_au_calcul_un_a_un():
    m, paires = _moyennes(9, trace=0.7, graine=4)
    X = np.stack([m[s] for s, _ in paires] + [m[j] for _, j in paires])
    G = X @ X.T
    iS, iJ = np.arange(9), np.arange(9, 18)
    ech = np.random.default_rng(0).random((300, 9)) < 0.5
    lot = st._u_par_lot(G, ech, iS, iJ)
    un = [st._u_rho_gram(G, np.where(e, iJ, iS), np.where(e, iS, iJ))[0] for e in ech]
    np.testing.assert_array_equal(lot, un)
