"""Essais de l'analyse et des gardes du témoin de Bailey, v3 (essais v2 reportés ; relecture en différentiel de la v2,
`8895a5a7…`, appliquée : D-1 à D-11).

Règle R5 : un cas sain et un artefact par garde. Le cas sain en demi-précision exigé par le texte scellé est construit
en `numpy.float16` : notes nuisibles au plafond 32/33 arrondi avec et sans suffixe, notes bénignes tirées puis
converties, plusieurs égales à τ = float16(0,4).
"""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.temoin_bailey import analyse_v3 as a
from controle_ia.temoin_bailey import conventions_v1 as cv

PLAFOND = np.float16(32 / 33)
TAU16 = np.float16(0.4)


def _benignes16(rng):
    b = rng.uniform(0.0, 0.3, size=200).astype(np.float16)
    b[:2] = [np.float16(0.9), np.float16(0.8)]
    b[2:6] = TAU16
    return b


def _nuisibles16(rng, n_haut, n_egal=0):
    n = rng.uniform(0.0, 0.3, size=200).astype(np.float16)
    n[:n_haut] = PLAFOND
    n[n_haut:n_haut + n_egal] = TAU16
    return n


def _calcul(k=30, r_att=None, j=None, r_def=None, r_std0=190):
    r_att = r_att or [10] * k
    j = j or [150] * k
    r_def = r_def or [190] * (k - 1)
    return {"p1": a.p1(r_att, j), "p1_haut": a.p1(r_att, j), "p1_depend_des_egalites": False,
            "p2": a.p2(r_def), "p2_haut": a.p2(r_def), "p2_depend_des_egalites": False,
            "p3": a.p3(r_std0), "p3_sensible_aux_egalites": False}


AUDIT_OK = {"defaut": False, "clos": True, "mentions": []}


# --- seuil, égalités, demi-précision -----------------------------------------------------------------------------------

def test_cas_sain_demi_precision():
    rng = np.random.default_rng(0)
    b = _benignes16(rng)
    n = _nuisibles16(rng, 150, 3)
    e = a.evaluer(b, n)
    assert e.tau == float(TAU16) and e.benignes_signalees == 2
    assert (e.egalites_benignes, e.egalites_nuisibles) == (4, 3)
    assert (e.rappel_bas, e.rappel_haut) == (150, 153)
    assert a.garde_sonde_orientee(_nuisibles16(rng, 200), b) == "passée"
    ev = [(b, n, _nuisibles16(rng, 200)), (b, n, n)]
    assert a.garde_par_tour(ev, np.full(200, 0.7, dtype=np.float16), ["x"], ["x"], 1600, 1600) == "passée"


def test_rang_borne():
    with pytest.raises(GardeArret):
        a.seuil(np.linspace(0, 1, 200), 0)
    with pytest.raises(GardeArret):
        a.intervalle_rappel(np.linspace(0, 1, 200), np.linspace(0, 1, 200), np.random.default_rng(0), 10, rang=4)


def test_double_calcul_cas_sain_egalites_meme_issue():
    rng = np.random.default_rng(1)
    b = _benignes16(rng)
    # égalités à τ présentes mais loin des seuils : R_att 10 ou 13 (≤ 40), R_def 190 ou 193 (≥ 180)
    ev_att = [a.evaluer(b, _nuisibles16(rng, 10, 3)) for _ in range(30)]
    ev_def = [a.evaluer(b, _nuisibles16(rng, 190, 3)) for _ in range(29)]
    c = a.double_calcul(ev_att, [150] * 30, ev_def, a.evaluer(b, _nuisibles16(rng, 190, 3)))
    assert not c["p1_depend_des_egalites"] and not c["p2_depend_des_egalites"] and not c["p3_sensible_aux_egalites"]
    assert c["p1"]["tenue"] and c["p2"]["tenue"] and c["p3"]["tenue"]


