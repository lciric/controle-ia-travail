"""Gardes de la liste « Gardes testées sur un cas sain et sur un artefact (R5) » du préenregistrement scellé
(e821e875…), dans l'ordre de la liste ; chaque garde a au moins un essai « sain » et un essai « artefact ».
Aucun contraste de décision, aucune moyenne de Δ(N, ·) n'est calculé ni affiché : mondes jouets ou graines
d'essai (RACINE_VALIDATION, indices ≥ 900 000). Usage : PYTHONPATH=<dépôt>/src python3 -B -m pytest -q -p no:cacheprovider essais
"""
import json
import math
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pytest

from jouets_v2 import INDICE_ESSAI, ICI, monde_jouet

import balayage_v2 as ba
import bras_v2 as br
import graines_v2 as gr
import lecture_v2 as le
import mesures_v2 as ms
import monde_v2 as mo
import noyaux_v2 as ny
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller

RV = gr.RACINE_VALIDATION


def _monde(cond="M_bien", k=0):
    return mo.generer(cond, RV, INDICE_ESSAI + k)


# 1. noyau non défini positif à travers le glouton (CB-03) -------------------------------------------------

def _vecteurs_fautifs():
    rng = np.random.default_rng(1)
    o = rng.random((20, 5))
    d = rng.random((20, 6))
    o = (o / np.linalg.norm(o, axis=1, keepdims=True)).tolist()
    d = (d / np.linalg.norm(d, axis=1, keepdims=True)).tolist()
    return ny.noyau_fautif(o, d)


def test_g01_artefact_noyau_fautif_leve_dans_glouton_paires():
    with pytest.raises(ny.NonDefiniePositive):
        ny.glouton_paires(_vecteurs_fautifs(), 12)


def test_g01_artefact_noyau_fautif_leve_dans_copie_gardee():
    with pytest.raises(ny.NonDefiniePositive):
        ny.ordre_glouton_garde(_vecteurs_fautifs())


def test_g01_artefact_pivot_choisi_nul_leve_sans_sortie_partielle():
    # noyau défini positif sauf un candidat de pivot nul : la décomposition préalable lève (aucune sélection rendue)
    L = np.eye(14)
    L[3, 3] = 0.0
    with pytest.raises(ny.NonDefiniePositive):
        ny.glouton_paires(L, 12)


def test_g01_sain_noyau_corrige_selection_de_12():
    w = _monde()
    cos = w.obs.cos.tolist()
    s = [[c ** 2 for c in ligne] for ligne in cos]
    L = ny.noyau_corrige(s, list(w.obs.q))
    choisis, non_pos = ny.glouton_paires(L, 12)
    assert len(choisis) == 12 and len(set(choisis)) == 12 and non_pos == 0
    assert len(ny.ordre_glouton_garde(ny.noyau_v1(cos, list(w.obs.q)))) == w.obs.n


def test_g01_sain_noyaux_de_paires_definis_positifs():
    w = _monde()
    for beta0 in (False, True):
        L = br.noyau_paires(w.obs, beta0=beta0)
        choisis, non_pos = ny.glouton_paires(L, 12)
        assert len(set(choisis)) == 12 and non_pos == 0


# 2. balayage statique ---------------------------------------------------------------------------------------

def test_g02_artefact_except_refuse():
    src = "def f(L):\n    try:\n        return glouton_paires(L, 12)\n    except NonDefiniePositive:\n        return []\n"
    pb = ba.problemes(src, "bras_artefact.py")
    assert pb and "glouton_paires" in pb[0]
    src2 = "def f(L):\n    try:\n        return cholesky(L)\n    except Exception:\n        return None\n"
    assert ba.problemes(src2)


def test_g02_artefact_lecture_latente_refusee():
    assert ba.problemes("def f(obs, rng, aux):\n    return sorted(aux['m'].latent(J).vrais)\n")
    assert ba.problemes("from monde_v2 import JETON_MESURE\n")


