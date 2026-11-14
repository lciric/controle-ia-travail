#!/usr/bin/env python3
"""Outil du lecteur de la règle de sélection — course « conception propre » — v3 (lecteur Astra).

v3 (14 novembre 2026, à partir de 07:43 UTC, `date -u`) = v2 (`../lecture-classement-v2/`, `a58fb8b9…`, gardée, R12),
écrite par un développeur neuf après l'échec de la lecture par Kimi (R-2658 : lots de 14 ou 15 fiches, `finish_reason =
length`, les 32 768 jetons de sortie mangés par le raisonnement) et le changement de lecteur décidé par Lazar (R-2659,
R-2662) : **Astra** (`gpt-6-astra`, famille OpenAI), voie déjà nommée par la conception (§ 4.2, `be3ba97e…`) ; la règle ne
change pas. Ce qui change, et seulement cela (détail : `rapport-lecture-classement-v3.md`) :

- **lecteur et point d'entrée** : `POST https://api.openai.com/v1/chat/completions` (Chat Completions, pas Responses :
  voie déjà employée avec `gpt-6-astra` dans le dépôt, modèle servi rendu exact, R-1454 ; réponse `chat.completion` dont
  `choices[0].finish_reason` porte directement la garde « fin autre que stop » de la v2 ; aucun état gardé chez le
  fournisseur, `store: false` explicite) ; corps = un seul message utilisateur (le même texte qu'en v2), `model`,
  `max_completion_tokens` (plafond de sortie, raisonnement compris), `reasoning_effort` (effort de raisonnement, choisi et
  consigné à la préparation), `store` ; aucun outil, aucun message système, aucune température ;
- **clé** : lue **par son nom seul**, `OPENAI_API_KEY`, dans la seule fonction `lire_cle` (le « relais » en processus :
  `envoyer`), retirée aussitôt de `os.environ`, posée dans l'en-tête `Authorization` et nulle part ailleurs : jamais
  affichée, jamais écrite, masquée dans tout message d'erreur ;
- **lots de 5 fiches** (`TAILLE_LOT`, paramètre unique ; 43 fiches → 9 lots par lecture, 18 appels) au lieu de 20 ;
- **plafond de sortie et effort explicites**, consignés au manifeste et dans chaque corps ;
- **modèle servi vérifié** : `model` de la réponse égal, octet pour octet, à `gpt-6-astra`, sinon anomalie bloquante ;
- **garde de dépense** dans `envoyer` : prix et plafond en USD fixés à la préparation (manifeste scellé), nombre d'appels
  maximal fixé d'avance (deux lectures × lots, au plus `MAX_APPELS` = 18) ; avant chaque appel, dépense comptée + pire cas
  de l'appel ≤ plafond, sinon arrêt sans envoi ; après chaque appel, coût lu dans `usage` (jetons d'entrée, d'entrée en
  cache, de sortie), compté **au pire cas** quand l'usage manque, est illisible ou incohérent ; journal de dépense chaîné,
  relu à chaque reprise (un arrêt ne remet pas le compte à zéro) ;
- **arrêt au premier écart** : statut autre que 200, modèle servi différent, fin autre que `stop`, usage absent, refus du
  lecteur, coût au-dessus du pire cas réservé : rien d'autre n'est envoyé (leçon de R-2658 : le second lot était parti
  avant la lecture de la fin du premier), aucune relecture, aucune reprise automatique ;
- **condition C1 de la relecture courte** (`relecture-courte-lecture-classement-v2.md`, r1) devenue une anomalie
  bloquante : une entrée à laquelle manque une clé de critère (R1 à R7, N, ou sa `valeur`) rend la lecture incomplète ;
- une **réponse absente** n'est acceptée par `verifier` que si le journal consigne un arrêt (elle devient alors une
  anomalie bloquante, verdict E2) ; sinon refus, comme en v2 ;
- un corps d'erreur du fournisseur n'est **jamais** écrit (il peut porter des identifiants du compte, R-2645) : seuls le
  statut, le type et le code de l'erreur, et l'empreinte du corps.

Les envois de la v1 (`lecture-g1-v1/envois/`, lots de 14 ou 15, corps au format Kimi) ne servent plus : `preparer` les
**régénère** de façon déterministe depuis la copie attestée des fiches validées et les témoins épinglés. Les ordres des deux
lectures sont ceux de la v2 (même `SeedSequence(2026111302).spawn(4)`, enfants 0 et 1, mêmes étiquettes F01…) ; seules
les frontières des lots changent.

De la v2 (inchangé) : attestation exigée ; pièces épinglées ; seule la copie scellée `runs/…/copies/sortie--fiches-validees.json`
acceptée (M3) ; admissibilité par programme ; vue servie sans auteur, identifiant, passe, empreinte ni marque de témoin,
clés dans l'ordre du gabarit, typographie de l'orchestrateur ; citations d'au moins 20 caractères hors espaces, vérifiées
mot pour mot ; catalogue lu dans la seule cellule du mécanisme (M1) ; anomalies bloquantes nommant les fiches (M2) ; R4
hors `levier:juge` à 1 par programme ; écriture scellée, jamais d'écrasement (R12).

Actions :

    python3 -I -B outil_lecteur_conception_propre_v3.py preparer --fiches F --attestation A --sortie DOSSIER \
        --effort low|medium|high --prix-entree PE --prix-sortie PS [--prix-cache PC] --source-prix TEXTE --plafond-usd X
    python3 -I -B outil_lecteur_conception_propre_v3.py envoyer --envois DOSSIER [--envois-max N]
    python3 -I -B outil_lecteur_conception_propre_v3.py bilan --envois DOSSIER
    python3 -I -B outil_lecteur_conception_propre_v3.py verifier --envois DOSSIER [--lecture L1|L2]

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
import urllib.request
from pathlib import Path

import numpy as np

VERSION = "outil-lecteur-conception-propre-v3"
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
TAILLE_MAX_REPONSE = 4_000_000
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
                        "cle_de_critere_manquante", "reponse_absente", "modele_servi_different", "refus_du_lecteur")
CODES_CATALOGUE = tuple(f"C{i}" for i in range(1, 13))
CHAMPS_INTERNES = ("auteur", "identifiant_auteur", "empreinte", "passe", "temoin")  # toujours retirés (orchestrateur)
ATTESTATION_CHAMPS = ("lecteur", "lu_le", "fiches_validees_sha256", "aucune_recette_aucun_secret",
                      "envoi_au_lecteur_externe_permis")
JOURNAL = "journal-depense-v3.jsonl"
MANIFESTE = "manifeste-envois-v3.json"
PILE = "pile-interne-v3.json"
CLE_LECTURES = "cle-lectures-v3.json"
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


def corps_requete(message: str, effort: str) -> str:
    """Corps de Chat Completions : un seul message utilisateur ; plafond de sortie et effort explicites ; rien gardé chez
    le fournisseur (`store: false`)."""
    return json.dumps({"model": MODELE_LECTEUR, "messages": [{"role": "user", "content": message}],
                       "max_completion_tokens": MAX_SORTIE, "reasoning_effort": effort, "store": False},
                      ensure_ascii=False)


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


def preparer(fiches_chemin, attestation_chemin, sortie, racine=RACINE_DEFAUT, *, effort, prix_entree, prix_sortie,
             plafond_usd, source_prix, prix_cache=None) -> dict:
    racine = Path(racine)
    sortie = Path(sortie)
    if sortie.exists() and any(sortie.iterdir()):
        raise Refus(f"{sortie} existe et n'est pas vide : on n'écrase jamais (R12)")
    if effort not in EFFORTS:
        raise Refus(f"effort de raisonnement {effort!r} hors de {EFFORTS}")
    prix = prix_valides({"entree": prix_entree, "sortie": prix_sortie,
                         "cache": prix_entree if prix_cache is None else prix_cache, "source": source_prix})
    if type(plafond_usd) not in (int, float) or not math.isfinite(plafond_usd) or plafond_usd <= 0:
        raise Refus(f"plafond invalide : {plafond_usd!r}")
    if plafond_usd > PLAFOND_ABSOLU_USD:
        raise Refus(f"plafond {plafond_usd} USD > {PLAFOND_ABSOLU_USD} (reste du GO-2026-11-13-06)")
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
    corps = {Lk: corps_requete(msg, effort) for Lk, msg in messages.items()}
    garde = []
    for (L, k) in sorted(corps):
        o = len(corps[(L, k)].encode("utf-8"))
        garde.append({"envoi": f"envoi-{L}-lot{k}-v3.corps.json", "lecture": L, "lot": k, "octets": o,
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
        nom_m, nom_c = f"envoi-{L}-lot{k}-v3.txt", f"envoi-{L}-lot{k}-v3.corps.json"
        fichiers[nom_m] = ecrire_scelle(sortie / nom_m, messages[(L, k)])
        fichiers[nom_c] = ecrire_scelle(sortie / nom_c, corps[(L, k)])
    fichiers[PILE] = ecrire_scelle(sortie / PILE, json_texte(pile))
    fichiers[CLE_LECTURES] = ecrire_scelle(sortie / CLE_LECTURES, json_texte(cle))
    e = enfants_ordres()
    manifeste = {
        "version": VERSION, "outil_sha256": sha256_fichier(__file__), "prepare_le": maintenant(),
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__},
        "pieces": {k: {"chemin": PIECES[k][0], "sha256": v} for k, v in empreintes.items()},
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
        "lecteur": {"modele": MODELE_LECTEUR, "url": URL_AMONT, "point_d_entree": "Chat Completions",
                    "variable_cle": VARIABLE_CLE, "max_completion_tokens": MAX_SORTIE, "reasoning_effort": effort,
                    "store": False},
        "garde_depense": {"prix_usd_par_million": prix, "plafond_usd": plafond_usd, "appels_max": appels,
                          "pire_cas_total_usd": round(total, 6), "appels_surs_au_pire_cas": surs,
                          "regle": "avant chaque appel : dépense comptée + pire cas de l'appel ≤ plafond, sinon arrêt ; "
                                   "après : coût lu dans usage, pire cas si usage absent, illisible ou incohérent",
                          "envois": garde},
        "ordre_d_envoi": [g["envoi"] for g in garde],
        "reponses_attendues": [f"reponse-{L}-lot{k}-v3.json" for L in LECTURES for k in range(1, len(lots_idx) + 1)],
        "fichiers": fichiers,
        "jamais_envoyes": [PILE, CLE_LECTURES, MANIFESTE, JOURNAL],
    }
    ecrire_scelle(sortie / MANIFESTE, json_texte(manifeste))
    return manifeste


# --- envoi : relais en processus, clé, garde de dépense --------------------------------------------------------------

def lire_cle() -> str:
    """La clé, lue par son nom seul, puis retirée de l'environnement du processus. Jamais affichée ni écrite."""
    cle = os.environ.pop(VARIABLE_CLE, None)
    if not cle:
        raise Refus(f"{VARIABLE_CLE} absente : rien n'est envoyé")
    return cle


