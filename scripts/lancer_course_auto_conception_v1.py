#!/usr/bin/env python3
"""Lanceur de la course d'auto-conception de l'organisme d'idéation — version 1.

Demande de Lazar (R-3209 point 6, R-3211, R-3235 ; GO-2026-11-18-18 pour l'ordre des priorités) : l'organisme conçoit sa
version suivante en partant de la matière première des mécanismes publiés (catalogue `matiere-premiere-v3.md`, R-3263),
sans refaire l'existant, sur les cinq axes du directeur (originalité, exploration, robustesse, mémoire, épreuve contre le
réel). Préenregistrement : `docs/notes/organisme-auto-conception-v1/course-v1/preenregistrement-course-auto-conception-v1.md`
(empreinte épinglée ci-dessous). Course 2 de l'orchestrateur épinglé (`demonstrations/ideation_v8.py --course-2`, v56), une
génération ; les cartes sont de la matière, jamais des preuves.

Modèle : le lanceur de la course d'affinage v4 (`scripts/lancer_course_affinage_mentors_v4.py`, non modifié), dont les gardes
sont reprises, **plus les cinq constats de sa contre-lecture portés d'emblée** :
1. la garde « une seule course » ne se bloque plus elle-même : une course est « lancée » seulement si un manifeste de départ
   existe au dépôt ou si un journal `course.stdout.txt` existe hors dépôt ; le dossier de sortie n'est créé qu'**après** la
   porte à blanc et toutes les gardes ;
2. `--url`, `--modeles-permis` et `--plafond-ligne` de chaque commande de porte sont recoupés avec la déclaration et la
   configuration (Claude : modèles Claude exacts de la configuration, plafond de ligne = plafond d'arrêt) ;
3. garde de crédit **v5** : « You exceeded your current quota … billing details » seul n'arrête pas la course (soupçon ;
   arrêt au deuxième soupçon du même relais) ;
4. le relais Gemini d'Argon est contrôlé avant le départ (PID : programme épinglé par la procédure, port 8788 de l'enveloppe,
   modèle, nombre d'appels permis ; état lu sur la boucle locale : zéro appel, variable de clé effacée) ;
5. le registre des GO est lu dans un **commit nommé** (`refs/remotes/origin/main`, résolu au lancement) ; le registre dérivé
   et le manifeste citent ce commit et l'empreinte du registre source.

Ce qui est propre à cette course :
- **Matière servie** : `docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md`, empreinte épinglée
  (R-3263), lue à l'octet dans le commit `refs/remotes/origin/main` (jamais la v1 ni la v2, jamais le relevé JSON) ;
  **tout est servi**, découpé en lots par les titres du catalogue lui-même (règle `decouper_matiere`, ci-dessous), sortie
  écrite et scellée au dossier du run ;
- **pièce de départ de la mère** (`course-v1/piece-de-depart-auto-conception-v1.json`, scellée par la mère) : identifiants
  des deux lignes de GO (course, épreuve des témoins), **nom de la variable de la clé Claude** (pas encore donné : refus
  tant qu'il n'est pas écrit ; Minuit refusée, réservée à la course d'affinage), crédit déclaré de cette clé, réserve à
  garder sur la clé de Kimi, et commandes d'Astra et de Carbon épinglées et éprouvées (sinon ces espèces sont refusées) ;
- **épreuve réelle des témoins du juge** (`scripts/epreuve_temoins_auto_conception_v1.py`, épinglé) : rapport scellé,
  « réussie », du jour, exigé avant tout départ (rien ne part sans elle, R-3229) ;
- contre-lecture par le modèle K, garde stricte (première ligne du verdict exactement « Scellable. »).

Codes : 0 course finie ; 2 refus avant départ, ou arrêt ou nœud de l'orchestrateur ; 3 alerte de crédit avant le départ ;
4 cumul lu au-dessus du plafond d'arrêt ; 5 course arrêtée au premier refus pour crédit d'un relais dispensé.

Usage (cwd = racine du dépôt de travail) :

    /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v1.py
    /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v1.py --a-blanc DOSSIER_NEUF
    /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v1.py --decouper MATIERE.md DOSSIER_NEUF

`--a-blanc` : moteur simulé de l'orchestrateur, relais factices, aucune dépense, aucun GO, aucune lecture de `registres/`.
`--decouper` : applique la règle des lots à un fichier local et écrit les lots scellés (aucun appel).

Bibliothèque standard seulement (le lanceur tourne sous `-I`). Ce lanceur nomme des modèles dans la configuration qu'il passe
à l'orchestrateur (comme le lanceur de référence) ; les pièces servies n'en nomment aucun.
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
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

VERSION = "lancer_course_auto_conception_v1"
PLAFOND_ARRET_USD = 90.0          # proposé au devis v1 ; la ligne de GO de la course doit porter exactement ce montant
PLAFOND_EPREUVE_USD = 5.0         # épreuve réelle des témoins : ligne de GO à part, exactement ce montant
DEPOT = Path(__file__).resolve().parents[1]
COURSE = "docs/notes/organisme-auto-conception-v1/course-v1"
COURSE_AFFINAGE_V3 = "docs/notes/organisme-affinage-mentors-v1/course-v3"
FOURNISSEURS_DISPENSABLES = ("argon", "astra", "carbon")
REFERENCE_DISPENSE = "R-3237"
PROCEDURE_RELAIS = f"{COURSE_AFFINAGE_V3}/procedure-relais-persistants-course-affinage-v3.json"
PIECE_DE_DEPART = f"{COURSE}/piece-de-depart-auto-conception-v1.json"
EPREUVE_REELLE = f"{COURSE}/epreuve-temoins-reelle-auto-conception-v1.json"
RELEVE_PRIX = f"{COURSE}/releve-prix-claude-course-auto-conception-v1.json"
PREREG = f"{COURSE}/preenregistrement-course-auto-conception-v1.md"
PREREG_SHA256 = "cef7ce8b397c9ed53f08cdde870c22838ba600e5f20870ae28fa78703a2677e0"
CONTRE_LECTURE = f"{COURSE}/contre-lecture-preenregistrement-course-auto-conception-v1.md"
DECLARATION_RELAIS = f"{COURSE}/declaration-relais-course-auto-conception-v1.json"
RELEVE_CREDITS = f"{COURSE}/releve-credits-avant-course-auto-conception-v1.json"
# Matière servie (R-3263) : la v3 seule, à son empreinte, lue dans le commit de main résolu au lancement.
MATIERE = ("docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md",
           "11f4b69ba42147c428090e4805948a708d0ed266da0c0cd07f194723eaba742d")
REF_MAIN = "refs/remotes/origin/main"
# Barème du relais de clé de la procédure (`pole/relais_reel.py`, 1b90b020…, l. 49-54), USD par million (entrée, sortie).
BAREME_CLAUDE = {"claude-opus-5-5": (4.0, 20.0), "claude-fable-5-1": (10.0, 50.0)}
# Programmes de relais épinglés par la procédure neutre (§ 1) : nom de fichier → empreinte.
PROGRAMMES_RELAIS = {"claude": ("relais_reel.py", "1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153"),
                     "kimi": ("relais_kimi_v4.py", "67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e"),
                     "argon": ("relais_gemini_v2.py", "2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb")}
PORT_RELAIS_ARGON = "8788"           # adresse fixée par l'enveloppe d'Argon v5 (`--url-base http://127.0.0.1:8788/v1beta`)
MODELE_ARGON = "gemini-4-argon"
ETAPE_A_BLANC = "porte-a-blanc"
DOSSIER_SORTIES = Path("/home/user/sorties-course-auto-conception-v1")
SUFFIXE_RUN = "-course-auto-conception-v1"
MARQUEUR_A_REMPLIR = "À REMPLIR"
PREFIXE_CLES_CLAUDE = "RR_ANTHROPIC_API_KEY"
CLES_CLAUDE_RESERVEES = ("RR_ANTHROPIC_API_KEY_MINUIT",)   # réservée à la course d'affinage (consigne de la mère)

PIECES = {
    "configuration": (f"{COURSE}/configuration-course-auto-conception-v1.json", "f4e5c021d9540c43dfd33915ffc556961610ab383526d27f42b59a0f55d26001"),
    "garde_credit": ("scripts/garde_credit_relais_v5.py", "6cf8786943bb6c9e51dd6909714e83de783e70dffc80ea1fad46a0e1545d30cd"),
    "porte_plafond": ("scripts/porte_plafond_relais_v1.py", "fab5fe2e924c47799d968663baddfecb85dd6f74e9f859d9047b185eb36382b1"),
    "procedure_relais": (PROCEDURE_RELAIS, "d97594dbc2263cd4200113d44dd4fd3fc8562bef617d3e182f6a382bf95ec792"),
    "procedure_ecrite": ("docs/procedures/relais-persistants-v1.md", "0ca9cf5daa190135f8f26175f2639e4c9c4b22b01c551ab30ff8f7bb0d085148"),
    "lanceur_relais": ("scripts/lancer_relais_local_v1.py", "d365affcb0303283a71ac7d5e67e24a5b6060e3b13c2a9e83ea592e48d4b3c82"),
    "consigne_proposeur": (f"{COURSE}/consigne-proposeur-auto-conception-v1.md", "a7c021c97dfaa061c0fd002c404eb82b01791cfefc860e5d71819c0df561c247"),
    "consigne_aiguilleur": (f"{COURSE}/consigne-aiguilleur-auto-conception-v1.md", "5e3dbdb50740c41267bdc6b66e733d9d677758674ffca0936280ead80d87556e"),
    "consigne_juge": (f"{COURSE}/consigne-juge-auto-conception-v1.md", "b03f33b87150eb67e5e55f3fc093812e5a359ab655362b3033dde561e58b5167"),
    "consigne_passe_tableau": (f"{COURSE}/consigne-passe-tableau-auto-conception-v1.md", "7c500696ab5716c9722ae323cbe4f152ba86f5c03c4ca265ce1631cf97d5d3c2"),
    "temoins": (f"{COURSE}/temoins-juge-auto-conception-v1.json", "a69f18265b2b5f3cec3e872fd167532fd300321807fe6199bb59c781c8f949df"),
    "epreuve_temoins": ("scripts/epreuve_temoins_auto_conception_v1.py", "5e354e7d2bd6d5e3f1b02f9b9594d615299604c63c77a698b2d0cdb8da30c975"),
    "enveloppe_argon": ("rapports/fille-ideation-1-v1/appel-argon-v5.sh",
                        "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"),
    "commande_argon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py",
                       "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46"),
}
PIECES_SERVIES = ("consigne_proposeur", "consigne_aiguilleur", "consigne_juge", "consigne_passe_tableau")
DEPOT_ATTENDU_PAR_L_ENVELOPPE = Path("/home/user/controle-ia-travail")

ORCHESTRATEURS_CANDIDATS = (Path("/home/user/ideation-organism/orchestrator"),
                            Path("/home/user/lciric/ideation-organism/orchestrator"))
COMMIT_ORCHESTRATEUR = "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb"
LANCEUR_ORCHESTRATEUR = "demonstrations/ideation_v8.py"
EMPREINTES_ORCHESTRATEUR = {
    "demonstrations/ideation_v8.py": "2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1",
    "demonstrations/ideation_v7.py": "7b90e65e1308b1c230b3f804743cfc42b9dc571d93b73ed6c5f3f8c9d2b481b2",
    "demonstrations/ideation_v6.py": "4c302e5b97b229d5b3edd9e9a427f1e50796c10f7081f63132165ffeef854ba4",
    "demonstrations/ideation_v5.py": "1894f250264eaaccbf891dfa255e71dc587fe415c8d21e283391203a2fe73444",
    "demonstrations/ideation_v4.py": "4212d4c9d014a265847d4c4ed87a8cd804fdafa73f85fd8947874d63fca1c36d",
    "demonstrations/ideation_v2.py": "bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845",
    "pole/configuration_v53.py": "ef72ffbf6b5ba546fb5e509502b59f0d9ac4f78772dcb9570ef36086639f4a78",
    "pole/configuration_v54.py": "3424ca7fa8911e5c2656cb56632f7d74c958008b9366af0ac45e6a62e4d16d66",
    "pole/configuration_v55.py": "2e6237c0a8b1c823fa17ddd6c680357a59ec4030bfbe9ac6ba970a700a864071",
    "pole/configuration_v56.py": "122405228d6ec550b2120114e87a1e70bcc74c14eee17342605d8402bd015d6b",
    "pole/course2_v53.py": "8f2d035828df913d8fa92e1b7d0c8e41ac73e8416e60f3b674753c27f5c61237",
    "pole/course2_v54.py": "ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342",
    "pole/course2_v55.py": "ee6a861e7f8db32a9545372a51f902389cdbea809b0ba354e621a3681e541a70",
    "pole/course2_v56.py": "14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1",
    "pole/budget_v56.py": "3a672aceeeee3cf83cd4e46ca461fdbaf3acd0a9552be24d2566627ce6b7c13e",
    "pole/adaptateurs.py": "a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99",
    "pole/adaptateurs_v56.py": "d36c79b272af450b8d67313f44068743d80f0204bcedbd30f5d879829c945a17",
    "pole/adaptateur_kimi_v53.py": "09a46515ff30a99f360fcbc7d4c613c35cb511439a5b6c249327e477fdee4ada",
    "pole/aiguilleur_v53.py": "a856cdaa37e8fb1f3b873ef2c0d9aa439ee0a8838f5ee9a2910cb3c0dcf8007f",
    "pole/juges_croises_v53.py": "c4c6ab12dc471eef078c116a4205a22d9b498da720ce71e37a0a6edae6c4239b",
    "pole/memoire_v53.py": "43b01b43b1ec347ff02b456975d74c17e7a0e974e9b95e9ba4935bdb895f31a0",
    "pole/noyau_v56.py": "eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b",
    "pole/gardes_e0_v56.py": "921e59f23753666d6367678447edf4ee2964dc6ec3d382aefa8582b996e123b9",
    "pole/simulation_v56.py": "bcafca44c5117dfd30262ee520a67944d051208f1b1deac6fac016e8cb95dc76",
    "pole/relais_reel_v2.py": "98c3e79e2c795a69345ffcf9aa742e31dde4a578a15f7c610f1ec7fd535ac8d7",
    "pole/fiches_v54.py": "1ab0796dd5d9de14ea84953b0307a065572bc300ebe45209ca207d7880bbaebf",
}

# Devis v1 (`docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v1.md`), estimation par appel, USD.
DEVIS_V1_PAR_APPEL = {"prop-opus": 0.2536, "prop-fable": 0.6341, "prop-argon": 0.5263, "prop-kimi": 0.1268, "prop-astra": 0.6341,
                      "aiguilleur": 0.031, "juge-opus": 0.037, "juge-argon": 0.0347}
DEVIS_V1_TOTAL = {"prop-argon+prop-fable+prop-opus": 22.3316, "prop-argon+prop-fable+prop-kimi+prop-opus": 25.9859,
                  "prop-argon+prop-astra+prop-fable+prop-kimi+prop-opus": 35.2199}

NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")
NOMS_DE_CLE = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY", "GOOGLE_API_KEY",
               "GEMINI_API_KEY", "KIMI_API_KEY", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN")
MOTIF_NOM_DE_CLE = re.compile(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)
MOTIF_VALEUR_DE_CLE = re.compile(r"(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|"
                                 r"AIza[0-9A-Za-z_-]{20,}|Bearer\s+[A-Za-z0-9._-]{16,})")
NOM_DE_VARIABLE = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
URL_LOCALE = re.compile(r"^http://(127\.0\.0\.1|localhost|\[::1\]):\d{2,5}(/.*)?$")
GO_FORME = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
TYPES_PERMIS = {"claude": "claude_sdk", "argon": "commande_externe", "kimi": "kimi_protocole", "astra": "commande_externe",
                "carbon": "commande_externe"}
CLES_PERMISES = {"claude_sdk": {"type", "url_relais", "porte_plafond"},
                 "commande_externe": {"type", "commande", "modeles_servis_permis", "porte_plafond"},
                 "kimi_protocole": {"type", "url_relais", "modele", "prix_entree", "prix_sortie", "max_sortie_jetons",
                                    "sortie_min_jetons", "delai_s", "porte_plafond"}}
CLES_META = {"nom_cle", "modele_propose", "inscription", "pid_relais", "url_etat_relais"}

SONDE_BAC_A_SABLE = (
    "import json, sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "from pole.adaptateurs import etat_bac_a_sable_detaille\n"
    "print(json.dumps(etat_bac_a_sable_detaille()))\n"
)

# --- règle des lots (découpage de la matière, sans jugement de valeur) ---------------------------------------------------------
LOT_TAILLE_MAX_OCTETS = 120_000
SECTIONS_EXIGEES = ("0", "1", "2", "3", "4", "5")
SECTIONS_COMMUNES = ("0", "4", "5", "11")
SECTIONS_MARGES = ("7", "8", "9", "10")
ETIQUETTES_INTERDITES_FIXES = ("Opus", "Fable", "Argon", "Astra", "Kimi", "Carbon")
MASQUE = "[nom retiré]"
TITRE_REGROUPEMENT = re.compile(r"^\*\*([^*]+? n° \d+ — [^*]+)\*\*\s*$")


class Refus(RuntimeError):
    """Garde du lanceur : rien n'est lancé (code 2)."""


