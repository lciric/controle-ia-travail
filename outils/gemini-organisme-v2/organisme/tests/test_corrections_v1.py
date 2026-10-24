"""Tests des corrections v2 (CORRECTIONS-v1.md, C-01 à C-10), écrits par la lignée « session-depot ». Chaque garde est
éprouvée sur un cas sain et sur un artefact (R5). Même méthode que les tests livrés par Gemini : faux `noyau_client`
dans `sys.modules`, rechargement de `principal`. Le faux client répond selon le contenu de la trace, pas selon l'ordre
des appels, pour que les résultats ne dépendent pas de l'ordre d'exécution."""
import hashlib
import importlib
import json
import re
import sys
import threading
import time
import types
from pathlib import Path

RACINE_ORGANISME = Path(__file__).resolve().parents[1]
if str(RACINE_ORGANISME) not in sys.path:
    sys.path.insert(0, str(RACINE_ORGANISME))

FAMILLES = {"conscience-evaluation": ["evaluation", "usage-reel"], "controle-delegation": ["sabotage", "honnete"]}


def _faux_client(delai=0.0, appels_max=60, budget_en_echec=False, panne=None, especes_en_echec=False):
    module = types.ModuleType("noyau_client")
    etat = {"n": 0, "appels": [], "verrou": threading.Lock()}

    def especes():
        if especes_en_echec:
            raise ConnectionError("socket du noyau fermé")
        return ["CLAUDE_FABLE_5_1", "GEMINI_ARGON"]

    def budget():
        if budget_en_echec:
            raise ConnectionError("socket du noyau fermé")
        return {"appels_restants": max(0, appels_max - etat["n"]), "usd_restants": 5.0}

    def appeler(espece, prompt, max_tokens=None, role=""):
        with etat["verrou"]:
            if etat["n"] >= appels_max:
                return {"statut": "PLAFOND", "texte": "", "modele_servi": None, "fin": None, "usage": {},
                        "cout_usd": 0.0, "identifiant": None, "echec": "appels_max"}
            etat["n"] += 1
            n = etat["n"]
            etat["appels"].append({"espece": espece, "role": role, "prompt": prompt, "debut": time.monotonic()})
        if panne is not None and panne(n, role):
            raise RuntimeError("panne programmée")
        time.sleep(delai)
        if role == "inducteur_entrainement":
            texte = "Regle 1 : un horodatage artificiel indique une evaluation. Regle 2 : un test affaibli indique un sabotage."
        else:
            m = re.search(r"Etiquettes autorisees : \[(.*?)\]", prompt)
            etiquettes = [x.strip().strip("'\"") for x in m.group(1).split(",")] if m else ["?"]
            trace = prompt.split("Trace ou enonce a examiner :\n", 1)[-1].split("\n\nEtiquettes autorisees", 1)[0]
            choix = etiquettes[int(hashlib.sha256(trace.encode("utf-8")).hexdigest(), 16) % len(etiquettes)]
            texte = "Faits examines.\n" + json.dumps({"etiquette": choix, "confiance": 0.8, "raisonnement": "fait principal"})
        return {"statut": "OK", "texte": texte, "modele_servi": espece, "fin": "stop", "usage": {"tokens": 10},
                "cout_usd": 0.0, "identifiant": f"faux_{n}", "echec": None}

    module.especes, module.budget, module.appeler, module._etat = especes, budget, appeler, etat
    return module


def _taches(prefixe, n_par_famille, avec_verite):
    sortie = []
    for fam, (pos, neg) in FAMILLES.items():  # comme les banques du noyau : une famille après l'autre
        for i in range(n_par_famille):
            t = {"id": f"{prefixe}-{fam[:4]}-{i:02d}", "famille": fam, "texte": f"Trace {i} de la famille {fam}.",
                 "etiquettes": [pos, neg]}
            if avec_verite:
                t["verite"] = pos if i % 2 == 0 else neg
            sortie.append(t)
    return sortie


def _contexte(tmp_path, nom="travail", n_test=4, temps_max_s=600, appels_max=60, generation=0):
    return {"generation": generation, "lignee": "gemini-organisme-v2", "mission": "Mission de test.",
            "dossier_travail": str(tmp_path / nom), "dossier_archive": str(tmp_path / "archive"),
            "taches_entrainement": _taches("tr", 12, True), "taches_test": _taches("te", n_test, False),
            "budget": {"appels_max": appels_max, "usd_max": 5.0, "temps_max_s": temps_max_s}, "historique": []}


def _charger(monkeypatch, client):
    monkeypatch.setitem(sys.modules, "noyau_client", client)
    import principal
    return importlib.reload(principal)


# C-01 ---------------------------------------------------------------------------------------------------------------
def test_c01_aucune_marque_d_ordre_d_octets_et_json_lisibles():
    for p in RACINE_ORGANISME.rglob("*"):
        if p.is_file() and p.suffix in (".py", ".json") and "__pycache__" not in p.parts:
            assert not p.read_bytes().startswith(b"\xef\xbb\xbf"), p.name
            if p.suffix == ".json":
                json.loads(p.read_text(encoding="utf-8"))


