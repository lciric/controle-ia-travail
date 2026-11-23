"""L'essai qui aurait vu le défaut de l'amorce de lecture du barreau 5 : le clone partiel des entrées sans l'aide
d'identification. Erratum de chaîne de la relecture décisive, v2 (`01298f0f…`), § 6.1 ; écrit avant le code (R5).

Le monde : un dépôt nu servi par `git http-backend`, derrière un serveur HTTP local (127.0.0.1, `ThreadingHTTPServer`, petit
gestionnaire maison) qui exige « Authorization: Basic » avec un jeton factice et répond 401 sinon ; `uploadpack.allowFilter`
et `http.receivepack` posés ; une branche du code (montée comme dans `tests/test_amorce_b5f_lecture_entiere_v1.py`, dont les
faux outils sont importés, déclaré : `FAUX`, `PYTHON_VENV`, `CLES` ; la fausse marche est la sienne, à une ligne près :
l'inventaire de l'arbre fermé porte ses fichiers, pour que `relecture_v1.ligne_scores` figée l'accepte) ; une branche des
entrées (un commit de base, puis un commit qui ajoute le dossier) ; l'URL officielle réécrite vers le serveur par
`insteadOf` ; serveur arrêté par `shutdown()`. Environnement (constat C9) : toutes les variables `GIT_*` retirées, puis
celles de l'essai posées (`HOME` et configuration globale propres, `GIT_CONFIG_NOSYSTEM=1`, `GIT_TERMINAL_PROMPT=0`) ;
variables de mandataire retirées ; `NO_PROXY=127.0.0.1,localhost`. Aucun réseau extérieur.

Scénarios, joués une fois par le gabarit du module (l'amorce entière, en essai à blanc, sortie écrite dans des fichiers, pour
ne pas attendre la minuterie, qui vit jusqu'à son échéance et que le gabarit attend avant de rendre la main ; aucun signal
n'est envoyé par l'essai) :
- monde A, dans l'ordre : l'amorce figée (le défaut, rejoué) ; l'amorce corrigée, branche de sortie présente (R12) ; copie
  de la branche de sortie sous `traces/barreau5-lecture-tentative-1` (même commit) et suppression à tête vérifiée ;
  l'amorce corrigée (cas sain) ;
- monde B : l'amorce corrigée, l'inscription de l'aide dans le clone des entrées refusée par un faux `git` en tête du `PATH`
  (artefact de la garde neuve, constat C8).
"""
from __future__ import annotations

import base64
import http.server
import os
import shutil
import subprocess
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

import pytest

import test_amorce_b5f_lecture_entiere_v1 as entiere      # faux outils de l'essai à blanc, réemployés (déclaré)
from controle_ia.barreau5_familles import commande_lecture_v3 as cl3
from controle_ia.barreau5_familles import relecture_v1 as rv

RACINE_DEPOT = Path(__file__).resolve().parents[1]
AMORCE_FIGEE = RACINE_DEPOT / rv.AMORCE
URL = entiere.URL
RUN = entiere.RUN
PREREG = entiere.PREREG
CLES = entiere.CLES
JETON = CLES[0]                                   # GH_TOKEN factice de l'amorce
UTILISATEUR = "x-access-token"                    # celui de l'aide d'identification de l'amorce
BRANCHE_CODE = "lot/b5f-lecture-v1"
SORTIE = "donnees/barreau5-familles-jumelles-v1-lecture"
COPIE = "traces/barreau5-lecture-tentative-1"
VRAI_GIT = shutil.which("git")
# l'inventaire de l'arbre fermé porte ses fichiers (seule différence avec la fausse marche de l'essai à blanc)
_INVENTAIRE_VIDE = """ecrire "donnees/$R/lecture/inventaire.json" '{"format": "b5f-inventaire-lecture-v1"}'"""
_INVENTAIRE_PLEIN = """inv() { local b="donnees/$R/lecture" p=1 f
    printf '{"format": "b5f-inventaire-lecture-v1", "run_id": "%s", "fichiers": [' "$R"
    for f in bilan-relecture.json scores/decisive-pli0.json jetons/decisive-pli0/X-01.json; do
        [ "$p" = 1 ] || printf ', '; p=0
        printf '{"chemin": "%s", "octets": %s, "sha256": "%s"}' "$f" "$(stat -c %s "$b/$f")" "$(sha256sum < "$b/$f" | cut -c1-64)"
    done; printf ']}'; }
ecrire "donnees/$R/lecture/inventaire.json" "$(inv)\""""
assert entiere.FAUSSE_MARCHE.count(_INVENTAIRE_VIDE) == 1
FAUSSE_MARCHE = entiere.FAUSSE_MARCHE.replace(_INVENTAIRE_VIDE, _INVENTAIRE_PLEIN)
# faux git du monde B : refuse la seule inscription de l'aide dans le clone des entrées ; tout le reste au vrai git
FAUX_GIT = """#!/usr/bin/env bash
if [ "${1:-}" = -C ] && [ "${2:-}" = "$ENTREES_REFUSEES" ] && [ "${3:-}" = config ] && [ "${4:-}" = credential.helper ]; then
    echo "faux git : inscription de l'aide refusée" >&2; exit 1; fi
exec "$VRAI_GIT" "$@"
"""


