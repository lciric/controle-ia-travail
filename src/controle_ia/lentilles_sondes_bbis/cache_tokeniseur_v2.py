"""Cache du tokeniseur pour un script du voisin joué **en ligne et sans clé** (première passe ; correctif du tokeniseur pour
`scripts/05_act_corpus.py` ; mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-correctif-tokeniseur-act-corpus-v1.md`, `4420c6df…`).

Le défaut. `montage_v1.poser_cache_tokeniseur` pose les petits fichiers vérifiés du modèle dans le cache des téléchargements, à
la révision épinglée. Hors ligne, cela suffit : la bibliothèque de chargement ne lit que le cache. En ligne, elle résout
d'abord la branche principale du dépôt en son commit (interface publique du dépôt, lue sans clé), puis demande chaque fichier
de tokeniseur qu'elle connaît ; un fichier **ni posé ni marqué absent** dans le cache est demandé à l'hôte, qui répond par le
refus du dépôt à porte (code 401) puisque l'enfant n'a pas la clé : le chargement s'arrête. C'est ce qui arrive au script du
corpus des jetons gardés, le seul que le montage joue en ligne.

La voie (voie (a) du mandat). À côté des fichiers posés, le cache reçoit, pour chaque fichier que la bibliothèque demande et
que le dépôt **ne porte pas** à la révision épinglée, le marqueur d'absence de la bibliothèque des téléchargements : un
fichier vide `.no_exist/<révision>/<nom>`. Pour une révision résolue en commit, la bibliothèque de chargement tient alors le
cache pour complet et ne demande plus rien à l'hôte pour ces noms. La clé ne passe à aucun enfant ; rien n'est téléchargé de
plus ; le voisin n'est pas touché.

Un marqueur est une affirmation sur le dépôt ; elle est vérifiée avant d'être écrite, jamais supposée :
- l'arbre de la racine du dépôt du modèle, à la révision épinglée, est lu **par le lanceur, avec la clé** (même adresse que
  `montage_v1.sha256_par_interface`) ;
- témoin : chaque fichier posé doit y figurer comme fichier (un arbre vide, tronqué ou d'un autre dépôt arrête) ;
- chaque nom à marquer doit en être absent ; présent : arrêt nommé, nœud (le poser demanderait une taille et un identifiant
  de contenu fixés par le texte : aucune règle n'est inventée ici) ;
- après la pose, et à chaque appel de `exiger_cache`, le cache est relu sur disque : la branche principale y désigne la
  révision épinglée, l'instantané ne porte que les fichiers posés, chacun de la taille et de l'identifiant de contenu du
  texte, et les marqueurs sont exactement ceux attendus, tous vides.
Ce module ne lit ni n'écrit la valeur de la clé : il la passe au transport, qui seul l'emploie ; aucun message ne la porte.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from . import constantes_v1 as K
from . import montage_v1 as mo
from .constantes_v1 import Arret

# Fichiers que la bibliothèque de chargement (transformers 5.18.0, huggingface_hub 1.33.0 : `requirements-cpu.txt`) demande
# pour le tokeniseur, en plus des quatre fichiers `.json` posés, et que le dépôt du modèle ne porte pas à sa racine. Relevé par
# l'essai local contre une porte simulée (note du correctif) : sans l'un des trois, le chargement en ligne et sans clé lève le
# refus du dépôt à porte ; avec les trois, aucun fichier n'est demandé à l'hôte.
ABSENTS_CONNUS = ("tokenizer.model", "added_tokens.json", "chat_template.jinja")
DOSSIER_ABSENTS = ".no_exist"                      # nom fixé par la bibliothèque des téléchargements
BRANCHE = "main"
BORNE_ARBRE = 1000                                 # une page d'arbre porte au plus 1 000 entrées : à ce nombre, l'arbre peut être coupé
_NOM_SIMPLE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")


def base_du_cache(hf_home: Path, depot: str = K.DEPOT_LLAMA) -> Path:
    """Dossier du dépôt du modèle dans le cache des téléchargements (même forme que `montage_v1.poser_cache_tokeniseur`)."""
    return Path(hf_home) / "hub" / ("models--" + depot.replace("/", "--"))


def exiger_noms(fichiers, absents) -> None:
    """Noms de fichiers de la racine seulement, sans dossier ; aucun nom à la fois posé et marqué absent ; aucun doublon."""
    fichiers, absents = list(fichiers), list(absents)
    for nom in fichiers + absents:
        if not isinstance(nom, str) or not _NOM_SIMPLE.fullmatch(nom):
            raise Arret(f"cache du tokeniseur : nom de fichier inattendu ({nom!r}) : seuls des noms de la racine du dépôt se posent "
                        "ou se marquent ; arrêt ; nœud")
    if len(set(absents)) != len(absents) or len(set(fichiers)) != len(fichiers):
        raise Arret("cache du tokeniseur : un nom est donné deux fois : arrêt ; nœud")
    communs = sorted(set(fichiers) & set(absents))
    if communs:
        raise Arret(f"cache du tokeniseur : {communs} à la fois posé et marqué absent : arrêt ; nœud")


def racine_du_depot(transport: mo.Transport, cle: mo.Cle | None, depot: str = K.DEPOT_LLAMA,
                    revision: str = K.REVISION_LLAMA) -> dict[str, str]:
    """Entrées de la racine du dépôt du modèle à la révision épinglée (chemin → sorte), lues par le transport avec la clé."""
    try:
        brut = transport.octets(mo.url_arbre(depot, revision), cle)
    except mo.RefusReseau as e:
        raise Arret(f"arbre des fichiers du modèle refusé ({e}) : l'absence d'un fichier ne peut pas être vérifiée : arrêt avant "
                    "tout flux long ; nœud") from None
    try:
        arbre = json.loads(brut.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise Arret("arbre des fichiers du modèle illisible : l'absence d'un fichier ne peut pas être vérifiée : arrêt avant tout "
                    "flux long ; nœud") from None
    if not isinstance(arbre, list) or not all(isinstance(e, dict) and isinstance(e.get("path"), str)
                                              and isinstance(e.get("type"), str) for e in arbre):
        raise Arret("arbre des fichiers du modèle d'une forme inattendue : l'absence d'un fichier ne peut pas être vérifiée : arrêt "
                    "avant tout flux long ; nœud")
    if len(arbre) >= BORNE_ARBRE:
        raise Arret(f"arbre des fichiers du modèle : {len(arbre)} entrées, il peut être coupé (page de {BORNE_ARBRE}) : l'absence "
                    "d'un fichier ne peut pas être vérifiée : arrêt avant tout flux long ; nœud")
    racine = {}
    for e in arbre:
        if e["path"] in racine:
            raise Arret("arbre des fichiers du modèle : une entrée en double : arrêt avant tout flux long ; nœud")
        racine[e["path"]] = e["type"]
    return racine


def exiger_absents(racine: dict[str, str], poses, absents) -> None:
    """Témoin : chaque fichier posé figure dans l'arbre comme fichier. Puis : aucun nom à marquer n'y figure."""
    manquants = sorted(n for n in poses if racine.get(n) != "file")
    if manquants:
        raise Arret(f"arbre des fichiers du modèle : {manquants} posé(s) dans le cache mais absent(s) de l'arbre : l'arbre lu n'est "
                    "pas celui de la racine du dépôt à la révision du texte : arrêt avant tout flux long ; nœud")
    presents = sorted(n for n in absents if n in racine)
    if presents:
        raise Arret(f"{presents} existe(nt) à la racine du dépôt du modèle à la révision du texte : aucun marqueur d'absence n'est "
                    "écrit ; le poser dans le cache demande une taille et un identifiant de contenu fixés par le texte : arrêt avant "
                    "tout flux long ; nœud")


def _entrees(dossier: Path) -> list[Path]:
    return sorted(dossier.iterdir()) if dossier.is_dir() and not dossier.is_symlink() else []


def exiger_cache(hf_home: Path, attendus: dict[str, tuple[int, str]], depot: str = K.DEPOT_LLAMA,
                 revision: str = K.REVISION_LLAMA, absents=ABSENTS_CONNUS) -> dict:
    """Relit le cache sur disque. `attendus` : nom → (taille, identifiant de contenu) du texte, pour chaque fichier posé.
    Arrêt si la branche principale ne désigne plus la révision épinglée, si l'instantané porte autre chose que les fichiers
    posés, si un fichier est d'une autre taille ou d'un autre identifiant, si les marqueurs d'absence ne sont pas exactement
    ceux attendus ou si l'un d'eux n'est pas vide."""
    exiger_noms(attendus, absents)
    base = base_du_cache(hf_home, depot)
    ref = base / "refs" / BRANCHE
    try:
        designe = ref.read_text(encoding="utf-8") if ref.is_file() and not ref.is_symlink() else None
    except (OSError, UnicodeDecodeError):
        designe = None
    if designe != revision:
        raise Arret("cache du tokeniseur : la branche principale n'y désigne pas la révision du texte (la branche du dépôt a bougé, "
                    "ou le cache a été réécrit) : arrêt ; nœud")
    if [p.name for p in _entrees(base / "refs")] != [BRANCHE] or [p.name for p in _entrees(base / "snapshots")] != [revision]:
        raise Arret("cache du tokeniseur : une autre branche ou une autre révision que celle du texte y figure : arrêt ; nœud")
    instantane = base / "snapshots" / revision
    poses = _entrees(instantane)
    if sorted(p.name for p in poses) != sorted(attendus) or any(p.is_symlink() or not p.is_file() for p in poses):
        raise Arret("cache du tokeniseur : l'instantané ne porte pas exactement les fichiers posés : arrêt ; nœud")
    fichiers = {}
    for p in poses:
        contenu = p.read_bytes()
        taille, identifiant = attendus[p.name]
        if len(contenu) != int(taille) or mo.identifiant_git(contenu) != identifiant:
            raise Arret(f"cache du tokeniseur : {p.name} d'une autre taille ou d'un autre identifiant de contenu que celui du "
                        "texte : arrêt ; nœud")
        fichiers[p.name] = {"taille": len(contenu), "identifiant_git": identifiant}
    dossier = base / DOSSIER_ABSENTS
    marqueurs = _entrees(dossier / revision)
    if ([p.name for p in _entrees(dossier)] != ([revision] if absents else [])
            or sorted(p.name for p in marqueurs) != sorted(absents)):
        raise Arret("cache du tokeniseur : les marqueurs d'absence ne sont pas exactement ceux attendus : arrêt ; nœud")
    for p in marqueurs:
        if p.is_symlink() or not p.is_file() or p.stat().st_size != 0:
            raise Arret(f"cache du tokeniseur : le marqueur d'absence {p.name} n'est pas un fichier vide : arrêt ; nœud")
    return {"depot": depot, "revision": revision, "fichiers_poses": fichiers, "marqueurs_d_absence": sorted(absents)}


