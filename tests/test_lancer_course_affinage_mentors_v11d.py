"""Essais du lanceur v11d (dérivés des essais v11c, `88a61acd…` : régression R1 de l'essai à blanc, configuration v11d, gabarit du
relevé des crédits v11d). Texte d'origine : essais du lanceur v11c (dérivés des essais v11b, `673a20d2…`, par remplacements exacts : corrections de la contre-lecture du lanceur v11b, réglages de production — 4 / 20 USD, juge à 1,00). Texte d'origine : essais du lanceur v11b (dérivés des essais v11, `297f1eed…`, par remplacements exacts ; GO_ID de la course = GO-2026-11-22-80). Texte d'origine : essais du lanceur v11 de la course d'affinage des idées des mentors : ceux de la v10 (branche prep/affinage-v10, `tests/test_lancer_course_affinage_mentors_v11.py`, `4e651669…`) portés par transformation (clé LUC, Astra gpt-6.2-astra sur OPENAI_API_KEY_2, sonde v3 et sonde commune v2 sous course-v11/, Carbon en flux par le relais Gemini v3 au port 8791, préenregistrement d'essai, garde Google remplacée par un double conforme dans les essais de bout en bout) ; les essais propres à la commande par lot et ceux qui relisent des pièces des branches prep (lanceurs v7 à v9, commandes et gabarits v10) sont retirés (liste au rapport du développeur v11) ; les essais propres à la v11 sont en fin de fichier.

Texte des essais v10 : Essais du lanceur v10 de la course d'affinage des idées des mentors — les essais de la v9 portés (lanceur v10, chemins `course-v10/`, commandes et gabarit v10 ; la configuration v9 est inchangée), puis les essais neufs de la v10 en fin de fichier : lanceur v10 = lanceur v9 à l'épingle du préenregistrement et aux chemins près (source reconstituée à l'octet près), textes v10 qui disent le plafond dur souple de l'orchestrateur épinglé (recoupé par sa vraie classe de budget), mutations des textes, devis, gabarits, essai à blanc v10.

Texte des essais v9 : essais du lanceur v9 de la course d'affinage des idées des mentors — les essais de la v8 portés (configuration v9 : plafond de session des proposeurs 3,00 USD ; parts au pire d'Astra et de Carbon 48, clé partagée 198 ; relais d'Astra à 48 USD dans le monde d'essai ; réglages de Carbon v9 : sortie retenue 32 768, pire cas 2,5715), puis les essais neufs de la v9 en fin de fichier.

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
CHEMIN_LANCEUR = RACINE / "scripts" / "lancer_course_affinage_mentors_v11d.py"
_spec = importlib.util.spec_from_file_location("lancer_course_affinage_mentors_v11d", CHEMIN_LANCEUR)
L = importlib.util.module_from_spec(_spec)
sys.modules["lancer_course_affinage_mentors_v11d"] = L
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
        "claude": {"type": "claude_sdk", "url_relais": url, "nom_cle": "RR_ANTHROPIC_API_KEY_LUC", "porte_plafond": porte,
                   "pid_relais": PID_CLAUDE},
        "argon": {"type": "commande_externe",
                  "commande": [sys.executable, "-I", "-B", str(depot / L.PIECES["commande_carbon"][0])] + L.ARGUMENTS_COMMANDES["argon"],
                  "nom_cle": "CLE_ESSAI_A", "porte_plafond": {"type": "environnement"}, "pid_relais": PID_ARGON}}}
    d["fournisseurs"].update(modifs)
    if "kimi" in modifs and mot_kimi is not None:  # v6 : Kimi non déclaré par défaut, mot écrit de la mère exigé
        d["kimi_autorise_par_la_mere"] = {"reference": "R-9001"} if mot_kimi is ... else mot_kimi
    return d


def luc(**modifs) -> dict:
    """Ligne de la clé Claude au format v11c (constat 3 ; GO-2026-11-22-124) : « solde non lu », référence, aucun montant."""
    o = {"solde_non_lu": True, "reference": "GO-2026-11-22-124", "source": "essai : relevé du jour"}
    o.update(modifs)
    return o


def releve(**cles) -> dict:
    base = {"RR_ANTHROPIC_API_KEY_LUC": luc(),
            "CLE_ESSAI_A": {"credit_usd": 1000.0, "reste_usd": 800.0, "source": "essai"}}
    base.update(cles)
    return {"releve_utc": "2026-11-18T07:00:00Z", "cles": base}


def contre_lecture(prereg_sha: str, lanceur_sha: str, verdict="Scellable.", suite="") -> str:
    return (f"# Contre-lecture d'essai, Opus 5.5, contre-lecteur neuf\n\nPréenregistrement : {prereg_sha}\nLanceur : {lanceur_sha}\n\n"
            f"## Verdict\n\n**{verdict}**\n" + suite)


def ligne_go(plafond="150 USD (plafond de GO-2026-11-18-14)", perimetre="course d'affinage des idées des mentors (organisme d'idéation)"):
    # v11b : GO-2026-11-18-14 (prolongé) et GO-2026-11-22-80 (GO de la course, qui le prolonge) ; accordés « le 18 » : monde d'essai
    return (f"| id | accordé le | type | périmètre | plafond | échéance | accordé par | réf. |\n|---|---|---|---|---|---|---|---|\n"
            "| GO-2026-11-18-14 | 2026-11-18 | calcul | course d'affinage des idées des mentors | 150 USD | 2026-11-25 | Lazar | R-3215 |\n"
            f"| {L.GO_ID} | 2026-11-18 | calcul | Prolongation de GO-2026-11-18-14 ({perimetre}) | {plafond} | 2026-12-15 | Lazar | "
            "GO-2026-11-22-77 |\n" + LIGNE_GO_CLE + LIGNE_GO_SIMPL)


LIGNE_GO_CLE = ("| GO-2026-11-22-107 | 2026-11-18 | calcul | course d'affinage des idées des mentors : exception déclarée à la règle "
                "« Claude par l'abonnement » (GO-2026-11-22-70), clé RR_ANTHROPIC_API_KEY_LUC | sous le plafond d'arrêt de "
                "GO-2026-11-18-14 (150 USD) | 2026-11-25 | Lazar | GO-2026-11-18-14 |\n")  # accordée « le 18 » : date du monde d'essai
LIGNE_GO_SIMPL = ("| GO-2026-11-22-124 | 2026-11-18 | calcul | affinage de l'organisme : plancher levé, solde de LUC non lu ; exception "
                  "de GO-2026-11-22-107 prolongée au 15 décembre | inchangé (150 USD ; part Claude 45 USD) | 2026-12-15 | Lazar | "
                  "mot direct |\n")


SHA_ASTRA = L.COMMANDES_EPINGLEES["astra"]["commande_astra_v1.py"]


def sonde_astra(**modifs) -> dict:
    o = {"version": "sonde_astra_affinage_v3", "horodatage_utc": "2026-11-18T07:30:00Z", "code": 0, "ok": True, "cout_usd": 0.004,
         "modele_servi": "gpt-6.2-astra", "commande_sha256": SHA_ASTRA,
         "relais_url": "http://127.0.0.1:18790", "relais_pid": 999}
    o.update(modifs)
    return o


COMMUNE_DU_JOUR = "docs/notes/organisme-affinage-mentors-v1/course-v11/sonde-astra-commune-2026-11-18-v2.json"


def sonde_commune(v2_rel: str, v2_sha: str, pid: int = 999, commande_sha: str = SHA_ASTRA, **modifs) -> dict:
    """v7 : rapport de la sonde commune (format de `scripts/sonde_astra_courses_v1.py`) qui cite le rapport v2."""
    o = {"version": "sonde_astra_courses_v3", "horodatage_utc": "2026-11-18T07:29:55Z", "jour": "2026-11-18", "ok": True,
         "echec_de_configuration": False, "appel_envoye": True, "cout_usd": 0.004, "depense_relais_usd": 0.004, "motif": None,
         "commande": {"chemin": "/tmp/commande_astra_v1.py", "sha256": commande_sha},
         "sonde_v2": {"chemin": "scripts/sonde_astra_affinage_v3.py", "sha256": L.PIECES["sonde_astra"][1]},
         "relais_jete": {"pid": pid, "port": 8793, "url": "http://127.0.0.1:8793", "max_appels": 1, "plafond_usd": 0.05,
                         "reserve_par_appel_usd": 0.01, "programme_sha256": L.PROGRAMMES_RELAIS["astra"][1],
                         "variable_cle": "OPENAI_API_KEY_2"},
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


PREREG_TEXTE = "# Préenregistrement d'ESSAI de la course d'affinage v11 (aucune valeur réelle)\n"
PREREG_SHA = hashlib.sha256(PREREG_TEXTE.encode("utf-8")).hexdigest()


def _octets_de_main(rel: str) -> bytes | None:
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"refs/remotes/origin/main:{rel}"], capture_output=True)
    return p.stdout if p.returncode == 0 else None


def octets_piece(rel: str) -> bytes:
    """Pièce du dépôt, ou de `origin/main` si elle n'est pas sur cette branche (garde Google)."""
    p = RACINE / rel
    return p.read_bytes() if p.is_file() else (_octets_de_main(rel) or b"")


def garde_google_factice(r, decl, pieces, fixe, liste):
    """Garde Google remplacée dans les essais de bout en bout : l'Argon réel ne passe pas la garde (voir les essais v11)."""
    return {"essai": "garde Google remplacée par un double conforme", **{n: {"conforme": True, "roles": []}
                                                                        for n in ("argon", "carbon") if n in decl["fournisseurs"]}}


