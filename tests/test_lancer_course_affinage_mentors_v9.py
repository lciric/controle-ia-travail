"""Essais du lanceur v9 de la course d'affinage des idées des mentors — les essais de la v8 portés (configuration v9 : plafond de session des proposeurs 3,00 USD ; parts au pire d'Astra et de Carbon 48, clé partagée 198 ; relais d'Astra à 48 USD dans le monde d'essai ; réglages de Carbon v9 : sortie retenue 32 768, pire cas 2,5715), puis les essais neufs de la v9 en fin de fichier.

Texte des essais v8 : essais du lanceur v8 de la course d'affinage des idées des mentors — les essais de la v7 portés (monde d'essai ajusté aux gardes v8 : état du relais de Carbon avec « releves » et « releves_restants » ; chemins `course-v8/` ; base du devis v8, 41,136 USD pour cinq espèces), et, en fin de fichier, les essais neufs de la v8 (un cas sain et un artefact par garde neuve, une mutation par garde, l'arithmétique de la garde recoupée avec la vraie commande de Carbon de `main`).

Texte des essais v7 : essais du lanceur v7 — les essais de la v6 portés (monde d'essai ajusté aux
gardes v7 : bornes basses de tous les relais, état lu complet, sonde commune liée, Kimi admis seulement par une référence de la
liste du lanceur), puis, en fin de fichier, les essais neufs de la v7 : un cas sain et un artefact (R5) par garde neuve, une
mutation par majeur (le code fautif réintroduit fait échouer un essai), et les essais de la v6b (sonde commune, commandes
réelles extraites de `main`) portés. Relais et orchestrateur **simulés** (sauf les essais qui jouent l'orchestrateur épinglé
en moteur simulé), aucun appel réel, aucun réseau, aucune clé."""
import datetime as dt
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_affinage_mentors_v9.py"
_spec = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v9", CHEMIN_LANCEUR)
L = importlib.util.module_from_spec(_spec)
sys.modules["lancer_course_affinage_mentors_v9"] = L
_spec.loader.exec_module(L)

AUJOURD_HUI = dt.date(2026, 11, 18)

FAUX_V8 = r'''
import json, os, sys
ici = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
comp = json.load(open(os.path.join(ici, "comportement.json")))
a = sys.argv[1:]
conf = json.load(open(a[a.index("--course-2") + 1]))
sortie = a[a.index("--course-2") + 2]
if "--verifier-seulement" in a:
    print(json.dumps({"montant_requis_go_usd": comp.get("montant", conf["budget"]["plafond_usd"]), "generations": 1, "go": None,
                      "specification": {"conforme": comp.get("spec", True)}, "configuration_sha256": "f" * 64}))
    sys.exit(comp.get("code_verif", 0))
arrete = False
if comp.get("executer"):
    import signal, subprocess, time
    etat = {"stop": False}
    signal.signal(signal.SIGTERM, lambda n, f: etat.__setitem__("stop", True))
    subprocess.run(conf["fournisseurs"][comp["executer"]]["commande"], input=b"consigne", capture_output=True)
    for _ in range(100):
        if etat["stop"]:
            break
        time.sleep(0.1)
    arrete = etat["stop"]
g = os.path.join(sortie, "generation-1")
os.makedirs(g)
cons = [{"fournisseur": f, "role": r, "cout_usd": c, "etape": "x"} for f, r, c in comp["couts"]]
cons.append({"fournisseur": "claude", "role": "plafond-relais", "cout_usd": 0.0, "etape": "x"})
json.dump({"consommations": cons}, open(os.path.join(g, "consommations.json"), "w"))
json.dump({"etapes": {"proposition": "jouee", "passe_tableau": "retiree"}, "noeud": None, "arret": None,
           "budget": {"cumul_usd": sum(c for _, _, c in comp["couts"])}}, open(os.path.join(g, "manifeste-fin.json"), "w"))
json.dump({"f1": {}, "f2": {}}, open(os.path.join(g, "fiches.json"), "w"))
json.dump(sorted(os.environ), open(os.path.join(sortie, "env-noms.json"), "w"))
json.dump({"cases": len(conf["cases"]), "proposeurs": [p["etiquette"] for p in conf["proposeurs"]],
           "interdites": conf["etiquettes_interdites"], "fournisseurs": sorted(conf["fournisseurs"]), "argv": a},
          open(os.path.join(sortie, "vu.json"), "w"))
sys.exit(2 if arrete else comp.get("code", 0))
'''

FAUX_ADAPTATEURS = r'''
import json, os
def etat_bac_a_sable_detaille():
    ici = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    comp = json.load(open(os.path.join(ici, "comportement.json")))
    return {"actif": comp.get("bac", True), "proc_neuf": comp.get("bac", True), "motif": "faux bac (essai)"}
'''

COUTS_SAINS = [("claude", "prop-opus", 2.0), ("claude", "prop-fable", 5.0), ("claude", "aiguilleur", 4.0),
               ("claude", "juge-opus", 5.0), ("argon", "prop-argon", 4.0), ("argon", "juge-argon", 5.0)]


def sceller(chemin: Path) -> None:
    h = hashlib.sha256(chemin.read_bytes()).hexdigest()
    Path(str(chemin) + ".sha256").write_text(f"{h}  {chemin.name}\n", encoding="utf-8")


def ecrire_scelle(chemin: Path, contenu) -> Path:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    texte = contenu if isinstance(contenu, str) else json.dumps(contenu, ensure_ascii=False, indent=1)
    chemin.write_text(texte, encoding="utf-8")
    sceller(chemin)
    return chemin


def git(d, *a):
    subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)


def faux_orchestrateur(tmp: Path, **comportement) -> tuple:
    o = tmp / "orchestrateur"
    (o / "demonstrations").mkdir(parents=True)
    (o / "pole").mkdir()
    (o / "demonstrations" / "ideation_v8.py").write_text(FAUX_V8, encoding="utf-8")
    (o / "pole" / "adaptateurs.py").write_text(FAUX_ADAPTATEURS, encoding="utf-8")
    (o / "pole" / "__init__.py").write_text("", encoding="utf-8")
    comportement.setdefault("couts", COUTS_SAINS)
    (o / "comportement.json").write_text(json.dumps(comportement), encoding="utf-8")
    git(o, "init", "-q", "-b", "main")
    git(o, "-c", "user.email=t@example.invalid", "-c", "user.name=t", "add", "-A")
    git(o, "-c", "user.email=t@example.invalid", "-c", "user.name=t", "commit", "-q", "-m", "faux")
    commit = subprocess.run(["git", "-C", str(o), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    empreintes = {rel: hashlib.sha256((o / rel).read_bytes()).hexdigest() for rel in ("demonstrations/ideation_v8.py", "pole/adaptateurs.py")}
    return o, commit, empreintes


from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading

FIXE = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
MODELES_CLAUDE = [e["modele"] for e in FIXE["especes"] if e["famille"] == "claude"]
CONTEXTE: dict = {}
PID_CLAUDE, PID_KIMI, PID_ARGON, PID_ASTRA, PID_CARBON = 424242, 424243, 424244, 424245, 424246


def serveur(etat: dict) -> ThreadingHTTPServer:
    """Relais factice local : ne sert que GET /relais/etat (aucune clé, aucun amont)."""
    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            corps = json.dumps(etat).encode()
            self.send_response(200 if self.path == "/relais/etat" else 404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(corps)

        def log_message(self, *a):
            pass
    s = ThreadingHTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s


def porte_commande(depot: Path, url: str, modeles: list) -> dict:
    return {"type": "commande", "delai_s": 10,
            "commande": [sys.executable, "-I", "-B", str(depot / L.PIECES["porte_plafond"][0]), "--url", url, "--modeles-permis",
                         ",".join(modeles), "--plafond-ligne", "150"]}


def declaration(depot: Path, mot_kimi=..., **modifs) -> dict:
    url = CONTEXTE["url_claude"]
    porte = porte_commande(depot, url, MODELES_CLAUDE)
    d = {"version": "essai", "fournisseurs": {
        "claude": {"type": "claude_sdk", "url_relais": url, "nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT", "porte_plafond": porte,
                   "pid_relais": PID_CLAUDE},
        "argon": {"type": "commande_externe", "commande": ["bash", str(depot / L.PIECES["enveloppe_argon"][0])],
                  "nom_cle": "CLE_ESSAI_A", "porte_plafond": {"type": "environnement"}, "pid_relais": PID_ARGON}}}
    d["fournisseurs"].update(modifs)
    if "kimi" in modifs and mot_kimi is not None:  # v6 : Kimi non déclaré par défaut, mot écrit de la mère exigé
        d["kimi_autorise_par_la_mere"] = {"reference": "R-9001"} if mot_kimi is ... else mot_kimi
    return d


def releve(**cles) -> dict:
    base = {"RR_ANTHROPIC_API_KEY_MINUIT": {"credit_usd": 1000.0, "reste_usd": 900.0, "source": "essai"},
            "CLE_ESSAI_A": {"credit_usd": 1000.0, "reste_usd": 800.0, "source": "essai"}}
    base.update(cles)
    return {"releve_utc": "2026-11-18T07:00:00Z", "cles": base}


def contre_lecture(prereg_sha: str, lanceur_sha: str, verdict="Scellable.", suite="") -> str:
    return (f"# Contre-lecture d'essai, par le modèle K\n\nPréenregistrement : {prereg_sha}\nLanceur : {lanceur_sha}\n\n"
            f"## Verdict\n\n**{verdict}**\n" + suite)


def ligne_go(plafond="150 USD", perimetre="course d'affinage des idées des mentors (organisme d'idéation)"):
    return (f"| id | accordé le | type | périmètre | plafond | échéance | accordé par | réf. |\n|---|---|---|---|---|---|---|---|\n"
            f"| {L.GO_ID} | 2026-11-18 | calcul | {perimetre} | {plafond} | 2026-11-30 | Lazar | R-3215 |\n")


SHA_ASTRA = L.COMMANDES_EPINGLEES["astra"]["commande_astra_v1.py"]


def sonde_astra(**modifs) -> dict:
    o = {"version": "sonde_astra_affinage_v2", "horodatage_utc": "2026-11-18T07:30:00Z", "code": 0, "ok": True, "cout_usd": 0.004,
         "modele_servi": "gpt-6-astra", "commande_sha256": SHA_ASTRA,
         "relais_url": "http://127.0.0.1:18790", "relais_pid": 999}
    o.update(modifs)
    return o


COMMUNE_DU_JOUR = "docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json"


def sonde_commune(v2_rel: str, v2_sha: str, pid: int = 999, commande_sha: str = SHA_ASTRA, **modifs) -> dict:
    """v7 : rapport de la sonde commune (format de `scripts/sonde_astra_courses_v1.py`) qui cite le rapport v2."""
    o = {"version": "sonde_astra_courses_v1", "horodatage_utc": "2026-11-18T07:29:55Z", "jour": "2026-11-18", "ok": True,
         "echec_de_configuration": False, "appel_envoye": True, "cout_usd": 0.004, "depense_relais_usd": 0.004, "motif": None,
         "commande": {"chemin": "/tmp/commande_astra_v1.py", "sha256": commande_sha},
         "sonde_v2": {"chemin": "scripts/sonde_astra_affinage_v2.py", "sha256": L.PIECES["sonde_astra"][1]},
         "relais_jete": {"pid": pid, "port": 8793, "url": "http://127.0.0.1:8793", "max_appels": 1, "plafond_usd": 0.05,
                         "reserve_par_appel_usd": 0.01, "programme_sha256": L.PROGRAMMES_RELAIS["astra"][1]},
         "rapport_v2": {"chemin": v2_rel, "sha256": v2_sha, "ok": True, "code_sonde_v2": 0}}
    o.update(modifs)
    return o


def ecrire_sondes(depot: Path, v2: dict | None = None, commune: dict | None = None, v2_rel: str = None,
                  commune_rel: str = COMMUNE_DU_JOUR) -> None:
    """v7 : écrit (ou remplace) le rapport v2 et le rapport de la sonde commune qui le cite par son empreinte."""
    v2_rel = v2_rel or L.SONDE_ASTRA
    for rel in (v2_rel, commune_rel):
        (depot / rel).unlink(missing_ok=True)
        Path(str(depot / rel) + ".sha256").unlink(missing_ok=True)
    v2 = sonde_astra() if v2 is None else v2
    ecrire_scelle(depot / v2_rel, v2)
    sha = hashlib.sha256((depot / v2_rel).read_bytes()).hexdigest()
    c = sonde_commune(v2_rel, sha, pid=v2.get("relais_pid", 999), commande_sha=v2.get("commande_sha256", SHA_ASTRA)) \
        if commune is None else commune
    ecrire_scelle(depot / commune_rel, c)


def releve_prix(**modifs) -> dict:
    prix = {"espece_claude_1": {"entree": 4.0, "sortie": 20.0}, "espece_claude_2": {"entree": 10.0, "sortie": 50.0}}
    prix.update(modifs)
    return {"releve_utc": "2026-11-18T06:55:00Z", "source": "essai : barème du relais", "prix": prix}


@pytest.fixture
def monde(tmp_path):
    """Dépôt d'essai : vraies pièces copiées (mêmes empreintes que les épingles), faux orchestrateur, relais simulés."""
    depot = tmp_path / "depot"
    for rel, _ in L.PIECES.values():
        (depot / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / rel, depot / rel)
    prereg = depot / L.PREREG
    prereg.parent.mkdir(parents=True, exist_ok=True)  # v7 : course-v7/ ne porte aucune pièce épinglée
    shutil.copy2(RACINE / L.PREREG, prereg)
    sceller(prereg)
    etat_claude = {"plafond_usd": 150.0, "depense_usd": 0.0, "engage_usd": 0.0, "appels": 0, "modeles_permis": list(MODELES_CLAUDE)}
    etat_kimi = {"plafond_usd": 30.0, "depense_usd": 0.0, "engage_usd": 0.0, "appels": 0, "modeles_permis": ["kimi-k3.1-pro"],
                 "max_appels": 20, "variable_cle_encore_presente": False, "reserve_par_appel_usd": 0.4}
    s_claude, s_kimi = serveur(etat_claude), serveur(etat_kimi)
    CONTEXTE.update(url_claude=f"http://127.0.0.1:{s_claude.server_address[1]}", url_kimi=f"http://127.0.0.1:{s_kimi.server_address[1]}")
    progs = tmp_path / "progs"
    progs.mkdir()
    (progs / "relais_reel.py").write_text("# relais factice\n", encoding="utf-8")
    (progs / "relais_kimi_v4.py").write_text("# relais factice kimi\n", encoding="utf-8")
    (progs / "relais_gemini_v2.py").write_text("# relais factice gemini v2\n", encoding="utf-8")
    (progs / "relais_gemini_v4.py").write_text("# relais factice gemini v4\n", encoding="utf-8")
    etats_gemini = {"8788": {"appels": 0, "variable_cle_encore_presente": False, "modeles": ["gemini-4-argon"], "max_appels": 450},
                    "8792": {"appels": 0, "variable_cle_encore_presente": False, "modeles": ["gemini-4-carbon"], "max_appels": 40,
                             "max_lots": 20, "lots_crees": 0, "releves": 0, "releves_restants": 2000},
                    "8790": {"appels": 0, "depense_usd": 0.0, "engage_usd": 0.0, "plafond_usd": 48.0, "modeles_permis": ["gpt-6-astra"],
                             "max_appels": 20, "variable_cle_encore_presente": False, "reserve_par_appel_usd": 0.4,
                             "prix_entree_usd_par_million": 10.0, "prix_sortie_usd_par_million": 50.0}}
    cmdlines = {PID_CLAUDE: [sys.executable, "-I", "-B", str(progs / "relais_reel.py"), "--variable-cle", "RR_ANTHROPIC_API_KEY_MINUIT",
                             "--port", CONTEXTE["url_claude"].rsplit(":", 1)[1], "--plafond-usd", "150", "--modeles-permis",
                             ",".join(MODELES_CLAUDE)],
                PID_KIMI: [sys.executable, "-I", "-B", str(progs / "relais_kimi_v4.py"), "--variable-cle", "CLE_ESSAI_K",
                           "--port", CONTEXTE["url_kimi"].rsplit(":", 1)[1], "--plafond-usd", "30", "--modeles-permis", "kimi-k3.1-pro",
                           "--max-appels", "20"],
                PID_ARGON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v2.py"), "--variable-cle", "CLE_ESSAI_A",
                            "--port", "8788", "--max-appels", "450", "--modele", "gemini-4-argon"],
                PID_ASTRA: [sys.executable, "-I", "-B", str(progs / "relais_kimi_v4.py"), "--amont", "https://api.openai.com",
                            "--variable-cle", "CLE_ESSAI_S", "--port", "8790", "--modeles-permis", "gpt-6-astra", "--plafond-usd", "48",
                            "--max-appels", "20"],
                PID_CARBON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v4.py"), "--variable-cle", "CLE_ESSAI_G",
                             "--port", "8792", "--max-appels", "40", "--max-lots", "20", "--modele", "gemini-4-carbon"]}
    o, commit, empreintes = faux_orchestrateur(tmp_path)
    lanceur_sha = hashlib.sha256(CHEMIN_LANCEUR.read_bytes()).hexdigest()
    ecrire_scelle(depot / L.CONTRE_LECTURE, contre_lecture(L.PREREG_SHA256, lanceur_sha))
    ecrire_scelle(depot / L.DECLARATION_RELAIS, declaration(depot))
    ecrire_scelle(depot / L.RELEVE_CREDITS, releve())
    ecrire_scelle(depot / L.RELEVE_PRIX, releve_prix())
    ecrire_sondes(depot)
    CONTEXTE["sonde"] = depot / L.SONDE_ASTRA
    (depot / "registres").mkdir()
    (depot / "registres" / "go.md").write_text(ligne_go(), encoding="utf-8")
    r = L.Reglages(depot=depot, orchestrateurs=(o,), commit_orchestrateur=commit, empreintes_orchestrateur=empreintes,
                   pieces=dict(L.PIECES), prereg=(prereg, L.PREREG_SHA256), contre_lecture=depot / L.CONTRE_LECTURE,
                   declaration=depot / L.DECLARATION_RELAIS, releve=depot / L.RELEVE_CREDITS,
                   registre_go=depot / "registres" / "go.md", procedure_relais=depot / L.PROCEDURE_RELAIS,
                   releve_prix=depot / L.RELEVE_PRIX, references_kimi_admises=("R-9001",), ref_registre=None, dossier_runs=depot / "runs", dossier_sorties=tmp_path / "sorties",
                   depot_attendu_par_l_enveloppe=depot, python=sys.executable, lanceur=CHEMIN_LANCEUR, moteur="reel",
                   environnement={"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "RR_ANTHROPIC_API_KEY_MINUIT": "valeur-secrete-essai-1",
                                  "RR_ANTHROPIC_API_KEY_RIGAUD": "valeur-secrete-essai-2"},
                   aujourd_hui=AUJOURD_HUI, horodatage=lambda: "Wed Nov 18 07:00:00 UTC 2026",
                   sorties_courses=tuple(tmp_path / f"sorties-anciennes-v{k}" for k in (1, 2, 3, 4, 5, 6, 7)),
                   programmes_relais={"claude": ("relais_reel.py", hashlib.sha256((progs / "relais_reel.py").read_bytes()).hexdigest()),
                                      "kimi": ("relais_kimi_v4.py", hashlib.sha256((progs / "relais_kimi_v4.py").read_bytes()).hexdigest()),
                                      "astra": ("relais_kimi_v4.py", hashlib.sha256((progs / "relais_kimi_v4.py").read_bytes()).hexdigest()),
                                      "argon": ("relais_gemini_v2.py", hashlib.sha256((progs / "relais_gemini_v2.py").read_bytes()).hexdigest()),
                                      "carbon": ("relais_gemini_v4.py", hashlib.sha256((progs / "relais_gemini_v4.py").read_bytes()).hexdigest())},
                   lire_cmdline=lambda pid: list(cmdlines[pid]),
                   lire_etat_relais=lambda url: dict(etats_par_port[url.rsplit(":", 1)[1]]))
    etats_par_port = dict(etats_gemini)
    etats_par_port[CONTEXTE["url_claude"].rsplit(":", 1)[1]] = etat_claude
    etats_par_port[CONTEXTE["url_kimi"].rsplit(":", 1)[1]] = etat_kimi
    yield {"r": r, "tmp": tmp_path, "depot": depot, "orch": o, "lanceur_sha": lanceur_sha, "etat_claude": etat_claude,
           "etat_kimi": etat_kimi, "cmdlines": cmdlines, "etats": etats_par_port}
    s_claude.shutdown()
    s_kimi.shutdown()


def lancer(r):
    return L.principal([], reglages=r)


def un_run(r):
    runs = [p for p in r.dossier_runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)]
    assert len(runs) == 1
    return runs[0]


