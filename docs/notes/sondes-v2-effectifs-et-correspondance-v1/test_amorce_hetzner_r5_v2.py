"""Essais à blanc R5 locaux de amorce-hetzner-sondes-v2-ccx63-v2.sh.

Prouve sur un dépôt git bare local `/tmp/test-hetzner-r5/` avec un faux serveur API Hetzner local :
  (a) Scénario A (petites sorties <= seuil) et Scénario B (sorties > seuil découpées par split) :
      100 % des fichiers *.sha256 dans le dépôt poussé passent `sha256sum -c`, et l'archive découpée
      se réassemble à l'octet contre `journaux-gels-complet.tar.gz.manifeste.sha256.txt`.
  (b) Sécurité : 0 fuite du faux jeton `ghp_TESTSECRET123` (ni du faux jeton Hetzner) dans `$LOG`
      poussé, dans tous les fichiers du commit poussé et dans `.git/config` ; rejet immédiat si
      un jeton est présent dans `REPO_URL`.
  (c) Minuterie interne R10 : tue un processus de calcul dépassant le délai (`WATCHDOG_SECONDES=3`),
      rapatrie les sorties partielles (`partiel-plafond-r10`) et déclenche `DELETE /v1/servers/<ID>`.

Nettoie intégralement `/tmp/test-hetzner-r5/` à la fin.
"""
from __future__ import annotations

import base64
import hashlib
import http.server
import os
import shutil
import stat
import subprocess
import sys
import threading
import time
from pathlib import Path

SCRIPT_AMORCE = Path(__file__).resolve().parent / "amorce-hetzner-sondes-v2-ccx63-v2.sh"
TEST_ROOT = Path("/tmp/test-hetzner-r5")
FAKE_GH_TOKEN = "ghp_TESTSECRET123"
FAKE_HCLOUD_TOKEN = "hc_TESTHCLOUD_987654"
FAKE_SERVER_ID = "99887766"
ENTROPIE = "305159624078239919914131004197200342142"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_cmd(cmd: list[str], cwd: Path | None = None, env: dict[str, str] | None = None, check: bool = True):
    res = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    if check and res.returncode != 0:
        raise AssertionError(f"Commande échouée ({res.returncode}): {cmd}\nSTDOUT:\n{res.stdout}\nSTDERR:\n{res.stderr}")
    return res


class FakeHetznerServer:
    def __init__(self, expected_token: str, server_id: str) -> None:
        self.expected_token = expected_token
        self.server_id = server_id
        self.deleted_ids: list[str] = []
        self.auth_errors: list[str] = []
        outer = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def log_message(self, format, *args):  # noqa: A002
                return

            def do_GET(self):
                if self.path == "/hetzner/v1/metadata/instance-id":
                    body = outer.server_id.encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                else:
                    self.send_response(404)
                    self.end_headers()

            def do_DELETE(self):
                auth = self.headers.get("Authorization", "")
                if auth != f"Bearer {outer.expected_token}":
                    outer.auth_errors.append(auth)
                    self.send_response(401)
                    self.end_headers()
                    return
                prefix = "/v1/servers/"
                if self.path.startswith(prefix):
                    sid = self.path[len(prefix):]
                    outer.deleted_ids.append(sid)
                    body = b'{"action":{"status":"success"}}'
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                else:
                    self.send_response(404)
                    self.end_headers()

        self.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.port = self.httpd.server_address[1]
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    def close(self) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()


