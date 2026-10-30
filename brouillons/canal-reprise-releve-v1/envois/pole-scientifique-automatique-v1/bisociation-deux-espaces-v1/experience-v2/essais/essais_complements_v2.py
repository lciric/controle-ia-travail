"""Essais complémentaires (seconde session, Sonnet) : graines du § 7, gardes de la liste d'arrêt non couvertes par
essais_gardes_v2.py, plomberie de l'analyse, de la validation et de l'invocation unique. Aucun contraste de décision
n'est calculé sur un monde : les contrastes sont calculés sur des tableaux synthétiques (nombres tirés par numpy, sans
monde) ; les mondes d'essai ont des indices ≥ 950 000 sous RACINE_VALIDATION ; RACINE n'est jamais employée.
Corrections v2 (après la contre-lecture du code et R-600) : V4 par copie, code 16, lignes synthétiques porteuses de
l'empreinte des latents ; les essais propres aux corrections sont dans essais_corrections_v2.py.
Usage : PYTHONPATH=<dépôt>/src python3 -B -m pytest -q -p no:cacheprovider essais/essais_complements_v2.py
"""
import json
import time
from datetime import datetime, timezone

import numpy as np
import pytest

from jouets_v2 import INDICE_ESSAI, ICI, monde_jouet

import analyse_v2 as an
import balayage_v2 as ba
import bras_v2 as br
import graines_v2 as gr
import invocation_unique_v2 as inv
import lecture_v2 as le
import mesures_v2 as ms
import monde_v2 as mo
import travail_v2 as tr
import validation_v2 as va
from controle_ia import manifeste as man
from controle_ia.gardes import GardeArret, exiger_numpy_minimal
from controle_ia.scellement import sceller

RV = gr.RACINE_VALIDATION
TOUTES = list(mo.CONDITIONS_V2) + list(mo.CONDITIONS_NR)


# --- graines du § 7 ---------------------------------------------------------------------------------------

def test_graines_cles_exactes_du_paragraphe_7():
    ss = gr.sequence(RV, 1, 5, gr.ROLE_MONDE)
    assert ss.entropy == RV and tuple(ss.spawn_key) == (1, 5, 0)
    assert tuple(gr.sequence(RV, 1, 5, 2, tentative=3).spawn_key) == (1, 5, 2, 3)          # G11 : 4e élément
    assert tuple(gr.sequence(RV, 5, 14, 99, extra=1).spawn_key) == (5, 14, 99, 1)           # second flux
    assert gr.CODES_CONDITION == {"M_bien": 1, "M_moyen": 2, "M_mal": 3, "SP": 4, "INV": 5, "V_fuite": 6,
                                  "V_concepts_absents": 7, "V_moyeu_conceptuel": 8, "V_surface": 9, "NR_bien": 10,
                                  "NR_moyen": 11, "M_inertes": 12, "M_couplage_faible": 13, "M_palettes_communes": 14,
                                  "M_palettes_disjointes": 15, "M_fonds_1ou2": 16}
    assert (gr.ROLE_MONDE, gr.ROLE_OBS_OPERATEURS, gr.ROLE_OBS_CONCEPTS, gr.ROLE_CONTRAINTES) == (0, 1, 2, 3)
    assert (gr.ROLE_PLACEBO_PC, gr.ROLE_PLACEBO_SP, gr.ROLE_PLACEBO_PCG, gr.ROLE_MIROIR) == (4, 5, 6, 7)
    assert gr.ROLE_REECHANTILLONNAGE == 99 and gr.RACINE == 20261101 and gr.RACINE_VALIDATION == 20261102
    assert br.ORDRE_BRAS[0] == "N" and gr.ROLE_BRAS_BASE + br.RANG["N"] == 10 and gr.ROLE_BRAS_BASE + br.RANG["N_grille"] == 30
    assert len(br.ORDRE_BRAS) == 21
    rng = ms.rng_contraste(RV, 5, 14, second=True)
    ref = np.random.default_rng(np.random.SeedSequence(entropy=RV, spawn_key=(5, 14, 99, 1)))
    assert rng.random() == ref.random()