def remplacer_orchestrateur(m, **comportement):
    shutil.rmtree(m["orch"])
    o, commit, empreintes = faux_orchestrateur(m["tmp"], **comportement)
    m["r"].orchestrateurs, m["r"].commit_orchestrateur, m["r"].empreintes_orchestrateur = (o,), commit, empreintes


# --- bout en bout (cas sain de toutes les gardes) ------------------------------------------------------------------------------


def test_bout_en_bout_sain_manifestes_couts_ecart(monde):
    r = monde["r"]
    assert lancer(r) == 0
    run = un_run(r)
    for nom in ("manifeste-lanceur-depart.json", "manifeste-lanceur-fin.json", "acte-de-gel.md", "configuration-orchestrateur.json"):
        assert L.scelle(run / nom), nom
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    # (4) R9 : configuration et empreinte, graines, versions, commit
    assert dep["configuration"]["sha256"] == L.sha256_fichier(run / "configuration-orchestrateur.json")
    assert dep["graines"]["racine"] == 2026111814 and "SeedSequence" in dep["graines"]["regle"]
    assert dep["versions"]["numpy"] and dep["versions"]["python"]
    assert "commit" in dep["depot_travail"] and dep["orchestrateur"]["commit"] == r.commit_orchestrateur
    assert dep["preenregistrement"]["sha256"] == L.PREREG_SHA256 and dep["go"]["plafond_lu"] == 150.0
    # espèces : Claude et Argon seuls déclarés → Kimi, Astra absentes ; Carbon non active
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon"]
    assert dep["carbon"]["active"] is False
    # (5) coût réel par relais, écart au devis
    assert fin["cout_reel"]["par_relais_usd"] == {"claude": 16.0, "argon": 9.0}
    assert fin["ecart_au_devis"]["par_role"]["prop-opus"]["devis_usd"] == pytest.approx(0.141)
    assert fin["releve_credits_apres"]["RR_ANTHROPIC_API_KEY_MINUIT"]["reste_estime_usd"] == pytest.approx(884.0)
    assert fin["alertes_apres"] == [] and fin["plafond_arret"]["depasse"] is False
    # l'orchestrateur a reçu seize cases, les retraits en étiquettes interdites, aucun nom de clé dans son environnement
    vu = json.loads((Path(dep["sortie"]) / "vu.json").read_text())
    assert vu["cases"] == 16 and "S3" in vu["interdites"] and "fc62b4ca23035" in vu["interdites"]
    assert "--confirmer-moteur-reel" in vu["argv"] and "--registre-go" in vu["argv"]
    noms = json.loads((Path(dep["sortie"]) / "env-noms.json").read_text())
    assert "RR_ANTHROPIC_API_KEY_MINUIT" not in noms and "RR_ANTHROPIC_API_KEY_RIGAUD" not in noms and "GO_ID" in noms
    # aucune valeur de clé écrite nulle part
    for p in list(run.iterdir()) + list(Path(dep["sortie"]).parent.rglob("*")):
        if p.is_file():
            assert "valeur-secrete-essai" not in p.read_text(errors="replace"), p


def test_course_deja_lancee_refusee(monde):
    assert lancer(monde["r"]) == 0
    assert lancer(monde["r"]) == 2


# --- (1) plafond d'arrêt -----------------------------------------------------------------------------------------------------


def test_go_plafond_autre_refuse(monde):
    monde["r"].registre_go.write_text(ligne_go("140 USD"), encoding="utf-8")
    assert lancer(monde["r"]) == 2
    assert not monde["r"].dossier_runs.exists()


def test_go_autre_perimetre_refuse(monde):
    monde["r"].registre_go.write_text(ligne_go(perimetre="collisionneur"), encoding="utf-8")
    assert lancer(monde["r"]) == 2


def test_configuration_fixe_sain_et_artefacts():
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    L.garde_configuration_fixe(fixe)
    for modif in (lambda f: f["budget"].__setitem__("plafond_usd", 151.0),
                  lambda f: f["budget"]["etapes"][3].__setitem__("plafond_relais_usd", 100.0),
                  lambda f: f["budget"]["etapes"][0].__setitem__("plafond_relais_usd", 120.0),
                  lambda f: f.__setitem__("etage_tests_de_mort", {"nombre": 1}),
                  lambda f: f.__setitem__("generations", 2)):
        f = json.loads(json.dumps(fixe))
        modif(f)
        with pytest.raises(L.Refus):
            L.garde_configuration_fixe(f)


def test_verification_orchestrateur_montant_autre_refuse(monde):
    remplacer_orchestrateur(monde, montant=140.0)
    assert lancer(monde["r"]) == 2
    runs = monde["r"].dossier_runs  # v6 : un refus avant la porte à blanc ne crée pas runs/<id>
    assert not (runs.is_dir() and [p for p in runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)])


def test_specification_non_conforme_refusee(monde):
    remplacer_orchestrateur(monde, spec=False)
    assert lancer(monde["r"]) == 2


def test_cumul_au_dela_du_plafond_alerte_code_4(monde):
    remplacer_orchestrateur(monde, couts=[("claude", "prop-opus", 100.0), ("argon", "juge-argon", 51.0)])
    assert lancer(monde["r"]) == 4
    run = un_run(monde["r"])
    assert L.scelle(run / "alerte-credits-apres.json")
    assert json.loads((run / "manifeste-lanceur-fin.json").read_text())["plafond_arret"]["depasse"] is True


# --- (2) crédits ---------------------------------------------------------------------------------------------------------------


def _releve(monde, objet):
    p = monde["r"].releve
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    ecrire_scelle(p, objet)


def test_credit_non_lisible_sans_dispense_refuse(monde):
    _releve(monde, releve(CLE_ESSAI_A={"non_lisible": True, "motif": "interface fermée"}))
    assert lancer(monde["r"]) == 2


def test_credit_non_lisible_avec_dispense_part(monde):
    objet = releve(CLE_ESSAI_A={"non_lisible": True, "motif": "interface fermée"})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_A"]}
    _releve(monde, objet)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["releve_credits_avant"]["cles"]["CLE_ESSAI_A"]["lisible"] is False


def test_credit_sous_un_cinquieme_alerte_code_3(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_MINUIT={"credit_usd": 5000.0, "reste_usd": 900.0, "source": "essai"}))
    assert lancer(monde["r"]) == 3
    alertes = [p for p in monde["r"].dossier_runs.iterdir() if p.name.endswith("-alerte-credits-affinage-mentors-v9")]
    assert len(alertes) == 1 and L.scelle(alertes[0] / "alerte-credits-avant.json")
    assert not [p for p in monde["r"].dossier_runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)]
    _releve(monde, releve())
    assert lancer(monde["r"]) == 0  # l'alerte ne bloque pas une course une fois la clé rechargée


def test_credit_sous_le_plafond_alerte_code_3(monde):
    _releve(monde, releve(CLE_ESSAI_A={"credit_usd": 160.0, "reste_usd": 149.0, "source": "essai"}))
    assert lancer(monde["r"]) == 3


def test_releve_perime_refuse(monde):
    objet = releve()
    objet["releve_utc"] = "2026-11-17T23:00:00Z"
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2


def test_releve_cle_omise_refuse(monde):
    objet = releve()
    del objet["cles"]["CLE_ESSAI_A"]
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2


def test_alerte_apres_si_reste_estime_sous_le_seuil(monde):
    _releve(monde, releve(CLE_ESSAI_A={"credit_usd": 1000.0, "reste_usd": 205.0, "source": "essai"}))
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["alertes_apres"] and fin["alertes_apres"][0]["cle"] == "CLE_ESSAI_A"
    assert L.scelle(run / "alerte-credits-apres.json")


# --- (3) préenregistrement, contre-lecture, retraits ----------------------------------------------------------------------------


def test_preenregistrement_autre_empreinte_refuse(monde):
    p = monde["r"].prereg[0]
    p.write_text(p.read_text() + "\nun octet de plus\n", encoding="utf-8")
    sceller(p)
    assert lancer(monde["r"]) == 2


def test_preenregistrement_non_scelle_refuse(monde):
    Path(str(monde["r"].prereg[0]) + ".sha256").unlink()
    assert lancer(monde["r"]) == 2


def _cl(monde, texte):
    c = monde["r"].contre_lecture
    c.unlink()
    Path(str(c) + ".sha256").unlink()
    ecrire_scelle(c, texte)


def test_contre_lecture_absente_refusee(monde):
    monde["r"].contre_lecture.unlink()
    assert lancer(monde["r"]) == 2


def test_contre_lecture_defavorable_refusee(monde):
    for verdict in ("Scellable après corrections.", "Non scellable.", "Scellable sous réserve."):
        _cl(monde, contre_lecture(L.PREREG_SHA256, monde["lanceur_sha"], verdict))
        assert lancer(monde["r"]) == 2, verdict


def test_contre_lecture_qui_ne_cite_pas_le_lanceur_refusee(monde):
    _cl(monde, contre_lecture(L.PREREG_SHA256, "0" * 64))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_non_scellee_refusee(monde):
    Path(str(monde["r"].contre_lecture) + ".sha256").unlink()
    assert lancer(monde["r"]) == 2


def test_verdicts():
    assert L.verdict_favorable("**Scellable.**") and L.verdict_favorable("Scellable.")
    for v in ("**Scellable après corrections.**", "Non scellable.", "Scellable sous réserve", "", None, "À sceller",
              "Scellable : rien à corriger", "Scellable", "Scellable. Deux remarques."):
        assert not L.verdict_favorable(v), v


def test_liste_sain_et_entree_servie_dans_les_retraits():
    liste = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
    c = L.verifier_liste(liste)
    assert c["fils"] == 16 and len(c["idees_retirees"]) == 14
    art = json.loads(json.dumps(liste))
    art["fils"][0]["idees_servies"].append({"numero": "S3", "texte_servi": "x"})
    with pytest.raises(L.Refus):
        L.verifier_liste(art)
    art = json.loads(json.dumps(liste))
    art["fils"][0]["idees_servies"][0]["texte_servi"] += " fe2f9cb3b665c"
    with pytest.raises(L.Refus):
        L.verifier_liste(art)


def test_piece_modifiee_refusee(monde):
    p = monde["depot"] / L.PIECES["consigne_juge"][0]
    p.write_text(p.read_text() + " ", encoding="utf-8")
    assert lancer(monde["r"]) == 2


# --- déclaration des relais, Carbon ---------------------------------------------------------------------------------------------


def _decl(monde, objet):
    p = monde["r"].declaration
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    ecrire_scelle(p, objet)


def test_declaration_valeur_de_cle_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = "sk-ant-" + "a" * 30
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_declaration_sans_claude_refusee(monde):
    d = declaration(monde["depot"])
    del d["fournisseurs"]["claude"]
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_declaration_adresse_hors_boucle_locale_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["url_relais"] = "http://10.0.0.5:8787"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_declaration_commande_argon_autre_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["commande"] = ["bash", "/tmp/autre.sh"]
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def epingler(monkeypatch, nom: str, script: Path) -> None:
    """Essais seulement : épingle une commande d'essai d'Astra ou de Carbon (la table du lanceur est vide en v4)."""
    monkeypatch.setitem(L.COMMANDES_EPINGLEES, nom, {script.name: hashlib.sha256(script.read_bytes()).hexdigest()})
    if nom == "astra" and CONTEXTE.get("sonde"):  # la sonde a été faite par cette commande (v7 : les deux rapports)
        depot = Path(str(CONTEXTE["sonde"])[: -len(L.SONDE_ASTRA) - 1])
        ecrire_sondes(depot, v2=sonde_astra(commande_sha256=hashlib.sha256(script.read_bytes()).hexdigest()))


def script_commande(dossier: Path, nom: str, ligne: dict) -> Path:
    script = dossier / f"{nom}.py"
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps(" + repr(ligne) + "))\n", encoding="utf-8")
    return script


def test_carbon_sans_inscription_inactive_et_avec_inscription_active(tmp_path, monkeypatch):
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    r = L.Reglages.production()
    CONTEXTE.setdefault("url_claude", "http://127.0.0.1:18787")
    sc = script_commande(tmp_path, "carbon", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "carbon", sc)
    carbon = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(sc)] + L.ARGUMENTS_COMMANDES["carbon"], "modele_propose": "gemini-4-carbon", "pid_relais": PID_CARBON, "nom_cle": "CLE_ESSAI_G",
              "porte_plafond": {"type": "environnement"}}
    d = L.verifier_declaration(declaration(r.depot, carbon=dict(carbon)), fixe, r)
    assert d["carbon"]["active"] is False and "carbon" not in d["fournisseurs"]
    d = L.verifier_declaration(declaration(r.depot, carbon=dict(carbon, inscription="R-3217")), fixe, r)
    assert d["carbon"]["active"] is True and d["cles"]["carbon"] == "CLE_ESSAI_G"
    assert [e["etiquette"] for e in d["especes_actives"]][-1] == "prop-carbon"
    d = L.verifier_declaration(declaration(r.depot), fixe, r)
    assert d["carbon"]["active"] is False and "non nommés" in d["carbon"]["motif"]
    with pytest.raises(L.Refus):
        L.verifier_declaration(declaration(r.depot, carbon=dict(carbon, inscription="R-3217", modele_propose="modele-autre")), fixe, r)


def test_espece_kimi_declaree_active(monde):
    _decl(monde, declaration(monde["depot"], kimi=kimi(monde)))
    _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 500.0, "reste_usd": 400.0, "source": "essai"}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-kimi" in dep["especes_actives"] and dep["cles_employees"]["kimi"] == "CLE_ESSAI_K"


# --- orchestrateur, bac à sable ---------------------------------------------------------------------------------------------------


def test_orchestrateur_modifie_refuse(monde):
    (monde["orch"] / "non-suivi.txt").write_text("x", encoding="utf-8")
    assert lancer(monde["r"]) == 2


def test_orchestrateur_autre_commit_refuse(monde):
    monde["r"].commit_orchestrateur = "0" * 40
    assert lancer(monde["r"]) == 2


def test_bac_a_sable_inactif_refuse(monde):
    remplacer_orchestrateur(monde, bac=False)
    assert lancer(monde["r"]) == 2


def test_arguments_refuses():
    assert L.principal(["--autre"]) == 2


# --- liste des fils : reconstruite par programme depuis le relevé, si `main` est là ------------------------------------------------


def test_liste_reconstruite_identique(tmp_path):
    p = subprocess.run(["git", "-C", str(RACINE), "show", "origin/main:" + "docs/notes/quatre-lectures-inventaire-v1/mentors-releve-d-ensemble-v1.md"],
                       capture_output=True)
    if p.returncode != 0:
        pytest.skip("relevé d'ensemble non disponible (origin/main non récupéré)")
    releve_ = tmp_path / "releve.md"
    releve_.write_bytes(p.stdout)
    sortie = tmp_path / "liste.json"
    q = subprocess.run([sys.executable, "-I", "-B", str(RACINE / "scripts" / "construire_fils_course_affinage_mentors_v1.py"),
                        str(releve_), str(sortie)], capture_output=True, text=True)
    assert q.returncode == 0, q.stderr
    assert hashlib.sha256(sortie.read_bytes()).hexdigest() == L.PIECES["liste_fils"][1]


# --- (1) plafond d'arrêt, sur le vrai orchestrateur (moteur simulé, appels fictifs chers) ----------------------------------------


def test_plafond_arret_coupe_la_course_avant_150_vrai_orchestrateur_simule(monde):
    """Artefact R5 de la garde (1) : chaque appel simulé coûte jusqu'à 1 USD (fictif, borné par le plafond de session) ; quatre
    espèces : proposition 64, aiguillage 32 ; les juges ne reçoivent qu'un plafond dur de 54 USD (150 − 96), sont coupés,
    la course s'arrête en nœud ; le cumul ne dépasse pas 150 et le lanceur écrit ce qui a été fait. Sauté si l'orchestrateur
    épinglé n'est pas sur cette machine."""
    presents = [o for o in L.ORCHESTRATEURS_CANDIDATS if (o / L.LANCEUR_ORCHESTRATEUR).is_file()]
    if len(presents) != 1:
        pytest.skip("orchestrateur épinglé absent")
    r, depot = monde["r"], monde["depot"]
    conf = depot / L.PIECES["configuration"][0]
    fixe = json.loads(conf.read_text())
    fixe["simulation"]["cout_par_appel_usd"] = 1.0
    conf.write_text(json.dumps(fixe, ensure_ascii=False), encoding="utf-8")
    r.pieces = dict(r.pieces, configuration=(L.PIECES["configuration"][0], L.sha256_fichier(conf)))
    r.orchestrateurs, r.commit_orchestrateur = tuple(presents), L.COMMIT_ORCHESTRATEUR
    r.empreintes_orchestrateur = dict(L.EMPREINTES_ORCHESTRATEUR)
    r.moteur, r.verifier_go, r.exiger_bac_a_sable = "simule", False, False
    kimi = {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:18788", "modele": "kimi-k3.1-pro", "prix_entree": 1.0,
            "prix_sortie": 2.0, "max_sortie_jetons": 1000, "sortie_min_jetons": 100, "delai_s": 60, "nom_cle": "CLE_ESSAI_K",
            "porte_plafond": {"type": "commande", "commande": ["/bin/true"], "delai_s": 5}}
    _decl(monde, declaration(depot, kimi=kimi))
    _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 500.0, "reste_usd": 400.0, "source": "essai"}))
    assert lancer(r) == 6  # nœud de l'orchestrateur : v7, code 6 (distinct du refus avant départ), manifeste de fin écrit
    fin = json.loads((un_run(r) / "manifeste-lanceur-fin.json").read_text())
    fait = fin["ce_qui_a_ete_fait"]
    assert fait["etapes"]["proposition"] == "jouee" and fait["etapes"]["aiguillage"] == "jouee"
    assert fait["etapes"]["juges"] == "non_mesuree_budget" and fait["noeud"]
    assert fin["cout_reel"]["total_usd"] <= 150.0 and fin["plafond_arret"]["depasse"] is False
    assert fin["cout_reel"]["coupures"] == ["juges"]
    assert not subprocess.run(["git", "-C", str(presents[0]), "status", "--porcelain", "--ignored"], capture_output=True,
                              text=True).stdout.strip()


# --- v2 : clé Minuit, Rigaud exclue, contre-lecture du modèle K ----------------------------------------------------------------


def test_variable_minuit_absente_arret_au_depart(monde):
    r = monde["r"]
    r.environnement = {k: v for k, v in r.environnement.items() if k != L.CLE_CLAUDE}
    assert lancer(r) == 2
    assert not r.dossier_runs.exists()
    r.environnement[L.CLE_CLAUDE] = "x"  # cas sain : présente par son nom
    assert lancer(r) == 0


def test_relais_claude_sur_rigaud_refuse(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_RIGAUD"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_relais_claude_sur_une_autre_cle_refuse(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_3"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_cle_claude_sur_un_autre_relais_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_MINUIT"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_configuration_cles_sain_et_artefacts():
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    L.garde_cles_configuration(fixe)
    for modif in (lambda f: f["cles"].__setitem__("claude", "RR_ANTHROPIC_API_KEY_RIGAUD"),
                  lambda f: f.__setitem__("cles_interdites", []),
                  lambda f: f["especes"][1].__setitem__("cle", "RR_ANTHROPIC_API_KEY_RIGAUD")):
        f = json.loads(json.dumps(fixe))
        modif(f)
        with pytest.raises(L.Refus):
            L.garde_cles_configuration(f)


def test_minuit_non_lisible_compte_au_prix_releve(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_MINUIT={"non_lisible": True, "depense_anterieure_usd": 0.0}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    c = dep["releve_credits_avant"]["cles"][L.CLE_CLAUDE]
    assert c["reste_usd"] == 200.0 and "compté" in c["source"]
    assert dep["cle_par_espece"]["prop-opus"] == L.CLE_CLAUDE and dep["cle_par_role_interne"]["aiguilleur"] == L.CLE_CLAUDE


def test_minuit_compte_sous_le_plafond_alerte_code_3(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_MINUIT={"non_lisible": True, "depense_anterieure_usd": 60.0}))
    assert lancer(monde["r"]) == 3


def test_minuit_non_lisible_sans_depense_anterieure_refuse(monde):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_MINUIT={"non_lisible": True}))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_qui_dit_n_avoir_pas_relu_refusee(monde):
    _cl(monde, contre_lecture(L.PREREG_SHA256, monde["lanceur_sha"], suite="\nLimite : je n'ai pas relu le lanceur en entier.\n"))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_sans_modele_k_refusee(monde):
    _cl(monde, contre_lecture(L.PREREG_SHA256, monde["lanceur_sha"]).replace("par le modèle K", "par un relecteur"))
    assert lancer(monde["r"]) == 2


