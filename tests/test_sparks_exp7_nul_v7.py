"""Essais de SPARKS-EXP7-NUL, v7 : ceux de la v6 sur les scripts v7, plus les appels de modules du script d'instance
(paquet trouvé sous `-I`, hors de tout PYTHONPATH : répétition v6). Origine v6 : ceux de la v5 sur les scripts v6, avec l'essai du tir indépendant du commit extrait
et de la date (répétition v5, R-1514). Origine : ceux de la v4 rejoués sur les fichiers v5 (contre-lecture du delta v3) : `timeout` sur chaque étape de l'amorce (git bloqué :
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

from controle_ia.sparks_exp7_nul_v5 import plan, redemarrage, tir

RACINE = Path(__file__).resolve().parents[1]
AMORCE = RACINE / "scripts" / "amorce_instance_sparks_exp7_nul_v7.sh"
LANCEUR = RACINE / "scripts" / "lancer_sparks_exp7_nul_v7.sh"
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
    redemarrage.marquer_demarrage(reg, 1, 600)
    redemarrage.marquer_demarrage(reg, 2, 35)
    b = redemarrage.borne_machine(reg, 1000, 0.8, 0.05, 1000 + 7200)
    assert b == pytest.approx(635 / 60 * 0.8 + 2 * 0.05)
    with pytest.raises(redemarrage.GardeOrdre):
        redemarrage.borne_machine(reg, 1000, 0.8, 0.05, 999)
    with pytest.raises(redemarrage.GardeOrdre):
        redemarrage.marquer_demarrage(reg, 3, -1)


def test_noms_de_branches_lies_au_commit():
    c = "0123456789ab" + "c" * 28
    assert plan.branche_ordres(c) == "ordres/sparks-exp7-nul-v5-0123456789ab"
    assert plan.branche_fabrication(c, "essai/") == "essai/sparks-exp7-nul-v5-0123456789ab"
    assert plan.branche_causal(c, 7) == "calcul/sparks-exp7-nul-causal-v5-0123456789ab-007"
    for mauvais in (lambda: plan.branche_ordres("abc"), lambda: plan.branche_causal(c, 1, "main/")):
        with pytest.raises(ValueError):
            mauvais()
    assert not plan.branche_ordres(c).startswith("calcul/")


# --- 2. amorce v5 contre un dépôt d'essai local ---------------------------------------------------------------------------
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
                  ("sparks_exp7_nul_v5", ("garde_code.py", "redemarrage.py", "tir.py")),
                  ("sparks_exp7_nul_v7", ("garde_code.py",))):
        (d / "src" / "controle_ia" / v).mkdir(parents=True, exist_ok=True)
        for f in fs:
            shutil.copy(RACINE / "src" / "controle_ia" / v / f, d / "src" / "controle_ia" / v / f)
    (d / "scripts").mkdir()
    (d / "scripts" / "sparks_exp7_nul_instance_v7.sh").write_text(
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
    for p in (r_ / "sparks-v5-minuterie.pid",):
        if p.exists():
            try:
                os.kill(int(p.read_text().strip()), signal.SIGTERM)
            except (ProcessLookupError, ValueError):
                pass


def _journal(r_: Path) -> str:
    p = r_ / "sparks-v5-minuterie.log"
    return p.read_text() if p.exists() else ""


def test_amorce_git_bloque_borne_par_timeout(tmp_path, depot):
    code, out, r_, duree = _amorce(tmp_path, *depot, git_bloque=True, AMORCE_T_GIT_S=3, timeout=60)
    _arreter_minuteries(r_)
    assert code == 2 and "clonage impossible (ou délai de 3 s)" in out and duree < 30, (code, out)


def test_amorce_delais_ne_s_allongent_jamais():
    t = AMORCE.read_text(encoding="utf-8")
    assert 'T_GIT=$(borne_t "${AMORCE_T_GIT_S:-}" 600)' in t and "borne_t()" in t
    avant_calcul = t[:t.index('consigner_demarrage "$MINUTES"\n    echo "AMORCE V5 : fabrication')]
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
    log = (tmp_path / "sparks-v5-minuterie.log").read_text()
    assert r.returncode == 0 and log.count("DELETE instance") == 1 and "détruite" in log and "vastai" not in (tmp_path / "faux.log").read_text()


@espace_processus
def test_apres_echeance_dans_un_espace_de_processus_attente_sur_pid(tmp_path, depot):
    code, out, r_, _ = _amorce(tmp_path, *depot, espace=True, ECHEANCE_UTC_S=int(time.time()) - 5)
    assert code == 0 and "aucun calcul" in out and "DELETE instance 123456" in _journal(r_), out


@espace_processus
def test_sans_attente_la_minuterie_meurt_avec_le_principal(tmp_path, depot):
    t = AMORCE.read_text(encoding="utf-8").replace('echo "AMORCE V5 : destruction demandée ($1)"; attendre_minuterie;',
                                                    'echo "AMORCE V5 : destruction demandée ($1)";')
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
    assert code == 2 and "non entière" in out and not (r_ / "sparks-v5-minuterie.sh").exists()


def test_prefixe_des_branches_refuse_hors_calcul_et_essai(tmp_path, depot):
    code, out, r_, _ = _amorce(tmp_path, *depot, BRANCHE_PREFIXE="main/")
    _arreter_minuteries(r_)
    assert code == 2 and "BRANCHE_PREFIXE" in out


def test_creation_refus_avant_tout_calcul_v5(tmp_path, depot):
    code, out, r_, _ = _amorce(tmp_path, *depot, DEJA_USD="39.99")
    _arreter_minuteries(r_)
    assert code == 2 and "plafond trop bas" in out and not (r_ / "sparks-v5-demarrages.txt").exists()


def _disque(tmp_path, depot, commit, gardes_ok=True):
    r_ = tmp_path / "racine"
    r_.mkdir(exist_ok=True)
    subprocess.run(["git", "clone", "-q", str(depot), str(r_ / "amorce-depot")], check=True)
    _git(r_ / "amorce-depot", "checkout", "-q", commit)
    (r_ / "sparks-v5-echeance.txt").write_text(str(int(time.time()) + 3600) + "\n")
    (r_ / "sparks-v5-creation.txt").write_text(str(int(time.time()) - 60) + "\n")
    if gardes_ok:
        (r_ / "sparks-v5-gardes-ok").touch()
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
    (r_ / "sparks-v5-ordres-faits.txt").write_text("1 5.0\n")
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "ordre refusé" in out
    (r_ / "sparks-v5-ordres-faits.txt").unlink()
    (r_ / "sparks-v5-ordres-faits.txt").symlink_to(tmp_path / "absent" / "faits.txt")   # lecture vide, écriture impossible
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "consignation de l'ordre impossible" in out and "DELETE" not in _journal(r_)


def test_borne_de_la_machine_l_emporte_sur_deja_usd(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 1, "instance": ID, "phase": "copie", "deja_usd": 0.0, "cas": ["vraie01"], "premier": False,
                    "copie_minutes": 5}])
    r_ = _disque(tmp_path, d, c)
    (r_ / "sparks-v5-demarrages.txt").write_text("p 1 3000\n")     # 50 h de carte à 0,80 : 40 USD déjà engagés
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
    assert f"INSTANCE FACTICE causal {prefixe}sparks-exp7-nul-causal-v5-{c[:12]}-003" in j
    assert code == 0 and "DELETE instance 123456" in _journal(r_)
    assert (r_ / "sparks-v5-demarrages.txt").read_text().split() != []


# --- 3. lanceur v5 --------------------------------------------------------------------------------------------------------
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
    assert "HTTP_PROXY=" not in cmd.replace("HTTPS_PROXY=", "") and "REQUESTS_CA_BUNDLE" not in cmd and "VAST_API_KEY" not in cmd
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
    ("SSLError: CERTIFICATE_VERIFY_FAILED (annexe)\nStarted. {'success': True, 'new_contract': 59079406}", "0", "CRÉÉE : instance 59079406", False),
    ("failed with error 404/3603: no_such_ask", "0", "CRÉATION INCERTAINE (code 0)", True),
    ("Started. {'success': False, 'error': 'x'}", "0", "CRÉATION INCERTAINE", True),
    ("Started. {'success': False, 'new_contract': 59079406}", "0", "CRÉATION INCERTAINE", True),
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
    ligne = [l for l in t.splitlines() if "vastai create instance" in l and "GO-2026-11-04-04" in l][0]
    assert ligne.startswith("GO_ID=GO-2026-11-04-04 timeout -k 10 300 $(prefixe_env) vastai create instance")
    assert "--label sparks-exp7-nul-v5-$COURT" in ligne
    suite = t[t.index(ligne):].splitlines()[2]
    assert '> "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v7.sh apres-creation "$F" \\$?' in suite
    assert 'git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v7.sh"' in suite and "cat scripts/amorce" not in t
    assert "-e ADDENDUM_SHA256=$SHA_A" in t[t.index(ligne):].splitlines()[1]
    assert [l for l in t.splitlines() if "vastai start instance" in l and "timeout -k 10 300" in l and '> "$F" 2>&1' in l
            and "apres-commande start" in l]
    assert "calcul/sparks-exp7-nul-v3-ordres" not in t and "ordres/sparks-exp7-nul-v5-$COURT" in t


# --- 4. neuf en v5 (contre-lecture du delta v4) ---------------------------------------------------------------------------
def test_borne_sur_la_duree_reelle_et_plafond_sans_fin(tmp_path):
    reg = tmp_path / "r.txt"
    redemarrage.marquer_demarrage(reg, 100, 1440)
    redemarrage.marquer_fin(reg, 100, 7)
    redemarrage.marquer_demarrage(reg, 200, 35)              # démarrage tué : aucune fin, le plafond compte
    assert redemarrage.minutes_consignees(reg) == 7 + 35
    (tmp_path / "x.txt").write_text("d 9 3\n")
    with pytest.raises(redemarrage.GardeOrdre, match="sans plafond"):
        redemarrage.minutes_consignees(tmp_path / "x.txt")
    (tmp_path / "y.txt").write_text("p 1 3\nzz\n")
    with pytest.raises(redemarrage.GardeOrdre):
        redemarrage.minutes_consignees(tmp_path / "y.txt")


def test_coin_haut_du_devis_la_phase_causale_reste_admise(tmp_path):
    """Création le 5 à 12:00, fabrication réelle 6 h, 18 copies de 30 min, 0,80/0,05 : la phase causale (≥ 60 min) passe."""
    from datetime import datetime, timezone
    from controle_ia.sparks_exp7_nul_v2 import depense
    reg = tmp_path / "r.txt"
    t = int(datetime(2026, 11, 5, 12, tzinfo=timezone.utc).timestamp())
    redemarrage.marquer_demarrage(reg, t, 1440)
    redemarrage.marquer_fin(reg, t, 360)
    for k in range(18):
        redemarrage.marquer_demarrage(reg, t + 1 + k, 35)
        redemarrage.marquer_fin(reg, t + 1 + k, 30)
    maintenant = t + 2 * 86400
    b = redemarrage.borne_machine(reg, t, 0.8, 0.05, maintenant)
    minutes = depense.duree_max_minutes(0.8, 0.05, datetime.fromtimestamp(maintenant, timezone.utc), deja_usd=b)
    assert minutes >= 60, (b, minutes)


def test_minuterie_corps_success_false_n_est_pas_un_succes(tmp_path):
    b = tmp_path / "bin-corps"
    b.mkdir()
    _faux_bin(tmp_path)
    shutil.copy(tmp_path / "faux-bin" / "vastai", b / "vastai")
    (b / "curl").write_text('#!/bin/bash\necho "curl $*" >> "$FAUX_JOURNAL"\nwhile [ $# -gt 0 ]; do [ "$1" = -o ] && '
                            'printf \'{"success": false, "msg": "x"}\' > "$2"; shift; done\nprintf 200\n')
    (b / "curl").chmod(0o755)
    r = _minuterie(tmp_path, int(time.time()), FAUX_VASTAI="1", MINUTERIE_MARGE_S="200", PATH=f"{b}:/usr/bin:/bin")
    log = (tmp_path / "sparks-v5-minuterie.log").read_text()
    assert r.returncode == 4 and "refus dans le corps : oui" in log and "détruite" not in log and log.count("DELETE instance") >= 2


def test_minuterie_aucune_tentative_au_dela_de_la_marge(tmp_path):
    r = _minuterie(tmp_path, int(time.time()), FAUX_HTTP="503", FAUX_VASTAI="1", MINUTERIE_MARGE_S="4")
    log = (tmp_path / "sparks-v5-minuterie.log").read_text()
    assert r.returncode == 4 and log.count("DELETE instance") == 1 and "plus de tentative possible" in log


def _fonction(nom: str) -> str:
    t = AMORCE.read_text(encoding="utf-8")
    i = t.index(f"{nom}() {{")
    return t[i:t.index("\n}\n", i) + 3]


def test_addendum_reconnu_empreinte_main_jouet_et_refus(tmp_path):
    d = tmp_path / "d"
    d.mkdir()
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "t@example.invalid")
    _git(d, "config", "user.name", "t")
    (d / "prereg").mkdir()
    (d / "prereg" / "SPARKS-EXP7-NUL-addendum-1.md").write_text("addendum scellé\n")
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "a")
    c = _git(d, "rev-parse", "HEAD")
    _git(d, "checkout", "-q", "-b", "essai")
    (d / "x").write_text("x")
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "essai")
    c_essai = _git(d, "rev-parse", "HEAD")
    r_ = tmp_path / "r"
    subprocess.run(["git", "clone", "-q", str(d), str(r_ / "amorce-depot")], check=True)
    import hashlib
    bon = hashlib.sha256(b"addendum scell\xc3\xa9\n").hexdigest()

    def jouer(commit, **env):
        script = f'R="{r_}"; T_GARDE=20; T_GIT=20; COMMIT={commit}\n' + _fonction("addendum_reconnu") + "addendum_reconnu\n"
        e = {"PATH": "/usr/bin:/bin", "HOME": str(tmp_path), **env}
        return subprocess.run(["bash", "-c", script], env=e, capture_output=True, text=True, timeout=60)
    assert jouer(c_essai, ADDENDUM_SHA256=bon).returncode == 0                 # empreinte attendue
    assert jouer(c_essai, ADDENDUM_SHA256="0" * 64).returncode == 1            # empreinte fausse, commit hors de main
    assert jouer(c_essai).returncode == 1                                       # aucune empreinte, commit hors de main
    assert jouer(c).returncode == 0                                             # commit contenu dans origin/main
    assert jouer(c_essai, MODE="jouet").returncode == 0                         # jouet : non exigé


def test_copie_ou_causal_exigent_les_gardes_passees(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 1, "instance": ID, "phase": "causal", "deja_usd": 1.0}], causal=True)
    r_ = _disque(tmp_path, d, c, gardes_ok=False)
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "seul un ordre « fin » est permis" in out and "INSTANCE FACTICE" not in (
        (tmp_path / "faux.log").read_text() if (tmp_path / "faux.log").exists() else "")


def test_duree_reelle_consignee_apres_la_phase_causale(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 3, "instance": ID, "phase": "causal", "deja_usd": 10.0}], causal=True)
    r_ = _disque(tmp_path, d, c)
    _amorce(tmp_path, d, c, FAUX_POUSSEE=1)
    _arreter_minuteries(r_)
    lignes = (r_ / "sparks-v5-demarrages.txt").read_text().split("\n")
    assert lignes[0].startswith("p ") and lignes[1].startswith("d ") and lignes[0].split()[1] == lignes[1].split()[1]
    assert int(lignes[1].split()[2]) <= 2


def test_temoin_minuterie_anterieure_et_outils(tmp_path, depot):
    d, c = depot
    r_ = tmp_path / "racine"
    r_.mkdir()
    vivant = subprocess.Popen(["sleep", "60"])
    try:
        (r_ / "sparks-v5-minuterie.pid").write_text(str(vivant.pid))
        code, out, _, _ = _amorce(tmp_path, d, c, DEJA_USD="39.99")
        _arreter_minuteries(r_)
        assert f"TÉMOIN : minuterie antérieure {vivant.pid} encore vivante" in out
        assert "AMORCE V5 : outils : curl oui, git oui, unshare " in out
    finally:
        vivant.kill()


def test_lanceur_cle_de_vast_par_son_nom(tmp_path):
    r = _lanceur(tmp_path, "destruction", "7", VAST_API_KEY="cle-tres-secrete", HTTPS_PROXY="http://p:1")
    cmd = [l for l in r.stdout.splitlines() if "vastai destroy" in l][0]
    assert 'VAST_API_KEY="$VAST_API_KEY"' in cmd and "cle-tres-secrete" not in r.stdout + r.stderr
    faux = tmp_path / "fb"
    faux.mkdir()
    (faux / "vastai").write_text('#!/bin/bash\nenv | sort > "$HOME/env-vu.txt"\necho "failed with error 401" >&2\nexit 0\n')
    (faux / "vastai").chmod(0o755)
    e = {"PATH": f"{faux}:/usr/bin:/bin", "HOME": str(tmp_path), "VAST_API_KEY": "cle-tres-secrete", "HTTPS_PROXY": "http://p:1",
         "SPARKS_ETAT_DIR": str(tmp_path / "etat")}
    p = subprocess.run(["bash", "-c", cmd], env=e, capture_output=True, text=True, timeout=60, cwd=str(RACINE))
    assert "VAST_API_KEY=cle-tres-secrete" in (tmp_path / "env-vu.txt").read_text()
    assert "REFUSÉ" in p.stdout and p.returncode == 5 and "401" not in p.stdout       # R-1506 : refus sur stderr, code 0


@pytest.mark.parametrize("sortie,quoi,code,att", [
    ("failed with error 404: no such instance", "destroy", 5, "REFUSÉ"),
    ('{"success": false}', "start", 5, "REFUSÉ"),
    ("SSLError: CERTIFICATE_VERIFY_FAILED", "start", 3, "NON PARVENU"),
    ("Starting instance 7.", "start", 0, "ENVOYÉ"),
])
def test_lanceur_apres_commande(tmp_path, sortie, quoi, code, att):
    f = tmp_path / "s.txt"
    f.write_text(sortie + "\nSECRET\n")
    r = _lanceur(tmp_path, "apres-commande", quoi, str(f), "0", "7")
    assert r.returncode == code and att in r.stdout and "SECRET" not in r.stdout and "vastai show instance 7 --raw" in r.stdout


@pytest.mark.parametrize("sortie,att,code,etat", [
    ('{"id": 7, "actual_status": "exited", "cur_state": "stopped", "ssh_key": "SECRET"}', "exited", 0, "exited"),
    ('{"id": 7, "actual_status": "running"}', "absente", 6, "running"),
    ("failed with error 404: no_such_instance", "absente", 0, "absente"),
    ("rien de lisible", "absente", 6, "illisible"),
])
def test_lanceur_inventaire(tmp_path, sortie, att, code, etat):
    f = tmp_path / "i.txt"
    f.write_text(sortie)
    r = _lanceur(tmp_path, "inventaire", str(f), "7", att)
    assert r.returncode == code and f"état {etat}" in r.stdout and "SECRET" not in r.stdout


def test_tir_go_plafond_devis_et_bornes(tmp_path):
    from datetime import date
    p = tmp_path / "go.md"
    l = "| GO-2026-11-05-01 | 2026-11-05 | calcul | tir réel de SPARKS v5 | {} | 2026-11-06 | {} | mot |"
    j = date(2026, 11, 5)
    p.write_text("| id | a | b | c | d | e | f | g |\n" + l.format("5 USD", "Lazar") + "\n")
    r = tir.preparer(p, "GO-2026-11-05-01", 0.8, 0.05, 25, j, maintenant_s=1000)
    assert r["echeance_utc_s"] == 1000 + 25 * 60 and r["devis_usd"] == pytest.approx(0.8 * 50 / 60 + 0.05 * 85 / 60)
    for contenu, motif in ((l.format("6 USD", "Lazar"), "plafond"), (l.format("5 USD", "Claude"), "auteur"), ("", "absent")):
        p.write_text("| id | a | b | c | d | e | f | g |\n" + contenu + "\n")
        with pytest.raises(tir.GardeTir, match=motif):
            tir.preparer(p, "GO-2026-11-05-01", 0.8, 0.05, 25, j)
    p.write_text("| id | a | b | c | d | e | f | g |\n" + l.format("1 USD", "Lazar") + "\n")
    with pytest.raises(tir.GardeTir, match="devis"):
        tir.preparer(p, "GO-2026-11-05-01", 3.0, 0.05, 25, j)
    for m in (19, 31):
        with pytest.raises(tir.GardeTir, match="durée"):
            tir.devis_tir(0.8, 0.05, m)
    p.write_text("| id | a | b | c | d | e | f | g |\n" + l.format("5 USD", "Lazar") + "\n")
    with pytest.raises(tir.GardeTir, match="validité"):
        tir.preparer(p, "GO-2026-11-05-01", 0.8, 0.05, 25, date(2026, 11, 7))


def _commit_du_code() -> str | None:
    """Commit du code, indépendant du commit extrait : `COMMIT_CODE` (posé par l'amorce sur l'instance), sinon le dernier
    commit qui a écrit la liste fermée v6 (un commit enfant qui ajoute l'addendum ne la touche pas)."""
    c = os.environ.get("COMMIT_CODE", "")
    if re.fullmatch(r"[0-9a-f]{40}", c):
        return c
    r = subprocess.run(["git", "-C", str(RACINE), "log", "-1", "--format=%H", "--", "src/controle_ia/sparks_exp7_nul_v7/liste-fermee-v1.txt"],
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", r.stdout.strip()) else None


def test_lanceur_mode_tir_commande_ecrite(tmp_path):
    if subprocess.run(["git", "-C", str(RACINE), "rev-parse", "HEAD"], capture_output=True).returncode != 0:
        pytest.skip("hors d'un dépôt git (copie du banc)")
    code = _commit_du_code()
    if code is None:
        pytest.skip("liste fermée v6 écrite au commit final")
    reg = tmp_path / "go.md"
    reg.write_text("| id | a | b | c | d | e | f | g |\n| GO-2026-11-05-01 | 2026-11-05 | calcul | tir | 5 USD | 2026-11-06 | Lazar | mot |\n")
    r = _lanceur(tmp_path, "tir", "123", "0.8", "0.05", code, "GO-2026-11-05-01", "25", SPARKS_REGISTRE_GO=str(reg),
                 SPARKS_DATE_TIR="2026-11-05")
    assert r.returncode == 0, r.stderr
    t = r.stdout
    assert "--label sparks-exp7-nul-tir-" in t and "GO_ID=GO-2026-11-05-01 timeout -k 10 300" in t and "--disk 20" in t
    assert "vastai start instance $ID" in t and "ordres/sparks-exp7-nul-v5-" in t and '"phase\\": \\"fin\\"' in t
    assert 'git show "' + code + ':scripts/amorce_instance_sparks_exp7_nul_v7.sh"' in t and "HF_TOKEN" not in t
    assert "inventaire" in t and "absente" in t and "exited" in t
    r2 = _lanceur(tmp_path, "tir", "123", "0.8", "0.05", code, "GO-2026-11-05-01", "25", SPARKS_REGISTRE_GO=str(reg),
                  SPARKS_DATE_TIR="2026-11-07")                       # même registre, date hors validité : refus
    assert r2.returncode == 2 and "validité" in r2.stderr


def test_amorce_v5_ordre_des_gardes_et_consignations():
    t = AMORCE.read_text(encoding="utf-8")
    creation = t[t.index('echo "AMORCE V5 : création"'):t.index('echo "AMORCE V5 : redémarrage"')]
    i_code, i_add = creation.index("import garde_code;"), creation.index("addendum_reconnu ||")
    i_ok, i_cons = creation.index('"$R/sparks-v5-gardes-ok"'), creation.index('consigner_demarrage "$MINUTES"')
    i_lance = creation.index("sparks_exp7_nul_instance_v7.sh")
    assert i_code < i_add < i_ok < i_cons < i_lance and "consigner_fin" in creation[i_lance:]
    copie = t[t.index("    copie)"):t.index("    causal)")]
    assert copie.index('consigner_demarrage "$((CM + 5))"') < copie.index("redemarrage.py\" lot") and "consigner_fin" in copie
    causal = t[t.index("    causal)"):]
    assert causal.index('consigner_demarrage "$MINUTES"') < causal.index("sparks_exp7_nul_instance_v7.sh") < causal.index("consigner_fin")


def test_lanceur_tir_statique():
    t = LANCEUR.read_text(encoding="utf-8")
    bloc = t[t.index('if [ "$QUOI" = tir ]; then'):t.index("    exit 0\nfi")]
    ligne = [l for l in bloc.splitlines() if "vastai create instance" in l][0]
    assert ligne.startswith("GO_ID=$GOT timeout -k 10 300 $(prefixe_env) vastai create instance") and "--disk 20" in ligne
    assert "--label sparks-exp7-nul-tir-$COURT" in ligne and "HF_TOKEN" not in bloc
    assert 'L=$(timeout 120 python3 -I -B "$P5/tir.py" verifier' in bloc and "garde_code; sys.exit(garde_code.main(sys.argv[1:]))\" liste" in bloc
    assert [l for l in bloc.splitlines() if l.startswith("GO_ID=$GOT timeout -k 10 300") and "vastai start instance" in l and "apres-commande start" in l]
    assert "inventaire_cmd '$ID' absente" in bloc and "inventaire_cmd '$ID' exited" in bloc


def test_v7_scripts_garde_v7_essais_v7_et_date_du_tir():
    a = AMORCE.read_text(encoding="utf-8")
    assert "sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v7'); import garde_code;" in a and a.count("sparks_exp7_nul_instance_v7.sh") == 2
    assert "'$P5'); import garde_code" not in a and "sparks_exp7_nul_instance_v5.sh" not in a
    i = (RACINE / "scripts" / "sparks_exp7_nul_instance_v7.sh").read_text(encoding="utf-8")
    l = [x for x in i.splitlines() if "-m pytest" in x][0]
    assert "tests/test_sparks_exp7_nul_v7.py" in l and "test_sparks_exp7_nul_v5.py" not in l
    assert "sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v7'); import garde_code;" in i
    t = LANCEUR.read_text(encoding="utf-8")
    assert '"$P5/tir.py" verifier "$REG" "$GOT" "$PRIX" "$STOCK" "$MIN" ${SPARKS_DATE_TIR:+"$SPARKS_DATE_TIR"})' in t
    assert t.count("sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v7'); import garde_code;") == 2
    assert "amorce_instance_sparks_exp7_nul_v5.sh" not in t and "lancer_sparks_exp7_nul_v5.sh" not in t


# --- 5. neuf en v7 : appels de modules sous -I (répétition v6) -------------------------------------------------------------
INSTANCE = RACINE / "scripts" / "sparks_exp7_nul_instance_v7.sh"


def _bloc_module() -> tuple[str, str]:
    """Définition de `SRC` et de la fonction `module`, et la ligne de l'essai d'égalité des lots, tirées du script v7."""
    t = INSTANCE.read_text(encoding="utf-8").splitlines()
    i = next(k for k, l in enumerate(t) if l.startswith('SRC="$PWD/src"'))
    j = next(k for k in range(i, len(t)) if t[k] == "}")
    egal = next(l for l in t if "egalite-lots" in l and not l.lstrip().startswith("#"))
    return "\n".join(t[i:j + 1]), egal


def _env_sans_pythonpath(tmp_path) -> dict:
    import sys
    return {"PATH": f"{Path(sys.executable).parent}:/usr/sbin:/usr/bin:/sbin:/bin", "HOME": str(tmp_path)}


def test_script_d_instance_trouve_le_paquet_sous_isolement(tmp_path):
    """Joue, depuis le script v7, la définition de `module` et le premier appel (essai d'égalité des lots), hors de tout
    PYTHONPATH et depuis un autre dossier : le module doit être trouvé et l'essai passer."""
    bloc, egal = _bloc_module()
    j = tmp_path / "journal.txt"
    script = f'set -euo pipefail\ncd "{RACINE}"\n{bloc}\ncd "{tmp_path}"\nJOURNAL="{j}"\nLOTS=oui\n{egal}\necho "LOTS=$LOTS"\n'
    r = subprocess.run(["bash", "-c", script], env=_env_sans_pythonpath(tmp_path), capture_output=True, text=True, timeout=600)
    journal = j.read_text() if j.exists() else ""
    assert "No module named" not in journal + r.stderr, journal[-500:]
    assert "EGALITE LOTS OK" in journal and r.stdout.strip().endswith("LOTS=oui"), (journal[-500:], r.stdout, r.stderr)


def test_temoin_l_ancien_appel_ne_trouve_pas_le_paquet(tmp_path):
    import sys
    r = subprocess.run([sys.executable, "-I", "-B", "-m", "controle_ia.sparks_exp7_nul_v3.instance", "egalite-lots"], cwd=str(RACINE),
                       env={**_env_sans_pythonpath(tmp_path), "PYTHONPATH": "src"}, capture_output=True, text=True, timeout=120)
    assert r.returncode != 0 and "No module named 'controle_ia'" in r.stderr


def test_manifeste_du_script_d_instance_trouve_le_paquet(tmp_path):
    import sys
    t = INSTANCE.read_text(encoding="utf-8")
    i = t.index("<<'PY'\n") + len("<<'PY'\n")
    tete = "\n".join(t[i:].splitlines()[:5])
    assert tete.splitlines()[1].startswith("sys.path.insert(0, sys.argv.pop(1))")
    code = tete + "\nprint('MANIFESTE IMPORTABLE', sys.argv[1:3])\n"
    r = subprocess.run([sys.executable, "-I", "-B", "-", str(RACINE / "src"), "run", "jouet"], input=code, cwd=str(tmp_path),
                       env=_env_sans_pythonpath(tmp_path), capture_output=True, text=True, timeout=120)
    assert r.returncode == 0 and "MANIFESTE IMPORTABLE ['run', 'jouet']" in r.stdout, r.stderr


def test_aucun_appel_python_isole_par_module_sans_chemin():
    t = INSTANCE.read_text(encoding="utf-8")
    assert not re.search(r"python3? (-u )?-I -B -m controle_ia", t)
    assert len(re.findall(r"^\s*(?:if \[ \"\$MODE\" = jouet \]; then |else )?module controle_ia\.", t, re.M)) == 5
    assert 'python -I -B - "$SRC" "$RUN_ID"' in t
