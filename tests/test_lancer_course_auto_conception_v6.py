"""Essais du lanceur v6 (additif v2f : Carbon à provision de pensée 28 672 et sortie 32 768, sortie retenue au pire ≥ 24 500,
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
CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_auto_conception_v6.py"
_spec = importlib.util.spec_from_file_location("lancer_course_auto_conception_v6", CHEMIN_LANCEUR)
L = importlib.util.module_from_spec(_spec)
sys.modules["lancer_course_auto_conception_v6"] = L
_spec.loader.exec_module(L)
_spec_e = importlib.util.spec_from_file_location("epreuve_temoins_auto_conception_v6", RACINE / "scripts" / "epreuve_temoins_auto_conception_v6.py")
E = importlib.util.module_from_spec(_spec_e)
sys.modules["epreuve_temoins_auto_conception_v6"] = E
_spec_e.loader.exec_module(E)
_spec_g = importlib.util.spec_from_file_location("garde_credit_relais_v5", RACINE / "scripts" / "garde_credit_relais_v5.py")
G = importlib.util.module_from_spec(_spec_g)
_spec_g.loader.exec_module(G)

AUJOURD_HUI = dt.date(2026, 11, 18)
COMMIT_MAIN = "c" * 40
CLE = "RR_ANTHROPIC_API_KEY_ESSAI"


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
        subprocess.run(conf["fournisseurs"][comp["executer"]]["commande"], input=b"consigne", capture_output=True)
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
           "budget": {"cumul_usd": sum(c for _, _, c in comp["couts"])}}, open(os.path.join(g, "manifeste-fin.json"), "w"))
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


def porte_commande(depot: Path, url: str, modeles: list, plafond="90") -> dict:
    return {"type": "commande", "delai_s": 10,
            "commande": [sys.executable, "-I", "-B", str(depot / L.PIECES["porte_plafond"][0]), "--url", url, "--modeles-permis",
                         ",".join(modeles), "--plafond-ligne", plafond]}


def declaration(depot: Path, **modifs) -> dict:
    url = CONTEXTE["url_claude"]
    d = {"version": "essai", "fournisseurs": {
        "claude": {"type": "claude_sdk", "url_relais": url, "nom_cle": CLE, "porte_plafond": porte_commande(depot, url, MODELES_CLAUDE),
                   "pid_relais": PID_CLAUDE},
        "argon": {"type": "commande_externe", "commande": ["bash", str(depot / L.PIECES["enveloppe_argon"][0])],
                  "nom_cle": "CLE_ESSAI_A", "porte_plafond": {"type": "environnement"}, "pid_relais": PID_ARGON,
                  "url_etat_relais": "http://127.0.0.1:8788"}}}
    d["fournisseurs"].update(modifs)
    return d


def piece_de_depart(**modifs) -> dict:
    d = {"version": "essai", "par": "mère", "go_course": "GO-2026-11-18-30", "go_epreuve": "GO-2026-11-18-31",
         "variable_cle_claude": CLE, "credit_declare_cle_claude_usd": 300.0, "reserve_cle_kimi_usd": 15.0,
         "commandes_epinglees": {}, "reserves_cle_claude": [{"montant_usd": 9.0, "pour": "a"}, {"montant_usd": 9.0, "pour": "b"}],
         "especes_optionnelles": {},
         # v5 : mot de reprise de la tentative neuve (la ligne de la course), course close citée
         "tentative_neuve": {"course_close": L.COURSE_CLOSE_ADMISE[0], "mot_de_reprise": "GO-2026-11-18-30"}}
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
            v2d: str = L.ADDITIF_V2D[1], v2e: str = L.ADDITIF_V2E[1]) -> str:
    return (f"# Additif d'essai (tentative neuve v2f)\n\nPréenregistrement : {prereg_sha}\nProgramme d'épreuve v6 : {epreuve_sha}\n"
            f"Additif v2c : {v2c}\nAdditif v2d : {v2d}\nAdditif v2e : {v2e}\nRien d'autre ne change.\n" + suite)


def registre(plafond_c="90 USD", plafond_e="5 USD", perimetre_c="course d'auto-conception de l'organisme d'idéation, tentative neuve",
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
    etat_claude = {"plafond_usd": 90.0, "depense_usd": 0.0, "appels": 0, "modeles_permis": list(MODELES_CLAUDE)}
    etat_kimi = {"plafond_usd": 6.0, "depense_usd": 0.0, "appels": 0, "modeles_permis": ["kimi-k3.1-pro"]}
    etat_argon = {"appels": 0, "max_appels": 600, "variable_cle_encore_presente": False}   # v4 : ≥ 2 × 275 + 2 = 552 (six espèces, Kimi comprise)
    s_claude, s_kimi = serveur(etat_claude), serveur(etat_kimi)
    CONTEXTE.update(url_claude=f"http://127.0.0.1:{s_claude.server_address[1]}", url_kimi=f"http://127.0.0.1:{s_kimi.server_address[1]}")
    progs = tmp_path / "progs"
    progs.mkdir()
    for n in ("relais_reel.py", "relais_kimi_v4.py", "relais_gemini_v2.py", "relais_gemini_v4.py"):
        (progs / n).write_text(f"# {n} factice\n", encoding="utf-8")
    cmdlines = {PID_CLAUDE: [sys.executable, "-I", "-B", str(progs / "relais_reel.py"), "--variable-cle", CLE,
                             "--port", CONTEXTE["url_claude"].rsplit(":", 1)[1], "--plafond-usd", "90", "--modeles-permis",
                             ",".join(MODELES_CLAUDE)],
                PID_KIMI: [sys.executable, "-I", "-B", str(progs / "relais_kimi_v4.py"), "--variable-cle", "CLE_ESSAI_K",
                           "--port", CONTEXTE["url_kimi"].rsplit(":", 1)[1], "--plafond-usd", "6"],
                PID_ARGON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v2.py"), "--port", "8788", "--max-appels", "600",
                            "--modele", "gemini-4-argon", "--variable-cle", "CLE_ESSAI_A"],
                PID_ASTRA: [sys.executable, "-I", "-B", str(progs / "relais_kimi_v4.py"), "--amont", "https://api.openai.com",
                            "--variable-cle", "CLE_ESSAI_S", "--port", "8790", "--modeles-permis", "modele-essai-astra",
                            "--plafond-usd", "20"],
                PID_CARBON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v4.py"), "--variable-cle", "CLE_ESSAI_C",
                             "--port", "8792", "--modele", "modele-essai-carbon", "--max-lots", "20"]}
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
    etat_carbon = {"appels": 0, "lots_crees": 0, "max_lots": 20}
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
                                  "RR_ANTHROPIC_API_KEY_MINUIT": "valeur-secrete-essai-2"},
                   aujourd_hui=AUJOURD_HUI, horodatage=lambda: "Wed Nov 18 07:00:00 UTC 2026",
                   programmes_relais={n: (p, hashlib.sha256((progs / p).read_bytes()).hexdigest()) for n, p in
                                      (("claude", "relais_reel.py"), ("kimi", "relais_kimi_v4.py"), ("argon", "relais_gemini_v2.py"),
                                       ("astra", "relais_kimi_v4.py"), ("carbon", "relais_gemini_v4.py"))},
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
    {"variable_cle_claude": "RR_ANTHROPIC_API_KEY_MINUIT"},
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
    d["fournisseurs"]["claude"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_MINUIT"
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert lancer(monde["r"]) == 2


def test_cle_claude_sur_un_autre_relais_refusee(monde):
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_AUTRE"
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert lancer(monde["r"]) == 2


# --- GO, registre, matière --------------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("texte", [registre(plafond_c="150 USD"), registre(perimetre_c="course d'affinage"),
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
    lambda c: c.__setitem__(c.index("--plafond-ligne") + 1, "150"),
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
    c[c.index("--plafond-usd") + 1] = "150"
    assert lancer(monde["r"]) == 2


def test_relais_claude_autre_variable_refuse(monde):
    c = monde["cmdlines"][PID_CLAUDE]
    c[c.index("--variable-cle") + 1] = "RR_ANTHROPIC_API_KEY_MINUIT"
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


OPTIONS_CARBON_SAINES = ["--modele", "modele-essai-carbon", "--prix-entree", "8.3", "--prix-sortie", "41.5",
                         "--provision-pensee-jetons", "28672", "--max-sortie-jetons", "32768", "--delai-s", "1620",
                         "--delai-requete-s", "60"]


def test_carbon_relais_controle(monde):
    script = monde["tmp"] / "commande_gemini_lot_v1.py"     # v5 : la garde des options lit la commande par son nom
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps({'texte': 'ok', 'cout_usd': 0.01}))\n", encoding="utf-8")
    carbon = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script), "--url-base", "http://127.0.0.1:8792/v1beta"]
              + OPTIONS_CARBON_SAINES,
              "modele_propose": "modele-essai-carbon", "nom_cle": "CLE_ESSAI_C", "porte_plafond": {"type": "environnement"},
              "pid_relais": PID_CARBON, "url_etat_relais": "http://127.0.0.1:8792"}
    _ecrire(monde, L.DECLARATION_RELAIS, declaration(monde["depot"], carbon=carbon))
    _ecrire(monde, L.RELEVE_CREDITS, dict(releve(CLE_ESSAI_C={"non_lisible": True, "motif": "illisible"}),
                                          dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_C"]}))
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(
        commandes_epinglees={"carbon": {"empreintes": [L.sha256_fichier(script)], "epreuve": "R-essai"}},
        especes_optionnelles={"carbon": {"declaree": True, "risque_accepte": True, "sonde_du_jour": "R-essai"}}))
    monde["etat_carbon"]["lots_crees"] = 1
    assert lancer(monde["r"]) == 2
    monde["etat_carbon"]["lots_crees"] = 0
    c = monde["cmdlines"][PID_CARBON]
    c[c.index("--port") + 1] = "8788"
    assert lancer(monde["r"]) == 2
    c[c.index("--port") + 1] = "8792"
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-carbon" in dep["especes_actives"]


# --- crédits ------------------------------------------------------------------------------------------------------------------------


def test_cle_claude_non_lisible_comptee_au_credit_declare_net_des_reserves(monde):
    _ecrire(monde, L.RELEVE_CREDITS, releve(**{CLE: {"non_lisible": True, "depense_anterieure_usd": 10.0}}))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["releve_credits_avant"]["cles"][CLE]["reste_usd"] == 272.0  # 300 − 10 − 9 − 9


def test_reserves_de_la_cle_claude_retranchees_code_3(monde):
    """Constat 8 (R-3271) : 124 déclarés, 2 dépensés, réserves 9 + 9 → 104 net > 90 : part ; 108 lus → 90 net : alerte."""
    _ecrire(monde, L.PIECE_DE_DEPART, piece_de_depart(credit_declare_cle_claude_usd=124.0))
    _ecrire(monde, L.RELEVE_CREDITS, releve(**{CLE: {"non_lisible": True, "depense_anterieure_usd": 2.0}}))
    assert lancer(monde["r"]) == 0
    shutil.rmtree(un_run(monde["r"]))
    shutil.rmtree(monde["r"].dossier_sorties)
    _ecrire(monde, L.RELEVE_CREDITS, releve(**{CLE: {"credit_usd": 124.0, "reste_usd": 108.0, "source": "essai"}}))
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
    for modif in (lambda f: f["budget"].__setitem__("plafond_usd", 150.0),
                  lambda f: f["budget"]["etapes"][3].__setitem__("plafond_relais_usd", 50.0),
                  lambda f: f["budget"]["etapes"][0].__setitem__("plafond_relais_usd", 80.0),
                  lambda f: f.__setitem__("etage_tests_de_mort", {"nombre": 1}),
                  lambda f: f.__setitem__("generations", 2),
                  lambda f: f.__setitem__("etiquettes_interdites_fixes", ["Opus"]),
                  lambda f: f["especes"][0].__setitem__("cle", "RR_ANTHROPIC_API_KEY_MINUIT")):
        f = json.loads(json.dumps(FIXE))
        modif(f)
        with pytest.raises(L.Refus):
            L.garde_configuration_fixe(f)


def test_verification_orchestrateur_montant_autre_refuse(monde):
    remplacer_orchestrateur(monde, montant=150.0)
    assert lancer(monde["r"]) == 2


def test_cumul_au_dela_du_plafond_code_4(monde):
    remplacer_orchestrateur(monde, couts=[("claude", "prop-opus", 60.0), ("argon", "juge-argon", 31.0)])
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


# --- v3 : correctif v2c ---------------------------------------------------------------------------------------------------------


_spec_l4 = importlib.util.spec_from_file_location("lancer_course_auto_conception_v4_pour_essai_v6",
                                                  RACINE / "scripts" / "lancer_course_auto_conception_v4.py")
L4 = importlib.util.module_from_spec(_spec_l4)
sys.modules[_spec_l4.name] = L4
_spec_l4.loader.exec_module(L4)
_spec_l5 = importlib.util.spec_from_file_location("lancer_course_auto_conception_v5_pour_essai_v6",
                                                  RACINE / "scripts" / "lancer_course_auto_conception_v5.py")
L5 = importlib.util.module_from_spec(_spec_l5)
sys.modules[_spec_l5.name] = L5
_spec_l5.loader.exec_module(L5)
SHA_PIECE_DE_DEPART = "e2689fa22fff31319ff69deefe10c066d5329fab28d9c9b133750f2534fc1ded"
SHA_EPREUVE_V2 = "19d03876a1b65557d20bf23bdbbf9c657ef726a2be16168fcf78a838f2eac536"
SHA_EPREUVE_V3 = "0c72dd8763537152b7339ca15ff439f759c062f0b33a6571a513029870eebd1b"
SHA_EPREUVE_V4 = "04f62b8c48db9e9b04114aaa37f00801e825ff0bc2d4a86934b44f2b79263d75"
SHA_EPREUVE_V5 = "4a10b39df473dfdab915ec3798d307c6803a9fd60f0746c0c5f1cd76b80309cb"
SHA_DIAGNOSTIC = "510312b105c62ad01a1d45ab9078dfc04333ce3bc2322b98695fa48c4daa8aec"
# fonctions et classes du lanceur v5 qui changent en v6 ; toutes les autres sont identiques à l'octet
CHANGEES_V6 = {"verifier_additif", "verifier_contre_lecture", "controler_options_carbon", "pire_cas_carbon", "charger_epreuve",
               "ecrire_registre_derive", "acte_de_gel", "executer", "reglages_a_blanc"}


def test_v6_bout_en_bout_cite_l_additif(monde):
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    assert run.name.endswith("-course-auto-conception-v6")
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    assert dep["additif_v2f"]["sha256"] == monde["additif_sha"] and dep["lanceur"]["version"] == "lancer_course_auto_conception_v6"
    assert dep["additifs_cites"]["v2e"]["sha256"] == L.ADDITIF_V2E[1] and dep["additifs_cites"]["v2d"]["sha256"] == L.ADDITIF_V2D[1]
    acte = (run / "acte-de-gel.md").read_text()
    assert monde["additif_sha"] in acte and "additif v2f" in acte
    assert dep["pieces"]["epreuve_temoins"]["chemin"] == "scripts/epreuve_temoins_auto_conception_v6.py"
    assert dep["epreuve_reelle_des_temoins"]["chemin"].endswith("course-v3/epreuve-temoins-reelle-auto-conception-v6.json")
    assert dep["declaration_relais"]["chemin"].endswith("course-v3/declaration-relais-course-auto-conception-v6.json")
    assert dep["une_seule_course"]["course_close_admise"] is None and dep["mot_de_reprise"]["id"] == "GO-2026-11-18-30"


@pytest.mark.parametrize("cas", ["absent", "non_scelle", "autre_empreinte", "non_pose", "sans_prereg", "sans_epreuve", "epreuve_v4",
                                 "epreuve_v5", "sans_v2c", "sans_v2d", "sans_v2e"])
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
        texte = {"sans_prereg": additif("1" * 64), "sans_epreuve": additif(monde["prereg_sha"], "2" * 64),
                 "epreuve_v4": additif(monde["prereg_sha"], SHA_EPREUVE_V4),
                 "epreuve_v5": additif(monde["prereg_sha"], SHA_EPREUVE_V5),
                 "sans_v2c": additif(monde["prereg_sha"], v2c="3" * 64),
                 "sans_v2d": additif(monde["prereg_sha"], v2d="4" * 64),
                 "sans_v2e": additif(monde["prereg_sha"], v2e="5" * 64)}[cas]
        ecrire_scelle(chemin, texte)
        r.additif = (chemin, L.sha256_fichier(chemin))
    assert lancer(r) == 2
    assert "additif" in capsys.readouterr().err
    assert not r.dossier_runs.exists()


def test_contre_lecture_qui_ne_cite_pas_l_additif_refusee(monde, capsys):
    _ecrire(monde, L.CONTRE_LECTURE, contre_lecture(monde["prereg_sha"], monde["lanceur_sha"]))
    assert lancer(monde["r"]) == 2
    assert "ne cite pas l'empreinte de l'additif v2f" in capsys.readouterr().err


def test_rapport_d_epreuve_du_programme_v5_ou_du_lanceur_v5_refuse(monde):
    """Un rapport d'épreuve joué par le programme v5 ou pour le lanceur v5 n'est pas accepté ; un rapport « réussie » écrit au
    chemin v5 n'est pas lu."""
    for cle, sha in (("programme", SHA_EPREUVE_V5), ("lanceur", L5.sha256_fichier(RACINE / "scripts" / "lancer_course_auto_conception_v5.py"))):
        e = epreuve(monde["lanceur_sha"], monde["commit"])
        e["empreintes"][cle] = sha
        _ecrire(monde, L.EPREUVE_REELLE, e)
        assert lancer(monde["r"]) == 2
    (monde["depot"] / L.EPREUVE_REELLE).unlink()
    Path(str(monde["depot"] / L.EPREUVE_REELLE) + ".sha256").unlink()
    _ecrire(monde, L5.EPREUVE_REELLE, epreuve(monde["lanceur_sha"], monde["commit"]))
    assert lancer(monde["r"]) == 2


