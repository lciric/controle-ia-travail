"""Essais R5 de `scripts/lancer_course_ideation_organismes_discrets_v8.py` (organisme d'idéation sur la conception des
organismes discrets : trois courses jumelles, une par lignée externe — Carbon, Astra, Argon — Opus 5.5 en proposeur et juge
internes ; mots de Lazar du 18 novembre 2026), adaptation fidèle des essais du lanceur « Regard ou raisons » v1
(`tests/test_lancer_course_ideation_regard_ou_raisons_v1.py`), dont le lanceur v8 est une transformation contrôlée.

Gardés : M1, M2, relevé de dépense et copies scellées dans le dépôt, ligne de GO trouvée par son contenu, environnement par
liste de noms, aucun bras, les trois gardes isolées, l'arrêt propre par SIGINT relayé, le registre réel des GO avant comme
après l'inscription. Changés : l'argument est la **lignée** (`carbon`, `astra`, `argon`) ; les pièces (question v3, faits v3,
témoins v1, enveloppe et commande externes de la lignée) ; les plafonds du devis v3 (course 9,2 USD, pire cas et borne
34 USD, une seule passe) ; les gardes de taille par famille (Gemini : Carbon et Argon ; OpenAI : Astra) ; le périmètre de
la ligne (« organisme d'idéation », « organismes discrets », « trois lignées »). Ajoutés : argument de lignée, réglages
d'une lignée avec l'argument d'une autre, relance unique **par lignée**, garde de cumul à travers les lignées, planchers
Astra et par famille, refus de `--seconde-passe`, garde de la lignée dans la mesure.

Aucun modèle appelé, aucun réseau. Un **faux orchestrateur** (dépôt git jetable) est servi au lanceur par `Reglages` ; il
lit l'étiquette du proposeur externe dans sa commande et nomme ses gardes, ses fiches et son juge différé d'après elle.
Deux essais **sans appel** contre l'orchestrateur réel (liste blanche et mesure ; analyseur d'arguments) tournent quand le
clone est là, dans des processus à part, `-I -B`, cache d'octets hors du clone. Un essai lance le vrai fichier dans un
processus à part avec une commande **fausse** (sans `-I`, ou lignée inconnue) : il refuse avant le verrou et avant toute
écriture. La commande exacte de production n'est jamais jouée ici."""
from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import json
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path
from types import SimpleNamespace

import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "lancer_course_ideation_organismes_discrets_v8.py"
_spec = importlib.util.spec_from_file_location("lancer_course_ideation_organismes_discrets_v8", SCRIPT)
lc = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = lc
_spec.loader.exec_module(lc)

LIGNEES = lc.LIGNEES
AUTRES = ("astra", "argon")                        # la plupart des essais tournent sur « carbon » ; ceux-ci sur les deux autres

FAUX_V8 = r'''
import hashlib, json, os, sys, time
argv = sys.argv[1:]

def sceller(chemin, objet=None, texte=None):
    t = texte if texte is not None else json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    open(chemin, "w", encoding="utf-8").write(t)
    open(chemin + ".sha256", "w").write(hashlib.sha256(t.encode("utf-8")).hexdigest() + "  " + os.path.basename(chemin) + "\n")

def valeur(option, defaut=None):
    return argv[argv.index(option) + 1] if option in argv else defaut

ext = valeur("--proposeur-externe", "externe=inconnu").split("=")[0]      # étiquette de la lignée externe de la course

def consigner(mode):
    noms = [n for n in os.environ if "KEY" in n or "TOKEN" in n or "SECRET" in n]
    with open(os.environ["FAUX_JOURNAL"], "a") as f:
        f.write(json.dumps({"mode": mode, "argv": argv, "cwd": os.getcwd(), "noms_cle": noms, "go_id": os.environ.get("GO_ID"),
                            "noms_env": sorted(os.environ), "home": os.environ.get("HOME"), "etiquette_externe": ext,
                            "pycache_prefix": sys.pycache_prefix, "orig_argv": sys.orig_argv, "pid": os.getpid(),
                            "sid": os.getsid(0)}) + "\n")

if "--construire-liste-blanche" in argv:
    i = argv.index("--construire-liste-blanche")
    liste = {os.path.realpath(c): hashlib.sha256(open(c, "rb").read()).hexdigest() for c in argv[i + 1:]}
    if os.environ.get("FAUX_LB_AUTRE") == "1":
        liste = {"/autre": "0" * 64}
    if os.environ.get("FAUX_LB_SANS_SCEAU") == "1":
        open(argv[0], "w").write(json.dumps(liste))
    else:
        sceller(argv[0], liste)
    sys.exit(0)
if "--mesurer-consignes" in argv:
    consigner("mesure")
    if os.environ.get("FAUX_MESURE_ILLISIBLE") == "1":
        print("pas du JSON")
        sys.exit(0)
    ctrl = int(os.environ.get("FAUX_CONTROLE", "70000"))
    cle = os.environ.get("FAUX_ETIQUETTE_GARDE", ext)
    print(json.dumps({"sans_appel": True, "prix_entree_usd_par_million_jetons": 10.0,
                      "consignes": {"consigne_de_controle_externe": ctrl, "consigne_passe_1": 30000,
                                    "consigne_du_juge_maximale": 900000, "fiches_au_juge_au_maximum": 40,
                                    "nombre_par_proposeur": 6},
                      "garde_course": {"passerait": ctrl <= 400000},
                      "gardes_passes_externes": {cle: {"passe_1": {"passerait": True}}}}))
    sys.exit(0)
sortie = argv[0]
consigner("course")
time.sleep(float(os.environ.get("FAUX_DORT", "0")))
code = int(os.environ.get("FAUX_CODE", "0"))
if os.environ.get("FAUX_RIEN") == "1":
    sys.exit(code)
if os.environ.get("FAUX_CONTROLE_SEUL"):
    c = sortie + "-controle"
    os.makedirs(os.path.join(c, "tentative-1-externe-" + ext))
    if os.environ["FAUX_CONTROLE_SEUL"] == "plancher":
        sceller(os.path.join(c, "tentative-1.json"), {"reglages": {"cout_claude_usd": 0.0,
                "cout_externe_usd": float(os.environ.get("FAUX_COUT_CONTROLE", "1e-06"))}})
    sys.exit(2)
ids = ["opus-p1-01", "opus-p1-02", ext + "-p1-01", "opus-p1-03", ext + "-p1-02"]
fiches = [{"identifiant_auteur": i, "auteur": i.split("-p")[0], "passe": int(i.split("-p")[1][0]), "nom": "Idée " + i,
           "enonce": "énoncé de " + i, "empreinte": hashlib.sha256(i[::-1].encode()).hexdigest()} for i in ids]
sceller(os.path.join(sortie, "fiches-validees.json"), fiches)
sceller(os.path.join(sortie, "fiches-refusees.json"), [])
sceller(os.path.join(sortie, "fiches-en-quarantaine.json"), [])
sceller(os.path.join(sortie, "noyau", "temoins-servis.json"), [{"identifiant_auteur": "temoin-p0-01"}])
sceller(os.path.join(sortie, "notes-par-juge.json"), {"opus-juge": {"opus-p1-01": {"total": 9}}})
sceller(os.path.join(sortie, "lecture-course.json"),
        {"bras_rapporte_differe": [{"etiquette": ext + "-juge", "consigne_en_attente_sha256": "c" * 64}]})
sceller(os.path.join(sortie, "lecture.json"), {"juges": ["opus-juge"], "juge_externe_differe": ext + "-juge"})
sceller(os.path.join(sortie, "classement.json"), [{"identifiant_auteur": i, "rang": n + 1} for n, i in enumerate(ids)])
sceller(os.path.join(sortie, "manifeste-depart.json"), {"sortie": sortie, "etiquette_externe": ext})
sceller(os.path.join(sortie, "manifeste-fin.json"),
        {"reglages": {"journal": {"cout_total_usd": float(os.environ.get("FAUX_COUT_CLAUDE", "2.5")),
                                  "cout_externe_usd": float(os.environ.get("FAUX_COUT_EXTERNE", "2.0"))},
                      "en_attente_bras": True, "statut_course": {"statut": "ok" if code == 0 else "erreur"}}})
sys.exit(code)
'''

FAUX_ADAPTATEURS = r'''
import os
def etat_bac_a_sable_detaille():
    e = os.environ.get("FAUX_BAC", "actif")
    if e == "illisible":
        print("pas du JSON")
        raise SystemExit(0)
    if e == "erreur":
        raise RuntimeError("sonde en panne")
    return {"actif": e in ("actif", "sans_proc"), "proc_neuf": e in ("actif", "eteint_proc_neuf"), "motif": "faux : " + e}
'''

PERIM = ("**Organisme d'idéation, atelier d'idées (N-065, rôle 2), sur la conception des organismes discrets : trois lignées "
         "externes (Carbon, Astra, Argon), trois courses jumelles, Opus 5.5 en proposeur et juge internes** (composition A, "
         "mots de Lazar du 18 novembre 2026)")
GO_LIGNE = f"| GO-2026-11-18-01 | 2026-11-18 | calcul | {PERIM} | 34 USD | 2026-12-31 | Lazar | devis v3 |"
PFX = Path("/x/sortie/pycache")


