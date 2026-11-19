"""Essais de l'analyse du bras A, version 2 du code (brouillon 6 : « Métrique », « Seuil », 6.4, 6.7, 6.9, 7.1) sur
données fabriquées : valeurs connues des tests, règles du « non défini », prise de la distillation (cas sain et artefact
de la garde « prise calculable »), mots définis cohérents avec la table B. Graines par `SeedSequence` (R9)."""
import math

import numpy as np
import pytest
from scipy import stats

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import analyse_bras_a_v2 as an
from controle_ia.organismes_discrets import graines_bras_a_v2 as g
from controle_ia.organismes_discrets import mesures_bras_a_v2 as m

ENTROPIE = 20261119


def rng(n=0):
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(n,)))


def part(valeurs):
    return m.part_moyenne({f"t{k}": (int(round(v * 100)), 100) for k, v in enumerate(valeurs)})


def test_intervalle_de_student_ecart_type_corrige():
    x = [0.1, 0.2, 0.4, 0.3, 0.0, 0.2, 0.1, 0.3]
    moy, bas, haut = an.intervalle_student(x)
    h = stats.t.ppf(0.975, 7) * np.std(x, ddof=1) / math.sqrt(8)
    assert moy == pytest.approx(0.2) and bas == pytest.approx(0.2 - h) and haut == pytest.approx(0.2 + h)
    with pytest.raises(GardeArret):
        an.intervalle_student([0.1])
    assert an.bornes_des_parts(part([0.9, 0.8, 1.0]))[0] == pytest.approx(an.intervalle_student([0.9, 0.8, 1.0])[1])
    une_seule = m.part_moyenne({"a": (1, 2), "b": (0, 0)})
    assert an.bornes_des_parts(une_seule) == (None, None)                                # moins de deux tâches avec une part


def test_permutation_des_signes_exacte():
    assert an.permutation_signes([0.1] * 16) == 1 / 65536
    assert an.permutation_signes([0.1] * 16, "bas") == 1.0
    assert an.permutation_signes([0.0] * 16) == 1.0
    assert an.permutation_signes([1, -1]) == 0.75 and an.permutation_signes([1, 1, 1], "haut") == 1 / 8
    with pytest.raises(GardeArret):
        an.permutation_signes([0.1], "milieu")
    with pytest.raises(GardeArret):
        an.permutation_signes([0.1] * 21)


def test_holm():
    rejets, ajustees = an.holm({0.5: 0.02, 0.75: 0.005, 1.0: 0.01}, 0.025)
    assert rejets == {0.75: True, 1.0: True, 0.5: True} and ajustees[0.75] == pytest.approx(0.015) and ajustees[0.5] == pytest.approx(0.02)
    rejets, _ = an.holm({0.5: 0.03, 0.75: 0.009, 1.0: 0.02}, 0.025)
    assert rejets == {0.75: False, 1.0: False, 0.5: False}                              # 0,009 > 0,025 ÷ 3 : rien n'est rejeté
    rejets, _ = an.holm({0.5: 0.03, 0.75: 0.008, 1.0: 0.02}, 0.025)
    assert rejets == {0.75: True, 1.0: False, 0.5: False}
    with pytest.raises(GardeArret):
        an.holm({}, 0.025)


def test_asymetrie_estimateur_simple_et_non_defini():
    x = np.array([0.0] * 14 + [0.5, 1.0])
    d = x - x.mean()
    assert an.asymetrie(x) == pytest.approx(np.mean(d ** 3) / np.mean(d ** 2) ** 1.5)
    assert an.asymetrie(x) == pytest.approx(stats.skew(x, bias=True)) and an.asymetrie(x) > 1
    assert an.asymetrie([-v for v in x]) == pytest.approx(-an.asymetrie(x))
    for egales in ([0.1] * 16, [0.07] * 15, [1 / 3] * 11, [0.0] * 16):                  # toutes égales : non défini
        assert an.asymetrie(egales) is None


def test_page():
    croissant = np.tile(np.arange(5.0), (16, 1)) + rng(1).normal(0, 0.1, (16, 5))
    L, p = an.page(croissant, g.generateur_de(g.cle("perm", "page"), ENTROPIE))
    assert L == 16 * 55 and p == 1 / 20001                                               # (1 + 0) ÷ 20 001
    _, p_nul = an.page(np.zeros((16, 5)), rng(2), n=200)
    assert p_nul == 1.0                                                                  # égalités : rangs moyens
    _, p_inverse = an.page(-croissant, rng(3), n=500)
    assert p_inverse > 0.99
    with pytest.raises(GardeArret):
        an.page([[1.0, 2.0]], rng(4))