# --- le serveur : git http-backend derrière une identification Basic -----------------------------------------------------

def _gestionnaire(racine_projets: Path, journal: list):
    attendu = "Basic " + base64.b64encode(f"{UTILISATEUR}:{JETON}".encode()).decode()

    class Gestionnaire(http.server.BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.0"

        def log_message(self, *a):
            pass

        def _corps(self) -> bytes:
            if self.headers.get("Transfer-Encoding", "").lower() == "chunked":
                morceaux = []
                while True:
                    n = int(self.rfile.readline().strip().split(b";")[0], 16)
                    if n == 0:
                        while self.rfile.readline().strip():
                            pass
                        return b"".join(morceaux)
                    morceaux.append(self.rfile.read(n))
                    self.rfile.readline()
            return self.rfile.read(int(self.headers.get("Content-Length") or 0))

        def _servir(self):
            identifie = self.headers.get("Authorization") == attendu
            journal.append((self.command, self.path, identifie))
            if not identifie:
                self.send_response(401)
                self.send_header("WWW-Authenticate", 'Basic realm="essai"')
                self.send_header("Content-Length", "0")
                self.end_headers()
                return
            corps = self._corps()
            chemin, _, requete = self.path.partition("?")
            env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(racine_projets),
                   "GIT_CONFIG_NOSYSTEM": "1", "GIT_PROJECT_ROOT": str(racine_projets), "GIT_HTTP_EXPORT_ALL": "1",
                   "PATH_INFO": chemin, "QUERY_STRING": requete, "REQUEST_METHOD": self.command,
                   "CONTENT_TYPE": self.headers.get("Content-Type", ""), "CONTENT_LENGTH": str(len(corps)),
                   "REMOTE_USER": UTILISATEUR, "REMOTE_ADDR": "127.0.0.1"}
            if self.headers.get("Git-Protocol"):
                env["GIT_PROTOCOL"] = self.headers["Git-Protocol"]
            if self.headers.get("Content-Encoding"):
                env["HTTP_CONTENT_ENCODING"] = self.headers["Content-Encoding"]
            p = subprocess.run([VRAI_GIT, "http-backend"], input=corps, env=env, capture_output=True)
            sep = b"\r\n\r\n" if b"\r\n\r\n" in p.stdout else b"\n\n"
            tete, _, reste = p.stdout.partition(sep)
            code, entetes = 200, []
            for ligne in tete.decode("latin-1").splitlines():
                if ":" not in ligne:
                    continue
                k, v = (x.strip() for x in ligne.split(":", 1))
                if k.lower() == "status":
                    code = int(v.split()[0])
                else:
                    entetes.append((k, v))
            self.send_response(code)
            for k, v in entetes:
                self.send_header(k, v)
            self.send_header("Content-Length", str(len(reste)))
            self.end_headers()
            self.wfile.write(reste)

        do_GET = do_POST = _servir

    return Gestionnaire


# --- le monde ------------------------------------------------------------------------------------------------------------

def _git(r, *a, env=None):
    return subprocess.run([VRAI_GIT, "-C", str(r), *a], check=True, capture_output=True, text=True, env=env).stdout.strip()