@pytest.fixture
def monde(tmp_path):
    """Dépôt d'essai : vraies pièces copiées (mêmes empreintes que les épingles), faux orchestrateur, relais simulés."""
    depot = tmp_path / "depot"
    for rel, _ in L.PIECES.values():
        (depot / rel).parent.mkdir(parents=True, exist_ok=True)
        (depot / rel).write_bytes(octets_piece(rel))
    conf_rel = L.PIECES["configuration"][0]                       # v11 : emplacement des juges rempli dans le monde d'essai
    o_conf = json.loads((depot / conf_rel).read_text(encoding="utf-8"))
    o_conf["argon_v11"]["plafond_session_juge_usd"] = 1.0           # v11c : production (constats 10 et 13)
    (depot / conf_rel).write_text(json.dumps(o_conf, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    pieces_essai = dict(L.PIECES, configuration=(conf_rel, hashlib.sha256((depot / conf_rel).read_bytes()).hexdigest()))
    prereg = depot / L.PREREG
    prereg.parent.mkdir(parents=True, exist_ok=True)
    prereg.write_text(PREREG_TEXTE, encoding="utf-8")
    sceller(prereg)
    etat_claude = {"plafond_usd": 45.0, "depense_usd": 0.0, "engage_usd": 0.0, "appels": 0, "modeles_permis": list(MODELES_CLAUDE),
                   "reserve_par_appel_usd": 0.4, "refus": 0, "appels_au_dessus_de_la_reserve": 0, "depassement_max_usd": 0.0}
    etat_kimi = {"plafond_usd": 30.0, "depense_usd": 0.0, "engage_usd": 0.0, "appels": 0, "modeles_permis": ["kimi-k3.1-pro"],
                 "max_appels": 20, "variable_cle_encore_presente": False, "reserve_par_appel_usd": 0.4}
    s_claude, s_kimi = serveur(etat_claude), serveur(etat_kimi)
    CONTEXTE.update(url_claude=f"http://127.0.0.1:{s_claude.server_address[1]}", url_kimi=f"http://127.0.0.1:{s_kimi.server_address[1]}")
    progs = tmp_path / "progs"
    progs.mkdir()
    (progs / "relais_reel.py").write_text("# relais factice\n", encoding="utf-8")
    (progs / "relais_kimi_v4.py").write_text("# relais factice kimi\n", encoding="utf-8")
    (progs / "relais_gemini_v2.py").write_text("# relais factice gemini v2\n", encoding="utf-8")
    (progs / "relais_gemini_v3.py").write_text("# relais factice gemini v3 en flux\n", encoding="utf-8")
    etats_gemini = {"8788": {"appels": 0, "variable_cle_encore_presente": False, "modeles": ["gemini-4-argon"], "max_appels": 450},
                    "8791": {"appels": 0, "variable_cle_encore_presente": False, "modeles": ["gemini-4-carbon"], "max_appels": 40},
                    "8790": {"appels": 0, "depense_usd": 0.0, "engage_usd": 0.0, "plafond_usd": 48.0, "modeles_permis": ["gpt-6.2-astra"],
                             "max_appels": 20, "variable_cle_encore_presente": False, "reserve_par_appel_usd": 0.4,
                             "prix_entree_usd_par_million": 8.0, "prix_sortie_usd_par_million": 40.0}}
    cmdlines = {PID_CLAUDE: [sys.executable, "-I", "-B", str(progs / "relais_reel.py"), "--variable-cle", "RR_ANTHROPIC_API_KEY_LUC",
                             "--port", CONTEXTE["url_claude"].rsplit(":", 1)[1], "--plafond-usd", "45", "--journal", str(tmp_path / "journal-relais-claude.jsonl"),
                             "--modeles-permis",
                             ",".join(MODELES_CLAUDE)],
                PID_KIMI: [sys.executable, "-I", "-B", str(progs / "relais_kimi_v4.py"), "--variable-cle", "CLE_ESSAI_K",
                           "--port", CONTEXTE["url_kimi"].rsplit(":", 1)[1], "--plafond-usd", "30", "--modeles-permis", "kimi-k3.1-pro",
                           "--max-appels", "20"],
                PID_ARGON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v3.py"), "--variable-cle", "CLE_ESSAI_A",
                            "--port", "8788", "--max-appels", "450", "--delai-silence-s", "240", "--delai-amont-s", "1800",
                            "--modele", "gemini-4-argon"],
                PID_ASTRA: [sys.executable, "-I", "-B", str(progs / "relais_kimi_v4.py"), "--amont", "https://api.openai.com",
                            "--variable-cle", "OPENAI_API_KEY_2", "--port", "8790", "--modeles-permis", "gpt-6.2-astra", "--plafond-usd", "48",
                            "--max-appels", "20"],
                PID_CARBON: [sys.executable, "-I", "-B", str(progs / "relais_gemini_v3.py"), "--variable-cle", "CLE_ESSAI_G",
                             "--port", "8791", "--max-appels", "40", "--delai-silence-s", "240", "--delai-amont-s", "1800",
                             "--modele", "gemini-4-carbon"]}
    o, commit, empreintes = faux_orchestrateur(tmp_path)
    lanceur_sha = hashlib.sha256(CHEMIN_LANCEUR.read_bytes()).hexdigest()
    ecrire_scelle(depot / L.CONTRE_LECTURE, contre_lecture(PREREG_SHA, lanceur_sha))
    ecrire_scelle(depot / L.DECLARATION_RELAIS, declaration(depot))
    ecrire_scelle(depot / L.RELEVE_CREDITS, releve())
    ecrire_scelle(depot / L.RELEVE_PRIX, releve_prix())
    ecrire_sondes(depot)
    CONTEXTE["sonde"] = depot / L.SONDE_ASTRA
    (depot / "registres").mkdir()
    (depot / "registres" / "go.md").write_text(ligne_go(), encoding="utf-8")
    r = L.Reglages(depot=depot, orchestrateurs=(o,), commit_orchestrateur=commit, empreintes_orchestrateur=empreintes,
                   pieces=pieces_essai, prereg=(prereg, PREREG_SHA), contre_lecture=depot / L.CONTRE_LECTURE,
                   declaration=depot / L.DECLARATION_RELAIS, releve=depot / L.RELEVE_CREDITS,
                   registre_go=depot / "registres" / "go.md", procedure_relais=depot / L.PROCEDURE_RELAIS,
                   releve_prix=depot / L.RELEVE_PRIX, references_kimi_admises=("R-9001",), ref_registre=None, dossier_runs=depot / "runs", dossier_sorties=tmp_path / "sorties",
                   depot_attendu_par_l_enveloppe=depot, python=sys.executable, lanceur=CHEMIN_LANCEUR, moteur="reel",
                   environnement={"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "RR_ANTHROPIC_API_KEY_LUC": "valeur-secrete-essai-1",
                                  "RR_ANTHROPIC_API_KEY_RIGAUD": "valeur-secrete-essai-2"},
                   aujourd_hui=AUJOURD_HUI, horodatage=lambda: "Wed Nov 18 07:00:00 UTC 2026",
                   sorties_courses=tuple(tmp_path / f"sorties-anciennes-v{k}" for k in range(1, 12)),
                   programmes_relais={"claude": ("relais_reel.py", hashlib.sha256((progs / "relais_reel.py").read_bytes()).hexdigest()),
                                      "kimi": ("relais_kimi_v4.py", hashlib.sha256((progs / "relais_kimi_v4.py").read_bytes()).hexdigest()),
                                      "astra": ("relais_kimi_v4.py", hashlib.sha256((progs / "relais_kimi_v4.py").read_bytes()).hexdigest()),
                                      "argon": ("relais_gemini_v3.py", hashlib.sha256((progs / "relais_gemini_v3.py").read_bytes()).hexdigest()),
                                      "carbon": ("relais_gemini_v3.py", hashlib.sha256((progs / "relais_gemini_v3.py").read_bytes()).hexdigest())},
                   lire_cmdline=lambda pid: list(cmdlines[pid]),
                   lire_etat_relais=lambda url: dict(etats_par_port[url.rsplit(":", 1)[1]]),
                   controler_google=garde_google_factice, intervalle_surveillance_s=0.05)
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
    assert dep["preenregistrement"]["sha256"] == PREREG_SHA and dep["go"]["plafond_lu"] == 150.0
    # espèces : Claude et Argon seuls déclarés → Kimi, Astra absentes ; Carbon non active
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon"]
    assert dep["carbon"]["active"] is False
    # (5) coût réel par relais, écart au devis
    assert fin["cout_reel"]["par_relais_usd"] == {"claude": 16.0, "argon": 9.0}
    assert fin["ecart_au_devis"]["par_role"]["prop-opus"]["devis_usd"] == pytest.approx(0.141)
    assert fin["releve_credits_apres"]["RR_ANTHROPIC_API_KEY_LUC"]["lisible"] is False                # GO-124 : solde non lu
    assert fin["alertes_apres"] == [] and fin["plafond_arret"]["depasse"] is False
    # l'orchestrateur a reçu seize cases, les retraits en étiquettes interdites, aucun nom de clé dans son environnement
    vu = json.loads((Path(dep["sortie"]) / "vu.json").read_text())
    assert vu["cases"] == 16 and "S3" in vu["interdites"] and "fc62b4ca23035" in vu["interdites"]
    assert "--confirmer-moteur-reel" in vu["argv"] and "--registre-go" in vu["argv"]
    noms = json.loads((Path(dep["sortie"]) / "env-noms.json").read_text())
    assert "RR_ANTHROPIC_API_KEY_LUC" not in noms and "RR_ANTHROPIC_API_KEY_RIGAUD" not in noms and "GO_ID" in noms
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
    # v11 : la règle du cinquième vaut pour les clés au crédit lisible hors Claude (ici celle d'Argon)
    _releve(monde, releve(CLE_ESSAI_A={"credit_usd": 5000.0, "reste_usd": 900.0, "source": "essai"}))
    assert lancer(monde["r"]) == 3
    alertes = [p for p in monde["r"].dossier_runs.iterdir() if p.name.endswith("-alerte-credits-affinage-mentors-v11")]
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
        _cl(monde, contre_lecture(PREREG_SHA, monde["lanceur_sha"], verdict))
        assert lancer(monde["r"]) == 2, verdict


def test_contre_lecture_qui_ne_cite_pas_le_lanceur_refusee(monde):
    _cl(monde, contre_lecture(PREREG_SHA, "0" * 64))
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
    d["fournisseurs"]["argon"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_LUC"
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


def test_luc_ligne_du_releve_non_lue_go_124(monde):
    # GO-2026-11-22-124 : le solde de LUC n'est pas lu ; « Minuit compté au prix relevé » est retiré ; la ligne est recopiée
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC=luc(note="solde non lu (GO-124)")))
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    c = dep["releve_credits_avant"]["cles"][L.CLE_CLAUDE]
    assert c["condition_de_depart"] is None and c["ligne_du_releve"]["solde_non_lu"] is True and c["plafond_part_claude_usd"] == 45.0
    assert dep["cle_par_espece"]["prop-opus"] == L.CLE_CLAUDE and dep["cle_par_role_interne"]["aiguilleur"] == L.CLE_CLAUDE
    assert dep["cle_claude"]["exception"] == "GO-2026-11-22-107" and dep["go_simplification_cle"]["id"] == "GO-2026-11-22-124"
    assert not hasattr(L, "CREDIT_DECLARE_CLE_CLAUDE_USD")


def test_contre_lecture_qui_dit_n_avoir_pas_relu_refusee(monde):
    _cl(monde, contre_lecture(PREREG_SHA, monde["lanceur_sha"], suite="\nLimite : je n'ai pas relu le lanceur en entier.\n"))
    assert lancer(monde["r"]) == 2


def test_contre_lecture_sans_modele_k_refusee(monde):
    _cl(monde, contre_lecture(PREREG_SHA, monde["lanceur_sha"]).replace("Opus 5.5, contre-lecteur neuf", "par le modèle K"))
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
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(sa)] + L.ARGUMENTS_COMMANDES["astra"], "modele_propose": "gpt-6.2-astra", "pid_relais": PID_ASTRA, "nom_cle": "OPENAI_API_KEY_2",
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
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script)] + L.ARGUMENTS_COMMANDES["astra"], "modele_propose": "gpt-6.2-astra", "pid_relais": PID_ASTRA,
             "nom_cle": "OPENAI_API_KEY_2", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    _releve(monde, releve(OPENAI_API_KEY_2={"credit_usd": 60.0, "reste_usd": 60.0, "source": "essai"}))
    assert lancer(monde["r"]) == 0
    _releve(monde, releve(OPENAI_API_KEY_2={"credit_usd": 60.0, "reste_usd": 47.0, "source": "essai"}))
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
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(script)] + L.ARGUMENTS_COMMANDES["astra"], "modele_propose": "gpt-6.2-astra", "pid_relais": PID_ASTRA,
             "nom_cle": "OPENAI_API_KEY_2", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    objet = releve(OPENAI_API_KEY_2={"non_lisible": True, "motif": "solde illisible (R-3222)"})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["OPENAI_API_KEY_2"]}
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
    assert dep["procedure_relais_persistants"]["relais_vivants"]["claude"]["variable_cle"] == "RR_ANTHROPIC_API_KEY_LUC"
    assert dep["releve_prix_claude"]["egal_au_bareme"] is True
    assert dep["registre_go_derive"]["nombre_de_lignes"] == 2  # v11b : GO-80 et GO-14


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
    faux.write_text(Path(d["derive"]).read_text().replace("| 150 USD (plafond de GO-2026-11-18-14) |", "| 140 USD |"), encoding="utf-8")
    with pytest.raises(GoRefuse):
        verifier_go_v55(L.GO_ID, str(faux), 150.0, aujourd_hui=AUJOURD_HUI)
    assert lancer(monde["r"]) == 0  # le lanceur part avec le registre à doublons de main
    vu = json.loads((Path(json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())["sortie"]) / "vu.json").read_text())
    assert vu["argv"][vu["argv"].index("--registre-go") + 1].endswith("registre-go-derive.md")


def test_revocation_incluse_au_registre_derive(monde, tmp_path):
    _registre(monde, ligne_go() + f"| GO-2026-11-19-01 | 2026-11-19 | révocation | révoque {L.GO_ID} | — | — | Lazar | R-9 |\n")
    d = L.ecrire_registre_derive(monde["r"].registre_go, tmp_path / "derive.md")
    assert d["nombre_de_lignes"] == 3  # v11b : GO-80, GO-14 et la révocation


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
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(s)] + L.ARGUMENTS_COMMANDES["astra"], "modele_propose": "gpt-6.2-astra", "pid_relais": PID_ASTRA,
             "nom_cle": "OPENAI_API_KEY_2", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    _releve(monde, releve(OPENAI_API_KEY_2={"credit_usd": 60.0, "reste_usd": 60.0, "source": "essai"}))
    assert lancer(monde["r"]) == 2


def test_reste_egal_a_la_part_refuse(monde, monkeypatch):
    s = script_commande(monde["tmp"], "astra", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "astra", s)
    astra = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(s)] + L.ARGUMENTS_COMMANDES["astra"], "modele_propose": "gpt-6.2-astra", "pid_relais": PID_ASTRA,
             "nom_cle": "OPENAI_API_KEY_2", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=astra))
    _releve(monde, releve(OPENAI_API_KEY_2={"credit_usd": 100.0, "reste_usd": 48.0, "source": "essai"}))
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
    sc = script_commande(monde["tmp"], "commande_gemini_flux_v2", {"texte": "", "cout_usd": 0.01})
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
    rv = dep["procedure_relais_persistants"]["relais_vivants"]["carbon"]                       # v11 : relais v3 en flux
    assert rv["max_appels"] == 40 and rv["delai_silence_s"] == 240.0 and rv["delai_amont_s"] == 1800.0
    assert dep["reglages_carbon_v11_flux"]["cas"]["entree_la_plus_longue"]["pire_cas_appel_usd"] <= 3.00


def test_carbon_arguments_autres_refuses(monde, monkeypatch):
    sc = script_commande(monde["tmp"], "commande_gemini_flux_v2", {"texte": "", "cout_usd": 0.01})
    args = list(L.ARGUMENTS_COMMANDES["carbon"])
    args[args.index("--delai-s") + 1] = "3000"
    _carbon(monde, monkeypatch, commande=[sys.executable, "-I", "-B", str(sc)] + args)
    assert lancer(monde["r"]) == 2


def _astra(monde, monkeypatch):
    s = script_commande(monde["tmp"], "commande_astra_v1", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "astra", s)
    a = {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(s)] + L.ARGUMENTS_COMMANDES["astra"],
         "modele_propose": "gpt-6.2-astra", "pid_relais": PID_ASTRA, "nom_cle": "OPENAI_API_KEY_2", "porte_plafond": {"type": "environnement"}}
    _decl(monde, declaration(monde["depot"], astra=a))
    _releve(monde, releve(OPENAI_API_KEY_2={"credit_usd": 100.0, "reste_usd": 90.0, "source": "essai"}))
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
    spec = importlib.util.spec_from_file_location("sonde_v2", RACINE / "scripts" / "sonde_astra_affinage_v3.py")
    S = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(S)
    for cout, servi, attendu in ((0.004, "gpt-6.2-astra", True), (0.06, "gpt-6.2-astra", False), (0.004, "autre-modele", False)):
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
    for t in ("écrire à quelqu'un@exemple.org", "voir session_01ABCDEFGH", "selon Lazar", "clé RR_ANTHROPIC_API_KEY_LUC",
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
    chemin, sha = L.CHEMINS_MAIN_COMMANDES["astra"], L.COMMANDES_EPINGLEES["astra"]["commande_astra_v1.py"]  # v11 : Carbon hors de main
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
    sc = script_commande(monde["tmp"], "commande_gemini_flux_v2", {"texte": "", "cout_usd": 0.01})
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
    spec = importlib.util.spec_from_file_location("sonde_v2_r", RACINE / "scripts" / "sonde_astra_affinage_v3.py")
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
    spec = importlib.util.spec_from_file_location("sonde_v2_b", RACINE / "scripts" / "sonde_astra_affinage_v3.py")
    S = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(S)
    assert S.VERSION == "sonde_astra_affinage_v3" and S.PLAFOND_USD == 0.05
    c = tmp_path / "cmd.py"
    c.write_text("import json,sys\nsys.stdin.read()\njson.dump(sys.argv[1:], open(" + repr(str(tmp_path / "argv.json"))
                 + ", 'w'))\nprint(json.dumps({'texte': 'prêt', 'cout_usd': 0.004, 'modele_servi': 'gpt-6.2-astra'}))\n", encoding="utf-8")
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
    assert "course-affinage-mentors-v11" in L.SUFFIXE_RUN and "-course-affinage-mentors-v10" in L.SUFFIXES_DEJA_LANCEE


# =================================================================================================================================
# v7 — essais neufs : un cas sain et un artefact (R5) par garde neuve ; une mutation par majeur ; essais v6b portés.
# =================================================================================================================================

PARTS_ASTRA = {"astra": {"part_au_pire_usd": 48.0}}  # v9
B_ASTRA = {"pid_relais": PID_ASTRA, "nom_cle": "OPENAI_API_KEY_2"}
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
    """v11 : relais Gemini v3 en flux : --max-appels ≥ 40, délais explicites (silence ≤ 240 s, amont ≥ 1 500 s), pensées
    demandées à l'amont, état neuf."""
    out = L.controler_relais_vivant(monde["r"], "carbon", dict(B_CARBON), FIXE, 5, None)
    assert out["max_appels"] == 40 and out["delai_silence_s"] == 240.0 and out["delai_amont_s"] == 1800.0
    base = list(monde["cmdlines"][PID_CARBON])
    for args, etat, motif in ((["--max-appels", "32"], {"max_appels": 32}, "max-appels 32 < 40"),
                              (["--delai-silence-s", None], {}, "--delai-silence-s absent"),
                              (["--delai-silence-s", "300"], {}, "delai-silence-s 300"),
                              (["--delai-amont-s", None], {}, "--delai-amont-s absent"),
                              (["--delai-amont-s", "1000"], {}, "delai-amont-s 1000"),
                              (["--sans-pensees-amont", "AJOUT"], {}, "sans-pensees-amont"),
                              ([], {"max_appels": 8}, "max_appels"),
                              ([], {"appels": 1}, "déjà employé"),
                              ([], {"appels": None}, "sans")):
        a = list(base)
        if args:
            if args[1] == "AJOUT":
                a.append(args[0])
            else:
                k = a.index(args[0])
                if args[1] is None:
                    del a[k:k + 2]
                else:
                    a[k + 1] = args[1]
        monde["cmdlines"][PID_CARBON] = a
        sauve = dict(monde["etats"]["8791"])
        for cle, v in etat.items():
            if v is None:
                monde["etats"]["8791"].pop(cle)
            else:
                monde["etats"]["8791"][cle] = v
        with pytest.raises(L.Refus, match=motif):
            L.controler_relais_vivant(monde["r"], "carbon", dict(B_CARBON), FIXE, 5, None)
        monde["etats"]["8791"].clear()
        monde["etats"]["8791"].update(sauve)
        monde["cmdlines"][PID_CARBON] = list(base)


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
    ("claude", {"pid_relais": PID_CLAUDE, "nom_cle": "RR_ANTHROPIC_API_KEY_LUC"}, None),
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
    b = {"pid_relais": PID_CLAUDE, "nom_cle": "RR_ANTHROPIC_API_KEY_LUC", "url_relais": CONTEXTE["url_claude"]}
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


def test_v7_sonde_commune_epinglee():
    assert L.PIECES["sonde_commune"][0] == "scripts/sonde_astra_courses_v3.py"            # v11c : sonde commune v3
    assert L.PIECES["sonde_commune"][1] == hashlib.sha256((RACINE / "scripts/sonde_astra_courses_v3.py").read_bytes()).hexdigest()
    assert L.PIECES["sonde_astra"][0] == "scripts/sonde_astra_affinage_v3.py"


def test_v7_devis_sur_les_especes_actives():
    v6b = ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]
    assert round(L.devis_estimation(v6b), 3) == 35.683                           # v11c : base du texte (Argon à 4 / 20)
    assert L.devis_estimation(v6b + ["prop-kimi"]) == pytest.approx(42.81056)     # six espèces
    assert L.devis_estimation(v6b) != pytest.approx(L.DEVIS_V5_TOTAL["six_especes"])  # artefact de la v6 : 45,28 pour cinq
    trois = ["prop-opus", "prop-fable", "prop-argon"]
    assert L.devis_estimation(trois) == pytest.approx(16 * (0.141 + 0.3525 + 0.133012) + 96 * (0.031 + 0.037 + 0.016723))
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
    b = {"pid_relais": PID_CLAUDE, "nom_cle": "RR_ANTHROPIC_API_KEY_LUC", "url_relais": CONTEXTE["url_claude"]}
    m["etat_claude"].clear()
    m["etat_claude"]["plafond_usd"] = 45.0  # v11 : relais Claude au plafond de la part
    m["etat_claude"]["reserve_par_appel_usd"] = 0.4  # v11c : la réserve lue n'est pas ce que l'essai mord
    with pytest.raises(module.Refus):
        module.controler_relais_vivant(m["r"], "claude", b, FIXE, 5, None)