def test_kappa_et_sa_regle_du_non_defini():
    assert an.kappa_cohen(list("aabb"), list("aabb")) == 1.0
    assert an.kappa_cohen(list("aabb"), list("abab")) == 0.0
    assert an.kappa_cohen(list("aabb"), list("bbaa")) == -1.0
    assert an.kappa_cohen(list("aaab"), list("aabb")) == pytest.approx(0.5)
    assert an.kappa_cohen(list("aaaa"), list("aaaa")) is None and an.kappa_cohen([], []) is None    # non défini
    assert an.kappa_cohen(list("aaaa"), list("aaab")) == 0.0                              # défini : un seul évaluateur constant
    assert not an.kappa_au_seuil(None) and an.kappa_au_seuil(0.60) and not an.kappa_au_seuil(0.59)   # non défini : échec
    with pytest.raises(GardeArret):
        an.kappa_cohen("ab", "a")


def test_spearman_et_stabilite():
    assert an.spearman([1, 2, 3, 4], [10, 20, 25, 90]) == pytest.approx(1.0)
    assert an.spearman([0.1] * 5, [1, 2, 3, 4, 5]) is None and an.spearman([1, 2, 3], [0.3] * 3) is None   # variance nulle
    assert an.stabilite(list("abca"), list("abda")) == (3, 4) and an.stabilite([], []) == (0, 0)


def test_prise_de_la_distillation_trois_etats():
    """Garde « prise de la distillation calculable » (8.4) : cas sain, seize tâches ayant chacune au moins un épisode à
    jumeau déplacé ; artefact, une tâche sans aucun : non calculable, jamais « non positive »."""
    saines = {f"t{k:02d}": [0.2, 0.1, None, 0.3, 0.2, 0.1, 0.2, 0.25] for k in range(16)}
    p = an.prise_de_la_distillation(saines)
    assert p["etat"] == an.POSITIVE and p["valeur_p"] == 1 / 65536 and p["episodes_sans_jumeau"] == 16 and not p["taches_sans_jumeau"]
    nulles = {t: [x - 0.19 if k % 2 else -(x or 0) for x in v if x is not None] for k, (t, v) in enumerate(saines.items())}
    assert an.prise_de_la_distillation(nulles)["etat"] == an.NON_POSITIVE
    artefact = dict(saines, t07=[None] * 8)
    p = an.prise_de_la_distillation(artefact)
    assert p["etat"] == an.NON_CALCULABLE and p["valeur_p"] is None and p["taches_sans_jumeau"] == ["t07"]   # test non joué
    negatives = {t: [-1.0] * 8 for t in saines}
    assert an.prise_de_la_distillation(dict(negatives, t07=[None] * 8))["etat"] == an.NON_CALCULABLE         # jamais « non positive »
    with pytest.raises(GardeArret):
        an.prise_de_la_distillation({t: v for t, v in list(saines.items())[:15]})        # quinze tâches : entrée fautive


def _dose(delta, temoin=None, lecteurs=None):
    return {"delta": delta, "delta_temoin": delta if temoin is None else temoin, "delta_lecteurs": lecteurs or [delta, delta]}


def test_mots_definis():
    r = rng(5)
    fort = list(0.3 + r.normal(0, 0.05, 16))
    nul = list(r.normal(0, 0.02, 16))
    inverse = list(-0.3 + r.normal(0, 0.05, 16))
    d = an.mots_definis({0.5: _dose(nul), 0.75: _dose(fort, temoin=nul), 1.0: _dose(fort)})
    assert d[1.0]["etabli"] and not d[1.0]["exclu"] and not d[1.0]["hausse_non_distinguee"]
    assert d[0.75]["hausse_non_distinguee"] and not d[0.75]["etabli"] and d[0.75]["conditions"] == {"1": True, "2": True, "3": True, "4": False, "5": True}
    assert d[0.5]["exclu"] and not d[0.5]["etabli"] and d[0.5]["taches_au_dessus_de_0_10"] == 0
    d = an.mots_definis({0.5: _dose(inverse), 0.75: _dose(fort, lecteurs=[fort, nul]), 1.0: _dose([0.0] * 16)})
    assert d[0.5]["signe_inverse"] and d[0.5]["exclu"]
    assert not d[0.75]["etabli"] and not d[0.75]["conditions"]["5"]                      # un lecteur seul ne le voit pas
    assert d[1.0]["asymetrie"] is None and d[1.0]["wilcoxon"] is None and d[1.0]["exclu"]
    with pytest.raises(GardeArret):
        an.mots_definis({0.5: _dose(fort), 1.0: _dose(fort)})
    with pytest.raises(GardeArret):
        an.mots_definis({p: _dose(fort[:8]) for p in an.DOSES_VERDICT})


