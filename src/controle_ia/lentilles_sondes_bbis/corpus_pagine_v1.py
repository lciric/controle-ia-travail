"""Cibles des essais d'un octet du corpus des jetons gardés, quand l'arbre d'un jeu de données est servi par pages
(texte scellé, « Plan d'analyse », point 4 : « un octet d'un fichier de chaque jeu de données du corpus des jetons gardés »).

Le défaut corrigé : `montage_v1.cibles_corpus` ne lit que la première page de l'arbre d'un jeu de données. Quand l'hôte sert
l'arbre par pages (lien de la page suivante dans l'en-tête `Link`, relation « next ») et que la première page ne porte que des
dossiers, il s'arrête sur « aucun fichier de données dans l'arbre » alors que l'arbre en porte.

Ce module rend la même liste de cibles en suivant les pages, dans l'ordre où l'hôte les sert, jusqu'à la première page qui
porte un fichier de données ; la cible est le plus petit chemin de cette page (même tri et mêmes extensions que
`montage_v1`). Quand la première page porte un fichier, le résultat est donc celui de `montage_v1.cibles_corpus`, à l'octet
près. Rien d'autre ne change : mêmes provenances lues, même adresse de départ (`montage_v1.url_arbre`), mêmes phrases d'arrêt
pour une provenance illisible, une requête refusée et un arbre sans fichier de données.

Gardes neuves, chacune avec son arrêt nommé :
- borne du nombre de pages lues par jeu de données (`BORNE_PAGES`) ;
- lien de page suivante qui sort de l'arbre du jeu demandé (autre hôte, autre jeu, autre interface) : jamais suivi ;
- transport qui ne sait pas lire une page avec son lien de suite : arrêt, jamais de repli sur la seule première page.

La clé d'accès n'entre jamais dans ce module : aucune fonction ne la reçoit, les pages de l'arbre d'un jeu de données public
sont demandées sans elle (comme dans `montage_v1`), et aucun message ne porte un en-tête, ni le texte d'une exception de la
bibliothèque de requêtes, ni la requête (curseur) d'une adresse de page ; un lien refusé par la garde n'est pas cité du tout,
et un refus du réseau cite, comme dans `montage_v1`, la cible sans sa requête et le code.

`montage_v1` n'est pas modifié : la lecture d'une page par le transport réel passe par sa propre ouverture
(`TransportRequests._ouvrir`, appelée sans clé), dont les refus gardent leur forme (cible sans requête, code).
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urljoin

from . import constantes_v1 as K
from . import montage_v1 as mo
from .constantes_v1 import Arret

BORNE_PAGES = 100
_RE_LIEN = re.compile(r"<([^<>]*)>((?:\s*;\s*[^,;<>]*)*)")
_RE_RELATION = re.compile(r"""^\s*rel\s*=\s*["']?([^"']*)["']?\s*$""", re.IGNORECASE)


def lien_suivant(en_tete: str | None, url: str) -> str | None:
    """Adresse de la page suivante d'après la valeur de l'en-tête `Link` (relation « next »), rendue absolue par rapport à
    `url` ; `None` si l'en-tête est absent ou ne porte aucune relation « next »."""
    if not en_tete:
        return None
    for lien, parametres in _RE_LIEN.findall(str(en_tete)):
        for parametre in parametres.split(";"):
            relation = _RE_RELATION.match(parametre)
            if relation and "next" in relation.group(1).lower().split():
                return urljoin(url, lien.strip())
    return None


def page_requests(transport: mo.TransportRequests, url: str) -> tuple[bytes, str | None]:
    """Une page par le transport réel, sans clé : ses octets et l'adresse de la page suivante (ou `None`)."""
    r = transport._ouvrir(url, None, None, None, flux=False)
    try:
        try:
            contenu = r.content
        except Exception as e:  # jamais le texte de l'exception : son type seulement
            raise mo.RefusReseau(f"lecture interrompue depuis {transport._cible(url)} ({type(e).__name__})") from None
        return contenu, lien_suivant(r.headers.get("Link"), url)
    finally:
        r.close()


