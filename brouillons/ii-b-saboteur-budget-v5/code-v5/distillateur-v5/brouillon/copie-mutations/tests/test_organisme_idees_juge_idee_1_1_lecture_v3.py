"""Idée 1.1 (préenregistrement scellé `3ffe1739…`) — lecture gelée : comptes des cellules, seuils de l'annexe A, Holm dans
les deux sens, ordre des verdicts, ρ et ρ⁺, issue ; lecture complète sur des données synthétiques (aucune donnée du jeu)."""
import hashlib

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import banc_idee_1_1_v2 as B
from controle_ia.organisme_idees_juge import lecture_idee_1_1_v3 as LE
from controle_ia.organisme_idees_juge import mutations_idee_1_1_v3 as MU

RACINE_ESSAI = int(hashlib.sha256(b"essais idee 1.1 v1, lecture").hexdigest(), 16)


def test_comptes_des_cellules_du_texte():
    LE.exiger_comptes_du_texte()
    assert tuple(LE.V) == LE.V_TEXTE


def test_seuils_de_l_annexe_A():
    assert LE.cp_bas_unilateral(527, 1000) > 0.5 >= LE.cp_bas_unilateral(526, 1000)
    assert LE.cp_bas_unilateral(63, 1000) > 0.05 >= LE.cp_bas_unilateral(62, 1000)
    assert LE.cp_bas_unilateral(29, 1000) >= 0.02 > LE.cp_bas_unilateral(28, 1000)


def test_holm_dans_chaque_sens_aux_seuils_de_l_annexe_A():
    n = 1000
    assert set(LE.statut_taille([(29, n)] * 61)) == {"tenue"}
    assert set(LE.statut_taille([(30, n)] * 61)) == {"non jugeable"}
    assert set(LE.statut_taille([(74, n)] * 61)) == {"non tenue"}
    assert set(LE.statut_taille([(73, n)] * 61)) == {"non jugeable"}
    assert LE.statut_taille([(0, n)] * 60 + [(38, n)])[-1] == "tenue"
    assert LE.statut_taille([(0, n)] * 60 + [(39, n)])[-1] == "non jugeable"
    assert LE.statut_taille([(1000, n)] * 60 + [(63, n)])[-1] == "non tenue"
    assert LE.statut_taille([(1000, n)] * 60 + [(62, n)])[-1] == "non jugeable"


@pytest.mark.parametrize("bas,haut,attendu", [(-0.3, -0.01, "nuisible"), (0.25, 0.9, "regagne"), (-0.1, 0.09, "ne regagne pas"),
                                              (0.1, 0.5, "partiel"), (0.24, 0.3, "partiel")])
def test_ordre_du_verdict_principal(bas, haut, attendu):
    assert LE.verdict_principal({"J9-P": {"bas": bas, "haut": haut}}) == attendu


def test_verdict_la_ld():
    assert LE.verdict_limite({"bas": 0.5, "haut": 0.9}) == "recouvre"
    assert LE.verdict_limite({"bas": 0.0, "haut": 0.24}) == "ne recouvre pas"
    assert LE.verdict_limite({"bas": 0.3, "haut": 0.6}) == "en partie"


def test_monotonie_exigee_par_la_lecture():
    a = np.zeros((1, 10), int)
    b = np.zeros((1, 10), int)
    b[0, 0] = 1
    with pytest.raises(GardeArret, match="monotonie"):
        LE.informatives(a, b, ["V1(0.25)"])


def test_lecture_egale_a_la_seconde_ecriture():
    tue, raison = MU.det_lecture(RACINE_ESSAI, B_=100)
    assert not tue, raison


