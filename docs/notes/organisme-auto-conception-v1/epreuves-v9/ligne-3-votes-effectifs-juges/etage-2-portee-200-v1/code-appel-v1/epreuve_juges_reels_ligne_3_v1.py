#!/usr/bin/env python3
"""Épreuve des juges réels — ligne 3 de l'organisme v9 (votes effectifs des juges croisés), étage 2 à 200 témoins — v1.

Plan de code : annexe A du texte v7 (`preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, 4e3680d9…), ligne 561 ;
section « Étage 2 » (l. 243 à 305), « Liste d'arrêt » (l. 352 et suivantes), « Plafond : arrêt dur par compteur » (l. 380
et suivantes) ; portée à 200 par l'additif 3 v3 (71b7a876…, § 4.1, § 4.2, § 7) : P 4, A 400, B 600, total 1 004 ;
plafond d'arrêt 88,36 USD ; réserve 0,60 USD. Écrit par le développeur, modèle O ; jamais lancé en mode réel par lui.

Ce que fait ce programme, et rien d'autre :
- il sert chaque témoin aux deux juges de la configuration de la course v9 par les fonctions de `juges_croises_v53.py`
  (`entree_une_fiche`, `lire_verdict`), importées depuis le clone de l'orchestrateur à son chemin, après vérification de
  l'empreinte de chaque module importé (compilées depuis les octets vérifiés eux-mêmes) ; une session neuve par appel, une
  seule carte servie, un identifiant opaque neuf par rendu, jamais l'identifiant interne ;
- il joue les blocs P (plomberie : 2 témoins de la version 2, 4 appels), A (chaque juge une fois sur les 200 témoins,
  400 appels) et B (entrelacé par témoin, moitié « lecture » d'abord : une lecture de plus du juge Opus, deux du juge
  Argon, 600 appels) ; ordre des témoins tiré dans chaque bloc par `numpy.random.SeedSequence(2026111935,
  spawn_key=(clé,))`, table des clés gelée ci-dessous (`CLES_TACHES`) ;
- il tient le compteur d'arrêt : journal à ajout seul sur disque ; engagement de 0,60 USD écrit avant chaque envoi ; aucun
  envoi si le cumul compté plus 0,60 dépasse 88,36 USD (`PLAFOND_C`, seule constante du plafond) ; règlement au coût
  relevé ; envoi refusé, coupé, en erreur ou sans coût lisible compté 0,60 ; rejeu unique d'un envoi refusé, coupé ou en
  erreur, compté lui aussi ; verdict lisible sans coût lisible gardé, non rejoué, compté 0,60 ; engagement sans règlement
  compté 0,60 à la relance ; coût relevé au-dessus de 0,60 : arrêt ; relance qui relit le journal, jamais de remise à
  zéro ; aucun repli, aucune bascule de modèle ; toutes les sommes en fractions exactes, aucun flottant dans une
  comparaison de seuil ;
- gardes : ligne de GO, modèle servi, réponses identiques, verdicts de la v9, vérité non servie, identifiant opaque neuf,
  moyen du plafond de session, plomberie ; juge « non mesuré » au-delà de 10 % d'absents, ρ′ « non mesuré » au-delà de la
  moitié de répétitions identiques ;
- il dépose, scellés (compagnon `.sha256`), les verdicts par moitié, l'état des juges et le rapport d'exécution ; il garde
  les réponses brutes et les entrées servies ; un manifeste par exécution (règle R9).

Moyen du plafond de session de 0,60 USD à chaque appel (texte l. 382 (i)) : `exiger_moyen_du_plafond_de_session`, appelée
avant tout envoi. Juge de fournisseur « commande externe » (Argon) : **borne de jetons produits** — l'adaptateur passe
`PLAFOND_SESSION_USD` = 0,6 à la commande d'Argon (`AdaptateurCommandeExterne.environnement_commande`), qui fixe
`maxOutputTokens` au reste du plafond moins la provision de pensée et refuse sans envoi si le pire cas dépasse (code 4) ;
contrôlé ici sur l'environnement que l'adaptateur passerait. Juge du kit (Opus) : **plafond du service** — l'option
`max_budget_usd` = 0,6 du kit, posée par `construire_options` (et `max_turns` = 1, aucun outil) ; contrôlée ici sur les
options que l'adaptateur construirait. Tout autre adaptateur : refus, pas de départ. Chaque envoi passe `budget_usd` =
0,6 (`budget_de_session`). Un coût relevé au-dessus de 0,60 arrête le programme.

Modes. Mode « essai » : `executer(…, service=…)` avec un service dont la nature est « essai » et des adaptateurs factices
injectés (`AdaptateurFactice`) : aucun réseau, aucune clé lue, aucun relais lancé ; les essais sont
`essais_epreuve_juges_reels_ligne_3_v1.py`. Mode réel (`--reel`) : jamais lancé par l'auteur ; il refuse de partir sans
`--go-id` valide au registre lu sur `origin/main`, sans relais déclarés (déclaration scellée, empreinte en argument) et
sans la banque scellée (empreinte attendue en argument), avant toute construction de service.

Codes : 0 exécution écrite (lire le rapport) ; 2 refus avant tout envoi ; 3 arrêt écrit (plafond, plomberie, coût).
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import importlib.util
import json
import math
import os
import platform
import re
import subprocess
import sys
import types
import unicodedata
from decimal import Decimal, ROUND_HALF_EVEN
from fractions import Fraction
from pathlib import Path

VERSION = "epreuve_juges_reels_ligne_3_v1"

# --- plafond (une seule constante, égale à la ligne de GO lue) -------------------------------------------------------------
PLAFOND_C = 8836            # 88,36 USD en centimes entiers : GO-2026-11-20-26 ; additif 3 v3, § 4.2
SESSION_C = 60              # 0,60 USD : plafond de session d'un appel de juge ; engagement ; coût compté d'un envoi refusé
PLAFOND = Fraction(PLAFOND_C, 100)
SESSION = Fraction(SESSION_C, 100)

# --- plan --------------------------------------------------------------------------------------------------------------------
N_TEMOINS = 200
N_PLOMBERIE = 2
JUGES = ("juge-opus", "juge-argon")                 # étiquettes de la configuration de la course v9 ; ordre dans un témoin
REPETITIONS_B = {"juge-opus": 1, "juge-argon": 2}   # rendus de plus au bloc B
MOITIES = ("lecture", "etalonnage")
CLASSES = ("bon", "mauvais")
NIVEAUX = ("declare", "net", "discret")
MAX_ESSAIS = 2                                      # l'envoi et son rejeu unique

# Tarif des cartes de la v9 par appel, en fractions exactes : tarif moyen par appel de chaque juge à la course v9 (manifeste
# de fin, 28bc36df…), comme le calcul v2 des conditions du plafond (`tarifs`, facteur « haut » = 1). Vérifié par les essais.
TARIF_DES_CARTES = {"juge-opus": Fraction(3431597, 47000000), "juge-argon": Fraction(51253, 2000000)}
FACTEUR_ARRET_PLOMBERIE = 3                         # texte l. 378 : « au-delà de trois fois le tarif des cartes »
SEUIL_ABSENTS = Fraction(1, 10)                     # au-delà : juge « non mesuré »
SEUIL_IDENTIQUES = Fraction(1, 2)                   # au-delà : ρ′ du juge « non mesuré »

# --- graines (règle R9) ------------------------------------------------------------------------------------------------------
RACINE_ORDRE = 2026111935                           # texte l. 303 : « ordre des appels »
CLES_TACHES = {"ordre-bloc-P": 1, "ordre-bloc-A": 2, "ordre-bloc-B": 3, "identifiants-opaques": 4}
REGLE_DES_GRAINES = "numpy.random.SeedSequence(racine, spawn_key=(clé,)) ; numpy.random.default_rng ; numpy ≥ 1.25"

# --- pièces épinglées --------------------------------------------------------------------------------------------------------
DEPOT = Path("/home/user/controle-ia-travail")
ORCHESTRATEUR = Path("/home/user/lciric/ideation-organism/orchestrator")
COMMIT_ORCHESTRATEUR = "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb"
# `juges_croises_v53.py` et ce qu'il importe (fiches_v53, outils ; fiches_v53 importe caviardage), plus le paquet.
MODULES_ORCHESTRATEUR = (
    ("__init__", "pole/__init__.py", "f7341b965ddba1e0fb21b44d9068f59650d5c77e3175f2b6b7ca879219fa5c9b"),
    ("outils", "pole/outils.py", "966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444"),
    ("caviardage", "pole/caviardage.py", "78abfd4731218e20538418608ebebaca3364206ef6d014b7a34829a3c9fd7e85"),
    ("fiches_v53", "pole/fiches_v53.py", "7cfcf8329c66c7a37ceb2992cc96e21aedbfa0a10525467672794090a128eda6"),
    ("juges_croises_v53", "pole/juges_croises_v53.py", "c4c6ab12dc471eef078c116a4205a22d9b498da720ce71e37a0a6edae6c4239b"),
)
PAQUET_PRIVE = "_pole_ligne_3_etage_2_v1"           # nom privé : aucune collision avec un `pole` déjà importé
CONSIGNE_JUGE = ("docs/notes/organisme-auto-conception-v1/course-v1/consigne-juge-auto-conception-v1.md",
                 "b03f33b87150eb67e5e55f3fc093812e5a359ab655362b3033dde561e58b5167")
TEMOINS_V2 = ("docs/notes/organisme-auto-conception-v1/course-v2/temoins-juge-auto-conception-v2.json",
              "84a1e0ea870ecb54c2de8ec5071e689e2ba409b3c97aecb57ab16ef3388439e0")
CONFIGURATION = ("docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json",
                 "3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8")
LANCEUR_V9 = ("scripts/lancer_course_auto_conception_v9.py",
              "1b47c1cf097e4cba290223223655d5ac63707dfeaec032be929930d30fde9b12")
PRECEDENT_V9 = ("scripts/epreuve_temoins_auto_conception_v9.py",
                "5be161fa35e339d171399a3ba2a2c927cd517fba42c745306fd867a4b3e3c69b")
ETAPE = "ligne-3-etage-2"

# --- garde « verdicts de la v9 » : chemins jamais ouverts ----------------------------------------------------------------------
COMPOSANTS_INTERDITS = ("archives-reponses-modeles",)
PREFIXE_COMPOSANT_INTERDIT = "coffre"
RACINES_INTERDITES = (Path("/home/user/sorties-course-auto-conception-v9"),
                      DEPOT / "runs" / "20261119-094145-course-auto-conception-v9")

# --- garde « ligne de GO » ----------------------------------------------------------------------------------------------------
GO_FORME = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
MOTS_PERIMETRE_GO = ("ligne 3", "etage 2")

# --- statuts des adaptateurs de l'orchestrateur -----------------------------------------------------------------------------
STATUTS_TECHNIQUES = ("erreur", "tours_epuises")    # refusé par le relais ou le fournisseur, coupé, en erreur
EVENEMENTS_CHANGEMENT_DE_MODELE = ("assistant.model", "result.model_usage", "resultat.modele_servi",
                                   "commande.modele_servi", "commande.modele_servi_absent", "system.model_fallback",
                                   "system.model_refusal_fallback", "system.model_refusal_no_fallback")


class Refus(RuntimeError):
    """Refus avant tout envoi (ou refus de servir) : rien n'est envoyé, rien n'est compté."""


# --- nombres exacts ----------------------------------------------------------------------------------------------------------


def centimes(x) -> int:
    if isinstance(x, bool) or not isinstance(x, int) or x < 0:
        raise TypeError("un seuil se donne en centimes entiers positifs, jamais en flottant")
    return x


def exacte(x) -> Fraction:
    """Entier ou fraction seulement (garde : jamais un flottant dans un seuil)."""
    if isinstance(x, bool) or not isinstance(x, (int, Fraction)):
        raise TypeError("grandeur exacte attendue (entier ou fraction), jamais un flottant")
    return Fraction(x)


def cout_lisible(x):
    """Coût rendu par un adaptateur en fraction exacte, ou None s'il n'est pas lisible (absent, booléen, non fini, nul ou
    négatif : un appel facturé ne coûte jamais 0). Un flottant est lu par son écriture décimale (`repr`), jamais par sa
    valeur binaire ; une fraction, un entier ou un décimal tels quels."""
    if x is None or isinstance(x, bool):
        return None
    if isinstance(x, Fraction):
        v = x
    elif isinstance(x, int):
        v = Fraction(x)
    elif isinstance(x, Decimal):
        if not x.is_finite():
            return None
        v = Fraction(x)
    elif isinstance(x, float):
        if not math.isfinite(x):
            return None
        v = Fraction(Decimal(repr(x)))
    else:
        return None
    return v if v > 0 else None


FRACTION_ECRITE = re.compile(r"^-?\d+(/\d+)?$")


def lire_fraction(texte) -> Fraction:
    if not isinstance(texte, str) or not FRACTION_ECRITE.match(texte):
        raise ValueError("fraction écrite attendue")
    return Fraction(texte)


def decimal_texte(x, chiffres=4) -> str:
    """Écriture décimale d'une fraction exacte, arrondie au demi pair (pour les rapports seulement, jamais un seuil)."""
    entier = round(exacte(x) * 10 ** chiffres)
    return format(Decimal(entier).scaleb(-chiffres).quantize(Decimal(1).scaleb(-chiffres), rounding=ROUND_HALF_EVEN),
                  f".{chiffres}f")


