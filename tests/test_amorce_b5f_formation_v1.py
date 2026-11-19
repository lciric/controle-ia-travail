"""Essais hors ligne de l'amorce d'instance de la formation du barreau 5 (`scripts/amorce_b5f_formation_v1.sh`) : rien n'est
lancé pour de vrai. L'essai local de l'amorce entière (arguments), puis ses blocs marqués, extraits et joués dans un bash
jetable avec un faux `curl` et un dépôt distant local ; enfin, des contrôles du texte. Cas sain et artefact (R5)."""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
from pathlib import Path

import pytest

RACINE_DEPOT = Path(__file__).resolve().parents[1]
AMORCE = RACINE_DEPOT / "scripts" / "amorce_b5f_formation_v1.sh"
TEXTE = AMORCE.read_text(encoding="utf-8")
SAINS = {"INSTANCE_B5F": "3", "COMMIT": "a" * 40, "BRANCHE_CODE": "lot/b5f-v1", "PREREG": "prereg/barreau5-texte.md",
         "RUN_B5F": "20261123-080000-b5f-formation-3", "PRIX_USD_H": "1.2", "ECHEANCE_ARRET_UTC_S": "1900000000",
         "GO_ID": "GO-2026-11-20-01", "DEPOT_URL": "https://github.com/lciric/controle-ia-travail.git"}


def _bloc(nom: str) -> str:
    m = re.search(rf"^# >>> {re.escape(nom)}\b.*?$(.*?)^# <<< {re.escape(nom)}$", TEXTE, re.S | re.M)
    assert m, nom
    return m.group(1)


def _env(**sup):
    env = {k: v for k, v in os.environ.items() if k not in SAINS and not k.startswith(("GIT_", "CONTAINER_"))}
    env.update(SAINS)
    env.update({k: v for k, v in sup.items() if v is not None})
    for k, v in sup.items():
        if v is None:
            env.pop(k, None)
    return env


def test_essai_local_cas_sain_arguments_conformes_rien_ecrit(tmp_path):
    p = subprocess.run(["bash", str(AMORCE)], env=_env(AMORCE_ESSAI_LOCAL="1", RACINE_AMORCE=str(tmp_path)),
                       capture_output=True, text=True, timeout=60)
    assert p.returncode == 0 and "arguments conformes" in p.stdout, p.stdout + p.stderr
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("cle, valeur, motif", [
    ("COMMIT", None, "COMMIT absente"), ("INSTANCE_B5F", "8", "1 à 7"), ("COMMIT", "a" * 39, "40 caractères"),
    ("COMMIT", "g" * 40, "COMMIT illisible"), ("BRANCHE_CODE", "a b", "BRANCHE_CODE"), ("PREREG", "prereg/../x.md", "PREREG"),
    ("PREREG", "docs/notes/x.md", "PREREG"), ("RUN_B5F", "20261123-080000-b5f-formation-4", "autre instance"),
    ("PRIX_USD_H", "1.35", "hors de"), ("PRIX_USD_H", "un", "illisible"), ("ECHEANCE_ARRET_UTC_S", "demain", "illisible"),
    ("GO_ID", "GO-26-1", "GO_ID"), ("DEPOT_URL", "https://github.com/lciric/controle-ia.git", "copie publique")])