def masquer(texte: str, cle: str) -> str:
    return texte.replace(cle, "[clé]") if cle else texte


def transport_reel(url: str, entetes: dict, corps: bytes, delai: float) -> tuple[int, bytes]:
    """Un seul POST, sans reprise. Mandataire de l'environnement (urllib), certificats de SSL_CERT_FILE s'il est donné."""
    if url != URL_AMONT:
        raise Refus("adresse d'amont autre que celle d'OpenAI : refusée")
    ca = os.environ.get("SSL_CERT_FILE")
    contexte = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
    ouvreur = urllib.request.build_opener(urllib.request.HTTPSHandler(context=contexte))
    req = urllib.request.Request(url, data=corps, method="POST", headers=entetes)
    try:
        with ouvreur.open(req, timeout=delai) as r:
            return r.status, r.read(TAILLE_MAX_REPONSE + 1)
    except urllib.error.HTTPError as e:
        return e.code, e.read(TAILLE_MAX_REPONSE + 1)


def entier(x) -> bool:
    return type(x) is int and x >= 0


def cout_usage(usage, prix: dict) -> tuple[float | None, str | None, dict]:
    """(coût en USD, problème, jetons lus). Coût None si l'usage est absent ou illisible (le pire cas s'applique).
    Règle : (prompt − cache) × entrée + cache × prix du cache + completion × sortie + excédent de total × prix le plus
    haut. `completion_tokens` compte le raisonnement (`completion_tokens_details.reasoning_tokens` en est une part :
    SUPPOSÉ, vérifié sur la première réponse) ; un raisonnement plus grand que la sortie est une incohérence."""
    if not isinstance(usage, dict):
        return None, "usage absent", {}
    p, c = usage.get("prompt_tokens"), usage.get("completion_tokens")
    if not entier(p) or not entier(c):
        return None, "usage illisible (prompt_tokens ou completion_tokens)", {}
    cache = (usage.get("prompt_tokens_details") or {}).get("cached_tokens", 0)
    raison = (usage.get("completion_tokens_details") or {}).get("reasoning_tokens", 0)
    total = usage.get("total_tokens", p + c)
    if not entier(cache) or not entier(raison) or not entier(total):
        return None, "usage illisible (détails)", {}
    lus = {"prompt_tokens": p, "cached_tokens": cache, "completion_tokens": c, "reasoning_tokens": raison,
           "total_tokens": total}
    probleme = None
    if cache > p:
        probleme = "jetons en cache au-dessus des jetons d'entrée"
    elif raison > c:
        probleme = "jetons de raisonnement au-dessus des jetons de sortie"
    elif c > MAX_SORTIE:
        probleme = f"jetons de sortie au-dessus du plafond demandé ({MAX_SORTIE})"
    exces = max(0, total - p - c)
    haut = max(prix["entree"], prix["sortie"])
    cout = ((p - min(cache, p)) * prix["entree"] + min(cache, p) * prix["cache"] + c * prix["sortie"]
            + exces * haut + (max(0, raison - c) * prix["sortie"])) / 1e6
    return cout, probleme, lus