def test_course_v1_deja_lancee_bloque_la_v2(monde):
    d = monde["r"].dossier_runs / "20261118-000000-course-affinage-mentors-v1"
    d.mkdir(parents=True)
    (d / "manifeste-lanceur-depart.json").write_text("{}", encoding="utf-8")
    assert lancer(monde["r"]) == 2


# --- v3 : règle de clé par part, Kimi, dispense R-3237, arrêt au premier refus pour crédit, procédure des relais ----------------

KIMI = {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:18788", "modele": "kimi-k3.1-pro", "prix_entree": 1.0,
        "prix_sortie": 2.0, "max_sortie_jetons": 1000, "sortie_min_jetons": 100, "delai_s": 60, "nom_cle": "CLE_ESSAI_K",
        "porte_plafond": {"type": "commande", "commande": ["PROCEDURE"], "delai_s": 5}}


def kimi(monde, **prix):
    k = dict(KIMI, **prix)
    k["url_relais"] = CONTEXTE["url_kimi"]
    k["pid_relais"] = PID_KIMI
    k["porte_plafond"] = porte_commande(monde["depot"], CONTEXTE["url_kimi"], ["kimi-k3.1-pro"])
    return k


def test_parts_au_pire(tmp_path, monkeypatch):
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    liste = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
    r = L.Reglages.production()
    r.references_kimi_admises = ("R-9001",)  # v7 : liste vide en production ; admise ici pour calculer la part de Kimi
    CONTEXTE.setdefault("url_claude", "http://127.0.0.1:18787")
    pieces = {n: {"absolu": str(RACINE / rel)} for n, (rel, _) in L.PIECES.items()}
    sa = script_commande(tmp_path, "astra", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "astra", sa)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(sa)] + L.ARGUMENTS_COMMANDES["astra"], "modele_propose": "gpt-6-astra", "pid_relais": PID_ASTRA, "nom_cle": "CLE_ESSAI_S",
             "porte_plafond": {"type": "environnement"}}
    k = dict(KIMI, prix_entree=10.0, prix_sortie=20.0, max_sortie_jetons=40000)
    d = L.verifier_declaration(declaration(r.depot, kimi=k, astra=astra), fixe, r)
    parts = L.parts_au_pire(fixe, liste, pieces, d)
    assert parts["claude"]["part_au_pire_usd"] == 150.0 and parts["argon"]["part_au_pire_usd"] == 150.0
    assert parts["astra"]["part_au_pire_usd"] == 48.0  # v9 : 16 × 3,00
    entree = len((RACINE / L.PIECES["consigne_proposeur"][0]).read_bytes()) + max(
        len(L.texte_de_case(f).encode()) for f in liste["fils"]) + 200
    attendu = ((entree + 1024) * 10.0 + 40000 * 20.0) / 1e6
    assert parts["kimi"]["par_appel_usd"] == pytest.approx(attendu) and parts["kimi"]["part_au_pire_usd"] == pytest.approx(16 * attendu)


def test_kimi_part_et_course_suivante_sain_et_artefact(monde):
    # sain : 16 × (8949 × 1 + 50 000 × 20) / 1e6 ≈ 16,14 ; + 11,3 = 27,44 ≤ 0,9 × 32,25 = 29,03
    _decl(monde, declaration(monde["depot"], kimi=kimi(monde, prix_sortie=20.0, max_sortie_jetons=50000)))
    _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 32.25, "reste_usd": 32.25, "source": "essai"}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["parts_au_pire"]["kimi"]["part_au_pire_usd"] < 17.73


def test_kimi_part_trop_haute_refus_les_courses_se_suivent(monde, capsys):
    # artefact : 16 × (8949 + 55 000 × 20) / 1e6 ≈ 17,74 ; + 11,3 = 29,04 > 29,03
    _decl(monde, declaration(monde["depot"], kimi=kimi(monde, prix_sortie=20.0, max_sortie_jetons=55000)))
    _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 32.25, "reste_usd": 32.25, "source": "essai"}))
    assert lancer(monde["r"]) == 3
    assert "les deux courses doivent se suivre" in capsys.readouterr().err


def test_part_au_pire_et_non_plafond_global(monde, monkeypatch):
    # une clé d'Astra à 60 USD : sous 150 (v2 : refus) mais au-dessus de sa part au pire (v9 : 48) et de son cinquième → départ
    script = monde["tmp"] / "astra.py"
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps({'texte': '', 'cout_usd': 0.01}))\n", encoding="utf-8")
    epingler(monkeypatch, "astra", script)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script)] + L.ARGUMENTS_COMMANDES["astra"], "modele_propose": "gpt-6-astra", "pid_relais": PID_ASTRA,
             "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    _releve(monde, releve(CLE_ESSAI_S={"credit_usd": 60.0, "reste_usd": 60.0, "source": "essai"}))
    assert lancer(monde["r"]) == 0
    _releve(monde, releve(CLE_ESSAI_S={"credit_usd": 60.0, "reste_usd": 47.0, "source": "essai"}))
    monde["r"].dossier_runs = monde["tmp"] / "runs-bis"
    assert lancer(monde["r"]) == 3


def test_dispense_autre_reference_refusee(monde):
    objet = releve(CLE_ESSAI_A={"non_lisible": True})
    objet["dispense"] = {"par": "mère", "reference": "R-9999", "cles": ["CLE_ESSAI_A"]}
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2


def test_dispense_sur_une_cle_non_dispensable_refusee(monde):
    _decl(monde, declaration(monde["depot"], kimi=kimi(monde)))
    objet = releve(CLE_ESSAI_K={"non_lisible": True})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_K"]}
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2


def _astra_dispensee(monde, ligne, monkeypatch):
    script = monde["tmp"] / "astra.py"
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps(" + repr(ligne) + "))\n", encoding="utf-8")
    epingler(monkeypatch, "astra", script)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script)] + L.ARGUMENTS_COMMANDES["astra"], "modele_propose": "gpt-6-astra", "pid_relais": PID_ASTRA,
             "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    objet = releve(CLE_ESSAI_S={"non_lisible": True, "motif": "solde illisible (R-3222)"})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S"]}
    _releve(monde, objet)
    remplacer_orchestrateur(monde, executer="astra")


def test_premier_refus_pour_credit_arrete_la_course_code_5(monde, monkeypatch):
    _astra_dispensee(monde, {"texte": "", "cout_usd": 0.01, "erreur": "HTTP 402 payment required : credit balance too low"}, monkeypatch)
    assert lancer(monde["r"]) == 5
    run = un_run(monde["r"])
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["arret_au_premier_refus_pour_credit"][0]["relais"] == "astra" and fin["code"] == 2
    assert L.scelle(run / "alerte-arret-credit.json")  # constat 12


def test_limite_de_debit_n_arrete_pas_la_course(monde, monkeypatch):
    _astra_dispensee(monde, {"texte": "", "cout_usd": 0.01, "erreur": "429 RESOURCE_EXHAUSTED: rate limit per minute"}, monkeypatch)
    assert lancer(monde["r"]) == 0


def test_appel_sans_refus_pour_credit_ne_s_arrete_pas(monde, monkeypatch):
    _astra_dispensee(monde, {"texte": "réponse", "cout_usd": 0.01, "modele_servi": "modele-essai-astra"}, monkeypatch)
    assert lancer(monde["r"]) == 0
    fin = json.loads((un_run(monde["r"]) / "manifeste-lanceur-fin.json").read_text())
    assert fin["arret_au_premier_refus_pour_credit"] == []


def test_garde_credit_v5_motifs():
    spec = importlib.util.spec_from_file_location("garde_v5", RACINE / "scripts" / "garde_credit_relais_v5.py")
    G = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(G)
    j = lambda e: json.dumps({"texte": "", "cout_usd": 0.01, "erreur": e})  # noqa: E731
    for e in ("HTTP 402 payment required", "insufficient_quota: check your billing details", "crédits épuisés",
              "Your prepayment credits are depleted", "RESOURCE_EXHAUSTED: billing account quota", "credit balance is too low"):
        assert G.motif_credit(j(e), "", 1), e
    assert G.motif_credit("", "billing hard limit reached", 1)
    for e in ("429 RESOURCE_EXHAUSTED: rate limit per minute", "délai dépassé", "quota exceeded"):
        assert not G.motif_credit(j(e), "", 1), e
    assert not G.motif_credit(j(""), "appel en 402 ms", 1)
    assert not G.motif_credit(j(""), "note: billing metadata absent", 1)
    assert not G.motif_credit('{"texte": "ok", "cout_usd": 0.2}', "credit balance is too low", 0)  # code 0 : stderr non lue
    assert not G.motif_credit('{"texte": "une carte sur le crédit d\'une idée", "cout_usd": 0.2}', "", 0)


def _procedure(monde, objet=None, texte=None):
    p = monde["depot"] / L.PROCEDURE_RELAIS
    p.unlink()
    Path(str(p) + ".sha256").unlink(missing_ok=True)
    ecrire_scelle(p, texte if texte is not None else objet)


def test_procedure_a_remplir_refusee(monde):
    _procedure(monde, texte='{"chemin": "À REMPLIR", "sha256": "À REMPLIR"}')
    assert lancer(monde["r"]) == 2


def test_procedure_absente_refusee(monde):
    p = monde["depot"] / L.PROCEDURE_RELAIS
    p.unlink()
    assert lancer(monde["r"]) == 2


def test_procedure_autre_empreinte_refusee(monde):
    _procedure(monde, {"chemin": str(monde["tmp"] / "procedure-relais.sh"), "sha256": "0" * 64})
    assert lancer(monde["r"]) == 2


def test_porte_qui_ne_lance_pas_la_procedure_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["porte_plafond"]["commande"] = ["/bin/true"]
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


# --- v4 : constats de la contre-lecture de la v3 ------------------------------------------------------------------------------


def _orch_present():
    presents = [o for o in L.ORCHESTRATEURS_CANDIDATS if (o / L.LANCEUR_ORCHESTRATEUR).is_file()]
    if len(presents) != 1:
        pytest.skip("orchestrateur épinglé absent")
    return presents[0]


def _classe_porte():
    o = _orch_present()
    sys.path.insert(0, str(o))
    ancien, sys.dont_write_bytecode = sys.dont_write_bytecode, True  # l'arbre de l'orchestrateur reste propre
    try:
        from pole.adaptateurs_v56 import PortePlafondCommande, RelaisSansPlafond
    finally:
        sys.path.remove(str(o))
        sys.dont_write_bytecode = ancien
    return PortePlafondCommande, RelaisSansPlafond


def test_porte_avec_la_vraie_classe_de_l_orchestrateur_sain_et_artefacts(monde):
    """Constat 1, R5 : la porte épinglée rejouée par `PortePlafondCommande` (classe réelle), relais factice local."""
    Porte, RelaisSansPlafond = _classe_porte()
    c = porte_commande(monde["depot"], CONTEXTE["url_claude"], MODELES_CLAUDE)["commande"]
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8"}
    assert Porte(c, 10, environnement=env).transmettre("proposition", 130.0)["plafond_usd"] == 130.0
    monde["etat_claude"]["depense_usd"] = 12.5  # en cours de course : accepté
    assert Porte(c, 10, environnement=env).transmettre("juges", 47.12)["plafond_usd"] == 47.12
    for modif in ({"plafond_usd": 200.0}, {"modeles_permis": ["autre-modele"]}, {"depense_usd": 151.0}):
        etat = dict(monde["etat_claude"])
        monde["etat_claude"].update(modif)
        with pytest.raises(RelaisSansPlafond):
            Porte(c, 10, environnement=env).transmettre("proposition", 130.0)
        monde["etat_claude"].clear()
        monde["etat_claude"].update(etat)
    with pytest.raises(RelaisSansPlafond):  # relais injoignable
        Porte(porte_commande(monde["depot"], "http://127.0.0.1:9", MODELES_CLAUDE)["commande"], 10,
              environnement=env).transmettre("proposition", 130.0)
    with pytest.raises(RelaisSansPlafond):  # la porte de la v3 (lanceur de relais) ne rend aucun accusé
        Porte([sys.executable, "-I", "-B", str(monde["depot"] / L.PIECES["lanceur_relais"][0])], 10,
              environnement=env).transmettre("proposition", 130.0)


def test_relais_deja_employe_refuse_avant_le_depart(monde):
    monde["etat_claude"]["depense_usd"] = 0.5
    monde["etat_claude"]["appels"] = 1
    assert lancer(monde["r"]) == 2
    runs = [p for p in monde["r"].dossier_runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)] if monde["r"].dossier_runs.is_dir() else []
    assert all(not (p / "manifeste-lanceur-depart.json").exists() for p in runs)  # tentative non brûlée


def test_refus_de_porte_a_blanc_puis_relance_acceptee(monde):
    """v5, constat 1 : un refus à la porte à blanc ne laisse ni dossier de sortie ni journal ; la relance part."""
    port = CONTEXTE["url_claude"].rsplit(":", 1)[1]
    monde["etats"][port] = dict(monde["etat_claude"])  # état lu par le lanceur : neuf
    monde["etat_claude"]["plafond_usd"] = 200.0  # état lu par la porte : plafond hors ligne → porte refusée
    assert lancer(monde["r"]) == 2
    runs = monde["r"].dossier_runs
    assert not (runs.is_dir() and [p for p in runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)])  # v6 : rien au dépôt
    sorties = monde["r"].dossier_sorties
    restes = sorted(p.name for p in sorties.iterdir()) if sorties.is_dir() else []
    assert all(n.endswith("-preparation") for n in restes)  # seule la préparation, hors dépôt, reste du refus
    monde["etat_claude"]["plafond_usd"] = 150.0
    assert lancer(monde["r"]) == 0  # même seconde possible : identifiant à la microseconde
    assert len([p for p in runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)]) == 1


def test_porte_a_blanc_au_manifeste(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["porte_a_blanc"]["claude"]["accuse"]["etape"] == "porte-a-blanc"
    assert dep["procedure_relais_persistants"]["relais_vivants"]["claude"]["variable_cle"] == "RR_ANTHROPIC_API_KEY_MINUIT"
    assert dep["releve_prix_claude"]["egal_au_bareme"] is True
    assert dep["registre_go_derive"]["nombre_de_lignes"] == 1


def test_commande_de_porte_qui_ne_commence_pas_par_la_porte_refusee(monde):
    d = declaration(monde["depot"])
    c = d["fournisseurs"]["claude"]["porte_plafond"]["commande"]
    d["fournisseurs"]["claude"]["porte_plafond"]["commande"] = ["/bin/sh", "-c", "true", c[3]]  # cite le chemin sans le lancer
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def test_relais_vivant_sur_rigaud_refuse(monde):
    args = monde["cmdlines"][PID_CLAUDE]
    args[args.index("--variable-cle") + 1] = "RR_ANTHROPIC_API_KEY_RIGAUD"
    assert lancer(monde["r"]) == 2


def test_relais_vivant_plafond_autre_que_150_refuse(monde):
    args = monde["cmdlines"][PID_CLAUDE]
    args[args.index("--plafond-usd") + 1] = "100"
    assert lancer(monde["r"]) == 2


def test_relais_vivant_programme_d_une_autre_empreinte_refuse(monde):
    p = [a for a in monde["cmdlines"][PID_CLAUDE] if a.endswith("relais_reel.py")][0]
    Path(p).write_text("# autre programme\n", encoding="utf-8")
    assert lancer(monde["r"]) == 2


def _registre(monde, texte):
    monde["r"].registre_go.write_text(texte, encoding="utf-8")


REGISTRE_AVEC_DOUBLONS = (ligne_go() + "| GO-2026-10-24-07 | 2026-10-24 | calcul | essai | 10 USD | 2026-10-30 | Lazar | R-1 |\n"
                          "| GO-2026-10-24-07 | 2026-10-25 | calcul | extension de GO-2026-10-24-07 | 12 USD | 2026-10-31 | Lazar | R-2 |\n")


def test_registre_derive_accepte_par_l_orchestrateur_et_source_refusee(monde, tmp_path):
    """Constat 2, R5 : la vraie lecture de l'orchestrateur refuse le registre à doublons, accepte le registre dérivé, refuse un
    registre dérivé falsifié."""
    o = _orch_present()
    sys.path.insert(0, str(o))
    ancien, sys.dont_write_bytecode = sys.dont_write_bytecode, True  # l'arbre de l'orchestrateur reste propre
    try:
        from pole.configuration_v55 import verifier_go_v55
        from pole.configuration_v53 import GoRefuse
    finally:
        sys.path.remove(str(o))
        sys.dont_write_bytecode = ancien
    _registre(monde, REGISTRE_AVEC_DOUBLONS)
    with pytest.raises(GoRefuse):
        verifier_go_v55(L.GO_ID, str(monde["r"].registre_go), 150.0, aujourd_hui=AUJOURD_HUI)
    d = L.ecrire_registre_derive(monde["r"].registre_go, tmp_path / "derive.md")
    assert verifier_go_v55(L.GO_ID, d["derive"], 150.0, aujourd_hui=AUJOURD_HUI)["plafond_lu_usd"] == 150.0
    faux = tmp_path / "derive-falsifie.md"
    faux.write_text(Path(d["derive"]).read_text().replace("| 150 USD |", "| 140 USD |"), encoding="utf-8")
    with pytest.raises(GoRefuse):
        verifier_go_v55(L.GO_ID, str(faux), 150.0, aujourd_hui=AUJOURD_HUI)
    assert lancer(monde["r"]) == 0  # le lanceur part avec le registre à doublons de main
    vu = json.loads((Path(json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())["sortie"]) / "vu.json").read_text())
    assert vu["argv"][vu["argv"].index("--registre-go") + 1].endswith("registre-go-derive.md")


def test_revocation_incluse_au_registre_derive(monde, tmp_path):
    _registre(monde, ligne_go() + f"| GO-2026-11-19-01 | 2026-11-19 | révocation | révoque {L.GO_ID} | — | — | Lazar | R-9 |\n")
    d = L.ecrire_registre_derive(monde["r"].registre_go, tmp_path / "derive.md")
    assert d["nombre_de_lignes"] == 2


def _prix(monde, objet):
    p = monde["r"].releve_prix
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    ecrire_scelle(p, objet)


def test_releve_prix_absent_refuse(monde):
    monde["r"].releve_prix.unlink()
    assert lancer(monde["r"]) == 2


def test_releve_prix_different_du_bareme_refuse(monde):
    _prix(monde, releve_prix(espece_claude_2={"entree": 12.0, "sortie": 60.0}))
    assert lancer(monde["r"]) == 2


def test_releve_prix_d_hier_refuse(monde):
    o = releve_prix()
    o["releve_utc"] = "2026-11-17T23:00:00Z"
    _prix(monde, o)
    assert lancer(monde["r"]) == 2


def test_variable_minuit_vide_refusee(monde):
    monde["r"].environnement[L.CLE_CLAUDE] = ""
    assert lancer(monde["r"]) == 2


def test_kimi_zeros_refuses(monde):
    for modif in ({"prix_entree": 0.0}, {"prix_sortie": 0}, {"max_sortie_jetons": 0}, {"sortie_min_jetons": 0}, {"delai_s": 0},
                  {"max_sortie_jetons": 1000.0}, {"sortie_min_jetons": 2000}):
        _decl(monde, declaration(monde["depot"], kimi=kimi(monde, **modif)))
        _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 500.0, "reste_usd": 400.0, "source": "essai"}))
        assert lancer(monde["r"]) == 2, modif


def test_astra_non_epinglee_refusee(monde):
    s = script_commande(monde["tmp"], "astra-non-epinglee", {"texte": "", "cout_usd": 0.01})
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(s)] + L.ARGUMENTS_COMMANDES["astra"], "modele_propose": "gpt-6-astra", "pid_relais": PID_ASTRA,
             "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    _releve(monde, releve(CLE_ESSAI_S={"credit_usd": 60.0, "reste_usd": 60.0, "source": "essai"}))
    assert lancer(monde["r"]) == 2