def git(d, *a):
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sceller(p: Path, texte: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    Path(str(p) + ".sha256").write_text(f"{sha(p)}  {p.name}\n")


def reecrire_go(r, ligne):
    r.registre_go.write_text("| id | a | t | p | pl | e | par | ref |\n|---|\n" + ligne + "\n")


@pytest.fixture
def monde(tmp_path):
    orch = tmp_path / "orch"
    (orch / "demonstrations").mkdir(parents=True)
    (orch / "pole").mkdir()
    (orch / "demonstrations" / "ideation_v8.py").write_text(FAUX_V8)
    (orch / "pole" / "__init__.py").write_text("")
    (orch / "pole" / "adaptateurs.py").write_text(FAUX_ADAPTATEURS)
    (orch / ".gitignore").write_text("__pycache__/\n*.pyc\n*.log\n")
    git(orch, "init", "-q", "-b", "main")
    git(orch, "config", "user.email", "t@example.invalid")
    git(orch, "config", "user.name", "t")
    git(orch, "add", "-A")
    git(orch, "commit", "-q", "-m", "faux")
    arbre = subprocess.run(["git", "-C", str(orch), "rev-parse", "HEAD:"], capture_output=True, text=True).stdout.strip()
    depot = tmp_path / "depot"
    pieces_par_lignee = {}                                  # les pièces des trois lignées, écrites une fois chacune
    for lignee in LIGNEES:
        pieces_par_lignee[lignee] = {}
        for nom, (rel, _) in lc.pieces_de(lignee).items():
            p = depot / rel
            if not p.exists():
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(f"pièce factice {nom} ({rel})\n")
            pieces_par_lignee[lignee][nom] = (rel, sha(p))
    (depot / "scripts").mkdir()
    lanceur = depot / "scripts" / lc.FICHIER_LANCEUR
    shutil.copyfile(SCRIPT, lanceur)
    Path(str(lanceur) + ".sha256").write_text(f"{sha(lanceur)}  {lanceur.name}\n")
    (depot / "registres").mkdir()
    journal = tmp_path / "journal.jsonl"
    env = {"PATH": "/usr/bin:/bin", "HOME": str(tmp_path), "FAUX_JOURNAL": str(journal), "FAUX_BAC": "actif",
           "ANTHROPIC_API_KEY": "valeur-factice-d-essai", "AUTRE_SECRET_X": "factice", "LANG": "C.UTF-8",
           "CLAUDE_CODE_REMOTE": "true", "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST": "1", "ANTHROPIC_BASE_URL": "http://hote.invalid",
           "CCR_AGENT_PROXY_ENABLED": "1", "HTTPS_PROXY": "http://mandataire.invalid", "NODE_OPTIONS": "--x",
           "KIMI_API_KEY": "factice"}
    horloge = {"t": dt.datetime(2026, 11, 18, 1, 0, 0, tzinfo=dt.timezone.utc)}

    def maintenant():
        horloge["t"] += dt.timedelta(seconds=1)
        return horloge["t"]

    def reglages_pour(lignee):
        """Les réglages d'une lignée : mêmes dossiers, même environnement, même horloge ; pièces, plafonds et commande
        exacte de la lignée."""
        return lc.Reglages(depot=depot, orchestrateur=orch, arbre_orchestrateur=arbre,
                           empreintes_orchestrateur={"demonstrations/ideation_v8.py": sha(orch / "demonstrations/ideation_v8.py"),
                                                     "pole/adaptateurs.py": sha(orch / "pole/adaptateurs.py")},
                           pieces=dict(pieces_par_lignee[lignee]), registre_go=depot / "registres" / "go.md",
                           dossier_runs=depot / "runs" / "course-x", dossier_sorties=tmp_path / "sorties",
                           depot_attendu_par_l_enveloppe=depot, python=sys.executable, fichier_lanceur=lanceur,
                           drapeaux=SimpleNamespace(isolated=1, dont_write_bytecode=1),
                           orig_argv=(sys.executable, "-I", "-B", f"scripts/{lc.FICHIER_LANCEUR}", lignee), cwd=str(depot),
                           lignee=lignee, plafonds=lc.plafonds_de(lignee), environnement=env,
                           aujourd_hui=dt.date(2026, 11, 18), horodatage=lambda: "Wed Nov 18 01:00:00 UTC 2026",
                           maintenant=maintenant, prefixe_essais="FAUX_")
    r = reglages_pour("carbon")
    reecrire_go(r, GO_LIGNE)
    yield {"r": r, "journal": journal, "env": env, "tmp": tmp_path, "depot": depot, "reglages_pour": reglages_pour}
    for pid in superviseurs(r):                       # jamais par motif : par PID, ceux de cet essai seulement
        try:
            os.kill(pid, signal.SIGKILL)
            os.waitpid(pid, 0)
        except (ProcessLookupError, ChildProcessError):
            pass


def avec_lignee(monde, lignee):
    """Le même monde (dépôt, sorties, journal, environnement, horloge), vu par les réglages d'une autre lignée."""
    return dict(monde, r=monde["reglages_pour"](lignee))


def superviseurs(r):
    pids = []
    if r.dossier_runs.is_dir():
        for d in r.dossier_runs.iterdir():
            f = d / "manifeste-lanceur-depart.json"
            if f.exists():
                pids.append(json.loads(f.read_text())["superviseur"]["pid"])
            else:
                p = r.dossier_sorties / d.name / lc.SUPERVISEUR_DOSSIER / "pid-superviseur.json"
                if p.exists():
                    pids.append(json.loads(p.read_text())["pid_superviseur"])
    return pids


def attendre(monde):
    for pid in superviseurs(monde["r"]):
        try:
            os.waitpid(pid, 0)
        except ChildProcessError:
            for _ in range(200):
                if lc.debut_processus(pid) is None:
                    break
                time.sleep(0.05)


def journal(monde):
    if not monde["journal"].exists():
        return []
    return [json.loads(x) for x in monde["journal"].read_text().splitlines()]


def lancer(monde, capsys=None, argv=None):
    argv = (monde["r"].lignee,) if argv is None else argv
    code = lc.principal(list(argv), monde["r"])
    sortie = capsys.readouterr() if capsys else None
    return code, (sortie.err + sortie.out) if sortie else ""


def jouer(monde, capsys=None):
    """Lancement détaché, attente du superviseur par son PID, clôture par la même commande."""
    c1, t1 = lancer(monde, capsys)
    if c1 != 0:
        return c1, t1
    attendre(monde)
    c2, t2 = lancer(monde, capsys)
    assert c2 == 0 and "clôture" in t2, t2
    return c2, t1 + t2


def runs(monde):
    return lc.runs_du_lanceur(monde["r"])


def _tuer_superviseur(sup):
    pidf = Path(sup["dossier"]) / "pid-orchestrateur.json"
    for _ in range(100):
        if pidf.exists() and Path(str(pidf) + ".sha256").exists():
            break
        time.sleep(0.05)
    os.kill(sup["pid"], signal.SIGKILL)
    os.waitpid(sup["pid"], 0)
    return json.loads(pidf.read_text())


def _attendre_mort(pid):
    for _ in range(200):
        if lc.debut_processus(pid) is None:
            return
        time.sleep(0.05)


def _journal_course(monde):
    return [x for x in journal(monde) if x["mode"] == "course"]


def _json(objet):
    """L'objet tel qu'il revient d'un manifeste JSON (tuples devenus listes)."""
    return json.loads(json.dumps(objet))


# ============================================================================================ argument : la lignée, fermée

@pytest.mark.parametrize("argv", [[], ["1"], ["0"], ["Carbon"], ["CARBON"], ["kimi"], ["gemini"], ["carbon", "astra"],
                                  ["carbon", "carbon"], ["--accepter-sans-bac-a-sable"], [" carbon"], ["carbon "], ["une"]])
def test_argument_artefacts(monde, capsys, argv):
    assert lc.principal(argv, monde["r"]) == 2
    assert "un seul argument" in capsys.readouterr().err and not monde["journal"].exists()
    assert not monde["r"].dossier_sorties.exists()


def test_lignees_trois_et_relance_unique_par_lignee():
    assert lc.LIGNEES == ("carbon", "astra", "argon") and lc.MAX_COURSES == 2
    for absent in ("ARGUMENT", "GENERATIONS", "PROPOSEUR_EXTERNE", "JUGE_EXTERNE", "PASSE_2_EXTERNE_USD", "plancher_argon",
                   "ENROBAGE_PAR_FICHE_PASSE_2", "RESERVE_LECTEUR_USD"):
        assert not hasattr(lc, absent), absent


@pytest.mark.parametrize("lignee", LIGNEES)
def test_argument_lignee_acceptee(monde, capsys, lignee):
    """Chacune des trois lignées passe le filtre de l'argument : le refus vient ensuite (ici, option -I absente), jamais
    de l'argument ; rien n'est écrit."""
    m = avec_lignee(monde, lignee)
    m["r"].drapeaux = SimpleNamespace(isolated=0, dont_write_bytecode=1)
    code, err = lancer(m, capsys)
    assert code == 2 and "-I absente" in err and "un seul argument" not in err
    assert lignee in err and not m["r"].dossier_sorties.exists() and not monde["journal"].exists()


@pytest.mark.parametrize("lignee", ["1", "Carbon", "kimi", "", "carbon "])
def test_production_refuse_lignee_inconnue(lignee):
    with pytest.raises(lc.Refus, match="lignée inconnue"):
        lc.Reglages.production(lignee)


@pytest.mark.parametrize("lignee_reglages,argument", [("carbon", "astra"), ("argon", "carbon"), ("astra", "argon")])
def test_reglages_d_une_lignee_argument_d_une_autre(monde, capsys, lignee_reglages, argument):
    m = avec_lignee(monde, lignee_reglages)
    code, err = lancer(m, capsys, argv=(argument,))
    assert code == 2 and "lignée des réglages" in err and lignee_reglages in err and argument in err
    assert not m["r"].dossier_sorties.exists() and not monde["journal"].exists()


# ============================================================================================ M1 : le lanceur se garde

@pytest.mark.parametrize("lignee", LIGNEES)
def test_m1_sain(monde, lignee):
    m = avec_lignee(monde, lignee)
    soi = lc.verifier_soi(m["r"])
    assert soi["sha256"] == sha(m["r"].fichier_lanceur) and soi["version"] == lc.VERSION
    assert soi["commande"][-1] == lignee


@pytest.mark.parametrize("modif,motif", [
    ({"drapeaux": SimpleNamespace(isolated=0, dont_write_bytecode=1)}, "-I absente"),
    ({"drapeaux": SimpleNamespace(isolated=1, dont_write_bytecode=0)}, "-B absente"),
    ({"orig_argv": ("/autre/python3", "-I", "-B", f"scripts/{lc.FICHIER_LANCEUR}", "carbon")}, "commande d'origine"),
    ({"orig_argv": ("PY", "-I", "-B", "-X", "dev", f"scripts/{lc.FICHIER_LANCEUR}", "carbon")}, "commande d'origine"),
    ({"orig_argv": ("PY", "-IB", f"scripts/{lc.FICHIER_LANCEUR}", "carbon")}, "commande d'origine"),
    ({"orig_argv": ("PY", "-I", "-B", f"./scripts/{lc.FICHIER_LANCEUR}", "carbon")}, "commande d'origine"),
    ({"orig_argv": ("PY", "-I", "-B", f"scripts/{lc.FICHIER_LANCEUR}", "carbon", "x")}, "commande d'origine"),
    ({"orig_argv": ("PY", "-I", "-B", f"scripts/{lc.FICHIER_LANCEUR}", "astra")}, "commande d'origine"),
    ({"orig_argv": ("PY", "-I", "-B", "scripts/lancer_course_ideation_regard_ou_raisons_v1.py", "carbon")}, "commande d'origine"),
    ({"cwd": "/"}, "dossier courant"),
])
def test_m1_artefacts_commande(monde, capsys, modif, motif):
    r = monde["r"]
    for k, v in modif.items():
        if k == "orig_argv":
            v = tuple(r.python if x == "PY" else x for x in v)
        setattr(r, k, v)
    code, err = lancer(monde, capsys)
    assert code == 2 and motif in err
    assert not r.dossier_sorties.exists() and not monde["journal"].exists()        # avant le verrou, rien écrit


@pytest.mark.parametrize("cas,motif", [("octet", "≠ celle de son compagnon"), ("sans_compagnon", "compagnon"),
                                       ("compagnon_mal_forme", "mal formé"), ("lien", "lien symbolique"),
                                       ("ailleurs", "hors de sa place")])
def test_m1_artefacts_fichier(monde, capsys, cas, motif):
    r = monde["r"]
    f = r.fichier_lanceur
    comp = Path(str(f) + ".sha256")
    if cas == "octet":
        f.write_bytes(f.read_bytes() + b"\n")
    elif cas == "sans_compagnon":
        comp.unlink()
    elif cas == "compagnon_mal_forme":
        comp.write_text(comp.read_text() + comp.read_text())
    elif cas == "lien":
        vrai = f.parent / "vrai.py"
        f.rename(vrai)
        f.symlink_to(vrai)
    else:
        autre = monde["tmp"] / "ailleurs" / f.name
        autre.parent.mkdir()
        shutil.copyfile(f, autre)
        shutil.copyfile(comp, Path(str(autre) + ".sha256"))
        r.fichier_lanceur = autre
    code, err = lancer(monde, capsys)
    assert code == 2 and motif in err and not r.dossier_sorties.exists()


@pytest.mark.xfail(not Path(str(SCRIPT) + ".sha256").exists(), strict=False,
                   reason="compagnon .sha256 du lanceur v8 pas encore écrit : à sceller (R6) avant tout lancement ; "
                          "l'essai redevient bloquant dès que le compagnon existe")
def test_m1_compagnon_reel_du_lanceur():
    assert lc.lire_compagnon(SCRIPT) == sha(SCRIPT), "le lanceur doit être scellé (compagnon égal au fichier)"


@pytest.mark.parametrize("lignee", LIGNEES)
def test_m1_production_lit_ses_vraies_valeurs(lignee):
    r = lc.Reglages.production(lignee)
    assert r.drapeaux is sys.flags and r.fichier_lanceur == SCRIPT and r.python == "/usr/local/bin/python3"
    assert tuple(r.orig_argv) == tuple(sys.orig_argv) and r.lignee == lignee
    assert r.pieces == lc.pieces_de(lignee) and r.plafonds == lc.plafonds_de(lignee)
    assert lc.commande_exacte(r) == ("/usr/local/bin/python3", "-I", "-B",
                                     "scripts/lancer_course_ideation_organismes_discrets_v8.py", lignee)


@pytest.mark.parametrize("args,argument,motif", [(["-B"], "carbon", "-I absente"), (["-I", "-B"], "1", "un seul argument"),
                                                 (["-I", "-B"], "Carbon", "un seul argument")])
def test_m1_vrai_fichier_commande_fausse_refuse_sans_rien_ecrire(tmp_path, args, argument, motif):
    """Le vrai fichier, en processus à part, avec une commande fausse : refus avant le verrou (rien n'est créé)."""
    if not Path(lc.PYTHON_COURSE).is_file():
        pytest.skip("interpréteur de production absent")
    avant = lc.DOSSIER_SORTIES.exists()
    argv = [lc.PYTHON_COURSE, *args, f"scripts/{lc.FICHIER_LANCEUR}", argument]
    p = subprocess.run(argv, cwd=str(RACINE), capture_output=True, text=True, timeout=60,
                       env={"PATH": "/usr/bin:/bin", "HOME": str(tmp_path)})
    assert p.returncode == 2 and motif in p.stderr, p.stderr
    assert lc.DOSSIER_SORTIES.exists() == avant


# ============================================================================================ chaîne saine de bout en bout

def test_course_bout_en_bout(monde, capsys):
    r = monde["r"]
    code, sortie = jouer(monde, capsys)
    assert code == 0 and "lancée, détachée" in sortie and "GO-2026-11-18-01" in sortie and '"lignee": "carbon"' in sortie
    rs = runs(monde)
    assert len(rs) == 1 and rs[0]["lance"] and rs[0]["fin"]["code"] == 0 and rs[0]["lignee"] == "carbon"
    assert rs[0]["nom"].endswith(lc.SUFFIXE_RUN + "carbon")
    j = _journal_course(monde)
    assert [x["mode"] for x in journal(monde)] == ["mesure", "course"]
    a = j[0]["argv"]
    assert j[0]["noms_cle"] == [] and j[0]["go_id"] == "GO-2026-11-18-01" and j[0]["etiquette_externe"] == "carbon"
    assert {n for n in j[0]["noms_env"] if not n.startswith("FAUX_")} <= set(lc.NOMS_PERMIS) | {"HOME", "GO_ID",
                                                                                               "PYTHONPYCACHEPREFIX"}
    assert j[0]["sid"] != os.getsid(0) and j[0]["orig_argv"][1:3] == ["-I", "-B"]
    assert a[a.index("--nombre") + 1] == "6" and a[a.index("--graine") + 1] == "2026111808"
    assert a[a.index("--budget-total-usd") + 1] == "6.0" and a[a.index("--budget-externe-usd") + 1] == "6.5"
    assert [a[i + 1] for i, x in enumerate(a) if x == "--piece"] == [str(r.depot / r.pieces["faits"][0])]
    assert [a[i + 1] for i, x in enumerate(a) if x == "--proposeur"] == ["opus=claude-opus-5-5"]
    assert [a[i + 1] for i, x in enumerate(a) if x == "--juge"] == ["opus-juge=claude-opus-5-5"]
    assert a[a.index("--proposeur-externe") + 1] == "carbon=gemini-4-carbon"
    assert a[a.index("--juge-externe") + 1] == "carbon-juge=gemini-4-carbon"
    assert a[a.index("--commande-externe") + 1] == "bash " + str(r.depot / r.pieces["enveloppe_externe"][0])
    assert a[a.index("--modele-commande-externe") + 1] == "gemini-4-carbon" and "--commande-externe-lit-modele" in a
    assert "--seconde-passe" not in a and "--budget-passe-2-externe-usd" not in a
    assert sorted(a[i + 1] for i, x in enumerate(a) if x == "--budget") == sorted(
        f"{k}={float(v)!r}" for k, v in lc.plafonds_de("carbon").items())
    assert "--bras-rapporte-differe" not in a and "--accepter-sans-bac-a-sable" not in a
    d = rs[0]["dossier"]
    pre = json.loads((d / "manifeste-lanceur-pre-depart.json").read_text())
    texte = (d / "manifeste-lanceur-pre-depart.json").read_text()
    for interdit in ("valeur-factice-d-essai", "hote.invalid", "mandataire.invalid", "ANTHROPIC_API_KEY",
                     "CLAUDE_CODE_REMOTE", "KIMI_API_KEY"):
        assert interdit not in texte                                    # m5 : ni valeurs, ni noms exclus
    assert pre["environnement"]["noms_exclus"]["nombre"] == 10
    assert pre["lignee"] == "carbon" and pre["lignee_externe"] == _json(lc.LIGNEES_EXTERNES["carbon"])
    assert pre["plafonds"]["sommes"]["somme_claude"] == 4.2 and pre["plafonds"]["sommes"]["somme_externe"] == 5.9
    assert pre["plafonds"]["sommes"]["exposition_externe_course"] == 3.2
    assert pre["plafonds"]["sommes"]["detail_claude"]["passes"] == 1
    assert pre["plafonds"]["plafond_course_usd"] == pytest.approx(9.2) and pre["plafonds"]["pire_cas_devis_usd"] == 34.0
    assert pre["plafonds"]["reglage"] == lc.plafonds_de("carbon") and "passe_2_externe_usd" not in pre["plafonds"]
    assert pre["plafonds"]["gardes_de_taille"]["commande_externe"]["famille"] == "gemini"
    assert "passe_2_seuil_de_fiche" not in pre["plafonds"]["gardes_de_taille"]
    assert "reserve_lecteur_usd" not in pre["plafonds"] and "reserve_lecteur_usd" not in pre["garde_de_cumul"]
    assert pre["garde_de_cumul"]["borne_usd"] == 34.0 and pre["relance"].startswith("lignée carbon : 0 course")
    assert pre["lanceur"]["sha256"] == sha(r.fichier_lanceur) and pre["depot_travail"]
    dep = json.loads((d / "manifeste-lanceur-depart.json").read_text())
    assert dep["pre_depart_sha256"] == sha(d / "manifeste-lanceur-pre-depart.json")
    rel = json.loads((d / "releve-depense.json").read_text())
    assert rel["course_usd"] == pytest.approx(4.5) and rel["lisible"] and rel["fiches_produites"] is True
    assert rel["comptes_fiches"]["fiches-validees.json"] == 5
    fin = json.loads((d / "manifeste-lanceur-fin.json").read_text())
    assert fin["releve_sha256"] == sha(d / "releve-depense.json") and fin["lignee"] == "carbon"
    assert fin["bilan_de_l_organisme"]["fiches_validees_sha256"] == sha(rs[0]["sortie"] / "fiches-validees.json")
    assert "lignée carbon" in fin["bilan_de_l_organisme"]["rappel"]
    assert (d / fin["bilan_de_l_organisme"]["copie"]).is_file() and "pour_l_attestation" not in fin
    for f in list(d.glob("*.json")) + list((d / "copies").glob("*.json")):
        h, nom = Path(str(f) + ".sha256").read_text().split()
        assert nom == f.name and h == sha(f)
    assert (d / "copies" / "sortie--fiches-validees.json").read_bytes() == (rs[0]["sortie"] / "fiches-validees.json").read_bytes()
    assert (d / "copies" / "sortie--noyau--temoins-servis.json").is_file()
    for ajoutee in ("manifeste-depart.json", "lecture.json", "classement.json", "lecture-course.json"):
        assert (d / "copies" / f"sortie--{ajoutee}").is_file(), ajoutee
    assert "carbon-juge" in (d / "copies" / "sortie--lecture-course.json").read_text()
    assert (d / "copies" / "superviseur--code.json").is_file() and (d / "copies" / "superviseur--pid-superviseur.json").is_file()
    code, err = lancer(monde, capsys)
    assert code == 2 and "fiches produites" in err and "jamais rejouée" in err and "lignée carbon verrouillée" in err
    assert not str(rs[0]["sortie"]).startswith(str(monde["depot"]))


@pytest.mark.parametrize("lignee", AUTRES)
def test_course_bout_en_bout_chaque_lignee(monde, capsys, lignee):
    """Les deux autres lignées : même chaîne, pièces, plafonds, étiquettes, famille de garde et nom de run de la lignée."""
    m = avec_lignee(monde, lignee)
    ext = lc.LIGNEES_EXTERNES[lignee]
    code, sortie = jouer(m, capsys)
    assert code == 0 and f'"lignee": "{lignee}"' in sortie
    rs = runs(m)
    assert len(rs) == 1 and rs[0]["lignee"] == lignee and rs[0]["nom"].endswith(lc.SUFFIXE_RUN + lignee)
    a = _journal_course(m)[0]["argv"]
    assert a[a.index("--proposeur-externe") + 1] == f"{lignee}={ext['modele']}"
    assert a[a.index("--juge-externe") + 1] == f"{lignee}-juge={ext['modele']}"
    assert a[a.index("--modele-commande-externe") + 1] == ext["modele"] and "--commande-externe-lit-modele" in a
    assert a[a.index("--commande-externe") + 1] == "bash " + str(m["r"].depot / ext["enveloppe"][0])
    assert "--seconde-passe" not in a
    d = rs[0]["dossier"]
    pre = json.loads((d / "manifeste-lanceur-pre-depart.json").read_text())
    assert pre["lignee"] == lignee and pre["lignee_externe"] == _json(ext) and pre["plafonds"]["reglage"] == lc.plafonds_de(lignee)
    assert pre["plafonds"]["gardes_de_taille"]["commande_externe"]["famille"] == ext["famille"]
    assert pre["plafonds"]["gardes_de_taille"]["commande_externe"]["modele"] == ext["modele"]
    assert set(pre["pieces"]) == set(lc.pieces_de(lignee)) and pre["pieces"]["enveloppe_externe"]["chemin"] == ext["enveloppe"][0]
    assert pre["plafonds"]["sommes"]["somme_externe"] == 5.9 and pre["garde_de_cumul"]["borne_usd"] == 34.0
    fin = json.loads((d / "manifeste-lanceur-fin.json").read_text())
    assert fin["lignee"] == lignee and f"lignée {lignee}" in fin["bilan_de_l_organisme"]["rappel"]
    assert f"{lignee}-juge" in (d / "copies" / "sortie--lecture-course.json").read_text()
    assert lc.releve_run(rs[0])["course_usd"] == pytest.approx(4.5)


def test_aucun_bras_dans_le_lanceur():
    texte = SCRIPT.read_text()
    for absent in ("def executer_bras", "def commande_bras", "def garder_bras", "lire_attestation("):
        assert absent not in texte
    assert "--bras-rapporte-differe" in lc.DRAPEAUX_INTERDITS


# ============================================================================================ B1, m1 : preuves dans le dépôt

def test_b1_dossier_hors_depot_perdu_apres_cloture(monde, capsys):
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", "0.275477"
    assert jouer(monde, capsys)[0] == 0
    avant = lc.releve_run(runs(monde)[0])
    shutil.rmtree(monde["r"].dossier_sorties)                           # le conteneur a été remplacé
    apres = lc.releve_run(runs(monde)[0])
    assert apres["course_usd"] == pytest.approx(0.275477) and apres["lisible"] and apres["fiches_produites"] is False
    assert apres["course_usd"] == avant["course_usd"]
    assert lc.relance_permise(runs(monde), "carbon")[0]
    assert (runs(monde)[0]["dossier"] / "copies" / "controle--tentative-1.json").is_file()


def test_m1_perte_partielle_de_la_sortie_sans_effet(monde, capsys):
    assert jouer(monde, capsys)[0] == 0
    shutil.rmtree(runs(monde)[0]["sortie"])                             # la sortie disparaît seule, après la clôture
    rel = lc.releve_run(runs(monde)[0])
    assert rel["fiches_produites"] is True and rel["course_usd"] == pytest.approx(4.5)
    assert not lc.relance_permise(runs(monde), "carbon")[0]


@pytest.mark.parametrize("cas", ["sceau_faux", "absent", "autre_empreinte"])
def test_b1_releve_altere_compte_le_plafond(monde, capsys, cas):
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", "0.3"
    assert jouer(monde, capsys)[0] == 0
    p = runs(monde)[0]["dossier"] / "releve-depense.json"
    if cas == "sceau_faux":
        p.write_text(p.read_text().replace("0.3", "0.0"))
    elif cas == "absent":
        p.unlink()
        Path(str(p) + ".sha256").unlink()
    else:
        t = p.read_text().replace("0.3", "0.0")
        p.unlink()
        Path(str(p) + ".sha256").unlink()
        sceller(p, t)                                                    # resceller ne suffit pas : la fin porte l'empreinte
    rel = lc.releve_run(runs(monde)[0])
    assert rel["course_usd"] == lc.PLAFOND_COURSE_USD and not rel["lisible"]
    ok, motif = lc.relance_permise(runs(monde), "carbon")
    assert not ok


def test_copier_scelle_idempotent(tmp_path):
    s = tmp_path / "s.json"
    s.write_text("{}")
    d = tmp_path / "c" / "d.json"
    assert not lc.copier_scelle(s, d).get("deja_la")
    assert lc.copier_scelle(s, d)["deja_la"]
    s.write_text("{\"x\": 1}")
    with pytest.raises(lc.Refus, match="différente de sa source"):
        lc.copier_scelle(s, d)


# ============================================================================================ M2 : après le détachement

def test_m2_aucune_commande_git_apres_le_detachement(monde, capsys, monkeypatch):
    etat = {"detache": False, "git_apres": 0}
    vrai_git, vrai_detache = lc._git, lc.lancer_detache

    def git_garde(*a, **k):
        if etat["detache"]:
            etat["git_apres"] += 1
            raise lc.Refus("git appelé après le détachement")
        return vrai_git(*a, **k)

    def detache(*a, **k):
        out = vrai_detache(*a, **k)
        etat["detache"] = True
        return out
    monkeypatch.setattr(lc, "_git", git_garde)
    monkeypatch.setattr(lc, "lancer_detache", detache)
    code, sortie = lancer(monde, capsys)
    assert code == 0 and "lancée, détachée" in sortie and etat["git_apres"] == 0
    attendre(monde)


def test_m2_source_aucun_appel_apres_le_detachement():
    texte = SCRIPT.read_text()
    corps = texte.split("def executer(")[1].split("\ndef principal(")[0]
    apres = corps.split("sup = lancer_detache(")[1]
    for interdit in ("_git(", "_depot_git(", "sha256_fichier(", "subprocess", "verifier_", "mesurer_", "construire_"):
        assert interdit not in apres, interdit
    assert corps.index("depot_git = _depot_git(r)") < corps.index("sup = lancer_detache(")


def test_m2_manifeste_de_depart_non_ecrit(monde, capsys, monkeypatch):
    monde["env"]["FAUX_DORT"] = "2"
    vrai = lc.ecrire_scelle

    def panne(chemin, contenu):
        if chemin.name == "manifeste-lanceur-depart.json":
            raise OSError("disque plein simulé")
        return vrai(chemin, contenu)
    monkeypatch.setattr(lc, "ecrire_scelle", panne)
    code, err = lancer(monde, capsys)
    assert code == 5 and "NON écrit" in err and "kill -TERM" in err and "pid_superviseur" in err
    assert err.index("kill -INT") < err.index("kill -TERM")                 # C1 : INT d'abord
    monkeypatch.undo()
    rs = runs(monde)
    assert len(rs) == 1 and rs[0]["depart"] is None and rs[0]["superviseur"]["retrouve"] and rs[0]["lance"]
    code, sortie = lancer(monde, capsys)
    assert code == 3 and "en marche" in sortie                          # retrouvée par le PID scellé du superviseur
    attendre(monde)
    code, sortie = lancer(monde, capsys)
    assert code == 0 and "clôture" in sortie
    assert lc.releve_run(runs(monde)[0])["course_usd"] == pytest.approx(4.5)


def test_m2_pre_depart_sans_superviseur_rien_lance(monde, capsys, monkeypatch):
    def panne(*a, **k):
        raise KeyboardInterrupt("signal avant le détachement")
    monkeypatch.setattr(lc, "lancer_detache", panne)
    code, err = lancer(monde, capsys)
    assert code == 2 and "manifeste de refus scellé" in err
    monkeypatch.undo()
    rs = runs(monde)
    assert rs[0]["refus"] and not rs[0]["lance"] and lc.releve_run(rs[0])["course_usd"] == 0.0
    assert rs[0]["refus"]["lignee"] == "carbon"
    assert jouer(monde, capsys)[0] == 0                                  # rien n'était parti : la course part


def test_m2_detachement_incertain_pas_de_refus(monde, capsys, monkeypatch):
    def panne(r, argv, env, dossier, pfx):
        dossier.mkdir()
        (dossier / "superviseur.stdout.txt").write_text("")
        raise OSError("panne après l'ouverture des journaux")
    monkeypatch.setattr(lc, "lancer_detache", panne)
    code, err = lancer(monde, capsys)
    assert code == 2 and "état incertain" in err
    monkeypatch.undo()
    rs = runs(monde)
    assert rs[0]["refus"] is None and rs[0]["superviseur"]["inconnu"]
    code, err = lancer(monde, capsys)
    assert code == 2 and "sans PID scellé" in err and len(journal(monde)) == 1      # mesure seule, aucune course
    assert lc.garde_cumul(rs, 34.0)["depense_relevee_usd"] == pytest.approx(9.2)      # plafond compté
    with pytest.raises(lc.Refus, match="garde de cumul"):
        lc.garde_cumul(rs, 18.3)                                          # 9,2 comptés + 9,2 de la suivante > 18,3


# ============================================================================================ détaché, PID, orphelin, verrou

def test_en_marche_rien_ne_part(monde, capsys):
    monde["env"]["FAUX_DORT"] = "3"
    assert lancer(monde, capsys)[0] == 0
    code, sortie = lancer(monde, capsys)
    assert code == 3 and "en marche" in sortie and "kill -TERM" in sortie
    assert sortie.index("kill -INT") < sortie.index("kill -TERM")           # C1 : INT d'abord
    attendre(monde)
    assert [j["mode"] for j in journal(monde)] == ["mesure", "course"]
    code, sortie = lancer(monde, capsys)
    assert code == 0 and "clôture" in sortie


def test_en_marche_sur_une_lignee_rien_ne_part_sur_une_autre(monde, capsys):
    """Le verrou et le compte rendu « en marche » valent pour toutes les lignées : une seule course à la fois."""
    monde["env"]["FAUX_DORT"] = "3"
    assert lancer(monde, capsys)[0] == 0
    code, sortie = lancer(avec_lignee(monde, "astra"), capsys)
    assert code == 3 and "en marche" in sortie and "carbon" in sortie
    attendre(monde)
    assert len(_journal_course(monde)) == 1
    code, sortie = lancer(avec_lignee(monde, "astra"), capsys)
    assert code == 0 and "clôture" in sortie                              # la clôture ne regarde pas la lignée


def test_mort_sans_fin_propre(monde, capsys):
    monde["env"]["FAUX_DORT"] = "30"
    assert lancer(monde, capsys)[0] == 0
    sup = runs(monde)[0]["superviseur"]
    p = _tuer_superviseur(sup)
    os.kill(p["pid_orchestrateur"], signal.SIGKILL)
    _attendre_mort(p["pid_orchestrateur"])
    code, sortie = lancer(monde, capsys)
    assert code == 0 and "mort sans fin propre" in sortie
    rel = lc.releve_run(runs(monde)[0])
    assert rel["course_usd"] == lc.PLAFOND_COURSE_USD and not rel["lisible"]
    code, err = lancer(monde, capsys)
    assert code == 2 and "verrouillée" in err


def test_arret_par_pid_relaye(monde, capsys):
    monde["env"]["FAUX_DORT"] = "30"
    assert lancer(monde, capsys)[0] == 0
    sup = runs(monde)[0]["superviseur"]
    pidf = Path(sup["dossier"]) / "pid-orchestrateur.json"
    for _ in range(100):
        if pidf.exists():
            break
        time.sleep(0.05)
    os.kill(sup["pid"], signal.SIGTERM)
    os.waitpid(sup["pid"], 0)
    assert json.loads((Path(sup["dossier"]) / "code.json").read_text())["code"] == -signal.SIGTERM
    sp = json.loads((Path(sup["dossier"]) / "pid-superviseur.json").read_text())
    assert sp["pid_superviseur"] == sup["pid"] and sp["debut_proc"] == sup["debut_proc"]


def test_orchestrateur_orphelin(monde, capsys):
    monde["env"]["FAUX_DORT"] = "30"
    assert lancer(monde, capsys)[0] == 0
    p = _tuer_superviseur(runs(monde)[0]["superviseur"])
    code, sortie = lancer(monde, capsys)
    assert code == 4 and "ORCHESTRATEUR ENCORE VIVANT" in sortie and f"kill -TERM {p['pid_orchestrateur']}" in sortie
    code, sortie = lancer(monde, capsys)
    assert code == 4 and "orphelin" in sortie
    os.kill(p["pid_orchestrateur"], signal.SIGKILL)
    _attendre_mort(p["pid_orchestrateur"])
    code, err = lancer(monde, capsys)
    assert code == 2 and "sans fin propre" in err


def test_zombie_tenu_pour_mort():
    p = subprocess.Popen(["sleep", "0.3"])
    debut = lc.debut_processus(p.pid)
    assert lc.superviseur_vivant({"pid": p.pid, "debut_proc": debut})
    for _ in range(100):
        time.sleep(0.05)
        try:
            etat = open(f"/proc/{p.pid}/stat").read().rsplit(")", 1)[-1].split()[0]
        except OSError:
            etat = None
        if etat == "Z":
            break
    assert etat == "Z"
    assert not lc.superviseur_vivant({"pid": p.pid, "debut_proc": debut})
    p.wait()


def test_superviseur_vivant_pid_reutilise_et_inconnu():
    assert lc.superviseur_vivant({"pid": os.getpid(), "debut_proc": lc.debut_processus(os.getpid())})
    assert not lc.superviseur_vivant({"pid": os.getpid(), "debut_proc": "0"})
    assert not lc.superviseur_vivant({"inconnu": True, "dossier": "/x"})


def test_verrou_deux_invocations(monde, capsys):
    import fcntl
    monde["r"].dossier_sorties.mkdir(parents=True)
    fd = os.open(monde["r"].dossier_sorties / lc.NOM_VERROU, os.O_CREAT | os.O_RDWR)
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    try:
        code, err = lancer(monde, capsys)
        assert code == 2 and "verrou" in err and not monde["journal"].exists()
        code, err = lancer(avec_lignee(monde, "argon"), capsys)             # verrou commun aux lignées
        assert code == 2 and "verrou" in err and not monde["journal"].exists()
    finally:
        os.close(fd)
    assert lancer(monde, capsys)[0] == 0
    attendre(monde)


def test_verrou_non_herite_par_le_superviseur(monde, capsys):
    import fcntl
    monde["env"]["FAUX_DORT"] = "3"
    assert lancer(monde, capsys)[0] == 0
    fd = os.open(monde["r"].dossier_sorties / lc.NOM_VERROU, os.O_RDWR)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    finally:
        os.close(fd)
    attendre(monde)


def test_compte_rendu_apres_echeance_du_go(monde, capsys):
    monde["env"]["FAUX_DORT"] = "3"
    assert lancer(monde, capsys)[0] == 0
    monde["r"].aujourd_hui = dt.date(2027, 1, 15)
    code, sortie = lancer(monde, capsys)
    assert code == 3 and "en marche" in sortie
    attendre(monde)
    code, sortie = lancer(monde, capsys)
    assert code == 0 and "clôture" in sortie


# ============================================================================================ relance unique par lignée, cumul

def test_relance_unique_apres_defaut_au_controle(monde, capsys):
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", "0.275477"
    assert jouer(monde, capsys)[0] == 0
    assert lc.relance_permise(runs(monde), "carbon")[0]
    assert jouer(monde, capsys)[0] == 0                                 # la seule relance
    code, err = lancer(monde, capsys)
    assert code == 2 and "2 courses déjà parties pour la lignée carbon" in err and "une seule relance par lignée" in err
    pre = json.loads((runs(monde)[1]["dossier"] / "manifeste-lanceur-pre-depart.json").read_text())
    assert pre["garde_de_cumul"]["depense_relevee_usd"] == pytest.approx(0.275477)
    assert pre["relance"].startswith("lignée carbon : 1 course")


@pytest.mark.parametrize("cout,permise", [("2.1", True), ("2.100001", False), ("5.0", False)])
def test_relance_bornee_par_le_plafond_de_relance(monde, capsys, cout, permise):
    """Une course arrêtée au contrôle, sans fiche, lisible, n'est rejouée que si son relevé est d'au plus 2,1 USD."""
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", cout
    assert jouer(monde, capsys)[0] == 0
    ok, motif = lc.relance_permise(runs(monde), "carbon")
    assert ok is permise, motif
    if not permise:
        assert "plafond de relance" in motif and str(lc.PLAFOND_RELANCE_USD) in motif
        code, err = lancer(monde, capsys)
        assert code == 2 and "plafond de relance" in err and len(runs(monde)) == 1


def test_plafond_de_relance_constante():
    assert lc.PLAFOND_RELANCE_USD == 2.1 and 3 * (lc.PLAFOND_COURSE_USD + lc.PLAFOND_RELANCE_USD) <= lc.BORNE_LIGNE_USD + 0.1

def test_relance_puis_succes(monde, capsys):
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", "0.3"
    assert jouer(monde, capsys)[0] == 0
    del monde["env"]["FAUX_CONTROLE_SEUL"]
    assert jouer(monde, capsys)[0] == 0
    assert lc.releve_run(runs(monde)[1])["fiches_produites"] is True


def test_deux_courses_au_plus_meme_sans_depense(monde, capsys):
    monde["env"]["FAUX_CODE"], monde["env"]["FAUX_RIEN"] = "2", "1"
    assert jouer(monde, capsys)[0] == 0
    assert jouer(monde, capsys)[0] == 0
    code, err = lancer(monde, capsys)
    assert code == 2 and "2 courses" in err


def test_pas_de_relance_apres_des_fiches(monde, capsys):
    monde["env"]["FAUX_CODE"] = "2"
    assert jouer(monde, capsys)[0] == 0
    monde["env"]["FAUX_CODE"] = "0"
    code, err = lancer(monde, capsys)
    assert code == 2 and "fiches produites" in err


def test_relance_refusee_si_depense_illisible(monde, capsys):
    monde["env"]["FAUX_CONTROLE_SEUL"] = "interrompu"
    assert jouer(monde, capsys)[0] == 0
    rel = lc.releve_run(runs(monde)[0])
    assert rel["course_usd"] == lc.PLAFOND_COURSE_USD and not rel["lisible"]
    code, err = lancer(monde, capsys)
    assert code == 2 and ("dépense illisible" in err or "non prouvée" in err)


def test_relance_refusee_sans_fin_propre(monde, capsys):
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", "0.1"
    assert jouer(monde, capsys)[0] == 0
    run = runs(monde)[0]
    ok, motif = lc.relance_permise([dict(run, fin=dict(run["fin"], code=None))], "carbon")
    assert not ok and "sans fin propre" in motif
    assert lc.relance_permise([dict(run, fin=dict(run["fin"], code=None))], "astra")[0]     # l'autre lignée reste libre


def test_relance_par_lignee_une_course_finie_sur_carbon_ne_bloque_pas_astra(monde, capsys):
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", "0.3"
    assert jouer(monde, capsys)[0] == 0                                 # carbon : finie proprement, sans fiche
    rs = runs(monde)
    assert lc.relance_permise(rs, "carbon")[1].startswith("lignée carbon : 1 course")
    assert lc.relance_permise(rs, "astra")[1].startswith("lignée astra : 0 course")
    assert lc.relance_permise(rs, "argon")[1].startswith("lignée argon : 0 course")
    assert jouer(avec_lignee(monde, "astra"), capsys)[0] == 0           # astra part : première course de sa lignée
    assert jouer(monde, capsys)[0] == 0                                 # carbon : sa seule relance
    code, err = lancer(monde, capsys)
    assert code == 2 and "2 courses déjà parties pour la lignée carbon" in err
    rs = runs(monde)
    assert [x["lignee"] for x in rs] == ["carbon", "astra", "carbon"]
    assert lc.relance_permise(rs, "astra")[1].startswith("lignée astra : 1 course")
    assert lc.relance_permise(rs, "argon")[1].startswith("lignée argon : 0 course")
    pre = json.loads((rs[2]["dossier"] / "manifeste-lanceur-pre-depart.json").read_text())
    assert pre["garde_de_cumul"]["depense_relevee_usd"] == pytest.approx(0.6)     # le cumul, lui, somme les lignées


def test_deux_courses_sur_carbon_bloquent_carbon_seulement(monde, capsys):
    monde["env"]["FAUX_CODE"], monde["env"]["FAUX_RIEN"] = "2", "1"
    assert jouer(monde, capsys)[0] == 0
    assert jouer(monde, capsys)[0] == 0
    code, err = lancer(monde, capsys)
    assert code == 2 and "2 courses déjà parties pour la lignée carbon" in err
    for lignee in AUTRES:
        assert jouer(avec_lignee(monde, lignee), capsys)[0] == 0, lignee
    assert [x["lignee"] for x in runs(monde)] == ["carbon", "carbon", "astra", "argon"]


def test_fiches_sur_une_lignee_ne_bloquent_pas_l_autre(monde, capsys):
    assert jouer(monde, capsys)[0] == 0                                 # carbon : fiches produites, jamais rejouée
    code, err = lancer(monde, capsys)
    assert code == 2 and "fiches produites" in err and "lignée carbon verrouillée" in err
    assert jouer(avec_lignee(monde, "argon"), capsys)[0] == 0
    code, err = lancer(avec_lignee(monde, "argon"), capsys)
    assert code == 2 and "lignée argon verrouillée" in err


@pytest.mark.parametrize("plafond,cout,attendu", [("34 USD", "24.8", 0), ("34 USD", "24.9", 2), ("40 USD", "24.9", 2),
                                                  ("34 USD", "24.79", 0), ("100 USD", "24.8", 0),
                                                  ("100 USD", "24.9", 2)])
def test_garde_de_cumul(monde, capsys, plafond, cout, attendu):
    """Une course de carbon arrêtée au contrôle à `cout` (au-dessus du plafond de relance : carbon n'est plus rejouée) ;
    la lignée astra, jamais partie, est refusée par la garde de cumul dès que `cout` + 9,2 passe la borne de 34 USD."""
    reecrire_go(monde["r"], GO_LIGNE.replace("| 34 USD |", f"| {plafond} |"))
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", cout
    assert jouer(monde, capsys)[0] == 0
    del monde["env"]["FAUX_CONTROLE_SEUL"]
    assert "plafond de relance" in lc.relance_permise(runs(monde), "carbon")[1]
    code, err = lancer(avec_lignee(monde, "astra"), capsys)
    assert code == attendu, err
    if attendu:
        assert "garde de cumul" in err and "réserve du lecteur" not in err
    else:
        attendre(monde)


@pytest.mark.parametrize("cout,attendu", [("12.5", 2), ("12.4", 0)])
def test_garde_de_cumul_somme_les_lignees(monde, capsys, cout, attendu):
    """Deux lignées jouées (dépense lisible), la troisième jamais partie : la garde de cumul la refuse quand la somme des
    trois lignées passerait la borne de la ligne (12,5 + 12,5 + 9,2 > 34), et la laisse partir juste en dessous."""
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", cout
    assert jouer(monde, capsys)[0] == 0
    assert jouer(avec_lignee(monde, "astra"), capsys)[0] == 0
    rs = runs(monde)
    assert lc.relance_permise(rs, "argon") == (True, "lignée argon : 0 course(s) précédente(s), finies proprement, sans fiche, "
                                                     "dépense lisible")
    code, err = lancer(avec_lignee(monde, "argon"), capsys)
    assert code == attendu, err
    if attendu:
        assert "garde de cumul" in err and f"dépense relevée {2 * float(cout):.4f}" in err
        assert len(_journal_course(monde)) == 2
    else:
        attendre(monde)
        pre = json.loads((runs(monde)[2]["dossier"] / "manifeste-lanceur-pre-depart.json").read_text())
        assert pre["garde_de_cumul"]["depense_relevee_usd"] == pytest.approx(2 * float(cout))


def test_garde_de_cumul_unitaire_a_travers_les_lignees():
    """Courses closes à dépense illisible : chacune compte le plafond d'une course (9,2), quelle que soit sa lignée ; la
    borne est celle de la ligne (34) : deux passent (18,4 + 9,2), trois non (27,6 + 9,2)."""
    def illisible(lignee):
        return {"nom": f"run-{lignee}", "lignee": lignee, "lance": True, "fin": None}
    deux = [illisible("carbon"), illisible("astra")]
    assert lc.garde_cumul(deux, 34.0)["depense_relevee_usd"] == pytest.approx(18.4)
    with pytest.raises(lc.Refus, match="garde de cumul"):
        lc.garde_cumul(deux + [illisible("argon")], 34.0)
    with pytest.raises(lc.Refus, match="garde de cumul"):
        lc.garde_cumul([illisible("carbon"), illisible("carbon")] + [illisible("astra")], 100.0)
    assert lc.garde_cumul([illisible("argon")], 18.4)["borne_usd"] == 18.4
    with pytest.raises(lc.Refus, match="garde de cumul"):
        lc.garde_cumul([illisible("argon")], 18.3)


def test_cumul_constantes():
    assert lc.PLAFOND_COURSE_USD == pytest.approx(9.2) and not hasattr(lc, "RESERVE_LECTEUR_USD")
    defaut_au_controle = 2 * lc.CONTROLE_CLAUDE_DEFAUT_USD + lc.CONTROLE_EXTERNE_USD
    assert defaut_au_controle == pytest.approx(2.1)
    assert 3 * (lc.PLAFOND_COURSE_USD + defaut_au_controle) == pytest.approx(33.9)
    assert 3 * (lc.PLAFOND_COURSE_USD + defaut_au_controle) <= lc.PIRE_CAS_DEVIS_USD
    assert lc.BORNE_LIGNE_USD == lc.PIRE_CAS_DEVIS_USD == 34.0
    c = lc.garde_cumul([], 34.0)
    assert c["depense_relevee_usd"] == 0.0 and c["borne_usd"] == 34.0 and set(c) == {
        "depense_relevee_usd", "plafond_course_usd", "borne_usd", "par_run"}
    assert lc.garde_cumul([], 100.0)["borne_usd"] == 34.0 and lc.garde_cumul([], 20.0)["borne_usd"] == 20.0
    with pytest.raises(lc.Refus, match="garde de cumul"):
        lc.garde_cumul([], 9.1)


@pytest.mark.parametrize("valeur", [-1, "x", True, None, float("inf"), float("nan")])
def test_cout_mal_type_compte_le_plafond(tmp_path, valeur):
    s = tmp_path / "sortie"
    s.mkdir()
    sceller(s / "manifeste-fin.json", json.dumps({"reglages": {"journal": {"cout_total_usd": valeur, "cout_externe_usd": 1}}},
                                                 allow_nan=True))
    assert lc.depense_course(s, True)[0] == lc.PLAFOND_COURSE_USD


def test_depense_course_cas(tmp_path):
    s = tmp_path / "sortie"
    c = tmp_path / "sortie-controle"
    assert lc.depense_course(s, False)[:2] == (lc.PLAFOND_COURSE_USD, False)
    assert lc.depense_course(s, True)[:2] == (0.0, True)
    (c / "tentative-1").mkdir(parents=True)
    sceller(c / "tentative-1.json", json.dumps({"reglages": {"cout_claude_usd": 0.01, "cout_externe_usd": 0.4}}))
    assert lc.depense_course(s, True)[0] == pytest.approx(0.41)
    (c / "tentative-1-externe-carbon").mkdir()
    assert lc.depense_course(s, True)[0] == pytest.approx(0.41)
    (c / "tentative-2-externe-astra").mkdir()
    assert lc.depense_course(s, True)[:2] == (lc.PLAFOND_COURSE_USD, False)


@pytest.mark.parametrize("contenus,attendu", [((None, None, None), False), (([], [], []), False), (([1], [], []), True),
                                              (([], [{"x": 1}], []), True), (("pas une liste", [], []), None)])
def test_fiches_produites(tmp_path, contenus, attendu):
    s = tmp_path / "sortie"
    if contenus[0] is not None:
        for nom, c in zip(("fiches-validees.json", "fiches-refusees.json", "fiches-en-quarantaine.json"), contenus):
            sceller(s / nom, json.dumps(c))
    assert lc.fiches_produites(s) is attendu


# ============================================================================================ ligne de GO

def test_go_sain_trouve_par_son_contenu(monde):
    g = lc.verifier_go(monde["r"].registre_go, dt.date(2026, 11, 18))
    assert g["id"] == "GO-2026-11-18-01" and g["plafond_usd"] == 34.0


def test_go_apostrophe_typographique(monde):
    reecrire_go(monde["r"], GO_LIGNE.replace("d'idéation", "d’idéation"))
    assert lc.verifier_go(monde["r"].registre_go, dt.date(2026, 11, 18))["id"] == "GO-2026-11-18-01"


@pytest.mark.parametrize("ligne,motif", [
    (GO_LIGNE.replace("trois lignées", "lignées"), "0 ligne"),
    (GO_LIGNE.replace("organismes discrets", "organismes"), "0 ligne"),
    (GO_LIGNE.replace("Organisme d'idéation", "Organisme"), "0 ligne"),
    (GO_LIGNE + "\n" + GO_LIGNE.replace("GO-2026-11-18-01", "GO-2026-11-18-02"), "2 ligne"),
    (GO_LIGNE.replace("| calcul |", "| publication |"), "type"),
    (GO_LIGNE.replace("| Lazar |", "| Claude |"), "Lazar exigé"),
    (GO_LIGNE.replace("| 34 USD |", "| 33.9 USD |"), "sous le pire cas"),
    (GO_LIGNE.replace("| 34 USD |", "| 17 USD |"), "sous le pire cas"),
    (GO_LIGNE.replace("| 34 USD |", "| trente-quatre |"), "illisible"),
    (GO_LIGNE.replace("| 2026-12-31 |", "| 2026-11-17 |"), "période"),
    (GO_LIGNE + "\n| GO-2026-11-18-03 | 2026-11-18 | révocation | révoque GO-2026-11-18-01 | — | — | Lazar | x |", "révoqué"),
    (GO_LIGNE + "\n| GO-2026-11-18-03 | 2026-11-18 | Revocation | révoque GO-2026-11-18-01 | — | — | Lazar | x |", "révoqué"),
    (GO_LIGNE + "\n| GO-2026-11-18-03 | 2026-11-18 | révocation | GO-2026-11-18-01 | — | — | Lazar | x | y |", "mal formée"),
    (GO_LIGNE + "\n| GO-2026-11-18-01 | 2026-11-18 | calcul | autre chose | 5 USD | 2026-11-20 | Lazar | x |", "lignes principales"),
])
def test_go_artefacts(monde, capsys, ligne, motif):
    reecrire_go(monde["r"], ligne)
    code, err = lancer(monde, capsys)
    assert code == 2 and motif in err and not monde["journal"].exists()


def test_go_registre_reel_avant_comme_apres_l_inscription():
    """Le registre réel : soit la ligne n'est pas encore inscrite (refus « 0 ligne », sens fermé), soit elle l'est, seule,
    au pire cas du devis au moins. Tient avant comme après l'inscription ; les lignes des courses « conception propre »
    (GO-2026-11-13-06), « Regard ou raisons » (GO-2026-11-14-01) et du collisionneur sur les organismes discrets
    (GO-2026-11-17-06, sans « trois lignées ») ne sont jamais prises pour celle-ci."""
    registre = RACINE / "registres" / "go.md"
    try:
        g = lc.verifier_go(registre, dt.date(2026, 11, 18))
    except lc.Refus as e:
        assert "0 ligne(s) principale(s)" in str(e), str(e)
        return
    assert g["plafond_usd"] >= lc.PIRE_CAS_DEVIS_USD and g["par"] == "Lazar"
    assert g["id"] not in ("GO-2026-11-13-06", "GO-2026-11-14-01", "GO-2026-11-17-06")


# ============================================================================================ environnement

def test_environnement_permis():
    class Env(dict):
        def __getitem__(self, n):
            if n not in lc.NOMS_PERMIS:
                raise AssertionError(f"valeur de {n} lue")
            return dict.__getitem__(self, n)
    env, noms = lc.environnement_permis(Env(PATH="/bin", ANTHROPIC_API_KEY="v", GH_TOKEN="v", CLAUDE_CODE_REMOTE="t",
                                            ANTHROPIC_BASE_URL="u", CCR_X="1", HOME="/root", LANG="C", KIMI_API_KEY="k"),
                                        "GO-X", Path("/p/pycache"), Path("/h"))
    assert env == {"PATH": "/bin", "LANG": "C", "GO_ID": "GO-X", "HOME": "/h", "PYTHONPYCACHEPREFIX": "/p/pycache"}
    assert noms["noms_exclus"]["nombre"] == 7 and "CLAUDE_CODE_REMOTE" not in json.dumps(noms)


def test_environnement_permis_prefixe_d_essai():
    assert all(lc.Reglages.production(l).prefixe_essais is None for l in LIGNEES)
    with pytest.raises(lc.Refus, match="préfixe d'essai interdit"):
        lc.environnement_permis({"PATH": "/bin"}, "GO-X", prefixe_essais="CLAUDE_")


def test_environnement_permis_artefact_nom_interdit(monkeypatch):
    monkeypatch.setattr(lc, "NOMS_PERMIS", lc.NOMS_PERMIS + ("CLAUDE_CODE_REMOTE",))
    with pytest.raises(lc.Refus, match="nom permis interdit"):
        lc.environnement_permis({"PATH": "/bin"}, "GO-X")


# ============================================================================================ gardes reprises

@pytest.mark.parametrize("lignee", LIGNEES)
def test_drapeaux_sain_commande_production(lignee):
    lc.garde_drapeaux(lc.commande_course(lc.Reglages.production(lignee), Path("/x/s"), Path("/x/l"), "h", PFX))


@pytest.mark.parametrize("drapeau", ["--accepter-sans-bac-a-sable", "--tolerer", "--bras-rapporte-differe",
                                     "--attestation-lecture-humaine=x", "--taille-max-consigne-externe=9"])
def test_drapeaux_artefact(monde, capsys, drapeau):
    monde["r"].arguments_en_plus = (drapeau,)
    code, err = lancer(monde, capsys)
    assert code == 2 and "interdit" in err and not monde["journal"].exists()


@pytest.mark.parametrize("lignee", LIGNEES)
def test_sommes_sain_production(lignee):
    s = lc.garde_sommes(lc.commande_course(lc.Reglages.production(lignee), Path("/x/s"), Path("/x/l"), "h", PFX))
    assert (s["somme_claude"], s["somme_externe"], s["exposition_externe_course"]) == (4.2, 5.9, 3.2)
    assert (s["total_claude"], s["total_externe"]) == (6.0, 6.5) and s["detail_claude"]["passes"] == 1
    assert s["detail_claude"]["modeles"] == ["claude-opus-5-5"]


@pytest.mark.parametrize("cle,valeur,motif", [("juge_ideation|gemini-4-carbon", 3.1, "pas sous le total externe"),
                                              ("proposeur_ideation|claude-opus-5-5", 4.0, "Claude"),
                                              ("proposeur_ideation|gemini-4-carbon", 1.6, "exposition")])
def test_sommes_artefacts(cle, valeur, motif):
    r = lc.Reglages.production("carbon")
    r.plafonds = dict(lc.plafonds_de("carbon"), **{cle: valeur})
    with pytest.raises(lc.Refus, match=motif):
        lc.garde_sommes(lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX))


