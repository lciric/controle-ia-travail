"""Essais de SPARKS-EXP7-NUL, v4 (contre-lecture du delta v3) : `timeout` sur chaque étape de l'amorce (git bloqué :
artefact), attente du principal sur `$!` jouée dans un espace de processus à part (`unshare -pf`), branche des ordres
hors `calcul/` liée au commit, clé `instance`, `deja_usd` qui ne baisse jamais, borne propre de la machine, consignation
contrôlée, branches des sorties liées au commit et à l'ordre avec préfixe réglable, lanceur (`timeout`, environnement
nettoyé avec les variables du mandataire, sortie jamais affichée, marqueur de création incertaine, certificat = non
parvenu, `--label`). `curl`, `vastai` et `git` bloqué simulés : aucun réseau. Cas sain et artefact pour chaque garde (R5)."""
from __future__ import annotations

import json
import os
import re
import shutil
import signal
import subprocess
import time
from pathlib import Path

import pytest

from controle_ia.sparks_exp7_nul_v4 import plan, redemarrage

RACINE = Path(__file__).resolve().parents[1]
AMORCE = RACINE / "scripts" / "amorce_instance_sparks_exp7_nul_v4.sh"
LANCEUR = RACINE / "scripts" / "lancer_sparks_exp7_nul_v4.sh"
L_BASE = "| GO-2026-11-04-04 | 2026-11-04 | calcul | SPARKS-EXP7-NUL, variante carte | 25 USD | 2026-11-18 | Lazar | mot |"
L_EXT = "| GO-2026-11-04-04 | 2026-11-04 | calcul | extension : SPARKS-EXP7-NUL, addendum | 40 USD | 2026-11-18 | Lazar | mot |"
UNSHARE = shutil.which("unshare") is not None and subprocess.run(["unshare", "-pf", "--mount-proc", "true"],
                                                                 capture_output=True).returncode == 0
espace_processus = pytest.mark.skipif(not UNSHARE, reason="unshare -pf indisponible")
ID = "123456"


# --- 1. ordres : instance, deja_usd, consignation, borne de la machine ------------------------------------------------
def _ordre(d: Path, n: int, **o) -> Path:
    p = d / f"ordre-{n:03d}.json"
    p.write_text(json.dumps({"numero": n, **o}), encoding="utf-8")
    return p


def test_ordre_exige_l_instance_de_cette_machine(tmp_path):
    p = _ordre(tmp_path, 1, instance=ID, phase="fin", deja_usd=1)
    assert redemarrage.lire_ordre(p, instance=ID)["instance"] == ID
    with pytest.raises(redemarrage.GardeOrdre, match="cette machine"):
        redemarrage.lire_ordre(p, instance="999")
    with pytest.raises(redemarrage.GardeOrdre, match="chiffres"):
        redemarrage.lire_ordre(_ordre(tmp_path, 3, instance="12a", phase="fin", deja_usd=1))
    for i in (None, 123456, "12a"):
        q = _ordre(tmp_path, 2, phase="fin", deja_usd=1, **({} if i is None else {"instance": i}))
        with pytest.raises(redemarrage.GardeOrdre):
            redemarrage.lire_ordre(q, instance=ID)


def test_deja_usd_ne_baisse_jamais_et_consignation(tmp_path):
    f = tmp_path / "faits.txt"
    redemarrage.marquer_fait(f, 3, 12.5)
    assert redemarrage.faits(f) == [(3, 12.5)]
    with pytest.raises(redemarrage.GardeOrdre, match="plus bas"):
        redemarrage.exiger_nouveau({"numero": 4, "deja_usd": 12.0}, f)
    redemarrage.exiger_nouveau({"numero": 4, "deja_usd": 12.5}, f)
    with pytest.raises(redemarrage.GardeOrdre, match="déjà"):
        redemarrage.exiger_nouveau({"numero": 3, "deja_usd": 20}, f)
    d = tmp_path / "dossier"
    d.mkdir()
    assert redemarrage.main(["fait", str(d), "5", "13"]) == 2              # consignation impossible : code 2


