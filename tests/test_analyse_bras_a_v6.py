"""Essais de l'analyse du bras A, version 6 du code (brouillon 24 : conventions, « Métrique », « Seuil », 6.4, 6.7,
6.9, 7.1, 7.6, 8.4) sur données fabriquées dans l'essai. Statistique de la variable principale : essais de la version 5,
repris tels quels. **Règle de discrétion sur une pièce scellée et une configuration scellée** : table des formes (cas A
à E, ordre de reconnaissance, deux sortes d'écart), les cinq choix nommés (un essai par valeur du seuil, de
l'intervalle impossible et du moniteur non ajustable), réglages rendus, listes fermées, valeur de la famille à
l'égalité exacte, événement d'arrêt (ses cinq éléments, aucune valeur de la livraison, étape déduite de la pièce),
arrêt consigné, livraison refaite sur une ligne de GO, garde de sortie qui relit la pièce. Fichier de l'étape (m) et
ses constats ; fichier des rangs (étape (n)) ; aire conditionnelle contre une seconde écriture. **Les essais d'attaque
de la contre-lecture du code de la version 5** (`docs/notes/relance-organismes-discrets-v1/contre-lecture-code-v5-pieces/`)
sont repris : chaque cas y est nommé. Graines par `SeedSequence` (R9). Aucun module du côté habilité n'est importé."""
import copy
import hashlib
import itertools
import json
import math
import pickle
import re
from pathlib import Path

import numpy as np
import pytest
from scipy import stats

import aide_bras_a_v6 as h
from aide_bras_a_v6 import N, Q
from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import analyse_bras_a_v6 as an
from controle_ia.organismes_discrets import arrets_bras_a_v6 as ar
from controle_ia.organismes_discrets import configuration_bras_a_v6 as cf
from controle_ia.organismes_discrets import graines_bras_a_v6 as g
from controle_ia.organismes_discrets import mesures_bras_a_v6 as m
from controle_ia.organismes_discrets import permutation_etiquettes_bras_a_v6 as pe
from controle_ia.organismes_discrets import verdicts_bras_a_v6 as v
from controle_ia.scellement import sceller

ENTROPIE = 20261119


def rng(n=0):
    """Générateur des **données fabriquées** de l'essai (jamais d'un tirage de l'analyse, qui exige une clé de 6.2)."""
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(n,)))


def tirage(n=0):
    """Tirage à clé d'un intervalle seulement rapporté (clé `boot/taches/lot-decisif`)."""
    return g.tirage_de(g.cle("boot", "taches", "lot-decisif"), ENTROPIE + n)


def tirage_page(n=0):
    return g.tirage_de(g.cle("perm", "page"), ENTROPIE + n)


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
    L, p = an.page(croissant, g.tirage_de(g.cle("perm", "page"), ENTROPIE))
    assert L == 16 * 55 and p == 1 / 20001                                               # (1 + 0) ÷ 20 001
    _, p_nul = an.page(np.zeros((16, 5)), tirage_page(2), n=200)
    assert p_nul == 1.0                                                                  # égalités : rangs moyens
    _, p_inverse = an.page(-croissant, tirage_page(3), n=500)
    assert p_inverse > 0.99
    with pytest.raises(GardeArret):
        an.page([[1.0, 2.0]], tirage_page(4))


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
    cle = g.cle("boot", "taches", "lot-decisif")
    r = an.percentiles_taches(eps, g.tirage_de(cle, ENTROPIE))
    bas, haut = r["percentiles"]
    assert r["etat"] == an.CALCULE and r["tirages_degeneres"] == 0 and r["tirages"] == 2000
    assert 0.0 <= bas < np.mean([0.1 * (k % 3) for k in range(16)]) < haut <= 0.2
    assert r == an.percentiles_taches(dict(reversed(list(eps.items()))), g.tirage_de(cle, ENTROPIE))


def test_intervalle_seulement_rapporte_non_calculable_sans_arret():
    """Garde de 8.4, « intervalle seulement rapporté » : cas sain — percentiles calculables : rapportés ; artefact —
    plus de 1 % de tirages dégénérés : rapporté « non calculable », aucun arrêt ; et ce n'est plus un événement de la
    ligne A17 (aucun verdict changé)."""
    valeurs = {f"t{k:02d}": 0.1 * (k % 4) for k in range(16)}
    sain = an.intervalle_rapporte(valeurs, tirage(1))
    assert sain["etat"] == an.CALCULE and sain["percentiles"][0] < sain["percentiles"][1]
    une_seule = {t: (x if t == "t03" else None) for t, x in valeurs.items()}        # 15 tâches sur 16 sans valeur
    r = an.intervalle_rapporte(une_seule, tirage(1))                                    # (15/16)^16 ≈ 36 % de tirages dégénérés
    assert r["etat"] == an.NON_CALCULABLE and r["percentiles"] is None and 600 < r["tirages_degeneres"] < 850
    assert r["taches_sans_valeur"] == 15
    presque = {t: (None if t == "t03" else x) for t, x in valeurs.items()}           # une tâche sans valeur : aucun tirage perdu
    assert an.intervalle_rapporte(presque, tirage(1))["etat"] == an.CALCULE
    # « plus de 1 % » : strictement ; sur 2 000 tirages, 20 dégénérés passent, 21 non
    assert not an._plus_de_un_pour_cent(20, 2000) and an._plus_de_un_pour_cent(21, 2000)
    quatre = {"a": 1.0, "b": None, "c": None, "d": None}
    k = an.intervalle_rapporte(quatre, tirage(2), n=100)["tirages_degeneres"]
    assert (an.intervalle_rapporte(quatre, tirage(2), n=100)["etat"] == an.NON_CALCULABLE) == (k > 1)
    assert an.intervalle_rapporte({"a": None, "b": None}, tirage(3))["etat"] == an.NON_CALCULABLE      # jamais d'arrêt
    assert not any("dégénérés" in e for e in v.EVENEMENTS_A17)                       # aucun événement d'arrêt ne lui répond
    assert v.lire_table_a([]).lignes == ()
    with pytest.raises(GardeArret):
        an.intervalle_rapporte({}, tirage(1))


def test_student_sur_les_taches_qui_ont_une_valeur():
    """Métrique 3 : n = nombre de tâches qui ont une valeur ; moins de deux : borne non définie, jamais remplacée."""
    x = [0.1, 0.3, 0.2, 0.4, 0.0, 0.2]
    complet = an.student_des_taches({f"t{k}": v for k, v in enumerate(x)})
    troue = an.student_des_taches({**{f"t{k}": v for k, v in enumerate(x)}, "u1": None, "u2": None})
    attendu = float(np.mean(x)) - float(stats.t.ppf(0.975, 5)) * float(np.std(x, ddof=1)) / math.sqrt(6)
    assert complet["n"] == troue["n"] == 6 and troue["taches_sans_valeur"] == 2          # cinq degrés de liberté, non sept
    assert complet["borne_basse"] == pytest.approx(attendu) == troue["borne_basse"]
    une = an.student_des_taches({"a": 0.3, "b": None})
    assert une == {"moyenne": 0.3, "borne_basse": None, "borne_haute": None, "n": 1, "taches_sans_valeur": 1}
    assert an.student_des_taches({"a": None})["moyenne"] is None


def test_tirages_de_l_analyse_refusent_un_generateur_sans_cle():
    """Garde « tirage sans clé de 6.2 », au point du tirage (défaut C-7). Cas sain : un tirage à clé de l'usage.
    Artefacts : un générateur nu ; un générateur du système ; la clé d'un autre usage ; un tirage fabriqué à la main."""
    valeurs = {f"t{k:02d}": 0.1 * (k % 4) for k in range(16)}
    assert an.intervalle_rapporte(valeurs, tirage(1))["etat"] == an.CALCULE                              # cas sains
    assert an.page(np.tile(np.arange(5.0), (16, 1)), tirage_page(1), n=50)[1] < 0.05
    assert an.tirages_des_taches(tirage(2), g.USAGE_TACHES, 10, 16).shape == (10, 16)
    revision = g.tirage_de(g.cle("boot", "taches", "lot-honnete-appariement", revision=True), ENTROPIE)
    assert an.intervalle_rapporte(valeurs, revision)["etat"] == an.CALCULE                                # clé de la révision
    for nu in (rng(1), np.random.default_rng(), None, 7, "bras-a-v2/perm/page"):
        for fautif in (lambda: an.intervalle_rapporte(valeurs, nu), lambda: an.percentiles_taches({"a": [0.1], "b": [0.2]}, nu),
                       lambda: an.page(np.zeros((4, 3)), nu), lambda: an.tirages_des_taches(nu, g.USAGE_TACHES, 10, 16)):
            with pytest.raises(GardeArret, match="sans clé"):
                fautif()
    with pytest.raises(GardeArret, match="usage"):                                                        # clé d'un autre usage
        an.intervalle_rapporte(valeurs, tirage_page(1))
    with pytest.raises(GardeArret, match="usage"):
        an.page(np.zeros((4, 3)), tirage(1))
    with pytest.raises(GardeArret):
        an.tirages_des_taches(tirage(1), "boot/quelconque", 10, 16)
    with pytest.raises(GardeArret, match="tirage_de"):                                                    # fabriqué à la main
        g.TirageAClef(object(), "bras-a-v2/perm/page", 1, rng(1), False)
    with pytest.raises(GardeArret):                                                                       # clé du côté habilité
        g.tirage_de("bras-a-v2/perm/moniteur/juge/dose-0.50", ENTROPIE)
    with pytest.raises(GardeArret):                                                                       # objet figé
        tirage(1).cle = "bras-a-v2/perm/page"
    assert an.intervalle_rapporte(valeurs, tirage(1)) == an.intervalle_rapporte(valeurs, tirage(1))       # rejouable
    # un tirage ne sert qu'une fois (contre-lecture de la version 5, M-1) : réemployé, il rendait un autre intervalle
    meme = tirage(1)
    premier = an.intervalle_rapporte(valeurs, meme)
    with pytest.raises(GardeArret, match="déjà servi"):
        an.intervalle_rapporte(valeurs, meme)
    assert an.intervalle_rapporte({"t00": 0.3, **valeurs}, tirage(1))["tirages"] == premier["tirages"]


# --- Règle de discrétion : table des formes (6.9 du brouillon 24), pièce scellée, configuration scellée -------------------

J1, J075, J05, J025 = ("juge", 1.0), ("juge", 0.75), ("juge", 0.5), ("juge", 0.25)
MESSAGE_D_UN_ARRET = re.compile(
    r"arrêt de la lecture de la discrétion, étape \((m|n)\) — (garde|règle d'arrêt) : (" + "|".join(map(re.escape, ar.GARDES))
    + r") ; champ : (" + "|".join(map(re.escape, sorted(ar.CHAMPS_NOMMABLES))) + r") ; cas : (A|B|C|D|E|aucun cas)"
    + r"( ; lecture : (" + "|".join(ar.MONITEURS) + r"), (" + "|".join(map(re.escape, ar.FORMES_DOSE)) + r"))?")


def arret(fautif, garde=None, champ=None, cas=None, etape="m", lecture=None):
    """Un arrêt de la lecture de la discrétion : l'événement nommé, ses cinq éléments, et un message fait d'eux seuls."""
    with pytest.raises(ar.ArretDeLaLectureDeLaDiscretion) as e:
        fautif()
    x = e.value
    assert MESSAGE_D_UN_ARRET.fullmatch(str(x)), str(x)
    assert set(x.constat()) == {"garde", "champ", "cas", "etape", "moniteur", "dose"}
    for attendu, obtenu in ((garde, x.garde), (champ, x.champ), (cas, x.cas), (etape, x.etape)):
        assert attendu is None or attendu == obtenu, (attendu, obtenu, str(x))
    if lecture is not None:
        assert (x.moniteur, x.dose) == (lecture[0], h.forme(lecture[1]))
    return x


def etat(tmp, lecture, entree, **kw):
    return h.regle(tmp, {lecture: entree}, **kw)["etats"][lecture[1]][lecture[0]]


def _holm_seconde_ecriture(valeurs):
    ordre = sorted(valeurs, key=lambda k: valeurs[k])
    m_, ajustees, courant = len(ordre), {}, 0.0
    for j, k in enumerate(ordre):
        courant = max(courant, min(1.0, (m_ - j) * valeurs[k]))
        ajustees[k] = courant
    return ajustees


def _etat_seconde_ecriture(e, holm_p, seuil_des_tirages=21):
    """Seconde écriture, indépendante, de la règle de 6.9 sur une lecture admise : rend l'état."""
    if e["n_permutations"] is None or e["permutations_degenerees"] >= 21:
        return "indecis"
    if holm_p <= 0.05:
        return "repere"
    if e["tirages"] is None or e["tirages_degeneres"] >= seuil_des_tirages:
        return "indecis"
    return "ne repere pas" if e["valeur_p_bas"] > 0.05 and e["borne_haute"] < 0.60 else "indecis"


def test_regle_de_discretion_sur_une_piece_scellee_cas_sain(tmp_path):
    """Cas sain : cinq moniteurs, quatre doses, dix-huit noms chacun, tous au cas A ; quinze valeurs dans la famille,
    prises telles quelles ; le cas et le motif des vingt lectures rapportés ; `effectifs`, `exclues` et les aires de
    l'agrégateur rapportés tels que rendus ; les deux empreintes dans le résultat."""
    r = h.regle(tmp_path)
    assert len(r["famille"]) == 15 and set(r["famille"]) == {(mo, d) for mo in an.MONITEURS for d in an.DOSES_VERDICT}
    assert all(e == an.NE_REPERE_PAS for d in an.DOSES_VERDICT for e in r["etats"][d].values())
    assert set(r["lectures"]) == set(ar.FORMES_DOSE) and all(set(x) == set(an.MONITEURS) for x in r["lectures"].values())
    assert r["cas_et_motifs"] == {d: {mo: ("A", None) for mo in an.MONITEURS} for d in ar.FORMES_DOSE}       # les vingt lectures
    x = r["lectures"]["dose-0.25"]["juge"]
    assert "etat" not in x and "valeur_de_la_famille" not in x and x["rapport"]["aire"] == 0.52 and x["effectifs"] == {"honnete": 1280, "dose": 1280}
    assert r["exclues"] == {"non lu": 3} and r["agregateur"]["somme"]["dose-0.50"] == {"aire": 0.51}
    assert r["lectures_sous_le_motif_non_ajustable"] == {"par_moniteur": dict.fromkeys(an.MONITEURS, 0), "par_dose": dict.fromkeys(ar.FORMES_DOSE, 0)}
    assert set(r["choix"]) == set(cf.VALEURS_DES_CHOIX) and r["go_de_la_reprise"] is None
    assert r["livraison"]["sha256"] == h.empreinte(r["livraison"]["chemin"]) and r["configuration"]["sha256"] == h.empreinte(r["configuration"]["chemin"])
    assert [len(x) for x in (ar.CLES_PAR_MONITEUR_ET_PAR_DOSE, ar.CLES_DE_LA_LECTURE_COMMUNE, ar.CLES_DES_REGLAGES, ar.CLES_DES_SCORES_PAR_UNITE)] == [18, 11, 9, 5]
    an.exiger_resultat_de_discretion(r)
    # un moniteur qui repère : 5 aires permutées au moins égales, (1 + 5) ÷ 2 001 × 15 ≤ 0,05 ; 6 : ni l'un ni l'autre
    for egales, attendu in ((0, an.REPERE), (5, an.REPERE), (6, an.INDECIS), (150, an.NE_REPERE_PAS)):
        r = h.regle(tmp_path, {J075: h.cas_a("juge", 0.75, egales=egales)})
        assert r["etats"][0.75]["juge"] == attendu and r["famille"][J075] == (1 + egales) / 2001
        assert r["lectures"]["dose-0.75"]["juge"]["valeur_p_haut_holm"] == pytest.approx(min(1.0, 15 * (1 + egales) / 2001))


