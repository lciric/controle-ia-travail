#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Implémentation B (indépendante), version 2, de la statistique décisive — course de convergence des
règles de défense et sa réplication.

Écrite uniquement d'après « specification-statistique-decisive-v2.md » (les « § n » et les « points n »
renvoient à cette spécification ; pour la v1 de ce module, voir implementation_b.py, non modifié). Elle
n'importe rien du dépôt : bibliothèque standard + numpy. À lancer avec l'interpréteur du dépôt
(/home/claude/controle-ia-travail/.venv/bin/python, numpy 2.4.6) ; la version de numpy est écrite dans la sortie.

Sous-commandes
  replication        la réplication (E1 résultats, E2 manifeste, E3 préenregistrement scellé, E4 pièces de la
                     course originale, E5 analyse de A) ; racines par la règle D ; sortie JSON neuve
  essai              essai sur des pièces de la course originale ou de ses variantes (§ 12.1, § 12.3) ;
                     la racine est celle de la course originale (20266201), non modifiable
  regle-d            règle D (§ 4) appliquée à un préenregistrement scellé ou à une empreinte
  valider-originale  validation complète du § 12 ; écrit sortie-b-originale-v2.json, validation-b-v2.json, .md

Codes de sortie (§ 11.1) : 0 = sortie écrite, lecture autorisée ; 2 = arrêt d'entrée (aucune sortie) ;
3 = arrêt de contrôle (sortie écrite, `lecture_autorisee` faux, motifs écrits).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import re
import subprocess
import sys
import tempfile
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np

VERSION_IMPLEMENTATION = "implementation-b-v2"
NOM_FICHIER_IMPLEMENTATION = "implementation_b_v2.py"

# --------------------------------------------------------------------------------------------
# § 2 — constantes (binaires64 les plus proches de l'écriture décimale)
# --------------------------------------------------------------------------------------------
N = 100                      # instances par budget
B = 20_000                   # rééchantillonnages
P = (0.003125, 0.00625, 0.0125, 0.025, 0.05, 0.95, 0.975, 0.9875, 0.99375, 0.996875)
M = 0.02                     # marge d'effet d'intérêt (S1)
S5 = 0.02                    # tolérance de non-régression sur (ii)
ALPHA = 0.01                 # taux de fausses alertes visé
DEUX_ALPHA = 2 * ALPHA       # 0,02 (le doublement est exact en binaire)
TAU = 0.05                   # seuil de taille de la réplication de HR1
Z_ETOILE = 2.497705474412374  # quantile 0,99375 de la loi normale centrée réduite
EPS = 1e-9                   # tolérance de concordance entre deux implémentations ; largeur de la frontière
S_PUR = float.fromhex("0x1.fffffff768fa1p-1")   # seuil de T3 (point 15) ; comparaison « ≥ »
G_GRAINES = 2                # « graines neuves » : arrêt si un compte est strictement supérieur à G (CL-10)

# § 7 — seuils des contrôles de santé
SEUIL_T2_TROP_BEAU = 0.99
SEUIL_T2_EST_R3 = 0.30
SEUIL_T2_EST_XBARRE = 0.30
SEUIL_T3_NB = 50
SEUIL_T4_COS = 0.999
SEUIL_T4_NB = 50
SEUIL_T5 = 0.01
SEUIL_T6 = 0.001
# § 10.2
SEUIL_TR2 = 0.001
# § 5.2 : −1e-12 ≤ x ≤ 1 + 1e-12, bornes incluses, binaires64 (point 12)
BORNE_01_BAS = -float("1e-12")
BORNE_01_HAUT = float("1.000000000001")

BUDGETS = (1, 2)
RACINE_COURSE_ORIGINALE = 20266201
RACINE_TENUE_COURSE_ORIGINALE = 20266202

# § 3 — empreintes épinglées
EMPREINTE_SPECIFICATION_V2 = "977dd9092cbd3715bd2cc9b5d5839f276242ad3f9df6302d383555f2b2ff511a"
EMPREINTE_RESULTATS_ORIGINAUX = "d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b"
EMPREINTE_ANALYSE_ORIGINALE = "18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42"
EMPREINTE_CONFIG = "3fbb27fc0824b7a9d13a0036c975c43e00e4dc7ece9f0231dfca7c0234785098"
LAMBDA_ATTENDU = 0.3
REFERENCE_ATTENDUE = "moyenne"

# --------------------------------------------------------------------------------------------
# § 1 — variantes, mesures, libellés
# --------------------------------------------------------------------------------------------
LAMBDA_GREC = "λ"
NOMS_VARIANTES = ("R0", "R1", "R2", "R3", "R4[moyenne," + LAMBDA_GREC + "=0.3]")
NOM_R4 = NOMS_VARIANTES[4]
RANG = {nom: i for i, nom in enumerate(NOMS_VARIANTES)}
NOM_COURT = {"R0": "R0", "R1": "R1", "R2": "R2", "R3": "R3", NOM_R4: "R4"}
VARIANTES_CONTRASTEES = ("R0", "R1", "R3", NOM_R4)   # toutes sauf R2

# identifiant interne -> (code j, champ). « Xbarre » = X̄, exploitabilité moyenne au fil des tours.
MESURES = {
    "V": (0, "V_iii_final"),
    "ii": (1, "ii_final"),
    "X": (2, "exploitabilite_finale"),
    "Xbarre": (8, "exploitabilite_moyenne_tours"),
}
CHAMPS_MESURES = tuple(champ for (_, champ) in MESURES.values())
CHAMPS_LUS = CHAMPS_MESURES + ("V_iii_standard", "V_iii_renforce", "fpr_final")
# § 10.3 : les trois mesures du contrôle « graines neuves »
MESURES_GRAINES = ("V", "Xbarre", "ii")


def libelle_contraste(nom_variante: str, mesure: str) -> str:
    """Libellé d'un contraste dans les fichiers d'analyse : « <nom de k> - R2 (<champ de M>) »."""
    return f"{nom_variante} - R2 ({MESURES[mesure][1]})"


TOUS_LES_CONTRASTES = tuple((nom, mes) for mes in MESURES for nom in VARIANTES_CONTRASTEES)   # 16
# CL-10 : arrêt pour discordance sur ces cinq-là (par budget) ; alerte seulement pour les 11 autres
CONTRASTES_A_ARRET = (("R3", "V"), ("R0", "V"), (NOM_R4, "V"), ("R0", "ii"), ("R1", "Xbarre"))
# § 10.2 — contrastes primaires (variante, mesure, budget)
PRIMAIRES = (("R3", "V", 1), ("R3", "V", 2), ("R0", "V", 1), ("R0", "V", 2))

CLES_QUANTILES = tuple("q" + repr(p) for p in P)
IDX_B2 = (1, 8)   # [q(0,00625) ; q(0,99375)]
IDX_B8 = (0, 9)   # [q(0,003125) ; q(0,996875)]
IDX_E8 = (1, 8)   # mêmes quantiles que B2, rôle d'équivalence

# --------------------------------------------------------------------------------------------
# § 8 / § 9 / § 10 — libellés (copiés mot pour mot de la spécification)
# --------------------------------------------------------------------------------------------
A_DEGENERE = "non concluant : jeu dégénéré"
A_CONFIRMEE = "HR1 confirmée"
A_REFUTEE = "HR1 réfutée"
A_NON_DEMONTREE = "HR1 non démontrée"
EQUIVALENT = "≈"
INCERTAIN = "?"
LIBELLES_TABLE_C = {
    1: "régression avérée au-delà de la tolérance",
    2: "régression démontrée, sous la tolérance",
    3: "régression démontrée, ampleur non tranchée",
    4: "amélioration",
    5: "sans régression à S5 près",
    6: "imprécis",
}
V_SANTE = "non jugeable (santé)"
V_DEGENERE = "non jugeable (jeu dégénéré)"
V_IMPRECIS = "non jugeable (imprécis)"
V_REPLIQUEE = "répliquée"
V_HR1_SIGNE = "non répliquée (signe inversé)"
V_HR1_PETIT = "non répliquée (effet démontré inférieur à 0,05)"
V_HR0_INTERET = "non répliquée (le réentraînement l'emporte d'un effet d'intérêt)"
V_HR0_NON_NUL = "non répliquée (le réentraînement l'emporte, effet démontré non nul)"
V_NON_REPLIQUEE = "non répliquée"
V_HR3_SANS_VERDICT = "sans verdict (R4 ≈ défense figée)"
V_AUDIT_ATTENTE = "non jugeable (audit en attente)"
V_ARTEFACT = "non jugeable (artefact)"
O_CONFIRMEE = "confirmée"
O_REFUTEE = "réfutée"
O_NON_TRANCHEE = "non tranchée"
ISSUES = {
    1: "non jugeable (plomberie)",
    2: "en attente d'audit",
    3: "non jugeable (artefact)",
    4: "échec de réplication du résultat positif",
    5: "réplication réussie",
    6: "réplication partielle : le mélange tient, l'équivalence de la défense figée ne tient pas",
    7: "réplication partielle : le mélange tient, l'équivalence de la défense figée reste imprécise",
    8: "non jugeable",
}
MENTION_V0 = "V0 : non évaluée par B"

# § 4 — règle D : ensembles interdits et six entiers des vecteurs d'essai
RACINES_INTERDITES_EXPLICITES = frozenset({20261201, 20261202, 20266201, 20266202})
PLAGE_INTERDITE = (20261000, 20269999)   # bornes incluses
VECTEURS_REGLE_D = (
    ("d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d",
     11786724493248295725, 9136419304016434890),
    ("0" * 64, 15793235383387715774, 12390638538380655177),
    ("f" * 64, 10168828190493638947, 4616211851522120706),
)
ENTIERS_DES_VECTEURS = frozenset(x for (_, a, b) in VECTEURS_REGLE_D for x in (a, b))

# § 5.5 — vecteurs d'essai du générateur (racine 20266201)
VECTEURS_GENERATEUR = (
    {"cle": (1, 203, 0, 0, 99),
     "ligne0_dix_premiers": [80, 79, 39, 86, 45, 87, 54, 22, 58, 80],
     "derniere_ligne_cinq_derniers": [56, 63, 4, 66, 85]},
    {"cle": (2, 200, 0, 0, 99),
     "ligne0_dix_premiers": [73, 34, 66, 88, 64, 92, 23, 55, 84, 31],
     "derniere_ligne_cinq_derniers": [10, 38, 20, 60, 51]},
)


class Arret(Exception):
    """Arrêt d'entrée prescrit par la spécification (code 2, aucune sortie, aucun repli silencieux)."""


class ErreurInterne(Exception):
    """Incohérence interne qui ne peut pas se produire si la spécification est cohérente (par exemple la
    ligne inatteignable de « HR1 répliquée ? » atteinte) : arrêt, code 2, aucune sortie."""


# ============================================================================================
# Lecture exacte, empreintes, compagnons (§ 3)
# ============================================================================================
def _paires_sans_doublon(paires):
    objet = {}
    for cle, valeur in paires:
        if cle in objet:
            raise Arret(f"clé dupliquée dans le JSON : {cle!r}")
        objet[cle] = valeur
    return objet


def _constante_refusee(texte):
    raise Arret(f"constante JSON non finie refusée : {texte}")


def lire_json_octets(octets: bytes, role: str):
    """Lecture exacte : décimaux lus comme binaire64 (float de Python), entiers lus exactement (int de Python,
    précision arbitraire : jamais de passage par le binaire64). Une clé dupliquée, NaN, Infinity : arrêt."""
    try:
        return json.loads(octets.decode("utf-8"), object_pairs_hook=_paires_sans_doublon,
                          parse_constant=_constante_refusee)
    except Arret as e:
        raise Arret(f"{role} : {e}") from None
    except (UnicodeDecodeError, ValueError) as e:
        raise Arret(f"{role} : JSON illisible ({e})") from None


