"""Essais hors ligne de l'amorce d'instance de la formation du barreau 5 (`scripts/amorce_b5f_formation_v1.sh`) : rien n'est
lancé pour de vrai. L'essai local de l'amorce entière (arguments), puis ses blocs marqués, extraits et joués dans un bash
jetable avec un faux `curl` et un dépôt distant local ; enfin, des contrôles du texte. Cas sain et artefact (R5). L'amorce
entière, jouée à blanc avec de faux outils, est éprouvée par `tests/test_amorce_b5f_formation_entiere_v1.py`. Corrigés le
19 novembre 2026 selon la contre-lecture du code de formation (constats M-1, M-2, M-5, M-9, m-1, m-6, m-7, m-12), puis
selon sa vérification (constats n-3 et n-7)."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import pytest

from controle_ia.barreau5_familles import formation_v1 as fv

RACINE_DEPOT = Path(__file__).resolve().parents[1]
AMORCE = RACINE_DEPOT / "scripts" / "amorce_b5f_formation_v1.sh"
TEXTE = AMORCE.read_text(encoding="utf-8")
RUN = "20261123-080000-b5f-formation-3"
SAINS = {"INSTANCE_B5F": "3", "RELANCE_B5F": "0", "COMMIT": "a" * 40, "BRANCHE_CODE": "lot/b5f-v1",
         "PREREG": "prereg/barreau5-texte.md", "RUN_B5F": RUN, "PRIX_USD_H": "1.2", "ECHEANCE_ARRET_UTC_S": "1900000000",
         "GO_ID": "GO-2026-11-20-01", "DEPOT_URL": "https://github.com/lciric/controle-ia-travail.git"}


def _bloc(nom: str) -> str:
    m = re.search(rf"^# >>> {re.escape(nom)}\b.*?$(.*?)^# <<< {re.escape(nom)}$", TEXTE, re.S | re.M)
    assert m, nom
    return m.group(1)


def _constante(nom: str) -> str:
    m = re.search(rf"^{nom}=(\S+)$", TEXTE, re.M)
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


def test_essai_local_cas_sain_arguments_conformes_rien_ecrit(tmp_path):
    for sup in ({}, {"RELANCE_B5F": "1", "RUN_B5F": RUN + "-x1"}):
        p = subprocess.run(["bash", str(AMORCE)], env=_env(AMORCE_ESSAI_LOCAL="1", RACINE_AMORCE=str(tmp_path), **sup),
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0 and "arguments conformes" in p.stdout, p.stdout + p.stderr
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("sup, motif", [
    ({"COMMIT": None}, "COMMIT absente"), ({"INSTANCE_B5F": "8"}, "1 à 7"), ({"COMMIT": "a" * 39}, "40 caractères"),
    ({"COMMIT": "g" * 40}, "COMMIT illisible"), ({"BRANCHE_CODE": "a b"}, "BRANCHE_CODE"),
    ({"PREREG": "prereg/../x.md"}, "PREREG"), ({"PREREG": "docs/notes/x.md"}, "PREREG"),
    ({"RUN_B5F": "20261123-080000-b5f-formation-4"}, "autre instance"), ({"PRIX_USD_H": "1.35"}, "hors de"),
    ({"PRIX_USD_H": "un"}, "illisible"), ({"ECHEANCE_ARRET_UTC_S": "demain"}, "illisible"), ({"GO_ID": "GO-26-1"}, "GO_ID"),
    ({"DEPOT_URL": "https://github.com/lciric/controle-ia.git"}, "copie publique"),
    ({"RELANCE_B5F": None}, "RELANCE_B5F absente"), ({"RELANCE_B5F": "2"}, "0 ou 1"),
    ({"RELANCE_B5F": "1"}, "suffixe de la relance"), ({"RUN_B5F": RUN + "-x1"}, "suffixe de la relance"),
    ({"B5F_PERIODE_VERSEMENT_S": "0"}, "période")])
def test_essai_local_artefacts_arguments_refuses(tmp_path, sup, motif):
    p = subprocess.run(["bash", str(AMORCE)], env=_env(AMORCE_ESSAI_LOCAL="1", RACINE_AMORCE=str(tmp_path), **sup),
                       capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and motif in p.stdout, p.stdout
    assert not list(tmp_path.iterdir())


def test_quart_d_heure_du_versement_raccourci_en_essai_a_blanc_seulement(tmp_path):
    """Constat n-3 : B5F_VERSEMENT_S n'est lu qu'en essai à blanc. Hors de lui, il est ignoré (l'essai local passe avec une
    valeur illisible) ; en essai à blanc, une valeur illisible arrête l'amorce avant tout, sans rien écrire."""
    p = subprocess.run(["bash", str(AMORCE)], env=_env(AMORCE_ESSAI_LOCAL="1", RACINE_AMORCE=str(tmp_path),
                                                       B5F_VERSEMENT_S="2m"), capture_output=True, text=True, timeout=60)
    assert p.returncode == 0 and "arguments conformes" in p.stdout, p.stdout + p.stderr
    p = subprocess.run(["bash", str(AMORCE)], env=_env(AMORCE_ESSAI_BLANC="1", RACINE_AMORCE=str(tmp_path),
                                                       B5F_VERSEMENT_S="2m"), capture_output=True, text=True, timeout=60)
    assert p.returncode == 2 and "quart d'heure du versement illisible" in p.stdout, p.stdout + p.stderr
    assert not list(tmp_path.iterdir())


