"""Montage au processeur (texte scellé, « Plan d'analyse », point 4 ; « Entrées exactes » ; « Liste d'arrêt »).

Briques du montage, chacune avec sa garde :
- clé d'accès lue **par son nom** (`HF_TOKEN`), jamais imprimée ni écrite (`Cle` masque sa valeur) ; modes de débogage refusés ;
- réseau : un `Transport` (réel : `TransportRequests` ; simulé dans les essais) ; essais d'un octet avant tout flux long ;
- identifiants git (contenu d'un petit fichier ; pointeur de stockage d'un fichier de poids) ;
- poids lus **en flux** : SHA-256 sur le flux entier, seuls les octets des tenseurs gardés écrits sur disque ;
- lentille publique : taille, SHA-256, disposition, `provenance`, 31 matrices distinctes de l'identité et deux à deux ;
- code voisin : commit, correctifs (2), (4), (6), comparaison de `readout.py` à la copie versée ;
- jetons gardés : `05_act_corpus.py` puis `03_token_counts.py` (une seule fois), liste `catalog.kept`, nombre et empreinte.
Ce module ne touche aucune sonde. Aucun message d'erreur ne porte la clé ni un en-tête de requête.
"""
from __future__ import annotations

import ast
import hashlib
import json
import logging
import os
import struct
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Protocol

import numpy as np
import torch

from . import constantes_v1 as K
from .constantes_v1 import Arret

HOTE_HF = "https://huggingface.co"
BLOC = 1 << 22
EN_TETE_MAX = 100 * 10 ** 6
EXTENSIONS_DONNEES = (".parquet", ".jsonl", ".json", ".zst", ".gz", ".arrow", ".csv", ".txt")
JOURNAUX_DEBOGAGE = ("urllib3", "httpx", "requests", "huggingface_hub", "http.client", "httpcore")
VARIABLES_CLE = (K.NOM_CLE, "HUGGING_FACE_HUB_TOKEN", "HUGGINGFACE_HUB_TOKEN", "HF_TOKEN_PATH")


# --- clé d'accès -------------------------------------------------------------------------------------------------------------------------
class Cle:
    """Clé d'accès au modèle. Sa valeur ne sort que par `valeur()`, appelée par le seul transport ; `repr` et `str` la
    masquent, et l'objet refuse la sérialisation."""
    __slots__ = ("_Cle__valeur",)

    def __init__(self, valeur: str):
        self.__valeur = valeur

    def valeur(self) -> str:
        return self.__valeur

    def __repr__(self) -> str:
        return "<clé d'accès masquée>"

    __str__ = __repr__

    def __reduce__(self):
        raise Arret("la clé d'accès ne s'écrit ni ne se transmet")


def lire_cle(env=None) -> Cle:
    """Lit `HF_TOKEN` par son nom ; absente ou vide : arrêt avant tout téléchargement, sans rien imprimer d'elle."""
    env = os.environ if env is None else env
    valeur = env.get(K.NOM_CLE)
    if valeur is None or not str(valeur).strip():
        raise Arret(f"clé d'accès au modèle ({K.NOM_CLE}) absente ou vide : arrêt avant tout téléchargement ; nœud")
    return Cle(str(valeur).strip())


def exiger_sans_debogage(env=None) -> None:
    """Aucun mode de débogage d'une bibliothèque de téléchargement (il imprimerait des en-têtes) : sinon arrêt, nœud."""
    env = os.environ if env is None else env
    if str(env.get("HF_DEBUG", "")).strip().lower() not in ("", "0", "false", "no", "off"):
        raise Arret("mode de débogage activé (HF_DEBUG) : arrêt ; nœud")
    if str(env.get("HF_HUB_VERBOSITY", "")).strip().lower() == "debug":
        raise Arret("mode de débogage activé (HF_HUB_VERBOSITY=debug) : arrêt ; nœud")
    for nom in JOURNAUX_DEBOGAGE:
        journal = logging.getLogger(nom)
        if journal.level != logging.NOTSET and journal.level <= logging.DEBUG:
            raise Arret(f"mode de débogage activé (journalisation « debug » de {nom}) : arrêt ; nœud")
    racine = logging.getLogger()
    if racine.level != logging.NOTSET and racine.level <= logging.DEBUG:
        raise Arret("mode de débogage activé (journalisation « debug » à la racine) : arrêt ; nœud")
    import http.client
    if getattr(http.client.HTTPConnection, "debuglevel", 0):
        raise Arret("mode de débogage activé (http.client.HTTPConnection.debuglevel) : arrêt ; nœud")


