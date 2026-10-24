"""Accès du noyau (root) aux fichiers qu'un organisme contrôle (R-372, « session-depot », 24 octobre 2026).

Le noyau tourne en root ; le dossier de travail d'une lignée appartient à l'utilisateur de l'organisme, qui peut y poser
des liens symboliques (vers `/proc/self/environ` du noyau, vers la banque…), des tubes nommés, des sockets. Une copie ou
une lecture faite par root qui suit un lien met le contenu de la cible là où l'organisme lit (sa vue, son résumé) ; un tube
nommé bloque le noyau. Toute copie ou lecture par root d'un chemin que l'organisme contrôle passe donc par ce module :

- `copier_sans_liens` : parcours sans suivre aucun lien ; seuls les dossiers et les fichiers ordinaires à un seul lien dur
  sont copiés ; liens, tubes, sockets, périphériques, fichiers à plusieurs liens durs sont écartés et **rendus** (chemin et
  raison), pour être consignés par l'appelant (aucun repli silencieux, R5) ;
- `lire_fichier_organisme` : `lstat` (fichier ordinaire, pas un lien, un seul lien dur, taille bornée), ouverture
  `O_NOFOLLOW | O_NONBLOCK`, même fichier après ouverture ; sinon une raison, et rien n'est lu ;
- `elements_non_ordinaires` : ce qu'une copie écarterait, pour refuser un successeur qui en contient ;
- `vrai_dossier` : un dossier qui n'est pas un lien.
"""
from __future__ import annotations

import fnmatch
import os
import pathlib
import shutil
import stat

OCTETS_MAX_REPONSES = 4_000_000       # reponses_test.json (quelques centaines de tâches)
OCTETS_MAX_METRIQUE = 200_000         # metrique_proposee.json
OCTETS_MAX_FIN_CONCEPTION = 20_000    # fin_conception.json (déclaration de l'organisme, recopiée dans les événements)
OCTETS_MAX_RESULTAT = 8_000_000       # resultat.json et modele.npz d'un entraînement


def _raison(s: os.stat_result) -> str | None:
    if stat.S_ISLNK(s.st_mode):
        return "lien symbolique"
    if stat.S_ISDIR(s.st_mode):
        return None
    if not stat.S_ISREG(s.st_mode):
        return "fichier spécial (tube, socket ou périphérique)"
    if s.st_nlink > 1:
        return "plusieurs liens durs"
    return None


def vrai_dossier(chemin: str | pathlib.Path) -> bool:
    try:
        return stat.S_ISDIR(os.lstat(chemin).st_mode)
    except OSError:
        return False