def test_artefact_racine_amorce_hors_essai_refusee(tmp_path):
    p = subprocess.run(["bash", str(AMORCE)], env=_env(RACINE_AMORCE=str(tmp_path)), capture_output=True, text=True,
                       timeout=60)
    assert p.returncode == 2 and "essai local seulement" in p.stdout


def _jouer(script: str, env_sup: dict, timeout: int = 30) -> subprocess.CompletedProcess:
    entete = 'set -uo pipefail\nj() { printf "%s\\n" "$*" >> "$L"; }\n'
    return subprocess.run(["bash", "-c", entete + script], env=_env(**env_sup), capture_output=True, text=True,
                          timeout=timeout)


def test_branche_de_sortie_meme_nom_que_le_code_de_formation():
    """Constat m-12 : la branche de sortie de l'amorce est celle de `formation_v1.branche_sortie`, relance comprise."""
    for n in range(1, 8):
        for relance in (0, 1):
            p = _jouer(_bloc("branche") + f"branche_sortie {n} {relance}", {})
            assert p.stdout.strip() == fv.branche_sortie(n, relance == 1), p.stderr


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
    """Constat M-2 : à l'échéance, témoin de versement prouvé présent : DELETE par l'identifiant, et rien d'autre."""
    p, appels, t, journal = _minuterie(tmp_path, "$(( $(date +%s) - 5 ))", "c" * 40)
    assert appels and all("-X DELETE" in a and a.endswith("https://console.vast.ai/api/v0/instances/4242/")
                          for a in appels), p.stderr
    assert "versement final prouvé" in journal and not (t / "signal-pour-la-mere.txt").exists()
    assert "cle-factice-xyz" not in journal


def test_minuterie_sans_preuve_arrete_sans_detruire_et_ecrit_un_signal_pour_la_mere(tmp_path):
    """Constat M-2 (règle « récupérer ce qui est récupérable ») : à l'échéance, sans preuve du versement final, l'instance
    est arrêtée (état « stopped », par l'identifiant, demande refaite), jamais détruite ; un signal l'écrit pour la mère."""
    p, appels, t, journal = _minuterie(tmp_path, "$(( $(date +%s) - 5 ))", None)
    assert len(appels) >= 2 and all("-X PUT" in a and '"state": "stopped"' in a and "/instances/4242/" in a
                                    for a in appels), p.stderr
    assert not any("DELETE" in a for a in appels)
    signal = (t / "signal-pour-la-mere.txt").read_text()
    assert "SIGNAL POUR LA MÈRE" in signal and "NON détruite" in signal and "SIGNAL POUR LA MÈRE" in journal