def environnement_enfant(voisin: Path, hf_home: Path, hors_ligne: bool, env=None) -> dict:
    """Environnement d'un processus enfant (scripts du voisin) : la clé n'y passe jamais."""
    e = {k: v for k, v in (os.environ if env is None else env).items() if k not in VARIABLES_CLE}
    e.pop("HF_HUB_OFFLINE", None)
    e |= {"NEURON_LENS_MODEL": K.DEPOT_LLAMA, "PYTHONPATH": str(voisin), "HF_HOME": str(hf_home),
          "HF_HUB_DISABLE_TELEMETRY": "1", "HF_HUB_DISABLE_IMPLICIT_TOKEN": "1", "PYTHONUNBUFFERED": "1"}
    if hors_ligne:
        e["HF_HUB_OFFLINE"] = "1"
    return e


def aucune_occurrence(dossiers: list[Path], cle: Cle) -> None:
    """Aucun fichier écrit ne porte la valeur de la clé ; sinon arrêt, nœud (Lazar décide d'un changement de clé)."""
    motif = cle.valeur().encode("utf-8")
    for dossier in dossiers:
        for p in sorted(Path(dossier).rglob("*")):
            if not p.is_file() or p.is_symlink():
                continue
            reste = b""
            with open(p, "rb") as f:
                for bloc in iter(lambda: f.read(BLOC), b""):
                    if motif in reste + bloc:
                        raise Arret(f"clé d'accès écrite dans un fichier ({p.name}) : arrêt ; nœud")
                    reste = bloc[-len(motif):]


# --- transport -----------------------------------------------------------------------------------------------------------------------------
class RefusReseau(Arret):
    """Requête refusée ou impossible (le message ne porte que la cible et le code, jamais un en-tête)."""


class Transport(Protocol):
    def octets(self, url: str, cle: Cle | None = None, debut: int | None = None, fin: int | None = None) -> bytes: ...

    def flux(self, url: str, cle: Cle | None = None, debut: int = 0) -> Iterator[bytes]: ...


class TransportRequests:
    """Transport réel. La clé n'est envoyée qu'à l'hôte de Hugging Face (la bibliothèque la retire d'une redirection vers un
    autre hôte) ; aucune journalisation ; les erreurs ne citent que l'URL sans requête et le code."""

    def __init__(self, delai_s: float = 60.0):
        import requests
        self._session = requests.Session()
        self._delai = delai_s

    @staticmethod
    def _cible(url: str) -> str:
        return url.split("?")[0]

    def _ouvrir(self, url: str, cle: Cle | None, debut: int | None, fin: int | None, flux: bool):
        en_tetes = {"Accept-Encoding": "identity"}
        if cle is not None:
            if not url.startswith(HOTE_HF + "/"):
                raise Arret("la clé n'est envoyée qu'à l'hôte de Hugging Face")
            en_tetes["Authorization"] = f"Bearer {cle.valeur()}"
        if debut is not None:
            en_tetes["Range"] = f"bytes={int(debut)}-{'' if fin is None else int(fin)}"
        try:
            r = self._session.get(url, headers=en_tetes, stream=flux, timeout=self._delai, allow_redirects=True)
        except Exception as e:  # jamais le texte de l'exception (il pourrait citer des en-têtes) : son type seulement
            raise RefusReseau(f"requête impossible vers {self._cible(url)} ({type(e).__name__})") from None
        if r.status_code not in (200, 206):
            r.close()
            raise RefusReseau(f"requête refusée par {self._cible(url)} (code {r.status_code})")
        if debut and r.status_code != 206:
            r.close()
            raise RefusReseau(f"{self._cible(url)} : reprise à l'octet {debut} non servie (code {r.status_code})")
        return r

    def octets(self, url, cle=None, debut=None, fin=None) -> bytes:
        r = self._ouvrir(url, cle, debut, fin, flux=debut is not None)
        try:
            if debut is not None and fin is not None:   # ne jamais lire plus que demandé si le serveur ignore l'intervalle
                return r.raw.read(int(fin) - int(debut) + 1)
            return r.content
        finally:
            r.close()

    def flux(self, url, cle=None, debut=0):
        r = self._ouvrir(url, cle, debut or None, None, flux=True)
        try:
            for bloc in r.iter_content(BLOC):
                yield bloc
        except Exception as e:
            raise RefusReseau(f"flux interrompu depuis {self._cible(url)} ({type(e).__name__})") from None
        finally:
            r.close()


def url_fichier(depot: str, revision: str, chemin: str, jeu: bool = False) -> str:
    return f"{HOTE_HF}/{'datasets/' if jeu else ''}{depot}/resolve/{revision}/{chemin}"


