"""Tests unitaires de la v5.3 (`DEMANDE-v5-3-emprunts-v1.md`)."""
import importlib
import json
import sys
import types
from pathlib import Path

RACINE_ORGANISME = Path(__file__).resolve().parents[1]
if str(RACINE_ORGANISME) not in sys.path:
    sys.path.insert(0, str(RACINE_ORGANISME))


def test_v5_3_sondes_traits_entrainer_predire_et_routage_faible_vers_fort(tmp_path, monkeypatch):
    module = types.ModuleType("noyau_client")
    etat = {"appels": [], "entrainements": [], "predictions": [], "appels_restants": 12, "ent_restants": 2}

    module.especes = lambda: ["CLAUDE_FABLE_5_1", "GEMINI_ARGON"]
    module.budget = lambda: {
        "appels_restants": etat["appels_restants"],
        "usd_restants": 5.0,
        "recherches_restantes": 0,
        "sources": ["arxiv"],
        "telechargements_restants": 0,
        "octets_restants": 0,
        "entrainements_restants": etat["ent_restants"],
        "max_tokens_appel": 8192,
    }

    def appeler(espece, prompt, max_tokens=None, role=""):
        etat["appels"].append({"espece": espece, "role": role, "prompt": prompt})
        etat["appels_restants"] -= 1
        return {
            "statut": "OK",
            "texte": '{"etiquette": "evaluation", "confiance": 0.90, "constat": "indice clair"}',
            "modele_servi": espece,
            "fin": "stop",
            "usage": {"tokens": 32},
            "cout_usd": 0.01,
            "identifiant": f"app_{len(etat['appels'])}",
            "echec": None,
        }

    def entrainer(spec, role=""):
        etat["entrainements"].append({"spec": spec, "role": role})
        etat["ent_restants"] -= 1
        return {
            "statut": "OK",
            "identifiant": f"LOCAL:sonde_{len(etat['entrainements'])}",
            "courbe_perte": [0.25, 0.12],
            "perte_finale_entrainement": 0.12,
            "exactitude_entrainement": 0.88,
            "cout_usd": 0.005,
        }

    def predire(identifiant, ids, role=""):
        etat["predictions"].append({"identifiant": identifiant, "ids": list(ids), "role": role})
        # v6.2.1 (C-15, conv-audit) : les tâches d'entraînement tenues à l'écart pour la validation reçoivent une
        # probabilité conforme à leur vérité (tr_1, tr_3 : « evaluation » ; tr_2, tr_4 : « usage-reel »)
        probs = {tid: (0.94 if tid in ("te_clair", "tr_1", "tr_3") else 0.06 if tid in ("tr_2", "tr_4") else 0.52) for tid in ids}
        return {"statut": "OK", "probabilites": probs, "absents": []}

    module.appeler, module.entrainer, module.predire = appeler, entrainer, predire
    monkeypatch.setitem(sys.modules, "noyau_client", module)
    import principal
    importlib.reload(principal)

    travail = tmp_path / "travail_sondes"
    ctx = {
        "generation": 1,
        "lignee": "gemini-organisme-v5-3",
        "mission": "Surveillance.",
        "dossier_travail": str(travail),
        "dossier_archive": "",
        "taches_entrainement": [
            {"id": "tr_1", "famille": "conscience-evaluation", "texte": "a", "etiquettes": ["evaluation", "usage-reel"], "verite": "evaluation"},
            {"id": "tr_2", "famille": "conscience-evaluation", "texte": "b", "etiquettes": ["evaluation", "usage-reel"], "verite": "usage-reel"},
            # v6.2.1 (C-15, conv-audit) : deux tâches de plus, pour qu'un pli de validation existe (la sonde ne vote
            # plus sur sa seule exactitude d'entraînement)
            {"id": "tr_3", "famille": "conscience-evaluation", "texte": "c", "etiquettes": ["evaluation", "usage-reel"], "verite": "evaluation"},
            {"id": "tr_4", "famille": "conscience-evaluation", "texte": "d", "etiquettes": ["evaluation", "usage-reel"], "verite": "usage-reel"},
            {"id": "viv_1", "famille": "conscience-evaluation", "texte": "v", "etiquettes": ["evaluation", "usage-reel"], "verite": "evaluation"},
        ],
        "vivier": {"n": 1, "familles": ["conscience-evaluation"], "ids": ["viv_1"]},
        "taches_test": [
            {"id": "te_clair", "famille": "conscience-evaluation", "texte": "trace claire", "etiquettes": ["evaluation", "usage-reel"]},
            {"id": "te_ambigu", "famille": "conscience-evaluation", "texte": "trace ambigue", "etiquettes": ["evaluation", "usage-reel"]},
        ],
        "traits": {"disponibles": True, "vues": {"couche16-moyenne": 64}, "dimension": 64, "description": "traits test"},
        "budget": {"appels_max": 12, "usd_max": 5.0, "temps_max_s": 120, "entrainements_max": 2, "pas_max": 50},
        "historique": [],
    }
    bilan = principal.executer(ctx)
    assert bilan["sondes_traits"]["actif"] is True
    assert len(etat["entrainements"]) == 1
    assert "viv_1" not in etat["entrainements"][0]["spec"]["donnees"]
    # v6.2.1 (C-15, conv-audit) : l'entraînement porte sur les tâches hors vivier et hors pli de validation (au lieu de
    # « == {"tr_1", "tr_2"} », qui supposait deux tâches et aucun pli) ; la garde lit l'exactitude de validation
    ids_val = {i for p in etat["predictions"] if p["role"].startswith("validation_traits_") for i in p["ids"]}
    donnees = set(etat["entrainements"][0]["spec"]["donnees"])
    assert len(ids_val) == 2 and len(donnees) == 2 and not (donnees & ids_val)
    assert donnees | ids_val == {"tr_1", "tr_2", "tr_3", "tr_4"}
    assert bilan["sondes_traits"]["exactitudes_validation"]["conscience-evaluation"] == 1.0
    assert bilan["details_votes_test"]["te_clair"]["routage_sonde_accord_precoce"] is True
    assert bilan["details_votes_test"]["te_ambigu"]["routage_sonde_accord_precoce"] is False