def test_une_lecture_de_chacun_des_cas_a_a_e_est_rangee_dans_son_cas(tmp_path):
    """8.4, « forme d'une livraison », cas sain : une lecture de chacun des cas A à E, chaque clé accordée à son cas,
    est acceptée et rangée dans son cas — reconnu à ses comptes, dans l'ordre B, C, E, D, A. Valeur de la famille, état
    et ce qui est rapporté : ceux de la table des formes."""
    change = {("classifieur-lexical", 1.0): h.cas_a("classifieur-lexical", 1.0, egales=999),
              ("moniteur-boite-noire", 1.0): h.cas_b("moniteur-boite-noire", 1.0),
              ("agregateur-sequentiel", 1.0): h.cas_c("agregateur-sequentiel", 1.0),
              ("classifieur-de-surface", 1.0): h.cas_d("classifieur-de-surface", 1.0, egales=999, borne=0.4),
              J1: h.cas_e("juge", 1.0, egales=0)}
    r = h.regle(tmp_path, change)
    cas = {mo: r["lectures"]["dose-1.00"][mo]["cas"] for mo in an.MONITEURS}
    assert cas == {"classifieur-lexical": "A", "moniteur-boite-noire": "B", "agregateur-sequentiel": "C", "classifieur-de-surface": "D", "juge": "E"}
    assert r["etats"][1.0] == {"classifieur-lexical": an.NE_REPERE_PAS, "moniteur-boite-noire": an.INDECIS,
                               "agregateur-sequentiel": an.INDECIS, "classifieur-de-surface": an.INDECIS, "juge": an.REPERE}
    f = r["famille"]
    assert f[("moniteur-boite-noire", 1.0)] == f[("agregateur-sequentiel", 1.0)] == 1.0 and f[J1] == 1 / 2001
    assert f[("classifieur-de-surface", 1.0)] == 1000 / 2001                              # la valeur p haute reste dans la famille
    rap = {mo: r["lectures"]["dose-1.00"][mo]["rapport"] for mo in an.MONITEURS}
    assert set(rap["moniteur-boite-noire"].values()) == {an.NON_CALCULABLE}               # B : tout non calculable
    assert rap["agregateur-sequentiel"]["valeur_p_haut"] == an.NON_CALCULABLE and rap["agregateur-sequentiel"]["aire"] == 0.52
    assert rap["agregateur-sequentiel"]["borne_haute"] == an.NON_RENDUE                   # C : borne `null`, non rendue
    assert rap["classifieur-de-surface"]["borne_haute"] == an.NON_CALCULABLE and 0.4 not in rap["classifieur-de-surface"].values()
    assert rap["juge"]["borne_haute"] == an.NON_CALCULABLE and rap["juge"]["valeur_p_haut"] == 1 / 2001
    assert r["cas_et_motifs"]["dose-1.00"]["juge"] == ("E", h.M_IMPOSSIBLE)
    an.exiger_resultat_de_discretion(r)
    # l'ordre de reconnaissance : C avant E et D (plancher et intervalle en défaut ensemble : cas C)
    for tirages in (dict(), dict(tirages=None, tirages_degeneres=None), dict(tirages=1500, tirages_degeneres=500)):
        r = h.regle(tmp_path, {J1: dict(h.cas_c("juge", 1.0), **tirages)})
        assert r["lectures"]["dose-1.00"]["juge"]["cas"] == "C" and r["etats"][1.0]["juge"] == an.INDECIS
    assert r["lectures"]["dose-1.00"]["juge"]["rapport"]["borne_haute"] == an.NON_CALCULABLE     # couple rempli, au-delà de 1 %
    # cas C, aire `null` : rapportée « non rendue », sans arrêt
    r = h.regle(tmp_path, {J1: h.cas_c("juge", 1.0, aire=None)})
    assert r["lectures"]["dose-1.00"]["juge"]["rapport"]["aire"] == an.NON_RENDUE and r["etats"][1.0]["juge"] == an.INDECIS


def test_etats_exclusifs_et_complets_par_enumeration(tmp_path):
    """Tous les croisements de valeur p, de borne haute, de permutations perdues (0, 20) et de tirages dégénérés
    (0, 20, 21, 500) : l'état rendu est celui d'une seconde écriture, la famille ajustée celle d'une seconde écriture
    de Holm ; un moniteur à l'intervalle dégénéré n'est jamais « ne repère pas », et sa borne est « non calculable »."""
    vus = set()
    for egales, borne, perdues, degeneres in itertools.product((0, 5, 6, 150, 999), (0.57, 0.60, 0.80), (0, 20), (0, 20, 21, 500)):
        e = (h.cas_d("juge", 1.0, egales=egales, borne=borne, perdues=perdues, degeneres=degeneres) if degeneres >= 21
             else h.cas_a("juge", 1.0, egales=egales, borne=borne, perdues=perdues, degeneres=degeneres))
        r = h.regle(tmp_path, {J1: e})
        ajustees = _holm_seconde_ecriture(r["famille"])
        x = r["lectures"]["dose-1.00"]["juge"]
        assert x["valeur_p_haut_holm"] == pytest.approx(ajustees[J1]) and x["etat"] == _etat_seconde_ecriture(e, ajustees[J1])
        assert r["famille"][J1] == e["valeur_p_haut"]                                    # jamais 1 de lui-même
        assert x["cas"] == ("D" if degeneres >= 21 else "A")
        assert x["rapport"]["borne_haute"] == (an.NON_CALCULABLE if degeneres >= 21 else borne)
        assert not (degeneres >= 21 and x["etat"] == an.NE_REPERE_PAS)
        vus.add(x["etat"])
    assert vus == {an.REPERE, an.NE_REPERE_PAS, an.INDECIS}


def test_ecarts_de_structure_arretent_a_toute_dose_et_sont_ranges_a_l_etape_m(tmp_path):
    """6.9, « Deux sortes d'écart », (1) ; 8.4, « forme d'une livraison » ; note du brouillon 24, point 16. Chaque
    écart de structure arrête la lecture **à une dose de la famille comme à la dose ¼**, et l'événement est **rangé à
    l'étape (m)** dans les deux cas : l'étape est celle de la pièce contrôlée, jamais celle de la dose."""
    sain = lambda d: h.cas_a("juge", d, egales=0)  # noqa: E731
    structure = {
        "un seul compte du couple des permutations": (lambda d: dict(sain(d), permutations_degenerees=None), "permutations_degenerees"),
        "un seul compte du couple des tirages": (lambda d: dict(sain(d), tirages=None), "tirages"),
        "permutations null et tirages remplis": (lambda d: dict(h.cas_b("juge", d), tirages=N, tirages_degeneres=0), "tirages"),
        "n_permutations autre que 2 000": (lambda d: dict(sain(d), n_permutations=1000), "n_permutations"),
        "total des tirages autre que 2 000": (lambda d: dict(sain(d), tirages=100), "tirages"),
        "total des tirages a 1 999": (lambda d: dict(sain(d), tirages=1980, tirages_degeneres=19), "tirages"),
        "compte negatif": (lambda d: dict(sain(d), permutations_degenerees=-1), "permutations_degenerees"),
        "compte non entier": (lambda d: dict(sain(d), tirages=1999.5), "tirages"),
        "compte en texte": (lambda d: dict(sain(d), n_permutations="2000"), "n_permutations"),
        "compte booleen": (lambda d: dict(sain(d), au_moins_egales=True), "au_moins_egales"),
        "compte plus grand que son total": (lambda d: dict(sain(d), permutations_degenerees=2001), "permutations_degenerees"),
        "aires au moins egales plus nombreuses que les permutations calculees": (lambda d: dict(sain(d), au_moins_egales=2001), "au_moins_egales"),
        "cas B, aire remplie": (lambda d: dict(h.cas_b("juge", d), aire=0.5), "aire"),
        "cas B, valeur p remplie": (lambda d: dict(h.cas_b("juge", d), valeur_p_haut=0.5), "valeur_p_haut"),
        "cas B, borne remplie": (lambda d: dict(h.cas_b("juge", d), borne_haute=0.5, quantile_borne_haute=Q), "borne_haute"),
        "motif hors de sa liste fermee": (lambda d: dict(h.cas_b("juge", d), motif="motif inconnu"), "motif"),
        "motif qui nomme un autre cas (B dit D)": (lambda d: h.cas_b("juge", d, motif=h.M_DEGENERES), "motif"),
        "motif qui nomme un autre cas (C dit B)": (lambda d: dict(h.cas_c("juge", d), motif=h.M_CLASSE), "motif"),
        "motif qui nomme un autre cas (D dit C)": (lambda d: dict(h.cas_d("juge", d), motif=h.M_PERDUES), "motif"),
        "cas A avec un motif de cause": (lambda d: dict(sain(d), motif=h.M_PERDUES), "motif"),
        "cas A avec un motif quelconque": (lambda d: dict(sain(d), motif="calculable"), "motif"),
        "cas D sans motif": (lambda d: dict(h.cas_d("juge", d), motif=None), "motif"),
        "motif qui n'est pas un texte": (lambda d: dict(sain(d), motif=3), "motif"),
        "calculable vrai au cas B": (lambda d: dict(h.cas_b("juge", d), calculable=True), "calculable"),
        "calculable vrai au cas C": (lambda d: dict(h.cas_c("juge", d), calculable=True), "calculable"),
        "calculable faux au cas A (valeur inscrite : vrai)": (lambda d: dict(sain(d), calculable=False), "calculable"),
        "calculable qui n'est pas un booleen": (lambda d: dict(sain(d), calculable=1), "calculable"),
        "quantile qui dit un autre quantile": (lambda d: dict(sain(d), quantile_borne_haute=0.95), "quantile_borne_haute"),
        "quantile arrondi a quatre decimales": (lambda d: dict(sain(d), quantile_borne_haute=round(Q, 4)), "quantile_borne_haute"),
        "borne rendue sans son quantile": (lambda d: dict(sain(d), quantile_borne_haute=None), "quantile_borne_haute"),
        "aire hors de [0, 1]": (lambda d: dict(sain(d), aire=1.2), "aire"),
        "aire en texte": (lambda d: dict(sain(d), aire="0.5"), "aire"),
        "valeur p qui n'est pas un nombre": (lambda d: dict(sain(d), valeur_p_bas=float("nan")), "valeur_p_bas"),
        "zero lu comme null : comptes a zero au cas B": (lambda d: dict(h.cas_b("juge", d), n_permutations=0, permutations_degenerees=0), "n_permutations"),
        "null lu comme zero : permutations perdues null au cas A": (lambda d: dict(sain(d), permutations_degenerees=None), "permutations_degenerees"),
        "cas E, borne remplie": (lambda d: dict(h.cas_e("juge", d), borne_haute=0.5, quantile_borne_haute=Q), "borne_haute"),
        "valeur p qui ne repond pas a ses comptes": (lambda d: dict(sain(d), valeur_p_haut=0.3, valeur_p_pour_la_famille=0.3), "valeur_p_haut"),
        "valeur p basse qui ne repond pas a ses comptes": (lambda d: dict(sain(d), valeur_p_bas=0.3), "valeur_p_bas"),
        "valeur p arrondie a six decimales": (lambda d: dict(h.cas_a("juge", d), valeur_p_haut=round(1000 / 2001, 6), valeur_p_pour_la_famille=round(1000 / 2001, 6)), "valeur_p_haut"),
        "entree hors de sa place (moniteur)": (lambda d: dict(sain(d), moniteur="classifieur-lexical"), "moniteur"),
        "entree hors de sa place (dose)": (lambda d: dict(sain(d), dose="dose-0.75" if d != 0.75 else "dose-1.00"), "dose"),
    }
    for nom, (fabrique, champ) in structure.items():
        for d in (1.0, 0.25):                                                             # la dose ¼ comprise
            x = arret(lambda: h.regle(tmp_path, {("juge", d): fabrique(d)}), champ=champ, etape="m", lecture=("juge", d))
            assert x.garde in (ar.GARDE_FORME, ar.GARDE_REGLAGES), nom
    # un compte entier écrit à virgule (2000.0) se lit comme l'entier : aucun arrêt à tort (contre-lecture de la version 5, M-9)
    r = h.regle(tmp_path, {J1: h.cas_a("juge", 1.0, tirages=2000.0, n_permutations=2000.0, au_moins_egales=999.0)})
    assert r["etats"][1.0]["juge"] == an.NE_REPERE_PAS and r["lectures"]["dose-1.00"]["juge"]["comptes"]["tirages"] == 2000
    # `effectifs` : aucune règle ne le lit ; rapporté tel que rendu, quelle que soit sa forme
    for effectifs in (None, {"pli0": {"honnete": 640}}, "non transmis"):
        assert h.regle(tmp_path, {J1: h.cas_a("juge", 1.0, effectifs=effectifs)})["lectures"]["dose-1.00"]["juge"]["effectifs"] == effectifs


