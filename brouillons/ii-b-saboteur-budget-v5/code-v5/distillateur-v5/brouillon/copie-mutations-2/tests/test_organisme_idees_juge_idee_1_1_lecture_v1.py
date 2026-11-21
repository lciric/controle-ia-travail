"""Idée 1.1 (préenregistrement scellé `3ffe1739…`) — lecture gelée : comptes des cellules, seuils de l'annexe A, Holm dans
les deux sens, ordre des verdicts, ρ et ρ⁺, issue ; lecture complète sur des données synthétiques (aucune donnée du jeu)."""
import hashlib

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import banc_idee_1_1_v1 as B
from controle_ia.organisme_idees_juge import lecture_idee_1_1_v1 as LE
from controle_ia.organisme_idees_juge import mutations_idee_1_1_v1 as MU

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
    for bras in ("J8", "J9", "J9+", "La", "Ld", "J9-P", "La-P", "A1", "A2"):
        d[bras] = {"promue": bool(p.get(bras, False)), "max": 5.0 if p.get(bras) else -1.0}
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
    assert res["garde_P4"]["dent_H7_terme_projete"]["passee"] and res["garde_P4"]["verdict"] == "nécessaire, montrée sur le terme projeté"
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
