"""Essais des règles de décision du papier C (v1) : chaque règle sur des cas construits dont le verdict attendu se lit
dans le texte r1 (table des « Critères de lecture gelés », règle de HC2, « Combinaisons », audit), cas limites aux
seuils compris."""
import pytest

import papier_c_decisions_v1 as dec
from papier_c_erreurs_v1 import ConfigurationInvalide, MoyenneEnProduction


def ic(bas, haut):
    return {"bas": bas, "haut": haut}


# --- C-P2 --------------------------------------------------------------------------------------------------------
def test_familles_positives_holm_au_seuil():
    f = dec.familles_d_un_juge([0.005, 0.2, 0.3, 0.4, 0.5], [0.9, 0.9, 0.9, 0.9, 0.9])
    assert f["p_ajuste_positif"][0] == pytest.approx(0.025) and f["positive"] == [True, False, False, False, False]
    g = dec.familles_d_un_juge([0.0051, 0.2, 0.3, 0.4, 0.5], [0.9] * 5)
    assert g["positive"][0] is False                                   # 5 × 0,0051 > 0,025
    n = dec.familles_d_un_juge([0.9] * 5, [0.001, 0.9, 0.9, 0.9, 0.9])
    assert n["negative"][0] and not any(n["positive"])


def test_structure_holm_sur_les_dix_paires():
    paires = {(a, b): 0.5 for a in range(5) for b in range(a + 1, 5)}
    assert not dec.structure_d_un_juge(paires)["structure"]
    paires[(0, 1)] = 0.005                                             # 10 × 0,005 = 0,05 : au seuil, établi
    assert dec.structure_d_un_juge(paires)["structure"]
    paires[(0, 1)] = 0.0051
    assert not dec.structure_d_un_juge(paires)["structure"]


BAS, HAUT = [[0.05] * 5] * 3, [[0.5] * 5] * 3
POS, NUL = [True, False, False, False, False], [False] * 5


@pytest.mark.parametrize("positives, structures, bornes, attendu", [
    ([POS, POS, NUL], [True, True, False], HAUT, dec.CONFIRMEE),
    ([POS, POS, POS], [True, False, False], HAUT, dec.SIGNE_SANS_STRUCTURE),
    ([POS, POS, NUL], [False, False, True], HAUT, dec.SIGNE_SANS_STRUCTURE),   # la structure d'un juge non positif ne compte pas
    ([NUL, NUL, NUL], [False] * 3, BAS, dec.REFUTEE),
    ([NUL, NUL, NUL], [False] * 3, [[0.05] * 5, [0.05] * 5, [0.05, 0.05, 0.5, 0.5, 0.5]], dec.REFUTEE),      # 12 sur 15
    ([NUL, NUL, NUL], [False] * 3, [[0.05] * 5, [0.05] * 5, [0.05, 0.5, 0.5, 0.5, 0.5]], dec.NON_CONCLUANTE),  # 11 sur 15
    ([NUL, NUL, NUL], [False] * 3, [[0.10] * 5] * 3, dec.NON_CONCLUANTE),      # borne haute égale à 0,10 : pas « sous »
    ([POS, NUL, NUL], [True, False, False], BAS, dec.NON_CONCLUANTE),          # un seul juge positif
])
def test_verdict_c_p2(positives, structures, bornes, attendu):
    assert dec.verdict_c_p2(positives, structures, bornes)["verdict"] == attendu


def test_intensites_graduees_au_seuil():
    assert dec.intensites_graduees(0.05)["etablies"] and dec.intensites_graduees(0.05)["reserves"] == []
    assert dec.intensites_graduees(0.0501)["reserves"] == [dec.R_INTENSITES]


# --- C-P1 --------------------------------------------------------------------------------------------------------
def famille(positive=True, c=1.0, deg=0.0, pG=0.001, cc=0.9, cs=0.9, mc=0.9, ms=0.9):
    return {"positive": positive, "c": c, "part_degeneres": deg, "p_ajuste_G": pG, "p_cible_calibree": cc,
            "p_cible_sans_calibrage": cs, "p_moyenne_calibree": mc, "p_moyenne_sans_calibrage": ms}


