#!/usr/bin/env python3
"""Lanceur de l'organisme d'idéation (atelier d'idées, N-065 rôle 2) sur la question des bassins d'idées étroits et
profonds : trois générations enchaînées — version 3.

Version 3, après la génération 1 jouée par la version 2 (`lancer_course_ideation_bassins_etroits_v2.py`, `c6d82d8c…`,
inchangée, R12), close en défaut au contrôle (0,275477 USD, Argon seul ; `operation-g1-v1.md`, `3beef39e…`), et la
vérification courte du v2 (`verification-courte-lanceur-v2-v1.md`, `ff33dd99…`) :
- **cause établie sans dépense** (`preparateur-outils-v3/eprouver_authentification_kit_v1.py`) : hérités de la session, les
  noms `CLAUDE_CODE_REMOTE*` font présenter par le kit d'agent un `Authorization: Bearer` de l'hôte au lieu du jeton factice
  en `x-api-key` ; le relais rend 401, le kit rend un message « <synthetic> » ;
- **environnement transmis par liste de noms permis** (`NOMS_PERMIS`) : PATH, LANG, LC_ALL, TZ, TMPDIR ; HOME fixé par le
  lanceur à un dossier neuf hors du dépôt ; GO_ID et PYTHONPYCACHEPREFIX fixés par lui ; tout autre nom (`ANTHROPIC_*`,
  `CLAUDE*`, `CCR_*`, mandataires, clés…) est exclu ; noms transmis et noms exclus au manifeste (noms seulement) ;
- **relance étroite** : une génération peut être relancée **une fois** si la tentative précédente a fini proprement (code
  scellé), sans aucune fiche produite, avec une dépense relevée lisible, comptée au cumul ; jamais après des fiches ; deux
  courses par génération au plus ; les runs du v2 sont lus comme tentatives antérieures (la course v2 de la génération 1
  compte pour la première, 0,275477 USD) ;
- **verrou d'invocation** (R1) : verrou exclusif (`fcntl.flock`) de la lecture de l'état au manifeste de départ ;
- **orchestrateur orphelin** (R2) : superviseur mort, orchestrateur vivant → la clôture le dit, code **4**, et rien ne part
  tant qu'il vit ; le superviseur écrit l'heure de départ du processus de l'orchestrateur ;
- R4 : exception au détachement du bras gardée ; R9 : compte rendu et clôture avant les gardes d'entrée ;
- essais des quatre mutations survivantes de la vérification courte (zombie, seuil, bras mort compté, bras sans code).

Usage, seul et exact (cwd = racine du dépôt de travail) :

    /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v3.py 1     (puis 2, puis 3)

Une invocation fait **une** chose : compte rendu d'un processus en marche (code 3) ; orchestrateur orphelin vivant (code 4) ;
clôture des processus finis (code 0) ; lancement détaché d'une course ou d'un bras (code 0) ; refus (code 2). Arrêt d'une
course : `kill -TERM <PID du superviseur>` (relayé par PID ; R10) ; d'un orphelin : `kill -TERM <PID de l'orchestrateur>`.

Bibliothèque standard seulement. Essais : `tests/test_lancer_course_ideation_bassins_etroits_v3.py`.
"""
from __future__ import annotations

import datetime as _dt
import fcntl
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping

VERSION = "lancer_course_ideation_bassins_etroits_v3"
GO_ID = "GO-2026-11-13-03"
DEPOT = Path(__file__).resolve().parents[1]
GENERATIONS = ("1", "2", "3")

# --- orchestrateur (dépôt public lciric/ideation-organism, clone en lecture), épinglé --------------------------------------
ORCHESTRATEUR = Path("/home/user/lciric/ideation-organism/orchestrator")
COMMIT_ORCHESTRATEUR = "be6b5af96c9e19812569d8dab55d6ce3978a3823"
EMPREINTES_ORCHESTRATEUR = {
    "demonstrations/ideation_v8.py": "2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1",
    "demonstrations/ideation_v7.py": "7b90e65e1308b1c230b3f804743cfc42b9dc571d93b73ed6c5f3f8c9d2b481b2",
    "demonstrations/ideation_v6.py": "4c302e5b97b229d5b3edd9e9a427f1e50796c10f7081f63132165ffeef854ba4",
    "demonstrations/ideation_v5.py": "1894f250264eaaccbf891dfa255e71dc587fe415c8d21e283391203a2fe73444",
    "demonstrations/ideation_v4.py": "4212d4c9d014a265847d4c4ed87a8cd804fdafa73f85fd8947874d63fca1c36d",
    "demonstrations/ideation_v2.py": "bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845",
    "pole/ideation_v2.py": "67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc",
    "pole/adaptateurs.py": "a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99",
    "pole/relais.py": "b5a76343e458cf8fb91ee1928244f9cb65d50c27ab9b1bae91c21a5c82349da3",
}
LANCEUR_ORCHESTRATEUR = "demonstrations/ideation_v8.py"

# --- pièces fixes, épinglées --------------------------------------------------------------------------------------------
NOTES = "docs/notes/organisme-bassins-etroits-v1"
PIECES = {
    "question": (f"{NOTES}/question-organisme-bassins-etroits-v1.md",
                 "c188fa9a8ada9c8793bb5a9150596a2583614ee1c8583d8b5ceab226667df7ef"),
    "faits": ("docs/notes/collisionneur-bassins-etroits-v1/faits-v1.md",
              "d19b540015ed9480774c020cd7f1a527db32d42600a5bc2bd34c92c17d7be0b3"),
    "temoins": (f"{NOTES}/temoins-bassins-etroits-v2.json",
                "f1ddcef9748d63e8884176c6e846bb65ef9df0b4e261e486b0656a5344687631"),
    "enveloppe_argon": ("rapports/fille-ideation-1-v1/appel-argon-v5.sh",
                        "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"),
    "commande_argon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py",
                       "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46"),
}
# pièces et attestations à chemin fixe, non épinglables d'avance : scellées (compagnon `.sha256`), empreintes au manifeste
ATTESTATIONS = f"{NOTES}/attestations"
RECOUPEMENT = f"{NOTES}/recoupement-methodes-v1.md"            # génération 1 : fourni par la mère
TAILLE_MAX_RECOUPEMENT = 40_000                                 # caractères
RELECTURE_RECOUPEMENT = f"{ATTESTATIONS}/attestation-relecture-recoupement-v1.json"
CONFIRMATION_REGLE = f"{ATTESTATIONS}/confirmation-regle-de-passage-v1.md"
MOTIF_ATTESTATION = r"attestation-lecture-humaine-g{g}-v(\d+)\.json"   # par génération, avant son bras ; la plus haute
TAILLE_MAX_FICHES_RECUES = 50_000                               # caractères de la pièce entière (générations 2 et 3)
NOMBRE_FICHES_RECUES = 5
DEPOT_ATTENDU_PAR_L_ENVELOPPE = Path("/home/user/controle-ia-travail")

# --- plafonds (GO-2026-11-13-03 : par course 12 + 8 ; ligne 60) ------------------------------------------------------------
TOTAL_LIGNE_USD = 60.0
TOTAL_CLAUDE_USD = 12.0
TOTAL_EXTERNE_USD = 8.0
PLAFOND_COURSE_USD = TOTAL_CLAUDE_USD + TOTAL_EXTERNE_USD
NOMBRE = 6
PLAFONDS = {
    "proposeur_ideation|claude-opus-5-5": 2.0,
    "proposeur_ideation|claude-fable-5-1": 2.0,
    "juge_ideation|claude-opus-5-5": 1.5,
    "proposeur_ideation|gemini-4-argon": 1.3,   # passe 1 d'Argon
    "juge_ideation|gemini-4-argon": 2.5,        # bras différé
}
CONTROLE_EXTERNE_USD = 1.7                      # M2 : tient la consigne de contrôle à 3 caractères par jeton
PASSE_2_EXTERNE_USD = 1.9
CONTROLE_BRAS_USD = 0.6                         # contrôle court d'Argon au bras (plancher ≈ 0,51)
PLAFOND_BRAS_USD = PLAFONDS["juge_ideation|gemini-4-argon"] + CONTROLE_BRAS_USD
MAX_TENTATIVES = 3                              # bras
PROPOSEURS = (("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1"))
PROPOSEUR_EXTERNE = ("argon", "gemini-4-argon")
JUGES = (("opus-juge", "claude-opus-5-5"),)
JUGE_EXTERNE = ("argon-juge", "gemini-4-argon")
GRAINE_BASE = 2026111300                        # graine de la génération g : GRAINE_BASE + g

# --- gardes de taille de `pole/ideation_v2.py` (commit épinglé), reproduites par calcul -------------------------------------
PRIX_CARACTERE_PRUDENT_USD = 10.0 / 1e6 / 4
PROVISION_SORTIE_PAR_FICHE = 12_000
TAILLE_FICHE_PROVISIONNEE_PASSE = 8_000
RAPPORT_SORTIE_ENTREE = 5
PROVISION_SORTIE_PAR_NOTE = 2_000
ENROBAGE_PAR_FICHE_PASSE_2 = 9
CONTROLE_CLAUDE_ET_BRAS_DEFAUT_USD = 0.2
DEFAUT_EXTERNE_PROPOSEUR_USD = 2.5
DEFAUT_EXTERNE_JUGE_USD = 3.5
DEFAUT_CONTROLE_EXTERNE_USD = 2.5
DEFAUTS_CLAUDE = {"proposeur_ideation|claude-opus-5-5": 5.0, "proposeur_ideation|claude-fable-5-1": 9.3,
                  "juge_ideation|claude-opus-5-5": 4.0, "juge_ideation|claude-fable-5-1": 7.0}
# --- garde avant envoi de `commande_argon_v3d.py` (réglages figés par `appel-argon-v5.sh`), reproduite par calcul ---------
# plafond ≥ ⌈⌈caractères / c⌉ × 1,05⌉ × 8,3e-6 + (4 096 + 8 192) × 41,5e-6 ; gardé à c = 3 (le compte exact de l'interface
# peut dépasser caractères / 4) ; lecture à c = 4 rapportée
ARGON_PRIX_ENTREE = 8.3e-6
ARGON_PRIX_SORTIE = 41.5e-6
ARGON_SORTIE_MIN = 4096
ARGON_PROVISION_PENSEE = 8192
ARGON_MARGE_ENTREE = 1.05
CARACTERES_PAR_JETON_GARDE = 3.0
PORT_RELAIS_CLAUDE = 8787
DOSSIER_SORTIES = Path("/home/user/sorties-course-ideation-bassins-etroits-v3")
SOUS_DOSSIER_RUNS = "course-ideation-bassins-etroits-v3"
SUFFIXE_RUN = "-course-ideation-bassins-etroits-v3-g"
# runs des versions antérieures, lus comme tentatives (même forme de manifestes) : (sous-dossier de runs/, suffixe, version)
ANTERIEURS = (("course-ideation-bassins-etroits-v2", "-course-ideation-bassins-etroits-v2-g",
               "lancer_course_ideation_bassins_etroits_v2"),)
NOM_VERROU = ".verrou-lanceur-bassins-etroits"
MAX_COURSES_PAR_GENERATION = 2
# environnement transmis à l'orchestrateur : liste de noms permis (cause du 401 de la génération 1 : `CLAUDE_CODE_REMOTE*`)
NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")
PYTHON_COURSE = "/usr/local/bin/python3"
NOM_DOSSIER_PYCACHE = "pycache"

