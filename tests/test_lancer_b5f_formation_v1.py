"""Essais hors ligne du lanceur de formation du barreau 5 (`scripts/lancer_b5f_formation_v1.sh`) : il ne crée, n'arrête
ni ne détruit rien ; il contrôle et imprime. Cas sain et artefact pour chaque garde (R5). Dépôt jetable, registres
fabriqués ; la garde de calcul du dépôt est copiée telle quelle. Corrigés le 19 novembre 2026 selon la contre-lecture du
code de formation (constats M-1, M-3, M-5, m-8, m-9 ; mutation M12)."""
from __future__ import annotations

import base64
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import date, timedelta
from pathlib import Path

import pytest
import torch

from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.barreau5_familles import formation_v1 as fv

RACINE_DEPOT = Path(__file__).resolve().parents[1]
SCRIPT = RACINE_DEPOT / "scripts" / "lancer_b5f_formation_v1.sh"
GO = "GO-2026-11-20-01"
GO_RELANCE = "GO-2026-11-20-03"
OFFRE = {"id": 123456, "gpu_name": "A100 SXM4", "num_gpus": 1, "gpu_ram": 81920, "cpu_cores_effective": 32,
         "cpu_ram": 257000, "disk_space": 200, "cuda_max_good": 13.0, "dph_total": 1.2, "storage_cost": 0.1}
PREREG = "prereg/barreau5-essai-v1.md"
RUN = "20261123-080000-b5f-formation-3"


def _git(r, *args):
    return subprocess.run(["git", "-C", str(r), *args], check=True, capture_output=True, text=True).stdout.strip()


def _ligne_go(ident, typ="calcul", par="Lazar"):
    a, e = date.today() - timedelta(days=1), date.today() + timedelta(days=10)
    return f"| {ident} | {a.isoformat()} | {typ} | formation barreau 5 | 200 USD | {e.isoformat()} | {par} | essai |"


def _registre_propre(r, code_commit, go=GO, membres=2, piece="instance", texte=PREREG, sha=None, relance=None,
                     scellement=True, code_relance=None):
    sha = sha or hashlib.sha256((r / texte).read_bytes()).hexdigest()
    lignes = [en.ligne_du_registre("SCELLEMENT-B5F", "2026-11-21T18:00:00Z",
                                   f"{texte} ; sha256 {sha} ; membres-apprentissage {membres} ; piece {piece}", "")]
    lignes = (lignes if scellement else []) + [
        en.ligne_du_registre("CODE-FORMATION-B5F", "2026-11-22T18:00:00Z", f"commit {code_commit} ; entropie 7", ""),
        en.ligne_du_registre("GO-FORMATION-B5F", "2026-11-22T19:00:00Z", go, "")]
    if relance:                                   # additif 1 : le code des relances, dans la référence de la ligne de relance
        lignes.append(en.ligne_du_registre("GO-RELANCE-FORMATION-B5F", "2026-11-25T08:00:00Z", relance,
                                           f"essai ; code des relances commit {code_relance}"))
    (r / fv.REGISTRE_PROPRE).write_text("\n".join(lignes) + "\n", encoding="utf-8")


def _code_v1(r):
    """Le commit du code des premières marches : le premier commit du dépôt jetable."""
    return _git(r, "rev-list", "--max-parents=0", "HEAD")


def _code_v2(r):
    """Le commit du code des relances : le code v1 plus un fichier ; créé une fois, descendant du code v1."""
    if not (r / "src" / "v2.py").is_file():
        (r / "src").mkdir(exist_ok=True)
        (r / "src" / "v2.py").write_text("V = 2\n", encoding="utf-8")
        _git(r, "add", "-A")
        _git(r, "commit", "-q", "-m", "code v2")
    return _git(r, "log", "-1", "--format=%H", "--", "src/v2.py")


def _course_de_relance(r, relance, **registre):
    """Course d'une relance : code v1 pour les premières marches, code v2 (fils) pour les relances."""
    registre.setdefault("code_relance", _code_v2(r))
    return _course(r, code=_code_v1(r), relance=relance, **registre)


def _course(r, **registre):
    """Registre propre neuf, commis : rend le commit de la course."""
    _registre_propre(r, registre.pop("code", None) or _git(r, "rev-parse", "HEAD~1"), **registre)
    _git(r, "commit", "-q", "-am", "course (registre neuf)")
    return _git(r, "rev-parse", "HEAD")


