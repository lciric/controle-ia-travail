"""Essais de `audit_apres_coup_v2.estimateurs` (rang 5) : biais nul et variance fermée de T̂ ; couverture de la
strate du plancher ; compte naïf sur audit orienté refusé ; courbe sécurité-utilité du cas sain."""
import math

import numpy as np
import pytest
from scipy import stats

from controle_ia.audit_apres_coup_v2.attaque_choisie import TYPES_ILLUSTRATION
from controle_ia.audit_apres_coup_v2.estimateurs import (STRATE_PLANCHER_SEUL, budget_realise, clopper_pearson,
                                                       estimateur_pondere, pi_par_type, recapture,
                                                       securite_au_pire_type, strate_plancher,
                                                       variance_ponderee_theorique)
from controle_ia.audit_apres_coup_v2.graines import generateur_auxiliaire
from controle_ia.audit_apres_coup_v2.oracle_simule import OracleSimule
from controle_ia.audit_apres_coup_v2.regle_audit import CONFIG_SANS_PLANCHER, RegleAudit, g_identite
from controle_ia.audit_apres_coup_v2.simulateur import Monde, politique_constante, simuler
from controle_ia.gardes import GardeArret

E = 20261122


def _monde():
    return Monde(10, E, TYPES_ILLUSTRATION, 1.6, politique_constante(0.05), 0.0)


def test_biais_nul_et_variance_fermee_de_T_chapeau():
    """Monde fixé (enjeux, dommages, scores) ; seules la pièce et l'oracle sont retirés : E(T̂) = q·T et
    Var(T̂) = Σ d_i·s_i²·q·(1/π_i − q)."""
    m, q = _monde(), 0.8
    r = RegleAudit(0.01, 0.015, 0.1, g_identite, 1.6)
    o = OracleSimule(q, 0.0, 0, "signature")
    R, N = 1500, 2000
    base = simuler(m, r, o, 0, N, chaine=False)
    d, s, pi = base.verite.dommage, base.journal.colonne("enjeu"), base.journal.colonne("pi")
    T = float(np.sum(d * s))
    vals = []
    for k in range(R):
        g = generateur_auxiliaire(E, "essais", 50, k)

        def t(u, g=g):
            u["piece"] = g.random(N)
            u["oracle"] = g.random(N)
            return u

        res = simuler(m, r, o, 0, N, transformer_uniformes=t, chaine=False)
        vals.append(estimateur_pondere(res.journal))
    vals = np.array(vals)
    V = variance_ponderee_theorique(d, s, pi, q)
    assert abs(vals.mean() - q * T) <= 4 * math.sqrt(V / R)
    # variance empirique contre la formule, à 4 erreurs types : erreur type relative √((κ − 1)/R), κ la kurtosis
    # empirique de T̂
    c = vals - vals.mean()
    kappa = float(np.mean(c ** 4) / np.mean(c ** 2) ** 2)
    assert abs(vals.var(ddof=1) / V - 1) <= 4 * math.sqrt((kappa - 1) / R)


def test_couverture_de_la_strate_du_plancher():
    m = _monde()
    r = RegleAudit(0.05, 0.015, 0.1, g_identite, 1.6)
    o = OracleSimule(1.0, 0.0, 0, "signature")
    R = 300
    couvert = 0
    for t in range(R):
        res = simuler(m, r, o, t, 4000, chaine=False)
        bas, haut = strate_plancher(res.journal, r)["intervalle"]
        couvert += bas <= 0.05 <= haut
    assert couvert >= int(stats.binom.ppf(0.001, R, 0.95))


def test_strate_refusee_sans_plancher():
    r = RegleAudit(0.0, 0.0, 0.1, g_identite, 1.6, configuration=CONFIG_SANS_PLANCHER)
    res = simuler(_monde(), r, OracleSimule(1.0, 0.0, 0, "signature"), 0, 1000)
    with pytest.raises(GardeArret, match="pas de borne"):
        strate_plancher(res.journal, r)


def test_artefact_compte_naif_sur_audit_oriente_refuse():
    m = Monde(11, E, ((1.0, 1.0),), 1.0, politique_constante(1.0), 0.0, loi_score=("signal", 0.2, 0.0))
    o = OracleSimule(1.0, 0.0, 0, "signature")
    oriente = RegleAudit(0.05, 0.0, 0.45, g_identite, 1.0)
    res = simuler(m, oriente, o, 0, 20_000, chaine=False)
    sig = res.journal.colonne("score") == 1
    with pytest.raises(GardeArret, match="naïf"):
        recapture(res.journal, sig, "naif")
    with pytest.raises(GardeArret, match="configuration"):
        recapture(res.journal, sig, "strate_sans_score")  # choix de strate non écrit : refus, aucun défaut
    assert abs(recapture(res.journal, sig, "strate_sans_score", STRATE_PLANCHER_SEUL) - 0.2) < 0.05
    # cas sain : tirage sans égard au score, le compte naïf est admis et vaut le vrai
    uniforme = RegleAudit(0.2, 0.0, 0.0, g_identite, 1.0)
    res2 = simuler(m, uniforme, o, 1, 20_000, chaine=False)
    sig2 = res2.journal.colonne("score") == 1
    n_aud = int(res2.journal.colonne("audite").sum())
    assert abs(recapture(res2.journal, sig2, "naif") - 0.2) <= 4 * math.sqrt(0.16 / n_aud)


def test_budget_realise_en_trois_parts():
    r = RegleAudit(0.01, 0.015, 0.1, g_identite, 1.6)
    res = simuler(_monde(), r, OracleSimule(1.0, 0.0, 0, "signature"), 0, 20_000, chaine=False)
    b = budget_realise(res.journal)
    assert b["pi_min"] == 0.01
    assert abs(b["part_enjeu"] - 0.015) < 0.002
    assert b["reste"] > 0 and b["part_ecretee"] == 0.0


def test_courbe_securite_cas_sain():
    """Enjeux 1, 5, 25 ; θ = 100 ; q = 1 ; L = 0 ; budget 0,02 (section 1, cas sain)."""
    T = TYPES_ILLUSTRATION
    uni = securite_au_pire_type([0.02] * 3, T, 1.0, 100, 0)
    assert uni["securite_par_type"][2] == pytest.approx(1 - 0.98 ** 4, abs=1e-12)
    assert round(uni["securite_par_type"][2], 3) == 0.078
    prop = securite_au_pire_type([0.02 * s / 1.6 for _, s in T], T, 1.0, 100, 0)
    assert [round(x, 3) for x in prop["securite_par_type"]] == [0.716, 0.725, 0.777]
    assert prop["pire_type"] == 1.0 and round(prop["securite"], 3) == 0.716
    r = RegleAudit(0.02, 0.0, 0.0, g_identite, 1.6)
    assert pi_par_type(r, T) == [0.02, 0.02, 0.02]


def test_clopper_pearson_refus_et_bornes():
    assert clopper_pearson(0, 10)[0] == 0.0 and clopper_pearson(10, 10)[1] == 1.0
    with pytest.raises(GardeArret):
        clopper_pearson(5, 3)
