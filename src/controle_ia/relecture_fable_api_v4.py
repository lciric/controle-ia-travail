"""Relecture d'une correction par Claude Fable 5.2 (ou Claude Opus 4.6, v4), appelé directement par l'interface
d'Anthropic, version 4.

v4 (développeur, Claude Opus 5.5, 22 novembre 2026 ; pièce d'instrument, classe B) : copie de relecture_fable_api_v3.py
(95bea064…, inchangée, R12). Un seul changement : option --modele à valeurs fermées, `claude-fable-5-2` (défaut :
réglages, envoi, pire coût, journal et sorties de la v3, à l'identique hors le nom et l'empreinte de l'outil) et
`claude-opus-4-6`. Toute autre valeur est refusée avant tout envoi (par l'analyseur, et par `relire` si elle lui parvient
autrement). Un effort non admis par le modèle choisi (« xhigh » pour `claude-opus-4-6`) est refusé avant tout envoi, avec
ligne de refus au journal. Le champ « modele » du journal, des compteurs et de l'en-tête porte le modèle demandé ; la
garde « modèle servi autre que celui demandé » compare au modèle demandé.
Réglages de `claude-opus-4-6`, et section de la compétence « claude-api » (chargée le 22 novembre 2026) d'où chacun vient :
- identifiant `claude-opus-4-6` : SKILL.md, table « Current Models (cached: 2026-11-03) » ; shared/models.md, table
  « Current Models (recommended) » (« Claude Opus 4.6 | `claude-opus-4-6` | 1M | 128K | Active ») ;
- réflexion `{"type": "adaptive"}`, envoyée explicitement : SKILL.md, tableau « Thinking & Effort (Quick Reference) »,
  ligne « Opus 4.6 / Sonnet 4.6 » (« `{type: "adaptive"}` (recommended) » ; « Omitting `thinking` : Set
  `{type: "adaptive"}` explicitly ») ; shared/model-migration.md, « Migrating to Opus 4.7 », « Adaptive thinking is off
  by default […] requests with no `thinking` field run without thinking, matching Opus 4.6 behavior » ;
- pas de champ `display` : shared/model-migration.md, « Migrating to Opus 4.7 » (« "display" is new on Opus 4.7 » ;
  « a silent change from Claude Opus 4.6, where the default was to return summarized thinking text »). Sur ce modèle, le
  résumé de la réflexion revient donc dans la réponse ; l'outil ne lit que les blocs `text` : le texte de la réflexion
  n'est ni demandé par un réglage, ni lu, ni écrit ;
- aucun `budget_tokens` : tableau « Thinking & Effort », ligne « Opus 4.6 / Sonnet 4.6 » (« Deprecated - do not use in
  new code; transitional escape hatch only ») et shared/model-migration.md, « Migrating to Opus 4.6 / Sonnet 4.6 »,
  point 1 (« If the user asks for a "thinking budget" on 4.6, the preferred answer is `effort` ») ; aucune option de
  budget n'est donc offerte, pour aucun des deux modèles, et la « limite déclarée » de la v3 (fin de cette docstring)
  vaut aussi pour claude-opus-4-6 ;
- effort `output_config.effort` à valeurs low, medium, high, max (« max » admis, « xhigh » refusé), défaut « high » :
  tableau « Thinking & Effort », ligne « Opus 4.6 / Sonnet 4.6 » (« `low`/`medium`/`high`/`max` (`xhigh` arrived with
  Opus 4.7) ») ; shared/model-migration.md, « Migrating to Opus 4.6 / Sonnet 4.6 », point 2 (« Default is `high`. `max`
  is supported on Fable 5, Opus 4.6 and later ») ;
- `max_tokens` au plus 128 000, en flux : shared/models.md, colonne « Max Output » (128K) et « Model Descriptions »
  (« 128K max output tokens (requires streaming for large outputs) ») ; SKILL.md, « Common Pitfalls », « 128K output
  tokens » ; le défaut (128 000) et le minimum hors fumée (64 000) de la v3 sont gardés ;
- tarif 5 USD par million de jetons d'entrée, 25 en sortie : SKILL.md, table « Current Models » (« Claude Opus 4.6 |
  `claude-opus-4-6` | 1M | $5.00 | $25.00 ») ; lectures de cache 0,50 (≈ 0,1 × l'entrée, Opus 4.6 n'étant pas parmi les
  exceptions nommées) : shared/prompt-caching.md, « Economics » ; écriture de cache comptée à 2 × l'entrée (« 2× for
  1-hour TTL », même section ; prudent, aucune mise en cache n'est demandée) ; la réflexion est comptée en sortie ;
- comptage : `messages.count_tokens` avec le même modèle, même message, même réglage : shared/token-counting.md
  (« Token counts are **model-specific** - pass the same model ID you'll use for inference ») ; shared/model-migration.md,
  « Migrating to Opus 4.7 » (Opus 4.6 compte autrement qu'Opus 4.7 et suivants : aucun compte d'un autre modèle n'est
  réemployé) ;
- aucun paramètre d'échantillonnage (`temperature`, `top_p`, `top_k`) : SKILL.md, tableau « Thinking & Effort »
  (« Allowed (400 on `2026-10-21`) ») et shared/api-version-migration.md ; le kit 2.x envoie la version 2026-10-21 ;
- `refusal` toujours traité en défaut ; `stop_details` n'est garanti qu'à partir d'Opus 4.7 (SKILL.md, « Stop details
  (GA, Opus 4.7+) ») : la catégorie peut être nulle sur ce modèle ; `fallbacks` non envoyé, comme en v3.
Les noms des sorties (relecture-fable-api.md, compteurs.json, texte partiel) sont gardés ; l'en-tête nomme le modèle.

v3 (développeur, Claude Opus 5.5, 21 novembre 2026, ordre de la mère après un défaut de réglage constaté sur la v2) : copie
de relecture_fable_api_v2.py (c8e8506f…, inchangée, R12). Défaut constaté : à l'effort « max », sans borne de la
réflexion, la réflexion a pris toute la sortie sur deux lots d'une autre session (128 000 et 96 000 jetons, aucun texte),
et 95 000 à 115 000 jetons sur 128 000 sur les trois relectures réussies. Changements, et seulement ceux-là :
(1) option --effort, à valeurs fermées tirées de la compétence « claude-api » (shared/model-migration.md, « Migrating
    to Claude Fable 5.2 », « Choosing an effort level - start at `high` » : « All five levels are supported and the
    default is `high` ») : low, medium, high, xhigh, max ; défaut « high » ; toute autre valeur est refusée avant tout
    envoi (par l'analyseur, et par `relire` si elle lui parvient autrement) ;
(2) aucune option de budget de réflexion : la compétence ne permet pas de borner la réflexion de ce modèle. Sources :
    tableau « Thinking & Effort » de SKILL.md (Fable 5 / 5.1 / 5.2 : « `budget_tokens` : Removed - `{type: "enabled",
    budget_tokens: N}` returns 400 ») ; « Thinking is always on […] Control depth with `output_config.effort` » ; les
    budgets de tâche (`output_config.task_budget`, bêta `task-budgets-2026-03-13`, au moins 20 000) sont « a suggestion
    the model is aware of, not a hard cap » (shared/model-migration.md, « New feature: Task Budgets (beta) ») et ne
    garantissent donc aucun nombre de jetons de texte ; seul `max_tokens` est une borne, et elle porte sur réflexion et
    texte ensemble. Une option --budget-reflexion est refusée par l'analyseur (option inconnue) ;
(3) pire coût et journal inchangés : le champ « effort » du journal, des compteurs et de l'en-tête porte désormais
    l'effort demandé.

v1 (développeur neuf, Claude Opus 5.5, 21 novembre 2026 ; pièce d'instrument, classe B, à contre-lire par un autre
modèle). Écrite sur l'ordre de la mère, pour la décision de Lazar GO-2026-11-21-84 (limite d'usage de Fable dans Claude
Code jusqu'au 24 novembre 05:00Z : « Opus 5.5, en effort maximal, écrit seulement les corrections, mot pour mot d'après les
remarques déjà reçues. + appels api claude fable 5.2 puis sceller »).

Emploi :
    python -m controle_ia.relecture_fable_api_v4 relire --piece P [--piece P2 …] --remarques R [--remarques R2 …]
        [--avant V] --consigne C --sortie DOSSIER --cle NOM_DE_VARIABLE [--espace NOM_DE_VARIABLE]
        --plafond-ligne USD --journal-depense FICHIER [--max-sortie N] [--fumee]
        [--effort low|medium|high|xhigh|max] [--modele claude-fable-5-2|claude-opus-4-6]
    (v4 : « xhigh » n'est admis que pour claude-fable-5-2.)
Les points 1 à 9 et les sources ci-dessous décrivent la v3, soit le modèle par défaut ; pour claude-opus-4-6, le
modèle, la réflexion, les efforts admis et le tarif sont ceux de la section v4 ci-dessus.

Ce que fait l'outil, dans cet ordre (tout refus arrête l'outil avant l'envoi, code non nul, ligne au journal) :
 1. lit les fichiers donnés, et eux seuls (UTF-8 strict) ; une pièce absente est un refus ; si un compagnon `F.sha256`
    existe, l'empreinte du fichier doit lui être égale, sinon refus ; un compagnon mal formé est un refus ;
 2. compose l'invite : la consigne (fichier C) telle quelle, puis chaque pièce entre balises
    `<piece role="…" chemin="…" sha256="…">` … `</piece>` ; une pièce qui contient elle-même `</piece>` est refusée ;
 3. garde de motifs sur l'invite entière, telle qu'elle partirait : elle doit être vide avant tout envoi (voir
    `garde_motifs`) ; l'outil ne nettoie jamais : une pièce qui cite un motif interdit doit être remplacée par une copie
    nettoyée que l'appelant fournit ;
 4. refuse si DOSSIER/relecture-fable-api.md, DOSSIER/compteurs.json, le fichier de texte partiel ou l'un de leurs
    compagnons .sha256 existe déjà (on n'écrase jamais, R12) ;
 5. lit la clé dans la variable dont le NOM est donné (jamais affichée, jamais écrite ; masquée dans tout message) ;
 6. pire coût avant l'envoi : entrée comptée par l'interface de comptage d'Anthropic (`messages.count_tokens`, même
    modèle, même message, même réglage), garde = ⌈compte × 1,01⌉ + 32 ; si le comptage échoue, pour quelque raison
    que ce soit, refus (code 10) : rien n'est envoyé, aucune borne de repli (1,76 caractère par jeton mesuré à la
    fumée) ; sortie comptée au maximum demandé ; refus si le cumul du journal plus ce pire dépasse le plafond de la
    ligne ; une interruption (Ctrl-C, SIGTERM) pendant l'envoi est consignée au pire avant la sortie ;
 7. un seul appel en flux à `claude-fable-5-2`, effort donné par --effort (v3 ; défaut « high »), réflexion adaptative (seul réglage
    admis par ce modèle, `budget_tokens` y est refusé) à affichage « omitted » (le texte de la réflexion n'est ni demandé
    ni écrit), aucune relance automatique (`max_retries=0`), aucun repli serveur vers un autre modèle (`fallbacks` non
    envoyé : une relecture servie par un autre modèle ne serait pas celle de Fable) ;
 8. défauts, jamais une réponse : texte vide, arrêt en `max_tokens`, refus (`refusal`), toute autre raison d'arrêt que
    `end_turn`, modèle servi autre que celui demandé, erreur d'envoi ou flux coupé ; ligne de défaut au journal, code non
    nul ; le texte partiel éventuel est gardé à part, marqué « défaut, pas une relecture » (récupérer ce qui est
    récupérable) ;
 9. réponse saine : DOSSIER/relecture-fable-api.md (en-tête : modèle, heure, empreintes des entrées, jetons, coût) et son
    compagnon .sha256, DOSSIER/compteurs.json et son compagnon ; ligne au journal (JSON Lines).

Sources des réglages (compétence « claude-api » de Claude Code, chargée le 21 novembre 2026, table « Current Models »
mise en cache le 2026-11-03, et section « Claude Fable 5.2 ») :
- identifiant `claude-fable-5-2` ; 1M de contexte ; 128K de sortie au plus ; tarif 8 USD par million de jetons d'entrée,
  40 en sortie, lectures de cache 0,20 ; la réflexion est facturée comme sortie et compte dans `max_tokens` ;
- réflexion toujours active : `thinking` omis ou `{type: "adaptive"}` ; `disabled` et `budget_tokens` refusés (400) ;
  profondeur réglée par `output_config.effort`, de `low` à `xhigh` puis `max` ; affichage `omitted` par défaut ;
- `refusal` possible (HTTP 200, `stop_details.category`) ; la compétence recommande `fallbacks` par défaut : écarté ici,
  à dessein (voir le point 7) ;
- comptage : `client.messages.count_tokens(model=…, messages=…)` → `input_tokens` ;
- flux : `client.messages.stream(...)` puis `get_final_message()` ; `usage.output_tokens_details.thinking_tokens` donne
  les jetons de réflexion quand la réponse le porte ;
- espace de travail : paramètre `workspace_id` du kit d'Anthropic, « seulement pour une clé qui peut agir sur plusieurs
  espaces » ; envoyé seulement si --espace est donné.
Le catalogue du collisionneur (docs/notes/collisionneur-v9/collisionneur_v9_v8c.py, lignes 309-311) porte 10 / 50 ; la
compétence, plus récente pour ce modèle, porte 8 / 40 : c'est 8 / 40 qui est compté (ordre de la mère).

Limite déclarée : Fable 5.2 n'admet aucun budget de réflexion ; « au moins 32 000 jetons de texte au-delà de la
réflexion » n'est donc tenu que si la réflexion reste sous `max_tokens` − 32 000. Le défaut `max_tokens` est 128 000 (le
plafond du modèle) ; hors fumée, --max-sortie est refusé sous 64 000.
"""
from __future__ import annotations

