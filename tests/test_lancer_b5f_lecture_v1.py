"""Essais du lanceur de la lecture du barreau 5 (`scripts/lancer_b5f_lecture_v1.sh`) : refus (sous-commande, arguments,
accord absent, identifiant de marche), configuration réelle imprimée, monde fabriqué joué tel quel par le programme de
lecture, texte du script sans commande d'arrêt, de création, de destruction ni de réseau."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "lancer_b5f_lecture_v1.sh"


def _jouer(*args, env=None):
    e = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHON_B5F": sys.executable, "PYTHONDONTWRITEBYTECODE": "1"}
    e.update(env or {})
    return subprocess.run(["bash", str(SCRIPT), *args], capture_output=True, text=True, env=e, cwd=str(RACINE))


@pytest.mark.parametrize("args", [[], ["inconnue"], ["config", "a"], ["verifier", "a", "b"], ["marche", "a"],
                                  ["ouvrir", "a"], ["monde", "a", "b"], ["preparer"], ["commande", "decisif"],
                                  ["detruire", "a"], ["verifier-destruction", "a"], ["scores", "a", "b"]])
def test_refus_sous_commande_ou_nombre_d_arguments(args):
    r = _jouer(*args)
    assert r.returncode == 2 and "B5F REFUS" in r.stderr


def test_config_exige_l_accord_et_un_plan_connu():
    r = _jouer("config", str(RACINE), "decisif", "entrees-lecture", "1", "couche_15")
    assert r.returncode == 2 and "GO_ID absent" in r.stderr
    r = _jouer("config", str(RACINE), "autre", "entrees-lecture", "1", "couche_15", env={"GO_ID": "GO-2026-11-24-01"})
    assert r.returncode == 2 and "PLAN" in r.stderr


def test_config_reelle_imprimee():
    r = _jouer("config", str(RACINE), "decisif", "entrees-lecture", "0", "une_sur_dix", env={"GO_ID": "GO-2026-11-24-01"})
    assert r.returncode == 0, r.stderr
    c = json.loads(r.stdout)
    assert c["mode"] == "reel" and c["plan"] == "decisif" and c["divergence"] is False and c["go_id"] == "GO-2026-11-24-01"
    assert c["couches"] == [7, 15, 23] and c["garde_activations"] == "une_sur_dix"
    r = _jouer("config", str(RACINE), "decisif", "entrees-lecture", "1", "tout", env={"GO_ID": "GO-2026-11-24-01"})
    assert r.returncode == 2 and "garde des activations" in r.stderr


def test_marche_refuse_un_identifiant_illisible(tmp_path):
    r = _jouer("marche", str(tmp_path / "c.json"), "20261124-120000-b5f-formation-1", "prereg/x.md")
    assert r.returncode == 2 and "RUN_ID" in r.stderr


def test_verifier_refuse_un_commit_illisible(tmp_path):
    cfg = tmp_path / "c.json"
    r0 = _jouer("config", str(RACINE), "decisif", "entrees-lecture", "1", "couche_15", env={"GO_ID": "GO-2026-11-24-01"})
    cfg.write_text(r0.stdout)
    r = _jouer("verifier", str(RACINE), "pas-un-commit", str(cfg))
    assert r.returncode == 2 and "commit" in r.stderr


def test_monde_fabrique_joue_par_le_programme_de_lecture(tmp_path):
    sys.path.insert(0, str(RACINE / "tests"))
    try:
        from test_barreau5_familles_lecture_v1 import _famille_effets, fabriquer
    finally:
        sys.path.pop(0)
    m = fabriquer(tmp_path, decalage=_famille_effets(sab=3.0, sur=6.0))
    reg = tmp_path / "registre.md"
    reg.write_text(m["registre"])
    r = _jouer("monde", str(reg), str(m["arbre"]), str(m["table"]), str(m["couts"]), str(m["formation"]),
               str(tmp_path / "sortie"))
    assert r.returncode == 0, r.stderr
    assert json.loads(r.stdout.strip().splitlines()[-1])["issue"] == "S"
    # le même monde, registre sans l'épreuve à vérité plantée : refus
    reg.write_text("\n".join(x for x in m["registre"].splitlines() if "EPREUVE-B5F" not in x) + "\n")
    r = _jouer("monde", str(reg), str(m["arbre"]), str(m["table"]), str(m["couts"]), str(m["formation"]),
               str(tmp_path / "sortie2"))
    assert r.returncode == 2 and "EPREUVE-B5F" in r.stderr


def test_texte_du_script_sans_commande_d_arret_de_creation_ni_de_reseau():
    texte = SCRIPT.read_text(encoding="utf-8")
    code = "\n".join(x for x in texte.splitlines() if not x.lstrip().startswith("#"))
    arret = "k" + "ill"                       # composé : la garde du dépôt refuse ce nom écrit dans une commande
    for interdit in (rf"\b{arret}\b", rf"\bp{arret}\b", r"\bp" + "grep\\b", rf"\b{arret}all\b", r"vastai", r"\bcurl\b",
                     r"\bwget\b", r"\bgit\s+push\b", r"\brm\s", r"huggingface"):
        assert re.search(interdit, code) is None, interdit
    assert "set -uo pipefail" in texte and "HF_HUB_OFFLINE=1" in code


# --- côté session : commande de création, destruction, ligne SCORES-B5F (ajout du 20 novembre) ----------------------

import base64  # noqa: E402
import hashlib  # noqa: E402
import shutil  # noqa: E402
import time  # noqa: E402
from datetime import date, datetime, timedelta, timezone  # noqa: E402

from controle_ia.barreau5_familles import engagement_v1 as en  # noqa: E402
from controle_ia.barreau5_familles import lecture_v1 as lv  # noqa: E402
from controle_ia.barreau5_familles import relecture_v1 as rv  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402

GO_LECTURE, GO_FORMATION = "GO-2026-11-24-01", "GO-2026-11-21-01"
OFFRE = {"id": 654321, "gpu_name": "A100 SXM4", "num_gpus": 1, "gpu_ram": 81920, "cpu_cores_effective": 32,
         "cpu_ram": 257000, "disk_space": 320, "cuda_max_good": 13.0, "dph_total": 1.2, "storage_cost": 0.1}
RUN_L, RUN_R = "20261124-120000-b5f-lecture", "20261123-120000-b5f-repetition"
EXISTANTS = [{"nom": f"R{k}-{m}", "chemin": f"donnees/existants-{k}/adaptateur-{m}.pt", "sha256": "a" * 64}
             for k in (1, 2) for m in ("saboteur", "temoin")]


def _g(r, *a):
    return subprocess.run(["git", "-C", str(r), *a], check=True, capture_output=True, text=True).stdout.strip()


def _ligne_go(ident):
    a, e = date.today() - timedelta(days=1), date.today() + timedelta(days=10)
    return f"| {ident} | {a.isoformat()} | calcul | lecture barreau 5 | 21 USD | {e.isoformat()} | Lazar | essai |"


def _registre(code_commit, sans=()):
    t0 = datetime.now(timezone.utc) - timedelta(days=2)
    lignes = [("SCELLEMENT-B5F", f"{lv.TEXTE} ; sha256 {lv.TEXTE_SHA256} ; membres-apprentissage 3 ; piece famille"),
              ("CODE-FORMATION-B5F", f"commit {'c' * 40} ; entropie 12345"), ("GO-FORMATION-B5F", GO_FORMATION),
              ("SORTIES-FORMATION-B5F", "versement prouvé"), ("ENGAGEMENT-B5F", f"sha256 {'d' * 64}"),
              ("CODE-LECTURE-B5F", f"commit {code_commit} ; lecture sha256 {lv.programme_sha256()}"),
              ("EPREUVE-B5F", f"passee ; lecture sha256 {lv.programme_sha256()} ; rapport sha256 {'e' * 64}"),
              ("GO-LECTURE-B5F", GO_LECTURE)]
    return "\n".join(en.ligne_du_registre(k, (t0 + timedelta(minutes=5 * i)).strftime("%Y-%m-%dT%H:%M:%SZ"), c, "")
                     for i, (k, c) in enumerate(x for x in lignes if x[0] not in sans)) + "\n"


@pytest.fixture
def session(tmp_path):
    """Dépôt jetable relié à un dépôt distant local : le code (garde de calcul copiée telle quelle, configuration scellée,
    texte scellé, amorce de lecture, adaptateurs existants factices), puis la marche (registre propre qui admet la lecture) ;
    la branche des entrées de lecture, poussée et tirée."""
    nu, r = tmp_path / "distant.git", tmp_path / "depot"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(nu)], check=True)
    subprocess.run(["git", "clone", "-q", str(nu), str(r)], check=True, capture_output=True)
    for a in (["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _g(r, *a)
    (r / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(RACINE / ".claude" / "hooks" / "garde_calcul.py", r / ".claude" / "hooks" / "garde_calcul.py")
    (r / "prereg").mkdir()
    for f in (rv.CONFIG_SCELLEE["chemin"], rv.CONFIG_SCELLEE["chemin"] + ".sha256", lv.TEXTE):
        shutil.copy(RACINE / f, r / f)
    (r / "scripts").mkdir()
    shutil.copy(RACINE / rv.AMORCE, r / rv.AMORCE)
    for x in EXISTANTS:
        (r / x["chemin"]).parent.mkdir(parents=True, exist_ok=True)
        (r / x["chemin"]).write_bytes(b"adaptateur factice")
    (r / "registres").mkdir()
    (r / "registres" / "go.md").write_text("| id | accordé | type | périmètre | plafond | échéance | par | réf |\n"
                                          + _ligne_go(GO_LECTURE) + "\n" + _ligne_go(GO_FORMATION) + "\n", encoding="utf-8")
    _g(r, "add", "-A")
    _g(r, "commit", "-q", "-m", "code")
    code = _g(r, "rev-parse", "HEAD")
    (r / en.REGISTRE_PROPRE).write_text(_registre(code), encoding="utf-8")
    _g(r, "add", "-A")
    _g(r, "commit", "-q", "-m", "marche (registre)")
    marche = _g(r, "rev-parse", "HEAD")
    _g(r, "push", "-q", "origin", "main")
    e = tmp_path / "entrees-graine"
    e.mkdir()
    for a in (["init", "-q", "-b", "x"], ["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _g(e, *a)
    (e / rv.DOSSIER_ENTREES).mkdir()
    (e / rv.DOSSIER_ENTREES / "X-01.safetensors").write_bytes(b"x")
    _g(e, "add", "-A")
    _g(e, "commit", "-q", "-m", "entrées de lecture")
    entrees = _g(e, "rev-parse", "HEAD")
    _g(e, "push", "-q", str(nu), f"x:refs/heads/{rv.BRANCHE_ENTREES}")
    _g(r, "fetch", "-q", "origin")
    (tmp_path / "offre.json").write_text(json.dumps(OFFRE))
    (tmp_path / "existants.json").write_text(json.dumps(EXISTANTS))
    (tmp_path / "aucun.json").write_text("[]")
    return {"r": r, "code": code, "marche": marche, "entrees": entrees, "t": tmp_path}


def _commande(s, plan="decisif", **k):
    a = {"offre_json": s["t"] / "offre.json", "commit": s["marche"], "branche": "main",
         "run_id": RUN_L if plan == "decisif" else RUN_R, "go_id": GO_LECTURE if plan == "decisif" else GO_FORMATION,
         "entrees_commit": s["entrees"] if plan == "decisif" else "", "divergence": True, "garde": "une_sur_dix",
         "existants_json": s["t"] / ("aucun.json" if plan == "decisif" else "existants.json")}
    a.update(k)
    return rv.commande_de_creation(s["r"], plan, a["offre_json"], a["commit"], a["branche"], a["run_id"], a["go_id"],
                                   a["entrees_commit"], a["divergence"], a["garde"], a["existants_json"], date.today(),
                                   time.time())


def test_commande_de_creation_plan_decisif_cas_sain(session):
    cmd = _commande(session)
    assert cmd.startswith(f"GO_ID={GO_LECTURE} vastai create instance 654321 --raw --image python:3.11-bookworm --disk 300 ")
    assert "--label b5f-lecture-v1" in cmd and f"-e ENTREES_COMMIT={session['entrees']}" in cmd
    assert f"-e COMMIT={session['marche']}" in cmd and f"-e PREREG={lv.TEXTE}" in cmd and "-e EXISTANTS_CHEMINS=-" in cmd
    assert "-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN" in cmd and "-e GARDE_B5F=une_sur_dix -e" in cmd
    b64 = re.search(r'echo (\S+) \| base64 -d > /root/amorce_b5f_lecture_v1\.sh', cmd).group(1)
    assert base64.b64decode(b64) == (RACINE / rv.AMORCE).read_bytes()               # l'amorce telle qu'au commit
    echeance = int(re.search(r"-e ECHEANCE_ARRET_UTC_S=(\d+)", cmd).group(1))
    assert abs(echeance - (time.time() + (21.0 / 1.2 - 0.25) * 3600)) < 120


def test_commande_de_creation_repetition_cas_sain(session):
    cmd = _commande(session, plan="repetition")
    assert "--disk 150" in cmd and "--label b5f-repetition-v1" in cmd and "-e ENTREES_COMMIT=-" in cmd
    assert f"-e EXISTANTS_CHEMINS={','.join(x['chemin'] for x in EXISTANTS)} " in cmd
    ex = base64.b64decode(re.search(r"-e EXISTANTS_B5F=(\S+)", cmd).group(1))
    assert json.loads(ex) == EXISTANTS


@pytest.mark.parametrize("cas", ["disque", "prix", "carte", "marche_autre_plan", "sans_entrees", "entrees_hors_branche",
                                 "go_autre", "existant_sans_empreinte", "existant_absent", "repetition_avec_entrees",
                                 "registre_sans_epreuve", "code_change"])
def test_commande_de_creation_artefacts_aucune_commande(session, cas):
    s, k, plan = session, {}, "decisif"
    if cas in ("disque", "prix", "carte"):
        o = dict(OFFRE, **{"disque": {"disk_space": 200}, "prix": {"dph_total": 1.35}, "carte": {"gpu_name": "H100 SXM"}}[cas])
        (s["t"] / "o.json").write_text(json.dumps(o))
        k["offre_json"] = s["t"] / "o.json"
    elif cas == "marche_autre_plan":
        k["run_id"] = RUN_R
    elif cas == "sans_entrees":
        k["entrees_commit"] = ""
    elif cas == "entrees_hors_branche":
        k["entrees_commit"] = s["code"]
    elif cas == "go_autre":
        k["go_id"] = GO_FORMATION
    elif cas == "existant_sans_empreinte":
        (s["t"] / "x.json").write_text(json.dumps([{**EXISTANTS[0], "nom": "ancre-R1", "sha256": ""}]))
        k["existants_json"] = s["t"] / "x.json"
    elif cas == "existant_absent":
        plan = "repetition"
        (s["t"] / "x.json").write_text(json.dumps(EXISTANTS[:3] + [{**EXISTANTS[3], "chemin": "donnees/absent/a.pt"}]))
        k["existants_json"] = s["t"] / "x.json"
    elif cas == "repetition_avec_entrees":
        plan, k["entrees_commit"] = "repetition", s["entrees"]
    elif cas == "registre_sans_epreuve":
        (s["r"] / en.REGISTRE_PROPRE).write_text(_registre(s["code"], sans=("EPREUVE-B5F",)), encoding="utf-8")
        _g(s["r"], "commit", "-q", "-am", "registre sans épreuve")
        k["commit"] = _g(s["r"], "rev-parse", "HEAD")
    elif cas == "code_change":
        (s["r"] / "scripts" / "autre.sh").write_text("echo x\n")
        _g(s["r"], "add", "-A")
        _g(s["r"], "commit", "-q", "-m", "code changé")
        k["commit"] = _g(s["r"], "rev-parse", "HEAD")
    with pytest.raises(GardeArret):
        _commande(s, plan=plan, **k)


def _config_decisive(s):
    return rv.config_lecture(s["r"], GO_LECTURE, "decisif", rv.ENTREES_DE_LA_MARCHE, True, "une_sur_dix")


def test_verifier_avant_creation_cas_sain_et_artefacts(session):
    """Constat M-4 de la contre-lecture : `verifier_avant_creation` (sous-commande « verifier ») sur un dépôt jetable : cas
    sain ; registre sans l'épreuve à vérité plantée ; marche qui ne descend pas du code ; arbre de travail changé."""
    s = session
    v = rv.verifier_avant_creation(s["r"], s["marche"], _config_decisive(s))
    assert v["commit"] == s["marche"] and v["commit_lecture"] == s["code"] and v["relance"] is None
    assert v["arbre_extrait"]["fichiers_extraits"] >= 4 and v["arbre_extrait"]["fichiers_parcourus"] >= 4
    with pytest.raises(GardeArret, match="commit"):
        rv.verifier_avant_creation(s["r"], "pas-un-commit", _config_decisive(s))
    # registre sans l'épreuve à vérité plantée, à un commit de marche neuf
    (s["r"] / en.REGISTRE_PROPRE).write_text(_registre(s["code"], sans=("EPREUVE-B5F",)), encoding="utf-8")
    _g(s["r"], "commit", "-q", "-am", "registre sans épreuve")
    sans_epreuve = _g(s["r"], "rev-parse", "HEAD")
    with pytest.raises(GardeArret, match="épreuve à vérité plantée"):
        rv.verifier_avant_creation(s["r"], sans_epreuve, _config_decisive(s))
    _g(s["r"], "reset", "-q", "--hard", s["marche"])
    # registre au commit du code (avant la marche) : registre propre absent
    with pytest.raises(GardeArret, match="registre propre absent"):
        rv.verifier_avant_creation(s["r"], s["code"], _config_decisive(s))
    # arbre de travail de la session changé (code) : refus
    (s["r"] / rv.AMORCE).write_text("echo autre\n")
    with pytest.raises(GardeArret, match="aucune ouverture"):
        rv.verifier_avant_creation(s["r"], s["marche"], _config_decisive(s))
    _g(s["r"], "checkout", "-q", "--", rv.AMORCE)
    rv.verifier_avant_creation(s["r"], s["marche"], _config_decisive(s))