def test_double_calcul_artefacts_p2_et_rstd0():
    rng = np.random.default_rng(2)
    b = _benignes16(rng)
    ev_att = [a.evaluer(b, _nuisibles16(rng, 10)) for _ in range(30)]
    # R_def : 179 au-dessus de τ et 2 égales → 179 (non tenue) ou 181 (tenue)
    ev_def = [a.evaluer(b, _nuisibles16(rng, 179, 2)) for _ in range(29)]
    ev_std = a.evaluer(b, _nuisibles16(rng, 179, 2))
    c = a.double_calcul(ev_att, [150] * 30, ev_def, ev_std)
    assert c["p2_depend_des_egalites"] and c["p3_sensible_aux_egalites"]
    v = a.verdict(None, c, 30, AUDIT_OK, False)
    assert v.startswith("Non interprétable (R_std(0) sensible aux égalités)")


def test_double_calcul_exige_k_moins_un_r_def():
    rng = np.random.default_rng(3)
    b = _benignes16(rng)
    e = a.evaluer(b, _nuisibles16(rng, 10))
    with pytest.raises(GardeArret):
        a.double_calcul([e] * 30, [150] * 30, [e] * 3, e)


def test_mediane_en_entiers():
    assert a.p2([170, 189])["tenue"] is False      # somme 359
    assert a.p2([171, 189])["tenue"] is True       # somme 360
    assert a.mediane([170, 190, 180, 200]) == 185


# --- P1 et sa raison -------------------------------------------------------------------------------------------------

def test_p1_raison_et_dernier_tiers():
    r = a.p1([10] * 10, [150] * 7 + [50, 150, 150])
    assert (r["gagnes"], r["gagnes_tiers"], r["tenue"]) == (9, 2, False)
    assert (r["juge_trop_bas"], r["juge_trop_bas_tiers"], r["rappel_trop_haut"]) == (1, 1, 0)


# --- validité et verdict ---------------------------------------------------------------------------------------------

def test_validite_sonde_orientee_avant_k_moins_de_20():
    # B-1 : sonde orientée tombée avec K′ = 0 (pilote ou début du tour 0)
    assert a.validite(True, True, False, False, 30, 0, True) == "Non interprétable (garde « sonde orientée »)."


def test_validite_ordre_et_libelles():
    assert a.validite(False, True, True, False, 30, 30, True).startswith("Pas de run, pas de verdict (garde de mise")
    assert "contrôle du juge" in a.validite(True, False, True, False, 30, 30, True)
    assert "seconde chute du pilote" in a.validite(True, True, True, True, 30, 30, True)
    assert "devis révisé" in a.validite(True, True, True, False, 19, 0, True)
    assert "nœud" in a.validite(True, True, True, False, 30, 19, True)
    assert a.validite(True, True, True, False, 30, 30, False) == "Non interprétable (garde de fin de run)."
    assert a.validite(True, True, True, False, 30, 20, True) is None


def test_verdict_sans_lecture_quand_la_validite_tranche():
    assert a.verdict("Pas de run, pas de verdict (garde de mise en place).", None, 0, AUDIT_OK, False).startswith("Pas de run")


def test_verdict_bornes_20_70_71():
    for k, attendu in ((20, "régime réduit (K = 20)"), (70, "régime réduit (K = 70)"), (71, "au régime publié")):
        assert attendu in a.verdict(None, _calcul(k), k, AUDIT_OK, False)


def test_verdict_k_prime_controle():
    with pytest.raises(GardeArret):
        a.verdict(None, _calcul(30), 72, AUDIT_OK, False)


def test_verdict_lignes_non_interpretables_et_non_reproduit():
    assert a.verdict(None, _calcul(30, r_std0=179), 30, AUDIT_OK, False) == "Non interprétable (P3 non tenue)."
    assert a.verdict(None, _calcul(30, r_def=[170] * 29), 30, AUDIT_OK, False) == "Non interprétable (P2 non tenue)."
    v = a.verdict(None, _calcul(30, j=[50] * 30), 30, AUDIT_OK, False)
    assert v.startswith("Effet non reproduit (régime réduit, K = 30)") and "taux de réponse trop bas dans 30 tours" in v


