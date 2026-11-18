#!/usr/bin/env python3
"""Lanceur de l'organisme d'idéation sur la conception des organismes discrets — **troisième course de la lignée Carbon, par
lot à 8 192 jetons de pensée**, Opus 5.5 en proposeur et juge internes, **témoins v6** — version 12.

Copie du lanceur v10 (`lancer_course_ideation_organismes_discrets_v10.py`, `c3abd573…`, inchangé, R12, jamais joué) ; ce qui
change, et rien d'autre :
- **décision de la session mère** (R-3241) : la lignée Carbon passe par le mode par lot à 8 192 jetons de pensée, en courses
  jumelles d'Argon ; l'enveloppe est `appel-carbon-v3.sh` (commande Gemini par lot `commande_gemini_lot_v1.py`, `9484dce0…`,
  relais Gemini v4 `relais_gemini_v4.py`, `543e728d…`, port 8792) au lieu de `appel-carbon-v2.sh` (synchrone, 2 048) ;
- **témoins v6** (`temoins-organisme-discrets-v6.json`, `07c80a23…`), conformément à l'addendum v4 (`3c6f9448…`) ;
- délais de l'orchestrateur relevés pour Carbon (`DELAIS_PAR_LIGNEE`) : `--delai-commande-s 3600` (la commande par lot dure au
  plus 3 570 s, l'enveloppe coupe à 3 590 s) et `--delai-session-s 3900` (sessions Claude seulement) ;
- la **commande épinglée** de la lignée Carbon est la commande par lot (`COMMANDE_GEMINI_LOT`, `9484dce0…`), celle que lance
  l'enveloppe v3 (contre-lecture du v12, constat significatif) ;
- série de runs `runs/course-ideation-organismes-discrets-v12/`, sortie `/home/user/sorties-course-ideation-organismes-discrets-v12` ;
  texte de décision du manifeste.
Ligne de GO : une ligne principale **neuve** et seule à porter « organisme d'idéation », « organismes discrets »,
« lignée carbon », écrite par la mère sur les empreintes de ce lanceur et de l'addendum v4.

Usage : `/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_organismes_discrets_v12.py carbon`.

Relais à lancer avant : relais Claude (port 8787) et relais Gemini v4 (`relais_gemini_v4.py --port 8792 --modele gemini-4-carbon
--max-appels 8 --max-lots 4 --journal …`, clé `GEMINI_API_KEY` par son nom ; procédure `docs/procedures/relais-persistants-v1.md`).

Essais : `tests/test_lancer_course_ideation_organismes_discrets_v12.py`.

## Texte du lanceur v10 (inchangé, pour mémoire)

Lanceur de l'organisme d'idéation sur la conception des organismes discrets — **troisième course de la lignée Carbon**
(`gemini-4-carbon`), Opus 5.5 en proposeur et juge internes — version 10.

Mots de Lazar du 18 novembre 2026 : « non il nous faut carbon, regarde pourquoi ca a ete coupé » (session de relance) ;
« oui Carbon partout » et « tu as mon go patout relance tout ce qui a ete bloque » (session mère, GO-2026-11-18-15 et -16).
Les deux courses Carbon du v8 ont été coupées (fermeture du tunnel à 69 s, puis connexion muette coupée à 300 s) ; deux
épreuves réelles (18 novembre, 06:45Z) établissent la cause : avec le budget de pensée par défaut (8 192 jetons), Carbon reste
muet au-delà de la coupure ; avec 1 024, il répond en 4,5 s sans flux et en 46 s en flux.

Copie du lanceur v9 corrigé après sa contre-lecture (`lancer_course_ideation_organismes_discrets_v9.py`, inchangé, R12) ;
ce qui change, et rien d'autre :

- `LIGNEES = ("carbon",)` ; enveloppe `appel-carbon-v2.sh` (budget de pensée 2 048, relais Gemini v3 en flux sur le port 8791),
  commande `commande_argon_v3e.py` (celle du v8), famille de garde « gemini » ; aucun délai relevé (`DELAIS_PAR_LIGNEE` ne
  vise que Kimi : l'enveloppe Carbon coupe à 1 500 s, sous les 1 800 s de l'orchestrateur) ;
- périmètre de la ligne de GO : « organisme d'idéation », « organismes discrets », « lignée carbon » ; pire cas et borne
  11,3 USD (dans le plafond commun de 34 avec GO-2026-11-18-11) ; texte de décision du manifeste propre à Carbon ;
- série de runs `runs/course-ideation-organismes-discrets-v10/`, sortie `/home/user/sorties-course-ideation-organismes-discrets-v10`.
  Le verrou, comme au v9, vit dans le dossier de sortie de ce lanceur : il n'exclut pas une course d'un autre lanceur ;
  l'opérateur ne lance une course qu'après la clôture de la précédente.

Écart déclaré : Argon a pensé avec 8 192 jetons ; Carbon pense ici avec 2 048. Les courses ne sont pas strictement jumelles.

Usage : `/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_organismes_discrets_v10.py carbon`.

Relais à lancer avant : relais Claude (port 8787) et relais Gemini v3 (`relais_gemini_v3.py --port 8791 --modele gemini-4-carbon
--max-appels 24 --journal …`, clé `GEMINI_API_KEY` par son nom).

Essais : `tests/test_lancer_course_ideation_organismes_discrets_v10.py`.

## Texte du lanceur v9 (inchangé, pour mémoire)

Lanceur de l'organisme d'idéation sur la conception des organismes discrets — **lignée Kimi** (`kimi-k3.1-pro`,
Moonshot), Opus 5.5 en proposeur et juge internes — version 9.

Mots de Lazar du 18 novembre 2026, dans la session de relance, verbatim : « oublie pas kimi dans les courses » ; « s'il marche
pas on n'arret pas les curses, on continue sans lui » (de Carbon, coupé deux fois). Le lanceur v8
(`lancer_course_ideation_organismes_discrets_v8.py`, `87fb4fec…`, inchangé, R12) porte les lignées Carbon, Astra et Argon
sous sa ligne de GO ; ce v9 porte **la seule lignée Kimi**, sous une ligne de GO à part, avec sa propre série de runs et sa
propre borne.

Ce qui change par rapport au v8, et rien d'autre :

- `LIGNEES = ("kimi",)` ; la lignée externe Kimi : enveloppe `rapports/organismes-discrets-v1/enveloppes-v1/appel-kimi-v2.sh`,
  commande `docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_kimi_ideation_v1.py` (copie de la commande Astra v1,
  défauts seuls changés), famille de garde de taille « kimi » (formule de la commande Astra, prix 2 / 10) ;
- périmètre de la ligne de GO : « organisme d'idéation », « organismes discrets », « lignée kimi » ;
- pire cas et borne du lanceur : **11,3 USD** (une course 9,2 et une relance au plus, après un arrêt au contrôle, 2,1) ;
- série de runs `runs/course-ideation-organismes-discrets-v9/`, sortie `/home/user/sorties-course-ideation-organismes-discrets-v9` ;
  la garde de cumul ne compte que cette série (les courses du v8 sont sous leur propre ligne) ;
- le verrou garde le nom de celui du v8 mais vit dans le dossier de sortie du v9 : il **n'exclut pas** une course du v8 en
  marche (contre-lecture du v9, constat 1). Ce qui tient : le v8 n'a plus de course à jouer (Carbon a ses deux courses ;
  Astra et Argon ont produit des fiches), et la somme reste bornée par le plafond du relais Claude ; l'opérateur ne lance
  une course qu'après la clôture de la précédente ;
- délais relevés pour Kimi (contre-lecture, constat 2) : enveloppe `appel-kimi-v2.sh` (commande 3 300 s, enveloppe 3 500 s),
  et le lanceur passe à l'orchestrateur `--delai-commande-s 3600` et `--delai-session-s 3900` (lignée Kimi seulement,
  `DELAIS_PAR_LIGNEE`).

Usage, seul et exact (dossier courant = racine du dépôt de travail) :

    /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_organismes_discrets_v9.py kimi

Relais à lancer avant : relais Claude (port 8787, celui des courses du v8) et relais compatible OpenAI vers Moonshot
(`relais_kimi_v4.py --amont https://api.moonshot.ai --variable-cle KIMI_API_KEY --port 8789 --modeles-permis kimi-k3.1-pro
--plafond-usd 5 --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 12 --delai-amont-s 3400 --journal …`).

Essais : `tests/test_lancer_course_ideation_organismes_discrets_v9.py`.

## Texte du lanceur v8 (inchangé, pour mémoire)

Lanceur de l'organisme d'idéation (atelier d'idées, N-065 rôle 2) sur la conception des organismes discrets — **trois
courses jumelles, une par lignée externe** (Carbon, Astra, Argon), Opus 5.5 en proposeur et juge internes — version 8.

Mots de Lazar du 18 novembre 2026 (session de relance) : « relance l'organisme d'idéation sur les organismes discrets » ;
« remplace un claude par gemini carbon et oublie pas astra de gpt » ; « go option A » (composition : proposeurs Opus 5.5,
Carbon, Astra, Argon ; juge interne Opus 5.5 ; juges externes différés Carbon, Astra, Argon) ; « go depenses go recos par
anticipation ». L'orchestrateur épinglé n'admet qu'une lignée externe par course au moteur réel (`verifier_commande_externe_reelle`,
v50-v51) : la composition tient donc en **trois courses**, mêmes pièces, même graine de base, une lignée externe chacune.

Dérivé, au plus près, du lanceur « Regard ou raisons » v1 (`lancer_course_ideation_regard_ou_raisons_v1.py`, `3b2dcb11…`,
inchangé, R12), lui-même dérivé du lanceur « conception propre » v1 (contre-lu « autorisable », R-2623 ; joué, R-2628, R-2698).
Les lanceurs v1 à v7 de cette course (`lancer_course_ideation_organismes_discrets_v1..v7.py`) restent intacts ; le v7 avait
laissé sa sortie hors du dépôt et un juge interne simulé (R-3132) : ce v8 copie la sortie scellée dans le dépôt à la
clôture, et tous les rôles internes sont réels (Opus 5.5 par le relais Claude).

Ce qui change par rapport au lanceur « Regard ou raisons » v1, et rien d'autre :

- l'**argument** est la lignée externe, parmi `carbon`, `astra`, `argon` (au lieu de la génération `1`) ; chaque lignée a sa
  propre série de runs (suffixe du dossier), sa propre relance unique ; une seule course à la fois (verrou commun) ;
- les **pièces** : question v3, faits v3, témoins v1 de `docs/notes/organismes-discrets-v1/organisme-ideation-v1/` ;
  l'enveloppe et la commande externes de la lignée (`rapports/organismes-discrets-v1/enveloppes-v1/`, `commande_argon_v3e.py`
  qui lit le modèle demandé, `commande_astra_v1.py`) ;
- les **rôles** : un seul proposeur interne (Opus 5.5) et un seul juge interne (Opus 5.5) ; proposeur externe et juge externe
  différé de la lignée ; `--modele-commande-externe` et `--commande-externe-lit-modele` passés à l'orchestrateur (CL15-05) ;
  **une seule passe** (pas de `--seconde-passe`) ;
- les **plafonds** (devis v3 de cette course) : total Claude 6 USD par course, total externe 6,5 ; proposeur et juge Opus 2,0
  chacun ; proposeur externe 1,5, juge externe différé 2,5 (déclaré, jamais joué ici), contrôle externe 1,7 ; plafond d'une
  course 9,2 ; pire cas de la ligne **34 USD** (trois lignées × (9,2 + 2,1)) ; borne de ce lanceur 34 USD ;
- la **ligne de GO** : périmètre « organisme d'idéation », « organismes discrets » et « trois lignées » ;
- les gardes de taille de la commande externe suivent la **famille** de la lignée (garde de la commande d'Argon pour Gemini,
  garde de la commande Astra pour OpenAI) ;
- les copies scellées à la clôture ajoutent `classement.json`, `lecture.json` et `manifeste-depart.json` quand ils existent.

Ce qui est gardé, à l'identique : M1 (options `-I -B`, commande d'origine exacte, argument unique, dossier courant,
interpréteur, fichier non lien et d'empreinte égale à son compagnon, avant le verrou et toute écriture) ; M2 (tout ce qui
peut échouer avant le détachement, aucune commande git après, manifeste de pré-départ scellé, code 5 avec PID) ; relevé de
dépense et copies scellées dans le dépôt à la clôture ; **une seule relance par lignée**, seulement après une course finie
proprement, sans fiche, à relevé lisible d'au plus 2,1 USD ; environnement par liste de noms permis ; verrou ; orchestrateur épinglé par
l'arbre de `orchestrator/` et neuf empreintes ; gardes de somme et de taille ; drapeaux interdits ; aucun bras joué ici.

Usage, seul et exact (dossier courant = racine du dépôt de travail), LIGNÉE parmi carbon, astra, argon :

    /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_organismes_discrets_v8.py LIGNÉE

Une invocation fait **une** chose : compte rendu d'une course en marche (code 3) ; orchestrateur orphelin vivant (code 4) ;
clôture d'une course finie (code 0) ; lancement détaché (code 0) ; lancement fait mais manifeste de départ non écrit (code
5, PID imprimé) ; refus (code 2). Arrêt d'une course : `kill -INT <PID du superviseur>` d'abord (relayé par PID, R10 ; fin
propre de l'orchestrateur), `kill -TERM <PID du superviseur>` seulement si elle ne finit pas.

Relais à lancer avant, séparément (`scripts/lancer_relais_local_v1.py`, clés par nom) : relais Claude (`pole/relais_reel.py`
du clone, port 8787, modèles permis = Opus 5.5 seul) ; relais Gemini v2 (port 8788, modèles permis argon et carbon) ; relais
compatible OpenAI (`relais_kimi_v4.py`, amont OpenAI, port 8790, modèle permis gpt-6-astra).

Bibliothèque standard seulement. Essais : `tests/test_lancer_course_ideation_organismes_discrets_v8.py`.
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
import time
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping

VERSION = "lancer_course_ideation_organismes_discrets_v12"
FICHIER_LANCEUR = VERSION + ".py"
DEPOT = Path(__file__).resolve().parents[1]
LIGNEES = ("carbon",)
PYTHON_COURSE = "/usr/local/bin/python3"

# --- ligne de GO, trouvée par son contenu (son identifiant n'existe pas encore) -------------------------------------------
PERIMETRE_GO = ("organisme d'idéation", "organismes discrets", "lignée carbon")
PIRE_CAS_DEVIS_USD = 11.3                        # v9 : une lignée × (course 9,2 + une première tentative en défaut au contrôle 2,1)
BORNE_LIGNE_USD = 11.3                           # v9 : borne de ce lanceur, le pire cas de sa ligne

# --- orchestrateur (dépôt public lciric/ideation-organism, clone en lecture), épinglé par l'arbre de `orchestrator/` -------
ORCHESTRATEUR = Path("/home/user/lciric/ideation-organism/orchestrator")
ARBRE_ORCHESTRATEUR = "ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70"   # même arbre aux commits be6b5af9… et 1168b02…
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

# --- pièces, épinglées ------------------------------------------------------------------------------------------------------
NOTES = "docs/notes/organismes-discrets-v1/organisme-ideation-v1"
ENVELOPPES = "rapports/organismes-discrets-v1/enveloppes-v1"
PIECES_COMMUNES = {
    "question": (f"{NOTES}/question-v3.md",
                 "2f7acf36a1dbdbc53a03a0f775327c773e0152323b04f83b4441db80d6b01dae"),
    "faits": (f"{NOTES}/faits-v3.md",
              "5e2e9dd85a88e9e07da806a3c7657f62c6c6343f11ed6de8a1d507a0b397962f"),
    "temoins": (f"{NOTES}/temoins-organisme-discrets-v6.json",   # v12 : témoins v6 (addendum v4, 3c6f9448…)
                "07c80a23eed67acb8457deefb5ad45135c54683eddc37949a2de60426a838a42"),
}
COMMANDE_GEMINI = ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3e.py",
                   "e94ecd4693657bd2d8b086fbbc903bb77635b3b034e1eede50d630675c3f3fc6")
COMMANDE_ASTRA = ("docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py",
                  "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71")
COMMANDE_GEMINI_LOT = ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py",   # v12
                      "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75")
COMMANDE_KIMI = ("docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_kimi_ideation_v1.py",
                 "5f6c0f275a125e87afe395b5df0a5dd2d171449829031dc88f959436a114f992")
# lignée externe : étiquette, modèle, famille de la garde de la commande, enveloppe et commande épinglées
LIGNEES_EXTERNES = {
    "carbon": {"etiquette": "carbon", "modele": "gemini-4-carbon", "famille": "gemini",
               "enveloppe": (f"{ENVELOPPES}/appel-carbon-v3.sh",   # v12 : par lot, 8 192 (décision R-3241)
                             "9ef03f804bc13a9aebf13b0c03639af59d1d71e2e057190d9a38ecda5b233f32"),
               "commande": COMMANDE_GEMINI_LOT},  # v12 : la commande que l'enveloppe v3 lance
}


def pieces_de(lignee: str) -> dict:
    l = LIGNEES_EXTERNES[lignee]
    return dict(PIECES_COMMUNES, enveloppe_externe=l["enveloppe"], commande_externe=l["commande"])


PIECES = pieces_de("carbon")                     # forme de référence (les essais la parcourent) ; la production prend sa lignée
DEPOT_ATTENDU_PAR_L_ENVELOPPE = Path("/home/user/controle-ia-travail")

# --- plafonds (devis v3 de cette course, gardés par le v9 : par course) -------------------------------------------------------------------
TOTAL_CLAUDE_USD = 6.0                           # total transmis à l'orchestrateur par course (le relais Claude en couvre trois)
TOTAL_EXTERNE_USD = 6.5                          # total transmis (la somme vérifiée par l'orchestrateur compte le juge différé)
NOMBRE = 6
PLAFOND_PROPOSEUR_EXTERNE_USD = 1.5
PLAFOND_JUGE_EXTERNE_USD = 2.5                   # juge différé : déclaré (exigé par le code), jamais joué ici
PLAFONDS_INTERNES = {
    "proposeur_ideation|claude-opus-5-5": 2.0,
    "juge_ideation|claude-opus-5-5": 2.0,
}


def plafonds_de(lignee: str) -> dict:
    m = LIGNEES_EXTERNES[lignee]["modele"]
    return dict(PLAFONDS_INTERNES, **{f"proposeur_ideation|{m}": PLAFOND_PROPOSEUR_EXTERNE_USD,
                                      f"juge_ideation|{m}": PLAFOND_JUGE_EXTERNE_USD})


PLAFONDS = plafonds_de("carbon")
CONTROLE_EXTERNE_USD = 1.7
EXPOSITION_EXTERNE_COURSE_USD = CONTROLE_EXTERNE_USD + PLAFOND_PROPOSEUR_EXTERNE_USD
PLAFOND_COURSE_USD = TOTAL_CLAUDE_USD + EXPOSITION_EXTERNE_COURSE_USD          # 9,2 : compté si la dépense est illisible
MAX_COURSES = 2                                  # une seule relance au total, par lignée
PLAFOND_RELANCE_USD = 2.1                        # une relance seulement après une course arrêtée au contrôle (relevé ≤ 2,1 USD)
PROPOSEURS = (("opus", "claude-opus-5-5"),)
DELAIS_PAR_LIGNEE = {"kimi": ("--delai-commande-s", "3600", "--delai-session-s", "3900"),
                     "carbon": ("--delai-commande-s", "3600", "--delai-session-s", "3900")}
# v12 : --delai-commande-s couvre la commande par lot (3 570 s au plus, enveloppe 3 590 s) ; --delai-session-s ne borne que
# les sessions Claude (gardé égal à celui de Kimi, sans effet sur la commande externe) ; la ligne de Kimi vient du v9 (contre-lecture, constat 2)
DECISION = ("mots de Lazar du 18 novembre 2026 : « non il nous faut carbon » (session de relance), « oui Carbon partout » et "
            "« tu as mon go patout relance tout ce qui a ete bloque » (session mère) ; décision de la mère R-3241 : Carbon par "
            "lot à 8 192 jetons de pensée ; ligne de GO « lignée carbon » trouvée par son contenu ; témoins v6 (addendum v4, "
            "3c6f9448…) ; pire cas et borne 11,3 USD pour la troisième course Carbon")
JUGES = (("opus-juge", "claude-opus-5-5"),)
GRAINE = 2026111808


def externe_de(lignee: str) -> tuple:
    """(proposeur externe, juge externe) de la lignée : (étiquette, modèle)."""
    l = LIGNEES_EXTERNES[lignee]
    return (l["etiquette"], l["modele"]), (l["etiquette"] + "-juge", l["modele"])


# --- gardes de taille de `pole/ideation_v2.py` (arbre épinglé), reproduites par calcul ---------------------------------------
PRIX_CARACTERE_PRUDENT_USD = 10.0 / 1e6 / 4
PROVISION_SORTIE_PAR_FICHE = 12_000
TAILLE_FICHE_PROVISIONNEE_PASSE = 8_000
RAPPORT_SORTIE_ENTREE = 5
CONTROLE_CLAUDE_DEFAUT_USD = 0.2
DEFAUT_EXTERNE_PROPOSEUR_USD = 2.5
DEFAUT_EXTERNE_JUGE_USD = 3.5
DEFAUT_CONTROLE_EXTERNE_USD = 2.5
DEFAUTS_CLAUDE = {"proposeur_ideation|claude-opus-5-5": 5.0, "proposeur_ideation|claude-fable-5-1": 9.3,
                  "juge_ideation|claude-opus-5-5": 4.0, "juge_ideation|claude-fable-5-1": 7.0}
GEMINI_PRIX_ENTREE = 8.3e-6                      # enveloppes argon v6 / carbon v1 (bornes hautes)
GEMINI_PRIX_SORTIE = 41.5e-6
GEMINI_SORTIE_MIN = 4096
GEMINI_PROVISION_PENSEE = 8192
GEMINI_MARGE_ENTREE = 1.05
CARACTERES_PAR_JETON_GARDE = 3.0
ASTRA_PRIX_ENTREE = 10e-6                        # enveloppe astra v1 (prix lu, R-2677 ; cache compté au prix plein)
ASTRA_PRIX_SORTIE = 50e-6
ASTRA_SORTIE_MIN = 4096
ASTRA_OCTETS_PAR_CARACTERE = 1.15                # UTF-8 du français : borne haute
ASTRA_ENROBAGE_OCTETS = 1024
KIMI_PRIX_ENTREE = 2e-6                          # v9 : enveloppe kimi v1 (prix vérifiés le 30 octobre ; cache au prix plein)
KIMI_PRIX_SORTIE = 10e-6
PORT_RELAIS_CLAUDE = 8787

DOSSIER_SORTIES = Path("/home/user/sorties-course-ideation-organismes-discrets-v12")
SOUS_DOSSIER_RUNS = "course-ideation-organismes-discrets-v12"
SUFFIXE_RUN = "-course-ideation-organismes-discrets-v12-"
NOM_VERROU = ".verrou-lanceur-organismes-discrets-v8"  # v9 : verrou du v8, gardé — une seule course à la fois, deux lanceurs confondus
NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")
NOM_DOSSIER_PYCACHE = "pycache"
SUPERVISEUR_DOSSIER = "superviseur-course"
ATTENTE_PID_SUPERVISEUR_PAS = 100                # 100 × 0,05 s : 5 s au plus, seulement si le départ manque
# sorties de l'orchestrateur copiées, octet pour octet et scellées, dans le dossier de run du dépôt à la clôture
COPIES_SORTIE = ("fiches-validees.json", "fiches-refusees.json", "fiches-en-quarantaine.json", "manifeste-fin.json",
                 "manifeste-depart.json", "lecture-course.json", "lecture.json", "classement.json", "notes-par-juge.json",
                 "classements-par-juge.json", "doublons-par-juge.json",
                 "noyau/temoins-servis.json", "noyau/cles-anonymisation-par-juge.json")
COPIES_SUPERVISEUR = ("code.json", "pid-superviseur.json", "pid-orchestrateur.json")

DRAPEAUX_INTERDITS = (
    "--accepter-sans-bac-a-sable", "--motif-sans-bac-a-sable",
    "--tolerer-somme-plafonds", "--tolerer-somme-plafonds-claude", "--tolerer-somme-plafonds-externe",
    "--taille-max-consigne-externe", "--taille-max-consigne-externe-bras", "--prix-entree-usd-par-million-jetons",
    "--bras-rapporte-differe", "--attestation-lecture-humaine",
)
NOMS_DE_CLE = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY", "GOOGLE_API_KEY",
               "GEMINI_API_KEY", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN",
               "KIMI_API_KEY")
MOTIF_NOM_DE_CLE = re.compile(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)
LIGNE_COMPAGNON = re.compile(r"^([0-9a-f]{64})  (\S+)$")

SONDE_BAC_A_SABLE = (
    "import json, sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "from pole.adaptateurs import etat_bac_a_sable_detaille\n"
    "print(json.dumps(etat_bac_a_sable_detaille()))\n"
)

# Superviseur détaché (bibliothèque standard ; `-I -B`, session de processus neuve). M2 : il scelle **d'abord** son propre
# PID et l'heure de départ de son processus, puis lance l'orchestrateur, scelle son PID, relaie SIGTERM, SIGINT et SIGHUP
# **par PID**, attend et scelle le code de sortie.
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
def debut_de(pid):
    try:
        with open("/proc/%d/stat" % pid) as f:
            return f.read().rsplit(")", 1)[-1].split()[19]
    except (OSError, IndexError):
        return None
debut = heure()
sceller("pid-superviseur.json", {"pid_superviseur": os.getpid(), "debut_proc": debut_de(os.getpid()), "debut_utc": debut})
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
    sceller("pid-orchestrateur.json", {"pid_orchestrateur": enfant.pid, "debut_utc": debut, "debut_proc": debut_de(enfant.pid)})
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
    arbre_orchestrateur: str
    empreintes_orchestrateur: dict
    pieces: dict
    registre_go: Path
    dossier_runs: Path
    dossier_sorties: Path
    depot_attendu_par_l_enveloppe: Path
    python: str
    fichier_lanceur: Path                  # M1 : le fichier exécuté (non résolu : un lien symbolique se voit)
    drapeaux: object                       # M1 : `sys.flags` en production
    orig_argv: tuple                       # M1 : `sys.orig_argv` en production
    cwd: str                               # M1 : dossier courant
    lignee: str = "carbon"                 # lignée externe de la course (argument de la commande exacte)
    plafonds: dict = field(default_factory=lambda: dict(PLAFONDS))
    controle_externe_usd: float = CONTROLE_EXTERNE_USD
    arguments_en_plus: tuple = ()          # vide en production ; les essais y glissent des artefacts
    environnement: Mapping | None = None   # None : os.environ (lu par noms, jamais copié en entier)
    aujourd_hui: _dt.date | None = None
    horodatage: object = date_u
    maintenant: object = None              # callable → datetime UTC (essais) ; None : l'horloge
    prefixe_essais: str | None = None      # essais seulement : noms « FAUX_* » du faux orchestrateur ; None en production

    @classmethod
    def production(cls, lignee: str) -> "Reglages":
        if lignee not in LIGNEES:
            raise Refus(f"lignée inconnue : {lignee!r} (parmi {list(LIGNEES)})")
        return cls(depot=DEPOT, orchestrateur=ORCHESTRATEUR, arbre_orchestrateur=ARBRE_ORCHESTRATEUR,
                   empreintes_orchestrateur=dict(EMPREINTES_ORCHESTRATEUR), pieces=pieces_de(lignee),
                   registre_go=DEPOT / "registres" / "go.md", dossier_runs=DEPOT / "runs" / SOUS_DOSSIER_RUNS,
                   dossier_sorties=DOSSIER_SORTIES, depot_attendu_par_l_enveloppe=DEPOT_ATTENDU_PAR_L_ENVELOPPE,
                   python=PYTHON_COURSE, fichier_lanceur=Path(os.path.abspath(__file__)), drapeaux=sys.flags,
                   orig_argv=tuple(getattr(sys, "orig_argv", ())), cwd=os.getcwd(), lignee=lignee,
                   plafonds=plafonds_de(lignee))

    def heure(self) -> _dt.datetime:
        return self.maintenant() if self.maintenant else _dt.datetime.now(_dt.timezone.utc)


# ======================================================================================================================
# M1 : le lanceur se garde lui-même
# ======================================================================================================================

def commande_exacte(r: Reglages) -> tuple:
    return (r.python, "-I", "-B", f"scripts/{FICHIER_LANCEUR}", r.lignee)


def lire_compagnon(chemin: Path) -> str:
    comp = Path(str(chemin) + ".sha256")
    try:
        lignes = [x for x in comp.read_text(encoding="utf-8").splitlines() if x.strip()]
    except (OSError, UnicodeDecodeError):
        raise Refus(f"compagnon d'empreinte absent ou illisible : {comp}") from None
    m = LIGNE_COMPAGNON.match(lignes[0]) if len(lignes) == 1 else None
    if m is None or m.group(2) != chemin.name:
        raise Refus(f"compagnon d'empreinte mal formé : {comp} (une ligne « <empreinte>  {chemin.name} » exigée)")
    return m.group(1)


def verifier_soi(r: Reglages) -> dict:
    """M1 : options `-I -B`, commande d'origine exacte, dossier courant, fichier lancé non lien, à sa place, empreinte égale à
    son compagnon. Avant le verrou et avant toute écriture."""
    if not getattr(r.drapeaux, "isolated", 0):
        raise Refus("option -I absente (sys.flags.isolated) : commande exacte exigée " + " ".join(commande_exacte(r)))
    if not getattr(r.drapeaux, "dont_write_bytecode", 0):
        raise Refus("option -B absente (sys.flags.dont_write_bytecode) : commande exacte exigée "
                    + " ".join(commande_exacte(r)))
    if tuple(r.orig_argv) != commande_exacte(r):
        raise Refus(f"commande d'origine {list(r.orig_argv)} ≠ commande exacte {list(commande_exacte(r))}")
    if os.path.realpath(r.cwd) != os.path.realpath(r.depot):
        raise Refus(f"dossier courant {r.cwd} : la racine du dépôt {r.depot} est exigée")
    f = Path(r.fichier_lanceur)
    if f.is_symlink() or not f.is_file():
        raise Refus(f"fichier du lanceur absent ou lien symbolique : {f}")
    if os.path.realpath(f) != os.path.realpath(r.depot / "scripts" / FICHIER_LANCEUR):
        raise Refus(f"fichier du lanceur {f} hors de sa place ({r.depot / 'scripts' / FICHIER_LANCEUR})")
    lue, attendue = sha256_fichier(f), lire_compagnon(f)
    if lue != attendue:
        raise Refus(f"empreinte du lanceur {lue} ≠ celle de son compagnon {attendue} : fichier modifié, rien lancé")
    return {"version": VERSION, "chemin": str(f), "sha256": lue, "commande": list(r.orig_argv)}


# ======================================================================================================================
# gardes d'entrée
# ======================================================================================================================

def lire_plafond_go(texte: str) -> float:
    m = re.fullmatch(r"\s*(\d+(?:[.,]\d+)?)\s*USD\s*", texte)
    if not m:
        raise Refus(f"plafond du GO illisible : {texte!r} (forme « <nombre> USD » exigée)")
    return float(m.group(1).replace(",", "."))


def _sans_accent(t: str) -> str:
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode("ascii").strip().lower()


def _normal(t: str) -> str:
    return t.replace("’", "'").replace("*", "").lower()


def verifier_go(registre: Path, aujourd_hui: _dt.date) -> dict:
    """Une seule ligne principale dont le périmètre contient les expressions de `PERIMETRE_GO` ; 8 colonnes,
    type calcul, accordée par Lazar, dans sa période, non révoquée, plafond ≥ pire cas du devis."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
    lignes = []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if m:
            lignes.append((m.group(1), [c.strip() for c in ligne.strip().strip("|").split("|")], ligne))
    candidates = [(i, c) for i, c, _ in lignes if len(c) == 8 and all(p in _normal(c[3]) for p in PERIMETRE_GO)
                  and not c[3].lower().startswith("extension")]
    if len(candidates) != 1:
        raise Refus(f"{len(candidates)} ligne(s) principale(s) de GO dont le périmètre contient {list(PERIMETRE_GO)} "
                    f"dans {registre.name} (une exigée)")
    go_id, c = candidates[0]
    for i, cellules, brute in lignes:
        if i != go_id and go_id in brute:
            if len(cellules) != 8:
                raise Refus(f"ligne {i} qui cite {go_id} mal formée ({len(cellules)} colonnes) : lecture impossible")
            if _sans_accent(cellules[2]) == "revocation":
                raise Refus(f"{go_id} révoqué par {i}")
    doublons = [x for x in lignes if x[0] == go_id and not (len(x[1]) == 8 and x[1][3].lower().startswith("extension"))]
    if len(doublons) != 1:
        raise Refus(f"{go_id} : {len(doublons)} lignes principales à cet identifiant (une exigée)")
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
    plafond_usd = lire_plafond_go(plafond)
    if plafond_usd < PIRE_CAS_DEVIS_USD:
        raise Refus(f"{go_id} : plafond {plafond_usd} USD sous le pire cas du devis ({PIRE_CAS_DEVIS_USD} USD)")
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
    """Arbre git du dossier de l'orchestrateur égal à l'épingle ; clone propre (fichiers ignorés compris) ; aucun cache
    d'octets ; empreintes des fichiers de la chaîne de lancement."""
    if not (r.orchestrateur / LANCEUR_ORCHESTRATEUR).is_file():
        raise Refus(f"orchestrateur absent : {r.orchestrateur / LANCEUR_ORCHESTRATEUR}")
    prefixe = _git(r.orchestrateur, "rev-parse", "--show-prefix").strip().rstrip("/")
    arbre = _git(r.orchestrateur, "rev-parse", f"HEAD:{prefixe}").strip()
    if arbre != r.arbre_orchestrateur:
        raise Refus(f"arbre de l'orchestrateur {arbre} (HEAD:{prefixe}), {r.arbre_orchestrateur} exigé")
    tete = _git(r.orchestrateur, "rev-parse", "HEAD").strip()
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
    return {"chemin": str(r.orchestrateur), "racine_clone": str(racine_clone), "commit": tete, "arbre": arbre,
            "empreintes": dict(r.empreintes_orchestrateur)}


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
        raise Refus(f"dépôt de travail en {r.depot}, les enveloppes attendent {r.depot_attendu_par_l_enveloppe}")
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
    if not chemin.is_file() or chemin.is_symlink():
        raise Refus(f"fichier scellé absent ou lien symbolique : {chemin}")
    attendue = lire_compagnon(chemin)
    octets = chemin.read_bytes()
    if hashlib.sha256(octets).hexdigest() != attendue:
        raise Refus(f"sceau faux : {chemin} (empreinte différente de son compagnon)")
    return octets


