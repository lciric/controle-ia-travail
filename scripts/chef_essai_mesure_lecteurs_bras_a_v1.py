#!/usr/bin/env python3
"""Chef de l'essai de mesure de la longueur de sortie des lecteurs du bras A des organismes discrets — version 1.

Devis joué : `docs/notes/relance-organismes-discrets-v1/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`
(`533ad5b15e6de1bdfe81c35f8501dbad376f52f907be84094c3fd8621b349592`), sections 4 à 12, et ses vérifications.
Une file par invocation. **Commandes exactes, stables, lancées depuis la racine du dépôt** :

    GO_ID=GO-2026-11-19-34 python3 -I -B scripts/chef_essai_mesure_lecteurs_bras_a_v1.py claude
    GO_ID=GO-2026-11-19-35 python3 -I -B scripts/chef_essai_mesure_lecteurs_bras_a_v1.py carbon
    GO_ID=GO-2026-11-19-36 python3 -I -B scripts/chef_essai_mesure_lecteurs_bras_a_v1.py gpt

La première est la seule qui demande une règle de permission (devis, 5.6) : elle n'a ni option ni variante.
Sans appel, sans dépense :

    python3 -I -B scripts/chef_essai_mesure_lecteurs_bras_a_v1.py rapport DOSSIER_DE_LA_COURSE
    python3 -I -B scripts/chef_essai_mesure_lecteurs_bras_a_v1.py regle DOSSIER_CLAUDE [DOSSIER_CARBON]

Ce que fait une file, dans l'ordre :
1. **Avant tout envoi** : empreinte de la configuration (constante ci-dessous) ; `GO_ID` égal à la ligne de la file ;
   ligne lue au registre de la branche principale (`git show origin/main:registres/go.md`), unique, de type « calcul »,
   au plafond de la file, non échue, citant l'empreinte du devis (G7) ; empreintes du devis, des textes, des deux
   consignes, de chaque consigne remplie, du relais, du lanceur de relais et, pour Carbon, de la page de prix scellée
   (sans elle, le prix compté ne vaut plus : une configuration nouvelle au prix de repli est due) ; file jamais jouée (une ligne ne se rejoue
   pas) ; liste locale des interdits présente (G5) ; pour la file Claude, variable de clé présente et relevé de
   vérification de la clé d'empreinte conforme (G8). Un défaut : rien ne part, code 2.
2. Dossier de la course créé ; manifeste de départ écrit ; relais lancé par `scripts/lancer_relais_local_v1.py` (clé
   exigée par son nom, jamais lue ni affichée ici ; pour GPT, valeur factice que le mandataire du réseau remplace) ;
   état du relais contrôlé (neuf, plafond, modèles).
3. L'**ouvrier** (ce même fichier, relancé avec un environnement réduit à `PATH`, `HOME`, `LANG`, `GO_ID` : il n'a
   aucune clé) joue la file en série, sur la boucle locale seulement, par `http.client` : aucune bibliothèque cliente,
   **aucune reprise automatique** ; au plus une reprise par appel, décidée ici.
4. Fin, arrêt par une garde, signal ou panne : état du relais lu, relais arrêté par son identifiant de processus (R10),
   recherche de toute chaîne de la forme d'une clé, rapport technique, **inventaire scellé** de tout le dossier. Rien
   n'est jamais supprimé par ce programme.

Gardes (devis, section 9) : G1 plafond par modèle et par file, refus **avant** l'envoi sur le pire cas de l'envoi (un
jeton par octet du corps, sortie maximale comptée) ; G2 délais, une reprise, trois délais de suite arrêtent le réglage,
délai global ; G3 sortie maximale envoyée et compteurs rendus ; G4 refus de compte (arrêt de la file), refus de contenu
(arrêt du modèle), modèle servi autre (arrêt de la file), surcharge (une reprise, puis arrêt du réglage), code 400
(arrêt de la file, sauf le refus de la température au premier envoi), **tout autre code : arrêt de la file, sans
reprise** ; G5 rien de personnel dans ce qui part ; G6 clés par leur nom ; G7 ligne de calcul ; G8 clé Claude vérifiée.

Lectures retenues, déclarées :
- un plafond atteint, de modèle ou de file, **arrête la file** (lettre de G1) ;
- la file Claude est lue en flux (`"stream": true`), comme le suppose G2 ; les relais de Google et d'OpenAI rendent
  une réponse entière : le silence y est surveillé par le relais (115 et 230 secondes), le délai total par le chef ;
- un envoi parti sans compteur lisible est compté au pire cas ; un refus rendu par le relais avant l'amont est compté
  zéro ; le refus de la température est compté au pire cas pour GPT, zéro pour Carbon (devis, 5.5 et 6.3) ;
- un refus de la clé pour un modèle (403 ou 404) arrête toute la file Claude : les modèles pas encore joués ne sont
  pas mesurés et demandent une ligne nouvelle (vérification du brouillon 3, point 3).

Ce programme ne lit jamais le texte d'une réponse pour un jugement : il en tire les compteurs, le motif de fin, le
modèle servi et la conformité de forme (oui ou non, code de cause), et le rapport n'en contient aucune sous-chaîne.
Bibliothèque standard seulement. Essais : `tests/test_chef_essai_mesure_lecteurs_bras_a_v1.py` (faux fournisseurs).
"""
from __future__ import annotations

import datetime
import hashlib
import http.client
import importlib.util
import json
import math
import os
import re
import signal
import socket
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

VERSION = "chef_essai_mesure_lecteurs_bras_a_v1"
RACINE = Path(__file__).resolve().parents[1]
CONFIGURATION = ("docs/notes/relance-organismes-discrets-v1/essai-mesure-lecteurs-bras-a-v1/"
                 "configuration-essai-mesure-lecteurs-bras-a-v1.json")