def test_mutation_mineur_3_etat_vide(monde):
    """La lecture de la v6 (champs absents tenus pour nuls) réintroduite : l'essai de l'état vide échoue."""
    m = _mutant("lanceur_v7_mutant_mineur_3", [
        ('    champs = ("appels",) + (("depense_usd", "engage_usd") if nom in RELAIS_A_DOLLARS else ())  # v11 : plus de lots pour Carbon\n',
         "    champs = ()\n")])
    with pytest.raises(pytest.fail.Exception):
        essai_etat_vide_refuse(m, monde)
    essai_etat_vide_refuse(L, monde)




# =================================================================================================================================
# Essais propres à la v11 : clé LUC (couverture au fil de l'eau, plafond propre de 45 USD), exception de clé, Astra
# gpt-6.2-astra, Carbon en flux sous la garde Google, garde des appels à Google. Un cas sain et un artefact par garde (R5) ;
# mutations demandées par la mère (Minuit réintroduit, ancien Astra, Carbon sans réglage de réflexion, plafond retiré ou relevé).
# =================================================================================================================================


def _etat_claude_apres_depart(m, **etat):
    """Après le manifeste de départ, le relais Claude rend `etat` (avant : l'état neuf du monde) ; `etat` vide = illisible."""
    base = m["r"].lire_etat_relais
    port = CONTEXTE["url_claude"].rsplit(":", 1)[1]
    vu = {"lectures": 0}

    def lire(url):
        if url.rsplit(":", 1)[1] == port and any(m["r"].dossier_runs.glob("*/manifeste-lanceur-depart.json")):
            vu["lectures"] += 1
            if not etat:
                raise OSError("relais Claude injoignable (essai)")
            return dict(base(url), **etat)
        return base(url)
    m["r"].lire_etat_relais = lire
    return vu


def _remplacer_orchestrateur_attente(m):
    """Faux orchestrateur qui attend le signal TERM (jusqu'à 10 s) et dit s'il l'a reçu."""
    shutil.rmtree(m["orch"])
    o, commit, empreintes = faux_orchestrateur(m["tmp"])
    v8 = o / "demonstrations" / "ideation_v8.py"
    v8.write_text(v8.read_text().replace("arrete = False\n", (
        "arrete = False\nif True:\n    import signal, time\n    _e = {'stop': False}\n"
        "    signal.signal(signal.SIGTERM, lambda n, f: _e.__setitem__('stop', True))\n"
        "    if '--verifier-seulement' not in a:\n        for _ in range(200):\n            if _e['stop']:\n                break\n"
        "            time.sleep(0.05)\n        arrete = _e['stop']\n        os.makedirs(sortie, exist_ok=True)\n"
        "        json.dump({'signal_term_recu': arrete}, open(os.path.join(sortie, 'signal.json'), 'w'))\n"), 1))
    git(o, "-c", "user.email=t@example.invalid", "-c", "user.name=t", "commit", "-q", "-am", "attente")
    commit = subprocess.run(["git", "-C", str(o), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    empreintes = dict(empreintes, **{"demonstrations/ideation_v8.py": hashlib.sha256(v8.read_bytes()).hexdigest()})
    m["r"].orchestrateurs, m["r"].commit_orchestrateur, m["r"].empreintes_orchestrateur = (o,), commit, empreintes
    m["orch"] = o


# --- 1. part Claude sur LUC (GO-2026-11-22-124) : plafond propre de 45 USD ; arrêt propre au premier refus (code 5) -------------


def _journal_claude(m):
    c = m["cmdlines"][PID_CLAUDE]
    return Path(c[c.index("--journal") + 1])


def test_v11_part_claude_cas_sain_sous_45(monde):
    vu = _etat_claude_apres_depart(monde, depense_usd=39.5, engage_usd=0.4, refus=0)
    _journal_claude(monde).write_text(json.dumps({"statut": 200, "modele": "claude-opus-5-5"}) + "\n", encoding="utf-8")
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    c = json.loads((run / "manifeste-lanceur-fin.json").read_text())["cle_claude_au_fil_de_l_eau"]
    assert c["arret"] is None and c["plafond_part_claude_usd"] == 45.0 and c["journal"] == str(_journal_claude(monde))
    assert c["lectures"] >= 1 and c["derniere_part_engagee_usd"] == pytest.approx(39.9) and vu["lectures"] >= 1
    assert not (run / "alerte-arret-part-claude.json").exists()


def test_v11_premier_refus_du_relais_claude_arret_propre_code_5_sans_relance(monde, capsys):
    _etat_claude_apres_depart(monde, depense_usd=44.7, engage_usd=0.0, refus=1)     # le relais a refusé un appel (402)
    _remplacer_orchestrateur_attente(monde)
    assert lancer(monde["r"]) == 5
    run = un_run(monde["r"])
    assert L.scelle(run / "alerte-arret-part-claude.json")
    alerte = json.loads((run / "alerte-arret-part-claude.json").read_text())
    assert alerte["code"] == 5 and "402" in alerte["motif"] and "sans relance" in alerte["alerte"] and "aucune" in alerte["relance"]
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["code_du_lanceur"] == 5 and fin["cle_claude_au_fil_de_l_eau"]["arret"]["code"] == 5
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    sig = Path(dep["sortie"]) / "signal.json"
    assert fin["code"] == -15 or json.loads(sig.read_text())["signal_term_recu"] is True
    assert "arret_cle_claude" in capsys.readouterr().err
    assert lancer(monde["r"]) == 2                                             # aucune relance sous cette version


@pytest.mark.parametrize("statut", [400, 401, 402])
def test_v11_premier_4xx_de_l_interface_lu_au_journal_arret_code_5(monde, statut):
    _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.4, refus=0)       # loin du plafond : c'est l'interface qui refuse
    _journal_claude(monde).write_text(json.dumps({"statut": 200}) + "\n" + json.dumps({"statut": 429}) + "\n"
                                      + json.dumps({"statut": statut, "chemin": "/v1/messages"}) + "\n", encoding="utf-8")
    _remplacer_orchestrateur_attente(monde)
    assert lancer(monde["r"]) == 5
    run = un_run(monde["r"])
    assert L.scelle(run / "alerte-arret-part-claude.json")
    alerte = json.loads((run / "alerte-arret-part-claude.json").read_text())
    assert alerte["code"] == 5 and f"statut {statut}" in alerte["motif"] and "interface" in alerte["motif"]
    assert alerte["statut"] == statut and alerte["cause"].startswith("inconnue")   # v11c : le relais ne garde pas la cause


def test_v11_200_et_429_n_arretent_pas(monde):
    _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.0, refus=0)
    _journal_claude(monde).write_text("".join(json.dumps({"statut": s}) + "\n" for s in (200, 429, 200, 429, 529, 500)), encoding="utf-8")
    assert lancer(monde["r"]) == 0


def test_v11_est_refus_interface():
    assert [s for s in (200, 299, 399, 400, 401, 402, 403, 404, 418, 429, 499, 500, 529) if L.est_refus_interface(s)] == \
        [400, 401, 402, 403, 404, 418, 499]
    assert not L.est_refus_interface(True) and not L.est_refus_interface("400") and not L.est_refus_interface(None)


def test_v11_mutation_garde_du_journal_retiree(monde):
    """La garde neuve retirée (le journal n'est plus lu) : un 400 de l'interface ne ferait plus arrêter la course."""
    m = _mutant("lanceur_v11_mutant_journal", [("            n_lignes, neuves = self._lignes_du_relais()\n",
                                                "            n_lignes, neuves = self.vu, []\n")])
    _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.0, refus=0)
    _journal_claude(monde).write_text(json.dumps({"statut": 400}) + "\n", encoding="utf-8")
    assert m.principal([], reglages=monde["r"]) == 0                                 # le mutant laisse partir : défaut visible
    monde["r"].dossier_runs = monde["tmp"] / "runs-ter"
    monde["r"].dossier_sorties = monde["tmp"] / "sorties-ter"
    assert lancer(monde["r"]) == 5                                                   # le lanceur, lui, arrête


def test_v11_part_engagee_au_plafond_arret_propre_code_5(monde):
    _etat_claude_apres_depart(monde, depense_usd=44.6, engage_usd=0.4, refus=0)    # 45,0 : dépense + réservé des appels en vol
    _remplacer_orchestrateur_attente(monde)
    assert lancer(monde["r"]) == 5
    alerte = json.loads((un_run(monde["r"]) / "alerte-arret-part-claude.json").read_text())
    assert "≥ plafond de la part Claude 45.0" in alerte["motif"]


def test_v11_relais_claude_a_un_autre_plafond_que_45_refuse(monde, capsys):
    monde["cmdlines"][PID_CLAUDE][monde["cmdlines"][PID_CLAUDE].index("--plafond-usd") + 1] = "150"   # l'ancienne règle
    monde["etat_claude"]["plafond_usd"] = 150.0
    assert lancer(monde["r"]) == 2
    assert "plafond de la part Claude" in capsys.readouterr().err


def test_v11_relais_claude_sans_journal_refuse(monde, capsys):
    c = monde["cmdlines"][PID_CLAUDE]
    k = c.index("--journal")
    del c[k:k + 2]
    assert lancer(monde["r"]) == 2
    assert "--journal" in capsys.readouterr().err


@pytest.mark.parametrize("cas", ["etat", "journal"])
def test_v11_etat_ou_journal_illisible_trois_fois_arret_propre_code_5(monde, cas):
    if cas == "etat":
        _etat_claude_apres_depart(monde)
    else:
        _etat_claude_apres_depart(monde, depense_usd=1.0, engage_usd=0.0, refus=0)
        _journal_claude(monde).write_text("{pas du json\n", encoding="utf-8")
    _remplacer_orchestrateur_attente(monde)
    assert lancer(monde["r"]) == 5
    alerte = json.loads((un_run(monde["r"]) / "alerte-arret-part-claude.json").read_text())
    assert "illisible 3 fois" in alerte["motif"]


def test_v11_une_lecture_manquee_n_arrete_pas():
    class R:
        lire_etat_relais = None
    n = {"k": 0}

    def lire(url):
        n["k"] += 1
        if n["k"] == 1:
            raise OSError("manquée")
        return {"depense_usd": 1.0, "engage_usd": 0.0, "refus": 0}
    r = R()
    r.lire_etat_relais = lire
    s = L.SurveillanceCleClaude(r, "http://127.0.0.1:1", 45.0)
    assert s.depasse() is None and s.illisibles == 1
    assert s.depasse() is None and s.illisibles == 0 and s.derniere == 1.0