def url_arbre(depot: str, revision: str, jeu: bool = False, recursif: bool = False) -> str:
    return f"{HOTE_HF}/api/{'datasets' if jeu else 'models'}/{depot}/tree/{revision}?recursive={'true' if recursif else 'false'}"


@dataclass(frozen=True)
class Cible:
    """Cible d'un essai d'un octet : `sorte` « octet » (un octet exact exigé) ou « en-tête » (réponse non vide exigée)."""
    nom: str
    url: str
    avec_cle: bool = False
    sorte: str = "octet"


def essais_un_octet(transport: Transport, cle: Cle, cibles: list[Cible]) -> list[dict]:
    """Un octet par hôte et par sorte de fichier, avant tout flux long ; un refus : arrêt avant tout téléchargement long."""
    faits = []
    for c in cibles:
        try:
            recu = transport.octets(c.url, cle if c.avec_cle else None, 0, 0)
        except RefusReseau as e:
            raise Arret(f"essai d'un octet refusé ({c.nom}) : {e} : arrêt avant tout téléchargement long ; nœud") from None
        if (c.sorte == "octet" and len(recu) != 1) or (c.sorte != "octet" and len(recu) < 1):
            raise Arret(f"essai d'un octet ({c.nom}) : {len(recu)} octet(s) reçu(s) : arrêt avant tout téléchargement long")
        faits.append({"cible": c.nom, "avec_cle": c.avec_cle, "sorte": c.sorte, "octets": len(recu), "tenu": True})
    return faits


# --- identifiants git --------------------------------------------------------------------------------------------------------------------
def identifiant_git(contenu: bytes) -> str:
    """Identifiant git (SHA-1 d'objet « blob ») d'un contenu."""
    return hashlib.sha1(b"blob %d\0" % len(contenu) + contenu).hexdigest()


def pointeur(sha256: str, taille: int) -> bytes:
    """Pointeur de stockage d'un gros fichier : il contient son SHA-256 et sa taille."""
    return f"version https://git-lfs.github.com/spec/v1\noid sha256:{sha256}\nsize {int(taille)}\n".encode("ascii")


def exiger_pointeur(nom: str, sha256: str, taille: int, identifiant_attendu: str, taille_attendue: int) -> None:
    if int(taille) != int(taille_attendue):
        raise Arret(f"{nom} : taille {taille} différente de celle du texte ({taille_attendue}) : arrêt ; message à la mère")
    if identifiant_git(pointeur(sha256, taille)) != identifiant_attendu:
        raise Arret(f"{nom} : identifiant git du pointeur différent de celui du texte : arrêt ; message à la mère")


def telecharger_petit(transport: Transport, url: str, nom: str, taille: int, identifiant: str, cle: Cle | None = None) -> bytes:
    """Petit fichier téléchargé entier ; taille et identifiant git recalculé comparés au texte."""
    contenu = transport.octets(url, cle)
    if len(contenu) != int(taille) or identifiant_git(contenu) != identifiant:
        raise Arret(f"{nom} : taille ou identifiant git différent de celui du texte : arrêt ; message à la mère")
    return contenu


