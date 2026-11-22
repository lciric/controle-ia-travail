"""Outil de recherche et de lecture borné aux deux listes de lecture de l'organe « mémoire du dépôt », version 3 (22 novembre 2026).
Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5). Dérivé de recherche_autorisee_v2.py ; seules changent
les règles de chemin, prises dans fusion-outils-v1/listes_lecture_v1.py :
  bras memo|base : liste d'autorisation v4 (stricte) ; bras boucle : liste de la boucle, trois niveaux (plein, noms, refus).
Un chemin de niveau « noms » est listé, jamais ouvert ni cherché (« REFUS : noms seuls »).
Le répondant ne lit le dépôt QUE par cet outil, au commit épinglé (`git show COMMIT:CHEMIN`), jamais l'arbre de travail.
Chaque fichier dont une ligne est montrée est consigné au journal (JSONL : agent, action, chemin, commit, bras).
Commandes :
  lister [PREFIXE]                       chemins listables au commit (sous PREFIXE) ; rien n'est journalisé (noms seuls)
  chercher MOTIF [PREFIXE] [--i]         lignes qui contiennent l'expression régulière MOTIF, dans les fichiers ouvrables
  lire CHEMIN [--de N] [--a M]           contenu d'un fichier ouvrable (lignes N à M)
  empreinte CHEMIN                       16 premiers signes du SHA-256 du fichier au commit
Options communes (obligatoires) : --commit SHA40 --bras memo|base|boucle --agent NOM --journal JOURNAL.jsonl [--depot .]
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
_spec = importlib.util.spec_from_file_location("ll1", os.path.join(ICI, "listes_lecture_v1.py"))
ll1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ll1)
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
    p.add_argument("--bras", required=True, choices=("memo", "base", "boucle"))
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
    tous = fichiers(a.depot, a.commit)
    listables = [c for c in tous if ll1.autorise_bras(c, a.bras)[1]]
    autorises = [c for c in listables if ll1.autorise_bras(c, a.bras)[0]]
    if a.commande == "lister":
        pref = ll1.normaliser_chemin(a.args[0]) if a.args else ""
        for c in listables:
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
        pref = ll1.normaliser_chemin(a.args[1]) if len(a.args) > 1 else ""
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
    c = ll1.normaliser_chemin(a.args[0])
    if c not in autorises:
        print("REFUS : noms seuls" if c in listables else "REFUS : hors périmètre, ou absent au commit")
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
