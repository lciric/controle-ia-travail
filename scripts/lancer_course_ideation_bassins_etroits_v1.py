#!/usr/bin/env python3
"""Lanceur de l'organisme d'idéation (atelier d'idées, N-065 rôle 2) sur la question des bassins d'idées étroits et
profonds : trois générations enchaînées — version 1.

Dérivé du lanceur `scripts/lancer_course_ideation_pilier_attaque_v2_v3.py` (`0a704661…`, inchangé, R12) : mêmes gardes
(interpréteur absolu, ligne de GO, orchestrateur au commit épinglé sans fichier ignoré ni cache d'octets, neuf empreintes,
pièces épinglées, drapeaux interdits, sommes des plafonds calculées comme l'orchestrateur, gardes de taille, préfixe du
cache d'octets hors du clone, sonde du bac à sable de l'orchestrateur telle quelle, clés décidées sur les noms seuls,
manifestes scellés, signaux relayés par PID). Ce qui change :

- **GO-2026-11-13-03** (60 USD, trois courses de 12 + 8 USD, échéance 2026-11-30) lue et exigée ;
- **un argument unique et fermé** : la génération, `1`, `2` ou `3` ; rien d'autre n'est admis ;
- **deux temps par génération**, choisis par l'état sur disque, jamais par un argument : la course (proposeurs Opus 5.5,
  Fable 5.1 et Argon ; juge Opus 5.5 ; juge Argon différé), puis, quand l'attestation de lecture humaine de cette génération
  est scellée à son chemin fixe, le bras différé (juge Argon) qui écrit le classement ;
- **règle de passage écrite d'avance** (`choisir_fiches_recues`) : la génération g ≥ 2 reçoit, comme pièce, au plus cinq
  fiches de la génération g − 1, prises dans le classement agrégé du bras (lisible, témoins tenus chez chaque juge), dans
  l'ordre du rang de l'orchestrateur, éligibles seulement, en sautant toute fiche signalée en doublon par un juge ou
  appariée (même fiche, autre passe) à une fiche déjà prise, sous un plafond de 50 000 caractères ; servies dans un ordre
  neutre (empreinte), sans note, sans rang, sans auteur ; la génération 1 reçoit le recoupement des méthodes, au chemin
  fixe `RECOUPEMENT`, scellé, au plus 40 000 caractères ;
- **garde de cumul** : la dépense relevée de toutes les courses et de tous les bras déjà joués par ce lanceur, plus le
  plafond de ce qui va être lancé (20 USD pour une course, 3,1 USD pour un bras), ne dépasse jamais 60 USD (ni le plafond lu
  de la ligne de GO) ; une dépense illisible compte son plafond entier, dit au manifeste ;
- générations 2 et 3 **refusées** si la génération précédente n'a pas ses manifestes de fin scellés (course et bras, code
  0) et un classement scellé lisible ; une génération déjà tentée avec dépense n'est jamais relancée par ce lanceur ;
- **mesure des consignes sans appel** : l'orchestrateur lui-même (`--mesurer-consignes`, sans appel ni fichier), sur les
  pièces réelles de la génération ; gardes de taille de l'orchestrateur et garde avant envoi de la commande d'Argon
  (`commande_argon_v3d.py`) recalculées ; au bras, garde de la consigne du juge sur sa taille réelle.

Usage, seul et exact (cwd = racine du dépôt de travail) :

    /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v1.py 1     (puis 2, puis 3)

Tout refus rend 2, motif sur la sortie d'erreur ; avant l'écriture du dossier de run, rien n'est écrit ; après, seul un
manifeste de refus scellé l'est, et rien n'est appelé. Les fiches et journaux vont hors du dépôt
(`/home/user/sorties-course-ideation-bassins-etroits-v1/<id>/`) ; le dépôt garde les manifestes et leurs empreintes
(`runs/course-ideation-bassins-etroits-v1/<id>/`).

Bibliothèque standard seulement (le lanceur tourne sous `-I`). Les essais (`tests/test_lancer_course_ideation_bassins_
etroits_v1.py`) remplacent l'orchestrateur par un faux exécutable via `Reglages` ; la ligne de commande n'expose aucun
réglage.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping

VERSION = "lancer_course_ideation_bassins_etroits_v1"
GO_ID = "GO-2026-11-13-03"
DEPOT = Path(__file__).resolve().parents[1]
GENERATIONS = ("1", "2", "3")

# --- orchestrateur (dépôt public lciric/ideation-organism, clone en lecture de la consigne), épinglé ----------------------
ORCHESTRATEUR = Path("/home/user/lciric/ideation-organism/orchestrator")
COMMIT_ORCHESTRATEUR = "be6b5af96c9e19812569d8dab55d6ce3978a3823"
EMPREINTES_ORCHESTRATEUR = {  # mêmes valeurs qu'au commit f39a7f4a du lanceur v3 : chaîne de lancement inchangée
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
    "temoins": (f"{NOTES}/temoins-bassins-etroits-v1.json",
                "748f391ec2dff1687e8c3d3a7c431613c61a023ddcd1ee43708b516020d3900a"),
    "enveloppe_argon": ("rapports/fille-ideation-1-v1/appel-argon-v5.sh",
                        "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"),
    "commande_argon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py",
                       "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46"),
}
# pièces à chemin fixe, non épinglables d'avance : scellées (compagnon `.sha256`), empreinte portée au manifeste
RECOUPEMENT = f"{NOTES}/recoupement-methodes-v1.md"            # génération 1 : fourni par la mère
TAILLE_MAX_RECOUPEMENT = 40_000                                 # caractères
ATTESTATION = NOTES + "/attestations/attestation-lecture-humaine-g{g}-v1.json"   # par génération, avant son bras
TAILLE_MAX_FICHES_RECUES = 50_000                               # caractères de la pièce des générations 2 et 3
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
CONTROLE_EXTERNE_USD = 1.5
PASSE_2_EXTERNE_USD = 1.9
CONTROLE_BRAS_USD = 0.6                         # contrôle court d'Argon au bras (≥ 0,51 : garde avant envoi de la commande)
PLAFOND_BRAS_USD = PLAFONDS["juge_ideation|gemini-4-argon"] + CONTROLE_BRAS_USD
PROPOSEURS = (("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1"))
PROPOSEUR_EXTERNE = ("argon", "gemini-4-argon")
JUGES = (("opus-juge", "claude-opus-5-5"),)
JUGE_EXTERNE = ("argon-juge", "gemini-4-argon")
GRAINE_BASE = 2026111300                        # graine de la génération g : GRAINE_BASE + g (règle de l'orchestrateur ensuite)

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
# plafond ≥ ⌈⌈caractères / c⌉ × 1,05⌉ × 8,3e-6 + (4 096 + 8 192) × 41,5e-6 ; c = 4 (estimation de la commande) ; le compte
# exact de l'interface (`countTokens`) peut être plus grand : lecture à c = 3 rapportée, sans garde
ARGON_PRIX_ENTREE = 8.3e-6
ARGON_PRIX_SORTIE = 41.5e-6
ARGON_SORTIE_MIN = 4096
ARGON_PROVISION_PENSEE = 8192
ARGON_MARGE_ENTREE = 1.05
PORT_RELAIS_CLAUDE = 8787
DOSSIER_SORTIES = Path("/home/user/sorties-course-ideation-bassins-etroits-v1")
SOUS_DOSSIER_RUNS = "course-ideation-bassins-etroits-v1"
SUFFIXE_RUN = "-course-ideation-bassins-etroits-v1-g"
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

    @classmethod
    def production(cls) -> "Reglages":
        return cls(depot=DEPOT, orchestrateur=ORCHESTRATEUR, commit_orchestrateur=COMMIT_ORCHESTRATEUR,
                   empreintes_orchestrateur=dict(EMPREINTES_ORCHESTRATEUR), pieces=dict(PIECES),
                   registre_go=DEPOT / "registres" / "go.md", dossier_runs=DEPOT / "runs" / SOUS_DOSSIER_RUNS,
                   dossier_sorties=DOSSIER_SORTIES, depot_attendu_par_l_enveloppe=DEPOT_ATTENDU_PAR_L_ENVELOPPE,
                   python=PYTHON_COURSE)

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
        elif len(cellules) == 8 and cellules[2] == "révocation" and (go_id in cellules[3] or go_id in cellules[7]):
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
    import math
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
        v["plancher_a_4_caracteres_par_jeton"] = round(plancher_argon(v["consigne"], 4.0), 6)
        v["plancher_a_3_caracteres_par_jeton_rapporte"] = round(plancher_argon(v["consigne"], 3.0), 6)
        v["tient_a_4"] = v["plafond"] >= v["plancher_a_4_caracteres_par_jeton"]
        v["tient_a_3_rapporte"] = v["plafond"] >= v["plancher_a_3_caracteres_par_jeton_rapporte"]
    g["commande_argon"] = argon
    trop = {n: v for n, v in g.items() if n != "commande_argon" and (v["marge"] < 0 or v.get("orchestrateur_passerait") is False)}
    trop.update({f"commande_argon/{n}": v for n, v in argon.items() if not v["tient_a_4"]})
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


def environnement_sans_cles(env: Mapping, prefixe_pycache: Path | None = None) -> tuple:
    retires = sorted(n for n in env if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n))
    exclus = set(retires)
    garde = {n: env[n] for n in env if n not in exclus}
    garde["GO_ID"] = GO_ID
    if prefixe_pycache is not None:
        garde["PYTHONPYCACHEPREFIX"] = str(prefixe_pycache)
    return garde, retires


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

def _lire_json_si_scelle(chemin: Path):
    try:
        return lire_json_scelle(chemin)
    except Refus:
        return None


def runs_du_lanceur(r: Reglages) -> list:
    """Les runs de ce lanceur (manifeste de départ scellé exigé ; un dossier sans lui est une incohérence : refus)."""
    if not r.dossier_runs.is_dir():
        return []
    runs = []
    for nom in sorted(os.listdir(r.dossier_runs)):
        m = re.fullmatch(r"\d{8}-\d{6}" + re.escape(SUFFIXE_RUN) + r"([123])", nom)
        if not m:
            raise Refus(f"dossier inattendu dans {r.dossier_runs} : {nom!r}")
        d = r.dossier_runs / nom
        depart = _lire_json_si_scelle(d / "manifeste-lanceur-depart.json")
        refus = _lire_json_si_scelle(d / "manifeste-lanceur-refus.json")
        if depart is None and refus is None:
            raise Refus(f"run {nom} sans manifeste de départ ni de refus scellé : état inconnu, aucun lancement")
        base = depart or refus
        if str(base.get("generation")) != m.group(1) or base.get("lanceur", {}).get("version") != VERSION:
            raise Refus(f"run {nom} : génération ou version du lanceur incohérente")
        fin = _lire_json_si_scelle(d / "manifeste-lanceur-fin.json")
        bras = []
        k = 1
        while (d / f"manifeste-lanceur-bras-depart-{k}.json").exists():
            bras.append({"numero": k, "depart": _lire_json_si_scelle(d / f"manifeste-lanceur-bras-depart-{k}.json"),
                         "fin": _lire_json_si_scelle(d / f"manifeste-lanceur-bras-fin-{k}.json")})
            k += 1
        runs.append({"nom": nom, "dossier": d, "generation": int(m.group(1)), "depart": depart, "refus": refus, "fin": fin,
                     "bras": bras, "sortie": Path(base["sortie"]) if base.get("sortie") else None})
    return runs


def _cout(objet, *cles) -> float:
    for c in cles:
        objet = objet[c]
    if isinstance(objet, bool) or not isinstance(objet, (int, float)) or not objet >= 0 or objet != objet:
        raise ValueError("coût non fini ou négatif")
    return float(objet)


def depense_course(sortie: Path) -> tuple:
    """(dépense en USD, lecture). Manifeste de fin de l'orchestrateur scellé : ses deux totaux (contrôles compris). Sortie
    absente : tentatives de contrôle scellées (refus de taille : 0), ou 0 si rien n'est parti. Sinon : plafond entier."""
    controle = Path(str(sortie) + "-controle")
    fin = sortie / "manifeste-fin.json"
    if fin.exists():
        m = _lire_json_si_scelle(fin)
        try:
            j = m["reglages"]["journal"]
            return _cout(j, "cout_total_usd") + _cout(j, "cout_externe_usd"), "manifeste de fin de l'orchestrateur"
        except (TypeError, KeyError, ValueError):
            return PLAFOND_COURSE_USD, "manifeste de fin illisible : plafond entier compté"
    if sortie.exists():
        return PLAFOND_COURSE_USD, "sortie sans manifeste de fin scellé : plafond entier compté"
    if not controle.exists():
        return 0.0, "rien parti (ni sortie, ni contrôle)"
    total = 0.0
    for nom in sorted(os.listdir(controle)):
        p = controle / nom
        if re.fullmatch(r"tentative-\d+\.json", nom):
            m = _lire_json_si_scelle(p)
            try:
                total += _cout(m, "reglages", "cout_claude_usd") + _cout(m, "reglages", "cout_externe_usd")
            except (TypeError, KeyError, ValueError):
                return PLAFOND_COURSE_USD, f"tentative de contrôle illisible ({nom}) : plafond entier compté"
        elif re.fullmatch(r"(tentative-\d+(-externe-[a-z0-9-]+)?|refus-taille-\d+\.json|.*\.sha256)", nom):
            continue
        else:
            return PLAFOND_COURSE_USD, f"fichier de contrôle inattendu ({nom}) : plafond entier compté"
    dossiers = [n for n in os.listdir(controle) if re.fullmatch(r"tentative-(\d+)", n)]
    for n in dossiers:
        if not (controle / f"{n}.json").exists():
            return PLAFOND_COURSE_USD, f"contrôle {n} sans tentative scellée : plafond entier compté"
    return total, "tentatives de contrôle scellées (course non partie)"


