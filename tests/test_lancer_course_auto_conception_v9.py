"""Essais du lanceur v9 (additif v2i : mot de Lazar « Course à 150 USD (Recommandé) » — plafond d'arrêt 150 USD, seuils internes
relevés d'autant, les juges lancés au haut du devis ; règle de Lazar R-3661 — conservation des réponses brutes par une enveloppe
épinglée mise entre la garde de crédit et chaque commande externe, inventaire de fin scellé quelle que soit l'issue) — les essais
v8 portés (lignes, relais et crédits à 150 USD ; essais propres à la v8 portés sur le module v8 quand ils l'essaient), plus, pour
chaque garde neuve, un cas sain, des artefacts (R5) et une mutation : configuration v5, seuils au haut (comparés à la vraie
classe `BudgetV56` de l'orchestrateur épinglé), enveloppe de conservation dans la commande, réponse conservée identique à la
réponse rendue, écriture impossible qui arrête l'appel, inventaire écrit même sur issue en échec. Relais et orchestrateur
simulés, aucun appel réel, aucune clé.

Texte des essais v8 :

Essais du lanceur v8 (additif v2h : Argon proposeur sans troncature par une enveloppe neuve à deux branches, juge à
l'identique de la v5 ; plafond de session des proposeurs 6,05 USD, sortie maximale exigée aux deux comptes) — les essais v7 portés
(sauf ceux que la v8 remplace : bout en bout, additif réel, configuration, constantes, essai à blanc), plus, pour chaque garde
neuve, un cas sain, des artefacts (R5) et une mutation. Relais et orchestrateur simulés, faux amont local pour l'enveloppe
d'Argon (aucun port de course), aucun appel réel, aucune clé.

Texte des essais v7 :

Essais du lanceur v7 (additif v2g : Carbon par la commande synchrone d'Argon, sans troncature ; plafonds relevés, 6 USD par
appel et 120 USD d'arrêt ; clé Claude Minuit sur le mot de Lazar ; courses v4 et v6 closes admises) — les essais v6 portés
(gardes générales, course jouée par le vrai noyau, bornes Gemini, épreuve recalculée, sonde d'Astra, composition), plus, pour
chaque garde neuve, un cas sain, des artefacts (R5) et une mutation : réglage de l'enveloppe de Carbon lu par l'analyseur de la
commande épinglée, déclaration exactement `["bash", enveloppe]`, pire cas sans troncature sous 6 USD (plafond nécessaire dit
sinon), relais Gemini v2 de Carbon, sonde de Carbon du jour, configuration v3, ligne de la course à 120 USD, clé Minuit, courses
closes. Relais et orchestrateur simulés (sauf l'essai du vrai noyau, moteur simulé), aucun appel réel, aucune clé.

Texte des essais v6 :

Essais du lanceur v6 (additif v2f : Carbon à provision de pensée 28 672 et sortie 32 768, sortie retenue au pire ≥ 24 500,
délai 1 620 s avec requêtes de 60 s) — les essais v5 portés, plus la garde de la sortie retenue (saine, artefacts, mutation).

Texte des essais v5 :

Essais du lanceur v5 de la course d'auto-conception de l'organisme (tentative neuve, additif v2e) et de la garde de crédit
v5 — relais et orchestrateur **simulés** pour le lanceur, aucun appel réel, aucun réseau hors de la boucle locale, aucune clé.
Chaque garde est essayée sur un cas sain et sur un artefact (R5).

(v5) Les essais du lanceur v4 (`tests/test_lancer_course_auto_conception_v4.py`) portés au v5 : pièce de départ avec son mot
    de reprise (`tentative_neuve`), lignes de GO neuves, périmètre de la course qui dit « tentative neuve », additif v2e qui
    cite les additifs v2c et v2d, rapport d'épreuve v5, commande de Carbon réglée, rapport de sonde d'Astra du jour ; puis, pour
    chaque garde neuve, un cas sain, des artefacts et une mutation : options de Carbon (absentes, autres, abrégées, en double,
    durée au-delà du délai fixe de l'orchestrateur) et pire cas sous le plafond de session ; mot de reprise (absent, autre,
    ligne consommée, périmètre sans « tentative neuve ») ; course v4 close admise seulement avec le mot (non close, autre
    course, journal d'une autre course, v5 déjà lancée) ; sonde d'Astra du jour ; composition tenue.

Texte des essais v4 :

(a) Les essais du lanceur v3 (`tests/test_lancer_course_auto_conception_v3.py`) portés au v4 : bornes d'Argon de l'essai
    relevées à la règle neuve (2 × appels d'Argon au pire + 2 : 288 pour trois espèces, 464 avec Astra et Carbon), additif
    v2d qui cite aussi l'additif v2c, contre-lecture neuve, rapport d'épreuve v4, une seule course sur v1 à v4.
(b) Gardes neuves : borne du relais d'Argon doublée (287 et 463 refusés, 288 et 464 acceptés ; 280, la borne des commandes
    v2c, refusé) ; relais de Carbon (23 appels ou 10 lots refusés, 24 et 11 acceptés) ; verdict de l'épreuve recalculé avec la
    requalification du v4 (manques tous techniques → « non conclue », refusé comme tout verdict non « réussi » ; une
    requalification ne fabrique jamais « réussie ») ; mutations de chacune.
(c) Essai du point 3 (v3) gardé : la course jouée par le vrai noyau de l'orchestrateur épinglé, moteur simulé, chaque dossier
    d'agent sous un chemin interdit en lecture."""
import datetime as dt
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

sys.dont_write_bytecode = True
RACINE = Path(__file__).resolve().parents[1]
CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_auto_conception_v9.py"
_spec = importlib.util.spec_from_file_location("lancer_course_auto_conception_v9", CHEMIN_LANCEUR)
L = importlib.util.module_from_spec(_spec)
sys.modules["lancer_course_auto_conception_v9"] = L
_spec.loader.exec_module(L)
_spec_e = importlib.util.spec_from_file_location("epreuve_temoins_auto_conception_v9", RACINE / "scripts" / "epreuve_temoins_auto_conception_v9.py")
E = importlib.util.module_from_spec(_spec_e)
sys.modules["epreuve_temoins_auto_conception_v9"] = E
_spec_e.loader.exec_module(E)
_spec_g = importlib.util.spec_from_file_location("garde_credit_relais_v5", RACINE / "scripts" / "garde_credit_relais_v5.py")
G = importlib.util.module_from_spec(_spec_g)
_spec_g.loader.exec_module(G)

AUJOURD_HUI = dt.date(2026, 11, 18)
COMMIT_MAIN = "c" * 40
CLE = "RR_ANTHROPIC_API_KEY_MINUIT"          # v7 : la clé de la tentative (mot de Lazar), nom seul


def _matiere_v3():
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"{L.REF_MAIN}:{L.MATIERE[0]}"], capture_output=True)
    if p.returncode != 0 or hashlib.sha256(p.stdout).hexdigest() != L.MATIERE[1]:
        return None
    return p.stdout


MATIERE = _matiere_v3()
avec_matiere = pytest.mark.skipif(MATIERE is None, reason="matière v3 absente de refs/remotes/origin/main (fetch ciblé requis)")

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
    for _ in range(comp.get("repetitions", 1)):
        dernier = subprocess.run(conf["fournisseurs"][comp["executer"]]["commande"], input=b"consigne", capture_output=True)
    for _ in range(50):
        if etat["stop"]:
            break
        time.sleep(0.1)
    arrete = etat["stop"]
g = os.path.join(sortie, "generation-1")
os.makedirs(g)
cons = [{"fournisseur": f, "role": r, "cout_usd": c, "etape": "x"} for f, r, c in comp["couts"]]
json.dump({"consommations": cons}, open(os.path.join(g, "consommations.json"), "w"))
json.dump({"etapes": {"proposition": "jouee", "passe_tableau": "retiree"}, "noeud": None, "arret": None,
           "budget": {"cumul_usd": sum(c for _, _, c in comp["couts"])}, "sessions": {"base": comp.get("sessions")}},
          open(os.path.join(g, "manifeste-fin.json"), "w"))
if comp.get("capter"):
    json.dump({"code": dernier.returncode, "stdout": dernier.stdout.decode("utf-8", "replace")},
              open(os.path.join(sortie, "capte.json"), "w"))
if comp.get("transcription"):
    t = os.path.join(os.environ["HOME"], ".claude", "projects", "essai")
    os.makedirs(t)
    open(os.path.join(t, "session.jsonl"), "w").write("{}\n")
json.dump({"f1": {}, "f2": {}}, open(os.path.join(g, "fiches.json"), "w"))
json.dump(sorted(os.environ), open(os.path.join(sortie, "env-noms.json"), "w"))
json.dump({"cases": [c[0] for c in conf["cases"]], "proposeurs": [p["etiquette"] for p in conf["proposeurs"]],
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

COUTS_SAINS = [("claude", "prop-opus", 2.0), ("claude", "prop-fable", 5.0), ("claude", "aiguilleur", 3.0),
               ("claude", "juge-opus", 3.0), ("argon", "prop-argon", 4.0), ("argon", "juge-argon", 3.0)]


def sceller(chemin: Path) -> None:
    Path(str(chemin) + ".sha256").write_text(f"{hashlib.sha256(chemin.read_bytes()).hexdigest()}  {chemin.name}\n", encoding="utf-8")


def ecrire_scelle(chemin: Path, contenu) -> Path:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    Path(str(chemin) + ".sha256").unlink(missing_ok=True)
    chemin.write_text(contenu if isinstance(contenu, str) else json.dumps(contenu, ensure_ascii=False, indent=1), encoding="utf-8")
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


FIXE = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
MODELES_CLAUDE = L.modeles_claude_de_la_configuration(FIXE)
CONTEXTE: dict = {}
PID_CLAUDE, PID_KIMI, PID_ARGON, PID_ASTRA, PID_CARBON = 424242, 424243, 424244, 424245, 424246


def serveur(etat: dict) -> ThreadingHTTPServer:
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


def porte_commande(depot: Path, url: str, modeles: list, plafond="150") -> dict:
    return {"type": "commande", "delai_s": 10,
            "commande": [sys.executable, "-I", "-B", str(depot / L.PIECES["porte_plafond"][0]), "--url", url, "--modeles-permis",
                         ",".join(modeles), "--plafond-ligne", plafond]}


def declaration(depot: Path, **modifs) -> dict:
    url = CONTEXTE["url_claude"]
    d = {"version": "essai", "fournisseurs": {
        "claude": {"type": "claude_sdk", "url_relais": url, "nom_cle": CLE, "porte_plafond": porte_commande(depot, url, MODELES_CLAUDE),
                   "pid_relais": PID_CLAUDE},
        "argon": {"type": "commande_externe", "commande": ["bash", str(depot / L.PIECES["enveloppe_argon_sans_troncature"][0])],
                  "nom_cle": "CLE_ESSAI_A", "porte_plafond": {"type": "environnement"}, "pid_relais": PID_ARGON,
                  "url_etat_relais": "http://127.0.0.1:8788"}}}
    d["fournisseurs"].update(modifs)
    return d


def piece_de_depart(**modifs) -> dict:
    d = {"version": "essai", "par": "mère", "go_course": "GO-2026-11-18-30", "go_epreuve": "GO-2026-11-18-31",
         "variable_cle_claude": CLE, "credit_declare_cle_claude_usd": 300.0, "reserve_cle_kimi_usd": 15.0,
         "cle_claude_mot_de_lazar": "« Clé Minuit (Recommandé) » (essai)",
         "commandes_epinglees": {}, "reserves_cle_claude": [{"montant_usd": 9.0, "pour": "a"}, {"montant_usd": 9.0, "pour": "b"}],
         "especes_optionnelles": {},
         # v5 : mot de reprise de la tentative neuve (la ligne de la course), course close citée
         "tentative_neuve": {"course_close": L.COURSE_CLOSE_CITEE, "mot_de_reprise": "GO-2026-11-18-30"}}   # v7 : la v6 close
    d.update(modifs)
    return d


def releve(**cles) -> dict:
    base = {CLE: {"credit_usd": 1000.0, "reste_usd": 900.0, "source": "essai"},
            "CLE_ESSAI_A": {"credit_usd": 1000.0, "reste_usd": 800.0, "source": "essai"}}
    base.update(cles)
    return {"releve_utc": "2026-11-18T07:00:00Z", "cles": base}


def contre_lecture(additif_sha: str, lanceur_sha: str, verdict="Scellable.", suite="") -> str:
    return (f"# Contre-lecture d'essai, par le modèle K\n\nAdditif v2c : {additif_sha}\nLanceur : {lanceur_sha}\n\n"
            f"## Verdict\n\n**{verdict}**\n" + suite)


def additif(prereg_sha: str, epreuve_sha: str = L.PIECES["epreuve_temoins"][1], suite="", v2c: str = L.ADDITIF_V2C[1],
            v2d: str = L.ADDITIF_V2D[1], v2e: str = L.ADDITIF_V2E[1], v2f: str = L.ADDITIF_V2F[1],
            configuration: str = L.PIECES["configuration"][1], enveloppe: str = L.PIECES["enveloppe_carbon"][1],
            commande: str = L.PIECES["commande_argon"][1], sonde: str = L.PIECES["sonde_carbon"][1], v2g: str = L.ADDITIF_V2G[1],
            enveloppe_argon: str = L.PIECES["enveloppe_argon_sans_troncature"][1], v2h: str = L.ADDITIF_V2H[1],
            conservation: str = L.PIECES["enveloppe_conservation"][1]) -> str:
    return (f"# Additif d'essai (v2g)\n\nPréenregistrement : {prereg_sha}\nProgramme d'épreuve v7 : {epreuve_sha}\n"
            f"Additif v2c : {v2c}\nAdditif v2d : {v2d}\nAdditif v2e : {v2e}\nAdditif v2f : {v2f}\nConfiguration v3 : {configuration}\n"
            f"Enveloppe : {enveloppe}\nCommande d'Argon : {commande}\nSonde : {sonde}\nAdditif v2g : {v2g}\n"
            f"Enveloppe d'Argon : {enveloppe_argon}\nAdditif v2h : {v2h}\nEnveloppe de conservation : {conservation}\n"
            "Rien d'autre ne change.\n" + suite)


def registre(plafond_c="150 USD", plafond_e="5 USD", perimetre_c="course d'auto-conception de l'organisme d'idéation, tentative neuve",
             perimetre_e="épreuve des témoins du juge (auto-conception)", suite="") -> str:
    return ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | réf. |\n|---|---|---|---|---|---|---|---|\n"
            f"| GO-2026-11-18-30 | 2026-11-18 | calcul | {perimetre_c} | {plafond_c} | 2026-11-30 | Lazar | R-1 |\n"
            f"| GO-2026-11-18-31 | 2026-11-18 | calcul | {perimetre_e} | {plafond_e} | 2026-11-30 | Lazar | R-2 |\n" + suite)


def releve_prix(**modifs) -> dict:
    prix = {"espece_claude_1": {"entree": 4.0, "sortie": 20.0}, "espece_claude_2": {"entree": 10.0, "sortie": 50.0}}
    prix.update(modifs)
    return {"releve_utc": "2026-11-18T06:55:00Z", "source": "essai : barème du relais", "prix": prix}


def bruts_parfaits() -> tuple:
    temoins = {t["id"]: t for t in json.loads((RACINE / L.PIECES["temoins"][0]).read_text())["temoins"]}
    items = FIXE["items_juge"]
    verdicts = {}
    for j in FIXE["juges"]:
        verdicts[j["etiquette"]] = {}
        for tid, t in temoins.items():
            its = E.verite(t, items)
            verdicts[j["etiquette"]][tid] = {"items": its, "notable": all(its.values()), "x": sum(its.values()) / len(items)}
    return verdicts, {tid: "niveau_methode" for tid in temoins}


def epreuve(lanceur_sha, commit_orch, **modifs) -> dict:
    v, c = bruts_parfaits()
    d = {"version": E.VERSION, "moteur": "reel", "verdict": "réussie", "horodatage_utc": "2026-11-18T07:30:00+00:00",
         "verdicts": v, "classes": c, "motif_arret": None, "version_servie_changee": [],
         "go": {"id": "GO-2026-11-18-31"}, "cout_usd": 1.0,
         "empreintes": {"temoins": L.PIECES["temoins"][1], "consigne_juge": L.PIECES["consigne_juge"][1],
                        "consigne_aiguilleur": L.PIECES["consigne_aiguilleur"][1], "programme": L.PIECES["epreuve_temoins"][1],
                        "lanceur": lanceur_sha, "orchestrateur_commit": commit_orch},
         "juges": [[j["etiquette"], j["modele"]] for j in FIXE["juges"]],
         "aiguilleur": [FIXE["aiguilleur"]["etiquette"], FIXE["aiguilleur"]["modele"]]}
    d.update(modifs)
    return d


@pytest.fixture
def monde(tmp_path):
    if MATIERE is None:
        pytest.skip("matière v3 absente")
    depot = tmp_path / "depot"
    for rel, _ in L.PIECES.values():
        (depot / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / rel, depot / rel)
    prereg = depot / L.PREREG
    prereg.parent.mkdir(parents=True, exist_ok=True)
    prereg.write_text("# préenregistrement d'essai\n", encoding="utf-8")
    sceller(prereg)
    prereg_sha = L.sha256_fichier(prereg)
    etat_claude = {"plafond_usd": 150.0, "depense_usd": 0.0, "appels": 0, "modeles_permis": list(MODELES_CLAUDE)}
    etat_kimi = {"plafond_usd": 6.0, "depense_usd": 0.0, "appels": 0, "modeles_permis": ["kimi-k3.1-pro"]}
    etat_argon = {"appels": 0, "max_appels": 600, "variable_cle_encore_presente": False}   # v4 : ≥ 2 × 275 + 2 = 552 (six espèces, Kimi comprise)
    s_claude, s_kimi = serveur(etat_claude), serveur(etat_kimi)
    CONTEXTE.update(url_claude=f"http://127.0.0.1:{s_claude.server_address[1]}", url_kimi=f"http://127.0.0.1:{s_kimi.server_address[1]}")
    progs = tmp_path / "progs"
    progs.mkdir()
    for n in ("relais_reel.py", "relais_kimi_v4.py", "relais_gemini_v2.py", "relais_gemini_v4.py"):
        (progs / n).write_text(f"# {n} factice\n", encoding="utf-8")
    cmdlines = {PID_CLAUDE: [sys.executable, "-I", "-B", str(progs / "relais_reel.py"), "--variable-cle", CLE,
                             "--port", CONTEXTE["url_claude"].rsplit(":", 1)[1], "--plafond-usd", "150", "--modeles-permis",
                             ",".join(MODELES_CLAUDE)],
                PID_KIMI: [sys.executable, "-I", "-B", str(progs / "relais_kimi_v4.py"), "--variable-cle", "CLE_ESSAI_K",
                           "--port", CONTEXTE["url_kimi"].rsplit(":", 1)[1], "--plafond-usd", "6"],
                PID_ARGON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v2.py"), "--port", "8788", "--max-appels", "600",
                            "--modele", "gemini-4-argon", "--variable-cle", "CLE_ESSAI_A"],
                PID_ASTRA: [sys.executable, "-I", "-B", str(progs / "relais_kimi_v4.py"), "--amont", "https://api.openai.com",
                            "--variable-cle", "CLE_ESSAI_S", "--port", "8790", "--modeles-permis", "modele-essai-astra",
                            "--plafond-usd", "20"],
                PID_CARBON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v2.py"), "--variable-cle", "CLE_ESSAI_C",
                             "--port", "8792", "--modele", "modele-essai-carbon", "--max-appels", "60"]}   # v7 : relais Gemini v2
    o, commit, empreintes = faux_orchestrateur(tmp_path)
    lanceur_sha = L.sha256_fichier(CHEMIN_LANCEUR)
    chemin_additif = ecrire_scelle(depot / L.ADDITIF, additif(prereg_sha))
    additif_sha = L.sha256_fichier(chemin_additif)
    ecrire_scelle(depot / L.CONTRE_LECTURE, contre_lecture(additif_sha, lanceur_sha))
    ecrire_scelle(depot / L.PIECE_DE_DEPART, piece_de_depart())
    ecrire_scelle(depot / L.DECLARATION_RELAIS, declaration(depot))
    ecrire_scelle(depot / L.RELEVE_CREDITS, releve())
    ecrire_scelle(depot / L.RELEVE_PRIX, releve_prix())
    ecrire_scelle(depot / L.EPREUVE_REELLE, epreuve(lanceur_sha, commit))
    fichiers_main = {"registres/go.md": registre().encode("utf-8"), L.MATIERE[0]: MATIERE}
    etat_astra = {"appels": 0, "max_appels": 50, "plafond_usd": 20.0}
    etat_carbon = {"appels": 0, "max_appels": 60, "variable_cle_encore_presente": False}   # v7 : relais Gemini v2
    etats = {"http://127.0.0.1:8788": etat_argon, "http://127.0.0.1:8790": etat_astra, "http://127.0.0.1:8792": etat_carbon}
    r = L.Reglages(depot=depot, orchestrateurs=(o,), commit_orchestrateur=commit, empreintes_orchestrateur=empreintes,
                   pieces=dict(L.PIECES), prereg=(prereg, prereg_sha), additif=(chemin_additif, additif_sha),
                   contre_lecture=depot / L.CONTRE_LECTURE,
                   piece_de_depart=depot / L.PIECE_DE_DEPART, epreuve_reelle=depot / L.EPREUVE_REELLE,
                   declaration=depot / L.DECLARATION_RELAIS, releve=depot / L.RELEVE_CREDITS,
                   procedure_relais=depot / L.PROCEDURE_RELAIS, releve_prix=depot / L.RELEVE_PRIX, dossier_runs=depot / "runs",
                   dossier_sorties=tmp_path / "sorties", depot_attendu_par_l_enveloppe=depot, python=sys.executable,
                   lanceur=CHEMIN_LANCEUR, moteur="reel",
                   environnement={"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", CLE: "valeur-secrete-essai-1",
                                  "RR_ANTHROPIC_API_KEY_RIGAUD": "valeur-secrete-essai-2"},
                   aujourd_hui=AUJOURD_HUI, horodatage=lambda: "Wed Nov 18 07:00:00 UTC 2026",
                   programmes_relais={n: (p, hashlib.sha256((progs / p).read_bytes()).hexdigest()) for n, p in
                                      (("claude", "relais_reel.py"), ("kimi", "relais_kimi_v4.py"), ("argon", "relais_gemini_v2.py"),
                                       ("astra", "relais_kimi_v4.py"), ("carbon", "relais_gemini_v2.py"))},
                   sorties_autres_versions=(tmp_path / "sorties-v1-absentes",),
                   lire_cmdline=lambda pid: list(cmdlines[pid]),
                   lire_main=lambda chemin: (fichiers_main[chemin], COMMIT_MAIN),
                   lire_etat_relais=lambda url: dict(etats[url.rstrip("/")]))
    yield {"r": r, "tmp": tmp_path, "depot": depot, "orch": o, "lanceur_sha": lanceur_sha, "etat_claude": etat_claude,
           "etat_argon": etat_argon, "etat_astra": etat_astra, "etat_carbon": etat_carbon, "cmdlines": cmdlines, "main": fichiers_main, "commit": commit, "prereg_sha": prereg_sha,
           "additif_sha": additif_sha}
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
    ep = m["depot"] / L.EPREUVE_REELLE
    ecrire_scelle(ep, epreuve(m["lanceur_sha"], commit))


