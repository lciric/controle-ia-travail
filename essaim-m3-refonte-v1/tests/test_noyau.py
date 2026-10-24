"""Tests du noyau, sans réseau : chaque garde sur un cas sain et sur un artefact (R5)."""
import json
import os
import pathlib
import shutil
import stat
import sys

import numpy as np
import pytest

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))

from essaim_m3.noyau import appels, archive, bac_a_sable, boucle, contrat, serveur, taches  # noqa: E402
from essaim_m3.simulateur import appelants_simules, organisme_en_texte  # noqa: E402

FIXTURE = RACINE / "tests" / "fixtures" / "organisme_factice"


def rng(graine=1):
    return np.random.default_rng(graine)


# ---------- contrat : extraction et validation ----------

def test_extraction_fichiers_sain_et_chemins_rejetes():
    texte = organisme_en_texte(FIXTURE)
    fichiers = contrat.extraire_fichiers(texte)
    assert "organisme/manifeste.json" in fichiers and "organisme/principal.py" in fichiers
    pirate = "<<<FICHIER organisme/../hors.py>>>\nx = 1\n<<<FIN FICHIER>>>\n<<<FICHIER organisme/a.so>>>\nb\n<<<FIN FICHIER>>>"
    assert contrat.extraire_fichiers(pirate) == {}


def test_validation_organisme_sain_et_artefacts(tmp_path):
    fichiers = contrat.extraire_fichiers(organisme_en_texte(FIXTURE))
    assert contrat.ecrire_organisme(fichiers, tmp_path / "sain") == []
    sans_manifeste = {k: v for k, v in fichiers.items() if not k.endswith("manifeste.json")}
    assert any("manifeste.json absent" in p for p in contrat.ecrire_organisme(sans_manifeste, tmp_path / "a1"))
    mauvaise_entree = dict(fichiers)
    mauvaise_entree["organisme/manifeste.json"] = json.dumps({"entree": "inexistant:executer"})
    assert any("introuvable" in p for p in contrat.ecrire_organisme(mauvaise_entree, tmp_path / "a2"))
    syntaxe = dict(fichiers)
    syntaxe["organisme/principal.py"] = "def executer(contexte):\n    return (\n"
    assert any("syntaxe" in p for p in contrat.ecrire_organisme(syntaxe, tmp_path / "a3"))


def test_validation_refuse_lien_symbolique(tmp_path):
    contrat.ecrire_organisme(contrat.extraire_fichiers(organisme_en_texte(FIXTURE)), tmp_path)
    (tmp_path / "organisme" / "lien.py").symlink_to("/etc/hostname")
    assert any("symbolique" in p for p in contrat.valider_organisme(tmp_path / "organisme"))


# ---------- couche d'appel ----------

def test_appelant_refuse_reel_sans_go_et_sans_appelants(tmp_path):
    with pytest.raises(appels.Arret):
        appels.Appelant(tmp_path, 1.0, appelants=None, reel=False)
    with pytest.raises(appels.Arret):
        appels.Appelant(tmp_path, 1.0, appelants=None, reel=True, go_id=None)


def test_appel_sain_journalise_et_erreur_jamais_texte(tmp_path):
    doubles, especes = appelants_simules(rng())
    a = appels.Appelant(tmp_path, 5.0, doubles)
    r = a.appeler("GEMINI_ARGON", "t", "Tâche de la famille « conscience-evaluation ». EXTRAIT :\nx\n\nCONNAISSANCES :\n- (aucune)", role="tache")
    assert r.ok and r.texte and r.modele_servi == "gemini-4-argon"
    especes["gemini-4-argon"].pannes = {"404": 1.0}
    r2 = a.appeler("GEMINI_ARGON", "t", "Tâche de la famille « conscience-evaluation ». EXTRAIT :\nx\n\nCONNAISSANCES :\n- (aucune)")
    assert r2.statut == "ECHEC_API" and r2.texte == ""
    lignes = a.lire_journal()
    assert len(lignes) == 2 and lignes[1]["statut"] == "ECHEC_API" and lignes[0]["sha256_prompt"]