DRAPEAUX_INTERDITS = (
    "--accepter-sans-bac-a-sable", "--motif-sans-bac-a-sable",
    "--tolerer-somme-plafonds", "--tolerer-somme-plafonds-claude", "--tolerer-somme-plafonds-externe",
    "--taille-max-consigne-externe", "--taille-max-consigne-externe-bras", "--prix-entree-usd-par-million-jetons",
)
NOMS_DE_CLE = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY", "GOOGLE_API_KEY",
               "GEMINI_API_KEY", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN")
MOTIF_NOM_DE_CLE = re.compile(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)
CHAMPS_INTERNES = ("auteur", "identifiant_auteur", "empreinte", "passe", "temoin", "citations_verifiees")
AUTEUR_TEMOIN = "temoin"

SONDE_BAC_A_SABLE = (
    "import json, sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "from pole.adaptateurs import etat_bac_a_sable_detaille\n"
    "print(json.dumps(etat_bac_a_sable_detaille()))\n"
)

# M7 : superviseur détaché (bibliothèque standard ; lancé sous `-I -B` dans une session de processus neuve). Il lance
# l'orchestrateur, écrit son PID (scellé), relaie SIGTERM, SIGINT et SIGHUP **par PID**, attend, scelle le code de sortie.
SUPERVISEUR = r'''
import datetime, hashlib, json, os, signal, subprocess, sys
argv, cwd, dossier = json.loads(sys.argv[1]), sys.argv[2], sys.argv[3]
def sceller(nom, objet):
    t = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(os.path.join(dossier, nom), "xb") as f:
        f.write(t)
    with open(os.path.join(dossier, nom + ".sha256"), "x", encoding="utf-8") as f:
        f.write(hashlib.sha256(t).hexdigest() + "  " + nom + "\n")
def heure():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
debut = heure()
with open(os.path.join(dossier, "orchestrateur.stdout.txt"), "xb") as fo, \
        open(os.path.join(dossier, "orchestrateur.stderr.txt"), "xb") as fe:
    enfant = subprocess.Popen(argv, cwd=cwd, stdout=fo, stderr=fe, stdin=subprocess.DEVNULL)
    def relayer(num, cadre):
        try:
            enfant.send_signal(num)
        except ProcessLookupError:
            pass
    for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
        signal.signal(s, relayer)
    try:
        with open("/proc/%d/stat" % enfant.pid) as f:
            debut_proc = f.read().rsplit(")", 1)[-1].split()[19]
    except (OSError, IndexError):
        debut_proc = None
    sceller("pid-orchestrateur.json", {"pid_orchestrateur": enfant.pid, "debut_utc": debut, "debut_proc": debut_proc})
    code = enfant.wait()
sceller("code.json", {"code": code, "pid_orchestrateur": enfant.pid, "debut_utc": debut, "fin_utc": heure()})
'''


class Refus(RuntimeError):
    """Garde du lanceur : rien n'est lancé."""


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def date_u() -> str:
    r = subprocess.run(["date", "-u"], capture_output=True, text=True, timeout=10)
    if r.returncode != 0 or not r.stdout.strip():
        raise Refus("`date -u` illisible : horodatage exigé")
    return r.stdout.strip()


@dataclass
class Reglages:
    """Tout ce que le lanceur lit ou écrit. La ligne de commande n'en expose aucun : `production()` seul y sert."""
    depot: Path
    orchestrateur: Path
    commit_orchestrateur: str
    empreintes_orchestrateur: dict
    pieces: dict
    registre_go: Path
    dossier_runs: Path
    dossier_sorties: Path
    depot_attendu_par_l_enveloppe: Path
    python: str
    plafonds: dict = field(default_factory=lambda: dict(PLAFONDS))
    controle_externe_usd: float = CONTROLE_EXTERNE_USD
    passe_2_externe_usd: float = PASSE_2_EXTERNE_USD
    controle_bras_usd: float = CONTROLE_BRAS_USD
    arguments_en_plus: tuple = ()          # vide en production ; les essais y glissent des artefacts
    environnement: Mapping | None = None   # None : os.environ (lu par noms, jamais copié en entier)
    aujourd_hui: _dt.date | None = None
    horodatage: object = date_u
    maintenant: object = None              # callable → datetime UTC (essais) ; None : l'horloge
    anterieurs: tuple = ()                 # ((dossier de runs, suffixe, version), …) des versions antérieures
    prefixe_essais: str | None = None      # essais seulement : noms « FAUX_* » du faux orchestrateur ; None en production

    @classmethod
    def production(cls) -> "Reglages":
        return cls(depot=DEPOT, orchestrateur=ORCHESTRATEUR, commit_orchestrateur=COMMIT_ORCHESTRATEUR,
                   empreintes_orchestrateur=dict(EMPREINTES_ORCHESTRATEUR), pieces=dict(PIECES),
                   registre_go=DEPOT / "registres" / "go.md", dossier_runs=DEPOT / "runs" / SOUS_DOSSIER_RUNS,
                   dossier_sorties=DOSSIER_SORTIES, depot_attendu_par_l_enveloppe=DEPOT_ATTENDU_PAR_L_ENVELOPPE,
                   python=PYTHON_COURSE,
                   anterieurs=tuple((DEPOT / "runs" / d, s, v) for d, s, v in ANTERIEURS))

    def heure(self) -> _dt.datetime:
        return self.maintenant() if self.maintenant else _dt.datetime.now(_dt.timezone.utc)


# ======================================================================================================================
# gardes communes (reprises du v3)
# ======================================================================================================================

def lire_plafond_go(texte: str) -> float:
    m = re.fullmatch(r"\s*(\d+(?:[.,]\d+)?)\s*USD\s*", texte)
    if not m:
        raise Refus(f"plafond du GO illisible : {texte!r} (forme « <nombre> USD » exigée)")
    return float(m.group(1).replace(",", "."))


def _sans_accent(t: str) -> str:
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode("ascii").strip().lower()


def verifier_go(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_ID) -> dict:
    """Une seule ligne principale `go_id`, 8 colonnes, type calcul, accordée par Lazar, dans sa période, non révoquée,
    périmètre « organisme d'idéation » et « bassins », plafond lu ≥ trois courses (60 USD)."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
    trouvees, revocations = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif go_id in ligne:  # m1 : toute autre ligne qui cite ce GO est bien formée, et une révocation l'est quelle que soit
            # la graphie de son type
            if len(cellules) != 8:
                raise Refus(f"ligne {m.group(1)} qui cite {go_id} mal formée ({len(cellules)} colonnes) : lecture impossible")
            if _sans_accent(cellules[2]) == "revocation":
                revocations.append(m.group(1))
    principales = [c for c in trouvees if not (len(c) == 8 and c[3].lower().startswith("extension"))]
    if len(principales) != 1:
        raise Refus(f"{go_id} : {len(principales)} ligne(s) principale(s) dans {registre.name} (une exigée)")
    c = principales[0]
    if len(c) != 8:
        raise Refus(f"{go_id} : ligne mal formée ({len(c)} colonnes, 8 attendues)")
    ident, accorde, typ, perimetre, plafond, echeance, par, ref = c
    if typ != "calcul":
        raise Refus(f"{go_id} : type {typ!r}, « calcul » exigé")
    if par != "Lazar":
        raise Refus(f"{go_id} : accordé par {par!r}, Lazar exigé")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"{go_id} : dates illisibles ({accorde!r}, {echeance!r})") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    p = perimetre.lower()
    if "organisme d'idéation" not in p or "bassins" not in p:
        raise Refus(f"{go_id} : périmètre sans « organisme d'idéation » ni « bassins » — ce n'est pas le GO de ces courses")
    plafond_usd = lire_plafond_go(plafond)
    if plafond_usd < TOTAL_LIGNE_USD:
        raise Refus(f"{go_id} : plafond {plafond_usd} USD sous les trois courses ({TOTAL_LIGNE_USD} USD)")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "plafond": plafond, "plafond_usd": plafond_usd,
            "par": par, "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def verifier_interprete(r: Reglages) -> dict:
    p = Path(r.python)
    if not p.is_absolute():
        raise Refus(f"interpréteur {r.python!r} non absolu : {PYTHON_COURSE} exigé, jamais le `PATH`")
    if not (p.is_file() and os.access(p, os.X_OK)):
        raise Refus(f"interpréteur {r.python} absent ou non exécutable")
    if os.path.abspath(sys.executable) != os.path.abspath(r.python):
        raise Refus(f"lanceur exécuté par {sys.executable}, la course le serait par {r.python} : un seul interpréteur admis")
    return {"chemin": r.python, "resolu": os.path.realpath(r.python), "version": sys.version.split()[0]}


def _git(dossier: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise Refus(f"git {' '.join(args)} dans {dossier} : code {r.returncode} ({r.stderr.strip()[:200]})")
    return r.stdout


def caches_d_octets(racine: Path) -> list:
    trouves = []
    for dossier, sous_dossiers, fichiers in os.walk(racine):
        if ".git" in sous_dossiers:
            sous_dossiers.remove(".git")
        for d in sous_dossiers:
            if d == "__pycache__":
                trouves.append(os.path.join(dossier, d))
        for f in fichiers:
            if f.endswith((".pyc", ".pyo")):
                trouves.append(os.path.join(dossier, f))
    return sorted(trouves)


def verifier_orchestrateur(r: Reglages) -> dict:
    if not (r.orchestrateur / LANCEUR_ORCHESTRATEUR).is_file():
        raise Refus(f"orchestrateur absent : {r.orchestrateur / LANCEUR_ORCHESTRATEUR}")
    tete = _git(r.orchestrateur, "rev-parse", "HEAD").strip()
    if tete != r.commit_orchestrateur:
        raise Refus(f"orchestrateur au commit {tete}, {r.commit_orchestrateur} exigé")
    sale = _git(r.orchestrateur, "status", "--porcelain").strip()
    if sale:
        raise Refus("orchestrateur modifié (git status non vide) : aucune modification admise\n" + sale[:1000])
    ignores = _git(r.orchestrateur, "status", "--porcelain", "--ignored").strip()
    if ignores:
        raise Refus("clone de l'orchestrateur avec fichiers ignorés (git status --porcelain --ignored non vide) : aucun "
                    "admis\n" + ignores[:1000])
    caches = caches_d_octets(r.orchestrateur)
    if caches:
        raise Refus("cache d'octets sous l'orchestrateur (lu à la place des sources empreintées) : " + json.dumps(caches[:20]))
    ecarts = {}
    for rel, attendu in sorted(r.empreintes_orchestrateur.items()):
        p = r.orchestrateur / rel
        lu = sha256_fichier(p) if p.is_file() else None
        if lu != attendu:
            ecarts[rel] = lu
    if ecarts:
        raise Refus(f"orchestrateur : empreintes différentes ou fichiers absents : {ecarts}")
    racine_clone = Path(_git(r.orchestrateur, "rev-parse", "--show-toplevel").strip())
    return {"chemin": str(r.orchestrateur), "racine_clone": str(racine_clone), "commit": tete,
            "empreintes": dict(r.empreintes_orchestrateur), "fichiers_ignores": [], "caches_d_octets": []}


def options_interprete(prefixe_pycache: Path) -> list:
    return ["-I", "-B", "-X", f"pycache_prefix={prefixe_pycache}"]


def verifier_prefixe_pycache(prefixe: Path, racine_clone: Path) -> None:
    if not prefixe.is_absolute():
        raise Refus(f"préfixe du cache d'octets non absolu : {prefixe}")
    if prefixe.exists():
        raise Refus(f"préfixe du cache d'octets déjà présent : {prefixe} (un dossier neuf est exigé)")
    p, c = Path(os.path.realpath(prefixe)), Path(os.path.realpath(racine_clone))
    if p == c or c in p.parents:
        raise Refus(f"préfixe du cache d'octets {prefixe} dans le clone {racine_clone}")


def verifier_pieces(r: Reglages) -> dict:
    if r.depot.resolve() != r.depot_attendu_par_l_enveloppe.resolve():
        raise Refus(f"dépôt de travail en {r.depot}, l'enveloppe d'Argon v5 attend {r.depot_attendu_par_l_enveloppe}")
    lues, ecarts = {}, {}
    for nom, (rel, attendu) in sorted(r.pieces.items()):
        p = r.depot / rel
        lu = sha256_fichier(p) if p.is_file() and not p.is_symlink() else None
        if lu != attendu:
            ecarts[nom] = {"chemin": rel, "attendu": attendu, "lu": lu}
        lues[nom] = {"chemin": rel, "sha256": attendu}
    if ecarts:
        raise Refus("pièces absentes ou d'empreinte différente (R11 : vérifiées sur disque et par empreinte) : "
                    + json.dumps(ecarts, ensure_ascii=False))
    return lues


def lire_scelle(chemin: Path) -> bytes:
    """Octets d'un fichier scellé (compagnon `.sha256` au format de `sha256sum`, bon nom, même empreinte) ; refus sinon."""
    comp = Path(str(chemin) + ".sha256")
    if not chemin.is_file() or chemin.is_symlink():
        raise Refus(f"fichier scellé absent ou lien symbolique : {chemin}")
    try:
        champs = comp.read_text(encoding="utf-8").split()
    except OSError:
        raise Refus(f"compagnon d'empreinte absent : {comp}") from None
    if len(champs) != 2 or champs[1] != chemin.name or not re.fullmatch(r"[0-9a-f]{64}", champs[0]):
        raise Refus(f"compagnon d'empreinte mal formé : {comp}")
    octets = chemin.read_bytes()
    if hashlib.sha256(octets).hexdigest() != champs[0]:
        raise Refus(f"sceau faux : {chemin} (empreinte différente de son compagnon)")
    return octets