def test_minuterie_avant_l_echeance_aucune_demande_et_echeance_ecrite(tmp_path):
    p, appels, _, journal = _minuterie(tmp_path, "1900000000", "c" * 40, duree=3)
    assert not appels and "minuterie : échéance 1900000000" in journal


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _sceller(p: Path, faux: bool = False) -> None:
    (p.parent / f"{p.name}.sha256").write_text(f"{'0' * 64 if faux else _sha(p)}  {p.name}\n")


@pytest.fixture
def depots(tmp_path):
    """Dépôt distant local (nu) et son clone D au commit COMMIT ; T, dossier de travail de l'amorce ; sorties d'une marche
    fabriquées sous D (permises par la liste blanche) : scellées, non scellées, à faux compagnon."""
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
    sorties = d / "donnees" / RUN / "T03"
    sorties.mkdir(parents=True)
    for nom, contenu in (("adaptateur-jumeau.pt", b"p" * 300), ("tirage.jsonl", b"{}")):
        (sorties / nom).write_bytes(contenu)
        _sceller(sorties / nom)
    (sorties / "evaluation-jumeau.jsonl").write_text("{}")                     # sans compagnon
    (sorties / "textes-distillation.jsonl").write_text("{}")
    _sceller(sorties / "textes-distillation.jsonl", faux=True)                   # compagnon faux
    (d / "runs" / RUN).mkdir(parents=True)
    (d / "runs" / RUN / "manifeste.json").write_text("{}\n")
    _sceller(d / "runs" / RUN / "manifeste.json")
    return {"nu": nu, "D": d, "T": t, "commit": commit, "L": tmp_path / "j.txt"}


def _verser(dep, script, seuil="94000000"):
    env = {"D": str(dep["D"]), "T": str(dep["T"]), "L": str(dep["L"]), "BR": "donnees/b5f-essai-instance-3",
           "SEUIL": seuil, "TEMOIN": str(dep["T"] / "versement-final-prouve"), "INSTANCE_B5F": "3"}
    return _jouer(_bloc("versement") + _bloc("preuve") + script, env)


def _git(r, *a):
    return subprocess.run(["git", "-C", str(r), *a], capture_output=True, text=True).stdout.strip()


def test_versement_cas_sain_fichiers_scelles_seulement_tete_inchangee(depots):
    p = _verser(depots, f"fichiers_scelles donnees/{RUN}")
    base = f"donnees/{RUN}/T03"
    assert p.stdout.split() == [f"{base}/adaptateur-jumeau.pt", f"{base}/adaptateur-jumeau.pt.sha256",
                                f"{base}/tirage.jsonl", f"{base}/tirage.jsonl.sha256"]
    p = _verser(depots, f'verser "essai" $(fichiers_scelles donnees/{RUN})')
    assert p.returncode == 0, p.stderr
    pousse = _git(depots["nu"], "rev-parse", "donnees/b5f-essai-instance-3")
    assert pousse == (depots["T"] / "parent-sortie").read_text().strip()
    assert _git(depots["nu"], "rev-parse", f"{pousse}^") == depots["commit"]
    assert subprocess.run(["git", "-C", str(depots["nu"]), "show", f"{pousse}:{base}/adaptateur-jumeau.pt"],
                          capture_output=True).stdout == b"p" * 300
    assert _git(depots["D"], "rev-parse", "HEAD") == depots["commit"]            # la tête de la marche n'a pas bougé
    assert (depots["D"] / base / "adaptateur-jumeau.pt").exists()               # rien n'est supprimé
    # rien de neuf : aucun commit de plus
    assert _verser(depots, f'verser "essai 2" $(fichiers_scelles donnees/{RUN})').returncode == 0
    assert (depots["T"] / "parent-sortie").read_text().strip() == pousse
    # versement final : tous les fichiers, scellés ou non
    assert _verser(depots, f'verser "fin" $(tous_les_fichiers donnees/{RUN} runs/{RUN})').returncode == 0
    fin = (depots["T"] / "parent-sortie").read_text().strip()
    noms = _git(depots["nu"], "ls-tree", "-r", "--name-only", fin).split()
    assert f"{base}/evaluation-jumeau.jsonl" in noms and f"{base}/textes-distillation.jsonl" in noms
    assert f"runs/{RUN}/manifeste.json" in noms