def test_reste_egal_a_la_part_refuse(monde, monkeypatch):
    s = script_commande(monde["tmp"], "astra", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "astra", s)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(s)] + L.ARGUMENTS_COMMANDES["astra"], "modele_propose": "gpt-6-astra", "pid_relais": PID_ASTRA,
             "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    _releve(monde, releve(CLE_ESSAI_S={"credit_usd": 100.0, "reste_usd": 48.0, "source": "essai"}))
    assert lancer(monde["r"]) == 3


def test_sorties_hors_depot_d_une_course_anterieure_refusees(monde):
    d = monde["r"].sorties_courses[2] / "20261118-000000-course-affinage-mentors-v3"
    (d / "arrets-credit").mkdir(parents=True)  # dossier laissé par un refus : ne compte pas (v5, constat 1)
    assert lancer(monde["r"]) == 0
    monde["r"].dossier_runs = monde["tmp"] / "runs-bis"
    (d / "course.stdout.txt").write_text("", encoding="utf-8")  # journal : la course a été lancée
    assert lancer(monde["r"]) == 2


def test_arbre_de_l_orchestrateur_reste_propre():
    o = _orch_present()
    assert not subprocess.run(["git", "-C", str(o), "status", "--porcelain", "--ignored"], capture_output=True, text=True).stdout.strip()


# --- v5 : constats 2 à 5 de la contre-lecture de la v4 ; Carbon ; Astra ; confidentialité ---------------------------------------


def _porte_arg(monde, nom_arg, valeur):
    d = declaration(monde["depot"])
    c = d["fournisseurs"]["claude"]["porte_plafond"]["commande"]
    c[c.index(nom_arg) + 1] = valeur
    _decl(monde, d)


def test_porte_plafond_ligne_autre_que_150_refusee(monde):
    _porte_arg(monde, "--plafond-ligne", "5000")
    assert lancer(monde["r"]) == 2


def test_porte_url_autre_que_le_relais_declare_refusee(monde):
    _porte_arg(monde, "--url", "http://127.0.0.1:9")
    assert lancer(monde["r"]) == 2


def test_porte_modeles_partiels_refusee(monde):
    _porte_arg(monde, "--modeles-permis", MODELES_CLAUDE[0])
    assert lancer(monde["r"]) == 2


def test_relais_vivant_modeles_differents_refuse(monde):
    args = monde["cmdlines"][PID_CLAUDE]
    args[args.index("--modeles-permis") + 1] = MODELES_CLAUDE[0]
    assert lancer(monde["r"]) == 2


def test_relais_argon_max_appels_insuffisant_refuse(monde):
    args = monde["cmdlines"][PID_ARGON]
    args[args.index("--max-appels") + 1] = "50"
    assert lancer(monde["r"]) == 2


def test_relais_argon_cle_non_effacee_refuse(monde):
    monde["etats"]["8788"]["variable_cle_encore_presente"] = True
    assert lancer(monde["r"]) == 2


def test_relais_argon_deja_employe_refuse(monde):
    monde["etats"]["8788"]["appels"] = 3
    assert lancer(monde["r"]) == 2


def test_relais_argon_autre_port_refuse(monde):
    args = monde["cmdlines"][PID_ARGON]
    args[args.index("--port") + 1] = "8791"
    assert lancer(monde["r"]) == 2


def test_relais_argon_sans_pid_refuse(monde):
    d = declaration(monde["depot"])
    del d["fournisseurs"]["argon"]["pid_relais"]
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


def _carbon(monde, monkeypatch, **modifs):
    sc = script_commande(monde["tmp"], "commande_gemini_lot_v1", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "carbon", sc)
    c = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(sc)] + L.ARGUMENTS_COMMANDES["carbon"],
         "modele_propose": "gemini-4-carbon", "nom_cle": "CLE_ESSAI_G", "inscription": "R-3217", "pid_relais": PID_CARBON,
         "porte_plafond": {"type": "environnement"}}
    c.update(modifs)
    _decl(monde, declaration(monde["depot"], carbon=c))
    objet = releve(CLE_ESSAI_A={"non_lisible": True}, CLE_ESSAI_G={"non_lisible": True})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_A", "CLE_ESSAI_G"]}
    _releve(monde, objet)


def test_carbon_declaree_part_au_pire_et_relais_controle(monde, monkeypatch):
    _carbon(monde, monkeypatch)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-carbon" in dep["especes_actives"] and dep["parts_au_pire"]["carbon"]["part_au_pire_usd"] == 48.0
    assert dep["procedure_relais_persistants"]["relais_vivants"]["carbon"]["max_lots"] == 20  # v7 : marge de 4 lots


def test_carbon_arguments_autres_refuses(monde, monkeypatch):
    sc = script_commande(monde["tmp"], "commande_gemini_lot_v1", {"texte": "", "cout_usd": 0.01})
    args = list(L.ARGUMENTS_COMMANDES["carbon"])
    args[args.index("--delai-s") + 1] = "3000"
    _carbon(monde, monkeypatch, commande=[sys.executable, "-I", "-B", str(sc)] + args)
    assert lancer(monde["r"]) == 2


def test_carbon_relais_max_lots_insuffisant_refuse(monde, monkeypatch):
    _carbon(monde, monkeypatch)
    args = monde["cmdlines"][PID_CARBON]
    args[args.index("--max-lots") + 1] = "8"
    assert lancer(monde["r"]) == 2


def _astra(monde, monkeypatch):
    s = script_commande(monde["tmp"], "commande_astra_v1", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "astra", s)
    a = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(s)] + L.ARGUMENTS_COMMANDES["astra"],
         "modele_propose": "gpt-6-astra", "pid_relais": PID_ASTRA, "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=a))
    _releve(monde, releve(CLE_ESSAI_S={"credit_usd": 100.0, "reste_usd": 90.0, "source": "essai"}))
    return s


def _sonde(monde, **modifs):
    """v7 : modifie le rapport v2 et réécrit la sonde commune qui le cite (même commande, même relais jeté), pour que le refus
    attendu vienne bien du champ modifié et non de l'empreinte."""
    p = monde["depot"] / L.SONDE_ASTRA
    o = json.loads(p.read_text())
    o.update(modifs)
    ecrire_sondes(monde["depot"], v2=o)


def test_astra_avec_sonde_reussie_part(monde, monkeypatch):
    _astra(monde, monkeypatch)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-astra" in dep["especes_actives"] and dep["sonde_astra"]["cout_usd"] <= 0.05


def test_astra_sonde_absente_refusee(monde, monkeypatch):
    _astra(monde, monkeypatch)
    (monde["depot"] / L.SONDE_ASTRA).unlink()
    assert lancer(monde["r"]) == 2


def test_astra_sonde_trop_chere_refusee(monde, monkeypatch):
    _astra(monde, monkeypatch)
    _sonde(monde, cout_usd=0.06)
    assert lancer(monde["r"]) == 2


def test_astra_sonde_par_le_relais_de_la_course_refusee(monde, monkeypatch):
    _astra(monde, monkeypatch)
    _sonde(monde, relais_pid=PID_ASTRA)
    assert lancer(monde["r"]) == 2


def test_astra_sonde_d_hier_refusee(monde, monkeypatch):
    _astra(monde, monkeypatch)
    _sonde(monde, horodatage_utc="2026-11-17T23:00:00Z")
    assert lancer(monde["r"]) == 2


def test_astra_relais_de_la_course_non_neuf_refuse(monde, monkeypatch):
    _astra(monde, monkeypatch)
    monde["etats"]["8790"]["appels"] = 1
    assert lancer(monde["r"]) == 2


def test_astra_absente_avec_motif_part_sans_elle(monde):
    d = declaration(monde["depot"])
    d["absences"] = {"astra": {"motif": "sonde échouée", "mot_de_la_mere": "R-9999"}}
    _decl(monde, d)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-astra" not in dep["especes_actives"] and dep["sonde_astra"]["motif"]["motif"] == "sonde échouée"


def test_sonde_astra_script(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("sonde_v2", RACINE / "scripts" / "sonde_astra_affinage_v2.py")
    S = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(S)
    for cout, servi, attendu in ((0.004, "gpt-6-astra", True), (0.06, "gpt-6-astra", False), (0.004, "autre-modele", False)):
        c = tmp_path / f"cmd-{cout}-{servi}.py"
        c.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps({'texte': 'prêt', 'cout_usd': " + repr(cout)
                     + ", 'modele_servi': " + repr(servi) + "}))\n", encoding="utf-8")
        monkeypatch.setattr(S, "EMPREINTE_COMMANDE", hashlib.sha256(c.read_bytes()).hexdigest())
        res = S.sonder(c, "http://127.0.0.1:18790", 777, horodatage=lambda: "2026-11-18T07:00:00Z")
        assert res["ok"] is attendu and res["relais_pid"] == 777
    monkeypatch.setattr(S, "EMPREINTE_COMMANDE", "0" * 64)
    with pytest.raises(ValueError):
        S.sonder(c, "http://127.0.0.1:18790", 777)


def test_garde_credit_v5_soupcon_puis_arret(tmp_path):
    g = RACINE / "scripts" / "garde_credit_relais_v5.py"
    cmd = tmp_path / "quota.py"
    cmd.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps({'texte': '', 'cout_usd': 0.01, 'erreur': "
                   "'You exceeded your current quota, please check your plan and billing details'}))\nsys.exit(3)\n", encoding="utf-8")
    arrets = tmp_path / "arrets"
    for k in (1, 2):
        subprocess.run([sys.executable, "-I", "-B", str(g), str(arrets), "astra", "--", sys.executable, "-I", "-B", str(cmd)],
                       input=b"x", capture_output=True)
        assert bool(list(arrets.glob("arret-credit-*.json"))) is (k == 2)
    assert list(arrets.glob("soupcon-credit-*.json"))


def test_premier_soupcon_n_arrete_pas_la_course(monde, monkeypatch):
    _astra_dispensee(monde, {"texte": "", "cout_usd": 0.01,
                             "erreur": "You exceeded your current quota, please check your plan and billing details"}, monkeypatch)
    assert lancer(monde["r"]) == 0
    fin = json.loads((un_run(monde["r"]) / "manifeste-lanceur-fin.json").read_text())
    assert fin["arret_au_premier_refus_pour_credit"] == []


def test_confidentialite_expurger_et_verifier():
    for t in ("écrire à quelqu'un@exemple.org", "voir session_01ABCDEFGH", "selon Lazar", "clé RR_ANTHROPIC_API_KEY_MINUIT",
              "question de Kirchner", "id 0123abcd-0123-4567-89ab-0123456789ab"):
        e, faites = L.expurger(t)
        assert faites and "[retiré]" in e, t
        with pytest.raises(L.Refus):
            L.verifier_confidentialite({"essai": t})
        L.verifier_confidentialite({"essai": e})
    assert L.expurger("effet de Berkson ; Petri ; Gu et Krenn")[1] == []  # noms d'auteurs publiés gardés


def test_confidentialite_fil_expurge_au_manifeste(monde):
    p = monde["depot"] / L.PIECES["liste_fils"][0]
    liste = json.loads(p.read_text())
    liste["fils"][0]["idees_servies"][0]["texte_servi"] += " (idée relayée par Lazar)"
    p.write_text(json.dumps(liste, ensure_ascii=False), encoding="utf-8")
    monde["r"].pieces = dict(monde["r"].pieces, liste_fils=(L.PIECES["liste_fils"][0], L.sha256_fichier(p)))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["confidentialite"]["expurgations"][0]["motif"] == "nom de personne interne"
    conf = (un_run(monde["r"]) / "configuration-orchestrateur.json").read_text()
    assert "Lazar" not in conf


def test_consigne_servie_confidentielle_refusee(monde):
    p = monde["depot"] / L.PIECES["consigne_juge"][0]
    p.write_text(p.read_text() + "\nContact : quelqu'un@exemple.org\n", encoding="utf-8")
    monde["r"].pieces = dict(monde["r"].pieces, consigne_juge=(L.PIECES["consigne_juge"][0], L.sha256_fichier(p)))
    assert lancer(monde["r"]) == 2


def test_registre_doit_etre_celui_de_main(tmp_path):
    g = tmp_path / "depot"
    (g / "registres").mkdir(parents=True)
    (g / "registres" / "go.md").write_text(ligne_go(), encoding="utf-8")
    git(g, "init", "-q", "-b", "main")
    git(g, "-c", "user.email=t@example.invalid", "-c", "user.name=t", "add", "-A")
    git(g, "-c", "user.email=t@example.invalid", "-c", "user.name=t", "commit", "-q", "-m", "x")
    r = L.Reglages.production()
    r.depot, r.registre_go, r.ref_registre = g, g / "registres" / "go.md", "HEAD"
    assert len(L.verifier_registre_main(r)) == 40
    (g / "registres" / "go.md").write_text(ligne_go() + "| GO-2026-11-19-01 | x |\n", encoding="utf-8")
    with pytest.raises(L.Refus):
        L.verifier_registre_main(r)


def test_registre_derive_cite_son_commit(tmp_path):
    reg = tmp_path / "go.md"
    reg.write_text(ligne_go(), encoding="utf-8")
    d = L.ecrire_registre_derive(reg, tmp_path / "derive.md", commit="a" * 40)
    assert d["commit_source"] == "a" * 40 and ("a" * 40) in Path(d["derive"]).read_text()


def test_extraction_de_main_verifiee(tmp_path):
    p = subprocess.run(["git", "-C", str(RACINE), "rev-parse", "--verify", "-q", "origin/main"], capture_output=True)
    if p.returncode != 0:
        pytest.skip("origin/main non récupérée")
    chemin, sha = L.CHEMINS_MAIN_COMMANDES["carbon"], L.COMMANDES_EPINGLEES["carbon"]["commande_gemini_lot_v1.py"]
    assert L.sha256_fichier(L.extraire_de_main(RACINE, chemin, sha, tmp_path / "c.py")) == sha
    with pytest.raises(L.Refus):
        L.extraire_de_main(RACINE, chemin, "0" * 64, tmp_path / "d.py")


# --- v6 : contre-lecture de la v5 portée ---------------------------------------------------------------------------------------


def test_identifiant_unique_et_relances_successives(monde):
    """1 : trois refus de porte à blanc puis une relance acceptée, à la suite (même seconde possible)."""
    port = CONTEXTE["url_claude"].rsplit(":", 1)[1]
    monde["etats"][port] = dict(monde["etat_claude"])
    monde["etat_claude"]["plafond_usd"] = 200.0
    for _ in range(3):
        assert lancer(monde["r"]) == 2
    runs = monde["r"].dossier_runs
    assert not (runs.is_dir() and [p for p in runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)])
    prepas = sorted(p.name for p in monde["r"].dossier_sorties.iterdir())
    assert len(prepas) == 3 and len(set(prepas)) == 3 and all(n.endswith("-preparation") for n in prepas)
    monde["etat_claude"]["plafond_usd"] = 150.0
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    for f in ("acte-de-gel.md", "configuration-orchestrateur.json", "registre-go-derive.md"):
        assert (run / f).is_file() and L.scelle(run / f), f
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    assert dep["preparation"].endswith(run.name + "-preparation")


def test_identifiant_a_la_microseconde():
    a = L._dt.datetime(2026, 11, 18, 7, 0, 0, 1).strftime("%Y%m%d-%H%M%S-%f")
    b = L._dt.datetime(2026, 11, 18, 7, 0, 0, 2).strftime("%Y%m%d-%H%M%S-%f")
    assert a != b and a.endswith("-000001")


def test_variable_minuit_faite_d_espaces_refusee(monde):
    for v in (" ", "   \t", "\n"):
        monde["r"].environnement[L.CLE_CLAUDE] = v
        assert lancer(monde["r"]) == 2, repr(v)
    monde["r"].environnement[L.CLE_CLAUDE] = "valeur-secrete-essai-1"
    assert lancer(monde["r"]) == 0


def test_kimi_sans_mot_de_la_mere_refuse(monde):
    for mot in (None, {"reference": "oui"}, "R-3300", {"reference": ""}):
        _decl(monde, declaration(monde["depot"], mot_kimi=mot, kimi=kimi(monde)))
        _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 500.0, "reste_usd": 400.0, "source": "essai"}))
        assert lancer(monde["r"]) == 2, mot
    _decl(monde, declaration(monde["depot"], mot_kimi={"reference": "R-3300"}, kimi=kimi(monde)))
    assert lancer(monde["r"]) == 2  # v7, mineur 9 : R-3300 n'est pas dans la liste des références admises (R-9001)
    monde["r"].references_kimi_admises = ("R-3300",)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["kimi_autorise_par_la_mere"] == {"reference": "R-3300"} and "prop-kimi" in dep["especes_actives"]


def test_sans_kimi_par_defaut(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-kimi" not in dep["especes_actives"] and dep["kimi_autorise_par_la_mere"] is None


def _carbon_cle_partagee(monde, monkeypatch, reste, credit=800.0):
    sc = script_commande(monde["tmp"], "commande_gemini_lot_v1", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "carbon", sc)
    c = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(sc)] + L.ARGUMENTS_COMMANDES["carbon"],
         "modele_propose": "gemini-4-carbon", "nom_cle": "CLE_ESSAI_A", "inscription": "R-3217", "pid_relais": PID_CARBON,
         "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], carbon=c))
    args = monde["cmdlines"][PID_CARBON]
    args[args.index("--variable-cle") + 1] = "CLE_ESSAI_A"
    _releve(monde, releve(CLE_ESSAI_A={"credit_usd": credit, "reste_usd": reste, "source": "essai"}))


def test_cle_partagee_argon_carbon_somme_des_parts_sain(monde, monkeypatch):
    """7 : Argon et Carbon sur la même clé : part au pire 150 + 48 = 198 (v9) ; reste 210 (cinquième 160) → départ."""
    _carbon_cle_partagee(monde, monkeypatch, reste=210.0)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    c = dep["releve_credits_avant"]["cles"]["CLE_ESSAI_A"]
    assert c["part_au_pire_usd"] == 198.0 and c["parts_par_relais"] == {"argon": 150.0, "carbon": 48.0}
    assert sorted(c["relais"]) == ["argon", "carbon"]


def test_cle_partagee_argon_carbon_reste_sous_la_somme_alerte(monde, monkeypatch):
    """7, artefact : reste 170 ≥ chaque part prise seule (150, 48) mais < la somme 198 → alerte, code 3."""
    _carbon_cle_partagee(monde, monkeypatch, reste=170.0)
    assert lancer(monde["r"]) == 3
    runs = monde["r"].dossier_runs
    assert not [p for p in runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)]


def test_verifier_credits_cle_partagee_unitaire(tmp_path):
    parts = {"argon": {"part_au_pire_usd": 150.0}, "carbon": {"part_au_pire_usd": 24.0}}
    cles = {"argon": "CLE_G", "carbon": "CLE_G"}
    rel = {"releve_utc": "2026-11-18T07:00:00Z", "cles": {"CLE_G": {"credit_usd": 800.0, "reste_usd": 174.5, "source": "essai"}}}
    s = L.verifier_credits(rel, cles, AUJOURD_HUI, tmp_path / "a", parts)
    assert s["CLE_G"]["part_au_pire_usd"] == 174.0 and s["CLE_G"]["fournisseur"] == "argon+carbon"
    rel["cles"]["CLE_G"]["reste_usd"] = 174.0  # égalité : le pire cas laisse zéro → alerte
    with pytest.raises(L.AlerteCredit):
        L.verifier_credits(rel, cles, AUJOURD_HUI, tmp_path / "b", parts)
    rel["cles"]["CLE_G"] = {"non_lisible": True}
    rel["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_G"]}
    s = L.verifier_credits(rel, cles, AUJOURD_HUI, tmp_path / "c", parts)
    assert s["CLE_G"]["lisible"] is False and s["CLE_G"]["part_au_pire_usd"] == 174.0
    cles_k = {"argon": "CLE_G", "kimi": "CLE_G"}  # une clé partagée avec Kimi : non dispensable
    with pytest.raises(L.Refus):
        L.verifier_credits(rel, cles_k, AUJOURD_HUI, tmp_path / "d", dict(parts, kimi={"part_au_pire_usd": 5.0}))


def _garde_v6():
    spec = importlib.util.spec_from_file_location("garde_v6", RACINE / "scripts" / "garde_credit_relais_v6.py")
    G = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(G)
    return G