def champ_court(x) -> str | None:
    return x if isinstance(x, str) and re.fullmatch(r"[A-Za-z0-9_.\-]{1,60}", x) else None


def analyser_reponse(statut, corps: bytes | None, pire_cas: float, prix: dict) -> dict:
    """Lit une réponse de l'amont (statut, octets). Rend {cout, au_pire_cas, anomalies, modele_servi, fin, lus, garder}.
    `garder` vrai : le corps est une réponse `chat.completion` (statut 200) à sceller telle quelle ; faux : on n'écrit que
    le statut, le type et le code d'erreur, et l'empreinte du corps (jamais le corps)."""
    r = {"cout_usd": pire_cas, "au_pire_cas": True, "anomalies": [], "modele_servi": None, "finish_reason": None,
         "jetons": {}, "garder": False, "erreur": None, "statut": statut,
         "corps_sha256": sha256_octets(corps) if corps is not None else None}
    if statut is None:
        r["anomalies"].append("transport_echec")
        return r
    if corps is not None and len(corps) > TAILLE_MAX_REPONSE:
        r["anomalies"].append("reponse_trop_grande")
        return r
    try:
        o = json.loads(corps.decode("utf-8")) if corps is not None else None
    except (UnicodeDecodeError, ValueError):
        o = None
    if statut != 200:
        err = (o or {}).get("error") if isinstance(o, dict) else None
        r["erreur"] = {"type": champ_court((err or {}).get("type")), "code": champ_court((err or {}).get("code"))}
        r["anomalies"].append("statut_non_200")
        return r
    if not isinstance(o, dict):
        r["anomalies"].append("reponse_illisible")
        return r
    r["garder"] = True
    r["modele_servi"] = o.get("model") if isinstance(o.get("model"), str) else None
    cout, probleme, lus = cout_usage(o.get("usage"), prix)
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
    ch = o.get("choices")
    if not isinstance(ch, list) or len(ch) != 1 or not isinstance(ch[0], dict):
        r["anomalies"].append("choix_non_unique")
        return r
    r["finish_reason"] = ch[0].get("finish_reason")
    if r["finish_reason"] != "stop":
        r["anomalies"].append("fin_non_stop")
    msg = ch[0].get("message") or {}
    if msg.get("refusal"):
        r["anomalies"].append("refus_du_lecteur")
    if not isinstance(msg.get("content"), str) or not msg["content"].strip():
        r["anomalies"].append("contenu_absent")
    return r


