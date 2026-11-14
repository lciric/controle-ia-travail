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
             'XT=traces/bbis-t07-repetition-v1; BR_SORTIE=calcul/t07bbis-repetition-v1; SEUIL=94000000\n'
             'fin_instance() { echo "FIN $1"; exit "$1"; }\nsleep() { :; }\n'
             + _extrait_rep("traces-de-la-repetition") + 'arret "essais : 80 passés < MIN_ESSAIS 86 de la course" 7\n')

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
    assert r.returncode == 7 and "traces poussées" in r.stdout and "FIN 7" in r.stdout, r.stdout + r.stderr
    tete = ad.git(distant, "rev-parse", "refs/heads/calcul/t07bbis-repetition-v1")
    assert ad.git(distant, "rev-parse", f"{tete}^") == commit
    assert ad.git(distant, "ls-tree", "-r", "--name-only", tete).splitlines() == [
        "src/controle_ia/x.py", "traces/bbis-t07-repetition-v1/journal-repetition.txt"]
    d, commit, distant, x = preparer(tmp_path / "avant")                           # artefact : avant le contrôle de la branche
    r = ad.jouer(corps, d, x, tmp_path / "avant", commit, 0, cwd=d)
    assert r.returncode == 7 and "traces poussées" not in r.stdout
    assert subprocess.run(["git", "-C", str(distant), "rev-parse", "--verify", "-q", "refs/heads/calcul/t07bbis-repetition-v1"],
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
         "etiquette": "bbis-t07-repetition-v1", "prix_usd_h": 1.3}
    o.update(k)
    chemin.write_text(json.dumps(o), encoding="utf-8")
    return chemin


def _depot_commande(base: Path, amorce_rep: str | None = None, avec_script: bool = True) -> tuple[Path, str]:
    d = ad.depot_vide(base)
    ad.ecrire(d, "scripts/amorce_bbis_v1.sh", (RACINE / "scripts" / "amorce_bbis_v1.sh").read_text(encoding="utf-8"))
    ad.ecrire(d, "scripts/amorce_repetition_bbis_v1.sh", amorce_rep or AMORCE_REP.read_text(encoding="utf-8"))
    if avec_script:
        ad.ecrire(d, "scripts/repetition_carte_bbis_v1.py", SCRIPT.read_text(encoding="utf-8"))
    return d, ad.committer(d, "code et répétition")


def test_lanceur_offre_commande_et_depense(tmp_path):
    import hashlib
    assert subprocess.run(["bash", "-n", str(LANCER_REP)]).returncode == 0
    assert subprocess.run(["bash", "-n", str(AMORCE_REP)]).returncode == 0
    f = _offre(tmp_path / "offre.json")
    assert _lancer_rep("offre", f, "99", "1.3").returncode == 0
    for faute, motif in (({"id": 98}, "identifiant"), ({"carte": "H200 SXM 141GB"}, "A100"), ({"etiquette": "bbis-t07-v1"}, "étiquette"),
                         ({"prix_usd_h": 1.5}, "prix"), ({"disque_go": 40}, "disque_go")):
        r = _lancer_rep("offre", _offre(tmp_path / "faute.json", **faute), "99", str(faute.get("prix_usd_h", 1.3)))
        assert r.returncode == 2 and motif in r.stdout, faute
    d, commit = _depot_commande(tmp_path / "depot")
    tmp = tmp_path / "tmp"
    tmp.mkdir()
    feu = "feu de la mère : GO-2026-11-14-09, R-2802"
    args = lambda commit_, ech, feu_=feu, offre=f: ("commande", d, offre, "99", commit_, "prep/t07bbis-code-v1", ech, "1.3", feu_,
                                                    "python:3.11-bookworm")
    r = _lancer_rep(*args(commit, int(time.time()) + 3600), env={"TMPDIR": str(tmp)})
    assert r.returncode == 0, r.stdout
    sha = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
    ligne = r.stdout.splitlines()[-1]
    assert ligne.startswith("GO_ID=GO-2026-11-14-09 vastai create instance 99 ") and "--label bbis-t07-repetition-v1" in ligne
    assert f"-e SCRIPT_SHA256={sha}" in ligne and "-e GH_TOKEN=$GH_TOKEN" in ligne and "--disk 60" in ligne
    assert "HF_TOKEN" not in ligne and list(tmp.iterdir()) == []
    for a, motif in ((args(commit, int(time.time()) + 3600, "feu GO-2026-11-14-09"), "R-2802"),
                     (args(commit, int(time.time()) + 2 * 3600), "au plus 1.75 h"),
                     (args("e" * 40, int(time.time()) + 3600), "absent de")):
        r = _lancer_rep(*a, env={"TMPDIR": str(tmp)})
        assert r.returncode == 2 and motif in r.stdout, (motif, r.stdout)
    d2, c2 = _depot_commande(tmp_path / "autre-amorce", amorce_rep=AMORCE_REP.read_text(encoding="utf-8") + "# autre\n")
    r = _lancer_rep("commande", d2, f, "99", c2, "prep/t07bbis-code-v1", int(time.time()) + 3600, "1.3", feu, "python:3.11-bookworm")
    assert r.returncode == 2 and "amorce de répétition du commit" in r.stdout
    d3, c3 = _depot_commande(tmp_path / "sans-script", avec_script=False)
    r = _lancer_rep("commande", d3, f, "99", c3, "prep/t07bbis-code-v1", int(time.time()) + 3600, "1.3", feu, "python:3.11-bookworm")
    assert r.returncode == 2 and "script de la répétition absent" in r.stdout
    assert _lancer_rep("depense", "2.0", "1.3").returncode == 0                     # 2,0 + 0,325 < 3
    r = _lancer_rep("depense", "2.7", "1.3")                                        # 2,7 + 0,325 ≥ 3 : arrêt et destruction
    assert r.returncode == 2 and "coupure 3 USD" in r.stdout and "detruire" in r.stdout and "verifier-destruction" in r.stdout