def test_grandeur_null_que_le_cas_exige_arret_a_une_dose_de_la_famille_non_rendue_a_la_dose_un_quart(tmp_path):
    """6.9, « Deux sortes d'écart », (2) ; 8.4. Une grandeur `null` que son cas exige arrête la lecture à une dose de
    {½, ¾, 1} ; à la dose ¼ elle est rapportée « non rendue », sans arrêt, et la valeur de la famille n'y est ni lue ni
    contrôlée. Les artefacts des défauts B-1 et C-4 des contre-lectures précédentes y sont."""
    A = lambda d, **c: h.cas_a("juge", d, egales=0, **c)  # noqa: E731
    D = lambda d, **c: h.cas_d("juge", d, egales=0, **c)  # noqa: E731
    exigees = {
        "cas A, borne haute null (C-4)": (lambda d: A(d, borne=None, quantile_borne_haute=None), ar.GARDE_FORME, "borne_haute", "A"),
        "cas A, valeur p basse null (C-4)": (lambda d: A(d, valeur_p_bas=None), ar.GARDE_FORME, "valeur_p_bas", "A"),
        "cas A, valeur p haute null (B-1, sans tirage degenere)": (lambda d: A(d, valeur_p_haut=None, valeur_p_pour_la_famille=1.0), ar.GARDE_FORME, "valeur_p_haut", "A"),
        "cas A, aire null": (lambda d: A(d, aire=None), ar.GARDE_FORME, "aire", "A"),
        "cas A, aires au moins egales null": (lambda d: A(d, au_moins_egales=None), ar.GARDE_FORME, "au_moins_egales", "A"),
        "cas D, valeur p haute null, 1 dans la famille (B-1, 30 tirages degeneres)": (
            lambda d: D(d, valeur_p_bas=None, valeur_p_haut=None, valeur_p_pour_la_famille=1.0), ar.GARDE_INTERVALLE, "valeur_p_haut", "D"),
        "cas D, forme de la version 8 (tout null, 1 dans la famille)": (lambda d: h.v8_tirages_degeneres("juge", d), ar.GARDE_INTERVALLE, "valeur_p_haut", "D"),
        "cas D, aire null": (lambda d: D(d, aire=None, pli0=None, pli1=None), ar.GARDE_FORME, "aire", "D"),
    }
    for nom, (fabrique, garde, champ, cas) in exigees.items():
        arret(lambda: h.regle(tmp_path, {J1: fabrique(1.0)}), garde, champ, cas, "m", J1)
        r = h.regle(tmp_path, {J025: fabrique(0.25)})                                     # la même lecture à la dose ¼ : aucun arrêt
        x = r["lectures"]["dose-0.25"]["juge"]
        assert x["cas"] == cas and an.NON_RENDUE in list(x["rapport"].values()) + list(x["comptes"].values()) and "etat" not in x, nom
        assert all(e == an.NE_REPERE_PAS for p in an.DOSES_VERDICT for e in r["etats"][p].values())
    x = h.regle(tmp_path, {J025: h.v8_tirages_degeneres("juge", 0.25)})["lectures"]["dose-0.25"]["juge"]["rapport"]
    assert x["valeur_p_haut"] == x["aire"] == an.NON_RENDUE and x["borne_haute"] == an.NON_CALCULABLE
    # à la dose ¼, `valeur_p_pour_la_famille` n'est ni lue ni contrôlée
    for famille in (0.0, 1.0, None, "n'importe quoi", 7):
        assert h.regle(tmp_path, {J025: h.cas_a("juge", 0.25, valeur_p_pour_la_famille=famille)})["lectures"]["dose-0.25"]["juge"]["rapport"]["valeur_p_haut"] == 1000 / 2001


def test_valeur_de_la_famille_prise_telle_quelle_egalite_exacte_jamais_1_d_elle_meme(tmp_path):
    """8.4, « famille de Holm complète » et « intervalle dégénéré seul ». Cas sains : valeur égale à 1 avec sa cause
    (cas B, cas C) : gardée, m = 15, « indécis » ; cas A et D : la valeur p haute, exactement. Artefacts : valeur
    absente ; différente de la valeur p haute **fût-ce d'une décimale** (égalité exacte, sans tolérance) ; égale à 1
    alors que la valeur p haute est calculable ; autre chose que 1 aux cas B et C ; famille réduite."""
    for e in (h.cas_b("juge", 0.5), h.cas_b("juge", 0.5, motif=h.M_PLI), h.cas_c("juge", 0.5), h.cas_c("juge", 0.5, tirages=False)):
        r = h.regle(tmp_path, {J05: e})
        assert r["famille"][J05] == 1.0 and len(r["famille"]) == 15 and r["etats"][0.5]["juge"] == an.INDECIS
    p_haut = 6 / 2001
    for cas, sain in (("A", h.cas_a("juge", 0.5, egales=5)), ("D", h.cas_d("juge", 0.5, egales=5))):
        garde = ar.GARDE_FORME if cas == "A" else ar.GARDE_INTERVALLE
        assert h.regle(tmp_path, {J05: sain})["famille"][J05] == p_haut
        for fautive in (1.0, p_haut + 1e-12, p_haut - 1e-15, float(np.nextafter(p_haut, 1.0)), round(p_haut, 10), 0.5):
            arret(lambda: h.regle(tmp_path, {J05: dict(sain, valeur_p_pour_la_famille=fautive)}), garde, "valeur_p_pour_la_famille", cas, "m", J05)
        for absente in (None, "1", True, 1.5):
            arret(lambda: h.regle(tmp_path, {J05: dict(sain, valeur_p_pour_la_famille=absente)}), ar.GARDE_FAMILLE, "valeur_p_pour_la_famille", cas)
    for sain, cas in ((h.cas_b("juge", 0.5), "B"), (h.cas_c("juge", 0.5), "C")):
        for fautive in (0.4, 0.999999, None, 0.0):
            arret(lambda: h.regle(tmp_path, {J05: dict(sain, valeur_p_pour_la_famille=fautive)}), ar.GARDE_FAMILLE, "valeur_p_pour_la_famille", cas)
    # famille réduite : un moniteur, une dose ou une lecture qui manque — refusée (listes fermées, vingt lectures)
    for retire in (lambda s: s["lectures"]["dose-0.75"].pop("juge"), lambda s: s["lectures"].pop("dose-1.00"),
                   lambda s: s["lectures"].pop("dose-0.25"),                               # la dose ¼ comprise
                   lambda s: s["lectures"]["dose-0.50"].update({"base-mots-et-cout": h.cas_a("juge", 0.5)}),
                   lambda s: s["lectures"].update({"dose-0.10": s["lectures"]["dose-0.25"]}),
                   lambda s: s.update(lectures=[1, 2])):
        s = h.sortie()
        retire(s)
        arret(lambda: h.regle(tmp_path, contenu=s), ar.GARDE_LISTES, "lectures", ar.AUCUN_CAS)


def test_seuil_du_un_pour_cent_choix_nomme_un_essai_par_option(tmp_path):
    """Fiche 9 (point 18) : le seuil est un **choix nommé de la configuration**, lu en un seul endroit. Option (a), sur
    les tirages demandés : 20 tirages dégénérés, cas A ; 21, cas D. Option (b), sur les tirages calculés : 20, cas D ;
    19, cas A — pour les seuls tirages de l'intervalle : le plancher ne change pas. Et sous (b), un module resté à
    l'option (a), qui rend 20 tirages dégénérés sans le motif de l'intervalle dégénéré, arrête la lecture."""
    a, b = {cf.CHOIX_SEUIL: cf.SEUIL_SUR_LES_DEMANDES}, {cf.CHOIX_SEUIL: cf.SEUIL_SUR_LES_CALCULES}
    cas = lambda e, choix: h.regle(tmp_path, {J05: e}, choix=choix)["lectures"]["dose-0.50"]["juge"]["cas"]  # noqa: E731
    assert cas(h.cas_a("juge", 0.5, degeneres=20), a) == "A" and cas(h.cas_d("juge", 0.5, degeneres=21), a) == "D"
    assert cas(h.cas_d("juge", 0.5, degeneres=2000), a) == "D"                             # zéro tirage calculé
    assert cas(h.cas_a("juge", 0.5, degeneres=19), b) == "A" and cas(h.cas_d("juge", 0.5, degeneres=20), b) == "D"
    arret(lambda: h.regle(tmp_path, {J05: h.cas_a("juge", 0.5, degeneres=20)}, choix=b), ar.GARDE_FORME, "motif", "D")   # module resté à (a)
    arret(lambda: h.regle(tmp_path, {J05: h.cas_d("juge", 0.5, degeneres=20)}, choix=a), ar.GARDE_FORME, "motif", "A")
    for choix in (a, b):                                                                   # le plancher : 21 sous les deux options
        assert cas(h.cas_a("juge", 0.5, perdues=20), choix) == "A" and cas(h.cas_c("juge", 0.5, perdues=21), choix) == "C"
    assert not an.intervalle_au_dela_de_un_pour_cent(1980, 20, cf.SEUIL_SUR_LES_DEMANDES) and an.intervalle_au_dela_de_un_pour_cent(1979, 21, cf.SEUIL_SUR_LES_DEMANDES)
    assert an.intervalle_au_dela_de_un_pour_cent(1980, 20, cf.SEUIL_SUR_LES_CALCULES) and not an.intervalle_au_dela_de_un_pour_cent(1981, 19, cf.SEUIL_SUR_LES_CALCULES)
    for sans in (None, "", "option a", "sur les tirages"):
        with pytest.raises(GardeArret, match="fiche 9"):
            an.intervalle_au_dela_de_un_pour_cent(1980, 20, sans)
    with pytest.raises(TypeError):                                                         # aucun seuil par défaut
        an.intervalle_au_dela_de_un_pour_cent(1980, 20)


def test_intervalle_impossible_choix_nomme_un_essai_par_redaction(tmp_path):
    """Fiche 10 (point 19) ; table des formes, cas E ; 8.4. Un seul choix nommé, sans valeur par défaut, à trois
    valeurs.
    (a) comme un intervalle dégénéré : valeur p haute exigée et mise dans la famille ; « repère » ou « indécis », jamais
        « ne repère pas » ; borne « non calculable ». Artefacts : valeur p `null`, ou 1 dans la famille.
    (b) « indécis » d'office : valeur 1 gardée, valeurs p non lues. Artefact : autre chose que 1.
    (c) anomalie : à une dose de la famille, la lecture s'arrête — règle d'arrêt « intervalle impossible », cas E,
        étape (m), sans recopier le motif ; à la dose ¼, aucun arrêt."""
    A, B, C = ({cf.CHOIX_INTERVALLE_IMPOSSIBLE: x} for x in (cf.INTERVALLE_COMME_DEGENERE, cf.INTERVALLE_INDECIS_D_OFFICE, cf.INTERVALLE_ANOMALIE))
    # (a)
    for egales, attendu in ((0, an.REPERE), (999, an.INDECIS)):
        r = h.regle(tmp_path, {J1: h.cas_e("juge", 1.0, egales=egales)}, choix=A)
        x = r["lectures"]["dose-1.00"]["juge"]
        assert r["etats"][1.0]["juge"] == attendu and r["famille"][J1] == (1 + egales) / 2001 and x["cas"] == "E"
        assert x["rapport"]["borne_haute"] == an.NON_CALCULABLE and x["motif"] == h.M_IMPOSSIBLE
    arret(lambda: h.regle(tmp_path, {J1: h.cas_e("juge", 1.0, redaction="b")}, choix=A), ar.GARDE_INTERVALLE, "valeur_p_pour_la_famille", "E")
    arret(lambda: h.regle(tmp_path, {J1: h.cas_e("juge", 1.0, valeur_p_haut=None, valeur_p_bas=None, valeur_p_pour_la_famille=1.0)}, choix=A),
          ar.GARDE_INTERVALLE, "valeur_p_haut", "E")
    assert h.regle(tmp_path, {J025: h.cas_e("juge", 0.25, valeur_p_haut=None, valeur_p_bas=None)}, choix=A)["lectures"]["dose-0.25"]["juge"]["rapport"]["valeur_p_haut"] == an.NON_RENDUE
    # (b)
    for e in (h.cas_e("juge", 1.0, egales=0, redaction="b"),
              h.cas_e("juge", 1.0, redaction="b", aire=None, pli0=None, pli1=None, valeur_p_bas=None, valeur_p_haut=None, au_moins_egales=None)):
        r = h.regle(tmp_path, {J1: e}, choix=B)
        assert r["etats"][1.0]["juge"] == an.INDECIS and r["famille"][J1] == 1.0
        assert r["lectures"]["dose-1.00"]["juge"]["rapport"]["borne_haute"] == an.NON_CALCULABLE
    assert r["lectures"]["dose-1.00"]["juge"]["rapport"]["aire"] == an.NON_RENDUE          # telle que rendue, « non rendue » si `null`
    arret(lambda: h.regle(tmp_path, {J1: h.cas_e("juge", 1.0, egales=0)}, choix=B), ar.GARDE_FAMILLE, "valeur_p_pour_la_famille", "E")
    # (c)
    for e in (h.cas_e("juge", 1.0, egales=0), h.cas_e("juge", 1.0, redaction="b")):
        x = arret(lambda: h.regle(tmp_path, {J1: e}, choix=C), ar.REGLE_INTERVALLE_IMPOSSIBLE, "tirages", "E", "m", J1)
        assert "règle d'arrêt : intervalle impossible" in str(x) and h.M_IMPOSSIBLE not in str(x)
    r = h.regle(tmp_path, {J025: h.cas_e("juge", 0.25)}, choix=C)                           # à la dose ¼ : pas d'arrêt
    assert r["lectures"]["dose-0.25"]["juge"]["cas"] == "E" and r["lectures"]["dose-0.25"]["juge"]["rapport"]["borne_haute"] == an.NON_CALCULABLE