EMPREINTE_CONFIGURATION = "e047c502ca711b188b435092537cb620a2650ff52cb25c7403afa37020ddf194"
FILES = ("claude", "carbon", "gpt")
HOTES_LOCAUX = ("127.0.0.1", "localhost", "::1")
AGENT_UTILISATEUR = "client-http/1.0"
ENVIRONNEMENT_OUVRIER = ("PATH", "HOME", "LANG", "GO_ID")
FORMES_DE_CLE = (r"sk-ant-[A-Za-z0-9_\-]{16,}", r"sk-[A-Za-z0-9_\-]{24,}", r"AIza[0-9A-Za-z_\-]{30,}")
FORMES_INTERDITES = (
    ("courriel", r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}"),
    ("identifiant de session", r"session_[0-9A-Za-z]{8,}"),
    ("identifiant universel", r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"),
    ("chemin du poste", r"(/home/|/root/|/tmp/|/Users/|[A-Za-z]:\\\\)"),
    ("adresse de session", r"claude\.ai/"),
)
FITS = ("answers", "does_not_answer", "cannot_tell")
CLES_APPARIEMENT = ("fit", "specific", "proposal_quote", "controls_quote")
CONTENUS = ("conforme", "altere", "absent")
PLACES = ("checks", "cannot_check", "general")
CLES_COUVERTURE = ("content", "quote", "place")
FENETRE_SOUS_CHAINE = 24


class Arret(Exception):
    """Une garde coupe : motif écrit, rien de silencieux (R5)."""


class Interruption(Exception):
    """Signal d'arrêt reçu par l'ouvrier : la file s'arrête, ce qui est reçu est gardé."""


def _lever_interruption(numero, cadre):
    raise Interruption(f"signal {numero}")


# --- outils -------------------------------------------------------------------------------------------------------------

def heure() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_octets(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def sha256_fichier(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def ecrire_neuf(chemin: Path, octets: bytes) -> None:
    """Écrit un fichier qui n'existe pas, vidé sur le disque ; jamais d'écrasement (R12)."""
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "xb") as f:
        f.write(octets)
        f.flush()
        os.fsync(f.fileno())


def json_octets(objet) -> bytes:
    return (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")


class Journal:
    """Journal de l'essai, une ligne JSON par événement, vidée sur le disque à chaque écriture."""

    def __init__(self, chemin: Path):
        self.chemin = chemin
        chemin.parent.mkdir(parents=True, exist_ok=True)

    def ecrire(self, **champs) -> None:
        ligne = json.dumps({"quand": heure(), **champs}, ensure_ascii=False, sort_keys=True) + "\n"
        with open(self.chemin, "a", encoding="utf-8") as f:
            f.write(ligne)
            f.flush()
            os.fsync(f.fileno())


def lire_journal(chemin: Path) -> list:
    if not chemin.exists():
        return []
    return [json.loads(l) for l in chemin.read_text(encoding="utf-8").splitlines() if l.strip()]


# --- configuration et pièces --------------------------------------------------------------------------------------------

def charger_configuration(chemin: Path, empreinte_attendue: str) -> dict:
    if not Path(chemin).is_file():
        raise Arret(f"configuration absente : {chemin}")
    empreinte = sha256_fichier(chemin)
    if empreinte != empreinte_attendue:
        raise Arret(f"configuration d'empreinte {empreinte[:12]}… au lieu de {empreinte_attendue[:12]}… : rien ne part")
    compagnon = Path(str(chemin) + ".sha256")
    if compagnon.exists() and compagnon.read_text(encoding="utf-8").split()[0] != empreinte:
        raise Arret("l'empreinte compagnon de la configuration ne répond pas au fichier")
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def verifier_piece(racine: Path, piece: dict, nom: str) -> None:
    chemin = racine / piece["chemin"]
    if not chemin.is_file():
        raise Arret(f"{nom} : fichier absent ({piece['chemin']})")
    empreinte = sha256_fichier(chemin)
    if empreinte != piece["sha256"]:
        raise Arret(f"{nom} : empreinte {empreinte[:12]}… au lieu de {piece['sha256'][:12]}… ({piece['chemin']})")


def extraire_consigne(texte_prereg: str, lignes: list, empreinte: str, nom: str) -> str:
    """Bloc de consigne, caractère pour caractère : lignes jointes par un saut de ligne, sans saut final."""
    toutes = texte_prereg.split("\n")
    debut, fin = lignes
    if fin >= len(toutes) or not (toutes[debut - 2].startswith("```") and toutes[fin].startswith("```")):
        raise Arret(f"consigne {nom} : les lignes {debut - 1} et {fin + 1} ne sont pas les clôtures du bloc")
    bloc = "\n".join(toutes[debut - 1:fin])
    if sha256_octets(bloc.encode("utf-8")) != empreinte:
        raise Arret(f"consigne {nom} : empreinte différente de celle de la configuration")
    return bloc


def remplir(consigne: str, valeurs: dict) -> str:
    """Simple remplacement de chaînes, en une passe : une valeur qui contient une accolade reste intacte."""
    motif = re.compile("|".join(re.escape(m) for m in valeurs))
    return motif.sub(lambda trouve: valeurs[trouve.group(0)], consigne)


def charger_textes(config: dict, racine: Path) -> dict:
    """Vérifie devis, lot d'entrées, consignes et chaque consigne remplie ; rend {identifiant: entrée + texte envoyé}."""
    verifier_piece(racine, config["devis"], "devis")
    verifier_piece(racine, config["entrees"], "lot des entrées")
    lot = json.loads((racine / config["entrees"]["chemin"]).read_text(encoding="utf-8"))
    prereg = (racine / config["prereg"]["chemin"]).read_text(encoding="utf-8")
    consignes = {}
    for nom, c in config["consignes"].items():
        if lot["consignes"][nom]["sha256"] != c["sha256"]:
            raise Arret(f"consigne {nom} : le lot d'entrées et la configuration ne citent pas la même empreinte")
        consignes[nom] = extraire_consigne(prereg, c["lignes"], c["sha256"], nom)
    textes = {}
    for e in lot["entrees"]:
        if e["instrument"] == "appariement":
            valeurs = {"{title}": e["title"], "{proposal}": e["proposal"], "{controls}": e["controls"]}
        else:
            valeurs = {"{plan}": e["plan"], "{reference}": e["reference"]}
        texte = remplir(consignes[e["instrument"]], valeurs)
        octets = texte.encode("utf-8")
        if sha256_octets(octets) != e["consigne_remplie"]["sha256"] or len(octets) != e["consigne_remplie"]["octets"]:
            raise Arret(f"entrée {e['id']} : la consigne remplie ne répond pas à son empreinte")
        textes[e["id"]] = {"id": e["id"], "instrument": e["instrument"], "longueur": e["longueur"], "bloc": e["bloc"],
                           "cas": e.get("cas"), "identifiants": e.get("identifiants"), "texte": texte}
    if sorted(lot["ordre"]) != sorted(textes):
        raise Arret("l'ordre du lot ne couvre pas exactement ses entrées")
    return {"ordre": lot["ordre"], "textes": textes}


def entrees_de_la_file(file: dict, lot: dict) -> list:
    if file["entrees"] == "toutes":
        return list(lot["ordre"])
    inconnues = [i for i in file["entrees"] if i not in lot["textes"]]
    if inconnues:
        raise Arret(f"entrées inconnues dans la configuration : {inconnues}")
    return [i for i in lot["ordre"] if i in set(file["entrees"])]


# --- G7 : ligne de calcul ----------------------------------------------------------------------------------------------

def lire_registre_git(racine: Path, config: dict) -> str:
    ref = f"{config['registre_go']['reference_git']}:{config['registre_go']['chemin']}"
    try:
        return subprocess.run(["git", "-C", str(racine), "show", ref], check=True, capture_output=True, text=True).stdout
    except (subprocess.CalledProcessError, OSError) as erreur:
        raise Arret(f"registre des GO de la branche principale illisible ({type(erreur).__name__})") from None


def verifier_ligne_de_calcul(config: dict, nom: str, environnement, registre: str, aujourd_hui: str) -> str:
    """G7 : `GO_ID` égal à la ligne de la file ; ligne unique, de type calcul, au plafond de la file, non échue, citant
    l'empreinte du devis. Rend l'empreinte de la ligne."""
    file = config["files"][nom]
    attendu = file["go"]
    if environnement.get("GO_ID") != attendu:
        raise Arret(f"GO_ID absent ou différent de {attendu} : rien ne part")
    lignes = [l for l in registre.splitlines() if l.startswith(f"| {attendu} |")]
    if len(lignes) != 1:
        raise Arret(f"{len(lignes)} ligne(s) {attendu} au registre de la branche principale (une seule attendue)")
    colonnes = [c.strip() for c in lignes[0].strip().strip("|").split(" | ")]
    if len(colonnes) != 8:
        raise Arret(f"la ligne {attendu} n'a pas huit colonnes")
    identifiant, _accorde, type_, perimetre, plafond, echeance = colonnes[:6]
    if identifiant != attendu or type_ != "calcul":
        raise Arret(f"la ligne {attendu} n'est pas une ligne de calcul")
    if plafond != file["plafond_registre"]:
        raise Arret(f"la ligne {attendu} porte le plafond « {plafond} » au lieu de « {file['plafond_registre']} »")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", echeance) or aujourd_hui > echeance:
        raise Arret(f"la ligne {attendu} est échue ({echeance}) ou sans échéance lisible")
    if config["devis"]["sha256"] not in perimetre:
        raise Arret(f"la ligne {attendu} ne cite pas l'empreinte du devis")
    if any(l.startswith("|") and "| révocation |" in l and attendu in l for l in registre.splitlines()):
        raise Arret(f"la ligne {attendu} est révoquée")
    return sha256_octets(lignes[0].encode("utf-8"))


# --- G8 : clé Claude vérifiée ------------------------------------------------------------------------------------------

def verifier_cle(file: dict, environnement, racine: Path) -> None:
    """G8 (file Claude) : variable présente et non vide (présence seule : aucune partie de la valeur n'est lue ni
    affichée) ; relevé de vérification présent, d'empreinte égale à celle de la configuration et à son compagnon."""
    cle = file["cle"]
    if cle.get("factice"):
        return
    if not environnement.get(cle["variable"]):
        raise Arret(f"variable de clé {cle['variable']} absente ou vide : la file ne part pas")
    attestation = cle.get("attestation")
    if not attestation:
        return
    chemin = racine / attestation["chemin"]
    if not chemin.is_file():
        raise Arret(f"relevé de vérification de la clé absent ({attestation['chemin']}) : la file ne part pas")
    empreinte = sha256_fichier(chemin)
    if empreinte != attestation["sha256"]:
        raise Arret("relevé de vérification de la clé d'empreinte autre que celle de la configuration : la file ne part pas")
    compagnon = Path(str(chemin) + ".sha256")
    if not compagnon.is_file() or compagnon.read_text(encoding="utf-8").split()[0] != empreinte:
        raise Arret("relevé de vérification de la clé sans empreinte compagnon conforme : la file ne part pas")


# --- G5 : rien de personnel dans ce qui part ---------------------------------------------------------------------------

def _sortie_git(racine: Path, *arguments) -> str:
    try:
        return subprocess.run(["git", "-C", str(racine), *arguments], capture_output=True, text=True, timeout=20).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def charger_interdits(config: dict, racine: Path, environnement) -> list:
    """Liste des termes interdits : fichier local exigé (jamais envoyé ni versé), plus ce que le poste dit de lui-même
    (auteur et courriel de git, dépôt distant, branche, dossier du dépôt, nom de machine, variables de session)."""
    garde = config["garde_g5"]
    fichier = Path(garde["fichier_local"])
    if not fichier.is_file():
        raise Arret(f"liste locale des interdits absente ({fichier}) : rien ne part")
    termes = [l.strip() for l in fichier.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    if not termes:
        raise Arret("liste locale des interdits vide : rien ne part")
    derives = [_sortie_git(racine, "config", "user.name"), _sortie_git(racine, "config", "user.email"),
               _sortie_git(racine, "rev-parse", "--abbrev-ref", "HEAD"), racine.name, socket.gethostname()]
    distant = _sortie_git(racine, "config", "--get", "remote.origin.url")
    derives += [p for p in re.split(r"[/:@]", distant.removesuffix(".git")) if p]
    for nom, valeur in environnement.items():  # identifiants de session du poste ; jamais une variable de clé
        if (re.search(r"SESSION|USERNAME|LOGNAME|EMAIL|HOSTNAME", nom) and not re.search(r"KEY|TOKEN|SECRET|CLE", nom)
                and len(valeur.strip()) >= 8):
            derives.append(valeur)
    exemptes = {t.lower() for t in garde["termes_exemptes"]}
    retenus = set()
    for t in termes + derives:
        t = t.strip().lower()
        if len(t) >= garde["longueur_min_terme"] and t not in exemptes and not re.fullmatch(r"[\d.:]+", t):
            retenus.add(t)
    return sorted(retenus)


def controler_envoi(corps: bytes, en_tetes: dict, interdits: list) -> None:
    """G5 : refuse l'envoi si le corps ou un en-tête porte un terme interdit ou une forme interdite."""
    texte = corps.decode("utf-8", errors="replace") + "\n" + "\n".join(f"{k}: {v}" for k, v in en_tetes.items())
    bas = texte.lower()
    for t in interdits:
        if t in bas:
            raise Arret(f"G5 : un terme de la liste des interdits est dans ce qui partirait (rang {interdits.index(t)})")
    for nom, forme in FORMES_INTERDITES:
        if re.search(forme, texte):
            raise Arret(f"G5 : forme interdite dans ce qui partirait ({nom})")
    if en_tetes.get("User-Agent") != AGENT_UTILISATEUR:
        raise Arret("G5 : agent d'utilisateur non générique")


# --- corps, pire cas, compteur (G1, G3) --------------------------------------------------------------------------------

def construire_corps(file: dict, reglage: dict, texte: str, avec_temperature: bool) -> dict:
    fournisseur = file["fournisseur"]
    if fournisseur == "anthropic":
        corps = {"model": reglage["modele"], "max_tokens": reglage["sortie_max"],
                 "output_config": {"effort": reglage["effort"]}, "messages": [{"role": "user", "content": texte}]}
        if file["appel"]["flux"]:
            corps["stream"] = True
        return corps
    if fournisseur == "google":
        generation = {"maxOutputTokens": reglage["sortie_max"], "thinkingConfig": {"thinkingBudget": reglage["budget_reflexion"]}}
        if avec_temperature:
            generation["temperature"] = file["appel"]["temperature"]
        return {"contents": [{"role": "user", "parts": [{"text": texte}]}], "generationConfig": generation}
    if fournisseur == "openai":
        corps = {"model": reglage["modele"], "messages": [{"role": "user", "content": texte}],
                 "max_completion_tokens": reglage["sortie_max"]}
        if avec_temperature:
            corps["temperature"] = file["appel"]["temperature"]
        return corps
    raise Arret(f"fournisseur inconnu : {fournisseur}")


def sortie_max_du_corps(fournisseur: str, corps: dict):
    if fournisseur == "anthropic":
        return corps.get("max_tokens")
    if fournisseur == "google":
        return (corps.get("generationConfig") or {}).get("maxOutputTokens")
    return corps.get("max_completion_tokens")


def controler_corps(file: dict, reglage: dict, corps: dict) -> None:
    """G3 et devis 5.2 : sortie maximale présente et égale à celle du réglage ; aucun champ que le devis exclut."""
    fournisseur = file["fournisseur"]
    sortie = sortie_max_du_corps(fournisseur, corps)
    if not isinstance(sortie, int) or isinstance(sortie, bool) or sortie != reglage["sortie_max"]:
        raise Arret(f"G3 : sortie maximale {sortie!r} au lieu de {reglage['sortie_max']} : l'envoi ne part pas")
    if fournisseur == "anthropic":
        interdits = {"temperature", "top_p", "top_k", "thinking", "fallbacks", "betas", "metadata", "system", "tools"}
        if interdits & set(corps):
            raise Arret(f"corps Claude : champ exclu par le devis ({sorted(interdits & set(corps))})")
        if set(corps) - {"model", "max_tokens", "output_config", "messages", "stream"}:
            raise Arret("corps Claude : champ hors de la liste du devis")
    if fournisseur == "google":
        budget = corps["generationConfig"]["thinkingConfig"]["thinkingBudget"]
        if budget != reglage["budget_reflexion"] or reglage["sortie_max_comptee"] != reglage["sortie_max"] + budget:
            raise Arret("G3 : budget de réflexion ou sortie comptée de Carbon non conformes au réglage")
    elif reglage["sortie_max_comptee"] != reglage["sortie_max"]:
        raise Arret("G3 : sortie comptée différente de la sortie maximale envoyée")


def pire_cas_usd(octets_corps: int, sortie_comptee: int, prix: list) -> float:
    """Pire cas d'un envoi : un jeton d'entrée par octet du corps réel, sortie maximale comptée servie pleine."""
    return (octets_corps * prix[0] + sortie_comptee * prix[1]) / 1e6


class Compteur:
    """G1 : cumul compté par modèle et pour la file ; refuse avant l'envoi."""

    def __init__(self, plafond_file: float, plafonds_modeles: dict, depense: dict | None = None):
        self.plafond_file = plafond_file
        self.plafonds = dict(plafonds_modeles)
        self.depense = {m: 0.0 for m in plafonds_modeles}
        self.depense.update(depense or {})

    @property
    def total(self) -> float:
        return sum(self.depense.values())

    def motif_de_refus(self, modele: str, pire_cas: float):
        marge = 1e-9
        if self.depense[modele] + pire_cas > self.plafonds[modele] + marge:
            return (f"G1 : plafond du modèle {modele} ({self.plafonds[modele]} USD) : cumul {self.depense[modele]:.6f} "
                    f"+ pire cas {pire_cas:.6f}")
        if self.total + pire_cas > self.plafond_file + marge:
            return f"G1 : plafond de la file ({self.plafond_file} USD) : cumul {self.total:.6f} + pire cas {pire_cas:.6f}"
        return None

    def compter(self, modele: str, cout: float) -> None:
        self.depense[modele] += cout


# --- envoi (boucle locale, sans bibliothèque cliente, sans reprise) ----------------------------------------------------

def envoyer(url_relais: str, chemin: str, en_tetes: dict, corps: bytes, flux: bool, delai_silence_s: float,
            delai_total_s: float) -> dict:
    """Un envoi, et un seul. Rend code, en-têtes, corps reçu (même partiel), durée, et `incident` : None, « delai » ou
    « coupure ». Réponse en flux : chaque silence est borné par `delai_silence_s`, l'ensemble par `delai_total_s`.
    Réponse entière : le relais surveille le silence ; ici, seul le délai total borne l'attente."""
    parties = urllib.parse.urlsplit(url_relais)
    if parties.scheme != "http" or parties.hostname not in HOTES_LOCAUX:
        raise Arret(f"le chef d'essai ne parle qu'à la boucle locale, reçu {url_relais!r}")
    debut = time.monotonic()
    attente = delai_silence_s if flux else delai_total_s
    connexion = http.client.HTTPConnection(parties.hostname, parties.port, timeout=attente)
    sortie = {"code": None, "en_tetes": {}, "corps": b"", "incident": None, "detail": None}
    morceaux = []
    try:
        connexion.request("POST", chemin, body=corps, headers=en_tetes)
        reponse = connexion.getresponse()
        sortie["code"] = reponse.status
        sortie["en_tetes"] = {k.lower(): v for k, v in reponse.getheaders()}
        while True:
            if time.monotonic() - debut > delai_total_s:
                sortie["incident"], sortie["detail"] = "delai", "délai total dépassé"
                break
            morceau = reponse.read1(65536)
            if not morceau:
                break
            morceaux.append(morceau)
    except Interruption as signal_recu:
        sortie["incident"], sortie["detail"] = "interruption", str(signal_recu)
    except (socket.timeout, TimeoutError):
        sortie["incident"], sortie["detail"] = "delai", "silence au-delà du délai"
    except (OSError, http.client.HTTPException) as erreur:
        sortie["incident"], sortie["detail"] = "coupure", type(erreur).__name__
    finally:
        connexion.close()
    sortie["corps"] = b"".join(morceaux)
    sortie["duree_s"] = round(time.monotonic() - debut, 3)
    return sortie


# --- lecture technique d'une réponse -----------------------------------------------------------------------------------

def _entier(x):
    return x if isinstance(x, int) and not isinstance(x, bool) else None


def _json(octets: bytes):
    try:
        return json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return None


def lire_reponse(fournisseur: str, corps: bytes, type_contenu: str = "") -> dict:
    """Champs techniques d'un corps reçu avec le code 200. Le texte rendu par le modèle n'est gardé qu'en mémoire, pour
    la conformité de forme jugée par programme ; il n'entre ni au journal ni au rapport."""
    lu = {"lisible": False, "motif_fin": None, "modele_servi": None, "jetons_entree": None, "jetons_sortie": None,
          "jetons_reflexion": None, "jetons_reponse": None, "usage": {}, "refus_de_contenu": False, "texte": ""}
    if fournisseur == "anthropic":
        if "text/event-stream" in type_contenu or corps.lstrip().startswith((b"event:", b"data:")):
            return _lire_flux_anthropic(corps, lu)
        o = _json(corps)
        if not isinstance(o, dict) or not isinstance(o.get("usage"), dict):
            return lu
        lu["modele_servi"], lu["motif_fin"] = o.get("model"), o.get("stop_reason")
        lu["texte"] = "".join(b.get("text", "") for b in o.get("content") or [] if isinstance(b, dict) and b.get("type") == "text")
        return _finir_anthropic(lu, o["usage"], complet=o.get("stop_reason") is not None)
    o = _json(corps)
    if not isinstance(o, dict):
        return lu
    if fournisseur == "google":
        usage = o.get("usageMetadata") if isinstance(o.get("usageMetadata"), dict) else {}
        lu["usage"] = {k: v for k, v in usage.items() if _entier(v) is not None}
        candidats = o.get("candidates") if isinstance(o.get("candidates"), list) else []
        premier = candidats[0] if candidats and isinstance(candidats[0], dict) else {}
        lu["motif_fin"] = premier.get("finishReason")
        blocage = (o.get("promptFeedback") or {}).get("blockReason") if isinstance(o.get("promptFeedback"), dict) else None
        if blocage:
            lu["motif_fin"], lu["refus_de_contenu"] = f"blocage:{blocage}"[:60], True
        parties = (premier.get("content") or {}).get("parts") if isinstance(premier.get("content"), dict) else []
        lu["texte"] = "".join(p.get("text", "") for p in parties or []
                              if isinstance(p, dict) and isinstance(p.get("text"), str) and not p.get("thought"))
        version = o.get("modelVersion")
        lu["modele_servi"] = version.removeprefix("models/") if isinstance(version, str) else None
        entree, reponse = _entier(usage.get("promptTokenCount")), _entier(usage.get("candidatesTokenCount"))
        pensee = _entier(usage.get("thoughtsTokenCount"))
        if entree is None or (reponse is None and pensee is None):
            return lu
        lu.update(jetons_entree=entree, jetons_reponse=reponse or 0, jetons_reflexion=pensee or 0,
                  jetons_sortie=(reponse or 0) + (pensee or 0), lisible=True)
        return lu
    usage = o.get("usage") if isinstance(o.get("usage"), dict) else {}
    lu["usage"] = {k: v for k, v in usage.items() if _entier(v) is not None}
    choix = o.get("choices") if isinstance(o.get("choices"), list) else []
    premier = choix[0] if choix and isinstance(choix[0], dict) else {}
    message = premier.get("message") if isinstance(premier.get("message"), dict) else {}
    lu["motif_fin"], lu["modele_servi"] = premier.get("finish_reason"), o.get("model")
    lu["texte"] = message.get("content") if isinstance(message.get("content"), str) else ""
    if message.get("refusal"):
        lu["refus_de_contenu"] = True
    entree, sortie = _entier(usage.get("prompt_tokens")), _entier(usage.get("completion_tokens"))
    if entree is None or sortie is None:
        return lu
    details = usage.get("completion_tokens_details") if isinstance(usage.get("completion_tokens_details"), dict) else {}
    lu.update(jetons_entree=entree, jetons_sortie=sortie, jetons_reflexion=_entier(details.get("reasoning_tokens")),
              lisible=True)
    return lu


def _finir_anthropic(lu: dict, usage: dict, complet: bool) -> dict:
    lu["usage"] = {k: v for k, v in usage.items() if _entier(v) is not None}
    entree, sortie = _entier(usage.get("input_tokens")), _entier(usage.get("output_tokens"))
    if entree is None or sortie is None or not complet:
        return lu
    # Borne haute : les jetons de cache, s'il y en a, sont comptés au prix plein de l'entrée.
    entree += (_entier(usage.get("cache_creation_input_tokens")) or 0) + (_entier(usage.get("cache_read_input_tokens")) or 0)
    a_part = [v for k, v in lu["usage"].items() if "thinking" in k or "reasoning" in k]
    lu.update(jetons_entree=entree, jetons_sortie=sortie, jetons_reflexion=(a_part[0] if a_part else None), lisible=True)
    return lu


def _lire_flux_anthropic(corps: bytes, lu: dict) -> dict:
    usage, textes, fini, erreur = {}, [], False, False
    for ligne in corps.split(b"\n"):
        ligne = ligne.strip()
        if not ligne.startswith(b"data:"):
            continue
        e = _json(ligne[5:].strip())
        if not isinstance(e, dict):
            continue
        genre = e.get("type")
        if genre == "message_start":
            message = e.get("message") if isinstance(e.get("message"), dict) else {}
            lu["modele_servi"] = message.get("model")
            usage.update({k: v for k, v in (message.get("usage") or {}).items() if _entier(v) is not None})
        elif genre == "content_block_delta":
            delta = e.get("delta") if isinstance(e.get("delta"), dict) else {}
            if delta.get("type") == "text_delta" and isinstance(delta.get("text"), str):
                textes.append(delta["text"])
        elif genre == "message_delta":
            delta = e.get("delta") if isinstance(e.get("delta"), dict) else {}
            if delta.get("stop_reason") is not None:
                lu["motif_fin"] = delta.get("stop_reason")
            usage.update({k: v for k, v in (e.get("usage") or {}).items() if _entier(v) is not None})
        elif genre == "message_stop":
            fini = True
        elif genre == "error":
            erreur = True
            detail = e.get("error") if isinstance(e.get("error"), dict) else {}
            lu["erreur_de_flux"] = str(detail.get("type"))[:60]
    lu["texte"] = "".join(textes)
    return _finir_anthropic(lu, usage, complet=fini and not erreur and lu["motif_fin"] is not None)


def origine_et_erreur(corps: bytes) -> tuple:
    """Un refus écrit par un relais porte la clé « erreur » ; une erreur du fournisseur porte « error »."""
    o = _json(corps)
    if isinstance(o, dict) and "erreur" in o:
        return "relais", o
    return "amont", o if isinstance(o, dict) else {}


# --- conformité de forme, jugée par programme (préenregistrement, sections 3.2 et 3.3) ---------------------------------

class _CleEnDouble(ValueError):
    pass


def _sans_doublon(paires):
    vues = {}
    for k, v in paires:
        if k in vues:
            raise _CleEnDouble("clé en double")
        vues[k] = v
    return vues


def conformite_de_forme(instrument: str, texte: str, identifiants, coupee: bool) -> tuple:
    """Oui ou non, et un code de cause sans texte : vide, coupee, entouree, non_json, cles, valeurs. Un objet JSON et
    rien d'autre (blancs de bord tolérés ; bloc de code, texte autour, clé en double refusés)."""
    if not isinstance(texte, str) or not texte.strip():
        return False, "vide"
    try:
        o = json.loads(texte.strip(), object_pairs_hook=_sans_doublon)
    except _CleEnDouble:
        return False, "cles"
    except ValueError:
        if coupee:
            return False, "coupee"
        debut, fin = texte.find("{"), texte.rfind("}")
        if 0 <= debut < fin:
            try:
                json.loads(texte[debut:fin + 1])
                return False, "entouree"
            except ValueError:
                pass
        return False, "non_json"
    if not isinstance(o, dict):
        return False, "non_json"
    if instrument == "appariement":
        if sorted(o) != sorted(CLES_APPARIEMENT):
            return False, "cles"
        fit, spec, pq, cq = (o[k] for k in CLES_APPARIEMENT)
        if fit not in FITS:
            return False, "valeurs"
        if (fit == "answers") != isinstance(spec, bool) or (fit != "answers" and spec is not None):
            return False, "valeurs"
        if fit == "cannot_tell":
            return (True, None) if pq is None and cq is None else (False, "valeurs")
        return (True, None) if isinstance(pq, str) and isinstance(cq, str) else (False, "valeurs")
    if sorted(o) != sorted(identifiants or []):
        return False, "cles"
    for ident in identifiants:
        v = o[ident]
        if not isinstance(v, dict) or sorted(v) != sorted(CLES_COUVERTURE):
            return False, "cles"
        if v["content"] not in CONTENUS or (v["quote"] is not None and not isinstance(v["quote"], str)):
            return False, "valeurs"
        if v["content"] == "absent":
            if v["place"] is not None:
                return False, "valeurs"
        elif v["place"] not in PLACES:
            return False, "valeurs"
    return True, None


# --- décision après un envoi (G2, G3, G4) ------------------------------------------------------------------------------

def decider(config: dict, file: dict, reglage: dict, retour: dict, lu: dict | None, rang: int, premier_envoi: bool,
            temperature_envoyee: bool) -> dict:
    """Rend {suite, motif, origine, compte} ; `suite` ∈ lecture, reprise, lecture_perdue, retirer_temperature,
    arret_reglage, arret_modele, arret_file ; `compte` ∈ reel, pire_cas, zero."""
    codes = config["codes"]
    fournisseur = file["fournisseur"]
    motifs = config["motifs_de_fin"][fournisseur]
    if retour["incident"] == "interruption":
        return {"suite": "arret_file", "motif": "interruption pendant un envoi", "origine": None, "compte": "pire_cas"}
    if retour["incident"] is not None and retour["code"] != 200:
        suite = "reprise" if rang == 1 else "lecture_perdue"
        return {"suite": suite, "motif": f"{retour['incident']} ({retour['detail']})", "origine": None, "compte": "pire_cas",
                "delai": True}
    code = retour["code"]
    origine, erreur = origine_et_erreur(retour["corps"]) if code != 200 else ("amont", {})
    if code == 200:
        if (retour["incident"] is None and lu is not None and not lu["lisible"]
                and (lu["refus_de_contenu"] or lu["motif_fin"] in motifs["refus"])):
            return {"suite": "arret_modele", "motif": "refus de contenu (sans compteur lisible)", "origine": "amont",
                    "compte": "pire_cas"}
        if retour["incident"] is not None or lu is None or not lu["lisible"]:
            suite = "reprise" if rang == 1 else "lecture_perdue"
            cause = retour["incident"] or "réponse sans compteur lisible"
            return {"suite": suite, "motif": f"code 200, {cause}", "origine": "amont", "compte": "pire_cas",
                    "delai": retour["incident"] is not None}
        admis = file["modeles"][reglage["modele"]]["versions_servies_admises"]
        if lu["modele_servi"] not in admis:
            return {"suite": "arret_file", "motif": "modèle servi autre que le modèle demandé", "origine": "amont",
                    "compte": "reel"}
        if lu["jetons_sortie"] > reglage["sortie_max_comptee"]:
            return {"suite": "arret_file", "motif": "G3 : compteurs de sortie au-delà de la borne comptée (dépassement "
                    "consigné)", "origine": "amont", "compte": "reel"}
        if lu["refus_de_contenu"] or lu["motif_fin"] in motifs["refus"]:
            return {"suite": "arret_modele", "motif": "refus de contenu", "origine": "amont", "compte": "reel"}
        return {"suite": "lecture", "motif": None, "origine": "amont", "compte": "reel"}
    avant_amont = origine == "relais" and code not in codes["surcharge"]
    compte = "zero" if avant_amont else "pire_cas"
    if code in codes["surcharge"]:
        if origine == "relais" and erreur.get("modele_servi") is not None \
                and erreur.get("modele_servi") != erreur.get("modele_demande"):
            return {"suite": "arret_file", "motif": "modèle servi autre que le modèle demandé (relais)", "origine": origine,
                    "compte": "pire_cas"}
        suite = "reprise" if rang == 1 else "arret_reglage"
        return {"suite": suite, "motif": f"surcharge ou coupure, code {code}", "origine": origine, "compte": "pire_cas"}
    if code in codes["refus_de_compte"]:
        return {"suite": "arret_file", "motif": f"refus de compte, code {code}", "origine": origine, "compte": compte}
    if code == 400:
        nomme = "temperature" in json.dumps(erreur, ensure_ascii=False).lower()
        if premier_envoi and temperature_envoyee and origine == "amont" and nomme:
            regle = file["appel"]["cout_refus_400_temperature"]
            return {"suite": "retirer_temperature", "motif": "code 400 qui nomme la température", "origine": origine,
                    "compte": "pire_cas" if regle == "pire_cas" else "zero"}
        return {"suite": "arret_file", "motif": "code 400", "origine": origine, "compte": compte}
    return {"suite": "arret_file", "motif": f"code {code} non nommé : arrêt sans reprise", "origine": origine,
            "compte": compte}


# --- la file ------------------------------------------------------------------------------------------------------------

def jouer_file(config: dict, nom: str, lot: dict, dossier: Path, url_relais: str, interdits: list,
               envoyer_=envoyer, horloge=time.monotonic) -> dict:
    """Joue la file en série. Rend le bilan ; écrit journal, corps envoyés et réponses reçues dans `dossier`."""
    file = config["files"][nom]
    journal = Journal(dossier / "journal-essai.jsonl")
    compteur = Compteur(file["plafond_usd"], {m: d["plafond_usd"] for m, d in file["modeles"].items()})
    identifiants = entrees_de_la_file(file, lot)
    appel = file["appel"]
    temperature = appel.get("temperature") is not None
    etat = {"arret_file": None, "modeles_arretes": {}, "reglages_arretes": {}, "envois": 0, "lectures": 0,
            "temperature_retiree": False}
    debut = horloge()
    sequence = 0
    journal.ecrire(evenement="depart_de_la_file", file=nom, go=file["go"], reglages=[r["nom"] for r in file["reglages"]],
                   entrees=identifiants, plafond_usd=file["plafond_usd"])
    try:
        for reglage in file["reglages"]:
            if etat["arret_file"]:
                break
            modele = reglage["modele"]
            if modele in etat["modeles_arretes"]:
                journal.ecrire(evenement="reglage_non_joue", reglage=reglage["nom"], motif=etat["modeles_arretes"][modele])
                continue
            delais_de_suite = 0
            for ident in identifiants:
                if etat["arret_file"] or modele in etat["modeles_arretes"] or reglage["nom"] in etat["reglages_arretes"]:
                    break
                entree = lot["textes"][ident]
                rang = 1
                while True:
                    if horloge() - debut > config["delai_global_s"]:
                        etat["arret_file"] = "G2 : délai global de la file dépassé"
                        break
                    corps_objet = construire_corps(file, reglage, entree["texte"], temperature)
                    controler_corps(file, reglage, corps_objet)
                    corps = json.dumps(corps_objet, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
                    en_tetes = {"Content-Type": "application/json", "Content-Length": str(len(corps)),
                                "User-Agent": AGENT_UTILISATEUR, "Accept": "*/*", **appel["en_tetes"]}
                    controler_envoi(corps, en_tetes, interdits)
                    pire = pire_cas_usd(len(corps), reglage["sortie_max_comptee"], file["modeles"][modele]["prix"])
                    refus = compteur.motif_de_refus(modele, pire)
                    if refus:
                        etat["arret_file"] = refus
                        journal.ecrire(evenement="envoi_refuse_avant_depart", reglage=reglage["nom"], entree=ident,
                                       rang=rang, motif=refus, pire_cas_usd=round(pire, 6))
                        break
                    sequence += 1
                    base = f"{sequence:04d}-{ident}-{reglage['nom']}-e{rang}"
                    ecrire_neuf(dossier / "envois" / f"{base}.json", corps)
                    journal.ecrire(evenement="envoi", sequence=sequence, reglage=reglage["nom"], modele=modele, entree=ident,
                                   instrument=entree["instrument"], longueur=entree["longueur"], rang=rang,
                                   octets_corps=len(corps), sha256_corps=sha256_octets(corps),
                                   pire_cas_usd=round(pire, 6), cumul_modele_usd=round(compteur.depense[modele], 6),
                                   cumul_file_usd=round(compteur.total, 6), temperature=temperature)
                    etat["envois"] += 1
                    chemin = appel["chemin"].replace("{modele}", modele)
                    retour = envoyer_(url_relais, chemin, en_tetes, corps, appel["flux"],
                                      appel.get("delai_silence_s") or appel["delai_total_s"], appel["delai_total_s"])
                    brut = dossier / "reponses-brutes-non-lues"
                    ecrire_neuf(brut / f"{base}.corps", retour["corps"])
                    ecrire_neuf(brut / f"{base}.entetes.json", json_octets(
                        {"code": retour["code"], "en_tetes": retour["en_tetes"], "incident": retour["incident"],
                         "detail": retour["detail"]}))
                    lu = (lire_reponse(file["fournisseur"], retour["corps"], retour["en_tetes"].get("content-type", ""))
                          if retour["code"] == 200 else None)
                    decision = decider(config, file, reglage, retour, lu, rang, etat["envois"] == 1, temperature)
                    lisible = bool(lu and lu["lisible"])
                    prix = file["modeles"][modele]["prix"]
                    cout_calcule = ((lu["jetons_entree"] * prix[0] + lu["jetons_sortie"] * prix[1]) / 1e6
                                    if lisible else 0.0)
                    if decision["compte"] == "reel":
                        cout_compte = cout_calcule
                    else:
                        cout_compte = pire if decision["compte"] == "pire_cas" else 0.0
                    compteur.compter(modele, cout_compte)
                    releve = {"evenement": "retour", "sequence": sequence, "reglage": reglage["nom"], "modele": modele,
                              "entree": ident, "instrument": entree["instrument"], "longueur": entree["longueur"],
                              "rang": rang, "code": retour["code"], "origine": decision["origine"],
                              "incident": retour["incident"], "duree_s": retour["duree_s"],
                              "octets_reponse": len(retour["corps"]), "sha256_reponse": sha256_octets(retour["corps"]),
                              "suite": decision["suite"], "motif": decision["motif"], "compte": decision["compte"],
                              "cout_compte_usd": round(cout_compte, 8),
                              "cout_calcule_usd": round(cout_calcule, 8) if lisible else None,
                              "cumul_modele_usd": round(compteur.depense[modele], 6),
                              "cumul_file_usd": round(compteur.total, 6)}
                    if lu is not None:
                        motifs = config["motifs_de_fin"][file["fournisseur"]]
                        coupee = lu["motif_fin"] in motifs["sortie_max"]
                        releve.update(motif_fin=(str(lu["motif_fin"])[:60] if lu["motif_fin"] is not None else None),
                                      modele_servi=(str(lu["modele_servi"])[:80] if lu["modele_servi"] is not None else None),
                                      jetons_entree=lu["jetons_entree"], jetons_sortie=lu["jetons_sortie"],
                                      jetons_reflexion=lu["jetons_reflexion"], jetons_reponse=lu["jetons_reponse"],
                                      usage=lu["usage"], fin_par_sortie_max=coupee,
                                      fin_normale=lu["motif_fin"] in motifs["normaux"])
                        if lisible and decision["suite"] == "lecture":
                            conforme, cause = conformite_de_forme(entree["instrument"], lu["texte"], entree["identifiants"],
                                                                  coupee)
                            releve.update(conforme=conforme, cause_non_conformite=cause)
                        if lisible and file["fournisseur"] == "google":
                            releve.update(reflexion_au_dela_du_budget=lu["jetons_reflexion"] > reglage["budget_reflexion"],
                                          sortie_au_dela_de_la_sortie_max=lu["jetons_sortie"] > reglage["sortie_max"])
                    journal.ecrire(**releve)
                    suite = decision["suite"]
                    delais_de_suite = delais_de_suite + 1 if decision.get("delai") else 0
                    if suite == "lecture":
                        etat["lectures"] += 1
                        break
                    if suite == "retirer_temperature":
                        temperature, etat["temperature_retiree"] = False, True
                        journal.ecrire(evenement="temperature_retiree", file=nom, motif=decision["motif"])
                        continue
                    if delais_de_suite >= config["delais_de_suite_max"]:
                        etat["reglages_arretes"][reglage["nom"]] = "G2 : trois délais de suite"
                        break
                    if suite == "reprise":
                        rang = 2
                        continue
                    if suite == "arret_reglage":
                        etat["reglages_arretes"][reglage["nom"]] = decision["motif"]
                    elif suite == "arret_modele":
                        etat["modeles_arretes"][modele] = decision["motif"]
                    elif suite == "arret_file":
                        etat["arret_file"] = f"{decision['motif']} (origine : {decision['origine']})"
                    break
            for cle, motif in (("reglages_arretes", etat["reglages_arretes"].get(reglage["nom"])),
                               ("modeles_arretes", etat["modeles_arretes"].get(modele))):
                if motif:
                    journal.ecrire(evenement="arret", portee=cle, reglage=reglage["nom"], modele=modele, motif=motif)
    except Interruption as signal_recu:
        etat["arret_file"] = f"interruption ({signal_recu})"
    except Arret as garde:
        etat["arret_file"] = str(garde)
    complet = (not etat["arret_file"] and not etat["modeles_arretes"] and not etat["reglages_arretes"]
               and etat["lectures"] == len(identifiants) * len(file["reglages"]))
    bilan = {"file": nom, "complet": complet, "arret_file": etat["arret_file"], "modeles_arretes": etat["modeles_arretes"],
             "reglages_arretes": etat["reglages_arretes"], "envois": etat["envois"], "lectures": etat["lectures"],
             "temperature_retiree": etat["temperature_retiree"], "depense_comptee_usd": round(compteur.total, 6),
             "depense_par_modele_usd": {m: round(v, 6) for m, v in compteur.depense.items()}}
    journal.ecrire(evenement="fin_de_la_file", **bilan)
    return bilan


# --- relais : lancement, état, arrêt par identifiant de processus (R10) -------------------------------------------------

def charger_lanceur(racine: Path, config: dict):
    verifier_piece(racine, config["lanceur_relais"], "lanceur de relais")
    spec = importlib.util.spec_from_file_location("lancer_relais_local_v1", racine / config["lanceur_relais"]["chemin"])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lancer_relais(config: dict, nom: str, racine: Path, dossier: Path, environnement) -> dict:
    """Lance le relais de la file par le lanceur de relais : environnement réduit à des noms, clé **exigée par son
    nom**. Pour une clé factice (GPT), la valeur factice de la configuration est posée sous le nom de la variable,
    quelle que soit la valeur présente : aucune valeur de clé du conteneur n'est transmise."""
    file = config["files"][nom]
    relais = file["relais"]
    verifier_piece(racine, relais, "relais")
    for piece in relais.get("autres_pieces", []):
        verifier_piece(racine, piece, "pièce du relais")
    lanceur = charger_lanceur(racine, config)
    source = dict(environnement)
    variable = file["cle"]["variable"]
    if file["cle"].get("factice"):
        source[variable] = file["cle"]["valeur_factice"]
    (dossier / "relais").mkdir(parents=True, exist_ok=True)
    console = dossier / "relais" / "console-relais.txt"
    journal = dossier / "relais" / "journal-relais.jsonl"
    commande = [sys.executable, "-I", "-B", str(racine / relais["chemin"]), *relais["arguments"],
                relais["option_journal"], str(journal)]
    noms = list(relais["noms_environnement"]) + ["!" + variable]
    try:
        lance = lanceur.lancer(str(console), noms, commande, source=source)
    except lanceur.Refus as refus:
        raise Arret(f"G6 : le lanceur de relais refuse ({refus}) : rien ne part") from None
    del source
    return {"pid": lance["pid"], "console": console, "journal": journal, "noms_transmis": lance["noms_transmis"]}


def attendre_relais(console: Path, pid: int, delai_s: float = 20.0) -> str:
    fin = time.monotonic() + delai_s
    while time.monotonic() < fin:
        texte = console.read_text(encoding="utf-8", errors="replace") if console.exists() else ""
        trouve = re.search(r"relais prêt sur (http://127\.0\.0\.1:\d+)", texte)
        if trouve:
            return trouve.group(1)
        if not processus_vivant(pid):
            break
        time.sleep(0.1)
    raise Arret("le relais n'a pas annoncé son adresse : rien ne part")


def etat_relais(url: str) -> dict:
    parties = urllib.parse.urlsplit(url)
    if parties.hostname not in HOTES_LOCAUX:
        raise Arret("état du relais : boucle locale seulement")
    connexion = http.client.HTTPConnection(parties.hostname, parties.port, timeout=10)
    try:
        connexion.request("GET", "/relais/etat", headers={"User-Agent": AGENT_UTILISATEUR})
        reponse = connexion.getresponse()
        return json.loads(reponse.read().decode("utf-8"))
    finally:
        connexion.close()


def controler_etat_initial(etat: dict, attendu: dict) -> None:
    for cle, valeur in attendu.items():
        recu = etat.get(cle)
        egal = sorted(recu) == sorted(valeur) if isinstance(valeur, list) and isinstance(recu, list) else recu == valeur
        if not egal:
            raise Arret(f"relais : état initial inattendu pour « {cle} » ({recu!r} au lieu de {valeur!r}) : rien ne part")


def processus_vivant(pid: int) -> bool:
    try:
        fini, _ = os.waitpid(pid, os.WNOHANG)
        if fini == pid:
            return False
    except ChildProcessError:
        pass
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    try:
        return Path(f"/proc/{pid}/stat").read_text().rsplit(")", 1)[1].split()[0] != "Z"
    except (OSError, IndexError):
        return True


def arreter_relais(pid: int) -> dict:
    """Arrêt par identifiant de processus (R10) : interruption, puis terminaison si le processus vit encore."""
    signaux = []
    for signal_envoye in (signal.SIGINT, signal.SIGTERM, signal.SIGKILL):
        if not processus_vivant(pid):
            break
        try:
            os.kill(pid, signal_envoye)
            signaux.append(signal_envoye.name)
        except ProcessLookupError:
            break
        fin = time.monotonic() + 5
        while time.monotonic() < fin and processus_vivant(pid):
            time.sleep(0.1)
    return {"pid": pid, "signaux": signaux, "arrete": not processus_vivant(pid), "quand": heure()}


# --- inventaire, recherche de clés, rapport -----------------------------------------------------------------------------

def chercher_formes_de_cle(dossier: Path) -> list:
    """G6 : toute chaîne de la forme d'une clé dans ce que la course a écrit ; rend les chemins, jamais la chaîne."""
    trouves = []
    for chemin in sorted(p for p in dossier.rglob("*") if p.is_file()):
        contenu = chemin.read_bytes().decode("utf-8", errors="replace")
        if any(re.search(forme, contenu) for forme in FORMES_DE_CLE):
            trouves.append(str(chemin.relative_to(dossier)))
    return trouves


def inventorier(dossier: Path, etat: str) -> dict:
    """Inventaire de tout ce que la course a produit (nom, taille, empreinte), avec son empreinte compagnon. Une course
    arrêtée s'inventorie comme une course finie : c'est la première chose faite, et rien n'est supprimé."""
    nom = "inventaire.json"
    fichiers = []
    for chemin in sorted(p for p in dossier.rglob("*") if p.is_file()):
        relatif = str(chemin.relative_to(dossier))
        if relatif in (nom, nom + ".sha256"):
            continue
        fichiers.append({"chemin": relatif, "octets": chemin.stat().st_size, "sha256": sha256_fichier(chemin)})
    inventaire = {"version": VERSION, "quand": heure(), "etat": etat, "fichiers": fichiers, "nombre": len(fichiers)}
    octets = json_octets(inventaire)
    cible = dossier / nom
    with open(cible, "wb") as f:
        f.write(octets)
        f.flush()
        os.fsync(f.fileno())
    (dossier / (nom + ".sha256")).write_text(f"{sha256_octets(octets)}  {nom}\n", encoding="utf-8")
    return inventaire


def _moyenne(valeurs):
    valeurs = [v for v in valeurs if v is not None]
    return sum(valeurs) / len(valeurs) if valeurs else None


def faire_rapport(dossier: Path, config: dict) -> dict:
    """Rapport technique, tiré du seul journal : aucun texte de réponse. Une lecture reprise compte par son dernier envoi
    pour les compteurs, par tous ses envois pour le coût."""
    lignes = lire_journal(dossier / "journal-essai.jsonl")
    depart = next((l for l in lignes if l["evenement"] == "depart_de_la_file"), None)
    if depart is None:
        raise Arret("journal sans départ de file : pas de rapport")
    nom = depart["file"]
    file = config["files"][nom]
    retours = [l for l in lignes if l["evenement"] == "retour"]
    fin = next((l for l in lignes if l["evenement"] == "fin_de_la_file"), None)
    reglages = {}
    for reglage in file["reglages"]:
        siens = [r for r in retours if r["reglage"] == reglage["nom"]]
        lectures = {}
        for r in siens:
            l = lectures.setdefault(r["entree"], {"entree": r["entree"], "instrument": r["instrument"],
                                                  "longueur": r["longueur"], "envois": 0, "cout_calcule_usd": 0.0,
                                                  "envois_sans_compteur": 0})
            l["envois"] += 1
            if r.get("cout_calcule_usd") is None:
                l["envois_sans_compteur"] += 1
            else:
                l["cout_calcule_usd"] += r["cout_calcule_usd"]
            l["dernier"] = {k: r.get(k) for k in (
                "code", "origine", "incident", "suite", "motif_fin", "modele_servi", "jetons_entree", "jetons_sortie",
                "jetons_reflexion", "jetons_reponse", "duree_s", "fin_par_sortie_max", "fin_normale", "conforme",
                "cause_non_conformite", "reflexion_au_dela_du_budget", "sortie_au_dela_de_la_sortie_max")}
        liste = [lectures[i] for i in depart["entrees"] if i in lectures]
        rendues = [l for l in liste if l["dernier"]["suite"] == "lecture"]
        refus = [r for r in siens if r["suite"] == "arret_modele" or (r["suite"] == "arret_file" and "refus" in (r["motif"] or ""))]
        par_instrument = {}
        for instrument in ("appariement", "couverture"):
            du_genre = [l for l in rendues if l["instrument"] == instrument]
            par_longueur = {}
            for longueur in ("courte", "mediane", "longue"):
                dans = [l for l in du_genre if l["longueur"] == longueur]
                par_longueur[longueur] = {
                    "lectures": len(dans),
                    "sortie_moyenne": _moyenne([l["dernier"]["jetons_sortie"] for l in dans]),
                    "entree_moyenne": _moyenne([l["dernier"]["jetons_entree"] for l in dans]),
                    "cout_moyen_usd": _moyenne([l["cout_calcule_usd"] for l in dans])}
            sorties = [l["dernier"]["jetons_sortie"] for l in du_genre]
            reponses = [l["dernier"]["jetons_reponse"] for l in du_genre if l["dernier"]["jetons_reponse"] is not None]
            par_instrument[instrument] = {
                "lectures": len(du_genre), "par_longueur": par_longueur,
                "sortie_moyenne_simple": _moyenne(sorties), "sortie_max": max(sorties) if sorties else None,
                "reponse_seule_max": max(reponses) if reponses else None,
                "non_conformes": sum(1 for l in du_genre if l["dernier"]["conforme"] is False)}
        attendues = len(depart["entrees"])
        conformes = sum(1 for l in rendues if l["dernier"]["conforme"] is True)
        fins_max = sum(1 for l in rendues if l["dernier"]["fin_par_sortie_max"])
        seuil = config["regle"]["conformite_min_sur_24"] if attendues == 24 else math.ceil(attendues * 22 / 24)
        reglages[reglage["nom"]] = {
            "modele": reglage["modele"], "reglage": {k: v for k, v in reglage.items() if k not in ("nom", "modele")},
            "lectures_attendues": attendues, "lectures_rendues": len(rendues), "envois": len(siens),
            "refus": len(refus), "fins_par_sortie_max": fins_max, "conformes": conformes,
            "codes": sorted({str(r["code"]) for r in siens}),
            "versions_servies": sorted({r["modele_servi"] for r in siens if r.get("modele_servi")}),
            "duree_moyenne_s": _moyenne([l["dernier"]["duree_s"] for l in rendues]),
            "cout_compte_usd": round(sum(r["cout_compte_usd"] for r in siens), 6),
            "reflexions_au_dela_du_budget": sum(1 for r in siens if r.get("reflexion_au_dela_du_budget")),
            "sorties_au_dela_de_la_sortie_max": sum(1 for r in siens if r.get("sortie_au_dela_de_la_sortie_max")),
            "tient": (len(rendues) == attendues and not refus and fins_max == 0 and conformes >= seuil),
            "par_instrument": par_instrument, "lectures": liste}
    rapport = {"version": VERSION, "file": nom, "go": file["go"], "fait": heure(), "bilan": fin,
               "arrets": [l for l in lignes if l["evenement"] in ("arret", "envoi_refuse_avant_depart", "temperature_retiree",
                                                                 "reglage_non_joue")],
               "reglages": reglages,
               "reserves": ["textes synthétiques : la moyenne mesurée peut sous-estimer celle des actions réelles",
                            "le rapport ne juge pas la qualité des lecteurs"]}
    return rapport


def texte_du_rapport(rapport: dict) -> str:
    lignes = [f"# Essai de mesure des lecteurs du bras A — rapport technique de la file {rapport['file']}", "",
              f"Ligne de calcul : {rapport['go']}. Fait le {rapport['fait']}. Champs techniques seulement.", "",
              "| réglage | modèle | lectures rendues | envois | refus | fins par sortie maximale | conformes | tient | "
              "sortie moyenne (appariement) | sortie maximale | coût compté (USD) |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for nom, r in rapport["reglages"].items():
        a = r["par_instrument"]["appariement"]
        moyenne = "—" if a["sortie_moyenne_simple"] is None else f"{a['sortie_moyenne_simple']:.0f}"
        lignes.append(f"| {nom} | {r['modele']} | {r['lectures_rendues']} sur {r['lectures_attendues']} | {r['envois']} | "
                      f"{r['refus']} | {r['fins_par_sortie_max']} | {r['conformes']} | {'oui' if r['tient'] else 'non'} | "
                      f"{moyenne} | {a['sortie_max'] if a['sortie_max'] is not None else '—'} | {r['cout_compte_usd']} |")
    bilan = rapport["bilan"] or {}
    lignes += ["", f"Bilan : complet = {bilan.get('complet')}, arrêt de la file = {bilan.get('arret_file')}, "
               f"dépense comptée = {bilan.get('depense_comptee_usd')} USD.", ""]
    return "\n".join(lignes)


def textes_des_reponses(dossier: Path, fournisseur: str) -> list:
    """Textes rendus par les modèles, relus par programme dans les corps bruts, pour le seul contrôle de sous-chaîne."""
    textes = []
    for chemin in sorted((dossier / "reponses-brutes-non-lues").glob("*.corps")):
        lu = lire_reponse(fournisseur, chemin.read_bytes())
        if lu["texte"]:
            textes.append(lu["texte"])
    return textes


def controler_aucune_sous_chaine(ecrit: str, textes: list, fenetre: int = FENETRE_SOUS_CHAINE) -> int:
    """Nombre de fenêtres de `fenetre` caractères d'une réponse retrouvées dans `ecrit` (zéro exigé)."""
    trouvees = 0
    for texte in textes:
        vues = set()
        for i in range(max(0, len(texte) - fenetre + 1)):
            morceau = texte[i:i + fenetre]
            if morceau.strip() and morceau not in vues:
                vues.add(morceau)
                if morceau in ecrit:
                    trouvees += 1
    return trouvees


def ecrire_rapport(dossier: Path, config: dict) -> dict:
    rapport = faire_rapport(dossier, config)
    octets_json, texte = json_octets(rapport), texte_du_rapport(rapport)
    fournisseur = config["files"][rapport["file"]]["fournisseur"]
    trouvees = controler_aucune_sous_chaine(octets_json.decode("utf-8") + texte, textes_des_reponses(dossier, fournisseur))
    if trouvees:
        raise Arret(f"le rapport contiendrait {trouvees} sous-chaîne(s) de réponse : il n'est pas écrit")
    for nom, octets in (("rapport-technique.json", octets_json), ("rapport-technique.md", texte.encode("utf-8"))):
        with open(dossier / nom, "wb") as f:
            f.write(octets)
    return rapport


# --- règle de choix (devis, section 7), sur les seuls rapports -----------------------------------------------------------

def _pondere(par_longueur: dict, champ: str):
    """Moyenne pondérée ¼ courte, ½ médiane, ¼ longue des moyennes simples par longueur."""
    c, m, l = (par_longueur[k][champ] for k in ("courte", "mediane", "longue"))
    return None if None in (c, m, l) else 0.25 * c + 0.5 * m + 0.25 * l


def mesures_du_reglage(r: dict, regle: dict) -> dict:
    a, c = r["par_instrument"]["appariement"], r["par_instrument"]["couverture"]
    s_a = _pondere(a["par_longueur"], "sortie_moyenne")
    cout_a = _pondere(a["par_longueur"], "cout_moyen_usd")
    cout_c = _moyenne([c["par_longueur"][k]["cout_moyen_usd"] for k in ("courte", "mediane", "longue")])
    projete = None
    if cout_a is not None and cout_c is not None and a["lectures"] and c["lectures"]:
        projete = (regle["lectures_appariement"] * cout_a * (1 + a["non_conformes"] / a["lectures"])
                   + regle["lectures_couverture"] * cout_c * (1 + c["non_conformes"] / c["lectures"]))
    sorties = [x for x in (a["sortie_max"], c["sortie_max"]) if x is not None]
    reponses = [x for x in (a["reponse_seule_max"], c["reponse_seule_max"]) if x is not None]
    return {"tient": r["tient"], "S_a": s_a, "C_usd": projete, "sortie_max_observee": max(sorties) if sorties else None,
            "reponse_seule_max_observee": max(reponses) if reponses else None}


def _sortie_maximale(observee, regle: dict):
    if observee is None:
        return None
    return max(regle["sortie_max_plancher"], 1024 * math.ceil(regle["sortie_max_facteur"] * observee / 1024))


def appliquer_regle(config: dict, rapport_claude: dict | None, rapport_carbon: dict | None) -> dict:
    """Règle écrite d'avance (devis, 7.3). Elle ne lit que des compteurs."""
    regle = config["regle"]
    sortie = {"version": VERSION, "seuil_S_a": regle["seuil_s_a"], "claude": None, "carbon": None}
    if rapport_claude is not None:
        retenus, details = {}, {}
        for modele, noms in regle["reglages_par_modele"].items():
            for effort in ("bas", "moyen"):
                nom = noms.get(effort)
                if nom and nom in rapport_claude["reglages"]:
                    m = mesures_du_reglage(rapport_claude["reglages"][nom], regle)
                    details[nom] = m
                    if m["tient"] and modele not in retenus:
                        retenus[modele] = {"reglage": nom, "effort": effort, **m}
        opus, sonnet = retenus.get(regle["modele_opus"]), retenus.get(regle["modele_sonnet"])
        seuil = regle["seuil_s_a"]
        if opus and opus["S_a"] is not None and opus["S_a"] <= seuil:
            choix, motif = regle["modele_opus"], "point 2 : S_a d'Opus 5.5 sous le seuil"
        elif opus:
            sous_seuil = bool(sonnet and sonnet["S_a"] is not None and sonnet["S_a"] <= seuil)
            moitie = bool(sonnet and sonnet["C_usd"] is not None and opus["C_usd"] is not None
                          and sonnet["C_usd"] <= opus["C_usd"] / 2)
            if sous_seuil or moitie:
                choix, motif = regle["modele_sonnet"], "point 3 : Opus 5.5 au-dessus du seuil ; Sonnet 5.5 sous le seuil ou à la moitié du coût"
            else:
                choix, motif = None, "point 4 : aucun des deux n'est retenu ; nœud de Lazar"
        elif sonnet:
            choix, motif = regle["modele_sonnet"], "point 4 : Opus 5.5 écarté, Sonnet 5.5 tient"
        else:
            choix, motif = None, "point 4 : aucun réglage ne tient ; nœud de Lazar"
        retenu = retenus.get(choix) if choix else None
        sortie["claude"] = {"choix": choix, "motif": motif, "reglage": retenu["reglage"] if retenu else None,
                            "sortie_maximale_du_devis_des_lectures": _sortie_maximale(
                                retenu["sortie_max_observee"], regle) if retenu else None,
                            "efforts_retenus": retenus, "mesures": details,
                            "jamais_retenus_par_la_regle": regle["jamais_retenus"]}
    if rapport_carbon is not None:
        choix, details = None, {}
        for nom in regle["reglages_carbon"]:
            if nom in rapport_carbon["reglages"]:
                details[nom] = mesures_du_reglage(rapport_carbon["reglages"][nom], regle)
                if details[nom]["tient"] and choix is None:
                    choix = nom
        sortie["carbon"] = {"choix": choix, "motif": "point 6" if choix else "point 6 : aucun budget ne tient ; nœud de Lazar",
                            "sortie_maximale_du_devis_des_lectures": _sortie_maximale(
                                details[choix]["reponse_seule_max_observee"], regle) if choix else None,
                            "mesures": details}
    return sortie


def controler_tous_les_corps(config: dict, nom: str, lot: dict, interdits: list) -> dict:
    """Avant tout envoi : chaque corps que la file peut envoyer passe G3 et G5 ; rend le pire cas de la file entière
    (deux envois par appel)."""
    file = config["files"][nom]
    total, nombre = 0.0, 0
    for reglage in file["reglages"]:
        for ident in entrees_de_la_file(file, lot):
            for avec_temperature in ({True, False} if file["appel"].get("temperature") is not None else {False}):
                objet = construire_corps(file, reglage, lot["textes"][ident]["texte"], avec_temperature)
                controler_corps(file, reglage, objet)
                corps = json.dumps(objet, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
                controler_envoi(corps, {"Content-Type": "application/json", "User-Agent": AGENT_UTILISATEUR,
                                        **file["appel"]["en_tetes"]}, interdits)
            total += 2 * pire_cas_usd(len(corps), reglage["sortie_max_comptee"], file["modeles"][reglage["modele"]]["prix"])
            nombre += 1
    return {"appels": nombre, "pire_cas_usd": round(total, 4)}


# --- amorce : gardes de départ, relais, ouvrier, fin ---------------------------------------------------------------------

def dossiers_deja_joues(base: Path, nom: str) -> list:
    return sorted(str(p) for p in base.glob(f"*-file-{nom}")) if base.is_dir() else []


def executer(nom: str, environnement, racine: Path = RACINE, chemin_configuration: Path | None = None,
             empreinte_configuration: str = EMPREINTE_CONFIGURATION, registre: str | None = None,
             aujourd_hui: str | None = None, commande_ouvrier=None) -> int:
    """Joue une file de bout en bout. Les paramètres autres que `nom` et `environnement` ne servent qu'aux essais :
    la ligne de commande ne les expose pas."""
    chemin_configuration = Path(chemin_configuration or racine / CONFIGURATION)
    dossier, relais, code = None, None, 2
    try:
        if nom not in FILES:
            raise Arret(f"file inconnue : {nom!r} (claude, carbon ou gpt)")
        config = charger_configuration(chemin_configuration, empreinte_configuration)
        file = config["files"][nom]
        empreinte_ligne = verifier_ligne_de_calcul(
            config, nom, environnement, registre if registre is not None else lire_registre_git(racine, config),
            aujourd_hui or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"))
        lot = charger_textes(config, racine)
        entrees_de_la_file(file, lot)
        verifier_piece(racine, file["relais"], "relais")
        for page in file.get("pages_de_prix", []):  # devis, 6.1 : sans page conforme, le prix compté ne vaut plus
            verifier_piece(racine, page, "page de prix")
        charger_lanceur(racine, config)
        interdits = charger_interdits(config, racine, environnement)
        prevu = controler_tous_les_corps(config, nom, lot, interdits)
        verifier_cle(file, environnement, racine)
        base = racine / config["dossier_des_courses"]
        deja = dossiers_deja_joues(base, nom)
        if deja:
            raise Arret(f"la file {nom} a déjà un dossier de course ({deja[0]}) : une ligne ne se rejoue pas")
        dossier = base / f"{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d-%H%M%S')}-file-{nom}"
        dossier.mkdir(parents=True)
    except Arret as garde:
        print(f"ARRÊT avant tout envoi : {garde}", file=sys.stderr)
        return 2
    journal = Journal(dossier / "journal-amorce.jsonl")
    processus = None
    recu = {"signal": None}

    def sur_signal(numero, cadre):
        recu["signal"] = numero
        if processus is not None and processus.poll() is None:
            processus.send_signal(signal.SIGTERM)

    anciens = {s: signal.signal(s, sur_signal) for s in (signal.SIGINT, signal.SIGTERM)}
    etat_final = "interrompue"
    try:
        commit = _sortie_git(racine, "rev-parse", "HEAD")
        manifeste = {
            "version": VERSION, "file": nom, "go": file["go"], "empreinte_ligne_go": empreinte_ligne, "depart": heure(),
            "commit": commit, "python": sys.version.split()[0], "pid_amorce": os.getpid(),
            "configuration": {"chemin": str(chemin_configuration), "sha256": empreinte_configuration},
            "chef": {"chemin": str(Path(__file__).resolve()), "sha256": sha256_fichier(__file__)},
            "devis": config["devis"], "entrees": config["entrees"], "consignes": config["consignes"],
            "relais": {"chemin": file["relais"]["chemin"], "sha256": file["relais"]["sha256"],
                       "arguments": file["relais"]["arguments"]},
            "cle": {"variable": file["cle"]["variable"], "factice": bool(file["cle"].get("factice")),
                    "attestation": file["cle"].get("attestation")},
            "interdits_g5": {"nombre": len(interdits), "sha256": sha256_octets("\n".join(interdits).encode("utf-8"))},
            "prevu": prevu,
            "graines": "aucun tirage dans le chef d'essai ; graines des textes dans le lot des entrées (R9)",
        }
        ecrire_neuf(dossier / "manifeste-depart.json", json_octets(manifeste))
        relais = lancer_relais(config, nom, racine, dossier, environnement)
        journal.ecrire(evenement="relais_lance", pid=relais["pid"], noms_transmis=relais["noms_transmis"])
        url = attendre_relais(relais["console"], relais["pid"])
        initial = etat_relais(url)
        ecrire_neuf(dossier / "relais" / "etat-initial.json", json_octets(initial))
        controler_etat_initial(initial, file["relais"]["etat_attendu"])
        journal.ecrire(evenement="relais_pret", url=url)
        if recu["signal"] is not None:
            raise Arret(f"signal {recu['signal']} avant le départ de l'ouvrier")
        commande = (commande_ouvrier or [sys.executable, "-I", "-B", str(Path(__file__).resolve()), "--ouvrier"]) + [str(dossier)]
        env_ouvrier = {k: environnement[k] for k in ENVIRONNEMENT_OUVRIER if k in environnement}
        entree = json.dumps({"url_relais": url, "interdits": interdits, "racine": str(racine)}).encode("utf-8")
        processus = subprocess.Popen(commande, env=env_ouvrier, stdin=subprocess.PIPE, cwd=str(racine))
        processus.stdin.write(entree)
        processus.stdin.close()
        while processus.poll() is None:
            time.sleep(0.2)
        journal.ecrire(evenement="ouvrier_fini", code=processus.returncode, signal_recu=recu["signal"])
        code = processus.returncode if recu["signal"] is None else 3
        etat_final = "finie" if code == 0 else "arretee"
    except Arret as garde:
        journal.ecrire(evenement="arret", motif=str(garde))
        print(f"ARRÊT : {garde}", file=sys.stderr)
        code, etat_final = 2, "arretee"
    except BaseException as panne:  # noqa: BLE001 — tout se termine par l'inventaire, quelle que soit la panne
        journal.ecrire(evenement="panne", genre=type(panne).__name__)
        code, etat_final = 4, "arretee"
    finally:
        # Récupération d'abord : état du relais, arrêt par identifiant de processus, recherche de clés, rapport,
        # inventaire. Chaque étape est tentée même si la précédente échoue ; rien n'est supprimé.
        for s, ancien in anciens.items():
            signal.signal(s, ancien)
        if processus is not None and processus.poll() is None:
            processus.terminate()
            try:
                processus.wait(timeout=30)
            except subprocess.TimeoutExpired:
                processus.kill()
        if relais is not None:
            try:
                url_lue = attendre_relais(relais["console"], relais["pid"], delai_s=1.0)
                with open(dossier / "relais" / "etat-final.json", "wb") as f:
                    f.write(json_octets(etat_relais(url_lue)))
            except (Arret, OSError, ValueError, http.client.HTTPException) as erreur:
                journal.ecrire(evenement="etat_final_du_relais_illisible", genre=type(erreur).__name__)
            arret = arreter_relais(relais["pid"])
            journal.ecrire(evenement="relais_arrete", **arret)
            if not arret["arrete"]:
                code = code or 5
        try:
            cles = chercher_formes_de_cle(dossier)
            journal.ecrire(evenement="recherche_de_formes_de_cle", fichiers=cles)
            if cles:
                print(f"ARRÊT : chaîne de la forme d'une clé dans {cles} — ne rien pousser avant examen", file=sys.stderr)
                code = 6
        except OSError as erreur:
            journal.ecrire(evenement="recherche_de_formes_de_cle_impossible", genre=type(erreur).__name__)
        try:
            if (dossier / "journal-essai.jsonl").exists():
                ecrire_rapport(dossier, config)
        except (Arret, OSError, KeyError, ValueError) as erreur:
            journal.ecrire(evenement="rapport_non_ecrit", motif=str(erreur)[:200])
            code = code or 7
        journal.ecrire(evenement="fin", code=code, etat=etat_final)
        inventaire = inventorier(dossier, etat_final)
    print(json.dumps({"file": nom, "code": code, "etat": etat_final, "dossier": str(dossier),
                      "fichiers_inventories": inventaire["nombre"]}, ensure_ascii=False))
    return code


def ouvrier(dossier: Path, environnement, entree: bytes) -> int:
    """L'ouvrier : environnement réduit, aucune clé ; il revérifie la configuration et les textes, puis joue la file."""
    if any(re.search(r"KEY|TOKEN|SECRET", k) for k in environnement):
        print("ARRÊT : l'ouvrier ne part pas avec un nom de clé dans son environnement", file=sys.stderr)
        return 2
    try:
        manifeste = json.loads((dossier / "manifeste-depart.json").read_text(encoding="utf-8"))
        if manifeste["pid_amorce"] != os.getppid() or environnement.get("GO_ID") != manifeste["go"]:
            raise Arret("l'ouvrier n'est lancé que par son amorce, sous la ligne de calcul de la file")
        donnees = json.loads(entree.decode("utf-8"))
        racine = Path(donnees["racine"])
        config = charger_configuration(Path(manifeste["configuration"]["chemin"]), manifeste["configuration"]["sha256"])
        lot = charger_textes(config, racine)
    except (Arret, OSError, ValueError, KeyError) as garde:
        print(f"ARRÊT de l'ouvrier avant tout envoi : {garde}", file=sys.stderr)
        return 2
    signal.signal(signal.SIGTERM, _lever_interruption)
    signal.signal(signal.SIGINT, _lever_interruption)
    bilan = jouer_file(config, manifeste["file"], lot, dossier, donnees["url_relais"], donnees["interdits"])
    return 0 if bilan["complet"] else 1


def principal(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) == 1 and argv[0] in FILES:
        return executer(argv[0], os.environ)
    if len(argv) == 2 and argv[0] == "--ouvrier":
        return ouvrier(Path(argv[1]), os.environ, sys.stdin.buffer.read())
    try:
        if len(argv) == 2 and argv[0] == "rapport":
            config = charger_configuration(RACINE / CONFIGURATION, EMPREINTE_CONFIGURATION)
            rapport = faire_rapport(Path(argv[1]), config)
            print(texte_du_rapport(rapport))
            return 0
        if len(argv) in (2, 3) and argv[0] == "regle":
            config = charger_configuration(RACINE / CONFIGURATION, EMPREINTE_CONFIGURATION)
            rapports = {}
            for chemin in argv[1:]:
                rapport = faire_rapport(Path(chemin), config)
                rapports[rapport["file"]] = rapport
            print(json.dumps(appliquer_regle(config, rapports.get("claude"), rapports.get("carbon")),
                             ensure_ascii=False, indent=1, sort_keys=True))
            return 0
    except Arret as garde:
        print(f"ARRÊT : {garde}", file=sys.stderr)
        return 2
    print("usage : chef_essai_mesure_lecteurs_bras_a_v1.py claude | carbon | gpt | rapport DOSSIER | regle DOSSIER [DOSSIER]",
          file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(principal())