def _ecrire(monde, rel, objet):
    ecrire_scelle(monde["depot"] / rel, objet)


# --- bout en bout ------------------------------------------------------------------------------------------------------------


def test_bout_en_bout_sain(monde):
    r = monde["r"]
    assert lancer(r) == 0
    run = un_run(r)
    for nom in ("manifeste-lanceur-depart.json", "manifeste-lanceur-fin.json", "acte-de-gel.md", "configuration-orchestrateur.json",
                "lots-matiere.json", "registre-go-derive.md"):
        assert L.scelle(run / nom), nom
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert dep["matiere"]["sha256"] == L.MATIERE[1] and dep["matiere"]["commit"] == COMMIT_MAIN
    assert dep["lots"]["nombre"] == 11 and dep["go"]["plafond_lu"] == L.PLAFOND_ARRET_USD
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon"]
    assert dep["cle_par_espece"]["prop-opus"] == CLE and dep["cle_par_role_interne"]["juge-argon"] == "CLE_ESSAI_A"
    assert dep["registre_go_derive"]["commit_source"] == COMMIT_MAIN  # constat 5
    assert COMMIT_MAIN in (run / "registre-go-derive.md").read_text()
    assert dep["procedure_relais_persistants"]["relais_vivants"]["argon"]["etat"]["appels"] == 0  # constat 4
    assert dep["porte_a_blanc"]["claude"]["code"] == 0
    assert dep["epreuve_reelle_des_temoins"]["verdict"] == "réussie"
    assert fin["cout_reel"]["par_relais_usd"] == {"claude": 13.0, "argon": 7.0}
    assert fin["ecart_au_devis_v1"]["devis_estimation_usd"] == pytest.approx(22.3331)
    vu = json.loads((Path(dep["sortie"]) / "vu.json").read_text())
    assert len(vu["cases"]) == 11 and all(L.MATIERE[1] in c for c in vu["cases"])
    noms = json.loads((Path(dep["sortie"]) / "env-noms.json").read_text())
    assert CLE not in noms and "GO_ID" in noms
    for p in list(run.rglob("*")) + list(Path(dep["sortie"]).parent.rglob("*")):
        if p.is_file():
            assert "valeur-secrete-essai" not in p.read_text(errors="replace"), p


def test_course_deja_lancee_refusee(monde):
    assert lancer(monde["r"]) == 0
    assert lancer(monde["r"]) == 2


def test_une_tentative_refusee_avant_le_depart_ne_bloque_pas_la_suivante(monde):
    """Constat 1 : porte à blanc refusée (relais déjà employé) → aucun dossier de sortie ; la tentative suivante part."""
    monde["etat_claude"]["appels"] = 3
    assert lancer(monde["r"]) == 2
    assert not monde["r"].dossier_sorties.exists() or not any(monde["r"].dossier_sorties.glob("*/course.stdout.txt"))
    monde["etat_claude"]["appels"] = 0
    assert lancer(monde["r"]) == 0


def test_journal_de_course_hors_depot_bloque(monde):
    j = monde["r"].dossier_sorties / "20261118-000000-course-auto-conception-v1" / "course.stdout.txt"
    j.parent.mkdir(parents=True)
    j.write_text("", encoding="utf-8")
    assert lancer(monde["r"]) == 2


# --- pièce de départ, clé Claude ------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("modif", [
    {"variable_cle_claude": "RR_ANTHROPIC_API_KEY_RIGAUD"},
    {"variable_cle_claude": "À REMPLIR"},
    {"variable_cle_claude": "AUTRE_CLE"},
    {"go_epreuve": "GO-2026-11-18-30"},
    {"credit_declare_cle_claude_usd": 0},
    {"reserve_cle_kimi_usd": None},
    {"par": "session"},
    {"commandes_epinglees": {"astra": {"empreintes": ["x"], "epreuve": "R-1"}}},
])
def test_piece_de_depart_artefacts_refuses(monde, modif):
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(**modif))
    assert lancer(monde["r"]) == 2
    assert not monde["r"].dossier_runs.exists()


def test_piece_de_depart_absente_ou_non_scellee(monde):
    p = monde["depot"] / L.PIECE_DE_DEPART
    Path(str(p) + ".sha256").unlink()
    assert lancer(monde["r"]) == 2
    p.unlink()
    assert lancer(monde["r"]) == 2


def test_variable_de_cle_absente_arret_au_depart(monde):
    monde["r"].environnement.pop(CLE)
    assert lancer(monde["r"]) == 2


def test_relais_claude_sur_une_autre_cle_refuse(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_RIGAUD"
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert lancer(monde["r"]) == 2


def test_cle_claude_sur_un_autre_relais_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_AUTRE"
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert lancer(monde["r"]) == 2


# --- GO, registre, matière --------------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("texte", [registre(plafond_c="120 USD"), registre(perimetre_c="course d'affinage"),
                                   registre(suite="| GO-2026-11-18-40 | 2026-11-18 | révocation | GO-2026-11-18-30 | — | — | Lazar | R-3 |\n"),
                                   registre().replace("| Lazar | R-1", "| mère | R-1")])
def test_go_artefacts_refuses(monde, texte):
    monde["main"]["registres/go.md"] = texte.encode("utf-8")
    assert lancer(monde["r"]) == 2


def test_matiere_d_une_autre_empreinte_refusee(monde):
    monde["main"][L.MATIERE[0]] = MATIERE + b"\n"
    assert lancer(monde["r"]) == 2


@avec_matiere
def test_decoupage_v3_couverture_et_lots():
    lots = L.decouper_matiere(MATIERE, L.MATIERE[1])
    assert [l["nom"] for l in lots["lots"]][:8] == [f"famille « {f} »" for f in ("exploration", "originalité", "épreuve", "jugement",
                                                                                 "mémoire", "sélection", "coût", "auto-conception")]
    assert len(lots["lots"]) == 11 and lots["couverture"]["lignes_non_vides_toutes_servies_une_fois"]
    assert lots["commun"]["regroupements_indexes"] >= 100
    servi = lots["commun"]["texte"] + "".join(l["texte"] for l in lots["lots"])
    for ligne in MATIERE.decode("utf-8").split("\n"):
        if ligne.strip():
            assert L.expurger(ligne)[0] in servi  # v2 : lignes servies après expurgation (constat 9)
    # rejouable : même entrée, même sortie
    assert json.dumps(L.decouper_matiere(MATIERE, L.MATIERE[1]), sort_keys=True) == json.dumps(lots, sort_keys=True)


def test_decoupage_artefacts():
    base = ("# T\n\n## 0. Lire\nx\n## 1. Familles\n### Famille « a »\n**a n° 1 — A**\n- m Kimi\n## 2. Machines\ny\n"
            "## 3. Hors\nz\n## 4. Fait\nw\n## 5. Questions\nq\n")
    lots = L.decouper_matiere(base.encode(), "0" * 64)
    assert len(lots["lots"]) == 3 and "[nom retiré]" in lots["lots"][0]["texte"] and lots["lots"][0]["masques"] == 1
    with pytest.raises(L.Refus):
        L.decouper_matiere(base.replace("## 2. Machines", "## 2b Machines").encode(), "0" * 64)
    with pytest.raises(L.Refus):
        L.decouper_matiere((base + "## 12. Autre\nk\n").encode(), "0" * 64)
    with pytest.raises(L.Refus):
        L.decouper_matiere(base.replace("### Famille « a »", "### Groupe a").encode(), "0" * 64)
    with pytest.raises(L.Refus):
        L.decouper_matiere((base + "## 7. Long\n" + "x" * 130_000 + "\n").encode(), "0" * 64)


# --- épreuve réelle des témoins ----------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("modif", [{"verdict": "échouée"}, {"verdict": "non conclue"}, {"moteur": "hors_ligne"},
                                   {"horodatage_utc": "2026-11-17T07:00:00+00:00"}, {"go": {"id": "GO-2026-11-18-30"}},
                                   {"juges": [["juge-opus", "claude-opus-5-5"]]}, {"aiguilleur": ["aiguilleur", "autre"]}])
def test_epreuve_reelle_artefacts_refuses(monde, modif):
    _ecrire(monde, L.EPREUVE_REELLE, epreuve(monde["lanceur_sha"], monde["commit"], **modif))
    assert lancer(monde["r"]) == 2


@pytest.mark.parametrize("cle", ["temoins", "consigne_juge", "programme", "lanceur", "orchestrateur_commit"])
def test_epreuve_reelle_autres_pieces_refusee(monde, cle):
    e = epreuve(monde["lanceur_sha"], monde["commit"])
    e["empreintes"][cle] = "0" * 64
    _ecrire(monde, L.EPREUVE_REELLE, e)
    assert lancer(monde["r"]) == 2


def test_epreuve_reelle_absente_refusee(monde):
    (monde["depot"] / L.EPREUVE_REELLE).unlink()
    assert lancer(monde["r"]) == 2


# --- portes et relais (constats 2 et 4) ---------------------------------------------------------------------------------------------


@pytest.mark.parametrize("modif", [
    lambda c: c.__setitem__(c.index("--modeles-permis") + 1, "claude-opus-5-5"),
    lambda c: c.__setitem__(c.index("--plafond-ligne") + 1, "120"),
    lambda c: c.__setitem__(c.index("--url") + 1, "http://127.0.0.1:1"),
])
def test_commande_de_porte_recoupee_avec_la_configuration(monde, modif):
    d = declaration(monde["depot"])
    modif(d["fournisseurs"]["claude"]["porte_plafond"]["commande"])
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert lancer(monde["r"]) == 2


def test_relais_argon_controle(monde):
    monde["etat_argon"]["appels"] = 1
    assert lancer(monde["r"]) == 2
    monde["etat_argon"].update(appels=0, variable_cle_encore_presente=True)
    assert lancer(monde["r"]) == 2
    monde["etat_argon"]["variable_cle_encore_presente"] = False
    c = monde["cmdlines"][PID_ARGON]
    c[c.index("--max-appels") + 1] = "50"
    monde["etat_argon"]["max_appels"] = 50
    assert lancer(monde["r"]) == 2
    c[c.index("--max-appels") + 1] = "600"
    monde["etat_argon"]["max_appels"] = 600
    c[c.index("--port") + 1] = "8791"
    assert lancer(monde["r"]) == 2
    c[c.index("--port") + 1] = "8788"
    assert lancer(monde["r"]) == 0


def test_relais_claude_plafond_autre_refuse(monde):
    c = monde["cmdlines"][PID_CLAUDE]
    c[c.index("--plafond-usd") + 1] = "120"
    assert lancer(monde["r"]) == 2


def test_relais_claude_autre_variable_refuse(monde):
    c = monde["cmdlines"][PID_CLAUDE]
    c[c.index("--variable-cle") + 1] = "RR_ANTHROPIC_API_KEY_RIGAUD"     # v7 : la clé Claude est Minuit
    assert lancer(monde["r"]) == 2


def test_espece_kimi_declaree_active_et_reserve(monde):
    kimi = {"type": "kimi_protocole", "url_relais": CONTEXTE["url_kimi"], "modele": "kimi-k3.1-pro", "prix_entree": 2.0,
            "prix_sortie": 10.0, "max_sortie_jetons": 16000, "sortie_min_jetons": 1000, "delai_s": 1800, "nom_cle": "CLE_ESSAI_K",
            "pid_relais": PID_KIMI, "porte_plafond": porte_commande(monde["depot"], CONTEXTE["url_kimi"], ["kimi-k3.1-pro"], "6")}
    _ecrire(monde, L.DECLARATION_RELAIS, declaration(monde["depot"], kimi=kimi))
    _ecrire(monde, L.RELEVE_CREDITS, releve(CLE_ESSAI_K={"credit_usd": 40.0, "reste_usd": 38.0, "source": "essai"}))
    assert lancer(monde["r"]) == 2  # constat 1 : sans mot écrit de la mère, Kimi n'est pas déclaré
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(especes_optionnelles={"kimi": {"declaree": True, "risque_accepte": True,
                                                                                     "sonde_du_jour": "R-essai"}}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-kimi" in dep["especes_actives"] and dep["parts_au_pire"]["kimi"]["part_au_pire_usd"] < 10


def test_kimi_reserve_trop_haute_alerte_code_3(monde):
    kimi = {"type": "kimi_protocole", "url_relais": CONTEXTE["url_kimi"], "modele": "kimi-k3.1-pro", "prix_entree": 2.0,
            "prix_sortie": 10.0, "max_sortie_jetons": 16000, "sortie_min_jetons": 1000, "delai_s": 1800, "nom_cle": "CLE_ESSAI_K",
            "pid_relais": PID_KIMI, "porte_plafond": porte_commande(monde["depot"], CONTEXTE["url_kimi"], ["kimi-k3.1-pro"], "6")}
    _ecrire(monde, L.DECLARATION_RELAIS, declaration(monde["depot"], kimi=kimi))
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(especes_optionnelles={"kimi": {"declaree": True, "risque_accepte": True,
                                                                                     "sonde_du_jour": "R-essai"}}))
    _ecrire(monde, L.RELEVE_CREDITS, releve(CLE_ESSAI_K={"credit_usd": 32.25, "reste_usd": 20.0, "source": "essai"}))
    assert lancer(monde["r"]) == 3


def _astra(monde, ligne=None):
    script = monde["tmp"] / "astra.py"
    ligne = ligne or {"texte": "ok", "cout_usd": 0.01}
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps(" + repr(ligne) + "))\n", encoding="utf-8")
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script), "--url-relais", "http://127.0.0.1:8790"],
             "modele_propose": "modele-essai-astra", "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"},
             "pid_relais": PID_ASTRA, "url_etat_relais": "http://127.0.0.1:8790"}
    _ecrire(monde, L.DECLARATION_RELAIS, declaration(monde["depot"], astra=astra))
    _ecrire(monde, L.RELEVE_CREDITS, dict(releve(CLE_ESSAI_S={"non_lisible": True, "motif": "illisible"}),
                                          dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S"]}))
    return script


SONDE_REL = f"{L.COURSE_V3}/sonde-astra-commune-essai-v1.json"


def sonde_astra(monde, sha_commande, **modifs) -> str:
    """v5 : rapport de sonde d'Astra du jour, au format de `scripts/sonde_astra_courses_v1.py`, scellé au dépôt d'essai."""
    o = {"version": "sonde_astra_courses_v1", "ok": True, "appel_envoye": True, "echec_de_configuration": False,
         "jour": AUJOURD_HUI.isoformat(), "cout_usd": 0.00041, "commande": {"chemin": "/x/commande_astra_v1.py", "sha256": sha_commande}}
    o.update(modifs)
    _ecrire(monde, SONDE_REL, o)
    return SONDE_REL


def _piece_astra(monde, script, **opt):
    o = {"declaree": True, "risque_accepte": True, "sonde_du_jour": "R-essai",
         "sonde_du_jour_rapport": sonde_astra(monde, L.sha256_fichier(script))}
    o.update(opt)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(
        commandes_epinglees={"astra": {"empreintes": [L.sha256_fichier(script)], "epreuve": "R-essai"}},
        especes_optionnelles={"astra": o}))


def test_astra_refusee_sans_commande_epinglee_ni_mot_et_active_avec(monde):
    script = _astra(monde)
    assert lancer(monde["r"]) == 2                     # ni mot de la mère, ni commande épinglée
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(commandes_epinglees={"astra": {"empreintes": [L.sha256_fichier(script)],
                                                                                    "epreuve": "R-essai"}}))
    assert lancer(monde["r"]) == 2                     # commande épinglée, mais pas de mot de la mère
    _piece_astra(monde, script, risque_accepte=False)
    assert lancer(monde["r"]) == 2                     # mot sans risque accepté
    _piece_astra(monde, script)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-astra" in dep["especes_actives"] and dep["procedure_relais_persistants"]["relais_vivants"]["astra"]["port"] == "8790"


def test_relais_astra_controle(monde):
    script = _astra(monde)
    _piece_astra(monde, script)
    monde["etat_astra"]["appels"] = 2
    assert lancer(monde["r"]) == 2
    monde["etat_astra"]["appels"] = 0
    c = monde["cmdlines"][PID_ASTRA]
    c[c.index("--amont") + 1] = "https://api.moonshot.ai"
    assert lancer(monde["r"]) == 2
    c[c.index("--amont") + 1] = "https://api.openai.com"
    c[c.index("--modeles-permis") + 1] = "autre"
    assert lancer(monde["r"]) == 2
    c[c.index("--modeles-permis") + 1] = "modele-essai-astra"
    assert lancer(monde["r"]) == 0



# --- crédits ------------------------------------------------------------------------------------------------------------------------