class AlerteCredit(RuntimeError):
    """Un reste est sous un seuil ; alerte écrite, arrêt avant le départ (code 3)."""


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def date_u() -> str:
    r = subprocess.run(["date", "-u"], capture_output=True, text=True, timeout=10)
    if r.returncode != 0 or not r.stdout.strip():
        raise Refus("`date -u` illisible")
    return r.stdout.strip()


def _normaliser(texte: str) -> str:
    return unicodedata.normalize("NFKD", texte.lower()).encode("ascii", "ignore").decode()


def scelle(chemin: Path) -> bool:
    """Compagnon `.sha256` présent, une ligne « empreinte  nom », égal à l'empreinte du fichier."""
    c = Path(str(chemin) + ".sha256")
    if not chemin.is_file() or not c.is_file():
        return False
    lignes = [x for x in c.read_text(encoding="utf-8").splitlines() if x.strip()]
    if len(lignes) != 1:
        return False
    m = re.match(r"^([0-9a-f]{64})  (\S.*)$", lignes[0])
    return bool(m) and m.group(2) == chemin.name and m.group(1) == sha256_fichier(chemin)


def ecrire_scelle(chemin: Path, contenu) -> str:
    if chemin.exists():
        raise Refus(f"{chemin} existe déjà (R12)")
    if isinstance(contenu, (bytes, str)):
        donnees = contenu.encode("utf-8") if isinstance(contenu, str) else contenu
    else:
        donnees = (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = sha256_octets(donnees)
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


def _epingle(v) -> bool:
    return isinstance(v, str) and bool(re.fullmatch(r"[0-9a-f]{64}", v))


# --- lecture dans un commit nommé (constat 5) ----------------------------------------------------------------------------------


def _git(dossier: Path, *args: str, octets: bool = False):
    p = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True, timeout=120)
    if p.returncode != 0:
        raise Refus(f"git {' '.join(args)} dans {dossier} : code {p.returncode} ({p.stderr.decode('utf-8', 'replace').strip()[:200]})")
    return p.stdout if octets else p.stdout.decode("utf-8")


def lire_dans_main(depot: Path, chemin: str) -> tuple:
    """Rend (octets, commit) : le fichier lu à l'octet dans `refs/remotes/origin/main`, résolu au lancement."""
    commit = _git(depot, "rev-parse", "--verify", REF_MAIN).strip()
    return _git(depot, "show", f"{commit}:{chemin}", octets=True), commit


# --- règle des lots -----------------------------------------------------------------------------------------------------------


def _sections(texte: str) -> tuple:
    """Préambule (avant le premier « ## »), puis [(numéro ou None, titre, lignes)] par titre de niveau 2."""
    lignes = texte.split("\n")
    preambule, sections, cour = [], [], None
    for l in lignes:
        if l.startswith("## "):
            m = re.match(r"^## (\d+)\. ", l)
            cour = [m.group(1) if m else None, l, [l]]
            sections.append(cour)
        elif cour is None:
            preambule.append(l)
        else:
            cour[2].append(l)
    return preambule, sections


def _sous_sections(lignes: list) -> tuple:
    """Lignes d'une section de niveau 2 → (tête, [(titre ###, lignes)])."""
    tete, subs, cour = [], [], None
    for l in lignes:
        if l.startswith("### "):
            cour = [l, [l]]
            subs.append(cour)
        elif cour is None:
            tete.append(l)
        else:
            cour[1].append(l)
    return tete, subs


def _nom_famille(titre: str) -> str | None:
    m = re.match(r"^### Famille « (.+) »\s*$", titre)
    return m.group(1).strip() if m else None


def _nom_suggeres(titre: str) -> str:
    return re.sub(r"\s*\(\d+\)\s*$", "", titre[4:]).strip()


def masquer(texte: str, interdites=ETIQUETTES_INTERDITES_FIXES) -> tuple:
    """Remplace par `[nom retiré]` chaque étiquette interdite, en mot entier, sans tenir compte de la casse. Rend (texte, n)."""
    n = 0
    for e in interdites:
        texte, k = re.subn(r"(?<![0-9A-Za-zÀ-ÿ])" + re.escape(e) + r"(?![0-9A-Za-zÀ-ÿ])", MASQUE, texte, flags=re.I)
        n += k
    return texte, n


def decouper_matiere(octets: bytes, sha256: str) -> dict:
    """Règle écrite au préenregistrement, appliquée par programme, sans jugement de valeur :
    - **partie commune** (servie dans chaque case) : le préambule (titre, changements de version), les sections 0, 4, 5 et 11
      telles quelles, et l'**index** de tous les regroupements (chaque titre « <famille> n° <k> — … » de la pièce, une fois,
      dans l'ordre de la pièce) ;
    - **un lot par famille** de la section 1 (dans l'ordre de la pièce), avec la sous-section de même nom de la section 6
      (mécanismes suggérés par le titre, comptés à part) ;
    - un lot « machines » (section 2), un lot « hors machine » (section 3), un lot « autre et marges » (sous-sections de la
      section 6 sans famille de même nom, puis sections 7 à 10) ;
    - toute autre section de niveau 2 numérotée et non nommée ci-dessus (s'il en existe) : refus ;
    - **couverture vérifiée** : chaque ligne de la pièce est servie exactement une fois (partie commune ou un lot), l'index
      excepté (il recopie des titres) ;
    - étiquettes interdites (noms d'espèces) remplacées par « [nom retiré] », comptées ; un lot au-delà de 120 000 octets
      avec la partie commune : refus."""
    try:
        texte = octets.decode("utf-8")
    except UnicodeDecodeError:
        raise Refus("matière : UTF-8 invalide") from None
    preambule, sections = _sections(texte)
    par_num = {}
    for num, titre, lignes in sections:
        if num is None:
            par_num.setdefault("entete", []).append(lignes)
            continue
        if num in par_num:
            raise Refus(f"matière : section {num} en double")
        par_num[num] = lignes
    manque = [s for s in SECTIONS_EXIGEES if s not in par_num]
    if manque:
        raise Refus(f"matière : sections exigées absentes {manque} — la règle des lots ne s'applique pas")
    connues = set(SECTIONS_COMMUNES) | set(SECTIONS_MARGES) | {"1", "2", "3", "6"}
    inconnues = sorted(n for n in par_num if n != "entete" and n not in connues)
    if inconnues:
        raise Refus(f"matière : sections numérotées hors de la règle {inconnues}")
    commun_lignes = list(preambule)
    for bloc in par_num.get("entete", []):
        commun_lignes += bloc
    for s in SECTIONS_COMMUNES:
        commun_lignes += par_num.get(s, [])
    tete1, familles = _sous_sections(par_num["1"])
    tete6, suggeres = _sous_sections(par_num.get("6", []))
    sugg_par_nom = {_nom_suggeres(t): l for t, l in suggeres}
    lots, servis = [], []
    for titre, lignes in familles:
        nom = _nom_famille(titre)
        if nom is None:
            raise Refus(f"matière : sous-section de la section 1 hors du format « Famille « … » » : {titre!r}")
        corps = (tete1 if not lots else []) + lignes
        if nom in sugg_par_nom:
            corps = corps + [""] + (tete6 if not any(l["sugg"] for l in lots) else []) + sugg_par_nom[nom]
        lots.append({"nom": f"famille « {nom} »", "lignes": corps, "sugg": nom in sugg_par_nom})
        servis.append(nom)
    lots.append({"nom": "machines (section 2)", "lignes": list(par_num["2"]), "sugg": False})
    lots.append({"nom": "hors machine (section 3)", "lignes": list(par_num["3"]), "sugg": False})
    marges = []
    restes6 = [(t, l) for t, l in suggeres if _nom_suggeres(t) not in servis]
    if restes6:
        marges += (tete6 if not any(l["sugg"] for l in lots) else []) + [x for _, l in restes6 for x in l]
    elif tete6 and not any(l["sugg"] for l in lots):
        marges += tete6
    for s in SECTIONS_MARGES:
        marges += par_num.get(s, [])
    if marges:
        lots.append({"nom": "autre et marges (section 6 sans famille, sections 7 à 10)", "lignes": marges, "sugg": False})
    # couverture : chaque ligne servie exactement une fois
    servies = len(commun_lignes) + sum(len(l["lignes"]) for l in lots)
    total = len(texte.split("\n"))
    non_vides_servies = sorted(x for x in commun_lignes + [y for l in lots for y in l["lignes"]] if x.strip())
    non_vides_piece = sorted(x for x in texte.split("\n") if x.strip())
    if non_vides_servies != non_vides_piece:
        raise Refus("matière : couverture fausse (une ligne non vide servie zéro ou deux fois)")
    index, vus = [], set()
    for l in texte.split("\n"):
        m = TITRE_REGROUPEMENT.match(l)
        if m and m.group(1) not in vus:
            vus.add(m.group(1))
            index.append(f"- {m.group(1)}")
    commun_texte = ("\n".join(commun_lignes).strip() + "\n\n## Index de tous les regroupements du catalogue (titres seuls, "
                    "dans l'ordre de la pièce, chacun une fois)\n\n" + "\n".join(index) + "\n")
    commun_texte, n_commun = masquer(commun_texte)
    sortie = {"version": "lots-matiere-auto-conception-v1", "matiere_sha256": sha256, "regle": decouper_matiere.__doc__.strip(),
              "commun": {"texte": commun_texte, "octets": len(commun_texte.encode("utf-8")), "masques": n_commun,
                         "regroupements_indexes": len(index)},
              "lots": [], "couverture": {"lignes_piece": total, "lignes_servies": servies,
                                         "lignes_non_vides_toutes_servies_une_fois": True}}
    for k, l in enumerate(lots, 1):
        t, n = masquer("\n".join(l["lignes"]).strip() + "\n")
        octets_case = len(commun_texte.encode("utf-8")) + len(t.encode("utf-8"))
        if octets_case > LOT_TAILLE_MAX_OCTETS:
            raise Refus(f"matière : lot {l['nom']} de {octets_case} octets avec la partie commune > {LOT_TAILLE_MAX_OCTETS}")
        sortie["lots"].append({"rang": k, "nom": l["nom"], "texte": t, "octets": len(t.encode("utf-8")), "masques": n,
                               "octets_avec_commun": octets_case, "sha256": sha256_octets(t.encode("utf-8"))})
    return sortie


