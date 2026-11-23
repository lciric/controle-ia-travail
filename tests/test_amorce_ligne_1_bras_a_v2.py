"""Essais de la machine autonome de la ligne 1 de carte du bras A, version 2 (les essais v1 restent, R12) : construction
de la branche d'entrée v2 (`scripts/construire_branche_entree_ligne_1_bras_a_v2.py`, 58 fichiers : l'amorce complète y
est portée), amorce d'appel (`scripts/amorce_appel_ligne_1_bras_a_v1.sh`, onstart de moins de 2 500 octets), amorce
complète v2 (`scripts/amorce_ligne_1_bras_a_v2.sh`, lancée par l'appel) et lanceur de la session v2
(`scripts/lanceur_machine_ligne_1_bras_a_v2.py`). Le monde jouet passe désormais par l'amorce d'appel. Heure du plafond
(règle v2) : coupe, versement, preuve, grâce en marche, destruction ; sans preuve, arrêt seulement. Processeur seul ; aucune instance, aucune clé réelle,
aucun réseau (un dépôt nu local joue GitHub ; un faux `curl` joue l'interface du loueur et consigne méthode et adresse,
jamais d'en-tête ; un petit serveur local joue la lecture de l'instance).

Le monde jouet : un dépôt source local rempli par la liste blanche v2 (modules calculés par programme, données), un
texte FICTIF au chemin du texte scellé, une configuration d'essai qui nomme un GUIDE FICTIF (déclaré tel ; ses
constantes sont injectées dans le lanceur v8 par un petit programme d'amorce posé sur la branche, comme dans les essais
de la course v2), un plan et un constat d'essai. Rien n'est lu sous `docs/sources/`, sauf l'essai de construction sur
le vrai dépôt, qui y prend quatre fichiers par `git show` redirigé dans un fichier (jamais lus ni empreintés ici).

Artefacts joués : empreinte posée fausse (échec versé, destruction), poussée non prouvée (arrêt, pas de destruction),
redémarrage (aucune relance ; versement repris, puis destruction), échéance dépassée (avant la course ; pendant la
course, arrêt par le PID), et le contrôle que les valeurs factices des secrets n'apparaissent nulle part (journal,
sorties, branche poussée, sorties du lanceur). Rejeu entier sur le modèle jouet : `AMORCE_LIGNE_1_ESSAI_LONG=1`."""
import hashlib
import http.server
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import pytest

from controle_ia.organismes_discrets import instrument_appariement_v4 as iv
from controle_ia.organismes_discrets import lanceur_bras_a_v8 as la
from controle_ia.scellement import sceller

DEPOT = Path(__file__).resolve().parents[1]
AMORCE = DEPOT / "scripts/amorce_ligne_1_bras_a_v2.sh"
APPEL = DEPOT / "scripts/amorce_appel_ligne_1_bras_a_v1.sh"
COURSE = "scripts/course_ligne_1_bras_a_v2.py"
REF = json.loads((DEPOT / la.CHEMIN_CONFIGURATION_DE_REFERENCE).read_text(encoding="utf-8"))
ENTROPIE_FICTIVE = 271828182845904523536028747135266249775
SECRETS = {"GH_TOKEN": "ghp_FAUXjetonDEPOT0123456789abcdef", "HF_TOKEN": "hf_FAUXjetonHUB0123456789abcdef",
           "CONTAINER_API_KEY": "FAUXcleCONTENEUR0123456789abcdef"}
FAUSSE_CLE_LOUEUR = "FAUXcleLOUEUR0123456789abcdef"
LONG = os.environ.get("AMORCE_LIGNE_1_ESSAI_LONG") == "1"


def _charger(relatif, nom):
    spec = importlib.util.spec_from_file_location(nom, DEPOT / relatif)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


cb = _charger("scripts/construire_branche_entree_ligne_1_bras_a_v2.py", "construire_branche_entree_ligne_1_bras_a_v2")
lm = _charger("scripts/lanceur_machine_ligne_1_bras_a_v2.py", "lanceur_machine_ligne_1_bras_a_v2")
lb = cb.charger_la_liste_blanche()


def _sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _instant(d: datetime) -> str:
    return d.strftime("%Y-%m-%dT%H:%M:%SZ")


def _git(*args, cwd=None):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                       env=dict(os.environ, GIT_AUTHOR_NAME="essai", GIT_AUTHOR_EMAIL="essai@invalid",
                                GIT_COMMITTER_NAME="essai", GIT_COMMITTER_EMAIL="essai@invalid"))
    assert r.returncode == 0, r.stderr
    return r.stdout


# --- Monde jouet ---------------------------------------------------------------------------------------------------------

MAINTENANT = datetime.now(timezone.utc).replace(microsecond=0)
ANCIEN = datetime.fromtimestamp(MAINTENANT.timestamp() - ((18.0 - 2.0) / 1.2333 * 3600 - 20), timezone.utc)
REGISTRE = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
            "| GO-2026-11-22-148 | 2026-11-01 | calcul | bras A, ligne 1 de carte | 18 USD | 2099-12-31 | Lazar | essai |\n")
