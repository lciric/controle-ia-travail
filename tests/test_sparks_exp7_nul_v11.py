"""Essais de SPARKS-EXP7-NUL, v8 : ceux de la v7 sur les scripts v8, plus le manifeste de chaque phase joué sur un commit
enfant (addendum scellé conforme : cas sain ; texte parent seul : refus ; répétition v7). Origine v7 : ceux de la v6 sur les scripts v7, plus les appels de modules du script d'instance
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
AMORCE = RACINE / "scripts" / "amorce_instance_sparks_exp7_nul_v11.sh"
LANCEUR = RACINE / "scripts" / "lancer_sparks_exp7_nul_v11.sh"
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
    (b / "curl").write_text('#!/bin/bash\necho "curl $*" >> "$FAUX_JOURNAL"\no=""; p=""; for a in "$@"; do [ "$p" = -o ] && o="$a"; p="$a"; done\n'
                            'if [ -n "$o" ]; then if [ -n "${FAUX_CORPS+x}" ]; then printf %s "$FAUX_CORPS" > "$o"; '
                            'else printf %s \'{"success": true}\' > "$o"; fi; fi\nprintf %s "${FAUX_HTTP:-200}"\n')
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
                  ("sparks_exp7_nul_v11", ("garde_code.py",))):
        (d / "src" / "controle_ia" / v).mkdir(parents=True, exist_ok=True)
        for f in fs:
            shutil.copy(RACINE / "src" / "controle_ia" / v / f, d / "src" / "controle_ia" / v / f)
    (d / "scripts").mkdir()
    (d / "scripts" / "sparks_exp7_nul_instance_v11.sh").write_text(
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
    t = AMORCE.read_text(encoding="utf-8").replace('attendre_minuterie; resultat_destruction "${2:-0}"; }', 'exit "${2:-0}"; }')
    assert t != AMORCE.read_text(encoding="utf-8")
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
    assert code == 2 and "non entière" in out and "destruction immédiate" in out and "DELETE instance 123456" in _journal(r_), out
    assert "destruction obtenue" in out


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
    assert code == 2 and "ordres illisibles" in out and "boucle de redémarrage présumée" in out
    assert "DELETE instance 123456" in _journal(r_)


def test_ordre_d_une_autre_instance_refuse(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 1, "instance": "999", "phase": "fin", "deja_usd": 0}])
    r_ = _disque(tmp_path, d, c)
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "ordre refusé" in out and "boucle de redémarrage présumée" in out and "DELETE instance 123456" in _journal(r_)


def test_deja_usd_plus_bas_refuse_et_consignation_impossible(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 2, "instance": ID, "phase": "fin", "deja_usd": 1.0}])
    r_ = _disque(tmp_path, d, c)
    (r_ / "sparks-v5-ordres-faits.txt").write_text("1 5.0\n")
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "ordre refusé" in out and "boucle de redémarrage présumée" in out
    (r_ / "sparks-v5-detruire").unlink()
    (r_ / "sparks-v5-minuterie.log").unlink()
    (r_ / "sparks-v5-ordres-faits.txt").unlink()
    (r_ / "sparks-v5-ordres-faits.txt").symlink_to(tmp_path / "absent" / "faits.txt")   # lecture vide, écriture impossible
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 2 and "consignation de l'ordre impossible" in out and "boucle de redémarrage présumée" in out
    assert "DELETE instance 123456" in _journal(r_)


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
    (faux / "vastai").write_text('#!/bin/bash\nenv | sort > "$HOME/env-vu.txt"\necho "destroying instance 1."\nexit 0\n')
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
    ("failed with error 404/3603: no_such_ask", "0", "OFFRE RETIRÉE (no_such_ask", False),
    ("{'success': False, 'error': True, 'msg': 'error 404/3603: no_such_ask  Instance type is not available.'}", "0", "OFFRE RETIRÉE", False),
    ("Started. {'success': True, 'new_contract': 59079406} no_such_ask", "0", "CRÉÉE : instance 59079406", False),
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
    assert r.returncode == {"CRÉÉE": 0, "CRÉATION INCERTAINE": 4, "NON PARVENUE": 3, "OFFRE RETIRÉE": 7}[attendu.split(" :")[0].split(" (")[0]]
    assert not f.exists()                                                     # sortie brute effacée (point 16)


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
    assert '> "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v11.sh apres-creation "$F" \\$?' in suite
    assert 'git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v11.sh"' in suite and "cat scripts/amorce" not in t
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
    lignes = [l.split() for l in (r_ / "sparks-v5-demarrages.txt").read_text().splitlines()]
    assert [l[0] for l in lignes] == ["p", "d", "p", "d"] and lignes[0][2] == "5"          # redémarrage (5 min), puis phase
    assert lignes[0][1] == lignes[1][1] != lignes[2][1] == lignes[3][1] and int(lignes[3][2]) <= 2


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
    ("starting instance 7.", "start", 0, "ENVOYÉ"),
    ("destroying instance 7.", "destroy", 0, "ENVOYÉ"),
    ("Instance 7 is not in a stopped state.", "start", 5, "REFUSÉ"),          # point 15 : refus de Vast en HTTP 200
    ("starting instance 77.", "start", 5, "REFUSÉ"),                           # autre identifiant
    ("Starting instance 7.", "start", 5, "REFUSÉ"),
])
def test_lanceur_apres_commande(tmp_path, sortie, quoi, code, att):
    f = tmp_path / "s.txt"
    f.write_text(sortie + "\nSECRET\n")
    r = _lanceur(tmp_path, "apres-commande", quoi, str(f), "0", "7")
    assert r.returncode == code and att in r.stdout and "SECRET" not in r.stdout and "vastai show instances --raw" in r.stdout
    assert not f.exists()


@pytest.mark.parametrize("sortie,att,code,etat", [
    ('[{"id": 7, "actual_status": "exited", "cur_state": "stopped", "extra_env": {"GH_TOKEN": "SECRET"}}]', "exited", 0, "exited"),
    ('[{"id": 7, "actual_status": "running"}]', "absente", 6, "running"),
    ('[{"id": 8, "actual_status": "running"}]', "absente", 0, "absente"),
    ('[]', "absente", 0, "absente"),
    ('{"instances": null}', "absente", 0, "absente"),
    ('{"instances": [{"id": 7, "actual_status": "loading"}]}', "running", 6, "loading"),
    ('[{"id": 7, "actual_status": null}]', "absente", 6, "en_creation"),
    ('[{"id": 1404, "actual_status": "running"}, {"id": 7, "actual_status": 404}]', "absente", 6, "illisible"),
    ('[{"id": "7", "actual_status": "exited"}]', "exited", 6, "illisible"),
    ("failed with error 404: no_such_instance", "absente", 6, "illisible"),        # point 10 : aucun motif 404 non ancré
    ('{"error": true, "status_code": 404, "msg": "not found"}', "absente", 6, "illisible"),
    ('[{"id": 7, "actual_status": "exited"}] et du texte', "exited", 6, "illisible"),
    ("rien de lisible", "absente", 6, "illisible"),
])
def test_lanceur_inventaire(tmp_path, sortie, att, code, etat):
    f = tmp_path / "i.json"
    f.write_text(sortie)
    (tmp_path / "i.json.err").write_text("SECRET-ERR")
    r = _lanceur(tmp_path, "inventaire", str(f), "7", att)
    assert r.returncode == code and re.search(f"état {etat}[ ,]", r.stdout) and "SECRET" not in r.stdout + r.stderr, r.stdout
    assert not f.exists() and not (tmp_path / "i.json.err").exists()
    assert (tmp_path / "etat" / "etats-7.txt").read_text().split()[1:3] == ["7", etat]


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
    r = subprocess.run(["git", "-C", str(RACINE), "log", "-1", "--format=%H", "--", "src/controle_ia/sparks_exp7_nul_v11/liste-fermee-v1.txt"],
                       capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", r.stdout.strip()) else None


OFFRES = [{"id": 5, "resource_type": "gpu", "num_gpus": 1, "dph_total": 0.3, "storage_cost": 0.15, "rentable": True},
          {"id": 3, "resource_type": "disk", "num_gpus": 0, "dph_total": 0.01, "storage_cost": 0.1},
          {"id": 4, "resource_type": "gpu", "num_gpus": 2, "dph_total": 0.05, "storage_cost": 0.1},
          {"id": 9, "resource_type": "gpu", "num_gpus": 1, "dph_total": 0.2, "storage_cost": 0.2, "ssh_key": "SECRET"}]
GO_TIR = "| id | a | b | c | d | e | f | g |\n| GO-2026-11-05-09 | 2026-11-05 | calcul | SPARKS-EXP7-NUL tir réel | 5 USD | 2026-11-06 | Lazar | mot |\n"


def _offres_retenues(tmp_path, offres=OFFRES) -> subprocess.CompletedProcess:
    f = tmp_path / "brut.json"
    f.write_text(json.dumps(offres))
    return _lanceur(tmp_path, "offres", str(f))


def test_lanceur_mode_tir_commande_ecrite(tmp_path):
    if subprocess.run(["git", "-C", str(RACINE), "rev-parse", "HEAD"], capture_output=True).returncode != 0:
        pytest.skip("hors d'un dépôt git (copie du banc)")
    code = _commit_du_code()
    if code is None:
        pytest.skip("liste fermée v9 écrite au commit final")
    reg = tmp_path / "go.md"
    reg.write_text(GO_TIR)
    assert _offres_retenues(tmp_path).returncode == 0
    r = _lanceur(tmp_path, "tir", code, "GO-2026-11-05-09", "25", "2", SPARKS_REGISTRE_GO=str(reg), SPARKS_DATE_TIR="2026-11-05")
    assert r.returncode == 0, r.stderr
    t = r.stdout
    assert "TIR CONFORME : offre 5 (rang 2), PRIX_CARTE 0.3, PRIX_STOCKAGE 0.00411" in t
    assert "vastai create instance 5 " in t and "-e PRIX_HEURE_USD=0.3 -e PRIX_STOCKAGE_HEURE_USD=0.00411" in t
    assert "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" in t and "$GH_TOKEN" not in t and "HF_TOKEN" not in t
    assert "--label sparks-exp7-nul-tir-" in t and "GO_ID=GO-2026-11-05-09 timeout -k 10 300" in t and "--disk 20" in t
    assert f"apres-creation" in t and f"$? {code} GO-2026-11-05-09 25 2" in t
    assert 'git show "' + code + ':scripts/amorce_instance_sparks_exp7_nul_v11.sh"' in t
    assert t.count("vastai show instances --raw") == 2 and "vastai show instance " not in t and "lancer_sparks_exp7_nul_v11.sh boucle $ID" in t
    assert "vastai logs $ID --tail 400" in t and '/tir-logs-1.txt" 1' in t and '/tir-logs-2.txt" 2' in t and "grep -E '^AMORCE" not in t
    assert "-e MODE=jouet -e JOUET_MACHINE=1 -e JOUET_FABRICATION_S=60 -e AMORCE_ATTENTE_FIN_S=180" in t and "DEMARRAGES=2, BOUCLE=non" in t
    assert "addendum_factice.py" in t and "'/prereg/SPARKS-EXP7-NUL-*'" in t and "ARRÊT OBTENU" in t and "vastai start instance $ID" in t
    r2 = _lanceur(tmp_path, "tir", code, "GO-2026-11-05-09", "25", "1", SPARKS_REGISTRE_GO=str(reg), SPARKS_DATE_TIR="2026-11-07")
    assert r2.returncode == 2 and "validité" in r2.stderr
    r3 = _lanceur(tmp_path, "tir", code, "GO-2026-11-05-09", "25", "3", SPARKS_REGISTRE_GO=str(reg), SPARKS_DATE_TIR="2026-11-05")
    assert r3.returncode == 2 and "pas d'offre au rang 3" in r3.stderr
    reg.write_text(GO_TIR.replace("SPARKS-EXP7-NUL tir réel", "sonde v10 d'A1-v3"))
    r4 = _lanceur(tmp_path, "tir", code, "GO-2026-11-05-09", "25", "1", SPARKS_REGISTRE_GO=str(reg), SPARKS_DATE_TIR="2026-11-05")
    assert r4.returncode == 2 and "« SPARKS » et « tir » exigés" in r4.stderr


def test_amorce_v5_ordre_des_gardes_et_consignations():
    t = AMORCE.read_text(encoding="utf-8")
    creation = t[t.index('echo "AMORCE V5 : création"'):t.index('echo "AMORCE V5 : redémarrage"')]
    i_code, i_add = creation.index("import garde_code;"), creation.index("addendum_reconnu ||")
    i_ok, i_cons = creation.index('"$R/sparks-v5-gardes-ok"'), creation.index('consigner_demarrage "$MINUTES"')
    i_lance = creation.index("sparks_exp7_nul_instance_v11.sh")
    assert i_code < i_add < i_ok < i_cons < i_lance and "consigner_fin" in creation[i_lance:]
    copie = t[t.index("    copie)"):t.index("    causal)")]
    assert copie.index('consigner_demarrage "$((CM + 5))"') < copie.index("redemarrage.py\" lot") and "consigner_fin" in copie
    causal = t[t.index("    causal)"):]
    assert causal.index('consigner_demarrage "$MINUTES"') < causal.index("sparks_exp7_nul_instance_v11.sh") < causal.index("consigner_fin")


def test_lanceur_tir_statique():
    t = LANCEUR.read_text(encoding="utf-8")
    bloc = t[t.index('if [ "$QUOI" = tir ]; then'):t.index("    exit 0\nfi")]
    ligne = [l for l in bloc.splitlines() if "vastai create instance" in l][0]
    assert ligne.startswith("GO_ID=$GOT timeout -k 10 300 $(prefixe_env) vastai create instance $OFFRE") and "--disk 20" in ligne
    assert "--label sparks-exp7-nul-tir-$COURT" in ligne and "HF_TOKEN" not in bloc
    assert 'L=$(timeout 120 python3 -I -B "$P9/tir.py" verifier' in bloc and "garde_code; sys.exit(garde_code.main(sys.argv[1:]))\" liste" in bloc
    assert "inventaire_cmd '$ID' absente" in bloc and "inventaire_cmd '$ID' exited" in bloc and "-e MODE=jouet -e JOUET_MACHINE=1" in bloc
    assert "sparks_exp7_nul_v8/addendum_factice.py" in bloc and "'/prereg/SPARKS-EXP7-NUL-*'" in bloc
    assert "-e GH_TOKEN=\\$CONTROLE_IA_GITHUB_TOKEN" in bloc and "GH_TOKEN=\\$GH_TOKEN" not in t     # point 12 : jeton écrit
    assert t.count("-e GH_TOKEN=\\$CONTROLE_IA_GITHUB_TOKEN") == 2


def test_v11_scripts_garde_v11_essais_v11_et_date_du_tir():
    a = AMORCE.read_text(encoding="utf-8")
    assert "sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v11'); import garde_code;" in a and a.count("sparks_exp7_nul_instance_v11.sh") == 2
    assert "'$P5'); import garde_code" not in a and "sparks_exp7_nul_instance_v5.sh" not in a
    i = (RACINE / "scripts" / "sparks_exp7_nul_instance_v11.sh").read_text(encoding="utf-8")
    l = [x for x in i.splitlines() if "-m pytest" in x][0]
    assert "tests/test_sparks_exp7_nul_v11.py" in l and "test_sparks_exp7_nul_v5.py" not in l
    assert "sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v11'); import garde_code;" in i
    t = LANCEUR.read_text(encoding="utf-8")
    assert '"$P9/tir.py" verifier "$REG" "$GOT" "$PRIX" "$STOCK" "$MIN" ${SPARKS_DATE_TIR:+"$SPARKS_DATE_TIR"})' in t
    assert t.count("sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v11'); import garde_code;") == 2
    assert "amorce_instance_sparks_exp7_nul_v5.sh" not in t and "lancer_sparks_exp7_nul_v5.sh" not in t


# --- 5. de la v7 : appels de modules sous -I (répétition v6), sur le script v8 ---------------------------------------------
INSTANCE = RACINE / "scripts" / "sparks_exp7_nul_instance_v11.sh"


def _bloc_module() -> tuple[str, str]:
    """Définition de `SRC` et de la fonction `module`, et la ligne de l'essai d'égalité des lots, tirées du script v8."""
    t = INSTANCE.read_text(encoding="utf-8").splitlines()
    i = next(k for k, l in enumerate(t) if l.startswith('SRC="$PWD/src"'))
    j = next(k for k in range(i, len(t)) if t[k] == "}")
    egal = next(l for l in t if "egalite-lots" in l and not l.lstrip().startswith("#"))
    return "\n".join(t[i:j + 1]), egal


def _env_sans_pythonpath(tmp_path) -> dict:
    import sys
    return {"PATH": f"{Path(sys.executable).parent}:/usr/sbin:/usr/bin:/sbin:/bin", "HOME": str(tmp_path)}


def test_script_d_instance_trouve_le_paquet_sous_isolement(tmp_path):
    """Joue, depuis le script v8, la définition de `module` et le premier appel (essai d'égalité des lots), hors de tout
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


def test_aucun_appel_python_isole_par_module_sans_chemin():
    t = INSTANCE.read_text(encoding="utf-8")
    assert not re.search(r"python3? (-u )?-I -B -m controle_ia", t)
    assert len(re.findall(r"^\s*(?:if \[ \"\$MODE\" = jouet \]; then |else )?module controle_ia\.", t, re.M)) == 6
    assert "<<'PY'" not in t and "creer_manifeste" not in t


# --- 6. neuf en v8 : manifeste de chaque phase, addendum scellé cité comme préenregistrement (répétition v7) -------------
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import creer_manifeste  # noqa: E402
from controle_ia.prereg import problemes  # noqa: E402
from controle_ia.sparks_exp7_nul_v8 import addendum_factice, manifeste_phase  # noqa: E402

CODE_FICTIF = "0123456789abcdef0123456789abcdef01234567"
PARENT = "prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md"
ADDENDUM = "prereg/SPARKS-EXP7-NUL-addendum-1.md"


def _lignes_manifeste() -> str:
    """L'appel du manifeste tiré du script v8 (de `module …manifeste_phase` à la fin de son `|| { … }`)."""
    t = INSTANCE.read_text(encoding="utf-8").splitlines()
    i = next(k for k, l in enumerate(t) if l.startswith("module controle_ia.sparks_exp7_nul_v8.manifeste_phase "))
    j = next(k for k in range(i, len(t)) if t[k].rstrip().endswith("}"))
    return "\n".join(t[i:j + 1])


def _depot_parent(tmp_path) -> Path:
    """Dépôt neuf au commit « parent » : le texte parent scellé seul (copié du dépôt, inchangé)."""
    d = tmp_path / "depot"
    (d / "prereg").mkdir(parents=True)
    for f in (PARENT, PARENT + ".sha256"):
        shutil.copy2(RACINE / f, d / f)
    _git(d, "init", "-q", "-b", "main")
    _git(d, "add", "-A")
    _git(d, "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-q", "-m", "parent")
    return d


def _enfant(d: Path, texte: str | None = None, factice: bool = False) -> str:
    """Commit enfant qui ajoute l'addendum scellé (factice marqué, ou le texte donné) et son compagnon."""
    p = d / ADDENDUM
    if factice:
        addendum_factice.ecrire(p, CODE_FICTIF)
    else:
        p.write_text(texte, encoding="utf-8")
        import hashlib
        (d / (ADDENDUM + ".sha256")).write_text(f"{hashlib.sha256(texte.encode()).hexdigest()}  {p.name}\n", encoding="utf-8")
    _git(d, "add", "-A")
    _git(d, "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-q", "-m", "enfant : addendum")
    return _git(d, "rev-parse", "HEAD")


def _jouer_manifeste(tmp_path, d: Path, mode: str, run: str = "fabrication") -> tuple[subprocess.CompletedProcess, str]:
    """Joue, tirés du script v8, `SRC`, `module` et l'appel du manifeste, dans le dépôt `d`, hors de tout PYTHONPATH."""
    bloc, _ = _bloc_module()
    j = tmp_path / f"journal-{mode}-{run}.txt"
    run_id = f"20261105-020000-sparks-exp7-nul-v5-{run}"
    script = (f'set -euo pipefail\ncd "{RACINE}"\n{bloc}\ncd "{d}"\nJOURNAL="{j}"\n'
              f'journal() {{ printf "%s\\n" "$*" >> "$JOURNAL"; }}\n'
              f'RUN_ID={run_id}\nDEPART=jouet\nHTTP=sans-objet\nPHASE=fabrication\nCOMMIT_CODE={CODE_FICTIF}\nLOTS=oui\n'
              f'MODE={mode}\n{_lignes_manifeste()}\necho "MANIFESTE_PASSE"\n')
    r = subprocess.run(["bash", "-c", script], env=_env_sans_pythonpath(tmp_path), capture_output=True, text=True, timeout=600)
    return r, (j.read_text(encoding="utf-8") if j.exists() else "")


def _addendum_reel_conforme() -> str:
    """Un addendum conforme sans la marque factice (forme de l'addendum réel scellé)."""
    t = addendum_factice.texte(CODE_FICTIF)
    return t.replace(f"# {addendum_factice.MARQUE}", "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL (essai)")


def test_temoin_le_texte_parent_n_est_pas_conforme_a_exiger_prereg():
    """Témoin de la répétition v7 : le texte parent scellé, inchangeable, n'a pas les deux empreintes à sa « Contre-lecture »."""
    assert any("deux empreintes" in p for p in problemes(RACINE / PARENT))


def test_manifeste_texte_parent_seul_refuse_sur_le_commit_parent(tmp_path):
    """Artefact : le commit parent (texte parent seul, aucun addendum) ; le manifeste est refusé, code 2, rien de créé."""
    d = _depot_parent(tmp_path)
    r, journal = _jouer_manifeste(tmp_path, d, "jouet")
    assert r.returncode == 2 and "MANIFESTE_PASSE" not in r.stdout, (r.stdout, r.stderr)
    assert "MANIFESTE REFUSÉ" in journal and "texte parent seul ne gouverne pas" in journal, journal
    assert "manifeste refusé (addendum scellé exigé) : arrêt avant tout calcul" in journal
    assert not (d / "runs").exists()
    with pytest.raises(GardeArret, match="deux empreintes"):          # l'appel de la v7 (texte parent cité) : même refus
        creer_manifeste(d, "20261105-020000-sparks-v7-temoin", {}, ["t"], decisif=True, prereg=d / PARENT)


def test_manifeste_cree_sur_le_commit_enfant_addendum_factice_en_jouet(tmp_path):
    """Cas sain (répétition) : commit enfant avec l'addendum factice marqué ; en mode jouet le manifeste est créé et cite
    l'addendum comme préenregistrement, le texte parent par son sceau ; hors du mode jouet, refus."""
    d = _depot_parent(tmp_path)
    enfant = _enfant(d, factice=True)
    assert problemes(d / ADDENDUM) == []
    r, journal = _jouer_manifeste(tmp_path, d, "jouet")
    assert r.returncode == 0 and r.stdout.strip().endswith("MANIFESTE_PASSE"), (r.stdout, r.stderr, journal)
    assert "MANIFESTE CRÉÉ" in journal and "ADDENDUM FACTICE (jouet)" in journal
    m = json.loads((d / "runs" / "20261105-020000-sparks-exp7-nul-v5-fabrication" / "manifeste.json").read_text(encoding="utf-8"))
    import hashlib
    assert m["preenregistrement"] == {"chemin": ADDENDUM, "sha256": hashlib.sha256((d / ADDENDUM).read_bytes()).hexdigest()}
    assert m["config"]["texte_parent"] == {"chemin": PARENT, "sha256": plan.SHA_PREREG}
    assert m["config"]["addendum_factice"] is True and m["config"]["mode"] == "jouet" and m["commit"] == enfant
    assert m["decisif"] is True and m["config"]["commit_code"] == CODE_FICTIF
    r2, journal2 = _jouer_manifeste(tmp_path, d, "reel", run="causal")
    assert r2.returncode == 2 and "addendum factice de répétition hors du mode jouet" in journal2, journal2


def test_manifeste_cree_en_reel_avec_un_addendum_conforme_non_factice(tmp_path):
    d = _depot_parent(tmp_path)
    _enfant(d, texte=_addendum_reel_conforme())
    r, journal = _jouer_manifeste(tmp_path, d, "reel")
    assert r.returncode == 0, (r.stderr, journal)
    m = json.loads((d / "runs" / "20261105-020000-sparks-exp7-nul-v5-fabrication" / "manifeste.json").read_text(encoding="utf-8"))
    assert m["preenregistrement"]["chemin"] == ADDENDUM and m["config"]["addendum_factice"] is False


@pytest.mark.parametrize("quoi, attendu", [
    ("sans_empreintes", "deux empreintes"),
    ("sans_commit", "n'y est pas cité en entier"),
    ("sans_hypothese", "section absente : Hypothèse"),
    ("non_scelle", "compagnon|empreinte|sceau|absent"),
])
def test_manifeste_refuse_un_addendum_non_conforme(tmp_path, quoi, attendu):
    d = _depot_parent(tmp_path)
    t = _addendum_reel_conforme()
    if quoi == "sans_empreintes":
        t = re.sub(r"`[0-9a-f]{64}`", "`abrégé…`", t)
    elif quoi == "sans_commit":
        t = t.replace(CODE_FICTIF, CODE_FICTIF[:12] + "…")
    elif quoi == "sans_hypothese":
        t = t.replace("## Hypothèse\n", "## Hypothèses du texte v1\n")
    _enfant(d, texte=t)
    if quoi == "non_scelle":
        (d / (ADDENDUM + ".sha256")).write_text("0" * 64 + "  SPARKS-EXP7-NUL-addendum-1.md\n", encoding="utf-8")
        _git(d, "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-qam", "sceau faux")
    r, journal = _jouer_manifeste(tmp_path, d, "reel")
    assert r.returncode == 2 and "MANIFESTE REFUSÉ" in journal and re.search(attendu, journal), journal
    assert not (d / "runs").exists()


def test_manifeste_refuse_un_texte_parent_altere(tmp_path):
    d = _depot_parent(tmp_path)
    p = d / PARENT
    p.write_text(p.read_text(encoding="utf-8") + "\najout\n", encoding="utf-8")
    import hashlib
    (d / (PARENT + ".sha256")).write_text(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n", encoding="utf-8")
    _git(d, "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-qam", "parent resscellé")
    _enfant(d, factice=True)
    r, journal = _jouer_manifeste(tmp_path, d, "jouet")
    assert r.returncode == 2 and "empreinte gelée" in journal, journal


def test_addendum_factice_marque_conforme_et_sans_ecrasement(tmp_path):
    p = tmp_path / "a.md"
    h = addendum_factice.ecrire(p, CODE_FICTIF)
    t = p.read_text(encoding="utf-8")
    assert t.startswith(f"# {addendum_factice.MARQUE}") and CODE_FICTIF in t and problemes(p) == []
    assert (tmp_path / "a.md.sha256").read_text() == f"{h}  a.md\n"
    cl = t[t.index("## Contre-lecture"):]
    assert addendum_factice.EMPREINTE_BROUILLON in cl and addendum_factice.EMPREINTE_RAPPORT in cl and "factice" in cl
    with pytest.raises(FileExistsError):
        addendum_factice.ecrire(p, CODE_FICTIF)
    with pytest.raises(ValueError):
        addendum_factice.texte("abc")


def test_v11_scripts_instance_v11_essais_v11_manifeste_v8():
    a = AMORCE.read_text(encoding="utf-8")
    assert a.count("sparks_exp7_nul_instance_v11.sh") == 2 and "sparks_exp7_nul_instance_v10.sh" not in a
    i = INSTANCE.read_text(encoding="utf-8")
    l = [x for x in i.splitlines() if "-m pytest" in x][0]
    assert "tests/test_sparks_exp7_nul_v11.py" in l and "test_sparks_exp7_nul_v10.py" not in l
    m = _lignes_manifeste()
    assert '"$RUN_ID" "$DEPART" "$HTTP" "$PHASE" "$COMMIT_CODE" "$LOTS" "$MODE"' in m and "exit 2" in m
    assert i.index("module controle_ia.sparks_exp7_nul_v8.manifeste_phase") < i.index('SORTIE="$TRAVAIL/sortie"')
    t = LANCEUR.read_text(encoding="utf-8")
    assert t.count("amorce_instance_sparks_exp7_nul_v11.sh") == 2 and "amorce_instance_sparks_exp7_nul_v10.sh" not in t


# --- 7. neuf en v9 : protocole du tir (contre-lecture du delta v8, points 5, 10 à 19, 31) et boucle détectée par l'amorce --
from controle_ia.sparks_exp7_nul_v9 import tir as tir9  # noqa: E402
from controle_ia.sparks_exp7_nul_v10 import vast_lecture  # noqa: E402


def test_offres_filtrees_prix_tires_de_l_offre_et_brut_efface(tmp_path):
    r = _offres_retenues(tmp_path, OFFRES + [dict(OFFRES[0], id=20 + k, dph_total=0.4 + k / 10) for k in range(4)])
    assert r.returncode == 0 and "SECRET" not in r.stdout and not (tmp_path / "brut.json").exists()
    d = json.loads((tmp_path / "etat" / "offres-retenues.json").read_text())
    assert [o["id"] for o in d["offres"]] == [9, 5, 20, 21]                # gpu, une carte, prix croissant, au plus 4
    o = d["offres"][0]
    assert o["prix_carte"] == 0.2 and o["prix_stockage_heure"] == pytest.approx(0.2 * 20 / 730, abs=1e-6)
    assert set(o) == {"rang", "id", "dph_total", "storage_cost", "resource_type", "prix_carte", "prix_stockage_heure"}
    vide = _offres_retenues(tmp_path, [OFFRES[1], OFFRES[2]])
    assert vide.returncode == 9 and "AUCUNE OFFRE CONFORME" in vide.stdout
    f = tmp_path / "brut.json"
    f.write_text('{"offers": []}')
    assert _lanceur(tmp_path, "offres", str(f)).returncode == 2 and not f.exists()


@pytest.mark.parametrize("etats,verdict,code", [
    ([(0, "exited", "stopped"), (150, "exited", "stopped"), (310, "exited", "stopped")], "arretee", 0),
    ([(0, "exited", "stopped"), (150, "exited", "stopped"), (200, "exited", "stopped")], "indecis", 6),   # < 5 min
    ([(0, "exited", "stopped"), (310, "exited", "stopped")], "indecis", 6),                               # deux lectures
    ([(0, "exited", "stopped"), (150, "running", "running"), (310, "exited", "stopped")], "boucle", 8),  # relancée entre deux
    ([(0, "running", "running"), (150, "exited", "stopped"), (310, "running", "running")], "boucle", 8),
    ([(0, "exited", "running"), (150, "exited", "running"), (310, "exited", "running")], "boucle", 8),   # relance prévue
    ([(0, "loading", "running"), (150, "exited", "stopped"), (320, "absente", "-")], "absente", 0),
    ([(0, "exited", "stopped"), (150, "illisible", "-"), (310, "exited", "stopped")], "boucle", 8),
])
def test_verdict_de_boucle_sur_trois_lectures(tmp_path, etats, verdict, code):
    (tmp_path / "etat").mkdir()
    (tmp_path / "etat" / "etats-7.txt").write_text("".join(f"{1000 + s} 7 {e} {c}\n" for s, e, c in etats) + "1400 8 running running\n")
    r = _lanceur(tmp_path, "boucle", "7")
    assert r.returncode == code and f"verdict {verdict}" in r.stdout, r.stdout
    assert ("vastai destroy instance 7 -y" in r.stdout and "NŒUD" in r.stdout) == (verdict == "boucle")


def test_inventaires_successifs_alimentent_le_verdict(tmp_path):
    f = tmp_path / "i.json"
    for k in range(3):
        f.write_text('[{"id": 7, "actual_status": "exited", "cur_state": "stopped"}]')
        _lanceur(tmp_path, "inventaire", str(f), "7", "exited")
    lignes = (tmp_path / "etat" / "etats-7.txt").read_text().splitlines()
    assert len(lignes) == 3 and all(l.split()[1:] == ["7", "exited", "stopped"] for l in lignes)
    assert vast_lecture.boucle(tmp_path / "etat" / "etats-7.txt", 7) == "indecis"      # trois lectures en moins de 5 min


def test_journal_amorce_sans_ancre_et_brut_efface(tmp_path):
    f = tmp_path / "logs.txt"
    f.write_text("2026-11-05T05:00:00Z AMORCE V5 2026-11-05T05:00:00Z : machine 7, commit x\nGH_TOKEN=SECRET\n"
                 "[conteneur] AMORCE V5 : redémarrage\nAMORCE V5 : redémarrage consigné au registre des démarrages : démarrage n° 1\n"
                 "AMORCE V5 : ordres illisibles (ou délai) : boucle de redémarrage présumée, destruction immédiate\n")
    r = _lanceur(tmp_path, "journal-amorce", str(f))
    assert r.returncode == 0 and "SECRET" not in r.stdout and not f.exists()
    assert "REDEMARRAGES=2 BOUCLE_PRESUMEE=1" in r.stdout and r.stdout.count("AMORCE V5") == 4


def test_tir_v9_perimetre_sparks_et_tir(tmp_path):
    from datetime import date
    p = tmp_path / "go.md"
    j = date(2026, 11, 5)
    for perim, bon in (("SPARKS-EXP7-NUL tir réel", True), ("tir de SPARKS", True), ("sonde v10 d'A1-v3", False),
                       ("SPARKS-EXP7-NUL, variante carte", False), ("SPARKS tirage", False), ("sparks tir", False)):
        p.write_text(GO_TIR.replace("SPARKS-EXP7-NUL tir réel", perim))
        if bon:
            assert tir9.preparer(p, "GO-2026-11-05-09", 0.8, 0.05, 25, j, maintenant_s=0)["echeance_utc_s"] == 1500
        else:
            with pytest.raises(tir9.GardeTir, match="« SPARKS » et « tir » exigés"):
                tir9.preparer(p, "GO-2026-11-05-09", 0.8, 0.05, 25, j)


def test_apres_creation_no_such_ask_offre_suivante_au_plus_quatre(tmp_path):
    f = tmp_path / "s.txt"
    for rang, attendu in (("1", "tir " + "a" * 40 + " GO-2026-11-05-09 25 2"), ("3", "GO-2026-11-05-09 25 4"), ("4", "nouvelle recherche")):
        f.write_text("failed with error 404/3603: no_such_ask\n")
        r = _lanceur(tmp_path, "apres-creation", str(f), "0", "a" * 40, "GO-2026-11-05-09", "25", rang)
        assert r.returncode == 7 and attendu in r.stdout and not (tmp_path / "etat" / ".creation-incertaine").exists()


def _boucle_sur_le_disque(tmp_path, depot, **kw):
    """Création refusée après le clone (plafond trop bas), puis relance des mêmes arguments sur le même disque : une boucle."""
    d, c = depot
    code1, out1, r_, _ = _amorce(tmp_path, d, c, DEJA_USD="39.99")
    _arreter_minuteries(r_)
    assert code1 == 2 and "plafond trop bas" in out1 and "refus avant l'ordre consommé" in out1 and "DELETE instance 123456" in _journal(r_)
    (r_ / "sparks-v5-detruire").unlink()                          # destruction supposée sans effet : Vast relance le conteneur
    (r_ / "sparks-v5-minuterie.log").unlink()
    code2, out2, _, _ = _amorce(tmp_path, d, c, DEJA_USD="39.99", **kw)
    _arreter_minuteries(r_)
    return code2, out2, r_


def test_boucle_apres_une_creation_refusee_destruction_immediate(tmp_path, depot):
    code, out, r_ = _boucle_sur_le_disque(tmp_path, depot)
    assert code == 2 and "AMORCE V5 : redémarrage" in out and "démarrage n° 1" in out
    assert "ordres illisibles (ou délai) : boucle de redémarrage présumée, destruction immédiate" in out
    assert "DELETE instance 123456" in _journal(r_) and "redémarrage sans ordre neuf" in (r_ / "sparks-v5-detruire").read_text()
    lignes = [l.split() for l in (r_ / "sparks-v5-demarrages.txt").read_text().splitlines()]
    assert [l[0] for l in lignes] == ["p", "d"] and lignes[0][2] == "5"        # le redémarrage compte à la borne


def test_temoin_sans_detection_la_boucle_attend_l_echeance(tmp_path, depot):
    t = AMORCE.read_text(encoding="utf-8").replace('    detruire "redémarrage sans ordre neuf ($1)" 2; }', '    exit 2; }')
    s = tmp_path / "amorce-sans-detection.sh"
    s.write_text(t)
    code, out, r_ = _boucle_sur_le_disque(tmp_path, depot, script=s)
    assert code == 2 and "boucle de redémarrage présumée" in out and "DELETE" not in _journal(r_)


def test_creation_relancee_sans_depot_extrait_est_une_boucle(tmp_path, depot):
    d, c = depot
    code1, out1, r_, _ = _amorce(tmp_path, d, c, git_bloque=True, AMORCE_T_GIT_S=3, timeout=60)
    _arreter_minuteries(r_)
    assert code1 == 2 and "clonage impossible" in out1 and (r_ / "sparks-v9-creation-tentee").exists()
    assert "DELETE instance 123456" in _journal(r_)                # v10 : le refus détruit
    (r_ / "sparks-v5-detruire").unlink()
    (r_ / "sparks-v5-minuterie.log").unlink()
    code2, out2, _, _ = _amorce(tmp_path, d, c, git_bloque=True, AMORCE_T_GIT_S=3, timeout=60)
    _arreter_minuteries(r_)
    assert code2 == 2 and "création déjà tentée sur ce disque" in out2 and "DELETE instance 123456" in _journal(r_)
    assert "clonage impossible" not in out2


def test_ordre_fin_avant_la_borne(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 1, "instance": ID, "phase": "fin", "deja_usd": 0}])
    r_ = _disque(tmp_path, d, c)
    code, out, _, _ = _amorce(tmp_path, d, c, PRIX_HEURE_USD="x")              # borne illisible : la fin passe quand même
    _arreter_minuteries(r_)
    assert code == 0 and "destruction demandée (ordre 1 : fin)" in out and "DELETE instance 123456" in _journal(r_)
    assert (r_ / "sparks-v5-ordres-faits.txt").read_text().split() == ["1", "0.0"]


