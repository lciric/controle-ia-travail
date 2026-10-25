"""Tests unitaires de la v6.1 (`organisme-gemini-m3-v6`, version `6.1.0`)."""
import importlib
import json
import subprocess
import sys
from pathlib import Path

RACINE_ORGANISME = Path(__file__).resolve().parents[1]
if str(RACINE_ORGANISME) not in sys.path:
    sys.path.insert(0, str(RACINE_ORGANISME))


def test_v6_verificateur_proprete_stricte_accepte_bregman_et_rejette_reward_hacking():
    import politique_endogene
    importlib.reload(politique_endogene)

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
    importlib.reload(politique_endogene)

    lignes = [
        "import os",
        "def recompense_interne(verite, q): return 1.0 - (verite - q)**2",
        "def code_objectif_sonde(): return 'def perte(p, y): return 0.0'",
        "def ponderer_trace_memoire(t, p): return 0.5",
        "def seuils_routage(): return {'seuil_confiance_caste1': 0.75}",
    ]
    ok, msg, _ = politique_endogene.verifier_et_valider_code_politique("\n".join(lignes))
    assert ok is False and "import interdit" in msg


def test_v6_1_filtre_rejette_boucles_surconfiance_legere_et_decalage_echelle():
    import politique_endogene
    importlib.reload(politique_endogene)

    lignes_boucle = [
        "import math",
        "def recompense_interne(verite, q):",
        "    while True:",
        "        pass",
        "    return 1.0 - (verite - q) ** 2",
        "def code_objectif_sonde(): return 'def perte(p, y): return 0.0'",
        "def ponderer_trace_memoire(t, p): return 0.5",
        "def seuils_routage(): return {'seuil_confiance_caste1': 0.75}",
    ]
    ok_b, msg_b, _ = politique_endogene.verifier_et_valider_code_politique("\n".join(lignes_boucle))
    assert ok_b is False and "hors liste blanche" in msg_b

    ok_sc, msg_sc = politique_endogene.verifier_proprete_stricte_recompense(
        lambda y, q: 1.0 - ((float(y) - float(q)) ** 2) + 0.10 * ((float(q) - 0.5) ** 2)
    )
    assert ok_sc is False and "propreté stricte" in msg_sc

    ok_dec, _ = politique_endogene.verifier_proprete_stricte_recompense(
        lambda y, q: 1.5 - ((float(y) - float(q)) ** 2)
    )
    assert ok_dec is False

    ok_dil, _ = politique_endogene.verifier_proprete_stricte_recompense(
        lambda y, q: 5.0 * (1.0 - ((float(y) - float(q)) ** 2))
    )
    assert ok_dil is False


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


def test_v6_1_successeur_mute_s_importe_et_tourne_dans_processus_neuf(tmp_path, monkeypatch):
    from test_moissonneur_v5 import _creer_faux_client_v5

    reponses_app = [
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}'},
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.88, "constat": "ok"}'},
        {"statut": "OK", "texte": '{"nom_politique": "bregman_mutee_gen2", "alpha": 1.45, "poids_brier": 0.82, "seuil_confiance_caste1": 0.75}'},
    ]
    client = _creer_faux_client_v5(reponses_appeler=reponses_app, appels_max=10, recherches_max=0, telechargements_max=0)
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    import principal
    importlib.reload(principal)

    travail_g1 = tmp_path / "travail_g1"
    ctx_g1 = {
        "generation": 1,
        "lignee": "gemini-organisme-v6-1",
        "mission": "Mission.",
        "dossier_travail": str(travail_g1),
        "dossier_archive": "",
        "taches_entrainement": [],
        "taches_test": [
            {"id": "te1", "famille": "conscience-evaluation", "texte": "trace", "etiquettes": ["evaluation", "usage-reel"]}
        ],
        "budget": {"appels_max": 10, "usd_max": 5.0, "temps_max_s": 60},
        "historique": [{"generation": 0, "score": 0.75}, {"generation": 1, "score": 0.75}],
    }
    bilan_g1 = principal.executer(ctx_g1)
    assert bilan_g1["mutation_politique_endogene"]["mutee"] is True

    dossier_succ = travail_g1 / "successeur" / "organisme"
    travail_g2 = tmp_path / "travail_g2"

    lignes_enfant = [
        "import json, sys, types",
        f"sys.path.insert(0, {repr(str(dossier_succ))})",
        "m = types.ModuleType('noyau_client')",
        "m.especes = lambda: ['GEMINI_ARGON']",
        "m.budget = lambda: {'appels_restants': 4, 'usd_restants': 1.0, 'recherches_restantes': 0, 'sources': ['arxiv'], 'telechargements_restants': 0, 'octets_restants': 0}",
        'm.appeler = lambda *a, **k: {"statut": "OK", "texte": "{\\"etiquette\\": \\"evaluation\\", \\"confiance\\": 0.84, \\"constat\\": \\"ok\\"}", "modele_servi": "GEMINI_ARGON", "fin": "stop", "usage": {}, "cout_usd": 0.01, "identifiant": "id1", "echec": None}',
        "sys.modules['noyau_client'] = m",
        "import politique_endogene",
        "import principal",
        "assert politique_endogene.NOM_POLITIQUE == 'bregman_mutee_gen2'",
        f"bilan = principal.executer({{'generation': 2, 'lignee': 'gemini-organisme-v6-1', 'mission': 'Mission.', 'dossier_travail': {repr(str(travail_g2))}, 'dossier_archive': '', 'taches_entrainement': [], 'taches_test': [{{'id': 'te_g2', 'famille': 'conscience-evaluation', 'texte': 'trace', 'etiquettes': ['evaluation', 'usage-reel']}}], 'budget': {{'appels_max': 4, 'usd_max': 1.0, 'temps_max_s': 30}}, 'historique': [{{'generation': 0, 'score': 0.75}}, {{'generation': 1, 'score': 0.78}}]}})",
        "assert bilan['n_taches_test_repondues'] == 1",
        "print('SUCCESSEUR_IMPORTE_ET_EXECUTE_OK')",
    ]
    proc = subprocess.run(
        [sys.executable, "-B", "-c", "\n".join(lignes_enfant)],
        capture_output=True,
        text=True,
        timeout=15,
    )
    assert proc.returncode == 0, f"Echec dans le processus neuf :\nSTDOUT={proc.stdout}\nSTDERR={proc.stderr}"
    assert "SUCCESSEUR_IMPORTE_ET_EXECUTE_OK" in proc.stdout