def test_graines_racine_interdite_et_numpy_minimal():
    with pytest.raises(GardeArret):
        gr.sequence(12345, 1, 0, 0)                    # artefact : racine hors du § 7
    with pytest.raises(GardeArret):
        ms.verifier_racine(gr.RACINE_VALIDATION, decision=True)   # monde de décision tiré avec RACINE_VALIDATION
    with pytest.raises(GardeArret):
        ms.verifier_racine(gr.RACINE, decision=False)
    assert ms.verifier_racine(gr.RACINE, decision=True) and ms.verifier_racine(RV, decision=False)   # sain
    with pytest.raises(GardeArret):
        exiger_numpy_minimal("1.24.4")                 # artefact : numpy < 1.25
    assert exiger_numpy_minimal("1.25.0") and exiger_numpy_minimal()


def test_monde_deterministe_et_independant_du_nombre_de_processus():
    for c in ("M_bien", "NR_moyen"):
        a = tr.executer_condition(c, RV, range(INDICE_ESSAI, INDICE_ESSAI + 16), bras=["N", "b", "c"], processus=1)
        b = tr.executer_condition(c, RV, range(INDICE_ESSAI, INDICE_ESSAI + 16), bras=["N", "b", "c"], processus=2)
        assert a == b


# --- G1 : séparation vérité / observation ----------------------------------------------------------------------

def test_g1_obs_ne_contient_aucun_latent_et_est_en_lecture_seule():
    w = mo.generer("M_bien", RV, INDICE_ESSAI)
    champs_observes = set(mo.Obs.__slots__) - {"_fige"}
    assert not (champs_observes & ba.INTERDITS)
    assert not w.obs.cos.flags.writeable
    with pytest.raises(TypeError):
        w.obs.df["op:x"] = 3          # fréquences documentaires : vue en lecture seule
    L = w.latent(mo.JETON_MESURE)
    assert L.vrais is not None and hasattr(L, "arts") and hasattr(L, "plante")


# --- G8, G5 : mondes d'essai de toutes les conditions, tous les bras --------------------------------------------

@pytest.mark.parametrize("cond", TOUTES)
def test_toutes_conditions_tous_les_bras_12_paires_valides_distinctes(cond):
    n_ok = 0
    for k in range(3):
        i = INDICE_ESSAI + 50 + k
        w = mo.generer(cond, RV, i)
        r = ms.executer_monde(w, cond, RV, i, br.ORDRE_BRAS, {"grille_e_beta": (8, 1)})
        if r["exclu"]:
            continue
        n_ok += 1
        attendus = set(br.ORDRE_BRAS) - ms.NON_APPLICABLES.get(cond, set())
        assert set(r["bras"]) == attendus
        for b, m in r["bras"].items():
            assert len(m["_paires"]) == 12 == len(set(m["_paires"])) and set(m["_paires"]) <= set(w.obs.valides)
            assert 0.0 <= m["precision"] <= 1.0 and m["n_complete"] >= 0
        assert r["bras"]["N_dpp"]["n_complete"] == 0 if "N_dpp" in r["bras"] else True
        assert "mecanismes_vrais" in r and "N_filtre_paliers" in r["rapport"]
        assert sum(r["rapport"]["N_filtre_paliers"]) <= 12
    assert n_ok >= 1


def test_bras_d1c_non_applicable_exclu_d_avance_dans_nr_et_concepts_absents():
    for cond in ("NR_bien", "NR_moyen", "V_concepts_absents"):
        i = INDICE_ESSAI + 7
        r = ms.executer_monde(mo.generer(cond, RV, i), cond, RV, i, ["N", "d1c", "d1"])
        assert r["exclu"] or ("d1c" not in r["bras"] and "d1" in r["bras"])