def lire_page(transport, url: str) -> tuple[bytes, str | None]:
    """Octets d'une page et adresse de la suivante. Un transport qui porte une méthode `page(url)` (transports simulés des
    essais) la fournit ; le transport réel de `montage_v1` passe par `page_requests` ; tout autre transport : arrêt (lire la
    seule première page par `octets` referait le défaut en silence)."""
    lire = getattr(transport, "page", None)
    if callable(lire):
        return lire(url)
    if isinstance(transport, mo.TransportRequests):
        return page_requests(transport, url)
    raise Arret("transport sans lecture de page (ni méthode `page`, ni transport réel) : l'arbre d'un jeu de données ne peut pas "
                "être suivi au-delà de sa première page : arrêt avant tout téléchargement long ; nœud")


def fichiers_de_donnees(page: bytes) -> list[str]:
    """Chemins triés des fichiers de données d'une page de l'arbre (même règle que `montage_v1.cibles_corpus`)."""
    arbre = json.loads(page.decode("utf-8"))
    return sorted(e["path"] for e in arbre if isinstance(e, dict) and e.get("type") == "file"
                  and str(e.get("path", "")).endswith(mo.EXTENSIONS_DONNEES))


def dans_l_arbre_du_jeu(url: str, depot: str) -> bool:
    """Vrai si `url` est une page de l'arbre du jeu de données `depot` sur l'hôte de `montage_v1` ; ni la façon dont l'hôte
    écrit la révision dans son lien, ni la requête (curseur) ne sont comparées."""
    return str(url).split("?")[0].startswith(f"{mo.HOTE_HF}/api/datasets/{depot}/tree/")


def premier_fichier_de_donnees(transport, depot: str, revision: str, tranche: str, borne: int = BORNE_PAGES) -> str:
    """Suit les pages de l'arbre du jeu de données jusqu'à la première qui porte un fichier de données ; rend le plus petit
    chemin de cette page. Arbre fini sans fichier : la phrase d'arrêt de `montage_v1`. Plus de `borne` pages : arrêt nommé."""
    url, lues = mo.url_arbre(depot, revision, jeu=True, recursif=True), 0
    while url is not None:
        if lues >= int(borne):
            raise Arret(f"jeu de données de la tranche {tranche} : plus de {int(borne)} pages d'arbre lues sans fichier de données "
                        "(borne du nombre de pages) : arrêt avant tout téléchargement long ; nœud")
        try:
            page, suivant = lire_page(transport, url)
        except mo.RefusReseau as e:
            raise Arret(f"essai d'un octet refusé (jeu de données de la tranche {tranche}) : {e} : arrêt avant tout "
                        "téléchargement long ; nœud") from None
        lues += 1
        fichiers = fichiers_de_donnees(page)
        if fichiers:
            return fichiers[0]
        if suivant is not None and not dans_l_arbre_du_jeu(suivant, depot):
            raise Arret(f"jeu de données de la tranche {tranche} : le lien de la page suivante sort de l'arbre du jeu demandé : il "
                        "n'est pas suivi : arrêt avant tout téléchargement long ; nœud")
        url = suivant
    raise Arret(f"jeu de données de la tranche {tranche} : aucun fichier de données dans l'arbre : arrêt ; nœud")


def cibles_corpus(voisin: Path, transport, borne: int = BORNE_PAGES) -> list[mo.Cible]:
    """Un fichier de chaque jeu de données du corpus des jetons gardés, d'après les provenances du code voisin corrigé ;
    l'arbre de chaque jeu est suivi page par page (`premier_fichier_de_donnees`)."""
    cibles = []
    for tranche in K.TRANCHES_CORPUS:
        nom = f"act-{tranche}.provenance.json" if tranche != "chat" else "act-chat-llama-3.1-8b-instruct.provenance.json"
        p = Path(voisin) / "data" / "corpus" / nom
        try:
            prov = json.loads(p.read_text(encoding="utf-8"))
            depot, revision = str(prov["repo"]), str(prov["revision"])
        except (OSError, json.JSONDecodeError, KeyError, TypeError):
            raise Arret(f"provenance du corpus {nom} absente ou illisible : arrêt avant tout téléchargement long ; nœud") from None
        chemin = premier_fichier_de_donnees(transport, depot, revision, tranche, borne)
        cibles.append(mo.Cible(f"jeu de données de la tranche {tranche}", mo.url_fichier(depot, revision, chemin, jeu=True)))
    return cibles