def test_modele_non_conforme_est_un_echec(tmp_path):
    doubles, especes = appelants_simules(rng())
    especes["claude-fable-5-1"].pannes = {"modele_non_conforme": 1.0}
    a = appels.Appelant(tmp_path, 5.0, doubles)
    r = a.appeler("CLAUDE_FABLE_5_1", "t", "Tâche de la famille « controle-delegation ». EXTRAIT :\nx\n\nCONNAISSANCES :\n- (aucune)")
    assert r.statut == "MODELE_NON_CONFORME" and r.texte == ""


def test_plafond_usd_arrete(tmp_path):
    doubles, _ = appelants_simules(rng())
    a = appels.Appelant(tmp_path, 0.001, doubles)
    with pytest.raises(appels.Arret):
        a.appeler("CLAUDE_OPUS_5_5", "t", "x" * 10, max_tokens=64000)


# ---------- serveur ----------

def test_serveur_budget_appels_et_requetes_invalides(tmp_path):
    doubles, _ = appelants_simules(rng())
    a = appels.Appelant(tmp_path, 5.0, doubles)
    s = serveur.ServeurAppels(a, str(tmp_path / "s.sock"), appels_max=1)
    assert s.traiter({"op": "especes"})["especes"] == sorted(appels.ESPECES)
    assert s.traiter(None)["statut"] == "ANOMALIE"
    assert s.traiter({"op": "appeler", "espece": "INCONNUE", "prompt": "x"})["statut"] == "ANOMALIE"
    ok = s.traiter({"op": "appeler", "espece": "GEMINI_ARGON", "prompt": "Exploration libre"})
    assert ok["statut"] == "OK" and ok["texte"]
    plafond = s.traiter({"op": "appeler", "espece": "GEMINI_ARGON", "prompt": "Exploration libre"})
    assert plafond["statut"] == "PLAFOND" and plafond["texte"] == ""
    assert s.traiter({"op": "budget"})["appels_restants"] == 0


# ---------- bac à sable ----------

def _preparer(tmp_path, organisme=FIXTURE / "organisme", contexte=None):
    travail = tmp_path / "travail"
    ctx = contexte or {"generation": 0, "lignee": "t", "mission": "m", "dossier_travail": str(travail),
                       "dossier_archive": str(tmp_path / "archive"), "taches_entrainement": [], "taches_test": [],
                       "budget": {"appels_max": 5, "usd_max": 1.0, "temps_max_s": 30}, "historique": []}
    bac_a_sable.preparer(travail, organisme, ctx)
    return travail


def test_bac_a_sable_execute_sans_cle_ni_mandataire(tmp_path):
    org = tmp_path / "org"
    shutil.copytree(FIXTURE / "organisme", org)
    (org / "principal.py").write_text(
        "import os, json\n"
        "def executer(contexte):\n"
        "    with open(os.path.join(contexte['dossier_travail'], 'env.json'), 'w') as fh:\n"
        "        json.dump(dict(os.environ), fh)\n"
        "    return 'ok'\n", encoding="utf-8")
    os.environ["ANTHROPIC_API_KEY"] = "secret-de-test"
    os.environ["HTTPS_PROXY_TEST"] = "x"
    try:
        travail = _preparer(tmp_path, org)
        res = bac_a_sable.executer(travail, str(tmp_path / "s.sock"), temps_max_s=30)
    finally:
        del os.environ["ANTHROPIC_API_KEY"]
        del os.environ["HTTPS_PROXY_TEST"]
    assert res["code"] == "OK"
    env = json.loads((travail / "env.json").read_text())
    assert "ANTHROPIC_API_KEY" not in env and "HTTPS_PROXY" not in env and "HTTPS_PROXY_TEST" not in env
    assert env["ESSAIM_SOCKET"].endswith("s.sock")


def test_bac_a_sable_exception_et_delai(tmp_path):
    org = tmp_path / "org"
    shutil.copytree(FIXTURE / "organisme", org)
    (org / "principal.py").write_text("def executer(contexte):\n    raise RuntimeError('boum')\n", encoding="utf-8")
    travail = _preparer(tmp_path, org)
    res = bac_a_sable.executer(travail, str(tmp_path / "s.sock"), temps_max_s=30)
    assert res["code"] == "EXCEPTION" and "boum" in res["statut"]["erreur"]
    (org / "principal.py").write_text("import time\ndef executer(contexte):\n    time.sleep(30)\n", encoding="utf-8")
    travail2 = _preparer(tmp_path / "b", org)
    res2 = bac_a_sable.executer(travail2, str(tmp_path / "s2.sock"), temps_max_s=2)
    assert res2["code"] == "DELAI_DEPASSE" and res2["delai_depasse"]