def test_cle_claude_non_lisible_comptee_au_credit_declare_net_des_reserves(monde):
    _ecrire(monde, L.RELEVE_CREDITS, releve(**{CLE: {"non_lisible": True, "depense_anterieure_usd": 10.0}}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["releve_credits_avant"]["cles"][CLE]["reste_usd"] == 272.0  # 300 − 10 − 9 − 9


def test_reserves_de_la_cle_claude_retranchees_code_3(monde):
    """Constat 8 (R-3271) ; v9 (part au pire 150) : 174 déclarés, 2 dépensés, réserves 9 + 9 → 154 net > 150 : part ; 168 lus →
    150 net : alerte."""
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(credit_declare_cle_claude_usd=174.0))
    _ecrire(monde, L.RELEVE_CREDITS, releve(**{CLE: {"non_lisible": True, "depense_anterieure_usd": 2.0}}))
    assert lancer(monde["r"]) == 0
    shutil.rmtree(un_run(monde["r"]))
    shutil.rmtree(monde["r"].dossier_sorties)
    _ecrire(monde, L.RELEVE_CREDITS, releve(**{CLE: {"credit_usd": 174.0, "reste_usd": 168.0, "source": "essai"}}))
    assert lancer(monde["r"]) == 3


def test_cle_claude_sous_la_part_au_pire_alerte_code_3(monde):
    _ecrire(monde, L.RELEVE_CREDITS, releve(**{CLE: {"credit_usd": 100.0, "reste_usd": 89.0, "source": "essai"}}))
    assert lancer(monde["r"]) == 3


def test_argon_illisible_sans_dispense_refuse_avec_dispense_part(monde):
    _ecrire(monde, L.RELEVE_CREDITS, releve(CLE_ESSAI_A={"non_lisible": True, "motif": "illisible"}))
    assert lancer(monde["r"]) == 2
    _ecrire(monde, L.RELEVE_CREDITS, dict(releve(CLE_ESSAI_A={"non_lisible": True, "motif": "illisible"}),
                                          dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_A"]}))
    assert lancer(monde["r"]) == 0


def test_garde_v5_quota_seul_ne_suffit_pas_deux_fois_arrete(tmp_path):
    q = json.dumps({"texte": "", "cout_usd": 0.01, "erreur": "You exceeded your current quota, please check your plan and billing details"})
    assert G.motif_credit(q, "", 1) is None and G.soupcon_credit(q, "", 1)
    d = tmp_path / "arrets"
    G.noter(str(d), "astra", None, G.soupcon_credit(q, "", 1), 1)
    assert sorted(p.name for p in d.iterdir()) == ["soupcon-credit-astra-1.json"]
    G.noter(str(d), "astra", None, G.soupcon_credit(q, "", 1), 1)
    assert "arret-credit-astra.json" in [p.name for p in d.iterdir()]
    j = lambda e: json.dumps({"texte": "", "cout_usd": 0.01, "erreur": e})  # noqa: E731
    for e in ("HTTP 402 payment required", "insufficient_quota: check your billing details", "crédits épuisés",
              "Your prepayment credits are depleted", "credit balance is too low"):
        assert G.motif_credit(j(e), "", 1), e
    for e in ("429 RESOURCE_EXHAUSTED: rate limit per minute", "délai dépassé", "quota exceeded"):
        assert not G.motif_credit(j(e), "", 1) and not G.soupcon_credit(j(e), "", 1), e
    assert G.motif_credit(j("You exceeded your current quota; insufficient funds"), "", 1)


def test_garde_v5_premier_refus_arrete_la_course_code_5(monde):
    script = _astra(monde, {"texte": "", "cout_usd": 0.01, "erreur": "HTTP 402 payment required"})
    _piece_astra(monde, script)
    remplacer_orchestrateur(monde, executer="astra")
    assert lancer(monde["r"]) == 5
    assert L.scelle(un_run(monde["r"]) / "alerte-arret-credit.json")


def test_garde_v5_quota_une_fois_n_arrete_pas_la_course(monde):
    script = _astra(monde, {"texte": "", "cout_usd": 0.01, "erreur": "You exceeded your current quota, please check your plan and billing details"})
    _piece_astra(monde, script)
    remplacer_orchestrateur(monde, executer="astra")
    assert lancer(monde["r"]) == 0
    fin = json.loads((un_run(monde["r"]) / "manifeste-lanceur-fin.json").read_text())
    assert fin["soupcons_de_credit"] == ["soupcon-credit-astra-1.json"] and fin["arret_au_premier_refus_pour_credit"] == []


# --- contre-lecture, préenregistrement, configuration, orchestrateur -------------------------------------------------------------


@pytest.mark.parametrize("verdict,suite", [("Scellable après corrections.", ""), ("Scellable", ""), ("Non scellable.", ""),
                                           ("Scellable.", "\nJe n'ai pas relu le lanceur.\n")])
def test_contre_lecture_stricte(monde, verdict, suite):
    _ecrire(monde, L.CONTRE_LECTURE, contre_lecture(monde["additif_sha"], monde["lanceur_sha"], verdict, suite))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_qui_ne_cite_pas_le_lanceur_refusee(monde):
    _ecrire(monde, L.CONTRE_LECTURE, contre_lecture(monde["additif_sha"], "0" * 64))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_sans_modele_k_refusee(monde):
    _ecrire(monde, L.CONTRE_LECTURE, contre_lecture(monde["additif_sha"], monde["lanceur_sha"]).replace("modèle K", "modèle J"))
    assert lancer(monde["r"]) == 2


def test_preenregistrement_autre_empreinte_refuse(monde):
    p = monde["r"].prereg[0]
    p.write_text("modifié\n", encoding="utf-8")
    sceller(p)
    assert lancer(monde["r"]) == 2


def test_empreinte_du_preenregistrement_non_posee_refusee(monde):
    monde["r"].prereg = (monde["r"].prereg[0], "À REMPLIR")
    assert lancer(monde["r"]) == 2


def test_piece_modifiee_refusee(monde):
    p = monde["depot"] / L.PIECES["temoins"][0]
    p.write_text(p.read_text() + " ", encoding="utf-8")
    assert lancer(monde["r"]) == 2


def test_configuration_fixe_sain_et_artefacts():
    L.garde_configuration_fixe(FIXE)
    for modif in (lambda f: f["budget"].__setitem__("plafond_usd", 120.0),
                  lambda f: f["budget"]["etapes"][3].__setitem__("plafond_relais_usd", 50.0),
                  lambda f: f["budget"]["etapes"][0].__setitem__("plafond_relais_usd", 110.0),
                  lambda f: f.__setitem__("etage_tests_de_mort", {"nombre": 1}),
                  lambda f: f.__setitem__("generations", 2),
                  lambda f: f.__setitem__("etiquettes_interdites_fixes", ["Opus"]),
                  lambda f: f["especes"][0].__setitem__("cle", "RR_ANTHROPIC_API_KEY_MINUIT")):
        f = json.loads(json.dumps(FIXE))
        modif(f)
        with pytest.raises(L.Refus):
            L.garde_configuration_fixe(f)


def test_verification_orchestrateur_montant_autre_refuse(monde):
    remplacer_orchestrateur(monde, montant=120.0)
    assert lancer(monde["r"]) == 2


def test_cumul_au_dela_du_plafond_code_4(monde):
    remplacer_orchestrateur(monde, couts=[("claude", "prop-opus", 75.0), ("argon", "juge-argon", 76.0)])   # v9 : > 150
    assert lancer(monde["r"]) == 4


def test_orchestrateur_modifie_refuse(monde):
    (monde["orch"] / "pole" / "en_trop.py").write_text("", encoding="utf-8")
    assert lancer(monde["r"]) == 2


def test_arguments_refuses():
    assert L.principal(["--autre"]) == 2


# --- v2 : constats de la contre-lecture de la v1 ---------------------------------------------------------------------------------


@pytest.mark.parametrize("modif", [{"reserves_cle_claude": None}, {"reserves_cle_claude": [{"montant_usd": 9.0}]},
                                   {"especes_optionnelles": {"kimi": {"declaree": True}}},
                                   {"especes_optionnelles": {"autre": {"declaree": False}}}])
def test_piece_de_depart_v2_artefacts(monde, modif):
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(**modif))
    assert lancer(monde["r"]) == 2


def test_verdict_de_l_epreuve_recalcule(monde):
    """Constat 11 : un rapport « réussie » dont les verdicts bruts disent autre chose est refusé."""
    e = epreuve(monde["lanceur_sha"], monde["commit"])
    e["verdicts"]["juge-argon"]["t06"]["items"]["voisin_nomme"] = True
    _ecrire(monde, L.EPREUVE_REELLE, e)
    assert lancer(monde["r"]) == 2
    e = epreuve(monde["lanceur_sha"], monde["commit"])
    e["classes"]["t01"] = "concret"
    _ecrire(monde, L.EPREUVE_REELLE, e)
    assert lancer(monde["r"]) == 2
    e = epreuve(monde["lanceur_sha"], monde["commit"])
    del e["verdicts"]["juge-argon"]
    _ecrire(monde, L.EPREUVE_REELLE, e)
    assert lancer(monde["r"]) == 2
    e = epreuve(monde["lanceur_sha"], monde["commit"], motif_arret="plafond")
    _ecrire(monde, L.EPREUVE_REELLE, e)
    assert lancer(monde["r"]) == 2


def test_course_v1_deja_lancee_bloque_la_v2(monde):
    d = monde["r"].dossier_runs / "20261118-000000-course-auto-conception-v1"
    d.mkdir(parents=True)
    (d / "manifeste-lanceur-depart.json").write_text("{}", encoding="utf-8")
    assert lancer(monde["r"]) == 2


def test_journal_v1_hors_depot_bloque_la_v2(monde):
    j = monde["tmp"] / "sorties-v1" / "x" / "course.stdout.txt"
    j.parent.mkdir(parents=True)
    j.write_text("", encoding="utf-8")
    monde["r"].sorties_autres_versions = (monde["tmp"] / "sorties-v1",)
    assert lancer(monde["r"]) == 2


def test_expurgation_sain_et_artefacts():
    t, l = L.expurger("Décision de Lazar, session `session_01ABCdefGHI`, proposé à Lazar ; Lazar dit.")
    assert "Lazar" not in t and "session_01" not in t and len(l) == 4 and "du directeur" in t and "au directeur" in t
    assert L.expurger("rien à retirer") == ("rien à retirer", [])


@avec_matiere
def test_aucun_texte_servi_ne_porte_le_nom_ni_une_session(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    vu = json.loads((Path(dep["sortie"]) / "vu.json").read_text())
    consigne = (RACINE / L.PIECES["consigne_proposeur"][0]).read_text()
    for texte in vu["cases"] + [consigne]:
        assert not L.RESTES_INTERDITS.search(texte)
    assert dep["expurgations_des_lots"] == 3


def test_consigne_non_expurgee_refusee(monde):
    p = monde["depot"] / L.PIECES["consigne_proposeur"][0]
    p.write_text(p.read_text() + "\nDécision de Lazar.\n", encoding="utf-8")
    monde["r"].pieces = dict(L.PIECES, consigne_proposeur=(L.PIECES["consigne_proposeur"][0], L.sha256_fichier(p)))
    assert lancer(monde["r"]) == 2


# --- v7 : Carbon synchrone sans troncature, plafonds relevés, clé Minuit, courses v4 et v6 closes ---------------------------------


def _charger_module(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


L6 = _charger_module("lancer_course_auto_conception_v6_pour_essai_v7", RACINE / "scripts" / "lancer_course_auto_conception_v6.py")
L4 = _charger_module("lancer_course_auto_conception_v4_pour_essai_v7", RACINE / "scripts" / "lancer_course_auto_conception_v4.py")
SHA_EPREUVE_V6 = L6.PIECES["epreuve_temoins"][1]
IDENT_V4, IDENT_V6 = (x[0] for x in L.COURSES_CLOSES_ADMISES)
COMMANDES_MAIN = {"astra": ("docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py",
                            "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71")}


def _de_main(rel, sha):
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"refs/remotes/origin/main:{rel}"], capture_output=True)
    return p.stdout if p.returncode == 0 and hashlib.sha256(p.stdout).hexdigest() == sha else None


OCTETS = {n: _de_main(*v) for n, v in COMMANDES_MAIN.items()}
avec_commandes = pytest.mark.skipif(any(v is None for v in OCTETS.values()) or MATIERE is None,
                                    reason="commande d'Astra ou matière absente de origin/main")
GABARIT = RACINE / L.COURSE_V4 / "piece-de-depart-gabarit-auto-conception-v2i.json"   # v9
SONDE_C_REL = f"{L.COURSE_V4}/sonde-carbon-synchrone-essai-v1.json"
CLE_RIGAUD = "RR_ANTHROPIC_API_KEY_RIGAUD"
GO_COURSE_NEUVE, GO_EPREUVE_NEUVE = "GO-2026-11-19-11", "GO-2026-11-19-12"


def entree_servie(depot):
    lots = L.decouper_matiere(MATIERE, L.MATIERE[1])
    return L.plus_grande_entree((depot / L.PIECES["consigne_proposeur"][0]).read_text(encoding="utf-8"), lots)


def sonde_carbon(m, commande=None, **modifs) -> str:
    """v7 : rapport de sonde de Carbon du jour, au format de `scripts/sonde_carbon_synchrone_v1.py`, scellé au dépôt d'essai."""
    o = L.rapport_sonde_carbon_d_essai(AUJOURD_HUI, entree_servie(m["depot"]))
    o["motif"] = None
    o["commande"].update(cout_usd=1.2, pensees_jetons=20000, candidats_jetons=3400, lecture_pensees="indetermine", duree_s=310.0)
    o["commande"].update(commande or {})
    o.update(modifs)
    _ecrire(m, SONDE_C_REL, o)
    return SONDE_C_REL


def bloc_carbon(m, **modifs) -> dict:
    b = {"type": "commande_externe", "commande": ["bash", str(m["depot"] / L.PIECES["enveloppe_carbon"][0])],
         "modele_propose": "gemini-4-carbon", "nom_cle": "CLE_ESSAI_C", "pid_relais": PID_CARBON,
         "url_etat_relais": "http://127.0.0.1:8792", "porte_plafond": {"type": "environnement"}}
    b.update(modifs)
    return b


def piece_remplie(**especes) -> dict:
    """Le gabarit v2g rempli pour l'essai (lignes de l'essai, mot de reprise = ligne de la course, sondes nommées)."""
    o = json.loads(GABARIT.read_text(encoding="utf-8"))
    o.update(statut="rempli pour l'essai", go_course="GO-2026-11-18-30", go_epreuve="GO-2026-11-18-31", ecrit_le="2026-11-18T11:00:00Z")
    o["tentative_neuve"]["mot_de_reprise"] = "GO-2026-11-18-30"
    o["especes_optionnelles"]["astra"]["sonde_du_jour"] = f"{SONDE_REL} (essai)"
    o["especes_optionnelles"]["astra"]["sonde_du_jour_rapport"] = SONDE_REL
    o["especes_optionnelles"]["carbon"]["sonde_du_jour"] = f"{SONDE_C_REL} (essai)"
    o["especes_optionnelles"]["carbon"]["sonde_du_jour_rapport"] = SONDE_C_REL
    for nom, modifs in especes.items():
        o["especes_optionnelles"][nom].update(modifs)
        for k in [k for k, v in modifs.items() if v is None]:
            del o["especes_optionnelles"][nom][k]
    return o


def preparer(m, cle=CLE) -> None:
    p = m["tmp"] / Path(COMMANDES_MAIN["astra"][0]).name
    p.write_bytes(OCTETS["astra"])
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(p), "--url-relais", "http://127.0.0.1:8790",
                                                      "--modele", "gpt-6-astra", "--prix-entree", "10", "--prix-sortie", "50"],
             "modele_propose": "gpt-6-astra", "nom_cle": "CLE_ESSAI_S", "pid_relais": PID_ASTRA,
             "url_etat_relais": "http://127.0.0.1:8790", "porte_plafond": {"type": "environnement"}}
    d = declaration(m["depot"], astra=astra, carbon=bloc_carbon(m))
    sonde_astra(m, COMMANDES_MAIN["astra"][1])
    sonde_carbon(m)
    d["fournisseurs"]["claude"]["nom_cle"] = cle
    _ecrire(m, L.DECLARATION_RELAIS, d)
    _ecrire(m, L.RELEVE_CREDITS, dict(releve(**{cle: {"credit_usd": 1000.0, "reste_usd": 900.0, "source": "essai"},
                                                "CLE_ESSAI_S": {"non_lisible": True, "motif": "illisible"},
                                                "CLE_ESSAI_C": {"non_lisible": True, "motif": "illisible"}}),
                                      dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S", "CLE_ESSAI_C"]}))
    c = m["cmdlines"]
    c[PID_CLAUDE][c[PID_CLAUDE].index("--variable-cle") + 1] = cle
    c[PID_ASTRA][c[PID_ASTRA].index("--modeles-permis") + 1] = "gpt-6-astra"
    c[PID_CARBON][c[PID_CARBON].index("--modele") + 1] = "gemini-4-carbon"
    c[PID_ARGON][c[PID_ARGON].index("--max-appels") + 1] = "464"   # v4 : 2 × 231 + 2 (231 au pire avec Astra et Carbon)
    m["etat_argon"]["max_appels"] = 464


def preparer_piece_reelle(m) -> None:
    """v7 : le gabarit v2g rempli comme la mère le remplira (clé Minuit sur le mot de Lazar, crédit 200, réserves vides, lignes
    neuves, mot de reprise = la ligne de la course à 120 USD), relevé de la clé Minuit illisible, dépense antérieure inscrite."""
    o = json.loads(GABARIT.read_text(encoding="utf-8"))
    o.update(statut="rempli pour l'essai", go_course=GO_COURSE_NEUVE, go_epreuve=GO_EPREUVE_NEUVE, ecrit_le="2026-11-19T08:00:00Z")
    o["tentative_neuve"]["mot_de_reprise"] = GO_COURSE_NEUVE
    for n, rel in (("astra", SONDE_REL), ("carbon", SONDE_C_REL)):
        o["especes_optionnelles"][n].update(sonde_du_jour=f"{rel} (essai)", sonde_du_jour_rapport=rel)
    preparer(m)
    _ecrire(m, L.PIECE_DE_DEPART, o)
    _ecrire(m, L.RELEVE_CREDITS, dict(releve(**{CLE: {"non_lisible": True, "depense_anterieure_usd": 0.972537},
                                                "CLE_ESSAI_S": {"non_lisible": True, "motif": "illisible"},
                                                "CLE_ESSAI_C": {"non_lisible": True, "motif": "illisible"}}),
                                      dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S", "CLE_ESSAI_C"]}))
    m["main"]["registres/go.md"] = registre().replace("GO-2026-11-18-30", GO_COURSE_NEUVE).replace(
        "GO-2026-11-18-31", GO_EPREUVE_NEUVE).encode("utf-8")
    _ecrire(m, L.EPREUVE_REELLE, epreuve(m["lanceur_sha"], m["commit"], go={"id": GO_EPREUVE_NEUVE}))


def _mutant_lanceur(tmp_path, ancien, nouveau, nom):
    texte = CHEMIN_LANCEUR.read_text(encoding="utf-8")
    assert texte.count(ancien) == 1, ancien
    p = tmp_path / f"{nom}.py"
    p.write_text(texte.replace(ancien, nouveau), encoding="utf-8")
    spec = importlib.util.spec_from_file_location(nom, p)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


def _rejouer(monde):
    for d in (monde["r"].dossier_runs, monde["r"].dossier_sorties):
        if d.exists():
            shutil.rmtree(d)


# bout en bout, additif, contre-lecture, épreuve ----------------------------------------------------------------------------------


@pytest.mark.parametrize("cas", ["absent", "non_scelle", "autre_empreinte", "non_pose", "sans_prereg", "sans_epreuve", "epreuve_v6",
                                 "sans_v2c", "sans_v2d", "sans_v2e", "sans_v2f", "sans_configuration", "sans_enveloppe",
                                 "sans_commande_argon", "sans_sonde"])
def test_additif_artefacts_refuses(monde, cas, capsys):
    r = monde["r"]
    chemin, _sha = r.additif
    if cas == "absent":
        chemin.unlink()
    elif cas == "non_scelle":
        Path(str(chemin) + ".sha256").unlink()
    elif cas == "autre_empreinte":
        r.additif = (chemin, "0" * 64)
    elif cas == "non_pose":
        r.additif = (chemin, "À REMPLIR")
    else:
        p = monde["prereg_sha"]
        texte = {"sans_prereg": additif("1" * 64), "sans_epreuve": additif(p, "2" * 64), "epreuve_v6": additif(p, SHA_EPREUVE_V6),
                 "sans_v2c": additif(p, v2c="3" * 64), "sans_v2d": additif(p, v2d="4" * 64), "sans_v2e": additif(p, v2e="5" * 64),
                 "sans_v2f": additif(p, v2f="6" * 64), "sans_configuration": additif(p, configuration="7" * 64),
                 "sans_enveloppe": additif(p, enveloppe="8" * 64), "sans_commande_argon": additif(p, commande="9" * 64),
                 "sans_sonde": additif(p, sonde="a" * 64)}[cas]
        ecrire_scelle(chemin, texte)
        r.additif = (chemin, L.sha256_fichier(chemin))
    assert lancer(r) == 2
    assert "additif" in capsys.readouterr().err
    assert not r.dossier_runs.exists()


def test_contre_lecture_qui_ne_cite_pas_l_additif_refusee(monde, capsys):
    _ecrire(monde, L.CONTRE_LECTURE, contre_lecture(monde["prereg_sha"], monde["lanceur_sha"]))
    assert lancer(monde["r"]) == 2
    assert "ne cite pas l'empreinte de l'additif v2i" in capsys.readouterr().err


def test_rapport_d_epreuve_du_programme_v6_ou_du_lanceur_v6_refuse(monde):
    """Un rapport d'épreuve joué par le programme v6 ou pour le lanceur v6 n'est pas accepté ; un rapport « réussie » écrit au
    chemin v6 n'est pas lu."""
    for cle, sha in (("programme", SHA_EPREUVE_V6), ("lanceur", L6.sha256_fichier(RACINE / "scripts" / "lancer_course_auto_conception_v6.py"))):
        e = epreuve(monde["lanceur_sha"], monde["commit"])
        e["empreintes"][cle] = sha
        _ecrire(monde, L.EPREUVE_REELLE, e)
        assert lancer(monde["r"]) == 2
    (monde["depot"] / L.EPREUVE_REELLE).unlink()
    Path(str(monde["depot"] / L.EPREUVE_REELLE) + ".sha256").unlink()
    _ecrire(monde, L6.EPREUVE_REELLE, epreuve(monde["lanceur_sha"], monde["commit"]))
    assert lancer(monde["r"]) == 2


# courses v4 et v6 closes admises sur mot de reprise -------------------------------------------------------------------------------


def course_close(monde, ident, fin=True, sceller_fin=True, journal=False) -> str:
    """Une course « lancée » au dépôt d'essai (manifeste de départ) et close (manifeste de fin scellé) ; l'empreinte de son
    manifeste de fin d'essai devient l'empreinte épinglée des réglages. Rend cette empreinte."""
    d = monde["r"].dossier_runs / ident
    d.mkdir(parents=True, exist_ok=True)
    (d / "manifeste-lanceur-depart.json").write_text(json.dumps({"essai": "départ", "id": ident}) + "\n", encoding="utf-8")
    sha = "0" * 64
    if fin:
        f = d / "manifeste-lanceur-fin.json"
        f.write_text(json.dumps({"essai": "fin", "id": ident, "code": 2}) + "\n", encoding="utf-8")
        sha = L.sha256_fichier(f)
        if sceller_fin:
            sceller(f)
    admises = dict(monde["r"].courses_closes_admises)
    admises[ident] = sha
    monde["r"].courses_closes_admises = tuple(admises.items())
    if journal:
        j = monde["tmp"] / "sorties-anciennes" / ident / "course.stdout.txt"
        j.parent.mkdir(parents=True, exist_ok=True)
        j.write_text("", encoding="utf-8")
        monde["r"].sorties_autres_versions = (monde["tmp"] / "sorties-anciennes",)
    return sha


def _piece_v6(**modifs):
    return piece_de_depart(tentative_neuve={"course_close": IDENT_V6, "mot_de_reprise": "GO-2026-11-18-30"}, **modifs)


def test_courses_v4_et_v6_closes_admises_avec_le_mot_de_reprise(monde):
    s4, s6 = course_close(monde, IDENT_V4, journal=True), course_close(monde, IDENT_V6, journal=True)
    assert lancer(monde["r"]) == 0
    u = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())["une_seule_course"]
    assert u["courses_closes_admises"] == [{"id": IDENT_V4, "manifeste_fin_sha256": s4}, {"id": IDENT_V6, "manifeste_fin_sha256": s6}]
    assert u["course_close_citee"] == IDENT_V6 and u["mot_de_reprise"] == "GO-2026-11-18-30" and len(u["journaux_hors_depot"]) == 2


def test_les_empreintes_epinglees_sont_celles_des_courses_closes_du_depot():
    for ident, sha in L.COURSES_CLOSES_ADMISES:
        f = RACINE / "runs" / ident / "manifeste-lanceur-fin.json"
        assert L.sha256_fichier(f) == sha and L.scelle(f), ident
    assert L.COURSE_CLOSE_CITEE == IDENT_V6 and IDENT_V4 == L6.COURSE_CLOSE_ADMISE[0]


def test_v7_ne_part_qu_une_fois(monde, capsys):
    course_close(monde, IDENT_V4)
    course_close(monde, IDENT_V6)
    assert lancer(monde["r"]) == 0
    assert lancer(monde["r"]) == 2 and "tentative v9 déjà lancée" in capsys.readouterr().err


@pytest.mark.parametrize("ident", ["v4", "v6"])
@pytest.mark.parametrize("cas", ["sans_fin", "fin_non_scellee", "fin_autre_empreinte"])
def test_course_close_non_close_refusee(monde, ident, cas, capsys):
    autre = IDENT_V6 if ident == "v4" else IDENT_V4
    course_close(monde, autre)
    i = IDENT_V4 if ident == "v4" else IDENT_V6
    course_close(monde, i, fin=(cas != "sans_fin"), sceller_fin=(cas != "fin_non_scellee"))
    if cas == "fin_autre_empreinte":
        monde["r"].courses_closes_admises = tuple((k, "1" * 64 if k == i else v) for k, v in monde["r"].courses_closes_admises)
    assert lancer(monde["r"]) == 2
    assert "non close" in capsys.readouterr().err


def test_course_citee_absente_du_depot_refusee(monde, capsys):
    course_close(monde, IDENT_V4)                                  # la v6 n'est pas au dépôt d'essai : pièce incohérente
    assert lancer(monde["r"]) == 2 and "n'est pas au dépôt" in capsys.readouterr().err


def test_piece_qui_cite_la_v4_refusee(monde, capsys):
    course_close(monde, IDENT_V4)
    course_close(monde, IDENT_V6)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(tentative_neuve={"course_close": IDENT_V4, "mot_de_reprise": "GO-2026-11-18-30"}))
    assert lancer(monde["r"]) == 2 and "course_close" in capsys.readouterr().err


@pytest.mark.parametrize("version", ["v1", "v2", "v3", "v5"])
def test_course_autre_que_les_closes_deja_lancee_bloque_la_v7(monde, version, capsys):
    course_close(monde, IDENT_V6)
    d = monde["r"].dossier_runs / f"20261118-000000-course-auto-conception-{version}"
    d.mkdir(parents=True)
    (d / "manifeste-lanceur-depart.json").write_text("{}", encoding="utf-8")
    assert lancer(monde["r"]) == 2
    assert "seules les courses closes" in capsys.readouterr().err


def test_journal_d_une_autre_course_a_cote_des_closes_refuse(monde, capsys):
    course_close(monde, IDENT_V6, journal=True)
    j = monde["tmp"] / "sorties-anciennes" / "20261118-999999-course-auto-conception-v4" / "course.stdout.txt"
    j.parent.mkdir(parents=True)
    j.write_text("", encoding="utf-8")
    assert lancer(monde["r"]) == 2 and "journaux hors dépôt d'une autre course" in capsys.readouterr().err


def test_mutation_course_close_sans_verifier_la_fin_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "        if not fin.is_file() or not scelle(fin) or sha256_fichier(fin) != admises[ident]:\n",
                        "        if False:\n", "lanceur_v9_mutant_course_close")
    course_close(monde, IDENT_V4)
    course_close(monde, IDENT_V6, fin=False)
    assert M.principal([], reglages=monde["r"]) == 0                          # muté : une course non close admise
    shutil.rmtree(monde["r"].dossier_runs / [p.name for p in monde["r"].dossier_runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)][0])
    shutil.rmtree(monde["r"].dossier_sorties)
    assert lancer(monde["r"]) == 2