@pytest.mark.parametrize("version", ["v1", "v2", "v3", "v5"])
def test_course_autre_que_la_v4_close_deja_lancee_bloque_la_v6(monde, version, capsys):
    d = monde["r"].dossier_runs / f"20261118-000000-course-auto-conception-{version}"
    d.mkdir(parents=True)
    (d / "manifeste-lanceur-depart.json").write_text("{}", encoding="utf-8")
    assert lancer(monde["r"]) == 2
    assert "seule la course close" in capsys.readouterr().err


def test_journal_v2_hors_depot_bloque_la_v6(monde):
    j = monde["tmp"] / "sorties-v2" / "x" / "course.stdout.txt"
    j.parent.mkdir(parents=True)
    j.write_text("", encoding="utf-8")
    monde["r"].sorties_autres_versions = (monde["tmp"] / "sorties-v1-absentes", monde["tmp"] / "sorties-v2")
    assert lancer(monde["r"]) == 2


def test_constantes_v6_et_rien_d_autre_ne_change():
    assert L.SORTIES_AUTRES_VERSIONS == tuple(Path(f"/home/user/sorties-course-auto-conception-v{k}") for k in (1, 2, 3, 4, 5))
    assert L.DOSSIER_SORTIES == Path("/home/user/sorties-course-auto-conception-v6") and L.SUFFIXE_RUN == "-course-auto-conception-v6"
    assert set(L.SUFFIXES_DEJA_LANCEE) == {f"-course-auto-conception-v{k}" for k in (1, 2, 3, 4, 5, 6)}
    assert (L.PROVISION_PENSEE_CARBON, L.MAX_SORTIE_CARBON, L.SORTIE_RETENUE_MIN_CARBON) == (28672, (32768, 32768), 24500)
    assert L.PROVISION_PENSEE_CARBON >= 1.385 * L.PENSEE_OBSERVEE_MAX_CARBON and L.PENSEE_OBSERVEE_MAX_CARBON == 20696
    for neuf in (L.EPREUVE_REELLE, L.CONTRE_LECTURE, L.DECLARATION_RELAIS, L.ADDITIF, L.PIECE_DE_DEPART):
        assert neuf.startswith(L.COURSE_V3 + "/") and neuf not in (L5.EPREUVE_REELLE, L5.CONTRE_LECTURE, L5.DECLARATION_RELAIS,
                                                                   L5.ADDITIF, L5.PIECE_DE_DEPART)
    assert L.ADDITIF_V2E == (L5.ADDITIF, L5.ADDITIF_SHA256)
    assert {k: v for k, v in L.PIECES.items() if k != "epreuve_temoins"} == {k: v for k, v in L5.PIECES.items() if k != "epreuve_temoins"}
    assert L.PIECES["epreuve_temoins"] == ("scripts/epreuve_temoins_auto_conception_v6.py",
                                           L.sha256_fichier(RACINE / "scripts" / "epreuve_temoins_auto_conception_v6.py"))
    for nom in ("PLAFOND_ARRET_USD", "PLAFOND_EPREUVE_USD", "MATIERE", "DEVIS_V1_PAR_APPEL", "DEVIS_V1_TOTAL", "BAREME_CLAUDE",
                "PROGRAMMES_RELAIS", "PORTS_RELAIS_EXTERNES", "EMPREINTES_ORCHESTRATEUR", "COMMIT_ORCHESTRATEUR", "PIECES_SERVIES",
                "ETIQUETTES_INTERDITES_FIXES", "EXPURGATIONS", "CLES_CLAUDE_RESERVEES", "FOURNISSEURS_DISPENSABLES", "TYPES_PERMIS",
                "CLES_PERMISES", "CLES_META", "PREREG", "PREREG_SHA256", "PORT_RELAIS_ARGON", "MODELE_ARGON", "AMONT_ASTRA",
                "APPELS_RELAIS_PAR_APPEL_GEMINI", "MARGE_APPELS_RELAIS_GEMINI", "NOMS_PERMIS", "NOMS_DE_CLE", "ADDITIF_V2C",
                "ADDITIF_V2D", "COURSE_CLOSE_ADMISE", "LIGNES_GO_CONSOMMEES", "MOTS_TENTATIVE_NEUVE", "PRIX_CARBON",
                "DELAI_COMMANDE_ORCHESTRATEUR_S", "MARGE_DELAI_COMMANDE_S", "OCTETS_PAR_JETON_AU_PIRE", "OPTIONS_COMMANDE_CARBON",
                "OPTIONS_CARBON_EXIGEES", "COMMANDES_MAIN_A_BLANC", "RELEVE_PRIX", "RELEVE_CREDITS"):
        assert getattr(L, nom) == getattr(L5, nom), nom
    import inspect
    for nom, objet in vars(L5).items():
        if (inspect.isfunction(objet) or inspect.isclass(objet)) and getattr(objet, "__module__", None) == L5.__name__ \
                and nom not in CHANGEES_V6:
            assert inspect.getsource(getattr(L, nom)) == inspect.getsource(objet), nom


