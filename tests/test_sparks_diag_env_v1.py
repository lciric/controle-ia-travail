"""Essais du tir de diagnostic d'environnement SPARKS, v1 (hors du code scellé) : socle repris à l'octet de l'amorce v12,
séquence du script d'instance v12 reprise, garde des secrets (cas sain et artefact), relevés sans valeur de clé, refus →
destruction, diagnostic joué en local de bout en bout (dépôt nu local, faux `curl`, poussée vérifiée, puis destruction),
poussée refusée → destruction, gardes du lanceur (fichiers du diagnostic seuls, GO à 40 minutes), commande du tir."""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import time
from datetime import date
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
AMORCE = RACINE / "scripts" / "amorce_diag_env_sparks_v1.sh"
LANCEUR = RACINE / "scripts" / "lancer_diag_env_sparks_v1.sh"
DIAG = RACINE / "scripts" / "diag_env_sparks_v1.py"
V12 = RACINE / "scripts" / "amorce_instance_sparks_exp7_nul_v12.sh"
INSTANCE_V12 = RACINE / "scripts" / "sparks_exp7_nul_instance_v12.sh"
LANCEMENT = "0d163bdcea563a9e001f336c33f36ee6d41c800a"
CODE_SCELLE = "78671d9362c82a3ef02312bcf80c076a19069d42"
ID = "123456"
SECRET = "jeton-tres-secret-0123456789"
GO_TIR = ("| id | a | b | c | d | e | f | g |\n"
          "| GO-2026-11-05-09 | 2026-11-05 | calcul | SPARKS-EXP7-NUL tir réel, codes v10 et suivants | 5 USD | 2026-11-06 | Lazar | mot |\n")


def _git(d, *a):
    return subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True, text=True).stdout.strip()


def _diag():
    import importlib.util
    s = importlib.util.spec_from_file_location("diag_env_sparks_v1", DIAG)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


# --- 1. socle et séquence repris ---------------------------------------------------------------------------------------
def test_socle_repris_a_l_octet_de_l_amorce_v12():
    v12 = V12.read_text(encoding="utf-8").splitlines(keepends=True)
    socle = "".join(v12[73:187]) + "".join(v12[214:220])
    t = AMORCE.read_text(encoding="utf-8")
    assert socle in t and v12[220] in t and v12[222] in t                   # l. 74 à 187, 215 à 219, 221 (AIDE), 223 (borne_t)
    assert '[ "$(date +%s)" -lt "$ECH" ] || detruire "démarrage après l\'échéance' in t
    assert t.index("set -uo pipefail") < t.index("AMORCE V10 DEMARRAGE") < t.index("destruction_immediate()") < t.index("detruire() {") \
        < t.index("refus() {") < t.index("tir de diagnostic d'environnement v1")


def test_sequence_du_script_d_instance_v12_reprise():
    i = INSTANCE_V12.read_text(encoding="utf-8")
    t = AMORCE.read_text(encoding="utf-8")
    for l in ('python3.11 -m venv "$R/venv" 2>/dev/null || python3 -m venv "$R/venv"', 'pip install -q -r requirements-gpu.txt',
              'pip freeze > "$D/pip-freeze.txt"', 'export PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 TOKENIZERS_PARALLELISM=false',
              'python -I -B -m pytest -q -p no:cacheprovider --tb=short -rA $ESSAIS > "$D/tests.txt" 2>&1'):
        assert l in t, l
    assert 'python3.11 -m venv "$TRAVAIL/venv" 2>/dev/null || python3 -m venv "$TRAVAIL/venv"' in i and "pip install -q -r requirements-gpu.txt" in i
    assert "python -I -B -m pytest -q -p no:cacheprovider tests/test_sparks_exp7_nul_v1.py" in i
    assert ("tests/test_sparks_exp7_nul_v1.py tests/test_sparks_exp7_nul_v2.py tests/test_sparks_exp7_nul_v3.py "
            "tests/test_sparks_exp7_nul_v4.py tests/test_sparks_exp7_nul_v12.py") in t
    assert "HF_TOKEN" not in t.split("Variables :")[1].split("\n")[0]


# --- 2. gardes de l'amorce, jouées sur leurs fonctions ----------------------------------------------------------------
def _fonctions(*noms: str) -> str:
    t = AMORCE.read_text(encoding="utf-8")
    out = []
    for n in noms:
        i = t.index(f"{n}() {{")
        out.append(t[i:t.index("\n}\n", i) + 3])
    return "\n".join(out)


def _bash(script: str, env: dict, **kw) -> subprocess.CompletedProcess:
    return subprocess.run(["bash", "-c", script], env={"PATH": "/usr/bin:/bin", **env}, capture_output=True, text=True, timeout=60, **kw)


