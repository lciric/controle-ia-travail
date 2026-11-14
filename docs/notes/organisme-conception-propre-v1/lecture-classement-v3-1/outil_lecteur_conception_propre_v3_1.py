#!/usr/bin/env python3
"""Outil du lecteur de la règle de sélection — course « conception propre » — v3.1 (lecteur Astra).

v3.1 (14 novembre 2026, à partir de 09:01 UTC, `date -u`) = v3 (`../lecture-classement-v3/`, `6a11cf3d…`, gardée, R12),
corrigée par son auteur d'après la contre-lecture `contre-lecture-lecture-classement-v3-v1.md` (`f5cc9cdb…`, modèle B,
R-2678 : « non utilisable en l'état pour `envoyer` ») et la consigne de la mère ; prix lus : `prix-astra-v2.md`
(`bf211a07…`, R-2677). La règle de lecture ne change pas (fonctions de la règle identiques à la v3, essai
`test_regle_inchangee_v3_v3_1`). Changements, et seulement eux (détail : `rapport-lecture-classement-v3-1.md`) :

- **B1, clé** : une clé vide, ou qui porte un caractère hors de l'ASCII imprimable (retour chariot, saut de ligne,
  espace…), est refusée sans être montrée, avant tout journal et tout envoi ; le message d'une exception de transport
  n'est jamais écrit (seul son type) ; tout ce qu'`envoyer` écrit (réponse, erreur, journal, relevé) passe par
  `expurger`, qui remplace la clé et ses formes échappées (JSON, `\\/`, pourcentage, repr) ; une réponse qui porte la clé
  est une anomalie bloquante (`cle_dans_la_reponse`) ;
- **B2, redirection** : aucune redirection suivie (`SansRedirection`) ; un statut 3xx est une anomalie bloquante
  (`redirection_refusee`) ; l'adresse finale doit égaler l'adresse demandée ; l'en-tête d'autorisation ne part que vers
  `api.openai.com` ;
- **M1** : `verifier` (donc le classement) refuse toute réponse sans réception ou clôture chaînée au journal, à son nom,
  à son empreinte et au statut 200 ; le journal et le dossier sont confrontés dans les deux sens ;
- **M2, C6** : un seul dossier d'envois par lecture, à un chemin fixe (`DOSSIER_ENVOIS_REL`) ; tout autre manifeste
  d'envois v3 sous `docs/` ou `runs/` fait refuser `preparer`, `envoyer`, `bilan` et `verifier` : la dépense ne repart
  jamais de zéro ; le plafond est borné par 14,20 USD moins la dépense antérieure déclarée (`--depense-anterieure-usd`,
  obligatoire, consignée) ;
- **M3** : une réponse 200 payée est écrite brute (le corps seul, sans en-têtes ni clé), scellée et consignée au journal
  (`recu`) **avant** toute analyse ; l'analyse ne lève plus (chaque champ contrôlé par son type ; filet déclaré
  `analyse_en_echec`, pire cas) ;
- **M4** : usage incohérent, compté au pire cas et bloquant, aussi vers le bas : total sous la somme, entrée sous un
  plancher (octets du corps / 16), sortie visible sous un plancher (octets du contenu rendu / 16, au moins 1 si le contenu
  n'est pas vide) ;
- **M5** : un cas sain et un artefact par garde dans les essais (mutants survivants du contre-lecteur) ; tout écart
  d'envoi consigné au journal est une anomalie bloquante de la vérification (`anomalie_d_envoi`, réserve r6 de la v3
  levée) ;
- **m1** : à l'envoi, le manifeste (même rescellé) est revérifié : prix égaux aux prix lus, plafond fini et dans les
  bornes, nombre d'appels, lecteur, octets et pire cas de chaque corps, paramètres de chaque corps ;
- **m3** : docstring de `lire_reponse` juste (le contenu d'une réponse à fin autre que `stop` est lu) ;
- **palier** : `--palier standard|flex` (défaut `standard`), consigné au manifeste ; `flex` ajoute
  `service_tier: "flex"` au corps et exige le même palier dans la réponse ; en standard, un palier servi autre que
  `default` (ou absent) est aussi une anomalie bloquante (SUPPOSÉ sur les noms, éprouvé au premier appel, C3) ; prix des
  deux paliers (entrée, entrée en cache, sortie) pris de `prix-astra-v2.md`, source et date au manifeste (C2) ;
  aucune option de prix en ligne de commande ;
- noms des fichiers écrits en `-v3-1` (R12).

De la v3 (inchangé, sauf ci-dessus) : Chat Completions (`POST https://api.openai.com/v1/chat/completions`) ; corps à un
seul message, `max_completion_tokens` 32 768, `reasoning_effort` choisi, `store: false` ; clé lue par son nom seul,
`OPENAI_API_KEY`, dans `lire_cle`, retirée aussitôt de l'environnement ; lots de 5 (`TAILLE_LOT`), 18 appels au plus ;
modèle servi vérifié à l'égalité exacte ; garde de dépense (avant chaque appel : dépense comptée + pire cas ≤ plafond ;
après : coût lu dans `usage`, pire cas sinon) ; journal chaîné, relu à chaque reprise ; arrêt au premier écart, aucune
reprise, aucune relecture ; corps d'erreur jamais écrit ; C1 bloquante ; envois régénérés de façon déterministe (mêmes
ordres et étiquettes que la v2). De la v2 : attestation exigée, pièces épinglées, provenance M3, admissibilité, vue servie
sans auteur ni marque de témoin, citations d'au moins 20 caractères vérifiées mot pour mot, catalogue lu dans la cellule
du mécanisme, anomalies bloquantes nommant les fiches.

Actions :

    python3 -I -B outil_lecteur_conception_propre_v3_1.py preparer --fiches F --attestation A --sortie DOSSIER_FIXE \
        --effort low|medium|high [--palier standard|flex] --plafond-usd X --depense-anterieure-usd D
    python3 -I -B outil_lecteur_conception_propre_v3_1.py envoyer --envois DOSSIER_FIXE [--envois-max N]
    python3 -I -B outil_lecteur_conception_propre_v3_1.py bilan --envois DOSSIER_FIXE
    python3 -I -B outil_lecteur_conception_propre_v3_1.py verifier --envois DOSSIER_FIXE [--lecture L1|L2]

DOSSIER_FIXE = `<racine>/docs/notes/organisme-conception-propre-v1/lecture-g1-v3-1/envois`.
Codes de sortie : 0 fait (ou pause demandée par `--envois-max`) ; 2 refus (rien d'envoyé de plus) ; 3 arrêt sur anomalie ;
4 arrêt avant un appel qui pourrait dépasser le plafond.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np

VERSION = "outil-lecteur-conception-propre-v3-1"
RACINE_DEFAUT = Path(__file__).resolve().parents[4]
DOSSIER = "docs/notes/organisme-conception-propre-v1"
PIECES = {
    "consigne": (f"{DOSSIER}/consigne-lecteur-v1.md",
                 "95efebaae5e97764c50b334daa1d3d4f28e5d4517396513afd1f3640ac06da8d"),
    "question": (f"{DOSSIER}/question-organisme-conception-propre-v1.md",
                 "77c524f3c591e43ec1b14e261bd4667cf0e085b6c94afe7e7b37f72816c6feb4"),
    "faits": ("docs/notes/collisionneur-bassins-etroits-v1/faits-v1.md",
              "d19b540015ed9480774c020cd7f1a527db32d42600a5bc2bd34c92c17d7be0b3"),
    "catalogue": (f"{DOSSIER}/catalogue-conceptions-publiees-v1.md",
                  "ddfb2522be0fe5095926405b8761d0e4be0065a29679585051a287349114fe9d"),
    "temoins_lecteur": (f"{DOSSIER}/temoins-lecteur-v1.json",
                        "d11efe787cd27d2acb4b912487565896e43fc7cefbc7f51aa18080f3cdf8a77e"),
    "temoins_hasard": (f"{DOSSIER}/temoins-hasard-v1.json",
                       "b5e38724cf74b61e1db47f6dbc0e8f6955a0e4419723dc0ecd627854206c539d"),
    "conception": (f"{DOSSIER}/conception-course-v1.md",
                   "be3ba97ee418de50fa356b0e39fcfa62c16d06f5767560265fcc7ee9f191a95e"),
}
ENTROPIE_ORDRES = 2026111302           # § 4.3 : spawn(4) → 0, 1 ordres ; 2 départage ; 3 témoin à score permuté
# v3 : 5 fiches par lot. Kimi a passé plus de 32 765 jetons à raisonner sur 14 ou 15 fiches sans rien rendre (R-2658),
# soit plus de 2 200 jetons de raisonnement par fiche ; on vise au moins 5 000 jetons de raisonnement et 700 de sortie
# visible par fiche sous un plafond de 32 768 : 32 768 / 5 700 ≈ 5,7 → 5. Plus petit multiplie le préambule fixe (≈ 28 ko
# servis à chaque appel) et le nombre d'appels ; 43 fiches → 9 lots (sept de 5, deux de 4), 18 appels.
TAILLE_LOT = 5
LECTURES = ("L1", "L2")
MODELE_LECTEUR = "gpt-6-astra"
URL_AMONT = "https://api.openai.com/v1/chat/completions"
VARIABLE_CLE = "OPENAI_API_KEY"
MAX_SORTIE = 32768                     # max_completion_tokens : sortie visible et raisonnement compris
EFFORTS = ("low", "medium", "high")    # reasoning_effort, choisi à la préparation, consigné
MAX_APPELS = 18                        # deux lectures × 9 lots : fixé d'avance ; plus d'appels → refus à la préparation
PLAFOND_ABSOLU_USD = 14.20             # reste du GO-2026-11-13-06 au 14 novembre (21 − 6,791087), arrondi en dessous
OCTETS_MARGE = 1024                    # pire cas d'entrée : un jeton par octet du corps, plus 1 024 (règle des relais)
DELAI_S = 1800
TAILLE_MAX_REPONSE = 1_000_000           # une réponse de 32 768 jetons fait moins de 200 ko
PLANCHER_OCTETS_PAR_JETON = 16           # M4 : planchers d'usage (entrée et sortie visible)
MOTIF_CLE = re.compile(r"[\x21-\x7e]{1,512}")  # B1 : ASCII imprimable, sans espace ni fin de ligne
LEVIERS = ("levier:juge", "levier:proposeurs", "levier:composition", "levier:cout")
NATURES_ADMISES = ("modification", "ajout")
CRITERES = ("R1", "R2", "R3", "R4", "R5", "R6", "R7")
CLES_ENTREE = CRITERES + ("N",)
LONGUEUR_MIN_PASSAGE = 20      # M1 : caractères hors espaces ; la consigne borne en haut à 200
LONGUEUR_MAX_CONSIGNE = 200    # rapporté seulement (un passage plus long n'est pas refusé)
CELLULE_MECANISME = 2          # colonnes du catalogue : Code | Conception | Mécanisme central | Source
DOSSIER_RUNS = "runs/course-ideation-conception-propre-v1"
MOTIF_RUN = r"\d{8}-\d{6}-course-ideation-conception-propre-v1-g1"
NOM_COPIE_FICHES = "sortie--fiches-validees.json"
MANIFESTE_FIN = "manifeste-lanceur-fin.json"
ANOMALIES_BLOQUANTES = ("reponse_illisible", "fin_non_stop", "entree_manquante", "entree_en_double",
                        "cle_de_critere_manquante", "reponse_absente", "modele_servi_different", "refus_du_lecteur",
                        "anomalie_d_envoi", "reponse_non_analysee", "palier_servi_different")
CODES_CATALOGUE = tuple(f"C{i}" for i in range(1, 13))
CHAMPS_INTERNES = ("auteur", "identifiant_auteur", "empreinte", "passe", "temoin")  # toujours retirés (orchestrateur)
ATTESTATION_CHAMPS = ("lecteur", "lu_le", "fiches_validees_sha256", "aucune_recette_aucun_secret",
                      "envoi_au_lecteur_externe_permis")
SUFFIXE = "v3-1"                       # R12 : noms des fichiers écrits
JOURNAL = f"journal-depense-{SUFFIXE}.jsonl"
MANIFESTE = f"manifeste-envois-{SUFFIXE}.json"
PILE = f"pile-interne-{SUFFIXE}.json"
CLE_LECTURES = f"cle-lectures-{SUFFIXE}.json"
# C6 : un seul dossier d'envois par lecture, à ce chemin (sous la racine)
DOSSIER_ENVOIS_REL = f"{DOSSIER}/lecture-g1-v3-1/envois"
# C2 : prix lus sur la page officielle (prix-astra-v2.md, tableau « Flagship models », contexte <= 272K jetons
# d'entrée), USD par million de jetons ; la ligne du tableau de chaque palier est revérifiée dans la pièce épinglée.
PIECES_PRIX = {"prix": (f"{DOSSIER}/prix-astra-v2.md",
                        "bf211a074868f49175bd59089a3082ec78da0d545850145ca27743b260ac78df")}
PRIX_LUS = {"standard": {"entree": 10.0, "cache": 1.0, "sortie": 50.0},
            "flex": {"entree": 5.0, "cache": 0.5, "sortie": 25.0}}
LIGNES_SOURCE_PRIX = {"standard": "| Standard | 10,00 | 1,00 | 50,00 |", "flex": "| Flex / Batch | 5,00 | 0,50 | 25,00 |"}
SOURCE_PRIX = ("prix-astra-v2.md (bf211a074868f49175bd59089a3082ec78da0d545850145ca27743b260ac78df), relevé par la "
               "session mère le 2026-11-14 à 08:45:38Z (R-2677) : page officielle "
               "https://developers.openai.com/api/docs/pricing (demandée https://platform.openai.com/docs/pricing), "
               "tableau Flagship models, contexte <= 272K input tokens ; copie "
               "docs/sources/tarifs-openai-v1/developers-openai-com-api-docs-pricing-2026-11-14.html "
               "(099c9496f75ffe6f08a57f30b007c5abf79f6eb26ecba5ddecf50ffdf4ec8028)")
PALIERS = ("standard", "flex")
SERVICE_TIER = {"standard": None, "flex": "flex"}   # champ `service_tier` du corps (absent en standard)
# palier servi admis dans la réponse : égalité pour flex (consigne) ; en standard, absent ou « default »
# (« standard » admis aussi) : SUPPOSÉ sur les noms, éprouvé au premier appel (C3)
PALIERS_SERVIS_ADMIS = {"standard": (None, "default", "standard"), "flex": ("flex",)}
# Vue du lecteur : clés du gabarit de l'orchestrateur (`pole/ideation_v2.py`, GABARIT), dans son ordre.
ORDRE_VUE = (("nom", None), ("type", None), ("enonce", None),
             ("loi_predictive", ("espace_instances", "prediction", "signe", "metrique")),
             ("perte_traduction", None), ("questions_servies", "liste"),
             ("avantage", ("source", "texte", "incopiable_parce_que")), ("originalite", ("niveau", "texte")),
             ("demande_organisme", ("nature", "texte")), ("cout", ("nature", "ordre_de_grandeur")),
             ("piege", None), ("cosmetique_si", None), ("anteriorite", ("reference", "statut")))
TABLE_TYPO = {"\xab": '"', "\xbb": '"', "“": '"', "”": '"', "‘": "'", "’": "'", "—": "-",
              "–": "-", "\xa0": " ", " ": " ", "…": "..."}


class Refus(Exception):
    """Arrêt sans repli : rien n'est écrit ni envoyé de plus."""