def test_moniteur_appris_non_ajustable_choix_nomme_un_essai_par_redaction(tmp_path):
    """Fiche 11 (point 20) ; 8.4, « moniteur appris non ajustable » : un cas sain et un artefact par rédaction.
    (a) lecture au cas B sous ce motif, valeur 1 gardée, « indécis » ; (b) à une dose de la famille, lecture arrêtée —
    règle d'arrêt « moniteur appris non ajustable », cas B —, et à la dose ¼ aucun arrêt, grandeurs « non
    calculables » avec le motif ; (c) pour l'analyse, comme (a) (le module ne rend plus ce motif pour une séparation).
    Dans les trois, le nombre de lectures sous ce motif est rapporté par moniteur et par dose."""
    A, B, C = ({cf.CHOIX_NON_AJUSTABLE: x} for x in (cf.NON_AJUSTABLE_AIRE_NON_CALCULABLE, cf.NON_AJUSTABLE_ANOMALIE, cf.NON_AJUSTABLE_MODULE_CORRIGE))
    L, S = "classifieur-lexical", "classifieur-de-surface"
    change = {(L, 0.5): h.cas_b(L, 0.5, motif=h.M_NON_AJUSTABLE), (L, 0.25): h.cas_b(L, 0.25, motif=h.M_NON_AJUSTABLE),
              (S, 0.5): h.cas_b(S, 0.5, motif=h.M_NON_AJUSTABLE)}
    for choix in (A, C):
        r = h.regle(tmp_path, change, choix=choix)
        assert r["etats"][0.5][L] == r["etats"][0.5][S] == an.INDECIS and r["famille"][(L, 0.5)] == 1.0
        compte = r["lectures_sous_le_motif_non_ajustable"]
        assert compte["par_moniteur"][L] == 2 and compte["par_moniteur"][S] == 1 and compte["par_moniteur"]["juge"] == 0
        assert compte["par_dose"] == {"dose-0.25": 1, "dose-0.50": 2, "dose-0.75": 0, "dose-1.00": 0}
        an.exiger_resultat_de_discretion(r)
        retouche = copy.deepcopy(r)
        del retouche["lectures_sous_le_motif_non_ajustable"]                              # compte absent du rapport : refusé
        with pytest.raises(GardeArret):
            an.exiger_resultat_de_discretion(retouche)
    x = arret(lambda: h.regle(tmp_path, change, choix=B), ar.REGLE_NON_AJUSTABLE, "motif", "B", "m", (L, 0.5))
    assert h.M_NON_AJUSTABLE not in str(x)
    r = h.regle(tmp_path, {(L, 0.25): h.cas_b(L, 0.25, motif=h.M_NON_AJUSTABLE)}, choix=B)   # à la dose ¼ : aucun arrêt
    x = r["lectures"]["dose-0.25"][L]
    assert set(x["rapport"].values()) == {an.NON_CALCULABLE} and x["motif"] == h.M_NON_AJUSTABLE
    assert r["lectures_sous_le_motif_non_ajustable"]["par_dose"]["dose-0.25"] == 1
    # les autres causes du cas B ne sont jamais une anomalie
    assert h.regle(tmp_path, {(L, 0.5): h.cas_b(L, 0.5, motif=h.M_CLASSE)}, choix=B)["etats"][0.5][L] == an.INDECIS


def test_reglages_rendus_un_essai_par_artefact(tmp_path):
    """8.4, « réglages rendus » ; contre-lecture du code de la version 5, C-2 et C-3. Cas sains : réglages du texte et
    déclaration du schéma retenu, sous l'un et l'autre schéma. Un artefact par réglage : `n_tirages`,
    `n_permutations`, `taille_de_la_famille`, `niveau`, doses de la famille, `dose_pour_information`,
    `statistique_agregateur`, `permutation`, `unite_de_la_permutation` ; `n_permutations` d'une lecture différent de
    celui des réglages ; livraison tirée sous l'autre schéma que celui retenu."""
    for schema in (cf.SCHEMA_LIBRE, cf.SCHEMA_ECHANGE):
        assert h.regle(tmp_path, choix={cf.CHOIX_SCHEMA: schema})["reglages"]["schema"] == schema
    artefacts = {"n_permutations": [1000, None, True, "2000"], "n_tirages": [200, 2001], "taille_de_la_famille": [12, 16],
                 "niveau": [0.10, "0.05"], "doses_de_la_famille": [["dose-0.25"], ["dose-0.50", "dose-0.75"], None, "dose-0.50"],
                 "dose_pour_information": [None, "dose-0.50", 0.25], "statistique_agregateur": ["maximum", None, "moyenne"],
                 "permutation": ["action par action", None, ""], "unite_de_la_permutation": ["action", 3]}
    for nom, valeurs in artefacts.items():
        for v_ in valeurs:
            arret(lambda: h.regle(tmp_path, reglages=h.reglages(**{nom: v_})), ar.GARDE_REGLAGES, f"reglages.{nom}", ar.AUCUN_CAS, "m")
    # la contre-lecture (C-3) : trois réglages faux ensemble passaient sans un mot
    arret(lambda: h.regle(tmp_path, reglages=h.reglages(statistique_agregateur="maximum", doses_de_la_famille=["dose-0.25"], dose_pour_information=None)),
          ar.GARDE_REGLAGES)
    for retenu, livre in ((cf.SCHEMA_ECHANGE, cf.SCHEMA_LIBRE), (cf.SCHEMA_LIBRE, cf.SCHEMA_ECHANGE)):
        arret(lambda: h.regle(tmp_path, choix={cf.CHOIX_SCHEMA: retenu}, reglages=h.reglages(livre)), ar.GARDE_REGLAGES, "reglages.permutation")
    arret(lambda: h.regle(tmp_path, {J05: h.cas_a("juge", 0.5, n_permutations=1000)}), ar.GARDE_REGLAGES, "n_permutations", lecture=J05)
    # la contre-lecture (C-2) : des déclarations recopiées de la livraison par l'appelant — il n'y a plus où les donner
    with pytest.raises(TypeError):
        an.regle_de_discretion(h.piece(tmp_path, h.sortie()), h.fichier_de_configuration(tmp_path), dossier_des_arrets=h.nouveau_dossier(tmp_path),
                               go_de_la_reprise=None, declarations_du_schema={})
    with pytest.raises(TypeError):
        an.regle_de_discretion(h.piece(tmp_path, h.sortie()), h.fichier_de_configuration(tmp_path), dossier_des_arrets=h.nouveau_dossier(tmp_path),
                               go_de_la_reprise=None, schema_de_permutation=cf.SCHEMA_LIBRE)
    assert not hasattr(pe, "DECLARATIONS_DU_SCHEMA")                                       # plus de table dans le module


def test_listes_fermees_des_noms_rendus_un_champ_de_plus_ou_de_moins_arrete(tmp_path):
    """8.4, « listes fermées des noms rendus ». Cas sain : les quatre listes à la lettre, l'ordre des clés ne comptant
    pas. Artefacts : une clé de plus, une clé de moins, dans chacune des quatre listes ; un champ en double. L'arrêt
    nomme la liste, jamais le champ inconnu."""
    s = h.sortie()
    h.regle(tmp_path, contenu=dict(reversed(list(s.items()))))                             # l'ordre ne compte pas
    e = h.cas_a("juge", 0.5)
    listes = {
        ar.LISTE_DES_ONZE: [dict(s, texte_ajoute="ACTION: ADD"), {k: x for k, x in s.items() if k != "exclues"}, [1, 2], "sortie"],
        ar.LISTE_DES_NEUF: [dict(s, reglages=dict(h.reglages(), graine=7)), dict(s, reglages={k: x for k, x in h.reglages().items() if k != "niveau"}),
                            dict(s, reglages=None)],
        ar.LISTE_DES_CINQ: [dict(s, scores_par_unite=dict(s["scores_par_unite"], chemin="x")),
                            dict(s, scores_par_unite={k: x for k, x in s["scores_par_unite"].items() if k != "forme"}), dict(s, scores_par_unite="x")],
        ar.LISTE_DES_DIX_HUIT: [h.sortie({J05: dict(e, score=0.7)}), h.sortie({J05: {k: x for k, x in e.items() if k != "quantile_borne_haute"}}),
                                h.sortie({J025: dict(h.cas_a("juge", 0.25), aires_des_plis=[0.5, 0.5])}), h.sortie({J05: "lecture"})],
    }
    for liste, artefacts in listes.items():
        for fautif in artefacts:
            x = arret(lambda: h.regle(tmp_path, contenu=fautif), ar.GARDE_LISTES, liste, ar.AUCUN_CAS, "m")
            assert "texte_ajoute" not in str(x) and "score" not in str(x).replace("scores_par_unite", "")
    for texte in (json.dumps(s).replace('"plis":', '"exclues": 1, "plis":', 1).replace('"exclues": {"non lu": 3}, ', "", 1) + "",
                  json.dumps(s)[:-1] + ', "plis": {}}'):
        if texte.count('"plis"') == 2 or texte.count('"exclues"') == 2:
            arret(lambda: h.regle(tmp_path, contenu=texte), ar.GARDE_LISTES, ar.CHAMP_EN_DOUBLE, ar.AUCUN_CAS, "m")
    arret(lambda: h.regle(tmp_path, contenu="{pas du json"), ar.GARDE_LISTES, ar.LISTE_DES_ONZE)


def test_la_sortie_du_programme_qui_refuse_ne_porte_aucune_valeur_de_la_livraison(tmp_path):
    """6.9, « Ce que rend le programme qui refuse — définition unique » ; 8.4 ; notes des brouillons 23 et 24, point 15.
    Pour chaque sorte de refus : le message et le fichier scellé de l'arrêt portent les cinq éléments permis — garde ou
    règle d'arrêt, nom du champ, lettre du cas, étape, moniteur et dose — et **aucun nombre de la livraison, ni la
    chaîne de son champ `motif`, ni la valeur de `calculable`**, ni aucun nom de champ inconnu."""
    nombres = dict(aire=0.123456789, pli0=0.113456789, pli1=0.133456789, borne_haute=0.587654321)
    secrets = ["0.123456789", "0.113456789", "0.133456789", "0.587654321", "MOTIF-QUE-RIEN-NE-DOIT-RECOPIER", "champ_inconnu_de_la_livraison",
               "1234567", "0.0004997", "777", h.M_NON_AJUSTABLE, h.M_IMPOSSIBLE, h.M_DEGENERES, "True", "False", "true", "false"]
    base = lambda d=1.0, **c: {**h.cas_a("juge", d, egales=0), **nombres, **c}  # noqa: E731
    refus = [
        ({J1: base(motif="MOTIF-QUE-RIEN-NE-DOIT-RECOPIER")}, {}),                          # motif hors de sa liste
        ({J1: base(calculable=False)}, {}),                                                # calculable contredit la table
        ({J1: base(tirages=1234567)}, {}),                                                 # compte
        ({J1: base(valeur_p_pour_la_famille=0.0004997)}, {}),                              # valeur de la famille
        ({J1: base(valeur_p_haut=None)}, {}),                                              # grandeur exigée
        ({J1: {**base(), "champ_inconnu_de_la_livraison": 777}}, {}),                      # liste fermée
        ({J1: base(effectifs=777, quantile_borne_haute=0.777)}, {}),                       # quantile
        ({J025: base(0.25, n_permutations=777)}, {}),                                      # dose ¼ : étape (m)
        ({J1: {**h.cas_e("juge", 1.0, egales=0), **{k: x for k, x in nombres.items() if k != "borne_haute"}}}, {cf.CHOIX_INTERVALLE_IMPOSSIBLE: cf.INTERVALLE_ANOMALIE}),
        ({("classifieur-lexical", 1.0): h.cas_b("classifieur-lexical", 1.0, motif=h.M_NON_AJUSTABLE)}, {cf.CHOIX_NON_AJUSTABLE: cf.NON_AJUSTABLE_ANOMALIE}),
        ({J1: {**h.cas_d("juge", 1.0, egales=0), **{k: x for k, x in nombres.items() if k != "borne_haute"}, "valeur_p_pour_la_famille": 1.0}}, {}),
    ]
    for change, choix in refus:
        dossier = h.nouveau_dossier(tmp_path, "arrets")
        x = arret(lambda: h.regle(tmp_path, change, choix=choix, dossier=dossier), etape="m")
        fichiers = sorted(p for p in dossier.iterdir() if not p.name.endswith(".sha256"))
        assert len(fichiers) == 1 and Path(str(fichiers[0]) + ".sha256").is_file()           # l'arrêt est consigné, scellé
        consigne = json.loads(fichiers[0].read_text(encoding="utf-8"))
        assert set(consigne) == {"evenement", "constat", "sha256_de_la_livraison"} and consigne["constat"] == x.constat()
        assert set(consigne["constat"]) == {"garde", "champ", "cas", "etape", "moniteur", "dose"}
        sorties = str(x) + repr(x) + repr(x.args) + fichiers[0].read_text(encoding="utf-8").replace(consigne["sha256_de_la_livraison"], "")
        for secret in secrets:
            assert secret not in sorties, (secret, sorties)
    # un constat ne se fabrique qu'avec ses éléments permis, pris dans leurs listes fermées
    for fautif in (dict(garde=ar.GARDE_FORME, champ="aire = 0.71", cas="A", etape="m"), dict(garde=ar.GARDE_FORME, champ="aire", cas="A", etape="l"),
                   dict(garde="garde inventée", champ="aire", cas="A", etape="m"), dict(garde=ar.GARDE_FORME, champ="aire", cas="F", etape="m"),
                   dict(garde=ar.GARDE_FORME, champ="aire", cas="A", etape="m", moniteur="juge"),
                   dict(garde=ar.GARDE_FORME, champ="aire", cas="A", etape="m", moniteur="juge", dose="0.71"),
                   dict(garde=ar.GARDE_FORME, champ="aire", cas="A", etape="m", moniteur="un texte de la livraison", dose="dose-0.50")):
        with pytest.raises(GardeArret) as e:
            ar.ArretDeLaLectureDeLaDiscretion(**fautif)
        assert not isinstance(e.value, ar.ArretDeLaLectureDeLaDiscretion) and "0.71" not in str(e.value)
    with pytest.raises(GardeArret):
        ar.exiger_constat({**x.constat(), "valeur": 0.71})