def test_borne_propre_de_la_machine(tmp_path):
    reg = tmp_path / "demarrages.txt"
    assert redemarrage.borne_machine(reg, 1000, 0.8, 0.05, 1000) == 0.0
    redemarrage.marquer_demarrage(reg, 600)
    redemarrage.marquer_demarrage(reg, 35)
    b = redemarrage.borne_machine(reg, 1000, 0.8, 0.05, 1000 + 7200)
    assert b == pytest.approx(635 / 60 * 0.8 + 2 * 0.05)
    with pytest.raises(redemarrage.GardeOrdre):
        redemarrage.borne_machine(reg, 1000, 0.8, 0.05, 999)
    with pytest.raises(redemarrage.GardeOrdre):
        redemarrage.marquer_demarrage(reg, -1)


def test_noms_de_branches_lies_au_commit():
    c = "0123456789ab" + "c" * 28
    assert plan.branche_ordres(c) == "ordres/sparks-exp7-nul-v4-0123456789ab"
    assert plan.branche_fabrication(c, "essai/") == "essai/sparks-exp7-nul-v4-0123456789ab"
    assert plan.branche_causal(c, 7) == "calcul/sparks-exp7-nul-causal-v4-0123456789ab-007"
    for mauvais in (lambda: plan.branche_ordres("abc"), lambda: plan.branche_causal(c, 1, "main/")):
        with pytest.raises(ValueError):
            mauvais()
    assert not plan.branche_ordres(c).startswith("calcul/")


# --- 2. amorce v4 contre un dépôt d'essai local ---------------------------------------------------------------------------
def _git(d, *a):
    return subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True, text=True).stdout.strip()


def _faux_bin(d: Path, git_bloque: bool = False) -> Path:
    b = d / ("faux-bin-git-bloque" if git_bloque else "faux-bin")
    b.mkdir(exist_ok=True)
    (b / "curl").write_text('#!/bin/bash\necho "curl $*" >> "$FAUX_JOURNAL"\nprintf %s "${FAUX_HTTP:-200}"\n')
    (b / "vastai").write_text('#!/bin/bash\necho "vastai $*" >> "$FAUX_JOURNAL"\necho SORTIE-BRUTE\nexit "${FAUX_VASTAI:-0}"\n')
    if git_bloque:
        (b / "git").write_text('#!/bin/bash\nfor a in "$@"; do case "$a" in clone|fetch) sleep 1000;; esac; done\n'
                               'exec /usr/bin/git "$@"\n')
    for f in b.iterdir():
        f.chmod(0o755)
    return b


@pytest.fixture
def depot(tmp_path):
    d = tmp_path / "depot"
    (d / "registres").mkdir(parents=True)
    (d / "registres" / "go.md").write_text("| id | a | b | c | d | e | f | g |\n|---|---|---|---|---|---|---|---|\n"
                                           + L_BASE + "\n" + L_EXT + "\n")
    for v, fs in (("sparks_exp7_nul_v2", ("go.py", "depense.py", "garde_code.py")),
                  ("sparks_exp7_nul_v4", ("garde_code.py", "redemarrage.py"))):
        (d / "src" / "controle_ia" / v).mkdir(parents=True, exist_ok=True)
        for f in fs:
            shutil.copy(RACINE / "src" / "controle_ia" / v / f, d / "src" / "controle_ia" / v / f)
    (d / "scripts").mkdir()
    (d / "scripts" / "sparks_exp7_nul_instance_v4.sh").write_text(
        '#!/bin/bash\necho "INSTANCE FACTICE $PHASE $BRANCHE" >> "$FAUX_JOURNAL"\nmkdir -p "$TRAVAIL"\n'
        '[ -n "${FAUX_POUSSEE:-}" ] && echo tete > "$TRAVAIL/POUSSEE-VERIFIEE"\nexit 0\n')
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "t@example.invalid")
    _git(d, "config", "user.name", "t")
    _git(d, "config", "uploadpack.allowFilter", "true")
    _git(d, "config", "uploadpack.allowAnySHA1InWant", "true")
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "essai")
    return d, _git(d, "rev-parse", "HEAD")