def test_ordre_consomme_avant_la_borne_ne_se_rejoue_pas(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 1, "instance": ID, "phase": "copie", "deja_usd": 0.0, "cas": ["vraie01"], "premier": False,
                    "copie_minutes": 5}])
    r_ = _disque(tmp_path, d, c)
    code, out, _, _ = _amorce(tmp_path, d, c, PRIX_HEURE_USD="x")
    _arreter_minuteries(r_)
    assert code == 2 and "borne de la machine illisible : aucun calcul (ordre 1 consommé)" in out and "DELETE" not in _journal(r_)
    code2, out2, _, _ = _amorce(tmp_path, d, c, PRIX_HEURE_USD="x")              # la même relance : plus d'ordre neuf
    _arreter_minuteries(r_)
    assert code2 == 2 and "boucle de redémarrage présumée" in out2 and "DELETE instance 123456" in _journal(r_)


def test_fin_causale_message_exact_code_et_poussee(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 3, "instance": ID, "phase": "causal", "deja_usd": 10.0}], causal=True)
    r_ = _disque(tmp_path, d, c)
    inst = r_ / "amorce-depot" / "scripts" / "sparks_exp7_nul_instance_v11.sh"
    inst.write_text('#!/bin/bash\nmkdir -p "$TRAVAIL"; echo tete > "$TRAVAIL/POUSSEE-VERIFIEE"\nexit 1\n')
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    assert code == 1 and "fin de la phase causale, code 1, poussée vérifiée" in out and "sans poussée vérifiée" not in out
    assert "phase causale en code 1, poussée vérifiée : pas de destruction" in out and "DELETE" not in _journal(r_)