def depense_bras(run: dict) -> tuple:
    """Dépense des bras d'un run : manifeste du bras de l'orchestrateur (tentative finale) et tentatives payées scellées ;
    chaque bras lancé sans trace lisible compte son plafond entier."""
    if not run["bras"]:
        return 0.0, "aucun bras"
    s = run["sortie"]
    total, lectures, expliques = 0.0, [], 0
    rapporte = s / "manifeste-bras-rapporte.json"
    if rapporte.exists():
        m = _lire_json_si_scelle(rapporte)
        try:
            total += _cout(m, "reglages", "journal", "cout_total_usd")
            lectures.append("manifeste du bras")
        except (TypeError, KeyError, ValueError):
            total += PLAFOND_BRAS_USD
            lectures.append("manifeste du bras illisible : plafond du bras compté")
        expliques += 1
    for nom in sorted(os.listdir(s)) if s.is_dir() else []:
        if re.fullmatch(r"bras-tentative-\d+\.json", nom):
            m = _lire_json_si_scelle(s / nom)
            try:
                total += _cout(m, "reglages", "journal", "cout_total_usd")
            except (TypeError, KeyError, ValueError):
                total += PLAFOND_BRAS_USD
                lectures.append(f"{nom} illisible : plafond du bras compté")
            expliques += 1
        elif re.fullmatch(r"manifeste-bras-(non-joue|refus-taille)-\d+\.json", nom):
            expliques += 1
    manquants = max(0, len(run["bras"]) - expliques)
    if manquants:
        total += manquants * PLAFOND_BRAS_USD
        lectures.append(f"{manquants} bras lancé(s) sans trace lisible : plafond du bras compté pour chacun")
    return total, "; ".join(lectures) or "bras sans dépense"