def texte_de_case(lots: dict, lot: dict) -> str:
    return (f"Lot {lot['rang']} sur {len(lots['lots'])} du catalogue des mécanismes publiés : {lot['nom']} "
            f"(catalogue sha256 {lots['matiere_sha256']}).\n\n"
            "### Partie commune à toutes les cases\n\n" + lots["commun"]["texte"] + "\n### Ton lot\n\n" + lot["texte"])


# --- réglages -----------------------------------------------------------------------------------------------------------------


@dataclass
class Reglages:
    depot: Path
    orchestrateurs: tuple
    commit_orchestrateur: str
    empreintes_orchestrateur: dict
    pieces: dict
    prereg: tuple
    contre_lecture: Path
    piece_de_depart: Path
    epreuve_reelle: Path
    declaration: Path
    releve: Path
    procedure_relais: Path
    releve_prix: Path
    dossier_runs: Path
    dossier_sorties: Path
    depot_attendu_par_l_enveloppe: Path
    python: str
    lanceur: Path
    matiere: tuple = MATIERE
    moteur: str = "reel"
    environnement: dict | None = None
    aujourd_hui: _dt.date | None = None
    horodatage: object = date_u
    exiger_bac_a_sable: bool = True
    programmes_relais: dict | None = None
    lire_cmdline: object = None
    lire_main: object = None          # (chemin) -> (octets, commit) ; défaut : `lire_dans_main`
    lire_etat_relais: object = None   # (url) -> dict ; défaut : GET sur la boucle locale
    verifier_go: bool = True

    @classmethod
    def production(cls) -> "Reglages":
        return cls(depot=DEPOT, orchestrateurs=ORCHESTRATEURS_CANDIDATS, commit_orchestrateur=COMMIT_ORCHESTRATEUR,
                   empreintes_orchestrateur=dict(EMPREINTES_ORCHESTRATEUR), pieces=dict(PIECES),
                   prereg=(DEPOT / PREREG, PREREG_SHA256), contre_lecture=DEPOT / CONTRE_LECTURE,
                   piece_de_depart=DEPOT / PIECE_DE_DEPART, epreuve_reelle=DEPOT / EPREUVE_REELLE,
                   declaration=DEPOT / DECLARATION_RELAIS, releve=DEPOT / RELEVE_CREDITS,
                   procedure_relais=DEPOT / PROCEDURE_RELAIS, releve_prix=DEPOT / RELEVE_PRIX, dossier_runs=DEPOT / "runs",
                   dossier_sorties=DOSSIER_SORTIES, depot_attendu_par_l_enveloppe=DEPOT_ATTENDU_PAR_L_ENVELOPPE,
                   python=sys.executable, lanceur=Path(__file__).resolve())

    def lire(self, chemin: str) -> tuple:
        return (self.lire_main or (lambda c: lire_dans_main(self.depot, c)))(chemin)


# --- (1) une seule course (constat 1), GO ----------------------------------------------------------------------------------


def nouvel_ident(r: Reglages) -> str:
    """Identifiant neuf : horodatage à la seconde ; si une tentative refusée de la même seconde a laissé son dossier de run
    (sans manifeste de départ), un rang est ajouté — jamais d'écrasement (R12), jamais de blocage (constat 1)."""
    base = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
    for k in range(1, 1000):
        ident = base + ("" if k == 1 else f"-{k}") + SUFFIXE_RUN
        if not (r.dossier_runs / ident).exists() and not (r.dossier_sorties / ident).exists():
            return ident
    raise Refus("aucun identifiant de run libre")


def verifier_course_jamais_lancee(r: Reglages) -> None:
    """Lancée = un manifeste de départ au dépôt, ou un journal de course hors dépôt. Un essai refusé avant le départ (dossier de
    run sans manifeste, ou rien hors dépôt) ne bloque rien : la garde ne se bloque pas elle-même (constat 1)."""
    if r.dossier_runs.is_dir():
        deja = sorted(p.name for p in r.dossier_runs.iterdir()
                      if p.name.endswith(SUFFIXE_RUN) and (p / "manifeste-lanceur-depart.json").exists())
        if deja:
            raise Refus(f"course déjà lancée ({deja}) : une relance est une nouvelle version et un mot de la mère")
    if r.dossier_sorties.is_dir():
        journaux = sorted(str(p) for p in r.dossier_sorties.glob("*/course.stdout.txt"))
        if journaux:
            raise Refus(f"journal d'une course déjà lancée hors dépôt : {journaux} — une seule course")


def _est_revocation(cellules: list, go_id: str) -> bool:
    return any(_normaliser(c).startswith("revoc") for c in cellules) and any(go_id in c for c in cellules)


def verifier_go(texte_registre: str, aujourd_hui: _dt.date, go_id: str, plafond_exige: float, mots_perimetre: tuple) -> dict:
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
    trouvees, revocations = [], []
    for ligne in texte_registre.splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif _est_revocation(cellules, go_id):
            revocations.append(m.group(1))
    principales = [c for c in trouvees if not (len(c) == 8 and c[3].lower().startswith("extension"))]
    if len(principales) != 1:
        raise Refus(f"{go_id} : {len(principales)} ligne(s) principale(s) dans le registre (une exigée)")
    c = principales[0]
    if len(c) != 8:
        raise Refus(f"{go_id} : ligne mal formée ({len(c)} colonnes, 8 attendues)")
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = c
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
    p = _normaliser(perimetre).replace("-", "")
    if not all(m in p for m in mots_perimetre):
        raise Refus(f"{go_id} : périmètre sans {mots_perimetre} — ce n'est pas le GO attendu")
    m_plafond = re.match(r"^\s*(\d+(?:[.,]\d+)?)\s*(?:USD|usd)\s*$", plafond)
    if not m_plafond:
        raise Refus(f"{go_id} : plafond illisible {plafond!r} (un nombre + USD attendu)")
    plafond_lu = float(m_plafond.group(1).replace(",", "."))
    if plafond_lu != plafond_exige:
        raise Refus(f"{go_id} : plafond lu {plafond_lu} USD != plafond exigé {plafond_exige} USD")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "plafond": plafond, "plafond_lu": plafond_lu, "par": par,
            "ligne_sha256": sha256_octets(("|".join(c)).encode("utf-8"))}


def lire_registre(r: Reglages) -> dict:
    octets, commit = r.lire("registres/go.md")
    return {"texte": octets.decode("utf-8"), "commit": commit, "sha256": sha256_octets(octets)}