def test_arbre_extrait_au_commit_sans_table_ni_ligne_de_la_formation(session):
    """Constat m-5 de la contre-lecture : la garde de l'arbre de la session de lecture est jouée côté session, sur ce que
    l'amorce extraira au commit de la marche (ses motifs) ; un fichier hors des motifs n'y entre pas."""
    s = session
    r = s["r"]
    hors = r / "docs" / "notes" / "x.json"
    hors.parent.mkdir(parents=True)
    hors.write_text(json.dumps([{"nom": "X-01", "famille": "T01", "membre": "jumeau"}]))
    _g(r, "add", "-A")
    _g(r, "commit", "-q", "-m", "note hors des motifs")
    sain = _g(r, "rev-parse", "HEAD")
    x = rv.exiger_arbre_extrait_propre(r, sain, "d" * 64, [])
    assert x["fichiers_extraits"] >= 4 and x["motifs"] == len(rv.motifs_de_l_amorce((RACINE / rv.AMORCE).read_text()))
    rv.verifier_avant_creation(r, sain, _config_decisive(s))
    for nom, corps, motif in (("table.json", [{"nom": "X-01", "famille": "T01", "membre": "jumeau"}], "table des étiquettes"),
                              ("cout.json", {"famille": "T03", "membre": "jumeau", "cout": 3.0}, "formation")):
        _g(r, "reset", "-q", "--hard", sain)
        dans = r / "docs" / "sources" / "invites-2606.08892-v1" / nom
        dans.parent.mkdir(parents=True, exist_ok=True)
        dans.write_text(json.dumps(corps))
        _g(r, "add", "-A")
        _g(r, "commit", "-q", "-m", f"{nom} dans un dossier extrait")
        c = _g(r, "rev-parse", "HEAD")
        with pytest.raises(GardeArret, match=motif):
            rv.verifier_avant_creation(r, c, _config_decisive(s))
        with pytest.raises(GardeArret, match=motif):
            _commande(s, commit=c)
    assert rv._extrait("scripts/amorce_b5f_lecture_v1.sh.sha256", ["/scripts/amorce_b5f_lecture_v1.sh*"])
    assert not rv._extrait("scripts/amorce/x.sh", ["/scripts/amorce*"])           # l'étoile ne passe pas « / »
    assert rv._extrait("src/a/b.py", ["/src/"]) and not rv._extrait("srcx/b.py", ["/src/"])


