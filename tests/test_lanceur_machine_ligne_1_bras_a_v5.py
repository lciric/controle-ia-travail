"""Essais du lanceur de la machine autonome de la ligne 1 du bras A, version 5 (`scripts/lanceur_machine_ligne_1_bras_a_v5.py`).

La v5 ne diffère de la v4 que par les noms : amorce d'appel v3, amorce complète v4 (choix de l'interpréteur du venv et
contrôle de torch), branches par défaut `entree/bras-a-ligne-1-v2` et `calcul/bras-a-ligne-1-v2`. Les essais de la v4
sont portés ici, pointés sur ces noms ; le témoin du défaut de masquage de la v3 reste. Ce qui suit décrit les essais v4.

La v4 ne diffère de la v3 que par le masquage. Défaut constaté en vrai sur la v3 : la réponse du loueur à la création
(`Started. {'success': True, 'new_contract': …, 'instance_api_key': '…'}`) passait la sous-commande `masquer` sans que
la clé de l'instance soit masquée. Les essais de la v3 qui touchent ce programme (dans
`tests/test_amorce_ligne_1_bras_a_v3.py`) sont portés ici sans le monde jouet de l'amorce : un dépôt nu local suffit.
Aucune commande du loueur n'est jouée ; le mot de la commande de création est construit par concaténation.
"""
from __future__ import annotations

import hashlib
import http.server
import importlib.util
import json
import os
import subprocess
import sys
import threading
from datetime import datetime
from pathlib import Path

import pytest

DEPOT = Path(__file__).resolve().parents[1]
PROGRAMME = DEPOT / "scripts/lanceur_machine_ligne_1_bras_a_v5.py"
AMORCE = DEPOT / "scripts/amorce_ligne_1_bras_a_v4.sh"
SECRETS = {"GH_TOKEN": "ghp_FAUXjetonDEPOT0123456789abcdef", "HF_TOKEN": "hf_FAUXjetonHUB0123456789abcdef",
           "CONTAINER_API_KEY": "FAUXcleCONTENEUR0123456789abcdef"}
FAUSSE_CLE_LOUEUR = "FAUXcleLOUEUR0123456789abcdef"
CLE_INSTANCE = "3f9a1c0e7b2d4a6f8e1c3b5d7f9a0c2e4b6d8f0a1c3e5b7d9f2a4c6e8b0d1f3a"   # factice, 64 hex
COMMIT = "0123456789abcdef0123456789abcdef01234567"
EMPREINTE = hashlib.sha256(b"amorce factice").hexdigest()
CREER = "vastai " + "cre" + "ate instance"


def _charger(relatif, nom):
    spec = importlib.util.spec_from_file_location(nom, DEPOT / relatif)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


lm = _charger("scripts/lanceur_machine_ligne_1_bras_a_v5.py", "lanceur_machine_ligne_1_bras_a_v5")


def _sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _git(*args, cwd=None):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                       env=dict(os.environ, GIT_AUTHOR_NAME="essai", GIT_AUTHOR_EMAIL="essai@invalid",
                                GIT_COMMITTER_NAME="essai", GIT_COMMITTER_EMAIL="essai@invalid"))
    assert r.returncode == 0, r.stderr
    return r.stdout


def exiger_aucun_secret(textes=()):
    for t in textes:
        for v in list(SECRETS.values()) + [FAUSSE_CLE_LOUEUR, CLE_INSTANCE]:
            assert v not in t


def _env(env_de_plus=None, sans=()):
    env = dict(os.environ, **SECRETS, VAST_API_KEY=FAUSSE_CLE_LOUEUR, NO_PROXY="127.0.0.1,localhost",
               no_proxy="127.0.0.1,localhost")
    for k in ("HTTP_PROXY", "http_proxy", "HTTPS_PROXY", "https_proxy", "ALL_PROXY", "all_proxy", *CONNUES, *sans):
        env.pop(k, None)
    env.update(env_de_plus or {})
    return env


CONNUES = ("COMMIT_ENTREE", "AMORCE_SHA256")


def _lanceur(*args, env_de_plus=None, entree=None):
    return subprocess.run([sys.executable, str(PROGRAMME), "--racine", str(DEPOT), *args], capture_output=True,
                          text=True, env=_env(env_de_plus), timeout=120, input=entree)


def _masquer(texte, *args, env_de_plus=None):
    r = _lanceur("masquer", *args, env_de_plus=env_de_plus, entree=texte)
    assert r.returncode == 0, r.stderr
    return r.stdout


# --- Le défaut constaté en vrai --------------------------------------------------------------------------------------

LIGNE_REELLE = f"Started. {{'success': True, 'new_contract': 62082700, 'instance_api_key': '{CLE_INSTANCE}'}}\n"