def test_redemarrage_aucun_exit_avant_l_ordre_consomme():
    t = AMORCE.read_text(encoding="utf-8")
    avant = t[t.index('echo "AMORCE V5 : redémarrage"\n'):t.index('if [ "$PHASE_O" = fin ]; then')]
    assert "exit" not in avant and avant.count("|| boucle ") >= 5 and "trap fin_lancement EXIT" in avant
    assert avant.index('redemarrage.py" demarrage "$REG" "$ID_L" 5') < avant.index("git -C \"$R/amorce-depot\" rev-parse HEAD")
    assert avant.index('redemarrage.py" fait') < len(avant)


def test_lecture_efface_chaque_sortie_brute_meme_illisible(tmp_path):
    for k, (quoi, contenu) in enumerate((("inventaire", "[]"), ("inventaire", "illisible"), ("offres", "[]"), ("offres", "x"),
                                          ("journal-amorce", "AMORCE V5 : x"))):
        f = tmp_path / f"b{k}.json"
        f.write_text(contenu)
        (tmp_path / f"b{k}.json.err").write_text("SECRET")
        if quoi == "inventaire":
            vast_lecture.inventaire(f, 7)
        elif quoi == "offres":
            try:
                vast_lecture.offres(f, tmp_path / "r.json")
            except vast_lecture.Illisible:
                pass
        else:
            vast_lecture.journal_amorce(f)
        assert not f.exists() and not (tmp_path / f"b{k}.json.err").exists(), quoi


