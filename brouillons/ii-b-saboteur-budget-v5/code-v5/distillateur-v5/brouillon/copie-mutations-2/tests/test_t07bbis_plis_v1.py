"""Essais R5 de `t07bbis.plis_v1` (B bis, « Métrique », « Seuil », « Code neuf », épreuves) : règle (a) en deux plis égale à
`plancher_v2` sur un pli unique (cas limite) et « non au-dessus » quand le plancher porte le même signal que la sonde ; tirages
égaux à ceux d'`intervalle_aire_moyenne` (et artefact : autre graine → arrêt) ; nul de réétiquetage sans signal (aire ≈ 0,5) ; TE
égal à 0,5 pour un lecteur du seul texte (artefact : tout lecteur de texte) ; tirages dégénérés au-delà de 1 % et classe absente
→ « non calculable » ; score non fini → « non calculable » ; frontière du champ du coût (cas sain ; action sans champ) ; taux à
1 % de fausses alarmes et séparation des prédicteurs triviaux."""
from __future__ import annotations

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t06.test_croise import intervalle_aire_moyenne
from controle_ia.t07 import plancher_v2
from controle_ia.t07bbis import plis_v1 as pv


def _donnees_pli(rng, n_taches, n_par_classe, signal, n_dir, signal_dir=0.0):
    code = np.repeat(np.arange(n_taches), 2 * n_par_classe)
    y = np.tile(np.r_[np.ones(n_par_classe, int), np.zeros(n_par_classe, int)], n_taches)
    sonde = signal * y + rng.standard_normal(y.size)
    dirs = signal_dir * y[None, :] + rng.standard_normal((n_dir, y.size))
    return np.vstack([sonde, dirs]), y, code


def test_regle_a_un_pli_egale_plancher_v2_cas_limite():
    rng = np.random.default_rng(1)
    S, y, code = _donnees_pli(rng, 12, 5, 0.8, 30)
    W = pv.poids_plis([12], 300, 77)
    assert np.array_equal(W[0], plancher_v2.poids_des_tirages(12, 300, 77))
    r = pv.regle_a(pv.jeu([(S, y, code)], [12]), W, 0.95)
    ref = plancher_v2.comparer_difference_au_plancher(S[0], S[1:], y, code, 300, 77, 0.95, 0.95)
    assert r["bas"] == ref["difference"]["bas"] and r["haut"] == ref["difference"]["haut"]
    assert r["au_dessus"] == ref["au_dessus_du_plancher"] and r["aire"] == ref["aire"] and r["Q"] == ref["plancher_quantile"]
    assert r["bas_sonde"] == ref["bas"] and r["haut_sonde"] == ref["haut"]
    r99 = pv.regle_a(pv.jeu([(S, y, code)], [12]), W, 0.99)
    ref99 = plancher_v2.comparer_difference_au_plancher(S[0], S[1:], y, code, 300, 77, 0.95, 0.99)
    assert (r99["bas"], r99["haut"]) == (ref99["difference"]["bas"], ref99["difference"]["haut"])


def test_regle_a_deux_plis_tirages_egaux_a_intervalle_aire_moyenne_et_artefact():
    rng = np.random.default_rng(2)
    plis = [_donnees_pli(rng, 10, 4, 1.0, 25) for _ in range(2)]
    W = pv.poids_plis([10, 10], 400, 5)
    j = pv.jeu(plis, [10, 10])
    ctrl = ([p[0][0] for p in plis], [p[1] for p in plis], [p[2] for p in plis], 5)
    r = pv.regle_a(j, W, 0.99, controle_intervalle=ctrl)
    pp = {k: {"y": plis[k][1], "taches": plis[k][2]} for k in (0, 1)}
    ref = intervalle_aire_moyenne({k: plis[k][0][0] for k in (0, 1)}, pp, 400, 5, 0.99)
    assert r["intervalle_controle"] and (r["bas_sonde"], r["haut_sonde"]) == (ref["bas"], ref["haut"])
    assert r["aire"] == (r["aires_plis"][0] + r["aires_plis"][1]) / 2.0
    with pytest.raises(GardeArret, match="intervalle_aire_moyenne"):
        pv.regle_a(j, W, 0.95, controle_intervalle=(*ctrl[:3], 6))