def test_ligne_reelle_du_loueur_la_cle_disparait_le_contrat_reste():
    sortie = _masquer(LIGNE_REELLE)
    assert CLE_INSTANCE not in sortie and CLE_INSTANCE[:16] not in sortie
    assert sortie == "Started. {'success': True, 'new_contract': 62082700, 'instance_api_key': '***'}\n"


def test_ligne_reelle_aussi_avec_la_liste_blanche_de_la_commande():
    sortie = _masquer(LIGNE_REELLE, "--commit-entree", COMMIT, "--amorce-sha256", EMPREINTE)
    assert CLE_INSTANCE not in sortie and "'new_contract': 62082700" in sortie


def test_la_v3_laissait_passer_la_cle():
    """Témoin du défaut : la v3, sur la même ligne, rend la clé ; la v4 non."""
    v3 = subprocess.run([sys.executable, str(DEPOT / "scripts/lanceur_machine_ligne_1_bras_a_v3.py"), "masquer"],
                        input=LIGNE_REELLE, capture_output=True, text=True, env=_env())
    assert v3.returncode == 0 and CLE_INSTANCE in v3.stdout
    assert CLE_INSTANCE not in _masquer(LIGNE_REELLE)


def test_reponse_json_raw():
    texte = json.dumps({"success": True, "new_contract": 62082700, "instance_api_key": CLE_INSTANCE}) + "\n"
    sortie = _masquer(texte)
    assert json.loads(sortie) == {"success": True, "new_contract": 62082700, "instance_api_key": "***"}


def test_json_indente_et_valeurs_non_chaines():
    texte = json.dumps({"a": {"Api_Key": "x", "jupyter_token": None, "secret": 42, "password": 'a"b'},
                        "new_contract": 7}, indent=1)
    sortie = json.loads(lm.masquer_texte(texte, [], []))
    assert sortie == {"a": {"Api_Key": "***", "jupyter_token": "***", "secret": "***", "password": "***"},
                      "new_contract": 7}


@pytest.mark.parametrize("nom", ["api_key", "APIKEY", "instance_api_key", "token", "jupyter_token", "client_secret",
                                 "password", "key", "ssh_key"])
def test_noms_de_secret_sous_toutes_les_formes(nom):
    v = "valeurSecrete42"
    for texte in (f'{{"{nom}": "{v}"}}', f"{{'{nom}': '{v}'}}", f"{nom}={v}", f"{nom} = '{v}'", f'["{nom}", "{v}"]',
                  f"('{nom}', '{v}')", f"https://h/x?{nom}={v}&n=1"):
        sortie = lm.masquer_texte(texte, [], [])
        assert v not in sortie and "***" in sortie, (texte, sortie)


def test_nom_egal_valeur():
    sortie = lm.masquer_texte("erreur : GH_TOKEN=abc123 HF_TOKEN=\"x y\" GO_ID=GO-2026-11-22-148 n=3\n", [], [])
    assert sortie == "erreur : GH_TOKEN=*** HF_TOKEN=\"***\" GO_ID=GO-2026-11-22-148 n=3\n"


def test_paires_de_variables():
    texte = "[['GH_TOKEN', 'abc'], ['GO_ID', 'GO-2026-11-22-148'], [\"Key\", 12]]"
    assert lm.masquer_texte(texte, [], []) == "[['GH_TOKEN', '***'], ['GO_ID', 'GO-2026-11-22-148'], [\"Key\", \"***\"]]"


def test_jetons_github_et_hugging_face():
    jetons = ["ghp_" + "A1b2" * 9, "gho_" + "Z9y8" * 9, "ghs_" + "Q7w6" * 9, "github_pat_" + "11ABC_def" * 5,
              "hf_" + "AbCdEfGh" * 4]
    sortie = _masquer("jetons : " + " ; ".join(jetons) + " ; hf_hub_download reste\n")
    assert not any(j in sortie for j in jetons) and sortie.count("***") == len(jetons)
    assert "hf_hub_download reste" in sortie


def test_suites_hexadecimales_masquees_empreintes_connues_gardees():
    autre = "f" * 40
    texte = f"commit {COMMIT} amorce {EMPREINTE} autre {autre} long {CLE_INSTANCE} court {'a' * 31} uuid 1234-abcd\n"
    sortie = _masquer(texte, "--commit-entree", COMMIT, "--amorce-sha256", EMPREINTE)
    assert COMMIT in sortie and EMPREINTE in sortie
    assert autre not in sortie and CLE_INSTANCE not in sortie and "a" * 31 in sortie and "uuid 1234-abcd" in sortie
    # sans liste blanche, tout est masqué
    nu = _masquer(texte)
    assert COMMIT not in nu and EMPREINTE not in nu
    # liste blanche par l'environnement, et en majuscules
    env = _masquer(texte.upper(), env_de_plus={"COMMIT_ENTREE": COMMIT, "AMORCE_SHA256": EMPREINTE})
    assert COMMIT.upper() in env and EMPREINTE.upper() in env and autre.upper() not in env
    # --connue
    assert autre in _masquer(texte, "--connue", autre)