def test_versement_un_gros_fichier_n_empeche_pas_les_autres(depots):
    """Constat m-1 : un fichier au-dessus du seuil reste sur le disque, noté au journal ; les autres sont poussés ; le
    code est 1 (versement incomplet)."""
    p = _verser(depots, f'verser "essai" $(tous_les_fichiers donnees/{RUN})', seuil="200")
    assert p.returncode == 1 and "plus de 200 octets" in depots["L"].read_text()
    fin = (depots["T"] / "parent-sortie").read_text().strip()
    assert fin != depots["commit"]
    noms = _git(depots["nu"], "ls-tree", "-r", "--name-only", fin).split()
    assert f"donnees/{RUN}/T03/tirage.jsonl" in noms and f"donnees/{RUN}/T03/adaptateur-jumeau.pt" not in noms
    assert (depots["D"] / "donnees" / RUN / "T03" / "adaptateur-jumeau.pt").exists()


def test_versement_artefacts_hors_liste_blanche_ou_distant_injoignable(depots):
    """Liste d'arrêt, point 5 : un fichier hors de la liste blanche ne sort pas de l'instance (gardé sur le disque, noté) ;
    dépôt distant injoignable : code 1, parent inchangé."""
    interdit = depots["D"] / "donnees" / RUN / "T03" / "activations.npy"
    interdit.write_bytes(b"x")
    p = _verser(depots, f'verser "essai" $(tous_les_fichiers donnees/{RUN})')
    assert p.returncode == 1 and "hors de la liste blanche" in depots["L"].read_text()
    fin = (depots["T"] / "parent-sortie").read_text().strip()
    assert f"donnees/{RUN}/T03/activations.npy" not in _git(depots["nu"], "ls-tree", "-r", "--name-only", fin).split()
    assert interdit.exists()
    subprocess.run(["git", "-C", str(depots["D"]), "remote", "set-url", "origin", str(depots["T"] / "absent.git")],
                   check=True)
    (depots["D"] / "donnees" / RUN / "T03" / "evaluation-saboteur.jsonl").write_text("{}")
    p = _verser(depots, f'sleep() {{ :; }}; verser "essai" $(tous_les_fichiers donnees/{RUN})')
    assert p.returncode == 1 and (depots["T"] / "parent-sortie").read_text().strip() == fin


def test_preuve_du_versement_final_cas_sain_inventaire_pousse_relu_et_accepte_par_la_session(depots):
    """Constat M-2 : inventaire (noms, tailles, empreintes) de tout ce qui existe, poussé, relu sur le dépôt distant ;
    témoin écrit avec le commit prouvé ; l'inventaire poussé suffit à la preuve de la session avant destruction."""
    script = (f'verser "fin" $(tous_les_fichiers donnees/{RUN} runs/{RUN}) && RUN_B5F={RUN} prouver_versement')
    p = _verser(depots, script)
    assert p.returncode == 0, p.stderr + depots["L"].read_text()
    tete = _git(depots["nu"], "rev-parse", "donnees/b5f-essai-instance-3")
    assert (depots["T"] / "versement-final-prouve").read_text().strip() == tete
    inv = json.loads(subprocess.run(["git", "-C", str(depots["nu"]), "show", f"{tete}:traces-b5f/inventaire-final.json"],
                                    capture_output=True, text=True).stdout)
    chemins = {f["chemin"]: f for f in inv["fichiers"]}
    assert inv["run_id"] == RUN and f"donnees/{RUN}/T03/adaptateur-jumeau.pt" in chemins
    assert chemins[f"donnees/{RUN}/T03/adaptateur-jumeau.pt"]["octets"] == 300
    subprocess.run(["git", "-C", str(depots["D"]), "fetch", "-q", "origin"], check=True)
    assert fv.exiger_versement(depots["D"], depots["D"] / "traces-b5f" / "inventaire-final.json", tete)["fichiers"] == \
        len(inv["fichiers"])