def test_additif_reel_epingle_scelle_et_cite_ses_pieces():
    chemin = RACINE / L.ADDITIF
    assert L._epingle(L.ADDITIF_SHA256) and L.sha256_fichier(chemin) == L.ADDITIF_SHA256 and L.scelle(chemin)
    texte = chemin.read_text(encoding="utf-8")
    assert L.PREREG_SHA256 in texte and L.PIECES["epreuve_temoins"][1] in texte
    for h in (L.ADDITIF_V2C[1], L.ADDITIF_V2D[1], L.ADDITIF_V2E[1], SHA_DIAGNOSTIC, L.COURSE_CLOSE_ADMISE[1]):
        assert h in texte, h
    assert "28672" in texte and "32768" in texte and "including thought tokens" in texte and "44,780492 USD" in texte


def test_piece_de_depart_v2_consommee_refusee_par_la_v6(monde, capsys):
    assert L.sha256_fichier(RACINE / L4.PIECE_DE_DEPART) == SHA_PIECE_DE_DEPART
    ecrire_scelle(monde["depot"] / L.PIECE_DE_DEPART, (RACINE / L4.PIECE_DE_DEPART).read_text(encoding="utf-8"))
    with pytest.raises(L.Refus, match="consommée"):
        L.verifier_piece_de_depart(monde["r"])
    assert lancer(monde["r"]) == 2 and "consommée" in capsys.readouterr().err