@pytest.fixture
def racine(tmp_path):
    """Dépôt jetable à deux commits : le code (garde de calcul copiée, amorce jouet, configuration scellée de la course de
    confirmation, texte), puis la course (registre propre qui cite le texte et le commit du code). Rend (racine, commit
    de la course)."""
    r = tmp_path / "depot"
    (r / ".claude" / "hooks").mkdir(parents=True)
    _git(r, "init", "-q")
    _git(r, "config", "user.email", "essai@invalid")
    _git(r, "config", "user.name", "essai")
    shutil.copy(RACINE_DEPOT / ".claude" / "hooks" / "garde_calcul.py", r / ".claude" / "hooks" / "garde_calcul.py")
    (r / "prereg").mkdir()
    for f in (fv.CONFIG_SCELLEE["chemin"], fv.CONFIG_SCELLEE["chemin"] + ".sha256"):
        shutil.copy(RACINE_DEPOT / f, r / f)
    (r / PREREG).write_text("# Texte scellé (essai)\n", encoding="utf-8")
    (r / "prereg" / "barreau5-autre-v1.md").write_text("# Autre texte (essai)\n", encoding="utf-8")
    (r / "prereg" / "barreau5-essai-v1-brouillon3.md").write_text("# Brouillon (essai)\n", encoding="utf-8")
    (r / "registres").mkdir()
    (r / "registres" / "go.md").write_text("| id | accordé | type | périmètre | plafond | échéance | par | réf |\n"
                                          + _ligne_go(GO) + "\n" + _ligne_go("GO-2026-11-20-02", typ="dépôt") + "\n"
                                          + _ligne_go(GO_RELANCE) + "\n", encoding="utf-8")
    (r / "scripts").mkdir()
    (r / fv.AMORCE).write_text("#!/usr/bin/env bash\necho amorce jouet\n", encoding="utf-8")
    (r / "offre.json").write_text(json.dumps(OFFRE), encoding="utf-8")
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "code")
    code = _git(r, "rev-parse", "HEAD")
    _registre_propre(r, code)
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "course")
    return r, _git(r, "rev-parse", "HEAD")


def _commande(r, commit, n=3, offre=None, run=RUN, prereg=PREREG, sous="commande"):
    return [sous, r, n, offre or (r / "offre.json"), commit, "main", prereg, run]


def _lancer(*args, go=GO):
    env = {k: v for k, v in os.environ.items() if k != "GO_ID"}
    env["PYTHON_B5F"] = sys.executable
    if go is not None:
        env["GO_ID"] = go
    return subprocess.run(["bash", str(SCRIPT), *map(str, args)], capture_output=True, text=True, env=env, timeout=120)


def test_plan_sept_instances_etiquetees():
    """Point (f) : à trois membres, les instances 6 et 7 portent leur entrée du devis (28 et 17 USD)."""
    r = _lancer("plan")
    assert r.returncode == 0
    lignes = [x for x in r.stdout.splitlines() if x.startswith("b5f-formation-v1-")]
    assert [x.split("\t")[0] for x in lignes] == [f"b5f-formation-v1-{n}" for n in range(1, 8)]
    assert "coupure à 3 membres 28 USD, 9.61 à 10.99 h ; à 2 membres 24 USD" in lignes[5]
    assert "coupure à 3 membres 17 USD, 5.71 à 6.4 h ; à 2 membres 15 USD" in lignes[6]
    assert "coupure à 3 membres 26 USD" in lignes[0]


def test_commande_cas_sain_etiquette_accord_echeance_cles_par_leur_nom_et_garde_de_calcul_rejouee(racine):
    r, course = racine
    avant = time.time()
    p = _lancer(*_commande(r, course))
    assert p.returncode == 0, p.stderr
    cmd = p.stdout.strip().splitlines()[-1]
    assert cmd.startswith(f"GO_ID={GO} vastai create instance 123456 ") and "--label b5f-formation-v1-3" in cmd
    for v in ("INSTANCE_B5F=3", "RELANCE_B5F=0", f"COMMIT={course}", "BRANCHE_CODE=main", f"PREREG={PREREG}",
              f"RUN_B5F={RUN}", "PRIX_USD_H=1.2", "HF_TOKEN=$HF_TOKEN", "GH_TOKEN=$GH_TOKEN"):
        assert v in cmd
    assert "\\$" not in cmd                                     # constat M-1 : aucune barre qui protège le signe
    arret = int(cmd.split("ECHEANCE_ARRET_UTC_S=")[1].split()[0])
    assert abs(arret - (avant + (26.0 / 1.2 - 0.25) * 3600)) < 120          # cumul plus un quart d'heure = coupure
    b64 = cmd.split("echo ")[1].split(" |")[0]
    assert base64.b64decode(b64) == (r / fv.AMORCE).read_bytes()
    fv.exiger_garde_de_calcul(r, cmd, date.today())               # la garde de calcul la laisserait passer