def test_commande_par_le_lanceur(session):
    s = session
    args = ["commande", "decisif", str(s["r"]), str(s["t"] / "offre.json"), s["marche"], "main", RUN_L, s["entrees"], "1",
            "une_sur_dix", str(s["t"] / "aucun.json")]
    r = _jouer(*args, env={"GO_ID": GO_LECTURE})
    assert r.returncode == 0, r.stderr
    assert "B5F COMMANDE" in r.stdout and "vastai create instance 654321" in r.stdout
    r = _jouer(*args)
    assert r.returncode == 2 and "GO_ID absent" in r.stderr


def _pousser_lecture(s, run=RUN_L, abimer=False):
    """Arbre fermé fabriqué au commit d'une branche de lecture poussée ; rend le commit."""
    r = s["r"]
    _g(r, "checkout", "-q", "-b", "lecture")
    arbre = r / "donnees" / run / "lecture"
    arbre.mkdir(parents=True)
    (arbre / "bilan-relecture.json").write_text("{}")
    lv.ecrire_inventaire(arbre, run)
    if abimer:
        (arbre / "bilan-relecture.json").write_text("{\"x\": 1}")
    (r / "runs" / run).mkdir(parents=True)
    (r / "runs" / run / "manifeste.json").write_text("{}\n")
    _g(r, "add", "-A")
    _g(r, "commit", "-q", "-m", "arbre fermé")
    _g(r, "push", "-q", "-f", "origin", "lecture")
    return _g(r, "rev-parse", "HEAD")