@pytest.mark.parametrize("modif", ["retire", "releve", "abaisse", "part_de_la_couverture"])
def test_v11_mutation_plafond_de_la_part_retire_ou_change_refuse(monde, modif):
    p = monde["depot"] / L.PIECES["configuration"][0]
    o = json.loads(p.read_text())
    c = o["changements_v11"]
    if modif == "retire":
        del c["plafond_part_claude_usd"]
    elif modif == "releve":
        c["plafond_part_claude_usd"] = 60.0
    elif modif == "abaisse":
        c["plafond_part_claude_usd"] = 30.0
    else:
        c["part_de_la_couverture"] = 0.8                      # la règle retirée par GO-2026-11-22-124 réintroduite
    p.write_text(json.dumps(o, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    monde["r"].pieces = dict(monde["r"].pieces, configuration=(L.PIECES["configuration"][0], hashlib.sha256(p.read_bytes()).hexdigest()))
    assert lancer(monde["r"]) == 2


def test_v11_mutation_constante_du_plafond_relevee_refusee(monde, monkeypatch, capsys):
    monkeypatch.setattr(L, "PLAFOND_PART_CLAUDE_USD", 60.0)
    assert lancer(monde["r"]) == 2
    assert "45 USD exigés" in capsys.readouterr().err


def test_v11_releve_sans_ligne_de_luc_part(monde, capsys):
    # v11c, constat 3 (renversé) : l'entrée « solde non lu, GO-2026-11-22-124 » de LUC est exigée ; absente : refus
    objet = releve()
    del objet["cles"][L.CLE_CLAUDE]
    _releve(monde, objet)
    assert lancer(monde["r"]) == 2
    assert "s'écrit, il ne s'omet pas" in capsys.readouterr().err


def test_v11_codes_de_sortie():
    assert L.code_de_sortie(False, False, None, 0, 5) == 5 and L.code_de_sortie(False, True, None, 2, 5) == 5
    assert L.code_de_sortie(True, False, None, 0, 5) == 4 and L.code_de_sortie(False, False, None, 0) == 0


# --- 2. clé Claude : Minuit réintroduite ---------------------------------------------------------------------------------------


def test_v11_mutation_minuit_dans_la_declaration_refusee(monde, capsys):
    d = declaration(monde["depot"])
    d["fournisseurs"]["claude"]["nom_cle"] = "RR_ANTHROPIC_API_KEY_MINUIT"
    _decl(monde, d)
    assert lancer(monde["r"]) == 2
    assert "MINUIT" in capsys.readouterr().err


def test_v11_mutation_minuit_dans_la_configuration_refusee():
    fixe = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    L.garde_cles_configuration(fixe)
    for modif in (lambda f: f["cles"].__setitem__("claude", "RR_ANTHROPIC_API_KEY_MINUIT"),
                  lambda f: f["especes"][0].__setitem__("cle", "RR_ANTHROPIC_API_KEY_MINUIT"),
                  lambda f: f["cles_interdites"].remove("RR_ANTHROPIC_API_KEY_MINUIT")):
        f = json.loads(json.dumps(fixe))
        modif(f)
        with pytest.raises(L.Refus):
            L.garde_cles_configuration(f)


def test_v11_mutation_minuit_dans_l_environnement_refusee(monde):
    monde["r"].environnement = {"PATH": "/usr/bin:/bin", "RR_ANTHROPIC_API_KEY_MINUIT": "valeur-secrete-essai-3"}
    assert lancer(monde["r"]) == 2


def test_v11_configuration_ne_differe_de_la_v9_que_par_les_cles_et_les_notes():
    p = subprocess.run(["git", "-C", str(RACINE), "show", "refs/remotes/origin/prep/affinage-v10-compte-organisme-v1:"
                        "docs/notes/organisme-affinage-mentors-v1/course-v9/configuration-course-affinage-mentors-v9.json"],
                       capture_output=True)
    if p.returncode != 0:
        pytest.skip("branche prep/affinage-v10 non récupérée")
    v9, v11 = json.loads(p.stdout), json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
    for k in set(v9) | set(v11):
        if k not in ("version", "statut", "cles", "cles_interdites", "credit_declare_usd", "especes", "changements_v11", "argon_v11",
                     "relais_persistants_v4"):
            assert v9.get(k) == v11.get(k), k
    # v11d : seul écart du bloc des relais persistants : plafond inerte retiré, note ajoutée
    attendu = {k: v for k, v in v9["relais_persistants_v4"].items() if k != "plafond_relais_claude_usd"}
    assert {k: v for k, v in v11["relais_persistants_v4"].items() if k != "note_v11d"} == attendu
    assert [dict(e, cle=None) for e in v9["especes"]] == [dict(e, cle=None) for e in v11["especes"]]
    assert v11["plafonds_session"]["proposeur"] == 3.0 and v11["changements_v11"]["plafond_part_claude_usd"] == 45.0


# --- 3. exception de clé (GO-2026-11-22-107) ------------------------------------------------------------------------------------


@pytest.mark.parametrize("remplace,par", [
    (LIGNE_GO_CLE, ""),                                                                                     # 107 absente
    (LIGNE_GO_CLE, LIGNE_GO_CLE.replace("RR_ANTHROPIC_API_KEY_LUC", "RR_ANTHROPIC_API_KEY_MINUIT")),       # autre clé
    (LIGNE_GO_CLE, LIGNE_GO_CLE.replace("GO-2026-11-22-70", "GO-2026-11-22-71")),                           # autre règle
    (LIGNE_GO_CLE, LIGNE_GO_CLE.replace("| Lazar |", "| la mère |")),                                       # pas Lazar
    (LIGNE_GO_SIMPL, ""),                                                                                   # 124 absente
    (LIGNE_GO_SIMPL, LIGNE_GO_SIMPL.replace("2026-12-15", "2026-11-17")),                                    # 124 échue
    (LIGNE_GO_SIMPL, LIGNE_GO_SIMPL.replace("GO-2026-11-22-107", "GO-2026-11-22-999")),                      # 124 sans 107
    (LIGNE_GO_SIMPL, LIGNE_GO_SIMPL + "| GO-2026-11-22-130 | 2026-11-22 | révocation | révoque GO-2026-11-22-124 | — | — | Lazar | — |\n"),
])
def test_v11_exceptions_de_cle_artefacts_refuses(monde, remplace, par):
    monde["r"].registre_go.write_text(ligne_go().replace(remplace, par), encoding="utf-8")
    assert lancer(monde["r"]) == 2


ENTETE_GO = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | réf. |\n|---|---|---|---|---|---|---|---|\n"
L14 = ("| GO-2026-11-18-14 | 2026-11-18 | calcul | course d'affinage des idées des mentors | 150 USD | 2026-11-25 | Lazar | R-3215 |\n")
L80 = ("| GO-2026-11-22-80 | 2026-11-22 | calcul | Prolongation de GO-2026-11-18-14 (affinage des 93 idées des mentors) | 150 USD "
       "(plafond de GO-2026-11-18-14) | 2026-12-15 | Lazar | GO-2026-11-22-77 |\n")
L107 = LIGNE_GO_CLE.replace("| 2026-11-18 | calcul", "| 2026-11-22 | calcul")
L124 = LIGNE_GO_SIMPL.replace("| 2026-11-18 | calcul", "| 2026-11-22 | calcul")
L131 = ("| GO-2026-11-22-131 | 2026-11-22 | décision | Lazar confirme la prolongation de GO-2026-11-22-107 au 15 décembre | — | "
        "2026-12-15 | Lazar | GO-2026-11-22-124 |\n")


def _registre_go_essai(tmp_path, *lignes):
    p = tmp_path / "go.md"
    p.write_text(ENTETE_GO + "".join(lignes), encoding="utf-8")
    return p


def _fixe_confirmation(valeur):
    f = json.loads(json.dumps(FIXE))
    f["changements_v11"]["confirmation_prolongation_go_107"] = valeur
    return f


def test_v11_go_avant_le_25_sans_prolongation_sain(tmp_path):
    # v11b : GO-80 est le GO de la course, exigé même avant le 25
    o = L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124), dt.date(2026, 11, 24), _fixe_confirmation(None))
    assert o["go"]["id"] == "GO-2026-11-22-80" and o["prolongation_course"]["valide"] is True and o["confirmation_107"]["valide"] is False
    assert o["prolongation_course"]["go_initial"]["id"] == "GO-2026-11-18-14"


def test_v11_go_apres_le_25_avec_80_et_confirmation_nommee_et_inscrite_sain(tmp_path):
    o = L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))
    assert o["prolongation_course"]["valide"] is True and o["confirmation_107"]["nommee"] == "GO-2026-11-22-131"
    assert o["exception_cle"]["id"] == "GO-2026-11-22-107"


def test_v11_go_apres_le_25_sans_80_refuse(tmp_path):
    with pytest.raises(L.Refus, match="GO-2026-11-22-80 .*non valide : ligne absente"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))


def test_v11_go_apres_le_25_80_revoquee_refuse(tmp_path):
    rev = "| GO-2026-11-22-140 | 2026-11-22 | révocation | révoque GO-2026-11-22-80 | — | — | Lazar | — |\n"
    with pytest.raises(L.Refus, match="GO-2026-11-22-80 .*révoquée par GO-2026-11-22-140"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, rev, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))


def test_v11_go_apres_le_25_confirmation_non_nommee_refuse(tmp_path):
    with pytest.raises(L.Refus, match="GO-2026-11-22-107 hors de sa période"):           # inscrite mais pas nommée
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 11, 27), _fixe_confirmation(None))


def test_v11_go_confirmation_nommee_mais_non_inscrite_refuse(tmp_path):
    with pytest.raises(L.Refus, match="confirmation de la prolongation"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124), dt.date(2026, 11, 24), _fixe_confirmation("GO-2026-11-22-131"))


def test_v11_go_confirmation_par_une_autre_que_lazar_refuse(tmp_path):
    with pytest.raises(L.Refus, match="confirmation de la prolongation"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131.replace("| Lazar | GO-2026-11-22-124", "| la mère | GO-2026-11-22-124")),
                          dt.date(2026, 11, 27), _fixe_confirmation("GO-2026-11-22-131"))


def test_v11_go_emplacement_de_confirmation_absent_refuse(tmp_path):
    f = json.loads(json.dumps(FIXE))
    del f["changements_v11"]["confirmation_prolongation_go_107"]
    with pytest.raises(L.Refus, match="emplacement"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124), dt.date(2026, 11, 24), f)


def test_v11_go_apres_le_15_decembre_refuse(tmp_path):
    with pytest.raises(L.Refus):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 12, 16), _fixe_confirmation("GO-2026-11-22-131"))