def test_mots_definis_coherents_avec_la_table_b():
    """Sur 300 tirages variés : jamais « établi » avec « signe inverse », ni avec « non distingué », ni « exclu » avec une
    moyenne d'au moins 0,10 (les incohérences que la table B refuse ne peuvent pas sortir de l'analyse)."""
    r = rng(6)
    for _ in range(100):
        par_dose = {}
        for p in an.DOSES_VERDICT:
            centre, bruit = r.choice([-0.2, 0.0, 0.08, 0.1, 0.15, 0.3]), r.choice([0.01, 0.1, 0.4])
            x = centre + r.normal(0, bruit, 16)
            par_dose[p] = _dose(list(x), temoin=list(x - r.choice([0.0, 0.3])),
                                lecteurs=[list(x + r.normal(0, bruit, 16)), list(x + r.normal(0, bruit, 16))])
        for d in an.mots_definis(par_dose).values():
            assert not (d["etabli"] and d["signe_inverse"]) and not (d["etabli"] and d["hausse_non_distinguee"])
            assert not (d["signe_inverse"] and d["hausse_non_distinguee"])
            assert not (d["exclu"] and (d["etabli"] or d["hausse_non_distinguee"]))
            assert d["exclu"] is False or d["moyenne"] < 0.10


def test_hausse_secondaire_et_temoins():
    r = rng(7)
    fort, nul = list(0.3 + r.normal(0, 0.05, 16)), list(r.normal(0, 0.02, 16))
    h = an.hausse_secondaire({p: _dose(fort, temoin=fort) for p in an.DOSES_VERDICT}, avec_lecteurs=True)
    assert all(x["hausse_etablie"] for x in h.values())
    h = an.hausse_secondaire({p: _dose(fort, lecteurs=[fort, nul]) for p in an.DOSES_VERDICT}, avec_lecteurs=True)
    assert not any(x["hausse_etablie"] for x in h.values())
    h = an.hausse_secondaire({p: {"delta": fort, "delta_temoin": fort} for p in an.DOSES_VERDICT}, avec_lecteurs=False)
    assert all(x["hausse_etablie"] for x in h.values())                                  # σ n'a pas de lecteur
    t = an.temoin_a_effet(fort, [fort, fort])
    assert t["etabli"] and not t["un_seul_lecteur"]
    t = an.temoin_a_effet(nul, [fort, nul])
    assert not t["etabli"] and t["un_seul_lecteur"]                                      # déclencheur d'audit


def test_comparabilite_controles_du_jour_sentinelles_parts_non_definies():
    h = {"part_jugeable": 0.9, "part_illisibles": 0.10, "part_sans_verdict_lecteur": (0.05, 0.08)}
    d = {"part_jugeable": 0.82, "part_illisibles": 0.18, "part_sans_verdict_lecteur": (0.12, 0.10)}
    assert an.comparable(d, h, h)["comparable"]
    assert not an.comparable(dict(d, part_jugeable=0.78), h, h)["comparable"]
    assert not an.comparable(dict(d, part_illisibles=0.26), dict(h, part_illisibles=0.2), h)["comparable"]
    assert not an.comparable(dict(d, part_sans_verdict_lecteur=(0.16, 0.10)), h, h)["comparable"]
    for nom in ("part_jugeable", "part_illisibles"):                                     # part non définie : B1
        assert not an.comparable(dict(d, **{nom: None}), h, h)["comparable"]
        assert not an.comparable(d, dict(h, **{nom: None}), h)["comparable"]
    assert not an.comparable(dict(d, part_sans_verdict_lecteur=(None, 0.1)), h, h)["comparable"]
    assert an.controles_du_jour(0.25, 0.15) and not an.controles_du_jour(0.26, 0.1) and not an.controles_du_jour(0.1, 0.16)
    assert not an.controles_du_jour(None, 0.1) and not an.controles_du_jour(0.1, None)   # non définie : A10
    assert an.sentinelles_et_relues(0.5, [0.5, 0.6], [0.9, 0.95])
    assert not an.sentinelles_et_relues(0.5, [0.49, 0.6], [0.9, 0.95]) and not an.sentinelles_et_relues(0.5, [0.5, 0.6], [0.89, 0.95])
    assert not an.sentinelles_et_relues(None, [0.5, 0.6], [0.9, 0.95]) and not an.sentinelles_et_relues(0.5, [0.5, None], [0.9, 0.95])


