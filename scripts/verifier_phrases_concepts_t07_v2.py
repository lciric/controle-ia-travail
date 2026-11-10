#!/usr/bin/env python3
"""Vérification, sélection et assemblage du jeu de phrases des concepts sans lien de T0.7 (témoin T7-P9) — v2.

Version 2 (R12) du script `scripts/verifier_phrases_concepts_t07_v1.py` (`6bc2665a…`, commit `1b87dfe1`), écrite sous la
consigne de la mère `consigne-script-concepts-v2-reecriture-v1.md` (`6801069b…`). Elle reprend tous les modes du v1, à
l'identique sur un dossier sans réécriture, sauf les corrections nommées (D-1, D-2, D-4, D-6, D-8 de la contre-lecture
`25bce60e…`), et ajoute la voie « réécriture d'un concept entier » (consigne des concepts, sections 3 et 7) :

    verifier --tour 2 --passe 1|2   remise versionnée des seuls concepts réécrits (72 paires chacun, indices 1 à 72) ;
                 mêmes contrôles ; C8 entre les paires neuves et contre les paires gardées des autres concepts (sélection
                 v1 après le décompte v1 : prises et réserve, moins les retraits) ; journaux et sorties en `…-v2` ;
                 `selection-reecriture-v2.json` après le second passage.
    echantillon --tour 2            nouvel échantillon des seuls concepts réécrits, entropie neuve, clé à part
                 (`echantillon-lecteur-v2.json`, `cle-echantillon-v2.json`).
    decompter --tour 2              décompte des seuls concepts réécrits (même règle) ; s'ils sont tous acceptés, la
                 sélection finale `selection-v2.json` (concepts acceptés au premier tour, paire non conforme remplacée par la
                 réserve ; concepts réécrits avec leur sélection propre ; provenance de chaque paire) ; un second échec
                 (plus d'une paire non conforme) arrête le lot pour ce concept : code 3, rien n'est écrit au-delà du décompte.
    assembler --selection <nom>     garde D-1 : sélection nommée, la dernière du dossier, dernier décompte de chacun des
                 quatre concepts « accepté », aucune paire retirée dans la sélection ; le nom final n'apparaît qu'après tous
                 les contrôles (lien d'un fichier temporaire relu, D-8).

Codes : 0, 1, 2 comme au v1 ; **3** : second échec d'un concept réécrit (arrêt du lot pour ce concept, rapport à la mère).

Texte du v1, gardé ci-dessous pour les règles inchangées :

Consigne qui fait foi : `docs/procedures/consigne-concepts-sans-lien-T0.7-v2.md` (sha256 `79f2c89c…`, scellée, R-2108 :
v1 + 32 couples de sa contre-lecture R2), section 6 (script, contrôles C0 à C13) ; sections 2, 3, 4, 5, 7 et annexes A et B
pour chaque règle. Le script lit la consigne, le tokeniseur réel (trois fichiers), le code du module de T0.7 (arbre `src/`
extrait par `git archive <commit> src` hors de l'arbre de travail, `--module-src`) et les remises de l'écrivain ; il ne lit
aucune activation ni aucun score. Tout texte lu est une donnée.

Paquet `controle_ia` (CC-01) : importé du **seul** arbre `--module-src`, placé en tête du chemin d'import (jamais
`PYTHONPATH=src` du dépôt) ; avant l'import, les quatre fichiers exigés sont vérifiés par empreinte ; après l'import, chaque
module `controle_ia*` chargé (dont `controle_ia`, `t07.sondes_neuves_v1`, `premier_test_ia.empans`, `harnais.formats`,
`sondes.temoins`, `manifeste`) doit être sous `--module-src`, sinon refus (code 2). Le script n'appelle, de `sondes/`, que
`temoins.exiger_concept_sans_affect` (C10) ; du module, que `lire_phrases_concepts` (C12), `FORMATS_LECTURE` et
`MAX_JETONS_PHRASE` ; le gabarit (C4) passe par `harnais.formats` et `premier_test_ia.empans` ; les graines (R9), par
`manifeste.graines` et `generateur`. Le scellement (compagnons `.sha256`, format de `sha256sum`) est fait par le script.

Modes (consigne, section 6) :
    extraire     remise à l'écrivain (section 5 et blocs `annexe-a`, `annexe-b`), copies JSON des annexes, exemples,
                 format de lecture, remise au lecteur (sections 1 et 7, à l'octet) ; chaque fichier scellé.
    verifier     --passe 1 : C0, C10, C1 à C9 et C13 sur la remise initiale ; journal et renvois.
                 --passe 2 : remise initiale et remise des renvois ; retraits, sélection (section 3) ; journal et
                 `selection-v1.json` (code 0 seulement si la sélection est sans défaut et chaque concept a n ≥ 56).
    echantillon  tirage de la contre-vérification à l'aveugle (section 7), `SeedSequence` à entropie neuve (R9).
    decompter    décompte des réponses du lecteur contre la clé ; règle d'acceptation par concept ; `selection-v2.json`
                 si une paire non conforme seule est retirée (CC-15) et qu'aucun concept n'attend un second lecteur ou
                 une réécriture.
    assembler    octets du fichier construits deux fois en mémoire, contrôlés (C1 de la section 2, C2 à C11), C12 sur une
                 copie temporaire hors de `donnees/` ; `phrases-concepts-v1.jsonl` écrit seulement si tout passe, relu et
                 égal à l'octet, scellé (CC-05) ; un défaut est un refus (code 2), le nom final n'existe pas.
    rejouer-c12  C11 et C12 rejoués sur un fichier assemblé et scellé, au code d'un autre commit du module (section 6 :
                 ligne `CODE-T07` d'un autre commit) ; choix de ce script.

Codes : 0 aucun défaut ; 1 au moins une paire en défaut (liste écrite) ; 2 refus (entrées, C0, C10, C11, C12, toute
exception non prévue ; motif écrit au journal du refus et sur la sortie d'erreur). Aucun repli silencieux (R5).

    .venv/bin/python scripts/verifier_phrases_concepts_t07_v1.py verifier --passe 1 \\
        --consigne docs/procedures/consigne-concepts-sans-lien-T0.7-v2.md --dossier donnees/t07-concepts-v1 \\
        --tokeniseur <dossier des trois fichiers> --module-src <arbre src/ du commit> \\
        --remise donnees/t07-concepts-v1/remise-ecrivain-v1.jsonl

Choix de ce script, dits comme tels (rapport
`docs/notes/g0-deux-semaines-v1/t07-concepts-v1/rapport-script-verification-concepts-v1.md`) :
- l'empreinte attendue de la consigne est celle de la v2 ; une autre consigne n'est lue que par
  `--empreinte-consigne <hex>` (écart déclaré au journal) ; un autre commit du module, par `--commit-module` et
  `--empreintes-module <json>` (écart déclaré) ; `lecture_v2.py` doit exister sous `--module-src` (empreinte écrite) ;
- C1 : une ligne illisible, un concept hors de la liste fermée ou un `indice` non entier ou hors de 1..72 est une « ligne
  rejetée » (sans paire) ; la case (concept, indice) qu'elle devait remplir est alors « absente », en défaut et renvoyée ;
  deux lignes pour une même case : la case est en défaut, son contenu n'est pas contrôlé ; l'ordre des clés n'est qu'une
  information ; les phrases d'une case en défaut à C1 sont contrôlées (C2 à C9) quand elles sont des chaînes ;
- second passage (CC-16) : une paire renvoyée non rendue, ou rendue en défaut à C1, est retirée d'abord ; puis C2 à C7 et
  C9 ; les paires en défaut sont retirées ; puis C8 entre les seules paires restantes ; une paire non renvoyée en défaut
  au second passage est un refus (incohérence entre passes), jamais un retrait ; un enregistrement d'une paire non
  renvoyée dans la remise des renvois, ou une ligne rejetée, est écrit et fait sortir en code 1 ;
- C2 : les mots sont les suites `[A-Za-z]+` ; une majuscule hors du premier caractère n'est admise que dans un mot de la
  liste fermée, ou dans une phrase du concept de `geographie` ;
- C13 : la règle du premier mot est appliquée par concept et sur l'ensemble des concepts ; les mots de nombre d'une paire
  sont comparés comme multiensembles ;
- `assembler` : un défaut de C2 à C9 sur la sélection (impossible après un second passage en code 0) est aussi un refus ;
- journal d'un refus : `journal-refus-<mode>-<horodatage>.txt` dans le dossier, s'il existe ; les noms de la consigne
  restent aux passages complets (R12) ;
- non écrits dans cette v1 du script (section 3 et 7) : le second lecteur de Q4, la réécriture d'un concept entier, la
  remise complémentaire (indices 73 à 72 + m) ; s'ils sont déclenchés, une v2 de ce script (R12).

Choix de la v2, dits comme tels (rapport `…/rapport-script-verification-concepts-v2.md`) :
- toujours non écrits : le second lecteur de Q4 et la remise complémentaire (CC-17) ; le script échoue fermé (code 1, ou
  refus du second tour si le premier décompte attend un second lecteur) ;
- second tour : les paires gardées des autres concepts (« fixes ») ne sont jamais en défaut ; une paire neuve en conflit
  (C8) avec une paire fixe est en défaut ; entre paires neuves, la règle de conflit de la section 3 ; une ligne d'un
  concept non réécrit dans la remise du second tour est une ligne rejetée ;
- D-2 : au second passage (des deux tours), une ligne rejetée ou un enregistrement d'une paire non renvoyée dans la remise
  des renvois est un **refus propre (code 2) avant toute écriture d'un nom définitif** : le second passage se rejoue sur
  une remise des renvois corrigée et versionnée ;
- D-4 : C8 du second passage est joué en deux temps : (a) les paires réécrites en conflit avec une paire non réécrite
  (ou fixe) sont retirées ; (b) les réécrites restantes, par rang croissant, n'entrent que si elles n'ont aucun conflit
  avec une réécrite déjà entrée (« une paire déjà retirée n'entre plus dans la comparaison ») ;
- D-6 : chaque module `controle_ia*` chargé est nommé au journal avec son empreinte ;
- D-8 : `decompter` refuse une clé tirée sur une entropie imposée sans `--essai` (écrit au décompte), et `assembler`
  refuse un décompte de clé imposée sans `--essai` ;
- `phrases-concepts-v1.jsonl` et `journal-assemblage-v1.txt` gardent les noms des sections 2 et 8 (jamais écrits : un
  seul assemblage) ; tout ce que le second tour écrit porte `-v2`.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import re
import sys
import tempfile
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import numpy as np

RACINE_DEPOT = Path(__file__).resolve().parents[1]
VERSION = "verifier_phrases_concepts_t07_v2"

# ---------------------------------------------------------------------------------------------------------- entrées (C0)
EMPREINTE_CONSIGNE = "79f2c89cc0763f187734e7487e837ab179fa91126a40e61dbef20f33603f1ee4"
REVISION_TOKENISEUR = "0e9e39f249a16976918f6564b8830bc894c89659"
EMPREINTES_TOKENISEUR = {
    "tokenizer.json": "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4",
    "tokenizer_config.json": "177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424",
    "special_tokens_map.json": "6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec",
}
COMMIT_MODULE = "8dc1cb09"
COMMIT_MODULE_COMPLET = "8dc1cb09f5e764f37aa87cf1410bc6586249b3d1"
EMPREINTES_MODULE_8DC1CB09 = {
    "t07/sondes_neuves_v1.py": "b1c59783ed231c88c5671bc124b0a3f448e5b948b48677db2f361fe6d05c085d",
    "premier_test_ia/empans.py": "58043c95c8d6afc9cf155015c2cffb2130596d479445a7b63a3b1cd9522746c0",
    "harnais/formats.py": "98dbfa9b13578946c4d731c4bb1cfcfb85b9fd0cacdfd56a786042c93e6ef6b4",
    "sondes/temoins.py": "3b051b6fc2d78eeb4a44aab8a385bbce65095998e944b80e5f2a66e21b57faf7",
}
FICHIERS_MODULE = tuple(EMPREINTES_MODULE_8DC1CB09)
EMPREINTE_MANIFESTE_8DC1CB09 = "1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d"
MODULES_EMPLOYES = ("controle_ia", "controle_ia.gardes", "controle_ia.t07.sondes_neuves_v1",
                    "controle_ia.premier_test_ia.empans", "controle_ia.harnais.formats", "controle_ia.sondes.temoins",
                    "controle_ia.manifeste")
DATE_GABARIT = "26 Jul 2024"  # `harnais/validation_reelle.py` l. 85 (consigne, C4)

# ------------------------------------------------------------------------------------------------- règles (sections 2 à 4)
CONCEPTS = ("chats", "meteo", "sports", "geographie")
CONCEPT_NOMS_PROPRES = "geographie"
DOMAINES = tuple(f"N{i}" for i in range(1, 9))
PAIRES_REMISE = 72
PAIRES_FICHIER = 64
PLANCHER = 56
CLES_REMISE = ("concept", "indice", "domaine_neutre", "phrase_concept", "phrase_neutre")
CLES_FICHIER = ("concept", "indice", "phrase_concept", "phrase_neutre")
ROLES = ("phrase_concept", "phrase_neutre")
ALPHABET = re.compile(r"[A-Z][A-Za-z ,'-]*\.")
CARACTERE_PERMIS = re.compile(r"[A-Za-z ,'.-]")
MAJUSCULES_PERMISES = frozenset(("Siamese", "Maine", "Coon", "Sphynx", "Celsius", "Fahrenheit", "Olympic", "Olympics"))
JETONS_MIN, JETONS_MAX = 8, 40
ECART_MAX = Fraction(15, 100)
DISTANCE_DOUBLON = 1
DISTANCE_EXEMPLE = 2
SUITE_EXEMPLE = 6
C13_MOYENNE_SIGNEE = Fraction(5, 100)
C13_ENTREES_MIN = 8
C13_PART_MAX = Fraction(60, 100)
C13_PREMIER_MOT_HAUT = Fraction(1, 2)
C13_PREMIER_MOT_BAS = Fraction(1, 10)
MOTS_NOMBRE = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "twenty",
               "thirty", "forty", "fifty", "hundred", "thousand", "million", "dozen", "half")
CATEGORIES_A = tuple(f"A{i}" for i in range(1, 8))
CATEGORIE_ADRESSE = "A7"
MOTIF_ENTREE = re.compile(r"[a-z]+( [a-z]+)*")

MARQUEUR_DEBUT = "<!-- section-5-debut -->"
MARQUEUR_FIN = "<!-- section-5-fin -->"
CLOTURE = "```"
BORNES_LECTEUR = (("## 1. ", "## 2. "), ("## 7. ", "## 8. "))

NOMS_EXTRAITS = {
    "remise": "remise-a-l-ecrivain-v1.md",
    "annexe_a": "annexe-a-mots-interdits-v1.json",
    "annexe_b": "annexe-b-lexiques-v1.json",
    "exemples": "exemples-v1.jsonl",
    "format": "format-lecture-v1.json",
    "remise_lecteur": "remise-au-lecteur-v1.md",
}
JOURNAL_EXTRACTION = "journal-extraction-v1.txt"
JOURNAL_PASSE = "journal-verification-passe{p}-v1.txt"
RENVOIS = "renvois-passe1-v1.json"
SELECTION = "selection-v1.json"
SELECTION_V2 = "selection-v2.json"
ECHANTILLON = "echantillon-lecteur-v1.json"
CLE_ECHANTILLON = "cle-echantillon-v1.json"
JOURNAL_ECHANTILLON = "journal-echantillon-v1.txt"
REPONSES = "reponses-lecteur-v1.json"
DECOMPTE = "decompte-contre-verification-v1.json"
JOURNAL_DECOMPTE = "journal-decompte-v1.txt"
FICHIER_ASSEMBLE = "phrases-concepts-v1.jsonl"
JOURNAL_ASSEMBLAGE = "journal-assemblage-v1.txt"

# Second tour (réécriture d'un concept entier, sections 3 et 7) : noms versionnés `-v2` (R12)
JOURNAL_PASSE_V2 = "journal-verification-passe{p}-v2.txt"
RENVOIS_V2 = "renvois-passe1-v2.json"
SELECTION_REECRITURE = "selection-reecriture-v2.json"
ECHANTILLON_V2 = "echantillon-lecteur-v2.json"
CLE_ECHANTILLON_V2 = "cle-echantillon-v2.json"
JOURNAL_ECHANTILLON_V2 = "journal-echantillon-v2.txt"
REPONSES_V2 = "reponses-lecteur-v2.json"
DECOMPTE_V2 = "decompte-contre-verification-v2.json"
JOURNAL_DECOMPTE_V2 = "journal-decompte-v2.txt"
REMISE_1, REMISE_2 = "remise-1", "remise-2"
CODE_ARRET = 3                      # second échec d'un concept réécrit : arrêt du lot pour ce concept
MOTIF_SELECTION = re.compile(r"selection-v([0-9]+)\.json")
MOTIF_DECOMPTE = re.compile(r"decompte-contre-verification-v([0-9]+)\.json")
DECISION_ACCEPTE = "accepté"
DECISION_REECRITURE = "réécriture"
DECISION_Q4 = "second lecteur"

VALEURS_Q1 = CONCEPTS + ("aucun",)
CLES_REPONSE = ("item", "Q1_A", "Q1_B", "Q2", "Q3_A", "Q3_B", "Q4_A", "citation_Q4_A", "Q4_B", "citation_Q4_B",
                "Q5_A", "Q5_B")


class Refus(Exception):
    """Refus (code 2) : entrée, C0, C10, C11, C12, ou exception non prévue ; le motif est écrit."""


class _Objet(list):
    """Objet JSON lu en liste de couples (clés répétées visibles, ordre gardé)."""


def maintenant() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


# ----------------------------------------------------------------------------------------------------------------------
# Sceaux (R6), écriture neuve (R12), absence vérifiée sur disque (R11) — format de `sha256sum`
# ----------------------------------------------------------------------------------------------------------------------

_LIGNE_SCEAU = re.compile(r"^([0-9a-f]{64})  (\S.*)$")


def empreinte(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def compagnon(chemin) -> Path:
    return Path(str(chemin) + ".sha256")


def lire_compagnon(chemin) -> str:
    c = compagnon(chemin)
    if not c.is_file():
        raise Refus(f"{Path(chemin).name} : compagnon {c.name} absent sur disque")
    lignes = [l for l in c.read_text(encoding="utf-8").splitlines() if l.strip()]
    m = _LIGNE_SCEAU.match(lignes[0]) if len(lignes) == 1 else None
    if not m or m.group(2) != Path(chemin).name:
        raise Refus(f"{c} : une ligne « <sha256>  {Path(chemin).name} » attendue")
    return m.group(1)


def sceller(chemin) -> str:
    h = empreinte(chemin)
    c = compagnon(chemin)
    if c.exists():
        if lire_compagnon(chemin) != h:
            raise Refus(f"{chemin} déjà scellé avec une autre empreinte : R12, jamais réécrit")
        return h
    with open(c, "x", encoding="utf-8") as f:
        f.write(f"{h}  {Path(chemin).name}\n")
    return h


def lire_scelle(chemin, role: str) -> bytes:
    chemin = Path(chemin)
    if not chemin.is_file():
        raise Refus(f"{role} absent sur disque ({chemin})")
    octets = chemin.read_bytes()
    attendu = lire_compagnon(chemin)
    if sha_octets(octets) != attendu:
        raise Refus(f"{role} : sha256 {sha_octets(octets)} ≠ compagnon {attendu}")
    return octets


def exiger_absents(chemins) -> None:
    deja = [str(c) for c in chemins if Path(c).exists() or compagnon(c).exists()]
    if deja:
        raise Refus(f"fichier(s) de sortie déjà présent(s) : {deja} ; R12 : on n'écrase jamais (nouvelle version = "
                    "nouveau nom)")


def ecrire_neuf(chemin: Path, octets: bytes) -> None:
    try:
        with open(chemin, "xb") as f:
            f.write(octets)
    except FileExistsError:
        raise Refus(f"{chemin} existe déjà : R12, jamais réécrit") from None


def exiger_hors_depot(chemin: Path, role: str) -> None:
    r = Path(chemin).resolve()
    racine = Path(RACINE_DEPOT).resolve()
    if r == racine or racine in r.parents:
        raise Refus(f"{role} : dossier dans l'arbre de travail ({r}) ; la consigne le veut hors de l'arbre (section 6)")


def json_canonique(objet) -> bytes:
    return (json.dumps(objet, ensure_ascii=True, indent=2) + "\n").encode("ascii")


# ----------------------------------------------------------------------------------------------------------------------
# Texte : mots (méthode de `scripts/verifier_jeux_synthetiques_t07_v2.py` l. 142-146, 173-176), distances
# ----------------------------------------------------------------------------------------------------------------------

def normaliser(texte: str) -> list[str]:
    """Mots sans casse, sans accents, sans ponctuation (suites `[0-9a-z]+` après décomposition Unicode)."""
    t = unicodedata.normalize("NFKD", texte)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.findall(r"[0-9a-z]+", t)


def suite(mots) -> str:
    return " " + " ".join(mots) + " "


def motif_entree(entree: str) -> str:
    """Une entrée d'annexe (un mot ou une suite de mots) cherchée comme suite de mots entiers."""
    return suite(normaliser(entree))