# mot de reprise, lignes consommées, ligne de la course à 120 USD -----------------------------------------------------------------


@pytest.mark.parametrize("modif,motif", [
    ({"tentative_neuve": None}, "tentative_neuve"),
    ({"tentative_neuve": {"course_close": IDENT_V6}}, "mot_de_reprise"),
    ({"tentative_neuve": {"course_close": IDENT_V6, "mot_de_reprise": "GO-2026-11-18-31"}}, "mot_de_reprise"),
    ({"tentative_neuve": {"course_close": IDENT_V4, "mot_de_reprise": "GO-2026-11-18-30"}}, "course_close"),
    ({"go_course": "GO-2026-11-18-67", "tentative_neuve": {"course_close": IDENT_V6, "mot_de_reprise": "GO-2026-11-18-67"}},
     "consommée"),
    ({"go_epreuve": "GO-2026-11-18-68"}, "consommée"), ({"go_epreuve": "GO-2026-11-18-21"}, "consommée"),
])
def test_mot_de_reprise_et_lignes_neuves_artefacts(monde, modif, motif, capsys):
    p = piece_de_depart(**{k: v for k, v in modif.items() if v is not None})
    for k in [k for k, v in modif.items() if v is None]:
        del p[k]
    _ecrire(monde, L.PIECE_DE_DEPART, p)
    assert lancer(monde["r"]) == 2 and motif in capsys.readouterr().err
    assert not monde["r"].dossier_runs.exists()


@pytest.mark.parametrize("texte", [registre(plafond_c="120 USD"), registre(plafond_c="90 USD"), registre(plafond_c="45 USD"),
                                   registre(suite="| GO-2026-11-18-41 | 2026-11-18 | révocation | GO-2026-11-18-30 | — | — | Lazar | R-4 |\n"),
                                   registre().replace("| GO-2026-11-18-30 | 2026-11-18 | calcul", "| GO-2026-11-18-30 | 2026-11-18 | décision")])
def test_ligne_de_la_course_artefacts(monde, texte):
    """Ligne de la course à 120 ou 90 USD (anciens plafonds) ou à 45, révoquée, ou d'un autre type : refus (150 exigés à l'identique)."""
    monde["main"]["registres/go.md"] = texte.encode("utf-8")
    assert lancer(monde["r"]) == 2


def test_verifier_mot_de_reprise_unitaire_sain_et_artefacts():
    p = piece_de_depart()
    assert L.verifier_mot_de_reprise(registre(), AUJOURD_HUI, p)["plafond_lu"] == 150.0
    with pytest.raises(L.Refus, match="plafond"):
        L.verifier_mot_de_reprise(registre(plafond_c="90 USD"), AUJOURD_HUI, p)
    with pytest.raises(L.Refus, match="tentative neuve"):
        L.verifier_mot_de_reprise(registre(perimetre_c="auto-conception"), AUJOURD_HUI, p)
    with pytest.raises(L.Refus, match="consommée"):
        L.verifier_mot_de_reprise(registre(), AUJOURD_HUI, dict(p, go_course="GO-2026-11-18-67",
                                                                tentative_neuve={"course_close": IDENT_V6, "mot_de_reprise": "GO-2026-11-18-67"}))


def test_mutation_lignes_consommees_v6_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, '"GO-2026-11-18-36", "GO-2026-11-18-67", "GO-2026-11-18-68")\n', '"GO-2026-11-18-36")\n',
                        "lanceur_v9_mutant_lignes")
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(go_epreuve="GO-2026-11-18-68"))
    assert M.verifier_piece_de_depart(monde["r"])["go_epreuve"] == "GO-2026-11-18-68"   # muté : la ligne de la v6 resservie
    with pytest.raises(L.Refus, match="consommée"):
        L.verifier_piece_de_depart(monde["r"])


def test_piece_v2f_de_la_course_v6_refusee(monde, capsys):
    v2f = RACINE / L6.PIECE_DE_DEPART
    ecrire_scelle(monde["depot"] / L.PIECE_DE_DEPART, v2f.read_text(encoding="utf-8"))
    with pytest.raises(L.Refus):
        L.verifier_piece_de_depart(monde["r"])
    o = json.loads(v2f.read_text(encoding="utf-8"))
    o.update(variable_cle_claude=CLE, cle_claude_mot_de_lazar="« Clé Minuit (Recommandé) »")
    ecrire_scelle(monde["depot"] / L.PIECE_DE_DEPART, json.dumps(o))
    with pytest.raises(L.Refus, match="consommée"):                       # même avec la clé Minuit : lignes de la v6 consommées
        L.verifier_piece_de_depart(monde["r"])


# plafonds relevés (configuration v3) ------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("modif", [lambda f: f["plafonds_session"].__setitem__("proposeur", 3.0),
                                   lambda f: f["budget"].__setitem__("plafond_usd", 90.0),
                                   lambda f: f["relais_persistants"].__setitem__("plafond_relais_claude_usd", 90.0),
                                   lambda f: f["budget"]["etapes"][3].__setitem__("plafond_relais_usd", 91.0)])
def test_configuration_v2_ou_plafonds_anciens_refuses(modif):
    f = json.loads(json.dumps(FIXE))
    modif(f)
    with pytest.raises(L.Refus):
        L.garde_configuration_fixe(f)
    with pytest.raises(L.Refus):
        L.garde_configuration_fixe(json.loads((RACINE / L6.PIECES["configuration"][0]).read_text(encoding="utf-8")))


def test_relais_claude_a_90_refuse(monde):
    c = monde["cmdlines"][PID_CLAUDE]
    for v in ("90", "120"):                                       # v9 : les anciens plafonds refusés
        c[c.index("--plafond-usd") + 1] = v
        assert lancer(monde["r"]) == 2


def test_mutation_plafond_de_session_non_verifie_attrapee(tmp_path):
    M = _mutant_lanceur(tmp_path, "    if ps.get(\"proposeur\") != PLAFOND_SESSION_PROPOSEUR_USD:\n", "    if False:\n",
                        "lanceur_v9_mutant_plafond_session")
    f = json.loads(json.dumps(FIXE))
    f["plafonds_session"]["proposeur"] = 3.0
    M.garde_configuration_fixe(f)                                  # muté : la configuration v2 passerait
    with pytest.raises(L.Refus):
        L.garde_configuration_fixe(f)


# clé Claude Minuit sur le mot de Lazar ------------------------------------------------------------------------------------------


@pytest.mark.parametrize("modif,motif", [({"variable_cle_claude": CLE_RIGAUD}, "refusée"),
                                         ({"variable_cle_claude": "RR_ANTHROPIC_API_KEY_ESSAI"}, "exigée"),
                                         ({"cle_claude_mot_de_lazar": None}, "cle_claude_mot_de_lazar"),
                                         ({"cle_claude_mot_de_lazar": "clé Rigaud"}, "cle_claude_mot_de_lazar")])
def test_cle_minuit_artefacts_refuses(monde, modif, motif, capsys):
    p = piece_de_depart(**{k: v for k, v in modif.items() if v is not None})
    for k in [k for k, v in modif.items() if v is None]:
        del p[k]
    _ecrire(monde, L.PIECE_DE_DEPART, p)
    assert lancer(monde["r"]) == 2 and motif in capsys.readouterr().err


def test_relais_claude_sur_rigaud_refuse(monde, capsys):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = CLE_RIGAUD
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert lancer(monde["r"]) == 2 and "refusée pour cette tentative" in capsys.readouterr().err


def test_mutation_cle_minuit_non_exigee_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "    if cle != CLE_CLAUDE_TENTATIVE:", "    if False:", "lanceur_v9_mutant_minuit")
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(variable_cle_claude="RR_ANTHROPIC_API_KEY_ESSAI"))
    assert M.verifier_piece_de_depart(monde["r"])["variable_cle_claude"] == "RR_ANTHROPIC_API_KEY_ESSAI"
    with pytest.raises(L.Refus):
        L.verifier_piece_de_depart(monde["r"])


# Carbon synchrone : réglage de l'enveloppe ----------------------------------------------------------------------------------------


def _pieces_reelles():
    return {n: {"chemin": rel, "absolu": str(RACINE / rel), "sha256": sha} for n, (rel, sha) in L.PIECES.items()}


def _enveloppe_modifiee(tmp_path, ancien, nouveau):
    t = (RACINE / L.PIECES["enveloppe_carbon"][0]).read_text(encoding="utf-8")
    assert t.count(ancien) >= 1, ancien
    p = tmp_path / "appel-carbon-synchrone-v1.sh"
    p.write_text(t.replace(ancien, nouveau), encoding="utf-8")
    pieces = _pieces_reelles()
    pieces["enveloppe_carbon"] = {"chemin": L.PIECES["enveloppe_carbon"][0], "absolu": str(p), "sha256": L.sha256_fichier(p)}
    return pieces


def _bloc(pieces, **modifs):
    b = {"commande": ["bash", pieces["enveloppe_carbon"]["absolu"]], "modele_propose": "gemini-4-carbon"}
    b.update(modifs)
    return b


def test_reglage_carbon_sain():
    pieces = _pieces_reelles()
    c = L.controler_reglage_carbon(_bloc(pieces), pieces, None)
    assert c["valeurs"] == L.REGLAGE_CARBON and c["drapeaux"] == ["--sans-config-pensee"] and c["max_sortie_de_la_commande"] == 65536
    assert c["duree_au_pire_s"] == 1740.0 <= c["borne_s"] == 1770.0
    assert c["valeurs"]["--provision-pensee-jetons"] >= c["valeurs"]["--max-sortie-jetons"]


@pytest.mark.parametrize("ancien,nouveau,motif", [
    ("--provision-pensee-jetons 65536", "--provision-pensee-jetons 49152", "65536"),
    ("--max-sortie-jetons 65536", "--max-sortie-jetons 32768", "65536"),
    (" --sans-config-pensee", "", "drapeaux"),
    (" --sans-config-pensee", " --sans-config-pensee --recherche-web", "drapeau"),
    (" --sans-config-pensee", " --sans-config-pensee --sans-compter-jetons", "drapeau"),
    ("--provision-pensee-jetons 65536", "--provision-pensee 65536", "options"),
    ("--prix-sortie 41.5", "--prix-sortie 41.5 --prix-sortie 20", "deux fois"),
    ("--prix-sortie 41.5", "--prix-sortie=41.5", "non admis"),
    ("--modele gemini-4-carbon", "--modele gemini-4-argon", "gemini-4-carbon"),
    ("--url-base http://127.0.0.1:8792/v1beta", "--url-base http://127.0.0.1:8788/v1beta", "8788"),
    ("timeout -k 20 1720", "timeout -k 20 1790", "timeout"),
    ("--delai-s 1680", "--delai-s 1720", "1720"),
    ("--prix-entree 8.3", "--prix-entree 4", "8.3"),
    ('if [ "$#" -ne 0 ]', 'if [ "1" -ne 1 ]', "refuser tout argument"),
    ("--url-base http://127.0.0.1:8792/v1beta\n", '--url-base http://127.0.0.1:8792/v1beta "$@"\n', "arguments du noyau"),
    ("argon-recherche-v1/commande_argon_v3d.py\"", "argon-recherche-v1/commande_argon_v3c.py\"", "commande d'Argon épinglée"),
])
def test_reglage_carbon_artefacts_refuses(tmp_path, ancien, nouveau, motif):
    pieces = _enveloppe_modifiee(tmp_path, ancien, nouveau)
    with pytest.raises(L.Refus, match=motif):
        L.controler_reglage_carbon(_bloc(pieces), pieces, None)


@pytest.mark.parametrize("modif,motif", [({"commande": None}, "exactement"), ({"modele_propose": "gemini-4-argon"}, "modele_propose")])
def test_declaration_de_carbon_artefacts(modif, motif):
    pieces = _pieces_reelles()
    b = _bloc(pieces, **modif)
    if b["commande"] is None:
        b["commande"] = ["bash", pieces["enveloppe_carbon"]["absolu"], "--provision-pensee-jetons", "1"]
    with pytest.raises(L.Refus, match=motif):
        L.controler_reglage_carbon(b, pieces, None)
    for autre in (["bash", "/tmp/appel-carbon-synchrone-v1.sh"], ["/bin/bash", pieces["enveloppe_carbon"]["absolu"]],
                  [sys.executable, pieces["commande_argon"]["absolu"]]):
        with pytest.raises(L.Refus, match="exactement"):
            L.controler_reglage_carbon(_bloc(pieces, commande=autre), pieces, None)


def test_reglage_carbon_exige_les_deux_pieces_epinglees_par_la_piece_de_depart():
    pieces = _pieces_reelles()
    bon = {"commandes_epinglees": {"carbon": {"empreintes": [pieces["enveloppe_carbon"]["sha256"], pieces["commande_argon"]["sha256"]]}}}
    L.controler_reglage_carbon(_bloc(pieces), pieces, bon)
    for garde in ([pieces["enveloppe_carbon"]["sha256"]], [pieces["commande_argon"]["sha256"]], ["9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75"]):
        with pytest.raises(L.Refus, match="non épinglée"):
            L.controler_reglage_carbon(_bloc(pieces), pieces, {"commandes_epinglees": {"carbon": {"empreintes": garde}}})


def test_pire_cas_carbon_sans_troncature_sous_6_usd():
    pieces = _pieces_reelles()
    c = L.controler_reglage_carbon(_bloc(pieces), pieces, None)
    e = {"rang": 1, "nom": "x", "octets": 136265, "caracteres": 130101, "sha256": "e" * 64}
    p = L.pire_cas_carbon(c, e, 6.0)
    assert p["max_output_tokens"] == 65536 and p["pire_cas_usd"] == pytest.approx(5.817437, abs=1e-6)
    assert p["au_compte_de_la_commande"]["entree_gardee_jetons"] == 45536
    assert p["borne_prudente_octets_sur_2"]["max_output_tokens"] == 64734
    assert p["borne_prudente_octets_sur_2"]["plafond_necessaire_usd"] == 6.04
    with pytest.raises(L.Refus, match="5.82"):
        L.pire_cas_carbon(c, e, 5.8)                               # la sortie serait réduite : troncature, plafond nécessaire dit
    with pytest.raises(L.Refus, match="troncature"):
        L.pire_cas_carbon(c, e, 3.0)                               # l'ancien plafond par appel
    assert L.pire_cas_carbon(c, dict(e, caracteres=150000, octets=160000), 6.0)["pire_cas_usd"] <= 6.0


def test_pire_cas_comme_la_commande_le_calcule():
    """La garde avant envoi de `commande_argon_v3d.executer`, refaite par la commande elle-même (aucun appel : la garde refuse ou
    non avant tout envoi) : sur une consigne de 130 101 caractères, plafond 6 USD, la sortie demandée est 65 536."""
    import math
    m = L.charger_commande_argon(str(RACINE / L.PIECES["commande_argon"][0]))
    garde = math.ceil(math.ceil(130101 / 3) * 1.05)
    place = math.floor((6.0 - garde * 8.3e-6) / 41.5e-6)
    assert garde == 45536 and min(m.MAX_SORTIE_JETONS_DEFAUT, place - 65536) == 65536
    assert garde * 8.3e-6 + (65536 + 65536) * 41.5e-6 == pytest.approx(5.817437, abs=1e-6)