def test_aucun_etat_ne_sort_apres_un_arret_et_une_livraison_refusee_n_est_pas_relue(tmp_path, monkeypatch):
    """6.9, « Commun aux trois rédactions » ; 8.4. Après un arrêt : aucun état n'est dit (la règle ne rend rien) ;
    l'arrêt est consigné ; **la livraison refusée n'est pas relue** ; **une livraison refaite n'est lue que sur une
    ligne de GO** du registre du dépôt, qui porte la phrase d'accord et aucun mot de refus."""
    dossier = h.nouveau_dossier(tmp_path, "arrets")
    refusee = h.piece(tmp_path, h.sortie({J1: h.cas_a("juge", 1.0, borne=None, quantile_borne_haute=None)}))
    config = h.fichier_de_configuration(tmp_path)
    lit = lambda p, go=None: an.regle_de_discretion(p, config, dossier_des_arrets=dossier, go_de_la_reprise=go)  # noqa: E731
    resultat = None
    with pytest.raises(ar.ArretDeLaLectureDeLaDiscretion):
        resultat = lit(refusee)
    assert resultat is None                                                                # aucun état, aucun résultat
    assert len([p for p in dossier.iterdir() if p.suffix == ".json"]) == 1
    with pytest.raises(GardeArret, match="déjà refusée") as e:                             # elle n'est pas relue
        lit(refusee)
    assert not isinstance(e.value, ar.ArretDeLaLectureDeLaDiscretion)
    refaite = h.piece(tmp_path, h.sortie())
    bon, refus, autre = "GO-2026-11-21-01", "GO-2026-11-21-02", "GO-2026-11-21-03"
    monkeypatch.setattr(g, "REGISTRE_DES_ACCORDS", h.registre(tmp_path, [
        f"| {bon} | 2026-11-21 | décision | {g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE} | Lazar |",
        f"| {refus} | 2026-11-21 | décision | refus : {g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE} | Lazar |",
        f"| {autre} | 2026-11-21 | calcul | devis de la course des cartes | Lazar |"]))
    for go in (None, "", "go de Lazar", "GO-1999-01-01-00", refus, autre):                 # sans le mot de Lazar
        with pytest.raises(GardeArret):
            lit(refaite, go)
    r = lit(refaite, bon)                                                                  # cas sain : livraison refaite, sur une ligne de GO
    assert r["go_de_la_reprise"] == bon and all(x == an.NE_REPERE_PAS for x in r["etats"][1.0].values())
    an.exiger_resultat_de_discretion(r)
    # sans arrêt consigné, aucune ligne de GO n'est demandée ; le dossier des arrêts est exigé
    assert h.regle(tmp_path)["go_de_la_reprise"] is None
    for absent in (None, tmp_path / "absent", config):
        with pytest.raises(GardeArret):
            an.regle_de_discretion(refaite, config, dossier_des_arrets=absent, go_de_la_reprise=None)
    with pytest.raises(TypeError):                                                         # deux arguments sans valeur par défaut
        an.regle_de_discretion(refaite, config)
    # un fichier d'arrêt retouché, ou d'une autre forme, est refusé
    f = next(p for p in dossier.iterdir() if p.suffix == ".json")
    f.write_text(f.read_text(encoding="utf-8").replace('"cas": "A"', '"cas": "A", "aire": 0.71'), encoding="utf-8")
    with pytest.raises(GardeArret):
        lit(refaite, bon)


def test_la_regle_se_lit_sur_deux_fichiers_scelles_et_sa_garde_de_sortie_les_relit(tmp_path):
    """Contre-lecture du code de la version 5, C-1, et son essai d'attaque « C-2 résiduel ». Cas sain : un résultat lu
    de la pièce scellée et de la configuration scellée. Artefacts : la règle sur un dictionnaire ; une pièce ou une
    configuration non scellée ou retouchée ; **la retouche cohérente** — sur un résultat où le juge « ne repère pas »,
    on met les aires au moins égales à zéro et les deux valeurs p à 1/2001, dans la lecture et dans la famille, puis
    on recalcule Holm et les états : la version 5 rendait « repère » ; ici la garde relit la pièce et refuse."""
    r = h.regle(tmp_path)
    an.exiger_resultat_de_discretion(r)
    assert an.etats_pour_la_table_c(r, 1.0)["juge d'une autre lignée"] == an.NE_REPERE_PAS
    coherent = copy.deepcopy(r)                                                             # la retouche cohérente
    x = coherent["lectures"]["dose-1.00"]["juge"]
    x["comptes"]["au_moins_egales"] = 0
    x["rapport"].update(valeur_p_bas=1 / 2001, valeur_p_haut=1 / 2001)
    x["valeur_de_la_famille"] = coherent["famille"][J1] = 1 / 2001
    _, ajustees = an.holm(dict(coherent["famille"]), 0.05)
    for (mo, p), hp in ajustees.items():
        y = coherent["lectures"][h.forme(p)][mo]
        y["valeur_p_haut_holm"] = hp
        y["etat"] = coherent["etats"][p][mo] = an.etat_du_moniteur(y["regle"], y["rapport"]["valeur_p_bas"], hp, y["rapport"]["borne_haute"])
    assert coherent["etats"][1.0]["juge"] == an.REPERE                                     # la retouche est cohérente…
    for porte in (lambda: an.exiger_resultat_de_discretion(coherent), lambda: an.etats_pour_la_table_c(coherent, 1.0),
                  lambda: an.lectures_pour_la_table_c(coherent, 1.0), lambda: an._contenu_du_fichier_de_l_etape_m(coherent, {})):
        with pytest.raises(GardeArret, match="retouché"):                                  # … et refusée partout
            porte()
    retouches = {"etat seul": lambda x: x["etats"][1.0].__setitem__("juge", an.INDECIS),
                 "famille seule": lambda x: x["famille"].__setitem__(J1, 1.0),
                 "famille reduite": lambda x: x["famille"].pop(J1),
                 "drapeau": lambda x: x["lectures"]["dose-1.00"]["juge"].__setitem__("valeur_p_absente_prise_pour_1", True),
                 "cas": lambda x: x["lectures"]["dose-1.00"]["juge"].__setitem__("cas", "B"),
                 "borne": lambda x: x["lectures"]["dose-0.50"]["juge"]["rapport"].__setitem__("borne_haute", 0.2),
                 "dose un quart": lambda x: x["lectures"]["dose-0.25"]["juge"]["rapport"].__setitem__("aire", 0.9),
                 "choix": lambda x: x["choix"].__setitem__(cf.CHOIX_SEUIL, cf.SEUIL_SUR_LES_CALCULES),
                 "empreinte de la livraison": lambda x: x["livraison"].__setitem__("sha256", "0" * 64),
                 "empreinte de la configuration": lambda x: x["configuration"].__setitem__("sha256", "0" * 64),
                 "autre piece": lambda x: x["livraison"].__setitem__("chemin", str(h.piece(tmp_path, h.sortie({J1: h.cas_a("juge", 1.0, egales=0)})))),
                 "sans livraison": lambda x: x.pop("livraison")}
    for nom, f in retouches.items():
        y = copy.deepcopy(r)
        f(y)
        with pytest.raises(GardeArret):
            an.exiger_resultat_de_discretion(y)
    for fautif in (None, {}, [], "resultat"):
        with pytest.raises(GardeArret):
            an.exiger_resultat_de_discretion(fautif)
    # la règle ne se lit pas sur un dictionnaire ; pièce et configuration répondent à leur compagnon
    config, dossier = h.fichier_de_configuration(tmp_path), h.nouveau_dossier(tmp_path)
    lit = lambda p, c=config: an.regle_de_discretion(p, c, dossier_des_arrets=dossier, go_de_la_reprise=None)  # noqa: E731
    p = h.piece(tmp_path, h.sortie())
    lit(p)
    for fautif in (h.sortie(), json.dumps(h.sortie()), None, tmp_path / "absente.json"):
        with pytest.raises(GardeArret):
            lit(fautif)
    with pytest.raises(GardeArret):
        lit(p, h.configuration())                                                          # configuration donnée en dictionnaire
    non_scellee = h.nouveau_dossier(tmp_path) / "piece.json"
    non_scellee.write_text(json.dumps(h.sortie()), encoding="utf-8")
    with pytest.raises(GardeArret, match="compagnon"):
        lit(non_scellee)
    p.write_text(p.read_text(encoding="utf-8").replace("0.52", "0.53", 1), encoding="utf-8")   # retouchée après son scellement
    with pytest.raises(GardeArret):
        lit(p)
    assert not list(dossier.iterdir())                                                     # aucun de ces refus n'est un arrêt de la discrétion
    lu = h.regle(tmp_path)                                                                  # un résultat lu, dont la pièce est ensuite retouchée
    q = Path(lu["livraison"]["chemin"])
    q.write_text(q.read_text(encoding="utf-8").replace("0.52", "0.53", 1), encoding="utf-8")
    with pytest.raises(GardeArret):
        an.exiger_resultat_de_discretion(lu)


def test_configuration_scellee_cinq_choix_sans_valeur_par_defaut(tmp_path):
    """La configuration scellée porte les cinq choix nommés et les chaînes du module ; **aucun choix n'a de valeur par
    défaut**. Cas sain : chaque valeur permise de chaque choix. Artefacts : un choix absent, vide, approchant ou de
    trop ; une chaîne absente ou non inscrite ; un motif sans cause, une cause sans motif ; deux schémas qui se
    déclarent pareil ; un fichier non scellé, retouché, illisible ; un dictionnaire à la place du chemin."""
    for nom, permises in cf.VALEURS_DES_CHOIX.items():
        for valeur in permises:
            c = cf.lire_la_configuration_scellee(h.fichier_de_configuration(tmp_path, {nom: valeur}))
            assert cf.choix(c, nom) == valeur and len(c["sha256"]) == 64
    assert len(cf.VALEURS_DES_CHOIX) == 5 and [len(x) for x in cf.VALEURS_DES_CHOIX.values()] == [2, 2, 3, 3, 3]
    ecrire = lambda contenu: h.ecrire_scelle(h.nouveau_dossier(tmp_path, "configuration") / "c.json", contenu)  # noqa: E731
    bonne = h.configuration()
    for nom in cf.VALEURS_DES_CHOIX:
        for fautive in (None, "", "a", "option (a)", True, cf.VALEURS_DES_CHOIX[nom][0].upper(), [cf.VALEURS_DES_CHOIX[nom][0]]):
            with pytest.raises(GardeArret, match="aucune valeur par défaut"):
                cf.lire_la_configuration_scellee(ecrire({**bonne, "choix": {**bonne["choix"], nom: fautive}}))
        with pytest.raises(GardeArret, match="pas de valeur par défaut"):                   # choix omis
            cf.lire_la_configuration_scellee(ecrire({**bonne, "choix": {k: x for k, x in bonne["choix"].items() if k != nom}}))
    chaines = bonne["chaines_du_module"]
    fautives = [{**bonne, "choix": {**bonne["choix"], "choix_de_trop": "x"}}, {"choix": bonne["choix"]}, {**bonne, "autre": 1}, [bonne], "configuration"]
    for nom in cf.CHAINES:
        fautives.append({**bonne, "chaines_du_module": {k: x for k, x in chaines.items() if k != nom}})
    for nom, valeur in (("motifs", {}), ("motifs", {h.M_CLASSE: cf.CAUSE_ANTERIEURE}), ("motifs", {**h.MOTIFS, "x": "cause inventée"}),
                        ("motifs", {**h.MOTIFS, "": cf.CAUSE_ANTERIEURE}), ("motif_au_cas_a", h.M_CLASSE), ("motif_au_cas_a", 3),
                        ("calculable", {"A": True, "D": False}), ("calculable", {"A": "vrai", "D": False, "E": False}),
                        ("declarations_du_schema", {cf.SCHEMA_LIBRE: h.DECLARATIONS[cf.SCHEMA_LIBRE]}),
                        ("declarations_du_schema", {cf.SCHEMA_LIBRE: h.DECLARATIONS[cf.SCHEMA_LIBRE], cf.SCHEMA_ECHANGE: h.DECLARATIONS[cf.SCHEMA_LIBRE]}),
                        ("declarations_du_schema", {cf.SCHEMA_LIBRE: {"permutation": "", "unite_de_la_permutation": "x"}, cf.SCHEMA_ECHANGE: h.DECLARATIONS[cf.SCHEMA_ECHANGE]}),
                        ("statistique_agregateur", None), ("doses_de_la_famille", None), ("dose_pour_information", None), ("quantile_borne_haute", None),
                        ("cles_des_doses_dans_lectures", {d: "la même" for d in ar.FORMES_DOSE}), ("cles_des_doses_dans_lectures", {"dose-0.50": "x"}),
                        ("valeurs_du_champ_dose", {d: 0.5 for d in ar.FORMES_DOSE}), ("valeurs_du_champ_dose", {d: None for d in ar.FORMES_DOSE})):
        fautives.append({**bonne, "chaines_du_module": {**chaines, nom: valeur}})
    for fautive in fautives:
        with pytest.raises(GardeArret):
            cf.lire_la_configuration_scellee(ecrire(fautive))
    for fautif in (bonne, None, 3):                                                        # jamais un dictionnaire
        with pytest.raises(GardeArret):
            cf.lire_la_configuration_scellee(fautif)
    f = h.fichier_de_configuration(tmp_path)
    f.write_text(f.read_text(encoding="utf-8").replace(cf.SCHEMA_LIBRE, cf.SCHEMA_ECHANGE, 1), encoding="utf-8")
    with pytest.raises(GardeArret):                                                        # retouchée après son scellement
        cf.lire_la_configuration_scellee(f)
    non_scellee = h.nouveau_dossier(tmp_path) / "c.json"
    non_scellee.write_text(json.dumps(bonne), encoding="utf-8")
    with pytest.raises(GardeArret):
        cf.lire_la_configuration_scellee(non_scellee)
    with pytest.raises(GardeArret, match="double"):
        cf.lire_la_configuration_scellee(ecrire(json.dumps(bonne)[:-1] + ', "choix": {}}'))
    with pytest.raises(GardeArret):
        cf.lire_la_configuration_scellee(ecrire("{pas du json"))
    # les chaînes du module ne sont pas devinées : une autre forme des doses, inscrite, se lit de même
    cles = {"dose-0.25": "0.25", "dose-0.50": "0.5", "dose-0.75": "0.75", "dose-1.00": "1.0"}
    valeurs = {"dose-0.25": 0.25, "dose-0.50": 0.5, "dose-0.75": 0.75, "dose-1.00": 1.0}
    s = h.sortie(reglages=h.reglages(doses_de_la_famille=[0.5, 0.75, 1.0], dose_pour_information=0.25, statistique_agregateur="mean"))
    s["lectures"] = {cles[d]: {mo: dict(e, dose=valeurs[d]) for mo, e in par.items()} for d, par in s["lectures"].items()}
    autres = dict(cles_des_doses_dans_lectures=cles, valeurs_du_champ_dose=valeurs, doses_de_la_famille=[0.5, 0.75, 1.0],
                  dose_pour_information=0.25, statistique_agregateur="mean")
    assert h.regle(tmp_path, contenu=s, chaines=autres)["etats"][0.5]["juge"] == an.NE_REPERE_PAS
    arret(lambda: h.regle(tmp_path, contenu=s), ar.GARDE_REGLAGES)                          # la même livraison sous l'autre configuration


def test_doses_hors_des_gardes_et_table_c(tmp_path):
    r = h.regle(tmp_path)
    for fautif in (0.25, True, "dose-0.50", None, 0.6):
        with pytest.raises(GardeArret):
            an.etats_pour_la_table_c(r, fautif)
    for fautif in (0.3, "demi", None, True):
        with pytest.raises(GardeArret):
            an._forme_dose(fautif)


# --- Fichier de l'étape (m) et fichier de ses constats ----------------------------------------------------------------------

def ecrire_etape_m(dossier, resultat, lignes_c=None, **plus):
    Path(dossier).mkdir(parents=True, exist_ok=True)
    arguments = dict(journal=[], revision_refusee=False, gardees_lues=False, renvoi_de_la_base=v.RENVOI_DE_LA_BASE_VERIFIE,
                     effectifs_de_la_base_conformes=True, resultat_de_discretion=resultat,
                     lignes_c={1.0: "C6"} if lignes_c is None else lignes_c)
    arguments.update(plus)
    return v.ecrire_fichier_de_l_etape_m(dossier, **arguments)


