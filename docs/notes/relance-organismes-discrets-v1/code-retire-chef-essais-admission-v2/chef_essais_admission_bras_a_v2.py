#!/usr/bin/env python3
"""Chef des deux essais d'admission du bras A des organismes discrets : Mistral Large 4, candidat au second lecteur,
et `gemini-4-neon`, juge des deux ancres — version 2.

Devis joué, qui fait foi : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md`
(`421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc`). Une ligne de calcul par invocation.
**Commandes, lancées depuis la racine du dépôt** (CONFIGURATION : chemin de la configuration scellée de la ligne ;
EMPREINTE : son empreinte sha256, que la commande redit pour qu'aucune autre configuration ne serve) :

    GO_ID=GO-… .venv/bin/python -I -B scripts/chef_essais_admission_bras_a_v2.py verification-mistral-eu CONFIGURATION EMPREINTE
    GO_ID=GO-… .venv/bin/python -I -B scripts/chef_essais_admission_bras_a_v2.py verification-mistral-global CONFIGURATION EMPREINTE
    GO_ID=GO-… .venv/bin/python -I -B scripts/chef_essais_admission_bras_a_v2.py verification-google CONFIGURATION EMPREINTE
    GO_ID=GO-… .venv/bin/python -I -B scripts/chef_essais_admission_bras_a_v2.py file-mistral CONFIGURATION EMPREINTE
    GO_ID=GO-… .venv/bin/python -I -B scripts/chef_essais_admission_bras_a_v2.py file-neon CONFIGURATION EMPREINTE

Sans appel, sans dépense, sans `GO_ID` :

    .venv/bin/python -I -B scripts/chef_essais_admission_bras_a_v2.py a-blanc LIGNE CONFIGURATION EMPREINTE
    .venv/bin/python -I -B scripts/chef_essais_admission_bras_a_v2.py rapport DOSSIER_DE_LA_FILE
    .venv/bin/python -I -B scripts/chef_essais_admission_bras_a_v2.py regles DOSSIER_DE_LA_FILE CONFIGURATION EMPREINTE

`a-blanc` joue toutes les gardes d'avant départ d'une ligne, hors la ligne de calcul (garde 8), sans rien lancer ni
rien écrire : elle éprouve les pièces de Lazar (constat, mot sur la sonde, lecture de la console, règles) avant que
la ligne de calcul existe. `rapport` imprime le rapport d'une file, toujours recalculé du journal ; il ne l'écrit et
ne le scelle que si aucun rapport n'a été rendu **et** que la file est close (son amorce a fini, ou n'est plus en
vie) : lancé pendant qu'une file tourne, il n'écrit rien.

Interpréteur : celui de l'environnement du dépôt (`.venv/bin/python`), consigné au manifeste. Une file peut durer
jusqu'à son délai global (40 heures au pire chez Mistral) : la lancer sous `nohup` ou dans un multiplexeur de
terminaux. Un signal de raccrochage reçu sans cela arrête la ligne proprement (relais arrêté, inventaire), et la file,
partie, ne se rejoue pas.

Ce que fait une ligne, dans l'ordre :
1. **Avant tout envoi** (un défaut : rien ne part, code 2) : configuration à son empreinte, non marquée « gabarit » ;
   identifiants figés et hôte de la ligne (garde 14) ; ligne de calcul lue au registre de la branche principale, qui
   nomme cette ligne et cite l'empreinte du devis (garde 8) ; pièces à leurs empreintes ; constat des conditions
   d'envoi **lu**, clé par clé (garde 9) ; lecture de la console exigée après tout envoi coupé d'une ligne antérieure
   du même fournisseur (garde 20) ; pour la vérification par le point d'accès global, relevé européen au signe
   constaté (garde 15) ; pour une file : relevé de vérification sain, sonde et majorant, crédit, mot de Lazar (garde
   10), fichier des règles (garde 12), file jamais partie (garde 13), entrées et ordre (garde 17) ; tous les corps
   construits et contrôlés (gardes 3 et 6).
2. Dossier créé, manifeste écrit, relais de la ligne lancé par `scripts/lancer_relais_local_v1.py` (clé exigée par
   son nom, jamais lue ni affichée ici : garde 7), état du relais contrôlé.
3. L'**ouvrier** (ce même fichier, relancé avec un environnement réduit à `PATH`, `HOME`, `LANG`, `GO_ID`) joue la
   ligne sur la boucle locale seulement, par `http.client` : aucune bibliothèque cliente, **aucune reprise cachée**.
4. Fin, arrêt par une garde, signal ou panne : relais arrêté par son identifiant de processus (R10), recherche de
   toute chaîne de la forme d'une clé, relevé ou rapport aux seuls champs techniques, contrôle « aucun morceau de
   réponse » (garde 18), inventaire scellé. Rien n'est jamais supprimé par ce programme.

Les vingt gardes du devis (section 10) sont nommées par leur numéro dans le code (`garde N`). Les critères d'admission
sont **recopiés** du devis, section 7, et non réinterprétés : `appliquer_regles`. Le fichier des règles en est la
copie à la lettre ; ce programme vérifie qu'il porte, caractère pour caractère, les lignes du texte en vigueur.

Lectures retenues, déclarées (elles sont redites dans la note du rédacteur) :
- les lignes 3 à 5 du classement de 4.4 (« code 200 ») visent une réponse **reçue entière** ; un flux de Mistral de
  code 200 qui finit sans son marqueur `[DONE]`, ou qu'un délai coupe, est une connexion coupée ou un délai (ligne 6).
  Un nom servi autre, vu avant la coupure, reste la ligne 4 ;
- à l'appel B (sonde), un code 429, un code de 500 à 599 ou une connexion coupée laissent la sonde « à refaire » par
  un lancement nouveau, sous la même ligne, si le compteur et le compte de trois appels le permettent ;
- une vérification dont l'appel sain n'a pas été suivi d'une sonde jouée ne laisse pas partir la file : aucune pièce
  du mot de Lazar ne couvre une sonde non jouée ;
- dans une file, un refus du mandataire à sa signature est une panne de transport comptée zéro (reprise unique) ;
- un refus écrit par le relais avant l'amont (origine `relais`, hors délai et coupure) arrête la ligne ; il est compté
  selon le régime du compteur, du côté prudent : le devis n'exempte que la signature du mandataire.

Ce programme ne lit jamais le texte d'une réponse pour un jugement : il en tire les compteurs, le motif de fin, le
nom servi, des longueurs, et la conformité de forme (oui ou non, un code de cause sans texte), jugée par le programme
de l'instrument que nomme la configuration. Bibliothèque standard seulement, hors ce programme de forme.
Essais : `tests/test_chef_essais_admission_bras_a_v2.py` (faux fournisseur local, aucun appel payant).
"""
from __future__ import annotations

import datetime
import decimal
import fcntl
import hashlib
import http.client
import importlib
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
import traceback
import urllib.parse
from pathlib import Path

VERSION = "chef_essais_admission_bras_a_v2"
RACINE = Path(__file__).resolve().parents[1]
EMPREINTE_DEVIS = "421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc"
# Garde 14 : constantes du texte, à la lettre.
IDENTIFIANTS = {"mistral": "mistral-large-4-0", "google": "gemini-4-neon"}
HOTES_PERMIS = ("api.eu.mistral.ai", "api.mistral.ai", "generativelanguage.googleapis.com")
LIGNES = {  # ligne : (genre, fournisseur, hôte de la ligne ; None : celui du relevé de vérification)
    "verification-mistral-eu": ("verification", "mistral", "api.eu.mistral.ai"),
    "verification-mistral-global": ("verification", "mistral", "api.mistral.ai"),
    "verification-google": ("verification", "google", "generativelanguage.googleapis.com"),
    "file-mistral": ("file", "mistral", None),
    "file-neon": ("file", "google", "generativelanguage.googleapis.com"),
}
# Devis, section 3 et garde 17 : les huit entrées de la file Neon, dans cet ordre.
ENTREES_NEON = ("A-b1-01", "A-b1-02", "A-b1-03", "A-b1-04", "A-b1-05", "A-b1-06", "C-b1-02", "C-b1-03")
# Devis, 4.4 : champs de réglage cherchés, en liste close.
CHAMPS_DE_REGLAGE = ("temperature", "max_tokens", "reasoning_effort", "stream", "maxOutputTokens", "max_output_tokens",
                     "thinkingLevel", "thinking_level", "thinkingConfig")
CHAMPS_NIVEAU_DE_REFLEXION = ("thinkingLevel", "thinking_level", "thinkingConfig")
# Devis, 4.5, constat 3.
CHAINES_MODELE_INCONNU = ("invalid model", "model not found", "unknown model", "does not exist")
# Devis, 5.5 : motifs de fin. Tout autre motif, absent compris, vaut refus.
MOTIFS = {"mistral": {"normale": ("stop",), "sortie_max": ("length", "model_length")},
          "google": {"normale": ("STOP",), "sortie_max": ("MAX_TOKENS", "CONTINUATION")}}
# Devis, section 7 : les critères, recopiés.
CRITERES = {"file-mistral": {"lectures": 24, "conformes_min": 22}, "file-neon": {"lectures": 8, "conformes_min": 8}}
ROLES = {"file-mistral": "second lecteur", "file-neon": "juge des deux ancres"}
MARGE_JETONS = 64                 # devis, 6.4 : jetons de contrôle comptés
CORPS_D_ERREUR_MAX = 500          # devis, 4.1 : corps d'erreur d'une vérification, borné
FENETRE_SOUS_CHAINE = 21          # garde 18 : aucune suite de plus de 20 caractères
LETTRES_MIN_FENETRE = 8           # garde 18 : une suite compte si elle porte au moins huit lettres ou chiffres
HOTES_LOCAUX = ("127.0.0.1", "localhost", "::1")
AGENT_UTILISATEUR = "client-http/1.0"
ENVIRONNEMENT_OUVRIER = ("PATH", "HOME", "LANG", "GO_ID")
FORMES_DE_CLE = (r"\bsk-ant-[A-Za-z0-9_\-]{16,}", r"\bsk-[A-Za-z0-9_\-]{24,}", r"AIza[0-9A-Za-z_\-]{30,}",
                 r"Bearer [A-Za-z0-9_\-]{20,}")