@pytest.mark.parametrize("cas", ["hors_liste_blanche", "gros_fichier", "tete_distante_autre", "distant_injoignable"])
def test_preuve_artefacts_aucun_temoin(depots, cas):
    """Sans versement complet prouvé, aucun témoin : la minuterie arrêtera l'instance sans la détruire."""
    seuil = "94000000"
    if cas == "hors_liste_blanche":
        (depots["D"] / "donnees" / RUN / "T03" / "journal-interne-jumeau.pt").write_bytes(b"x")
    elif cas == "gros_fichier":
        seuil = "200"
    script = f'verser "fin" $(tous_les_fichiers donnees/{RUN} runs/{RUN}); '
    if cas == "tete_distante_autre":                 # quelqu'un d'autre a poussé sur la branche après nous
        script += ('autre=$(git -C "$D" commit-tree "$(cat "$T/parent-sortie")^{tree}" -p "$(cat "$T/parent-sortie")" '
                   '-m autre); git -C "$D" push -q origin "$autre:refs/heads/$BR"; sleep() { :; }; ')
    elif cas == "distant_injoignable":
        script += f'git -C "$D" remote set-url origin "$T/absent.git"; sleep() {{ :; }}; '
    p = _verser(depots, script + f"RUN_B5F={RUN} prouver_versement", seuil=seuil)
    assert p.returncode == 1
    assert not (depots["T"] / "versement-final-prouve").exists()


@pytest.mark.parametrize("cas", ["branche_supprimee", "branche_ramenee_au_depart"])
def test_preuve_artefact_tete_distante_seule_aucun_temoin(depots, cas):
    """Constat n-7 de la vérification (mutation V01) : la comparaison de la tête distante est le seul verrou qui joue quand
    le versement de l'inventaire ne pousse rien de neuf alors que la branche distante a bougé. Première preuve tenue ;
    témoin retiré ; branche distante supprimée, ou ramenée au commit de départ ; seconde preuve : rien de neuf n'est
    poussé, aucun témoin, et le refus dit pourquoi."""
    premiere = _verser(depots, f'verser "fin" $(tous_les_fichiers donnees/{RUN} runs/{RUN}) && RUN_B5F={RUN} prouver_versement')
    temoin = depots["T"] / "versement-final-prouve"
    assert premiere.returncode == 0 and temoin.is_file(), premiere.stderr
    prouve = temoin.read_text().strip()
    temoin.unlink()
    branche = "refs/heads/donnees/b5f-essai-instance-3"
    if cas == "branche_supprimee":
        subprocess.run(["git", "-C", str(depots["nu"]), "update-ref", "-d", branche], check=True)
    else:
        subprocess.run(["git", "-C", str(depots["nu"]), "update-ref", branche, depots["commit"]], check=True)
    seconde = _verser(depots, f"RUN_B5F={RUN} prouver_versement")
    assert seconde.returncode == 1 and not temoin.exists()
    assert (depots["T"] / "parent-sortie").read_text().strip() == prouve            # rien de neuf n'a été poussé
    assert depots["L"].read_text().rstrip().endswith("preuve : tête distante ≠ dernier commit poussé")


def test_preuve_artefact_inventaire_refuse_par_le_distant_aucun_temoin(depots):
    """Mutation V02 du vérificateur, isolée (elle passait seule, couverte par la relecture) : les sorties sont déjà
    poussées, puis le dépôt distant refuse le seul commit de l'inventaire. La tête distante égale encore le dernier commit
    poussé et chaque sortie inventoriée y est : seul l'échec du versement de l'inventaire refuse la preuve ; aucun témoin."""
    crochet = depots["nu"] / "hooks" / "pre-receive"
    crochet.write_text("#!/usr/bin/env bash\nwhile read -r ancien neuf ref; do\n"
                       "    if git ls-tree -r --name-only \"$neuf\" | grep -qx 'traces-b5f/inventaire-final.json'; then\n"
                       "        echo 'refusé : inventaire' >&2; exit 1; fi\ndone\nexit 0\n", encoding="utf-8")
    crochet.chmod(0o755)
    p = _verser(depots, f'sleep() {{ :; }}; verser "fin" $(tous_les_fichiers donnees/{RUN} runs/{RUN}) '
                        f'&& RUN_B5F={RUN} prouver_versement')
    assert p.returncode == 1 and not (depots["T"] / "versement-final-prouve").exists()
    sorties = _git(depots["nu"], "ls-tree", "-r", "--name-only", "donnees/b5f-essai-instance-3").split()
    assert f"donnees/{RUN}/T03/adaptateur-jumeau.pt" in sorties and "traces-b5f/inventaire-final.json" not in sorties
    assert "versement final prouvé" not in depots["L"].read_text()


