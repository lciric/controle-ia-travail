# -*- coding: utf-8 -*-
"""Tests du module commun : chaque garde est éprouvée sur un cas sain et sur un artefact (R5)."""
import json
from pathlib import Path

import pytest

import m3_commun as m3
import memoire_isvd_plugin_revu as memoire


def _config(tmp_path: Path, **kw) -> m3.Config:
    base = dict(dossier=tmp_path, a_blanc=True, graine=7, max_appels=50, max_jetons_sortie=10_000, nom_run="t")
    base.update(kw)
    return m3.Config(**base)


def _reponse(texte="", statut="ok", raison="end_turn", ok=None, modele_servi="m", lignee="CLAUDE_OPUS_5_5"):
    if ok is None:
        ok = statut == "ok"
    return m3.Reponse(ok=ok, statut=statut, lignee=lignee, modele_demande="m", modele_servi=modele_servi, texte=texte,
                      raison_arret=raison, http=200, erreur=None, jetons_entree=0, jetons_sortie=0, duree_s=0.0,
                      etiquette="e", empreinte_invite="", empreinte_texte=m3.empreinte(texte), tentatives=1,
                      heure_utc="", a_blanc=True, temperature_envoyee=None)


# ---- lignées -------------------------------------------------------------------------------------------------
def test_normaliser_lignee_sain_et_artefact():
    assert m3.normaliser_lignee("gemini-4-argon") == "GEMINI_ARGON"
    assert m3.normaliser_lignee("Claude Opus 5.5") == "CLAUDE_OPUS_5_5"
    with pytest.raises(m3.LigneeInconnue):
        m3.normaliser_lignee("claude-3-5-sonnet")  # aucun repli vers un autre modèle


# ---- extraction de texte : jamais la réflexion -------------------------------------------------------------------
def test_texte_anthropic_ignore_thinking():
    resp = {"content": [{"type": "thinking", "thinking": "secret"}, {"type": "text", "text": "visible"}]}
    assert m3.texte_anthropic(resp) == "visible"
    assert m3.texte_anthropic({"content": [{"type": "thinking", "thinking": "secret"}]}) == ""


def test_texte_gemini_ignore_thought():
    resp = {"candidates": [{"content": {"parts": [{"text": "pensée", "thought": True}, {"text": "visible"}]}}]}
    assert m3.texte_gemini(resp) == "visible"


# ---- client : un seul modèle, échec = échec, journal ------------------------------------------------------------
def test_client_ne_substitue_jamais_et_consigne_l_echec(tmp_path, monkeypatch):
    monkeypatch.setenv("M3_ANTHROPIC_API_KEY", "cle-test-a")
    monkeypatch.setenv("M3_GEMINI_API_KEY", "cle-test-g")
    appels = []

    def transport(url, data, headers, timeout):
        appels.append(json.loads(data.decode("utf-8")).get("model"))
        return 404, '{"error": "not found"}'

    config = _config(tmp_path, a_blanc=False)
    journal = m3.Journal(config.journal)
    client = m3.Client(config, journal, m3.Budget(10, 1000), transport=transport)
    rep = client.appeler("CLAUDE_FABLE_5_1", "bonjour", 0.3, "e1")
    assert rep.ok is False and rep.statut == "echec_api" and rep.http == 404
    assert rep.modele_servi is None and rep.texte == ""
    assert appels == ["claude-fable-5-1"], "un seul modèle appelé, aucune rotation"
    lignes = config.journal.read_text(encoding="utf-8").strip().splitlines()
    assert len(lignes) == 1 and json.loads(lignes[0])["statut"] == "echec_api"


def test_client_consigne_modele_servi_et_jetons(tmp_path, monkeypatch):
    monkeypatch.setenv("M3_ANTHROPIC_API_KEY", "cle-test-a")
    monkeypatch.setenv("M3_GEMINI_API_KEY", "cle-test-g")

    def transport(url, data, headers, timeout):
        corps = {"model": "claude-opus-5-5-20261001", "stop_reason": "end_turn",
                 "content": [{"type": "thinking", "thinking": "x"}, {"type": "text", "text": "Réponse $$a=b+c$$ assez longue."}],
                 "usage": {"input_tokens": 12, "output_tokens": 34}}
        return 200, json.dumps(corps)

    config = _config(tmp_path, a_blanc=False)
    budget = m3.Budget(10, 1000)
    client = m3.Client(config, m3.Journal(config.journal), budget, transport=transport)
    rep = client.appeler("opus", "q", None, "e")
    assert rep.ok and rep.modele_servi == "claude-opus-5-5-20261001" and "x" not in rep.texte
    assert budget.etat()["jetons_sortie"] == 34


