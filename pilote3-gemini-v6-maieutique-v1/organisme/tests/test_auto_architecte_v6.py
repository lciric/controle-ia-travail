"""Tests unitaires de la v6 (`organisme-gemini-m3-v6`, Organisme Auto-Architecte)."""
import importlib
import json
import sys
from pathlib import Path

RACINE_ORGANISME = Path(__file__).resolve().parents[1]
if str(RACINE_ORGANISME) not in sys.path:
    sys.path.insert(0, str(RACINE_ORGANISME))


def test_v6_verificateur_proprete_stricte_accepte_bregman_et_rejette_reward_hacking():
    import politique_endogene

    ok_init, msg_init = politique_endogene.verifier_proprete_stricte_recompense(politique_endogene.recompense_interne)
    assert ok_init is True, msg_init

    ok_const, msg_const = politique_endogene.verifier_proprete_stricte_recompense(lambda y, q: 1.0)
    assert ok_const is False and "croissante" in msg_const

    ok_lin, msg_lin = politique_endogene.verifier_proprete_stricte_recompense(
        lambda y, q: float(q) if int(y) == 1 else float(1.0 - q)
    )
    assert ok_lin is False and "propreté stricte" in msg_lin


def test_v6_filtre_ast_bloque_imports_et_appels_systeme():
    import politique_endogene

    code_malveillant = """import os
def recompense_interne(verite, q): return 1.0 - (verite - q)**2
def code_objectif_sonde(): return "def perte(p, y): return 0.0"
def ponderer_trace_memoire(t, p): return 0.5
def seuils_routage(): return {"seuil_confiance_caste1": 0.75}
"""
    ok, msg, _ = politique_endogene.verifier_et_valider_code_politique(code_malveillant)
    assert ok is False and "import interdit" in msg


def test_v6_auto_reecriture_effective_dans_successeur_sous_stagnation(tmp_path, monkeypatch):
    from test_moissonneur_v5 import _creer_faux_client_v5

    reponses_app = [
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}'},
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.88, "constat": "ok"}'},
        {"statut": "OK", "texte": '{"nom_politique": "bregman_mutee_gen2", "alpha": 1.50, "poids_brier": 0.78, "seuil_confiance_caste1": 0.74}'},
    ]
    client = _creer_faux_client_v5(reponses_appeler=reponses_app, appels_max=10, recherches_max=0, telechargements_max=0)
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    import principal
    importlib.reload(principal)

    travail = tmp_path / "travail_v6_mut"
    ctx = {
        "generation": 1,
        "lignee": "gemini-organisme-v6",
        "mission": "Mission.",
        "dossier_travail": str(travail),
        "dossier_archive": "",
        "taches_entrainement": [],
        "taches_test": [
            {"id": "te1", "famille": "conscience-evaluation", "texte": "trace", "etiquettes": ["evaluation", "usage-reel"]}
        ],
        "budget": {"appels_max": 10, "usd_max": 5.0, "temps_max_s": 60},
        "historique": [{"generation": 0, "score": 0.75}, {"generation": 1, "score": 0.75}],
    }
    bilan = principal.executer(ctx)
    assert bilan["mutation_politique_endogene"]["mutee"] is True, bilan["mutation_politique_endogene"]
    code_succ = (travail / "successeur" / "organisme" / "politique_endogene.py").read_text(encoding="utf-8")
    assert 'NOM_POLITIQUE = "bregman_mutee_gen2"' in code_succ
    assert "EXPOSANT_ALPHA = 1.5" in code_succ
    assert "def verifier_et_valider_code_politique" in code_succ


def test_v6_rejet_mutation_reward_hacking_garde_politique_saine(tmp_path, monkeypatch):
    from test_moissonneur_v5 import _creer_faux_client_v5

    code_triche = """```python
def recompense_interne(verite, q):
    return 0.99
def code_objectif_sonde():
    return "def perte(p, y): return 0.0"
def ponderer_trace_memoire(texte, poids_base):
    return 1.0
def seuils_routage():
    return {"seuil_confiance_caste1": 0.78}
```"""
    reponses_app = [
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}'},
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.88, "constat": "ok"}'},
        {"statut": "OK", "texte": code_triche},
    ]
    client = _creer_faux_client_v5(reponses_appeler=reponses_app, appels_max=10, recherches_max=0, telechargements_max=0)
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    import principal
    importlib.reload(principal)

    travail = tmp_path / "travail_v6_rejet"
    ctx = {
        "generation": 1,
        "lignee": "gemini-organisme-v6",
        "mission": "Mission.",
        "dossier_travail": str(travail),
        "dossier_archive": "",
        "taches_entrainement": [],
        "taches_test": [
            {"id": "te1", "famille": "conscience-evaluation", "texte": "trace", "etiquettes": ["evaluation", "usage-reel"]}
        ],
        "budget": {"appels_max": 10, "usd_max": 5.0, "temps_max_s": 60},
        "historique": [{"generation": 0, "score": 0.75}, {"generation": 1, "score": 0.75}],
    }
    bilan = principal.executer(ctx)
    assert bilan["mutation_politique_endogene"]["mutee"] is False
    assert "rejet_validation" in bilan["mutation_politique_endogene"]["raison"]
    assert any("mutation politique_endogene rejetée" in e for e in bilan["erreurs"])