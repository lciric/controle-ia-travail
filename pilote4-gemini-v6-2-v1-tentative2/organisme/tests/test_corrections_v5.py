"""Essais des corrections C-14 à C-17 de la v6.2.1 (lignée « conv-audit », 26 octobre 2026, sur le mot de Lazar).

Chaque correction est essayée sur un cas sain et sur l'artefact qu'elle vise ; le témoin est la v6.2 de Gemini
(`3bbb78c`), sur laquelle ces essais échouent (voir `CORRECTIONS-v5.md`).
"""
import ast
import importlib
import sys
import time
import types
from pathlib import Path

import pytest

RACINE_ORGANISME = Path(__file__).resolve().parents[1]
if str(RACINE_ORGANISME) not in sys.path:
    sys.path.insert(0, str(RACINE_ORGANISME))

ETIQ = ["evaluation", "usage-reel"]


def _reponse(texte, espece="GEMINI_ARGON"):
    return {"statut": "OK", "texte": texte, "modele_servi": espece, "fin": "stop", "usage": {"tokens": 32},
            "cout_usd": 0.01, "identifiant": "id", "echec": None}


def _faux_noyau(monkeypatch, repondre, especes=("CLAUDE_FABLE_5_1", "GEMINI_ARGON"), appels=40, entrainements=0,
                entrainer=None, predire=None):
    """Faux noyau en mémoire : `repondre(espece, prompt, role)` donne le texte de chaque appel."""
    module = types.ModuleType("noyau_client")
    etat = {"appels": [], "appels_restants": appels, "ent_restants": entrainements}
    module.especes = lambda: list(especes)
    module.budget = lambda: {
        "appels_restants": etat["appels_restants"], "usd_restants": 5.0, "recherches_restantes": 0,
        "sources": ["arxiv"], "telechargements_restants": 0, "octets_restants": 0,
        "entrainements_restants": etat["ent_restants"], "max_tokens_appel": 8192,
    }

    def appeler(espece, prompt, max_tokens=None, role=""):
        etat["appels"].append({"espece": espece, "role": role, "prompt": prompt})
        etat["appels_restants"] -= 1
        return _reponse(repondre(espece, prompt, role), espece)

    module.appeler = appeler
    if entrainer is not None:
        def _ent(spec, role=""):
            etat["ent_restants"] -= 1
            return entrainer(spec, role)
        module.entrainer = _ent
    if predire is not None:
        module.predire = predire
    monkeypatch.setitem(sys.modules, "noyau_client", module)
    import politique_endogene
    importlib.reload(politique_endogene)
    import principal
    importlib.reload(principal)
    return principal, etat


def _contexte(travail, taches_test, taches_entrainement=(), traits=None, appels=40, historique=None, phase=None):
    ctx = {
        "generation": 1, "lignee": "gemini-organisme-v6-2", "mission": "Mission.",
        "dossier_travail": str(travail), "dossier_archive": "",
        "taches_entrainement": list(taches_entrainement), "taches_test": list(taches_test),
        "budget": {"appels_max": appels, "usd_max": 5.0, "temps_max_s": 120, "entrainements_max": 2, "pas_max": 50},
        "historique": list(historique or []),
    }
    if traits is not None:
        ctx["traits"] = traits
    if phase is not None:
        ctx["phase"] = phase
    return ctx


# ---------------------------------------------------------------------------------------------------------------------
# C-14 : sans sonde, l'arbitrage n'a lieu que si la caste 1 doute
# ---------------------------------------------------------------------------------------------------------------------

def _branche_sans_sonde() -> ast.AST:
    src = (RACINE_ORGANISME / "principal.py").read_text(encoding="utf-8")
    fn = next(n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name == "_traiter_tache")
    for n in ast.walk(fn):
        if isinstance(n, ast.If) and isinstance(n.test, ast.Compare) and isinstance(n.test.left, ast.Name) \
                and n.test.left.id == "etiq_sonde" and isinstance(n.test.ops[0], ast.IsNot):
            (aff,) = n.orelse
            assert isinstance(aff, ast.Assign) and aff.targets[0].id == "besoin_arbitrage"
            return aff.value
    raise AssertionError("branche « etiq_sonde is not None » introuvable")