def test_essai_local_artefacts_arguments_refuses(tmp_path, cle, valeur, motif):
    p = subprocess.run(["bash", str(AMORCE)], env=_env(AMORCE_ESSAI_LOCAL="1", RACINE_AMORCE=str(tmp_path), **{cle: valeur}),
                       capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and motif in p.stdout, p.stdout
    assert not list(tmp_path.iterdir())


def test_artefact_racine_amorce_hors_essai_refusee(tmp_path):
    p = subprocess.run(["bash", str(AMORCE)], env=_env(RACINE_AMORCE=str(tmp_path)), capture_output=True, text=True,
                       timeout=60)
    assert p.returncode == 2 and "essai local seulement" in p.stdout


def _jouer(script: str, env_sup: dict, timeout: int = 30) -> subprocess.CompletedProcess:
    entete = 'set -uo pipefail\nj() { printf "%s\\n" "$*" >> "$L"; }\n'
    return subprocess.run(["bash", "-c", entete + script], env=_env(**env_sup), capture_output=True, text=True,
                          timeout=timeout)


def test_duree_de_la_marche_cas_sain_et_artefact():
    p = _jouer(_bloc("duree-de-la-marche") + "duree_marche 10000 6400", {})
    assert p.returncode == 0 and p.stdout.strip() == "3600"
    assert _jouer(_bloc("duree-de-la-marche") + "duree_marche 10030 10000", {}).returncode == 1
    assert _jouer(_bloc("duree-de-la-marche") + "duree_marche 100 10000", {}).returncode == 1


def _faux_curl(tmp_path) -> Path:
    b = tmp_path / "bin"
    b.mkdir()
    (b / "curl").write_text('#!/usr/bin/env bash\nprintf "%s\\n" "$*" >> "$JOURNAL_CURL"\nprintf 200\n', encoding="utf-8")
    (b / "curl").chmod(0o755)
    return b


def test_fin_instance_etat_stopped_par_l_identifiant_cle_jamais_ecrite(tmp_path):
    b = _faux_curl(tmp_path)
    env = {"PATH": f"{b}:{os.environ['PATH']}", "JOURNAL_CURL": str(tmp_path / "curl.txt"), "L": str(tmp_path / "j.txt"),
           "CONTAINER_ID": "4242", "CONTAINER_API_KEY": "cle-factice-xyz", "B5F_SANS_ATTENTE": "1"}
    p = _jouer("API=https://console.vast.ai/api/v0\n" + _bloc("fin-instance") + "fin_instance 3", env)
    assert p.returncode == 3
    appel = (tmp_path / "curl.txt").read_text()
    assert "-X PUT" in appel and '"state": "stopped"' in appel and "/instances/4242/" in appel and "DELETE" not in appel
    assert "cle-factice-xyz" not in (tmp_path / "j.txt").read_text() + p.stdout + p.stderr


def test_minuterie_detruit_par_l_identifiant_a_l_echeance_et_pas_avant(tmp_path):
    b = _faux_curl(tmp_path)
    env = {"PATH": f"{b}:{os.environ['PATH']}", "JOURNAL_CURL": str(tmp_path / "curl.txt"), "L": str(tmp_path / "j.txt"),
           "CONTAINER_ID": "4242", "CONTAINER_API_KEY": "cle-factice-xyz", "B5F_PAS_MINUTERIE": "1"}
    corps = "export API=https://console.vast.ai/api/v0\n" + _bloc("minuterie")
    p = _jouer(corps + 'timeout 4 bash -c "$(declare -f minuterie j); minuterie $(( $(date +%s) - 5 ))"', env)
    appels = (tmp_path / "curl.txt").read_text().splitlines()
    assert appels and all("-X DELETE" in a and a.endswith("https://console.vast.ai/api/v0/instances/4242/")
                          for a in appels), p.stderr
    (tmp_path / "curl.txt").unlink()
    _jouer(corps + 'timeout 3 bash -c "$(declare -f minuterie j); minuterie $(( $(date +%s) + 3600 ))"', env)
    assert not (tmp_path / "curl.txt").exists()                      # avant l'échéance : aucune demande


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


@pytest.fixture
def depots(tmp_path):
    """Dépôt distant local (nu) et son clone D au commit COMMIT ; T, dossier de travail de l'amorce."""
    nu, d, t = tmp_path / "distant.git", tmp_path / "T" / "depot", tmp_path / "T"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(nu)], check=True)
    graine = tmp_path / "graine"
    graine.mkdir()
    for a in (["init", "-q", "-b", "main"], ["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        subprocess.run(["git", "-C", str(graine), *a], check=True)
    (graine / "src.py").write_text("x = 1\n")
    subprocess.run(["git", "-C", str(graine), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(graine), "commit", "-q", "-m", "code"], check=True)
    subprocess.run(["git", "-C", str(graine), "push", "-q", str(nu), "main"], check=True)
    subprocess.run(["git", "clone", "-q", str(nu), str(d)], check=True)
    for a in (["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        subprocess.run(["git", "-C", str(d), *a], check=True)
    commit = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    (t / "parent-sortie").write_text(commit + "\n")
    sorties = d / "donnees" / "run"
    sorties.mkdir(parents=True)
    for nom, contenu in (("adaptateur-jumeau.pt", b"poids"), ("textes.jsonl", b"{}")):
        (sorties / nom).write_bytes(contenu)
        (sorties / f"{nom}.sha256").write_text(f"{_sha(sorties / nom)}  {nom}\n")
    (sorties / "sans-compagnon.json").write_text("{}")
    (sorties / "faux.json").write_text("{}")
    (sorties / "faux.json.sha256").write_text("0" * 64 + "  faux.json\n")
    return {"nu": nu, "D": d, "T": t, "commit": commit, "L": tmp_path / "j.txt"}


def _verser(dep, script, seuil="94000000"):
    env = {"D": str(dep["D"]), "T": str(dep["T"]), "L": str(dep["L"]), "BR": "donnees/b5f-essai-instance-3",
           "SEUIL": seuil}
    return _jouer(_bloc("versement") + script, env)


def test_versement_cas_sain_fichiers_scelles_seulement_tete_inchangee(depots):
    p = _verser(depots, "fichiers_scelles donnees/run")
    assert p.stdout.split() == ["donnees/run/adaptateur-jumeau.pt", "donnees/run/adaptateur-jumeau.pt.sha256",
                                "donnees/run/textes.jsonl", "donnees/run/textes.jsonl.sha256"]
    p = _verser(depots, 'verser "essai" $(fichiers_scelles donnees/run)')
    assert p.returncode == 0, p.stderr
    pousse = subprocess.run(["git", "-C", str(depots["nu"]), "rev-parse", "donnees/b5f-essai-instance-3"],
                            capture_output=True, text=True).stdout.strip()
    assert pousse == (depots["T"] / "parent-sortie").read_text().strip()
    parent = subprocess.run(["git", "-C", str(depots["nu"]), "rev-parse", f"{pousse}^"], capture_output=True,
                            text=True).stdout.strip()
    assert parent == depots["commit"]
    contenu = subprocess.run(["git", "-C", str(depots["nu"]), "show", f"{pousse}:donnees/run/adaptateur-jumeau.pt"],
                             capture_output=True).stdout
    assert contenu == b"poids"
    tete = subprocess.run(["git", "-C", str(depots["D"]), "rev-parse", "HEAD"], capture_output=True, text=True).stdout
    assert tete.strip() == depots["commit"]                          # la tête de la marche n'a pas bougé
    assert (depots["D"] / "donnees" / "run" / "adaptateur-jumeau.pt").exists()     # rien n'est supprimé
    # rien de neuf : aucun commit de plus
    assert _verser(depots, 'verser "essai 2" $(fichiers_scelles donnees/run)').returncode == 0
    assert (depots["T"] / "parent-sortie").read_text().strip() == pousse
    # versement final : tous les fichiers, scellés ou non
    assert _verser(depots, 'verser "fin" $(tous_les_fichiers donnees/run)').returncode == 0
    fin = (depots["T"] / "parent-sortie").read_text().strip()
    noms = subprocess.run(["git", "-C", str(depots["nu"]), "ls-tree", "-r", "--name-only", fin], capture_output=True,
                          text=True).stdout.split()
    assert "donnees/run/sans-compagnon.json" in noms and "donnees/run/faux.json" in noms


def test_versement_artefacts_fichier_trop_gros_ou_distant_injoignable(depots):
    p = _verser(depots, 'verser "essai" $(fichiers_scelles donnees/run)', seuil="3")
    assert p.returncode == 1 and "plus de 3 octets" in depots["L"].read_text()
    assert (depots["T"] / "parent-sortie").read_text().strip() == depots["commit"]
    subprocess.run(["git", "-C", str(depots["D"]), "remote", "set-url", "origin", str(depots["T"] / "absent.git")],
                   check=True)
    p = _verser(depots, 'sleep() { :; }; verser "essai" $(fichiers_scelles donnees/run)')
    assert p.returncode == 1 and (depots["T"] / "parent-sortie").read_text().strip() == depots["commit"]


# --- contrôles du texte de l'amorce -------------------------------------------------------------------------------------

def test_texte_aucune_lecture_d_activation_ni_de_score_aucun_arret_par_motif():
    modules = set(re.findall(r"-m (controle_ia\.[A-Za-z0-9_.]+)", TEXTE))
    assert modules == {"controle_ia.barreau5_familles.formation_v1"}
    assert set(re.findall(r"from (controle_ia\.[A-Za-z0-9_.]+) import", TEXTE)) == {"controle_ia.harnais.modeles"}
    for interdit in ("sondes", "t07bbis", "relecture", "lecture_v1", "pkill", "killall", "pgrep", "rm -rf", "git reset"):
        assert interdit not in TEXTE, interdit
    assert re.findall(r"(?<![-\w])kill(?![-\w])[^\n]*", TEXTE) == ['kill -0 "$PID" 2> /dev/null; do']   # sonde de vie seule
    essais = re.findall(r"-m pytest[^\n]*", TEXTE)
    assert len(essais) == 1 and "tests/test_barreau5_familles_*.py" in essais[0]


def test_texte_aucune_valeur_de_cle_seulement_des_noms():
    assert not re.search(r"ghp_|github_pat_|hf_[A-Za-z0-9]{8}|Bearer [A-Za-z0-9]", TEXTE)
    for nom in ("GH_TOKEN", "HF_TOKEN", "CONTAINER_API_KEY"):
        for ligne in TEXTE.splitlines():
            if nom in ligne and not ligne.lstrip().startswith("#"):
                assert re.search(rf"\$\{{{nom}(:-)?\}}|\$\{{{nom}:-\}}|{nom} absent", ligne) or f"variable {nom}" in ligne \
                    or f"{nom} (par" in ligne or "par le nom" in ligne, ligne
                assert not re.search(rf"(echo|j|printf)[^\n]*\$\{{?{nom}", ligne.split("password=")[0]), ligne


def test_texte_extraction_sans_docs_notes_ni_diag_et_accord_de_la_formation():
    motifs = _bloc("motifs")
    assert "/src/" in motifs and "/registres/barreau5-familles-jumelles-v1.md*" in motifs
    assert not re.search(r"^/(docs/notes|diag|runs|brouillons)", motifs, re.M)
    assert "/docs/sources/invites-2606.08892-v1/" in motifs
    assert "donnees/barreau5-familles-jumelles-v1-formation-instance-$INSTANCE_B5F" in TEXTE