def test_v11_go_lus_au_manifeste(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["go"]["id"] == "GO-2026-11-22-80" and dep["go"]["prolongation"]["id"] == "GO-2026-11-22-80"
    assert dep["go"]["prolongation"]["go_initial"]["id"] == "GO-2026-11-18-14"
    assert dep["go_exception_cle"]["confirmation"]["nommee"] is None and dep["go_simplification_cle"]["echeance"] == "2026-12-15"


def test_v11_exception_de_cle_sur_la_vraie_ligne_de_main(tmp_path):
    p = subprocess.run(["git", "-C", str(RACINE), "show", "refs/remotes/origin/main:registres/go.md"], capture_output=True)
    if p.returncode != 0 or b"GO-2026-11-22-107" not in p.stdout:
        pytest.skip("registre de main sans la ligne GO-2026-11-22-107")
    reg = tmp_path / "go.md"
    reg.write_bytes(p.stdout)
    o = L.verifier_go_exception_cle(reg, dt.date(2026, 11, 22))
    assert o["id"] == "GO-2026-11-22-107" and o["par"] == "Lazar"
    with pytest.raises(L.Refus, match="période"):
        L.verifier_go_exception_cle(reg, dt.date(2026, 11, 26))
    if b"GO-2026-11-22-124" in p.stdout:
        s = L.verifier_go_simplification(reg, dt.date(2026, 11, 26))
        assert s["echeance"] == "2026-12-15"
        assert L.verifier_go_exception_cle(reg, dt.date(2026, 11, 26), prolongation=s["echeance"])["id"] == "GO-2026-11-22-107"
        with pytest.raises(L.Refus):                                             # sans confirmation nommée : refus après le 25
            L.verifier_les_go(reg, dt.date(2026, 11, 26), _fixe_confirmation(None))


# --- 4. Astra : gpt-6.2-astra, OPENAI_API_KEY_2, sonde v3, palier ---------------------------------------------------------------


def test_v11_astra_arguments_et_modele():
    a = L.ARGUMENTS_COMMANDES["astra"]
    assert a[a.index("--modele") + 1] == "gpt-6.2-astra" and L.MODELES_RELAIS["astra"] == ["gpt-6.2-astra"]
    assert (a[a.index("--prix-entree") + 1], a[a.index("--prix-sortie") + 1]) == ("8", "40") and L.PRIX_ASTRA == (8.0, 40.0)
    assert L.CLE_ASTRA == "OPENAI_API_KEY_2"


def test_v11_astra_cas_sain_au_manifeste(monde, monkeypatch):
    _astra(monde, monkeypatch)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["palier_astra"]["borne_entree_jetons"] < 272000 and dep["cles_employees"]["astra"] == "OPENAI_API_KEY_2"


@pytest.mark.parametrize("modifs,motif", [({"modele_propose": "gpt-6-astra"}, "gpt-6.2-astra"),
                                          ({"nom_cle": "OPENAI_API_KEY"}, "OPENAI_API_KEY_2")])
def test_v11_astra_mutations_refusees(monde, monkeypatch, capsys, modifs, motif):
    _astra(monde, monkeypatch)
    d = json.loads(monde["r"].declaration.read_text())
    d["fournisseurs"]["astra"].update(modifs)
    _decl(monde, d)
    assert lancer(monde["r"]) == 2
    assert motif in capsys.readouterr().err


@pytest.mark.parametrize("modifs,motif", [({"version": "sonde_astra_affinage_v2"}, "sonde épinglée"),
                                          ({"modele_servi": "gpt-6-astra"}, "modèle servi")])
def test_v11_sonde_d_astra_ancienne_refusee(monde, monkeypatch, capsys, modifs, motif):
    _astra(monde, monkeypatch)
    _sonde(monde, **modifs)
    assert lancer(monde["r"]) == 2
    assert motif in capsys.readouterr().err


def test_v11_sonde_commune_v1_refusee(monde, monkeypatch, capsys):
    _astra(monde, monkeypatch)
    c = json.loads((monde["depot"] / COMMUNE_DU_JOUR).read_text())
    c["version"] = "sonde_astra_courses_v1"
    ecrire_sondes(monde["depot"], v2=json.loads((monde["depot"] / L.SONDE_ASTRA).read_text()), commune=c)
    assert lancer(monde["r"]) == 2
    assert "version" in capsys.readouterr().err


def test_v11_palier_d_astra_sain_et_artefact():
    pieces = {"consigne_proposeur": {"absolu": str(RACINE / L.PIECES["consigne_proposeur"][0])}}
    liste = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
    assert L.verifier_palier_astra(pieces, liste)["borne_entree_jetons"] < 20000
    grosse = json.loads(json.dumps(liste))
    grosse["fils"][0]["idees_servies"][0]["texte_servi"] = "x" * 300000
    with pytest.raises(L.Refus, match="palier"):
        L.verifier_palier_astra(pieces, grosse)


# --- 5. Carbon en flux : budget sous le plafond de session (point 3 de la mère) -------------------------------------------------


def _decl_carbon_reelle(args=None):
    c = RACINE / L.PIECES["commande_carbon"][0]
    return {"fournisseurs": {"carbon": {"commande": [sys.executable, "-I", "-B", str(c)] + list(args or L.ARGUMENTS_COMMANDES["carbon"])}}}


def _pieces_rel():
    return {k: {"chemin": v[0], "absolu": str(RACINE / v[0]), "sha256": v[1]} for k, v in L.PIECES.items()}


def test_v11_carbon_pire_cas_sous_le_plafond_de_session():
    o = L.controler_pire_cas_carbon(_decl_carbon_reelle(), FIXE, LISTE_V11, _pieces_rel())
    cas = o["cas"]["entree_la_plus_longue"]
    assert cas["entree_gardee_jetons"] == 2618 and cas["sortie_demandee_jetons"] == 65536
    assert cas["pire_cas_appel_usd"] == pytest.approx((2618 * 4 + 65536 * 20) / 1e6) == pytest.approx(1.321192, abs=1e-6)  # R-5018
    assert cas["pire_cas_appel_usd"] <= o["plafond_session_usd"] == 3.0
    assert o["texte_jetons"] == 36864 >= 16000 and o["texte_jetons"] > o["limite_invite_caracteres"] == 18000


@pytest.mark.parametrize("option,valeur,motif", [("--max-sortie-jetons", "40000", "texte"),       # 40 000 − 28 672 < 16 000
                                                 ("--max-sortie-jetons", "46000", "limite de l'invite"),  # 17 328 ≤ 18 000
                                                 ("--max-sortie-jetons", "200000", "plafond de session"),  # 200 000 × 20 > 3,00
                                                 ("--provision-pensee-jetons", "20000", "provision")])
def test_v11_carbon_budget_artefacts(option, valeur, motif):
    args = list(L.ARGUMENTS_COMMANDES["carbon"])
    args[args.index(option) + 1] = valeur
    with pytest.raises(L.Refus, match=motif):
        L.controler_pire_cas_carbon(_decl_carbon_reelle(args), FIXE, LISTE_V11, _pieces_rel())


def test_v11_carbon_sous_un_plafond_de_1_00_refuse():
    fixe = json.loads(json.dumps(FIXE))
    fixe["plafonds_session"]["proposeur"] = 1.0                       # 1,32 > 1,00 : Carbon en flux ne tiendrait pas
    with pytest.raises(L.Refus, match="plafond de session"):
        L.controler_pire_cas_carbon(_decl_carbon_reelle(), fixe, LISTE_V11, _pieces_rel())


@pytest.mark.parametrize("niveau", ["medium", "low"])
def test_v11_carbon_mutation_reflexion_abaissee_refusee_a_la_declaration(monde, monkeypatch, capsys, niveau):
    sc = script_commande(monde["tmp"], "commande_gemini_flux_v2", {"texte": "", "cout_usd": 0.01})
    args = list(L.ARGUMENTS_COMMANDES["carbon"])
    args[args.index("--niveau-reflexion") + 1] = niveau
    _carbon(monde, monkeypatch, commande=[sys.executable, "-I", "-B", str(sc)] + args)
    assert lancer(monde["r"]) == 2
    assert "niveau-reflexion" in capsys.readouterr().err


def test_v11_carbon_commande_par_lot_refusee_a_la_declaration(monde, monkeypatch):
    sc = script_commande(monde["tmp"], "commande_gemini_lot_v1", {"texte": "", "cout_usd": 0.01})
    _carbon(monde, monkeypatch)
    d = json.loads(monde["r"].declaration.read_text())
    d["fournisseurs"]["carbon"]["commande"][3] = str(sc)                  # l'ancienne commande : plus épinglée
    _decl(monde, d)
    assert lancer(monde["r"]) == 2


# --- 6. garde des appels à Google (règle gelée, GO-2026-11-21-71) ---------------------------------------------------------------


LISTE_V11 = json.loads((RACINE / L.PIECES["liste_fils"][0]).read_text())
COMMANDE_GOOGLE_FACTICE = r'''
import json, sys, urllib.request
a = sys.argv[1:]
url = a[a.index("--url-base") + 1]
config = json.loads(a[a.index("--config") + 1])
corps = {"contents": [{"role": "user", "parts": [{"text": sys.stdin.read()}]}], "generationConfig": config}
ouv = urllib.request.build_opener(urllib.request.ProxyHandler({}))
req = urllib.request.Request(url + "/models/gemini-4-carbon:generateContent", data=json.dumps(corps).encode(), method="POST",
                             headers={"Content-Type": "application/json"})
try:
    ouv.open(req, timeout=10)
except Exception:
    pass
print(json.dumps({"texte": "", "cout_usd": 1e-6, "erreur": "capturé"}))
sys.exit(3)
'''


def _pieces_garde(tmp_path):
    o = _octets_de_main("src/controle_ia/garde_google_v3.py")
    if o is None:
        pytest.skip("garde Google absente de origin/main")
    g = tmp_path / "garde_google_v3.py"
    g.write_bytes(o)
    pieces = _pieces_rel()
    pieces["garde_google"]["absolu"] = str(g)
    return pieces


def _carbon_factice(tmp_path, config, provision="28672"):
    s = tmp_path / "commande_google_factice.py"
    s.write_text(COMMANDE_GOOGLE_FACTICE, encoding="utf-8")
    return {"commande": [sys.executable, "-I", "-B", str(s), "--config", json.dumps(config), "--provision-pensee-jetons", provision,
                         "--url-base", "http://127.0.0.1:8791/v1beta"]}


def test_v11_garde_google_vraie_commande_en_flux_conforme(tmp_path):
    pieces = _pieces_garde(tmp_path)
    o = L.controler_chemins_google(L.Reglages.production(), _decl_carbon_reelle(), pieces, FIXE, LISTE_V11)
    assert o["carbon"]["conforme"] is True, o
    rg = o["carbon"]["roles"][0]["reglages_captures"]
    assert rg["mode"] == "flux" and rg["maxOutputTokens"] == 65536 and rg["provision"] == 28672
    assert rg["thinkingConfig"] == {"thinkingLevel": "high", "includeThoughts": True}


@pytest.mark.parametrize("config,motif", [
    ({"maxOutputTokens": 65536}, "thinkingLevel absent"),                                               # sans réflexion
    ({"maxOutputTokens": 65536, "thinkingConfig": {"thinkingBudget": 28672, "includeThoughts": True}}, "thinkingBudget présent"),
    ({"maxOutputTokens": 65536, "thinkingConfig": {"thinkingLevel": "low", "includeThoughts": True}}, "niveau envoyé"),
    ({"maxOutputTokens": 65536, "thinkingConfig": {"thinkingLevel": "high"}}, "includeThoughts"),
    ({"maxOutputTokens": 40000, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "jetons de texte"),
    ({"maxOutputTokens": 70000, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "au-delà de la limite"),
    ({"maxOutputTokens": 46000, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "limite de l'invite"),
])
def test_v11_garde_google_mutations_refusees(tmp_path, config, motif):
    pieces = _pieces_garde(tmp_path)
    o = L.controler_chemins_google(L.Reglages.production(), {"fournisseurs": {"carbon": _carbon_factice(tmp_path, config)}},
                                   pieces, FIXE, LISTE_V11)
    probs = o["carbon"]["roles"][0]["problemes"]
    assert o["carbon"]["conforme"] is False and any(motif in p for p in probs), probs


def test_v11_garde_google_rien_capture_refuse(tmp_path):
    pieces = _pieces_garde(tmp_path)
    s = tmp_path / "muette.py"
    s.write_text("import sys\nprint('{\"texte\": \"\", \"cout_usd\": 1e-06}')\nsys.exit(4)\n", encoding="utf-8")
    o = L.controler_chemins_google(L.Reglages.production(), {"fournisseurs": {"carbon": {"commande": [sys.executable, "-I", "-B", str(s)]}}},
                                   pieces, FIXE, LISTE_V11)
    assert o["carbon"]["conforme"] is False and "aucun corps" in o["carbon"]["roles"][0]["problemes"][0]


def test_v11_garde_google_argon_reel_et_ancien_lot_refuses(tmp_path):
    """L'Argon réel (enveloppe v5, `commande_argon_v3d.py`) et l'ancienne commande par lot de Carbon (`main`, 9484dce0…) posent
    `thinkingBudget` sans `thinkingLevel` ni `includeThoughts` : refusés ; rien n'est envoyé chez Google."""
    pieces = _pieces_garde(tmp_path)
    lot = _octets_de_main("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py")
    if lot is None:
        pytest.skip("commande par lot absente de origin/main")
    c = tmp_path / "commande_gemini_lot_v1.py"
    c.write_bytes(lot)
    args_lot = ["--modele", "gemini-4-carbon", "--url-base", "http://127.0.0.1:8792/v1beta", "--prix-entree", "8.3", "--prix-sortie",
                "41.5", "--facteur-lot", "0.5", "--max-sortie-jetons", "32768", "--sortie-min-jetons", "4096",
                "--provision-pensee-jetons", "28672", "--roles", "proposeur_ideation"]
    decl = {"fournisseurs": {"argon": {}, "carbon": {"commande": [sys.executable, "-I", "-B", str(c)] + args_lot}}}
    o = L.controler_chemins_google(L.Reglages.production(), decl, pieces, FIXE, LISTE_V11)
    for nom in ("argon", "carbon"):
        assert o[nom]["conforme"] is False
        for role in o[nom]["roles"]:
            assert any("thinkingBudget présent" in p for p in role["problemes"]) and any("includeThoughts" in p for p in role["problemes"])


def test_v11_garde_google_reelle_depart_sain_argon_en_flux(monde):
    """La garde réelle (pièce de main) sur l'Argon déclaré en flux : conforme, départ en moteur réel (relais simulés)."""
    if _octets_de_main("src/controle_ia/garde_google_v3.py") is None:
        pytest.skip("garde Google absente de origin/main")
    monde["r"].controler_google = None
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["garde_google"]["argon"]["conforme"] is True and len(dep["garde_google"]["argon"]["roles"]) == 2


def test_v11_garde_google_reelle_refuse_un_chemin_non_conforme(monde, monkeypatch, capsys):
    if _octets_de_main("src/controle_ia/garde_google_v3.py") is None:
        pytest.skip("garde Google absente de origin/main")
    monde["r"].controler_google = None
    s = monde["tmp"] / "commande_gemini_flux_v2.py"                       # même nom, autre code : sans réglage de réflexion
    s.write_text(COMMANDE_GOOGLE_FACTICE.replace("gemini-4-carbon", "gemini-4-argon").replace(
        'config = json.loads(a[a.index("--config") + 1])', 'config = {"maxOutputTokens": 45056}'), encoding="utf-8")
    monkeypatch.setitem(L.COMMANDES_EPINGLEES, "argon", {s.name: hashlib.sha256(s.read_bytes()).hexdigest()})
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["commande"][3] = str(s)
    _decl(monde, d)
    assert lancer(monde["r"]) == 2
    err = capsys.readouterr().err
    assert "garde des appels à Google" in err and "thinkingLevel absent" in err
    runs = monde["r"].dossier_runs
    assert not (runs.is_dir() and [p for p in runs.iterdir() if p.name.endswith(L.SUFFIXE_RUN)])


def test_v11_garde_google_en_moteur_simule_ecrite_sans_refus(monde, capsys):
    monde["r"].controler_google = lambda r, decl, pieces, fixe, liste: {
        "argon": {"conforme": False, "roles": [{"problemes": ["réflexion : essai"]}]}}
    monde["r"].moteur, monde["r"].exiger_bac_a_sable, monde["r"].verifier_go = "simule", False, False
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["garde_google"]["refus_en_moteur_reel"] == ["argon"]
    assert "avertissement_garde_google" in capsys.readouterr().err


def test_v11_arguments_de_l_enveloppe_d_argon():
    a = L.arguments_enveloppe_argon(RACINE / L.PIECES["enveloppe_argon"][0])
    assert "$@" not in a and a[a.index("--url-base") + 1] == "http://127.0.0.1:8788/v1beta"


# --- 7. version, préenregistrement, gabarit -------------------------------------------------------------------------------------


def test_v11_version_et_chemins():
    assert L.VERSION == "lancer_course_affinage_mentors_v11d" and "course-v11" in L.PREREG and "course-v11" in L.DECLARATION_RELAIS
    assert L.PROGRAMMES_RELAIS["carbon"][0] == "relais_gemini_v3.py" and L.PIECES["commande_carbon"][0].endswith("commande_gemini_flux_v2.py")


def test_v11_preenregistrement_non_pose_refuse(monde, capsys):
    monde["r"].prereg = (monde["r"].prereg[0], L.PREREG_SHA256)
    assert L.PREREG_SHA256 == ""
    assert lancer(monde["r"]) == 2
    assert "non posée" in capsys.readouterr().err


def test_v11_gabarit_de_declaration_accepte_une_fois_rempli(monde, monkeypatch):
    o = json.loads((RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v11/declaration-relais-gabarit-course-affinage-v11c.json").read_text())
    del o["gabarit"]
    s = _astra(monde, monkeypatch)
    sc = script_commande(monde["tmp"], "commande_gemini_flux_v2", {"texte": "", "cout_usd": 0.01})
    epingler(monkeypatch, "carbon", sc)
    ref = declaration(monde["depot"])["fournisseurs"]
    f = o["fournisseurs"]
    f["claude"].update(porte_plafond=ref["claude"]["porte_plafond"], url_relais=ref["claude"]["url_relais"], pid_relais=PID_CLAUDE)
    f["argon"].update(commande=ref["argon"]["commande"], nom_cle="CLE_ESSAI_A", pid_relais=PID_ARGON)
    f["astra"]["commande"][0], f["astra"]["commande"][3] = sys.executable, str(s)
    f["astra"]["pid_relais"] = PID_ASTRA
    f["carbon"]["commande"][0], f["carbon"]["commande"][3] = sys.executable, str(sc)
    f["carbon"].update(nom_cle="CLE_ESSAI_G", pid_relais=PID_CARBON)
    assert f["claude"]["nom_cle"] == L.CLE_CLAUDE and f["astra"]["nom_cle"] == L.CLE_ASTRA
    assert f["carbon"]["commande"][4:] == L.ARGUMENTS_COMMANDES["carbon"] and f["astra"]["commande"][4:] == L.ARGUMENTS_COMMANDES["astra"]
    _decl(monde, o)
    objet = releve(CLE_ESSAI_A={"non_lisible": True}, CLE_ESSAI_G={"non_lisible": True},
                   OPENAI_API_KEY_2={"credit_usd": 100.0, "reste_usd": 90.0, "source": "essai"})
    objet["dispense"] = {"par": "mère", "reference": "R-3237", "cles": ["CLE_ESSAI_A", "CLE_ESSAI_G"]}
    _releve(monde, objet)
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    assert dep["especes_actives"] == ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]


# --- 8. Argon sous la garde Google (décision de la mère) : emplacement du plafond des juges, commande en flux ------------------


def _decl_argon_reelle():
    c = RACINE / L.PIECES["commande_carbon"][0]
    return {"fournisseurs": {"argon": {"commande": [sys.executable, "-I", "-B", str(c)] + L.ARGUMENTS_COMMANDES["argon"]}}}


def _fixe_juge(valeur):
    f = json.loads(json.dumps(FIXE))
    f["argon_v11"]["plafond_session_juge_usd"] = valeur
    return f


def test_v11_argon_emplacement_de_production_1_00():
    assert FIXE["argon_v11"]["plafond_session_juge_usd"] == 1.00 and FIXE["plafonds_session"]["juge"] == 0.6
    f = json.loads(json.dumps(FIXE))
    assert L.appliquer_emplacement_argon(f)["plafond_session_juge_usd"] == 1.00 and f["plafonds_session"]["juge"] == 1.00
    o = L.controler_pire_cas_argon(_decl_argon_reelle(), f, LISTE_V11, _pieces_rel())
    assert o["roles"]["juge"]["pire_cas_appel_usd"] <= 1.00
    with pytest.raises(L.Refus, match="1.00 USD exactement"):                   # v11c : vide refusé (constat 10)
        L.appliquer_emplacement_argon(_fixe_juge(None))


@pytest.mark.parametrize("valeur,issue", [(1.0, "sain"), (0.92, "refus"), (1.1, "refus"), (0.6, "refus"), (2.0, "refus")])
def test_v11_argon_plafond_des_juges_au_plus_juste(valeur, issue):
    # v11c (constat 10) : 1,00 exactement ; toute autre valeur refusée à la lecture de la configuration
    f = _fixe_juge(valeur)
    if issue == "sain":
        assert L.appliquer_emplacement_argon(f)["plafond_session_juge_usd"] == 1.0 and f["plafonds_session"]["juge"] == 1.0
        o = L.controler_pire_cas_argon(_decl_argon_reelle(), f, LISTE_V11, _pieces_rel())
        n = len(L.entree_juge_la_plus_longue(Path(_pieces_rel()["consigne_juge"]["absolu"]).read_text(encoding="utf-8")))
        e = L.math.ceil(n / L.CARACTERES_PAR_JETON_CARBON * (1 + L.MARGE_ENTREE_CARBON))
        assert o["roles"]["juge"]["pire_cas_appel_usd"] == pytest.approx((e * 4 + 45056 * 20) / 1e6, abs=1e-6)
        assert o["roles"]["juge"]["pire_cas_appel_usd"] <= 1.0
        assert o["roles"]["proposeur"]["pire_cas_appel_usd"] <= 3.0
    else:
        with pytest.raises(L.Refus, match="1.00 USD exactement"):
            L.appliquer_emplacement_argon(f)


@pytest.mark.parametrize("valeur", ["2", 0, -1.0, 3.5, True])
def test_v11_argon_emplacement_mal_forme_refuse(valeur):
    with pytest.raises(L.Refus):
        L.appliquer_emplacement_argon(_fixe_juge(valeur))
    f = json.loads(json.dumps(FIXE))
    del f["argon_v11"]
    with pytest.raises(L.Refus, match="emplacement"):
        L.appliquer_emplacement_argon(f)


def test_v11_argon_juge_servi_au_plafond_de_l_emplacement(monde):
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    conf = json.loads((run / "configuration-orchestrateur.json").read_text())
    assert conf["plafonds_session"]["juge"] == 1.0 and "argon_v11" not in conf          # v11c : production
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    assert dep["argon_v11"]["emplacement"] == 1.0 and dep["reglages_argon_v11_flux"]["roles"]["juge"]["plafond_minimal_usd"] == 0.92


def test_v11_argon_enveloppe_v5_refusee_a_la_declaration(monde, capsys):
    d = declaration(monde["depot"])
    d["fournisseurs"]["argon"]["commande"] = ["bash", str(monde["depot"] / L.PIECES["enveloppe_argon"][0])]
    _decl(monde, d)
    assert lancer(monde["r"]) == 2
    assert "enveloppe v5" in capsys.readouterr().err


def test_v11_garde_google_argon_en_flux_sain(tmp_path):
    pieces = _pieces_garde(tmp_path)
    f = _fixe_juge(1.0)
    L.appliquer_emplacement_argon(f)                                         # plafond des juges servi : 1,00 (devis v11)
    o = L.controler_chemins_google(L.Reglages.production(), _decl_argon_reelle(), pieces, f, LISTE_V11)
    assert o["argon"]["conforme"] is True, o
    for role in o["argon"]["roles"]:
        assert role["reglages_captures"]["mode"] == "flux" and role["reglages_captures"]["maxOutputTokens"] == 45056
        assert role["reglages_captures"]["thinkingConfig"] == {"thinkingLevel": "high", "includeThoughts": True}


@pytest.mark.parametrize("config,motif", [
    ({"maxOutputTokens": 45056}, "thinkingLevel absent"),                                                  # réflexion absente
    ({"maxOutputTokens": 30000, "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}, "jetons de texte"),  # trop bas
])
def test_v11_garde_google_argon_artefacts(tmp_path, config, motif):
    pieces = _pieces_garde(tmp_path)
    s = tmp_path / "commande_google_factice.py"
    s.write_text(COMMANDE_GOOGLE_FACTICE.replace("gemini-4-carbon", "gemini-4-argon"), encoding="utf-8")
    decl = {"fournisseurs": {"argon": {"commande": [sys.executable, "-I", "-B", str(s), "--config", json.dumps(config),
                                                    "--provision-pensee-jetons", "24576", "--niveau-reflexion", "high",
                                                    "--url-base", "http://127.0.0.1:8788/v1beta"]}}}
    f = _fixe_juge(1.0)
    L.appliquer_emplacement_argon(f)
    o = L.controler_chemins_google(L.Reglages.production(), decl, pieces, f, LISTE_V11)
    assert o["argon"]["conforme"] is False
    for role in o["argon"]["roles"]:
        assert any(motif in p for p in role["problemes"]), role["problemes"]


# --- brouillon 2 du préenregistrement v11, point (a) : identifiants de GO à trois chiffres de rang ---------------------------------
REV_3 = "| GO-2026-11-22-150 | 2026-11-22 | révocation | révoque GO-2026-11-18-14 | — | — | Lazar | — |\n"
L_3 = ("| GO-2026-11-22-151 | 2026-11-22 | calcul | course d'affinage des idées des mentors | 150 USD | 2026-12-15 | Lazar | "
       "GO-2026-11-18-14 |\n")


def test_v11_go_trois_chiffres_ligne_lue_sain(tmp_path):
    o = L.verifier_go(_registre_go_essai(tmp_path, L14, L_3), dt.date(2026, 11, 27), go_id="GO-2026-11-22-151")
    assert o["id"] == "GO-2026-11-22-151"
    assert L.verifier_go(_registre_go_essai(tmp_path, L80, L_3), dt.date(2026, 11, 24))["id"] == "GO-2026-11-22-80"  # deux chiffres


def test_v11_go_revocation_a_trois_chiffres_vue_refuse(tmp_path):
    with pytest.raises(L.Refus, match="révoqué par GO-2026-11-22-150"):
        L.verifier_go(_registre_go_essai(tmp_path, L14, REV_3), dt.date(2026, 11, 24), go_id="GO-2026-11-18-14")


def test_v11_go_registre_derive_garde_la_revocation_a_trois_chiffres(tmp_path):
    d = L.ecrire_registre_derive(_registre_go_essai(tmp_path, L14, REV_3, L_3), tmp_path / "derive.md")
    texte = (tmp_path / "derive.md").read_text(encoding="utf-8")
    assert d["nombre_de_lignes"] == 2 and "GO-2026-11-22-150" in texte and "GO-2026-11-22-151" not in texte  # GO-14 et sa révocation


def test_v11_go_mutation_lecture_a_deux_chiffres_absente_du_lanceur():
    # artefact : la lecture de v10 (deux chiffres de rang seulement) ne doit plus figurer dans le lanceur
    src = Path(L.__file__).read_text(encoding="utf-8")
    assert r"(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|" not in src and src.count(r"(GO-\d{4}-\d{2}-\d{2}-\d{2,3})\s*\|") >= 2


# === v11b : GO de la course = GO-2026-11-22-80 (prolongation de GO-2026-11-18-14) ============================================
REV_80 = "| GO-2026-11-22-141 | 2026-11-22 | révocation | révoque GO-2026-11-22-80 | — | — | Lazar | — |\n"
REV_14 = "| GO-2026-11-22-142 | 2026-11-22 | révocation | révoque GO-2026-11-18-14 | — | — | Lazar | — |\n"
CONF_131 = "GO-2026-11-22-131"


def _sans_ligne(texte, go_id):
    lignes = [l for l in texte.splitlines(keepends=True) if not l.startswith(f"| {go_id} |")]
    assert len(lignes) == len(texte.splitlines(keepends=True)) - 1
    return "".join(lignes)


def test_v11b_go_de_la_course_et_commande_de_lancement():
    assert L.GO_ID == "GO-2026-11-22-80" == L.GO_PROLONGATION_COURSE and L.GO_COURSE_INITIAL == "GO-2026-11-18-14"
    assert "GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11b.py" in L.__doc__
    assert FIXE["changements_v11"]["go_course"] == "GO-2026-11-22-80"
    garde, _, _ = L.environnement_filtre({"GO_ID": "GO-2026-11-18-14"}, Path("/nulle-part"))
    assert garde["GO_ID"] == "GO-2026-11-22-80"                       # passé tel quel à l'orchestrateur


def test_v11b_depart_sain_avec_go_80(monde):
    assert lancer(monde["r"]) == 0


def test_v11b_depart_refuse_si_go_80_absent(monde):
    monde["r"].registre_go.write_text(_sans_ligne(ligne_go(), "GO-2026-11-22-80"), encoding="utf-8")
    assert lancer(monde["r"]) == 2
    assert not monde["r"].dossier_runs.exists()


def test_v11b_depart_refuse_si_go_80_revoque(monde):
    monde["r"].registre_go.write_text(ligne_go() + REV_80, encoding="utf-8")
    assert lancer(monde["r"]) == 2
    assert not monde["r"].dossier_runs.exists()


def test_v11b_depart_refuse_si_go_14_absent_ou_revoque(monde):
    monde["r"].registre_go.write_text(_sans_ligne(ligne_go(), "GO-2026-11-18-14"), encoding="utf-8")
    assert lancer(monde["r"]) == 2
    monde["r"].registre_go.write_text(ligne_go() + REV_14, encoding="utf-8")
    assert lancer(monde["r"]) == 2
    assert not monde["r"].dossier_runs.exists()


def test_v11b_go_80_qui_ne_prolonge_pas_go_14_refuse(tmp_path):
    l80 = L80.replace("Prolongation de GO-2026-11-18-14 (affinage", "Course (affinage")
    with pytest.raises(L.Refus, match="ne dit pas prolonger GO-2026-11-18-14"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, l80, L107, L124), dt.date(2026, 11, 24), _fixe_confirmation(None))


def test_v11b_go_80_accorde_par_un_autre_refuse(tmp_path):
    l80 = L80.replace("| 2026-12-15 | Lazar |", "| 2026-12-15 | la mère |")
    with pytest.raises(L.Refus, match="accordée par"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, l80, L107, L124), dt.date(2026, 11, 24), _fixe_confirmation(None))


def test_v11b_depart_accepte_au_26_avec_go_80_et_confirmation_nommee(tmp_path):
    o = L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 11, 26), _fixe_confirmation(CONF_131))
    assert o["go"]["id"] == "GO-2026-11-22-80" and o["go"]["plafond_lu"] == 150.0
    assert o["confirmation_107"]["nommee"] == CONF_131 and o["exception_cle"]["id"] == "GO-2026-11-22-107"


def test_v11b_depart_refuse_au_26_sans_confirmation(tmp_path):
    with pytest.raises(L.Refus, match="GO-2026-11-22-107 hors de sa période"):
        L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 11, 26), _fixe_confirmation(None))


def test_v11b_go_de_la_configuration_autre_refuse(tmp_path):
    for valeur in ("GO-2026-11-18-14", None):
        f = _fixe_confirmation(CONF_131)
        f["changements_v11"]["go_course"] = valeur
        with pytest.raises(L.Refus, match="go_course"):
            L.verifier_les_go(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), dt.date(2026, 11, 26), f)