def test_commande_jouee_dans_un_shell_transmet_au_loueur_la_valeur_des_cles_jamais_leur_nom(racine):
    """Constat M-1 (forme du sondage S2) : la ligne imprimée, jouée dans un bash où `vastai` est une fonction qui affiche
    ses arguments et où les deux clés ont des valeurs factices, donne au loueur ces valeurs, jamais « $HF_TOKEN » ; la
    ligne imprimée, elle, ne porte que les noms."""
    r, course = racine
    p = _lancer(*_commande(r, course))
    cmd = p.stdout.strip().splitlines()[-1]
    assert "valeur-factice" not in cmd
    env = {"PATH": os.environ["PATH"], "HF_TOKEN": "valeur-factice-hf", "GH_TOKEN": "valeur-factice-gh"}
    joue = subprocess.run(["bash", "-c", 'vastai() { printf "%s\\n" "$@"; }\n' + cmd], env=env, capture_output=True,
                          text=True, timeout=60)
    assert joue.returncode == 0, joue.stderr
    arg_env = next(x for x in joue.stdout.splitlines() if x.startswith("-e INSTANCE_B5F"))
    assert "-e HF_TOKEN=valeur-factice-hf -e GH_TOKEN=valeur-factice-gh" in arg_env
    assert "$HF_TOKEN" not in arg_env and "$GH_TOKEN" not in arg_env


@pytest.mark.parametrize("cas", ["sans_go", "code_change", "code_non_ancetre", "amorce", "go_hors_registre",
                                 "go_non_calcul", "instance", "offre_chere", "offre_carte", "offre_cuda", "run",
                                 "sans_scellement", "autre_texte", "autre_empreinte", "brouillon", "texte_absent",
                                 "session_modifiee", "relance_sept_instances"])