@pytest.mark.parametrize("contenu, variable, attendu", [
    ("rien de secret ici\n", "GH_TOKEN", 0),                                      # cas sain
    (f"url=https://x-access-token:{SECRET}@github.com/\n", "GH_TOKEN", 1),       # artefact : valeur du jeton
    (f"Bearer {SECRET}\n", "CONTAINER_API_KEY", 1),
    (f"clé {SECRET}\n", "HF_TOKEN", 1),
    ("court\n", "GH_TOKEN", 0),                                                   # valeur trop courte (< 8) : ignorée
])
def test_garde_des_secrets_sain_et_artefacts(tmp_path, contenu, variable, attendu):
    f = tmp_path / "pip.txt"
    f.write_text(contenu)
    (tmp_path / "autre.txt").write_text("ok\n")
    valeur = "court" if contenu == "court\n" else SECRET
    r = _bash(_fonctions("garde_secrets") + f'\ngarde_secrets "{tmp_path}"/*\n', {variable: valeur})
    assert r.returncode == attendu, r.stdout + r.stderr
    assert ("GARDE DES SECRETS : valeur de " + variable in r.stdout) == (attendu == 1) and SECRET not in r.stdout


def test_releves_sans_aucune_valeur_de_cle(tmp_path):
    d = tmp_path / "diag-env"
    d.mkdir()
    r = _bash(_fonctions("relever") + f'\nD="{d}"\nrelever\n', {"GH_TOKEN": SECRET, "CONTAINER_API_KEY": "autre-cle-secrete-xyz",
                                                                   "HOME": str(tmp_path), "VIRTUAL_ENV": "/x"})
    assert r.returncode == 0, r.stderr
    env = (d / "env-sans-secrets.txt").read_text()
    assert "GH_TOKEN\n" in env and "CONTAINER_API_KEY\n" in env and SECRET not in env and "autre-cle-secrete-xyz" not in env and "=" not in env.split("\n", 1)[1]
    for f in ("systeme.txt", "python-version.txt", "nvidia-smi.txt"):
        assert (d / f).exists() and SECRET not in (d / f).read_text(errors="replace"), f
    assert "python3 :" in (d / "python-version.txt").read_text()


# --- 3. l'amorce jouée en local --------------------------------------------------------------------------------------------
def _faux_bin(tmp_path: Path) -> Path:
    b = tmp_path / "faux-bin"
    b.mkdir(exist_ok=True)
    (b / "curl").write_text('#!/bin/bash\necho "curl $*" >> "$FAUX_JOURNAL"\no=""; p=""; for a in "$@"; do [ "$p" = -o ] && o="$a"; p="$a"; done\n'
                            '[ -n "$o" ] && printf %s \'{"success": true}\' > "$o"\nprintf %s "${FAUX_HTTP:-200}"\n')
    (b / "curl").chmod(0o755)
    return b


def _depot_nu(tmp_path: Path, refuse_poussee: bool = False) -> Path:
    """Dépôt nu local qui emprunte les objets du dépôt de travail (le commit de lancement y est)."""
    commun = Path(_git(RACINE, "rev-parse", "--git-common-dir"))
    commun = commun if commun.is_absolute() else RACINE / commun
    b = tmp_path / "depot.git"
    _git(tmp_path, "init", "-q", "--bare", str(b))
    (b / "objects" / "info" / "alternates").write_text(str(commun / "objects") + "\n")
    if (commun / "shallow").exists():
        shutil.copy(commun / "shallow", b / "shallow")
    _git(b, "config", "uploadpack.allowFilter", "true")
    _git(b, "config", "uploadpack.allowAnySHA1InWant", "true")
    _git(b, "update-ref", "refs/heads/lancement", LANCEMENT)
    if refuse_poussee:
        h = b / "hooks" / "pre-receive"
        h.write_text("#!/bin/bash\necho 'poussée refusée (essai)' >&2\nexit 1\n")
        h.chmod(0o755)
    return b


def _env(tmp_path: Path, depot_url: str, **kw) -> dict:
    r_ = tmp_path / "racine"
    r_.mkdir(exist_ok=True)
    import sys
    venv = Path(sys.prefix)                      # le venv qui joue ces essais, réutilisé (VENV_EXISTANT)
    e = {"PATH": f"{_faux_bin(tmp_path)}:{venv / 'bin'}:/usr/bin:/bin", "HOME": str(tmp_path),
         "FAUX_JOURNAL": str(tmp_path / "faux.log"), "CONTAINER_ID": ID, "CONTAINER_API_KEY": "cle-conteneur-factice-123",
         "MINUTERIE_PAS_S": "1", "MINUTERIE_REESSAI_S": "1", "MINUTERIE_MARGE_S": "4", "RACINE_AMORCE": str(r_),
         "DEPOT_URL": depot_url, "COMMIT": LANCEMENT, "GH_TOKEN": SECRET, "ECHEANCE_UTC_S": str(int(time.time()) + 3600),
         "VENV_EXISTANT": str(venv),
         "DIAG_FICHIERS_ESSAIS": "tests/test_sparks_exp7_nul_v1.py -k etiquette", "GIT_CONFIG_GLOBAL": "/dev/null"}
    e.update({k: str(v) for k, v in kw.items()})
    return e


