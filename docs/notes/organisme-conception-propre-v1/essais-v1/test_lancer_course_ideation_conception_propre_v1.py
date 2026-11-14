"""Essais R5 de `scripts/lancer_course_ideation_conception_propre_v1.py` (une génération, question de la conception propre
de l'organisme ; R-2593, R-2609), dérivés de ceux du lanceur v3 des bassins étroits (`6ab6ec5d…`). Ajouts : M1 (le lanceur
garde ses options, sa commande d'origine, son dossier courant, sa place et son empreinte), M2 (aucune commande git après le
détachement ; manifeste de départ manquant → PID imprimé, course retrouvée par le pré-départ et le PID scellé par le
superviseur), B1 et m1 (relevé de dépense et copies scellées dans le dépôt ; le dossier hors dépôt peut disparaître),
une seule relance au total, ligne de GO trouvée par son contenu, garde de cumul à 25 USD avec la réserve du lecteur,
aucun bras.

Aucun modèle appelé, aucun réseau. Un **faux orchestrateur** (dépôt git jetable) est servi au lanceur par `Reglages`. Deux
essais **sans appel** contre l'orchestrateur réel (liste blanche et mesure ; analyseur d'arguments) tournent quand le clone
est là, dans des processus à part, `-I -B`, cache d'octets hors du clone. Deux essais lancent le vrai fichier dans un
processus à part avec une commande **fausse** (sans `-I`, mauvais argument) : il refuse avant le verrou et avant toute
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
SCRIPT = RACINE / "scripts" / "lancer_course_ideation_conception_propre_v1.py"
_spec = importlib.util.spec_from_file_location("lancer_course_ideation_conception_propre_v1", SCRIPT)
lc = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = lc
_spec.loader.exec_module(lc)

FAUX_V8 = r'''
import hashlib, json, os, sys, time
argv = sys.argv[1:]

def sceller(chemin, objet=None, texte=None):
    t = texte if texte is not None else json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    open(chemin, "w", encoding="utf-8").write(t)
    open(chemin + ".sha256", "w").write(hashlib.sha256(t.encode("utf-8")).hexdigest() + "  " + os.path.basename(chemin) + "\n")

def consigner(mode):
    noms = [n for n in os.environ if "KEY" in n or "TOKEN" in n or "SECRET" in n]
    with open(os.environ["FAUX_JOURNAL"], "a") as f:
        f.write(json.dumps({"mode": mode, "argv": argv, "cwd": os.getcwd(), "noms_cle": noms, "go_id": os.environ.get("GO_ID"),
                            "noms_env": sorted(os.environ), "home": os.environ.get("HOME"),
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
    print(json.dumps({"sans_appel": True, "prix_entree_usd_par_million_jetons": 10.0,
                      "consignes": {"consigne_de_controle_externe": ctrl, "consigne_passe_1": 30000,
                                    "consigne_passe_2_maximale": 300000, "consigne_du_juge_maximale": 900000,
                                    "fiches_au_juge_au_maximum": 40, "nombre_par_proposeur": 6},
                      "garde_course": {"passerait": ctrl <= 400000},
                      "gardes_passes_externes": {"argon": {"passe_1": {"passerait": True}}}}))
    sys.exit(0)
sortie = argv[0]
consigner("course")
time.sleep(float(os.environ.get("FAUX_DORT", "0")))
code = int(os.environ.get("FAUX_CODE", "0"))
if os.environ.get("FAUX_RIEN") == "1":
    sys.exit(code)
if os.environ.get("FAUX_CONTROLE_SEUL"):
    c = sortie + "-controle"
    os.makedirs(os.path.join(c, "tentative-1-externe-argon"))
    if os.environ["FAUX_CONTROLE_SEUL"] == "plancher":
        sceller(os.path.join(c, "tentative-1.json"), {"reglages": {"cout_claude_usd": 0.0,
                "cout_externe_usd": float(os.environ.get("FAUX_COUT_CONTROLE", "1e-06"))}})
    sys.exit(2)
ids = ["opus-p1-01", "opus-p2-01", "fable-p1-01", "argon-p1-01", "fable-p1-02"]
fiches = [{"identifiant_auteur": i, "auteur": i.split("-p")[0], "passe": int(i.split("-p")[1][0]), "nom": "Idée " + i,
           "enonce": "énoncé de " + i, "empreinte": hashlib.sha256(i[::-1].encode()).hexdigest()} for i in ids]
sceller(os.path.join(sortie, "fiches-validees.json"), fiches)
sceller(os.path.join(sortie, "fiches-refusees.json"), [])
sceller(os.path.join(sortie, "fiches-en-quarantaine.json"), [])
sceller(os.path.join(sortie, "noyau", "temoins-servis.json"), [{"identifiant_auteur": "temoin-p0-01"}])
sceller(os.path.join(sortie, "notes-par-juge.json"), {"opus-juge": {"opus-p1-01": {"total": 9}}})
sceller(os.path.join(sortie, "lecture-course.json"),
        {"bras_rapporte_differe": [{"etiquette": "argon-juge", "consigne_en_attente_sha256": "c" * 64}]})
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
    return {"actif": e in ("actif", "sans_proc"), "proc_neuf": e == "actif", "motif": "faux : " + e}
'''

PERIM = ("**Organisme d'idéation, atelier d'idées (N-065, rôle 2), sur sa propre conception (juge, proposeurs, composition, "
         "coût) : une génération** (R-2593, R-2609)")
GO_LIGNE = f"| GO-2026-11-14-01 | 2026-11-13 | calcul | {PERIM} | 21 USD | 2026-11-30 | Lazar | R-2609 |"
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
    pieces = {}
    for nom, (rel, _) in lc.PIECES.items():
        p = depot / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"pièce factice {nom}\n")
        pieces[nom] = (rel, sha(p))
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
    horloge = {"t": dt.datetime(2026, 11, 14, 1, 0, 0, tzinfo=dt.timezone.utc)}

    def maintenant():
        horloge["t"] += dt.timedelta(seconds=1)
        return horloge["t"]
    r = lc.Reglages(depot=depot, orchestrateur=orch, arbre_orchestrateur=arbre,
                    empreintes_orchestrateur={"demonstrations/ideation_v8.py": sha(orch / "demonstrations/ideation_v8.py"),
                                              "pole/adaptateurs.py": sha(orch / "pole/adaptateurs.py")},
                    pieces=pieces, registre_go=depot / "registres" / "go.md", dossier_runs=depot / "runs" / "course-x",
                    dossier_sorties=tmp_path / "sorties", depot_attendu_par_l_enveloppe=depot, python=sys.executable,
                    fichier_lanceur=lanceur, drapeaux=SimpleNamespace(isolated=1, dont_write_bytecode=1),
                    orig_argv=(sys.executable, "-I", "-B", f"scripts/{lc.FICHIER_LANCEUR}", "1"), cwd=str(depot),
                    environnement=env, aujourd_hui=dt.date(2026, 11, 14), horodatage=lambda: "Sat Nov 14 01:00:00 UTC 2026",
                    maintenant=maintenant, prefixe_essais="FAUX_")
    reecrire_go(r, GO_LIGNE)
    yield {"r": r, "journal": journal, "env": env, "tmp": tmp_path, "depot": depot}
    for pid in superviseurs(r):                       # jamais par motif : par PID, ceux de cet essai seulement
        try:
            os.kill(pid, signal.SIGKILL)
            os.waitpid(pid, 0)
        except (ProcessLookupError, ChildProcessError):
            pass


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


def lancer(monde, capsys=None, argv=("1",)):
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


# ============================================================================================ argument unique et fermé

@pytest.mark.parametrize("argv", [[], ["2"], ["0"], ["1", "1"], ["--accepter-sans-bac-a-sable"], ["01"], [" 1"], ["un"]])
def test_argument_artefacts(monde, capsys, argv):
    assert lc.principal(argv, monde["r"]) == 2
    assert "un seul argument" in capsys.readouterr().err and not monde["journal"].exists()
    assert not monde["r"].dossier_sorties.exists()


def test_generations_une_seule():
    assert lc.GENERATIONS == ("1",) and lc.ARGUMENT == "1" and lc.MAX_COURSES == 2


# ============================================================================================ M1 : le lanceur se garde

def test_m1_sain(monde):
    soi = lc.verifier_soi(monde["r"])
    assert soi["sha256"] == sha(monde["r"].fichier_lanceur) and soi["version"] == lc.VERSION


@pytest.mark.parametrize("modif,motif", [
    ({"drapeaux": SimpleNamespace(isolated=0, dont_write_bytecode=1)}, "-I absente"),
    ({"drapeaux": SimpleNamespace(isolated=1, dont_write_bytecode=0)}, "-B absente"),
    ({"orig_argv": ("/autre/python3", "-I", "-B", "scripts/" + "lancer_course_ideation_conception_propre_v1.py", "1")},
     "commande d'origine"),
    ({"orig_argv": ("PY", "-I", "-B", "-X", "dev", "scripts/lancer_course_ideation_conception_propre_v1.py", "1")},
     "commande d'origine"),
    ({"orig_argv": ("PY", "-IB", "scripts/lancer_course_ideation_conception_propre_v1.py", "1")}, "commande d'origine"),
    ({"orig_argv": ("PY", "-I", "-B", "./scripts/lancer_course_ideation_conception_propre_v1.py", "1")},
     "commande d'origine"),
    ({"orig_argv": ("PY", "-I", "-B", "scripts/lancer_course_ideation_conception_propre_v1.py", "1", "x")},
     "commande d'origine"),
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


def test_m1_compagnon_reel_du_lanceur():
    assert lc.lire_compagnon(SCRIPT) == sha(SCRIPT), "le lanceur doit être scellé (compagnon égal au fichier)"


def test_m1_production_lit_ses_vraies_valeurs():
    r = lc.Reglages.production()
    assert r.drapeaux is sys.flags and r.fichier_lanceur == SCRIPT and r.python == "/usr/local/bin/python3"
    assert tuple(r.orig_argv) == tuple(sys.orig_argv)
    assert lc.commande_exacte(r) == ("/usr/local/bin/python3", "-I", "-B",
                                     "scripts/lancer_course_ideation_conception_propre_v1.py", "1")


@pytest.mark.parametrize("args,motif", [(["-B"], "-I absente"), (["-I", "-B"], "un seul argument")])
def test_m1_vrai_fichier_commande_fausse_refuse_sans_rien_ecrire(tmp_path, args, motif):
    """Le vrai fichier, en processus à part, avec une commande fausse : refus avant le verrou (rien n'est créé)."""
    if not Path(lc.PYTHON_COURSE).is_file():
        pytest.skip("interpréteur de production absent")
    avant = lc.DOSSIER_SORTIES.exists()
    argv = [lc.PYTHON_COURSE, *args, f"scripts/{lc.FICHIER_LANCEUR}"] + (["1"] if "-I" not in args else ["2"])
    p = subprocess.run(argv, cwd=str(RACINE), capture_output=True, text=True, timeout=60,
                       env={"PATH": "/usr/bin:/bin", "HOME": str(tmp_path)})
    assert p.returncode == 2 and motif in p.stderr, p.stderr
    assert lc.DOSSIER_SORTIES.exists() == avant


# ============================================================================================ chaîne saine de bout en bout

def test_generation_bout_en_bout(monde, capsys):
    r = monde["r"]
    code, sortie = jouer(monde, capsys)
    assert code == 0 and "lancée, détachée" in sortie and "GO-2026-11-14-01" in sortie
    rs = runs(monde)
    assert len(rs) == 1 and rs[0]["lance"] and rs[0]["fin"]["code"] == 0
    j = [x for x in journal(monde) if x["mode"] == "course"]
    assert [x["mode"] for x in journal(monde)] == ["mesure", "course"]
    a = j[0]["argv"]
    assert j[0]["noms_cle"] == [] and j[0]["go_id"] == "GO-2026-11-14-01"
    assert {n for n in j[0]["noms_env"] if not n.startswith("FAUX_")} <= set(lc.NOMS_PERMIS) | {"HOME", "GO_ID",
                                                                                               "PYTHONPYCACHEPREFIX"}
    assert j[0]["sid"] != os.getsid(0) and j[0]["orig_argv"][1:3] == ["-I", "-B"]
    assert a[a.index("--nombre") + 1] == "6" and a[a.index("--graine") + 1] == "2026111401"
    assert a[a.index("--budget-total-usd") + 1] == "10.0" and a[a.index("--budget-externe-usd") + 1] == "8.0"
    assert [a[i + 1] for i, x in enumerate(a) if x == "--piece"] == [str(r.depot / r.pieces["faits"][0])]
    assert "--bras-rapporte-differe" not in a and "--accepter-sans-bac-a-sable" not in a
    d = rs[0]["dossier"]
    pre = json.loads((d / "manifeste-lanceur-pre-depart.json").read_text())
    texte = (d / "manifeste-lanceur-pre-depart.json").read_text()
    for interdit in ("valeur-factice-d-essai", "hote.invalid", "mandataire.invalid", "ANTHROPIC_API_KEY",
                     "CLAUDE_CODE_REMOTE", "KIMI_API_KEY"):
        assert interdit not in texte                                    # m5 : ni valeurs, ni noms exclus
    assert pre["environnement"]["noms_exclus"]["nombre"] == 10
    assert pre["plafonds"]["sommes"]["somme_claude"] == 9.9 and pre["plafonds"]["sommes"]["somme_externe"] == 7.6
    assert pre["plafonds"]["sommes"]["exposition_externe_course"] == 4.9
    assert pre["lanceur"]["sha256"] == sha(r.fichier_lanceur) and pre["depot_travail"]
    dep = json.loads((d / "manifeste-lanceur-depart.json").read_text())
    assert dep["pre_depart_sha256"] == sha(d / "manifeste-lanceur-pre-depart.json")
    rel = json.loads((d / "releve-depense.json").read_text())
    assert rel["course_usd"] == pytest.approx(4.5) and rel["lisible"] and rel["fiches_produites"] is True
    assert rel["comptes_fiches"]["fiches-validees.json"] == 5
    fin = json.loads((d / "manifeste-lanceur-fin.json").read_text())
    assert fin["releve_sha256"] == sha(d / "releve-depense.json")
    assert fin["pour_l_attestation"]["fiches_validees_sha256"] == sha(rs[0]["sortie"] / "fiches-validees.json")
    for f in list(d.glob("*.json")) + list((d / "copies").glob("*.json")):
        h, nom = Path(str(f) + ".sha256").read_text().split()
        assert nom == f.name and h == sha(f)
    assert (d / "copies" / "sortie--fiches-validees.json").read_bytes() == (rs[0]["sortie"] / "fiches-validees.json").read_bytes()
    assert (d / "copies" / "sortie--noyau--temoins-servis.json").is_file()
    assert (d / "copies" / "superviseur--code.json").is_file() and (d / "copies" / "superviseur--pid-superviseur.json").is_file()
    code, err = lancer(monde, capsys)
    assert code == 2 and "fiches produites" in err and "jamais rejouée" in err
    assert not str(rs[0]["sortie"]).startswith(str(monde["depot"]))


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
    assert lc.relance_permise(runs(monde))[0]
    assert (runs(monde)[0]["dossier"] / "copies" / "controle--tentative-1.json").is_file()


def test_m1_perte_partielle_de_la_sortie_sans_effet(monde, capsys):
    assert jouer(monde, capsys)[0] == 0
    shutil.rmtree(runs(monde)[0]["sortie"])                             # la sortie disparaît seule, après la clôture
    rel = lc.releve_run(runs(monde)[0])
    assert rel["fiches_produites"] is True and rel["course_usd"] == pytest.approx(4.5)
    assert not lc.relance_permise(runs(monde))[0]


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
    ok, motif = lc.relance_permise(runs(monde))
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
    with pytest.raises(lc.Refus, match="garde de cumul"):
        lc.garde_cumul(rs, 21.0)                                          # plafond compté


# ============================================================================================ détaché, PID, orphelin, verrou

def test_en_marche_rien_ne_part(monde, capsys):
    monde["env"]["FAUX_DORT"] = "3"
    assert lancer(monde, capsys)[0] == 0
    code, sortie = lancer(monde, capsys)
    assert code == 3 and "en marche" in sortie and "kill -TERM" in sortie
    attendre(monde)
    assert [j["mode"] for j in journal(monde)] == ["mesure", "course"]
    code, sortie = lancer(monde, capsys)
    assert code == 0 and "clôture" in sortie


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
    monde["r"].aujourd_hui = dt.date(2026, 12, 1)
    code, sortie = lancer(monde, capsys)
    assert code == 3 and "en marche" in sortie
    attendre(monde)
    code, sortie = lancer(monde, capsys)
    assert code == 0 and "clôture" in sortie


# ============================================================================================ relance unique, cumul

def test_relance_unique_apres_defaut_au_controle(monde, capsys):
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", "0.275477"
    assert jouer(monde, capsys)[0] == 0
    assert lc.relance_permise(runs(monde))[0]
    assert jouer(monde, capsys)[0] == 0                                 # la seule relance
    code, err = lancer(monde, capsys)
    assert code == 2 and "2 courses déjà parties" in err
    pre = json.loads((runs(monde)[1]["dossier"] / "manifeste-lanceur-pre-depart.json").read_text())
    assert pre["garde_de_cumul"]["depense_relevee_usd"] == pytest.approx(0.275477)
    assert pre["relance"].startswith("1 course")


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
    ok, motif = lc.relance_permise([dict(run, fin=dict(run["fin"], code=None))])
    assert not ok and "sans fin propre" in motif


@pytest.mark.parametrize("plafond,cout,attendu", [("21 USD", "2.0", 0), ("21 USD", "2.2", 2), ("25 USD", "2.2", 0),
                                                  ("21 USD", "2.1", 0), ("100 USD", "6.1", 0),
                                                  ("100 USD", "6.2", 2)])
def test_garde_de_cumul(monde, capsys, plafond, cout, attendu):
    reecrire_go(monde["r"], GO_LIGNE.replace("| 21 USD |", f"| {plafond} |"))
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", cout
    assert jouer(monde, capsys)[0] == 0
    del monde["env"]["FAUX_CONTROLE_SEUL"]
    code, err = lancer(monde, capsys)
    assert code == attendu, err
    if attendu:
        assert "garde de cumul" in err and "réserve du lecteur" in err
    else:
        attendre(monde)


def test_cumul_constantes():
    assert lc.PLAFOND_COURSE_USD == pytest.approx(14.9) and lc.RESERVE_LECTEUR_USD == 4.0
    assert lc.PIRE_CAS_DEVIS_USD == pytest.approx(lc.PLAFOND_COURSE_USD + 2.1 + lc.RESERVE_LECTEUR_USD)
    assert lc.BORNE_LIGNE_USD == 25.0 and lc.garde_cumul([], 21.0)["depense_relevee_usd"] == 0.0


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
    (c / "tentative-2-externe-argon").mkdir()
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
    g = lc.verifier_go(monde["r"].registre_go, dt.date(2026, 11, 14))
    assert g["id"] == "GO-2026-11-14-01" and g["plafond_usd"] == 21.0


def test_go_apostrophe_typographique(monde):
    reecrire_go(monde["r"], GO_LIGNE.replace("d'idéation", "d’idéation"))
    assert lc.verifier_go(monde["r"].registre_go, dt.date(2026, 11, 14))["id"] == "GO-2026-11-14-01"


@pytest.mark.parametrize("ligne,motif", [
    (GO_LIGNE.replace("propre conception", "conception"), "0 ligne"),
    (GO_LIGNE + "\n" + GO_LIGNE.replace("GO-2026-11-14-01", "GO-2026-11-14-02"), "2 ligne"),
    (GO_LIGNE.replace("| calcul |", "| publication |"), "type"),
    (GO_LIGNE.replace("| Lazar |", "| Claude |"), "Lazar exigé"),
    (GO_LIGNE.replace("| 21 USD |", "| 20.9 USD |"), "sous le pire cas"),
    (GO_LIGNE.replace("| 21 USD |", "| vingt et un |"), "illisible"),
    (GO_LIGNE.replace("| 2026-11-30 |", "| 2026-11-13 |"), "période"),
    (GO_LIGNE + "\n| GO-2026-11-14-03 | 2026-11-14 | révocation | révoque GO-2026-11-14-01 | — | — | Lazar | x |", "révoqué"),
    (GO_LIGNE + "\n| GO-2026-11-14-03 | 2026-11-14 | Revocation | révoque GO-2026-11-14-01 | — | — | Lazar | x |", "révoqué"),
    (GO_LIGNE + "\n| GO-2026-11-14-03 | 2026-11-14 | révocation | GO-2026-11-14-01 | — | — | Lazar | x | y |", "mal formée"),
    (GO_LIGNE + "\n| GO-2026-11-14-01 | 2026-11-14 | calcul | autre chose | 5 USD | 2026-11-20 | Lazar | x |", "lignes principales"),
])
def test_go_artefacts(monde, capsys, ligne, motif):
    reecrire_go(monde["r"], ligne)
    code, err = lancer(monde, capsys)
    assert code == 2 and motif in err and not monde["journal"].exists()


def test_go_registre_reel_ne_contient_pas_encore_la_ligne():
    """La ligne n'est pas inscrite à la préparation : le lanceur refuserait (sens fermé)."""
    with pytest.raises(lc.Refus):
        lc.verifier_go(RACINE / "registres" / "go.md", dt.date(2026, 11, 14))


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
    assert lc.Reglages.production().prefixe_essais is None
    with pytest.raises(lc.Refus, match="préfixe d'essai interdit"):
        lc.environnement_permis({"PATH": "/bin"}, "GO-X", prefixe_essais="CLAUDE_")


def test_environnement_permis_artefact_nom_interdit(monkeypatch):
    monkeypatch.setattr(lc, "NOMS_PERMIS", lc.NOMS_PERMIS + ("CLAUDE_CODE_REMOTE",))
    with pytest.raises(lc.Refus, match="nom permis interdit"):
        lc.environnement_permis({"PATH": "/bin"}, "GO-X")


# ============================================================================================ gardes reprises du v3

def test_drapeaux_sain_commande_production():
    lc.garde_drapeaux(lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h", PFX))


@pytest.mark.parametrize("drapeau", ["--accepter-sans-bac-a-sable", "--tolerer", "--bras-rapporte-differe",
                                     "--attestation-lecture-humaine=x", "--taille-max-consigne-externe=9"])
def test_drapeaux_artefact(monde, capsys, drapeau):
    monde["r"].arguments_en_plus = (drapeau,)
    code, err = lancer(monde, capsys)
    assert code == 2 and "interdit" in err and not monde["journal"].exists()


def test_sommes_sain_production():
    s = lc.garde_sommes(lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h", PFX))
    assert (s["somme_claude"], s["somme_externe"], s["exposition_externe_course"]) == (9.9, 7.6, 4.9)


@pytest.mark.parametrize("cle,valeur,motif", [("juge_ideation|gemini-4-argon", 3.0, "pas sous le total externe"),
                                              ("proposeur_ideation|claude-fable-5-1", 2.1, "Claude"),
                                              ("proposeur_ideation|gemini-4-argon", 1.4, "exposition")])
def test_sommes_artefacts(cle, valeur, motif):
    r = lc.Reglages.production()
    r.plafonds = dict(lc.PLAFONDS, **{cle: valeur})
    with pytest.raises(lc.Refus, match=motif):
        lc.garde_sommes(lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX))


@pytest.mark.parametrize("etat,motif", [("inactif", "inactif"), ("sans_proc", "/proc neuf"), ("illisible", "illisible"),
                                         ("erreur", "illisible")])
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
    r = lc.Reglages.production()
    if not (r.orchestrateur / lc.LANCEUR_ORCHESTRATEUR).is_file():
        pytest.skip("clone de l'orchestrateur absent")
    o = lc.verifier_orchestrateur(r)
    assert o["arbre"] == lc.ARBRE_ORCHESTRATEUR


def test_pieces_sain_depot_reel():
    assert set(lc.verifier_pieces(lc.Reglages.production())) == set(lc.PIECES)


def test_pieces_artefact(monde, capsys):
    (monde["depot"] / monde["r"].pieces["question"][0]).write_text("autre question\n")
    code, err = lancer(monde, capsys)
    assert code == 2 and "pièces" in err and not monde["journal"].exists()


@pytest.mark.parametrize("python,motif", [("python3", "non absolu"), ("/nulle/part/python3", "absent"),
                                          ("/bin/sh", "un seul interpréteur")])
def test_interprete_artefacts(monde, capsys, python, motif):
    monde["r"].python = python
    monde["r"].orig_argv = (python, "-I", "-B", f"scripts/{lc.FICHIER_LANCEUR}", "1")
    code, err = lancer(monde, capsys)
    assert code == 2 and motif in err and not monde["journal"].exists()


def test_ecrire_scelle_jamais_ecrase(tmp_path):
    p = tmp_path / "m.json"
    lc.ecrire_scelle(p, {"a": 1})
    with pytest.raises(lc.Refus, match="existe déjà"):
        lc.ecrire_scelle(p, {"a": 2})


def test_dossier_inattendu_dans_les_runs(monde, capsys):
    (monde["r"].dossier_runs / "autre-chose").mkdir(parents=True)
    code, err = lancer(monde, capsys)
    assert code == 2 and "inattendu" in err


def test_run_sans_manifeste(monde, capsys):
    (monde["r"].dossier_runs / ("20261114-010000" + lc.SUFFIXE_RUN + "1")).mkdir(parents=True)
    code, err = lancer(monde, capsys)
    assert code == 2 and "état inconnu" in err


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

def _clone_reel():
    r = lc.Reglages.production()
    if not (r.orchestrateur / lc.LANCEUR_ORCHESTRATEUR).is_file():
        pytest.skip("clone de l'orchestrateur absent")
    lc.verifier_orchestrateur(r)
    return r


def test_liste_blanche_et_mesure_contre_l_orchestrateur_reel(tmp_path):
    """Sans appel : modes `--construire-liste-blanche` et `--mesurer-consignes` de l'orchestrateur réel, sur les vraies
    pièces de la course ; gardes de taille ; le clone reste propre (fichiers ignorés compris)."""
    r = _clone_reel()
    fichiers = {str(r.depot / r.pieces[n][0]): r.pieces[n][1] for n in ("question", "faits", "temoins")}
    env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(tmp_path), "LANG": "C.UTF-8"}
    lb = lc.construire_liste_blanche(r, tmp_path / "liste-blanche.json", env, tmp_path / "pyc", fichiers)
    assert lb["sha256"] == sha(tmp_path / "liste-blanche.json")
    m, _ = lc.mesurer_consignes(r, lc.commande_mesure(r, tmp_path / "liste-blanche.json", tmp_path / "pyc"), env,
                                tmp_path / "mesure.json")
    g = lc.gardes_de_taille(m, r)
    assert g["course"]["marge"] > 0 and g["commande_argon"]["controle_externe"]["tient"]
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
                "juge_externe": ns.juge_externe, "pieces": ns.piece, "temoins": ns.temoins}