TARIFS = {"carte_usd_h": 1.1833, "stockage_usd_h": 0.05, "telechargement_usd_go": 0.05}
CONF = "prereg/configuration-essai-machine-ligne-1-v1.json"
PLAN = "essai/plan-essai-machine-v1.json"
GUIDE_DOSSIER = "essai/guide-fictif-v1"
TEXTE_GUIDE = "GUIDE FICTIF D'ESSAI — ce texte n'est pas le guide H1-classification ; essais de la machine autonome.\n"
INJECTEUR = ("import json, runpy, sys\n"
             "from controle_ia.organismes_discrets import lanceur_bras_a_v8 as la\n"
             "for k, v in json.load(open(sys.argv[1], encoding='utf-8')).items():\n"
             "    setattr(la, k, v)          # guide FICTIF, injecté par l'essai\n"
             "course = sys.argv[2]\n"
             "sys.argv = [course] + sys.argv[3:]\n"
             "runpy.run_path(course, run_name='__main__')\n")
FAUX_CURL = ("#!/usr/bin/env bash\n"
             "m=GET; u=''\n"
             "while [ $# -gt 0 ]; do case \"$1\" in -X) m=\"$2\"; shift;; http*) u=\"$1\";; esac; shift; done\n"
             "cat > /dev/null\n"
             "printf '%s %s\\n' \"$m\" \"$u\" >> \"$FAUX_CURL_JOURNAL\"\n"
             "printf '200'\n")
MONDE: dict = {}


def _texte_fictif() -> str:
    corps = {"Hypothèse": "h", "Prédiction chiffrée et signe attendu": "p", "Métrique": "m", "Seuil": "s",
             "Plan d'analyse": f"entropie racine : {ENTROPIE_FICTIVE}", "Critères de lecture gelés": "c",
             "Liste d'arrêt": "l", "Contre-lecture": "brouillon " + "a" * 64 + " ; rapport " + "b" * 64}
    return "# Texte fictif des essais de la machine de la ligne 1\n\n" + "".join(f"## {k}\n\n{v}\n\n" for k, v in corps.items())


def _poser(racine: Path, relatif: str) -> None:
    (racine / relatif).parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(DEPOT / relatif, racine / relatif)


@pytest.fixture(scope="module")
def monde(tmp_path_factory):
    base = tmp_path_factory.mktemp("machine")
    src = base / "source"
    src.mkdir()
    modules = lb.modules_importes(DEPOT, [COURSE, la.CHEMIN_DU_LANCEUR])
    assert not [x for x in modules if lb.est_cloisonne_ici(x)]
    for x in modules + list(cb.EXIGENCES) + [cb.AMORCE_COMPLETE]:
        _poser(src, x)
    for x in (la.CHEMIN_CONFIGURATION_DE_REFERENCE, REF["taches_distillation"]["chemin"], REF["taches_evaluation"]["chemin"]):
        _poser(src, x)
        _poser(src, x + ".sha256")
    t = src / la.CHEMIN_TEXTE_SCELLE
    t.write_text(_texte_fictif(), encoding="utf-8")
    sceller(t)
    g = src / GUIDE_DOSSIER
    (g / "invites").mkdir(parents=True)
    (g / "invites/H1-classification.txt").write_text(TEXTE_GUIDE, encoding="utf-8")
    sceller(g / "invites/H1-classification.txt")
    (g / "index.json").write_text(json.dumps({"objet": "index fictif d'essai", "invites": [
        {"id": "H1-classification", "fichier": "invites/H1-classification.txt",
         "sha256": _sha(g / "invites/H1-classification.txt")}]}), encoding="utf-8")
    sceller(g / "index.json")
    guide = {"identifiant": "H1-classification", "fichier": f"{GUIDE_DOSSIER}/invites/H1-classification.txt",
             "sha256": _sha(g / "invites/H1-classification.txt"), "index": f"{GUIDE_DOSSIER}/index.json",
             "index_sha256": _sha(g / "index.json")}
    constantes = {"CHEMIN_DU_GUIDE": guide["fichier"], "EMPREINTE_DU_GUIDE": guide["sha256"],
                  "CHEMIN_DE_L_INDEX_DU_GUIDE": guide["index"], "EMPREINTE_DE_L_INDEX_DU_GUIDE": guide["index_sha256"]}
    (src / "essai/constantes.json").write_text(json.dumps(constantes), encoding="utf-8")
    (src / "essai/injecteur.py").write_text(INJECTEUR, encoding="utf-8")
    c = {"lanceur": {"chemin": la.CHEMIN_DU_LANCEUR, "sha256": _sha(DEPOT / la.CHEMIN_DU_LANCEUR)},
         "texte": {"chemin": la.CHEMIN_TEXTE_SCELLE, "sha256": _sha(t)},
         "configuration_de_reference": {"chemin": la.CHEMIN_CONFIGURATION_DE_REFERENCE,
                                        "sha256": la.EMPREINTE_CONFIGURATION_DE_REFERENCE},
         "entropie": ENTROPIE_FICTIVE, "entropie_fictive": False, "reglages_instrument": dict(iv.OPTIONS_RETENUES),
         "ligne_1": {"plafond_usd": 18.0, "marge_de_credit_usd": 2.0}, "guide": guide}
    (src / CONF).write_text(json.dumps(c), encoding="utf-8")
    sceller(src / CONF)
    with pytest.MonkeyPatch.context() as mp:
        for k, v in constantes.items():
            mp.setattr(la, k, v)
        config = la.lire_la_configuration(src / CONF, src)
        plan = la.plan_des_taches(config)
        for nom, quand in (("essai/constat.json", MAINTENANT), ("essai/constat-ancien.json", ANCIEN)):
            constat = la.constat_de_depart_ligne_1(config, go_id="GO-2026-11-22-148", texte_du_registre_go=REGISTRE,
                                                   maintenant=quand, credit_lu_usd=20.0,
                                                   tarifs=dict(TARIFS, date_utc=_instant(quand)))
            (src / nom).write_text(json.dumps(constat), encoding="utf-8")
    (src / PLAN).write_text(json.dumps({"configuration_du_lanceur": {"sha256": config["sha256"]},
                                        "fabrication": [x["identifiant"] for x in plan["fabrication"]],
                                        "verification": [x["identifiant"] for x in plan["verification"]],
                                        "ouvertes": plan["ouvertes"], "gardees": plan["gardees"]}), encoding="utf-8")
    sceller(src / PLAN)
    _git("init", "-q", "-b", "main", cwd=src)
    _git("add", "-A", cwd=src)
    _git("commit", "-q", "-m", "monde jouet", cwd=src)
    commit = _git("rev-parse", "HEAD", cwd=src).strip()
    guide_fichiers = [f"{GUIDE_DOSSIER}/invites/H1-classification.txt", f"{GUIDE_DOSSIER}/invites/H1-classification.txt.sha256",
                      f"{GUIDE_DOSSIER}/index.json", f"{GUIDE_DOSSIER}/index.json.sha256"]
    fichiers = sorted(set(_git("ls-files", cwd=src).split("\n")[:-1]) - set(guide_fichiers)
                      - {"essai/constat.json", "essai/constat-ancien.json"})
    nu = base / "distant.git"
    _git("init", "-q", "--bare", str(nu))
    faux = base / "faux-curl"
    faux.write_text(FAUX_CURL, encoding="utf-8")
    faux.chmod(0o755)
    MONDE.update(base=base, src=src, commit=commit, fichiers=fichiers, nu=nu, faux=faux,
                 guide=[(p, _sha(src / p)) for p in guide_fichiers])
    return MONDE


