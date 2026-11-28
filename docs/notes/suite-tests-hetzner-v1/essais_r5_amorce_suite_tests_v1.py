#!/usr/bin/env python3
"""Essais R5 locaux de scripts/amorce_hetzner_suite_tests_v1.sh (GO-2026-11-28-04).

Chemin du serveur reproduit : amorce lancée en super-utilisateur, essais sous l'utilisateur sans privilège « essais »,
dépôt d'origine nu en file://, faux serveur d'API Hetzner (métadonnées et DELETE) sur 127.0.0.1.
Scénarios :
  A (cas sain)               : un essai réussi, un essai en échec qui imprime le jeton GitHub factice ; attendu :
                               poussée prouvée, jeton absent de la branche, réexécution en série, autodestruction ;
  B (artefact, retrait sauté): même dépôt, retrait des jetons désactivé ; attendu : poussée refusée, autodestruction ;
  C (artefact, minuterie)    : un essai de 120 s sous un plafond de 15 s ; attendu : arrêt du groupe des essais,
                               rapatriement partiel marqué « délai dépassé », autodestruction, aucun processus restant ;
  D (cloisonnement)          : l'utilisateur des essais ne lit pas les fichiers de jetons.
Sortie : un résumé JSON sur la sortie standard ; code 0 si tout passe.
"""
from __future__ import annotations

import hashlib
import http.server
import json
import os
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path

DEPOT_PROGRAMME = Path(__file__).resolve().parents[3]
AMORCE = DEPOT_PROGRAMME / "scripts" / "amorce_hetzner_suite_tests_v1.sh"
PY = DEPOT_PROGRAMME / ".venv" / "bin" / "python3"
BASE = Path("/home/user/essais-r5-suite-tests-v1")
JETON_GH = "ghp_EssaiR5JetonFactice0123456789abcdef"
JETON_HC = "hcEssaiR5JetonFacticeHetzner0123456789"
UTILISATEUR = "essais"


class FausseAPI(http.server.BaseHTTPRequestHandler):
    supprimes: list[tuple[str, bool]] = []

    def do_GET(self):
        self._repondre(200, b"424242") if self.path.endswith("/metadata/instance-id") else self._repondre(404, b"")

    def do_DELETE(self):
        FausseAPI.supprimes.append((self.path, self.headers.get("Authorization", "") == f"Bearer {JETON_HC}"))
        self._repondre(200, b'{"action":{}}')

    def _repondre(self, code, corps):
        self.send_response(code)
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)

    def log_message(self, *a):
        pass