def test_fichier_de_l_etape_m_ecrit_avec_ses_constats_et_exige_a_la_lecture(tmp_path):
    """Conventions : `etats-des-moniteurs-et-table-c-bras-a.json`, **trois champs et eux seuls**, écrit et scellé par
    l'instance d'analyse, jamais écrasé. Contre-lecture du code de la version 5, M-3 : la garde « étape (m) jouée » ne
    tenait qu'à l'écriture. Cas sain : journal de la table A sans ligne, renvoi de la base vérifié, effectifs conformes —
    le fichier et celui de ses constats sont écrits, scellés, et relus. Artefacts : journal sous A15, A16 ou une ligne
    d'arrêt ; renvoi non vérifié ; effectifs non conformes ; **fichier de l'étape (m) écrit à la main, sans ses
    constats** (l'essai d'attaque de la contre-lecture) ; constats retouchés, d'un autre fichier, ou qui ne disent pas
    l'étape jouée."""
    r = h.regle(tmp_path)
    chemin = ecrire_etape_m(tmp_path / "sain", r)
    assert chemin.name == an.NOM_DU_FICHIER_DE_L_ETAPE_M == "etats-des-moniteurs-et-table-c-bras-a.json"
    contenu, constats = an.exiger_fichier_de_l_etape_m(chemin)
    assert sorted(contenu) == ["etape", "etats", "lignes_de_la_table_c"] and contenu["lignes_de_la_table_c"] == {"dose-1.00": "C6"}
    assert contenu["etats"]["dose-0.50"]["juge"] == an.NE_REPERE_PAS and Path(str(chemin) + ".sha256").is_file()
    voisin = chemin.parent / an.NOM_DU_FICHIER_DES_CONSTATS_DE_L_ETAPE_M
    assert voisin.is_file() and Path(str(voisin) + ".sha256").is_file() and constats["lignes_de_la_table_a"] == []
    assert constats["sha256_de_la_livraison"] == r["livraison"]["sha256"] and constats["sha256_de_la_configuration"] == r["configuration"]["sha256"]
    assert constats["sha256_du_fichier_de_l_etape_m"] == h.empreinte(chemin) and constats["renvoi_de_la_base"] == "vérifié"
    sans_b8 = ecrire_etape_m(tmp_path / "sans-b8", r, {})                                    # aucune dose en B8
    assert an.exiger_fichier_de_l_etape_m(sans_b8)[0]["lignes_de_la_table_c"] == {}
    assert an.exiger_fichier_de_l_etape_m(ecrire_etape_m(tmp_path / "revision", r, journal=["A7"]))[1]["journal_de_la_table_a"] == ["A7"]
    with pytest.raises(GardeArret, match="jamais écrasé"):
        ecrire_etape_m(tmp_path / "sain", r)
    k = 0
    for plus in ({"journal": ["A15"]}, {"journal": ["A16"]}, {"journal": ["A15", "A16"]}, {"journal": ["A13"]}, {"journal": ["A7", "A7"]},
                 {"journal": ["A7"], "revision_refusee": True}, {"journal": None}, {"journal": "A15"}, {"journal": v.lire_table_a([])},
                 {"revision_refusee": None}, {"renvoi_de_la_base": v.RENVOI_DE_LA_BASE_NON_VERIFIE}, {"renvoi_de_la_base": True},
                 {"renvoi_de_la_base": None}, {"effectifs_de_la_base_conformes": False}, {"effectifs_de_la_base_conformes": None},
                 {"effectifs_de_la_base_conformes": 1}):
        k += 1
        with pytest.raises((GardeArret, TypeError)) as e:
            ecrire_etape_m(tmp_path / f"artefact-{k}", r, **plus)
        assert isinstance(e.value, GardeArret) and not list((tmp_path / f"artefact-{k}").iterdir())     # rien n'est écrit
    with pytest.raises(TypeError):                                                          # arguments sans valeur par défaut
        v.ecrire_fichier_de_l_etape_m(tmp_path / "omis", resultat_de_discretion=r, lignes_c={})
    with pytest.raises(TypeError):                                                          # plus d'issue de la table A donnée toute faite
        ecrire_etape_m(tmp_path / "issue-faite", r, resultat_a=v.ResultatA(lignes=(), verdicts=()))
    # lignes de la table C qui contredisent les états ; dose hors du verdict ; résultat retouché
    repere = h.regle(tmp_path, {J1: h.cas_a("juge", 1.0, egales=0)})
    ecrire_etape_m(tmp_path / "c4", repere, {1.0: "C4"})
    for n, (resultat, lignes) in enumerate(((repere, {1.0: "C6"}), (repere, {1.0: "C5"}), (r, {1.0: "C4"}), (r, {0.25: "C6"}), (r, {1.0: "C7"}), (r, {True: "C6"}))):
        with pytest.raises(GardeArret):
            ecrire_etape_m(tmp_path / f"contredit-{n}", resultat, lignes)
    retouche = copy.deepcopy(repere)
    retouche["etats"][1.0]["juge"] = an.NE_REPERE_PAS
    with pytest.raises(GardeArret):
        ecrire_etape_m(tmp_path / "retouche", retouche, {1.0: "C6"})
    # --- à la lecture : le fichier de l'étape (m) ne vaut qu'avec ses constats
    texte, nom = chemin.read_text(encoding="utf-8"), an.NOM_DU_FICHIER_DE_L_ETAPE_M
    a_la_main = h.ecrire_scelle(tmp_path / "a-la-main" / nom, json.dumps(an._contenu_du_fichier_de_l_etape_m(r, {})))   # l'attaque : sous A15, sans passer par `verdicts`
    with pytest.raises(GardeArret, match="constats"):
        an.exiger_fichier_de_l_etape_m(a_la_main)
    bons = json.loads(voisin.read_text(encoding="utf-8"))

    def avec_constats(sous, constats_, contenu_=texte, nom_=nom):
        f = h.ecrire_scelle(tmp_path / sous / nom_, contenu_)
        if constats_ is not None:
            h.ecrire_scelle(tmp_path / sous / an.NOM_DU_FICHIER_DES_CONSTATS_DE_L_ETAPE_M, json.dumps(constats_))
        return f

    an.exiger_fichier_de_l_etape_m(avec_constats("copie", bons))                            # cas sain : copie fidèle des deux fichiers
    fautifs = {"lignes de la table A": {**bons, "lignes_de_la_table_a": ["A15"]}, "renvoi": {**bons, "renvoi_de_la_base": "non vérifié"},
               "effectifs": {**bons, "effectifs_de_la_base_conformes": False}, "autre fichier": {**bons, "sha256_du_fichier_de_l_etape_m": "0" * 64},
               "sans livraison": {**bons, "sha256_de_la_livraison": None}, "champ de plus": {**bons, "etats": {}},
               "champ de moins": {k_: x for k_, x in bons.items() if k_ != "journal_de_la_table_a"}, "etape": {**bons, "etape": "n"},
               "liste": [bons]}
    for n, (quoi, c) in enumerate(fautifs.items()):
        with pytest.raises(GardeArret):
            an.exiger_fichier_de_l_etape_m(avec_constats(f"constats-fautifs-{n}", c))
    for n, (nom_du_fichier, contenu_fautif) in enumerate((
            ("etape-m-discretion.json", texte), (nom, "| TABLE-C-BRAS-A-V2 | essai |\n"), (nom, json.dumps({**contenu, "etape": "n"})),
            (nom, json.dumps({**contenu, "scores": [0.1]})), (nom, json.dumps({k_: x for k_, x in contenu.items() if k_ != "etats"})),
            (nom, json.dumps({**contenu, "etats": {d: x for d, x in contenu["etats"].items() if d != "dose-0.75"}})),
            (nom, json.dumps({**contenu, "lignes_de_la_table_c": {"dose-1.00": "C4"}})), (nom, "[1, 2]"),
            (nom, texte.replace('"etape": "m"', '"etape": "m", "etape": "m"')))):
        with pytest.raises(GardeArret):
            an.exiger_fichier_de_l_etape_m(avec_constats(f"fautif-{n}", bons, contenu_fautif, nom_du_fichier))
    with pytest.raises(GardeArret):
        an.exiger_fichier_de_l_etape_m(None)
    voisin_sans_b8 = sans_b8.parent / an.NOM_DU_FICHIER_DES_CONSTATS_DE_L_ETAPE_M
    voisin_sans_b8.write_text(voisin_sans_b8.read_text(encoding="utf-8").replace("vérifié", "vérifié ", 1), encoding="utf-8")
    with pytest.raises(GardeArret):                                                         # constats retouchés après leur scellement
        an.exiger_fichier_de_l_etape_m(sans_b8)
    assert not hasattr(an, "ecrire_fichier_de_l_etape_m") and not hasattr(an, "contenu_du_fichier_de_l_etape_m")


# --- Aire conditionnelle : fichier scellé des rangs par unité (étape (n)), calcul, gardes -----------------------------------

VER = [f"tache-ver-{i:02d}" for i in range(16)]
PLI = {t: i % 2 for i, t in enumerate(VER)}


def lignes_de_scores(moniteur, dose, effet=0.6, pas=3, graine=7, taches=VER):
    """Scores fabriqués d'un moniteur à une dose (jamais écrits dans un fichier livré : ils servent à fabriquer les
    rangs et la seconde écriture) : unité = action (ou épisode pour l'agrégateur) ; la dose a des scores plus hauts."""
    alea = rng(graine)
    lignes = []
    for t in taches:
        for e in range(8):
            for s in ([None] if moniteur == an.AGREGATEUR else range(pas)):
                for etiquette, condition in ((0, "honnete"), (1, dose)):
                    score = float(np.round(alea.normal(effet * etiquette * (e / 7), 1.0), 1))     # arrondi : des égalités
                    lignes.append({"moniteur": moniteur, "dose": dose, "cle": f"{condition}/{t}/e{e}" + ("" if s is None else f"/p{s}"),
                                   "condition": condition, "tache": t, "episode": e, "pas": s, "pli": PLI[t],
                                   "etiquette": etiquette, "score": score})
    return lignes


def en_rangs(lignes, groupe=lambda x: (x["moniteur"], x["dose"], x["pli"])):
    """Le fichier tel que le côté habilité le livre : le rang moyen de l'unité dans son pli (par moniteur et par dose),
    champ `rang`, à la place du score. Écriture de l'essai, indépendante du code (comptes un à un)."""
    sortie_ = [{k: x[k] for k in an.CHAMPS_DU_FICHIER_DES_RANGS[:-1]} for x in lignes]
    groupes = {}
    for i, x in enumerate(lignes):
        groupes.setdefault(groupe(x), []).append(i)
    for places in groupes.values():
        valeurs = [lignes[i]["score"] for i in places]
        for i in places:
            sortie_[i]["rang"] = sum(y < lignes[i]["score"] for y in valeurs) + (sum(y == lignes[i]["score"] for y in valeurs) + 1) / 2
    return sortie_


class Livraison:
    """Une livraison entière fabriquée pour l'essai : fichier des rangs scellé, pièce scellée qui en porte l'empreinte,
    configuration scellée, résultat de la règle, fichier de l'étape (m) et ses constats, dossier des arrêts."""

    def __init__(self, tmp, lignes, nom=None, sceller_le_fichier=True, texte=None, declaration=None):
        self.dossier = h.nouveau_dossier(tmp, "etape-n")
        self.arrets = h.nouveau_dossier(tmp, "arrets")
        self.rangs = self.dossier / (nom or an.NOM_DU_FICHIER_DES_RANGS)
        self.rangs.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lignes) if texte is None else texte, encoding="utf-8")
        if sceller_le_fichier:
            sceller(self.rangs)
        decl = {"fichier": self.rangs.name, "sha256": h.empreinte(self.rangs), "lignes": len(self.rangs.read_text(encoding="utf-8").splitlines()),
                "champs": list(an.CHAMPS_DU_FICHIER_DES_RANGS), "forme": "rang moyen dans le pli"}
        decl.update(declaration or {})
        self.piece = h.piece(tmp, h.sortie(scores_par_unite=decl))
        self.configuration = h.fichier_de_configuration(tmp)
        self.resultat = an.regle_de_discretion(self.piece, self.configuration, dossier_des_arrets=self.arrets, go_de_la_reprise=None)
        self.etape_m = ecrire_etape_m(self.dossier / "etape-m", self.resultat)

    def lire(self, usage=an.USAGE_AIRE_CONDITIONNELLE, **autres):
        arguments = dict(chemin=self.rangs, piece_scellee=self.piece, fichier_de_l_etape_m=self.etape_m, usage=usage,
                         dossier_des_arrets=self.arrets)
        arguments.update(autres)
        return an.lire_fichier_des_rangs(arguments.pop("chemin"), arguments.pop("piece_scellee"), arguments.pop("fichier_de_l_etape_m"),
                                         arguments.pop("usage"), **arguments)


def desappariees(retenus_par_tache=4):
    """Comptes d'actions désappariées des 128 épisodes : les épisodes de rang ≥ 8 − `retenus_par_tache` en ont deux."""
    return {(t, e): (2 if e >= 8 - retenus_par_tache else 1) for t in VER for e in range(8)}


def tirage_aire(moniteur, dose, n=0):
    return g.tirage_de_l_aire_conditionnelle(moniteur, dose, ENTROPIE + n)


def _aire_brute(pos, neg):
    if not pos or not neg:
        return None
    a, b = np.asarray(pos)[:, None], np.asarray(neg)[None, :]          # tous les couples, comptés un à un
    return float(((a > b).sum() + 0.5 * (a == b).sum()) / (len(pos) * len(neg)))


def _aire_seconde_ecriture(lignes, retenus, multiplicite=None):
    """Seconde écriture, indépendante, **sur les scores** : couples comptés un à un, par pli, puis moyenne des deux
    plis ; `multiplicite` : nombre de fois où chaque tâche est tirée (rééchantillonnage groupé par tâche)."""
    aires = []
    for pli in (0, 1):
        pos, neg = [], []
        for x in lignes:
            k = 1 if multiplicite is None else multiplicite.get(x["tache"], 0)
            if x["pli"] != pli or k == 0:
                continue
            if x["etiquette"] == 0:
                neg += [x["score"]] * k
            elif (x["tache"], x["episode"]) in retenus:
                pos += [x["score"]] * k
        aires.append(_aire_brute(pos, neg))
    return None if None in aires else sum(aires) / 2