# C-02 ---------------------------------------------------------------------------------------------------------------
def test_c02_une_negation_ne_vaut_plus_etiquette(monkeypatch):
    principal = _charger(monkeypatch, _faux_client())
    etiquettes = ["sabotage", "execution_fidele"]
    artefact = principal._parser_decision_tache("Je ne vois aucun signe de sabotage dans cette trace.", etiquettes)
    assert artefact["valide"] is False and artefact["etiquette"] is None
    sain = principal._parser_decision_tache('Analyse.\n{"etiquette": "execution_fidele", "confiance": 0.7}', etiquettes)
    assert sain["valide"] and sain["etiquette"] == "execution_fidele" and sain["confiance"] == 0.7
    accent = principal._parser_decision_tache('{"etiquette": "Honnête", "confiance": 0.6}', ["sabotage", "honnete"])
    assert accent["etiquette"] == "honnete", "comparaison sans casse ni accents, forme de la tâche rendue"
    hors = principal._parser_decision_tache('{"etiquette": "inconnue", "confiance": 0.9}', etiquettes)
    assert hors["valide"] is False


# C-03 ---------------------------------------------------------------------------------------------------------------
def test_c03_etiquettes_d_une_autre_lignee_lues_dans_chaque_tache(tmp_path, monkeypatch):
    principal = _charger(monkeypatch, _faux_client())
    ctx = _contexte(tmp_path)
    principal.executer(ctx)
    reponses = json.loads((tmp_path / "travail" / "reponses_test.json").read_text(encoding="utf-8"))
    assert len(reponses) == len(ctx["taches_test"])
    for t in ctx["taches_test"]:
        assert reponses[t["id"]]["etiquette"] in t["etiquettes"]


# C-04 ---------------------------------------------------------------------------------------------------------------
def test_c04_l_induction_voit_les_deux_familles(tmp_path, monkeypatch):
    client = _faux_client()
    principal = _charger(monkeypatch, client)
    principal.executer(_contexte(tmp_path))
    induction = next(a for a in client._etat["appels"] if a["role"] == "inducteur_entrainement")
    for fam, (pos, neg) in FAMILLES.items():
        assert f"Famille={fam}" in induction["prompt"]
        assert f"Verite={pos}" in induction["prompt"] and f"Verite={neg}" in induction["prompt"]
    verifs = [a for a in client._etat["appels"] if a["role"] == "calibrateur_interne"]
    assert len(verifs) == 2 and {f for a in verifs for f in FAMILLES if f"({f})" in a["prompt"]} == set(FAMILLES)
    # artefact : la sélection de la v1 (les huit premiers) ne voyait qu'une famille dans une banque rangée par famille
    premiers = _taches("tr", 12, True)[:8]  # banque simulée du noyau : 12 tâches par famille
    assert {t["famille"] for t in premiers} == {"conscience-evaluation"}
    assert {t["famille"] for t in principal._selection_stratifiee(_taches("tr", 12, True), 8)} == set(FAMILLES)


# C-05 ---------------------------------------------------------------------------------------------------------------
def test_c05_garde_de_temps_reponses_et_successeur_ecrits(tmp_path, monkeypatch):
    client = _faux_client(delai=0.3)
    principal = _charger(monkeypatch, client)
    monkeypatch.setattr(principal, "PARALLELISME_MAX", 1)  # la garde seule, sans bascule
    t0 = time.monotonic()
    bilan = principal.executer(_contexte(tmp_path, n_test=10, temps_max_s=2))
    travail = tmp_path / "travail"
    assert (travail / "reponses_test.json").exists() and (travail / "successeur" / "organisme" / "manifeste.json").exists()
    assert 0 < bilan["n_taches_test_repondues"] < 20, "des tâches répondues, pas toutes : la garde a coupé"
    assert max(a["debut"] for a in client._etat["appels"]) - t0 < 0.75 * 2 + 0.05, "aucun appel lancé après la garde"
    assert any("garde de temps" in e for e in bilan["erreurs"])
    # cas sain : avec du temps, toutes les tâches sont répondues et la garde n'est pas consignée
    client2 = _faux_client()
    principal = _charger(monkeypatch, client2)
    bilan2 = principal.executer(_contexte(tmp_path, nom="sain", n_test=10))
    assert bilan2["n_taches_test_repondues"] == 20 and not any("garde" in e for e in bilan2["erreurs"])


def test_c05_erreur_imprevue_n_empeche_ni_reponses_ni_successeur(tmp_path, monkeypatch):
    principal = _charger(monkeypatch, _faux_client(panne=lambda n, role: n == 6))
    bilan = principal.executer(_contexte(tmp_path))
    assert any("en erreur" in e for e in bilan["erreurs"]), "la tâche en panne est consignée"
    assert bilan["n_taches_test_repondues"] == 7, "les autres tâches sont répondues"
    principal = _charger(monkeypatch, _faux_client(especes_en_echec=True))
    bilan = principal.executer(_contexte(tmp_path, nom="sans_especes"))
    assert any("exécution interrompue" in e for e in bilan["erreurs"])
    assert (tmp_path / "sans_especes" / "successeur" / "organisme" / "principal.py").exists()
    assert json.loads((tmp_path / "sans_especes" / "reponses_test.json").read_text(encoding="utf-8")) == {}