def test_liste_blanche_ne_couvre_jamais_un_champ_de_secret():
    """Une valeur connue placée sous un nom de secret reste masquée (règle 1 avant la liste blanche)."""
    sortie = _masquer(f"{{'instance_api_key': '{EMPREINTE}'}}\n", "--amorce-sha256", EMPREINTE)
    assert EMPREINTE not in sortie


def test_liste_blanche_refuse_ce_qui_n_est_pas_une_empreinte():
    assert lm._liste_blanche(["abc", "x" * 40, COMMIT.upper(), EMPREINTE, None]) == frozenset({COMMIT, EMPREINTE})


def test_valeurs_de_l_environnement_masquees():
    sortie = _masquer(f"erreur : {SECRETS['CONTAINER_API_KEY']} et {FAUSSE_CLE_LOUEUR} et api_key\n")
    assert sortie == "erreur : *** et *** et api_key\n"


# --- Essais de la v3 portés -------------------------------------------------------------------------------------------

def test_masquer_structure():
    v = list(SECRETS.values())
    sortie = lm.masquer({"a": [["HF_TOKEN", "z"], ["GO_ID", "g"]], "Api_Key": "k", "b": f"x{v[0]}y", "n": 3,
                         "c": f"{{'instance_api_key': '{CLE_INSTANCE}'}}", "d": COMMIT}, v, [COMMIT])
    assert sortie == {"a": [["HF_TOKEN", "***"], ["GO_ID", "g"]], "Api_Key": "***", "b": "x***y", "n": 3,
                      "c": "{'instance_api_key': '***'}", "d": COMMIT}


def test_masquer_recopie_l_entree_masquee():
    r = subprocess.run([sys.executable, str(PROGRAMME), "masquer"], input=f"erreur : {SECRETS['GH_TOKEN']} et api_key\n",
                       capture_output=True, text=True, env=_env())
    assert r.returncode == 0 and r.stdout == "erreur : *** et api_key\n"


def test_creation_imprime_la_commande_sans_valeur_secrete():
    from vastai.utils import parse_env
    r = _lanceur("creation", "--offre", "123456", "--commit-entree", "a" * 40, "--sans-verifier-entree")
    assert r.returncode == 0, r.stderr
    ligne = r.stdout.strip()
    assert ligne.startswith(f"GO_ID=GO-2026-11-22-148 {CREER} 123456 --image "
                            "pytorch/pytorch:2.14.1-cuda13.0-cudnn9-runtime --disk 150 ")
    assert "--onstart scripts/amorce_appel_ligne_1_bras_a_v3.sh 2>&1 | " in ligne
    assert ligne.endswith(f"scripts/lanceur_machine_ligne_1_bras_a_v5.py masquer --commit-entree {'a' * 40} "
                          f"--amorce-sha256 {_sha(AMORCE)}")
    brut = ligne.split('--env "')[1].split('"')[0]
    assert "-e GH_TOKEN=${GH_TOKEN:?} -e HF_TOKEN=${HF_TOKEN:?} " in brut and "-e AVANT_CREATION_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)" in brut
    developpe = subprocess.run(["bash", "-c", f'printf "%s" "{brut}"'], capture_output=True, text=True,
                               env=dict(os.environ, **SECRETS)).stdout
    env = parse_env(developpe)
    assert env["GH_TOKEN"] == SECRETS["GH_TOKEN"] and env["HF_TOKEN"] == SECRETS["HF_TOKEN"] and env["COMMIT_ENTREE"] == "a" * 40
    assert env["BRANCHE_ENTREE"] == "entree/bras-a-ligne-1-v2" and env["BRANCHE_SORTIE"] == "calcul/bras-a-ligne-1-v2"
    assert env["AMORCE_SHA256"] == _sha(AMORCE) and env["GO_ID"] == "GO-2026-11-22-148"
    assert datetime.strptime(env["AVANT_CREATION_UTC"], "%Y-%m-%dT%H:%M:%SZ")
    exiger_aucun_secret(textes=[r.stdout, r.stderr])
    assert _lanceur("creation", "--offre", "0", "--commit-entree", "a" * 40, "--sans-verifier-entree").returncode == 2