def test_mutation_troncature_non_refusee_attrapee(tmp_path):
    M = _mutant_lanceur(tmp_path, '    if cmd["max_output_tokens"] < v["--max-sortie-jetons"]:\n', "    if False:\n",
                        "lanceur_v9_mutant_troncature")
    pieces = _pieces_reelles()
    c = L.controler_reglage_carbon(_bloc(pieces), pieces, None)
    e = {"rang": 1, "nom": "x", "octets": 136265, "caracteres": 130101, "sha256": "e" * 64}
    assert M.pire_cas_carbon(c, e, 5.8)["max_output_tokens"] < 65536          # muté : sortie réduite acceptée
    with pytest.raises(L.Refus):
        L.pire_cas_carbon(c, e, 5.8)


def test_mutation_commande_de_carbon_non_figee_attrapee(tmp_path):
    M = _mutant_lanceur(tmp_path, '    if bloc.get("commande") != ["bash", env_abs]:\n        raise Refus(f"fournisseurs.carbon.commande',
                        '    if False:\n        raise Refus(f"fournisseurs.carbon.commande', "lanceur_v9_mutant_fige")
    pieces = _pieces_reelles()
    b = _bloc(pieces, commande=["bash", pieces["enveloppe_carbon"]["absolu"], "--sans-config-pensee"])
    assert M.controler_reglage_carbon(b, pieces, None)["valeurs"] == L.REGLAGE_CARBON   # muté : un argument passerait
    with pytest.raises(L.Refus):
        L.controler_reglage_carbon(b, pieces, None)


def test_mutation_provision_sous_la_sortie_attrapee(tmp_path):
    M = _mutant_lanceur(tmp_path, '    if valeurs["--max-sortie-jetons"] != maxi or valeurs["--provision-pensee-jetons"] < valeurs["--max-sortie-jetons"]:\n        raise Refus(f"enveloppe de Carbon',
                        '    if False:\n        raise Refus(f"enveloppe de Carbon', "lanceur_v9_mutant_provision")
    pieces = _enveloppe_modifiee(tmp_path, "--provision-pensee-jetons 65536", "--provision-pensee-jetons 32768")
    reg = dict(M.REGLAGE_CARBON, **{"--provision-pensee-jetons": 32768})
    M.REGLAGE_CARBON.clear()
    M.REGLAGE_CARBON.update(reg)
    assert M.controler_reglage_carbon(_bloc(pieces), pieces, None)["valeurs"]["--provision-pensee-jetons"] == 32768
    with pytest.raises(L.Refus):
        L.controler_reglage_carbon(_bloc(pieces), pieces, None)


# Carbon synchrone : relais, sonde du jour, course entière -----------------------------------------------------------------------


@avec_commandes
def test_gabarit_rempli_carbon_synchrone_actif(monde):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]
    c = dep["carbon_regle"]
    assert c["valeurs"] == L.REGLAGE_CARBON and c["pire_cas"]["max_output_tokens"] == 65536
    assert c["pire_cas"]["pire_cas_usd"] == pytest.approx(6.03327, abs=1e-6) and c["duree_au_pire_s"] == 1740.0   # v8
    assert dep["sonde_carbon_du_jour"]["exigee"] is True and dep["plus_grande_entree_servie"]["octets"] == 136265
    v = dep["procedure_relais_persistants"]["relais_vivants"]["carbon"]
    assert v["port"] == "8792" and v["programme_sha256"] == L.PROGRAMMES_RELAIS["carbon"][1] or v["programme"].endswith("relais_gemini_v2.py")
    assert dep["parts_au_pire"]["carbon"]["part_au_pire_usd"] == pytest.approx(66.55) and dep["parts_au_pire"]["claude"]["part_au_pire_usd"] == 150.0
    vu = json.loads((Path(dep["sortie"]) / "vu.json").read_text())
    assert "carbon" in vu["fournisseurs"]


@avec_commandes
@pytest.mark.parametrize("etat,code,motif", [({"max_appels": 23}, 2, "24"), ({"max_appels": 24}, 0, None),
                                             ({"variable_cle_encore_presente": True}, 2, "variable de clé"),
                                             ({"max_appels": None}, 2, "max_appels"), ({"appels": 1}, 2, "relais neuf")])
def test_relais_carbon_gemini_v2(monde, etat, code, motif, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    monde["etat_carbon"].update(etat)
    assert lancer(monde["r"]) == code
    if motif:
        assert motif in capsys.readouterr().err


@avec_commandes
@pytest.mark.parametrize("modif,motif", [
    (lambda c: c.__setitem__(c.index("--modele") + 1, "gemini-4-argon"), "--modele"),
    (lambda c: c.extend(["--amont", "http://127.0.0.1:9"]), "--amont"),
    (lambda c: c.__setitem__(c.index("--port") + 1, "8788"), "port"),
])
def test_relais_carbon_arguments_artefacts(monde, modif, motif, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    modif(monde["cmdlines"][PID_CARBON])
    assert lancer(monde["r"]) == 2 and motif in capsys.readouterr().err


@avec_commandes
@pytest.mark.parametrize("commande,modifs,motif", [
    ({}, {"jour": "2026-11-17"}, "du jour"), ({}, {"ok": False}, "non réussie"), ({}, {"version": "autre"}, "version"),
    ({"code": 5}, {}, "code 5"), ({"fin": "MAX_TOKENS"}, {}, "MAX_TOKENS"), ({"reponse_non_vide": False}, {}, "non vide"),
    ({"non_tronquee": False}, {}, "non tronquée"), ({"max_sortie_jetons": 64734}, {}, "sortie demandée"),
    ({"modele_servi": "gemini-4-carbon-preview"}, {}, "modèle servi"), ({"modele_servi": "models/gemini-4-carbon"}, {}, "modèle servi"),
    ({"cout_usd": 6.5}, {}, "coût"), ({}, {"plafond_session_usd": 3.0}, "plafond"),
    ({}, {"empreintes": {"programme": "b" * 64}}, "empreinte"), ({}, {"entree": {"sha256": "c" * 64, "octets": 136265}}, "entrée"),
    ({}, {"reglage": dict(L.REGLAGE_CARBON, **{"--provision-pensee-jetons": 49152})}, "réglage"),
])
def test_sonde_carbon_du_jour_artefacts(monde, commande, modifs, motif, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    if "empreintes" in modifs:
        modifs["empreintes"] = dict(L.rapport_sonde_carbon_d_essai(AUJOURD_HUI, entree_servie(monde["depot"]))["empreintes"],
                                    **modifs["empreintes"])
    sonde_carbon(monde, commande, **modifs)
    assert lancer(monde["r"]) == 2 and motif in capsys.readouterr().err


@avec_commandes
def test_sonde_carbon_absente_non_scellee_ou_non_nommee_refusee(monde):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    Path(str(monde["depot"] / SONDE_C_REL) + ".sha256").unlink()
    assert lancer(monde["r"]) == 2
    (monde["depot"] / SONDE_C_REL).unlink()
    assert lancer(monde["r"]) == 2
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie(carbon={"sonde_du_jour_rapport": None}))
    with pytest.raises(L.Refus, match="sonde_du_jour_rapport"):
        L.verifier_piece_de_depart(monde["r"])


@avec_commandes
def test_mutation_sonde_carbon_sans_non_tronquee_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, 'c.get("reponse_non_vide") is not True or c.get("non_tronquee") is not True:',
                        'c.get("reponse_non_vide") is not True:', "lanceur_v9_mutant_sonde_tronquee")
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    sonde_carbon(monde, {"non_tronquee": False})
    assert M.principal([], reglages=monde["r"]) == 0                          # muté : une sonde tronquée passerait
    _rejouer(monde)
    assert lancer(monde["r"]) == 2


@avec_commandes
def test_mutation_sonde_carbon_non_verifiee_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "    sonde_carbon = verifier_sonde_carbon(r, depart, aujourd_hui, pieces, entree_servie, carbon)",
                        "    sonde_carbon = {}", "lanceur_v9_mutant_sonde_absente")
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    sonde_carbon(monde, {"code": 7, "fin": "STOP"}, ok=False)
    assert M.principal([], reglages=monde["r"]) == 0
    _rejouer(monde)
    assert lancer(monde["r"]) == 2


@avec_commandes
def test_mutation_relais_carbon_variable_non_verifiee_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, '    if nom == "carbon" and (etat.get("variable_cle_encore_presente") is not False',
                        '    if False and (etat.get("variable_cle_encore_presente") is not False', "lanceur_v9_mutant_relais_carbon")
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    monde["etat_carbon"]["variable_cle_encore_presente"] = True
    assert M.principal([], reglages=monde["r"]) == 0
    _rejouer(monde)
    assert lancer(monde["r"]) == 2


@avec_commandes
def test_piece_de_depart_carbon_commandes_non_epinglees_refusee(monde, capsys):
    preparer(monde)
    o = piece_remplie()
    o["commandes_epinglees"]["carbon"]["empreintes"] = [L.PIECES["enveloppe_carbon"][1]]   # la commande d'Argon manque
    _ecrire(monde, L.PIECE_DE_DEPART, o)
    assert lancer(monde["r"]) == 2 and "non épinglée" in capsys.readouterr().err