def test_commande_artefacts_aucune_commande_de_creation(racine, cas):
    r, course = racine
    go, n, offre, run, prereg = GO, 3, None, RUN, PREREG
    if cas == "sans_go":
        go = None
    elif cas == "code_change":                       # code modifié après le commit de CODE-FORMATION-B5F
        (r / "src").mkdir()
        (r / "src" / "x.py").write_text("x = 1\n")
        _git(r, "add", "-A")
        _git(r, "commit", "-q", "-m", "code changé")
        course = _git(r, "rev-parse", "HEAD")
    elif cas == "code_non_ancetre":
        course = _course(r, code="d" * 40)
    elif cas == "amorce":                            # code cité sans amorce (retirer l'amorce change le code : autre motif)
        _git(r, "rm", "-q", fv.AMORCE)
        _git(r, "commit", "-q", "-m", "code sans amorce")
        course = _course(r, code=_git(r, "rev-parse", "HEAD"))
    elif cas == "go_hors_registre":
        (r / "registres" / "go.md").write_text("| id | a | t | p | pl | e | par | r |\n", encoding="utf-8")
    elif cas == "go_non_calcul":
        go = "GO-2026-11-20-02"
        course = _course(r, go=go)
    elif cas == "instance":
        n, run = 8, "20261123-080000-b5f-formation-8"
    elif cas == "run":
        run = "20261123-080000-b5f-formation-4"
    elif cas == "sans_scellement":
        course = _course(r, scellement=False)
    elif cas == "autre_texte":
        prereg = "prereg/barreau5-autre-v1.md"
    elif cas == "autre_empreinte":
        course = _course(r, sha="e" * 64)
    elif cas == "brouillon":                         # texte scellé comme brouillon : ni cité, ni accepté
        prereg = "prereg/barreau5-essai-v1-brouillon3.md"
        course = _course(r, texte=prereg)
    elif cas == "texte_absent":
        prereg = "prereg/barreau5-absent-v1.md"
    elif cas == "session_modifiee":                  # constat m-9 : l'arbre de travail de la session n'est pas le code figé
        (r / fv.AMORCE).write_text("#!/usr/bin/env bash\necho amorce retouchée\n", encoding="utf-8")
    elif cas == "relance_sept_instances":            # additif 1 : la ligne de relance cite six instances au plus
        course = _course_de_relance(r, f"{GO} ; instances 1,2,3,4,5,6,7", membres=3, piece="famille")
    else:
        o = dict(OFFRE)
        o.update({"offre_chere": {"dph_total": 1.35}, "offre_carte": {"gpu_name": "H100 SXM5"},
                  "offre_cuda": {"cuda_max_good": 12.8}}[cas])
        offre = r / "offre-artefact.json"
        offre.write_text(json.dumps(o), encoding="utf-8")
    p = _lancer(*_commande(r, course, n, offre, run, prereg), go=go)
    motifs = {"sans_go": "GO_ID absent", "code_change": "CODE-FORMATION-B5F", "code_non_ancetre": "CODE-FORMATION-B5F",
              "amorce": "amorce", "go_hors_registre": "absent de registres/go.md", "go_non_calcul": "pas « calcul »",
              "instance": "hors du plan", "offre_chere": "dph_total", "offre_carte": "carte", "offre_cuda": "cuda_max_good",
              "run": "identifiant de marche", "sans_scellement": "SCELLEMENT-B5F", "autre_texte": "texte cité",
              "autre_empreinte": "empreinte du texte", "brouillon": "brouillon", "texte_absent": "absent du commit",
              "session_modifiee": "arbre de travail de la session", "relance_sept_instances": "7 instances citées, 6 au plus"}
    assert p.returncode == 2 and "vastai create" not in p.stdout
    assert motifs[cas] in p.stderr, p.stderr


def test_commande_lit_le_registre_au_commit_de_la_course_et_non_dans_l_arbre_de_travail(racine):
    """Mutation M12 : un registre retouché dans l'arbre de travail (non commis) n'est jamais lu : l'accord du commit de la
    course passe, celui de l'arbre de travail est refusé."""
    r, course = racine
    _registre_propre(r, _git(r, "rev-parse", "HEAD~1"), go=GO_RELANCE)          # retouché, non commis
    p = _lancer(*_commande(r, course), go=GO)
    assert p.returncode == 0, p.stderr
    p = _lancer(*_commande(r, course), go=GO_RELANCE)
    assert p.returncode == 2 and f"≠ GO-FORMATION-B5F {GO}" in p.stderr, p.stderr


def test_relance_unique_cas_sain_et_artefacts(racine):
    """Constat M-5 : la relance d'une instance tombée exige GO-RELANCE-FORMATION-B5F qui la cite, son accord, et une
    marche suffixée « -x1 » ; la commande porte RELANCE_B5F=1. Additif 1 (code v2) : l'accord de la ligne de relance est
    celui de GO-FORMATION-B5F ; les six instances tombées sont citées d'un coup."""
    r, _ = racine
    course = _course_de_relance(r, f"{GO} ; instances 1,2,3,4,5,7", membres=3, piece="famille")
    run = RUN + "-x1"
    p = _lancer(*_commande(r, course, run=run, sous="relance"), go=GO)
    assert p.returncode == 0, p.stderr
    cmd = p.stdout.strip().splitlines()[-1]
    assert "RELANCE_B5F=1" in cmd and f"RUN_B5F={run}" in cmd and cmd.startswith(f"GO_ID={GO} vastai create")
    for args, go, motif in ((_commande(r, course, run=run, sous="relance"), GO_RELANCE, "≠ GO-RELANCE-FORMATION-B5F"),
                            (_commande(r, course, sous="relance"), GO, "identifiant de marche"),
                            (_commande(r, course, 6, run="20261123-080000-b5f-formation-6-x1", sous="relance"), GO,
                             "non accordée"),
                            (_commande(r, course, run=run), GO, "identifiant de marche")):
        p = _lancer(*args, go=go)
        assert p.returncode == 2 and motif in p.stderr, (motif, p.stderr)
    sans = _course(r, code=_code_v1(r))
    p = _lancer(*_commande(r, sans, run=run, sous="relance"), go=GO)
    assert p.returncode == 2 and "non accordée" in p.stderr, p.stderr
    autre = _course_de_relance(r, f"{GO_RELANCE} ; instances 3,5")    # un autre accord que celui de GO-FORMATION-B5F
    p = _lancer(*_commande(r, autre, run=run, sous="relance"), go=GO_RELANCE)
    assert p.returncode == 2 and "≠ accord de GO-FORMATION-B5F" in p.stderr, p.stderr
    six = _course_de_relance(r, f"{GO} ; instances 3,6")              # l'instance 6 n'est pas tombée
    p = _lancer(*_commande(r, six, run=run, sous="relance"), go=GO)
    assert p.returncode == 2 and "instance non tombée citée" in p.stderr, p.stderr