def depense_run(run: dict) -> dict:
    if run["depart"] is None:  # refus du lanceur avant la course : l'orchestrateur n'a rien lancé
        return {"run": run["nom"], "course_usd": 0.0, "bras_usd": 0.0, "lecture": "refus du lanceur avant la course"}
    c, lc = depense_course(run["sortie"])
    b, lb = depense_bras(run)
    return {"run": run["nom"], "course_usd": round(c, 6), "bras_usd": round(b, 6), "lecture": f"course : {lc} ; bras : {lb}"}


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


def etat_generation(runs: list, g: int) -> dict:
    """Le temps à jouer pour la génération g : « course » ou « bras » (avec le run), ou refus."""
    du_g = [x for x in runs if x["generation"] == g]
    if any(bras_reussi(x) for x in du_g):
        raise Refus(f"génération {g} déjà jouée (course et bras réussis) : jamais rejouée")
    reussies = [x for x in du_g if course_reussie(x)]
    if len(reussies) > 1:
        raise Refus(f"génération {g} : {len(reussies)} courses réussies (une au plus) : nœud pour la mère")
    if reussies:
        run = reussies[0]
        if len(run["bras"]) >= 3:
            raise Refus(f"génération {g} : trois bras déjà lancés sur {run['nom']} : plus de relance par ce lanceur")
        if run["bras"] and run["bras"][-1]["fin"] is None:
            raise Refus(f"génération {g} : bras {len(run['bras'])} sans manifeste de fin scellé : état inconnu, nœud")
        return {"temps": "bras", "run": run}
    parties = [x for x in du_g if x["depart"] is not None]
    for x in parties:
        dep = depense_run(x)
        if dep["course_usd"] + dep["bras_usd"] > 0 or x["fin"] is None:
            raise Refus(f"génération {g} déjà tentée ({x['nom']}, dépense relevée {dep['course_usd'] + dep['bras_usd']:.4f} "
                        f"USD, fin {'absente' if x['fin'] is None else 'code ' + str(x['fin'].get('code'))}) : aucune "
                        "relance après dépense par ce lanceur (R3) ; nœud pour la mère ou Lazar")
    if len(parties) >= 3:
        raise Refus(f"génération {g} : trois tentatives déjà faites")
    if g >= 2:
        prec = [x for x in runs if x["generation"] == g - 1 and bras_reussi(x)]
        if len(prec) != 1:
            raise Refus(f"génération {g} refusée : la génération {g - 1} n'a pas une course et un bras réussis, manifestes de "
                        "fin scellés et classement lisible")
        return {"temps": "course", "precedente": prec[0]}
    return {"temps": "course", "precedente": None}