def entree(nom: str, constat: str = "essai/constat.json", guide=None, distant=None) -> str:
    """Construit puis pousse une branche d'entrée jouet ; rend son commit."""
    dossier = MONDE["base"] / ("entree-" + nom.replace("/", "-"))
    compte = cb.construire(MONDE["src"], MONDE["commit"], MONDE["fichiers"], {cb.NOM_DU_CONSTAT: constat},
                           guide or MONDE["guide"], "main", nom, dossier, lb.est_cloisonne_ici)
    cb.pousser(dossier, nom, str(distant or MONDE["nu"]))
    return compte["commit_entree"]


def jouer(scenario: str, branche_entree: str, commit_entree: str, distant=None, racine=None, delai=900, **env_de_plus):
    racine = racine or MONDE["base"] / f"racine-{scenario}"
    journal_curl = MONDE["base"] / f"curl-{scenario}.txt"
    env = {"PATH": os.environ["PATH"], "HOME": str(MONDE["base"]), "LANG": "C.UTF-8",
           "AMORCE_JOUET": "1", "RACINE_AMORCE": str(racine), "AMORCE_DEPOT_URL": str(distant or MONDE["nu"]),
           "AMORCE_CURL": str(MONDE["faux"]), "AMORCE_PYTHON": sys.executable, "AMORCE_PAS_S": "1",
           "FAUX_CURL_JOURNAL": str(journal_curl), "GO_ID": "GO-2026-11-22-148",
           "BRANCHE_ENTREE": branche_entree, "BRANCHE_SORTIE": f"calcul/jouet-{scenario}", "COMMIT_ENTREE": commit_entree,
           "AVANT_CREATION_UTC": _instant(MAINTENANT), "CONTAINER_ID": "4242",
           "JOUET_CONFIGURATION": CONF, "JOUET_PLAN": PLAN, "JOUET_INJECTEUR": "essai/injecteur.py",
           "JOUET_CONSTANTES": "essai/constantes.json", "GIT_CONFIG_NOSYSTEM": "1", "AMORCE_SHA256": _sha(AMORCE),
           "AMORCE_GRACE_S": "3", **SECRETS}
    env.update({k: v for k, v in env_de_plus.items() if v is not None})
    for k, v in env_de_plus.items():
        if v is None:
            env.pop(k, None)
    r = subprocess.run(["bash", str(APPEL)], env=env, capture_output=True, text=True, timeout=delai)
    journal = "".join((racine / "ligne-1-bras-a" / n).read_text(encoding="utf-8")
                      for n in ("journal-appel.txt", "journal-amorce.txt") if (racine / "ligne-1-bras-a" / n).exists())
    appels = journal_curl.read_text(encoding="utf-8").splitlines() if journal_curl.exists() else []
    return r, journal, appels, racine


def exiger_aucun_secret(*lieux, textes=()):
    valeurs = [v.encode() for v in list(SECRETS.values()) + [FAUSSE_CLE_LOUEUR]]
    for t in textes:
        assert not any(v.decode() in t for v in valeurs)
    for lieu in lieux:
        lieu = Path(lieu)
        for p in ([lieu] if lieu.is_file() else lieu.rglob("*")):
            if p.is_file() and not p.is_symlink():
                b = p.read_bytes()
                assert not any(v in b for v in valeurs), f"valeur secrète dans {p}"