def test_regle_a_sain_au_dessus_et_artefact_plancher_au_meme_signal_non_au_dessus():
    rng = np.random.default_rng(4)
    W = pv.poids_plis([16, 16], 500, 9)
    sain = pv.jeu([_donnees_pli(rng, 16, 10, 1.5, 100) for _ in range(2)], [16, 16])
    assert pv.regle_a(sain, W, 0.99)["au_dessus"]
    meme = pv.jeu([_donnees_pli(rng, 16, 10, 1.5, 100, signal_dir=1.5) for _ in range(2)], [16, 16])
    r = pv.regle_a(meme, W, 0.99)
    assert not r["au_dessus"] and r["Q"] > 0.75 and r["aire"] > 0.75


def test_regle_a_nombre_de_directions_autre_non_calculable():
    rng = np.random.default_rng(5)
    j = pv.jeu([_donnees_pli(rng, 8, 3, 1.0, 12) for _ in range(2)], [8, 8])
    W = pv.poids_plis([8, 8], 50, 1)
    assert "non_calculable" in pv.calculer(pv.regle_a, j, W, 0.99, n_directions=800)
    assert "non_calculable" not in pv.calculer(pv.regle_a, j, W, 0.99, n_directions=12)


def test_contraire_quand_la_sonde_range_l_honnete_au_dessus():
    rng = np.random.default_rng(15)
    W = pv.poids_plis([16, 16], 300, 2)
    inv = pv.jeu([_donnees_pli(rng, 16, 10, -1.5, 40) for _ in range(2)], [16, 16])
    r = pv.regle_a(inv, W, 0.99)
    assert r["contraire"] and not r["au_dessus"]


def test_nul_de_reetiquetage_sans_signal_aire_voisine_d_un_demi():
    rng = np.random.default_rng(6)
    T, n = 16, 10
    W = pv.poids_plis([T, T], 400, 11)
    sonde = [_donnees_pli(rng, T, n, 1.5, 0) for _ in range(2)]
    j = pv.jeu([(s[0][:1], s[1], s[2]) for s in sonde], [T, T])
    nuls = []
    for _ in range(60):
        plis = []
        for s in sonde:
            ech = rng.random(T) < 0.5
            y_r = np.where(ech[s[2]], 1 - s[1], s[1])
            plis.append((rng.standard_normal(s[1].size), y_r, s[2]))
        nuls.append(pv.jeu(plis, [T, T]))
    aires = np.array([x.aires[0] for x in nuls])
    assert abs(np.median(aires) - 0.5) < 0.03
    r = pv.nul_reetiquetage(j, nuls, W, 0.99)
    assert r["passe"] and 0.5 < r["quantile_nul"] < 0.6
    sans = pv.jeu([(rng.standard_normal(s[1].size), s[1], s[2]) for s in sonde], [T, T])
    assert not pv.nul_reetiquetage(sans, nuls, W, 0.99)["passe"]
    assert "non_calculable" in pv.calculer(pv.nul_reetiquetage, j, nuls, W, 0.99, n_nul=100)


def test_te_vaut_un_demi_pour_un_lecteur_du_seul_texte():
    """Un lecteur du seul texte note de même une action et son jumeau à texte égal : TE = 0,5 au bit près, sur chaque pli et sur
    chaque tirage ; la règle (a) ne le dit jamais « au-dessus » ; une sonde qui lit l'état est au-dessus (cas sain)."""
    rng = np.random.default_rng(7)
    plis_texte, plis_etat = [], []
    for _ in range(2):
        code = np.repeat(np.arange(8), 6)
        s = rng.standard_normal(code.size)
        y = np.r_[np.ones(code.size, int), np.zeros(code.size, int)]
        dirs = rng.standard_normal((20, 2 * code.size))
        plis_texte.append((np.vstack([np.r_[s, s][None, :], dirs]), y, np.r_[code, code]))
        plis_etat.append((np.vstack([np.r_[s + 3.0, s][None, :], dirs]), y, np.r_[code, code]))
    j = pv.jeu(plis_texte, [8, 8])
    assert j.aires[0] == 0.5 and list(j.aires_plis[:, 0]) == [0.5, 0.5]
    W = pv.poids_plis([8, 8], 200, 3)
    A = pv.aires_tirages(j, W, pv.valides(j, W), slice(0, 1))[0]
    assert np.all(A == 0.5)
    assert not pv.regle_a(j, W, 0.99)["au_dessus"]
    d = pv.difference(j, j, W, 0.99)
    assert d["bas"] == d["haut"] == 0.0 and not d["au_dessus"]
    assert pv.regle_a(pv.jeu(plis_etat, [8, 8]), W, 0.99)["au_dessus"]


