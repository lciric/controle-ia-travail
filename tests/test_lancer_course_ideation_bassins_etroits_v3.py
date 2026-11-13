"""Essais R5 de `scripts/lancer_course_ideation_bassins_etroits_v3.py` (trois générations, GO-2026-11-13-03), dérivés de ceux
du v2 (`4038ca4e…`) ; ajouts du v3 : environnement par liste de noms permis, relance étroite après un défaut au contrôle,
runs du v2 lus comme tentatives, verrou d'invocation (R1), orchestrateur orphelin (R2), exception au détachement du bras
(R4), compte rendu avant les gardes d'entrée (R9), et les quatre mutations survivantes de la vérification courte (zombie,
seuil, bras mort compté, bras sans code scellé).

Aucun modèle appelé, aucun réseau. Un **faux orchestrateur** (dépôt git jetable ; faux `demonstrations/ideation_v8.py` qui,
comme le vrai, écrit la liste blanche **et son compagnon**, rend une mesure des consignes, écrit une sortie de course ou de
bras scellée ; faux `pole/adaptateurs.py` dont la sonde rend l'état demandé) est servi au lanceur par `Reglages`. Le lanceur
détache l'orchestrateur sous un superviseur : les essais attendent le superviseur par son PID, puis relancent la même
commande, qui clôt. Trois essais **sans appel** contre l'orchestrateur réel (liste blanche, mesure, analyseur d'arguments)
tournent quand le clone est là, dans des processus à part, `-I -B`, cache d'octets hors du clone. Le bras n'est jamais
exécuté contre l'orchestrateur réel."""
from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "lancer_course_ideation_bassins_etroits_v3.py"
_spec = importlib.util.spec_from_file_location("lancer_course_ideation_bassins_etroits_v3", SCRIPT)
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
        sceller(argv[0], liste)               # comme l'orchestrateur réel : la liste et son compagnon (B1)
    sys.exit(0)
if "--mesurer-consignes" in argv:
    consigner("mesure")
    if os.environ.get("FAUX_MESURE_ILLISIBLE") == "1":
        print("pas du JSON")
        sys.exit(0)
    ctrl = int(os.environ.get("FAUX_CONTROLE", "322793"))
    print(json.dumps({"sans_appel": True, "prix_entree_usd_par_million_jetons": 10.0,
                      "consignes": {"consigne_de_controle_externe": ctrl, "consigne_passe_1": 56691,
                                    "consigne_passe_2_maximale": 322318, "consigne_du_juge_maximale": 1660189,
                                    "fiches_au_juge_au_maximum": 40, "nombre_par_proposeur": 6},
                      "garde_course": {"passerait": ctrl <= 400000},
                      "gardes_passes_externes": {"argon": {"passe_1": {"passerait": True}}}}))
    sys.exit(0)
sortie = argv[0]
if "--bras-rapporte-differe" in argv:
    consigner("bras")
    time.sleep(float(os.environ.get("FAUX_DORT_BRAS", "0")))
    mode = os.environ.get("FAUX_BRAS", "ok")
    if mode == "non_joue":
        n = 1 + len([x for x in os.listdir(sortie) if x.startswith("manifeste-bras-non-joue-") and x.endswith(".json")])
        sceller(os.path.join(sortie, f"manifeste-bras-non-joue-{n}.json"), {"reglages": {"journal": {"cout_total_usd": 0.0}}})
        sys.exit(2)
    if mode == "paye":
        n = 1 + len([x for x in os.listdir(sortie) if x.startswith("bras-tentative-") and x.endswith(".json")])
        sceller(os.path.join(sortie, f"bras-tentative-{n}.json"), {"reglages": {"journal": {"cout_total_usd": 0.4}}})
        sys.exit(2)
    lisible = mode == "ok"
    sceller(os.path.join(sortie, "manifeste-bras-rapporte.json"),
            {"reglages": {"journal": {"cout_total_usd": float(os.environ.get("FAUX_COUT_BRAS", "0.9"))}}})
    sceller(os.path.join(sortie, "doublons-bras-rapporte.json"), {"argon-juge": [["T02", "T03"]]})
    rangs = ["opus-p1-01", "opus-p2-01", "fable-p1-01", "argon-p1-01", "fable-p1-02", "argon-p2-02", "fable-p2-03",
             "fable-p1-04", "opus-p1-05"]
    lignes = [{"rang": k, "identifiant_auteur": i, "auteur": i.split("-p")[0], "eligible": k <= 8, "total": 15 - k}
              for k, i in enumerate(rangs, 1)]
    sceller(os.path.join(sortie, "classement.json"), {"lisible_L2_L4": lisible, "lignes": lignes})
    sys.exit(0 if lisible else 4)
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
ids = ["opus-p1-01", "opus-p2-01", "fable-p1-01", "argon-p1-01", "fable-p1-02", "argon-p2-02", "fable-p2-03",
       "fable-p1-04", "opus-p1-05"]
grand = int(os.environ.get("FAUX_GRANDE", "0"))
fiches = [{"identifiant_auteur": i, "auteur": i.split("-p")[0], "passe": int(i.split("-p")[1][0]), "nom": "Idée " + i,
           "enonce": ("x" * grand if i == "fable-p1-01" else "énoncé de " + i),
           "empreinte": hashlib.sha256(i[::-1].encode()).hexdigest()} for i in ids]
sceller(os.path.join(sortie, "fiches-validees.json"), fiches)
sceller(os.path.join(sortie, "noyau", "temoins-servis.json"), [{"identifiant_auteur": "temoin-p0-01"}])
sceller(os.path.join(sortie, "noyau", "cles-anonymisation-par-juge.json"),
        {"opus-juge": {"T01": "fable-p1-01", "T02": "argon-p2-02", "T03": "opus-p1-05"},
         "argon-juge": {"T01": "opus-p1-01", "T02": "argon-p1-01", "T03": "fable-p1-02"}})
sceller(os.path.join(sortie, "doublons-par-juge.json"), {"opus-juge": [["T02", "T03"]]})
sceller(os.path.join(sortie, "juges-bras-rapporte", "traces-argon-juge", "consigne-en-attente.md"),
        texte="consigne du juge " * int(os.environ.get("FAUX_JUGE_REPET", "1000")))
sceller(os.path.join(sortie, "lecture-course.json"),
        {"bras_rapporte_differe": [{"etiquette": "argon-juge", "consigne_en_attente_sha256": "c" * 64}]})
conv = {"opus": {"opus-p1-01": {"identifiant_passe_1": "opus-p1-01", "identifiant_passe_2": "opus-p2-01"}}}
sceller(os.path.join(sortie, "manifeste-fin.json"),
        {"reglages": {"journal": {"cout_total_usd": float(os.environ.get("FAUX_COUT_CLAUDE", "2.5")),
                                  "cout_externe_usd": float(os.environ.get("FAUX_COUT_EXTERNE", "2.0"))},
                      "en_attente_bras": True, "statut_course": {"statut": "ok" if code == 0 else "erreur"},
                      "mesures_convergence": {"par_proposeur": conv}}})
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

GO_LIGNE = ("| GO-2026-11-13-03 | 2026-11-13 | calcul | **Organisme d'idéation, atelier d'idées (N-065, rôle 2), sur la question "
            "des bassins d'idées étroits et profonds : trois générations** | 60 USD | 2026-11-30 | Lazar | R-2530 |")
PFX = Path("/x/sortie/pycache")