import argparse
import dataclasses
import datetime as _dt
import hashlib
import json
import math
import os
import re
import signal
import sys
import threading
import unicodedata

VERSION = "relecture_fable_api_v4"
MODELE = "claude-fable-5-2"  # v4 : modèle par défaut (celui de la v3)
EFFORTS = ("low", "medium", "high", "xhigh", "max")  # v3 : niveaux admis par claude-fable-5-2 (compétence)
EFFORT_DEFAUT = "high"  # v3 : défaut du modèle et recommandation de la compétence pour ce modèle
REFLEXION = {"type": "adaptive", "display": "omitted"}
PRIX_ENTREE_USD_PAR_MJ = 8.0
PRIX_SORTIE_USD_PAR_MJ = 40.0
PRIX_LECTURE_CACHE_USD_PAR_MJ = 0.20
FACTEUR_ECRITURE_CACHE = 2.0  # prudent (écriture d'une heure) ; aucune mise en cache n'est demandée


@dataclasses.dataclass(frozen=True)
class Reglage:
    """v4 : réglages d'un modèle admis (sources dans la docstring du module)."""
    nom: str                 # nom en clair, pour l'en-tête
    efforts: tuple
    reflexion: dict
    affichage: str           # phrase de l'en-tête sur la réflexion
    prix_entree: float       # USD par million de jetons
    prix_sortie: float
    prix_lecture_cache: float
    max_sortie: int