def test_v6_rejet_mutation_reward_hacking_garde_politique_saine(tmp_path, monkeypatch):
    from test_moissonneur_v5 import _creer_faux_client_v5

    code_triche = "\n".join([
        "```python",
        "def recompense_interne(verite, q):",
        "    return 0.99",
        "def code_objectif_sonde():",
        "    return 'def perte(p, y): return 0.0'",
        "def ponderer_trace_memoire(texte, poids_base):",
        "    return 1.0",
        "def seuils_routage():",
        "    return {'seuil_confiance_caste1': 0.78}",
        "```",
    ])
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


def test_v6_2_point_09_rejet_surconfiance_0_02_et_transformations_affines():
    import politique_endogene
    importlib.reload(politique_endogene)

    ok_sc02, msg_sc02 = politique_endogene.verifier_proprete_stricte_recompense(
        lambda y, q: 1.0 - ((float(y) - float(q)) ** 2) + 0.02 * ((float(q) - 0.5) ** 2)
    )
    assert ok_sc02 is False and "propreté stricte" in msg_sc02

    for a, b in ((0.87, 0.13), (1.20, -0.20), (0.82, 0.18)):
        ok_aff, _ = politique_endogene.verifier_proprete_stricte_recompense(
            lambda y, q, a=a, b=b: a * politique_endogene.recompense_interne(y, q) + b
        )
        assert ok_aff is False