def test_bac_a_sable_isolation_reseau_refusee_si_indisponible(tmp_path, monkeypatch):
    monkeypatch.setattr(bac_a_sable, "isolation_reseau_disponible", lambda: False)
    travail = _preparer(tmp_path)
    res = bac_a_sable.executer(travail, str(tmp_path / "s.sock"), temps_max_s=5, isoler_reseau=True)
    assert res["code"] == "ISOLATION_INDISPONIBLE"


# ---------- archive ----------

def test_archive_scelle_et_ne_reecrit_jamais(tmp_path):
    a = archive.Archive(tmp_path / "archive")
    travail = tmp_path / "travail"
    travail.mkdir()
    (travail / "reponses_test.json").write_text("{}")
    ligne = a.deposer("l", 0, FIXTURE / "organisme", travail, None, {"score": 0.5}, {"statut": "OK", "cout_usd": 0.0, "n_appels": 0, "successeur": False})
    d = tmp_path / "archive" / "l" / "g000"
    assert (d / "organisme.tar.gz.sha256").exists() and (d / "score.json.sha256").exists() and ligne["empreinte_organisme"]
    assert a.historique("l") == [{"generation": 0, "lignee": "l", "score": 0.5, "statut": "OK", "cout_usd": 0.0, "n_appels": 0}]
    with pytest.raises(FileExistsError):
        a.deposer("l", 0, FIXTURE / "organisme", travail, None, {"score": 0.6}, {"statut": "OK"})


def test_archive_tar_reproductible(tmp_path):
    e1 = archive.archiver_organisme(FIXTURE / "organisme", tmp_path / "a.tar.gz")
    e2 = archive.archiver_organisme(FIXTURE / "organisme", tmp_path / "b.tar.gz")
    assert e1 == e2


# ---------- juge ----------

def test_juge_exactitude_equilibree_et_non_reponse_erreur():
    banque = taches.banque_simulation(rng(3), 8, 8)
    parfait = {t["id"]: {"etiquette": t["verite"]} for t in banque["test"]}
    assert taches.evaluer(parfait, banque["test"])["score"] == 1.0
    aucun = taches.evaluer({}, banque["test"])
    assert aucun["score"] == 0.0 and all(v["non_repondu"] == v["n"] for v in aucun["par_famille"].values())
    masque = taches.masquer(banque["test"][0])
    assert "verite" not in masque and "categorie" not in masque


def test_juge_inverse_est_nul():
    banque = taches.banque_simulation(rng(4), 8, 8)
    inverse = {t["id"]: {"etiquette": [e for e in taches.ETIQUETTES[t["famille"]] if e != t["verite"]][0]} for t in banque["test"]}
    assert taches.evaluer(inverse, banque["test"])["score"] == 0.0


# ---------- boucle complète ----------

def _noyau(tmp_path, generations=2, options=None, especes=("GEMINI_ARGON",), appels_max=40, plafond=10.0):
    ss = np.random.SeedSequence(7)
    r1, r2 = (np.random.default_rng(s) for s in ss.spawn(2))
    banque = taches.banque_simulation(r1, 8, 8)
    doubles, esp = appelants_simules(r2, **(options or {}))
    n = boucle.Noyau(tmp_path / "run", "mission de test", banque, {"appels_max": appels_max, "usd_max": 5.0, "temps_max_s": 60},
                     plafond, generations, appelants=doubles, especes_amorcage=list(especes), entropie=7)
    return n, esp


def test_boucle_complete_simulation(tmp_path):
    n, _ = _noyau(tmp_path, generations=2)
    am = n.amorcer()
    assert am["gemini-argon"]["statut"] == "ORGANISME_VALIDE"
    rapport = n.boucler()
    assert len(rapport["courbes"]["gemini-argon"]) == 2
    assert all(0.0 <= s <= 1.0 for s in rapport["courbes"]["gemini-argon"])
    assert (tmp_path / "run" / "archive" / "gemini-argon" / "g001" / "organisme.tar.gz").exists()
    assert (tmp_path / "run" / "manifeste-run.json").exists() and (tmp_path / "run" / "rapport-v1.json.sha256").exists()
    assert n.lignees["gemini-argon"]["fin"] == "générations maximales"