def sha256_par_interface(transport: Transport, depot: str, revision: str, cle: Cle | None, noms: tuple[str, ...]) -> dict:
    """SHA-256 et taille des fichiers de poids, relus dans l'interface (arbre des fichiers à la révision)."""
    try:
        arbre = json.loads(transport.octets(url_arbre(depot, revision), cle).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise Arret("arbre des fichiers du modèle illisible : arrêt") from None
    sortie = {}
    for e in arbre if isinstance(arbre, list) else []:
        if isinstance(e, dict) and e.get("path") in noms and isinstance(e.get("lfs"), dict):
            sortie[e["path"]] = (str(e["lfs"].get("oid")), int(e["lfs"].get("size", -1)))
    manquants = [n for n in noms if n not in sortie]
    if manquants:
        raise Arret(f"arbre des fichiers du modèle : {manquants} sans SHA-256 de stockage : arrêt")
    return sortie


# --- lecture en flux d'un fichier de poids ---------------------------------------------------------------------------------------------------
class ExtracteurSafetensors:
    """Reçoit le flux d'un fichier `safetensors` (longueur de l'en-tête sur 8 octets, puis description JSON des positions,
    puis les données) ; calcule le SHA-256 du flux entier ; n'écrit sur disque que les octets des tenseurs voulus (fichiers
    `.partiel`, renommés par `conclure` après vérification). Le fichier entier n'est jamais écrit."""

    def __init__(self, voulus: tuple[str, ...], dossier: Path):
        self.voulus, self.dossier = tuple(voulus), Path(dossier)
        self.dossier.mkdir(parents=True, exist_ok=True)
        self.hachage, self.position, self.tampon = hashlib.sha256(), 0, b""
        self.debut_donnees: int | None = None
        self.plages: list[tuple[int, int, str]] = []
        self.description: dict[str, dict] = {}
        self.fichiers: dict[str, object] = {}

    @staticmethod
    def nom_fichier(nom: str) -> str:
        return nom.replace("/", "_") + ".brut"

    def _lire_en_tete(self) -> None:
        if len(self.tampon) < 8:
            return
        n = struct.unpack("<Q", self.tampon[:8])[0]
        if n > EN_TETE_MAX:
            raise Arret("fichier de poids : en-tête d'une longueur invraisemblable : arrêt")
        if len(self.tampon) < 8 + n:
            return
        try:
            en_tete = json.loads(self.tampon[8:8 + n].decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            raise Arret("fichier de poids : en-tête illisible : arrêt") from None
        self.debut_donnees = 8 + n
        for nom in self.voulus:
            if nom not in en_tete:
                raise Arret(f"fichier de poids : tenseur {nom} absent de l'en-tête : arrêt")
            a, b = en_tete[nom]["data_offsets"]
            self.description[nom] = {"dtype": en_tete[nom]["dtype"], "shape": [int(x) for x in en_tete[nom]["shape"]],
                                     "octets": int(b) - int(a)}
            self.plages.append((self.debut_donnees + int(a), self.debut_donnees + int(b), nom))
            self.fichiers[nom] = open(self.dossier / (self.nom_fichier(nom) + ".partiel"), "xb")
        self.tampon = b""

    def recevoir(self, bloc: bytes) -> None:
        """Réception d'un bloc ; la queue d'un bloc qui achève l'en-tête est écrite comme une donnée."""
        self.hachage.update(bloc)
        debut = self.position
        self.position += len(bloc)
        if self.debut_donnees is not None:
            self._ecrire(bloc, debut)
            return
        self.tampon += bloc
        debut_tampon = self.position - len(self.tampon)
        tampon = self.tampon
        self._lire_en_tete()
        if self.debut_donnees is not None and self.position > self.debut_donnees:
            self._ecrire(tampon[self.debut_donnees - debut_tampon:], self.debut_donnees)

    def _ecrire(self, bloc: bytes, debut: int) -> None:
        fin = debut + len(bloc)
        for a, b, nom in self.plages:
            if a < fin and b > debut:
                self.fichiers[nom].write(bloc[max(a, debut) - debut:min(b, fin) - debut])

    def conclure(self, taille_attendue: int, sha256_attendu: str) -> dict[str, dict]:
        """Vérifie la taille et le SHA-256 du flux entier, puis rend définitifs les tenseurs extraits ; sinon arrêt, et aucun
        tenseur extrait de ce flux n'est gardé."""
        for f in self.fichiers.values():
            f.close()
        partiels = {nom: self.dossier / (self.nom_fichier(nom) + ".partiel") for nom in self.fichiers}
        ok = (self.debut_donnees is not None and self.position == int(taille_attendue)
              and self.hachage.hexdigest() == sha256_attendu
              and all(p.stat().st_size == self.description[nom]["octets"] for nom, p in partiels.items()))
        if not ok:
            for p in partiels.values():
                p.unlink(missing_ok=True)
            raise Arret("fichier de poids : taille ou SHA-256 du flux différent de celui du texte : arrêt ; message à la mère")
        for nom, p in partiels.items():
            p.rename(self.dossier / self.nom_fichier(nom))
            self.description[nom]["fichier"] = self.nom_fichier(nom)
        return self.description


def lire_poids_en_flux(transport: Transport, url: str, cle: Cle | None, voulus: tuple[str, ...], dossier: Path,
                       taille: int, sha256: str, reprises: int = 5) -> dict[str, dict]:
    """Lit un fichier de poids en flux (reprise à l'octet atteint si le flux se rompt, au plus `reprises` fois)."""
    ex = ExtracteurSafetensors(voulus, dossier)
    essais = 0
    while True:
        try:
            for bloc in transport.flux(url, cle, ex.position):
                ex.recevoir(bloc)
            break
        except RefusReseau:
            essais += 1
            if essais > reprises or ex.position >= int(taille):
                for f in ex.fichiers.values():
                    f.close()
                for nom in ex.fichiers:
                    (ex.dossier / (ex.nom_fichier(nom) + ".partiel")).unlink(missing_ok=True)
                raise
    return ex.conclure(taille, sha256)


def charger_tenseur(dossier: Path, description: dict, lignes: np.ndarray | None = None) -> np.ndarray:
    """Tenseur extrait, rendu en simple précision (conversion **exacte** de bfloat16 et de la demi-précision). `lignes` :
    ne charger que ces lignes d'une matrice."""
    types = {"BF16": "<u2", "F16": "<f2", "F32": "<f4"}
    if description["dtype"] not in types:
        raise Arret(f"tenseur de type {description['dtype']} : bfloat16, demi ou simple précision attendue")
    brut = np.memmap(Path(dossier) / description["fichier"], dtype=types[description["dtype"]], mode="r",
                     shape=tuple(description["shape"]))
    a = np.asarray(brut[lignes] if lignes is not None else brut)
    if description["dtype"] == "BF16":
        return (a.astype(np.uint32) << 16).view(np.float32)
    return a.astype(np.float32)


def tenseurs_par_fichier(index: bytes, voulus: tuple[str, ...]) -> dict[str, tuple[str, ...]]:
    """Liste des fichiers de poids qui portent un tenseur gardé, lue dans l'index."""
    try:
        carte = json.loads(index.decode("utf-8"))["weight_map"]
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError):
        raise Arret("index des poids illisible : arrêt") from None
    sortie: dict[str, list[str]] = {}
    for nom in voulus:
        if nom not in carte:
            raise Arret(f"index des poids : tenseur {nom} absent : arrêt")
        sortie.setdefault(carte[nom], []).append(nom)
    return {f: tuple(v) for f, v in sorted(sortie.items())}


# --- lentille publique ----------------------------------------------------------------------------------------------------------------------
def telecharger_en_fichier(transport: Transport, url: str, chemin: Path, taille: int, sha256: str,
                           cle: Cle | None = None, reprises: int = 5) -> None:
    """Fichier téléchargé en flux sur disque ; taille et SHA-256 vérifiés ; sinon le fichier est retiré et la course s'arrête."""
    h, n, essais = hashlib.sha256(), 0, 0
    with open(chemin, "xb") as f:
        while True:
            try:
                for bloc in transport.flux(url, cle, n):
                    h.update(bloc)
                    f.write(bloc)
                    n += len(bloc)
                break
            except RefusReseau:
                essais += 1
                if essais > reprises or n >= int(taille):
                    f.close()
                    Path(chemin).unlink(missing_ok=True)
                    raise Arret("lentille publique absente ou illisible : arrêt ; message à la mère ; jamais remplacée par une "
                                "autre lentille ; la lecture par la seule lentille des logits n'est pas rendue") from None
    if n != int(taille) or h.hexdigest() != sha256:
        Path(chemin).unlink(missing_ok=True)
        raise Arret("lentille publique d'une autre taille ou d'une autre empreinte que le texte : arrêt ; message à la mère ; "
                    "jamais remplacée par une autre lentille ; la lecture par la seule lentille des logits n'est pas rendue")


def exiger_fichier_lentille(chemin: Path, taille: int = K.TAILLE_LENTILLE, sha256: str = K.SHA256_LENTILLE) -> None:
    """Lentille publique absente, illisible, d'une autre taille ou d'une autre empreinte : arrêt ; jamais de repli sur la
    seule lentille des logits."""
    suite = (" : arrêt ; message à la mère ; jamais remplacée par une autre lentille ; la lecture par la seule lentille des "
             "logits n'est pas rendue")
    chemin = Path(chemin)
    if not chemin.is_file():
        raise Arret("lentille publique absente" + suite)
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(BLOC), b""):
            h.update(bloc)
    if chemin.stat().st_size != int(taille) or h.hexdigest() != sha256:
        raise Arret("lentille publique d'une autre taille ou d'une autre empreinte que le texte" + suite)