# --- empreintes et sceaux ---------------------------------------------------------------------------------------------

def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_fichier(chemin) -> str:
    return sha256_octets(Path(chemin).read_bytes())


def verifier_sceau(chemin) -> str:
    """Le fichier égale son compagnon `.sha256` (« <hex>  <nom> », ou « <hex> » seul) ; rend l'empreinte."""
    p = Path(chemin)
    c = Path(str(p) + ".sha256")
    if not p.is_file():
        raise Refus(f"{p} : absent")
    if not c.is_file():
        raise Refus(f"{p} : compagnon .sha256 absent (non scellé)")
    jetons = c.read_text(encoding="utf-8").split()
    if not jetons or not re.fullmatch(r"[0-9a-f]{64}", jetons[0]):
        raise Refus(f"{c} : illisible")
    if len(jetons) > 2 or (len(jetons) == 2 and jetons[1] != p.name):
        raise Refus(f"{c} : nom différent de {p.name}")
    h = sha256_fichier(p)
    if h != jetons[0]:
        raise Refus(f"{p} : empreinte {h[:12]}… ≠ scellée {jetons[0][:12]}…")
    return h


def ecrire_scelle_octets(chemin, b: bytes) -> str:
    """Écrit un fichier neuf et son compagnon ; refuse d'écraser (R12)."""
    p = Path(chemin)
    if p.exists() or Path(str(p) + ".sha256").exists():
        raise Refus(f"{p} existe déjà : on n'écrase jamais (R12)")
    p.write_bytes(b)
    h = sha256_octets(b)
    Path(str(p) + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


def ecrire_scelle(chemin, texte: str) -> str:
    return ecrire_scelle_octets(chemin, texte.encode("utf-8"))


def json_texte(objet) -> str:
    return json.dumps(objet, ensure_ascii=False, indent=1, allow_nan=False) + "\n"


def lire_piece(racine, nom) -> tuple[str, str]:
    rel, attendue = PIECES[nom]
    p = Path(racine) / rel
    if not p.is_file():
        raise Refus(f"pièce {nom} absente : {rel}")
    h = sha256_fichier(p)
    if h != attendue:
        raise Refus(f"pièce {nom} ({rel}) : empreinte {h[:12]}… ≠ épinglée {attendue[:12]}…")
    return p.read_text(encoding="utf-8"), h


def maintenant() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


# --- vue du lecteur (inchangée depuis la v2) -----------------------------------------------------------------------------

def normaliser_typographie(texte: str) -> str:
    """Recopie de `normaliser_typographie` de l'orchestrateur (CL31-17), comparée à l'original par les essais."""
    for a, b in TABLE_TYPO.items():
        texte = texte.replace(a, b)
    return re.sub(r"[ \t]+", " ", texte)


def normaliser_objet(o):
    if isinstance(o, str):
        return normaliser_typographie(o)
    if isinstance(o, list):
        return [normaliser_objet(x) for x in o]
    if isinstance(o, dict):
        return {k: normaliser_objet(v) for k, v in o.items()}
    return o


def vue_lecteur(fiche: dict) -> tuple[dict, list[str]]:
    """(vue servie au lecteur, chemins des champs retirés). Refus si une clé du gabarit manque."""
    if not isinstance(fiche, dict):
        raise Refus("fiche non dictionnaire")
    vue, retires = {}, [k for k in fiche if k not in dict(ORDRE_VUE) and k not in CHAMPS_INTERNES]
    for cle, sous in ORDRE_VUE:
        if cle not in fiche:
            raise Refus(f"fiche sans le champ {cle!r}")
        v = fiche[cle]
        if sous is None:
            if not isinstance(v, str):
                raise Refus(f"{cle} : texte attendu")
            vue[cle] = v
        elif sous == "liste":
            if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
                raise Refus(f"{cle} : liste de textes attendue")
            vue[cle] = list(v)
        elif cle == "anteriorite":
            if not isinstance(v, list):
                raise Refus("anteriorite : liste attendue")
            vue[cle] = []
            for i, a in enumerate(v):
                if not isinstance(a, dict) or any(not isinstance(a.get(s), str) for s in sous):
                    raise Refus(f"anteriorite[{i}] : champs manquants")
                retires += [f"anteriorite[{i}].{k}" for k in a if k not in sous]
                vue[cle].append({s: a[s] for s in sous})
        else:
            if not isinstance(v, dict):
                raise Refus(f"{cle} : objet attendu")
            retires += [f"{cle}.{k}" for k in v if k not in sous]
            vue[cle] = {}
            for s in sous:
                if s not in v:
                    if cle == "avantage" and s == "incopiable_parce_que":
                        continue  # facultatif au gabarit quand la source est « aucune »
                    raise Refus(f"{cle}.{s} manquant")
                if not isinstance(v[s], str):
                    raise Refus(f"{cle}.{s} : texte attendu")
                vue[cle][s] = v[s]
    return normaliser_objet(vue), sorted(retires)


def leviers_de(fiche: dict) -> list[str]:
    return [q for q in fiche.get("questions_servies", []) if isinstance(q, str) and q.strip() in LEVIERS]


def admissibilite(fiche: dict) -> tuple[bool, str]:
    """§ 4.1 (la fiche est validée par construction : elle vient de `fiches-validees.json`)."""
    lev = leviers_de(fiche)
    if len(lev) != 1:
        return False, f"{len(lev)} étiquette(s) de levier (exactement une exigée)"
    nature = (fiche.get("demande_organisme") or {}).get("nature")
    if nature not in NATURES_ADMISES:
        return False, f"nature de la demande {nature!r} (modification ou ajout exigée)"
    return True, "admissible"


# --- préparation --------------------------------------------------------------------------------------------------------

def verifier_attestation(chemin, sha_fiches: str) -> dict:
    verifier_sceau(chemin)
    try:
        a = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise Refus(f"attestation illisible : {e}") from e
    if not isinstance(a, dict) or any(k not in a for k in ATTESTATION_CHAMPS):
        raise Refus("attestation : champs manquants " + ", ".join(k for k in ATTESTATION_CHAMPS if k not in (a or {})))
    if a["fiches_validees_sha256"] != sha_fiches:
        raise Refus("attestation : elle ne porte pas l'empreinte du fichier de fiches donné")
    if a["aucune_recette_aucun_secret"] is not True or a["envoi_au_lecteur_externe_permis"] is not True:
        raise Refus("attestation : envoi au lecteur externe non permis")
    if not isinstance(a["lecteur"], str) or not a["lecteur"].strip():
        raise Refus("attestation : lecteur non nommé")
    return a


def verifier_fiches_de_run(racine, chemin) -> dict:
    """M3 : le seul fichier accepté est la copie scellée des fiches validées dans le dossier d'un run du lanceur, dont le
    manifeste de fin (scellé, code 0) porte la même empreinte. Rend {chemin relatif, run, sha256, manifeste_fin_sha256}."""
    racine = Path(racine).resolve()
    p = Path(chemin)
    p = p if p.is_absolute() else racine / p
    if p.is_symlink() or any(q.is_symlink() for q in p.parents if str(q).startswith(str(racine))):
        raise Refus(f"{p} : lien symbolique refusé")
    try:
        rel = p.resolve().relative_to(racine)
    except ValueError as e:
        raise Refus(f"{p} : hors du dépôt") from e
    parties = rel.parts
    attendu = tuple(DOSSIER_RUNS.split("/"))
    if (len(parties) != len(attendu) + 3 or parties[:len(attendu)] != attendu
            or not re.fullmatch(MOTIF_RUN, parties[len(attendu)]) or parties[-2] != "copies"
            or parties[-1] != NOM_COPIE_FICHES):
        raise Refus(f"{rel} : seul {DOSSIER_RUNS}/<run>/copies/{NOM_COPIE_FICHES} est accepté")
    sha = verifier_sceau(p)
    d_run = racine.joinpath(*parties[:len(attendu) + 1])
    h_fin = verifier_sceau(d_run / MANIFESTE_FIN)
    try:
        fin = json.loads((d_run / MANIFESTE_FIN).read_text(encoding="utf-8"))
    except ValueError as e:
        raise Refus(f"{MANIFESTE_FIN} illisible : {e}") from e
    if not isinstance(fin, dict) or fin.get("code") != 0:
        raise Refus(f"{MANIFESTE_FIN} : course sans fin propre (code {fin.get('code') if isinstance(fin, dict) else '?'})")
    if (fin.get("pour_l_attestation") or {}).get("fiches_validees_sha256") != sha:
        raise Refus(f"{MANIFESTE_FIN} : l'empreinte des fiches validées ne correspond pas à {NOM_COPIE_FICHES}")
    return {"chemin": "/".join(parties), "run": parties[len(attendu)], "sha256": sha, "manifeste_fin_sha256": h_fin}


def verifier_forme_fiches_validees(fiches) -> None:
    """M3 : une liste de fiches validées de l'orchestrateur (clés du gabarit et champs internes), jamais une autre liste
    (quarantaine `{fiche, signaux}`, refus, témoins)."""
    if not isinstance(fiches, list):
        raise Refus("fichier des fiches : liste attendue")
    for i, f in enumerate(fiches):
        if not isinstance(f, dict):
            raise Refus(f"élément {i} : non dictionnaire")
        manque = [c for c, _ in ORDRE_VUE if c not in f] + [c for c in ("auteur", "identifiant_auteur", "passe",
                                                                         "empreinte") if c not in f]
        if manque:
            raise Refus(f"élément {i} : pas une fiche validée (manque {', '.join(manque)})")


def construire_pile(fiches_reelles: list, temoins_lecteur: dict, temoins_hasard: dict) -> dict:
    pile, hors_question, retires = [], [], {}
    for i, f in enumerate(fiches_reelles):
        if not isinstance(f, dict):
            raise Refus(f"fiche réelle {i} : non dictionnaire")
        ident = f.get("identifiant_auteur") or f"reelle-{i:02d}"
        ok, motif = admissibilite(f)
        if not ok:
            hors_question.append({"id": ident, "indice_fichier": i, "auteur": f.get("auteur"), "motif": motif})
            continue
        vue, r = vue_lecteur(f)
        if r:
            retires[ident] = r
        pile.append({"id": ident, "origine": "reelle", "indice_fichier": i, "auteur": f.get("auteur"),
                     "passe": f.get("passe"), "famille": "reelle", "code": None, "attendu": None,
                     "levier": leviers_de(f)[0].strip(), "cout": f["cout"]["nature"], "vue": vue})
    for groupe in (temoins_lecteur, temoins_hasard):
        for t in groupe["temoins"]:
            ok, motif = admissibilite(t["fiche"])
            if not ok:
                raise Refus(f"témoin {t['code']} non admissible : {motif}")
            vue, r = vue_lecteur(t["fiche"])
            if r:
                retires[t["code"]] = r
            pile.append({"id": t["code"], "origine": "temoin", "indice_fichier": None, "auteur": None, "passe": None,
                         "famille": t["famille"], "code": t["code"], "attendu": t.get("attendu"),
                         "cible": t.get("cible"), "entree": t.get("entree"),
                         "levier": leviers_de(t["fiche"])[0].strip(), "cout": t["fiche"]["cout"]["nature"],
                         "vue": vue})
    ids = [p["id"] for p in pile]
    if len(set(ids)) != len(ids):
        raise Refus("identifiants de la pile non uniques")
    return {"fiches": pile, "hors_question": hors_question, "champs_retires": retires}


def enfants_ordres():
    return np.random.SeedSequence(ENTROPIE_ORDRES).spawn(4)


def ordres_lectures(n: int) -> dict:
    e = enfants_ordres()
    return {L: [int(x) for x in np.random.default_rng(e[i]).permutation(n)] for i, L in enumerate(LECTURES)}


def decouper_lots(n: int) -> list[list[int]]:
    """⌈n / TAILLE_LOT⌉ lots consécutifs de tailles égales à un près (TAILLE_LOT au plus)."""
    if n == 0:
        return []
    k = math.ceil(n / TAILLE_LOT)
    return [[int(x) for x in a] for a in np.array_split(np.arange(n), k)]


def etiquette(rang: int) -> str:
    return f"F{rang + 1:02d}"


def texte_message(pieces: dict, lot: list[tuple[str, dict]], k: int, m: int) -> str:
    fiches = [{"etiquette": e, "fiche": v} for e, v in lot]
    return ("".join([
        pieces["consigne"].rstrip("\n"), "\n\n",
        "=== Pièce : la question posée aux proposeurs (question-organisme-conception-propre-v1.md) ===\n\n",
        pieces["question"].rstrip("\n"), "\n\n",
        "=== Pièce : faits-v1.md ===\n\n", pieces["faits"].rstrip("\n"), "\n\n",
        "=== Pièce : catalogue fermé (catalogue-conceptions-publiees-v1.md) ===\n\n",
        pieces["catalogue"].rstrip("\n"), "\n\n",
        f"=== Lot {k} sur {m} : {len(lot)} fiches, {lot[0][0]} à {lot[-1][0]}, dans cet ordre ===\n\n",
        "```json\n", json.dumps(fiches, ensure_ascii=False, indent=1), "\n```\n"]))


def lecteur_attendu(effort: str, palier: str) -> dict:
    return {"modele": MODELE_LECTEUR, "url": URL_AMONT, "point_d_entree": "Chat Completions",
            "variable_cle": VARIABLE_CLE, "max_completion_tokens": MAX_SORTIE, "reasoning_effort": effort,
            "store": False, "service_tier": SERVICE_TIER[palier]}


def corps_requete(message: str, effort: str, palier: str = "standard") -> str:
    """Corps de Chat Completions : un seul message utilisateur ; plafond de sortie et effort explicites ; rien gardé chez
    le fournisseur (`store: false`) ; palier Flex demandé par `service_tier: "flex"`, aucun champ pour le standard."""
    c = {"model": MODELE_LECTEUR, "messages": [{"role": "user", "content": message}],
         "max_completion_tokens": MAX_SORTIE, "reasoning_effort": effort, "store": False}
    if SERVICE_TIER[palier] is not None:
        c["service_tier"] = SERVICE_TIER[palier]
    return json.dumps(c, ensure_ascii=False)


def prix_valides(prix: dict) -> dict:
    for k in ("entree", "sortie", "cache"):
        v = prix.get(k)
        if type(v) not in (int, float) or not math.isfinite(v) or v <= 0:
            raise Refus(f"prix {k} invalide : {v!r} (USD par million de jetons, strictement positif)")
    if prix["cache"] > prix["entree"]:
        raise Refus("prix du cache au-dessus du prix d'entrée")
    if not isinstance(prix.get("source"), str) or not prix["source"].strip():
        raise Refus("source des prix non dite (page lue, date, empreinte)")
    return prix


def pire_cas_usd(octets: int, prix: dict) -> float:
    """Pire cas d'un appel : un jeton d'entrée par octet du corps (+ 1 024), plafond de sortie entier."""
    return (octets + OCTETS_MARGE) * prix["entree"] / 1e6 + MAX_SORTIE * prix["sortie"] / 1e6


def nombre_fini(x) -> bool:
    return type(x) in (int, float) and math.isfinite(x)


def prix_du_palier(racine, palier) -> dict:
    """Prix lus (C2) : constantes du code, revérifiées dans la pièce épinglée `prix-astra-v2.md` (empreinte, ligne du
    tableau du palier). Aucun prix n'est pris d'une option en ligne de commande."""
    if palier not in PALIERS:
        raise Refus(f"palier {palier!r} hors de {PALIERS}")
    rel, attendue = PIECES_PRIX["prix"]
    p = Path(racine) / rel
    if not p.is_file():
        raise Refus(f"pièce des prix absente : {rel}")
    h = sha256_fichier(p)
    if h != attendue:
        raise Refus(f"pièce des prix ({rel}) : empreinte {h[:12]}… ≠ épinglée {attendue[:12]}…")
    if LIGNES_SOURCE_PRIX[palier] not in p.read_text(encoding="utf-8"):
        raise Refus(f"pièce des prix : ligne du palier {palier} introuvable ({LIGNES_SOURCE_PRIX[palier]})")
    return {**PRIX_LUS[palier], "source": SOURCE_PRIX}


def racine_du_dossier(dossier) -> Path:
    """C6 : le seul dossier d'envois accepté est `<racine>/DOSSIER_ENVOIS_REL` ; rend la racine."""
    d = Path(dossier).resolve()
    parties = tuple(DOSSIER_ENVOIS_REL.split("/"))
    if d.parts[-len(parties):] != parties:
        raise Refus(f"{dossier} : seul <racine>/{DOSSIER_ENVOIS_REL} est accepté (C6 : un seul dossier d'envois)")
    return d.parents[len(parties) - 1]


def verifier_unicite(racine, attendu) -> None:
    """C6 : sous `docs/` et `runs/` de la racine, aucun autre manifeste d'envois v3 (v3 ou v3.1) que `attendu` (ou
    aucun, à la préparation). Une seconde préparation, même ailleurs, est refusée : la dépense ne repart jamais de zéro."""
    racine = Path(racine).resolve()
    trouves = sorted(p.resolve() for base in ("docs", "runs") if (racine / base).is_dir()
                     for p in (racine / base).rglob("manifeste-envois-v3*.json"))
    voulus = [] if attendu is None else [Path(attendu).resolve()]
    if trouves != voulus:
        autres = [str(p.relative_to(racine)) if p.is_relative_to(racine) else str(p) for p in trouves if p not in voulus]
        raise Refus("C6 : un seul dossier d'envois v3 par lecture ; trouvés : " + (", ".join(autres) or "aucun")
                    + (" ; attendu : " + str(voulus[0]) if voulus and voulus[0] not in trouves else ""))


def preparer(fiches_chemin, attestation_chemin, sortie, racine=RACINE_DEFAUT, *, effort, plafond_usd,
             depense_anterieure_usd, palier="standard") -> dict:
    racine = Path(racine)
    sortie = Path(sortie)
    if sortie.resolve() != (racine.resolve() / DOSSIER_ENVOIS_REL):
        raise Refus(f"{sortie} : seul <racine>/{DOSSIER_ENVOIS_REL} est accepté (C6 : un seul dossier d'envois)")
    if sortie.exists() and any(sortie.iterdir()):
        raise Refus(f"{sortie} existe et n'est pas vide : on n'écrase jamais (R12) ; une seconde préparation est un nœud (C6)")
    verifier_unicite(racine, None)
    if effort not in EFFORTS:
        raise Refus(f"effort de raisonnement {effort!r} hors de {EFFORTS}")
    prix = prix_valides(prix_du_palier(racine, palier))
    if not nombre_fini(depense_anterieure_usd) or depense_anterieure_usd < 0:
        raise Refus(f"dépense antérieure invalide : {depense_anterieure_usd!r} (USD comptés depuis le devis, au moins 0)")
    disponible = PLAFOND_ABSOLU_USD - depense_anterieure_usd
    if not nombre_fini(plafond_usd) or plafond_usd <= 0:
        raise Refus(f"plafond invalide : {plafond_usd!r}")
    if plafond_usd > disponible + 1e-9:
        raise Refus(f"plafond {plafond_usd} USD > {PLAFOND_ABSOLU_USD} (reste du GO-2026-11-13-06) moins la dépense "
                    f"antérieure {depense_anterieure_usd} (C4)")
    pieces, empreintes = {}, {}
    for nom in PIECES:
        pieces[nom], empreintes[nom] = lire_piece(racine, nom)
    prov = verifier_fiches_de_run(racine, fiches_chemin)
    sha_fiches = prov["sha256"]
    att = verifier_attestation(attestation_chemin, sha_fiches)
    sha_att = sha256_fichier(attestation_chemin)
    fiches = json.loads((racine / prov["chemin"]).read_text(encoding="utf-8"))
    verifier_forme_fiches_validees(fiches)
    if not fiches:
        raise Refus("aucune fiche validée (E1) : rien à lire")
    pile = construire_pile(fiches, json.loads(pieces["temoins_lecteur"]), json.loads(pieces["temoins_hasard"]))
    if not any(p["origine"] == "reelle" for p in pile["fiches"]):
        raise Refus("aucune fiche réelle admissible (E1) : rien n'est envoyé")
    n = len(pile["fiches"])
    ordres = ordres_lectures(n)
    lots_idx = decouper_lots(n)
    appels = len(LECTURES) * len(lots_idx)
    if appels > MAX_APPELS:
        raise Refus(f"{appels} appels > {MAX_APPELS} fixés d'avance (pile de {n} fiches, lots de {TAILLE_LOT})")
    messages, cle = {}, {}
    for L in LECTURES:
        ordre = ordres[L]
        etiquettes = {etiquette(r): pile["fiches"][i]["id"] for r, i in enumerate(ordre)}
        lots = []
        for k, idx in enumerate(lots_idx, 1):
            lot = [(etiquette(r), pile["fiches"][ordre[r]]["vue"]) for r in idx]
            messages[(L, k)] = texte_message(pieces, lot, k, len(lots_idx))
            lots.append([etiquette(r) for r in idx])
        cle[L] = {"ordre": [pile["fiches"][i]["id"] for i in ordre], "etiquettes": etiquettes, "lots": lots}
    corps = {Lk: corps_requete(msg, effort, palier) for Lk, msg in messages.items()}
    garde = []
    for (L, k) in sorted(corps):
        o = len(corps[(L, k)].encode("utf-8"))
        garde.append({"envoi": f"envoi-{L}-lot{k}-{SUFFIXE}.corps.json", "lecture": L, "lot": k, "octets": o,
                      "pire_cas_usd": round(pire_cas_usd(o, prix), 6)})
    plus_gros = max(g["pire_cas_usd"] for g in garde)
    if plus_gros > plafond_usd:
        raise Refus(f"plafond {plafond_usd} USD sous le pire cas d'un seul appel ({plus_gros:.4f}) : aucun appel ne tiendrait")
    total = sum(g["pire_cas_usd"] for g in garde)
    surs, cumul = 0, 0.0
    for g in garde:  # appels que le plafond paie même si chacun coûte son pire cas
        if cumul + g["pire_cas_usd"] > plafond_usd:
            break
        cumul += g["pire_cas_usd"]
        surs += 1
    sortie.mkdir(parents=True, exist_ok=True)
    fichiers = {}
    for (L, k) in sorted(messages):
        nom_m, nom_c = f"envoi-{L}-lot{k}-{SUFFIXE}.txt", f"envoi-{L}-lot{k}-{SUFFIXE}.corps.json"
        fichiers[nom_m] = ecrire_scelle(sortie / nom_m, messages[(L, k)])
        fichiers[nom_c] = ecrire_scelle(sortie / nom_c, corps[(L, k)])
    fichiers[PILE] = ecrire_scelle(sortie / PILE, json_texte(pile))
    fichiers[CLE_LECTURES] = ecrire_scelle(sortie / CLE_LECTURES, json_texte(cle))
    e = enfants_ordres()
    manifeste = {
        "version": VERSION, "outil_sha256": sha256_fichier(__file__), "prepare_le": maintenant(),
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__},
        "dossier_envois": DOSSIER_ENVOIS_REL, "palier": palier,
        "pieces": {k: {"chemin": PIECES[k][0], "sha256": v} for k, v in empreintes.items()},
        "piece_prix": {"chemin": PIECES_PRIX["prix"][0], "sha256": PIECES_PRIX["prix"][1]},
        "fiches_validees": {**prov, "nombre": len(fiches)},
        "attestation": {"chemin": str(attestation_chemin), "sha256": sha_att, "lecteur": att["lecteur"],
                        "lu_le": att["lu_le"]},
        "graines": {"entropie": ENTROPIE_ORDRES, "methode": "numpy.random.SeedSequence(2026111302).spawn(4)",
                    "enfants": {"ordre_L1": list(e[0].spawn_key), "ordre_L2": list(e[1].spawn_key),
                                "departage": list(e[2].spawn_key), "temoin_permute": list(e[3].spawn_key)}},
        "pile": {"fiches": n, "reelles_admissibles": sum(p["origine"] == "reelle" for p in pile["fiches"]),
                 "temoins": sum(p["origine"] == "temoin" for p in pile["fiches"]),
                 "hors_question": len(pile["hors_question"]), "champs_retires": pile["champs_retires"]},
        "lots": {"taille_lot": TAILLE_LOT, "nombre_par_lecture": len(lots_idx), "tailles": [len(x) for x in lots_idx]},
        "lecteur": lecteur_attendu(effort, palier),
        "garde_depense": {"prix_usd_par_million": prix, "plafond_usd": plafond_usd,
                          "depense_anterieure_usd": depense_anterieure_usd, "plafond_disponible_usd": round(disponible, 6),
                          "appels_max": appels, "pire_cas_total_usd": round(total, 6), "appels_surs_au_pire_cas": surs,
                          "regle": "avant chaque appel : dépense comptée + pire cas de l'appel ≤ plafond, sinon arrêt ; "
                                   "après : coût lu dans usage, pire cas si usage absent, illisible ou incohérent",
                          "envois": garde},
        "ordre_d_envoi": [g["envoi"] for g in garde],
        "reponses_attendues": [f"reponse-{L}-lot{k}-{SUFFIXE}.json" for L in LECTURES for k in range(1, len(lots_idx) + 1)],
        "fichiers": fichiers,
        "jamais_envoyes": [PILE, CLE_LECTURES, MANIFESTE, JOURNAL],
    }
    ecrire_scelle(sortie / MANIFESTE, json_texte(manifeste))
    return manifeste