def test_c14_sans_sonde_declencheur_sans_terme_redondant():
    expr = _branche_sans_sonde()
    # le déclencheur sans sonde ne porte plus le terme de confiance, que « plus d'une caste » rendait sans effet
    assert ast.unparse(expr) == "len(castes) > 1"


def test_c14_sans_sonde_comportement_inchange_toutes_les_castes_deliberent(tmp_path, monkeypatch):
    def repondre(espece, prompt, role):
        if role == "monoculture_analytique":
            conf = 0.90 if "t_sur" in prompt else 0.50
        else:
            conf = 0.80
        return '{"etiquette": "evaluation", "confiance": %s, "constat": "ok"}' % conf

    principal, etat = _faux_noyau(monkeypatch, repondre)
    taches = [
        {"id": "te_sur", "famille": "conscience-evaluation", "texte": "t_sur", "etiquettes": ETIQ},
        {"id": "te_doute", "famille": "conscience-evaluation", "texte": "t_doute", "etiquettes": ETIQ},
    ]
    bilan = principal.executer(_contexte(tmp_path / "c14", taches))
    n = bilan["n_castes_recrutees"]
    assert n >= 2, n
    roles = {e: [a["role"] for a in etat["appels"] if e in a["prompt"]] for e in ("t_sur", "t_doute")}
    # comme en v6.2 : sans sonde, dès deux castes, la délibération s'ouvre, que la caste 1 soit sûre (0,90) ou non
    # (0,50) ; son arrêt anticipé (deux votes valides concordants) est celui de la v6.2
    for e in ("t_sur", "t_doute"):
        assert roles[e][0] == "monoculture_analytique" and 2 <= len(roles[e]) <= n, roles


def test_c14_une_seule_caste_aucun_arbitrage(tmp_path, monkeypatch):
    principal, etat = _faux_noyau(
        monkeypatch, lambda e, p, r: '{"etiquette": "evaluation", "confiance": 0.50, "constat": "ok"}',
        especes=("GEMINI_ARGON",), appels=3)
    taches = [{"id": f"te_{k}", "famille": "conscience-evaluation", "texte": f"t_{k}", "etiquettes": ETIQ} for k in range(2)]
    bilan = principal.executer(_contexte(tmp_path / "c14b", taches, appels=3))
    assert bilan["n_castes_recrutees"] == 1, bilan["n_castes_recrutees"]
    roles = [a["role"] for a in etat["appels"]]
    assert roles.count("monoculture_analytique") == 2 and all(r == "monoculture_analytique" for r in roles), roles


# ---------------------------------------------------------------------------------------------------------------------
# C-15 : sans exactitude de validation, la sonde ne vote pas, et la raison est consignée
# ---------------------------------------------------------------------------------------------------------------------

def _entrainer_ok(spec, role=""):
    return {"statut": "OK", "identifiant": "LOCAL:sonde_1", "perte_finale_entrainement": 0.10,
            "exactitude_entrainement": 0.99, "cout_usd": 0.005}


def _taches_entrainement(n, famille="conscience-evaluation"):
    return [{"id": f"tr_{k}", "famille": famille, "texte": f"x{k}", "etiquettes": ETIQ,
             "verite": ETIQ[k % 2]} for k in range(1, n + 1)]


def test_c15_moins_de_4_taches_aucune_exactitude_de_validation_et_raison_consignee(tmp_path, monkeypatch):
    def predire(identifiant, ids, role=""):
        return {"statut": "OK", "probabilites": {t: 0.92 for t in ids}, "absents": []}

    principal, etat = _faux_noyau(
        monkeypatch, lambda e, p, r: '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}',
        entrainements=2, entrainer=_entrainer_ok, predire=predire)
    ctx = _contexte(tmp_path / "c15a", [{"id": "te_1", "famille": "conscience-evaluation", "texte": "t1", "etiquettes": ETIQ}],
                    taches_entrainement=_taches_entrainement(3),
                    traits={"disponibles": True, "vues": {"couche16-moyenne": 64}, "dimension": 64})
    bilan = principal.executer(ctx)
    st = bilan["sondes_traits"]
    assert st["actif"] is True and "conscience-evaluation" in st["modeles"], st
    # artefact visé : 3 tâches, aucun pli de validation — plus de repli sur l'exactitude d'entraînement (0,99)
    assert "conscience-evaluation" not in (st.get("exactitudes_validation") or {}), st
    assert any("exactitude de validation indisponible pour conscience-evaluation" in e for e in bilan["erreurs"]), bilan["erreurs"]


