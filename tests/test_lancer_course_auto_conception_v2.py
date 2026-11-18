"""Essais du lanceur de la course d'auto-conception de l'organisme (v2 : constats de la contre-lecture de la v1 portés), de la garde de crédit v5 et de l'épreuve des témoins —
relais et orchestrateur **simulés**, aucun appel réel, aucun réseau hors de la boucle locale, aucune clé. Chaque garde est
essayée sur un cas sain et sur un artefact (R5)."""
import datetime as dt
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_auto_conception_v2.py"
_spec = importlib.util.spec_from_file_location("lancer_course_auto_conception_v2", CHEMIN_LANCEUR)
L = importlib.util.module_from_spec(_spec)
sys.modules["lancer_course_auto_conception_v2"] = L
_spec.loader.exec_module(L)
_spec_e = importlib.util.spec_from_file_location("epreuve_temoins_auto_conception_v2", RACINE / "scripts" / "epreuve_temoins_auto_conception_v2.py")
E = importlib.util.module_from_spec(_spec_e)
sys.modules["epreuve_temoins_auto_conception_v2"] = E
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
         "especes_optionnelles": {}}
    d.update(modifs)
    return d


def releve(**cles) -> dict:
    base = {CLE: {"credit_usd": 1000.0, "reste_usd": 900.0, "source": "essai"},
            "CLE_ESSAI_A": {"credit_usd": 1000.0, "reste_usd": 800.0, "source": "essai"}}
    base.update(cles)
    return {"releve_utc": "2026-11-18T07:00:00Z", "cles": base}


def contre_lecture(prereg_sha: str, lanceur_sha: str, verdict="Scellable.", suite="") -> str:
    return (f"# Contre-lecture d'essai, par le modèle K\n\nPréenregistrement : {prereg_sha}\nLanceur : {lanceur_sha}\n\n"
            f"## Verdict\n\n**{verdict}**\n" + suite)


def registre(plafond_c="90 USD", plafond_e="5 USD", perimetre_c="course d'auto-conception de l'organisme d'idéation",
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
    etat_argon = {"appels": 0, "max_appels": 200, "variable_cle_encore_presente": False}
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
                PID_ARGON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v2.py"), "--port", "8788", "--max-appels", "200",
                            "--modele", "gemini-4-argon", "--variable-cle", "CLE_ESSAI_A"],
                PID_ASTRA: [sys.executable, "-I", "-B", str(progs / "relais_kimi_v4.py"), "--amont", "https://api.openai.com",
                            "--variable-cle", "CLE_ESSAI_S", "--port", "8790", "--modeles-permis", "modele-essai-astra",
                            "--plafond-usd", "20"],
                PID_CARBON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v4.py"), "--variable-cle", "CLE_ESSAI_C",
                             "--port", "8792", "--modele", "modele-essai-carbon", "--max-lots", "20"]}
    o, commit, empreintes = faux_orchestrateur(tmp_path)
    lanceur_sha = L.sha256_fichier(CHEMIN_LANCEUR)
    ecrire_scelle(depot / L.CONTRE_LECTURE, contre_lecture(prereg_sha, lanceur_sha))
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
                   pieces=dict(L.PIECES), prereg=(prereg, prereg_sha), contre_lecture=depot / L.CONTRE_LECTURE,
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
           "etat_argon": etat_argon, "etat_astra": etat_astra, "etat_carbon": etat_carbon, "cmdlines": cmdlines, "main": fichiers_main, "commit": commit, "prereg_sha": prereg_sha}
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
    c[c.index("--max-appels") + 1] = "200"
    monde["etat_argon"]["max_appels"] = 200
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


def _piece_astra(monde, script, **opt):
    o = {"declaree": True, "risque_accepte": True, "sonde_du_jour": "R-essai"}
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


def test_carbon_relais_v4_controle(monde):
    script = monde["tmp"] / "carbon.py"
    script.write_text("import json,sys\nsys.stdin.read()\nprint(json.dumps({'texte': 'ok', 'cout_usd': 0.01}))\n", encoding="utf-8")
    carbon = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script), "--url-base", "http://127.0.0.1:8792/v1beta"],
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
    _ecrire(monde, L.CONTRE_LECTURE, contre_lecture(monde["prereg_sha"], monde["lanceur_sha"], verdict, suite))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_qui_ne_cite_pas_le_lanceur_refusee(monde):
    _ecrire(monde, L.CONTRE_LECTURE, contre_lecture(monde["prereg_sha"], "0" * 64))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_sans_modele_k_refusee(monde):
    _ecrire(monde, L.CONTRE_LECTURE, contre_lecture(monde["prereg_sha"], monde["lanceur_sha"]).replace("modèle K", "modèle J"))
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


