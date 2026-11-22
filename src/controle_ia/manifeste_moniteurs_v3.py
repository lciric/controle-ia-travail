"""Manifeste des moniteurs, référence de la garde 5 de la course du banc fermé — v3.

v3 (22 novembre 2026) : copie de manifeste_moniteurs_v2.py (inchangée, R12), après la vérification de Sonnet :
liens vers des dossiers suivis et comptés, avec garde contre les boucles, sur le banc comme dans les stockages ; taille
minimale par défaut à 1 octet (seul le fichier vide est écarté) ; un seuil plus haut doit être écrit au périmètre, et les
fichiers qu'il écarte sont comptés et rapportés ; une étiquette qui ne désigne pas un commit arrête « etablir » (déclaré).

v2 :
Pièce d'instrument, classe B (session fille de l'attaquant informé, 22 novembre 2026 ; section D7 bis du préenregistrement
de la course, champ n° 16). Copie corrigée de manifeste_moniteurs_v1.py (inchangée, R12), après la contre-lecture de
Sonnet (« à reprendre ») : banc vide ou illisible refusé ; noms non UTF-8 rendus en hexadécimal ; toute exception rend un
refus sans trace ; liens, sous-modules et pointeurs de stockage de gros fichiers comptés et rapportés ; fichiers trop
petits écartés de la comparaison et comptés ; toutes les références lues par leur nom complet ; limites déclarées ;
manifeste lu vérifié dans sa forme et, au besoin, par son empreinte.

**Ce que le programme rend** : des noms, des tailles et des empreintes. **Il n'affiche, n'écrit ni ne renvoie aucun
contenu de fichier.** Les octets lus servent au seul calcul de l'empreinte et ne quittent pas la fonction qui les lit.
Un message de refus ne porte jamais de chemin ni d'octet de fichier, seulement le type d'erreur et une raison.

**Le périmètre n'est pas choisi ici** : il est donné par un fichier JSON écrit par qui établit le manifeste (la mère),
ni l'auteur du préenregistrement ni l'opérateur :

    {
      "version": 2,
      "depot": "chemin du dépôt git local (le fetch est fait avant, par l'appelant)",
      "references": ["refs/remotes/*", "refs/heads/*", "refs/tags/*"],   # motifs sur le nom complet de la référence
      "motifs_chemins": ["sondes/*", …],          # fnmatch : « * » traverse « / » ; « ** » vaut « * »
      "exclusions": ["*/__init__.py"],           # facultatif : motifs exclus après les motifs retenus
      "taille_minimale": 1,                      # facultatif (défaut 1 : seul le vide est écarté) ; en deçà, compté
      "stockages": ["/chemin/absolu", …]          # facultatif : dossiers locaux parcourus en entier
    }

**Limites, à dire dans tout usage** : la comparaison est faite octet pour octet par empreinte SHA-256. Un fichier de
moniteur compressé, découpé, réencodé, chiffré, intégré dans une archive ou dans les fichiers d'objets d'une copie du
dépôt échappe à la garde ; un fichier extrait de git avec des filtres (fins de ligne, stockage de gros fichiers) peut
différer de son objet. « Aucune rencontre » veut dire « aucune copie octet pour octet », pas « absent ». Les références
lues sont celles présentes dans le dépôt local au moment de l'appel : la date du dernier fetch est relevée quand elle
existe. Les sous-modules et les pointeurs de stockage de gros fichiers ne sont pas suivis : ils sont comptés et rapportés.
Un fichier sous la taille minimale du périmètre sort de la référence : un petit moniteur (un seuil de quelques octets) n'est
alors plus gardé ; d'où le défaut à 1 octet. Une étiquette qui ne désigne pas un commit arrête l'établissement (refus).
Les liens vers des dossiers sont suivis, une seule fois par dossier réel.

Sous-commandes :
- `etablir PERIMETRE SORTIE [--factice]`.
- `verifier-banc MANIFESTE DOSSIER [--epreuve] [--empreinte-attendue H]` : garde 5. Code 0 si aucune rencontre ;
  code 5 s'il y en a ; code 4 si le banc est vide, illisible, si le manifeste est mal formé, factice hors épreuve,
  ou d'empreinte autre que celle attendue.
Codes : 3 sortie déjà présente (R12) ; 4 refus ; rien n'est écrit en cas de refus.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import fnmatch
import hashlib
import json
import os
import subprocess
import sys
import tempfile

TAILLE_BLOC = 1 << 20
TAILLE_MINIMALE_DEFAUT = 1
TETE_LFS = b"version https://git-lfs.github.com/spec/"


class Refus(Exception):
    pass


def _sha256_flux(lire) -> tuple[str, int, bytes]:
    h, n, tete = hashlib.sha256(), 0, b""
    while True:
        bloc = lire(TAILLE_BLOC)
        if not bloc:
            return h.hexdigest(), n, tete
        if not tete:
            tete = bloc[:len(TETE_LFS)]
        h.update(bloc)
        n += len(bloc)


def empreinte_fichier(chemin: str) -> tuple[str, int]:
    with open(chemin, "rb") as f:
        h, n, _ = _sha256_flux(f.read)
    return h, n


def _git(depot: str, *args: str) -> bytes:
    r = subprocess.run(["git", "-C", depot, *args], capture_output=True)
    if r.returncode != 0:
        raise Refus(f"git {args[0]} a échoué (code {r.returncode})")
    return r.stdout


def _nom_sur(octets_ou_texte) -> dict:
    """Chemin rendu en texte s'il est UTF-8 strict, sinon en hexadécimal : jamais de caractère non représentable."""
    octets = octets_ou_texte if isinstance(octets_ou_texte, bytes) else os.fsencode(octets_ou_texte)
    try:
        return {"chemin": octets.decode("utf-8")}
    except UnicodeDecodeError:
        return {"chemin_hex": octets.hex()}