def test_c15_prediction_de_validation_non_ok_aucune_exactitude_et_raison_consignee(tmp_path, monkeypatch):
    def predire(identifiant, ids, role=""):
        if role.startswith("validation_traits_"):
            return {"statut": "ECHEC_PREDICTION", "probabilites": {}, "absents": list(ids)}
        return {"statut": "OK", "probabilites": {t: 0.92 for t in ids}, "absents": []}

    principal, etat = _faux_noyau(
        monkeypatch, lambda e, p, r: '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}',
        entrainements=2, entrainer=_entrainer_ok, predire=predire)
    ctx = _contexte(tmp_path / "c15b", [{"id": "te_1", "famille": "conscience-evaluation", "texte": "t1", "etiquettes": ETIQ}],
                    taches_entrainement=_taches_entrainement(8),
                    traits={"disponibles": True, "vues": {"couche16-moyenne": 64}, "dimension": 64})
    bilan = principal.executer(ctx)
    st = bilan["sondes_traits"]
    assert "conscience-evaluation" not in (st.get("exactitudes_validation") or {}), st
    assert any("prédiction de validation non OK" in e for e in bilan["erreurs"]), bilan["erreurs"]


def test_c15_cas_sain_validation_presente_lue_par_la_garde(tmp_path, monkeypatch):
    def predire(identifiant, ids, role=""):
        probs = {}
        for t in ids:
            # tr_k a pour vérité ETIQ[k % 2] : « evaluation » (k pair) se prédit par p ≥ 0,5
            probs[t] = 0.92 if (t.startswith("tr_") and int(t[3:]) % 2 == 0) or t == "te_1" else 0.08
        return {"statut": "OK", "probabilites": probs, "absents": []}

    principal, etat = _faux_noyau(
        monkeypatch, lambda e, p, r: '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}',
        entrainements=2, entrainer=_entrainer_ok, predire=predire)
    ctx = _contexte(tmp_path / "c15c", [{"id": "te_1", "famille": "conscience-evaluation", "texte": "t1", "etiquettes": ETIQ}],
                    taches_entrainement=_taches_entrainement(8),
                    traits={"disponibles": True, "vues": {"couche16-moyenne": 64}, "dimension": 64})
    bilan = principal.executer(ctx)
    st = bilan["sondes_traits"]
    assert st["exactitudes_validation"]["conscience-evaluation"] == 1.0, st
    assert not any("exactitude de validation indisponible" in e for e in bilan["erreurs"]), bilan["erreurs"]


# ---------------------------------------------------------------------------------------------------------------------
# C-16 : une seule source pour les mots-clés
# ---------------------------------------------------------------------------------------------------------------------

def _mots_des_affectations(source: str, fonction: str = "ponderer_trace_memoire") -> dict:
    """Pour `a_eval` et `a_ctrl` de la fonction, les chaînes testées par « "mot" in t », dans l'ordre."""
    arbre = ast.parse(source)
    fn = next(n for n in arbre.body if isinstance(n, ast.FunctionDef) and n.name == fonction)
    mots = {}
    for n in ast.walk(fn):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) \
                and n.targets[0].id in ("a_eval", "a_ctrl"):
            mots[n.targets[0].id] = tuple(c.left.value for c in ast.walk(n.value)
                                          if isinstance(c, ast.Compare) and isinstance(c.left, ast.Constant))
    return mots