# --- épreuve des témoins ---------------------------------------------------------------------------------------------------------


TEMOINS = {t["id"]: t for t in json.loads((RACINE / L.PIECES["temoins"][0]).read_text())["temoins"]}
ITEMS = FIXE["items_juge"]


def _verdicts(fonction):
    out = {}
    for tid, t in TEMOINS.items():
        its = fonction(t)
        out[tid] = {"items": its, "notable": all(its.values())}
    return out


def test_lecture_epreuve_parfait_et_artefacts():
    a = {tid: "niveau_methode" for tid in TEMOINS}
    assert E.lire_epreuve({"j": _verdicts(lambda t: E.verite(t, ITEMS))}, a, TEMOINS, ITEMS)["verdict"] == "réussie"
    assert E.lire_epreuve({"j": _verdicts(lambda t: {k: True for k in ITEMS})}, a, TEMOINS, ITEMS)["verdict"] == "échouée"
    assert E.lire_epreuve({"j": _verdicts(lambda t: {k: False for k in ITEMS})}, a, TEMOINS, ITEMS)["verdict"] == "échouée"
    un_manque = _verdicts(lambda t: E.verite(t, ITEMS))
    un_manque["t06"] = None
    assert E.lire_epreuve({"j": un_manque}, a, TEMOINS, ITEMS)["verdict"] == "échouée"
    parfait = _verdicts(lambda t: E.verite(t, ITEMS))
    assert E.lire_epreuve({"j": parfait}, dict(a, t03="a_corriger"), TEMOINS, ITEMS)["verdict"] == "échouée"
    assert E.lire_epreuve({"j": parfait}, dict(a, t07="concret"), TEMOINS, ITEMS)["verdict"] == "échouée"
    assert E.lire_epreuve({"j": parfait}, dict(a, t07="a_corriger"), TEMOINS, ITEMS)["verdict"] == "réussie"
    assert E.lire_epreuve({}, a, TEMOINS, ITEMS)["verdict"] == "échouée"


def test_temoins_couvrent_chaque_item_et_aucune_regle_de_longueur():
    s = E.controles_statiques(TEMOINS, ITEMS, (RACINE / L.PIECES["consigne_proposeur"][0]).read_text(), MATIERE)
    assert s["items_plantes_tous_couverts"] and s["bornes_tenues"] and s["champs_identiques"]
    assert s["regle_de_seuil_sur_la_longueur_erreurs_min"] >= 1 and not s["titres_de_temoin_dans_la_consigne_servie"]
    if MATIERE is not None:
        assert s["identifiants_absents_de_la_matiere"] == []
    assert sorted(TEMOINS["t01"]["contenu"]) == sorted(FIXE["champs_fiche"])


@avec_matiere
def test_epreuve_hors_ligne_bout_en_bout(tmp_path):
    m = tmp_path / "matiere-v3.md"
    m.write_bytes(MATIERE)
    orch = E.orchestrateur_present(L.ORCHESTRATEURS_CANDIDATS)
    rap = E.hors_ligne(tmp_path / "epreuve", m, orch)
    assert rap["conclusion"]["verdict"] == "témoins éprouvés hors ligne"
    assert rap["lectures"]["parfait"]["verdict"] == "réussie" and rap["juges_au_hasard_reussis"] == 0
    assert all(rap["lectures"][n]["verdict"] == "échouée" for n in ("longueur", "indulgent", "severe"))
    assert rap["artefact_aiguilleur_tout_concret"] == "échouée"


def test_epreuve_reelle_refuse_un_environnement_avec_cle(monkeypatch):
    monkeypatch.setenv("UNE_API_KEY", "x")
    with pytest.raises(Exception) as e:
        E.reel()
    assert type(e.value).__name__ == "Refus" and "UNE_API_KEY" in str(e.value)


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


def test_temoins_v2_entrelaces_par_champ_lu():
    s = E.controles_statiques(TEMOINS, ITEMS, (RACINE / L.PIECES["consigne_proposeur"][0]).read_text(), MATIERE)
    assert s["regle_de_seuil_sur_le_champ_lu_erreurs_min"] >= 1
    assert "même dépense totale" in TEMOINS["t02"]["contenu"]["epreuve_monde_plante"]
    assert "jamais employée pour écarter" in TEMOINS["t03"]["contenu"]["module_change"]