def branche_poussee(nom: str, distant=None) -> str | None:
    r = subprocess.run(["git", "ls-remote", str(distant or MONDE["nu"]), f"refs/heads/{nom}"], capture_output=True, text=True)
    return r.stdout.split()[0] if r.stdout.strip() else None


def verification(nom: str, distant=None, *args) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(DEPOT / "scripts/lanceur_machine_ligne_1_bras_a_v2.py"), "--racine", str(DEPOT),
                           "verification", "--branche-sortie", nom, "--distant", str(distant or MONDE["nu"]), *args],
                          capture_output=True, text=True, env=dict(os.environ, **SECRETS))


# --- Construction de la branche d'entrée ---------------------------------------------------------------------------------

def test_construction_jouet_ne_porte_que_la_liste(monde, tmp_path):
    compte = cb.construire(monde["src"], monde["commit"], monde["fichiers"], {cb.NOM_DU_CONSTAT: "essai/constat.json"},
                           monde["guide"], "main", "entree/essai-liste", tmp_path / "d", lb.est_cloisonne_ici)
    attendus = sorted(monde["fichiers"] + [p for p, _ in monde["guide"]] + [cb.NOM_DU_CONSTAT, cb.NOM_DES_EMPREINTES])
    assert compte["fichiers"] == attendus and compte["nombre_de_fichiers"] == len(attendus)
    assert "essai/constat.json" not in compte["fichiers"]
    assert f"Commit-source: {monde['commit']}" in _git("log", "-1", "--format=%B", cwd=tmp_path / "d")
    lignes = (tmp_path / "d" / cb.NOM_DES_EMPREINTES).read_text(encoding="utf-8").splitlines()
    assert len(lignes) == len(attendus) - 1
    assert subprocess.run(["sha256sum", "--strict", "--quiet", "-c", cb.NOM_DES_EMPREINTES], cwd=tmp_path / "d").returncode == 0


@pytest.mark.parametrize("ecart, motif", [
    ({"fichiers": ["bases/rien.py"]}, "cloisonnés"),
    ({"fichiers": ["sondes/rien.json"]}, "cloisonnés"),
    ({"fichiers": ["scripts/mots_et_cout_rien.py"]}, "cloisonnés"),
    ({"renommes": {"constat-ligne-1.json": "registres/etat.md"}}, "cloisonnés"),
    ({"guide": [("essai/x", "Z" * 64)]}, "illisible"),
    ({"branche": "Entree/../x"}, "illisible"),
    ({"commit": "abc"}, "commit"),
    ({"fichiers": ["../hors.py"]}, "relatif"),
])
def test_construction_refus(monde, tmp_path, ecart, motif):
    a = {"source": monde["src"], "commit": monde["commit"], "fichiers": [], "renommes": {}, "guide": [],
         "reference_guide": "main", "branche": "entree/refus", "dossier": tmp_path / "d", "est_cloisonne": lb.est_cloisonne_ici}
    a.update(ecart)
    with pytest.raises(cb.Refus, match=motif):
        cb.construire(**a)
    assert not (tmp_path / "d").exists()            # refus avant toute extraction


def test_poussee_de_l_entree_refusee_a_un_autre_commit(monde, tmp_path):
    nu = tmp_path / "nu.git"
    _git("init", "-q", "--bare", str(nu))
    entree("entree/essai-r12", distant=nu)
    d = tmp_path / "autre"
    cb.construire(monde["src"], monde["commit"], monde["fichiers"][:3], {}, [], "main", "entree/essai-r12", d,
                  lb.est_cloisonne_ici)
    with pytest.raises(cb.Refus, match="R12"):
        cb.pousser(d, "entree/essai-r12", str(nu))


def test_construction_sur_le_vrai_depot(tmp_path):
    """La vraie branche (sans poussée) : 58 fichiers ; les quatre du guide aux empreintes DONNÉES (jamais recalculées :
    rien n'est lu ni empreinté sous `docs/sources/` par cet essai) ; aucun autre chemin cloisonné."""
    for c, _ in cb.GUIDE_DONNE:
        if subprocess.run(["git", "-C", str(DEPOT), "cat-file", "-e", f"origin/main:{c}"]).returncode != 0:
            pytest.skip("origin/main ne porte pas le guide dans ce clone")
    r = subprocess.run([sys.executable, str(DEPOT / "scripts/construire_branche_entree_ligne_1_bras_a_v2.py"),
                        "--racine", str(DEPOT), "--dossier", str(tmp_path / "d")], capture_output=True, text=True,
                       env=dict(os.environ, PYTHONPATH=str(DEPOT / "src")))
    if r.returncode == 2 and "arbre de travail" in r.stderr:
        pytest.skip("arbre de travail modifié sur un fichier posé")
    assert r.returncode == 0, r.stderr
    compte = json.loads(r.stdout)
    assert compte["nombre_de_fichiers"] == 58 and compte["liste_blanche"] == 52 and compte["poussee"] is False
    guide = {c for c, _ in cb.GUIDE_DONNE}
    assert [c for c in compte["fichiers"] if lb.est_cloisonne_ici(c)] == sorted(guide)
    assert {"requirements-gpu.txt", "requirements-cpu.txt", "requirements-donnees.txt", "constat-ligne-1.json",
            "empreintes-posees.txt", COURSE, la.CHEMIN_DU_LANCEUR} <= set(compte["fichiers"])
    lignes = dict(reversed(l.split("  ", 1)) for l in
                  (tmp_path / "d/empreintes-posees.txt").read_text(encoding="utf-8").splitlines())
    assert {c: lignes[c] for c in guide} == dict(cb.GUIDE_DONNE)
    constat = DEPOT / cb.CONSTAT
    assert lignes["constat-ligne-1.json"] == _sha(constat)
    assert lignes[cb.AMORCE_COMPLETE] == _sha(AMORCE) == compte["amorce_complete_sha256"]