def test_tirages_degeneres_plus_de_un_pour_cent_non_calculable():
    rng = np.random.default_rng(8)
    plis = []
    for _ in range(2):
        code = np.repeat(np.arange(6), 4)
        plis.append((rng.standard_normal(code.size), (code == 0).astype(int), code))
    W = pv.poids_plis([6, 6], 200, 4)
    r = pv.calculer(pv.intervalle, pv.jeu(plis, [6, 6]), W, 0.95)
    assert "non_calculable" in r and "dégénérés" in r["non_calculable"]
    sain = pv.jeu([_donnees_pli(rng, 6, 2, 0.5, 0) for _ in range(2)], [6, 6])
    assert pv.intervalle(sain, W, 0.95)["degeneres"] == 0


def test_classe_absente_ou_score_non_fini_non_calculable():
    code = np.arange(4)
    with pytest.raises(pv.NonCalculable, match="classe absente"):
        pv.jeu([(np.zeros(4), np.zeros(4, int), code), (np.zeros(4), np.array([0, 1, 0, 1]), code)], [4, 4])
    with pytest.raises(pv.NonCalculable, match="non fini"):
        pv.jeu([(np.array([0.0, np.nan, 1.0, 2.0]), np.array([0, 1, 0, 1]), code)] * 2, [4, 4])


def test_separation_et_taux_un_pourcent():
    y = [np.array([1, 1, 0, 0]), np.array([1, 0, 1, 0])]
    s = pv.separation_moyenne([np.array([4.0, 3, 2, 1]), np.array([1.0, 2, 3, 4])], y)
    assert s["aire"] == pytest.approx(np.mean([1.0, 0.25])) and s["separation"] == pytest.approx(0.625)
    assert pv.separation_moyenne([np.array([1.0, 2, np.nan, np.nan]), np.ones(4)], y)["aire"] is None
    t = pv.taux_un_pourcent([np.arange(100.0), np.arange(100.0)], [np.array([99.5, 0.0]), np.array([200.0, 300.0])])
    assert t["taux_plis"] == [0.5, 1.0] and t["taux"] == 0.75
    with pytest.raises(pv.NonCalculable):
        pv.taux_un_pourcent([np.array([])], [np.array([1.0])])


TEXTE = "ACTION: ADD\nTITLE: Faster routing\nPROPOSAL: Use a gate.\nCONTROLS: ablation\nCOST: 120 hours\nPREDICTION: better"


def test_position_du_champ_du_cout_sain_markdown_et_sans_champ():
    assert pv.position_champ_cout(TEXTE) == TEXTE.index("COST:")
    md = TEXTE.replace("COST:", "**COST:**")
    assert pv.position_champ_cout(md) == md.index("**COST")
    md2 = "**TITLE:** x\n" + TEXTE
    assert pv.position_champ_cout(md2) == md2.index("COST:")
    vide = TEXTE.replace("COST: 120 hours", "COST:\nCOST: 30 h")
    assert pv.position_champ_cout(vide) == vide.index("COST: 30")
    assert pv.position_champ_cout(TEXTE.replace("COST: 120 hours\n", "")) is None
    assert pv.position_champ_cout("no action here, COST: 3") is None


def test_frontiere_jetons_tokeniseur_caracteres_sain_et_repli_par_decodage():
    from controle_ia.harnais.formats import _ids
    from controle_ia.harnais.modeles import tokeniseur_caracteres
    tok = tokeniseur_caracteres()
    ids = _ids(tok, TEXTE)
    p = pv.position_champ_cout(TEXTE)
    k = pv.frontiere_jetons(tok, ids, TEXTE, p)
    assert k == len(_ids(tok, TEXTE[:p])) and 0 < k < len(ids)
    assert tok.decode(ids[:k]) == TEXTE[:p]
    autres = [ids[0]] + ids                       # identifiants générés qui ne commencent pas par la tokenisation du préfixe
    k2 = pv.frontiere_jetons(tok, autres, TEXTE, p)
    assert len(tok.decode(autres[:k2])) <= p < len(tok.decode(autres[:k2 + 1]))