MODELES = {
    MODELE: Reglage(nom="Claude Fable 5.2", efforts=EFFORTS, reflexion=REFLEXION,
                    affichage="réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit)",
                    prix_entree=PRIX_ENTREE_USD_PAR_MJ, prix_sortie=PRIX_SORTIE_USD_PAR_MJ,
                    prix_lecture_cache=PRIX_LECTURE_CACHE_USD_PAR_MJ, max_sortie=128000),
    "claude-opus-4-6": Reglage(nom="Claude Opus 4.6", efforts=("low", "medium", "high", "max"),
                               reflexion={"type": "adaptive"},
                               affichage="réflexion adaptative sans champ « display » (absent sur ce modèle ; le résumé "
                                         "de la réflexion revient, il n'est ni lu ni écrit)",
                               prix_entree=5.0, prix_sortie=25.0, prix_lecture_cache=0.50, max_sortie=128000),
}
MAX_SORTIE_MODELE = 128000
MAX_SORTIE_DEFAUT = 128000
MAX_SORTIE_MIN_RELECTURE = 64000
MAX_SORTIE_MIN_FUMEE = 1000
TEXTE_MIN_AU_DELA_REFLEXION = 32000
TOLERANCE_COMPTE = (0.01, 32)
DELAI_LECTURE_S = 3600.0
DELAI_CONNEXION_S = 30.0
URL_API = "https://api.anthropic.com"
NOM_RELECTURE = "relecture-fable-api.md"
NOM_COMPTEURS = "compteurs.json"
NOM_PARTIEL = "defaut-texte-partiel-PAS-UNE-RELECTURE.md"
MOTIF_NOM_VARIABLE = re.compile(r"^[A-Z_][A-Z0-9_]{0,99}$")

# Codes de sortie
OK = 0
CODE_USAGE = 2
CODE_PIECE = 3
CODE_GARDE = 4
CODE_PLAFOND = 5
CODE_CLE = 6
CODE_DEFAUT = 7
CODE_ENVOI = 8
CODE_EXISTE = 9
CODE_COMPTAGE = 10

# ---------- garde de motifs ----------

NOMS_INTERDITS = ("lazar", "ciric")  # comparés sans casse ni accent (« Ćirić » → « ciric »)
MOTIF_SESSION = re.compile(r"session[_\-][0-9A-Za-z]{20,}", re.IGNORECASE)
MOTIF_UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.IGNORECASE)
MOTIF_COURRIEL = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}")
# Termes refusés partout (sans casse ni accent ; séparateurs « - », « _ » ou espace admis entre les mots)
TERMES_PARTOUT = {
    "consigne-privee": re.compile(r"consigne[\s_\-]*privee"),
    "conception-ii-b": re.compile(r"conception[\s_\-.()]*ii[\s_\-.()]*b"),
    "donnees/": re.compile(r"donnees\s*[/\\]"),
}
# Termes refusés dans un chemin ou un nom : jeton qui contient « / », « \ », « _ », « - » ou finit par une extension,
# ou texte entre accents graves (`…`). Le mot seul dans la prose (« le rendu », « les scores ») n'est pas refusé.
TERMES_DE_CHEMIN = ("verite", "rendu", "scores")
JETON = re.compile(r"[a-z0-9_./\\\-]+")
EXTENSION = re.compile(r"\.[a-z0-9]{1,8}$")
CODE_EN_LIGNE = re.compile(r"`([^`\n]+)`")


def sans_accents(texte: str) -> str:
    decompose = unicodedata.normalize("NFKD", texte)
    return "".join(c for c in decompose if not unicodedata.combining(c)).lower()


def _jeton_de_chemin(jeton: str) -> bool:
    return any(s in jeton for s in "/\\_-") or bool(EXTENSION.search(jeton))