def sh(*cmd, **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def depot_essai(dossier: Path, lent: bool) -> tuple[str, str]:
    src = dossier / "src-depot"
    (src / "tests").mkdir(parents=True)
    (src / "pyproject.toml").write_text('[tool.pytest.ini_options]\ntestpaths = ["tests"]\n')
    (src / "tests" / "test_ok.py").write_text(
        "import pytest\n\n@pytest.mark.parametrize('k', range(6))\ndef test_ok(k):\n    assert k + k == 2 * k\n")
    (src / "tests" / "test_echec.py").write_text(
        f"def test_echec():\n    print('fuite simulee : {JETON_GH}')\n    assert False, '{JETON_GH}'\n")
    if lent:
        (src / "tests" / "test_lent.py").write_text("import time\n\ndef test_lent():\n    time.sleep(120)\n")
    sh("git", "init", "-q", "-b", "main", str(src))
    sh("git", "-C", str(src), "add", "-A")
    sh("git", "-C", str(src), "-c", "user.name=essai", "-c", "user.email=essai@invalid", "commit", "-q", "-m", "essai")
    origine = dossier / "origin.git"
    sh("git", "clone", "-q", "--bare", str(src), str(origine))
    sh("git", "-C", str(origine), "config", "uploadpack.allowReachableSHA1InWant", "true")
    commit = sh("git", "-C", str(src), "rev-parse", "HEAD").stdout.strip()
    return f"file://{origine}", commit


def jouer(nom: str, port: int, lent: bool, plafond: int, sans_retrait: bool) -> dict:
    dossier = BASE / nom
    dossier.mkdir(parents=True)
    os.chmod(dossier, 0o755)
    url, commit = depot_essai(dossier, lent)
    (dossier / "jeton-github").write_text(JETON_GH + "\n")
    (dossier / "jeton-hcloud").write_text(JETON_HC + "\n")
    os.chmod(dossier / "jeton-github", 0o600)
    os.chmod(dossier / "jeton-hcloud", 0o600)
    branche = f"calcul/essai-r5-{nom}"
    params = {
        "RUN_ID": f"essai-r5-{nom}", "DEPOT_URL": url, "COMMIT_CODE": commit, "BRANCHE_CODE": "main",
        "BRANCHE_SORTIE": branche, "PLAFOND_SECONDES": str(plafond), "TRAVAIL": str(dossier / "travail"),
        "GH_TOKEN_FILE": str(dossier / "jeton-github"), "HC_TOKEN_FILE": str(dossier / "jeton-hcloud"),
        "CONTRAINTES": "/dev/null", "INSTALLER": "non", "PY_ESSAIS": str(PY), "UTILISATEUR": UTILISATEUR,
        "NPROC": "2", "PAUSE_POUSSEE": "1", "DETRUIRE": "oui",
        "HCLOUD_API": f"http://127.0.0.1:{port}/v1", "METADONNEES": f"http://127.0.0.1:{port}/hetzner/v1/metadata",
    }
    if sans_retrait:
        params["SANS_RETRAIT"] = "1"
    fichier_params = dossier / "parametres.env"
    fichier_params.write_text("".join(f"{k}={v}\n" for k, v in params.items()))
    avant = len(FausseAPI.supprimes)
    t0 = time.monotonic()
    rc = subprocess.run(["bash", str(AMORCE), str(fichier_params)], timeout=600).returncode
    duree = time.monotonic() - t0
    supprimes = FausseAPI.supprimes[avant:]
    ref = subprocess.run(["git", "-C", str(dossier / "origin.git"), "rev-parse", "--verify", "-q",
                          f"refs/heads/{branche}"], capture_output=True, text=True)
    pousse = ref.returncode == 0
    res = {"scenario": nom, "code_amorce": rc, "duree_s": round(duree, 1), "poussee": pousse,
           "delete": supprimes, "processus_essais_restants": len(subprocess.run(
               ["ps", "-u", UTILISATEUR, "-o", "pid="], capture_output=True, text=True).stdout.split())}
    if pousse:
        extrait = dossier / "extrait"
        sh("git", "clone", "-q", "--branch", branche, str(dossier / "origin.git"), str(extrait))
        diag = extrait / "diag" / params["RUN_ID"]
        fichiers = sorted(p for p in diag.iterdir() if not p.name.endswith(".sha256"))
        sceaux_ok = all(
            (p.parent / (p.name + ".sha256")).read_text().split()[0] == hashlib.sha256(p.read_bytes()).hexdigest()
            and (p.parent / (p.name + ".sha256")).read_text().split()[1] == p.name for p in fichiers)
        tout = b"".join(p.read_bytes() for p in diag.rglob("*") if p.is_file())
        resume = json.loads((diag / "resume-v1.json").read_text())
        res.update({"fichiers": [p.name for p in fichiers], "sceaux_ok": sceaux_ok,
                    "jeton_github_present": JETON_GH.encode() in tout, "jeton_hcloud_present": JETON_HC.encode() in tout,
                    "retrait_visible": b"***JETON-RETIRE***" in tout, "resume": resume})
    fin = dossier / "travail" / "journal-fin.txt"
    res["arret_securite_journalise"] = fin.exists() and "ARRÊT SÉCURITÉ" in fin.read_text(errors="replace")
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
    a = jouer("A", port, lent=False, plafond=600, sans_retrait=False)
    b = jouer("B", port, lent=False, plafond=600, sans_retrait=True)
    c = jouer("C", port, lent=True, plafond=15, sans_retrait=False)
    lecture = subprocess.run(["setpriv", f"--reuid={UTILISATEUR}", f"--regid={UTILISATEUR}", "--init-groups", "--",
                              "cat", str(BASE / "A" / "jeton-github")], capture_output=True, text=True)
    d = {"scenario": "D", "lecture_refusee": lecture.returncode != 0 and JETON_GH not in lecture.stdout}
    serveur.shutdown()
    ok_delete = lambda r: r["delete"] == [("/v1/servers/424242", True)]
    verdicts = {
        "A": bool(a["poussee"] and a["sceaux_ok"] and not a["jeton_github_present"] and not a["jeton_hcloud_present"]
                  and a["retrait_visible"] and ok_delete(a) and a["resume"]["phase_parallele"]["failures"] == 1
                  and a["resume"]["echecs_persistants_en_serie"] == ["tests.test_echec::test_echec"]
                  and a["resume"]["delai_depasse"] == 0 and a["processus_essais_restants"] == 0),
        "B": bool((not b["poussee"]) and b["arret_securite_journalise"] and ok_delete(b)),
        "C": bool(c["poussee"] and c["resume"]["delai_depasse"] == 1 and c["duree_s"] < 100 and ok_delete(c)
                  and c["processus_essais_restants"] == 0 and not c["jeton_github_present"]),
        "D": d["lecture_refusee"],
    }
    print(json.dumps({"verdicts": verdicts, "details": [a, b, c, d]}, ensure_ascii=False, indent=1, default=str))
    return 0 if all(verdicts.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