def test_c_p1_lectures_conjointes_et_reserves():
    lignes = dec.lectures_c_p1_d_un_juge([
        famille(cc=0.001, cs=0.001),                       # vers la cible aux deux lectures
        famille(mc=0.001, ms=0.001, pG=0.004),             # vers la moyenne, gain fort
        famille(mc=0.001, ms=0.001, pG=0.006),             # vers la moyenne, réserve « gain faible »
        famille(cc=0.001, cs=0.9),                         # une seule lecture conclut
        famille(positive=False, cc=0.0001, cs=0.0001),     # non positive : non identifiable, hors de Holm
    ])
    assert [l["lecture"] for l in lignes] == [dec.VERS_LA_CIBLE, dec.VERS_LA_MOYENNE, dec.VERS_LA_MOYENNE,
                                             dec.ENTRE_LES_DEUX, dec.NON_IDENTIFIABLE]
    assert lignes[1]["reserves"] == [] and lignes[2]["reserves"] == [dec.R_GAIN_FAIBLE]
    assert lignes[3]["reserves"] == [dec.R_MODELE_ERREUR]
    assert not lignes[4]["identifiable"] and "p_ajustees" not in lignes[4]


def test_c_p1_holm_sur_les_familles_positives_seulement():
    # deux familles positives : 0,0125 × 2 = 0,025 ≤ 0,025 ; avec trois positives, 0,0125 × 3 > 0,025
    deux = dec.lectures_c_p1_d_un_juge([famille(cc=0.0125, cs=0.0125), famille(cc=0.5, cs=0.5), famille(positive=False)])
    assert deux[0]["lecture"] == dec.VERS_LA_CIBLE
    trois = dec.lectures_c_p1_d_un_juge([famille(cc=0.0125, cs=0.0125), famille(cc=0.5, cs=0.5), famille(cc=0.6, cs=0.6)])
    assert trois[0]["lecture"] == dec.ENTRE_LES_DEUX


@pytest.mark.parametrize("c, deg, identifiable", [(39.99, 0.01, True), (40.0, 0.0, False), (-30.0, 0.0, False),
                                                   (45.0, 0.0, False), (1.0, 0.0101, False), (float("nan"), 0.0, False)])
def test_c_p1_identifiabilite(c, deg, identifiable):
    ligne = dec.lectures_c_p1_d_un_juge([famille(c=c, deg=deg, cc=0.001, cs=0.001)])[0]
    assert ligne["identifiable"] is identifiable
    assert ligne["lecture"] == (dec.VERS_LA_CIBLE if identifiable else dec.NON_IDENTIFIABLE)


def couples(*lectures):
    return [{"positive": l is not None, "identifiable": l not in (None, "x"), "lecture": l or dec.NON_IDENTIFIABLE}
            for l in lectures]


C, M, E = dec.VERS_LA_CIBLE, dec.VERS_LA_MOYENNE, dec.ENTRE_LES_DEUX


@pytest.mark.parametrize("lectures, attendu, mention", [
    ((C, C, E), dec.CONFIRMEE, None),
    ((C, C, E, E), dec.CONFIRMEE, None),                     # exactement la moitié « vers la cible »
    ((C, E, E), dec.NON_CONCLUANTE, "mélange : rapporté famille par famille (C-P1b)"),
    ((C, C, M), dec.NON_CONCLUANTE, "mélange : rapporté famille par famille (C-P1b)"),   # un « vers la moyenne » suffit
    ((M, M, E), dec.REFUTEE, None),
    ((M, M, E, E), dec.REFUTEE, None),
    ((M, M, C), dec.NON_CONCLUANTE, "mélange : rapporté famille par famille (C-P1b)"),
    ((C, C), dec.NON_CONCLUANTE, "loi non identifiable"),    # moins de trois identifiables
    ((C, C, "x"), dec.NON_CONCLUANTE, "loi non identifiable"),
    ((None, None, None), dec.NON_CONCLUANTE, dec.NON_IDENTIFIABLE),   # C-P2 sans famille positive
])
def test_verdict_c_p1(lectures, attendu, mention):
    v = dec.verdict_c_p1(couples(*lectures))
    assert v["verdict"] == attendu and (mention is None or mention in v["mentions"])