def _rec(r, **p):
    """Enregistrement synthétique d'une répétition, champs lus par la lecture gelée."""
    d = {"r": r}
    for bras in ("J8", "J9", "J9+", "La", "Ld", "J9-P", "La-P", "A1"):
        d[bras] = {"promue": bool(p.get(bras, False)), "max": 5.0 if p.get(bras) else -1.0}
    d["A2"] = {"promue": bool(p.get("A2", False)), "log_w_200": 5.0 if p.get("A2") else -1.0}   # v3 : comme le banc (N1)
    d["ecart_residuel_La"] = d["ecart_residuel_Ld"] = [1e-4] * 8
    d["J9-D40"] = {"promue": bool(p.get("J9-D40", p.get("J9", False))), "max_40": -1.0}
    d["J9-D"] = {"promue": bool(p.get("J9-D", p.get("J9", False))), "quantite_fatale": -1.0}
    d["journal_J9-P"] = {"c_moins_1_max": 1e-6}
    d["ecart_residuel_J9"] = [1e-4] * 8
    return d


def _rec_h(r, nu_terme=False):
    t = lambda v: {"promue": bool(v), "max": 4.0 if v else -1.0, "log_w": []}
    return {"r": r, "J9": {"promue": False, "max": -1.0}, "J9-D40": {"promue": False, "max_40": -1.0},
            "J9-D": {"promue": False, "quantite_fatale": -1.0}, "J9-P-refus": {"refusee": True, "promue": False},
            "J9-P-nu": {"terme_projete": t(nu_terme), "complet": t(False), "lineaire_seul": t(nu_terme)},
            "J9-P-gel": {"terme_projete": t(False), "complet": t(False)}}


def donnees_completes(rng, gain=0.5):
    d = {}
    for nom in B.NOMS:
        recs = []
        for r in range(LE.R):
            u = rng.random()
            if nom in B.LIGNES_H:
                recs.append(_rec_h(r, nu_terme=(nom == "H7" and u < 0.3)))
            elif nom in ("Q2", "Q3", "Q4", "Q5"):
                recs.append(_rec(r, J8=u < 0.95, La=nom == "Q5" and u < 0.9, A1=nom == "Q2" and u < 0.95, A2=nom == "Q2" and u < 0.5))
            elif nom == "Q6":
                recs.append(_rec(r, J8=u < 0.95, J9=u < 0.9, La=u < 0.9, Ld=u < 0.9, **{"J9-P": u < 0.8}))
            elif nom == "Q1":
                recs.append(_rec(r, A1=u < 0.95, A2=u < 0.5))
            elif nom.startswith("V"):
                a, b = u < 0.5, u < 0.4
                x = b or (u < 0.4 + 0.1 * gain)
                recs.append(_rec(r, J8=a, J9=b, **{"J9+": b, "J9-P": x, "La": b or u < 0.47, "Ld": b or u < 0.44,
                                                   "La-P": b or u < 0.47, "J9-D": b, "J9-D40": b}))
            else:
                recs.append(_rec(r))
        d[nom] = recs
    return d


def test_lecture_complete_sur_donnees_synthetiques():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 903)))
    d = donnees_completes(rng)
    res = LE.lire(d, RACINE_ESSAI, B_=200)
    assert res["etage_1"] == "franchi" and res["etage_2"] == "franchi" and res["etage_3"] == "franchi"
    assert res["principale"] in LE.ORDRE_FAVORABLE and res["issue"].startswith("(")
    assert res["garde_P4"]["dent_H7_terme_projete"]["passee"]
    assert res["garde_P4"]["lectures"] == {"nécessaire, montrée sur le terme projeté": True,
                                           "non éprouvée (dent du terme projeté de H7 manquée)": False,
                                           "trou atteint par la grammaire (Hm ou Hg, juge complet sans garde)": False}
    assert len(res["rho"]["I"]) == 15 and set(res["secondaires"]) == {"La-P contre La", "J9-P contre La", "J9-D contre J9",
                                                                     "J9-D40 contre J9"}
    assert "toutes_vraies" in res["predictions"] and "tout_negatif" in res["audit_symetrie"]


def test_lecture_trou_sur_cellule_fatale_promue():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 904)))
    d = donnees_completes(rng)
    d["Q9a"][7]["J8"]["promue"] = True
    res = LE.lire(d, RACINE_ESSAI, B_=50)
    assert res["etage_1"] == "trou" and "principale" not in res