@avec_matiere
def test_essai_a_blanc_v6(tmp_path):
    assert L.principal(["--a-blanc", str(tmp_path / "a-blanc")]) == 0
    runs = list((tmp_path / "a-blanc" / "runs").iterdir())
    assert len(runs) == 1 and runs[0].name.endswith("-course-auto-conception-v6")
    dep = json.loads((runs[0] / "manifeste-lanceur-depart.json").read_text())
    fin = json.loads((runs[0] / "manifeste-lanceur-fin.json").read_text())
    assert dep["additif_v2f"]["sha256"] == L.ADDITIF_SHA256 and fin["code"] == 0
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]
    v = dep["carbon_regle"]["valeurs"]
    assert (v["--provision-pensee-jetons"], v["--max-sortie-jetons"], v["--delai-s"], v["--delai-requete-s"]) == (28672, 32768, 1620.0, 60.0)
    assert dep["carbon_regle"]["pire_cas"]["max_output_tokens"] >= 24500 and dep["carbon_regle"]["pire_cas"]["pire_cas_usd"] <= 3.0
    assert dep["sonde_astra_du_jour"]["exigee"] is True and fin["ce_qui_a_ete_fait"]["cartes_a_passeport"] == 110
# --- v2b portée au v3 : Astra et Carbon déclarés (commandes réelles de `main`) ------------------------------------------------


GABARIT = RACINE / "docs/notes/organisme-auto-conception-v1/course-v3/piece-de-depart-gabarit-auto-conception-v2f.json"   # v6
COMMANDES_MAIN = {"astra": ("docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py",
                            "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71"),
                  "carbon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py",
                             "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75")}


def _de_main(rel, sha):
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"refs/remotes/origin/main:{rel}"], capture_output=True)
    return p.stdout if p.returncode == 0 and hashlib.sha256(p.stdout).hexdigest() == sha else None


OCTETS = {n: _de_main(*v) for n, v in COMMANDES_MAIN.items()}
avec_commandes = pytest.mark.skipif(any(v is None for v in OCTETS.values()), reason="commandes absentes de origin/main")


def piece_remplie(**especes) -> dict:
    o = json.loads(GABARIT.read_text(encoding="utf-8"))
    o.update(statut="rempli pour l'essai", go_course="GO-2026-11-18-30", go_epreuve="GO-2026-11-18-31", variable_cle_claude=CLE,
             credit_declare_cle_claude_usd=300.0, ecrit_le="2026-11-18T11:00:00Z")
    o["especes_optionnelles"]["astra"]["sonde_du_jour"] = ("docs/notes/organisme-auto-conception-v1/course-v2/"
                                                          "sonde-astra-2026-11-18-v1.json (sha256 " + "a" * 64 + ", ok vrai)")
    o["especes_optionnelles"]["astra"]["sonde_du_jour_rapport"] = SONDE_REL          # v5 : écrit par `preparer`
    o["tentative_neuve"]["mot_de_reprise"] = "GO-2026-11-18-30"                       # v5 : mot de reprise = ligne de la course
    for nom, modifs in especes.items():
        o["especes_optionnelles"][nom].update(modifs)
        for k in [k for k, v in modifs.items() if v is None]:
            del o["especes_optionnelles"][nom][k]
    return o


def preparer(m, cle=CLE) -> None:
    cmds = {}
    for n, b in OCTETS.items():
        p = m["tmp"] / Path(COMMANDES_MAIN[n][0]).name
        p.write_bytes(b)
        cmds[n] = str(p)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", cmds["astra"], "--url-relais", "http://127.0.0.1:8790",
                                                      "--modele", "gpt-6-astra", "--prix-entree", "10", "--prix-sortie", "50"],
             "modele_propose": "gpt-6-astra", "nom_cle": "CLE_ESSAI_S", "pid_relais": PID_ASTRA,
             "url_etat_relais": "http://127.0.0.1:8790", "porte_plafond": {"type": "environnement"}}
    carbon = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", cmds["carbon"], "--url-base",
                                                       "http://127.0.0.1:8792/v1beta", "--modele", "gemini-4-carbon",
                                                       "--prix-entree", "8.3", "--prix-sortie", "41.5",
                                                       "--provision-pensee-jetons", "28672", "--max-sortie-jetons", "32768",
                                                       "--delai-s", "1620", "--delai-requete-s", "60"],     # v6 : Carbon réglé
              "modele_propose": "gemini-4-carbon", "nom_cle": "CLE_ESSAI_C", "pid_relais": PID_CARBON,
              "url_etat_relais": "http://127.0.0.1:8792", "porte_plafond": {"type": "environnement"}}
    d = declaration(m["depot"], astra=astra, carbon=carbon)
    sonde_astra(m, COMMANDES_MAIN["astra"][1])                                        # v5 : sonde d'Astra du jour
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


@avec_commandes
def test_relais_argon_sous_464_appels_de_relais_refuse(monde, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    c = monde["cmdlines"][PID_ARGON]
    c[c.index("--max-appels") + 1] = "200"
    assert lancer(monde["r"]) == 2 and "464" in capsys.readouterr().err


def test_gabarit_brut_refuse_tant_qu_il_n_est_pas_rempli(monde):
    ecrire_scelle(monde["depot"] / L.PIECE_DE_DEPART, GABARIT.read_text(encoding="utf-8"))
    with pytest.raises(L.Refus, match="À REMPLIR"):
        L.verifier_piece_de_depart(monde["r"])


@avec_commandes
def test_gabarit_rempli_astra_et_carbon_declares_actifs(monde):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    depart = L.verifier_piece_de_depart(monde["r"])
    assert depart["especes_optionnelles"]["astra"]["declaree"] and depart["especes_optionnelles"]["carbon"]["declaree"]
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    actives = dep["especes_actives"]
    assert {"prop-astra", "prop-carbon", "prop-argon"} <= set(actives) and len(actives) == 5 and not any("kimi" in e for e in actives)
    vivants = dep["procedure_relais_persistants"]["relais_vivants"]
    assert vivants["astra"]["port"] == "8790" and vivants["carbon"]["port"] == "8792"


@avec_commandes
@pytest.mark.parametrize("espece,modifs", [
    ("astra", {"sonde_du_jour": None}), ("astra", {"sonde_du_jour": "  "}), ("astra", {"risque_accepte": False}),
    ("carbon", {"sonde_du_jour": None}), ("carbon", {"risque_accepte": None})])
def test_sans_sonde_ou_sans_risque_accepte_refuse(monde, espece, modifs):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie(**{espece: modifs}))
    with pytest.raises(L.Refus, match="sonde_du_jour"):
        L.verifier_piece_de_depart(monde["r"])
    assert lancer(monde["r"]) == 2


