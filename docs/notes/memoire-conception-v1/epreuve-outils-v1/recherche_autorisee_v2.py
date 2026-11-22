"""Outil de recherche et de lecture borné à la liste d'autorisation, pour les répondants de l'épreuve, version 2 (22 novembre 2026).
Version 2 : règles de verifier_citations_v5 (segment « ne-pas-lire » exclu) ; chaque ligne du journal porte le commit et le bras.

Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5), correction (1) accordée par la mère après l'essai 1
(docs/notes/memoire-conception-v1/epreuve-essai-1-ne-pas-lire-bibliothecaire-v1/verdict-examinateur-essai-1-v1.md).
Le répondant ne lit le dépôt QUE par cet outil. Il lit les fichiers au commit épinglé (`git show COMMIT:CHEMIN`), jamais
l'arbre de travail, et n'en montre que ceux que la liste d'autorisation v2 permet au bras (règles de
verifier_citations_v4.chemin_autorise_bras). Chaque fichier dont une ligne est montrée est consigné au journal
(JSONL : agent, action, chemin) ; le vérificateur juge la porte 1 sur ce journal.
Commandes :
  lister [PREFIXE]                       chemins autorisés au commit (sous PREFIXE) ; rien n'est journalisé (noms seuls)
  chercher MOTIF [PREFIXE] [--i]         lignes qui contiennent l'expression régulière MOTIF, dans les fichiers autorisés
  lire CHEMIN [--de N] [--a M]           contenu d'un fichier autorisé (lignes N à M)
  empreinte CHEMIN                       16 premiers signes du SHA-256 du fichier au commit
Options communes (obligatoires) : --commit SHA40 --bras memo|base --agent NOM --journal JOURNAL.jsonl [--depot .]
Un chemin refusé rend « REFUS : hors périmètre » sans rien montrer ni journaliser de son contenu.
"""
import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("vc4", os.path.join(ICI, "verifier_citations_v5.py"))
vc4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vc4)
LIGNES_MAX_SORTIE = 400


def git(depot, *args):
    return subprocess.run(["git", "-C", depot, *args], capture_output=True)


def fichiers(depot, commit):
    r = git(depot, "ls-tree", "-r", "--name-only", commit)
    return [l for l in r.stdout.decode("utf-8", "replace").split("\n") if l]


def journaliser(a, action, chemin):
    with open(a.journal, "a", encoding="utf-8") as f:
        f.write(json.dumps({"agent": a.agent, "action": action, "chemin": chemin, "commit": a.commit, "bras": a.bras},
                           ensure_ascii=False) + "\n")


def contenu(a, chemin):
    r = git(a.depot, "show", f"{a.commit}:{chemin}")
    return r.stdout if r.returncode == 0 else None


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("commande", choices=("lister", "chercher", "lire", "empreinte"))
    p.add_argument("args", nargs="*")
    p.add_argument("--commit", required=True)
    p.add_argument("--bras", required=True, choices=("memo", "base"))
    p.add_argument("--agent", required=True)
    p.add_argument("--journal", required=True)
    p.add_argument("--depot", default=".")
    p.add_argument("--i", action="store_true", help="recherche sans casse")
    p.add_argument("--de", type=int, default=1)
    p.add_argument("--a", dest="jusqua", type=int, default=None)
    a = p.parse_args(argv)
    if not re.fullmatch(r"[0-9a-f]{40}", a.commit):
        print("ARRET : --commit doit être un SHA complet", file=sys.stderr)
        return 1
    autorises = [c for c in fichiers(a.depot, a.commit) if vc4.chemin_autorise_bras(c, a.bras)[0]]
    if a.commande == "lister":
        pref = vc4.normaliser_chemin(a.args[0]) if a.args else ""
        for c in autorises:
            if not pref or c == pref or c.startswith(pref + "/"):
                print(c)
        return 0
    if a.commande == "chercher":
        if not a.args:
            print("ARRET : motif manquant", file=sys.stderr)
            return 1
        try:
            rx = re.compile(a.args[0], re.IGNORECASE if a.i else 0)
        except re.error as e:
            print(f"ARRET : motif illisible ({e})", file=sys.stderr)
            return 1
        pref = vc4.normaliser_chemin(a.args[1]) if len(a.args) > 1 else ""
        montrees = 0
        for c in autorises:
            if pref and not (c == pref or c.startswith(pref + "/")):
                continue
            if c.lower().endswith((".pdf", ".png", ".gz", ".zip", ".tar", ".jpg")):
                continue
            b = contenu(a, c)
            if b is None:
                continue
            touche = False
            for i, l in enumerate(b.decode("utf-8", "replace").split("\n"), start=1):
                if rx.search(l):
                    if not touche:
                        journaliser(a, "chercher", c)
                        touche = True
                    print(f"{c}:{i}: {l[:500]}")
                    montrees += 1
                    if montrees >= LIGNES_MAX_SORTIE:
                        print(f"[arrêt à {LIGNES_MAX_SORTIE} lignes : affiner le motif ou le préfixe]")
                        return 0
        return 0
    if not a.args:
        print("ARRET : chemin manquant", file=sys.stderr)
        return 1
    c = vc4.normaliser_chemin(a.args[0])
    if c not in autorises:
        print("REFUS : hors périmètre, ou absent au commit")
        return 2
    b = contenu(a, c)
    if a.commande == "empreinte":
        print(hashlib.sha256(b).hexdigest()[:16])
        return 0
    journaliser(a, "lire", c)
    lignes = b.decode("utf-8", "replace").split("\n")
    fin = min(len(lignes), a.de + LIGNES_MAX_SORTIE - 1) if a.jusqua is None else min(a.jusqua, len(lignes))
    for i in range(max(1, a.de), fin + 1):
        print(f"{i}\t{lignes[i - 1]}")
    if fin < len(lignes):
        print(f"[suite : --de {fin + 1} ; {len(lignes)} lignes en tout]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