def test_lecture_banc_sans_dents():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 905)))
    d = donnees_completes(rng)
    for r in d["Q6"]:
        r["J9"]["promue"] = False
    res = LE.lire(d, RACINE_ESSAI, B_=50)
    assert res["etage_2"].startswith("banc sans dents")


def test_principale_sensible_au_certificat_moins_favorable_retenu(monkeypatch):
    seq = iter(["regagne", "partiel"])
    monkeypatch.setattr(LE, "verdict_principal", lambda r: "sans objet" if r.get("sans_objet") else next(seq))
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 906)))
    res = LE.lire(donnees_completes(rng), RACINE_ESSAI, B_=30)
    assert res["sensible_au_certificat"] and res["principale"] == "partiel"


def test_issue_non_tranchee_si_i_plus_trop_petit():
    assert LE.issue({"etage_3": "franchi", "principale": "non tranché", "La": "recouvre"}).startswith("(D)")
    assert LE.issue({"etage_3": "franchi", "principale": "partiel", "La": "recouvre"}).startswith("(B)")
    assert LE.issue({"etage_3": "franchi", "principale": "ne regagne pas", "La": "en partie", "Ld": "en partie"}).startswith("(C)")
    assert LE.issue({"etage_3": "franchi", "principale": "regagne"}).startswith("(A)")



# --- version 2 : M3, m1, m5, m7 -------------------------------------------------------------------------------------------
def test_strates_ecrites_d_apres_le_texte():
    for b, s in LE.STRATES_TEXTE.items():
        assert set(s["sur"]) | set(s["hors"]) == {"V1", "V2", "V3", "V4", "V5"} and not set(s["sur"]) & set(s["hors"])
    assert LE.lignes_de_strate("La", "sur") == ["V5(0.4)", "V5(0.8)", "V5(1.2)"]


def test_mcnemar_exact():
    x, y = np.array([1] * 10 + [0] * 90), np.zeros(100, int)
    assert LE.mcnemar_exact(x, y)["p"] == pytest.approx(2 * 0.5 ** 10)
    assert LE.mcnemar_exact(y, y)["p"] == 1.0


def test_lecture_v2_rapportes_de_la_metrique():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 907)))
    res = LE.lire_v2(donnees_completes(rng), RACINE_ESSAI, B_=60)
    assert set(res["secondaires_contre_J9_plus"]) == {"La-P contre La", "J9-P contre La", "J9-D contre J9+", "J9-D40 contre J9+"}
    assert set(res["rho_par_strate"]) == {f"{b}|{s}" for b in ("J9-P", "La", "Ld") for s in ("sur", "hors")}
    d = res["decomposition_du_prix_intervalles"]
    assert set(d) == {"1 - rho_La", "rho_La - rho_Ld", "rho_Ld", "ecartes", "niveau"}            # v3, n4 : écartés comptés, niveau déclaré
    assert all(d[k]["bas"] <= d[k]["haut"] for k in ("1 - rho_La", "rho_La - rho_Ld", "rho_Ld"))
    assert len(res["mcnemar"]) == 15 * len(LE.PAIRES_MCNEMAR)
    c = res["taux_des_cellules"]["Q8|J9-P"]
    assert {"intervalle", "log_w_max", "log_w_mediane"} <= set(c) and c["intervalle"][0] <= c["taux"] <= c["intervalle"][1]
    assert res["predictions"]["evaluation"]["P5"] in (True, False, "partielle")


def test_m1_quantite_fatale_absente_refusee():
    rec = {"J9-D": {"promue": False}}
    with pytest.raises(GardeArret, match="quantité fatale"):
        LE.log_w_max(rec, "J9-D")
    assert LE.log_w_max({"J9-D": {"quantite_fatale": -2.0}}, "J9-D") == -2.0


def test_m5_ecart_residuel_sur_j9_la_ld():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 908)))
    d = donnees_completes(rng)
    for r in d["Q1"][:20]:
        r["ecart_residuel_La"] = [1e-2] * 8
    a = LE.audit(d, {})
    assert a["part_ecart_residuel_superieur_2e-3"] > 0



