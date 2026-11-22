"""Pièce 1 — registre de tirage et engagement (garde G2) : cas sain, artefacts, aucun repli, graines."""
import json

import numpy as np
import pytest

from controle_ia.hasard_defenseur_v2 import registre_v2 as R
from controle_ia.hasard_defenseur_v2.erreurs_v2 import RefusEngagement, RefusGraine, RefusPlan
from controle_ia.hasard_defenseur_v2.puissance_v2 import ETIQUETTES_SIMULEES as ETIQ

ENT = 0x1234_5678_9ABC
IDS = [f"tache-{i}" for i in range(5)]


def test_g2_cas_sain_registre_conforme(tmp_path):
    plan = R.tirer_plan(ENT, IDS, ETIQ)
    cr, ce = R.engager(plan, tmp_path, "essai")
    relu = R.verifier_engagement(cr, ce, entropie_revelee=ENT)
    assert np.array_equal(relu.conditions, plan.conditions)
    assert relu.graines == plan.graines
    texte = cr.read_text(encoding="utf-8") + ce.read_text(encoding="utf-8")
    assert str(ENT) not in texte and f"{ENT:x}" not in texte  # l'entropie racine n'est écrite nulle part avant la révélation
    for t in range(len(IDS)):
        assert np.bincount(plan.conditions[t], minlength=3).tolist() == [2, 2, 2]


def test_g2_artefact_registre_modifie_apres_coup(tmp_path):
    plan = R.tirer_plan(ENT, IDS, ETIQ)
    cr, ce = R.engager(plan, tmp_path, "essai")
    d = json.loads(cr.read_text(encoding="utf-8"))
    e0 = d["taches"][0]["emplacements"]
    e0[0]["condition"], e0[1]["condition"] = e0[1]["condition"], e0[0]["condition"]
    cr.write_text(json.dumps(d), encoding="utf-8")
    with pytest.raises(RefusEngagement):
        R.verifier_engagement(cr, ce)


def test_g2_artefact_graine_absente():
    plan = R.tirer_plan(ENT, IDS, ETIQ)
    d = R.registre_en_dict(plan)
    del d["taches"][2]["emplacements"][3]["graine_agent"]
    with pytest.raises(RefusGraine):
        R.plan_depuis_dict(d)


def test_g2_artefact_rejeu_avec_une_autre_entropie(tmp_path):
    plan = R.tirer_plan(ENT, IDS, ETIQ)
    cr, ce = R.engager(plan, tmp_path, "essai")
    with pytest.raises(RefusEngagement):
        R.verifier_engagement(cr, ce, entropie_revelee=ENT + 1)


def test_g2_artefact_code_different_du_code_engage(tmp_path):
    from controle_ia import scellement

    plan = R.tirer_plan(ENT, IDS, ETIQ)
    cr = tmp_path / "x-registre.json"
    cr.write_text(R.texte_registre(plan), encoding="utf-8")
    ce = tmp_path / "x-engagement.json"
    ce.write_text(json.dumps({"version": R.VERSION_ENGAGEMENT, "registre": cr.name, "empreinte_registre": scellement.empreinte(cr),
                              "empreinte_code": "0" * 64, "empreintes_modules": {}}), encoding="utf-8")
    scellement.sceller(cr)
    scellement.sceller(ce)
    with pytest.raises(RefusEngagement):
        R.verifier_engagement(cr, ce)


def test_aucun_repli_silencieux(tmp_path):
    with pytest.raises(RefusGraine):
        R.tirer_plan(None, IDS, ETIQ)
    with pytest.raises(RefusPlan):
        R.tirer_plan(ENT, IDS, ETIQ, k=1)
    with pytest.raises(RefusPlan):
        R.tirer_plan(ENT, ["a", "a"], ETIQ)
    with pytest.raises(RefusPlan):
        R.tirer_plan(ENT, IDS, {"E": "x", "D": "x", "U": "y"})
    plan = R.tirer_plan(ENT, IDS, ETIQ)
    R.engager(plan, tmp_path, "essai")
    with pytest.raises(RefusEngagement):
        R.engager(plan, tmp_path, "essai")  # R12 : on n'écrase jamais
    d = R.registre_en_dict(plan)
    del d["ordre_passage"]
    with pytest.raises(RefusEngagement):
        R.plan_depuis_dict(d)


def test_graines_cles_distinctes_conditions_et_agent():
    plan = R.tirer_plan(ENT, IDS, ETIQ, nb_mots_agent=4)
    for t in range(len(IDS)):
        rng = np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=(0, t)))
        assert np.array_equal(plan.conditions[t], rng.permutation(R.base_conditions(2)))
        for e in range(6):
            mots = np.random.SeedSequence(ENT, spawn_key=(1, t, e)).generate_state(2, np.uint64)
            assert plan.graines[t][e] == R.graine_hex(mots)
    # la graine consignée ne dépend pas du nombre de mots d'agent demandés (cohérence par préfixe)
    assert R.tirer_plan(ENT, IDS, ETIQ, nb_mots_agent=0).graines == plan.graines
    # clés distinctes : le flux des conditions n'est pas celui de l'agent
    a = np.random.SeedSequence(ENT, spawn_key=(0, 0)).generate_state(2, np.uint64)
    b = np.random.SeedSequence(ENT, spawn_key=(1, 0, 0)).generate_state(2, np.uint64)
    assert not np.array_equal(a, b)
    assert len({g for l in plan.graines for g in l}) == len(IDS) * 6