@avec_commandes
def test_espece_retiree_de_la_piece_mais_declaree_aux_relais_refusee(monde):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie(astra={"declaree": False}))
    assert lancer(monde["r"]) == 2


@avec_commandes
def test_commande_d_une_autre_empreinte_refusee(monde):
    preparer(monde)
    o = piece_remplie()
    o["commandes_epinglees"]["astra"]["empreintes"] = ["b" * 64]
    _ecrire(monde, L.PIECE_DE_DEPART, o)
    assert lancer(monde["r"]) == 2


@avec_commandes
def test_relais_de_course_d_astra_non_neuf_refuse(monde, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    monde["etat_astra"]["appels"] = 1
    assert lancer(monde["r"]) == 2
    assert "relais astra : relais neuf" in capsys.readouterr().err
    monde["etat_astra"]["appels"] = 0
    assert lancer(monde["r"]) == 0


# --- pièce de départ scellée existante, telle quelle --------------------------------------------------------------------------


CLE_RIGAUD = "RR_ANTHROPIC_API_KEY_RIGAUD"
GO_COURSE_NEUVE, GO_EPREUVE_NEUVE = "GO-2026-11-19-01", "GO-2026-11-19-02"


def preparer_piece_reelle(m) -> None:
    """v5 : le gabarit v2e rempli comme la mère le remplira (clé Claude nommée, deux lignes de GO neuves, mot de reprise = la
    ligne de la course, crédit qui laisse un reste net au-dessus de 90), au registre, l'épreuve v5 jouée sous la ligne neuve de
    l'épreuve, Astra (sonde du jour) et Carbon (réglé) par les commandes réelles de `main`."""
    o = json.loads(GABARIT.read_text(encoding="utf-8"))
    o.update(statut="rempli pour l'essai", go_course=GO_COURSE_NEUVE, go_epreuve=GO_EPREUVE_NEUVE, credit_declare_cle_claude_usd=150.0,
             ecrit_le="2026-11-19T08:00:00Z")
    o["tentative_neuve"]["mot_de_reprise"] = GO_COURSE_NEUVE
    o["especes_optionnelles"]["astra"]["sonde_du_jour"] = f"{SONDE_REL} (essai)"
    o["especes_optionnelles"]["astra"]["sonde_du_jour_rapport"] = SONDE_REL
    preparer(m, cle=CLE_RIGAUD)
    _ecrire(m, L.PIECE_DE_DEPART, o)
    m["r"].environnement[CLE_RIGAUD] = "valeur-secrete-essai-3"
    m["main"]["registres/go.md"] = registre().replace("GO-2026-11-18-30", GO_COURSE_NEUVE).replace(
        "GO-2026-11-18-31", GO_EPREUVE_NEUVE).encode("utf-8")
    _ecrire(m, L.EPREUVE_REELLE, epreuve(m["lanceur_sha"], m["commit"], go={"id": GO_EPREUVE_NEUVE}))


@avec_commandes
def test_gabarit_v2e_rempli_accepte(monde):
    preparer_piece_reelle(monde)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["go"]["id"] == GO_COURSE_NEUVE and dep["mot_de_reprise"]["id"] == GO_COURSE_NEUVE
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]
    assert dep["cle_par_espece"]["prop-opus"] == CLE_RIGAUD
    assert dep["carbon_regle"]["duree_au_pire_s"] == 1770.0 and dep["carbon_regle"]["pire_cas"]["max_output_tokens"] == 29271
    for p in list(un_run(monde["r"]).rglob("*")):
        if p.is_file():
            assert "valeur-secrete-essai" not in p.read_text(errors="replace"), p


@avec_commandes
def test_gabarit_v2e_au_credit_de_la_piece_v2_alerte_code_3(monde):
    """Le reste net de la clé Claude au crédit de la pièce v2 (124 USD), dépense antérieure lue après la course v4 et l'épreuve
    v5 (≈ 33,27 USD) et réserves (18 USD) : 72,73 ≤ 90 → alerte, code 3 (devis v2e)."""
    preparer_piece_reelle(monde)
    o = json.loads((monde["depot"] / L.PIECE_DE_DEPART).read_text(encoding="utf-8"))
    o["credit_declare_cle_claude_usd"] = 124.0
    _ecrire(monde, L.PIECE_DE_DEPART, o)
    _ecrire(monde, L.RELEVE_CREDITS, dict(releve(**{CLE_RIGAUD: {"non_lisible": True, "depense_anterieure_usd": 33.268864},
                                                    "CLE_ESSAI_S": {"non_lisible": True, "motif": "illisible"},
                                                    "CLE_ESSAI_C": {"non_lisible": True, "motif": "illisible"}}),
                                          dispense={"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_S", "CLE_ESSAI_C"]}))
    assert lancer(monde["r"]) == 3
    o["credit_declare_cle_claude_usd"] = 141.3
    _ecrire(monde, L.PIECE_DE_DEPART, o)
    shutil.rmtree(monde["r"].dossier_runs)
    assert lancer(monde["r"]) == 0
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


@avec_commandes
@pytest.mark.parametrize("etat,code,motif", [({"max_appels": 23}, 2, "24"), ({"max_appels": 24}, 0, None),
                                             ({"max_lots": 10}, 2, "max_lots"), ({"max_lots": 11}, 0, None),
                                             ({"max_appels": 60, "max_lots": 15}, 0, None)])
def test_relais_carbon_deux_appels_par_lot(monde, etat, code, motif, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    monde["etat_carbon"].update(etat)
    assert lancer(monde["r"]) == code
    if motif:
        assert motif in capsys.readouterr().err


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


@avec_commandes
def test_mutation_borne_argon_non_doublee_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "    return APPELS_RELAIS_PAR_APPEL_GEMINI * int(appels) + MARGE_APPELS_RELAIS_GEMINI\n",
                        "    return int(appels)\n", "lanceur_v6_mutant_borne")
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
                        "    requis = appels_requis\n", "lanceur_v6_mutant_carbon")
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    monde["etat_carbon"]["max_appels"] = 15
    assert M.principal([], reglages=monde["r"]) == 0
    shutil.rmtree(monde["r"].dossier_runs)
    shutil.rmtree(monde["r"].dossier_sorties)
    assert lancer(monde["r"]) == 2


