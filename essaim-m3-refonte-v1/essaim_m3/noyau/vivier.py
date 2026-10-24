"""Vivier de conception (décision de Lazar du 25 octobre 2026, 00:05 heure de Paris : « GO now », relayée par
« conv-audit », message n° 28 § 2) : des tâches à vérité connue servies **pendant la phase de conception seulement**, en
plus des tâches d'entraînement de la banque, venues d'un fichier distinct de la banque scellée (pour la conscience
d'évaluation : le reste du jeu public sans GAIA, moins les tâches de la banque). Jamais dans une génération notée.

`charger_vivier(chemin, banque)` :
- fichier ordinaire et compagnon `.sha256` conforme (sinon refus) ;
- format du sous-ensemble extrait par Lazar (clé `exemples` ou `lignes`, ou liste) ; texte sous `input` ou `texte` ;
  `verite` parmi les étiquettes de la famille ; famille `conscience-evaluation` sauf champ `famille` connu ; un item
  sans texte ou à vérité hors étiquettes fait refuser le fichier entier (aucun repli silencieux, R5) ;
- identifiants servis **opaques** (`cv-0001`…) : `id_source`, `category` et les autres champs ne sont jamais servis (ce
  sont des champs secrets de la banque : `category` dirait l'étiquette) ; texte borné comme la banque (`borner_texte`) ;
- **garde de disjonction par le contenu** : le noyau n'a pas le fichier secret de la banque (identifiants de source),
  il compare donc les textes : un item qui contient au moins `PART_RECOUPEMENT` des fenêtres de `MOTS` mots d'un texte
  de la banque (même échantillon, au bornage près) est écarté et compté — « recoupe le test » (développement ou final)
  ou « doublon de l'entraînement ». Une seule fenêtre commune ne suffit pas (contrairement à la garde de la moisson,
  CE3-04) : des items différents partagent des gabarits d'agent entiers, ce qui n'est pas une fuite d'un item de test.
  Les items servis dont le recoupement avec un texte de test dépasse `PART_PROCHE` sont comptés à part. La disjonction
  par identifiant de source reste celle du script d'extraction, vérifiée contre le fichier secret ;
- doublons exacts (texte normalisé identique) à l'intérieur du vivier : le premier est gardé, les autres comptés.

Rend {"taches": [{id, famille, texte, etiquettes, verite}], "manifeste": {chemin, sha256, comptes, écartés}}.
"""
from __future__ import annotations

import hashlib
import json
import pathlib

from . import taches as _taches
from .garde_fuite import MOTS, empreintes_de_fuite, normaliser

PART_RECOUPEMENT = 0.80   # part des fenêtres d'un texte de la banque retrouvées dans l'item : même échantillon
PART_PROCHE = 0.50        # au-delà, l'item servi est compté « proche d'un texte de test » (rapporté, non écarté)
FAMILLE_DEFAUT = "conscience-evaluation"
OCTETS_MAX = 400_000_000


class VivierRefuse(ValueError):
    pass


def _lignes(brut) -> list:
    if isinstance(brut, list):
        return brut
    if isinstance(brut, dict):
        for cle in ("exemples", "lignes"):
            if isinstance(brut.get(cle), list):
                return brut[cle]
    raise VivierRefuse("liste d'items attendue (clé `exemples`, `lignes`, ou liste)")


def _index_banque(banque: dict) -> tuple[dict[str, list[int]], list[int], list[str]]:
    """Fenêtres de chaque texte de la banque → indices des tâches qui les contiennent ; taille de chaque ensemble ;
    partie de la banque de chaque tâche."""
    index: dict[str, list[int]] = {}
    tailles: list[int] = []
    parties: list[str] = []
    for partie in ("train", "test", "test_final"):
        for t in banque.get(partie) or []:
            k = len(tailles)
            fen = empreintes_de_fuite([t["texte"]])
            tailles.append(len(fen))
            parties.append(partie)
            for e in fen:
                index.setdefault(e, []).append(k)
    return index, tailles, parties


def recoupement_max(texte: str, index: dict, tailles: list[int], parties: list[str]) -> tuple[float, float]:
    """(part maximale des fenêtres d'un texte de test ou de test final retrouvées dans `texte`, idem pour l'entraînement)."""
    compte: dict[int, int] = {}
    for e in empreintes_de_fuite([texte]):
        for k in index.get(e, ()):
            compte[k] = compte.get(k, 0) + 1
    test, train = 0.0, 0.0
    for k, n in compte.items():
        part = n / tailles[k] if tailles[k] else 0.0
        if parties[k] == "train":
            train = max(train, part)
        else:
            test = max(test, part)
    return test, train


