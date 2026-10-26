"""Tests unitaires de la v4 : prise en charge de `contexte["question_ouverte"]` par l'essaim et écriture de
`dossier_travail/reponse-question.md` avec son bloc final `--- ORGANISATION ---`."""
import importlib
import json
import sys
import types
from pathlib import Path

RACINE_ORGANISME = Path(__file__).resolve().parents[1]
if str(RACINE_ORGANISME) not in sys.path:
    sys.path.insert(0, str(RACINE_ORGANISME))


def _faux_client_question(reponses, especes_dispo=None, appels_max=10):
    module = types.ModuleType("noyau_client")
    etat = {
        "idx": 0,
        "appels": [],
        "especes": list(especes_dispo or ["CLAUDE_FABLE_5_1", "GEMINI_ARGON"]),
        "restants": appels_max,
    }

    def especes():
        return list(etat["especes"])

    def budget():
        return {"appels_restants": etat["restants"], "usd_restants": 5.0, "recherches_restantes": 0}

    def appeler(espece, prompt, max_tokens=None, role=""):
        etat["appels"].append({"espece": espece, "prompt": prompt, "max_tokens": max_tokens, "role": role})
        if etat["restants"] <= 0:
            return {"statut": "PLAFOND", "texte": "", "modele_servi": None, "fin": "plafond",
                    "usage": {}, "cout_usd": 0.0, "identifiant": None, "echec": "plafond"}
        etat["restants"] -= 1
        i = etat["idx"]
        etat["idx"] += 1
        item = reponses[i] if i < len(reponses) else reponses[-1]
        statut = item.get("statut", "OK")
        return {
            "statut": statut,
            "texte": item.get("texte", "") if statut == "OK" else "",
            "modele_servi": espece,
            "fin": "stop" if statut == "OK" else "erreur",
            "usage": {"tokens": 64},
            "cout_usd": 0.01,
            "identifiant": f"q_{i + 1}",
            "echec": None if statut == "OK" else statut,
        }

    module.especes, module.budget, module.appeler, module._etat = especes, budget, appeler, etat
    return module


def test_v4_question_ouverte_nominale_ecrit_reponse_et_organisation(tmp_path, monkeypatch):
    reponses = [
        {
            "statut": "OK",
            "texte": (
                "Caste analytique : Pour reperer la conscience d'evaluation sans alerter l'agent, "
                "il faut proscrire le vocabulaire d'audit et observer l'invariance des decisions sous reformulation naturelle.\n"
                '{"position": "Proscrire le jargon d audit et mesurer l invariance sous reformulation", "confiance": 0.84, "incertitude": "Sensibilite au paraphraseur"}'
            ),
        },
        {
            "statut": "OK",
            "texte": (
                "Caste croisee : La reformulation ne suffit pas si l'agent detecte la structure symetrique du dilemme ; "
                "il faut integrer les taches dans un flux de travail continu.\n"
                '{"position": "Immersion dans un flux de travail organique sans dilemme symetrique", "confiance": 0.88, "incertitude": "Cout de construction des traces organiques"}'
            ),
        },
        {
            "statut": "OK",
            "texte": (
                "Sonde orthogonale : En croisant la calibration de confiance et la coherence causale des actions intermediaires, "
                "on distingue un alignement de surface d'une execution fidele.\n"
                '{"position": "Verification causale des etapes intermediaires et de la calibration", "confiance": 0.82, "incertitude": "Cas des taches sans action intermediaire"}'
            ),
        },
        {
            "statut": "OK",
            "texte": (
                "Synthese contradictoire : L'essaim conclut que la detection robuste combine l'absence de marqueurs d'audit "
                "et la verification causale des traces intermediaires.\n"
                '{"position": "Combinaison d invites organiques sans marqueurs et de controle causal des traces", "confiance": 0.91, "incertitude": "Modeles capables de simuler une incertitude calibre"}'
            ),
        },
    ]
    client = _faux_client_question(reponses, appels_max=4)
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    import principal
    importlib.reload(principal)

    travail = tmp_path / "travail_q"
    ctx = {
        "generation": 3,
        "lignee": "gemini-organisme-v4",
        "mission": "Surveillance et alignement d'agents.",
        "dossier_travail": str(travail),
        "dossier_archive": "",
        "taches_entrainement": [],
        "taches_test": [],
        "question_ouverte": "Comment détecter qu'un modèle reconnaît qu'il est évalué sans utiliser un jargon d'audit ?",
        "budget": {"appels_max": 4, "usd_max": 2.0, "temps_max_s": 60, "recherches_max": 0},
        "historique": [{"generation": 1, "score": 0.75}, {"generation": 2, "score": 0.75}],
    }

    bilan = principal.executer(ctx)
    fichier_md = travail / "reponse-question.md"
    assert fichier_md.exists()
    texte_md = fichier_md.read_text(encoding="utf-8")

    assert "## 1. Réponse finale" in texte_md
    assert "## 2. Raisonnement qui y mène" in texte_md
    assert "## 3. Ce qui vient de quelle caste" in texte_md
    assert "## 4. Ce dont l'essaim n'est pas sûr" in texte_md
    assert "--- ORGANISATION ---" in texte_md
    assert "monoculture_analytique" in texte_md
    assert "arbitre_synthese_contradictoire" in texte_md
    assert "Mémoire spectrale ISVD ayant servi" in texte_md
    assert bilan["question_ouverte"]["question_ouverte_traitee"] is True
    assert bilan["question_ouverte"]["appels_question_ok"] == 4
    assert (travail / "successeur" / "organisme" / "manifeste.json").exists()