def setup_fake_bare_repo(root: Path) -> tuple[Path, str, str, str]:
    """Crée /tmp/test-hetzner-r5/origin.git avec branches main et sondes-v2/code-v2."""
    bare = root / "origin.git"
    seed = root / "seed-repo"
    run_cmd(["git", "init", "--bare", str(bare)])
    run_cmd(["git", "init", str(seed)])
    run_cmd(["git", "-C", str(seed), "config", "user.name", "test-r5"])
    run_cmd(["git", "-C", str(seed), "config", "user.email", "test@r5.local"])

    # Branche main : note des effectifs + .sha256
    run_cmd(["git", "-C", str(seed), "checkout", "-B", "main"])
    note_dir = seed / "docs/notes/sondes-v2-effectifs-et-correspondance-v1"
    note_dir.mkdir(parents=True, exist_ok=True)
    note_path = note_dir / "note-des-effectifs-sondes-v2-v1.md"
    note_path.write_text("# Note effectifs factice R5\n", encoding="utf-8")
    sha_note = sha256_file(note_path)
    (note_dir / "note-des-effectifs-sondes-v2-v1.md.sha256").write_text(
        f"{sha_note}  note-des-effectifs-sondes-v2-v1.md\n", encoding="utf-8"
    )
    run_cmd(["git", "-C", str(seed), "add", "-A"])
    run_cmd(["git", "-C", str(seed), "commit", "-m", "main: note effectifs factice"])
    run_cmd(["git", "-C", str(seed), "push", str(bare), "main:refs/heads/main"])

    # Branche sondes-v2/code-v2 : verites_mondes_plantes_v4.json
    run_cmd(["git", "-C", str(seed), "checkout", "-B", "sondes-v2/code-v2"])
    v_dir = seed / "src/controle_ia/sondes_v2"
    v_dir.mkdir(parents=True, exist_ok=True)
    verites_path = v_dir / "verites_mondes_plantes_v4.json"
    verites_path.write_text('{"format":"verites-v4-test"}\n', encoding="utf-8")
    sha_verites = sha256_file(verites_path)
    run_cmd(["git", "-C", str(seed), "add", "-A"])
    run_cmd(["git", "-C", str(seed), "commit", "-m", "code-v2: verites factice"])
    commit_code = run_cmd(["git", "-C", str(seed), "rev-parse", "HEAD"]).stdout.strip()
    run_cmd(["git", "-C", str(seed), "push", str(bare), "sondes-v2/code-v2:refs/heads/sondes-v2/code-v2"])

    shutil.rmtree(seed)
    return bare, commit_code, sha_verites, sha_note


def write_fake_runner(path: Path, *, mode_complet_behavior: str) -> None:
    """Écrit un faux runner qui simule programme_monde_plante_v4 (+ fuite volontaire de jetons sur stderr)."""
    script = f"""#!/usr/bin/env python3
import base64, hashlib, json, os, sys, time
from pathlib import Path

mode = sys.argv[1]
outdir = Path(sys.argv[2])
entropie = sys.argv[3]
outdir.mkdir(parents=True, exist_ok=True)

def write_with_sha(p: Path, data: bytes) -> None:
    p.write_bytes(data)
    h = hashlib.sha256(data).hexdigest()
    p.with_name(p.name + ".sha256").write_text(f"{{h}}  {{p.name}}\\n", encoding="utf-8")

# Simuler une ligne d'erreur stderr contenant les faux jetons pour tester le filtre sed anti-fuite
print("SIMULATION ERREUR HTTP: https://x-access-token:{FAKE_GH_TOKEN}@github.com/lciric/controle-ia-travail.git", file=sys.stderr, flush=True)
print("SIMULATION HEADER HCLOUD: {FAKE_HCLOUD_TOKEN}", file=sys.stderr, flush=True)

if mode == "complet" and {mode_complet_behavior!r} == "sleep":
    print("SIMULATION CALCUL LONG (60s) POUR DECLENCHER WATCHDOG R10", flush=True)
    time.sleep(60)
    sys.exit(0)

# Rapport de plage + synthèse fusionnée
write_with_sha(
    outdir / f"rapport-monde-plante-v4-{{mode}}-{{entropie}}-r0-10.json",
    json.dumps({{"mode": mode, "plage": [0, 10]}}).encode("utf-8"),
)
write_with_sha(
    outdir / f"synthese-fusionnee-monde-plante-v4-{{mode}}-{{entropie}}.json",
    json.dumps({{"mode": mode, "synthese": True}}).encode("utf-8"),
)

if mode == "complet":
    if {mode_complet_behavior!r} == "small":
        content = b'{{"gel": 1, "note": "petit"}}\\n' * 20
    elif {mode_complet_behavior!r} == "large":
        # Données pseudo-aléatoires incompressibles (~140 Ko) -> dépasse SEUIL_ARCHIVE_OCTETS=65536
        rng = os.urandom(105000)
        b64 = base64.b64encode(rng).decode("ascii")
        content = (json.dumps({{"gel": 1, "bloc": b64}}) + "\\n").encode("utf-8")
    else:
        raise SystemExit("comportement inconnu")
    write_with_sha(outdir / "journal-gels-r0-10.jsonl", content)
"""
    path.write_text(script, encoding="utf-8")
    path.chmod(0o700)