FORMES_INTERDITES = (
    ("courriel", r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}"),
    ("identifiant de session", r"session_[0-9A-Za-z]{8,}"),
    ("identifiant universel", r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"),
    ("chemin du poste", r"(/home/|/root/|/tmp/|/Users/|[A-Za-z]:\\\\)"),
    ("adresse de session", r"claude\.ai/"),
)
MOTIF_DATE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?Z")
MOTIF_NOMBRE = re.compile(r"\d+([.,]\d+)?")


class Arret(Exception):
    """Une garde coupe : motif écrit, rien de silencieux (R5)."""


class Interruption(Exception):
    """Signal d'arrêt ou délai global : la ligne s'arrête, ce qui est reçu est gardé."""


def _lever_interruption(numero, cadre):
    raise Interruption("délai global dépassé" if numero == signal.SIGALRM else f"signal {numero}")


# --- outils -------------------------------------------------------------------------------------------------------------

def maintenant() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def heure() -> str:
    return maintenant().strftime("%Y-%m-%dT%H:%M:%SZ")


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


def sceller(chemin: Path) -> str:
    """Empreinte compagnon (R6), à la forme de `controle_ia.scellement` : empreinte, deux espaces, nom du fichier."""
    empreinte = sha256_fichier(chemin)
    ecrire_neuf(Path(str(chemin) + ".sha256"), f"{empreinte}  {chemin.name}\n".encode("utf-8"))
    return empreinte


def json_octets(objet) -> bytes:
    return (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")


def lire_json(octets):
    try:
        return json.loads(octets.decode("utf-8") if isinstance(octets, bytes) else octets)
    except (ValueError, UnicodeDecodeError):
        return None


def _entier(x) -> bool:
    return isinstance(x, int) and not isinstance(x, bool) and x >= 0


class Journal:
    """Journal de la ligne, une ligne JSON par événement, vidée sur le disque à chaque écriture."""

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
    """Les lignes d'un journal. Une ligne illisible (écriture coupée) lève `Arret` : rien n'est deviné."""
    if not chemin.exists():
        return []
    try:
        return [json.loads(l) for l in chemin.read_text(encoding="utf-8").splitlines() if l.strip()]
    except ValueError:
        raise Arret(f"journal illisible ({chemin.parent.name}/{chemin.name}) : nœud de Lazar, lecture de la console due") from None


INCIDENTS_D_UN_ENVOI_COUPE = ("delai", "coupure", "borne_octets", "interruption")


def departs_sans_reponse(lignes: list) -> list:
    """C-1 : les « départ » du journal restés sans événement « envoi » (ouvrier tué, machine arrêtée, signal entre
    la réponse et son écriture). Chacun a pu atteindre le fournisseur : il vaut un envoi coupé."""
    ecrits = {l.get("envoi") for l in lignes if l.get("evenement") == "envoi"}
    return [l for l in lignes if l.get("evenement") == "depart" and l.get("envoi") not in ecrits]


def cout_si_sans_reponse(compteur, fournisseur: str, octets_corps: int, L: dict, sortie_max: int) -> float:
    """C-1 : ce que compte un départ resté sans réponse au journal. Sa durée n'est pas connue : régime prudent sur le
    délai total de la ligne (200 jetons par seconde), et au moins sa réserve. Écrit à l'événement « départ », pour
    que la reconstitution ne dépende que du journal."""
    return compteur.cout_sans_compteur("prudent", fournisseur, octets_corps, L["reserve_sortie_jetons"], sortie_max,
                                       L["delais"]["total_s"], 0)


# --- configuration et pièces --------------------------------------------------------------------------------------------

def charger_configuration(chemin: Path, empreinte_attendue: str) -> dict:
    """La configuration à son empreinte et à son compagnon ; un gabarit ne sert aucune ligne."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise Arret(f"configuration absente : {chemin}")
    empreinte = sha256_fichier(chemin)
    if empreinte != empreinte_attendue:
        raise Arret(f"configuration d'empreinte {empreinte[:12]}… au lieu de {str(empreinte_attendue)[:12]}… : rien ne part")
    compagnon = Path(str(chemin) + ".sha256")
    if not compagnon.is_file() or compagnon.read_text(encoding="utf-8").split()[0] != empreinte:
        raise Arret("la configuration n'a pas d'empreinte compagnon conforme : rien ne part")
    config = json.loads(chemin.read_text(encoding="utf-8"))
    if config.get("etat") == "gabarit":
        raise Arret("la configuration est un gabarit : elle ne sert aucune ligne")
    if config.get("etat") not in ("definitive", "essai"):
        raise Arret(f"état de la configuration inconnu ({config.get('etat')!r}) : « definitive » ou « essai » attendu")
    if config["devis"]["sha256"] != EMPREINTE_DEVIS:
        raise Arret("la configuration ne cite pas l'empreinte du devis accepté")
    return config


def verifier_piece(racine: Path, piece: dict, nom: str, compagnon: bool = False) -> str:
    """Pièce présente, d'empreinte égale à celle de la configuration (et à son compagnon, si demandé)."""
    if not isinstance(piece, dict) or not piece.get("chemin") or not piece.get("sha256"):
        raise Arret(f"{nom} : chemin et empreinte non inscrits à la configuration")
    chemin = racine / piece["chemin"]
    if not chemin.is_file():
        raise Arret(f"{nom} : fichier absent ({piece['chemin']})")
    empreinte = sha256_fichier(chemin)
    if empreinte != piece["sha256"]:
        raise Arret(f"{nom} : empreinte {empreinte[:12]}… au lieu de {piece['sha256'][:12]}… ({piece['chemin']})")
    if compagnon:
        c = Path(str(chemin) + ".sha256")
        if not c.is_file() or c.read_text(encoding="utf-8").split()[0] != empreinte:
            raise Arret(f"{nom} : sans empreinte compagnon conforme ({piece['chemin']})")
    return empreinte


def controler_identifiants(config: dict, ligne: str) -> str:
    """Garde 14 : identifiants égaux à la lettre aux constantes du texte ; hôte permis, et celui de la ligne."""
    if ligne not in LIGNES:
        raise Arret(f"ligne inconnue : {ligne!r}")
    genre, fournisseur, hote_de_la_ligne = LIGNES[ligne]
    for nom, attendu in IDENTIFIANTS.items():
        if config["fournisseurs"][nom]["modele"] != attendu:
            raise Arret(f"garde 14 : identifiant {config['fournisseurs'][nom]['modele']!r} au lieu de {attendu!r}")
    if tuple(config["hotes_permis"]) != HOTES_PERMIS:
        raise Arret("garde 14 : la liste des hôtes permis n'est pas celle du devis")
    hote = config["lignes"][ligne].get("hote")
    if hote not in HOTES_PERMIS:
        raise Arret(f"garde 14 : hôte amont non permis ({hote!r})")
    if hote_de_la_ligne is not None and hote != hote_de_la_ligne:
        raise Arret(f"garde 14 : hôte {hote!r} sous une ligne qui exige {hote_de_la_ligne!r}")
    if fournisseur == "mistral" and hote == "generativelanguage.googleapis.com":
        raise Arret("garde 14 : hôte de Google sous une ligne de Mistral")
    if ligne == "file-neon" and tuple(config["lignes"][ligne]["entrees"]) != ENTREES_NEON:
        raise Arret("garde 17 : la file Neon n'envoie que ses huit entrées, dans leur ordre")
    return hote


# --- textes envoyés -----------------------------------------------------------------------------------------------------

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
    """Garde 6 (lot relu par empreinte, consigne remplie comparée à son empreinte) : vérifie le devis, le texte en
    vigueur, le lot, les deux consignes et chaque consigne remplie ; rend {identifiant: entrée et texte envoyé}."""
    verifier_piece(racine, config["devis"], "devis")
    verifier_piece(racine, config["prereg_en_vigueur"], "texte en vigueur")
    verifier_piece(racine, config["entrees"], "lot des entrées")
    lot = json.loads((racine / config["entrees"]["chemin"]).read_text(encoding="utf-8"))
    prereg = (racine / config["prereg_en_vigueur"]["chemin"]).read_text(encoding="utf-8")
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
        textes[e["id"]] = {"id": e["id"], "instrument": e["instrument"], "longueur": e["longueur"], "texte": texte,
                           "champs": {k: e.get(k) for k in ("title", "proposal", "controls", "plan", "identifiants")}}
    if sorted(lot["ordre"]) != sorted(textes):
        raise Arret("l'ordre du lot ne couvre pas exactement ses entrées")
    return {"ordre": lot["ordre"], "textes": textes}


def entrees_de_la_file(ligne: str, config: dict, lot: dict) -> list:
    """Garde 17 : la file Neon n'envoie que ses huit identifiants, dans cet ordre ; la file Mistral, les 24 du lot,
    dans l'ordre du lot."""
    demande = config["lignes"][ligne]["entrees"]
    if ligne == "file-neon":
        if tuple(demande) != ENTREES_NEON:
            raise Arret("garde 17 : la file Neon n'envoie que ses huit entrées, dans leur ordre")
        ordre = list(ENTREES_NEON)
    elif demande == "toutes":
        ordre = list(lot["ordre"])
    else:
        raise Arret("garde 17 : la file Mistral envoie les 24 entrées du lot, et rien d'autre")
    inconnues = [i for i in ordre if i not in lot["textes"]]
    if inconnues:
        raise Arret(f"garde 17 : entrées absentes du lot : {inconnues}")
    if len(ordre) != CRITERES[ligne]["lectures"] or len(set(ordre)) != len(ordre):
        raise Arret(f"garde 17 : {len(ordre)} entrées au lieu de {CRITERES[ligne]['lectures']}")
    return ordre


# --- garde 8 : ligne de calcul ------------------------------------------------------------------------------------------

def lire_registre_git(racine: Path, config: dict) -> str:
    ref = f"{config['registre_go']['reference_git']}:{config['registre_go']['chemin']}"
    try:
        return subprocess.run(["git", "-C", str(racine), "show", ref], check=True, capture_output=True, text=True).stdout
    except (subprocess.CalledProcessError, OSError) as erreur:
        raise Arret(f"registre des GO de la branche principale illisible ({type(erreur).__name__})") from None


def verifier_ligne_de_calcul(config: dict, ligne: str, environnement, registre: str, aujourd_hui: str) -> str:
    """Garde 8 : `GO_ID` égal à l'identifiant inscrit pour cette ligne ; ligne unique au registre, de type calcul, au
    plafond de la ligne, non échue, non révoquée, qui **nomme cette ligne** (toutes les marques de son périmètre) et
    cite l'empreinte du devis accepté. Rend l'empreinte de la ligne."""
    L = config["lignes"][ligne]
    attendu = L.get("go")
    if not attendu or not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2,}", attendu):
        raise Arret(f"garde 8 : aucun identifiant de ligne de calcul inscrit à la configuration pour {ligne}")
    if environnement.get("GO_ID") != attendu:
        raise Arret(f"garde 8 : GO_ID absent ou différent de {attendu} : rien ne part")
    lignes = [l for l in registre.splitlines() if l.startswith(f"| {attendu} |")]
    if len(lignes) != 1:
        raise Arret(f"garde 8 : {len(lignes)} ligne(s) {attendu} au registre de la branche principale (une seule attendue)")
    colonnes = [c.strip() for c in lignes[0].strip().strip("|").split(" | ")]
    if len(colonnes) != 8:
        raise Arret(f"garde 8 : la ligne {attendu} n'a pas huit colonnes")
    identifiant, accorde, type_, perimetre, plafond, echeance, par, reference = colonnes
    if identifiant != attendu or type_ != "calcul":
        raise Arret(f"garde 8 : la ligne {attendu} n'est pas une ligne de calcul")
    if par != "Lazar":
        raise Arret(f"garde 8 : la ligne {attendu} n'est pas accordée par Lazar")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", accorde) or accorde > aujourd_hui:
        raise Arret(f"garde 8 : la ligne {attendu} porte une date d'accord illisible ou postérieure à ce jour ({accorde})")
    if plafond != L["plafond_registre"]:
        raise Arret(f"garde 8 : la ligne {attendu} porte le plafond « {plafond} » au lieu de « {L['plafond_registre']} »")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", echeance) or aujourd_hui > echeance:
        raise Arret(f"garde 8 : la ligne {attendu} est échue ({echeance}) ou sans échéance lisible")
    marques = L.get("marques_du_perimetre") or []
    if not marques or any(m not in perimetre for m in marques):
        raise Arret(f"garde 8 : la ligne {attendu} ne nomme pas {ligne} (marques du périmètre absentes)")
    if config["devis"]["sha256"] not in perimetre:
        raise Arret(f"garde 8 : la ligne {attendu} ne cite pas l'empreinte du devis accepté")
    verification = (config.get("verification_du_devis") or {}).get("sha256")
    if verification and verification not in perimetre and verification not in reference:
        # m-15 : le fichier du devis se dit encore « brouillon » ; son acceptation vit dans la ligne, qui cite donc
        # aussi la pièce de sa vérification (quand la configuration l'inscrit).
        raise Arret(f"garde 8 : la ligne {attendu} ne cite pas l'empreinte de la vérification du devis")
    if any(l.startswith("|") and "| révocation |" in l and attendu in l for l in registre.splitlines()):
        raise Arret(f"garde 8 : la ligne {attendu} est révoquée")
    return sha256_octets(lignes[0].encode("utf-8"))


# --- pièces écrites de Lazar : constat, mot sur la sonde, lecture de la console -----------------------------------------

def _nombre(texte: str):
    """Un nombre écrit en chiffres, virgule ou point ; toute autre chaîne rend None (« après usage » compris)."""
    t = texte.strip().replace(" ", "").replace(" ", "")
    return float(t.replace(",", ".")) if MOTIF_NOMBRE.fullmatch(t) else None


MOTIF_CONVERSION = re.compile(r"(\d+(?:[.,]\d+)?) ([A-Z]{3}) ; taux (\d+(?:[.,]\d+)?) USD par ([A-Z]{3}) ; "
                              r"source : (.+?) ; heure du taux \(UTC\) : (\S+)")


AGE_MAX_DU_TAUX = datetime.timedelta(hours=24)
MOTIF_DEVISE = re.compile(r"[A-Z]{3}")
CONSOLES = {"google": "Google", "mistral": "Mistral"}


def controler_conversion(champs: dict, libelle: str, valeur_usd: float, reference, nom: str, sens: str = "plancher",
                         marge=None, devise: str | None = None):
    """Une console peut afficher un montant dans une autre devise que le dollar (le solde prépayé de Google, en
    euros). La valeur que lit le programme reste **un nombre en USD** (devis, section 9) ; la pièce porte, hors de son
    tableau, la ligne « - LIBELLÉ : MONTANT DEVISE ; taux TAUX USD par DEVISE ; source : … ; heure du taux (UTC) :
    AAAA-MM-JJTHH:MMZ ».

    `devise` est la devise que le constat dit affichée par la console : « USD », la ligne de conversion ne doit pas
    figurer ; autre, elle est **exigée**, dans cette devise ; None (appel sans constat), elle est lue si elle figure.
    L'heure du taux est au plus 24 heures avant `reference`, jamais après. La **marge de change** de la configuration
    (`marge`, une fraction) joue du côté prudent : un crédit ou un solde (`plancher`) ne dépasse pas montant × taux ×
    (1 − marge), arrondi au centime **inférieur** ; une dépense vue (`plafond`) n'est pas sous montant × taux ×
    (1 + marge), arrondi au centime **supérieur**. Aucun arrondi favorable. Rend None, ou le détail de la conversion."""
    brut = champs.get(libelle)
    if devise == "USD":
        if brut is not None:
            raise Arret(f"{nom} : la console est dite en USD, et la pièce porte pourtant « {libelle} »")
        return None
    if brut is None:
        if devise is not None:
            raise Arret(f"{nom} : la console affiche des {devise} : la ligne « {libelle} » est exigée (montant, taux, "
                        "source, heure du taux)")
        return None
    trouve = MOTIF_CONVERSION.fullmatch(brut.strip())
    if not trouve:
        raise Arret(f"{nom} : la ligne « {libelle} » n'a pas la forme « MONTANT DEVISE ; taux TAUX USD par DEVISE ; "
                    "source : … ; heure du taux (UTC) : AAAA-MM-JJTHH:MMZ »")
    montant, devise_lue, taux, devise_du_taux, source, quand = trouve.groups()
    if devise_lue == "USD" or devise_lue != devise_du_taux:
        raise Arret(f"{nom} : « {libelle} » : devise du montant ({devise_lue}) et devise du taux ({devise_du_taux}) "
                    "doivent être la même, autre que USD")
    if devise is not None and devise_lue != devise:
        raise Arret(f"{nom} : « {libelle} » est en {devise_lue}, la console est dite en {devise}")
    reference = reference or maintenant()
    releve = _date(quand)
    if releve is None or releve > reference:
        raise Arret(f"{nom} : « {libelle} » : heure du taux absente, illisible ou postérieure à ce qu'elle sert")
    if reference - releve > AGE_MAX_DU_TAUX:
        raise Arret(f"{nom} : « {libelle} » : taux daté de plus de 24 heures ({quand}) : à relever de nouveau")
    if not source.strip():
        raise Arret(f"{nom} : « {libelle} » : source du taux absente")
    if not (isinstance(marge, (int, float)) and not isinstance(marge, bool) and 0 <= marge < 1):
        raise Arret(f"{nom} : conversion de devise sans marge de change inscrite à la configuration (`marge_de_change`)")
    le_taux = decimal.Decimal(taux.replace(",", "."))
    if le_taux <= 0:
        raise Arret(f"{nom} : « {libelle} » : taux nul")
    produit = decimal.Decimal(montant.replace(",", ".")) * le_taux
    la_marge = decimal.Decimal(repr(float(marge)))
    centime, valeur = decimal.Decimal("0.01"), decimal.Decimal(repr(float(valeur_usd)))
    if sens == "plancher":
        borne = (produit * (1 - la_marge)).quantize(centime, rounding=decimal.ROUND_FLOOR)
        if valeur > borne:
            raise Arret(f"{nom} : la valeur en USD ({valeur}) dépasse la conversion ({montant} {devise_lue} au taux {taux}, "
                        f"marge de change {marge}, soit {borne} USD au centime inférieur) : aucun arrondi favorable")
    else:
        borne = (produit * (1 + la_marge)).quantize(centime, rounding=decimal.ROUND_CEILING)
        if valeur < borne:
            raise Arret(f"{nom} : la valeur en USD ({valeur}) est sous la conversion ({montant} {devise_lue} au taux {taux}, "
                        f"marge de change {marge}, soit {borne} USD au centime supérieur) : aucun arrondi favorable")
    return {"libelle": libelle, "montant": montant, "devise": devise_lue, "taux_usd_par_unite": taux, "source": source.strip(),
            "heure_du_taux": quand, "marge_de_change": marge, "converti_usd": str(borne), "sens": sens}


def devises_des_consoles(champs: dict, nom: str) -> dict:
    """Constat : la ligne « - devise affichée par la console de Google : XXX » est obligatoire, et de même pour
    Mistral (hors du tableau : les treize clés du devis ne changent pas). Rend {fournisseur: devise}."""
    devises = {}
    for fournisseur, console in CONSOLES.items():
        valeur = (champs.get(f"devise affichée par la console de {console}") or "").strip()
        if not MOTIF_DEVISE.fullmatch(valeur):
            raise Arret(f"{nom} : la ligne « devise affichée par la console de {console} » est absente ou illisible "
                        "(trois lettres majuscules, par exemple USD ou EUR)")
        devises[fournisseur] = valeur
    return devises


def _date(texte: str):
    t = texte.strip()
    if not MOTIF_DATE.fullmatch(t):
        return None
    try:
        return datetime.datetime.strptime(t if len(t) == 20 else t[:-1] + ":00Z", "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=datetime.timezone.utc)
    except ValueError:
        return None


def champs_de_piece(texte: str) -> dict:
    """Lignes « - clé : valeur » d'une pièce (la première occurrence d'une clé compte ; un doublon est refusé)."""
    champs = {}
    for l in texte.splitlines():
        trouve = re.fullmatch(r"- ([^:]+?) : (.*)", l.strip())
        if trouve:
            cle = trouve.group(1).strip()
            if cle in champs:
                raise Arret(f"pièce : la ligne « {cle} » figure deux fois")
            champs[cle] = trouve.group(2).strip()
    return champs


def mot_de_lazar_present(texte: str) -> bool:
    """Le mot de Lazar, à la lettre : une section « ## Mot de Lazar » suivie d'au moins une ligne citée non vide."""
    dans, lignes = False, []
    for l in texte.splitlines():
        if l.startswith("## "):
            dans = l.strip().lower().startswith("## mot de lazar")
            continue
        if dans and l.startswith(">") and l[1:].strip():
            lignes.append(l)
    return bool(lignes)


def lire_constat(texte: str, regles_des_cles: dict, a_l_instant: datetime.datetime, marge=None) -> dict:
    """Garde 9 : le tableau du constat est **lu**. Les clés de la section 9 du devis, toutes et elles seules, chacune
    à une valeur admise ; chaque date en temps universel, antérieure à l'envoi ; le mot de Lazar présent. Rend
    {clé: valeur} (nombres pour les crédits et les limites) et l'heure de la transcription."""
    if not mot_de_lazar_present(texte):
        raise Arret("garde 9 : le constat ne porte pas le mot de Lazar")
    lues = {}
    for l in texte.splitlines():
        if not l.startswith("|"):
            continue
        cellules = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cellules) != 5 or not re.fullmatch(r"[a-z_]+", cellules[0]):
            continue
        cle, valeur, page, date, qui = cellules
        valeur = valeur.strip("`")
        if cle in lues:
            raise Arret(f"garde 9 : la clé {cle} figure deux fois au constat")
        if not page or not qui:
            raise Arret(f"garde 9 : la clé {cle} n'a ni page ni témoin")
        quand = _date(date)
        if quand is None:
            raise Arret(f"garde 9 : la clé {cle} n'a pas de date lisible en temps universel")
        if quand >= a_l_instant:
            raise Arret(f"garde 9 : la clé {cle} porte une date postérieure à l'envoi")
        lues[cle] = (valeur, quand)
    manquantes, de_trop = sorted(set(regles_des_cles) - set(lues)), sorted(set(lues) - set(regles_des_cles))
    if manquantes:
        raise Arret(f"garde 9 : clé(s) manquante(s) au constat : {manquantes}")
    if de_trop:
        raise Arret(f"garde 9 : clé(s) de trop au constat : {de_trop}")
    valeurs, conversions, hors_tableau = {}, [], champs_de_piece(texte)
    devises = devises_des_consoles(hors_tableau, "garde 9")
    for cle, regle in regles_des_cles.items():
        valeur = lues[cle][0]
        if regle["type"] == "valeurs":
            if valeur not in regle["admises"]:
                raise Arret(f"garde 9 : {cle} vaut « {valeur} », hors des valeurs admises")
            valeurs[cle] = valeur
        elif regle["type"] == "entier_egal":
            if not re.fullmatch(r"\d+", valeur) or int(valeur) != regle["valeur"]:
                raise Arret(f"garde 9 : {cle} vaut « {valeur} » au lieu de {regle['valeur']}")
            valeurs[cle] = int(valeur)
        elif regle["type"] == "nombre_min":
            n = _nombre(valeur)
            if n is None:
                raise Arret(f"garde 9 : {cle} n'est pas un nombre (« {valeur} »)")
            if n + 1e-9 < regle["min"]:
                raise Arret(f"garde 9 : {cle} vaut {n}, sous le seuil de {regle['min']}")
            valeurs[cle] = n
            if cle.endswith("_usd"):       # montant vu dans une autre devise : conversion refaite, sans arrondi favorable
                # le taux est daté de 24 heures au plus avant le premier envoi de la ligne
                conversion = controler_conversion(hors_tableau, f"conversion de {cle}", n, a_l_instant, f"garde 9 : {cle}",
                                                  marge=marge, devise=devises.get(cle.split("_")[0]))
                if conversion:
                    conversions.append(conversion)
        else:
            raise Arret(f"garde 9 : règle inconnue pour {cle}")
    transcription = _date(champs_de_piece(texte).get("heure de la transcription (UTC)", ""))
    if transcription is None or transcription >= a_l_instant:
        raise Arret("garde 9 : heure de la transcription absente, illisible ou postérieure à l'envoi")
    return {"valeurs": valeurs, "transcription": transcription, "conversions": conversions, "devises": devises,
            "derniere_date": max(q for _, q in lues.values())}


def garde_constat(config: dict, racine: Path, a_l_instant: datetime.datetime) -> dict:
    """Garde 9, entière : pièce présente, d'empreinte égale à celle de la configuration et à son compagnon, puis lue."""
    verifier_piece(racine, config.get("constat"), "garde 9 : constat des conditions d'envoi", compagnon=True)
    texte = (racine / config["constat"]["chemin"]).read_text(encoding="utf-8")
    return lire_constat(texte, config["constat_cles"], a_l_instant, config.get("marge_de_change"))


def _go_du_dossier(dossier: Path):
    manifeste = lire_json((dossier / "manifeste-depart.json").read_bytes()) if (dossier / "manifeste-depart.json").is_file() else None
    return manifeste.get("go") if isinstance(manifeste, dict) else None


def _appel_reconstitue(depart: dict, rang: int, lancement: int) -> dict:
    """C-1 : la fiche d'un appel de vérification dont seul le « départ » est au journal."""
    sonde = depart.get("type") == "B"
    return {"envoi": depart.get("envoi"), "type": depart.get("type"), "rang": rang, "lancement": lancement,
            "compte_parmi_les_trois": True, "reconstitue": True, "code": None, "incident": "coupure",
            "detail_de_l_incident": "départ sans réponse au journal : envoi tenu pour coupé (reconstitué)",
            "signature_du_mandataire": False, "coupe_par_un_delai": False, "connexion_coupee_en_route": True,
            "coupe_a_sa_borne_en_octets": False, "nom_servi": None, "noms_servis": None, "motif_de_fin": None,
            "champs_usage": None, "compteurs_lisibles": False, "sortie_facturee": None, "octets_contenu": None,
            "morceaux_par_type": None, "reflexion": None, "duree_s": None,
            "cout_usd": round(float(depart.get("cout_si_sans_reponse_usd") or 0.0), 6),
            "facon_de_compter": "départ sans réponse : régime prudent sur le délai total", "regime": "prudent",
            "temperature_envoyee": depart.get("temperature_envoyee"), "orthographe_niveau": depart.get("orthographe_niveau"),
            "ligne_du_classement": None if sonde else 6, "a_refaire": sonde, "sonde": None, "corps_d_erreur": None,
            "issue": "départ sans réponse au journal : tenu pour une connexion coupée"}


def lancements_de_verification(racine: Path, config: dict, ligne: str) -> dict:
    """C-1 : l'état de chaque ligne de calcul d'une ligne de vérification, lu dans **tous** ses dossiers. Pour chaque
    ligne de calcul : son dernier relevé (cumulé), puis, pour tout dossier postérieur **sans relevé**, ce que porte
    son journal — chaque « envoi » écrit, et chaque « départ » sans « envoi » tenu pour un envoi coupé, compté au
    régime prudent. Un dossier sans relevé, sans manifeste, mais avec un départ, arrête tout. Rend
    {go: {appels, listes, depense_comptee_usd, close, lancements, reconstitue, piece, quand}}."""
    base = racine / config["lignes"][ligne]["dossier"]
    etats = {}
    for dossier in sorted(p for p in base.glob(f"*-{ligne}") if p.is_dir()) if base.is_dir() else []:
        chemin = dossier / "releve-verification-v1.json"
        if chemin.is_file():
            o = lire_json(chemin.read_bytes())
            if not isinstance(o, dict) or not o.get("go"):
                raise Arret(f"pièce d'une ligne jouée illisible : {chemin.relative_to(racine)}")
            etats[o["go"]] = {"appels": list(o.get("appels") or []), "listes": list(o.get("listes") or []),
                              "depense_comptee_usd": float(o.get("depense_comptee_usd") or 0.0),
                              "close": bool(o.get("close")), "lancements": int(o.get("lancements") or 1),
                              "reconstitue": [], "piece": chemin, "quand": o.get("quand"),
                              "envois_coupes": list(o.get("envois_coupes") or [])}
            continue
        journal = lire_journal(dossier / "journal-essai.jsonl")
        if not journal:
            continue                      # rien n'a été joué dans ce dossier (relais non lancé, garde avant l'ouvrier)
        go = _go_du_dossier(dossier)
        if not go:
            if any(l.get("evenement") in ("depart", "envoi") for l in journal):
                raise Arret(f"dossier {dossier.relative_to(racine)} sans relevé ni manifeste, avec des envois au journal : "
                            "nœud de Lazar, lecture de la console due")
            continue
        etat = etats.setdefault(go, {"appels": [], "listes": [], "depense_comptee_usd": 0.0, "close": False,
                                     "lancements": 0, "reconstitue": [], "piece": None, "quand": None,
                                     "envois_coupes": []})
        etat["lancements"] += 1
        etat["listes"] += [{k: v for k, v in l.items() if k != "evenement"} for l in journal if l.get("evenement") == "liste"]
        orphelins = {l.get("envoi") for l in departs_sans_reponse(journal)}
        for l in journal:
            if l.get("evenement") == "envoi":
                fiche = {k: v for k, v in l.items() if k not in ("evenement", "quand")}
            elif l.get("evenement") == "depart" and l.get("envoi") in orphelins:
                fiche = _appel_reconstitue(l, len(etat["appels"]) + 1, etat["lancements"])
            else:
                continue
            etat["appels"].append(fiche)
            etat["depense_comptee_usd"] += float(fiche.get("cout_usd") or 0.0)
            if fiche.get("incident") in INCIDENTS_D_UN_ENVOI_COUPE:
                etat["envois_coupes"].append(fiche.get("envoi"))
        etat["reconstitue"].append(dossier.name)
        etat["piece"], etat["quand"] = dossier / "journal-essai.jsonl", journal[-1].get("quand")
        etat["close"] = False
    return etats


def lignes_jouees(racine: Path, config: dict, fournisseur: str) -> list:
    """Les lignes déjà jouées chez un fournisseur, pour les gardes 10 et 20. Vérifications : `lancements_de_verification`
    (relevé cumulé, complété des journaux des dossiers sans relevé : C-1). Files : le rapport ; sans rapport rendu,
    le rapport est reconstitué en mémoire depuis le journal. La pièce citée est alors le journal lui-même. Rend des
    dictionnaires {go, ligne, chemin, sha256, depense_comptee_usd, envois_coupes, quand, reconstitue}."""
    trouvees = []
    for ligne, (genre, f, _) in LIGNES.items():
        if f != fournisseur:
            continue
        if genre == "verification":
            for go, etat in lancements_de_verification(racine, config, ligne).items():
                if etat["piece"] is None:
                    continue
                trouvees.append({"go": go, "ligne": ligne, "chemin": str(etat["piece"].relative_to(racine)),
                                 "sha256": sha256_fichier(etat["piece"]),
                                 "depense_comptee_usd": float(etat["depense_comptee_usd"]),
                                 "envois_coupes": len(etat["envois_coupes"]), "quand": etat["quand"],
                                 "reconstitue": bool(etat["reconstitue"])})
            continue
        base = racine / config["lignes"][ligne]["dossier"]
        for dossier in sorted(p for p in base.glob(f"*-{ligne}") if p.is_dir()) if base.is_dir() else []:
            chemin = dossier / "rapport-technique.json"
            if chemin.is_file():
                o, reconstitue = lire_json(chemin.read_bytes()), False
                if not isinstance(o, dict) or not o.get("go"):
                    raise Arret(f"pièce d'une ligne jouée illisible : {chemin.relative_to(racine)}")
            else:
                journal = lire_journal(dossier / "journal-essai.jsonl")
                if not any(l.get("evenement") in ("depart", "envoi") for l in journal):
                    continue              # file jamais partie (C-2) : aucune dépense, aucun envoi coupé
                if not (dossier / "manifeste-depart.json").is_file():
                    raise Arret(f"dossier {dossier.relative_to(racine)} sans rapport ni manifeste, avec des envois au "
                                "journal : nœud de Lazar, lecture de la console due")
                try:
                    o, reconstitue, chemin = faire_rapport(dossier), True, dossier / "journal-essai.jsonl"
                except (KeyError, TypeError, ValueError):
                    raise Arret(f"dossier {dossier.relative_to(racine)} : rapport impossible à reconstituer du journal : "
                                "nœud de Lazar, lecture de la console due") from None
            trouvees.append({"go": o["go"], "ligne": ligne, "chemin": str(chemin.relative_to(racine)),
                             "sha256": sha256_fichier(chemin), "depense_comptee_usd": float(o.get("depense_comptee_usd") or 0.0),
                             "envois_coupes": len(o.get("envois_coupes") or []), "quand": o.get("quand"),
                             "reconstitue": reconstitue})
    return trouvees


def garde_console(config: dict, racine: Path, ligne: str, go: str, devises: dict | None = None) -> list:
    """Garde 20 : une ligne ne part pas si une ligne antérieure du même fournisseur porte un envoi coupé — par un
    délai, à sa borne en octets, ou par une connexion coupée en route, hors le refus du mandataire à sa signature —,
    sans la pièce scellée de la lecture de la console, d'empreinte inscrite à la configuration, qui cite ce relevé ou
    ce rapport et dont la dépense vue est au plus égale à la dépense comptée ; chez Google, la pièce porte le solde
    prépayé vu, au moins égal à ce que le devis (6.5) exige pour la ligne."""
    genre, fournisseur, _ = LIGNES[ligne]
    L, f = config["lignes"][ligne], config["fournisseurs"][fournisseur]
    pieces = []
    for p in L.get("lectures_console") or []:
        verifier_piece(racine, p, "garde 20 : lecture de la console", compagnon=True)
        texte = (racine / p["chemin"]).read_text(encoding="utf-8")
        pieces.append((champs_de_piece(texte), mot_de_lazar_present(texte), p))
    servies = []
    for jouee in lignes_jouees(racine, config, fournisseur):
        if jouee["go"] == go or not jouee["envois_coupes"]:
            continue
        citant = [x for x in pieces if x[0].get("empreinte du relevé ou du rapport") == jouee["sha256"]]
        if not citant:
            raise Arret(f"garde 20 : envoi coupé à la ligne {jouee['go']} ({jouee['chemin']}) sans lecture de la console "
                        "par Lazar : la ligne ne part pas" + (
                            " ; la pièce finale de cette ligne n'a pas été rendue : la lecture de la console cite "
                            "l'empreinte de ce journal" if jouee.get("reconstitue") else ""))
        champs, mot, piece = citant[0]
        if not mot:
            raise Arret("garde 20 : la lecture de la console ne porte pas le mot de Lazar")
        vue = _nombre(champs.get("dépense vue (USD)", ""))
        if vue is None or not champs.get("page") or _date(champs.get("heure (UTC)", "")) is None:
            raise Arret("garde 20 : la lecture de la console ne donne pas la dépense vue, sa page et son heure")
        devise, marge = (devises or {}).get(fournisseur), config.get("marge_de_change")
        quand = _date(champs.get("heure (UTC)", ""))      # le taux : 24 heures au plus avant l'heure de la lecture
        controler_conversion(champs, "conversion de la dépense vue", vue, quand, "garde 20 : dépense vue", sens="plafond",
                             marge=marge, devise=devise)
        if vue > jouee["depense_comptee_usd"] + 1e-9:
            raise Arret(f"garde 20 : dépense vue ({vue}) au-dessus de la dépense comptée ({jouee['depense_comptee_usd']:.4f}) : "
                        "nœud de Lazar, le devis est repris")
        if fournisseur == "google":
            seuil = f["credit_min_avant_file_usd"] if genre == "file" else f["credit_min_avant_verification_usd"]
            solde = _nombre(champs.get("solde prépayé vu (USD)", ""))
            if solde is None or solde + 1e-9 < seuil:
                raise Arret(f"garde 20 : solde prépayé vu absent ou sous {seuil} USD : la ligne ne part pas")
            controler_conversion(champs, "conversion du solde prépayé vu", solde, quand, "garde 20 : solde prépayé vu",
                                 marge=marge, devise=devise)
        servies.append({"cite": jouee["sha256"], "piece": piece["sha256"], "depense_vue_usd": vue})
    return servies


def alertes_de_cle(racine: Path, config: dict, fournisseur: str) -> list:
    """Garde 7 (m-c) : les dossiers des lignes de ce fournisseur où une clé a été vue — par le relais, valeur exacte,
    dans une réponse de l'amont (booléen de son journal), ou par la relecture de fin de ligne, par sa forme (journal
    de l'amorce). Rend leurs noms."""
    alertes = []
    for ligne, (_, f, _) in LIGNES.items():
        base = racine / config["lignes"][ligne]["dossier"]
        if f != fournisseur or not base.is_dir():
            continue
        for dossier in sorted(p for p in base.glob(f"*-{ligne}") if p.is_dir()):
            vue = cle_vue_par_le_relais(dossier / "relais" / "journal-relais.jsonl") > 0
            try:
                vue = vue or any(l.get("evenement") == "recherche_de_formes_de_cle" and l.get("fichiers")
                                 for l in lire_journal(dossier / "journal-amorce.jsonl"))
            except Arret:
                vue = True
            if vue and dossier.name not in alertes:
                alertes.append(dossier.name)
    return alertes


def garde_cle_vue(config: dict, racine: Path, ligne: str) -> list:
    """Garde 7 (m-c) : après une clé vue dans une réponse ou dans une pièce (code de sortie 7), aucune ligne de ce
    fournisseur ne part sans la pièce scellée de Lazar qui la lève, d'empreinte inscrite à la configuration
    (`levees_cle` de la ligne), sur le modèle de la lecture de la console : elle porte le mot de Lazar, la ligne
    « - dossier de l'alerte : NOM » et la ligne « - clé révoquée et remplacée : oui »."""
    _, fournisseur, _ = LIGNES[ligne]
    pieces = []
    for p in config["lignes"][ligne].get("levees_cle") or []:
        verifier_piece(racine, p, "garde 7 : levée d'une alerte de clé", compagnon=True)
        texte = (racine / p["chemin"]).read_text(encoding="utf-8")
        pieces.append((champs_de_piece(texte), mot_de_lazar_present(texte), p))
    levees = []
    for nom in alertes_de_cle(racine, config, fournisseur):
        citant = [x for x in pieces if x[0].get("dossier de l'alerte") == nom]
        if not citant:
            raise Arret(f"garde 7 : une clé a été vue au dossier {nom} (code de sortie 7) et aucune pièce de Lazar ne lève "
                        "cette alerte : la ligne ne part pas")
        champs, mot, piece = citant[0]
        if not mot or champs.get("clé révoquée et remplacée") != "oui":
            raise Arret("garde 7 : la pièce qui lève l'alerte ne porte pas le mot de Lazar et « clé révoquée et remplacée : oui »")
        levees.append({"dossier": nom, "piece": piece["sha256"]})
    return levees


def controler_verification_du_devis(config: dict, racine: Path) -> None:
    """Garde 8 (m-15) : dans une configuration définitive, la pièce de la vérification du devis est inscrite, présente
    à son empreinte et à son compagnon ; la valeur nulle n'est admise que d'une configuration d'essai."""
    piece = config.get("verification_du_devis")
    if config.get("etat") == "definitive" and not (isinstance(piece, dict) and piece.get("sha256")):
        raise Arret("garde 8 : une configuration définitive inscrit la pièce de la vérification du devis : rien ne part")
    if isinstance(piece, dict) and piece.get("sha256"):
        verifier_piece(racine, piece, "garde 8 : vérification du devis", compagnon=True)
    if config.get("etat") == "definitive" and not _marge_inscrite(config):
        raise Arret("garde 9 : une configuration définitive inscrit la marge de change (`marge_de_change`) : rien ne part")


def _marge_inscrite(config: dict) -> bool:
    marge = config.get("marge_de_change")
    return isinstance(marge, (int, float)) and not isinstance(marge, bool) and 0 <= marge < 1


def lire_releve(racine: Path, piece: dict, nom: str) -> dict:
    verifier_piece(racine, piece, nom, compagnon=True)
    o = lire_json((racine / piece["chemin"]).read_bytes())
    if not isinstance(o, dict):
        raise Arret(f"{nom} : illisible")
    return o


def garde_repli(config: dict, racine: Path) -> dict:
    """Garde 15 : la vérification par le point d'accès global exige le relevé scellé de la vérification européenne,
    **signe constaté**, d'empreinte inscrite."""
    piece = config["lignes"]["verification-mistral-global"].get("releve_europeen")
    releve = lire_releve(racine, piece, "garde 15 : relevé de la vérification européenne")
    if releve.get("ligne") != "verification-mistral-eu" or releve.get("hote") != "api.eu.mistral.ai":
        raise Arret("garde 15 : le relevé inscrit n'est pas celui de la vérification européenne")
    if releve.get("signe_constate") is not True:
        raise Arret("garde 15 : le signe de « ne sert pas ce modèle » n'est pas constaté au relevé européen : "
                    "la vérification globale ne part pas")
    return releve


def garde_cle_verifiee(config: dict, racine: Path, ligne: str, constat: dict) -> dict:
    """Garde 10 : la file exige le relevé scellé de sa vérification, sain, d'empreinte inscrite, sonde « comprise »
    et, chez Mistral, majorant par octets « établi » ; sinon le mot de Lazar, sous sa forme écrite, et la file part
    au régime prudent. Chez Google, dans tous les cas, le crédit du dernier constat moins la dépense comptée des
    lignes de Google jouées depuis ce constat est d'au moins 16,08 USD. Rend le contexte de la file."""
    _, fournisseur, _ = LIGNES[ligne]
    L, f = config["lignes"][ligne], config["fournisseurs"][fournisseur]
    releve = lire_releve(racine, L.get("releve_verification"), "garde 10 : relevé de la vérification de la clé")
    if releve.get("fournisseur") != fournisseur or releve.get("saine") is not True:
        raise Arret("garde 10 : le relevé de vérification n'est pas sain : la file ne part pas")
    if releve.get("noeud_de_lazar") and releve.get("issue_finale_ligne") in (4, 5, 8, 12, 13):
        raise Arret("garde 10 : le relevé de vérification porte une issue fermée : la file ne part pas")
    if releve.get("hote") != L["hote"]:
        raise Arret(f"garde 10 : le relevé est celui d'un autre point d'accès ({releve.get('hote')!r})")
    if releve.get("nom_servi") != IDENTIFIANTS[fournisseur]:
        raise Arret("garde 10 : le nom servi du relevé n'est pas l'identifiant figé")
    inscrit = L.get("inscrit") or {}
    attendu = {"nom_servi": releve.get("nom_servi"), "hote": releve.get("hote")}
    if fournisseur == "mistral":
        attendu["temperature_envoyee"] = releve.get("temperature_envoyee")
    else:
        attendu["orthographe_niveau"] = releve.get("orthographe_niveau")
    if inscrit != attendu:
        raise Arret("garde 10 : ce que la configuration inscrit (nom servi, point d'accès, orthographe, température) "
                    "n'est pas ce que porte le relevé")
    sonde = (releve.get("sonde") or {}).get("issue")
    majorant = releve.get("majorant")
    if sonde not in ("comprise", "non comprise", "indécidée"):
        raise Arret("garde 10 : la sonde de borne n'a pas été jouée : la file ne part pas")
    courant = sonde == "comprise" and (fournisseur == "google" or majorant == "établi")
    contexte = {"regime": "courant" if courant else "prudent", "sonde": sonde, "majorant": majorant,
                "nom_servi": releve["nom_servi"], "hote": releve["hote"],
                "temperature_envoyee": releve.get("temperature_envoyee"),
                "orthographe_niveau": releve.get("orthographe_niveau"), "mot_de_lazar": None,
                "releve": {"chemin": L["releve_verification"]["chemin"], "sha256": L["releve_verification"]["sha256"]}}
    if not courant:
        piece = L.get("mot_de_lazar_sonde")
        if not piece:
            raise Arret(f"garde 10 : sonde « {sonde} », majorant « {majorant} », sans pièce du mot de Lazar : "
                        "nœud de Lazar, la file ne part pas")
        verifier_piece(racine, piece, "garde 10 : pièce du mot de Lazar", compagnon=True)
        texte = (racine / piece["chemin"]).read_text(encoding="utf-8")
        champs = champs_de_piece(texte)
        if not mot_de_lazar_present(texte):
            raise Arret("garde 10 : la pièce ne porte pas le mot de Lazar")
        if champs.get("empreinte du relevé de vérification") != L["releve_verification"]["sha256"]:
            raise Arret("garde 10 : la pièce du mot de Lazar cite un autre relevé")
        if champs.get("issue de la sonde visée") != sonde:
            raise Arret("garde 10 : la pièce du mot de Lazar ne vise pas l'issue de la sonde du relevé")
        if fournisseur == "mistral" and champs.get("majorant visé") != str(majorant):
            raise Arret("garde 10 : la pièce du mot de Lazar ne vise pas le constat du majorant du relevé")
        if fournisseur == "google":
            vu = _nombre(champs.get("crédit prépayé vu après la vérification (USD)", ""))
            if vu is None or not champs.get("page") or _date(champs.get("heure (UTC)", "")) is None:
                raise Arret("garde 10 : la pièce du mot de Lazar ne porte pas le crédit prépayé vu, sa page et son heure")
            if vu + 1e-9 < f["credit_min_avant_file_usd"]:
                raise Arret(f"garde 10 : crédit prépayé vu de {vu} USD, sous {f['credit_min_avant_file_usd']} : "
                            "la file ne part pas")
            contexte["credit_vu_usd"] = vu
            contexte["conversion_du_credit_vu"] = controler_conversion(
                champs, "conversion du crédit prépayé vu", vu, _date(champs.get("heure (UTC)", "")),
                "garde 10 : crédit prépayé vu", marge=config.get("marge_de_change"),
                devise=(constat.get("devises") or {}).get("google"))
        contexte["mot_de_lazar"] = piece["sha256"]
    if fournisseur == "google":
        # Le solde vu ne dispense pas du contrôle par la dépense comptée : la console peut retarder sur la dépense.
        depuis = [j for j in lignes_jouees(racine, config, "google")
                  if _date(j["quand"] or "") is None or _date(j["quand"]) >= constat["transcription"]]
        comptee = sum(j["depense_comptee_usd"] for j in depuis)
        reste = constat["valeurs"][f["cle_credit"]] - comptee
        contexte["credit_du_constat_moins_depense_comptee_usd"] = round(reste, 6)
        if reste + 1e-9 < f["credit_min_avant_file_usd"]:
            raise Arret(f"garde 10 : crédit du constat moins dépense comptée = {reste:.2f} USD, sous "
                        f"{f['credit_min_avant_file_usd']} : la file ne part pas")
    return contexte


def texte_des_regles(texte_prereg: str, lignes: list) -> str:
    debut, fin = lignes
    return "\n".join(texte_prereg.split("\n")[debut - 1:fin])


def garde_regles(config: dict, racine: Path) -> str:
    """Garde 12 : le fichier des règles est présent, scellé, d'empreinte égale à celle de la configuration ; il cite
    l'empreinte du texte en vigueur ; il porte, caractère pour caractère, les huit règles de ce texte (3.4) ; il
    n'est pas un gabarit. Rend son empreinte."""
    empreinte = verifier_piece(racine, config.get("regles"), "garde 12 : fichier des règles", compagnon=True)
    texte = (racine / config["regles"]["chemin"]).read_text(encoding="utf-8")
    champs = champs_de_piece(texte)
    if champs.get("état", "").lower().startswith("gabarit"):
        raise Arret("garde 12 : le fichier des règles est un gabarit : la file ne part pas")
    if champs.get("empreinte du texte en vigueur") != config["prereg_en_vigueur"]["sha256"]:
        raise Arret("garde 12 : le fichier des règles cite un autre brouillon que le texte en vigueur : la file ne part pas")
    verifier_piece(racine, config["prereg_en_vigueur"], "texte en vigueur")
    prereg = (racine / config["prereg_en_vigueur"]["chemin"]).read_text(encoding="utf-8")
    if texte_des_regles(prereg, config["regles"]["lignes_du_texte"]) not in texte:
        raise Arret("garde 12 : le fichier des règles n'est pas la copie à la lettre des règles du texte en vigueur")
    if "**Règles d'admission, fermées" not in texte or "    8. **Les règles sont appliquées par programme" not in texte:
        raise Arret("garde 12 : les huit règles ne sont pas toutes au fichier des règles")
    return empreinte


def dossier_parti(dossier: Path) -> bool:
    """C-2 ; règle 4 du texte : « une file est partie dès son premier envoi ». Un dossier est parti si son journal
    porte un « départ » (écrit avant l'envoi), si le journal de son relais porte des octets envoyés à l'amont, ou si
    un rapport y est rendu. Un journal illisible vaut parti (du côté prudent)."""
    try:
        if any(l.get("evenement") == "depart" for l in lire_journal(dossier / "journal-essai.jsonl")):
            return True
        if any((l.get("octets_envoyes_amont") or 0) > 0 for l in lire_journal(dossier / "relais" / "journal-relais.jsonl")):
            return True
    except Arret:
        return True
    return (dossier / "rapport-technique.json").exists()


def dossiers_de_la_file(base: Path, ligne: str) -> tuple:
    """Garde 13 : (dossiers partis, dossiers sans aucun départ). Un dossier parti interdit un second départ de la
    même file ; un dossier sans départ est gardé tel quel et cité au manifeste du lancement suivant."""
    tous = sorted(p for p in base.glob(f"*-{ligne}") if p.is_dir()) if base.is_dir() else []
    partis = [str(p) for p in tous if dossier_parti(p)]
    return partis, [p.name for p in tous if str(p) not in partis]


# --- garde 6 : rien de personnel dans ce qui part -----------------------------------------------------------------------

def _sortie_git(racine: Path, *arguments) -> str:
    try:
        return subprocess.run(["git", "-C", str(racine), *arguments], capture_output=True, text=True, timeout=20).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def charger_interdits(config: dict, racine: Path, environnement) -> list:
    """Liste des termes interdits : fichier local exigé (jamais envoyé ni versé), plus ce que le poste dit de lui-même
    (auteur et courriel de git, dépôt distant, branche, dossier du dépôt, nom de machine, variables de session)."""
    garde = config["garde_interdits"]
    fichier = Path(garde["fichier_local"])
    if not fichier.is_file():
        raise Arret(f"garde 6 : liste locale des interdits absente ({fichier}) : rien ne part")
    termes = [l.strip() for l in fichier.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    if not termes:
        raise Arret("garde 6 : liste locale des interdits vide : rien ne part")
    derives = [_sortie_git(racine, "config", "user.name"), _sortie_git(racine, "config", "user.email"),
               _sortie_git(racine, "rev-parse", "--abbrev-ref", "HEAD"), racine.name, socket.gethostname()]
    distant = _sortie_git(racine, "config", "--get", "remote.origin.url")
    # m-7 : le schéma de l'adresse du dépôt distant n'est pas un terme (« http » est dans l'agent d'utilisateur).
    derives += [p for p in re.split(r"[/:@]", distant.removesuffix(".git"))
                if p and p.lower() not in ("http", "https", "ssh", "git", "file")]
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
    """Garde 6 : refuse l'envoi si le corps ou un en-tête porte un terme interdit ou une forme interdite."""
    texte = corps.decode("utf-8", errors="replace") + "\n" + "\n".join(f"{k}: {v}" for k, v in en_tetes.items())
    bas = texte.lower()
    for rang, t in enumerate(interdits):
        if t in bas:
            raise Arret(f"garde 6 : un terme de la liste des interdits est dans ce qui partirait (rang {rang})")
    for nom, forme in FORMES_INTERDITES:
        if re.search(forme, texte):
            raise Arret(f"garde 6 : forme interdite dans ce qui partirait ({nom})")
    if en_tetes.get("User-Agent") != AGENT_UTILISATEUR:
        raise Arret("garde 6 : agent d'utilisateur non générique")


# --- corps des appels (garde 3) -----------------------------------------------------------------------------------------

def construire_corps(fournisseur: str, f: dict, texte: str, sortie_max: int, temperature_envoyee: bool = True,
                     orthographe: str | None = None) -> dict:
    """Devis, 5.2 et 5.3 : les champs exacts, et rien d'autre."""
    if fournisseur == "mistral":
        corps = {"model": IDENTIFIANTS["mistral"], "messages": [{"role": "user", "content": texte}],
                 "max_tokens": sortie_max, "reasoning_effort": f["reasoning_effort"], "stream": True}
        if temperature_envoyee:
            corps["temperature"] = f["temperature"]
        return corps
    return {"contents": [{"role": "user", "parts": [{"text": texte}]}],
            "generationConfig": {"maxOutputTokens": sortie_max, "thinkingConfig": {"thinkingLevel": orthographe}}}


def chemin_de_l_appel(fournisseur: str) -> str:
    if fournisseur == "mistral":
        return "/v1/chat/completions"
    return f"/v1beta/models/{IDENTIFIANTS['google']}:generateContent"


def controler_corps(fournisseur: str, f: dict, corps: dict, chemin: str, sortie_max_attendue: int,
                    temperature_envoyee: bool = True, orthographe: str | None = None) -> None:
    """Garde 3 (et garde 14 pour l'identifiant) : le corps porte la sortie maximale de sa ligne et les seuls champs de
    5.2 ou 5.3 ; sinon refus avant l'envoi."""
    if not isinstance(corps, dict):
        raise Arret("garde 3 : corps qui n'est pas un objet")
    if chemin != chemin_de_l_appel(fournisseur):
        raise Arret(f"garde 14 : chemin d'appel {chemin!r} autre que celui de l'identifiant figé")
    if fournisseur == "mistral":
        attendues = {"model", "messages", "max_tokens", "reasoning_effort", "stream"} | (
            {"temperature"} if temperature_envoyee else set())
        if set(corps) != attendues:
            raise Arret(f"garde 3 : champs du corps {sorted(corps)} au lieu de {sorted(attendues)}")
        if corps["model"] != IDENTIFIANTS["mistral"]:
            raise Arret(f"garde 14 : identifiant {corps['model']!r} au lieu de {IDENTIFIANTS['mistral']!r}")
        if corps["stream"] is not True:
            raise Arret("garde 3 : `stream` doit valoir vrai (Mistral est lu en flux)")
        if corps["max_tokens"] != sortie_max_attendue or isinstance(corps["max_tokens"], bool):
            raise Arret(f"garde 3 : sortie maximale {corps['max_tokens']!r} au lieu de {sortie_max_attendue}")
        if corps["reasoning_effort"] != f["reasoning_effort"]:
            raise Arret("garde 3 : réglage de raisonnement autre que celui du devis")
        if temperature_envoyee and (corps["temperature"] != f["temperature"] or isinstance(corps["temperature"], bool)):
            raise Arret("garde 3 : température autre que celle du devis")
        messages = corps["messages"]
        if not (isinstance(messages, list) and len(messages) == 1 and isinstance(messages[0], dict)
                and set(messages[0]) == {"role", "content"} and messages[0]["role"] == "user"
                and isinstance(messages[0]["content"], str) and messages[0]["content"]):
            raise Arret("garde 3 : un seul message, de rôle « user », et rien d'autre")
        return
    if set(corps) != {"contents", "generationConfig"}:
        raise Arret(f"garde 3 : champs du corps {sorted(corps)} au lieu de contents et generationConfig")
    reglages = corps["generationConfig"]
    if not isinstance(reglages, dict) or set(reglages) != {"maxOutputTokens", "thinkingConfig"}:
        raise Arret("garde 3 : `generationConfig` ne porte que la sortie maximale et le niveau de réflexion")
    if reglages["maxOutputTokens"] != sortie_max_attendue or isinstance(reglages["maxOutputTokens"], bool):
        raise Arret(f"garde 3 : sortie maximale {reglages['maxOutputTokens']!r} au lieu de {sortie_max_attendue}")
    if orthographe not in f["orthographes_niveau"] or reglages["thinkingConfig"] != {"thinkingLevel": orthographe}:
        raise Arret("garde 3 : niveau de réflexion autre que l'orthographe retenue")
    contenus = corps["contents"]
    if not (isinstance(contenus, list) and len(contenus) == 1 and isinstance(contenus[0], dict)
            and set(contenus[0]) == {"role", "parts"} and contenus[0]["role"] == "user"
            and isinstance(contenus[0]["parts"], list) and len(contenus[0]["parts"]) == 1
            and isinstance(contenus[0]["parts"][0], dict) and set(contenus[0]["parts"][0]) == {"text"}
            and isinstance(contenus[0]["parts"][0]["text"], str) and contenus[0]["parts"][0]["text"]):
        raise Arret("garde 3 : un seul contenu, de rôle « user », une part de texte, et rien d'autre")


def en_tetes_de_l_envoi(identifiant_envoi: str) -> dict:
    return {"Content-Type": "application/json", "User-Agent": AGENT_UTILISATEUR, "X-Envoi": identifiant_envoi}


# --- compteur à réserve, deux régimes (garde 1 ; devis, 6.4) -------------------------------------------------------------

class Compteur:
    """Compteur d'une ligne. Avant l'envoi : refus si le cumul compté plus la réserve de l'envoi dépasse le plafond.
    Après : coût réel d'un envoi fini ; un envoi sans compteur lisible est compté selon le régime."""

    def __init__(self, plafond_usd: float, prix, debit_declare: float, cumul_usd: float = 0.0):
        self.plafond, self.prix, self.debit, self.cumul = float(plafond_usd), tuple(prix), float(debit_declare), float(cumul_usd)

    def cout(self, entree: float, sortie: float) -> float:
        return (entree * self.prix[0] + sortie * self.prix[1]) / 1e6

    def reserve(self, octets_corps: int, sortie_de_reserve: int) -> float:
        """Réserve d'un envoi : l'entrée à un jeton par octet du corps réel, plus la sortie de réserve."""
        return self.cout(octets_corps, sortie_de_reserve)

    def motif_de_refus(self, reserve: float):
        if self.cumul + reserve > self.plafond + 1e-9:
            return (f"garde 1 : plafond de la ligne ({self.plafond} USD) : cumul compté {self.cumul:.6f} + réserve "
                    f"{reserve:.6f}")
        return None

    def cout_sans_compteur(self, regime: str, fournisseur: str, octets_corps: int, sortie_de_reserve: int,
                           sortie_max: int, duree_s: float, octets_recus: int) -> float:
        """Régime prudent : 200 jetons de sortie par seconde de la durée, et au moins la réserve. Régime courant :
        chez Google, la sortie maximale envoyée ; chez Mistral, la plus grande de la sortie maximale et des octets
        de contenu reçus plus 64."""
        if regime == "prudent":
            return self.cout(octets_corps, max(sortie_de_reserve, self.debit * duree_s))
        if fournisseur == "google":
            return self.cout(octets_corps, sortie_max)
        return self.cout(octets_corps, max(sortie_max, octets_recus + MARGE_JETONS))

    def compter(self, cout: float) -> None:
        self.cumul += cout


def delai_global_file(appels: int, delai_total_s: float, attente_429_max_s: float, pause_s: float) -> float:
    """Devis, 5.6 : `appels × (2 × total + attente + pause) + attente`."""
    return appels * (2 * delai_total_s + attente_429_max_s + pause_s) + attente_429_max_s


def delai_global_verification(appels: int, delai_total_s: float, attente_429_max_s: float) -> float:
    """Devis, 5.6 : `3 × total + 600` par lancement."""
    return appels * delai_total_s + attente_429_max_s


# --- lecture technique des réponses (devis, 5.5) ------------------------------------------------------------------------

def octets_des_chaines(objet) -> int:
    """Somme des longueurs en octets UTF-8 de toutes les chaînes d'un contenu, hors les valeurs des champs `type`."""
    if isinstance(objet, str):
        return len(objet.encode("utf-8"))
    if isinstance(objet, list):
        return sum(octets_des_chaines(x) for x in objet)
    if isinstance(objet, dict):
        return sum(octets_des_chaines(v) for k, v in objet.items() if k != "type")
    return 0


def _chaines(objet, sortie: list) -> None:
    if isinstance(objet, str):
        sortie.append(objet)
    elif isinstance(objet, list):
        for x in objet:
            _chaines(x, sortie)
    elif isinstance(objet, dict):
        for k, v in objet.items():
            if k != "type":
                _chaines(v, sortie)


class LecteurFlux:
    """Lit le flux de Mistral au fil de l'eau. Il compte des longueurs et des types ; le texte jugé n'est gardé que
    pour le programme de forme et le contrôle « aucun morceau de réponse »."""

    def __init__(self):
        self.reste = b""
        self.evenements = 0
        self.illisibles = 0
        self.noms: list = []
        self.usage = None
        self.motif = None
        self.textes: list = []
        self.autres: list = []           # chaînes des morceaux écartés du texte jugé (pensée), pour la garde 18 seule
        self.octets_contenu = 0
        self.morceaux_par_type: dict = {}
        self.fini = False
        self.erreur_relais = None
        self._evenement_relais = False

    def nourrir(self, octets: bytes) -> None:
        self.reste += octets
        *lignes, self.reste = self.reste.split(b"\n")
        for ligne in lignes:
            self._ligne(ligne.strip())

    def clore(self) -> None:
        if self.reste.strip():
            self._ligne(self.reste.strip())
        self.reste = b""

    def _ligne(self, ligne: bytes) -> None:
        if ligne.startswith(b"event:"):
            self._evenement_relais = ligne[6:].strip() == b"relais"
            return
        if not ligne.startswith(b"data:"):
            return
        donnee = ligne[5:].strip()
        if self._evenement_relais:
            o = lire_json(donnee)
            self.erreur_relais = (o or {}).get("erreur", {}).get("motif", "inconnu") if isinstance(o, dict) else "inconnu"
            self._evenement_relais = False
            return
        if donnee == b"[DONE]":           # le marqueur de fin n'est pas un événement de données (devis, 4.3)
            self.fini = True
            return
        o = lire_json(donnee)
        if not isinstance(o, dict):
            self.illisibles += 1
            return
        self.evenements += 1
        if "model" in o and o["model"] not in self.noms:
            self.noms.append(o["model"])
        if isinstance(o.get("usage"), dict):
            self.usage = o["usage"]
        choix = o.get("choices")
        if not (isinstance(choix, list) and choix and isinstance(choix[0], dict)):
            return
        if choix[0].get("finish_reason") is not None:
            self.motif = choix[0]["finish_reason"]
        delta = choix[0].get("delta")
        contenu = delta.get("content") if isinstance(delta, dict) else None
        if isinstance(contenu, str):
            if contenu:
                self.morceaux_par_type["(chaîne)"] = self.morceaux_par_type.get("(chaîne)", 0) + 1
                self.octets_contenu += len(contenu.encode("utf-8"))
                self.textes.append(contenu)
        elif isinstance(contenu, list):
            for morceau in contenu:
                genre = morceau.get("type") if isinstance(morceau, dict) else None
                nom = genre if isinstance(genre, str) else "(sans type)"
                self.morceaux_par_type[nom] = self.morceaux_par_type.get(nom, 0) + 1
                self.octets_contenu += octets_des_chaines(morceau)
                if genre == "text" and isinstance(morceau.get("text"), str):
                    self.textes.append(morceau["text"])
                else:
                    _chaines(morceau, self.autres)


def lu_mistral(lecteur: LecteurFlux) -> dict:
    """Champs techniques d'un flux de Mistral (devis, 4.3 et 5.5)."""
    usage = lecteur.usage if isinstance(lecteur.usage, dict) else {}
    p, c, t = usage.get("prompt_tokens"), usage.get("completion_tokens"), usage.get("total_tokens")
    lisible = _entier(p) and _entier(c) and _entier(t)
    controle = t - p if lisible else None
    return {"evenements": lecteur.evenements, "noms_servis": list(lecteur.noms),
            "nom_servi": lecteur.noms[0] if len(lecteur.noms) == 1 and isinstance(lecteur.noms[0], str) else None,
            "nom_absent": not lecteur.noms, "nom_multiple": len(lecteur.noms) > 1,
            "compteurs_lisibles": bool(lisible), "champs_usage": sorted(usage),
            "entree": p if lisible else None, "sortie_lue": c if lisible else None, "sortie_controle": controle,
            "sortie_facturee": max(c, controle) if lisible else None, "reflexion": None, "reponse_seule": None,
            "reflexion_constatee": lecteur.morceaux_par_type.get("thinking", 0) > 0,
            "motif": lecteur.motif, "texte": "".join(lecteur.textes), "autres_textes": list(lecteur.autres),
            "octets_contenu": lecteur.octets_contenu, "morceaux_par_type": dict(lecteur.morceaux_par_type),
            "fini": lecteur.fini, "erreur_relais": lecteur.erreur_relais, "illisibles": lecteur.illisibles}


def lu_google(corps: bytes) -> dict:
    """Champs techniques d'une réponse de `generateContent` (devis, 4.3 et 5.5)."""
    o = lire_json(corps)
    o = o if isinstance(o, dict) else {}
    usage = o.get("usageMetadata") if isinstance(o.get("usageMetadata"), dict) else {}
    p, c, t = usage.get("promptTokenCount"), usage.get("candidatesTokenCount"), usage.get("totalTokenCount")
    pensees = usage.get("thoughtsTokenCount", 0)
    lisible = _entier(p) and _entier(c) and _entier(t) and _entier(pensees)
    candidats = o.get("candidates")
    candidat = candidats[0] if isinstance(candidats, list) and candidats and isinstance(candidats[0], dict) else None
    motif, texte = None, ""
    if candidat is not None:
        motif = candidat.get("finishReason")
        parts = (candidat.get("content") or {}).get("parts") if isinstance(candidat.get("content"), dict) else None
        for part in parts if isinstance(parts, list) else []:
            if isinstance(part, dict) and isinstance(part.get("text"), str) and part.get("thought") is not True:
                texte += part["text"]
    elif isinstance(o.get("promptFeedback"), dict):
        motif = o["promptFeedback"].get("blockReason")
    autres = []
    if candidat is not None:
        for part in ((candidat.get("content") or {}).get("parts") or []) if isinstance(candidat.get("content"), dict) else []:
            if isinstance(part, dict) and part.get("thought") is True and isinstance(part.get("text"), str):
                autres.append(part["text"])
    nom = o.get("modelVersion")
    controle = t - p if lisible else None
    return {"noms_servis": [nom] if "modelVersion" in o else [], "nom_servi": nom if isinstance(nom, str) else None,
            "nom_absent": "modelVersion" not in o, "nom_multiple": False,
            "compteurs_lisibles": bool(lisible), "champs_usage": sorted(usage),
            "entree": p if lisible else None, "sortie_lue": c + pensees if lisible else None, "sortie_controle": controle,
            "sortie_facturee": max(c + pensees, controle) if lisible else None,
            "reflexion": pensees if lisible else None, "reponse_seule": c if lisible else None,
            "reflexion_constatee": bool(lisible and pensees > 0), "motif": motif if isinstance(motif, str) else None,
            "texte": texte, "autres_textes": autres, "octets_contenu": None, "morceaux_par_type": None,
            "fini": bool(o), "erreur_relais": None, "illisibles": 0 if o else 1}


def classe_du_motif(fournisseur: str, motif) -> str:
    """Devis, 5.5 : « normale », « sortie_max », ou « refus » pour tout autre motif, absent compris."""
    for classe, valeurs in MOTIFS[fournisseur].items():
        if motif in valeurs:
            return classe
    return "refus"


# --- envoi (boucle locale, sans bibliothèque cliente, sans reprise) ------------------------------------------------------

def envoyer(url_relais: str, methode: str, chemin: str, en_tetes: dict, corps: bytes | None, flux: bool,
            delai_silence_s: float, delai_total_s: float, borne_octets: int | None = None) -> dict:
    """Un envoi, et un seul (garde 4 : aucune reprise cachée). Rend le code, les en-têtes, le corps reçu (même partiel),
    la durée, et `incident` : None, « delai », « coupure », « borne_octets » ou « interruption ». Les délais sont ceux
    de la garde 2 (devis, 5.6) : sans flux, le délai total ; en flux, le silence et le total. En flux, chaque silence est borné par
    `delai_silence_s`, l'ensemble par `delai_total_s`, et **le contenu par `borne_octets`** (garde 19) : dès que le
    compte des octets de contenu passe la borne, la connexion est fermée."""
    parties = urllib.parse.urlsplit(url_relais)
    if parties.scheme != "http" or parties.hostname not in HOTES_LOCAUX:
        raise Arret(f"garde 7 : le chef d'essai ne parle qu'à la boucle locale, reçu {url_relais!r}")
    debut = time.monotonic()
    connexion = http.client.HTTPConnection(parties.hostname, parties.port,
                                           timeout=min(delai_silence_s, delai_total_s) if flux else delai_total_s)
    sortie = {"code": None, "en_tetes": {}, "corps": b"", "incident": None, "detail": None, "flux": None}
    lecteur = LecteurFlux() if flux else None
    morceaux, reponse = [], None
    try:
        connexion.request(methode, chemin, body=corps, headers=en_tetes)
        reponse = connexion.getresponse()
        sortie["code"] = reponse.status
        sortie["en_tetes"] = {k.lower(): v for k, v in reponse.getheaders()}
        en_flux = flux and reponse.status == 200
        while True:
            reste = delai_total_s - (time.monotonic() - debut)
            if reste <= 0:
                sortie["incident"], sortie["detail"] = "delai", "délai total dépassé"
                break
            if connexion.sock is not None:
                connexion.sock.settimeout(min(delai_silence_s, reste) if en_flux else reste)
            morceau = reponse.read1(65536)
            if not morceau:
                break
            morceaux.append(morceau)
            if en_flux:
                lecteur.nourrir(morceau)
                if borne_octets is not None and lecteur.octets_contenu > borne_octets:
                    sortie["incident"], sortie["detail"] = "borne_octets", "borne en octets de l'envoi passée"
                    break
    except Interruption as signal_recu:
        sortie["incident"], sortie["detail"] = "interruption", str(signal_recu)
    except (socket.timeout, TimeoutError):
        ecoule = time.monotonic() - debut
        sortie["incident"] = "delai"
        sortie["detail"] = "délai total dépassé" if ecoule >= delai_total_s - 0.05 else "silence au-delà du délai"
    except (OSError, http.client.HTTPException) as erreur:
        sortie["incident"], sortie["detail"] = "coupure", type(erreur).__name__
    finally:
        try:
            if connexion.sock is not None:
                connexion.sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        # Fermeture explicite de la réponse : quand le relais annonce la fermeture, `http.client` lui passe la prise,
        # et fermer la connexion seule ne la fermerait pas (garde 19 : la coupure doit atteindre le relais, puis l'amont).
        try:
            if reponse is not None:
                reponse.close()
        except OSError:
            pass
        connexion.close()
    sortie["corps"] = b"".join(morceaux)
    sortie["duree_s"] = round(time.monotonic() - debut, 3)
    if lecteur is not None and sortie["code"] == 200:
        lecteur.clore()
        sortie["flux"] = lecteur
    return sortie


def origine_du_retour(retour: dict) -> tuple:
    """Un refus écrit par un relais porte la clé « erreur » et son origine (`relais` ou `mandataire`) ; une réponse du
    fournisseur est d'origine `amont`. Rend (origine, motif)."""
    if retour["code"] is None:
        return "relais", None
    o = lire_json(retour["corps"]) if retour.get("flux") is None else None
    if isinstance(o, dict) and isinstance(o.get("erreur"), dict):
        return o["erreur"].get("origine") or "relais", o["erreur"].get("motif")
    return "amont", None


def signature_du_mandataire(retour: dict, journal_relais, identifiant_envoi: str) -> bool:
    """Devis, 4.4, ligne 1 : le relais rend son code 502 avec l'origine `mandataire`, **et** son journal porte, pour
    cet envoi, zéro octet envoyé à l'amont. Le programme exige les deux."""
    origine, _ = origine_du_retour(retour)
    if retour["code"] != 502 or origine != "mandataire" or journal_relais is None:
        return False
    for l in lire_journal(Path(journal_relais)):
        if l.get("envoi") == identifiant_envoi:
            return l.get("origine") == "mandataire" and l.get("octets_envoyes_amont") == 0
    return False


def incident_de(fournisseur: str, retour: dict, lu: dict | None) -> str | None:
    """Ce qui a coupé l'envoi, s'il l'a été : « delai », « coupure », « borne_octets », « interruption » ou None.
    Un code d'erreur rendu par le service n'est pas un envoi coupé (devis, 6.4)."""
    if retour["incident"]:
        return retour["incident"]
    origine, motif = origine_du_retour(retour)
    if retour["code"] == 502 and origine == "relais" and motif in ("delai_silence", "delai_total"):
        return "delai"
    if retour["code"] == 502 and origine == "relais" and motif in ("coupure_amont", "connexion"):
        return "coupure"
    if retour["code"] == 502 and origine == "mandataire":
        # m-1 ; devis, 4.4, sous le tableau : sans la signature (journal du relais illisible, envoi non retrouvé),
        # une absence de réponse est une panne — ligne 6, comptée parmi les trois et au compteur.
        return "coupure"
    if fournisseur == "mistral" and retour["code"] == 200 and lu is not None:
        if lu["erreur_relais"] in ("delai_silence", "delai_total"):
            return "delai"
        if lu["erreur_relais"] is not None or not lu["fini"]:
            return "coupure"   # un flux sans son marqueur de fin est une connexion coupée en route
    return None


def detail_de_l_incident(retour: dict, lu: dict | None, incident: str | None) -> str | None:
    """m-6 : la cause, sans texte de réponse, pour que Lazar distingue une forme du service d'une panne."""
    if incident is None:
        return None
    if retour["incident"]:
        return retour["detail"]
    origine, motif = origine_du_retour(retour)
    if origine == "mandataire":
        return "refus du mandataire sans sa signature au journal du relais"
    if origine == "relais":
        return f"écrit par le relais : {motif}"
    if lu is not None and lu.get("erreur_relais") is not None:
        return f"flux interrompu par le relais : {lu['erreur_relais']}"
    if lu is not None and not lu.get("fini"):
        return "flux de code 200 fini sans son marqueur de fin"
    return None


def lire_le_retour(fournisseur: str, retour: dict) -> dict | None:
    if retour["code"] != 200:
        return None
    if fournisseur == "mistral":
        return lu_mistral(retour["flux"]) if retour.get("flux") is not None else None
    return lu_google(retour["corps"])


def compter_envoi(compteur: Compteur, regime: str, fournisseur: str, octets_corps: int, sortie_de_reserve: int,
                  sortie_max: int, retour: dict, lu: dict | None, incident: str | None, signature: bool) -> tuple:
    """Garde 1 : ce que compte un envoi. Rend (coût, façon de compter)."""
    if signature:
        return 0.0, "refus du mandataire à sa signature : compté zéro"
    if incident == "borne_octets":
        return compteur.reserve(octets_corps, sortie_de_reserve), "coupé à sa borne en octets : réserve entière"
    if retour["code"] == 200 and incident is None and lu is not None and lu["compteurs_lisibles"]:
        return compteur.cout(lu["entree"], lu["sortie_facturee"]), "coût réel"
    recus = (lu or {}).get("octets_contenu") or 0
    return (compteur.cout_sans_compteur(regime, fournisseur, octets_corps, sortie_de_reserve, sortie_max,
                                        retour["duree_s"], recus), f"sans compteur lisible : régime {regime}")


# --- vérification de la clé : formes, signe, classement, sonde, majorant (gardes 11 et 16) ------------------------------

def liste_lue(fournisseur: str, code, corps: bytes) -> dict:
    """Devis, 4.1 et 4.4 : de l'appel de liste, le programme ne garde que le code, la présence de l'identifiant et,
    pour Google, `outputTokenLimit`. Liste « lisible » de Mistral : un objet dont `data` est un tableau, ou un tableau
    nu ; chaque entrée est un objet qui a un champ `id`, une chaîne. Les champs `aliases` sont ignorés."""
    o = lire_json(corps) if code == 200 else None
    lisible, porte, limite = False, False, None
    if fournisseur == "mistral":
        entrees = o.get("data") if isinstance(o, dict) else o
        if isinstance(entrees, list) and all(isinstance(e, dict) and isinstance(e.get("id"), str) for e in entrees):
            lisible = True
            porte = any(e["id"] == IDENTIFIANTS["mistral"] for e in entrees)
    elif isinstance(o, dict) and isinstance(o.get("name"), str):
        lisible = True
        porte = o["name"] in (IDENTIFIANTS["google"], "models/" + IDENTIFIANTS["google"])
        limite = o["outputTokenLimit"] if _entier(o.get("outputTokenLimit")) else None
    return {"code": code, "lisible": lisible, "porte_identifiant": porte, "limite_sortie": limite,
            "admise_sans_identifiant": code == 200 and lisible and not porte}


def _elements_de_loc(corps) -> list:
    """Les éléments des `loc` des entrées de `detail`, en minuscules (égalité d'un élément, non sous-chaîne)."""
    sortie = []
    detail = corps.get("detail") if isinstance(corps, dict) else None
    for entree in detail if isinstance(detail, list) else []:
        loc = entree.get("loc") if isinstance(entree, dict) else None
        sortie.append([str(x).lower() for x in loc] if isinstance(loc, list) else [])
    return sortie


def _violations(objet, sortie: list) -> None:
    if isinstance(objet, dict):
        for k, v in objet.items():
            if k == "fieldViolations" and isinstance(v, list):
                sortie.extend(x["field"] for x in v if isinstance(x, dict) and isinstance(x.get("field"), str))
            else:
                _violations(v, sortie)
    elif isinstance(objet, list):
        for x in objet:
            _violations(x, sortie)


def champs_nommes(corps) -> set:
    """Devis, 4.4 : « nomme le champ X », sans égard à la casse — X est une sous-chaîne du champ `param` ; ou un
    élément d'un `loc` d'une entrée de `detail` est égal à X ; ou X est une sous-chaîne d'un champ `field` d'une
    entrée de `fieldViolations` ; ou X est une sous-chaîne du message d'erreur (`message` ou `error.message`)."""
    if not isinstance(corps, dict):
        return set()
    sous_chaines = []
    if isinstance(corps.get("param"), str):
        sous_chaines.append(corps["param"])
    if isinstance(corps.get("message"), str):
        sous_chaines.append(corps["message"])
    if isinstance(corps.get("error"), dict) and isinstance(corps["error"].get("message"), str):
        sous_chaines.append(corps["error"]["message"])
    _violations(corps, sous_chaines)
    bas = [s.lower() for s in sous_chaines]
    locs = [x for loc in _elements_de_loc(corps) for x in loc]
    return {c for c in CHAMPS_DE_REGLAGE if any(c.lower() in s for s in bas) or c.lower() in locs}


def signe_ne_sert_pas(liste: dict, code, corps) -> bool:
    """Signe de « ne sert pas ce modèle » (garde 11 ; devis, 4.5) : le point d'accès européen « ne sert pas ce modèle » si, et seulement si, (1) l'appel de
    liste rend le code 200 et une liste lisible où aucune entrée n'a l'identifiant ; (2) l'appel A rend le code 400,
    404 ou 422 ; (3) le corps d'erreur, lu comme du JSON, désigne le modèle, par l'une des formes fermées."""
    if not liste.get("admise_sans_identifiant") or code not in (400, 404, 422) or not isinstance(corps, dict):
        return False
    if corps.get("type") == "invalid_model":
        return True
    if "code" in corps and not isinstance(corps["code"], (dict, list)) and str(corps["code"]) == "1500":
        return True
    message = corps.get("message")
    if isinstance(message, str):
        bas = message.lower()
        if IDENTIFIANTS["mistral"] in bas and any(c in bas for c in CHAINES_MODELE_INCONNU):
            return True
    locs = _elements_de_loc(corps)
    reglages = {c.lower() for c in CHAMPS_DE_REGLAGE}
    return any("model" in loc for loc in locs) and not any(reglages & set(loc) for loc in locs)


def forme_de_verification(fournisseur: str, lu: dict) -> tuple:
    """Forme exigée de la réponse à la vérification (garde 16 ; devis, 4.3) : (nom servi égal à la lettre, forme
    entière). La liste des modèles n'y entre pas."""
    nom_egal = (not lu["nom_absent"] and not lu["nom_multiple"] and lu["nom_servi"] == IDENTIFIANTS[fournisseur])
    entiere = (nom_egal and lu["compteurs_lisibles"] and lu["motif"] == MOTIFS[fournisseur]["normale"][0]
               and bool(lu["texte"]))
    return nom_egal, entiere


def classer_issue(fournisseur: str, hote: str, appel: str, liste: dict, retour: dict, lu: dict | None,
                  incident: str | None, signature: bool) -> tuple:
    """Classement de la vérification (garde 16 ; devis, 4.4) : classement fermé des issues des appels A et A′, la première ligne qui s'applique.
    Rend (numéro de la ligne, issue). La ligne 2 se constate avant tout appel payant (`issue_de_la_liste`)."""
    code = retour["code"]
    origine, _ = origine_du_retour(retour)
    corps = lire_json(retour["corps"]) if code != 200 else None
    if signature:
        return 1, "refus du mandataire du réseau : rien n'en est conclu ; l'accès au réseau est une décision de Lazar"
    if incident == "borne_octets":
        return 13, "envoi coupé à sa borne en octets : non saine ; nœud de Lazar ; ni repli, ni appel de plus"
    if code == 200 and lu is not None and (lu["nom_multiple"] or (
            not lu["nom_absent"] and lu["nom_servi"] != IDENTIFIANTS[fournisseur])):
        return 4, "code 200 avec un autre nom servi : nœud de Lazar ; pas de repli"
    if incident in ("delai", "coupure", "interruption"):
        return 6, "délai dépassé ou connexion coupée : cause à attendre ou à corriger ; à refaire sous la même ligne, si le compteur le permet"
    if code == 200 and lu is not None:
        nom_egal, entiere = forme_de_verification(fournisseur, lu)
        if entiere:
            return 3, "saine ; point d'accès retenu, quelle que soit la liste"
        if not nom_egal:
            return 4, "code 200, nom servi absent : nœud de Lazar ; pas de repli"
        return 5, "code 200, nom servi égal, autre défaut de forme : non saine ; brouillon neuf du devis"
    if origine != "amont":
        return 13, "refus écrit par le relais : non saine ; nœud de Lazar ; ni repli, ni appel de plus"
    if code == 429 or (isinstance(code, int) and 500 <= code <= 599):
        return 6, f"code {code} : cause à attendre ou à corriger ; à refaire sous la même ligne, si le compteur le permet"
    if code in (401, 402, 403):
        if liste.get("admise_sans_identifiant"):
            return 8, f"code {code}, liste lisible sans l'identifiant : nœud de Lazar"
        return 7, f"code {code} : cause à corriger (clé refusée, compte non approvisionné) ; à refaire sous la même ligne"
    if fournisseur == "mistral" and hote == "api.eu.mistral.ai" and signe_ne_sert_pas(liste, code, corps):
        return 9, "signe de « ne sert pas ce modèle » constaté : repli sur le point d'accès global, sous sa ligne"
    nommes = champs_nommes(corps) if code in (400, 422) else set()
    if fournisseur == "mistral" and nommes == {"temperature"} and appel == "A":
        return 10, "la température est refusée : appel A′ sans elle"
    if (fournisseur == "google" and code == 400 and nommes and nommes <= set(CHAMPS_NIVEAU_DE_REFLEXION)
            and appel == "A"):
        return 11, "l'orthographe du niveau de réflexion est refusée : appel A′ avec la seconde"
    if nommes:
        return 12, "un champ de réglage est refusé : rien d'autre n'est essayé ; brouillon neuf du devis"
    return 13, f"toute autre issue (code {code}) : non saine ; nœud de Lazar ; ni repli, ni appel de plus"


def issue_de_la_sonde(fournisseur: str, f: dict, retour: dict, lu: dict | None, incident: str | None) -> dict:
    """Sonde de borne (garde 16 ; devis, 4.6) : son issue, la première ligne qui s'applique."""
    borne = f["sortie_max_sonde"]
    octets_max = borne * f.get("octets_par_jeton_de_la_borne", 8)
    recus = (lu or {}).get("octets_contenu")
    if fournisseur == "mistral" and incident == "borne_octets":
        return {"issue": "non comprise", "par_constat_d_octets": True, "constat": "envoi coupé à sa borne en octets"}
    if fournisseur == "mistral" and recus is not None and recus > octets_max:
        return {"issue": "non comprise", "par_constat_d_octets": True,
                "constat": f"plus de {octets_max} octets de contenu reçus"}
    lisible = retour["code"] == 200 and incident is None and lu is not None and lu["compteurs_lisibles"]
    if lisible and lu["sortie_facturee"] > borne:
        return {"issue": "non comprise", "par_constat_d_octets": False, "constat": "sortie facturée au-dessus de la borne"}
    nom_egal = lisible and not lu["nom_multiple"] and lu["nom_servi"] == IDENTIFIANTS[fournisseur]
    if (lisible and classe_du_motif(fournisseur, lu["motif"]) == "sortie_max" and lu["reflexion_constatee"]
            and not nom_egal):
        # C-3, lecture déclarée : une sonde mesurable mais sans nom servi ne dit pas « comprise » (rien ne dit que le
        # modèle demandé a répondu) ; elle reste « indécidée », nœud de Lazar, sans rendre la vérification non saine.
        return {"issue": "indécidée", "par_constat_d_octets": False, "constat": "mesure faite, nom servi absent"}
    if (lisible and classe_du_motif(fournisseur, lu["motif"]) == "sortie_max" and lu["reflexion_constatee"]):
        return {"issue": "comprise", "par_constat_d_octets": False,
                "constat": "au plus la borne facturée, fin par sortie maximale atteinte, réflexion constatée"}
    return {"issue": "indécidée", "par_constat_d_octets": False, "constat": "aucune des trois premières lignes"}


def constat_du_majorant(appels: list):
    """Constat du majorant par octets (garde 16 ; devis, 4.3) : « établi » si, à chaque appel de code 200 (A, A′ et B), la sortie facturée est au plus égale aux
    octets de contenu reçus plus 64 ; « démenti » si un seul appel la passe ; None si aucun appel ne s'y prête."""
    vus = [a for a in appels if a.get("code") == 200 and a.get("sortie_facturee") is not None
           and a.get("octets_contenu") is not None]
    if not vus:
        return None
    return "démenti" if any(a["sortie_facturee"] > a["octets_contenu"] + MARGE_JETONS for a in vus) else "établi"


# --- programme de forme de l'instrument (devis, section 8 ; texte, 3.2 et 3.3) -------------------------------------------

def charger_programme_de_forme(config: dict, racine: Path):
    """Le programme de conformité de forme et de vérification des extraits est celui de l'instrument, nommé par la
    configuration et vérifié par empreinte. Rend (module des réponses, réglages de l'instrument)."""
    p = config["programme_de_forme"]
    for piece in p["pieces"]:
        verifier_piece(racine, piece, "programme de forme de l'instrument")
    source = str(racine / p["racine_des_modules"])
    if source not in sys.path:
        sys.path.insert(0, source)
    module = importlib.import_module(p["module"])
    reglages = getattr(importlib.import_module(p["module_des_reglages"]), "Reglages")()
    return module, reglages


def juger_la_forme(programme, entree: dict, texte: str) -> dict:
    """Conformité de forme, oui ou non, avec un code de cause **sans texte** ; étayée, oui ou non (mesuré, sans
    verdict). Aucun morceau de la réponse ne sort d'ici."""
    module, reglages = programme
    if not isinstance(texte, str) or not texte.strip():
        return {"conforme": False, "cause": "vide", "etayee": False, "bloc_retire": False}
    champs = entree["champs"]
    try:
        if entree["instrument"] == "appariement":
            reponse = module.lire_forme_appariement(texte, reglages)
            bloc = bool(reponse.bloc_retire)
        else:
            traduite, _places, comptes = module.lire_forme_couverture(texte, champs["identifiants"], reglages)
            bloc = bool(comptes["bloc_retire"])
    except module.ErreurForme:
        return {"conforme": False, "cause": "forme", "etayee": False, "bloc_retire": False}
    except Exception as panne:  # noqa: BLE001 — C-5 : une panne du programme de forme (récursion comprise) n'arrête
        # pas la file : la lecture est « non conforme », avec un code de cause sans texte, rapporté et visible de Lazar.
        return {"conforme": False, "cause": f"panne_du_programme_de_forme:{type(panne).__name__}", "etayee": False,
                "bloc_retire": False}
    try:
        if entree["instrument"] == "appariement":
            cadre = importlib.import_module(module.ChampsAppariement.__module__).ChampsAppariement(
                champs["title"], champs["proposal"], champs["controls"])
            etayee = module.verdict_appariement(reponse, cadre).motif != "non etaye"
        else:
            etayee = all(module.verifier_extrait(l["extrait"], champs["plan"], module.LONGUEUR_MIN).verifie
                         for l in traduite.values() if l["statut"] != "absent")
    except Exception:  # noqa: BLE001 — une garde de l'instrument sur un extrait : non étayée, sans texte
        etayee = False
    return {"conforme": True, "cause": None, "etayee": bool(etayee), "bloc_retire": bloc}


# --- pièces gardées d'un envoi ------------------------------------------------------------------------------------------

def garder_le_corps(dossier: Path, identifiant: str, octets: bytes) -> None:
    ecrire_neuf(dossier / "envois" / f"{identifiant}.corps.json", octets)


def garder_la_reponse(dossier: Path, identifiant: str, retour: dict) -> None:
    """Chaque réponse est écrite, entière, telle que reçue du relais, avant d'être analysée."""
    base = dossier / "reponses-brutes-non-lues"
    ecrire_neuf(base / f"{identifiant}.corps", retour["corps"])
    ecrire_neuf(base / f"{identifiant}.meta.json", json_octets({
        "code": retour["code"], "en_tetes": retour["en_tetes"], "incident": retour["incident"],
        "detail": retour["detail"], "duree_s": retour["duree_s"]}))


def fiche_technique(identifiant: str, fournisseur: str, hote: str, retour: dict, lu: dict | None, incident,
                    signature: bool, cout: float, facon: str, regime: str, sortie_max: int) -> dict:
    """Les champs techniques d'un envoi (devis, 4.1 et section 8). Aucun texte de réponse."""
    origine, motif_relais = origine_du_retour(retour)
    lu = lu or {}
    fiche = {
        "envoi": identifiant, "modele_demande": IDENTIFIANTS[fournisseur], "hote": hote,
        "mode_de_lecture": "flux" if fournisseur == "mistral" else "sans flux",
        "code": retour["code"], "origine": origine, "motif_du_relais": motif_relais, "incident": incident,
        "detail_de_l_incident": detail_de_l_incident(retour, lu or None, incident),
        "signature_du_mandataire": signature,
        "coupe_par_un_delai": incident == "delai", "connexion_coupee_en_route": incident in ("coupure", "interruption"),
        "coupe_a_sa_borne_en_octets": incident == "borne_octets",
        "nom_servi": lu.get("nom_servi"), "noms_servis": lu.get("noms_servis"),
        "motif_de_fin": lu.get("motif"), "champs_usage": lu.get("champs_usage"),
        "compteurs_lisibles": bool(lu.get("compteurs_lisibles")),
        "entree": lu.get("entree"), "sortie_lue": lu.get("sortie_lue"), "sortie_controle": lu.get("sortie_controle"),
        "sortie_facturee": lu.get("sortie_facturee"), "reflexion": lu.get("reflexion"),
        "reponse_seule": lu.get("reponse_seule"), "reflexion_constatee": lu.get("reflexion_constatee"),
        "sortie_facturee_au_dela_de_la_sortie_maximale": (lu.get("sortie_facturee") or 0) > sortie_max,
        "longueur_du_texte_extrait": len(lu.get("texte") or ""),
        "octets_contenu": lu.get("octets_contenu"), "morceaux_par_type": lu.get("morceaux_par_type"),
        "duree_s": retour["duree_s"], "cout_usd": round(cout, 6), "facon_de_compter": facon, "regime": regime,
    }
    if fournisseur == "google":
        fiche["borne_en_octets"] = "aucune : un appel de Google ne porte aucune borne en octets (garde 19)"
    return fiche


def textes_des_reponses(dossier: Path, fournisseur: str) -> list:
    """Textes rendus par les modèles (texte jugé et pensée), relus par programme dans les réponses gardées de code
    200, pour le seul contrôle de sous-chaîne (garde 18)."""
    textes = []
    for meta in sorted((dossier / "reponses-brutes-non-lues").glob("*.meta.json")):
        if json.loads(meta.read_text(encoding="utf-8")).get("code") != 200:
            continue
        corps = Path(str(meta)[:-len(".meta.json")] + ".corps").read_bytes()
        if fournisseur == "mistral":
            lecteur = LecteurFlux()
            lecteur.nourrir(corps)
            lecteur.clore()
            lu = lu_mistral(lecteur)
        else:
            lu = lu_google(corps)
        textes.extend(t for t in [lu["texte"], *lu["autres_textes"]] if t)
    return textes


def controler_aucune_sous_chaine(ecrit: str, textes: list, fenetre: int = FENETRE_SOUS_CHAINE) -> int:
    """Garde 18 : nombre de suites de plus de 20 caractères d'une réponse retrouvées dans `ecrit` (zéro exigé).
    Le JSON écrit échappe guillemets et sauts de ligne : la suite est cherchée aussi sous sa forme échappée."""
    trouvees = 0
    for texte in textes:
        vues = set()
        for i in range(max(0, len(texte) - fenetre + 1)):
            morceau = texte[i:i + fenetre]
            # m-5 : une fenêtre faite de ponctuation, d'espaces et d'accolades (JSON indenté) n'est pas un morceau de
            # réponse : au moins huit lettres ou chiffres sont exigés.
            if sum(c.isalnum() for c in morceau) >= LETTRES_MIN_FENETRE and morceau not in vues:
                vues.add(morceau)
                if morceau in ecrit or json.dumps(morceau, ensure_ascii=False)[1:-1] in ecrit:
                    trouvees += 1
    return trouvees


def rendre_piece(dossier: Path, nom: str, objet: dict, fournisseur: str, texte_md: str | None = None) -> None:
    """Écrit un relevé ou un rapport, après la garde 18 ; sinon la pièce n'est pas rendue."""
    octets = json_octets(objet)
    ecrit = octets.decode("utf-8") + (texte_md or "")
    trouvees = controler_aucune_sous_chaine(ecrit, textes_des_reponses(dossier, fournisseur))
    if trouvees:
        raise Arret(f"garde 18 : la pièce contiendrait {trouvees} morceau(x) de réponse : elle n'est pas rendue")
    ecrire_neuf(dossier / nom, octets)
    sceller(dossier / nom)
    if texte_md is not None:
        ecrire_neuf(dossier / (nom[:-5] + ".md"), texte_md.encode("utf-8"))


def armer_le_delai_global(secondes: float):
    """Délai global (garde 2 ; devis, 5.6) : il n'arrête qu'un programme bloqué. Rend de quoi le désarmer."""
    try:
        ancien = signal.signal(signal.SIGALRM, _lever_interruption)
        signal.setitimer(signal.ITIMER_REAL, secondes)
    except ValueError:      # hors du fil principal : pas de minuterie (essais)
        return lambda: None

    def desarmer():
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, ancien)
    return desarmer


# --- vérification de la clé (devis, section 4) --------------------------------------------------------------------------

def etat_de_la_ligne(racine: Path, config: dict, ligne: str, go: str) -> dict:
    """Ce qui a déjà été joué sous cette ligne de calcul (tout ce qui se refait reste sous la même ligne, dans son
    compte de trois appels et sous son plafond) : son dernier relevé, cumulé, complété de ce que portent les journaux
    des dossiers restés sans relevé (C-1 : un relevé non rendu n'efface plus la mémoire de la ligne)."""
    etat = lancements_de_verification(racine, config, ligne).get(go)
    if etat is None:
        return {"appels": [], "listes": [], "depense_comptee_usd": 0.0, "close": False, "lancements": 0, "reconstitue": []}
    return {k: etat[k] for k in ("appels", "listes", "depense_comptee_usd", "close", "lancements", "reconstitue")}


def suite_de_la_verification(appels: list) -> tuple:
    """Devis, 4.2 : quel appel vient — « A », « Ap » (A′) ou « B » —, ou None et la raison de la clôture."""
    comptes = [a for a in appels if a["compte_parmi_les_trois"]]
    essais = [a for a in comptes if a["type"] in ("A", "Ap")]
    if any(a["ligne_du_classement"] == 3 for a in essais):
        sondes = [a for a in comptes if a["type"] == "B"]
        if not sondes or sondes[-1].get("a_refaire"):
            return "B", None
        return None, "sonde jouée"
    if not essais:
        return "A", None
    dernier = essais[-1]
    if dernier["ligne_du_classement"] in (10, 11):
        return "Ap", None
    if dernier["ligne_du_classement"] in (6, 7):
        return dernier["type"], None
    return None, f"issue fermée à la ligne {dernier['ligne_du_classement']} du classement"


def appel_de_liste(url_relais: str, fournisseur: str, journal_relais, identifiant: str) -> dict:
    """Devis, 4.1 : avant tout appel au modèle, un appel de liste, gratuit, qui n'envoie aucun texte."""
    chemin = "/v1/models" if fournisseur == "mistral" else f"/v1beta/models/{IDENTIFIANTS['google']}"
    retour = envoyer(url_relais, "GET", chemin, {"User-Agent": AGENT_UTILISATEUR, "X-Envoi": identifiant}, None, False,
                     60.0, 60.0)
    origine, _ = origine_du_retour(retour)
    liste = liste_lue(fournisseur, retour["code"] if origine == "amont" else None, retour["corps"])
    liste.update({"origine": origine, "incident": retour["incident"], "quand": heure(),
                  "signature_du_mandataire": signature_du_mandataire(retour, journal_relais, identifiant)})
    return liste


def jouer_verification(config: dict, ligne: str, dossier: Path, url_relais: str, journal_relais, interdits: list,
                       etat: dict, go: str, dormir=time.sleep) -> dict:
    """Joue un lancement de la vérification d'une clé : appel de liste, puis A, A′ et B selon 4.2 à 4.6, sans reprise.
    Rend le relevé (cumulé sur la ligne), écrit et scellé."""
    _, fournisseur, _ = LIGNES[ligne]
    f, L = config["fournisseurs"][fournisseur], config["lignes"][ligne]
    hote, flux = L["hote"], fournisseur == "mistral"
    if etat.get("close"):
        raise Arret(f"la ligne {go} est close : ce qui se refait demande une ligne nouvelle")
    journal = Journal(dossier / "journal-essai.jsonl")
    appels, listes = [dict(a) for a in etat["appels"]], list(etat["listes"])
    compteur = Compteur(L["plafond_usd"], f["prix"], config["debit_declare_jetons_par_s"], etat["depense_comptee_usd"])
    cloture, a_refaire, lancement = None, None, etat["lancements"] + 1
    desarmer = armer_le_delai_global(delai_global_verification(L["appels_max"], L["delais"]["total_s"],
                                                               config["attente_429"]["max_s"]))
    try:
        liste = appel_de_liste(url_relais, fournisseur, journal_relais, f"L{lancement}-liste")
        listes.append(liste)
        journal.ecrire(evenement="liste", **liste)
        if liste["signature_du_mandataire"]:
            a_refaire = "ligne 1 du classement, à l'appel de liste : refus du mandataire du réseau"
        elif liste["origine"] != "amont" or liste["incident"]:
            # C-4 : l'appel de liste, gratuit, est le seul essai de la voie avant tout appel payant. Sans réponse du
            # fournisseur (panne de transport, délai, refus écrit par le relais), aucun appel payant ne part.
            a_refaire = ("appel de liste sans réponse du fournisseur (panne de transport) : aucun appel payant, rien "
                         "n'est compté ; à refaire par un lancement nouveau, sous la même ligne")
        elif fournisseur == "google" and liste["limite_sortie"] is not None and liste["limite_sortie"] < f["sortie_max"]:
            cloture = (2, "`outputTokenLimit` sous la sortie maximale envoyée : aucun appel payant ; brouillon neuf du devis")
        while cloture is None and a_refaire is None:
            genre, raison = suite_de_la_verification(appels)
            if genre is None:
                cloture = (None, raison)
                break
            if sum(1 for a in appels if a["compte_parmi_les_trois"]) >= L["appels_max"]:
                cloture = (None, f"{L['appels_max']} appels consommés : ce qui reste demande une ligne nouvelle")
                break
            temperature = genre != "Ap" if fournisseur == "mistral" else True
            orthographe = None
            if genre == "B":
                sain = [a for a in appels if a["type"] in ("A", "Ap") and a["ligne_du_classement"] == 3][-1]
                temperature = sain["temperature_envoyee"]
                orthographe = sain["orthographe_niveau"]
            elif fournisseur == "google":
                orthographe = f["orthographes_niveau"][0 if genre == "A" else 1]
            sortie_max = f["sortie_max_sonde"] if genre == "B" else f["sortie_max"]
            message = config["messages"]["sonde" if genre == "B" else "appel_a"]
            chemin = chemin_de_l_appel(fournisseur)
            corps = construire_corps(fournisseur, f, message, sortie_max, temperature, orthographe)
            controler_corps(fournisseur, f, corps, chemin, sortie_max, temperature, orthographe)
            octets = json.dumps(corps, ensure_ascii=False).encode("utf-8")
            identifiant = f"L{lancement}-{len(appels) + 1:02d}-{genre}"
            en_tetes = en_tetes_de_l_envoi(identifiant)
            controler_envoi(octets, en_tetes, interdits)
            reserve = compteur.reserve(len(octets), L["reserve_sortie_jetons"])
            refus = compteur.motif_de_refus(reserve)
            if refus:
                cloture = (None, refus + " : la ligne s'arrête ; ce qui se refait demande une ligne nouvelle")
                journal.ecrire(evenement="refus_du_compteur", motif=refus)
                break
            journal.ecrire(evenement="depart", envoi=identifiant, type=genre, octets_corps=len(octets),
                           reserve_usd=round(reserve, 6), cumul_usd=round(compteur.cumul, 6),
                           temperature_envoyee=temperature, orthographe_niveau=orthographe,
                           cout_si_sans_reponse_usd=round(cout_si_sans_reponse(compteur, fournisseur, len(octets), L,
                                                                              sortie_max), 6))
            garder_le_corps(dossier, identifiant, octets)
            retour = envoyer(url_relais, "POST", chemin, en_tetes, octets, flux, L["delais"]["silence_s"],
                             L["delais"]["total_s"], L.get("borne_octets"))
            garder_la_reponse(dossier, identifiant, retour)
            lu = lire_le_retour(fournisseur, retour)
            signature = signature_du_mandataire(retour, journal_relais, identifiant)
            incident = None if signature else incident_de(fournisseur, retour, lu)
            cout, facon = compter_envoi(compteur, "prudent", fournisseur, len(octets), L["reserve_sortie_jetons"],
                                        sortie_max, retour, lu, incident, signature)
            compteur.compter(cout)
            fiche = fiche_technique(identifiant, fournisseur, hote, retour, lu, incident, signature, cout, facon,
                                    "prudent", sortie_max)
            fiche.update({"type": genre, "rang": len(appels) + 1, "lancement": lancement,
                          "compte_parmi_les_trois": not signature, "temperature_envoyee": temperature,
                          "orthographe_niveau": orthographe, "sortie_maximale_envoyee": sortie_max,
                          "ligne_du_classement": None, "issue": None, "a_refaire": False, "sonde": None,
                          "corps_d_erreur": None})
            if retour["code"] not in (None, 200):   # devis, 4.1 : pour une réponse d'erreur, et pour elle seule
                fiche["corps_d_erreur"] = retour["corps"].decode("utf-8", errors="replace")[:CORPS_D_ERREUR_MAX]
            origine, _ = origine_du_retour(retour)
            if genre in ("A", "Ap"):
                numero, issue = classer_issue(fournisseur, hote, genre, liste, retour, lu, incident, signature)
                fiche["ligne_du_classement"], fiche["issue"] = numero, issue
                if numero in (1, 6, 7):
                    a_refaire = issue
                elif numero not in (3, 10, 11):
                    cloture = (numero, issue)
            else:
                # C-3 : « autre nom servi » seulement sur une réponse reçue entière, dont un nom est présent et
                # différent (ou multiple). Un nom absent ou une forme illisible laisse l'issue à la sonde (« indécidée »).
                nom_autre = (incident is None and lu is not None and (lu["nom_multiple"] or (
                    not lu["nom_absent"] and lu["nom_servi"] != IDENTIFIANTS[fournisseur])))
                fiche["sonde"] = issue_de_la_sonde(fournisseur, f, retour, lu, incident)
                refaisable = signature or incident in ("coupure", "interruption") or (
                    origine == "amont" and (retour["code"] == 429 or (isinstance(retour["code"], int)
                                                                      and 500 <= retour["code"] <= 599)))
                if nom_autre:
                    fiche["ligne_du_classement"] = 4
                    fiche["issue"] = "sonde : code 200 avec un autre nom servi : nœud de Lazar"
                    cloture = (4, fiche["issue"])
                elif refaisable and fiche["sonde"]["issue"] == "indécidée":
                    fiche["a_refaire"] = True
                    a_refaire = "sonde à refaire par un lancement nouveau, sous la même ligne"
                else:
                    cloture = (None, "sonde jouée")
            appels.append(fiche)
            journal.ecrire(evenement="envoi", **fiche)
            if cloture is None and a_refaire is None:
                dormir(config["pause_s"])
    except Interruption as coupure:
        a_refaire = f"lancement interrompu ({coupure})"
        journal.ecrire(evenement="interruption", motif=str(coupure))
    finally:
        desarmer()
    essais = [a for a in appels if a["type"] in ("A", "Ap") and a["compte_parmi_les_trois"]]
    sains = [a for a in essais if a["ligne_du_classement"] == 3]
    nom_autre_a_la_sonde = any(a["type"] == "B" and a["ligne_du_classement"] == 4 for a in appels)
    saine = bool(sains) and not nom_autre_a_la_sonde
    sondes = [a for a in appels if a["type"] == "B" and a["compte_parmi_les_trois"] and not a["a_refaire"]]
    sonde = sondes[-1]["sonde"] if sondes else {"issue": None, "par_constat_d_octets": False, "constat": "sonde non jouée"}
    majorant = constat_du_majorant(appels) if fournisseur == "mistral" else None
    ligne_finale = cloture[0] if cloture and cloture[0] else (essais[-1]["ligne_du_classement"] if essais else None)
    releve = {
        "version": VERSION, "piece": "releve-verification-v1", "ligne": ligne, "go": go, "fournisseur": fournisseur,
        "hote": hote, "point_d_acces": f"https://{hote}", "mode_de_lecture": "flux" if flux else "sans flux",
        "modele_demande": IDENTIFIANTS[fournisseur], "quand": heure(), "lancements": lancement,
        "texte_en_vigueur": config["prereg_en_vigueur"], "devis": config["devis"],
        "listes": listes, "appels": appels, "appels_comptes": sum(1 for a in appels if a["compte_parmi_les_trois"]),
        "saine": saine, "nom_servi": sains[-1]["nom_servi"] if saine else None,
        "temperature_envoyee": sains[-1]["temperature_envoyee"] if saine and fournisseur == "mistral" else None,
        "orthographe_niveau": sains[-1]["orthographe_niveau"] if saine and fournisseur == "google" else None,
        "sonde": sonde, "majorant": majorant, "signe_constate": any(a["ligne_du_classement"] == 9 for a in essais),
        "issue_finale_ligne": ligne_finale,
        "issue_finale": (cloture[1] if cloture else a_refaire),
        "a_refaire": a_refaire, "close": cloture is not None,
        "noeud_de_lazar": bool(ligne_finale in (4, 8, 13) or (saine and sonde["issue"] != "comprise" and cloture is not None)
                               or majorant == "démenti"),
        "regime_du_compteur": "prudent", "plafond_usd": L["plafond_usd"],
        "depense_comptee_usd": round(compteur.cumul, 6),
        "envois_coupes": [a["envoi"] for a in appels if a["incident"] in INCIDENTS_D_UN_ENVOI_COUPE],
        "lecture_de_la_console_due": any(a["incident"] in INCIDENTS_D_UN_ENVOI_COUPE for a in appels),
        "champs_du_bloc_d_usage": sorted({c for a in appels for c in (a["champs_usage"] or [])}),
    }
    releve["dossiers_sans_releve_reconstitues"] = list(etat.get("reconstitue") or [])
    releve["cle_vue_dans_une_reponse"] = cle_vue_par_le_relais(journal_relais) if journal_relais else 0   # m-c
    try:
        rendre_piece(dossier, "releve-verification-v1.json", releve, fournisseur)
    except Arret as garde_18:
        # C-1 : la garde 18 refuse le relevé ; un relevé **réduit** est écrit et scellé quand même, aux seules valeurs
        # que fixe le programme (aucune chaîne venue du service) : le compte de la ligne ne se perd pas. La ligne est
        # close : nœud de Lazar.
        gardes = ("envoi", "type", "rang", "lancement", "compte_parmi_les_trois", "ligne_du_classement", "a_refaire",
                  "incident", "cout_usd", "code", "temperature_envoyee", "coupe_par_un_delai",
                  "connexion_coupee_en_route", "coupe_a_sa_borne_en_octets", "signature_du_mandataire", "regime")
        reduit = {k: releve[k] for k in ("version", "piece", "ligne", "go", "fournisseur", "hote", "quand", "lancements",
                                         "appels_comptes", "plafond_usd", "depense_comptee_usd", "envois_coupes",
                                         "lecture_de_la_console_due", "regime_du_compteur")}
        reduit.update({"reduit": True, "motif_de_la_reduction": "garde 18 : le relevé entier contiendrait un morceau de réponse",
                       "appels": [{k: (a.get(k) if not isinstance(a.get(k), str) or k in ("envoi", "type", "incident", "regime")
                                       else None) for k in gardes} for a in appels],
                       "listes": [], "saine": False, "nom_servi": None, "temperature_envoyee": None,
                       "orthographe_niveau": None, "sonde": {"issue": None, "par_constat_d_octets": False,
                                                              "constat": "relevé réduit"},
                       "majorant": None, "signe_constate": False, "issue_finale_ligne": None, "a_refaire": None,
                       "issue_finale": "relevé réduit après un refus de la garde 18 : nœud de Lazar", "close": True,
                       "noeud_de_lazar": True, "champs_du_bloc_d_usage": []})
        ecrire_neuf(dossier / "releve-verification-v1.json", json_octets(reduit))
        sceller(dossier / "releve-verification-v1.json")
        journal.ecrire(evenement="releve_reduit", motif=str(garde_18))
        journal.ecrire(evenement="fin", close=True, saine=False, a_refaire=None)
        return reduit
    journal.ecrire(evenement="fin", close=releve["close"], saine=saine, a_refaire=a_refaire)
    return releve


def code_de_sortie_verification(releve: dict) -> int:
    """8 : relevé réduit (garde 18) ; 0 : saine, sonde « comprise » et, chez Mistral, majorant « établi » ; 3 : à refaire par un lancement nouveau ;
    1 : toute autre issue (nœud de Lazar, non saine, signe constaté, ligne close)."""
    if releve.get("reduit"):
        return 8
    if releve["a_refaire"] and not releve["close"]:
        return 3
    if (releve["saine"] and releve["sonde"]["issue"] == "comprise"
            and (releve["fournisseur"] == "google" or releve["majorant"] == "établi")):
        return 0
    return 1


# --- les deux files (devis, section 5) ----------------------------------------------------------------------------------

def attente_sur_429(en_tetes: dict, regle: dict) -> float:
    """Devis, 5.6 : ce que dit `Retry-After`, borné à 600 secondes (30 sans en-tête lisible)."""
    brut = (en_tetes.get("retry-after") or "").strip()
    return float(min(int(brut), regle["max_s"])) if re.fullmatch(r"\d+", brut) else float(regle["defaut_s"])


def decider_dans_la_file(fournisseur: str, retour: dict, lu: dict | None, incident, signature: bool, rang: int,
                         nom_releve: str) -> tuple:
    """Gardes 2, 3, 4, 5 et 19 : après un envoi d'une file. Rend (décision, cause) : « ok », « reprise », « attente »
    (code 429 : attendre, puis reprise) ou « arret »."""
    code = retour["code"]
    origine, _ = origine_du_retour(retour)
    if signature:
        return ("reprise" if rang == 1 else "arret"), "refus du mandataire à sa signature (panne de transport)"
    if incident == "borne_octets":
        return "arret", "envoi coupé à sa borne en octets : file arrêtée par sa borne de dépense, sans reprise"
    if incident in ("delai", "coupure"):
        cause = "délai dépassé" if incident == "delai" else "connexion coupée"
        return ("reprise", cause) if rang == 1 else ("arret", f"seconde panne sur le même appel ({cause})")
    if incident == "interruption":
        return "arret", "interruption de notre côté"
    if code == 200:
        if lu is None or lu["nom_absent"] or lu["nom_multiple"] or lu["nom_servi"] != nom_releve:
            return "arret", "garde 5 : nom servi autre que celui du relevé de vérification"
        if not lu["compteurs_lisibles"]:
            return "arret", "réponse de code 200 sans compteur lisible"
        classe = classe_du_motif(fournisseur, lu["motif"])
        if classe == "sortie_max":
            return "arret", "garde 3 : fin par sortie maximale atteinte"
        if classe == "refus":
            return "arret", "garde 4 : motif de fin de refus (tout motif autre que la fin normale)"
        return "ok", None
    if origine != "amont":
        return "arret", f"refus écrit par le relais (code {code})"
    if code == 429:
        return ("attente", "code 429") if rang == 1 else ("arret", "second envoi d'un appel sur un code 429")
    if isinstance(code, int) and 500 <= code <= 599:
        return ("reprise", f"code {code}") if rang == 1 else ("arret", f"seconde panne sur le même appel (code {code})")
    if code in (401, 402, 403):
        return "arret", f"garde 4 : code {code}, arrêt sans reprise"
    return "arret", f"garde 4 : code {code}, arrêt"


def jouer_file(config: dict, ligne: str, lot: dict, dossier: Path, url_relais: str, journal_relais, interdits: list,
               contexte: dict, programme_de_forme, dormir=time.sleep) -> dict:
    """Joue une file en série : deux envois au plus par appel (l'envoi, et une reprise sur une panne de transport),
    aucune redemande de forme. Rend le bilan ; tout est au journal."""
    _, fournisseur, _ = LIGNES[ligne]
    f, L = config["fournisseurs"][fournisseur], config["lignes"][ligne]
    hote, flux, chemin = contexte["hote"], fournisseur == "mistral", chemin_de_l_appel(fournisseur)
    journal = Journal(dossier / "journal-essai.jsonl")
    compteur = Compteur(L["plafond_usd"], f["prix"], config["debit_declare_jetons_par_s"])
    regime, ordre = contexte["regime"], entrees_de_la_file(ligne, config, lot)
    bilan = {"complet": False, "arret": None, "arretee_a_son_plafond": False, "arretee_par_sa_borne_de_depense": False,
             "interrompue": False, "appels_finis": 0, "regime_final": regime, "majorant_dementi_en_file": False}
    desarmer = armer_le_delai_global(delai_global_file(len(ordre), L["delais"]["total_s"], config["attente_429"]["max_s"],
                                                       config["pause_s"]))
    journal.ecrire(evenement="depart_de_la_file", ligne=ligne, regime=regime, entrees=ordre)
    try:
        for numero, ident in enumerate(ordre, start=1):
            entree = lot["textes"][ident]
            corps = construire_corps(fournisseur, f, entree["texte"], f["sortie_max"],
                                     bool(contexte.get("temperature_envoyee")), contexte.get("orthographe_niveau"))
            controler_corps(fournisseur, f, corps, chemin, f["sortie_max"], bool(contexte.get("temperature_envoyee")),
                            contexte.get("orthographe_niveau"))
            octets = json.dumps(corps, ensure_ascii=False).encode("utf-8")
            for rang in (1, 2):      # un troisième envoi d'un même appel est impossible
                identifiant = f"{numero:02d}-{ident}-{rang}"
                en_tetes = en_tetes_de_l_envoi(identifiant)
                controler_envoi(octets, en_tetes, interdits)
                reserve = compteur.reserve(len(octets), L["reserve_sortie_jetons"])
                refus = compteur.motif_de_refus(reserve)
                if refus:
                    bilan["arret"], bilan["arretee_a_son_plafond"] = refus + " : file arrêtée à son plafond", True
                    journal.ecrire(evenement="refus_du_compteur", envoi=identifiant, motif=refus)
                    raise StopIteration
                journal.ecrire(evenement="depart", envoi=identifiant, entree=ident, rang=rang, octets_corps=len(octets),
                               reserve_usd=round(reserve, 6), cumul_usd=round(compteur.cumul, 6), regime=regime,
                               appel=numero, instrument=entree["instrument"], longueur=entree["longueur"],
                               cout_si_sans_reponse_usd=round(cout_si_sans_reponse(compteur, fournisseur, len(octets), L,
                                                                                  f["sortie_max"]), 6))
                garder_le_corps(dossier, identifiant, octets)
                retour = envoyer(url_relais, "POST", chemin, en_tetes, octets, flux, L["delais"]["silence_s"],
                                 L["delais"]["total_s"], L.get("borne_octets"))
                garder_la_reponse(dossier, identifiant, retour)
                lu = lire_le_retour(fournisseur, retour)
                signature = signature_du_mandataire(retour, journal_relais, identifiant)
                incident = None if signature else incident_de(fournisseur, retour, lu)
                cout, facon = compter_envoi(compteur, regime, fournisseur, len(octets), L["reserve_sortie_jetons"],
                                            f["sortie_max"], retour, lu, incident, signature)
                compteur.compter(cout)
                decision, cause = decider_dans_la_file(fournisseur, retour, lu, incident, signature, rang,
                                                       contexte["nom_servi"])
                fiche = fiche_technique(identifiant, fournisseur, hote, retour, lu, incident, signature, cout, facon,
                                        regime, f["sortie_max"])
                fiche.update({"entree": ident, "instrument": entree["instrument"], "longueur": entree["longueur"],
                              "appel": numero, "rang": rang, "decision": decision, "cause": cause,
                              "jetons_d_entree": fiche.pop("entree"),
                              "classe_du_motif": classe_du_motif(fournisseur, (lu or {}).get("motif")) if lu else None,
                              "conforme": None, "cause_de_forme": None, "etayee": None, "bloc_de_code_retire": None,
                              "majorant_dementi": False, "cumul_usd": round(compteur.cumul, 6)})
                if (fournisseur == "mistral" and lu is not None and lu["compteurs_lisibles"]
                        and lu["sortie_facturee"] > lu["octets_contenu"] + MARGE_JETONS):
                    # Devis, section 7 : le majorant est démenti en pleine file ; régime prudent pour la suite.
                    fiche["majorant_dementi"] = True
                    regime = bilan["regime_final"] = "prudent"
                    bilan["majorant_dementi_en_file"] = True
                # C-5 : l'envoi, payé, est écrit au journal **avant** le jugement de forme ; la forme suit, dans un
                # second événement. Une panne du programme de forme ne peut plus ôter un envoi du rapport.
                journal.ecrire(evenement="envoi", **fiche)
                if decision == "ok":
                    forme = juger_la_forme(programme_de_forme, entree, lu["texte"])
                    journal.ecrire(evenement="forme", envoi=identifiant, conforme=forme["conforme"],
                                   cause_de_forme=forme["cause"], etayee=forme["etayee"],
                                   bloc_de_code_retire=forme["bloc_retire"])
                if decision == "arret":
                    bilan["arret"] = cause
                    bilan["arretee_par_sa_borne_de_depense"] = incident == "borne_octets"
                    bilan["interrompue"] = incident == "interruption"
                    raise StopIteration
                if decision == "attente":
                    attente = attente_sur_429(retour["en_tetes"], config["attente_429"])
                    journal.ecrire(evenement="attente_sur_429", envoi=identifiant, secondes=attente)
                    dormir(attente)
                else:
                    dormir(config["pause_s"])
                if decision == "ok":
                    bilan["appels_finis"] += 1
                    break
        bilan["complet"] = bilan["appels_finis"] == len(ordre)
    except StopIteration:
        pass
    except Interruption as coupure:
        bilan["arret"], bilan["interrompue"] = f"file interrompue de notre côté ({coupure})", True
    finally:
        desarmer()
    bilan["depense_comptee_usd"] = round(compteur.cumul, 6)
    journal.ecrire(evenement="fin", **bilan)
    return bilan


# --- rapport aux seuls champs techniques (devis, section 8) --------------------------------------------------------------

def _moyenne(valeurs):
    valeurs = [v for v in valeurs if v is not None]
    return sum(valeurs) / len(valeurs) if valeurs else None


def faire_rapport(dossier: Path) -> dict:
    """Rapport technique d'une file, tiré du manifeste et du journal. Aucun texte de réponse."""
    manifeste = json.loads((dossier / "manifeste-depart.json").read_text(encoding="utf-8"))
    lignes = lire_journal(dossier / "journal-essai.jsonl")
    formes = {l["envoi"]: l for l in lignes if l.get("evenement") == "forme"}
    orphelins = {l.get("envoi"): l for l in departs_sans_reponse(lignes)}
    envois = []
    for l in lignes:
        if l.get("evenement") == "envoi":
            e = {k: v for k, v in l.items() if k != "evenement"}
            if e["envoi"] in formes:       # C-5 : la forme est jugée après l'écriture de l'envoi
                e.update({k: formes[e["envoi"]][k] for k in ("conforme", "cause_de_forme", "etayee", "bloc_de_code_retire")})
            elif e.get("decision") == "ok":
                e["cause_de_forme"] = "forme_non_jugee"      # panne entre l'envoi et son jugement : non conforme
            envois.append(e)
        elif l.get("evenement") == "depart" and l.get("envoi") in orphelins:
            # C-1 : un départ sans réponse au journal vaut un envoi coupé, compté au régime prudent.
            envois.append({"quand": l.get("quand"), "envoi": l.get("envoi"), "entree": l.get("entree"),
                           "appel": l.get("appel"), "rang": l.get("rang"), "instrument": l.get("instrument"),
                           "longueur": l.get("longueur"), "reconstitue": True, "code": None, "origine": None,
                           "incident": "coupure",
                           "detail_de_l_incident": "départ sans réponse au journal : envoi tenu pour coupé (reconstitué)",
                           "connexion_coupee_en_route": True, "coupe_par_un_delai": False,
                           "coupe_a_sa_borne_en_octets": False, "decision": "arret",
                           "cause": "départ sans réponse au journal (programme ou machine arrêtés)",
                           "classe_du_motif": None, "conforme": None, "cause_de_forme": None, "etayee": None,
                           "bloc_de_code_retire": None, "nom_servi": None, "noms_servis": None,
                           "sortie_facturee": None, "sortie_facturee_au_dela_de_la_sortie_maximale": False,
                           "duree_s": None, "regime": "prudent",
                           "cout_usd": round(float(l.get("cout_si_sans_reponse_usd") or 0.0), 6),
                           "facon_de_compter": "départ sans réponse : régime prudent sur le délai total"})
    fin = next((l for l in reversed(lignes) if l.get("evenement") == "fin"), None)
    ligne = manifeste["ligne"]
    derniers = {}
    for e in envois:
        derniers[e["appel"]] = e
    lectures = list(derniers.values())
    finies = [e for e in lectures if e["decision"] == "ok"]
    couts = {}
    for e in envois:   # une lecture reprise compte par ses deux envois pour le coût
        couts[e["appel"]] = couts.get(e["appel"], 0.0) + e["cout_usd"]
    par_instrument = {}
    for instrument in ("appariement", "couverture"):
        du_genre = [e for e in finies if e["instrument"] == instrument]
        par_longueur = {}
        for longueur in ("courte", "mediane", "longue"):
            choisis = [e for e in du_genre if e["longueur"] == longueur]
            par_longueur[longueur] = {"lectures": len(choisis),
                                      "sortie_moyenne": _moyenne([e["sortie_facturee"] for e in choisis]),
                                      "cout_moyen_usd": _moyenne([couts[e["appel"]] for e in choisis])}
        par_instrument[instrument] = {
            "lectures": len(du_genre), "non_conformes": sum(1 for e in du_genre if not e["conforme"]),
            "sortie_max": max((e["sortie_facturee"] for e in du_genre), default=None),
            "cout_moyen_par_appel_usd": _moyenne([couts[e["appel"]] for e in du_genre]), "par_longueur": par_longueur}
    coupes = [e["envoi"] for e in envois if e["incident"] in INCIDENTS_D_UN_ENVOI_COUPE]
    rapport = {
        "version": VERSION, "piece": "rapport-technique", "ligne": ligne, "go": manifeste["go"],
        "fournisseur": manifeste["fournisseur"], "hote": manifeste["contexte"]["hote"], "quand": heure(),
        "texte_en_vigueur": manifeste["texte_en_vigueur"], "regles": manifeste["regles"],
        "releve_de_verification": manifeste["contexte"]["releve"], "nom_servi_du_releve": manifeste["contexte"]["nom_servi"],
        "issue_de_la_sonde": manifeste["contexte"]["sonde"], "regime_de_depart": manifeste["contexte"]["regime"],
        "lectures_prevues": CRITERES[ligne]["lectures"], "envois": envois, "nombre_d_envois": len(envois),
        "lectures_jouees": len(lectures), "reponses_de_code_200": sum(1 for e in lectures if e["code"] == 200 and not e["incident"]),
        "refus": sum(1 for e in lectures if e["code"] == 200 and not e["incident"] and e["classe_du_motif"] == "refus"),
        "fins_par_sortie_maximale": sum(1 for e in lectures if e["classe_du_motif"] == "sortie_max"),
        "conformes": sum(1 for e in finies if e["conforme"]), "etayees": sum(1 for e in finies if e["etayee"]),
        "blocs_de_code_retires": sum(1 for e in finies if e["bloc_de_code_retire"]),
        "noms_servis": sorted({n for e in lectures for n in (e["noms_servis"] or []) if isinstance(n, str)}),
        "lectures_sans_nom_servi_lisible": sum(1 for e in lectures if e["code"] == 200 and not e["nom_servi"]),
        "sortie_facturee_max": max((e["sortie_facturee"] for e in finies), default=None),
        "sorties_au_dela_de_la_sortie_maximale": sum(1 for e in finies if e["sortie_facturee_au_dela_de_la_sortie_maximale"]),
        "par_instrument": par_instrument, "durees_s": [e["duree_s"] for e in envois],
        "envois_coupes": coupes, "lecture_de_la_console_due": bool(coupes),
        "departs_sans_reponse_reconstitues": sorted(orphelins),
        "cle_vue_dans_une_reponse": cle_vue_par_le_relais(dossier / "relais" / "journal-relais.jsonl"),   # m-c
        "depense_comptee_usd": round(sum(e["cout_usd"] for e in envois), 6),
        "fin": {k: v for k, v in (fin or {}).items() if k not in ("evenement", "quand")} if fin else None,
        "complete": bool(fin and fin.get("complet")),
        "arret": (fin or {}).get("arret") if fin else "file sans ligne de fin au journal : interrompue de notre côté",
    }
    rapport["cout_projete"] = cout_projete(rapport, manifeste.get("projection") or {})
    return rapport


def cout_projete(rapport: dict, projection: dict):
    """Mesuré et rapporté, sans verdict (devis, section 7). Mistral : la grandeur `C` du devis de l'essai de mesure
    (lectures de l'appariement et de la couverture, redemandes au taux de non-conformité mesuré ; l'appariement
    pondéré ¼, ½, ¼ par longueur). Neon : le coût moyen d'un appel par instrument."""
    a, c = rapport["par_instrument"]["appariement"], rapport["par_instrument"]["couverture"]
    if rapport["ligne"] == "file-neon":
        return {"cout_moyen_par_appel_usd": {"appariement": a["cout_moyen_par_appel_usd"],
                                             "couverture": c["cout_moyen_par_appel_usd"]}}
    la, lc = (a["par_longueur"][k]["cout_moyen_usd"] for k in ("courte", "mediane", "longue")), None
    courte, mediane, longue = la
    cout_a = None if None in (courte, mediane, longue) else 0.25 * courte + 0.5 * mediane + 0.25 * longue
    cout_c = _moyenne([c["par_longueur"][k]["cout_moyen_usd"] for k in ("courte", "mediane", "longue")])
    if cout_a is None or cout_c is None or not a["lectures"] or not c["lectures"] or not projection:
        return {"C_usd": None}
    return {"C_usd": round(projection["lectures_appariement"] * cout_a * (1 + a["non_conformes"] / a["lectures"])
                           + projection["lectures_couverture"] * cout_c * (1 + c["non_conformes"] / c["lectures"]), 4)}


def texte_du_rapport(rapport: dict) -> str:
    return "\n".join([
        f"# Rapport technique — {rapport['ligne']} — bras A, essai d'admission ({ROLES[rapport['ligne']]})", "",
        f"- ligne de calcul : {rapport['go']} ; point d'accès : {rapport['hote']} ; régime de départ : {rapport['regime_de_depart']}",
        f"- texte en vigueur : {rapport['texte_en_vigueur']['sha256']}",
        f"- lectures : {rapport['lectures_jouees']} sur {rapport['lectures_prevues']} ; envois : {rapport['nombre_d_envois']}",
        f"- réponses de code 200 : {rapport['reponses_de_code_200']} ; refus : {rapport['refus']} ; fins par sortie "
        f"maximale atteinte : {rapport['fins_par_sortie_maximale']}",
        f"- de forme conforme : {rapport['conformes']} ; étayées (sans verdict) : {rapport['etayees']}",
        f"- noms servis : {rapport['noms_servis']} ; dépense comptée : {rapport['depense_comptee_usd']} USD",
        f"- envois coupés : {rapport['envois_coupes']} ; lecture de la console due : {rapport['lecture_de_la_console_due']}",
        f"- file complète : {rapport['complete']} ; arrêt : {rapport['arret']}", "",
        "Aucun texte de réponse. Les règles d'admission s'appliquent par la commande `regles`.", ""])


def appliquer_regles(rapport: dict) -> dict:
    """Les critères écrits d'avance, recopiés du devis (section 7) et du texte (3.4), appliqués **sur les seuls
    compteurs du rapport** (règle 8). Règle 1 : Mistral Large 4 tient si ses 24 lectures rendent 24 réponses de code
    200, reprise unique comprise, sans refus, sans fin par sortie maximale atteinte, avec au moins 22 réponses de
    forme conforme ; une file arrêtée à son plafond ne tient pas. Règle 2 : `gemini-4-neon` tient si ses huit lectures
    rendent huit réponses de code 200, sans refus, sans fin par sortie maximale atteinte, toutes les huit de forme
    conforme. Règle 3 : toutes les réponses portent le nom servi relevé à la vérification de la clé ; ne tient pas non
    plus une file coupée par le service après son premier envoi. Règle 5 : si le modèle tient, il prend son rôle ;
    sinon son rôle n'est pas pourvu : nœud de Lazar. Règle 7 : sortie maximale à la course."""
    ligne = rapport["ligne"]
    critere, causes = CRITERES[ligne], []
    n = critere["lectures"]
    if rapport["reponses_de_code_200"] != n or rapport["lectures_jouees"] != n:
        causes.append(f"{rapport['reponses_de_code_200']} réponse(s) de code 200 sur {n} lectures")
    if rapport["refus"]:
        causes.append(f"{rapport['refus']} refus")
    if rapport["fins_par_sortie_maximale"]:
        causes.append(f"{rapport['fins_par_sortie_maximale']} fin(s) par sortie maximale atteinte")
    if rapport["conformes"] < critere["conformes_min"]:
        causes.append(f"{rapport['conformes']} réponse(s) de forme conforme, sous {critere['conformes_min']}")
    if not rapport["complete"]:
        causes.append(f"file non menée au bout : {rapport['arret']}")
    if rapport["noms_servis"] != [rapport["nom_servi_du_releve"]] or rapport["lectures_sans_nom_servi_lisible"]:
        causes.append("une réponse ne porte pas le nom servi que la vérification de la clé a relevé")
    tient = not causes
    observee = rapport["sortie_facturee_max"]
    regle_7 = None
    if observee is not None:
        regle_7 = {"maximum_observe_de_la_sortie_facturee": observee,
                   "sortie_maximale_a_la_course": max(8192, 1024 * math.ceil(4 * observee / 1024)),
                   "lue_sur": ("réponse et réflexion ensemble (sonde « comprise »)"
                               if rapport["issue_de_la_sonde"] == "comprise"
                               else "la sortie facturée entière, qui majore la réponse seule : nœud de Lazar (devis, 4.6)")}
    return {"version": VERSION, "ligne": ligne, "tient": tient, "causes": causes,
            "critere": {"lectures": n, "conformes_min": critere["conformes_min"], "un_seul_nom_servi": True},
            "suite": (f"le modèle est le {ROLES[ligne]}" if tient
                      else f"le rôle de {ROLES[ligne]} n'est pas pourvu : nœud de Lazar, tableau des mesures à l'appui"),
            "regle_7": regle_7, "rapport_sha256": None, "regles_sha256": rapport["regles"]["sha256"]}


def appliquer_regles_au_dossier(dossier: Path, config: dict, racine: Path) -> dict:
    """Garde 12, second temps : le programme des règles ne lit que le rapport, et refuse un fichier des règles dont
    l'empreinte n'est pas celle du manifeste de la file."""
    chemin = dossier / "rapport-technique.json"
    if not chemin.is_file():
        raise Arret("rapport technique absent : les règles ne s'appliquent pas")
    compagnon = Path(str(chemin) + ".sha256")
    if not compagnon.is_file() or compagnon.read_text(encoding="utf-8").split()[0] != sha256_fichier(chemin):
        raise Arret("le rapport technique ne répond pas à son empreinte compagnon")
    rapport = json.loads(chemin.read_text(encoding="utf-8"))
    fichier = racine / rapport["regles"]["chemin"]
    if not fichier.is_file() or sha256_fichier(fichier) != rapport["regles"]["sha256"]:
        raise Arret("garde 12 : le fichier des règles n'a plus l'empreinte du manifeste de la file : "
                    "le programme des règles refuse")
    if config["regles"]["sha256"] != rapport["regles"]["sha256"]:
        raise Arret("garde 12 : la configuration cite un autre fichier des règles que le manifeste de la file")
    # V-1 : le rapport scellé doit répondre au journal de la file (un rapport figé avant la fin ne sert aucune règle).
    if not file_close(dossier):
        raise Arret("la file n'est pas close : les règles ne s'appliquent pas encore")
    recalcule = faire_rapport(dossier)
    for cle in ("nombre_d_envois", "lectures_jouees", "reponses_de_code_200", "conformes", "complete", "depense_comptee_usd"):
        if recalcule.get(cle) != rapport.get(cle):
            raise Arret(f"le rapport scellé ne répond pas au journal de la file (« {cle} ») : nœud de Lazar, "
                        "les règles ne s'appliquent pas")
    resultat = appliquer_regles(rapport)
    resultat["rapport_sha256"] = sha256_fichier(chemin)
    return resultat


# --- relais : lancement par ligne, arrêt par identifiant de processus ----------------------------------------------------

def charger_lanceur(racine: Path, config: dict):
    verifier_piece(racine, config["lanceur_relais"], "lanceur de relais")
    spec = importlib.util.spec_from_file_location("lancer_relais_local_v1", racine / config["lanceur_relais"]["chemin"])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def arguments_du_relais(config: dict, ligne: str) -> list:
    """Un relais est lancé par ligne de calcul, avec la borne d'appels de cette ligne et, pour celui de Mistral, le
    plafond en dollars de cette ligne (devis, 6.4)."""
    _, fournisseur, _ = LIGNES[ligne]
    f, L = config["fournisseurs"][fournisseur], config["lignes"][ligne]
    arguments = ["--variable-cle", f["variable_cle"], "--port", "0", "--amont", L["hote"], "--modele",
                 IDENTIFIANTS[fournisseur], "--max-appels", str(L["envois_max"]),
                 "--delai-total-s", str(L["delais"]["relais_total_s"])]
    if fournisseur == "mistral":
        arguments += ["--plafond-usd", str(L["plafond_usd"]), "--prix-entree", str(f["prix"][0]), "--prix-sortie",
                      str(f["prix"][1]), "--reserve-sortie-jetons", str(L["reserve_sortie_jetons"]),
                      "--delai-silence-s", str(L["delais"]["relais_silence_s"])]
    essai = (config.get("essai_local") or {}).get(fournisseur)
    if essai:
        arguments += ["--adresse-d-essai", essai]
    return arguments


def controler_voie_d_essai(config: dict, fournisseur: str) -> None:
    """Garde 14, voie d'accès : une configuration définitive ne porte aucune adresse d'essai ; une configuration qui
    n'est pas définitive ne joint que le faux fournisseur local, jamais un hôte réel."""
    essai = (config.get("essai_local") or {}).get(fournisseur)
    if config.get("etat") == "definitive":
        if config.get("essai_local"):
            raise Arret("garde 14 : une configuration définitive ne porte aucune adresse d'essai : rien ne part")
    elif not essai:
        raise Arret("garde 14 : une configuration qui n'est pas définitive ne joint que le faux fournisseur local, "
                    "et aucune adresse d'essai n'y est inscrite pour ce fournisseur : rien ne part")


def lancer_relais(config: dict, ligne: str, racine: Path, dossier: Path, environnement) -> dict:
    """Garde 7 : le relais est lancé par le lanceur du dépôt, environnement réduit à des noms, clé **exigée par son
    nom**. Ce programme ne lit ni n'affiche aucune valeur de clé."""
    _, fournisseur, _ = LIGNES[ligne]
    f = config["fournisseurs"][fournisseur]
    relais = f["relais"]
    controler_voie_d_essai(config, fournisseur)
    verifier_piece(racine, relais, "relais")
    lanceur = charger_lanceur(racine, config)
    (dossier / "relais").mkdir(parents=True, exist_ok=True)
    console = dossier / "relais" / "console-relais.txt"
    journal = dossier / "relais" / "journal-relais.jsonl"
    commande = [sys.executable, "-I", "-B", str(racine / relais["chemin"]), *arguments_du_relais(config, ligne),
                "--journal", str(journal)]
    noms = list(relais["noms_environnement"]) + ["!" + f["variable_cle"]]
    try:
        lance = lanceur.lancer(str(console), noms, commande, source=environnement)
    except lanceur.Refus as refus:
        raise Arret(f"garde 7 : le lanceur de relais refuse ({refus}) : rien ne part") from None
    return {"pid": lance["pid"], "console": console, "journal": journal, "noms_transmis": lance["noms_transmis"]}


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
        return json.loads(connexion.getresponse().read().decode("utf-8"))
    finally:
        connexion.close()


def controler_etat_initial(etat: dict, config: dict, ligne: str) -> None:
    """Garde 14, côté relais : amont de la ligne, modèle figé, borne d'appels de la ligne, relais neuf ; une adresse
    d'essai n'est admise que si la configuration la déclare."""
    _, fournisseur, _ = LIGNES[ligne]
    L = config["lignes"][ligne]
    attendu = {"amont": L["hote"], "modele": IDENTIFIANTS[fournisseur], "appels": 0, "max_appels": L["envois_max"],
               "adresse_d_essai": (config.get("essai_local") or {}).get(fournisseur),
               "cle_dans_l_environnement": False}
    if fournisseur == "mistral":
        attendu["plafond_usd"] = L["plafond_usd"]
    for cle, valeur in attendu.items():
        if etat.get(cle) != valeur:
            raise Arret(f"relais : état initial inattendu pour « {cle} » ({etat.get(cle)!r} au lieu de {valeur!r}) : "
                        "rien ne part")


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


def chercher_formes_de_cle(dossier: Path) -> list:
    """Garde 7 : toute chaîne de la forme d'une clé dans ce que la ligne a écrit ; rend les chemins, jamais la chaîne."""
    trouves = []
    for chemin in sorted(p for p in dossier.rglob("*") if p.is_file()):
        contenu = chemin.read_bytes().decode("utf-8", errors="replace")
        if any(re.search(forme, contenu) for forme in FORMES_DE_CLE):
            trouves.append(str(chemin.relative_to(dossier)))
    return trouves


def cle_vue_par_le_relais(journal_relais) -> int:
    """Garde 7 (m-4) : nombre d'envois où le relais a vu la valeur exacte de sa clé dans ce que rendait l'amont."""
    try:
        return sum(1 for l in lire_journal(Path(journal_relais)) if l.get("cle_vue_dans_la_reponse") is True)
    except Arret:
        return 1          # journal du relais illisible : du côté prudent


def inventorier(dossier: Path, etat: str, nom: str = "inventaire.json") -> dict:
    """Inventaire de tout ce que la ligne a produit (nom, taille, empreinte), avec son empreinte compagnon."""
    fichiers = []
    for chemin in sorted(p for p in dossier.rglob("*") if p.is_file()):
        relatif = str(chemin.relative_to(dossier))
        if relatif in (nom, nom + ".sha256"):
            continue
        fichiers.append({"chemin": relatif, "octets": chemin.stat().st_size, "sha256": sha256_fichier(chemin)})
    inventaire = {"version": VERSION, "quand": heure(), "etat": etat, "fichiers": fichiers, "nombre": len(fichiers)}
    octets = json_octets(inventaire)
    with open(dossier / nom, "wb") as f:
        f.write(octets)
        f.flush()
        os.fsync(f.fileno())
    with open(dossier / (nom + ".sha256"), "w", encoding="utf-8") as f:
        f.write(f"{sha256_octets(octets)}  {nom}\n")
    return inventaire


# --- une ligne, de bout en bout ------------------------------------------------------------------------------------------

def gardes_avant_depart(config: dict, ligne: str, environnement, racine: Path, registre: str | None,
                        a_l_instant: datetime.datetime, a_blanc: bool = False) -> dict:
    """Toutes les gardes d'avant le premier envoi d'une ligne. Un défaut lève `Arret` : rien ne part. `a_blanc`
    (m-13) : les mêmes gardes, hors la ligne de calcul (garde 8) ; rien n'est lancé."""
    genre, fournisseur, _ = LIGNES[ligne]
    controler_identifiants(config, ligne)                                             # garde 14
    go = config["lignes"][ligne].get("go")
    empreinte_ligne = None if a_blanc else verifier_ligne_de_calcul(
        config, ligne, environnement, registre, a_l_instant.strftime("%Y-%m-%d"))     # garde 8
    controler_verification_du_devis(config, racine)                                   # garde 8 (m-15), marge de change
    lot = charger_textes(config, racine)
    constat = garde_constat(config, racine, a_l_instant)                              # garde 9
    levees = garde_cle_vue(config, racine, ligne)                                     # garde 7 (m-c)
    lectures = garde_console(config, racine, ligne, go, constat["devises"])           # garde 20
    avant = {"ligne": ligne, "go": go, "fournisseur": fournisseur, "empreinte_ligne_go": empreinte_ligne,
             "alertes_de_cle_levees": levees, "conversions_du_constat": constat["conversions"],
             "lectures_de_la_console": lectures, "constat": config["constat"], "contexte": None, "etat": None,
             "regles": None, "dossiers_anterieurs_sans_depart": []}
    if genre == "verification":
        if ligne == "verification-mistral-global":
            garde_repli(config, racine)                                               # garde 15
        etat = etat_de_la_ligne(racine, config, ligne, go)
        if etat["close"]:
            raise Arret(f"la ligne {go} est close : ce qui se refait demande une ligne nouvelle")
        avant["etat"] = etat
    else:
        avant["contexte"] = garde_cle_verifiee(config, racine, ligne, constat)        # garde 10
        avant["regles"] = {"chemin": config["regles"]["chemin"], "sha256": garde_regles(config, racine)}  # garde 12
        entrees_de_la_file(ligne, config, lot)                                        # garde 17
        deja, sans_depart = dossiers_de_la_file(racine / config["lignes"][ligne]["dossier"], ligne)
        if deja:
            raise Arret(f"garde 13 : la file a déjà un dossier parti ({deja[0]}) : une file ne se rejoue pas")
        avant["dossiers_anterieurs_sans_depart"] = sans_depart
    verifier_piece(racine, config["fournisseurs"][fournisseur]["relais"], "relais")
    charger_lanceur(racine, config)
    for page in config.get("pages_de_prix", []):   # devis, 6.1 : sans page conforme, le prix compté ne vaut plus
        verifier_piece(racine, page, "page de prix")
    return avant


def controler_tous_les_corps(config: dict, ligne: str, lot: dict, interdits: list, contexte: dict | None) -> int:
    """Gardes 3 et 6, avant tout envoi : chaque corps de la ligne est construit et contrôlé. Rend leur nombre."""
    genre, fournisseur, _ = LIGNES[ligne]
    f = config["fournisseurs"][fournisseur]
    chemin, en_tetes, faits = chemin_de_l_appel(fournisseur), en_tetes_de_l_envoi("controle"), 0
    if genre == "verification":
        variantes = [(config["messages"]["appel_a"], f["sortie_max"], True, 0), (config["messages"]["appel_a"], f["sortie_max"], False, 1),
                     (config["messages"]["sonde"], f["sortie_max_sonde"], True, 0)]
        for message, sortie_max, temperature, rang in variantes:
            orthographe = f["orthographes_niveau"][rang] if fournisseur == "google" else None
            corps = construire_corps(fournisseur, f, message, sortie_max, temperature, orthographe)
            controler_corps(fournisseur, f, corps, chemin, sortie_max, temperature, orthographe)
            controler_envoi(json.dumps(corps, ensure_ascii=False).encode("utf-8"), en_tetes, interdits)
            faits += 1
        return faits
    for ident in entrees_de_la_file(ligne, config, lot):
        corps = construire_corps(fournisseur, f, lot["textes"][ident]["texte"], f["sortie_max"],
                                 bool(contexte.get("temperature_envoyee")), contexte.get("orthographe_niveau"))
        controler_corps(fournisseur, f, corps, chemin, f["sortie_max"], bool(contexte.get("temperature_envoyee")),
                        contexte.get("orthographe_niveau"))
        controler_envoi(json.dumps(corps, ensure_ascii=False).encode("utf-8"), en_tetes, interdits)
        faits += 1
    return faits


def executer(ligne: str, chemin_configuration, empreinte_configuration: str, environnement, racine: Path = RACINE,
             registre: str | None = None, a_l_instant: datetime.datetime | None = None, commande_ouvrier=None) -> int:
    """Joue une ligne de bout en bout. `racine`, `registre`, `a_l_instant` et `commande_ouvrier` ne servent qu'aux
    essais : la ligne de commande ne les expose pas."""
    dossier, relais, verrou = None, None, None
    a_l_instant = a_l_instant or maintenant()
    try:
        if ligne not in LIGNES:
            raise Arret(f"ligne inconnue : {ligne!r}")
        config = charger_configuration(Path(chemin_configuration), empreinte_configuration)
        genre, fournisseur, _ = LIGNES[ligne]
        avant = gardes_avant_depart(config, ligne, environnement, racine,
                                    registre if registre is not None else lire_registre_git(racine, config), a_l_instant)
        lot = charger_textes(config, racine)
        charger_programme_de_forme(config, racine)
        interdits = charger_interdits(config, racine, environnement)
        prevus = controler_tous_les_corps(config, ligne, lot, interdits, avant["contexte"])
        controler_voie_d_essai(config, fournisseur)
        # m-a : verrou exclusif de la ligne, tenu par l'amorce jusqu'à sa fin (le système le lâche si elle meurt). Deux
        # lancements simultanés ne passent pas tous deux la garde 13 : les gardes sont rejouées sous le verrou.
        base = racine / config["lignes"][ligne]["dossier"]
        base.mkdir(parents=True, exist_ok=True)
        verrou = os.open(base / f"{ligne}.verrou", os.O_CREAT | os.O_RDWR, 0o644)
        try:
            fcntl.flock(verrou, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            os.close(verrou)
            verrou = None
            raise Arret(f"un autre lancement de la ligne {ligne} est en cours (verrou tenu) : rien ne part") from None
        avant = gardes_avant_depart(config, ligne, environnement, racine,
                                    registre if registre is not None else lire_registre_git(racine, config), a_l_instant)
        dossier = racine / config["lignes"][ligne]["dossier"] / f"{a_l_instant.strftime('%Y%m%d-%H%M%S')}-{ligne}"
        try:
            dossier.mkdir(parents=True)
        except OSError as erreur:
            dossier = None
            raise Arret(f"dossier de la ligne impossible à créer ({type(erreur).__name__}) : rien ne part") from None
    except Arret as garde:
        if verrou is not None:
            os.close(verrou)
        print(f"ARRÊT avant tout envoi : {garde}", file=sys.stderr)
        return 2
    journal = Journal(dossier / "journal-amorce.jsonl")
    processus, recu = None, {"signal": None}

    def sur_signal(numero, cadre):
        recu["signal"] = numero
        if processus is not None and processus.poll() is None:
            processus.send_signal(signal.SIGTERM)

    # m-14 : le raccrochage du terminal arrête la ligne proprement, sauf s'il est déjà ignoré (`nohup`).
    signaux = [signal.SIGINT, signal.SIGTERM] + (
        [signal.SIGHUP] if signal.getsignal(signal.SIGHUP) != signal.SIG_IGN else [])
    anciens = {s: signal.signal(s, sur_signal) for s in signaux}
    code, etat_final = 2, "interrompue"
    try:
        manifeste = {
            "version": VERSION, "ligne": ligne, "genre": genre, "fournisseur": fournisseur, "go": avant["go"],
            "empreinte_ligne_go": avant["empreinte_ligne_go"], "depart": heure(),
            "commit": _sortie_git(racine, "rev-parse", "HEAD"), "python": sys.version.split()[0],
            "pid_amorce": os.getpid(),
            "configuration": {"chemin": str(chemin_configuration), "sha256": empreinte_configuration},
            "chef": {"chemin": str(Path(__file__).resolve()), "sha256": sha256_fichier(__file__)},
            "devis": config["devis"], "texte_en_vigueur": config["prereg_en_vigueur"], "entrees": config["entrees"],
            "consignes": config["consignes"], "constat": config["constat"], "regles": avant["regles"],
            "relais": {**config["fournisseurs"][fournisseur]["relais"], "arguments": arguments_du_relais(config, ligne)},
            "variable_cle": config["fournisseurs"][fournisseur]["variable_cle"],
            "interdits": {"nombre": len(interdits), "sha256": sha256_octets("\n".join(interdits).encode("utf-8"))},
            "corps_controles_avant_depart": prevus, "contexte": avant["contexte"],
            "lectures_de_la_console": avant["lectures_de_la_console"], "projection": config.get("projection"),
            "dossiers_anterieurs_sans_depart": avant["dossiers_anterieurs_sans_depart"],
            "alertes_de_cle_levees": avant["alertes_de_cle_levees"],
            "conversions_du_constat": avant["conversions_du_constat"], "marge_de_change": config.get("marge_de_change"),
            "interpreteur": sys.executable,
            "graines": "aucun tirage dans le chef d'essai ; graines des textes dans le lot des entrées (R9)",
        }
        ecrire_neuf(dossier / "manifeste-depart.json", json_octets(manifeste))
        # Devis, section 8, « Gardé » : la configuration de la ligne est gardée au dossier, telle que lue.
        ecrire_neuf(dossier / "configuration.json", Path(chemin_configuration).read_bytes())
        relais = lancer_relais(config, ligne, racine, dossier, environnement)
        journal.ecrire(evenement="relais_lance", pid=relais["pid"], noms_transmis=relais["noms_transmis"])
        url = attendre_relais(relais["console"], relais["pid"])
        initial = etat_relais(url)
        ecrire_neuf(dossier / "relais" / "etat-initial.json", json_octets(initial))
        controler_etat_initial(initial, config, ligne)
        if recu["signal"] is not None:
            raise Arret(f"signal {recu['signal']} avant le départ de l'ouvrier")
        commande = (commande_ouvrier or [sys.executable, "-I", "-B", str(Path(__file__).resolve()), "--ouvrier"]) + [str(dossier)]
        env_ouvrier = {k: environnement[k] for k in ENVIRONNEMENT_OUVRIER if k in environnement}
        entree = json.dumps({"url_relais": url, "journal_relais": str(relais["journal"]), "interdits": interdits,
                             "racine": str(racine), "etat": avant["etat"]}).encode("utf-8")
        # m-8 : la sortie d'erreur de l'ouvrier est gardée au dossier (motifs d'arrêt ; jamais un texte de réponse).
        with open(dossier / "ouvrier-sortie-erreur.txt", "xb") as erreurs:
            processus = subprocess.Popen(commande, env=env_ouvrier, stdin=subprocess.PIPE, stderr=erreurs, cwd=str(racine))
        processus.stdin.write(entree)
        processus.stdin.close()
        while processus.poll() is None:
            time.sleep(0.2)
        journal.ecrire(evenement="ouvrier_fini", code=processus.returncode, signal_recu=recu["signal"])
        code = processus.returncode if recu["signal"] is None else 4
        etat_final = "finie" if code == 0 else "arretee"
    except Arret as garde:
        journal.ecrire(evenement="arret", motif=str(garde))
        print(f"ARRÊT : {garde}", file=sys.stderr)
        code, etat_final = 2, "arretee"
    except BaseException as panne:  # noqa: BLE001 — tout se termine par l'inventaire, quelle que soit la panne
        journal.ecrire(evenement="panne", genre=type(panne).__name__)
        code, etat_final = 5, "arretee"
    finally:
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
                code = code or 6
        try:
            cles = chercher_formes_de_cle(dossier)
            journal.ecrire(evenement="recherche_de_formes_de_cle", fichiers=cles)
            if cles:
                print(f"ARRÊT : chaîne de la forme d'une clé dans {cles} — ne rien pousser avant examen", file=sys.stderr)
                code = 7
            # m-4 : le relais, qui tient la clé, cherche sa valeur exacte dans tout ce que rend l'amont, la masque
            # et le dit par un booléen à son journal. Le chef ne connaît jamais la valeur.
            vues = cle_vue_par_le_relais(relais["journal"]) if relais is not None else 0
            journal.ecrire(evenement="cle_vue_par_le_relais_dans_une_reponse", envois=vues)
            if vues:
                print("ARRÊT : garde 7 : le relais a vu la valeur de sa clé dans une réponse de l'amont (masquée avant "
                      "d'être relayée) — nœud de Lazar, clé à révoquer", file=sys.stderr)
                code = 7
        except OSError as erreur:
            journal.ecrire(evenement="recherche_de_formes_de_cle_impossible", genre=type(erreur).__name__)
        try:
            if genre == "file" and (dossier / "journal-essai.jsonl").exists():
                if (dossier / "rapport-technique.json").exists():
                    # V-1 : l'amorce seule rend le rapport de sa file ; un rapport déjà là n'est pas le sien.
                    raise Arret("un rapport que l'amorce n'a pas écrit est au dossier : nœud de Lazar, il n'est pas gardé "
                                "en silence et les règles ne s'appliquent pas")
                rapport = faire_rapport(dossier)
                rendre_piece(dossier, "rapport-technique.json", rapport, fournisseur, texte_du_rapport(rapport))
        except (Arret, OSError, KeyError, ValueError) as erreur:
            journal.ecrire(evenement="rapport_non_rendu", motif=str(erreur)[:200])
            print(f"ARRÊT : {erreur}", file=sys.stderr)
            code = code or 8
        journal.ecrire(evenement="fin", code=code, etat=etat_final)
        inventaire = inventorier(dossier, etat_final)
        if verrou is not None:
            os.close(verrou)
    print(json.dumps({"ligne": ligne, "code": code, "etat": etat_final, "dossier": str(dossier),
                      "fichiers_inventories": inventaire["nombre"]}, ensure_ascii=False))
    return code


def ouvrier(dossier: Path, environnement, entree: bytes) -> int:
    """L'ouvrier : environnement réduit, aucune clé ; il revérifie la configuration et les textes, puis joue la ligne."""
    if any(re.search(r"KEY|TOKEN|SECRET", k) for k in environnement):
        print("ARRÊT : garde 7 : l'ouvrier ne part pas avec un nom de clé dans son environnement", file=sys.stderr)
        return 2
    try:
        manifeste = json.loads((dossier / "manifeste-depart.json").read_text(encoding="utf-8"))
        if manifeste["pid_amorce"] != os.getppid() or environnement.get("GO_ID") != manifeste["go"]:
            raise Arret("l'ouvrier n'est lancé que par son amorce, sous la ligne de calcul de la ligne")
        donnees = json.loads(entree.decode("utf-8"))
        racine = Path(donnees["racine"])
        config = charger_configuration(Path(manifeste["configuration"]["chemin"]), manifeste["configuration"]["sha256"])
        lot = charger_textes(config, racine)
        programme = charger_programme_de_forme(config, racine)
    except (Arret, OSError, ValueError, KeyError) as garde:
        print(f"ARRÊT de l'ouvrier avant tout envoi : {garde}", file=sys.stderr)
        return 2
    signal.signal(signal.SIGTERM, _lever_interruption)
    signal.signal(signal.SIGINT, _lever_interruption)
    ligne = manifeste["ligne"]
    try:
        if manifeste["genre"] == "verification":
            releve = jouer_verification(config, ligne, dossier, donnees["url_relais"], donnees["journal_relais"],
                                        donnees["interdits"], donnees["etat"], manifeste["go"])
            return code_de_sortie_verification(releve)
        bilan = jouer_file(config, ligne, lot, dossier, donnees["url_relais"], donnees["journal_relais"],
                           donnees["interdits"], manifeste["contexte"], programme)
        return 0 if bilan["complet"] else 1
    except Arret as garde:
        print(f"ARRÊT de l'ouvrier : {garde}", file=sys.stderr)
        return 2
    except Exception as panne:  # noqa: BLE001 — m-8 : une panne du programme a son code (9), distinct d'une file non
        # complète (1). La trace gardée ne porte que le type et les lieux du code, jamais le message (qui pourrait
        # citer une donnée reçue).
        lieux = [f"{Path(c.filename).name}:{c.lineno} dans {c.name}" for c in traceback.extract_tb(panne.__traceback__)]
        print(f"PANNE de l'ouvrier : {type(panne).__name__} ; " + " < ".join(reversed(lieux)), file=sys.stderr)
        return 9


def a_blanc(ligne: str, chemin_configuration, empreinte_configuration: str, environnement, racine: Path = RACINE,
            a_l_instant: datetime.datetime | None = None) -> int:
    """m-13 : joue les gardes d'avant départ d'une ligne (9, 10, 12, 13, 14, 15, 17, 20, puis 3 et 6 sur tous les
    corps), sans ligne de calcul, sans rien lancer ni rien écrire. Code 0 : tout passe, hors la garde 8."""
    config = charger_configuration(Path(chemin_configuration), empreinte_configuration)
    avant = gardes_avant_depart(config, ligne, environnement, racine, None, a_l_instant or maintenant(), a_blanc=True)
    lot = charger_textes(config, racine)
    charger_programme_de_forme(config, racine)
    corps = controler_tous_les_corps(config, ligne, lot, charger_interdits(config, racine, environnement), avant["contexte"])
    print(json.dumps({"ligne": ligne, "a_blanc": True, "gardes_passees": "9, 10, 12, 13, 14, 15, 17, 20, 3 et 6",
                      "garde_non_jouee": "8 (ligne de calcul)", "corps_controles": corps,
                      "regime": (avant["contexte"] or {}).get("regime"),
                      "lectures_de_la_console": len(avant["lectures_de_la_console"]),
                      "etat_de_la_ligne": ({k: avant["etat"][k] for k in ("depense_comptee_usd", "lancements", "close")}
                                           if avant["etat"] else None),
                      "dossiers_anterieurs_sans_depart": avant["dossiers_anterieurs_sans_depart"]},
                     ensure_ascii=False, indent=1, sort_keys=True))
    return 0


def file_close(dossier: Path) -> bool:
    """V-1 : une file est close si son amorce a écrit son événement « fin », ou si le processus de l'amorce (inscrit
    au manifeste) n'est plus en vie. Sans identifiant de processus au manifeste, rien ne le dit : non close."""
    if any(l.get("evenement") == "fin" for l in lire_journal(dossier / "journal-amorce.jsonl")):
        return True
    manifeste = lire_json((dossier / "manifeste-depart.json").read_bytes()) if (dossier / "manifeste-depart.json").is_file() else None
    pid = manifeste.get("pid_amorce") if isinstance(manifeste, dict) else None
    return _entier(pid) and pid > 1 and not processus_vivant(pid)


def rapport_du_dossier(dossier: Path) -> dict:
    """Commande `rapport` : le rapport d'une file, **toujours recalculé** du journal. Il n'est écrit et scellé que si
    aucun rapport n'existe **et** que la file est close (V-1 : lancée pendant qu'une file tourne, la commande ne fige
    rien) ; il porte alors un inventaire d'après-coup, sous un nom neuf (R12). Le rapport rendu dit `ecrit`."""
    rapport = faire_rapport(dossier)
    ecrit = False
    if not (dossier / "rapport-technique.json").exists() and file_close(dossier):
        rendre_piece(dossier, "rapport-technique.json", rapport, rapport["fournisseur"], texte_du_rapport(rapport))
        inventorier(dossier, "rapport rendu après coup", nom=f"inventaire-apres-coup-{maintenant().strftime('%Y%m%d-%H%M%S')}.json")
        ecrit = True
    return dict(rapport, ecrit=ecrit, file_close=file_close(dossier))


def principal(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) == 3 and argv[0] in LIGNES:
        return executer(argv[0], argv[1], argv[2], os.environ)
    if len(argv) == 2 and argv[0] == "--ouvrier":
        return ouvrier(Path(argv[1]), os.environ, sys.stdin.buffer.read())
    try:
        if len(argv) == 4 and argv[0] == "a-blanc" and argv[1] in LIGNES:
            return a_blanc(argv[1], argv[2], argv[3], os.environ)
        if len(argv) == 2 and argv[0] == "rapport":
            rapport = rapport_du_dossier(Path(argv[1]))
            print(texte_du_rapport(rapport))
            if not rapport["file_close"]:
                print("La file n'est pas close : rapport partiel, imprimé seulement, rien n'est écrit.", file=sys.stderr)
            return 0
        if len(argv) == 4 and argv[0] == "regles":
            config = charger_configuration(Path(argv[2]), argv[3])
            resultat = appliquer_regles_au_dossier(Path(argv[1]), config, RACINE)
            print(json.dumps(resultat, ensure_ascii=False, indent=1, sort_keys=True))
            return 0 if resultat["tient"] else 1
    except Arret as garde:
        print(f"ARRÊT : {garde}", file=sys.stderr)
        return 2
    print("usage : chef_essais_admission_bras_a_v2.py LIGNE CONFIGURATION EMPREINTE | rapport DOSSIER | "
          "regles DOSSIER CONFIGURATION EMPREINTE | a-blanc LIGNE CONFIGURATION EMPREINTE\n        LIGNE : " + ", ".join(LIGNES), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(principal())