def test_mutation_recalcul_sans_requalification_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "    return E.qualifier_verdict(lecture, incidents, None, [], True)\n",
                        '    return lecture["verdict"]\n', "lanceur_v6_mutant_recalcul")
    e = epreuve(monde["lanceur_sha"], monde["commit"], verdict="non conclue", incidents_techniques=_incidents_tous())
    for j in e["verdicts"]:
        e["verdicts"][j] = {t: None for t in e["verdicts"][j]}
    e["classes"] = {t: None for t in e["classes"]}
    pieces = {"epreuve_temoins": {"absolu": str(RACINE / L.PIECES["epreuve_temoins"][0])},
              "temoins": {"absolu": str(RACINE / L.PIECES["temoins"][0])},
              "configuration": {"absolu": str(RACINE / L.PIECES["configuration"][0])}}
    assert L.recalculer_verdict_epreuve(e, pieces) == "non conclue"
    assert M.recalculer_verdict_epreuve(e, pieces) == "échouée"


def test_controle_carbon_unitaire_sain_et_artefacts():
    """`controler_relais_externe` sur Carbon : la borne d'appels est doublée, la borne de lots exigée ; Astra inchangé."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        prog = Path(d) / "relais_gemini_v4.py"
        prog.write_text("# factice\n", encoding="utf-8")
        prog_a = Path(d) / "relais_kimi_v4.py"
        prog_a.write_text("# factice a\n", encoding="utf-8")
        for etat, ok in (({"max_appels": 24, "max_lots": 11}, True), ({"max_appels": 23, "max_lots": 11}, False),
                         ({"max_appels": 24, "max_lots": 10}, False), ({"max_appels": 12, "max_lots": 11}, False)):
            r = L.Reglages.production()
            r.programmes_relais = dict(L.PROGRAMMES_RELAIS, carbon=("relais_gemini_v4.py", L.sha256_fichier(prog)))
            r.lire_cmdline = lambda pid: [sys.executable, str(prog), "--port", "8792", "--variable-cle", "K", "--modele", "m-carbon"]
            r.lire_etat_relais = lambda url, e=etat: dict(e, appels=0, lots_crees=0)
            b = {"nom_cle": "K", "modele_propose": "m-carbon"}
            meta = {"pid_relais": 4242, "url_etat_relais": "http://127.0.0.1:8792"}
            if ok:
                assert L.controler_relais_externe(r, "carbon", b, meta, 11)["etat"]["max_appels"] == 24
            else:
                with pytest.raises(L.Refus):
                    L.controler_relais_externe(r, "carbon", b, meta, 11)
        r = L.Reglages.production()
        r.programmes_relais = dict(L.PROGRAMMES_RELAIS, astra=("relais_kimi_v4.py", L.sha256_fichier(prog_a)))
        r.lire_cmdline = lambda pid: [sys.executable, str(prog_a), "--port", "8790", "--variable-cle", "K", "--amont", L.AMONT_ASTRA,
                                      "--modeles-permis", "m-astra", "--plafond-usd", "20"]
        r.lire_etat_relais = lambda url: {"appels": 0, "max_appels": 11}
        assert L.controler_relais_externe(r, "astra", {"nom_cle": "K", "modele_propose": "m-astra"},
                                          {"pid_relais": 4243, "url_etat_relais": "http://127.0.0.1:8790"}, 11)


# --- v5 : gardes neuves de la tentative neuve (sain, artefacts, mutation) ------------------------------------------------------


IDENT_V4 = L.COURSE_CLOSE_ADMISE[0]


def course_v4_close(monde, fin=True, sceller_fin=True, journal=False) -> str:
    """Une course v4 « lancée » au dépôt d'essai (manifeste de départ) et close (manifeste de fin scellé) ; l'empreinte du
    manifeste de fin d'essai est posée comme empreinte épinglée des réglages. Rend cette empreinte."""
    d = monde["r"].dossier_runs / IDENT_V4
    d.mkdir(parents=True, exist_ok=True)
    (d / "manifeste-lanceur-depart.json").write_text('{"essai": "départ v4"}\n', encoding="utf-8")
    sha = "0" * 64
    if fin:
        f = d / "manifeste-lanceur-fin.json"
        f.write_text('{"essai": "fin v4", "code": 2}\n', encoding="utf-8")
        sha = L.sha256_fichier(f)
        if sceller_fin:
            sceller(f)
    monde["r"].course_close_admise = (IDENT_V4, sha)
    if journal:
        j = monde["tmp"] / "sorties-v4" / IDENT_V4 / "course.stdout.txt"
        j.parent.mkdir(parents=True, exist_ok=True)
        j.write_text("", encoding="utf-8")
        monde["r"].sorties_autres_versions = (monde["tmp"] / "sorties-v4",)
    return sha


def test_course_v4_close_admise_avec_le_mot_de_reprise(monde):
    sha = course_v4_close(monde, journal=True)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    adm = dep["une_seule_course"]["course_close_admise"]
    assert adm == {"id": IDENT_V4, "manifeste_fin_sha256": sha, "mot_de_reprise": "GO-2026-11-18-30"}
    assert dep["une_seule_course"]["courses_lancees"] == [IDENT_V4] and len(dep["une_seule_course"]["journaux_hors_depot"]) == 1


def test_v5_ne_part_qu_une_fois_meme_avec_la_v4_close(monde, capsys):
    course_v4_close(monde)
    assert lancer(monde["r"]) == 0
    assert lancer(monde["r"]) == 2 and "tentative neuve déjà lancée" in capsys.readouterr().err


@pytest.mark.parametrize("cas", ["sans_fin", "fin_non_scellee", "fin_autre_empreinte"])
def test_course_v4_non_close_refusee(monde, cas, capsys):
    course_v4_close(monde, fin=(cas != "sans_fin"), sceller_fin=(cas != "fin_non_scellee"))
    if cas == "fin_autre_empreinte":
        monde["r"].course_close_admise = (IDENT_V4, "1" * 64)
    assert lancer(monde["r"]) == 2
    assert "non close" in capsys.readouterr().err


def test_course_v4_close_sans_mot_de_reprise_refusee(monde, capsys):
    course_v4_close(monde)
    p = piece_de_depart()
    del p["tentative_neuve"]
    _ecrire(monde, L.PIECE_DE_DEPART, p)
    assert lancer(monde["r"]) == 2 and "tentative_neuve" in capsys.readouterr().err


def test_course_v4_close_et_une_autre_course_refusee(monde, capsys):
    course_v4_close(monde)
    d = monde["r"].dossier_runs / "20261118-000000-course-auto-conception-v3"
    d.mkdir(parents=True)
    (d / "manifeste-lanceur-depart.json").write_text("{}", encoding="utf-8")
    assert lancer(monde["r"]) == 2 and "seule la course close" in capsys.readouterr().err


def test_journal_d_une_autre_course_a_cote_de_la_v4_close_refuse(monde, capsys):
    course_v4_close(monde, journal=True)
    j = monde["tmp"] / "sorties-v4" / "20261118-999999-course-auto-conception-v4" / "course.stdout.txt"
    j.parent.mkdir(parents=True)
    j.write_text("", encoding="utf-8")
    assert lancer(monde["r"]) == 2 and "journaux hors dépôt d'une autre course" in capsys.readouterr().err


def test_mutation_course_close_sans_verifier_la_fin_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "    if not fin.is_file() or not scelle(fin) or sha256_fichier(fin) != sha_fin:\n",
                        "    if False:\n", "lanceur_v6_mutant_course_close")
    course_v4_close(monde, fin=False)
    assert M.principal([], reglages=monde["r"]) == 0                          # muté : une course non close admise
    shutil.rmtree(monde["r"].dossier_runs / [p.name for p in monde["r"].dossier_runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)][0])
    shutil.rmtree(monde["r"].dossier_sorties)
    assert lancer(monde["r"]) == 2