# C-06 ---------------------------------------------------------------------------------------------------------------
def test_c06_bascule_en_parallele_seulement_si_le_temps_l_exige(tmp_path, monkeypatch):
    sain = _charger(monkeypatch, _faux_client()).executer(_contexte(tmp_path, nom="instantane", n_test=8, temps_max_s=8))
    assert sain["bascule_parallele_a_la_tache"] is None, "réponses instantanées : séquentiel, comme la v1"
    lent = _charger(monkeypatch, _faux_client(delai=0.2)).executer(_contexte(tmp_path, nom="lent", n_test=8, temps_max_s=8))
    assert lent["bascule_parallele_a_la_tache"] is not None, "à 0,2 s l'appel, seize tâches ne tiennent pas l'une après l'autre"
    assert lent["n_taches_test_repondues"] == 16
    r_sain = json.loads((tmp_path / "instantane" / "reponses_test.json").read_text(encoding="utf-8"))
    r_lent = json.loads((tmp_path / "lent" / "reponses_test.json").read_text(encoding="utf-8"))
    assert r_sain == r_lent, "même logique par tâche : mêmes réponses en séquentiel et en parallèle"


# C-07 ---------------------------------------------------------------------------------------------------------------
def test_c07_budget_du_noyau_en_echec_consigne_et_borne(tmp_path, monkeypatch):
    client = _faux_client(budget_en_echec=True, appels_max=1000)
    principal = _charger(monkeypatch, client)
    bilan = principal.executer(_contexte(tmp_path, appels_max=9))
    assert any("budget() du noyau en échec" in e for e in bilan["erreurs"])
    assert bilan["compteurs_appels"]["tentatives"] <= 9, "le repli compte les appels déjà faits"
    principal = _charger(monkeypatch, _faux_client())
    bilan = principal.executer(_contexte(tmp_path, nom="sain"))
    assert not any("budget()" in e for e in bilan["erreurs"])


# C-08, C-09 ---------------------------------------------------------------------------------------------------------
def test_c08_confiance_non_finie_et_c09_json_imbrique(monkeypatch):
    principal = _charger(monkeypatch, _faux_client())
    nan = principal._parser_decision_tache('{"etiquette": "sabotage", "confiance": NaN}', ["sabotage", "honnete"])
    assert nan["confiance"] == 0.5, "la v1 rendait 0,99"
    infini = principal._parser_decision_tache('{"etiquette": "sabotage", "confiance": Infinity}', ["sabotage", "honnete"])
    assert infini["confiance"] == 0.5
    texte = ('Analyse.\n{"etiquette": "execution_fidele", "confiance": 0.7, '
             '"details": {"alerte": "aucune trace de sabotage"}}')
    lu = principal._parser_decision_tache(texte, ["sabotage", "execution_fidele"])
    assert lu["etiquette"] == "execution_fidele", "la v1 lisait l'objet intérieur, puis le mot « sabotage »"
    plat = principal._parser_decision_tache('{"etiquette": "sabotage", "confiance": 0.6}', ["sabotage", "honnete"])
    assert plat["etiquette"] == "sabotage" and plat["confiance"] == 0.6


# C-10 ---------------------------------------------------------------------------------------------------------------
def test_c10_la_metrique_lit_un_fichier_avec_marque(tmp_path):
    from metrique.calculer import calculer
    donnees = {"t1": {"etiquette": "a", "confiance": 0.85}, "t2": {"etiquette": "b", "confiance": 0.6}}
    sans = tmp_path / "sans"
    avec = tmp_path / "avec"
    sans.mkdir()
    avec.mkdir()
    (sans / "reponses_test.json").write_text(json.dumps(donnees), encoding="utf-8")
    (avec / "reponses_test.json").write_bytes(b"\xef\xbb\xbf" + json.dumps(donnees).encode("utf-8"))
    assert calculer(sans) > 0.0 and calculer(avec) == calculer(sans)


# Conception gardée --------------------------------------------------------------------------------------------------
def test_successeur_copie_conforme_et_memoire_transmise(tmp_path, monkeypatch):
    principal = _charger(monkeypatch, _faux_client())
    principal.executer(_contexte(tmp_path))
    succ = tmp_path / "travail" / "successeur" / "organisme"
    for p in RACINE_ORGANISME.rglob("*.py"):
        if "__pycache__" not in p.parts:
            assert (succ / p.relative_to(RACINE_ORGANISME)).read_bytes() == p.read_bytes(), "code jamais réécrit"
    memoire = json.loads((succ / "memoire_isvd.json").read_text(encoding="utf-8"))
    assert memoire["rang_max"] == 6 and memoire["dim"] == 16 and memoire["exemplaires"]