def test_identifiants_de_demarrage_jamais_reutilises(tmp_path):
    """Répétition locale v9, run 3 : deux démarrages dans la même seconde avaient le même identifiant ; le registre
    écrasait le plafond de l'un (borne sous-estimée)."""
    f = _fonction("nouvel_id")
    reg = tmp_path / "reg.txt"

    def jouer() -> int:
        r = subprocess.run(["bash", "-c", f'REG="{reg}"\n{f}nouvel_id\n'], capture_output=True, text=True, timeout=30)
        return int(r.stdout.strip())
    t0 = int(time.time())
    assert t0 <= jouer() <= t0 + 5                                        # registre absent : l'instant
    reg.write_text(f"p {t0 + 100} 5\nd {t0 + 100} 1\np {t0 + 50} 10\n")
    assert jouer() == t0 + 101                                            # jamais un identifiant déjà consigné
    reg.write_text("p 1 5\n")
    assert jouer() >= t0
    t = AMORCE.read_text(encoding="utf-8")
    assert "ID_L=$(nouvel_id)" in t and "ID_D=$(nouvel_id)" in t and "ID_D=$(date +%s)" not in t and "ID_L=$(date +%s)" not in t


def test_deux_redemarrages_dans_la_meme_seconde_restent_distincts(tmp_path, depot):
    d, c = depot
    _ordres(d, c, [{"numero": 1, "instance": ID, "phase": "copie", "deja_usd": 0.0, "cas": ["vraie01"], "premier": False,
                    "copie_minutes": 5}])
    r_ = _disque(tmp_path, d, c)
    futur = int(time.time()) + 1000
    (r_ / "sparks-v5-demarrages.txt").write_text(f"p {futur} 7\nd {futur} 3\n")     # identifiant le plus grand, dans le futur
    code, out, _, _ = _amorce(tmp_path, d, c)
    _arreter_minuteries(r_)
    lignes = [l.split() for l in (r_ / "sparks-v5-demarrages.txt").read_text().splitlines()]
    ids_p = [l[1] for l in lignes if l[0] == "p"]
    assert len(ids_p) == len(set(ids_p)) == 3 and ids_p[1] == str(futur + 1) and ids_p[2] == str(futur + 2), lignes