def test_reserves_de_destination():
    base = dict(ic_c_net=ic(0.0, 1.0), ic_c_brut=ic(0.0, 1.0), etendue_attracteur=(3.0, 4.0), ic_c_temoin=ic(2.5, 3.5),
                v_etoile=0.0, attracteur=3.5, ic_c_rang_faible=ic(0.0, 1.0), ic_c_rang_fort=ic(0.5, 1.5),
                ic_ecart_intention=ic(-0.5, 0.5), c_p1_confirmee=True)
    assert dec.reserves_de_destination(**base) == []
    assert dec.reserves_de_destination(**{**base, "etendue_attracteur": (0.9, 4.0)}) == [dec.R_NON_SPECIFIQUE_ATTAQUE]
    assert dec.reserves_de_destination(**{**base, "ic_c_temoin": ic(1.0, 3.5)}) == [dec.R_NON_SPECIFIQUE_ATTAQUE]
    assert dec.reserves_de_destination(**{**base, "ic_c_temoin": ic(1.0, 3.5), "c_p1_confirmee": False}) == []
    assert dec.reserves_de_destination(**{**base, "attracteur": 0.4}) == [dec.R_ATTRACTEUR]       # |v* − a| < 0,5
    assert dec.reserves_de_destination(**{**base, "attracteur": 0.5}) == []                       # égal : pas inférieur
    assert dec.reserves_de_destination(**{**base, "ic_c_rang_fort": ic(1.1, 1.5)}) == [dec.R_HETEROGENE]
    assert dec.reserves_de_destination(**{**base, "ic_ecart_intention": ic(0.1, 0.5)}) == [dec.R_INTENTION]
    assert dec.reserves_de_destination(**{**base, "ic_ecart_intention": ic(0.0, 0.5)}) == []      # 0 dans l'intervalle


def test_verdict_c_p1b():
    assert dec.verdict_c_p1b([{(0, 1): 0.05}, {(0, 1): 0.01}, {(0, 1): 0.9}])["ligne"] == "destination dépendante de la famille"
    assert dec.verdict_c_p1b([{(0, 1): 0.051}, {(0, 1): 0.01}, {(0, 1): 0.9}])["ligne"] == "destination commune non rejetée"
    # deux juges, deux paires différentes : lecture littérale, la même paire est exigée chez deux juges
    assert dec.verdict_c_p1b([{(0, 1): 0.01, (0, 2): 0.9}, {(0, 1): 0.9, (0, 2): 0.01}, None])["ligne"] == \
        "destination commune non rejetée"
    assert dec.verdict_c_p1b([None, {(0, 1): 0.01}, {(0, 1): 0.01}])["non_concluant_pour_les_juges"] == [0]


# --- HC2 : règle « confirmation, réfutation et côté négatif », versions (i) et (n) -------------------------------
DANS, LARGE = ic(-0.05, 0.05), ic(-0.3, 0.3)


def hc2(niveaux90=None, moy95=DANS, corr=None, moy90=DANS, d0=True, agregation="max", non_testable=False):
    niveaux90 = niveaux90 or [DANS] * 3
    return dec.verdict_hc2(niveaux90, moy95, corr or niveaux90, moy90, d0, agregation, non_testable)


def test_hc2_confirmee_niveau_par_niveau_des_deux_cotes():
    v = hc2()
    assert v["verdict"] == dec.CONFIRMEE and v["mentions"] == [dec.M_ACTION]
    assert hc2([ic(-0.10, 0.10)] * 3)["verdict"] == dec.CONFIRMEE                    # bornes égales à la marge : dedans
    assert hc2([DANS, DANS, ic(-0.05, 0.1001)], moy95=LARGE, moy90=LARGE)["verdict"] == dec.NON_CONCLUANTE
    assert hc2([DANS, DANS, ic(-0.1001, 0.05)], moy95=LARGE, moy90=LARGE)["verdict"] == dec.NON_CONCLUANTE   # version (i)


def test_hc2_refutee_cote_positif_et_cote_negatif():
    haut = [LARGE] * 3
    p = hc2(haut, moy95=ic(0.1001, 0.4))
    assert p["verdict"] == dec.REFUTEE and p["cote"] == "positif" and dec.M_NEGATIF not in p["mentions"]
    assert hc2(haut, moy95=ic(0.10, 0.4), moy90=LARGE)["verdict"] == dec.NON_CONCLUANTE     # borne basse égale : pas > 0,10
    n = hc2(haut, moy95=ic(-0.4, -0.1001))
    assert n["verdict"] == dec.REFUTEE and n["cote"] == "négatif" and dec.M_NEGATIF in n["mentions"]
    assert hc2(haut, moy95=ic(-0.4, -0.10), moy90=LARGE)["verdict"] == dec.NON_CONCLUANTE