def git(d, *a):
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sceller(p: Path, texte: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    Path(str(p) + ".sha256").write_text(f"{sha(p)}  {p.name}\n")


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
    commit = subprocess.run(["git", "-C", str(orch), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    depot = tmp_path / "depot"
    pieces = {}
    for nom, (rel, _) in lc.PIECES.items():
        p = depot / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"pièce factice {nom}\n")
        pieces[nom] = (rel, sha(p))
    sceller(depot / lc.RECOUPEMENT, "# Recoupement factice\n\nméthodes recoupées\n")
    relecture(depot)
    sceller(depot / lc.CONFIRMATION_REGLE, "Mot de Lazar recopié (factice d'essai).\n")
    (depot / "registres").mkdir()
    (depot / "registres" / "go.md").write_text("| id | a | t | p | pl | e | par | ref |\n|---|\n" + GO_LIGNE + "\n")
    journal = tmp_path / "journal.jsonl"
    env = {"PATH": "/usr/bin:/bin", "HOME": str(tmp_path), "FAUX_JOURNAL": str(journal), "FAUX_BAC": "actif",
           "ANTHROPIC_API_KEY": "valeur-factice-d-essai", "AUTRE_SECRET_X": "factice", "LANG": "C.UTF-8",
           "CLAUDE_CODE_REMOTE": "true", "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST": "1", "ANTHROPIC_BASE_URL": "http://hote.invalid",
           "CCR_AGENT_PROXY_ENABLED": "1", "HTTPS_PROXY": "http://mandataire.invalid", "NODE_OPTIONS": "--x"}
    horloge = {"t": dt.datetime(2026, 11, 13, 14, 0, 0, tzinfo=dt.timezone.utc)}

    def maintenant():
        horloge["t"] += dt.timedelta(seconds=1)
        return horloge["t"]
    r = lc.Reglages(depot=depot, orchestrateur=orch, commit_orchestrateur=commit,
                    empreintes_orchestrateur={"demonstrations/ideation_v8.py": sha(orch / "demonstrations/ideation_v8.py"),
                                              "pole/adaptateurs.py": sha(orch / "pole/adaptateurs.py")},
                    pieces=pieces, registre_go=depot / "registres" / "go.md", dossier_runs=depot / "runs" / "course-x",
                    dossier_sorties=tmp_path / "sorties", depot_attendu_par_l_enveloppe=depot, python=sys.executable,
                    environnement=env, aujourd_hui=dt.date(2026, 11, 13), horodatage=lambda: "Fri Nov 13 14:00:00 UTC 2026",
                    maintenant=maintenant, prefixe_essais="FAUX_")
    yield {"r": r, "journal": journal, "env": env, "tmp": tmp_path, "depot": depot}
    for pid in superviseurs(r):                       # jamais par motif : par PID, ceux de cet essai seulement
        try:
            os.kill(pid, signal.SIGKILL)
            os.waitpid(pid, 0)
        except (ProcessLookupError, ChildProcessError):
            pass


def relecture(depot, **modif):
    a = {"lecteur": "la mère (essai)", "lu_le": "2026-11-13", "recoupement_sha256": sha(depot / lc.RECOUPEMENT),
         "niveau_methode_aucune_recette_aucun_secret": True, "temoin_vrai_absent": True}
    a.update(modif)
    p = depot / lc.RELECTURE_RECOUPEMENT
    if p.exists():
        p.unlink()
        Path(str(p) + ".sha256").unlink()
    sceller(p, json.dumps(a))


def superviseurs(r):
    pids = []
    if r.dossier_runs.is_dir():
        for d in r.dossier_runs.iterdir():
            for f in d.glob("manifeste-lanceur-*depart*.json"):
                try:
                    pids.append(json.loads(f.read_text())["superviseur"]["pid"])
                except (KeyError, ValueError):
                    pass
    return pids


def attendre(monde):
    for pid in superviseurs(monde["r"]):
        try:
            os.waitpid(pid, 0)
        except ChildProcessError:
            pass


def journal(monde):
    if not monde["journal"].exists():
        return []
    return [json.loads(x) for x in monde["journal"].read_text().splitlines()]


def lancer(monde, g, capsys=None):
    code = lc.principal([str(g)], monde["r"])
    sortie = capsys.readouterr() if capsys else None
    return code, (sortie.err + sortie.out) if sortie else ""


def jouer(monde, g, capsys=None):
    """Lancement détaché, attente du superviseur par son PID, clôture par la même commande."""
    c1, t1 = lancer(monde, g, capsys)
    if c1 != 0:
        return c1, t1
    attendre(monde)
    c2, t2 = lancer(monde, g, capsys)
    assert c2 == 0 and "clôture" in t2, t2
    return c2, t1 + t2


def run_de(monde, g):
    return [x for x in lc.runs_du_lanceur(monde["r"]) if x["generation"] == g]


def attester(monde, g, version=1, **modif):
    run = [x for x in run_de(monde, g) if lc.course_reussie(x)][0]
    a = {"lecteur": "la mère (essai)", "lu_le": "2026-11-13", "fiches_validees_sha256": sha(run["sortie"] / "fiches-validees.json"),
         "consignes_en_attente_sha256": {"argon-juge": "c" * 64}, "temoin_vrai_absent_des_fiches_validees": True}
    a.update(modif)
    sceller(monde["depot"] / lc.ATTESTATIONS / f"attestation-lecture-humaine-g{g}-v{version}.json", json.dumps(a))
    return run


def generation_complete(monde, g, capsys):
    assert jouer(monde, g, capsys)[0] == 0
    attester(monde, g)
    assert jouer(monde, g, capsys)[0] == 0


# ============================================================================================ argument unique et fermé

@pytest.mark.parametrize("argv", [[], ["4"], ["0"], ["1", "2"], ["--accepter-sans-bac-a-sable"], ["01"], [" 1"], ["un"]])
def test_argument_artefacts(monde, capsys, argv):
    assert lc.principal(argv, monde["r"]) == 2
    assert "un seul argument" in capsys.readouterr().err and not monde["journal"].exists()


# ============================================================================================ chaîne saine de bout en bout

def test_trois_generations_bout_en_bout(monde, capsys):
    r = monde["r"]
    for g in (1, 2, 3):
        assert jouer(monde, g, capsys)[0] == 0                       # course détachée, puis clôture
        runs = run_de(monde, g)
        assert len(runs) == 1 and lc.course_reussie(runs[0])
        code, err = lancer(monde, g, capsys)                         # bras sans attestation : refus
        assert code == 2 and "attestation" in err
        attester(monde, g)
        assert jouer(monde, g, capsys)[0] == 0                       # bras
        assert lc.bras_reussi(run_de(monde, g)[0])
    modes = [j["mode"] for j in journal(monde)]
    assert modes == ["mesure", "course", "bras"] * 3
    courses = [j for j in journal(monde) if j["mode"] == "course"]
    for k, j in enumerate(courses, 1):
        a = j["argv"]
        assert j["noms_cle"] == [] and j["go_id"] == "GO-2026-11-13-03"
        assert {n for n in j["noms_env"] if not n.startswith("FAUX_")} <= set(lc.NOMS_PERMIS) | {"HOME", "GO_ID",
                                                                                                "PYTHONPYCACHEPREFIX"}
        assert {"PATH", "LANG", "HOME", "GO_ID"} <= set(j["noms_env"])
        assert j["home"].endswith("/home") and str(monde["tmp"] / "sorties") in j["home"]
        assert j["sid"] != os.getsid(0)                               # M7 : session de processus neuve
        assert "--accepter-sans-bac-a-sable" not in a and not any(x.startswith("--tolerer") for x in a)
        assert a[a.index("--nombre") + 1] == "6" and a[a.index("--graine") + 1] == str(2026111300 + k)
        assert a[a.index("--budget-controle-externe-usd") + 1] == "1.7"
        assert a[a.index("--budget-passe-2-externe-usd") + 1] == "1.9"
        pieces = [a[i + 1] for i, x in enumerate(a) if x == "--piece"]
        assert pieces[1].endswith("recoupement-methodes-v1.md" if k == 1 else f"fiches-recues-g{k - 1}-pour-g{k}.md")
        assert [a[i + 1] for i, x in enumerate(a) if x == "--piece-juge"] == pieces
        assert j["orig_argv"][1:3] == ["-I", "-B"] and j["pycache_prefix"]
    bras = [j for j in journal(monde) if j["mode"] == "bras"]
    for b in bras:
        a = b["argv"]
        assert a[a.index("--budget-controle-usd") + 1] == "0.6" and a[a.index("--moteur") + 1] == "claude-sdk"
        assert "--confirmer-moteur-reel" in a
    code, err = lancer(monde, 3, capsys)
    assert code == 2 and "déjà jouée" in err
    runs = lc.runs_du_lanceur(r)
    dep = json.loads((runs[0]["dossier"] / "manifeste-lanceur-depart.json").read_text())
    exclus = dep["environnement"]["noms_exclus"]
    for n in ("ANTHROPIC_API_KEY", "AUTRE_SECRET_X", "CLAUDE_CODE_REMOTE", "ANTHROPIC_BASE_URL", "CCR_AGENT_PROXY_ENABLED",
              "HTTPS_PROXY", "NODE_OPTIONS", "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"):
        assert n in exclus
    assert [n for n in dep["environnement"]["noms_transmis"] if not n.startswith("FAUX_")] == sorted(
        ["GO_ID", "HOME", "LANG", "PATH", "PYTHONPYCACHEPREFIX"])
    texte = (runs[0]["dossier"] / "manifeste-lanceur-depart.json").read_text()
    assert "valeur-factice-d-essai" not in texte and "hote.invalid" not in texte and "mandataire.invalid" not in texte
    assert dep["plafonds"]["sommes"]["somme_externe"] == 7.6 and dep["plafonds"]["sommes"]["somme_claude"] == 9.9
    assert dep["piece_variable"]["relecture"]["lecteur"] == "la mère (essai)"
    assert dep["liste_blanche"]["compagnon"].startswith("écrit par l'orchestrateur")
    dep3 = json.loads((runs[2]["dossier"] / "manifeste-lanceur-depart.json").read_text())
    assert dep3["garde_de_cumul"]["depense_relevee_usd"] == pytest.approx(2 * (2.5 + 2.0 + 0.9))
    fin1 = json.loads((runs[0]["dossier"] / "manifeste-lanceur-fin.json").read_text())
    assert fin1["code"] == 0 and fin1["pour_l_attestation"]["consignes_en_attente_sha256"] == {"argon-juge": "c" * 64}
    for x in runs:
        for f in x["dossier"].glob("*.json"):
            h, nom = Path(str(f) + ".sha256").read_text().split()
            assert nom == f.name and h == sha(f)
        assert not str(x["sortie"]).startswith(str(monde["depot"]))


# ============================================================================================ B1 : compagnon de la liste blanche

def test_b1_compagnon_ecrit_par_l_orchestrateur_verifie(monde, capsys):
    assert lancer(monde, 1, capsys)[0] == 0
    d = lc.runs_du_lanceur(monde["r"])[0]["dossier"]
    assert lc.lire_scelle(d / "liste-blanche.json")


@pytest.mark.parametrize("variable,motif", [("FAUX_LB_SANS_SCEAU", "compagnon"), ("FAUX_LB_AUTRE", "différente")])
def test_b1_artefacts_liste_blanche(monde, capsys, variable, motif):
    monde["env"][variable] = "1"
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and motif in err
    run = lc.runs_du_lanceur(monde["r"])[0]
    assert run["refus"] and run["depart"] is None and [j["mode"] for j in journal(monde)] == []


def _clone_reel():
    r = lc.Reglages.production()
    if not (r.orchestrateur / lc.LANCEUR_ORCHESTRATEUR).is_file():
        pytest.skip("clone de l'orchestrateur absent")
    lc.verifier_orchestrateur(r)
    return r


def test_b1_liste_blanche_et_mesure_contre_l_orchestrateur_reel(tmp_path):
    """Sans appel : modes `--construire-liste-blanche` et `--mesurer-consignes` de l'orchestrateur réel, à travers les
    fonctions du lanceur ; le clone reste propre (fichiers ignorés compris)."""
    r = _clone_reel()
    piece = tmp_path / "piece" / "recoupement-gabarit.md"
    piece.parent.mkdir()
    piece.write_text("Matériau factice de gabarit.\n" * 1200, encoding="utf-8")
    fichiers = {str(r.depot / r.pieces[n][0]): r.pieces[n][1] for n in ("question", "faits", "temoins")}
    fichiers[str(piece)] = sha(piece)
    env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": str(tmp_path), "LANG": "C.UTF-8"}
    lb = lc.construire_liste_blanche(r, tmp_path / "liste-blanche.json", env, tmp_path / "pyc", fichiers)
    assert lb["sha256"] == sha(tmp_path / "liste-blanche.json")
    m = lc.mesurer_consignes(r, lc.commande_mesure(r, tmp_path / "liste-blanche.json", tmp_path / "pyc", piece), env,
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
    out[nom] = {"inconnus": inconnus, "moteur": ns.moteur, "bras": ns.bras_rapporte_differe,
                "controle": ns.budget_controle_usd, "commande_externe": bool(ns.commande_externe),
                "juge_externe": ns.juge_externe, "attestation": bool(ns.attestation_lecture_humaine)}
print(json.dumps(out))
'''


def test_analyseur_reel_accepte_les_trois_commandes(tmp_path):
    """Sans appel : l'analyseur d'arguments réel, dans un processus à part, sur les trois commandes construites ; rien
    n'est lancé (le bras n'est jamais exécuté)."""
    r = _clone_reel()
    pfx = tmp_path / "pyc"
    cmds = {"course": lc.commande_course(r, Path("/x/sortie"), Path("/x/lb.json"), "h", pfx, Path("/x/p.md"), 1),
            "mesure": lc.commande_mesure(r, Path("/x/lb.json"), pfx, Path("/x/p.md")),
            "bras": lc.commande_bras(r, Path("/x/sortie"), Path("/x/lb.json"), Path("/x/a.json"), "h", pfx)}
    p = subprocess.run([r.python, "-I", "-B", "-X", f"pycache_prefix={tmp_path / 'pyc-analyseur'}", "-c", ANALYSEUR,
                        str(r.orchestrateur), json.dumps({k: v[6:] for k, v in cmds.items()})],
                       capture_output=True, text=True, timeout=120, cwd=str(tmp_path),
                       env={"PATH": "/usr/bin:/bin", "HOME": str(tmp_path)})
    assert p.returncode == 0, p.stderr[-800:]
    out = json.loads(p.stdout)
    assert all(v["inconnus"] == [] for v in out.values())
    assert out["bras"]["moteur"] == "claude-sdk" and out["bras"]["bras"] and out["bras"]["controle"] == 0.6
    assert out["bras"]["commande_externe"] and out["bras"]["attestation"]
    assert lc._git(r.orchestrateur, "status", "--porcelain", "--ignored").strip() == ""


# ============================================================================================ M7 : détaché, PID, clôture

def test_m7_en_marche_rien_ne_part(monde, capsys):
    monde["env"]["FAUX_DORT"] = "3"
    assert lancer(monde, 1, capsys)[0] == 0
    code, sortie = lancer(monde, 1, capsys)
    assert code == 3 and "en marche" in sortie and "kill -TERM" in sortie
    assert lancer(monde, 2, capsys)[0] == 3                         # aucune autre génération non plus
    attendre(monde)
    assert [j["mode"] for j in journal(monde)] == ["mesure", "course"]
    code, sortie = lancer(monde, 1, capsys)
    assert code == 0 and "clôture" in sortie
    assert lc.course_reussie(run_de(monde, 1)[0])


def test_m7_mort_sans_fin_propre(monde, capsys):
    monde["env"]["FAUX_DORT"] = "30"
    assert lancer(monde, 1, capsys)[0] == 0
    run = run_de(monde, 1)[0]
    sup = run["depart"]["superviseur"]
    assert lc.superviseur_vivant(sup)
    p = _tuer_superviseur(monde, sup)                                 # par PID (R10)
    os.kill(p["pid_orchestrateur"], signal.SIGKILL)                   # l'orchestrateur aussi (orphelin : voir R2)
    for _ in range(100):
        if lc.debut_processus(p["pid_orchestrateur"]) is None:
            break
        time.sleep(0.05)
    code, sortie = lancer(monde, 1, capsys)
    assert code == 0 and "mort sans fin propre" in sortie
    fin = json.loads((run["dossier"] / "manifeste-lanceur-fin.json").read_text())
    assert fin["code"] is None and fin["orchestrateur_orphelin"] is None
    assert lc.depense_run(run_de(monde, 1)[0])["course_usd"] == 20.0
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "verrouillée" in err


def test_m7_arret_par_pid_relaye(monde, capsys):
    monde["env"]["FAUX_DORT"] = "30"
    assert lancer(monde, 1, capsys)[0] == 0
    sup = run_de(monde, 1)[0]["depart"]["superviseur"]
    pidf = Path(sup["dossier"]) / "pid-orchestrateur.json"
    for _ in range(100):
        if pidf.exists():
            break
        time.sleep(0.05)
    os.kill(sup["pid"], signal.SIGTERM)                              # relayé par PID à l'orchestrateur
    os.waitpid(sup["pid"], 0)
    code = json.loads((Path(sup["dossier"]) / "code.json").read_text())["code"]
    assert code == -signal.SIGTERM


def test_m7_superviseur_vivant_pid_reutilise():
    assert lc.superviseur_vivant({"pid": os.getpid(), "debut_proc": lc.debut_processus(os.getpid())})
    assert not lc.superviseur_vivant({"pid": os.getpid(), "debut_proc": "0"})
    assert not lc.superviseur_vivant({"pid": 2 ** 22 + 7, "debut_proc": "1"})


def test_v2_zombie_tenu_pour_mort():
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
    assert etat == "Z"                                                  # fini, non récolté
    assert not lc.superviseur_vivant({"pid": p.pid, "debut_proc": debut})
    p.wait()


def test_r1_verrou_deux_invocations(monde, capsys):
    import fcntl
    monde["r"].dossier_sorties.mkdir(parents=True)
    fd = os.open(monde["r"].dossier_sorties / lc.NOM_VERROU, os.O_CREAT | os.O_RDWR)
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)                     # une autre invocation tient le verrou
    try:
        code, err = lancer(monde, 1, capsys)
        assert code == 2 and "verrou" in err and not monde["journal"].exists()
    finally:
        os.close(fd)
    assert lancer(monde, 1, capsys)[0] == 0                             # libéré : la course part
    code, sortie = lancer(monde, 1, capsys)
    assert code in (0, 3)


def test_r1_verrou_non_herite_par_le_superviseur(monde, capsys):
    import fcntl
    monde["env"]["FAUX_DORT"] = "3"
    assert lancer(monde, 1, capsys)[0] == 0
    fd = os.open(monde["r"].dossier_sorties / lc.NOM_VERROU, os.O_RDWR)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)                 # le superviseur vivant ne le tient pas
    finally:
        os.close(fd)
    attendre(monde)


def _tuer_superviseur(monde, sup):
    pidf = Path(sup["dossier"]) / "pid-orchestrateur.json"
    for _ in range(100):
        if pidf.exists() and Path(str(pidf) + ".sha256").exists():
            break
        time.sleep(0.05)
    os.kill(sup["pid"], signal.SIGKILL)
    os.waitpid(sup["pid"], 0)
    return json.loads(pidf.read_text())


def test_r2_orchestrateur_orphelin(monde, capsys):
    monde["env"]["FAUX_DORT"] = "30"
    assert lancer(monde, 1, capsys)[0] == 0
    sup = run_de(monde, 1)[0]["depart"]["superviseur"]
    p = _tuer_superviseur(monde, sup)
    assert p["debut_proc"]
    code, sortie = lancer(monde, 1, capsys)
    assert code == 4 and "ORCHESTRATEUR ENCORE VIVANT" in sortie and f"kill -TERM {p['pid_orchestrateur']}" in sortie
    code, sortie = lancer(monde, 2, capsys)
    assert code == 4 and "orphelin" in sortie                           # rien ne part tant qu'il vit
    os.kill(p["pid_orchestrateur"], signal.SIGKILL)                     # par PID
    for _ in range(100):
        if lc.debut_processus(p["pid_orchestrateur"]) is None:
            break
        time.sleep(0.05)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "sans fin propre" in err


def test_v10_v16_bras_mort_compte_et_verrouille(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    monde["env"]["FAUX_DORT_BRAS"] = "30"
    assert lancer(monde, 1, capsys)[0] == 0
    run = run_de(monde, 1)[0]
    sup = run["bras"][0]["depart"]["superviseur"]
    p = _tuer_superviseur(monde, sup)
    os.kill(p["pid_orchestrateur"], signal.SIGKILL)
    for _ in range(100):
        if lc.debut_processus(p["pid_orchestrateur"]) is None:
            break
        time.sleep(0.05)
    assert lc.depense_run(run_de(monde, 1)[0])["bras_usd"] == pytest.approx(lc.PLAFOND_BRAS_USD)     # V10
    code, sortie = lancer(monde, 1, capsys)
    assert code == 0 and "mort sans fin propre" in sortie
    assert lc.depense_run(run_de(monde, 1)[0])["bras_usd"] == pytest.approx(lc.PLAFOND_BRAS_USD)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "un bras sans fin propre" in err                                         # V16


def test_r4_exception_au_detachement_du_bras(monde, capsys, monkeypatch):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    def panne(*a, **k):
        raise OSError("panne simulée")
    monkeypatch.setattr(lc, "lancer_detache", panne)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "exception au détachement" in err
    monkeypatch.undo()
    assert jouer(monde, 1, capsys)[0] == 0
    assert lc.bras_reussi(run_de(monde, 1)[0])


def test_r9_compte_rendu_apres_echeance_du_go(monde, capsys):
    monde["env"]["FAUX_DORT"] = "3"
    assert lancer(monde, 1, capsys)[0] == 0
    monde["r"].aujourd_hui = dt.date(2026, 12, 1)
    code, sortie = lancer(monde, 1, capsys)
    assert code == 3 and "en marche" in sortie
    attendre(monde)
    code, sortie = lancer(monde, 1, capsys)
    assert code == 0 and "clôture" in sortie
    code, err = lancer(monde, 2, capsys)
    assert code == 2 and "période" in err


# ============================================================================================ règle de passage (M4)

def test_regle_de_passage(monde, capsys):
    generation_complete(monde, 1, capsys)
    run = run_de(monde, 1)[0]
    choix = lc.choisir_fiches_recues(run["sortie"], 1)
    # rang 2 (opus-p2-01, autre passe d'opus-p1-01, non signalée en doublon) est prise ; rang 5 (fable-p1-02) : doublon
    # explicite d'argon-p1-01 chez argon-juge
    assert choix["ordre_de_prise"] == ["opus-p1-01", "opus-p2-01", "fable-p1-01", "argon-p1-01", "argon-p2-02"]
    assert [s["identifiant"] for s in choix["sautees"]] == ["fable-p1-02"]
    fiches = {f["identifiant_auteur"]: f for f in json.loads((run["sortie"] / "fiches-validees.json").read_text())}
    ordre = [p["identifiant"] for p in choix["prises"]]
    assert ordre == sorted(ordre, key=lambda i: fiches[i]["empreinte"])
    t = choix["texte"]
    for interdit in ('"identifiant_auteur"', '"empreinte"', '"auteur"', '"rang"', '"total"', '"passe"', '"eligible"'):
        assert interdit not in t
    assert "n'est pas un rang" in t and len(t) == choix["taille_caracteres"] <= lc.TAILLE_MAX_FICHES_RECUES


def test_regle_de_passage_n_emploie_pas_les_mesures_de_convergence(monde, capsys):
    generation_complete(monde, 1, capsys)
    s = run_de(monde, 1)[0]["sortie"]
    avant = lc.choisir_fiches_recues(s, 1)["ordre_de_prise"]
    p = s / "manifeste-fin.json"
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    assert lc.choisir_fiches_recues(s, 1)["ordre_de_prise"] == avant


def test_regle_de_passage_plafond_de_la_piece_entiere(monde, capsys):
    monde["env"]["FAUX_GRANDE"] = str(lc.TAILLE_MAX_FICHES_RECUES - 600)
    generation_complete(monde, 1, capsys)
    choix = lc.choisir_fiches_recues(run_de(monde, 1)[0]["sortie"], 1)
    assert "fable-p1-01" not in choix["ordre_de_prise"]
    assert any(s["identifiant"] == "fable-p1-01" and s["motif"].startswith("pièce") for s in choix["sautees"])
    assert choix["taille_caracteres"] <= lc.TAILLE_MAX_FICHES_RECUES


@pytest.mark.parametrize("fichier,contenu,motif", [
    ("doublons-bras-rapporte.json", {"argon-juge": [["T09", "T02"]]}, "mal formés"),
    ("doublons-bras-rapporte.json", {}, "juges attendus"),
    ("classement.json", {"lisible_L2_L4": True, "lignes": [{"identifiant_auteur": "x"}]}, "mal formés"),
    ("classement.json", {"lisible_L2_L4": False, "lignes": []}, "illisible"),
    ("classement.json", {"lisible_L2_L4": True, "lignes": [{"rang": 1, "identifiant_auteur": "opus-p1-01",
                                                             "eligible": False}]}, "aucune fiche"),
])
def test_regle_de_passage_artefacts(monde, capsys, fichier, contenu, motif):
    generation_complete(monde, 1, capsys)
    s = run_de(monde, 1)[0]["sortie"]
    (s / fichier).unlink()
    Path(str(s / fichier) + ".sha256").unlink()
    sceller(s / fichier, json.dumps(contenu))
    with pytest.raises(lc.Refus, match=motif):
        lc.choisir_fiches_recues(s, 1)


def test_regle_de_passage_sceau_faux(monde, capsys):
    generation_complete(monde, 1, capsys)
    s = run_de(monde, 1)[0]["sortie"]
    p = s / "classement.json"
    p.write_text(p.read_text().replace('"eligible": false', '"eligible": true'))
    with pytest.raises(lc.Refus, match="sceau faux"):
        lc.choisir_fiches_recues(s, 1)


# ============================================================================================ enchaînement, M5, M9

def test_generation_2_sans_generation_1(monde, capsys):
    code, err = lancer(monde, 2, capsys)
    assert code == 2 and "génération 1" in err and not monde["journal"].exists()


def test_m5_generation_2_sans_confirmation(monde, capsys):
    generation_complete(monde, 1, capsys)
    p = monde["depot"] / lc.CONFIRMATION_REGLE
    p.unlink()
    code, err = lancer(monde, 2, capsys)
    assert code == 2 and "confirmation-regle-de-passage" in err
    assert [j["mode"] for j in journal(monde)].count("course") == 1


def test_m9_temoin_vrai_present_dans_les_fiches(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1, temoin_vrai_absent_des_fiches_validees=False)
    assert jouer(monde, 1, capsys)[0] == 0
    code, err = lancer(monde, 2, capsys)
    assert code == 2 and "témoin vrai" in err


def test_generation_3_apres_seule_course_2(monde, capsys):
    generation_complete(monde, 1, capsys)
    assert jouer(monde, 2, capsys)[0] == 0
    code, err = lancer(monde, 3, capsys)
    assert code == 2 and "génération 2" in err


# ============================================================================================ M1, M2 : relances de la course

def test_pas_de_relance_apres_des_fiches(monde, capsys):
    monde["env"]["FAUX_CODE"] = "2"                                     # course en défaut après avoir produit des fiches
    assert jouer(monde, 1, capsys)[0] == 0
    monde["env"]["FAUX_CODE"] = "0"
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "fiches" in err and "verrouillée" in err
    assert [j["mode"] for j in journal(monde)] == ["mesure", "course"]


def test_relance_unique_apres_defaut_au_controle(monde, capsys):
    """Le cas de la génération 1 du v2 : contrôle d'Argon payé, contrôles Claude refusés, aucune fiche."""
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", "0.275477"
    assert jouer(monde, 1, capsys)[0] == 0
    assert lc.relance_permise(run_de(monde, 1))[0]
    assert jouer(monde, 1, capsys)[0] == 0                              # seconde course : permise, une fois
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "2 courses déjà parties" in err               # jamais une troisième
    dep = json.loads((run_de(monde, 1)[1]["dossier"] / "manifeste-lanceur-depart.json").read_text())
    assert dep["garde_de_cumul"]["depense_relevee_usd"] == pytest.approx(0.275477)
    assert dep["relance"].startswith("1 course")


def test_relance_puis_succes(monde, capsys):
    monde["env"]["FAUX_CONTROLE_SEUL"], monde["env"]["FAUX_COUT_CONTROLE"] = "plancher", "0.3"
    assert jouer(monde, 1, capsys)[0] == 0
    del monde["env"]["FAUX_CONTROLE_SEUL"]
    assert jouer(monde, 1, capsys)[0] == 0
    assert lc.course_reussie(run_de(monde, 1)[1])


def test_v3_seuil_mutation_deux_courses_au_plus(monde, capsys):
    """Mutant V3 de la vérification courte (relance permise à faible dépense) : ici, une dépense nulle ne donne pas une
    troisième course."""
    monde["env"]["FAUX_CODE"], monde["env"]["FAUX_RIEN"] = "2", "1"
    assert jouer(monde, 1, capsys)[0] == 0
    assert jouer(monde, 1, capsys)[0] == 0
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "2 courses" in err


def test_relance_refusee_si_depense_illisible(monde, capsys):
    monde["env"]["FAUX_CONTROLE_SEUL"] = "interrompu"
    assert jouer(monde, 1, capsys)[0] == 0
    d = lc.depense_run(run_de(monde, 1)[0])
    assert d["course_usd"] == 20.0 and not d["course_lisible"] and "sans tentative scellée" in d["lecture"]
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "dépense illisible" in err


@pytest.mark.parametrize("contenus,attendu", [((None, None, None), False), (([], [], []), False), (([1], [], []), True),
                                              (([], [{"x": 1}], []), True), (("pas une liste", [], []), None)])
def test_fiches_produites(tmp_path, contenus, attendu):
    s = tmp_path / "sortie"
    if contenus[0] is not None:
        for nom, c in zip(("fiches-validees.json", "fiches-refusees.json", "fiches-en-quarantaine.json"), contenus):
            sceller(s / nom, json.dumps(c))
    assert lc.fiches_produites(s) is attendu
    if contenus[0] is None:
        s.mkdir()
        assert lc.fiches_produites(s) is None                           # sortie sans listes : non prouvé


def test_run_anterieur_v2_compte_comme_premiere_tentative(monde, capsys):
    """Un run de la forme du v2 (version, dossier et suffixe du v2), en défaut au contrôle : lu par le v3, compté au cumul,
    première des deux courses."""
    ant = monde["tmp"] / "runs-v2"
    nom = "20261113-152926" + lc.ANTERIEURS[0][1] + "1"
    d = ant / nom
    d.mkdir(parents=True)
    so = monde["tmp"] / "sorties-v2" / nom
    sup = so / "superviseur-course"
    sup.mkdir(parents=True)
    sceller(sup / "code.json", json.dumps({"code": 2, "pid_orchestrateur": 1}))
    c = so / "sortie-controle"
    (c / "tentative-1").mkdir(parents=True)
    (c / "tentative-1-externe-argon").mkdir()
    sceller(c / "tentative-1.json", json.dumps({"reglages": {"cout_claude_usd": 0.0, "cout_externe_usd": 0.275477}}))
    socle = {"lanceur": {"version": lc.ANTERIEURS[0][2]}, "generation": 1, "sortie": str(so / "sortie")}
    sceller(d / "manifeste-lanceur-depart.json", json.dumps(dict(socle, superviseur={
        "pid": 2 ** 22 + 11, "debut_proc": "1", "dossier": str(sup), "arret": "kill"})))
    sceller(d / "manifeste-lanceur-fin.json", json.dumps({"code": 2, "issue": "fin propre"}))
    monde["r"].anterieurs = ((ant, lc.ANTERIEURS[0][1], lc.ANTERIEURS[0][2]),)
    runs = lc.runs_du_lanceur(monde["r"])
    assert [x["version"] for x in runs] == [lc.ANTERIEURS[0][2]]
    assert lc.depense_run(runs[0])["course_usd"] == pytest.approx(0.275477)
    monde["env"]["FAUX_CODE"], monde["env"]["FAUX_RIEN"] = "2", "1"
    assert jouer(monde, 1, capsys)[0] == 0                              # la seconde course
    v3 = [x for x in run_de(monde, 1) if x["version"] == lc.VERSION]
    assert len(v3) == 1
    dep = json.loads((v3[0]["dossier"] / "manifeste-lanceur-depart.json").read_text())
    assert dep["garde_de_cumul"]["depense_relevee_usd"] == pytest.approx(0.275477)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "2 courses" in err
    assert lc.garde_cumul(lc.runs_du_lanceur(monde["r"]), 20.0, 60.0)["depense_relevee_usd"] == pytest.approx(0.275477)


def test_run_reel_du_v2_reconnu():
    """Le dépôt réel : le run du v2 (génération 1, défaut au contrôle) est la première tentative, 0,275477 USD."""
    r = lc.Reglages.production()
    nom = "20261113-152926-course-ideation-bassins-etroits-v2-g1"
    if not (RACINE / "runs" / lc.ANTERIEURS[0][0] / nom).is_dir():
        pytest.skip("run du v2 absent du dépôt")
    runs = [x for x in lc.runs_du_lanceur(r) if x["generation"] == 1]
    v2 = [x for x in runs if x["nom"] == nom]
    assert len(v2) == 1, "le run du v2 présent sur disque doit être lu par le v3"
    assert lc.depense_run(v2[0]) == {"run": v2[0]["nom"], "course_usd": 0.275477, "bras_usd": 0.0, "course_lisible": True,
                                     "lecture": "course : tentatives de contrôle scellées (course non partie) ; bras : aucun bras"}
    assert lc.fiches_produites(v2[0]["sortie"]) is False
    if len(runs) == 1:
        assert lc.relance_permise(runs)[0]


def test_relance_refusee_sans_fin_propre_au_manifeste(tmp_path):
    """État incohérent : code scellé par le superviseur, mais manifeste de fin du lanceur sans code. La relance est
    refusée par la garde « fin propre » elle-même (la dépense, elle, serait lisible et nulle)."""
    sup = tmp_path / "superviseur-course"
    sup.mkdir()
    sceller(sup / "code.json", json.dumps({"code": 2}))
    run = {"nom": "r1", "depart": {"superviseur": {"pid": 2 ** 22 + 13, "debut_proc": "1", "dossier": str(sup)}},
           "fin": {"code": None}, "bras": [], "sortie": tmp_path / "sortie"}
    assert lc.depense_run(run)["course_lisible"] and lc.depense_run(run)["course_usd"] == 0.0
    ok, motif = lc.relance_permise([run])
    assert not ok and "sans fin propre" in motif
    assert lc.relance_permise([dict(run, fin={"code": 2})])[0]


def test_depense_course_cas(tmp_path):
    s = tmp_path / "sortie"
    c = tmp_path / "sortie-controle"
    assert lc.depense_course(s, False)[:2] == (20.0, False)              # aucun 0 par défaut
    assert lc.depense_course(s, True) == (0.0, True, "rien parti (fin propre du superviseur ; ni sortie, ni contrôle)")
    (c / "tentative-1").mkdir(parents=True)
    sceller(c / "tentative-1.json", json.dumps({"reglages": {"cout_claude_usd": 0.01, "cout_externe_usd": 0.4}}))
    assert lc.depense_course(s, True)[0] == pytest.approx(0.41)
    (c / "tentative-2-externe-argon").mkdir()
    assert lc.depense_course(s, True)[:2] == (20.0, False)
    (c / "tentative-2-externe-argon").rmdir()
    (c / "autre.txt").write_text("x")
    assert lc.depense_course(s, True)[0] == 20.0


@pytest.mark.parametrize("valeur", [-1, "x", True, None, float("inf"), float("nan")])
def test_cout_mal_type_compte_le_plafond(tmp_path, valeur):
    s = tmp_path / "sortie"
    s.mkdir()
    sceller(s / "manifeste-fin.json", json.dumps({"reglages": {"journal": {"cout_total_usd": valeur, "cout_externe_usd": 1}}},
                                                 allow_nan=True))
    assert lc.depense_course(s, True)[0] == 20.0


# ============================================================================================ M3 : bras

def test_m3_bras_paye_pas_de_relance(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    monde["env"]["FAUX_BRAS"] = "paye"
    assert jouer(monde, 1, capsys)[0] == 0
    monde["env"]["FAUX_BRAS"] = "ok"
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "aucune relance après dépense" in err
    assert lc.depense_run(run_de(monde, 1)[0])["bras_usd"] == pytest.approx(0.4)


@pytest.mark.parametrize("mode", ["illisible"])
def test_m3_bras_joue_illisible_verrouille(monde, capsys, mode):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    monde["env"]["FAUX_BRAS"] = mode
    assert jouer(monde, 1, capsys)[0] == 0
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "verrouillée" in err
    code, err = lancer(monde, 2, capsys)
    assert code == 2 and "génération 1" in err


def test_m3_bras_non_joue_relancable_trois_fois_au_plus(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    monde["env"]["FAUX_BRAS"] = "non_joue"
    for _ in range(3):
        assert jouer(monde, 1, capsys)[0] == 0
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "3 bras" in err
    assert len(run_de(monde, 1)[0]["bras"]) == 3


def test_m3_bras_non_joue_puis_reussi(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    monde["env"]["FAUX_BRAS"] = "non_joue"
    assert jouer(monde, 1, capsys)[0] == 0
    monde["env"]["FAUX_BRAS"] = "ok"
    assert jouer(monde, 1, capsys)[0] == 0
    assert lc.bras_reussi(run_de(monde, 1)[0])


def test_m10_generation_jouee_exige_le_manifeste_du_bras(monde, capsys):
    generation_complete(monde, 1, capsys)
    s = run_de(monde, 1)[0]["sortie"]
    (s / "manifeste-bras-rapporte.json").unlink()
    assert not lc.bras_reussi(run_de(monde, 1)[0])
    code, err = lancer(monde, 2, capsys)
    assert code == 2 and "génération 1" in err


def test_m2_bras_joue_hors_du_lanceur_compte(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    s = run_de(monde, 1)[0]["sortie"]
    sceller(s / "manifeste-bras-rapporte.json", json.dumps({"reglages": {"journal": {"cout_total_usd": 0.7}}}))
    assert lc.depense_run(run_de(monde, 1)[0])["bras_usd"] == pytest.approx(0.7)


# ============================================================================================ attestation (M6), garde du bras

@pytest.mark.parametrize("modif,motif", [
    ({"fiches_validees_sha256": "0" * 64}, "empreinte des fiches validées"),
    ({"consignes_en_attente_sha256": {}}, "consigne en attente"),
    ({"consignes_en_attente_sha256": {"argon-juge": "d" * 64}}, "consigne en attente"),
    ({"lecteur": " "}, "mal formée"),
    ({"temoin_vrai_absent_des_fiches_validees": "oui"}, "mal formée"),
])
def test_attestation_artefacts(monde, capsys, modif, motif):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1, **modif)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and motif in err and "bras" not in [j["mode"] for j in journal(monde)]


def test_attestation_version_la_plus_haute(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1, version=1, fiches_validees_sha256="0" * 64)
    attester(monde, 1, version=2)
    assert jouer(monde, 1, capsys)[0] == 0
    dep = json.loads((run_de(monde, 1)[0]["dossier"] / "manifeste-lanceur-bras-depart-1.json").read_text())
    assert dep["attestation"]["chemin"].endswith("-v2.json") and dep["attestation"]["lecteur"] == "la mère (essai)"


def test_attestation_non_scellee(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    p = monde["depot"] / lc.ATTESTATIONS / "attestation-lecture-humaine-g1-v1.json"
    p.write_text(p.read_text() + " ")
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "sceau faux" in err


def test_bras_garde_de_taille(monde, capsys):
    monde["env"]["FAUX_JUGE_REPET"] = "60000"
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "garde du bras" in err and "bras" not in [j["mode"] for j in journal(monde)]


def test_m12_plancher_du_controle_court(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    monde["r"].controle_bras_usd = 0.5
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "plancher_controle_court" in err


# ============================================================================================ M8 : recoupement

@pytest.mark.parametrize("cas,motif", [("absent", "absent"), ("non_scelle", "sceau faux"), ("trop_long", "trop long"),
                                       ("vide", "vide"), ("sans_relecture", "absent"), ("autre_empreinte", "empreinte"),
                                       ("recette", "aucune recette"), ("temoin", "témoin vrai"),
                                       ("sans_lecteur", "mal formée")])
def test_m8_recoupement_artefacts(monde, capsys, cas, motif):
    p = monde["depot"] / lc.RECOUPEMENT
    if cas == "absent":
        p.unlink()
    elif cas == "non_scelle":
        p.write_text(p.read_text() + "ajout\n")
    elif cas == "trop_long":
        p.unlink()
        sceller(p, "x" * (lc.TAILLE_MAX_RECOUPEMENT + 1))
        relecture(monde["depot"])
    elif cas == "vide":
        p.unlink()
        sceller(p, "  \n")
        relecture(monde["depot"])
    elif cas == "sans_relecture":
        (monde["depot"] / lc.RELECTURE_RECOUPEMENT).unlink()
    elif cas == "autre_empreinte":
        relecture(monde["depot"], recoupement_sha256="0" * 64)
    elif cas == "recette":
        relecture(monde["depot"], niveau_methode_aucune_recette_aucun_secret=False)
    elif cas == "temoin":
        relecture(monde["depot"], temoin_vrai_absent=False)
    else:
        relecture(monde["depot"], lecteur="")
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and motif in err and not monde["journal"].exists()


# ============================================================================================ garde de cumul

def test_cumul_sain():
    assert lc.garde_cumul([], 20.0, 60.0)["depense_relevee_usd"] == 0.0


def test_cumul_bout_en_bout_passe(monde, capsys):
    monde["env"]["FAUX_COUT_CLAUDE"], monde["env"]["FAUX_COUT_EXTERNE"] = "11.9", "7.9"
    monde["env"]["FAUX_COUT_BRAS"] = "0.05"
    generation_complete(monde, 1, capsys)
    generation_complete(monde, 2, capsys)
    assert lancer(monde, 3, capsys)[0] == 0                          # 39,7 + 20 ≤ 60


def test_cumul_depasse(monde, capsys):
    monde["env"]["FAUX_COUT_CLAUDE"], monde["env"]["FAUX_COUT_EXTERNE"] = "12.0", "8.0"
    monde["env"]["FAUX_COUT_BRAS"] = "0.5"
    generation_complete(monde, 1, capsys)
    generation_complete(monde, 2, capsys)
    code, err = lancer(monde, 3, capsys)
    assert code == 2 and "garde de cumul" in err


def test_m7_borne_du_cumul_jamais_au_dela_de_60(monde, capsys):
    reg = monde["r"].registre_go
    reg.write_text(reg.read_text().replace("| 60 USD |", "| 100 USD |"))
    monde["env"]["FAUX_COUT_CLAUDE"], monde["env"]["FAUX_COUT_EXTERNE"] = "12.0", "8.0"
    monde["env"]["FAUX_COUT_BRAS"] = "0.5"
    generation_complete(monde, 1, capsys)
    generation_complete(monde, 2, capsys)
    code, err = lancer(monde, 3, capsys)
    assert code == 2 and "> 60.0 USD" in err


# ============================================================================================ gardes reprises du v3

def test_drapeaux_sain_commande_production():
    r = lc.Reglages.production()
    lc.garde_drapeaux(lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX, Path("/x/p.md"), 1))
    lc.garde_drapeaux(lc.commande_bras(r, Path("/x/s"), Path("/x/l"), Path("/x/a.json"), "h", PFX))


@pytest.mark.parametrize("drapeau", ["--accepter-sans-bac-a-sable", "--accepter-sans", "--tolerer", "--motif-sans-bac-a-sable=x",
                                     "--taille-max-consigne-externe-bras=9", "--prix-entree-usd-par-million-jetons"])
def test_drapeaux_artefact(monde, capsys, drapeau):
    monde["r"].arguments_en_plus = (drapeau,)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "interdit" in err and not monde["journal"].exists()


def test_sommes_sain_production():
    s = lc.garde_sommes(lc.commande_course(lc.Reglages.production(), Path("/x/s"), Path("/x/l"), "h", PFX, Path("/x/p"), 1))
    assert (s["somme_claude"], s["somme_externe"]) == (9.9, 7.6)
    assert s["externe_pire_course_plus_bras"] == pytest.approx(8.0)


@pytest.mark.parametrize("cle,valeur,motif", [("juge_ideation|gemini-4-argon", 3.2, "pas sous le total externe"),
                                              ("proposeur_ideation|claude-fable-5-1", 3.1, "Claude"),
                                              ("proposeur_ideation|gemini-4-argon", 1.4, "le bras serait refusé")])
def test_sommes_artefacts(cle, valeur, motif):
    r = lc.Reglages.production()
    r.plafonds = dict(lc.PLAFONDS, **{cle: valeur})
    with pytest.raises(lc.Refus, match=motif):
        lc.garde_sommes(lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX, Path("/x/p"), 1))


@pytest.mark.parametrize("etat,motif", [("inactif", "inactif"), ("sans_proc", "/proc neuf"), ("illisible", "illisible"),
                                         ("erreur", "illisible")])
def test_bac_a_sable_artefact(monde, capsys, etat, motif):
    monde["env"]["FAUX_BAC"] = etat
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and motif in err
    assert not monde["journal"].exists() and not monde["r"].dossier_runs.exists()


def test_bac_a_sable_artefact_au_bras(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    monde["env"]["FAUX_BAC"] = "inactif"
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "inactif" in err and [j["mode"] for j in journal(monde)] == ["mesure", "course"]


def test_go_sain_registre_reel():
    g = lc.verifier_go(RACINE / "registres" / "go.md", dt.date(2026, 11, 13))
    assert g["id"] == "GO-2026-11-13-03" and g["plafond_usd"] == 60.0 and g["echeance"] == "2026-11-30"


@pytest.mark.parametrize("avant,apres,motif", [
    ("| calcul |", "| publication |", "type"), ("| Lazar |", "| Claude |", "Lazar exigé"),
    ("| 60 USD |", "| 59 USD |", "sous les trois courses"), ("| 60 USD |", "| soixante |", "illisible"),
    ("bassins d'idées", "piliers", "périmètre"),
])
def test_go_artefacts(monde, capsys, avant, apres, motif):
    reg = monde["r"].registre_go
    reg.write_text(reg.read_text().replace(avant, apres))
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and motif in err


@pytest.mark.parametrize("jour", [dt.date(2026, 11, 12), dt.date(2026, 12, 1)])
def test_go_hors_periode(monde, capsys, jour):
    monde["r"].aujourd_hui = jour
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "période" in err


@pytest.mark.parametrize("ligne,motif", [
    ("| GO-2026-11-14-01 | 2026-11-14 | révocation | révoque GO-2026-11-13-03 | — | — | Lazar | x |", "révoqué"),
    ("| GO-2026-11-14-01 | 2026-11-14 | Revocation | révoque GO-2026-11-13-03 | — | — | Lazar | x |", "révoqué"),
    ("| GO-2026-11-14-01 | 2026-11-14 | révocation | révoque GO-2026-11-13-03 | — | — | Lazar | x | y |", "mal formée"),
])
def test_m1_go_revoque_ou_ligne_mal_formee(monde, capsys, ligne, motif):
    with open(monde["r"].registre_go, "a") as f:
        f.write(ligne + "\n")
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and motif in err


def test_go_ligne_qui_cite_bien_formee_admise(monde, capsys):
    with open(monde["r"].registre_go, "a") as f:
        f.write("| GO-2026-11-14-02 | 2026-11-14 | calcul | autre chose, voir GO-2026-11-13-03 | 5 USD | 2026-11-20 | Lazar | x |\n")
    assert lancer(monde, 1, capsys)[0] == 0


def test_orchestrateur_artefacts(monde, capsys):
    p = monde["r"].orchestrateur / "pole" / "adaptateurs.py"
    p.write_text(p.read_text() + "\n# remplacement\n")
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "modifié" in err and not monde["journal"].exists()


def test_orchestrateur_cache_d_octets(monde, capsys):
    (monde["r"].orchestrateur / "pole" / "__pycache__").mkdir()
    (monde["r"].orchestrateur / "pole" / "__pycache__" / "adaptateurs.cpython-313.pyc").write_bytes(b"x")
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "ignorés" in err


def test_orchestrateur_commit(monde, capsys):
    monde["r"].commit_orchestrateur = "f" * 40
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "commit" in err


def test_orchestrateur_sain_clone_reel():
    assert _clone_reel() is not None


def test_pieces_sain_depot_reel():
    assert set(lc.verifier_pieces(lc.Reglages.production())) == set(lc.PIECES)


def test_pieces_artefact(monde, capsys):
    (monde["depot"] / monde["r"].pieces["question"][0]).write_text("autre question\n")
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "pièces" in err and not monde["journal"].exists()


def test_environnement_permis():
    class Env(dict):
        def __getitem__(self, n):
            if n not in lc.NOMS_PERMIS:
                raise AssertionError(f"valeur de {n} lue")
            return dict.__getitem__(self, n)
    env, noms = lc.environnement_permis(Env(PATH="/bin", ANTHROPIC_API_KEY="v", GH_TOKEN="v", CLAUDE_CODE_REMOTE="t",
                                            ANTHROPIC_BASE_URL="u", CCR_X="1", HOME="/root", LANG="C"),
                                        Path("/p/pycache"), Path("/h"))
    assert env == {"PATH": "/bin", "LANG": "C", "GO_ID": "GO-2026-11-13-03", "HOME": "/h", "PYTHONPYCACHEPREFIX": "/p/pycache"}
    assert noms["noms_exclus"] == ["ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL", "CCR_X", "CLAUDE_CODE_REMOTE", "GH_TOKEN", "HOME"]


def test_environnement_permis_prefixe_d_essai():
    assert lc.Reglages.production().prefixe_essais is None
    with pytest.raises(lc.Refus, match="préfixe d'essai interdit"):
        lc.environnement_permis({"PATH": "/bin"}, prefixe_essais="CLAUDE_")


def test_environnement_permis_artefact_nom_interdit(monkeypatch):
    monkeypatch.setattr(lc, "NOMS_PERMIS", lc.NOMS_PERMIS + ("CLAUDE_CODE_REMOTE",))
    with pytest.raises(lc.Refus, match="nom permis interdit"):
        lc.environnement_permis({"PATH": "/bin"})


@pytest.mark.parametrize("python,motif", [("python3", "non absolu"), ("/nulle/part/python3", "absent"),
                                          ("/bin/sh", "un seul interpréteur")])
def test_interprete_artefacts(monde, capsys, python, motif):
    monde["r"].python = python
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and motif in err and not monde["journal"].exists()


def test_prefixe_du_cache_artefact(monde, capsys):
    monde["r"].dossier_sorties = monde["r"].orchestrateur / "sorties"
    code, err = lancer(monde, 1, capsys)
    # le verrou crée le dossier des sorties : le clone n'est plus propre ; refus avant tout appel, quel que soit le motif
    assert code == 2 and ("dans le clone" in err or "orchestrateur modifié" in err) and not monde["journal"].exists()
    with pytest.raises(lc.Refus, match="dans le clone"):
        lc.verifier_prefixe_pycache(monde["r"].orchestrateur / "x" / "pycache", monde["r"].orchestrateur)


def test_ecrire_scelle_jamais_ecrase(tmp_path):
    p = tmp_path / "m.json"
    lc.ecrire_scelle(p, {"a": 1})
    with pytest.raises(lc.Refus, match="existe déjà"):
        lc.ecrire_scelle(p, {"a": 2})


def test_dossier_inattendu_dans_les_runs(monde, capsys):
    (monde["r"].dossier_runs / "autre-chose").mkdir(parents=True)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "inattendu" in err


def test_run_sans_manifeste(monde, capsys):
    (monde["r"].dossier_runs / ("20261113-140000" + lc.SUFFIXE_RUN + "1")).mkdir(parents=True)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "état inconnu" in err


def test_run_version_incoherente(monde, capsys):
    assert jouer(monde, 1, capsys)[0] == 0
    d = run_de(monde, 1)[0]["dossier"]
    autre = monde["r"].dossier_runs / d.name.replace("-g1", "-g2")
    d.rename(autre)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "incohérente" in err


def test_m8_toute_exception_ecrit_un_manifeste_de_refus(monde, capsys, monkeypatch):
    def panne(*a, **k):
        raise OSError("panne simulée")
    monkeypatch.setattr(lc, "lancer_detache", panne)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "panne simulée" in err
    run = lc.runs_du_lanceur(monde["r"])[0]
    assert run["refus"] and "OSError" in run["refus"]["refus"]
    monkeypatch.undo()
    assert jouer(monde, 1, capsys)[0] == 0                            # relance permise : rien n'était parti


def test_mesure_illisible(monde, capsys):
    monde["env"]["FAUX_MESURE_ILLISIBLE"] = "1"
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "mesure des consignes illisible" in err


def test_source_sans_import_de_l_orchestrateur():
    import re
    texte = SCRIPT.read_text()
    assert [x for x in texte.splitlines() if re.match(r"^\s*(from\s+pole\b|import\s+pole\b)", x)] == []
    assert "setattr(" not in texte and "monkeypatch" not in texte and "dict(os.environ)" not in texte
    assert "sceller_existant(chemin)" not in texte.split("def construire_liste_blanche")[1].split("def mesurer_consignes")[0]
    assert not [m for m in sys.modules if m == "pole" or m.startswith("pole.")]


# ============================================================================================ gardes de taille (calcul)

MESURE = {"sans_appel": True, "prix_entree_usd_par_million_jetons": 10.0,
          "consignes": {"consigne_de_controle_externe": 322793, "consigne_passe_1": 56691, "consigne_du_juge_maximale": 1660189,
                        "fiches_au_juge_au_maximum": 40, "nombre_par_proposeur": 6},
          "garde_course": {"passerait": True}, "gardes_passes_externes": {"argon": {"passe_1": {"passerait": True}}}}


def test_tailles_sain_mesure_gabarit():
    g = lc.gardes_de_taille(MESURE, lc.Reglages.production())
    assert (g["course"]["taille_max"], g["course"]["marge"]) == (400000, 77207)
    assert g["commande_argon"]["controle_externe"]["plancher_garde_a_3_caracteres_par_jeton"] == pytest.approx(1.447669)
    m = json.loads(json.dumps(MESURE))
    m["consignes"]["consigne_de_controle_externe"] = 332856        # pièce de 50 000 caractères (générations 2 et 3)
    assert lc.gardes_de_taille(m, lc.Reglages.production())["commande_argon"]["controle_externe"]["tient"]


@pytest.mark.parametrize("modif,motif", [
    ({"consigne_de_controle_externe": 400001}, "course"),
    ({"nombre_par_proposeur": 8}, "--nombre"),
])
def test_tailles_artefacts(modif, motif):
    m = json.loads(json.dumps(MESURE))
    m["consignes"].update(modif)
    with pytest.raises(lc.Refus, match=motif):
        lc.gardes_de_taille(m, lc.Reglages.production())


def test_tailles_artefact_commande_argon_a_3_caracteres():
    r = lc.Reglages.production()
    r.controle_externe_usd = 1.5                                      # tient à 4 caractères par jeton, pas à 3
    m = json.loads(json.dumps(MESURE))
    m["consignes"]["consigne_de_controle_externe"] = 360000
    with pytest.raises(lc.Refus, match="commande_argon/controle_externe"):
        lc.gardes_de_taille(m, r)


def test_plancher_argon():
    assert lc.plancher_argon(0) == pytest.approx(0.509952)
    assert 0.2 < lc.plancher_argon(200, 3.0) < lc.CONTROLE_BRAS_USD