def lire_json_scelle(chemin: Path):
    try:
        return json.loads(lire_scelle(chemin).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise Refus(f"JSON scellé illisible : {chemin}") from None


def _usd(x: float) -> str:
    return repr(float(x))


def garde_drapeaux(argv: list) -> None:
    trouves = []
    for jeton in argv:
        if not isinstance(jeton, str) or not jeton.startswith("--") or len(jeton) <= 2:
            continue
        nom = jeton.split("=", 1)[0]
        if any(f == nom or f.startswith(nom) for f in DRAPEAUX_INTERDITS):
            trouves.append(jeton)
    if trouves:
        raise Refus(f"drapeau(x) interdit(s) dans la commande : {trouves} (contournement du bac à sable, tolérance de somme "
                    "ou relèvement d'une garde de taille : jamais dans ce lanceur)")


def _valeurs(argv: list, option: str) -> list:
    out = []
    for i, jeton in enumerate(argv):
        if jeton == option and i + 1 < len(argv):
            out.append(argv[i + 1])
        elif isinstance(jeton, str) and jeton.startswith(option + "="):
            out.append(jeton.split("=", 1)[1])
    return out


def _une(argv: list, option: str, defaut):
    v = _valeurs(argv, option)
    if len(v) > 1:
        raise Refus(f"{option} donné {len(v)} fois")
    return float(v[0]) if v else defaut


def sommes_plafonds(argv: list) -> dict:
    """Les deux sommes, comme l'orchestrateur les calcule avant tout appel (`verifier_reglages`), défauts compris."""
    budgets = dict(DEFAUTS_CLAUDE)
    prop = [v.split("=", 1)[1] for v in _valeurs(argv, "--proposeur")]
    juges = [v.split("=", 1)[1] for v in _valeurs(argv, "--juge")]
    prop_ext = [v.split("=", 1)[1] for v in _valeurs(argv, "--proposeur-externe")]
    juges_ext = [v.split("=", 1)[1] for v in _valeurs(argv, "--juge-externe")]
    for m in juges_ext:
        budgets.setdefault(f"juge_ideation|{m}", DEFAUT_EXTERNE_JUGE_USD)
    for m in prop_ext:
        budgets.setdefault(f"proposeur_ideation|{m}", DEFAUT_EXTERNE_PROPOSEUR_USD)
    for v in _valeurs(argv, "--budget"):
        cle, valeur = v.split("=", 1)
        role, modele = cle.split("|", 1)
        budgets[f"{role.strip()}|{modele.strip()}"] = float(valeur)
    passes = 2 if "--seconde-passe" in argv else 1
    controle = _une(argv, "--budget-controle-usd", CONTROLE_CLAUDE_ET_BRAS_DEFAUT_USD)
    controle_ext = _une(argv, "--budget-controle-externe-usd", DEFAUT_CONTROLE_EXTERNE_USD)
    passe_2 = _une(argv, "--budget-passe-2-externe-usd", None)
    total_claude = _une(argv, "--budget-total-usd", 40.0)
    total_externe = _une(argv, "--budget-externe-usd", 11.6)
    modeles_claude = sorted(set(prop) | set(juges))
    somme_claude = controle * len(modeles_claude) + passes * sum(budgets[f"proposeur_ideation|{m}"] for m in prop) \
        + sum(budgets[f"juge_ideation|{m}"] for m in juges)
    somme_externe = controle_ext * len(prop_ext) \
        + sum((passe_2 if (n == 2 and passe_2 is not None) else budgets[f"proposeur_ideation|{m}"])
              for m in prop_ext for n in range(1, passes + 1)) \
        + sum(budgets[f"juge_ideation|{m}"] for m in juges_ext) + controle * len(juges_ext)
    return {"somme_claude": round(somme_claude, 6), "total_claude": total_claude,
            "somme_externe": round(somme_externe, 6), "total_externe": total_externe,
            "detail_externe": {"controle_externe": controle_ext, "passes": passes, "passe_2": passe_2,
                               "proposeurs_externes": {m: budgets[f"proposeur_ideation|{m}"] for m in prop_ext},
                               "juges_externes": {m: budgets[f"juge_ideation|{m}"] for m in juges_ext},
                               "controle_du_bras_compte_par_la_course": controle},
            "detail_claude": {"controle": controle, "modeles": modeles_claude}}


def garde_sommes(argv: list) -> dict:
    s = sommes_plafonds(argv)
    if s["total_externe"] != TOTAL_EXTERNE_USD or s["total_claude"] != TOTAL_CLAUDE_USD:
        raise Refus(f"totaux {s['total_claude']} + {s['total_externe']} ≠ {TOTAL_CLAUDE_USD} + {TOTAL_EXTERNE_USD} du GO")
    if not s["somme_externe"] < s["total_externe"]:
        raise Refus(f"somme des plafonds externes {s['somme_externe']:.2f} pas sous le total externe {s['total_externe']}")
    if s["somme_claude"] > s["total_claude"]:
        raise Refus(f"somme des plafonds Claude {s['somme_claude']:.2f} > total Claude {s['total_claude']}")
    # au bras, l'orchestrateur exige : dépense externe de la course + juge + contrôle du bras ≤ total externe ; au pire cas
    # de la course (contrôle externe + deux passes à leurs plafonds), le bras doit encore tenir
    d = s["detail_externe"]
    pire_course_externe = d["controle_externe"] + sum(d["proposeurs_externes"].values()) + (d["passe_2"] or 0.0)
    pire_avec_bras = pire_course_externe + PLAFONDS["juge_ideation|gemini-4-argon"] + CONTROLE_BRAS_USD
    s["externe_pire_course_plus_bras"] = round(pire_avec_bras, 6)
    if pire_avec_bras > TOTAL_EXTERNE_USD + 1e-9:
        raise Refus(f"au pire cas, course externe {pire_course_externe:.2f} + bras {PLAFOND_BRAS_USD:.2f} > "
                    f"{TOTAL_EXTERNE_USD} : le bras serait refusé par l'orchestrateur")
    return s


def taille_max(plafond_usd: float, provision: int = 0, prix: float = PRIX_CARACTERE_PRUDENT_USD) -> int:
    """`taille_max_consigne_par_defaut` de l'orchestrateur, recalculée (aucun import)."""
    return max(0, int(float(plafond_usd) / prix + 1e-6) - int(provision))


def plancher_argon(caracteres: int, caracteres_par_jeton: float = 4.0) -> float:
    """Plafond de session minimal pour que `commande_argon_v3d.py` envoie une consigne de `caracteres` (garde avant envoi,
    réglages de `appel-argon-v5.sh`, recherche sur le Web absente)."""
    entree = math.ceil(math.ceil(caracteres / caracteres_par_jeton) * ARGON_MARGE_ENTREE)
    return entree * ARGON_PRIX_ENTREE + (ARGON_SORTIE_MIN + ARGON_PROVISION_PENSEE) * ARGON_PRIX_SORTIE


def gardes_de_taille(mesure: dict, r: Reglages) -> dict:
    """Sur la mesure de l'orchestrateur (`--mesurer-consignes`, sans appel) : gardes de l'orchestrateur (course, passe 1,
    lues et recalculées), garde avant envoi de la commande d'Argon (contrôle, passe 1, passe 2 aux fiches de 8 000), seuil
    de fiche de la passe 2 et juge d'Argon rapportés. Refus si une garde ne tient pas."""
    try:
        c = mesure["consignes"]
        controle, passe_1 = int(c["consigne_de_controle_externe"]), int(c["consigne_passe_1"])
        nombre, fiches_juge = int(c["nombre_par_proposeur"]), int(c["fiches_au_juge_au_maximum"])
        juge_max = int(c["consigne_du_juge_maximale"])
        course_orch = bool(mesure["garde_course"]["passerait"])
        passe_1_orch = bool(mesure["gardes_passes_externes"]["argon"]["passe_1"]["passerait"])
    except (KeyError, TypeError, ValueError):
        raise Refus("mesure des consignes illisible : tailles ou gardes absentes") from None
    if mesure.get("prix_entree_usd_par_million_jetons") != 10.0 or nombre != NOMBRE:
        raise Refus("mesure des consignes à un autre prix que le prix prudent (10) ou à un autre --nombre")
    p1, p2, ctrl = r.plafonds["proposeur_ideation|gemini-4-argon"], r.passe_2_externe_usd, r.controle_externe_usd
    juge = r.plafonds["juge_ideation|gemini-4-argon"]
    prov_course = nombre * PROVISION_SORTIE_PAR_FICHE * RAPPORT_SORTIE_ENTREE
    prov_passe = nombre * TAILLE_FICHE_PROVISIONNEE_PASSE * RAPPORT_SORTIE_ENTREE
    consigne_p2_8000 = passe_1 + nombre * (TAILLE_FICHE_PROVISIONNEE_PASSE + ENROBAGE_PAR_FICHE_PASSE_2)
    g = {
        "course": {"taille_max": min(taille_max(ctrl), taille_max(p2, prov_course)), "consigne": controle,
                   "orchestrateur_passerait": course_orch},
        "passe_1": {"taille_max": taille_max(p1, prov_passe), "consigne": passe_1, "orchestrateur_passerait": passe_1_orch},
        "passe_2_fiches_8000": {"taille_max": taille_max(p2, prov_passe), "consigne": consigne_p2_8000},
    }
    for v in g.values():
        v["marge"] = v["taille_max"] - v["consigne"]
    argon = {
        "controle_externe": {"plafond": ctrl, "consigne": controle},
        "passe_1": {"plafond": p1, "consigne": passe_1},
        "passe_2_fiches_8000": {"plafond": p2, "consigne": consigne_p2_8000},
    }
    for v in argon.values():
        v["plancher_garde_a_3_caracteres_par_jeton"] = round(plancher_argon(v["consigne"], CARACTERES_PAR_JETON_GARDE), 6)
        v["plancher_a_4_caracteres_par_jeton_rapporte"] = round(plancher_argon(v["consigne"], 4.0), 6)
        v["tient"] = v["plafond"] >= v["plancher_garde_a_3_caracteres_par_jeton"]
    g["commande_argon"] = argon
    trop = {n: v for n, v in g.items() if n != "commande_argon" and (v["marge"] < 0 or v.get("orchestrateur_passerait") is False)}
    trop.update({f"commande_argon/{n}": v for n, v in argon.items() if not v["tient"]})
    if trop:
        raise Refus("garde(s) de taille qui ne tiendrai(en)t pas — refus avant tout appel : " + json.dumps(trop, ensure_ascii=False))
    g["passe_2_seuil_de_fiche"] = {
        "fiche_de_passe_1_la_plus_longue_admise": (taille_max(p2) - passe_1 - ENROBAGE_PAR_FICHE_PASSE_2 * nombre)
        // (nombre * (1 + RAPPORT_SORTIE_ENTREE)),
        "au_dela": "refus de l'orchestrateur avant l'envoi de la passe 2 d'Argon ; course arrêtée",
        "garde": "rapporté, non gardé ici : dépend des fiches réelles"}
    t_juge = taille_max(juge, fiches_juge * PROVISION_SORTIE_PAR_NOTE * RAPPORT_SORTIE_ENTREE)
    g["juge_argon_rapporte"] = {"taille_max_au_maximum_de_fiches": t_juge, "consigne_du_juge_maximale": juge_max,
                                "lecture": ("passerait au maximum théorique" if t_juge >= juge_max else
                                            "ne passerait pas au maximum théorique ; gardé au bras sur la taille réelle"),
                                "garde": "au bras, sur la consigne en attente réelle (garder_bras)"}
    return g


def environnement_permis(env: Mapping, prefixe_pycache: Path | None = None, home: Path | None = None,
                         prefixe_essais: str | None = None) -> tuple:
    """(environnement transmis, description par noms). Liste de noms permis (`NOMS_PERMIS`) ; HOME, GO_ID et
    PYTHONPYCACHEPREFIX fixés par le lanceur ; tout autre nom est exclu, valeur jamais lue. Un nom de clé dans la liste
    permise serait une faute de ce fichier : refus."""
    for n in NOMS_PERMIS:
        if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n) or n.startswith(("ANTHROPIC", "CLAUDE", "CCR")):
            raise Refus(f"nom permis interdit : {n}")
    if prefixe_essais is not None and prefixe_essais != "FAUX_":
        raise Refus(f"préfixe d'essai interdit : {prefixe_essais!r}")
    garde = {n: env[n] for n in env if n in NOMS_PERMIS or (prefixe_essais and n.startswith(prefixe_essais))}
    exclus = sorted(n for n in env if n not in garde)
    garde["GO_ID"] = GO_ID
    if home is not None:
        garde["HOME"] = str(home)
    if prefixe_pycache is not None:
        garde["PYTHONPYCACHEPREFIX"] = str(prefixe_pycache)
    return garde, {"noms_transmis": sorted(garde), "noms_fixes_par_le_lanceur": sorted(
        n for n in ("GO_ID", "HOME", "PYTHONPYCACHEPREFIX") if n in garde), "noms_exclus": exclus,
        "valeurs": "aucune valeur écrite ; transmis par liste de noms permis"}


