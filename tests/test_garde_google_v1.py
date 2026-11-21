"""Essais de la garde commune des réglages de Google, src/controle_ia/garde_google_v1.py (classe B).

Un cas sain et un artefact par contrôle (R5) : un essai par réglage manquant et par motif de fin. Sans réseau.
Lancement : PYTHONPATH=src python -m pytest -q tests/test_garde_google_v1.py
"""
import json
from pathlib import Path

import pytest

from controle_ia import garde_google_v1 as g

RACINE = Path(__file__).resolve().parents[1]


def corps(niveau="high", plafond=65536, budget=None, inclure=True, sans_niveau=False):
    pensee = {} if sans_niveau else {"thinkingLevel": niveau}
    if budget is not None:
        pensee["thinkingBudget"] = budget
    if inclure is not None:
        pensee["includeThoughts"] = inclure
    config = {"thinkingConfig": pensee}
    if plafond is not None:
        config["maxOutputTokens"] = plafond
    return {"contents": [{"role": "user", "parts": [{"text": "x"}]}], "generationConfig": config}


# ---------- avant l'envoi ----------

@pytest.mark.parametrize("espece,niveau,plafond,provision,mode", [
    ("argon", "high", 32768, 16384, "flux"), ("argon", "high", 32768, 16384, "non_diffuse"),
    ("carbon", "high", 65536, 49152, "flux"), ("carbon", "high", 32768, 16384, "non_diffuse"),
    ("neon", "xhigh", 65536, 32768, "flux"), ("neon", "xhigh", 65536, 32768, "non_diffuse")])
def test_sain_par_espece_et_par_mode(espece, niveau, plafond, provision, mode):
    assert g.verifier_reglages_google(espece, corps(niveau, plafond), provision, mots=4000, mode=mode) == []
    assert niveau == g.NIVEAU_MAX_REFLEXION[espece]


@pytest.mark.parametrize("cas,reglage,attendu", [
    ("niveau absent", dict(sans_niveau=True), "thinkingLevel absent"),
    ("niveau non admis", dict(niveau="xhigh"), "non admis"),
    ("niveau plus bas que le plus haut", dict(niveau="medium"), "au lieu de 'high'"),
    ("niveau en majuscules", dict(niveau="HIGH"), "non admis"),
    ("budget avec le niveau", dict(budget=32768), "thinkingBudget présent"),
    ("pensées non incluses", dict(inclure=None), "includeThoughts"),
    ("pensées incluses fausses", dict(inclure=False), "includeThoughts"),
    ("plafond absent", dict(plafond=None), "mal formés"),
    ("plafond flottant", dict(plafond=65536.0), "mal formés"),
    ("plafond au-delà de la limite en flux", dict(plafond=65537), "au-delà de la limite"),
    ("texte sous 16 000", dict(plafond=49152 + 15999), "< 16000"),
])
def test_un_essai_par_reglage_manquant(cas, reglage, attendu):
    problemes = g.verifier_reglages_google("carbon", corps(**reglage), 49152)
    assert any(attendu in p for p in problemes), (cas, problemes)


def test_limites_versees_par_mode():
    # Carbon et Argon : 32 768 en appel non diffusé (liste versée, lignes 612 et 594)
    for espece in ("carbon", "argon"):
        p = g.verifier_reglages_google(espece, corps("high", 32769), 16384, mode="non_diffuse")
        assert any("au-delà de la limite" in x for x in p)
    assert any("au-delà de la limite" in x for x in g.verifier_reglages_google("argon", corps("high", 32769), 16384))
    assert g.verifier_reglages_google("neon", corps("xhigh", 65536), 32768, mode="non_diffuse") == []
    assert "mode d'appel" in g.verifier_reglages_google("carbon", corps(), 49152, mode="lot")[0]


def test_limites_egales_a_la_liste_versee():
    liste = RACINE / "docs" / "notes" / "collisionneur-v9" / "liste-modeles-gemini-20261121T134904Z.json"
    if not liste.exists():
        pytest.skip("liste versée absente")
    modeles = {x["name"]: x for x in json.loads(liste.read_text(encoding="utf-8"))["modeles"]}
    for espece in ("argon", "carbon", "neon"):
        assert g.LIMITES_SORTIE[espece]["non_diffuse"] == modeles[f"models/gemini-4-{espece}"]["outputTokenLimit"]
    assert g.LIMITES_SORTIE["argon"]["flux"] == 32768  # liste versée ; aucun envoi au-delà relevé