@pytest.mark.parametrize("plafond, issue", [
    ("150 USD (plafond de GO-2026-11-18-14)", "sain"), ("150 USD", "sain"),
    ("150 USD (ou 200)", "refus"), ("140 USD (plafond de GO-2026-11-18-14)", "refus"), ("150 USD (plafond) 20", "refus"),
])
def test_v11b_plafond_de_go_80(tmp_path, plafond, issue):
    l80 = L80.replace("| 150 USD (plafond de GO-2026-11-18-14) |", f"| {plafond} |")
    reg = _registre_go_essai(tmp_path, L14, l80)
    if issue == "sain":
        assert L.verifier_go(reg, dt.date(2026, 11, 26))["plafond_lu"] == 150.0
    else:
        with pytest.raises(L.Refus):
            L.verifier_go(reg, dt.date(2026, 11, 26))


def test_v11b_registre_derive_garde_go_80_et_go_14_et_leurs_revocations(tmp_path):
    autre = "| GO-2026-11-20-03 | 2026-11-20 | calcul | autre course | 10 USD | 2026-11-30 | Lazar | — |\n"
    d = L.ecrire_registre_derive(_registre_go_essai(tmp_path, L14, L80, autre, L107, REV_80, REV_14), tmp_path / "derive.md")
    texte = (tmp_path / "derive.md").read_text(encoding="utf-8")
    assert d["nombre_de_lignes"] == 4
    for go in ("GO-2026-11-18-14", "GO-2026-11-22-80", "GO-2026-11-22-141", "GO-2026-11-22-142"):
        assert f"| {go} |" in texte
    assert "GO-2026-11-20-03" not in texte and "| GO-2026-11-22-107 |" not in texte


def test_v11b_sur_le_vrai_registre_de_main(tmp_path):
    p = subprocess.run(["git", "-C", str(RACINE), "show", "refs/remotes/origin/main:registres/go.md"], capture_output=True)
    if p.returncode != 0 or b"| GO-2026-11-22-80 |" not in p.stdout:
        pytest.skip("registre de main sans la ligne GO-2026-11-22-80")
    reg = tmp_path / "go.md"
    reg.write_bytes(p.stdout)
    assert L.verifier_go(reg, dt.date(2026, 11, 26))["id"] == "GO-2026-11-22-80"
    assert L.lire_prolongation(reg, dt.date(2026, 11, 26), L.GO_ID, L.GO_COURSE_INITIAL)["valide"] is True
    assert L.verifier_go_initial(reg)["id"] == "GO-2026-11-18-14"
    with pytest.raises(L.Refus):
        L.verifier_go(reg, dt.date(2026, 12, 16))
    with pytest.raises(L.Refus, match="GO-2026-11-22-107 hors de sa période"):     # aucune confirmation nommée au 26
        L.verifier_les_go(reg, dt.date(2026, 11, 26), _fixe_confirmation(None))
    d = L.ecrire_registre_derive(reg, tmp_path / "derive.md")
    texte = (tmp_path / "derive.md").read_text(encoding="utf-8")
    assert "| GO-2026-11-22-80 |" in texte and "| GO-2026-11-18-14 |" in texte


# --- l'orchestrateur épinglé lit le registre dérivé v11b (vraie lecture, `configuration_v55.verifier_go_v55`) ------------------
EMPREINTES_LECTURE_GO = {"pole/configuration_v55.py": "2e6237c0a8b1c823fa17ddd6c680357a59ec4030bfbe9ac6ba970a700a864071",
                         "pole/configuration_v53.py": "ef72ffbf"}