def distance_edition(a, b) -> int:
    """Levenshtein sur deux suites de mots."""
    if not a:
        return len(b)
    if not b:
        return len(a)
    prec = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        cour = [i]
        for j, y in enumerate(b, 1):
            cour.append(min(prec[j] + 1, cour[j - 1] + 1, prec[j - 1] + (x != y)))
        prec = cour
    return prec[-1]


def au_plus_un(a, b) -> bool:
    """Distance d'édition en mots au plus 1 (égalité, une substitution, une insertion ou une suppression)."""
    la, lb = len(a), len(b)
    if la == lb:
        return sum(x != y for x, y in zip(a, b)) <= 1
    if abs(la - lb) != 1:
        return False
    if la > lb:
        a, b = b, a
    i = 0
    while i < len(a) and a[i] == b[i]:
        i += 1
    return list(a[i:]) == list(b[i + 1:])


def n_grammes(mots, n: int) -> set:
    return {tuple(mots[i:i + n]) for i in range(len(mots) - n + 1)}


def ecart_relatif(a: int, b: int) -> Fraction:
    """|a − b| / max(a, b) (`ecart_relatif`, script des jeux l. 168-170), en fraction exacte."""
    m = max(a, b)
    return Fraction(abs(a - b), m) if m else Fraction(0)


def compter_jetons(tok, texte: str) -> int:
    return len(tok.encode(texte, add_special_tokens=False).ids)


# ----------------------------------------------------------------------------------------------------------------------
# Journal
# ----------------------------------------------------------------------------------------------------------------------

class Journal:
    def __init__(self, mode: str) -> None:
        self.mode = mode
        self.lignes: list[str] = []
        self.reserves: list[str] = []
        self.chemin: Path | None = None
        self.debut = maintenant()

    def ligne(self, texte: str = "") -> None:
        self.lignes.append(texte)

    def info(self, texte: str) -> None:
        self.lignes.append(f"[INFO] {texte}")

    def ecart(self, texte: str) -> None:
        self.lignes.append(f"[ÉCART DÉCLARÉ] {texte}")

    def reserve(self, texte: str) -> None:
        self.reserves.append(texte)
        self.lignes.append(f"[RÉSERVE] {texte}")

    def ok(self, controle: str, nom: str, detail: str = "") -> None:
        self.lignes.append(f"[OK] {controle} — {nom}" + (f" : {detail}" if detail else ""))

    def controle(self, controle: str, nom: str, defauts: list) -> None:
        if not defauts:
            self.ok(controle, nom)
            return
        self.lignes.append(f"[DÉFAUT] {controle} — {nom} : {len(defauts)} défaut(s)")
        for d in defauts:
            self.lignes.append(f"    - {d['paire']} ({d['role']}) : {d['motif']}")

    def texte(self) -> str:
        return "\n".join(self.lignes) + "\n"


def entete(journal: Journal, a) -> None:
    journal.ligne(f"# Journal — {VERSION}, mode {a.mode}" + (f" (passe {a.passe})" if getattr(a, "passe", None) else "")
                  + (" — second tour (réécriture d'un concept entier)" if getattr(a, "tour", 1) == 2 else ""))
    journal.ligne(f"début : {journal.debut} (horloge UTC du système)")
    script = Path(__file__).resolve()
    journal.ligne(f"script : {script} sha256 {empreinte(script)}")
    journal.ligne(f"python : {sys.version.split()[0]} ; numpy {np.__version__}")


# ----------------------------------------------------------------------------------------------------------------------
# Paires et défauts
# ----------------------------------------------------------------------------------------------------------------------