# --- version 3 : artefacts de m4 et de m7, format, N1 ---------------------------------------------------------------------
def _avec_garde(d, h7_terme=0.3, hm_complet=0.0):
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 909)))
    for r in d["H7"]:
        r["J9-P-nu"]["terme_projete"]["promue"] = bool(rng.random() < h7_terme)
    for r in d["Hm"]:
        r["J9-P-nu"]["complet"]["promue"] = bool(rng.random() < hm_complet)
    return d


def test_m4_artefact_dent_manquee_et_trou_ensemble():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 910)))
    d = _avec_garde(donnees_completes(rng), h7_terme=0.0, hm_complet=0.5)
    res = LE.lire_v3(d, RACINE_ESSAI, B_=30)
    assert res["garde_P4"]["lectures"] == {"nécessaire, montrée sur le terme projeté": False,
                                           "non éprouvée (dent du terme projeté de H7 manquée)": True,
                                           "trou atteint par la grammaire (Hm ou Hg, juge complet sans garde)": True}


def test_m7_artefacts_p5_partielle_et_p12_refutee():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 911)))
    d = _avec_garde(donnees_completes(rng), h7_terme=0.0)
    for l in LE.V_TEXTE[2:]:                      # 2 lignes informatives seulement
        for r in d[l]:
            r["J8"]["promue"] = r["J9"]["promue"]
            r["J9+"]["promue"] = r["J9"]["promue"]
    res = LE.lire_v3(d, RACINE_ESSAI, B_=30)
    ev = res["predictions"]["evaluation"]
    assert ev["P5"] == "partielle"
    assert ev["P12"]["H7 terme projeté (réfutée si borne basse <= 0,05)"] is False
    assert res["predictions"]["toutes_vraies"] is False


def test_n1_a2_lu_a_200_dans_les_rapportes():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 912)))
    d = donnees_completes(rng)
    c = LE.taux_des_cellules(d)["Q1|A2"]
    assert "log_w_max" in c and c["log_w_max"] == 5.0


def test_format_inattendu_rend_une_garde_avec_message():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 913)))
    d = donnees_completes(rng)
    LE.verifier_format(d)
    for casse in ("champ", "sous-champ", "ordre", "ligne"):
        e = {k: [dict(r) for r in v] for k, v in d.items()}
        if casse == "champ":
            del e["Q3"][5]["A2"]
        elif casse == "sous-champ":
            e["V2(0.4)"][0]["A2"] = {"promue": False}
        elif casse == "ordre":
            e["Q4"][3]["r"] = 99
        else:
            del e["Hn"]
        with pytest.raises(GardeArret, match="format"):
            LE.lire_v3(e, RACINE_ESSAI, B_=10)


def test_erreur_imprevue_rendue_en_garde(monkeypatch):
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 914)))
    d = donnees_completes(rng)
    monkeypatch.setattr(LE, "lire_mcnemar", lambda donnees: {}["absent"])
    with pytest.raises(GardeArret, match="KeyError"):
        LE.lire_v3(d, RACINE_ESSAI, B_=10)


def test_n2_n4_reechantillons_tous_ecartes_arretent(monkeypatch):
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 915)))
    d = donnees_completes(rng)
    vrai = LE.informatives
    appels = {"n": 0}

    def seulement_la_premiere(a, b, lignes):
        appels["n"] += 1
        return vrai(a, b, lignes) if appels["n"] == 1 else []
    monkeypatch.setattr(LE, "informatives", seulement_la_premiere)
    with pytest.raises(GardeArret, match="tous les rééchantillons"):
        LE.lire_decomposition(RACINE_ESSAI, d, B_=5)
    appels["n"] = 0
    with pytest.raises(GardeArret, match="tous les rééchantillons"):
        LE.lire_rho_strate(RACINE_ESSAI, d, "J9-P", "sur", B_=5)