def test_relance_au_code_de_la_ligne_code_relance_cas_sain_et_artefacts(racine):
    """Additif 1 (code v2) : le code d'une relance est le « code des relances » que cite la référence de la ligne de
    relance, fils du code de CODE-FORMATION-B5F ; celui d'une première marche reste celui de CODE-FORMATION-B5F. Monde :
    code v1, puis code v2 (un fichier de plus), puis la course."""
    r, _ = racine
    v1, v2 = _code_v1(r), _code_v2(r)
    run = RUN + "-x1"
    course = _course_de_relance(r, f"{GO} ; instances 3,5")
    p = _lancer(*_commande(r, course, run=run, sous="relance"), go=GO)
    assert p.returncode == 0 and "RELANCE_B5F=1" in p.stdout, p.stderr
    p = _lancer(*_commande(r, course), go=GO)                         # une première marche ne joue pas le code v2
    assert p.returncode == 2 and f"celui de CODE-FORMATION-B5F {v1[:12]}" in p.stderr, p.stderr
    ancien = _course_de_relance(r, f"{GO} ; instances 3,5", code_relance=v1)      # la ligne cite le code v1 : refus
    p = _lancer(*_commande(r, ancien, run=run, sous="relance"), go=GO)
    assert p.returncode == 2 and "celui des premières marches" in p.stderr, p.stderr
    sans = _course_de_relance(r, f"{GO} ; instances 3,5", code_relance="")        # référence sans commit : refus
    p = _lancer(*_commande(r, sans, run=run, sous="relance"), go=GO)
    assert p.returncode == 2 and "une et une seule mention" in p.stderr, p.stderr
    branche = _git(r, "rev-parse", "--abbrev-ref", "HEAD")
    _git(r, "checkout", "-q", "-b", "cote", v1)                                    # fils du code v1, mais autre code
    (r / "src").mkdir(exist_ok=True)
    (r / "src" / "cote.py").write_text("C = 1\n", encoding="utf-8")
    _git(r, "add", "-A")
    _git(r, "commit", "-q", "-m", "code de côté")
    cote = _git(r, "rev-parse", "HEAD")
    _git(r, "checkout", "-q", "--orphan", "ailleurs")                              # code d'une autre lignée
    _git(r, "commit", "-q", "-m", "autre lignée")
    orphelin = _git(r, "rev-parse", "HEAD")
    _git(r, "checkout", "-q", branche)
    for autre, motif in (("d" * 40, "ne descend pas du code de CODE-FORMATION-B5F"),              # commit absent
                         (orphelin, "ne descend pas du code de CODE-FORMATION-B5F"),
                         (cote, f"celui de GO-RELANCE-FORMATION-B5F (code des relances) {cote[:12]}")):
        mauvais = _course_de_relance(r, f"{GO} ; instances 3,5", code_relance=autre)
        p = _lancer(*_commande(r, mauvais, run=run, sous="relance"), go=GO)
        assert p.returncode == 2 and motif in p.stderr, (motif, p.stderr)
    (r / fv.AMORCE).write_text("#!/usr/bin/env bash\necho amorce retouchée\n", encoding="utf-8")
    p = _lancer(*_commande(r, course, run=run, sous="relance"), go=GO)            # session qui ne joue pas le code v2
    assert (p.returncode == 2
            and "différent du code de GO-RELANCE-FORMATION-B5F (code des relances)" in p.stderr), p.stderr