@dataclass
class Paire:
    concept: str
    indice: object                    # entier (remise ou fichier) ; « E1 »… pour les exemples
    domaine: str | None
    phrase_concept: str
    phrase_neutre: str
    reecrite: bool = False
    indice_remise: int | None = None
    fixe: bool = False                # second tour : paire gardée d'un autre concept, jamais en défaut
    remise: str = REMISE_1
    mots: dict = field(default_factory=dict, repr=False)
    suites: dict = field(default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        self.mots = {r: normaliser(getattr(self, r)) for r in ROLES}
        self.suites = {r: suite(self.mots[r]) for r in ROLES}

    @property
    def cle(self):
        return (self.concept, self.indice)

    @property
    def nom(self) -> str:
        base = f"{self.concept}/{self.indice}" if isinstance(self.indice, int) else str(self.indice)
        return f"{base} (gardée, {self.remise})" if self.fixe else base

    def rang(self) -> tuple:
        k = self.indice if isinstance(self.indice, int) else int(str(self.indice)[1:])
        return (CONCEPTS.index(self.concept) if self.concept in CONCEPTS else len(CONCEPTS), k)


def defaut(p: Paire, controle: str, role: str, motif: str, **valeurs) -> dict:
    d = {"paire": p.nom, "concept": p.concept, "indice": p.indice, "controle": controle, "role": role,
         "motif": motif, "valeurs": valeurs}
    if p.fixe:
        d["fixe"] = True
    return d


def defaut_case(concept: str, indice: int, controle: str, motif: str, **valeurs) -> dict:
    return {"paire": f"{concept}/{indice}", "concept": concept, "indice": indice, "controle": controle,
            "role": "paire", "motif": motif, "valeurs": valeurs}


def defaut_lieu(lieu: str, controle: str, motif: str, **valeurs) -> dict:
    return {"paire": lieu, "concept": None, "indice": None, "controle": controle, "role": "fichier", "motif": motif,
            "valeurs": valeurs}


def trier(paires) -> list:
    return sorted(paires, key=lambda p: p.rang())


def ordre_case(cle) -> tuple:
    return (CONCEPTS.index(cle[0]), cle[1])


def perdant_passe1(a: Paire, b: Paire) -> Paire:
    """Section 3 : au premier passage, la paire de rang le plus élevé (concept, puis indice de remise) est en défaut."""
    return a if a.rang() > b.rang() else b


def perdant_passe2(a: Paire, b: Paire) -> Paire:
    """Section 3 (CC-16) : au second passage, une paire réécrite en conflit avec une paire non réécrite est en défaut ; de
    deux paires réécrites, celle de rang le plus élevé."""
    if a.reecrite != b.reecrite:
        return a if a.reecrite else b
    return perdant_passe1(a, b)


def avec_fixes(perdant):
    """Second tour : une paire neuve en conflit avec une paire gardée d'un autre concept (fixe) est en défaut ; deux
    paires fixes en conflit : incohérence (elles ont passé le premier tour), refus."""
    def p(a: Paire, b: Paire) -> Paire:
        if a.fixe and b.fixe:
            raise Refus(f"incohérence : deux paires gardées en conflit à C8 ({a.nom}, {b.nom})")
        if a.fixe != b.fixe:
            return b if a.fixe else a
        return perdant(a, b)
    return p


def exiger_aucun_defaut_fixe(defs: list) -> None:
    fixes = [d for d in defs if d.get("fixe")]
    if fixes:
        raise Refus(f"incohérence : paire(s) gardée(s) en défaut au second tour : {[d['paire'] for d in fixes][:6]}")


# ----------------------------------------------------------------------------------------------------------------------
# Consigne : section 5, blocs, remise au lecteur (mode `extraire` ; C0)
# ----------------------------------------------------------------------------------------------------------------------

def oter_citation(ligne: str) -> str | None:
    if ligne.startswith("> "):
        return ligne[2:]
    if ligne.startswith(">"):
        return ligne[1:]
    return None


def lire_consigne(octets: bytes) -> dict:
    """Section 5 (lignes strictement entre les deux marqueurs, préfixe de citation ôté) ; blocs `format-lecture`,
    `annexe-a`, `annexe-b` (hors citation) et `exemples` (cité, dans la section 5) ; remise au lecteur (sections 1 et 7, à
    l'octet). Un bloc ou une borne absente, en double ou mal formée est un refus."""
    try:
        texte = octets.decode("utf-8")
    except UnicodeDecodeError as e:
        raise Refus(f"consigne illisible en UTF-8 ({e})") from None
    lignes = texte.split("\n")
    deb = [i for i, l in enumerate(lignes) if l == MARQUEUR_DEBUT]
    fin = [i for i, l in enumerate(lignes) if l == MARQUEUR_FIN]
    if len(deb) != 1 or len(fin) != 1 or deb[0] >= fin[0]:
        raise Refus(f"consigne : marqueurs de la section 5 absents, en double ou dans le désordre ({len(deb)} début, "
                    f"{len(fin)} fin)")
    d, f = deb[0], fin[0]
    section5 = []
    for i in range(d + 1, f):
        nu = oter_citation(lignes[i])
        if nu is None:
            raise Refus(f"consigne, ligne {i + 1} : ligne de la section 5 sans préfixe de citation")
        section5.append(nu)

    def bloc(nom: str, cite: bool) -> tuple[list[str], str]:
        ouverture = CLOTURE + nom
        pos = [i for i, l in enumerate(lignes) if (oter_citation(l) if l.startswith(">") else l) == ouverture]
        if len(pos) != 1:
            raise Refus(f"consigne : bloc `{nom}` trouvé {len(pos)} fois (une fois attendu)")
        i = pos[0]
        if lignes[i].startswith(">") != cite or (cite and not d < i < f) or (not cite and d < i < f):
            raise Refus(f"consigne : bloc `{nom}` mal placé (ligne {i + 1})")
        corps = []
        for j in range(i + 1, len(lignes)):
            nu = oter_citation(lignes[j]) if cite else lignes[j]
            if nu is None:
                raise Refus(f"consigne : bloc `{nom}` interrompu à la ligne {j + 1}")
            if nu == CLOTURE:
                if not corps:
                    raise Refus(f"consigne : bloc `{nom}` vide")
                return corps, "\n".join(lignes[i:j + 1]) + "\n"
            if nu.startswith(CLOTURE):
                raise Refus(f"consigne : bloc `{nom}`, ligne {j + 1} : clôture mal formée")
            corps.append(nu)
        raise Refus(f"consigne : bloc `{nom}` non clos")

    fmt, _ = bloc("format-lecture", False)
    corps_a, brut_a = bloc("annexe-a", False)
    corps_b, brut_b = bloc("annexe-b", False)
    corps_ex, _ = bloc("exemples", True)
    if len(fmt) != 1:
        raise Refus(f"consigne : bloc `format-lecture` de {len(fmt)} lignes (une attendue)")
    lecteur = ""
    for debut, fin_ in BORNES_LECTEUR:
        pos = {}
        for b in (debut, fin_):
            k = [i for i, l in enumerate(lignes) if l.startswith(b)]
            if len(k) != 1:
                raise Refus(f"consigne : borne « {b.strip()} » de la remise au lecteur trouvée {len(k)} fois (une attendue)")
            pos[b] = k[0]
        if pos[debut] >= pos[fin_]:
            raise Refus(f"consigne : bornes « {debut.strip()} » et « {fin_.strip()} » dans le désordre")
        lecteur += "\n".join(lignes[pos[debut]:pos[fin_]]) + "\n"
    return {"section5": "\n".join(section5) + "\n", "format_ligne": fmt[0], "brut_a": brut_a, "brut_b": brut_b,
            "annexe_a": lire_annexe_a(corps_a), "annexe_b": lire_annexe_b(corps_b), "exemples_lignes": corps_ex,
            "remise_lecteur": lecteur}


def lire_annexe_a(lignes: list[str]) -> dict:
    if len(lignes) != len(CATEGORIES_A):
        raise Refus(f"annexe A : {len(lignes)} lignes, {len(CATEGORIES_A)} attendues (A1 à A7)")
    sortie = {}
    for i, l in enumerate(lignes):
        m = re.fullmatch(r"(A[0-9]+) \| (.+)", l)
        if not m or m.group(1) != CATEGORIES_A[i]:
            raise Refus(f"annexe A, ligne {i + 1} : « {CATEGORIES_A[i]} | <entrée>, <entrée>, … » attendu")
        sortie[m.group(1)] = m.group(2).split(", ")
    return sortie


def lire_annexe_b(lignes: list[str]) -> dict:
    lu: dict = {}
    for i, l in enumerate(lignes):
        m = re.fullmatch(r"(\S+) \| (noyau|champ) \| (.+)", l)
        if not m:
            raise Refus(f"annexe B, ligne {i + 1} : « <concept> | noyau|champ | <entrée>, … » attendu")
        c, partie = m.group(1), m.group(2)
        if c not in CONCEPTS:
            raise Refus(f"annexe B, ligne {i + 1} : concept {c!r} hors de la liste fermée {list(CONCEPTS)}")
        if partie in lu.setdefault(c, {}):
            raise Refus(f"annexe B : {c} {partie} en double")
        lu[c][partie] = [e.split("/") for e in m.group(3).split(", ")]
    manque = [f"{c} {p}" for c in CONCEPTS for p in ("noyau", "champ") if p not in lu.get(c, {})]
    if manque:
        raise Refus(f"annexe B : lignes absentes : {manque}")
    return {c: {"noyau": lu[c]["noyau"], "champ": lu[c]["champ"]} for c in CONCEPTS}


def coherence_annexes(pieces: dict) -> dict:
    """C0 : entrées en minuscules ASCII, sans doublon ; A ∩ B vide ; lexiques deux à deux disjoints ; aucune entrée de
    plusieurs mots de B ne contient un mot de A ni un mot du lexique d'un autre concept (CC-02)."""
    a, b = pieces["annexe_a"], pieces["annexe_b"]
    toutes_a = [e for cat in CATEGORIES_A for e in a[cat]]
    mal = [e for e in toutes_a if not MOTIF_ENTREE.fullmatch(e)]
    if mal:
        raise Refus(f"annexe A : entrées hors de la forme [a-z]+( [a-z]+)* : {mal[:10]}")
    doubles = sorted(e for e, k in Counter(toutes_a).items() if k > 1)
    if doubles:
        raise Refus(f"annexe A : entrées en double : {doubles}")
    formes = {c: [f for partie in ("noyau", "champ") for e in b[c][partie] for f in e] for c in CONCEPTS}
    mal = [f for c in CONCEPTS for f in formes[c] if not MOTIF_ENTREE.fullmatch(f)]
    if mal:
        raise Refus(f"annexe B : formes hors de la forme [a-z]+( [a-z]+)* : {mal[:10]}")
    for i, c in enumerate(CONCEPTS):
        for d in CONCEPTS[i + 1:]:
            commun = sorted(set(formes[c]) & set(formes[d]))
            if commun:
                raise Refus(f"annexe B : lexiques de {c} et de {d} non disjoints : {commun}")
    for c in CONCEPTS:
        doubles = sorted(f for f, k in Counter(formes[c]).items() if k > 1)
        if doubles:
            raise Refus(f"annexe B : formes en double dans {c} : {doubles}")
    commun = sorted(set(toutes_a) & {f for c in CONCEPTS for f in formes[c]})
    if commun:
        raise Refus(f"annexes : A ∩ B non vide : {commun}")
    for c in CONCEPTS:
        for f in formes[c]:
            if " " not in f:
                continue
            s = suite(f.split())
            dans_a = [e for e in toutes_a if motif_entree(e) in s]
            if dans_a:
                raise Refus(f"annexe B : l'entrée « {f} » de {c} contient un mot de l'annexe A : {dans_a}")
            autres = [g for d in CONCEPTS if d != c for g in formes[d] if motif_entree(g) in s]
            if autres:
                raise Refus(f"annexe B : l'entrée « {f} » de {c} contient un mot du lexique d'un autre concept : {autres}")
    return {"entrees_a": {cat: len(a[cat]) for cat in CATEGORIES_A},
            "formes_b": {c: {p: sum(len(e) for e in b[c][p]) for p in ("noyau", "champ")} for c in CONCEPTS}}


def lire_exemples(lignes: list[str]) -> list[Paire]:
    """Bloc `exemples` : huit paires E1 à E8, domaines N1 à N8, clés de la remise ; mal formé → refus."""
    if len(lignes) != 8:
        raise Refus(f"bloc `exemples` : {len(lignes)} lignes, 8 attendues")
    sortie = []
    for k, l in enumerate(lignes, 1):
        try:
            obj = json.loads(l, object_pairs_hook=_Objet)
        except ValueError as e:
            raise Refus(f"exemple {k} : JSON illisible ({e})") from None
        if not isinstance(obj, _Objet) or [c for c, _ in obj] != list(CLES_REMISE):
            raise Refus(f"exemple {k} : clés {list(CLES_REMISE)} attendues dans cet ordre")
        d = dict(obj)
        if d["concept"] not in CONCEPTS or d["indice"] != f"E{k}" or d["domaine_neutre"] != f"N{k}" \
                or not all(isinstance(d[r], str) for r in ROLES):
            raise Refus(f"exemple {k} : concept, indice E{k}, domaine N{k} et deux phrases attendus")
        sortie.append(Paire(d["concept"], d["indice"], d["domaine_neutre"], d["phrase_concept"], d["phrase_neutre"]))
    return sortie


def octets_extraits(pieces: dict) -> dict:
    a = {cat: pieces["annexe_a"][cat] for cat in CATEGORIES_A}
    b = {c: pieces["annexe_b"][c] for c in CONCEPTS}
    return {
        "remise": (pieces["section5"] + "\n" + pieces["brut_a"] + "\n" + pieces["brut_b"]).encode("utf-8"),
        "annexe_a": json_canonique(a),
        "annexe_b": json_canonique(b),
        "exemples": ("\n".join(pieces["exemples_lignes"]) + "\n").encode("utf-8"),
        "format": (pieces["format_ligne"] + "\n").encode("utf-8"),
        "remise_lecteur": pieces["remise_lecteur"].encode("utf-8"),
    }


def ecart_copie(cle: str, attendu: bytes, lu: bytes) -> str:
    """Différence lisible entre une copie et son bloc (entrées manquantes ou en trop pour les annexes)."""
    if cle in ("annexe_a", "annexe_b"):
        try:
            x, y = json.loads(attendu), json.loads(lu)
        except ValueError:
            return "copie illisible en JSON"

        def aplatir(o, pre=""):
            if isinstance(o, dict):
                return {v for k, w in o.items() for v in aplatir(w, f"{pre}{k}/")}
            if isinstance(o, list):
                return {v for w in o for v in aplatir(w, pre)}
            return {f"{pre}{o}"}
        manque, trop = sorted(aplatir(x) - aplatir(y)), sorted(aplatir(y) - aplatir(x))
        if manque or trop:
            return f"entrées manquantes {manque[:10]}, en trop {trop[:10]}"
    return "octets différents"


# ----------------------------------------------------------------------------------------------------------------------
# Tokeniseur réel et paquet du module (C0, CC-01)
# ----------------------------------------------------------------------------------------------------------------------

def charger_tokeniseur(dossier: Path, journal: Journal):
    dossier = Path(dossier)
    exiger_hors_depot(dossier, "tokeniseur")
    if not dossier.is_dir():
        raise Refus(f"tokeniseur : dossier absent sur disque ({dossier})")
    for nom, attendue in EMPREINTES_TOKENISEUR.items():
        f = dossier / nom
        if not f.is_file():
            raise Refus(f"tokeniseur : {nom} absent sur disque ({f}) : jetons non mesurés")
        h = empreinte(f)
        if h != attendue:
            raise Refus(f"tokeniseur altéré : {nom} sha256 {h} ≠ attendue {attendue}")
        journal.info(f"tokeniseur {nom} : sha256 {h} (= attendue ; révision {REVISION_TOKENISEUR})")
    try:
        import tokenizers
        from tokenizers import Tokenizer
    except ImportError as e:
        raise Refus(f"bibliothèque `tokenizers` absente ({e}) : jetons non mesurés") from None
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    try:
        import transformers
        from transformers import AutoTokenizer
    except ImportError as e:
        raise Refus(f"bibliothèque `transformers` absente ({e}) : gabarit non rejoué (C4)") from None
    try:
        tok = Tokenizer.from_file(str(dossier / "tokenizer.json"))
        tok_hf = AutoTokenizer.from_pretrained(str(dossier), local_files_only=True)
    except Exception as e:  # noqa: BLE001 — tout échec de lecture est un refus, dit
        raise Refus(f"tokeniseur illisible ({type(e).__name__}: {e})") from None
    journal.info(f"bibliothèques : tokenizers {tokenizers.__version__} ; transformers {transformers.__version__} "
                 "(chargement hors ligne : HF_HUB_OFFLINE=1, TRANSFORMERS_OFFLINE=1)")
    return tok, tok_hf


def empreintes_attendues(commit: str, fichier: str | None, journal: Journal) -> dict:
    if fichier:
        try:
            d = json.loads(Path(fichier).read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            raise Refus(f"--empreintes-module illisible ({e})") from None
        if not isinstance(d, dict) or set(d) != set(FICHIERS_MODULE) \
                or not all(isinstance(v, str) and re.fullmatch(r"[0-9a-f]{64}", v) for v in d.values()):
            raise Refus(f"--empreintes-module : un objet {{chemin: sha256}} pour {list(FICHIERS_MODULE)} attendu")
        journal.ecart(f"commit du module {commit} : empreintes lues dans {fichier} (sha256 {empreinte(fichier)}) ; "
                      "la section 2 de la consigne est à relire à ce commit")
        return {k: d[k] for k in FICHIERS_MODULE}
    if len(commit) < 7 or not COMMIT_MODULE_COMPLET.startswith(commit):
        raise Refus(f"commit du module {commit} ≠ {COMMIT_MODULE} : ses empreintes sont à relire et à donner par "
                    "--empreintes-module (section 6)")
    return dict(EMPREINTES_MODULE_8DC1CB09)


def purger_paquet() -> None:
    for nom in [m for m in sys.modules if m == "controle_ia" or m.startswith("controle_ia.")]:
        del sys.modules[nom]


def placer_en_tete(src: Path) -> None:
    """Place l'arbre `--module-src` en tête du chemin d'import (CC-01) ; point d'accroche des essais."""
    sys.path.insert(0, str(src))


def garde_emplacement(src: Path) -> list:
    """CC-01 : chaque module `controle_ia*` chargé, et d'abord ceux qu'emploie le script, a son fichier sous
    `--module-src` ; sinon refus (code 2)."""
    base = Path(src).resolve()
    absents = [m for m in MODULES_EMPLOYES if m not in sys.modules]
    if absents:
        raise Refus(f"C0 — modules employés non chargés : {absents}")
    hors = []
    for nom in sorted(m for m in sys.modules if m == "controle_ia" or m.startswith("controle_ia.")):
        f = getattr(sys.modules[nom], "__file__", None)
        if f is None or base not in Path(f).resolve().parents:
            hors.append(f"{nom} ({f})")
    if hors:
        raise Refus(f"C0 — modules du paquet controle_ia importés hors de --module-src {base} : {hors[:6]}"
                    f"{' …' if len(hors) > 6 else ''} (CC-01 : refus, jamais un repli)")
    return sorted(m for m in sys.modules if m == "controle_ia" or m.startswith("controle_ia."))


def charger_paquet(src: Path, commit: str, fichier_empreintes: str | None, journal: Journal) -> dict:
    src = Path(src)
    exiger_hors_depot(src, "code du module")
    racine = src / "controle_ia"
    if not racine.is_dir():
        raise Refus(f"code du module : {racine} absent sur disque (arbre `src/` de `git archive <commit> src` attendu)")
    attendues = empreintes_attendues(commit, fichier_empreintes, journal)
    for rel, att in attendues.items():
        f = racine / rel
        if not f.is_file():
            raise Refus(f"code du module : {rel} absent sur disque ({f})")
        h = empreinte(f)
        if h != att:
            raise Refus(f"code du module altéré : {rel} sha256 {h} ≠ attendue {att} (commit {commit})")
        journal.info(f"module (commit {commit}) {rel} : sha256 {h} (= attendue)")
    for rel in ("t07/lecture_v2.py", "manifeste.py"):
        f = racine / rel
        if not f.is_file():
            raise Refus(f"code du module : {rel} absent sur disque ({f}) : ce n'est pas l'arbre du module de T0.7")
        h = empreinte(f)
        note = ""
        if rel == "manifeste.py":
            note = " (= celle du commit 8dc1cb09)" if h == EMPREINTE_MANIFESTE_8DC1CB09 else \
                f" (≠ {EMPREINTE_MANIFESTE_8DC1CB09} du commit 8dc1cb09 : écrite)"
        journal.info(f"module {rel} : sha256 {h}{note}")
    sys.dont_write_bytecode = True
    purger_paquet()
    placer_en_tete(src.resolve())
    importlib.invalidate_caches()
    try:
        mods = {nom: importlib.import_module(nom) for nom in MODULES_EMPLOYES}
    except Exception as e:  # noqa: BLE001 — un import impossible est un refus, dit
        raise Refus(f"C0 — import du paquet controle_ia depuis --module-src impossible ({type(e).__name__}: {e})") from None
    charges = garde_emplacement(src)
    for nom, rel in (("controle_ia.t07.sondes_neuves_v1", "t07/sondes_neuves_v1.py"),
                     ("controle_ia.premier_test_ia.empans", "premier_test_ia/empans.py"),
                     ("controle_ia.harnais.formats", "harnais/formats.py"),
                     ("controle_ia.sondes.temoins", "sondes/temoins.py")):
        if Path(mods[nom].__file__).resolve() != (racine / rel).resolve():
            raise Refus(f"C0 — {nom} chargé depuis {mods[nom].__file__}, pas depuis {racine / rel}")
    journal.ok("C0", "emplacement du paquet (CC-01)", f"{len(charges)} modules controle_ia* chargés, tous sous {src.resolve()}")
    for nom in charges:                                    # D-6 : chaque module chargé nommé, avec son empreinte
        f = Path(sys.modules[nom].__file__).resolve()
        journal.info(f"module chargé {nom} : {f.relative_to(src.resolve())} sha256 {empreinte(f)}")
    sn, fm, em = mods["controle_ia.t07.sondes_neuves_v1"], mods["controle_ia.harnais.formats"], \
        mods["controle_ia.premier_test_ia.empans"]
    mod = {"GardeArret": mods["controle_ia.gardes"].GardeArret, "FormatChat": fm.FormatChat, "_ids": fm._ids,
           "jetons_message_utilisateur": em.jetons_message_utilisateur,
           "exiger_concept_sans_affect": mods["controle_ia.sondes.temoins"].exiger_concept_sans_affect,
           "lire_phrases_concepts": sn.lire_phrases_concepts, "FORMATS_LECTURE": tuple(sn.FORMATS_LECTURE),
           "MAX_JETONS_PHRASE": int(sn.MAX_JETONS_PHRASE), "graines": mods["controle_ia.manifeste"].graines,
           "generateur": mods["controle_ia.manifeste"].generateur, "commit": commit, "src": str(src.resolve())}
    journal.info(f"module : FORMATS_LECTURE = {list(mod['FORMATS_LECTURE'])} ; MAX_JETONS_PHRASE = {mod['MAX_JETONS_PHRASE']}")
    return mod


def construire_format(mod: dict, tok_hf):
    """`FormatChat(tok, variables={"date_string": "26 Jul 2024"})` (C4) ; point d'accroche des essais (gabarit falsifié)."""
    return mod["FormatChat"](tok_hf, variables={"date_string": DATE_GABARIT})


def controle_c10(mod: dict, journal: Journal) -> None:
    """C10 : `exiger_concept_sans_affect` sur chacun des noms de la liste fermée ; refus = arrêt et nœud."""
    for c in CONCEPTS:
        try:
            mod["exiger_concept_sans_affect"](c)
        except mod["GardeArret"] as e:
            raise Refus(f"C10 — concept sans affect : {e} (refus, arrêt et nœud)") from None
    journal.ok("C10", "concept sans affect", f"{list(CONCEPTS)} acceptés par exiger_concept_sans_affect "
               f"(commit {mod['commit']})")


# ----------------------------------------------------------------------------------------------------------------------
# Contexte (C0, C10)
# ----------------------------------------------------------------------------------------------------------------------

@dataclass
class Contexte:
    consigne: Path
    sha_consigne: str
    pieces: dict
    tok: object = None
    tok_hf: object = None
    fmt: object = None
    mod: dict | None = None
    exemples: list = field(default_factory=list)
    lex_a: dict = field(default_factory=dict)
    lex_b: dict = field(default_factory=dict)
    format_valeur: str = ""


def verifier_consigne(a, journal: Journal) -> tuple[Path, str, bytes]:
    c = Path(a.consigne)
    if not c.is_file():
        raise Refus(f"consigne absente sur disque ({c})")
    octets = c.read_bytes()
    h = sha_octets(octets)
    scellee = lire_compagnon(c)
    if scellee != h:
        raise Refus(f"consigne : sha256 {h} ≠ son compagnon {scellee}")
    attendue = a.empreinte_consigne or EMPREINTE_CONSIGNE
    if h != attendue:
        raise Refus(f"consigne : sha256 {h} ≠ attendue {attendue}")
    if a.empreinte_consigne:
        journal.ecart(f"empreinte de la consigne donnée par --empreinte-consigne ({h}), autre que celle du script "
                      f"({EMPREINTE_CONSIGNE})")
    journal.info(f"consigne {c} : sha256 {h} (= compagnon, = attendue)")
    return c, h, octets


def charger_contexte(a, journal: Journal, *, extraits: bool) -> Contexte:
    """C0 (entrées, paquet, annexes, exemples, copies si `extraits`) et C10 ; toute faute est un refus (code 2)."""
    consigne, h, octets = verifier_consigne(a, journal)
    tok, tok_hf = charger_tokeniseur(Path(a.tokeniseur), journal)
    mod = charger_paquet(Path(a.module_src), a.commit_module, a.empreintes_module, journal)
    controle_c10(mod, journal)
    pieces = lire_consigne(octets)
    try:
        objet = json.loads(pieces["format_ligne"], object_pairs_hook=_Objet)
    except ValueError as e:
        raise Refus(f"bloc `format-lecture` illisible ({e})") from None
    if not isinstance(objet, _Objet) or [k for k, _ in objet] != ["format_lecture"] \
            or dict(objet)["format_lecture"] not in mod["FORMATS_LECTURE"]:
        raise Refus(f"bloc `format-lecture` : {{\"format_lecture\": {list(mod['FORMATS_LECTURE'])}}} attendu, "
                    f"lu {pieces['format_ligne']!r}")
    comptes = coherence_annexes(pieces)
    ctx = Contexte(consigne, h, pieces, tok, tok_hf, None, mod, format_valeur=dict(objet)["format_lecture"])
    try:
        ctx.fmt = construire_format(mod, tok_hf)
    except mod["GardeArret"] as e:
        raise Refus(f"gabarit de dialogue : {e}") from None
    ctx.lex_a = {cat: [(e, motif_entree(e)) for e in pieces["annexe_a"][cat]] for cat in CATEGORIES_A}
    ctx.lex_b = {c: {p: [("/".join(e), [motif_entree(f) for f in e]) for e in pieces["annexe_b"][c][p]]
                     for p in ("noyau", "champ")} for c in CONCEPTS}
    ctx.exemples = lire_exemples(pieces["exemples_lignes"])
    tampon = Journal("exemples")
    defs = controler_paires(ctx, ctx.exemples, perdant_passe1, tampon, avec_c9=False)[0]
    if defs:
        raise Refus("C0 — exemple(s) en défaut : la consigne est fautive, ou le gabarit, le tokeniseur ou "
                    "l'environnement (arrêt, rapport à la mère ; jamais un renvoi à l'écrivain, jamais un ajustement du "
                    "script) : " + " ; ".join(f"{d['paire']} {d['controle']} ({d['role']}) {d['motif']}" for d in defs))
    for e in ctx.exemples:
        try:
            mod["exiger_concept_sans_affect"](e.concept)
        except mod["GardeArret"] as x:
            raise Refus(f"C0 — exemple {e.nom} : C10 refuse son concept ({x})") from None
    if extraits:
        verifier_copies(ctx, Path(a.dossier), journal)
    journal.ok("C0", "entrées et annexes",
               f"consigne, tokeniseur (3), module (4), bibliothèques ; format {ctx.format_valeur!r} ; annexe A "
               f"{sum(comptes['entrees_a'].values())} entrées {comptes['entrees_a']} ; annexe B formes "
               f"{comptes['formes_b']} ; A ∩ B vide ; lexiques deux à deux disjoints ; entrées de plusieurs mots de B "
               "sans mot de A ni d'un autre concept ; huit exemples conformes à C2-C8 et C10"
               + (" ; copies égales aux blocs" if extraits else ""))
    return ctx


def verifier_copies(ctx: Contexte, dossier: Path, journal: Journal) -> None:
    attendus = octets_extraits(ctx.pieces)
    for cle, nom in NOMS_EXTRAITS.items():
        lu = lire_scelle(dossier / nom, f"copie {nom}")
        if lu != attendus[cle]:
            raise Refus(f"C0 — copie {nom} ≠ bloc de la consigne relu par programme : "
                        f"{ecart_copie(cle, attendus[cle], lu)}")
        journal.info(f"copie {nom} : sha256 {sha_octets(lu)} (= compagnon, = bloc de la consigne)")


# ----------------------------------------------------------------------------------------------------------------------
# Contrôles C2 à C9 (sur une liste de paires)
# ----------------------------------------------------------------------------------------------------------------------

def motifs_c2(t: str, concept: str, role: str) -> list[str]:
    """C2 (CC-07) : alphabet fermé `^[A-Z][A-Za-z ,'-]*\\.$`, ni espace en fin ni double espace ; majuscules."""
    m = []
    if not ALPHABET.fullmatch(t):
        hors = sorted({c for c in t if not CARACTERE_PERMIS.fullmatch(c)})
        if hors:
            m.append("caractère(s) hors de l'alphabet fermé : " + ", ".join(
                repr(c) if 0x21 <= ord(c) <= 0x7E else f"U+{ord(c):04X}" for c in hors))
        if t.startswith(" "):
            m.append("espace en tête")
        elif not t or not "A" <= t[0] <= "Z":
            m.append("premier caractère : majuscule ASCII attendue")
        if t.endswith(" "):
            m.append("espace en fin")
        if not t.endswith("."):
            m.append("ne finit pas par un point")
        if "." in t[:-1]:
            m.append("point ailleurs qu'en dernier caractère (seconde phrase, abréviation, points de suspension)")
        if not m:
            m.append("hors de l'alphabet fermé ^[A-Z][A-Za-z ,'-]*\\.$")
    if "  " in t:
        m.append("double espace")
    if not (role == "phrase_concept" and concept == CONCEPT_NOMS_PROPRES):
        fautifs = [w.group() for w in re.finditer(r"[A-Za-z]+", t)
                   if any(ch.isupper() and w.start() + i > 0 for i, ch in enumerate(w.group()))
                   and w.group() not in MAJUSCULES_PERMISES]
        if fautifs:
            m.append(f"majuscule hors du premier caractère : {fautifs} (admise seulement dans "
                     f"{sorted(MAJUSCULES_PERMISES)}, ou dans une phrase du concept de {CONCEPT_NOMS_PROPRES})")
    return m


def controle_c2(paires) -> list:
    return [defaut(p, "C2", r, x) for p in paires for r in ROLES for x in motifs_c2(getattr(p, r), p.concept, r)]


def controle_c3(ctx: Contexte, paires) -> tuple[list, list, dict]:
    jetons, defs, borne = {}, [], []
    mx = ctx.mod["MAX_JETONS_PHRASE"]
    for p in paires:
        n = {}
        for r in ROLES:
            n[r] = compter_jetons(ctx.tok, getattr(p, r))
            jetons[(p.cle, r)] = n[r]
            if n[r] < JETONS_MIN:
                defs.append(defaut(p, "C3", r, f"{n[r]} jetons < {JETONS_MIN}", jetons=n[r]))
            elif n[r] > JETONS_MAX:
                defs.append(defaut(p, "C3", r, f"{n[r]} jetons > {JETONS_MAX}", jetons=n[r]))
            if n[r] > mx:
                borne.append(defaut(p, "C3-borne", r, f"{n[r]} jetons > {mx} (borne du module : tronquée sans refus)",
                                    jetons=n[r]))
        e = ecart_relatif(n["phrase_concept"], n["phrase_neutre"])
        if e > ECART_MAX:
            defs.append(defaut(p, "C3", "paire", f"écart relatif {float(e):.3f} > 0,15 ({n['phrase_concept']} et "
                               f"{n['phrase_neutre']} jetons)", jetons_concept=n["phrase_concept"],
                               jetons_neutre=n["phrase_neutre"], ecart=round(float(e), 4)))
    return defs, borne, jetons


def controle_c4(ctx: Contexte, paires, jetons: dict) -> list:
    """Gabarit `message_utilisateur` (garde du module) et chemin `phrase_seule` : comptes égaux à ceux de C3."""
    g, defs = ctx.mod["GardeArret"], []
    for p in paires:
        for r in ROLES:
            t, n3 = getattr(p, r), jetons[(p.cle, r)]
            try:
                res = ctx.mod["jetons_message_utilisateur"](ctx.fmt, "", t, ctx.mod["MAX_JETONS_PHRASE"])
            except g as e:
                defs.append(defaut(p, "C4", r, f"gabarit : {e}", jetons_c3=n3))
                continue
            if res["jetons_texte"] != n3:
                defs.append(defaut(p, "C4", r, f"jetons du message utilisateur {res['jetons_texte']} ≠ {n3} (C3)",
                                   jetons_gabarit=res["jetons_texte"], jetons_c3=n3))
            seule = len(ctx.mod["_ids"](ctx.fmt.tok, t.strip()))
            if seule != n3:
                defs.append(defaut(p, "C4", r, f"jetons de la phrase seule {seule} ≠ {n3} (C3)", jetons_seule=seule,
                                   jetons_c3=n3))
    return defs


def controle_c5_c6(ctx: Contexte, paires) -> tuple[list, list]:
    d5, d6 = [], []
    for p in paires:
        for r in ROLES:
            s = p.suites[r]
            adr = [e for e, m in ctx.lex_a[CATEGORIE_ADRESSE] if m in s]
            if adr:
                d5.append(defaut(p, "C5", r, f"adresse ou personne : {adr}", mots=adr))
            trouves = [(cat, e) for cat in CATEGORIES_A if cat != CATEGORIE_ADRESSE for e, m in ctx.lex_a[cat] if m in s]
            if trouves:
                d6.append(defaut(p, "C6", r, "mot(s) interdit(s) : " + ", ".join(f"{e} ({c})" for c, e in trouves),
                                 mots=[{"categorie": c, "mot": e} for c, e in trouves]))
    return d5, d6


def controle_c7(ctx: Contexte, paires) -> list:
    defs = []
    for p in paires:
        sc, sn = p.suites["phrase_concept"], p.suites["phrase_neutre"]
        noyau = [lab for lab, ms in ctx.lex_b[p.concept]["noyau"] if any(m in sc for m in ms)]
        if not noyau:
            defs.append(defaut(p, "C7", "phrase_concept", f"aucun mot du noyau de {p.concept}"))
        autres = [(c, part, lab) for c in CONCEPTS if c != p.concept for part in ("noyau", "champ")
                  for lab, ms in ctx.lex_b[c][part] if any(m in sc for m in ms)]
        if autres:
            defs.append(defaut(p, "C7", "phrase_concept", "mot(s) d'un autre concept : "
                               + ", ".join(f"{lab} ({c} {part})" for c, part, lab in autres),
                               mots=[{"concept": c, "partie": part, "entree": lab} for c, part, lab in autres]))
        tous = [(c, part, lab) for c in CONCEPTS for part in ("noyau", "champ")
                for lab, ms in ctx.lex_b[c][part] if any(m in sn for m in ms)]
        if tous:
            defs.append(defaut(p, "C7", "phrase_neutre", "mot(s) de l'annexe B : "
                               + ", ".join(f"{lab} ({c} {part})" for c, part, lab in tous),
                               mots=[{"concept": c, "partie": part, "entree": lab} for c, part, lab in tous]))
    return defs


def conflits_c8(paires) -> list:
    """Égalité après normalisation ou distance d'édition en mots au plus 1, entre deux phrases quelconques ; rend les
    conflits (pa, ra, pb, rb, distance) dans l'ordre du v1 (pa is pb : les deux phrases d'une même paire)."""
    phr = [(tuple(p.mots[r]), p, r) for p in paires for r in ROLES]
    par_longueur: dict = {}
    for i, (m, _, _) in enumerate(phr):
        par_longueur.setdefault(len(m), []).append(i)
    sortie = []
    for longueur, idx in sorted(par_longueur.items()):
        plus = par_longueur.get(longueur + DISTANCE_DOUBLON, [])
        for x, i in enumerate(idx):
            for j in idx[x + 1:] + plus:
                a, pa, ra = phr[i]
                b, pb, rb = phr[j]
                if au_plus_un(a, b):
                    sortie.append((pa, ra, pb, rb, 0 if a == b else 1))
    return sortie


def defaut_c8_intra(p: Paire, d: int) -> dict:
    return defaut(p, "C8", "paire", f"phrase_concept et phrase_neutre à distance {d} en mots", distance=d)


def defaut_c8_conflit(perd: Paire, rp: str, autre: Paire, ro: str, d: int) -> dict:
    return defaut(perd, "C8", rp, f"à distance {d} en mots de {autre.nom} ({ro})", distance=d,
                  paire_en_conflit=autre.nom, role_en_conflit=ro)


def controle_c8(paires, perdant) -> list:
    """C8 (règle du v1, inchangée) : chaque conflit met en défaut la paire que désigne `perdant`."""
    defs = []
    for pa, ra, pb, rb, d in conflits_c8(paires):
        if pa is pb:
            defs.append(defaut_c8_intra(pa, d))
            continue
        perd = perdant(pa, pb)
        (rp, autre, ro) = (ra, pb, rb) if perd is pa else (rb, pa, ra)
        defs.append(defaut_c8_conflit(perd, rp, autre, ro, d))
    return defs


def c8_second_passage(restantes, fixes=()) -> list:
    """C8 du second passage (section 3, CC-16 ; D-4 de la contre-lecture) entre les paires non retirées (et, au second
    tour, contre les paires gardées des autres concepts) :
    (0) une paire dont les deux phrases sont en conflit est retirée ;
    (a) une paire réécrite en conflit avec une paire non réécrite (ou gardée) est retirée ;
    (b) entre réécrites restantes, par rang croissant (concept, puis indice de remise), une réécrite n'entre que si elle
        n'a aucun conflit avec une réécrite déjà entrée ; sinon elle est retirée (rang le plus élevé) — une paire déjà
        retirée n'entre plus dans la comparaison.
    Un conflit entre deux paires non réécrites est rendu en défaut sur l'une d'elles (le second passage le refuse :
    incohérence entre passes), entre deux paires gardées, refusé."""
    conf = conflits_c8(trier(list(restantes) + list(fixes)))
    defs, retirees = [], set()

    def stable(p: Paire) -> bool:
        return p.fixe or not p.reecrite
    for pa, ra, pb, rb, d in conf:                                            # (0)
        if pa is pb:
            defs.append(defaut_c8_intra(pa, d))
            retirees.add(id(pa))
    voisins: dict = {}
    for pa, ra, pb, rb, d in conf:                                            # (a)
        if pa is pb:
            continue
        if stable(pa) and stable(pb):
            perd = avec_fixes(perdant_passe2)(pa, pb)                       # incohérence, rendue au second passage
        elif id(pa) in retirees or id(pb) in retirees:
            continue                                                          # déjà retirée : n'entre plus
        elif stable(pa) or stable(pb):
            perd = pb if stable(pa) else pa
        else:
            voisins.setdefault(id(pa), []).append((pb, ra, rb, d))
            voisins.setdefault(id(pb), []).append((pa, rb, ra, d))
            continue
        (rp, autre, ro) = (ra, pb, rb) if perd is pa else (rb, pa, ra)
        defs.append(defaut_c8_conflit(perd, rp, autre, ro, d))
        retirees.add(id(perd))
    entrees: set = set()
    for p in trier(p for p in restantes if p.reecrite and not p.fixe and id(p) not in retirees):   # (b)
        conflit = [(q, rp, rq, d) for q, rp, rq, d in voisins.get(id(p), []) if id(q) in entrees]
        if conflit:
            q, rp, rq, d = conflit[0]
            defs.append(defaut_c8_conflit(p, rp, q, rq, d))
            retirees.add(id(p))
        else:
            entrees.add(id(p))
    return defs


def controle_c9(ctx: Contexte, paires) -> list:
    ex = [(f"{e.nom} ({r})", e.mots[r], n_grammes(e.mots[r], SUITE_EXEMPLE)) for e in ctx.exemples for r in ROLES]
    defs = []
    for p in paires:
        for r in ROLES:
            m = p.mots[r]
            g = n_grammes(m, SUITE_EXEMPLE)
            for nom, me, ge in ex:
                if abs(len(m) - len(me)) <= DISTANCE_EXEMPLE:
                    d = distance_edition(m, me)
                    if d <= DISTANCE_EXEMPLE:
                        defs.append(defaut(p, "C9", r, f"à distance {d} en mots de l'exemple {nom}", exemple=nom,
                                           distance=d))
                        continue
                commun = sorted(g & ge)
                if commun:
                    defs.append(defaut(p, "C9", r, f"suite de {SUITE_EXEMPLE} mots commune avec l'exemple {nom} : "
                                       f"« {' '.join(commun[0])} »", exemple=nom, suite=" ".join(commun[0])))
    return defs


def controle_c8_tour(paires, perdant, fixes) -> list:
    """C8 du second tour : entre les paires neuves et contre les paires gardées des autres concepts (fixes) ; une paire
    fixe n'est jamais en défaut (refus d'incohérence sinon)."""
    if not fixes:
        return controle_c8(paires, perdant)
    defs = controle_c8(trier(list(paires) + list(fixes)), avec_fixes(perdant))
    exiger_aucun_defaut_fixe(defs)
    return defs


def controler_paires(ctx: Contexte, paires, perdant, journal: Journal, *, avec_c8: bool = True,
                     avec_c9: bool = True, fixes=()) -> tuple[list, dict]:
    """C2 à C9 dans l'ordre (C8 en dernier) ; chaque contrôle écrit son état ; rend les défauts et les jetons. Second
    tour : `fixes` (paires gardées des autres concepts) n'entrent qu'à C8."""
    paires = list(paires)
    defs = []
    d = controle_c2(paires)
    journal.controle("C2", "caractères et phrase unique (alphabet fermé, majuscules)", d)
    defs += d
    d, borne, jetons = controle_c3(ctx, paires)
    journal.controle("C3", f"longueurs en jetons ({JETONS_MIN} à {JETONS_MAX} ; écart relatif ≤ 0,15)", d)
    journal.controle("C3", f"borne du module ({ctx.mod['MAX_JETONS_PHRASE']} jetons, ligne à part)", borne)
    defs += d + borne
    d = controle_c4(ctx, paires, jetons)
    journal.controle("C4", "gabarit et identité des jetons", d)
    defs += d
    d5, d6 = controle_c5_c6(ctx, paires)
    journal.controle("C5", "adresse et personne (A7)", d5)
    journal.controle("C6", "mots interdits (A1 à A6)", d6)
    defs += d5 + d6
    d = controle_c7(ctx, paires)
    journal.controle("C7", "concept présent ou absent (annexe B)", d)
    defs += d
    if avec_c9:
        d = controle_c9(ctx, paires)
        journal.controle("C9", "exemples non repris", d)
        defs += d
    if avec_c8:
        d = controle_c8_tour(paires, perdant, fixes)
        journal.controle("C8", "doublons et quasi-doublons" + (
            f" (paires neuves, et contre {len(fixes)} paires gardées des autres concepts)" if fixes else ""), d)
        defs += d
    return defs, jetons


# ----------------------------------------------------------------------------------------------------------------------
# C13 — mesures (rapporté, réserves)
# ----------------------------------------------------------------------------------------------------------------------

def _stats(v) -> dict:
    return {"moyenne": round(sum(v) / len(v), 3), "min": min(v), "max": max(v)} if v else {}


def _premier_mot(premiers: dict, n: dict) -> list:
    sortie = []
    for r, o in ((ROLES[0], ROLES[1]), (ROLES[1], ROLES[0])):
        for w, k in premiers[r].items():
            ko = premiers[o].get(w, 0)
            if n[r] and n[o] and Fraction(k, n[r]) > C13_PREMIER_MOT_HAUT and Fraction(ko, n[o]) < C13_PREMIER_MOT_BAS:
                sortie.append((r, w, k, n[r], ko, n[o]))
    return sortie


def nombres_de(mots) -> list:
    return sorted(w for w in mots if w in MOTS_NOMBRE)


def mesures_c13(ctx: Contexte, paires, jetons: dict, journal: Journal, titre: str) -> tuple[dict, list]:
    paires = list(paires)
    mesures, reserves = {}, []
    premiers_tous = {r: Counter() for r in ROLES}
    n_tous = {r: 0 for r in ROLES}
    for c in CONCEPTS:
        pc = [p for p in paires if p.concept == c]
        if not pc:
            continue
        m: dict = {"paires": len(pc)}
        for r in ROLES:
            m[r] = {"jetons": _stats([jetons[(p.cle, r)] for p in pc]), "mots": _stats([len(p.mots[r]) for p in pc])}
        signee = sum((Fraction(jetons[(p.cle, "phrase_concept")] - jetons[(p.cle, "phrase_neutre")],
                               max(jetons[(p.cle, "phrase_concept")], jetons[(p.cle, "phrase_neutre")]) or 1)
                      for p in pc), Fraction(0)) / len(pc)
        m["moyenne_signee"] = round(float(signee), 4)
        compte = Counter(lab for p in pc for lab, ms in ctx.lex_b[c]["noyau"]
                         if any(x in p.suites["phrase_concept"] for x in ms))
        m["noyau_employees"] = len(compte)
        haut, k = compte.most_common(1)[0] if compte else (None, 0)
        part = Fraction(k, len(pc))
        m["noyau_plus_employee"] = {"entree": haut, "phrases": k, "part": round(float(part), 4)}
        m["domaines"] = dict(sorted(Counter(str(p.domaine) for p in pc).items()))
        premiers = {r: Counter(p.mots[r][0] if p.mots[r] else "" for p in pc) for r in ROLES}
        m["premiers_mots"] = {r: dict(premiers[r].most_common(5)) for r in ROLES}
        m["mots_nombre"] = {r: dict(sorted(Counter(w for p in pc for w in nombres_de(p.mots[r])).items())) for r in ROLES}
        differents = [p.nom for p in pc if nombres_de(p.mots["phrase_concept"]) != nombres_de(p.mots["phrase_neutre"])]
        m["paires_nombres_differents"] = len(differents)
        mesures[c] = m
        if abs(signee) > C13_MOYENNE_SIGNEE:
            reserves.append(f"{c} : moyenne signée {float(signee):+.4f} des (jetons du concept − jetons neutres) / max, "
                            "au-delà de ±0,05")
        if len(compte) < C13_ENTREES_MIN:
            reserves.append(f"{c} : {len(compte)} entrée(s) du noyau employée(s), moins de {C13_ENTREES_MIN}")
        if part > C13_PART_MAX:
            reserves.append(f"{c} : l'entrée {haut!r} est dans {k} phrases du concept sur {len(pc)} (plus de 60 %)")
        for r, w, kr, nr, ko, no in _premier_mot(premiers, {r: len(pc) for r in ROLES}):
            reserves.append(f"{c} : le premier mot {w!r} ouvre {kr}/{nr} phrases ({r}) et {ko}/{no} de l'autre rôle")
        if differents:
            reserves.append(f"{c} : {len(differents)} paire(s) sans les mêmes mots de nombre dans ses deux phrases : "
                            f"{differents[:10]}")
        for r in ROLES:
            premiers_tous[r].update(premiers[r])
            n_tous[r] += len(pc)
    for r, w, kr, nr, ko, no in _premier_mot(premiers_tous, n_tous):
        reserves.append(f"tous concepts : le premier mot {w!r} ouvre {kr}/{nr} phrases ({r}) et {ko}/{no} de l'autre rôle")
    journal.ligne(f"C13 — mesures ({titre}) :")
    for c, m in mesures.items():
        journal.ligne(f"    {c} : {json.dumps(m, ensure_ascii=False, sort_keys=True)}")
    if reserves:
        for x in reserves:
            journal.reserve(f"C13 — {x}")
    else:
        journal.ok("C13", "mesures", "aucune réserve")
    return mesures, reserves


# ----------------------------------------------------------------------------------------------------------------------
# C1 — schéma de la remise
# ----------------------------------------------------------------------------------------------------------------------

def lire_remise(chemin: Path, initiale: bool, renvoyees: set | None = None, concepts=CONCEPTS,
                remise: str = REMISE_1) -> tuple[dict, list, list, dict]:
    """Rend (paires utilisables par case, défauts C1 par case, lignes rejetées, informations). Second tour : `concepts`
    (les concepts réécrits) ; une ligne d'un autre concept de la liste fermée est rejetée."""
    chemin = Path(chemin)
    if not chemin.is_file():
        raise Refus(f"remise absente sur disque ({chemin})")
    try:
        texte = chemin.read_bytes().decode("utf-8")
    except UnicodeDecodeError as e:
        raise Refus(f"remise {chemin} illisible en UTF-8 ({e})") from None
    lignes = texte.split("\n")
    if lignes and lignes[-1] == "":
        lignes = lignes[:-1]
    rejets, recs = [], {}
    ordre_autre = 0
    for num, l in enumerate(lignes, 1):
        if not l.strip():
            rejets.append({"ligne": num, "motif": "ligne vide"})
            continue
        try:
            obj = json.loads(l, object_pairs_hook=_Objet)
        except ValueError as e:
            rejets.append({"ligne": num, "motif": f"JSON illisible ({e})", "texte": l[:300]})
            continue
        if not isinstance(obj, _Objet):
            rejets.append({"ligne": num, "motif": "un objet JSON attendu", "texte": l[:300]})
            continue
        cles = [k for k, _ in obj]
        if len(set(cles)) != len(cles):
            rejets.append({"ligne": num, "motif": f"clé répétée ({cles})", "texte": l[:300]})
            continue
        d = dict(obj)
        concept, indice = d.get("concept"), d.get("indice")
        if not isinstance(concept, str) or concept not in CONCEPTS:
            rejets.append({"ligne": num, "motif": f"concept {concept!r} hors de la liste fermée {list(CONCEPTS)}",
                           "texte": l[:300]})
            continue
        if concept not in concepts:
            rejets.append({"ligne": num, "motif": f"concept {concept!r} non réécrit : hors de cette remise (concepts de la "
                           f"remise : {list(concepts)})", "texte": l[:300]})
            continue
        if isinstance(indice, bool) or not isinstance(indice, int):
            rejets.append({"ligne": num, "motif": f"indice {indice!r} : entier non booléen attendu", "texte": l[:300]})
            continue
        if not 1 <= indice <= PAIRES_REMISE:
            rejets.append({"ligne": num, "motif": f"indice {indice} hors de 1..{PAIRES_REMISE}", "texte": l[:300]})
            continue
        if cles != list(CLES_REMISE) and set(cles) == set(CLES_REMISE):
            ordre_autre += 1
        recs.setdefault((concept, indice), []).append((num, d, cles))
    paires, defs = {}, []
    for (c, k), liste in sorted(recs.items(), key=lambda x: ordre_case(x[0])):
        nums = [n for n, _, _ in liste]
        if renvoyees is not None and (c, k) not in renvoyees:
            defs.append(defaut_case(c, k, "C1", f"paire non renvoyée dans la remise des renvois (ligne(s) {nums}) : "
                                    "enregistrement ignoré", non_renvoyee=True, lignes=nums))
            continue
        if len(liste) > 1:
            defs.append(defaut_case(c, k, "C1", f"indice répété (lignes {nums})", lignes=nums))
            continue
        num, d, cles = liste[0]
        if set(cles) != set(CLES_REMISE):
            defs.append(defaut_case(c, k, "C1", f"clés {cles} ≠ {list(CLES_REMISE)} (en trop : "
                                    f"{sorted(set(cles) - set(CLES_REMISE))} ; manquantes : "
                                    f"{sorted(set(CLES_REMISE) - set(cles))})", ligne=num))
        attendu = DOMAINES[(k - 1) % len(DOMAINES)]
        if d.get("domaine_neutre") != attendu:
            defs.append(defaut_case(c, k, "C1", f"domaine_neutre {d.get('domaine_neutre')!r} ≠ {attendu} (rotation de "
                                    "la section 4.2)", ligne=num, attendu=attendu))
        pc, pn = d.get("phrase_concept"), d.get("phrase_neutre")
        if isinstance(pc, str) and isinstance(pn, str):
            paires[(c, k)] = Paire(c, k, d.get("domaine_neutre"), pc, pn, remise=remise)
        else:
            defs.append(defaut_case(c, k, "C1", "phrase_concept et phrase_neutre : chaînes attendues", ligne=num))
    if initiale:
        for c in concepts:
            for k in range(1, PAIRES_REMISE + 1):
                if (c, k) not in recs:
                    defs.append(defaut_case(c, k, "C1", "paire absente de la remise (aucune ligne valide pour ce "
                                            f"concept et cet indice ; lignes rejetées : {len(rejets)})"))
    info = {"lignes": len(lignes), "ordre_des_cles_autre": ordre_autre,
            "par_concept": {c: sum(1 for (cc, _) in recs if cc == c) for c in concepts}}
    return paires, defs, rejets, info


def journal_c1(journal: Journal, titre: str, defs: list, rejets: list, info: dict) -> None:
    journal.info(f"{titre} : {info['lignes']} ligne(s) ; cases par concept {info['par_concept']} ; clés dans un autre "
                 f"ordre (information) : {info['ordre_des_cles_autre']}")
    journal.controle("C1", f"schéma de la remise ({titre})", defs)
    if rejets:
        journal.ligne(f"[DÉFAUT] C1 — lignes rejetées ({titre}) : {len(rejets)}")
        for r in rejets:
            journal.ligne(f"    - ligne {r['ligne']} : {r['motif']}")
    else:
        journal.ok("C1", f"lignes rejetées ({titre})", "aucune")


# ----------------------------------------------------------------------------------------------------------------------
# Mode `verifier` : passes 1 et 2, sélection (section 3)
# ----------------------------------------------------------------------------------------------------------------------

def regrouper(defs: list) -> dict:
    par: dict = {}
    for d in defs:
        par.setdefault((d["concept"], d["indice"]), []).append(
            {"controle": d["controle"], "role": d["role"], "motif": d["motif"], "valeurs": d["valeurs"]})
    return par


@dataclass
class Tour:
    """Premier tour (les quatre concepts, noms `-v1`) ou second tour (réécriture des concepts nommés par le premier
    décompte, noms `-v2`, paires gardées des autres concepts en C8)."""
    numero: int
    concepts: tuple
    fixes: list
    journal_passe: str
    renvois: str
    selection: str
    remise: str
    amont: dict


def tour_1() -> Tour:
    return Tour(1, CONCEPTS, [], JOURNAL_PASSE, RENVOIS, SELECTION, REMISE_1, {})


def lire_json_scelle(chemin: Path, role: str) -> tuple[bytes, object]:
    brut = lire_scelle(chemin, role)
    try:
        return brut, json.loads(brut)
    except ValueError as e:
        raise Refus(f"{role} illisible en JSON ({e})") from None


def decisions_de(decompte: dict, role: str) -> dict:
    concepts = decompte.get("concepts") if isinstance(decompte, dict) else None
    if not isinstance(concepts, dict) or not concepts or any(
            c not in CONCEPTS or not isinstance(s, dict) or not isinstance(s.get("decision"), str)
            for c, s in concepts.items()):
        raise Refus(f"{role} : « concepts » {{concept: {{decision…}}}} attendu")
    return {c: concepts[c]["decision"] for c in CONCEPTS if c in concepts}


def amont_tour2(dossier: Path, h_consigne: str, journal: Journal, essai: bool) -> Tour:
    """Second tour : la sélection du premier tour (code 0), son décompte et sa clé, scellés et liés entre eux ; les
    concepts à réécrire sont ceux que le décompte du premier tour envoie en réécriture ; les paires gardées des autres
    concepts sont leurs paires prises et de réserve, moins les paires retirées par la contre-vérification."""
    b_sel, sel = lire_json_scelle(dossier / SELECTION, f"sélection du premier tour ({SELECTION})")
    if sel.get("consigne", {}).get("sha256") != h_consigne:
        raise Refus(f"{SELECTION} faite sous une autre consigne")
    if sel.get("code_passe2") != 0:
        raise Refus(f"{SELECTION} sortie du second passage en code {sel.get('code_passe2')!r} : pas de second tour")
    b_dc, dc = lire_json_scelle(dossier / DECOMPTE, f"décompte du premier tour ({DECOMPTE})")
    if dc.get("selection") != {"chemin": SELECTION, "sha256": sha_octets(b_sel)}:
        raise Refus(f"{DECOMPTE} ne porte pas sur {SELECTION} (sha256 {sha_octets(b_sel)}) : {dc.get('selection')}")
    b_cle, cle = lire_json_scelle(dossier / CLE_ECHANTILLON, f"clé du premier tour ({CLE_ECHANTILLON})")
    if dc.get("cle") != sha_octets(b_cle):
        raise Refus(f"{DECOMPTE} : clé {dc.get('cle')} ≠ {CLE_ECHANTILLON} sha256 {sha_octets(b_cle)}")
    if cle.get("entropie_imposee") is not False and not essai:
        raise Refus(f"{CLE_ECHANTILLON} : entropie imposée ({cle.get('entropie_imposee')!r}) ; essais seulement (--essai)")
    for f in (dossier / SELECTION_V2, compagnon(dossier / SELECTION_V2)):
        if f.exists():
            raise Refus(f"{f.name} existe : la sélection finale est déjà écrite au premier tour, pas de second tour")
    decisions = decisions_de(dc, DECOMPTE)
    if set(decisions) != set(CONCEPTS):
        raise Refus(f"{DECOMPTE} : décisions attendues pour les quatre concepts, lues pour {sorted(decisions)}")
    reecrits = tuple(c for c in CONCEPTS if decisions[c].startswith(DECISION_REECRITURE))
    q4 = [c for c in CONCEPTS if decisions[c].startswith(DECISION_Q4)]
    acceptes = [c for c in CONCEPTS if decisions[c].startswith(DECISION_ACCEPTE)]
    if q4:
        raise Refus(f"premier décompte : {q4} attend(ent) le second lecteur de Q4, voie non écrite dans ce script : "
                    "rapport à la mère")
    if not reecrits:
        raise Refus(f"{DECOMPTE} : aucun concept à réécrire : pas de second tour")
    if len(reecrits) + len(acceptes) != len(CONCEPTS):
        raise Refus(f"{DECOMPTE} : décisions inconnues {decisions}")
    attente = dc.get("retraits_en_attente", {})
    retraits = {}
    for c in acceptes:
        nc = sorted(it["indice_remise"] for it in dc["concepts"][c].get("items_non_conformes", []))
        lu = sorted(attente.get(c, []))
        if nc != lu:
            raise Refus(f"{DECOMPTE} : {c} : retraits en attente {lu} ≠ paires non conformes {nc}")
        retraits[c] = set(nc)
    fixes = []
    for c in acceptes:
        e = sel["concepts"][c]
        for r in e["pris"] + e["reserve"]:
            if r["indice_remise"] not in retraits[c]:
                fixes.append(Paire(c, r["indice_remise"], r["domaine_neutre"], r["phrase_concept"], r["phrase_neutre"],
                                   r["reecrite"], r["indice_remise"], fixe=True, remise=REMISE_1))
    gardees = {c: sum(1 for p in fixes if p.concept == c) for c in acceptes}
    amont = {"selection_v1": {"chemin": SELECTION, "sha256": sha_octets(b_sel)},
             "decompte_v1": {"chemin": DECOMPTE, "sha256": sha_octets(b_dc)},
             "cle_v1": {"chemin": CLE_ECHANTILLON, "sha256": sha_octets(b_cle)},
             "concepts_reecrits": list(reecrits), "concepts_acceptes_tour1": acceptes,
             "retraits_contre_verification_tour1": {c: sorted(retraits[c]) for c in acceptes},
             "paires_gardees": gardees,
             "remises_tour1": [r.get("sha256") for r in sel.get("remises", [])]}
    journal.info(f"second tour : {SELECTION} sha256 {sha_octets(b_sel)} ; {DECOMPTE} sha256 {sha_octets(b_dc)} ; "
                 f"{CLE_ECHANTILLON} sha256 {sha_octets(b_cle)} (= compagnons, liés)")
    journal.info(f"second tour : concepts réécrits {list(reecrits)} (les paires de leur ancienne remise sortent du jeu) ; "
                 f"concepts acceptés au premier tour {acceptes} ; paires gardées (prises et réserve, moins les retraits "
                 f"de la contre-vérification {amont['retraits_contre_verification_tour1']}) : {gardees}")
    return Tour(2, reecrits, fixes, JOURNAL_PASSE_V2, RENVOIS_V2, SELECTION_REECRITURE, REMISE_2, amont)


def passe1(ctx: Contexte, remise: Path, dossier: Path, journal: Journal, tour: Tour | None = None) -> int:
    tour = tour or tour_1()
    paires, def_c1, rejets, info = lire_remise(remise, initiale=True, concepts=tour.concepts, remise=tour.remise)
    journal_c1(journal, "remise initiale" if tour.numero == 1 else "remise du second tour", def_c1, rejets, info)
    liste = trier(paires.values())
    defs, jetons = controler_paires(ctx, liste, perdant_passe1, journal, fixes=tour.fixes)
    mesures_c13(ctx, liste, jetons, journal, "remise initiale" if tour.numero == 1 else "remise du second tour")
    par = regrouper(def_c1 + defs)
    renvois = []
    for (c, k) in sorted(par, key=ordre_case):
        p = paires.get((c, k))
        renvois.append({"concept": c, "indice": k, "domaine_neutre": DOMAINES[(k - 1) % len(DOMAINES)],
                        "phrase_concept": p.phrase_concept if p else None,
                        "phrase_neutre": p.phrase_neutre if p else None, "motifs": par[(c, k)]})
    objet = {"version": Path(tour.renvois).stem, "script": VERSION, "passe": 1,
             "consigne": {"chemin": str(ctx.consigne), "sha256": ctx.sha_consigne},
             "remise": {"chemin": str(remise), "sha256": empreinte(remise)},
             "renvois": renvois, "lignes_rejetees": rejets}
    if tour.numero == 2:
        objet |= {"tour": 2, "remise_tour": tour.remise, "amont": tour.amont}
    ecrire_neuf(dossier / tour.renvois, json_canonique(objet))
    h = sceller(dossier / tour.renvois)
    journal.info(f"renvois : {len(renvois)} paire(s) ; {len(rejets)} ligne(s) rejetée(s) ; {tour.renvois} sha256 {h}")
    for c in tour.concepts:
        journal.info(f"renvois {c} : {[r['indice'] for r in renvois if r['concept'] == c]}")
    return 0 if not renvois and not rejets else 1


def enregistrement(p: Paire, i: int | None = None, avec_remise: bool = False) -> dict:
    r = {"indice_remise": p.indice, "domaine_neutre": p.domaine, "reecrite": p.reecrite,
         "phrase_concept": p.phrase_concept, "phrase_neutre": p.phrase_neutre}
    if avec_remise:
        r["remise"] = p.remise
    return ({"indice": i} | r) if i is not None else r


def selectionner(valides_par_concept: dict, concepts=CONCEPTS, avec_remise: bool = False) -> dict:
    """Section 3 : dans chaque concept, les paires valides par indice de remise croissant ; les 64 premières, numérotées
    de 1 à n ; plancher 56. `valides_par_concept` : {concept: [Paire…]}."""
    sortie = {}
    for c in concepts:
        valides = sorted(valides_par_concept.get(c, []), key=lambda p: p.indice)
        pris, reserve = valides[:PAIRES_FICHIER], valides[PAIRES_FICHIER:]
        n = len(pris)
        statut = "complet" if n == PAIRES_FICHIER else ("plancher" if n >= PLANCHER else "sous-plancher")
        sortie[c] = {"n": n, "statut": statut, "manque": PAIRES_FICHIER - n, "valides": [p.indice for p in valides],
                     "table_indices": {str(p.indice): i for i, p in enumerate(pris, 1)},
                     "pris": [enregistrement(p, i, avec_remise) for i, p in enumerate(pris, 1)],
                     "reserve": [enregistrement(p, None, avec_remise) for p in reserve]}
    return sortie


def paires_de_selection(concepts: dict) -> list:
    return [Paire(c, r["indice"], r["domaine_neutre"], r["phrase_concept"], r["phrase_neutre"], r["reecrite"],
                  r["indice_remise"], remise=r.get("remise", REMISE_1))
            for c in CONCEPTS if c in concepts for r in concepts[c]["pris"]]


def passe2(ctx: Contexte, remises: list, dossier: Path, journal: Journal, tour: Tour | None = None) -> int:
    tour = tour or tour_1()
    brut = lire_scelle(dossier / tour.renvois, f"renvois du premier passage ({tour.renvois})")
    r1 = json.loads(brut)
    journal.info(f"{tour.renvois} : sha256 {sha_octets(brut)} (= compagnon)")
    if r1.get("passe") != 1 or r1["consigne"]["sha256"] != ctx.sha_consigne:
        raise Refus(f"{tour.renvois} : premier passage sous une autre consigne ({r1['consigne']['sha256']})")
    if tour.numero == 2 and (r1.get("tour") != 2 or r1.get("amont") != tour.amont):
        raise Refus(f"{tour.renvois} : premier passage du second tour sur un autre amont (sélection, décompte ou clé du "
                    "premier tour changés depuis)")
    h0 = empreinte(remises[0])
    if h0 != r1["remise"]["sha256"]:
        raise Refus(f"remise initiale sha256 {h0} ≠ celle du premier passage {r1['remise']['sha256']}")
    renvoyees = {(e["concept"], e["indice"]) for e in r1["renvois"]}
    if renvoyees and len(remises) != 2:
        raise Refus(f"{len(renvoyees)} paire(s) renvoyée(s) : la remise des renvois est exigée (second fichier de "
                    "--remise ; un fichier vide si rien n'est rendu)")
    if not renvoyees and len(remises) == 2:
        raise Refus("aucune paire renvoyée au premier passage : pas de remise des renvois")
    init, _, _, _ = lire_remise(remises[0], initiale=True, concepts=tour.concepts, remise=tour.remise)
    for c in tour.concepts:
        for k in range(1, PAIRES_REMISE + 1):
            if (c, k) not in renvoyees and (c, k) not in init:
                raise Refus(f"incohérence entre passes : {c}/{k} non renvoyée et absente de la remise initiale")
    if len(remises) == 2:
        rw, def_rw, rej_rw, info = lire_remise(remises[1], initiale=False, renvoyees=renvoyees, concepts=tour.concepts,
                                               remise=tour.remise)
        journal_c1(journal, "remise des renvois", def_rw, rej_rw, info)
    else:
        rw, def_rw, rej_rw = {}, [], []
        journal.info("aucune paire renvoyée : pas de remise des renvois")
    hors = [d for d in def_rw if d["valeurs"].get("non_renvoyee")]
    if hors or rej_rw:                                                  # D-2 : refus propre, aucun nom définitif écrit
        raise Refus("D-2 — remise des renvois hors de forme : "
                    + "; ".join([f"ligne {r['ligne']} : {r['motif']}" for r in rej_rw]
                                + [f"{d['paire']} : {d['motif']}" for d in hors])
                    + f" ; aucun nom définitif écrit ({tour.journal_passe.format(p=2)}, {tour.selection} absents) : "
                      "rejouer le second passage sur une remise des renvois corrigée et versionnée (R12)")
    c1_rw = regrouper([d for d in def_rw if not d["valeurs"].get("non_renvoyee")])
    courant, retraits = {}, {}
    for c in tour.concepts:
        for k in range(1, PAIRES_REMISE + 1):
            cle = (c, k)
            if cle not in renvoyees:
                courant[cle] = init[cle]
            elif cle in c1_rw:
                retraits[cle] = list(c1_rw[cle])
            elif cle in rw:
                rw[cle].reecrite = True
                courant[cle] = rw[cle]
            else:
                retraits[cle] = [{"controle": "C1", "role": "paire", "motif": "non rendue", "valeurs": {}}]
    journal.info(f"second passage : {len(renvoyees)} renvoyée(s), {sum(1 for p in courant.values() if p.reecrite)} "
                 f"rendue(s) sans défaut de C1, {len(retraits)} retirée(s) d'abord (non rendues ou en défaut à C1)")

    def retirer(defs: list) -> None:
        exiger_aucun_defaut_fixe(defs)
        for cle, motifs in regrouper(defs).items():
            if not courant[cle].reecrite:
                raise Refus(f"incohérence entre passes : {cle[0]}/{cle[1]}, non renvoyée, en défaut au second passage : "
                            f"{motifs}")
            retraits.setdefault(cle, []).extend(motifs)

    journal.ligne("Second passage — C2 à C7 et C9 sur les paires courantes (non renvoyées et réécrites) :")
    retirer(controler_paires(ctx, trier(courant.values()), perdant_passe2, journal, avec_c8=False)[0])
    restantes = trier(p for cle, p in courant.items() if cle not in retraits)
    d8 = c8_second_passage(restantes, tour.fixes)
    journal.controle("C8", "doublons et quasi-doublons, entre les paires non retirées (CC-16 ; D-4 : une paire déjà "
                     "retirée n'entre plus)" + (f" et contre {len(tour.fixes)} paires gardées des autres concepts"
                                               if tour.fixes else ""), d8)
    retirer(d8)
    journal.ligne(f"Retraits définitifs (second défaut) : {len(retraits)}")
    for (c, k) in sorted(retraits, key=ordre_case):
        journal.ligne(f"    - {c}/{k} : " + " ; ".join(f"{m['controle']} ({m['role']}) {m['motif']}" for m in retraits[(c, k)]))
    valides = {c: [p for cle, p in courant.items() if cle[0] == c and cle not in retraits] for c in tour.concepts}
    sel = selectionner(valides, tour.concepts, avec_remise=tour.numero == 2)
    for c in tour.concepts:
        e = sel[c]
        journal.info(f"sélection {c} : n = {e['n']} ({e['statut']}) ; retirées "
                     f"{sorted(k for (cc, k) in retraits if cc == c)} ; réserve non prise "
                     f"{[r['indice_remise'] for r in e['reserve']]} ; table (indice de remise → indice du fichier) "
                     f"{e['table_indices']}")
        if e["statut"] == "plancher":
            journal.reserve(f"{c} : {e['n']} paires (< {PAIRES_FICHIER}, ≥ {PLANCHER}) : manque de {e['manque']} déclaré")
    sous = [c for c in tour.concepts if sel[c]["statut"] == "sous-plancher"]
    if sous:
        journal.ligne(f"[DÉFAUT] sélection — sous le plancher de {PLANCHER} : {sous} : le lot s'arrête pour ce(s) "
                      "concept(s), la mère est saisie (section 3)")
    sel_paires = paires_de_selection(sel)
    journal.ligne("Contrôle de la sélection (C2 à C9) :")
    defs_sel, jetons_sel = controler_paires(ctx, sel_paires, perdant_passe2, journal, fixes=tour.fixes)
    _, reserves = mesures_c13(ctx, sel_paires, jetons_sel, journal, "sélection")
    code = 0 if not defs_sel and not sous else 1
    objet = {"version": Path(tour.selection).stem, "script": VERSION, "code_passe2": code,
             "consigne": {"chemin": str(ctx.consigne), "sha256": ctx.sha_consigne},
             "remises": [{"role": "initiale" if i == 0 else "renvois", "chemin": str(r), "sha256": empreinte(r)}
                         for i, r in enumerate(remises)],
             "renvois_passe1": {"chemin": str(dossier / tour.renvois), "sha256": sha_octets(brut)},
             "retraits": [{"concept": c, "indice_remise": k, "motifs": retraits[(c, k)]}
                          for (c, k) in sorted(retraits, key=ordre_case)],
             "reserves_c13": reserves, "concepts": sel}
    if tour.numero == 2:
        objet |= {"tour": 2, "remise_tour": tour.remise, "concepts_reecrits": list(tour.concepts), "amont": tour.amont}
    ecrire_neuf(dossier / tour.selection, json_canonique(objet))
    journal.info(f"{tour.selection} : sha256 {sceller(dossier / tour.selection)} ; code du second passage {code}")
    return code


def mode_verifier(a, journal: Journal) -> int:
    dossier = Path(a.dossier)
    if not dossier.is_dir():
        raise Refus(f"dossier absent sur disque ({dossier})")
    remises = [Path(x) for x in (a.remise or [])]
    if a.passe == 1 and len(remises) != 1:
        raise Refus("passe 1 : une seule remise (la remise initiale) attendue")
    if a.passe == 2 and len(remises) not in (1, 2):
        raise Refus("passe 2 : la remise initiale, puis la remise des renvois s'il y a des renvois")
    nom_journal = JOURNAL_PASSE if a.tour == 1 else JOURNAL_PASSE_V2
    sortie = (RENVOIS if a.tour == 1 else RENVOIS_V2) if a.passe == 1 else \
        (SELECTION if a.tour == 1 else SELECTION_REECRITURE)
    journal.chemin = dossier / nom_journal.format(p=a.passe)
    exiger_absents([journal.chemin, dossier / sortie])
    for r in remises:
        if not r.is_file():
            raise Refus(f"remise absente sur disque ({r})")
    ctx = charger_contexte(a, journal, extraits=True)
    tour = tour_1() if a.tour == 1 else amont_tour2(dossier, ctx.sha_consigne, journal, a.essai)
    for i, r in enumerate(remises):
        h = empreinte(r)
        journal.info(f"remise {'initiale' if i == 0 else 'des renvois'}{' du second tour' if a.tour == 2 else ''} {r} : "
                     f"sha256 {h}")
        if a.tour == 2 and h in tour.amont["remises_tour1"]:
            raise Refus(f"remise {r} (sha256 {h}) : c'est une remise du premier tour ; le second tour exige la remise "
                        "versionnée de l'écrivain neuf")
    return passe1(ctx, remises[0], dossier, journal, tour) if a.passe == 1 else \
        passe2(ctx, remises, dossier, journal, tour)


# ----------------------------------------------------------------------------------------------------------------------
# Mode `extraire`
# ----------------------------------------------------------------------------------------------------------------------

def mode_extraire(a, journal: Journal) -> int:
    dossier = Path(a.dossier)
    journal.chemin = dossier / JOURNAL_EXTRACTION
    exiger_absents([dossier / n for n in NOMS_EXTRAITS.values()] + [journal.chemin])
    ctx = charger_contexte(a, journal, extraits=False)
    dossier.mkdir(parents=True, exist_ok=True)
    octs = octets_extraits(ctx.pieces)
    for cle, nom in NOMS_EXTRAITS.items():
        ecrire_neuf(dossier / nom, octs[cle])
        journal.info(f"écrit {nom} : sha256 {sceller(dossier / nom)}")
    verifier_copies(ctx, dossier, journal)
    journal.ok("C0", "copies relues", "égales aux blocs de la consigne et à leurs compagnons")
    return 0


# ----------------------------------------------------------------------------------------------------------------------
# Modes `assembler` (C11, C12 ; CC-05, CC-06) et `rejouer-c12`
# ----------------------------------------------------------------------------------------------------------------------

def controle_c11_selection(sel: dict) -> list:
    """C11 avant la construction : quatre concepts, sélection de la section 3, plancher, indices de 1 à n sans trou."""
    defs = []
    concepts = sel.get("concepts") if isinstance(sel, dict) else None
    if not isinstance(concepts, dict):
        return [defaut_lieu("selection", "C11", "« concepts » absent de la sélection")]
    autres = sorted(set(concepts) - set(CONCEPTS))
    if autres:
        defs.append(defaut_lieu("selection", "C11", f"concepts hors de la liste fermée : {autres}"))
    absents = [c for c in CONCEPTS if c not in concepts]
    if absents:
        defs.append(defaut_lieu("selection", "C11", f"{len(CONCEPTS) - len(absents)} concept(s) seulement ; absents : "
                                f"{absents} (quatre attendus)"))
    for c in CONCEPTS:
        if c not in concepts:
            continue
        e = concepts[c]
        pris, valides = e["pris"], sorted(e["valides"])
        n = len(pris)
        if n < PLANCHER:
            defs.append(defaut_lieu(c, "C11", f"n = {n} < {PLANCHER} (plancher de la section 3)", n=n))
        if n > PAIRES_FICHIER:
            defs.append(defaut_lieu(c, "C11", f"n = {n} > {PAIRES_FICHIER}", n=n))
        if [r["indice"] for r in pris] != list(range(1, n + 1)):
            defs.append(defaut_lieu(c, "C11", f"indices {[r['indice'] for r in pris]} : de 1 à n sans trou attendus"))
        if [r["indice_remise"] for r in pris] != valides[:PAIRES_FICHIER]:
            defs.append(defaut_lieu(c, "C11", "paires prises ≠ les 64 premières valides par indice de remise croissant "
                                    "(section 3)"))
        if not all(isinstance(r.get(x), str) for r in pris for x in ROLES):
            defs.append(defaut_lieu(c, "C11", "phrases manquantes dans la sélection"))
    return defs


def octets_assemblage(ctx: Contexte, sel: dict) -> bytes:
    """Section 2 : première ligne = bloc `format-lecture` ; une ligne par paire, `json.dumps(objet, ensure_ascii=True)`."""
    lignes = [ctx.pieces["format_ligne"]]
    for c in CONCEPTS:
        for r in sel["concepts"][c]["pris"]:
            lignes.append(json.dumps({"concept": c, "indice": r["indice"], "phrase_concept": r["phrase_concept"],
                                      "phrase_neutre": r["phrase_neutre"]}, ensure_ascii=True))
    return ("\n".join(lignes) + "\n").encode("ascii")


def controle_c11_octets(ctx: Contexte, octets: bytes) -> tuple[list, list, dict]:
    """C1 (schéma de la section 2) et C11 sur les octets du fichier : première ligne = bloc à l'octet, clés et ordre,
    sérialisation, ordre des lignes, indices de 1 à n, quatre concepts, plancher. Rend (défauts, paires, n par concept)."""
    defs, paires = [], []

    def dd(lieu, motif, controle="C11"):
        defs.append(defaut_lieu(lieu, controle, motif))
    if any(b > 0x7E or (b < 0x20 and b != 0x0A) for b in octets):
        dd("fichier", "caractère hors de l'ASCII imprimable ou fin de ligne autre que \\n")
    texte = octets.decode("utf-8", errors="replace")
    if not texte.endswith("\n"):
        dd("fichier", "dernière fin de ligne absente")
    lignes = texte.split("\n")[:-1] if texte.endswith("\n") else texte.split("\n")
    if any(not l for l in lignes):
        dd("fichier", "ligne vide")
    if not lignes or lignes[0] != ctx.pieces["format_ligne"]:
        dd("ligne 1", f"première ligne {lignes[0][:120] if lignes else None!r} ≠ bloc `format-lecture` "
           f"{ctx.pieces['format_ligne']!r}")
    if lignes:
        try:
            o = json.loads(lignes[0], object_pairs_hook=_Objet)
            ok = isinstance(o, _Objet) and [k for k, _ in o] == ["format_lecture"] \
                and dict(o)["format_lecture"] in ctx.mod["FORMATS_LECTURE"]
        except ValueError:
            ok = False
        if not ok:
            dd("ligne 1", f"première ligne : {{\"format_lecture\": {list(ctx.mod['FORMATS_LECTURE'])}}} attendu (aucune "
               "autre clé)")
    vus: dict = {c: [] for c in CONCEPTS}
    ordre = []
    for num, l in enumerate(lignes[1:], 2):
        try:
            o = json.loads(l, object_pairs_hook=_Objet)
        except ValueError as e:
            dd(f"ligne {num}", f"JSON illisible ({e})", "C1")
            continue
        if not isinstance(o, _Objet) or [k for k, _ in o] != list(CLES_FICHIER):
            dd(f"ligne {num}", f"clés {[k for k, _ in o] if isinstance(o, _Objet) else None} ≠ {list(CLES_FICHIER)} "
               "dans cet ordre (domaine_neutre ôté)", "C1")
            continue
        d = dict(o)
        c, k = d["concept"], d["indice"]
        if c not in CONCEPTS or isinstance(k, bool) or not isinstance(k, int) \
                or not all(isinstance(d[r], str) for r in ROLES):
            dd(f"ligne {num}", f"concept {c!r} ou indice {k!r} hors domaine, ou phrases non textuelles", "C1")
            continue
        if json.dumps(d, ensure_ascii=True) != l:
            dd(f"ligne {num}", "sérialisation ≠ json.dumps(objet, ensure_ascii=True)")
        vus[c].append(k)
        ordre.append((CONCEPTS.index(c), k))
        paires.append(Paire(c, k, None, d["phrase_concept"], d["phrase_neutre"]))
    if ordre != sorted(ordre):
        dd("fichier", "lignes hors de l'ordre (concepts chats, meteo, sports, geographie ; indice croissant)")
    n = {c: len(v) for c, v in vus.items() if v}
    presents = [c for c in CONCEPTS if vus[c]]
    if len(presents) != len(CONCEPTS):
        dd("fichier", f"{len(presents)} concept(s) seulement : {presents} (quatre attendus)")
    for c in presents:
        if sorted(vus[c]) != list(range(1, len(vus[c]) + 1)):
            dd(c, f"indices de {c} : de 1 à n sans trou ni répétition attendus")
        if not PLANCHER <= len(vus[c]) <= PAIRES_FICHIER:
            dd(c, f"{c} : n = {len(vus[c])} hors de {PLANCHER}..{PAIRES_FICHIER}")
    return defs, paires, n


def controle_c12(ctx: Contexte, chemin: Path, attendus: dict | None) -> list:
    """C12 : `lire_phrases_concepts(chemin, min_concepts=4)` au code du module, puis indices entiers uniques de 1 à n et
    aucune phrase au-delà de la borne du module."""
    defs = []

    def dd(motif):
        defs.append(defaut_lieu("fichier", "C12", motif))
    try:
        r = ctx.mod["lire_phrases_concepts"](Path(chemin), min_concepts=4)
    except ctx.mod["GardeArret"] as e:
        dd(f"le module refuse : {e}")
        return defs
    if r["format_lecture"] != ctx.format_valeur:
        dd(f"format rendu {r['format_lecture']!r} ≠ bloc {ctx.format_valeur!r}")
    if sorted(r["concepts"]) != sorted(CONCEPTS):
        dd(f"concepts rendus {sorted(r['concepts'])} ≠ {sorted(CONCEPTS)}")
    mx = ctx.mod["MAX_JETONS_PHRASE"]
    for c, recs in r["concepts"].items():
        ind = [x["indice"] for x in recs]
        if attendus is not None and len(recs) != attendus.get(c):
            dd(f"{c} : {len(recs)} paires rendues ≠ {attendus.get(c)} attendues")
        if not all(isinstance(k, int) and not isinstance(k, bool) for k in ind) or len(set(ind)) != len(ind) \
                or sorted(ind) != list(range(1, len(ind) + 1)):
            dd(f"{c} : indices {ind[:12]}{'…' if len(ind) > 12 else ''} : entiers uniques de 1 à n attendus "
               "(le module ne le contrôle pas)")
        for x in recs:
            for role in ROLES:
                nj = compter_jetons(ctx.tok, x[role].strip())
                if nj > mx:
                    dd(f"{c}/{x['indice']} ({role}) : {nj} jetons > {mx} (borne du module, tronquée sans refus)")
    return defs


def c12_sur_copie(ctx: Contexte, octets: bytes, attendus: dict | None) -> list:
    """C12 joué sur une copie écrite dans un dossier temporaire hors de `donnees/` (CC-05)."""
    with tempfile.TemporaryDirectory(prefix="c12-concepts-t07-") as d:
        copie = Path(d) / FICHIER_ASSEMBLE
        copie.write_bytes(octets)
        return controle_c12(ctx, copie, attendus)


def garde_assemblage(dossier: Path, nom_sel: str, sel: dict, a, journal: Journal) -> None:
    """D-1 : la sélection nommée est la dernière `selection-v<k>.json` du dossier ; le dernier décompte de chacun des
    quatre concepts est « accepté » ; la sélection est liée aux décomptes du dossier ; aucune paire retirée (second
    passage, contre-vérification) ni aucune paire de l'ancienne remise d'un concept réécrit n'y figure ; aucune clé tirée
    sur une entropie imposée hors essai (D-8). Toute faute est un refus (code 2), avant toute écriture."""
    m = MOTIF_SELECTION.fullmatch(nom_sel)
    if not m:
        raise Refus(f"D-1 — sélection {nom_sel!r} hors de la forme selection-v<k>.json")
    versions = sorted(int(MOTIF_SELECTION.fullmatch(p.name).group(1)) for p in dossier.iterdir()
                      if MOTIF_SELECTION.fullmatch(p.name))
    if int(m.group(1)) != max(versions):
        raise Refus(f"D-1 — {nom_sel} n'est pas la dernière sélection du dossier (versions présentes : "
                    f"{['selection-v%d.json' % v for v in versions]})")
    decomptes = sorted((int(MOTIF_DECOMPTE.fullmatch(p.name).group(1)), p) for p in dossier.iterdir()
                       if MOTIF_DECOMPTE.fullmatch(p.name))
    if not decomptes:
        raise Refus("D-1 — aucun décompte de contre-vérification dans le dossier : la contre-vérification précède "
                    "l'assemblage (section 7)")
    derniere, retirees, reecrits, refs, essai = {}, set(), set(), [], False
    for v, p in decomptes:
        b, dc = lire_json_scelle(p, f"décompte {p.name}")
        refs.append({"chemin": p.name, "sha256": sha_octets(b)})
        nom_cle = CLE_ECHANTILLON if v == 1 else f"cle-echantillon-v{v}.json"
        b_cle, cle = lire_json_scelle(dossier / nom_cle, f"clé {nom_cle}")
        if dc.get("cle") != sha_octets(b_cle):
            raise Refus(f"D-1 — {p.name} : clé {dc.get('cle')} ≠ {nom_cle} sha256 {sha_octets(b_cle)}")
        if cle.get("entropie_imposee") is not False:
            if not a.essai:
                raise Refus(f"D-8 — {nom_cle} tirée sur une entropie imposée : essais seulement (--essai)")
            essai = True
        src = dc.get("selection", {})
        b_s, s = lire_json_scelle(dossier / str(src.get("chemin")), f"sélection du décompte {p.name}")
        if sha_octets(b_s) != src.get("sha256"):
            raise Refus(f"D-1 — {p.name} porte sur {src} ≠ sha256 {sha_octets(b_s)} sur disque")
        remise = f"remise-{v}"
        for r in s.get("retraits", []):
            retirees.add((r["concept"], remise, r["indice_remise"]))
        for c, dec in decisions_de(dc, p.name).items():
            derniere[c] = (p.name, dec)
            if dec.startswith(DECISION_REECRITURE):
                reecrits.add((c, remise))
            for it in dc["concepts"][c].get("items_non_conformes", []):
                retirees.add((c, remise, it["indice_remise"]))
    manque = [c for c in CONCEPTS if c not in derniere]
    non = {c: derniere[c] for c in CONCEPTS if c in derniere and not derniere[c][1].startswith(DECISION_ACCEPTE)}
    if manque or non:
        raise Refus(f"D-1 — dernier décompte non « accepté » : {non}" + (f" ; sans décompte : {manque}" if manque else ""))
    if int(m.group(1)) >= 2 and sel.get("decomptes") != refs:
        raise Refus(f"D-1 — {nom_sel} n'est pas liée aux décomptes du dossier ({sel.get('decomptes')} ≠ {refs})")
    fautives = []
    for c in CONCEPTS:
        for r in sel.get("concepts", {}).get(c, {}).get("pris", []):
            rem = r.get("remise", REMISE_1)
            if (c, rem) in reecrits:
                fautives.append(f"{c}/{r.get('indice')} ({rem} {r.get('indice_remise')}) : ancienne remise d'un concept "
                                "réécrit")
            if (c, rem, r.get("indice_remise")) in retirees:
                fautives.append(f"{c}/{r.get('indice')} ({rem} {r.get('indice_remise')}) : paire retirée")
    if fautives:
        raise Refus(f"D-1 — paire(s) retirée(s) dans {nom_sel} : {fautives[:8]}")
    if essai:
        journal.ecart("D-8 — clé(s) tirée(s) sur une entropie imposée, admises par --essai : essais seulement")
    journal.ok("D-1", "garde de l'assemblage",
               f"{nom_sel} = dernière sélection du dossier ; décomptes {[r['chemin'] for r in refs]} ; dernier décompte "
               f"accepté pour {list(CONCEPTS)} ; {len(retirees)} paire(s) retirée(s) et {sorted(reecrits)} absentes")


def ecrire_final(chemin: Path, octets: bytes) -> None:
    """D-8 : écrit les octets sous un nom temporaire du même dossier, les relit, puis crée le nom final par un lien
    (exclusif) ; le nom final n'apparaît qu'avec des octets relus égaux ; sinon refus, sans nom final."""
    tmp = chemin.with_name(f".{chemin.name}.{os.getpid()}.tmp")
    ecrire_neuf(tmp, octets)
    try:
        relu = tmp.read_bytes()
        if relu != octets:
            raise Refus(f"{tmp.name} relu ≠ octets contrôlés (sha256 {sha_octets(relu)} ≠ {sha_octets(octets)}) ; "
                        f"{chemin.name} non écrit")
        try:
            os.link(tmp, chemin)
        except FileExistsError:
            raise Refus(f"{chemin} existe déjà : R12, jamais réécrit") from None
        except OSError as e:
            raise Refus(f"{chemin.name} : lien impossible ({e}) ; non écrit (aucun repli)") from None
    finally:
        tmp.unlink(missing_ok=True)


def mode_assembler(a, journal: Journal) -> int:
    dossier = Path(a.dossier)
    if not dossier.is_dir():
        raise Refus(f"dossier absent sur disque ({dossier})")
    if not a.selection:
        raise Refus("D-1 — assembler exige une sélection nommée (--selection selection-v<k>.json), la dernière du "
                    "dossier ; aucun défaut")
    nom_sel = a.selection
    chemin = dossier / FICHIER_ASSEMBLE
    journal.chemin = dossier / JOURNAL_ASSEMBLAGE
    exiger_absents([chemin, journal.chemin])
    ctx = charger_contexte(a, journal, extraits=True)
    brut = lire_scelle(dossier / nom_sel, f"sélection ({nom_sel})")
    sel = json.loads(brut)
    journal.info(f"sélection {nom_sel} : sha256 {sha_octets(brut)} (= compagnon)")
    if sel.get("consigne", {}).get("sha256") != ctx.sha_consigne:
        raise Refus(f"sélection faite sous une autre consigne ({sel.get('consigne')})")
    if sel.get("code_passe2") != 0:
        raise Refus(f"sélection sortie du second passage en code {sel.get('code_passe2')!r} : aucun assemblage")
    garde_assemblage(dossier, nom_sel, sel, a, journal)
    pre = controle_c11_selection(sel)
    journal.controle("C11", "sélection (section 3)", pre)
    if pre:
        raise Refus(f"C11 — sélection refusée : {[d['motif'] for d in pre]} ; {FICHIER_ASSEMBLE} non écrit")
    o1, o2 = octets_assemblage(ctx, sel), octets_assemblage(ctx, sel)
    if o1 != o2:
        raise Refus("C11 — deux assemblages des mêmes entrées diffèrent ; rien n'est écrit")
    journal.ok("C11", "deux assemblages en mémoire des mêmes entrées", f"égaux à l'octet (sha256 {sha_octets(o1)})")
    d11, paires, n = controle_c11_octets(ctx, o1)
    journal.controle("C11", "forme des octets construits (C1 de la section 2, C11)", d11)
    journal.ligne("C2 à C9 sur les octets construits :")
    defs = controler_paires(ctx, trier(paires), perdant_passe1, journal)[0]
    controle_c10(ctx.mod, journal)
    d12 = c12_sur_copie(ctx, o1, {c: sel["concepts"][c]["n"] for c in CONCEPTS})
    journal.controle("C12", f"forme par le module sur une copie temporaire (lire_phrases_concepts, min_concepts=4, "
                     f"commit {ctx.mod['commit']})", d12)
    if d11 or defs or d12:
        raise Refus(f"assemblage refusé ({len(d11)} défaut(s) de C1/C11, {len(defs)} de C2 à C9, {len(d12)} de C12) ; "
                    f"{FICHIER_ASSEMBLE} non écrit")
    ecrire_final(chemin, o1)
    relu = chemin.read_bytes()
    if relu != o1:
        raise Refus(f"{FICHIER_ASSEMBLE} relu ≠ octets contrôlés (sha256 {sha_octets(relu)} ≠ {sha_octets(o1)}) ; non scellé")
    journal.info(f"{FICHIER_ASSEMBLE} écrit, relu égal à l'octet, scellé (nom créé par lien d'un fichier temporaire relu, "
                 f"D-8) : sha256 "
                 f"{sceller(chemin)} ; n par concept {n} ; provenance des paires : "
                 f"{ {c: sel.get('provenance', {}).get(c, {}).get('remise', REMISE_1) for c in CONCEPTS} }")
    return 0


def mode_rejouer_c12(a, journal: Journal) -> int:
    dossier = Path(a.dossier)
    if not dossier.is_dir():
        raise Refus(f"dossier absent sur disque ({dossier})")
    if not a.fichier:
        raise Refus("rejouer-c12 : --fichier (fichier assemblé et scellé) attendu")
    fichier = Path(a.fichier)
    journal.chemin = dossier / f"journal-c12-{re.sub(r'[^0-9a-zA-Z]', '', a.commit_module)[:12]}-v1.txt"
    exiger_absents([journal.chemin])
    brut = lire_scelle(fichier, f"fichier assemblé ({fichier})")
    ctx = charger_contexte(a, journal, extraits=True)
    journal.info(f"fichier {fichier} : sha256 {sha_octets(brut)} (= compagnon)")
    d11, _, n = controle_c11_octets(ctx, brut)
    journal.controle("C11", "forme du fichier", d11)
    d12 = controle_c12(ctx, fichier, n)
    journal.controle("C12", f"forme par le module (commit {ctx.mod['commit']})", d12)
    if d11 or d12:
        raise Refus(f"C11/C12 refusés au commit {ctx.mod['commit']} : {[d['motif'] for d in d11 + d12][:6]} (nœud)")
    return 0


# ----------------------------------------------------------------------------------------------------------------------
# Section 7 : `echantillon` et `decompter`
# ----------------------------------------------------------------------------------------------------------------------

def mode_echantillon(a, journal: Journal) -> int:
    dossier = Path(a.dossier)
    if not dossier.is_dir():
        raise Refus(f"dossier absent sur disque ({dossier})")
    t2 = a.tour == 2
    n_ech, n_cle, n_jou = (ECHANTILLON_V2, CLE_ECHANTILLON_V2, JOURNAL_ECHANTILLON_V2) if t2 else \
        (ECHANTILLON, CLE_ECHANTILLON, JOURNAL_ECHANTILLON)
    journal.chemin = dossier / n_jou
    exiger_absents([dossier / n_ech, dossier / n_cle, journal.chemin])
    _, h_consigne, _ = verifier_consigne(a, journal)
    mod = charger_paquet(Path(a.module_src), a.commit_module, a.empreintes_module, journal)
    if t2:
        if a.selection not in (None, SELECTION_REECRITURE):
            raise Refus(f"second tour : l'échantillon se tire sur {SELECTION_REECRITURE}, pas sur {a.selection}")
        tour = amont_tour2(dossier, h_consigne, journal, a.essai)
        nom_sel = SELECTION_REECRITURE
    else:
        tour, nom_sel = None, a.selection or SELECTION
    brut = lire_scelle(dossier / nom_sel, f"sélection ({nom_sel})")
    sel = json.loads(brut)
    journal.info(f"sélection {nom_sel} : sha256 {sha_octets(brut)} (= compagnon)")
    if sel.get("consigne", {}).get("sha256") != h_consigne:
        raise Refus("sélection faite sous une autre consigne")
    if sel.get("code_passe2") != 0:
        raise Refus(f"sélection sortie du second passage en code {sel.get('code_passe2')!r} : aucun échantillon")
    if t2 and (sel.get("tour") != 2 or sel.get("amont") != tour.amont):
        raise Refus(f"{SELECTION_REECRITURE} : second tour sur un autre amont (premier tour changé depuis)")
    concepts = tuple(tour.concepts) if t2 else CONCEPTS
    if a.entropie is not None:
        entropie, imposee = int(a.entropie), True
        journal.ecart("entropie imposée par --entropie : essais seulement ; une contre-vérification réelle tire une "
                      "entropie neuve (SeedSequence().entropy)")
    else:
        entropie, imposee = int(np.random.SeedSequence().entropy), False
    cles = [f"echantillon-{c}" for c in concepts] + ["ordre-echantillon"]
    g = mod["graines"](cles, entropie)
    journal.info(f"entropie {entropie} ({'imposée' if imposee else 'neuve, relevée au tirage'}) ; clés {cles}")
    tirage = []
    for c in concepts:
        pris = sel["concepts"][c]["pris"]
        n = len(pris)
        k = -(-n // 10)
        idx = sorted(int(i) for i in mod["generateur"](g[f"echantillon-{c}"]).choice(n, size=k, replace=False))
        tirage += [(c, pris[i]) for i in idx]
        journal.info(f"{c} : {k} paire(s) tirée(s) sur {n} (⌈n/10⌉)")
    rng = mod["generateur"](g["ordre-echantillon"])
    ordre = [int(i) for i in rng.permutation(len(tirage))]
    places = [int(x) for x in rng.integers(0, 2, size=len(tirage))]
    items, cle_items = [], []
    for num, (j, pl) in enumerate(zip(ordre, places), 1):
        c, r = tirage[j]
        pa, pb = (r["phrase_concept"], r["phrase_neutre"]) if pl == 0 else (r["phrase_neutre"], r["phrase_concept"])
        items.append({"item": num, "phrase_A": pa, "phrase_B": pb})
        cle_items.append({"item": num, "concept": c, "indice": r["indice"], "indice_remise": r["indice_remise"],
                          "place_concept": "A" if pl == 0 else "B"})
    ecrire_neuf(dossier / n_ech, json_canonique({"items": items}))
    cle = {"version": Path(n_cle).stem, "script": VERSION, "entropie": str(entropie), "entropie_imposee": imposee,
           "graines": g, "selection": {"chemin": nom_sel, "sha256": sha_octets(brut)}, "items": cle_items}
    if t2:
        cle |= {"tour": 2, "concepts": list(concepts)}
    ecrire_neuf(dossier / n_cle, json_canonique(cle))
    journal.info(f"{n_ech} : sha256 {sceller(dossier / n_ech)} ; {len(items)} items (ni concept, ni rôle, ni indice)")
    journal.info(f"{n_cle} : sha256 {sceller(dossier / n_cle)} — son empreinte est à consigner par la session mère avant "
                 "que le lecteur commence ; la clé n'est jamais montrée au lecteur")
    return 0


def lire_reponses(objet, ech: dict, nom: str = REPONSES) -> list:
    if not isinstance(objet, dict) or set(objet) != {"items"} or not isinstance(objet["items"], list):
        raise Refus(f"{nom} : un objet {{\"items\": [...]}} attendu")
    phrases = {it["item"]: it for it in ech["items"]}
    vus = {}
    for e in objet["items"]:
        if not isinstance(e, dict) or list(e) != list(CLES_REPONSE):
            raise Refus(f"{nom} : clés {list(CLES_REPONSE)} attendues dans cet ordre")
        i = e["item"]
        if isinstance(i, bool) or not isinstance(i, int) or i not in phrases or i in vus:
            raise Refus(f"{nom} : item {i!r} inconnu ou répété")
        for q in ("Q1_A", "Q1_B"):
            if e[q] not in VALEURS_Q1:
                raise Refus(f"{nom}, item {i} : {q} = {e[q]!r} hors de {list(VALEURS_Q1)}")
        for q in ("Q2", "Q3_A", "Q3_B", "Q4_A", "Q4_B", "Q5_A", "Q5_B"):
            if e[q] not in ("oui", "non"):
                raise Refus(f"{nom}, item {i} : {q} = {e[q]!r} hors de oui / non")
        for x in ("A", "B"):
            cit = e[f"citation_Q4_{x}"]
            if e[f"Q4_{x}"] == "oui":
                if not isinstance(cit, str) or not cit.strip() \
                        or cit.strip().lower() not in phrases[i][f"phrase_{x}"].lower():
                    raise Refus(f"{nom}, item {i} : « oui » à Q4 ({x}) sans citation tirée de la phrase")
            elif cit is not None:
                raise Refus(f"{nom}, item {i} : citation_Q4_{x} nulle attendue pour « non »")
        vus[i] = e
    manque = sorted(set(phrases) - set(vus))
    if manque:
        raise Refus(f"{nom} : items sans réponse : {manque}")
    return [vus[i] for i in sorted(vus)]


def recalculer(sel: dict, concepts, retirees: dict, remise: str) -> dict:
    """Section 7 (CC-15) : les paires non conformes retirées sont remplacées par les paires de réserve valides suivantes ;
    sélection recalculée (section 3, plancher compris), provenance (remise) de chaque paire écrite."""
    valides = {}
    for c in concepts:
        e = sel["concepts"][c]
        valides[c] = [Paire(c, r["indice_remise"], r["domaine_neutre"], r["phrase_concept"], r["phrase_neutre"],
                            r["reecrite"], remise=remise)
                      for r in e["pris"] + e["reserve"] if r["indice_remise"] not in retirees.get(c, set())]
    return selectionner(valides, concepts, avec_remise=True)


def selection_v2(sel: dict, retirees: dict) -> dict:
    """Premier tour (v1, CC-15) : recalcul des quatre concepts depuis la sélection du premier tour."""
    return recalculer(sel, CONCEPTS, retirees, REMISE_1)


def compter(reponses: list, par_item: dict, concepts) -> dict:
    sortie = {c: {"paires": 0, "conformes": 0, "non_conformes": 0, "items_non_conformes": [], "citations_Q4": [],
                  "par_question": {"Q1_concept_faux": 0, "Q1_neutre_faux": 0, "Q2_non": 0, "Q3_oui": 0, "Q4_oui": 0,
                                   "Q5_non": 0}} for c in concepts}
    for e in reponses:
        k = par_item[e["item"]]
        c, pc = k["concept"], k["place_concept"]
        pn = "B" if pc == "A" else "A"
        s = sortie[c]
        s["paires"] += 1
        motifs = []
        if e[f"Q1_{pc}"] != c:
            motifs.append(f"Q1 phrase du concept : {e[f'Q1_{pc}']}")
            s["par_question"]["Q1_concept_faux"] += 1
        if e[f"Q1_{pn}"] != "aucun":
            motifs.append(f"Q1 phrase neutre : {e[f'Q1_{pn}']}")
            s["par_question"]["Q1_neutre_faux"] += 1
        if e["Q2"] != "oui":
            motifs.append("Q2 non")
            s["par_question"]["Q2_non"] += 1
        for x in ("A", "B"):
            if e[f"Q3_{x}"] != "non":
                motifs.append(f"Q3 oui ({x})")
                s["par_question"]["Q3_oui"] += 1
            if e[f"Q4_{x}"] != "non":
                motifs.append(f"Q4 oui ({x})")
                s["par_question"]["Q4_oui"] += 1
                s["citations_Q4"].append({"item": e["item"], "indice": k["indice"], "phrase": x,
                                          "citation": e[f"citation_Q4_{x}"]})
            if e[f"Q5_{x}"] != "oui":
                motifs.append(f"Q5 non ({x})")
                s["par_question"]["Q5_non"] += 1
        if motifs:
            s["non_conformes"] += 1
            s["items_non_conformes"].append({"item": e["item"], "indice": k["indice"],
                                             "indice_remise": k["indice_remise"], "motifs": motifs})
        else:
            s["conformes"] += 1
    return sortie


def mode_decompter(a, journal: Journal) -> int:
    dossier = Path(a.dossier)
    if not dossier.is_dir():
        raise Refus(f"dossier absent sur disque ({dossier})")
    t2 = a.tour == 2
    n_ech, n_cle, n_rep, n_dc, n_jou = \
        (ECHANTILLON_V2, CLE_ECHANTILLON_V2, REPONSES_V2, DECOMPTE_V2, JOURNAL_DECOMPTE_V2) if t2 else \
        (ECHANTILLON, CLE_ECHANTILLON, REPONSES, DECOMPTE, JOURNAL_DECOMPTE)
    journal.chemin = dossier / n_jou
    exiger_absents([dossier / n_dc, dossier / SELECTION_V2, journal.chemin])
    _, h_consigne, _ = verifier_consigne(a, journal)
    tour = amont_tour2(dossier, h_consigne, journal, a.essai) if t2 else None
    b_ech = lire_scelle(dossier / n_ech, f"échantillon ({n_ech})")
    b_cle = lire_scelle(dossier / n_cle, f"clé ({n_cle})")
    b_rep = lire_scelle(dossier / n_rep, f"réponses du lecteur ({n_rep})")
    for nom, b in ((n_ech, b_ech), (n_cle, b_cle), (n_rep, b_rep)):
        journal.info(f"{nom} : sha256 {sha_octets(b)} (= compagnon)")
    ech, cle = json.loads(b_ech), json.loads(b_cle)
    if cle.get("entropie_imposee") is not False:                       # D-8
        if not a.essai:
            raise Refus(f"D-8 — {n_cle} tirée sur une entropie imposée ({cle.get('entropie_imposee')!r}) : une "
                        "contre-vérification réelle tire une entropie neuve ; essais seulement (--essai)")
        journal.ecart(f"D-8 — {n_cle} tirée sur une entropie imposée, admise par --essai : essais seulement")
    b_sel = lire_scelle(dossier / cle["selection"]["chemin"], "sélection de l'échantillon")
    if sha_octets(b_sel) != cle["selection"]["sha256"]:
        raise Refus("sélection ≠ celle de la clé de l'échantillon")
    sel = json.loads(b_sel)
    if sel.get("consigne", {}).get("sha256") != h_consigne:
        raise Refus("sélection faite sous une autre consigne")
    if t2 and (cle["selection"]["chemin"] != SELECTION_REECRITURE or sel.get("amont") != tour.amont):
        raise Refus(f"{n_cle} : second tour sur {cle['selection']['chemin']} ou sur un autre amont ({SELECTION_REECRITURE} "
                    "et premier tour inchangé attendus)")
    try:
        rep = json.loads(b_rep)
    except ValueError as e:
        raise Refus(f"{n_rep} illisible ({e})") from None
    if [it["item"] for it in ech["items"]] != [it["item"] for it in cle["items"]]:
        raise Refus("échantillon et clé : items différents")
    concepts = tuple(tour.concepts) if t2 else CONCEPTS
    if sorted({it["concept"] for it in cle["items"]}, key=CONCEPTS.index) != list(concepts):
        raise Refus(f"{n_cle} : concepts {sorted({it['concept'] for it in cle['items']})} ≠ {list(concepts)}")
    reponses = lire_reponses(rep, ech, n_rep)
    sortie = compter(reponses, {it["item"]: it for it in cle["items"]}, concepts)
    acceptes, retirees, en_attente, arrets = [], {}, [], []
    for c in concepts:
        s = sortie[c]
        if s["non_conformes"] > 1:
            if t2:
                s["decision"] = ("second échec après réécriture : arrêt du lot pour ce concept (rapport à la mère, rien "
                                 "d'assemblé)")
                arrets.append(c)
            else:
                s["decision"] = "réécriture du concept entier par un écrivain neuf (cette règle prime sur celle de Q4)"
        elif s["par_question"]["Q4_oui"]:
            s["decision"] = "second lecteur de Q4 sur toutes les paires sélectionnées du concept"
        elif s["non_conformes"] == 1:
            s["decision"] = "accepté ; la paire non conforme est retirée et remplacée par la réserve (CC-15)"
            retirees[c] = {s["items_non_conformes"][0]["indice_remise"]}
        else:
            s["decision"] = "accepté"
        if s["decision"].startswith(DECISION_ACCEPTE):
            acceptes.append(c)
            journal.ok(f"contre-vérification {c}", "acceptée",
                       f"{s['conformes']}/{s['paires']} conformes, aucun oui à Q4 ; {s['decision']}")
        else:
            if c not in arrets:
                en_attente.append(c)
            journal.ligne(f"[{'ARRÊT' if c in arrets else 'DÉFAUT'}] contre-vérification {c} : {s['conformes']}/"
                          f"{s['paires']} conformes, {s['par_question']['Q4_oui']} oui à Q4 : {s['decision']}")
        for it in s["items_non_conformes"]:
            journal.ligne(f"    - item {it['item']} ({c}/{it['indice']}, remise {it['indice_remise']}) : {it['motifs']}")
    objet = {"version": Path(n_dc).stem, "script": VERSION,
             "echantillon": sha_octets(b_ech), "cle": sha_octets(b_cle), "reponses": sha_octets(b_rep),
             "selection": cle["selection"],
             "regle": "par concept : au plus une paire non conforme dans l'échantillon et aucun « oui » à Q4 ; plus d'une "
                      "paire non conforme prime (réécriture) ; une seule paire non conforme est retirée et remplacée",
             "acceptes": acceptes, "retraits_en_attente": {c: sorted(v) for c, v in retirees.items()},
             "concepts": sortie}
    if t2:
        objet |= {"tour": 2, "regle_second_tour": "un second échec (plus d'une paire non conforme) arrête le lot pour ce "
                  "concept", "arrets": arrets, "amont": tour.amont}
    if cle.get("entropie_imposee") is not False:
        objet["essai"] = True
    ecrire_neuf(dossier / n_dc, json_canonique(objet))
    h_dc = sceller(dossier / n_dc)
    journal.info(f"{n_dc} : sha256 {h_dc} ; acceptés {acceptes}")
    if arrets:
        journal.ligne(f"[ARRÊT] second échec de {arrets} après réécriture : le lot s'arrête pour ce(s) concept(s) ; "
                      f"rapport à la mère ; {SELECTION_V2} non écrit, rien n'est assemblé (code {CODE_ARRET})")
        return CODE_ARRET
    if t2:
        if en_attente:
            journal.info(f"{en_attente} attend(ent) le second lecteur de Q4 (voie non écrite dans ce script) : "
                         f"{SELECTION_V2} non écrit ; rapport à la mère")
            return 1
        b_s1, s1 = lire_json_scelle(dossier / SELECTION, SELECTION)
        b_d1 = lire_scelle(dossier / DECOMPTE, DECOMPTE)
        acceptes1 = tour.amont["concepts_acceptes_tour1"]
        ret1 = {c: set(v) for c, v in tour.amont["retraits_contre_verification_tour1"].items()}
        part1 = recalculer(s1, acceptes1, ret1, REMISE_1)
        part2 = recalculer(sel, concepts, retirees, REMISE_2)
        sel2 = {c: (part1 | part2)[c] for c in CONCEPTS}
        provenance = {c: ({"tour": 1, "remise": REMISE_1, "selection": SELECTION} if c in part1 else
                          {"tour": 2, "remise": REMISE_2, "selection": SELECTION_REECRITURE}) for c in CONCEPTS}
        retraits_cv = {c: sorted(v) for c, v in ret1.items() if v} | {c: sorted(v) for c, v in retirees.items()}
        reserves = list(s1.get("reserves_c13", [])) + list(sel.get("reserves_c13", []))
        sources = {"selection_v1": {"chemin": SELECTION, "sha256": sha_octets(b_s1)},
                   "selection_reecriture": cle["selection"]}
        decomptes = [{"chemin": DECOMPTE, "sha256": sha_octets(b_d1)}, {"chemin": n_dc, "sha256": h_dc}]
    else:
        if not retirees or en_attente:
            if retirees:
                journal.info(f"retraits de la contre-vérification en attente {objet['retraits_en_attente']} : "
                             f"{SELECTION_V2} s'écrit une fois, après le second lecteur ou la réécriture de {en_attente}")
            return 0 if not en_attente else 1
        sel2 = selection_v2(sel, retirees)
        provenance = {c: {"tour": 1, "remise": REMISE_1, "selection": SELECTION} for c in CONCEPTS}
        retraits_cv = {c: sorted(v) for c, v in retirees.items()}
        reserves = sel.get("reserves_c13", [])
        sources = {"selection_v1": cle["selection"]}
        decomptes = [{"chemin": n_dc, "sha256": h_dc}]
    for c in CONCEPTS:
        journal.info(f"{SELECTION_V2} {c} : {provenance[c]['remise']} ; retirée(s) {retraits_cv.get(c, [])} ; n = "
                     f"{sel2[c]['n']} ({sel2[c]['statut']}) ; table (indice de remise → indice du fichier) "
                     f"{sel2[c]['table_indices']}")
    sous = [c for c in CONCEPTS if sel2[c]["statut"] == "sous-plancher"]
    v2 = {"version": "selection-v2", "script": VERSION, "code_passe2": 0 if not sous else 1,
          "consigne": sel["consigne"]} | sources | {
          "decompte": decomptes[-1], "decomptes": decomptes, "retraits_contre_verification": retraits_cv,
          "reserves_c13": reserves, "provenance": provenance, "concepts": sel2}
    if t2:
        v2["concepts_reecrits"] = list(concepts)
    ecrire_neuf(dossier / SELECTION_V2, json_canonique(v2))
    journal.info(f"{SELECTION_V2} : sha256 {sceller(dossier / SELECTION_V2)} (paires entrées non relues : à déclarer "
                 "dans la provenance)")
    if sous:
        journal.ligne(f"[DÉFAUT] {SELECTION_V2} : sous le plancher de {PLANCHER} : {sous}")
        return 1
    return 0


# ----------------------------------------------------------------------------------------------------------------------
# Entrée
# ----------------------------------------------------------------------------------------------------------------------

MODES = {"extraire": mode_extraire, "verifier": mode_verifier, "echantillon": mode_echantillon,
         "decompter": mode_decompter, "assembler": mode_assembler, "rejouer-c12": mode_rejouer_c12}


def analyser(argv) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog=VERSION, description=__doc__.split("\n")[0])
    p.add_argument("mode", choices=sorted(MODES))
    p.add_argument("--consigne", required=True, help="consigne scellée (égale à son compagnon .sha256)")
    p.add_argument("--dossier", required=True, help="dossier du jeu (donnees/t07-concepts-v1/)")
    p.add_argument("--empreinte-consigne", default=None, help="autre empreinte attendue de la consigne (écart déclaré)")
    p.add_argument("--tokeniseur", default=None, help="dossier des trois fichiers du tokeniseur, hors de l'arbre")
    p.add_argument("--module-src", default=None, help="arbre src/ de `git archive <commit> src`, hors de l'arbre")
    p.add_argument("--commit-module", default=COMMIT_MODULE)
    p.add_argument("--empreintes-module", default=None, help="JSON {chemin: sha256} pour un autre commit (écart déclaré)")
    p.add_argument("--passe", type=int, choices=(1, 2), default=None)
    p.add_argument("--remise", nargs="+", default=None, help="remise initiale, puis remise des renvois")
    p.add_argument("--selection", default=None, help=f"nom de la sélection dans le dossier (echantillon : {SELECTION} "
                   f"par défaut ; assembler : exigé, la dernière selection-v<k>.json du dossier, D-1)")
    p.add_argument("--entropie", default=None, help="essais seulement : entropie imposée (écart déclaré)")
    p.add_argument("--tour", type=int, choices=(1, 2), default=1,
                   help="verifier, echantillon, decompter : 2 pour la réécriture d'un concept entier (noms -v2)")
    p.add_argument("--essai", action="store_true",
                   help="essais seulement : admet une clé tirée sur une entropie imposée (D-8 ; écart écrit)")
    p.add_argument("--fichier", default=None, help="rejouer-c12 : fichier assemblé et scellé")
    a = p.parse_args(argv)
    if a.mode in ("extraire", "verifier", "assembler", "rejouer-c12") and (not a.tokeniseur or not a.module_src):
        p.error(f"{a.mode} : --tokeniseur et --module-src sont exigés")
    if a.mode == "echantillon" and not a.module_src:
        p.error("echantillon : --module-src est exigé (graines par controle_ia.manifeste)")
    if a.mode == "verifier" and (a.passe is None or not a.remise):
        p.error("verifier : --passe et --remise sont exigés")
    if a.tour == 2 and a.mode not in ("verifier", "echantillon", "decompter"):
        p.error(f"{a.mode} : --tour 2 n'existe que pour verifier, echantillon et decompter")
    return a


def ecrire_journal(journal: Journal, chemin: Path) -> None:
    ecrire_neuf(chemin, journal.texte().encode("utf-8"))
    sceller(chemin)


def refuser(a, journal: Journal, motif: str) -> int:
    journal.ligne(f"[REFUS] {motif}")
    journal.ligne(f"fin : {maintenant()} (horloge UTC du système) ; code 2")
    print(f"REFUS (code 2) : {motif}", file=sys.stderr)
    dossier = Path(a.dossier)
    if dossier.is_dir():
        base = f"journal-refus-{a.mode}{'-tour2' if getattr(a, 'tour', 1) == 2 else ''}-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
        chemin, k = dossier / f"{base}.txt", 1
        while chemin.exists():
            k += 1
            chemin = dossier / f"{base}-{k}.txt"
        try:
            ecrire_journal(journal, chemin)
            print(f"journal du refus : {chemin}", file=sys.stderr)
        except Exception as e:  # noqa: BLE001 — le refus reste dit sur la sortie d'erreur
            print(f"journal du refus non écrit ({type(e).__name__}: {e})", file=sys.stderr)
    return 2


def main(argv=None) -> int:
    a = analyser(argv)
    journal = Journal(a.mode)
    entete(journal, a)
    try:
        code = MODES[a.mode](a, journal)
    except Refus as e:
        return refuser(a, journal, str(e))
    except Exception as e:  # noqa: BLE001 — toute exception non prévue : refus, code 2, motif écrit (R5)
        return refuser(a, journal, f"exception non prévue : {type(e).__name__}: {e}")
    journal.ligne(f"fin : {maintenant()} (horloge UTC du système) ; code {code}")
    try:
        ecrire_journal(journal, journal.chemin)
    except Exception as e:  # noqa: BLE001
        print(f"REFUS (code 2) : journal non écrit ({type(e).__name__}: {e})", file=sys.stderr)
        return 2
    print(f"{a.mode}{' tour 2' if a.tour == 2 else ''}{' passe ' + str(a.passe) if a.passe else ''} : code {code} ; "
          f"journal {journal.chemin}")
    return code


if __name__ == "__main__":
    sys.exit(main())
