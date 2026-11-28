#!/usr/bin/env python3
"""Essais R5 locaux du lot v2 (amorce, filet, lanceur) de la suite des tests sur Hetzner (GO-2026-11-28-04).

Chemin du serveur reproduit : amorce en super-utilisateur, essais sous l'utilisateur sans privilège « essais », dépôt
d'origine nu en file://, faux serveur d'API Hetzner (métadonnées, liste par nom, DELETE) sur 127.0.0.1, règle
iptables propre à l'utilisateur des essais pour le cas sain de l'autotest du cloisonnement.
Scénarios (cas sain et artefact pour chaque garde, R5) :
  A sain ; B retrait des jetons sauté ; C minuterie pendant les essais ; D jetons illisibles par les essais ;
  E branche de sortie existante (repli réduit) ; F minuterie pendant une étape d'installation ;
  G métadonnées absentes (identifiant retrouvé par le nom) ; H amorce tuée par SIGKILL (filet indépendant) ;
  I DELETE refusé cinq fois ; K métadonnées lisibles par les essais (autotest, arrêt 13) ;
  L garde-fous du lanceur (GO échu, de mauvais type, révoqué ; dépôt, nom, plafond ; données de démarrage).
Sortie : résumé JSON ; code 0 si tout passe.
"""
from __future__ import annotations

import base64
import gzip
import hashlib
import http.server
import importlib.util
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
from datetime import date
from pathlib import Path
from types import SimpleNamespace

DEPOT_PROGRAMME = Path(__file__).resolve().parents[3]
AMORCE = DEPOT_PROGRAMME / "scripts" / "amorce_hetzner_suite_tests_v2.sh"
FILET = DEPOT_PROGRAMME / "scripts" / "filet_hetzner_suite_tests_v2.sh"
LANCEUR = DEPOT_PROGRAMME / "scripts" / "lancer_hetzner_suite_tests_v2.py"
PY = DEPOT_PROGRAMME / ".venv" / "bin" / "python3"
BASE = Path("/home/user/essais-r5-suite-tests-v2")
JETON_GH = "ghp_EssaiR5JetonFactice0123456789abcdef"
JETON_HC = "hcEssaiR5JetonFacticeHetzner0123456789"
UTILISATEUR = "essais"
MODE = {"metadonnees": "ok", "delete": "ok"}


class FausseAPI(http.server.BaseHTTPRequestHandler):
    supprimes: list[tuple[str, bool]] = []

    def do_GET(self):
        if self.path.endswith("/metadata/instance-id"):
            return self._r(200, b"424242") if MODE["metadonnees"] == "ok" else self._r(404, b"")
        if self.path.startswith("/v1/servers?name=essai-r5-G"):
            return self._r(200, b'{"servers":[{"id":777,"name":"essai-r5-G"}]}')
        return self._r(404, b"")

    def do_DELETE(self):
        FausseAPI.supprimes.append((self.path, self.headers.get("Authorization", "") == f"Bearer {JETON_HC}"))
        return self._r(500, b"{}") if MODE["delete"] == "refus" else self._r(200, b'{"action":{}}')

    def _r(self, code, corps):
        self.send_response(code)
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)

    def log_message(self, *a):
        pass


