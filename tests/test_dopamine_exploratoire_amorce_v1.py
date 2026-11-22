"""Amorce de la machine (exploratoire) : arguments, minuterie de destruction, liste blanche, versement et preuve, joués
par bash avec un faux `curl` et un dépôt distant local. Aucun réseau, aucune machine (R5 : sain et artefact)."""
import os
import re
import subprocess
import time
from pathlib import Path

import pytest

AMORCE = Path(__file__).resolve().parents[1] / "src" / "controle_ia" / "dopamine_exploratoire" / "amorce_v1.sh"
RUN = "20261121-130000-dopamine-exploratoire-v1-etape-1"
COMMIT = "a" * 40


def bloc(nom: str) -> str:
    t = AMORCE.read_text(encoding="utf-8")
    m = re.search(rf"^# >>> {nom}\n(.*?)^# <<< {nom}\n", t, re.S | re.M)
    assert m, nom
    return m.group(1)


def env_ok(**k):
    now = int(time.time())
    e = {"ETAPE": "1", "COMMIT": COMMIT, "RUN_ID": RUN, "PRIX_USD_H": "1.19", "FIN_LANCEMENTS_UTC_S": str(now + 19800),
         "DESTRUCTION_UTC_S": str(now + 23400), "GO_ID": "GO-2026-11-21-48",
         "DEPOT_URL": "https://github.com/lciric/controle-ia-travail.git", "CONTEXTES": "-", "LISTE_HONNETES": "-"}
    e.update(k)
    return e


def jouer_amorce(env):
    full = {"PATH": os.environ["PATH"], "AMORCE_ESSAI_LOCAL": "1", **env}
    return subprocess.run(["bash", str(AMORCE)], env=full, capture_output=True, text=True)


def test_arguments_sains_essai_local():
    r = jouer_amorce(env_ok())
    assert r.returncode == 0 and "ESSAI LOCAL" in r.stdout
    r2 = jouer_amorce(env_ok(CONTEXTES="ctx/c.jsonl", LISTE_HONNETES="ctx/l.json"))
    assert r2.returncode == 0


@pytest.mark.parametrize("champ,valeur", [
    ("DEPOT_URL", "https://github.com/lciric/controle-ia.git"),     # jamais la copie publique
    ("RUN_ID", "20261121-130000-dopamine-v1-etape-1"),             # sans « exploratoire »
    ("ETAPE", "2a"), ("COMMIT", "abc"), ("GO_ID", "GO-21"), ("PRIX_USD_H", "1.9"),
    ("FIN_LANCEMENTS_UTC_S", str(int(time.time()) + 99999)),        # fin des lancements après la destruction
    ("CONTEXTES", "ctx/c.jsonl"),                                  # sans la liste des épisodes honnêtes
    ("CONTEXTES", "../hors.jsonl"),
])
def test_arguments_artefacts(champ, valeur):
    r = jouer_amorce(env_ok(**{champ: valeur}))
    assert r.returncode == 2 and "REFUS" in r.stdout


def test_variable_absente():
    e = env_ok()
    del e["GO_ID"]
    assert jouer_amorce(e).returncode == 2


def _faux_curl(tmp_path):
    b = tmp_path / "bin"
    b.mkdir()
    (b / "curl").write_text(f'#!/usr/bin/env bash\necho "$@" >> {tmp_path}/curl.log\nprintf 200\n')
    (b / "curl").chmod(0o755)
    return b


def _harnais(tmp_path, corps: str, **env):
    T = tmp_path / "T"
    (T / "traces").mkdir(parents=True, exist_ok=True)
    tete = (f'T="{T}"; D="$T/depot"; X="$T/traces"; L="$X/journal.txt"; API=https://exemple.invalid/api\n'
            f'TEMOIN="$T/versement-final-prouve"; SIGNAL="$X/signal-pour-la-mere.txt"; BR=donnees/dopamine-exploratoire-v1\n'
            f'RUN_ID={RUN}; COMMIT="${{COMMIT:-{COMMIT}}}"; SEUIL="${{SEUIL:-94000000}}"\n'
            "j() { printf '%s\\n' \"$*\" >> \"$L\"; }\n")
    script = tmp_path / "harnais.sh"
    script.write_text(tete + corps)
    full = {"PATH": f"{_faux_curl(tmp_path) if not (tmp_path / 'bin').exists() else tmp_path / 'bin'}:{os.environ['PATH']}",
            "CONTAINER_ID": "777", "CONTAINER_API_KEY": "cle-factice", "HOME": str(tmp_path), **env}
    return subprocess.run(["bash", str(script)], env=full, capture_output=True, text=True, timeout=60), T