def test_attente_de_la_marche_rend_la_main_vite_apres_sa_fin():
    """Constat M-2 : aucun sommeil d'un seul tenant : l'attente rend la main au plus PAS_ATTENTE_S secondes après la fin
    de la marche (moins de 20 secondes), sans attendre la période de versement."""
    pas = int(_constante("PAS_ATTENTE_S"))
    assert pas <= 15
    env = {"PAS_ATTENTE_S": str(pas), "PERIODE_VERSEMENT_S": "600", "L": "/dev/null", "INSTANCE_B5F": "3", "RUN_B5F": RUN}
    debut = time.monotonic()
    p = _jouer("export PAS_ATTENTE_S PERIODE_VERSEMENT_S\n" + _bloc("attente") + "sleep 2 &\nattendre_la_marche $!\n", env,
               timeout=60)
    duree = time.monotonic() - debut
    assert p.returncode == 0 and 2 <= duree < 2 + pas + 3 < 20, (duree, p.stderr)


# --- contrôles du texte de l'amorce -------------------------------------------------------------------------------------

def _lignes_de_code():
    return [x for x in TEXTE.splitlines() if not x.lstrip().startswith("#")]


def test_texte_aucune_lecture_d_activation_ni_de_score_aucun_arret_par_motif():
    modules = set(re.findall(r"-m (controle_ia\.[A-Za-z0-9_.]+)", TEXTE))
    assert modules == {"controle_ia.barreau5_familles.formation_v1"}
    assert set(re.findall(r"from (controle_ia\.[A-Za-z0-9_.]+) import", TEXTE)) == {"controle_ia.harnais.modeles"}
    for interdit in ("sondes", "t07bbis", "relecture", "lecture_v1", "pkill", "killall", "pgrep", "rm -rf", "git reset"):
        assert interdit not in TEXTE, interdit
    assert re.findall(r"(?<![-\w])kill(?![-\w])[^\n]*", TEXTE) == ['kill -0 "$1" 2> /dev/null; do']   # sonde de vie seule
    essais = re.findall(r"-m pytest[^\n]*", TEXTE)
    assert len(essais) == 1 and "tests/test_barreau5_familles_*.py" in essais[0]


def test_texte_aucune_suppression_hors_de_l_index_de_versement():
    """Constat M-9, point 10 (mutation M07) : la seule commande de suppression de l'amorce est celle de son index de
    versement à part (`rm -f "$ix"`) ; aucune autre (`rm`, `git rm`, `unlink`, `shred`, `find -delete`, `truncate`)."""
    suppressions = [x.strip() for x in _lignes_de_code() if re.search(r"(?<![-\w])(rm|unlink|shred|truncate)(?![-\w])", x)
                    or "-delete" in x]
    assert suppressions == ['rm -f "$ix"'], suppressions