# --- Amorce : refus hors du mode jouet -----------------------------------------------------------------------------------

@pytest.mark.parametrize("coquille", ["bash", "sh"])
def test_variables_de_jouet_refusees_hors_jouet(tmp_path, coquille):
    """Hors jouet, une variable de jouet arrête tout avant le moindre dossier ; jouée par `sh`, l'amorce se reprend
    par bash."""
    r = subprocess.run([coquille, str(AMORCE)], env={"PATH": os.environ["PATH"], "RACINE_AMORCE": str(tmp_path / "r")},
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 2 and "mode jouet" in r.stdout and not (tmp_path / "r").exists()


# --- Amorce : mode court (refus de la course, versement, preuve, destruction) --------------------------------------------

def test_mode_court_refus_de_la_course_verse_et_detruit(monde):
    commit = entree("entree/jouet-court")
    r, journal, appels, racine = jouer("court", "entree/jouet-court", commit, JOUET_INJECTEUR=None, JOUET_CONSTANTES=None)
    assert r.returncode == 0, journal + r.stderr
    assert "empreintes posées conformes" in journal and "course lancée" in journal
    assert "FIN DE LA COURSE : code 2" in journal and "versement scellé par le lanceur v8" in journal
    assert "POUSSÉE PROUVÉE" in journal and "JOUET : destruction simulée" in journal
    assert appels == ["DELETE https://console.vast.ai/api/v0/instances/4242/"]
    v = verification("calcul/jouet-court")
    assert v.returncode == 0, v.stderr
    sortie = json.loads(v.stdout)
    assert sortie["etat"] == "arret" and sortie["code_course"] == "2" and sortie["commit"] == branche_poussee("calcul/jouet-court")
    d = Path(sortie["copie_locale"]) / sortie["dossier"]
    assert "REFUS AVANT JEU" in (d / "journal-course-ligne-1.txt").read_text(encoding="utf-8")
    manifeste = json.loads((d / "manifeste-du-versement.json").read_text(encoding="utf-8"))
    assert manifeste["manquants"][0]["nom"] == "manifeste-de-la-ligne-1.json"
    assert {"amorce.json", "constat-ligne-1.json", "empreintes-posees.txt", "journal-amorce.txt", "course.out"} <= \
        {x["nom"] for x in manifeste["inventaire"]}
    exiger_aucun_secret(racine, Path(sortie["copie_locale"]), textes=[r.stdout, r.stderr, v.stdout, v.stderr])


def test_arret_au_plafond_verse_le_manifeste_de_la_ligne(monde):
    commit = entree("entree/jouet-plafond", constat="essai/constat-ancien.json")
    r, journal, appels, racine = jouer("plafond", "entree/jouet-plafond", commit, AVANT_CREATION_UTC=_instant(ANCIEN),
                                       AMORCE_ECHEANCE_S="200000", AMORCE_PLAFOND_S="300000")
    assert r.returncode == 0, journal + r.stderr
    assert "FIN DE LA COURSE : code 3" in journal or "FIN DE LA COURSE : code 2" in journal, journal
    assert "POUSSÉE PROUVÉE" in journal and appels[-1].startswith("DELETE ")
    v = verification("calcul/jouet-plafond")
    assert v.returncode == 0, v.stderr
    sortie = json.loads(v.stdout)
    assert sortie["creation_retenue_utc"] == _instant(ANCIEN)
    d = Path(sortie["copie_locale"]) / sortie["dossier"]
    assert "ArretDePlafond" in (d / "journal-course-ligne-1.txt").read_text(encoding="utf-8")
    if sortie["code_course"] == "3":
        assert "versement scellé par le lanceur v8" in journal
        m = json.loads((d / "manifeste-du-versement.json").read_text(encoding="utf-8"))
        assert m["manifeste_de_la_ligne"]["arret"].startswith("ArretDePlafond") and m["manquants"] == []
    exiger_aucun_secret(racine, Path(sortie["copie_locale"]), textes=[r.stdout, r.stderr])


# --- Artefacts -----------------------------------------------------------------------------------------------------------

def test_empreinte_posee_fausse_echec_verse_et_destruction(monde):
    guide = [(p, ("0" * 64 if p.endswith("index.json") else s)) for p, s in monde["guide"]]
    commit = entree("entree/jouet-faux", guide=guide)
    r, journal, appels, racine = jouer("faux", "entree/jouet-faux", commit)
    assert r.returncode == 0, journal + r.stderr
    assert "EMPREINTES POSÉES NON CONFORMES" in journal and "course lancée" not in journal
    assert "bibliothèque standard" in journal and "POUSSÉE PROUVÉE" in journal
    assert appels == ["DELETE https://console.vast.ai/api/v0/instances/4242/"]
    v = verification("calcul/jouet-faux")
    assert v.returncode == 0, v.stderr
    assert json.loads(v.stdout)["etat"] == "echec"
    exiger_aucun_secret(racine, textes=[r.stdout, r.stderr])


def test_commit_d_entree_different_arret_par_l_appel(monde):
    """Erreur avant l'exec de l'amorce complète : arrêt simple, jamais de destruction (rien n'est produit)."""
    commit = entree("entree/jouet-commit")
    r, journal, appels, racine = jouer("commit", "entree/jouet-commit", "f" * 40)
    assert r.returncode == 3 and "APPEL ARRET : commit cloné différent" in journal, journal + r.stdout
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"]
    assert not (racine / "ligne-1-bras-a/journal-amorce.txt").exists()
    exiger_aucun_secret(racine, textes=[r.stdout, r.stderr])


# --- Amorce d'appel ----------------------------------------------------------------------------------------------------

def test_amorce_d_appel_courte():
    assert APPEL.stat().st_size < 2500


def test_appel_empreinte_de_l_amorce_complete_fausse_arret(monde):
    commit = entree("entree/jouet-appel-sha")
    r, journal, appels, racine = jouer("appel-sha", "entree/jouet-appel-sha", commit, AMORCE_SHA256="0" * 64)
    assert r.returncode == 3 and "empreinte de l'amorce complète" in journal
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"]
    assert not (racine / "ligne-1-bras-a/journal-amorce.txt").exists()
    # l'aide d'identification est inscrite dans la configuration du clone (R-5101), par le nom du jeton seulement
    aide = subprocess.run(["git", "-C", str(racine / "ligne-1-bras-a/entree"), "config", "credential.helper"],
                          capture_output=True, text=True).stdout
    assert "x-access-token" in aide and "${GH_TOKEN}" in aide
    exiger_aucun_secret(racine, textes=[r.stdout, r.stderr])


@pytest.mark.parametrize("absente", ["GH_TOKEN", "COMMIT_ENTREE", "AMORCE_SHA256", "CONTAINER_API_KEY"])
def test_appel_variable_absente_arret_sans_clone(monde, absente):
    r, journal, appels, racine = jouer(f"appel-{absente.lower()}", "entree/jouet-court", "a" * 40, **{absente: None})
    assert r.returncode == 3 and f"{absente} absente" in journal
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"]
    assert not (racine / "ligne-1-bras-a/entree").exists()


def test_appel_hors_jouet_refuse_les_variables_de_jouet(tmp_path):
    r = subprocess.run(["bash", str(APPEL)], env={"PATH": os.environ["PATH"], "RACINE_AMORCE": str(tmp_path / "r")},
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 2 and "variable de jouet hors jouet" in r.stdout and not (tmp_path / "r").exists()


def test_poussee_non_prouvee_arret_puis_reprise_sans_relance(monde, tmp_path):
    nu = tmp_path / "rejet.git"
    _git("clone", "-q", "--bare", str(monde["nu"]), str(nu))
    crochet = nu / "hooks/pre-receive"
    crochet.write_text("#!/bin/sh\nwhile read a b ref; do case \"$ref\" in refs/heads/calcul/*) echo refus; exit 1;; esac; done\n")
    crochet.chmod(0o755)
    commit = entree("entree/jouet-rejet", distant=nu)
    racine = tmp_path / "racine"
    r, journal, appels, _ = jouer("rejet", "entree/jouet-rejet", commit, distant=nu, racine=racine,
                                  JOUET_INJECTEUR=None, JOUET_CONSTANTES=None)
    assert r.returncode == 3, journal + r.stderr
    assert "poussée non prouvée" in journal and "ARRÊT (state=stopped)" in journal
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"]       # arrêt, jamais destruction
    assert branche_poussee("calcul/jouet-rejet", nu) is None
    assert any((racine / "ligne-1-bras-a").glob("sortie-git-*/diag/organismes-discrets-v-a-v2/ligne-1-arret-*"))
    # redémarrage du conteneur : l'amorce reprend, ne relance rien, repousse le même versement, puis détruit
    crochet.unlink()
    (MONDE["base"] / "curl-rejet.txt").unlink(missing_ok=True)
    r2, journal2, appels2, _ = jouer("rejet", "entree/jouet-rejet", commit, distant=nu, racine=racine,
                                     JOUET_INJECTEUR=None, JOUET_CONSTANTES=None)
    assert r2.returncode == 0, journal2 + r2.stderr
    assert "REPRISE après redémarrage" in journal2 and journal2.count("course lancée") == 1
    assert journal2.count("versement committé") == 1 and "POUSSÉE PROUVÉE" in journal2
    assert appels2[-1] == "DELETE https://console.vast.ai/api/v0/instances/4242/"
    assert verification("calcul/jouet-rejet", nu).returncode == 0
    # troisième départ après la destruction prouvée : rien que la destruction
    r3, journal3, _, _ = jouer("rejet", "entree/jouet-rejet", commit, distant=nu, racine=racine)
    assert r3.returncode == 0 and journal3.count("course lancée") == 1 and journal3.count("versement committé") == 1
    exiger_aucun_secret(racine, textes=[r.stdout, r2.stdout, r3.stdout])


def test_echeance_deja_passee_aucune_course(monde):
    commit = entree("entree/jouet-echeance")
    r, journal, appels, racine = jouer("echeance", "entree/jouet-echeance", commit, AMORCE_ECHEANCE_S="0")
    assert r.returncode == 0, journal + r.stderr
    assert "échéance passée : étape non lancée" in journal and "FIN DE LA COURSE : code 124" in journal
    assert appels[-1].startswith("DELETE ")
    assert json.loads(verification("calcul/jouet-echeance").stdout)["etat"] == "arret"


def test_echeance_pendant_la_course_arret_par_le_pid(monde):
    commit = entree("entree/jouet-minuterie")
    ecart = int(time.time() - MAINTENANT.timestamp()) + 25          # création retenue = horloge du constat
    r, journal, appels, racine = jouer("minuterie", "entree/jouet-minuterie", commit, AMORCE_ECHEANCE_S=str(ecart))
    assert r.returncode == 0, journal + r.stderr
    assert "MINUTERIE : échéance atteinte" in journal and "POUSSÉE PROUVÉE" in journal
    assert "course lancée" in journal and "TERM envoyé" in journal and "arrêtée par la minuterie" in journal, journal
    assert json.loads(verification("calcul/jouet-minuterie").stdout)["etat"] == "arret"
    assert appels[-1].startswith("DELETE ")
    exiger_aucun_secret(racine, textes=[r.stdout, r.stderr])


def test_heure_du_plafond_poussee_prouvee_grace_puis_destruction(monde):
    """Règle v2 : la minuterie coupe la course ; le fil principal verse, prouve, passe la grâce en marche, relit la
    preuve, puis détruit ; aucune destruction avant."""
    commit = entree("entree/jouet-heure-plafond")
    ecart = int(time.time() - MAINTENANT.timestamp()) + 25
    r, journal, appels, racine = jouer("heure-plafond", "entree/jouet-heure-plafond", commit, AMORCE_PLAFOND_S=str(ecart))
    assert r.returncode == 0, journal + r.stderr
    assert "MINUTERIE : heure du plafond atteinte" in journal and "TERM envoyé" in journal
    assert "coupée par la minuterie à l'heure du plafond" in journal
    suite = journal.split("POUSSÉE PROUVÉE")[1]
    assert "grâce de 3 s en marche" in suite and "preuve relue après la grâce" in suite
    assert appels == ["DELETE https://console.vast.ai/api/v0/instances/4242/"]
    exiger_aucun_secret(racine, textes=[r.stdout, r.stderr])


def test_heure_du_plafond_sans_poussee_prouvee_arret_seulement(monde, tmp_path):
    nu = tmp_path / "rejet.git"
    _git("clone", "-q", "--bare", str(monde["nu"]), str(nu))
    crochet = nu / "hooks/pre-receive"
    crochet.write_text("#!/bin/sh\nwhile read a b ref; do case \"$ref\" in refs/heads/calcul/*) exit 1;; esac; done\n")
    crochet.chmod(0o755)
    commit = entree("entree/jouet-plafond-rejet", distant=nu)
    r, journal, appels, _ = jouer("plafond-rejet", "entree/jouet-plafond-rejet", commit, distant=nu, AMORCE_PLAFOND_S="0",
                                  JOUET_INJECTEUR=None, JOUET_CONSTANTES=None)
    assert r.returncode == 3, journal + r.stderr
    assert "heure du plafond atteinte" in journal and "nœud pour la mère" in journal
    assert appels == ["PUT https://console.vast.ai/api/v0/instances/4242/"]       # jamais de destruction


def test_creation_relevee_avant_le_constat_echec(monde):
    commit = entree("entree/jouet-avant")
    r, journal, appels, _ = jouer("avant", "entree/jouet-avant", commit, AVANT_CREATION_UTC=_instant(ANCIEN),
                                  AMORCE_PLAFOND_S="200000", AMORCE_ECHEANCE_S="100000")
    assert r.returncode == 0 and "AVANT_CREATION_UTC antérieure au constat" in journal, journal
    assert "course lancée" not in journal and "MINUTERIE" not in journal
    assert appels[-1].startswith("DELETE ")


@pytest.mark.skipif(not LONG, reason="rejeu entier sur le jouet : AMORCE_LIGNE_1_ESSAI_LONG=1 pour le jouer")
def test_rejeu_entier_sur_le_modele_jouet(monde):
    commit = entree("entree/jouet-long")
    r, journal, appels, racine = jouer("long", "entree/jouet-long", commit, delai=8000)
    assert r.returncode == 0, journal + r.stderr
    sortie = json.loads(verification("calcul/jouet-long").stdout)
    print(f"\nREJEU JOUET DE LA MACHINE : code de la course {sortie['code_course']}, état {sortie['etat']}")
    assert sortie["code_course"] in ("0", "3") and appels[-1].startswith("DELETE ")
    exiger_aucun_secret(racine, Path(sortie["copie_locale"]), textes=[r.stdout, r.stderr])


# --- Lanceur de la session -----------------------------------------------------------------------------------------------

def _lanceur(*args, env_de_plus=None):
    env = dict(os.environ, **SECRETS, VAST_API_KEY=FAUSSE_CLE_LOUEUR, NO_PROXY="127.0.0.1,localhost",
               no_proxy="127.0.0.1,localhost", **(env_de_plus or {}))
    for k in ("HTTP_PROXY", "http_proxy", "HTTPS_PROXY", "https_proxy", "ALL_PROXY", "all_proxy"):
        env.pop(k, None)
    return subprocess.run([sys.executable, str(DEPOT / "scripts/lanceur_machine_ligne_1_bras_a_v2.py"),
                           "--racine", str(DEPOT), *args], capture_output=True, text=True, env=env, timeout=120)


def test_creation_imprime_la_commande_sans_valeur_secrete():
    from vastai.utils import parse_env
    r = _lanceur("creation", "--offre", "123456", "--commit-entree", "a" * 40, "--sans-verifier-entree")
    assert r.returncode == 0, r.stderr
    ligne = r.stdout.strip()
    assert ligne.startswith("GO_ID=GO-2026-11-22-148 vastai create instance 123456 --image "
                            "pytorch/pytorch:2.14.1-cuda13.0-cudnn9-runtime --disk 150 ")
    assert ligne.endswith("--onstart scripts/amorce_appel_ligne_1_bras_a_v1.sh")
    brut = ligne.split('--env "')[1].split('"')[0]
    assert "-e GH_TOKEN=$GH_TOKEN -e HF_TOKEN=$HF_TOKEN " in brut and "-e AVANT_CREATION_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)" in brut
    # ce que voit `vastai` après le développement par le shell de la session (valeurs factices ici, jamais affichées)
    developpe = subprocess.run(["bash", "-c", f'printf "%s" "{brut}"'], capture_output=True, text=True,
                               env=dict(os.environ, **SECRETS)).stdout
    env = parse_env(developpe)
    assert env["GH_TOKEN"] == SECRETS["GH_TOKEN"] and env["HF_TOKEN"] == SECRETS["HF_TOKEN"] and env["COMMIT_ENTREE"] == "a" * 40
    assert env["BRANCHE_ENTREE"] == "entree/bras-a-ligne-1-v1" and env["BRANCHE_SORTIE"] == "calcul/bras-a-ligne-1-v1"
    assert env["AMORCE_SHA256"] == _sha(AMORCE) and env["GO_ID"] == "GO-2026-11-22-148"
    assert datetime.strptime(env["AVANT_CREATION_UTC"], "%Y-%m-%dT%H:%M:%SZ")
    exiger_aucun_secret(textes=[r.stdout, r.stderr])
    assert _lanceur("creation", "--offre", "0", "--commit-entree", "a" * 40, "--sans-verifier-entree").returncode == 2


def test_creation_verifie_l_entree_sur_le_distant(monde):
    commit = entree("entree/jouet-creation")
    ok = _lanceur("creation", "--offre", "7", "--commit-entree", commit, "--distant", str(monde["nu"]),
                  "--branche-entree", "entree/jouet-creation", "--branche-sortie", "calcul/jouet-creation-neuve")
    assert ok.returncode == 0, ok.stderr
    mauvais = _lanceur("creation", "--offre", "7", "--commit-entree", "b" * 40, "--distant", str(monde["nu"]),
                       "--branche-entree", "entree/jouet-creation", "--branche-sortie", "calcul/jouet-creation-neuve")
    assert mauvais.returncode == 2 and "attendu" in mauvais.stderr


class _Loueur(http.server.BaseHTTPRequestHandler):
    vus: list = []

    def do_GET(self):
        _Loueur.vus.append((self.path, self.headers.get("Authorization")))
        corps = {"instances": {"id": 4242, "actual_status": "running", "dph_total": 1.2, "start_date": 1795400000.7,
                               "label": "bras-a-ligne-1-v1", "status_msg": "jeton " + SECRETS["GH_TOKEN"],
                               "extra_env": [["GH_TOKEN", SECRETS["GH_TOKEN"]], ["GO_ID", "GO-2026-11-22-148"]],
                               "api_key": "x", "jupyter_token": "y"}}
        b = json.dumps(corps).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def log_message(self, *a):
        pass


def test_etat_masque_les_secrets_et_compare_le_prix(tmp_path):
    serveur = http.server.HTTPServer(("127.0.0.1", 0), _Loueur)
    threading.Thread(target=serveur.serve_forever, daemon=True).start()
    try:
        constat = tmp_path / "constat.json"
        constat.write_text(json.dumps({"tarifs": {"carte_usd_h": 1.12, "stockage_usd_h": 0.0722}}), encoding="utf-8")
        r = _lanceur("etat", "--instance", "4242", "--constat", str(constat),
                     "--api", f"http://127.0.0.1:{serveur.server_port}/api/v0")
    finally:
        serveur.shutdown()
    assert r.returncode == 0, r.stderr
    sortie = json.loads(r.stdout)
    assert sortie["start_date_utc"] == "2026-11-23T02:13:20Z" and sortie["status_msg"] == "jeton [masqué]"
    assert sortie["prix_reel_sous_le_constat"] is False and "destruction" in sortie["consigne"]
    assert _Loueur.vus == [("/api/v0/instances/4242/?owner=me", f"Bearer {FAUSSE_CLE_LOUEUR}")]
    exiger_aucun_secret(textes=[r.stdout, r.stderr])
    assert _lanceur("etat", "--instance", "42; x").returncode == 2


def test_masquer():
    v = list(SECRETS.values())
    sortie = lm.masquer({"a": [["HF_TOKEN", "z"], ["GO_ID", "g"]], "Api_Key": "k", "b": f"x{v[0]}y", "n": 3}, v)
    assert sortie == {"a": [["HF_TOKEN", "[masqué]"], ["GO_ID", "g"]], "Api_Key": "[masqué]", "b": "x[masqué]y", "n": 3}


def test_verification_refuse_une_branche_absente(monde):
    r = verification("calcul/jouet-absente")
    assert r.returncode == 2 and "absente" in r.stderr