def _ordres(depot: Path, commit: str, ordres: list[dict], *, branche: str | None = None, causal: bool = False):
    _git(depot, "checkout", "-q", "-B", branche or plan.branche_ordres(commit))
    (depot / "ordres").mkdir(exist_ok=True)
    for o in ordres:
        (depot / "ordres" / f"ordre-{o['numero']:03d}.json").write_text(json.dumps(o))
    if causal:
        (depot / "ordres" / "causal" / "reponses").mkdir(parents=True, exist_ok=True)
        (depot / "ordres" / "causal" / "cle-ouverte-v1.json").write_text("{}")
    _git(depot, "add", "-A")
    _git(depot, "commit", "-q", "-m", "ordres")
    _git(depot, "checkout", "-q", "main")


def _env(tmp_path, depot, commit, *, git_bloque=False, **kw) -> dict:
    r_ = tmp_path / "racine"
    r_.mkdir(exist_ok=True)
    e = {"PATH": f"{_faux_bin(tmp_path, git_bloque)}:/usr/bin:/bin", "HOME": str(tmp_path), "FAUX_JOURNAL": str(tmp_path / "faux.log"),
         "CONTAINER_ID": ID, "CONTAINER_API_KEY": "cle-factice", "MINUTERIE_PAS_S": "1", "MINUTERIE_REESSAI_S": "1",
         "MINUTERIE_MARGE_S": "4", "RACINE_AMORCE": str(r_), "DEPOT_URL": f"file://{depot}", "COMMIT": commit,
         "COMMIT_CODE": commit, "GH_TOKEN": "x", "PRIX_HEURE_USD": "0.8", "PRIX_STOCKAGE_HEURE_USD": "0.05",
         "GO_DATE": "2026-11-04", "ECHEANCE_UTC_S": str(int(time.time()) + 3600)}
    e.update({k: str(v) for k, v in kw.items()})
    return {k: v for k, v in e.items() if v != "∅"}