def test_config_reelle_de_chaque_instance_cas_sain_et_artefacts(racine):
    r, course = racine
    for n in range(1, 8):
        for relance in (0, 1):
            p = _lancer("config", r, n, 1.25, course, relance)
            assert p.returncode == 0, p.stderr
            c = json.loads(p.stdout)
            assert c["mode"] == "reel" and c["instance"] == n and c["familles"] == list(fv.familles_du_plan(n, relance == 1))
            assert c["coupure_usd"] == fv.COUPURES_USD[n] and c["prix_usd_h"] == 1.25 and c["go_id"] == GO
            assert c["adaptateur"]["rang"] == 16 and c["distillation"]["epoques"] == 3     # recette scellée
            assert (c["membres_apprentissage"], c["piece"]) == (2, "instance")            # lus dans SCELLEMENT-B5F
    assert _lancer("config", r, 1, 1.40, course, 0).returncode == 2               # au-dessus du prix du devis
    trois = _course(r, membres=3, piece="famille")
    assert json.loads(_lancer("config", r, 3, 1.25, trois, 0).stdout)["membres_apprentissage"] == 3
    # point (f) : 39 adaptateurs, les instances 6 et 7 prennent leur entrée du devis à trois membres
    assert [json.loads(_lancer("config", r, n, 1.25, trois, 0).stdout)["coupure_usd"] for n in (6, 7)] == [28.0, 17.0]


def test_commande_a_trois_membres_instance_6_echeance_a_la_coupure_de_28_usd(racine):
    """Point (f) : à 39 adaptateurs, la commande de création de l'instance 6 passe, et son échéance d'arrêt se compte à
    la coupure de 28 USD de son entrée du devis."""
    r, _ = racine
    course = _course(r, membres=3, piece="famille")
    avant = time.time()
    p = _lancer(*_commande(r, course, 6, run="20261123-080000-b5f-formation-6"))
    assert p.returncode == 0, p.stderr
    arret = int(p.stdout.strip().splitlines()[-1].split("ECHEANCE_ARRET_UTC_S=")[1].split()[0])
    assert abs(arret - (avant + (28.0 / 1.2 - 0.25) * 3600)) < 120


def test_depense_cas_sain_et_artefacts_coupure_et_plafond():
    assert _lancer("depense", 1, 2, 20.0, 1.3, 100.0, 9.1, 0).returncode == 0
    r = _lancer("depense", 1, 2, 25.7, 1.3, 100.0, 9.1, 0)
    assert r.returncode == 2 and "detruire" in r.stderr
    assert _lancer("depense", 7, 2, 14.7, 1.3, 100.0, 9.1, 0).returncode == 2    # coupure de 15 USD de l'instance 7
    assert _lancer("depense", 1, 2, 10.0, 1.3, 198.0, 9.1, 0).returncode == 2    # plafond commun
    assert _lancer("depense", 9, 2, 1.0, 1.3, 1.0, 1.3, 0).returncode == 2       # instance hors du plan
    assert _lancer("depense", 6, 3, 27.6, 1.3, 1.0, 1.3, 0).returncode == 0      # 39 adaptateurs : coupure de 28 USD
    assert _lancer("depense", 6, 3, 27.7, 1.3, 1.0, 1.3, 0).returncode == 2
    assert _lancer("depense", 1, 2, 20.0, 1.3, 100.0, 9.1).returncode == 2        # RELANCE exigé, sans défaut
    assert _lancer("depense", 1, 2, 20.0, 1.3, 100.0, 9.1, 2).returncode == 2


def test_depense_d_une_relance_sous_le_plafond_commun_et_sa_coupure():
    """Additif 1 (code v2) : la dépense d'une relance entre sous le plafond commun, qui l'arrête aussi ; la coupure de
    l'instance qu'elle remplace tient toujours."""
    p = _lancer("depense", 3, 3, 20.0, 1.3, 150.0, 9.1, 1)
    assert p.returncode == 0 and json.loads(p.stdout) == {"instance": 3, "relance": True, "coupure": 26.0,
                                                          "plafond": 200.0}, p.stderr
    assert _lancer("depense", 3, 3, 20.0, 1.3, 199.9, 9.1, 1).returncode == 2     # plafond commun atteint : relance arrêtée
    assert _lancer("depense", 3, 3, 20.0, 1.3, 199.9, 9.1, 0).returncode == 2     # la même dépense, pour une pièce du devis
    assert _lancer("depense", 3, 3, 25.7, 1.3, 0.0, 0.0, 1).returncode == 2       # coupure de l'instance remplacée