def test_hc2_refutation_par_niveau_version_n():
    niveaux = [DANS, DANS, ic(0.12, 0.3)]
    r = hc2(niveaux, moy95=ic(-0.02, 0.15), corr=[DANS, DANS, ic(0.101, 0.35)], moy90=ic(0.0, 0.12))
    assert r["verdict"] == dec.REFUTEE and r["cote"] == "niveau 3 (positif)"
    neg = hc2(niveaux, moy95=ic(-0.15, 0.02), corr=[DANS, ic(-0.4, -0.11), DANS], moy90=ic(-0.12, 0.0))
    assert neg["verdict"] == dec.REFUTEE and neg["cote"] == "niveau 2 (négatif)"
    # le niveau n'est pas entièrement hors de la marge au niveau corrigé : non concluante
    nc = hc2(niveaux, moy95=ic(-0.02, 0.15), corr=[DANS, DANS, ic(0.09, 0.35)], moy90=ic(0.0, 0.12))
    assert nc["verdict"] == dec.NON_CONCLUANTE and nc["mentions"] == [dec.M_ACTION]


def test_hc2_non_concluante_mention_du_niveau():
    v = hc2([DANS, ic(-0.02, 0.14), DANS], moy95=ic(-0.03, 0.09), corr=[DANS, ic(-0.05, 0.2), DANS], moy90=ic(-0.02, 0.08))
    assert v["verdict"] == dec.NON_CONCLUANTE and v["mentions"] == [dec.M_ACTION, "niveau 2 hors de la marge"]
    assert v["niveaux_hors_marge"] == [2]


def test_hc2_prerequis_et_puissance():
    assert hc2(d0=False)["verdict"] == dec.NON_INTERPRETABLE
    v = hc2(non_testable=True)
    assert v["verdict"] == dec.NON_CONCLUANTE and dec.M_NON_TESTABLE in v["mentions"] and v["issue_de_la_regle"] == dec.CONFIRMEE


@pytest.mark.parametrize("agregation", ["moyenne", "max_des_moyennes_glissantes", "mediane"])
def test_hc2_refuse_une_agregation_a_moyenne(agregation):
    """Interdit de CLAUDE.md et N-026 : un bras de diagnostic ne porte jamais une ligne de HC2 (artefact) ;
    le maximum et l'attention passent (cas sain)."""
    with pytest.raises(MoyenneEnProduction):
        hc2(agregation=agregation)
    assert hc2(agregation="attention")["verdict"] == dec.CONFIRMEE


def test_porte_gc_et_niveaux_gradues():
    assert dec.ligne_porte_gc(ic(0.001, 0.05), True)["ligne_ecrite"]
    assert not dec.ligne_porte_gc(ic(0.0, 0.05), True)["ligne_ecrite"]            # borne basse égale à 0 : pas > 0
    assert dec.ligne_porte_gc(ic(0.01, 0.05), False)["etat"] == dec.NON_INTERPRETABLE
    assert dec.niveaux_gradues([0.05, 0.01, 0.9])["reserves"] == []
    assert dec.niveaux_gradues([0.051, 0.01, 0.9])["reserves"] == [dec.R_NIVEAUX]
    assert dec.prerequis_d0(ic(0.01, 1)) and not dec.prerequis_d0(ic(0.0, 1))


# --- HC2b, C-P4b, C-P4c, C-P6 ------------------------------------------------------------------------------------
@pytest.mark.parametrize("i95, i90, attendu", [
    (ic(-0.4, -0.001), ic(-0.38, -0.02), dec.CONFIRMEE),
    (ic(-0.4, 0.0), ic(-0.38, -0.02), dec.NON_CONCLUANTE),            # borne haute égale à 0 : pas < 0
    (ic(-0.12, 0.12), ic(-0.10, 0.10), dec.REFUTEE),                  # équivalence à la marge
    (ic(-0.12, 0.12), ic(-0.101, 0.10), dec.NON_CONCLUANTE),
    (ic(0.001, 0.5), ic(0.02, 0.45), dec.REFUTEE),                    # borne basse à 95 % > 0
])
def test_verdict_hc2b(i95, i90, attendu):
    assert dec.verdict_hc2b(i95, i90, True, "max")["verdict"] == attendu
    assert dec.verdict_hc2b(i95, i90, False, "max")["verdict"] == dec.NON_INTERPRETABLE
    with pytest.raises(MoyenneEnProduction):
        dec.verdict_hc2b(i95, i90, True, "moyenne")


