#!/usr/bin/env python3
"""Générateur des témoins plantés, garde de recouvrement, partage et audit du générateur — ligne 3 de l'organisme v9
(votes effectifs des juges croisés), étage 2 à 200 témoins — v3.

Version 3 (même développeur, règle R12 ; la v2, `generer_temoins_ligne_3_v2.py`, a3a4e82f…, est gardée sans modification) :
décisions de la mère (15:20Z), rien d'autre. (1) `creer-journal-rejeux` refuse aussi si l'historique git du dépôt connaît
déjà le manifeste de création (`git log --all -- CHEMIN`, lecture seule, aucun réseau ; historique illisible : refus).
(2) Seule la forme réelle du fichier des cartes reste : {identifiant de treize caractères : {contenu, empreinte, meta}} ; les
sept cartes du repli se trouvent par égalité exacte. (3) La pièce du (4) porte une ligne de portée (« Portée : garde
entière » ou « Portée : repli seul »), confrontée à `--repli`. (4) `creer-journal-rejeux` sur un journal existant sans
manifeste : refus nommé, sans trace brute. (5) Pièce du (4) : octets lus une fois, empreinte vérifiée sur ces octets,
analyse de ces mêmes octets.

Texte de la v2 :

Version 2 (même développeur, règle R12 ; la v1, `generer_temoins_ligne_3_v1.py`, b264760c…, est gardée sans modification) :
corrections du contrôle de la condition (4) v1 (934d6bce…, « non conforme ») et de la contre-lecture v1 (d3b72675…),
ajouts de la mère (15:05Z). (1) Journal des rejeux et manifeste de sa création en CONSTANTES (`JOURNAL_REJEUX`,
`MANIFESTE_JOURNAL_REJEUX`) ; aucun chemin libre ; création refusée si ce manifeste existe ; la garde exige ce manifeste,
scellé, qui nomme ce journal. (2) La pièce du contrôle (4) doit porter une ligne de verdict « Conforme » (et aucune « Non
conforme ») et l'empreinte de ce programme ; sinon refus avant l'ouverture. (3) `meta` retiré à toute profondeur, niveau du
fichier compris. (4) Ligne de commande de la garde entièrement sous `try` : aucune trace brute ; arguments hors liste
refusés. (5) Forme réelle du fichier des cartes (contre-lecture, § 3) : objet {identifiant de treize caractères : {contenu,
empreinte, meta}} ; admise. (6) Fautif de `modules` d'un autre item que `module_nomme` : nomme un module (C1). (7) Deux
contenus identiques dans la banque : refus nommé ; nombre maximal de fragments communs entre deux témoins rapporté (M5).
(8) Constructeurs d'entrée non « production » : garde des chemins (R3). Le clone de l'organisme est présent à
`/home/user/lciric/ideation-organism` (commit a41b7b50…) : la voie réelle de l'audit s'y exerce sans réseau ni clé (M6).

Plan de code : annexe A du texte v7 (`preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, 4e3680d9…), ligne 560 ;
banque, écriture, vérification, garde de recouvrement et ses conditions (1) à (5), repli, partage, audit : lignes 251 à
266 ; liste d'arrêt (l. 352 et suivantes) ; Q3 (l. 76) ; en-tête (les sept cartes nommées du repli, l. 30). Portée à 200
par l'additif 3 v3 (71b7a876…, § 4.2) : 100 bons (50 simples, 50 à piège ; 50 citants) ; 100 mauvais (20 par item : 4
déclarés, 8 nets, 8 discrets ; 50 citants, 10 par item) ; contrôle des traits de la lettre à 100 bons contre 80 mauvais.
Décision de la mère R-4246 : les fragments sont un fichier de données à part, scellé avec la banque, jamais une constante
du code. Écrit par le développeur, modèle O. Jamais lancé par l'auteur sur le fichier des cartes.

Ce que fait ce programme, et rien d'autre :
- `composer` : lit un fichier de fragments (format au rapport du développeur, schéma vérifié au chargement), compose les
  200 témoins aux proportions de l'additif 3, longueurs de 1 200 à 2 800 caractères entrelacées entre les classes (huit
  bandes de 200 caractères, réparties à égalité dans chaque classe), citation équilibrée ; écrit la banque (format lu par
  le code d'appel v4, `valider_banque`), le journal de construction (la vérité : classe, item, niveau, citation, piège,
  fragments employés par identifiant) et le partage stratifié (moitié « lecture », moitié « étalonnage ») ;
- `creer-journal-rejeux` : crée vide le journal à ajout seul des rejeux de la garde, par un geste écrit à son manifeste ;
- `garde` : garde de recouvrement, à la lettre des conditions (1) à (5) et du repli ; seule entrée du côté des cartes :
  le fichier des cartes, chemin et empreinte en constantes (`CHEMIN_CARTES`, `EMPREINTE_CARTES`), compte de 94 vérifié
  avant toute comparaison ; champ `meta` retiré au chargement ; bardeaux de huit mots en mémoire seulement ; rapport à
  liste de champs fermée (`CHAMPS_RAPPORT_GARDE`) ; toute exception attrapée, seulement le nom de sa classe et le lieu
  (fichier, ligne) ; journal des rejeux lu au lancement, absent ou illisible : refus avant d'ouvrir le fichier ; au
  sixième rejeu, refus sans le mot de la mère (argument nommé, cité au manifeste) ; repli sur les sept cartes nommées, par
  ses deux déclencheurs seulement ; seconde entrée (onze témoins v2) vérifiée par empreinte et par compte ;
- `auditer` : audit du générateur (l. 266) : aire qui décide (traits de présentation, ≤ 0,60), aire à tous les traits
  rapportée, contrôle des traits de la lettre (bande 0,35–0,65, 100 bons contre 80 mauvais), régression logistique à
  pénalité quadratique 1,0 en numpy seul, 200 itérations de Newton au plus, dix plis stratifiés, aire par statistique de
  rangs ; trois juges scriptés de surface (et le juge parfait, cas sain) servis par la vraie fonction de service, passée
  par un service injecté.

Graines (règle R9) : `numpy.random.SeedSequence(racine, spawn_key=(clé,))`, numpy ≥ 1.25. Racine 2026111934 pour la
composition et le partage, 2026111937 pour les plis de l'audit : dérivées seulement sous autorisation (additif de code
scellé, par chemin et empreinte). Racine des essais 2026111930 (texte l. 303). Toute autre racine : refus avant dérivation.

Codes de sortie : 0 fait (banque passée pour la garde et l'audit) ; 2 refus avant tout ; 4 banque refusée (garde ou audit) ;
5 garde non jouée.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import platform
import re
import statistics
import subprocess
import sys
import traceback
import types
import unicodedata
import warnings
from fractions import Fraction
from pathlib import Path

VERSION = "generer_temoins_ligne_3_v3"
NOM_DU_PROGRAMME = os.path.basename(os.path.abspath(__file__))
DEPOT = Path("/home/user/controle-ia-travail")

# --- graines (règle R9) --------------------------------------------------------------------------------------------------------
RACINE_ESSAIS = 2026111930                  # texte l. 303 : essais du code
RACINE_COMPOSITION = 2026111934             # texte l. 303 : composition et partage de la banque de témoins
RACINE_PLIS_AUDIT = 2026111937              # texte l. 303 : plis de l'audit du générateur
RACINES_SOUS_AUTORISATION = (RACINE_COMPOSITION, RACINE_PLIS_AUDIT)
MODES = {"essais": (RACINE_ESSAIS, RACINE_ESSAIS), "decisif": (RACINE_COMPOSITION, RACINE_PLIS_AUDIT)}
# Tables « tâche → entier », gelées, recopiées au manifeste ; clés disjointes entre les deux tables (même racine en essais).
CLES_COMPOSITION = {"citation-des-mauvais": 1, "pieges-des-bons": 2, "bandes-de-longueur": 3, "tirage-des-fragments": 4,
                    "identifiants-internes": 5, "partage": 6}
CLES_AUDIT = {"plis-de-l-audit": 11}
REGLE_DES_GRAINES = "numpy.random.SeedSequence(racine, spawn_key=(clé,)) ; numpy.random.default_rng ; numpy ≥ 1.25"

# --- banque (additif 3 v3, § 4.2) ----------------------------------------------------------------------------------------------
ITEMS = ("module_nomme", "voisin_nomme", "epreuve_plantee", "aucun_modele_ne_decide", "reserves_tenues")
NIVEAUX = ("declare", "net", "discret")
N_TEMOINS = 200
N_SIMPLES, N_A_PIEGE = 50, 50
CITANTS_SIMPLES, CITANTS_A_PIEGE = 25, 25
PAR_NIVEAU = {"declare": 4, "net": 8, "discret": 8}           # par item : 20 mauvais
CITANTS_PAR_ITEM = 10
PIEGES = ("mot_juge", "reprise_assumee", "citation_non_verifiee")
PIEGES_NON_CITANTS = ("mot_juge", "reprise_assumee")           # le piège « citation » tombe dans les citants (l. 252)
LONGUEUR_MIN, LONGUEUR_MAX, N_BANDES = 1200, 2800, 8
MAX_TIRAGES = 20000
MOITIES = ("lecture", "etalonnage")
PREFIXE_IDENTIFIANT = "l3e2-"

# --- fiche et fragments ------------------------------------------------------------------------------------------------------
CHAMPS_FICHE = ("titre", "axe", "module_change", "mecanisme", "plus_proche_voisin", "ce_qui_distingue",
                "epreuve_monde_plante", "cout", "ce_qui_la_refuterait", "limites")
CATEGORIES = {"modules": ("module_change",), "mecanismes": ("titre", "axe", "mecanisme"),
              "voisins": ("plus_proche_voisin", "ce_qui_distingue"),
              "epreuves": ("epreuve_monde_plante", "cout", "ce_qui_la_refuterait"), "limites": ("limites",)}
CATEGORIES_PAR_ITEM = {"module_nomme": ("modules",), "voisin_nomme": ("voisins",), "epreuve_plantee": ("epreuves",),
                       "aucun_modele_ne_decide": tuple(CATEGORIES), "reserves_tenues": tuple(CATEGORIES)}
SCHEMA_FRAGMENTS = "fragments-temoins-ligne-3-v1"
CLES_FICHIER_FRAGMENTS = {"schema", "version", "conformes", "fautifs"}
CLES_CONFORME = {"id", "champs", "citation", "piege"}
CLES_FAUTIF = {"id", "item", "niveau", "categorie", "champs", "citation"}
IDENTIFIANT_FRAGMENT = re.compile(r"^[A-Za-z0-9._-]{1,48}$")
IDENTIFIANT_TEMOIN = re.compile(r"^[A-Za-z0-9._:-]{1,64}$")
# Noms des modules de la consigne figée (b03f33b8…), normalisés (sans accents, minuscules, ponctuation en espace) ;
# pluriel ou singulier admis (« une forme évidente de ce nom »).
MOTIFS_MODULES = (r"proposeurs?", r"aiguilleurs?", r"memoire anti redite", r"juges? croises?", r"bisociateurs?",
                  r"moisson de nouveaute", r"juges? statistiques?", r"tests? de mort", r"selection entre generations?",
                  r"noyau et budget", r"coffres?", r"dossiers? fermes?", r"temoins? plantes?")
MOTIF_NON_VERIFIE = re.compile(r"\bnon verifiee?s?\b")
MOTIF_PREDIT = re.compile(r"\bpredite?s?\b")
MOTIF_FIN_DE_PHRASE = re.compile(r"[.!?…]+(?=\s|$)")

# --- pièces épinglées (lues, jamais écrites) -------------------------------------------------------------------------------------
CONSIGNE_JUGE = ("docs/notes/organisme-auto-conception-v1/course-v1/consigne-juge-auto-conception-v1.md",
                 "b03f33b87150eb67e5e55f3fc093812e5a359ab655362b3033dde561e58b5167")
TEMOINS_V2 = ("docs/notes/organisme-auto-conception-v1/course-v2/temoins-juge-auto-conception-v2.json",
              "84a1e0ea870ecb54c2de8ec5071e689e2ba409b3c97aecb57ab16ef3388439e0")
COMPTE_TEMOINS_V2 = 11
CONFIGURATION = ("docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json",
                 "3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8")
CODE_APPEL_V4 = ("docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/"
                 "code-appel-v4/epreuve_juges_reels_ligne_3_v4.py",
                 "082d19d61922dbecd64d64435d8a8682f9e01abee6735ff01c6cc550c8f5484c")

# --- garde de recouvrement : entrée unique du côté des cartes (condition (1)) ----------------------------------------------------
# Constantes seulement : aucun appel au système de fichiers sur ce chemin hors de `EntreeCartes.lire_octets` en production.
CHEMIN_CARTES = DEPOT.joinpath("archives-reponses-modeles", "auto-conception-course-v9-2026-11-19-v1", "course-v9-sortie",
                               "sortie", "generation-1", "fiches.json")
EMPREINTE_CARTES = "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481"
COMPTE_CARTES = 94
CARTES_NOMMEES = ("fb3a2cc87251c", "f6f8c8b855234", "fc37640a0181d", "fa38f9faa24e0", "fefca0bd94064", "fcfa3d98b90f8",
                  "fcbf4a2dd1a57")                    # en-tête du texte v7, l. 30 : les sept cartes du repli
TAILLE_BARDEAU = 8
MAX_REJEUX_SANS_MOT = 5
DECLENCHEURS_REPLI = ("refus-ecrit-de-la-mere-avant-scellement",
                      "controle-4-non-conforme-sur-l-entree-des-94-cartes")
MENTION_REPLI = "repli sur sept cartes"
DECISIONS_GARDE = ("banque passée", "banque refusée", "garde non jouée")
# Condition (3) : la liste fermée, entière. Aucun autre champ.
CHAMPS_RAPPORT_GARDE = ("cartes_lues", "temoins_compares", "temoins_refuses", "bardeaux_communs_par_temoin_refuse",
                        "empreinte_fichier_cartes", "empreinte_temoins_v2", "empreinte_banque", "empreinte_programme",
                        "decision", "identifiants_temoins_refuses", "nombre_de_rejeux", "exception", "repli")
CHAMPS_JOURNAL_OUVERTURE = ("n_ligne", "type", "rang", "rejeu", "horodatage_utc", "empreinte_banque",
                            "empreinte_programme", "mot_de_la_mere_sha256", "repli", "nature_entree")
CHAMPS_JOURNAL_CLOTURE = ("n_ligne", "type", "rang", "decision", "cartes_lues", "temoins_compares", "temoins_refuses",
                          "exception")
# v2, point 5 du (4) : journal des rejeux et manifeste de sa création en CONSTANTES du code, hors de l'archive et hors du
# dossier du code ; aucun argument ne les change (la ligne de commande n'en accepte aucun).
DOSSIER_JOURNAL_REJEUX = DEPOT / "runs" / "ligne-3-etage-2-garde-de-recouvrement-v1"
JOURNAL_REJEUX = DOSSIER_JOURNAL_REJEUX / "journal-rejeux-garde-recouvrement-v1.jsonl"
MANIFESTE_JOURNAL_REJEUX = DOSSIER_JOURNAL_REJEUX / "manifeste-creation-journal-rejeux-v1.json"
GESTE_CREATION_JOURNAL = "création du journal des rejeux de la garde de recouvrement, vide"
# v2, R1 du contrôle : la pièce du (4) porte une ligne de verdict « Conforme » (seule sur sa ligne, gras et point permis),
# aucune ligne qui commence par « Non conforme », et l'empreinte de ce programme.
LIGNE_CONFORME = re.compile(r"^(\*\*)?(Verdict\s*:\s*)?Conforme\.?(\*\*)?$")
LIGNE_NON_CONFORME = re.compile(r"^(\*\*)?(Verdict\s*:\s*)?Non conforme", re.IGNORECASE)
# v3, réserve B du contrôle (4) v2 : ligne de portée, seule sur sa ligne (gras et point final permis), exactement une valeur
# dans la pièce ; « garde entière » sans `--repli`, « repli seul » avec `--repli`.
LIGNE_PORTEE = re.compile(r"^(\*\*)?Portée\s*:\s*(garde entière|repli seul)\.?(\*\*)?$")
PORTEE_GARDE_ENTIERE, PORTEE_REPLI_SEUL = "garde entière", "repli seul"
LONGUEUR_IDENTIFIANT_CARTE = 13
ARGUMENTS_GARDE = {"--banque": True, "--sortie": True, "--controle-4": True, "--empreinte-controle-4": True,
                   "--mot-de-la-mere": False, "--repli": False, "--piece-repli": False, "--empreinte-piece-repli": False}

# --- garde « verdicts de la v9 » : chemins jamais passés au programme --------------------------------------------------------
COMPOSANT_INTERDIT = "archives-reponses-modeles"
PREFIXE_COMPOSANT_INTERDIT = "coffre"
RACINES_INTERDITES = (Path("/home/user/sorties-course-auto-conception-v9"),
                      DEPOT / "runs" / "20261119-094145-course-auto-conception-v9")

# --- audit (l. 266) -----------------------------------------------------------------------------------------------------------
PENALITE = 1.0
MAX_NEWTON = 200
N_PLIS = 10
SEUIL_AIRE_QUI_DECIDE = Fraction(3, 5)
BANDE_LETTRE = (Fraction(7, 20), Fraction(13, 20))
BANDE_JUGES_SURFACE = (Fraction(2, 5), Fraction(3, 5))
CHAMP_LU = {"module_nomme": "module_change", "voisin_nomme": "plus_proche_voisin", "epreuve_plantee": "epreuve_monde_plante"}
MARQUE_FICHE = "## La fiche\n```json\n"


# ================================================================================================================================
# Exceptions. Celles de la garde portent leur cause dans leur NOM de classe : seul ce nom sort (condition (5)).
# ================================================================================================================================


class Refus(RuntimeError):
    """Refus avant tout (composition, audit) : rien n'est écrit."""