# ======================================================================================================================
# règle de passage d'une génération à la suivante (écrite d'avance)
# ======================================================================================================================

def vue_servie(fiche: dict) -> dict:
    return {k: v for k, v in fiche.items() if k not in CHAMPS_INTERNES}


def taille_servie(fiche: dict) -> int:
    return len(json.dumps([vue_servie(fiche)], ensure_ascii=False, indent=1))


def choisir_fiches_recues(sortie: Path, generation_source: int) -> dict:
    """Règle de passage, écrite d'avance (conception § 3) : classement agrégé du bras (scellé, lisible) ; lignes dans
    l'ordre du rang de l'orchestrateur ; éligibles seulement, témoins exclus ; une fiche est sautée si un juge l'a signalée
    en doublon d'une fiche déjà prise, si elle est l'autre passe d'une fiche déjà prise (appariement des mesures de
    convergence de l'orchestrateur), ou si elle ferait passer la pièce au-delà de TAILLE_MAX_FICHES_RECUES ; arrêt à
    NOMBRE_FICHES_RECUES. Ordre servi : empreinte croissante ; étiquettes G<g>-R<i> ; ni note, ni rang, ni auteur."""
    classement = lire_json_scelle(sortie / "classement.json")
    if classement.get("lisible_L2_L4") is not True:
        raise Refus("classement illisible (témoins non tenus) : aucune fiche transmise")
    fiches = {f["identifiant_auteur"]: f for f in lire_json_scelle(sortie / "fiches-validees.json")}
    cles = lire_json_scelle(sortie / "noyau" / "cles-anonymisation-par-juge.json")
    doublons = dict(lire_json_scelle(sortie / "doublons-par-juge.json"))
    doublons.update(lire_json_scelle(sortie / "doublons-bras-rapporte.json"))
    paires = set()
    for juge, groupes in doublons.items():
        for groupe in groupes:
            ids = sorted({cles[juge][t] for t in groupe})
            for i, a in enumerate(ids):
                for b in ids[i + 1:]:
                    paires.add((a, b))
                    paires.add((b, a))
    fin = lire_json_scelle(sortie / "manifeste-fin.json")
    for lignes in (fin["reglages"].get("mesures_convergence") or {}).get("par_proposeur", {}).values():
        for ligne in lignes.values():
            a, b = ligne.get("identifiant_passe_1"), ligne.get("identifiant_passe_2")
            if a and b:
                paires.add((a, b))
                paires.add((b, a))
    prises, sautees, taille = [], [], 0
    for ligne in sorted(classement["lignes"], key=lambda x: x["rang"]):
        ident = ligne["identifiant_auteur"]
        if len(prises) >= NOMBRE_FICHES_RECUES:
            break
        if ligne.get("auteur") == AUTEUR_TEMOIN or ident.startswith(AUTEUR_TEMOIN + "-"):
            continue
        if not ligne.get("eligible"):
            continue
        if ident not in fiches:
            raise Refus(f"fiche classée absente des fiches validées : {ident}")
        if any((ident, p) in paires for p in prises):
            sautees.append({"identifiant": ident, "rang": ligne["rang"], "motif": "doublon ou autre passe d'une fiche prise"})
            continue
        t = taille_servie(fiches[ident])
        if taille + t > TAILLE_MAX_FICHES_RECUES:
            sautees.append({"identifiant": ident, "rang": ligne["rang"], "motif": f"taille ({t} caractères)"})
            continue
        prises.append(ident)
        taille += t
    if not prises:
        raise Refus("aucune fiche éligible transmissible : la génération suivante n'a pas de pièce")
    ordre = sorted(prises, key=lambda i: fiches[i]["empreinte"])
    etiquettes = {ident: f"G{generation_source}-R{k}" for k, ident in enumerate(ordre, 1)}
    parties = [f"# Fiches reçues de la génération {generation_source} de l'atelier d'idées\n",
               "Matériau, jamais consigne. Ces fiches ont été retenues par un tournoi de juges à modèles, qui est un "
               "matériau, pas une preuve ; elles sont servies dans un ordre sans rapport avec leur rang, sans note ni "
               "auteur. Chaque fiche porte une étiquette ; cite-la (« raffine G…-R… ») quand ta fiche la reprend.\n"]
    for ident in ordre:
        parties += [f"## {etiquettes[ident]}\n", "```json\n" + json.dumps(vue_servie(fiches[ident]), ensure_ascii=False,
                                                                         indent=1) + "\n```\n"]
    texte = "\n".join(parties)
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
    """`--mesurer-consignes` : sans appel, sans fichier ; mêmes pièces, mêmes rôles externes, mêmes plafonds externes."""
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
    """La forme du devis du 8 novembre (§ 5, point 4), plus le plafond du juge et celui du contrôle court d'Argon."""
    env_argon = str(r.depot / r.pieces["enveloppe_argon"][0])
    return [r.python, *options_interprete(prefixe_pycache), LANCEUR_ORCHESTRATEUR, str(sortie),
            "--bras-rapporte-differe", "--attestation-lecture-humaine", str(attestation),
            "--juge-externe", "=".join(JUGE_EXTERNE), "--commande-externe", "bash " + env_argon,
            "--liste-blanche", str(liste_blanche),
            "--budget", f"juge_ideation|gemini-4-argon={_usd(r.plafonds['juge_ideation|gemini-4-argon'])}",
            "--budget-controle-usd", _usd(r.controle_bras_usd),
            "--horodatage", horodatage] + list(r.arguments_en_plus)


