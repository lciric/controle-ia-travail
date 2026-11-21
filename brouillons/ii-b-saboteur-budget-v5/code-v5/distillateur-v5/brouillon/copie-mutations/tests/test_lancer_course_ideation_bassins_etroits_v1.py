"""Essais R5 de `scripts/lancer_course_ideation_bassins_etroits_v1.py` (trois générations, GO-2026-11-13-03).

Aucun modèle appelé, aucun réseau, l'orchestrateur réel jamais exécuté : un **faux orchestrateur** (dépôt git jetable,
faux `demonstrations/ideation_v8.py` qui construit la liste blanche, rend une mesure des consignes, écrit une sortie de
course ou de bras scellée et consigne ses arguments et les **noms** de son environnement ; faux `pole/adaptateurs.py` dont la
sonde rend l'état demandé) est servi au lanceur par `Reglages`, réglage que la ligne de commande n'expose pas. Pour chaque
garde : un cas sain et un artefact. Ajouts propres à cette version : argument fermé, enchaînement course → bras →
génération suivante, règle de passage, garde de cumul, refus de relance après dépense, garde du bras."""
from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "lancer_course_ideation_bassins_etroits_v1.py"
_spec = importlib.util.spec_from_file_location("lancer_course_ideation_bassins_etroits_v1", SCRIPT)
lc = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = lc
_spec.loader.exec_module(lc)