def poser_cache_tokeniseur(transport: mo.Transport, cle: mo.Cle | None, hf_home: Path, fichiers: dict[str, bytes],
                           attendus: dict[str, tuple[int, str]], depot: str = K.DEPOT_LLAMA, revision: str = K.REVISION_LLAMA,
                           absents=ABSENTS_CONNUS) -> dict:
    """Pose les petits fichiers vérifiés (par `montage_v1.poser_cache_tokeniseur`, inchangé), puis les marqueurs d'absence
    des noms de `absents`, après avoir vérifié sur l'arbre du dépôt que chacun en est absent. Rien n'est écrit si une
    vérification échoue. Rend le relevé de `exiger_cache`, avec les noms de la racine du dépôt."""
    absents = tuple(absents)
    exiger_noms(fichiers, absents)
    if sorted(attendus) != sorted(fichiers):
        raise Arret("cache du tokeniseur : les fichiers à poser et leurs tailles et identifiants attendus ne se répondent pas : "
                    "arrêt ; nœud")
    base = base_du_cache(hf_home, depot)
    if base.exists() or base.is_symlink():
        raise Arret("cache du tokeniseur : le dossier du dépôt du modèle existe déjà dans le cache : rien n'y est réécrit (R12) ; "
                    "arrêt ; nœud")
    racine = racine_du_depot(transport, cle, depot, revision)
    exiger_absents(racine, fichiers, absents)
    mo.poser_cache_tokeniseur(hf_home, fichiers, depot, revision)
    if absents:
        (base / DOSSIER_ABSENTS / revision).mkdir(parents=True)
    for nom in absents:
        with open(base / DOSSIER_ABSENTS / revision / nom, "xb"):
            pass
    return exiger_cache(hf_home, attendus, depot, revision, absents) | {"racine_du_depot": sorted(racine)}