def _egales(a: torch.Tensor, b: torch.Tensor | None, bloc: int = 256) -> bool:
    """Écart maximal ≤ 10⁻⁶ entre `a` et `b` (`b` `None` : l'identité) ; s'arrête au premier bloc de lignes qui diffère."""
    d = a.shape[0]
    for s in range(0, d, bloc):
        x = a[s:s + bloc].float()
        y = torch.eye(d, dtype=torch.float32)[s:s + bloc] if b is None else b[s:s + bloc].float()
        if float((x - y).abs().max()) > K.ECART_MATRICES:
            return False
    return True


def controler_lentille(chemin: Path, largeur: int = K.LARGEUR, couches: tuple[int, ...] = K.COUCHES_LENTILLE,
                       gardees: tuple[int, ...] = K.COUCHES, cible: int = K.COUCHE_CIBLE_LENTILLE):
    """Contrôles de disposition (repris de `neuronpedia_lens`, correctif (2)), de `provenance` et des matrices. Rend (rapport,
    matrices gardées en demi-précision par indice). Toute anomalie : arrêt avant tout calcul ; nœud."""
    try:
        charge = torch.load(chemin, map_location="cpu", weights_only=True, mmap=True)
    except Exception as e:
        raise Arret(f"lentille publique illisible ({type(e).__name__}) : arrêt ; message à la mère ; jamais remplacée par une "
                    "autre lentille ; la lecture par la seule lentille des logits n'est pas rendue") from None
    J = charge.get("J") if isinstance(charge, dict) else None
    ok = isinstance(J, dict) and bool(J) and all(
        type(l) is int and isinstance(m, torch.Tensor) and m.ndim == 2 and tuple(m.shape) == (largeur, largeur)
        and m.dtype == torch.float16 for l, m in J.items())
    if not ok or sorted(J) != list(couches):
        raise Arret(f"lentille publique : disposition autre que {{\"J\": {{{couches[0]}..{couches[-1]}}}}} de matrices "
                    f"{largeur} × {largeur} en demi-précision : arrêt avant tout calcul ; nœud")
    prov = charge.get("provenance")
    if not isinstance(prov, dict) or "capture_point" not in prov:
        raise Arret("lentille publique : clé provenance absente ou sans point de capture lisible : arrêt avant tout calcul ; nœud")
    if prov["capture_point"] != K.POINT_DE_CAPTURE:
        raise Arret(f"lentille publique : point de capture autre que « {K.POINT_DE_CAPTURE} » : arrêt avant tout calcul ; nœud")
    if "target_layer" in prov and prov["target_layer"] != cible:
        raise Arret(f"lentille publique : target_layer différent de {cible} : arrêt avant tout calcul ; nœud")
    if "source_layers" in prov:
        sl = prov["source_layers"]
        if not isinstance(sl, (list, tuple, range)) or [int(x) for x in sl] != list(couches):
            raise Arret("lentille publique : source_layers de provenance différent des couches attendues : arrêt ; nœud")
    if "d_model" in prov and prov["d_model"] != largeur:
        raise Arret("lentille publique : d_model de provenance différent de la largeur attendue : arrêt ; nœud")
    ecarts = {}
    for l in couches:
        if _egales(J[l], None):
            raise Arret(f"lentille publique : la matrice de la couche {l} égale l'identité : arrêt avant tout calcul ; nœud")
        m = J[l].float()
        ecarts[str(l)] = float((m - torch.eye(largeur)).norm() / np.sqrt(largeur))
    paires = 0
    for i, a in enumerate(couches):
        for b in couches[i + 1:]:
            paires += 1
            if _egales(J[a], J[b]):
                raise Arret(f"lentille publique : les matrices des couches {a} et {b} sont égales (écart maximal ≤ 10⁻⁶) : "
                            "arrêt avant tout calcul ; nœud")
    matrices = {int(l): np.ascontiguousarray(J[l].numpy()) for l in gardees}
    from .lecture_v1 import empreinte_matrice
    rapport = {"couches": [int(couches[0]), int(couches[-1])], "largeur": int(largeur), "precision": "float16",
               "autres_cles": sorted(str(k) for k in charge if k != "J"),
               "provenance": {str(k): (v if isinstance(v, (str, int, float, bool, type(None))) else
                                       [int(x) for x in v] if isinstance(v, (list, tuple, range)) else str(type(v).__name__))
                              for k, v in prov.items()},
               "cles_attendues_absentes": [k for k in ("source_layers", "d_model", "n_prompts") if k not in prov],
               "paires_distinctes": paires, "ecart_relatif_a_l_identite_par_couche": ecarts,
               "empreintes_matrices_gardees": {str(l): empreinte_matrice(m) for l, m in matrices.items()}}
    return rapport, matrices