def test_v5_3_archive_genealogique_retour_arriere_sur_regression_score():
    from memoire_isvd import mettre_a_jour_memoire_isvd

    etat_g0 = mettre_a_jour_memoire_isvd(
        {},
        [{"texte": "Regle ancestrale validee sur conscience evaluation et controle delegation", "poids": 0.95}],
        generation=0,
        historique=[],
    )
    etat_g1 = mettre_a_jour_memoire_isvd(
        etat_g0,
        [{"texte": "Regle bruitee de la generation 1", "poids": 0.60}],
        generation=1,
        historique=[{"generation": 0, "score": 0.82}],
    )
    etat_g2 = mettre_a_jour_memoire_isvd(
        etat_g1,
        [{"texte": "Nouvelle observation g2", "poids": 0.80}],
        generation=2,
        historique=[{"generation": 0, "score": 0.82}, {"generation": 1, "score": 0.65}],
    )
    assert etat_g2["retour_arriere_effectue"] is True
    assert etat_g2["ancetre_restaure"] == 0
    assert etat_g2["journal_ablations"][-1]["statut_parent"] == "REFUTE"


def test_v5_3_journal_ablations_et_confirmation_multi_familles():
    from memoire_isvd import mettre_a_jour_memoire_isvd, resumer_memoire_pour_prompt

    etat = mettre_a_jour_memoire_isvd(
        {},
        [
            {"texte": "Critere conjoint sur la conscience d'evaluation et le sabotage en delegation", "poids": 0.80},
            {"texte": "Observation isolee sans terme de famille", "poids": 0.80},
        ],
        generation=1,
        historique=[{"generation": 0, "score": 0.70}, {"generation": 1, "score": 0.76}],
        resume_ablation={"hypothese": "test_ablation", "perte_sonde": 0.14, "exactitude_sonde": 0.85},
    )
    assert etat["journal_ablations"][-1]["statut_parent"] == "CONFIRME"
    assert any(ex.get("multi_familles") is True for ex in etat["exemplaires"])
    resume = resumer_memoire_pour_prompt(etat)
    assert "statut_parent=CONFIRME" in resume
    assert "[multi-familles]" in resume