def lire_journal(dossier) -> dict:
    """Relit le journal de dépense chaîné (chaque ligne porte l'empreinte de la précédente). Rend la dépense comptée (un
    envoi sans clôture compte son pire cas), les appels, les envois clos, les anomalies et l'arrêt consigné."""
    p = Path(dossier) / JOURNAL
    etat = {"appels": 0, "depense_usd": 0.0, "clos": {}, "en_vol": [], "anomalies": [], "arret": None, "lignes": 0,
            "dernier_sha256": "debut"}
    if not p.exists():
        return etat
    ouverts = {}
    for i, brute in enumerate(p.read_bytes().splitlines(keepends=True)):
        try:
            ev = json.loads(brute.decode("utf-8"))
        except ValueError as e:
            raise Refus(f"{JOURNAL} ligne {i + 1} illisible") from e
        if ev.get("n") != i + 1 or ev.get("precedent") != etat["dernier_sha256"]:
            raise Refus(f"{JOURNAL} ligne {i + 1} : chaîne rompue (journal tronqué ou réécrit)")
        etat["dernier_sha256"] = sha256_octets(brute)
        etat["lignes"] = i + 1
        g = ev.get("evenement")
        if g == "envoi":
            if ev["envoi"] in ouverts or ev["envoi"] in etat["clos"]:
                raise Refus(f"{JOURNAL} : {ev['envoi']} envoyé deux fois")
            etat["appels"] += 1
            ouverts[ev["envoi"]] = ev
        elif g == "clos":
            if ev["envoi"] not in ouverts:
                raise Refus(f"{JOURNAL} : clôture sans envoi ({ev['envoi']})")
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