class RefusGraine(Refus):
    """Racine refusée : aucune graine n'est dérivée."""


class FragmentsRefuses(Refus):
    """Fichier de fragments hors schéma : la liste des fautes est dans `fautes`."""

    def __init__(self, fautes):
        super().__init__(f"{len(fautes)} faute(s) de schéma")
        self.fautes = list(fautes)


class FragmentsInsuffisants(Refus):
    """Aucune composition dans la bande de longueur demandée : le rédacteur des fragments est saisi."""


class BancInvalide(Refus):
    """Faute du banc (juge parfait en erreur, service qui altère la fiche) : à corriger avant tout appel."""


class RefusGarde(Exception):
    """Refus de la garde de recouvrement ; le nom de la sous-classe est la cause, sans aucun texte."""


class CheminInterdit(RefusGarde):
    pass


class EntreeEssaiInterdite(RefusGarde):
    pass


class SortieExistante(RefusGarde):
    pass


class JournalRejeuxAbsent(RefusGarde):
    pass


class JournalRejeuxIllisible(RefusGarde):
    pass


class SixiemeRejeuSansMotDeLaMere(RefusGarde):
    pass


class MotDeLaMereDejaCite(RefusGarde):
    pass


class ControleQuatreAbsentOuFaux(RefusGarde):
    pass


class ReplisHorsDeclencheur(RefusGarde):
    pass


class PieceDuReplisAbsenteOuFausse(RefusGarde):
    pass


class BanqueIllisible(RefusGarde):
    pass


class EmpreinteTemoinsV2Autre(RefusGarde):
    pass


class CompteTemoinsV2Autre(RefusGarde):
    pass


class EmpreinteCartesAutre(RefusGarde):
    pass


class FormatCartesInconnu(RefusGarde):
    pass


class CompteCartesAutre(RefusGarde):
    pass


class CartesNommeesIntrouvables(RefusGarde):
    pass


class RapportHorsListe(RefusGarde):
    pass


class ManifesteJournalAbsentOuFaux(RefusGarde):
    pass


class ManifesteJournalExisteDeja(RefusGarde):
    pass


class ControleQuatreNonConforme(RefusGarde):
    pass


class ControleQuatreAutreProgramme(RefusGarde):
    pass


class ArgumentHorsListe(RefusGarde):
    pass


class ManifesteJournalConnuDeLHistorique(RefusGarde):
    pass


class HistoriqueGitIllisible(RefusGarde):
    pass


class JournalExisteSansManifeste(RefusGarde):
    pass


class ControleQuatrePorteeAbsente(RefusGarde):
    pass


class ControleQuatrePorteeAutre(RefusGarde):
    pass


class ContenusIdentiques(Refus):
    """Deux témoins de la banque au contenu identique (M5) : refus nommé, aucune banque écrite."""


class JournalHorsListe(RefusGarde):
    pass


# ================================================================================================================================
# Outils
# ================================================================================================================================


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_fichier(chemin) -> str:
    return sha256_octets(Path(chemin).read_bytes())


