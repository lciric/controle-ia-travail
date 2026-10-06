"""Pilote de l'environnement (a) (T0.5), sur modèle jouet : plan des épisodes, jeu par lots, notation, appariement."""
from __future__ import annotations

import json

import numpy as np
import pytest
import torch

from controle_ia.environnements import pilote_a as pa
from controle_ia.gardes import GardeArret
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import modele_jouet, regler_determinisme, tokeniseur_caracteres_chat
from controle_ia.manifeste import generateur, graines
from controle_ia.scellement import sceller

regler_determinisme(1)
TOK = tokeniseur_caracteres_chat()
FMT = FormatChat(TOK, fins={TOK.convert_tokens_to_ids("<|im_end|>"), TOK.eos_token_id})
CONFIG = {"N": 1, "T": 2, "episodes_par_tache": 2, "lot": 3, "max_nouveaux": 6, "temperature": 1.0,
          "couches": [0, 1, 2], "fraction_equivalence": 0.5, "statistique_equivalence": "max",
          "tolerance_equivalence": 1e-4}
TACHES = [{"identifiant": "2506.00001v1", "questions": "Why do routers matter?",
           "classification": {"theory_experiment": "mostly_experiments", "data_type": "real_only", "domains": []}},
          {"identifiant": "2506.00002v1", "questions": "How to calibrate?", "classification": None}]


def _modele():
    return modele_jouet(5, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)


def _generateurs(plan, entropie=7):
    g = graines([e for e, _ in plan], entropie)
    return {e: generateur(g[e]) for e, _ in plan}


def test_config_incomplete_arrete():
    pa.exiger_config(CONFIG)
    with pytest.raises(GardeArret, match="incomplète"):
        pa.exiger_config({k: v for k, v in CONFIG.items() if k != "lot"})


def test_charger_taches(tmp_path):
    f = tmp_path / "taches.json"
    f.write_text(json.dumps({"taches": TACHES}), encoding="utf-8")
    with pytest.raises(GardeArret):
        pa.charger_taches(f)  # non scellé
    sceller(f)
    assert [t["identifiant"] for t in pa.charger_taches(f)] == ["2506.00001v1", "2506.00002v1"]
    for contenu, motif in [({"taches": TACHES + TACHES[:1]}, "double"),
                           ({"taches": [{"identifiant": "x", "questions": " "}]}, "sans énoncé")]:
        g = tmp_path / f"t-{motif[:4]}.json"
        g.write_text(json.dumps(contenu), encoding="utf-8")
        sceller(g)
        with pytest.raises(GardeArret, match=motif):
            pa.charger_taches(g)


def test_plan_et_graines_deterministes():
    plan = pa.plan_des_episodes(TACHES, 2)
    assert [e for e, _ in plan] == ["2506.00001v1/e0", "2506.00001v1/e1", "2506.00002v1/e0", "2506.00002v1/e1"]
    a = pa.graines_des_actions(_generateurs(plan)["2506.00001v1/e0"], 2, 3)
    b = pa.graines_des_actions(_generateurs(plan)["2506.00001v1/e0"], 2, 3)
    assert a == b and sorted(a) == [(i, t) for i in range(2) for t in range(3)]
    with pytest.raises(GardeArret):
        pa.plan_des_episodes(TACHES, 0)


def test_jouer_pilote_par_lots_et_rejeu():
    plan = pa.plan_des_episodes(TACHES, 2)
    m = _modele()
    fiches, vecteurs = pa.jouer_pilote(m, FMT, plan, _generateurs(plan), CONFIG)
    assert [f["episode"] for f in fiches] == [e for e, _ in plan]
    assert all(f["bilan"]["actions"] == 2 for f in fiches) and sum(len(f["equivalence"]["actions"]) for f in fiches) > 0
    assert set(vecteurs) == {f"{e}|{c}" for e, _ in plan for c in CONFIG["couches"]}
    assert vecteurs["2506.00001v1/e0|1"].shape == (1, 2, 32) and vecteurs["2506.00001v1/e0|1"].dtype == np.float16
    rejeu, _ = pa.jouer_pilote(m, FMT, plan, _generateurs(plan), CONFIG)
    assert [f["empreintes"] for f in rejeu] == [f["empreintes"] for f in fiches]


def test_jouer_pilote_generateur_manquant_arrete():
    plan = pa.plan_des_episodes(TACHES, 1)
    with pytest.raises(GardeArret, match="générateurs absents"):
        pa.jouer_pilote(_modele(), FMT, plan, {}, CONFIG)


def test_noter_ensembles_sans_imputation():
    demandes = [{"cle": f"j{k}", "questions": "Why?", "ensemble": "PROPOSAL 1: x", "classification": None,
                 "variante": v} for k, v in enumerate(["b0", "b*"])]
    sorties = pa.noter_ensembles(_modele(), FMT, demandes, {"j0": 1, "j1": 2}, lot=2, max_nouveaux=5, temperature=1.0)
    assert [s["cle"] for s in sorties] == ["j0", "j1"]
    assert all(s["score"] is None and s["anomalies"] and s["jetons_reponse"] <= 5 for s in sorties)


def test_logits_independants_du_remplissage():
    m = _modele()
    contextes = [FMT.ouverture("s", "court"), FMT.ouverture("système plus long", "observation bien plus longue")]
    lot = pa.logits_derniere_position(m, contextes, TOK.pad_token_id)
    seuls = torch.cat([pa.logits_derniere_position(m, [c], TOK.pad_token_id) for c in contextes])
    assert torch.allclose(lot, seuls, atol=1e-5)
    with pytest.raises(GardeArret):
        pa.logits_derniere_position(m, [[]], TOK.pad_token_id)


def test_jetons_oui_non():
    with pytest.raises(GardeArret, match="un seul jeton"):
        pa.jetons_oui_non(TOK)  # tokeniseur par caractères : « Yes » fait trois jetons

    class Tok:
        def encode(self, s, add_special_tokens=False):
            return {"Yes": [7], "No": [9]}[s]

    assert pa.jetons_oui_non(Tok()) == (7, 9)


def test_apparier_probabilites(monkeypatch):
    monkeypatch.setattr(pa, "jetons_oui_non", lambda tok: (TOK.convert_tokens_to_ids("Y"), TOK.convert_tokens_to_ids("N")))
    paires = [{"cle": f"p{k}", "proposition": "Train a dense baseline.", "cible": c}
              for k, c in enumerate(["a dense baseline", "an ablation"])]
    s = pa.apparier(_modele(), FMT, paires, lot=2)
    assert [x["cle"] for x in s] == ["p0", "p1"] and all(0.0 <= x["p_oui"] <= 1.0 and x["masse_oui_non"] > 0 for x in s)