def _erreur_parcours(e: OSError):
    raise Refus(f"dossier illisible pendant le parcours ({type(e).__name__})")


def parcourir(racine_depart: str, comptes: dict):
    """Rend (chemin complet, est_lien) pour chaque fichier ; suit les liens de dossier une fois par dossier réel."""
    vus = {os.path.realpath(racine_depart)}
    for racine, dossiers, noms in os.walk(racine_depart, onerror=_erreur_parcours, followlinks=True):
        gardes = []
        for d in dossiers:
            complet = os.path.join(racine, d)
            if os.path.islink(complet):
                comptes["liens_dossiers"] = comptes.get("liens_dossiers", 0) + 1
            reel = os.path.realpath(complet)
            if reel in vus:
                comptes["boucles_evitees"] = comptes.get("boucles_evitees", 0) + 1
                continue
            vus.add(reel)
            gardes.append(d)
        dossiers[:] = gardes
        for nom in sorted(noms):
            complet = os.path.join(racine, nom)
            yield complet, os.path.islink(complet)


def lire_perimetre(chemin: str) -> dict:
    try:
        with open(chemin, "rb") as f:
            octets = f.read()
        p = json.loads(octets.decode("utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as e:
        raise Refus(f"périmètre illisible ({type(e).__name__})") from e
    if not isinstance(p, dict) or p.get("version") != 2:
        raise Refus("périmètre : version 2 attendue")
    for cle in ("depot", "references", "motifs_chemins"):
        if cle not in p:
            raise Refus(f"périmètre : clé « {cle} » absente")
    def liste_de_textes(cle, vide_admise):
        v = p.get(cle, [])
        if not isinstance(v, list) or (not v and not vide_admise) or any(not isinstance(m, str) or not m.strip()
                                                                          for m in v):
            raise Refus(f"périmètre : « {cle} » vide ou mal formé")
        return v
    liste_de_textes("references", False)
    liste_de_textes("motifs_chemins", False)
    liste_de_textes("exclusions", True)
    stockages = liste_de_textes("stockages", True)
    if any(not os.path.isabs(s) for s in stockages):
        raise Refus("périmètre : stockages en chemins absolus attendus")
    t = p.get("taille_minimale", TAILLE_MINIMALE_DEFAUT)
    if not isinstance(t, int) or isinstance(t, bool) or t < 1:
        raise Refus("périmètre : taille_minimale entière ≥ 1 attendue")
    if not isinstance(p["depot"], str) or not os.path.isdir(p["depot"]):
        raise Refus("périmètre : dépôt absent")
    for s in stockages:
        if not os.path.isdir(s):
            raise Refus("périmètre : un stockage est absent")
    p["_sha256"] = hashlib.sha256(octets).hexdigest()
    return p


def references_retenues(depot: str, motifs: list[str]) -> list[str]:
    refs = _git(depot, "for-each-ref", "--format=%(refname)").decode("utf-8", "replace").split()
    retenues = sorted({r for r in refs if not r.endswith("/HEAD") and any(fnmatch.fnmatchcase(r, m) for m in motifs)})
    if not retenues:
        raise Refus("aucune référence retenue par le périmètre")
    return retenues


def _retenu(chemin: str, motifs: list[str], exclusions: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(chemin, m) for m in motifs) and not any(
        fnmatch.fnmatchcase(chemin, x) for x in exclusions)


def date_dernier_fetch(depot: str) -> str | None:
    try:
        gitdir = _git(depot, "rev-parse", "--absolute-git-dir").decode().strip()
        t = os.path.getmtime(os.path.join(gitdir, "FETCH_HEAD"))
    except (Refus, OSError):
        return None
    return _dt.datetime.fromtimestamp(t, _dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def etablir(perimetre: dict, factice: bool) -> dict:
    depot, motifs = perimetre["depot"], perimetre["motifs_chemins"]
    exclusions = perimetre.get("exclusions", [])
    seuil = perimetre.get("taille_minimale", TAILLE_MINIMALE_DEFAUT)
    fichiers, commits, cache = [], {}, {}
    comptes = {"liens": 0, "sous_modules": 0, "pointeurs_gros_fichiers": 0, "ecartes_trop_petits": 0,
               "liens_dossiers": 0, "boucles_evitees": 0}

    def garder(lieu, nom, h, n, tete):
        if tete.startswith(TETE_LFS):
            comptes["pointeurs_gros_fichiers"] += 1
        if n < seuil:
            comptes["ecartes_trop_petits"] += 1
            return
        fichiers.append({"lieu": lieu, **_nom_sur(nom), "taille": n, "sha256": h})

    for ref in references_retenues(depot, perimetre["references"]):
        commits[ref] = _git(depot, "rev-parse", ref + "^{commit}").decode().strip()
        for ligne in _git(depot, "ls-tree", "-r", "-z", "--full-tree", ref).split(b"\0"):
            if not ligne:
                continue
            entete, chemin = ligne.split(b"\t", 1)
            mode, genre, objet = entete.decode().split()
            texte = chemin.decode("utf-8", "surrogateescape")
            if not _retenu(texte, motifs, exclusions):
                continue
            if genre == "commit":
                comptes["sous_modules"] += 1
                continue
            if mode == "120000":
                comptes["liens"] += 1
                continue
            if genre != "blob":
                continue
            if objet not in cache:
                with subprocess.Popen(["git", "-C", depot, "cat-file", "blob", objet], stdout=subprocess.PIPE,
                                      stderr=subprocess.DEVNULL) as proc:
                    cache[objet] = _sha256_flux(proc.stdout.read)
                if proc.returncode != 0:
                    raise Refus("git cat-file a échoué")
            garder(ref, chemin, *cache[objet])
    for stockage in perimetre.get("stockages", []):
        for complet, est_lien in parcourir(stockage, comptes):
            if est_lien:
                comptes["liens"] += 1
                if not os.path.exists(complet):
                    continue
            if not os.path.isfile(complet):
                continue
            with open(complet, "rb") as f:  # un lien de fichier est suivi : sa cible est hachée
                h, n, tete = _sha256_flux(f.read)
            garder(stockage, os.path.relpath(complet, stockage), h, n, tete)
    if not fichiers:
        raise Refus("aucun fichier retenu : un manifeste vide ne protège rien")
    return {
        "version": 2,
        "nature": "épreuve (factice)" if factice else "réel",
        "date_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dernier_fetch_utc": date_dernier_fetch(depot),
        "perimetre_sha256": perimetre["_sha256"],
        "taille_minimale": seuil,
        "commits": commits,
        "comptes": comptes,
        "nombre_fichiers": len(fichiers),
        "empreintes_distinctes": len({f["sha256"] for f in fichiers}),
        "fichiers": sorted(fichiers, key=lambda f: (f["lieu"], f.get("chemin", ""), f.get("chemin_hex", ""))),
    }


def ecrire_exclusif(chemin: str, texte: str) -> None:
    dossier = os.path.dirname(os.path.abspath(chemin))
    fd, tmp = tempfile.mkstemp(dir=dossier, prefix=".manifeste-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(texte)
            f.flush()
            os.fsync(f.fileno())
        os.link(tmp, chemin)
    finally:
        os.unlink(tmp)


def lire_manifeste(chemin: str, attendue: str | None) -> dict:
    try:
        with open(chemin, "rb") as f:
            octets = f.read()
        m = json.loads(octets.decode("utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as e:
        raise Refus(f"manifeste illisible ({type(e).__name__})") from e
    if attendue is not None and hashlib.sha256(octets).hexdigest() != attendue:
        raise Refus("manifeste d'empreinte autre que celle attendue")
    if not isinstance(m, dict) or m.get("version") != 2 or m.get("nature") not in ("réel", "épreuve (factice)"):
        raise Refus("manifeste mal formé (version ou nature)")
    fichiers = m.get("fichiers")
    if not isinstance(fichiers, list) or not fichiers:
        raise Refus("manifeste sans fichier")
    for f in fichiers:
        if not isinstance(f, dict) or not isinstance(f.get("sha256"), str) or len(f["sha256"]) != 64:
            raise Refus("manifeste : entrée mal formée")
        if not isinstance(f.get("taille"), int):
            raise Refus("manifeste : entrée sans taille")
    return m


def verifier_banc(manifeste: dict, dossier: str) -> dict:
    connues = {f["sha256"] for f in manifeste["fichiers"]}
    seuil = manifeste.get("taille_minimale", TAILLE_MINIMALE_DEFAUT)
    bilan = {"vus": 0, "rencontres": 0, "liens_suivis": 0, "trop_petits": 0}
    comptes = {}
    for complet, est_lien in parcourir(dossier, comptes):
        if est_lien:
            bilan["liens_suivis"] += 1
            if not os.path.exists(complet):
                continue  # lien mort : rien à comparer, compté
        if not os.path.isfile(complet):
            continue
        h, n = empreinte_fichier(complet)  # suit le lien : la cible est comparée
        bilan["vus"] += 1
        if n < seuil:
            bilan["trop_petits"] += 1
        if h in connues:
            bilan["rencontres"] += 1
    bilan["liens_dossiers_suivis"] = comptes.get("liens_dossiers", 0)
    bilan["boucles_evitees"] = comptes.get("boucles_evitees", 0)
    if bilan["vus"] == 0:
        raise Refus("banc vide : rien n'a été vu, la garde ne peut rien constater")
    return bilan


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="python -m controle_ia.manifeste_moniteurs_v3")
    s = p.add_subparsers(dest="commande", required=True)
    e = s.add_parser("etablir")
    e.add_argument("perimetre")
    e.add_argument("sortie")
    e.add_argument("--factice", action="store_true")
    v = s.add_parser("verifier-banc")
    v.add_argument("manifeste")
    v.add_argument("dossier")
    v.add_argument("--epreuve", action="store_true", help="admet un manifeste factice (épreuves à blanc)")
    v.add_argument("--empreinte-attendue", default=None)
    a = p.parse_args(argv)
    try:
        if a.commande == "etablir":
            if os.path.exists(a.sortie):
                print("REFUS : sortie déjà présente (R12)", file=sys.stderr)
                return 3
            m = etablir(lire_perimetre(a.perimetre), a.factice)
            texte = json.dumps(m, ensure_ascii=True, indent=1) + "\n"
            ecrire_exclusif(a.sortie, texte)
            print(f"manifeste {m['nature']} : {m['nombre_fichiers']} fichiers, {m['empreintes_distinctes']} empreintes "
                  f"distinctes, {len(m['commits'])} références ; comptes {json.dumps(m['comptes'])} ; "
                  f"dernier fetch {m['dernier_fetch_utc']} ; périmètre {m['perimetre_sha256']} ; "
                  f"sortie {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")
            return 0
        m = lire_manifeste(a.manifeste, a.empreinte_attendue)
        if m["nature"] != "réel" and not a.epreuve:
            raise Refus("manifeste factice hors épreuve")
        if not os.path.isdir(a.dossier):
            raise Refus("dossier du banc absent")
        b = verifier_banc(m, a.dossier)
        print(f"garde 5 : {b['vus']} fichiers vus, {b['rencontres']} rencontre(s), {b['liens_suivis']} lien(s) suivi(s), "
              f"{b['liens_dossiers_suivis']} lien(s) de dossier suivi(s), {b['boucles_evitees']} boucle(s) évitée(s), "
              f"{b['trop_petits']} sous la taille minimale ; manifeste {m['nature']} du {m['date_utc']}")
        return 5 if b["rencontres"] else 0
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 4
    except FileExistsError:
        print("REFUS : sortie déjà présente (R12)", file=sys.stderr)
        return 3
    except Exception as e:  # aucune trace : elle pourrait porter un chemin ou des octets
        print(f"REFUS : erreur inattendue ({type(e).__name__})", file=sys.stderr)
        return 4


if __name__ == "__main__":
    sys.exit(main())
