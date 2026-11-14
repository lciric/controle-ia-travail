#!/usr/bin/env python3
"""Outil du lecteur de la règle de sélection — course « conception propre » — v2.

v2 (14 novembre 2026, à partir de 00:13 UTC, `date -u`) = v1 (`../lecture-classement-v1/`, `59e665af…`, gardée, R12)
corrigée d'après la contre-lecture `contre-lecture-lecture-classement-v1.md` (`baabfb13…`, R-2627) :
- **M1** : un passage ne prouve que s'il a au moins `LONGUEUR_MIN_PASSAGE` = 20 caractères hors espaces ; le passage du
  catalogue n'est cherché que dans la cellule « Mécanisme central » de l'entrée Ck (jamais son code, son nom, sa source
  ni une date) ;
- **M2** : chaque anomalie de lecture nomme les fiches qu'elle touche ; les anomalies **bloquantes** (réponse illisible,
  fin autre que `stop`, entrée manquante ou en double) sont listées à part : le classement les porte au verdict et interdit
  la désignation ;
- **M3** : seul le fichier `runs/course-ideation-conception-propre-v1/<run>/copies/sortie--fiches-validees.json` est
  accepté (chemin réel, aucun lien, compagnon, empreinte égale à celle du manifeste de fin du lanceur, issue code 0) ;
  chaque élément doit porter les clés du gabarit et les champs internes de l'orchestrateur ; une pile sans fiche réelle
  admissible est refusée avant tout envoi (E1, rien payé).

De la v1 : écrit le 13 novembre 2026 (à partir de 23:42 UTC) par un développeur neuf (tâche N3 de R-2615), avant toute
course et toute lecture. Comportement fixé par `conception-course-v1.md` (be3ba97e…), § 3, 4.1 à 4.5, et par
`consigne-lecteur-v1.md` (95efebaa…). **N'appelle aucun modèle, ne lit aucune clé** : il prépare les envois (texte du
message et corps de requête au format du relais Kimi v4), que la mère envoie elle-même sous la ligne GO-2026-11-13-06 ;
puis il vérifie les réponses rendues, mot pour mot, contre les fiches servies.

Deux actions :

    python3 -I -B outil_lecteur_conception_propre_v2.py preparer --fiches F --attestation A --sortie DOSSIER
    python3 -I -B outil_lecteur_conception_propre_v2.py verifier --envois DOSSIER [--lecture L1|L2]

`preparer` :
- vérifie les pièces épinglées (consigne, question, faits, catalogue, témoins) par leur empreinte ; le fichier des fiches
  validées par son compagnon `.sha256` ; l'attestation de lecture de la mère (§ 3 : empreinte des fiches, deux drapeaux
  vrais, compagnon) ; sans elle, rien n'est préparé ;
- admissibilité par programme (§ 4.1) : exactement une étiquette de levier dans `questions_servies`, nature de la demande
  `modification` ou `ajout` ; les autres sont « hors question », comptées par motif, jamais servies ;
- pile = fiches réelles admissibles, puis 12 témoins du lecteur, puis 8 idées tirées au hasard (ordre canonique) ; chaque
  fiche sous la **vue du lecteur** : clés du gabarit seules, dans l'ordre du gabarit (le fichier de l'orchestrateur est
  écrit à clés triées, les témoins dans l'ordre du gabarit : sans réordonner, l'ordre des clés trahirait l'origine),
  typographie ramenée à la forme de l'orchestrateur (`normaliser_typographie`, recopiée de `pole/ideation_v2.py`) ;
  les champs retirés sont consignés, jamais silencieusement ;
- deux ordres indépendants : `numpy.random.SeedSequence(2026111302).spawn(4)`, enfants 0 et 1 ; étiquettes F01… dans
  l'ordre de chaque lecture ; lots consécutifs, ⌈n/20⌉ lots de tailles égales à un près (20 au plus) ;
- garde de dépense avant envoi (borne haute du relais : (octets du corps + 1024) × 2 USD/M + max_tokens × 10 USD/M) :
  la somme des pires cas ≤ 4,0 USD (réserve du lecteur), au plus 6 appels (`--max-appels 6` du relais) ; `max_tokens`
  = min(32 768, part égale de la réserve), refus sous 16 384 ;
- écrit, chacun scellé : `envoi-<L>-lot<k>-v2.txt` (message), `envoi-<L>-lot<k>-v2.corps.json` (corps), `pile-interne-v2.json`
  et `cle-lectures-v2.json` (**jamais envoyés** : origine des fiches et correspondance des étiquettes),
  `manifeste-envois-v2.json` (graines, versions, empreintes, garde de dépense, réponses attendues).

`verifier` lit les réponses `reponse-<L>-lot<k>-v2.json` (réponse entière du relais, `chat.completion`, scellée par la mère)
et écrit `lecture-verifiee-<L>-v2.json` (scellé) : pour chaque fiche et chaque critère, la valeur brute, la valeur comptée,
et la raison d'un « non prouvé ». Règle (§ 4.5) : un 1 à R1–R7 compte seulement si `passage` se trouve mot pour mot,
espaces normalisés, dans une chaîne de la fiche servie ; une occupation `Ck` compte seulement si `passage_fiche` est dans
la fiche et `passage_catalogue` dans l'entrée `Ck` du catalogue servi ; sinon la lecture compte `aucune`. R4 hors
`levier:juge` vaut 1 par programme (§ 4.4).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path

import numpy as np

VERSION = "outil-lecteur-conception-propre-v2"
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
TAILLE_LOT = 20
LECTURES = ("L1", "L2")
MODELE_LECTEUR = "kimi-k3.1-pro"
PRIX_ENTREE_USD_M, PRIX_SORTIE_USD_M = 2.0, 10.0
RESERVE_LECTEUR_USD = 4.0
MAX_APPELS = 6
MAX_TOKENS, MIN_TOKENS = 32768, 16384
LEVIERS = ("levier:juge", "levier:proposeurs", "levier:composition", "levier:cout")
NATURES_ADMISES = ("modification", "ajout")
CRITERES = ("R1", "R2", "R3", "R4", "R5", "R6", "R7")
LONGUEUR_MIN_PASSAGE = 20      # M1 : caractères hors espaces ; la consigne borne en haut à 200
LONGUEUR_MAX_CONSIGNE = 200    # rapporté seulement (un passage plus long n'est pas refusé)
CELLULE_MECANISME = 2          # colonnes du catalogue : Code | Conception | Mécanisme central | Source
DOSSIER_RUNS = "runs/course-ideation-conception-propre-v1"
MOTIF_RUN = r"\d{8}-\d{6}-course-ideation-conception-propre-v1-g1"
NOM_COPIE_FICHES = "sortie--fiches-validees.json"
MANIFESTE_FIN = "manifeste-lanceur-fin.json"
ANOMALIES_BLOQUANTES = ("reponse_illisible", "fin_non_stop", "entree_manquante", "entree_en_double")
CODES_CATALOGUE = tuple(f"C{i}" for i in range(1, 13))
CHAMPS_INTERNES = ("auteur", "identifiant_auteur", "empreinte", "passe", "temoin")  # toujours retirés (orchestrateur)
ATTESTATION_CHAMPS = ("lecteur", "lu_le", "fiches_validees_sha256", "aucune_recette_aucun_secret",
                      "envoi_au_lecteur_externe_permis")
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
    """Arrêt sans repli : rien n'est écrit de plus."""


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