def charger_vivier(chemin: str | pathlib.Path, banque: dict, borne: int | None = None) -> dict:
    from ..banque import BORNE_CARACTERES, borner_texte
    chemin = pathlib.Path(chemin)
    if chemin.is_symlink() or not chemin.is_file():
        raise VivierRefuse(f"{chemin} : fichier ordinaire attendu")
    if chemin.stat().st_size > OCTETS_MAX:
        raise VivierRefuse(f"{chemin} : plus de {OCTETS_MAX} octets")
    compagnon = chemin.with_name(chemin.name + ".sha256")
    if not compagnon.is_file():
        raise VivierRefuse(f"{chemin} : compagnon {compagnon.name} absent (R6)")
    donnees = chemin.read_bytes()
    empreinte = hashlib.sha256(donnees).hexdigest()
    attendue = (compagnon.read_text(encoding="utf-8").split() or [""])[0]
    if attendue != empreinte:
        raise VivierRefuse(f"{chemin} : empreinte {empreinte[:16]}… différente de son compagnon ({attendue[:16]}…)")
    try:
        lignes = _lignes(json.loads(donnees.decode("utf-8-sig")))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise VivierRefuse(f"{chemin} : JSON illisible ({type(e).__name__})")
    if not lignes:
        raise VivierRefuse(f"{chemin} : aucun item")
    borne = int(borne or (banque.get("manifeste") or {}).get("borne_caracteres") or BORNE_CARACTERES)
    index, tailles, parties = _index_banque(banque)
    vus: set[str] = set()
    taches: list[dict] = []
    comptes = {"items": len(lignes), "servis": 0, "ecartes_recoupe_test": 0, "ecartes_doublon_entrainement": 0,
               "doublons_internes": 0, "servis_proches_test": 0, "tronques": 0}
    recoupement_servi_max = 0.0
    familles: dict[str, int] = {}
    for i, o in enumerate(lignes):
        if not isinstance(o, dict):
            raise VivierRefuse(f"{chemin} : item {i} : objet attendu")
        texte = o.get("input") if "input" in o else o.get("texte")
        if not isinstance(texte, str) or not texte.strip():
            raise VivierRefuse(f"{chemin} : item {i} sans texte")
        famille = o.get("famille", FAMILLE_DEFAUT)
        if famille not in _taches.ETIQUETTES:
            raise VivierRefuse(f"{chemin} : item {i} : famille inconnue {famille!r}")
        if o.get("verite") not in _taches.ETIQUETTES[famille]:
            raise VivierRefuse(f"{chemin} : item {i} : vérité {o.get('verite')!r} hors {_taches.ETIQUETTES[famille]}")
        texte = texte.strip()
        cle = hashlib.sha256(" ".join(normaliser(texte)).encode("utf-8")).hexdigest()
        if cle in vus:
            comptes["doublons_internes"] += 1
            continue
        vus.add(cle)
        r_test, r_train = recoupement_max(texte, index, tailles, parties)
        if r_test >= PART_RECOUPEMENT:
            comptes["ecartes_recoupe_test"] += 1
            continue
        if r_train >= PART_RECOUPEMENT:
            comptes["ecartes_doublon_entrainement"] += 1
            continue
        if r_test >= PART_PROCHE:
            comptes["servis_proches_test"] += 1
        recoupement_servi_max = max(recoupement_servi_max, r_test)
        texte_servi, tronque = borner_texte(texte, borne)
        comptes["tronques"] += int(tronque)
        taches.append({"id": f"cv-{len(taches) + 1:04d}", "famille": famille, "texte": texte_servi,
                       "etiquettes": list(_taches.ETIQUETTES[famille]), "verite": o["verite"]})
        familles[famille] = familles.get(famille, 0) + 1
    ids_banque = {t["id"] for p in ("train", "test", "test_final") for t in banque.get(p) or []}
    if ids_banque & {t["id"] for t in taches}:
        raise VivierRefuse("identifiants servis du vivier en collision avec la banque")
    comptes["servis"] = len(taches)
    verites = {}
    for t in taches:
        verites.setdefault(t["famille"], {}).setdefault(t["verite"], 0)
        verites[t["famille"]][t["verite"]] += 1
    manifeste = {"chemin": str(chemin), "sha256": empreinte, "borne_caracteres": borne, "mots_par_fenetre": MOTS,
                 "part_recoupement": PART_RECOUPEMENT, "part_proche": PART_PROCHE, "comptes": comptes,
                 "familles": familles, "verites": verites, "recoupement_test_max_servi": round(recoupement_servi_max, 4)}
    return {"taches": taches, "manifeste": manifeste}