def _amorce(tmp_path, depot, commit, *, timeout=90, espace=False, script=AMORCE, **kw):
    env = _env(tmp_path, depot, commit, **kw)
    cmd = (["unshare", "-pf", "--mount-proc"] if espace else []) + ["bash", str(script)]
    t0 = time.time()
    try:
        r = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=timeout)
        out, code = r.stdout + r.stderr, r.returncode
    except subprocess.TimeoutExpired as e:
        out, code = (e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")), "délai"
    return code, out, Path(env["RACINE_AMORCE"]), time.time() - t0


def _arreter_minuteries(r_: Path):
    """Toutes les minuteries nées des démarrages de l'essai, par leur numéro de processus (R10)."""
    for p in (r_ / "sparks-v4-minuterie.pid",):
        if p.exists():
            try:
                os.kill(int(p.read_text().strip()), signal.SIGTERM)
            except (ProcessLookupError, ValueError):
                pass


def _journal(r_: Path) -> str:
    p = r_ / "sparks-v4-minuterie.log"
    return p.read_text() if p.exists() else ""


def test_amorce_git_bloque_borne_par_timeout(tmp_path, depot):
    code, out, r_, duree = _amorce(tmp_path, *depot, git_bloque=True, AMORCE_T_GIT_S=3, timeout=60)
    _arreter_minuteries(r_)
    assert code == 2 and "clonage impossible (ou délai de 3 s)" in out and duree < 30, (code, out)


def test_amorce_delais_ne_s_allongent_jamais():
    t = AMORCE.read_text(encoding="utf-8")
    assert 'T_GIT=$(borne_t "${AMORCE_T_GIT_S:-}" 600)' in t and "borne_t()" in t
    avant_calcul = t[:t.index('consigner_demarrage "$MINUTES"\n    echo "AMORCE V4 : fabrication')]
    for motif in ("git -c credential.helper=\"$AIDE\" clone", "sparse-checkout set", "checkout -q \"$COMMIT\"", "fetch -q --depth 1",
                  "archive -o", "tar -x", "import go;", "import depense;", "import garde_code;", "redemarrage.py\" verifier",
                  "redemarrage.py\" fait", "redemarrage.py\" lot", "redemarrage.py\" borne", "redemarrage.py\" demarrage"):
        lignes = [l for l in t.splitlines() if motif in l]
        assert lignes and all("timeout" in l for l in lignes), motif
    assert "timeout -k 5 120 vastai destroy instance" in t and avant_calcul


def test_delais_raccourcis_jamais_allonges():
    t = AMORCE.read_text(encoding="utf-8")
    f = [l for l in t.splitlines() if l.startswith("borne_t()")][0]
    out = subprocess.run(["bash", "-c", f + '\nborne_t 99999 600; borne_t 3 600; borne_t x 600; borne_t 0 600'],
                         capture_output=True, text=True).stdout.split()
    assert out == ["600", "3", "600", "600"]


def _minuterie(tmp_path, ech, **kw):
    t = AMORCE.read_text(encoding="utf-8")
    m = re.search(r"<<'MINUTERIE'\n(.*?)\nMINUTERIE\n", t, re.S)
    p = tmp_path / "minuterie.sh"
    p.write_text(m.group(1) + "\n")
    env = {"PATH": f"{_faux_bin(tmp_path)}:/usr/bin:/bin", "HOME": str(tmp_path), "FAUX_JOURNAL": str(tmp_path / "faux.log"),
           "CONTAINER_ID": ID, "CONTAINER_API_KEY": "k", "MINUTERIE_PAS_S": "1", "MINUTERIE_REESSAI_S": "1",
           "MINUTERIE_MARGE_S": "4", **{k: str(v) for k, v in kw.items()}}
    return subprocess.run(["bash", str(p), str(ech), str(tmp_path), "https://exemple.invalid/api"], env=env,
                          capture_output=True, text=True, timeout=60)


def test_minuterie_succes_http_2xx_sans_repli(tmp_path):
    r = _minuterie(tmp_path, int(time.time()), FAUX_HTTP="204", FAUX_VASTAI="1")
    log = (tmp_path / "sparks-v4-minuterie.log").read_text()
    assert r.returncode == 0 and log.count("DELETE instance") == 1 and "détruite" in log and "vastai" not in (tmp_path / "faux.log").read_text()


@espace_processus
def test_apres_echeance_dans_un_espace_de_processus_attente_sur_pid(tmp_path, depot):
    code, out, r_, _ = _amorce(tmp_path, *depot, espace=True, ECHEANCE_UTC_S=int(time.time()) - 5)
    assert code == 0 and "aucun calcul" in out and "DELETE instance 123456" in _journal(r_), out


@espace_processus
def test_sans_attente_la_minuterie_meurt_avec_le_principal(tmp_path, depot):
    t = AMORCE.read_text(encoding="utf-8").replace('echo "AMORCE V4 : destruction demandée ($1)"; attendre_minuterie;',
                                                    'echo "AMORCE V4 : destruction demandée ($1)";')
    s = tmp_path / "amorce-sans-attente.sh"
    s.write_text(t)
    code, out, r_, _ = _amorce(tmp_path, *depot, espace=True, script=s, ECHEANCE_UTC_S=int(time.time()) - 5)
    time.sleep(2)
    assert "DELETE" not in _journal(r_)          # témoin : la démonstration du contre-lecteur, reproduite


@espace_processus
def test_redemarrage_fin_dans_un_espace_de_processus(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 1, "instance": ID, "phase": "fin", "deja_usd": 0}])
    r_ = _disque(tmp_path, d, c)
    code, out, _, _ = _amorce(tmp_path, d, c, espace=True)
    assert code == 0 and "ordre 1 (fin)" in out and "DELETE instance 123456" in _journal(r_), out


def test_echeance_non_entiere_refusee(tmp_path, depot):
    code, out, r_, _ = _amorce(tmp_path, *depot, ECHEANCE_UTC_S="demain")
    assert code == 2 and "non entière" in out and not (r_ / "sparks-v4-minuterie.sh").exists()


def test_prefixe_des_branches_refuse_hors_calcul_et_essai(tmp_path, depot):
    code, out, r_, _ = _amorce(tmp_path, *depot, BRANCHE_PREFIXE="main/")
    _arreter_minuteries(r_)
    assert code == 2 and "BRANCHE_PREFIXE" in out


def test_creation_refus_avant_tout_calcul_v4(tmp_path, depot):
    code, out, r_, _ = _amorce(tmp_path, *depot, DEJA_USD="39.99")
    _arreter_minuteries(r_)
    assert code == 2 and "plafond trop bas" in out and not (r_ / "sparks-v4-demarrages.txt").exists()