def test_garde_credit_v6_choix_de_la_limite_de_debit():
    G = _garde_v6()
    assert G.VERSION == "garde_credit_relais_v6"
    j = lambda e: json.dumps({"texte": "", "cout_usd": 0.01, "erreur": e})  # noqa: E731
    debit = j("You exceeded your current quota: rate limit per minute")
    assert G.soupcon_credit(debit, "", 1)  # (a) par défaut : soupçon (lettre de la v5)
    assert G.soupcon_credit(debit, "", 1, True)
    assert G.soupcon_credit(debit, "", 1, False) is None  # (b) : ignoré
    seul = j("You exceeded your current quota, please check your plan")
    assert G.soupcon_credit(seul, "", 1, False) and G.soupcon_credit(seul, "", 1, True)  # sans limite de débit : soupçon
    mixte = j("You exceeded your current quota (rate limit per minute); check your billing details")
    assert not G.motif_credit(mixte, "", 1)  # le message de quota d'OpenAI reste ambigu (lettre de la v5)
    assert G.soupcon_credit(mixte, "", 1, False) and G.soupcon_credit(mixte, "", 1, True)  # mot de facturation : soupçon même en (b)
    # le reste de la v5 inchangé
    for e in ("HTTP 402 payment required", "credit balance is too low"):
        assert G.motif_credit(j(e), "", 1), e
    assert not G.motif_credit(j("429 RESOURCE_EXHAUSTED: rate limit per minute"), "", 1)


def test_garde_credit_v6_option_en_ligne_de_commande(tmp_path):
    g = RACINE / "scripts" / "garde_credit_relais_v6.py"
    cmd = tmp_path / "debit.py"
    cmd.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps({'texte': '', 'cout_usd': 0.01, 'erreur': "
                   "'You exceeded your current quota: rate limit per minute'}))\nsys.exit(3)\n", encoding="utf-8")
    for option, arret_attendu in (([], True), (["--limite-de-debit-pas-soupcon"], False)):
        arrets = tmp_path / f"arrets-{len(option)}"
        for _ in range(2):
            p = subprocess.run([sys.executable, "-I", "-B", str(g), str(arrets), "astra"] + option + ["--", sys.executable, "-I", "-B",
                                str(cmd)], input=b"x", capture_output=True)
            assert json.loads(p.stdout.decode().strip().splitlines()[-1])["cout_usd"] == 0.01
        assert bool(list(arrets.glob("arret-credit-*.json"))) is arret_attendu, option
    p = subprocess.run([sys.executable, "-I", "-B", str(g), str(tmp_path / "x"), "astra", "--autre", "--", "true"], capture_output=True)
    assert p.returncode == 2


def test_lanceur_pose_l_option_selon_la_declaration(tmp_path):
    for valeur, attendu in ((None, False), (True, False), (False, True)):
        decl = {"fournisseurs": {"argon": {"commande": ["bash", "x.sh"]}, "claude": {"url_relais": "u"}}}
        if valeur is not None:
            decl["compter_limite_de_debit_comme_soupcon"] = valeur
        d = L.envelopper_commandes(decl, "py", tmp_path / "garde.py", tmp_path / "arrets")
        c = d["fournisseurs"]["argon"]["commande"]
        assert ("--limite-de-debit-pas-soupcon" in c) is attendu
        assert c[c.index("--") + 1:] == ["bash", "x.sh"] and "commande" not in d["fournisseurs"]["claude"]
    assert L.verifier_choix_limite({}) is True
    assert L.verifier_choix_limite({"compter_limite_de_debit_comme_soupcon": False}) is False
    for mauvais in ("faux", 0, None):
        with pytest.raises(L.Refus):
            L.verifier_choix_limite({"compter_limite_de_debit_comme_soupcon": mauvais})


def test_choix_de_la_limite_au_manifeste_et_dans_la_commande(monde, monkeypatch):
    _astra_dispensee(monde, {"texte": "", "cout_usd": 0.01, "erreur": "You exceeded your current quota: rate limit per minute"},
                     monkeypatch)
    d = json.loads(monde["r"].declaration.read_text())
    d["compter_limite_de_debit_comme_soupcon"] = False
    _decl(monde, d)
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    assert dep["compter_limite_de_debit_comme_soupcon"] is False
    conf = json.loads((run / "configuration-orchestrateur.json").read_text())
    assert "--limite-de-debit-pas-soupcon" in conf["fournisseurs"]["astra"]["commande"]
    assert not list(Path(dep["dossier_arrets_credit"]).glob("soupcon-credit-*.json"))


def _de_main(chemin: str, attendu: str, destination: Path):
    p = subprocess.run(["git", "-C", str(RACINE), "rev-parse", "--verify", "-q", "origin/main"], capture_output=True)
    if p.returncode != 0:
        pytest.skip("origin/main non récupérée")
    L.extraire_de_main(RACINE, chemin, attendu, destination)
    spec = importlib.util.spec_from_file_location(destination.stem + "_essai", destination)
    m = importlib.util.module_from_spec(spec)
    ancien = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(m)
    finally:
        sys.dont_write_bytecode = ancien
    return m


def test_reserve_du_relais_epingle_pour_la_sonde_sain_et_artefact(tmp_path):
    """2 : relais compatible OpenAI épinglé (67f36951…) et commande d'Astra épinglée, appel direct du compteur du relais.
    Sain : `--reserve-par-appel 0.01`, plafond 0,05, un appel → la requête de la sonde v2 est admise. Artefact : la réserve par
    défaut (0,40) → 402, l'échec de la v5."""
    relais = _de_main("docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py", L.PROGRAMMES_RELAIS["astra"][1],
                      tmp_path / "relais_kimi_v4.py")
    cmd = _de_main(L.CHEMINS_MAIN_COMMANDES["astra"], L.COMMANDES_EPINGLEES["astra"]["commande_astra_v1.py"],
                   tmp_path / "commande_astra_v1.py")
    spec = importlib.util.spec_from_file_location("sonde_v2_r", RACINE / "scripts" / "sonde_astra_affinage_v2.py")
    S = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(S)
    assert relais.RESERVE_PAR_APPEL_DEFAUT == 0.40 and relais.MARGE_JETONS_ENTREE == 1024
    # même point fixe que la commande épinglée, avec les réglages de la sonde v2
    n = None
    for _ in range(3):
        corps = json.dumps({"model": S.MODELE, "messages": [{"role": "user", "content": S.CONSIGNE}],
                            "max_completion_tokens": n or 4096}, ensure_ascii=False).encode("utf-8")
        n2 = cmd.max_tokens_permis(len(corps), S.PLAFOND_USD, 10, 50, 4096, 16)
        assert n2 is not None
        if n2 == n:
            break
        n = n2
    corps = json.dumps({"model": S.MODELE, "messages": [{"role": "user", "content": S.CONSIGNE}], "max_completion_tokens": n},
                       ensure_ascii=False).encode("utf-8")
    assert 512 < n < 1000  # la sortie n'est plus bornée à 512 (troncature) ; le plafond la borne
    bareme = relais.Bareme(10, 50, 1, 4096)
    pire = bareme.pire_cas(len(corps), json.loads(corps))
    assert pire <= S.PLAFOND_USD + 1e-12  # pire cas sous 0,05 USD
    sain = relais.Compteur(0.05, 0.01, 1, 10 ** 6)
    assert sain.admettre(max(sain.reserve_min, pire)) is None
    defaut = relais.Compteur(0.05, relais.RESERVE_PAR_APPEL_DEFAUT, 1, 10 ** 6)
    assert defaut.admettre(max(defaut.reserve_min, pire))[0] == 402
    # avec l'ancienne sortie bornée à 512 : admise aussi, mais tronquée au-delà de 512 jetons
    assert cmd.max_tokens_permis(len(corps), S.PLAFOND_USD, 10, 50, 512, 16) == 512


def test_sonde_v2_lance_sortie_4096(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("sonde_v2_b", RACINE / "scripts" / "sonde_astra_affinage_v2.py")
    S = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(S)
    assert S.VERSION == "sonde_astra_affinage_v2" and S.PLAFOND_USD == 0.05
    c = tmp_path / "cmd.py"
    c.write_text("import json,sys\nsys.stdin.read()\njson.dump(sys.argv[1:], open(" + repr(str(tmp_path / "argv.json"))
                 + ", 'w'))\nprint(json.dumps({'texte': 'prêt', 'cout_usd': 0.004, 'modele_servi': 'gpt-6-astra'}))\n", encoding="utf-8")
    monkeypatch.setattr(S, "EMPREINTE_COMMANDE", hashlib.sha256(c.read_bytes()).hexdigest())
    res = S.sonder(c, "http://127.0.0.1:18790", 777, horodatage=lambda: "2026-11-18T07:00:00Z")
    argv = json.loads((tmp_path / "argv.json").read_text())
    assert res["ok"] is True and argv[argv.index("--max-sortie-jetons") + 1] == "4096"


def test_sonde_v1_refusee_par_le_lanceur_v7(monde, monkeypatch):
    _astra(monde, monkeypatch)
    _sonde(monde, version="sonde_astra_affinage_v1")
    assert lancer(monde["r"]) == 2


def test_acte_de_gel_porte_le_nom_du_lanceur(monde):
    assert lancer(monde["r"]) == 0
    acte = (un_run(monde["r"]) / "acte-de-gel.md").read_text()
    assert acte.startswith("# Acte de gel — course d'affinage des idées des mentors, lanceur " + L.VERSION)


def test_course_v7_deja_lancee_refusee(monde):
    assert lancer(monde["r"]) == 0
    assert lancer(monde["r"]) == 2
    assert "course-affinage-mentors-v9" in L.SUFFIXE_RUN


# =================================================================================================================================
# v7 — essais neufs : un cas sain et un artefact (R5) par garde neuve ; une mutation par majeur ; essais v6b portés.
# =================================================================================================================================

PARTS_ASTRA = {"astra": {"part_au_pire_usd": 48.0}}  # v9
B_ASTRA = {"pid_relais": PID_ASTRA, "nom_cle": "CLE_ESSAI_S"}
B_CARBON = {"pid_relais": PID_CARBON, "nom_cle": "CLE_ESSAI_G"}
B_ARGON = {"pid_relais": PID_ARGON, "nom_cle": "CLE_ESSAI_A"}


def _args_astra(m, **valeurs) -> list:
    """Ligne de commande du relais d'Astra du monde d'essai, avec des options remplacées (None : option retirée)."""
    a = list(m["cmdlines"][PID_ASTRA])
    for opt, v in valeurs.items():
        o = "--" + opt.replace("_", "-")
        if o in a:
            k = a.index(o)
            del a[k:k + 2]
        if v is not None:
            a += [o, str(v)]
    return a


def _relais_comme_la_sonde(m) -> None:
    """Artefact du constat 1 : le relais d'Astra de la course lancé avec les réglages du relais jeté de la sonde (0,05 USD, un
    appel, réserve 0,01) ; l'état rendu est cohérent avec ces arguments (un vrai relais ainsi lancé le rendrait)."""
    m["cmdlines"][PID_ASTRA] = _args_astra(m, plafond_usd="0.05", reserve_par_appel="0.01", max_appels="1")
    m["etats"]["8790"].update(plafond_usd=0.05, max_appels=1, reserve_par_appel_usd=0.01)


def essai_relais_jete_refuse(module, m) -> None:
    """L'essai du majeur 1 : un relais d'Astra réglé comme le relais jeté de la sonde est refusé avant le départ."""
    _relais_comme_la_sonde(m)
    with pytest.raises(module.Refus, match="astra"):
        module.controler_relais_vivant(m["r"], "astra", dict(B_ASTRA), FIXE, 5, PARTS_ASTRA)


def test_v7_astra_bornes_basses_sain(monde):
    out = L.controler_relais_vivant(monde["r"], "astra", dict(B_ASTRA), FIXE, 5, PARTS_ASTRA)
    assert out["max_appels"] == 20 and out["plafond_usd"] == 48.0 and out["part_au_pire_usd"] == 48.0 and out["etat_neuf"]


def test_v7_astra_regle_comme_la_sonde_refuse(monde):
    essai_relais_jete_refuse(L, monde)


@pytest.mark.parametrize("valeurs, etat, motif", [
    ({"max_appels": "16"}, {"max_appels": 16}, "max-appels 16 < 20"),                  # marge nulle de la v6
    ({"max_appels": None}, {}, "--max-appels absent"),                                 # aucun défaut supposé
    ({"plafond_usd": "47.99"}, {"plafond_usd": 47.99}, "part au pire"),                # sous la part : 402 en fin d'étape
    ({"plafond_usd": "60"}, {"plafond_usd": 60.0}, "part au pire"),                    # au-dessus : barrière plus large
    ({"plafond_usd": "24"}, {"plafond_usd": 24.0}, "part au pire"),                    # v9 : le relais des commandes v8
    ({}, {"max_appels": 64}, "max_appels"),                                            # état différent des arguments
    ({}, {"plafond_usd": 150.0}, "plafond_usd"),
    ({}, {"reserve_par_appel_usd": 3.5}, "réserve"),           # v9 : plafond de session 3,00
    ({}, {"prix_entree_usd_par_million": 1.0}, "prix"),
    ({}, {"variable_cle_encore_presente": True}, "variable de clé"),
])
def test_v7_astra_bornes_basses_artefacts(monde, valeurs, etat, motif):
    monde["cmdlines"][PID_ASTRA] = _args_astra(monde, **valeurs)
    monde["etats"]["8790"].update(etat)
    with pytest.raises(L.Refus, match=motif):
        L.controler_relais_vivant(monde["r"], "astra", dict(B_ASTRA), FIXE, 5, PARTS_ASTRA)


def test_v7_astra_part_au_pire_inconnue_refusee(monde):
    with pytest.raises(L.Refus, match="part au pire inconnue"):
        L.controler_relais_vivant(monde["r"], "astra", dict(B_ASTRA), FIXE, 5, None)


def test_v7_astra_relais_comme_la_sonde_bout_en_bout(monde, monkeypatch, capsys):
    _astra(monde, monkeypatch)
    assert lancer(monde["r"]) == 0                                 # sain : relais 48 USD (v9), 20 appels
    _relais_comme_la_sonde(monde)
    monde["r"].dossier_runs = monde["tmp"] / "runs-bis"
    assert lancer(monde["r"]) == 2                                 # artefact : refus avant le départ, tentative gardée
    assert "astra" in capsys.readouterr().err
    assert not (monde["tmp"] / "runs-bis").exists() or not list((monde["tmp"] / "runs-bis").iterdir())


def test_v7_carbon_bornes_basses_sain_et_artefacts(monde):
    out = L.controler_relais_vivant(monde["r"], "carbon", dict(B_CARBON), FIXE, 5, None)
    assert out["max_lots"] == 20 and out["max_appels"] == 40
    base = list(monde["cmdlines"][PID_CARBON])
    for args, etat, motif in ((["--max-lots", "16"], {"max_lots": 16}, "max-lots 16 < 20"),   # la v6 acceptait 16
                              (["--max-appels", "32"], {"max_appels": 32}, "max-appels 32 < 40"),
                              (["--max-lots", None], {}, "--max-lots absent"),
                              ([], {"max_lots": 8}, "max_lots"),
                              ([], {"lots_crees": 1}, "déjà employé"),
                              ([], {"lots_crees": None}, "sans")):
        a = list(base)
        if args:
            k = a.index(args[0])
            if args[1] is None:
                del a[k:k + 2]
            else:
                a[k + 1] = args[1]
        monde["cmdlines"][PID_CARBON] = a
        sauve = dict(monde["etats"]["8792"])
        for cle, v in etat.items():
            if v is None:
                monde["etats"]["8792"].pop(cle)
            else:
                monde["etats"]["8792"][cle] = v
        with pytest.raises(L.Refus, match=motif):
            L.controler_relais_vivant(monde["r"], "carbon", dict(B_CARBON), FIXE, 5, None)
        monde["etats"]["8792"].clear()
        monde["etats"]["8792"].update(sauve)


def test_v7_argon_max_appels_absent_ou_different_refuse(monde):
    assert L.controler_relais_vivant(monde["r"], "argon", dict(B_ARGON), FIXE, 5, None)["max_appels"] == 450
    a = list(monde["cmdlines"][PID_ARGON])
    k = a.index("--max-appels")
    monde["cmdlines"][PID_ARGON] = a[:k] + a[k + 2:]               # la v6 supposait le défaut du relais (64)
    with pytest.raises(L.Refus, match="--max-appels absent"):
        L.controler_relais_vivant(monde["r"], "argon", dict(B_ARGON), FIXE, 5, None)
    monde["cmdlines"][PID_ARGON] = a
    monde["etats"]["8788"]["max_appels"] = 64
    with pytest.raises(L.Refus, match="max_appels"):
        L.controler_relais_vivant(monde["r"], "argon", dict(B_ARGON), FIXE, 5, None)


def test_v7_kimi_bornes_basses(monde):
    b = dict(kimi(monde), pid_relais=PID_KIMI, nom_cle="CLE_ESSAI_K")
    port = CONTEXTE["url_kimi"].rsplit(":", 1)[1]
    assert L.controler_relais_vivant(monde["r"], "kimi", b, FIXE, 6, {"kimi": {"part_au_pire_usd": 16.0}})["max_appels"] == 20
    with pytest.raises(L.Refus, match="part au pire"):
        L.controler_relais_vivant(monde["r"], "kimi", b, FIXE, 6, {"kimi": {"part_au_pire_usd": 31.0}})
    a = list(monde["cmdlines"][PID_KIMI])
    a[a.index("--max-appels") + 1] = "16"
    monde["cmdlines"][PID_KIMI] = a
    monde["etats"][port]["max_appels"] = 16
    with pytest.raises(L.Refus, match="max-appels 16 < 20"):
        L.controler_relais_vivant(monde["r"], "kimi", b, FIXE, 6, {"kimi": {"part_au_pire_usd": 16.0}})


# --- v7, mineur 3 : un état vide ou incomplet ne passe plus pour « neuf » -------------------------------------------------------


@pytest.mark.parametrize("nom, b, parts", [
    ("claude", {"pid_relais": PID_CLAUDE, "nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT"}, None),
    ("astra", B_ASTRA, PARTS_ASTRA), ("carbon", B_CARBON, None), ("argon", B_ARGON, None)])
def test_v7_etat_vide_refuse(monde, nom, b, parts):
    b = dict(b, url_relais=CONTEXTE["url_claude"]) if nom == "claude" else dict(b)
    assert L.controler_relais_vivant(monde["r"], nom, b, FIXE, 5, parts)["etat_neuf"] is True       # sain
    lire = monde["r"].lire_etat_relais
    for faux in ({}, {"autre": 1}, []):
        monde["r"].lire_etat_relais = lambda url, f=faux: f
        with pytest.raises(L.Refus):
            L.controler_relais_vivant(monde["r"], nom, b, FIXE, 5, parts)
    monde["r"].lire_etat_relais = lire


def test_v7_etat_sans_depense_ou_engage_refuse(monde):
    b = {"pid_relais": PID_CLAUDE, "nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT", "url_relais": CONTEXTE["url_claude"]}
    for champ in ("depense_usd", "engage_usd", "appels"):
        sauve = monde["etat_claude"].pop(champ)
        with pytest.raises(L.Refus, match=champ):
            L.controler_relais_vivant(monde["r"], "claude", b, FIXE, 5, None)
        monde["etat_claude"][champ] = sauve
    monde["etat_claude"]["appels"] = "0"                                                          # mauvais type
    with pytest.raises(L.Refus, match="déjà employé"):
        L.controler_relais_vivant(monde["r"], "claude", b, FIXE, 5, None)
    monde["etat_claude"]["appels"] = 0
    monde["etat_claude"]["engage_usd"] = 0.4                                                      # appel en vol
    with pytest.raises(L.Refus, match="déjà employé"):
        L.controler_relais_vivant(monde["r"], "claude", b, FIXE, 5, None)


def test_v7_etat_vide_bout_en_bout(monde, capsys):
    monde["etat_claude"].clear()
    assert lancer(monde["r"]) == 2
    assert "état non reconnu" in capsys.readouterr().err


# --- v7, majeur 2 : l'autre course de l'organisme (auto-conception) -------------------------------------------------------------


def _course_auto_conception(m, nom="20261118-120000-course-auto-conception-v2", fin_utc: str | None = "2026-11-18T06:00:00"):
    d = m["r"].dossier_runs / nom
    d.mkdir(parents=True)
    (d / "manifeste-lanceur-depart.json").write_text("{}", encoding="utf-8")
    if fin_utc is not None:
        f = d / "manifeste-lanceur-fin.json"
        f.write_text("{}", encoding="utf-8")
        t = dt.datetime.fromisoformat(fin_utc + "+00:00").timestamp()
        os.utime(f, (t, t))
    return d


def essai_auto_conception_en_cours_refusee(principal, m) -> None:
    """L'essai du majeur 2 : une course d'auto-conception partie sans manifeste de fin interdit le départ."""
    _course_auto_conception(m, fin_utc=None)
    assert principal([], reglages=m["r"]) == 2


def test_v7_sans_autre_course_sain(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["autres_courses_de_l_organisme"]["autres_courses"] == []


def test_v7_auto_conception_en_cours_refusee(monde, capsys):
    essai_auto_conception_en_cours_refusee(L.principal, monde)
    assert "jamais en" in capsys.readouterr().err
    assert not [p for p in monde["r"].dossier_runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)]


def test_v7_auto_conception_finie_avant_le_releve_part(monde):
    _course_auto_conception(monde, fin_utc="2026-11-18T06:00:00")             # relevé du monde : 07:00Z
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["autres_courses_de_l_organisme"]["autres_courses"][0]["run"].endswith("-course-auto-conception-v2")


def test_v7_releve_anterieur_a_la_fin_de_l_autre_course_refuse(monde, capsys):
    _course_auto_conception(monde, fin_utc="2026-11-18T08:00:00")
    assert lancer(monde["r"]) == 2
    assert "relevé à refaire" in capsys.readouterr().err
    objet = releve()
    objet["releve_utc"] = "2026-11-18T08:30:00Z"                              # relevé refait après la fin
    _releve(monde, objet)
    assert lancer(monde["r"]) == 0


def test_v7_releve_heure_illisible_refuse(monde):
    for quand in ("2026-11-18", "2026-11-18 (matin)", "2026-11-18T25:00:00Z"):
        objet = releve()
        objet["releve_utc"] = quand
        _releve(monde, objet)
        assert lancer(monde["r"]) == 2, quand
    objet["releve_utc"] = "2026-11-18T07:00:00Z"
    _releve(monde, objet)
    assert lancer(monde["r"]) == 0


def test_v7_affinage_anterieur_ne_compte_pas_comme_autre_course(monde):
    d = monde["r"].dossier_runs / "20261118-050000-alerte-credits-affinage-mentors-v7"   # dossier d'alerte : pas une course
    d.mkdir(parents=True)
    assert lancer(monde["r"]) == 0


# --- v7, sonde d'Astra liée à la sonde commune du jour -----------------------------------------------------------------------------


def _decl_astra_min(m, s: Path) -> dict:
    return {"fournisseurs": {"astra": {"commande": [sys.executable, "-I", "-B", str(s)]}}, "metas": {"astra": {"pid_relais": PID_ASTRA}}}


def test_v7_sonde_commune_saine_et_artefacts(monde, monkeypatch):
    s = _astra(monde, monkeypatch)
    sha_cmd = hashlib.sha256(s.read_bytes()).hexdigest()
    decl = _decl_astra_min(monde, s)
    r, depot = monde["r"], monde["depot"]
    out = L.verifier_sonde_astra(r, decl, AUJOURD_HUI)
    assert out["sonde_commune"]["chemin"] == COMMUNE_DU_JOUR and out["sha256"] == L.sha256_fichier(depot / L.SONDE_ASTRA)
    v2_sha = L.sha256_fichier(depot / L.SONDE_ASTRA)
    artefacts = {
        "absente": None,
        "autre empreinte du v2": sonde_commune(L.SONDE_ASTRA, "0" * 64, commande_sha=sha_cmd),
        "autre relais jeté": sonde_commune(L.SONDE_ASTRA, v2_sha, pid=998, commande_sha=sha_cmd),
        "échec de configuration": sonde_commune(L.SONDE_ASTRA, v2_sha, commande_sha=sha_cmd, ok=False, echec_de_configuration=True),
        "d'hier": sonde_commune(L.SONDE_ASTRA, v2_sha, commande_sha=sha_cmd, jour="2026-11-17"),
        "autre commande": sonde_commune(L.SONDE_ASTRA, v2_sha),
        "autre sonde v2": sonde_commune(L.SONDE_ASTRA, v2_sha, commande_sha=sha_cmd, sonde_v2={"sha256": "1" * 64}),
        "v2 hors des chemins lus": sonde_commune("docs/ailleurs/sonde.json", v2_sha, commande_sha=sha_cmd),
        "relais jeté sur un port de course": sonde_commune(L.SONDE_ASTRA, v2_sha, commande_sha=sha_cmd,
                                                           relais_jete=dict(sonde_commune("", "")["relais_jete"], port=8790)),
        "relais jeté à plusieurs appels": sonde_commune(L.SONDE_ASTRA, v2_sha, commande_sha=sha_cmd,
                                                        relais_jete=dict(sonde_commune("", "")["relais_jete"], max_appels=16)),
        "dépense au-dessus de 0,05": sonde_commune(L.SONDE_ASTRA, v2_sha, commande_sha=sha_cmd, depense_relais_usd=0.06),
        "version": sonde_commune(L.SONDE_ASTRA, v2_sha, commande_sha=sha_cmd, version="sonde_astra_courses_v0"),
    }
    commune = depot / COMMUNE_DU_JOUR
    for quoi, objet in artefacts.items():
        commune.unlink()
        Path(str(commune) + ".sha256").unlink()
        if objet is not None:
            ecrire_scelle(commune, objet)
        with pytest.raises(L.Refus, match="sonde"):
            L.verifier_sonde_astra(r, decl, AUJOURD_HUI)
        if objet is None:
            ecrire_scelle(commune, sonde_commune(L.SONDE_ASTRA, v2_sha, commande_sha=sha_cmd))
    ecrire_sondes(depot, v2=sonde_astra(commande_sha256=sha_cmd))
    autre = depot / f"{L.COURSE_V6}/sonde-astra-commune-2026-11-18-v1.json"   # deux rapports communs du jour : ambigu
    ecrire_scelle(autre, json.loads((depot / COMMUNE_DU_JOUR).read_text()))
    with pytest.raises(L.Refus, match="2 rapport"):
        L.verifier_sonde_astra(r, decl, AUJOURD_HUI)


def test_v7_sonde_d_un_autre_jour_sous_course_v7(monde, monkeypatch):
    s = _astra(monde, monkeypatch)
    sha_cmd = hashlib.sha256(s.read_bytes()).hexdigest()
    decl = _decl_astra_min(monde, s)
    jour = dt.date(2026, 11, 19)
    with pytest.raises(L.Refus, match="0 rapport"):                         # la sonde du 18 ne vaut pas le 19
        L.verifier_sonde_astra(monde["r"], decl, jour)
    v2_rel = f"{L.COURSE}/sonde-astra-course-affinage-v9-2026-11-19.json"
    ecrire_sondes(monde["depot"], v2=sonde_astra(commande_sha256=sha_cmd, horodatage_utc="2026-11-19T08:00:00Z"),
                  v2_rel=v2_rel, commune_rel=f"{L.COURSE}/sonde-astra-commune-2026-11-19-v1.json",
                  commune=None)
    c = monde["depot"] / f"{L.COURSE}/sonde-astra-commune-2026-11-19-v1.json"
    objet = json.loads(c.read_text())
    objet.update(jour="2026-11-19", horodatage_utc="2026-11-19T07:59:55Z")
    c.unlink()
    Path(str(c) + ".sha256").unlink()
    ecrire_scelle(c, objet)
    out = L.verifier_sonde_astra(monde["r"], decl, jour)
    assert out["chemin"].endswith("sonde-astra-course-affinage-v9-2026-11-19.json")


def test_v7_rapports_reels_du_18_novembre_acceptes_ce_jour_seulement(monde, tmp_path):
    """Les deux rapports versés le 18 novembre (sonde commune 802b840e…, rapport v2 d2cacbcf…) et la commande d'Astra réelle
    de `main` : le lanceur v7 les accepte le 18 novembre, les refuse le 19."""
    p = subprocess.run(["git", "-C", str(RACINE), "show", "refs/remotes/origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/"
                        "commande_astra_v1.py"], capture_output=True)
    assert p.returncode == 0, "origin/main absente (git fetch ciblé requis)"
    cmd = tmp_path / "commande_astra_v1.py"
    cmd.write_bytes(p.stdout)
    assert L.sha256_fichier(cmd) == SHA_ASTRA
    depot = monde["depot"]
    for rel in (L.SONDE_ASTRA, COMMUNE_DU_JOUR):
        for suffixe in ("", ".sha256"):
            (depot / (rel + suffixe)).unlink(missing_ok=True)
            shutil.copy2(RACINE / (rel + suffixe), depot / (rel + suffixe))
    assert L.sha256_fichier(depot / L.SONDE_ASTRA) == "d2cacbcf1872de9d90cdff440bafa61698b3a19e2ffb7c1646eecc29a5b7872f"
    assert L.sha256_fichier(depot / COMMUNE_DU_JOUR) == "802b840edbf14983ce302b71253242c753e70aa60335868e811fdb6fd45e8f43"
    decl = _decl_astra_min(monde, cmd)
    out = L.verifier_sonde_astra(monde["r"], decl, dt.date(2026, 11, 18))
    assert out["cout_usd"] == 0.00041 and out["sonde_commune"]["relais_jete_pid"] == 5016
    assert "5016" in out["relais_jete_a_arreter"]
    with pytest.raises(L.Refus):
        L.verifier_sonde_astra(monde["r"], decl, dt.date(2026, 11, 19))


def test_v7_sonde_commune_epinglee(monde):
    assert L.PIECES["sonde_commune"] == ("scripts/sonde_astra_courses_v1.py",
                                         "d374d1071f4ef70b3604d97dc62e2f14103c440a166342b330d7a576d8b4c777")
    assert L.sha256_fichier(RACINE / L.PIECES["sonde_commune"][0]) == L.PIECES["sonde_commune"][1]
    assert lancer(monde["r"]) == 0
    p = monde["depot"] / L.PIECES["sonde_commune"][0]
    p.write_text(p.read_text() + "\n# modifiée\n", encoding="utf-8")
    monde["r"].dossier_runs = monde["tmp"] / "runs-bis"
    assert lancer(monde["r"]) == 2


# --- v7, mineur 4 : écart au devis sur les espèces actives -----------------------------------------------------------------------


def test_v7_devis_sur_les_especes_actives():
    v6b = ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]
    assert L.devis_estimation(v6b) == pytest.approx(41.136)                       # devis v8 (cinq espèces ; v6b : 37,576)
    assert L.devis_estimation(v6b + ["prop-kimi"]) == pytest.approx(48.8384)      # six espèces, Carbon au prix v8
    assert L.devis_estimation(v6b) != pytest.approx(L.DEVIS_V5_TOTAL["six_especes"])  # artefact de la v6 : 45,28 pour cinq
    trois = ["prop-opus", "prop-fable", "prop-argon"]
    assert L.devis_estimation(trois) == pytest.approx(16 * (0.141 + 0.3525 + 0.276) + 96 * (0.031 + 0.037 + 0.0347))
    with pytest.raises(L.Refus):
        L.devis_estimation(["prop-inconnue"])


def test_v7_ecart_au_devis_au_manifeste(monde):
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    attendu = L.devis_estimation(dep["especes_actives"])
    assert fin["ecart_au_devis"]["devis_estimation_sans_marge_usd"] == pytest.approx(attendu)
    assert dep["devis_estimation_sans_marge_usd"] == pytest.approx(attendu)
    assert fin["ecart_au_devis"]["base_du_devis"]["nombre"] == 3


# --- v7, mineur 5 : codes de sortie distincts ------------------------------------------------------------------------------------


def test_v7_codes_de_sortie_table():
    assert L.code_de_sortie(False, False, None, 0) == 0
    for code in (1, 2, 3, 4, 5, -15, None):
        assert L.code_de_sortie(False, False, None, code) == 6, code
    assert L.code_de_sortie(False, False, "RuntimeError: x", 0) == 6
    assert L.code_de_sortie(True, True, "x", 3) == 4 and L.code_de_sortie(False, True, None, 2) == 5


@pytest.mark.parametrize("code", [3, 4, 5])
def test_v7_code_de_l_orchestrateur_ne_se_confond_plus(monde, code):
    remplacer_orchestrateur(monde, code=code)
    assert lancer(monde["r"]) == 6                                    # la v6 rendait 3, 4 ou 5 tels quels
    fin = json.loads((un_run(monde["r"]) / "manifeste-lanceur-fin.json").read_text())
    assert fin["code_orchestrateur"] == code and fin["code_du_lanceur"] == 6


# --- v7, mineur 9 : Kimi refusé en production ------------------------------------------------------------------------------------


def test_v7_kimi_refuse_par_le_lanceur_de_production(monde, capsys):
    assert L.REFERENCES_KIMI_ADMISES == () and L.Reglages.production().references_kimi_admises == ()
    monde["r"].references_kimi_admises = L.REFERENCES_KIMI_ADMISES
    _decl(monde, declaration(monde["depot"], kimi=kimi(monde)))               # mot de la mère de la bonne forme (R-9001)
    _releve(monde, releve(CLE_ESSAI_K={"credit_usd": 500.0, "reste_usd": 400.0, "source": "essai"}))
    assert lancer(monde["r"]) == 2
    assert "non admise" in capsys.readouterr().err
    _decl(monde, declaration(monde["depot"]))                                  # sain : Kimi absent
    assert lancer(monde["r"]) == 0


# --- mutations : le code fautif réintroduit fait échouer un essai ---------------------------------------------------------------


def _mutant(nom: str, remplacements: list):
    source = CHEMIN_LANCEUR.read_text(encoding="utf-8")
    for ancien, nouveau in remplacements:
        assert source.count(ancien) == 1, ancien
        source = source.replace(ancien, nouveau)
    module = type(sys)(nom)
    module.__file__ = str(CHEMIN_LANCEUR)
    sys.modules[nom] = module
    try:
        exec(compile(source, str(CHEMIN_LANCEUR), "exec"), module.__dict__)
    finally:
        sys.modules.pop(nom, None)
    return module


def test_mutation_majeur_1_bornes_basses_d_astra(monde):
    """Le contrôle de la v6 (aucune borne basse pour Astra) réintroduit : l'essai du relais jeté échoue."""
    m = _mutant("lanceur_v7_mutant_majeur_1", [('        if nom in ("kimi", "astra"):\n            part = ',
                                               '        if False:\n            part = ')])
    with pytest.raises(pytest.fail.Exception):
        essai_relais_jete_refuse(m, monde)
    monde["cmdlines"][PID_ASTRA] = _args_astra(monde)
    essai_relais_jete_refuse(L, monde)                                        # le lanceur v7 tient


def test_mutation_majeur_2_exclusion_des_deux_courses(monde):
    """La v6 (aucun regard sur l'autre course) réintroduite : l'essai de la course d'auto-conception en cours échoue."""
    m = _mutant("lanceur_v7_mutant_majeur_2", [("    autres_courses = verifier_autres_courses(r, releve_brut)  # v7, majeur 2\n",
                                                "    autres_courses = {\"autres_courses\": []}\n")])
    with pytest.raises(AssertionError):
        essai_auto_conception_en_cours_refusee(m.principal, monde)           # le mutant part (code 0)
    monde["r"].dossier_runs = monde["tmp"] / "runs-ter"
    essai_auto_conception_en_cours_refusee(L.principal, monde)                # le lanceur v7 refuse


def essai_etat_vide_refuse(module, m) -> None:
    """L'essai du mineur 3 : un état qui ne rend que le plafond (ni appels, ni dépense, ni engagement) est refusé."""
    b = {"pid_relais": PID_CLAUDE, "nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT", "url_relais": CONTEXTE["url_claude"]}
    m["etat_claude"].clear()
    m["etat_claude"]["plafond_usd"] = 150.0
    with pytest.raises(module.Refus):
        module.controler_relais_vivant(m["r"], "claude", b, FIXE, 5, None)


def test_mutation_mineur_3_etat_vide(monde):
    """La lecture de la v6 (champs absents tenus pour nuls) réintroduite : l'essai de l'état vide échoue."""
    m = _mutant("lanceur_v7_mutant_mineur_3", [
        ('    champs = ("appels",) + (("depense_usd", "engage_usd") if nom in RELAIS_A_DOLLARS else ()) \\\n'
         '        + (("lots_crees", "releves") if nom == "carbon" else ())  # v8 : « releves » nul exigé aussi pour Carbon\n',
         "    champs = ()\n")])
    with pytest.raises(pytest.fail.Exception):
        essai_etat_vide_refuse(m, monde)
    essai_etat_vide_refuse(L, monde)


# --- majeur 2, commandes exactes v7 : le texte dit l'exclusion, le relevé refait, l'arrêt par PID -------------------------------

COMMANDES_V7 = RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v9/commandes-exactes-course-affinage-v9.md"  # v9
EXIGENCES_COMMANDES = {
    "exclusion mutuelle": "ne tournent jamais en même temps",
    "ports partagés": "8787 à 8793",
    "relevé refait": "relevé des crédits refait",
    "relais jeté arrêté par PID": "relais jeté de la sonde",
    "kill par PID": "kill -INT",
    "-rs dans les essais": "pytest -q -rs",
    "quatre PID": "quatre PID",
    "aucun renvoi aux commandes v6": None,
}


def manques_des_commandes(texte: str) -> list:
    manques = [k for k, v in EXIGENCES_COMMANDES.items() if v is not None and v not in texte]
    if "commandes-exactes-course-affinage-v6" in texte.split("## Ce qui ne vaut plus")[0]:
        manques.append("aucun renvoi aux commandes v6")
    return manques


def test_v7_commandes_exactes_disent_le_majeur_2():
    assert manques_des_commandes(COMMANDES_V7.read_text(encoding="utf-8")) == []


def test_mutation_commandes_sans_l_exclusion_mutuelle():
    texte = COMMANDES_V7.read_text(encoding="utf-8")
    assert manques_des_commandes(texte.replace("ne tournent jamais en même temps", "")) == ["exclusion mutuelle"]
    assert "relevé refait" in manques_des_commandes(texte.replace("relevé des crédits refait", "relevé"))


def test_v7_commandes_citent_les_empreintes_du_lanceur_et_du_preenregistrement():
    texte = COMMANDES_V7.read_text(encoding="utf-8")
    assert L.sha256_fichier(CHEMIN_LANCEUR) in texte and L.PREREG_SHA256 in texte
    assert L.CONTRE_LECTURE in texte and "--max-appels 20" in texte and "--max-lots 20" in texte


# --- essais de la v6b portés (sonde commune réelle devant le relais factice ; commandes réelles de `main`) ------------------------

_spec_ts = importlib.util.spec_from_file_location("essais_sonde_astra_courses_v1_pour_v9", RACINE / "tests" / "test_sonde_astra_courses_v1.py")
TS = importlib.util.module_from_spec(_spec_ts)
_spec_ts.loader.exec_module(TS)
GABARIT_V7 = RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v9/declaration-relais-gabarit-course-affinage-v9.json"  # v9
COMMANDES_MAIN = {"astra": ("docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py", SHA_ASTRA),
                  "carbon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py",
                             "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75")}