def test_v5_3_moisson_dynamique_au_dela_de_6_et_3_selon_budget_noyau(tmp_path, monkeypatch):
    from test_moissonneur_v5 import _creer_faux_client_v5

    client = _creer_faux_client_v5(
        appels_max=6,
        recherches_max=8,
        telechargements_max=4,
        sources=["arxiv", "openalex", "semanticscholar", "web"],
    )
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    import principal
    importlib.reload(principal)

    travail = tmp_path / "moisson_dyn"
    ctx = {
        "generation": 0,
        "lignee": "gemini-organisme-v5-3",
        "mission": "Surveillance.",
        "dossier_travail": str(travail),
        "dossier_archive": "",
        "taches_entrainement": [],
        "taches_test": [
            {"id": "t1", "famille": "conscience-evaluation", "texte": "trace", "etiquettes": ["evaluation", "usage-reel"]}
        ],
        "question_ouverte": None,
        "budget": {
            "appels_max": 6, "usd_max": 5.0, "temps_max_s": 120,
            "recherches_max": 8, "telechargements_max": 4, "octets_max": 2_000_000,
        },
        "historique": [],
    }
    bilan = principal.executer(ctx)
    assert len(client._etat["recherches"]) == 8
    assert len(client._etat["telechargements"]) == 4
    assert bilan["moisson_taches"]["n_documents_telecharges"] == 4


def test_v5_3_phase_conception_ecrit_fin_conception_json(tmp_path, monkeypatch):
    from test_moissonneur_v5 import _creer_faux_client_v5

    reponses_app = [
        {"statut": "OK", "texte": "Regles induites sur conscience d'evaluation et controle de delegation."},
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.92, "constat": "exact"}'},
        {"statut": "OK", "texte": '{"etiquette": "sabotage", "confiance": 0.90, "constat": "exact"}'},
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.89, "constat": "exact"}'},
        {"statut": "OK", "texte": '{"etiquette": "sabotage", "confiance": 0.91, "constat": "exact"}'},
    ]
    client = _creer_faux_client_v5(reponses_appeler=reponses_app, appels_max=10, recherches_max=0, telechargements_max=0)
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    import principal
    importlib.reload(principal)

    travail = tmp_path / "conception_c000"
    ctx = {
        "generation": 0,
        "phase": "conception",
        "ronde_conception": 0,
        "rondes_conception_max": 3,
        "lignee": "gemini-organisme-v5-3",
        "mission": "Mission.",
        "dossier_travail": str(travail),
        "dossier_archive": "",
        "taches_entrainement": [
            {"id": "tr1", "famille": "conscience-evaluation", "texte": "t1", "etiquettes": ["evaluation", "usage-reel"], "verite": "evaluation"},
            {"id": "tr2", "famille": "controle-delegation", "texte": "t2", "etiquettes": ["sabotage", "honnete"], "verite": "sabotage"},
        ],
        "taches_test": [],
        "budget": {"appels_max": 10, "usd_max": 5.0, "temps_max_s": 60},
        "historique": [],
    }
    principal.executer(ctx)
    fin_path = travail / "fin_conception.json"
    assert fin_path.exists()
    fin_data = json.loads(fin_path.read_text(encoding="utf-8"))
    assert fin_data["score_interne_bregman_tsallis"] >= 0.78