FAUX_V8 = r'''
import hashlib, json, os, sys
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
                            "pycache_prefix": sys.pycache_prefix, "orig_argv": sys.orig_argv}) + "\n")

if "--construire-liste-blanche" in argv:
    i = argv.index("--construire-liste-blanche")
    liste = {os.path.realpath(c): hashlib.sha256(open(c, "rb").read()).hexdigest() for c in argv[i + 1:]}
    open(argv[0], "w").write(json.dumps(liste))
    sys.exit(0)
if "--mesurer-consignes" in argv:
    consigner("mesure")
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
    lisible = os.environ.get("FAUX_LISIBLE", "1") == "1"
    sceller(os.path.join(sortie, "manifeste-bras-rapporte.json"),
            {"reglages": {"journal": {"cout_total_usd": float(os.environ.get("FAUX_COUT_BRAS", "0.9"))}}})
    sceller(os.path.join(sortie, "doublons-bras-rapporte.json"), {"argon-juge": [["T02", "T03"]]})
    rangs = ["opus-p1-01", "opus-p2-01", "fable-p1-01", "argon-p1-01", "fable-p1-02", "argon-p2-02", "fable-p2-03",
             "fable-p1-04", "opus-p1-05"]
    lignes = [{"rang": k, "identifiant_auteur": i, "auteur": i.split("-p")[0], "eligible": k <= 8, "total": 15 - k}
              for k, i in enumerate(rangs, 1)]
    sceller(os.path.join(sortie, "classement.json"), {"lisible_L2_L4": lisible, "lignes": lignes})
    sys.exit(int(os.environ.get("FAUX_CODE_BRAS", "0" if lisible else "4")))
consigner("course")
code = int(os.environ.get("FAUX_CODE", "0"))
if os.environ.get("FAUX_RIEN") == "1":
    sys.exit(code)
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
    (depot / "registres").mkdir()
    (depot / "registres" / "go.md").write_text("| id | a | t | p | pl | e | par | ref |\n|---|\n" + GO_LIGNE + "\n")
    journal = tmp_path / "journal.jsonl"
    env = {"PATH": "/usr/bin:/bin", "HOME": str(tmp_path), "FAUX_JOURNAL": str(journal), "FAUX_BAC": "actif",
           "ANTHROPIC_API_KEY": "valeur-factice-d-essai", "AUTRE_SECRET_X": "factice"}
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
                    maintenant=maintenant)
    return {"r": r, "journal": journal, "env": env, "tmp": tmp_path, "depot": depot}


def journal(monde):
    if not monde["journal"].exists():
        return []
    return [json.loads(x) for x in monde["journal"].read_text().splitlines()]


def lancer(monde, g, capsys=None):
    code = lc.principal([str(g)], monde["r"])
    err = capsys.readouterr().err if capsys else ""
    return code, err


def attester(monde, g):
    run = [x for x in lc.runs_du_lanceur(monde["r"]) if x["generation"] == g and lc.course_reussie(x)][0]
    a = {"lecteur": "essai", "lu_le": "2026-11-13", "fiches_validees_sha256": sha(run["sortie"] / "fiches-validees.json"),
         "consignes_en_attente_sha256": {"argon-juge": "c" * 64}}
    sceller(monde["depot"] / lc.ATTESTATION.format(g=g), json.dumps(a))
    return run


def generation_complete(monde, g, capsys):
    assert lancer(monde, g, capsys)[0] == 0
    attester(monde, g)
    assert lancer(monde, g, capsys)[0] == 0


# ============================================================================================ argument unique et fermé

@pytest.mark.parametrize("argv", [[], ["4"], ["0"], ["1", "2"], ["--accepter-sans-bac-a-sable"], ["01"], [" 1"], ["un"]])
def test_argument_artefacts(monde, capsys, argv):
    assert lc.principal(argv, monde["r"]) == 2
    assert "un seul argument" in capsys.readouterr().err and not monde["journal"].exists()


# ============================================================================================ chaîne saine de bout en bout

def test_trois_generations_bout_en_bout(monde, capsys):
    r = monde["r"]
    for g in (1, 2, 3):
        assert lancer(monde, g, capsys)[0] == 0                     # course
        runs = [x for x in lc.runs_du_lanceur(r) if x["generation"] == g]
        assert len(runs) == 1 and lc.course_reussie(runs[0])
        code, err = lancer(monde, g, capsys)                       # bras sans attestation : refus
        assert code == 2 and "attestation" in err
        attester(monde, g)
        assert lancer(monde, g, capsys)[0] == 0                     # bras
        assert lc.bras_reussi(lc.runs_du_lanceur(r)[-1])
    modes = [j["mode"] for j in journal(monde)]
    assert modes == ["mesure", "course", "bras"] * 3
    courses = [j for j in journal(monde) if j["mode"] == "course"]
    for k, j in enumerate(courses, 1):
        a = j["argv"]
        assert j["noms_cle"] == [] and j["go_id"] == "GO-2026-11-13-03"
        assert "--accepter-sans-bac-a-sable" not in a and not any(x.startswith("--tolerer") for x in a)
        assert a[a.index("--nombre") + 1] == "6" and a[a.index("--graine") + 1] == str(2026111300 + k)
        assert a[a.index("--budget-controle-externe-usd") + 1] == "1.5"
        assert a[a.index("--budget-passe-2-externe-usd") + 1] == "1.9"
        assert "proposeur_ideation|gemini-4-argon=1.3" in a
        pieces = [a[i + 1] for i, x in enumerate(a) if x == "--piece"]
        assert pieces[0].endswith("faits-v1.md")
        assert pieces[1].endswith("recoupement-methodes-v1.md" if k == 1 else f"fiches-recues-g{k - 1}-pour-g{k}.md")
        assert [a[i + 1] for i, x in enumerate(a) if x == "--piece-juge"] == pieces
        assert j["orig_argv"][1:5][:2] == ["-I", "-B"] and j["pycache_prefix"]
    bras = [j for j in journal(monde) if j["mode"] == "bras"]
    assert all(b["argv"][b["argv"].index("--budget-controle-usd") + 1] == "0.6" for b in bras)
    assert all("--moteur" not in b["argv"] for b in bras)
    code, err = lancer(monde, 3, capsys)
    assert code == 2 and "déjà jouée" in err
    runs = lc.runs_du_lanceur(r)
    dep = json.loads((runs[0]["dossier"] / "manifeste-lanceur-depart.json").read_text())
    assert dep["cles"]["noms_retires_de_l_environnement"] == ["ANTHROPIC_API_KEY", "AUTRE_SECRET_X"]
    assert "valeur-factice-d-essai" not in (runs[0]["dossier"] / "manifeste-lanceur-depart.json").read_text()
    assert dep["plafonds"]["sommes"]["somme_externe"] == 7.4 and dep["plafonds"]["sommes"]["somme_claude"] == 9.9
    assert dep["garde_de_cumul"]["depense_relevee_usd"] == 0.0
    dep3 = json.loads((runs[2]["dossier"] / "manifeste-lanceur-depart.json").read_text())
    assert dep3["garde_de_cumul"]["depense_relevee_usd"] == pytest.approx(2 * (2.5 + 2.0 + 0.9))
    fin1 = json.loads((runs[0]["dossier"] / "manifeste-lanceur-fin.json").read_text())
    assert fin1["pour_l_attestation"]["consignes_en_attente_sha256"] == {"argon-juge": "c" * 64}
    for x in runs:
        for f in x["dossier"].glob("*.json"):
            h, nom = Path(str(f) + ".sha256").read_text().split()
            assert nom == f.name and h == sha(f)
        assert not str(x["sortie"]).startswith(str(monde["depot"]))


# ============================================================================================ règle de passage

def test_regle_de_passage(monde, capsys):
    generation_complete(monde, 1, capsys)
    run = lc.runs_du_lanceur(monde["r"])[0]
    choix = lc.choisir_fiches_recues(run["sortie"], 1)
    # rang 2 : autre passe de opus-p1-01 ; rang 5 (fable-p1-02) : doublon d'argon-p1-01 chez argon-juge
    assert choix["ordre_de_prise"] == ["opus-p1-01", "fable-p1-01", "argon-p1-01", "argon-p2-02", "fable-p2-03"]
    assert {s["identifiant"] for s in choix["sautees"]} == {"opus-p2-01", "fable-p1-02"}
    fiches = {f["identifiant_auteur"]: f for f in json.loads((run["sortie"] / "fiches-validees.json").read_text())}
    ordre = [p["identifiant"] for p in choix["prises"]]
    assert ordre == sorted(ordre, key=lambda i: fiches[i]["empreinte"])           # ordre neutre
    assert [p["etiquette"] for p in choix["prises"]] == [f"G1-R{k}" for k in range(1, 6)]
    t = choix["texte"]
    for interdit in ('"identifiant_auteur"', '"empreinte"', '"auteur"', '"rang"', '"total"', '"passe"', '"eligible"'):
        assert interdit not in t
    assert len(t) <= lc.TAILLE_MAX_FICHES_RECUES


def test_regle_de_passage_plafond_de_taille(monde, capsys):
    monde["env"]["FAUX_GRANDE"] = str(lc.TAILLE_MAX_FICHES_RECUES)
    generation_complete(monde, 1, capsys)
    choix = lc.choisir_fiches_recues(lc.runs_du_lanceur(monde["r"])[0]["sortie"], 1)
    assert "fable-p1-01" not in choix["ordre_de_prise"]
    assert any(s["identifiant"] == "fable-p1-01" and s["motif"].startswith("taille") for s in choix["sautees"])
    assert len(choix["ordre_de_prise"]) == 5 and "fable-p1-04" in choix["ordre_de_prise"]


def test_regle_de_passage_classement_illisible(monde, capsys):
    assert lancer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    monde["env"]["FAUX_LISIBLE"] = "0"
    assert lancer(monde, 1, capsys)[0] == 4
    with pytest.raises(lc.Refus, match="illisible"):
        lc.choisir_fiches_recues(lc.runs_du_lanceur(monde["r"])[0]["sortie"], 1)
    code, err = lancer(monde, 2, capsys)
    assert code == 2 and "génération 1" in err


def test_regle_de_passage_sceau_faux(monde, capsys):
    generation_complete(monde, 1, capsys)
    s = lc.runs_du_lanceur(monde["r"])[0]["sortie"]
    p = s / "classement.json"
    p.write_text(p.read_text().replace('"eligible": false', '"eligible": true'))
    with pytest.raises(lc.Refus, match="sceau faux"):
        lc.choisir_fiches_recues(s, 1)


# ============================================================================================ enchaînement : refus

def test_generation_2_sans_generation_1(monde, capsys):
    code, err = lancer(monde, 2, capsys)
    assert code == 2 and "génération 1" in err and not monde["journal"].exists()


def test_generation_3_apres_seule_course_2(monde, capsys):
    generation_complete(monde, 1, capsys)
    assert lancer(monde, 2, capsys)[0] == 0
    code, err = lancer(monde, 3, capsys)
    assert code == 2 and "génération 2" in err


def test_pas_de_relance_apres_depense(monde, capsys):
    monde["env"]["FAUX_CODE"] = "2"
    assert lancer(monde, 1, capsys)[0] == 2
    monde["env"]["FAUX_CODE"] = "0"
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "aucune relance après dépense" in err
    assert [j["mode"] for j in journal(monde)] == ["mesure", "course"]


def test_relance_permise_si_rien_parti(monde, capsys):
    monde["env"]["FAUX_CODE"], monde["env"]["FAUX_RIEN"] = "2", "1"
    assert lancer(monde, 1, capsys)[0] == 2
    monde["env"]["FAUX_CODE"], monde["env"]["FAUX_RIEN"] = "0", "0"
    assert lancer(monde, 1, capsys)[0] == 0


def test_refus_apres_ecriture_laisse_un_manifeste_et_permet_la_relance(monde, capsys):
    monde["env"]["FAUX_CONTROLE"] = "500000"
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "garde(s) de taille" in err
    runs = lc.runs_du_lanceur(monde["r"])
    assert len(runs) == 1 and runs[0]["refus"] and runs[0]["depart"] is None
    assert [j["mode"] for j in journal(monde)] == ["mesure"]
    monde["env"]["FAUX_CONTROLE"] = "322793"
    assert lancer(monde, 1, capsys)[0] == 0


def test_bras_attestation_fausse(monde, capsys):
    assert lancer(monde, 1, capsys)[0] == 0
    a = {"lecteur": "essai", "lu_le": "2026-11-13", "fiches_validees_sha256": "0" * 64,
         "consignes_en_attente_sha256": {"argon-juge": "c" * 64}}
    sceller(monde["depot"] / lc.ATTESTATION.format(g=1), json.dumps(a))
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "empreinte des fiches validées" in err


def test_bras_attestation_non_scellee(monde, capsys):
    assert lancer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    p = monde["depot"] / lc.ATTESTATION.format(g=1)
    p.write_text(p.read_text() + " ")
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "sceau faux" in err


def test_bras_garde_de_taille(monde, capsys):
    monde["env"]["FAUX_JUGE_REPET"] = "60000"      # ≈ 1 020 000 caractères > 1 000 000 − 10 × 10 000
    assert lancer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "garde du bras" in err
    assert [j["mode"] for j in journal(monde)] == ["mesure", "course"]


def test_bras_relance_apres_echec(monde, capsys):
    assert lancer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    monde["env"]["FAUX_CODE_BRAS"] = "2"
    assert lancer(monde, 1, capsys)[0] == 2
    monde["env"]["FAUX_CODE_BRAS"] = "0"
    assert lancer(monde, 1, capsys)[0] == 0
    run = lc.runs_du_lanceur(monde["r"])[0]
    assert len(run["bras"]) == 2 and lc.bras_reussi(run)


# ============================================================================================ garde de cumul

def test_cumul_sain():
    assert lc.garde_cumul([], 20.0, 60.0)["depense_relevee_usd"] == 0.0


def test_cumul_artefact_bout_en_bout(monde, capsys):
    monde["env"]["FAUX_COUT_CLAUDE"], monde["env"]["FAUX_COUT_EXTERNE"] = "11.9", "7.9"
    monde["env"]["FAUX_COUT_BRAS"] = "0.05"
    generation_complete(monde, 1, capsys)
    generation_complete(monde, 2, capsys)          # 19,85 + 20 ≤ 60
    code, err = lancer(monde, 3, capsys)           # 39,7 + 20 ≤ 60 : passe
    assert code == 0
    monde["env"]["FAUX_COUT_BRAS"] = "0.5"


def test_cumul_artefact_depasse(monde, capsys):
    monde["env"]["FAUX_COUT_CLAUDE"], monde["env"]["FAUX_COUT_EXTERNE"] = "12.0", "8.0"
    monde["env"]["FAUX_COUT_BRAS"] = "0.5"
    generation_complete(monde, 1, capsys)
    generation_complete(monde, 2, capsys)          # 20,5 + 20,5 = 41 ; + 20 > 60
    code, err = lancer(monde, 3, capsys)
    assert code == 2 and "garde de cumul" in err
    assert [j["mode"] for j in journal(monde)].count("course") == 2


def test_cumul_depense_illisible_compte_le_plafond(monde, capsys):
    assert lancer(monde, 1, capsys)[0] == 0
    run = lc.runs_du_lanceur(monde["r"])[0]
    p = run["sortie"] / "manifeste-fin.json"
    p.write_text(p.read_text() + " ")               # sceau faux
    d = lc.depense_run(lc.runs_du_lanceur(monde["r"])[0])
    assert d["course_usd"] == 20.0 and "plafond entier" in d["lecture"]


def test_cumul_bras_sans_trace(monde, capsys):
    assert lancer(monde, 1, capsys)[0] == 0
    attester(monde, 1)
    assert lancer(monde, 1, capsys)[0] == 0
    run = lc.runs_du_lanceur(monde["r"])[0]
    (run["sortie"] / "manifeste-bras-rapporte.json").unlink()
    d = lc.depense_run(lc.runs_du_lanceur(monde["r"])[0])
    assert d["bras_usd"] == pytest.approx(lc.PLAFOND_BRAS_USD)


def test_depense_course_tentatives_de_controle(tmp_path):
    s = tmp_path / "sortie"
    c = tmp_path / "sortie-controle"
    assert lc.depense_course(s) == (0.0, "rien parti (ni sortie, ni contrôle)")
    (c / "tentative-1").mkdir(parents=True)
    sceller(c / "tentative-1.json", json.dumps({"reglages": {"cout_claude_usd": 0.01, "cout_externe_usd": 0.4}}))
    assert lc.depense_course(s)[0] == pytest.approx(0.41)
    (c / "tentative-2").mkdir()
    assert lc.depense_course(s)[0] == 20.0          # contrôle sans tentative scellée


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
    assert (s["somme_claude"], s["somme_externe"], s["externe_pire_course_plus_bras"]) == (9.9, 7.4, 7.8)


@pytest.mark.parametrize("cle,valeur,motif", [("juge_ideation|gemini-4-argon", 3.2, "pas sous le total externe"),
                                              ("proposeur_ideation|claude-fable-5-1", 3.1, "Claude"),
                                              ("proposeur_ideation|gemini-4-argon", 1.6, "le bras serait refusé")])
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
    assert lancer(monde, 1, capsys)[0] == 0
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


def test_go_revoque(monde, capsys):
    with open(monde["r"].registre_go, "a") as f:
        f.write("| GO-2026-11-14-01 | 2026-11-14 | révocation | révoque GO-2026-11-13-03 | — | — | Lazar | x |\n")
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "révoqué" in err


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
    r = lc.Reglages.production()
    if not (r.orchestrateur / lc.LANCEUR_ORCHESTRATEUR).is_file():
        pytest.skip("clone de l'orchestrateur absent")
    o = lc.verifier_orchestrateur(r)
    assert o["commit"] == lc.COMMIT_ORCHESTRATEUR


def test_pieces_sain_depot_reel():
    assert set(lc.verifier_pieces(lc.Reglages.production())) == set(lc.PIECES)


def test_pieces_artefact(monde, capsys):
    (monde["depot"] / monde["r"].pieces["question"][0]).write_text("autre question\n")
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "pièces" in err and not monde["journal"].exists()


@pytest.mark.parametrize("cas", ["absent", "non_scelle", "trop_long", "vide"])
def test_recoupement_artefacts(monde, capsys, cas):
    p = monde["depot"] / lc.RECOUPEMENT
    if cas == "absent":
        p.unlink()
    elif cas == "non_scelle":
        p.write_text(p.read_text() + "ajout\n")
    elif cas == "trop_long":
        sceller(p, "x" * (lc.TAILLE_MAX_RECOUPEMENT + 1))
    else:
        sceller(p, "  \n")
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and ("recoupement" in err or "scellé" in err or "sceau" in err)
    assert not monde["journal"].exists()


def test_cles_noms_seuls():
    class Env(dict):
        def __getitem__(self, n):
            if "KEY" in n or "TOKEN" in n:
                raise AssertionError(f"valeur de {n} lue")
            return dict.__getitem__(self, n)
    env, retires = lc.environnement_sans_cles(Env(PATH="/bin", ANTHROPIC_API_KEY="v", GH_TOKEN="v"), Path("/p/pycache"))
    assert retires == ["ANTHROPIC_API_KEY", "GH_TOKEN"]
    assert env == {"PATH": "/bin", "GO_ID": "GO-2026-11-13-03", "PYTHONPYCACHEPREFIX": "/p/pycache"}


@pytest.mark.parametrize("python,motif", [("python3", "non absolu"), ("/nulle/part/python3", "absent"),
                                          ("/bin/sh", "un seul interpréteur")])
def test_interprete_artefacts(monde, capsys, python, motif):
    monde["r"].python = python
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and motif in err and not monde["journal"].exists()


def test_interprete_production():
    r = lc.Reglages.production()
    assert r.python == "/usr/local/bin/python3"
    assert lc.commande_course(r, Path("/x/s"), Path("/x/l"), "h", PFX, Path("/x/p"), 1)[0] == "/usr/local/bin/python3"


def test_ecrire_scelle_jamais_ecrase(tmp_path):
    p = tmp_path / "m.json"
    lc.ecrire_scelle(p, {"a": 1})
    with pytest.raises(lc.Refus, match="existe déjà"):
        lc.ecrire_scelle(p, {"a": 2})


def test_dossier_inattendu_dans_les_runs(monde, capsys):
    (monde["r"].dossier_runs / "autre-chose").mkdir(parents=True)
    code, err = lancer(monde, 1, capsys)
    assert code == 2 and "inattendu" in err


def test_source_sans_import_de_l_orchestrateur():
    import re
    texte = SCRIPT.read_text()
    lignes = [x for x in texte.splitlines() if re.match(r"^\s*(from\s+pole\b|import\s+pole\b)", x)]
    assert lignes == []
    assert "setattr(" not in texte and "monkeypatch" not in texte and "dict(os.environ)" not in texte
    assert not [m for m in sys.modules if m == "pole" or m.startswith("pole.")]


# ============================================================================================ gardes de taille (calcul)

MESURE = {"sans_appel": True, "prix_entree_usd_par_million_jetons": 10.0,
          "consignes": {"consigne_de_controle_externe": 322793, "consigne_passe_1": 56691, "consigne_du_juge_maximale": 1660189,
                        "fiches_au_juge_au_maximum": 40, "nombre_par_proposeur": 6},
          "garde_course": {"passerait": True}, "gardes_passes_externes": {"argon": {"passe_1": {"passerait": True}}}}


def test_tailles_sain_mesure_gabarit():
    """Tailles de la mesure sans appel du 13 novembre (pièce de génération 1 au gabarit de 40 000 caractères)."""
    g = lc.gardes_de_taille(MESURE, lc.Reglages.production())
    assert (g["course"]["taille_max"], g["course"]["marge"]) == (400000, 77207)
    assert (g["passe_1"]["taille_max"], g["passe_2_fiches_8000"]["taille_max"]) == (280000, 520000)
    assert g["commande_argon"]["controle_externe"]["plancher_a_4_caracteres_par_jeton"] == pytest.approx(1.213244)
    assert g["passe_2_seuil_de_fiche"]["fiche_de_passe_1_la_plus_longue_admise"] == 19534


@pytest.mark.parametrize("modif,motif", [
    ({"consigne_de_controle_externe": 400001}, "course"),
    ({"consigne_de_controle_externe": 460000}, "commande_argon/controle_externe"),
    ({"nombre_par_proposeur": 8}, "--nombre"),
])
def test_tailles_artefacts(modif, motif):
    m = json.loads(json.dumps(MESURE))
    m["consignes"].update(modif)
    with pytest.raises(lc.Refus, match=motif):
        lc.gardes_de_taille(m, lc.Reglages.production())


def test_tailles_artefact_garde_de_l_orchestrateur():
    m = json.loads(json.dumps(MESURE))
    m["garde_course"]["passerait"] = False
    with pytest.raises(lc.Refus, match="garde"):
        lc.gardes_de_taille(m, lc.Reglages.production())


def test_plancher_argon():
    # (4 096 + 8 192) × 41,5e-6 = 0,509952 ; contrôle court : ≈ 0,51 < 0,6 ; 0,2 ne suffirait pas (R-1864)
    assert lc.plancher_argon(0) == pytest.approx(0.509952)
    assert lc.plancher_argon(200) < lc.CONTROLE_BRAS_USD and lc.plancher_argon(200) > 0.2