def test_client_refuse_cle_rr(tmp_path, monkeypatch):
    monkeypatch.setenv("M3_ANTHROPIC_API_KEY", "meme-cle")
    monkeypatch.setenv("M3_GEMINI_API_KEY", "g")
    monkeypatch.setenv("RR_ANTHROPIC_API_KEY", "meme-cle")
    config = _config(tmp_path, a_blanc=False)
    with pytest.raises(m3.ClesRefusees):
        m3.Client(config, m3.Journal(config.journal), m3.Budget(1, 1))


def test_client_sans_cles_refuse(tmp_path, monkeypatch):
    monkeypatch.delenv("M3_ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("M3_GEMINI_API_KEY", raising=False)
    config = _config(tmp_path, a_blanc=False)
    with pytest.raises(m3.ClesRefusees):
        m3.Client(config, m3.Journal(config.journal), m3.Budget(1, 1))


def test_budget_arrete_au_plafond(tmp_path):
    config = _config(tmp_path, max_appels=2)
    client = m3.Client(config, m3.Journal(config.journal), m3.Budget(2, 10_000))
    client.appeler("GEMINI_ARGON", "a", 0.5, "e1")
    client.appeler("GEMINI_ARGON", "b", 0.5, "e2")
    with pytest.raises(m3.BudgetDepasse):
        client.appeler("GEMINI_ARGON", "c", 0.5, "e3")


def test_a_blanc_est_deterministe(tmp_path):
    textes = []
    for _ in range(2):
        config = _config(tmp_path, graine=11)
        client = m3.Client(config, m3.Journal(config.journal), m3.Budget(100, 10_000))
        textes.append([client.appeler("CLAUDE_OPUS_5_5", "x", 0.4, "e").statut for _ in range(12)])
    assert textes[0] == textes[1]
    assert set(textes[0]) <= {"ok", "vide", "echec_api"}


# ---- blocs LaTeX, analyse spectrale --------------------------------------------------------------------------------
def test_extraire_blocs_latex():
    t = "a $$x+y=z+w$$ b $$x+y=z+w$$ c $$ab$$ d $$\\int_0^1 f$$"
    # dédoublonnage, et les blocs de moins de 7 caractères (`ab`) sont ignorés comme dans les scripts d'origine
    assert m3.extraire_blocs_latex(t) == ["x+y=z+w", "\\int_0^1 f"]


def test_analyse_spectrale_sain_et_artefact():
    r = m3.analyse_spectrale(["$$\\alpha$$ bregman divergence proper", "$$\\beta$$ martingale doob stopping",
                              "$$\\alpha$$ bregman convex potential"])
    assert r["calcule"] is True and r["n_textes"] == 3 and r["capacite_shannon_gram"] > 0
    assert m3.analyse_spectrale(["seul"])["calcule"] is False
    assert m3.analyse_spectrale([])["calcule"] is False


# ---- substrat ------------------------------------------------------------------------------------------------------
def test_sauver_substrat_renvoie_le_dict_et_garde_une_copie(tmp_path):
    chemin = tmp_path / "s.json"
    s = m3.sauver_substrat(chemin, {"a": 1})
    assert isinstance(s, dict) and chemin.exists()
    s2 = m3.sauver_substrat(chemin, {"a": 2})
    assert s2["a"] == 2
    assert any(p.name.endswith(".secours.json") for p in tmp_path.iterdir()), "copie de secours de l'existant"
    with pytest.raises(m3.ErreurEssaim):
        m3.sauver_substrat(chemin, None)


# ---- évaluation : le statut prime -------------------------------------------------------------------------------
def test_evaluer_reponse_vide_et_echec_ne_valent_ni_refus_ni_cooperation():
    e_vide = m3.evaluer_reponse(_reponse("", statut="vide"))
    e_echec = m3.evaluer_reponse(_reponse("", statut="echec_api", modele_servi=None))
    for e in (e_vide, e_echec):
        assert e["refus_de_role_heuristique"] is False and e["cooperation_complete_heuristique"] is False
    r = m3.resumer_bras("A", [e_vide, e_echec])
    assert r["n_ok"] == 0 and r["refus_de_role_pct_sur_ok"] is None and r["cooperation_pct_sur_ok"] is None
    assert r["n_vide"] == 1 and r["n_echec_api"] == 1


def test_evaluer_reponse_ok_cooperation_et_refus():
    coop = m3.evaluer_reponse(_reponse("Preuve : $$D_\\Phi(u\\|q) \\ge 0$$ ; confiance : 0.85"))
    assert coop["cooperation_complete_heuristique"] is True and coop["n_blocs_latex"] == 1
    refus = m3.evaluer_reponse(_reponse("Je ne peux pas adopter l'identité d'un agent fictif. $$a=b$$ q = 0.5"))
    assert refus["refus_de_role_heuristique"] is True and refus["cooperation_complete_heuristique"] is False
    r = m3.resumer_bras("B", [coop, refus])
    assert r["n_ok"] == 2 and r["cooperation_pct_sur_ok"] == 50.0 and r["refus_de_role_pct_sur_ok"] == 50.0


# ---- extraction JSON : jamais le gabarit -------------------------------------------------------------------------
def test_extraction_json_echec_renvoie_listes_vides(tmp_path, monkeypatch):
    monkeypatch.setenv("M3_ANTHROPIC_API_KEY", "a")
    monkeypatch.setenv("M3_GEMINI_API_KEY", "g")

    def transport(url, data, headers, timeout):
        return 200, json.dumps({"model": "claude-opus-5-5", "stop_reason": "end_turn",
                                "content": [{"type": "text", "text": "Je ne renvoie pas de JSON, voici du texte long."}],
                                "usage": {"input_tokens": 1, "output_tokens": 1}})

    config = _config(tmp_path, a_blanc=False)
    client = m3.Client(config, m3.Journal(config.journal), m3.Budget(10, 1000), transport=transport)
    r = m3.extraire_json_structure(client, "invite", ["k1", "k2"], "t")
    assert r["ok"] is False and r["donnees"] == {"k1": [], "k2": []} and len(r["tentatives"]) == 2


def test_extraction_json_succes(tmp_path, monkeypatch):
    monkeypatch.setenv("M3_ANTHROPIC_API_KEY", "a")
    monkeypatch.setenv("M3_GEMINI_API_KEY", "g")

    def transport(url, data, headers, timeout):
        return 200, json.dumps({"model": "claude-opus-5-5", "stop_reason": "end_turn",
                                "content": [{"type": "text", "text": '```json\n{"k1": ["x [A_1]"], "k2": []}\n```'}],
                                "usage": {"input_tokens": 1, "output_tokens": 1}})

    config = _config(tmp_path, a_blanc=False)
    client = m3.Client(config, m3.Journal(config.journal), m3.Budget(10, 1000), transport=transport)
    r = m3.extraire_json_structure(client, "invite", ["k1", "k2"], "t")
    assert r["ok"] is True and r["donnees"] == {"k1": ["x [A_1]"], "k2": []}


# ---- castes --------------------------------------------------------------------------------------------------------
def test_castes_du_substrat_ecarte_les_mal_formees():
    s = {"PRIMORDIAL_MITOSIS_DONE_CACHE": {"castes": [
        {"mode": "MONOCULTURE", "lineages": ["GEMINI_ARGON"], "temp": 0.5},
        {"mode": "HYBRIDE", "lineages": ["claude-3-5-sonnet"], "temp": 0.5},
        {"mode": "MONOCULTURE", "lineages": [], "temp": 0.5}]}}
    c = m3.castes_du_substrat(s)
    assert sum(1 for x in c if "lineages" in x) == 1 and c[-1] == {"_ecartees": 2}
    assert len(m3.selectionner_castes(c, 5)) == 5 and len(m3.selectionner_castes([], 3)) == 3


# ---- mémoire -------------------------------------------------------------------------------------------------------
def test_memoire_assimile_et_projette():
    store = {}
    memoire.assimiler(store, 1, ["texte alpha q=0.9", {"confidence": 0.7, "x": "beta"}])
    etat = store["isvd_state"]
    assert etat["r_max"] == 6 and len(etat["Sigma"]) == 6 and etat["exemplars"]
    assert "\\Sigma" in memoire.projeter(store, 2)
    assert "0}_{16" in memoire.projeter({}, 1)