def lire_json_scelle(chemin: Path):
    try:
        return json.loads(lire_scelle(chemin).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise Refus(f"JSON scellé illisible : {chemin}") from None


def _lire_json_si_scelle(chemin: Path):
    try:
        return lire_json_scelle(chemin)
    except Refus:
        return None


def _scelle_present(chemin: Path) -> bool:
    return chemin.exists() or Path(str(chemin) + ".sha256").exists()


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
        raise Refus(f"drapeau(x) interdit(s) dans la commande : {trouves} (contournement du bac à sable, tolérance de somme, "
                    "relèvement d'une garde de taille ou bras : jamais dans ce lanceur)")


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
    """Les deux sommes, comme l'orchestrateur les calcule avant tout appel, défauts compris."""
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
    controle = _une(argv, "--budget-controle-usd", CONTROLE_CLAUDE_DEFAUT_USD)
    controle_ext = _une(argv, "--budget-controle-externe-usd", DEFAUT_CONTROLE_EXTERNE_USD)
    passe_2 = _une(argv, "--budget-passe-2-externe-usd", None)
    if passes != 1 or passe_2 is not None:
        raise Refus("une seule passe dans cette course : --seconde-passe et --budget-passe-2-externe-usd interdits")
    total_claude = _une(argv, "--budget-total-usd", 40.0)
    total_externe = _une(argv, "--budget-externe-usd", 11.6)
    modeles_claude = sorted(set(prop) | set(juges))
    somme_claude = controle * len(modeles_claude) + passes * sum(budgets[f"proposeur_ideation|{m}"] for m in prop) \
        + sum(budgets[f"juge_ideation|{m}"] for m in juges)
    somme_externe = controle_ext * len(prop_ext) \
        + sum((passe_2 if (n == 2 and passe_2 is not None) else budgets[f"proposeur_ideation|{m}"])
              for m in prop_ext for n in range(1, passes + 1)) \
        + sum(budgets[f"juge_ideation|{m}"] for m in juges_ext) + controle * len(juges_ext)
    exposition = controle_ext * len(prop_ext) + sum(
        (passe_2 if (n == 2 and passe_2 is not None) else budgets[f"proposeur_ideation|{m}"])
        for m in prop_ext for n in range(1, passes + 1))
    return {"somme_claude": round(somme_claude, 6), "total_claude": total_claude,
            "somme_externe": round(somme_externe, 6), "total_externe": total_externe,
            "exposition_externe_course": round(exposition, 6),
            "detail_claude": {"controle": controle, "modeles": modeles_claude, "passes": passes}}


def garde_sommes(argv: list) -> dict:
    s = sommes_plafonds(argv)
    if s["total_externe"] != TOTAL_EXTERNE_USD or s["total_claude"] != TOTAL_CLAUDE_USD:
        raise Refus(f"totaux {s['total_claude']} + {s['total_externe']} ≠ {TOTAL_CLAUDE_USD} + {TOTAL_EXTERNE_USD} du devis")
    if not s["somme_externe"] < s["total_externe"]:
        raise Refus(f"somme des plafonds externes {s['somme_externe']:.2f} pas sous le total externe {s['total_externe']}")
    if s["somme_claude"] > s["total_claude"]:
        raise Refus(f"somme des plafonds Claude {s['somme_claude']:.2f} > total Claude {s['total_claude']}")
    if s["total_claude"] + s["exposition_externe_course"] > PLAFOND_COURSE_USD + 1e-9:
        raise Refus(f"exposition de la course {s['total_claude'] + s['exposition_externe_course']:.2f} > plafond de la "
                    f"course du devis {PLAFOND_COURSE_USD}")
    return s


def taille_max(plafond_usd: float, provision: int = 0, prix: float = PRIX_CARACTERE_PRUDENT_USD) -> int:
    """`taille_max_consigne_par_defaut` de l'orchestrateur, recalculée (aucun import)."""
    return max(0, int(float(plafond_usd) / prix + 1e-6) - int(provision))


def plancher_gemini(caracteres: int, caracteres_par_jeton: float = 4.0) -> float:
    """Plafond de session minimal pour que `commande_argon_v3e.py` (Argon ou Carbon) envoie une consigne de `caracteres`."""
    entree = math.ceil(math.ceil(caracteres / caracteres_par_jeton) * GEMINI_MARGE_ENTREE)
    return entree * GEMINI_PRIX_ENTREE + (GEMINI_SORTIE_MIN + GEMINI_PROVISION_PENSEE) * GEMINI_PRIX_SORTIE


def plancher_astra(caracteres: int) -> float:
    """Plafond de session minimal pour que `commande_astra_v1.py` envoie une consigne de `caracteres` : pire cas de la
    commande, (octets du corps + 1024) × prix d'entrée + sortie minimale × prix de sortie, octets bornés par caractère."""
    octets = math.ceil(caracteres * ASTRA_OCTETS_PAR_CARACTERE) + ASTRA_ENROBAGE_OCTETS
    return octets * ASTRA_PRIX_ENTREE + ASTRA_SORTIE_MIN * ASTRA_PRIX_SORTIE


def plancher_kimi(caracteres: int) -> float:
    """v9 : plafond de session minimal pour que `commande_kimi_ideation_v1.py` (formule de la commande Astra v1) envoie une
    consigne de `caracteres`, aux prix de Kimi."""
    octets = math.ceil(caracteres * ASTRA_OCTETS_PAR_CARACTERE) + ASTRA_ENROBAGE_OCTETS
    return octets * KIMI_PRIX_ENTREE + ASTRA_SORTIE_MIN * KIMI_PRIX_SORTIE


def plancher_externe(famille: str, caracteres: int) -> dict:
    if famille == "gemini":
        return {"plancher_garde_a_3_caracteres_par_jeton": round(plancher_gemini(caracteres, CARACTERES_PAR_JETON_GARDE), 6),
                "plancher_a_4_caracteres_par_jeton_rapporte": round(plancher_gemini(caracteres, 4.0), 6)}
    if famille == "openai":
        return {"plancher_garde_a_3_caracteres_par_jeton": round(plancher_astra(caracteres), 6),
                "plancher_a_4_caracteres_par_jeton_rapporte": round(plancher_astra(caracteres), 6)}
    if famille == "kimi":
        return {"plancher_garde_a_3_caracteres_par_jeton": round(plancher_kimi(caracteres), 6),
                "plancher_a_4_caracteres_par_jeton_rapporte": round(plancher_kimi(caracteres), 6)}
    raise Refus(f"famille de commande externe inconnue : {famille!r}")


def gardes_de_taille(mesure: dict, r: Reglages) -> dict:
    """Sur la mesure de l'orchestrateur (`--mesurer-consignes`, sans appel) : gardes de l'orchestrateur (course, passe 1),
    garde avant envoi de la commande externe de la lignée (contrôle, passe 1). Refus si une garde ne tient pas."""
    l = LIGNEES_EXTERNES[r.lignee]
    try:
        c = mesure["consignes"]
        controle, passe_1 = int(c["consigne_de_controle_externe"]), int(c["consigne_passe_1"])
        nombre = int(c["nombre_par_proposeur"])
        course_orch = bool(mesure["garde_course"]["passerait"])
        passe_1_orch = bool(mesure["gardes_passes_externes"][l["etiquette"]]["passe_1"]["passerait"])
    except (KeyError, TypeError, ValueError):
        raise Refus("mesure des consignes illisible : tailles ou gardes absentes") from None
    if mesure.get("prix_entree_usd_par_million_jetons") != 10.0 or nombre != NOMBRE:
        raise Refus("mesure des consignes à un autre prix que le prix prudent (10) ou à un autre --nombre")
    p1, ctrl = r.plafonds[f"proposeur_ideation|{l['modele']}"], r.controle_externe_usd
    prov_course = nombre * PROVISION_SORTIE_PAR_FICHE * RAPPORT_SORTIE_ENTREE
    prov_passe = nombre * TAILLE_FICHE_PROVISIONNEE_PASSE * RAPPORT_SORTIE_ENTREE
    g = {
        "course": {"taille_max": min(taille_max(ctrl), taille_max(p1, prov_course)), "consigne": controle,
                   "orchestrateur_passerait": course_orch},
        "passe_1": {"taille_max": taille_max(p1, prov_passe), "consigne": passe_1, "orchestrateur_passerait": passe_1_orch},
    }
    for v in g.values():
        v["marge"] = v["taille_max"] - v["consigne"]
    externe = {
        "controle_externe": {"plafond": ctrl, "consigne": controle},
        "passe_1": {"plafond": p1, "consigne": passe_1},
    }
    for v in externe.values():
        v.update(plancher_externe(l["famille"], v["consigne"]))
        v["tient"] = v["plafond"] >= v["plancher_garde_a_3_caracteres_par_jeton"]
    g["commande_externe"] = {"famille": l["famille"], "modele": l["modele"], **externe}
    trop = {k: v for k, v in g.items() if k != "commande_externe" and (v["marge"] < 0 or v.get("orchestrateur_passerait") is False)}
    trop.update({f"commande_externe/{k}": v for k, v in externe.items() if not v["tient"]})
    if trop:
        raise Refus("garde(s) de taille qui ne tiendrai(en)t pas — refus avant tout appel : " + json.dumps(trop, ensure_ascii=False))
    return g


def environnement_permis(env: Mapping, go_id: str, prefixe_pycache: Path | None = None, home: Path | None = None,
                         prefixe_essais: str | None = None) -> tuple:
    """(environnement transmis, description). Liste de noms permis ; HOME, GO_ID et PYTHONPYCACHEPREFIX fixés par le
    lanceur ; tout autre nom est exclu, valeur jamais lue. m5 : les noms exclus ne sont ni listés ni écrits ; seuls leur
    nombre et l'empreinte de leur liste triée le sont."""
    for n in NOMS_PERMIS:
        if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n) or n.startswith(("ANTHROPIC", "CLAUDE", "CCR")):
            raise Refus(f"nom permis interdit : {n}")
    if prefixe_essais is not None and prefixe_essais != "FAUX_":
        raise Refus(f"préfixe d'essai interdit : {prefixe_essais!r}")
    garde = {n: env[n] for n in env if n in NOMS_PERMIS or (prefixe_essais and n.startswith(prefixe_essais))}
    exclus = sorted(n for n in env if n not in garde)
    garde["GO_ID"] = go_id
    if home is not None:
        garde["HOME"] = str(home)
    if prefixe_pycache is not None:
        garde["PYTHONPYCACHEPREFIX"] = str(prefixe_pycache)
    return garde, {"noms_transmis": sorted(garde), "noms_fixes_par_le_lanceur": sorted(
        n for n in ("GO_ID", "HOME", "PYTHONPYCACHEPREFIX") if n in garde),
        "noms_exclus": {"nombre": len(exclus), "sha256_liste_triee": hashlib.sha256("\n".join(exclus).encode()).hexdigest()},
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


def _depot_git(r: Reglages) -> dict:
    """État git du dépôt de travail, **avant** le détachement seulement (M2)."""
    try:
        return {"commit": _git(r.depot, "rev-parse", "HEAD").strip(),
                "arbre_modifie": bool(_git(r.depot, "status", "--porcelain", "--untracked-files=no").strip())}
    except (Refus, OSError, subprocess.SubprocessError) as e:
        return {"commit": None, "erreur": f"{type(e).__name__} : {str(e)[:200]}"}


# ======================================================================================================================
# processus détachés
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
    return bool(sup) and not sup.get("inconnu") and debut_processus(sup["pid"]) is not None \
        and debut_processus(sup["pid"]) == sup["debut_proc"]


def lancer_detache(r: Reglages, argv: list, env: dict, dossier: Path, prefixe_pycache: Path) -> dict:
    """Le superviseur, dans une session de processus neuve, sorties vers des fichiers ; rend {pid, debut_proc, dossier}."""
    dossier.mkdir()
    with open(dossier / "superviseur.stdout.txt", "xb") as fo, open(dossier / "superviseur.stderr.txt", "xb") as fe:
        p = subprocess.Popen([r.python, *options_interprete(prefixe_pycache), "-c", SUPERVISEUR, json.dumps(argv),
                              str(r.orchestrateur), str(dossier)], cwd=str(r.orchestrateur), env=env, stdout=fo, stderr=fe,
                             stdin=subprocess.DEVNULL, start_new_session=True)
    return {"pid": p.pid, "debut_proc": debut_processus(p.pid), "dossier": str(dossier),
            "arret": f"kill -INT {p.pid} d'abord (relayé par PID à l'orchestrateur, fin propre ; jamais par motif, R10) ; "
                     f"kill -TERM {p.pid} seulement si la course ne finit pas"}


def lire_code(sup: dict) -> dict | None:
    return _lire_json_si_scelle(Path(sup["dossier"]) / "code.json")


def superviseur_retrouve(dossier: Path) -> dict | None:
    """M2 : le superviseur d'une course dont le manifeste de départ manque, par le PID qu'il a scellé lui-même."""
    if not dossier.is_dir():
        return None
    for _ in range(ATTENTE_PID_SUPERVISEUR_PAS):       # le superviseur scelle son PID dès son départ : attente bornée
        if _scelle_present(dossier / "pid-superviseur.json") and (dossier / "pid-superviseur.json.sha256").exists():
            break
        time.sleep(0.05)
    p = _lire_json_si_scelle(dossier / "pid-superviseur.json")
    if not isinstance(p, dict) or not isinstance(p.get("pid_superviseur"), int):
        return {"inconnu": True, "dossier": str(dossier)}
    return {"pid": p["pid_superviseur"], "debut_proc": p.get("debut_proc"), "dossier": str(dossier), "retrouve": True,
            "arret": f"kill -INT {p['pid_superviseur']} d'abord (relayé par PID ; R10) ; "
                     f"kill -TERM {p['pid_superviseur']} seulement si la course ne finit pas"}


# ======================================================================================================================
# état des runs (lu dans le dépôt)
# ======================================================================================================================

def runs_du_lanceur(r: Reglages) -> list:
    """Les runs de ce lanceur, dans l'ordre du temps. Un dossier sans manifeste de pré-départ ni de refus scellé est une
    incohérence : refus."""
    d_runs = r.dossier_runs
    if not d_runs.is_dir():
        return []
    runs = []
    for nom in sorted(os.listdir(d_runs)):
        m = re.fullmatch(r"\d{8}-\d{6}" + re.escape(SUFFIXE_RUN) + "(" + "|".join(LIGNEES) + ")", nom)
        if not m:
            raise Refus(f"dossier inattendu dans {d_runs} : {nom!r}")
        d = d_runs / nom
        pre = _lire_json_si_scelle(d / "manifeste-lanceur-pre-depart.json")
        refus = _lire_json_si_scelle(d / "manifeste-lanceur-refus.json")
        if pre is None and refus is None:
            raise Refus(f"run {nom} sans manifeste de pré-départ ni de refus scellé : état inconnu, aucun lancement")
        base = pre or refus
        if base.get("lignee") != m.group(1) or base.get("lanceur", {}).get("version") != VERSION:
            raise Refus(f"run {nom} : lignée ou version du lanceur incohérente")
        depart = _lire_json_si_scelle(d / "manifeste-lanceur-depart.json")
        if depart is None and _scelle_present(d / "manifeste-lanceur-depart.json"):
            raise Refus(f"run {nom} : manifeste de départ au sceau faux")
        fin = _lire_json_si_scelle(d / "manifeste-lanceur-fin.json")
        if fin is None and _scelle_present(d / "manifeste-lanceur-fin.json"):
            raise Refus(f"run {nom} : manifeste de fin au sceau faux")
        sortie = Path(base["sortie"]) if base.get("sortie") else None
        if refus is not None:
            sup = None
        elif depart is not None:
            if not depart.get("superviseur") or depart.get("pre_depart_sha256") != sha256_fichier(
                    d / "manifeste-lanceur-pre-depart.json"):
                raise Refus(f"run {nom} : manifeste de départ sans superviseur ou sans l'empreinte du pré-départ")
            sup = depart["superviseur"]
        else:
            sup = superviseur_retrouve(sortie.parent / SUPERVISEUR_DOSSIER) if sortie else None
        runs.append({"nom": nom, "dossier": d, "lignee": m.group(1), "pre": pre, "depart": depart, "refus": refus,
                     "fin": fin, "sortie": sortie, "superviseur": sup, "lance": sup is not None})
    return runs


def _cout(objet, *cles) -> float:
    for c in cles:
        objet = objet[c]
    if isinstance(objet, bool) or not isinstance(objet, (int, float)) or not math.isfinite(objet) or objet < 0:
        raise ValueError("coût non fini ou négatif")
    return float(objet)


def depense_course(sortie: Path, sup_fini: bool) -> tuple:
    """À la clôture seulement (le dossier hors dépôt est alors lu une fois) : (dépense, lisible, lecture). Aucun chemin ne
    rend 0 par défaut : 0 seulement si le superviseur a fini proprement et que rien n'est parti."""
    if not sup_fini:
        return PLAFOND_COURSE_USD, False, "processus mort sans fin propre : plafond entier compté"
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


def fiches_produites(sortie: Path | None):
    """À la clôture : False si aucune fiche (sortie absente, ou les trois listes scellées et vides) ; True si une fiche
    existe ; None si on ne peut pas le prouver (tenu pour « produites »)."""
    if sortie is None or not sortie.exists():
        return False
    listes = [_lire_json_si_scelle(sortie / n) for n in ("fiches-validees.json", "fiches-refusees.json",
                                                        "fiches-en-quarantaine.json")]
    if any(not isinstance(x, list) for x in listes):
        return None
    return any(listes)


def copier_scelle(source: Path, dest: Path) -> dict:
    """Copie octet pour octet, scellée ; idempotente : une copie déjà là doit être scellée et égale à la source."""
    octets = source.read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if dest.exists() or Path(str(dest) + ".sha256").exists():
        if hashlib.sha256(lire_scelle(dest)).hexdigest() != h:
            raise Refus(f"copie {dest.name} déjà présente et différente de sa source : état incohérent, nœud")
        return {"source": str(source), "sha256": h, "deja_la": True}
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "xb") as f:
        f.write(octets)
    with open(str(dest) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {dest.name}\n")
    return {"source": str(source), "sha256": h}


def copier_preuves(run: dict, sup: dict) -> dict:
    """B1, m1 : les preuves de la dépense, de la relance et de la lecture, copiées dans le dépôt."""
    copies = {}
    d_copies = run["dossier"] / "copies"
    for nom in COPIES_SUPERVISEUR:
        s = Path(sup["dossier"]) / nom
        if s.is_file():
            copies[f"superviseur/{nom}"] = copier_scelle(s, d_copies / f"superviseur--{nom}")
    s_ctrl = Path(str(run["sortie"]) + "-controle") if run["sortie"] else None
    if s_ctrl and s_ctrl.is_dir():
        for nom in sorted(os.listdir(s_ctrl)):
            if re.fullmatch(r"(tentative|refus-taille)-\d+\.json", nom):
                copies[f"controle/{nom}"] = copier_scelle(s_ctrl / nom, d_copies / f"controle--{nom}")
    if run["sortie"] and run["sortie"].is_dir():
        for rel in COPIES_SORTIE:
            s = run["sortie"] / rel
            if s.is_file():
                copies[f"sortie/{rel}"] = copier_scelle(s, d_copies / ("sortie--" + rel.replace("/", "--")))
    return copies


def releve_run(run: dict) -> dict:
    """La dépense d'un run, lue **dans le dépôt** : refus avant départ ou rien lancé → 0 ; clos → relevé scellé ; sinon
    (en marche, mort non clos, superviseur sans PID) → plafond entier, illisible."""
    if not run["lance"]:
        return {"run": run["nom"], "course_usd": 0.0, "lisible": True, "fiches_produites": False,
                "lecture": "rien lancé (refus du lanceur avant le départ, ou superviseur jamais créé)"}
    if run["fin"] is None:
        return {"run": run["nom"], "course_usd": PLAFOND_COURSE_USD, "lisible": False, "fiches_produites": None,
                "lecture": "course non close : plafond entier compté"}
    rel = _lire_json_si_scelle(run["dossier"] / "releve-depense.json")
    try:
        if run["fin"].get("releve_sha256") != sha256_fichier(run["dossier"] / "releve-depense.json"):
            raise ValueError
        out = {"run": run["nom"], "course_usd": _cout(rel, "course_usd"), "lisible": rel["lisible"] is True,
               "fiches_produites": rel["fiches_produites"], "lecture": "relevé scellé dans le dépôt : " + rel["lecture"]}
        if not out["lisible"]:
            out["course_usd"] = max(out["course_usd"], PLAFOND_COURSE_USD)
        return out
    except (TypeError, KeyError, ValueError, OSError):
        return {"run": run["nom"], "course_usd": PLAFOND_COURSE_USD, "lisible": False, "fiches_produites": None,
                "lecture": "relevé absent, au sceau faux ou illisible : plafond entier compté"}


def garde_cumul(runs: list, plafond_go: float) -> dict:
    lignes = [releve_run(x) for x in runs]
    deja = round(sum(x["course_usd"] for x in lignes), 6)
    borne = min(BORNE_LIGNE_USD, plafond_go)
    suivant = PLAFOND_COURSE_USD                     # toutes lignées confondues : la borne est celle de la ligne
    if deja + suivant > borne + 1e-9:
        raise Refus(f"garde de cumul : dépense relevée {deja:.4f} + course {PLAFOND_COURSE_USD} > {borne} USD ; "
                    f"détail : {json.dumps(lignes, ensure_ascii=False)}")
    return {"depense_relevee_usd": deja, "plafond_course_usd": PLAFOND_COURSE_USD, "borne_usd": borne, "par_run": lignes}


def relance_permise(runs: list, lignee: str) -> tuple:
    """Pour la lignée : une course part si aucune n'est partie, ou si **chaque** course partie a fini proprement (code
    scellé), n'a produit aucune fiche, a un relevé lisible **d'au plus `PLAFOND_RELANCE_USD`** (arrêt au contrôle : au-delà,
    la course a dépensé plus loin et n'est pas rejouée) ; deux courses au plus par lignée (une seule relance)."""
    lances = [x for x in runs if x["lance"] and x["lignee"] == lignee]
    for x in lances:
        if x["fin"] is None or x["fin"].get("code") is None:
            return False, f"course {x['nom']} sans fin propre (code non scellé)"
        rel = releve_run(x)
        if rel["fiches_produites"] is not False:
            quoi = "fiches produites" if rel["fiches_produites"] else "production de fiches non prouvée nulle"
            return False, f"course {x['nom']} : {quoi} : génération jouée, jamais rejouée (R3)"
        if not rel["lisible"]:
            return False, f"course {x['nom']} : dépense illisible ({rel['lecture']})"
        if rel["course_usd"] > PLAFOND_RELANCE_USD + 1e-9:
            return False, (f"course {x['nom']} : relevé {rel['course_usd']} USD au-dessus du plafond de relance "
                           f"{PLAFOND_RELANCE_USD} USD (arrêt au-delà du contrôle : pas de seconde course, nœud)")
    if len(lances) >= MAX_COURSES:
        return False, f"{MAX_COURSES} courses déjà parties pour la lignée {lignee} : aucune autre (une seule relance par lignée)"
    return True, f"lignée {lignee} : {len(lances)} course(s) précédente(s), finies proprement, sans fiche, dépense lisible"


# ======================================================================================================================
# commandes
# ======================================================================================================================

def commande_course(r: Reglages, sortie: Path, liste_blanche: Path, horodatage: str, prefixe_pycache: Path) -> list:
    p = {nom: str(r.depot / rel) for nom, (rel, _) in r.pieces.items()}
    for chemin in p.values():
        if any(ch.isspace() for ch in chemin):
            raise Refus(f"chemin avec espace ({chemin}) : la commande externe est découpée par l'orchestrateur")
    b = r.plafonds
    prop_ext, juge_ext = externe_de(r.lignee)
    argv = [
        r.python, *options_interprete(prefixe_pycache), LANCEUR_ORCHESTRATEUR, str(sortie),
        "--liste-blanche", str(liste_blanche),
        "--question", p["question"],
        "--piece", p["faits"], "--piece-juge", p["faits"],
        "--temoins", p["temoins"],
    ]
    for e, m in PROPOSEURS:
        argv += ["--proposeur", f"{e}={m}"]
    argv += ["--proposeur-externe", "=".join(prop_ext), "--commande-externe", "bash " + p["enveloppe_externe"],
             "--modele-commande-externe", prop_ext[1], "--commande-externe-lit-modele"]
    for e, m in JUGES:
        argv += ["--juge", f"{e}={m}"]
    argv += ["--juge-externe", "=".join(juge_ext), "--nombre", str(NOMBRE),
             "--budget-total-usd", _usd(TOTAL_CLAUDE_USD), "--budget-externe-usd", _usd(TOTAL_EXTERNE_USD)]
    for cle in sorted(b):
        argv += ["--budget", f"{cle}={_usd(b[cle])}"]
    argv += ["--budget-controle-externe-usd", _usd(r.controle_externe_usd),
             "--graine", str(GRAINE),
             "--moteur", "claude-sdk", "--url-relais", f"http://127.0.0.1:{PORT_RELAIS_CLAUDE}", "--confirmer-moteur-reel",
             "--horodatage", horodatage]
    argv += list(DELAIS_PAR_LIGNEE.get(r.lignee, ()))
    return argv + list(r.arguments_en_plus)


def commande_mesure(r: Reglages, liste_blanche: Path, prefixe_pycache: Path) -> list:
    p = {nom: str(r.depot / rel) for nom, (rel, _) in r.pieces.items()}
    b = r.plafonds
    prop_ext, juge_ext = externe_de(r.lignee)
    return [r.python, *options_interprete(prefixe_pycache), LANCEUR_ORCHESTRATEUR, "--mesurer-consignes",
            "--liste-blanche", str(liste_blanche), "--question", p["question"],
            "--piece", p["faits"], "--piece-juge", p["faits"], "--temoins", p["temoins"],
            *[x for e, m in PROPOSEURS for x in ("--proposeur", f"{e}={m}")],
            "--proposeur-externe", "=".join(prop_ext),
            *[x for e, m in JUGES for x in ("--juge", f"{e}={m}")],
            "--juge-externe", "=".join(juge_ext), "--nombre", str(NOMBRE),
            "--budget", f"proposeur_ideation|{prop_ext[1]}={_usd(b['proposeur_ideation|' + prop_ext[1]])}",
            "--budget", f"juge_ideation|{juge_ext[1]}={_usd(b['juge_ideation|' + juge_ext[1]])}",
            "--budget-controle-externe-usd", _usd(r.controle_externe_usd)]


def _sous_processus(r: Reglages, argv: list, env: dict, quoi: str) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(argv, cwd=str(r.orchestrateur), env=env, capture_output=True, text=True, timeout=300,
                              stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"{quoi} : non exécuté ({type(e).__name__})") from None


def construire_liste_blanche(r: Reglages, chemin: Path, env: dict, prefixe_pycache: Path, fichiers: dict) -> dict:
    """Par l'orchestrateur lui-même, sans appel ; il écrit la liste **et son compagnon** : le sceau est vérifié, jamais
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


def mesurer_consignes(r: Reglages, argv: list, env: dict, chemin: Path) -> tuple:
    p = _sous_processus(r, argv, env, "mesure des consignes")
    try:
        mesure = json.loads(p.stdout) if p.returncode == 0 else None
    except json.JSONDecodeError:
        mesure = None
    if not isinstance(mesure, dict) or mesure.get("sans_appel") is not True:
        raise Refus(f"mesure des consignes illisible (code {p.returncode}) : {p.stderr.strip()[-500:]!r}")
    return mesure, ecrire_scelle(chemin, mesure)


# ======================================================================================================================
# exécution
# ======================================================================================================================

def orchestrateur_orphelin(sup: dict) -> dict | None:
    """L'orchestrateur d'un superviseur mort, s'il vit encore (PID et, s'il est écrit, heure de départ du processus)."""
    p = _lire_json_si_scelle(Path(sup["dossier"]) / "pid-orchestrateur.json")
    if not isinstance(p, dict) or not isinstance(p.get("pid_orchestrateur"), int):
        return None
    pid, debut = p["pid_orchestrateur"], p.get("debut_proc")
    vu = debut_processus(pid)
    if vu is None or (debut is not None and vu != debut):
        return None
    return {"pid": pid, "debut_proc": debut, "heure_de_depart_verifiee": debut is not None,
            "arret": f"kill -INT {pid} d'abord (par PID, R10) ; kill -TERM {pid} seulement s'il ne finit pas"}


def cloturer(r: Reglages, runs: list) -> list:
    """Pour chaque course lancée, non close, dont le superviseur ne vit plus : copies scellées des preuves dans le dépôt,
    relevé de dépense scellé, puis manifeste de fin (qui porte l'empreinte du relevé)."""
    faits = []
    for run in runs:
        sup = run["superviseur"]
        if not run["lance"] or run["fin"] is not None or superviseur_vivant(sup):
            continue
        code = lire_code(sup)
        orphelin = orchestrateur_orphelin(sup) if code is None else None
        copies = copier_preuves(run, sup)
        sup_fini = code is not None
        dep, lisible, lecture = depense_course(run["sortie"], sup_fini) if run["sortie"] else (PLAFOND_COURSE_USD, False,
                                                                                              "sortie inconnue")
        fp = fiches_produites(run["sortie"]) if sup_fini else None
        comptes = {}
        for n in ("fiches-validees.json", "fiches-refusees.json", "fiches-en-quarantaine.json"):
            x = _lire_json_si_scelle(run["sortie"] / n) if run["sortie"] else None
            comptes[n] = len(x) if isinstance(x, list) else None
        releve = {"run": run["nom"], "course_usd": round(dep, 6), "lisible": lisible, "lecture": lecture,
                  "fiches_produites": fp, "comptes_fiches": comptes, "code": code["code"] if code else None,
                  "copies": copies, "cloture_utc": r.heure().isoformat()}
        h_rel = ecrire_scelle(run["dossier"] / "releve-depense.json", releve)
        d = Path(sup["dossier"])
        journaux = {n: sha256_fichier(d / n) for n in ("orchestrateur.stdout.txt", "orchestrateur.stderr.txt",
                                                       "superviseur.stdout.txt", "superviseur.stderr.txt") if (d / n).is_file()}
        issue = ("fin propre" if code else
                 (f"superviseur mort, ORCHESTRATEUR ENCORE VIVANT (PID {orphelin['pid']}) : plafond compté, génération "
                  f"verrouillée ; arrêt : {orphelin['arret']}" if orphelin else
                  "mort sans fin propre : plafond compté, génération verrouillée"))
        bilan = {"run": run["nom"], "lignee": run["lignee"], "superviseur": sup, "orchestrateur_orphelin": orphelin,
                 "code": code["code"] if code else None, "issue": issue, "journaux_sha256": journaux,
                 "releve_sha256": h_rel, "cloture_utc": r.heure().isoformat()}
        if code and code["code"] == 0 and "sortie/fiches-validees.json" in copies:
            bilan["bilan_de_l_organisme"] = {
                "copie": "copies/sortie--fiches-validees.json",
                "fiches_validees_sha256": copies["sortie/fiches-validees.json"]["sha256"],
                "rappel": "bilan de l'organisme d'idéation sur les organismes discrets (question-v3.md), lignée "
                          + run["lignee"] + " : fiches scellées avant d'être lues par quiconque ; le juge externe de la lignée "
                          "est différé (attestation de lecture de Lazar) ; les lignées se lisent ensemble"}
        ecrire_scelle(run["dossier"] / "manifeste-lanceur-fin.json", bilan)
        faits.append({"run": run["nom"], "code": bilan["code"], "issue": issue, "orchestrateur_orphelin": orphelin,
                      "depense_relevee_usd": releve["course_usd"], "lisible": lisible})
    return faits


def prendre_verrou(r: Reglages) -> int:
    """Verrou exclusif, non bloquant, tenu de la lecture de l'état jusqu'au manifeste de départ (libéré à la sortie du
    processus, même brutale ; jamais hérité par le superviseur)."""
    r.dossier_sorties.mkdir(parents=True, exist_ok=True)
    fd = os.open(r.dossier_sorties / NOM_VERROU, os.O_CREAT | os.O_RDWR, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        os.close(fd)
        raise Refus("une autre invocation du lanceur tient le verrou : rien lancé") from None
    return fd


def executer(r: Reglages, soi: dict) -> int:
    env_lu = os.environ if r.environnement is None else r.environnement
    interprete = verifier_interprete(r)
    runs = runs_du_lanceur(r)
    inconnus = [x["nom"] for x in runs if x["superviseur"] and x["superviseur"].get("inconnu") and x["fin"] is None]
    if inconnus:
        raise Refus(f"course(s) {inconnus} : superviseur créé sans PID scellé ni manifeste de départ ; vérifier à la main "
                    "(par PID) qu'aucun processus de la course ne vit ; plafond compté ; nœud pour la mère")
    orphs = [{"run": x["nom"], **o} for x in runs if x["lance"] and x["fin"] is not None and x["fin"].get("code") is None
             and not superviseur_vivant(x["superviseur"]) for o in [orchestrateur_orphelin(x["superviseur"])] if o]
    if orphs:
        print(json.dumps({"etat": "orchestrateur orphelin vivant : rien lancé", "orphelins": orphs}, ensure_ascii=False),
              flush=True)
        return 4
    en_marche = [x for x in runs if x["lance"] and x["fin"] is None and superviseur_vivant(x["superviseur"])]
    if en_marche:
        print(json.dumps({"etat": "en marche : rien lancé", "processus": [
            {"run": x["nom"], "pid_superviseur": x["superviseur"]["pid"], "arret": x["superviseur"]["arret"]}
            for x in en_marche]}, ensure_ascii=False), flush=True)
        return 3
    clos = cloturer(r, runs)
    if clos:
        print(json.dumps({"etat": "clôture", "processus": clos}, ensure_ascii=False), flush=True)
        return 4 if any(c["orchestrateur_orphelin"] for c in clos) else 0
    go = verifier_go(r.registre_go, r.aujourd_hui or r.heure().date())
    ok, motif = relance_permise(runs, r.lignee)
    if not ok:
        raise Refus(f"lignée {r.lignee} verrouillée : {motif} ; nœud")
    cumul = garde_cumul(runs, go["plafond_usd"])
    orch = verifier_orchestrateur(r)
    pieces = verifier_pieces(r)
    horodatage = r.horodatage()
    ident = r.heure().strftime("%Y%m%d-%H%M%S") + SUFFIXE_RUN + r.lignee
    dossier_run = r.dossier_runs / ident
    dossier_sortie = r.dossier_sorties / ident
    sortie = dossier_sortie / "sortie"
    prefixe_pycache = dossier_sortie / NOM_DOSSIER_PYCACHE
    liste_blanche = dossier_run / "liste-blanche.json"
    argv = commande_course(r, sortie, liste_blanche, horodatage, prefixe_pycache)
    garde_drapeaux(argv)
    sommes = garde_sommes(argv)
    if dossier_run.exists() or dossier_sortie.exists():
        raise Refus(f"{dossier_run} ou {dossier_sortie} existe déjà (R12)")
    verifier_prefixe_pycache(prefixe_pycache, Path(orch["racine_clone"]))
    env, noms_env = environnement_permis(env_lu, go["id"], prefixe_pycache, dossier_sortie / "home", r.prefixe_essais)
    bac = sonder_bac_a_sable(r, env, prefixe_pycache)
    depot_git = _depot_git(r)                       # M2 : avant le détachement, jamais après

    # --- écritures : toute exception avant le départ écrit un manifeste de refus scellé ; rien n'est appelé avant le départ
    dossier_run.mkdir(parents=True)
    socle = {"lanceur": soi, "lignee": r.lignee, "id": ident, "go": go, "sortie": str(sortie), "horodatage_canonique": horodatage}
    detachement_tente = False
    try:
        dossier_sortie.mkdir(parents=True)
        prefixe_pycache.mkdir()
        (dossier_sortie / "home").mkdir(mode=0o700)
        fichiers = {str(r.depot / r.pieces[n][0]): r.pieces[n][1] for n in ("question", "faits", "temoins")}
        lb = construire_liste_blanche(r, liste_blanche, env, prefixe_pycache, fichiers)
        mesure, h_mesure = mesurer_consignes(r, commande_mesure(r, liste_blanche, prefixe_pycache), env,
                                             dossier_run / "mesure-consignes.json")
        tailles = gardes_de_taille(mesure, r)
        pre = dict(socle, **{
            "decision": DECISION,
            "lignee_externe": LIGNEES_EXTERNES[r.lignee],
            "superviseur_attendu": {"dossier": str(dossier_sortie / SUPERVISEUR_DOSSIER)},
            "orchestrateur": orch, "pieces": pieces, "liste_blanche": lb, "mesure_consignes_sha256": h_mesure,
            "bac_a_sable": bac, "commande": argv, "cwd": str(r.orchestrateur),
            "plafonds": {"reglage": dict(r.plafonds), "controle_externe_usd": r.controle_externe_usd,
                         "sommes": sommes, "gardes_de_taille": tailles,
                         "plafond_course_usd": PLAFOND_COURSE_USD, "pire_cas_devis_usd": PIRE_CAS_DEVIS_USD},
            "garde_de_cumul": cumul, "relance": motif, "drapeaux_interdits_verifies_absents": list(DRAPEAUX_INTERDITS),
            "environnement": noms_env, "depot_travail": depot_git, "python": interprete,
            "cache_d_octets": {"prefixe": str(prefixe_pycache), "option": f"-X pycache_prefix={prefixe_pycache}"}})
        h_pre = ecrire_scelle(dossier_run / "manifeste-lanceur-pre-depart.json", pre)
        detachement_tente = True
        sup = lancer_detache(r, argv, env, dossier_sortie / SUPERVISEUR_DOSSIER, prefixe_pycache)
    except BaseException as e:  # noqa: BLE001 — jamais un run sans manifeste ; rien n'est parti
        motif_refus = str(e) if isinstance(e, Refus) else f"{type(e).__name__} : {e}"
        if detachement_tente and (dossier_sortie / SUPERVISEUR_DOSSIER / "superviseur.stdout.txt").exists():
            # le superviseur a peut-être démarré : jamais de manifeste de refus (il dirait « rien parti ») ; l'invocation
            # suivante retrouve la course par le pré-départ et le PID scellé par le superviseur, ou refuse (nœud)
            raise Refus("exception au détachement, superviseur peut-être démarré : état incertain, rien écrit de plus ; "
                        "relancer la même commande pour le compte rendu : " + motif_refus[:400]) from None
        ecrire_scelle(dossier_run / "manifeste-lanceur-refus.json", dict(socle, refus=motif_refus[:2000]))
        if isinstance(e, Refus):
            raise
        raise Refus("exception avant le départ, manifeste de refus scellé : " + motif_refus[:500]) from None
    # --- M2 : après le détachement, une seule écriture, courte ; aucune commande git, aucun calcul qui puisse échouer
    try:
        h = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json",
                          {"pre_depart_sha256": h_pre, "superviseur": sup, "lanceur": {"version": VERSION}})
    except BaseException as e:  # noqa: BLE001
        print(json.dumps({"etat": "COURSE LANCÉE, manifeste de départ NON écrit", "pid_superviseur": sup["pid"],
                          "arret": sup["arret"], "erreur": f"{type(e).__name__} : {str(e)[:300]}",
                          "suite": "la même commande retrouve la course par le manifeste de pré-départ et le PID scellé par "
                                   "le superviseur"}, ensure_ascii=False), file=sys.stderr, flush=True)
        return 5
    print(json.dumps({"lignee": r.lignee, "etat": "lancée, détachée", "pid_superviseur": sup["pid"], "arret": sup["arret"],
                      "manifeste_depart_sha256": h, "sortie": str(sortie), "go": go["id"]}, ensure_ascii=False), flush=True)
    return 0


def principal(argv: list | None = None, reglages: Reglages | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) != 1 or argv[0] not in LIGNEES:
        print(json.dumps({"refus": f"un seul argument admis, la lignée parmi {list(LIGNEES)} (reçu {argv!r})"},
                         ensure_ascii=False), file=sys.stderr)
        return 2
    r = reglages or Reglages.production(argv[0])
    if r.lignee != argv[0]:
        print(json.dumps({"refus": f"lignée des réglages {r.lignee!r} ≠ argument {argv[0]!r}"}, ensure_ascii=False), file=sys.stderr)
        return 2
    fd = None
    try:
        soi = verifier_soi(r)
        fd = prendre_verrou(r)
        return executer(r, soi)
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    finally:
        if fd is not None:
            os.close(fd)


if __name__ == "__main__":
    raise SystemExit(principal())