def _sous_processus(r: Reglages, argv: list, env: dict, quoi: str) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(argv, cwd=str(r.orchestrateur), env=env, capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"{quoi} : non exécuté ({type(e).__name__})") from None


def construire_liste_blanche(r: Reglages, chemin: Path, env: dict, prefixe_pycache: Path, fichiers: dict) -> dict:
    """Par l'orchestrateur lui-même, sans appel ; contenu vérifié contre les empreintes attendues ; scellé ensuite."""
    p = _sous_processus(r, [r.python, *options_interprete(prefixe_pycache), LANCEUR_ORCHESTRATEUR, str(chemin),
                            "--construire-liste-blanche", *fichiers], env, "liste blanche")
    if p.returncode != 0 or not chemin.is_file():
        raise Refus(f"liste blanche non construite (code {p.returncode}) : {p.stderr.strip()[-500:]!r}")
    lue = json.loads(chemin.read_text(encoding="utf-8"))
    attendue = {os.path.realpath(f): h for f, h in fichiers.items()}
    if lue != attendue:
        raise Refus(f"liste blanche différente des pièces attendues : {lue}")
    return {"chemin": str(chemin), "sha256": sceller_existant(chemin), "contenu": lue}


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
    """Le recoupement des méthodes : chemin fixe, scellé, UTF-8, au plus TAILLE_MAX_RECOUPEMENT caractères."""
    chemin = r.depot / RECOUPEMENT
    octets = lire_scelle(chemin)
    try:
        texte = octets.decode("utf-8")
    except UnicodeDecodeError:
        raise Refus(f"recoupement non UTF-8 : {RECOUPEMENT}") from None
    if not texte.strip() or len(texte) > TAILLE_MAX_RECOUPEMENT:
        raise Refus(f"recoupement vide ou trop long ({len(texte)} caractères > {TAILLE_MAX_RECOUPEMENT})")
    return chemin, hashlib.sha256(octets).hexdigest(), {"chemin": RECOUPEMENT, "caracteres": len(texte)}