def test_m_inertes_bras_et_placebos_tirent_avec_le_code_12():
    i = INDICE_ESSAI + 3
    w = mo.generer("M_inertes", RV, i)
    r = ms.executer_monde(w, "M_inertes", RV, i, ["c", "oracle"])
    if r["exclu"]:
        pytest.skip("monde exclu")
    attendu = [w.obs.valides[int(k)] for k in gr.generateur(RV, 12, i, 10 + br.RANG["c"]).choice(
        len(w.obs.valides), size=12, replace=False)]
    assert r["bras"]["c"]["_paires"] == attendu
    wb = mo.generer("M_bien", RV, i)
    rb = ms.executer_monde(wb, "M_bien", RV, i, ["c"])
    if not rb["exclu"]:
        assert rb["bras"]["c"]["_paires"] != attendu or wb.obs.valides == w.obs.valides is False


# --- mécanismes (G12), rapports -------------------------------------------------------------------------------

def test_mecanismes_somme_egale_nombre_de_vraies_paires_et_plantes_a_la_main():
    w = mo.generer("M_bien", RV, INDICE_ESSAI + 9)
    L = w.latent(mo.JETON_MESURE)
    mec = ms.mecanismes_vrais(L)
    assert set(mec) == L.vrais and set(mec.values()) <= set(ms.MECANISMES)
    # à la main : trois vraies paires, deux plantées
    j = monde_jouet([0, 1, 2, 3], [{"op:x"}] * 4, vrais=[(0, 1), (0, 2), (1, 3)])
    Lj = j.latent(mo.JETON_MESURE)
    Lj.plante = {sorted(Lj.vrais)[0]: "greffe", sorted(Lj.vrais)[1]: "conceptuel"}
    assert sorted(ms.mecanismes_vrais(Lj).values()) == ["expansion", "greffe", "pont_conceptuel_direct"]


# --- liste d'arrêt : gardes de contrôle -------------------------------------------------------------------------

def test_plafond_de_l_oracle():
    assert ms.verifier_plafond_oracle(0.45, "M_bien")                         # sain
    assert ms.verifier_plafond_oracle(0.2, "M_mal") is False                  # descriptive : pas d'arrêt
    with pytest.raises(GardeArret):
        ms.verifier_plafond_oracle(0.29, "M_moyen")                           # artefact
    with pytest.raises(GardeArret):
        ms.verifier_plafond_oracle(float("nan"), "M_bien")


def test_taux_s11_exclusion_regeneration_sortie_vide():
    sain = [{"exclu": None, "tentatives": 0, "bras": {"N": {"sortie_vide": False}}}] * 100
    assert ms.verifier_taux(sain, "M_bien")["taux_exclus"] == 0.0
    exclus = [{"exclu": "x", "tentatives": 0, "bras": {}}] * 3 + sain[:97]
    with pytest.raises(GardeArret):
        ms.verifier_taux(exclus, "M_bien")                                   # 3 % > 2 %
    assert ms.verifier_taux(exclus, "M_mal", decision=False)["taux_exclus"] == 0.03   # condition non décisive : rapporté
    vides = [{"exclu": None, "tentatives": 0, "bras": {"d1": {"sortie_vide": i < 3}}} for i in range(100)]
    with pytest.raises(GardeArret):
        ms.verifier_taux(vides, "M_bien")
    regen = [{"exclu": None, "tentatives": 1 if i < 3 else 0, "bras": {}} for i in range(100)]
    with pytest.raises(GardeArret):
        ms.verifier_taux(regen, "M_bien")


def test_nombre_de_mondes_et_empreintes_du_code():
    assert ms.verifier_nombre_de_mondes("M_bien", 2625, 2625)
    with pytest.raises(GardeArret):
        ms.verifier_nombre_de_mondes("M_bien", 2400, 2625)
    e = ms.empreintes_code()
    assert "monde_v2.py" in e and "invocation_unique_v2.py" in e and "pole/recombinaison.py" in e
    assert ms.verifier_empreintes_code(e)
    with pytest.raises(GardeArret):
        ms.verifier_empreintes_code({**e, "bras_v2.py": "0" * 64})


