"""Rapportés sans règle, v5 (texte scellé, section 13, « Rapportés sans règle »)."""
import json
import math

import numpy as np

from controle_ia.iib import rapportes_v5 as rp
from controle_ia.iib.jouet_v5 import etalonnage_numerique, ligne_numerique


def _par(graine=9, **kw):
    e = etalonnage_numerique(np.random.default_rng(graine), **kw)
    par = {}
    for l in e["lignes"]:
        par.setdefault((l["oracle"], l["phase"]), []).append(l)
    return par


def test_rapportes_d_un_groupe_complets_et_sans_texte():
    par = _par()
    r = rp.rapportes(par[("N", "etalonnage-regenere")])
    assert r["actions"] == 640 and r["episodes"] == 64 and set(r["par_position"]) == {str(i) for i in range(1, 11)}
    assert r["par_position"]["1"]["bornables"] == 0 and r["par_position"]["5"]["bornables"] == 64
    assert r["par_position"]["1"]["ecart_absolu_median_des_suites"] > 5 * r["par_position"]["5"]["ecart_absolu_median_des_suites"]
    assert r["couplage"]["reecrites"] == 576 and r["couplage"]["cas_a"] == 576 and sum(r["histogramme_des_rangs"].values()) == 640
    h = rp.rapportes(par[("P", "etalonnage-honnete")])
    assert abs(h["ancienne_statistique_mediane_des_exces"]) < 0.05 and h["couplage"]["reecrites"] == 0
    assert 0.8 < h["ancrage"]["jumeau_sur_agent_precedent"] < 1.0 and abs(h["ancrage"]["jumeau_sur_jumeau_precedent"]) < 0.15     # P : le jumeau suit l'agent
    assert h["discretion"]["part_au_dessus_de_toutes_ses_suites"] < 0.25
    reg = rp.rapportes(par[("P", "etalonnage-regenere")])
    assert reg["discretion"]["part_au_dessus_de_toutes_ses_suites"] > 0.5 and reg["discretion"]["suivants_moins_premier_cout_moyenne"] > h["discretion"]["suivants_moins_premier_cout_moyenne"]
    json.dumps(r, allow_nan=False)


def test_lecture_de_la_troisieme_donnee_sur_un_jeu_construit():
    """y = 0,5 x + bruit dont l'écart type croît avec |x| : la pente est retrouvée, l'écart type du tiers haut dépasse celui du bas."""
    rng = np.random.default_rng(0)
    n, p = [], []
    for e in range(40):
        for pas in range(2, 10):
            x = rng.normal(0, 0.5)
            y = 0.5 * x + rng.normal(0, 0.02 + 0.3 * abs(x))
            n.append(ligne_numerique("N", "etalonnage-honnete", f"e{e}", pas, 100.0, [100.0 * 10 ** y] * 8, False, 100.0 * 10 ** x, 100.0))
            p.append(ligne_numerique("P", "etalonnage-honnete", f"e{e}", pas, 100.0, [100.0] * 8, False, 100.0, 100.0))
    r = rp.lecture_de_la_troisieme_donnee(n, p, np.random.default_rng(1), tirages=300)
    assert r["actions"] == 320 and r["episodes"] == 40 and abs(r["pente"] - 0.5) < 0.1
    bas, _, haut = r["ecart_type_par_tiers"]
    assert haut > 2 * bas and r["difference_haut_moins_bas"] == haut - bas and r["intervalle_95"][0] > 0
    assert r["ecart_absolu_median_de_x_par_tiers"][0] < r["ecart_absolu_median_de_x_par_tiers"][2]
    assert rp.lecture_de_la_troisieme_donnee(n[:5], p[:5], np.random.default_rng(1)) is None
    assert math.isfinite(r["pente"]) and "pas dimensionnée" in r["reserve"]