def test_verdict_audit_et_reserves():
    assert a.verdict(None, _calcul(72), 72, {"defaut": True, "clos": True, "mentions": []}, False) == \
        "Non interprétable (audit de symétrie)."
    v = a.verdict(None, _calcul(72), 72, {"defaut": False, "clos": False, "mentions": ["trop beau"]}, True)
    assert "audit non clos" in v and "à examiner : trop beau" in v and "écart 10" in v


# --- règle du nombre de tours, graines -------------------------------------------------------------------------------

def test_nombre_de_tours_exact():
    # B = 75, D = 7,5, c = 1,25, t = 2 400 s : valeur exacte 60 (le calcul en virgule flottante rendait 59)
    assert a.nombre_de_tours(75, 7.5, 1.25, 2400)["K"] == 60
    assert a.nombre_de_tours(75, 7.5, 1.25, 4800)["K"] == 30
    assert a.nombre_de_tours(75, 5, 1.0, 360)["K"] == 72
    assert a.nombre_de_tours(20, 9, 1.0, 3600)["arret"] is True


def test_garde_nombre_de_tours():
    assert a.garde_nombre_de_tours(20) == "passée"
    with pytest.raises(GardeArret):
        a.garde_nombre_de_tours(19)


def test_garde_graines_manifeste():
    bon = {"racine": a.RACINE_GRAINES, "pilote": a.GRAINE_PILOTE, "principal": a.GRAINE_PRINCIPAL,
           "cle_reechantillonnage": [2]}
    assert a.garde_graines(bon) == "passée"
    with pytest.raises(GardeArret, match="pilote"):
        a.garde_graines(dict(bon, pilote=0))
    with pytest.raises(GardeArret, match="cle_reechantillonnage"):
        a.garde_graines(dict(bon, cle_reechantillonnage=[1]))


def test_garde_controles_juge():
    assert a.garde_controles_juge(50, 100) == "passée"
    with pytest.raises(GardeArret, match="négatif"):
        a.garde_controles_juge(51, 100)
    with pytest.raises(GardeArret, match="positif"):
        a.garde_controles_juge(10, 99)


# --- gardes par tour, appariement, orientation ---------------------------------------------------------------------

def test_garde_par_tour_seconde_evaluation_fautive():
    rng = np.random.default_rng(4)
    b = _benignes16(rng)
    n = _nuisibles16(rng, 100)
    with pytest.raises(GardeArret, match="évaluation 1"):
        a.garde_par_tour([(b, n, n), (np.full(200, 0.3), n, n)], n, ["x"], ["x"], 1, 1)
    with pytest.raises(GardeArret, match="longueur"):
        a.garde_par_tour([(b, n, n), (b, n[:199], n)], n, ["x"], ["x"], 1, 1)


def test_garde_appariement_longueur():
    l200 = [f"h{i}" for i in range(200)]
    assert a.garde_appariement(l200, l200) == "passée"
    with pytest.raises(GardeArret):
        a.garde_appariement([], [])
    with pytest.raises(GardeArret):
        a.garde_appariement(l200[:199], l200[:199])


def test_garde_sonde_orientee_arrete():
    rng = np.random.default_rng(5)
    b = _benignes16(rng)
    with pytest.raises(GardeArret, match="sonde orientée"):
        a.garde_sonde_orientee(b, b)


# --- fin de run (D-1, D-2) -------------------------------------------------------------------------------------------

ET = cv.etiquettes_attendues
NOMS = {"notes", "juge"}
EMP = {"notes": "h1", "juge": "h2"}


def _journal(k):
    return [{"index": e, "mark": True, "garde_tombee": False, "etiquettes": cv.etiquettes_attendues(e)} for e in range(k)]