# --- 8. neuf en v10 : tir réel v9 (image sans curl, amorce sortie à chaque démarrage, plus de 110 relances) -----------------
def _sans(tmp_path, *exclus: str) -> Path:
    """Un dossier de commandes : tout /usr/bin, sauf `exclus` (une image sans curl ni git, par exemple)."""
    d = tmp_path / ("sans-" + "-".join(exclus))
    d.mkdir(exist_ok=True)
    for f in Path("/usr/bin").iterdir():
        if f.name not in exclus and not (d / f.name).exists():
            (d / f.name).symlink_to(f)
    return d


def _apt(tmp_path, reussit: bool) -> tuple[Path, Path]:
    """Faux `apt-get` : `install` lie le faux curl et le vrai git dans un dossier du chemin ; ou échoue (code 100)."""
    a, inst = tmp_path / "apt", tmp_path / "installe"
    a.mkdir(exist_ok=True)
    inst.mkdir(exist_ok=True)
    faux = _faux_bin(tmp_path)
    corps = (f'#!/bin/bash\necho "apt-get $*" >> "{tmp_path}/apt.log"\ncase "$*" in *install*) '
             f'ln -sf "{faux}/curl" "{inst}/curl"; ln -sf /usr/bin/git "{inst}/git";; esac\nexit 0\n') if reussit else \
        f'#!/bin/bash\necho "apt-get $*" >> "{tmp_path}/apt.log"\nexit 100\n'
    (a / "apt-get").write_text(corps)
    (a / "apt-get").chmod(0o755)
    return a, inst