def test_reproduction_des_temoins_sain_et_artefact():
    sain = {"b": 0.20, "a": 0.15, "c": 0.15, "d1": 0.24}
    assert all(e["dans"] for e in ms.verifier_reproduction("NR_bien", sain).values())
    with pytest.raises(GardeArret):
        ms.verifier_reproduction("NR_bien", {**sain, "d1": 0.30})          # 0,30 > 0,249 + 0,02
    # tout juste dans la marge de S12 : 0,215 + 0,02 = 0,235 pour b en « bien »
    assert ms.verifier_reproduction("NR_bien", {**sain, "b": 0.2349})
    with pytest.raises(GardeArret):
        ms.verifier_reproduction("NR_bien", {**sain, "b": 0.2351})


def test_vecteur_nul_rapporte_par_monde():
    w = monde_jouet([0, 0, 1, 1, 2, 2, 3],
                    [{"op:x", "co:A"}, {"op:y", "co:A"}, {"op:x", "co:B"}, {"op:y"}, {"op:x", "co:B"},
                     {"op:y", "co:A"}, {"op:z"}])
    r = ms.executer_monde(w, "M_bien", RV, INDICE_ESSAI, ["N", "b"])
    assert r["exclu"] or r["vecteurs_nuls"] == 2      # les articles 3 et 6 n'ont aucune étiquette de concept


def test_pivots_non_positifs_rapportes_par_monde_pour_les_noyaux_de_paires():
    i = INDICE_ESSAI + 2
    r = ms.executer_monde(mo.generer("M_bien", RV, i), "M_bien", RV, i, ["N_dpp", "N_dpp_beta0"])
    if not r["exclu"]:
        assert r["rapport"]["N_dpp_pivots_non_positifs"] == 0 and r["rapport"]["N_dpp_beta0_pivots_non_positifs"] == 0


# --- identité de la forme corrigée avec v1 (bras complet, pas seulement l'ordre) -----------------------------------

def test_bras_a_identique_a_corrige_de_v1_sur_50_mondes_nr():
    import methodes_v1 as mt
    import monde_v1 as m1
    for k in range(50):
        cond = "NR_bien" if k % 2 else "NR_moyen"
        i = INDICE_ESSAI + 100 + k
        w = mo.generer(cond, RV, i)
        graine = int(gr.sequence(RV, gr.CODES_CONDITION[cond], i, gr.ROLE_MONDE).generate_state(1)[0])
        w1 = m1.generer({"niveau": "bien" if cond == "NR_bien" else "moyen"}, graine)
        assert list(w.obs.valides) == list(w1["valides"])
        assert br.bras_a(w.obs, None, {}) == mt.corrige(w1, [a["q"] for a in w1["arts"]])


# --- analyse (sur tableaux synthétiques) ------------------------------------------------------------------------

def _lignes_synthetiques(cond, n, rng, decalage=0.0):
    out = []
    for i in range(n):
        bras = {}
        for b in an.BRAS_PRECISION:
            if b in ms.NON_APPLICABLES.get(cond, ()):
                continue
            p = float(rng.integers(0, 13)) / 12
            bras[b] = {"precision": p, "precision_placebo": float(rng.integers(0, 13)) / 12, "n_complete": 0,
                       "sortie_vide": False}
        out.append({"indice": i, "exclu": None, "n_champs": int(rng.choice([2, 3, 4])), "tentatives": 0,
                    "replantations": 0, "n_valides": 100, "n_vrais_valides": 5, "n_vrais": 6, "bras": bras,
                    "empreinte_latents": None if cond.startswith("NR_") else f"latents-{i}",
                    "concordance_verite": None if cond.startswith("NR_") else (9, 10)})
    return out