def _lecture_go_orchestrateur():
    cands = [Path(os.environ["ORCHESTRATEUR_AFFINAGE_ESSAI"])] if os.environ.get("ORCHESTRATEUR_AFFINAGE_ESSAI") else []
    cands += list(L.ORCHESTRATEURS_CANDIDATS)
    for o in cands:
        if all((o / rel).is_file() and hashlib.sha256((o / rel).read_bytes()).hexdigest().startswith(sha)
               for rel, sha in EMPREINTES_LECTURE_GO.items()):
            sys.path.insert(0, str(o))
            ancien, sys.dont_write_bytecode = sys.dont_write_bytecode, True
            try:
                from pole.configuration_v55 import verifier_go_v55
                from pole.configuration_v53 import GoRefuse
            finally:
                sys.path.remove(str(o))
                sys.dont_write_bytecode = ancien
            return verifier_go_v55, GoRefuse
    pytest.skip("orchestrateur épinglé (a41b7b50) absent : variable ORCHESTRATEUR_AFFINAGE_ESSAI")


def test_v11b_orchestrateur_accepte_go_80_au_26_et_refusait_go_14(tmp_path):
    verifier_go_v55, GoRefuse = _lecture_go_orchestrateur()
    d = L.ecrire_registre_derive(_registre_go_essai(tmp_path, L14, L80, L107, L124, L131), tmp_path / "derive.md")
    g = verifier_go_v55(L.GO_ID, d["derive"], 150.0, aujourd_hui=dt.date(2026, 11, 26))
    assert g["identifiant"] == "GO-2026-11-22-80" and g["plafond_lu_usd"] == 150.0 and g["echeance"] == "2026-12-15"
    with pytest.raises(GoRefuse, match="période"):                              # ce que v11 lui passait
        verifier_go_v55("GO-2026-11-18-14", d["derive"], 150.0, aujourd_hui=dt.date(2026, 11, 26))
    with pytest.raises(GoRefuse, match="période"):
        verifier_go_v55(L.GO_ID, d["derive"], 150.0, aujourd_hui=dt.date(2026, 12, 16))


def test_v11b_orchestrateur_refuse_go_80_revoque_au_registre_derive(tmp_path):
    verifier_go_v55, GoRefuse = _lecture_go_orchestrateur()
    rev2 = "| GO-2026-11-22-41 | 2026-11-22 | révocation | révoque GO-2026-11-22-80 | — | — | Lazar | — |\n"  # deux chiffres : lisible par lui
    d = L.ecrire_registre_derive(_registre_go_essai(tmp_path, L14, L80, rev2), tmp_path / "derive.md")
    with pytest.raises(GoRefuse, match="révoqué"):
        verifier_go_v55(L.GO_ID, d["derive"], 150.0, aujourd_hui=dt.date(2026, 11, 26))


# === v11c : corrections de la contre-lecture du lanceur v11b (`contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`) ==================


def test_v11c_version_et_pieces():
    assert L.VERSION == "lancer_course_affinage_mentors_v11d"
    assert L.PIECES["configuration"][0].endswith("configuration-course-affinage-mentors-v11d.json")
    assert L.PIECES["commande_carbon"][0] == "scripts/commande_gemini_flux_v2.py"
    assert L.PIECES["commande_carbon"][1] == hashlib.sha256((RACINE / "scripts/commande_gemini_flux_v2.py").read_bytes()).hexdigest()
    assert L.PIECES["configuration"][1] == hashlib.sha256((RACINE / L.PIECES["configuration"][0]).read_bytes()).hexdigest()
    assert not hasattr(L, "PART_CLAUDE_HAUT_USD") and not hasattr(L, "RESERVE_APPEL_CLAUDE_USD")
    assert "code 7" not in json.dumps(FIXE["changements_v11"]["plafond_part_claude_source"], ensure_ascii=False)


# --- constat 1 : base de l'écart au devis ------------------------------------------------------------------------------------------


def test_v11c_base_de_l_ecart_au_devis_egale_au_texte():
    assert L.PRIX_ARGON_PROPOSEUR_PAR_APPEL_USD == 0.133012 and L.PRIX_ARGON_JUGE_PAR_APPEL_USD == 0.016723
    assert L.PRIX_CARBON_PAR_APPEL_USD == 0.480472
    cinq = ["prop-opus", "prop-fable", "prop-argon", "prop-astra", "prop-carbon"]
    assert round(L.devis_estimation(cinq), 3) == 35.683 == round(L.DEVIS_V5_TOTAL["cinq_especes"], 3)
    assert L.devis_estimation(cinq) != pytest.approx(40.848)                        # artefact : la base du lanceur v11b


def test_v11c_ecart_au_devis_au_manifeste_de_fin_sur_la_base_du_texte(monde):
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["ecart_au_devis"]["devis_estimation_sans_marge_usd"] == pytest.approx(L.devis_estimation(dep["especes_actives"]))
    assert "part_haut_usd" not in dep["cle_claude"]                                 # constat 15


# --- constat 3 : ligne de LUC au relevé des crédits ---------------------------------------------------------------------------


def test_v11c_ligne_de_luc_saine_au_manifeste(monde):
    assert lancer(monde["r"]) == 0
    c = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())["releve_credits_avant"]["cles"][L.CLE_CLAUDE]
    assert c["ligne_du_releve"] == {"solde_non_lu": True, "reference": "GO-2026-11-22-124", "source": "essai : relevé du jour"}


@pytest.mark.parametrize("ligne,motif", [
    ({"reference": "GO-2026-11-22-124"}, "solde_non_lu"),                                     # mention absente
    ({"solde_non_lu": False, "reference": "GO-2026-11-22-124"}, "solde_non_lu"),
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-107"}, "solde_non_lu"),               # autre référence
    ({"solde_non_lu": True}, "solde_non_lu"),
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-124", "solde_console_usd": 860.0}, "refusé"),   # un solde
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-124", "credit_usd": 100.0, "reste_usd": 80.0}, "refusé"),
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-124", "couverture_usd": 20.65}, "refusé"),
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-124", "recharge_declaree_usd": 40.0}, "refusé"),
    ({"solde_non_lu": True, "reference": "GO-2026-11-22-124", "autre": "x"}, "refusé"),       # champ hors liste
    ({"non_lisible": True, "motif": "solde non lu (GO-124)"}, "solde_non_lu"),                 # forme du v11b
    ("solde non lu", "s'écrit"),                                                               # pas un objet
])
def test_v11c_ligne_de_luc_artefacts_refuses(monde, capsys, ligne, motif):
    _releve(monde, releve(RR_ANTHROPIC_API_KEY_LUC=ligne))
    assert lancer(monde["r"]) == 2
    assert motif in capsys.readouterr().err
    assert not monde["r"].dossier_runs.exists() or not list(monde["r"].dossier_runs.glob("*/manifeste-lanceur-depart.json"))


def test_v11c_verifier_ligne_luc_unitaire():
    assert L.verifier_ligne_luc(luc()) == luc() and L.verifier_ligne_luc(luc(note="x"))["note"] == "x"
    for mauvais in (None, {}, luc(solde_usd=1.0), luc(reference="GO-2026-11-22-12"), luc(solde_non_lu="oui")):
        with pytest.raises(L.Refus):
            L.verifier_ligne_luc(mauvais)


# --- constat 4 : libellé de la contre-lecture ----------------------------------------------------------------------------------


def test_v11c_libelle_de_contre_lecture_sain_et_artefacts(monde, capsys):
    assert L.LIBELLE_CONTRE_LECTURE == "Opus 5.5, contre-lecteur neuf"
    for autre in ("modèle K", "Opus 5.5", "contre-lecteur neuf", "Opus 5.5 contre-lecteur"):   # artefacts d'abord (rien ne part)
        _cl(monde, contre_lecture(PREREG_SHA, monde["lanceur_sha"]).replace("Opus 5.5, contre-lecteur neuf", autre))
        assert lancer(monde["r"]) == 2, autre
        assert "libellé" in capsys.readouterr().err
    _cl(monde, contre_lecture(PREREG_SHA, monde["lanceur_sha"]))
    assert lancer(monde["r"]) == 0


# --- constat 5 : relecture finale du relais Claude après l'arrêt de l'orchestrateur ----------------------------------------------


def _orchestrateur_qui_ecrit_un_refus_et_sort(m, statut=400, code=3, motif=None):
    """Faux orchestrateur : attend 0,5 s (après la première lecture du lanceur), écrit une ligne de statut au journal du relais
    Claude, puis sort aussitôt avec `code`."""
    shutil.rmtree(m["orch"])
    o, commit, empreintes = faux_orchestrateur(m["tmp"])
    v8 = o / "demonstrations" / "ideation_v8.py"
    ligne = {"statut": statut, "chemin": "/v1/messages"}
    if motif:
        ligne["motif"] = motif
    v8.write_text(v8.read_text().replace("arrete = False\n", (
        "arrete = False\nif '--verifier-seulement' not in a:\n    import time\n    time.sleep(0.5)\n"
        f"    open({str(_journal_claude(m))!r}, 'a').write({json.dumps(ligne)!r} + '\\n')\n"
        + (f"    sys.exit({code})\n" if code is not None else "")), 1))
    git(o, "-c", "user.email=t@example.invalid", "-c", "user.name=t", "commit", "-q", "-am", "refus puis sortie")
    commit = subprocess.run(["git", "-C", str(o), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    empreintes = dict(empreintes, **{"demonstrations/ideation_v8.py": hashlib.sha256(v8.read_bytes()).hexdigest()})
    m["r"].orchestrateurs, m["r"].commit_orchestrateur, m["r"].empreintes_orchestrateur = (o,), commit, empreintes
    m["orch"] = o
    m["r"].intervalle_surveillance_s = 1000.0                   # une seule lecture pendant la course : au départ


@pytest.mark.parametrize("statut,motif,nature", [(400, None, "interface"), (402, "plafond de dépense du relais atteint", "relais")])
def test_v11c_refus_ecrit_apres_la_derniere_lecture_vu_a_la_relecture_finale(monde, capsys, statut, motif, nature):
    vu = _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.0, refus=0)
    _orchestrateur_qui_ecrit_un_refus_et_sort(monde, statut=statut, motif=motif)
    assert lancer(monde["r"]) == 5                                                  # et non 6 (orchestrateur en code 3)
    run = un_run(monde["r"])
    assert L.scelle(run / "alerte-arret-part-claude.json")
    alerte = json.loads((run / "alerte-arret-part-claude.json").read_text())
    assert alerte["moment"].startswith("relecture finale") and alerte["statut"] == statut and nature in alerte["nature"]
    if motif:
        assert alerte["cause"] == motif                                             # constat 7 : la cause réelle, lue
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    assert fin["code"] == 3 and fin["code_du_lanceur"] == 5 and vu["lectures"] >= 2
    assert "arret_cle_claude" in capsys.readouterr().err


def test_v11c_mutation_sans_relecture_finale_rend_6(monde):
    """Artefact (R5) : la relecture finale retirée, le même refus donne le code 6, sans alerte."""
    m = _mutant("lanceur_v11c_mutant_finale", [("            arret_luc = surveillance.lecture_finale()\n",
                                                "            arret_luc = None\n")])
    _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.0, refus=0)
    _orchestrateur_qui_ecrit_un_refus_et_sort(monde)
    assert m.principal([], reglages=monde["r"]) == 6
    assert not (un_run(monde["r"]) / "alerte-arret-part-claude.json").exists()


def test_v11c_relecture_finale_sans_refus_ne_change_rien(monde):
    _etat_claude_apres_depart(monde, depense_usd=3.0, engage_usd=0.0, refus=0)
    _orchestrateur_qui_ecrit_un_refus_et_sort(monde, statut=200, code=None)   # puis la course finit normalement
    assert lancer(monde["r"]) == 0
    fin = json.loads((un_run(monde["r"]) / "manifeste-lanceur-fin.json").read_text())
    assert fin["cle_claude_au_fil_de_l_eau"]["appels_par_statut"] == {"200": 1}


def test_v11c_lecture_finale_illisible_refaite_puis_code_5():
    class R:
        lire_etat_relais = None
    r = R()
    r.lire_etat_relais = lambda url: (_ for _ in ()).throw(OSError("injoignable"))
    s = L.SurveillanceCleClaude(r, "http://127.0.0.1:1", 45.0)
    a = s.lecture_finale()
    assert a["code"] == 5 and "illisible 3 fois" in a["motif"] and s.lignes_ecrites == 3


# --- constat 6 : journal du run, comptes par statut, dépassement --------------------------------------------------------------


def test_v11c_journal_du_run_et_comptes_au_manifeste_de_fin(monde):
    _etat_claude_apres_depart(monde, depense_usd=12.0, engage_usd=0.4, refus=0, appels_au_dessus_de_la_reserve=7,
                              depassement_max_usd=1.85, reserve_par_appel_usd=0.4)
    _journal_claude(monde).write_text("".join(json.dumps({"statut": s}) + "\n" for s in (200, 200, 429, 529, 200)), encoding="utf-8")
    assert lancer(monde["r"]) == 0
    run = un_run(monde["r"])
    c = json.loads((run / "manifeste-lanceur-fin.json").read_text())["cle_claude_au_fil_de_l_eau"]
    assert c["appels_par_statut"] == {"200": 3, "429": 1, "529": 1}
    assert c["depassement_max_usd"] == 1.85 and c["appels_au_dessus_de_la_reserve"] == 7 and c["reserve_par_appel_usd"] == 0.4
    j = c["journal_du_run"]
    p = Path(j["chemin"])
    assert p.parent == run and p.name == L.JOURNAL_PART_CLAUDE and L.scelle(p) and j["sha256"] == L.sha256_fichier(p)
    lignes = [json.loads(x) for x in p.read_text().splitlines()]
    assert len(lignes) == j["lignes"] == c["lectures_ecrites_au_journal_du_run"] >= 2          # au fil de l'eau + relecture finale
    assert lignes[-1]["moment"] == "relecture finale" and lignes[0]["etat"]["depense_usd"] == 12.0
    assert sum(sum(x["statuts_neufs"].values()) for x in lignes) == 5                        # chaque ligne du relais comptée une fois
    texte = p.read_text()
    assert "texte" not in texte and "consigne" not in texte                                   # montants, comptes, statuts seulement


def test_v11c_ligne_du_relais_en_cours_d_ecriture_lue_la_fois_suivante(tmp_path):
    j = tmp_path / "journal.jsonl"
    j.write_text(json.dumps({"statut": 200}) + "\n" + '{"statut": 40', encoding="utf-8")     # dernière ligne sans fin de ligne

    class R:
        lire_etat_relais = staticmethod(lambda url: {"depense_usd": 1.0, "engage_usd": 0.0, "refus": 0})
    s = L.SurveillanceCleClaude(R(), "http://127.0.0.1:1", 45.0, journal=str(j), journal_run=tmp_path / "run.jsonl")
    assert s.depasse() is None and s.illisibles == 0 and s.par_statut == {"200": 1}
    with open(j, "a", encoding="utf-8") as f:
        f.write('0}\n')
    a = s.depasse()
    assert a["code"] == 5 and a["statut"] == 400 and s.par_statut == {"200": 1, "400": 1}