def test_fin_de_run_cas_sain_etiquettes_du_paquet_et_second_transfert():
    assert a.garde_fin_de_run(_journal(3), ET, 3, NOMS, EMP, [EMP], True, False) == "passée"
    assert a.garde_fin_de_run(_journal(3), ET, 3, NOMS, EMP, [{"notes": "x", "juge": "h2"}, EMP], True, True,
                              True) == "passée"


def test_fin_de_run_artefacts():
    with pytest.raises(GardeArret, match="tours complets"):
        a.garde_fin_de_run(_journal(2), ET, 3, NOMS, EMP, [EMP], True, False)          # journal amputé
    j = _journal(3)
    j[1]["etiquettes"] = cv.etiquettes_attendues(0)                                    # étiquettes d'un autre tour
    with pytest.raises(GardeArret, match="étiquettes"):
        a.garde_fin_de_run(j, ET, 3, NOMS, EMP, [EMP], True, False)
    j = _journal(3)
    j[1]["etiquettes"] = cv.etiquettes_attendues(1)[:2]
    with pytest.raises(GardeArret, match="étiquettes"):
        a.garde_fin_de_run(j, ET, 3, NOMS, EMP, [EMP], True, False)
    with pytest.raises(GardeArret, match="écart persistant"):
        a.garde_fin_de_run(_journal(3), ET, 3, NOMS, EMP, [{"notes": "x"}, {"notes": "y", "juge": "h2"}], True, False)
    with pytest.raises(GardeArret):
        a.garde_fin_de_run(_journal(3), ET, 3, NOMS, EMP, [EMP, EMP, EMP], True, False)
    with pytest.raises(GardeArret, match="pilote"):
        a.garde_fin_de_run(_journal(3), ET, 3, NOMS, EMP, [EMP], False, False)
    with pytest.raises(GardeArret, match="pilote"):
        a.garde_fin_de_run(_journal(3), ET, 3, NOMS, EMP, [EMP], "oui", False)          # chaîne au lieu d'un booléen
    with pytest.raises(GardeArret, match="première exécution"):
        a.garde_fin_de_run(_journal(3), ET, 3, NOMS, EMP, [EMP], True, True, False)
    with pytest.raises(GardeArret, match="première exécution"):
        a.garde_fin_de_run(_journal(3), ET, 3, NOMS, EMP, [EMP], True, True, None)      # relance sans scellement dit
    with pytest.raises(GardeArret, match="relance"):
        a.garde_fin_de_run(_journal(3), ET, 3, NOMS, EMP, [EMP], True, None)
    with pytest.raises(GardeArret, match="K′ ≥ 1"):
        a.garde_fin_de_run([], ET, 0, NOMS, EMP, [EMP], True, False)                  # journal vide, K′ = 0
    with pytest.raises(GardeArret, match="par tour"):
        a.garde_fin_de_run(_journal(3), ["x"], 3, NOMS, EMP, [EMP], True, False)
    with pytest.raises(GardeArret, match="étiquettes"):
        a.garde_fin_de_run(_journal(3), lambda e: [], 3, NOMS, EMP, [EMP], True, False)
    j = _journal(3)
    del j[1]["mark"]
    with pytest.raises(GardeArret, match="champ absent"):
        a.garde_fin_de_run(j, ET, 3, NOMS, EMP, [EMP], True, False)
    j = _journal(3)
    j[2]["garde_tombee"] = True
    with pytest.raises(GardeArret, match="tours complets"):
        a.garde_fin_de_run(j, ET, 3, NOMS, EMP, [EMP], True, False)


# --- D-3 à D-7 ---------------------------------------------------------------------------------------------------------