def test_controle_carbon_unitaire_sain_et_artefacts():
    """`controler_relais_externe` sur Carbon (relais Gemini v2) : borne doublée, variable effacée, amont de Google."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        prog = Path(d) / "relais_gemini_v2.py"
        prog.write_text("# factice\n", encoding="utf-8")
        for etat, args, ok in (({"max_appels": 24}, [], True), ({"max_appels": 23}, [], False),
                               ({"max_appels": 24, "variable_cle_encore_presente": True}, [], False),
                               ({"max_appels": 24}, ["--amont", L.AMONT_GEMINI], True),
                               ({"max_appels": 24}, ["--amont", "https://autre.example"], False),
                               ({"max_appels": "24"}, [], False)):
            r = L.Reglages.production()
            r.programmes_relais = dict(L.PROGRAMMES_RELAIS, carbon=("relais_gemini_v2.py", L.sha256_fichier(prog)))
            r.lire_cmdline = lambda pid, a=args: [sys.executable, str(prog), "--port", "8792", "--variable-cle", "K", "--modele", "m-carbon"] + a
            r.lire_etat_relais = lambda url, e=etat: dict({"appels": 0, "variable_cle_encore_presente": False}, **e)
            b = {"nom_cle": "K", "modele_propose": "m-carbon"}
            meta = {"pid_relais": 4242, "url_etat_relais": "http://127.0.0.1:8792"}
            if ok:
                assert L.controler_relais_externe(r, "carbon", b, meta, 11)["etat"]["max_appels"] == 24
            else:
                with pytest.raises(L.Refus):
                    L.controler_relais_externe(r, "carbon", b, meta, 11)


# gabarit v2g, pièce telle que la mère la remplira ---------------------------------------------------------------------------------


def test_gabarit_brut_refuse_tant_qu_il_n_est_pas_rempli(monde):
    ecrire_scelle(monde["depot"] / L.PIECE_DE_DEPART, GABARIT.read_text(encoding="utf-8"))
    with pytest.raises(L.Refus, match="À REMPLIR"):
        L.verifier_piece_de_depart(monde["r"])


def test_gabarit_v2g_porte_les_mots_de_lazar_et_de_la_mere():
    o = json.loads(GABARIT.read_text(encoding="utf-8"))
    assert o["variable_cle_claude"] == "RR_ANTHROPIC_API_KEY_MINUIT" and o["credit_declare_cle_claude_usd"] == 200.0
    assert o["reserves_cle_claude"] == [] and "Clé Minuit" in o["cle_claude_mot_de_lazar"]
    assert o["tentative_neuve"]["course_close"] == IDENT_V6
    assert o["commandes_epinglees"]["carbon"]["empreintes"] == [L.PIECES["enveloppe_carbon"][1], L.PIECES["commande_argon"][1]]
    assert o["especes_optionnelles"]["carbon"]["declaree"] and o["especes_optionnelles"]["astra"]["declaree"]
    assert not o["especes_optionnelles"]["kimi"]["declaree"]


@avec_commandes
def test_gabarit_v2g_rempli_accepte_au_credit_de_minuit(monde):
    preparer_piece_reelle(monde)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["go"]["id"] == GO_COURSE_NEUVE and dep["mot_de_reprise"]["id"] == GO_COURSE_NEUVE
    assert dep["cle_par_espece"]["prop-opus"] == CLE and dep["releve_credits_avant"]["cles"][CLE]["reste_usd"] == pytest.approx(199.027463)
    for p in list(un_run(monde["r"]).rglob("*")):
        if p.is_file():
            assert "valeur-secrete-essai" not in p.read_text(errors="replace"), p


@avec_commandes
def test_credit_de_minuit_insuffisant_alerte_code_3(monde):
    """Reste net ≤ 150 (part au pire de la clé Claude) → alerte, code 3 ; au-dessus → départ."""
    preparer_piece_reelle(monde)
    _ecrire(monde, L.RELEVE_CREDITS, dict(releve(**{CLE: {"non_lisible": True, "depense_anterieure_usd": 50.0},
                                                    "CLE_ESSAI_S": {"non_lisible": True, "motif": "illisible"},
                                                    "CLE_ESSAI_C": {"non_lisible": True, "motif": "illisible"}}),
                                          dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S", "CLE_ESSAI_C"]}))
    assert lancer(monde["r"]) == 3
    _rejouer(monde)
    _ecrire(monde, L.RELEVE_CREDITS, dict(releve(**{CLE: {"non_lisible": True, "depense_anterieure_usd": 49.9},
                                                    "CLE_ESSAI_S": {"non_lisible": True, "motif": "illisible"},
                                                    "CLE_ESSAI_C": {"non_lisible": True, "motif": "illisible"}}),
                                          dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S", "CLE_ESSAI_C"]}))
    assert lancer(monde["r"]) == 0


# constantes v7 et rien d'autre ne change ----------------------------------------------------------------------------------------


# --- v8 : Argon proposeur sans troncature, juge v5 à l'identique, plafond de session 6,05 USD --------------------------------------


import inspect  # noqa: E402
L7 = _charger_module("lancer_course_auto_conception_v7_pour_essai_v9", RACINE / "scripts" / "lancer_course_auto_conception_v7.py")
SHA_EPREUVE_V7 = L7.PIECES["epreuve_temoins"][1]
ENV_ARGON = RACINE / L.PIECES["enveloppe_argon_sans_troncature"][0]
ENV_ARGON_V5 = RACINE / L.PIECES["enveloppe_argon"][0]
FAUX_AMONT = RACINE / "docs/notes/ideation-organisme-v1/argon-recherche-v1/faux_amont_gemini_recherche_v3.py"


def _pieces_argon(tmp_path, ancien=None, nouveau=None, compte=1):
    pieces = _pieces_reelles()
    if ancien is not None:
        t = ENV_ARGON.read_text(encoding="utf-8")
        assert t.count(ancien) >= compte, ancien
        p = tmp_path / "appel-argon-sans-troncature-v1.sh"
        p.write_text(t.replace(ancien, nouveau), encoding="utf-8")
        pieces["enveloppe_argon_sans_troncature"] = {"chemin": L.PIECES["enveloppe_argon_sans_troncature"][0], "absolu": str(p),
                                                     "sha256": L.sha256_fichier(p)}
    return pieces


def _bloc_argon(pieces, **modifs):
    b = {"commande": ["bash", pieces["enveloppe_argon_sans_troncature"]["absolu"]]}
    b.update(modifs)
    return b


def _v8_bout_en_bout_remplace_par_v9():
    """(v9) remplacé par `test_v9_bout_en_bout_150_seuils_et_conservation`."""


@pytest.mark.parametrize("cas", ["sans_v2g", "sans_enveloppe_argon", "epreuve_v7"])
def test_additif_v2h_artefacts_refuses(monde, cas, capsys):
    r, p = monde["r"], monde["prereg_sha"]
    chemin, _sha = r.additif
    texte = {"sans_v2g": additif(p, v2g="b" * 64), "sans_enveloppe_argon": additif(p, enveloppe_argon="c" * 64),
             "epreuve_v7": additif(p, SHA_EPREUVE_V7)}[cas]
    ecrire_scelle(chemin, texte)
    r.additif = (chemin, L.sha256_fichier(chemin))
    assert lancer(r) == 2 and "additif v2i" in capsys.readouterr().err


def test_additif_v2h_reel_de_la_v8_epingle_scelle_et_cite_ses_pieces():
    chemin = RACINE / L8.ADDITIF
    assert L8._epingle(L8.ADDITIF_SHA256) and L8.sha256_fichier(chemin) == L8.ADDITIF_SHA256 and L8.scelle(chemin)
    texte = chemin.read_text(encoding="utf-8")
    for h in (L8.PREREG_SHA256, L8.PIECES["epreuve_temoins"][1], L8.ADDITIF_V2C[1], L8.ADDITIF_V2D[1], L8.ADDITIF_V2E[1],
              L8.ADDITIF_V2F[1], L8.ADDITIF_V2G[1], L8.PIECES["configuration"][1], L8.PIECES["enveloppe_carbon"][1],
              L8.PIECES["commande_argon"][1], L8.PIECES["sonde_carbon"][1], L8.PIECES["enveloppe_argon_sans_troncature"][1]):
        assert h in texte, h
    for mot in ("fais sauter la troncature pour argo aussi", "6,05", "6,03327", "5,817437", "65 536", "--sans-config-pensee",
                "≈ 5 560", "≈ 6 876", "464", "66,55"):
        assert mot in texte, mot


def test_rapport_d_epreuve_du_programme_v7_ou_du_lanceur_v7_refuse(monde):
    for cle, sha in (("programme", SHA_EPREUVE_V7), ("lanceur", L7.sha256_fichier(RACINE / "scripts" / "lancer_course_auto_conception_v7.py"))):
        e = epreuve(monde["lanceur_sha"], monde["commit"])
        e["empreintes"][cle] = sha
        _ecrire(monde, L.EPREUVE_REELLE, e)
        assert lancer(monde["r"]) == 2


# Argon : l'enveloppe à deux branches --------------------------------------------------------------------------------------------


def test_reglage_argon_sain():
    pieces = _pieces_reelles()
    a = L.controler_reglage_argon(_bloc_argon(pieces), pieces)
    assert a["valeurs"] == L.REGLAGE_ARGON_PROPOSEUR and a["drapeaux"] == ["--sans-config-pensee"]
    assert a["valeurs"]["--max-sortie-jetons"] == a["max_sortie_de_la_commande"] == 65536 <= a["valeurs"]["--provision-pensee-jetons"]
    assert a["duree_au_pire_s"] == 1740.0 and a["juge"]["identique_a_la_v5"]
    assert (a["juge"]["provision_pensee_jetons"], a["juge"]["delai_s"], a["juge"]["caracteres_par_jeton"]) == (8192, 1500.0, 4.0)
    assert L.REGLAGE_ARGON_PROPOSEUR == dict(L.REGLAGE_CARBON, **{"--modele": "gemini-4-argon", "--url-base": "http://127.0.0.1:8788/v1beta"})


def test_ligne_du_juge_egale_a_la_v5_jeton_pour_jeton():
    lu = L.lire_reglage_enveloppe_argon(ENV_ARGON.read_text(encoding="utf-8"))
    v5 = L.ligne_v5_du_juge(ENV_ARGON_V5.read_text(encoding="utf-8"))
    assert lu["juge"]["jetons"] == v5 and "$@" not in v5 and v5[4] == "1700" and "--delai-s" in v5


@pytest.mark.parametrize("ancien,nouveau,motif", [
    ("--provision-pensee-jetons 65536 --sans-config-pensee", "--provision-pensee-jetons 49152 --sans-config-pensee", "65536"),
    ("--sans-config-pensee --max-sortie-jetons 65536", "--sans-config-pensee --max-sortie-jetons 32768", "65536"),
    (" --sans-config-pensee --max-sortie-jetons", " --max-sortie-jetons", "drapeaux"),
    ("--provision-pensee-jetons 65536 --sans-config-pensee", "--provision-pensee 65536 --sans-config-pensee", "options"),
    ("--modele gemini-4-argon", "--modele gemini-4-carbon", "gemini-4-argon"),
    ("--delai-s 1680 --url-base http://127.0.0.1:8788/v1beta", "--delai-s 1680 --url-base http://127.0.0.1:8792/v1beta", "8788"),
    ("timeout -k 20 1720", "timeout -k 20 1790", "timeout"),
    ("--delai-s 1500 --prix-entree", "--delai-s 1600 --prix-entree", "v5"),                                   # juge changé
    ("--provision-outil-jetons 32768 --url-base", "--provision-outil-jetons 32768 --provision-pensee-jetons 65536 --url-base", "v5"),
    ("--max-requetes-web-pire-cas 20 --provision-outil-jetons", "--max-requetes-web-pire-cas 20 \"$@\" --provision-outil-jetons", "arguments du noyau"),
    ("proposeur_ideation)\nexec", "juge_ideation)\nexec", "étiquette"),
    ('*)\necho', '*)\nexec /bin/true\necho', "exec"),
    ('case "${ROLE_POLE:-}" in', 'case "${ROLE:-}" in', "ROLE_POLE"),
    ('if [ "$#" -ne 0 ]', 'if [ "1" -ne 1 ]', "argument"),
    ("argon-recherche-v1/commande_argon_v3d.py\"", "argon-recherche-v1/commande_argon_v3c.py\"", "commande d'Argon épinglée"),
])
def test_reglage_argon_artefacts_refuses(tmp_path, ancien, nouveau, motif):
    pieces = _pieces_argon(tmp_path, ancien, nouveau)
    with pytest.raises(L.Refus, match=motif):
        L.controler_reglage_argon(_bloc_argon(pieces), pieces)


def test_declaration_d_argon_artefacts():
    pieces = _pieces_reelles()
    for autre in (["bash", str(ENV_ARGON_V5)], ["bash", pieces["enveloppe_argon_sans_troncature"]["absolu"], "--x"],
                  ["/bin/bash", pieces["enveloppe_argon_sans_troncature"]["absolu"]]):
        with pytest.raises(L.Refus, match="exactement"):
            L.controler_reglage_argon(_bloc_argon(pieces, commande=autre), pieces)


def test_declaration_argon_v5_refusee_par_le_lanceur(monde, capsys):
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["commande"] = ["bash", str(monde["depot"] / L.PIECES["enveloppe_argon"][0])]
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert lancer(monde["r"]) == 2 and "fournisseurs.argon.commande" in capsys.readouterr().err


def _lancer_enveloppe_d_essai(tmp_path, role, plafond, *options):
    """L'enveloppe d'Argon à l'octet, sauf l'adresse (faux amont local) : aucun port de course employé."""
    fa = subprocess.Popen([sys.executable, "-I", "-B", str(FAUX_AMONT), "--port", "0", "--journal", str(tmp_path / "j.jsonl"),
                           *options], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    try:
        url = fa.stdout.readline().strip().split(" ", 1)[1]
        t = ENV_ARGON.read_text(encoding="utf-8")
        assert t.count("--url-base http://127.0.0.1:8788/v1beta") == 2
        p = tmp_path / "argon-essai.sh"
        p.write_text(t.replace("--url-base http://127.0.0.1:8788/v1beta", f"--url-base {url}/v1beta"), encoding="utf-8")
        env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": plafond, "ROLE_POLE": role,
               "HOME": str(tmp_path)}
        q = subprocess.run(["bash", str(p)], input="consigne d'essai".encode(), capture_output=True, env=env, timeout=120)
    finally:
        fa.kill()
    lignes = (tmp_path / "j.jsonl").read_text().splitlines() if (tmp_path / "j.jsonl").exists() else []
    return q.returncode, json.loads(q.stdout.decode().strip().splitlines()[-1]), [json.loads(x) for x in lignes]


def test_enveloppe_argon_proposeur_sans_troncature_par_le_faux_amont(tmp_path):
    code, o, req = _lancer_enveloppe_d_essai(tmp_path, "proposeur_ideation", "6.05", "--pensees", "30000", "--candidats", "3000")
    assert code == 0 and o["code"] == 0 and o["fin"] == "STOP" and o["max_sortie_jetons"] == 65536 and o["config_pensee"] is False
    gc = req[1]["corps"]["generationConfig"]
    assert gc == {"maxOutputTokens": 65536} and "gemini-4-argon:generateContent" in req[1]["chemin"]


def test_enveloppe_argon_juge_comme_la_v5_par_le_faux_amont(tmp_path):
    code, o, req = _lancer_enveloppe_d_essai(tmp_path, "juge_ideation", "0.6")
    gc = req[1]["corps"]["generationConfig"]
    assert code == 0 and o["provision_pensee_jetons"] == 8192 and gc["thinkingConfig"] == {"thinkingBudget": 8192}
    assert gc["maxOutputTokens"] == o["max_sortie_jetons"] < 14000                    # réduite par la garde sous 0,60 USD


def test_enveloppe_argon_role_inconnu_refuse(tmp_path):
    code, o, req = _lancer_enveloppe_d_essai(tmp_path, "lecteur", "0.6")
    assert code == 2 and o["cout_usd"] == 1e-06 and req == []


def test_pire_cas_sans_troncature_aux_deux_comptes():
    pieces = _pieces_reelles()
    e = {"rang": 1, "nom": "x", "octets": 136265, "caracteres": 130101, "sha256": "e" * 64}
    for nom, c in (("Argon", L.controler_reglage_argon(_bloc_argon(pieces), pieces)),
                   ("Carbon", L.controler_reglage_carbon(_bloc(pieces), pieces, None))):
        p = L.pire_cas_sans_troncature(c, e, 6.05, nom)
        assert p["au_compte_de_la_commande"]["max_output_tokens"] == p["borne_prudente_octets_sur_2"]["max_output_tokens"] == 65536
        assert p["au_compte_de_la_commande"]["pire_cas_usd"] == pytest.approx(5.817437, abs=1e-6)
        assert p["pire_cas_usd"] == pytest.approx(6.03327, abs=1e-6) and p["pire_cas_usd"] <= 6.05
        with pytest.raises(L.Refus, match="6.04"):
            L.pire_cas_sans_troncature(c, e, 6.0, nom)                 # l'ancien plafond : la borne prudente réduirait la sortie
        assert L.pire_cas_sans_troncature(c, e, 6.04, nom)["max_output_tokens"] == 65536


def test_bornes_du_relais_d_argon_inchangees():
    assert L.appels_relais_gemini_requis(231) == 464 and L.APPELS_RELAIS_PAR_APPEL_GEMINI == 2 and L.MARGE_APPELS_RELAIS_GEMINI == 2
    assert inspect.getsource(L.controler_relais_argon) == inspect.getsource(L7.controler_relais_argon)


def test_mutation_juge_non_compare_a_la_v5_attrapee(tmp_path):
    M = _mutant_lanceur(tmp_path, '    if lu["juge"]["jetons"] != v5:\n', "    if False:\n", "lanceur_v9_mutant_juge")
    pieces = _pieces_argon(tmp_path, "--delai-s 1500 --prix-entree", "--delai-s 1600 --prix-entree")
    assert M.controler_reglage_argon(_bloc_argon(pieces), pieces)["juge"]["delai_s"] == 1600.0     # muté : juge changé admis
    with pytest.raises(L.Refus):
        L.controler_reglage_argon(_bloc_argon(pieces), pieces)


def test_mutation_borne_prudente_non_exigee_attrapee(tmp_path):
    M = _mutant_lanceur(tmp_path, '    for nom, g in (("au compte de la commande", cmd), ("à la borne prudente", prudent)):\n',
                        '    for nom, g in (("au compte de la commande", cmd),):\n', "lanceur_v9_mutant_prudente")
    pieces = _pieces_reelles()
    c = L.controler_reglage_argon(_bloc_argon(pieces), pieces)
    e = {"rang": 1, "nom": "x", "octets": 136265, "caracteres": 130101, "sha256": "e" * 64}
    assert M.pire_cas_sans_troncature(c, e, 6.0, "Argon")["max_output_tokens"] == 65536   # muté : 6,00 accepté
    with pytest.raises(L.Refus):
        L.pire_cas_sans_troncature(c, e, 6.0, "Argon")


def test_mutation_controle_d_argon_non_appele_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, '    argon = controler_reglage_argon(decl_brute["fournisseurs"]["argon"], pieces)',
                        '    argon = {"valeurs": REGLAGE_ARGON_PROPOSEUR}', "lanceur_v9_mutant_argon")
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["commande"] = ["bash", str(monde["depot"] / L.PIECES["enveloppe_argon"][0])]
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert M.principal([], reglages=monde["r"]) == 0                          # muté : Argon v5 (tronqué) partirait
    _rejouer(monde)
    assert lancer(monde["r"]) == 2


@avec_commandes
def test_gabarit_v2h_rempli_argon_et_carbon_sans_troncature(monde):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    for nom, regle in (("argon_regle", L.REGLAGE_ARGON_PROPOSEUR), ("carbon_regle", L.REGLAGE_CARBON)):
        assert dep[nom]["valeurs"] == regle and dep[nom]["pire_cas"]["max_output_tokens"] == 65536
        assert dep[nom]["pire_cas"]["pire_cas_usd"] == pytest.approx(6.03327, abs=1e-6)
    assert dep["parts_au_pire"]["carbon"]["part_au_pire_usd"] == pytest.approx(66.55)
    assert dep["parts_au_pire"]["astra"]["part_au_pire_usd"] == pytest.approx(66.55)
    assert dep["parts_au_pire"]["argon"]["part_au_pire_usd"] == 150.0 and dep["sonde_carbon_du_jour"]["exigee"] is True


# configuration v4, sonde de Carbon relue à 6,00 ---------------------------------------------------------------------------------------


def test_configuration_v4_plafond_6_05_et_rien_d_autre():
    v3 = json.loads((RACINE / L7.PIECES["configuration"][0]).read_text(encoding="utf-8"))
    v4 = json.loads((RACINE / L8.PIECES["configuration"][0]).read_text(encoding="utf-8"))   # v9 : la v4, celle de la v8
    assert (v3["plafonds_session"]["proposeur"], v4["plafonds_session"]["proposeur"]) == (6.0, 6.05)
    for c in (v3, v4):
        for k in ("version", "statut"):
            c.pop(k)
        c["plafonds_session"].pop("proposeur")
    assert v3 == v4
    with pytest.raises(L.Refus):
        L.garde_configuration_fixe(json.loads((RACINE / L7.PIECES["configuration"][0]).read_text(encoding="utf-8")))
    with pytest.raises(L.Refus):
        L.garde_configuration_fixe(json.loads((RACINE / L8.PIECES["configuration"][0]).read_text(encoding="utf-8")))


@avec_commandes
def test_sonde_de_carbon_relue_au_plafond_de_sonde(monde, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    sonde_carbon(monde, plafond_session_usd=6.05)                  # la sonde (v1) joue sous 6,00 : un rapport à 6,05 est faux
    assert lancer(monde["r"]) == 2 and "plafond" in capsys.readouterr().err


# constantes v8 et rien d'autre ne change ----------------------------------------------------------------------------------------


CHANGEES_V8 = {"verifier_additif", "verifier_contre_lecture", "charger_epreuve", "ecrire_registre_derive", "acte_de_gel", "executer",
               "reglages_a_blanc", "verifier_sonde_carbon", "rapport_sonde_carbon_d_essai", "charger_commande_argon",
               "verifier_course_jamais_lancee_ou_closes_admises"}


def test_constantes_v8_portees_sur_la_v8():
    assert L8.SORTIES_AUTRES_VERSIONS == tuple(Path(f"/home/user/sorties-course-auto-conception-v{k}") for k in range(1, 8))
    assert L8.DOSSIER_SORTIES == Path("/home/user/sorties-course-auto-conception-v8") and L8.SUFFIXE_RUN == "-course-auto-conception-v8"
    assert set(L8.SUFFIXES_DEJA_LANCEE) == {f"-course-auto-conception-v{k}" for k in range(1, 9)}
    assert (L8.PLAFOND_ARRET_USD, L8.PLAFOND_SESSION_PROPOSEUR_USD, L8.PLAFOND_SONDE_CARBON_USD) == (120.0, 6.05, 6.0)
    assert L8.ADDITIF_V2G == (L7.ADDITIF, L7.ADDITIF_SHA256)
    for neuf in (L8.EPREUVE_REELLE, L8.CONTRE_LECTURE, L8.DECLARATION_RELAIS, L8.ADDITIF, L8.PIECE_DE_DEPART, L8.RELEVE_PRIX, L8.RELEVE_CREDITS):
        assert neuf.startswith(L8.COURSE_V4 + "/") and neuf not in (L7.EPREUVE_REELLE, L7.CONTRE_LECTURE, L7.DECLARATION_RELAIS,
                                                                   L7.ADDITIF, L7.PIECE_DE_DEPART, L7.RELEVE_PRIX, L7.RELEVE_CREDITS)
    changees = {"configuration", "epreuve_temoins"}
    assert {k: v for k, v in L8.PIECES.items() if k not in changees | {"enveloppe_argon_sans_troncature"}} == \
        {k: v for k, v in L7.PIECES.items() if k not in changees}
    for nom in ("MATIERE", "PROGRAMMES_RELAIS", "PORTS_RELAIS_EXTERNES", "EMPREINTES_ORCHESTRATEUR", "COMMIT_ORCHESTRATEUR",
                "PIECES_SERVIES", "ETIQUETTES_INTERDITES_FIXES", "FOURNISSEURS_DISPENSABLES", "TYPES_PERMIS", "CLES_PERMISES",
                "PREREG_SHA256", "PORT_RELAIS_ARGON", "MODELE_ARGON", "APPELS_RELAIS_PAR_APPEL_GEMINI", "MARGE_APPELS_RELAIS_GEMINI",
                "ADDITIF_V2C", "ADDITIF_V2D", "ADDITIF_V2E", "ADDITIF_V2F", "MOTS_TENTATIVE_NEUVE", "LIGNES_GO_CONSOMMEES",
                "COURSES_CLOSES_ADMISES", "COURSE_CLOSE_CITEE", "REGLAGE_CARBON", "DRAPEAUX_CARBON", "TIMEOUT_ENVELOPPE_CARBON",
                "CLE_CLAUDE_TENTATIVE", "CLES_CLAUDE_REFUSEES", "PLAFOND_SONDE_CARBON_USD", "PLAFOND_ARRET_USD"):
        assert getattr(L8, nom) == getattr(L7, nom), nom
    for nom, objet in vars(L7).items():
        if (inspect.isfunction(objet) or inspect.isclass(objet)) and getattr(objet, "__module__", None) == L7.__name__ \
                and nom not in CHANGEES_V8:
            assert inspect.getsource(getattr(L8, nom)) == inspect.getsource(objet), nom


def _essai_a_blanc_v8_remplace_par_v9():
    """(v9) remplacé par `test_essai_a_blanc_v9`."""


# --- (b) point 3 : la course place-t-elle les dossiers des agents sous un chemin interdit ? --------------------------------------


def _orchestrateur_reel():
    presents = [Path(o) for o in L.ORCHESTRATEURS_CANDIDATS if (Path(o) / L.LANCEUR_ORCHESTRATEUR).is_file()]
    return presents[0] if len(presents) == 1 else None


ORCH_REEL = _orchestrateur_reel()
avec_orchestrateur = pytest.mark.skipif(ORCH_REEL is None, reason="copie de l'orchestrateur épinglé absente")


def _v8_reel(nom):
    if str(ORCH_REEL) not in sys.path:
        sys.path.insert(0, str(ORCH_REEL))
    spec = importlib.util.spec_from_file_location(nom, ORCH_REEL / L.LANCEUR_ORCHESTRATEUR)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def jouer_la_course_par_le_vrai_noyau(conf_chemin: Path, tmp_path: Path, monkeypatch) -> dict:
    """La course 2 de l'orchestrateur épinglé (`ideation_v8.principal`, `--moteur simule`), dans ce processus, sur la
    configuration assemblée par le lanceur v3 : le noyau, ses sessions et ses gardes sont les vrais ; seuls les appels sont
    simulés. On relève chaque dossier d'agent (`OrchestreV55.session`) et chaque appel (fournisseur, rôle du kit, dossier)."""
    v8 = _v8_reel("ideation_v8_pour_essai_course_v3")
    from pole import noyau_v55
    from pole.simulation_v56 import AdaptateurSimuleV56
    vus, sessions, capte = [], {}, {}
    lancer_orig, session_orig, simules_orig = AdaptateurSimuleV56.lancer, noyau_v55.OrchestreV55.session, v8.adaptateurs_simules
    executer_orig = v8.c2.executer_course_v56

    def lancer_releve(self, role, consigne, dossier, budget_usd, max_tours, modele=None, **kw):
        vus.append({"fournisseur": getattr(self, "_fournisseur_essai", None), "role_kit": role, "dossier": dossier, "modele": modele})
        return lancer_orig(self, role, consigne, dossier, budget_usd, max_tours, modele=modele, **kw)

    def session_relevee(self, *logique):
        d = session_orig(self, *logique)
        sessions[d] = tuple(str(x) for x in logique)
        return d

    def simules_etiquetes(conf, fournisseurs):
        ads = simules_orig(conf, fournisseurs)
        for n, a in ads.items():
            a._fournisseur_essai = n
        return ads

    def executer_capte(conf, sortie, *a, **kw):
        capte.update(sortie=sortie, base=kw.get("racine_sessions"))
        return executer_orig(conf, sortie, *a, **kw)
    monkeypatch.setattr(AdaptateurSimuleV56, "lancer", lancer_releve)
    monkeypatch.setattr(noyau_v55.OrchestreV55, "session", session_relevee)
    monkeypatch.setattr(v8, "adaptateurs_simules", simules_etiquetes)
    monkeypatch.setattr(v8.c2, "executer_course_v56", executer_capte)
    (tmp_path / "tmp-course").mkdir()
    monkeypatch.setattr(tempfile, "tempdir", str(tmp_path / "tmp-course"))
    sortie = tmp_path / "sorties-course-essai" / "id-essai" / "sortie"
    sortie.parent.mkdir(parents=True)
    code = v8.principal(["--course-2", str(conf_chemin), str(sortie), "--generations", "1", "--moteur", "simule"])
    return {"code": code, "v8": v8, "vus": vus, "sessions": sessions, "sortie": capte["sortie"], "base": capte["base"],
            "conf": json.loads(conf_chemin.read_text(encoding="utf-8"))}


def _sous_norme(chemin: str, racine: str) -> bool:
    chemin, racine = os.path.normpath(chemin), os.path.normpath(racine)
    return chemin == racine or chemin.startswith(racine.rstrip(os.sep) + os.sep)


@avec_orchestrateur
@avec_commandes
def test_course_dossiers_des_agents_sous_un_chemin_interdit_chaque_role(monde, tmp_path, monkeypatch):
    preparer_piece_reelle(monde)
    assert lancer(monde["r"]) == 0
    c = jouer_la_course_par_le_vrai_noyau(un_run(monde["r"]) / "configuration-orchestrateur.json", tmp_path, monkeypatch)
    assert c["code"] == 0 and c["vus"]
    # les adaptateurs réels, construits comme `executer` les construit en moteur réel, sur la même sortie et la même base
    ads, portes = c["v8"].adaptateurs_reels_v56(c["conf"], c["sortie"], c["base"])
    from pole.adaptateurs import AdaptateurClaudeSDK, construire_options
    from pole.adaptateurs_v56 import AdaptateurCommandeExterneV56, verifier_lecture_interdite
    from pole.noyau_v55 import verifier_emplacement_sessions
    assert sorted(ads) == ["argon", "astra", "carbon", "claude"] and sorted(portes) == sorted(ads)
    claude = ads["claude"]
    assert isinstance(claude, AdaptateurClaudeSDK)
    assert all(isinstance(ads[n], AdaptateurCommandeExterneV56) for n in ("argon", "astra", "carbon"))
    base_reelle, sortie_reelle = os.path.realpath(c["base"]), os.path.realpath(os.path.abspath(c["sortie"]))
    assert claude.interdire_lecture == [base_reelle, sortie_reelle]
    racine = verifier_emplacement_sessions(os.path.join(c["base"], "generation-1"), c["sortie"])
    assert set(verifier_lecture_interdite(claude, c["sortie"], racine)) == {"proposeur_ideation", "juge_ideation"}
    # chaque appel de la course : dossier sous la racine des sessions (base interdite), hors de la sortie ; le kit l'accepte
    dossiers = sorted({v["dossier"] for v in c["vus"]})
    roles = set()
    for v in c["vus"]:
        d = v["dossier"]
        logique = c["sessions"][d]
        roles.add((logique[0], logique[2] if logique[0] in ("proposition", "juges") else "aiguilleur", v["fournisseur"], v["role_kit"]))
        assert _sous_norme(d, racine) and _sous_norme(d, base_reelle) and not _sous_norme(d, sortie_reelle)
        o = construire_options(os.path.abspath(d), 1.0, 1, url_relais=claude.url_relais, role=v["role_kit"],
                               interdire_lecture=claude.interdire_lecture)
        fs = o["sandbox"]["filesystem"]
        assert fs["allowRead"] == [os.path.normpath(d)] and fs["denyRead"] == [base_reelle, sortie_reelle]
    for d in dossiers:  # aucun voisin lisible : chaque autre dossier est sous la base interdite et hors du seul dossier rouvert
        assert not any(_sous_norme(autre, d) for autre in dossiers if autre != d)
    attendus = {("proposition", "prop-opus", "claude", "proposeur_ideation"), ("proposition", "prop-fable", "claude", "proposeur_ideation"),
                ("proposition", "prop-argon", "argon", "proposeur_ideation"), ("proposition", "prop-astra", "astra", "proposeur_ideation"),
                ("proposition", "prop-carbon", "carbon", "proposeur_ideation"), ("aiguillage", "aiguilleur", "claude", "juge_ideation"),
                ("juges", "juge-opus", "claude", "juge_ideation"), ("juges", "juge-argon", "argon", "juge_ideation")}
    assert attendus <= roles, sorted(attendus - roles)
    assert len(c["vus"]) == len(dossiers)  # une session neuve par appel


