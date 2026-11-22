"""Outil de recherche et de lecture borné aux deux listes de lecture de l'organe « mémoire du dépôt », version 7 (22 novembre 2026).
Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5). Version 7, après la vérification de la v6
(verification-porte-perimetre-v2-v1.md) : V1 un verrou exclusif (fcntl.flock) sur le témoin entoure la lecture du
témoin, l'ajout de la ligne et la mise à jour du témoin, et les lectures parallèles gardent la chaîne ; V2 plus d'option
--depot : le dépôt est MEMOIRE_DEPOT, posé par le lanceur, comme le rôle. Version 6, après la contre-lecture de la porte de
périmètre (contre-lecture-porte-perimetre-v1-v1.md, P2 à P5) : l'appelant ne choisit plus ni le journal, ni le bras, ni
l'agent. Le rôle (MEMOIRE_ROLE : reponse -> bras memo ; boucle -> bras boucle), la session (MEMOIRE_SESSION) et l'agent
(MEMOIRE_AGENT) sont posés par le lanceur de la mère dans l'environnement ; le journal est à chemin fixe :
<depot>/registres/veille-de-cap/journaux-outil/<role>-<AAAA-MM-JJ>.jsonl (date UTC), une ligne par lecture, numérotée,
horodatée et chaînée (empreinte de la ligne précédente) ; un témoin <role>-<AAAA-MM-JJ>.temoin porte le dernier numéro et
la dernière empreinte. Toute écriture impossible arrête l'outil avant de rien montrer. Limite déclarée : un agent de même
privilège peut poser lui-même l'environnement ou réécrire journal et témoin ensemble ; la porte confronte le rôle de chaque
ligne au rôle que la mère a assigné à la session. Version 5 : règles de listes_lecture_v3.py ; la branche
principale n'est plus choisie par l'appelant (R1 de la vérification) : origin/main, sinon main. Version 4 : règles de
listes_lecture_v2.py (B1, C8, C11) ; seuls les fichiers ordinaires (mode 100644 ou 100755) sont vus, liens et sous-modules
exclus (C8, remarque 7) ; noms lus par `ls-tree -z`, accents compris (C9) ; le commit doit être ancêtre de la branche
principale (--ref-principale, défaut origin/main, sinon main) (C7). Règles de chemin :
  bras memo|base : liste d'autorisation v4 (stricte) ; bras boucle : liste de la boucle, trois niveaux (plein, noms, refus).
Un chemin de niveau « noms » est listé, jamais ouvert ni cherché (« REFUS : noms seuls »).
Le répondant ne lit le dépôt QUE par cet outil, au commit épinglé (`git show COMMIT:CHEMIN`), jamais l'arbre de travail.
Chaque fichier dont une ligne est montrée est consigné au journal (JSONL : agent, action, chemin, commit, bras).
Commandes :
  lister [PREFIXE]                       chemins listables au commit (sous PREFIXE) ; rien n'est journalisé (noms seuls)
  chercher MOTIF [PREFIXE] [--i]         lignes qui contiennent l'expression régulière MOTIF, dans les fichiers ouvrables
  lire CHEMIN [--de N] [--a M]           contenu d'un fichier ouvrable (lignes N à M)
  empreinte CHEMIN                       16 premiers signes du SHA-256 du fichier au commit
Options : --commit SHA40 ; environnement posé par le lanceur : MEMOIRE_DEPOT, MEMOIRE_ROLE, MEMOIRE_SESSION, MEMOIRE_AGENT.
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
_spec = importlib.util.spec_from_file_location("ll1", os.path.join(ICI, "listes_lecture_v3.py"))
ll1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ll1)
LIGNES_MAX_SORTIE = 400


def git(depot, *args):
    return subprocess.run(["git", "-C", depot, *args], capture_output=True)


def fichiers(depot, commit):
    """Fichiers ordinaires seulement (mode 100644 ou 100755, type blob) ; noms exacts par -z (C9)."""
    r = git(depot, "ls-tree", "-r", "-z", commit)
    sortie = []
    for ent in r.stdout.split(b"\0"):
        if not ent or b"\t" not in ent:
            continue
        tete, nom = ent.split(b"\t", 1)
        mode, genre, _ = tete.split(b" ", 2)
        if genre == b"blob" and mode in (b"100644", b"100755"):
            sortie.append(nom.decode("utf-8", "replace"))
    return sortie


REFS_PRINCIPALES = ("origin/main", "main")   # figées (R1) ; aucune option ne les change


def ancetre_de_principale(depot, commit):
    refs = REFS_PRINCIPALES
    for r_ in refs:
        if git(depot, "rev-parse", "--verify", "--quiet", r_).returncode == 0:
            return git(depot, "merge-base", "--is-ancestor", commit, r_).returncode == 0
    return False


ROLES = {"reponse": "memo", "boucle": "boucle"}
DOSSIER_JOURNAUX = "registres/veille-de-cap/journaux-outil"


def chemins_journal(depot, role, jour):
    base = os.path.join(depot, DOSSIER_JOURNAUX, f"{role}-{jour}")
    return base + ".jsonl", base + ".temoin"


def journaliser(a, action, chemin):
    """Ajoute une ligne chaînée et met le témoin à jour, sous verrou exclusif ; lève OSError si impossible."""
    import datetime
    import fcntl
    maintenant = datetime.datetime.now(datetime.timezone.utc)
    jour = maintenant.strftime("%Y-%m-%d")
    jpath, tpath = chemins_journal(a.depot, a.role, jour)
    os.makedirs(os.path.dirname(jpath), exist_ok=True)
    with open(jpath[:-len(".jsonl")] + ".verrou", "a") as verrou:
        fcntl.flock(verrou, fcntl.LOCK_EX)
        try:
            _journaliser_sous_verrou(a, action, chemin, maintenant, jpath, tpath)
        finally:
            fcntl.flock(verrou, fcntl.LOCK_UN)


def _journaliser_sous_verrou(a, action, chemin, maintenant, jpath, tpath):
    n, prec = 0, "0" * 64
    if os.path.exists(tpath):
        t = json.load(open(tpath, encoding="utf-8"))
        n, prec = int(t["n"]), str(t["empreinte"])
    ligne = json.dumps({"n": n + 1, "quand": maintenant.strftime("%Y-%m-%dT%H:%M:%SZ"), "session": a.session,
                        "agent": a.agent, "role": a.role, "bras": a.bras, "action": action, "chemin": chemin,
                        "commit": a.commit, "precedent": prec}, ensure_ascii=False)
    with open(jpath, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
    tmp = tpath + ".en-cours"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"n": n + 1, "empreinte": hashlib.sha256(ligne.encode("utf-8")).hexdigest()}, f)
    os.replace(tmp, tpath)


def contenu(a, chemin):
    r = git(a.depot, "show", f"{a.commit}:{chemin}")
    return r.stdout if r.returncode == 0 else None


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("commande", choices=("lister", "chercher", "lire", "empreinte"))
    p.add_argument("args", nargs="*")
    p.add_argument("--commit", required=True)
    p.add_argument("--i", action="store_true", help="recherche sans casse")
    p.add_argument("--de", type=int, default=1)
    p.add_argument("--a", dest="jusqua", type=int, default=None)
    a = p.parse_args(argv)
    a.role = os.environ.get("MEMOIRE_ROLE", "")
    a.session = os.environ.get("MEMOIRE_SESSION", "")
    a.agent = os.environ.get("MEMOIRE_AGENT", "")
    a.depot = os.environ.get("MEMOIRE_DEPOT", "")
    if not a.depot or not os.path.isdir(os.path.join(a.depot, ".git")):
        print("ARRET : MEMOIRE_DEPOT (racine du dépôt de travail) doit être posé par le lanceur", file=sys.stderr)
        return 1
    if a.role not in ROLES or not a.session or not a.agent:
        print("ARRET : MEMOIRE_ROLE (reponse|boucle), MEMOIRE_SESSION et MEMOIRE_AGENT doivent être posés par le lanceur",
              file=sys.stderr)
        return 1
    a.bras = ROLES[a.role]
    if not re.fullmatch(r"[0-9a-f]{40}", a.commit):
        print("ARRET : --commit doit être un SHA complet", file=sys.stderr)
        return 1
    if not ancetre_de_principale(a.depot, a.commit):
        print("ARRET : le commit n'est pas un ancêtre de la branche principale (C7)", file=sys.stderr)
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
                        try:
                            journaliser(a, "chercher", c)
                        except (OSError, ValueError, KeyError) as e:
                            print(f"ARRET : journal impossible ({e})", file=sys.stderr)
                            return 1
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
    if b is None:
        print("REFUS : illisible au commit")
        return 2
    if a.commande == "empreinte":
        print(hashlib.sha256(b).hexdigest()[:16])
        return 0
    try:
        journaliser(a, "lire", c)
    except (OSError, ValueError, KeyError) as e:
        print(f"ARRET : journal impossible ({e})", file=sys.stderr)
        return 1
    lignes = b.decode("utf-8", "replace").split("\n")
    fin = min(len(lignes), a.de + LIGNES_MAX_SORTIE - 1) if a.jusqua is None else min(a.jusqua, len(lignes))
    for i in range(max(1, a.de), fin + 1):
        print(f"{i}\t{lignes[i - 1]}")
    if fin < len(lignes):
        print(f"[suite : --de {fin + 1} ; {len(lignes)} lignes en tout]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