FAUX_VASTAI = r"""#!/usr/bin/env bash
etat="$FAUX_ETAT"
case "$1 $2" in
    "destroy instance") id="$3"; shift 3; oui=0; for a in "$@"; do [ "$a" = -y ] && oui=1; done
        if [ "$oui" = 0 ]; then printf '[y/N]: '; read -r rep || rep=""; [ "$rep" = y ] || { echo "Aborted."; exit 0; }; fi
        grep -vx "$id" "$etat" > "$etat.n"; mv "$etat.n" "$etat"; echo "destroying instance $id."; exit 0;;
    "show instances") python3 -c 'import json, sys; print(json.dumps([{"id": int(l)} for l in open(sys.argv[1]) if l.strip()]))' "$etat"; exit 0;;
esac
exit 1
"""


def test_la_repetition_lit_la_liste_de_la_course():
    """R-2795 : une seule liste des instances d'autres sessions, celle de la course, lue telle quelle par la répétition."""
    from controle_ia.t07bbis import registre_bbis_v1 as rb
    m = _module()
    assert m.INSTANCES_D_AUTRES_SESSIONS is rb.INSTANCES_D_AUTRES_SESSIONS and tuple(AUTRES) == rb.INSTANCES_D_AUTRES_SESSIONS
    assert not re.search(r"^INSTANCES_D_AUTRES_SESSIONS\s*=", SCRIPT.read_text(encoding="utf-8"), re.M)   # aucune copie
    with pytest.raises(m.Refus, match="autre session"):
        m.exiger_identifiant("60670453")
    assert m.exiger_absence([{"id": 60670453}], "424242", "60670453")["temoin"] == "60670453"


def test_destruction_de_la_repetition_avec_y_verifiee_contre_un_faux_outil(tmp_path):
    def outil(base: Path, ids) -> dict:
        b = base / "bin"
        b.mkdir(parents=True)
        (b / "vastai").write_text(FAUX_VASTAI, encoding="utf-8")
        (b / "vastai").chmod(0o755)
        (base / "etat.txt").write_text("".join(f"{i}\n" for i in ids), encoding="utf-8")
        return {"PATH": f"{b}:{os.environ['PATH']}", "FAUX_ETAT": str(base / "etat.txt"), "TMPDIR": str(base)}

    r = _lancer_rep("detruire", "424242")
    ligne = r.stdout.splitlines()[0]
    assert r.returncode == 0 and ligne == "GO_ID=GO-2026-11-14-09 vastai destroy instance 424242 -y"
    assert "verifier-destruction 424242 60480302" in r.stdout
    env = outil(tmp_path / "sain", ["424242", "60670453"])
    d = subprocess.run(["bash", "-c", ligne], capture_output=True, text=True, stdin=subprocess.DEVNULL, env={**os.environ, **env})
    assert d.returncode == 0 and "destroying instance 424242" in d.stdout
    v = _lancer_rep("verifier-destruction", "424242", "60670453", env=env)
    assert v.returncode == 0 and "DESTRUCTION PROUVEE 424242" in v.stdout
    env = outil(tmp_path / "sans-y", ["424242", "60480302"])                       # le cas du 2026-11-14 : « Aborted. », code 0
    d = subprocess.run(["bash", "-c", ligne[: -len(" -y")]], capture_output=True, text=True, stdin=subprocess.DEVNULL,
                       env={**os.environ, **env})
    assert d.returncode == 0 and "Aborted." in d.stdout
    v = _lancer_rep("verifier-destruction", "424242", "60480302", env=env)
    assert v.returncode == 2 and "toujours dans la liste" in v.stdout
    v = _lancer_rep("verifier-destruction", "424242", "999", env=outil(tmp_path / "temoin", ["60480302"]))
    assert v.returncode == 2 and "témoin 999 absent" in v.stdout
    for autre in AUTRES:
        r = _lancer_rep("detruire", autre)
        assert r.returncode == 2 and "autre session" in r.stdout and "vastai destroy" not in r.stdout, autre
        assert _lancer_rep("verifier-destruction", autre, "424242", tmp_path / "sain" / "etat.txt").returncode == 2
    assert _lancer_rep("detruire", "inst*").returncode == 2