def lire_attestation(r: Reglages, g: int, sortie: Path) -> tuple:
    chemin = r.depot / ATTESTATION.format(g=g)
    a = lire_json_scelle(chemin)
    if not isinstance(a, dict) or not {"lecteur", "lu_le", "fiches_validees_sha256", "consignes_en_attente_sha256"} <= set(a):
        raise Refus(f"attestation de la génération {g} mal formée : {chemin}")
    if a["fiches_validees_sha256"] != sha256_fichier(sortie / "fiches-validees.json"):
        raise Refus(f"l'attestation de la génération {g} ne porte pas l'empreinte des fiches validées de sa course")
    if JUGE_EXTERNE[0] not in (a.get("consignes_en_attente_sha256") or {}):
        raise Refus(f"l'attestation de la génération {g} ne porte pas la consigne en attente de {JUGE_EXTERNE[0]}")
    return chemin, sha256_fichier(chemin)


def garder_bras(r: Reglages, sortie: Path) -> dict:
    """Garde de taille du bras sur la consigne en attente réelle (celle de l'orchestrateur : plafond du juge / prix prudent
    − 2 000 caractères de note par fiche servie au rapport 5 ; un refus là compterait une tentative non relançable) et garde
    avant envoi de la commande d'Argon (juge et contrôle court)."""
    consigne = sortie / "juges-bras-rapporte" / f"traces-{JUGE_EXTERNE[0]}" / "consigne-en-attente.md"
    texte = lire_scelle(consigne).decode("utf-8")
    servies = len(lire_json_scelle(sortie / "fiches-validees.json")) + len(lire_json_scelle(sortie / "noyau" / "temoins-servis.json"))
    juge = r.plafonds["juge_ideation|gemini-4-argon"]
    t = taille_max(juge, servies * PROVISION_SORTIE_PAR_NOTE * RAPPORT_SORTIE_ENTREE)
    g = {"consigne_caracteres": len(texte), "fiches_servies": servies, "taille_max_orchestrateur": t,
         "marge": t - len(texte), "plancher_argon_a_4": round(plancher_argon(len(texte)), 6),
         "plancher_argon_a_3_rapporte": round(plancher_argon(len(texte), 3.0), 6),
         "plancher_controle_court": round(plancher_argon(200), 6)}
    if g["marge"] < 0 or juge < g["plancher_argon_a_4"] or r.controle_bras_usd < g["plancher_controle_court"]:
        raise Refus("garde du bras qui ne tiendrait pas — refus avant tout appel : " + json.dumps(g, ensure_ascii=False))
    return g


# ======================================================================================================================
# exécution
# ======================================================================================================================

def _executer_enfant(argv: list, r: Reglages, env: dict, sortie_std: Path, sortie_err: Path) -> tuple:
    debut = r.heure()
    with open(sortie_std, "xb") as fo, open(sortie_err, "xb") as fe:
        enfant = subprocess.Popen(argv, cwd=str(r.orchestrateur), env=env, stdout=fo, stderr=fe)

        def relayer(num, _cadre):  # R10 : par PID, jamais par motif
            try:
                enfant.send_signal(num)
            except ProcessLookupError:
                pass
        anciens = {s: signal.signal(s, relayer) for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)}
        try:
            code = enfant.wait()
        finally:
            for s, a in anciens.items():
                signal.signal(s, a)
    return enfant.pid, code, debut, r.heure()