def test_verdict_c_p4b():
    assert dec.verdict_c_p4b(ic(0.01, 0.5), True)["verdict"] == dec.CONFIRMEE
    assert dec.verdict_c_p4b(ic(-0.5, -0.01), True)["verdict"] == dec.REFUTEE
    assert dec.verdict_c_p4b(ic(0.0, 0.5), True)["verdict"] == dec.NON_CONCLUANTE
    assert dec.verdict_c_p4b(ic(0.01, 0.5), False)["verdict"] == dec.NON_INTERPRETABLE


def couple(e=(0.1, 0.5), ec=(0.1, 0.5), ex=(0.1, 0.5), ok=True):
    return {"interpretable": ok, "ic_e": ic(*e), "ic_e_c": ic(*ec), "ic_e_x": ic(*ex)}


def test_opposition_d_une_sonde():
    assert dec.opposition_d_une_sonde([couple(), couple(), couple(e=(-0.1, 0.5))])["etat"] == "opposition établie"
    un = dec.opposition_d_une_sonde([couple(), couple(e=(-0.1, 0.5)), couple(e=(-0.1, 0.5))])
    assert un["etat"] == "autrement" and un["juges_etablis"] == 1
    inv = dec.opposition_d_une_sonde([couple(e=(-0.5, -0.1), ec=(-0.5, -0.1))] * 2 + [couple()])
    assert inv["etat"] == "opposition inverse"
    excl = dec.opposition_d_une_sonde([couple(ec=(-0.1, 0.5))] * 3)
    assert excl["etat"] == "autrement" and excl["mentions"] == [dec.M_EXCLUSION]
    fixe = dec.opposition_d_une_sonde([couple(ex=(-0.1, 0.5)), couple(), couple()])
    assert fixe["etat"] == "opposition établie" and fixe["mentions"] == [dec.M_LONGUEUR_FIXE]
    hors = dec.opposition_d_une_sonde([couple(ok=False), couple(ok=False), couple()])
    assert hors["etat"] == "autrement" and hors["par_juge"][:2] == [dec.NON_INTERPRETABLE] * 2


@pytest.mark.parametrize("etats, attendu", [
    (["opposition établie", "autrement"], dec.CONFIRMEE),
    (["opposition établie", "opposition inverse"], dec.NON_CONCLUANTE),
    (["opposition inverse", "opposition inverse"], dec.REFUTEE),
    (["opposition inverse", "autrement"], dec.NON_CONCLUANTE),
    (["autrement"], dec.NON_CONCLUANTE),
])
def test_verdict_c_p4c(etats, attendu):
    v = dec.verdict_c_p4c([{"etat": e} for e in etats])
    assert v["verdict"] == attendu and v["mentions"] == [dec.M_ACTION]


def test_c_p6_sondes_et_table():
    assert dec.lecture_sonde_c_p6(ic(-0.10, 0.10), LARGE, True, "max") == "équivalence"
    assert dec.lecture_sonde_c_p6(LARGE, ic(0.11, 0.3), True, "max") == "écart"
    assert dec.lecture_sonde_c_p6(LARGE, ic(-0.3, -0.11), True, "max") == "écart"
    assert dec.lecture_sonde_c_p6(LARGE, ic(0.10, 0.3), True, "max") == "autrement"
    assert dec.lecture_sonde_c_p6(DANS, DANS, False, "max") == dec.NON_INTERPRETABLE
    T, F = True, False
    assert dec.verdict_c_p6([T, T, F], [0.5] * 3, ["équivalence", "autrement"])["verdict"] == dec.CONFIRMEE
    assert dec.verdict_c_p6([T, T, F], [0.5] * 3, ["équivalence", "écart"])["verdict"] == dec.NON_CONCLUANTE
    assert dec.verdict_c_p6([T, F, F], [0.5] * 3, ["équivalence"])["verdict"] == dec.NON_CONCLUANTE
    r = dec.verdict_c_p6([F, F, F], [0.05, 0.09, 0.5], ["équivalence"])
    assert r["verdict"] == dec.REFUTEE and r["versant_juges"] == dec.REFUTEE and r["versant_sondes"] == dec.CONFIRMEE
    assert dec.verdict_c_p6([F, F, F], [0.05, 0.10, 0.5], ["équivalence"])["verdict"] == dec.NON_CONCLUANTE
    assert dec.verdict_c_p6([T, T, T], [0.5] * 3, ["écart", "écart"])["verdict"] == dec.REFUTEE