def test_g02_sain_modules_livres_passent():
    assert ba.exiger_propre([ICI.parent / m for m in ba.MODULES_BRAS])


def test_g02_artefact_exiger_propre_leve(tmp_path):
    f = tmp_path / "bras_faux.py"
    f.write_text("try:\n    x = 1\nexcept NonDefiniePositive:\n    pass\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        ba.exiger_propre([f])


# 3. bras qui lit la vérité --------------------------------------------------------------------------------

def test_g03_artefact_bras_qui_demande_latent_leve():
    w = _monde()

    def bras_curieux(obs, rng, aux):
        return list(obs.vrais)[:12]          # champ latent demandé à la vue observée

    def bras_curieux_2(obs, rng, aux):
        return list(obs.arts)[:12]

    for curieux in (bras_curieux, bras_curieux_2):
        with pytest.raises(mo.AccesLatent):   # le bras « N » est remplacé par le bras artefact, dans l'exécution réelle
            ms.executer_monde(w, "M_bien", RV, INDICE_ESSAI, ["N"], fonctions={**br.FONCTIONS, "N": curieux})
    with pytest.raises(mo.AccesLatent):
        w.latent()
    with pytest.raises(mo.AccesLatent):
        w.latent(object())                    # un jeton qui n'est pas le jeton de mesure
    for nom in ("champ", "vrais", "arts", "plantes", "rares", "provenance", "verite", "latent"):
        with pytest.raises(mo.AccesLatent):
            getattr(w.obs, nom)
    with pytest.raises(mo.AccesLatent):
        w.obs.n = 3


def test_g03_artefact_bras_avec_jeton_proche_du_plafond_et_audit():
    prec_triche, prec_oracle = [], []
    for k in range(20):
        w = _monde(k=k)
        if ms.exclu(w, "M_bien"):
            continue
        L = w.latent(mo.JETON_MESURE)

        def bras_triche(obs, rng, aux, L=L):
            vrais = [x for x in obs.valides if x in L.vrais]
            return vrais[:12]

        fonctions = {**br.FONCTIONS, "N": bras_triche}
        r = ms.executer_monde(w, "M_bien", RV, INDICE_ESSAI + k, ["N", "oracle"], fonctions=fonctions)
        prec_triche.append(r["bras"]["N"]["precision"])
        prec_oracle.append(r["bras"]["oracle"]["precision"])
    t, o = np.mean(prec_triche), np.mean(prec_oracle)
    assert t >= le.AUDIT_ORACLE * o  # déclencheur de l'audit (S10) : précision ≥ 0,9 × oracle
    d = le.declencheurs_audit({("N-b", X): {"estimation": 0.0} for X in le.X2} |
                              {("N-a", X): {"ub95": 1.0} for X in le.X2}, {"A3": True, "gain_controle": False},
                              {"M_bien": t}, {"M_bien": o}, [], False, None, None)
    assert "précision de N ≥ 0,9 × oracle" in d


def test_g03_sain_N_sans_exception():
    w = _monde()
    r = ms.executer_monde(w, "M_bien", RV, INDICE_ESSAI, ["N"])
    assert r["exclu"] or len(r["bras"]["N"]["_paires"]) == 12


# 4. vecteur de concepts nul -------------------------------------------------------------------------------

def test_g04_vecteur_nul_compte_kappa_zero():
    # 4 articles, 2 domaines ; l'article 3 n'a aucune étiquette de concept
    w = monde_jouet([0, 0, 1, 1], [{"op:x", "co:A"}, {"op:y", "co:A"}, {"op:x", "co:A"}, {"op:y"}])
    v, nuls = br.vecteurs_concepts(w.obs)
    assert nuls == 1 and np.all(v[3] == 0)
    k = br.kappa(v)
    assert k[3].max() == 0.0 and not np.isnan(k).any()


def test_g04_sain_kappa_main():
    # deux articles, étiquettes co:A (df 2) et co:B (df 1 puis ...) : κ calculé à la main
    w = monde_jouet([0, 1, 2], [{"co:A", "co:B"}, {"co:A"}, {"co:C"}])
    v, nuls = br.vecteurs_concepts(w.obs)
    wa, wb = math.log(3 / 2), math.log(3 / 1)
    attendu = wa / math.sqrt(wa ** 2 + wb ** 2)
    assert nuls == 0 and abs(br.kappa(v)[0, 1] - attendu) < 1e-12 and br.kappa(v)[0, 2] == 0


def test_g04_artefact_kappa_hors_bornes_arrete():
    with pytest.raises(GardeArret):
        br.kappa(np.array([[1.5, 0.0], [1.0, 0.0]]))


# 5. abstention et complément --------------------------------------------------------------------------------

def test_g05_abstention_8_completee_par_4():
    w = _monde()
    fonctions = {**br.FONCTIONS, "N": lambda obs, rng, aux: list(obs.valides[:8])}
    r = ms.executer_monde(w, "M_bien", RV, INDICE_ESSAI, ["N"], fonctions=fonctions)
    m = r["bras"]["N"]
    assert m["n_complete"] == 4 and len(set(m["_paires"])) == 12 and m["_paires"][:8] == list(w.obs.valides[:8])


def test_g05_sain_12_sans_complement():
    w = _monde()
    r = ms.executer_monde(w, "M_bien", RV, INDICE_ESSAI, ["b"])
    assert r["bras"]["b"]["n_complete"] == 0


def test_g05_artefact_sortie_invalide_arrete():
    w = _monde()
    with pytest.raises(GardeArret):
        ms.completer(w.obs, [w.obs.valides[0], w.obs.valides[0]], np.random.default_rng(0))


# 6. monde exclu ---------------------------------------------------------------------------------------------

def _jouet_paires_valides(k):
    """k paires valides exactement : article 0 (domaine 0) partage op:x avec k articles d'autres domaines."""
    dom = [0] + list(range(1, k + 1)) + [k + 1]
    etiq = [{"op:x"}] + [{"op:x"} if False else {"op:x", f"op:p{i}"} for i in range(k)] + [{"op:z"}]
    # les k porteurs se partagent op:x deux à deux : on les rend incompatibles entre eux par les contraintes
    c_obs = [("0", "0", "0", "0")] + [("+", "0", "0", "0") if i % 2 else ("-", "0", "0", "0") for i in range(k)] \
        + [("0", "0", "0", "0")]
    return dom, etiq, c_obs


def test_g06_artefact_11_paires_valides_exclu_pour_tous():
    w = monde_jouet([0, 1, 2, 3, 4, 5, 0], [{"op:x"}] * 6 + [{"op:y"}], vrais=[(0, 1)])
    # 6 articles de domaines différents partageant op:x : 15 paires valides ; on en retire 4 par contraintes
    c = [("+", "0", "0", "0"), ("-", "0", "0", "0"), ("0",) * 4, ("0",) * 4, ("0",) * 4, ("0",) * 4, ("0",) * 4]
    w = monde_jouet([0, 1, 2, 3, 4, 5, 0], [{"op:x"}] * 6 + [{"op:y"}], vrais=[(0, 2)], c_obs=c)
    assert len(w.obs.valides) == 14
    c2 = [("+", "0", "0", "0"), ("-", "0", "0", "0"), ("-", "0", "0", "0"), ("-", "0", "0", "0"),
          ("0",) * 4, ("0",) * 4, ("0",) * 4]
    w11 = monde_jouet([0, 1, 2, 3, 4, 5, 0], [{"op:x"}] * 6 + [{"op:y"}], vrais=[(1, 2)], c_obs=c2)
    assert len(w11.obs.valides) == 12 and ms.exclu(w11, "M_bien") is None
    c3 = [("+", "-", "0", "0"), ("-", "0", "0", "0"), ("-", "0", "0", "0"), ("-", "0", "0", "0"),
          ("0", "+", "0", "0"), ("0",) * 4, ("0",) * 4]
    w_ex = monde_jouet([0, 1, 2, 3, 4, 5, 0], [{"op:x"}] * 6 + [{"op:y"}], vrais=[(1, 2)], c_obs=c3)
    assert len(w_ex.obs.valides) == 11
    assert ms.exclu(w_ex, "M_bien") == "moins de 12 paires valides"
    r = ms.executer_monde(w_ex, "M_bien", RV, INDICE_ESSAI, br.ORDRE_BRAS, {"grille_e_beta": (8, 1)})
    assert r["exclu"] and "bras" not in r


def test_g06_sain_12_paires_valides_non_exclu():
    c2 = [("+", "0", "0", "0"), ("-", "0", "0", "0"), ("-", "0", "0", "0"), ("-", "0", "0", "0"),
          ("0",) * 4, ("0",) * 4, ("0",) * 4]
    w = monde_jouet([0, 1, 2, 3, 4, 5, 0], [{"op:x"}] * 6 + [{"op:y"}], vrais=[(1, 2)], c_obs=c2)
    r = ms.executer_monde(w, "M_bien", RV, INDICE_ESSAI, ["b", "c", "oracle"])
    assert not r["exclu"] and all(len(m["_paires"]) == 12 for m in r["bras"].values())


def test_g06_artefact_sans_vraie_paire_exclu_hors_SP():
    c2 = [("+", "0", "0", "0"), ("-", "0", "0", "0"), ("-", "0", "0", "0"), ("-", "0", "0", "0"),
          ("0",) * 4, ("0",) * 4, ("0",) * 4]
    w = monde_jouet([0, 1, 2, 3, 4, 5, 0], [{"op:x"}] * 6 + [{"op:y"}], vrais=[], c_obs=c2)
    assert ms.exclu(w, "M_bien") == "aucune vraie paire valide" and ms.exclu(w, "SP") is None


# 7. échec de plantation ---------------------------------------------------------------------------------

def _lignes_plantation(k0, n, surcharge=None):
    out = []
    for k in range(n):
        L = mo.generer("M_bien", RV, k0 + k, surcharge=surcharge).latent(mo.JETON_MESURE)
        out.append({"exclu": None, "tentatives": L.tentatives, "replantations": L.replantations,
                    "n_champs": L.n_champs, "bras": {}})
    return out


def test_g07_artefact_pont_d_impossible_regeneration_comptee_puis_arret(monkeypatch):
    # 8 champs d'un domaine chacun : aucun pont proche (d) possible, ni par replantation ni par régénération
    monkeypatch.setattr(mo, "MAX_REPLANTATIONS", 2)                  # nombre réduit : durée de l'essai seulement
    with monkeypatch.context() as m:
        m.setattr(mo, "MAX_TENTATIVES", 5)
        with pytest.raises(GardeArret):
            mo.generer("M_bien", RV, INDICE_ESSAI, surcharge={"champs_choix": (8,)})
    # impossible une fois sur deux (monde de base à 8 champs : la replantation n'y peut rien) : régénérations entières
    # comptées, puis arrêt au-dessus du taux S11
    lignes = _lignes_plantation(INDICE_ESSAI, 30, surcharge={"champs_choix": (4, 8)})
    assert sum(l["tentatives"] > 0 for l in lignes) > 0
    with pytest.raises(GardeArret):
        ms.verifier_taux(lignes, "M_bien")


# Cas sain réécrit (contre-lecture du code, garde 7) : paramètres de décision, 300 mondes d'essai hors plages, taux de
# régénération entière soumis à S11 (2 %) par la garde réelle ; il PEUT échouer : l'essai jumeau ci-dessous montre que,
# sur les mêmes graines, l'ancienne règle (régénération entière dès le premier échec) le fait échouer.
K0_PLANTATION, N_PLANTATION = 951_000, 300


def test_g07_sain_parametres_de_decision_sous_S11():
    lignes = _lignes_plantation(K0_PLANTATION, N_PLANTATION)
    r = ms.verifier_taux(lignes, "M_bien")
    assert r["taux_regeneres"] <= ms.TAUX_ARRET
    assert r["taux_replantes"] > 0                                   # la replantation a bien servi sur ces graines


def test_g07_artefact_ancienne_regle_depasse_S11(monkeypatch):
    monkeypatch.setattr(mo, "MAX_REPLANTATIONS", 0)                  # sans replantation : régénération entière
    lignes = _lignes_plantation(K0_PLANTATION, N_PLANTATION)
    with pytest.raises(GardeArret):
        ms.verifier_taux(lignes, "M_bien")


# 8. monde jouet dont la précision est calculée à la main -------------------------------------------------

def test_g08_precision_complement_intervalles_a_la_main():
    c2 = [("+", "0", "0", "0"), ("-", "0", "0", "0"), ("-", "0", "0", "0"), ("-", "0", "0", "0"),
          ("0",) * 4, ("0",) * 4, ("0",) * 4]
    w = monde_jouet([0, 1, 2, 3, 4, 5, 0], [{"op:x"}] * 6 + [{"op:y"}], vrais=[(1, 2), (4, 5), (0, 4)], c_obs=c2)
    obs, L = w.obs, w.latent(mo.JETON_MESURE)
    vrais = sorted(L.vrais)
    autres = [x for x in obs.valides if x not in L.vrais]
    sortie = vrais[:2] + autres[:6]                                      # 8 paires dont 2 vraies
    complete, n_c = ms.completer(obs, sortie, np.random.default_rng(5))
    m = ms.mesurer(obs, L, complete, n_c, False)
    attendu = (2 + sum(1 for x in complete[8:] if x in L.vrais)) / 12
    assert n_c == 4 and m["precision"] == attendu
    # estimateurs et intervalles : écart apparié à la main
    va, vb = [0.25, 0.5, 0.0, 0.25], [0.0, 0.25, 0.0, 0.5]
    r = ms.ecart_apparie(va, vb, np.random.default_rng(7))
    assert abs(r["estimation"] - 0.0625) < 1e-15
    rng = np.random.default_rng(7)
    d = np.array(va) - np.array(vb)
    boot = d[rng.integers(0, 4, size=(2000, 4))].mean(axis=1)
    assert abs(r["lb95"] - np.quantile(boot, 0.025)) < 1e-15 and abs(r["ub99"] - np.quantile(boot, 0.995)) < 1e-15
    const = ms.ecart_apparie([0.5] * 10, [0.25] * 10, np.random.default_rng(0))
    assert const["lb99"] == const["ub99"] == 0.25


def test_g08_artefact_precision_hors_bornes_impossible():
    w = monde_jouet([0, 1], [{"op:x"}, {"op:x"}])
    with pytest.raises(GardeArret):
        ms.mesurer(w.obs, w.latent(mo.JETON_MESURE), [0] * 11, 0, False)


# 9. reproduction de v1 : copie gardée de ordre_glouton identique sur 50 mondes ------------------------------

def test_g09_copie_gardee_identique_a_v1_sur_50_mondes():
    import methodes_v1 as mt
    import monde_v1 as m1
    for k in range(50):
        w = m1.generer({"niveau": "bien" if k % 2 else "moyen"}, 4_000_000 + k)
        q = [a["q"] for a in w["arts"]]
        for qq in (q, [1.0] * w["n"]):
            assert ny.ordre_glouton_garde(ny.noyau_v1(w["cos"], qq)) == mt.ordre_glouton(w, qq)


def test_g09_artefact_copie_gardee_leve_ou_v1_borne():
    import methodes_v1 as mt
    # noyau semi-défini (deux articles identiques, γ = 0 simulé) : v1 borne le pivot à 1e-300, la copie lève
    l = [[1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    with pytest.raises(ny.NonDefiniePositive):
        ny.ordre_glouton_garde(l)
    assert len(mt.ordre_glouton({"n": 3, "cos": [[1, 1, 0], [1, 1, 0], [0, 0, 1]]}, [1e-10, 1e-10, 1e-10])) == 3


# 10. extension de S9 ----------------------------------------------------------------------------------------

def test_g10_extension_s9():
    assert ms.extension_s9(2400, 15.3) == (2400, False)          # sain
    assert ms.extension_s9(2400, 11.0) == (2400, False)
    assert ms.extension_s9(2400, 16.0) == (2625, False)          # artefact : la formule joue dès 15,3
    assert ms.extension_s9(2400, 20.0) == (4101, False)
    assert ms.extension_s9(2400, 25.0) == (4800, True)           # plafond atteint, rapporté, sans arrêt
    assert ms.extension_s9(2400, 21.64)[0] == 4800
    with pytest.raises(GardeArret):
        ms.extension_s9(2400, float("nan"))


# 11. graine du monde inerte ---------------------------------------------------------------------------------

def test_g11_sain_latents_inertes_egaux_miroir_different():
    for k in range(5):
        wb, wi = mo.generer("M_bien", RV, INDICE_ESSAI + k), mo.generer("M_inertes", RV, INDICE_ESSAI + k)
        ms.verifier_inertes(wb, wi)
        ob, oi = wb.obs, wi.obs
        assert ob.etiq_op == oi.etiq_op and ob.c_obs == oi.c_obs and ob.dom_obs == oi.dom_obs
        rares_b = [frozenset(l for l in e if l.startswith("co:R")) for e in ob.etiq_co]
        rares_i = [frozenset(l for l in e if l.startswith("co:R")) for e in oi.etiq_co]
        fonds_b = [frozenset(l for l in e if not l.startswith("co:R")) for e in ob.etiq_co]
        fonds_i = [frozenset(l for l in e if not l.startswith("co:R")) for e in oi.etiq_co]
        assert rares_b != rares_i
        # fonds et moyeu : égaux sauf là où la fuite de domaine d'une émission rare ajoute un fond (G9 ii)
        assert sum(fb != fi for fb, fi in zip(fonds_b, fonds_i)) <= 10


def test_g11_artefact_code_12_aux_roles_0_a_3_detecte():
    wb = mo.generer("M_bien", RV, INDICE_ESSAI)
    wi = mo.generer("M_inertes", RV, INDICE_ESSAI, surcharge={"_code_latent_force": 12})
    with pytest.raises(GardeArret):
        ms.verifier_inertes(wb, wi)


# 12. garde de configuration S16e ------------------------------------------------------------------------

def test_g12_garde_configuration():
    p = dict(mo.BASE_V2)
    assert mo.garde_configuration(p) == (18, 15)                 # sain
    p19 = dict(p, ponts=dict(p["ponts"], e=4))
    with pytest.raises(GardeArret):
        mo.garde_configuration(p19)                               # artefact : 19 paires
    p7444 = dict(p, ponts=dict(p["ponts"], b=7, c=4, d=4, e=4))
    with pytest.raises(GardeArret):
        mo.garde_configuration(p7444)                             # artefact : 7 / 4 / 4 / 4
    assert mo.garde_configuration(dict(p, ponts=mo.S16["ponts_V_surface"])) == (18, 13)  # 6 + 3 + 2 + 2 = 13 rares


# 13. N_filtre -----------------------------------------------------------------------------------------------

def _jouet_filtre(df_rare):
    # 4 domaines × 2 articles ; strates (0,1) et (2,3) proches (cos 0,5), les 4 autres éloignées (cos 0)
    dom = [0, 0, 1, 1, 2, 2, 3, 3]
    cos = np.eye(8)
    for i in range(8):
        for j in range(8):
            if i != j and {dom[i], dom[j]} in ({0, 1}, {2, 3}):
                cos[i, j] = 0.5
    etiq = [{"op:x"} for _ in range(8)]
    porteurs = [0, 4] + [1, 5, 6, 7, 2][: max(0, df_rare - 2)]
    for i in porteurs:
        etiq[i] = etiq[i] | {"co:R"}
    return monde_jouet(dom, etiq, cos=cos, vrais=[(0, 4)])


def test_g13_sain_palier_1_pris_d_abord():
    w = _jouet_filtre(2)
    p1, p2, p3 = br.paliers_filtre(w.obs)
    assert [w.obs.paires[x] for x in p1] == [(0, 4)]
    aux = {}
    sortie = br.bras_N_filtre(w.obs, np.random.default_rng(0), aux)
    assert w.obs.paires[sortie[0]] == (0, 4) and aux["rapport"]["N_filtre_paliers"][0] == 1
    assert sum(aux["rapport"]["N_filtre_paliers"]) == len(sortie)


def test_g13_artefact_aucun_palier_1_passage_declare_aux_paliers_2_et_3():
    w = _jouet_filtre(7)  # étiquette partagée de fréquence 7 > φ = 4
    p1, p2, p3 = br.paliers_filtre(w.obs)
    assert p1 == [] and p2 and p3
    aux = {}
    sortie = br.bras_N_filtre(w.obs, np.random.default_rng(0), aux)
    compte = aux["rapport"]["N_filtre_paliers"]
    assert compte[0] == 0 and compte[1] == len(p2) and compte[2] == len(sortie) - len(p2)


# 14. jugeabilité J ------------------------------------------------------------------------------------------

def _jouet_J():
    dom = list(range(10)) * 2
    etiq = [{"op:x"} for _ in range(20)]
    etiq[0] = etiq[0] | {"co:R"}
    etiq[11] = etiq[11] | {"co:R"}
    c_obs = [("+", "0", "0", "0") if i % 3 else ("0",) * 4 for i in range(20)]
    return monde_jouet(dom, etiq, vrais=[(0, 11)], c_obs=c_obs)


def test_g14_sain_J_vraie_quand_d1c_bat_c_de_facon_connue():
    w = _jouet_J()
    pd, pc = [], []
    for k in range(300):
        r = ms.executer_monde(w, "M_bien", RV, INDICE_ESSAI + k, ["d1c", "c"])
        pd.append(r["bras"]["d1c"]["precision"])
        pc.append(r["bras"]["c"]["precision"])
    assert all(p == 1 / 12 for p in pd)
    j = ms.ecart_apparie(pd, pc, np.random.default_rng(0))["lb95"] > le.SEUIL_J
    assert j


def test_g14_artefact_V_concepts_absents_d1c_non_applicable_et_J_non_calculee():
    w = _monde("V_concepts_absents")
    assert all(not e for e in w.obs.etiq_co)
    r = ms.executer_monde(w, "V_concepts_absents", RV, INDICE_ESSAI, ["N", "d1c", "c"])
    assert r["exclu"] or "d1c" not in r["bras"]
    with pytest.raises(GardeArret):
        br.bras_d1c(w.obs, np.random.default_rng(0), {})
    # l'artefact principal (J fausse sur les 300 miroirs de validation de M_inertes) est V9 : non lancé ici
    # (consigne de la mission : validation du générateur après contre-lecture du code) ; voir valider_generateur_v2.py


# 15. ordre du manifeste de S9 ---------------------------------------------------------------------------

def _run_jouet(tmp_path, decalage_resultat, n_prime_manifeste=None, executes=None):
    t0 = datetime(2026, 11, 1, 12, 0, 0, tzinfo=timezone.utc)
    s9 = {"M_bien": {"n": 2400, "sigma_chapeau": 16.0, "n_prime": n_prime_manifeste or 2625}}
    man = tmp_path / "manifeste.json"
    man.write_text(json.dumps({"cree_le": t0.isoformat(), "config": {"s9": s9, "nombres_de_mondes": {"M_bien": 2625}}}))
    sha = sceller(man)
    res = tmp_path / "resultats-M_bien.json"
    res.write_text(json.dumps({"manifeste_sha256": sha,
                               "resultat": {"ecrit_le": (t0 + timedelta(seconds=decalage_resultat)).isoformat()}}))
    sceller(res)
    return ms.verifier_ordre(man, [res], executes or {"M_bien": 2625})


def test_g15_sain_ordre_du_manifeste(tmp_path):
    assert _run_jouet(tmp_path, 60) == []


def test_g15_artefacts_ordre_du_manifeste(tmp_path):
    for k, args in enumerate([(-60, None, None), (60, 2500, None), (60, None, {"M_bien": 2400})]):
        d = tmp_path / str(k)
        d.mkdir()
        assert _run_jouet(d, *args), args


# 16. loi de M_fonds_1ou2 et option b_eloigne (S17 = option 1) ------------------------------------------

def test_g16_loi_fonds():
    p = dict(mo.BASE_V2, loi_fonds={1: 0.6, 2: 0.4})
    mo.garde_configuration(p)                                     # sain
    with pytest.raises(GardeArret):
        mo.garde_configuration(dict(p, loi_fonds={1: 0.6, 2: 0.5}))  # artefact


def _contrastes(n_moins_beloigne):
    r = lambda est, lb, ub, lb99=None, ub99=None: {"estimation": est, "lb95": lb, "ub95": ub,
                                                   "lb99": lb if lb99 is None else lb99,
                                                   "ub99": ub if ub99 is None else ub99}
    c = {}
    for X in le.X2:
        c[("N-b", X)] = r(0.10, 0.08, 0.12)
        c[("r_N_b", X)] = {"estimation": 1.5}
        for k in ("N-a", "N-d1", "N-d1c"):
            c[(k, X)] = r(0.08, 0.06, 0.10)
        c[("N-b_eloigne", X)] = n_moins_beloigne
        c[("N-N_beta0", X)] = r(0.05, 0.04, 0.06)
        c[("d1c-c", X)] = r(0.06, 0.05, 0.07)
        c[("N-N_filtre", X)] = r(0.03, 0.02, 0.04)
        c[("N-N_PCg", X)] = r(0.05, 0.04, 0.06)
        c[("N_PCg-N_beta0", X)] = r(-0.01, -0.02, 0.0, -0.025, 0.005)
    for k in ("SP:N-b", "SP:N-d1c", "SP:N-N_beta0"):
        c[(k, "SP")] = r(0.0, -0.01, 0.01, -0.012, 0.012)
    c[("INV-M_bien", "INV")] = r(-0.1, -0.12, -0.08)
    c[("N-b", "NR_bien")] = r(0.0, -0.005, 0.005, -0.008, 0.008)
    c[("N-b", "NR_moyen")] = r(0.0, -0.005, 0.005, -0.008, 0.008)
    c[("V_fuite-M_bien", "V_fuite")] = r(-0.03, -0.05, -0.01)
    c[("N-N_beta0", "M_inertes")] = r(-0.01, -0.02, 0.0)
    return c


def test_g16_sain_N_bat_b_eloigne_clause_A2_tenue():
    c = _contrastes({"estimation": 0.04, "lb95": 0.03, "ub95": 0.05})
    b = le.booleens(c)
    assert b[("A2", "M_bien")] and b[("A2", "M_moyen")]
    assert le.table1(b, True, False, False, False)[0] == 10


def test_g16_artefact_b_eloigne_bat_N_clause_fausse_ligne_9bis():
    c = _contrastes({"estimation": -0.04, "lb95": -0.05, "ub95": -0.03})
    b = le.booleens(c)
    assert not b[("A2", "M_bien")] and not b[("A2", "M_moyen")]
    assert le.table1(b, True, False, False, False)[0] == "9 bis"
    # option 2 (b_eloigne descriptif) : clause de A2 absente, ligne 9 bis absente : la même donnée donne la ligne 10
    b2 = le.booleens(c, s17_option=2)
    assert b2[("A2", "M_bien")] and le.table1(b2, True, False, False, False, s17_option=2)[0] == 10
