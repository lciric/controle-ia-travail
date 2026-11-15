"""Essais R5 de la répétition sur carte de l'étape B bis (mot de Lazar R-2802 ; `scripts/repetition_carte_bbis_v1.py`,
`scripts/amorce_repetition_bbis_v1.sh`, `scripts/lancer_repetition_bbis_v1.sh`), chacun avec son cas sain et son artefact :
partie carte jouée sur processeur à petite taille (déterminisme, contrôle carte-processeur, arrêt écrit, seuil jamais relâché) ;
extraits de l'amorce de répétition joués par bash (motifs de la course, aucune entrée de 7b, installation bornée à code dédié,
traces poussées sur COMMIT, minuterie) ; lanceur (offre, commande, dépense à 3 USD, destruction avec -y vérifiée contre un faux
outil `vastai`). Dépôts et dossiers jetables seulement ; aucune donnée de 7a, 7b, T0.7 ni de P3-bis. Ce fichier ne suit pas le
motif `tests/test_t07bbis_*` : il n'entre ni dans les essais de l'instance de la course ni dans `MIN_ESSAIS`."""
from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import time
from pathlib import Path

import pytest

import aide_t07bbis_depot_v1 as ad

RACINE = ad.RACINE_DEPOT
SCRIPT = RACINE / "scripts" / "repetition_carte_bbis_v1.py"
AMORCE_REP = RACINE / "scripts" / "amorce_repetition_bbis_v1.sh"
LANCER_REP = RACINE / "scripts" / "lancer_repetition_bbis_v1.sh"
AUTRES = ("58936096", "58936099", "58936100", "60480302", "60599797", "60670453")