def _env_git_propre(home: Path) -> dict:
    """Constat C9 : toutes les variables `GIT_*` retirées (dont `GIT_CONFIG_COUNT`, `GIT_CONFIG_KEY_*`,
    `GIT_CONFIG_VALUE_*`, `GIT_CONFIG_PARAMETERS`, `GIT_ASKPASS`), puis celles de l'essai ; mandataires retirés."""
    mandataires = {"http_proxy", "https_proxy", "all_proxy", "no_proxy", "ftp_proxy"}
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(("GIT_", "CONTAINER_", "B5F_", "AMORCE_", "SSH_ASKPASS")) and k.lower() not in mandataires}
    env.update({"HOME": str(home), "GIT_CONFIG_NOSYSTEM": "1", "GIT_TERMINAL_PROMPT": "0",
                "NO_PROXY": "127.0.0.1,localhost", "no_proxy": "127.0.0.1,localhost"})
    return env


def _monter_depot(t: Path, projets: Path, nom: str) -> dict:
    """Dépôt nu servi, branche du code (fichiers de l'essai à blanc), branche des entrées (base, puis le dossier)."""
    nu = projets / nom
    subprocess.run([VRAI_GIT, "init", "-q", "--bare", "-b", "main", str(nu)], check=True)
    for k, v in (("uploadpack.allowFilter", "true"), ("http.receivepack", "true")):
        _git(nu, "config", k, v)
    g = t / f"graine-{nom}"
    g.mkdir()
    for a in (["init", "-q", "-b", BRANCHE_CODE], ["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _git(g, *a)
    fichiers = {"requirements-gpu.txt": "-r requirements-cpu.txt\n-r requirements-donnees.txt\n",
                "requirements-cpu.txt": "numpy\n", "requirements-donnees.txt": "\n", "pyproject.toml": "[project]\n",
                "src/controle_ia/__init__.py": "", "tests/conftest.py": "",
                "tests/test_barreau5_familles_lecture_v1.py": "", "tests/test_barreau5_familles_sondes_v1.py": "",
                "tests/test_barreau5_familles_relecture_v1.py": "", rv.CONFIG_SCELLEE["chemin"]: "{}\n",
                PREREG: "# texte\n", "registres/barreau5-familles-jumelles-v1.md": "\n",
                "donnees/20261007-082440-t05-extraction/taches-evaluation.json": "{}\n",
                "docs/sources/invites-2606.08892-v1/index.json": "{}\n", "docs/notes/secret.md": "jamais extrait\n"}
    for chemin, contenu in fichiers.items():
        (g / chemin).parent.mkdir(parents=True, exist_ok=True)
        (g / chemin).write_text(contenu, encoding="utf-8")
    for f in (".gitignore", ".gitattributes", rv.AMORCE, "scripts/lancer_b5f_lecture_v1.sh"):
        (g / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(RACINE_DEPOT / f, g / f)
    _git(g, "add", "-A")
    _git(g, "add", "-f", "donnees")
    _git(g, "commit", "-q", "-m", "code")
    _git(g, "push", "-q", str(nu), BRANCHE_CODE)
    e = t / f"entrees-{nom}"
    e.mkdir()
    for a in (["init", "-q", "-b", "x"], ["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _git(e, *a)
    (e / "LISEZ-MOI").write_text("base\n")
    _git(e, "add", "-A")
    _git(e, "commit", "-q", "-m", "base")
    d = e / rv.DOSSIER_ENTREES
    d.mkdir()
    for n in ("X-01.safetensors", "A1-saboteur.safetensors"):
        (d / n).write_bytes(n.encode())
    _git(e, "add", "-A")
    _git(e, "commit", "-q", "-m", "entrées de lecture")
    _git(e, "push", "-q", str(nu), f"x:refs/heads/{rv.BRANCHE_ENTREES}")
    return {"nu": nu, "commit": _git(g, "rev-parse", "HEAD"), "entrees": _git(e, "rev-parse", "HEAD")}


def _jouer_amorce(t: Path, amorce: Path, depot: dict, port: int, nom: str, outils: Path, ajout_path: Path | None = None
                  ) -> dict:
    """L'amorce entière, en essai à blanc, sous `RACINE_AMORCE` neuve ; sortie dans des fichiers (la minuterie, en arrière-
    plan, vit jusqu'à son échéance : le gabarit l'attend)."""
    home = t / f"home-{nom}"
    home.mkdir()
    (home / ".gitconfig").write_text(f'[url "http://127.0.0.1:{port}/{depot["nu"].name}"]\n\tinsteadOf = {URL}\n',
                                     encoding="utf-8")
    j = t / f"journaux-{nom}"
    j.mkdir()
    racine = t / f"racine-{nom}"
    env = _env_git_propre(home)
    env.update({"PATH": (f"{ajout_path}:" if ajout_path else "") + f"{outils}:{os.environ['PATH']}",
                "AMORCE_ESSAI_BLANC": "1", "RACINE_AMORCE": str(racine), "B5F_SANS_ATTENTE": "1",
                "B5F_PAS_MINUTERIE": "1", "B5F_VERSEMENT_S": "1", "B5F_MINUTERIE_UNE_FOIS": "1",
                "PLAN_B5F": "decisif", "COMMIT": depot["commit"], "BRANCHE_CODE": BRANCHE_CODE, "PREREG": PREREG,
                "RUN_LECTURE": RUN, "PRIX_USD_H": "1.2", "GO_ID": "GO-2026-11-24-01", "DEPOT_URL": URL,
                "ENTREES_COMMIT": depot["entrees"], "DIVERGENCE_B5F": "1", "GARDE_B5F": "une_sur_dix",
                "EXISTANTS_B5F": "W10=", "EXISTANTS_CHEMINS": "-", "GH_TOKEN": CLES[0], "HF_TOKEN": CLES[1],
                "CONTAINER_ID": "4242", "CONTAINER_API_KEY": CLES[2], "JOURNAL_CURL": str(j / "curl.txt"),
                "JOURNAL_TIMEOUT": str(j / "timeout.txt"), "JOURNAL_MARCHE": str(j / "marche.txt"),
                "JOURNAL_CONFIG": str(j / "config.txt"), "FAUX_PYTHON_VENV": str(outils / "python-venv"),
                "FAUSSE_MARCHE": str(outils / "fausse-marche"), "VRAI_PYTHON3": shutil.which("python3"),
                "VRAI_TIMEOUT": shutil.which("timeout"), "VRAI_GIT": VRAI_GIT,
                "ENTREES_REFUSEES": str(racine / "b5f-lecture-v1" / "entrees"),
                "FAUX_PYTEST_LIGNE": f"{entiere.MIN_ESSAIS} passed in 1.00s", "FAUX_PYTEST_CODE": "0",
                "ECHEANCE_ARRET_UTC_S": str(int(time.time()) + 62)})
    with open(j / "sortie.txt", "wb") as so, open(j / "erreur.txt", "wb") as se:
        p = subprocess.run(["bash", str(amorce)], env=env, stdout=so, stderr=se, stdin=subprocess.DEVNULL, timeout=240)
    T = racine / "b5f-lecture-v1"
    lire = lambda f: f.read_text(encoding="utf-8", errors="replace") if f.exists() else ""  # noqa: E731
    return {"code": p.returncode, "sortie": lire(j / "sortie.txt"), "erreur": lire(j / "erreur.txt"),
            "journal_f": T / "traces" / "journal-b5f-lecture.txt", "T": T, "D": T / "depot", "E": T / "entrees",
            "marche": lire(j / "marche.txt"), "racine": racine, "home": home, "env": env}


def _journal(r) -> str:
    return r["journal_f"].read_text(encoding="utf-8") if r["journal_f"].exists() else ""


def _branche(nu: Path, nom: str = SORTIE):
    tete = subprocess.run([VRAI_GIT, "-C", str(nu), "rev-parse", "--verify", "-q", f"refs/heads/{nom}"],
                          capture_output=True, text=True).stdout.strip()
    return tete, (_git(nu, "ls-tree", "-r", "--name-only", tete).split() if tete else [])


@pytest.fixture(scope="module")
def scenarios(tmp_path_factory):
    t = tmp_path_factory.mktemp("b5f-identification")
    projets = t / "projets"
    projets.mkdir()
    A, B = _monter_depot(t, projets, "distant.git"), _monter_depot(t, projets, "distant-b.git")
    outils = t / "outils"
    outils.mkdir()
    for nom, contenu in {**entiere.FAUX, "python-venv": entiere.PYTHON_VENV, "fausse-marche": FAUSSE_MARCHE}.items():
        (outils / nom).write_text(contenu, encoding="utf-8")
        (outils / nom).chmod(0o755)
    faux_git = t / "faux-git"
    faux_git.mkdir()
    (faux_git / "git").write_text(FAUX_GIT, encoding="utf-8")
    (faux_git / "git").chmod(0o755)
    corrigee = t / "amorce-corrigee" / "amorce_b5f_lecture_v1.sh"
    corrigee.parent.mkdir()
    corrigee.write_bytes(cl3.amorce_corrigee(AMORCE_FIGEE.read_bytes()))
    journal_http = []
    serveur = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _gestionnaire(projets, journal_http))
    fil = threading.Thread(target=serveur.serve_forever, daemon=True)
    fil.start()
    port = serveur.server_address[1]
    sortie = {"A": A, "B": B, "port": port, "journal_http": journal_http, "t": t}
    try:
        def monde_b():
            sortie["garde_neuve"] = _jouer_amorce(t, corrigee, B, port, "garde-neuve", outils, ajout_path=faux_git)
        fb = threading.Thread(target=monde_b)
        fb.start()
        sortie["defaut"] = _jouer_amorce(t, AMORCE_FIGEE, A, port, "defaut", outils)
        sortie["tete_defaut"], sortie["fichiers_defaut"] = _branche(A["nu"])
        sortie["r12"] = _jouer_amorce(t, corrigee, A, port, "r12", outils)
        sortie["tete_apres_r12"] = _branche(A["nu"])[0]
        tete = sortie["tete_defaut"]
        if tete:                       # voie B : copie sous traces/…, même commit, puis suppression à tête vérifiée
            _git(A["nu"], "update-ref", f"refs/heads/{COPIE}", tete)
            _git(A["nu"], "update-ref", "-d", f"refs/heads/{SORTIE}", tete)
        sortie["sain"] = _jouer_amorce(t, corrigee, A, port, "sain", outils)
        fb.join(timeout=300)
        # sans réseau extérieur : un clone local (tous les refs) pour la ligne figée des scores
        clone = t / "clone-verif"
        subprocess.run([VRAI_GIT, "clone", "-q", str(A["nu"]), str(clone)], check=True, capture_output=True,
                       env=_env_git_propre(t))
        sortie["clone"] = clone
        # témoin : une requête sans identification
        try:
            urllib.request.build_opener(urllib.request.ProxyHandler({})).open(
                f"http://127.0.0.1:{port}/distant.git/info/refs?service=git-upload-pack", timeout=30)
            sortie["sans_identification"] = 200
        except urllib.error.HTTPError as e:
            sortie["sans_identification"] = e.code
        yield sortie
    finally:
        # la minuterie de chaque amorce vit jusqu'à son échéance (une seule demande, essai à blanc) : on l'attend
        limite = time.time() + 180
        for k in ("defaut", "r12", "sain", "garde_neuve"):
            r = sortie.get(k)
            while r is not None and "MINUTERIE :" not in _journal(r) and time.time() < limite:
                time.sleep(1)
        serveur.shutdown()
        serveur.server_close()


# --- témoins -------------------------------------------------------------------------------------------------------------

def test_temoin_une_requete_sans_identification_recoit_401(scenarios):
    assert scenarios["sans_identification"] == 401
    assert any(not ok for _, _, ok in scenarios["journal_http"]) and any(ok for _, _, ok in scenarios["journal_http"])


def test_artefact_le_defaut_l_amorce_figee_tombe_au_checkout_des_entrees(scenarios):
    """L'amorce figée, dans ce même monde : journal « ARRET : commit des entrées <C> introuvable » ; sortie d'erreur avec
    « could not read Username » et « promisor remote » ; branche de sortie créée avec les seules traces. C'est l'incident,
    rejoué ; le cas sain ne vaut que parce que ceci tombe."""
    r, A = scenarios["defaut"], scenarios["A"]
    assert r["code"] == 2, r["erreur"][-2000:] + _journal(r)
    assert f"ARRET : commit des entrées {A['entrees']} introuvable" in _journal(r)
    assert "could not read Username" in r["erreur"] and "promisor remote" in r["erreur"], r["erreur"][-2000:]
    assert scenarios["tete_defaut"] and scenarios["fichiers_defaut"]
    ajoutes = _git(A["nu"], "diff", "--name-only", A["commit"], scenarios["tete_defaut"]).split()
    assert ajoutes and all(f.startswith("traces-b5f-lecture/") for f in ajoutes), ajoutes
    assert not r["marche"]
    # « remote.origin.promisor » n'est pas un témoin : git le pose dans le clone des entrées, qui tombe pourtant
    assert _git(r["E"], "config", "--get", "remote.origin.promisor") == "true"
    assert not (r["E"] / rv.DOSSIER_ENTREES).exists()


def test_artefact_r12_branche_de_sortie_presente_l_amorce_corrigee_refuse_avant_tout_clone_des_entrees(scenarios):
    r = scenarios["r12"]
    assert r["code"] == 2
    assert "branche de sortie donnees/barreau5-familles-jumelles-v1-lecture présente sur le dépôt distant (R12)" in _journal(r)
    assert not r["E"].exists() and "clonage des entrées" not in _journal(r)
    assert scenarios["tete_apres_r12"] == scenarios["tete_defaut"]       # rien poussé sur la branche gardée


def test_artefact_la_garde_neuve_inscription_de_l_aide_refusee_arret_sans_extraction(scenarios):
    """Constat C8 : un faux `git` refuse la seule inscription de l'aide dans le clone des entrées : la ligne ajoutée
    arrête l'amorce au journal, et aucune extraction n'est tentée."""
    r = scenarios["garde_neuve"]
    j = _journal(r)
    assert r["code"] == 2, r["erreur"][-2000:] + j
    assert "ARRET : aide d'identification non inscrite dans le clone des entrées" in j
    assert "faux git : inscription de l'aide refusée" in r["erreur"]
    assert "extraction des entrées" not in j and "commit des entrées" not in j
    assert r["E"].is_dir() and not (r["E"] / rv.DOSSIER_ENTREES).exists()
    assert subprocess.run([VRAI_GIT, "-C", str(r["E"]), "config", "--get", "credential.helper"],
                          capture_output=True).returncode != 0
    assert not r["marche"]


def test_cas_sain_voie_b_copie_suppression_puis_amorce_corrigee(scenarios):
    """Voie B : la branche de sortie copiée sous `traces/…` (même commit), supprimée, puis l'amorce corrigée : entrées
    extraites, fausse marche, versement sur `…-lecture`, preuve, témoin ; `relecture_v1.ligne_scores`, figée, accepte le
    commit prouvé ; le clone des entrées porte l'aide sans la valeur du jeton ; le jeton factice n'est écrit nulle part."""
    r, A = scenarios["sain"], scenarios["A"]
    j = _journal(r)
    assert r["code"] == 0, r["erreur"][-2000:] + j
    assert _branche(A["nu"], COPIE)[0] == scenarios["tete_defaut"]
    assert sorted(p.relative_to(r["E"]).as_posix() for p in r["E"].rglob("*") if p.is_file() and ".git" not in p.parts) \
        == [f"{rv.DOSSIER_ENTREES}/A1-saboteur.safetensors", f"{rv.DOSSIER_ENTREES}/X-01.safetensors"]
    assert f"entrées de lecture au commit {A['entrees']}" in j and f"--run-id {RUN}" in r["marche"]
    tete, fichiers = _branche(A["nu"])
    assert tete and tete != scenarios["tete_defaut"] and f"donnees/{RUN}/lecture/inventaire.json" in fichiers
    prouve = (r["T"] / "versement-final-prouve").read_text().strip()
    assert prouve == (r["T"] / "versement-des-sorties-prouve").read_text().strip()
    contenu = rv.ligne_scores(scenarios["clone"], prouve, RUN)
    assert contenu.startswith(f"commit {prouve} ; inventaire sha256 ") and contenu.split()[-1] in j
    aide = _git(r["E"], "config", "--get", "credential.helper")
    assert "${GH_TOKEN}" in aide and JETON not in aide
    # le jeton factice n'est écrit dans aucun fichier de l'instance, ni dans le journal, ni sur la branche poussée
    for f in r["T"].rglob("*"):
        if f.is_file():
            assert JETON.encode() not in f.read_bytes(), f
    for f in fichiers:
        assert JETON not in _git(A["nu"], "show", f"{tete}:{f}")
    assert JETON not in r["sortie"] + r["erreur"]
    # l'empreinte écrite au journal distingue l'amorce corrigée de la figée (écart 13 de l'erratum)
    assert f"amorce de lecture v1 : empreinte {cl3.AMORCE_CORRIGEE_SHA256}" in j
    assert f"amorce de lecture v1 : empreinte {cl3.AMORCE_FIGEE_SHA256}" in _journal(scenarios["defaut"])