def test_minuterie_detruit_seulement_apres_preuve(tmp_path):
    corps = bloc("minuterie") + 'echo commit-prouve > "$TEMOIN"\nminuterie $(( $(date +%s) - 1 ))\n'
    r, T = _harnais(tmp_path, corps, DOPAMINE_ESSAIS_MINUTERIE="1", DOPAMINE_PAS_MINUTERIE="0")
    assert r.returncode == 0
    log = (tmp_path / "curl.log").read_text()
    assert "-X DELETE" in log and "/instances/777/" in log and "stopped" not in log
    assert not (T / "traces" / "signal-pour-la-mere.txt").exists()


def test_minuterie_sans_preuve_arrete_sans_detruire(tmp_path):
    corps = bloc("minuterie") + "minuterie $(( $(date +%s) - 1 ))\n"
    r, T = _harnais(tmp_path, corps, DOPAMINE_ESSAIS_MINUTERIE="1", DOPAMINE_PAS_MINUTERIE="0")
    log = (tmp_path / "curl.log").read_text()
    assert "DELETE" not in log and '{"state": "stopped"}' in log
    assert "NON détruite" in (T / "traces" / "signal-pour-la-mere.txt").read_text()


@pytest.mark.parametrize("chemin,attendu", [
    (f"donnees/{RUN}/generations/lot-00003.jsonl", True), (f"donnees/{RUN}/notation/lot-00003.jsonl.sha256", True),
    (f"donnees/{RUN}/etats/couche-02/lot-00001.index.json", True),
    (f"donnees/{RUN}/etats-s0/couche-03.npy", True), (f"donnees/{RUN}/sondes/poids/noyau--graine-0.npz", True),
    (f"donnees/{RUN}/relecture-forcee/couche-15.npy", True), (f"diag/{RUN}/etape1-noyau-exploratoire.json", True),
    (f"runs/{RUN}/manifeste.json", True), ("traces-dopamine/journal/journal.txt", True),
    (f"donnees/{RUN}/etats/couche-02/lot-00001.npy", False),          # trajectoires : inscrites, pas versées
    ("donnees/20261019-230011-p3-reel/scores-p3.npz", False), (f"donnees/{RUN}/../../registres/go.md", False),
    ("diag/20261121-000000-autre/x.json", False),
])
def test_liste_blanche(tmp_path, chemin, attendu):
    r, _ = _harnais(tmp_path, bloc("versement") + f'permis "{chemin}" && echo OUI || echo NON\n')
    assert r.stdout.strip() == ("OUI" if attendu else "NON")


def _depot_et_distant(tmp_path):
    nu = tmp_path / "distant.git"
    subprocess.run(["git", "init", "-q", "--bare", str(nu)], check=True)
    D = tmp_path / "T" / "depot"
    D.mkdir(parents=True)
    g = lambda *a: subprocess.run(["git", "-C", str(D), *a], check=True, capture_output=True, text=True).stdout.strip()
    g("init", "-q")
    g("config", "user.email", "e@invalid")
    g("config", "user.name", "essai")
    (D / "LISEZ-MOI").write_text("x")
    g("add", "-A")
    g("commit", "-q", "-m", "code")
    g("remote", "add", "origin", str(nu))
    g("push", "-q", "origin", "HEAD:refs/heads/prep")
    commit = g("rev-parse", "HEAD")
    for rel, contenu in ((f"donnees/{RUN}/generations/lot-00000.jsonl", "{}\n"),
                         (f"donnees/{RUN}/etats/couche-02/lot-00000.npy", "trajectoire\n"),
                         (f"runs/{RUN}/manifeste.json", "{}\n")):
        f = D / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(contenu)
    return D, nu, commit