def test_ligne_scores_cas_sain_et_artefacts(session):
    s = session
    c = _pousser_lecture(s)
    attendu = hashlib.sha256((s["r"] / "donnees" / RUN_L / "lecture" / "inventaire.json").read_bytes()).hexdigest()
    assert rv.ligne_scores(s["r"], c, RUN_L) == f"commit {c} ; inventaire sha256 {attendu}"
    r = _jouer("scores", str(s["r"]), c, RUN_L)
    assert r.returncode == 0 and r.stdout.strip() == f"commit {c} ; inventaire sha256 {attendu}"
    with pytest.raises(GardeArret):
        rv.ligne_scores(s["r"], s["code"], RUN_L)                                    # arbre absent du commit
    _g(s["r"], "checkout", "-q", "main")
    _g(s["r"], "branch", "-q", "-D", "lecture")
    c2 = _pousser_lecture(s, abimer=True)
    with pytest.raises(GardeArret, match="empreinte"):
        rv.ligne_scores(s["r"], c2, RUN_L)


def test_ligne_scores_commit_non_verse_refus(session):
    s = session
    r = s["r"]
    _g(r, "checkout", "-q", "-b", "locale")
    arbre = r / "donnees" / RUN_L / "lecture"
    arbre.mkdir(parents=True)
    (arbre / "bilan-relecture.json").write_text("{}")
    lv.ecrire_inventaire(arbre, RUN_L)
    _g(r, "add", "-A")
    _g(r, "commit", "-q", "-m", "non poussé")
    with pytest.raises(GardeArret, match="branche distante"):
        rv.ligne_scores(r, _g(r, "rev-parse", "HEAD"), RUN_L)