# --- code voisin ---------------------------------------------------------------------------------------------------------------------------
def _git(args: list[str], cwd: Path) -> str:
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        raise Arret(f"git {args[0]} en échec (code {r.returncode}) dans {Path(cwd).name}")
    return r.stdout


def cloner_voisin(dossier: Path, url: str = K.URL_VOISIN, commit: str = K.COMMIT_VOISIN) -> str:
    """Clone du code voisin au commit du texte ; `git rev-parse HEAD` relevé et comparé."""
    dossier = Path(dossier)
    if dossier.exists():
        raise Arret(f"{dossier} existe déjà (R12)")
    _git(["clone", "-q", "--no-checkout", url, str(dossier)], dossier.parent)
    _git(["-c", "advice.detachedHead=false", "checkout", "-q", commit], dossier)
    tete = _git(["rev-parse", "HEAD"], dossier).strip()
    if tete != commit:
        raise Arret(f"code voisin : commit {tete} au lieu de {commit} : arrêt")
    return tete


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(BLOC), b""):
            h.update(bloc)
    return h.hexdigest()


def appliquer_correctifs(voisin: Path, racine_depot: Path, correctifs=K.CORRECTIFS) -> dict:
    """Correctifs (2), (4), (6) appliqués sans commit ; empreinte de chaque correctif comparée au texte ; empreintes des
    fichiers corrigés relevées."""
    for chemin, attendue in correctifs:
        p = Path(racine_depot) / chemin
        if not p.is_file() or sha256_fichier(p) != attendue:
            raise Arret(f"correctif {Path(chemin).name} absent ou d'une autre empreinte que le texte : arrêt")
        _git(["apply", str(p.resolve())], voisin)
    touches = set(_git(["diff", "--name-only"], voisin).split()) | set(
        _git(["ls-files", "--others", "--exclude-standard"], voisin).split())
    return {f: sha256_fichier(Path(voisin) / f) for f in sorted(touches)}