def test_tuyau_de_la_commande_imprimee_masque_la_ligne_reelle():
    """La queue imprimée (après `|`), jouée telle quelle sur la ligne réelle : clé masquée, contrat lisible."""
    r = _lanceur("creation", "--offre", "123456", "--commit-entree", COMMIT, "--sans-verifier-entree")
    queue = r.stdout.strip().split("2>&1 | ", 1)[1]
    t = subprocess.run(["bash", "-c", queue], cwd=DEPOT, input=LIGNE_REELLE + f"commit {COMMIT}\n", capture_output=True,
                       text=True, env=_env())
    assert t.returncode == 0, t.stderr
    assert CLE_INSTANCE not in t.stdout and "'new_contract': 62082700" in t.stdout and COMMIT in t.stdout


@pytest.fixture()
def nu(tmp_path):
    depot = tmp_path / "nu.git"
    _git("init", "-q", "--bare", str(depot))
    travail = tmp_path / "travail"
    _git("init", "-q", str(travail))
    (travail / "f.txt").write_text("x\n")
    _git("add", "f.txt", cwd=travail)
    _git("commit", "-q", "-m", "entree", cwd=travail)
    _git("push", "-q", str(depot), "HEAD:refs/heads/entree/jouet-creation", cwd=travail)
    return depot, _git("rev-parse", "HEAD", cwd=travail).strip()


def test_creation_verifie_l_entree_sur_le_distant(nu):
    depot, commit = nu
    ok = _lanceur("creation", "--offre", "7", "--commit-entree", commit, "--distant", str(depot),
                  "--branche-entree", "entree/jouet-creation", "--branche-sortie", "calcul/jouet-creation-neuve")
    assert ok.returncode == 0, ok.stderr
    mauvais = _lanceur("creation", "--offre", "7", "--commit-entree", "b" * 40, "--distant", str(depot),
                       "--branche-entree", "entree/jouet-creation", "--branche-sortie", "calcul/jouet-creation-neuve")
    assert mauvais.returncode == 2 and "attendu" in mauvais.stderr
    # le commit cité par la commande reste lisible ; celui lu sur le distant n'est pas dans la liste blanche
    assert "b" * 40 in mauvais.stderr and "distant ***" in mauvais.stderr


def test_verification_refuse_une_branche_absente(nu):
    depot, _ = nu
    r = _lanceur("verification", "--branche-sortie", "calcul/jouet-absente", "--distant", str(depot))
    assert r.returncode == 2 and "absente" in r.stderr


class _Loueur(http.server.BaseHTTPRequestHandler):
    vus: list = []

    def do_GET(self):
        _Loueur.vus.append((self.path, self.headers.get("Authorization")))
        corps = {"instances": {"id": 4242, "actual_status": "running", "dph_total": 1.2, "start_date": 1795400000.7,
                               "label": "bras-a-ligne-1-v1", "status_msg": "jeton " + SECRETS["GH_TOKEN"]
                               + f" cle {CLE_INSTANCE}",
                               "extra_env": [["GH_TOKEN", SECRETS["GH_TOKEN"]], ["GO_ID", "GO-2026-11-22-148"]],
                               "api_key": "x", "jupyter_token": "y", "instance_api_key": CLE_INSTANCE}}
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
    assert sortie["start_date_utc"] == "2026-11-23T02:13:20Z" and sortie["status_msg"] == "jeton *** cle ***"
    assert sortie["prix_reel_sous_le_constat"] is False and "destruction" in sortie["consigne"]
    assert _Loueur.vus == [("/api/v0/instances/4242/?owner=me", f"Bearer {FAUSSE_CLE_LOUEUR}")]
    exiger_aucun_secret(textes=[r.stdout, r.stderr])
    assert _lanceur("etat", "--instance", "42; x").returncode == 2


def test_verification_garde_le_commit_et_l_empreinte_calcules(monkeypatch):
    """La vérification met dans la liste blanche le commit lu et l'empreinte du manifeste qu'elle a calculés."""
    sortie = {"commit": COMMIT, "manifeste_du_versement_sha256": EMPREINTE, "motif": f"x {CLE_INSTANCE}"}
    lignes = []
    monkeypatch.setattr("builtins.print", lambda *a, **k: lignes.append(a[0]))
    lm.ecrire(sortie, connues=[COMMIT, EMPREINTE])
    lu = json.loads(lignes[0])
    assert lu["commit"] == COMMIT and lu["manifeste_du_versement_sha256"] == EMPREINTE and lu["motif"] == "x ***"


def test_constantes_de_la_v5():
    assert lm.CE_PROGRAMME == "scripts/lanceur_machine_ligne_1_bras_a_v5.py" and lm.MASQUE == "***"
    assert lm.AMORCE == "scripts/amorce_appel_ligne_1_bras_a_v3.sh" and lm.AMORCE_COMPLETE == "scripts/amorce_ligne_1_bras_a_v4.sh"
    assert lm.BRANCHE_ENTREE == "entree/bras-a-ligne-1-v2" and lm.BRANCHE_SORTIE == "calcul/bras-a-ligne-1-v2"
    assert lm.GO_ID == "GO-2026-11-22-148"