def test_provision_nulle_ou_negative_refusee():
    for provision in (0, -1, None, 1.5):
        assert any("mal formés ou nuls" in p for p in g.verifier_reglages_google("neon", corps("xhigh"), provision))


def test_limite_de_mots_bord():
    # Carbon : 65 536 − 49 152 = 16 384 jetons de texte ; 10 239 mots × 1,6 = 16 383 (accepté), 10 240 → 16 384 (refusé)
    assert g.verifier_reglages_google("carbon", corps(), 49152, mots=10239) == []
    assert any("limite de mots" in p for p in g.verifier_reglages_google("carbon", corps(), 49152, mots=10240))


def test_espece_inconnue_refusee():
    assert "rien ne part" in g.verifier_reglages_google("hydrogen", corps(), 49152)[0]


def test_niveau_attendu_explicite():
    assert g.verifier_reglages_google("carbon", corps("medium"), 49152, niveau_attendu="medium") == []
    assert any("au lieu de 'medium'" in p for p in g.verifier_reglages_google("carbon", corps("high"), 49152,
                                                                               niveau_attendu="medium"))


def test_repli_declare_au_budget():
    budget = corps(sans_niveau=True, budget=32768)
    assert g.verifier_reglages_google("carbon", budget, 49152, budget_attendu=32768) == []
    assert any("au lieu du budget prévu" in p for p in g.verifier_reglages_google("carbon", budget, 49152,
                                                                                    budget_attendu=24576))
    assert any("thinkingLevel présent" in p for p in g.verifier_reglages_google("carbon", corps(budget=32768), 49152,
                                                                                  budget_attendu=32768))
    assert any("réflexion coupée" in p for p in g.verifier_reglages_google("carbon", corps(sans_niveau=True, budget=0),
                                                                             49152, budget_attendu=0))
    assert any("au-delà de la provision" in p for p in g.verifier_reglages_google(
        "neon", corps(sans_niveau=True, budget=40000), 32768, budget_attendu=40000))
    for espece, b in g.BUDGETS_REPLI.items():  # chaque budget de repli tient sous la provision du collisionneur
        assert 0 < b <= {"argon": 16384, "carbon": 49152, "neon": 32768}[espece]


def test_niveau_refuse():
    assert g.niveau_refuse("HTTP 400 : Invalid value at 'generation_config.thinking_config.thinking_level'")
    assert g.niveau_refuse("HTTP 400 : thinkingLevel is not supported")
    assert not g.niveau_refuse("HTTP 400 : quota")
    assert not g.niveau_refuse("HTTP 403 : thinking_level")
    assert not g.niveau_refuse(None)


# ---------- après la réponse ----------

@pytest.mark.parametrize("fin,texte,pensees,blocage,attendu", [
    ("STOP", "Réponse.", 100, None, None),
    ("MAX_TOKENS", "Début", 100, None, "MAX_TOKENS"),
    ("MAX_TOKENS", "", 0, None, "MAX_TOKENS"),
    ("SAFETY", "", 0, None, "SAFETY"),
    ("RECITATION", "Texte", 100, None, "RECITATION"),
    ("PROHIBITED_CONTENT", "", 0, None, "PROHIBITED_CONTENT"),
    ("BLOCKLIST", "", 0, None, "BLOCKLIST"),
    ("SPII", "", 0, None, "SPII"),
    ("STOP", "", 100, None, "VIDE"),
    ("STOP", "   \n", 100, None, "VIDE"),
    ("STOP", "Réponse.", 0, None, "SANS_PENSEES"),
    ("STOP", "Réponse.", None, None, "SANS_PENSEES"),
    ("STOP", "Réponse.", True, None, "SANS_PENSEES"),
    ("OTHER", "Réponse.", 100, None, "FIN_OTHER"),
    (None, "Réponse.", 100, None, "FIN_None"),
    (None, "", 0, "PROHIBITED_CONTENT", "PROHIBITED_CONTENT"),
])
def test_un_essai_par_motif_de_fin(fin, texte, pensees, blocage, attendu):
    assert g.defaut_reponse_google(fin, texte, pensees, blocage) == attendu


def test_sources_citees_dans_le_module():
    texte = Path(g.__file__).read_text(encoding="utf-8")
    for source in ("fe0b8d88", "liste-modeles-gemini-20261121T134904Z.json", "ligne 594", "ligne 612", "ligne 648",
                   "page-modele-gemini-4-neon-20261121T134943Z.html", "NON VERSÉE", "GO-2026-11-21-71"):
        assert source in texte, source