def test_analyse_et_lecture_sur_donnees_synthetiques_sans_monde():
    rng = np.random.default_rng(0)
    par = {c: _lignes_synthetiques(c, 40, rng) for c in gr.CODES_CONDITION}
    assert an.CODE_CONTRASTE_NR == 16                               # Q-03 décidée (R-585, R-600)
    with pytest.MonkeyPatch.context() as m:
        m.setattr(an, "CODE_CONTRASTE_NR", None)
        with pytest.raises(GardeArret):
            an.calculer_tout(par, RV)                              # garde gardée : code non fixé, arrêt
    plat = an.calculer_tout(par, RV)                                # code 16
    c = an.charger_pour_lecture(plat)
    for X in le.X2:
        for k in ("N-b", "N-a", "N-d1", "N-d1c", "N-b_eloigne", "N-N_beta0", "d1c-c", "N-N_filtre", "N-N_PCg",
                  "N_PCg-N_beta0", "r_N_b"):
            assert (k, X) in c
    for k in ("SP:N-b", "SP:N-d1c", "SP:N-N_beta0"):
        assert ("lb99" in c[(k, "SP")]) and ("ub99" in c[(k, "SP")])
    for k in (("INV-M_bien", "INV"), ("V_fuite-M_bien", "V_fuite"), ("N-N_beta0", "M_inertes"), ("N-b", "NR_bien"),
              ("N-b", "NR_moyen"), ("fonds_1ou2-M_bien", "M_fonds_1ou2"), ("ecart_M_bien-M_inertes", "M_inertes")):
        assert k in c
    assert plat["N-d1c|V_concepts_absents"] == {"non_applicable": True}
    b = le.booleens(c)                                              # toutes les clés attendues par lecture_v2 existent
    assert isinstance(le.table1(b, True, False, False, False)[0], (int, str))
    assert isinstance(le.table2(b, True, False, False, False)[0], int)
    json.dumps(plat)                                                # sérialisable


def test_graines_de_reechantillonnage_des_contrastes():
    rng = np.random.default_rng(1)
    la, lb = _lignes_synthetiques("INV", 30, rng), _lignes_synthetiques("M_bien", 50, rng)
    r = an.ecart_entre_conditions(la, lb, RV, 5, 14, "N", "b")
    da, db = an.deltas(la, "N", "b"), an.deltas(lb, "N", "b")
    ref = ms.ecart_entre_ensembles(list(da.values()), list(db.values()),
                                   np.random.default_rng(np.random.SeedSequence(entropy=RV, spawn_key=(5, 14, 99))),
                                   np.random.default_rng(np.random.SeedSequence(entropy=RV, spawn_key=(5, 14, 99, 1))))
    assert r == ref
    # contraste 10 : un seul flux (1, 10, 99) pour l'écart apparié
    lm, li = _lignes_synthetiques("M_bien", 30, rng), _lignes_synthetiques("M_inertes", 30, rng)
    r10 = an.ecart_apparie_inertes(lm, li, RV)
    d = np.array([an.deltas(lm, "N", "N_beta0")[k] - an.deltas(li, "N", "N_beta0")[k] for k in range(30)])
    ref10 = ms.ecart_apparie(d, np.zeros_like(d), np.random.default_rng(np.random.SeedSequence(entropy=RV, spawn_key=(1, 10, 99))))
    assert r10["lb95"] == ref10["lb95"] and r10["estimation"] == ref10["estimation"]


# --- balayage statique : tous les modules de bras ---------------------------------------------------------------

def test_balayage_sur_les_modules_livres_et_artefacts_dynamiques():
    assert ba.exiger_propre([ICI.parent / m for m in ba.MODULES_BRAS])
    assert ba.problemes("def f(o):\n    return getattr(o, 'vr' + 'ais')\n")
    assert ba.problemes("def f(o):\n    return o.__dict__\n")
    assert ba.problemes("def f(o):\n    return o['vrais']\n")