@pytest.mark.parametrize("ajout", [("--seconde-passe",), ("--budget-passe-2-externe-usd", "1.9"),
                                   ("--budget-passe-2-externe-usd=1.9",)])
def test_une_seule_passe_glissee_refusee(monde, capsys, ajout):
    """`--seconde-passe` ou le budget de passe 2, glissés dans la commande : refus de la garde des sommes, avant toute
    écriture et tout sous-processus."""
    monde["r"].arguments_en_plus = ajout
    code, err = lancer(monde, capsys)
    assert code == 2 and "une seule passe" in err and "interdits" in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


def test_sommes_plafonds_une_seule_passe_unitaire():
    base = lc.commande_course(lc.Reglages.production("astra"), Path("/x/s"), Path("/x/l"), "h", PFX)
    assert lc.sommes_plafonds(base)["detail_claude"]["passes"] == 1
    with pytest.raises(lc.Refus, match="une seule passe"):
        lc.sommes_plafonds(base + ["--seconde-passe"])
    with pytest.raises(lc.Refus, match="une seule passe"):
        lc.sommes_plafonds(base + ["--budget-passe-2-externe-usd", "0.5"])


@pytest.mark.parametrize("etat,motif", [("inactif", "inactif"), ("sans_proc", "/proc neuf"), ("illisible", "illisible"),
                                         ("erreur", "illisible"),
                                         ("eteint_proc_neuf", "bac à sable de l'orchestrateur inactif")])