def _octets_de_main(rel, sha):
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"refs/remotes/origin/main:{rel}"], capture_output=True)
    return p.stdout if p.returncode == 0 and hashlib.sha256(p.stdout).hexdigest() == sha else None


OCTETS_MAIN = {n: _octets_de_main(*v) for n, v in COMMANDES_MAIN.items()}


def declaration_v7_remplie(m) -> dict:
    assert all(OCTETS_MAIN.values()), "commandes absentes de origin/main (git fetch ciblé requis)"
    o = json.loads(GABARIT_V7.read_text(encoding="utf-8"))
    del o["gabarit"]
    o["redige_utc"] = "2026-11-18T11:00:00Z"
    f = o["fournisseurs"]
    for n in ("astra", "carbon"):
        p = m["tmp"] / Path(COMMANDES_MAIN[n][0]).name
        p.write_bytes(OCTETS_MAIN[n])
        f[n]["commande"][0], f[n]["commande"][3] = sys.executable, str(p)
        assert f[n]["commande"][4:] == L.ARGUMENTS_COMMANDES[n]
    ref = declaration(m["depot"])["fournisseurs"]
    f["claude"].update(porte_plafond=ref["claude"]["porte_plafond"], url_relais=ref["claude"]["url_relais"], pid_relais=PID_CLAUDE)
    f["argon"].update(commande=ref["argon"]["commande"], nom_cle="CLE_ESSAI_A", pid_relais=PID_ARGON)
    f["carbon"].update(nom_cle="CLE_ESSAI_G", pid_relais=PID_CARBON)
    f["astra"].update(nom_cle="CLE_ESSAI_S", pid_relais=PID_ASTRA)
    return o