def _ouvrir(chemin: pathlib.Path, s: os.stat_result):
    """Ouvre en lecture sans suivre de lien ni attendre un écrivain ; vérifie que c'est bien le fichier vu par `lstat`."""
    fd = os.open(chemin, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    f = os.fdopen(fd, "rb")
    s2 = os.fstat(f.fileno())
    if not stat.S_ISREG(s2.st_mode) or (s2.st_dev, s2.st_ino) != (s.st_dev, s.st_ino):
        f.close()
        raise OSError("fichier changé entre lstat et ouverture")
    return f


def lire_fichier_organisme(chemin: str | pathlib.Path, octets_max: int) -> tuple[bytes | None, str | None]:
    """(contenu, None) ; ou (None, raison) si le fichier manque, est un lien, n'est pas ordinaire, a plusieurs liens durs,
    dépasse `octets_max`, ou change pendant l'ouverture. La raison « absent » distingue l'absence d'un refus."""
    p = pathlib.Path(chemin)
    try:
        s = os.lstat(p)
    except FileNotFoundError:
        return None, "absent"
    except OSError as e:
        return None, f"illisible ({type(e).__name__})"
    raison = _raison(s) or ("dossier" if stat.S_ISDIR(s.st_mode) else None)
    if raison:
        return None, f"refusé : {raison}"
    if s.st_size > octets_max:
        return None, f"refusé : {s.st_size} octets > {octets_max}"
    try:
        with _ouvrir(p, s) as f:
            donnees = f.read(octets_max + 1)
    except OSError as e:
        return None, f"refusé : ouverture ({str(e)[:80]})"
    if len(donnees) > octets_max:
        return None, f"refusé : plus de {octets_max} octets"
    return donnees, None


def ouvrir_fichier_organisme(chemin: str | pathlib.Path, octets_max: int):
    """Objet fichier binaire ouvert sans suivre de lien (pour `numpy.load`) ; lève `OSError` avec la raison sinon."""
    p = pathlib.Path(chemin)
    s = os.lstat(p)
    raison = _raison(s) or ("dossier" if stat.S_ISDIR(s.st_mode) else None)
    if raison:
        raise OSError(f"refusé : {raison}")
    if s.st_size > octets_max:
        raise OSError(f"refusé : {s.st_size} octets > {octets_max}")
    return _ouvrir(p, s)


def elements_non_ordinaires(dossier: str | pathlib.Path) -> list[str]:
    """Chemins relatifs (et raisons) de ce que `copier_sans_liens` écarterait sous `dossier` ; le dossier lui-même doit être
    un vrai dossier."""
    dossier = pathlib.Path(dossier)
    if not vrai_dossier(dossier):
        return [". : pas un vrai dossier (lien symbolique ou absent)"]
    sortie = []
    for racine, dossiers, fichiers in os.walk(dossier, followlinks=False):
        for nom in sorted(dossiers + fichiers):
            p = pathlib.Path(racine) / nom
            try:
                raison = _raison(os.lstat(p))
            except OSError as e:
                raison = f"illisible ({type(e).__name__})"
            if raison:
                sortie.append(f"{p.relative_to(dossier)} : {raison}")
    return sorted(sortie)


def copier_sans_liens(source: str | pathlib.Path, destination: str | pathlib.Path, ignorer: tuple[str, ...] = ()) -> list[str]:
    """Copie l'arbre `source` dans `destination` (qui ne doit pas exister), sans suivre aucun lien. `ignorer` : motifs de noms
    (comme `shutil.ignore_patterns`), à toute profondeur, omis sans être comptés comme écartés. Rend les éléments écartés
    (« chemin relatif : raison »), triés."""
    source, destination = pathlib.Path(source), pathlib.Path(destination)
    if not vrai_dossier(source):
        raise ValueError(f"copie refusée : la source n'est pas un vrai dossier : {source}")
    destination.mkdir(parents=True, exist_ok=False)
    ecartes: list[str] = []

    def parcourir(rel: pathlib.PurePosixPath | None) -> None:
        dossier = source / rel if rel else source
        try:
            noms = sorted(os.listdir(dossier))
        except OSError as e:
            ecartes.append(f"{rel or '.'} : dossier illisible ({type(e).__name__})")
            return
        for nom in noms:
            if any(fnmatch.fnmatch(nom, m) for m in ignorer):
                continue
            r = (rel / nom) if rel else pathlib.PurePosixPath(nom)
            p = source / r
            try:
                s = os.lstat(p)
            except OSError as e:
                ecartes.append(f"{r} : illisible ({type(e).__name__})")
                continue
            raison = _raison(s)
            if raison:
                ecartes.append(f"{r} : {raison}")
            elif stat.S_ISDIR(s.st_mode):
                (destination / r).mkdir()
                parcourir(r)
            else:
                try:
                    with _ouvrir(p, s) as fsrc, open(destination / r, "xb") as fdst:
                        shutil.copyfileobj(fsrc, fdst)
                    os.utime(destination / r, ns=(s.st_atime_ns, s.st_mtime_ns))
                except OSError as e:
                    ecartes.append(f"{r} : copie refusée ({str(e)[:80]})")

    parcourir(None)
    return sorted(ecartes)