def test_bac_a_sable_artefact(monde, capsys, etat, motif):
    monde["env"]["FAUX_BAC"] = etat
    code, err = lancer(monde, capsys)
    assert code == 2 and motif in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


def test_orchestrateur_modifie(monde, capsys):
    p = monde["r"].orchestrateur / "pole" / "adaptateurs.py"
    p.write_text(p.read_text() + "\n# remplacement\n")
    code, err = lancer(monde, capsys)
    assert code == 2 and "modifié" in err and not monde["journal"].exists()


def test_orchestrateur_arbre(monde, capsys):
    monde["r"].arbre_orchestrateur = "f" * 40
    code, err = lancer(monde, capsys)
    assert code == 2 and "arbre de l'orchestrateur" in err


def test_orchestrateur_commit_neuf_meme_arbre_admis(monde, capsys):
    """Un commit qui ne touche pas l'arbre épinglé (ici : commit vide) ne bloque pas la course."""
    git(monde["r"].orchestrateur, "commit", "-q", "--allow-empty", "-m", "page publique")
    assert jouer(monde, capsys)[0] == 0


def test_orchestrateur_cache_d_octets(monde, capsys):
    (monde["r"].orchestrateur / "pole" / "__pycache__").mkdir()
    (monde["r"].orchestrateur / "pole" / "__pycache__" / "adaptateurs.cpython-313.pyc").write_bytes(b"x")
    code, err = lancer(monde, capsys)
    assert code == 2 and "ignorés" in err