# --- validation (plomberie seulement ; valeurs ni imprimées ni lues) --------------------------------------------

def test_validation_plomberie_sur_mondes_d_essai():
    ws = list(va.mondes("M_bien", RV, range(INDICE_ESSAI + 200, INDICE_ESSAI + 204)))
    assert set(va.v1_cosinus(ws)) == {"meme", "proche", "eloigne"}
    assert set(va.v2_fuite(ws, RV, INDICE_ESSAI + 200)) == {"F", "F_nulle"}
    assert isinstance(va.v3_queue(ws), float)
    assert va.v6_vraies_paires(ws) >= 0
    assert "mecanismes_par_monde" in va.v8_rapport(ws, "M_bien")
    assert isinstance(va.v7_rapport(ws), dict)
    ws30 = list(va.mondes("M_bien", RV, range(INDICE_ESSAI + 300, INDICE_ESSAI + 330)))
    assert va.v5_rarete(ws30)["ecart_max"] >= 0
    ranks = va.rangs([3, 1, 1, 2])
    assert list(ranks) == [4.0, 1.5, 1.5, 3.0] and abs(va.spearman([1, 2, 3, 4], [10, 20, 30, 50]) - 1.0) < 1e-12
    with pytest.raises(GardeArret):
        va.spearman([1, 1, 1], [1, 2, 3])


def test_v9_ne_calcule_que_d1c_et_c_et_ne_rend_qu_un_booleen():
    def interdit(obs, rng, aux):
        raise AssertionError("V9 a exécuté un bras candidat")
    f = {**br.FONCTIONS, **{b: interdit for b in br.FONCTIONS if b not in ("d1c", "c")}}
    j = va.v9_j_miroirs(RV, range(INDICE_ESSAI + 400, INDICE_ESSAI + 430), fonctions=f)
    assert isinstance(j, bool)


def test_v4_jumelle_refusee_sans_lecture_confirmee_puis_latents_egaux():
    with pytest.raises(GardeArret):
        va.v4_jumelles(RV, range(INDICE_ESSAI, INDICE_ESSAI + 2))
    with pytest.raises(GardeArret):
        va.v4_jumelles(RV, range(INDICE_ESSAI, INDICE_ESSAI + 2), lecture="echange_ponts")   # lecture remplacée (R-600)
    for m in range(INDICE_ESSAI, INDICE_ESSAI + 3):
        w, j = mo.generer("M_bien", RV, m), mo.generer("M_bien", RV, m, surcharge={"jumelle": True})
        assert mo.empreinte_latents(w) == mo.empreinte_latents(j)
        assert w.obs.etiq_co == j.obs.etiq_co and w.obs.etiq_op == j.obs.etiq_op      # absence de couplage dans le code
    r = va.v4_jumelles(RV, range(INDICE_ESSAI, INDICE_ESSAI + 3), lecture=va.LECTURE_V4)
    assert r["concordance"] == 1.0 and r["variation_cos"] > 0.0    # la variation n'est pas lue au-delà de « non nulle »


def test_validation_seuils_sain_et_artefact():
    ok = {"V1": {"meme": 0.54, "proche": 0.28, "eloigne": 0.03}, "V3": 0.05, "V5": {"ecart_max": 0.2}, "V6": 7.0,
          "plafond_oracle": 0.5, "V2": {"F": 0.05}}
    r = {"M_bien": ok, "M_moyen": dict(ok, plafond_oracle=0.4), "jumelles": {"concordance": 1.0, "variation_cos": 0.3}}
    assert all(va.evaluer_seuils(r).values())
    r2 = {**r, "M_bien": dict(ok, V1={"meme": 0.54, "proche": 0.35, "eloigne": 0.03}, V6=1.0)}
    s = va.evaluer_seuils(r2)
    assert not s["V1_M_bien"]