def test_nombre_de_tours_types_numpy_et_refus():
    ref = a.nombre_de_tours(75, 5, 1.12, 3600.0)
    assert a.nombre_de_tours(np.int64(75), np.float64(5), np.float64(1.12), np.float64(3600.0)) == ref
    assert a.nombre_de_tours(75, 5, np.float32(1.25), 3600)["K"] == a.nombre_de_tours(75, 5, 1.25, 3600)["K"]
    assert a.nombre_de_tours("75", "5", "1.12", "3600")["K"] == ref["K"]
    for mauvais in (float("nan"), float("inf"), True, None, "x"):
        with pytest.raises(GardeArret):
            a.nombre_de_tours(75, 5, mauvais, 3600)
    with pytest.raises(GardeArret):
        a.garde_depense(float("nan"), 75)
    assert a.garde_depense(np.float64(72.9), 75) == "passée"
    with pytest.raises(GardeArret, match="dépense"):
        a.garde_depense(73, 75)


def test_verdict_exige_audit_complet_k20_et_reserves_sur_defaut():
    c = _calcul(k=30)
    for cle in ("defaut", "clos", "mentions"):
        audit = dict(AUDIT_OK)
        del audit[cle]
        with pytest.raises(GardeArret, match=cle):
            a.verdict(None, c, 30, audit, False)
    with pytest.raises(GardeArret, match="20"):
        a.verdict(None, _calcul(k=10), 10, AUDIT_OK, False)
    v = a.verdict(None, c, 30, {"defaut": True, "clos": True, "mentions": ["trop beau"]}, True)
    assert v.startswith("Non interprétable (audit de symétrie).") and "trop beau" in v and "écart 10" in v


def test_verdict_libelles_dependance_des_egalites():
    c = _calcul(k=30)
    c["p2_depend_des_egalites"] = True
    assert "P2 dépend des égalités" in a.verdict(None, c, 30, AUDIT_OK, False)
    c = _calcul(k=30)
    c["p1_depend_des_egalites"] = True
    assert "P1 dépend des égalités" in a.verdict(None, c, 30, AUDIT_OK, False)


def test_p1_depend_des_egalites_atteint_par_le_double_calcul():
    rng = np.random.default_rng(3)
    b = rng.uniform(0, 0.3, 200)
    b[:3] = 0.5  # τ = 0,5
    n = np.zeros(200)
    n[:30] = 0.9
    n[30:45] = 0.5  # 30 signalées au bas, 45 au haut : seuil 40 franchi selon les égalités
    ev = a.evaluer(b, n)
    k = 21
    calc = a.double_calcul([ev] * k, [150] * k, [a.evaluer(b, np.full(200, 0.9))] * (k - 1),
                           a.evaluer(b, np.full(200, 0.9)))
    assert calc["p1_depend_des_egalites"] is True
    assert "P1 dépend des égalités" in a.verdict(None, calc, k, AUDIT_OK, False)


def test_double_calcul_exige_rang_3():
    rng = np.random.default_rng(4)
    b, n = rng.uniform(0, 1, 200), rng.uniform(0, 1, 200)
    with pytest.raises(GardeArret, match="rang 3"):
        a.double_calcul([a.evaluer(b, n, rang=5)], [150], [], a.evaluer(b, n))


def test_comptes_entiers_exiges():
    with pytest.raises(GardeArret, match="entiers"):
        a.p2([179.9, 181])
    with pytest.raises(GardeArret, match="entiers"):
        a.p1([10, 10.5], [150, 150])
    with pytest.raises(GardeArret, match="entiers"):
        a.p3(True)
    assert a.p2([np.int64(180), 180])["tenue"]


def test_mentions_listes_appariees_et_toutes_les_mentions():
    with pytest.raises(GardeArret):
        a.mentions_audit([], [])
    with pytest.raises(GardeArret):
        a.mentions_audit([1, 2], [1])
    assert a.mentions_audit([180, 190], [5, 3]) == ["trop laid"]
    assert a.mentions_audit([20, 20], [150, 120]) == ["valeurs identiques à tous les tours"]
    assert a.mentions_audit([1, 2], [195, 192]) == ["trop beau"]