def test_orchestrateur_sain_clone_reel():
    r = lc.Reglages.production("carbon")
    if not (r.orchestrateur / lc.LANCEUR_ORCHESTRATEUR).is_file():
        pytest.skip("clone de l'orchestrateur absent")
    o = lc.verifier_orchestrateur(r)
    assert o["arbre"] == lc.ARBRE_ORCHESTRATEUR


def _ecarts_d_empreinte(lignee) -> dict:
    """Les pièces de la lignée dont l'empreinte épinglée par le lanceur diffère du fichier du dépôt (ou absent)."""
    out = {}
    for nom, (rel, attendu) in lc.pieces_de(lignee).items():
        p = RACINE / rel
        lu = sha(p) if p.is_file() else None
        if lu != attendu:
            out[nom] = (rel, attendu[:8], (lu or "absent")[:8])
    return out


def _xfail_si_empreinte_perimee(lignee):
    """Défaut du lanceur, pas de l'essai : une pièce épinglée a changé sur le dépôt après l'écriture du lanceur v8 (vu le
    18 novembre 2026 : `commande_astra_v1.py` reconstruite, commit 236a1b03 ; épingle `5e287603…`, fichier `986cf71e…`).
    Le lanceur refuserait la lignée (R11) ; correction : réépingler dans une version nouvelle du lanceur (R12). Marque
    stricte : elle tombe d'elle-même quand l'épingle et le dépôt concordent."""
    e = _ecarts_d_empreinte(lignee)
    return pytest.mark.xfail(bool(e), strict=True, reason=f"lignée {lignee} : empreinte épinglée par le lanceur ≠ fichier du "
                                                          f"dépôt (défaut du lanceur, pas de l'essai) : {e}")


