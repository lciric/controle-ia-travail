# -*- coding: utf-8 -*-
"""Tests de l'enveloppe v2 (`organisme/`) sous un faux `noyau_client`, dans un sous-processus `python -I -s`, comme le
lanceur du bac à sable du noyau. Chaque garde est éprouvée sur un cas sain et sur un artefact (R5)."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parent.parent
FAMILLES = {"conscience-evaluation": ["evaluation", "usage-reel"], "controle-delegation": ["sabotage", "honnete"]}


def _taches(prefixe, n_par_famille, avec_verite):
    sortie = []
    for fam, (pos, neg) in FAMILLES.items():  # comme la banque du noyau : une famille après l'autre
        for i in range(n_par_famille):
            t = {"id": f"{prefixe}-{fam[:4]}-{i:02d}", "famille": fam, "texte": f"Extrait {i} de {fam}.", "etiquettes": [pos, neg]}
            if avec_verite:
                t["verite"] = pos if i % 2 == 0 else neg
            sortie.append(t)
    return sortie


def _preparer(tmp_path, organisme=None, generation=0, appels_max=60, temps_max_s=600, pannes=None, delai_s=0.0,
              confrontation=False, nom="travail", **options):
    travail = tmp_path / nom
    travail.mkdir()
    shutil.copytree(organisme or (RACINE / "organisme"), travail / "organisme")
    shutil.copy(RACINE / "tests" / "faux_noyau_client.py", travail / "noyau_client.py")
    (travail / "faux_noyau.json").write_text(json.dumps(dict({"appels_max": appels_max, "pannes": pannes or {}, "delai_s": delai_s},
                                                             **options)), encoding="utf-8")
    contexte = {"generation": generation, "lignee": "gemini-v2", "mission": "Mission de test : deux familles.",
                "dossier_travail": str(travail), "dossier_archive": str(tmp_path / "archive"),
                "taches_entrainement": _taches("tr", 12, True), "taches_test": _taches("te", 8, False),
                "budget": {"appels_max": appels_max, "usd_max": 5.0, "temps_max_s": temps_max_s}, "historique": []}
    if confrontation:
        contexte["confrontation"] = True
    (travail / "contexte.json").write_text(json.dumps(contexte, ensure_ascii=False), encoding="utf-8")
    return travail


def _executer(travail, timeout=300):
    code = ("import sys, os, json; sys.path.insert(0, os.path.join(os.getcwd(), 'organisme')); sys.path.insert(0, os.getcwd()); "
            "import principal; print(principal.executer(json.load(open('contexte.json', encoding='utf-8'))))")
    r = subprocess.run([sys.executable, "-I", "-s", "-B", "-c", code], cwd=travail, capture_output=True, text=True, timeout=timeout)
    assert r.returncode == 0, r.stderr[-3000:]
    return r.stdout


def _journal(travail, g=0):
    f = travail / "runs_debogage" / f"g{g:03d}" / "journal_appels.jsonl"
    return [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]


def _invites(travail):
    return [json.loads(l) for l in (travail / "faux_noyau_invites.jsonl").read_text(encoding="utf-8").splitlines()]


def test_generation_0_saine_bout_en_bout(tmp_path):
    travail = _preparer(tmp_path)
    _executer(travail)
    reponses = json.loads((travail / "reponses_test.json").read_text(encoding="utf-8"))
    assert len(reponses) == 16, "chaque tâche de test reçoit une réponse"
    succ = travail / "successeur" / "organisme"
    assert (succ / "manifeste.json").exists() and (succ / "principal.py").exists()
    for f in ("definition.md", "calculer.py", "attaques.json"):
        assert (succ / "metrique" / f).exists(), f
    substrat = json.loads((succ / "SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json").read_text(encoding="utf-8"))
    store = substrat["custom_swarm_memory_store"]
    assert store["isvd_state"]["r_max"] == 6 and store["regles_de_decision"] and store["dernier_guide"]
    assert len(_journal(travail)) <= 60
    trace = json.loads((travail / "runs_debogage" / "g000" / "trace_etapes.json").read_text(encoding="utf-8"))
    etapes = [e["etape"] for e in trace["etapes"]]
    for e in ("plan", "M3_mitose", "M2_sondes", "M1_extraction", "M0_synthese", "ETIQUETAGE_lot", "METRIQUE"):
        assert e in etapes, e
    assert not any(p.name.endswith(".secours.json") for p in succ.iterdir())


def test_exemples_stratifies_les_deux_familles_sont_vues(tmp_path):
    travail = _preparer(tmp_path)
    _executer(travail)
    premiere = next(i for i in _invites(travail) if i["role"].startswith("M3_C1_"))
    exemples = premiere["prompt"].split("EXEMPLES D'ENTRAÎNEMENT :", 1)[1].split("[PROTOCOLE", 1)[0]
    assert "conscience-evaluation" in exemples and "controle-delegation" in exemples
    assert "vérité : evaluation" in exemples and "vérité : usage-reel" in exemples


def test_mitose_suit_le_moteur_lignees_hybrides_et_arret(tmp_path):
    travail = _preparer(tmp_path)
    _executer(travail)
    inv = _invites(travail)
    cell1 = next(i for i in inv if i["role"].startswith("M3_C1_"))
    assert cell1["espece"] == "GEMINI_ARGON"
    critiques = [i for i in inv if i["role"].endswith("_crit")]
    assert all(len(i["role"]) <= 40 for i in inv), "les rôles tiennent dans les 40 caractères du noyau"
    assert critiques, "les cellules hybrides font deux appels réels"
    journal = _journal(travail)
    assert all(e.get("temperature_transmise") is False for e in journal if "temperature_tiree" in e)
    trace = json.loads((travail / "runs_debogage" / "g000" / "trace_etapes.json").read_text(encoding="utf-8"))
    fin = next(e for e in trace["etapes"] if e["etape"] == "M3_mitose")
    assert fin["arret"] in ("arrêt spectral (seuils du moteur)", "budget de l'étage épuisé", "garde de temps")


def test_pannes_refus_et_modele_non_conforme_comptes_a_part(tmp_path):
    travail = _preparer(tmp_path, pannes={"M3_W1_C3_": "REFUS", "M3_W1_C5_": "MODELE_NON_CONFORME", "M2_Onsager_1": "ECHEC_API"})
    _executer(travail)
    statuts = [e["statut"] for e in _journal(travail) if "statut_noyau" in e]
    assert "refus" in statuts and "modele_non_conforme" in statuts and "echec_api" in statuts
    assert len(json.loads((travail / "reponses_test.json").read_text(encoding="utf-8"))) == 16


def test_plafond_du_noyau_arrete_proprement(tmp_path):
    travail = _preparer(tmp_path, appels_max=60)
    (travail / "faux_noyau.json").write_text(json.dumps({"appels_max": 7, "pannes": {}, "delai_s": 0.0}), encoding="utf-8")
    sortie = _executer(travail)
    assert "plafond" in sortie
    assert (travail / "reponses_test.json").exists() and (travail / "successeur" / "organisme" / "manifeste.json").exists()
    servis = [e for e in _journal(travail) if e.get("statut") != "plafond_noyau"]
    assert len(servis) <= 7, "aucun appel servi au-delà du plafond du noyau"
    assert any(e.get("statut") == "plafond_noyau" for e in _journal(travail))


def test_garde_de_temps_preserve_les_reponses(tmp_path):
    travail = _preparer(tmp_path, temps_max_s=4, delai_s=1.0)
    _executer(travail, timeout=120)
    trace = json.loads((travail / "runs_debogage" / "g000" / "trace_etapes.json").read_text(encoding="utf-8"))
    fin = next(e for e in trace["etapes"] if e["etape"] == "M3_mitose")
    assert fin["arret"] == "garde de temps"
    assert json.loads((travail / "reponses_test.json").read_text(encoding="utf-8")), "les réponses sont écrites malgré la garde"


def test_confrontation_ni_successeur_ni_metrique(tmp_path):
    travail = _preparer(tmp_path, generation=-1, confrontation=True)
    _executer(travail)
    assert not (travail / "successeur").exists()
    assert not any(i["role"].startswith("METRIQUE") for i in _invites(travail))
    assert len(json.loads((travail / "reponses_test.json").read_text(encoding="utf-8"))) == 16


def test_generation_1_herite_memoire_et_metrique(tmp_path):
    t0 = _preparer(tmp_path, nom="g0")
    _executer(t0)
    t1 = _preparer(tmp_path, organisme=t0 / "successeur" / "organisme", generation=1, nom="g1")
    _executer(t1)
    inv = _invites(t1)
    assert not any(i["role"].startswith("METRIQUE") for i in inv), "la métrique héritée n'est pas réélaborée"
    assert any("mémoire spectrale tronquée" in i["prompt"] for i in inv if i["role"].startswith("M3_W")), \
        "la mémoire de la génération 0 est projetée dans les invites"


def test_metrique_invalide_n_est_pas_donnee_au_successeur(tmp_path):
    travail = _preparer(tmp_path, pannes={"METRIQUE_ecriture": "VIDE"})
    _executer(travail)
    assert not (travail / "successeur" / "organisme" / "metrique").exists()


def test_valider_metrique_sain_et_artefacts(monkeypatch):
    import importlib
    import types
    faux = types.ModuleType("noyau_client")
    faux.appeler, faux.especes, faux.budget = (lambda *a, **k: {}), (lambda: []), (lambda: {})
    monkeypatch.setitem(sys.modules, "noyau_client", faux)
    monkeypatch.syspath_prepend(str(RACINE / "organisme"))
    for nom in ("principal", "adaptateur_noyau"):
        sys.modules.pop(nom, None)
    principal = importlib.import_module("principal")
    familles = [("conscience-evaluation", ("evaluation", "usage-reel")), ("controle-delegation", ("sabotage", "honnete"))]
    attaque = {"id": "a", "famille": "f", "texte": "t", "etiquettes": ["evaluation", "usage-reel"], "verite": "evaluation"}
    sain = {"definition.md": "x", "calculer.py": "def calculer(d):\n    return 0.0\n", "attaques.json": json.dumps([attaque])}
    assert principal.valider_metrique(sain, familles) == []
    assert principal.valider_metrique(dict(sain, **{"calculer.py": "def calculer(:"}), familles)
    autre = dict(attaque, etiquettes=["x", "y"], verite="x")
    assert principal.valider_metrique(dict(sain, **{"attaques.json": json.dumps([autre])}), familles)
    assert principal.valider_metrique(dict(sain, **{"attaques.json": json.dumps([attaque, attaque])}), familles)
    assert principal.valider_metrique({k: v for k, v in sain.items() if k != "definition.md"}, familles)
    assert principal.halton(1, 2) == 0.5 and principal.halton(3, 2) == 0.75
    plan = principal.planifier(60, 16, True)
    assert plan["lots_etiquettes"] == 2 and plan["metrique"] == 5 and plan["m3"] + plan["m2"] + plan["m1_max"] + 2 + 1 + 5 <= 60


# -- v3 : plancher de l'arrêt spectral, reprise de l'étiquetage, lecture des étiquettes -----------------------------
def _module_principal(monkeypatch):
    import importlib
    import types
    faux = types.ModuleType("noyau_client")
    faux.appeler, faux.especes, faux.budget = (lambda *a, **k: {}), (lambda: []), (lambda: {})
    monkeypatch.setitem(sys.modules, "noyau_client", faux)
    monkeypatch.syspath_prepend(str(RACINE / "organisme"))
    for nom in ("principal", "adaptateur_noyau"):
        sys.modules.pop(nom, None)
    return importlib.import_module("principal")


def test_plancher_de_l_arret_spectral_regle(monkeypatch):
    principal = _module_principal(monkeypatch)
    assert principal.plancher_m3(220) == 125 and principal.plancher_m3(37) == 22 and principal.plancher_m3(0) == 0
    assert not principal.arret_spectral(13, 22, 0.0, 0.0), "sous le plancher, le critère n'est jamais consulté"
    assert principal.arret_spectral(22, 22, 0.1, 0.5) and principal.arret_spectral(30, 22, 0.9, 0.01)
    assert not principal.arret_spectral(30, 22, 0.9, 0.5), "au-delà du plancher, gain et λ min au-dessus des seuils"


def test_mitose_ne_s_arrete_pas_avant_le_plancher(tmp_path):
    travail = _preparer(tmp_path, m3_identiques=True)  # contributions identiques : gain nul dès la première vague
    _executer(travail)
    trace = json.loads((travail / "runs_debogage" / "g000" / "trace_etapes.json").read_text(encoding="utf-8"))
    vagues = [e for e in trace["etapes"] if e["etape"] == "M3_vague"]
    fin = next(e for e in trace["etapes"] if e["etape"] == "M3_mitose")
    assert vagues[0]["gain_par_cellule"] < 0.42 and not vagues[0]["plancher_atteint"]
    assert len(vagues) >= 2, "la v2 s'arrêtait ici, après la première vague"
    assert fin["arret"] == "arrêt spectral (seuils du moteur)" and fin["appels_m3"] >= fin["plancher_appels"] > 13


def test_reprise_d_un_lot_en_echec(tmp_path):
    travail = _preparer(tmp_path, pannes={"ETIQUETAGE_lot1": "ECHEC_API"})
    _executer(travail)
    assert len(json.loads((travail / "reponses_test.json").read_text(encoding="utf-8"))) == 16, "le lot en échec est repris"
    trace = json.loads((travail / "runs_debogage" / "g000" / "trace_etapes.json").read_text(encoding="utf-8"))
    reprises = [e for e in trace["etapes"] if e["etape"] == "ETIQUETAGE_reprise"]
    assert reprises and sum(e.get("reponses", 0) for e in reprises) == 8
    assert any(e["etape"] == "METRIQUE" and e.get("tentative") for e in trace["etapes"]), "la réserve de la métrique tient"
    assert (travail / "successeur" / "organisme" / "metrique" / "calculer.py").exists()
    assert len(_journal(travail)) <= 60


def test_lire_etiquettes_sain_et_artefacts(monkeypatch):
    principal = _module_principal(monkeypatch)
    lot = [{"id": "a", "etiquettes": ["Evaluation", "usage-reel"]}, {"id": "b", "etiquettes": ["sabotage", "honnete"]}]
    lu = principal.lire_etiquettes('```json\n{"reponses": {"a": {"etiquette": "evaluation", "confiance": 0.7}, '
                                   '"b": {"etiquette": "inconnue", "confiance": 0.9}}}\n```', lot)
    assert lu == {"a": {"etiquette": "Evaluation", "confiance": 0.7}}, "forme de la tâche ; étiquette hors tâche refusée"
    seul = [lot[1]]
    assert principal.lire_etiquettes('Faits.\n{"etiquette": "honnete", "confiance": 2}', seul) == \
        {"b": {"etiquette": "honnete", "confiance": 1.0}}, "objet seul pour un lot d'une tâche, confiance bornée"
    assert principal.lire_etiquettes('{"etiquette": "honnete"}', lot) == {}, "objet seul refusé pour un lot de plusieurs"
    assert principal.lire_etiquettes("La trace montre un sabotage, pas un comportement honnete.", seul) == {}, \
        "aucune lecture par présence d'un mot"
    assert principal.lire_etiquettes('{"reponses": {"b": {"etiquette": "sabotage", "confiance": "NaN"}}}', seul)["b"]["confiance"] == 0.5