def budget_de_session() -> float:
    """Le `budget_usd` passé à chaque appel : 0,6 (l'interface des adaptateurs veut un flottant). Garde : son écriture
    décimale vaut exactement le plafond de session ; aucune comparaison de seuil ne se fait sur ce flottant."""
    b = SESSION_C / 100
    if cout_lisible(b) != SESSION:
        raise Refus("plafond de session : le budget passé à l'appel n'est pas 0,60 USD exactement")
    return b


# --- fichiers ---------------------------------------------------------------------------------------------------------------


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_fichier(chemin) -> str:
    return sha256_octets(Path(chemin).read_bytes())


def json_octets(objet) -> bytes:
    return (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def ecrire_scelle(chemin: Path, objet) -> str:
    """Écrit sans jamais écraser (mode exclusif) et pose le compagnon `.sha256` au format de sha256sum (règle R6)."""
    donnees = json_octets(objet)
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = sha256_octets(donnees)
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {Path(chemin).name}\n")
    return h


def ecrire_exclusif(chemin: Path, octets: bytes) -> str:
    with open(chemin, "xb") as f:
        f.write(octets)
    return sha256_octets(octets)


def lire_par_empreinte(chemin: Path, attendue: str, quoi: str) -> bytes:
    try:
        octets = Path(chemin).read_bytes()
    except OSError as e:
        raise Refus(f"{quoi} : illisible ({type(e).__name__})") from None
    if sha256_octets(octets) != attendue:
        raise Refus(f"{quoi} : empreinte différente de l'empreinte attendue")
    return octets


def exiger_compagnon(chemin: Path, attendue: str, quoi: str) -> None:
    compagnon = Path(str(chemin) + ".sha256")
    try:
        mots = compagnon.read_text(encoding="utf-8").split()
    except OSError:
        raise Refus(f"{quoi} : non scellé (compagnon .sha256 absent)") from None
    if not mots or mots[0] != attendue:
        raise Refus(f"{quoi} : compagnon .sha256 différent de l'empreinte attendue")


def normaliser(texte: str) -> str:
    d = unicodedata.normalize("NFD", texte)
    s = "".join(c for c in d if not unicodedata.combining(c))
    return re.sub(r"[^0-9a-z]+", " ", s.lower()).strip()


# --- garde « verdicts de la v9 » ----------------------------------------------------------------------------------------------


def garde_chemins(chemins) -> list:
    """Refuse, avant toute ouverture, tout chemin du coffre de la course v9 ou de l'archive des réponses : composant
    `archives-reponses-modeles`, composant qui commence par « coffre », ou chemin sous une racine interdite. La forme écrite
    est contrôlée d'abord (sans aucun appel au système de fichiers), puis le chemin réel."""
    vus = []
    for c in chemins:
        if c is None:
            continue
        ecrit = os.path.normpath(os.path.abspath(str(c)))
        for forme in (ecrit, None):
            s = ecrit if forme is not None else os.path.realpath(ecrit)
            parts = Path(s).parts
            if any(p in COMPOSANTS_INTERDITS or p.lower().startswith(PREFIXE_COMPOSANT_INTERDIT) for p in parts):
                raise Refus("verdicts de la v9 : chemin du coffre ou de l'archive des réponses passé au programme : refus")
            for r in RACINES_INTERDITES:
                r = os.path.normpath(str(r))
                if s == r or s.startswith(r + os.sep):
                    raise Refus("verdicts de la v9 : chemin sous la sortie ou le run de la course v9 : refus")
        vus.append(ecrit)
    return vus


# --- service des juges : modules de l'orchestrateur, vérifiés puis compilés depuis leurs octets ------------------------------


def charger_service_des_juges(racine: Path = ORCHESTRATEUR) -> dict:
    """Vérifie l'empreinte de chaque module importé (constantes `MODULES_ORCHESTRATEUR`) **avant tout import** ; écart :
    refus nommé. Puis compile et exécute chaque module depuis les octets vérifiés eux-mêmes, sous un nom de paquet privé
    (aucune lecture d'un fichier compilé en cache, aucune collision avec un paquet `pole` déjà importé). Rend les fonctions
    de `juges_croises_v53` (`entree_une_fiche`, `lire_verdict`), `normaliser_texte` et `caviarder`."""
    racine = Path(racine)
    garde_chemins([racine])
    octets = {}
    for nom, rel, attendue in MODULES_ORCHESTRATEUR:
        chemin = racine / rel
        try:
            b = chemin.read_bytes()
        except OSError:
            raise Refus(f"service des juges : module {rel} absent du clone de l'orchestrateur") from None
        if sha256_octets(b) != attendue:
            raise Refus(f"service des juges : module {rel} d'une autre empreinte que celle du texte ({attendue[:8]}…) : "
                        "aucun import")
        octets[nom] = (chemin, b)
    if PAQUET_PRIVE in sys.modules:
        paquet = sys.modules[PAQUET_PRIVE]
        if getattr(paquet, "__empreintes__", None) != {n: a for n, _r, a in MODULES_ORCHESTRATEUR}:
            raise Refus("service des juges : paquet privé déjà chargé avec d'autres empreintes")
    else:
        paquet = types.ModuleType(PAQUET_PRIVE)
        paquet.__path__ = [str(racine / "pole")]
        paquet.__package__ = PAQUET_PRIVE
        paquet.__file__ = str(octets["__init__"][0])
        sys.modules[PAQUET_PRIVE] = paquet
        try:
            exec(compile(octets["__init__"][1], str(octets["__init__"][0]), "exec"), paquet.__dict__)
            for nom, _rel, _a in MODULES_ORCHESTRATEUR[1:]:
                chemin, b = octets[nom]
                m = types.ModuleType(f"{PAQUET_PRIVE}.{nom}")
                m.__package__ = PAQUET_PRIVE
                m.__file__ = str(chemin)
                sys.modules[m.__name__] = m
                exec(compile(b, str(chemin), "exec"), m.__dict__)
                setattr(paquet, nom, m)
        except BaseException:
            for k in [k for k in sys.modules if k == PAQUET_PRIVE or k.startswith(PAQUET_PRIVE + ".")]:
                del sys.modules[k]
            raise
        paquet.__empreintes__ = {n: a for n, _r, a in MODULES_ORCHESTRATEUR}
    jc = sys.modules[f"{PAQUET_PRIVE}.juges_croises_v53"]
    return {"entree_une_fiche": jc.entree_une_fiche, "lire_verdict": jc.lire_verdict,
            "normaliser_texte": sys.modules[f"{PAQUET_PRIVE}.outils"].normaliser_texte,
            "caviarder": sys.modules[f"{PAQUET_PRIVE}.caviardage"].caviarder,
            "version_juges": jc.VERSION, "racine": str(racine), "commit": COMMIT_ORCHESTRATEUR,
            "empreintes": {rel: a for _n, rel, a in MODULES_ORCHESTRATEUR}}


# --- banque de témoins (fichier de données) ----------------------------------------------------------------------------------

CHAMPS_TEMOIN = ("identifiant_interne", "classe", "item", "niveau", "citation", "moitie", "contenu")
IDENTIFIANT_INTERNE = re.compile(r"^[A-Za-z0-9._:-]{1,64}$")
CLES_RESERVEES_CONTENU = ("identifiant", "ident", "meta", "empreinte", "case", "fournisseur", "passe", "origine", "bras",
                          "classe", "temoin", "item", "niveau", "citation", "moitie", "identifiant_interne")


def valider_banque(objet, items, n=N_TEMOINS) -> list:
    """Format de la banque (champs minimaux) : {"temoins": [{identifiant_interne, classe, item, niveau, citation, moitie,
    contenu}]} ; `contenu` = le texte des champs, seul servi. Rend la liste des témoins."""
    if not isinstance(objet, dict) or not isinstance(objet.get("temoins"), list):
        raise Refus("banque : objet {\"temoins\": [...]} attendu")
    temoins, vus = [], set()
    for k, t in enumerate(objet["temoins"]):
        if not isinstance(t, dict):
            raise Refus(f"banque : témoin {k} non objet")
        manquants = [c for c in CHAMPS_TEMOIN if c not in t]
        if manquants:
            raise Refus(f"banque : témoin {k} sans les champs {manquants}")
        i = t["identifiant_interne"]
        if not isinstance(i, str) or not IDENTIFIANT_INTERNE.match(i) or i in vus:
            raise Refus(f"banque : témoin {k} : identifiant interne illisible ou répété")
        vus.add(i)
        if t["classe"] not in CLASSES:
            raise Refus(f"banque : {i} : classe hors de {CLASSES}")
        if t["classe"] == "bon" and (t["item"] is not None or t["niveau"] is not None):
            raise Refus(f"banque : {i} : un bon témoin n'a ni item ni niveau")
        if t["classe"] == "mauvais" and (t["item"] not in items or t["niveau"] not in NIVEAUX):
            raise Refus(f"banque : {i} : un mauvais témoin a un item de la consigne et un niveau de {NIVEAUX}")
        if not isinstance(t["citation"], bool):
            raise Refus(f"banque : {i} : citation booléenne attendue")
        if t["moitie"] not in MOITIES:
            raise Refus(f"banque : {i} : moitié hors de {MOITIES}")
        c = t["contenu"]
        if not isinstance(c, dict) or not c or not all(isinstance(a, str) and a and isinstance(b, str) and b.strip()
                                                       for a, b in c.items()):
            raise Refus(f"banque : {i} : contenu {{champ: texte}} non vide attendu")
        if set(c) & set(CLES_RESERVEES_CONTENU):
            raise Refus(f"banque : {i} : champ réservé dans le contenu servi")
        temoins.append(t)
    if len(temoins) != n:
        raise Refus(f"banque : {len(temoins)} témoins, {n} attendus")
    for m in MOITIES:
        if sum(1 for t in temoins if t["moitie"] == m) != n // 2:
            raise Refus(f"banque : la moitié « {m} » n'a pas {n // 2} témoins")
    return temoins


def lire_banque(chemin: Path, sha_attendue: str, items, n=N_TEMOINS) -> tuple:
    """Banque scellée seulement : empreinte égale à l'empreinte attendue passée en argument, compagnon égal."""
    if not isinstance(sha_attendue, str) or not re.fullmatch(r"[0-9a-f]{64}", sha_attendue):
        raise Refus("banque : empreinte attendue (64 caractères hexadécimaux) exigée en argument")
    garde_chemins([chemin])
    octets = lire_par_empreinte(chemin, sha_attendue, "banque de témoins")
    exiger_compagnon(chemin, sha_attendue, "banque de témoins")
    try:
        objet = json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise Refus("banque : JSON illisible") from None
    return valider_banque(objet, items, n), sha_attendue


def lire_temoins_v2(chemin: Path, ids_plomberie) -> tuple:
    garde_chemins([chemin])
    octets = lire_par_empreinte(chemin, TEMOINS_V2[1], "témoins de la version 2")
    brut = json.loads(octets.decode("utf-8"))
    par_id = {t["id"]: t for t in brut["temoins"]}
    ids = list(ids_plomberie)
    if len(ids) != N_PLOMBERIE or len(set(ids)) != N_PLOMBERIE or any(i not in par_id for i in ids):
        raise Refus(f"plomberie : {N_PLOMBERIE} identifiants distincts de témoins de la version 2 exigés")
    return {f"v2:{i}": {"identifiant_interne": f"v2:{i}", "contenu": par_id[i]["contenu"], "classe": par_id[i]["classe"],
                        "item": par_id[i]["item_plante"]} for i in ids}, TEMOINS_V2[1]


# --- plan des envois -----------------------------------------------------------------------------------------------------------


def _version_numpy_suffisante(np) -> bool:
    m = re.match(r"^(\d+)\.(\d+)", np.__version__)
    return bool(m) and (int(m.group(1)), int(m.group(2))) >= (1, 25)


def ordre_tire(cle: str, ids_tries: list) -> list:
    import numpy as np
    if not _version_numpy_suffisante(np):
        raise Refus("numpy ≥ 1.25 exigé (règle R9)")
    ss = np.random.SeedSequence(RACINE_ORDRE, spawn_key=(CLES_TACHES[cle],))
    perm = np.random.default_rng(ss).permutation(len(ids_tries))
    return [ids_tries[int(i)] for i in perm]


def rendu_id(temoin: str, juge: str, rendu: int) -> str:
    return f"{temoin}|{juge}|r{rendu}"


def plan_des_envois(banque: list, plomberie: dict) -> list:
    """Ordre des envois prévus : bloc P (témoins de la version 2), bloc A (par témoin, juge Opus puis juge Argon), bloc B
    (moitié « lecture » d'abord, puis « étalonnage », chacune dans l'ordre tiré ; par témoin : rendu 2 du juge Opus, puis
    rendus 2 et 3 du juge Argon). C'est l'ordre que le calcul v2 des conditions du plafond a supposé."""
    moitie = {t["identifiant_interne"]: t["moitie"] for t in banque}
    ids = sorted(moitie)
    p = ordre_tire("ordre-bloc-P", sorted(plomberie))
    a = ordre_tire("ordre-bloc-A", ids)
    b_tire = ordre_tire("ordre-bloc-B", ids)
    b = [t for t in b_tire if moitie[t] == "lecture"] + [t for t in b_tire if moitie[t] == "etalonnage"]
    plan = []
    for rang, t in enumerate(p, 1):
        for j in JUGES:
            plan.append({"bloc": "P", "rang": rang, "temoin": t, "juge": j, "rendu": 1, "moitie": None})
    for rang, t in enumerate(a, 1):
        for j in JUGES:
            plan.append({"bloc": "A", "rang": rang, "temoin": t, "juge": j, "rendu": 1, "moitie": moitie[t]})
    for rang, t in enumerate(b, 1):
        for j in JUGES:
            for k in range(REPETITIONS_B[j]):
                plan.append({"bloc": "B", "rang": rang, "temoin": t, "juge": j, "rendu": 2 + k, "moitie": moitie[t]})
    for e in plan:
        e["id"] = rendu_id(e["temoin"], e["juge"], e["rendu"])
    return plan


# --- identifiants opaques et gardes de service --------------------------------------------------------------------------------


class Opaques:
    """Identifiant opaque servi, neuf à chaque rendu (forme du service de la course : « F » + cinq chiffres
    hexadécimaux), tiré par `SeedSequence(2026111935, spawn_key=(4,))` ; un identifiant déjà servi (journal compris, à la
    relance) n'est jamais repris."""

    def __init__(self, deja_servis=()):
        import numpy as np
        if not _version_numpy_suffisante(np):
            raise Refus("numpy ≥ 1.25 exigé (règle R9)")
        self.rng = np.random.default_rng(np.random.SeedSequence(RACINE_ORDRE,
                                                                spawn_key=(CLES_TACHES["identifiants-opaques"],)))
        self.servis = set(deja_servis)

    def neuf(self) -> str:
        while True:
            v = "F%05x" % int(self.rng.integers(0, 16 ** 5))
            if v not in self.servis:
                return v


MARQUE_FICHE = "## La fiche\n```json\n"


def fiche_servie(texte: str) -> tuple:
    if texte.count(MARQUE_FICHE) < 1:
        raise Refus("vérité non servie : fiche introuvable dans le texte servi")
    corps = texte.rsplit(MARQUE_FICHE, 1)[1].rsplit("\n```", 1)[0]
    try:
        return corps, json.loads(corps)
    except ValueError:
        raise Refus("vérité non servie : fiche servie illisible") from None


def garde_identifiant_neuf(opaque: str, servis: set) -> None:
    if not isinstance(opaque, str) or not re.fullmatch(r"F[0-9a-f]{5}", opaque):
        raise Refus("identifiant opaque neuf : forme inattendue : refus de servir")
    if opaque in servis:
        raise Refus("identifiant opaque neuf : identifiant déjà servi : refus de servir")


def garde_verite_non_servie(texte: str, contenu: dict, opaque: str, ids_internes, items, normaliser_texte) -> None:
    """Le texte servi ne porte ni l'identifiant interne du témoin ni celui du rendu (nulle part) ; la fiche servie est le
    contenu du témoin à l'octet près des valeurs, plus le seul identifiant opaque ; elle ne porte ni le mot « classe » ni
    le nom d'un item de la consigne. Sinon : refus de servir."""
    for i in ids_internes:
        if i and i in texte:
            raise Refus("vérité non servie : identifiant interne présent dans le texte servi : refus de servir")
    corps, d = fiche_servie(texte)
    if not isinstance(d, dict) or set(d) != set(contenu) | {"identifiant"} or d.get("identifiant") != opaque:
        raise Refus("vérité non servie : champs servis différents du contenu plus l'identifiant opaque : refus de servir")
    if {k: v for k, v in d.items() if k != "identifiant"} != contenu:
        raise Refus("vérité non servie : texte servi différent du contenu du témoin : refus de servir")
    plat = " " + normaliser_texte(corps) + " "
    if " classe " in plat:
        raise Refus("vérité non servie : le mot « classe » est dans la fiche servie : refus de servir")
    for item in items:
        if item in corps:
            raise Refus("vérité non servie : un nom d'item de la consigne est dans la fiche servie : refus de servir")


# --- journal à ajout seul et compteur d'arrêt ---------------------------------------------------------------------------------

TYPES_DE_LIGNE = ("ouverture", "relance", "engagement", "reglement", "arret_du_role", "arret", "fin")


class Journal:
    """Journal à ajout seul (une ligne JSON par événement, `fsync` après chaque ligne). Créé en mode exclusif ; relu en
    entier à la relance ; une ligne illisible, une ligne coupée ou un numéro de ligne faux : refus (jamais de remise à
    zéro, aucun repli)."""

    def __init__(self, chemin: Path, creer: bool):
        self.chemin = Path(chemin)
        self.lignes = []
        if creer:
            fd = os.open(self.chemin, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_APPEND, 0o644)
        else:
            self.lignes = self._lire()
            fd = os.open(self.chemin, os.O_WRONLY | os.O_APPEND)
        self._fd = fd

    def _lire(self) -> list:
        try:
            octets = self.chemin.read_bytes()
        except OSError:
            raise Refus("journal du compteur absent ou illisible : aucune relance, la mère est saisie") from None
        if octets and not octets.endswith(b"\n"):
            raise Refus("journal du compteur : dernière ligne coupée : aucune relance, la mère est saisie")
        lignes = []
        for k, brut in enumerate(octets.decode("utf-8", "strict").splitlines()):
            try:
                o = json.loads(brut)
            except ValueError:
                raise Refus(f"journal du compteur : ligne {k} illisible : aucune relance, la mère est saisie") from None
            if not isinstance(o, dict) or o.get("type") not in TYPES_DE_LIGNE or o.get("n_ligne") != k:
                raise Refus(f"journal du compteur : ligne {k} hors forme : aucune relance, la mère est saisie")
            lignes.append(o)
        if not lignes or lignes[0]["type"] != "ouverture":
            raise Refus("journal du compteur : sans ligne d'ouverture : aucune relance, la mère est saisie")
        return lignes

    def ajouter(self, objet: dict) -> dict:
        if objet.get("type") not in TYPES_DE_LIGNE:
            raise ValueError("type de ligne inconnu")
        o = dict(objet, n_ligne=len(self.lignes))
        donnees = (json.dumps(o, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")
        os.write(self._fd, donnees)
        os.fsync(self._fd)
        self.lignes.append(o)
        return o

    def fermer(self) -> None:
        if self._fd is not None:
            os.close(self._fd)
            self._fd = None


class Compteur:
    """Compteur d'arrêt dur. Cumul compté = somme des montants réglés + 0,60 par engagement sans règlement. Un envoi ne part
    que si cumul + 0,60 ≤ plafond. Toutes les sommes en fractions exactes."""

    def __init__(self, journal: Journal, plafond_c: int = PLAFOND_C, session_c: int = SESSION_C):
        self.journal = journal
        self.plafond = Fraction(centimes(plafond_c), 100)
        self.session = Fraction(centimes(session_c), 100)
        self.engagements, self.reglements = {}, {}
        self._regle = Fraction(0)
        self._orphelins = set()
        for l in journal.lignes:
            if l["type"] == "engagement":
                n = l.get("n")
                try:
                    montant = lire_fraction(l.get("montant"))
                except ValueError:
                    montant = None
                if n != len(self.engagements) + 1 or montant != self.session:
                    raise Refus("journal du compteur : engagement hors forme : aucune relance, la mère est saisie")
                self.engagements[n] = l
                self._orphelins.add(n)
            elif l["type"] == "reglement":
                n = l.get("n")
                if n not in self.engagements or n in self.reglements:
                    raise Refus("journal du compteur : règlement sans engagement ou double : aucune relance")
                try:
                    compte = lire_fraction(l.get("compte"))
                except ValueError:
                    raise Refus("journal du compteur : montant réglé illisible : aucune relance") from None
                if compte < self.session and l.get("nature") != "cout_releve":
                    raise Refus("journal du compteur : envoi non relevé compté sous 0,60 USD : aucune relance")
                if compte <= 0:
                    raise Refus("journal du compteur : coût compté nul ou négatif : aucune relance")
                self.reglements[n] = l
                self._regle += compte
                self._orphelins.discard(n)

    def orphelins(self) -> list:
        return sorted(self._orphelins)

    def cumul(self) -> Fraction:
        return self._regle + self.session * len(self._orphelins)

    def peut_envoyer(self) -> bool:
        return self.cumul() + self.session <= self.plafond

    def engager(self, envoi: dict) -> int:
        if not self.peut_envoyer():
            raise RuntimeError("engagement interdit par la règle du compteur")  # jamais atteint : la boucle s'arrête avant
        n = len(self.engagements) + 1
        l = self.journal.ajouter(dict(envoi, type="engagement", n=n, montant=str(self.session),
                                      cumul_compte_avant=str(self.cumul())))
        self.engagements[n] = l
        self._orphelins.add(n)
        return n

    def regler(self, n: int, compte: Fraction, resultat: dict) -> dict:
        compte = exacte(compte)
        if n not in self.engagements or n in self.reglements:
            raise RuntimeError("règlement sans engagement ou double")
        if compte <= 0 or (compte < self.session and resultat.get("nature") != "cout_releve"):
            raise RuntimeError("jamais de coût compté à zéro ; un envoi non relevé est compté 0,60 USD")
        l = self.journal.ajouter(dict(resultat, type="reglement", n=n, compte=str(compte)))
        self.reglements[n] = l
        self._regle += compte
        self._orphelins.discard(n)
        return l

    def regler_les_orphelins(self) -> list:
        """À la relance : chaque engagement resté sans règlement (panne pendant l'envoi) est compté 0,60 USD ; l'envoi est
        tenu pour en erreur (son rendu garde le rejeu unique s'il était le premier essai)."""
        faits = []
        for n in self.orphelins():
            e = self.engagements[n]
            self.regler(n, self.session, {"nature": "engagement_sans_reglement", "statut": "panne", "succes": False,
                                          "cout_releve": None, "lisible": False, "rendu": e.get("rendu"),
                                          "essai": e.get("essai"), "reponse": None, "modele_servi": None,
                                          "modele_change": False})
            faits.append(n)
        return faits


# --- moyen du plafond de session ---------------------------------------------------------------------------------------------


def exiger_moyen_du_plafond_de_session(service) -> dict:
    """Pas de départ sans un moyen qui tient le plafond de session de 0,60 USD à chaque appel (texte l. 382 (i))."""
    budget = budget_de_session()
    moyens = {}
    for j in service.juges:
        ad = service.adaptateurs.get(j["fournisseur"])
        decl = getattr(ad, "moyen_du_plafond_de_session", None)
        if service.nature == "essai" and isinstance(decl, dict) and decl.get("type") == "factice":
            moyens[j["etiquette"]] = dict(decl, budget_usd_par_appel=decl_texte(budget))
            continue
        if service.nature != "reel" or ad is None:
            raise Refus(f"moyen du plafond de session : aucun pour {j['etiquette']} : pas de départ")
        if callable(getattr(ad, "environnement_commande", None)):
            env = ad.environnement_commande(budget, "juge_ideation", j["modele"])
            if cout_lisible(_float_ou_none(env.get("PLAFOND_SESSION_USD"))) != SESSION:
                raise Refus(f"moyen du plafond de session : PLAFOND_SESSION_USD ≠ 0,60 pour {j['etiquette']} : pas de départ")
            moyens[j["etiquette"]] = {
                "type": "borne de jetons produits",
                "ou": ("adaptateur commande externe : PLAFOND_SESSION_USD = 0,6 dans l'environnement de la commande ; "
                       "commande d'Argon v3d : maxOutputTokens = min(--max-sortie-jetons, reste du plafond au prix de sortie "
                       "moins la provision de pensée) ; pire cas au-dessus du plafond : refus sans envoi (code 4) ; coût "
                       "calculé au-delà du plafond : échec (code 10)"),
                "controle": "environnement de la commande relu : PLAFOND_SESSION_USD = 0,6"}
            continue
        construire = getattr(sys.modules.get(type(ad).__module__), "construire_options", None)
        if callable(construire) and hasattr(ad, "url_relais"):
            d = str(service.dossier_appels / j["etiquette"] / "controle-du-plafond")
            o = construire(d, budget, 1, url_relais=ad.url_relais, modele=j["modele"], role="juge_ideation",
                           interdire_lecture=getattr(ad, "interdire_lecture", None))
            if cout_lisible(o.get("max_budget_usd")) != SESSION or o.get("max_turns") != 1 or o.get("tools") != []:
                raise Refus(f"moyen du plafond de session : options du kit hors règle pour {j['etiquette']} : pas de départ")
            moyens[j["etiquette"]] = {
                "type": "plafond du service",
                "ou": ("adaptateur du kit : construire_options pose max_budget_usd = 0,6, max_turns = 1, aucun outil ; le kit "
                       "rend « budget_depasse » au-delà"),
                "controle": "options du kit construites et relues (fonction pure, aucun appel)"}
            continue
        raise Refus(f"moyen du plafond de session : adaptateur inconnu pour {j['etiquette']} : pas de départ")
    return moyens


def _float_ou_none(texte):
    try:
        return float(texte)
    except (TypeError, ValueError):
        return None


def decl_texte(x) -> str:
    return repr(x)


# --- service -------------------------------------------------------------------------------------------------------------------


class Service:
    """Ce qu'il faut pour servir : juges [{etiquette, fournisseur, modele}], adaptateurs {fournisseur: adaptateur}, consigne
    figée (texte et empreinte), items, étiquettes interdites, dossier des appels, fonctions de l'orchestrateur, nature
    (« essai » ou « reel »), configuration servie des juges et son empreinte, et une garde facultative avant chaque envoi
    (`avant_envoi() -> motif ou None`, par exemple l'arrêt pour crédit d'un relais)."""

    def __init__(self, *, nature, juges, adaptateurs, consigne, consigne_sha, items, interdites, dossier_appels, fonctions,
                 configuration_servie, avant_envoi=None):
        if nature not in ("essai", "reel"):
            raise ValueError("nature : « essai » ou « reel »")
        if [j["etiquette"] for j in juges] != list(JUGES):
            raise Refus(f"juges : {list(JUGES)} exigés, dans cet ordre")
        self.nature, self.juges, self.adaptateurs = nature, juges, adaptateurs
        self.consigne, self.consigne_sha = consigne, consigne_sha
        if sha256_octets(consigne.encode("utf-8")) != consigne_sha or consigne_sha != CONSIGNE_JUGE[1]:
            raise Refus("consigne servie : empreinte différente de la consigne figée du juge")
        self.items, self.interdites = list(items), list(interdites)
        self.dossier_appels = Path(dossier_appels)
        self.fonctions = fonctions
        self.configuration_servie = configuration_servie
        self.configuration_sha = sha256_octets(json_octets(configuration_servie))
        self.avant_envoi = avant_envoi

    def juge(self, etiquette):
        return next(j for j in self.juges if j["etiquette"] == etiquette)


class ResultatFactice:
    def __init__(self, texte, cout, statut="ok", modele_servi=None, cout_inconnu=False, refus=None, erreur=None):
        self.texte_final = texte
        self.texte_brut = texte
        self.cout_declare_usd = cout
        self.statut = statut
        self.modele_servi = modele_servi
        self.cout_inconnu = cout_inconnu
        self.refus = refus
        self.erreur = erreur


class AdaptateurFactice:
    """Adaptateur factice du mode « essai » : aucun réseau, aucune clé, aucun relais. `regle(i, consigne, modele, dossier)`
    rend un `ResultatFactice` (ou lève) ; chaque appel est consigné (budget, tours, modèle, dossier, consigne)."""

    moyen_du_plafond_de_session = {"type": "factice",
                                   "moyen": "essai : le budget_usd reçu à chaque appel est consigné par l'adaptateur factice"}

    def __init__(self, regle):
        self.regle = regle
        self.appels = []

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        self.appels.append({"role": role, "budget_usd": budget_usd, "max_tours": max_tours, "modele": modele,
                            "dossier": dossier, "consigne": consigne})
        return self.regle(len(self.appels) - 1, consigne, modele, dossier)


# --- classement d'un retour ------------------------------------------------------------------------------------------------------


def changement_de_modele(r) -> bool:
    refus = getattr(r, "refus", None)
    ev = refus.get("evenement") if isinstance(refus, dict) else None
    return isinstance(ev, str) and (ev in EVENEMENTS_CHANGEMENT_DE_MODELE or ev.startswith("system.model_"))


def classer(r, exception, lire_verdict, items) -> dict:
    """Ce que le compteur compte et ce que le rendu devient. Refusé, coupé, en erreur (statut technique, exception, refus
    sans changement de modèle) : compté 0,60, rejouable. Retour obtenu (ok, budget dépassé, changement de modèle) : compté au
    coût relevé, ou 0,60 sans coût lisible ; jamais rejoué. Un coût relevé au-dessus de 0,60 est compté tel quel (jamais
    sous-compté) et arrête le programme."""
    if r is None:
        return {"succes": False, "statut": f"exception:{exception}", "cout_releve": None, "nature": "refuse_ou_erreur",
                "compte": SESSION, "texte": None, "lisible": False, "modele_servi": None, "changement": False}
    statut = str(getattr(r, "statut", None))
    cout = None if getattr(r, "cout_inconnu", False) is True else cout_lisible(getattr(r, "cout_declare_usd", None))
    changement = statut == "refus" and changement_de_modele(r)
    technique = statut in STATUTS_TECHNIQUES or (statut == "refus" and not changement) or \
        statut not in ("ok", "budget_depasse", "refus") + STATUTS_TECHNIQUES
    servi = getattr(r, "modele_servi", None)
    servi = servi if isinstance(servi, str) and servi else None
    if technique:
        compte = cout if (cout is not None and cout > SESSION) else SESSION
        return {"succes": False, "statut": statut, "cout_releve": cout, "nature": "refuse_ou_erreur", "compte": compte,
                "texte": None, "lisible": False, "modele_servi": servi, "changement": False}
    texte = (getattr(r, "texte_brut", None) or getattr(r, "texte_final", None)) if statut == "ok" else None
    lisible = bool(texte) and lire_verdict(texte, items) is not None
    return {"succes": True, "statut": statut, "cout_releve": cout,
            "nature": "cout_releve" if cout is not None else "sans_cout_lisible",
            "compte": cout if cout is not None else SESSION, "texte": texte, "lisible": lisible, "modele_servi": servi,
            "changement": changement}


# --- état reconstruit depuis le journal ----------------------------------------------------------------------------------------


def etat_depuis_journal(lignes: list) -> dict:
    """Par rendu : essais (n, succès), envoi retenu ; modèles servis premiers ; rôles arrêtés ; identifiants servis ;
    arrêt écrit ; fin écrite."""
    engagements = {l["n"]: l for l in lignes if l["type"] == "engagement"}
    rendus, premiers, roles, servis = {}, {}, {}, set()
    arret, fin = None, None
    for l in lignes:
        if l["type"] == "engagement":
            servis.add(l["opaque"])
        elif l["type"] == "reglement":
            e = engagements[l["n"]]
            s = rendus.setdefault(e["rendu"], {"essais": [], "retenu": None, "modele_change": False})
            s["essais"].append({"n": l["n"], "succes": bool(l.get("succes"))})
            if l.get("succes"):
                if l.get("modele_change"):
                    s["modele_change"] = True
                else:
                    s["retenu"] = l["n"]
                if l.get("statut") == "ok" and l.get("modele_servi") and not l.get("modele_change"):
                    premiers.setdefault(e["juge"], l["modele_servi"])
        elif l["type"] == "arret_du_role":
            roles[l["juge"]] = l.get("motif")
        elif l["type"] == "arret":
            arret = l
        elif l["type"] == "fin":
            fin = l
    return {"rendus": rendus, "premiers": premiers, "roles_arretes": roles, "servis": servis, "arret": arret, "fin": fin}


def rendu_fini(s) -> bool:
    return s is not None and (s["retenu"] is not None or s["modele_change"] or
                              sum(1 for e in s["essais"] if not e["succes"]) >= MAX_ESSAIS)


# --- exécution -----------------------------------------------------------------------------------------------------------------


def _decrire(prevu: dict, essai=None) -> dict:
    d = {"bloc": prevu["bloc"], "rang_dans_le_bloc": prevu["rang"], "juge": prevu["juge"], "rendu": prevu["rendu"]}
    if prevu["moitie"]:
        d["moitie"] = prevu["moitie"]
    if essai is not None:
        d["essai"] = essai
    return d


def executer(sortie, banque_chemin, banque_sha, plomberie_ids, service: Service, contexte: dict,
             temoins_v2_chemin=None, n_temoins=N_TEMOINS, arret_de_plomberie=True) -> dict:
    """Joue le plan (ou le reprend après une panne) sous le compteur ; dépose et scelle ce qui est fait. Rend le rapport.

    `arret_de_plomberie` : vrai en mode réel, toujours (le mode réel ne le passe pas). Faux seulement pour l'essai qui
    reproduit le calcul v2 « tous refusés » : ce calcul ne joue pas l'arrêt de la plomberie (écart déclaré au rapport)."""
    if not arret_de_plomberie and service.nature != "essai":
        raise Refus("l'arrêt de la plomberie ne se lève qu'en mode essai")
    sortie = Path(sortie)
    temoins_v2_chemin = Path(temoins_v2_chemin) if temoins_v2_chemin else DEPOT / TEMOINS_V2[0]
    garde_chemins([sortie, banque_chemin, temoins_v2_chemin, service.dossier_appels])
    depot = sortie / "sortie" / "epreuve"
    journal_chemin = depot / "journal-compteur.jsonl"
    relance = journal_chemin.exists()
    if not relance and depot.exists() and any(depot.iterdir()):
        raise Refus("dossier de dépôt non vide sans journal du compteur : aucune remise à zéro, la mère est saisie")
    banque, banque_sha = lire_banque(Path(banque_chemin), banque_sha, service.items, n_temoins)
    plomberie, temoins_v2_sha = lire_temoins_v2(temoins_v2_chemin, plomberie_ids)
    par_id = {t["identifiant_interne"]: t for t in banque}
    par_id.update(plomberie)
    plan = plan_des_envois(banque, plomberie)
    moyens = exiger_moyen_du_plafond_de_session(service)
    for d in (depot, depot / "reponses-brutes", depot / "entrees-servies", service.dossier_appels):
        d.mkdir(parents=True, exist_ok=True)
    k_exec = 1 + sum(1 for x in depot.iterdir() if x.name.startswith("manifeste-execution-") and x.name.endswith(".json"))
    journal = Journal(journal_chemin, creer=not relance)
    try:
        compteur = Compteur(journal)
        etat_avant = etat_depuis_journal(journal.lignes)
        if relance:
            if etat_avant["arret"] is not None:
                raise Refus("relance refusée : une exécution précédente s'est arrêtée (plafond, plomberie ou coût) : aucune "
                            "suite sous cette ligne")
            if etat_avant["fin"] is not None:
                raise Refus("relance refusée : le plan est déjà servi en entier")
        lecture = {"engagements": len(compteur.engagements), "reglements": len(compteur.reglements),
                   "orphelins": compteur.orphelins(), "cumul_compte_lu": str(compteur.cumul())}
        manifeste = manifeste_d_execution(k_exec, relance, lecture, contexte, service, banque_sha, temoins_v2_sha,
                                          plomberie_ids, moyens, plan, sortie, n_temoins, arret_de_plomberie)
        ecrire_scelle(depot / f"manifeste-execution-{k_exec}.json", manifeste)
        if relance:
            regles = compteur.regler_les_orphelins()
            journal.ajouter({"type": "relance", "execution": k_exec, "orphelins_regles_a_0_60": regles,
                             "cumul_compte": str(compteur.cumul())})
        else:
            journal.ajouter({"type": "ouverture", "execution": k_exec, "version": VERSION, "plafond_c": PLAFOND_C,
                             "session_c": SESSION_C, "banque_sha256": banque_sha})
        arret = jouer(plan, par_id, service, compteur, journal, depot, arret_de_plomberie)
    finally:
        journal.fermer()
    return deposer(depot, k_exec, plan, par_id, service, journal.lignes, compteur, arret)


def jouer(plan, par_id, service, compteur, journal, depot, arret_de_plomberie):
    f = service.fonctions
    etat = etat_depuis_journal(journal.lignes)
    rendus, premiers, roles = etat["rendus"], dict(etat["premiers"]), dict(etat["roles_arretes"])
    opaques = Opaques(etat["servis"])
    dernier = None
    for prevu in plan:
        s = rendus.get(prevu["id"])
        if rendu_fini(s) or prevu["juge"] in roles:
            continue
        juge = service.juge(prevu["juge"])
        ad = service.adaptateurs[juge["fournisseur"]]
        t = par_id[prevu["temoin"]]
        while not rendu_fini(rendus.get(prevu["id"])):
            essai = 1 + len((rendus.get(prevu["id"]) or {"essais": []})["essais"])
            motif = service.avant_envoi() if service.avant_envoi else None
            if motif:
                return journal.ajouter({"type": "arret", "motif": "garde avant envoi : " + str(motif),
                                        "premier_envoi_non_parti": _decrire(prevu, essai), "dernier_envoi_parti": dernier,
                                        "cumul_compte": str(compteur.cumul())})
            if not compteur.peut_envoyer():
                return journal.ajouter({"type": "arret", "motif": "plafond : cumul compté plus 0,60 USD dépasse le plafond",
                                        "premier_envoi_interdit": _decrire(prevu, essai), "dernier_envoi_parti": dernier,
                                        "cumul_compte": str(compteur.cumul())})
            opaque = opaques.neuf()
            try:
                garde_identifiant_neuf(opaque, opaques.servis)
                texte = f["entree_une_fiche"](service.consigne, {"contenu": t["contenu"]}, service.interdites,
                                              identifiant_servi=opaque)
                garde_verite_non_servie(texte, t["contenu"], opaque, (prevu["temoin"], prevu["id"]), service.items,
                                        f["normaliser_texte"])
            except Refus as e:
                return journal.ajouter({"type": "arret", "motif": "refus de servir : " + str(e),
                                        "premier_envoi_non_parti": _decrire(prevu, essai), "dernier_envoi_parti": dernier,
                                        "cumul_compte": str(compteur.cumul())})
            except Exception as e:  # noqa: BLE001 — garde A4 de l'orchestrateur (étiquette interdite) ou fiche refusée
                return journal.ajouter({"type": "arret", "motif": "refus de servir (service des juges) : "
                                        + type(e).__name__, "premier_envoi_non_parti": _decrire(prevu, essai),
                                        "dernier_envoi_parti": dernier, "cumul_compte": str(compteur.cumul())})
            opaques.servis.add(opaque)
            dossier = service.dossier_appels / prevu["juge"] / opaque
            dossier.mkdir(parents=True, exist_ok=False)
            n = compteur.engager({"rendu": prevu["id"], "bloc": prevu["bloc"], "rang": prevu["rang"],
                                  "temoin": prevu["temoin"], "juge": prevu["juge"], "essai": essai, "opaque": opaque,
                                  "entree_sha256": sha256_octets(texte.encode("utf-8"))})
            # la fiche servie seule (la consigne figée est la même à chaque appel, son empreinte est au manifeste) ; le texte
            # entier se refait par `entree_une_fiche` et son empreinte est à l'engagement
            ecrire_exclusif(depot / "entrees-servies" / f"envoi-{n:05d}.json", fiche_servie(texte)[0].encode("utf-8"))
            r, exc = None, None
            try:
                r = ad.lancer("juge_ideation", texte, str(dossier), budget_de_session(), 1, modele=juge["modele"])
            except Exception as e:  # noqa: BLE001 — envoi en erreur : compté 0,60, rejouable ; seul le nom de classe est gardé
                exc = type(e).__name__
            c = classer(r, exc, f["lire_verdict"], service.items)
            change = c["changement"]
            if c["succes"] and c["statut"] == "ok" and c["modele_servi"]:
                vu = premiers.setdefault(prevu["juge"], c["modele_servi"])
                change = change or vu != c["modele_servi"]
            brut = {"statut": c["statut"], "texte_brut": getattr(r, "texte_brut", None) if r is not None else None,
                    "texte_final": getattr(r, "texte_final", None) if r is not None else None,
                    "cout_declare_usd": repr(getattr(r, "cout_declare_usd", None)) if r is not None else None,
                    "cout_inconnu": getattr(r, "cout_inconnu", None) if r is not None else None,
                    "modele_servi": c["modele_servi"], "exception": exc,
                    "erreur": f["caviarder"](str(getattr(r, "erreur", "") or ""))[0][:500] if r is not None else None}
            reponse_sha = ecrire_exclusif(depot / "reponses-brutes" / f"envoi-{n:05d}.json", json_octets(brut))
            l = compteur.regler(n, c["compte"], {
                "rendu": prevu["id"], "essai": essai, "succes": c["succes"], "statut": c["statut"], "nature": c["nature"],
                "cout_releve": None if c["cout_releve"] is None else str(c["cout_releve"]), "lisible": c["lisible"],
                "modele_servi": c["modele_servi"], "modele_change": bool(change and c["succes"]),
                "reponse": f"reponses-brutes/envoi-{n:05d}.json", "reponse_sha256": reponse_sha})
            s = rendus.setdefault(prevu["id"], {"essais": [], "retenu": None, "modele_change": False})
            s["essais"].append({"n": n, "succes": c["succes"]})
            if c["succes"]:
                if change:
                    s["modele_change"] = True
                else:
                    s["retenu"] = n
            dernier = dict(_decrire(prevu, essai), n=n, refuse=not c["succes"])
            if change:
                roles[prevu["juge"]] = "modèle servi changé (A2) : arrêt du rôle, aucune bascule sans mot de Lazar"
                journal.ajouter({"type": "arret_du_role", "juge": prevu["juge"], "motif": roles[prevu["juge"]], "n": n})
            if c["cout_releve"] is not None and c["cout_releve"] > SESSION:
                return journal.ajouter({"type": "arret", "motif": "coût relevé au-dessus du plafond de session de 0,60 USD",
                                        "dernier_envoi_parti": dernier, "cumul_compte": str(compteur.cumul())})
            if prevu["juge"] in roles:
                break
        if prevu["bloc"] == "P" and arret_de_plomberie and prevu["juge"] not in roles:
            motif = motif_plomberie(rendus.get(prevu["id"]), compteur, prevu["juge"])
            if motif:
                return journal.ajouter({"type": "arret", "motif": "plomberie : " + motif, "dernier_envoi_parti": dernier,
                                        "cumul_compte": str(compteur.cumul()), "retour": "à la mère"})
        if all(j in roles for j in JUGES):
            break
    journal.ajouter({"type": "fin", "cumul_compte": str(compteur.cumul()), "dernier_envoi_parti": dernier})
    return None


def motif_plomberie(s, compteur, juge):
    """Texte l. 378 : plomberie illisible, ou coût par appel au-delà de trois fois le tarif des cartes : arrêt, retour à la
    mère. Un coût non relevé ne permet pas la lecture du coût par appel : arrêt aussi (choix écrit au rapport)."""
    if s is None or s["retenu"] is None:
        return "réponse absente ou rôle sans réponse retenue"
    l = compteur.reglements[s["retenu"]]
    if not l.get("lisible"):
        return "réponse illisible"
    if l.get("cout_releve") is None:
        return "coût par appel non relevé"
    if lire_fraction(l["cout_releve"]) > FACTEUR_ARRET_PLOMBERIE * TARIF_DES_CARTES[juge]:
        return "coût par appel au-delà de trois fois le tarif des cartes"
    return None


# --- dépôt ----------------------------------------------------------------------------------------------------------------------


def deposer(depot, k_exec, plan, par_id, service, lignes, compteur, arret) -> dict:
    f = service.fonctions
    etat = etat_depuis_journal(lignes)
    rendus, roles = etat["rendus"], etat["roles_arretes"]
    regles = {l["n"]: l for l in lignes if l["type"] == "reglement"}
    textes = {}
    sorties = {"P": [], "lecture": [], "etalonnage": []}
    par_rendu = {}
    for prevu in plan:
        s = rendus.get(prevu["id"])
        verdict, motif, etat_r, reponse_sha = None, None, None, None
        if s is not None and s["retenu"] is not None:
            l = regles[s["retenu"]]
            brut = json.loads((depot / l["reponse"]).read_bytes().decode("utf-8"))
            texte = brut.get("texte_brut") or brut.get("texte_final")
            textes[prevu["id"]] = (texte or "").encode("utf-8")
            verdict = f["lire_verdict"](texte, service.items) if texte else None
            etat_r = "obtenu"
            motif = None if verdict is not None else "verdict illisible"
            reponse_sha = l.get("reponse_sha256")
        elif s is not None and s["modele_change"]:
            etat_r, motif = "absent", "modèle servi changé"
        elif s is not None and sum(1 for e in s["essais"] if not e["succes"]) >= MAX_ESSAIS:
            etat_r, motif = "absent", "envoi et rejeu refusés, coupés ou en erreur"
        elif prevu["juge"] in roles:
            etat_r, motif = "role_arrete", roles[prevu["juge"]]
        else:
            etat_r, motif = "non_parti", "non parti (arrêt ou plan non servi)"
        ligne = {"temoin": prevu["temoin"], "juge": prevu["juge"], "rendu": prevu["rendu"], "bloc": prevu["bloc"],
                 "rang_dans_le_bloc": prevu["rang"], "etat": etat_r, "motif": motif, "verdict": verdict,
                 "envois": [e["n"] for e in (s or {"essais": []})["essais"]], "reponse_sha256": reponse_sha}
        par_rendu[prevu["id"]] = ligne
        sorties["P" if prevu["bloc"] == "P" else prevu["moitie"]].append(ligne)
    noms = {"P": "verdicts-plomberie", "lecture": "verdicts-moitie-lecture", "etalonnage": "verdicts-moitie-etalonnage"}
    empreintes = {}
    for cle, nom in noms.items():
        chemin = depot / f"{nom}-execution-{k_exec}.json"
        empreintes[chemin.name] = ecrire_scelle(chemin, {"version": VERSION, "execution": k_exec, "rendus": sorties[cle]})
    juges = etat_des_juges(plan, par_rendu, textes, roles, etat["premiers"])
    empreintes[f"etat-des-juges-execution-{k_exec}.json"] = ecrire_scelle(
        depot / f"etat-des-juges-execution-{k_exec}.json", juges)
    complets = comptes_complets(plan, par_rendu)
    rapport = {"version": VERSION, "execution": k_exec, "nature": service.nature,
               "envois_partis": len(compteur.engagements), "envois_prevus": len(plan),
               "envois_refuses_comptes": sum(1 for l in regles.values() if not l.get("succes")),
               "rendus_obtenus": sum(1 for x in par_rendu.values() if x["etat"] == "obtenu"),
               "cumul_compte_exact_usd": str(compteur.cumul()), "cumul_compte_usd": decimal_texte(compteur.cumul()),
               "plafond_usd": decimal_texte(PLAFOND, 2), "arret": arret, "complets": complets,
               "roles_arretes": roles, "etat_des_juges": juges,
               "journal_sha256": sha256_fichier(depot / "journal-compteur.jsonl"), "depots": empreintes}
    ecrire_scelle(depot / f"rapport-execution-{k_exec}.json", rapport)
    return rapport


def comptes_complets(plan, par_rendu) -> dict:
    obtenu = {i for i, x in par_rendu.items() if x["etat"] == "obtenu"}
    par_temoin = {}
    for p in plan:
        par_temoin.setdefault((p["bloc"], p["temoin"]), []).append(p)
    def complet(bloc):
        return {t for (b, t), ps in par_temoin.items() if b == bloc and all(p["id"] in obtenu for p in ps)}
    def partiel(bloc):
        return {t for (b, t), ps in par_temoin.items() if b == bloc and any(p["id"] in obtenu for p in ps)} - complet(bloc)
    moitie = {p["temoin"]: p["moitie"] for p in plan if p["bloc"] != "P"}
    rang_b = {p["temoin"]: p["rang"] for p in plan if p["bloc"] == "B"}
    b = complet("B")
    return {"plomberie": len(complet("P")) == N_PLOMBERIE, "bloc_A": len(complet("A")), "bloc_B": len(b),
            "bloc_B_moitie_lecture": sum(1 for t in b if moitie[t] == "lecture"),
            "bloc_B_moitie_etalonnage": sum(1 for t in b if moitie[t] == "etalonnage"),
            "rangs_des_temoins_partiels_au_bloc_B": sorted(rang_b[t] for t in partiel("B"))}


def etat_des_juges(plan, par_rendu, textes, roles, premiers) -> dict:
    """Absents (verdict absent ou illisible) parmi les rendus tentés des blocs A et B ; au-delà de 10 % : juge « non
    mesuré ». Réponses brutes identiques à l'octet : part des paires de rendus d'un même témoin, par juge ; au-delà de la
    moitié : ρ′ « non mesuré ». Aucun verdict n'est comparé à la vérité ici."""
    sortie = {}
    for j in JUGES:
        tentes = [x for p in plan if p["bloc"] != "P" and p["juge"] == j
                  for x in [par_rendu[p["id"]]] if x["etat"] in ("obtenu", "absent")]
        absents = sum(1 for x in tentes if x["verdict"] is None)
        part_abs = Fraction(absents, len(tentes)) if tentes else None
        par_temoin = {}
        for p in plan:
            if p["bloc"] != "P" and p["juge"] == j and p["id"] in textes:
                par_temoin.setdefault(p["temoin"], []).append((p["rendu"], textes[p["id"]]))
        paires = identiques = paires12 = identiques12 = 0
        for liste in par_temoin.values():
            liste.sort()
            for a in range(len(liste)):
                for b in range(a + 1, len(liste)):
                    paires += 1
                    identiques += liste[a][1] == liste[b][1]
                    if (liste[a][0], liste[b][0]) == (1, 2):
                        paires12 += 1
                        identiques12 += liste[a][1] == liste[b][1]
        part_id = Fraction(identiques, paires) if paires else None
        sortie[j] = {"rendus_tentes_A_et_B": len(tentes), "absents": absents,
                     "part_d_absents": None if part_abs is None else str(part_abs),
                     "juge_non_mesure": part_abs is not None and part_abs > SEUIL_ABSENTS,
                     "paires_de_rendus": paires, "paires_identiques_a_l_octet": identiques,
                     "part_identique": None if part_id is None else str(part_id),
                     "paires_rendus_1_et_2": paires12, "identiques_rendus_1_et_2": identiques12,
                     "rho_prime_non_mesure": part_id is not None and part_id > SEUIL_IDENTIQUES,
                     "modele_servi_premier": premiers.get(j), "role_arrete": roles.get(j)}
    return sortie


# --- manifeste (règle R9) ------------------------------------------------------------------------------------------------------


def manifeste_d_execution(k, relance, lecture, contexte, service, banque_sha, temoins_v2_sha, plomberie_ids, moyens, plan,
                          sortie, n_temoins, arret_de_plomberie) -> dict:
    import numpy as np
    reglages = {"sortie": str(sortie), "n_temoins": n_temoins, "plomberie": list(plomberie_ids),
                "plafond_c": PLAFOND_C, "session_c": SESSION_C, "banque_sha256": banque_sha,
                "arret_de_plomberie": arret_de_plomberie, **{k2: v for k2, v in (contexte.get("arguments") or {}).items()}}
    return {
        "version": VERSION, "execution": k, "relance": relance, "lecture_du_journal_au_lancement": lecture,
        "nature": service.nature, "horodatage_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "programme_sha256": sha256_fichier(Path(__file__)), "configuration": reglages,
        "configuration_sha256": sha256_octets(json_octets(reglages)),
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "plateforme": platform.platform()},
        "graines": {"racine": RACINE_ORDRE, "cles": dict(CLES_TACHES), "regle": REGLE_DES_GRAINES},
        "commits": {"depot_de_travail": contexte.get("commit_depot"), "orchestrateur": COMMIT_ORCHESTRATEUR},
        "service_des_juges": {"modules": service.fonctions.get("empreintes"), "version": service.fonctions.get("version_juges")},
        "consigne_servie_sha256": service.consigne_sha, "configuration_servie_des_juges": service.configuration_servie,
        "configuration_servie_des_juges_sha256": service.configuration_sha, "temoins_v2_sha256": temoins_v2_sha,
        "moyen_du_plafond_de_session": moyens, "plan": {
            "P": sum(1 for p in plan if p["bloc"] == "P"), "A": sum(1 for p in plan if p["bloc"] == "A"),
            "B": sum(1 for p in plan if p["bloc"] == "B"), "total": len(plan)},
        "ligne_de_go": contexte.get("ligne_de_go"), "reel": contexte.get("reel")}


# --- garde « ligne de GO » -----------------------------------------------------------------------------------------------------


def _plafond_en_centimes(texte: str):
    m = re.match(r"^\s*(\d+)(?:[.,](\d{1,2}))?\s*USD\s*$", texte or "")
    if not m:
        return None
    return int(m.group(1)) * 100 + int((m.group(2) or "0").ljust(2, "0"))


def verifier_ligne_de_go(texte_registre: str, go_id: str, aujourd_hui: _dt.date, plafond_c: int = PLAFOND_C) -> dict:
    """La ligne `go_id` (passée en argument : la garde ne dit pas quelle ligne vaut départ) est au registre, une seule ligne
    principale, huit colonnes, type « calcul », accordée par Lazar, non révoquée, dans sa période (échéance non passée),
    périmètre « ligne 3 » et « étage 2 », montant égal au plafond, en centimes exacts."""
    if not isinstance(go_id, str) or not GO_FORME.match(go_id):
        raise Refus("ligne de GO : identifiant GO-AAAA-MM-JJ-NN exigé : aucun appel")
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
    trouvees, revocations = [], []
    for ligne in texte_registre.splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif any(normaliser(c).startswith("revoc") for c in cellules) and any(go_id in c for c in cellules):
            revocations.append(m.group(1))
    principales = [c for c in trouvees if not (len(c) == 8 and c[3].lower().startswith("extension"))]
    if len(principales) != 1:
        raise Refus(f"ligne de GO {go_id} : {len(principales)} ligne(s) au registre (une exigée) : aucun appel")
    c = principales[0]
    if len(c) != 8:
        raise Refus(f"ligne de GO {go_id} : {len(c)} colonnes (8 attendues) : aucun appel")
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = c
    if typ != "calcul" or par != "Lazar":
        raise Refus(f"ligne de GO {go_id} : type « calcul » accordé par Lazar exigé : aucun appel")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"ligne de GO {go_id} : dates illisibles : aucun appel") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"ligne de GO {go_id} : hors de sa période ({d_acc} → {d_ech}) : échue ou pas encore valide : aucun appel")
    if revocations:
        raise Refus(f"ligne de GO {go_id} : révoquée : aucun appel")
    p = normaliser(perimetre)
    if not all(m in p for m in MOTS_PERIMETRE_GO):
        raise Refus(f"ligne de GO {go_id} : d'un autre périmètre (« ligne 3 » et « étage 2 » exigés) : aucun appel")
    lu = _plafond_en_centimes(plafond)
    if lu is None or lu != centimes(plafond_c):
        raise Refus(f"ligne de GO {go_id} : montant différent du plafond du programme ({PLAFOND_C} centimes) : aucun appel")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "plafond": plafond, "plafond_centimes": lu,
            "ligne_sha256": sha256_octets("|".join(c).encode("utf-8"))}