def sonde_commune_reelle(m, reserve=0.01) -> int:
    """Joue la sonde commune (script épinglé) devant le relais factice (code du relais épinglé) ; ses deux rapports sont
    écrits aux chemins que lit le lanceur v7 pour le jour de l'essai (`date -u`)."""
    p_cmd = m["tmp"] / "sonde" / "commande_astra_v1.py"
    p_cmd.parent.mkdir(exist_ok=True)
    p_cmd.write_bytes(OCTETS_MAIN["astra"])
    relais_copie = m["tmp"] / "sonde" / "relais_kimi_v4.py"
    relais_copie.write_bytes(TS.CHEMIN_RELAIS.read_bytes())
    jour = subprocess.run(["date", "-u", "+%F"], capture_output=True, text=True).stdout.strip()
    depot = m["depot"]
    sortie_v2, sortie_c = depot / L.SONDE_ASTRA, depot / COMMUNE_DU_JOUR.replace("2026-11-18", jour)
    for s in (sortie_v2, sortie_c, depot / COMMUNE_DU_JOUR):
        s.unlink(missing_ok=True)
        Path(str(s) + ".sha256").unlink(missing_ok=True)
    sortie_c.parent.mkdir(parents=True, exist_ok=True)
    amont = TS.FauxAmont()
    relais = TS.RelaisFactice(amont, reserve=reserve)
    try:
        code = TS.S.sonder(p_cmd, relais.url, os.getpid(), sortie_c, sortie_v2,
                           lire_cmd=lambda pid: [sys.executable, str(relais_copie), "--port", str(relais.port)], amont=amont.url)
    finally:
        relais.fermer()
    m["r"].aujourd_hui = dt.date.fromisoformat(jour)
    m["jour"] = jour
    return code


def _ecrire_tout_v7(m, decl):
    _decl(m, decl)
    objet = dict(releve(CLE_ESSAI_G={"non_lisible": True, "motif": "illisible"}, CLE_ESSAI_S={"non_lisible": True, "motif": "illisible"}),
                 dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_A", "CLE_ESSAI_G", "CLE_ESSAI_S"]})
    objet["releve_utc"] = f"{m.get('jour', '2026-11-18')}T07:00:00Z"
    _releve(m, objet)
    for p in (m["r"].releve_prix,):
        o = json.loads(p.read_text())
        o["releve_utc"] = f"{m.get('jour', '2026-11-18')}T06:55:00Z"
        p.unlink()
        Path(str(p) + ".sha256").unlink()
        ecrire_scelle(p, o)


def test_v6b_porte_declaration_v7_cinq_especes_kimi_absent(monde):
    d = L.verifier_declaration(declaration_v7_remplie(monde), FIXE, monde["r"])
    actives = [e["etiquette"] for e in d["especes_actives"]]
    assert len(actives) == 5 and {"prop-astra", "prop-carbon", "prop-argon"} <= set(actives)
    assert not any("kimi" in e for e in actives) and d["carbon"]["active"] is True
    assert d["compter_limite_de_debit_comme_soupcon"] is False and d["kimi_autorise_par_la_mere"] is None


def test_v6b_porte_bout_en_bout_avec_la_sonde_commune(monde):
    assert sonde_commune_reelle(monde) == 0
    _ecrire_tout_v7(monde, declaration_v7_remplie(monde))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]
    assert dep["sonde_astra"]["cout_usd"] <= 0.05 and dep["sonde_astra"]["sonde_commune"]["sha256"]
    assert dep["devis_estimation_sans_marge_usd"] == pytest.approx(41.136)
    fin = json.loads((un_run(monde["r"]) / "manifeste-lanceur-fin.json").read_text())
    assert fin["ecart_au_devis"]["devis_estimation_sans_marge_usd"] == pytest.approx(41.136)   # v8 : Carbon à 0,4985


def test_v6b_porte_sonde_commune_echouee_astra_refusee(monde, capsys):
    assert sonde_commune_reelle(monde, reserve=0.40) == 1                      # échec de configuration : aucun rapport v2
    _ecrire_tout_v7(monde, declaration_v7_remplie(monde))
    assert lancer(monde["r"]) == 2
    assert "sonde d'Astra" in capsys.readouterr().err


def test_v6b_porte_sonde_sur_le_relais_de_la_course_refusee(monde, capsys):
    assert sonde_commune_reelle(monde) == 0
    decl = declaration_v7_remplie(monde)
    v2 = json.loads((monde["depot"] / L.SONDE_ASTRA).read_text())
    decl["fournisseurs"]["astra"]["pid_relais"] = v2["relais_pid"]
    monde["cmdlines"][v2["relais_pid"]] = monde["cmdlines"][PID_ASTRA]
    _ecrire_tout_v7(monde, decl)
    assert lancer(monde["r"]) == 2
    assert "relais de la course" in capsys.readouterr().err


def test_v6b_porte_relais_de_course_d_astra_non_neuf_refuse(monde, capsys):
    assert sonde_commune_reelle(monde) == 0
    _ecrire_tout_v7(monde, declaration_v7_remplie(monde))
    monde["etats"]["8790"]["appels"] = 1
    assert lancer(monde["r"]) == 2
    err = capsys.readouterr().err
    assert "astra" in err and "neuf" in err, err
    monde["etats"]["8790"]["appels"] = 0
    assert lancer(monde["r"]) == 0


# =================================================================================================================================
# v8 — essais neufs : réglages de la commande de Carbon (pensée, sortie, délai) et relevés du relais de Carbon. Un cas sain et un
# artefact (R5) par garde neuve ; une mutation par garde (le code fautif réintroduit fait échouer un essai) ; l'arithmétique de la
# garde du lanceur recoupée avec la vraie commande de Carbon de `main` (aucun réseau : ouvreur factice).
# =================================================================================================================================

_spec7 = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v7_pour_v9",
                                                RACINE / "scripts" / "lancer_course_affinage_mentors_v7.py")
L7 = importlib.util.module_from_spec(_spec7)
sys.modules["lancer_course_affinage_mentors_v7_pour_v9"] = L7
_spec7.loader.exec_module(L7)

LISTE = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text(encoding="utf-8"))
PIECES_CONSIGNE = {"consigne_proposeur": {"absolu": str(RACINE / L.PIECES["consigne_proposeur"][0])}}
ARGS_V8 = list(L.ARGUMENTS_COMMANDES["carbon"])


def _args_carbon(**valeurs) -> list:
    """Arguments de la commande de Carbon v8 avec des options remplacées (None : option et valeur retirées)."""
    a = list(ARGS_V8)
    for opt, v in valeurs.items():
        o = "--" + opt.replace("_", "-")
        k = a.index(o)
        if v is None:
            del a[k:k + 2]
        else:
            a[k + 1] = str(v)
    return a


def _decl_carbon(args: list) -> dict:
    return {"fournisseurs": {"carbon": {"commande": [sys.executable, "-I", "-B", "/x/commande_gemini_lot_v1.py"] + list(args)}}}


def test_v8_constantes_et_arguments_epingles():
    assert L.VERSION == "lancer_course_affinage_mentors_v9" and L.PREREG.endswith("course-v9/preenregistrement-course-affinage-mentors-v9.md")
    assert L.CONTRE_LECTURE.endswith("course-v9/contre-lecture-preenregistrement-course-affinage-mentors-v9.md")
    a = L.ARGUMENTS_COMMANDES["carbon"]
    for opt, v in (("--provision-pensee-jetons", "28672"), ("--max-sortie-jetons", "32768"), ("--sortie-min-jetons", "4096"),
                   ("--delai-s", "1620"), ("--intervalle-s", "30"), ("--delai-requete-s", "60"), ("--facteur-lot", "0.5")):
        assert a[a.index(opt) + 1] == v
    assert L.ARGUMENTS_COMMANDES["astra"] == L7.ARGUMENTS_COMMANDES["astra"]       # Astra : aucune reprise, commande inchangée
    assert L.COMMANDES_EPINGLEES == L7.COMMANDES_EPINGLEES                          # commandes épinglées inchangées
    assert L.MIN_RELEVES_CARBON == 1120 and L.PLAFOND_ARRET_USD == 150.0
    assert L.PREREG_SHA256 == hashlib.sha256((RACINE / L.PREREG).read_bytes()).hexdigest()


# --- garde 1 : options de Carbon exigées, une fois chacune, lisibles ---------------------------------------------------------------


def test_v8_options_carbon_sain():
    lues = L.lire_reglages_carbon(ARGS_V8)
    assert lues["--provision-pensee-jetons"] == 28672 and lues["--delai-s"] == 1620 and lues["--delai-requete-s"] == 60
    assert set(lues) == set(L.OPTIONS_CARBON_EXIGEES)


@pytest.mark.parametrize("option", [o[2:].replace("-", "_") for o in L.OPTIONS_CARBON_EXIGEES])
def test_v8_option_carbon_absente_refusee(option):
    with pytest.raises(L.Refus, match="absentes"):
        L.lire_reglages_carbon(_args_carbon(**{option: None}))


@pytest.mark.parametrize("args, motif", [
    (ARGS_V8 + ["--delai-s", "3000"], "plusieurs fois"),
    (_args_carbon(provision_pensee_jetons="beaucoup"), "illisible"),
    (_args_carbon(delai_s="0"), "strictement positif"),
    (_args_carbon(prix_sortie="nan"), "strictement positif"),
    (_args_carbon(facteur_lot="-1"), "strictement positif"),
])
def test_v8_option_carbon_artefacts(args, motif):
    with pytest.raises(L.Refus, match=motif):
        L.lire_reglages_carbon(args)


def test_v8_arguments_v7_de_carbon_refuses_a_la_declaration(monde, monkeypatch, capsys):
    """Les arguments de la v7 (pensée 8 192, délai 1 500 s, délai de requête par défaut) : refusés, motif précis."""
    sc = script_commande(monde["tmp"], "commande_gemini_lot_v1", {"texte": "", "cout_usd": 0.01})
    _carbon(monde, monkeypatch, commande=[sys.executable, "-I", "-B", str(sc)] + list(L7.ARGUMENTS_COMMANDES["carbon"]))
    assert lancer(monde["r"]) == 2
    assert "absentes" in capsys.readouterr().err


@pytest.mark.parametrize("option", ["provision_pensee_jetons", "max_sortie_jetons", "delai_s", "delai_requete_s"])
def test_v8_declaration_sans_option_refusee_bout_en_bout(monde, monkeypatch, capsys, option):
    sc = script_commande(monde["tmp"], "commande_gemini_lot_v1", {"texte": "", "cout_usd": 0.01})
    _carbon(monde, monkeypatch, commande=[sys.executable, "-I", "-B", str(sc)] + _args_carbon(**{option: None}))
    assert lancer(monde["r"]) == 2
    assert "absentes" in capsys.readouterr().err


# --- garde 2 : provision de pensée ≥ 1,25 × la plus forte pensée observée -------------------------------------------------------


def test_v8_provision_sain_et_limite():
    out = L.controler_delai_carbon(L.lire_reglages_carbon(ARGS_V8), FIXE)
    assert out["provision_minimale_jetons"] == 25870
    L.controler_delai_carbon(L.lire_reglages_carbon(_args_carbon(provision_pensee_jetons=25870)), FIXE)   # à la borne : passe


@pytest.mark.parametrize("p", [8192, 20696, 25869])
def test_v8_provision_artefacts(p):
    with pytest.raises(L.Refus, match="provision-pensee-jetons"):
        L.controler_delai_carbon(L.lire_reglages_carbon(_args_carbon(provision_pensee_jetons=p)), FIXE)


# --- garde 3 : durée maximale de la commande sous le délai de l'orchestrateur et d'A3 ; délai de lot relevé ----------------------


def test_v8_delai_sain():
    out = L.controler_delai_carbon(L.lire_reglages_carbon(ARGS_V8), FIXE)
    assert out["duree_max_s"] == 1770 and out["borne_s"] == 1800 and out["duree_max_s"] + out["marge_s"] <= out["borne_s"]


@pytest.mark.parametrize("valeurs, motif", [
    ({"delai_s": 3000}, "durée maximale"),                                     # 3 000 s demandés : l'orchestrateur tuerait la commande
    ({"delai_requete_s": 120}, "durée maximale"),                              # 1 620 + 30 + 240 = 1 890 s
    ({"delai_s": 1700}, "durée maximale"),
    ({"delai_s": 1500}, "1620"),                                               # le délai de la v7 : refusé
    ({"intervalle_s": 61}, "durée maximale"),
])
def test_v8_delai_artefacts(valeurs, motif):
    with pytest.raises(L.Refus, match=motif):
        L.controler_delai_carbon(L.lire_reglages_carbon(_args_carbon(**valeurs)), FIXE)


def test_v8_delai_a3_de_la_configuration():
    fixe = json.loads(json.dumps(FIXE))
    fixe["arrets"]["a3_delai_s"]["carbon"] = 1700                               # A3 plus court que l'adaptateur : il borne
    with pytest.raises(L.Refus, match="1700"):
        L.controler_delai_carbon(L.lire_reglages_carbon(ARGS_V8), fixe)
    fixe["arrets"]["a3_delai_s"] = {}
    with pytest.raises(L.Refus, match="a3_delai_s"):
        L.controler_delai_carbon(L.lire_reglages_carbon(ARGS_V8), fixe)
    assert FIXE["arrets"]["a3_delai_s"] == {"*": 1800}                        # configuration v6 épinglée : 1 800 s


# --- garde 4 : chaque appel de Carbon peut partir ; pire cas d'un appel sous le plafond de session ------------------------------


def test_v8_pire_cas_carbon_sain():
    out = L.controler_pire_cas_carbon(_decl_carbon(ARGS_V8), FIXE, LISTE, PIECES_CONSIGNE)
    long, court = out["cas"]["entree_la_plus_longue"], out["cas"]["entree_la_plus_courte"]
    assert out["plafond_session_usd"] == 3.0 and out["part_au_pire_usd"] == 48.0                       # v9
    assert long["caracteres"] == 7478 and long["entree_gardee_jetons"] == 2618 and long["sortie_demandee_jetons"] == 32768
    assert court["sortie_demandee_jetons"] == 32768
    assert long["pire_cas_appel_usd_prix_plein"] == pytest.approx(2.571489, abs=1e-6)
    assert court["pire_cas_appel_usd_prix_plein"] == pytest.approx(2.56211, abs=1e-6)
    assert long["pire_cas_appel_usd_prix_du_lot"] == pytest.approx(1.285745, abs=1e-6)
    for c in (long, court):
        assert c["pire_cas_minimal_usd"] <= 3.0 and c["pire_cas_appel_usd_prix_plein"] <= 3.0
    assert L.controler_pire_cas_carbon({"fournisseurs": {}}, FIXE, LISTE, PIECES_CONSIGNE) is None   # Carbon non active


@pytest.mark.parametrize("valeurs", [{"provision_pensee_jetons": 70000}, {"sortie_min_jetons": 50000},
                                     {"prix_sortie": 100}])
def test_v8_pire_cas_carbon_artefacts(valeurs):
    with pytest.raises(L.Refus, match="code 4"):
        L.controler_pire_cas_carbon(_decl_carbon(_args_carbon(**valeurs)), FIXE, LISTE, PIECES_CONSIGNE)


def test_v8_pire_cas_sous_un_plafond_de_session_plus_bas_refuse():
    fixe = json.loads(json.dumps(FIXE))
    fixe["plafonds_session"]["proposeur"] = 1.2
    with pytest.raises(L.Refus, match="plafond de session 1.2"):
        L.controler_pire_cas_carbon(_decl_carbon(ARGS_V8), fixe, LISTE, PIECES_CONSIGNE)


class _Reponse:
    def __init__(self, objet):
        self.objet = objet

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def read(self):
        return json.dumps(self.objet).encode("utf-8")


class _OuvreurFactice:
    """Aucun réseau : `countTokens` rend 1 jeton (l'entrée gardée est alors celle des caractères, comme dans le lanceur) ; la
    création du lot est capturée puis rendue sans nom valide (code 3 de la commande, coût rendu au pire cas)."""

    def __init__(self):
        self.lots = []

    def open(self, req, timeout=None):
        if req.full_url.endswith(":countTokens"):
            return _Reponse({"totalTokens": 1})
        self.lots.append(json.loads(req.data))
        return _Reponse({"name": "nom invalide"})