def test_ligne_de_demarrage_horodatee_et_comptee(tmp_path, depot):
    d, c = depot
    sorties = []
    for k in range(2):
        code, out, r_, _ = _amorce(tmp_path, d, c, DEJA_USD="39.99")
        _arreter_minuteries(r_)
        sorties.append(out)
        assert code == 2 and re.search(rf"^AMORCE V10 DEMARRAGE {k + 1} : 20\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ, machine 123456, commit {c}$", out, re.M), out
        assert out.splitlines()[0].startswith(f"AMORCE V10 DEMARRAGE {k + 1} :")          # premier geste
        for f in ("sparks-v5-detruire", "sparks-v5-minuterie.log", "sparks-v9-creation-tentee"):
            (r_ / f).unlink(missing_ok=True)
        shutil.rmtree(r_ / "amorce-depot", ignore_errors=True)
    assert (r_ / "sparks-v10-demarrages-amorce.txt").read_text().strip() == "2"
    f = tmp_path / "logs.txt"
    f.write_text("\n".join(sorties))
    r = _lanceur(tmp_path, "journal-amorce", str(f), "1")
    assert r.returncode == 8 and "DEMARRAGES=2 ATTENDUS=1 BOUCLE=oui" in r.stdout and not f.exists()


def test_refus_a_la_creation_detruit_l_instance(tmp_path, depot):
    code, out, r_, _ = _amorce(tmp_path, *depot, DEJA_USD="39.99", AMORCE_ATTENTE_REFUS_S="1")
    _arreter_minuteries(r_)
    assert code == 2 and "plafond trop bas" in out and "refus avant l'ordre consommé : destruction de l'instance" in out
    assert "attente de 1 s avant la destruction" in out and "DELETE instance 123456" in _journal(r_)
    assert (r_ / "sparks-v5-detruire").read_text().startswith("refus : plafond trop bas")