# mot de reprise ---------------------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("modif,motif", [
    ({"tentative_neuve": None}, "tentative_neuve"),
    ({"tentative_neuve": {"course_close": IDENT_V4}}, "mot_de_reprise"),
    ({"tentative_neuve": {"course_close": IDENT_V4, "mot_de_reprise": "GO-2026-11-18-31"}}, "mot_de_reprise"),
    ({"tentative_neuve": {"course_close": "20261118-000000-course-auto-conception-v3", "mot_de_reprise": "GO-2026-11-18-30"}},
     "course_close"),
    ({"go_course": "GO-2026-11-18-20", "tentative_neuve": {"course_close": IDENT_V4, "mot_de_reprise": "GO-2026-11-18-20"}},
     "consommée"),
    ({"go_epreuve": "GO-2026-11-18-21"}, "consommée"),
])
def test_mot_de_reprise_et_lignes_neuves_artefacts(monde, modif, motif, capsys):
    p = piece_de_depart(**{k: v for k, v in modif.items() if v is not None})
    for k in [k for k, v in modif.items() if v is None]:
        del p[k]
    _ecrire(monde, L.PIECE_DE_DEPART, p)
    assert lancer(monde["r"]) == 2 and motif in capsys.readouterr().err
    assert not monde["r"].dossier_runs.exists()


def test_mot_de_reprise_au_registre_sans_tentative_neuve_refuse(monde, capsys):
    monde["main"]["registres/go.md"] = registre(perimetre_c="course d'auto-conception de l'organisme d'idéation").encode("utf-8")
    assert lancer(monde["r"]) == 2 and "tentative neuve" in capsys.readouterr().err


@pytest.mark.parametrize("texte", [registre(plafond_c="45 USD"),
                                   registre(suite="| GO-2026-11-18-41 | 2026-11-18 | révocation | GO-2026-11-18-30 | — | — | Lazar | R-4 |\n"),
                                   registre().replace("| GO-2026-11-18-30 | 2026-11-18 | calcul", "| GO-2026-11-18-30 | 2026-11-18 | décision")])
def test_mot_de_reprise_au_registre_artefacts(monde, texte):
    """Ligne de la course à 45 USD (l'orchestrateur exige 90 à l'identique), révoquée, ou d'un autre type : refus."""
    monde["main"]["registres/go.md"] = texte.encode("utf-8")
    assert lancer(monde["r"]) == 2


def test_verifier_mot_de_reprise_unitaire_sain_et_artefacts():
    p = piece_de_depart()
    texte = registre()
    assert L.verifier_mot_de_reprise(texte, AUJOURD_HUI, p)["id"] == "GO-2026-11-18-30"
    with pytest.raises(L.Refus, match="tentative neuve"):
        L.verifier_mot_de_reprise(registre(perimetre_c="auto-conception"), AUJOURD_HUI, p)
    with pytest.raises(L.Refus, match="différent"):
        L.verifier_mot_de_reprise(texte, AUJOURD_HUI, dict(p, go_course="GO-2026-11-18-32"))
    with pytest.raises(L.Refus, match="absent"):
        L.verifier_mot_de_reprise(texte, AUJOURD_HUI, {k: v for k, v in p.items() if k != "tentative_neuve"})
    with pytest.raises(L.Refus, match="hors de sa période"):
        L.verifier_mot_de_reprise(texte, dt.date(2026, 12, 1), p)


def test_mutation_mot_de_reprise_sans_tentative_neuve_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, 'MOTS_TENTATIVE_NEUVE = ("autoconception", "tentative neuve")\n',
                        'MOTS_TENTATIVE_NEUVE = ("autoconception",)\n', "lanceur_v6_mutant_mot")
    monde["main"]["registres/go.md"] = registre(perimetre_c="course d'auto-conception de l'organisme d'idéation").encode("utf-8")
    assert M.principal([], reglages=monde["r"]) == 0                          # muté : une ligne sans « tentative neuve » passe
    shutil.rmtree(monde["r"].dossier_runs)
    shutil.rmtree(monde["r"].dossier_sorties)
    assert lancer(monde["r"]) == 2


def test_mutation_lignes_consommees_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, 'LIGNES_GO_CONSOMMEES = ("GO-2026-11-18-20", "GO-2026-11-18-21", "GO-2026-11-18-36")\n',
                        "LIGNES_GO_CONSOMMEES = ()\n", "lanceur_v6_mutant_lignes")
    p = piece_de_depart(go_epreuve="GO-2026-11-18-21")
    _ecrire(monde, L.PIECE_DE_DEPART, p)
    assert M.verifier_piece_de_depart(monde["r"])["go_epreuve"] == "GO-2026-11-18-21"   # muté : la ligne de la v4 resservie
    with pytest.raises(L.Refus, match="consommée"):
        L.verifier_piece_de_depart(monde["r"])


# Carbon réglé ------------------------------------------------------------------------------------------------------------------


def _bloc_carbon(options, nom="commande_gemini_lot_v1.py"):
    return {"commande": ["/usr/local/bin/python3", "-I", "-B", f"/x/{nom}", "--url-base", "http://127.0.0.1:8792/v1beta"] + options,
            "modele_propose": "gemini-4-carbon"}


SAINES = ["--modele", "gemini-4-carbon", "--prix-entree", "8.3", "--prix-sortie", "41.5", "--provision-pensee-jetons", "28672",
          "--max-sortie-jetons", "32768", "--delai-s", "1620", "--delai-requete-s", "60"]


def _remplacer(opts, cle, valeur):
    o = list(opts)
    o[o.index(cle) + 1] = valeur
    return o


def _sans(opts, cle):
    o = list(opts)
    i = o.index(cle)
    return o[:i] + o[i + 2:]


def test_options_carbon_saines():
    c = L.controler_options_carbon(_bloc_carbon(SAINES))
    assert c["duree_au_pire_s"] == 1770.0 and c["borne_s"] == 1770.0
    assert c["valeurs"]["--provision-pensee-jetons"] == 28672 and c["valeurs"]["--max-sortie-jetons"] == 32768
    c2 = L.controler_options_carbon(_bloc_carbon(_sans(_remplacer(SAINES, "--delai-s", "1500"), "--delai-requete-s")))
    assert c2["duree_au_pire_s"] == 1770.0                     # 1 500 + 30 + 2 × 120 (défauts de la commande)


@pytest.mark.parametrize("options,motif", [
    (_sans(SAINES, "--provision-pensee-jetons"), "options exigées absentes"),
    (_sans(SAINES, "--max-sortie-jetons"), "options exigées absentes"),
    (_sans(SAINES, "--delai-s"), "options exigées absentes"),
    (_remplacer(SAINES, "--provision-pensee-jetons", "8192"), "28672 exigé"),
    (_remplacer(SAINES, "--provision-pensee-jetons", "32768"), "28672 exigé"),        # le réglage de la v5
    (_remplacer(SAINES, "--max-sortie-jetons", "16384"), "hors de"),                 # le réglage de la v5 : tronqué
    (_remplacer(SAINES, "--max-sortie-jetons", "40000"), "hors de"),
    (_remplacer(SAINES, "--delai-s", "3000"), "délai fixe"),
    (_remplacer(SAINES, "--delai-s", "1621"), "délai fixe"),
    (_remplacer(SAINES, "--delai-requete-s", "200"), "délai fixe"),
    (_sans(SAINES, "--delai-requete-s"), "délai fixe"),                               # 1 620 + 30 + 2 × 120 = 1 890
    (SAINES + ["--intervalle-s", "60"], "délai fixe"),
    (_remplacer(SAINES, "--prix-sortie", "20"), "prix"),
    (SAINES + ["--facteur-lot", "0.5"], "prix"),
    (_remplacer(SAINES, "--modele", "gemini-4-argon"), "modele_propose"),
    (SAINES + ["--provision", "8192"], "non admis"),
    (SAINES + ["--provision-pensee-jetons=8192"], "non admis"),
    (SAINES + ["--provision-pensee-jetons", "8192"], "deux fois"),
    (_sans(SAINES, "--delai-requete-s") + ["--delai-requete-s"], "sans valeur"),
    (_remplacer(SAINES, "--delai-s", "beaucoup"), "illisible"),
    (_remplacer(SAINES, "--delai-s", "nan"), "non fini"),
    (SAINES + ["--sortie-min-jetons", "40000"], "sortie-min-jetons"),
])
def test_options_carbon_artefacts_refusees(options, motif):
    with pytest.raises(L.Refus, match=motif):
        L.controler_options_carbon(_bloc_carbon(options))