def empreinte_octets(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def chemin_compagnon(chemin) -> Path:
    """Le compagnon de F est F.sha256, même dossier (point 6) : jamais d'autre nom."""
    chemin = Path(chemin)
    return chemin.with_name(chemin.name + ".sha256")


def lire_compagnon(chemin):
    """Compagnon `<fichier>.sha256` : exactement « 64 hexadécimaux minuscules, deux espaces, nom de base du
    fichier, fin de ligne » (format de sha256sum). Rend (empreinte, nom de base inscrit, chemin du compagnon).
    Tout écart de format est un arrêt d'entrée."""
    chemin = Path(chemin)
    comp = chemin_compagnon(chemin)
    if not comp.is_file():
        raise Arret(f"aucun fichier compagnon {comp.name} à côté de {chemin.name}")
    try:
        texte = comp.read_bytes().decode("utf-8")
    except (OSError, UnicodeDecodeError) as e:
        raise Arret(f"compagnon {comp.name} illisible ({e})") from None
    m = re.fullmatch(r"([0-9a-f]{64})  ([^\n\r/\\]+)\n", texte)
    if m is None:
        raise Arret(f"compagnon {comp.name} : le format « empreinte (64 hexadécimaux minuscules), deux espaces, "
                    f"nom de base, fin de ligne » sur une seule ligne n'est pas respecté")
    return m.group(1), m.group(2), comp


def lire_fichier_verifie(chemin, role: str, *, attendue: str | None = None):
    """Lit les octets d'un fichier et vérifie son empreinte : celle imposée (`attendue`, épinglée) ou, à
    défaut, celle de son compagnon (empreinte ET nom de base vérifiés). Rend (octets, empreinte)."""
    chemin = Path(chemin)
    try:
        octets = chemin.read_bytes()
    except OSError as e:
        raise Arret(f"{role} : lecture impossible ({e})") from None
    sha = empreinte_octets(octets)
    if attendue is None:
        attendue, nom_inscrit, _ = lire_compagnon(chemin)
        if nom_inscrit != chemin.name:
            raise Arret(f"{role} : le compagnon nomme « {nom_inscrit} », le fichier est « {chemin.name} »")
    if sha != attendue:
        raise Arret(f"{role} : empreinte {sha} différente de l'attendue {attendue}")
    return octets, sha


def lire_fichier_compagnon_ou_epingle(chemin, role: str, epingles=()):
    """Pièce de la course originale ou de ses variantes (essais du § 12, points 7) : si un compagnon existe il est
    vérifié ; sinon le fichier n'est accepté que si son empreinte est l'une des empreintes épinglées."""
    chemin = Path(chemin)
    if chemin_compagnon(chemin).is_file():
        return lire_fichier_verifie(chemin, role)
    try:
        octets = chemin.read_bytes()
    except OSError as e:
        raise Arret(f"{role} : lecture impossible ({e})") from None
    sha = empreinte_octets(octets)
    if sha not in epingles:
        raise Arret(f"{role} : ni fichier compagnon {chemin_compagnon(chemin).name}, ni empreinte épinglée "
                    f"connue ({sha}) : empreinte non vérifiable")
    return octets, sha


# ============================================================================================
# § 4 — règle D
# ============================================================================================
def regle_d_derivation(h_hex: str):
    """Étapes 1 à 5 : E = entier de H (base 16) ; S = SeedSequence(E) sans clé de descendance ;
    (w0, w1) = deux premiers mots uint64 de generate_state ; rho = w0, rho_t = w1. Aucune garde."""
    if not isinstance(h_hex, str) or not re.fullmatch(r"[0-9a-f]{64}", h_hex):
        raise Arret("règle D : H doit s'écrire en 64 chiffres hexadécimaux minuscules")
    e = int(h_hex, 16)
    mots = np.random.SeedSequence(e).generate_state(2, dtype=np.uint64)
    return int(mots[0]), int(mots[1])


def regle_d_gardes(rho: int, rho_t: int) -> None:
    """Étape 6 : rho != rho_t ; ni l'un ni l'autre dans F (quatre racines nommées + plage
    [20261000 ; 20269999] bornes incluses) ni parmi les six entiers des vecteurs d'essai. Sinon arrêt."""
    if rho == rho_t:
        raise Arret("règle D : rho == rho_t")
    for nom, r in (("rho", rho), ("rho_t", rho_t)):
        if r in RACINES_INTERDITES_EXPLICITES or PLAGE_INTERDITE[0] <= r <= PLAGE_INTERDITE[1]:
            raise Arret(f"règle D : {nom} = {r} appartient à l'ensemble interdit F")
        if r in ENTIERS_DES_VECTEURS:
            raise Arret(f"règle D : {nom} = {r} est un des six entiers des vecteurs d'essai")


def regle_d(h_hex: str):
    """Règle D complète (dérivation + gardes). Rend (rho, rho_t)."""
    rho, rho_t = regle_d_derivation(h_hex)
    regle_d_gardes(rho, rho_t)
    return rho, rho_t


def regle_d_depuis_octets(octets: bytes):
    """H = SHA-256 des octets exacts du préenregistrement scellé. Rend (H, rho, rho_t)."""
    h = empreinte_octets(octets)
    rho, rho_t = regle_d(h)
    return h, rho, rho_t


# ============================================================================================
# § 3 / § 5.1 — forme de E1, sélection, ordre, gardes ; extraction des champs
# ============================================================================================
def _entier(x, nom: str) -> int:
    if isinstance(x, bool) or not isinstance(x, int):
        raise Arret(f"{nom} : entier attendu, trouvé {x!r}")
    return x


def _texte(x, nom: str) -> str:
    if not isinstance(x, str):
        raise Arret(f"{nom} : chaîne attendue, trouvé {x!r}")
    return x


def _nombre(x, nom: str) -> float:
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise Arret(f"{nom} : nombre attendu, trouvé {x!r}")
    try:
        v = float(x)
    except OverflowError:
        raise Arret(f"{nom} : entier trop grand pour un nombre à virgule") from None
    if not math.isfinite(v):
        raise Arret(f"{nom} : valeur non finie")
    return v


def valider_forme_E1(e1) -> list:
    """Forme de E1 (§ 3, point 9) : un objet qui contient AU MOINS `run_id` (chaîne), `manifeste_sha256` (chaîne) et
    `resultat` ; `resultat` contient au moins `temps` et `resultats`, liste de 200 tâches. Des clés supplémentaires
    sont permises partout (sauf dans `regles`)."""
    if not isinstance(e1, dict) or not {"run_id", "manifeste_sha256", "resultat"} <= set(e1):
        raise Arret("E1 : l'objet doit contenir run_id, manifeste_sha256 et resultat")
    _texte(e1["run_id"], "E1 run_id")
    _texte(e1["manifeste_sha256"], "E1 manifeste_sha256")
    res = e1["resultat"]
    if not isinstance(res, dict) or not {"temps", "resultats"} <= set(res):
        raise Arret("E1 : `resultat` doit contenir `temps` et `resultats`")
    taches = res["resultats"]
    if not isinstance(taches, list) or len(taches) != 2 * N:
        raise Arret("E1 : `resultats` doit être une liste de 200 tâches")
    return taches


DELTA_DU_BUDGET = {1: 1.4, 2: 1.6}


def controler_racines_taches(taches: list, rho: int, rho_t: int) -> None:
    """Garde (§ 3, § 4) : (racine, racine_tenue) de chacune des 200 tâches égales, exactement, à (rho, rho_t)."""
    for i, t in enumerate(taches):
        if not isinstance(t, dict):
            raise Arret(f"tâche {i} : objet attendu")
        for cle in ("racine", "racine_tenue"):
            if cle not in t:
                raise Arret(f"tâche {i} : champ `{cle}` absent")
        if _entier(t["racine"], f"tâche {i} racine") != rho or \
                _entier(t["racine_tenue"], f"tâche {i} racine_tenue") != rho_t:
            raise Arret(f"E1 : tâche {i} : (racine, racine_tenue) ≠ ({rho}, {rho_t})")


def selectionner_taches(taches: list) -> dict:
    """T_c triées par instance croissante ; gardes du § 5.1 et du § 3 (`delta`, `config_sha256`). Rend
    {c: [tâche, ...]} (c = 1, 2)."""
    par_budget = {c: [] for c in BUDGETS}
    for i, t in enumerate(taches):
        if not isinstance(t, dict):
            raise Arret(f"tâche {i} : objet attendu")
        for cle in ("code_delta", "instance", "delta", "racine", "racine_tenue", "config_sha256", "regles"):
            if cle not in t:
                raise Arret(f"tâche {i} : champ `{cle}` absent")
        c = _entier(t["code_delta"], f"tâche {i} code_delta")
        if c not in par_budget:
            raise Arret(f"tâche {i} : code_delta = {c} (1 ou 2 attendu)")
        _entier(t["instance"], f"tâche {i} instance")
        if _nombre(t["delta"], f"tâche {i} delta") != DELTA_DU_BUDGET[c]:
            raise Arret(f"tâche {i} : delta = {t['delta']!r} incohérent avec code_delta = {c} "
                        f"({DELTA_DU_BUDGET[c]} attendu)")
        if _texte(t["config_sha256"], f"tâche {i} config_sha256") != EMPREINTE_CONFIG:
            raise Arret(f"tâche {i} : config_sha256 = {t['config_sha256']!r} ≠ l'empreinte de configuration "
                        f"épinglée {EMPREINTE_CONFIG}")
        par_budget[c].append(t)
    for c in BUDGETS:
        par_budget[c].sort(key=lambda t: t["instance"])
        if len(par_budget[c]) != N:
            raise Arret(f"budget {c} : {len(par_budget[c])} tâches au lieu de {N}")
        if [t["instance"] for t in par_budget[c]] != list(range(N)):
            raise Arret(f"budget {c} : les instances ne sont pas exactement 0, 1, …, {N - 1} sans doublon")
        for t in par_budget[c]:
            regles = t["regles"]
            if not isinstance(regles, dict) or set(regles) != set(NOMS_VARIANTES):
                raise Arret(f"budget {c}, instance {t['instance']} : les clés de `regles` ne sont pas "
                            f"exactement les cinq noms de variantes")
            if list(regles) != list(NOMS_VARIANTES):
                raise Arret(f"budget {c}, instance {t['instance']} : ordre des variantes différent de "
                            f"R0, R1, R2, R3, R4")
    return par_budget


def extraire_donnees(taches_c: list, c: int) -> dict:
    """Champs numériques de chaque variante (tableaux numpy float64 de longueur n, dans l'ordre des instances),
    poids finaux de R3 et cosinus consécutifs de R4. Gardes du § 5.2, du § 3 (`lam`, `reference`) et de la
    cohérence de V (§ 7)."""
    champs = {nom: {ch: np.empty(N) for ch in CHAMPS_LUS} for nom in NOMS_VARIANTES}
    for l, t in enumerate(taches_c):
        for nom in NOMS_VARIANTES:
            v = t["regles"][nom]
            if not isinstance(v, dict):
                raise Arret(f"budget {c}, instance {l}, {nom} : objet attendu")
            for ch in CHAMPS_LUS:
                if ch not in v:
                    raise Arret(f"budget {c}, instance {l}, {nom} : champ `{ch}` absent")
                x = _nombre(v[ch], f"budget {c}, instance {l}, {nom}.{ch}")
                if ch in CHAMPS_MESURES and not (BORNE_01_BAS <= x <= BORNE_01_HAUT):
                    raise Arret(f"budget {c}, instance {l}, {nom}.{ch} = {x} hors de [-1e-12 ; 1 + 1e-12]")
                champs[nom][ch][l] = x
            # garde de cohérence de V : V_iii_final = min(V_iii_standard, V_iii_renforce) exactement
            if champs[nom]["V_iii_final"][l] != min(champs[nom]["V_iii_standard"][l],
                                                   champs[nom]["V_iii_renforce"][l]):
                raise Arret(f"budget {c}, instance {l}, {nom} : V_iii_final ≠ min(V_iii_standard, V_iii_renforce)")
            # garde `lam` / `reference` (point 13) : R4 = (0.3, « moyenne »), les quatre autres = (null, null)
            for cle in ("lam", "reference"):
                if cle not in v:
                    raise Arret(f"budget {c}, instance {l}, {nom} : champ `{cle}` absent")
            if nom == NOM_R4:
                if isinstance(v["lam"], bool) or not isinstance(v["lam"], (int, float)) or v["lam"] != LAMBDA_ATTENDU:
                    raise Arret(f"budget {c}, instance {l}, {nom} : lam = {v['lam']!r} ≠ {LAMBDA_ATTENDU}")
                if not isinstance(v["reference"], str) or v["reference"] != REFERENCE_ATTENDUE:
                    raise Arret(f"budget {c}, instance {l}, {nom} : reference = {v['reference']!r} ≠ "
                                f"« {REFERENCE_ATTENDUE} »")
            elif v["lam"] is not None or v["reference"] is not None:
                raise Arret(f"budget {c}, instance {l}, {nom} : lam et reference doivent être null "
                            f"(trouvé {v['lam']!r}, {v['reference']!r})")
    poids_r3, cos_r4 = [], []
    for l, t in enumerate(taches_c):
        w = t["regles"]["R3"].get("poids_finaux")
        if not isinstance(w, list) or len(w) == 0:
            raise Arret(f"budget {c}, instance {l}, R3 : `poids_finaux` doit être une liste non vide")
        poids_r3.append([_nombre(x, f"budget {c}, instance {l}, R3.poids_finaux") for x in w])
        par_tour = t["regles"][NOM_R4].get("par_tour")
        cos = par_tour.get("cos_consecutif") if isinstance(par_tour, dict) else None
        if not isinstance(cos, list) or len(cos) != 8:
            raise Arret(f"budget {c}, instance {l}, R4 : `par_tour.cos_consecutif` doit contenir 8 nombres")
        cos_r4.append([_nombre(x, f"budget {c}, instance {l}, R4.cos_consecutif") for x in cos])
    return {"champs": champs, "poids_R3": poids_r3, "cos_R4": cos_r4}


# ============================================================================================
# § 5.2 à 5.7 — la statistique d'un contraste
# ============================================================================================
def code_generateur(mesure: str, nom_variante: str) -> int:
    """code = 200 + 100 × j(M) + r(k)  (§ 5.4)."""
    return 200 + 100 * MESURES[mesure][0] + RANG[nom_variante]


def generateur(rho: int, c: int, code: int) -> np.random.Generator:
    """Generator fondé sur PCG64, initialisé par SeedSequence(entropie rho, clé (c, code, 0, 0, 99))."""
    graine = np.random.SeedSequence(entropy=int(rho), spawn_key=(int(c), int(code), 0, 0, 99))
    return np.random.Generator(np.random.PCG64(graine))


def indices_reechantillonnage(rho: int, c: int, code: int) -> np.ndarray:
    """Matrice I (B lignes, n colonnes) d'entiers uniformes de {0..n-1}, un seul appel, remplie ligne
    par ligne : integers(0, n, size=(B, n)) en entiers signés 64 bits (§ 5.5)."""
    return generateur(rho, c, code).integers(0, N, size=(B, N), dtype=np.int64)


def quantile_type7(tri: np.ndarray, p: float) -> float:
    """Quantile de type 7 (Hyndman et Fan) d'un tableau déjà trié (§ 5.6)."""
    h = (len(tri) - 1) * p
    f = int(math.floor(h))
    t = h - f
    if f >= len(tri) - 1:
        return float(tri[-1])
    return float(tri[f]) + t * (float(tri[f + 1]) - float(tri[f]))


def statistique_contraste(d: np.ndarray, rho: int, c: int, code: int) -> dict:
    """Sortie d'un contraste au format du § 5.7 à partir des différences appariées d."""
    if d.shape != (N,):
        raise Arret("différences appariées : longueur ≠ n")
    est = float(np.mean(d))
    s = float(np.sqrt(np.sum((d - est) ** 2) / (N - 1)))
    zeros = int(np.count_nonzero(d == 0))
    mu = np.sum(d[indices_reechantillonnage(rho, c, code)], axis=1) / N
    tri = np.sort(mu)
    quantiles = {cle: quantile_type7(tri, p) for cle, p in zip(CLES_QUANTILES, P)}
    return {"moyenne": est, "ecart_type": s, "n": N, "quantiles": quantiles, "zeros_exacts": zeros}


def bornes_depuis_statistique(stat: dict) -> dict:
    """Intervalles B2, B8, E8 (§ 2) d'une statistique au format du § 5.7."""
    q = [stat["quantiles"][cle] for cle in CLES_QUANTILES]
    return {"B2": (q[IDX_B2[0]], q[IDX_B2[1]]),
            "B8": (q[IDX_B8[0]], q[IDX_B8[1]]),
            "E8": (q[IDX_E8[0]], q[IDX_E8[1]])}


def calculer_contrastes_budget(donnees: dict, c: int, rho: int) -> dict:
    """Les 16 contrastes d'un budget : {libellé: statistique du § 5.7}."""
    champs = donnees["champs"]
    sortie = {}
    for nom, mes in TOUS_LES_CONTRASTES:
        champ = MESURES[mes][1]
        d = champs[nom][champ] - champs["R2"][champ]
        sortie[libelle_contraste(nom, mes)] = statistique_contraste(d, rho, c, code_generateur(mes, nom))
    return sortie


# ============================================================================================
# Comparaisons à un seuil avec suivi de la « frontière numérique » (§ 8, point 4)
# ============================================================================================
def _cmp(trace: list, nom: str, x: float, op: str, seuil: float) -> bool:
    """Comparaison atomique « x op seuil » ; elle est consignée dans la trace (sans court-circuit possible :
    l'appelant évalue toutes les comparaisons d'une ligne examinée avant de combiner)."""
    if op == ">":
        r = x > seuil
    elif op == "<":
        r = x < seuil
    elif op == ">=":
        r = x >= seuil
    elif op == "<=":
        r = x <= seuil
    else:   # pragma: no cover
        raise ValueError(op)
    trace.append((nom, x, op, seuil, bool(r)))
    return bool(r)


def _proches(trace: list) -> list:
    """Comparaisons à la frontière : |x − seuil| ≤ ε, inclusif."""
    return [{"quantite": nom, "valeur": x, "comparaison": f"{op} {s!r}", "ecart_au_seuil": abs(x - s)}
            for (nom, x, op, s, _) in trace if abs(x - s) <= EPS]


def _marque(trace: list, heritages: dict | None = None) -> dict:
    """Marque de frontière d'un élément (classe, contrôle, verdict, déclencheur, issue) : marqué si l'une de ses
    comparaisons est à la frontière, OU s'il hérite de la marque d'une entrée marquée (`heritages` : nom -> bool)."""
    heritages = heritages or {}
    proches = _proches(trace)
    hers = sorted(k for k, v in heritages.items() if v)
    marge = min((abs(x - s) for (_, x, _, s, _) in trace), default=None)
    return {"frontiere": bool(proches) or bool(hers), "frontiere_propre": bool(proches), "heritee_de": hers,
            "marge_min_au_seuil": marge, "comparaisons_a_la_frontiere": proches}


def _clore(trace: list, ligne: int, libelle: str, cle: str = "classe", extra: dict | None = None,
           heritages: dict | None = None) -> dict:
    r = {"ligne": ligne, cle: libelle}
    r.update(_marque(trace, heritages))
    if extra:
        r.update(extra)
    return r


# ============================================================================================
# § 8 — classes (la première condition vraie décide)
# ============================================================================================
def classe_table_A(par_budget: dict) -> dict:
    """Table A — Δ(R3, R2) sur V (HR1, règles de la course originale).
    par_budget[c] = {"est", "bas_B2", "haut_B2", "moyennes_V": {nom de variante: moy_c(k, V)}}."""
    trace: list = []
    degenere = {}
    for c in BUDGETS:
        pb = par_budget[c]
        degenere[c] = all([_cmp(trace, f"moy_{c}({NOM_COURT[nom]}, V)", pb["moyennes_V"][nom], "<=", DEUX_ALPHA)
                           for nom in NOMS_VARIANTES])
    detail = {str(c): {"est": par_budget[c]["est"], "bas_B2": par_budget[c]["bas_B2"],
                       "haut_B2": par_budget[c]["haut_B2"], "jeu_degenere": degenere[c]} for c in BUDGETS}
    extra = {"par_budget": detail}
    if any(degenere.values()):                                                      # ligne 1
        return _clore(trace, 1, A_DEGENERE, extra=extra)
    ok2 = {}
    for c in BUDGETS:
        a = _cmp(trace, f"est_{c}", par_budget[c]["est"], ">=", M)
        b = _cmp(trace, f"bas(B2)_{c}", par_budget[c]["bas_B2"], ">", 0.0)
        ok2[c] = a and b
    if ok2[1] and ok2[2]:                                                           # ligne 2
        return _clore(trace, 2, A_CONFIRMEE, extra=extra)
    neg = [_cmp(trace, f"haut(B2)_{c}", par_budget[c]["haut_B2"], "<", 0.0) for c in BUDGETS]
    if any(neg):                                                                    # ligne 3
        return _clore(trace, 3, A_REFUTEE, extra=extra)
    return _clore(trace, 4, A_NON_DEMONTREE, extra=extra)                           # ligne 4


def _classe_B_generique(bornes: dict, libelles: tuple) -> dict:
    bas8, haut8 = bornes["B8"]
    bas_e, haut_e = bornes["E8"]
    trace: list = []
    if _cmp(trace, "bas(B8)", bas8, ">", M):
        return _clore(trace, 1, libelles[0])
    if _cmp(trace, "haut(B8)", haut8, "<", -M):
        return _clore(trace, 2, libelles[1])
    a = _cmp(trace, "bas(E8)", bas_e, ">", -M)
    b = _cmp(trace, "haut(E8)", haut_e, "<", M)
    if a and b:
        return _clore(trace, 3, libelles[2])
    if _cmp(trace, "bas(B8)", bas8, ">", 0.0):
        return _clore(trace, 4, libelles[3])
    if _cmp(trace, "haut(B8)", haut8, "<", 0.0):
        return _clore(trace, 5, libelles[4])
    return _clore(trace, 6, libelles[5])


def classe_table_B(nom_court: str, bornes: dict) -> dict:
    """Table B — Δ(R_k, R2) sur V (signe + : R_k détecte mieux, donc est moins exploitable)."""
    k = nom_court
    return _classe_B_generique(bornes, (f"{k} > R2", f"R2 > {k}", EQUIVALENT, f"{k} ≳ R2", f"R2 ≳ {k}", INCERTAIN))


def classe_table_Bprime(nom_court: str, bornes: dict) -> dict:
    """Table B′ — D̄(R_k, R2) sur X̄ (signe + : R_k plus exploitable)."""
    k = nom_court
    return _classe_B_generique(bornes, (f"R2 > {k}", f"{k} > R2", EQUIVALENT, f"R2 ≳ {k}", f"{k} ≳ R2", INCERTAIN))


def classe_table_C(bornes: dict) -> dict:
    """Table C — Δ(R_k, R2) sur (ii), bornes B8, tolérance S5 ; on rend le numéro de ligne."""
    bas, haut = bornes["B8"]
    trace: list = []
    if _cmp(trace, "haut(B8)", haut, "<", -S5):
        return _clore(trace, 1, LIBELLES_TABLE_C[1])
    a = _cmp(trace, "haut(B8)", haut, "<", 0.0)
    b = _cmp(trace, "bas(B8)", bas, ">", -S5)
    if a and b:
        return _clore(trace, 2, LIBELLES_TABLE_C[2])
    if a:
        return _clore(trace, 3, LIBELLES_TABLE_C[3])
    if _cmp(trace, "bas(B8)", bas, ">", 0.0):
        return _clore(trace, 4, LIBELLES_TABLE_C[4])
    if _cmp(trace, "bas(B8)", bas, ">", -S5):
        return _clore(trace, 5, LIBELLES_TABLE_C[5])
    return _clore(trace, 6, LIBELLES_TABLE_C[6])


def classes_depuis_contrastes(contrastes: dict, moyennes_V: dict) -> dict:
    """Applique les tables A, B, B′, C à des contrastes au format du § 5.7.
    contrastes = {"1": {libellé: stat}, "2": {...}} ; moyennes_V = {"1": {nom de variante: moy}, ...}.
    Les moyennes de V servent seulement au prédicat « jeu dégénéré » de la table A."""
    bornes = {str(c): {(nom, mes): bornes_depuis_statistique(contrastes[str(c)][libelle_contraste(nom, mes)])
                       for nom, mes in TOUS_LES_CONTRASTES} for c in BUDGETS}
    entrees_A = {}
    for c in BUDGETS:
        stat = contrastes[str(c)][libelle_contraste("R3", "V")]
        b2 = bornes[str(c)][("R3", "V")]["B2"]
        entrees_A[c] = {"est": stat["moyenne"], "bas_B2": b2[0], "haut_B2": b2[1],
                        "moyennes_V": moyennes_V[str(c)]}
    classes = {"table_A": classe_table_A(entrees_A), "table_B": {}, "table_Bprime": {}, "table_C": {}}
    for nom in VARIANTES_CONTRASTEES:
        court = NOM_COURT[nom]
        classes["table_B"][court] = {str(c): classe_table_B(court, bornes[str(c)][(nom, "V")]) for c in BUDGETS}
        classes["table_Bprime"][court] = {str(c): classe_table_Bprime(court, bornes[str(c)][(nom, "Xbarre")])
                                          for c in BUDGETS}
        classes["table_C"][court] = {str(c): classe_table_C(bornes[str(c)][(nom, "ii")]) for c in BUDGETS}
    return classes


# ============================================================================================
# § 7 — contrôles de santé (recalculés depuis E1, par budget ; déclenché si au moins un budget)
# ============================================================================================
def controles_sante_budget(donnees: dict, contrastes_c: dict) -> dict:
    """T2 à T6 pour un budget. `contrastes_c` : {libellé: stat} du même budget. Chaque contrôle rend `declenche`
    (état), `frontiere` (marque, § 8) et les valeurs comparées."""
    ch = donnees["champs"]

    def moy(nom, champ):
        return float(np.mean(ch[nom][champ]))

    moyennes_V = {nom: moy(nom, "V_iii_final") for nom in NOMS_VARIANTES}

    # T2 — trop beau, trop mauvais (bloque toutes les lectures)
    tr: list = []
    trop_beau = [_cmp(tr, f"moy({NOM_COURT[nom]}, V)", moyennes_V[nom], ">=", SEUIL_T2_TROP_BEAU)
                 for nom in NOMS_VARIANTES]
    tous_mauvais = all([_cmp(tr, f"moy({NOM_COURT[nom]}, V)", moyennes_V[nom], "<=", DEUX_ALPHA)
                        for nom in NOMS_VARIANTES])
    est_r3 = contrastes_c[libelle_contraste("R3", "V")]["moyenne"]
    r3_trop_grand = _cmp(tr, "est(R3, V)", est_r3, ">", SEUIL_T2_EST_R3)
    est_xbarre = {nom: contrastes_c[libelle_contraste(nom, "Xbarre")]["moyenne"] for nom in VARIANTES_CONTRASTEES}
    xbarre_grand = [_cmp(tr, f"|est({NOM_COURT[nom]}, Xbarre)|", abs(est_xbarre[nom]), ">", SEUIL_T2_EST_XBARRE)
                    for nom in VARIANTES_CONTRASTEES]
    t2 = {"declenche": bool(any(trop_beau) or tous_mauvais or r3_trop_grand or any(xbarre_grand)),
          "une_variante_moy_V_ge_0_99": bool(any(trop_beau)),
          "cinq_variantes_moy_V_le_0_02": bool(tous_mauvais),
          "est_R3_V_gt_0_30": bool(r3_trop_grand),
          "un_abs_est_Xbarre_gt_0_30": bool(any(xbarre_grand)),
          "est_R3_V": est_r3,
          "abs_est_Xbarre": {NOM_COURT[nom]: abs(v) for nom, v in est_xbarre.items()}}
    t2.update(_marque(tr))

    # T3 — mélange dégénéré (bloque HR1). La comparaison du plus grand poids à S_PUR porte sur une valeur
    # brute de E1 et le compte est un entier : ni l'une ni l'autre ne marque (§ 8).
    plus_grands = [max(w) for w in donnees["poids_R3"]]
    nb_pur = sum(1 for g in plus_grands if g >= S_PUR)
    t3 = {"declenche": bool(nb_pur > SEUIL_T3_NB), "frontiere": False, "frontiere_propre": False,
          "heritee_de": [], "nb_taches_poids_pur": nb_pur, "seuil_nb": SEUIL_T3_NB,
          "plus_grand_poids_maximal": max(plus_grands),
          "information_nb_taches_a_moins_de_epsilon_de_s_pur": sum(1 for g in plus_grands if abs(g - S_PUR) <= EPS)}

    # T4 — régularisation dégénérée, S12 (bloque HR3 seulement). cos_moyen est une moyenne calculée : sa
    # comparaison à 0,999 compte pour la frontière (§ 8).
    cos_moyens = [sum(v) / 8 for v in donnees["cos_R4"]]
    tr4: list = []
    nb_cos = sum(1 for g in cos_moyens if _cmp(tr4, "cos_moyen", g, ">=", SEUIL_T4_COS))
    t4 = {"declenche": bool(nb_cos > SEUIL_T4_NB), "nb_taches_cos_moyen_ge_0_999": nb_cos, "seuil_nb": SEUIL_T4_NB,
          "nb_taches_a_la_frontiere": len(_proches(tr4))}
    t4.update({k: v for k, v in _marque(tr4).items() if k != "comparaisons_a_la_frontiere"})
    t4["comparaisons_a_la_frontiere"] = _proches(tr4)

    # T5 — optimiseur (bloque toutes les lectures ; point 11) : (a) unilatérale, (b) bilatérale
    tr5: list = []
    std_moins_ren = {nom: moy(nom, "V_iii_standard") - moy(nom, "V_iii_renforce") for nom in NOMS_VARIANTES}
    partie_a = [_cmp(tr5, f"moy_standard−moy_renforcé({NOM_COURT[nom]})", std_moins_ren[nom], ">", SEUIL_T5)
                for nom in NOMS_VARIANTES]
    ecart_contraste = {}
    partie_b = []
    for nom in VARIANTES_CONTRASTEES:
        a = float(np.mean(ch[nom]["V_iii_standard"] - ch["R2"]["V_iii_standard"]))
        b = float(np.mean(ch[nom]["V_iii_renforce"] - ch["R2"]["V_iii_renforce"]))
        ecart_contraste[NOM_COURT[nom]] = {"a_standard": a, "b_renforce": b, "a_moins_b": a - b}
        partie_b.append(_cmp(tr5, f"|a−b|({NOM_COURT[nom]})", abs(a - b), ">", SEUIL_T5))
    t5 = {"declenche": bool(any(partie_a) or any(partie_b)),
          "a_unilaterale_declenche": bool(any(partie_a)),
          "b_bilaterale_declenche": bool(any(partie_b)),
          "standard_moins_renforce": {NOM_COURT[n_]: v for n_, v in std_moins_ren.items()},
          "plus_grand_standard_moins_renforce": max(std_moins_ren.values()),
          "ecart_de_contraste": ecart_contraste,
          "plus_grand_abs_ecart_de_contraste": max(abs(v["a_moins_b"]) for v in ecart_contraste.values())}
    t5.update(_marque(tr5))

    # T6 — dérive des fausses alertes (bloque toutes les lectures)
    tr6: list = []
    ecarts_alpha = {nom: moy(nom, "fpr_final") - ALPHA for nom in NOMS_VARIANTES}
    deriv = [_cmp(tr6, f"|moy_fpr({NOM_COURT[nom]}) − α|", abs(ecarts_alpha[nom]), ">", SEUIL_T6)
             for nom in NOMS_VARIANTES]
    t6 = {"declenche": bool(any(deriv)),
          "moyenne_fpr_final": {NOM_COURT[nom]: moy(nom, "fpr_final") for nom in NOMS_VARIANTES},
          "plus_grand_abs_ecart_a_alpha": max(abs(v) for v in ecarts_alpha.values())}
    t6.update(_marque(tr6))

    return {"moyennes_V": moyennes_V, "jeu_degenere": bool(tous_mauvais),
            "T2": t2, "T3": t3, "T4": t4, "T5": t5, "T6": t6, "garde_coherence_V": "ok"}


def etats_globaux_sante(sante: dict) -> tuple:
    """(état, marque) globaux de chaque contrôle : déclenché (resp. marqué) s'il l'est dans au moins un des deux
    budgets (point 1 ; la marque suit la même règle)."""
    etat = {t: bool(any(sante[str(c)][t]["declenche"] for c in BUDGETS)) for t in ("T2", "T3", "T4", "T5", "T6")}
    front = {t: bool(any(sante[str(c)][t]["frontiere"] for c in BUDGETS)) for t in ("T2", "T3", "T4", "T5", "T6")}
    return etat, front


# ============================================================================================
# Verdicts : § 9 (course originale) et § 10.1 (réplication). Une marque de frontière (§ 8) est héritée de toute
# classe, de tout contrôle et de tout déclencheur qui ENTRE dans le chemin de décision du verdict (lignes
# examinées jusqu'à la première vraie comprise).
# ============================================================================================
def _agrege(ligne, verdict: str, trace: list, heritages: dict | None = None, extra: dict | None = None) -> dict:
    r = {"ligne": ligne, "verdict": verdict}
    r.update(_marque(trace, heritages))
    if extra:
        r.update(extra)
    return r


def _noms_classes(table: str, court: str) -> list:
    return [f"{table}/{court}/budget {c}" for c in BUDGETS]


def verdicts_regles_originales(classes: dict, etat: dict, front: dict) -> dict:
    """HR1, HR0, HR3, HR2 selon le § 9 (contrôles T2, T3, T5, T6 supposés non déclenchés ; T4 évalué)."""
    a = classes["table_A"]
    hr1 = _agrege(a["ligne"], a["classe"], [], {"table_A": a["frontiere"]})

    cl0 = classes["table_B"]["R0"]
    lib0 = [cl0[str(c)]["classe"] for c in BUDGETS]
    if all(x == "R2 > R0" for x in lib0):
        v0 = O_CONFIRMEE
    elif any(x in ("R0 > R2", "R0 ≳ R2", EQUIVALENT) for x in lib0):
        v0 = O_REFUTEE
    else:
        v0 = O_NON_TRANCHEE
    hr0 = _agrege(None, v0, [], {n: cl0[str(c)]["frontiere"] for n, c in zip(_noms_classes("table_B", "R0"), BUDGETS)},
                  {"classes": lib0})

    cl4 = classes["table_B"]["R4"]
    lib4 = [cl4[str(c)]["classe"] for c in BUDGETS]
    her3 = {"T4": front["T4"]}
    if etat["T4"]:
        v3 = V_HR3_SANS_VERDICT
    else:
        her3.update({n: cl4[str(c)]["frontiere"] for n, c in zip(_noms_classes("table_B", "R4"), BUDGETS)})
        if all(x in ("R4 > R2", "R4 ≳ R2", EQUIVALENT) for x in lib4):
            v3 = O_CONFIRMEE
        elif any(x == "R2 > R4" for x in lib4):
            v3 = O_REFUTEE
        else:
            v3 = O_NON_TRANCHEE
    hr3 = _agrege(None, v3, [], her3, {"classes": lib4, "T4_dans_au_moins_un_budget": bool(etat["T4"])})

    cl1 = classes["table_Bprime"]["R1"]
    lib1 = [cl1[str(c)]["classe"] for c in BUDGETS]
    if all(x == "R2 > R1" for x in lib1):
        v2 = O_CONFIRMEE
    elif any(x in ("R1 > R2", "R1 ≳ R2", EQUIVALENT) for x in lib1):
        v2 = O_REFUTEE
    else:
        v2 = O_NON_TRANCHEE
    hr2 = _agrege(None, v2, [], {n: cl1[str(c)]["frontiere"] for n, c in zip(_noms_classes("table_Bprime", "R1"), BUDGETS)},
                  {"classes": lib1})
    return {"HR1": hr1, "HR0": hr0, "HR3": hr3, "HR2": hr2,
            "hypothese": "contrôles T2, T3, T5, T6 supposés non déclenchés (§ 9) ; déclencheurs d'audit ignorés",
            "T2_T3_T5_T6_effectivement_non_declenches": not any(etat[t] for t in ("T2", "T3", "T5", "T6"))}


def verdict_HR1_replication(etat: dict, front: dict, par_budget: dict, moyennes_V: dict) -> dict:
    """§ 10.1 « HR1 répliquée ? ». par_budget[c] = {"est", "bas_B2", "haut_B2"} du contraste (R3, V) ;
    moyennes_V[str(c)] = {nom de variante: moy_c(k, V)}. La ligne 2 est inatteignable (sa condition fait partie
    de T2, testé à la ligne 1) ; elle est gardée pour correspondre mot pour mot à la Table A originale."""
    trace: list = []
    her = {t: front[t] for t in ("T2", "T3", "T5", "T6")}
    if etat["T2"] or etat["T3"] or etat["T5"] or etat["T6"]:                         # ligne 1
        return _agrege(1, V_SANTE, trace, her)
    jeu = {c: all([_cmp(trace, f"moy_{c}({NOM_COURT[nom]}, V)", moyennes_V[str(c)][nom], "<=", DEUX_ALPHA)
                   for nom in NOMS_VARIANTES]) for c in BUDGETS}
    if any(jeu.values()):                                                            # ligne 2 (inatteignable)
        return _agrege(2, V_DEGENERE, trace, her)
    ok3 = {}
    for c in BUDGETS:
        a = _cmp(trace, f"est_{c}", par_budget[c]["est"], ">=", TAU)
        b = _cmp(trace, f"bas(B2)_{c}", par_budget[c]["bas_B2"], ">", 0.0)
        ok3[c] = a and b
    if ok3[1] and ok3[2]:                                                            # ligne 3
        return _agrege(3, V_REPLIQUEE, trace, her)
    if any([_cmp(trace, f"haut(B2)_{c}", par_budget[c]["haut_B2"], "<", 0.0) for c in BUDGETS]):   # ligne 4
        return _agrege(4, V_HR1_SIGNE, trace, her)
    if any([_cmp(trace, f"haut(B2)_{c}", par_budget[c]["haut_B2"], "<", TAU) for c in BUDGETS]):   # ligne 5
        return _agrege(5, V_HR1_PETIT, trace, her)
    return _agrege(6, V_IMPRECIS, trace, her)                                        # ligne 6


def _heritages_classes(classes_par_budget: dict, table: str, court: str) -> dict:
    return {n: bool(classes_par_budget[c]["frontiere"]) for n, c in zip(_noms_classes(table, court), BUDGETS)}


def verdict_HR0_replication(etat: dict, front: dict, kappa: dict) -> dict:
    """§ 10.1 « HR0 répliquée ? ». kappa[c] = classe (dict de `classe_table_B`) de (R0, V) au budget c (c = 1, 2)."""
    k = [kappa[c]["classe"] for c in BUDGETS]
    her = {t: front[t] for t in ("T2", "T5", "T6")}
    if etat["T2"] or etat["T5"] or etat["T6"]:                                       # ligne 1
        return _agrege(1, V_SANTE, [], her)
    her.update(_heritages_classes(kappa, "table_B", "R0"))
    if any(x == "R2 > R0" for x in k):                                               # ligne 2
        return _agrege(2, V_HR0_INTERET, [], her)
    if any(x == "R2 ≳ R0" for x in k):                                               # ligne 3
        return _agrege(3, V_HR0_NON_NUL, [], her)
    if all(x in (EQUIVALENT, "R0 ≳ R2", "R0 > R2") for x in k):                      # ligne 4
        return _agrege(4, V_REPLIQUEE, [], her)
    return _agrege(5, V_IMPRECIS, [], her)                                           # ligne 5


def verdict_HR3_replication(etat: dict, front: dict, kappa: dict) -> dict:
    """§ 10.1 « HR3 répliquée ? » (secondaire). kappa[c] = classe de (R4, V) par la table B au budget c."""
    k = [kappa[c]["classe"] for c in BUDGETS]
    her = {t: front[t] for t in ("T2", "T5", "T6")}
    if etat["T2"] or etat["T5"] or etat["T6"]:                                       # ligne 1
        return _agrege(1, V_SANTE, [], her)
    her["T4"] = front["T4"]
    if etat["T4"]:                                                                   # ligne 2
        return _agrege(2, V_HR3_SANS_VERDICT, [], her)
    her.update(_heritages_classes(kappa, "table_B", "R4"))
    if any(x in ("R2 > R4", "R2 ≳ R4") for x in k):                                  # ligne 3
        return _agrege(3, V_NON_REPLIQUEE, [], her)
    if all(x in ("R4 > R2", "R4 ≳ R2", EQUIVALENT) for x in k):                      # ligne 4
        return _agrege(4, V_REPLIQUEE, [], her)
    return _agrege(5, V_IMPRECIS, [], her)                                           # ligne 5


def verdict_ii_replication(etat: dict, front: dict, classes_C: dict) -> dict:
    """§ 10.1 « lois tenues à l'écart, défense figée mieux que l'historique ? » (secondaire).
    classes_C[c] = classe (dict de `classe_table_C`, avec sa ligne) de (R0, (ii)) au budget c."""
    lg = [classes_C[c]["ligne"] for c in BUDGETS]
    her = {t: front[t] for t in ("T2", "T5", "T6")}
    if etat["T2"] or etat["T5"] or etat["T6"]:                                       # ligne 1
        return _agrege(1, V_SANTE, [], her)
    her.update(_heritages_classes(classes_C, "table_C", "R0"))
    if all(x == 4 for x in lg):                                                      # ligne 2
        return _agrege(2, V_REPLIQUEE, [], her)
    if any(x in (1, 2, 3) for x in lg):                                              # ligne 3
        return _agrege(3, V_HR1_SIGNE, [], her)
    return _agrege(4, V_IMPRECIS, [], her)                                           # ligne 4


def verdicts_bruts_replication(classes: dict, contrastes: dict, sante: dict, v9: dict) -> dict:
    """Les cinq lignes du § 10.1 (HR1, HR0, HR3, lois tenues à l'écart (ii), HR2 recopié du § 9)."""
    etat, front = sante["etat_global"], sante["frontiere_globale"]
    par_budget = {}
    for c in BUDGETS:
        stat = contrastes[str(c)][libelle_contraste("R3", "V")]
        bas, haut = bornes_depuis_statistique(stat)["B2"]
        par_budget[c] = {"est": stat["moyenne"], "bas_B2": bas, "haut_B2": haut}
    moyennes_V = {str(c): sante[str(c)]["moyennes_V"] for c in BUDGETS}
    hr1 = verdict_HR1_replication(etat, front, par_budget, moyennes_V)
    if hr1["ligne"] == 2:
        raise ErreurInterne("la ligne 2 de « HR1 répliquée ? » (inatteignable) a été atteinte : incohérence "
                            "entre T2 et le prédicat « jeu dégénéré »")
    cl0 = {c: classes["table_B"]["R0"][str(c)] for c in BUDGETS}
    cl4 = {c: classes["table_B"]["R4"][str(c)] for c in BUDGETS}
    clC = {c: classes["table_C"]["R0"][str(c)] for c in BUDGETS}
    hr0 = verdict_HR0_replication(etat, front, cl0)
    hr3 = verdict_HR3_replication(etat, front, cl4)
    iii = verdict_ii_replication(etat, front, clC)
    return {"HR1": hr1, "HR0": hr0, "HR3": hr3, "lois_tenues_ii": iii,
            "HR2": {**v9["HR2"], "note": "classes de (R1, X̄) par la Table B′ et verdict du § 9 recopiés, "
                                         "sans verdict de réplication"},
            "kappa_R0_V": {str(c): cl0[c]["classe"] for c in BUDGETS},
            "kappa_prime_R4_V": {str(c): cl4[c]["classe"] for c in BUDGETS},
            "lignes_C_R0_ii": {str(c): clC[c]["ligne"] for c in BUDGETS}}


# ============================================================================================
# § 10.2 — écart de réplication et déclencheurs d'audit symétriques
# ============================================================================================
def sigma_pi(s_rep: float, s_or: float) -> float:
    return math.sqrt(s_rep ** 2 / 100 + s_or ** 2 / 100)


def lire_primaires_E4(analyse_originale: dict) -> dict:
    """est_or et s_or des quatre contrastes primaires, lus dans l'analyse originale (E4)."""
    sortie = {}
    for nom, mes, c in PRIMAIRES:
        lib = libelle_contraste(nom, mes)
        try:
            ori = analyse_originale["resultat"][str(c)]["contrastes_contre_R2"][lib]
            sortie[(nom, mes, c)] = (_nombre(ori["moyenne"], f"E4 {lib} moyenne"),
                                     _nombre(ori["ecart_type"], f"E4 {lib} ecart_type"))
        except (KeyError, TypeError) as e:
            raise Arret(f"analyse originale : contraste « {lib} » du budget {c} introuvable ({e})") from None
    return sortie


def ecart_replication(contrastes_rep: dict, analyse_originale: dict) -> dict:
    """g, sigma, z des quatre contrastes primaires. `analyse_originale` : analyse de E4."""
    sortie = {}
    for (nom, mes, c), (est_or, s_or) in lire_primaires_E4(analyse_originale).items():
        lib = libelle_contraste(nom, mes)
        rep = contrastes_rep[str(c)][lib]
        g = rep["moyenne"] - est_or
        sigma = sigma_pi(rep["ecart_type"], s_or)
        z = (g / sigma) if sigma > 0 else None
        sortie[f"({NOM_COURT[nom]}, {mes}, c={c})"] = {
            "libelle": lib, "budget": c, "est_rep": rep["moyenne"], "s_rep": rep["ecart_type"],
            "est_or": est_or, "s_or": s_or, "g": g, "sigma": sigma, "z": z}
    return sortie


def declencheurs_audit(ecarts: dict, classes: dict, verdicts_bruts: dict) -> dict:
    """TR1 à TR4 et « au moins un », chacun avec sa marque de frontière. Toutes les comparaisons de chaque
    déclencheur sont évaluées (aucun court-circuit)."""
    # TR1 — |g| > z* × σ pour au moins un π (forme canonique soumise à la frontière)
    t1: list = []
    l1 = [_cmp(t1, f"|g|{cle}", abs(e["g"]), ">", Z_ETOILE * e["sigma"]) for cle, e in ecarts.items()]
    # TR2 — |g| < 0,001 pour les quatre π
    t2: list = []
    l2 = [_cmp(t2, f"|g|{cle}", abs(e["g"]), "<", SEUIL_TR2) for cle, e in ecarts.items()]
    # TR3 — κ_c ∈ {R0 > R2, R0 ≳ R2} dans au moins un budget
    cl0 = classes["table_B"]["R0"]
    l3 = [cl0[str(c)]["classe"] in ("R0 > R2", "R0 ≳ R2") for c in BUDGETS]
    h3 = {n: cl0[str(c)]["frontiere"] for n, c in zip(_noms_classes("table_B", "R0"), BUDGETS)}
    # TR4 — verdict brut de HR1 ou de HR0 commençant par « non répliquée »
    l4 = [verdicts_bruts["HR1"]["verdict"].startswith("non répliquée"),
          verdicts_bruts["HR0"]["verdict"].startswith("non répliquée")]
    h4 = {"HR1": verdicts_bruts["HR1"]["frontiere"], "HR0": verdicts_bruts["HR0"]["frontiere"]}
    d = {"TR1": {"nom": "écart de réplication, dans les deux sens", "declenche": bool(any(l1)), **_marque(t1)},
         "TR2": {"nom": "trop propre", "declenche": bool(all(l2)), **_marque(t2)},
         "TR3": {"nom": "défense figée plus belle que l'original", "declenche": bool(any(l3)), **_marque([], h3)},
         "TR4": {"nom": "non-réplication", "declenche": bool(any(l4)), **_marque([], h4)}}
    d["au_moins_un"] = {"declenche": bool(any(d[k]["declenche"] for k in ("TR1", "TR2", "TR3", "TR4"))),
                        **_marque([], {k: d[k]["frontiere"] for k in ("TR1", "TR2", "TR3", "TR4")})}
    return d


CLES_VERDICTS_REPLICATION = ("HR1", "HR0", "HR3", "lois_tenues_ii")


def verdicts_apres_declencheurs(verdicts_bruts: dict, declencheurs: dict) -> dict:
    """Effet des déclencheurs : s'il y en a au moins un, HR1, HR0, HR3 et (ii) deviennent « non jugeable (audit en
    attente) » jusqu'au rapport scellé de l'audit (HR2 n'a pas de verdict de réplication). Les marques des quatre
    déclencheurs sont héritées (ils sont tous évalués) ; celle du verdict brut l'est quand il subsiste."""
    au_moins = declencheurs["au_moins_un"]
    sortie = {}
    for k in CLES_VERDICTS_REPLICATION:
        if au_moins["declenche"]:
            sortie[k] = _agrege(None, V_AUDIT_ATTENTE, [], {"au_moins_un_TR": au_moins["frontiere"]},
                                {"origine": "déclencheur(s) d'audit"})
        else:
            sortie[k] = _agrege(verdicts_bruts[k]["ligne"], verdicts_bruts[k]["verdict"], [],
                                {"au_moins_un_TR": au_moins["frontiere"], f"{k} brut": verdicts_bruts[k]["frontiere"]},
                                {"origine": "verdict brut (aucun déclencheur)"})
    return sortie


# ============================================================================================
# § 10.3 — contrôle « graines neuves » (CL-10 : V, X̄ et (ii) ; arrêt si un compte > G = 2)
# ============================================================================================
def comptes_graines_neuves(donnees_rep: dict, donnees_orig: dict) -> dict:
    """Pour chaque variante et chacune des mesures V, X̄, (ii) : nombre de tâches (c, i) où la valeur de la
    réplication est égale AU BIT (binaire64, comparaison des 64 bits) à celle de la course originale à la même
    tâche. donnees_*[c] : sorties de extraire_donnees. Rend {variante: {champ: compte}} (quinze comptes)."""
    comptes = {}
    for nom in NOMS_VARIANTES:
        comptes[NOM_COURT[nom]] = {}
        for mes in MESURES_GRAINES:
            champ = MESURES[mes][1]
            total = 0
            for c in BUDGETS:
                a = np.ascontiguousarray(donnees_rep[c]["champs"][nom][champ]).view(np.uint64)
                b = np.ascontiguousarray(donnees_orig[c]["champs"][nom][champ]).view(np.uint64)
                total += int(np.count_nonzero(a == b))
            comptes[NOM_COURT[nom]][champ] = total
    return comptes


def resume_graines_neuves(comptes: dict) -> dict:
    au_dessus = [(v, champ, n) for v, par_champ in comptes.items() for champ, n in par_champ.items() if n > G_GRAINES]
    return {"comptes": comptes, "seuil_G": G_GRAINES, "regle": "arrêt si un des quinze comptes est strictement supérieur à G",
            "comptes_au_dessus_du_seuil": [{"variante": v, "mesure": champ, "compte": n} for v, champ, n in au_dessus],
            "arret_graines_non_neuves": bool(au_dessus)}


# ============================================================================================
# § 10.4 — issues globales
# ============================================================================================
def _vtexte(v):
    """(texte, marque) d'un verdict donné soit comme chaîne, soit comme dict de verdict."""
    if isinstance(v, str):
        return v, False
    return v["verdict"], bool(v.get("frontiere"))


def issue_globale(hr1, hr0, *, arret_controle: bool = False, plomberie_fausse: bool = False) -> dict:
    """Première ligne vraie du § 10.4. hr1 et hr0 : verdicts (chaîne ou dict). La ligne 1 est appliquée avec
    les seules conditions que B calcule : arrêt de contrôle (graines non neuves, discordance A/B) et l'option
    `plomberie_fausse` (valeur neutre : faux) ; V0 n'est pas évaluée par B."""
    t1, f1 = _vtexte(hr1)
    t0, f0 = _vtexte(hr0)
    if plomberie_fausse or arret_controle:
        ligne, front = 1, False
    else:
        front = bool(f1 or f0)
        if t1 == V_AUDIT_ATTENTE or t0 == V_AUDIT_ATTENTE:
            ligne = 2
        elif t1 == V_ARTEFACT or t0 == V_ARTEFACT:
            ligne = 3
        elif t1.startswith("non répliquée"):
            ligne = 4
        elif t1 == V_REPLIQUEE and t0 == V_REPLIQUEE:
            ligne = 5
        elif t1 == V_REPLIQUEE and t0.startswith("non répliquée"):
            ligne = 6
        elif t1 == V_REPLIQUEE and t0.startswith("non jugeable"):
            ligne = 7
        else:
            ligne = 8
    return {"ligne": ligne, "issue": ISSUES[ligne], "frontiere": front, "V0": MENTION_V0,
            "sous_reserve_de_V0": True}


# ============================================================================================
# Lecture d'une analyse (E4 ou E5) : contrastes validés
# ============================================================================================
def contrastes_depuis_analyse(analyse, role: str) -> dict:
    """Contrastes d'une analyse au format de l'analyse de la course originale : {"1": {libellé: stat}, "2": {...}},
    les 16 libellés par budget, chacun avec moyenne, ecart_type, n, zeros_exacts et les dix quantiles. Tout champ
    exigé absent ou mal typé est un arrêt d'entrée."""
    sortie = {}
    for c in BUDGETS:
        try:
            tous = analyse["resultat"][str(c)]["contrastes_contre_R2"]
        except (KeyError, TypeError) as e:
            raise Arret(f"{role} : contrastes du budget {c} absents ({e!r})") from None
        if not isinstance(tous, dict):
            raise Arret(f"{role} : `contrastes_contre_R2` du budget {c} doit être un objet")
        sortie[str(c)] = {}
        for nom, mes in TOUS_LES_CONTRASTES:
            lib = libelle_contraste(nom, mes)
            e = tous.get(lib)
            if not isinstance(e, dict):
                raise Arret(f"{role} : contraste « {lib} » du budget {c} absent")
            for cle in ("moyenne", "ecart_type", "n", "quantiles", "zeros_exacts"):
                if cle not in e:
                    raise Arret(f"{role} : contraste « {lib} » du budget {c} : champ `{cle}` absent")
            q = e["quantiles"]
            if not isinstance(q, dict) or any(k not in q for k in CLES_QUANTILES):
                raise Arret(f"{role} : contraste « {lib} » du budget {c} : quantiles incomplets")
            sortie[str(c)][lib] = {
                "moyenne": _nombre(e["moyenne"], f"{role} {lib} moyenne"),
                "ecart_type": _nombre(e["ecart_type"], f"{role} {lib} ecart_type"),
                "n": _entier(e["n"], f"{role} {lib} n"),
                "zeros_exacts": _entier(e["zeros_exacts"], f"{role} {lib} zeros_exacts"),
                "quantiles": {k: _nombre(q[k], f"{role} {lib} {k}") for k in CLES_QUANTILES}}
    return sortie


def verifier_rattachement_analyse(analyse, role: str, run_id: str, empreinte_manifeste: str) -> None:
    """E5 (ou toute analyse de A) : `run_id` égal à celui de E1 et `manifeste_sha256` égal à l'empreinte de E2."""
    if not isinstance(analyse, dict) or "run_id" not in analyse or "manifeste_sha256" not in analyse:
        raise Arret(f"{role} : `run_id` et `manifeste_sha256` exigés")
    if analyse["run_id"] != run_id:
        raise Arret(f"{role} : run_id {analyse['run_id']!r} ≠ celui de E1 ({run_id!r})")
    if analyse["manifeste_sha256"] != empreinte_manifeste:
        raise Arret(f"{role} : manifeste_sha256 ≠ l'empreinte du manifeste ({empreinte_manifeste})")


# ============================================================================================
# Lecture complète (classes, verdicts, déclencheurs) à partir de contrastes et de contrôles de santé
# ============================================================================================
def lecture_depuis_contrastes(contrastes: dict, sante: dict, analyse_originale: dict) -> dict:
    """Applique les tables, les verdicts et les déclencheurs à des contrastes au format du § 5.7 (ceux de B ou ceux
    de A) ; les contrôles de santé `sante` sont ceux recalculés par B depuis E1 (point 14)."""
    moyennes_V = {str(c): sante[str(c)]["moyennes_V"] for c in BUDGETS}
    classes = classes_depuis_contrastes(contrastes, moyennes_V)
    v9 = verdicts_regles_originales(classes, sante["etat_global"], sante["frontiere_globale"])
    vb = verdicts_bruts_replication(classes, contrastes, sante, v9)
    ecarts = ecart_replication(contrastes, analyse_originale)
    decl = declencheurs_audit(ecarts, classes, vb)
    va = verdicts_apres_declencheurs(vb, decl)
    return {"classes": classes, "verdicts_regles_originales": v9, "verdicts_bruts_replication": vb,
            "ecart_de_replication": {"constantes": {"z_etoile": Z_ETOILE, "seuil_TR2": SEUIL_TR2},
                                     "contrastes_primaires": ecarts},
            "declencheurs_audit": decl, "verdicts_apres_declencheurs": va}


def _lister_frontieres(classes: dict) -> list:
    out = []
    if classes["table_A"]["frontiere"]:
        out.append("table_A")
    for table in ("table_B", "table_Bprime", "table_C"):
        for court, par_c in classes[table].items():
            for c, cl in par_c.items():
                if cl["frontiere"]:
                    out.append(f"{table}/{court}/budget {c}")
    return out


# ============================================================================================
# Calcul de B sur des données déjà lues (aucun fichier)
# ============================================================================================
def calculer_B(e1, rho: int, rho_t: int, e4_analyse: dict, e4_resultats: dict, journal: list | None = None) -> dict:
    """Cœur de l'analyse : E1 déjà lu et vérifié ; (rho, rho_t) = racines attendues (règle D, ou celles de la
    course originale) ; E4 (analyse et résultats originaux) déjà lus et vérifiés. Rend un dictionnaire
    JSON-compatible, SANS comparaison avec A et SANS conclusion (voir `comparer_a_reference`, `conclure`)."""
    taches = valider_forme_E1(e1)
    controler_racines_taches(taches, rho, rho_t)
    par_budget = selectionner_taches(taches)
    donnees = {c: extraire_donnees(par_budget[c], c) for c in BUDGETS}

    contrastes = {str(c): calculer_contrastes_budget(donnees[c], c, rho) for c in BUDGETS}
    intervalles = {str(c): {lib: {k: [float(x) for x in v] for k, v in bornes_depuis_statistique(st).items()}
                            for lib, st in contrastes[str(c)].items()} for c in BUDGETS}
    sante = {str(c): controles_sante_budget(donnees[c], contrastes[str(c)]) for c in BUDGETS}
    etat, front = etats_globaux_sante(sante)
    sante["etat_global"], sante["frontiere_globale"] = etat, front
    lecture = lecture_depuis_contrastes(contrastes, sante, e4_analyse)

    # « graines neuves » : E4 passe par les mêmes gardes que E1 (racines de la course originale comprises)
    taches_or = valider_forme_E1(e4_resultats)
    controler_racines_taches(taches_or, RACINE_COURSE_ORIGINALE, RACINE_TENUE_COURSE_ORIGINALE)
    par_budget_or = selectionner_taches(taches_or)
    donnees_or = {c: extraire_donnees(par_budget_or[c], c) for c in BUDGETS}
    graines = resume_graines_neuves(comptes_graines_neuves(donnees, donnees_or))

    sortie = {
        "run_id": e1["run_id"],
        "resultat": {str(c): {"contrastes_contre_R2": contrastes[str(c)]} for c in BUDGETS},
        "intervalles": intervalles,
        "sante": sante,
        **lecture,
        "classes_a_la_frontiere": _lister_frontieres(lecture["classes"]),
        "comptes_graines_neuves": graines,
    }
    if journal is not None:
        journal.append("calcul de B terminé (statistiques, contrôles, classes, verdicts, déclencheurs, graines)")
    return sortie


# ============================================================================================
# § 11.2 — comparaison avec l'implémentation de référence A (E5)
# ============================================================================================
def comparer_contrastes(contrastes_b: dict, contrastes_a: dict) -> dict:
    """Écarts absolus, contraste par contraste. `niveau` : « arrêt » pour les cinq contrastes de concordance exigée
    (par budget), « alerte » pour les onze autres. `ok` : moyenne, écart-type et dix quantiles à ε près (inclus),
    et (lecture prudente) n et zéros exacts identiques."""
    detail = {}
    for c in BUDGETS:
        detail[str(c)] = {}
        for nom, mes in TOUS_LES_CONTRASTES:
            lib = libelle_contraste(nom, mes)
            sb, sa = contrastes_b[str(c)][lib], contrastes_a[str(c)][lib]
            niveau = "arrêt" if (nom, mes) in CONTRASTES_A_ARRET else "alerte"
            e_moy = abs(sb["moyenne"] - sa["moyenne"])
            e_sd = abs(sb["ecart_type"] - sa["ecart_type"])
            e_q = {cle: abs(sb["quantiles"][cle] - sa["quantiles"][cle]) for cle in CLES_QUANTILES}
            e_max = max([e_moy, e_sd, *e_q.values()])
            n_ok = bool(sb["n"] == sa["n"])
            z_ok = bool(sb["zeros_exacts"] == sa["zeros_exacts"])
            detail[str(c)][lib] = {
                "niveau": niveau, "ecart_moyenne": e_moy, "ecart_ecart_type": e_sd,
                "ecart_quantiles": e_q, "ecart_quantiles_max": max(e_q.values()), "ecart_max_abs": e_max,
                "n_identique": n_ok, "zeros_exacts_identiques": z_ok, "ok": bool(e_max <= EPS and n_ok and z_ok)}
    return detail


def _diff(chemin, eb: dict, ea: dict, vb, va, diffs: list, frontieres: list) -> None:
    """Compare un élément B à l'élément A ; une différence sur un élément marqué (de l'un ou l'autre côté) n'est
    pas un arrêt : la valeur retenue pour la lecture est celle calculée avec les nombres de A (§ 8)."""
    front = bool(eb.get("frontiere") or ea.get("frontiere"))
    if front:
        frontieres.append(chemin)
    if vb != va:
        diffs.append({"chemin": chemin, "B": vb, "A": va, "a_la_frontiere": front,
                      "valeur_retenue_pour_la_lecture": va if front else None})


def comparer_classes(classes_b: dict, classes_a: dict) -> dict:
    """Identité des lignes et des classes, table par table (§ 11.2)."""
    diffs, frontieres = [], []
    ligne_classe = lambda d: [d["ligne"], d["classe"]]
    _diff("table_A", classes_b["table_A"], classes_a["table_A"], ligne_classe(classes_b["table_A"]),
          ligne_classe(classes_a["table_A"]), diffs, frontieres)
    nb = 1
    for table in ("table_B", "table_Bprime", "table_C"):
        for court, par_c in classes_b[table].items():
            for c in par_c:
                _diff(f"{table}/{court}/budget {c}", par_c[c], classes_a[table][court][c],
                      ligne_classe(par_c[c]), ligne_classe(classes_a[table][court][c]), diffs, frontieres)
                nb += 1
    strictes = [d for d in diffs if not d["a_la_frontiere"]]
    return {"nombre_de_classes_comparees": nb, "differences": diffs, "differences_hors_frontiere": strictes,
            "elements_a_la_frontiere": frontieres, "identiques": not strictes}


def comparer_verdicts_et_declencheurs(lb: dict, la: dict) -> dict:
    """Verdicts du § 9, verdicts bruts du § 10.1, verdicts après déclencheurs et déclencheurs TR1 à TR4 : identiques
    entre B et les valeurs calculées sur les nombres de A, sauf élément marqué."""
    diffs, frontieres = [], []
    for k in ("HR1", "HR0", "HR3", "HR2"):
        _diff(f"verdicts_regles_originales/{k}", lb["verdicts_regles_originales"][k], la["verdicts_regles_originales"][k],
              lb["verdicts_regles_originales"][k]["verdict"], la["verdicts_regles_originales"][k]["verdict"], diffs, frontieres)
    for k in ("HR1", "HR0", "HR3", "lois_tenues_ii", "HR2"):
        eb, ea = lb["verdicts_bruts_replication"][k], la["verdicts_bruts_replication"][k]
        _diff(f"verdicts_bruts_replication/{k}", eb, ea, [eb.get("ligne"), eb["verdict"]], [ea.get("ligne"), ea["verdict"]],
              diffs, frontieres)
    for k in CLES_VERDICTS_REPLICATION:
        eb, ea = lb["verdicts_apres_declencheurs"][k], la["verdicts_apres_declencheurs"][k]
        _diff(f"verdicts_apres_declencheurs/{k}", eb, ea, eb["verdict"], ea["verdict"], diffs, frontieres)
    for k in ("TR1", "TR2", "TR3", "TR4"):
        eb, ea = lb["declencheurs_audit"][k], la["declencheurs_audit"][k]
        _diff(f"declencheurs_audit/{k}", eb, ea, eb["declenche"], ea["declenche"], diffs, frontieres)
    strictes = [d for d in diffs if not d["a_la_frontiere"]]
    return {"differences": diffs, "differences_hors_frontiere": strictes, "elements_a_la_frontiere": frontieres,
            "identiques": not strictes}


def comparer_a_reference(sortie_b: dict, contrastes_a: dict, analyse_originale: dict) -> dict:
    """§ 11.2. `sortie_b` : sortie de `calculer_B` ; `contrastes_a` : contrastes validés de E5
    (`contrastes_depuis_analyse`). Les classes, verdicts et déclencheurs « de A » sont calculés avec les nombres de A
    et les contrôles de santé recalculés par B depuis E1 (point 14). Rend le résultat de la comparaison, dont
    `discordance_a_arret` (arrêt de contrôle, code 3) et les `alertes` (onze autres contrastes)."""
    contrastes_b = {c: sortie_b["resultat"][c]["contrastes_contre_R2"] for c in ("1", "2")}
    detail = comparer_contrastes(contrastes_b, contrastes_a)
    lecture_a = lecture_depuis_contrastes(contrastes_a, sortie_b["sante"], analyse_originale)
    cmp_classes = comparer_classes(sortie_b["classes"], lecture_a["classes"])
    cmp_verdicts = comparer_verdicts_et_declencheurs(sortie_b, lecture_a)
    z_b = {k: v["z"] for k, v in sortie_b["ecart_de_replication"]["contrastes_primaires"].items()}
    z_a = {k: v["z"] for k, v in lecture_a["ecart_de_replication"]["contrastes_primaires"].items()}
    ecarts_z = {k: (abs(z_a[k] - z_b[k]) if z_a[k] is not None and z_b[k] is not None else
                    (0.0 if z_a[k] is None and z_b[k] is None else math.inf)) for k in z_a}
    z_ok = all(v <= EPS for v in ecarts_z.values())

    tous = [(c, lib, d) for c in detail for lib, d in detail[c].items()]
    a_arret = [(c, lib, d) for c, lib, d in tous if d["niveau"] == "arrêt"]
    a_alerte = [(c, lib, d) for c, lib, d in tous if d["niveau"] == "alerte"]
    motifs = []
    for c, lib, d in a_arret:
        if not d["ok"]:
            motifs.append(f"contraste de concordance exigée « {lib} » (budget {c}) : écart max {d['ecart_max_abs']:.3e}"
                          f"{'' if d['n_identique'] and d['zeros_exacts_identiques'] else ', n ou zéros exacts différents'}")
    if not z_ok:
        motifs.append("écarts réduits z_π(A) et z_π(B) différents de plus de ε : "
                      + ", ".join(f"{k}: {v:.3e}" for k, v in ecarts_z.items() if v > EPS))
    for d in cmp_classes["differences_hors_frontiere"]:
        motifs.append(f"classe différente hors frontière : {d['chemin']} (B {d['B']}, A {d['A']})")
    for d in cmp_verdicts["differences_hors_frontiere"]:
        motifs.append(f"verdict ou déclencheur différent hors frontière : {d['chemin']} (B {d['B']}, A {d['A']})")
    alertes = [{"budget": c, "contraste": lib, "ecart_max_abs": d["ecart_max_abs"]} for c, lib, d in a_alerte if not d["ok"]]
    return {
        "evaluee": True, "tolerance": EPS,
        "detail_par_contraste": detail,
        "ecart_maximal_absolu": max(d["ecart_max_abs"] for _, _, d in tous),
        "ecart_maximal_absolu_contrastes_a_arret": max(d["ecart_max_abs"] for _, _, d in a_arret),
        "ecart_maximal_absolu_contrastes_a_alerte": max(d["ecart_max_abs"] for _, _, d in a_alerte),
        "z_pi": {"A": z_a, "B": z_b, "ecart_abs": ecarts_z, "ok": z_ok},
        "classes": cmp_classes, "verdicts_et_declencheurs": cmp_verdicts,
        "alertes_de_discordance": alertes,
        "discordance_a_arret": bool(motifs), "motifs": motifs,
        "concordance": bool(not motifs and not alertes),
    }


# ============================================================================================
# Conclusion : arrêts de contrôle, lecture autorisée, issues globales, code de sortie (§ 10.4, § 11.1)
# ============================================================================================
def conclure(sortie: dict, *, plomberie_fausse: bool = False) -> dict:
    """Ajoute à la sortie `motifs_arret`, `lecture_autorisee`, `code_de_sortie` (0 ou 3) et les deux issues
    globales (brute et après déclencheurs), « sous réserve de V0 »."""
    motifs = []
    g = sortie["comptes_graines_neuves"]
    if g["arret_graines_non_neuves"]:
        motifs.append("graines non neuves : " + ", ".join(
            f"{x['variante']} {x['mesure']} = {x['compte']}" for x in g["comptes_au_dessus_du_seuil"])
            + f" (arrêt si un compte est strictement supérieur à {G_GRAINES})")
    cmp_ab = sortie.get("comparaison_A_B", {"evaluee": False})
    if cmp_ab.get("evaluee") and cmp_ab["discordance_a_arret"]:
        motifs.append("discordance A/B de niveau arrêt : " + " ; ".join(cmp_ab["motifs"]))
    arret = bool(motifs)
    vb, va = sortie["verdicts_bruts_replication"], sortie["verdicts_apres_declencheurs"]
    sortie["motifs_arret"] = motifs
    sortie["lecture_autorisee"] = not arret
    sortie["code_de_sortie"] = 3 if arret else 0
    sortie["issues_globales"] = {
        "V0": MENTION_V0,
        "brute": issue_globale(vb["HR1"], vb["HR0"], arret_controle=arret, plomberie_fausse=plomberie_fausse),
        "apres_declencheurs": issue_globale(va["HR1"], va["HR0"], arret_controle=arret,
                                            plomberie_fausse=plomberie_fausse),
        "regle_de_lecture": ("Avant tout audit, l'issue après déclencheurs vaut ; après un audit « pas d'artefact », "
                             "l'issue brute vaut avec la mention « après audit » ; après un audit « artefact trouvé », "
                             "l'issue est « non jugeable (artefact) ». La ligne 1 du § 10.4 dépend de V0, que B ne peut "
                             "pas évaluer : le lecteur l'applique en entier."),
    }
    return sortie


# ============================================================================================
# Sortie JSON neuve (jamais écrasée) et analyse « de bout en bout » depuis les fichiers
# ============================================================================================
def ecrire_json_neuf(chemin, objet) -> str:
    """Écrit un fichier JSON neuf (création exclusive : jamais écrasé). Rend son empreinte."""
    chemin = Path(chemin)
    texte = json.dumps(objet, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    try:
        with open(chemin, "x", encoding="utf-8", newline="\n") as f:
            f.write(texte)
    except FileExistsError:
        raise FileExistsError(f"{chemin} existe déjà : une nouvelle version porte un nouveau nom") from None
    return empreinte_octets(texte.encode("utf-8"))


def verifier_E2(e2, e1: dict, sha_e2: str, h: str, rho: int, rho_t: int) -> dict:
    """Vérifications de E2 (§ 3, point 5), chacune un arrêt d'entrée. Rend les valeurs lues, pour la sortie."""
    if not isinstance(e2, dict):
        raise Arret("E2 : objet attendu")

    def champ(obj, chemin):
        cur = obj
        for k in chemin:
            if not isinstance(cur, dict) or k not in cur:
                raise Arret(f"E2 : champ `{'.'.join(chemin)}` absent")
            cur = cur[k]
        return cur

    # 1. rattachement à E1
    if sha_e2 != e1["manifeste_sha256"]:
        raise Arret("E2 : l'empreinte du manifeste ≠ manifeste_sha256 de E1")
    if champ(e2, ["run_id"]) != e1["run_id"]:
        raise Arret("E2 : run_id ≠ celui de E1")
    # 2. racines (entiers exacts) et leurs écritures décimales
    if _entier(champ(e2, ["config", "racine"]), "E2 config.racine") != rho or \
            _entier(champ(e2, ["config", "racine_tenue"]), "E2 config.racine_tenue") != rho_t:
        raise Arret("E2 : (config.racine, config.racine_tenue) ≠ (rho, rho_t) de la règle D")
    cfg = e2["config"]
    if "racine_chaine" in cfg and cfg["racine_chaine"] != str(rho):
        raise Arret("E2 : config.racine_chaine ≠ l'écriture décimale de rho")
    if "racine_tenue_chaine" in cfg and cfg["racine_tenue_chaine"] != str(rho_t):
        raise Arret("E2 : config.racine_tenue_chaine ≠ l'écriture décimale de rho_t")
    # 3. préenregistrement
    sha_prereg = champ(e2, ["preenregistrement", "sha256"])
    if champ(e2, ["config", "prereg_sha256"]) != h or sha_prereg != h:
        raise Arret("E2 : config.prereg_sha256 et preenregistrement.sha256 doivent être égaux à H recalculé")
    # 4. λ et référence
    lam = champ(e2, ["config", "lambda"])
    if isinstance(lam, bool) or not isinstance(lam, (int, float)) or lam != LAMBDA_ATTENDU:
        raise Arret(f"E2 : config.lambda = {lam!r} ≠ {LAMBDA_ATTENDU}")
    if champ(e2, ["config", "reference"]) != REFERENCE_ATTENDUE:
        raise Arret(f"E2 : config.reference ≠ « {REFERENCE_ATTENDUE} »")
    # 5. N et configuration
    n_inst = champ(e2, ["config", "config", "n_instances"])
    if isinstance(n_inst, bool) or not isinstance(n_inst, int) or n_inst != N:
        raise Arret(f"E2 : config.config.n_instances = {n_inst!r} ≠ {N}")
    if champ(e2, ["config", "config_sha256"]) != EMPREINTE_CONFIG:
        raise Arret("E2 : config.config_sha256 ≠ l'empreinte de configuration épinglée")
    return {"run_id": e2["run_id"], "lambda": lam, "reference": cfg["reference"], "n_instances": n_inst,
            "config_sha256": cfg["config_sha256"], "prereg_sha256": h}


def analyser_fichiers(*, mode: str, resultats, analyse_originale, resultats_originaux, prereg=None, manifeste=None,
                      analyse_A=None, empreinte_E1=None, plomberie_fausse: bool = False) -> dict:
    """Lit et vérifie les fichiers (§ 3), dérive ou impose les racines, calcule B, PUIS lit E5 et compare, enfin conclut.
    Deux modes :
    - `replication` : E1 (compagnon), E2 (compagnon), E3 (compagnon), E4 (empreintes épinglées), E5 (compagnon)
      obligatoires ; racines par la règle D ;
    - `essai` : pièces de la course originale ou de ses variantes (§ 12.1, § 12.3) ; racines (20266201, 20266202) ;
      E5 facultative ; E1 : compagnon, sinon empreinte `empreinte_E1`, sinon empreinte des résultats originaux."""
    t0 = time.perf_counter()
    fichiers: list = []
    journal: list = []

    def noter(role, chemin, sha):
        fichiers.append({"role": role, "fichier": Path(chemin).name, "sha256": sha})
        journal.append(f"lecture de {role}")

    if mode not in ("replication", "essai"):
        raise Arret(f"mode inconnu : {mode!r}")
    if mode == "replication":
        if prereg is None or manifeste is None or analyse_A is None:
            raise Arret("réplication : E3 (préenregistrement), E2 (manifeste) et E5 (analyse de A) sont obligatoires")
        if empreinte_E1 is not None:
            raise Arret("réplication : l'empreinte de E1 vient du compagnon, jamais de la ligne de commande")
    else:
        if prereg is not None or manifeste is not None:
            raise Arret("essai : pas de préenregistrement ni de manifeste (racine de la course originale)")
    if analyse_originale is None or resultats_originaux is None:
        raise Arret("E4 (analyse et résultats originaux) est obligatoire")

    # E1
    if mode == "replication":
        octets_e1, sha_e1 = lire_fichier_verifie(resultats, "E1")
    elif empreinte_E1 is not None:
        octets_e1, sha_e1 = lire_fichier_verifie(resultats, "E1", attendue=empreinte_E1)
    else:
        octets_e1, sha_e1 = lire_fichier_compagnon_ou_epingle(resultats, "E1", (EMPREINTE_RESULTATS_ORIGINAUX,))
    noter("E1 résultats analysés", resultats, sha_e1)
    e1 = lire_json_octets(octets_e1, "E1")
    valider_forme_E1(e1)

    # E4 (empreintes épinglées, sans compagnon)
    o, sha = lire_fichier_verifie(analyse_originale, "E4 analyse originale", attendue=EMPREINTE_ANALYSE_ORIGINALE)
    e4_analyse = lire_json_octets(o, "E4 analyse originale")
    noter("E4 analyse originale", analyse_originale, sha)
    o, sha = lire_fichier_verifie(resultats_originaux, "E4 résultats originaux", attendue=EMPREINTE_RESULTATS_ORIGINAUX)
    e4_resultats = lire_json_octets(o, "E4 résultats originaux")
    noter("E4 résultats originaux", resultats_originaux, sha)

    # racines
    info_e2 = None
    sha_e2 = None
    if mode == "replication":
        octets_e3, sha_e3 = lire_fichier_verifie(prereg, "E3 préenregistrement")
        noter("E3 préenregistrement scellé", prereg, sha_e3)
        octets_e2, sha_e2 = lire_fichier_verifie(manifeste, "E2 manifeste")
        noter("E2 manifeste du run", manifeste, sha_e2)
        e2 = lire_json_octets(octets_e2, "E2")
        h, rho, rho_t = regle_d_depuis_octets(octets_e3)
        info_e2 = verifier_E2(e2, e1, sha_e2, h, rho, rho_t)
        racines = {"origine": "règle D appliquée au texte scellé (E3)", "rho": str(rho), "rho_t": str(rho_t),
                   "controle": "racines de E2 et des 200 tâches de E1 égales à (rho, rho_t), comparées comme entiers exacts"}
    else:
        h, rho, rho_t = None, RACINE_COURSE_ORIGINALE, RACINE_TENUE_COURSE_ORIGINALE
        racines = {"origine": "course originale (essai)", "rho": str(rho), "rho_t": str(rho_t)}

    sortie = calculer_B(e1, rho, rho_t, e4_analyse, e4_resultats, journal)

    # E5 : lue seulement APRÈS le calcul de B (§ 3)
    if analyse_A is not None:
        if mode == "replication":
            o5, sha5 = lire_fichier_verifie(analyse_A, "E5 analyse de A")
        else:
            o5, sha5 = lire_fichier_compagnon_ou_epingle(analyse_A, "E5 analyse de A", (EMPREINTE_ANALYSE_ORIGINALE,))
        noter("E5 analyse de A", analyse_A, sha5)
        e5 = lire_json_octets(o5, "E5")
        verifier_rattachement_analyse(e5, "E5", e1["run_id"], sha_e2 if mode == "replication" else e1["manifeste_sha256"])
        contrastes_a = contrastes_depuis_analyse(e5, "E5")
        sortie["comparaison_A_B"] = comparer_a_reference(sortie, contrastes_a, e4_analyse)
    else:
        sortie["comparaison_A_B"] = {"evaluee": False, "raison": "E5 absente (mode essai) : discordance A/B non évaluée"}
    conclure(sortie, plomberie_fausse=plomberie_fausse)

    entete = {
        "implementation": f"{NOM_FICHIER_IMPLEMENTATION} ({VERSION_IMPLEMENTATION})",
        "specification": {"fichier": "specification-statistique-decisive-v2.md", "sha256_epinglee": EMPREINTE_SPECIFICATION_V2},
        "mode": mode,
        "H": h,
        "racines": racines,
        "racine_de_reechantillonnage": str(rho),
        "manifeste_E2": info_e2,
    }
    options = {"mode": mode, "plomberie_fausse_V0": bool(plomberie_fausse),
               "empreinte_E1_imposee_en_ligne_de_commande": empreinte_E1}
    meta = {"versions": {"python": platform.python_version(), "numpy": np.__version__,
                         "implementation": VERSION_IMPLEMENTATION},
            "duree_calcul_s": round(time.perf_counter() - t0, 3)}
    return {**entete, **sortie, "options": options, "empreintes_fichiers": fichiers, "ordre_des_lectures": journal,
            "meta_non_deterministe": meta}


# ============================================================================================
# Ligne de commande
# ============================================================================================
def _imprimer_json(objet) -> None:
    sys.stdout.write(json.dumps(objet, ensure_ascii=False, indent=2, allow_nan=False) + "\n")


def _executer(a, mode: str) -> int:
    sortie_chemin = Path(a.sortie)
    if sortie_chemin.exists():
        sys.stderr.write(f"ARRÊT : {sortie_chemin} existe déjà (jamais écrasé ; nouvelle version = nouveau nom)\n")
        return 2
    try:
        res = analyser_fichiers(
            mode=mode, resultats=a.resultats, analyse_originale=a.analyse_originale,
            resultats_originaux=a.resultats_originaux, prereg=getattr(a, "prereg", None),
            manifeste=getattr(a, "manifeste", None), analyse_A=a.analyse_A,
            empreinte_E1=getattr(a, "empreinte_e1", None), plomberie_fausse=a.plomberie_fausse)
    except (Arret, ErreurInterne) as e:
        sys.stderr.write(f"ARRÊT : {e}\n")
        return 2
    try:
        sha = ecrire_json_neuf(sortie_chemin, res)
    except FileExistsError as e:
        sys.stderr.write(f"ARRÊT : {e}\n")
        return 2
    sys.stderr.write(f"sortie écrite : {sortie_chemin} (sha256 {sha})\n")
    if res["motifs_arret"]:
        sys.stderr.write("ARRÊT DE CONTRÔLE (lecture non autorisée) : " + " ; ".join(res["motifs_arret"]) + "\n")
    return res["code_de_sortie"]


def _cmd_replication(a) -> int:
    return _executer(a, "replication")


def _cmd_essai(a) -> int:
    return _executer(a, "essai")


def _cmd_regle_d(a) -> int:
    try:
        if a.prereg:
            octets, sha = lire_fichier_verifie(a.prereg, "E3 préenregistrement")
            h = sha
        else:
            h = a.empreinte
        rho, rho_t = regle_d_derivation(h)
        try:
            regle_d_gardes(rho, rho_t)
            gardes = "ok"
        except Arret as e:
            gardes = f"ARRÊT : {e}"
    except Arret as e:
        sys.stderr.write(f"ARRÊT : {e}\n")
        return 2
    _imprimer_json({"H": h, "E_decimal": str(int(h, 16)), "rho": str(rho), "rho_t": str(rho_t), "gardes": gardes})
    return 0 if gardes == "ok" else 2


def _parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog=NOM_FICHIER_IMPLEMENTATION, description=__doc__.split("\n\n")[0])
    sp = ap.add_subparsers(dest="commande", required=True)

    def commun(p, avec_E5_obligatoire: bool):
        p.add_argument("--resultats", required=True, help="E1 : fichier de résultats")
        p.add_argument("--analyse-originale", required=True, help="E4 : analyse de la course originale")
        p.add_argument("--resultats-originaux", required=True, help="E4 : résultats de la course originale")
        p.add_argument("--analyse-A", required=avec_E5_obligatoire, help="E5 : analyse de l'implémentation de référence A")
        p.add_argument("--plomberie-fausse", action="store_true",
                       help="option du § 10.4, ligne 1 : V0 de la réplication faux (défaut neutre : non) ; valeur écrite dans la sortie")
        p.add_argument("--sortie", required=True, help="fichier JSON neuf (jamais écrasé)")

    rp = sp.add_parser("replication", help="la réplication (racines par la règle D)")
    rp.add_argument("--manifeste", required=True, help="E2 : manifeste du run")
    rp.add_argument("--prereg", required=True, help="E3 : préenregistrement scellé")
    commun(rp, True)
    rp.set_defaults(fonction=_cmd_replication)

    es = sp.add_parser("essai", help="essai sur la course originale ou ses variantes (racine 20266201)")
    es.add_argument("--empreinte-e1", help="empreinte épinglée de E1 (variante de la course originale, sans compagnon)")
    commun(es, False)
    es.set_defaults(fonction=_cmd_essai)

    rd = sp.add_parser("regle-d", help="règle D (§ 4)")
    g = rd.add_mutually_exclusive_group(required=True)
    g.add_argument("--prereg", help="préenregistrement scellé (compagnon requis)")
    g.add_argument("--empreinte", help="empreinte H en 64 hexadécimaux minuscules")
    rd.set_defaults(fonction=_cmd_regle_d)

    va = sp.add_parser("valider-originale", help="validation complète du § 12")
    va.add_argument("--dossier", default=str(Path(__file__).resolve().parent),
                    help="dossier contenant entrees/ (par défaut : celui du module)")
    va.add_argument("--dossier-sortie", help="dossier d'écriture (par défaut : --dossier)")
    va.add_argument("--executer-essais", action="store_true",
                    help="lance aussi la suite d'essais (pytest) et en consigne les comptes")
    va.add_argument("--mutations", help="« détectées/total » de la campagne de mutations (consigné tel quel)")
    va.set_defaults(fonction=_cmd_valider)
    return ap


def main(argv=None) -> int:
    a = _parser().parse_args(argv)
    return a.fonction(a)


# ============================================================================================
# § 12 — validation obligatoire
# ============================================================================================
NOM_SORTIE_B = "sortie-b-originale-v2.json"
NOM_VALIDATION_JSON = "validation-b-v2.json"
NOM_VALIDATION_MD = "validation-b-v2.md"
NOM_TESTS = "test_implementation_b_v2.py"

# Classes, contrôles et verdicts annoncés par le § 12.1 pour la course originale (budget 1, budget 2).
ATTENDU_12 = {
    "table_A": (2, A_CONFIRMEE),
    "table_B": {"R0": (EQUIVALENT, EQUIVALENT), "R1": ("R2 ≳ R1", INCERTAIN),
                "R3": ("R3 > R2", "R3 > R2"), "R4": ("R4 ≳ R2", "R4 ≳ R2")},
    "table_Bprime": {"R0": (EQUIVALENT, EQUIVALENT), "R1": ("R2 > R1", "R2 ≳ R1"),
                     "R3": ("R3 > R2", "R3 > R2"), "R4": ("R4 ≳ R2", "R4 ≳ R2")},
    "table_C": {"R0": (4, 4), "R1": (4, 4), "R3": (1, 1), "R4": (4, 4)},
    "T3_nb_taches_poids_pur": (0, 0),
    "T4_nb_taches": (5, 2),
    "T5_plus_grand_standard_moins_renforce_arrondi_5_decimales": 0.00039,
    "T5_plus_grand_ecart_de_contraste_arrondi_5_decimales": 0.00043,
    "T6_plus_grand_ecart_a_alpha_arrondi_5_decimales": 0.00019,
    "verdicts_9": {"HR1": A_CONFIRMEE, "HR0": O_REFUTEE, "HR3": O_CONFIRMEE, "HR2": O_NON_TRANCHEE},
}


def lire_table_12(texte: str) -> list:
    """Extrait du texte de la spécification le tableau de valeurs de contrôle du § 12.1 (dix lignes) :
    budget, variante, mesure, moyenne, écart-type, q(0,003125), q(0,00625), q(0,99375), q(0,996875)."""
    lignes = texte.split("\n")
    debut = next((i for i, ligne in enumerate(lignes) if ligne.startswith("## 12.")), None)
    if debut is None:
        raise Arret("spécification : section 12 introuvable")
    mesures = {"V": "V", "(ii)": "ii", "X̄": "Xbarre"}
    rangees = []
    for ligne in lignes[debut:]:
        if not ligne.startswith("|"):
            continue
        cellules = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if len(cellules) != 8 or cellules[0] not in ("1", "2"):
            continue
        m = re.fullmatch(r"(R\d) - R2, (V|\(ii\)|X̄)", cellules[1].replace("−", "-"))
        if m is None:
            raise Arret(f"spécification : ligne de contrôle illisible : {cellules[1]!r}")
        v = [float(x.replace("−", "-")) for x in cellules[2:]]
        nom = NOM_R4 if m.group(1) == "R4" else m.group(1)
        rangees.append({"budget": int(cellules[0]), "variante": nom, "mesure": mesures[m.group(2)],
                        "moyenne": v[0], "ecart_type": v[1],
                        "q0.003125": v[2], "q0.00625": v[3], "q0.99375": v[4], "q0.996875": v[5]})
    return rangees


def _vecteurs_regle_d() -> dict:
    sortie = {"vecteurs": [], "gardes_rejettent_les_six_entiers": True}
    for h, rho_att, rho_t_att in VECTEURS_REGLE_D:
        rho, rho_t = regle_d_derivation(h)
        try:
            regle_d_gardes(rho, rho_t)
            rejete = False
        except Arret:
            rejete = True
        sortie["gardes_rejettent_les_six_entiers"] &= rejete
        sortie["vecteurs"].append({"H": h, "rho": str(rho), "rho_t": str(rho_t), "rho_attendu": str(rho_att),
                                   "rho_t_attendu": str(rho_t_att), "ok": (rho, rho_t) == (rho_att, rho_t_att),
                                   "gardes_rejettent_ce_vecteur": rejete})
    h0 = VECTEURS_REGLE_D[0][0]
    rho, rho_t = regle_d_derivation(h0)
    sortie["cas_sain"] = {"H_preenregistrement_original": h0, "rho": str(rho), "rho_t": str(rho_t),
                          "differe_de_20266201_20266202": (rho, rho_t) != (20266201, 20266202)}
    sortie["ok"] = (all(v["ok"] for v in sortie["vecteurs"]) and sortie["gardes_rejettent_les_six_entiers"]
                    and sortie["cas_sain"]["differe_de_20266201_20266202"])
    return sortie


def _vecteurs_generateur() -> dict:
    sortie = {"vecteurs": []}
    for v in VECTEURS_GENERATEUR:
        c, code = v["cle"][0], v["cle"][1]
        ind = indices_reechantillonnage(RACINE_COURSE_ORIGINALE, c, code)
        d10, f5 = [int(x) for x in ind[0, :10]], [int(x) for x in ind[-1, -5:]]
        sortie["vecteurs"].append({
            "racine": RACINE_COURSE_ORIGINALE, "cle": list(v["cle"]), "forme": list(ind.shape),
            "dtype": str(ind.dtype), "ligne0_dix_premiers": d10, "attendu": v["ligne0_dix_premiers"],
            "derniere_ligne_cinq_derniers": f5, "attendu_derniere": v["derniere_ligne_cinq_derniers"],
            "ok": d10 == v["ligne0_dix_premiers"] and f5 == v["derniere_ligne_cinq_derniers"]})
    sortie["ok"] = all(v["ok"] for v in sortie["vecteurs"])
    return sortie


def _entiers_64_bits() -> dict:
    """§ 12.4 : lecture exacte, comparaison exacte et écriture en chaîne exacte d'entiers de plus de 2^63."""
    grand = 2 ** 64 - 59
    lu = lire_json_octets(f'{{"racine": {grand}, "autre": {grand + 1}}}'.encode(), "essai")
    ecrit = json.loads(json.dumps({"racine": str(lu["racine"])}))
    return {"entier_essai": str(grand), "lu_exactement": lu["racine"] == grand and lu["autre"] == grand + 1,
            "voisins_distincts_comme_entiers": lu["racine"] != lu["autre"],
            "voisins_confondus_si_binaire64": float(grand) == float(grand + 1),
            "ecrit_en_chaine_exacte": ecrit["racine"] == str(grand),
            "ok": bool(lu["racine"] == grand and lu["racine"] != lu["autre"] and float(grand) == float(grand + 1)
                       and ecrit["racine"] == str(grand))}


def _table_12(res: dict, texte_spec: str) -> dict:
    rangees = lire_table_12(texte_spec)
    detail, ecart_max = [], 0.0
    for r in rangees:
        stat = res["resultat"][str(r["budget"])]["contrastes_contre_R2"][libelle_contraste(r["variante"], r["mesure"])]
        e = {"moyenne": abs(stat["moyenne"] - r["moyenne"]), "ecart_type": abs(stat["ecart_type"] - r["ecart_type"])}
        for cle in ("q0.003125", "q0.00625", "q0.99375", "q0.996875"):
            e[cle] = abs(stat["quantiles"][cle] - r[cle])
        m = max(e.values())
        ecart_max = max(ecart_max, m)
        detail.append({"budget": r["budget"], "contraste": libelle_contraste(r["variante"], r["mesure"]),
                       "ecarts": e, "ecart_max_abs": m, "ok": m <= EPS})
    return {"nombre_de_lignes_lues": len(rangees), "lignes": detail, "ecart_maximal_absolu": ecart_max,
            "ok": len(rangees) == 10 and all(d["ok"] for d in detail)}


def _attendus_12(res: dict) -> dict:
    """Confronte classes, contrôles, verdicts et auto-essai de la sortie aux valeurs écrites dans le § 12."""
    cl, sa = res["classes"], res["sante"]
    t = {}
    a = cl["table_A"]
    t["table_A"] = {"obtenu": [a["ligne"], a["classe"]], "attendu": list(ATTENDU_12["table_A"]),
                    "ok": (a["ligne"], a["classe"]) == ATTENDU_12["table_A"]}
    for table, cle_obt in (("table_B", "classe"), ("table_Bprime", "classe"), ("table_C", "ligne")):
        t[table] = {}
        for court, att in ATTENDU_12[table].items():
            obt = tuple(cl[table][court][str(c)][cle_obt] for c in BUDGETS)
            t[table][court] = {"obtenu": list(obt), "attendu": list(att), "ok": obt == att}
    eg = sa["etat_global"]
    ctrl = {
        "T2_non_declenche": not eg["T2"],
        "T3_non_declenche": not eg["T3"],
        "T3_nb_taches": [sa[str(c)]["T3"]["nb_taches_poids_pur"] for c in BUDGETS],
        "T4_non_declenche": not eg["T4"],
        "T4_nb_taches": [sa[str(c)]["T4"]["nb_taches_cos_moyen_ge_0_999"] for c in BUDGETS],
        "T5_non_declenche": not eg["T5"],
        "T5_plus_grand_standard_moins_renforce": max(sa[str(c)]["T5"]["plus_grand_standard_moins_renforce"] for c in BUDGETS),
        "T5_plus_grand_ecart_de_contraste": max(sa[str(c)]["T5"]["plus_grand_abs_ecart_de_contraste"] for c in BUDGETS),
        "T6_non_declenche": not eg["T6"],
        "T6_plus_grand_ecart_a_alpha": max(sa[str(c)]["T6"]["plus_grand_abs_ecart_a_alpha"] for c in BUDGETS),
    }
    ctrl["ok"] = (ctrl["T2_non_declenche"] and ctrl["T3_non_declenche"] and ctrl["T4_non_declenche"]
                  and ctrl["T5_non_declenche"] and ctrl["T6_non_declenche"]
                  and tuple(ctrl["T3_nb_taches"]) == ATTENDU_12["T3_nb_taches_poids_pur"]
                  and tuple(ctrl["T4_nb_taches"]) == ATTENDU_12["T4_nb_taches"]
                  and round(ctrl["T5_plus_grand_standard_moins_renforce"], 5) == ATTENDU_12["T5_plus_grand_standard_moins_renforce_arrondi_5_decimales"]
                  and round(ctrl["T5_plus_grand_ecart_de_contraste"], 5) == ATTENDU_12["T5_plus_grand_ecart_de_contraste_arrondi_5_decimales"]
                  and round(ctrl["T6_plus_grand_ecart_a_alpha"], 5) == ATTENDU_12["T6_plus_grand_ecart_a_alpha_arrondi_5_decimales"])
    t["controles"] = ctrl
    v9 = {k: res["verdicts_regles_originales"][k]["verdict"] for k in ("HR1", "HR0", "HR3", "HR2")}
    t["verdicts_9"] = {"obtenu": v9, "attendu": ATTENDU_12["verdicts_9"], "ok": v9 == ATTENDU_12["verdicts_9"]}
    t["ok"] = (t["table_A"]["ok"] and all(v["ok"] for tb in ("table_B", "table_Bprime", "table_C") for v in t[tb].values())
               and ctrl["ok"] and t["verdicts_9"]["ok"])
    return t


def _cas_a(res: dict) -> dict:
    """§ 12.3 (a) : la course originale contre elle-même, lue dans la sortie."""
    g = [e["g"] for e in res["ecart_de_replication"]["contrastes_primaires"].values()]
    comptes = res["comptes_graines_neuves"]["comptes"]
    tous = [n for par in comptes.values() for n in par.values()]
    return {"g_pi": g, "tous_nuls": all(x == 0 for x in g), "TR2_declenche": res["declencheurs_audit"]["TR2"]["declenche"],
            "nombre_de_comptes": len(tous), "tous_egaux_a_200": all(n == 200 for n in tous),
            "arret_graines_non_neuves": res["comptes_graines_neuves"]["arret_graines_non_neuves"],
            "lecture_autorisee": res["lecture_autorisee"], "code_de_sortie": res["code_de_sortie"],
            "issue_brute": res["issues_globales"]["brute"]["issue"],
            "ok": bool(all(x == 0 for x in g) and res["declencheurs_audit"]["TR2"]["declenche"] and len(tous) == 15
                       and all(n == 200 for n in tous) and res["comptes_graines_neuves"]["arret_graines_non_neuves"]
                       and not res["lecture_autorisee"] and res["code_de_sortie"] == 3)}


def _variante(octets_e1: bytes, transformation) -> dict:
    """E1 de la course originale relu puis transformé en place (chaque variante repart des octets d'origine)."""
    e1 = lire_json_octets(octets_e1, "E1 (variante)")
    for t in e1["resultat"]["resultats"]:
        transformation(t)
    return e1


def _decaler_b(t: dict, extra_r3: float = 0.0):
    """§ 12.3 (b) : V, V standard, V renforcé, X̄ et (ii) augmentés de 1e-6 ; les trois champs de V de R3 augmentés en
    plus de `extra_r3`."""
    for nom, v in t["regles"].items():
        for ch in ("V_iii_final", "V_iii_standard", "V_iii_renforce", "exploitabilite_moyenne_tours", "ii_final"):
            v[ch] = v[ch] + 1e-6
        if nom == "R3":
            for ch in ("V_iii_final", "V_iii_standard", "V_iii_renforce"):
                v[ch] = v[ch] + extra_r3


def _decaler_r3(t: dict, delta: float, borne_zero: bool = False):
    for ch in ("V_iii_final", "V_iii_standard", "V_iii_renforce"):
        x = t["regles"]["R3"][ch] + delta
        t["regles"]["R3"][ch] = max(x, 0.0) if borne_zero else x


def cas_synthetiques_12_3(octets_e1: bytes, e4_analyse: dict, e4_resultats: dict) -> dict:
    """§ 12.3 (b) à (e), en mémoire (racine de la course originale imposée)."""
    def lancer(e1):
        s = calculer_B(e1, RACINE_COURSE_ORIGINALE, RACINE_TENUE_COURSE_ORIGINALE, e4_analyse, e4_resultats)
        s["comparaison_A_B"] = {"evaluee": False}
        return conclure(s)

    out = {}
    # (b) cas sain
    s = lancer(_variante(octets_e1, lambda t: _decaler_b(t, 0.01)))
    comptes = [n for par in s["comptes_graines_neuves"]["comptes"].values() for n in par.values()]
    out["b_cas_sain"] = {"comptes_max": max(comptes), "TR1": s["declencheurs_audit"]["TR1"]["declenche"],
                         "TR2": s["declencheurs_audit"]["TR2"]["declenche"], "arret": bool(s["motifs_arret"]),
                         "code_de_sortie": s["code_de_sortie"], "lecture_autorisee": s["lecture_autorisee"],
                         "ok": bool(max(comptes) == 0 and not s["declencheurs_audit"]["TR1"]["declenche"]
                                    and not s["declencheurs_audit"]["TR2"]["declenche"] and not s["motifs_arret"]
                                    and s["code_de_sortie"] == 0)}
    # (c) R3 décalé de +0,06
    s = lancer(_variante(octets_e1, lambda t: (_decaler_b(t, 0.0), _decaler_r3(t, 0.06))))
    z = {k: v["z"] for k, v in s["ecart_de_replication"]["contrastes_primaires"].items()}
    out["c_R3_plus_0_06"] = {"TR1": s["declencheurs_audit"]["TR1"]["declenche"], "z_R3": {k: v for k, v in z.items() if "R3" in k},
                             "ok": bool(s["declencheurs_audit"]["TR1"]["declenche"]
                                        and all(v > 0 for k, v in z.items() if "R3" in k))}
    # (d) R3 décalé de −0,03, borné à 0
    s = lancer(_variante(octets_e1, lambda t: (_decaler_b(t, 0.0), _decaler_r3(t, -0.03, True))))
    z = {k: v["z"] for k, v in s["ecart_de_replication"]["contrastes_primaires"].items()}
    out["d_R3_moins_0_03"] = {"TR1": s["declencheurs_audit"]["TR1"]["declenche"], "z_R3": {k: v for k, v in z.items() if "R3" in k},
                              "ok": bool(s["declencheurs_audit"]["TR1"]["declenche"]
                                         and all(v < 0 for k, v in z.items() if "R3" in k))}
    # (e) une seule variante dont k tâches gardent leur valeur originale exacte de V
    originale = lire_json_octets(octets_e1, "E1 (originale)")["resultat"]["resultats"]
    for k, attendu_arret in ((3, True), (2, False)):
        e1 = _variante(octets_e1, lambda t: _decaler_b(t, 0.01))
        compte = 0
        for i, t in enumerate(e1["resultat"]["resultats"]):
            if t["code_delta"] == 1 and t["instance"] < k:
                for ch in ("V_iii_final", "V_iii_standard", "V_iii_renforce"):
                    t["regles"]["R1"][ch] = originale[i]["regles"]["R1"][ch]
                compte += 1
        s = lancer(e1)
        out[f"e_{k}_taches_gardees"] = {
            "taches_gardees": compte, "compte_R1_V": s["comptes_graines_neuves"]["comptes"]["R1"]["V_iii_final"],
            "arret_graines_non_neuves": s["comptes_graines_neuves"]["arret_graines_non_neuves"],
            "code_de_sortie": s["code_de_sortie"],
            "ok": bool(s["comptes_graines_neuves"]["arret_graines_non_neuves"] == attendu_arret
                       and s["code_de_sortie"] == (3 if attendu_arret else 0))}
    out["ok"] = all(v["ok"] for v in out.values())
    return out


def _recoupements_hors_specification(res: dict, analyse_a: dict, e1: dict) -> dict:
    """Recoupements avec des champs de l'analyse de la course qui ne font pas partie du contrat de la spécification
    (sections `variantes` et contrastes « V standard seul / renforce seul »). Informatif : une absence ou une
    différence est consignée telle quelle."""
    par_budget = selectionner_taches(valider_forme_E1(e1))
    sortie, ecart_max, nb_comparaisons = {}, 0.0, 0
    for c in BUDGETS:
        d = extraire_donnees(par_budget[c], c)
        ch = d["champs"]
        var_a = analyse_a["resultat"][str(c)].get("variantes", {})
        lignes = {}
        for nom in NOMS_VARIANTES:
            va = var_a.get(nom)
            if va is None:
                lignes[NOM_COURT[nom]] = "absent de l'analyse de référence"
                continue
            comp = {}
            paires = {
                "V_iii_final (moyenne)": (va.get("V_iii_final"), float(np.mean(ch[nom]["V_iii_final"]))),
                "ii_final (moyenne)": (va.get("ii_final"), float(np.mean(ch[nom]["ii_final"]))),
                "exploitabilite_finale (moyenne)": (va.get("exploitabilite_finale"), float(np.mean(ch[nom]["exploitabilite_finale"]))),
                "exploitabilite_moyenne_tours (moyenne)": (va.get("exploitabilite_moyenne_tours"), float(np.mean(ch[nom]["exploitabilite_moyenne_tours"]))),
                "fpr (moyenne)": (va.get("fpr_moyen"), float(np.mean(ch[nom]["fpr_final"]))),
                "standard - renforce (moyenne)": (va.get("standard_moins_renforce"),
                                                 float(np.mean(ch[nom]["V_iii_standard"])) - float(np.mean(ch[nom]["V_iii_renforce"]))),
            }
            for lib, (x_a, x_b) in paires.items():
                if isinstance(x_a, (int, float)):
                    comp[lib] = abs(float(x_a) - x_b)
                    ecart_max = max(ecart_max, comp[lib])
                    nb_comparaisons += 1
                else:
                    comp[lib] = None
            lignes[NOM_COURT[nom]] = comp
        cos_a = var_a.get(NOM_R4, {}).get("cos_consecutif_par_tache")
        if isinstance(cos_a, list) and len(cos_a) == N:
            mes = [sum(v) / 8 for v in d["cos_R4"]]
            e = max(abs(x - y) for x, y in zip(cos_a, mes))
            lignes["R4 cos moyen par tâche (cos_consecutif_par_tache)"] = e
            ecart_max = max(ecart_max, e)
            nb_comparaisons += 1
        pur = var_a.get("R3", {}).get("poids", {}).get("part_pure")
        if isinstance(pur, (int, float)):
            lignes["R3 part de tâches à poids pur (poids.part_pure)"] = abs(float(pur) - res["sante"][str(c)]["T3"]["nb_taches_poids_pur"] / N)
            nb_comparaisons += 1
        contr_a = analyse_a["resultat"][str(c)]["contrastes_contre_R2"]
        for nom in VARIANTES_CONTRASTEES:
            ent = contr_a.get(f"{nom} - R2 (V standard seul / renforce seul)")
            if ent is None:
                continue
            ec = res["sante"][str(c)]["T5"]["ecart_de_contraste"][NOM_COURT[nom]]
            e = max(abs(ent["moyenne_standard"] - ec["a_standard"]), abs(ent["moyenne_renforce"] - ec["b_renforce"]),
                    abs(ent["ecart"] - ec["a_moins_b"]))
            lignes[f"{NOM_COURT[nom]} contraste standard seul / renforcé seul (T5, a, b, a−b)"] = e
            ecart_max = max(ecart_max, e)
            nb_comparaisons += 1
        sortie[str(c)] = lignes
    return {"nature": "hors contrat de la spécification ; informatif", "nombre_de_comparaisons": nb_comparaisons,
            "ecart_maximal_absolu": ecart_max, "par_budget": sortie}


def _plus_petites_marges(res: dict, combien: int = 6) -> list:
    cl = res["classes"]
    lignes = [("table_A", cl["table_A"]["marge_min_au_seuil"])]
    for table in ("table_B", "table_Bprime", "table_C"):
        for court, par_c in cl[table].items():
            for c, d in par_c.items():
                lignes.append((f"{table}/{court}/budget {c}", d["marge_min_au_seuil"]))
    lignes.sort(key=lambda x: x[1])
    return [{"classe": nom, "marge_min_au_seuil": m} for nom, m in lignes[:combien]]


# --- contenu statique du rapport (X3) ------------------------------------------------------------------------
POINTS_V2 = (
    (1, "Contrôles T2, T3, T5, T6 : par budget ou globalement", "déjà ainsi en v1",
     "états par budget, déclenché si au moins un budget ; v2 écrit en plus la marque de frontière globale"),
    (2, "Ligne 2 de « HR1 répliquée ? » inatteignable", "déjà ainsi en v1 pour la ligne ; changé en v2 pour la garde",
     "ligne gardée mot pour mot ; v2 ajoute une alarme interne (code 2) si la ligne était atteinte par le chemin complet, et des essais"),
    (3, "Deux issues globales (brute / après déclencheurs)", "déjà ainsi en v1",
     "v2 ajoute la mention « V0 : non évaluée par B », « sous réserve de V0 » et la marque de frontière des issues"),
    (4, "Frontière numérique : quelles comparaisons comptent", "changé en v2 (partiellement déjà ainsi)",
     "v1 : tables et contrôles T2/T5/T6 sans court-circuit, mais T4 (cos_moyen) non marqué, déclencheurs non marqués (TR1 en `any` à court-circuit), "
     "verdicts sans héritage des contrôles ni des déclencheurs ; v2 : tout cela est marqué et hérité sur le chemin de décision"),
    (5, "Champs de E2 non vérifiés", "changé en v2", "liste fermée de vérifications, chacune un arrêt (v1 : avertissements)"),
    (6, "Nom du fichier compagnon", "changé en v2",
     "v1 acceptait aussi `<fichier sans extension>.sha256` et ne faisait qu'avertir sur un nom de base différent ; v2 : `<fichier>.sha256` seul, "
     "une ligne exacte, empreinte et nom de base vérifiés (arrêt)"),
    (7, "Résultats originaux sans compagnon", "déjà ainsi en v1",
     "empreinte épinglée ; v2 précise : compagnon vérifié s'il existe, sinon empreinte épinglée, sinon arrêt ; variantes : `--empreinte-e1`"),
    (8, "V0 et discordance A/B", "changé en v2",
     "v1 : options `--plomberie-fausse` et `--discordance-ab` ; v2 : plus d'option de discordance, elle est calculée depuis E5 ; V0 non évaluée par B"),
    (9, "Forme de E1 : « contient »", "changé en v2",
     "v1 lisait « au moins » pour `resultat` mais exigeait exactement trois clés au premier niveau ; v2 : clés supplémentaires permises partout sauf dans `regles`"),
    (10, "Arrêt sans sortie et auto-essai du § 12 : codes de sortie", "changé en v2",
     "v1 : codes 0, 2, 3, 4 et discordance A/B hors du chemin d'analyse ; v2 : codes 0, 2, 3 seulement (sortie déjà existante = 2) et discordance A/B → 3"),
    (11, "T5 : première condition unilatérale, seconde bilatérale", "déjà ainsi en v1",
     "v2 rend les deux conditions explicites dans la sortie (`a_unilaterale_declenche`, `b_bilaterale_declenche`)"),
    (12, "« À 1e-12 près » pour [0 ; 1]", "déjà ainsi en v1", "v2 écrit les bornes explicitement (−1e-12 ; float('1.000000000001')), égales à 1.0 + 1e-12"),
    (13, "Champs documentés non utilisés", "changé en v2",
     "gardes neuves : `delta` (v1 : avertissement), `config_sha256` identique et épinglé, `lam` et `reference` ; `par_tour.exploitabilite` jamais exigé"),
    (14, "L'analyse de A ne contient pas ses contrôles de santé", "déjà ainsi en v1",
     "B ne lit pas les états de A ; classes, verdicts et déclencheurs « de A » sont calculés avec les contrôles recalculés depuis E1"),
    (15, "Seuil de T3", "déjà ainsi en v1 (même valeur)", "v2 : constante hexadécimale `0x1.fffffff768fa1p-1` ; égale à 1.0 - 1e-9 et à float('0.999999999')"),
    ("CL-10", "« Graines neuves » : seuil et mesures", "changé en v2",
     "v1 : plus de 10 tâches, V seule, par variante ; v2 : plus de 2 tâches, V, X̄ et (ii), quinze comptes"),
    ("—", "Environnement", "changé en v2", "interpréteur du dépôt, numpy 2.4.6 (validation et emploi)"),
)

CORRESPONDANCE_CLES = (
    ("Verdict d'ensemble : lecture autorisée ; motifs d'arrêt (§ 11.1)", "`lecture_autorisee`, `motifs_arret`, `code_de_sortie`"),
    ("Empreinte H ; racines ρ, ρ_t en chaînes décimales", "`H`, `racines.rho`, `racines.rho_t`, `racine_de_reechantillonnage`"),
    ("Contrastes de chaque budget, indexés par libellé (§ 5.7)", "`resultat.\"1\"|\"2\".contrastes_contre_R2.<libellé>.{moyenne, ecart_type, n, quantiles, zeros_exacts}`"),
    ("Intervalles B2, B8, E8", "`intervalles.\"1\"|\"2\".<libellé>.{B2, B8, E8}`"),
    ("Classes des Tables A, B, B′, C avec leurs marques de frontière", "`classes.table_A`, `classes.table_B.<R0|R1|R3|R4>.\"1\"|\"2\"`, `classes.table_Bprime…`, `classes.table_C…` (clés `ligne`, `classe`, `frontiere`, `frontiere_propre`, `heritee_de`, `marge_min_au_seuil`, `comparaisons_a_la_frontiere`) ; liste : `classes_a_la_frontiere`"),
    ("Contrôles T2 à T6 : valeurs comparées et état, par budget", "`sante.\"1\"|\"2\".<T2…T6>.{declenche, frontiere, …valeurs}` ; moyennes de V : `sante.\"c\".moyennes_V`"),
    ("Contrôles : état global (au moins un budget) et marque globale", "`sante.etat_global.<T2…T6>`, `sante.frontiere_globale.<T2…T6>`"),
    ("Verdicts du § 9 (course originale)", "`verdicts_regles_originales.{HR1, HR0, HR3, HR2}.verdict`"),
    ("Verdicts bruts du § 10.1", "`verdicts_bruts_replication.{HR1, HR0, HR3, lois_tenues_ii, HR2}.{ligne, verdict, frontiere}` ; classes κ : `kappa_R0_V`, `kappa_prime_R4_V`, `lignes_C_R0_ii`"),
    ("g_π, σ_π, z_π", "`ecart_de_replication.contrastes_primaires.\"(R3, V, c=1)\"….{g, sigma, z, est_rep, s_rep, est_or, s_or}`"),
    ("État de TR1 à TR4 (avec marques) et « au moins un »", "`declencheurs_audit.{TR1, TR2, TR3, TR4, au_moins_un}.{declenche, frontiere}`"),
    ("Verdicts après l'effet du § 10.2", "`verdicts_apres_declencheurs.{HR1, HR0, HR3, lois_tenues_ii}.{verdict, frontiere}`"),
    ("Les quinze comptes « graines neuves » (§ 10.3)", "`comptes_graines_neuves.comptes.<R0|R1|R2|R3|R4>.<V_iii_final|exploitabilite_moyenne_tours|ii_final>` ; `comptes_graines_neuves.arret_graines_non_neuves`"),
    ("Deux issues globales (§ 10.4) et mention de V0", "`issues_globales.brute`, `issues_globales.apres_declencheurs` (clés `ligne`, `issue`, `frontiere`, `V0`, `sous_reserve_de_V0`) ; `issues_globales.V0` = « V0 : non évaluée par B »"),
    ("Résultat de la comparaison A/B (§ 11.2)", "`comparaison_A_B.{evaluee, discordance_a_arret, motifs, alertes_de_discordance, detail_par_contraste, z_pi, classes, verdicts_et_declencheurs, concordance}`"),
    ("Empreintes de tous les fichiers lus", "`empreintes_fichiers[].{role, fichier, sha256}` ; ordre des lectures : `ordre_des_lectures`"),
    ("Versions (Python, numpy)", "`meta_non_deterministe.versions.{python, numpy, implementation}`"),
    ("Valeur de toute option de ligne de commande employée", "`options.{mode, plomberie_fausse_V0, empreinte_E1_imposee_en_ligne_de_commande}`"),
    ("Valeurs lues dans E2 (réplication)", "`manifeste_E2.{run_id, lambda, reference, n_instances, config_sha256, prereg_sha256}`"),
)

COMMANDE_COURSE = (
    "/home/claude/controle-ia-travail/.venv/bin/python \\\n"
    "  /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/implementation_b_v2.py replication \\\n"
    "  --resultats <RACINE_DEPOT>/diag/<run>/resultats-regles-defense.json \\\n"
    "  --manifeste <RACINE_DEPOT>/runs/<run>/manifeste.json \\\n"
    "  --prereg <RACINE_DEPOT>/prereg/preregistrement-replication-regles-defense-convergence-v1.md \\\n"
    "  --analyse-A <RACINE_DEPOT>/diag/<run>/analyse-regles-defense.json \\\n"
    "  --analyse-originale /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/analyse-regles-defense.json \\\n"
    "  --resultats-originaux /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/resultats-regles-defense.json \\\n"
    "  --sortie /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/sortie-b-replication-v2.json"
)

AMBIGUITES_RESTANTES = (
    "Présence de `temps` dans `resultat` : le § 3 écrit « `resultat` contient `temps` et `resultats` », le tableau « Emploi de chaque champ » "
    "écrit « `temps` … présence non exigée ». Lecture prudente retenue (celle qui arrête) : `temps` est exigé.",
    "Contenu admis d'un compagnon : le § 3 dit « une seule ligne non vide » puis « une fin de ligne ». Lecture prudente : le fichier est "
    "exactement `<64 hexadécimaux minuscules>␣␣<nom de base>\\n` (ni ligne vide en plus, ni retour chariot, ni dossier dans le nom).",
    "Marques de frontière héritées : « toute classe, tout contrôle, tout déclencheur qui y entre » est lu comme « examiné sur le chemin de "
    "décision du verdict (lignes examinées jusqu'à la première vraie comprise) » ; lecture prudente puisqu'une marque ne fait que tolérer une "
    "divergence (donc plus étroite = plus d'arrêts). Pour HR3 original et réplication, T4 entre quand la ligne qui le teste est examinée.",
    "Comparaison A/B des contrastes de concordance exigée : n et zéros exacts identiques sont exigés EN PLUS des douze écarts à ε près "
    "(lecture prudente ; le § 11.2 ne cite que la moyenne, l'écart-type et les dix quantiles).",
    "« Égale au bit » du § 10.3 : lu comme égalité des 64 bits (0.0 et −0.0 seraient distincts ; le § 10.3 écrit aussi « égalité de binaires64 »).",
    "« Arrêt » de la ligne 1 du § 10.4 : lu comme tout arrêt de contrôle de B (graines non neuves, discordance A/B de niveau arrêt) ; "
    "les alertes (11 autres contrastes) n'y entrent pas.",
    "Le § 11.2 compare « verdicts bruts » ; B compare aussi les verdicts du § 9, les verdicts après déclencheurs et HR2 recopié (plus strict).",
    "Si E1 d'un essai porte des racines ≠ (20266201, 20266202), c'est un arrêt d'entrée ; en réplication, E1 doit porter (ρ, ρ_t) de la règle D.",
    "E5 : les champs `run_id` et `manifeste_sha256` du premier niveau de l'analyse sont exigés ; en mode essai (pas de E2) `manifeste_sha256` est "
    "comparé à celui de E1.",
    "Une marque de frontière sur un élément ne fait que tolérer une différence A/B ; la valeur « retenue » est celle de A, mais B ne "
    "remplace pas ses propres classes : il écrit les deux.",
    "T3 : la comparaison du plus grand poids à 0x1.fffffff768fa1p-1 porte sur une valeur brute de E1 (exclue de la marque, § 8) ; B écrit "
    "seulement à titre d'information le nombre de tâches à moins de ε de ce seuil, sans marque.",
    "Contrastes de concordance exigée : « z_π(A) − z_π(B) ≤ 1e-9 » est appliqué aux quatre contrastes primaires, ce qui est plus étroit que "
    "la tolérance sur la moyenne (un écart de 5e-10 sur la moyenne d'un contraste primaire déplace z_π de plus de 1e-9 : arrêt).",
    "Mode `essai` (pièces de la course originale ou de ses variantes) : sous-commande de B hors du contrat du § 3, utilisée pour le § 12 ; "
    "elle impose les racines de la course originale et ne peut pas servir pour la réplication (E3 et E2 y sont refusés).",
)

LIMITES_VALIDATION = (
    "Le mode `replication` de bout en bout (règle D sur un texte scellé, E2, E3, E5, compagnons) n'est essayé que sur des pièces "
    "synthétiques construites à partir de la course originale ; aucune donnée de la réplication n'existe encore.",
    "Les sorties des essais (b) à (e) sont obtenues sans E5 (A n'a pas calculé ces variantes) : la discordance A/B n'y est pas évaluée "
    "(elle l'est sur la course originale contre sa propre analyse, et sur des analyses synthétiques altérées dans les essais).",
    "Les contrôles de santé de A ne sont pas dans l'analyse de la course : leur confrontation est limitée aux champs voisins "
    "(recoupements hors contrat) et au texte du § 12.1.",
    "La campagne de mutations est un contrôle de la suite d'essais, pas une preuve de justesse ; son code vit hors du dossier livré.",
)

FICHIERS_OUVERTS = (
    "/home/claude/controle-ia-travail/CLAUDE.md (consignes permanentes du dépôt, fournies par l'outil dans le contexte de la session ; non ouvert par une commande)",
    "/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/consigne-implementation-b-v2.md (lu)",
    "/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/specification-statistique-decisive-v2.md (lu en entier ; empreinte vérifiée)",
    "/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/specification-statistique-decisive-v1.md (v1, lu lors du travail précédent)",
    "/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/resultats-regles-defense.json (lu ; empreinte vérifiée)",
    "/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/analyse-regles-defense.json (lu ; empreinte vérifiée)",
    "/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/implementation_b.py (v1, lu, non modifié)",
    "/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/test_implementation_b.py (v1, lu, non modifié)",
    "/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/validation-b-v1.md, validation-b-v1.json, sortie-b-originale-v1.json (v1, lus, non modifiés)",
    "/home/claude/controle-ia-travail/.venv/bin/python (exécution) ; pytest 9.1.1 et numpy 2.4.6 de ce même environnement (importés par l'exécution)",
    "/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/mut/mutations.py (mon script de mutations de la v1, lu pour l'adapter)",
    "/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/v2/ (mes brouillons : part1-3.py, tpart1-4.py, mutations2.py, run/, mutw/ ; supprimés à la fin)",
    "Listage (ls) des dossiers …/convergence-replication-v1/, …/implementation-b/ et du dossier temporaire de la session (noms seulement ; aucun fichier étranger à ce travail n'a été ouvert)",
    "/tmp/pytest-of-root/ et dossiers temporaires créés par les essais et la campagne de mutations (écrits par les essais eux-mêmes, supprimés à la fin)",
)

MODELE = "Claude Sonnet 5.5 (identifiant claude-sonnet-5-5), famille Claude, d'Anthropic"


def executer_suite_d_essais(dossier: Path) -> dict:
    """Lance la suite d'essais avec l'interpréteur courant et consigne les comptes (par catégorie de préfixe)."""
    t0 = time.perf_counter()
    with tempfile.TemporaryDirectory() as tmp:
        xml = Path(tmp) / "junit.xml"
        p = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", f"--junitxml={xml}",
                            str(Path(dossier) / NOM_TESTS)], cwd=str(dossier), capture_output=True, text=True,
                           env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})
        if not xml.exists():
            return {"lances": False, "stderr": p.stderr[-2000:], "stdout": p.stdout[-2000:]}
        racine = ET.parse(xml).getroot()
        suite = racine if racine.tag == "testsuite" else racine.find("testsuite")
        cas = list(suite.iter("testcase"))
        par_cat: dict = {}
        for tc in cas:
            m = re.match(r"test_(c\d+_\d+|mut|[a-z]+)_", tc.get("name"))
            cat = m.group(1) if m else "autres"
            d = par_cat.setdefault(cat, {"essais": 0, "echecs": 0})
            d["essais"] += 1
            if tc.find("failure") is not None or tc.find("error") is not None:
                d["echecs"] += 1
        return {"lances": True, "essais": int(suite.get("tests")), "echecs": int(suite.get("failures")),
                "erreurs": int(suite.get("errors")), "ignores": int(suite.get("skipped")),
                "duree_pytest_s": float(suite.get("time")), "duree_mur_s": round(time.perf_counter() - t0, 1),
                "par_categorie": par_cat, "code_retour_pytest": p.returncode}