@espace_processus
def test_destruction_non_obtenue_sleep_infinity_sans_boucler(tmp_path, depot):
    code, out, r_, _ = _amorce(tmp_path, *depot, espace=True, timeout=25, DEJA_USD="39.99", FAUX_HTTP="503", FAUX_VASTAI="1")
    assert code == "délai", (code, out)                                    # le conteneur ne sort pas : pas de relance
    assert "destruction non obtenue (minuterie, code 4) : sleep infinity pour ne pas boucler" in out
    assert "ALARME" in _journal(r_)


def test_attente_avant_destruction_bornee():
    t = AMORCE.read_text(encoding="utf-8")
    f = t[t.index("refus() {"):t.index("\n", t.index('detruire "refus : $1" 2; }'))]
    assert '[ "$a" -le 600 ] || a=600' in f and 'case "$a" in \'\'|*[!0-9]*) a=0;; esac' in f


@espace_processus
def test_image_sans_curl_ni_git_installes_par_apt_get(tmp_path, depot):
    a, inst = _apt(tmp_path, reussit=True)
    chemin = f"{inst}:{a}:{_sans(tmp_path, 'curl', 'git')}"
    code, out, r_, _ = _amorce(tmp_path, *depot, espace=True, DEJA_USD="39.99", PATH=chemin, AMORCE_T_APT_S="20")
    assert "outils absents : curl git : installation bornée (apt-get, 20 s par étape)" in out, out
    assert "installation (ca-certificates curl git) : code 0" in out and "AMORCE V5 : outils : curl oui, git oui" in out
    assert code == 2 and "plafond trop bas" in out and "DELETE instance 123456" in _journal(r_)
    log = (tmp_path / "apt.log").read_text()
    assert "update -qq" in log and "install -y -qq --no-install-recommends ca-certificates curl git" in log


@espace_processus
def test_image_sans_curl_ni_python3_installation_impossible_sleep_infinity(tmp_path, depot):
    a, _ = _apt(tmp_path, reussit=False)
    chemin = f"{a}:{_sans(tmp_path, 'curl', 'git', 'python3')}"
    code, out, r_, _ = _amorce(tmp_path, *depot, espace=True, timeout=25, PATH=chemin, AMORCE_T_APT_S="5")
    assert code == "délai", (code, out)
    assert "outils absents après installation : curl git python3 : refus avant l'ordre consommé : destruction immédiate" in out
    assert "destruction non obtenue (code 5) : sleep infinity pour ne pas boucler" in out
    assert "ni curl ni python3" in _journal(r_)


def test_minuterie_par_python3_si_curl_absent(tmp_path):
    import http.server
    import threading
    vu = []

    class H(http.server.BaseHTTPRequestHandler):
        def do_DELETE(self):
            vu.append((self.path, self.headers.get("Authorization")))
            corps = b'{"success": true}'
            self.send_response(200)
            self.send_header("Content-Length", str(len(corps)))
            self.end_headers()
            self.wfile.write(corps)

        def log_message(self, *a):
            pass
    s = http.server.HTTPServer(("127.0.0.1", 0), H)
    th = threading.Thread(target=s.serve_forever, daemon=True)
    th.start()
    try:
        t = AMORCE.read_text(encoding="utf-8")
        m = re.search(r"<<'MINUTERIE'\n(.*?)\nMINUTERIE\n", t, re.S)
        sc = tmp_path / "minuterie.sh"
        sc.write_text(m.group(1) + "\n")
        env = {"PATH": str(_sans(tmp_path, "curl")), "HOME": str(tmp_path), "CONTAINER_ID": ID, "CONTAINER_API_KEY": "cle-k",
               "MINUTERIE_PAS_S": "1", "MINUTERIE_REESSAI_S": "1", "MINUTERIE_MARGE_S": "4"}
        r = subprocess.run(["bash", str(sc), str(int(time.time())), str(tmp_path), f"http://127.0.0.1:{s.server_port}/api/v0"],
                           env=env, capture_output=True, text=True, timeout=60)
    finally:
        s.shutdown()
    log = (tmp_path / "sparks-v5-minuterie.log").read_text()
    assert r.returncode == 0 and "HTTP 200" in log and "détruite" in log, log
    assert vu == [(f"/api/v0/instances/{ID}/", "Bearer cle-k")]


def test_outils_supposes_couverts():
    t = AMORCE.read_text(encoding="utf-8")
    ligne = next(l for l in t.splitlines() if l.startswith('OUTILS="'))
    outils = set(ligne.split('"')[1].split())
    for o in ("curl", "git", "python3", "timeout", "setsid", "sha256sum", "tar", "gzip", "awk", "sed", "sort", "cut", "tail",
              "head", "mktemp", "find", "grep", "date", "sleep", "cat", "tr"):
        assert o in outils, o
    f = next(l for l in t.splitlines() if l.startswith("paquet()"))
    for o in outils:
        r = subprocess.run(["bash", "-c", f + f"\npaquet {o}"], capture_output=True, text=True, timeout=10)
        assert r.stdout.strip(), o
    assert "apt-get update -qq" in t and t.count("timeout -k 10 \"$T_APT\" apt-get") == 2


def test_journal_amorce_v10_compte_les_demarrages_anciens_et_neufs(tmp_path):
    f = tmp_path / "l.txt"
    ancien = "".join(f"AMORCE V5 2026-11-05T06:27:{k:02d}Z : machine 59219396, commit x\nAMORCE V5 : curl absent : refus, rien ne part\n"
                     for k in range(3))
    for contenu, att, n, boucle in ((ancien, "1", 3, "oui"), ("AMORCE V10 DEMARRAGE 7 : 2026-11-05T07:00:00Z, machine 1, commit x\n", "7", 7, "non"),
                                    ("AMORCE V10 DEMARRAGE 1 : 2026-11-05T07:00:00Z, machine 1, commit x\n", "1", 1, "non")):
        f.write_text(contenu)
        r = _lanceur(tmp_path, "journal-amorce", str(f), att)
        assert f"DEMARRAGES={n} ATTENDUS={att} BOUCLE={boucle}" in r.stdout and r.returncode == (8 if boucle == "oui" else 0), r.stdout



# --- 9. neuf en v11 : arrêt par l'interface de Vast en fin normale de phase (R-1542) -------------------------------------
def _serveur(reponse: tuple[int, bytes]):
    import http.server
    import threading
    vu = []

    class H(http.server.BaseHTTPRequestHandler):
        def do_PUT(self):
            n = int(self.headers.get("Content-Length", "0"))
            vu.append((self.path, self.headers.get("Authorization"), self.rfile.read(n)))
            self.send_response(reponse[0])
            self.send_header("Content-Length", str(len(reponse[1])))
            self.end_headers()
            self.wfile.write(reponse[1])

        def log_message(self, *a):
            pass
    s = http.server.HTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s, vu