def garde_motifs_ligne(ligne: str) -> list[str]:
    """Motifs interdits trouvés dans une ligne (noms des motifs, jamais le texte trouvé)."""
    trouves = []
    ligne = "".join(c for c in ligne if unicodedata.category(c) != "Cf")  # caractères invisibles (U+200B…) retirés
    if MOTIF_SESSION.search(ligne):
        trouves.append("identifiant de session")
    if MOTIF_UUID.search(ligne):
        trouves.append("identifiant de session (UUID)")
    if MOTIF_COURRIEL.search(ligne):
        trouves.append("adresse de courriel")
    norm = sans_accents(ligne)
    for nom in NOMS_INTERDITS:
        if nom in norm:
            trouves.append(f"nom de personne interdit « {nom} »")
    for terme, motif in TERMES_PARTOUT.items():
        if motif.search(norm):
            trouves.append(f"terme interdit « {terme} »")
    jetons = [j for j in JETON.findall(norm) if _jeton_de_chemin(j)]
    codes = CODE_EN_LIGNE.findall(norm)
    for terme in TERMES_DE_CHEMIN:
        if any(terme in j for j in jetons) or any(terme in c for c in codes):
            trouves.append(f"terme « {terme} » dans un chemin ou un nom")
    return trouves


def garde_motifs(segments: list[tuple[str, str]]) -> list[dict]:
    """Garde sur l'invite entière, découpée en segments (étiquette, texte) dont la réunion est l'invite exacte.
    Rend la liste des motifs trouvés, avec le segment et le numéro de ligne dans le segment ; vide = l'envoi est permis."""
    trouves = []
    for etiquette, texte in segments:
        for i, ligne in enumerate(texte.split("\n"), start=1):
            for motif in garde_motifs_ligne(ligne):
                trouves.append({"motif": motif, "segment": etiquette, "ligne": i})
    # Motifs à cheval sur deux segments : contrôle de l'invite jointe aussi (aucun ne doit apparaître de plus).
    invite = "".join(t for _, t in segments)
    lignes_jointes = sum(len(garde_motifs_ligne(l)) for l in invite.split("\n"))
    if lignes_jointes > len(trouves):
        trouves.append({"motif": "motif à cheval sur deux segments", "segment": "invite", "ligne": 0})
    return trouves


# ---------- erreurs et structures ----------