def valider_originale(dossier, dossier_sortie, *, executer_essais: bool = False, mutations: str | None = None) -> dict:
    """Validation du § 12. Écrit la sortie sur la course originale (sortie-b-originale-v2.json) et rend le rapport
    (dictionnaire) ; l'appelant écrit validation-b-v2.json et validation-b-v2.md."""
    t0 = time.perf_counter()
    dossier, dossier_sortie = Path(dossier), Path(dossier_sortie)
    entrees = dossier / "entrees"
    p_spec = entrees / "specification-statistique-decisive-v2.md"
    p_res = entrees / "resultats-regles-defense.json"
    p_ana = entrees / "analyse-regles-defense.json"

    octets_spec = p_spec.read_bytes()
    sha_spec = empreinte_octets(octets_spec)
    rapport = {"version_validation": "validation-b-v2", "implementation": f"{NOM_FICHIER_IMPLEMENTATION} ({VERSION_IMPLEMENTATION})",
               "python": platform.python_version(), "numpy": np.__version__, "interpreteur": sys.executable,
               "modele": MODELE}
    rapport["entrees"] = {
        "specification_v2": {"fichier": p_spec.name, "sha256": sha_spec, "attendu": EMPREINTE_SPECIFICATION_V2,
                             "conforme": sha_spec == EMPREINTE_SPECIFICATION_V2},
        "resultats_originaux": {"fichier": p_res.name, "sha256": empreinte_octets(p_res.read_bytes()),
                                "attendu": EMPREINTE_RESULTATS_ORIGINAUX},
        "analyse_de_reference_A": {"fichier": p_ana.name, "sha256": empreinte_octets(p_ana.read_bytes()),
                                   "attendu": EMPREINTE_ANALYSE_ORIGINALE}}
    for k in ("resultats_originaux", "analyse_de_reference_A"):
        rapport["entrees"][k]["conforme"] = rapport["entrees"][k]["sha256"] == rapport["entrees"][k]["attendu"]

    rapport["vecteurs_regle_D"] = _vecteurs_regle_d()
    rapport["vecteurs_generateur"] = _vecteurs_generateur()
    rapport["entiers_64_bits"] = _entiers_64_bits()
    rapport["constantes"] = {
        "s_pur_hex": S_PUR.hex(), "s_pur_egal_1_moins_1e_9": S_PUR == 1.0 - 1e-9,
        "s_pur_egal_float_0_999999999": S_PUR == float("0.999999999"),
        "borne_haute_egale_1_plus_1e_12": BORNE_01_HAUT == 1.0 + 1e-12, "G": G_GRAINES}

    # 12.1 + 12.3 (a) : la course originale contre elle-même, avec E5 = analyse de la course originale
    t1 = time.perf_counter()
    res = analyser_fichiers(mode="essai", resultats=p_res, analyse_originale=p_ana, resultats_originaux=p_res, analyse_A=p_ana)
    duree_analyse = time.perf_counter() - t1
    chemin_b = dossier_sortie / NOM_SORTIE_B
    sha_b = ecrire_json_neuf(chemin_b, res)
    rapport["sortie_de_B"] = {"fichier": chemin_b.name, "sha256": sha_b, "racine": res["racine_de_reechantillonnage"],
                              "lecture_autorisee": res["lecture_autorisee"], "code_de_sortie": res["code_de_sortie"],
                              "motifs_arret": res["motifs_arret"], "duree_analyse_s": round(duree_analyse, 3)}
    analyse_a = lire_json_octets(p_ana.read_bytes(), "A")
    e1 = lire_json_octets(p_res.read_bytes(), "E1")
    comparaison = res["comparaison_A_B"]
    rapport["comparaison_A_B"] = comparaison
    rapport["table_de_controle_12"] = _table_12(res, octets_spec.decode("utf-8"))
    rapport["attendus_12"] = _attendus_12(res)
    rapport["cas_a_original_contre_lui_meme"] = _cas_a(res)
    rapport["plus_petites_marges_aux_seuils"] = _plus_petites_marges(res)
    rapport["classes_a_la_frontiere"] = res["classes_a_la_frontiere"]
    rapport["recoupements_hors_specification"] = _recoupements_hors_specification(res, analyse_a, e1)

    # 12.3 (b) à (e)
    t2 = time.perf_counter()
    rapport["cas_12_3_b_a_e"] = cas_synthetiques_12_3(p_res.read_bytes(), analyse_a, e1)
    rapport["cas_12_3_b_a_e"]["duree_s"] = round(time.perf_counter() - t2, 1)

    if executer_essais:
        rapport["essais"] = executer_suite_d_essais(dossier)
    else:
        rapport["essais"] = {"lances": False, "raison": "option --executer-essais non demandée"}
    rapport["mutations"] = {"consigne": mutations} if mutations else {"consigne": "non fournie"}

    rapport["points_de_la_specification_0"] = [{"point": p, "intitule": i, "statut": s, "detail": d} for p, i, s, d in POINTS_V2]
    rapport["table_de_correspondance_des_cles"] = [{"element": a, "cle_json": b} for a, b in CORRESPONDANCE_CLES]
    rapport["commande_pour_la_course"] = COMMANDE_COURSE
    rapport["ambiguites_restantes"] = list(AMBIGUITES_RESTANTES)
    rapport["ce_que_la_validation_ne_couvre_pas"] = list(LIMITES_VALIDATION)
    rapport["fichiers_ouverts"] = list(FICHIERS_OUVERTS)

    cond = {
        "entrees_conformes": all(v.get("conforme", False) for v in rapport["entrees"].values()),
        "vecteurs_regle_D": rapport["vecteurs_regle_D"]["ok"],
        "vecteurs_generateur": rapport["vecteurs_generateur"]["ok"],
        "entiers_64_bits": rapport["entiers_64_bits"]["ok"],
        "statistiques_16x2_a_1e-9": (not comparaison["discordance_a_arret"]) and not comparaison["alertes_de_discordance"]
                                    and comparaison["ecart_maximal_absolu"] <= EPS,
        "table_de_controle_12": rapport["table_de_controle_12"]["ok"],
        "classes_identiques_A_B": comparaison["classes"]["identiques"],
        "verdicts_et_declencheurs_identiques_A_B": comparaison["verdicts_et_declencheurs"]["identiques"],
        "z_pi_concordants": comparaison["z_pi"]["ok"],
        "classes_controles_verdicts_conformes_au_12": rapport["attendus_12"]["ok"],
        "cas_a_artefact": rapport["cas_a_original_contre_lui_meme"]["ok"],
        "cas_b_a_e": rapport["cas_12_3_b_a_e"]["ok"],
    }
    if executer_essais:
        e = rapport["essais"]
        cond["suite_d_essais"] = bool(e.get("lances") and e.get("echecs") == 0 and e.get("erreurs") == 0)
    cond["validation_reussie"] = all(cond.values())
    rapport["conclusion"] = cond
    rapport["duree_totale_s"] = round(time.perf_counter() - t0, 1)
    return rapport