def verify_pushed_branch(bare: Path, check_dir: Path, branche: str) -> Path:
    if check_dir.exists():
        shutil.rmtree(check_dir)
    run_cmd(["git", "clone", "--branch", branche, str(bare), str(check_dir)])
    ep_dir = check_dir / "epreuve-plantee-v4"
    assert ep_dir.is_dir(), "Dossier epreuve-plantee-v4 absent du dépôt poussé"

    # (a) 100 % des *.sha256 doivent passer sha256sum -c dans leur répertoire
    sha_files = sorted(ep_dir.rglob("*.sha256"))
    assert len(sha_files) > 0, "Aucun fichier .sha256 trouvé dans epreuve-plantee-v4"
    for sf in sha_files:
        run_cmd(["sha256sum", "-c", sf.name], cwd=sf.parent)

    # (b) 0 fuite des faux jetons dans TOUS les fichiers du dépôt poussé
    for f in ep_dir.rglob("*"):
        if f.is_file():
            raw = f.read_bytes()
            assert FAKE_GH_TOKEN.encode() not in raw, f"FUITE GH_TOKEN dans {f}"
            assert FAKE_HCLOUD_TOKEN.encode() not in raw, f"FUITE HCLOUD_TOKEN dans {f}"

    log_txt = (ep_dir / "journal-execution.log").read_text(encoding="utf-8")
    assert "[MASQUE_GH]" in log_txt, "Le filtre de masquage GH n'a pas été observé dans journal-execution.log"
    assert "[MASQUE_HCLOUD]" in log_txt, "Le filtre de masquage HCLOUD n'a pas été observé dans journal-execution.log"
    return ep_dir


def base_env(
    run_dir: Path,
    bare: Path,
    commit_code: str,
    sha_verites: str,
    sha_note: str,
    port: int,
    runner: Path,
    gh_tok_file: Path,
    hc_tok_file: Path,
) -> dict[str, str]:
    env = os.environ.copy()
    env.update({
        "PYTHONDONTWRITEBYTECODE": "1",
        "MODE_RUN": "complet_et_etalon",
        "COMMIT_CODE": commit_code,
        "ENTROPIE": ENTROPIE,
        "SHA_VERITES": sha_verites,
        "SHA_NOTE": sha_note,
        "BRANCHE_CODE": "sondes-v2/code-v2",
        "BRANCHE_SORTIE": "calcul/sondes-v2-epreuve-plantee-v4",
        "REPO_URL": str(bare),
        "HCLOUD_API": f"http://127.0.0.1:{port}/v1",
        "METADATA_URL": f"http://127.0.0.1:{port}/hetzner/v1/metadata/instance-id",
        "HCLOUD_TOKEN_FILE": str(hc_tok_file),
        "GH_TOKEN_FILE": str(gh_tok_file),
        "WORK": str(run_dir / "work"),
        "ENTREE": str(run_dir / "entree"),
        "SORTIE": str(run_dir / "sortie"),
        "LOG": str(run_dir / "epreuve.log"),
        "SKIP_ENV_INSTALL": "1",
        "PY_BIN": sys.executable,
        "SIMULER_MODE_CMD": str(runner),
        "N_WORKERS": "2",
    })
    return env