print(json.dumps(out))
'''


def test_analyseur_reel_accepte_les_deux_commandes(tmp_path):
    r = _clone_reel()
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
    assert out["course"]["moteur"] == "claude-sdk" and not out["course"]["bras"] and out["course"]["graine"] == 2026111401
    assert out["course"]["juge_externe"] == ["argon-juge=gemini-4-argon"]
    assert lc._git(r.orchestrateur, "status", "--porcelain", "--ignored").strip() == ""


# ============================================================================================ gardes de taille (calcul)

MESURE = {"sans_appel": True, "prix_entree_usd_par_million_jetons": 10.0,
          "consignes": {"consigne_de_controle_externe": 70000, "consigne_passe_1": 30000, "nombre_par_proposeur": 6},
          "garde_course": {"passerait": True}, "gardes_passes_externes": {"argon": {"passe_1": {"passerait": True}}}}


def test_tailles_sain():
    g = lc.gardes_de_taille(MESURE, lc.Reglages.production())
    assert g["course"]["marge"] > 0 and all(v["tient"] for v in g["commande_argon"].values())


@pytest.mark.parametrize("modif,motif", [({"consigne_de_controle_externe": 400001}, "course"),
                                         ({"nombre_par_proposeur": 8}, "--nombre")])
def test_tailles_artefacts(modif, motif):
    m = json.loads(json.dumps(MESURE))
    m["consignes"].update(modif)
    with pytest.raises(lc.Refus, match=motif):
        lc.gardes_de_taille(m, lc.Reglages.production())


def test_plancher_argon():
    assert lc.plancher_argon(0) == pytest.approx(0.509952)