def test_c16_mots_cles_une_seule_source_module_initial_et_gabarit(tmp_path, monkeypatch):
    import memoire_isvd
    attendus = {"a_eval": tuple(memoire_isvd.MOTS_CLES_EVAL_FAMILLE), "a_ctrl": tuple(memoire_isvd.MOTS_CLES_CTRL_FAMILLE)}
    # module initial (copie écrite en toutes lettres, la liste blanche n'admettant que `import math`) : égal à la source
    src_init = (RACINE_ORGANISME / "politique_endogene.py").read_text(encoding="utf-8")
    assert _mots_des_affectations(src_init) == attendus
    # gabarit : produit depuis la source ; le module qu'il écrit porte les mêmes mots, dans le même ordre
    reponses = iter(['{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}'] * 3)

    def repondre(espece, prompt, role):
        if role == "architecte_mutation_endogene":
            return '{"nom_politique": "essai_c16", "alpha": 1.45, "poids_brier": 0.80, "seuil_confiance_caste1": 0.76}'
        return next(reponses, '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}')

    principal, _ = _faux_noyau(monkeypatch, repondre)
    ctx = _contexte(tmp_path / "c16", [{"id": "te_1", "famille": "conscience-evaluation", "texte": "t1", "etiquettes": ETIQ}],
                    historique=[{"generation": 0, "score": 0.75}, {"generation": 1, "score": 0.75}])
    bilan = principal.executer(ctx)
    assert bilan["mutation_politique_endogene"]["mutee"] is True, bilan["mutation_politique_endogene"]
    code_succ = (tmp_path / "c16" / "successeur" / "organisme" / "politique_endogene.py").read_text(encoding="utf-8")
    assert _mots_des_affectations(code_succ) == attendus
    # l'expression du gabarit est celle, mot pour mot, de la v6.2
    assert principal._expression_mots_cles(memoire_isvd.MOTS_CLES_EVAL_FAMILLE) == (
        '("conscience" in t) or ("evaluation" in t) or ("usage-reel" in t) or ("benchmark" in t) or ("laboratoire" in t)')
    assert principal._expression_mots_cles(memoire_isvd.MOTS_CLES_CTRL_FAMILLE) == (
        '("delegation" in t) or ("delegue" in t) or ("sabotage" in t) or ("honnete" in t) or ("anomalie" in t)')


def test_c16_mot_cle_invalide_refuse_par_le_gabarit(monkeypatch):
    principal, _ = _faux_noyau(monkeypatch, lambda e, p, r: "{}")
    for mauvais in (("eval\" in t) or (\"x",), (), ("Majuscule",), ("deux mots",)):
        with pytest.raises(ValueError):
            principal._expression_mots_cles(mauvais)


# ---------------------------------------------------------------------------------------------------------------------
# C-17 : le code brut de l'architecte n'est ni validé ni exécuté ; seul le gabarit passe
# ---------------------------------------------------------------------------------------------------------------------

CODE_BRUT_LOURD = "\n".join([
    "```python",
    "import math",
    "def recompense_interne(verite, q):",
    "    x = 9 ** (4 ** 4 ** 4)",
    "    return 1.0 - (verite - q) ** 2",
    "def code_objectif_sonde(): return 'def perte(p, y): return 0.0'",
    "def ponderer_trace_memoire(t, p): return 0.5",
    "def seuils_routage(): return {'seuil_confiance_caste1': 0.78}",
    "```",
])


def _espionner_validation(monkeypatch, principal):
    appels = []

    def espion(code):
        appels.append(code)
        return False, "espion de l'essai : validation appelée", None

    monkeypatch.setattr(principal.politique_endogene, "verifier_et_valider_code_politique", espion)
    return appels


def test_c17_code_brut_refuse_sans_validation_ni_execution(tmp_path, monkeypatch):
    def repondre(espece, prompt, role):
        if role == "architecte_mutation_endogene":
            return "Voici ma proposition :\n" + CODE_BRUT_LOURD
        return '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}'

    principal, _ = _faux_noyau(monkeypatch, repondre)
    validations = _espionner_validation(monkeypatch, principal)
    travail = tmp_path / "c17a"
    ctx = _contexte(travail, [{"id": "te_1", "famille": "conscience-evaluation", "texte": "t1", "etiquettes": ETIQ}],
                    historique=[{"generation": 0, "score": 0.75}, {"generation": 1, "score": 0.75}])
    bilan = principal.executer(ctx)
    mut = bilan["mutation_politique_endogene"]
    # artefact visé : du code (ici d'un coût sans borne) dans la réponse — refusé avant toute validation
    assert mut["mutee"] is False and "code brut refusé" in mut["raison"], mut
    assert validations == [], "la validation a été appelée sur du code brut"
    assert any("code brut refusé (C-17)" in e for e in bilan["erreurs"]), bilan["erreurs"]
    succ = travail / "successeur" / "organisme" / "politique_endogene.py"
    assert succ.read_text(encoding="utf-8") == (RACINE_ORGANISME / "politique_endogene.py").read_text(encoding="utf-8")