def main() -> int:
    # Vérification syntaxique bash -n préalable
    run_cmd(["bash", "-n", str(SCRIPT_AMORCE)])

    if TEST_ROOT.exists():
        shutil.rmtree(TEST_ROOT)
    TEST_ROOT.mkdir(parents=True, exist_ok=True)
    server = FakeHetznerServer(FAKE_HCLOUD_TOKEN, FAKE_SERVER_ID)

    try:
        bare, commit_code, sha_verites, sha_note = setup_fake_bare_repo(TEST_ROOT)
        gh_tok_file = TEST_ROOT / ".gh_token"
        hc_tok_file = TEST_ROOT / ".hcloud_token"
        gh_tok_file.write_text(FAKE_GH_TOKEN + "\n", encoding="utf-8")
        hc_tok_file.write_text(FAKE_HCLOUD_TOKEN + "\n", encoding="utf-8")
        gh_tok_file.chmod(0o600)
        hc_tok_file.chmod(0o600)

        # --- SCÉNARIO A : petites sorties (archive <= seuil) + filtre anti-fuite + DELETE ---
        server.deleted_ids.clear()
        run_a = TEST_ROOT / "run-a"
        runner_a = TEST_ROOT / "runner_a.py"
        write_fake_runner(runner_a, mode_complet_behavior="small")
        env_a = base_env(run_a, bare, commit_code, sha_verites, sha_note, server.port, runner_a, gh_tok_file, hc_tok_file)
        env_a["WATCHDOG_SECONDES"] = "60"
        res_a = run_cmd(["bash", str(SCRIPT_AMORCE)], env=env_a)
        assert "RAPATRIEMENT PROUVÉ" in res_a.stdout
        assert server.deleted_ids == [FAKE_SERVER_ID], f"DELETE non reçu en Scénario A: {server.deleted_ids}"
        assert not server.auth_errors, server.auth_errors
        git_cfg_a = (run_a / "work/repo/.git/config").read_text(encoding="utf-8")
        assert FAKE_GH_TOKEN not in git_cfg_a, "Fuite GH_TOKEN dans .git/config"
        ep_a = verify_pushed_branch(bare, TEST_ROOT / "verify-a", "calcul/sondes-v2-epreuve-plantee-v4")
        assert (ep_a / "complet/journaux-gels-complet.tar.gz").is_file()
        assert (ep_a / "complet/journaux-gels-complet.tar.gz.sha256").is_file()
        assert (ep_a / "complet/journaux-gels.manifeste.sha256.txt").is_file()
        assert not (ep_a / "complet/journaux-gels.sha256").exists()
        print("SCÉNARIO A (petites sorties + anti-fuite + DELETE) : OK")

        # --- SCÉNARIO B : sorties simulées > 90 Mo découpées (split) + réassemblage ---
        server.deleted_ids.clear()
        run_b = TEST_ROOT / "run-b"
        runner_b = TEST_ROOT / "runner_b.py"
        write_fake_runner(runner_b, mode_complet_behavior="large")
        env_b = base_env(run_b, bare, commit_code, sha_verites, sha_note, server.port, runner_b, gh_tok_file, hc_tok_file)
        env_b["WATCHDOG_SECONDES"] = "60"
        env_b["SEUIL_ARCHIVE_OCTETS"] = "65536"
        env_b["TAILLE_MORCEAU"] = "32k"
        res_b = run_cmd(["bash", str(SCRIPT_AMORCE)], env=env_b)
        assert "RAPATRIEMENT PROUVÉ" in res_b.stdout
        assert server.deleted_ids == [FAKE_SERVER_ID], f"DELETE non reçu en Scénario B: {server.deleted_ids}"
        ep_b = verify_pushed_branch(bare, TEST_ROOT / "verify-b", "calcul/sondes-v2-epreuve-plantee-v4")
        comp_b = ep_b / "complet"
        assert not (comp_b / "journaux-gels-complet.tar.gz").exists(), "L'archive entière ne doit pas être copiée en branche split"
        assert not (comp_b / "journaux-gels-complet.tar.gz.sha256").exists(), "Aucun .sha256 orphelin autorisé en branche split"
        parts = sorted(comp_b.glob("journaux-gels-complet.tar.gz.part.*"))
        assert len(parts) >= 3, f"Au moins 3 morceaux attendus, reçu {len(parts)}"
        assert (comp_b / "journaux-gels-complet.parts.sha256").is_file()
        assert (comp_b / "journaux-gels-complet.tar.gz.manifeste.sha256.txt").is_file()
        # Prouver le réassemblage exact contre le manifeste
        reassembled = TEST_ROOT / "verify-b/journaux-gels-complet.tar.gz"
        with reassembled.open("wb") as out_f:
            for p in parts:
                out_f.write(p.read_bytes())
        expected_line = (comp_b / "journaux-gels-complet.tar.gz.manifeste.sha256.txt").read_text(encoding="utf-8").strip()
        expected_sha = expected_line.split()[0]
        assert sha256_file(reassembled) == expected_sha, "Réassemblage des morceaux != empreinte du manifeste"
        print(f"SCÉNARIO B (archive découpée en {len(parts)} morceaux + sha256sum -c 100 % + réassemblage exact) : OK")

        # --- SCÉNARIO C : minuterie interne R10 (WATCHDOG_SECONDES=3) ---
        server.deleted_ids.clear()
        run_c = TEST_ROOT / "run-c"
        runner_c = TEST_ROOT / "runner_c.py"
        write_fake_runner(runner_c, mode_complet_behavior="sleep")
        env_c = base_env(run_c, bare, commit_code, sha_verites, sha_note, server.port, runner_c, gh_tok_file, hc_tok_file)
        env_c["WATCHDOG_SECONDES"] = "3"
        t0 = time.monotonic()
        res_c = run_cmd(["bash", str(SCRIPT_AMORCE)], env=env_c, check=False)
        elapsed = time.monotonic() - t0
        assert res_c.returncode == 124, f"Code de sortie 124 attendu sur timeout R10, reçu {res_c.returncode}\nSTDOUT:\n{res_c.stdout}\nSTDERR:\n{res_c.stderr}"
        assert elapsed < 20.0, f"La minuterie R10 a mis trop longtemps ({elapsed:.1f}s)"
        assert server.deleted_ids == [FAKE_SERVER_ID], f"DELETE non reçu sur timeout R10: {server.deleted_ids}"
        ep_c = verify_pushed_branch(bare, TEST_ROOT / "verify-c", "calcul/sondes-v2-epreuve-plantee-v4")
        log_c = (ep_c / "journal-execution.log").read_text(encoding="utf-8")
        assert "PLAFOND INTERNE R10 (3s) ATTEINT" in log_c
        assert (ep_c / f"etalon/synthese-fusionnee-monde-plante-v4-etalon-{ENTROPIE}.json").is_file()
        print(f"SCÉNARIO C (minuterie interne R10 en {elapsed:.1f}s -> rc=124 + rapatriement partiel + DELETE {FAKE_SERVER_ID}) : OK")

        # --- SCÉNARIO D : rejet de REPO_URL contenant un jeton ---
        env_d = base_env(TEST_ROOT / "run-d", bare, commit_code, sha_verites, sha_note, server.port, runner_a, gh_tok_file, hc_tok_file)
        env_d["REPO_URL"] = f"https://x-access-token:{FAKE_GH_TOKEN}@github.com/lciric/controle-ia-travail.git"
        res_d = run_cmd(["bash", str(SCRIPT_AMORCE)], env=env_d, check=False)
        assert res_d.returncode == 1 and "ARRÊT SÉCURITÉ" in res_d.stderr
        print("SCÉNARIO D (rejet de REPO_URL contenant un jeton) : OK")

        print("TOUS LES ESSAIS R5 DE amorce-hetzner-sondes-v2-ccx63-v2.sh : SUCCÈS COMPLET (4/4)")
        return 0
    finally:
        server.close()
        if TEST_ROOT.exists():
            shutil.rmtree(TEST_ROOT)


if __name__ == "__main__":
    sys.exit(main())