@pytest.mark.parametrize("lignee", [pytest.param(l, marks=_xfail_si_empreinte_perimee(l)) for l in LIGNEES])
def test_pieces_sain_depot_reel(lignee):
    """Les pièces de la lignée (question v3, faits v3, témoins v1, enveloppe et commande externes) sont sur le dépôt réel
    à leurs empreintes ; aucun lien symbolique."""
    lues = lc.verifier_pieces(lc.Reglages.production(lignee))
    assert set(lues) == set(lc.pieces_de(lignee)) == {"question", "faits", "temoins", "enveloppe_externe", "commande_externe"}
    assert lues["enveloppe_externe"]["chemin"] == lc.LIGNEES_EXTERNES[lignee]["enveloppe"][0]
    assert lues["commande_externe"]["chemin"] == lc.LIGNEES_EXTERNES[lignee]["commande"][0]


_PIECES_REELLES = sorted({(rel, h) for l in LIGNEES for rel, h in lc.pieces_de(l).values()})


def _marque_piece_reelle(rel, attendu):
    """Empreinte périmée : défaut du lanceur (strict, voir `_xfail_si_empreinte_perimee`) ; compagnon absent : pièce non
    encore scellée (R6), l'essai redevient bloquant dès que le compagnon existe."""
    p = RACINE / rel
    if not p.is_file() or sha(p) != attendu:
        return pytest.mark.xfail(strict=True, reason=f"{rel} : empreinte épinglée {attendu[:8]}… ≠ fichier du dépôt "
                                                     f"{(sha(p) if p.is_file() else 'absent')[:8]}… (défaut du lanceur)")
    if not Path(str(p) + ".sha256").exists():
        return pytest.mark.xfail(strict=False, reason=f"compagnon .sha256 absent pour {rel} : pièce non scellée (R6)")
    return ()


@pytest.mark.parametrize("rel,attendu", [pytest.param(rel, h, id=Path(rel).name, marks=_marque_piece_reelle(rel, h))
                                         for rel, h in _PIECES_REELLES])
def test_pieces_scellees_depot_reel(rel, attendu):
    """Chaque pièce épinglée, à son empreinte sur disque **et** scellée par un compagnon égal (R6)."""
    assert sha(RACINE / rel) == attendu
    assert lc.lire_compagnon(RACINE / rel) == attendu


def test_pieces_artefact(monde, capsys):
    (monde["depot"] / monde["r"].pieces["question"][0]).write_text("autre question\n")
    code, err = lancer(monde, capsys)
    assert code == 2 and "pièces" in err and not monde["journal"].exists()


@pytest.mark.parametrize("python,motif", [("python3", "non absolu"), ("/nulle/part/python3", "absent"),
                                          ("/bin/sh", "un seul interpréteur")])
def test_interprete_artefacts(monde, capsys, python, motif):
    monde["r"].python = python
    monde["r"].orig_argv = (python, "-I", "-B", f"scripts/{lc.FICHIER_LANCEUR}", "carbon")
    code, err = lancer(monde, capsys)
    assert code == 2 and motif in err and not monde["journal"].exists()


def test_ecrire_scelle_jamais_ecrase(tmp_path):
    p = tmp_path / "m.json"
    lc.ecrire_scelle(p, {"a": 1})
    with pytest.raises(lc.Refus, match="existe déjà"):
        lc.ecrire_scelle(p, {"a": 2})


@pytest.mark.parametrize("nom", ["autre-chose", "20261118-010000" + lc.SUFFIXE_RUN + "1", "20261118-010000" + lc.SUFFIXE_RUN + "kimi",
                                 "20261118-010000" + lc.SUFFIXE_RUN + "Carbon", "20261118-010000-course-ideation-regard-ou-raisons-v1-g1"])
def test_dossier_inattendu_dans_les_runs(monde, capsys, nom):
    (monde["r"].dossier_runs / nom).mkdir(parents=True)
    code, err = lancer(monde, capsys)
    assert code == 2 and "inattendu" in err


def test_run_sans_manifeste(monde, capsys):
    (monde["r"].dossier_runs / ("20261118-010000" + lc.SUFFIXE_RUN + "carbon")).mkdir(parents=True)
    code, err = lancer(monde, capsys)
    assert code == 2 and "état inconnu" in err


def test_run_d_une_autre_lignee_dans_le_manifeste(monde, capsys):
    """Dossier nommé « carbon », manifeste qui dit « astra » : incohérence, refus (quelle que soit la lignée invoquée)."""
    d = monde["r"].dossier_runs / ("20261118-010000" + lc.SUFFIXE_RUN + "carbon")
    d.mkdir(parents=True)
    lc.ecrire_scelle(d / "manifeste-lanceur-refus.json", {"lignee": "astra", "lanceur": {"version": lc.VERSION}, "refus": "x"})
    for lignee in LIGNEES:
        code, err = lancer(avec_lignee(monde, lignee), capsys)
        assert code == 2 and "lignée ou version du lanceur incohérente" in err


def test_toute_exception_avant_depart_ecrit_un_refus(monde, capsys, monkeypatch):
    def panne(*a, **k):
        raise OSError("panne simulée")
    monkeypatch.setattr(lc, "construire_liste_blanche", panne)
    code, err = lancer(monde, capsys)
    assert code == 2 and "panne simulée" in err
    assert runs(monde)[0]["refus"] and not runs(monde)[0]["lance"]
    monkeypatch.undo()
    assert jouer(monde, capsys)[0] == 0