def _jouer_arret(tmp_path, reponse, sans_curl=False, code_sortie="3"):
    t = AMORCE.read_text(encoding="utf-8")
    fonctions = _fonction_ligne(t, "borne_s()") + "\n" + t[t.index("arreter_instance() {"):t.index("refus() {")]
    s, vu = _serveur(reponse)
    try:
        script = (f'R="{tmp_path}"; API="http://127.0.0.1:{s.server_port}/api/v0"\n'
                  'detruire() { echo "DETRUIRE $1 / $2"; exit 9; }\n' + fonctions + f'\narreter_instance "fin de la fabrication, code {code_sortie}" {code_sortie}\n')
        chemin = str(_sans(tmp_path, "curl")) if sans_curl else "/usr/bin:/bin"
        r = subprocess.run(["bash", "-c", script], env={"PATH": chemin, "HOME": str(tmp_path), "CONTAINER_ID": ID, "CONTAINER_API_KEY": "cle-k",
                                                       "AMORCE_ATTENTE_ARRET_S": "0"}, capture_output=True, text=True, timeout=60)
    finally:
        s.shutdown()
    return r, vu


def _fonction_ligne(t: str, debut: str) -> str:
    return next(l for l in t.splitlines() if l.startswith(debut))


@pytest.mark.parametrize("sans_curl", [False, True])
def test_arret_obtenu_puis_sortie(tmp_path, sans_curl):
    r, vu = _jouer_arret(tmp_path, (200, b'{"success": true}'), sans_curl=sans_curl)
    assert r.returncode == 3 and "fin de la fabrication, code 3 : ARRÊT OBTENU (état voulu « stopped », HTTP 200)" in r.stdout, r.stdout + r.stderr
    assert "DETRUIRE" not in r.stdout
    assert len(vu) == 1 and vu[0][0] == f"/api/v0/instances/{ID}/" and vu[0][1] == "Bearer cle-k"
    assert json.loads(vu[0][2]) == {"state": "stopped"}


@pytest.mark.parametrize("reponse, motif", [
    ((200, b'{"success": false, "msg": "non"}'), "HTTP 200"),       # arrêt refusé
    ((403, b'{"success": false}'), "HTTP 403"),                      # refusé par le code
    ((200, b'<html>erreur</html>'), "HTTP 200"),                    # réponse illisible
    ((200, b''), "HTTP 200"),                                        # corps vide
    ((500, b'{"success": true}'), "HTTP 500"),                      # succès écrit, mais code non 2xx (banc v11 : survivante)
])
def test_arret_non_obtenu_destruction(tmp_path, reponse, motif):
    r, _ = _jouer_arret(tmp_path, reponse)
    assert r.returncode == 9 and f"ARRÊT NON OBTENU ({motif}, succès non lu) : destruction ; perdus : les couches des modèles" in r.stdout
    assert "DETRUIRE arrêt non obtenu : fin de la fabrication, code 3 / 3" in r.stdout


def test_arret_sans_reponse_destruction(tmp_path):
    t = AMORCE.read_text(encoding="utf-8")
    fonctions = _fonction_ligne(t, "borne_s()") + "\n" + t[t.index("arreter_instance() {"):t.index("refus() {")]
    script = (f'R="{tmp_path}"; API="http://127.0.0.1:9/api/v0"\ndetruire() {{ echo "DETRUIRE $1"; exit 9; }}\n' + fonctions
              + '\narreter_instance "fin de la fenêtre de copie" 0\n')
    r = subprocess.run(["bash", "-c", script], env={"PATH": "/usr/bin:/bin", "HOME": str(tmp_path), "CONTAINER_ID": ID,
                                                   "CONTAINER_API_KEY": "k", "AMORCE_ATTENTE_ARRET_S": "0"}, capture_output=True, text=True, timeout=120)
    assert r.returncode == 9 and "ARRÊT NON OBTENU (HTTP 000" in r.stdout and "DETRUIRE arrêt non obtenu : fin de la fenêtre de copie" in r.stdout


@pytest.mark.parametrize("corps, detruite", [('{"success": true}', False), ('{"success": false}', True)])
def test_fin_causale_arret_ou_destruction(tmp_path, depot, corps, detruite):
    d, c = depot
    _ordres(d, c, [{"numero": 3, "instance": ID, "phase": "causal", "deja_usd": 10.0}], causal=True)
    r_ = _disque(tmp_path, d, c)
    inst = r_ / "amorce-depot" / "scripts" / "sparks_exp7_nul_instance_v11.sh"
    inst.write_text('#!/bin/bash\nmkdir -p "$TRAVAIL"; echo tete > "$TRAVAIL/POUSSEE-VERIFIEE"\nexit 1\n')
    code, out, _, _ = _amorce(tmp_path, d, c, FAUX_CORPS=corps, AMORCE_ATTENTE_ARRET_S="0")
    _arreter_minuteries(r_)
    assert "phase causale en code 1, poussée vérifiée : pas de destruction" in out
    assert ("ARRÊT NON OBTENU" in out and "DELETE instance 123456" in _journal(r_)) == detruite, out
    assert ("ARRÊT OBTENU (état voulu « stopped »" in out and "DELETE" not in _journal(r_)) == (not detruite)
    assert code == 1


def _bloc_fabrication(t: str) -> str:
    i = t.index('    if [ "${MODE:-reel}" = jouet ] && [ "${JOUET_MACHINE:-}" = 1 ]')
    j = t.index("    consigner_fin; echo \"AMORCE V5 $(date -u +%FT%TZ) : fin de la fabrication, code $code\"")
    return t[i:j]


@pytest.mark.parametrize("mode, machine, marque, factice", [
    ("jouet", "1", True, True), ("reel", "1", True, False), ("jouet", "", True, False), ("jouet", "1", False, False)])
def test_fabrication_factice_seulement_jouet_machine_et_addendum_marque(tmp_path, mode, machine, marque, factice):
    from controle_ia.sparks_exp7_nul_v8.addendum_factice import MARQUE
    t = AMORCE.read_text(encoding="utf-8")
    bloc = _bloc_fabrication(t)
    i = bloc.index("        timeout --signal=TERM"); j = bloc.index("        code=$?\n", i)
    bloc = bloc[:i] + "        echo FABRICATION-REELLE\n" + bloc[j:]
    (tmp_path / "amorce-depot" / "prereg").mkdir(parents=True)
    (tmp_path / "amorce-depot" / "prereg" / "SPARKS-EXP7-NUL-addendum-1.md").write_text((f"# {MARQUE}\n" if marque else "# Addendum\n") + "x\n")
    script = f'R="{tmp_path}"\n' + _fonction_ligne(t, "borne_s()") + "\n" + bloc + 'echo "CODE=$code"\n'
    r = subprocess.run(["bash", "-c", script], env={"PATH": "/usr/bin:/bin", "MODE": mode, "JOUET_MACHINE": machine, "JOUET_FABRICATION_S": "1"},
                       capture_output=True, text=True, timeout=60)
    assert ("fabrication factice (mode jouet sur machine réelle, addendum factice) : 1 s" in r.stdout) == factice, r.stdout + r.stderr
    assert ("FABRICATION-REELLE" in r.stdout) == (not factice) and "CODE=" in r.stdout


def test_v11_fins_de_phase_arretent_et_attentes_bornees():
    t = AMORCE.read_text(encoding="utf-8")
    assert t.count("arreter_instance \"") == 3
    assert 'arreter_instance "fin de la fabrication, code $code" "$code"' in t and 'arreter_instance "fin de la fenêtre de copie" 0' in t
    assert 'arreter_instance "fin de la phase causale, code $code" "$code"' in t
    assert 'AF=$(borne_s "${AMORCE_ATTENTE_FIN_S:-0}" 600)' in t and 'JF=$(borne_s "${JOUET_FABRICATION_S:-60}" 600)' in t
    assert 'sleep "$(borne_s "${AMORCE_ATTENTE_ARRET_S:-10}" 60)"' in t
    f = _fonction_ligne(t, "borne_s()")
    out = subprocess.run(["bash", "-c", f + "\nborne_s 9999 600; borne_s 5 600; borne_s x 600"], capture_output=True, text=True).stdout.split()
    assert out == ["600", "5", "0"]