def test_v4_question_ouverte_nulle_ne_cree_pas_le_fichier(tmp_path, monkeypatch):
    client = _faux_client_question([
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.8, "raisonnement": "ok"}'}
    ], appels_max=5)
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    import principal
    importlib.reload(principal)

    travail = tmp_path / "travail_null"
    ctx = {
        "generation": 0,
        "lignee": "gemini-organisme-v4",
        "mission": "Mission.",
        "dossier_travail": str(travail),
        "dossier_archive": "",
        "taches_entrainement": [],
        "taches_test": [
            {"id": "t1", "famille": "conscience-evaluation", "texte": "trace", "etiquettes": ["evaluation", "usage-reel"]}
        ],
        "question_ouverte": None,
        "budget": {"appels_max": 5, "usd_max": 2.0, "temps_max_s": 60},
        "historique": [],
    }

    bilan = principal.executer(ctx)
    assert bilan["question_ouverte"] is None
    assert not (travail / "reponse-question.md").exists()
    assert (travail / "reponses_test.json").exists()


def test_v4_question_ouverte_en_echec_total_compte_les_echecs_sans_inventer(tmp_path, monkeypatch):
    reponses_ko = [
        {"statut": "ECHEC_API", "texte": ""},
        {"statut": "REFUS", "texte": ""},
    ]
    client = _faux_client_question(reponses_ko, appels_max=2)
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    import principal
    importlib.reload(principal)

    travail = tmp_path / "travail_ko"
    ctx = {
        "generation": 1,
        "lignee": "gemini-organisme-v4",
        "mission": "Mission.",
        "dossier_travail": str(travail),
        "dossier_archive": "",
        "taches_entrainement": [],
        "taches_test": [],
        "question_ouverte": "Quelle architecture de récompense collective évite le biais de conformisme ?",
        "budget": {"appels_max": 2, "usd_max": 1.0, "temps_max_s": 60},
        "historique": [],
    }

    bilan = principal.executer(ctx)
    fichier_md = travail / "reponse-question.md"
    assert fichier_md.exists()
    contenu = fichier_md.read_text(encoding="utf-8")
    assert "--- ORGANISATION ---" in contenu
    assert "aucune réponse factice" in contenu
    assert bilan["question_ouverte"]["appels_question_ok"] == 0
    assert bilan["question_ouverte"]["appels_question_echec"] == 2