def sonder_bac_a_sable(r: Reglages, env: dict, prefixe_pycache: Path) -> dict:
    """La sonde de l'orchestrateur, telle quelle, dans un processus à part ; `actif` et `proc_neuf` exigés vrais."""
    try:
        p = subprocess.run([r.python, *options_interprete(prefixe_pycache), "-c", SONDE_BAC_A_SABLE, str(r.orchestrateur)],
                           cwd=str(r.orchestrateur), env=env, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"sonde du bac à sable : non exécutée ({type(e).__name__})") from None
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    try:
        etat = json.loads(lignes[-1]) if p.returncode == 0 and lignes else None
    except json.JSONDecodeError:
        etat = None
    if not (isinstance(etat, dict) and isinstance(etat.get("actif"), bool) and isinstance(etat.get("proc_neuf"), bool)):
        raise Refus(f"sonde du bac à sable illisible (code {p.returncode}) : {p.stderr.strip()[-500:]!r}")
    if not etat["actif"]:
        raise Refus("bac à sable de l'orchestrateur inactif : " + str(etat.get("motif")))
    if not etat["proc_neuf"]:
        raise Refus("bac à sable sans /proc neuf : " + str(etat.get("motif")))
    return etat


def ecrire_scelle(chemin: Path, contenu: dict) -> str:
    if chemin.exists():
        raise Refus(f"{chemin} existe déjà (R12 : jamais écrasé)")
    donnees = (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


def sceller_existant(chemin: Path) -> str:
    """Compagnon `.sha256` d'un fichier écrit par l'orchestrateur (liste blanche), sans le réécrire."""
    h = sha256_fichier(chemin)
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


def _depot_git(r: Reglages) -> dict:
    try:
        return {"commit": _git(r.depot, "rev-parse", "HEAD").strip(),
                "arbre_modifie": bool(_git(r.depot, "status", "--porcelain", "--untracked-files=no").strip())}
    except Refus as e:
        return {"commit": None, "erreur": str(e)}


# ======================================================================================================================
# état des générations, dépense relevée, garde de cumul
# ======================================================================================================================


# ======================================================================================================================
# processus détachés (M7)
# ======================================================================================================================

def debut_processus(pid: int) -> str | None:
    """Heure de départ du processus (champ 22 de /proc/<pid>/stat), None s'il n'existe pas ou est un zombie."""
    try:
        with open(f"/proc/{int(pid)}/stat", "r", encoding="utf-8", errors="replace") as f:
            stat = f.read()
    except OSError:
        return None
    champs = stat.rsplit(")", 1)[-1].split()
    if len(champs) < 20 or champs[0] == "Z":
        return None
    return champs[19]


def superviseur_vivant(sup: dict | None) -> bool:
    return bool(sup) and debut_processus(sup["pid"]) is not None and debut_processus(sup["pid"]) == sup["debut_proc"]


def lancer_detache(r: Reglages, argv: list, env: dict, dossier: Path, prefixe_pycache: Path) -> dict:
    """Le superviseur, dans une session de processus neuve, sorties vers des fichiers ; rend {pid, debut_proc, dossier}."""
    dossier.mkdir()
    with open(dossier / "superviseur.stdout.txt", "xb") as fo, open(dossier / "superviseur.stderr.txt", "xb") as fe:
        p = subprocess.Popen([r.python, *options_interprete(prefixe_pycache), "-c", SUPERVISEUR, json.dumps(argv),
                              str(r.orchestrateur), str(dossier)], cwd=str(r.orchestrateur), env=env, stdout=fo, stderr=fe,
                             stdin=subprocess.DEVNULL, start_new_session=True)
    return {"pid": p.pid, "debut_proc": debut_processus(p.pid), "dossier": str(dossier),
            "arret": f"kill -TERM {p.pid} (relayé par PID à l'orchestrateur ; jamais par motif, R10)"}


def lire_code(sup: dict) -> dict | None:
    return _lire_json_si_scelle(Path(sup["dossier"]) / "code.json")


# ======================================================================================================================
# état des runs, dépense relevée, garde de cumul
# ======================================================================================================================

def _lire_json_si_scelle(chemin: Path):
    try:
        return lire_json_scelle(chemin)
    except Refus:
        return None


def _scelle_present(chemin: Path) -> bool:
    return chemin.exists() or Path(str(chemin) + ".sha256").exists()


def runs_du_lanceur(r: Reglages) -> list:
    """Les runs de ce lanceur et des versions antérieures (`r.anterieurs`), dans l'ordre du temps. Un dossier sans
    manifeste de départ ni de refus scellé est une incohérence : refus."""
    runs = []
    for dossier, suffixe, version in tuple(r.anterieurs) + ((r.dossier_runs, SUFFIXE_RUN, VERSION),):
        runs += _runs_de(Path(dossier), suffixe, version)
    return sorted(runs, key=lambda x: x["nom"])


def _runs_de(dossier_runs: Path, suffixe: str, version: str) -> list:
    if not dossier_runs.is_dir():
        return []
    runs = []
    for nom in sorted(os.listdir(dossier_runs)):
        m = re.fullmatch(r"\d{8}-\d{6}" + re.escape(suffixe) + r"([123])", nom)
        if not m:
            raise Refus(f"dossier inattendu dans {dossier_runs} : {nom!r}")
        d = dossier_runs / nom
        depart = _lire_json_si_scelle(d / "manifeste-lanceur-depart.json")
        refus = _lire_json_si_scelle(d / "manifeste-lanceur-refus.json")
        if depart is None and refus is None:
            raise Refus(f"run {nom} sans manifeste de départ ni de refus scellé : état inconnu, aucun lancement")
        base = depart or refus
        if str(base.get("generation")) != m.group(1) or base.get("lanceur", {}).get("version") != version:
            raise Refus(f"run {nom} : génération ou version du lanceur incohérente")
        if depart is not None and not depart.get("superviseur"):
            raise Refus(f"run {nom} : manifeste de départ sans superviseur")
        fin = _lire_json_si_scelle(d / "manifeste-lanceur-fin.json")
        if fin is None and _scelle_present(d / "manifeste-lanceur-fin.json"):
            raise Refus(f"run {nom} : manifeste de fin au sceau faux")
        bras = []
        k = 1
        while _scelle_present(d / f"manifeste-lanceur-bras-depart-{k}.json"):
            dep_b = _lire_json_si_scelle(d / f"manifeste-lanceur-bras-depart-{k}.json")
            if dep_b is None or not dep_b.get("superviseur"):
                raise Refus(f"run {nom} : manifeste de départ du bras {k} illisible")
            fin_b = _lire_json_si_scelle(d / f"manifeste-lanceur-bras-fin-{k}.json")
            if fin_b is None and _scelle_present(d / f"manifeste-lanceur-bras-fin-{k}.json"):
                raise Refus(f"run {nom} : manifeste de fin du bras {k} au sceau faux")
            bras.append({"numero": k, "depart": dep_b, "fin": fin_b})
            k += 1
        runs.append({"nom": nom, "dossier": d, "generation": int(m.group(1)), "version": version, "depart": depart,
                     "refus": refus, "fin": fin,
                     "bras": bras, "sortie": Path(base["sortie"]) if base.get("sortie") else None})
    return runs


def processus_de(run: dict) -> list:
    """[(quoi, superviseur, manifeste de fin)] de la course et des bras d'un run lancé."""
    if run["depart"] is None:
        return []
    return [("course", run["depart"]["superviseur"], run["fin"])] + \
        [(f"bras-{b['numero']}", b["depart"]["superviseur"], b["fin"]) for b in run["bras"]]


def _cout(objet, *cles) -> float:
    for c in cles:
        objet = objet[c]
    if isinstance(objet, bool) or not isinstance(objet, (int, float)) or not math.isfinite(objet) or objet < 0:
        raise ValueError("coût non fini ou négatif")
    return float(objet)


def depense_course(sortie: Path, sup_fini: bool) -> tuple:
    """(dépense en USD, lisible, lecture). Aucun chemin ne rend 0 par défaut (M1) : 0 seulement si le superviseur a fini proprement
    et que rien n'est parti ; une sortie sans manifeste de fin scellé et lisible, un dossier de contrôle non expliqué en
    entier par des tentatives scellées, un processus mort sans fin propre comptent le plafond entier."""
    if not sup_fini:
        return PLAFOND_COURSE_USD, False, "processus mort sans fin propre, ou en marche : plafond entier compté"
    controle = Path(str(sortie) + "-controle")
    fin = sortie / "manifeste-fin.json"
    if _scelle_present(fin):
        m = _lire_json_si_scelle(fin)
        try:
            j = m["reglages"]["journal"]
            return _cout(j, "cout_total_usd") + _cout(j, "cout_externe_usd"), True, "manifeste de fin de l'orchestrateur"
        except (TypeError, KeyError, ValueError):
            return PLAFOND_COURSE_USD, False, "manifeste de fin illisible : plafond entier compté"
    if sortie.exists():
        return PLAFOND_COURSE_USD, False, "sortie sans manifeste de fin scellé : plafond entier compté"
    if not controle.exists():
        return 0.0, True, "rien parti (fin propre du superviseur ; ni sortie, ni contrôle)"
    total, scellees = 0.0, set()
    noms = sorted(os.listdir(controle))
    for nom in noms:
        p = controle / nom
        if re.fullmatch(r"tentative-\d+\.json", nom):
            m = _lire_json_si_scelle(p)
            try:
                total += _cout(m, "reglages", "cout_claude_usd") + _cout(m, "reglages", "cout_externe_usd")
            except (TypeError, KeyError, ValueError):
                return PLAFOND_COURSE_USD, False, f"tentative de contrôle illisible ({nom}) : plafond entier compté"
            scellees.add(nom.split(".")[0])
        elif re.fullmatch(r"refus-taille-\d+\.json", nom):
            if _lire_json_si_scelle(p) is None:
                return PLAFOND_COURSE_USD, False, f"refus de taille au sceau faux ({nom}) : plafond entier compté"
        elif nom.endswith(".sha256") or re.fullmatch(r"tentative-\d+(-externe-[a-z0-9-]+)?", nom):
            continue
        else:
            return PLAFOND_COURSE_USD, False, f"fichier de contrôle inattendu ({nom}) : plafond entier compté"
    for nom in noms:
        m = re.fullmatch(r"(tentative-\d+)(-externe-[a-z0-9-]+)?", nom)
        if m and (controle / nom).is_dir() and m.group(1) not in scellees:
            return PLAFOND_COURSE_USD, False, f"contrôle {nom} sans tentative scellée : plafond entier compté"
    return total, True, "tentatives de contrôle scellées (course non partie)"


def traces_bras(sortie: Path) -> dict:
    """Ce que l'orchestrateur a écrit des bras de cette sortie (même joués hors du lanceur, m2)."""
    t = {"rapporte": None, "payees": [], "non_jouees": 0, "refus_taille": 0, "illisibles": []}
    if not sortie or not sortie.is_dir():
        return t
    if _scelle_present(sortie / "manifeste-bras-rapporte.json"):
        t["rapporte"] = _lire_json_si_scelle(sortie / "manifeste-bras-rapporte.json") or "illisible"
    for nom in sorted(os.listdir(sortie)):
        if re.fullmatch(r"bras-tentative-\d+\.json", nom):
            t["payees"].append(_lire_json_si_scelle(sortie / nom) or "illisible")
        elif re.fullmatch(r"manifeste-bras-non-joue-\d+\.json", nom):
            t["non_jouees"] += 1
        elif re.fullmatch(r"manifeste-bras-refus-taille-\d+\.json", nom):
            t["refus_taille"] += 1
    return t


def depense_bras(run: dict) -> tuple:
    t = traces_bras(run["sortie"])
    total, lectures = 0.0, []
    for objet, nom in ([(t["rapporte"], "manifeste du bras")] if t["rapporte"] else []) + \
            [(x, "tentative payée du bras") for x in t["payees"]]:
        try:
            total += _cout(objet, "reglages", "journal", "cout_total_usd")
            lectures.append(nom)
        except (TypeError, KeyError, ValueError):
            total += PLAFOND_BRAS_USD
            lectures.append(f"{nom} illisible : plafond du bras compté")
    expliques = (1 if t["rapporte"] else 0) + len(t["payees"]) + t["non_jouees"] + t["refus_taille"]
    morts = [b for b in run["bras"] if not superviseur_vivant(b["depart"]["superviseur"])
             and lire_code(b["depart"]["superviseur"]) is None]
    vivants = [b for b in run["bras"] if superviseur_vivant(b["depart"]["superviseur"])]
    manquants = max(len(morts) + len(vivants), len(run["bras"]) - expliques)
    if manquants:
        total += manquants * PLAFOND_BRAS_USD
        lectures.append(f"{manquants} bras sans fin propre ou sans trace : plafond du bras compté pour chacun")
    return total, "; ".join(lectures) or "aucun bras"


def depense_run(run: dict) -> dict:
    if run["depart"] is None:  # refus du lanceur avant tout départ : aucun processus lancé
        return {"run": run["nom"], "course_usd": 0.0, "bras_usd": 0.0, "course_lisible": True,
                "lecture": "refus du lanceur avant tout départ"}
    sup = run["depart"]["superviseur"]
    c, lisible, lc_ = depense_course(run["sortie"], (not superviseur_vivant(sup)) and lire_code(sup) is not None)
    b, lb = depense_bras(run)
    return {"run": run["nom"], "course_usd": round(c, 6), "bras_usd": round(b, 6), "course_lisible": lisible,
            "lecture": f"course : {lc_} ; bras : {lb}"}


def garde_cumul(runs: list, plafond_suivant: float, plafond_go: float) -> dict:
    lignes = [depense_run(x) for x in runs]
    deja = round(sum(x["course_usd"] + x["bras_usd"] for x in lignes), 6)
    borne = min(TOTAL_LIGNE_USD, plafond_go)
    if deja + plafond_suivant > borne + 1e-9:
        raise Refus(f"garde de cumul : dépense relevée {deja:.4f} + plafond suivant {plafond_suivant} > {borne} USD "
                    f"({GO_ID}) ; détail : {json.dumps(lignes, ensure_ascii=False)}")
    return {"depense_relevee_usd": deja, "plafond_suivant_usd": plafond_suivant, "borne_usd": borne, "par_run": lignes}


def course_reussie(run: dict) -> bool:
    if not (run["fin"] and run["fin"].get("code") == 0 and run["sortie"]):
        return False
    m = _lire_json_si_scelle(run["sortie"] / "manifeste-fin.json")
    try:
        return bool(m["reglages"]["en_attente_bras"]) and m["reglages"]["statut_course"]["statut"] == "ok"
    except (TypeError, KeyError):
        return False


def bras_reussi(run: dict) -> bool:
    if not run["bras"]:
        return False
    der = run["bras"][-1]["fin"]
    if not (der and der.get("code") == 0):
        return False
    c = _lire_json_si_scelle(run["sortie"] / "classement.json")
    return bool(isinstance(c, dict) and c.get("lisible_L2_L4") is True
                and _lire_json_si_scelle(run["sortie"] / "manifeste-bras-rapporte.json") is not None)


def bras_relancable(run: dict) -> tuple:
    """M3 : un bras ne se relance que si chaque tentative précédente a fini proprement en « non joué, rien envoyé »."""
    t = traces_bras(run["sortie"])
    if t["rapporte"] or t["payees"] or t["refus_taille"]:
        return False, "bras joué, payé ou refusé pour taille (non relançable) : aucune relance après dépense"
    if any(lire_code(b["depart"]["superviseur"]) is None for b in run["bras"]):
        return False, "un bras sans fin propre : état inconnu"
    if t["non_jouees"] < len(run["bras"]):
        return False, "un bras sans trace « non joué » de l'orchestrateur"
    if len(run["bras"]) >= MAX_TENTATIVES:
        return False, f"{MAX_TENTATIVES} bras déjà tentés"
    return True, "bras précédents non joués, rien envoyé"


def derniere_attestation(r: Reglages, g: int) -> Path:
    d = r.depot / ATTESTATIONS
    versions = []
    if d.is_dir():
        for nom in os.listdir(d):
            m = re.fullmatch(MOTIF_ATTESTATION.format(g=g), nom)
            if m:
                versions.append((int(m.group(1)), d / nom))
    if not versions:
        raise Refus(f"attestation de lecture de la génération {g} absente ({ATTESTATIONS}/"
                    f"attestation-lecture-humaine-g{g}-v<N>.json)")
    return max(versions)[1]


def lire_attestation(r: Reglages, g: int, sortie: Path) -> tuple:
    """M6 : qui (`lecteur`, non vide), quoi (empreintes des fiches validées et de la consigne en attente du juge, égales à
    celles de la course), quand (`lu_le`), et, pour la génération suivante, `temoin_vrai_absent_des_fiches_validees` (M9)."""
    chemin = derniere_attestation(r, g)
    a = lire_json_scelle(chemin)
    if not isinstance(a, dict) or not all(isinstance(a.get(k), str) and a[k].strip() for k in ("lecteur", "lu_le")) \
            or not isinstance(a.get("consignes_en_attente_sha256"), dict) \
            or not isinstance(a.get("temoin_vrai_absent_des_fiches_validees"), bool):
        raise Refus(f"attestation de la génération {g} mal formée : {chemin.name} (lecteur, lu_le, fiches_validees_sha256, "
                    "consignes_en_attente_sha256, temoin_vrai_absent_des_fiches_validees exigés)")
    if a.get("fiches_validees_sha256") != sha256_fichier(sortie / "fiches-validees.json"):
        raise Refus(f"l'attestation de la génération {g} ne porte pas l'empreinte des fiches validées de sa course")
    lc_ = lire_json_scelle(sortie / "lecture-course.json")
    attendues = {b["etiquette"]: b["consigne_en_attente_sha256"] for b in lc_.get("bras_rapporte_differe", [])}
    if JUGE_EXTERNE[0] not in attendues or a["consignes_en_attente_sha256"].get(JUGE_EXTERNE[0]) != attendues[JUGE_EXTERNE[0]]:
        raise Refus(f"l'attestation de la génération {g} ne porte pas l'empreinte de la consigne en attente de "
                    f"{JUGE_EXTERNE[0]}")
    return chemin, sha256_fichier(chemin), a


def fiches_produites(sortie: Path):
    """False si aucune fiche n'a été produite (sortie absente, ou les trois listes de fiches scellées et vides) ; True si
    une fiche existe ; None si on ne peut pas le prouver (tenu pour « produites »)."""
    if sortie is None or not sortie.exists():
        return False
    listes = [_lire_json_si_scelle(sortie / n) for n in ("fiches-validees.json", "fiches-refusees.json",
                                                        "fiches-en-quarantaine.json")]
    if any(not isinstance(x, list) for x in listes):
        return None
    return any(listes)


def relance_permise(runs_g: list) -> tuple:
    """Règle étroite : une génération se relance **une fois** si chaque course précédente a fini proprement (code scellé,
    manifeste de fin du lanceur), n'a produit aucune fiche, a une dépense relevée lisible (comptée au cumul) et n'a aucun
    bras ; deux courses par génération au plus."""
    parties = [x for x in runs_g if x["depart"] is not None]
    for x in parties:
        if x["fin"] is None or x["fin"].get("code") is None:
            return False, f"tentative {x['nom']} sans fin propre (code non scellé)"
        if x["bras"]:
            return False, f"tentative {x['nom']} a un bras"
        dep = depense_run(x)
        if not dep["course_lisible"]:
            return False, f"tentative {x['nom']} : dépense illisible ({dep['lecture']})"
        fp = fiches_produites(x["sortie"])
        if fp is not False:
            return False, f"tentative {x['nom']} : {'fiches produites' if fp else 'production de fiches non prouvée nulle'}"
    if len(parties) >= MAX_COURSES_PAR_GENERATION:
        return False, f"{MAX_COURSES_PAR_GENERATION} courses déjà parties pour cette génération"
    return True, f"{len(parties)} course(s) précédente(s), finies proprement, sans fiche, dépense lisible"


def etat_generation(r: Reglages, runs: list, g: int) -> dict:
    """Le temps à jouer pour la génération g : « course » ou « bras » (avec le run), ou refus."""
    du_g = [x for x in runs if x["generation"] == g]
    if any(bras_reussi(x) for x in du_g):
        raise Refus(f"génération {g} déjà jouée (course et bras réussis) : jamais rejouée")
    reussies = [x for x in du_g if course_reussie(x)]
    if len(reussies) > 1:
        raise Refus(f"génération {g} : {len(reussies)} courses réussies (une au plus) : nœud pour la mère")
    if reussies:
        run = reussies[0]
        if run["bras"]:
            ok, motif = bras_relancable(run)
            if not ok:
                raise Refus(f"génération {g} verrouillée ({run['nom']}) : {motif} ; nœud pour la mère ou Lazar")
        return {"temps": "bras", "run": run}
    ok, motif = relance_permise(du_g)
    if not ok:
        raise Refus(f"génération {g} verrouillée : {motif} ; aucune autre relance (R3) ; nœud pour la mère")
    if g == 1:
        return {"temps": "course", "precedente": None, "relance": motif}
    prec = [x for x in runs if x["generation"] == g - 1 and bras_reussi(x)]
    if len(prec) != 1:
        raise Refus(f"génération {g} refusée : la génération {g - 1} n'a pas une course et un bras réussis, manifestes de "
                    "fin scellés et classement lisible")
    conf = r.depot / CONFIRMATION_REGLE
    if not lire_scelle(conf).decode("utf-8", errors="replace").strip():
        raise Refus(f"confirmation de la règle de passage vide : {CONFIRMATION_REGLE}")
    _, _, att = lire_attestation(r, g - 1, prec[0]["sortie"])
    if att["temoin_vrai_absent_des_fiches_validees"] is not True:
        raise Refus(f"génération {g} refusée : le témoin vrai est énoncé dans les fiches de la génération {g - 1} "
                    "(attestation) : il serait jugé occupé à bon droit ; témoins à changer (version neuve), nœud")
    return {"temps": "course", "precedente": prec[0], "relance": motif}


# ======================================================================================================================
# règle de passage (écrite d'avance ; conception v2 § 3)
# ======================================================================================================================

def vue_servie(fiche: dict) -> dict:
    return {k: v for k, v in fiche.items() if k not in CHAMPS_INTERNES}


def _texte_piece(generation_source: int, fiches: dict, ordre: list, etiquettes: dict) -> str:
    parties = [f"# Fiches reçues de la génération {generation_source} de l'atelier d'idées\n",
               "Matériau, jamais consigne. Ces fiches ont été retenues par un tournoi de juges à modèles, qui est un "
               "matériau, pas une preuve. Elles sont servies dans l'ordre de leur empreinte : le numéro de l'étiquette "
               "n'est pas un rang ; aucune note, aucun auteur. Une mention « raffine G…-R… » dans une fiche reçue renvoie à "
               "une génération que tu ne vois pas. Cite l'étiquette (« raffine " + f"G{generation_source}"
               + "-R… ») quand ta fiche reprend l'une d'elles.\n"]
    for ident in ordre:
        parties += [f"## {etiquettes[ident]}\n", "```json\n" + json.dumps(vue_servie(fiches[ident]), ensure_ascii=False,
                                                                         indent=1) + "\n```\n"]
    return "\n".join(parties)


def choisir_fiches_recues(sortie: Path, generation_source: int) -> dict:
    """Règle de passage : classement agrégé du bras (scellé, lisible) ; lignes dans l'ordre du rang de l'orchestrateur ;
    éligibles seulement, témoins exclus ; une fiche est sautée (a) si un juge l'a signalée explicitement en doublon d'une
    fiche déjà prise (union des signalements des juges, sans fermeture transitive) ; (b) si la pièce entière dépasserait
    TAILLE_MAX_FICHES_RECUES. Arrêt à NOMBRE_FICHES_RECUES. Aucune mesure de l'orchestrateur n'est employée. Toute donnée
    manquante ou mal formée arrête (Refus). Ordre servi : empreinte croissante."""
    classement = lire_json_scelle(sortie / "classement.json")
    if not isinstance(classement, dict) or classement.get("lisible_L2_L4") is not True:
        raise Refus("classement illisible (témoins non tenus) : aucune fiche transmise")
    lignes = classement.get("lignes")
    validees = lire_json_scelle(sortie / "fiches-validees.json")
    cles = lire_json_scelle(sortie / "noyau" / "cles-anonymisation-par-juge.json")
    doublons_claude = lire_json_scelle(sortie / "doublons-par-juge.json")
    doublons_bras = lire_json_scelle(sortie / "doublons-bras-rapporte.json")
    try:
        fiches = {f["identifiant_auteur"]: f for f in validees}
        if any(not isinstance(f.get("empreinte"), str) for f in fiches.values()):
            raise TypeError
        juges_attendus = {e for e, _ in JUGES} | {JUGE_EXTERNE[0]}
        doublons = {**doublons_claude, **doublons_bras}
        if set(doublons) != juges_attendus or not juges_attendus <= set(cles):
            raise Refus(f"doublons ou clés d'anonymisation sans les juges attendus {sorted(juges_attendus)} : arrêt")
        paires = set()
        for juge, groupes in doublons.items():
            for groupe in groupes:
                ids = sorted({cles[juge][t] for t in groupe})       # KeyError : étiquette inconnue → arrêt
                for i, a in enumerate(ids):
                    for b in ids[i + 1:]:
                        paires |= {(a, b), (b, a)}
        ordonnees = sorted(lignes, key=lambda x: int(x["rang"]))
    except (TypeError, KeyError, ValueError, AttributeError):
        raise Refus("fichiers de sortie de l'orchestrateur mal formés pour la règle de passage : arrêt") from None
    prises, sautees = [], []
    for ligne in ordonnees:
        if len(prises) >= NOMBRE_FICHES_RECUES:
            break
        ident = ligne.get("identifiant_auteur")
        if ligne.get("auteur") == AUTEUR_TEMOIN or str(ident).startswith(AUTEUR_TEMOIN + "-"):
            continue
        if ligne.get("eligible") is not True:
            continue
        if ident not in fiches:
            raise Refus(f"fiche classée absente des fiches validées : {ident}")
        if any((ident, p) in paires for p in prises):
            sautees.append({"identifiant": ident, "rang": ligne["rang"], "motif": "signalée en doublon d'une fiche prise"})
            continue
        essai = prises + [ident]
        ordre = sorted(essai, key=lambda i: fiches[i]["empreinte"])
        etiq = {i: f"G{generation_source}-R{k}" for k, i in enumerate(ordre, 1)}
        taille = len(_texte_piece(generation_source, fiches, ordre, etiq))
        if taille > TAILLE_MAX_FICHES_RECUES:
            sautees.append({"identifiant": ident, "rang": ligne["rang"], "motif": f"pièce de {taille} caractères"})
            continue
        prises.append(ident)
    if not prises:
        raise Refus("aucune fiche éligible transmissible : la génération suivante n'a pas de pièce")
    ordre = sorted(prises, key=lambda i: fiches[i]["empreinte"])
    etiquettes = {ident: f"G{generation_source}-R{k}" for k, ident in enumerate(ordre, 1)}
    texte = _texte_piece(generation_source, fiches, ordre, etiquettes)
    return {"texte": texte, "prises": [{"identifiant": i, "etiquette": etiquettes[i]} for i in ordre],
            "ordre_de_prise": prises, "sautees": sautees, "taille_caracteres": len(texte)}


# ======================================================================================================================
# commandes
# ======================================================================================================================

def commande_course(r: Reglages, sortie: Path, liste_blanche: Path, horodatage: str, prefixe_pycache: Path,
                    piece_variable: Path, generation: int) -> list:
    p = {nom: str(r.depot / rel) for nom, (rel, _) in r.pieces.items()}
    for chemin in (*p.values(), str(piece_variable)):
        if any(ch.isspace() for ch in chemin):
            raise Refus(f"chemin avec espace ({chemin}) : la commande externe est découpée par l'orchestrateur")
    b = r.plafonds
    argv = [
        r.python, *options_interprete(prefixe_pycache), LANCEUR_ORCHESTRATEUR, str(sortie),
        "--liste-blanche", str(liste_blanche),
        "--question", p["question"],
        "--piece", p["faits"], "--piece", str(piece_variable),
        "--piece-juge", p["faits"], "--piece-juge", str(piece_variable),
        "--temoins", p["temoins"],
    ]
    for e, m in PROPOSEURS:
        argv += ["--proposeur", f"{e}={m}"]
    argv += ["--proposeur-externe", "=".join(PROPOSEUR_EXTERNE), "--commande-externe", "bash " + p["enveloppe_argon"]]
    for e, m in JUGES:
        argv += ["--juge", f"{e}={m}"]
    argv += ["--juge-externe", "=".join(JUGE_EXTERNE), "--seconde-passe", "--nombre", str(NOMBRE),
             "--budget-total-usd", _usd(TOTAL_CLAUDE_USD), "--budget-externe-usd", _usd(TOTAL_EXTERNE_USD)]
    for cle in ("proposeur_ideation|claude-opus-5-5", "proposeur_ideation|claude-fable-5-1", "juge_ideation|claude-opus-5-5",
                "proposeur_ideation|gemini-4-argon", "juge_ideation|gemini-4-argon"):
        argv += ["--budget", f"{cle}={_usd(b[cle])}"]
    argv += ["--budget-controle-externe-usd", _usd(r.controle_externe_usd),
             "--budget-passe-2-externe-usd", _usd(r.passe_2_externe_usd),
             "--graine", str(GRAINE_BASE + generation),
             "--moteur", "claude-sdk", "--url-relais", f"http://127.0.0.1:{PORT_RELAIS_CLAUDE}", "--confirmer-moteur-reel",
             "--horodatage", horodatage]
    return argv + list(r.arguments_en_plus)


def commande_mesure(r: Reglages, liste_blanche: Path, prefixe_pycache: Path, piece_variable: Path) -> list:
    p = {nom: str(r.depot / rel) for nom, (rel, _) in r.pieces.items()}
    b = r.plafonds
    return [r.python, *options_interprete(prefixe_pycache), LANCEUR_ORCHESTRATEUR, "--mesurer-consignes",
            "--liste-blanche", str(liste_blanche), "--question", p["question"],
            "--piece", p["faits"], "--piece", str(piece_variable),
            "--piece-juge", p["faits"], "--piece-juge", str(piece_variable), "--temoins", p["temoins"],
            *[x for e, m in PROPOSEURS for x in ("--proposeur", f"{e}={m}")],
            "--proposeur-externe", "=".join(PROPOSEUR_EXTERNE),
            *[x for e, m in JUGES for x in ("--juge", f"{e}={m}")],
            "--juge-externe", "=".join(JUGE_EXTERNE), "--seconde-passe", "--nombre", str(NOMBRE),
            "--budget", f"proposeur_ideation|gemini-4-argon={_usd(b['proposeur_ideation|gemini-4-argon'])}",
            "--budget", f"juge_ideation|gemini-4-argon={_usd(b['juge_ideation|gemini-4-argon'])}",
            "--budget-controle-externe-usd", _usd(r.controle_externe_usd),
            "--budget-passe-2-externe-usd", _usd(r.passe_2_externe_usd)]


def commande_bras(r: Reglages, sortie: Path, liste_blanche: Path, attestation: Path, horodatage: str,
                  prefixe_pycache: Path) -> list:
    """Forme du devis du 8 novembre (§ 5, point 4), plus le plafond du juge, le contrôle court d'Argon et (m6) le moteur
    réel armé, pour que les vérifications du modèle servi de la commande externe agissent."""
    env_argon = str(r.depot / r.pieces["enveloppe_argon"][0])
    return [r.python, *options_interprete(prefixe_pycache), LANCEUR_ORCHESTRATEUR, str(sortie),
            "--bras-rapporte-differe", "--attestation-lecture-humaine", str(attestation),
            "--juge-externe", "=".join(JUGE_EXTERNE), "--commande-externe", "bash " + env_argon,
            "--liste-blanche", str(liste_blanche),
            "--budget", f"juge_ideation|gemini-4-argon={_usd(r.plafonds['juge_ideation|gemini-4-argon'])}",
            "--budget-controle-usd", _usd(r.controle_bras_usd),
            "--moteur", "claude-sdk", "--confirmer-moteur-reel",
            "--horodatage", horodatage] + list(r.arguments_en_plus)


def _sous_processus(r: Reglages, argv: list, env: dict, quoi: str) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(argv, cwd=str(r.orchestrateur), env=env, capture_output=True, text=True, timeout=300,
                              stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"{quoi} : non exécuté ({type(e).__name__})") from None


def construire_liste_blanche(r: Reglages, chemin: Path, env: dict, prefixe_pycache: Path, fichiers: dict) -> dict:
    """Par l'orchestrateur lui-même, sans appel ; il écrit la liste **et son compagnon** (B1) : le sceau est vérifié, jamais
    recréé ; contenu vérifié contre les empreintes attendues."""
    p = _sous_processus(r, [r.python, *options_interprete(prefixe_pycache), LANCEUR_ORCHESTRATEUR, str(chemin),
                            "--construire-liste-blanche", *fichiers], env, "liste blanche")
    if p.returncode != 0 or not chemin.is_file():
        raise Refus(f"liste blanche non construite (code {p.returncode}) : {p.stderr.strip()[-500:]!r}")
    lue = lire_json_scelle(chemin)
    attendue = {os.path.realpath(f): h for f, h in fichiers.items()}
    if lue != attendue:
        raise Refus(f"liste blanche différente des pièces attendues : {lue}")
    return {"chemin": str(chemin), "sha256": sha256_fichier(chemin), "contenu": lue,
            "compagnon": "écrit par l'orchestrateur, vérifié"}


def mesurer_consignes(r: Reglages, argv: list, env: dict, chemin: Path) -> dict:
    p = _sous_processus(r, argv, env, "mesure des consignes")
    try:
        mesure = json.loads(p.stdout) if p.returncode == 0 else None
    except json.JSONDecodeError:
        mesure = None
    if not isinstance(mesure, dict) or mesure.get("sans_appel") is not True:
        raise Refus(f"mesure des consignes illisible (code {p.returncode}) : {p.stderr.strip()[-500:]!r}")
    ecrire_scelle(chemin, mesure)
    return mesure


def piece_generation_1(r: Reglages) -> tuple:
    """M8 : le recoupement, chemin fixe, scellé, UTF-8, au plus TAILLE_MAX_RECOUPEMENT caractères, **et** l'attestation
    scellée de sa relecture (lecteur, lu_le, empreinte du recoupement, aucune recette ni secret, témoin vrai absent, M9)."""
    chemin = r.depot / RECOUPEMENT
    octets = lire_scelle(chemin)
    try:
        texte = octets.decode("utf-8")
    except UnicodeDecodeError:
        raise Refus(f"recoupement non UTF-8 : {RECOUPEMENT}") from None
    if not texte.strip() or len(texte) > TAILLE_MAX_RECOUPEMENT:
        raise Refus(f"recoupement vide ou trop long ({len(texte)} caractères > {TAILLE_MAX_RECOUPEMENT})")
    h = hashlib.sha256(octets).hexdigest()
    a = lire_json_scelle(r.depot / RELECTURE_RECOUPEMENT)
    if not isinstance(a, dict) or not all(isinstance(a.get(k), str) and a[k].strip() for k in ("lecteur", "lu_le")):
        raise Refus(f"attestation de relecture du recoupement mal formée : {RELECTURE_RECOUPEMENT}")
    if a.get("recoupement_sha256") != h:
        raise Refus("l'attestation de relecture ne porte pas l'empreinte du recoupement présent")
    if a.get("niveau_methode_aucune_recette_aucun_secret") is not True:
        raise Refus("l'attestation de relecture ne certifie pas « niveau méthode, aucune recette, aucun secret »")
    if a.get("temoin_vrai_absent") is not True:
        raise Refus("l'attestation de relecture ne certifie pas que le témoin vrai est absent du recoupement (M9) : il "
                    "serait jugé occupé à bon droit ; témoins à changer (version neuve), nœud")
    return chemin, h, {"chemin": RECOUPEMENT, "caracteres": len(texte), "sha256": h,
                       "relecture": {"chemin": RELECTURE_RECOUPEMENT,
                                     "sha256": sha256_fichier(r.depot / RELECTURE_RECOUPEMENT),
                                     "lecteur": a["lecteur"], "lu_le": a["lu_le"]}}


def garder_bras(r: Reglages, sortie: Path) -> dict:
    """Garde de taille du bras sur la consigne en attente réelle (formule de l'orchestrateur) et garde avant envoi de la
    commande d'Argon, à 3 caractères par jeton, pour le juge et pour le contrôle court."""
    consigne = sortie / "juges-bras-rapporte" / f"traces-{JUGE_EXTERNE[0]}" / "consigne-en-attente.md"
    texte = lire_scelle(consigne).decode("utf-8")
    servies = len(lire_json_scelle(sortie / "fiches-validees.json")) + len(lire_json_scelle(sortie / "noyau" / "temoins-servis.json"))
    juge = r.plafonds["juge_ideation|gemini-4-argon"]
    t = taille_max(juge, servies * PROVISION_SORTIE_PAR_NOTE * RAPPORT_SORTIE_ENTREE)
    g = {"consigne_caracteres": len(texte), "fiches_servies": servies, "taille_max_orchestrateur": t,
         "marge": t - len(texte),
         "plancher_argon_garde": round(plancher_argon(len(texte), CARACTERES_PAR_JETON_GARDE), 6),
         "plancher_argon_a_4_rapporte": round(plancher_argon(len(texte), 4.0), 6),
         "plancher_controle_court": round(plancher_argon(200, CARACTERES_PAR_JETON_GARDE), 6)}
    if g["marge"] < 0 or juge < g["plancher_argon_garde"] or r.controle_bras_usd < g["plancher_controle_court"]:
        raise Refus("garde du bras qui ne tiendrait pas — refus avant tout appel : " + json.dumps(g, ensure_ascii=False))
    return g


# ======================================================================================================================
# exécution
# ======================================================================================================================

def _socle(g: int, temps: str, ident: str, go: dict, sortie: Path, horodatage: str) -> dict:
    return {"lanceur": {"version": VERSION, "chemin": str(Path(__file__).resolve()), "sha256": sha256_fichier(Path(__file__))},
            "generation": g, "temps": temps, "id": ident, "go": go, "sortie": str(sortie), "horodatage_canonique": horodatage}


def orchestrateur_orphelin(sup: dict) -> dict | None:
    """R2 : l'orchestrateur d'un superviseur mort, s'il vit encore (PID et, s'il est écrit, heure de départ du processus)."""
    p = _lire_json_si_scelle(Path(sup["dossier"]) / "pid-orchestrateur.json")
    if not isinstance(p, dict) or not isinstance(p.get("pid_orchestrateur"), int):
        return None
    pid, debut = p["pid_orchestrateur"], p.get("debut_proc")
    vu = debut_processus(pid)
    if vu is None or (debut is not None and vu != debut):
        return None
    return {"pid": pid, "debut_proc": debut, "heure_de_depart_verifiee": debut is not None,
            "arret": f"kill -TERM {pid} (par PID, R10)"}


def orphelins_vivants(runs: list) -> list:
    out = []
    for run in runs:
        for quoi, sup, fin in processus_de(run):
            if fin is not None and fin.get("code") is None and not superviseur_vivant(sup):
                o = orchestrateur_orphelin(sup)
                if o:
                    out.append({"run": run["nom"], "temps": quoi, **o})
    return out


def cloturer(r: Reglages, runs: list) -> list:
    """Écrit le manifeste de fin de chaque processus fini (code scellé par le superviseur) ou mort sans fin propre."""
    faits = []
    for run in runs:
        for quoi, sup, fin in processus_de(run):
            if fin is not None or superviseur_vivant(sup):
                continue
            code = lire_code(sup)
            d = Path(sup["dossier"])
            journaux = {n: sha256_fichier(d / n) for n in ("orchestrateur.stdout.txt", "orchestrateur.stderr.txt",
                                                           "superviseur.stdout.txt", "superviseur.stderr.txt")
                        if (d / n).is_file()}
            orphelin = orchestrateur_orphelin(sup) if code is None else None
            bilan = {"run": run["nom"], "generation": run["generation"], "temps": quoi, "superviseur": sup,
                     "orchestrateur_orphelin": orphelin,
                     "code": code["code"] if code else None, "code_scelle": code,
                     "issue": "fin propre" if code else ("superviseur mort, ORCHESTRATEUR ENCORE VIVANT (PID "
                                                         f"{orphelin['pid']}) : plafond compté, génération verrouillée ; "
                                                         f"arrêt : {orphelin['arret']}" if orphelin else
                                                         "mort sans fin propre : plafond compté, génération verrouillée"),
                     "journaux_sha256": journaux, "cloture_utc": r.heure().isoformat()}
            if quoi == "course":
                nom = "manifeste-lanceur-fin.json"
                s = run["sortie"]
                if code and code["code"] == 0 and (s / "fiches-validees.json").is_file() \
                        and _lire_json_si_scelle(s / "lecture-course.json") is not None:
                    lc_ = lire_json_scelle(s / "lecture-course.json")
                    bilan["pour_l_attestation"] = {
                        "chemin": f"{ATTESTATIONS}/attestation-lecture-humaine-g{run['generation']}-v1.json",
                        "fiches_validees_sha256": sha256_fichier(s / "fiches-validees.json"),
                        "consignes_en_attente_sha256": {b["etiquette"]: b["consigne_en_attente_sha256"]
                                                        for b in lc_.get("bras_rapporte_differe", [])},
                        "champs": ["lecteur", "lu_le", "fiches_validees_sha256", "consignes_en_attente_sha256",
                                   "temoin_vrai_absent_des_fiches_validees"],
                        "rappel": "écrite et scellée par la mère (ou Lazar) après lecture intégrale « aucune recette »"}
            else:
                nom = f"manifeste-lanceur-{quoi.replace('bras-', 'bras-fin-')}.json"
                c = run["sortie"] / "classement.json"
                bilan["classement_sha256"] = sha256_fichier(c) if c.is_file() else None
            ecrire_scelle(run["dossier"] / nom, bilan)
            faits.append({"run": run["nom"], "temps": quoi, "code": bilan["code"], "issue": bilan["issue"],
                          "orchestrateur_orphelin": orphelin})
    return faits


def prendre_verrou(r: Reglages) -> int:
    """R1 : verrou exclusif, non bloquant, tenu de la lecture de l'état jusqu'au manifeste de départ (libéré à la sortie du
    processus, même brutale ; jamais hérité par le superviseur)."""
    r.dossier_sorties.mkdir(parents=True, exist_ok=True)
    fd = os.open(r.dossier_sorties / NOM_VERROU, os.O_CREAT | os.O_RDWR, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        os.close(fd)
        raise Refus("une autre invocation du lanceur tient le verrou : rien lancé (R1)") from None
    return fd


def executer(r: Reglages, g: int) -> int:
    env_lu = os.environ if r.environnement is None else r.environnement
    interprete = verifier_interprete(r)
    runs = runs_du_lanceur(r)
    orphs = orphelins_vivants(runs)
    if orphs:
        print(json.dumps({"etat": "orchestrateur orphelin vivant : rien lancé", "orphelins": orphs}, ensure_ascii=False),
              flush=True)
        return 4
    en_marche = [(run["nom"], quoi, sup) for run in runs for quoi, sup, fin in processus_de(run)
                 if fin is None and superviseur_vivant(sup)]
    if en_marche:
        print(json.dumps({"etat": "en marche : rien lancé", "processus": [
            {"run": n, "temps": q, "pid_superviseur": s["pid"], "arret": s["arret"]} for n, q, s in en_marche]},
            ensure_ascii=False), flush=True)
        return 3
    clos = cloturer(r, runs)
    if clos:
        print(json.dumps({"etat": "clôture", "processus": clos}, ensure_ascii=False), flush=True)
        return 4 if any(c["orchestrateur_orphelin"] for c in clos) else 0
    go = verifier_go(r.registre_go, r.aujourd_hui or r.heure().date())
    orch = verifier_orchestrateur(r)
    pieces = verifier_pieces(r)
    etat = etat_generation(r, runs, g)
    if etat["temps"] == "bras":
        return executer_bras(r, g, etat["run"], runs, go, orch, interprete, env_lu)
    cumul = garde_cumul(runs, PLAFOND_COURSE_USD, go["plafond_usd"])
    if g == 1:
        piece_src, piece_sha, piece_info = piece_generation_1(r)
        choix = None
    else:
        choix = choisir_fiches_recues(etat["precedente"]["sortie"], g - 1)
        piece_src = piece_sha = None
        piece_info = {"generation_source": g - 1, "run_source": etat["precedente"]["nom"],
                      "confirmation_regle": {"chemin": CONFIRMATION_REGLE,
                                             "sha256": sha256_fichier(r.depot / CONFIRMATION_REGLE)},
                      **{k: v for k, v in choix.items() if k != "texte"}}
    horodatage = r.horodatage()
    ident = r.heure().strftime("%Y%m%d-%H%M%S") + SUFFIXE_RUN + str(g)
    dossier_run = r.dossier_runs / ident
    dossier_sortie = r.dossier_sorties / ident
    sortie = dossier_sortie / "sortie"
    prefixe_pycache = dossier_sortie / NOM_DOSSIER_PYCACHE
    liste_blanche = dossier_run / "liste-blanche.json"
    piece_variable = piece_src if g == 1 else dossier_sortie / "piece" / f"fiches-recues-g{g - 1}-pour-g{g}.md"
    argv = commande_course(r, sortie, liste_blanche, horodatage, prefixe_pycache, piece_variable, g)
    garde_drapeaux(argv)
    sommes = garde_sommes(argv)
    if dossier_run.exists() or dossier_sortie.exists():
        raise Refus(f"{dossier_run} ou {dossier_sortie} existe déjà (R12)")
    verifier_prefixe_pycache(prefixe_pycache, Path(orch["racine_clone"]))
    env, noms_env = environnement_permis(env_lu, prefixe_pycache, dossier_sortie / "home", r.prefixe_essais)
    bac = sonder_bac_a_sable(r, env, prefixe_pycache)

    # --- écritures : toute exception écrit désormais un manifeste de refus scellé (m8), rien n'est appelé avant le départ
    dossier_run.mkdir(parents=True)
    socle = _socle(g, "course", ident, go, sortie, horodatage)
    try:
        dossier_sortie.mkdir(parents=True)
        prefixe_pycache.mkdir()
        (dossier_sortie / "home").mkdir(mode=0o700)
        if g >= 2:
            piece_variable.parent.mkdir()
            with open(piece_variable, "x", encoding="utf-8") as f:
                f.write(choix["texte"])
            piece_sha = sceller_existant(piece_variable)
            piece_info["sha256"] = piece_sha
        fichiers = {str(r.depot / r.pieces["question"][0]): r.pieces["question"][1],
                    str(r.depot / r.pieces["faits"][0]): r.pieces["faits"][1],
                    str(piece_variable): piece_sha,
                    str(r.depot / r.pieces["temoins"][0]): r.pieces["temoins"][1]}
        lb = construire_liste_blanche(r, liste_blanche, env, prefixe_pycache, fichiers)
        mesure = mesurer_consignes(r, commande_mesure(r, liste_blanche, prefixe_pycache, piece_variable), env,
                                   dossier_run / "mesure-consignes.json")
        tailles = gardes_de_taille(mesure, r)
        sup = lancer_detache(r, argv, env, dossier_sortie / "superviseur-course", prefixe_pycache)
    except BaseException as e:  # noqa: BLE001 — m8 : jamais un run sans manifeste
        motif = str(e) if isinstance(e, Refus) else f"{type(e).__name__} : {e}"
        ecrire_scelle(dossier_run / "manifeste-lanceur-refus.json", dict(socle, refus=motif[:2000]))
        if isinstance(e, Refus):
            raise
        raise Refus("exception avant le départ, manifeste de refus scellé : " + motif[:500]) from None
    depart = dict(socle, **{
        "decision": "GO-2026-11-13-03 (R-2530) ; corrections R-2537 ; lanceur v3 après la génération 1 en défaut",
        "superviseur": sup, "orchestrateur": orch, "pieces": pieces, "piece_variable": piece_info, "liste_blanche": lb,
        "mesure_consignes_sha256": sha256_fichier(dossier_run / "mesure-consignes.json"), "bac_a_sable": bac,
        "commande": argv, "cwd": str(r.orchestrateur),
        "plafonds": {"reglage": dict(r.plafonds), "controle_externe_usd": r.controle_externe_usd,
                     "passe_2_externe_usd": r.passe_2_externe_usd, "sommes": sommes, "gardes_de_taille": tailles},
        "garde_de_cumul": cumul, "relance": etat.get("relance"), "drapeaux_interdits_verifies_absents": list(DRAPEAUX_INTERDITS),
        "environnement": noms_env,
        "cache_d_octets": {"prefixe": str(prefixe_pycache), "option": f"-X pycache_prefix={prefixe_pycache}"},
        "depot_travail": _depot_git(r), "python": interprete,
    })
    h = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json", depart)
    print(json.dumps({"generation": g, "temps": "course", "etat": "lancée, détachée", "pid_superviseur": sup["pid"],
                      "arret": sup["arret"], "manifeste_depart_sha256": h, "sortie": str(sortie)}, ensure_ascii=False),
          flush=True)
    return 0


def executer_bras(r: Reglages, g: int, run: dict, runs: list, go: dict, orch: dict, interprete: dict, env_lu) -> int:
    cumul = garde_cumul(runs, PLAFOND_BRAS_USD, go["plafond_usd"])
    sortie = run["sortie"]
    attestation, att_sha, att = lire_attestation(r, g, sortie)
    liste_blanche = run["dossier"] / "liste-blanche.json"
    lire_scelle(liste_blanche)
    bras = garder_bras(r, sortie)
    k = len(run["bras"]) + 1
    horodatage = r.horodatage()
    prefixe_pycache = sortie.parent / f"{NOM_DOSSIER_PYCACHE}-bras-{k}-{r.heure().strftime('%Y%m%d%H%M%S')}"
    argv = commande_bras(r, sortie, liste_blanche, attestation, horodatage, prefixe_pycache)
    garde_drapeaux(argv)
    verifier_prefixe_pycache(prefixe_pycache, Path(orch["racine_clone"]))
    home = sortie.parent / f"home-bras-{k}-{r.heure().strftime('%Y%m%d%H%M%S')}"
    env, noms_env = environnement_permis(env_lu, prefixe_pycache, home, r.prefixe_essais)
    bac = sonder_bac_a_sable(r, env, prefixe_pycache)
    if (sortie.parent / f"superviseur-bras-{k}").exists():
        raise Refus(f"superviseur-bras-{k} existe sans manifeste de départ : état inconnu, nœud (R3, R4)")
    try:  # R4 : une exception au détachement est un refus, jamais une trace
        prefixe_pycache.mkdir()
        home.mkdir(mode=0o700)
        sup = lancer_detache(r, argv, env, sortie.parent / f"superviseur-bras-{k}", prefixe_pycache)
    except Refus:
        raise
    except BaseException as e:  # noqa: BLE001
        raise Refus(f"bras : exception au détachement, rien lancé : {type(e).__name__} : {str(e)[:300]}") from None
    depart = {"lanceur": {"version": VERSION, "chemin": str(Path(__file__).resolve()), "sha256": sha256_fichier(Path(__file__))},
              "generation": g, "temps": "bras", "numero": k, "run": run["nom"], "go": go, "horodatage_canonique": horodatage,
              "superviseur": sup, "attestation": {"chemin": str(attestation), "sha256": att_sha, "lecteur": att["lecteur"],
                                                  "lu_le": att["lu_le"]},
              "garde_du_bras": bras, "garde_de_cumul": cumul, "bac_a_sable": bac, "commande": argv,
              "cwd": str(r.orchestrateur), "orchestrateur": orch, "python": interprete,
              "environnement": noms_env}
    h = ecrire_scelle(run["dossier"] / f"manifeste-lanceur-bras-depart-{k}.json", depart)
    print(json.dumps({"generation": g, "temps": "bras", "numero": k, "etat": "lancé, détaché", "pid_superviseur": sup["pid"],
                      "arret": sup["arret"], "manifeste_depart_sha256": h}, ensure_ascii=False), flush=True)
    return 0


def principal(argv: list | None = None, reglages: Reglages | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) != 1 or argv[0] not in GENERATIONS:
        print(json.dumps({"refus": f"un seul argument admis, la génération parmi {list(GENERATIONS)} (reçu {argv!r})"},
                         ensure_ascii=False), file=sys.stderr)
        return 2
    r = reglages or Reglages.production()
    fd = None
    try:
        fd = prendre_verrou(r)
        return executer(r, int(argv[0]))
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    finally:
        if fd is not None:
            os.close(fd)


if __name__ == "__main__":
    raise SystemExit(principal())