def _amorce(tmp_path: Path, env: dict, timeout: int = 600):
    r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=timeout)
    r_ = Path(env["RACINE_AMORCE"])
    log = (r_ / "sparks-v5-minuterie.log").read_text() if (r_ / "sparks-v5-minuterie.log").exists() else ""
    return r.returncode, r.stdout + r.stderr, log, r_


@pytest.fixture(scope="module")
def venv_present():
    import sys
    if not (Path(sys.prefix) / "bin" / "activate").exists():
        pytest.skip("aucun venv à réutiliser (VENV_EXISTANT)")


def test_refus_avant_le_clone_detruit_l_instance(tmp_path):
    code, out, log, _ = _amorce(tmp_path, _env(tmp_path, f"file://{tmp_path}/absent.git", AMORCE_T_GIT_S=20), timeout=120)
    assert code == 2 and "clonage impossible" in out and "refus avant l'ordre consommé : destruction de l'instance" in out, out
    assert "DELETE instance 123456" in log and "détruite" in log and SECRET not in out + log


def test_diagnostic_de_bout_en_bout_local_poussee_verifiee_puis_destruction(tmp_path, venv_present):
    b = _depot_nu(tmp_path)
    code, out, log, r_ = _amorce(tmp_path, _env(tmp_path, f"file://{b}"))
    assert "AMORCE V10 DEMARRAGE 1" in out and "séquence du script d'instance v12" in out, out[-3000:]
    assert re.search(r"essais : code 0 : .*passed", out) and "poussée vérifiée sur essai/sparks-diag-env-v1-123456" in out, out[-3000:]
    assert "destruction demandée (fin du diagnostic (essais : code 0), poussée vérifiée)" in out and code == 0
    assert "DELETE instance 123456" in log and "détruite" in log
    tete = _git(b, "rev-parse", f"refs/heads/essai/sparks-diag-env-v1-{ID}")
    fichiers = _git(b, "ls-tree", "-r", "--name-only", tete).splitlines()
    for f in ("tests.txt", "tests-code.txt", "pip.txt", "pip-freeze.txt", "python-version.txt", "nvidia-smi.txt", "env-sans-secrets.txt",
              "systeme.txt", "torch.txt"):
        assert f"diag-env/{f}" in fichiers, f
        contenu = subprocess.run(["git", "-C", str(b), "show", f"{tete}:diag-env/{f}"], capture_output=True, text=True).stdout
        assert SECRET not in contenu and "cle-conteneur-factice-123" not in contenu, f      # garde des secrets, de bout en bout
    assert _git(b, "show", f"{tete}:diag-env/tests-code.txt").strip() == "0"
    assert "passed" in _git(b, "show", f"{tete}:diag-env/tests.txt") and "PASSED" in _git(b, "show", f"{tete}:diag-env/tests.txt")   # -rA
    assert "venv existant" in _git(b, "show", f"{tete}:diag-env/pip.txt")
    assert _git(b, "rev-parse", f"{tete}^") == LANCEMENT                                  # relevés posés sur le commit de lancement


def test_poussee_refusee_destruction_quand_meme(tmp_path, venv_present):
    b = _depot_nu(tmp_path, refuse_poussee=True)
    code, out, log, _ = _amorce(tmp_path, _env(tmp_path, f"file://{b}"))
    assert "POUSSÉE NON VÉRIFIÉE sur essai/sparks-diag-env-v1-123456" in out and "relevés perdus" in out, out[-2000:]
    assert "DELETE instance 123456" in log and code == 0
    assert subprocess.run(["git", "-C", str(b), "rev-parse", "--verify", f"refs/heads/essai/sparks-diag-env-v1-{ID}"], capture_output=True).returncode != 0


# --- 4. gardes du lanceur --------------------------------------------------------------------------------------------------
def test_liste_du_diagnostic_hors_du_code_scelle():
    d = _diag()
    tete = _git(RACINE, "rev-parse", "HEAD")
    if tete == CODE_SCELLE or _git(RACINE, "status", "--porcelain"):
        pytest.skip("commit du diagnostic non encore écrit")
    assert d.verifier_liste(RACINE, tete) == 8
    with pytest.raises(d.GardeTir, match="hors liste"):
        d.verifier_liste(RACINE, LANCEMENT)                                      # le commit de lancement ajoute l'addendum : refus
    with pytest.raises(d.GardeTir, match="ne descend pas"):
        d.verifier_liste(RACINE, "4fd104072bcdf22bb0f5eb1daffca295858f0ac6")