# --- C-P5 --------------------------------------------------------------------------------------------------------
def test_c_p5_par_juge_et_table():
    assert dec.lecture_c_p5_d_un_juge((0.90, 0.99), ic(0.90, 0.99)) == "confirmé"
    assert dec.lecture_c_p5_d_un_juge((0.899, 0.99), ic(0.95, 0.99)) == "autrement"       # les deux bornes exigées
    assert dec.lecture_c_p5_d_un_juge((0.5, 0.899), ic(0.5, 0.899)) == "réfuté"
    assert dec.lecture_c_p5_d_un_juge((0.5, 0.90), ic(0.5, 0.80)) == "autrement"
    c, r, a = "confirmé", "réfuté", "autrement"
    assert dec.verdict_c_p5([c, c, a], [True] * 3)["verdict"] == dec.CONFIRMEE
    assert dec.verdict_c_p5([c, c, r], [True] * 3)["verdict"] == dec.NON_CONCLUANTE       # aucun réfuté exigé
    assert dec.verdict_c_p5([r, r, c], [True] * 3)["verdict"] == dec.REFUTEE
    assert dec.verdict_c_p5([c, a, a], [True, False, True])["reserves"] == [f"{dec.R_CONTROLE_MANIPULATION} (juge 1)"]


# --- Combinaisons par sonde --------------------------------------------------------------------------------------
def combi(**k):
    base = dict(hc2={"verdict": dec.CONFIRMEE}, hc2b={"verdict": dec.NON_CONCLUANTE}, porte_gc={"ligne_ecrite": False},
                bornes_basses_juges=[0.2, 0.3, -0.1], ic95_gain_filtre=ic(-0.1, 0.1), ic95_lexical=ic(0.1, 0.4),
                c_p4c_verdict=dec.CONFIRMEE, niveaux={"reserves": []}, controlabilite_mesuree=True, ic95_moyenne=ic(-0.05, 0.05))
    return dec.combinaisons_d_une_sonde(**{**base, **k})


def test_combinaisons_audit_a9_dans_les_deux_sens():
    assert combi()["mentions"] == [] and combi()["lecture_confirmation"]
    c = combi(bornes_basses_juges=[0.0, -0.1, -0.2])
    assert c["mentions"] == [dec.M_SANS_EFFET] and c["audit_A9"] and not c["lecture_confirmation"]
    assert "présence du paragraphe dans les contenus SP_m" in c["audit_a_mener"]
    r = combi(hc2={"verdict": dec.REFUTEE}, bornes_basses_juges=[0.0, -0.1, -0.2])
    assert r["mentions"] == [dec.M_SONDE_SEULE] and r["audit_A9"]
    assert combi(hc2={"verdict": dec.NON_CONCLUANTE}, bornes_basses_juges=[0.0, 0.0, 0.0])["audit_A9"] is False