def test_amorcage_invalide_ne_cree_pas_de_lignee(tmp_path):
    n, esp = _noyau(tmp_path, options={"C": {"pannes": {"amorcage_sans_manifeste": 1.0}}})
    am = n.amorcer()
    assert am["gemini-argon"]["statut"] == "AMORCAGE_INVALIDE" and "gemini-argon" not in n.lignees
    rapport = n.boucler()
    assert rapport["courbes"] == {} and n.evenements[-1]["raison"] == "aucune lignée active"


def test_lignee_sans_successeur_s_arrete(tmp_path):
    org = tmp_path / "fixture"
    shutil.copytree(FIXTURE, org)
    (org / "organisme" / "principal.py").write_text(
        "import json, os\ndef executer(contexte):\n"
        "    json.dump({}, open(os.path.join(contexte['dossier_travail'], 'reponses_test.json'), 'w'))\n", encoding="utf-8")
    n, _ = _noyau(tmp_path, generations=3, options={"commun": {"organisme_amorcage": str(org)}})
    n.amorcer()
    rapport = n.boucler()
    assert rapport["courbes"]["gemini-argon"] == [0.0]
    assert n.lignees["gemini-argon"]["fin"] == "sans successeur valide"


def test_organisme_poli_s_arrete_au_budget(tmp_path):
    n, _ = _noyau(tmp_path, generations=1, appels_max=3)
    n.amorcer()
    n.boucler()
    resume = json.loads((tmp_path / "run" / "archive" / "gemini-argon" / "g000" / "resume.json").read_text())
    assert resume["n_appels"] == 3 and resume["refus_noyau"] == [] and resume["statut"] == "OK"


def test_organisme_gourmand_recoit_plafond_sans_exception(tmp_path):
    org = tmp_path / "fixture"
    shutil.copytree(FIXTURE, org)
    (org / "organisme" / "principal.py").write_text(
        "import json, os\nimport noyau_client as nc\n"
        "def executer(contexte):\n"
        "    statuts = [nc.appeler('GEMINI_ARGON', 'Exploration libre', role='x')['statut'] for _ in range(6)]\n"
        "    json.dump({}, open(os.path.join(contexte['dossier_travail'], 'reponses_test.json'), 'w'))\n"
        "    json.dump(statuts, open(os.path.join(contexte['dossier_travail'], 'statuts.json'), 'w'))\n", encoding="utf-8")
    n, _ = _noyau(tmp_path, generations=1, appels_max=3, options={"commun": {"organisme_amorcage": str(org)}})
    n.amorcer()
    n.boucler()
    resume = json.loads((tmp_path / "run" / "archive" / "gemini-argon" / "g000" / "resume.json").read_text())
    statuts = json.loads((tmp_path / "run" / "archive" / "gemini-argon" / "g000" / "travail" / "statuts.json").read_text())
    assert resume["n_appels"] == 3 and statuts == ["OK", "OK", "OK", "PLAFOND", "PLAFOND", "PLAFOND"]
    assert len([r for r in resume["refus_noyau"] if r["raison"] == "appels_max"]) == 3 and resume["statut"] == "OK"


def test_fichier_stop_arrete_la_boucle(tmp_path):
    n, _ = _noyau(tmp_path, generations=5)
    n.amorcer()
    (tmp_path / "run" / "STOP").write_text("stop")
    rapport = n.boucler()
    assert rapport["courbes"] == {} and n.evenements[-1]["raison"] == "fichier STOP"


def test_mode_reel_refuse_sans_go(tmp_path):
    banque = taches.banque_simulation(rng(1), 4, 4)
    with pytest.raises(appels.Arret):
        boucle.Noyau(tmp_path / "r", "m", banque, {"appels_max": 1, "usd_max": 1, "temps_max_s": 10}, 1.0, 1, appelants=None, reel=True, go_id=None)