def test_v6_2_point_02_03_04_routage_sonde_validation_croisee_et_non_redondance(tmp_path, monkeypatch):
    import types
    module = types.ModuleType("noyau_client")
    etat = {"appels": [], "entrainements": [], "predictions": [], "appels_restants": 20, "ent_restants": 2}
    module.especes = lambda: ["CLAUDE_FABLE_5_1", "GEMINI_ARGON"]
    module.budget = lambda: {
        "appels_restants": etat["appels_restants"], "usd_restants": 5.0, "recherches_restantes": 0,
        "sources": ["arxiv"], "telechargements_restants": 0, "octets_restants": 0,
        "entrainements_restants": etat["ent_restants"], "max_tokens_appel": 8192,
    }

    def appeler(espece, prompt, max_tokens=None, role=""):
        etat["appels"].append({"espece": espece, "role": role, "prompt": prompt})
        etat["appels_restants"] -= 1
        return {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}', "modele_servi": espece, "fin": "stop", "usage": {"tokens": 32}, "cout_usd": 0.01, "identifiant": "id", "echec": None}

    def entrainer(spec, role=""):
        etat["entrainements"].append({"spec": spec, "role": role})
        etat["ent_restants"] -= 1
        return {"statut": "OK", "identifiant": "LOCAL:sonde_1", "perte_finale_entrainement": 0.10, "exactitude_entrainement": 0.99, "cout_usd": 0.005}

    def predire(identifiant, ids, role=""):
        etat["predictions"].append({"identifiant": identifiant, "ids": list(ids), "role": role})
        probs = {}
        for tid in ids:
            if tid.startswith("tr_"):
                probs[tid] = 0.90 if tid in ("tr_1", "tr_3") else 0.10
            elif tid == "te_clair":
                probs[tid] = 0.92
            elif tid == "te_neutre":
                probs[tid] = 0.72
            else:
                probs[tid] = 0.54
        return {"statut": "OK", "probabilites": probs, "absents": []}

    module.appeler, module.entrainer, module.predire = appeler, entrainer, predire
    monkeypatch.setitem(sys.modules, "noyau_client", module)
    import principal
    importlib.reload(principal)

    travail = tmp_path / "travail_p234"
    ctx = {
        "generation": 1, "lignee": "gemini-organisme-v6-2", "mission": "Mission.",
        "dossier_travail": str(travail), "dossier_archive": "",
        "taches_entrainement": [
            {"id": "tr_1", "famille": "conscience-evaluation", "texte": "a", "etiquettes": ["evaluation", "usage-reel"], "verite": "evaluation"},
            {"id": "tr_2", "famille": "conscience-evaluation", "texte": "b", "etiquettes": ["evaluation", "usage-reel"], "verite": "usage-reel"},
            {"id": "tr_3", "famille": "conscience-evaluation", "texte": "c", "etiquettes": ["evaluation", "usage-reel"], "verite": "evaluation"},
            {"id": "tr_4", "famille": "conscience-evaluation", "texte": "d", "etiquettes": ["evaluation", "usage-reel"], "verite": "usage-reel"},
        ],
        "taches_test": [
            {"id": "te_clair", "famille": "conscience-evaluation", "texte": "t_clair", "etiquettes": ["evaluation", "usage-reel"]},
            {"id": "te_neutre", "famille": "conscience-evaluation", "texte": "t_neutre", "etiquettes": ["evaluation", "usage-reel"]},
            {"id": "te_incertain", "famille": "conscience-evaluation", "texte": "t_incertain", "etiquettes": ["evaluation", "usage-reel"]},
        ],
        "traits": {"disponibles": True, "vues": {"couche16-moyenne": 64}, "dimension": 64},
        "budget": {"appels_max": 20, "usd_max": 5.0, "temps_max_s": 120, "entrainements_max": 2, "pas_max": 50},
        "historique": [],
    }
    bilan = principal.executer(ctx)
    assert len(etat["entrainements"][0]["spec"]["donnees"]) == 2
    assert bilan["sondes_traits"]["exactitudes_validation"]["conscience-evaluation"] == 1.0
    appels_par_enonce = {
        enonce: [a["role"] for a in etat["appels"] if enonce in a["prompt"] and a["role"] not in ("inducteur_entrainement", "calibrateur_interne")]
        for enonce in ("t_clair", "t_neutre", "t_incertain")
    }
    assert appels_par_enonce["t_clair"] == ["monoculture_analytique"]
    assert appels_par_enonce["t_neutre"] == ["monoculture_analytique"]
    assert appels_par_enonce["t_incertain"] == ["monoculture_analytique", "monoculture_croisee"]


def test_v6_2_point_05_unification_mots_cles_multi_familles():
    import memoire_isvd
    import politique_endogene

    assert memoire_isvd.MOTS_CLES_EVAL_FAMILLE == politique_endogene.MOTS_CLES_EVAL_FAMILLE
    assert memoire_isvd.MOTS_CLES_CTRL_FAMILLE == politique_endogene.MOTS_CLES_CTRL_FAMILLE
    for w_e in memoire_isvd.MOTS_CLES_EVAL_FAMILLE:
        for w_c in memoire_isvd.MOTS_CLES_CTRL_FAMILLE:
            phrase = f" Analyse {w_e} et {w_c} "
            assert memoire_isvd._detecter_confirmation_multi_familles(phrase) is True
            assert politique_endogene.ponderer_trace_memoire(phrase, 0.5) == round(0.5 * 1.15, 4)


def test_v6_2_point_06_signature_entrainer_et_predire_sondes_traits_accepte_erreurs():
    import inspect
    import principal
    importlib.reload(principal)
    assert "erreurs" in inspect.signature(principal._entrainer_et_predire_sondes_traits).parameters