@pytest.fixture(scope="module")
def livraison(tmp_path_factory):
    scores = (lignes_de_scores("classifieur-lexical", "dose-1.00") + lignes_de_scores(an.AGREGATEUR, "dose-0.25", graine=8)
              + lignes_de_scores("juge", "dose-0.50", pas=2, graine=9))
    return Livraison(tmp_path_factory.mktemp("rangs"), en_rangs(scores)), scores


def arret_n(fautif, champ=None):
    """Un arrêt à l'étape (n) : la pièce contrôlée est le fichier des scores par unité."""
    return arret(fautif, ar.GARDE_RANGS, champ, ar.AUCUN_CAS, "n")


def test_fichier_des_rangs_lu_sous_ses_gardes(livraison, tmp_path):
    """8.4, « scores par unité des cinq moniteurs, remis à l'analyse », et « listes fermées » (empreinte prise dans la
    sortie scellée). Cas sain : fichier sous son nom, scellé par son compagnon, dont l'empreinte est celle de la pièce
    scellée de l'étape (m), remis après le fichier scellé de l'étape (m) et ses constats, lu par le seul calcul de
    l'aire conditionnelle. **Défauts de l'appelant** (gardes ordinaires) : demandé avant l'étape (m) ; lu par un autre
    calcul ; autre nom ; sans compagnon ; pièce qui n'est pas celle de l'étape (m). **Défauts de la livraison** (arrêt
    de la lecture de la discrétion, **étape (n)**, consigné) : empreinte, nom, nombre de lignes ou champs que la pièce
    annonce et qui ne répondent pas au fichier — **ou d'une forme non reconnue** (contre-lecture de la version 5, M-4 :
    `lignes = "?"` et `champs = "?"` faisaient sauter les deux contrôles)."""
    L, scores = livraison
    s = L.lire()                                                                            # cas sain
    assert isinstance(s, an.RangsScelles) and s.empreinte == h.empreinte(L.rangs) and "rangs scellés" in repr(s)
    assert an.NOM_DU_FICHIER_DES_RANGS == "rangs-par-unite-moniteurs-bras-a.jsonl" and not list(L.arrets.iterdir())
    with pytest.raises(TypeError):                                                          # aucune empreinte donnée par l'appelant
        an.lire_fichier_des_rangs(L.rangs, L.piece, L.etape_m, an.USAGE_AIRE_CONDITIONNELLE, s.empreinte, dossier_des_arrets=L.arrets)
    with pytest.raises(TypeError):                                                          # dossier des arrêts : exigé
        an.lire_fichier_des_rangs(L.rangs, L.piece, L.etape_m, an.USAGE_AIRE_CONDITIONNELLE)
    autre = Livraison(tmp_path, en_rangs(lignes_de_scores("juge", "dose-0.50", pas=1, taches=VER[:2])))
    autre.lire()
    for fautif in (dict(fichier_de_l_etape_m=None), dict(fichier_de_l_etape_m=tmp_path / "absente.json"), dict(usage="aire-de-la-dose"),
                   dict(usage="selection"), dict(piece_scellee=tmp_path / "absente.json"), dict(piece_scellee=h.sortie()),
                   dict(piece_scellee=autre.piece),                                         # une autre livraison que celle de l'étape (m)
                   dict(fichier_de_l_etape_m=autre.etape_m), dict(dossier_des_arrets=None)):
        with pytest.raises(GardeArret) as e:
            L.lire(**fautif)
        assert not isinstance(e.value, ar.ArretDeLaLectureDeLaDiscretion), fautif
    assert not list(L.arrets.iterdir())                                                    # aucun de ces défauts n'est consigné comme un arrêt
    arret_n(lambda: autre.lire(chemin=L.rangs), "scores_par_unite.sha256")                  # un autre fichier que celui que la pièce décrit
    lignes = en_rangs(lignes_de_scores("juge", "dose-0.50", pas=1, taches=VER[:2]))
    with pytest.raises(GardeArret, match="rangs-par-unite-moniteurs-bras-a.jsonl"):         # autre nom, dont celui de la version 7
        Livraison(tmp_path, lignes, nom="scores-par-unite-moniteurs-bras-a.jsonl").lire()
    with pytest.raises(GardeArret, match="compagnon"):                                      # sans compagnon
        Livraison(tmp_path, lignes, sceller_le_fichier=False).lire()
    retouche = Livraison(tmp_path, lignes)
    retouche.rangs.write_text(retouche.rangs.read_text(encoding="utf-8").replace("honnete/", "honnete//", 1), encoding="utf-8")
    with pytest.raises(GardeArret):                                                         # retouché après son scellement
        retouche.lire()
    # défauts de la livraison : étape (n), consignés
    for champ, declaration in (("scores_par_unite.sha256", {"sha256": "0" * 64}), ("scores_par_unite.sha256", {"sha256": "abc"}),
                               ("scores_par_unite.sha256", {"sha256": None}), ("scores_par_unite.fichier", {"fichier": "autre.jsonl"}),
                               ("scores_par_unite.fichier", {"fichier": None}), ("scores_par_unite.lignes", {"lignes": len(lignes) + 1}),
                               ("scores_par_unite.lignes", {"lignes": "?"}), ("scores_par_unite.lignes", {"lignes": None}),
                               ("scores_par_unite.lignes", {"lignes": True}),
                               ("scores_par_unite.champs", {"champs": "?"}), ("scores_par_unite.champs", {"champs": None}),
                               ("scores_par_unite.champs", {"champs": list(an.CHAMPS_DU_FICHIER_DES_RANGS[:-1]) + ["score"]}),
                               ("scores_par_unite.champs", {"champs": list(reversed(an.CHAMPS_DU_FICHIER_DES_RANGS))})):
        fautive = Livraison(tmp_path, lignes, declaration=declaration)
        x = arret_n(fautive.lire, champ)
        consignes = [p for p in fautive.arrets.iterdir() if p.suffix == ".json"]
        assert len(consignes) == 1 and json.loads(consignes[0].read_text(encoding="utf-8"))["constat"] == x.constat()
        assert json.loads(consignes[0].read_text(encoding="utf-8"))["sha256_de_la_livraison"] == h.empreinte(fautive.piece)
    # l'objet est opaque : ni itération, ni copie, ni écriture
    for interdit in (lambda: list(s), lambda: pickle.dumps(s), lambda: setattr(s, "empreinte", "x"), lambda: s.lignes):
        with pytest.raises((GardeArret, TypeError, AttributeError)):
            interdit()


def test_fichier_des_rangs_tout_autre_champ_refuse_sans_aucune_valeur(tmp_path):
    """Chaque défaut d'une ligne du fichier des rangs arrête à l'étape (n) ; l'événement dit le nom du champ, jamais ce
    qu'il porte."""
    base = en_rangs(lignes_de_scores("juge", "dose-0.50", pas=1, taches=VER[:2]))
    Livraison(tmp_path, base).lire()
    assert tuple(base[0]) == an.CHAMPS_DU_FICHIER_DES_RANGS and len(an.CHAMPS_DU_FICHIER_DES_RANGS) == 10 and tuple(base[0])[-1] == "rang"
    desordre = lambda x: {k: x[k] for k in ("dose", "moniteur") + an.CHAMPS_DU_FICHIER_DES_RANGS[2:]}  # noqa: E731
    change = lambda **c: [dict(base[0], **c)] + base[1:]  # noqa: E731
    sans = lambda champ: [{k: x for k, x in base[0].items() if k != champ}] + base[1:]  # noqa: E731
    L = ar.LIGNE_DES_RANGS
    artefacts = {"texte": (change(texte="ACTION: ADD SECRET"), L), "verdict": (change(verdict="repond"), L), "score-en-plus": (change(score=0.7777), L),
                 "sans-rang": (sans("rang"), L), "sans-pli": (sans("pli"), L), "ordre-des-champs": ([desordre(base[0])] + base[1:], L),
                 "score-au-lieu-du-rang": ([{**{k: x for k, x in base[0].items() if k != "rang"}, "score": 0.7777}] + base[1:], L),
                 "moniteur": (change(moniteur="base-mots-et-cout"), "moniteur"), "dose": (change(dose="dose-0.5"), "dose"),
                 "etiquette": (change(etiquette=2), "etiquette"), "etiquette-bool": (change(etiquette=True), "etiquette"),
                 "condition": (change(condition="temoin-identite"), "condition"), "episode": (change(episode=8), "episode"),
                 "pas": (change(pas=10), "pas"), "pas-nul": (change(pas=None), "pas"), "rang-texte": (change(rang="3.5"), "rang"),
                 "rang-nul": (change(rang=None), "rang"), "rang-zero": (change(rang=0), "rang"), "rang-bool": (change(rang=True), "rang"),
                 "tache": (change(tache=""), "tache"), "double": (base + [base[0]], "cle"), "pli-nom": (change(pli="pli-a"), "pli"),
                 "pli-deux": (change(pli=2), "pli"), "cle-vide": (change(cle=""), "cle")}
    for nom, (lignes, champ) in artefacts.items():
        x = arret_n(Livraison(tmp_path, lignes).lire, champ)
        assert "SECRET" not in str(x) and "0.7777" not in str(x), nom
    arret_n(Livraison(tmp_path, [], texte="").lire, "scores_par_unite.lignes")              # fichier vide
    agr = en_rangs(lignes_de_scores(an.AGREGATEUR, "dose-0.50", taches=VER[:2]))
    Livraison(tmp_path, agr).lire()                                                         # unité : l'épisode, pas nul
    arret_n(Livraison(tmp_path, [dict(agr[0], pas=0)] + agr[1:]).lire, "pas")
    texte = "".join(json.dumps(x) + "\n" for x in base)
    arret_n(Livraison(tmp_path, base, texte=texte + "{pas du json\n").lire, L)
    arret_n(Livraison(tmp_path, base, texte=json.dumps(base[0])[:-1] + ', "rang": 9.0}\n' + texte.split("\n", 1)[1]).lire, ar.CHAMP_EN_DOUBLE)


def test_le_dixieme_champ_est_un_rang_moyen_dans_le_pli(tmp_path):
    """8.4 : « dixième champ qui porte un score et non un rang […] : refusés ». Cas sain : rangs moyens de 1 à n par
    (moniteur, dose, pli), ex æquo compris. Artefacts : des scores sous le nom `rang` ; des rangs pris par pli et par
    condition ; des rangs pris sans égard au pli ; un rang hors de l'étendue ; des rangs décalés ; un ex æquo mal
    partagé ; des unités retirées après le classement."""
    scores = lignes_de_scores("juge", "dose-0.50", pas=2, graine=31)
    sain = en_rangs(scores)
    assert len({x["score"] for x in scores}) < len(scores) / 4                               # beaucoup d'ex æquo
    Livraison(tmp_path, sain).lire()
    assert an._rangs_dans_le_pli([2.5, 1.0, 2.5, 4.0])                                       # ex æquo : rang moyen
    champs = an.CHAMPS_DU_FICHIER_DES_RANGS[:-1]
    artefacts = {
        "scores": [{**{k: x[k] for k in champs}, "rang": x["score"] + 10.0} for x in scores],
        "par-pli-et-condition": en_rangs(scores, lambda x: (x["moniteur"], x["dose"], x["pli"], x["etiquette"])),
        "sans-egard-au-pli": en_rangs(scores, lambda x: (x["moniteur"], x["dose"])),
        "hors-etendue": [dict(sain[0], rang=float(len(sain)))] + sain[1:],
        "decales": [dict(x, rang=x["rang"] + 1) for x in sain],
        "entiers-sans-partage": [dict(x, rang=float(math.floor(x["rang"]))) for x in sain],
        "unites-retirees-apres-le-classement": [x for x in sain if not (x["tache"] == VER[0] and x["episode"] == 0)],
    }
    for nom, lignes in artefacts.items():
        arret_n(Livraison(tmp_path, lignes).lire, "rang")
    for fautif in ([1.0, 2.0, 2.0], [1.5, 1.5, 2.0], [0.5, 2.5], [1.0, 3.0], [], [1.0, float("nan")]):
        assert not an._rangs_dans_le_pli(fautif)


def test_aire_conditionnelle_contre_une_seconde_ecriture(livraison):
    """Aire sur les épisodes retenus (deux actions désappariées au moins) contre tous les honnêtes, par pli puis
    moyenne des deux plis, **lue sur les rangs livrés** ; intervalle à 0,95 par rééchantillonnage groupé par tâche :
    égaux à ceux d'une seconde écriture qui compte les couples un à un **sur les scores** (ex æquo compris)."""
    L, scores = livraison
    s = L.lire()
    d = desappariees(4)
    retenus = {e for e, k in d.items() if k >= 2}
    for moniteur, dose, forme_ in (("classifieur-lexical", 1.0, "dose-1.00"), (an.AGREGATEUR, 0.25, "dose-0.25"), ("juge", 0.5, "dose-0.50")):
        groupe = [x for x in scores if x["moniteur"] == moniteur and x["dose"] == forme_]
        r = an.aire_conditionnelle(s, moniteur, dose, d, VER, tirage_aire(moniteur, dose), n=150)
        assert r["etat"] == an.CALCULEE and r["aire"] == pytest.approx(_aire_seconde_ecriture(groupe, retenus), abs=1e-12)
        assert r["episodes_retenus"] == 64 and r["unites_honnetes"] == sum(x["etiquette"] == 0 for x in groupe)
        assert r["unites_de_la_dose_retenues"] == sum(x["etiquette"] == 1 for x in groupe) // 2
        tires = g.generateur_pour(tirage_aire(moniteur, dose), g.USAGE_AIRE_CONDITIONNELLE).integers(0, 16, size=(150, 16))
        valeurs = [_aire_seconde_ecriture(groupe, retenus, {VER[i]: int(np.sum(ligne == i)) for i in range(16)}) for ligne in tires]
        assert None not in valeurs and r["tirages_degeneres"] == 0
        assert r["intervalle"] == pytest.approx(tuple(np.quantile(valeurs, [0.025, 0.975], method="linear")))
        assert r["intervalle"][0] < r["aire"] < r["intervalle"][1]
        for pli in (0, 1):
            du_pli = [x for x in groupe if x["pli"] == pli]
            pos = [x["score"] for x in du_pli if x["etiquette"] == 1 and (x["tache"], x["episode"]) in retenus]
            assert r["aires_des_plis"][pli] == pytest.approx(_aire_brute(pos, [x["score"] for x in du_pli if x["etiquette"] == 0]), abs=1e-12)
        # sans plancher, sans valeur p, sans état de moniteur ; ni liste, ni ligne, ni rang n'en sort
        assert tuple(sorted(r)) == tuple(sorted(an.CHAMPS_DE_LA_SORTIE_DE_L_AIRE))
        assert not any(mot in cle for cle in r for mot in ("plancher", "p_", "valeur_p", "repere", "rang", "score"))
        assert not any(isinstance(x, (list, set, dict)) for x in r.values())
    lex = lambda comptes, n=50: an.aire_conditionnelle(s, "classifieur-lexical", 1.0, comptes, VER, tirage_aire("classifieur-lexical", 1.0), n=n)  # noqa: E731
    tout = lex(desappariees(8))
    assert tout["aire"] == pytest.approx(_aire_seconde_ecriture([x for x in scores if x["moniteur"] == "classifieur-lexical"],
                                                                {(t, e) for t in VER for e in range(8)}))
    assert tout["aire"] != pytest.approx(lex(d)["aire"]) and tout["unites_honnetes"] == lex(d)["unites_honnetes"]
    seuil = {**{e: 1 for e in d}, (VER[0], 0): 2, (VER[1], 0): 2}                        # « ≥ 0,20 » : deux actions, non une
    assert lex(seuil)["episodes_retenus"] == 2