# --- envoi : relais en processus, clé, garde de dépense --------------------------------------------------------------

def lire_cle() -> str:
    """La clé, lue par son nom seul, puis retirée de l'environnement du processus. Jamais affichée ni écrite. B1 : vide,
    ou portant un caractère hors de l'ASCII imprimable (retour chariot, saut de ligne, espace, tabulation…), elle est
    refusée sans être montrée, avant tout journal et tout envoi."""
    cle = os.environ.pop(VARIABLE_CLE, None)
    if not cle:
        raise Refus(f"{VARIABLE_CLE} absente ou vide : rien n'est envoyé")
    if not MOTIF_CLE.fullmatch(cle):
        raise Refus(f"{VARIABLE_CLE} : caractère hors de l'ASCII imprimable (fin de ligne, espace…) ; clé refusée sans "
                    "être affichée ; rien n'est envoyé")
    return cle


def formes_de_cle(cle: str) -> list[bytes]:
    """B1 : la clé et ses formes échappées (JSON, barre oblique échappée, pourcentage, repr), les plus longues d'abord."""
    j = json.dumps(cle)[1:-1]
    formes = {cle, j, cle.replace("/", "\\/"), j.replace("/", "\\/"), urllib.parse.quote(cle, safe=""), repr(cle)[1:-1]}
    return sorted({f.encode("utf-8") for f in formes if f}, key=len, reverse=True)