def _e(x) -> str:
    return "0" if x == 0 else f"{x:.2e}"


def rapport_markdown(r: dict) -> str:
    """Rendu lisible du rapport de validation (le fichier JSON fait foi)."""
    c, cmp_ = r["conclusion"], r["comparaison_A_B"]
    ok = "RÉUSSIE" if c["validation_reussie"] else "ÉCHEC"
    L = []
    L.append("# Validation de l'implémentation B, version 2 — v2\n")
    if c["validation_reussie"]:
        L.append(f"**Verdict : validation {ok}.** Sur la course originale (racine 20266201), écart absolu maximal entre ma sortie et l'analyse de "
                 f"référence : **{_e(cmp_['ecart_maximal_absolu'])}** sur 32 contrastes (16 par budget ; moyenne, écart-type, dix quantiles ; exigence ≤ 1e-9). "
                 f"Classes, verdicts et déclencheurs : **identiques** à ceux calculés sur les nombres de la référence et conformes au § 12.1 de la spécification v2. "
                 f"Les cas du § 12.3 (artefact, cas sain, décalages, seuil de trois tâches) rendent ce qu'attend la spécification.\n")
    else:
        L.append(f"**Verdict : validation {ok}.** Voir les conditions non remplies ci-dessous.\n")
    L.append(f"Implémentation : `{r['implementation']}` · modèle : {r['modele']} · interpréteur `{r['interpreteur']}` · "
             f"Python {r['python']} · numpy {r['numpy']} · analyse complète en {r['sortie_de_B']['duree_analyse_s']} s · "
             f"validation complète en {r['duree_totale_s']} s.\n")
    L.append("## Conditions de réussite\n")
    L.append("| Condition | Résultat |\n|---|---|")
    libs = {
        "entrees_conformes": "Empreintes des trois entrées conformes (spécification v2, résultats et analyse de la course originale)",
        "vecteurs_regle_D": "Règle D : trois vecteurs d'essai, gardes sur les six entiers, cas sain",
        "vecteurs_generateur": "Générateur : indices des deux vecteurs d'essai du § 5.5",
        "entiers_64_bits": "Entiers de plus de 2^63 : lecture, comparaison et écriture exactes",
        "statistiques_16x2_a_1e-9": "Statistiques des 16 contrastes × 2 budgets à 1e-9 près",
        "table_de_controle_12": "Tableau de contrôle du § 12.1 (10 lignes lues dans la spécification v2)",
        "classes_identiques_A_B": "Classes (tables A, B, B′, C) identiques entre ma sortie et les nombres de la référence",
        "verdicts_et_declencheurs_identiques_A_B": "Verdicts (§ 9, § 10.1, après déclencheurs) et déclencheurs TR1 à TR4 identiques",
        "z_pi_concordants": "Écarts réduits z des quatre contrastes primaires concordants à 1e-9",
        "classes_controles_verdicts_conformes_au_12": "Classes, contrôles et verdicts du § 9 conformes au texte du § 12.1",
        "cas_a_artefact": "§ 12.3 (a) : original contre lui-même → écart nul, TR2, quinze comptes à 200, arrêt, code 3",
        "cas_b_a_e": "§ 12.3 (b) à (e) : cas sain, R3 +0,06, R3 −0,03, trois tâches / deux tâches",
        "suite_d_essais": "Suite d'essais (pytest) sans échec ni erreur",
    }
    for k, lib in libs.items():
        if k in c:
            L.append(f"| {lib} | {'oui' if c[k] else '**NON**'} |")
    L.append("")
    L.append("## Entrées (empreintes SHA-256)\n")
    for k, v in r["entrees"].items():
        L.append(f"- {k} : `{v['fichier']}` — `{v['sha256']}` (conforme à l'empreinte épinglée : {v['conforme']})")
    L.append(f"- Sortie de B sur la course originale : `{r['sortie_de_B']['fichier']}` — `{r['sortie_de_B']['sha256']}` "
             f"(racine {r['sortie_de_B']['racine']} ; code de sortie {r['sortie_de_B']['code_de_sortie']} ; lecture autorisée : "
             f"{r['sortie_de_B']['lecture_autorisee']} — attendu : l'original contre lui-même est l'artefact du § 12.3 (a))\n")
    L.append("## Le § 0 de la spécification v2, point par point\n")
    L.append("| # | Point | Dans B v1, puis dans B v2 | Détail |\n|---|---|---|---|")
    for p in r["points_de_la_specification_0"]:
        L.append(f"| {p['point']} | {p['intitule']} | {p['statut']} | {p['detail']} |")
    L.append("")
    L.append("## Vecteurs d'essai\n")
    L.append("Règle D (§ 4) — H, ρ calculé, résultat :\n")
    for v in r["vecteurs_regle_D"]["vecteurs"]:
        L.append(f"- `{v['H'][:8]}…` : ρ = {v['rho']} ; ρ_t = {v['rho_t']} → {'identiques aux attendus' if v['ok'] else '**DIFFÉRENTS**'} ; "
                 f"les gardes rejettent ce vecteur (interdit comme racine) : {v['gardes_rejettent_ce_vecteur']}")
    cs = r["vecteurs_regle_D"]["cas_sain"]
    L.append(f"- Cas sain : la règle D appliquée à l'empreinte du préenregistrement original rend ({cs['rho']}, {cs['rho_t']}), "
             f"différent de (20266201, 20266202) : {cs['differe_de_20266201_20266202']}.\n")
    L.append("Générateur (§ 5.5), racine 20266201 :\n")
    for v in r["vecteurs_generateur"]["vecteurs"]:
        L.append(f"- clé {tuple(v['cle'])} : forme {tuple(v['forme'])}, {v['dtype']} ; ligne 0, dix premiers = {v['ligne0_dix_premiers']} ; "
                 f"dernière ligne, cinq derniers = {v['derniere_ligne_cinq_derniers']} → {'conformes' if v['ok'] else '**DIFFÉRENTS**'}")
    e64 = r["entiers_64_bits"]
    L.append(f"\nEntiers de 64 bits (§ 12.4) : {e64['entier_essai']} lu exactement : {e64['lu_exactement']} ; son voisin est distinct comme entier "
             f"({e64['voisins_distincts_comme_entiers']}) mais serait confondu en binaire64 ({e64['voisins_confondus_si_binaire64']}) ; écrit en chaîne exacte : {e64['ecrit_en_chaine_exacte']}.")
    cst = r["constantes"]
    L.append(f"Constantes : seuil de T3 `{cst['s_pur_hex']}` = 1.0 − 1e-9 : {cst['s_pur_egal_1_moins_1e_9']} ; = float('0.999999999') : {cst['s_pur_egal_float_0_999999999']} ; "
             f"borne haute [0 ; 1] = 1.0 + 1e-12 : {cst['borne_haute_egale_1_plus_1e_12']} ; G = {cst['G']}.\n")
    t12 = r["table_de_controle_12"]
    L.append(f"## Tableau de contrôle du § 12.1 ({t12['nombre_de_lignes_lues']} lignes lues dans le texte de la spécification v2)\n")
    L.append("| Budget | Contraste | Écart max. absolu (moyenne, écart-type, 4 quantiles) | Conforme |\n|---|---|---|---|")
    for d in t12["lignes"]:
        L.append(f"| {d['budget']} | {d['contraste']} | {_e(d['ecart_max_abs'])} | {'oui' if d['ok'] else '**NON**'} |")
    L.append("")
    L.append("## Concordance avec l'analyse de référence, contraste par contraste\n")
    L.append("Niveau « arrêt » : les cinq contrastes dont une discordance arrête la lecture ; « alerte » : les onze autres.\n")
    L.append("| Budget | Contraste | Niveau | Écart max. absolu | n / zéros |\n|---|---|---|---|---|")
    for cb in ("1", "2"):
        for lib, d in cmp_["detail_par_contraste"][cb].items():
            L.append(f"| {cb} | {lib} | {d['niveau']} | {_e(d['ecart_max_abs'])} | {'oui' if d['n_identique'] and d['zeros_exacts_identiques'] else '**NON**'} |")
    L.append("")
    L.append(f"Écart maximal absolu : tous contrastes **{_e(cmp_['ecart_maximal_absolu'])}** ; contrastes à arrêt {_e(cmp_['ecart_maximal_absolu_contrastes_a_arret'])} ; "
             f"contrastes à alerte {_e(cmp_['ecart_maximal_absolu_contrastes_a_alerte'])}. Écart A/B maximal sur les z des quatre contrastes primaires : "
             f"{_e(max(cmp_['z_pi']['ecart_abs'].values()))}. Classes comparées : {cmp_['classes']['nombre_de_classes_comparees']}, "
             f"différences : {len(cmp_['classes']['differences'])} ; éléments à la frontière : {len(cmp_['classes']['elements_a_la_frontiere']) + len(cmp_['verdicts_et_declencheurs']['elements_a_la_frontiere'])}.\n")
    L.append("## Classes (première condition vraie ; budget 1 / budget 2)\n")
    at = r["attendus_12"]
    L.append(f"- Table A (Δ(R3, R2) sur V) : ligne {at['table_A']['obtenu'][0]}, « {at['table_A']['obtenu'][1]} » — conforme au § 12.1 : {at['table_A']['ok']}")
    noms_tables = {"table_B": "Table B (détection V)", "table_Bprime": "Table B′ (exploitabilité moyenne X̄)",
                   "table_C": "Table C (détection (ii), numéro de ligne)"}
    for tb, nom in noms_tables.items():
        L.append(f"- {nom} :")
        for court, v in at[tb].items():
            L.append(f"  - {court} : {v['obtenu'][0]} / {v['obtenu'][1]} — conforme : {v['ok']}")
    L.append("")
    L.append("## Contrôles de santé et verdicts du § 9\n")
    ct = at["controles"]
    L.append(f"- T2 non déclenché : {ct['T2_non_declenche']} ; T3 non déclenché : {ct['T3_non_declenche']} (tâches à poids pur : {ct['T3_nb_taches']}) ; "
             f"T4 non déclenché : {ct['T4_non_declenche']} (tâches à cosinus moyen ≥ 0,999 : {ct['T4_nb_taches']}, attendu 5 et 2)")
    L.append(f"- T5 non déclenché : {ct['T5_non_declenche']} (plus grand écart standard − renforcé : {ct['T5_plus_grand_standard_moins_renforce']:.6f}, attendu 0,00039 ; "
             f"plus grand écart de contraste : {ct['T5_plus_grand_ecart_de_contraste']:.6f}, attendu 0,00043) ; "
             f"T6 non déclenché : {ct['T6_non_declenche']} (plus grand écart à α : {ct['T6_plus_grand_ecart_a_alpha']:.6f}, attendu 0,00019)")
    v9 = at["verdicts_9"]["obtenu"]
    L.append(f"- Le mélange bat l'historique (HR1) : **{v9['HR1']}** ; réentraîner vaut mieux que ne rien faire (HR0) : **{v9['HR0']}** ; "
             f"la régularisation ne nuit pas (HR3) : **{v9['HR3']}** ; oublier coûte (HR2, descriptif) : **{v9['HR2']}** — conformes au § 12.1 : {at['verdicts_9']['ok']}.\n")
    L.append("## Gardes de la réplication : cas sain et artefact (§ 12.3)\n")
    ca = r["cas_a_original_contre_lui_meme"]
    L.append(f"- (a) artefact, l'original contre lui-même : écart g des quatre contrastes primaires {ca['g_pi']} (tous nuls : {ca['tous_nuls']}) ; "
             f"TR2 déclenché : {ca['TR2_declenche']} ; {ca['nombre_de_comptes']} comptes « graines neuves », tous égaux à 200 : {ca['tous_egaux_a_200']} ; "
             f"arrêt « graines non neuves » : {ca['arret_graines_non_neuves']} ; code de sortie {ca['code_de_sortie']} ; lecture autorisée : {ca['lecture_autorisee']} ; "
             f"issue brute : « {ca['issue_brute']} » → conforme : {ca['ok']}")
    cb_ = r["cas_12_3_b_a_e"]
    b, cc, dd, e3, e2 = cb_["b_cas_sain"], cb_["c_R3_plus_0_06"], cb_["d_R3_moins_0_03"], cb_["e_3_taches_gardees"], cb_["e_2_taches_gardees"]
    L.append(f"- (b) cas sain (+1e-6 ; R3 en plus +0,01) : plus grand compte {b['comptes_max']} ; TR1 {b['TR1']} ; TR2 {b['TR2']} ; arrêt {b['arret']} ; code {b['code_de_sortie']} → {b['ok']}")
    L.append(f"- (c) R3 +0,06 : TR1 déclenché {cc['TR1']}, z de R3 {cc['z_R3']} (positifs) → {cc['ok']}")
    L.append(f"- (d) R3 −0,03 borné à 0 : TR1 déclenché {dd['TR1']}, z de R3 {dd['z_R3']} (négatifs) → {dd['ok']}")
    L.append(f"- (e) une variante (R1), trois tâches gardent leur V original : compte {e3['compte_R1_V']}, arrêt {e3['arret_graines_non_neuves']}, code {e3['code_de_sortie']} → {e3['ok']} ; "
             f"deux tâches : compte {e2['compte_R1_V']}, arrêt {e2['arret_graines_non_neuves']}, code {e2['code_de_sortie']} → {e2['ok']}\n")
    L.append("## Suite d'essais (§ 12.2, 12.3, 12.4, 12.5, mutations)\n")
    es = r["essais"]
    if es.get("lances"):
        L.append(f"- {es['essais']} essais lancés avec `{r['interpreteur']}` : {es['essais'] - es['echecs'] - es['erreurs']} passés, {es['echecs']} échoués, "
                 f"{es['erreurs']} en erreur, {es['ignores']} ignorés ; durée {es['duree_pytest_s']} s.")
        noms = {"c12_1": "§ 12.1 course originale", "c12_2": "§ 12.2 branches des tables, verdicts, contrôles, déclencheurs, issues",
                "c12_3": "§ 12.3 gardes de la réplication (a) à (e) et comparaison A/B", "c12_4": "§ 12.4 entiers de 64 bits et règle D",
                "c12_5": "§ 12.5 gardes d'entrée, cas sain et artefact", "mut": "essais rattachés aux mutations de B v1 et aux exigences neuves",
                "base": "constantes, générateur, quantiles, lecture, CLI et divers"}
        for cat, d in sorted(es["par_categorie"].items()):
            L.append(f"  - {noms.get(cat, cat)} : {d['essais']} essais, {d['echecs']} échecs")
    else:
        L.append(f"- Suite d'essais non lancée par cette commande ({es.get('raison', '')}).")
    L.append(f"- Campagne de mutations : {r['mutations']['consigne']}.\n")
    L.append("## Marges aux seuils\n")
    L.append("Plus petite distance entre une quantité comparée et son seuil, sur les comparaisons évaluées pour chaque classe (frontière numérique : 1e-9). Les six plus petites :\n")
    for m in r["plus_petites_marges_aux_seuils"]:
        L.append(f"- {m['classe']} : {m['marge_min_au_seuil']:.3e}")
    L.append(f"\nClasses marquées à la frontière : {r['classes_a_la_frontiere'] or 'aucune'}.\n")
    rc = r["recoupements_hors_specification"]
    L.append("## Recoupements hors contrat de la spécification (informatif)\n")
    L.append(f"{rc['nombre_de_comparaisons']} comparaisons de champs de l'analyse de référence qui ne font pas partie du contrat "
             f"(moyennes par variante, cosinus moyens par tâche de R4, part de tâches à poids pur de R3, contrastes standard seul / renforcé seul). "
             f"Écart maximal absolu : **{_e(rc['ecart_maximal_absolu'])}**.\n")
    L.append("## Table de correspondance « élément du § 11.1 → clé JSON »\n")
    L.append("| Élément | Clé(s) JSON |\n|---|---|")
    for x in r["table_de_correspondance_des_cles"]:
        L.append(f"| {x['element']} | {x['cle_json']} |")
    L.append("")
    L.append("## Commande exacte pour la course (chemins à compléter par la session principale)\n")
    L.append("```\n" + r["commande_pour_la_course"] + "\n```\n")
    L.append("Aucune option ne peut changer un seuil, sauter une vérification ou forcer une racine. Seule option qui touche une ligne du § 10.4 : "
             "`--plomberie-fausse` (défaut neutre : non ; sa valeur est écrite dans `options.plomberie_fausse_V0`). Sortie : code 0 (lecture autorisée), "
             "2 (arrêt d'entrée, aucune sortie) ou 3 (arrêt de contrôle, sortie écrite, `lecture_autorisee: false`).\n")
    L.append("## Ce que cette validation ne couvre pas\n")
    for x in r["ce_que_la_validation_ne_couvre_pas"]:
        L.append(f"- {x}")
    L.append("\n## Ambiguïtés restantes (lecture prudente retenue dans chaque cas)\n")
    for x in r["ambiguites_restantes"]:
        L.append(f"- {x}")
    L.append("\n## Fichiers ouverts pendant tout le travail (lecture ou exécution)\n")
    for x in r["fichiers_ouverts"]:
        L.append(f"- {x}")
    L.append(f"\n## Modèle\n\n{r['modele']}.\n")
    return "\n".join(L) + "\n"