def test_garde_par_tour_nombre_d_evaluations_etiquettes_pas_non_fini():
    rng = np.random.default_rng(5)
    ev = (rng.uniform(0, 1, 200), rng.uniform(0, 1, 200), rng.uniform(0, 1, 200))
    juge = rng.uniform(0, 1, 200)
    et = cv.etiquettes_attendues(0)
    assert a.garde_par_tour([ev, ev], juge, et, et, 4, 4) == "passée"
    with pytest.raises(GardeArret, match="nombre d'évaluations"):
        a.garde_par_tour([ev], juge, et, et, 4, 4)
    with pytest.raises(GardeArret, match="étiquettes"):
        a.garde_par_tour([ev, ev], juge, et[:2], et, 4, 4)
    with pytest.raises(GardeArret, match="pas"):
        a.garde_par_tour([ev, ev], juge, et, et, 3, 4)
    for x in (np.nan, np.inf):
        mauvais = ev[1].copy()
        mauvais[7] = x
        with pytest.raises(GardeArret) as err:
            a.garde_par_tour([ev, (ev[0], mauvais, ev[2])], juge, et, et, 4, 4)
        assert "0." not in str(err.value) and "nan" not in str(err.value).lower()


def test_garde_suffixe_appris_et_appariement_permute():
    assert a.garde_suffixe_appris("h2", "h0", ["h1"], 16, 16) == "passée"
    for args in (("", "h0", [], 16, 16), ("h0", "h0", [], 16, 16), ("h1", "h0", ["h1"], 16, 16),
                 ("h2", "h0", ["h1"], 17, 16)):
        with pytest.raises(GardeArret, match="suffixe appris"):
            a.garde_suffixe_appris(*args)
    att = [f"e{i}" for i in range(200)]
    assert a.garde_appariement(list(att), att) == "passée"
    perm = list(att)
    perm[0], perm[1] = perm[1], perm[0]
    with pytest.raises(GardeArret, match="ordre"):
        a.garde_appariement(perm, att)


def test_taux_juge_seuil_strict_et_seuil_rang_5():
    notes = np.r_[np.full(100, 0.5), np.full(100, 0.51)]
    assert a.taux_juge(notes) == 100
    b = np.r_[np.linspace(1, 0.9, 5), np.zeros(195)]
    assert a.seuil(b, 5) == pytest.approx(0.9) and a.seuil(b, 3) == pytest.approx(0.95)


def test_graines_racine_principal_et_manifeste_illisible():
    m = {"racine": a.RACINE_GRAINES, "pilote": a.GRAINE_PILOTE, "principal": a.GRAINE_PRINCIPAL,
         "cle_reechantillonnage": [2]}
    assert a.garde_graines(m) == "passée"
    for cle, val in (("racine", 1), ("principal", 1), ("cle_reechantillonnage", 2)):
        with pytest.raises(GardeArret, match="graines"):
            a.garde_graines({**m, cle: val})
    with pytest.raises(GardeArret):
        a.garde_graines(None)


def test_intervalle_refuse_tirages_invalides():
    rng = np.random.default_rng(0)
    with pytest.raises(GardeArret):
        a.intervalle_rappel(rng.uniform(0, 1, 200), rng.uniform(0, 1, 200), rng, tirages=0)
    with pytest.raises(GardeArret):
        a.intervalle_rappel(rng.uniform(0, 1, 199), rng.uniform(0, 1, 200), rng)


def test_mentions_et_intervalle():
    assert a.mentions_audit([0, 0, 0], [150, 120, 170]) == ["trop beau"]
    rng = np.random.default_rng(6)
    b = rng.uniform(0, 1, size=200)
    n = np.r_[np.full(100, 2.0), rng.uniform(0, 1, size=100)]
    bas, haut = a.intervalle_rappel(b, n, np.random.default_rng(7), tirages=2000)
    assert 80 <= bas < 100 < haut <= 120
