"""Manifeste des moniteurs, référence de la garde 5 de la course du banc fermé — v1.

Pièce d'instrument, classe B (session fille de l'attaquant informé, 22 novembre 2026 ; section D7 bis du préenregistrement
de la course, champ n° 16). Le programme ne rend que des noms, des tailles et des empreintes : **il n'affiche, n'écrit ni
ne renvoie aucun contenu de fichier**. Les octets lus servent au seul calcul de l'empreinte et ne quittent pas la
fonction qui les lit.

Le périmètre n'est pas choisi ici : il est donné par un fichier JSON écrit par qui établit le manifeste (la mère),
ni l'auteur du préenregistrement ni l'opérateur. Forme du périmètre :

    {
      "version": 1,
      "depot": "chemin du dépôt git local",
      "branches": ["*"] ou une liste de motifs de références distantes (fnmatch, sur « origin/… »),
      "motifs_chemins": ["…/*.pt", "…/sondes/**", …],     # motifs fnmatch sur le chemin dans l'arbre
      "stockages": ["/chemin/absolu/d/un/stockage", …]     # dossiers locaux parcourus en entier (facultatif)
    }

Sous-commandes :
- `etablir PERIMETRE SORTIE [--factice]` : parcourt chaque branche distante retenue (`git ls-tree -r`) et chaque stockage,
  garde les fichiers dont le chemin répond à un motif (tout fichier, pour un stockage), écrit SORTIE (JSON) : date UTC,
  empreinte du périmètre, commit de chaque branche, et pour chaque fichier (lieu, chemin, taille, sha256). `--factice`
  marque le manifeste « épreuve » (D7 bis : manifeste d'épreuve pour les épreuves à blanc).
- `verifier-banc MANIFESTE DOSSIER` : garde 5. Calcule l'empreinte de chaque fichier de DOSSIER et refuse (code 5) si une
  empreinte figure au manifeste. Rend le nombre de fichiers vus et le nombre de rencontres, jamais un chemin du manifeste
  ni un contenu. Code 0 si aucune rencontre. Un manifeste factice est refusé hors de `--epreuve`.

Refus (code 4, rien d'écrit) : périmètre mal formé, motif vide, aucune branche retenue, dépôt ou stockage absent, sortie
existante (R12), aucun fichier retenu (un manifeste vide ne protège rien : refus explicite, R5).
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


class Refus(Exception):
    pass


def _sha256_flux(lire) -> tuple[str, int]:
    h, n = hashlib.sha256(), 0
    while True:
        bloc = lire(TAILLE_BLOC)
        if not bloc:
            return h.hexdigest(), n
        h.update(bloc)
        n += len(bloc)


def empreinte_fichier(chemin: str) -> tuple[str, int]:
    with open(chemin, "rb") as f:
        return _sha256_flux(f.read)


def _git(depot: str, *args: str) -> bytes:
    r = subprocess.run(["git", "-C", depot, *args], capture_output=True)
    if r.returncode != 0:
        raise Refus(f"git {args[0]} a échoué (code {r.returncode})")
    return r.stdout


def empreinte_blob(depot: str, objet: str) -> tuple[str, int]:
    with subprocess.Popen(["git", "-C", depot, "cat-file", "blob", objet], stdout=subprocess.PIPE) as p:
        resultat = _sha256_flux(p.stdout.read)
    if p.returncode != 0:
        raise Refus("git cat-file a échoué")
    return resultat


def lire_perimetre(chemin: str) -> dict:
    try:
        with open(chemin, "rb") as f:
            octets = f.read()
        p = json.loads(octets.decode("utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as e:
        raise Refus(f"périmètre illisible ({type(e).__name__})") from e
    if not isinstance(p, dict) or p.get("version") != 1:
        raise Refus("périmètre : version 1 attendue")
    for cle in ("depot", "branches", "motifs_chemins"):
        if cle not in p:
            raise Refus(f"périmètre : clé « {cle} » absente")
    if not isinstance(p["branches"], list) or not p["branches"]:
        raise Refus("périmètre : liste de branches vide")
    motifs = p["motifs_chemins"]
    if not isinstance(motifs, list) or not motifs or any(not isinstance(m, str) or not m.strip() for m in motifs):
        raise Refus("périmètre : motifs de chemins vides ou mal formés")
    stockages = p.get("stockages", [])
    if not isinstance(stockages, list) or any(not isinstance(s, str) or not os.path.isabs(s) for s in stockages):
        raise Refus("périmètre : stockages en chemins absolus attendus")
    if not os.path.isdir(p["depot"]):
        raise Refus("périmètre : dépôt absent")
    for s in stockages:
        if not os.path.isdir(s):
            raise Refus(f"périmètre : stockage absent : {s}")
    p["_sha256"] = hashlib.sha256(octets).hexdigest()
    return p


def branches_retenues(depot: str, motifs: list[str]) -> list[str]:
    refs = _git(depot, "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin").decode().split()
    refs = [r for r in refs if r != "origin/HEAD" and r != "origin"]
    retenues = sorted({r for r in refs if any(fnmatch.fnmatchcase(r, m if m.startswith("origin/") else "origin/" + m)
                                              for m in motifs)})
    if not retenues:
        raise Refus("aucune branche distante retenue par le périmètre")
    return retenues


def _repond(chemin: str, motifs: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(chemin, m) for m in motifs)


def etablir(perimetre: dict, factice: bool) -> dict:
    depot, motifs = perimetre["depot"], perimetre["motifs_chemins"]
    fichiers, commits = [], {}
    for ref in branches_retenues(depot, perimetre["branches"]):
        commits[ref] = _git(depot, "rev-parse", ref).decode().strip()
        for ligne in _git(depot, "ls-tree", "-r", "-z", "--full-tree", ref).split(b"\0"):
            if not ligne:
                continue
            entete, chemin = ligne.split(b"\t", 1)
            _mode, genre, objet = entete.decode().split()
            chemin = chemin.decode("utf-8", "surrogateescape")
            if genre != "blob" or not _repond(chemin, motifs):
                continue
            h, n = empreinte_blob(depot, objet)
            fichiers.append({"lieu": ref, "chemin": chemin, "taille": n, "sha256": h})
    for stockage in perimetre.get("stockages", []):
        for racine, _dossiers, noms in os.walk(stockage):
            for nom in sorted(noms):
                complet = os.path.join(racine, nom)
                if os.path.islink(complet) or not os.path.isfile(complet):
                    continue
                h, n = empreinte_fichier(complet)
                fichiers.append({"lieu": stockage, "chemin": os.path.relpath(complet, stockage), "taille": n,
                                 "sha256": h})
    if not fichiers:
        raise Refus("aucun fichier retenu : un manifeste vide ne protège rien")
    return {
        "version": 1,
        "nature": "épreuve (factice)" if factice else "réel",
        "date_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "perimetre_sha256": perimetre["_sha256"],
        "commits": commits,
        "nombre_fichiers": len(fichiers),
        "empreintes_distinctes": len({f["sha256"] for f in fichiers}),
        "fichiers": sorted(fichiers, key=lambda f: (f["lieu"], f["chemin"])),
    }


def ecrire_exclusif(chemin: str, texte: str) -> None:
    dossier = os.path.dirname(os.path.abspath(chemin))
    fd, tmp = tempfile.mkstemp(dir=dossier, prefix=".manifeste-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(texte)
        os.link(tmp, chemin)
    finally:
        os.unlink(tmp)


def verifier_banc(manifeste: dict, dossier: str) -> tuple[int, int]:
    connues = {f["sha256"] for f in manifeste["fichiers"]}
    vus = rencontres = 0
    for racine, _d, noms in os.walk(dossier):
        for nom in noms:
            complet = os.path.join(racine, nom)
            if os.path.islink(complet) or not os.path.isfile(complet):
                continue
            vus += 1
            if empreinte_fichier(complet)[0] in connues:
                rencontres += 1
    return vus, rencontres


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="python -m controle_ia.manifeste_moniteurs_v1")
    s = p.add_subparsers(dest="commande", required=True)
    e = s.add_parser("etablir")
    e.add_argument("perimetre")
    e.add_argument("sortie")
    e.add_argument("--factice", action="store_true")
    v = s.add_parser("verifier-banc")
    v.add_argument("manifeste")
    v.add_argument("dossier")
    v.add_argument("--epreuve", action="store_true", help="admet un manifeste factice (épreuves à blanc)")
    a = p.parse_args(argv)
    try:
        if a.commande == "etablir":
            if os.path.exists(a.sortie):
                print(f"REFUS : {a.sortie} existe déjà (R12)", file=sys.stderr)
                return 3
            m = etablir(lire_perimetre(a.perimetre), a.factice)
            texte = json.dumps(m, ensure_ascii=False, indent=1) + "\n"
            ecrire_exclusif(a.sortie, texte)
            print(f"manifeste {m['nature']} : {m['nombre_fichiers']} fichiers, {m['empreintes_distinctes']} empreintes "
                  f"distinctes, {len(m['commits'])} branches ; périmètre {m['perimetre_sha256']} ; "
                  f"sortie {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")
            return 0
        try:
            with open(a.manifeste, encoding="utf-8") as f:
                m = json.load(f)
            assert isinstance(m.get("fichiers"), list) and m["fichiers"]
        except (OSError, ValueError, AssertionError) as e:
            raise Refus(f"manifeste illisible ou vide ({type(e).__name__})") from e
        if m.get("nature") != "réel" and not a.epreuve:
            raise Refus("manifeste factice hors épreuve")
        if not os.path.isdir(a.dossier):
            raise Refus("dossier du banc absent")
        vus, rencontres = verifier_banc(m, a.dossier)
        print(f"garde 5 : {vus} fichiers vus sur le banc, {rencontres} rencontre(s) avec le manifeste "
              f"({m['nature']}, {m['date_utc']})")
        return 5 if rencontres else 0
    except Refus as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 4
    except FileExistsError:
        print("REFUS : sortie déjà présente (R12)", file=sys.stderr)
        return 3
    except OSError as e:
        print(f"REFUS : erreur système ({type(e).__name__})", file=sys.stderr)
        return 4


if __name__ == "__main__":
    sys.exit(main())