# --- l'invocation unique : ordre, comptes, prérequis (exécuteur synthétique, aucun monde) ------------------------

def _manifeste_sans_git(depot, run_id, config, taches, **kw):
    """Substitut d'essai de manifeste.creer_manifeste (qui exige un dépôt git propre) : même contenu, même scellement."""
    import hashlib
    from pathlib import Path
    d = Path(depot) / "runs" / run_id
    d.mkdir(parents=True)
    corps = {"run_id": run_id, "cree_le": datetime.now(timezone.utc).isoformat(timespec="seconds"), "config": config,
             "config_sha256": hashlib.sha256(man.config_canonique(config)).hexdigest()}
    p = d / "manifeste.json"
    p.write_text(json.dumps(corps, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sceller(p)
    return p, corps


class Executeur:
    """Exécuteur synthétique : rend des lignes sans monde ; consigne les appels (pour l'ordre)."""
    def __init__(self, tmp, sigma_bien=11.0, sigma_moyen=16.0):
        self.appels, self.tmp, self.rng = [], tmp, np.random.default_rng(5)

    def __call__(self, cond, racine, indices, bras=None, processus=1, aux_extra=None, rapport=None):
        if not self.appels:
            time.sleep(1.1)   # l'horodatage du manifeste est à la seconde : le premier résultat doit lui être postérieur
        self.appels.append((cond, racine, len(list(indices)), (self.tmp / "runs").exists()))
        lignes = _lignes_synthetiques(cond, len(list(indices)), self.rng)
        for l in lignes:
            for b, m in l["bras"].items():
                m["_paires"] = list(range(12))
        return lignes


def _prerequis_factices(depot, validation, reproduction, audit_rendu, code_contraste_nr):
    if code_contraste_nr is None:
        raise GardeArret("code de contraste de la non-régression non fixé")
    return {}


def _etape1_factice(sigmas):
    def f(processus, rapport=None, executer=None):
        s9 = {}
        for c, sg in sigmas.items():
            n_prime, plafond = ms.extension_s9(inv.N_GELES[c], sg)
            s9[c] = {"n": inv.N_GELES[c], "sigma_chapeau": sg, "n_prime": n_prime, "plafond": plafond}
        return s9, {"moyenne_delta_N_b_validation": {}, "grille_ecarts_a_e8_beta1": {}}
    return f


def _petits_nombres(monkeypatch):
    # mondes en nombre réduit : l'ordre et les comptes sont ce que l'on éprouve, pas la taille
    monkeypatch.setattr(inv, "N_GELES", {k: 6 for k in inv.N_GELES})
    monkeypatch.setattr(ms, "TAUX_ARRET", 1.0)


def test_invocation_sain_manifeste_avant_tout_resultat_et_comptes(tmp_path, monkeypatch):
    _petits_nombres(monkeypatch)
    ex = Executeur(tmp_path)
    monkeypatch.setattr(ms, "verifier_reproduction", lambda c, m: {})
    monkeypatch.setattr(ms, "verifier_plafond_oracle", lambda m, c: True)
    res = inv.invocation(tmp_path, "20261101-000000-essai", 2, "v", "r", None, executer=ex,
                         etape1_fn=_etape1_factice({"M_bien": 11.0, "M_moyen": 16.0}),
                         creer_manifeste=_manifeste_sans_git, code_contraste_nr=1,
                         verifier_prerequis_fn=_prerequis_factices)
    # n' : σ̂ = 16 donne ⌈6 × (16 / 15,3)²⌉ = 7 ; M_inertes reprend le n' de M_bien (6)
    assert res["comptes"]["M_moyen"] == 7 and res["comptes"]["M_bien"] == 6 and res["comptes"]["M_inertes"] == 6
    assert all(a[3] for a in ex.appels)                              # le dossier du manifeste existait à chaque appel
    assert [a[0] for a in ex.appels] == inv.CONDITIONS and all(a[1] == gr.RACINE for a in ex.appels)
    viol = ms.verifier_ordre(res["manifeste"], [f for f in res["fichiers"] if "resultats-" in f], res["comptes"])
    assert viol == []
    # artefacts du contrôle du lecteur : nombre de mondes exécuté différent, ou manifeste réécrit avec un autre n'
    assert ms.verifier_ordre(res["manifeste"], [f for f in res["fichiers"] if "resultats-" in f],
                             {**res["comptes"], "M_bien": 5})


def test_invocation_prerequis_manquant_arrete_avant_tout_monde(tmp_path, monkeypatch):
    monkeypatch.setattr(an, "CODE_CONTRASTE_NR", None)              # artefact : code de la non-régression absent
    ex = Executeur(tmp_path)
    with pytest.raises(GardeArret):
        inv.invocation(tmp_path, "20261101-000001-essai", 2, "v", "r", None, executer=ex,
                       etape1_fn=_etape1_factice({"M_bien": 11.0, "M_moyen": 11.0}),
                       creer_manifeste=_manifeste_sans_git, code_contraste_nr=None,
                       verifier_prerequis_fn=_prerequis_factices)
    assert ex.appels == [] and not (tmp_path / "runs").exists()      # rien n'a tourné, aucun manifeste


def test_invocation_nombre_de_mondes_different_arrete(tmp_path, monkeypatch):
    _petits_nombres(monkeypatch)
    ex = Executeur(tmp_path)
    original = ex.__call__

    def court(cond, racine, indices, **kw):
        lignes = original(cond, racine, indices, **kw)
        return lignes[:-1] if cond == "SP" else lignes
    with pytest.raises(GardeArret):
        inv.invocation(tmp_path, "20261101-000002-essai", 2, "v", "r", None, executer=court,
                       etape1_fn=_etape1_factice({"M_bien": 11.0, "M_moyen": 11.0}),
                       creer_manifeste=_manifeste_sans_git, code_contraste_nr=1,
                       verifier_prerequis_fn=_prerequis_factices)


def test_invocation_code_modifie_en_cours_de_run_arrete(tmp_path, monkeypatch):
    _petits_nombres(monkeypatch)
    ex = Executeur(tmp_path)
    vrai = ms.empreintes_code
    monkeypatch.setattr(ms, "empreintes_code", lambda: vrai())
    suite = {"n": 0}

    def derive():
        suite["n"] += 1
        e = vrai()
        if suite["n"] > 1:
            e["bras_v2.py"] = "f" * 64                               # code différent entre deux sessions d'un même run
        return e
    monkeypatch.setattr(ms, "empreintes_code", derive)
    with pytest.raises(GardeArret):
        inv.invocation(tmp_path, "20261101-000003-essai", 2, "v", "r", None, executer=ex,
                       etape1_fn=_etape1_factice({"M_bien": 11.0, "M_moyen": 11.0}),
                       creer_manifeste=_manifeste_sans_git, code_contraste_nr=1,
                       verifier_prerequis_fn=_prerequis_factices)


def test_prerequis_reels_refusent_validation_non_passee(tmp_path, monkeypatch):
    monkeypatch.setattr(inv, "exiger_addendum_scelle", lambda depot: "0" * 64)   # addendum : essai à part (corrections)
    v = tmp_path / "validation.json"
    v.write_text(json.dumps({"seuils": {"V1_M_bien": False}}))
    sceller(v)
    r = tmp_path / "rep.json"
    r.write_text(json.dumps({"reproduction_passee": True}))
    sceller(r)
    with pytest.raises(GardeArret):
        inv.verifier_prerequis(inv.DEPOT, v, r, None, 1)             # validation du générateur non passée
    with pytest.raises(GardeArret):
        inv.verifier_prerequis(inv.DEPOT, v, r, None, None)          # code de contraste NR non fixé
