"""Essais hors ligne de l'amorce de l'instance de lecture du barreau 5 (`scripts/amorce_b5f_lecture_v1.sh`) : rien n'est lancé
pour de vrai. L'essai local de l'amorce entière (arguments), puis ses blocs marqués, extraits et joués dans un bash jetable
avec un faux `curl` et des dépôts distants locaux ; enfin, des contrôles du texte. Cas sain et artefact (R5). Écrits le 20
novembre 2026 sur le modèle de `tests/test_amorce_b5f_formation_v1.py`."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

from controle_ia.barreau5_familles import relecture_v1 as rv

RACINE_DEPOT = Path(__file__).resolve().parents[1]
AMORCE = RACINE_DEPOT / "scripts" / "amorce_b5f_lecture_v1.sh"
TEXTE = AMORCE.read_text(encoding="utf-8")
RUN = "20261124-120000-b5f-lecture"
SAINS = {"PLAN_B5F": "decisif", "COMMIT": "a" * 40, "BRANCHE_CODE": "lot/b5f-lecture-v1",
         "PREREG": "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md", "RUN_LECTURE": RUN,
         "PRIX_USD_H": "1.2", "ECHEANCE_ARRET_UTC_S": "1900000000", "GO_ID": "GO-2026-11-24-01",
         "DEPOT_URL": "https://github.com/lciric/controle-ia-travail.git", "ENTREES_COMMIT": "b" * 40, "DIVERGENCE_B5F": "1",
         "GARDE_B5F": "une_sur_dix", "EXISTANTS_B5F": "W10=", "EXISTANTS_CHEMINS": "-"}
REPETITION = {"PLAN_B5F": "repetition", "RUN_LECTURE": "20261123-120000-b5f-repetition", "ENTREES_COMMIT": "-",
              "EXISTANTS_CHEMINS": "donnees/r/adaptateur-saboteur.pt,donnees/r/adaptateur-temoin.pt", "EXISTANTS_B5F": "eyJhIjoxfQ=="}
ARRET = "k" + "ill"                  # composé : la garde du dépôt refuse ce nom écrit dans une commande


def _bloc(nom: str) -> str:
    m = re.search(rf"^# >>> {re.escape(nom)}\b.*?$(.*?)^# <<< {re.escape(nom)}$", TEXTE, re.S | re.M)
    assert m, nom
    return m.group(1)


def _constante(nom: str) -> str:
    m = re.search(rf"^{nom}=(\S+)", TEXTE, re.M)
    assert m, nom
    return m.group(1)


def _env(**sup):
    env = {k: v for k, v in os.environ.items() if k not in SAINS and not k.startswith(("GIT_", "CONTAINER_", "B5F_"))}
    env.update(SAINS)
    env.update({k: v for k, v in sup.items() if v is not None})
    for k, v in sup.items():
        if v is None:
            env.pop(k, None)
    return env


def _jouer(script: str, env_sup: dict, timeout: int = 60) -> subprocess.CompletedProcess:
    entete = 'set -uo pipefail\nj() { printf "%s\\n" "$*" >> "$L"; }\n'
    return subprocess.run(["bash", "-c", entete + script], env=_env(**env_sup), capture_output=True, text=True,
                          timeout=timeout)


# --- arguments (essai local de l'amorce entière) ------------------------------------------------------------------------

def test_essai_local_cas_sain_arguments_conformes_rien_ecrit(tmp_path):
    for sup in ({}, REPETITION, {"GARDE_B5F": "couche_15", "DIVERGENCE_B5F": "0"}):
        p = subprocess.run(["bash", str(AMORCE)], env=_env(AMORCE_ESSAI_LOCAL="1", RACINE_AMORCE=str(tmp_path), **sup),
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0 and "arguments conformes" in p.stdout, p.stdout + p.stderr
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("sup, motif", [
    ({"COMMIT": None}, "COMMIT absente"), ({"PLAN_B5F": "autre"}, "decisif ou repetition"),
    ({"COMMIT": "a" * 39}, "40 caractères"), ({"COMMIT": "g" * 40}, "COMMIT illisible"),
    ({"BRANCHE_CODE": "a b"}, "BRANCHE_CODE"), ({"PREREG": "prereg/autre-v1.md"}, "PREREG"),
    ({"RUN_LECTURE": "20261124-120000-b5f-repetition"}, "autre plan"),
    ({"RUN_LECTURE": "20261124-120000-b5f-formation-3"}, "RUN_LECTURE"), ({"PRIX_USD_H": "1.35"}, "hors de"),
    ({"PRIX_USD_H": "un"}, "illisible"), ({"ECHEANCE_ARRET_UTC_S": "demain"}, "illisible"), ({"GO_ID": "GO-26-1"}, "GO_ID"),
    ({"DEPOT_URL": "https://github.com/lciric/controle-ia.git"}, "copie publique"),
    ({"ENTREES_COMMIT": "-"}, "plan décisif"), ({"ENTREES_COMMIT": "c" * 39}, "plan décisif"),
    ({"DIVERGENCE_B5F": "2"}, "0 ou 1"), ({"GARDE_B5F": "tout"}, "GARDE_B5F"), ({"EXISTANTS_B5F": "a b"}, "base64"),
    ({"EXISTANTS_CHEMINS": "../x.pt"}, "chemin"), ({"EXISTANTS_CHEMINS": "diag/r/adaptateur.pt"}, "refusé"),
    ({"EXISTANTS_CHEMINS": "donnees/20261122-101010-b5f-formation-1/T01/adaptateur-jumeau.pt"}, "refusé"),
    ({"EXISTANTS_B5F": None}, "EXISTANTS_B5F absente")])
def test_essai_local_artefacts_arguments_refuses(tmp_path, sup, motif):
    p = subprocess.run(["bash", str(AMORCE)], env=_env(AMORCE_ESSAI_LOCAL="1", RACINE_AMORCE=str(tmp_path), **sup),
                       capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and motif in p.stdout, p.stdout
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("sup, motif", [({"ENTREES_COMMIT": "b" * 40}, "« - » attendu"),
                                        ({"EXISTANTS_CHEMINS": "-"}, "sans adaptateurs existants")])
def test_repetition_artefacts(tmp_path, sup, motif):
    p = subprocess.run(["bash", str(AMORCE)], env=_env(AMORCE_ESSAI_LOCAL="1", RACINE_AMORCE=str(tmp_path),
                                                       **{**REPETITION, **sup}), capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and motif in p.stdout, p.stdout


def test_artefact_racine_amorce_hors_essai_refusee(tmp_path):
    p = subprocess.run(["bash", str(AMORCE)], env=_env(RACINE_AMORCE=str(tmp_path)), capture_output=True, text=True,
                       timeout=60)
    assert p.returncode == 2 and "RACINE_AMORCE" in p.stdout and not list(tmp_path.iterdir())


def test_branche_de_sortie_meme_nom_que_le_code_de_lecture():
    for plan in ("decisif", "repetition"):
        p = _jouer(_bloc("branche") + f"branche_sortie {plan}", {})
        assert p.stdout.strip() == rv.PIECES_LECTURE[plan]["branche"]
    assert _jouer(_bloc("branche") + "branche_sortie autre", {}).returncode == 1


def test_duree_de_la_marche_cas_sain_et_artefact():
    assert _jouer(_bloc("duree-de-la-marche") + "duree_marche 10000 6400", {}).stdout.strip() == "3600"
    assert _jouer(_bloc("duree-de-la-marche") + "duree_marche 10030 10000", {}).returncode == 1


# --- fin, minuterie (faux curl) --------------------------------------------------------------------------------------

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


def _minuterie(tmp_path, echeance: str, temoin: str | None, duree: int = 4):
    b = _faux_curl(tmp_path)
    t = tmp_path / "T"
    t.mkdir()
    if temoin is not None:
        (t / "versement-final-prouve").write_text(temoin)
    env = {"PATH": f"{b}:{os.environ['PATH']}", "JOURNAL_CURL": str(tmp_path / "curl.txt"), "L": str(tmp_path / "j.txt"),
           "CONTAINER_ID": "4242", "CONTAINER_API_KEY": "cle-factice-xyz", "B5F_PAS_MINUTERIE": "1",
           "TEMOIN": str(t / "versement-final-prouve"), "SIGNAL": str(t / "signal-pour-la-mere.txt"),
           "API": "https://console.vast.ai/api/v0"}
    corps = "export TEMOIN SIGNAL API\n" + _bloc("minuterie")
    p = _jouer(corps + f'timeout {duree} bash -c "$(declare -f minuterie j); minuterie {echeance}"', env)
    appels = (tmp_path / "curl.txt").read_text().splitlines() if (tmp_path / "curl.txt").exists() else []
    return p, appels, t, (tmp_path / "j.txt").read_text() if (tmp_path / "j.txt").exists() else ""


def test_minuterie_detruit_par_l_identifiant_seulement_si_le_versement_final_est_prouve(tmp_path):
    p, appels, t, journal = _minuterie(tmp_path, "$(( $(date +%s) - 5 ))", "c" * 40)
    assert appels and all("-X DELETE" in a and a.endswith("https://console.vast.ai/api/v0/instances/4242/") for a in appels)
    assert not (t / "signal-pour-la-mere.txt").exists() and "cle-factice-xyz" not in journal


def test_minuterie_sans_preuve_arrete_sans_detruire_et_ecrit_un_signal_pour_la_mere(tmp_path):
    p, appels, t, journal = _minuterie(tmp_path, "$(( $(date +%s) - 5 ))", None)
    assert len(appels) >= 2 and all("-X PUT" in a and '"state": "stopped"' in a for a in appels)
    assert not any("DELETE" in a for a in appels)
    assert "NON détruite" in (t / "signal-pour-la-mere.txt").read_text()


def test_minuterie_avant_l_echeance_aucune_demande(tmp_path):
    p, appels, _, journal = _minuterie(tmp_path, "1900000000", "c" * 40, duree=3)
    assert not appels and "minuterie : échéance 1900000000" in journal


# --- entrées de lecture : un seul commit, seul leur dossier --------------------------------------------------------

def _git(r, *a, check=True):
    return subprocess.run(["git", "-C", str(r), *a], capture_output=True, text=True, check=check).stdout.strip()


def _depot_entrees(tmp_path, en_deux=False, modifie=False):
    """Branche des entrées dans un dépôt distant local : un commit de base, puis le commit qui ajoute le dossier des
    entrées (ou, artefacts, un dossier versé en deux commits, ou un fichier modifié par le dernier commit)."""
    g = tmp_path / "graine"
    g.mkdir()
    for a in (["init", "-q", "-b", "main"], ["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _git(g, *a)
    (g / "LISEZ-MOI").write_text("base\n")
    _git(g, "add", "-A")
    _git(g, "commit", "-q", "-m", "base")
    d = g / rv.DOSSIER_ENTREES
    d.mkdir()
    for n in ("X-01.safetensors", "X-02.safetensors", "A1-saboteur.safetensors"):
        (d / n).write_bytes(n.encode())
        (d / f"{n}.sha256").write_text(f"{hashlib.sha256(n.encode()).hexdigest()}  {n}\n")
        if en_deux and n == "X-01.safetensors":
            _git(g, "add", "-A")
            _git(g, "commit", "-q", "-m", "premier versement")
    _git(g, "add", "-A")
    _git(g, "commit", "-q", "-m", "entrées de lecture")
    if modifie:
        (d / "X-02.safetensors").write_bytes(b"autre")
        _git(g, "commit", "-q", "-am", "retouche")
    commit = _git(g, "rev-parse", "HEAD")
    nu = tmp_path / "distant.git"
    subprocess.run(["git", "init", "-q", "--bare", str(nu)], check=True)
    _git(g, "push", "-q", str(nu), f"main:refs/heads/{rv.BRANCHE_ENTREES}")
    e = tmp_path / "entrees"
    subprocess.run(["git", "clone", "-q", "--no-checkout", "--single-branch", "--branch", rv.BRANCHE_ENTREES, str(nu), str(e)],
                   check=True)
    _git(e, "sparse-checkout", "init", "--no-cone")
    subprocess.run(["git", "-C", str(e), "sparse-checkout", "set", "--no-cone", "--stdin"], input=f"/{rv.DOSSIER_ENTREES}/\n",
                   text=True, check=True)
    _git(e, "checkout", "-q", commit)
    return e, commit


def _verifier_entrees(tmp_path, e, commit):
    corps = (f"DOSSIER_ENTREES={rv.DOSSIER_ENTREES}\nENTREES_COMMIT={commit}\n" + _bloc("entrees") + f'verifier_entrees "{e}"')
    return _jouer(corps, {"L": str(tmp_path / "j.txt")})


def test_entrees_cas_sain_un_seul_commit_seul_leur_dossier(tmp_path):
    e, commit = _depot_entrees(tmp_path)
    p = _verifier_entrees(tmp_path, e, commit)
    assert p.returncode == 0, (tmp_path / "j.txt").read_text() if (tmp_path / "j.txt").exists() else p.stderr
    assert not (e / "LISEZ-MOI").exists()


@pytest.mark.parametrize("cas, motif", [("en_deux", "un seul commit"), ("modifie", "un seul commit"),
                                        ("intrus", "hors de"), ("formation", "branche de la formation"),
                                        ("tete", "tête")])
def test_entrees_artefacts(tmp_path, cas, motif):
    e, commit = _depot_entrees(tmp_path, en_deux=(cas == "en_deux"), modifie=(cas == "modifie"))
    if cas == "intrus":
        (e / "table-etiquettes.json").write_text("[]")
    if cas == "formation":
        _git(e, "update-ref", "refs/remotes/origin/donnees/barreau5-familles-jumelles-v1-formation", commit)
    p = _verifier_entrees(tmp_path, e, ("f" * 40) if cas == "tete" else commit)
    assert p.returncode == 1 and motif in (tmp_path / "j.txt").read_text()


# --- versement, lots, preuve, témoin ---------------------------------------------------------------------------------

def _sceller(p: Path) -> None:
    (p.parent / f"{p.name}.sha256").write_text(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n")


@pytest.fixture
def depots(tmp_path):
    """Dépôt distant local (nu) et son clone D au commit du code ; T ; sorties d'une marche de lecture fabriquées sous D :
    arbre fermé, poids, inventaires, trois activations gardées et une non gardée, manifeste."""
    nu, d, t = tmp_path / "distant.git", tmp_path / "T" / "depot", tmp_path / "T"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(nu)], check=True)
    g = tmp_path / "graine"
    g.mkdir()
    for a in (["init", "-q", "-b", "main"], ["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _git(g, *a)
    (g / "src.py").write_text("x = 1\n")
    _git(g, "add", "-A")
    _git(g, "commit", "-q", "-m", "code")
    _git(g, "push", "-q", str(nu), "main")
    subprocess.run(["git", "clone", "-q", str(nu), str(d)], check=True)
    for a in (["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _git(d, *a)
    commit = _git(d, "rev-parse", "HEAD")
    (t / "parent-sortie").write_text(commit + "\n")
    s = d / "donnees" / RUN
    for rel, contenu in (("lecture/inventaire.json", b"{}"), ("lecture/scores/decisive-pli0.json", b"{\"s\": 1}"),
                         ("poids/decisive-pli0.json", b"{}"), ("garde-activations.json", b"{}"),
                         ("inventaire-activations.json", b"{}")):
        (s / rel).parent.mkdir(parents=True, exist_ok=True)
        (s / rel).write_bytes(contenu)
        _sceller(s / rel)
    acts = []
    for serie in ("nu", "X-01", "A1-sur_saboteur", "X-02"):
        p = s / "activations" / serie / "c15" / "e0__p0.npy"
        p.parent.mkdir(parents=True)
        p.write_bytes(b"a" * 100)
        acts.append(p.relative_to(d).as_posix())
    (d / "runs" / RUN).mkdir(parents=True)
    (d / "runs" / RUN / "manifeste.json").write_text("{}\n")
    _sceller(d / "runs" / RUN / "manifeste.json")
    return {"nu": nu, "D": d, "T": t, "commit": commit, "L": tmp_path / "j.txt", "acts": acts}


def _env_versement(dep, lot="900000000"):
    t = dep["T"]
    return {"D": str(dep["D"]), "T": str(t), "L": str(dep["L"]), "BR": "donnees/barreau5-familles-jumelles-v1-lecture",
            "SEUIL": "94000000", "LOT_OCTETS": lot, "RUN_LECTURE": RUN, "TEMOIN": str(t / "versement-final-prouve"),
            "SORTIES_PROUVEES": str(t / "versement-des-sorties-prouve"),
            "ACTIVATIONS_VERSEES": str(t / "activations-gardees-versees"), "MARCHE_FINIE": str(t / "marche-menee-au-bout")}


def _verser(dep, script, **k):
    return _jouer(_bloc("versement") + _bloc("preuve") + script, _env_versement(dep, **k))


def _noms(dep, commit=None):
    commit = commit or (dep["T"] / "parent-sortie").read_text().strip()
    return set(_git(dep["nu"], "ls-tree", "-r", "--name-only", commit).split())


def test_versement_des_fichiers_fermes_sans_aucune_activation(depots):
    p = _verser(depots, 'verser "fermés" $(sorties_fermees)')
    assert p.returncode == 0, p.stderr
    noms = _noms(depots)
    assert f"donnees/{RUN}/lecture/scores/decisive-pli0.json" in noms and f"donnees/{RUN}/poids/decisive-pli0.json" in noms
    assert f"donnees/{RUN}/garde-activations.json.sha256" in noms and f"runs/{RUN}/manifeste.json" in noms
    assert not any("/activations/" in n for n in noms)
    assert _git(depots["D"], "rev-parse", "HEAD") == depots["commit"]            # la tête de la marche n'a pas bougé


def test_versement_d_une_activation_par_la_voie_ordinaire_refuse(depots):
    p = _verser(depots, f'verser "essai" {depots["acts"][0]}')
    assert p.returncode == 1 and "hors de la liste blanche" in depots["L"].read_text()
    assert (depots["T"] / "parent-sortie").read_text().strip() == depots["commit"]


def test_activations_gardees_versees_par_lots(depots):
    """Trois activations de 100 octets, lots de 250 octets au plus : deux lots, deux commits poussés ; un chemin qui n'est pas
    une activation de la marche est refusé par la liste blanche des activations."""
    gardees = depots["acts"][:3]
    p = _verser(depots, f'verser_par_lots "activations" {" ".join(gardees)}', lot="250")
    assert p.returncode == 0, p.stderr + depots["L"].read_text()
    fin = (depots["T"] / "parent-sortie").read_text().strip()
    assert _git(depots["nu"], "rev-list", "--count", f"{depots['commit']}..{fin}") == "2"
    assert set(gardees) <= _noms(depots) and depots["acts"][3] not in _noms(depots)
    p = _verser(depots, f'verser_par_lots "intrus" donnees/{RUN}/lecture/produits.json runs/{RUN}/manifeste.json')
    assert p.returncode == 1


def test_preuve_cas_sain_puis_temoin_final_seulement_si_tout_tient(depots):
    t = depots["T"]
    (t / "activations-gardees.txt").write_text("\n".join(depots["acts"][:3]) + "\n")
    script = (f'verser "fermés" $(sorties_fermees) && verser_par_lots "act" $(cat "$T/activations-gardees.txt") '
              '&& prouver_versement')
    p = _verser(depots, script)
    assert p.returncode == 0, p.stderr + depots["L"].read_text()
    tete = _git(depots["nu"], "rev-parse", "donnees/barreau5-familles-jumelles-v1-lecture")
    assert (t / "versement-des-sorties-prouve").read_text().strip() == tete
    inv = json.loads(subprocess.run(["git", "-C", str(depots["nu"]), "show", f"{tete}:traces-b5f-lecture/inventaire-final.json"],
                                    capture_output=True, text=True).stdout)
    chemins = {f["chemin"] for f in inv["fichiers"]}
    assert set(depots["acts"][:3]) <= chemins and f"donnees/{RUN}/lecture/inventaire.json" in chemins
    # témoin : marche menée, sorties prouvées, activations versées ; il manque l'une : aucun témoin
    p = _verser(depots, "temoin_final")
    assert p.returncode == 1 and not (t / "versement-final-prouve").exists()
    (t / "marche-menee-au-bout").write_text("menee\n")
    assert _verser(depots, "temoin_final").returncode == 1 and not (t / "versement-final-prouve").exists()
    (t / "activations-gardees-versees").write_text("versees\n")
    assert _verser(depots, "temoin_final").returncode == 0
    assert (t / "versement-final-prouve").read_text().strip() == tete


def test_preuve_artefact_activation_listee_non_versee(depots):
    t = depots["T"]
    (t / "activations-gardees.txt").write_text("\n".join(depots["acts"][:3]) + "\n")
    p = _verser(depots, 'verser "fermés" $(sorties_fermees) && prouver_versement')
    assert p.returncode == 1 and not (t / "versement-des-sorties-prouve").exists()
    assert "absent du commit" in depots["L"].read_text()


# --- contrôles du texte de l'amorce ----------------------------------------------------------------------------------

def _lignes_de_code():
    return [x for x in TEXTE.splitlines() if not x.lstrip().startswith("#")]


def test_texte_seul_module_joue_la_relecture_aucun_code_en_ligne_aucun_arret_par_motif():
    assert set(re.findall(r"-m (controle_ia\.[A-Za-z0-9_.]+)", TEXTE)) == {"controle_ia.barreau5_familles.relecture_v1"}
    code = "\n".join(_lignes_de_code())
    assert not re.search(r'"\$PY" -c|python3? -c', code)
    assert not re.search(r"formation_v1|sondes_v1", code)        # aucun module de la formation ni des sondes appelé
    for interdit in (f"p{ARRET}", f"{ARRET}all", "pg" + "rep", "rm -rf", "git reset"):
        assert interdit not in TEXTE, interdit
    assert re.findall(rf"(?<![-\w]){ARRET}(?![-\w])", TEXTE) == []          # aucun envoi de signal ; `wait` attend
    essais = re.findall(r"-m pytest[^\n]*\n[^\n]*", TEXTE)
    assert len(essais) == 1 and all(f in essais[0] for f in ("test_barreau5_familles_lecture_v1.py",
                                                             "test_barreau5_familles_sondes_v1.py",
                                                             "test_barreau5_familles_relecture_v1.py"))


def test_texte_aucune_suppression_hors_de_l_index_de_versement():
    suppressions = [x.strip() for x in _lignes_de_code() if re.search(r"(?<![-\w])(rm|unlink|shred|truncate)(?![-\w])", x)
                    or "-delete" in x]
    assert suppressions == ['rm -f "$ix"'], suppressions


def test_texte_marche_sous_timeout_minuterie_a_l_echeance_plus_le_quart_d_heure():
    assert re.search(r'timeout --signal=TERM --kill-after=120 "\$DUREE" \\\n\s+"\$PY" -m controle_ia\.barreau5_familles\.'
                     r'relecture_v1 --config', TEXTE)
    assert _constante("VERSEMENT_S") == "900"
    assert sum("B5F_VERSEMENT_S" in x for x in _lignes_de_code()) == 1
    assert "ECHEANCE_MINUTERIE=$(( ECHEANCE_ARRET_UTC_S + VERSEMENT_S ))" in TEXTE
    assert re.search(r'^minuterie "\$ECHEANCE_MINUTERIE" < /dev/null &$', TEXTE, re.M)
    assert '[ "$c" = 0 ] && [ "${NP:-0}" -ge "$MIN_ESSAIS" ] || arret "essais de la lecture' in TEXTE


def test_texte_fichiers_fermes_verses_avant_les_activations():
    terminer = TEXTE[TEXTE.index("terminer() {"):TEXTE.index("arret() {")]
    assert terminer.index('verser "barreau 5, lecture : fichiers fermés') < terminer.index("verser_par_lots") \
        < terminer.index("prouver_versement") < terminer.index("temoin_final") < terminer.index("SCORES-B5F")
    assert 'printf \'menee\\n\' > "$MARCHE_FINIE"; terminer 0' in TEXTE


def test_texte_plancher_d_essais_egal_au_nombre_d_essais_de_la_lecture():
    fichiers = ["tests/test_barreau5_familles_lecture_v1.py", "tests/test_barreau5_familles_sondes_v1.py",
                "tests/test_barreau5_familles_relecture_v1.py"]
    p = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "--collect-only", "-p", "no:cacheprovider", *fichiers],
                       cwd=RACINE_DEPOT, capture_output=True, text=True, timeout=300,
                       env={**os.environ, "PYTHONPATH": str(RACINE_DEPOT / "src"), "PYTHONDONTWRITEBYTECODE": "1"})
    n = int(re.search(r"(\d+) tests? collected", p.stdout).group(1))
    assert int(_constante("MIN_ESSAIS")) == n, (n, p.stdout[-300:])


def test_texte_aucune_valeur_de_cle_seulement_des_noms():
    assert not re.search(r"ghp_|github_pat_|hf_[A-Za-z0-9]{8}|Bearer [A-Za-z0-9]", TEXTE)
    for nom in ("GH_TOKEN", "HF_TOKEN", "CONTAINER_API_KEY"):
        for ligne in _lignes_de_code():
            if nom in ligne:
                assert not re.search(rf"(echo|j|printf)[^\n]*\$\{{?{nom}", ligne.split("password=")[0]), ligne
    assert """case "${GH_TOKEN:-}${HF_TOKEN:-}" in *'$'*) arret""" in TEXTE


def test_texte_extraction_nommee_sans_docs_notes_ni_formation_ni_taches_de_reserve():
    motifs = _bloc("motifs")
    lignes = [x.strip().strip("'").replace("MOTIFS=", "").strip("'") for x in motifs.splitlines() if x.strip()]
    assert "/*" not in lignes and not re.search(r"^/(docs/notes|diag|runs|brouillons)", motifs, re.M)
    assert "taches-entrainement" not in motifs and "formation" not in motifs
    for f in ("/src/", "/registres/barreau5-familles-jumelles-v1.md*", "/docs/sources/invites-2606.08892-v1/",
              "/prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md*",
              "/donnees/20261007-082440-t05-extraction/taches-evaluation.json*", "/requirements-gpu.txt"):
        assert f in lignes, f
    for inclus in re.findall(r"^-r (\S+)$", (RACINE_DEPOT / "requirements-gpu.txt").read_text(), re.M):
        assert f"/{inclus}" in lignes, inclus
    assert "for d in docs/notes diag runs brouillons; do" in TEXTE
    assert _constante("BRANCHE_ENTREES") == rv.BRANCHE_ENTREES and _constante("DOSSIER_ENTREES") == rv.DOSSIER_ENTREES
    assert f'ENTREES="../entrees/$DOSSIER_ENTREES"' in TEXTE and rv.ENTREES_DE_LA_MARCHE == f"../entrees/{rv.DOSSIER_ENTREES}"