def test_go_du_diagnostic_quarante_minutes(tmp_path):
    d = _diag()
    p = tmp_path / "go.md"
    p.write_text(GO_TIR)
    r = d.preparer(p, "GO-2026-11-05-09", 0.06, 0.004, date(2026, 11, 5), maintenant_s=1000)
    assert r["echeance_utc_s"] == 1000 + 40 * 60 and r["devis_usd"] == pytest.approx(0.06 * 65 / 60 + 0.004 * 100 / 60, abs=1e-4)
    p.write_text(GO_TIR.replace("SPARKS-EXP7-NUL tir réel, codes v10 et suivants", "sonde v10 d'A1-v3"))
    with pytest.raises(d.GardeTir, match="« SPARKS » et « tir » exigés"):
        d.preparer(p, "GO-2026-11-05-09", 0.06, 0.004, date(2026, 11, 5))
    p.write_text(GO_TIR)
    with pytest.raises(d.GardeTir, match="devis"):
        d.preparer(p, "GO-2026-11-05-09", 5.0, 0.004, date(2026, 11, 5))
    with pytest.raises(d.GardeTir, match="validité"):
        d.preparer(p, "GO-2026-11-05-09", 0.06, 0.004, date(2026, 11, 9))


def _lanceur(tmp_path, *args, **env):
    e = {"PATH": "/usr/bin:/bin", "HOME": str(tmp_path), "SPARKS_ETAT_DIR": str(tmp_path / "etat")}
    e.update(env)
    return subprocess.run(["bash", str(LANCEUR), *args], env=e, capture_output=True, text=True, timeout=120)


def test_lanceur_commande_du_tir_de_diagnostic(tmp_path):
    tete = _git(RACINE, "rev-parse", "HEAD")
    if tete == CODE_SCELLE or _git(RACINE, "status", "--porcelain"):
        pytest.skip("commit du diagnostic non encore écrit")
    f = tmp_path / "brut.json"
    f.write_text(json.dumps([{"id": 9, "resource_type": "gpu", "num_gpus": 1, "dph_total": 0.06, "storage_cost": 0.15}]))
    assert _lanceur(tmp_path, "offres", str(f)).returncode == 0                   # délégué au lanceur v12
    reg = tmp_path / "go.md"
    reg.write_text(GO_TIR)
    r = _lanceur(tmp_path, "tir", tete, "GO-2026-11-05-09", "1", SPARKS_REGISTRE_GO=str(reg), SPARKS_DATE_TIR="2026-11-05")
    assert r.returncode == 0, r.stderr
    t = r.stdout
    assert "DIAGNOSTIC HORS DU CODE SCELLÉ : 8 fichiers neufs" in t and "DIAGNOSTIC CONFORME : offre 9 (rang 1)" in t and "MINUTES=40" in t
    assert "vastai create instance 9 --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 20 --label sparks-diag-env-v1-" in t
    assert f"-e COMMIT={LANCEMENT} -e ECHEANCE_UTC_S=" in t and "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" in t and "HF_TOKEN" not in t
    assert f'git show "{tete}:scripts/amorce_diag_env_sparks_v1.sh"' in t and "GO_ID=GO-2026-11-05-09 timeout -k 10 300" in t
    assert "apres-creation" in t and "journal-amorce" in t and "vastai show instances --raw" in t and "'$ID' absente" in t
    r2 = _lanceur(tmp_path, "tir", tete, "GO-2026-11-05-09", "1", SPARKS_REGISTRE_GO=str(reg), SPARKS_DATE_TIR="2026-11-09")
    assert r2.returncode == 2 and "validité" in r2.stderr
    r3 = _lanceur(tmp_path, "tir", LANCEMENT, "GO-2026-11-05-09", "1", SPARKS_REGISTRE_GO=str(reg), SPARKS_DATE_TIR="2026-11-05")
    assert r3.returncode == 2 and "hors liste" in r3.stderr                        # un commit qui n'est pas le diagnostic : refus


def test_lanceur_delegue_les_autres_modes_au_v12(tmp_path):
    f = tmp_path / "i.json"
    f.write_text('[{"id": 7, "actual_status": "exited", "cur_state": "stopped"}]')
    r = _lanceur(tmp_path, "inventaire", str(f), "7", "exited")
    assert r.returncode == 0 and "état exited (cur_state stopped)" in r.stdout and not f.exists()
    r = _lanceur(tmp_path, "destruction", "7")
    assert "vastai destroy instance 7 -y" in r.stdout