def sh(*cmd, **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def depot_essai(dossier: Path, lent: int) -> tuple[str, str]:
    src = dossier / "src-depot"
    (src / "tests").mkdir(parents=True)
    (src / "pyproject.toml").write_text('[tool.pytest.ini_options]\ntestpaths = ["tests"]\n')
    (src / "tests" / "test_ok.py").write_text(
        "import pytest\n\n@pytest.mark.parametrize('k', range(6))\ndef test_ok(k):\n    assert k + k == 2 * k\n")
    (src / "tests" / "test_echec.py").write_text(
        f"def test_echec():\n    print('fuite simulee : {JETON_GH}')\n    assert False, '{JETON_GH}'\n")
    if lent:
        (src / "tests" / "test_lent.py").write_text(f"import time\n\ndef test_lent():\n    time.sleep({lent})\n")
    sh("git", "init", "-q", "-b", "main", str(src))
    sh("git", "-C", str(src), "add", "-A")
    sh("git", "-C", str(src), "-c", "user.name=essai", "-c", "user.email=essai@invalid", "commit", "-q", "-m", "essai")
    origine = dossier / "origin.git"
    sh("git", "clone", "-q", "--bare", str(src), str(origine))
    sh("git", "-C", str(origine), "config", "uploadpack.allowReachableSHA1InWant", "true")
    return f"file://{origine}", sh("git", "-C", str(src), "rev-parse", "HEAD").stdout.strip()


def preparer(nom: str, port: int, lent: int = 0, plafond: int = 600, **extra) -> tuple[Path, dict]:
    dossier = BASE / nom
    dossier.mkdir(parents=True)
    os.chmod(dossier, 0o755)
    url, commit = depot_essai(dossier, lent)
    for f, v in (("jeton-github", JETON_GH), ("jeton-hcloud", JETON_HC)):
        (dossier / f).write_text(v + "\n")
        os.chmod(dossier / f, 0o600)
    params = {
        "RUN_ID": f"essai-r5-{nom}", "DEPOT_URL": url, "COMMIT_CODE": commit, "BRANCHE_CODE": "main",
        "BRANCHE_SORTIE": f"calcul/essai-r5-{nom}", "PLAFOND_SECONDES": str(plafond),
        "TRAVAIL": str(dossier / "travail"), "DEPOT": str(dossier / "depot"),
        "GH_TOKEN_FILE": str(dossier / "jeton-github"), "HC_TOKEN_FILE": str(dossier / "jeton-hcloud"),
        "CONTRAINTES": "/dev/null", "INSTALLER": "non", "PY_ESSAIS": str(PY), "UTILISATEUR": UTILISATEUR,
        "NPROC": "2", "PAUSE_POUSSEE": "1", "PAUSE_DELETE": "0", "DETRUIRE": "oui", "AUTOTEST_CLOISON": "oui",
        "HCLOUD_API": f"http://127.0.0.1:{port}/v1", "METADONNEES": f"http://127.0.0.1:{port}/hetzner/v1/metadata",
        "METADONNEES_AUTOTEST": f"http://127.0.0.1:{port}/hetzner/v1/metadata",
    }
    params.update({k: str(v) for k, v in extra.items()})
    (dossier / "parametres.env").write_text("".join(f"{k}={v}\n" for k, v in params.items()))
    return dossier, params


def bilan(nom: str, dossier: Path, params: dict, avant: int, rc: int, duree: float) -> dict:
    res = {"scenario": nom, "code_amorce": rc, "duree_s": round(duree, 1), "delete": FausseAPI.supprimes[avant:],
           "processus_essais_restants": len(subprocess.run(["ps", "-u", UTILISATEUR, "-o", "pid="],
                                                           capture_output=True, text=True).stdout.split())}
    for etiquette, branche in (("poussee", params["BRANCHE_SORTIE"]), ("poussee_reduite", params["BRANCHE_SORTIE"] + "-reduit")):
        ref = subprocess.run(["git", "-C", str(dossier / "origin.git"), "rev-parse", "--verify", "-q",
                              f"refs/heads/{branche}"], capture_output=True, text=True)
        res[etiquette] = ref.returncode == 0
        if res[etiquette]:
            extrait = dossier / f"extrait-{etiquette}"
            sh("git", "clone", "-q", "--branch", branche, str(dossier / "origin.git"), str(extrait))
            diag = extrait / "diag" / params["RUN_ID"]
            if not diag.is_dir():              # branche préexistante sans versement (scénario E)
                res[etiquette + "_fichiers"] = []
                continue
            fichiers = sorted(p for p in diag.iterdir() if not p.name.endswith(".sha256"))
            res[etiquette + "_fichiers"] = [p.name for p in fichiers]
            res[etiquette + "_sceaux_ok"] = all(
                (p.parent / (p.name + ".sha256")).read_text().split() ==
                [hashlib.sha256(p.read_bytes()).hexdigest(), p.name] for p in fichiers)
            tout = b"".join(p.read_bytes() for p in diag.rglob("*") if p.is_file())
            res[etiquette + "_jeton_present"] = JETON_GH.encode() in tout or JETON_HC.encode() in tout
            if (diag / "resume-v2.json").exists():
                res[etiquette + "_resume"] = json.loads((diag / "resume-v2.json").read_text())
            if (diag / "environnement-v2.txt").exists():
                res["commit_consigne"] = "commit=" + params["COMMIT_CODE"] in (diag / "environnement-v2.txt").read_text()
    fin = dossier / "travail" / "journal-fin.txt"
    res["journal_fin"] = fin.read_text(errors="replace")[-600:] if fin.exists() else ""
    j = dossier / "travail" / "sortie" / params["RUN_ID"] / "journal-amorce-v2.txt"
    res["journal_amorce"] = j.read_text(errors="replace")[-900:] if j.exists() else ""
    return res


def jouer(nom: str, port: int, **kw) -> dict:
    dossier, params = preparer(nom, port, **kw)
    if nom == "E":   # branche de sortie déjà présente à l'origine : la poussée complète doit être refusée
        sh("git", "-C", str(dossier / "src-depot"), "push", "-q", str(dossier / "origin.git"),
           f"HEAD:refs/heads/{params['BRANCHE_SORTIE']}")
    avant = len(FausseAPI.supprimes)
    t0 = time.monotonic()
    rc = subprocess.run(["bash", str(AMORCE), str(dossier / "parametres.env")], timeout=900).returncode
    return bilan(nom, dossier, params, avant, rc, time.monotonic() - t0)


def jouer_h(port: int) -> dict:
    """Amorce tuée par SIGKILL pendant une étape longue : aucun DELETE par l'amorce, DELETE par le filet."""
    dossier, params = preparer("H", port, ESSAI_PAUSE_ETAPE_PYTHON=60)
    avant = len(FausseAPI.supprimes)
    proc = subprocess.Popen(["bash", str(AMORCE), str(dossier / "parametres.env")], start_new_session=True)
    time.sleep(6)
    os.kill(proc.pid, signal.SIGKILL)          # R10 : par PID
    proc.wait()
    apres_kill = FausseAPI.supprimes[avant:]
    entete = dossier / "entete-filet"
    entete.write_text(f"Authorization: Bearer {JETON_HC}\n")
    os.chmod(entete, 0o600)
    env = dict(os.environ, METADONNEES=params["METADONNEES"], HCLOUD_API=params["HCLOUD_API"], PAUSE_FILET="0")
    rcf = subprocess.run(["bash", str(FILET), str(entete), str(dossier / "journal-filet.txt")], env=env,
                         timeout=120).returncode
    return {"scenario": "H", "delete_par_amorce_apres_kill": apres_kill, "code_filet": rcf,
            "delete_par_filet": FausseAPI.supprimes[avant + len(apres_kill):],
            "journal_filet": (dossier / "journal-filet.txt").read_text()}


def charger_lanceur():
    spec = importlib.util.spec_from_file_location("lanceur_v2", LANCEUR)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sort(fn, *a) -> str:
    try:
        r = fn(*a)
        return f"accepté ({r})"
    except SystemExit as e:
        return f"refusé : {str(e)[:90]}"


def jouer_l() -> dict:
    m = charger_lanceur()
    d = BASE / "L"
    d.mkdir(parents=True)
    tete = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
            "|---|---|---|---|---|---|---|---|\n")
    cas = {
        "valide": "| GO-2026-11-28-90 | 2026-11-28 | calcul | essai | 3 USD | 2026-11-29 | Lazar | R |\n",
        "echu": "| GO-2026-11-28-90 | 2026-11-20 | calcul | essai | 3 USD | 2026-11-21 | Lazar | R |\n",
        "type": "| GO-2026-11-28-90 | 2026-11-28 | décision | essai | 3 USD | 2026-11-29 | Lazar | R |\n",
        "revoque": ("| GO-2026-11-28-90 | 2026-11-28 | calcul | essai | 3 USD | 2026-11-29 | Lazar | R |\n"
                    "| GO-2026-11-28-91 | 2026-11-28 | révocation | révoque GO-2026-11-28-90 | — | 2026-11-28 | Lazar | R |\n"),
    }
    res = {}
    for k, ligne in cas.items():
        f = d / f"go-{k}.md"
        f.write_text(tete + ligne)
        res["go_" + k] = sort(m.exiger_go, "GO-2026-11-28-90", f, date(2026, 11, 28))
    base = dict(depot_url=m.DEPOT_URL, run_id="suite-tests-hetzner-20261128", branche_code="claude/x",
                branche_sortie="calcul/suite-tests-hetzner-20261128", commit="a" * 40, plafond_secondes=28800)
    for k, modif in {"entrees_valides": {}, "depot_public": {"depot_url": "https://github.com/lciric/controle-ia.git"},
                     "nom_invalide": {"run_id": "Suite_Tests"}, "branche_invalide": {"branche_sortie": "a b;rm"},
                     "plafond_trop_long": {"plafond_secondes": 40000}}.items():
        res[k] = sort(m.exiger_entrees, SimpleNamespace(**dict(base, **modif)))
    os.environ.setdefault("CONTROLE_IA_GITHUB_TOKEN_2", JETON_GH)
    os.environ.setdefault("HCLOUD_TOKEN", JETON_HC)
    a = SimpleNamespace(**dict(base, variable_jeton_github="CONTROLE_IA_GITHUB_TOKEN_2",
                               contraintes=str(DEPOT_PROGRAMME / "docs/notes/suite-tests-hetzner-v1/contraintes-pip-v1.txt")))
    donnees = m.donnees_demarrage(a)
    blocs = re.findall(r"echo '([A-Za-z0-9+/=]+)' \| base64 -d \| gunzip", donnees)
    restitues = [gzip.decompress(base64.b64decode(b)) for b in blocs]
    res["donnees_demarrage_octets"] = len(donnees.encode())
    res["donnees_restituent_filet_et_amorce"] = restitues == [FILET.read_bytes(), AMORCE.read_bytes()]
    return res