def _communs(r: Reglages, g: int) -> tuple:
    interprete = verifier_interprete(r)
    go = verifier_go(r.registre_go, r.aujourd_hui or r.heure().date())
    orch = verifier_orchestrateur(r)
    pieces = verifier_pieces(r)
    runs = runs_du_lanceur(r)
    etat = etat_generation(runs, g)
    return interprete, go, orch, pieces, runs, etat


def executer(r: Reglages, g: int) -> int:
    env_lu = os.environ if r.environnement is None else r.environnement
    interprete, go, orch, pieces, runs, etat = _communs(r, g)
    if etat["temps"] == "bras":
        return executer_bras(r, g, etat["run"], runs, go, orch, interprete, env_lu)
    cumul = garde_cumul(runs, PLAFOND_COURSE_USD, go["plafond_usd"])
    if g == 1:
        piece_src, piece_sha, piece_info = piece_generation_1(r)
        choix = None
    else:
        choix = choisir_fiches_recues(etat["precedente"]["sortie"], g - 1)
        piece_src = piece_sha = None
        piece_info = {"generation_source": g - 1, "run_source": etat["precedente"]["nom"], **{k: v for k, v in choix.items()
                                                                                            if k != "texte"}}
    horodatage = r.horodatage()
    ident = r.heure().strftime("%Y%m%d-%H%M%S") + SUFFIXE_RUN + str(g)
    dossier_run = r.dossier_runs / ident
    dossier_sortie = r.dossier_sorties / ident
    sortie = dossier_sortie / "sortie"
    prefixe_pycache = dossier_sortie / NOM_DOSSIER_PYCACHE
    liste_blanche = dossier_run / "liste-blanche.json"
    if g == 1:
        piece_variable = piece_src
    else:
        piece_variable = dossier_sortie / "piece" / f"fiches-recues-g{g - 1}-pour-g{g}.md"
    argv = commande_course(r, sortie, liste_blanche, horodatage, prefixe_pycache, piece_variable, g)
    garde_drapeaux(argv)
    sommes = garde_sommes(argv)
    if dossier_run.exists() or dossier_sortie.exists():
        raise Refus(f"{dossier_run} ou {dossier_sortie} existe déjà (R12)")
    verifier_prefixe_pycache(prefixe_pycache, Path(orch["racine_clone"]))
    env, retires = environnement_sans_cles(env_lu, prefixe_pycache)
    bac = sonder_bac_a_sable(r, env, prefixe_pycache)

    # --- écritures (un refus désormais écrit un manifeste de refus scellé, rien n'est appelé) ---
    dossier_run.mkdir(parents=True)
    dossier_sortie.mkdir(parents=True)
    prefixe_pycache.mkdir()
    socle = {"lanceur": {"version": VERSION, "chemin": str(Path(__file__).resolve()), "sha256": sha256_fichier(Path(__file__))},
             "generation": g, "temps": "course", "id": ident, "go": go, "sortie": str(sortie), "horodatage_canonique": horodatage}
    try:
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
    except Refus as e:
        ecrire_scelle(dossier_run / "manifeste-lanceur-refus.json", dict(socle, refus=str(e)))
        raise
    depart = dict(socle, **{
        "decision": "GO-2026-11-13-03 (R-2530) : règle de permission pour la seule commande exacte",
        "orchestrateur": orch, "pieces": pieces, "piece_variable": piece_info, "liste_blanche": lb,
        "mesure_consignes_sha256": sha256_fichier(dossier_run / "mesure-consignes.json"), "bac_a_sable": bac,
        "commande": argv, "cwd": str(r.orchestrateur),
        "plafonds": {"reglage": dict(r.plafonds), "controle_externe_usd": r.controle_externe_usd,
                     "passe_2_externe_usd": r.passe_2_externe_usd, "sommes": sommes, "gardes_de_taille": tailles},
        "garde_de_cumul": cumul, "drapeaux_interdits_verifies_absents": list(DRAPEAUX_INTERDITS),
        "cles": {"noms_retires_de_l_environnement": retires,
                 "valeurs": "aucune valeur de clé écrite, transmise ni consultée (décision sur les noms)"},
        "cache_d_octets": {"prefixe": str(prefixe_pycache), "option": f"-X pycache_prefix={prefixe_pycache}"},
        "depot_travail": _depot_git(r), "python": interprete,
        "journaux": {"stdout": str(dossier_sortie / "course.stdout.txt"), "stderr": str(dossier_sortie / "course.stderr.txt")},
    })
    h_depart = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json", depart)
    print(json.dumps({"generation": g, "temps": "course", "manifeste_depart": str(dossier_run / "manifeste-lanceur-depart.json"),
                      "sha256": h_depart, "sortie": str(sortie)}, ensure_ascii=False), flush=True)
    pid, code, debut, fin = _executer_enfant(argv, r, env, dossier_sortie / "course.stdout.txt",
                                             dossier_sortie / "course.stderr.txt")
    bilan = {"id": ident, "generation": g, "temps": "course", "manifeste_depart_sha256": h_depart, "pid_orchestrateur": pid,
             "code": code, "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat(),
             "journaux_sha256": {n: sha256_fichier(dossier_sortie / n) for n in ("course.stdout.txt", "course.stderr.txt")},
             "sortie_existe": sortie.exists()}
    if code == 0 and (sortie / "fiches-validees.json").is_file() and (sortie / "lecture-course.json").is_file():
        lc = json.loads((sortie / "lecture-course.json").read_text(encoding="utf-8"))
        bilan["pour_l_attestation"] = {
            "chemin": ATTESTATION.format(g=g), "fiches_validees_sha256": sha256_fichier(sortie / "fiches-validees.json"),
            "consignes_en_attente_sha256": {b["etiquette"]: b["consigne_en_attente_sha256"]
                                            for b in lc.get("bras_rapporte_differe", [])},
            "rappel": "l'attestation est écrite et scellée par le lecteur humain après lecture intégrale « aucune recette »"}
    h_fin = ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
    print(json.dumps({"manifeste_fin": str(dossier_run / "manifeste-lanceur-fin.json"), "sha256": h_fin, "code": code},
                     ensure_ascii=False), flush=True)
    return code