class Refus(Exception):
    """Refus avant l'envoi : rien ne part."""

    def __init__(self, code: int, message: str, details: dict | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details or {}


class CleRefusee(Exception):
    pass


class ComptageImpossible(Exception):
    pass


@dataclasses.dataclass
class Resultat:
    """Ce que rend un envoi. `base_cout` : « usage » (usage lu), « pire » (envoi parti sans usage sûr), « zero » (refusé
    avant tout traitement : 4xx, connexion impossible)."""
    envoye: bool
    texte: str = ""
    raison_arret: str | None = None
    categorie_refus: str | None = None
    modele_servi: str | None = None
    identifiant: str | None = None
    identifiant_requete: str | None = None
    usage: dict | None = None
    erreur: str | None = None
    base_cout: str = "usage"
    cle_refusee: bool = False


@dataclasses.dataclass
class Entree:
    role: str
    chemin: str        # chemin affiché (relatif au dossier courant s'il y est)
    texte: str
    sha256: str
    compagnon: str     # « vérifié » ou « absent »
    caracteres: int


# ---------- lecture des entrées ----------

def empreinte_octets(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def chemin_affiche(chemin: str) -> str:
    absolu = os.path.abspath(chemin)
    courant = os.path.abspath(os.getcwd())
    if absolu == courant or absolu.startswith(courant + os.sep):
        return os.path.relpath(absolu, courant)
    return absolu


def lire_compagnon(chemin: str) -> str | None:
    """Empreinte portée par `chemin.sha256`, ou None s'il n'existe pas. Mal formé : Refus."""
    compagnon = chemin + ".sha256"
    if not os.path.exists(compagnon):
        return None
    with open(compagnon, "r", encoding="utf-8") as f:
        lignes = [l.strip() for l in f.read().splitlines() if l.strip()]
    base = os.path.basename(chemin)
    candidates = []
    for l in lignes:
        m = re.match(r"^([0-9a-f]{64})\s+\*?(.+)$", l)
        if not m:
            raise Refus(CODE_PIECE, f"compagnon mal formé : {chemin_affiche(compagnon)}")
        if os.path.basename(m.group(2).strip()) == base:
            candidates.append(m.group(1))
    if len(lignes) == 1 and not candidates:
        m = re.match(r"^([0-9a-f]{64})\b", lignes[0])
        candidates = [m.group(1)] if m else []
    if len(set(candidates)) != 1:
        raise Refus(CODE_PIECE, f"compagnon sans ligne unique pour {base} : {chemin_affiche(compagnon)}")
    return candidates[0]


def lire_entree(role: str, chemin: str) -> Entree:
    if not os.path.isfile(chemin):
        raise Refus(CODE_PIECE, f"pièce absente ({role}) : {chemin_affiche(chemin)}",
                    {"role": role, "chemin": chemin_affiche(chemin)})
    with open(chemin, "rb") as f:
        octets = f.read()
    h = empreinte_octets(octets)
    attendue = lire_compagnon(chemin)
    if attendue is not None and attendue != h:
        raise Refus(CODE_PIECE, f"empreinte inégale à son compagnon ({role}) : {chemin_affiche(chemin)} "
                                f"(fichier {h[:12]}…, compagnon {attendue[:12]}…)",
                    {"role": role, "chemin": chemin_affiche(chemin), "sha256": h, "compagnon_sha256": attendue})
    try:
        texte = octets.decode("utf-8")
    except UnicodeDecodeError:
        raise Refus(CODE_PIECE, f"pièce non UTF-8 ({role}) : {chemin_affiche(chemin)}")
    return Entree(role=role, chemin=chemin_affiche(chemin), texte=texte, sha256=h,
                  compagnon="vérifié" if attendue is not None else "absent", caracteres=len(texte))


def composer_invite(consigne: Entree, pieces: list[Entree]) -> list[tuple[str, str]]:
    """Segments (étiquette, texte) ; leur réunion est l'invite exacte."""
    segments = [(f"consigne {consigne.chemin}", consigne.texte.rstrip("\n") + "\n\n")]
    for p in pieces:
        if "</piece>" in p.texte:
            raise Refus(CODE_PIECE, f"la pièce contient elle-même « </piece> » : {p.chemin}")
        for c in ('"', "<", ">"):
            if c in p.chemin:
                raise Refus(CODE_PIECE, f"chemin de pièce inadmissible dans une balise : {p.chemin}")
        ouverture = f'<piece role="{p.role}" chemin="{p.chemin}" sha256="{p.sha256}">\n'
        segments.append((f"balise de {p.chemin}", ouverture))
        segments.append((f"pièce {p.chemin}", p.texte.rstrip("\n") + "\n"))
        segments.append((f"fin de {p.chemin}", "</piece>\n\n"))
    return segments


# ---------- journal de dépense ----------

def heure_utc() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def cumul_journal(chemin: str) -> float:
    """Somme des coûts comptés du journal. Absent : 0 (le dossier parent doit exister). Ligne illisible : Refus."""
    parent = os.path.dirname(os.path.abspath(chemin))
    if not os.path.isdir(parent):
        raise Refus(CODE_PLAFOND, f"dossier du journal de dépense absent : {chemin_affiche(parent)}")
    if not os.path.exists(chemin):
        return 0.0
    total = 0.0
    with open(chemin, "r", encoding="utf-8") as f:
        for n, ligne in enumerate(f, start=1):
            if not ligne.strip():
                continue
            try:
                objet = json.loads(ligne)
                cout = objet["cout_compte_usd"]
            except (ValueError, KeyError, TypeError):
                raise Refus(CODE_PLAFOND, f"journal de dépense illisible, ligne {n} : {chemin_affiche(chemin)}")
            if not isinstance(cout, (int, float)) or isinstance(cout, bool) or cout < 0 or math.isnan(cout):
                raise Refus(CODE_PLAFOND, f"coût mal formé au journal, ligne {n} : {chemin_affiche(chemin)}")
            total += float(cout)
    return total


def ecrire_journal(chemin: str, ligne: dict) -> None:
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(json.dumps(ligne, ensure_ascii=False, sort_keys=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


# ---------- coûts ----------

def garde_entree(compte: int) -> int:
    """⌈compte × 1,01⌉ + 32, en arithmétique entière (pas d'erreur d'arrondi flottant)."""
    return -(-compte * 101 // 100) + TOLERANCE_COMPTE[1]


def pire_cout(entree: int, max_sortie: int, modele: str = MODELE) -> float:
    r = MODELES[modele]
    return (entree * r.prix_entree + max_sortie * r.prix_sortie) / 1e6


def cout_usage(usage: dict, modele: str = MODELE) -> float:
    r = MODELES[modele]
    return (usage.get("entree", 0) * r.prix_entree
            + usage.get("ecriture_cache", 0) * r.prix_entree * FACTEUR_ECRITURE_CACHE
            + usage.get("lecture_cache", 0) * r.prix_lecture_cache
            + usage.get("sortie", 0) * r.prix_sortie) / 1e6


# ---------- transport réel (kit d'Anthropic) ----------

def client_reel(cle: str, base_url: str | None = None):
    """Client du kit d'Anthropic : clé explicite (les variables d'identité de l'environnement ne sont pas lues), aucune
    relance (max_retries=0), délai de lecture d'une heure entre deux morceaux du flux, sans traces. Adresse locale (essais
    seulement) : sans mandataire de l'environnement."""
    import anthropic
    kwargs = dict(api_key=cle, max_retries=0, base_url=base_url or URL_API, open_telemetry=False,
                  timeout=anthropic.Timeout(DELAI_LECTURE_S, connect=DELAI_CONNEXION_S))
    if base_url and re.match(r"^http://(127\.0\.0\.1|localhost)(:\d+)?/?$", base_url):
        kwargs["http_client"] = anthropic.DefaultHttpxClient(trust_env=False)
    return anthropic.Anthropic(**kwargs)


def masquer(texte, cle: str | None) -> str:
    texte = str(texte)
    return texte.replace(cle, "[clé]") if cle else texte


def compter_par_sdk(client, params: dict, cle: str | None = None) -> int:
    import anthropic
    corps = {k: params[k] for k in ("model", "messages", "thinking", "output_config", "workspace_id") if k in params}
    try:
        rep = client.messages.count_tokens(**corps)
    except (anthropic.AuthenticationError, anthropic.PermissionDeniedError) as e:
        raise CleRefusee(masquer(f"HTTP {e.status_code} au comptage : {e.message}", cle)[:400])
    except anthropic.APIError as e:
        raise ComptageImpossible(masquer(f"{type(e).__name__} : {e}", cle)[:400])
    n = getattr(rep, "input_tokens", None)
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ComptageImpossible(f"compte invraisemblable : {n!r}")
    return n


def _usage_de(message) -> dict | None:
    u = getattr(message, "usage", None)
    if u is None:
        return None
    details = getattr(u, "output_tokens_details", None)
    return {"entree": u.input_tokens or 0, "sortie": u.output_tokens or 0,
            "reflexion": getattr(details, "thinking_tokens", None) if details is not None else None,
            "ecriture_cache": getattr(u, "cache_creation_input_tokens", None) or 0,
            "lecture_cache": getattr(u, "cache_read_input_tokens", None) or 0}


def _texte_de(message) -> str:
    return "".join(b.text for b in (getattr(message, "content", None) or []) if getattr(b, "type", None) == "text")


def envoyer_par_sdk(client, params: dict, cle: str | None = None) -> Resultat:
    """Un seul envoi en flux. Jamais de relance. Le texte de la réflexion n'est jamais lu."""
    import anthropic
    import httpx2
    etape, flux = "ouverture", None
    try:
        with client.messages.stream(**params) as flux:
            etape = "flux"
            for _evenement in flux:
                pass
            message = flux.get_final_message()
    except (anthropic.AuthenticationError, anthropic.PermissionDeniedError) as e:
        return Resultat(envoye=False, erreur=masquer(f"clé refusée : HTTP {e.status_code} : {e.message}", cle)[:400],
                        base_cout="zero", cle_refusee=True)
    except anthropic.APIStatusError as e:
        base = "pire" if (e.status_code >= 500 or etape == "flux") else "zero"
        return Resultat(envoye=base == "pire", erreur=masquer(f"HTTP {e.status_code} ({etape}) : {e.message}",
                                                               cle)[:400], base_cout=base,
                        texte=_texte_partiel(flux))
    except anthropic.APIConnectionError as e:
        impossible = etape == "ouverture" and isinstance(e.__cause__, httpx2.ConnectError)
        base = "zero" if impossible else "pire"
        return Resultat(envoye=not impossible, erreur=masquer(f"{type(e).__name__} ({etape}) : {e.__cause__ or e}",
                                                              cle)[:400], base_cout=base, texte=_texte_partiel(flux))
    except Exception as e:  # coupure, flux illisible : l'envoi est parti, compté au pire
        return Resultat(envoye=etape == "flux", erreur=masquer(f"{type(e).__name__} ({etape}) : {e}", cle)[:400],
                        base_cout="pire" if etape == "flux" else "zero", texte=_texte_partiel(flux))
    details = getattr(message, "stop_details", None)
    return Resultat(envoye=True, texte=_texte_de(message), raison_arret=message.stop_reason,
                    categorie_refus=getattr(details, "category", None) if details is not None else None,
                    modele_servi=message.model, identifiant=message.id,
                    identifiant_requete=getattr(flux, "request_id", None) if flux is not None else None,
                    usage=_usage_de(message), base_cout="usage")


def _texte_partiel(flux) -> str:
    try:
        return _texte_de(flux.current_message_snapshot) if flux is not None else ""
    except Exception:
        return ""


# ---------- écriture des sorties ----------

def _sigterm_en_interruption(signum, frame):
    raise KeyboardInterrupt(f"signal {signum} pendant l'envoi")


def sceller(chemin: str) -> str:
    with open(chemin, "rb") as f:
        h = empreinte_octets(f.read())
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {os.path.basename(chemin)}\n")
    return h


def ecrire_neuf(chemin: str, texte: str) -> str:
    with open(chemin, "x", encoding="utf-8") as f:
        f.write(texte)
    return sceller(chemin)


def empreinte_module() -> str:
    with open(os.path.abspath(__file__), "rb") as f:
        return empreinte_octets(f.read())


def entete(titre: str, ligne: dict, entrees: list[Entree]) -> str:
    u = ligne.get("jetons") or {}
    r = MODELES[ligne["modele"]]  # v4 : modèle demandé
    l = [f"# {titre}", "",
         f"- Outil : `controle_ia.{VERSION}` (empreinte du module {ligne['empreinte_outil']})",
         f"- Modèle demandé : `{ligne['modele']}` ; modèle servi : `{ligne.get('modele_servi')}` ; identifiant du message : "
         f"`{ligne.get('identifiant_message')}`",
         f"- Heure (UTC) : {ligne['heure_utc']}",
         f"- Réglages : effort `{ligne['effort']}`, {r.affichage}, "
         f"`max_tokens` {ligne['max_tokens']}, aucune relance, aucun repli vers un autre modèle"
         + (" ; APPEL DE FUMÉE, ce n'est pas une relecture" if ligne.get("fumee") else ""),
         "- Entrées :"]
    for e in entrees:
        l.append(f"  - {e.role} : `{e.chemin}` — sha256 {e.sha256} (compagnon : {e.compagnon})")
    l += [f"- Empreinte de l'invite envoyée : {ligne['sha256_invite']}",
          f"- Jetons : entrée {u.get('entree')}, sortie {u.get('sortie')} (dont réflexion {u.get('reflexion')}), "
          f"écriture de cache {u.get('ecriture_cache')}, lecture de cache {u.get('lecture_cache')} ; raison d'arrêt "
          f"`{ligne.get('raison_arret')}`",
          f"- Coût compté : {ligne['cout_compte_usd']:.6f} USD (base : {ligne['base_cout']} ; tarif {r.prix_entree:g}"
          f" / {r.prix_sortie:g} USD par million de jetons d'entrée / de sortie)",
          "", "---", ""]
    return "\n".join(l)


# ---------- commande ----------

def _ligne_base(args, entrees: list[Entree], max_sortie: int) -> dict:
    modele = getattr(args, "modele", None)  # v4 : modèle demandé ; hors liste, consigné tel quel, sans réglage
    reflexion = dict(MODELES[modele].reflexion) if isinstance(modele, str) and modele in MODELES else None
    return {"heure_utc": heure_utc(), "outil": VERSION, "empreinte_outil": empreinte_module(), "modele": modele,
            "effort": args.effort, "reflexion": reflexion, "max_tokens": max_sortie, "fumee": bool(args.fumee),
            "plafond_ligne_usd": args.plafond_ligne,
            "entrees": [{"role": e.role, "chemin": e.chemin, "sha256": e.sha256, "compagnon": e.compagnon}
                        for e in entrees],
            "envoye": False, "statut": None, "defaut": None, "cout_compte_usd": 0.0, "base_cout": "aucun envoi"}


def relire(args, envoyeur=None, compteur=None, environ=None, base_url=None) -> int:
    """Corps de la commande `relire`. `envoyeur(params) -> Resultat` et `compteur(params) -> int` remplacent le transport
    réel dans les essais ; `environ` remplace os.environ ; `base_url` (essais) remplace l'adresse de l'interface."""
    environ = os.environ if environ is None else environ
    journal = args.journal_depense
    entrees: list[Entree] = []
    max_sortie = args.max_sortie
    ligne: dict | None = None
    cle = None

    def refuser(r: Refus) -> int:
        nonlocal ligne
        if ligne is None:
            ligne = _ligne_base(args, entrees, max_sortie)
        ligne.update({"statut": "refus_avant_envoi", "defaut": r.message, "details": r.details})
        try:
            if journal and os.path.isdir(os.path.dirname(os.path.abspath(journal))):
                ecrire_journal(journal, ligne)
        except OSError as e:
            print(f"AVERTISSEMENT : refus non consigné au journal ({type(e).__name__})", file=sys.stderr)
        print(f"REFUS (rien n'est envoyé) : {masquer(r.message, cle)}", file=sys.stderr)
        return r.code

    try:
        # arguments
        if not (isinstance(args.plafond_ligne, float) and args.plafond_ligne > 0 and math.isfinite(args.plafond_ligne)):
            raise Refus(CODE_USAGE, "--plafond-ligne doit être un nombre positif (USD)")
        for nom in [args.cle] + ([args.espace] if args.espace else []):
            if not MOTIF_NOM_VARIABLE.match(nom or ""):
                raise Refus(CODE_USAGE, "nom de variable d'environnement mal formé (majuscules, chiffres, « _ »)")
        minimum = MAX_SORTIE_MIN_FUMEE if args.fumee else MAX_SORTIE_MIN_RELECTURE
        if not (minimum <= max_sortie <= MAX_SORTIE_MODELE):
            raise Refus(CODE_USAGE, f"--max-sortie hors de [{minimum}, {MAX_SORTIE_MODELE}]"
                                    + ("" if args.fumee else " (hors fumée)"))
        if args.effort not in EFFORTS:  # v3 : valeurs fermées, contrôlées aussi hors de l'analyseur
            raise Refus(CODE_USAGE, f"--effort hors de {list(EFFORTS)}")
        modele = getattr(args, "modele", None)  # v4 : valeurs fermées, contrôlées aussi hors de l'analyseur
        if not isinstance(modele, str) or modele not in MODELES:
            raise Refus(CODE_USAGE, f"--modele hors de {list(MODELES)}")
        reglage = MODELES[modele]
        if args.effort not in reglage.efforts:  # v4 : effort non admis par le modèle choisi
            raise Refus(CODE_USAGE, f"--effort {args.effort} non admis par {modele} (admis : {list(reglage.efforts)})")
        if max_sortie > reglage.max_sortie:
            raise Refus(CODE_USAGE, f"--max-sortie au-delà du plafond de {modele} ({reglage.max_sortie})")
        if not args.piece:
            raise Refus(CODE_USAGE, "au moins une --piece")
        if not args.remarques:
            raise Refus(CODE_USAGE, "au moins un --remarques")
        # 1. entrées
        consigne = lire_entree("consigne", args.consigne)
        entrees.append(consigne)
        pieces = []
        for role, liste in (("correction", args.piece), ("remarques", args.remarques), ("avant", args.avant or [])):
            for chemin in liste:
                e = lire_entree(role, chemin)
                entrees.append(e)
                pieces.append(e)
        # 2. invite ; 3. garde de motifs
        segments = composer_invite(consigne, pieces)
        trouves = garde_motifs(segments)
        if trouves:
            raise Refus(CODE_GARDE, "garde de motifs non vide : " + " ; ".join(
                f"{t['motif']} ({t['segment']}, ligne {t['ligne']})" for t in trouves), {"motifs": trouves})
        invite = "".join(t for _, t in segments)
        sha_invite = empreinte_octets(invite.encode("utf-8"))
        # 4. sorties neuves
        if os.path.exists(args.sortie) and not os.path.isdir(args.sortie):
            raise Refus(CODE_USAGE, f"--sortie n'est pas un dossier : {chemin_affiche(args.sortie)}")
        for nom in [n + s for n in (NOM_RELECTURE, NOM_COMPTEURS, NOM_PARTIEL) for s in ("", ".sha256")]:
            if os.path.lexists(os.path.join(args.sortie, nom)):
                raise Refus(CODE_EXISTE, f"sortie déjà présente, jamais écrasée : "
                                         f"{chemin_affiche(os.path.join(args.sortie, nom))}")
        # 5. clé et espace
        cle = environ.get(args.cle) or None
        if not cle:
            raise Refus(CODE_CLE, f"clé absente : la variable nommée {args.cle} est vide ou absente")
        espace = None
        if args.espace:
            espace = environ.get(args.espace) or None
            if not espace:
                raise Refus(CODE_CLE, f"espace demandé absent : la variable nommée {args.espace} est vide ou absente")
        # 6. pire coût et plafond
        cumul = cumul_journal(journal)
        params = {"model": modele, "max_tokens": max_sortie, "thinking": dict(reglage.reflexion),
                  "output_config": {"effort": args.effort}, "messages": [{"role": "user", "content": invite}]}
        if espace:
            params["workspace_id"] = espace
        client = None
        if envoyeur is None or compteur is None:
            client = client_reel(cle, base_url)
        compter = compteur or (lambda p: compter_par_sdk(client, p, cle))
        envoyer = envoyeur or (lambda p: envoyer_par_sdk(client, p, cle))
        try:
            compte = compter(params)
        except CleRefusee as e:
            raise Refus(CODE_ENVOI, f"clé refusée au comptage, rien n'est envoyé : {masquer(e, cle)}")
        except Exception as e:  # ComptageImpossible ou imprévu : aucune borne de repli, rien n'est envoyé
            raise Refus(CODE_COMPTAGE, "comptage de l'entrée impossible, rien n'est envoyé : "
                                       + masquer(f"{type(e).__name__} : {e}", cle)[:300])
        entree_garde, source = garde_entree(compte), "count_tokens d'Anthropic, garde ⌈n × 1,01⌉ + 32"
        pire = pire_cout(entree_garde, max_sortie, modele)
        ligne = _ligne_base(args, entrees, max_sortie)
        ligne.update({"sha256_invite": sha_invite, "caracteres_invite": len(invite), "entree_comptee": compte,
                      "entree_garde": entree_garde, "source_entree": source, "pire_usd": round(pire, 6),
                      "cumul_avant_usd": round(cumul, 6)})
        if cumul + pire > args.plafond_ligne:
            raise Refus(CODE_PLAFOND, f"plafond de ligne dépassé : cumul {cumul:.6f} + pire {pire:.6f} > "
                                      f"{args.plafond_ligne:.6f} USD")
    except Refus as r:
        return refuser(r)

    # 7. un seul envoi
    os.makedirs(args.sortie, exist_ok=True)
    principal = threading.current_thread() is threading.main_thread()
    sigterm_avant = signal.signal(signal.SIGTERM, _sigterm_en_interruption) if principal else None
    try:
        res = envoyer(params)
    except Exception as e:  # imprévu : on ne sait pas si l'envoi est parti, compté au pire
        res = Resultat(envoye=True, erreur=masquer(f"imprévu : {type(e).__name__} : {e}", cle)[:400], base_cout="pire")
    except BaseException as e:  # interruption (Ctrl-C, SIGTERM) pendant l'envoi : comptée au pire, consignée, puis on sort
        ligne.update({"heure_utc": heure_utc(), "envoye": True, "statut": "defaut",
                      "defaut": f"interruption pendant l'envoi : {type(e).__name__}", "base_cout": "pire",
                      "cout_compte_usd": round(pire, 6)})
        ecrire_journal(journal, ligne)
        raise
    finally:
        if principal:
            signal.signal(signal.SIGTERM, sigterm_avant)
    ligne["heure_utc"] = heure_utc()
    ligne.update({"envoye": res.envoye, "modele_servi": res.modele_servi, "identifiant_message": res.identifiant,
                  "identifiant_requete": res.identifiant_requete, "raison_arret": res.raison_arret,
                  "categorie_refus": res.categorie_refus, "jetons": res.usage, "base_cout": res.base_cout})
    if res.base_cout == "usage" and res.usage is not None:
        cout = cout_usage(res.usage, modele)
        if res.usage.get("entree", 0) > entree_garde:
            ligne["entree_au_dela_de_la_garde"] = True
    elif res.base_cout == "zero":
        cout = 0.0
    else:
        cout, ligne["base_cout"] = pire, "pire"
    ligne["cout_compte_usd"] = round(cout, 6)

    # 8. défauts
    defaut = None
    if res.erreur:
        defaut = ("clé refusée : " if res.cle_refusee else "erreur d'envoi : ") + masquer(res.erreur, cle)
    elif res.usage is None:
        defaut, ligne["base_cout"], ligne["cout_compte_usd"] = "usage absent de la réponse", "pire", round(pire, 6)
    elif res.raison_arret == "max_tokens":
        defaut = "arrêt en max_tokens"
    elif res.raison_arret == "refusal":
        defaut = f"refus du modèle (catégorie {res.categorie_refus})"
    elif res.raison_arret != "end_turn":
        defaut = f"raison d'arrêt inattendue : {res.raison_arret}"
    elif res.modele_servi != modele:
        defaut = f"modèle servi autre que celui demandé : {res.modele_servi}"
    elif not res.texte.strip():
        defaut = "texte vide"
    compteurs = {k: ligne.get(k) for k in ("heure_utc", "modele", "modele_servi", "identifiant_message", "effort",
                                           "max_tokens", "fumee", "raison_arret", "categorie_refus", "jetons",
                                           "entree_comptee", "entree_garde", "source_entree", "pire_usd",
                                           "cout_compte_usd", "base_cout", "sha256_invite")}
    if defaut:
        ligne.update({"statut": "defaut", "defaut": defaut})
        compteurs.update({"statut": "defaut", "defaut": defaut})
        ecrire_journal(journal, ligne)
        ecrire_neuf(os.path.join(args.sortie, NOM_COMPTEURS),
                    json.dumps(compteurs, ensure_ascii=False, indent=2) + "\n")
        if res.texte:
            ecrire_neuf(os.path.join(args.sortie, NOM_PARTIEL),
                        entete("DÉFAUT — texte partiel gardé, ce n'est PAS une relecture", ligne, entrees)
                        + f"Défaut : {defaut}\n\n" + res.texte + "\n")
        print(f"DÉFAUT (pas une réponse) : {defaut} ; coût compté {ligne['cout_compte_usd']:.6f} USD "
              f"({ligne['base_cout']})", file=sys.stderr)
        return CODE_ENVOI if res.erreur else CODE_DEFAUT

    # 9. réponse saine
    ligne.update({"statut": "reponse"})
    compteurs["statut"] = "reponse"
    titre = f"Appel de fumée à {reglage.nom} (interface d'Anthropic) — pas une relecture" if args.fumee else \
        f"Relecture par {reglage.nom} (appel direct à l'interface d'Anthropic)"
    contenu = entete(titre, ligne, entrees) + res.texte + "\n"
    h_rel = empreinte_octets(contenu.encode("utf-8"))
    ligne["sha256_relecture"] = compteurs["sha256_relecture"] = h_rel
    ecrire_journal(journal, ligne)  # la dépense est consignée avant toute écriture de sortie
    if ecrire_neuf(os.path.join(args.sortie, NOM_RELECTURE), contenu) != h_rel:
        print("DÉFAUT : empreinte de la relecture écrite inégale à celle du journal", file=sys.stderr)
        return CODE_DEFAUT
    ecrire_neuf(os.path.join(args.sortie, NOM_COMPTEURS), json.dumps(compteurs, ensure_ascii=False, indent=2) + "\n")
    u = res.usage
    print(f"RÉPONSE : {chemin_affiche(os.path.join(args.sortie, NOM_RELECTURE))} (sha256 {h_rel}) ; jetons entrée "
          f"{u['entree']}, sortie {u['sortie']} (réflexion {u['reflexion']}) ; coût {ligne['cout_compte_usd']:.6f} USD")
    return OK


def analyseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python -m controle_ia.relecture_fable_api_v4",
                                description="Relecture d'une correction par Claude Fable 5.2 (ou Claude Opus 4.6), par "
                                            "l'interface d'Anthropic.")
    sous = p.add_subparsers(dest="commande", required=True)
    r = sous.add_parser("relire")
    r.add_argument("--piece", action="append", default=[], help="pièce corrigée (répétable)")
    r.add_argument("--remarques", action="append", default=[], help="remarques déjà reçues (répétable)")
    r.add_argument("--avant", action="append", default=[], help="version précédente (facultative, répétable)")
    r.add_argument("--consigne", required=True, help="consigne de relecture")
    r.add_argument("--sortie", required=True, help="dossier de sortie")
    r.add_argument("--cle", required=True, help="NOM de la variable d'environnement qui porte la clé d'Anthropic")
    r.add_argument("--espace", help="NOM de la variable qui porte l'identifiant d'espace de travail (facultatif)")
    r.add_argument("--plafond-ligne", required=True, type=float, help="plafond de la ligne de dépense, USD")
    r.add_argument("--journal-depense", required=True, help="journal de dépense (JSON Lines)")
    r.add_argument("--max-sortie", type=int, default=MAX_SORTIE_DEFAUT, help="max_tokens (défaut 128 000)")
    r.add_argument("--fumee", action="store_true", help="appel de fumée : --max-sortie admis dès 1 000, marqué partout")
    r.add_argument("--effort", choices=EFFORTS, default=EFFORT_DEFAUT,
                   help="effort (v3 ; défaut high ; aucune borne de la réflexion n'est offerte ; xhigh : "
                        "claude-fable-5-2 seulement)")
    r.add_argument("--modele", choices=tuple(MODELES), default=MODELE,
                   help="modèle demandé (v4 ; défaut claude-fable-5-2)")
    return p


def main(argv=None) -> int:
    args = analyseur().parse_args(argv)
    if args.commande == "relire":
        return relire(args)
    return CODE_USAGE


if __name__ == "__main__":
    sys.exit(main())