def main() -> int:
    if os.geteuid() != 0:
        print("essais à jouer en super-utilisateur (chemin du serveur)", file=sys.stderr)
        return 2
    if subprocess.run(["id", "-u", UTILISATEUR], capture_output=True).returncode != 0:
        sh("useradd", "-m", "-s", "/bin/bash", UTILISATEUR)
    if BASE.exists():
        shutil.rmtree(BASE)
    BASE.mkdir(parents=True)
    os.chmod(BASE, 0o755)
    serveur = http.server.ThreadingHTTPServer(("127.0.0.1", 0), FausseAPI)
    port = serveur.server_address[1]
    threading.Thread(target=serveur.serve_forever, daemon=True).start()
    regle = ["OUTPUT", "-p", "tcp", "-d", "127.0.0.1", "--dport", str(port), "-m", "owner", "--uid-owner",
             UTILISATEUR, "-j", "REJECT"]
    sh("iptables", "-I", *regle)
    try:
        r = {}
        r["A"] = jouer("A", port)
        r["B"] = jouer("B", port, SANS_RETRAIT=1)
        r["C"] = jouer("C", port, lent=120, plafond=15)
        r["E"] = jouer("E", port)
        r["F"] = jouer("F", port, plafond=5, ESSAI_PAUSE_ETAPE_PYTHON=60)
        MODE["metadonnees"] = "absente"
        r["G"] = jouer("G", port)
        MODE["metadonnees"] = "ok"
        r["H"] = jouer_h(port)
        MODE["delete"] = "refus"
        r["I"] = jouer("I", port)
        MODE["delete"] = "ok"
    finally:
        sh("iptables", "-D", *regle)          # même spécification exacte : aucune suppression par motif
    r["K"] = jouer("K", port)                 # règle retirée : métadonnées lisibles par les essais
    lecture = subprocess.run(["setpriv", f"--reuid={UTILISATEUR}", f"--regid={UTILISATEUR}", "--init-groups", "--",
                              "cat", str(BASE / "A" / "jeton-github")], capture_output=True, text=True)
    r["D"] = {"lecture_refusee": lecture.returncode != 0 and JETON_GH not in lecture.stdout}
    r["L"] = jouer_l()
    serveur.shutdown()
    ok_del = lambda x, chemin="/v1/servers/424242": x["delete"] == [(chemin, True)]
    a, b, c, e, f, g, i, k, l = (r[x] for x in "ABCEFGIKL")
    verdicts = {
        "A": bool(a["poussee"] and a["poussee_sceaux_ok"] and not a["poussee_jeton_present"] and ok_del(a)
                  and a["poussee_resume"]["phase_parallele"]["failures"] == 1
                  and a["poussee_resume"]["echecs_persistants_en_serie"] == ["tests.test_echec::test_echec"]
                  and a["poussee_resume"]["delai_depasse"] == 0 and a.get("commit_consigne")
                  and "autotest du cloisonnement : conforme" in a["journal_amorce"]
                  and a["processus_essais_restants"] == 0),
        "B": bool(not b["poussee"] and not b["poussee_reduite"] and "ARRÊT SÉCURITÉ" in b["journal_fin"] and ok_del(b)),
        "C": bool(c["poussee"] and c["poussee_resume"]["delai_depasse"] == 1 and c["duree_s"] < 100 and ok_del(c)
                  and c["processus_essais_restants"] == 0 and not c["poussee_jeton_present"]),
        "D": r["D"]["lecture_refusee"],
        "E": bool(e.get("poussee_fichiers") == [] and e["poussee_reduite"] and e["poussee_reduite_sceaux_ok"]
                  and "resume-v2.json" in e["poussee_reduite_fichiers"] and ok_del(e)),
        "F": bool(f["code_amorce"] == 124 and f["duree_s"] < 40 and "journal-pytest-v2.txt" not in f.get("poussee_fichiers", [])
                  and f["poussee"] and f["poussee_resume"]["delai_depasse"] == 1 and ok_del(f)),
        "G": bool(ok_del(g, "/v1/servers/777") and "identifiant retrouvé par le nom : 777" in g["journal_fin"]),
        "H": bool(r["H"]["delete_par_amorce_apres_kill"] == [] and r["H"]["code_filet"] == 0
                  and r["H"]["delete_par_filet"] == [("/v1/servers/424242", True)]),
        "I": bool(len(i["delete"]) == 5 and "DELETE refusé cinq fois" in i["journal_fin"]),
        "K": bool(k["code_amorce"] == 13 and "métadonnées lisibles" in k["journal_amorce"] and ok_del(k)
                  and "journal-pytest-v2.txt" not in k.get("poussee_fichiers", [])),
        "L": bool(l["go_valide"].startswith("accepté (3.0)") and all(l[x].startswith("refusé") for x in
                  ("go_echu", "go_type", "go_revoque", "depot_public", "nom_invalide", "branche_invalide",
                   "plafond_trop_long")) and l["entrees_valides"].startswith("accepté")
                  and l["donnees_restituent_filet_et_amorce"] and l["donnees_demarrage_octets"] < 32 * 1024),
    }
    print(json.dumps({"verdicts": verdicts, "details": r}, ensure_ascii=False, indent=1, default=str))
    return 0 if all(verdicts.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