def executer_bras(r: Reglages, g: int, run: dict, runs: list, go: dict, orch: dict, interprete: dict, env_lu) -> int:
    cumul = garde_cumul(runs, PLAFOND_BRAS_USD, go["plafond_usd"])
    sortie = run["sortie"]
    attestation, att_sha = lire_attestation(r, g, sortie)
    liste_blanche = run["dossier"] / "liste-blanche.json"
    lire_scelle(liste_blanche)
    bras = garder_bras(r, sortie)
    k = len(run["bras"]) + 1
    horodatage = r.horodatage()
    prefixe_pycache = sortie.parent / f"{NOM_DOSSIER_PYCACHE}-bras-{k}"
    argv = commande_bras(r, sortie, liste_blanche, attestation, horodatage, prefixe_pycache)
    garde_drapeaux(argv)
    verifier_prefixe_pycache(prefixe_pycache, Path(orch["racine_clone"]))
    env, retires = environnement_sans_cles(env_lu, prefixe_pycache)
    bac = sonder_bac_a_sable(r, env, prefixe_pycache)
    prefixe_pycache.mkdir()
    std, err = sortie.parent / f"bras-{k}.stdout.txt", sortie.parent / f"bras-{k}.stderr.txt"
    depart = {"lanceur": {"version": VERSION, "chemin": str(Path(__file__).resolve()), "sha256": sha256_fichier(Path(__file__))},
              "generation": g, "temps": "bras", "numero": k, "run": run["nom"], "go": go, "horodatage_canonique": horodatage,
              "attestation": {"chemin": str(attestation), "sha256": att_sha}, "garde_du_bras": bras, "garde_de_cumul": cumul,
              "bac_a_sable": bac, "commande": argv, "cwd": str(r.orchestrateur), "orchestrateur": orch, "python": interprete,
              "cles": {"noms_retires_de_l_environnement": retires,
                       "valeurs": "aucune valeur de clé écrite, transmise ni consultée (décision sur les noms)"},
              "journaux": {"stdout": str(std), "stderr": str(err)}}
    h_depart = ecrire_scelle(run["dossier"] / f"manifeste-lanceur-bras-depart-{k}.json", depart)
    print(json.dumps({"generation": g, "temps": "bras", "numero": k, "sha256": h_depart}, ensure_ascii=False), flush=True)
    pid, code, debut, fin = _executer_enfant(argv, r, env, std, err)
    bilan = {"generation": g, "temps": "bras", "numero": k, "manifeste_depart_sha256": h_depart, "pid_orchestrateur": pid,
             "code": code, "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat(),
             "journaux_sha256": {std.name: sha256_fichier(std), err.name: sha256_fichier(err)},
             "classement_sha256": sha256_fichier(sortie / "classement.json") if (sortie / "classement.json").is_file() else None}
    h_fin = ecrire_scelle(run["dossier"] / f"manifeste-lanceur-bras-fin-{k}.json", bilan)
    print(json.dumps({"manifeste_fin": f"manifeste-lanceur-bras-fin-{k}.json", "sha256": h_fin, "code": code},
                     ensure_ascii=False), flush=True)
    return code


def principal(argv: list | None = None, reglages: Reglages | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) != 1 or argv[0] not in GENERATIONS:
        print(json.dumps({"refus": f"un seul argument admis, la génération parmi {list(GENERATIONS)} (reçu {argv!r})"},
                         ensure_ascii=False), file=sys.stderr)
        return 2
    try:
        return executer(reglages or Reglages.production(), int(argv[0]))
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