def contient_cle(octets: bytes, cle: str) -> bool:
    return any(f in octets for f in formes_de_cle(cle))


def expurger(octets: bytes, cle: str) -> tuple[bytes, bool]:
    """Remplace toute forme de la clé par `[cle]` ; rend (octets, vrai si une forme a été trouvée)."""
    trouve = False
    for f in formes_de_cle(cle):
        if f in octets:
            octets, trouve = octets.replace(f, b"[cle]"), True
    return octets, trouve


class ErreurTransport(Exception):
    """Issue de transport refusée (adresse finale autre que l'adresse demandée)."""


class SansRedirection(urllib.request.HTTPRedirectHandler):
    """B2 : aucune redirection n'est suivie ; un statut 3xx revient tel quel (anomalie bloquante), et l'en-tête
    d'autorisation ne part jamais vers une autre adresse que celle d'OpenAI."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def transport_reel(url: str, entetes: dict, corps: bytes, delai: float) -> tuple[int, bytes]:
    """Un seul POST vers l'adresse d'OpenAI, sans reprise ni redirection (B2). Mandataire de l'environnement (urllib :
    en HTTPS, l'en-tête d'autorisation passe dans le tunnel, jamais au mandataire), certificats de SSL_CERT_FILE."""
    if url != URL_AMONT:
        raise Refus("adresse d'amont autre que celle d'OpenAI : refusée")
    ca = os.environ.get("SSL_CERT_FILE")
    contexte = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
    ouvreur = urllib.request.build_opener(SansRedirection, urllib.request.HTTPSHandler(context=contexte))
    req = urllib.request.Request(url, data=corps, method="POST", headers=entetes)
    try:
        with ouvreur.open(req, timeout=delai) as r:
            if r.geturl() != url:
                raise ErreurTransport("adresse finale différente de l'adresse demandée")
            return r.status, r.read(TAILLE_MAX_REPONSE + 1)
    except urllib.error.HTTPError as e:
        return e.code, e.read(TAILLE_MAX_REPONSE + 1)


def entier(x) -> bool:
    return type(x) is int and x >= 0


def cout_usage(usage, prix: dict, octets_envoyes: int = 0, octets_contenu: int = 0):
    """(coût en USD, problème, jetons lus). Coût None si l'usage est absent ou illisible (le pire cas s'applique).
    Règle : (prompt − cache) × entrée + cache × prix du cache + completion × sortie + excédent de total × prix le plus
    haut. `completion_tokens` compte le raisonnement (`completion_tokens_details.reasoning_tokens` en est une part :
    SUPPOSÉ, vérifié sur la première réponse, C3). M4 : usage incohérent, compté au pire cas, si le cache dépasse
    l'entrée, le raisonnement la sortie, la sortie le plafond demandé, si le total est sous la somme, si l'entrée est
    sous un plancher (octets du corps / 16) ou la sortie visible (sortie − raisonnement) sous un plancher (octets du
    contenu rendu / 16, au moins 1 dès que le contenu n'est pas vide)."""
    if not isinstance(usage, dict):
        return None, "usage absent", {}
    p, c = usage.get("prompt_tokens"), usage.get("completion_tokens")
    if not entier(p) or not entier(c):
        return None, "usage illisible (prompt_tokens ou completion_tokens)", {}
    ptd, ctd = usage.get("prompt_tokens_details"), usage.get("completion_tokens_details")
    if (ptd is not None and not isinstance(ptd, dict)) or (ctd is not None and not isinstance(ctd, dict)):
        return None, "usage illisible (détails non objets)", {}
    cache = (ptd or {}).get("cached_tokens")
    raison = (ctd or {}).get("reasoning_tokens")
    total = usage.get("total_tokens")
    cache, raison, total = (0 if cache is None else cache), (0 if raison is None else raison), (p + c if total is None
                                                                                                 else total)
    if not entier(cache) or not entier(raison) or not entier(total):
        return None, "usage illisible (détails)", {}
    lus = {"prompt_tokens": p, "cached_tokens": cache, "completion_tokens": c, "reasoning_tokens": raison,
           "total_tokens": total}
    plancher_entree = octets_envoyes // PLANCHER_OCTETS_PAR_JETON
    plancher_visible = -(-octets_contenu // PLANCHER_OCTETS_PAR_JETON)
    probleme = None
    if cache > p:
        probleme = "jetons en cache au-dessus des jetons d'entrée"
    elif raison > c:
        probleme = "jetons de raisonnement au-dessus des jetons de sortie"
    elif c > MAX_SORTIE:
        probleme = f"jetons de sortie au-dessus du plafond demandé ({MAX_SORTIE})"
    elif total < p + c:
        probleme = "total_tokens sous la somme des jetons d'entrée et de sortie"
    elif p < plancher_entree:
        probleme = f"jetons d'entrée sous le plancher ({plancher_entree} pour {octets_envoyes} octets envoyés)"
    elif c - raison < plancher_visible:
        probleme = f"jetons de sortie visibles sous le plancher ({plancher_visible} pour {octets_contenu} octets rendus)"
    exces = max(0, total - p - c)
    haut = max(prix["entree"], prix["sortie"])
    cout = ((p - min(cache, p)) * prix["entree"] + min(cache, p) * prix["cache"] + c * prix["sortie"]
            + exces * haut + (max(0, raison - c) * prix["sortie"])) / 1e6
    return cout, probleme, lus


def champ_court(x) -> str | None:
    """Type ou code d'erreur du fournisseur, gardé seulement s'il a la forme d'un code (minuscules et soulignés) : un
    identifiant de compte, d'organisation ou de clé n'est jamais écrit."""
    return x if isinstance(x, str) and re.fullmatch(r"[a-z_]{1,64}", x) else None


def analyser_reponse(statut, corps, pire_cas: float, prix: dict, octets_envoyes: int = 0,
                     palier: str = "standard") -> dict:
    """Lit une réponse de l'amont (statut, octets) sans lever : toute forme inattendue est une anomalie (M3). Rend
    {cout_usd, au_pire_cas, anomalies, modele_servi, palier_servi, finish_reason, jetons, erreur, statut, corps_sha256}.
    Le corps d'une réponse 200 a déjà été écrit, brut, par `envoyer` ; pour un autre statut, seuls le type et le code
    d'erreur filtrés sont gardés (jamais le corps)."""
    r = {"cout_usd": pire_cas, "au_pire_cas": True, "anomalies": [], "modele_servi": None, "palier_servi": None,
         "finish_reason": None, "jetons": {}, "erreur": None, "statut": statut,
         "corps_sha256": sha256_octets(corps) if corps is not None else None}
    if statut is None:
        r["anomalies"].append("transport_echec")
        return r
    corps = corps if corps is not None else b""
    if len(corps) > TAILLE_MAX_REPONSE:
        r["anomalies"].append("reponse_trop_grande")
        return r
    try:
        o = json.loads(corps.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        o = None
    if statut != 200:
        err = o.get("error") if isinstance(o, dict) else None
        err = err if isinstance(err, dict) else {}
        r["erreur"] = {"type": champ_court(err.get("type")), "code": champ_court(err.get("code"))}
        r["anomalies"].append("statut_non_200")
        if 300 <= statut < 400:
            r["anomalies"].append("redirection_refusee")
        return r
    if not isinstance(o, dict):
        r["anomalies"].append("reponse_illisible")
        return r
    r["modele_servi"] = o.get("model") if isinstance(o.get("model"), str) else None
    r["palier_servi"] = o.get("service_tier") if isinstance(o.get("service_tier"), str) else None
    ch = o.get("choices")
    c0 = ch[0] if isinstance(ch, list) and len(ch) >= 1 and isinstance(ch[0], dict) else {}
    msg = c0.get("message") if isinstance(c0.get("message"), dict) else {}
    texte = msg.get("content") if isinstance(msg.get("content"), str) else ""
    cout, probleme, lus = cout_usage(o.get("usage"), prix, octets_envoyes, len(texte.encode("utf-8")))
    r["jetons"] = lus
    if cout is None:
        r["anomalies"].append("usage_absent")
    elif probleme:
        r["anomalies"].append("usage_incoherent")
        r["probleme_usage"] = probleme
        r["cout_usd"], r["au_pire_cas"] = max(cout, pire_cas), cout <= pire_cas
    else:
        r["cout_usd"], r["au_pire_cas"] = cout, False
        if cout > pire_cas + 1e-12:
            r["anomalies"].append("cout_au_dessus_du_pire_cas")
    if o.get("object") != "chat.completion":
        r["anomalies"].append("reponse_illisible")
    if r["modele_servi"] != MODELE_LECTEUR:
        r["anomalies"].append("modele_servi_different")
    if (o.get("service_tier") not in PALIERS_SERVIS_ADMIS[palier]
            or (o.get("service_tier") is not None and r["palier_servi"] is None)):
        r["anomalies"].append("palier_servi_different")
    if not isinstance(ch, list) or len(ch) != 1 or not isinstance(ch[0], dict):
        r["anomalies"].append("choix_non_unique")
        return r
    r["finish_reason"] = c0.get("finish_reason") if isinstance(c0.get("finish_reason"), str) else None
    if r["finish_reason"] != "stop":
        r["anomalies"].append("fin_non_stop")
    if msg.get("refusal"):
        r["anomalies"].append("refus_du_lecteur")
    if not isinstance(msg.get("content"), str) or not msg["content"].strip():
        r["anomalies"].append("contenu_absent")
    return r


def lire_journal(dossier) -> dict:
    """Relit le journal de dépense chaîné (chaque ligne porte l'empreinte de la précédente). Rend la dépense comptée (un
    envoi sans clôture compte son pire cas), les appels, les envois, réceptions et clôtures, les anomalies et l'arrêt."""
    p = Path(dossier) / JOURNAL
    etat = {"appels": 0, "depense_usd": 0.0, "envois": {}, "recus": {}, "clos": {}, "en_vol": [], "anomalies": [],
            "arret": None, "lignes": 0, "dernier_sha256": "debut"}
    if not p.exists():
        return etat
    ouverts = {}
    for i, brute in enumerate(p.read_bytes().splitlines(keepends=True)):
        try:
            ev = json.loads(brute.decode("utf-8"))
        except ValueError as e:
            raise Refus(f"{JOURNAL} ligne {i + 1} illisible") from e
        if not isinstance(ev, dict) or ev.get("n") != i + 1 or ev.get("precedent") != etat["dernier_sha256"]:
            raise Refus(f"{JOURNAL} ligne {i + 1} : chaîne rompue (journal tronqué ou réécrit)")
        etat["dernier_sha256"] = sha256_octets(brute)
        etat["lignes"] = i + 1
        g = ev.get("evenement")
        if g in ("envoi", "recu", "clos") and not isinstance(ev.get("envoi"), str):
            raise Refus(f"{JOURNAL} ligne {i + 1} : envoi non nommé")
        if g == "envoi":
            if ev["envoi"] in ouverts or ev["envoi"] in etat["clos"]:
                raise Refus(f"{JOURNAL} : {ev['envoi']} envoyé deux fois")
            if not nombre_fini(ev.get("pire_cas_usd")) or ev["pire_cas_usd"] < 0:
                raise Refus(f"{JOURNAL} ligne {i + 1} : pire cas illisible")
            etat["appels"] += 1
            ouverts[ev["envoi"]] = ev
            etat["envois"][ev["envoi"]] = ev
        elif g == "recu":
            if ev["envoi"] not in ouverts or ev["envoi"] in etat["recus"]:
                raise Refus(f"{JOURNAL} : réception sans envoi ouvert ({ev['envoi']})")
            etat["recus"][ev["envoi"]] = ev
        elif g == "clos":
            if ev["envoi"] not in ouverts:
                raise Refus(f"{JOURNAL} : clôture sans envoi ({ev['envoi']})")
            if not nombre_fini(ev.get("cout_usd")) or ev["cout_usd"] < 0 or not isinstance(ev.get("anomalies"), list):
                raise Refus(f"{JOURNAL} ligne {i + 1} : clôture illisible")
            ouverts.pop(ev["envoi"])
            etat["clos"][ev["envoi"]] = ev
            etat["depense_usd"] += ev["cout_usd"]
            etat["anomalies"] += [{"envoi": ev["envoi"], "genre": a} for a in ev["anomalies"]]
        elif g == "arret":
            etat["arret"] = ev
        else:
            raise Refus(f"{JOURNAL} ligne {i + 1} : événement inconnu {g!r}")
    for nom, ev in ouverts.items():  # appel parti sans clôture (coupure) : pire cas, et la lecture ne reprend pas
        etat["en_vol"].append(nom)
        etat["depense_usd"] += ev["pire_cas_usd"]
    return etat


def ajouter_journal(dossier, etat: dict, ev: dict, cle: str | None = None) -> None:
    ev = {"n": etat["lignes"] + 1, "precedent": etat["dernier_sha256"], "utc": maintenant(), **ev}
    ligne = (json.dumps(ev, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")
    if cle:
        ligne, _ = expurger(ligne, cle)  # B1 : un champ rendu par l'amont ne porte jamais la clé au journal
    with open(Path(dossier) / JOURNAL, "ab") as f:
        f.write(ligne)
        f.flush()
        os.fsync(f.fileno())
    etat["lignes"] += 1
    etat["dernier_sha256"] = sha256_octets(ligne)


def nom_reponse(envoi: str) -> str:
    return envoi.replace("envoi-", "reponse-").replace(f"-{SUFFIXE}.corps.json", f"-{SUFFIXE}.json")


def nom_erreur(envoi: str) -> str:
    return envoi.replace("envoi-", "erreur-").replace(f"-{SUFFIXE}.corps.json", f"-{SUFFIXE}.json")


def controler_coherence(dossier, man: dict, j: dict) -> None:
    """M1 : chaque fichier nommé par une réception ou une clôture du journal existe, scellé, à la même empreinte ; et
    chaque réponse ou erreur présente dans le dossier est nommée par le journal. Sinon, refus."""
    refs = {}
    for ev in list(j["recus"].values()) + list(j["clos"].values()):
        nom, h = ev.get("fichier"), ev.get("fichier_sha256")
        if nom is None:
            continue
        if not isinstance(nom, str) or "/" in nom or (nom in refs and refs[nom] != h):
            raise Refus(f"{JOURNAL} : fichier {nom!r} nommé deux fois à des empreintes différentes")
        refs[nom] = h
    for nom, h in refs.items():
        if not (Path(dossier) / nom).exists() or verifier_sceau(Path(dossier) / nom) != h:
            raise Refus(f"{nom} : nommé au journal mais absent ou à une autre empreinte (journal ou dossier altéré)")
    for g in man["garde_depense"]["envois"]:
        for nom in (nom_reponse(g["envoi"]), nom_erreur(g["envoi"])):
            if (Path(dossier) / nom).exists() and nom not in refs:
                raise Refus(f"{nom} sans clôture conforme au journal (journal tronqué ou fichier étranger)")


def valider_manifeste(man: dict, dossier) -> tuple[dict, float, int, str]:
    """D6, D7, m1 : à l'envoi, le manifeste (même rescellé) est revérifié contre les bornes et les prix du code, et chaque
    corps contre son pire cas et ses paramètres ; rend (prix, plafond, appels_max, palier)."""
    palier = man.get("palier")
    if palier not in PALIERS:
        raise Refus(f"manifeste : palier {palier!r} hors de {PALIERS}")
    g = man.get("garde_depense") if isinstance(man.get("garde_depense"), dict) else {}
    prix = g.get("prix_usd_par_million")
    if prix != {**PRIX_LUS[palier], "source": SOURCE_PRIX}:
        raise Refus(f"manifeste : prix autres que les prix lus du palier {palier} (prix-astra-v2.md)")
    anterieure, plafond, appels_max = g.get("depense_anterieure_usd"), g.get("plafond_usd"), g.get("appels_max")
    envois = g.get("envois") if isinstance(g.get("envois"), list) else []
    if not nombre_fini(anterieure) or anterieure < 0:
        raise Refus("manifeste : dépense antérieure invalide")
    if not nombre_fini(plafond) or plafond <= 0 or plafond > PLAFOND_ABSOLU_USD - anterieure + 1e-9:
        raise Refus("manifeste : plafond hors des bornes du code (C4)")
    if type(appels_max) is not int or appels_max > MAX_APPELS or appels_max != len(envois):
        raise Refus("manifeste : nombre d'appels hors des bornes du code")
    lecteur = man.get("lecteur") if isinstance(man.get("lecteur"), dict) else {}
    effort = lecteur.get("reasoning_effort")
    if effort not in EFFORTS or lecteur != lecteur_attendu(effort, palier):
        raise Refus("manifeste : lecteur autre que celui du code (modèle, adresse, plafond de sortie, effort, palier)")
    if man.get("ordre_d_envoi") != [e.get("envoi") for e in envois if isinstance(e, dict)] or not envois:
        raise Refus("manifeste : ordre d'envoi incohérent")
    for e in envois:
        p = Path(dossier) / e["envoi"]
        corps = p.read_bytes() if p.is_file() else b""
        if len(corps) != e.get("octets") or e.get("pire_cas_usd") != round(pire_cas_usd(len(corps), prix), 6):
            raise Refus(f"manifeste : {e['envoi']} : octets ou pire cas différents du corps et des prix")
        try:
            c = json.loads(corps.decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as ex:
            raise Refus(f"{e['envoi']} : corps illisible") from ex
        attendu = {"model", "messages", "max_completion_tokens", "reasoning_effort", "store"} | (
            {"service_tier"} if SERVICE_TIER[palier] is not None else set())
        if (not isinstance(c, dict) or set(c) != attendu or c["model"] != MODELE_LECTEUR
                or c["max_completion_tokens"] != MAX_SORTIE or c["reasoning_effort"] != effort or c["store"] is not False
                or c.get("service_tier") != SERVICE_TIER[palier] or not isinstance(c["messages"], list)
                or len(c["messages"]) != 1 or c["messages"][0].get("role") != "user"):
            raise Refus(f"{e['envoi']} : paramètres du corps autres que ceux du manifeste")
    return prix, plafond, appels_max, palier


def bilan(dossier) -> dict:
    """C3 et C5 : état du journal, sans clé ; refus si une réponse ou une erreur n'a pas sa clôture conforme."""
    env = charger_envois(dossier)
    man = env["manifeste"]
    j = lire_journal(dossier)
    controler_coherence(dossier, man, j)
    attendus = len(man["garde_depense"]["envois"])
    clotures = [{**{k: ev.get(k) for k in ("envoi", "statut", "modele_servi", "palier_servi", "finish_reason", "jetons",
                                          "cout_usd", "au_pire_cas", "anomalies")},
                 "pire_cas_usd": j["envois"][nom]["pire_cas_usd"]} for nom, ev in j["clos"].items()]
    return {"appels": j["appels"], "appels_max": man["garde_depense"]["appels_max"],
            "depense_comptee_usd": round(j["depense_usd"], 6), "plafond_usd": man["garde_depense"]["plafond_usd"],
            "palier": man.get("palier"), "clos": len(j["clos"]), "attendus": attendus, "en_vol": j["en_vol"],
            "anomalies": j["anomalies"], "arret": (j["arret"] or {}).get("motif"), "clotures": clotures,
            "pret_pour_verifier": (len(j["clos"]) == attendus and not j["en_vol"] and not j["anomalies"]
                                   and j["arret"] is None)}


def envoyer(dossier, transport=None, envois_max=None) -> dict:
    """Envoie les lots dans l'ordre du manifeste, un à la fois, sous la garde de dépense ; s'arrête au premier écart.
    Rend {issue: fait|pause|anomalie|plafond, …}. Toute réponse 200 est écrite brute et scellée avant son analyse (M3) ;
    toute autre issue laisse un fichier d'erreur scellé sans le corps."""
    transport = transport or transport_reel
    env = charger_envois(dossier)
    man = env["manifeste"]
    if man.get("version") != VERSION:
        raise Refus(f"envois préparés par {man.get('version')!r}, pas par {VERSION}")
    prix, plafond, appels_max, palier = valider_manifeste(man, dossier)
    g = man["garde_depense"]
    j = lire_journal(dossier)
    controler_coherence(dossier, man, j)
    if j["en_vol"]:
        raise Refus(f"appel sans clôture au journal ({', '.join(j['en_vol'])}) : compté au pire cas ; aucune reprise")
    if j["anomalies"] or j["arret"]:
        raise Refus("lecture déjà arrêtée (anomalie ou plafond consignés) : aucun envoi, aucune relecture")
    a_faire = [e for e in g["envois"] if e["envoi"] not in j["clos"]]
    if not a_faire:
        return {"issue": "fait", "appels": j["appels"], "depense_comptee_usd": round(j["depense_usd"], 6)}
    cle = lire_cle()
    entetes = {"Content-Type": "application/json", "Authorization": "Bearer " + cle}
    envoyes, issue, detail = 0, "fait", None
    for e in a_faire:
        if envois_max is not None and envoyes >= envois_max:
            issue = "pause"
            break
        if j["appels"] >= appels_max:
            issue, detail = "plafond", f"nombre d'appels {appels_max} atteint"
            ajouter_journal(dossier, j, {"evenement": "arret", "motif": "appels", "detail": detail}, cle)
            break
        corps = (Path(dossier) / e["envoi"]).read_bytes()
        if sha256_octets(corps) != man["fichiers"][e["envoi"]]:
            raise Refus(f"{e['envoi']} : corps différent du manifeste")
        pire = max(e["pire_cas_usd"], pire_cas_usd(len(corps), prix))  # recalculé sur les octets envoyés
        if j["depense_usd"] + pire > plafond + 1e-12:
            issue = "plafond"
            detail = (f"{e['envoi']} : dépense comptée {j['depense_usd']:.6f} + pire cas {pire:.6f} "
                      f"> plafond {plafond}")
            ajouter_journal(dossier, j, {"evenement": "arret", "motif": "plafond", "detail": detail}, cle)
            break
        ajouter_journal(dossier, j, {"evenement": "envoi", "envoi": e["envoi"], "octets": len(corps),
                                     "pire_cas_usd": pire}, cle)
        envoyes += 1
        try:
            statut, rep = transport(URL_AMONT, entetes, corps, DELAI_S)
            cause = None
        except Refus:
            raise
        except Exception as ex:  # coupure, délai, mandataire, en-tête refusé : pire cas ; seul le type est gardé (B1)
            statut, rep, cause = None, None, type(ex).__name__
        nom, h, expurgee = None, None, False
        if statut == 200 and rep is not None and len(rep) <= TAILLE_MAX_REPONSE:
            # M3 : la réponse payée est écrite brute (le corps seul, sans en-têtes ; la clé expurgée si l'amont la
            # renvoie, B1), scellée et consignée avant toute analyse.
            brut, expurgee = expurger(rep, cle)
            nom = nom_reponse(e["envoi"])
            h = ecrire_scelle_octets(Path(dossier) / nom, brut)
            ajouter_journal(dossier, j, {"evenement": "recu", "envoi": e["envoi"], "fichier": nom, "fichier_sha256": h,
                                         "brut_sha256": sha256_octets(rep), "octets": len(rep),
                                         "cle_expurgee": expurgee}, cle)
        try:
            a = analyser_reponse(statut, rep, pire, prix, len(corps), palier)
        except Exception as ex:  # filet déclaré : l'analyse ne doit pas lever ; anomalie bloquante, pire cas
            a = {"cout_usd": pire, "au_pire_cas": True, "anomalies": ["analyse_en_echec"], "modele_servi": None,
                 "palier_servi": None, "finish_reason": None, "jetons": {}, "erreur": None, "statut": statut,
                 "corps_sha256": sha256_octets(rep) if rep is not None else None, "cause_analyse": type(ex).__name__}
        if expurgee:
            a["anomalies"].append("cle_dans_la_reponse")
        if nom is None:
            nom = nom_erreur(e["envoi"])
            texte = json_texte({
                "envoi": e["envoi"], "statut": statut, "erreur": a["erreur"], "corps_sha256": a["corps_sha256"],
                "corps_octets": len(rep) if rep is not None else None, "cause_transport": cause,
                "anomalies": a["anomalies"],
                "note": "corps de l'amont jamais écrit (il peut porter des identifiants du compte)"})
            h = ecrire_scelle_octets(Path(dossier) / nom, expurger(texte.encode("utf-8"), cle)[0])
        ev = {"evenement": "clos", "envoi": e["envoi"], "statut": statut, "fichier": nom, "fichier_sha256": h,
              "modele_servi": a["modele_servi"], "palier_servi": a["palier_servi"], "finish_reason": a["finish_reason"],
              "jetons": a["jetons"], "cout_usd": round(a["cout_usd"], 6), "au_pire_cas": a["au_pire_cas"],
              "anomalies": a["anomalies"]}
        ajouter_journal(dossier, j, ev, cle)
        j = lire_journal(dossier)  # dépense et appels recomptés depuis le journal écrit
        if a["anomalies"]:
            issue, detail = "anomalie", f"{e['envoi']} : {', '.join(a['anomalies'])}"
            break
    del cle, entetes
    releve = {"version": VERSION, "fin_utc": maintenant(), "issue": issue, "detail": detail,
              "envoyes_cette_fois": envoyes, "appels": j["appels"], "appels_max": appels_max,
              "depense_comptee_usd": round(j["depense_usd"], 6), "plafond_usd": plafond, "palier": palier,
              "journal_sha256": sha256_fichier(Path(dossier) / JOURNAL)}
    k = 1
    while (Path(dossier) / f"releve-depense-{SUFFIXE}-{k}.json").exists():
        k += 1
    ecrire_scelle(Path(dossier) / f"releve-depense-{SUFFIXE}-{k}.json", json_texte(releve))
    return releve


# --- vérification --------------------------------------------------------------------------------------------------------

def espaces(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def feuilles(o) -> list[str]:
    if isinstance(o, str):
        return [o]
    if isinstance(o, list):
        return [t for x in o for t in feuilles(x)]
    if isinstance(o, dict):
        return [t for v in o.values() for t in feuilles(v)]
    return []


def court(passage) -> bool:
    return isinstance(passage, str) and len(re.sub(r"\s", "", passage)) < LONGUEUR_MIN_PASSAGE


def passage_dans(passage, textes) -> tuple[bool, str]:
    if not isinstance(passage, str):
        return False, "passage absent ou non textuel"
    p = espaces(passage)
    if court(p):  # passage vide compris
        return False, f"passage trop court (moins de {LONGUEUR_MIN_PASSAGE} caractères hors espaces)"
    # la fiche est servie en JSON : un passage recopié avec ses échappements (\" ou \\) est aussi « mot pour mot »
    formes = {p, espaces(p.replace('\\"', '"').replace("\\\\", "\\"))}
    if any(f in espaces(t) for f in formes for t in textes):
        return True, "mot pour mot"
    return False, "passage introuvable mot pour mot"


def entrees_catalogue(texte: str) -> dict:
    """{Ck: [cellules de la ligne du tableau, marques ** retirées]}."""
    entrees = {}
    for ligne in texte.splitlines():
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if cellules and cellules[0] in CODES_CATALOGUE:
            entrees[cellules[0]] = cellules
    if sorted(entrees, key=lambda c: int(c[1:])) != list(CODES_CATALOGUE):
        raise Refus("catalogue : entrées C1 à C12 non trouvées")
    return entrees


def sans_gras(s: str) -> str:
    return s.replace("**", "")


def extraire_json(contenu: str) -> dict:
    """Un seul objet JSON : le texte entier, ou un seul bloc ```json … ``` (forme de l'exemple de la consigne)."""
    t = contenu.strip()
    blocs = re.findall(r"```(?:json)?\s*\n(.*?)\n?```", t, flags=re.S)
    if len(blocs) > 1:
        raise ValueError(f"{len(blocs)} blocs JSON (un seul attendu)")
    brut = blocs[0] if blocs else t
    o = json.loads(brut)
    if not isinstance(o, dict) or not isinstance(o.get("lecture"), list):
        raise ValueError("objet {\"lecture\": [...]} attendu")
    return o


def lire_reponse(chemin, palier: str = "standard") -> tuple[str | None, dict, list]:
    """(contenu ou None, méta, anomalies). Une réponse non scellée ou altérée est refusée. Modèle servi autre ou refus du
    lecteur : anomalie bloquante, contenu non lu. Fin autre que `stop`, forme inattendue, palier servi autre : anomalie
    bloquante, le contenu est lu s'il est un texte (le verdict est E2 de toute façon ; m3 corrigé)."""
    verifier_sceau(chemin)
    nom = Path(chemin).name
    vide = {"finish_reason": None, "usage": None, "modele_servi": None, "palier_servi": None}
    try:
        r = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except ValueError:
        return None, vide, [("reponse_illisible", f"{nom} : JSON")]
    if not isinstance(r, dict):
        return None, vide, [("reponse_illisible", nom)]
    ch = r.get("choices")
    c0 = ch[0] if isinstance(ch, list) and len(ch) == 1 and isinstance(ch[0], dict) else {}
    msg = c0.get("message") if isinstance(c0.get("message"), dict) else {}
    meta = {"finish_reason": c0.get("finish_reason"), "usage": r.get("usage"), "modele_servi": r.get("model"),
            "palier_servi": r.get("service_tier")}
    an = []
    if r.get("model") != MODELE_LECTEUR:
        an.append(("modele_servi_different", f"{nom} : {str(r.get('model'))[:60]}"))
    if r.get("object") != "chat.completion" or not c0:
        an.append(("reponse_illisible", f"{nom} : forme chat.completion à un seul choix attendue"))
    if c0 and c0.get("finish_reason") != "stop":
        an.append(("fin_non_stop", f"{nom} : {c0.get('finish_reason')}"))
    if msg.get("refusal"):
        an.append(("refus_du_lecteur", nom))
    if r.get("service_tier") not in PALIERS_SERVIS_ADMIS.get(palier, ()):
        an.append(("palier_servi_different", f"{nom} : {str(r.get('service_tier'))[:30]}"))
    contenu = msg.get("content")
    if any(g in ("modele_servi_different", "refus_du_lecteur") for g, _ in an) or not isinstance(contenu, str):
        contenu = None
    return contenu, meta, an


def entree_vide(motif: str, juge: bool) -> dict:
    res = {c: {"brut": None, "compte": 0, "prouve": False, "motif": motif} for c in CRITERES}
    if not juge:
        res["R4"] = {"brut": None, "compte": 1, "prouve": True, "motif": "hors levier:juge : 1 par programme"}
    res["N"] = {"brut": None, "compte": "aucune", "occupation_non_prouvee": False, "motif": motif}
    return res


def cles_manquantes(e: dict) -> list[str]:
    """C1 : critères sans valeur brute (clé absente, non objet, ou `valeur` absente ou nulle)."""
    return [c for c in CLES_ENTREE if not (isinstance(e.get(c), dict) and e[c].get("valeur") is not None)]


def verifier_entree(e: dict, vue: dict, juge: bool, cat: dict) -> dict:
    textes = feuilles(vue)
    res = {}
    for c in CRITERES:
        x = e.get(c)
        brut = x.get("valeur") if isinstance(x, dict) else None
        if c == "R4" and not juge:
            res[c] = {"brut": brut, "compte": 1, "prouve": True, "motif": "hors levier:juge : 1 par programme"}
            continue
        if type(brut) is not int or brut not in (0, 1):
            res[c] = {"brut": brut, "compte": 0, "prouve": False, "motif": "valeur hors {0, 1}"}
        elif brut == 0:
            res[c] = {"brut": 0, "compte": 0, "prouve": False, "motif": "0 rendu"}
        else:
            ok, motif = passage_dans(x.get("passage"), textes)
            res[c] = {"brut": 1, "compte": 1 if ok else 0, "prouve": ok, "motif": motif if ok else "non prouvé : " + motif,
                      "passage_rendu": x.get("passage") if isinstance(x.get("passage"), str) else None}
    x = e.get("N")
    brut = x.get("valeur") if isinstance(x, dict) else None
    if brut == "aucune":
        res["N"] = {"brut": brut, "compte": "aucune", "occupation_non_prouvee": False, "motif": "aucune rendue"}
    elif isinstance(brut, str) and brut in cat:
        ok_f, m_f = passage_dans(x.get("passage_fiche"), textes)
        ok_c, m_c = passage_dans(sans_gras(x["passage_catalogue"]) if isinstance(x.get("passage_catalogue"), str)
                                 else None, [sans_gras(cat[brut][CELLULE_MECANISME])])
        if ok_f and ok_c:
            res["N"] = {"brut": brut, "compte": brut, "occupation_non_prouvee": False, "motif": "occupation prouvée"}
        else:
            res["N"] = {"brut": brut, "compte": "aucune", "occupation_non_prouvee": True,
                        "motif": "occupation non prouvée : " + ("fiche : " + m_f if not ok_f else "catalogue : " + m_c)}
    else:
        res["N"] = {"brut": brut, "compte": "aucune", "occupation_non_prouvee": brut is not None,
                    "motif": "valeur de N illisible"}
    return res


def verifier_lot(contenu: str, etiquettes_lot: list[str], vue_de: dict, juge_de: dict, cat: dict) -> tuple[dict, list]:
    anomalies = []
    try:
        o = extraire_json(contenu)
    except ValueError as e:
        anomalies.append({"genre": "reponse_illisible", "detail": str(e)[:300], "etiquettes": list(etiquettes_lot)})
        return {et: entree_vide("réponse illisible", juge_de[et]) for et in etiquettes_lot}, anomalies
    par_et, vues_dans_ordre = {}, []
    for e in o["lecture"]:
        et = e.get("etiquette") if isinstance(e, dict) else None
        if et not in etiquettes_lot:
            anomalies.append({"genre": "etiquette_hors_lot", "detail": str(et)[:40], "etiquettes": []})
            continue
        vues_dans_ordre.append(et)
        par_et.setdefault(et, []).append(e)
    if [et for et in etiquettes_lot if et in vues_dans_ordre] != list(dict.fromkeys(vues_dans_ordre)):
        anomalies.append({"genre": "ordre_du_lot_non_suivi", "detail": "", "etiquettes": []})
    res = {}
    for et in etiquettes_lot:
        entrees = par_et.get(et, [])
        if len(entrees) == 0:
            anomalies.append({"genre": "entree_manquante", "detail": et, "etiquettes": [et]})
            res[et] = entree_vide("entrée manquante", juge_de[et])
        elif len(entrees) > 1:
            anomalies.append({"genre": "entree_en_double", "detail": et, "etiquettes": [et]})
            res[et] = entree_vide("entrée en double : aucune retenue", juge_de[et])
        else:
            manque = cles_manquantes(entrees[0])
            if manque:  # C1 (relecture courte, r1) : bloquante
                anomalies.append({"genre": "cle_de_critere_manquante", "detail": f"{et} : {', '.join(manque)}",
                                  "etiquettes": [et]})
            res[et] = verifier_entree(entrees[0], vue_de[et], juge_de[et], cat)
    return res, anomalies


def charger_envois(dossier) -> dict:
    """C6 : le dossier est le dossier fixe, seul de son espèce ; puis sceaux et empreintes du manifeste."""
    d = Path(dossier)
    racine = racine_du_dossier(d)
    verifier_unicite(racine, d / MANIFESTE)
    for nom in (MANIFESTE, PILE, CLE_LECTURES):
        verifier_sceau(d / nom)
    man = json.loads((d / MANIFESTE).read_text(encoding="utf-8"))
    for nom, h in man["fichiers"].items():
        if verifier_sceau(d / nom) != h:
            raise Refus(f"{nom} : empreinte différente du manifeste")
    pile = json.loads((d / PILE).read_text(encoding="utf-8"))
    cle = json.loads((d / CLE_LECTURES).read_text(encoding="utf-8"))
    return {"manifeste": man, "pile": pile, "cle": cle, "racine": racine}


def verifier_lecture(dossier, L: str, catalogue_texte: str) -> dict:
    env = charger_envois(dossier)
    cat = entrees_catalogue(catalogue_texte)
    par_id = {p["id"]: p for p in env["pile"]["fiches"]}
    cle = env["cle"][L]
    palier = env["manifeste"].get("palier")
    journal = lire_journal(dossier)  # absent : vide ; rompu : refus
    controler_coherence(dossier, env["manifeste"], journal)  # M1 : aucune réponse hors du journal
    arret = bool(journal["arret"] or journal["anomalies"] or journal["en_vol"])
    fiches, anomalies, reponses = {}, [], {}
    for k, lot in enumerate(cle["lots"], 1):
        nom = f"reponse-{L}-lot{k}-{SUFFIXE}.json"
        nom_c = f"envoi-{L}-lot{k}-{SUFFIXE}.corps.json"
        vue_de = {et: par_id[cle["etiquettes"][et]]["vue"] for et in lot}
        juge_de = {et: par_id[cle["etiquettes"][et]]["levier"] == "levier:juge" for et in lot}
        an_lot = []
        ev, recu = journal["clos"].get(nom_c), journal["recus"].get(nom_c)
        if ev and ev.get("anomalies"):  # écart d'envoi (usage, coût, statut, palier…) : bloquant (v3.1)
            an_lot.append({"genre": "anomalie_d_envoi", "detail": ", ".join(map(str, ev["anomalies"])),
                           "etiquettes": list(lot)})
        if not (Path(dossier) / nom).exists():
            if not arret:
                raise Refus(f"réponse attendue absente : {nom} (aucun arrêt consigné au journal)")
            reponses[nom] = None
            an_lot.append({"genre": "reponse_absente", "detail": f"{nom} : non envoyée ou non rendue (arrêt consigné)",
                           "etiquettes": list(lot)})
            res = {et: entree_vide("réponse absente", juge_de[et]) for et in lot}
        else:
            h = sha256_fichier(Path(dossier) / nom)
            if ev is None and recu is not None and recu.get("fichier") == nom and recu.get("fichier_sha256") == h:
                reponses[nom] = {"sha256": h, "non_analysee": True}
                an_lot.append({"genre": "reponse_non_analysee", "detail": f"{nom} : reçue, jamais close au journal",
                               "etiquettes": list(lot)})
                res = {et: entree_vide("réponse non analysée", juge_de[et]) for et in lot}
            elif ev is None or ev.get("fichier") != nom or ev.get("fichier_sha256") != h or ev.get("statut") != 200:
                raise Refus(f"{nom} : aucune clôture chaînée au journal à son nom, à son empreinte et au statut 200 (M1)")
            else:
                contenu, meta, an = lire_reponse(Path(dossier) / nom, palier)
                reponses[nom] = {"sha256": h, **meta}
                an_lot += [{"genre": g, "detail": d, "etiquettes": list(lot)} for g, d in an]
                if contenu is None:
                    if not an:
                        an_lot.append({"genre": "reponse_illisible", "detail": f"{nom} : contenu absent",
                                       "etiquettes": list(lot)})
                    res = {et: entree_vide("contenu non lu", juge_de[et]) for et in lot}
                else:
                    res, an2 = verifier_lot(contenu, lot, vue_de, juge_de, cat)
                    an_lot += an2
        for a in an_lot:
            a["lot"] = k
            a["ids"] = [cle["etiquettes"][et] for et in a.get("etiquettes", [])]
        anomalies += an_lot
        for et, r in res.items():
            fiches[cle["etiquettes"][et]] = {"etiquette": et, "lot": k, **r}
    comptes = {c: sum(1 for f in fiches.values() if f[c]["brut"] == 1 and not f[c]["prouve"]) for c in CRITERES}
    comptes["N_occupation_non_prouvee"] = sum(1 for f in fiches.values() if f["N"]["occupation_non_prouvee"])
    courts = {c: sum(1 for f in fiches.values() if f[c]["brut"] == 1 and "trop court" in f[c]["motif"])
              for c in CRITERES}
    courts["N"] = sum(1 for f in fiches.values() if "trop court" in f["N"]["motif"])
    bloquantes = [a for a in anomalies if a["genre"] in ANOMALIES_BLOQUANTES]
    return {"version": VERSION, "lecture": L, "reponses": reponses, "fiches": fiches, "anomalies": anomalies,
            "anomalies_bloquantes": bloquantes,
            "ids_touches": sorted({i for a in bloquantes for i in a.get("ids", [])}),
            "non_prouves": comptes, "passages_courts_refuses": courts,
            "passages_au_dela_de_200": sum(1 for f in fiches.values() for c in CRITERES
                                           if isinstance(f[c].get("passage_rendu"), str)
                                           and len(f[c]["passage_rendu"]) > LONGUEUR_MAX_CONSIGNE)}


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    s = a.add_subparsers(dest="action", required=True)
    p = s.add_parser("preparer")
    p.add_argument("--fiches", required=True)
    p.add_argument("--attestation", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--effort", required=True, choices=EFFORTS)
    p.add_argument("--palier", default="standard", choices=PALIERS)
    p.add_argument("--plafond-usd", type=float, required=True)
    p.add_argument("--depense-anterieure-usd", type=float, required=True)
    p.add_argument("--racine", default=str(RACINE_DEFAUT))
    e = s.add_parser("envoyer")
    e.add_argument("--envois", required=True)
    e.add_argument("--envois-max", type=int, default=None)
    b = s.add_parser("bilan")
    b.add_argument("--envois", required=True)
    v = s.add_parser("verifier")
    v.add_argument("--envois", required=True)
    v.add_argument("--lecture", choices=LECTURES, action="append")
    v.add_argument("--racine", default=str(RACINE_DEFAUT))
    args = a.parse_args(argv)
    try:
        if args.action == "preparer":
            m = preparer(args.fiches, args.attestation, args.sortie, args.racine, effort=args.effort,
                         palier=args.palier, plafond_usd=args.plafond_usd,
                         depense_anterieure_usd=args.depense_anterieure_usd)
            g = m["garde_depense"]
            print(json.dumps({"pile": m["pile"]["fiches"], "lots": m["lots"]["tailles"], "appels": g["appels_max"],
                              "palier": m["palier"], "prix_usd_par_million": {k: g["prix_usd_par_million"][k]
                                                                              for k in ("entree", "cache", "sortie")},
                              "pire_cas_total_usd": g["pire_cas_total_usd"], "plafond_usd": g["plafond_usd"],
                              "appels_surs_au_pire_cas": g["appels_surs_au_pire_cas"],
                              "max_completion_tokens": MAX_SORTIE, "reasoning_effort": args.effort},
                             ensure_ascii=False))
        elif args.action == "envoyer":
            if args.envois_max is not None and args.envois_max < 1:
                raise Refus("--envois-max : au moins 1")
            r = envoyer(args.envois, envois_max=args.envois_max)
            print(json.dumps(r, ensure_ascii=False))
            return {"fait": 0, "pause": 0, "anomalie": 3, "plafond": 4}[r["issue"]]
        elif args.action == "bilan":
            print(json.dumps(bilan(args.envois), ensure_ascii=False))
        else:
            if racine_du_dossier(args.envois) != Path(args.racine).resolve():
                raise Refus("--racine différente de la racine du dossier d'envois")
            cat, _ = lire_piece(args.racine, "catalogue")
            for L in args.lecture or LECTURES:
                r = verifier_lecture(args.envois, L, cat)
                ecrire_scelle(Path(args.envois) / f"lecture-verifiee-{L}-{SUFFIXE}.json", json_texte(r))
                print(json.dumps({"lecture": L, "non_prouves": r["non_prouves"], "anomalies": len(r["anomalies"]),
                                  "anomalies_bloquantes": len(r["anomalies_bloquantes"])}, ensure_ascii=False))
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