def _verse(tmp_path):
    """Dépôt jetable relié à un dépôt distant nu : sorties fabriquées, manifeste, inventaire, commis et poussés."""
    distant = tmp_path / "distant.git"
    subprocess.run(["git", "init", "-q", "--bare", str(distant)], check=True)
    racine = tmp_path / "verse"
    racine.mkdir()
    for a in (["init", "-q"], ["config", "user.email", "essai@invalid"], ["config", "user.name", "essai"],
              ["remote", "add", "origin", str(distant)]):
        _git(racine, *a)
    sorties = racine / "donnees" / "run"
    (sorties / "T03").mkdir(parents=True)
    torch.save({"q.A": torch.zeros(2, 3), "q.B": torch.zeros(3, 2)}, sorties / "T03" / "adaptateur-jumeau.pt")
    (racine / "runs" / "run").mkdir(parents=True)
    (racine / "runs" / "run" / "manifeste.json").write_text("{}\n")
    inv = fv.ecrire_inventaire(sorties, racine, "run")
    _git(racine, "add", "-A")
    _git(racine, "commit", "-q", "-m", "versement")
    _git(racine, "push", "-q", "origin", "HEAD:refs/heads/donnees/essai")
    _git(racine, "fetch", "-q", "origin")
    return racine, inv, _git(racine, "rev-parse", "HEAD")


def _liste(tmp_path, instances):
    p = tmp_path / "instances.json"
    p.write_text(json.dumps(instances), encoding="utf-8")
    return p


def test_detruire_cas_sain_etiquette_et_versement_prouves(tmp_path):
    racine, inv, tete = _verse(tmp_path)
    liste = _liste(tmp_path, [{"id": 42, "label": "b5f-formation-v1-2"}, {"id": 7, "label": "autre"}])
    r = _lancer("detruire", racine, 42, 2, liste, inv, tete)
    assert r.returncode == 0, r.stderr
    assert f"GO_ID={GO} vastai destroy instance 42 -y" in r.stdout


@pytest.mark.parametrize("cas", ["etiquette", "identifiant", "absente", "non_verse", "sans_go", "jamais_pousse"])
def test_detruire_artefacts_rien_n_est_detruit(tmp_path, cas):
    racine, inv, tete = _verse(tmp_path)
    instances, ident, go, commit = [{"id": 42, "label": "b5f-formation-v1-2"}], "42", GO, tete
    if cas == "etiquette":
        instances = [{"id": 42, "label": "bbis-t07-v1"}]
    elif cas == "identifiant":
        ident = "42x"
    elif cas == "absente":
        ident = "43"
    elif cas == "sans_go":
        go = None
    elif cas == "non_verse":
        torch.save({"q.A": torch.ones(2, 3), "q.B": torch.zeros(3, 2)}, racine / "donnees" / "run" / "T03" / "adaptateur-jumeau.pt")
        _git(racine, "commit", "-q", "-am", "changé")
        _git(racine, "push", "-q", "origin", "HEAD:refs/heads/donnees/essai")
        _git(racine, "fetch", "-q", "origin")
        commit = _git(racine, "rev-parse", "HEAD")
    elif cas == "jamais_pousse":                     # constat m-8 : commit local, absent de toute branche distante
        _git(racine, "commit", "-q", "--allow-empty", "-m", "local")
        commit = _git(racine, "rev-parse", "HEAD")
    r = _lancer("detruire", racine, ident, 2, _liste(tmp_path, instances), inv, commit, go=go)
    assert r.returncode == 2 and "destroy" not in r.stdout


def test_verifier_destruction_cas_sain_et_artefacts(tmp_path):
    assert _lancer("verifier-destruction", _liste(tmp_path, [{"id": 7}]), 42, 7).returncode == 0
    assert _lancer("verifier-destruction", _liste(tmp_path, [{"id": 7}, {"id": 42}]), 42, 7).returncode == 2
    assert _lancer("verifier-destruction", _liste(tmp_path, []), 42, 7).returncode == 2


def test_sous_commande_inconnue_refusee():
    assert _lancer("arreter-tout").returncode == 2