def test_combinaisons_mentions_fixees():
    assert combi(porte_gc={"ligne_ecrite": True})["mentions"] == [dec.M_MARGE_POSITIVE, dec.M_PORTE_GC]
    assert combi(c_p4c_verdict=dec.REFUTEE)["mentions"] == [dec.M_JUGES_MOINS]
    b = combi(hc2b={"verdict": dec.CONFIRMEE})
    assert b["mentions"] == [dec.M_TRAHISON_FAIBLE, dec.M_TEXTE]
    assert combi(hc2b={"verdict": dec.CONFIRMEE}, ic95_gain_filtre=ic(-0.3, -0.01))["mentions"] == \
        [dec.M_TRAHISON_FAIBLE, dec.M_TEXTE, dec.M_HORS_TEXTE]
    assert combi(ic95_lexical=ic(-0.1, 0.4))["reserves"] == [dec.M_MOTS]
    assert combi(ic95_lexical=None)["mentions"] == ["témoin lexical non mesuré"]
    assert combi(niveaux={"reserves": [dec.R_NIVEAUX]})["reserves"] == [dec.R_NIVEAUX]
    assert combi(controlabilite_mesuree=False)["mentions"] == [dec.M_CONTROLABILITE]
    n = combi(hc2={"verdict": dec.REFUTEE}, ic95_gain_filtre=ic(-0.3, -0.01), ic95_moyenne=ic(-0.4, -0.11))
    assert dec.M_NEGATIF_CHAMPS in n["mentions"]
    assert dec.M_NEGATIF_CHAMPS not in combi(ic95_gain_filtre=ic(-0.3, -0.01), ic95_moyenne=ic(-0.4, -0.10))["mentions"]
    assert combi(hc2={"verdict": dec.NON_INTERPRETABLE})["mentions"] == [
        "toutes les lignes de la sonde non interprétables, porte GC comprise"]


# --- Audit de symétrie -------------------------------------------------------------------------------------------
def test_audits_seuils():
    assert dec.audit_a1(0.11, 0.2) == [dec.R_LONGUEUR] and dec.audit_a1(0.10, 0.2) == []
    assert dec.audit_a2(1.0, ic(0.5, 1.5)) == [dec.R_NON_SPECIFIQUE] and dec.audit_a2(1.6, ic(0.5, 1.5)) == []
    assert dec.audit_a3(0.95, 0.84) == [dec.R_MASSE] and dec.audit_a3(0.95, 0.85) == []
    assert dec.audit_a5(r2_joint_net=0.98)["reserves"] == [dec.R_TROP_PROPRE]
    assert dec.audit_a5(r2_joint_net=0.979, largeur_ic_lambda=0.02, largeur_equivalence=0.02, separation_parfaite=False)["reserves"] == []
    assert dec.audit_a5(largeur_ic_lambda=0.019)["audit_a_mener"] == list(dec.AUDIT_TROP_PROPRE)
    assert dec.audit_a5(separation_parfaite=True)["motifs"] == ["séparation parfaite des alarmes"]
    assert dec.audit_a6(G_nets_du_juge=[0.0, -0.1, -0.2, 0.0, -0.3])["audit_a_mener"] == list(dec.AUDIT_DE_CHAINE)
    assert dec.audit_a6(G_nets_du_juge=[0.01, -0.1, -0.2, 0.0, -0.3])["motifs"] == []
    assert dec.audit_a6(alarme_jamais_au_dessus=True)["motifs"] and dec.audit_a6(ordre_contraire_trois_juges=True)["motifs"]
    assert dec.audit_a7(0.81) == [dec.R_BASCULE] and dec.audit_a7(0.8) == []
    assert dec.part_des_verdicts_changes([1, 2, 3, 4], [1, 2, 0, 0]) == 0.5
    assert dec.audit_a8(dec.CONFIRMEE, dec.NON_CONCLUANTE) == [dec.R_LONGUEUR_MAXIMUM] and dec.audit_a8("a", "a") == []


def test_banc_sur_carte_et_usurpation_marquee():
    sain = dec.banc_sur_carte(-0.5, 0.5, 1.0, 3.0, ic(0.5, 1.5))
    assert not sain["ordre_contraire"] and sain["reserves"] == [] and sain["juge_retire"] is False
    assert dec.banc_sur_carte(0.5, 0.5, 1.0, 3.0, ic(0.5, 1.5))["reserves"] == [dec.R_CONTROLE_POSITIF_ECHEC]
    assert dec.banc_sur_carte(-0.5, 0.5, 3.0, 3.0, ic(0.5, 1.5))["ordre_contraire"]
    assert dec.banc_sur_carte(-0.5, 0.5, 1.0, 3.0, ic(-0.1, 1.5))["reserves"] == [dec.R_CONTROLE_POSITIF_FAIBLE]
    assert dec.reserve_usurpation_marquee(0.21) == [dec.R_USURPATION_MARQUEE] and dec.reserve_usurpation_marquee(0.20) == []


def test_intervalle_mal_forme_refuse():
    with pytest.raises(ConfigurationInvalide):
        dec.verdict_c_p4b({"bas": 0.1}, True)