def valider_originale_cli(a) -> int:
    dossier = Path(a.dossier)
    dossier_sortie = Path(a.dossier_sortie) if a.dossier_sortie else dossier
    chemins = [dossier_sortie / n for n in (NOM_SORTIE_B, NOM_VALIDATION_JSON, NOM_VALIDATION_MD)]
    existants = [str(p) for p in chemins if p.exists()]
    if existants:
        sys.stderr.write("ARRÊT : fichiers déjà existants (jamais écrasés ; nouvelle version = nouveau nom) : "
                         + ", ".join(existants) + "\n")
        return 2
    try:
        rapport = valider_originale(dossier, dossier_sortie, executer_essais=a.executer_essais, mutations=a.mutations)
    except (Arret, ErreurInterne) as e:
        sys.stderr.write(f"ARRÊT : {e}\n")
        return 2
    sha_json = ecrire_json_neuf(dossier_sortie / NOM_VALIDATION_JSON, rapport)
    md = rapport_markdown(rapport)
    with open(dossier_sortie / NOM_VALIDATION_MD, "x", encoding="utf-8", newline="\n") as f:
        f.write(md)
    sys.stderr.write(f"{NOM_VALIDATION_JSON} sha256 {sha_json}\n")
    sys.stderr.write("validation " + ("RÉUSSIE" if rapport["conclusion"]["validation_reussie"] else "ÉCHEC") + "\n")
    return 0 if rapport["conclusion"]["validation_reussie"] else 3


def _cmd_valider(a) -> int:
    return valider_originale_cli(a)


if __name__ == "__main__":
    sys.exit(main())