@pytest.mark.parametrize("variable,motif", [("FAUX_LB_SANS_SCEAU", "compagnon"), ("FAUX_LB_AUTRE", "différente")])
def test_liste_blanche_artefacts(monde, capsys, variable, motif):
    monde["env"][variable] = "1"
    code, err = lancer(monde, capsys)
    assert code == 2 and motif in err and [j["mode"] for j in journal(monde)] == []


def test_mesure_illisible(monde, capsys):
    monde["env"]["FAUX_MESURE_ILLISIBLE"] = "1"
    code, err = lancer(monde, capsys)
    assert code == 2 and "mesure des consignes illisible" in err


def test_mesure_garde_de_taille(monde, capsys):
    monde["env"]["FAUX_CONTROLE"] = "400001"
    code, err = lancer(monde, capsys)
    assert code == 2 and "garde(s) de taille" in err and "course" not in [j["mode"] for j in journal(monde)]


@pytest.mark.parametrize("lignee,autre", [("carbon", "argon"), ("astra", "carbon"), ("argon", "astra")])
def test_mesure_sans_la_garde_de_la_lignee(monde, capsys, lignee, autre):
    """La mesure rend la garde de passe d'une autre étiquette que celle du proposeur externe de la lignée : illisible, refus
    avant la course."""
    monde["env"]["FAUX_ETIQUETTE_GARDE"] = autre
    code, err = lancer(avec_lignee(monde, lignee), capsys)
    assert code == 2 and "tailles ou gardes absentes" in err and [j["mode"] for j in journal(monde)] == ["mesure"]


def test_source_sans_import_de_l_orchestrateur():
    import re
    texte = SCRIPT.read_text()
    assert [x for x in texte.splitlines() if re.match(r"^\s*(from\s+pole\b|import\s+pole\b)", x)] == []
    assert "setattr(" not in texte and "dict(os.environ)" not in texte
    assert not [m for m in sys.modules if m == "pole" or m.startswith("pole.")]


def test_source_sans_identifiant_de_cle_ni_valeur():
    texte = SCRIPT.read_text()
    assert "os.environ[" not in texte and "getenv(" not in texte


# ============================================================================================ orchestrateur réel, sans appel

def _clone_reel(lignee="carbon"):
    r = lc.Reglages.production(lignee)
    if not (r.orchestrateur / lc.LANCEUR_ORCHESTRATEUR).is_file():
        pytest.skip("clone de l'orchestrateur absent")
    lc.verifier_orchestrateur(r)
    return r


@pytest.mark.parametrize("lignee", LIGNEES)
def test_liste_blanche_et_mesure_contre_l_orchestrateur_reel(tmp_path, lignee):
    """Sans appel : modes `--construire-liste-blanche` et `--mesurer-consignes` de l'orchestrateur réel, sur les vraies
    pièces de la course, pour chaque lignée ; gardes de taille de la famille ; le clone reste propre (fichiers ignorés
    compris)."""
    r = _clone_reel(lignee)
    fichiers = {str(r.depot / r.pieces[n][0]): r.pieces[n][1] for n in ("question", "faits", "temoins")}
    env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(tmp_path), "LANG": "C.UTF-8"}
    lb = lc.construire_liste_blanche(r, tmp_path / "liste-blanche.json", env, tmp_path / "pyc", fichiers)
    assert lb["sha256"] == sha(tmp_path / "liste-blanche.json")
    m, _ = lc.mesurer_consignes(r, lc.commande_mesure(r, tmp_path / "liste-blanche.json", tmp_path / "pyc"), env,
                                tmp_path / "mesure.json")
    assert set(m["gardes_passes_externes"]) == {lignee}
    g = lc.gardes_de_taille(m, r)
    assert g["course"]["marge"] > 0 and g["passe_1"]["marge"] > 0
    assert g["commande_externe"]["controle_externe"]["tient"] and g["commande_externe"]["passe_1"]["tient"]
    assert g["commande_externe"]["famille"] == lc.LIGNEES_EXTERNES[lignee]["famille"]
    assert "passe_2_seuil_de_fiche" not in g and "commande_argon" not in g
    assert lc._git(r.orchestrateur, "status", "--porcelain", "--ignored").strip() == ""


ANALYSEUR = r'''
import json, sys
sys.path.insert(0, sys.argv[1])
import importlib.util
spec = importlib.util.spec_from_file_location("v2_essai", sys.argv[1] + "/demonstrations/ideation_v2.py")
v2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v2)
out = {}
for nom, argv in json.loads(sys.argv[2]).items():
    ns, inconnus = v2.construire_analyseur().parse_known_args(argv)
    out[nom] = {"inconnus": inconnus, "moteur": ns.moteur, "bras": ns.bras_rapporte_differe, "graine": ns.graine,
                "juge_externe": ns.juge_externe, "pieces": ns.piece, "temoins": ns.temoins,
                "proposeur_externe": ns.proposeur_externe,
                "modele_commande_externe": getattr(ns, "modele_commande_externe", None),
                "commande_externe_lit_modele": getattr(ns, "commande_externe_lit_modele", None),
                "seconde_passe": getattr(ns, "seconde_passe", None)}
print(json.dumps(out))
'''


@pytest.mark.parametrize("lignee", LIGNEES)
def test_analyseur_reel_accepte_les_deux_commandes(tmp_path, lignee):
    r = _clone_reel(lignee)
    ext = lc.LIGNEES_EXTERNES[lignee]
    pfx = tmp_path / "pyc"
    cmds = {"course": lc.commande_course(r, Path("/x/sortie"), Path("/x/lb.json"), "h", pfx),
            "mesure": lc.commande_mesure(r, Path("/x/lb.json"), pfx)}
    p = subprocess.run([r.python, "-I", "-B", "-X", f"pycache_prefix={tmp_path / 'pyc-analyseur'}", "-c", ANALYSEUR,
                        str(r.orchestrateur), json.dumps({k: v[6:] for k, v in cmds.items()})],
                       capture_output=True, text=True, timeout=120, cwd=str(tmp_path),
                       env={"PATH": "/usr/bin:/bin", "HOME": str(tmp_path)})
    assert p.returncode == 0, p.stderr[-800:]
    out = json.loads(p.stdout)
    assert all(v["inconnus"] == [] for v in out.values())
    assert out["course"]["moteur"] == "claude-sdk" and not out["course"]["bras"] and out["course"]["graine"] == 2026111808
    assert out["course"]["juge_externe"] == [f"{lignee}-juge={ext['modele']}"]
    assert out["course"]["proposeur_externe"] == [f"{lignee}={ext['modele']}"]
    assert out["course"]["modele_commande_externe"] == ext["modele"] and out["course"]["commande_externe_lit_modele"] is True
    assert not out["course"]["seconde_passe"] and not out["mesure"]["seconde_passe"]
    assert lc._git(r.orchestrateur, "status", "--porcelain", "--ignored").strip() == ""


# ============================================================================================ gardes de taille (calcul)

def mesure_de(etiquette, controle=70000):
    return {"sans_appel": True, "prix_entree_usd_par_million_jetons": 10.0,
            "consignes": {"consigne_de_controle_externe": controle, "consigne_passe_1": 30000, "nombre_par_proposeur": 6},
            "garde_course": {"passerait": True}, "gardes_passes_externes": {etiquette: {"passe_1": {"passerait": True}}}}


@pytest.mark.parametrize("lignee", LIGNEES)
def test_tailles_sain(lignee):
    ext = lc.LIGNEES_EXTERNES[lignee]
    g = lc.gardes_de_taille(mesure_de(lignee), lc.Reglages.production(lignee))
    assert g["course"]["marge"] > 0 and g["passe_1"]["marge"] > 0
    assert set(g) == {"course", "passe_1", "commande_externe"}
    ce = g["commande_externe"]
    assert ce["famille"] == ext["famille"] and ce["modele"] == ext["modele"]
    assert set(ce) == {"famille", "modele", "controle_externe", "passe_1"}
    assert all(ce[k]["tient"] for k in ("controle_externe", "passe_1"))
    assert ce["controle_externe"]["plafond"] == 1.7 and ce["passe_1"]["plafond"] == 1.5
    attendu = lc.plancher_externe(ext["famille"], 70000)
    assert ce["controle_externe"]["plancher_garde_a_3_caracteres_par_jeton"] == attendu["plancher_garde_a_3_caracteres_par_jeton"]


@pytest.mark.parametrize("modif,motif", [({"consigne_de_controle_externe": 400001}, "course"),
                                         ({"nombre_par_proposeur": 8}, "--nombre")])
def test_tailles_artefacts(modif, motif):
    m = mesure_de("carbon")
    m["consignes"].update(modif)
    with pytest.raises(lc.Refus, match=motif):
        lc.gardes_de_taille(m, lc.Reglages.production("carbon"))


@pytest.mark.parametrize("lignee,autre", [("carbon", "argon"), ("argon", "carbon"), ("astra", "argon")])
def test_tailles_garde_d_une_autre_lignee_illisible(lignee, autre):
    with pytest.raises(lc.Refus, match="tailles ou gardes absentes"):
        lc.gardes_de_taille(mesure_de(autre), lc.Reglages.production(lignee))


@pytest.mark.parametrize("lignee", LIGNEES)
def test_tailles_plafond_externe_trop_bas(lignee):
    """Un plafond de proposeur externe sous le plancher de sa commande : refus qui nomme la commande externe."""
    r = lc.Reglages.production(lignee)
    r.plafonds = dict(r.plafonds, **{f"proposeur_ideation|{lc.LIGNEES_EXTERNES[lignee]['modele']}": 0.3})
    with pytest.raises(lc.Refus, match="commande_externe/passe_1"):
        lc.gardes_de_taille(mesure_de(lignee), r)


def test_plancher_gemini():
    assert lc.plancher_gemini(0) == pytest.approx(0.509952)
    assert lc.plancher_gemini(70000, 3.0) == pytest.approx(24501 * 8.3e-6 + 0.509952)
    assert lc.plancher_gemini(70000, 3.0) > lc.plancher_gemini(70000, 4.0) > lc.plancher_gemini(0)


def test_plancher_astra():
    assert lc.plancher_astra(0) == pytest.approx(1024 * 10e-6 + 4096 * 50e-6) == pytest.approx(0.21504)
    assert lc.plancher_astra(70000) == pytest.approx((80500 + 1024) * 10e-6 + 0.2048)
    assert lc.plancher_astra(70000) > lc.plancher_astra(0)


def test_plancher_externe():
    g = lc.plancher_externe("gemini", 70000)
    assert set(g) == {"plancher_garde_a_3_caracteres_par_jeton", "plancher_a_4_caracteres_par_jeton_rapporte"}
    assert g["plancher_garde_a_3_caracteres_par_jeton"] == pytest.approx(lc.plancher_gemini(70000, 3.0))
    assert g["plancher_a_4_caracteres_par_jeton_rapporte"] == pytest.approx(lc.plancher_gemini(70000, 4.0))
    o = lc.plancher_externe("openai", 70000)
    assert o["plancher_garde_a_3_caracteres_par_jeton"] == o["plancher_a_4_caracteres_par_jeton_rapporte"] == pytest.approx(
        lc.plancher_astra(70000))
    for famille in ("kimi", "", "GEMINI", "anthropic"):
        with pytest.raises(lc.Refus, match="famille de commande externe inconnue"):
            lc.plancher_externe(famille, 1000)


# ============================================================================================ essais propres à cette course

def test_noms_propres_a_cette_course():
    """Rien de cette course ne peut se mêler aux runs, aux sorties ni au verrou des courses précédentes (« conception
    propre », « Regard ou raisons », v1 à v7 de celle-ci)."""
    for v in (str(lc.DOSSIER_SORTIES), lc.SOUS_DOSSIER_RUNS, lc.SUFFIXE_RUN, lc.NOM_VERROU, lc.VERSION):
        assert "organismes-discrets-v8" in v.replace("_", "-") and "regard" not in v and "conception" not in v, v
    assert lc.SUFFIXE_RUN.endswith("-v8-") and lc.FICHIER_LANCEUR == SCRIPT.name == lc.VERSION + ".py"
    assert lc.NOTES == "docs/notes/organismes-discrets-v1/organisme-ideation-v1"
    assert lc.ENVELOPPES == "rapports/organismes-discrets-v1/enveloppes-v1"
    assert lc.PERIMETRE_GO == ("organisme d'idéation", "organismes discrets", "trois lignées")
    assert lc.GRAINE == 2026111808 and lc.MAX_COURSES == 2 and lc.NOMBRE == 6
    assert lc.NOMS_PERMIS == ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")
    assert lc.DOSSIER_SORTIES == Path("/home/user/sorties-course-ideation-organismes-discrets-v8")