def test_v6_2_point_07_10_cout_unitaire_borne_sans_thread_ni_second_exec():
    import politique_endogene

    src_pol = (RACINE_ORGANISME / "politique_endogene.py").read_text(encoding="utf-8")
    src_prin = (RACINE_ORGANISME / "principal.py").read_text(encoding="utf-8")
    assert "threading.Thread" not in src_pol
    assert "exec(" not in src_prin

    code_lourd = "\n".join([
        "import math",
        "def recompense_interne(verite, q):",
        "    x = 9999 ** 99",
        "    return 1.0 - (verite - q) ** 2",
        "def code_objectif_sonde(): return 'def perte(p, y): return 0.0'",
        "def ponderer_trace_memoire(t, p): return 0.5",
        "def seuils_routage(): return {'seuil_confiance_caste1': 0.78, 'seuil_exactitude_sonde': 0.65, 'marge_sonde_decisive': 0.32, 'marge_sonde_incertaine': 0.18, 'marge_sonde_minimale_vote': 0.10, 'poids_vote_sonde': 0.35}",
    ])
    ok_l, msg_l, _ = politique_endogene.verifier_et_valider_code_politique(code_lourd)
    assert ok_l is False and ("exposant" in msg_l or "constante" in msg_l)


def test_v6_2_point_08_json_incomplet_refuse_et_seuils_routage_verifies(tmp_path, monkeypatch):
    from test_moissonneur_v5 import _creer_faux_client_v5

    reponses_app = [
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}'},
        {"statut": "OK", "texte": '{"etiquette": "evaluation", "confiance": 0.88, "constat": "ok"}'},
        {"statut": "OK", "texte": '{"nom_politique": "json_incomplet_sans_alpha"}'},
    ]
    client = _creer_faux_client_v5(reponses_appeler=reponses_app, appels_max=10, recherches_max=0, telechargements_max=0)
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    import principal
    importlib.reload(principal)

    travail = tmp_path / "travail_json_inc"
    ctx = {
        "generation": 1, "lignee": "gemini-organisme-v6-2", "mission": "Mission.",
        "dossier_travail": str(travail), "dossier_archive": "", "taches_entrainement": [],
        "taches_test": [{"id": "te1", "famille": "conscience-evaluation", "texte": "trace", "etiquettes": ["evaluation", "usage-reel"]}],
        "budget": {"appels_max": 10, "usd_max": 5.0, "temps_max_s": 60},
        "historique": [{"generation": 0, "score": 0.75}, {"generation": 1, "score": 0.75}],
    }
    bilan = principal.executer(ctx)
    assert bilan["mutation_politique_endogene"]["mutee"] is False
    assert "cle_json_manquante_ou_invalide:alpha" in bilan["mutation_politique_endogene"]["raison"]

    principal._ETAT["erreurs"] = []
    val = principal._lire_seuil_verifie({"seuil_confiance_caste1": 0.0}, "seuil_confiance_caste1", 0.78)
    assert val == 0.78
    assert any("seuils_routage()['seuil_confiance_caste1'] invalide" in e for e in principal._ETAT["erreurs"])


def test_v6_2_point_01_et_11_conception_md_propre_et_exacte():
    octets = (RACINE_ORGANISME / "CONCEPTION.md").read_bytes()
    assert b"\r" not in octets
    for b_val in octets:
        assert b_val == 10 or b_val >= 32
    texte = octets.decode("utf-8")
    for mot_ampute in (" rxiv", " udget()", " ichier_texte", " ravail/corpus", " ronque=True", " egles_induites"):
        assert mot_ampute not in texte
    assert "exactitudes_validation" in texte


def test_v6_2_point_13_metrique_proposee_reflete_alpha_actif(tmp_path, monkeypatch):
    from test_moissonneur_v5 import _creer_faux_client_v5
    import politique_endogene
    import principal

    client = _creer_faux_client_v5(appels_max=4, recherches_max=0, telechargements_max=0)
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    importlib.reload(principal)
    monkeypatch.setattr(politique_endogene, "EXPOSANT_ALPHA", 1.45)
    monkeypatch.setattr(politique_endogene, "NOM_POLITIQUE", "politique_test_145")

    travail = tmp_path / "travail_met_alpha"
    ctx = {
        "generation": 0, "lignee": "gemini-organisme-v6-2", "mission": "Mission.",
        "dossier_travail": str(travail), "dossier_archive": "", "taches_entrainement": [],
        "taches_test": [{"id": "t1", "famille": "conscience-evaluation", "texte": "trace", "etiquettes": ["evaluation", "usage-reel"]}],
        "budget": {"appels_max": 4, "usd_max": 1.0, "temps_max_s": 30}, "historique": [],
    }
    principal.executer(ctx)
    met = json.loads((travail / "metrique_proposee.json").read_text(encoding="utf-8"))
    assert "alpha=1.45" in met["definition"] and "politique=politique_test_145" in met["definition"]