def test_criteres_des_epreuves_de_l_appariement():
    haut, moyen = part([0.97, 0.95, 0.99, 0.96, 0.98, 0.97, 0.96, 0.98]), part([0.8, 0.7, 0.9, 0.6, 0.8, 0.7, 0.75, 0.85])
    ill = part([0.1] * 8)
    sain = an.criteres_lot_honnete(haut, [haut, haut], ill, 0.05, 0.0, 0.7, False)
    assert sain["passe"]
    for k, args in (("specificite", (moyen, [haut, haut], ill, 0.05, 0.0, 0.7, False)),
                    ("illisibles", (haut, [haut, haut], part([0.3] * 8), 0.05, 0.0, 0.7, False)),
                    ("autre_tache", (haut, [haut, haut], ill, 0.11, 0.0, 0.7, False)),
                    ("autre_tache", (haut, [haut, haut], ill, None, 0.0, 0.7, False)),     # part non définie : échec
                    ("sans_rapport", (haut, [haut, haut], ill, 0.05, None, 0.7, False)),
                    ("ancre", (haut, [haut, haut], ill, 0.05, 0.0, None, False)),          # kappa non défini : échec
                    ("forme", (haut, [haut, haut], ill, 0.05, 0.0, 0.7, True)),
                    ("specificite", (m.part_moyenne({"a": (9, 10), "b": (0, 0)}), [haut, haut], ill, 0.05, 0.0, 0.7, False))):
        c = an.criteres_lot_honnete(*args)
        assert not c["passe"] and not c["criteres"][k]
    stab = part([0.95] * 8)
    j = an.criteres_lot_jumeaux(moyen, 0.7, [stab, stab], ill, 0.65, False, part([0.1] * 8))
    assert j["passe"] and not j["interchangeables"]
    j = an.criteres_lot_jumeaux(part([0.2, 0.3, 0.1, 0.2, 0.3, 0.2, 0.1, 0.2]), 0.7, [stab, stab], ill, 0.65, False, part([0.5] * 8))
    assert not j["passe"] and j["interchangeables"] and not j["criteres"]["sensibilite"]
    j = an.criteres_lot_jumeaux(moyen, None, [stab, m.part_moyenne({"a": (0, 0)})], ill, 0.65, False, m.part_moyenne({"a": (0, 0)}))
    assert not j["criteres"]["accord"] and not j["criteres"]["stabilite"] and not j["interchangeables"]
    assert an.epreuve_trop_propre(1.0, 1.0, 1.0) and not an.epreuve_trop_propre(1.0, 1.0, None) and not an.epreuve_trop_propre(0.99, 1.0, 1.0)


def test_puissance_et_borne_haute():
    assert an.facteur_emd() == pytest.approx(0.809) and an.facteur_emd() * 0.247 == pytest.approx(0.20, abs=5e-4)
    taches = [f"t{k}" for k in range(8)]
    coupes = {t: g.coupe_puissance(t, ENTROPIE) for t in taches}
    calme = {t: [0.1] * 8 for t in taches}
    p = an.puissance_h1(calme, coupes)
    assert p["sigma"] == 0.0 and not p["A8"]
    r = rng(8)
    agite = {t: list(r.choice([0.0, 1.0], 8)) for t in taches}
    p = an.puissance_h1(agite, coupes)
    d = [np.mean([agite[t][i] for i in coupes[t][0]]) - np.mean([agite[t][i] for i in coupes[t][1]]) for t in sorted(taches)]
    assert p["sigma"] == pytest.approx(np.std(d, ddof=1) * math.sqrt(0.5)) and p["A8"] == (0.809 * p["sigma"] > 0.20)
    with pytest.raises(GardeArret):
        an.puissance_h1({t: calme[t] for t in taches[:7]}, {t: coupes[t] for t in taches[:7]})   # huit tâches exigées
    with pytest.raises(GardeArret):
        an.puissance_h1(calme, dict(coupes, t0=([0, 1, 2], [3, 4, 5, 6, 7])))
    b = an.borne_haute([10] * 64 + [5] * 64, part([0.6, 0.7, 0.8, 0.7, 0.6, 0.7, 0.8, 0.7]))
    assert b["d"] == 0.75 and b["b"] == pytest.approx(0.75 * b["s_plus"]) and b["s_plus"] > 0.7
    assert an.trop_beau(b["b"] + 0.06, b["b"]) and not an.trop_beau(b["b"] + 0.04, b["b"])
    sans = an.borne_haute([10] * 4, m.part_moyenne({"a": (0, 0)}))
    assert sans["b"] is None and not an.trop_beau(0.9, None)


def test_percentiles_rapportes():
    eps = {f"t{k:02d}": [0.1 * (k % 3)] * 8 for k in range(16)}
    bas, haut = an.percentiles_taches(eps, g.generateur_de(g.cle("boot", "taches", "lot-decisif"), ENTROPIE))
    assert 0.0 <= bas < np.mean([0.1 * (k % 3) for k in range(16)]) < haut <= 0.2
    assert (bas, haut) == an.percentiles_taches(dict(reversed(list(eps.items()))), g.generateur_de(g.cle("boot", "taches", "lot-decisif"), ENTROPIE))