def test_plafonds_du_devis_v3():
    assert (lc.TOTAL_CLAUDE_USD, lc.TOTAL_EXTERNE_USD, lc.CONTROLE_EXTERNE_USD) == (6.0, 6.5, 1.7)
    assert (lc.PLAFOND_PROPOSEUR_EXTERNE_USD, lc.PLAFOND_JUGE_EXTERNE_USD) == (1.5, 2.5)
    assert lc.PLAFONDS_INTERNES == {"proposeur_ideation|claude-opus-5-5": 2.0, "juge_ideation|claude-opus-5-5": 2.0}
    assert lc.EXPOSITION_EXTERNE_COURSE_USD == pytest.approx(3.2) and lc.PLAFOND_COURSE_USD == pytest.approx(9.2)
    assert lc.PIRE_CAS_DEVIS_USD == lc.BORNE_LIGNE_USD == 34.0
    assert lc.PROPOSEURS == (("opus", "claude-opus-5-5"),) and lc.JUGES == (("opus-juge", "claude-opus-5-5"),)
    for lignee in LIGNEES:
        m = lc.LIGNEES_EXTERNES[lignee]["modele"]
        assert lc.plafonds_de(lignee) == {"proposeur_ideation|claude-opus-5-5": 2.0, "juge_ideation|claude-opus-5-5": 2.0,
                                          f"proposeur_ideation|{m}": 1.5, f"juge_ideation|{m}": 2.5}
        assert lc.externe_de(lignee) == ((lignee, m), (f"{lignee}-juge", m))
    assert lc.PLAFONDS == lc.plafonds_de("carbon")
    assert lc.ARBRE_ORCHESTRATEUR == "ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70" and len(lc.EMPREINTES_ORCHESTRATEUR) == 9
    assert lc.LANCEUR_ORCHESTRATEUR == "demonstrations/ideation_v8.py"


def test_lignees_externes_coherentes():
    assert tuple(lc.LIGNEES_EXTERNES) == lc.LIGNEES
    modeles, enveloppes = set(), set()
    for lignee, d in lc.LIGNEES_EXTERNES.items():
        assert set(d) == {"etiquette", "modele", "famille", "enveloppe", "commande"} and d["etiquette"] == lignee
        assert d["famille"] in ("gemini", "openai") and lignee in d["enveloppe"][0]
        modeles.add(d["modele"])
        enveloppes.add(d["enveloppe"][0])
    assert len(modeles) == len(enveloppes) == 3
    assert lc.LIGNEES_EXTERNES["carbon"]["commande"] == lc.LIGNEES_EXTERNES["argon"]["commande"] == lc.COMMANDE_GEMINI
    assert lc.LIGNEES_EXTERNES["astra"]["commande"] == lc.COMMANDE_ASTRA and lc.LIGNEES_EXTERNES["astra"]["famille"] == "openai"
    assert lc.LIGNEES_EXTERNES["carbon"]["famille"] == lc.LIGNEES_EXTERNES["argon"]["famille"] == "gemini"
    assert lc.COMMANDE_GEMINI[0].endswith("commande_argon_v3e.py") and lc.COMMANDE_ASTRA[0].endswith("commande_astra_v1.py")
    assert lc.LIGNEES_EXTERNES == {"carbon": {"etiquette": "carbon", "modele": "gemini-4-carbon", "famille": "gemini",
                                              "enveloppe": lc.LIGNEES_EXTERNES["carbon"]["enveloppe"], "commande": lc.COMMANDE_GEMINI},
                                   "astra": {"etiquette": "astra", "modele": "gpt-6-astra", "famille": "openai",
                                             "enveloppe": lc.LIGNEES_EXTERNES["astra"]["enveloppe"], "commande": lc.COMMANDE_ASTRA},
                                   "argon": {"etiquette": "argon", "modele": "gemini-4-argon", "famille": "gemini",
                                             "enveloppe": lc.LIGNEES_EXTERNES["argon"]["enveloppe"], "commande": lc.COMMANDE_GEMINI}}
    with pytest.raises(KeyError):
        lc.pieces_de("kimi")


def test_noms_de_cle_liste_entiere():
    """Mutation « équivalente » de la contre-lecture précédente (un nom de clé retiré de la liste) : rendue décidable."""
    assert set(lc.NOMS_DE_CLE) == {"ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY",
                                   "GOOGLE_API_KEY", "GEMINI_API_KEY", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN",
                                   "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN", "KIMI_API_KEY"}
    assert not set(lc.NOMS_PERMIS) & set(lc.NOMS_DE_CLE)


def test_pieces_de_cette_course():
    assert lc.PIECES == lc.pieces_de("carbon") and set(lc.PIECES_COMMUNES) == {"question", "faits", "temoins"}
    assert lc.PIECES_COMMUNES["question"][0] == f"{lc.NOTES}/question-v3.md"
    assert lc.PIECES_COMMUNES["faits"][0] == f"{lc.NOTES}/faits-v3.md"
    assert lc.PIECES_COMMUNES["temoins"][0] == f"{lc.NOTES}/temoins-organisme-discrets-v1.json"
    for lignee in LIGNEES:
        p = lc.pieces_de(lignee)
        assert {k: p[k] for k in lc.PIECES_COMMUNES} == lc.PIECES_COMMUNES
        assert p["enveloppe_externe"][0].startswith(lc.ENVELOPPES + "/appel-" + lignee)
        assert not any("bilan" in rel for rel, _ in p.values())          # aucun bilan d'une autre source n'est servi
        for nom, (rel, _) in p.items():
            assert (RACINE / rel).is_file(), (lignee, nom)                  # l'empreinte : `test_pieces_scellees_depot_reel`
    assert "sorties-course-ideation" not in json.dumps(lc.PIECES)        # les pièces viennent du dépôt, jamais des sorties


def test_temoins_quatre_classes_sans_fausse_nouveaute():
    """Les quatre classes exigées par l'orchestrateur ; les fiches « faux » se déclarent occupées (aucune affirmation
    fausse dans une pièce servie) ; le jumeau nomme le vrai."""
    d = json.loads((RACINE / lc.PIECES_COMMUNES["temoins"][0]).read_text(encoding="utf-8"))
    assert "temoins" in d
    par_classe = {t["classe"]: t for t in d["temoins"]}
    assert sorted(par_classe) == ["faux_anteriorite", "faux_falsifiabilite", "jumeau", "vrai"] and len(d["temoins"]) == 4
    assert par_classe["faux_anteriorite"]["fiche"]["originalite"]["niveau"] == "occupee"
    assert par_classe["faux_falsifiabilite"]["fiche"]["originalite"]["niveau"] == "occupee"
    assert par_classe["jumeau"]["jumeau_de"] == par_classe["vrai"]["fiche"]["nom"]


def test_copies_sortie_ajoutees():
    assert {"manifeste-depart.json", "lecture.json", "classement.json"} <= set(lc.COPIES_SORTIE)
    assert {"fiches-validees.json", "fiches-refusees.json", "fiches-en-quarantaine.json", "manifeste-fin.json",
            "lecture-course.json", "noyau/temoins-servis.json"} <= set(lc.COPIES_SORTIE)
    assert len(lc.COPIES_SORTIE) == len(set(lc.COPIES_SORTIE)) == 13


# --- les trois gardes sans essai qui les isole (m4 de la contre-lecture du lanceur « conception propre »)

def test_depense_sortie_sans_manifeste_de_fin_compte_le_plafond(tmp_path):
    s = tmp_path / "sortie"
    s.mkdir()                                                             # sortie créée, aucun manifeste de fin, aucun contrôle
    dep, lisible, lecture = lc.depense_course(s, True)
    assert dep == lc.PLAFOND_COURSE_USD and lisible is False and "sans manifeste de fin" in lecture


@pytest.mark.parametrize("piece", ["question", "faits", "temoins", "enveloppe_externe", "commande_externe"])
def test_pieces_artefact_chacune(monde, capsys, piece):
    """Chaque pièce épinglée, y compris les deux que la liste blanche de l'orchestrateur ne couvre pas."""
    (monde["depot"] / monde["r"].pieces[piece][0]).write_text("contenu remplacé\n")
    code, err = lancer(monde, capsys)
    assert code == 2 and "pièces absentes ou d'empreinte différente" in err and piece in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


@pytest.mark.parametrize("lignee", AUTRES)
def test_pieces_artefact_enveloppe_de_la_lignee(monde, capsys, lignee):
    """L'enveloppe d'une lignée remplacée : refus de cette lignée seulement ; les autres pièces restent vérifiées."""
    m = avec_lignee(monde, lignee)
    (monde["depot"] / m["r"].pieces["enveloppe_externe"][0]).write_text("contenu remplacé\n")
    code, err = lancer(m, capsys)
    assert code == 2 and "pièces absentes ou d'empreinte différente" in err and "enveloppe_externe" in err
    assert jouer(monde, capsys)[0] == 0                                   # carbon, dont l'enveloppe est intacte, part


@pytest.mark.parametrize("piece", ["question", "enveloppe_externe", "commande_externe"])
def test_pieces_lien_symbolique(monde, capsys, piece):
    p = monde["depot"] / monde["r"].pieces[piece][0]
    vrai = p.with_name(p.name + ".vrai")
    p.rename(vrai)
    p.symlink_to(vrai)
    code, err = lancer(monde, capsys)
    assert code == 2 and "pièces absentes ou d'empreinte différente" in err and not monde["journal"].exists()


def test_bac_a_sable_inactif_isole(monde, capsys):
    """Bac inactif alors que /proc est neuf : seule la garde « inactif » peut refuser."""
    monde["env"]["FAUX_BAC"] = "eteint_proc_neuf"
    code, err = lancer(monde, capsys)
    assert code == 2 and "bac à sable de l'orchestrateur inactif" in err and "/proc neuf" not in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


# --- relevé illisible : toujours remonté au plafond (mutation « équivalente » rendue décidable)

def test_releve_illisible_remonte_au_plafond(tmp_path):
    d = tmp_path / "run"
    d.mkdir()
    sceller(d / "releve-depense.json", json.dumps({"course_usd": 0.1, "lisible": False, "fiches_produites": False,
                                                   "lecture": "essai"}))
    run = {"nom": "run", "dossier": d, "lignee": "carbon", "lance": True,
           "fin": {"code": 0, "releve_sha256": sha(d / "releve-depense.json")}}
    rel = lc.releve_run(run)
    assert rel["course_usd"] == lc.PLAFOND_COURSE_USD and rel["lisible"] is False
    with pytest.raises(lc.Refus, match="garde de cumul"):
        lc.garde_cumul([run], 18.3)
    assert lc.garde_cumul([run], 34.0)["depense_relevee_usd"] == pytest.approx(9.2)
    lisible = dict(run, fin={"code": 0, "releve_sha256": "0" * 64})
    assert lc.releve_run(lisible)["course_usd"] == lc.PLAFOND_COURSE_USD      # relevé non lié à la fin : plafond
    assert not lc.relance_permise([run], "carbon")[0] and lc.relance_permise([run], "astra")[0]


# --- arrêt propre : SIGINT relayé par PID (condition C1 de la contre-lecture du lanceur « conception propre »)

def test_arret_propre_par_int_relaye(monde, capsys):
    if signal.getsignal(signal.SIGINT) is signal.SIG_IGN:
        pytest.skip("SIGINT ignoré dans ce processus (lancé en arrière-plan) : l'enfant l'ignorerait aussi")
    monde["env"]["FAUX_DORT"] = "30"
    code, sortie = lancer(monde, capsys)
    assert code == 0 and sortie.index("kill -INT") < sortie.index("kill -TERM")
    sup = runs(monde)[0]["superviseur"]
    assert sup["arret"].startswith(f"kill -INT {sup['pid']} d'abord")
    pidf = Path(sup["dossier"]) / "pid-orchestrateur.json"
    for _ in range(100):
        if pidf.exists() and Path(str(pidf) + ".sha256").exists():
            break
        time.sleep(0.05)
    time.sleep(0.3)                                                        # l'enfant a posé son gestionnaire de SIGINT
    os.kill(sup["pid"], signal.SIGINT)
    os.waitpid(sup["pid"], 0)
    c = json.loads((Path(sup["dossier"]) / "code.json").read_text())
    assert c["code"] != 0 and c["code"] in (-signal.SIGINT, 1, 130)        # arrêté par SIGINT, code scellé par le superviseur
    assert lc.debut_processus(c["pid_orchestrateur"]) is None             # l'orchestrateur ne vit plus
    code, sortie = lancer(monde, capsys)
    assert code == 0 and "clôture" in sortie and "fin propre" in sortie


def test_orphelin_conseil_d_arret_int_d_abord(monde, capsys):
    monde["env"]["FAUX_DORT"] = "30"
    assert lancer(monde, capsys)[0] == 0
    p = _tuer_superviseur(runs(monde)[0]["superviseur"])
    o = lc.orchestrateur_orphelin(runs(monde)[0]["superviseur"])
    assert o["arret"].startswith(f"kill -INT {p['pid_orchestrateur']} d'abord") and f"kill -TERM {p['pid_orchestrateur']}" in o["arret"]
    os.kill(p["pid_orchestrateur"], signal.SIGKILL)
    _attendre_mort(p["pid_orchestrateur"])