def _source_fonction(source: str, nom: str) -> str:
    for noeud in ast.parse(source).body:
        if isinstance(noeud, ast.FunctionDef) and noeud.name == nom:
            return ast.get_source_segment(source, noeud)
    raise Arret(f"readout.py : fonction {nom} absente : arrêt avant tout calcul ; nœud")


def comparer_readout(chemin_voisin: Path, copie_versee: Path, sha256_copie: str = K.SHA256_COPIE_READOUT) -> dict:
    """`readout.py` du commit comparé à la copie versée dans `rms_norm_columns`, `transport` et `read` (risque connu : la
    copie vient de la branche `main` du voisin) ; un écart : arrêt avant tout calcul ; nœud."""
    if sha256_fichier(copie_versee) != sha256_copie:
        raise Arret("copie versée de readout.py d'une autre empreinte que le texte : arrêt avant tout calcul ; nœud")
    a, b = Path(chemin_voisin).read_text(encoding="utf-8"), Path(copie_versee).read_text(encoding="utf-8")
    for nom in K.FONCTIONS_READOUT:
        if _source_fonction(a, nom) != _source_fonction(b, nom):
            raise Arret(f"readout.py du commit différent de la copie versée dans {nom} (risque connu) : arrêt avant tout calcul ; "
                        "nœud")
    return {"fonctions_egales": list(K.FONCTIONS_READOUT), "sha256_readout_du_commit": sha256_fichier(chemin_voisin),
            "fichier_entier_egal": a == b}