def _module():
    spec = importlib.util.spec_from_file_location("repetition_carte_bbis_v1", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _extrait_rep(nom: str) -> str:
    t = AMORCE_REP.read_text(encoding="utf-8")
    m = re.findall(rf"^# >>> {re.escape(nom)}\b[^\n]*\n(.*?)^# <<< {re.escape(nom)}$", t, re.S | re.M)
    assert len(m) == 1, nom
    return m[0]


@pytest.fixture
def torch_restaure():
    """`regler_determinisme` règle torch pour tout le processus : réglages remis après l'essai."""
    import torch
    fils, det = torch.get_num_threads(), torch.are_deterministic_algorithms_enabled()
    yield
    torch.set_num_threads(fils)
    torch.use_deterministic_algorithms(det)


def _sans_cle_aire(doc) -> bool:
    if isinstance(doc, dict):
        return all(not str(k).startswith("aire") and _sans_cle_aire(v) for k, v in doc.items())
    if isinstance(doc, list):
        return all(_sans_cle_aire(v) for v in doc)
    return True


# ------------------------------------------------------------------------------------------------------------ partie carte

def test_carte_sur_processeur_cas_sain_et_artefacts(tmp_path, monkeypatch, torch_restaure):
    import torch
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    m = _module()
    petit = dict(appareil="cpu", n_actions=24, largeur=32, par_famille=2)
    assert m.jouer_carte(tmp_path / "sain.json", **petit) == 0
    d = json.loads((tmp_path / "sain.json").read_text(encoding="utf-8"))
    assert d["etat"] == "reussie" and d["deterministe"] == {"lineaire": True, "attention": True}
    assert [a["famille"] for a in d["apprentissages"]] == ["lineaire", "attention", "lineaire", "attention"]   # entrelacés
    assert all(c["ecart_relatif_max"] <= 1e-4 and c["tolerance"] == 1e-4 for c in d["controle_carte_processeur"].values())
    g = d["garde_de_debit"]
    assert g["apprentissages_course"] == 2460 and g["apprentissages_r1"] == 1240 and g["limite_h"] == 11.0
    assert d["determinisme"]["deterministe"] and d["determinisme"]["fils"] == 1 and _sans_cle_aire(d)
    assert m.jouer_carte(tmp_path / "sain.json", **petit) == 2                       # sortie présente : R12
    # le seuil du texte n'est jamais relâché ; un seuil plus strict que l'écart réel arrête (code 9, motif écrit)
    assert m.jouer_carte(tmp_path / "relache.json", **petit, tolerance=1e-3) == 2
    assert m.jouer_carte(tmp_path / "strict.json", **petit, tolerance=1e-30) == 9
    assert "contrôle carte-processeur" in json.loads((tmp_path / "strict.json").read_text(encoding="utf-8"))["motif"]
    # erreur de torch pendant l'apprentissage : arrêt écrit, code fermé 8, jamais une chute
    vrai = ac.entrainer

    def panne(*a, **k):
        raise RuntimeError("CUDA error: an illegal memory access was encountered (simulée)")
    monkeypatch.setattr(ac, "entrainer", panne)
    assert m.jouer_carte(tmp_path / "panne.json", **petit) == 8
    p = json.loads((tmp_path / "panne.json").read_text(encoding="utf-8"))
    assert p["etat"] == "apprentissage" and "CUDA error" in p["motif"] and "RuntimeError" in p["pile"]
    # apprentissage non déterministe (second apprentissage du même réglage perturbé) : code 9
    vus = set()

    def instable(lot, famille, nom, *a, **k):
        s = vrai(lot, famille, nom, *a, **k)
        if nom in vus:
            s.w[0] += 1e-12
        vus.add(nom)
        return s
    monkeypatch.setattr(ac, "entrainer", instable)
    assert m.jouer_carte(tmp_path / "instable.json", **petit) == 9
    assert "non déterministe" in json.loads((tmp_path / "instable.json").read_text(encoding="utf-8"))["motif"]
    monkeypatch.setattr(ac, "entrainer", vrai)
    if not torch.cuda.is_available():                                               # carte demandée, absente : garde
        assert m.jouer_carte(tmp_path / "sans-carte.json", appareil="cuda", n_actions=24, largeur=32) == 2


# ------------------------------------------------------------------------------------------------------------ amorce

def _amorce(env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(["bash", str(AMORCE_REP)], capture_output=True, text=True, env={**os.environ, **env})


def test_amorce_de_repetition_essai_local_sans_ecriture_et_arguments(tmp_path):
    base = {"AMORCE_ESSAI_LOCAL": "1", "COMMIT": "c" * 40, "BRANCHE_CODE": "prep/t07bbis-code-v1", "ECHEANCE_UTC_S": "1795000000",
            "GO_ID": "GO-2026-11-14-09", "SCRIPT_SHA256": "a" * 64, "RACINE_AMORCE": str(tmp_path / "r")}
    r = _amorce(base)
    assert r.returncode == 0 and "aucun dossier" in r.stdout and not (tmp_path / "r").exists()
    for faute in ({"GO_ID": "GO-2026-11-02-28"}, {"COMMIT": "xyz"}, {"SCRIPT_SHA256": "a" * 63}, {"SCRIPT_SHA256": ""},
                  {"ECHEANCE_UTC_S": "demain"}, {"ACTIONS_REPETITION": "beaucoup"}):
        r = _amorce({**base, **faute})
        assert r.returncode == 2 and "REFUS" in r.stdout, faute
    r = _amorce({k: v for k, v in base.items() if k != "AMORCE_ESSAI_LOCAL"})
    assert r.returncode == 2 and "RACINE_AMORCE en essai local seulement" in r.stdout
    texte = AMORCE_REP.read_text(encoding="utf-8")
    assert "fetch" not in texte and "BRANCHE_7B" not in texte and "RUN_7B" not in texte   # aucune entrée de 7b
    assert texte.index("minuterie < /dev/null &") < texte.index("clone -q")             # minuterie avant toute passe


def test_motifs_de_la_course_et_aucune_entree_de_7b(tmp_path):
    corps = _extrait_rep("motifs-de-la-course")
    course = (RACINE / "scripts" / "amorce_bbis_v1.sh").read_text(encoding="utf-8")
    r = ad.jouer(corps + 'motifs_de_la_course "$(cat "$1")"\n', RACINE / "scripts" / "amorce_bbis_v1.sh")
    assert r.returncode == 0 and r.stdout.rstrip("\n").split("\n") == ad.motifs()   # les motifs mêmes de la course
    for nom, texte in (("deux", course + "\nMOTIFS='/x'\n"), ("aucun", course.replace("MOTIFS='", "AUTRES='"))):
        f = tmp_path / f"amorce-{nom}.sh"
        f.write_text(texte, encoding="utf-8")
        assert ad.jouer(corps + 'motifs_de_la_course "$(cat "$1")"\n', f).returncode == 1, nom
    # extraction réelle sur un dépôt jetable : rien sous runs/, diag/, donnees/ ; le script de la répétition reste hors de l'arbre
    d = ad.depot_vide(tmp_path / "depot")
    for p in ("src/controle_ia/x.py", "scripts/amorce_bbis_v1.sh", "scripts/repetition_carte_bbis_v1.py", "runs/r/manifeste.json",
              "diag/r/episodes-t06.json", "donnees/r/mesures-t06.npz", "essai/x.json", "registres/t07-etape-b-bis-v1.md"):
        ad.ecrire(d, p)
    ad.committer(d, "arbre jouet")
    ad.appliquer_motifs(d, ad.motifs())
    assert ad.jouer(corps + 'jamais_7b "$1"\n', d).returncode == 0
    assert not (d / "scripts" / "repetition_carte_bbis_v1.py").exists() and (d / "scripts" / "amorce_bbis_v1.sh").is_file()
    assert ad.git(d, "show", "HEAD:scripts/repetition_carte_bbis_v1.py") == "x"
    for p in ("runs", "diag", "donnees", "essai"):                                 # artefact : une entrée présente → arrêt
        e = tmp_path / f"avec-{p}"
        (e / p).mkdir(parents=True)
        assert ad.jouer(corps + 'jamais_7b "$1"\n', e).returncode == 1, p


FAUX_PYTHON = r"""#!/usr/bin/env bash
# faux python du venv : `-m pip install -v -r F` réussit, dure, ou échoue selon FAUX_PIP
[ "$1 $2 $3" = "-m pip install" ] || exit 3
echo "Collecting torch (verbeux)"
case "${FAUX_PIP:-ok}" in ok) echo "Successfully installed"; exit 0;; lent) sleep 5; exit 0;; *) echo "ERROR: no matching distribution"; exit 1;; esac
"""


def test_installation_bornee_par_timeout_et_code_dedie(tmp_path):
    py = tmp_path / "python"
    py.write_text(FAUX_PYTHON, encoding="utf-8")
    py.chmod(0o755)
    corps = ('DELAI_PIP_S="$2"\n' + _extrait_rep("installation")
             + 'installer "$1" exigences.txt "$3"; c=$?; echo "CODE $c DUREE $DUREE_PIP"\n')
    for faux, delai, code in (("ok", 60, 0), ("lent", 1, 5), ("echec", 60, 6)):
        journal = tmp_path / f"pip-{faux}.txt"
        r = subprocess.run(["bash", "-c", "set -uo pipefail\n" + corps, "essai", str(py), str(delai), str(journal)],
                           capture_output=True, text=True, env={**os.environ, "FAUX_PIP": faux})
        assert f"CODE {code} DUREE" in r.stdout, (faux, r.stdout, r.stderr)
        assert "Collecting torch (verbeux)" in journal.read_text(encoding="utf-8")
    texte = AMORCE_REP.read_text(encoding="utf-8")
    assert re.search(r"^DELAI_PIP_S=3600$", texte, re.M) and "pip install -v -r" in texte
    assert 'arret "installation au-delà de $DELAI_PIP_S s (pip-verbeux.txt)" 5' in texte


def test_lecture_de_la_course_compte_minimum_et_resume_de_la_carte(tmp_path, torch_restaure):
    corps = _extrait_rep("lecture-de-la-course")
    course = (RACINE / "scripts" / "amorce_bbis_v1.sh").read_text(encoding="utf-8")
    m = re.findall(r"^MIN_ESSAIS=(\d+)$", course, re.M)
    r = ad.jouer(corps + 'lire_course "$(cat "$1")" || exit 9\necho "MIN $MIN_COURSE"\ncompte_passes "$2"\n',
                 RACINE / "scripts" / "amorce_bbis_v1.sh", "86 passed, 22 skipped, 4 warnings in 60.77s")
    assert r.returncode == 0 and r.stdout.split() == ["MIN", m[0], "86"], r.stdout + r.stderr   # texte même de la course
    for nom, texte in (("deux-min", course + "\nMIN_ESSAIS=10\n"),
                       ("sans-compte", course.replace("# >>> compte-des-essais", "# >>> autre"))):
        f = tmp_path / f"{nom}.sh"
        f.write_text(texte, encoding="utf-8")
        assert ad.jouer(corps + 'lire_course "$(cat "$1")" || exit 9\n', f).returncode == 9, nom
    sortie = tmp_path / "carte.json"
    assert _module().jouer_carte(sortie, appareil="cpu", n_actions=16, largeur=16, par_famille=1) == 0
    r = ad.jouer(corps + 'resume_carte "$1" "$2"\n', os.sys.executable, sortie)
    assert r.returncode == 0 and r.stdout.startswith("état reussie ; jetons") and "écarts carte-processeur" in r.stdout
    assert not re.search(r"\baire", r.stdout) and _sans_cle_aire(json.loads(sortie.read_text(encoding="utf-8")))


def test_traces_de_la_repetition_poussees_sur_commit(tmp_path):
    corps = ('D="$1"; X="$2"; T="$3"; COMMIT="$4"; SORTIE_LIBRE="$5"\n'
             'XT=traces/bbis-t07-repetition-v1; BR_SORTIE=calcul/t07bbis-repetition-v2; SEUIL=94000000\n'
             'fin_instance() { echo "FIN $1"; exit "$1"; }\nsleep() { :; }\n'
             + _extrait_rep("fins") + 'arret "essais : 80 passés < MIN_ESSAIS 87 de la course" 7\n')

    def preparer(base: Path):
        d = ad.depot_vide(base / "depot")
        ad.ecrire(d, "src/controle_ia/x.py")
        commit = ad.committer(d, "code")
        distant = base / "distant.git"
        ad.git(base, "init", "-q", "--bare", str(distant))
        ad.git(d, "remote", "add", "origin", str(distant))
        ad.git(d, "push", "-q", "origin", "main")
        x = base / "x"
        x.mkdir()
        (x / "journal-repetition.txt").write_text("BBIS REPETITION ARRET : essais\n", encoding="utf-8")
        return d, commit, distant, x

    d, commit, distant, x = preparer(tmp_path / "sain")
    r = ad.jouer(corps, d, x, tmp_path / "sain", commit, 1, cwd=d)
    assert r.returncode == 7 and "traces poussées" in r.stdout and "fin, code 7" in r.stdout, r.stdout + r.stderr
    tete = ad.git(distant, "rev-parse", "refs/heads/calcul/t07bbis-repetition-v2")
    assert ad.git(distant, "rev-parse", f"{tete}^") == commit
    assert ad.git(distant, "ls-tree", "-r", "--name-only", tete).splitlines() == [
        "src/controle_ia/x.py", "traces/bbis-t07-repetition-v1/journal-repetition.txt"]
    d, commit, distant, x = preparer(tmp_path / "avant")                           # artefact : avant le contrôle de la branche
    r = ad.jouer(corps, d, x, tmp_path / "avant", commit, 0, cwd=d)
    assert r.returncode == 7 and "traces poussées" not in r.stdout
    assert subprocess.run(["git", "-C", str(distant), "rev-parse", "--verify", "-q", "refs/heads/calcul/t07bbis-repetition-v2"],
                          capture_output=True).returncode != 0


def test_minuterie_de_la_repetition_meme_texte_que_la_course(tmp_path):
    rep, course = _extrait_rep("minuterie"), ad.extrait("minuterie")
    corps_de = lambda t: t[t.index("minuterie() {"):]
    assert corps_de(rep) == corps_de(course)                                       # corps identique à celui de la course
    appels = tmp_path / "appels.txt"
    corps = (f'APPELS="{appels}"; API=https://console.vast.ai/api/v0; CONTAINER_ID=123456; ECHEANCE_UTC_S=1\n'
             'curl() { printf "%s\\n" "$*" >> "$APPELS"; echo 200; }\n'
             'k=0; sleep() { k=$((k + 1)); [ "$k" -ge 6 ] && exit 0; }\n' + rep + "minuterie\n")
    r = ad.jouer(corps)
    lignes = appels.read_text(encoding="utf-8").splitlines()
    assert r.returncode == 0 and sum("-X DELETE" in l for l in lignes) == 6 and sum("-X PUT" in l for l in lignes) == 1


# ------------------------------------------------------------------------------------------------------------ lanceur

def _lancer_rep(*args, env=None) -> subprocess.CompletedProcess:
    e = {**os.environ, "PYTHON_BBIS": str(Path(os.sys.executable))}
    e.update(env or {})
    return subprocess.run(["bash", str(LANCER_REP), *map(str, args)], capture_output=True, text=True, env=e)


def _offre(chemin: Path, **k) -> Path:
    o = {"id": 99, "carte": "A100 SXM4 80GB", "coeurs": 32, "memoire_vive_mo": 256000, "disque_go": 80, "stockage_usd_h": 0.05,
         "etiquette": "bbis-t07-repetition-v1", "prix_usd_h": 1.3,
         "cuda_max_good": 13.0}
    o.update(k)
    chemin.write_text(json.dumps(o), encoding="utf-8")
    return chemin


def _depot_commande(base: Path, amorce_rep: str | None = None, avec_script: bool = True) -> tuple[Path, str]:
    d = ad.depot_vide(base)
    ad.ecrire(d, "scripts/amorce_bbis_v1.sh", (RACINE / "scripts" / "amorce_bbis_v1.sh").read_text(encoding="utf-8"))
    ad.ecrire(d, "scripts/amorce_repetition_bbis_v1.sh", amorce_rep or AMORCE_REP.read_text(encoding="utf-8"))
    if avec_script:
        ad.ecrire(d, "scripts/repetition_carte_bbis_v1.py", SCRIPT.read_text(encoding="utf-8"))
    c = ad.committer(d, "code et répétition")
    ad.distant_officiel(d, base.with_name(base.name + "-distant"))       # branche de sortie absente du distant jetable
    return d, c


# ------------------------------------------------------------------------------------------------------------ gardes de l'amorce
# (contre-lecture de conformité M-1 : chaque garde shell jouée par son bloc marqué, avec de faux outils ; cas sain et artefact)

TETE = ('set -uo pipefail\nj() { echo "J $*"; }\nsleep() { echo "SLEEP $*"; }\n'
        'fin_instance() { echo "FIN $1"; exit "$1"; }\narret() { echo "ARRET : $1"; exit "${2:-4}"; }\n')


def _faux(base: Path, nom: str, corps: str) -> Path:
    b = base / "bin"
    b.mkdir(parents=True, exist_ok=True)
    (b / nom).write_text("#!/usr/bin/env bash\n" + corps, encoding="utf-8")
    (b / nom).chmod(0o755)
    return b


def _bash(script: str, *args, env=None, cwd=None) -> subprocess.CompletedProcess:
    return subprocess.run(["bash", "-c", script, "essai", *map(str, args)], capture_output=True, text=True,
                          env={**os.environ, **(env or {})}, cwd=cwd)


def test_refus_avant_la_minuterie_demande_la_destruction_de_l_instance(tmp_path):
    """Contre-lecture de sûreté M2 bis (i) : un refus avant la minuterie, en marche réelle, demande la destruction de l'instance
    par elle-même (trois DELETE jamais jugés, puis « stopped ») ; identifiant illisible : aucun appel, la mère détruit."""
    appels = tmp_path / "appels.txt"
    corps = (f'APPELS="{appels}"; API=https://console.vast.ai/api/v0; ESSAI="$1"; CONTAINER_ID="$2"\n'
             'curl() { printf "%s\\n" "$*" >> "$APPELS"; echo 200; }\nsleep() { :; }\n'
             + _extrait_rep("refus-avant-minuterie") + 'refus "échéance hors de [maintenant, + 3 h]"\n')
    r = _bash("set -uo pipefail\n" + corps, 0, 123456)
    lignes = appels.read_text(encoding="utf-8").splitlines()
    assert r.returncode == 2 and sum("-X DELETE" in l for l in lignes) == 3 and sum("-X PUT" in l for l in lignes) == 1
    assert "REFUS : échéance hors de" in r.stdout and "jamais jugé" in r.stdout
    for ident in ("", "12 3", "０１２", "0123", "inst"):                                # identifiant illisible : aucun appel
        appels.unlink()
        appels.touch()
        r = _bash("set -uo pipefail\n" + corps, 0, ident)
        assert r.returncode == 2 and appels.read_text() == "" and "la mère détruit" in r.stdout, ident
    r = _bash("set -uo pipefail\n" + corps, 1, 123456)                              # essai local : jamais d'appel
    assert r.returncode == 2 and appels.read_text() == ""


def test_fins_sans_stopped_et_piege_de_sortie(tmp_path):
    """Sûreté M2 bis (ii) et (iii) : la fin voulue ne demande pas « stopped » (l'instance reste en marche, minuterie armée) ;
    une sortie imprévue (`set -u`) passe par le piège : traces poussées si la branche est contrôlée, instance laissée en marche."""
    appels = tmp_path / "appels.txt"
    appels.touch()
    blocs = _extrait_rep("fins")
    corps_fin = blocs[blocs.index("fin_instance()"):blocs.index("arret()")]
    assert "curl" not in corps_fin and '"state"' not in corps_fin and "-X PUT" not in corps_fin
    tete = (f'APPELS="{appels}"; SORTIE_LIBRE="$1"; FIN_VOULUE=0\nj() {{ echo "J $*"; }}\n'
            'curl() { printf "%s\\n" "$*" >> "$APPELS"; echo 200; }\nsleep() { echo "SLEEP $*"; }\n')
    pousse = 'pousser_traces() { echo "POUSSEES ($1)"; }\n'
    r = _bash("set -uo pipefail\n" + tete + blocs + pousse + "trap 'fin_inattendue $?' EXIT\nfin_instance 0\n", 1)
    assert "fin, code 0 ; instance laissée en marche" in r.stdout and "SLEEP infinity" in r.stdout
    assert "SORTIE INATTENDUE" not in r.stdout and appels.read_text() == ""            # aucune demande « stopped »
    r = _bash("set -uo pipefail\n" + tete + blocs + pousse + "trap 'fin_inattendue $?' EXIT\necho \"$VARIABLE_ABSENTE\"\n", 1)
    assert "SORTIE INATTENDUE" in r.stdout and "POUSSEES (sortie inattendue" in r.stdout and "SLEEP infinity" in r.stdout
    r = _bash("set -uo pipefail\n" + tete + blocs + pousse + "trap 'fin_inattendue $?' EXIT\necho \"$VARIABLE_ABSENTE\"\n", 0)
    assert "SORTIE INATTENDUE" in r.stdout and "POUSSEES" not in r.stdout             # avant le contrôle de la branche
    r = _bash("set -uo pipefail\n" + tete + blocs + pousse + 'arret "essais en échec" 7\n', 1)
    assert "J ARRET : essais en échec" in r.stdout and "POUSSEES (arrêt, code 7)" in r.stdout
    texte = AMORCE_REP.read_text(encoding="utf-8")
    assert texte.index("trap 'fin_inattendue $?' EXIT") > texte.index("minuterie < /dev/null &")


def test_budget_de_travail_avant_la_reserve_de_fin():
    corps = TETE + 'ECHEANCE_UTC_S=$(( $(date +%s) + $1 )); RESERVE_FIN_S=900\n' + _extrait_rep("budget") + \
        'budget_ou_arret "la partie carte"; echo "BUDGET $BUDGET"\n'
    r = _bash(corps, 3600)
    assert r.returncode == 0 and 2600 < int(r.stdout.split("BUDGET ")[1]) <= 2700
    r = _bash(corps, 900 + 30)                                                       # échéance proche : arrêt 10
    assert r.returncode == 10 and "échéance proche : plus de temps pour la partie carte" in r.stdout
    texte = AMORCE_REP.read_text(encoding="utf-8")
    assert re.search(r"^RESERVE_FIN_S=900$", texte, re.M)
    for etape in ("l'installation", "les essais", "la partie carte"):
        assert f'budget_ou_arret "{etape}"' in texte


NVIDIA = '[ "$#" = 0 ] && { [ "${FAUX_ENTETE:-}" = echec ] && exit 9; echo "| NVIDIA-SMI 580.65.06   Driver Version: 580.65.06   CUDA Version: 13.0     |"; exit 0; }\n' + \
    'case "${FAUX_CARTE:-sxm}" in sxm) echo "NVIDIA A100-SXM4-80GB, 81920 MiB, 550.54";; pcie) echo "NVIDIA A100-PCIE-40GB, 40960 MiB, 550.54";; *) exit 9;; esac\n'


def test_machine_carte_jeton_outils_et_torch(tmp_path):
    b = _faux(tmp_path, "nvidia-smi", NVIDIA)
    _faux(tmp_path, "python-faux", 'exit "${FAUX_TORCH:-0}"\n')
    x = tmp_path / "x"
    x.mkdir()
    corps = TETE + f'X="{x}"; R="{tmp_path}"\n' + _extrait_rep("machine") + 'verifier_machine; verifier_torch "$1"; echo "MACHINE CONFORME"\n'
    env = {"PATH": f"{b}:{os.environ['PATH']}", "GH_TOKEN": "jeton-factice"}
    py = b / "python-faux"
    r = _bash(corps, py, env=env)
    assert r.returncode == 0 and "MACHINE CONFORME" in r.stdout and "A100-SXM4-80GB" in r.stdout, r.stdout + r.stderr
    assert "CUDA Version: 13.0" in (x / "nvidia-smi-entete.txt").read_text(encoding="utf-8")      # en-tête gardé pour la garde CUDA
    for faute, motif in (({"FAUX_CARTE": "pcie"}, "carte autre qu'une A100 SXM4 80 Go"), ({"FAUX_CARTE": "aucune"}, "carte invisible"),
                         ({"GH_TOKEN": ""}, "GH_TOKEN absent"), ({"FAUX_TORCH": "1"}, "torch ne voit pas la carte"),
                         ({"FAUX_ENTETE": "echec"}, "carte invisible (nvidia-smi, en-tête)")):
        r = _bash(corps, py, env={**env, **faute})
        assert r.returncode == 2 and motif in r.stdout, (faute, r.stdout)
    seul = tmp_path / "seul"                                                         # outil absent : `timeout` retiré du chemin
    seul.mkdir()
    for o in ("git", "curl", "python3", "sha256sum", "awk", "sed", "grep", "stat", "date", "tee", "head", "df"):
        p = subprocess.run(["bash", "-c", f"command -v {o}"], capture_output=True, text=True).stdout.strip()
        (seul / o).symlink_to(p)
    r = subprocess.run(["/bin/bash", "-c", corps, "essai", str(py)], capture_output=True, text=True,
                       env={"PATH": f"{b}:{seul}", "GH_TOKEN": "jeton-factice"})
    assert r.returncode == 2 and "outil absent : timeout" in r.stdout, r.stdout + r.stderr


def _distant(base: Path, motifs_avec_runs: bool = False, branche_sortie: bool = False) -> tuple[Path, str, str]:
    """Dépôt « distant » jetable : branche prep portant l'amorce de la course, le script de la répétition, du code, des essais et
    des entrées interdites hors des motifs."""
    d = ad.depot_vide(base)
    course = (RACINE / "scripts" / "amorce_bbis_v1.sh").read_text(encoding="utf-8")
    if motifs_avec_runs:
        course = course.replace("!/*/\n", "!/*/\n/runs/\n", 1)
    ad.ecrire(d, "scripts/amorce_bbis_v1.sh", course)
    ad.ecrire(d, "scripts/repetition_carte_bbis_v1.py", "script de la répétition, jouet\n")
    for p in ("src/controle_ia/x.py", "tests/test_t07bbis_x.py", "runs/r/manifeste.json", "diag/r/episodes-t06.json",
              "donnees/r/mesures-t06.npz"):
        ad.ecrire(d, p)
    ad.git(d, "checkout", "-q", "-b", "prep")
    commit = ad.committer(d, "code")
    if branche_sortie:
        ad.git(d, "branch", "calcul/t07bbis-repetition-v2")
    import hashlib
    return d, commit, hashlib.sha256(b"script de la r\xc3\xa9p\xc3\xa9tition, jouet\n").hexdigest()


def _preparer(tmp_path: Path, distant: Path, commit: str, sha: str, extra: str = "") -> subprocess.CompletedProcess:
    t = tmp_path / "t"
    (t / "traces").mkdir(parents=True, exist_ok=True)
    corps = (TETE + f'T="{t}"; D="{t}/depot"; X="{t}/traces"; COMMIT="{commit}"; BRANCHE_CODE=prep; SCRIPT_SHA256="{sha}"\n'
             'BR_SORTIE=calcul/t07bbis-repetition-v2; GH_TOKEN=jeton-factice; SORTIE_LIBRE=0\n'
             + _extrait_rep("motifs-de-la-course") + _extrait_rep("depot") + extra
             + 'preparer_depot "$1"; echo "DEPOT PRET S=$S SORTIE_LIBRE=$SORTIE_LIBRE"; ls "$D"\n')
    return _bash(corps, distant)


def test_depot_branche_de_sortie_extraction_tete_et_empreinte(tmp_path):
    d, commit, sha = _distant(tmp_path / "distant")
    r = _preparer(tmp_path / "sain", d, commit, sha)
    assert r.returncode == 0 and "DEPOT PRET" in r.stdout and "SORTIE_LIBRE=1" in r.stdout, r.stdout + r.stderr
    assert "runs" not in r.stdout.split("DEPOT PRET")[1].split() and "src" in r.stdout.split("DEPOT PRET")[1].split()
    assert (tmp_path / "sain" / "t" / "repetition_carte_bbis_v1.py").read_text(encoding="utf-8").startswith("script de la")
    d2, c2, _ = _distant(tmp_path / "distant-branche", branche_sortie=True)          # branche de sortie déjà présente
    r = _preparer(tmp_path / "branche", d2, c2, sha)
    assert r.returncode == 2 and "présente sur le dépôt distant" in r.stdout
    r = _preparer(tmp_path / "injoignable", tmp_path / "nulle-part", commit, sha)
    assert r.returncode == 2 and "ARRET : clonage" in r.stdout
    r = _preparer(tmp_path / "empreinte", d, commit, "0" * 64)
    assert r.returncode == 2 and "empreinte ≠ SCRIPT_SHA256" in r.stdout
    r = _preparer(tmp_path / "commit", d, "e" * 40, sha)
    assert r.returncode == 2 and "amorce de la course illisible au commit" in r.stdout
    faux_git = ('git() { if [ "${3:-}" = rev-parse ] && [ "${4:-}" = HEAD ]; then echo ' + "f" * 40 + '; else command git "$@"; fi; }\n')
    r = _preparer(tmp_path / "tete", d, commit, sha, extra=faux_git)
    assert r.returncode == 2 and "tête ≠ COMMIT" in r.stdout
    d3, c3, _ = _distant(tmp_path / "distant-runs", motifs_avec_runs=True)          # une entrée de 7b extraite : arrêt
    r = _preparer(tmp_path / "runs", d3, c3, sha)
    assert r.returncode == 2 and "aucune entrée de 7b" in r.stdout
    r = _preparer(tmp_path / "sain", d, commit, sha)                                 # R12 : dossier déjà là
    assert r.returncode == 2 and "existe déjà" in r.stdout


def test_installation_des_paquets_codes_5_6_10():
    corps = (TETE + 'ECHEANCE_UTC_S=$(( $(date +%s) + $1 )); RESERVE_FIN_S=900; DELAI_PIP_S="$2"; T=/nonexistent; D=/nonexistent; '
             'X=/nonexistent\n' + _extrait_rep("budget") + _extrait_rep("installation")
             + 'installer() { DUREE_PIP=1; return "$3_CODE"; }\n'.replace('"$3_CODE"', '"$CODE_FAUX"')
             + 'CODE_FAUX="$3"; installer_paquets python; echo "SUITE DELAI $DELAI"\n')
    r = _bash(corps, 3600, 3600, 0)
    assert r.returncode == 0 and "SUITE DELAI" in r.stdout and int(r.stdout.split("SUITE DELAI ")[1]) < 3600   # borné par le budget
    assert _bash(corps, 3 * 3600, 3600, 5).returncode == 5                           # délai de pip (60 min) atteint : 5
    r = _bash(corps, 3600, 3600, 5)                                                  # le budget a coupé : 10
    assert r.returncode == 10 and "échéance proche : installation interrompue" in r.stdout
    assert _bash(corps, 3600, 3600, 6).returncode == 6


FAUX_PY_ESSAIS = r"""if [ "$1" = -I ]; then exec "$PYTHON_VRAI" "$@"; fi
if [ "$1 $2" = "-m pytest" ]; then
    [ "${FAUX_ECRIT:-0}" = 1 ] && echo x > src/ecrit-par-les-essais.py
    echo "........"; echo "${FAUX_RES:-87 passed, 22 skipped in 60.0s}"; exit "${FAUX_CODE:-0}"
fi
if [ "$2" = carte ]; then
    while [ "$#" -gt 0 ]; do [ "$1" = --sortie ] && { shift; printf '{"etat": "%s", "jetons": 10}\n' "faux" > "$1"; }; shift; done
    echo "BBIS REPETITION FAUX"; exit "${FAUX_CODE:-0}"
fi
exit 3
"""


def test_essais_de_la_course_et_partie_carte_codes_2_4_7_8_9_10(tmp_path):
    b = _faux(tmp_path, "python-faux", FAUX_PY_ESSAIS)
    d = ad.depot_vide(tmp_path / "depot")
    ad.ecrire(d, "src/controle_ia/x.py")
    ad.ecrire(d, "tests/test_t07bbis_x.py")
    ad.committer(d, "arbre")
    t, x = tmp_path / "t", tmp_path / "x"
    t.mkdir()
    x.mkdir()
    course = (RACINE / "scripts" / "amorce_bbis_v1.sh").read_text(encoding="utf-8")
    f_course = tmp_path / "course.sh"
    f_course.write_text(course, encoding="utf-8")
    corps = (TETE + f'T="{t}"; X="{x}"; D="{d}"; S=script.py; RESERVE_FIN_S=900; ECHEANCE_UTC_S=$(( $(date +%s) + $2 ))\n'
             'A_COURSE="$(cat "$3")"\n' + _extrait_rep("budget") + _extrait_rep("lecture-de-la-course")
             + _extrait_rep("essais-et-carte") + '"$4" "$1"; echo SUITE\n')
    py = b / "python-faux"
    env = {"PYTHON_VRAI": os.sys.executable}
    r = _bash(corps, py, 3600, f_course, "essais_de_la_course", env=env, cwd=d)
    assert r.returncode == 0 and "SUITE" in r.stdout and "minimum de la course : 87" in r.stdout, r.stdout + r.stderr
    for faute, code, motif in (({"FAUX_RES": "80 passed, 22 skipped in 60s"}, 7, "80 passés < MIN_ESSAIS 87"),
                               ({"FAUX_CODE": "1"}, 7, "essais en échec"), ({"FAUX_CODE": "124"}, 10, "essais interrompus"),
                               ({"FAUX_ECRIT": "1"}, 2, "ont écrit sous src ou tests")):
        r = _bash(corps, py, 3600, f_course, "essais_de_la_course", env={**env, **faute}, cwd=d)
        assert r.returncode == code and motif in r.stdout, (faute, r.stdout)
        (d / "src" / "ecrit-par-les-essais.py").unlink(missing_ok=True)
    r = _bash(corps, py, 900 + 30, f_course, "essais_de_la_course", env=env, cwd=d)
    assert r.returncode == 10 and "plus de temps pour les essais" in r.stdout
    for code_carte, code, motif in (("0", 0, "SUITE"), ("8", 8, "erreur d'apprentissage"), ("9", 9, "au-delà de 10⁻⁴"),
                                    ("2", 2, "carte : garde"), ("1", 4, "carte : code 1"), ("124", 10, "partie carte interrompue")):
        (x / "repetition-carte.json").unlink(missing_ok=True)
        r = _bash(corps, py, 3600, f_course, "partie_carte", env={**env, "FAUX_CODE": code_carte}, cwd=d)
        assert r.returncode == code and motif in r.stdout, (code_carte, r.stdout + r.stderr)
        assert "carte : état faux ; jetons 10" in r.stdout                             # résumé lu dans la sortie écrite


# ------------------------------------------------------------------------------------------------------------ lanceur

def _lancer_rep(*args, env=None) -> subprocess.CompletedProcess:
    e = {**os.environ, "PYTHON_BBIS": str(Path(os.sys.executable)), "GH_TOKEN": "jeton-factice"}
    e.update(env or {})
    return subprocess.run(["bash", str(LANCER_REP), *map(str, args)], capture_output=True, text=True, env=e)


def _offre(chemin: Path, **k) -> Path:
    o = {"id": 99, "carte": "A100 SXM4 80GB", "coeurs": 32, "memoire_vive_mo": 256000, "disque_go": 80, "stockage_usd_h": 0.05,
         "etiquette": "bbis-t07-repetition-v1", "prix_usd_h": 1.3,
         "cuda_max_good": 13.0}
    o.update(k)
    chemin.write_text(json.dumps(o), encoding="utf-8")
    return chemin


def _depot_commande(base: Path, amorce_rep: str | None = None, avec_script: bool = True) -> tuple[Path, str]:
    d = ad.depot_vide(base)
    ad.ecrire(d, "scripts/amorce_bbis_v1.sh", (RACINE / "scripts" / "amorce_bbis_v1.sh").read_text(encoding="utf-8"))
    ad.ecrire(d, "scripts/amorce_repetition_bbis_v1.sh", amorce_rep or AMORCE_REP.read_text(encoding="utf-8"))
    if avec_script:
        ad.ecrire(d, "scripts/repetition_carte_bbis_v1.py", SCRIPT.read_text(encoding="utf-8"))
    c = ad.committer(d, "code et répétition")
    ad.distant_officiel(d, base.with_name(base.name + "-distant"))       # branche de sortie absente du distant jetable
    return d, c


OFFRES = [{"id": 99, "gpu_name": "A100 SXM4", "num_gpus": 1, "gpu_ram": 81920, "cpu_cores_effective": 32, "cpu_ram": 257000,
           "disk_space": 120, "dph_total": 1.12, "storage_cost": 0.15, "cuda_max_good": 13.0},
          {"id": 98, "gpu_name": "A100 PCIE", "num_gpus": 1, "gpu_ram": 40960, "cpu_cores_effective": 32, "cpu_ram": 257000,
           "disk_space": 120, "dph_total": 0.80, "storage_cost": 0.15, "cuda_max_good": 13.0}]


def test_offre_construite_par_programme_depuis_la_recherche(tmp_path):
    rech = tmp_path / "recherche.json"
    rech.write_text(json.dumps(OFFRES), encoding="utf-8")
    r = _lancer_rep("offre-depuis-recherche", rech, "99", tmp_path / "offre.json")
    assert r.returncode == 0 and "OFFRE ECRITE" in r.stdout, r.stdout
    o = json.loads((tmp_path / "offre.json").read_text(encoding="utf-8"))
    assert o["carte"] == "A100 SXM4 80GB" and o["prix_usd_h"] == 1.12 and o["etiquette"] == "bbis-t07-repetition-v1"
    assert abs(o["stockage_usd_h"] - 0.15 * 60 / 730) < 1e-12
    assert _lancer_rep("offre", tmp_path / "offre.json", "99", "1.12").returncode == 0
    assert _lancer_rep("offre-depuis-recherche", rech, "99", tmp_path / "offre.json").returncode == 2   # R12
    for k, v, motif in (("gpu_name", "A100 PCIE", "A100 SXM4 80 Go exactement"), ("gpu_ram", 40960, "exactement"),
                        ("num_gpus", 2, "exactement"), ("dph_total", 1.41, "prix"), ("storage_cost", None, "clé(s)")):
        rech.write_text(json.dumps([{**OFFRES[0], k: v}]), encoding="utf-8")
        r = _lancer_rep("offre-depuis-recherche", rech, "99", tmp_path / f"o-{k}.json")
        assert r.returncode == 2 and motif in r.stdout and not (tmp_path / f"o-{k}.json").exists(), (k, r.stdout)
    rech.write_text(json.dumps(OFFRES), encoding="utf-8")
    assert _lancer_rep("offre-depuis-recherche", rech, "97", tmp_path / "o97.json").returncode == 2            # offre absente
    assert _lancer_rep("offre-depuis-recherche", rech, "099", tmp_path / "o099.json").returncode == 2          # forme refusée


def test_lanceur_offre_commande_et_depense(tmp_path):
    import hashlib
    assert subprocess.run(["bash", "-n", str(LANCER_REP)]).returncode == 0
    assert subprocess.run(["bash", "-n", str(AMORCE_REP)]).returncode == 0
    f = _offre(tmp_path / "offre.json")
    assert _lancer_rep("offre", f, "99", "1.3").returncode == 0
    for faute, motif in (({"id": 98}, "identifiant"), ({"carte": "A100 PCIE 40GB"}, "exactement"), ({"carte": "H200 SXM 141GB"}, "exactement"),
                         ({"etiquette": "bbis-t07-v1"}, "étiquette"), ({"prix_usd_h": 1.5}, "prix"), ({"disque_go": 40}, "disque_go"),
                         ({"coeurs": 8}, "coeurs"), ({"memoire_vive_mo": 64000}, "memoire_vive_mo"), ({"stockage_usd_h": 0.2}, "stockage")):
        r = _lancer_rep("offre", _offre(tmp_path / "faute.json", **faute), "99", str(faute.get("prix_usd_h", 1.3)))
        assert r.returncode == 2 and motif in r.stdout, faute
    d, commit = _depot_commande(tmp_path / "depot")
    tmp = tmp_path / "tmp"
    tmp.mkdir()
    image = "pytorch/pytorch:2.4.1-cuda12.1-cudnn9-runtime"
    feu = f"feu de la mère : GO-2026-11-14-09, R-2802, image {image}"
    args = lambda commit_, ech, feu_=feu, image_=image: ("commande", d, f, "99", commit_, "prep/t07bbis-code-v1", ech, "1.3", feu_, image_)
    r = _lancer_rep(*args(commit, int(time.time()) + 3600), env={"TMPDIR": str(tmp)})
    assert r.returncode == 0, r.stdout
    sha = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
    ligne = r.stdout.splitlines()[-1]
    assert ligne.startswith("GO_ID=GO-2026-11-14-09 vastai create instance 99 ") and "--label bbis-t07-repetition-v1" in ligne
    assert f"-e SCRIPT_SHA256={sha}" in ligne and "-e GH_TOKEN=$GH_TOKEN" in ligne and "--disk 60" in ligne
    assert "HF_TOKEN" not in ligne and "jeton-factice" not in r.stdout and list(tmp.iterdir()) == []
    assert "strictement sous 3" in r.stdout and "budget de travail" in r.stdout
    for a, motif, env in ((args(commit, int(time.time()) + 3600, "feu GO-2026-11-14-09 " + image), "R-2802", {}),
                          (args(commit, int(time.time()) + 3600, "feu R-2802 " + image), "GO-2026-11-14-09", {}),
                          (args(commit, int(time.time()) + 3600, "feu GO-2026-11-14-09 R-2802"), "ne nomme pas l'image", {}),
                          (args(commit, int(time.time()) + 2 * 3600), "strictement moins de 1.75 h", {}),
                          (args("e" * 40, int(time.time()) + 3600), "absent de", {}),
                          (args(commit, int(time.time()) + 3600), "GH_TOKEN absent", {"GH_TOKEN": ""})):
        r = _lancer_rep(*a, env={"TMPDIR": str(tmp), **env})
        assert r.returncode == 2 and motif in r.stdout, (motif, r.stdout)
    r = _lancer_rep("commande", d, f, "099", commit, "prep/t07bbis-code-v1", int(time.time()) + 3600, "1.3", feu, image)
    assert r.returncode == 2 and "identifiant d'offre illisible" in r.stdout
    d2, c2 = _depot_commande(tmp_path / "autre-amorce", amorce_rep=AMORCE_REP.read_text(encoding="utf-8") + "# autre\n")
    r = _lancer_rep("commande", d2, f, "99", c2, "prep/t07bbis-code-v1", int(time.time()) + 3600, "1.3", feu, image)
    assert r.returncode == 2 and "amorce de répétition du commit" in r.stdout
    d3, c3 = _depot_commande(tmp_path / "sans-script", avec_script=False)
    r = _lancer_rep("commande", d3, f, "99", c3, "prep/t07bbis-code-v1", int(time.time()) + 3600, "1.3", feu, image)
    assert r.returncode == 2 and "script de la répétition absent" in r.stdout
    assert _lancer_rep("depense", "2.0", "1.3").returncode == 0                     # 2,0 + 0,325 < 3
    r = _lancer_rep("depense", "2.7", "1.3")                                        # 2,7 + 0,325 ≥ 3 : arrêt et destruction
    assert r.returncode == 2 and "coupure 3 USD" in r.stdout and "detruire CREATION.json" in r.stdout


def test_plafond_strictement_sous_3_usd_et_prix_hors_bornes():
    m = _module()
    maintenant = 1_800_000_000
    for prix in (1.09, 1.3, 1.4):
        egal = maintenant + int(round(m.duree_max_h(prix) * 3600))
        with pytest.raises(m.Refus, match="strictement"):
            m.garde_commande(egal + 1, prix, "GO-2026-11-14-09 R-2802", maintenant)
        r = m.garde_commande(egal - 60, prix, "GO-2026-11-14-09 R-2802", maintenant)
        assert r["cout_max_usd"] < 3.0
    for prix in (0.0, -1.0, 1.41):
        with pytest.raises(m.Refus, match="prix"):
            m.garde_commande(maintenant + 600, prix, "GO-2026-11-14-09 R-2802", maintenant)


FAUX_VASTAI = r"""#!/usr/bin/env bash
etat="$FAUX_ETAT"
case "$1 $2" in
    "destroy instance") id="$3"; shift 3; oui=0; for a in "$@"; do [ "$a" = -y ] && oui=1; done
        if [ "$oui" = 0 ]; then printf '[y/N]: '; read -r rep || rep=""; [ "$rep" = y ] || { echo "Aborted."; exit 0; }; fi
        python3 -c 'import json, sys
p = sys.argv[1]; l = json.load(open(p)); json.dump([i for i in l if str(i["id"]) != sys.argv[2]], open(p, "w"))' "$etat" "$id"
        echo "destroying instance $id."; exit 0;;
    "show instances") [ -n "${FAUX_MODE:-}" ] && stat -L -c %a /proc/self/fd/1 > "$FAUX_MODE"
        case "${FAUX_LISTE:-}" in illisible) echo "pas du json"; exit 0;; echec) exit 1;; esac
        cat "$etat"; exit 0;;
    "show user") [ -n "${FAUX_MODE:-}" ] && stat -L -c %a /proc/self/fd/1 > "$FAUX_MODE"; cat "$FAUX_UTILISATEUR"; exit 0;;
esac
exit 1
"""


def _outil(base: Path, instances: list, utilisateur: dict | None = None) -> dict:
    b = base / "bin"
    b.mkdir(parents=True)
    (b / "vastai").write_text(FAUX_VASTAI, encoding="utf-8")
    (b / "vastai").chmod(0o755)
    (base / "etat.json").write_text(json.dumps(instances), encoding="utf-8")
    (base / "utilisateur.json").write_text(json.dumps(utilisateur or {}), encoding="utf-8")
    tmp = base / "tmp"
    tmp.mkdir()
    return {"PATH": f"{b}:{os.environ['PATH']}", "FAUX_ETAT": str(base / "etat.json"), "TMPDIR": str(tmp),
            "FAUX_UTILISATEUR": str(base / "utilisateur.json"), "FAUX_MODE": str(base / "mode.txt")}


REP = {"label": "bbis-t07-repetition-v1", "gpu_name": "A100 SXM4", "gpu_ram": 81920, "dph_total": 1.12}


def _creation(base: Path, valeur) -> Path:
    p = base / f"creation-{abs(hash(repr(valeur)))}.json"
    p.write_text(json.dumps({"success": True, "new_contract": valeur}), encoding="utf-8")
    return p


def test_la_repetition_lit_la_liste_de_la_course():
    """R-2795 : une seule liste des instances d'autres sessions, celle de la course, lue telle quelle, plus la liste propre de la
    répétition (60671759, contre-lecture de sûreté M1)."""
    from controle_ia.t07bbis import registre_bbis_v1 as rb
    m = _module()
    assert m.INSTANCES_D_AUTRES_SESSIONS is rb.INSTANCES_D_AUTRES_SESSIONS and tuple(AUTRES) == rb.INSTANCES_D_AUTRES_SESSIONS
    assert not re.search(r"^INSTANCES_D_AUTRES_SESSIONS\s*=", SCRIPT.read_text(encoding="utf-8"), re.M)   # aucune copie
    assert m.PROTEGEES == {int(p) for p in AUTRES} | {60671759} and "60671759" not in rb.INSTANCES_D_AUTRES_SESSIONS
    for p in AUTRES + ("60671759",):
        with pytest.raises(m.Refus, match="autre session"):
            m.exiger_identifiant(p)
    assert m.exiger_absence([{"id": 60670453}], "424242", "60670453")["temoin"] == 60670453


def test_identifiants_en_entiers_ascii_seulement():
    m = _module()
    assert m.entier_ascii("424242") == 424242 and m.entier_ascii(424242) == 424242
    for faux in ("060670453", "０６０６７０４５３", "6067０453", " 424242", "424242 ", "42 42", "", "-1", "1e5", True, 0, -3, 1.5, None):
        with pytest.raises(m.Refus):
            m.entier_ascii(faux)
    with pytest.raises(m.Refus, match="illisible"):                                  # la forme ne contourne plus la garde
        m.exiger_identifiant("060670453")
    with pytest.raises(m.Refus, match="illisible"):                                  # ni la preuve d'absence
        m.exiger_absence([{"id": "060670453"}, {"id": 60480302}], "424242", "60480302")


def test_destruction_garde_positive_par_new_contract_et_etiquette(tmp_path):
    env = _outil(tmp_path / "sain", [{"id": 424242, **REP}, {"id": 60670453, "label": "autre"}, {"id": 60671759, "label": "neuron"}])
    c = _creation(tmp_path, 424242)
    r = _lancer_rep("detruire", c, env=env)
    lignes = r.stdout.splitlines()
    assert r.returncode == 0 and lignes[-2] == "GO_ID=GO-2026-11-14-09 vastai destroy instance 424242 -y", r.stdout
    assert (tmp_path / "sain" / "mode.txt").read_text().strip() == "600"            # liste écrite sous umask 077
    assert list((tmp_path / "sain" / "tmp").iterdir()) == []                        # puis supprimée
    d = subprocess.run(["bash", "-c", lignes[-2]], capture_output=True, text=True, stdin=subprocess.DEVNULL, env={**os.environ, **env})
    assert d.returncode == 0 and "destroying instance 424242" in d.stdout
    v = _lancer_rep("verifier-destruction", c, "60670453", env=env)
    assert v.returncode == 0 and "DESTRUCTION PROUVEE 424242" in v.stdout and list((tmp_path / "sain" / "tmp").iterdir()) == []
    # artefacts : étiquette autre, instance absente de la liste, identifiants de forme fautive ou protégés, new_contract absent
    env = _outil(tmp_path / "etiquette", [{"id": 424242, **REP, "label": "neuron-lens"}, {"id": 60670453}])
    r = _lancer_rep("detruire", _creation(tmp_path, 424242), env=env)
    assert r.returncode == 2 and "jamais détruite par la répétition" in r.stdout and "vastai destroy" not in r.stdout
    r = _lancer_rep("detruire", _creation(tmp_path, 515151), env=env)
    assert r.returncode == 2 and "absente de la liste" in r.stdout and "vastai destroy" not in r.stdout
    for valeur in ("060670453", "０６０６７０４５３", " 424242", 60670453, "60671759", 60480302, True):
        r = _lancer_rep("detruire", _creation(tmp_path, valeur), env=env)
        assert r.returncode == 2 and "vastai destroy" not in r.stdout, valeur
    sans = tmp_path / "sans.json"
    sans.write_text(json.dumps({"success": True}), encoding="utf-8")
    r = _lancer_rep("detruire", sans, env=env)
    assert r.returncode == 2 and "ne pas deviner" in r.stdout


def test_verification_de_l_absence_temoins_et_cas_du_jour(tmp_path):
    c = _creation(tmp_path, 424242)
    env = _outil(tmp_path / "sans-y", [{"id": 424242, **REP}, {"id": 60480302}])     # le cas du 2026-11-14 : « Aborted. », code 0
    d = subprocess.run(["bash", "-c", "GO_ID=GO-2026-11-14-09 vastai destroy instance 424242"], capture_output=True, text=True,
                       stdin=subprocess.DEVNULL, env={**os.environ, **env})
    assert d.returncode == 0 and "Aborted." in d.stdout
    v = _lancer_rep("verifier-destruction", c, "60480302", env=env)
    assert v.returncode == 2 and "toujours dans la liste" in v.stdout
    env = _outil(tmp_path / "temoins", [{"id": 60480302}, {"id": 60671759}])
    assert _lancer_rep("verifier-destruction", c, "60480302", env=env).returncode == 0
    for temoin, motif in (("60671759", "hors de"), ("999", "hors de"), ("60670453", "témoin 60670453 absent")):
        v = _lancer_rep("verifier-destruction", c, temoin, env=env)
        assert v.returncode == 2 and motif in v.stdout, temoin
    for faute, motif in (("illisible", "illisible"), ("echec", "lecture de la liste des instances en échec")):
        v = _lancer_rep("verifier-destruction", c, "60480302", env={**env, "FAUX_LISTE": faute})
        assert v.returncode == 2 and "NON PROUVEE" in v.stdout.upper().replace("É", "E") and motif in v.stdout, faute
    jeton = "gh" + "p_" + "A" * 36                                                   # un jeton dans la liste : alerte, jamais affiché
    env = _outil(tmp_path / "jeton", [{"id": 60480302, "extra_env": [["GH_TOKEN", jeton]]}])
    v = _lancer_rep("verifier-destruction", c, "60480302", env=env)
    assert v.returncode == 0 and "révoquer le jeton" in v.stdout and jeton not in v.stdout + v.stderr


def test_relire_trouver_et_credit(tmp_path):
    c = _creation(tmp_path, 424242)
    env = _outil(tmp_path / "sain", [{"id": 424242, **REP}, {"id": 60480302}])
    r = _lancer_rep("relire", c, env=env)
    assert r.returncode == 0 and "INSTANCE CONFORME 424242" in r.stdout
    for k, v, motif in (("gpu_name", "A100 PCIE", "hors borne"), ("dph_total", 1.5, "hors borne"), ("gpu_ram", 40960, "hors borne"),
                        ("label", "autre", "jamais détruite par la répétition")):
        env = _outil(tmp_path / f"relire-{k}", [{"id": 424242, **REP, k: v}])
        r = _lancer_rep("relire", c, env=env)
        assert r.returncode == 2 and motif in r.stdout, k
    env = _outil(tmp_path / "trouver", [{"id": 424242, **REP}, {"id": 60480302, "label": "autre"}])
    r = _lancer_rep("trouver", tmp_path / "trouvee.json", env=env)
    assert r.returncode == 0 and json.loads((tmp_path / "trouvee.json").read_text())["new_contract"] == 424242
    env = _outil(tmp_path / "trouver-deux", [{"id": 424242, **REP}, {"id": 424243, **REP}])
    assert _lancer_rep("trouver", tmp_path / "trouvee-2.json", env=env).returncode == 2
    env = _outil(tmp_path / "credit", [], {"credit": 12.5, "email": "personne@exemple.invalid", "api_key": "secret-factice"})
    r = _lancer_rep("credit", env=env)
    assert r.returncode == 0 and "CREDIT 12.50 USD" in r.stdout and "personne@" not in r.stdout and "secret" not in r.stdout
    assert (tmp_path / "credit" / "mode.txt").read_text().strip() == "600" and list((tmp_path / "credit" / "tmp").iterdir()) == []
    env = _outil(tmp_path / "credit-bas", [], {"credit": 2.0})
    assert _lancer_rep("credit", env=env).returncode == 2
    env = _outil(tmp_path / "credit-sans", [], {"email": "x"})
    assert _lancer_rep("credit", env=env).returncode == 2


def test_etat_partiel_ecrit_avant_les_controles_sur_processeur(tmp_path, monkeypatch, torch_restaure):
    """Contre-lecture M-4 : si le budget coupe la partie carte pendant les contrôles sur processeur, les durées sur la carte et la
    projection sont déjà écrites (état « partiel »)."""
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    m = _module()
    sortie, vus = tmp_path / "carte.json", []

    def coupe(*a, **k):
        vus.append(json.loads(sortie.read_text(encoding="utf-8")))
        raise RuntimeError("interrompu (simulé)")
    monkeypatch.setattr(ac, "controle_carte_processeur", coupe)
    assert m.jouer_carte(sortie, appareil="cpu", n_actions=16, largeur=16, par_famille=1) == 8
    assert vus and vus[0]["etat"].startswith("partiel") and vus[0]["garde_de_debit"]["apprentissages_course"] == 2460
    assert len(vus[0]["apprentissages"]) == 2 and _sans_cle_aire(vus[0])


# ------------------------------------------------------------------------------------------------------------ CUDA de l'hôte
# Répétition sur carte du 15 novembre (traces/bbis-t07-repetition-v1 sur calcul/t07bbis-repetition-v1, 56f5b8b8) : pilote
# 570.211.01, CUDA 12.8 ; roue torch 2.14.1 construite pour CUDA 13.0 ; « torch ne voit pas la carte » après 118 s d'installation.

TRACE_NVIDIA_SMI = "NVIDIA A100-SXM4-80GB, 81920 MiB, 570.211.01\n"          # nvidia-smi.txt des traces, tel quel
ENTETE_HOTE_DES_TRACES = ("+-----------------------------------------------------------------------------------------+\n"
                          "| NVIDIA-SMI 570.211.01            Driver Version: 570.211.01     CUDA Version: 12.8     |\n"
                          "|-----------------------------------------+------------------------+----------------------+\n")
ENTETE_SAIN = ("+-----------------------------------------------------------------------------------------+\n"
               "| NVIDIA-SMI 580.65.06              Driver Version: 580.65.06      CUDA Version: 13.0     |\n"
               "|-----------------------------------------+------------------------+----------------------+\n")


def test_offre_de_la_repetition_exige_cuda_13_de_l_hote(tmp_path):
    rech = tmp_path / "recherche.json"
    for nom, valeur, motif in (("vieux", 12.8, "cuda_max_good 12.8 < 13"), ("texte", "13.0", "absent ou illisible"),
                               ("nul", None, "absent ou illisible")):
        rech.write_text(json.dumps([{**OFFRES[0], "cuda_max_good": valeur}]), encoding="utf-8")
        r = _lancer_rep("offre-depuis-recherche", rech, "99", tmp_path / f"o-{nom}.json")
        assert r.returncode == 2 and motif in r.stdout and not (tmp_path / f"o-{nom}.json").exists(), (nom, r.stdout)
    rech.write_text(json.dumps([{k: v for k, v in OFFRES[0].items() if k != "cuda_max_good"}]), encoding="utf-8")
    r = _lancer_rep("offre-depuis-recherche", rech, "99", tmp_path / "o-sans.json")       # champ absent : refus
    assert r.returncode == 2 and "cuda_max_good" in r.stdout and not (tmp_path / "o-sans.json").exists()
    rech.write_text(json.dumps([{**OFFRES[0], "cuda_max_good": 13.0}]), encoding="utf-8")
    r = _lancer_rep("offre-depuis-recherche", rech, "99", tmp_path / "o-sain.json")       # cas sain : borne incluse
    assert r.returncode == 0 and "CUDA de l'hôte 13" in r.stdout, r.stdout
    o = json.loads((tmp_path / "o-sain.json").read_text(encoding="utf-8"))
    assert o["cuda_max_good"] == 13.0
    assert _lancer_rep("offre", tmp_path / "o-sain.json", "99", "1.12").returncode == 0
    for nom, faute in (("vieux", {"cuda_max_good": 12.8}), ("nan", {"cuda_max_good": float("nan")})):
        r = _lancer_rep("offre", _offre(tmp_path / f"f-{nom}.json", **faute), "99", "1.3")
        assert r.returncode == 2 and "cuda_max_good" in r.stdout, (nom, r.stdout)
    sans = tmp_path / "f-sans.json"
    sans.write_text(json.dumps({k: v for k, v in json.loads(_offre(tmp_path / "x.json").read_text()).items()
                                if k != "cuda_max_good"}), encoding="utf-8")
    r = _lancer_rep("offre", sans, "99", "1.3")
    assert r.returncode == 2 and "cuda_max_good" in r.stdout
    assert "cuda_max_good>=13.0" in LANCER_REP.read_text(encoding="utf-8")                # filtre de la recherche décrit


def test_cuda_du_pilote_avant_l_installation_dans_les_deux_amorces(tmp_path):
    """Contrôle de l'amorce (même texte dans les deux amorces) : en-tête sain (13.0) accepté ; en-tête de l'hôte des traces (12.8)
    refusé, code 2 comme « torch ne voit pas la carte » ; sortie des traces telle quelle (sans « CUDA Version ») refusée ; en-tête
    multiple, vide ou absent refusé. Le contrôle précède toute installation des paquets dans les deux amorces."""
    bloc = _extrait_rep("cuda-du-pilote")
    assert bloc == ad.extrait("cuda-du-pilote")                                         # même texte dans l'amorce de la course
    corps = TETE + bloc + 'exiger_cuda_du_pilote "$1"; echo "CUDA CONFORME"\n'
    cas = {"sain": ENTETE_SAIN, "sain-13.2": ENTETE_SAIN.replace("13.0", "13.2"), "sain-14.1": ENTETE_SAIN.replace("13.0", "14.1"),
           "sain-13.10": ENTETE_SAIN.replace("13.0", "13.10"), "sain-100.0": ENTETE_SAIN.replace("13.0", "100.0"),
           "vieux-9.2": ENTETE_SAIN.replace("13.0", "9.2"), "na": ENTETE_SAIN.replace("13.0    ", "N/A     "),
           "hote-des-traces": ENTETE_HOTE_DES_TRACES, "trace-telle-quelle": TRACE_NVIDIA_SMI,
           "double": ENTETE_SAIN + ENTETE_HOTE_DES_TRACES, "vide": "", "illisible": ENTETE_SAIN.replace("13.0", "13.x"),
           "majeur-seul": ENTETE_SAIN.replace("13.0", "13 ")}
    for nom, texte in cas.items():
        (tmp_path / nom).write_text(texte, encoding="utf-8")
    for nom in ("sain", "sain-13.2", "sain-14.1", "sain-13.10", "sain-100.0"):
        r = _bash(corps, tmp_path / nom)
        assert r.returncode == 0 and "CUDA CONFORME" in r.stdout and "CUDA servie par le pilote" in r.stdout, (nom, r.stdout + r.stderr)
    r = _bash(corps, tmp_path / "hote-des-traces")
    assert r.returncode == 2 and "pilote trop ancien : CUDA 12.8" in r.stdout and "CUDA CONFORME" not in r.stdout, r.stdout
    assert "avant l'installation des paquets" in r.stdout
    r = _bash(corps, tmp_path / "vieux-9.2")                                        # comparaison d'entiers, jamais de texte
    assert r.returncode == 2 and "pilote trop ancien : CUDA 9.2" in r.stdout, r.stdout
    r = _bash(corps, tmp_path / "na")                                               # m2 : la ligne lue est écrite au journal
    assert r.returncode == 2 and "illisible" in r.stdout
    assert "J lignes « CUDA » lues dans l'en-tête : | NVIDIA-SMI 580.65.06" in r.stdout and "CUDA Version: N/A" in r.stdout
    for nom in ("trace-telle-quelle", "double", "vide", "illisible", "majeur-seul", "absent", "na"):
        r = _bash(corps, tmp_path / nom)
        assert r.returncode == 2 and "illisible" in r.stdout and "CUDA CONFORME" not in r.stdout, (nom, r.stdout + r.stderr)
    # le code d'arrêt est celui de « torch ne voit pas la carte » dans les deux amorces
    for texte in (AMORCE_REP.read_text(encoding="utf-8"), ad.AMORCE.read_text(encoding="utf-8")):
        assert re.search(r'arret "torch ne voit pas la carte" 2', texte)
    # ordre : la garde est appelée une fois, après la capture de l'en-tête, avant toute installation
    rep = AMORCE_REP.read_text(encoding="utf-8")
    assert len(re.findall(r'^exiger_cuda_du_pilote "\$X/nvidia-smi-entete.txt"', rep, re.M)) == 1
    i = rep.index('exiger_cuda_du_pilote "$X/nvidia-smi-entete.txt"   #')
    assert rep.index("\nverifier_machine\n") < rep.index("\npreparer_depot ") < i < rep.index('\ninstaller_paquets "$T/venv/bin/python"')
    assert rep.index('nvidia-smi > "$X/nvidia-smi-entete.txt"') < rep.index("\nverifier_machine\n")
    course = ad.AMORCE.read_text(encoding="utf-8")
    assert len(re.findall(r'^exiger_cuda_du_pilote "\$X/nvidia-smi-entete.txt"', course, re.M)) == 1
    i = course.index('\nexiger_cuda_du_pilote "$X/nvidia-smi-entete.txt"')
    assert course.index('\nnvidia-smi > "$X/nvidia-smi-entete.txt"') < i < course.index("pip\" install") < course.index("torch.cuda.is_available()")
    assert i < course.index("git -c credential.helper")                               # avant le clonage et la sortie de 7b


def test_carte_et_cuda_de_la_course_en_tete_en_echec_et_hote_ancien(tmp_path):
    """m4 : l'arrêt « carte invisible (nvidia-smi, en-tête) » de l'étape 1 de la course, joué par son bloc marqué avec un faux
    `nvidia-smi` ; cas sain (13.0), en-tête en échec et hôte à 12.8 : code 2."""
    faux = ('[ "$#" = 0 ] && { [ "${FAUX_ENTETE:-}" = echec ] && exit 9; printf "%s" "$FAUX_TEXTE"; exit 0; }\n'
            'echo "NVIDIA A100-SXM4-80GB, 81920 MiB"\n')
    b = _faux(tmp_path, "nvidia-smi", faux)
    x = tmp_path / "x"
    x.mkdir()
    corps = TETE + f'X="{x}"; R="{tmp_path}"\n' + ad.extrait("cuda-du-pilote") + ad.extrait("carte-et-cuda") + 'echo "CARTE CONFORME"\n'
    env = {"PATH": f"{b}:{os.environ['PATH']}", "FAUX_TEXTE": ENTETE_SAIN}
    r = _bash(corps, env=env)
    assert r.returncode == 0 and "CARTE CONFORME" in r.stdout and "CUDA servie par le pilote : 13.0" in r.stdout, r.stdout + r.stderr
    r = _bash(corps, env={**env, "FAUX_ENTETE": "echec"})
    assert r.returncode == 2 and "carte invisible (nvidia-smi, en-tête)" in r.stdout and "CARTE CONFORME" not in r.stdout
    r = _bash(corps, env={**env, "FAUX_TEXTE": ENTETE_HOTE_DES_TRACES})
    assert r.returncode == 2 and "pilote trop ancien : CUDA 12.8" in r.stdout and "CARTE CONFORME" not in r.stdout


def _bloc_branche(lanceur: Path) -> str:
    t = lanceur.read_text(encoding="utf-8")
    m = re.findall(r"^# >>> branche-de-sortie\b[^\n]*\n(.*?)^# <<< branche-de-sortie$", t, re.S | re.M)
    assert len(m) == 1, lanceur
    return m[0]


def test_branche_de_sortie_neuve_exigee_avant_la_commande(tmp_path):
    """M1 : la branche de sortie de la répétition est `calcul/t07bbis-repetition-v2` (la v1 existe à distance depuis le
    15 novembre) ; `commande` des deux lanceurs refuse (code 2, motif écrit) si la branche de sortie de l'amorce existe déjà sur
    le dépôt distant, si celui-ci est injoignable, absent, ou n'est pas le dépôt de l'amorce. Cas sain et artefacts (R5)."""
    import hashlib
    rep = AMORCE_REP.read_text(encoding="utf-8")
    assert re.findall(r"^BR_SORTIE=(.*)$", rep, re.M) == ["calcul/t07bbis-repetition-v2"]
    assert re.findall(r"^BR_SORTIE=(.*)$", ad.AMORCE.read_text(encoding="utf-8"), re.M) == ["donnees/t07-etape-b-bis-v1"]
    bloc = _bloc_branche(LANCER_REP)
    assert bloc == _bloc_branche(ad.LANCER)                                           # même texte dans les deux lanceurs
    corps = "set -uo pipefail\n" + bloc + 'branche_de_sortie_neuve "$1" "$2"; c=$?; echo "CODE $c"; exit $c\n'
    d = ad.depot_vide(tmp_path / "d")
    ad.ecrire(d, "x", "x\n")
    ad.committer(d, "x")
    for amorce, br in ((AMORCE_REP, "calcul/t07bbis-repetition-v2"), (ad.AMORCE, "donnees/t07-etape-b-bis-v1")):
        r = _bash(corps, d, amorce)                                                   # aucun « origin »
        assert r.returncode == 2 and "« origin » absent" in r.stdout, r.stdout
    distant = ad.distant_officiel(d, tmp_path / "distant", ("calcul/t07bbis-repetition-v1", "main"))
    for amorce, br in ((AMORCE_REP, "calcul/t07bbis-repetition-v2"), (ad.AMORCE, "donnees/t07-etape-b-bis-v1")):
        r = _bash(corps, d, amorce)                                                   # cas sain : v1 présente, branche de l'amorce absente
        assert r.returncode == 0 and "CODE 0" in r.stdout, r.stdout + r.stderr
        ad.git(d, "push", "-q", "origin", f"HEAD:refs/heads/{br}")                   # artefact : branche de sortie présente
        r = _bash(corps, d, amorce)
        assert r.returncode == 2 and f"branche de sortie {br} présente" in r.stdout, r.stdout
    vieille = tmp_path / "vieille.sh"                                                 # artefact : l'amorce v1 (nom du 15 novembre)
    vieille.write_text(rep.replace("BR_SORTIE=calcul/t07bbis-repetition-v2", "BR_SORTIE=calcul/t07bbis-repetition-v1"), encoding="utf-8")
    r = _bash(corps, d, vieille)
    assert r.returncode == 2 and "calcul/t07bbis-repetition-v1 présente" in r.stdout
    double = tmp_path / "double.sh"
    double.write_text(rep + "BR_SORTIE=autre\n", encoding="utf-8")
    assert "illisible ou multiple" in _bash(corps, d, double).stdout
    d2 = ad.depot_vide(tmp_path / "d2")                                               # « origin » d'un autre dépôt
    autre = tmp_path / "autre" / "lciric" / "autre-depot.git"
    autre.parent.mkdir(parents=True)
    ad.git(tmp_path, "init", "-q", "--bare", str(autre))
    ad.git(d2, "remote", "add", "origin", str(autre))
    r = _bash(corps, d2, AMORCE_REP)
    assert r.returncode == 2 and "n'est pas le dépôt de l'amorce (lciric/controle-ia-travail)" in r.stdout, r.stdout
    d3 = ad.depot_vide(tmp_path / "d3")                                               # distant injoignable (nom juste, absent)
    ad.git(d3, "remote", "add", "origin", str(tmp_path / "rien" / "lciric" / "controle-ia-travail.git"))
    r = _bash(corps, d3, AMORCE_REP)
    assert r.returncode == 2 and "dépôt distant injoignable" in r.stdout, r.stdout
    # câblage : `commande` du lanceur de répétition refuse si la branche de sortie est présente
    dc, commit = _depot_commande(tmp_path / "depot")
    f = _offre(tmp_path / "offre.json")
    image = "pytorch/pytorch:2.4.1-cuda12.1-cudnn9-runtime"
    feu = f"feu de la mère : GO-2026-11-14-09, R-2802, image {image}"
    tmp = tmp_path / "tmp"
    tmp.mkdir()
    a = ("commande", dc, f, "99", commit, "prep/t07bbis-code-v1", int(time.time()) + 3600, "1.3", feu, image)
    assert _lancer_rep(*a, env={"TMPDIR": str(tmp)}).returncode == 0
    ad.git(dc, "push", "-q", "origin", "HEAD:refs/heads/calcul/t07bbis-repetition-v2")
    r = _lancer_rep(*a, env={"TMPDIR": str(tmp)})
    assert r.returncode == 2 and "BBIS REPETITION REFUS : branche de sortie calcul/t07bbis-repetition-v2 présente" in r.stdout
    assert "vastai create" not in r.stdout and list(tmp.iterdir()) == []
    assert hashlib.sha256(AMORCE_REP.read_bytes()).hexdigest()                      # (empreinte rendue par le rapport)