def _vraie_commande_carbon(tmp_path):
    assert OCTETS_MAIN["carbon"], "commande de Carbon absente de origin/main (git fetch ciblé requis)"
    p = tmp_path / "commande_gemini_lot_v1_de_main.py"
    p.write_bytes(OCTETS_MAIN["carbon"])
    s = importlib.util.spec_from_file_location("commande_gemini_lot_v1_de_main", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def _consigne_la_plus_longue() -> str:
    consigne = Path(PIECES_CONSIGNE["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8")
    servies = [L.consigne_servie_proposeur(consigne, L.expurger(L.texte_de_case(f))[0]) for f in LISTE["fils"]]
    return max(servies, key=len)


def test_v8_arithmetique_recoupee_avec_la_vraie_commande_de_carbon(tmp_path):
    """La vraie commande de `main` (9484dce0…), jouée hors réseau sur la consigne servie la plus longue et un plafond de session
    de 1,50 USD : elle demande exactement la sortie et la pensée que le lanceur annonce, et rend le pire cas qu'il calcule."""
    C = _vraie_commande_carbon(tmp_path)
    attendu = L.controler_pire_cas_carbon(_decl_carbon(ARGS_V8), FIXE, LISTE, PIECES_CONSIGNE)["cas"]["entree_la_plus_longue"]
    env = {"ROLE_POLE": "proposeur_ideation", "PLAFOND_SESSION_USD": "3.0", "MODELE_DEMANDE_POLE": "gemini-4-carbon"}  # v9
    o = _OuvreurFactice()
    code, ligne = C.executer(C.analyseur().parse_args(ARGS_V8), _consigne_la_plus_longue(), env, o, dormir=lambda s: None)
    assert code == 3 and len(o.lots) == 1
    gen = o.lots[0]["batch"]["input_config"]["requests"]["requests"][0]["request"]["generationConfig"]
    assert gen["maxOutputTokens"] == attendu["sortie_demandee_jetons"] == 32768 >= L.SORTIE_RETENUE_MIN_CARBON
    assert gen["thinkingConfig"]["thinkingBudget"] == 28672
    assert ligne["cout_usd"] == pytest.approx(attendu["pire_cas_appel_usd_prix_plein"], abs=1e-6) and ligne["cout_usd"] <= 3.0


def test_v8_provision_32768_la_vraie_commande_refuse_chaque_appel(tmp_path):
    """Artefact (constat de la v8, sous 1,50 USD) : la provision de 32 768 ; la vraie commande rend le code 4 sans rien envoyer."""
    C = _vraie_commande_carbon(tmp_path)
    env = {"ROLE_POLE": "proposeur_ideation", "PLAFOND_SESSION_USD": "1.5", "MODELE_DEMANDE_POLE": "gemini-4-carbon"}
    consigne = Path(PIECES_CONSIGNE["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8")
    for texte in (_consigne_la_plus_longue(), L.consigne_servie_proposeur(consigne, "x")):
        o = _OuvreurFactice()
        code, ligne = C.executer(C.analyseur().parse_args(_args_carbon(provision_pensee_jetons=32768)), texte, env, o,
                                 dormir=lambda s: None)
        assert code == 4 and o.lots == [] and ligne["cout_usd"] == 1e-6


def test_v8_carbon_bout_en_bout_reglages_au_manifeste(monde, monkeypatch):
    _carbon(monde, monkeypatch)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    rc = dep["reglages_carbon_v8"]
    assert rc["reglages"]["--provision-pensee-jetons"] == 28672 and rc["delai"]["duree_max_s"] == 1770
    assert rc["cas"]["entree_la_plus_longue"]["sortie_demandee_jetons"] == 32768
    assert rc["cas"]["entree_la_plus_longue"]["pire_cas_appel_usd_prix_plein"] <= 3.0
    assert dep["procedure_relais_persistants"]["relais_vivants"]["carbon"]["releves_restants"] == 2000


def test_v8_sans_carbon_reglages_non_actifs(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["reglages_carbon_v8"] == {"carbon": "non active"}


# --- garde 5 : relevés du relais de Carbon ----------------------------------------------------------------------------------------


def test_v8_releves_carbon_sain(monde):
    out = L.controler_relais_vivant(monde["r"], "carbon", dict(B_CARBON), FIXE, 5, None)
    assert out["releves_restants"] == 2000
    monde["etats"]["8792"]["releves_restants"] = 1120                                     # à la borne : passe
    assert L.controler_relais_vivant(monde["r"], "carbon", dict(B_CARBON), FIXE, 5, None)["releves_restants"] == 1120


@pytest.mark.parametrize("etat, motif", [({"releves_restants": 1119}, "releves_restants"),
                                         ({"releves_restants": None}, "releves_restants"),
                                         ({"releves_restants": "beaucoup"}, "releves_restants"),
                                         ({"releves": 3}, "déjà employé"),
                                         ({"releves": None}, "sans")])
def test_v8_releves_carbon_artefacts(monde, etat, motif):
    for cle, v in etat.items():
        if v is None:
            monde["etats"]["8792"].pop(cle)
        else:
            monde["etats"]["8792"][cle] = v
    with pytest.raises(L.Refus, match=motif):
        L.controler_relais_vivant(monde["r"], "carbon", dict(B_CARBON), FIXE, 5, None)


# --- mutations : une par garde neuve ----------------------------------------------------------------------------------------------


def essai_option_absente(module) -> None:
    with pytest.raises(module.Refus) as e:
        module.lire_reglages_carbon(_args_carbon(delai_requete_s=None))
    assert "absentes" in str(e.value)


def test_mutation_v8_options_exigees():
    m = _mutant("lanceur_v8_mutant_options", [
        ("    manquantes = [o for o in OPTIONS_CARBON_EXIGEES if o not in args]\n", "    manquantes = []\n"),
        ("    doubles = [o for o in OPTIONS_CARBON_EXIGEES if args.count(o) != 1]\n", "    doubles = []\n")])
    with pytest.raises(AssertionError):
        essai_option_absente(m)
    essai_option_absente(L)


def essai_provision_basse(module) -> None:
    with pytest.raises(module.Refus, match="provision"):
        module.controler_delai_carbon(module.lire_reglages_carbon(_args_carbon(provision_pensee_jetons=8192)), FIXE)


def test_mutation_v8_provision():
    m = _mutant("lanceur_v8_mutant_provision", [('    if lues["--provision-pensee-jetons"] < minimum:\n', "    if False:\n")])
    with pytest.raises(pytest.fail.Exception):
        essai_provision_basse(m)
    essai_provision_basse(L)


def essai_delai_3000(module) -> None:
    with pytest.raises(module.Refus, match="durée maximale"):
        module.controler_delai_carbon(module.lire_reglages_carbon(_args_carbon(delai_s=3000)), FIXE)


def test_mutation_v8_duree_sous_l_orchestrateur():
    m = _mutant("lanceur_v8_mutant_duree", [("    if duree_max + MARGE_DELAI_CARBON_S > borne:\n", "    if False:\n")])
    with pytest.raises(pytest.fail.Exception):
        essai_delai_3000(m)
    essai_delai_3000(L)


def essai_delai_de_la_v7(module) -> None:
    with pytest.raises(module.Refus, match="1620"):
        module.controler_delai_carbon(module.lire_reglages_carbon(_args_carbon(delai_s=1500)), FIXE)


def test_mutation_v8_delai_releve():
    m = _mutant("lanceur_v8_mutant_delai_releve", [('    if lues["--delai-s"] < DELAI_CARBON_S:\n', "    if False:\n")])
    with pytest.raises(pytest.fail.Exception):
        essai_delai_de_la_v7(m)
    essai_delai_de_la_v7(L)


def essai_provision_32768(module) -> None:  # v9 : sous 3,00 USD, une provision de 70 000 ne laisse plus partir aucun appel
    with pytest.raises(module.Refus, match="code 4"):
        module.controler_pire_cas_carbon(_decl_carbon(_args_carbon(provision_pensee_jetons=70000)), FIXE, LISTE, PIECES_CONSIGNE)


def test_mutation_v8_pire_cas_minimal():
    m = _mutant("lanceur_v8_mutant_pire_cas", [("        if minimal > plafond + 1e-12:\n", "        if False:\n")])
    # v9 : le mutant est encore refusé, mais par la garde de la sortie retenue (motif autre que « code 4 ») : l'essai échoue
    with pytest.raises((pytest.fail.Exception, AssertionError)):
        essai_provision_32768(m)
    essai_provision_32768(L)


def essai_carbon_qui_ne_partirait_jamais(module, monde, monkeypatch) -> int:
    """Bout en bout : la déclaration et la table des arguments portent une provision de 70 000 (v9 : Carbon ne partirait jamais)."""
    sc = script_commande(monde["tmp"], "commande_gemini_lot_v1", {"texte": "", "cout_usd": 0.01})
    args = _args_carbon(provision_pensee_jetons=70000)
    monkeypatch.setitem(module.ARGUMENTS_COMMANDES, "carbon", args)
    monkeypatch.setitem(module.COMMANDES_EPINGLEES, "carbon", {sc.name: hashlib.sha256(sc.read_bytes()).hexdigest()})
    monkeypatch.setattr(module, "PROVISION_PENSEE_CARBON", 70000)
    _carbon(monde, monkeypatch, commande=[sys.executable, "-I", "-B", str(sc)] + args)
    return module.principal([], reglages=monde["r"])


def test_mutation_v8_garde_du_pire_cas_appelee_au_depart(monde, monkeypatch, capsys):
    m = _mutant("lanceur_v8_mutant_appel_pire_cas", [
        ("    reglages_carbon = controler_pire_cas_carbon(decl, fixe, liste, pieces)  # v8 : chaque appel peut partir, pire cas écrit\n",
         "    reglages_carbon = None\n")])
    assert essai_carbon_qui_ne_partirait_jamais(L, monde, monkeypatch) == 2           # le lanceur v8 refuse
    assert "code 4" in capsys.readouterr().err
    assert essai_carbon_qui_ne_partirait_jamais(m, monde, monkeypatch) == 0           # le mutant part : Carbon muette en course


def test_mutation_v8_options_lues_a_la_declaration(monde, monkeypatch, capsys):
    m = _mutant("lanceur_v8_mutant_declaration", [
        ("                controler_delai_carbon(lire_reglages_carbon(c[4:]), fixe)\n", "                pass\n")])
    sc = script_commande(monde["tmp"], "commande_gemini_lot_v1", {"texte": "", "cout_usd": 0.01})
    _carbon(monde, monkeypatch, commande=[sys.executable, "-I", "-B", str(sc)] + list(L7.ARGUMENTS_COMMANDES["carbon"]))
    monkeypatch.setitem(m.COMMANDES_EPINGLEES, "carbon", {sc.name: hashlib.sha256(sc.read_bytes()).hexdigest()})
    assert m.principal([], reglages=monde["r"]) == 2
    assert "absentes" not in capsys.readouterr().err                                    # le mutant ne dit pas le motif
    assert lancer(monde["r"]) == 2
    assert "absentes" in capsys.readouterr().err


def essai_releves_insuffisants(module, m) -> None:
    m["etats"]["8792"]["releves_restants"] = 1000
    with pytest.raises(module.Refus, match="releves_restants"):
        module.controler_relais_vivant(m["r"], "carbon", dict(B_CARBON), FIXE, 5, None)


def test_mutation_v8_releves_restants(monde):
    m = _mutant("lanceur_v8_mutant_releves", [("        if not _nombre(restants) or restants < MIN_RELEVES_CARBON:\n",
                                               "        if False:\n")])
    with pytest.raises(pytest.fail.Exception):
        essai_releves_insuffisants(m, monde)
    essai_releves_insuffisants(L, monde)


def essai_releves_deja_faits(module, m) -> None:
    m["etats"]["8792"]["releves"] = 5
    with pytest.raises(module.Refus, match="déjà employé"):
        module.controler_relais_vivant(m["r"], "carbon", dict(B_CARBON), FIXE, 5, None)


def test_mutation_v8_releves_nuls(monde):
    m = _mutant("lanceur_v8_mutant_releves_nuls", [('        + (("lots_crees", "releves") if nom == "carbon" else ())',
                                                    '        + (("lots_crees",) if nom == "carbon" else ())')])
    with pytest.raises(pytest.fail.Exception):
        essai_releves_deja_faits(m, monde)
    essai_releves_deja_faits(L, monde)


# --- devis v8, commandes v8, gabarit v8 ----------------------------------------------------------------------------------------


def test_v8_devis_prix_de_carbon():
    assert L.DEVIS_V5_PAR_APPEL["prop-carbon"] == 0.4985
    assert (2618 * 8.3 + (20000 + 3500) * 41.5) / 1e6 * 0.5 == pytest.approx(0.4985, abs=1e-4)
    autres = {k: v for k, v in L.DEVIS_V5_PAR_APPEL.items() if k != "prop-carbon"}
    assert autres == {k: v for k, v in L7.DEVIS_V5_PAR_APPEL.items() if k != "prop-carbon"}
    devis = (RACINE / "docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v8.md").read_text(encoding="utf-8")
    for chiffre in ("0,4985", "41,136", "45,25", "122,73", "1,499959", "174,00", "24,00", "150,00", "RR_ANTHROPIC_API_KEY_MINUIT",
                    "GEMINI_API_KEY"):
        assert chiffre in devis, chiffre


EXIGENCES_COMMANDES_V8 = {  # v9
    "lanceur v9": "scripts/lancer_course_affinage_mentors_v9.py",
    "contre-lecture v9": "course-v9/contre-lecture-preenregistrement-course-affinage-mentors-v9.md",
    "relais d'Astra à 48 USD": "--plafond-usd 48",
    "sortie de Carbon": "32768",
    "lancement détaché": "setsid",
    "bac à sable installé": "bwrap",
    "socat": "socat",
    "sonde neuve sous course-v9": "course-v9/sonde-astra-commune-",
    "provision de Carbon": "28672",
    "délai de Carbon": "1620",
    "relevés du relais de Carbon": "releves_restants",
    "une course à la fois": "ne tournent jamais en même temps",
}


def test_v8_commandes_exactes_completes():
    texte = COMMANDES_V7.read_text(encoding="utf-8")                                  # chemin v8 (porté)
    assert [k for k, v in EXIGENCES_COMMANDES_V8.items() if v not in texte] == []
    avant = texte.split("## Ce qui ne vaut plus")[0]
    assert "commandes-exactes-course-affinage-v7" not in avant and "commandes-exactes-course-affinage-v8" not in avant


def test_mutation_v8_commandes_sans_lancement_detache():
    texte = COMMANDES_V7.read_text(encoding="utf-8").replace("setsid", "")
    assert [k for k, v in EXIGENCES_COMMANDES_V8.items() if v not in texte] == ["lancement détaché"]


def test_v8_gabarit_porte_les_arguments_v8():
    o = json.loads(GABARIT_V7.read_text(encoding="utf-8"))                            # chemin v8 (porté)
    assert o["fournisseurs"]["carbon"]["commande"][4:] == ARGS_V8
    assert o["fournisseurs"]["astra"]["commande"][4:] == L.ARGUMENTS_COMMANDES["astra"]
    assert "kimi" not in o["fournisseurs"] and o["compter_limite_de_debit_comme_soupcon"] is False


# =================================================================================================================================
# v9 — essais neufs : configuration v9 (plafond de session des proposeurs 3,00 USD), sortie retenue de Carbon ≥ 24 500 jetons
# (la sortie maximale compte la pensée), parts au pire recalculées, devis v9. Cas sain, artefacts, mutation ; la vraie commande
# de Carbon de `main` rejouée hors réseau sous les deux plafonds.
# =================================================================================================================================

FIXE_V6 = json.loads((RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v6/configuration-course-affinage-mentors-v6.json")
                     .read_text(encoding="utf-8"))
_spec8 = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v8_pour_v9",
                                                RACINE / "scripts" / "lancer_course_affinage_mentors_v8.py")
L8 = importlib.util.module_from_spec(_spec8)
sys.modules["lancer_course_affinage_mentors_v8_pour_v9"] = L8
_spec8.loader.exec_module(L8)


def test_v9_configuration_seul_le_plafond_des_proposeurs_change():
    chemin, sha = L.PIECES["configuration"]
    assert chemin.endswith("course-v9/configuration-course-affinage-mentors-v9.json")
    assert hashlib.sha256((RACINE / chemin).read_bytes()).hexdigest() == sha
    assert FIXE["plafonds_session"]["proposeur"] == 3.0 and FIXE_V6["plafonds_session"]["proposeur"] == 1.5
    differences = sorted(k for k in set(FIXE) | set(FIXE_V6) if FIXE.get(k) != FIXE_V6.get(k))
    assert differences == ["plafonds_session", "statut", "version"]
    assert {k: v for k, v in FIXE["plafonds_session"].items() if k != "proposeur"} == \
        {k: v for k, v in FIXE_V6["plafonds_session"].items() if k != "proposeur"}
    assert FIXE["budget"] == FIXE_V6["budget"] and FIXE["arrets"] == FIXE_V6["arrets"]
    autres = {k: v for k, v in L.PIECES.items() if k != "configuration"}
    assert autres == {k: v for k, v in L8.PIECES.items() if k != "configuration"}          # aucune autre pièce ne change
    assert L.ARGUMENTS_COMMANDES["astra"] == L8.ARGUMENTS_COMMANDES["astra"]              # Astra : aléa accepté, commande inchangée


def test_v9_arguments_de_carbon():
    diff = [(a, b) for a, b in zip(L8.ARGUMENTS_COMMANDES["carbon"], L.ARGUMENTS_COMMANDES["carbon"]) if a != b]
    assert diff == [("16384", "32768")] and len(L8.ARGUMENTS_COMMANDES["carbon"]) == len(L.ARGUMENTS_COMMANDES["carbon"])
    assert L.SORTIE_RETENUE_MIN_CARBON == 24500 >= L.PENSEE_OBSERVEE_MAX_JETONS + L.REPONSE_OBSERVEE_MAX_JETONS


# --- garde v9 : sortie retenue par la commande ≥ 24 500 jetons --------------------------------------------------------------------


def test_v9_sortie_retenue_saine():
    out = L.controler_pire_cas_carbon(_decl_carbon(ARGS_V8), FIXE, LISTE, PIECES_CONSIGNE)
    assert all(c["sortie_demandee_jetons"] == 32768 >= 24500 for c in out["cas"].values())


@pytest.mark.parametrize("valeurs", [{"max_sortie_jetons": 16384},           # la sortie maximale de la v8
                                     {"max_sortie_jetons": 24499},
                                     {"provision_pensee_jetons": 50000}])    # le plafond paie alors moins de 24 500 jetons
def test_v9_sortie_retenue_artefacts(valeurs):
    with pytest.raises(L.Refus, match="sortie retenue"):
        L.controler_pire_cas_carbon(_decl_carbon(_args_carbon(**valeurs)), FIXE, LISTE, PIECES_CONSIGNE)


def test_v9_sortie_retenue_a_la_borne():
    out = L.controler_pire_cas_carbon(_decl_carbon(_args_carbon(max_sortie_jetons=24500)), FIXE, LISTE, PIECES_CONSIGNE)
    assert out["cas"]["entree_la_plus_longue"]["sortie_demandee_jetons"] == 24500


def essai_plafond_de_la_v8(module) -> None:
    """Sous le plafond de session de la configuration v6 (1,50), les réglages v9 laissent 6 948 jetons : refus."""
    with pytest.raises(module.Refus, match="sortie retenue"):
        module.controler_pire_cas_carbon(_decl_carbon(ARGS_V8), FIXE_V6, LISTE, PIECES_CONSIGNE)


def test_v9_plafond_de_session_de_la_v8_refuse():
    essai_plafond_de_la_v8(L)


def test_mutation_v9_sortie_retenue():
    m = _mutant("lanceur_v9_mutant_sortie_retenue", [("        if demandee < SORTIE_RETENUE_MIN_CARBON:", "        if False:")])
    with pytest.raises(pytest.fail.Exception):
        essai_plafond_de_la_v8(m)
    essai_plafond_de_la_v8(L)


def test_v9_la_vraie_commande_sous_1_50_couperait_la_reponse(tmp_path):
    """Le constat qui fait la v9 : sous 1,50 USD, la vraie commande de `main` demande 6 948 jetons de sortie (pensée comprise,
    selon la documentation du fournisseur), moins que la pensée observée (20 696) : le lanceur v9 refuse ce régime."""
    C = _vraie_commande_carbon(tmp_path)
    env = {"ROLE_POLE": "proposeur_ideation", "PLAFOND_SESSION_USD": "1.5", "MODELE_DEMANDE_POLE": "gemini-4-carbon"}
    o = _OuvreurFactice()
    code, _ligne = C.executer(C.analyseur().parse_args(ARGS_V8), _consigne_la_plus_longue(), env, o, dormir=lambda s: None)
    gen = o.lots[0]["batch"]["input_config"]["requests"]["requests"][0]["request"]["generationConfig"]
    assert code == 3 and gen["maxOutputTokens"] == 6948 < L.PENSEE_OBSERVEE_MAX_JETONS


def test_v9_pire_cas_toujours_sous_le_plafond():
    for p in (25870, 28672, 30000, 40000):
        for smax in (24500, 32768, 65536):
            try:
                out = L.controler_pire_cas_carbon(_decl_carbon(_args_carbon(provision_pensee_jetons=p, max_sortie_jetons=smax)),
                                                  FIXE, LISTE, PIECES_CONSIGNE)
            except L.Refus as e:
                assert "sortie retenue" in str(e)
                continue
            assert all(c["pire_cas_appel_usd_prix_plein"] <= 3.0 for c in out["cas"].values())


# --- parts au pire, relais d'Astra, bout en bout ----------------------------------------------------------------------------------


def test_v9_parts_au_pire_bout_en_bout(monde, monkeypatch):
    _carbon(monde, monkeypatch)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["parts_au_pire"]["carbon"]["part_au_pire_usd"] == 48.0
    assert dep["parts_au_pire"]["claude"]["part_au_pire_usd"] == 150.0 and dep["parts_au_pire"]["argon"]["part_au_pire_usd"] == 150.0
    rc = dep["reglages_carbon_v8"]
    assert rc["plafond_session_usd"] == 3.0 and rc["part_au_pire_usd"] == 48.0
    assert rc["cas"]["entree_la_plus_longue"]["pire_cas_appel_usd_prix_plein"] == pytest.approx(2.571489, abs=1e-6)


def test_v9_relais_d_astra_des_commandes_v8_refuse(monde):
    """Le relais d'Astra des commandes v8 (24 USD) est sous la part v9 (48) : refus (402 sinon en fin d'étape)."""
    monde["cmdlines"][PID_ASTRA] = _args_astra(monde, plafond_usd="24")
    monde["etats"]["8790"]["plafond_usd"] = 24.0
    with pytest.raises(L.Refus, match="part au pire"):
        L.controler_relais_vivant(monde["r"], "astra", dict(B_ASTRA), FIXE, 5, PARTS_ASTRA)


def test_v9_cle_partagee_198_unitaire(tmp_path):
    parts = {"argon": {"part_au_pire_usd": 150.0}, "carbon": {"part_au_pire_usd": 48.0}}
    cles = {"argon": "CLE_G", "carbon": "CLE_G"}
    rel = {"releve_utc": "2026-11-18T07:00:00Z", "cles": {"CLE_G": {"credit_usd": 800.0, "reste_usd": 198.5, "source": "essai"}}}
    assert L.verifier_credits(rel, cles, AUJOURD_HUI, tmp_path / "a", parts)["CLE_G"]["part_au_pire_usd"] == 198.0
    rel["cles"]["CLE_G"]["reste_usd"] = 180.0                                       # assez en v8 (174), plus en v9
    with pytest.raises(L.AlerteCredit):
        L.verifier_credits(rel, cles, AUJOURD_HUI, tmp_path / "b", parts)


# --- devis v9, commandes v9 -----------------------------------------------------------------------------------------------------


def test_v9_devis():
    devis = (RACINE / "docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v9.md").read_text(encoding="utf-8")
    for chiffre in ("3,00", "32 768", "2,571489", "45,25", "141,59", "198,00", "48,00", "150,00", "24 500", "76,36",
                    "RR_ANTHROPIC_API_KEY_MINUIT", "GEMINI_API_KEY", "OPENAI_API_KEY"):
        assert chiffre in devis, chiffre
    assert L.devis_estimation(["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]) == pytest.approx(41.136)


def test_v9_commandes_ne_lancent_plus_le_relais_d_astra_a_24():
    texte = COMMANDES_V7.read_text(encoding="utf-8")                                  # chemin v9 (porté)
    assert "--plafond-usd 24 " not in texte and "--plafond-usd 48 " in texte
    assert L.sha256_fichier(CHEMIN_LANCEUR) in texte and L.PREREG_SHA256 in texte and L.PIECES["configuration"][1] in texte