def charger_read_voisin(chemin_readout: Path):
    """Fonction `read` du voisin, chargée du fichier `readout.py` seul (il n'importe que torch)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("readout_voisin_lentilles_bbis", str(chemin_readout),
                                                  loader=importlib.machinery.SourceFileLoader(
                                                      "readout_voisin_lentilles_bbis", str(chemin_readout)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.read


# --- jetons gardés ---------------------------------------------------------------------------------------------------------------------------
def empreinte_liste_gardee(ids) -> str:
    """Même forme que la tranche des lentilles : identifiants triés, un par ligne, ASCII."""
    ids = sorted(int(i) for i in ids)
    if len(set(ids)) != len(ids):
        raise Arret("doublon dans la liste des jetons gardés : arrêt")
    return hashlib.sha256("".join(f"{i}\n" for i in ids).encode("ascii")).hexdigest()


def exiger_jetons_gardes(ids, n: int = K.N_JETONS_GARDES, sha256: str = K.SHA256_JETONS_GARDES) -> dict:
    """Liste des jetons gardés d'un autre nombre ou d'une autre empreinte que le texte : arrêt avant tout calcul ; nœud."""
    e = empreinte_liste_gardee(ids)
    if len(ids) != int(n) or e != sha256:
        raise Arret(f"liste des jetons gardés : {len(ids)} identifiants ou empreinte différents du texte ({n}) : arrêt avant tout "
                    "calcul ; nœud")
    return {"n": len(ids), "sha256": e, "jeton_de_debut_garde": bool(K.JETON_DE_DEBUT in set(int(i) for i in ids))}


def poser_cache_tokeniseur(hf_home: Path, fichiers: dict[str, bytes], depot: str = K.DEPOT_LLAMA,
                           revision: str = K.REVISION_LLAMA) -> Path:
    """Pose les petits fichiers vérifiés de Llama dans le cache des téléchargements, à la révision épinglée, pour que les
    scripts du voisin lisent le tokeniseur sans clé ni réseau."""
    base = Path(hf_home) / "hub" / ("models--" + depot.replace("/", "--"))
    instantane = base / "snapshots" / revision
    instantane.mkdir(parents=True, exist_ok=True)
    for nom, contenu in fichiers.items():
        (instantane / nom).write_bytes(contenu)
    (base / "refs").mkdir(exist_ok=True)
    (base / "refs" / "main").write_text(revision)
    return instantane


SCRIPT_JETONS = (
    "import json, sys\n"
    "from neuron_lens import catalog\n"
    "ids = [int(i) for i in catalog.kept(catalog.MODEL).tolist()]\n"
    "tok = catalog.tokenizer(catalog.MODEL)\n"
    "with open(sys.argv[1], 'x', encoding='utf-8') as f:\n"
    "    json.dump({'modele': catalog.MODEL, 'ids': ids, 'chaines': [tok.decode([i]) for i in ids]}, f)\n")


def jouer_script(commande: list[str], cwd: Path, env: dict, journal: Path) -> None:
    """Joue un script du voisin ; sortie rangée dans un journal du dossier de travail ; échec : arrêt."""
    with open(journal, "xb") as j:
        r = subprocess.run(commande, cwd=cwd, env=env, stdout=j, stderr=subprocess.STDOUT)
    if r.returncode != 0:
        raise Arret(f"{Path(commande[1]).name if len(commande) > 1 else commande[0]} en échec (code {r.returncode}) : arrêt")


def calculer_jetons_gardes(voisin: Path, hf_home: Path, travail: Path, python: str = sys.executable, env=None) -> dict:
    """`05_act_corpus.py` puis `03_token_counts.py` (une seule fois), puis la liste `catalog.kept` et le décodage de chaque
    jeton gardé par le tokeniseur du voisin. Rend `{"ids": […], "chaines": […]}`."""
    sortie = Path(travail) / "jetons-gardes.json"
    if sortie.exists():
        raise Arret("jetons gardés déjà calculés : `03_token_counts.py` ne se joue qu'une fois ; nœud")
    jouer_script([python, "scripts/05_act_corpus.py", "--docs", K.DOCS_CORPUS], voisin,
                 environnement_enfant(voisin, hf_home, False, env), Path(travail) / "journal-05_act_corpus.txt")
    jouer_script([python, "scripts/03_token_counts.py"], voisin, environnement_enfant(voisin, hf_home, True, env),
                 Path(travail) / "journal-03_token_counts.txt")
    jouer_script([python, "-c", SCRIPT_JETONS, str(sortie)], voisin, environnement_enfant(voisin, hf_home, True, env),
                 Path(travail) / "journal-jetons-gardes.txt")
    lu = json.loads(sortie.read_text(encoding="utf-8"))
    if lu.get("modele") != K.DEPOT_LLAMA or len(lu["ids"]) != len(lu["chaines"]):
        raise Arret("jetons gardés : modèle ou longueurs inattendus : arrêt")
    return lu


def cibles_corpus(voisin: Path, transport: Transport) -> list[Cible]:
    """Un fichier de chaque jeu de données du corpus des jetons gardés, d'après les provenances du code voisin corrigé."""
    cibles = []
    for tranche in K.TRANCHES_CORPUS:
        nom = f"act-{tranche}.provenance.json" if tranche != "chat" else "act-chat-llama-3.1-8b-instruct.provenance.json"
        p = Path(voisin) / "data" / "corpus" / nom
        try:
            prov = json.loads(p.read_text(encoding="utf-8"))
            depot, revision = str(prov["repo"]), str(prov["revision"])
        except (OSError, json.JSONDecodeError, KeyError, TypeError):
            raise Arret(f"provenance du corpus {nom} absente ou illisible : arrêt avant tout téléchargement long ; nœud") from None
        try:
            arbre = json.loads(transport.octets(url_arbre(depot, revision, jeu=True, recursif=True)).decode("utf-8"))
        except RefusReseau as e:
            raise Arret(f"essai d'un octet refusé (jeu de données de la tranche {tranche}) : {e} : arrêt avant tout "
                        "téléchargement long ; nœud") from None
        fichiers = sorted(e["path"] for e in arbre if isinstance(e, dict) and e.get("type") == "file"
                          and str(e.get("path", "")).endswith(EXTENSIONS_DONNEES))
        if not fichiers:
            raise Arret(f"jeu de données de la tranche {tranche} : aucun fichier de données dans l'arbre : arrêt ; nœud")
        cibles.append(Cible(f"jeu de données de la tranche {tranche}", url_fichier(depot, revision, fichiers[0], jeu=True)))
    return cibles