# --- mode réel (jamais lancé par l'auteur) -------------------------------------------------------------------------------------


def _argument(argv, nom, obligatoire=True):
    if nom in argv:
        i = argv.index(nom)
        if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
            return argv[i + 1]
    if obligatoire:
        raise Refus(f"argument {nom} exigé")
    return None


def charger_par_empreinte(rel: str, attendue: str, nom: str):
    chemin = DEPOT / rel
    octets = lire_par_empreinte(chemin, attendue, nom)
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    exec(compile(octets, str(chemin), "exec"), m.__dict__)
    return m


def lire_registre_main() -> dict:
    p = subprocess.run(["git", "-C", str(DEPOT), "show", "origin/main:registres/go.md"], capture_output=True, timeout=60)
    c = subprocess.run(["git", "-C", str(DEPOT), "rev-parse", "origin/main"], capture_output=True, text=True, timeout=60)
    if p.returncode != 0 or c.returncode != 0:
        raise Refus("registre des GO illisible sur origin/main : aucun appel")
    return {"texte": p.stdout.decode("utf-8"), "commit": c.stdout.strip(), "sha256": sha256_octets(p.stdout)}


def preparer_reel(argv, environ, aujourd_hui, lire_registre=lire_registre_main, construire_service=None) -> dict:
    """Refus avant tout, dans cet ordre : noms de clé dans l'environnement (par le nom seulement) ; chemins du coffre ;
    `--go-id` (et `GO_ID` s'il est posé, égal) valide au registre lu sur origin/main ; banque scellée à l'empreinte passée ;
    déclaration des relais scellée à l'empreinte passée, Claude et Argon seulement. Puis seulement `construire_service`."""
    noms = sorted(n for n in environ if re.search(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", n, re.I))
    if noms:
        raise Refus(f"noms de variables de clé dans l'environnement ({noms}) : la clé reste dans son relais")
    go_id = _argument(argv, "--go-id")
    if environ.get("GO_ID") not in (None, go_id):
        raise Refus("GO_ID de l'environnement différent de --go-id")
    banque, banque_sha = Path(_argument(argv, "--banque")), _argument(argv, "--banque-sha")
    decl, decl_sha = Path(_argument(argv, "--declaration")), _argument(argv, "--declaration-sha")
    sortie = Path(_argument(argv, "--sortie"))
    plomberie = (_argument(argv, "--plomberie") or "").split(",")
    nom_cle_claude = _argument(argv, "--nom-cle-claude")
    garde_chemins([banque, decl, sortie])
    registre = lire_registre()
    go = verifier_ligne_de_go(registre["texte"], go_id, aujourd_hui)
    if not re.fullmatch(r"[0-9a-f]{64}", banque_sha or ""):
        raise Refus("banque : empreinte attendue exigée")
    lire_par_empreinte(banque, banque_sha, "banque de témoins")
    exiger_compagnon(banque, banque_sha, "banque de témoins")
    if not re.fullmatch(r"[0-9a-f]{64}", decl_sha or ""):
        raise Refus("déclaration des relais : empreinte attendue exigée")
    octets = lire_par_empreinte(decl, decl_sha, "déclaration des relais")
    exiger_compagnon(decl, decl_sha, "déclaration des relais")
    try:
        d = json.loads(octets.decode("utf-8"))
    except ValueError:
        raise Refus("déclaration des relais : JSON illisible") from None
    if sorted((d.get("fournisseurs") or {})) != ["argon", "claude"]:
        raise Refus("déclaration des relais : claude et argon seulement (les deux juges de la configuration)")
    if construire_service is None:
        raise Refus("aucun constructeur de service")
    contexte = {"ligne_de_go": dict(go, registre_commit=registre["commit"], registre_sha256=registre["sha256"]),
                "arguments": {"go_id": go_id, "declaration": str(decl), "declaration_sha256": decl_sha,
                              "nom_cle_claude": nom_cle_claude}}
    service, reel = construire_service(decl=decl, decl_brute=d, decl_sha=decl_sha, sortie=sortie,
                                       nom_cle_claude=nom_cle_claude)
    contexte["reel"] = reel
    return {"service": service, "contexte": contexte, "banque": banque, "banque_sha": banque_sha, "sortie": sortie,
            "plomberie": plomberie}


def construire_service_reel(*, decl, decl_brute, decl_sha, sortie, nom_cle_claude):
    """Moyens de service du précédent (épreuve des témoins v9, 5be161fa… ; lanceur v9, 1b47c1cf…), repris sans les
    réinventer : pièces épinglées, orchestrateur épinglé, sonde du bac à sable, déclaration des relais, relais vivants
    contrôlés par PID, borne du relais d'Argon à deux actions par jugement, porte à blanc, enveloppes (garde de crédit,
    conservation des réponses brutes), adaptateurs réels et garde des dossiers d'appel, transmission du plafond d'étape.
    Jamais exécuté par l'auteur."""
    L = charger_par_empreinte(*LANCEUR_V9, "lancer_course_auto_conception_v9")
    P = charger_par_empreinte(*PRECEDENT_V9, "epreuve_temoins_auto_conception_v9")
    try:
        r = L.Reglages.production()
        pieces = L.verifier_pieces(r)
        orch = L.verifier_orchestrateur(r)
        racine_orch = Path(orch["chemin"])
        bac = P.exiger_bac_a_sable(L, r, racine_orch, P.environnement_de_sonde(os.environ))
        fixe = json.loads(Path(pieces["configuration"]["absolu"]).read_text(encoding="utf-8"))
        if pieces["configuration"]["sha256"] != CONFIGURATION[1]:
            raise Refus("configuration des juges : empreinte inattendue")
        if cout_lisible(fixe["plafonds_session"]["juge"]) != SESSION:
            raise Refus("configuration : plafond de session du juge différent de 0,60 USD")
        juges = [{"etiquette": j["etiquette"], "fournisseur": j["fournisseur"], "modele": j["modele"]} for j in fixe["juges"]]
        depart = {"variable_cle_claude": nom_cle_claude, "commandes_epinglees": {}, "especes_optionnelles": {}}
        decl_v = L.verifier_declaration(decl_brute, fixe, depart)
        appels_argon = 2 * (N_PLOMBERIE + N_TEMOINS + N_TEMOINS * REPETITIONS_B["juge-argon"])   # rejeu compris, au pire
        requis = L.appels_relais_gemini_requis(appels_argon)
        procedure = L.verifier_procedure_relais(r, decl_v, pieces, fixe, requis, plafond_ligne=float(PLAFOND))
        borne = P.verifier_borne_argon(procedure, requis, L.Refus)
        portes_a_blanc = L.porte_a_blanc(decl_v)
        arrets = sortie / "arrets-credit"
        arrets.mkdir(parents=True, exist_ok=True)       # à la relance, un arrêt pour crédit déjà posé arrête tout envoi
        conservation = sortie / L.DOSSIER_CONSERVATION_NOM
        conservation.mkdir(exist_ok=True)
        decl_v = L.envelopper_commandes(decl_v, sys.executable, Path(pieces["garde_credit"]["absolu"]), arrets,
                                        Path(pieces["enveloppe_conservation"]["absolu"]), conservation)
        P.charger_orchestrateur(racine_orch)            # comme le précédent : orchestrateur épinglé sur le chemin d'import
        spec = importlib.util.spec_from_file_location("ideation_v8_pour_ligne_3", racine_orch / L.LANCEUR_ORCHESTRATEUR)
        v8 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(v8)
        consigne = Path(pieces["consigne_juge"]["absolu"]).read_text(encoding="utf-8")
        base_sessions = str(sortie / "sessions")
        os.makedirs(base_sessions, exist_ok=True)
        plan_garde = [(j["etiquette"], j, consigne, float(SESSION), True) for j in juges]
        adaptateurs, portes, appels, controle = P.preparer_appels(v8, decl_v["fournisseurs"], sortie, base_sessions,
                                                                   plan_garde, {"controle-a": {}, "controle-b": {}},
                                                                   refus=L.Refus)
        accuses = {nom: p.transmettre(ETAPE, float(PLAFOND)) for nom, p in sorted(portes.items())}
    except L.Refus as e:
        raise Refus(f"service réel : {e}") from None
    fonctions = charger_service_des_juges(racine_orch)
    service = Service(nature="reel", juges=juges, adaptateurs=adaptateurs, consigne=consigne,
                      consigne_sha=sha256_octets(consigne.encode("utf-8")), items=fixe["items_juge"],
                      interdites=fixe["etiquettes_interdites_fixes"], dossier_appels=appels, fonctions=fonctions,
                      configuration_servie={"juges": juges, "items": fixe["items_juge"],
                                            "etiquettes_interdites": fixe["etiquettes_interdites_fixes"],
                                            "plafond_session_juge": fixe["plafonds_session"]["juge"],
                                            "configuration_sha256": CONFIGURATION[1]},
                      avant_envoi=lambda: ("refus pour crédit d'un relais" if any(
                          x.name.startswith("arret-credit-") for x in arrets.iterdir()) else None))
    reel = {"bac_a_sable": bac, "borne_relais_argon": borne, "porte_a_blanc": portes_a_blanc, "accuses_de_plafond": accuses,
            "declaration": {"chemin": str(decl), "sha256": decl_sha}, "procedure": procedure,
            "dossiers_d_appel": {"racine": str(appels), "controle_avant_appel": controle},
            "orchestrateur": {"chemin": str(racine_orch), "commit": orch.get("commit")},
            "reprise_du_precedent": {"lanceur": LANCEUR_V9, "precedent": PRECEDENT_V9}}
    return service, reel


def commit_du_depot() -> str | None:
    p = subprocess.run(["git", "-C", str(DEPOT), "rev-parse", "HEAD"], capture_output=True, text=True, timeout=60)
    return p.stdout.strip() if p.returncode == 0 else None


def principal(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if not argv or argv[0] != "--reel":
        print("usage : --reel --go-id GO-… --banque B --banque-sha S --declaration D --declaration-sha S2 "
              "--sortie DOSSIER_NEUF_OU_DE_RELANCE --plomberie tXX,tYY --nom-cle-claude NOM", file=sys.stderr)
        return 2
    try:
        prep = preparer_reel(argv, dict(os.environ), _dt.datetime.now(_dt.timezone.utc).date(),
                             construire_service=construire_service_reel)
        prep["contexte"]["commit_depot"] = commit_du_depot()
        rapport = executer(prep["sortie"], prep["banque"], prep["banque_sha"], prep["plomberie"], prep["service"],
                           prep["contexte"])
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps({"envois_partis": rapport["envois_partis"], "cumul_compte_usd": rapport["cumul_compte_usd"],
                      "arret": (rapport["arret"] or {}).get("motif")}, ensure_ascii=False))
    return 3 if rapport["arret"] else 0


if __name__ == "__main__":
    raise SystemExit(principal())