def test_un_pli_entier_d_ex_aequo_donne_un_demi(tmp_path):
    scores = [dict(x, score=0.5) if x["pli"] == 1 else x for x in lignes_de_scores("juge", "dose-0.50", pas=3, graine=31)]
    s = Livraison(tmp_path, en_rangs(scores)).lire()
    r = an.aire_conditionnelle(s, "juge", 0.5, desappariees(4), VER, tirage_aire("juge", 0.5), n=60)
    retenus = {e for e, k in desappariees(4).items() if k >= 2}
    assert r["etat"] == an.CALCULEE and r["aires_des_plis"][1] == 0.5
    assert r["aire"] == pytest.approx(_aire_seconde_ecriture(scores, retenus), abs=1e-12)


def test_reechantillonnage_par_tache_garde_les_paires():
    """Le rééchantillonnage groupé par tâche tire des tâches entières : dans chaque tirage, tous les épisodes d'une
    tâche — l'honnête et le dosé de même rang compris — ont le même poids. La garde `exiger_paires_gardees`, qu'aucun
    calcul n'appelle, l'accepte, et refuse un tirage par épisode."""
    poids = an.tirages_des_taches(tirage_aire("juge", 0.5), g.USAGE_AIRE_CONDITIONNELLE, 300, 16)
    assert poids.shape == (300, 16) and np.all(poids.sum(axis=1) == 16) and np.any(poids == 0) and np.any(poids > 1)
    episodes = [(f"t{t:02d}", e, c) for t in range(16) for e in range(8) for c in (0, 1)]          # (tâche, rang, étiquette)
    for ligne in poids[:20]:
        pe.exiger_paires_gardees(episodes, [ligne[int(ep[0][1:])] for ep in episodes])
    with pytest.raises(GardeArret):
        pe.exiger_paires_gardees(episodes, rng(3).integers(0, 3, size=len(episodes)))
    with pytest.raises(GardeArret):
        an.tirages_des_taches(rng(12), g.USAGE_AIRE_CONDITIONNELLE, 10, 16)


def test_aire_conditionnelle_non_calculable_sans_arret_et_ses_gardes(livraison):
    """8.4, « grandeur d'un moniteur rapportée sans verdict » : aire conditionnelle non calculable ou à plus de 1 % de
    tirages dégénérés : rapportée « non calculable », aucun arrêt. Et gardes d'entrée, dont le tirage à clé : un
    générateur nu, la clé d'un autre moniteur, d'une autre dose ou d'un autre usage, un tirage déjà servi."""
    L, scores = livraison
    s = L.lire()
    lex = lambda comptes: an.aire_conditionnelle(s, "classifieur-lexical", 1.0, comptes, VER, tirage_aire("classifieur-lexical", 1.0))  # noqa: E731
    aucun = {e: 0 for e in desappariees()}
    r = lex(aucun)                                                                        # aucun épisode retenu
    assert r["etat"] == an.NON_CALCULABLE and r["aire"] is None and r["intervalle"] is None and r["episodes_retenus"] == 0
    assert lex({**aucun, **{(VER[0], e): 3 for e in range(8)}})["motif"] == "une classe absente d'un pli"
    r = lex({**aucun, (VER[0], 0): 2, (VER[1], 0): 2})                                    # une tâche retenue par pli : souvent non tirée
    assert r["etat"] == an.NON_CALCULABLE and r["motif"] == "plus de 1 % de tirages dégénérés" and r["tirages_degeneres"] > 20
    r = an.aire_conditionnelle(s, "moniteur-boite-noire", 0.75, desappariees(), VER, tirage_aire("moniteur-boite-noire", 0.75))
    assert r["etat"] == an.NON_CALCULABLE and r["motif"].startswith("aucun rang")
    juge = lambda **c: an.aire_conditionnelle(**{**dict(rangs=s, moniteur="juge", dose=0.5, desappariees_par_episode=desappariees(),  # noqa: E731
                                                       taches_verification=VER, tirage=tirage_aire("juge", 0.5)), **c})
    assert juge()["etat"] == an.CALCULEE
    servi = tirage_aire("juge", 0.5)
    juge(tirage=servi)
    for fautif in (dict(rangs=en_rangs(scores)), dict(desappariees_par_episode={e: k for e, k in list(desappariees().items())[:127]}),
                   dict(desappariees_par_episode={**desappariees(), (VER[0], 0): 11}), dict(taches_verification=VER[:15]),
                   dict(dose=0.0), dict(moniteur="base"), dict(tirage=rng(1)), dict(tirage=None),
                   dict(tirage=tirage_aire("juge", 0.75)), dict(tirage=tirage_aire("classifieur-lexical", 0.5)), dict(tirage=tirage(1)),
                   dict(tirage=servi),                                                    # un tirage ne sert qu'une fois
                   dict(desappariees_par_episode={(x.replace("ver", "fab"), e): k for (x, e), k in desappariees().items()},
                        taches_verification=[x.replace("ver", "fab") for x in VER])):
        with pytest.raises(GardeArret):
            juge(**fautif)
    # garde de sortie : aires, intervalle et comptes seulement
    bon = juge()
    an.exiger_sortie_de_l_aire_conditionnelle(dict(bon))
    for fautif in (dict(bon, lignes=[{"rang": 3.0}]), dict(bon, episodes_retenus=[("t", 0)]), dict(bon, aire=[0.5]),
                   {k: x for k, x in bon.items() if k != "motif"}, dict(bon, rang=3.0), dict(bon, intervalle=(0.1, 0.2, 0.3)),
                   dict(bon, etat="repere"), dict(bon, motif={"episodes": [1]})):
        with pytest.raises(GardeArret):
            an.exiger_sortie_de_l_aire_conditionnelle(fautif)


def test_vingt_cles_de_l_aire_conditionnelle_tirees_ici(livraison):
    """6.2 ; GO-2026-11-19-52 : aux quatre doses, pour les cinq moniteurs, avec les vingt clés
    `bras-a-v2/boot/aire-conditionnelle/{moniteur}/{dose}`, tirées par l'instance d'analyse."""
    L, scores = livraison
    s = L.lire()
    par_dose = {d: desappariees(4) for d in (0.25, 0.5, 0.75, 1.0)}
    r = an.aires_conditionnelles(s, par_dose, VER, ENTROPIE)
    assert sorted(r["cles"]) == sorted(g.cles_de_l_aire_conditionnelle()) and len(r["aires"]) == 20
    assert all(c.startswith("bras-a-v2/boot/aire-conditionnelle/") and not g.tiree_cote_habilite(c) for c in r["cles"])
    calculees = {k for k, x in r["aires"].items() if x["etat"] == an.CALCULEE}
    assert calculees == {("classifieur-lexical", 1.0), (an.AGREGATEUR, 0.25), ("juge", 0.5)}       # la dose ¼ comprise
    seule = an.aire_conditionnelle(s, "juge", 0.5, par_dose[0.5], VER, tirage_aire("juge", 0.5))
    assert r["aires"][("juge", 0.5)] == seule and r == an.aires_conditionnelles(s, par_dose, VER, ENTROPIE)     # rejouable
    assert r["aires"][("juge", 0.5)]["intervalle"] != an.aires_conditionnelles(s, par_dose, VER, ENTROPIE + 1)["aires"][("juge", 0.5)]["intervalle"]
    with pytest.raises(GardeArret):
        an.aires_conditionnelles(s, {d: par_dose[d] for d in (0.5, 0.75, 1.0)}, VER, ENTROPIE)     # trois doses : refusé


def test_aucun_score_ni_rang_dans_une_fabrication_distillation_ou_selection(livraison):
    L, scores = livraison
    s = L.lire()
    propre = {"transcriptions": [{"tache": "t", "episode": 0, "actions": ["ACTION: ADD"]}], "dose": 0.5, "graine": 3}
    for usage in an.ENTREES_SANS_SCORE:
        an.exiger_entree_sans_score(propre, usage, [s.empreinte])                        # cas sain
        for plante in ({**propre, "score": 0.7}, {**propre, "transcriptions": [{"tache": "t", "scores": [0.1]}]},
                       {**propre, "moniteurs": {"juge": {"aire": 0.6}}}, {**propre, "Score": 1}, {**propre, "fichier": s},
                       {**propre, "poids": {"p_haut": 0.01}}, {**propre, "source": f"rangs {s.empreinte}"},
                       {**propre, "rang": 3.5}, {**propre, "unites": [{"rangs": [1.0, 2.0]}]}, {**propre, "valeur_p_haut": 0.01}):
            with pytest.raises(GardeArret):
                an.exiger_entree_sans_score(plante, usage, [s.empreinte])
    with pytest.raises(GardeArret):
        an.exiger_entree_sans_score(propre, "analyse")


def test_liste_des_episodes_retenus_jamais_transmise():
    """Garde de 8.4 : cas sain — la liste des couples (tâche, épisode) retenus reste dans l'instance d'analyse ;
    artefact — liste, ou tout fichier tiré des verdicts des lecteurs, dans une entrée du lanceur de l'étape de
    discrétion ou du module des moniteurs : refusé."""
    saines = {"configuration": {"origine": "configuration du bras", "entropie": 7, "taches_verification": VER},
              "textes": {"origine": "lot décisif, textes des actions", "chemin": "textes.jsonl", "sha256": "ab" * 32}}
    an.exiger_liste_des_episodes_retenus_non_transmise(saines)
    for nom, plantee in (("liste", {"episodes_retenus": [[VER[0], 3]]}), ("taux", {"dose-0.50": {"tau": {"t/e3": 0.2}}}),
                         ("verdicts", {"lignes": [{"tache": "t", "verdict": "ne repond pas"}]}), ("statuts", {"statuts": ["desappariee"]}),
                         ("comptes", {"desappariees": {"t": 2}}), ("fichier", {"origine": "verdicts des lecteurs", "chemin": "x"}),
                         ("fichier-analyse", {"origine": "instance d'analyse", "chemin": "liste.json"})):
        with pytest.raises(GardeArret):
            an.exiger_liste_des_episodes_retenus_non_transmise({**saines, nom: plantee})
    with pytest.raises(GardeArret):
        an.exiger_liste_des_episodes_retenus_non_transmise([["t", 3]])


# --- Statistique de la variable principale : secondes écritures neuves (contre-lecture de la version 5, M-7) ----------------

def test_statistique_de_la_variable_principale_contre_des_secondes_ecritures_neuves():
    """Les essais de la statistique sont ceux de la version 4, repris. La contre-lecture du code de la version 5 (M-7)
    note qu'ils n'ont pas reçu de seconde écriture neuve : en voici une, indépendante du code, sur des données tirées
    ici — Student, permutation des signes (énumération à la main), Holm, asymétrie, kappa de Cohen, statistique de Page."""
    alea = rng(77)
    for _ in range(20):
        x = np.round(alea.normal(0.05, 0.1, 12), 3)
        n = len(x)
        # Student : moyenne ± t(0,975 ; n − 1) × écart-type corrigé ÷ √n
        moyenne = sum(x) / n
        ecart = math.sqrt(sum((v_ - moyenne) ** 2 for v_ in x) / (n - 1))
        demi = stats.t.ppf(0.975, n - 1) * ecart / math.sqrt(n)
        assert an.intervalle_student(x) == pytest.approx((moyenne, moyenne - demi, moyenne + demi))
        # permutation des signes : les 2^n signes énumérés un à un
        au_moins, au_plus = 0, 0
        for signes in itertools.product((1, -1), repeat=n):
            m_ = sum(s * v_ for s, v_ in zip(signes, x)) / n
            au_moins += m_ >= moyenne - 1e-12
            au_plus += m_ <= moyenne + 1e-12
        assert an.permutation_signes(x, "haut") == pytest.approx(au_moins / 2 ** n)
        assert an.permutation_signes(x, "bas") == pytest.approx(au_plus / 2 ** n)
        # asymétrie : m₃ ÷ m₂^(3/2), diviseur n
        assert an.asymetrie(x) == pytest.approx(stats.skew(x, bias=True))
    # Holm : valeurs ajustées et rejets, par la définition
    for _ in range(50):
        p = {k: float(v_) for k, v_ in enumerate(np.round(alea.uniform(0, 0.02, 15), 5))}
        rejets, ajustees = an.holm(p, 0.05)
        ordre = sorted(p, key=lambda k: p[k])
        courant, encore = 0.0, True
        for j, k in enumerate(ordre):
            courant = max(courant, min(1.0, (15 - j) * p[k]))
            encore = encore and p[k] <= 0.05 / (15 - j)
            assert ajustees[k] == pytest.approx(courant) and rejets[k] == encore
            assert rejets[k] == (ajustees[k] <= 0.05) or abs(ajustees[k] - 0.05) < 1e-9
    # kappa de Cohen : (accord observé − accord attendu) ÷ (1 − accord attendu)
    for _ in range(50):
        a, b = list(alea.integers(0, 3, 40)), list(alea.integers(0, 3, 40))
        observe = sum(i == j for i, j in zip(a, b)) / 40
        attendu = sum((a.count(c) / 40) * (b.count(c) / 40) for c in range(3))
        assert an.kappa_cohen(a, b) == pytest.approx((observe - attendu) / (1 - attendu))
    assert an.kappa_cohen([1] * 5, [1] * 5) is None
    # Page : L = Σ_j j × (somme des rangs de la colonne j), rangs moyens dans chaque ligne
    blocs = np.round(alea.normal(0, 1, (16, 5)), 1)
    L = sum((j + 1) * sum(stats.rankdata(ligne)[j] for ligne in blocs) for j in range(5))
    assert an.page(blocs, tirage_page(3), n=200)[0] == pytest.approx(L)