# --- constat 7 : nature, statut et cause réels -----------------------------------------------------------------------------------


@pytest.mark.parametrize("ligne,nature,cause", [
    ({"statut": 401, "motif": "jeton différent du jeton factice"}, "refus du relais Claude", "jeton différent du jeton factice"),
    ({"statut": 403, "motif": "modèle non permis (R-764)"}, "refus du relais Claude", "modèle non permis (R-764)"),
    ({"statut": 400, "en_flux": False, "octets": 120}, "refus de l'interface d'Anthropic, relayé", "inconnue"),
])
def test_v11c_alerte_dit_la_nature_et_la_cause_reelles(tmp_path, ligne, nature, cause):
    j = tmp_path / "journal.jsonl"
    j.write_text(json.dumps(ligne) + "\n", encoding="utf-8")

    class R:
        lire_etat_relais = staticmethod(lambda url: {"depense_usd": 1.0, "engage_usd": 0.0, "refus": 1 if "motif" in ligne else 0})
    a = L.SurveillanceCleClaude(R(), "http://127.0.0.1:1", 45.0, journal=str(j)).depasse()
    assert a["nature"] == nature and a["statut"] == ligne["statut"] and a["cause"].startswith(cause)
    assert f"statut {ligne['statut']}" in a["motif"]


def test_v11c_refus_compte_a_l_etat_sans_ligne_lue_ne_pretend_pas_402(tmp_path):
    class R:
        lire_etat_relais = staticmethod(lambda url: {"depense_usd": 1.0, "engage_usd": 0.0, "refus": 1})
    a = L.SurveillanceCleClaude(R(), "http://127.0.0.1:1", 45.0).depasse()
    assert a["nature"] == "refus du relais Claude" and a["statut"] is None and "la ligne du journal dit lequel" in a["cause"]


# --- constat 8 : réserve par appel du relais Claude -------------------------------------------------------------------------------


def test_v11c_reserve_du_relais_claude_lue_au_depart(monde):
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    c = dep["procedure_relais_persistants"]["relais_vivants"]["claude"]
    assert c["reserve_par_appel_usd"] == 0.4 and c["reserve_par_appel_source"].startswith("état")
    assert c["depassement_possible_par_appel_en_vol_usd"] == pytest.approx(3.0 - 0.4)


@pytest.mark.parametrize("args,etat,issue", [
    ("0.4", 0.4, 0), ("0.5", 0.4, 2), (None, None, 2), (None, 45.0, 2), (None, -0.1, 2), ("x", 0.4, 2)])
def test_v11c_reserve_du_relais_claude_artefacts(monde, args, etat, issue):
    c = monde["cmdlines"][PID_CLAUDE]
    if args is not None:
        c += ["--reserve-par-appel", args]
    if etat is None:
        del monde["etat_claude"]["reserve_par_appel_usd"]
    else:
        monde["etat_claude"]["reserve_par_appel_usd"] = etat
    assert lancer(monde["r"]) == issue


# --- constat 9 : sonde commune v3 ------------------------------------------------------------------------------------------------


def _commune_modifiee(monde, monkeypatch, changer):
    _astra(monde, monkeypatch)                                                      # Astra déclarée : la sonde est lue
    depot = monde["depot"]
    v2 = json.loads((depot / L.SONDE_ASTRA).read_text())
    o = json.loads((depot / COMMUNE_DU_JOUR).read_text())
    changer(o)
    ecrire_sondes(depot, v2=v2, commune=o)


def test_v11c_sonde_commune_v3_saine(monde, monkeypatch):
    _commune_modifiee(monde, monkeypatch, lambda o: None)
    assert lancer(monde["r"]) == 0


@pytest.mark.parametrize("variable", [None, "OPENAI_API_KEY", "OPENAI_API_KEY_3"])
def test_v11c_sonde_commune_d_une_autre_variable_de_cle_refusee(monde, monkeypatch, capsys, variable):
    def changer(o):
        if variable is None:
            del o["relais_jete"]["variable_cle"]
        else:
            o["relais_jete"]["variable_cle"] = variable
    _commune_modifiee(monde, monkeypatch, changer)
    assert lancer(monde["r"]) == 2
    assert "variable de clé du relais jeté" in capsys.readouterr().err


def test_v11c_sonde_commune_v2_refusee(monde, monkeypatch, capsys):
    _commune_modifiee(monde, monkeypatch, lambda o: o.__setitem__("version", "sonde_astra_courses_v2"))
    assert lancer(monde["r"]) == 2
    assert "sonde_astra_courses_v2" in capsys.readouterr().err


# --- constat 11 : garde Google sur la plus longue entrée de chaque rôle, juge de la forme de l'orchestrateur ---------------------


def test_v11c_entree_de_juge_de_la_forme_de_l_orchestrateur():
    consigne = Path(_pieces_rel()["consigne_juge"]["absolu"]).read_text(encoding="utf-8")
    e = L.entree_juge_la_plus_longue(consigne)
    assert e.startswith(consigne.rstrip() + "\n\n## La fiche\n```json\n") and e.endswith("\n```\n")
    corps = e[len(consigne.rstrip() + "\n\n## La fiche\n```json\n"):-len("\n```\n")]
    fiche = json.loads(corps)
    assert len(fiche["carte"]) == L.CARACTERES_PAR_CARTE_MAX and len(e) > len(consigne) + L.CARACTERES_PAR_CARTE_MAX + 1000


def test_v11c_garde_google_rejouee_sur_la_plus_longue_entree_de_chaque_role(monde):
    if _octets_de_main("src/controle_ia/garde_google_v3.py") is None:
        pytest.skip("garde Google absente de origin/main")
    monde["r"].controler_google = None
    assert lancer(monde["r"]) == 0
    dep = json.loads((un_run(monde["r"]) / "manifeste-lanceur-depart.json").read_text())
    roles = {x["role"]: x for x in dep["garde_google"]["argon"]["roles"]}
    consigne_j = (monde["depot"] / L.PIECES["consigne_juge"][0]).read_text(encoding="utf-8")
    assert roles["juge_ideation"]["entree_caracteres"] == len(L.entree_juge_la_plus_longue(consigne_j))
    consigne_p = (monde["depot"] / L.PIECES["consigne_proposeur"][0]).read_text(encoding="utf-8")
    plus_longue = max(len(L.consigne_servie_proposeur(consigne_p, L.expurger(L.texte_de_case(f))[0])) for f in LISTE_V11["fils"])
    assert roles["proposeur_ideation"]["entree_caracteres"] == plus_longue
    assert all(not x["problemes"] for x in roles.values())


# --- constat 15 : GO-2026-11-22-124, le montant de la part Claude lu --------------------------------------------------------------


@pytest.mark.parametrize("plafond,issue", [
    ("inchangé (150 USD ; part Claude 45 USD)", "sain"), ("inchangé (150 USD ; part Claude 45,0 USD)", "sain"),
    ("inchangé (150 USD ; part Claude 145 USD)", "refus"), ("inchangé (150 USD ; part Claude 4500 USD)", "refus"),
    ("inchangé (450 USD)", "refus"), ("45", "refus")])
def test_v11c_go_124_montant_45_lu_exactement(tmp_path, plafond, issue):
    ligne = L124.replace("| inchangé (150 USD ; part Claude 45 USD) |", f"| {plafond} |")
    reg = _registre_go_essai(tmp_path, ligne)
    if issue == "sain":
        assert L.verifier_go_simplification(reg, dt.date(2026, 11, 26))["id"] == "GO-2026-11-22-124"
    else:
        with pytest.raises(L.Refus, match="part Claude 45 USD"):
            L.verifier_go_simplification(reg, dt.date(2026, 11, 26))


# === v11d : régression R1 (essai à blanc), configuration v11d, gabarit du relevé des crédits v11d =============================


@pytest.fixture
def depot_a_blanc(tmp_path, monkeypatch):
    """Dépôt d'essai pour l'essai à blanc : pièces copiées du dépôt (garde Google de origin/main), préenregistrement d'essai
    scellé ; `DEPOT` du lanceur pointé dessus ; extraction de main faite depuis le dépôt réel."""
    garde = _octets_de_main(L.PIECES["garde_google"][0])
    if garde is None:
        pytest.skip("garde Google absente de origin/main")
    depot = tmp_path / "depot-a-blanc"
    for nom, (rel, _) in L.PIECES.items():
        (depot / rel).parent.mkdir(parents=True, exist_ok=True)
        (depot / rel).write_bytes(garde if nom == "garde_google" else octets_piece(rel))
    pre = depot / L.PREREG
    pre.parent.mkdir(parents=True, exist_ok=True)
    pre.write_text(PREREG_TEXTE, encoding="utf-8")
    sceller(pre)
    monkeypatch.setattr(L, "DEPOT", depot)
    origine = L.extraire_de_main
    monkeypatch.setattr(L, "extraire_de_main", lambda d, chemin, attendu, dest: origine(RACINE, chemin, attendu, dest))
    return depot


def _cles_de(decl: dict) -> dict:
    return {f: b["nom_cle"] for f, b in decl["fournisseurs"].items()}


def test_v11d_releve_de_l_essai_a_blanc_passe_verifier_credits(depot_a_blanc, tmp_path):
    r = L.reglages_a_blanc(tmp_path / "a-blanc")
    releve = json.loads(r.releve.read_text())
    assert releve["cles"][L.CLE_CLAUDE] == {"solde_non_lu": True, "reference": "GO-2026-11-22-124", "source": "essai à blanc"}
    jour = L._dt.date.fromisoformat(releve["releve_utc"][:10])
    o = L.verifier_credits(releve, _cles_de(json.loads(r.declaration.read_text())), jour, tmp_path / "alerte", {})
    assert o[L.CLE_CLAUDE]["ligne_du_releve"]["solde_non_lu"] is True and o[L.CLE_CLAUDE]["condition_de_depart"] is None


def test_v11d_artefact_ligne_de_luc_de_l_essai_a_blanc_v11c_refusee():
    v11c = {"solde_console_usd": 0.0, "source": "essai à blanc : aucune lecture réelle", "recharge_declaree_usd": 100.0,
            "recharge_source": "essai à blanc : valeur factice"}
    with pytest.raises(L.Refus, match="solde_non_lu"):
        L.verifier_ligne_luc(v11c)


def test_v11d_essai_a_blanc_de_bout_en_bout_moteur_simule_rend_0(depot_a_blanc, tmp_path, capsys):
    dossier = tmp_path / "a-blanc-complet"
    r = L.reglages_a_blanc(dossier)
    o, commit, empreintes = faux_orchestrateur(tmp_path)
    r.orchestrateurs, r.commit_orchestrateur, r.empreintes_orchestrateur = (o,), commit, empreintes
    r.sorties_courses = ()
    assert L.principal(["--a-blanc", str(dossier)], reglages=r) == 0, capsys.readouterr().err
    run = [p for p in (dossier / "runs").iterdir() if p.name.endswith(L.SUFFIXE_RUN)]
    assert len(run) == 1 and L.scelle(run[0] / "manifeste-lanceur-fin.json")
    dep = json.loads((run[0] / "manifeste-lanceur-depart.json").read_text())
    assert dep["releve_credits_avant"]["cles"][L.CLE_CLAUDE]["ligne_du_releve"]["solde_non_lu"] is True


def test_v11d_mutation_essai_a_blanc_avec_la_ligne_v11c_refuse(depot_a_blanc, tmp_path):
    """Artefact (R5) : la ligne de LUC du v11c rétablie dans l'essai à blanc, le départ est refusé (code 2)."""
    m = _mutant("lanceur_v11d_mutant_a_blanc", [(
        '''**{CLE_CLAUDE: {"solde_non_lu": True, "reference": REFERENCE_LUC_SANS_SOLDE,  # v11d, R1\n''',
        '''**{CLE_CLAUDE: {"solde_console_usd": 0.0, "recharge_declaree_usd": 100.0,\n''')])
    monkeypatch_depot = L.DEPOT
    m.DEPOT, m.extraire_de_main = monkeypatch_depot, L.extraire_de_main
    dossier = tmp_path / "a-blanc-mutant"
    r = m.reglages_a_blanc(dossier)
    o, commit, empreintes = faux_orchestrateur(tmp_path)
    r.orchestrateurs, r.commit_orchestrateur, r.empreintes_orchestrateur = (o,), commit, empreintes
    r.sorties_courses = ()
    assert m.principal(["--a-blanc", str(dossier)], reglages=r) == 2


# --- configuration v11d ----------------------------------------------------------------------------------------------------------


def test_v11d_configuration_notes_et_plafond_inerte_retire():
    c = FIXE["changements_v11"]
    assert "commande_gemini_flux_v2.py" in c["carbon"] and "commande_gemini_flux_v2.py" in c["argon"]
    assert "commande_gemini_flux_v1.py" not in c["carbon"] + c["argon"]
    assert "plafond_relais_claude_usd" not in FIXE["relais_persistants_v4"]
    assert 'plafond_relais_claude_usd"' not in CHEMIN_LANCEUR.read_text(encoding="utf-8")      # aucun code ne le lisait


# --- gabarit du relevé des crédits v11d -------------------------------------------------------------------------------------------


GABARIT_RELEVE = RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v11/releve-credits-gabarit-course-affinage-v11d.json"
GABARIT_DECL = RACINE / "docs/notes/organisme-affinage-mentors-v1/course-v11/declaration-relais-gabarit-course-affinage-v11c.json"


def test_v11d_gabarit_du_releve_des_credits_rempli_passe_verifier_credits(tmp_path):
    g = json.loads(GABARIT_RELEVE.read_text())
    assert g["cles"][L.CLE_CLAUDE] == {"solde_non_lu": True, "reference": "GO-2026-11-22-124",
                                       "source": g["cles"][L.CLE_CLAUDE]["source"]}
    g["releve_utc"] = "2026-11-26T07:00:00Z"
    o = L.verifier_credits(g, _cles_de(json.loads(GABARIT_DECL.read_text())), dt.date(2026, 11, 26), tmp_path / "alerte", {})
    assert set(o) == {L.CLE_CLAUDE, "GEMINI_API_KEY", "OPENAI_API_KEY_2"} and o[L.CLE_CLAUDE]["condition_de_depart"] is None


def test_v11d_gabarit_non_rempli_refuse(tmp_path):
    g = json.loads(GABARIT_RELEVE.read_text())
    with pytest.raises(L.Refus):
        L.verifier_credits(g, _cles_de(json.loads(GABARIT_DECL.read_text())), dt.date(2026, 11, 26), tmp_path / "a", {})