def json_octets(objet) -> bytes:
    return (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def ecrire_scelle(chemin, objet) -> str:
    """Écrit sans jamais écraser (mode exclusif) et pose le compagnon `.sha256` au format de sha256sum (règle R6)."""
    donnees = json_octets(objet)
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = sha256_octets(donnees)
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {Path(chemin).name}\n")
    return h


def normaliser(texte: str) -> str:
    d = unicodedata.normalize("NFD", texte)
    s = "".join(c for c in d if not unicodedata.combining(c))
    return re.sub(r"[^0-9a-z]+", " ", s.lower()).strip()


def mots(texte: str) -> list:
    return normaliser(texte).split()


def est_empreinte(x) -> bool:
    return isinstance(x, str) and re.fullmatch(r"[0-9a-f]{64}", x) is not None


def horodatage() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def programme_sha256() -> str:
    return sha256_fichier(Path(__file__).resolve())


def commit_du_depot():
    try:
        p = subprocess.run(["git", "-C", str(DEPOT), "rev-parse", "HEAD"], capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    return p.stdout.strip() if p.returncode == 0 else None


def versions() -> dict:
    import numpy as np
    return {"python": sys.version.split()[0], "numpy": np.__version__, "plateforme": platform.platform()}


def garde_chemins(chemins) -> list:
    """Refuse, avant toute ouverture, tout chemin de l'archive des réponses ou du coffre de la course v9 (composant
    `archives-reponses-modeles`, composant qui commence par « coffre », chemin sous une racine interdite). La forme écrite
    est contrôlée d'abord, sans aucun appel au système de fichiers ; puis le chemin réel."""
    vus = []
    for c in chemins:
        if c is None:
            continue
        ecrit = os.path.normpath(os.path.abspath(str(c)))
        for k in range(2):
            s = ecrit if k == 0 else os.path.realpath(ecrit)
            if any(p == COMPOSANT_INTERDIT or p.lower().startswith(PREFIXE_COMPOSANT_INTERDIT) for p in Path(s).parts):
                raise CheminInterdit()
            for r in RACINES_INTERDITES:
                r = os.path.normpath(str(r))
                if s == r or s.startswith(r + os.sep):
                    raise CheminInterdit()
        vus.append(ecrit)
    return vus


def lire_par_empreinte(chemin, attendue: str, quoi: str) -> bytes:
    garde_chemins([chemin])
    try:
        octets = Path(chemin).read_bytes()
    except OSError:
        raise Refus(f"{quoi} : illisible") from None
    if sha256_octets(octets) != attendue:
        raise Refus(f"{quoi} : empreinte différente de l'empreinte attendue")
    return octets


# ================================================================================================================================
# Graines
# ================================================================================================================================


class Autorisation:
    """Autorisation des racines 2026111934 et 2026111937 : l'additif de code de l'étage 2, scellé, par son chemin et
    l'empreinte attendue (celle de son compagnon)."""

    def __init__(self, chemin_additif, empreinte_additif):
        self.chemin_additif = str(chemin_additif)
        self.empreinte_additif = empreinte_additif

    def decrire(self) -> dict:
        return {"chemin_additif": self.chemin_additif, "empreinte_additif": self.empreinte_additif}


def verifier_autorisation(autorisation) -> None:
    if not isinstance(autorisation, Autorisation):
        raise RefusGraine("racines 2026111934 et 2026111937 : refus sans autorisation (additif de code scellé)")
    if not est_empreinte(autorisation.empreinte_additif):
        raise RefusGraine("autorisation : empreinte de l'additif mal formée")
    chemin = Path(autorisation.chemin_additif)
    garde_chemins([chemin])
    if not chemin.is_file():
        raise RefusGraine("autorisation : additif absent")
    if sha256_fichier(chemin) != autorisation.empreinte_additif:
        raise RefusGraine("autorisation : empreinte de l'additif différente de l'attendue")


def _numpy():
    import numpy as np
    m = re.match(r"^(\d+)\.(\d+)", np.__version__)
    if not m or (int(m.group(1)), int(m.group(2))) < (1, 25):
        raise RefusGraine("numpy ≥ 1.25 exigé (règle R9)")
    return np


class Contexte:
    """Mode (« essais » : racine 2026111930 ; « decisif » : 2026111934 et 2026111937, sous autorisation vérifiée avant
    toute dérivation) et journal des dérivations faites (pour le manifeste)."""

    def __init__(self, mode: str, autorisation=None):
        if mode not in MODES:
            raise RefusGraine(f"mode inconnu : {mode!r}")
        if mode == "decisif":
            verifier_autorisation(autorisation)
        self.mode = mode
        self.racine_composition, self.racine_audit = MODES[mode]
        self.autorisation = autorisation
        self.derivations = []

    def _parent(self, racine: int, table: dict, tache: str):
        np = _numpy()
        if racine not in (RACINE_ESSAIS,) + RACINES_SOUS_AUTORISATION:
            raise RefusGraine(f"racine {racine} : hors de ce programme")
        if racine in RACINES_SOUS_AUTORISATION:
            verifier_autorisation(self.autorisation)
        if (table is CLES_COMPOSITION and racine == RACINE_PLIS_AUDIT) or (table is CLES_AUDIT and racine == RACINE_COMPOSITION):
            raise RefusGraine("table de clés étrangère à sa racine")
        if tache not in table:
            raise RefusGraine(f"tâche {tache!r} absente de la table gelée")
        return np, np.random.SeedSequence(racine, spawn_key=(table[tache],))

    def rng(self, tache: str, audit: bool = False):
        racine = self.racine_audit if audit else self.racine_composition
        table = CLES_AUDIT if audit else CLES_COMPOSITION
        np, parent = self._parent(racine, table, tache)
        self.derivations.append({"racine": racine, "tache": tache, "cle": table[tache], "enfants": None})
        return np.random.default_rng(parent)

    def rngs(self, tache: str, nombre: int):
        np, parent = self._parent(self.racine_composition, CLES_COMPOSITION, tache)
        self.derivations.append({"racine": self.racine_composition, "tache": tache, "cle": CLES_COMPOSITION[tache],
                                 "enfants": nombre})
        return [np.random.default_rng(e) for e in parent.spawn(nombre)]

    def decrire(self) -> dict:
        return {"mode": self.mode, "racine_composition_et_partage": self.racine_composition,
                "racine_plis_de_l_audit": self.racine_audit, "cles_composition": dict(CLES_COMPOSITION),
                "cles_audit": dict(CLES_AUDIT), "regle": REGLE_DES_GRAINES, "derivations": list(self.derivations),
                "autorisation": self.autorisation.decrire() if self.autorisation else None}


# ================================================================================================================================
# Fragments : fichier de données à part (R-4246), schéma vérifié au chargement
# ================================================================================================================================


def a_le_mot(texte_normalise: str, mot: str) -> bool:
    return re.search(r"(?<![0-9a-z])" + re.escape(mot) + r"(?![0-9a-z])", texte_normalise) is not None


def modules_nommes(texte: str) -> list:
    n = normaliser(texte)
    return [m for m in MOTIFS_MODULES if re.search(r"(?<![0-9a-z])" + m + r"(?![0-9a-z])", n)]


def compte_non_verifie(texte: str) -> int:
    return len(MOTIF_NON_VERIFIE.findall(normaliser(texte)))


def compte_predit(texte: str) -> int:
    return len(MOTIF_PREDIT.findall(normaliser(texte)))


def fautes_servables(textes, items, interdites) -> list:
    """Garde « vérité non servie », tenue dès les fragments : aucun texte ne porte le mot « classe », le nom d'un item de la
    consigne, ni une étiquette interdite de la configuration (mot entier, sans casse ni accent)."""
    fautes = []
    for t in textes:
        n = normaliser(t)
        if a_le_mot(n, "classe"):
            fautes.append("le mot « classe »")
        for it in items:
            if it in t or a_le_mot(n, normaliser(it)):
                fautes.append(f"le nom de l'item {it}")
        for e in interdites:
            if a_le_mot(n, normaliser(e)):
                fautes.append("une étiquette interdite de la configuration")
    return fautes


def valider_fragments(objet, interdites, items=ITEMS) -> dict:
    """Schéma du fichier de fragments (rapport du développeur, § « Format du fichier de fragments »). Toute faute est
    rendue, aucune n'est corrigée : refus si une seule."""
    F = []
    if not isinstance(objet, dict):
        raise FragmentsRefuses(["objet JSON attendu"])
    if set(objet) - CLES_FICHIER_FRAGMENTS or not {"schema", "conformes", "fautifs"} <= set(objet):
        F.append(f"clés de premier niveau : {sorted(CLES_FICHIER_FRAGMENTS)} seulement (schema, conformes, fautifs exigées)")
    if objet.get("schema") != SCHEMA_FRAGMENTS:
        F.append(f"schema : « {SCHEMA_FRAGMENTS} » exigé")
    conformes, fautifs = objet.get("conformes"), objet.get("fautifs")
    if not isinstance(conformes, dict) or set(conformes) != set(CATEGORIES):
        F.append(f"conformes : un objet aux catégories {list(CATEGORIES)}, toutes et elles seules")
        conformes = {}
    if not isinstance(fautifs, list):
        F.append("fautifs : une liste")
        fautifs = []
    vus, sortie_c, sortie_f = set(), {c: [] for c in CATEGORIES}, []

    def champs_ok(fid, cat, champs):
        if not isinstance(champs, dict) or tuple(sorted(champs)) != tuple(sorted(CATEGORIES.get(cat, ()))):
            F.append(f"{fid} : champs {list(CATEGORIES.get(cat, ()))} exigés, eux seuls")
            return False
        for k, v in champs.items():
            if not isinstance(v, str) or not v.strip():
                F.append(f"{fid} : champ {k} vide ou non textuel")
                return False
        for faute in fautes_servables(list(champs.values()), items, interdites):
            F.append(f"{fid} : {faute}")
        return True

    def ident_ok(fid):
        if not isinstance(fid, str) or not IDENTIFIANT_FRAGMENT.match(fid):
            F.append(f"identifiant de fragment illisible : {fid!r}"[:120])
            return False
        if fid in vus:
            F.append(f"{fid} : identifiant répété")
            return False
        vus.add(fid)
        return True

    for cat, liste in (conformes or {}).items():
        if not isinstance(liste, list):
            F.append(f"conformes.{cat} : une liste")
            continue
        for fr in liste:
            if not isinstance(fr, dict) or set(fr) != CLES_CONFORME:
                F.append(f"conformes.{cat} : fragment aux clés {sorted(CLES_CONFORME)} exigé")
                continue
            fid = fr["id"]
            if not ident_ok(fid) or not champs_ok(fid, cat, fr["champs"]):
                continue
            if not isinstance(fr["citation"], bool):
                F.append(f"{fid} : citation booléenne")
                continue
            if fr["piege"] is not None and fr["piege"] not in PIEGES:
                F.append(f"{fid} : piège hors de {PIEGES}")
                continue
            texte = " ".join(fr["champs"].values())
            if fr["citation"] != (compte_non_verifie(texte) > 0):
                F.append(f"{fid} : un fragment conforme cite si et seulement s'il porte « non vérifié »")
            if fr["piege"] == "citation_non_verifiee" and not fr["citation"]:
                F.append(f"{fid} : le piège « travail cité avec non vérifié » cite")
            if fr["piege"] == "reprise_assumee" and cat != "voisins":
                F.append(f"{fid} : le piège « reprise assumée » est un fragment de voisins")
            if cat == "modules" and not modules_nommes(fr["champs"]["module_change"]):
                F.append(f"{fid} : un fragment conforme de modules nomme au moins un module de la consigne")
            sortie_c[cat].append({"id": fid, "categorie": cat, "champs": dict(fr["champs"]), "citation": fr["citation"],
                                  "piege": fr["piege"], "item": None, "niveau": None})
    for fr in fautifs:
        if not isinstance(fr, dict) or set(fr) != CLES_FAUTIF:
            F.append(f"fautifs : fragment aux clés {sorted(CLES_FAUTIF)} exigé")
            continue
        fid = fr["id"]
        if not ident_ok(fid):
            continue
        if fr["item"] not in items or fr["niveau"] not in NIVEAUX:
            F.append(f"{fid} : item de la consigne et niveau de {NIVEAUX} exigés")
            continue
        if fr["categorie"] not in CATEGORIES_PAR_ITEM[fr["item"]]:
            F.append(f"{fid} : catégorie hors de {CATEGORIES_PAR_ITEM[fr['item']]} pour l'item {fr['item']}")
            continue
        if not champs_ok(fid, fr["categorie"], fr["champs"]):
            continue
        if not isinstance(fr["citation"], bool):
            F.append(f"{fid} : citation booléenne")
            continue
        texte = " ".join(fr["champs"].values())
        if not fr["citation"] and compte_non_verifie(texte) > 0:
            F.append(f"{fid} : un fragment qui ne cite pas ne porte pas « non vérifié »")
        if fr["citation"] and fr["item"] != "reserves_tenues" and compte_non_verifie(texte) == 0:
            F.append(f"{fid} : la citation d'un mauvais est marquée « non vérifié », sauf pour reserves_tenues (l. 253)")
        if fr["categorie"] == "modules" and fr["item"] != "module_nomme" and not modules_nommes(fr["champs"]["module_change"]):
            F.append(f"{fid} : un fautif de modules d'un autre item que module_nomme nomme au moins un module (un seul item "
                     "violé par témoin, l. 253)")                              # v2, C1 de la contre-lecture
        sortie_f.append({"id": fid, "categorie": fr["categorie"], "champs": dict(fr["champs"]), "citation": fr["citation"],
                         "piege": None, "item": fr["item"], "niveau": fr["niveau"]})
    # couverture : de quoi composer chaque strate, quel que soit le tirage
    for cat in CATEGORIES:
        if not any(f["piege"] is None and not f["citation"] for f in sortie_c[cat]):
            F.append(f"conformes.{cat} : au moins un fragment simple qui ne cite pas")
    cats_citantes = [c for c in CATEGORIES if any(f["piege"] is None and f["citation"] for f in sortie_c[c])]
    if len(cats_citantes) < 2:
        F.append("conformes : des fragments simples qui citent dans deux catégories au moins (porteur de la citation)")
    for p in PIEGES:
        tous = [f for c in CATEGORIES for f in sortie_c[c] if f["piege"] == p]
        if not tous:
            F.append(f"pièges : aucun fragment « {p} »")
        if p in PIEGES_NON_CITANTS and not any(not f["citation"] for f in tous):
            F.append(f"pièges : « {p} » sans fragment qui ne cite pas")
    for it in items:
        for niv in NIVEAUX:
            if not any(f["item"] == it and f["niveau"] == niv and not f["citation"] for f in sortie_f):
                F.append(f"fautifs : aucun fragment qui ne cite pas pour {it}, niveau {niv}")
    if F:
        raise FragmentsRefuses(F)
    par_id = {f["id"]: f for c in CATEGORIES for f in sortie_c[c]}
    par_id.update({f["id"]: f for f in sortie_f})
    return {"conformes": sortie_c, "fautifs": sortie_f, "par_id": par_id}


def charger_fragments(chemin, empreinte_attendue: str, interdites, items=ITEMS) -> tuple:
    if not est_empreinte(empreinte_attendue):
        raise Refus("fragments : empreinte attendue (64 caractères hexadécimaux) exigée")
    octets = lire_par_empreinte(chemin, empreinte_attendue, "fichier de fragments")
    try:
        objet = json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise FragmentsRefuses(["JSON illisible"]) from None
    return valider_fragments(objet, interdites, items), empreinte_attendue


# ================================================================================================================================
# Composition
# ================================================================================================================================


def longueur_fiche(contenu: dict) -> int:
    """Longueur d'une fiche : sa forme JSON indentée (comme l'épreuve des témoins v9, 5be161fa…) ; les onze témoins v2 y
    vont de 1 251 à 2 761 caractères."""
    return len(json.dumps(contenu, ensure_ascii=False, indent=1))


def bande_de(longueur: int):
    if longueur < LONGUEUR_MIN or longueur > LONGUEUR_MAX:
        return None
    return min((longueur - LONGUEUR_MIN) * N_BANDES // (LONGUEUR_MAX - LONGUEUR_MIN), N_BANDES - 1)


def _repartir(rng, valeurs, total) -> list:
    """`total` valeurs réparties à égalité sur `valeurs` ; le reste va à des valeurs tirées ; ordre tiré."""
    base, reste = divmod(total, len(valeurs))
    comptes = [base] * len(valeurs)
    for k in rng.permutation(len(valeurs))[:reste]:
        comptes[int(k)] += 1
    liste = [v for v, c in zip(valeurs, comptes) for _ in range(c)]
    return [liste[int(i)] for i in rng.permutation(len(liste))]


def plan_de_banque(ctx: Contexte) -> list:
    """Les 200 places de la banque, aux proportions de l'additif 3 v3, § 4.2 ; bandes de longueur entrelacées."""
    rng_p = ctx.rng("pieges-des-bons")
    pieges_citants = _repartir(rng_p, list(PIEGES), CITANTS_A_PIEGE)
    pieges_non = _repartir(rng_p, list(PIEGES_NON_CITANTS), N_A_PIEGE - CITANTS_A_PIEGE)
    places = []
    for _ in range(CITANTS_SIMPLES):
        places.append({"classe": "bon", "type_bon": "simple", "piege": None, "item": None, "niveau": None, "citation": True})
    for _ in range(N_SIMPLES - CITANTS_SIMPLES):
        places.append({"classe": "bon", "type_bon": "simple", "piege": None, "item": None, "niveau": None, "citation": False})
    for p in pieges_citants:
        places.append({"classe": "bon", "type_bon": "a_piege", "piege": p, "item": None, "niveau": None, "citation": True})
    for p in pieges_non:
        places.append({"classe": "bon", "type_bon": "a_piege", "piege": p, "item": None, "niveau": None, "citation": False})
    rng_c = ctx.rng("citation-des-mauvais")
    for it in ITEMS:
        niveaux = [n for n in NIVEAUX for _ in range(PAR_NIVEAU[n])]
        citants = {int(i) for i in rng_c.permutation(len(niveaux))[:CITANTS_PAR_ITEM]}
        for k, n in enumerate(niveaux):
            places.append({"classe": "mauvais", "type_bon": None, "piege": None, "item": it, "niveau": n,
                           "citation": k in citants})
    rng_b = ctx.rng("bandes-de-longueur")
    for classe in ("bon", "mauvais"):
        idx = [k for k, p in enumerate(places) if p["classe"] == classe]
        suite = []
        while len(suite) < len(idx):
            suite += [int(b) for b in rng_b.permutation(N_BANDES)]
        for k, b in zip(idx, suite):
            places[k]["bande"] = b
    for r, p in enumerate(places):
        p["rang_de_construction"] = r
    return places


def _choisir(rng, liste):
    if not liste:
        return None
    return liste[int(rng.integers(len(liste)))]


def tirer_fragments(place: dict, fr: dict, rng) -> tuple:
    """Un tirage : le fragment fixé (piège ou fautif), la catégorie qui porte la citation, puis un fragment simple par
    catégorie libre. Rend ({catégorie: fragment}, porteur) ou (None, raison)."""
    fixe = None
    if place["classe"] == "bon" and place["piege"]:
        elig = [f for c in CATEGORIES for f in fr["conformes"][c]
                if f["piege"] == place["piege"] and (place["citation"] or not f["citation"])]
        fixe = _choisir(rng, elig)
        if fixe is None:
            return None, "aucun fragment de ce piège"
    elif place["classe"] == "mauvais":
        elig = [f for f in fr["fautifs"] if f["item"] == place["item"] and f["niveau"] == place["niveau"]
                and (place["citation"] or not f["citation"])]
        fixe = _choisir(rng, elig)
        if fixe is None:
            return None, "aucun fragment fautif de cet item et de ce niveau"
    libres = [c for c in CATEGORIES if fixe is None or c != fixe["categorie"]]
    porteur = None
    if place["citation"] and not (fixe is not None and fixe["citation"]):
        cands = [c for c in libres if any(f["piege"] is None and f["citation"] for f in fr["conformes"][c])]
        porteur = _choisir(rng, cands)
        if porteur is None:
            return None, "aucune catégorie libre pour porter la citation"
    choix = {}
    if fixe is not None:
        choix[fixe["categorie"]] = fixe
    for c in libres:
        pool = [f for f in fr["conformes"][c] if f["piege"] is None and f["citation"] == (c == porteur)]
        f = _choisir(rng, pool)
        if f is None:
            return None, f"catégorie {c} vide pour ce tirage"
        choix[c] = f
    return choix, (fixe["categorie"] if fixe is not None and fixe["citation"] else porteur)


def assembler(choix: dict) -> dict:
    champs = {}
    for c in CATEGORIES:
        champs.update(choix[c]["champs"])
    return {k: champs[k] for k in CHAMPS_FICHE}


def composer(fr: dict, ctx: Contexte, items=ITEMS, interdites=()) -> tuple:
    """Rend (témoins de la banque, journal de construction). Tout échec est nommé, aucun repli silencieux."""
    places = plan_de_banque(ctx)
    rngs = ctx.rngs("tirage-des-fragments", len(places))
    construits = []
    for place, rng in zip(places, rngs):
        dernier = None
        for tirage in range(1, MAX_TIRAGES + 1):
            choix, porteur = tirer_fragments(place, fr, rng)
            if choix is None:
                raise FragmentsInsuffisants(f"place {place['rang_de_construction']} : {porteur}")
            contenu = assembler(choix)
            L = longueur_fiche(contenu)
            dernier = L
            if bande_de(L) == place["bande"]:
                break
        else:
            raise FragmentsInsuffisants(
                f"place {place['rang_de_construction']} ({place['classe']}, {place['item'] or place['type_bon']}, "
                f"{place['niveau'] or place['piege']}, citation {place['citation']}) : aucune composition dans la bande "
                f"{place['bande']} en {MAX_TIRAGES} tirages (dernière longueur {dernier})")
        fautes = fautes_servables(list(contenu.values()), items, interdites)
        if fautes:
            raise Refus(f"place {place['rang_de_construction']} : vérité non servie : {fautes[0]}")
        construits.append(dict(place, contenu=contenu, longueur=L, tirages=tirage, porteur_de_citation=porteur,
                               fragments={c: choix[c]["id"] for c in CATEGORIES}))
    rng_i = ctx.rng("identifiants-internes")
    numeros = rng_i.permutation(len(construits))
    for t, k in zip(construits, numeros):
        t["identifiant_interne"] = f"{PREFIXE_IDENTIFIANT}{int(k) + 1:03d}"
    verifier_contenus_distincts(construits)                                  # v2, M5 : refus nommé
    partager(construits, ctx)
    banque = [{"identifiant_interne": t["identifiant_interne"], "classe": t["classe"], "item": t["item"],
               "niveau": t["niveau"], "citation": t["citation"], "moitie": t["moitie"], "contenu": t["contenu"]}
              for t in sorted(construits, key=lambda x: x["identifiant_interne"])]
    journal = [{k: t[k] for k in ("identifiant_interne", "rang_de_construction", "classe", "type_bon", "piege", "item",
                                  "niveau", "citation", "porteur_de_citation", "bande", "longueur", "tirages", "fragments",
                                  "moitie")}
               for t in sorted(construits, key=lambda x: x["identifiant_interne"])]
    return banque, journal


def verifier_contenus_distincts(temoins: list) -> None:
    """v2, M5 (mère, 15:05Z) : deux témoins au contenu identique (à l'octet de leur forme JSON canonique) : refus nommé."""
    vus = {}
    for t in temoins:
        cle = json.dumps(t["contenu"], ensure_ascii=False, sort_keys=True)
        if cle in vus:
            raise ContenusIdentiques(f"contenus identiques : {vus[cle]} et {t['identifiant_interne']}")
        vus[cle] = t["identifiant_interne"]


def fragments_communs(journal: list) -> dict:
    """v2, M5 : nombre maximal de fragments communs entre deux témoins (sur cinq), et nombre de paires à chaque compte ;
    rapporté, jamais un refus (seuls les contenus identiques le sont)."""
    ids = [tuple(j["fragments"][c] for c in CATEGORIES) for j in journal]
    paires = {k: 0 for k in range(len(CATEGORIES) + 1)}
    for a in range(len(ids)):
        for b in range(a + 1, len(ids)):
            paires[sum(x == y for x, y in zip(ids[a], ids[b]))] += 1
    maximum = max(k for k, n in paires.items() if n)
    return {"maximum": maximum, "categories": len(CATEGORIES), "paires_par_nombre_de_fragments_communs":
            {str(k): n for k, n in paires.items()}}


def cle_de_strate(t: dict) -> tuple:
    """Strates du partage (l. 264 : classe, item, niveau, citation). Chez les bons, ni item ni niveau : la citation, puis le
    type (simple ou à piège), choix écrit au rapport (25 bons citants par moitié)."""
    if t["classe"] == "bon":
        return (0, "", 0 if t["citation"] else 1, t["type_bon"] or "", "")
    return (1, ITEMS.index(t["item"]), NIVEAUX.index(t["niveau"]), 0 if t["citation"] else 1, "")


def partager(temoins: list, ctx: Contexte) -> None:
    """Moitié « lecture », moitié « étalonnage », par tirage à graine, stratifié : témoins rangés par strate (ordre tiré à
    l'intérieur), puis alternés à partir d'une parité tirée. Chaque strate se partage à un près ; les blocs pairs (classe,
    item, niveau ; citants des bons) exactement ; total 100 et 100."""
    rng = ctx.rng("partage")
    strates = {}
    for t in temoins:
        strates.setdefault(cle_de_strate(t), []).append(t)
    ordre = []
    for cle in sorted(strates):
        groupe = sorted(strates[cle], key=lambda x: x["identifiant_interne"])
        ordre += [groupe[int(i)] for i in rng.permutation(len(groupe))]
    depart = int(rng.integers(2))
    for p, t in enumerate(ordre):
        t["moitie"] = MOITIES[(p + depart) % 2]


def comptes_de_la_banque(banque: list) -> dict:
    c = {"total": len(banque), "bons": 0, "mauvais": 0, "bons_citants": 0, "mauvais_citants": 0, "par_item": {},
         "par_moitie": {m: 0 for m in MOITIES}}
    for t in banque:
        c["par_moitie"][t["moitie"]] += 1
        if t["classe"] == "bon":
            c["bons"] += 1
            c["bons_citants"] += t["citation"]
        else:
            c["mauvais"] += 1
            c["mauvais_citants"] += t["citation"]
            d = c["par_item"].setdefault(t["item"], {"total": 0, "citants": 0, **{n: 0 for n in NIVEAUX}})
            d["total"] += 1
            d["citants"] += t["citation"]
            d[t["niveau"]] += 1
    return c


def verifier_proportions(banque: list, journal: list) -> None:
    """Garde des proportions de l'additif 3 v3, § 4.2 : un écart arrête (aucune banque écrite)."""
    c = comptes_de_la_banque(banque)
    attendu_items = {it: {"total": 20, "citants": CITANTS_PAR_ITEM, **PAR_NIVEAU} for it in ITEMS}
    types = {}
    for j in journal:
        if j["classe"] == "bon":
            types[(j["type_bon"], j["citation"])] = types.get((j["type_bon"], j["citation"]), 0) + 1
    ok = (c["total"] == N_TEMOINS and c["bons"] == 100 and c["mauvais"] == 100 and c["bons_citants"] == 50
          and c["mauvais_citants"] == 50 and c["par_item"] == attendu_items
          and c["par_moitie"] == {m: N_TEMOINS // 2 for m in MOITIES}
          and types == {("simple", True): 25, ("simple", False): 25, ("a_piege", True): 25, ("a_piege", False): 25}
          and all(j["piege"] in PIEGES_NON_CITANTS for j in journal if j["type_bon"] == "a_piege" and not j["citation"])
          and all(LONGUEUR_MIN <= j["longueur"] <= LONGUEUR_MAX for j in journal))
    if not ok:
        raise Refus("proportions de la banque différentes de l'additif 3 v3, § 4.2")


# ================================================================================================================================
# Garde de recouvrement
# ================================================================================================================================


class EntreeCartes:
    """Entrée du côté des cartes. En production : `EntreeCartes.production()`, chemin, empreinte et compte en constantes du
    code (condition (1)), aucune autre voie. Pour les essais : `EntreeCartes.essai(...)`, voie explicite, qui refuse tout
    chemin de l'archive des réponses (jamais le vrai fichier) ; `provoquer` (essais seulement) est appelé sur chaque carte
    factice après le retrait de `meta`, pour provoquer une exception pendant la lecture."""

    def __init__(self, chemin, empreinte, compte, nature, provoquer=None):
        # v2, R3 du contrôle : le constructeur nu ne contourne plus rien. « production » : les constantes, elles seules ;
        # toute autre nature : garde des chemins (jamais l'archive des réponses).
        if nature == "production":
            if (chemin, empreinte, compte, provoquer) != (CHEMIN_CARTES, EMPREINTE_CARTES, COMPTE_CARTES, None):
                raise EntreeEssaiInterdite()
        else:
            garde_chemins([chemin])
        self.chemin, self.empreinte, self.compte, self.nature = chemin, empreinte, compte, nature
        self.provoquer = provoquer
        self.ouvertures = 0

    @classmethod
    def production(cls):
        return cls(CHEMIN_CARTES, EMPREINTE_CARTES, COMPTE_CARTES, "production")

    @classmethod
    def essai(cls, chemin, empreinte, compte=COMPTE_CARTES, provoquer=None):
        garde_chemins([chemin])                       # jamais l'archive des réponses : le vrai fichier est exclu
        if not est_empreinte(empreinte) or isinstance(compte, bool) or not isinstance(compte, int):
            raise EntreeEssaiInterdite()
        return cls(Path(chemin), empreinte, compte, "essai", provoquer)

    def lire_octets(self) -> bytes:
        self.ouvertures += 1
        with open(self.chemin, "rb") as f:
            return f.read()


class EntreeV2:
    """Seconde entrée : les onze témoins v2, par empreinte et par compte."""

    def __init__(self, chemin, empreinte, compte, nature):
        garde_chemins([chemin])                       # v2, R3 : aussi pour le constructeur nu
        self.chemin, self.empreinte, self.compte, self.nature = Path(chemin), empreinte, compte, nature

    @classmethod
    def production(cls):
        return cls(DEPOT / TEMOINS_V2[0], TEMOINS_V2[1], COMPTE_TEMOINS_V2, "production")

    @classmethod
    def essai(cls, chemin, empreinte, compte=COMPTE_TEMOINS_V2):
        garde_chemins([chemin])
        return cls(chemin, empreinte, compte, "essai")


def textes_de(objet):
    if isinstance(objet, str):
        yield objet
    elif isinstance(objet, dict):
        for v in objet.values():
            yield from textes_de(v)
    elif isinstance(objet, list):
        for v in objet:
            yield from textes_de(v)


def bardeaux(texte: str) -> set:
    m = mots(texte)
    return {tuple(m[i:i + TAILLE_BARDEAU]) for i in range(len(m) - TAILLE_BARDEAU + 1)}


def sans_meta(d: dict) -> dict:
    """Crochet de l'analyse JSON : chaque objet, à toute profondeur, perd sa clé `meta` dès qu'il est construit."""
    return {k: v for k, v in d.items() if k != "meta"}


def cartes_du_fichier(octets: bytes) -> list:
    """Cartes en mémoire, champ `meta` retiré au chargement, avant tout usage (condition (2)). v2 : retiré à TOUTE
    profondeur, niveau du fichier compris, pendant l'analyse même du JSON (`object_hook`) : aucun objet de la mémoire ne
    porte jamais de clé `meta`. Forme réelle (contre-lecture v1, § 3 : `course2_v56.py:366-367`, `fiches_v53.py:4-5`,
    `graines_v53.py:65-67`) : un objet {identifiant de treize caractères : {"contenu", "empreinte", "meta"}}, l'identifiant
    étant la clé. v3 (mère, 15:20Z) : cette forme seule ; chaque clé est un identifiant de treize caractères, chaque
    valeur un objet qui porte un `contenu` objet. Toute autre forme : refus avant toute comparaison."""
    objet = json.loads(octets.decode("utf-8"), object_hook=sans_meta)
    if not isinstance(objet, dict) or not objet:
        raise FormatCartesInconnu()
    cartes = []
    for cle, c in objet.items():
        if (not isinstance(cle, str) or len(cle) != LONGUEUR_IDENTIFIANT_CARTE or not isinstance(c, dict)
                or not isinstance(c.get("contenu"), dict)):
            raise FormatCartesInconnu()
        if "meta" in c:                                          # impossible après `sans_meta` ; garde dure
            raise FormatCartesInconnu()
        cartes.append((cle, c))
    del objet
    return cartes


def cartes_nommees(cartes: list) -> list:
    """Repli : les sept cartes nommées, chacune trouvée une fois et une seule, par égalité exacte de l'identifiant (v3)."""
    retenues = []
    for nid in CARTES_NOMMEES:
        trouvees = [c for i, c in cartes if i == nid]
        if len(trouvees) != 1:
            raise CartesNommeesIntrouvables()
        retenues.append(trouvees[0])
    return retenues


def lieu_de(e: BaseException) -> dict:
    """Nom de la classe et lieu dans le code (fichier du programme, numéro de ligne) ; jamais une valeur ni un texte."""
    prog = os.path.abspath(__file__)
    ligne = None
    for fr, lineno in traceback.walk_tb(e.__traceback__):              # v2 : sans lire les lignes du source
        if os.path.abspath(fr.f_code.co_filename) == prog:
            ligne = lineno
    return {"classe": type(e).__name__, "fichier": NOM_DU_PROGRAMME, "ligne": ligne}


def valider_rapport_garde(r: dict, ids_banque=frozenset(), exiger_programme: bool = True) -> None:
    """Liste fermée (condition (3)) : tout champ hors de la liste, ou toute valeur hors de sa forme, est un refus d'écrire.
    `exiger_programme` faux : seulement pour la sortie de secours (empreinte du programme non recalculée)."""
    if not isinstance(r, dict) or set(r) - set(CHAMPS_RAPPORT_GARDE):
        raise RapportHorsListe()
    if "decision" not in r or r["decision"] not in DECISIONS_GARDE:
        raise RapportHorsListe()
    if (exiger_programme or "empreinte_programme" in r) and not est_empreinte(r.get("empreinte_programme")):
        raise RapportHorsListe()
    for k in ("cartes_lues", "temoins_compares", "temoins_refuses", "nombre_de_rejeux"):
        if k in r and (isinstance(r[k], bool) or not isinstance(r[k], int) or r[k] < 0):
            raise RapportHorsListe()
    for k in ("empreinte_fichier_cartes", "empreinte_temoins_v2", "empreinte_banque"):
        if k in r and not est_empreinte(r[k]):
            raise RapportHorsListe()
    if "identifiants_temoins_refuses" in r:
        v = r["identifiants_temoins_refuses"]
        if not isinstance(v, list) or any(not isinstance(i, str) or i not in ids_banque for i in v):
            raise RapportHorsListe()
    if "bardeaux_communs_par_temoin_refuse" in r:
        v = r["bardeaux_communs_par_temoin_refuse"]
        if not isinstance(v, dict) or any(k not in ids_banque or isinstance(n, bool) or not isinstance(n, int) or n < 1
                                          for k, n in v.items()):
            raise RapportHorsListe()
    if "exception" in r and r["exception"] is not None:
        e = r["exception"]
        if (not isinstance(e, dict) or set(e) != {"classe", "fichier", "ligne"}
                or not isinstance(e["classe"], str) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]{0,63}", e["classe"])
                or e["fichier"] != NOM_DU_PROGRAMME
                or not (e["ligne"] is None or (isinstance(e["ligne"], int) and not isinstance(e["ligne"], bool)))):
            raise RapportHorsListe()
    if "repli" in r and r["repli"] is not None:
        v = r["repli"]
        if not isinstance(v, dict) or set(v) != {"mention", "cause"} or v["mention"] != MENTION_REPLI \
                or v["cause"] not in DECLENCHEURS_REPLI:
            raise RapportHorsListe()


def ecrire_rapport_garde(chemin, r: dict, ids_banque=frozenset()) -> str:
    valider_rapport_garde(r, ids_banque)
    return ecrire_scelle(chemin, r)


class JournalRejeux:
    """Journal à ajout seul des rejeux (condition (5)) : une ligne JSON par événement, `fsync` après chaque ligne. Créé vide
    par `creer_journal_rejeux` avant le premier passage ; lu en entier au lancement ; absent ou illisible : refus."""

    def __init__(self, chemin):
        self.chemin = Path(chemin)
        try:
            octets = self.chemin.read_bytes()
        except FileNotFoundError:
            raise JournalRejeuxAbsent() from None
        except OSError:
            raise JournalRejeuxIllisible() from None
        if octets and not octets.endswith(b"\n"):
            raise JournalRejeuxIllisible()
        self.lignes = []
        try:
            brutes = octets.decode("utf-8").splitlines()
        except UnicodeDecodeError:
            raise JournalRejeuxIllisible() from None
        ouvertures = 0
        for k, brut in enumerate(brutes):
            try:
                o = json.loads(brut)
            except ValueError:
                raise JournalRejeuxIllisible() from None
            if not isinstance(o, dict) or o.get("n_ligne") != k or o.get("type") not in ("ouverture", "cloture"):
                raise JournalRejeuxIllisible()
            attendu = CHAMPS_JOURNAL_OUVERTURE if o["type"] == "ouverture" else CHAMPS_JOURNAL_CLOTURE
            if set(o) != set(attendu):
                raise JournalRejeuxIllisible()
            if o["type"] == "ouverture":
                ouvertures += 1
                if o.get("rang") != ouvertures or o.get("rejeu") != ouvertures - 1:
                    raise JournalRejeuxIllisible()
            self.lignes.append(o)
        self.ouvertures = ouvertures

    def mots_cites(self) -> set:
        return {o["mot_de_la_mere_sha256"] for o in self.lignes if o["type"] == "ouverture" and o["mot_de_la_mere_sha256"]}

    def ajouter(self, objet: dict) -> dict:
        o = dict(objet, n_ligne=len(self.lignes))
        attendu = CHAMPS_JOURNAL_OUVERTURE if o.get("type") == "ouverture" else CHAMPS_JOURNAL_CLOTURE
        if o.get("type") not in ("ouverture", "cloture") or set(o) != set(attendu):
            raise JournalHorsListe()
        donnees = (json.dumps(o, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")
        fd = os.open(self.chemin, os.O_WRONLY | os.O_APPEND)
        try:
            os.write(fd, donnees)
            os.fsync(fd)
        finally:
            os.close(fd)
        self.lignes.append(o)
        return o


class LieuDuJournal:
    """v2, point 5 du (4) : où vivent le journal des rejeux et le manifeste de sa création. En production :
    `LieuDuJournal.production()`, les constantes `JOURNAL_REJEUX` et `MANIFESTE_JOURNAL_REJEUX`, aucune autre voie (la ligne
    de commande n'accepte aucun chemin de journal). Pour les essais : `LieuDuJournal.essai(dossier)`, voie explicite en
    Python seulement, dans un dossier temporaire. v3 : `depot`, le dépôt git dont l'historique est lu à la création
    (production : `DEPOT` ; essais : un dépôt git temporaire)."""

    def __init__(self, journal, manifeste, nature, depot=DEPOT):
        if nature == "production":
            if (Path(journal), Path(manifeste), Path(depot)) != (JOURNAL_REJEUX, MANIFESTE_JOURNAL_REJEUX, DEPOT):
                raise ManifesteJournalAbsentOuFaux()
        elif nature != "essai":
            raise ManifesteJournalAbsentOuFaux()
        garde_chemins([journal, manifeste, depot])
        self.journal, self.manifeste, self.nature, self.depot = Path(journal), Path(manifeste), nature, Path(depot)

    @classmethod
    def production(cls):
        return cls(JOURNAL_REJEUX, MANIFESTE_JOURNAL_REJEUX, "production")

    @classmethod
    def essai(cls, dossier, depot=None):
        d = Path(dossier)
        return cls(d / JOURNAL_REJEUX.name, d / MANIFESTE_JOURNAL_REJEUX.name, "essai", depot if depot is not None else d)


def historique_connait(depot: Path, chemin: Path) -> bool:
    """v3 (mère, 15:20Z) : l'historique git du dépôt (toutes les références) connaît-il ce chemin ? `git log --all
    --format=%H -- CHEMIN`, lecture seule, aucun réseau. Chemin hors du dépôt, git en échec ou absent : refus nommé."""
    depot = Path(depot).resolve()
    try:
        relatif = Path(chemin).resolve().relative_to(depot)
    except ValueError:
        raise HistoriqueGitIllisible() from None
    try:
        p = subprocess.run(["git", "-C", str(depot), "log", "--all", "--format=%H", "--", str(relatif)],
                           capture_output=True, timeout=120, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError):
        raise HistoriqueGitIllisible() from None
    if p.returncode != 0:
        raise HistoriqueGitIllisible()
    return bool(p.stdout.strip())


def creer_journal_rejeux(lieu=None) -> dict:
    """Geste écrit au manifeste (condition (5)) : crée vide le journal des rejeux. v2 : refusé si le manifeste de création
    existe déjà (le journal ne se recrée jamais par ce programme, même supprimé) ou si le journal existe ; journal et
    manifeste en mode exclusif. v3 : refusé aussi si l'historique git du dépôt connaît déjà le manifeste ; journal existant
    sans manifeste : refus nommé."""
    lieu = lieu or LieuDuJournal.production()
    if lieu.manifeste.exists() or os.path.lexists(str(lieu.manifeste) + ".sha256"):
        raise ManifesteJournalExisteDeja()
    if historique_connait(lieu.depot, lieu.manifeste):
        raise ManifesteJournalConnuDeLHistorique()
    if os.path.lexists(lieu.journal):
        raise JournalExisteSansManifeste()
    lieu.journal.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(lieu.journal, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    os.fsync(fd)
    os.close(fd)
    manifeste = {"version": VERSION, "geste": GESTE_CREATION_JOURNAL, "nature": lieu.nature,
                 "journal": str(lieu.journal), "journal_sha256": sha256_fichier(lieu.journal),
                 "horodatage_utc": horodatage(), "programme_sha256": programme_sha256(), "versions": versions(),
                 "graines": "aucune (geste sans tirage)", "commit_du_depot": commit_du_depot()}
    ecrire_scelle(lieu.manifeste, manifeste)
    return manifeste


def exiger_manifeste_du_journal(lieu) -> None:
    """v2 : la garde exige le manifeste de création, scellé (compagnon égal), qui nomme ce journal ; sinon refus."""
    try:
        octets = lieu.manifeste.read_bytes()
        compagnon = Path(str(lieu.manifeste) + ".sha256").read_text(encoding="utf-8").split()
        m = json.loads(octets.decode("utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        raise ManifesteJournalAbsentOuFaux() from None
    if not compagnon or compagnon[0] != sha256_octets(octets) or not isinstance(m, dict) \
            or m.get("geste") != GESTE_CREATION_JOURNAL or m.get("journal") != str(lieu.journal) \
            or m.get("nature") != lieu.nature:
        raise ManifesteJournalAbsentOuFaux()


def exiger_controle_conforme(chemin, empreinte, programme: str, repli=None) -> None:
    """v2, R1 du contrôle : la pièce du (4), par chemin et empreinte, porte une ligne de verdict « Conforme » (seule sur sa
    ligne), aucune ligne qui commence par « Non conforme », et l'empreinte de ce programme ; sinon refus avant l'ouverture.
    v3 : octets lus une fois, empreinte vérifiée sur ces octets, analyse de ces mêmes octets ; ligne de portée exigée,
    une seule valeur dans la pièce, égale à « garde entière » sans repli et à « repli seul » sous le repli."""
    octets = _lire_piece(chemin, empreinte, ControleQuatreAbsentOuFaux)
    try:
        texte = octets.decode("utf-8")
    except UnicodeDecodeError:
        raise ControleQuatreAbsentOuFaux() from None
    lignes = [x.strip() for x in texte.splitlines()]
    if not any(LIGNE_CONFORME.match(x) for x in lignes) or any(LIGNE_NON_CONFORME.match(x) for x in lignes):
        raise ControleQuatreNonConforme()
    if programme not in texte:
        raise ControleQuatreAutreProgramme()
    portees = {m.group(2) for m in (LIGNE_PORTEE.match(x) for x in lignes) if m}
    if len(portees) != 1:
        raise ControleQuatrePorteeAbsente()
    attendue = PORTEE_GARDE_ENTIERE if repli is None else PORTEE_REPLI_SEUL
    if portees != {attendue}:
        raise ControleQuatrePorteeAutre()


def _lire_piece(chemin, empreinte, classe_refus) -> bytes:
    """v3 : les octets d'une pièce, lus une seule fois, rendus seulement si leur empreinte est l'attendue."""
    if chemin is None or not est_empreinte(empreinte):
        raise classe_refus()
    garde_chemins([chemin])
    try:
        octets = Path(chemin).read_bytes()
    except OSError:
        raise classe_refus() from None
    if sha256_octets(octets) != empreinte:
        raise classe_refus()
    return octets


def _verifier_piece(chemin, empreinte, classe_refus) -> str:
    _lire_piece(chemin, empreinte, classe_refus)
    return empreinte


def _temoins_de_la_banque(chemin) -> tuple:
    try:
        octets = Path(chemin).read_bytes()
        objet = json.loads(octets.decode("utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        raise BanqueIllisible() from None
    if not isinstance(objet, dict) or not isinstance(objet.get("temoins"), list) or not objet["temoins"]:
        raise BanqueIllisible()
    temoins, vus = [], set()
    for t in objet["temoins"]:
        if not isinstance(t, dict) or not isinstance(t.get("contenu"), dict):
            raise BanqueIllisible()
        i = t.get("identifiant_interne")
        if not isinstance(i, str) or not IDENTIFIANT_TEMOIN.match(i) or i in vus:
            raise BanqueIllisible()
        vus.add(i)
        temoins.append((i, t["contenu"]))
    return temoins, sha256_octets(octets)


def _bardeaux_v2(entree_v2: EntreeV2) -> tuple:
    octets = entree_v2.chemin.read_bytes()
    if sha256_octets(octets) != entree_v2.empreinte:
        raise EmpreinteTemoinsV2Autre()
    objet = json.loads(octets.decode("utf-8"))
    temoins = objet.get("temoins") if isinstance(objet, dict) else None
    if not isinstance(temoins, list) or len(temoins) != entree_v2.compte:
        raise CompteTemoinsV2Autre()
    ens = set()
    for t in temoins:
        for s in textes_de(t):
            ens |= bardeaux(s)
    return ens, entree_v2.empreinte


def bardeaux_communs(temoins: list, reference: set) -> dict:
    """{identifiant du témoin : nombre de bardeaux distincts communs avec la référence}, pour les seuls témoins refusés."""
    refuses = {}
    for i, contenu in temoins:
        b = set()
        for s in textes_de(contenu):
            b |= bardeaux(s)
        n = len(b & reference)
        if n:
            refuses[i] = n
    return refuses


def jouer_la_garde(banque, sortie, controle_4, empreinte_controle_4, mot_de_la_mere=None, repli=None,
                   piece_repli=None, empreinte_piece_repli=None, entree_cartes=None, entree_v2=None,
                   lieu_journal=None, programme=None) -> dict:
    """La garde, une exécution. Rend le rapport (liste fermée), écrit et scellé dans `sortie` quand c'est possible. Toute
    exception est attrapée : seuls son nom de classe et son lieu sortent. v2 : le journal des rejeux n'est plus un argument
    (constantes, `LieuDuJournal`) ; `programme` : l'empreinte de ce programme, calculée une fois par l'appelant."""
    r = {"decision": "garde non jouée", "empreinte_programme": programme or programme_sha256()}
    ids = frozenset()
    jr, rang, ouvert, sortie_prete = None, None, False, False
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            entree_cartes = entree_cartes or EntreeCartes.production()
            entree_v2 = entree_v2 or EntreeV2.production()
            lieu_journal = lieu_journal or LieuDuJournal.production()
            journal = lieu_journal.journal
            garde_chemins([banque, journal, lieu_journal.manifeste, sortie, controle_4, piece_repli])
            sortie = Path(sortie)
            if sortie.exists():
                raise SortieExistante()
            sortie.mkdir(parents=False)
            sortie_prete = True
            exiger_manifeste_du_journal(lieu_journal)                     # v2 : manifeste de création exigé
            jr = JournalRejeux(journal)                                   # absent ou illisible : refus avant ouverture
            r["nombre_de_rejeux"] = max(0, jr.ouvertures - 1)
            if repli is not None:
                if repli not in DECLENCHEURS_REPLI:
                    raise ReplisHorsDeclencheur()
                _verifier_piece(piece_repli, empreinte_piece_repli, PieceDuReplisAbsenteOuFausse)
            exiger_controle_conforme(controle_4, empreinte_controle_4, r["empreinte_programme"],   # (4) : verdict, et
                                     repli)                                                       # v3 : portée
            mot_sha = sha256_octets(mot_de_la_mere.encode("utf-8")) if mot_de_la_mere else None
            if jr.ouvertures >= 1 + MAX_REJEUX_SANS_MOT:                  # ce passage serait le sixième rejeu (ou plus)
                if not mot_sha:
                    raise SixiemeRejeuSansMotDeLaMere()
                if mot_sha in jr.mots_cites():
                    raise MotDeLaMereDejaCite()
            temoins, h_banque = _temoins_de_la_banque(banque)
            ids = frozenset(i for i, _ in temoins)
            r["empreinte_banque"] = h_banque
            ref_v2, h_v2 = _bardeaux_v2(entree_v2)
            r["empreinte_temoins_v2"] = h_v2
            manifeste = {
                "version": VERSION, "geste": "garde de recouvrement", "horodatage_utc": horodatage(),
                "programme_sha256": r["empreinte_programme"], "commit_du_depot": commit_du_depot(), "versions": versions(),
                "graines": "aucune (la garde ne tire rien)",
                "entree_des_cartes": {"nature": entree_cartes.nature, "chemin": str(entree_cartes.chemin),
                                      "empreinte_attendue": entree_cartes.empreinte, "compte_attendu": entree_cartes.compte},
                "seconde_entree": {"chemin": str(entree_v2.chemin), "empreinte": h_v2, "compte": entree_v2.compte},
                "banque": {"chemin": str(Path(banque).resolve()), "empreinte": h_banque, "temoins": len(temoins)},
                "journal_des_rejeux": {"chemin": str(journal), "manifeste_de_creation": str(lieu_journal.manifeste),
                                       "nature": lieu_journal.nature, "ouvertures_lues": jr.ouvertures,
                                       "rejeux_lus": max(0, jr.ouvertures - 1)},
                "ce_passage": {"rang": jr.ouvertures + 1, "rejeu": jr.ouvertures},
                "controle_de_la_condition_4": {"chemin": str(Path(controle_4).resolve()), "empreinte": empreinte_controle_4},
                "mot_de_la_mere": mot_de_la_mere,
                "repli": None if repli is None else {
                    "cause": repli, "piece": str(Path(piece_repli).resolve()), "empreinte_piece": empreinte_piece_repli,
                    "ecart": "garde jouée sur les sept cartes nommées au lieu des 94, par ce déclencheur"},
                "note": "manifeste écrit avant l'ouverture du fichier des cartes : rien n'y vient de ce fichier"}
            ecrire_scelle(sortie / "manifeste-garde.json", manifeste)
            rang = jr.ouvertures + 1
            jr.ajouter({"type": "ouverture", "rang": rang, "rejeu": rang - 1, "horodatage_utc": horodatage(),
                        "empreinte_banque": h_banque, "empreinte_programme": r["empreinte_programme"],
                        "mot_de_la_mere_sha256": mot_sha, "repli": repli, "nature_entree": entree_cartes.nature})
            r["nombre_de_rejeux"] = rang - 1
            ouvert = True
            octets = entree_cartes.lire_octets()                         # la seule ouverture du fichier des cartes
            r["empreinte_fichier_cartes"] = sha256_octets(octets)
            if r["empreinte_fichier_cartes"] != entree_cartes.empreinte:
                raise EmpreinteCartesAutre()                             # ni garde ni repli
            cartes = cartes_du_fichier(octets)                           # meta retiré au chargement
            del octets
            if entree_cartes.provoquer is not None:
                for _i, c in cartes:
                    entree_cartes.provoquer(c)
            if repli is not None:
                retenues = cartes_nommees(cartes)
            else:
                if len(cartes) != entree_cartes.compte:
                    raise CompteCartesAutre()                            # avant toute comparaison
                retenues = [c for _i, c in cartes]
            del cartes
            reference = set(ref_v2)
            for c in retenues:
                for s in textes_de(c):
                    reference |= bardeaux(s)
            n_cartes = len(retenues)
            del retenues
            refuses = bardeaux_communs(temoins, reference)
            del reference, ref_v2
            r.update({"cartes_lues": n_cartes, "temoins_compares": len(temoins), "temoins_refuses": len(refuses),
                      "identifiants_temoins_refuses": sorted(refuses), "bardeaux_communs_par_temoin_refuse": refuses,
                      "decision": "banque refusée" if refuses else "banque passée",
                      "repli": None if repli is None else {"mention": MENTION_REPLI, "cause": repli}})
    except BaseException as e:                                           # noqa: BLE001 — condition (5) : tout est attrapé
        lieu = lieu_de(e)
        e.__traceback__ = None
        del e
        for k in ("cartes_lues", "temoins_compares", "temoins_refuses", "identifiants_temoins_refuses",
                  "bardeaux_communs_par_temoin_refuse"):
            r.pop(k, None)
        r["decision"] = "garde non jouée"
        r["exception"] = lieu
        r["repli"] = None if repli not in DECLENCHEURS_REPLI else {"mention": MENTION_REPLI, "cause": repli}
    if ouvert and jr is not None:
        try:
            jr.ajouter({"type": "cloture", "rang": rang, "decision": r["decision"], "cartes_lues": r.get("cartes_lues"),
                        "temoins_compares": r.get("temoins_compares"), "temoins_refuses": r.get("temoins_refuses"),
                        "exception": r.get("exception")})
        except BaseException as e:                                       # noqa: BLE001
            lieu = lieu_de(e)
            e.__traceback__ = None
            del e
            r.update({"decision": "garde non jouée", "exception": lieu})
            for k in ("cartes_lues", "temoins_compares", "temoins_refuses", "identifiants_temoins_refuses",
                      "bardeaux_communs_par_temoin_refuse"):
                r.pop(k, None)
    if sortie_prete:
        try:
            ecrire_rapport_garde(Path(sortie) / "rapport-garde.json", r, ids)
        except BaseException as e:                                       # noqa: BLE001
            lieu = lieu_de(e)
            e.__traceback__ = None
            del e
            r = {k: v for k, v in (("decision", "garde non jouée"), ("empreinte_programme", r["empreinte_programme"]),
                                   ("nombre_de_rejeux", r.get("nombre_de_rejeux")), ("exception", lieu)) if v is not None}
    valider_rapport_garde(r, ids)
    return r


# ================================================================================================================================
# Audit du générateur (l. 266 ; additif 3, § 4.2 : 100 bons contre 80 mauvais)
# ================================================================================================================================


NOMS_TRAITS_PRESENTATION = (["longueur_totale"] + [f"longueur:{c}" for c in CHAMPS_FICHE]
                            + [f"phrases:{c}" for c in CHAMPS_FICHE] + ["chiffres", "citation"])
NOMS_TRAITS_LETTRE = [f"module:{m}" for m in MOTIFS_MODULES] + ["non_verifie", "predit"]


def phrases(texte: str) -> int:
    t = texte.strip()
    if not t:
        return 0
    return max(1, len(MOTIF_FIN_DE_PHRASE.findall(t)))


def traits_presentation(contenu: dict, citation: bool) -> list:
    v = [float(longueur_fiche(contenu))]
    v += [float(len(contenu.get(c, ""))) for c in CHAMPS_FICHE]
    v += [float(phrases(contenu.get(c, ""))) for c in CHAMPS_FICHE]
    v += [float(sum(ch.isdigit() for c in CHAMPS_FICHE for ch in contenu.get(c, ""))), float(bool(citation))]
    return v


def traits_lettre(contenu: dict) -> list:
    texte = " ".join(contenu.get(c, "") for c in CHAMPS_FICHE)
    n = normaliser(texte)
    v = [float(re.search(r"(?<![0-9a-z])" + m + r"(?![0-9a-z])", n) is not None) for m in MOTIFS_MODULES]
    return v + [float(compte_non_verifie(texte)), float(compte_predit(texte))]


def aire_par_rangs(scores, positifs) -> Fraction:
    """Aire sous la courbe par la statistique de rangs (Mann-Whitney), rangs moyens aux ex æquo, en fraction exacte ;
    positifs = mauvais."""
    np = _numpy()
    s = np.asarray(scores, dtype=float)
    y = np.asarray(positifs, dtype=bool)
    n1, n0 = int(y.sum()), int((~y).sum())
    if n1 == 0 or n0 == 0:
        raise BancInvalide("aire : une des deux populations est vide")
    ordre = np.argsort(s, kind="mergesort")
    rangs2 = np.empty(len(s), dtype=np.int64)          # rangs doublés (entiers) : début + fin du groupe d'ex æquo
    i = 0
    while i < len(s):
        j = i
        while j + 1 < len(s) and s[ordre[j + 1]] == s[ordre[i]]:
            j += 1
        rangs2[ordre[i:j + 1]] = (i + 1) + (j + 1)
        i = j + 1
    r2 = int(rangs2[y].sum())
    return Fraction(r2 - n1 * (n1 + 1), 2 * n1 * n0)


def plis_stratifies(y, rng, k: int = N_PLIS):
    np = _numpy()
    y = np.asarray(y)
    plis = np.empty(len(y), dtype=np.int64)
    for valeur in (0, 1):
        idx = np.flatnonzero(y == valeur)
        perm = idx[rng.permutation(len(idx))]
        plis[perm] = np.arange(len(perm)) % k
    return plis


def logistique(X, y, penalite: float = PENALITE, max_iter: int = MAX_NEWTON) -> tuple:
    """Régression logistique à pénalité quadratique (½ · penalite · ‖w‖², ordonnée non pénalisée), Newton, au plus
    `max_iter` itérations ; arrêt quand le plus grand pas est sous 1e-10. Rend (w, b, itérations, convergé)."""
    np = _numpy()
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    n, d = X.shape
    w, b = np.zeros(d), 0.0
    it, converge = 0, False
    for it in range(1, max_iter + 1):
        z = X @ w + b
        p = 0.5 * (1.0 + np.tanh(0.5 * z))
        s = p * (1.0 - p)
        g = np.concatenate([X.T @ (p - y) + penalite * w, [np.sum(p - y)]])
        H = np.empty((d + 1, d + 1))
        H[:d, :d] = X.T @ (X * s[:, None]) + penalite * np.eye(d)
        H[:d, d] = X.T @ s
        H[d, :d] = H[:d, d]
        H[d, d] = s.sum() + 1e-12
        pas = np.linalg.solve(H, g)
        w = w - pas[:d]
        b = b - pas[d]
        if float(np.max(np.abs(pas))) < 1e-10:
            converge = True
            break
    return w, b, it, converge


def scores_hors_pli(X, y, plis) -> tuple:
    """Prédictions hors pli ; traits centrés et réduits sur les plis d'apprentissage (écart type nul : 1)."""
    np = _numpy()
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    sortie = np.empty(len(y))
    iterations, tous_converges = [], True
    for f in range(int(plis.max()) + 1):
        test = plis == f
        app = ~test
        mu = X[app].mean(axis=0)
        sd = X[app].std(axis=0)
        sd[sd == 0] = 1.0
        w, b, it, conv = logistique((X[app] - mu) / sd, y[app])
        sortie[test] = ((X[test] - mu) / sd) @ w + b
        iterations.append(it)
        tous_converges = tous_converges and conv
    return sortie, iterations, tous_converges


class ServiceAudit:
    """Service injecté : `entree_une_fiche` et `lire_verdict` (les vraies fonctions de `juges_croises_v53.py` en mode réel,
    par le code d'appel v4 ; des fonctions factices dans les essais), la consigne figée, les items et les étiquettes
    interdites. L'appel est celui du code d'appel v4 : `entree_une_fiche(consigne, {"contenu": contenu}, interdites,
    identifiant_servi=opaque)`."""

    def __init__(self, *, nature, entree_une_fiche, lire_verdict, consigne, items, interdites):
        if nature not in ("essai", "reel"):
            raise ValueError("nature : « essai » ou « reel »")
        self.nature, self.entree_une_fiche, self.lire_verdict = nature, entree_une_fiche, lire_verdict
        self.consigne, self.items, self.interdites = consigne, list(items), list(interdites)
        self.appels = 0

    def servir(self, contenu: dict, opaque: str) -> str:
        self.appels += 1
        return self.entree_une_fiche(self.consigne, {"contenu": contenu}, self.interdites, identifiant_servi=opaque)


def fiche_servie(texte: str) -> dict:
    if MARQUE_FICHE not in texte:
        raise BancInvalide("fiche introuvable dans le texte servi")
    corps = texte.rsplit(MARQUE_FICHE, 1)[1].rsplit("\n```", 1)[0]
    d = json.loads(corps)
    d.pop("identifiant", None)
    return d


def juger_scripte(genre: str, fiche: dict, temoin: dict, items, medianes: dict) -> dict:
    """Juges scriptés de la liste d'arrêt : parfait (vérité plantée), longueur (notable si la fiche servie est plus longue
    que la médiane de la banque), champ lu (chaque item vrai si son champ lu est plus long que la médiane de ce champ),
    citation (notable si aucune citation : la citation de construction du témoin reconnu par son contenu)."""
    if genre == "parfait":
        return {k: not (temoin["classe"] == "mauvais" and k == temoin["item"]) for k in items}
    if genre == "longueur":
        v = longueur_fiche(fiche) > medianes["longueur"]
        return {k: v for k in items}
    if genre == "champ_lu":
        return {k: (len(fiche.get(CHAMP_LU[k], "")) > medianes[k]) if k in CHAMP_LU else True for k in items}
    if genre == "citation":
        v = not temoin["citation"]
        return {k: v for k in items}
    raise ValueError("juge scripté inconnu")


def jouer_juges_de_surface(banque: list, service: ServiceAudit) -> dict:
    """Chaque juge scripté lit chaque témoin, servi par la fonction de service ; la réponse est lue par `lire_verdict`.
    Erreur équilibrée contre la vérité plantée."""
    items = service.items
    medianes = {"longueur": statistics.median(longueur_fiche(t["contenu"]) for t in banque)}
    for k, c in CHAMP_LU.items():
        medianes[k] = statistics.median(len(t["contenu"].get(c, "")) for t in banque)
    par_contenu = {json.dumps(t["contenu"], sort_keys=True, ensure_ascii=False): t for t in banque}
    sortie = {}
    servis = set()
    for genre in ("parfait", "longueur", "champ_lu", "citation"):
        vr = fa = 0
        n_bons = n_mauvais = 0
        for t in banque:
            graine = 0
            while True:
                opaque = "F" + sha256_octets(f"audit-ligne-3|{genre}|{t['identifiant_interne']}|{graine}"
                                             .encode("utf-8"))[:5]
                if opaque not in servis:
                    break
                graine += 1
            servis.add(opaque)
            texte = service.servir(t["contenu"], opaque)
            fiche = fiche_servie(texte)
            if fiche != t["contenu"]:
                raise BancInvalide("la fonction de service a changé le contenu du témoin")
            reconnu = par_contenu.get(json.dumps(fiche, sort_keys=True, ensure_ascii=False))
            its = juger_scripte(genre, fiche, reconnu, items, medianes)
            reponse = "```json\n" + json.dumps({"items": its, "note": "juge scripté"}, ensure_ascii=False) + "\n```"
            v = service.lire_verdict(reponse, items)
            if v is None or not isinstance(v.get("items"), dict):
                raise BancInvalide("verdict d'un juge scripté illisible par lire_verdict")
            notable = all(bool(v["items"].get(k)) for k in items)
            if t["classe"] == "bon":
                n_bons += 1
                vr += not notable
            else:
                n_mauvais += 1
                fa += notable
        erreur = (Fraction(vr, n_bons) + Fraction(fa, n_mauvais)) / 2
        sortie[genre] = {"vrais_rejetes": vr, "bons": n_bons, "faux_acceptes": fa, "mauvais": n_mauvais,
                         "erreur_equilibree_exacte": str(erreur), "erreur_equilibree": float(erreur)}
    if Fraction(sortie["parfait"]["erreur_equilibree_exacte"]) != 0:
        raise BancInvalide("juge parfait en erreur : faute du banc")
    for genre in ("longueur", "champ_lu", "citation"):
        e = Fraction(sortie[genre]["erreur_equilibree_exacte"])
        sortie[genre]["dans_la_bande"] = BANDE_JUGES_SURFACE[0] <= e <= BANDE_JUGES_SURFACE[1]
    sortie["medianes"] = medianes
    return sortie


def auditer(banque: list, ctx: Contexte, service: ServiceAudit) -> dict:
    np = _numpy()
    y = np.array([t["classe"] == "mauvais" for t in banque], dtype=float)
    Xp = np.array([traits_presentation(t["contenu"], t["citation"]) for t in banque])
    Xl = np.array([traits_lettre(t["contenu"]) for t in banque])
    Xa = np.hstack([Xp, Xl])
    plis = plis_stratifies(y, ctx.rng("plis-de-l-audit", audit=True))
    sp, it_p, conv_p = scores_hors_pli(Xp, y, plis)
    sa, it_a, conv_a = scores_hors_pli(Xa, y, plis)
    aire_p, aire_a = aire_par_rangs(sp, y), aire_par_rangs(sa, y)
    lettre = {}
    n_mod = Xl[:, :len(MOTIFS_MODULES)].sum(axis=1)
    for nom, colonne, exclu in (("modules_distincts", n_mod, "module_nomme"),
                                ("non_verifie", Xl[:, len(MOTIFS_MODULES)], "reserves_tenues"),
                                ("predit", Xl[:, len(MOTIFS_MODULES) + 1], "reserves_tenues")):
        garde = np.array([t["classe"] == "bon" or t["item"] != exclu for t in banque])
        a = aire_par_rangs(colonne[garde], y[garde])
        lettre[nom] = {"item_exclu": exclu, "bons": int((garde & (y == 0)).sum()), "mauvais": int((garde & (y == 1)).sum()),
                       "aire_exacte": str(a), "aire": float(a), "dans_la_bande": BANDE_LETTRE[0] <= a <= BANDE_LETTRE[1]}
    juges = jouer_juges_de_surface(banque, service)
    refus = []
    if aire_p > SEUIL_AIRE_QUI_DECIDE:
        refus.append("aire qui décide au-dessus de 0,60")
    refus += [f"trait de la lettre « {k} » hors de la bande 0,35–0,65" for k, v in lettre.items() if not v["dans_la_bande"]]
    refus += [f"juge scripté « {g} » hors de [0,40 ; 0,60]" for g in ("longueur", "champ_lu", "citation")
              if not juges[g]["dans_la_bande"]]
    return {"version": VERSION, "decision": "banque refusée" if refus else "banque passée", "motifs_de_refus": refus,
            "aire_qui_decide": {"traits": NOMS_TRAITS_PRESENTATION, "aire_exacte": str(aire_p), "aire": float(aire_p),
                                "seuil": "0,60 (refus au-dessus)", "iterations_par_pli": it_p, "convergence": conv_p},
            "aire_a_tous_les_traits": {"traits": NOMS_TRAITS_PRESENTATION + NOMS_TRAITS_LETTRE, "aire_exacte": str(aire_a),
                                       "aire": float(aire_a), "seuil": "aucun (rapportée)", "iterations_par_pli": it_a,
                                       "convergence": conv_a},
            "traits_de_la_lettre": lettre, "juges_scriptes_de_surface": juges,
            "plis": {"nombre": N_PLIS, "effectifs": [[int(((plis == f) & (y == v)).sum()) for v in (0, 1)]
                                                      for f in range(N_PLIS)]},
            "regression": {"penalite": PENALITE, "forme": "½ · 1,0 · ‖w‖², ordonnée non pénalisée", "newton_max": MAX_NEWTON},
            "service": {"nature": service.nature, "appels": service.appels}}


# ================================================================================================================================
# Pièces réelles (v2 : la voie réelle de l'audit est exercée sur la banque factice par un essai, sans réseau ni clé, M6)
# ================================================================================================================================


def lire_configuration() -> dict:
    octets = lire_par_empreinte(DEPOT / CONFIGURATION[0], CONFIGURATION[1], "configuration des juges")
    return json.loads(octets.decode("utf-8"))


def charger_code_appel_v4():
    octets = lire_par_empreinte(DEPOT / CODE_APPEL_V4[0], CODE_APPEL_V4[1], "code d'appel v4")
    nom = "epreuve_juges_reels_ligne_3_v4_pour_le_generateur"
    m = types.ModuleType(nom)
    m.__file__ = str(DEPOT / CODE_APPEL_V4[0])
    sys.modules[nom] = m
    exec(compile(octets, m.__file__, "exec"), m.__dict__)
    return m


def construire_service_reel(orchestrateur=None) -> ServiceAudit:
    """La vraie fonction de service : `charger_service_des_juges` du code d'appel v4 (082d19d6…), qui vérifie l'empreinte
    de chaque module de l'orchestrateur avant tout import. v2 (T2, M6) : le clone de l'organisme est présent
    (`/home/user/lciric/ideation-organism`, commit a41b7b50…) ; cette voie est exercée par un essai sur la banque factice :
    fonctions pures, aucun réseau, aucune clé, aucune écriture dans le clone."""
    v4 = charger_code_appel_v4()
    f = v4.charger_service_des_juges(Path(orchestrateur) if orchestrateur else v4.ORCHESTRATEUR)
    consigne = lire_par_empreinte(DEPOT / CONSIGNE_JUGE[0], CONSIGNE_JUGE[1], "consigne figée du juge").decode("utf-8")
    conf = lire_configuration()
    return ServiceAudit(nature="reel", entree_une_fiche=f["entree_une_fiche"], lire_verdict=f["lire_verdict"],
                        consigne=consigne, items=conf["items_juge"], interdites=conf["etiquettes_interdites_fixes"])


# ================================================================================================================================
# Gestes en ligne de commande
# ================================================================================================================================


def manifeste_de_base(geste: str, ctx, arguments: dict) -> dict:
    return {"version": VERSION, "geste": geste, "horodatage_utc": horodatage(), "programme_sha256": programme_sha256(),
            "configuration": arguments, "configuration_sha256": sha256_octets(json_octets(arguments)),
            "versions": versions(), "graines": ctx.decrire() if ctx else "aucune",
            "commit_du_depot": commit_du_depot()}


def geste_composer(fragments, empreinte_fragments, sortie, ctx: Contexte, interdites, items=ITEMS) -> dict:
    garde_chemins([fragments, sortie])
    if tuple(items) != ITEMS:
        raise Refus("items de la configuration différents des cinq items de la consigne, dans leur ordre")
    sortie = Path(sortie)
    if sortie.exists():
        raise Refus("dossier de sortie déjà présent : une exécution par dossier")
    fr, h = charger_fragments(fragments, empreinte_fragments, interdites, items)
    banque, journal = composer(fr, ctx, items, interdites)
    verifier_proportions(banque, journal)
    sortie.mkdir(parents=False)
    communs = fragments_communs(journal)                                  # v2, M5 : rapporté
    usages = {}
    for j in journal:
        for fid in j["fragments"].values():
            usages[fid] = usages.get(fid, 0) + 1
    args = {"fragments": str(Path(fragments).resolve()), "fragments_sha256": h, "sortie": str(sortie.resolve()),
            "n_temoins": N_TEMOINS, "max_tirages": MAX_TIRAGES, "bandes": [LONGUEUR_MIN, LONGUEUR_MAX, N_BANDES]}
    empreintes = {}
    empreintes["banque-temoins-ligne-3-v1.json"] = ecrire_scelle(sortie / "banque-temoins-ligne-3-v1.json", {
        "version": VERSION, "fragments_sha256": h, "items": list(items), "temoins": banque})
    empreintes["journal-construction-ligne-3-v1.json"] = ecrire_scelle(sortie / "journal-construction-ligne-3-v1.json", {
        "version": VERSION, "fragments_sha256": h, "verite": "la construction : classe, item, niveau, citation, piège, "
        "fragments employés par identifiant", "temoins": journal, "usages_par_fragment": usages,
        "fragments_jamais_employes": sorted(set(fr["par_id"]) - set(usages)), "comptes": comptes_de_la_banque(banque),
        "fragments_communs_entre_deux_temoins": communs, "contenus_identiques": 0})
    empreintes["partage-ligne-3-v1.json"] = ecrire_scelle(sortie / "partage-ligne-3-v1.json", {
        "version": VERSION, "strates": "classe ; bons : citation, puis type ; mauvais : item, niveau, citation",
        "lecture": sorted(t["identifiant_interne"] for t in banque if t["moitie"] == "lecture"),
        "etalonnage": sorted(t["identifiant_interne"] for t in banque if t["moitie"] == "etalonnage"),
        "comptes": partage_par_strate(journal)})
    m = manifeste_de_base("composition et partage de la banque", ctx, args)
    m["sorties"] = empreintes
    m["fragments_communs_entre_deux_temoins"] = communs
    ecrire_scelle(sortie / "manifeste-composition.json", m)
    return {"banque": banque, "journal": journal, "empreintes": empreintes, "manifeste": m, "communs": communs}


def partage_par_strate(journal: list) -> list:
    d = {}
    for j in journal:
        cle = cle_de_strate(j)
        e = d.setdefault(cle, {"classe": j["classe"], "type_bon": j["type_bon"], "item": j["item"], "niveau": j["niveau"],
                               "citation": j["citation"], "lecture": 0, "etalonnage": 0})
        e[j["moitie"]] += 1
    return [d[k] for k in sorted(d)]


def lire_banque_ecrite(chemin, empreinte) -> list:
    octets = lire_par_empreinte(chemin, empreinte, "banque de témoins")
    objet = json.loads(octets.decode("utf-8"))
    banque = objet["temoins"]
    if len(banque) != N_TEMOINS:
        raise Refus("banque : 200 témoins attendus")
    return banque


def geste_auditer(banque_chemin, empreinte_banque, sortie, ctx: Contexte, service: ServiceAudit) -> dict:
    garde_chemins([banque_chemin, sortie])
    sortie = Path(sortie)
    if sortie.exists():
        raise Refus("dossier de sortie déjà présent : une exécution par dossier")
    banque = lire_banque_ecrite(banque_chemin, empreinte_banque)
    rapport = auditer(banque, ctx, service)
    sortie.mkdir(parents=False)
    rapport["banque_sha256"] = empreinte_banque
    h = ecrire_scelle(sortie / "rapport-audit-ligne-3-v1.json", rapport)
    m = manifeste_de_base("audit du générateur", ctx, {"banque": str(Path(banque_chemin).resolve()),
                                                      "banque_sha256": empreinte_banque, "sortie": str(sortie.resolve())})
    m["sorties"] = {"rapport-audit-ligne-3-v1.json": h}
    ecrire_scelle(sortie / "manifeste-audit.json", m)
    return rapport


def _argument(argv, nom, obligatoire=True):
    if nom in argv:
        i = argv.index(nom)
        if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
            return argv[i + 1]
    if obligatoire:
        raise Refus(f"argument {nom} exigé")
    return None


def lire_arguments_garde(reste: list) -> dict:
    """v2 : arguments de la garde par paires, chacun dans `ARGUMENTS_GARDE`, une fois ; obligatoires présents ; tout autre
    argument (dont un chemin de journal) est un refus."""
    if len(reste) % 2:
        raise ArgumentHorsListe()
    valeurs = {}
    for k in range(0, len(reste), 2):
        nom, valeur = reste[k], reste[k + 1]
        if nom not in ARGUMENTS_GARDE or nom in valeurs or not isinstance(valeur, str):
            raise ArgumentHorsListe()
        valeurs[nom] = valeur
    if any(oblig and nom not in valeurs for nom, oblig in ARGUMENTS_GARDE.items()):
        raise ArgumentHorsListe()
    return valeurs


def _sortie_de_secours(e: BaseException) -> int:
    """Dernier recours de la garde : nom de classe et lieu seulement, écrits sans rien recalculer ; aucune trace brute."""
    try:
        lieu = lieu_de(e)
    except BaseException:                                                # noqa: BLE001
        lieu = {"classe": "LieuIllisible", "fichier": NOM_DU_PROGRAMME, "ligne": None}
    try:
        r = {"decision": "garde non jouée", "exception": lieu}
        valider_rapport_garde(r, exiger_programme=False)
        os.write(1, (json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8"))
    except BaseException:                                                # noqa: BLE001 — rien d'autre ne sort
        pass
    return 5


def principal_garde(argv: list, entree_cartes=None, entree_v2=None, lieu_journal=None) -> int:
    """v2, R6 du contrôle : tout le geste `garde`, lecture des arguments et sortie standard comprises, sous `try`."""
    try:
        programme = programme_sha256()
        a = lire_arguments_garde(list(argv[1:]))
        r = jouer_la_garde(a["--banque"], a["--sortie"], a["--controle-4"], a["--empreinte-controle-4"],
                           mot_de_la_mere=a.get("--mot-de-la-mere"), repli=a.get("--repli"),
                           piece_repli=a.get("--piece-repli"), empreinte_piece_repli=a.get("--empreinte-piece-repli"),
                           entree_cartes=entree_cartes, entree_v2=entree_v2, lieu_journal=lieu_journal,
                           programme=programme)
        texte = json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n"
        sys.stdout.write(texte)
        sys.stdout.flush()
        return {"banque passée": 0, "banque refusée": 4}.get(r["decision"], 5)
    except BaseException as e:                                           # noqa: BLE001 — condition (5)
        code = _sortie_de_secours(e)
        e.__traceback__ = None
        del e
        return code


def principal(argv=None, entree_cartes=None, entree_v2=None, lieu_journal=None) -> int:
    """Ligne de commande. `entree_cartes`, `entree_v2` et `lieu_journal` : voie d'essai explicite (appel en Python
    seulement) ; la ligne de commande ne les expose pas et passe toujours par les constantes."""
    try:
        argv = sys.argv[1:] if argv is None else list(argv)
        geste = argv[0] if argv else None
    except BaseException:                                                # noqa: BLE001
        return 2
    if geste == "garde":
        return principal_garde(argv, entree_cartes, entree_v2, lieu_journal)
    try:
        if geste == "creer-journal-rejeux":
            try:                                                         # v3 : tout refus nommé, aucune trace brute
                if len(argv) != 1:                                       # v2 : aucun chemin ; les constantes seules
                    raise ArgumentHorsListe()
                creer_journal_rejeux(lieu_journal)
            except BaseException as e:                                   # noqa: BLE001
                lieu = lieu_de(e)
                e.__traceback__ = None
                del e
                print(json.dumps({"refus": lieu["classe"], "ligne": lieu["ligne"]}, ensure_ascii=False), file=sys.stderr)
                return 2
            print(json.dumps({"journal": "créé vide"}, ensure_ascii=False))
            return 0
        autorisation = Autorisation(_argument(argv, "--autorisation-additif"), _argument(argv, "--empreinte-additif"))
        ctx = Contexte("decisif", autorisation)
        if geste == "composer":
            conf = lire_configuration()
            res = geste_composer(_argument(argv, "--fragments"), _argument(argv, "--empreinte-fragments"),
                                 _argument(argv, "--sortie"), ctx, conf["etiquettes_interdites_fixes"],
                                 tuple(conf["items_juge"]))
            print(json.dumps({"sorties": res["empreintes"]}, ensure_ascii=False))
            return 0
        if geste == "auditer":
            service = construire_service_reel(_argument(argv, "--orchestrateur", False))
            r = geste_auditer(_argument(argv, "--banque"), _argument(argv, "--empreinte-banque"),
                              _argument(argv, "--sortie"), ctx, service)
            print(json.dumps({"decision": r["decision"], "motifs_de_refus": r["motifs_de_refus"]}, ensure_ascii=False))
            return 0 if r["decision"] == "banque passée" else 4
    except FragmentsRefuses as e:
        print(json.dumps({"refus": str(e), "fautes": e.fautes}, ensure_ascii=False), file=sys.stderr)
        return 2
    except (Refus, RefusGarde) as e:
        print(json.dumps({"refus": type(e).__name__, "motif": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print("usage : composer | creer-journal-rejeux | garde | auditer (voir le rapport du développeur, § commandes)",
          file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(principal())