@avec_orchestrateur
def test_course_artefacts_sessions_hors_des_chemins_interdits_refusees(tmp_path):
    """R5 : un dossier d'agent hors de la base des sessions et de la sortie → la garde de l'orchestrateur refuse ; une base de
    sessions sous la sortie → refusée par le noyau (CL19-04)."""
    v8 = _v8_reel("ideation_v8_pour_essai_course_v3_artefact")
    from pole.adaptateurs import construire_options
    from pole.noyau_v55 import SessionsMalPlacees, verifier_emplacement_sessions
    sortie, base = tmp_path / "x" / "sortie", tmp_path / "base"
    sortie.parent.mkdir()
    base.mkdir()
    ads, _ = v8.adaptateurs_reels_v56({"fournisseurs": {"claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787",
                                                                   "porte_plafond": {"type": "commande", "commande": ["/bin/false"],
                                                                                     "delai_s": 5}}}}, str(sortie), str(base))
    claude = ads["claude"]
    construire_options(str(base / "generation-1" / "sessions" / "abc"), 1.0, 1, url_relais=claude.url_relais,
                       role="juge_ideation", interdire_lecture=claude.interdire_lecture)        # sain
    with pytest.raises(ValueError, match="doit être sous un chemin interdit en lecture"):
        construire_options(str(tmp_path / "x" / "sessions" / "abc"), 1.0, 1, url_relais=claude.url_relais,
                           role="juge_ideation", interdire_lecture=claude.interdire_lecture)
    with pytest.raises(SessionsMalPlacees):
        verifier_emplacement_sessions(str(sortie / "sessions-base"), str(sortie))


# --- v4 : correctif v2d — bornes des relais Gemini, verdict requalifié ----------------------------------------------------------


def test_regle_des_bornes_gemini_chiffree():
    assert L.APPELS_RELAIS_PAR_APPEL_GEMINI == 2 and L.MARGE_APPELS_RELAIS_GEMINI == 2
    assert L.appels_argon_au_pire(FIXE, 11, [e for e in FIXE["especes"] if e["fournisseur"] != "kimi"], FIXE["cartes_max_comptees"]) == 231
    assert L.appels_argon_au_pire(FIXE, 11, FIXE["especes"], FIXE["cartes_max_comptees"]) == 275 and L.appels_relais_gemini_requis(275) == 552
    assert L.appels_relais_gemini_requis(231) == 464 and L.appels_relais_gemini_requis(143) == 288
    assert L.appels_relais_gemini_requis(11) == 24


@pytest.mark.parametrize("borne,code", [(287, 2), (288, 0), (300, 0)])
def test_relais_argon_trois_especes_borne_doublee(monde, borne, code, capsys):
    c = monde["cmdlines"][PID_ARGON]
    c[c.index("--max-appels") + 1] = str(borne)
    monde["etat_argon"]["max_appels"] = borne
    assert lancer(monde["r"]) == code
    if code:
        assert "288" in capsys.readouterr().err


@avec_commandes
@pytest.mark.parametrize("borne,code", [(280, 2), (463, 2), (464, 0)])
def test_relais_argon_avec_astra_et_carbon_borne_doublee(monde, borne, code, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    c = monde["cmdlines"][PID_ARGON]
    c[c.index("--max-appels") + 1] = str(borne)
    monde["etat_argon"]["max_appels"] = borne
    assert lancer(monde["r"]) == code
    if code:
        err = capsys.readouterr().err
        assert "464" in err and "countTokens" in err


def _incidents_tous(etiquettes=("aiguilleur", "juge-opus", "juge-argon")):
    temoins = {t["id"] for t in json.loads((RACINE / L.PIECES["temoins"][0]).read_text())["temoins"]}
    return {e: {t: {"statut": "erreur"} for t in temoins} for e in etiquettes}


def test_rapport_non_conclu_pour_manques_techniques_recalcule_et_refuse(monde, capsys):
    """Un rapport v4 « non conclue » (tous les manques techniques) : le lanceur recalcule « non conclue » (pas d'écart) et
    refuse comme tout verdict non « réussi » ; sans les incidents, le même rapport est un écart (recalcul « échouée »)."""
    e = epreuve(monde["lanceur_sha"], monde["commit"], verdict="non conclue", incidents_techniques=_incidents_tous())
    for j in e["verdicts"]:
        e["verdicts"][j] = {t: None for t in e["verdicts"][j]}
    e["classes"] = {t: None for t in e["classes"]}
    _ecrire(monde, L.EPREUVE_REELLE, e)
    assert lancer(monde["r"]) == 2
    err = capsys.readouterr().err
    assert "verdict 'non conclue'" in err and "recalculé" not in err
    del e["incidents_techniques"]
    _ecrire(monde, L.EPREUVE_REELLE, e)
    assert lancer(monde["r"]) == 2 and "recalculé 'échouée'" in capsys.readouterr().err


def test_requalification_ne_fabrique_jamais_reussie(monde, capsys):
    """Un rapport « réussie » forgé dont un juge n'a rien rendu (incident déclaré) : recalcul « non conclue » → refus."""
    e = epreuve(monde["lanceur_sha"], monde["commit"], incidents_techniques=_incidents_tous(("juge-argon",)))
    e["verdicts"]["juge-argon"] = {t: None for t in e["verdicts"]["juge-argon"]}
    _ecrire(monde, L.EPREUVE_REELLE, e)
    assert lancer(monde["r"]) == 2 and "recalculé 'non conclue'" in capsys.readouterr().err


def test_manque_non_technique_a_cote_reste_echouee(monde, capsys):
    e = epreuve(monde["lanceur_sha"], monde["commit"], verdict="non conclue", incidents_techniques=_incidents_tous(("juge-opus",)))
    e["verdicts"]["juge-opus"] = {t: None for t in e["verdicts"]["juge-opus"]}
    e["verdicts"]["juge-argon"]["t06"]["items"]["voisin_nomme"] = True          # un verdict lu et faux
    _ecrire(monde, L.EPREUVE_REELLE, e)
    assert lancer(monde["r"]) == 2 and "recalculé 'échouée'" in capsys.readouterr().err



@avec_commandes
def test_mutation_borne_argon_non_doublee_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "    return APPELS_RELAIS_PAR_APPEL_GEMINI * int(appels) + MARGE_APPELS_RELAIS_GEMINI\n",
                        "    return int(appels)\n", "lanceur_v9_mutant_borne")
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    c = monde["cmdlines"][PID_ARGON]
    c[c.index("--max-appels") + 1] = "280"                                      # la borne des commandes v2c
    monde["etat_argon"]["max_appels"] = 280
    assert M.principal([], reglages=monde["r"]) == 0                          # muté : la course serait partie
    shutil.rmtree(monde["r"].dossier_runs)
    shutil.rmtree(monde["r"].dossier_sorties)
    assert lancer(monde["r"]) == 2


@avec_commandes
def test_mutation_carbon_non_double_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, '    requis = appels_relais_gemini_requis(appels_requis) if nom == "carbon" else appels_requis\n',
                        "    requis = appels_requis\n", "lanceur_v9_mutant_carbon")
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    monde["etat_carbon"]["max_appels"] = 15
    assert M.principal([], reglages=monde["r"]) == 0
    shutil.rmtree(monde["r"].dossier_runs)
    shutil.rmtree(monde["r"].dossier_sorties)
    assert lancer(monde["r"]) == 2


def test_mutation_recalcul_sans_requalification_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "    return E.qualifier_verdict(lecture, incidents, None, [], True)\n",
                        '    return lecture["verdict"]\n', "lanceur_v9_mutant_recalcul")
    e = epreuve(monde["lanceur_sha"], monde["commit"], verdict="non conclue", incidents_techniques=_incidents_tous())
    for j in e["verdicts"]:
        e["verdicts"][j] = {t: None for t in e["verdicts"][j]}
    e["classes"] = {t: None for t in e["classes"]}
    pieces = {"epreuve_temoins": {"absolu": str(RACINE / L.PIECES["epreuve_temoins"][0])},
              "temoins": {"absolu": str(RACINE / L.PIECES["temoins"][0])},
              "configuration": {"absolu": str(RACINE / L.PIECES["configuration"][0])}}
    assert L.recalculer_verdict_epreuve(e, pieces) == "non conclue"
    assert M.recalculer_verdict_epreuve(e, pieces) == "échouée"


# sonde d'Astra du jour, composition tenue --------------------------------------------------------------------------------------


@avec_commandes
@pytest.mark.parametrize("modifs,motif", [({"jour": "2026-11-17"}, "du jour"), ({"ok": False}, "non réussie"),
                                          ({"appel_envoye": False}, "non réussie"), ({"echec_de_configuration": True}, "non réussie"),
                                          ({"commande": {"sha256": "b" * 64}}, "non épinglée"), ({"version": "autre"}, "version")])
def test_sonde_astra_du_jour_artefacts(monde, modifs, motif, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    sonde_astra(monde, COMMANDES_MAIN["astra"][1], **modifs)
    assert lancer(monde["r"]) == 2 and motif in capsys.readouterr().err


@avec_commandes
def test_sonde_astra_non_scellee_ou_absente_refusee(monde):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    Path(str(monde["depot"] / SONDE_REL) + ".sha256").unlink()
    assert lancer(monde["r"]) == 2
    (monde["depot"] / SONDE_REL).unlink()
    assert lancer(monde["r"]) == 2
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie(astra={"sonde_du_jour_rapport": None}))
    with pytest.raises(L.Refus, match="sonde_du_jour_rapport"):
        L.verifier_piece_de_depart(monde["r"])


@avec_commandes
def test_sonde_astra_saine_au_manifeste(monde):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["sonde_astra_du_jour"]["exigee"] is True and dep["sonde_astra_du_jour"]["jour"] == "2026-11-18"


@avec_commandes
def test_mutation_sonde_sans_jour_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, '    if o.get("jour") != aujourd_hui.isoformat():\n        motifs.append(f"sonde du {o.get(\'jour\')!r}, du jour ({aujourd_hui}) exigée")\n    if (o.get("commande")',
                        '    if False:\n        motifs.append(f"sonde du {o.get(\'jour\')!r}, du jour ({aujourd_hui}) exigée")\n    if (o.get("commande")',
                        "lanceur_v9_mutant_sonde")
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    sonde_astra(monde, COMMANDES_MAIN["astra"][1], jour="2026-11-17")       # la sonde de la veille
    assert M.principal([], reglages=monde["r"]) == 0
    shutil.rmtree(monde["r"].dossier_runs)
    shutil.rmtree(monde["r"].dossier_sorties)
    assert lancer(monde["r"]) == 2


@avec_commandes
def test_composition_tenue_espece_omise_refusee(monde, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    d = json.loads((monde["depot"] / L.DECLARATION_RELAIS).read_text(encoding="utf-8"))
    del d["fournisseurs"]["carbon"]
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert lancer(monde["r"]) == 2 and "composition" in capsys.readouterr().err


@avec_commandes
def test_mutation_composition_non_tenue_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "    if manquantes:\n        raise Refus(f\"composition :",
                        "    if False:\n        raise Refus(f\"composition :", "lanceur_v9_mutant_composition")
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    d = json.loads((monde["depot"] / L.DECLARATION_RELAIS).read_text(encoding="utf-8"))
    del d["fournisseurs"]["carbon"]
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert M.principal([], reglages=monde["r"]) == 0                          # muté : Carbon « absente » en silence
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-carbon" not in dep["especes_actives"]


# --- v9 : plafond d'arrêt 150 USD, seuils au haut, conservation des réponses brutes, inventaire de fin --------------------------


L8 = _charger_module("lancer_course_auto_conception_v8_pour_essai_v9", RACINE / "scripts" / "lancer_course_auto_conception_v8.py")
SHA_EPREUVE_V8 = L8.PIECES["epreuve_temoins"][1]
CONF_V4 = json.loads((RACINE / L8.PIECES["configuration"][0]).read_text(encoding="utf-8"))
CONF_V5 = json.loads((RACINE / L.PIECES["configuration"][0]).read_text(encoding="utf-8"))
ESTIMATION_V2I = {"proposition": 44.641339, "aiguillage": 3.41, "juges": 7.887}


def _conf(base=None, **etapes):
    f = json.loads(json.dumps(base or CONF_V5))
    for nom, champs in etapes.items():
        if nom == "budget":
            f["budget"].update(champs)
            continue
        e = next(x for x in f["budget"]["etapes"] if x["nom"] == nom)
        e.update(champs)
    return f