def ajouter_journal(dossier, etat: dict, ev: dict) -> None:
    ev = {"n": etat["lignes"] + 1, "precedent": etat["dernier_sha256"], "utc": maintenant(), **ev}
    ligne = (json.dumps(ev, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")
    with open(Path(dossier) / JOURNAL, "ab") as f:
        f.write(ligne)
        f.flush()
        os.fsync(f.fileno())
    etat["lignes"] += 1
    etat["dernier_sha256"] = sha256_octets(ligne)


def nom_reponse(envoi: str) -> str:
    return envoi.replace("envoi-", "reponse-").replace("-v3.corps.json", "-v3.json")


def nom_erreur(envoi: str) -> str:
    return envoi.replace("envoi-", "erreur-").replace("-v3.corps.json", "-v3.json")


def controler_coherence(dossier, man: dict, j: dict) -> None:
    """Chaque réponse ou erreur déposée a sa clôture au journal, à la même empreinte ; aucune autre n'existe."""
    for g in man["garde_depense"]["envois"]:
        for nom in (nom_reponse(g["envoi"]), nom_erreur(g["envoi"])):
            if (Path(dossier) / nom).exists():
                h = verifier_sceau(Path(dossier) / nom)
                ev = j["clos"].get(g["envoi"])
                if ev is None or ev.get("fichier") != nom or ev.get("fichier_sha256") != h:
                    raise Refus(f"{nom} sans clôture conforme au journal (journal tronqué ou fichier étranger)")


def bilan(dossier) -> dict:
    env = charger_envois(dossier)
    man = env["manifeste"]
    j = lire_journal(dossier)
    controler_coherence(dossier, man, j)
    return {"appels": j["appels"], "appels_max": man["garde_depense"]["appels_max"],
            "depense_comptee_usd": round(j["depense_usd"], 6), "plafond_usd": man["garde_depense"]["plafond_usd"],
            "clos": sorted(j["clos"]), "en_vol": j["en_vol"], "anomalies": j["anomalies"],
            "arret": (j["arret"] or {}).get("motif")}


def envoyer(dossier, transport=None, envois_max=None) -> dict:
    """Envoie les lots dans l'ordre du manifeste, un à la fois, sous la garde de dépense ; s'arrête au premier écart.
    Rend {issue: fait|pause|anomalie|plafond, …}. Toute réponse 200 est scellée telle quelle ; toute autre issue laisse un
    fichier d'erreur scellé sans le corps."""
    transport = transport or transport_reel
    env = charger_envois(dossier)
    man = env["manifeste"]
    if man.get("version") != VERSION:
        raise Refus(f"envois préparés par {man.get('version')!r}, pas par {VERSION}")
    g = man["garde_depense"]
    prix = prix_valides(dict(g["prix_usd_par_million"]))
    plafond, appels_max = g["plafond_usd"], g["appels_max"]
    if plafond > PLAFOND_ABSOLU_USD or appels_max > MAX_APPELS:
        raise Refus("manifeste : plafond ou nombre d'appels au-delà des bornes du code")
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
            ajouter_journal(dossier, j, {"evenement": "arret", "motif": "appels", "detail": detail})
            break
        corps = (Path(dossier) / e["envoi"]).read_bytes()
        if sha256_octets(corps) != man["fichiers"][e["envoi"]]:
            raise Refus(f"{e['envoi']} : corps différent du manifeste")
        pire = max(e["pire_cas_usd"], pire_cas_usd(len(corps), prix))  # recalculé sur les octets envoyés
        if j["depense_usd"] + pire > plafond + 1e-12:
            issue = "plafond"
            detail = (f"{e['envoi']} : dépense comptée {j['depense_usd']:.6f} + pire cas {pire:.6f} "
                      f"> plafond {plafond}")
            ajouter_journal(dossier, j, {"evenement": "arret", "motif": "plafond", "detail": detail})
            break
        ajouter_journal(dossier, j, {"evenement": "envoi", "envoi": e["envoi"], "octets": len(corps),
                                     "pire_cas_usd": pire})
        envoyes += 1
        try:
            statut, rep = transport(URL_AMONT, entetes, corps, DELAI_S)
            cause = None
        except Refus:
            raise
        except Exception as ex:  # coupure, délai, mandataire : l'appel compte au pire cas
            statut, rep, cause = None, None, masquer(f"{type(ex).__name__}: {ex}", cle)[:200]
        a = analyser_reponse(statut, rep, pire, prix)
        if a["garder"]:
            nom = nom_reponse(e["envoi"])
            h = ecrire_scelle_octets(Path(dossier) / nom, rep)
        else:
            nom = nom_erreur(e["envoi"])
            h = ecrire_scelle(Path(dossier) / nom, json_texte({
                "envoi": e["envoi"], "statut": statut, "erreur": a["erreur"], "corps_sha256": a["corps_sha256"],
                "corps_octets": len(rep) if rep is not None else None, "cause_transport": cause,
                "note": "corps de l'amont jamais écrit (il peut porter des identifiants du compte)"}))
        ev = {"evenement": "clos", "envoi": e["envoi"], "statut": statut, "fichier": nom, "fichier_sha256": h,
              "modele_servi": a["modele_servi"], "finish_reason": a["finish_reason"], "jetons": a["jetons"],
              "cout_usd": round(a["cout_usd"], 6), "au_pire_cas": a["au_pire_cas"], "anomalies": a["anomalies"]}
        ajouter_journal(dossier, j, ev)
        j = lire_journal(dossier)  # dépense et appels recomptés depuis le journal écrit
        if a["anomalies"]:
            issue, detail = "anomalie", f"{e['envoi']} : {', '.join(a['anomalies'])}"
            break
    del cle, entetes
    releve = {"version": VERSION, "fin_utc": maintenant(), "issue": issue, "detail": detail,
              "envoyes_cette_fois": envoyes, "appels": j["appels"], "appels_max": appels_max,
              "depense_comptee_usd": round(j["depense_usd"], 6), "plafond_usd": plafond,
              "journal_sha256": sha256_fichier(Path(dossier) / JOURNAL)}
    k = 1
    while (Path(dossier) / f"releve-depense-v3-{k}.json").exists():
        k += 1
    ecrire_scelle(Path(dossier) / f"releve-depense-v3-{k}.json", json_texte(releve))
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


def lire_reponse(chemin) -> tuple[str | None, dict, list]:
    """(contenu ou None, méta, anomalies). Une réponse non scellée ou altérée est refusée ; un modèle servi autre, une fin
    autre que `stop`, un refus, une forme illisible sont des anomalies bloquantes (le contenu n'est alors pas lu)."""
    verifier_sceau(chemin)
    nom = Path(chemin).name
    try:
        r = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except ValueError:
        return None, {"finish_reason": None, "usage": None, "modele_servi": None}, [("reponse_illisible", f"{nom} : JSON")]
    if not isinstance(r, dict):
        return None, {"finish_reason": None, "usage": None, "modele_servi": None}, [("reponse_illisible", nom)]
    ch = r.get("choices")
    c0 = ch[0] if isinstance(ch, list) and len(ch) == 1 and isinstance(ch[0], dict) else {}
    meta = {"finish_reason": c0.get("finish_reason"), "usage": r.get("usage"), "modele_servi": r.get("model")}
    an = []
    if r.get("model") != MODELE_LECTEUR:
        an.append(("modele_servi_different", f"{nom} : {str(r.get('model'))[:60]}"))
    if r.get("object") != "chat.completion" or not c0:
        an.append(("reponse_illisible", f"{nom} : forme chat.completion à un seul choix attendue"))
    if c0 and c0.get("finish_reason") != "stop":
        an.append(("fin_non_stop", f"{nom} : {c0.get('finish_reason')}"))
    msg = c0.get("message") or {}
    if msg.get("refusal"):
        an.append(("refus_du_lecteur", nom))
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
    d = Path(dossier)
    for nom in (MANIFESTE, PILE, CLE_LECTURES):
        verifier_sceau(d / nom)
    man = json.loads((d / MANIFESTE).read_text(encoding="utf-8"))
    for nom, h in man["fichiers"].items():
        if verifier_sceau(d / nom) != h:
            raise Refus(f"{nom} : empreinte différente du manifeste")
    pile = json.loads((d / PILE).read_text(encoding="utf-8"))
    cle = json.loads((d / CLE_LECTURES).read_text(encoding="utf-8"))
    return {"manifeste": man, "pile": pile, "cle": cle}


def verifier_lecture(dossier, L: str, catalogue_texte: str) -> dict:
    env = charger_envois(dossier)
    cat = entrees_catalogue(catalogue_texte)
    par_id = {p["id"]: p for p in env["pile"]["fiches"]}
    cle = env["cle"][L]
    fiches, anomalies, reponses = {}, [], {}
    journal = lire_journal(dossier)  # absent : vide ; rompu : refus
    arret = bool(journal["arret"] or journal["anomalies"] or journal["en_vol"])
    for k, lot in enumerate(cle["lots"], 1):
        nom = f"reponse-{L}-lot{k}-v3.json"
        vue_de = {et: par_id[cle["etiquettes"][et]]["vue"] for et in lot}
        juge_de = {et: par_id[cle["etiquettes"][et]]["levier"] == "levier:juge" for et in lot}
        an_lot = []
        ev = journal["clos"].get(f"envoi-{L}-lot{k}-v3.corps.json")
        if ev and ev.get("anomalies"):  # écart d'envoi (usage, coût, statut…) : rapporté ; bloquant s'il touche la lecture
            an_lot.append({"genre": "anomalie_d_envoi", "detail": ", ".join(ev["anomalies"]), "etiquettes": []})
        if not (Path(dossier) / nom).exists():
            if not arret:
                raise Refus(f"réponse attendue absente : {nom} (aucun arrêt consigné au journal)")
            reponses[nom] = None
            an_lot.append({"genre": "reponse_absente", "detail": f"{nom} : non envoyée ou non rendue (arrêt consigné)",
                           "etiquettes": list(lot)})
            res = {et: entree_vide("réponse absente", juge_de[et]) for et in lot}
        else:
            contenu, meta, an = lire_reponse(Path(dossier) / nom)
            reponses[nom] = {"sha256": sha256_fichier(Path(dossier) / nom), **meta}
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
    p.add_argument("--prix-entree", type=float, required=True)
    p.add_argument("--prix-sortie", type=float, required=True)
    p.add_argument("--prix-cache", type=float, default=None)
    p.add_argument("--source-prix", required=True)
    p.add_argument("--plafond-usd", type=float, required=True)
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
                         prix_entree=args.prix_entree, prix_sortie=args.prix_sortie, prix_cache=args.prix_cache,
                         source_prix=args.source_prix, plafond_usd=args.plafond_usd)
            g = m["garde_depense"]
            print(json.dumps({"pile": m["pile"]["fiches"], "lots": m["lots"]["tailles"], "appels": g["appels_max"],
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
            cat, _ = lire_piece(args.racine, "catalogue")
            for L in args.lecture or LECTURES:
                r = verifier_lecture(args.envois, L, cat)
                ecrire_scelle(Path(args.envois) / f"lecture-verifiee-{L}-v3.json", json_texte(r))
                print(json.dumps({"lecture": L, "non_prouves": r["non_prouves"], "anomalies": len(r["anomalies"]),
                                  "anomalies_bloquantes": len(r["anomalies_bloquantes"])}, ensure_ascii=False))
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