def _disque(tmp_path, depot, commit):
    r_ = tmp_path / "racine"
    r_.mkdir(exist_ok=True)
    subprocess.run(["git", "clone", "-q", str(depot), str(r_ / "amorce-depot")], check=True)
    _git(r_ / "amorce-depot", "checkout", "-q", commit)
    (r_ / "sparks-v4-echeance.txt").write_text(str(int(time.time()) + 3600) + "\n")
    (r_ / "sparks-v4-creation.txt").write_text(str(int(time.time()) - 60) + "\n")
    return r_


def test_ordres_sur_la_branche_liee_au_commit_seulement(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 1, "instance": ID, "phase": "fin", "deja_usd": 0}], branche="calcul/sparks-exp7-nul-v3-ordres")
    r_ = _disque(tmp_path, d, c)
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "ordres illisibles" in out and "DELETE" not in _journal(r_)


def test_ordre_d_une_autre_instance_refuse(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 1, "instance": "999", "phase": "fin", "deja_usd": 0}])
    r_ = _disque(tmp_path, d, c)
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "ordre refusé" in out and "DELETE" not in _journal(r_)


def test_deja_usd_plus_bas_refuse_et_consignation_impossible(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 2, "instance": ID, "phase": "fin", "deja_usd": 1.0}])
    r_ = _disque(tmp_path, d, c)
    (r_ / "sparks-v4-ordres-faits.txt").write_text("1 5.0\n")
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "ordre refusé" in out
    (r_ / "sparks-v4-ordres-faits.txt").unlink()
    (r_ / "sparks-v4-ordres-faits.txt").symlink_to(tmp_path / "absent" / "faits.txt")   # lecture vide, écriture impossible
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "consignation de l'ordre impossible" in out and "DELETE" not in _journal(r_)


def test_borne_de_la_machine_l_emporte_sur_deja_usd(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 1, "instance": ID, "phase": "copie", "deja_usd": 0.0, "cas": ["vraie01"], "premier": False,
                    "copie_minutes": 5}])
    r_ = _disque(tmp_path, d, c)
    (r_ / "sparks-v4-demarrages.txt").write_text("3000\n")         # 50 h de carte à 0,80 : 40 USD déjà engagés
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "borne retenue 40" in out and "plafond trop bas pour la copie" in out, out


@pytest.mark.parametrize("prefixe", ["calcul/", "essai/"])
def test_causal_branche_liee_au_commit_et_a_l_ordre(tmp_path, depot, prefixe):
    d, c = depot
    _ordres(d, c, [{"numero": 3, "instance": ID, "phase": "causal", "deja_usd": 10.0}], causal=True)
    r_ = _disque(tmp_path, d, c)
    code, out, _, _ = _amorce(tmp_path, d, c, BRANCHE_PREFIXE=prefixe, FAUX_POUSSEE=1)
    _arreter_minuteries(r_)
    j = (tmp_path / "faux.log").read_text()
    assert f"INSTANCE FACTICE causal {prefixe}sparks-exp7-nul-causal-v4-{c[:12]}-003" in j
    assert code == 0 and "DELETE instance 123456" in _journal(r_)
    assert (r_ / "sparks-v4-demarrages.txt").read_text().split() != []


# --- 3. lanceur v4 --------------------------------------------------------------------------------------------------------
def _lanceur(tmp_path, *args, **env):
    e = {"PATH": "/usr/bin:/bin", "HOME": str(tmp_path), "SPARKS_ETAT_DIR": str(tmp_path / "etat")}
    e.update(env)
    return subprocess.run(["bash", str(LANCEUR), *args], env=e, capture_output=True, text=True, timeout=60)


def test_lanceur_destruction_timeout_env_nettoye_et_mandataire_par_nom(tmp_path):
    r = _lanceur(tmp_path, "destruction", "59079406", HTTPS_PROXY="http://jeton-secret@mandataire:3128",
                 SSL_CERT_FILE="/etc/ca.pem", NO_PROXY="localhost")
    assert r.returncode == 0
    cmd = [l for l in r.stdout.splitlines() if "vastai destroy" in l][0]
    assert cmd.startswith("timeout -k 10 120 env -i ") and cmd.count("vastai destroy instance 59079406 -y") == 1
    assert 'HTTPS_PROXY="$HTTPS_PROXY"' in cmd and 'SSL_CERT_FILE="$SSL_CERT_FILE"' in cmd and 'NO_PROXY="$NO_PROXY"' in cmd
    assert "HTTP_PROXY=" not in cmd.replace("HTTPS_PROXY=", "") and "REQUESTS_CA_BUNDLE" not in cmd
    assert "jeton-secret" not in r.stdout + r.stderr and '> "' in cmd and "2>&1" in cmd
    assert _lanceur(tmp_path, "destruction", "59; ls").returncode == 2