def test_versement_et_preuve_sains(tmp_path):
    D, nu, commit = _depot_et_distant(tmp_path)
    corps = bloc("versement") + bloc("preuve") + "prouver_versement && echo PROUVE\n"
    r, T = _harnais(tmp_path, corps, COMMIT=commit)
    assert "PROUVE" in r.stdout, r.stdout + r.stderr + (T / "traces" / "journal.txt").read_text()
    tete = (T / "versement-final-prouve").read_text().strip()
    ls = subprocess.run(["git", "-C", str(nu), "ls-tree", "-r", "--name-only", tete], capture_output=True,
                        text=True).stdout.split()
    assert f"donnees/{RUN}/generations/lot-00000.jsonl" in ls and "traces-dopamine/inventaire-final.json" in ls
    assert f"donnees/{RUN}/etats/couche-02/lot-00000.npy" not in ls              # trajectoire : inscrite seulement
    inv = subprocess.run(["git", "-C", str(nu), "show", f"{tete}:traces-dopamine/inventaire-final.json"],
                         capture_output=True, text=True).stdout
    assert '"verse": false' in inv and '"verse": true' in inv


def test_preuve_refusee_si_un_fichier_permis_ne_sort_pas(tmp_path):
    D, nu, commit = _depot_et_distant(tmp_path)
    corps = bloc("versement") + bloc("preuve") + "prouver_versement && echo PROUVE || echo NON\n"
    r, T = _harnais(tmp_path, corps, COMMIT=commit, SEUIL="2")                    # tout fichier permis est trop gros
    assert "NON" in r.stdout and not (T / "versement-final-prouve").exists()


def test_preuve_refusee_si_un_seul_fichier_permis_est_trop_gros(tmp_path):
    """Un fichier permis trop gros pour sortir reste sur le disque : pas de preuve, donc pas de destruction."""
    D, nu, commit = _depot_et_distant(tmp_path)
    gros = D / "donnees" / RUN / "generations" / "lot-00001.jsonl"
    gros.write_text("x" * 6000)
    corps = bloc("versement") + bloc("preuve") + "prouver_versement && echo PROUVE || echo NON\n"
    r, T = _harnais(tmp_path, corps, COMMIT=commit, SEUIL="5000")
    assert "NON" in r.stdout and not (T / "versement-final-prouve").exists()
    assert "non poussé" in (T / "traces" / "journal.txt").read_text()


def test_attente_rend_la_main_a_la_fin_du_processus(tmp_path):
    corps = (bloc("versement") + bloc("attente") + "PAS_ATTENTE_S=1; PERIODE_VERSEMENT_S=100\n"
             "sleep 2 & p=$!\nt0=$(date +%s); attendre_la_marche $p; echo $(( $(date +%s) - t0 ))\n")
    r, _ = _harnais(tmp_path, corps)
    assert int(r.stdout.strip()) <= 5


def test_amorce_ne_contient_aucune_suppression_ni_arret_par_motif():
    t = AMORCE.read_text(encoding="utf-8")
    assert not re.search(r"(^|[\s;&|(])rm\s", t, re.M)
    assert not re.search(r"\b(pkill|killall|pgrep)\b", t)
    assert "vastai" not in t                                                      # l'instance ne se pilote que par l'API


def test_min_essais_de_l_amorce_egal_au_nombre_d_essais_du_paquet():
    n = int(re.search(r"^MIN_ESSAIS=(\d+)$", AMORCE.read_text(encoding="utf-8"), re.M).group(1))
    racine = AMORCE.parents[3]
    r = subprocess.run([os.sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--noconftest", "--collect-only",
                        *sorted(str(p) for p in (racine / "tests").glob("test_dopamine_exploratoire_*.py"))],
                       capture_output=True, text=True, cwd=racine, env={**os.environ, "PYTHONPATH": str(racine / "src")})
    assert f"{n} tests collected" in r.stdout, r.stdout[-300:]


def test_essais_de_l_amorce_sans_conftest_du_depot():
    """L'extraction partielle n'emporte ni le greffon des échecs connus ni les fichiers qu'il liste (R-4755) :
    les essais du paquet se jouent sans le conftest du dépôt, qu'ils n'emploient pas."""
    t = AMORCE.read_text(encoding="utf-8")
    ligne = [l for l in t.splitlines() if "-m pytest" in l and "test_dopamine_exploratoire_" in l]
    assert len(ligne) == 1 and "--noconftest" in ligne[0]