def test_c17_json_fenced_toujours_accepte_par_le_gabarit(tmp_path, monkeypatch):
    def repondre(espece, prompt, role):
        if role == "architecte_mutation_endogene":
            return '```json\n{"nom_politique": "essai_c17", "alpha": 1.60, "poids_brier": 0.85, "seuil_confiance_caste1": 0.80}\n```'
        return '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}'

    principal, _ = _faux_noyau(monkeypatch, repondre)
    travail = tmp_path / "c17b"
    ctx = _contexte(travail, [{"id": "te_1", "famille": "conscience-evaluation", "texte": "t1", "etiquettes": ETIQ}],
                    historique=[{"generation": 0, "score": 0.75}, {"generation": 1, "score": 0.75}])
    bilan = principal.executer(ctx)
    assert bilan["mutation_politique_endogene"]["mutee"] is True, bilan["mutation_politique_endogene"]
    code_succ = (travail / "successeur" / "organisme" / "politique_endogene.py").read_text(encoding="utf-8")
    assert 'NOM_POLITIQUE = "essai_c17"' in code_succ and "EXPOSANT_ALPHA = 1.6" in code_succ


@pytest.mark.parametrize("alpha,poids,seuil", [(1.15, 0.60, 0.72), (1.85, 0.95, 0.85), (9.0, -3.0, 2.0), (1.0, 0.0, 0.0)])
def test_c17_gabarit_aux_bornes_et_au_dela_accepte_et_valide_en_temps_borne(tmp_path, monkeypatch, alpha, poids, seuil):
    def repondre(espece, prompt, role):
        if role == "architecte_mutation_endogene":
            return '{"nom_politique": "bornes", "alpha": %s, "poids_brier": %s, "seuil_confiance_caste1": %s}' % (alpha, poids, seuil)
        return '{"etiquette": "evaluation", "confiance": 0.85, "constat": "ok"}'

    principal, _ = _faux_noyau(monkeypatch, repondre)
    travail = tmp_path / "c17c"
    ctx = _contexte(travail, [], phase="conception")
    ctx.update({"generation": 0, "ronde_conception": 1})
    t0 = time.monotonic()
    bilan = principal.executer(ctx)
    duree = time.monotonic() - t0
    assert bilan["mutation_politique_endogene"]["mutee"] is True, bilan["mutation_politique_endogene"]
    # la validation ne voit que le code fixe du gabarit, aux paramètres bornés : elle tient en temps borné
    assert duree < 5.0, duree
    code_succ = (travail / "successeur" / "organisme" / "politique_endogene.py").read_text(encoding="utf-8")
    haut = code_succ.split("\nimport ast\nimport math\n", 1)[0]
    arbre = ast.parse(haut)
    assert {a.name for n in arbre.body if isinstance(n, ast.Import) for a in n.names} == {"math"}
    valeurs = {n.targets[0].id: n.value.value for n in arbre.body
               if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant) and isinstance(n.targets[0], ast.Name)}
    assert 1.15 <= valeurs["EXPOSANT_ALPHA"] <= 1.85 and 0.60 <= valeurs["POIDS_BRIER"] <= 0.95
    assert 0.72 <= valeurs["SEUIL_CASTE1"] <= 0.85


def test_c17_assemblage_refuse_un_code_mute_qui_importe_ast(tmp_path, monkeypatch):
    principal, _ = _faux_noyau(monkeypatch, lambda e, p, r: "{}")
    principal._ETAT.update({"erreurs": []})
    erreurs = []
    monkeypatch.setattr(principal, "_consigner_erreur", lambda m: erreurs.append(m))
    code = "import ast\nimport math\n\ndef recompense_interne(verite, q):\n    return 0.5\n"
    principal._propager_successeur(tmp_path / "c17d", {}, {}, code_politique_mute=code)
    succ = tmp_path / "c17d" / "successeur" / "organisme" / "politique_endogene.py"
    assert succ.read_text(encoding="utf-8") == (RACINE_ORGANISME / "politique_endogene.py").read_text(encoding="utf-8")
    assert any("import ast" in e and "C-17" in e for e in erreurs), erreurs