def test_lanceur_variables_du_mandataire_recues_par_le_sous_processus(tmp_path):
    r = _lanceur(tmp_path, "destruction", "1", HTTPS_PROXY="http://p:1", REQUESTS_CA_BUNDLE="/x.pem", HTTP_PROXY="http://q:2")
    cmd = [l for l in r.stdout.splitlines() if "vastai destroy" in l][0]
    faux = tmp_path / "fb"
    faux.mkdir()
    (faux / "vastai").write_text('#!/bin/bash\nenv | sort > "$HOME/env-vu.txt"\nexit 0\n')
    (faux / "vastai").chmod(0o755)
    e = {"PATH": f"{faux}:/usr/bin:/bin", "HOME": str(tmp_path), "HTTPS_PROXY": "http://p:1", "REQUESTS_CA_BUNDLE": "/x.pem",
         "HTTP_PROXY": "http://q:2", "AUTRE_SECRET": "ne-doit-pas-passer"}
    subprocess.run(["bash", "-c", cmd], env=e, check=True, timeout=60)
    vu = (tmp_path / "env-vu.txt").read_text()
    assert "HTTPS_PROXY=http://p:1" in vu and "REQUESTS_CA_BUNDLE=/x.pem" in vu and "HTTP_PROXY=http://q:2" in vu
    assert "AUTRE_SECRET" not in vu


@pytest.mark.parametrize("sortie,code,attendu,marqueur", [
    ("Started. {'success': True, 'new_contract': 59079406}", "0", "CRÉÉE : instance 59079406", False),
    ("Started. {'success': False, 'error': 'x'}", "0", "CRÉATION INCERTAINE", True),
    ("", "124", "CRÉATION INCERTAINE (code 124)", True),
    ("requests.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed", "1", "NON PARVENUE", False),
])
def test_lanceur_apres_creation(tmp_path, sortie, code, attendu, marqueur):
    f = tmp_path / "sortie.txt"
    f.write_text(sortie + "\nSECRET-DE-SORTIE\n")
    r = _lanceur(tmp_path, "apres-creation", str(f), code)
    assert attendu in r.stdout and "SECRET-DE-SORTIE" not in r.stdout + r.stderr
    assert (tmp_path / "etat" / ".creation-incertaine").exists() == marqueur
    assert r.returncode == {"CRÉÉE": 0, "CRÉATION INCERTAINE": 4, "NON PARVENUE": 3}[attendu.split(" :")[0].split(" (")[0]]


def test_lanceur_refuse_une_creation_apres_un_marqueur(tmp_path):
    (tmp_path / "etat").mkdir()
    (tmp_path / "etat" / ".creation-incertaine").write_text("code 124")
    r = _lanceur(tmp_path, "creation", "1", "0.8", "0.05", "a" * 40, "a" * 40, str(tmp_path / "e.json"))
    assert r.returncode == 2 and "création incertaine antérieure" in r.stderr


def test_lanceur_commande_de_creation_bornee_etiquetee_et_muette():
    t = LANCEUR.read_text(encoding="utf-8")
    ligne = [l for l in t.splitlines() if "vastai create instance" in l][0]
    assert ligne.startswith("GO_ID=GO-2026-11-04-04 timeout -k 10 300 $(prefixe_env) vastai create instance")
    assert "--label sparks-exp7-nul-v4-$COURT" in ligne
    suite = t[t.index(ligne):].splitlines()[2]
    assert '> "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v4.sh apres-creation "$F" \\$?' in suite
    assert [l for l in t.splitlines() if "vastai start instance" in l and "timeout -k 10 300" in l and '> "$F" 2>&1' in l]
    assert "calcul/sparks-exp7-nul-v3-ordres" not in t and "ordres/sparks-exp7-nul-v4-$COURT" in t