def test_texte_marche_sous_timeout_minuterie_a_l_echeance_plus_le_quart_d_heure_porte_des_essais():
    """Constat M-9, point 10 (mutations M14, M15, M21), contrôles du texte ; l'amorce entière les éprouve aussi."""
    assert re.search(r'timeout --signal=TERM --kill-after=120 "\$DUREE" \\\n\s+"\$PY" -m controle_ia\.barreau5_familles\.'
                     r'formation_v1 ', TEXTE)
    assert _constante("VERSEMENT_S") == "900"
    # constat n-3 : le quart d'heure ne se raccourcit qu'en essai à blanc, et en une seule ligne de code
    assert '[ "$BLANC" != 1 ] || VERSEMENT_S="${B5F_VERSEMENT_S:-900}"' in TEXTE
    assert sum("B5F_VERSEMENT_S" in x for x in _lignes_de_code()) == 1
    assert "ECHEANCE_MINUTERIE=$(( ECHEANCE_ARRET_UTC_S + VERSEMENT_S ))" in TEXTE
    assert re.search(r'^minuterie "\$ECHEANCE_MINUTERIE" < /dev/null &$', TEXTE, re.M)
    assert '[ "$c" = 0 ] && [ "${NP:-0}" -ge "$MIN_ESSAIS" ] || arret "essais du paquet' in TEXTE
    assert re.search(r'--relance "\$RELANCE_B5F"', TEXTE)


def test_texte_plancher_d_essais_egal_au_nombre_d_essais_du_paquet():
    """Le plancher MIN_ESSAIS de la porte des essais égale le nombre d'essais de `tests/test_barreau5_familles_*.py`
    (remesuré sur l'arbre extrait des fichiers corrigés)."""
    fichiers = sorted(str(p.relative_to(RACINE_DEPOT)) for p in (RACINE_DEPOT / "tests").glob("test_barreau5_familles_*.py"))
    p = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "--collect-only", "-p", "no:cacheprovider", *fichiers],
                       cwd=RACINE_DEPOT, capture_output=True, text=True, timeout=300,
                       env={**os.environ, "PYTHONPATH": str(RACINE_DEPOT / "src")})
    n = int(re.search(r"(\d+) tests? collected", p.stdout).group(1))
    assert int(_constante("MIN_ESSAIS")) == n, (n, p.stdout[-300:])


def test_texte_aucune_valeur_de_cle_seulement_des_noms_et_nom_recu_refuse():
    assert not re.search(r"ghp_|github_pat_|hf_[A-Za-z0-9]{8}|Bearer [A-Za-z0-9]", TEXTE)
    for nom in ("GH_TOKEN", "HF_TOKEN", "CONTAINER_API_KEY"):
        for ligne in TEXTE.splitlines():
            if nom in ligne and not ligne.lstrip().startswith("#"):
                assert re.search(rf"\$\{{{nom}(:-)?\}}|\$\{{{nom}:-\}}|{nom} absent", ligne) or f"variable {nom}" in ligne \
                    or f"{nom} (par" in ligne or "par le nom" in ligne, ligne
                assert not re.search(rf"(echo|j|printf)[^\n]*\$\{{?{nom}", ligne.split("password=")[0]), ligne
    assert """case "${GH_TOKEN:-}${HF_TOKEN:-}" in *'$'*) arret""" in TEXTE          # constat M-1


def test_texte_extraction_nommee_sans_docs_notes_ni_diag_et_branche_de_la_formation():
    """Constats m-6 et m-7 : la racine du dépôt n'est plus extraite en entier (motif « /* ») ; les fichiers nommés
    comprennent ceux qu'appelle `requirements-gpu.txt` ; l'amorce vérifie l'absence de docs/notes, diag, runs, brouillons."""
    motifs = _bloc("motifs")
    lignes = [x.strip().strip("'").replace("MOTIFS=", "").strip("'") for x in motifs.splitlines() if x.strip()]
    assert "/*" not in lignes and "!/*/" not in lignes
    assert "/src/" in motifs and "/registres/barreau5-familles-jumelles-v1.md*" in motifs
    assert not re.search(r"^/(docs/notes|diag|runs|brouillons)", motifs, re.M)
    assert "/docs/sources/invites-2606.08892-v1/" in motifs
    for f in ("requirements-gpu.txt", "pyproject.toml", ".gitignore"):
        assert f"/{f}" in lignes
    for inclus in re.findall(r"^-r (\S+)$", (RACINE_DEPOT / "requirements-gpu.txt").read_text(), re.M):
        assert f"/{inclus}" in lignes, inclus
    assert "for d in docs/notes diag runs brouillons; do" in TEXTE
    assert "donnees/barreau5-familles-jumelles-v1-formation-instance-$1$s" in _bloc("branche")