def _conf_au_depot(monde, f):
    rel = L.PIECES["configuration"][0]
    p = monde["depot"] / rel
    p.write_text(json.dumps(f, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sha = L.sha256_fichier(p)
    monde["r"].pieces["configuration"] = (rel, sha)
    chemin = monde["r"].additif[0]                      # l'additif d'essai cite la configuration ; la contre-lecture, l'additif
    ecrire_scelle(chemin, additif(monde["prereg_sha"], configuration=sha))
    monde["r"].additif = (chemin, L.sha256_fichier(chemin))
    _ecrire(monde, L.CONTRE_LECTURE, contre_lecture(monde["r"].additif[1], monde["lanceur_sha"]))


def test_v9_bout_en_bout_150_seuils_et_conservation(monde):
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    assert run.name.endswith("-course-auto-conception-v9")
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert dep["additif_v2i"]["sha256"] == monde["additif_sha"] and dep["lanceur"]["version"] == "lancer_course_auto_conception_v9"
    assert dep["additifs_cites"]["v2h"] == {"chemin": L8.ADDITIF, "sha256": L8.ADDITIF_SHA256}
    acte = (run / "acte-de-gel.md").read_text()
    assert monde["additif_sha"] in acte and "additif v2i" in acte.lower() and "150 USD" in acte and "6,05 USD" in acte
    assert dep["pieces"]["epreuve_temoins"]["chemin"] == "scripts/epreuve_temoins_auto_conception_v9.py"
    assert dep["pieces"]["configuration"]["chemin"].endswith("course-v4/configuration-course-auto-conception-v5.json")
    assert dep["pieces"]["enveloppe_conservation"]["chemin"] == "scripts/enveloppe_conservation_reponses_v1.py"
    assert dep["epreuve_reelle_des_temoins"]["chemin"].endswith("course-v4/epreuve-temoins-reelle-auto-conception-v9.json")
    assert dep["declaration_relais"]["chemin"].endswith("course-v4/declaration-relais-course-auto-conception-v9.json")
    assert dep["go"]["plafond_lu"] == 150.0 and dep["verification_orchestrateur"]["montant_requis_go_usd"] == 150.0
    assert dep["plafond_arret_usd"] == 150.0 and dep["parts_au_pire"]["claude"]["part_au_pire_usd"] == 150.0
    s = dep["seuils_internes_au_haut"]["lecture"]
    assert all(s[n]["etat"] == "jouee" for n in ("proposition", "aiguillage", "juges"))
    sortie = Path(dep["sortie"])
    assert dep["conservation"]["dossier"] == str(sortie.parent / "conservation-reponses-v1") and Path(dep["conservation"]["dossier"]).is_dir()
    inv = run / "inventaire-conservation.json"
    assert L.scelle(inv) and fin["inventaire_conservation"]["sha256"] == L.sha256_fichier(inv)
    o = json.loads(inv.read_text())
    assert o["rien_supprime"] is True and o["issue"]["code"] == 0
    assert o["parties"]["sorties_orchestrateur"]["nombre"] >= 4 and o["parties"]["conservation_reponses"]["present"] is True
    vu = json.loads((sortie / "vu.json").read_text())
    assert "argon" in vu["fournisseurs"]


def test_ligne_de_la_course_a_120_refusee_150_acceptee(monde, capsys):
    monde["main"]["registres/go.md"] = registre(plafond_c="120 USD").encode("utf-8")
    assert lancer(monde["r"]) == 2 and "150" in capsys.readouterr().err
    monde["main"]["registres/go.md"] = registre().encode("utf-8")
    assert lancer(monde["r"]) == 0


# configuration v5 et seuils internes -------------------------------------------------------------------------------------------


def test_configuration_v5_plafond_150_et_rien_d_autre():
    v4, v5 = json.loads(json.dumps(CONF_V4)), json.loads(json.dumps(CONF_V5))
    assert (v4["budget"]["plafond_usd"], v5["budget"]["plafond_usd"]) == (120.0, 150.0)
    assert (v4["relais_persistants"]["plafond_relais_claude_usd"], v5["relais_persistants"]["plafond_relais_claude_usd"]) == (120.0, 150.0)
    sac = lambda c: [e["plafond_relais_usd"] for e in c["budget"]["etapes"] if e["role"] == "sacrifiable"]  # noqa: E731
    assert (sac(v4), sac(v5)) == ([121.0, 121.0], [151.0, 151.0])
    prot = lambda c: [(e["nom"], e["attendu_usd"], e["plafond_relais_usd"]) for e in c["budget"]["etapes"] if e["role"] == "protegee"]  # noqa: E731
    assert prot(v4) == prot(v5) == [("proposition", 19.0, 45.0), ("aiguillage", 3.0, 15.0), ("juges", 7.0, 30.0), ("etiquettes", 0.0, 0.0)]
    assert v5["plafonds_session"]["proposeur"] == 6.05 and "Course à 150 USD (Recommandé)" in v5["statut"]
    for c in (v4, v5):
        for k in ("version", "statut"):
            c.pop(k)
        c["budget"].pop("plafond_usd")
        c["relais_persistants"].pop("plafond_relais_claude_usd")
        for e in c["budget"]["etapes"]:
            if e["role"] == "sacrifiable":
                e.pop("plafond_relais_usd")
    assert v4 == v5
    L.garde_configuration_fixe(CONF_V5)
    with pytest.raises(L.Refus, match="150"):
        L.garde_configuration_fixe(CONF_V4)


def test_seuils_internes_releves_d_autant():
    """Les seuils de la règle d'A1 (S17 − plafond de relais de l'étape) montent de 30 USD avec S17 : 110 → 140, 105 → 135, 90 → 120."""
    for conf, (p, a, j) in ((CONF_V4, (110.0, 105.0, 90.0)), (CONF_V5, (140.0, 135.0, 120.0))):
        lec = L.lecture_a1(conf, {})
        assert lec["proposition"]["plafond_dur_usd"] == p
        assert (lec["aiguillage"]["seuil_cumul_usd"], lec["juges"]["seuil_cumul_usd"]) == (a, j)
        assert lec["passe_tableau"]["etat"] == lec["fusions"]["etat"] == "retiree"


def test_garde_seuils_au_haut_saine_v5_et_v4_refusee():
    g = L.garde_seuils_au_haut(CONF_V5)
    lec = g["lecture"]
    assert [lec[n]["etat"] for n in ("proposition", "aiguillage", "juges")] == ["jouee"] * 3
    assert (lec["proposition"]["plafond_dur_usd"], lec["aiguillage"]["plafond_dur_usd"], lec["juges"]["plafond_dur_usd"]) == (140.0, 72.96, 59.5)
    assert lec["juges"]["cumul_avant_usd"] == pytest.approx(90.491788) and g["cumul_au_haut_usd"] == pytest.approx(137.813788)
    v4 = L.lecture_a1(CONF_V4, L.HAUT_DEVIS_V2I_USD)                       # le constat du devis v2h : juges non lancés à 120
    assert v4["aiguillage"]["etat"] == "jouee" and v4["juges"]["etat"] == "non_mesuree"
    with pytest.raises(L.Refus, match="juges"):
        L.garde_seuils_au_haut(CONF_V4)


@pytest.mark.parametrize("conf,motif", [
    (_conf(juges={"plafond_relais_usd": 61.0}), "juges"),                      # 90,49 + 61 > 150 : juges non lancés
    (_conf(aiguillage={"plafond_relais_usd": 80.0}), "aiguillage"),            # 70,03 + 80 > 150 : aiguillage non lancé
    (_conf(budget={"plafond_usd": 135.0}), "juges"),                          # juges lancés, plafond dur 44,51 < 47,32 : coupés
    (_conf(proposition={"plafond_relais_usd": 151.0}), "proposition"),        # proposition non lancée
])
def test_garde_seuils_au_haut_artefacts_refuses(conf, motif):
    with pytest.raises(L.Refus, match=motif):
        L.garde_seuils_au_haut(conf)


def test_lecture_a1_refuse_une_etape_reductible():
    f = _conf(juges={"role": "reductible", "rang": 3, "reduite": {"attendu_usd": 1.0, "plafond_relais_usd": 5.0}})
    with pytest.raises(L.Refus, match="réductible"):
        L.lecture_a1(f, {})


def _budget_v56():
    if str(ORCH_REEL) not in sys.path:
        sys.path.insert(0, str(ORCH_REEL))
    from pole.budget_v56 import BudgetV56, JOUER, NON_MESUREE
    return BudgetV56, JOUER, NON_MESUREE


@avec_orchestrateur
@pytest.mark.parametrize("couts", [L.HAUT_DEVIS_V2I_USD, ESTIMATION_V2I,
                                   {"proposition": 100.06352, "aiguillage": 20.46, "juges": 47.322},
                                   {"proposition": 140.0, "aiguillage": 20.46, "juges": 47.322},
                                   {"proposition": 110.0, "aiguillage": 20.0, "juges": 30.0},
                                   {"proposition": 70.031788, "aiguillage": 60.0, "juges": 19.0}])
@pytest.mark.parametrize("nom_conf", ["v4", "v5", "s135"])
def test_lecture_a1_egale_a_la_vraie_classe_budget_v56(couts, nom_conf):
    """La lecture du lanceur et la vraie classe `BudgetV56` de l'orchestrateur épinglé rendent les mêmes états et les mêmes
    plafonds durs, étape par étape (le second calcul des seuils du devis v2i)."""
    BudgetV56, JOUER, NON_MESUREE = _budget_v56()
    conf = {"v4": CONF_V4, "v5": CONF_V5, "s135": _conf(budget={"plafond_usd": 135.0})}[nom_conf]
    b = conf["budget"]
    budget = BudgetV56(b["plafond_usd"], b["arret_etape_usd"], b["etapes"])
    vrai = {}
    for nom in budget.ordre:
        d, detail = budget.avant_etape(nom)
        if d == JOUER:
            etat = budget.apres_etape(nom, float(couts.get(nom, 0.0)))
            vrai[nom] = (etat, detail["plafond_dur_usd"])
        else:
            vrai[nom] = (d, None)
        if not budget.etat()["c13_satisfaite"]:
            break
    lu = L.lecture_a1(conf, couts)
    traduit = {"jouee": "jouee", "retiree": "retiree", "non_mesuree": NON_MESUREE, "coupee": NON_MESUREE}
    assert list(lu) == list(vrai)
    for nom, (etat, dur) in vrai.items():
        assert traduit[lu[nom]["etat"]] == etat, (nom, lu[nom], etat)
        if lu[nom]["etat"] in ("jouee", "coupee"):
            assert lu[nom]["plafond_dur_usd"] == dur, nom


def test_mutation_garde_des_seuils_non_appelee_attrapee(monde, tmp_path, capsys):
    M = _mutant_lanceur(tmp_path, "    seuils = garde_seuils_au_haut(fixe)", "    seuils = {}", "lanceur_v9_mutant_seuils")
    _conf_au_depot(monde, _conf(juges={"plafond_relais_usd": 61.0}))
    assert M.principal([], reglages=monde["r"]) == 0                          # muté : les juges ne seraient pas lancés au haut
    _rejouer(monde)
    assert lancer(monde["r"]) == 2 and "seuils internes" in capsys.readouterr().err


def test_mutation_coupure_au_plafond_dur_non_lue_attrapee(tmp_path):
    M = _mutant_lanceur(tmp_path, "        if cout > dur + 1e-9:\n", "        if False:\n", "lanceur_v9_mutant_coupure")
    f = _conf(budget={"plafond_usd": 135.0})
    assert M.garde_seuils_au_haut(f)["lecture"]["juges"]["etat"] == "jouee"   # muté : juges coupés lus « joués »
    with pytest.raises(L.Refus):
        L.garde_seuils_au_haut(f)


def test_mutation_seuil_du_plafond_d_etape_non_lu_attrapee(tmp_path):
    M = _mutant_lanceur(tmp_path, "            if cumul + relais > s17 + 1e-9:\n                lecture[nom] = {\"etat\": \"non_mesuree\"",
                        "            if False:\n                lecture[nom] = {\"etat\": \"non_mesuree\"", "lanceur_v9_mutant_seuil")
    couts = {"proposition": 75.0, "aiguillage": 20.0, "juges": 25.0}           # cumul 95 avant les juges, seuil 90 (v4)
    assert M.lecture_a1(CONF_V4, couts)["juges"]["etat"] == "jouee"             # muté : le seuil de l'étape n'est plus lu
    assert L.lecture_a1(CONF_V4, couts)["juges"]["etat"] == "non_mesuree"


# conservation des réponses brutes, inventaire de fin (R-3661) ------------------------------------------------------------------


def test_envelopper_commandes_conservation_entre_la_garde_et_la_commande(tmp_path):
    decl = {"fournisseurs": {"claude": {"type": "claude_sdk"}, "astra": {"commande": ["py", "astra.py"]},
                             "argon": {"commande": ["bash", "argon.sh"]}}}
    d = L.envelopper_commandes(json.loads(json.dumps(decl)), "PY", Path("/g.py"), Path("/arrets"), Path("/c.py"), Path("/cons"))
    assert d["fournisseurs"]["astra"]["commande"] == ["PY", "-I", "-B", "/g.py", "/arrets", "astra", "--", "PY", "-I", "-B", "/c.py",
                                                      "/cons", "astra", "--", "py", "astra.py"]
    assert d["fournisseurs"]["argon"]["commande"][7:14] == ["PY", "-I", "-B", "/c.py", "/cons", "argon", "--"]
    assert "commande" not in d["fournisseurs"]["claude"]
    for a, b in ((Path("/c.py"), None), (None, Path("/cons"))):
        with pytest.raises(L.Refus, match="ensemble"):
            L.envelopper_commandes(json.loads(json.dumps(decl)), "PY", Path("/g.py"), Path("/arrets"), a, b)


def test_reponse_d_astra_conservee_identique_a_la_reponse_rendue_et_inventoriee(monde):
    ligne = {"texte": "réponse d'essai é", "cout_usd": 0.01, "modele_servi": "modele-essai-astra"}
    script = _astra(monde, ligne)
    _piece_astra(monde, script)
    remplacer_orchestrateur(monde, executer="astra", repetitions=2, transcription=True)
    attendu = subprocess.run([sys.executable, "-I", "-B", str(script)], input=b"consigne", capture_output=True).stdout
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    cons = Path(dep["conservation"]["dossier"])
    appels = sorted(p.name for p in cons.iterdir())
    assert appels == ["astra-appel-0001", "astra-appel-0002"]
    rep = next((cons / "astra-appel-0001").glob("astra-appel-0001-lot-sans-lot-*-reponse.bin"))
    assert rep.read_bytes() == attendu
    conf = json.loads(Path(dep["configuration"]["chemin"]).read_text())
    c = conf["fournisseurs"]["astra"]["commande"]
    assert c[3].endswith("garde_credit_relais_v5.py") and c[10].endswith("enveloppe_conservation_reponses_v1.py") and c[11] == str(cons)
    inv = json.loads((run / "inventaire-conservation.json").read_text())
    fichiers = {f["chemin"]: f for f in inv["parties"]["conservation_reponses"]["fichiers"]}
    assert len(fichiers) == 6 and fichiers[str(rep.relative_to(cons))]["sha256"] == hashlib.sha256(attendu).hexdigest()
    t = inv["parties"]["transcriptions_claude"]
    assert t["present"] is True and t["fichiers"][0]["chemin"] == "projects/essai/session.jsonl"
    assert (Path(dep["sortie"]).parent / ".claude" / "projects" / "essai" / "session.jsonl").is_file()   # rien n'est supprimé


@pytest.mark.parametrize("comportement,code", [({"code": 2}, 2), ({"couts": [("claude", "prop-opus", 75.0), ("argon", "juge-argon", 76.0)]}, 4)])
def test_inventaire_ecrit_meme_sur_issue_en_echec(monde, comportement, code, tmp_path):
    base = tmp_path / "sessions-essai"
    (base / "s1").mkdir(parents=True)
    (base / "s1" / "trace.txt").write_text("trace", encoding="utf-8")
    remplacer_orchestrateur(monde, sessions=str(base), **comportement)
    assert lancer(monde["r"]) == code
    run = un_run(monde["r"])
    inv = run / "inventaire-conservation.json"
    assert L.scelle(inv)
    o = json.loads(inv.read_text())
    assert o["issue"]["code"] == comportement.get("code", 0)
    assert o["parties"]["sessions_orchestrateur"]["fichiers"][0]["chemin"] == "s1/trace.txt"
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["inventaire_conservation"]["sha256"] == L.sha256_fichier(inv)
    assert (base / "s1" / "trace.txt").is_file()


def test_inventaire_ecrit_si_l_orchestrateur_ne_part_pas(monde, monkeypatch):
    vrai_popen = subprocess.Popen

    def refuse(args, *a, **k):                      # seul le lancement de la course (sortie vers un fichier) échoue
        if isinstance(args, list) and "--course-2" in args and "--verifier-seulement" not in args \
                and k.get("stdout") not in (None, subprocess.PIPE):
            raise OSError("essai : orchestrateur non lancé")
        return vrai_popen(args, *a, **k)
    monkeypatch.setattr(subprocess, "Popen", refuse)
    with pytest.raises(RuntimeError):
        L.executer(monde["r"])
    run = un_run(monde["r"])
    o = json.loads((run / "inventaire-conservation.json").read_text())
    assert "OSError" in o["issue"]["echec_lanceur"] and L.scelle(run / "manifeste-lanceur-fin.json")


def test_inventaire_unitaire_liens_non_suivis_absents_notes(tmp_path):
    d = tmp_path / "d"
    (d / "a").mkdir(parents=True)
    (d / "a" / "x.bin").write_bytes(b"\x00\x01")
    (d / "lien").symlink_to(tmp_path)
    (d / "a" / "l2").symlink_to(d / "a" / "x.bin")
    f = tmp_path / "seul.txt"
    f.write_text("s", encoding="utf-8")
    o = L.inventorier({"d": d, "f": f, "absent": tmp_path / "rien", "aucun": None})
    p = o["parties"]
    assert p["d"]["fichiers"] == [{"chemin": "a/x.bin", "octets": 2, "sha256": hashlib.sha256(b"\x00\x01").hexdigest()}]
    assert sorted(x["chemin"] for x in p["d"]["liens"]) == ["a/l2", "lien"]
    assert p["f"]["fichiers"][0]["chemin"] == "seul.txt" and p["absent"]["present"] is False and p["aucun"]["racine"] is None
    assert sorted(x.name for x in d.iterdir()) == ["a", "lien"]                                   # rien n'est supprimé


def test_mutation_inventaire_saute_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, '        h_inv = ecrire_scelle(dossier_run / "inventaire-conservation.json", inventaire)\n',
                        "        h_inv = None\n", "lanceur_v9_mutant_inventaire")
    remplacer_orchestrateur(monde, code=2)
    assert M.principal([], reglages=monde["r"]) == 2
    assert not (un_run(monde["r"]) / "inventaire-conservation.json").exists()               # muté : rien d'inventorié
    _rejouer(monde)
    assert lancer(monde["r"]) == 2 and (un_run(monde["r"]) / "inventaire-conservation.json").is_file()


def test_mutation_conservation_non_inseree_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "            if conservation is not None:\n", "            if False:\n", "lanceur_v9_mutant_conservation")
    script = _astra(monde)
    _piece_astra(monde, script)
    remplacer_orchestrateur(monde, executer="astra")
    assert M.principal([], reglages=monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert list(Path(dep["conservation"]["dossier"]).iterdir()) == []                   # muté : la réponse n'est pas gardée
    _rejouer(monde)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert [p.name for p in Path(dep["conservation"]["dossier"]).iterdir()] == ["astra-appel-0001"]


def test_conservation_impossible_arrete_l_appel_dans_la_course(monde, tmp_path):
    """Le dossier de conservation retiré pendant la course : l'appel d'Astra est arrêté (code 9 de l'enveloppe), la réponse
    n'est pas rendue à l'orchestrateur ; le coût déclaré reste compté par la garde de crédit (aucun repli silencieux)."""
    script = monde["tmp"] / "astra-retire.py"
    script.write_text("import json, os, shutil, sys\nsys.stdin.read()\nh = os.environ['HOME']\n"
                      "shutil.rmtree(os.path.join(h, 'conservation-reponses-v1'))\n"
                      "print(json.dumps({'texte': 'ok', 'cout_usd': 0.02}))\n", encoding="utf-8")
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script), "--url-relais", "http://127.0.0.1:8790"],
             "modele_propose": "modele-essai-astra", "nom_cle": "CLE_ESSAI_S", "porte_plafond": {"type": "environnement"},
             "pid_relais": PID_ASTRA, "url_etat_relais": "http://127.0.0.1:8790"}
    _ecrire(monde, L.DECLARATION_RELAIS, declaration(monde["depot"], astra=astra))
    _ecrire(monde, L.RELEVE_CREDITS, dict(releve(CLE_ESSAI_S={"non_lisible": True, "motif": "illisible"}),
                                          dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S"]}))
    _piece_astra(monde, script)
    remplacer_orchestrateur(monde, executer="astra", capter=True)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    capte = json.loads((Path(dep["sortie"]) / "capte.json").read_text())
    assert capte["code"] == 9 and '"texte": ""' in capte["stdout"] and "conservation impossible" in capte["stdout"]
    assert '"texte": "ok"' not in capte["stdout"]


# additif v2i, épreuve v9, essai à blanc ----------------------------------------------------------------------------------------


@pytest.mark.parametrize("cas", ["sans_v2h", "sans_conservation", "epreuve_v8"])
def test_additif_v2i_artefacts_refuses(monde, cas, capsys):
    r, p = monde["r"], monde["prereg_sha"]
    chemin, _sha = r.additif
    texte = {"sans_v2h": additif(p, v2h="d" * 64), "sans_conservation": additif(p, conservation="e" * 64),
             "epreuve_v8": additif(p, SHA_EPREUVE_V8)}[cas]
    ecrire_scelle(chemin, texte)
    r.additif = (chemin, L.sha256_fichier(chemin))
    assert lancer(r) == 2 and "additif v2i" in capsys.readouterr().err


def test_additif_v2i_reel_epingle_scelle_et_cite_ses_pieces():
    chemin = RACINE / L.ADDITIF
    assert L._epingle(L.ADDITIF_SHA256) and L.sha256_fichier(chemin) == L.ADDITIF_SHA256 and L.scelle(chemin)
    texte = chemin.read_text(encoding="utf-8")
    for h in (L.PREREG_SHA256, L.PIECES["epreuve_temoins"][1], L.ADDITIF_V2C[1], L.ADDITIF_V2D[1], L.ADDITIF_V2E[1],
              L.ADDITIF_V2F[1], L.ADDITIF_V2G[1], L.ADDITIF_V2H[1], L.PIECES["configuration"][1], L.PIECES["enveloppe_carbon"][1],
              L.PIECES["commande_argon"][1], L.PIECES["sonde_carbon"][1], L.PIECES["enveloppe_argon_sans_troncature"][1],
              L.PIECES["enveloppe_conservation"][1]):
        assert h in texte, h
    for mot in ("Course à 150 USD (Recommandé)", "R-3661", "150 USD", "90,49", "120", "135", "140", "59,50", "72,96", "6,05", "161,05",
                "aucun écart"):
        assert mot in texte, mot


def test_rapport_d_epreuve_du_programme_v8_ou_du_lanceur_v8_refuse(monde):
    for cle, sha in (("programme", SHA_EPREUVE_V8), ("lanceur", L8.sha256_fichier(RACINE / "scripts" / "lancer_course_auto_conception_v8.py"))):
        e = epreuve(monde["lanceur_sha"], monde["commit"])
        e["empreintes"][cle] = sha
        _ecrire(monde, L.EPREUVE_REELLE, e)
        assert lancer(monde["r"]) == 2


CHANGEES_V9 = {"verifier_additif", "verifier_contre_lecture", "charger_epreuve", "ecrire_registre_derive", "acte_de_gel", "executer",
               "reglages_a_blanc", "charger_commande_argon", "verifier_course_jamais_lancee_ou_closes_admises", "envelopper_commandes"}


def test_constantes_v9_et_rien_d_autre_ne_change():
    assert L.SORTIES_AUTRES_VERSIONS == tuple(Path(f"/home/user/sorties-course-auto-conception-v{k}") for k in range(1, 9))
    assert L.DOSSIER_SORTIES == Path("/home/user/sorties-course-auto-conception-v9") and L.SUFFIXE_RUN == "-course-auto-conception-v9"
    assert set(L.SUFFIXES_DEJA_LANCEE) == {f"-course-auto-conception-v{k}" for k in range(1, 10)}
    assert (L.PLAFOND_ARRET_USD, L.PLAFOND_SESSION_PROPOSEUR_USD, L.PLAFOND_SONDE_CARBON_USD) == (150.0, 6.05, 6.0)
    assert L.ADDITIF_V2H == (L8.ADDITIF, L8.ADDITIF_SHA256) and L.ADDITIF_V2G == L8.ADDITIF_V2G
    assert L.HAUT_DEVIS_V2I_USD == {"proposition": 70.031788, "aiguillage": 20.46, "juges": 47.322}
    assert (L.DOSSIER_CONSERVATION_NOM, L.DOSSIER_TRANSCRIPTIONS_CLAUDE) == ("conservation-reponses-v1", ".claude")
    for neuf in (L.EPREUVE_REELLE, L.CONTRE_LECTURE, L.DECLARATION_RELAIS, L.ADDITIF, L.PIECE_DE_DEPART, L.RELEVE_PRIX, L.RELEVE_CREDITS):
        assert neuf.startswith(L.COURSE_V4 + "/") and neuf not in (L8.EPREUVE_REELLE, L8.CONTRE_LECTURE, L8.DECLARATION_RELAIS,
                                                                   L8.ADDITIF, L8.PIECE_DE_DEPART, L8.RELEVE_PRIX, L8.RELEVE_CREDITS)
    changees = {"configuration", "epreuve_temoins"}
    assert {k: v for k, v in L.PIECES.items() if k not in changees | {"enveloppe_conservation"}} == \
        {k: v for k, v in L8.PIECES.items() if k not in changees}
    for nom in ("MATIERE", "PROGRAMMES_RELAIS", "PORTS_RELAIS_EXTERNES", "EMPREINTES_ORCHESTRATEUR", "COMMIT_ORCHESTRATEUR",
                "PIECES_SERVIES", "ETIQUETTES_INTERDITES_FIXES", "FOURNISSEURS_DISPENSABLES", "TYPES_PERMIS", "CLES_PERMISES",
                "PREREG_SHA256", "PORT_RELAIS_ARGON", "MODELE_ARGON", "APPELS_RELAIS_PAR_APPEL_GEMINI", "MARGE_APPELS_RELAIS_GEMINI",
                "ADDITIF_V2C", "ADDITIF_V2D", "ADDITIF_V2E", "ADDITIF_V2F", "MOTS_TENTATIVE_NEUVE", "LIGNES_GO_CONSOMMEES",
                "COURSES_CLOSES_ADMISES", "COURSE_CLOSE_CITEE", "REGLAGE_CARBON", "DRAPEAUX_CARBON", "TIMEOUT_ENVELOPPE_CARBON",
                "CLE_CLAUDE_TENTATIVE", "CLES_CLAUDE_REFUSEES", "PLAFOND_SONDE_CARBON_USD", "PLAFOND_SESSION_PROPOSEUR_USD",
                "REGLAGE_ARGON_PROPOSEUR", "DRAPEAUX_ARGON_PROPOSEUR", "TIMEOUT_ENVELOPPE_ARGON_PROPOSEUR", "BAREME_CLAUDE",
                "PLAFOND_EPREUVE_USD", "DEVIS_V1_PAR_APPEL", "DEVIS_V1_TOTAL", "NOMS_PERMIS", "NOMS_DE_CLE"):
        assert getattr(L, nom) == getattr(L8, nom), nom
    for nom, objet in vars(L8).items():
        if (inspect.isfunction(objet) or inspect.isclass(objet)) and getattr(objet, "__module__", None) == L8.__name__ \
                and nom not in CHANGEES_V9:
            assert inspect.getsource(getattr(L, nom)) == inspect.getsource(objet), nom


def test_epreuve_v9_appelle_l_enveloppe_de_conservation_du_lanceur():
    src = inspect.getsource(E.reel)
    assert 'Path(pieces["enveloppe_conservation"]["absolu"]), conservation)' in src and "L.inventorier(" in src
    assert E.LANCEUR.name == "lancer_course_auto_conception_v9.py" and E.CONFIGURATION.name == "configuration-course-auto-conception-v5.json"


@avec_matiere
def test_essai_a_blanc_v9(tmp_path):
    assert L.principal(["--a-blanc", str(tmp_path / "a-blanc")]) == 0
    runs = list((tmp_path / "a-blanc" / "runs").iterdir())
    assert len(runs) == 1 and runs[0].name.endswith("-course-auto-conception-v9")
    dep = json.loads((runs[0] / "manifeste-lanceur-depart.json").read_text())
    fin = json.loads((runs[0] / "manifeste-lanceur-fin.json").read_text())
    assert dep["additif_v2i"]["sha256"] == L.ADDITIF_SHA256 and fin["code"] == 0
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]
    assert dep["argon_regle"]["valeurs"] == L.REGLAGE_ARGON_PROPOSEUR and dep["carbon_regle"]["valeurs"] == L.REGLAGE_CARBON
    assert dep["argon_regle"]["pire_cas"]["max_output_tokens"] == dep["carbon_regle"]["pire_cas"]["max_output_tokens"] == 65536
    assert dep["verification_orchestrateur"]["montant_requis_go_usd"] == 150.0 and fin["ce_qui_a_ete_fait"]["cartes_a_passeport"] == 110
    assert all(dep["seuils_internes_au_haut"]["lecture"][n]["etat"] == "jouee" for n in ("proposition", "aiguillage", "juges"))
    assert L.scelle(runs[0] / "inventaire-conservation.json") and fin["inventaire_conservation"]["erreurs"] == 0