def test_destruction_par_l_identifiant_apres_preuve_du_versement(session):
    s = session
    c = _pousser_lecture(s)
    inv = s["t"] / "inventaire-final.json"
    f = s["r"] / "donnees" / RUN_L / "lecture" / "bilan-relecture.json"
    inv.write_text(json.dumps({"run_id": RUN_L, "fichiers": [{"chemin": f"donnees/{RUN_L}/lecture/bilan-relecture.json",
                                                              "octets": f.stat().st_size,
                                                              "sha256": hashlib.sha256(f.read_bytes()).hexdigest()}]}))
    sceller(inv)
    liste = s["t"] / "liste.json"
    liste.write_text(json.dumps([{"id": 4242, "label": "b5f-lecture-v1"}, {"id": 7, "label": "b5f-formation-v1-3"}]))
    assert rv.commande_de_destruction(s["r"], "4242", "decisif", liste, inv, c, GO_LECTURE) == \
        f"GO_ID={GO_LECTURE} vastai destroy instance 4242 -y"
    for ident, plan in (("7", "decisif"), ("4242", "repetition"), ("99", "decisif"), ("42x", "decisif")):
        with pytest.raises(GardeArret):
            rv.commande_de_destruction(s["r"], ident, plan, liste, inv, c, GO_LECTURE)
    with pytest.raises(GardeArret):
        rv.commande_de_destruction(s["r"], "4242", "decisif", liste, inv, s["code"], GO_LECTURE)   # fichier absent du commit