def ecrire_scelle(chemin, texte: str) -> str:
    """Écrit un fichier neuf et son compagnon ; refuse d'écraser (R12)."""
    p = Path(chemin)
    if p.exists() or Path(str(p) + ".sha256").exists():
        raise Refus(f"{p} existe déjà : on n'écrase jamais (R12)")
    b = texte.encode("utf-8")
    p.write_bytes(b)
    h = sha256_octets(b)
    Path(str(p) + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


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


# --- vue du lecteur ---------------------------------------------------------------------------------------------------

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


def corps_requete(message: str, max_tokens: int) -> str:
    return json.dumps({"model": MODELE_LECTEUR, "messages": [{"role": "user", "content": message}],
                       "max_tokens": max_tokens}, ensure_ascii=False)


def pire_cas_usd(octets: int, max_tokens: int) -> float:
    return (octets + 1024) * PRIX_ENTREE_USD_M / 1e6 + max_tokens * PRIX_SORTIE_USD_M / 1e6


def preparer(fiches_chemin, attestation_chemin, sortie, racine=RACINE_DEFAUT) -> dict:
    racine = Path(racine)
    sortie = Path(sortie)
    if sortie.exists() and any(sortie.iterdir()):
        raise Refus(f"{sortie} existe et n'est pas vide : on n'écrase jamais (R12)")
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
        raise Refus(f"{appels} appels > {MAX_APPELS} permis par le relais (pile de {n} fiches)")
    # messages, puis max_tokens par part égale de la réserve
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
    part = RESERVE_LECTEUR_USD / appels
    max_tok = MAX_TOKENS
    for msg in messages.values():
        octets = len(corps_requete(msg, MAX_TOKENS).encode("utf-8"))
        permis = math.floor((part - (octets + 1024) * PRIX_ENTREE_USD_M / 1e6) / (PRIX_SORTIE_USD_M / 1e6))
        max_tok = min(max_tok, permis)
    if max_tok < MIN_TOKENS:
        raise Refus(f"max_tokens permis {max_tok} < {MIN_TOKENS} : la réserve de {RESERVE_LECTEUR_USD} USD ne suffit pas")
    sortie.mkdir(parents=True, exist_ok=True)
    fichiers, garde = {}, []
    for (L, k), msg in sorted(messages.items()):
        nom_m, nom_c = f"envoi-{L}-lot{k}-v2.txt", f"envoi-{L}-lot{k}-v2.corps.json"
        corps = corps_requete(msg, max_tok)
        fichiers[nom_m] = ecrire_scelle(sortie / nom_m, msg)
        fichiers[nom_c] = ecrire_scelle(sortie / nom_c, corps)
        garde.append({"envoi": nom_c, "octets": len(corps.encode("utf-8")),
                      "pire_cas_usd": round(pire_cas_usd(len(corps.encode("utf-8")), max_tok), 6)})
    total = sum(g["pire_cas_usd"] for g in garde)
    if total > RESERVE_LECTEUR_USD + 1e-9:  # garde redondante (ne devrait jamais tenir)
        raise Refus(f"pire cas total {total:.4f} > {RESERVE_LECTEUR_USD}")
    fichiers["pile-interne-v2.json"] = ecrire_scelle(sortie / "pile-interne-v2.json", json_texte(pile))
    fichiers["cle-lectures-v2.json"] = ecrire_scelle(sortie / "cle-lectures-v2.json", json_texte(cle))
    e = enfants_ordres()
    manifeste = {
        "version": VERSION, "outil_sha256": sha256_fichier(__file__),
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
        "lots": {"nombre_par_lecture": len(lots_idx), "tailles": [len(x) for x in lots_idx]},
        "garde_depense": {"modele": MODELE_LECTEUR, "max_tokens": max_tok, "appels": appels,
                          "reserve_usd": RESERVE_LECTEUR_USD, "pire_cas_total_usd": round(total, 6), "envois": garde},
        "reponses_attendues": [f"reponse-{L}-lot{k}-v2.json" for L in LECTURES for k in range(1, len(lots_idx) + 1)],
        "fichiers": fichiers,
        "jamais_envoyes": ["pile-interne-v2.json", "cle-lectures-v2.json", "manifeste-envois-v2.json"],
    }
    ecrire_scelle(sortie / "manifeste-envois-v2.json", json_texte(manifeste))
    return manifeste


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


def lire_reponse(chemin) -> tuple[str, dict]:
    verifier_sceau(chemin)
    r = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if r.get("model") != MODELE_LECTEUR:
        raise Refus(f"{Path(chemin).name} : modèle servi {r.get('model')!r} ≠ {MODELE_LECTEUR}")
    ch = r.get("choices")
    if not isinstance(ch, list) or len(ch) != 1:
        raise Refus(f"{Path(chemin).name} : un seul choix attendu")
    contenu = (ch[0].get("message") or {}).get("content")
    if not isinstance(contenu, str):
        raise Refus(f"{Path(chemin).name} : contenu absent")
    return contenu, {"finish_reason": ch[0].get("finish_reason"), "usage": r.get("usage")}


def entree_vide(motif: str, juge: bool) -> dict:
    res = {c: {"brut": None, "compte": 0, "prouve": False, "motif": motif} for c in CRITERES}
    if not juge:
        res["R4"] = {"brut": None, "compte": 1, "prouve": True, "motif": "hors levier:juge : 1 par programme"}
    res["N"] = {"brut": None, "compte": "aucune", "occupation_non_prouvee": False, "motif": motif}
    return res


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
            anomalies.append({"genre": "etiquette_hors_lot", "detail": str(et)[:40]})
            continue
        vues_dans_ordre.append(et)
        par_et.setdefault(et, []).append(e)
    if [et for et in etiquettes_lot if et in vues_dans_ordre] != list(dict.fromkeys(vues_dans_ordre)):
        anomalies.append({"genre": "ordre_du_lot_non_suivi", "detail": ""})
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
            res[et] = verifier_entree(entrees[0], vue_de[et], juge_de[et], cat)
    return res, anomalies


def charger_envois(dossier) -> dict:
    d = Path(dossier)
    for nom in ("manifeste-envois-v2.json", "pile-interne-v2.json", "cle-lectures-v2.json"):
        verifier_sceau(d / nom)
    man = json.loads((d / "manifeste-envois-v2.json").read_text(encoding="utf-8"))
    for nom, h in man["fichiers"].items():
        if verifier_sceau(d / nom) != h:
            raise Refus(f"{nom} : empreinte différente du manifeste")
    pile = json.loads((d / "pile-interne-v2.json").read_text(encoding="utf-8"))
    cle = json.loads((d / "cle-lectures-v2.json").read_text(encoding="utf-8"))
    return {"manifeste": man, "pile": pile, "cle": cle}


def verifier_lecture(dossier, L: str, catalogue_texte: str) -> dict:
    env = charger_envois(dossier)
    cat = entrees_catalogue(catalogue_texte)
    par_id = {p["id"]: p for p in env["pile"]["fiches"]}
    cle = env["cle"][L]
    fiches, anomalies, reponses = {}, [], {}
    for k, lot in enumerate(cle["lots"], 1):
        nom = f"reponse-{L}-lot{k}-v2.json"
        contenu, meta = lire_reponse(Path(dossier) / nom)
        reponses[nom] = {"sha256": sha256_fichier(Path(dossier) / nom), **meta}
        if meta["finish_reason"] != "stop":
            anomalies.append({"genre": "fin_non_stop", "detail": f"{nom} : {meta['finish_reason']}",
                              "etiquettes": list(lot)})
        vue_de = {et: par_id[cle["etiquettes"][et]]["vue"] for et in lot}
        juge_de = {et: par_id[cle["etiquettes"][et]]["levier"] == "levier:juge" for et in lot}
        res, an = verifier_lot(contenu, lot, vue_de, juge_de, cat)
        anomalies += [{**a, "lot": k} for a in an]
        for a in anomalies:
            if a.get("lot") == k or (a["genre"] == "fin_non_stop" and "lot" not in a):
                a["lot"] = k
                a["ids"] = [cle["etiquettes"][et] for et in a.get("etiquettes", [])]
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
    p.add_argument("--racine", default=str(RACINE_DEFAUT))
    v = s.add_parser("verifier")
    v.add_argument("--envois", required=True)
    v.add_argument("--lecture", choices=LECTURES, action="append")
    v.add_argument("--racine", default=str(RACINE_DEFAUT))
    args = a.parse_args(argv)
    try:
        if args.action == "preparer":
            m = preparer(args.fiches, args.attestation, args.sortie, args.racine)
            print(json.dumps({"pile": m["pile"]["fiches"], "appels": m["garde_depense"]["appels"],
                              "pire_cas_total_usd": m["garde_depense"]["pire_cas_total_usd"],
                              "max_tokens": m["garde_depense"]["max_tokens"]}, ensure_ascii=False))
        else:
            cat, _ = lire_piece(args.racine, "catalogue")
            for L in args.lecture or LECTURES:
                r = verifier_lecture(args.envois, L, cat)
                ecrire_scelle(Path(args.envois) / f"lecture-verifiee-{L}-v2.json", json_texte(r))
                print(json.dumps({"lecture": L, "non_prouves": r["non_prouves"], "anomalies": len(r["anomalies"]),
                                  "anomalies_bloquantes": len(r["anomalies_bloquantes"])}, ensure_ascii=False))
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