def ecrire_registre_derive(registre: dict, chemin: Path, go_id: str) -> dict:
    """Constat 5 : registre dérivé (ligne du GO et révocations qui la visent, lignes nommées seulement), qui cite le commit
    source et l'empreinte du registre source."""
    gardees = []
    for ligne in registre["texte"].splitlines():
        m = re.match(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|", ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id and not (len(cellules) == 8 and cellules[3].lower().startswith("extension")):
            gardees.append(ligne)
        elif len(cellules) == 8 and cellules[2] == "révocation" and go_id in (cellules[3] + cellules[7]):
            gardees.append(ligne)
    texte = (f"# Registre des GO dérivé (course d'auto-conception, lanceur v1) — lignes nommées seulement\n\n"
             f"Source : `registres/go.md` au commit `{registre['commit']}` ({REF_MAIN}), sha256 `{registre['sha256']}`.\n\n"
             "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
             "|---|---|---|---|---|---|---|---|\n" + "\n".join(gardees) + "\n")
    h = ecrire_scelle(chemin, texte)
    return {"source": "registres/go.md", "commit_source": registre["commit"], "source_sha256": registre["sha256"],
            "derive": str(chemin), "derive_sha256": h, "lignes": [sha256_octets(l.encode("utf-8")) for l in gardees],
            "nombre_de_lignes": len(gardees)}


# --- (2) pièces : préenregistrement, contre-lecture, pièce de départ, matière, épreuve des témoins ------------------------------


def verifier_preenregistrement(r: Reglages) -> dict:
    chemin, attendu = r.prereg
    if not _epingle(attendu):
        raise Refus("empreinte du préenregistrement non posée dans le lanceur : aucun lancement")
    if not chemin.is_file():
        raise Refus(f"préenregistrement absent : {chemin}")
    lu = sha256_fichier(chemin)
    if lu != attendu:
        raise Refus(f"préenregistrement d'empreinte {lu}, {attendu} épinglée")
    if not scelle(chemin):
        raise Refus("préenregistrement non scellé (compagnon .sha256 absent ou faux)")
    return {"chemin": str(chemin.relative_to(r.depot)) if chemin.is_relative_to(r.depot) else str(chemin), "sha256": lu}


def lire_verdict(texte: str) -> str | None:
    lignes = texte.splitlines()
    for i, l in enumerate(lignes):
        if re.match(r"^#{1,3}\s*Verdict\b", l.strip()):
            for suite in lignes[i + 1:]:
                if suite.strip():
                    return suite.strip()
    return None


VERDICTS_EXACTS = ("Scellable.", "**Scellable.**")
AVEUX_NON_RELU = re.compile(r"(n'ai pas (re)?lu|pas (ete )?relu|non relu|sans (la )?relire|sans relecture|n'a pas (ete )?(re)?lu|"
                            r"lecture partielle du (preenregistrement|lanceur)|pas pu (re)?lire)")


def verdict_favorable(verdict: str | None) -> bool:
    return isinstance(verdict, str) and verdict.strip() in VERDICTS_EXACTS


def verifier_contre_lecture(r: Reglages, prereg_sha: str, lanceur_sha: str) -> dict:
    c = r.contre_lecture
    if not c.is_file():
        raise Refus(f"contre-lecture absente : {c} (R2 : aucun lancement sans contre-lecture scellée)")
    if not scelle(c):
        raise Refus("contre-lecture non scellée (compagnon .sha256 absent ou faux)")
    texte = c.read_text(encoding="utf-8")
    if prereg_sha not in texte:
        raise Refus("la contre-lecture ne cite pas l'empreinte du préenregistrement épinglé")
    if lanceur_sha not in texte:
        raise Refus("la contre-lecture ne cite pas l'empreinte de ce lanceur (elle n'a pas lu cette version)")
    v = lire_verdict(texte)
    if not verdict_favorable(v):
        raise Refus(f"verdict de la contre-lecture défavorable, illisible ou inexact : {v!r} (première ligne exacte « Scellable. » exigée)")
    if "modele k" not in _normaliser(texte):
        raise Refus("la contre-lecture ne dit pas être du modèle K (contre-lecteur attendu)")
    aveu = AVEUX_NON_RELU.search(_normaliser(texte).replace("’", "'"))
    if aveu:
        raise Refus(f"la contre-lecture dit n'avoir pas relu ({aveu.group(0)!r}) : refusée")
    return {"chemin": str(c), "sha256": sha256_fichier(c), "verdict": v}


def verifier_pieces(r: Reglages) -> dict:
    if r.moteur == "reel" and r.depot.resolve() != r.depot_attendu_par_l_enveloppe.resolve():
        raise Refus(f"dépôt de travail en {r.depot}, l'enveloppe d'Argon v5 attend {r.depot_attendu_par_l_enveloppe}")
    lues, ecarts = {}, {}
    for nom, (rel, attendu) in sorted(r.pieces.items()):
        p = r.depot / rel
        lu = sha256_fichier(p) if p.is_file() else None
        if lu != attendu:
            ecarts[nom] = {"chemin": rel, "attendu": attendu, "lu": lu}
        lues[nom] = {"chemin": rel, "absolu": str(p), "sha256": lu}
    if ecarts:
        raise Refus("pièces absentes ou d'empreinte différente (R11) : " + json.dumps(ecarts, ensure_ascii=False))
    return lues


def lire_json_scelle(chemin: Path, quoi: str) -> tuple:
    if not chemin.is_file():
        raise Refus(f"{quoi} absent : {chemin}")
    if not scelle(chemin):
        raise Refus(f"{quoi} non scellé (compagnon .sha256 absent ou faux) : {chemin}")
    brut = chemin.read_text(encoding="utf-8")
    if MOTIF_VALEUR_DE_CLE.search(brut):
        raise Refus(f"{quoi} : une chaîne de la forme d'une valeur de clé y figure — refus, rien n'est lu ni recopié")
    if MARQUEUR_A_REMPLIR in brut:
        raise Refus(f"{quoi} : « {MARQUEUR_A_REMPLIR} » y figure encore — pièce non remplie")
    try:
        return json.loads(brut), sha256_fichier(chemin)
    except ValueError:
        raise Refus(f"{quoi} : JSON illisible") from None


def _reel_positif(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and v >= 0


def verifier_piece_de_depart(r: Reglages) -> dict:
    """Pièce scellée par la mère : identifiants des deux GO, nom de la variable de clé Claude, crédit déclaré, réserve de la clé
    de Kimi, commandes d'Astra et de Carbon (empreintes et référence de leur épreuve) ; « À REMPLIR » refusé."""
    o, h = lire_json_scelle(r.piece_de_depart, "pièce de départ de la mère")
    if o.get("par") != "mère":
        raise Refus("pièce de départ : « par » = « mère » exigé")
    for k in ("go_course", "go_epreuve"):
        if not isinstance(o.get(k), str) or not GO_FORME.match(o[k]):
            raise Refus(f"pièce de départ : {k} (GO-AAAA-MM-JJ-NN) exigé")
    if o["go_course"] == o["go_epreuve"]:
        raise Refus("pièce de départ : la course et l'épreuve des témoins ont chacune leur ligne de GO")
    cle = o.get("variable_cle_claude")
    if not isinstance(cle, str) or not NOM_DE_VARIABLE.match(cle) or not cle.startswith(PREFIXE_CLES_CLAUDE):
        raise Refus(f"pièce de départ : variable_cle_claude, nom de variable en {PREFIXE_CLES_CLAUDE}… exigé (le nom seul)")
    if cle in CLES_CLAUDE_RESERVEES:
        raise Refus(f"pièce de départ : {cle} est réservée à la course d'affinage — une autre clé Claude est exigée")
    credit = o.get("credit_declare_cle_claude_usd")
    if not (_reel_positif(credit) and credit > 0):
        raise Refus("pièce de départ : credit_declare_cle_claude_usd (nombre > 0) exigé")
    if not _reel_positif(o.get("reserve_cle_kimi_usd")):
        raise Refus("pièce de départ : reserve_cle_kimi_usd (nombre ≥ 0 : ce qui doit rester sur la clé de Kimi) exigé")
    cmds = o.get("commandes_epinglees") or {}
    if set(cmds) - {"astra", "carbon"}:
        raise Refus("pièce de départ : commandes_epinglees n'admet que astra et carbon")
    for nom, c in cmds.items():
        if not (isinstance(c, dict) and isinstance(c.get("empreintes"), list) and c["empreintes"]
                and all(_epingle(x) for x in c["empreintes"]) and isinstance(c.get("epreuve"), str) and c["epreuve"].strip()):
            raise Refus(f"pièce de départ : commandes_epinglees.{nom} = {{empreintes: [sha256…], epreuve: référence}} exigé")
    return dict(o, sha256=h, chemin=str(r.piece_de_depart))


def verifier_matiere(r: Reglages) -> dict:
    chemin, attendu = r.matiere
    octets, commit = r.lire(chemin)
    lu = sha256_octets(octets)
    if lu != attendu:
        raise Refus(f"matière {chemin} au commit {commit} : empreinte {lu}, {attendu} épinglée (R-3263) — aucune autre servie")
    return {"chemin": chemin, "commit": commit, "sha256": lu, "octets": octets}


def verifier_epreuve_reelle(r: Reglages, pieces: dict, fixe: dict, depart: dict, aujourd_hui: _dt.date, lanceur_sha: str) -> dict:
    """Rien ne part sans l'épreuve réelle des témoins réussie (R-3229) : rapport scellé, du jour, moteur réel, au GO de
    l'épreuve, aux pièces épinglées (témoins, consignes, programme d'épreuve, orchestrateur), juges et aiguilleur de la
    configuration, verdict « réussie »."""
    o, h = lire_json_scelle(r.epreuve_reelle, "rapport de l'épreuve réelle des témoins")
    if o.get("moteur") != "reel":
        raise Refus("épreuve des témoins : moteur réel exigé (l'épreuve hors ligne ne suffit pas)")
    if o.get("verdict") != "réussie":
        raise Refus(f"épreuve des témoins : verdict {o.get('verdict')!r} — aucune course (R-3229 : aucune retouche des témoins "
                    "sans version neuve)")
    if not str(o.get("horodatage_utc") or "").startswith(aujourd_hui.isoformat()):
        raise Refus("épreuve des témoins : rapport du jour exigé")
    if (o.get("go") or {}).get("id") != depart["go_epreuve"]:
        raise Refus("épreuve des témoins : jouée sous un autre GO que celui de la pièce de départ")
    attendus = {"temoins": pieces["temoins"]["sha256"], "consigne_juge": pieces["consigne_juge"]["sha256"],
                "consigne_aiguilleur": pieces["consigne_aiguilleur"]["sha256"], "programme": pieces["epreuve_temoins"]["sha256"],
                "lanceur": lanceur_sha, "orchestrateur_commit": r.commit_orchestrateur}
    lus = o.get("empreintes") or {}
    ecarts = {k: (lus.get(k), v) for k, v in attendus.items() if lus.get(k) != v}
    if ecarts:
        raise Refus(f"épreuve des témoins : pièces d'une autre empreinte {ecarts}")
    juges = sorted((j["etiquette"], j["modele"]) for j in fixe["juges"])
    if sorted(tuple(x) for x in (o.get("juges") or [])) != juges:
        raise Refus("épreuve des témoins : juges différents de ceux de la configuration")
    a = fixe["aiguilleur"]
    if tuple(o.get("aiguilleur") or ()) != (a["etiquette"], a["modele"]):
        raise Refus("épreuve des témoins : aiguilleur différent de celui de la configuration")
    return {"chemin": str(r.epreuve_reelle), "sha256": h, "verdict": o["verdict"], "cout_usd": o.get("cout_usd"),
            "horodatage_utc": o.get("horodatage_utc")}


# --- (3) déclaration des relais, relais vivants ---------------------------------------------------------------------------------


def _cmdline(pid: int) -> list:
    with open(f"/proc/{int(pid)}/cmdline", "rb") as f:
        return [x.decode("utf-8", "replace") for x in f.read().split(b"\0") if x]


def _valeur_arg(args: list, nom: str):
    return args[args.index(nom) + 1] if nom in args and args.index(nom) + 1 < len(args) else None


def _valeurs_arg(args: list, nom: str) -> list:
    return [args[i + 1] for i, a in enumerate(args) if a == nom and i + 1 < len(args)]


def lire_etat_local(url: str) -> dict:
    import urllib.request
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with ouvreur.open(url.rstrip("/") + "/relais/etat", timeout=5) as rep:
        return json.loads(rep.read().decode("utf-8"))


def modeles_claude_de_la_configuration(fixe: dict) -> list:
    roles = [e for e in fixe["especes"] if e["famille"] == "claude"] + [fixe["aiguilleur"]] + list(fixe["juges"]) \
        + list(fixe["lecteurs_etiquettes"])
    return sorted({x["modele"] for x in roles if x.get("fournisseur", "claude") == "claude" and x.get("modele")})


def appels_argon_au_pire(fixe: dict, n_cases: int, especes_actives: list, cartes_max: int) -> int:
    """Appels d'Argon au pire dans la course : proposeur (une par case) + juge (une par carte, au plus `cartes_max` cartes
    par appel de proposeur, toutes espèces) + lecteurs (aucun appel en pratique : aucun bras)."""
    n_prop = n_cases * sum(1 for e in especes_actives if e["fournisseur"] == "argon")
    n_cartes = n_cases * len(especes_actives) * cartes_max
    n_juges = n_cartes * sum(1 for j in fixe["juges"] if j["fournisseur"] == "argon")
    return n_prop + n_juges


def verifier_declaration(decl: dict, fixe: dict, depart: dict) -> dict:
    """Rend {fournisseurs (blocs de l'orchestrateur), especes_actives, especes_absentes, cles, metas}."""
    f_decl = decl.get("fournisseurs")
    if not isinstance(f_decl, dict):
        raise Refus("déclaration des relais : « fournisseurs » (objet) exigé")
    inconnus = sorted(set(f_decl) - set(TYPES_PERMIS))
    if inconnus:
        raise Refus(f"déclaration des relais : fournisseurs inconnus {inconnus}")
    for requis in ("claude", "argon"):
        if requis not in f_decl:
            raise Refus(f"déclaration des relais : « {requis} » exigé (Claude d'abord ; juge Argon)")
    cle_claude = depart["variable_cle_claude"]
    epingles = depart.get("commandes_epinglees") or {}
    blocs, cles, modeles, metas = {}, {}, {}, {}
    for nom, b in sorted(f_decl.items()):
        if not isinstance(b, dict):
            raise Refus(f"fournisseurs.{nom} : objet attendu")
        t = TYPES_PERMIS[nom]
        if b.get("type") != t:
            raise Refus(f"fournisseurs.{nom}.type : {t!r} exigé (reçu {b.get('type')!r})")
        en_trop = sorted(set(b) - CLES_PERMISES[t] - CLES_META)
        if en_trop:
            raise Refus(f"fournisseurs.{nom} : clés non permises {en_trop}")
        nom_cle = b.get("nom_cle")
        if not isinstance(nom_cle, str) or not NOM_DE_VARIABLE.match(nom_cle):
            raise Refus(f"fournisseurs.{nom}.nom_cle : nom de variable exigé (le nom seul, jamais la valeur)")
        if nom_cle in CLES_CLAUDE_RESERVEES:
            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : clé réservée à la course d'affinage")
        if nom == "claude" and nom_cle != cle_claude:
            raise Refus(f"fournisseurs.claude.nom_cle = {nom_cle} : la pièce de départ de la mère nomme {cle_claude}")
        if nom != "claude" and nom_cle.startswith(PREFIXE_CLES_CLAUDE):
            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : une clé de la famille Claude sur un autre relais est refusée")
        pp = b.get("porte_plafond")
        if not isinstance(pp, dict) or pp.get("type") not in ("commande", "environnement"):
            raise Refus(f"fournisseurs.{nom}.porte_plafond : {{type: commande|environnement}} exigé")
        if t == "commande_externe" and pp["type"] != "environnement":
            raise Refus(f"fournisseurs.{nom}.porte_plafond : « environnement » exigé pour une commande externe")
        if t != "commande_externe":
            if pp["type"] != "commande" or not isinstance(pp.get("commande"), list) or not pp["commande"] \
                    or not all(isinstance(x, str) and x for x in pp["commande"]):
                raise Refus(f"fournisseurs.{nom}.porte_plafond : commande (liste non vide) exigée pour un relais persistant")
            if not isinstance(pp.get("delai_s"), (int, float)) or isinstance(pp.get("delai_s"), bool) or pp["delai_s"] <= 0:
                raise Refus(f"fournisseurs.{nom}.porte_plafond.delai_s : nombre > 0 exigé")
            if not isinstance(b.get("url_relais"), str) or not URL_LOCALE.match(b["url_relais"]):
                raise Refus(f"fournisseurs.{nom}.url_relais : adresse de boucle locale exigée (http://127.0.0.1:PORT)")
        if nom == "argon":
            if not isinstance(b.get("url_etat_relais"), str) or not URL_LOCALE.match(b["url_etat_relais"]) \
                    or not b["url_etat_relais"].endswith(":" + PORT_RELAIS_ARGON):
                raise Refus(f"fournisseurs.argon.url_etat_relais : http://127.0.0.1:{PORT_RELAIS_ARGON} exigé (relais de l'enveloppe)")
        if nom in ("astra", "carbon"):
            m = b.get("modele_propose")
            motif = next(e.get("motif_modele") for e in fixe["especes"] if e["fournisseur"] == nom)
            if not isinstance(m, str) or motif not in m.lower() or "claude" in m.lower() or not re.fullmatch(r"[a-z0-9.\-]+", m):
                raise Refus(f"fournisseurs.{nom}.modele_propose : identifiant de modèle qui contient « {motif} » exigé")
            if not isinstance(b.get("commande"), list) or not b["commande"]:
                raise Refus(f"fournisseurs.{nom}.commande : liste non vide exigée")
            fichiers = [x for x in b["commande"] if isinstance(x, str) and os.path.isfile(x) and not x.startswith(("/usr/", "/bin/"))]
            permis = set((epingles.get(nom) or {}).get("empreintes") or [])
            if not fichiers or any(sha256_fichier(Path(x)) not in permis for x in fichiers):
                raise Refus(f"fournisseurs.{nom}.commande : programme non épinglé par la pièce de départ de la mère — l'espèce "
                            f"{nom} ne part qu'avec une commande épinglée et éprouvée")
            modeles[nom] = m
        if nom == "kimi":
            if b.get("modele") != "kimi-k3.1-pro":
                raise Refus("fournisseurs.kimi.modele : « kimi-k3.1-pro » exigé (configuration fixe)")
            controler_kimi(b)
        if "inscription" in b and nom != "carbon":
            raise Refus(f"fournisseurs.{nom}.inscription : clé réservée à Carbon")
        blocs[nom] = {k: v for k, v in b.items() if k not in CLES_META}
        metas[nom] = {k: v for k, v in b.items() if k in CLES_META}
        cles[nom] = nom_cle
    actives, absentes = [], []
    for e in sorted(fixe["especes"], key=lambda x: x["ordre"]):
        if e["fournisseur"] in blocs:
            actives.append(dict(e, modele=e["modele"] or modeles[e["fournisseur"]]))
        else:
            absentes.append({"etiquette": e["etiquette"], "motif": "relais non déclaré (ou commande non épinglée)"})
    return {"fournisseurs": blocs, "especes_actives": actives, "especes_absentes": absentes, "cles": cles, "metas": metas}


def controler_kimi(bloc: dict) -> None:
    for k in ("prix_entree", "prix_sortie", "delai_s"):
        v = bloc.get(k)
        if not (isinstance(v, (int, float)) and not isinstance(v, bool) and v > 0):
            raise Refus(f"fournisseurs.kimi.{k} : réel > 0 exigé, comme l'adaptateur de Kimi")
    for k in ("max_sortie_jetons", "sortie_min_jetons"):
        v = bloc.get(k)
        if not (isinstance(v, int) and not isinstance(v, bool) and v >= 1):
            raise Refus(f"fournisseurs.kimi.{k} : entier ≥ 1 exigé, comme l'adaptateur de Kimi")
    if bloc["sortie_min_jetons"] > bloc["max_sortie_jetons"]:
        raise Refus("fournisseurs.kimi : sortie_min_jetons > max_sortie_jetons")


def controler_relais_vivant(r: Reglages, nom: str, b: dict, plafond_ligne_exige: float | None) -> dict:
    """Arguments du relais lus par PID (jamais son environnement) : programme épinglé par la procédure, variable de la clé
    déclarée, port de l'adresse déclarée, plafond (Claude : égal au plafond d'arrêt ; Kimi : ≤)."""
    pid = b.get("pid_relais")
    if not isinstance(pid, int) or isinstance(pid, bool) or pid <= 1:
        raise Refus(f"fournisseurs.{nom}.pid_relais : PID du relais vivant exigé (lancé par le lanceur de relais)")
    try:
        args = (r.lire_cmdline or _cmdline)(pid)
    except OSError:
        raise Refus(f"relais {nom} : PID {pid} absent") from None
    nom_prog, attendu = (r.programmes_relais or PROGRAMMES_RELAIS)[nom]
    progs = [a for a in args if os.path.basename(a) == nom_prog]
    if len(progs) != 1 or not os.path.isfile(progs[0]) or sha256_fichier(Path(progs[0])) != attendu:
        raise Refus(f"relais {nom} : programme {nom_prog} absent des arguments ou d'une autre empreinte que celle de la procédure")
    url = b.get("url_relais") if nom != "argon" else b.get("url_etat_relais")
    port = re.search(r":(\d+)", url or "")
    if not port or _valeur_arg(args, "--port") != port.group(1):
        raise Refus(f"relais {nom} : port des arguments différent de l'adresse déclarée")
    sortie = {"pid": pid, "programme": progs[0], "programme_sha256": attendu, "port": port.group(1)}
    if nom == "argon":
        modeles = _valeurs_arg(args, "--modele")
        if modeles and modeles != [MODELE_ARGON]:
            raise Refus(f"relais argon : modèles {modeles} ({MODELE_ARGON} seul exigé)")
        if (_valeur_arg(args, "--variable-cle") or "GEMINI_API_KEY") != b["nom_cle"]:
            raise Refus(f"relais argon : lancé sur une autre variable que {b['nom_cle']}")
        try:
            sortie["max_appels"] = int(_valeur_arg(args, "--max-appels"))
        except (TypeError, ValueError):
            raise Refus("relais argon : --max-appels absent des arguments") from None
        return sortie
    if _valeur_arg(args, "--variable-cle") != b["nom_cle"]:
        raise Refus(f"relais {nom} : lancé sur la variable {_valeur_arg(args, '--variable-cle')!r}, {b['nom_cle']} déclarée")
    try:
        plafond = float(_valeur_arg(args, "--plafond-usd"))
    except (TypeError, ValueError):
        raise Refus(f"relais {nom} : --plafond-usd absent des arguments") from None
    if plafond > PLAFOND_ARRET_USD or (plafond_ligne_exige is not None and plafond != plafond_ligne_exige):
        raise Refus(f"relais {nom} : plafond {plafond} hors règle (≤ {PLAFOND_ARRET_USD} ; Claude : égal, relais de ligne entière)")
    sortie.update(variable_cle=b["nom_cle"], plafond_usd=plafond)
    return sortie


def controler_relais_argon(r: Reglages, b: dict, meta: dict, appels_requis: int) -> dict:
    """Constat 4 : relais Gemini d'Argon contrôlé avant le départ (PID et état lu sur la boucle locale)."""
    vivant = controler_relais_vivant(r, "argon", dict(b, **meta), None)
    if vivant["max_appels"] < appels_requis:
        raise Refus(f"relais argon : --max-appels {vivant['max_appels']} < {appels_requis} appels au pire de la course")
    try:
        etat = (r.lire_etat_relais or lire_etat_local)(meta["url_etat_relais"])
    except Exception as e:  # noqa: BLE001
        raise Refus(f"relais argon : état illisible ({type(e).__name__})") from None
    if not isinstance(etat, dict) or etat.get("appels") != 0 or etat.get("variable_cle_encore_presente") is not False:
        raise Refus(f"relais argon : relais neuf (0 appel) et variable de clé effacée exigés ; lu {etat!r}"[:300])
    if etat.get("max_appels") is not None and etat.get("max_appels") != vivant["max_appels"]:
        raise Refus("relais argon : max_appels de l'état différent de celui des arguments")
    return dict(vivant, etat={k: etat.get(k) for k in ("appels", "max_appels", "variable_cle_encore_presente")})


def verifier_procedure_relais(r: Reglages, decl: dict, pieces: dict, fixe: dict, appels_argon: int,
                              plafond_ligne: float = PLAFOND_ARRET_USD) -> dict:
    """Pièce de la procédure épinglée ; commande de chaque porte « commande » = interpréteur + porte épinglée, et ses
    arguments recoupés (constat 2) ; chaque relais vivant contrôlé par PID ; relais d'Argon contrôlé (constat 4)."""
    o = json.loads(Path(pieces["procedure_relais"]["absolu"]).read_text(encoding="utf-8"))
    for cle_chemin, cle_sha, piece in (("chemin", "sha256", "lanceur_relais"), ("procedure_ecrite", "procedure_ecrite_sha256", "procedure_ecrite")):
        if o.get(cle_sha) != pieces[piece]["sha256"]:
            raise Refus(f"pièce de la procédure : {cle_chemin} d'une autre empreinte que la pièce épinglée {piece}")
    porte = pieces["porte_plafond"]["absolu"]
    relais = {}
    claude_modeles = modeles_claude_de_la_configuration(fixe)
    for nom, b in sorted(decl["fournisseurs"].items()):
        meta = decl.get("metas", {}).get(nom, {})
        pp = b.get("porte_plafond") or {}
        if pp.get("type") != "commande":
            continue
        c = pp.get("commande") or []
        if len(c) < 4 or not os.path.isabs(c[0]) or c[1:3] != ["-I", "-B"] or c[3] != porte:
            raise Refus(f"fournisseurs.{nom}.porte_plafond : la commande doit commencer par « python -I -B {porte} »")
        vivant = controler_relais_vivant(r, nom, dict(b, **meta), plafond_ligne if nom == "claude" else None)
        attendus = {"--url": b["url_relais"].rstrip("/"),
                    "--modeles-permis": claude_modeles if nom == "claude" else ["kimi-k3.1-pro"],
                    "--plafond-ligne": plafond_ligne if nom == "claude" else vivant["plafond_usd"]}
        lus_url = (_valeur_arg(c, "--url") or "").rstrip("/")
        lus_mod = sorted(m.strip() for m in (_valeur_arg(c, "--modeles-permis") or "").split(",") if m.strip())
        try:
            lus_pl = float(_valeur_arg(c, "--plafond-ligne"))
        except (TypeError, ValueError):
            lus_pl = None
        if lus_url != attendus["--url"] or lus_mod != sorted(attendus["--modeles-permis"]) or lus_pl != attendus["--plafond-ligne"]:
            raise Refus(f"fournisseurs.{nom}.porte_plafond : --url, --modeles-permis ou --plafond-ligne différents de la "
                        f"déclaration et de la configuration (constat 2) : attendu {attendus}")
        relais[nom] = vivant
    relais["argon"] = controler_relais_argon(r, decl["fournisseurs"]["argon"], decl["metas"]["argon"], appels_argon)
    return {"procedure": o.get("procedure_ecrite"), "lanceur_relais": o.get("chemin"), "porte": porte, "relais_vivants": relais}


def porte_a_blanc(decl: dict) -> dict:
    """Chaque porte « commande » jouée une fois avant le manifeste de départ (étape « porte-a-blanc »), accusé au centime."""
    sortie = {}
    for nom, b in sorted(decl["fournisseurs"].items()):
        pp = b.get("porte_plafond") or {}
        if pp.get("type") != "commande":
            continue
        env = {"PATH": os.environ.get("PATH", os.defpath), "LANG": "C.UTF-8", "ETAPE_POLE": ETAPE_A_BLANC,
               "PLAFOND_ETAPE_USD": "1.00"}
        try:
            p = subprocess.run(pp["commande"], env=env, capture_output=True, text=True, timeout=float(pp["delai_s"]),
                               stdin=subprocess.DEVNULL)
        except (OSError, subprocess.SubprocessError) as e:
            raise Refus(f"porte à blanc de {nom} non jouée ({type(e).__name__})") from None
        lignes = [x for x in p.stdout.splitlines() if x.strip()]
        try:
            accuse = json.loads(lignes[-1]) if lignes else None
        except ValueError:
            accuse = None
        if p.returncode != 0 or not isinstance(accuse, dict) or accuse.get("etape") != ETAPE_A_BLANC \
                or round(float(accuse.get("plafond_usd") or -1), 2) != 1.00:
            raise Refus(f"porte à blanc de {nom} refusée (code {p.returncode}) : {(p.stderr or p.stdout).strip()[-300:]!r}")
        sortie[nom] = {"accuse": accuse, "code": 0}
    return sortie


# --- (4) crédits ------------------------------------------------------------------------------------------------------------


def borne_appel_kimi(bloc: dict, octets_entree_max: int, plafond_session: float) -> float:
    for k in ("prix_entree", "prix_sortie", "max_sortie_jetons"):
        if not _reel_positif(bloc.get(k)):
            raise Refus(f"fournisseurs.kimi.{k} : nombre ≥ 0 exigé pour la part au pire")
    brut = ((octets_entree_max + 1024) * bloc["prix_entree"] + bloc["max_sortie_jetons"] * bloc["prix_sortie"]) / 1e6
    return round(min(brut, plafond_session), 6)


def parts_au_pire(fixe: dict, n_cases: int, entree_max: int, decl: dict) -> dict:
    """Part au pire de chaque relais (règle de clé par part, R-3237 point 1) : relais qui tient l'aiguilleur ou un juge →
    plafond d'arrêt (cartes non bornées par programme) ; relais de proposeur seulement → cases × espèces × pire coût d'un
    appel (plafond de session ; pour Kimi, la formule de son adaptateur si elle est plus basse)."""
    actives = decl["especes_actives"]
    ps = fixe["plafonds_session"]
    internes = {fixe["aiguilleur"]["fournisseur"]} | {j["fournisseur"] for j in fixe["juges"]}
    parts = {}
    for f in sorted({e["fournisseur"] for e in actives} | internes):
        if f in internes:
            parts[f] = {"part_au_pire_usd": PLAFOND_ARRET_USD, "regle": "aiguilleur ou juge : cartes non bornées, plafond d'arrêt"}
            continue
        n = n_cases * sum(1 for e in actives if e["fournisseur"] == f)
        par_appel = float(ps["proposeur"])
        regle = f"{n} appels × plafond de session {par_appel}"
        if f == "kimi":
            par_appel = borne_appel_kimi(decl["fournisseurs"]["kimi"], entree_max, float(ps["proposeur"]))
            regle = f"{n} appels × pire coût d'un appel de Kimi (formule de son adaptateur, entrée ≤ {entree_max} octets)"
        parts[f] = {"part_au_pire_usd": round(min(n * par_appel, PLAFOND_ARRET_USD), 6), "par_appel_usd": par_appel, "regle": regle}
    return parts


def verifier_credits(releve: dict, cles: dict, aujourd_hui: _dt.date, dossier_alerte: Path, parts: dict, depart: dict) -> dict:
    """Relevé du jour ; chaque clé employée y figure. Clé Claude illisible : comptée au crédit déclaré par la pièce de départ
    moins la dépense antérieure déclarée. Argon, Astra, Carbon illisibles : seulement sous la dispense écrite de la mère
    (R-3237), arrêt au premier refus pour crédit. Lisible : alerte et arrêt (code 3) si reste ≤ part au pire, reste < un
    cinquième du crédit, ou (Kimi) part au pire + réserve déclarée > 90 % du reste."""
    quand = str(releve.get("releve_utc") or "")
    if not quand.startswith(aujourd_hui.isoformat()):
        raise Refus(f"relevé des crédits du {quand!r} : un relevé du jour ({aujourd_hui}) est exigé")
    lignes = releve.get("cles")
    if not isinstance(lignes, dict):
        raise Refus("relevé des crédits : « cles » (objet) exigé")
    dispense = releve.get("dispense") or {}
    dispensees = set(dispense.get("cles") or []) if dispense.get("par") == "mère" and dispense.get("reference") == REFERENCE_DISPENSE else set()
    cle_claude, credit_claude = depart["variable_cle_claude"], float(depart["credit_declare_cle_claude_usd"])
    reserve_kimi = float(depart["reserve_cle_kimi_usd"])
    sortie, alertes = {}, []
    for fournisseur, nom in sorted(cles.items()):
        x = lignes.get(nom)
        part = (parts.get(fournisseur) or {}).get("part_au_pire_usd")
        if nom == cle_claude and isinstance(x, dict) and x.get("non_lisible") is True:
            anterieure = x.get("depense_anterieure_usd")
            if not _reel_positif(anterieure):
                raise Refus(f"crédit de {nom} non lisible : depense_anterieure_usd (≥ 0) exigée pour le compter au prix relevé")
            x = {"credit_usd": credit_claude, "reste_usd": max(0.0, credit_claude - anterieure),
                 "source": "compté au prix relevé : crédit déclaré par la pièce de départ moins la dépense antérieure déclarée"}
        if not isinstance(x, dict):
            raise Refus(f"relevé des crédits : clé {nom} ({fournisseur}) absente — « non lisible » s'écrit, il ne s'omet pas")
        if x.get("non_lisible") is True:
            if fournisseur not in FOURNISSEURS_DISPENSABLES:
                raise Refus(f"crédit de la clé {nom} ({fournisseur}) non lisible : seules les clés d'Argon, d'Astra et de Carbon "
                            "peuvent partir sous dispense (R-3237)")
            if nom not in dispensees:
                raise Refus(f"crédit de la clé {nom} ({fournisseur}) non lisible et sans dispense écrite de la mère citant "
                            f"{REFERENCE_DISPENSE} : aucun départ")
            sortie[nom] = {"fournisseur": fournisseur, "lisible": False, "motif": x.get("motif"), "dispense": dispense,
                           "part_au_pire_usd": part, "regle": "arrêt de la course au premier refus pour crédit (R-3237)"}
            continue
        credit, reste = x.get("credit_usd"), x.get("reste_usd")
        if not (_reel_positif(credit) and _reel_positif(reste)) or reste > credit:
            raise Refus(f"relevé des crédits : clé {nom} : credit_usd et reste_usd (nombres ≥ 0, reste ≤ crédit) exigés")
        if part is None:
            raise Refus(f"part au pire du relais {fournisseur} inconnue : aucun départ")
        d = {"fournisseur": fournisseur, "lisible": True, "credit_usd": credit, "reste_usd": reste, "source": x.get("source"),
             "part_au_pire_usd": part, "cinquieme_usd": credit / 5.0}
        motifs = []
        if reste <= part:
            motifs.append(f"reste {reste} ≤ part au pire {part} (à l'égalité, le pire cas laisse zéro)")
        if reste < credit / 5.0:
            motifs.append(f"reste {reste} < un cinquième du crédit {credit / 5.0}")
        if fournisseur == "kimi" and part + reserve_kimi > 0.9 * reste:
            motifs.append(f"part au pire {part} + réserve déclarée {reserve_kimi} > 90 % du reste ({round(0.9 * reste, 6)})")
        d["motifs_d_arret"] = motifs
        sortie[nom] = d
        if motifs:
            alertes.append({"cle": nom, "fournisseur": fournisseur, "reste_usd": reste, "credit_usd": credit, "part_au_pire_usd": part,
                            "motifs": motifs})
    if alertes:
        texte = {"alerte": "crédit insuffisant pour la part au pire d'une clé, avant la course d'auto-conception : départ refusé",
                 "regle": "R-3237 : chaque clé confrontée à sa part au pire ; un cinquième du crédit ; Kimi : part + réserve "
                          "déclarée ≤ 90 % du reste ; Lazar à prévenir avant qu'une clé n'atteigne zéro",
                 "cles": alertes, "pour": "la mère (à transmettre à Lazar)"}
        dossier_alerte.mkdir(parents=True, exist_ok=True)
        chemin = dossier_alerte / "alerte-credits-avant.json"
        if not chemin.exists():
            ecrire_scelle(chemin, texte)
        raise AlerteCredit(json.dumps(dict(texte, fichier=str(chemin)), ensure_ascii=False))
    return sortie


def verifier_releve_prix(chemin: Path, fixe: dict, aujourd_hui: _dt.date) -> dict:
    o, h = lire_json_scelle(chemin, "relevé des prix Claude")
    if not str(o.get("releve_utc") or "").startswith(aujourd_hui.isoformat()):
        raise Refus(f"relevé des prix Claude : du jour ({aujourd_hui}) exigé")
    if not isinstance(o.get("source"), str) or not o["source"].strip():
        raise Refus("relevé des prix Claude : source exigée")
    claude = [e for e in fixe["especes"] if e["famille"] == "claude"]
    prix = o.get("prix") or {}
    for k, e in enumerate(claude, 1):
        lu = prix.get(f"espece_claude_{k}")
        if not (isinstance(lu, dict) and [lu.get("entree"), lu.get("sortie")] == list(BAREME_CLAUDE[e["modele"]])):
            raise Refus(f"relevé des prix Claude : espèce Claude {k} lue {lu!r}, différente du barème du relais : arrêt, nouveau devis")
    return {"chemin": str(chemin), "sha256": h, "source": o["source"], "releve_utc": o["releve_utc"], "egal_au_bareme": True}


def envelopper_commandes(decl: dict, python: str, garde: Path, dossier_arrets: Path) -> dict:
    for nom in FOURNISSEURS_DISPENSABLES:
        b = decl["fournisseurs"].get(nom)
        if b is not None:
            b["commande"] = [python, "-I", "-B", str(garde), str(dossier_arrets), nom, "--"] + list(b["commande"])
    return decl


# --- (5) orchestrateur, configuration -------------------------------------------------------------------------------------------


def verifier_orchestrateur(r: Reglages) -> dict:
    presents = [o for o in r.orchestrateurs if (o / LANCEUR_ORCHESTRATEUR).is_file()]
    if len(presents) != 1:
        raise Refus(f"orchestrateur : {len(presents)} copie(s) trouvée(s) parmi {[str(o) for o in r.orchestrateurs]} (une exigée)")
    o = presents[0]
    tete = _git(o, "rev-parse", "HEAD").strip()
    if tete != r.commit_orchestrateur:
        raise Refus(f"orchestrateur au commit {tete}, {r.commit_orchestrateur} exigé")
    porcelaine = _git(o, "status", "--porcelain", "--untracked-files=all", "--ignored=matching").strip()
    if porcelaine:
        raise Refus(f"orchestrateur modifié, fichiers non suivis ou ignorés : {porcelaine[:200]!r}")
    ecarts = {rel: (sha256_fichier(o / rel) if (o / rel).is_file() else None) for rel in r.empreintes_orchestrateur}
    ecarts = {k: v for k, v in ecarts.items() if v != r.empreintes_orchestrateur[k]}
    if ecarts:
        raise Refus(f"orchestrateur : empreintes différentes ou fichiers absents : {ecarts}")
    return {"chemin": str(o), "commit": tete, "empreintes": dict(r.empreintes_orchestrateur)}


def garde_configuration_fixe(fixe: dict) -> None:
    b = fixe.get("budget") or {}
    if b.get("plafond_usd") != PLAFOND_ARRET_USD:
        raise Refus(f"configuration : budget.plafond_usd {b.get('plafond_usd')!r} != plafond d'arrêt {PLAFOND_ARRET_USD}")
    if b.get("portee_plafond") != "course" or fixe.get("generations") != 1:
        raise Refus("configuration : portée « course » et une seule génération exigées")
    etapes = {e["nom"]: e for e in b.get("etapes") or []}
    for nom in ("passe_tableau", "fusions"):
        e = etapes.get(nom) or {}
        if e.get("role") != "sacrifiable" or not e.get("plafond_relais_usd", 0) > PLAFOND_ARRET_USD or e.get("attendu_usd") != 0:
            raise Refus(f"configuration : l'étape {nom} doit être retirée par construction (sacrifiable, plafond de relais > S17, attendu 0)")
    protegees = sum(e["plafond_relais_usd"] for e in etapes.values() if e.get("role") == "protegee")
    if protegees > PLAFOND_ARRET_USD:
        raise Refus(f"configuration : somme des plafonds de relais des étapes protégées {protegees} > {PLAFOND_ARRET_USD}")
    if "etage_tests_de_mort" in fixe:
        raise Refus("configuration : pas de tests de mort dans cette course")
    if fixe.get("bisociateur", {}).get("bras") != [] or fixe.get("bisociateur", {}).get("k_paires") != 0:
        raise Refus("configuration : aucun bras du bisociateur, aucune fusion")
    if list(fixe.get("etiquettes_interdites_fixes") or []) != list(ETIQUETTES_INTERDITES_FIXES):
        raise Refus("configuration : étiquettes interdites fixes différentes de celles du lanceur (masquage des lots)")
    for e in fixe.get("especes") or []:
        if e.get("famille") == "claude" and e.get("cle") != "pièce de départ":
            raise Refus(f"configuration : espèce {e.get('etiquette')} : la clé Claude vient de la pièce de départ")


def assembler_configuration(fixe: dict, lots: dict, pieces: dict, decl: dict, specification: dict | None) -> dict:
    garde_configuration_fixe(fixe)
    actives = decl["especes_actives"]
    if not any(e["famille"] == "claude" for e in actives):
        raise Refus("aucune espèce Claude active : Claude d'abord (R-3209, point 2)")
    conf = {k: v for k, v in fixe.items() if k not in ("version", "statut", "orchestrateur", "generations", "cartes_par_appel",
                                                       "especes", "etiquettes_interdites_fixes", "cles", "regle_cles",
                                                       "relais_persistants", "matiere",
                                                       "cartes_max_comptees")}
    conf["proposeurs"] = [{"etiquette": e["etiquette"], "modele": e["modele"], "fournisseur": e["fournisseur"],
                           "consigne": "consigne_proposeur"} for e in actives]
    conf["cases"] = [[texte_de_case(lots, l), "auto-conception"] for l in lots["lots"]]
    conf["pieces"] = {n: {"chemin": pieces[n]["absolu"], "sha256": pieces[n]["sha256"]} for n in PIECES_SERVIES}
    conf["etiquettes_interdites"] = list(fixe["etiquettes_interdites_fixes"])
    conf["fournisseurs"] = decl["fournisseurs"]
    if specification is not None:
        conf["specification"] = specification
    utilises = {conf["aiguilleur"]["fournisseur"]} | {j["fournisseur"] for j in conf["juges"]} | \
        {x["fournisseur"] for x in conf["lecteurs_etiquettes"]}
    manquants = sorted(utilises - set(conf["fournisseurs"]))
    if manquants:
        raise Refus(f"relais absents pour l'aiguilleur, un juge ou un lecteur : {manquants}")
    return conf


def acte_de_gel(prereg: dict, cl: dict, lanceur_sha: str, horodatage: str, matiere: dict, lots_sha: str) -> str:
    return ("# Acte de gel — course d'auto-conception de l'organisme d'idéation, version 1\n\n"
            f"Écrit par le lanceur `{VERSION}` (sha256 {lanceur_sha}) le {horodatage}, après vérification.\n\n"
            f"- Préenregistrement : `{prereg['chemin']}`, sha256 {prereg['sha256']}, scellé.\n"
            f"- Contre-lecture : `{cl['chemin']}`, sha256 {cl['sha256']}, scellée ; verdict lu : {cl['verdict']}\n"
            f"- Matière servie : `{matiere['chemin']}`, sha256 {matiere['sha256']}, lue au commit {matiere['commit']} ; "
            f"lots écrits par la règle du préenregistrement, sha256 {lots_sha}.\n"
            "- Cet acte est la spécification servie à l'orchestrateur (`specification.preenregistrement`) ; il ne change rien au "
            "préenregistrement.\n")


# --- (6) environnement, bac à sable ---------------------------------------------------------------------------------------------


def environnement_filtre(env: dict, dossier_maison: Path, go_id: str) -> tuple:
    retires = sorted(n for n in env if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n))
    hors_liste = sorted(n for n in env if n not in NOMS_PERMIS and n not in retires)
    garde = {n: env[n] for n in env if n in NOMS_PERMIS}
    garde["GO_ID"] = go_id
    garde["HOME"] = str(dossier_maison)
    garde["PYTHONPYCACHEPREFIX"] = str(dossier_maison / "pycache")
    return garde, retires, hors_liste


def sonder_bac_a_sable(r: Reglages, orchestrateur: Path, env: dict) -> dict:
    try:
        p = subprocess.run([r.python, "-I", "-B", "-c", SONDE_BAC_A_SABLE, str(orchestrateur)], cwd=str(orchestrateur), env=env,
                           capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"sonde du bac à sable non exécutée ({type(e).__name__})") from None
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    try:
        etat = json.loads(lignes[-1]) if p.returncode == 0 and lignes else None
    except json.JSONDecodeError:
        etat = None
    if not (isinstance(etat, dict) and isinstance(etat.get("actif"), bool)):
        raise Refus(f"sonde du bac à sable illisible (code {p.returncode})")
    if r.exiger_bac_a_sable and not (etat["actif"] and etat.get("proc_neuf")):
        raise Refus("bac à sable inactif ou sans /proc neuf : " + str(etat.get("motif")))
    return etat


# --- (7) après la course --------------------------------------------------------------------------------------------------------


def couts_reels(sortie: Path) -> dict:
    chemin = sortie / "generation-1" / "consommations.json"
    if not chemin.is_file():
        return {"lisible": False, "motif": f"{chemin} absent"}
    donnees = json.loads(chemin.read_text(encoding="utf-8")).get("consommations") or []
    par_relais, par_role, appels, coupures, inconnus = {}, {}, {}, [], {}
    for x in donnees:
        role = x.get("role")
        if role == "plafond-relais":
            continue
        if role == "coupure" or x.get("coupure"):
            coupures.append(str(x.get("etape")))
            continue
        f, role, c = str(x.get("fournisseur") or "(sans relais)"), str(role or "(sans rôle)"), float(x.get("cout_usd") or 0.0)
        par_relais[f] = round(par_relais.get(f, 0.0) + c, 6)
        par_role[role] = round(par_role.get(role, 0.0) + c, 6)
        appels[role] = appels.get(role, 0) + 1
        if x.get("cout_inconnu"):
            inconnus[f] = inconnus.get(f, 0) + 1
    return {"lisible": True, "fichier_sha256": sha256_fichier(chemin), "par_relais_usd": par_relais, "par_role_usd": par_role,
            "appels_par_role": appels, "total_usd": round(sum(par_relais.values()), 6), "coupures": coupures,
            "appels_a_cout_inconnu_par_relais": inconnus}


def ecart_au_devis(couts: dict, especes: list) -> dict:
    if not couts.get("lisible"):
        return {"lisible": False}
    lignes = {}
    for role, n in sorted(couts["appels_par_role"].items()):
        attendu = DEVIS_V1_PAR_APPEL.get(role)
        reel = couts["par_role_usd"][role]
        lignes[role] = {"appels": n, "reel_usd": reel, "devis_usd": round(n * attendu, 6) if attendu is not None else None,
                        "ecart_usd": round(reel - n * attendu, 6) if attendu is not None else None}
    cle = "+".join(sorted(e for e in especes))
    total_devis = DEVIS_V1_TOTAL.get(cle)
    return {"lisible": True, "par_role": lignes, "total_reel_usd": couts["total_usd"], "devis_estimation_usd": total_devis,
            "ecart_total_usd": round(couts["total_usd"] - total_devis, 6) if total_devis is not None else None}


def releve_apres(credits: dict, couts: dict, cles: dict, reserve_kimi: float) -> tuple:
    apres, alertes = {}, []
    for nom, avant in sorted(credits.items()):
        fournisseurs = [f for f, n in cles.items() if n == nom]
        depense = round(sum((couts.get("par_relais_usd") or {}).get(f, 0.0) for f in fournisseurs), 6) if couts.get("lisible") else None
        if not avant.get("lisible") or depense is None:
            apres[nom] = {"lisible": False, "depense_comptee_usd": depense, "a_relever": "par l'interface de facturation si elle le permet"}
            continue
        reste = round(avant["reste_usd"] - depense, 6)
        seuil = avant["credit_usd"] / 5.0
        if "kimi" in fournisseurs:
            seuil = max(seuil, reserve_kimi / 0.9)
        apres[nom] = {"lisible": "estimé", "reste_estime_usd": reste, "depense_comptee_usd": depense, "seuil_usd": seuil,
                      "a_relever": "par l'interface de facturation (confirmation)"}
        if reste < seuil:
            alertes.append({"cle": nom, "reste_estime_usd": reste, "seuil_usd": seuil})
    return apres, alertes


def lire_resume_course(sortie: Path) -> dict:
    """Ce qui a été fait, sans lire aucun verdict : étapes, nœud, arrêt, cumul, nombre de cartes."""
    out = {}
    m = sortie / "generation-1" / "manifeste-fin.json"
    if m.is_file():
        d = json.loads(m.read_text(encoding="utf-8"))
        out.update(etapes=d.get("etapes"), noeud=d.get("noeud"), arret=d.get("arret"), roles_arretes=d.get("roles_arretes"),
                   exclues_a4=d.get("exclues_a4"), cumul_usd=(d.get("budget") or {}).get("cumul_usd"),
                   depassement_s17_usd=(d.get("budget") or {}).get("depassement_s17_usd"))
    f = sortie / "generation-1" / "fiches.json"
    if f.is_file():
        out["cartes_a_passeport"] = len(json.loads(f.read_text(encoding="utf-8")))
    b = sortie / "bilan-course.json"
    if b.is_file():
        out["bilan_sha256"] = sha256_fichier(b)
    return out


def _depot_git(r: Reglages) -> dict:
    try:
        return {"commit": _git(r.depot, "rev-parse", "HEAD").strip(),
                "arbre_modifie": bool(_git(r.depot, "status", "--porcelain", "--untracked-files=no").strip())}
    except Refus as e:
        return {"commit": None, "erreur": str(e)}


def _versions(r: Reglages, orch: Path, env: dict) -> dict:
    p = subprocess.run([r.python, "-I", "-B", "-c", "import numpy, platform; print(numpy.__version__, platform.python_version())"],
                       cwd=str(orch), env=env, capture_output=True, text=True, timeout=60)
    morceaux = p.stdout.split()
    return {"python": morceaux[1] if len(morceaux) == 2 else None, "numpy": morceaux[0] if len(morceaux) == 2 else None,
            "executable": r.python}


# --- exécution ------------------------------------------------------------------------------------------------------------------


def executer(r: Reglages) -> int:
    env_lu = dict(os.environ) if r.environnement is None else dict(r.environnement)
    aujourd_hui = r.aujourd_hui or _dt.datetime.now(_dt.timezone.utc).date()
    reel = r.moteur == "reel"

    verifier_course_jamais_lancee(r)
    depart = verifier_piece_de_depart(r)
    cle_claude = depart["variable_cle_claude"]
    cle_presente = bool(env_lu.get(cle_claude))  # nom présent et valeur non vide ; la valeur n'est jamais lue ni écrite
    if reel and not cle_presente:
        raise Refus(f"variable {cle_claude} absente ou vide dans l'environnement du lanceur : arrêt au départ")
    registre = lire_registre(r) if (reel and r.verifier_go) else None
    go = verifier_go(registre["texte"], aujourd_hui, depart["go_course"], PLAFOND_ARRET_USD, ("autoconception",)) if registre \
        else {"go": "sans objet (moteur simulé, aucune dépense)"}
    lanceur_sha = sha256_fichier(r.lanceur)
    prereg = verifier_preenregistrement(r)
    cl = verifier_contre_lecture(r, prereg["sha256"], lanceur_sha)
    pieces = verifier_pieces(r)
    fixe = json.loads(Path(pieces["configuration"]["absolu"]).read_text(encoding="utf-8"))
    garde_configuration_fixe(fixe)
    matiere = verifier_matiere(r)
    lots = decouper_matiere(matiere["octets"], matiere["sha256"])
    epreuve = verifier_epreuve_reelle(r, pieces, fixe, depart, aujourd_hui, lanceur_sha) if reel \
        else {"exigee": False, "motif": "moteur simulé : l'épreuve hors ligne des témoins suffit à l'essai à blanc"}
    decl_brute, decl_sha = lire_json_scelle(r.declaration, "déclaration des relais")
    decl = verifier_declaration(decl_brute, fixe, depart)
    releve_brut, releve_sha = lire_json_scelle(r.releve, "relevé des crédits")
    horodatage = r.horodatage()
    ident = nouvel_ident(r)
    dossier_run = r.dossier_runs / ident
    consigne = Path(pieces["consigne_proposeur"]["absolu"]).read_bytes()
    entree_max = len(consigne) + max(len(texte_de_case(lots, l).encode("utf-8")) for l in lots["lots"]) + 400
    parts = parts_au_pire(fixe, len(lots["lots"]), entree_max, decl)
    credits = verifier_credits(releve_brut, decl["cles"], aujourd_hui,
                               r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-auto-conception-v1"), parts, depart)
    appels_argon = appels_argon_au_pire(fixe, len(lots["lots"]), decl["especes_actives"], fixe["cartes_max_comptees"])
    procedure = verifier_procedure_relais(r, decl, pieces, fixe, appels_argon) if reel \
        else {"exigee": False, "motif": "moteur simulé : aucun relais réel"}
    prix = verifier_releve_prix(r.releve_prix, fixe, aujourd_hui) if reel else {"exige": False, "motif": "moteur simulé"}
    orch = verifier_orchestrateur(r)
    orch_dir = Path(orch["chemin"])

    dossier_sortie = r.dossier_sorties / ident
    sortie = dossier_sortie / "sortie"
    if dossier_run.exists() or dossier_sortie.exists():
        raise Refus(f"{dossier_run} ou {dossier_sortie} existe déjà (R12)")
    env, retires, hors_liste = environnement_filtre(env_lu, dossier_sortie, depart["go_course"])
    bac = sonder_bac_a_sable(r, orch_dir, env) if reel else {"exige": False, "motif": "moteur simulé : aucun agent réel"}

    # Dossier du run (n'empêche pas une nouvelle tentative : la garde « une seule course » lit le manifeste de départ).
    dossier_run.mkdir(parents=True)
    h_lots = ecrire_scelle(dossier_run / "lots-matiere.json", lots)
    dossier_arrets = dossier_sortie / "arrets-credit"   # chemin seulement : la sortie est créée après la porte à blanc
    decl = envelopper_commandes(decl, r.python, Path(pieces["garde_credit"]["absolu"]), dossier_arrets)
    h_acte = ecrire_scelle(dossier_run / "acte-de-gel.md", acte_de_gel(prereg, cl, lanceur_sha, horodatage, matiere, h_lots))
    spec = {"preenregistrement": {"chemin": str(dossier_run / "acte-de-gel.md"), "sha256": h_acte},
            "contre_lecture": {"chemin": cl["chemin"], "sha256": cl["sha256"]}}
    conf = assembler_configuration(fixe, lots, pieces, decl, spec)
    chemin_conf = dossier_run / "configuration-orchestrateur.json"
    h_conf = ecrire_scelle(chemin_conf, conf)
    base = [r.python, "-I", "-B", LANCEUR_ORCHESTRATEUR, "--course-2", str(chemin_conf), str(sortie), "--generations", "1"]
    derive = ecrire_registre_derive(registre, dossier_run / "registre-go-derive.md", depart["go_course"]) if registre \
        else {"motif": "moteur simulé"}
    moteur = ["--moteur", "reel", "--confirmer-moteur-reel", "--registre-go", derive["derive"]] if reel else ["--moteur", "simule"]
    env_verif = dict(env, HOME=str(dossier_run))
    verif = subprocess.run(base + ["--verifier-seulement"] + (moteur if reel else []),
                           cwd=str(orch_dir), env=env_verif, capture_output=True, text=True, timeout=600)
    try:
        verif_json = json.loads(verif.stdout) if verif.returncode == 0 else None
    except ValueError:
        verif_json = None
    if verif_json is None or verif_json.get("montant_requis_go_usd") != PLAFOND_ARRET_USD:
        raise Refus(f"vérification de l'orchestrateur refusée (code {verif.returncode}) : "
                    f"{(verif.stderr or verif.stdout).strip()[-800:]!r}")
    if verif_json.get("specification", {}).get("conforme") is not True:
        raise Refus(f"spécification refusée par l'orchestrateur : {verif_json.get('specification')}")
    portes = porte_a_blanc(decl) if reel else {"exige": False, "motif": "moteur simulé : portes tenues par le noyau"}
    dossier_sortie.mkdir(parents=True)   # constat 1 : seulement après la porte à blanc et toutes les gardes
    dossier_arrets.mkdir()
    argv = base + moteur
    especes = [e["etiquette"] for e in decl["especes_actives"]]
    depart_manifeste = {
        "lanceur": {"version": VERSION, "chemin": str(r.lanceur), "sha256": lanceur_sha}, "moteur": r.moteur,
        "horodatage_canonique": horodatage, "id": ident, "go": go, "plafond_arret_usd": PLAFOND_ARRET_USD,
        "piece_de_depart": {k: v for k, v in depart.items()}, "preenregistrement": prereg, "contre_lecture": cl,
        "acte_de_gel_sha256": h_acte, "pieces": pieces,
        "matiere": {k: v for k, v in matiere.items() if k != "octets"},
        "lots": {"sha256": h_lots, "nombre": len(lots["lots"]), "commun_octets": lots["commun"]["octets"],
                 "octets_par_lot": {l["nom"]: l["octets"] for l in lots["lots"]},
                 "masques": lots["commun"]["masques"] + sum(l["masques"] for l in lots["lots"]), "entree_max_octets": entree_max},
        "epreuve_reelle_des_temoins": epreuve,
        "declaration_relais": {"chemin": str(r.declaration), "sha256": decl_sha},
        "especes_actives": especes, "especes_absentes": decl["especes_absentes"], "cles_employees": decl["cles"],
        "cle_par_espece": {e["etiquette"]: decl["cles"][e["fournisseur"]] for e in decl["especes_actives"]},
        "cle_par_role_interne": {"aiguilleur": decl["cles"][fixe["aiguilleur"]["fournisseur"]],
                                 **{j["etiquette"]: decl["cles"][j["fournisseur"]] for j in fixe["juges"]}},
        "parts_au_pire": parts, "appels_argon_au_pire": appels_argon, "procedure_relais_persistants": procedure,
        "porte_a_blanc": portes, "registre_go_derive": derive, "releve_prix_claude": prix,
        "dossier_arrets_credit": str(dossier_arrets),
        "cle_claude": {"nom": cle_claude, "presente_dans_l_environnement_du_lanceur": cle_presente, "valeur": "jamais lue",
                       "cles_reservees_refusees": list(CLES_CLAUDE_RESERVEES)},
        "releve_credits_avant": {"chemin": str(r.releve), "sha256": releve_sha, "cles": credits},
        "orchestrateur": orch, "configuration": {"chemin": str(chemin_conf), "sha256": h_conf},
        "verification_orchestrateur": {k: verif_json.get(k) for k in ("configuration_sha256", "montant_requis_go_usd",
                                                                      "specification", "go", "generations")},
        "commande": argv, "cwd": str(orch_dir), "sortie": str(sortie), "bac_a_sable": bac,
        "environnement": {"noms_retires": retires, "noms_exclus": hors_liste, "valeurs": "jamais lues"},
        "graines": {"racine": conf["racine_graines"], "prefixe": conf["graines"]["prefixe"],
                    "regle": "numpy.random.SeedSequence(racine, spawn_key=(cle_de_tache(tache),)) dans l'orchestrateur (R9)"},
        "versions": _versions(r, orch_dir, env), "depot_travail": _depot_git(r),
        "journaux": {"stdout": str(dossier_sortie / "course.stdout.txt"), "stderr": str(dossier_sortie / "course.stderr.txt")},
    }
    h_depart = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json", depart_manifeste)
    print(json.dumps({"manifeste_depart": str(dossier_run / "manifeste-lanceur-depart.json"), "sha256": h_depart}, ensure_ascii=False),
          flush=True)

    code, pid, echec, arret_credit = None, None, None, []
    debut = _dt.datetime.now(_dt.timezone.utc)

    def arrets():
        return sorted(x.name for x in dossier_arrets.iterdir() if x.name.startswith("arret-credit-"))
    try:
        with open(dossier_sortie / "course.stdout.txt", "xb") as fo, open(dossier_sortie / "course.stderr.txt", "xb") as fe:
            enfant = subprocess.Popen(argv, cwd=str(orch_dir), env=env, stdout=fo, stderr=fe)
            pid = enfant.pid

            def relayer(num, _cadre):
                try:
                    enfant.send_signal(num)
                except ProcessLookupError:
                    pass
            anciens = {s: signal.signal(s, relayer) for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)}
            try:
                while True:
                    try:
                        code = enfant.wait(timeout=1.0)
                        break
                    except subprocess.TimeoutExpired:
                        if not arret_credit and arrets():
                            arret_credit = arrets()
                            enfant.send_signal(signal.SIGTERM)  # R-3237 : arrêt au premier refus pour crédit (par PID, R10)
            finally:
                for s, a in anciens.items():
                    signal.signal(s, a)
    except BaseException as exc:  # noqa: BLE001 — le manifeste de fin est écrit sur tout chemin
        echec = f"{type(exc).__name__}: {exc}"
    fin = _dt.datetime.now(_dt.timezone.utc)
    bilan = {"id": ident, "manifeste_depart_sha256": h_depart, "pid_orchestrateur": pid, "code": code, "echec_lanceur": echec,
             "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat(),
             "arret_au_premier_refus_pour_credit": [json.loads((dossier_arrets / n).read_text(encoding="utf-8")) for n in arrets()],
             "soupcons_de_credit": sorted(x.name for x in dossier_arrets.iterdir() if x.name.startswith("soupcon-credit-"))}
    alertes_apres, depasse = [], False
    try:
        couts = couts_reels(sortie)
        cumul = (lire_resume_course(sortie).get("cumul_usd") or 0.0)
        apres, alertes_apres = releve_apres(credits, couts, decl["cles"], float(depart["reserve_cle_kimi_usd"]))
        depasse = bool(couts.get("lisible") and couts["total_usd"] > PLAFOND_ARRET_USD + 1e-9) or cumul > PLAFOND_ARRET_USD + 1e-9
        bilan.update({"ce_qui_a_ete_fait": lire_resume_course(sortie), "cout_reel": couts,
                      "ecart_au_devis_v1": ecart_au_devis(couts, especes),
                      "plafond_arret": {"usd": PLAFOND_ARRET_USD, "depasse": depasse},
                      "releve_credits_apres": apres, "alertes_apres": alertes_apres})
    except Exception as exc:  # noqa: BLE001
        bilan["erreur_bilan"] = f"{type(exc).__name__}: {exc}"
        echec = echec or bilan["erreur_bilan"]
    bilan["journaux_sha256"] = {n: sha256_fichier(dossier_sortie / n) for n in ("course.stdout.txt", "course.stderr.txt")
                                if (dossier_sortie / n).is_file()}
    if bilan.get("arret_au_premier_refus_pour_credit"):
        ecrire_scelle(dossier_run / "alerte-arret-credit.json",
                      {"alerte": "course arrêtée au premier refus pour crédit d'un relais au solde illisible (R-3237)",
                       "relais": bilan["arret_au_premier_refus_pour_credit"], "pour": "la mère, qui prévient Lazar"})
    if alertes_apres or depasse:
        ecrire_scelle(dossier_run / "alerte-credits-apres.json",
                      {"alerte": "après la course : reste estimé sous le seuil ou plafond d'arrêt dépassé", "cles": alertes_apres,
                       "plafond_depasse": bool(depasse), "pour": "la mère (à transmettre à Lazar avant qu'une clé n'atteigne zéro)"})
    h_fin = ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
    print(json.dumps({"manifeste_fin": str(dossier_run / "manifeste-lanceur-fin.json"), "sha256": h_fin, "code": code,
                      "cout_reel_usd": (bilan.get("cout_reel") or {}).get("total_usd"), "alertes_apres": alertes_apres},
                     ensure_ascii=False), flush=True)
    if echec:
        raise RuntimeError(echec)
    if depasse:
        return 4
    if bilan["arret_au_premier_refus_pour_credit"]:
        return 5
    return 0 if code == 0 else (code if isinstance(code, int) and code > 0 else 2)


# --- essai à blanc ----------------------------------------------------------------------------------------------------------------


def reglages_a_blanc(dossier: Path) -> Reglages:
    """Moteur simulé, relais factices, pièce de départ, contre-lecture et relevé d'essai écrits dans le dossier ; aucun GO,
    rien n'est lu dans `registres/` ; la matière est lue dans `refs/remotes/origin/main` à son empreinte épinglée."""
    if dossier.exists():
        raise Refus(f"{dossier} existe déjà (R12)")
    dossier.mkdir(parents=True)
    essai = dossier / "pieces-d-essai"
    essai.mkdir()
    r = Reglages.production()
    lanceur_sha = sha256_fichier(r.lanceur)
    prereg_sha = r.prereg[1] if _epingle(r.prereg[1]) else sha256_fichier(r.prereg[0])
    cl = essai / "contre-lecture-d-essai.md"
    ecrire_scelle(cl, f"# Contre-lecture d'ESSAI par le modèle K (aucune valeur réelle)\n\nPréenregistrement lu : {prereg_sha}\n"
                      f"Lanceur lu : {lanceur_sha}\n\n## Verdict\n\nScellable.\n\nEssai à blanc seulement.\n")
    cle_essai = "RR_ANTHROPIC_API_KEY_ESSAI_A_BLANC"
    depart = {"version": "piece-de-depart-essai-a-blanc", "par": "mère", "go_course": "GO-2026-01-01-01", "go_epreuve": "GO-2026-01-01-02",
              "variable_cle_claude": cle_essai, "credit_declare_cle_claude_usd": 500.0, "reserve_cle_kimi_usd": 0.0,
              "commandes_epinglees": {}}
    chemin_depart = essai / "piece-de-depart-d-essai.json"
    ecrire_scelle(chemin_depart, depart)
    porte = ["/bin/false"]
    decl = {"version": "declaration-relais-essai-a-blanc", "fournisseurs": {
        "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:18999", "nom_cle": cle_essai,
                   "porte_plafond": {"type": "commande", "commande": porte, "delai_s": 5}},
        "argon": {"type": "commande_externe", "commande": ["bash", str(r.depot / PIECES["enveloppe_argon"][0])],
                  "nom_cle": "CLE_FACTICE_ARGON", "porte_plafond": {"type": "environnement"},
                  "url_etat_relais": f"http://127.0.0.1:{PORT_RELAIS_ARGON}"},
        "kimi": {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:18999", "modele": "kimi-k3.1-pro", "prix_entree": 2.0,
                 "prix_sortie": 10.0, "max_sortie_jetons": 16000, "sortie_min_jetons": 1000, "delai_s": 1800,
                 "nom_cle": "CLE_FACTICE_KIMI", "porte_plafond": {"type": "commande", "commande": porte, "delai_s": 5}}}}
    chemin_decl = essai / "declaration-relais-d-essai.json"
    ecrire_scelle(chemin_decl, decl)
    aujourd_hui = _dt.datetime.now(_dt.timezone.utc).date()
    releve = {"version": "releve-credits-essai-a-blanc", "releve_utc": aujourd_hui.isoformat() + " (essai)",
              "cles": {"CLE_FACTICE_ARGON": {"non_lisible": True, "motif": "essai à blanc : solde illisible, sous dispense"},
                       "CLE_FACTICE_KIMI": {"credit_usd": 30.0, "reste_usd": 30.0, "source": "factice (essai à blanc)"},
                       cle_essai: {"non_lisible": True, "motif": "essai à blanc : compté au prix relevé", "depense_anterieure_usd": 0.0}},
              "dispense": {"par": "mère", "reference": REFERENCE_DISPENSE, "cles": ["CLE_FACTICE_ARGON"]}}
    chemin_releve = essai / "releve-credits-d-essai.json"
    ecrire_scelle(chemin_releve, releve)
    r.prereg = (r.prereg[0], prereg_sha)
    r.contre_lecture, r.declaration, r.releve, r.piece_de_depart = cl, chemin_decl, chemin_releve, chemin_depart
    r.dossier_runs, r.dossier_sorties = dossier / "runs", dossier / "sorties"
    r.moteur, r.exiger_bac_a_sable, r.verifier_go = "simule", False, False
    return r


