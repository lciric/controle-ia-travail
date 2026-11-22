"""Compléments de la contre-lecture (classe B) : les six essais de l'annexe (mutations survivantes de la v1), portés sur
la v2, et les essais des corrections des constats 4 et 5."""
import json

import numpy as np
import pytest

from controle_ia import scellement
from controle_ia.hasard_defenseur_v2 import contraste_v2 as C
from controle_ia.hasard_defenseur_v2 import gardes_v2 as G
from controle_ia.hasard_defenseur_v2 import monde_v2 as M
from controle_ia.hasard_defenseur_v2 import permutation_v2 as K
from controle_ia.hasard_defenseur_v2 import puissance_v2 as P
from controle_ia.hasard_defenseur_v2 import registre_v2 as R
from controle_ia.hasard_defenseur_v2.erreurs_v2 import RefusEngagement, RefusGraine, RefusLecture
from controle_ia.hasard_defenseur_v2.puissance_v2 import ETIQUETTES_SIMULEES as ETIQ

ENT = 0x1234_5678_9ABC
IDS = [f"tache-{i}" for i in range(5)]


# ---------------------------------------------------------------- annexe de la contre-lecture (constats 1, 2, 3, 6, 7, 8)

def test_g2_artefact_registre_rescelle_conditions_echangees(tmp_path):
    plan = R.tirer_plan(ENT, IDS, ETIQ)
    cr, ce = R.engager(plan, tmp_path, "essai")
    d = json.loads(cr.read_text(encoding="utf-8"))
    e0 = d["taches"][0]["emplacements"]
    iE = next(i for i, x in enumerate(e0) if x["condition"] == "E")
    iU = next(i for i, x in enumerate(e0) if x["condition"] == "U")
    e0[iE]["condition"], e0[iU]["condition"] = "U", "E"
    cr.write_text(json.dumps(d, ensure_ascii=False, sort_keys=True, indent=1) + "\n", encoding="utf-8")
    eng = json.loads(ce.read_text(encoding="utf-8"))
    eng["empreinte_registre"] = scellement.empreinte(cr)
    ce.write_text(json.dumps(eng, ensure_ascii=False, sort_keys=True, indent=1) + "\n", encoding="utf-8")
    for p in (cr, ce):
        (p.parent / (p.name + ".sha256")).unlink()
        scellement.sceller(p)
    R.verifier_engagement(cr, ce)  # sans entropie, un faux rescellé passe : l'ancre est l'empreinte publiée
    with pytest.raises(RefusEngagement, match="conditions"):
        R.verifier_engagement(cr, ce, entropie_revelee=ENT)


def test_g2_graine_partagee_refusee_par_le_registre():
    plan = R.tirer_plan(ENT, IDS, ETIQ)
    plan.graines[1][0] = plan.graines[0][0]
    with pytest.raises(RefusGraine):
        R.verifier_plan_structure(plan)


def test_p_tirage_phipson_smyth_et_exacte():
    t_b = np.array([0.0, 1.0, 2.0, 3.0])
    assert K.p_valeur(2.0, t_b, "tirage") == pytest.approx(3 / 5)
    assert K.p_valeur(9.0, t_b, "tirage") == pytest.approx(1 / 5)  # jamais nulle
    assert K.p_valeur(2.0, t_b, "exact") == pytest.approx(2 / 4)


def test_g7_maximum_conjoint_egal_au_calcul_a_la_main():
    plan = R.tirer_plan(4242, [f"t{i}" for i in range(50)], ETIQ, nb_mots_agent=M.NB_MOTS_MONDE)
    m = M.simuler_monde(plan, 2, M.ParametresMonde(0.10, 0.0, 0.0, 1.0, 0.10))
    tir = K.tirages_du_plan(plan, 4242, B=499, simulation=True)
    o = "jumeau_sensible"
    sec = {"sonde": m.sonde[o], "trait": m.trait[o], "issue_nulle": m.Y["jumeau_insensible"]}
    ps = G.maximum_conjoint(sec, tir, {n: K.stat_dirigee for n in sec})
    std = {}
    for n, y in sec.items():
        t_b = K.stat_dirigee(y, tir.affectations, tir.k)
        t_o = K.stat_dirigee(y, tir.observe[None], tir.k)[0]
        std[n] = (abs(t_o - t_b.mean()) / t_b.std(), np.abs(t_b - t_b.mean()) / t_b.std())
    maxi = np.max([v[1] for v in std.values()], axis=0)
    brute = {}
    for n, (v, propre) in std.items():
        tol = 1e-9 * max(1.0, v)
        assert ps[n].valeur == pytest.approx((1 + np.sum(maxi >= v - tol)) / (maxi.shape[0] + 1))
        brute[n] = (1 + np.sum(propre >= v - tol)) / (maxi.shape[0] + 1)
    assert any(ps[n].valeur > brute[n] for n in sec)  # la correction mord au moins une fois


def test_perception_absente_refusee_meme_sans_rejet():
    with pytest.raises(RefusLecture):
        C.regle_paragraphe_3(0.2, 0.2, 0.2, None)


def test_g5_sain_contre_le_jumeau_sensible():
    cas = P.cas_g5_sain()
    assert cas.jumeau == "jumeau_sensible" and cas.params.delta_J == 0.10 and cas.params.delta == 0.25
    assert cas.params.r == 1.0 and cas.params.rho == 0.0 and not cas.params.uniformes_communes and cas.N == 300


# ---------------------------------------------------------------- corrections portées (constats 4 et 5)

def test_constat_4_variance_d_arrondi_tenue_pour_nulle():
    L = np.array([[[0, 0, 1, 1, 2, 2]]], dtype=np.int8)
    z = np.array([[0.3, 0.3, 0.0, 0.0, 0.977, 0.977]])
    assert C.stat_studentisee(z, L, 2)[0] == pytest.approx((0.977 - 0.3) * 1e6)
    z = np.array([[0.3, 0.5, 0.0, 0.0, 0.977, 0.977]])  # variance réelle sous E : formule ordinaire
    assert C.stat_studentisee(z, L, 2)[0] == pytest.approx((0.977 - 0.4) / np.sqrt(0.02 / 2))


def test_constat_5_entropie_revelee_entier_seul(tmp_path):
    plan = R.tirer_plan(ENT, IDS, ETIQ)
    cr, ce = R.engager(plan, tmp_path, "essai")
    R.verifier_engagement(cr, ce, entropie_revelee=ENT)  # cas sain
    for faux in ([ENT, 0], [ENT], np.int64(ENT), True):
        with pytest.raises(RefusGraine):
            R.verifier_engagement(cr, ce, entropie_revelee=faux)
        with pytest.raises(RefusGraine):
            G.controler_ordre(plan, faux)