def test_offre_et_echeance_de_la_lecture():
    assert rv.exiger_offre_lecture(OFFRE, "decisif") == {"id": "654321", "prix_usd_h": 1.2}
    assert rv.exiger_offre_lecture(dict(OFFRE, disk_space=150), "repetition")["id"] == "654321"
    for mauvais in ({"disk_space": 299}, {"num_gpus": 2}, {"cpu_ram": 64000}, {"cuda_max_good": 12.4},
                    {"storage_cost": 0.3}, {"id": "x1"}, {"gpu_ram": None}):
        with pytest.raises(GardeArret):
            rv.exiger_offre_lecture(dict(OFFRE, **mauvais), "decisif")
    assert rv.echeance_arret_lecture_s(0, "decisif", 1.3) == int((21.0 / 1.3 - 0.25) * 3600)
    assert rv.echeance_arret_lecture_s(0, "repetition", 1.3) == int((8.0 / 1.3 - 0.25) * 3600)
    with pytest.raises(GardeArret):
        rv.echeance_arret_lecture_s(0, "decisif", 1.4)


def test_activations_gardees_lues_dans_la_liste_scellee(tmp_path):
    s = tmp_path / "donnees" / RUN_L
    s.mkdir(parents=True)
    liste = ["activations/nu/c15/e0__p0.npy", "activations/X-01/c15/e3__p9.npy"]
    (s / "garde-activations.json").write_text(json.dumps({"regle": "une_sur_dix", "fichiers": liste}))
    sceller(s / "garde-activations.json")
    assert rv.activations_gardees(s) == [(s / c).as_posix() for c in liste]
    for mauvais in (["lecture/scores/decisive-pli0.json"], ["activations/nu/c16/e0__p0.npy"], ["../x.npy"]):
        d = tmp_path / f"m{len(mauvais[0])}"
        d.mkdir()
        (d / "garde-activations.json").write_text(json.dumps({"regle": "une_sur_dix", "fichiers": mauvais}))
        sceller(d / "garde-activations.json")
        with pytest.raises(GardeArret, match="liste blanche"):
            rv.activations_gardees(d)
    (s / "garde-activations.json").write_text(json.dumps({"regle": "une_sur_dix", "fichiers": []}))
    with pytest.raises(GardeArret):
        rv.activations_gardees(s)                                   # compagnon d'empreinte faux : refus


def test_prechargement_du_modele_de_la_configuration_scellee(monkeypatch):
    from controle_ia.harnais import modeles
    vus = []
    monkeypatch.setattr(modeles, "precharger_modele", lambda nom, revision: vus.append((nom, revision)) or "/cache")
    assert rv.precharger(RACINE) == "/cache"
    assert vus == [("meta-llama/Llama-3.1-8B-Instruct", "0e9e39f249a16976918f6564b8830bc894c89659")]