def test_options_carbon_commande_absente_refusee():
    with pytest.raises(L.Refus, match="absente de la commande"):
        L.controler_options_carbon(_bloc_carbon(SAINES, nom="autre.py"))


def test_pire_cas_carbon_sain_et_artefacts():
    c = L.controler_options_carbon(_bloc_carbon(SAINES))
    p = L.pire_cas_carbon(c, 136622, 3.0)                       # plus grande entrée de la course v4, jetons comptés au pire
    assert p["max_output_tokens"] == 29271 and p["pire_cas_usd"] == pytest.approx(2.999969, abs=1e-6)
    assert p["max_output_tokens"] >= L.SORTIE_RETENUE_MIN_CARBON == 24500
    petit = L.pire_cas_carbon(c, 60000, 3.0)
    assert petit["max_output_tokens"] == 32768 and petit["pire_cas_usd"] <= 3.0
    with pytest.raises(L.Refus, match="sortie retenue"):
        L.pire_cas_carbon(c, 200_000, 3.0)                      # la commande enverrait, mais la pensée et la réponse ne tiendraient plus
    with pytest.raises(L.Refus, match="sortie retenue"):
        L.pire_cas_carbon(c, 136622, 2.0)
    with pytest.raises(L.Refus, match="sortie possible"):
        L.pire_cas_carbon(c, 136622, 1.5)                       # le plafond ne paie plus la provision et la sortie minimale
    with pytest.raises(L.Refus, match="sortie possible"):
        L.pire_cas_carbon(c, 400_000, 3.0)


def test_pire_cas_de_la_commande_elle_meme_sous_3_usd():
    """Règle de la commande épinglée (caractères / 3, marge 5 %) sur la plus grande entrée : sortie 32 768, pire cas 2,946649."""
    import math
    e = math.ceil(136622 / 3.0 * 1.05)
    sortie = int(min(32768, math.floor((3.0 - e * 8.3e-6) / 41.5e-6 - 28672)))
    pire = e * 8.3e-6 + (sortie + 28672) * 41.5e-6
    assert sortie == 32768 and pire == pytest.approx(2.946649, abs=1e-6) and pire < 3.0 and sortie >= 24500


def test_mutation_sortie_retenue_non_verifiee_attrapee(tmp_path):
    M = _mutant_lanceur(tmp_path, "    if sortie < SORTIE_RETENUE_MIN_CARBON:", "    if False:", "lanceur_v6_mutant_sortie_retenue")
    c = L.controler_options_carbon(_bloc_carbon(SAINES))
    assert M.pire_cas_carbon(c, 200_000, 3.0)["max_output_tokens"] < 24500   # muté : la réponse serait tronquée
    with pytest.raises(L.Refus, match="sortie retenue"):
        L.pire_cas_carbon(c, 200_000, 3.0)
@avec_commandes
@pytest.mark.parametrize("modif,code", [(lambda o: o, 0), (lambda o: _sans(o, "--provision-pensee-jetons"), 2),
                                        (lambda o: _remplacer(o, "--delai-s", "3000"), 2),
                                        (lambda o: _remplacer(o, "--max-sortie-jetons", "16384"), 2)])
def test_declaration_de_carbon_reglee_exigee_par_le_lanceur(monde, modif, code, capsys):
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    d = json.loads((monde["depot"] / L.DECLARATION_RELAIS).read_text(encoding="utf-8"))
    c = d["fournisseurs"]["carbon"]["commande"]
    i = c.index("--modele")
    d["fournisseurs"]["carbon"]["commande"] = c[:i] + modif(c[i:])
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert lancer(monde["r"]) == code
    if code:
        assert "fournisseurs.carbon.commande" in capsys.readouterr().err
    else:
        dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
        assert dep["carbon_regle"]["pire_cas"]["pire_cas_usd"] <= 3.0


@avec_commandes
def test_mutation_carbon_sans_borne_de_duree_attrapee(monde, tmp_path):
    M = _mutant_lanceur(tmp_path, "    if duree > borne:\n", "    if False:\n", "lanceur_v6_mutant_duree")
    b = _bloc_carbon(_remplacer(SAINES, "--delai-s", "3000"))
    assert M.controler_options_carbon(b)["duree_au_pire_s"] == 3150.0   # muté : la commande serait tuée à 1 800 s
    with pytest.raises(L.Refus, match="délai fixe"):
        L.controler_options_carbon(b)


def test_mutation_carbon_sans_provision_attrapee(tmp_path):
    M = _mutant_lanceur(tmp_path, '    if v["--provision-pensee-jetons"] != PROVISION_PENSEE_CARBON:\n', "    if False:\n",
                        "lanceur_v6_mutant_provision")
    b = _bloc_carbon(_remplacer(SAINES, "--provision-pensee-jetons", "8192"))
    assert M.controler_options_carbon(b)["valeurs"]["--provision-pensee-jetons"] == 8192   # muté : le défaut de la v4 repart
    with pytest.raises(L.Refus):
        L.controler_options_carbon(b)


def test_mutation_carbon_garde_non_appelee_attrapee(monde, tmp_path):
    """Dans `executer`, la garde des options de Carbon est appelée ; sans elle, une déclaration au réglage de la v4 partirait."""
    M = _mutant_lanceur(tmp_path, '    carbon = controler_options_carbon(decl_brute["fournisseurs"]["carbon"]) if "carbon" in decl["fournisseurs"] \\\n',
                        '    carbon = {"declare": False} if True \\\n', "lanceur_v6_mutant_appel_carbon")
    if OCTETS["carbon"] is None:
        pytest.skip("commandes absentes de origin/main")
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    d = json.loads((monde["depot"] / L.DECLARATION_RELAIS).read_text(encoding="utf-8"))
    d["fournisseurs"]["carbon"]["commande"] = _sans(d["fournisseurs"]["carbon"]["commande"], "--provision-pensee-jetons")
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert M.principal([], reglages=monde["r"]) == 0
    shutil.rmtree(monde["r"].dossier_runs)
    shutil.rmtree(monde["r"].dossier_sorties)
    assert lancer(monde["r"]) == 2


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
    M = _mutant_lanceur(tmp_path, '    if o.get("jour") != aujourd_hui.isoformat():\n', "    if False:\n", "lanceur_v6_mutant_sonde")
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
                        "    if False:\n        raise Refus(f\"composition :", "lanceur_v6_mutant_composition")
    preparer(monde)
    _ecrire(monde, L.PIECE_DE_DEPART, piece_remplie())
    d = json.loads((monde["depot"] / L.DECLARATION_RELAIS).read_text(encoding="utf-8"))
    del d["fournisseurs"]["carbon"]
    _ecrire(monde, L.DECLARATION_RELAIS, d)
    assert M.principal([], reglages=monde["r"]) == 0                          # muté : Carbon « absente » en silence
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert "prop-carbon" not in dep["especes_actives"]