def decouper_vers(matiere: Path, dossier: Path) -> int:
    if dossier.exists():
        raise Refus(f"{dossier} existe déjà (R12)")
    octets = matiere.read_bytes()
    lots = decouper_matiere(octets, sha256_octets(octets))
    dossier.mkdir(parents=True)
    h = ecrire_scelle(dossier / "lots-matiere.json", lots)
    print(json.dumps({"lots": str(dossier / "lots-matiere.json"), "sha256": h, "matiere_sha256": lots["matiere_sha256"],
                      "nombre": len(lots["lots"]), "commun_octets": lots["commun"]["octets"],
                      "octets_avec_commun": {l["nom"]: l["octets_avec_commun"] for l in lots["lots"]}}, ensure_ascii=False))
    return 0


def principal(argv: list | None = None, reglages: Reglages | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    try:
        if argv and argv[0] == "--a-blanc" and len(argv) == 2:
            reglages = reglages or reglages_a_blanc(Path(argv[1]).resolve())
        elif argv and argv[0] == "--decouper" and len(argv) == 3:
            return decouper_vers(Path(argv[1]).resolve(), Path(argv[2]).resolve())
        elif argv:
            print(json.dumps({"refus": f"arguments non admis (reçu {argv!r}) ; « --a-blanc DOSSIER » ou « --decouper MATIERE DOSSIER »"},
                             ensure_ascii=False), file=sys.stderr)
            return 2
        return executer(reglages or Reglages.production())
    except AlerteCredit as e:
        print(json.dumps({"alerte_credit": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 3
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"erreur": f"{type(e).__name__}: {e}"}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
