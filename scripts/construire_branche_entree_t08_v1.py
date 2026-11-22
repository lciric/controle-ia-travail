#!/usr/bin/env python3
"""Branche d'entrée de la course de T0.8 — v1 (consigne de la chaîne de lancement, `722ceb5e…`, tenue en v3 `6f52c4db…` ; texte au brouillon 15 `8d68b7a0…`, § 3.1).

Règle du texte de T0.8 (« Liste d'arrêt », troisième puce) : le fichier de sondes n'est jamais copié sur la machine, ni comme
fichier ni comme objet git ; la machine ne clone que la branche d'entrée et le code cité. Ce programme :

1. lit, par `git show <commit>:<chemin>` seulement, sans rien ouvrir d'autre, les fichiers de la liste blanche **que la course
   lit**, et leurs compagnons `.sha256` :
   - de la branche de sortie de 7b (commit `--commit-7b`) : les entrées `textes_7b`, `episodes_7b`, `manifeste_7b` de la
     configuration de la course (`course_v1.ENTREES_COURSE_REQUISES`) ; ni `mesures-t06.npz` ni `lecture-cout-t06.json`, que la
     course ne lit pas (ils ne servent qu'à la lecture, sur processeur, hors de la machine) ;
   - du commit du code (`--commit-code`, descendant de `main`) : les entrées `taches`, `consignes`, `invite` de la configuration,
     et le guide de classification que la course charge par `charger_invite("H1-classification")` (l'index des invites et le
     fichier de l'invite, `GUIDE`) ;
   - du commit qui porte le texte scellé (`--commit-texte`) : le texte scellé de T0.8 et la configuration réelle de la course ;
2. vérifie chaque empreinte : contre le compagnon lu au même commit, toujours ; en plus, pour les trois fichiers de 7b, contre
   l'empreinte que porte la configuration (marqueur `EMPREINTES_ENTREES_7B` et entrée de la liste blanche) **et** que porte le
   texte scellé (telle quelle) ; pour les autres entrées de la configuration, contre l'empreinte qu'elle consigne ; le commit
   de 7b doit être cité tel quel par le texte scellé ; un écart arrête tout, rien n'est écrit ;
3. écrit une branche locale **neuve et orpheline** (un seul commit, sans parent) qui ne contient que ces fichiers, à leurs
   chemins, copiés à l'octet (blob identique à celui de la source) ; refuse une branche qui existe (locale ou suivie) ;
4. contrôle par programme la branche écrite (`verifier`, aussi appelé seul par le lanceur) : la liste de ses fichiers est
   exactement la liste blanche ; aucun nom ne commence par `lecture-sondes-t06` ; aucun `resume.json`,
   `distillation-t06.json`, activation, adaptateur, ni fichier `.pt` ou `.safetensors` ; un seul commit, sans parent ; les objets
   de son histoire sont exactement ce commit, ses arbres et les blobs de la liste blanche.

`base-a-t08.json` n'y va jamais (lecture seulement). Le programme ne pousse rien, ne touche aucun registre, n'appelle aucun
réseau : la session mère pousse la branche qu'il a écrite (`git push origin refs/heads/<branche>`).

    python3 -I -B scripts/construire_branche_entree_t08_v1.py construire --depot . --branche entree/t08-course-v1 \
        --commit-7b <40> --commit-code <40> --commit-texte <40> \
        --texte prereg/T0.8-bases-boite-noire-v0-v1.md --config prereg/T0.8-configuration-course-v1.json
    python3 -I -B scripts/construire_branche_entree_t08_v1.py verifier --depot . --ref <ref ou commit> \
        --commit-7b <40> --commit-code <40> --commit-texte <40> --texte … --config …

Codes : 0 conforme (une ligne JSON sur la sortie standard : branche, commit, fichiers et empreintes) ; 1 arrêt (motif sur la
sortie d'erreur, rien d'écrit par `construire`) ; 2 usage.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

VERSION = "construire_branche_entree_t08_v1"
# entrées de la course (course_v1.ENTREES_COURSE_REQUISES) et leur source
ENTREES_7B = ("textes_7b", "episodes_7b", "manifeste_7b")
ENTREES_CODE = ("taches", "consignes", "invite")
ENTREES_COURSE = ENTREES_7B + ENTREES_CODE
FICHIERS_7B_PAR_ENTREE = {"textes_7b": "textes-actions-t06.jsonl", "episodes_7b": "episodes-t06.json",
                          "manifeste_7b": "manifeste.json"}
# guide de classification, chargé par le code (`environnements.invites.charger_invite("H1-classification")`), hors de la
# configuration : l'index scellé des invites et le fichier de l'invite
GUIDE = ("docs/sources/invites-2606.08892-v1/index.json",
         "docs/sources/invites-2606.08892-v1/invites/H1-classification.txt")
_HEX40 = re.compile(r"^[0-9a-f]{40}$")
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_COMPAGNON = re.compile(r"^([0-9a-f]{64})  (\S.*)$")


class Arret(Exception):
    pass


def git(depot: Path, *args: str, entree: bytes | None = None, env: dict | None = None) -> bytes:
    r = subprocess.run(["git", "-C", str(depot), *args], input=entree, capture_output=True,
                       env={**os.environ, **(env or {})})
    if r.returncode != 0:
        raise Arret(f"git {' '.join(args[:3])} … : {r.stderr.decode(errors='replace').strip()[:300]}")
    return r.stdout


def _chemin_sur(chemin: str) -> str:
    if (not isinstance(chemin, str) or not chemin or chemin != chemin.strip() or chemin.startswith("/")
            or ".." in Path(chemin).parts or "\\" in chemin):
        raise Arret(f"chemin {chemin!r} : relatif au dépôt, sans « .. », attendu")
    return chemin


def nom_interdit(chemin: str) -> str | None:
    """Motif interdit sur la branche d'entrée (« Liste d'arrêt », plan point 1 « jamais ») : rend le motif ou None."""
    c = chemin.lower()
    nom = c.rsplit("/", 1)[-1]
    if nom.startswith("lecture-sondes-t06"):
        return "lecture-sondes-t06"
    if nom in ("resume.json", "distillation-t06.json"):
        return nom
    if "activation" in nom:
        return "activation"
    if "adaptateur" in nom:
        return "adaptateur"
    if nom.endswith((".pt", ".safetensors")):
        return "poids"
    if nom.startswith("base-a-t08"):
        return "base-a-t08 (lecture seulement)"
    return None


def montrer(depot: Path, commit: str, chemin: str) -> bytes:
    """Contenu d'un fichier à un commit, par `git show` seul (aucune autre ouverture)."""
    if nom_interdit(chemin):
        raise Arret(f"{chemin} : motif interdit {nom_interdit(chemin)!r} : jamais extrait (arrêt)")
    git(depot, "cat-file", "-e", f"{commit}:{chemin}")
    return git(depot, "show", f"{commit}:{chemin}")


def blob(depot: Path, commit: str, chemin: str) -> str:
    return git(depot, "rev-parse", f"{commit}:{chemin}").decode().strip()


def empreinte_compagnon(contenu: bytes, chemin: str) -> str:
    lignes = [x for x in contenu.decode("utf-8").splitlines() if x.strip()]
    m = _COMPAGNON.match(lignes[0]) if len(lignes) == 1 else None
    if m is None or m.group(2) != Path(chemin).name:
        raise Arret(f"{chemin}.sha256 : une ligne « <empreinte>  {Path(chemin).name} » attendue")
    return m.group(1)


def _tel_quel(texte: str, valeur: str) -> bool:
    """Même règle que `configuration_v1._tel_quel` : valeur bornée par des caractères qui ne la prolongent pas."""
    return re.search(r"(?<![0-9A-Za-z_-])" + re.escape(valeur) + r"(?![0-9A-Za-z_-])", texte) is not None


def _commit(depot: Path, c: str, quoi: str) -> str:
    if not _HEX40.match(str(c)):
        raise Arret(f"{quoi} : commit de 40 caractères hexadécimaux attendu ({c!r})")
    git(depot, "cat-file", "-e", f"{c}^{{commit}}")
    return c


def plan(depot: Path, commit_7b: str, commit_code: str, commit_texte: str, texte: str, config: str,
         cite_7b: str | None = None) -> dict:
    """Liste blanche (chemin → source, empreinte attendue), toutes empreintes vérifiées ; rien n'est écrit. `cite_7b` : commit
    de 7b que le texte doit citer, quand la source des fichiers de 7b est la branche d'entrée elle-même (vérification seule)."""
    depot = Path(depot)
    for c, q in ((commit_7b, "--commit-7b"), (commit_code, "--commit-code"), (commit_texte, "--commit-texte")):
        _commit(depot, c, q)
    cite_7b = cite_7b or commit_7b
    texte, config = _chemin_sur(texte), _chemin_sur(config)
    fichiers: dict[str, dict] = {}

    def prendre(source: str, commit: str, chemin: str, attendues: tuple = ()) -> bytes:
        chemin = _chemin_sur(chemin)
        if chemin in fichiers:
            raise Arret(f"{chemin} cité deux fois dans la liste blanche")
        corps = montrer(depot, commit, chemin)
        comp = montrer(depot, commit, chemin + ".sha256")
        sha = hashlib.sha256(corps).hexdigest()
        sc = empreinte_compagnon(comp, chemin)
        if sha != sc:
            raise Arret(f"{chemin} ({source}) : empreinte {sha[:12]}… ≠ compagnon {sc[:12]}… (R11)")
        for quoi, a in attendues:
            if a != sha:
                raise Arret(f"{chemin} ({source}) : empreinte {sha[:12]}… ≠ {quoi} {str(a)[:12]}… (R11)")
        fichiers[chemin] = {"source": source, "commit": commit, "sha256": sha,
                            "blob": blob(depot, commit, chemin)}
        fichiers[chemin + ".sha256"] = {"source": source, "commit": commit,
                                        "sha256": hashlib.sha256(comp).hexdigest(),
                                        "blob": blob(depot, commit, chemin + ".sha256")}
        return corps

    corps_texte = prendre("texte scellé", commit_texte, texte).decode("utf-8")
    cfg = json.loads(prendre("configuration réelle de la course", commit_texte, config))
    if cfg.get("mode") != "reel":
        raise Arret(f"configuration de la course : mode {cfg.get('mode')!r}, « reel » attendu")
    if not (_HEX40.match(str(cite_7b)) and _tel_quel(corps_texte, cite_7b)):
        raise Arret(f"commit de 7b {cite_7b} non cité tel quel par le texte scellé (tête de la branche de sortie de 7b)")
    entrees = cfg.get("entrees")
    if not isinstance(entrees, dict) or sorted(entrees) != sorted(ENTREES_COURSE):
        raise Arret(f"entrées de la configuration {sorted(entrees) if isinstance(entrees, dict) else entrees!r} ≠ "
                    f"entrées de la course {sorted(ENTREES_COURSE)} (course_v1.ENTREES_COURSE_REQUISES)")
    emp7b = (cfg.get("marqueurs") or {}).get("EMPREINTES_ENTREES_7B") or {}
    for nom in ENTREES_7B:
        e, f = entrees[nom], FICHIERS_7B_PAR_ENTREE[nom]
        if Path(e["chemin"]).name != f:
            raise Arret(f"entrée {nom} : {e['chemin']} ne se termine pas par {f}")
        if not (_HEX64.match(str(e.get("sha256"))) and emp7b.get(f) == e["sha256"]):
            raise Arret(f"entrée {nom} : empreinte de la liste ≠ EMPREINTES_ENTREES_7B[{f}] de la configuration")
        if not _tel_quel(corps_texte, e["sha256"]):
            raise Arret(f"entrée {nom} : empreinte {e['sha256'][:12]}… absente du texte scellé (R11)")
        prendre("branche de sortie de 7b", commit_7b, e["chemin"], (("empreinte consignée", e["sha256"]),))
    for nom in ENTREES_CODE:
        e = entrees[nom]
        if not _HEX64.match(str(e.get("sha256"))):
            raise Arret(f"entrée {nom} : empreinte consignée absente")
        prendre("commit du code", commit_code, e["chemin"], (("empreinte consignée", e["sha256"]),))
    for chemin in GUIDE:
        prendre("commit du code (guide de classification)", commit_code, chemin)
    return {"fichiers": dict(sorted(fichiers.items())), "texte": texte, "config": config,
            "commit_code_config": (cfg.get("marqueurs") or {}).get("COMMIT_CODE_T08")}


def commits_du_message(depot: Path, ref: str) -> dict:
    """Commits de 7b, du code et du texte que le message du commit de la branche d'entrée consigne (écrits par `ecrire`)."""
    m = git(Path(depot), "log", "-1", "--format=%B", ref).decode()
    r = {}
    for cle, motif in (("7b", "commit de 7b"), ("code", "commit du code"), ("texte", "commit du texte")):
        x = re.findall(rf"^{motif} ([0-9a-f]{{40}})$", m, re.M)
        if len(x) != 1:
            raise Arret(f"{ref} : message sans une seule ligne « {motif} <40> »")
        r[cle] = x[0]
    return r


def ecrire(depot: Path, branche: str, p: dict, commits: dict) -> str:
    """Commit orphelin sur `refs/heads/<branche>`, créée seulement si elle n'existe pas (ni locale ni suivie)."""
    depot = Path(depot)
    if not re.match(r"^[A-Za-z0-9][A-Za-z0-9._/-]*$", branche) or ".." in branche or branche.endswith("/"):
        raise Arret(f"nom de branche illisible : {branche!r}")
    for ref in (f"refs/heads/{branche}", f"refs/remotes/origin/{branche}"):
        r = subprocess.run(["git", "-C", str(depot), "rev-parse", "--verify", "-q", ref], capture_output=True)
        if r.returncode == 0:
            raise Arret(f"{ref} existe déjà : la branche d'entrée est toujours neuve (R12)")
    with tempfile.TemporaryDirectory() as d:
        env = {"GIT_INDEX_FILE": str(Path(d) / "index")}
        for chemin, f in p["fichiers"].items():
            git(depot, "update-index", "--add", "--cacheinfo", f"100644,{f['blob']},{chemin}", env=env)
        arbre = git(depot, "write-tree", env=env).decode().strip()
    message = (f"T0.8 : branche d'entrée de la course ({len(p['fichiers'])} fichiers, liste blanche ; {VERSION})\n\n"
               f"commit de 7b {commits['7b']}\ncommit du code {commits['code']}\ncommit du texte {commits['texte']}\n")
    ident = {"GIT_AUTHOR_NAME": "branche d'entrée T0.8", "GIT_AUTHOR_EMAIL": "branche-entree@invalid",
             "GIT_COMMITTER_NAME": "branche d'entrée T0.8", "GIT_COMMITTER_EMAIL": "branche-entree@invalid"}
    commit = git(depot, "commit-tree", arbre, entree=message.encode(), env=ident).decode().strip()
    git(depot, "update-ref", f"refs/heads/{branche}", commit, "0" * 40)     # échoue si la référence existe
    return commit


def verifier_ref(depot: Path, ref: str, p: dict) -> dict:
    """Contrôle final de la branche écrite (ou relevée par le lanceur) : liste exacte, aucun interdit, orpheline, objets."""
    depot = Path(depot)
    commit = git(depot, "rev-parse", "--verify", f"{ref}^{{commit}}").decode().strip()
    parents = git(depot, "rev-list", "--parents", "-n", "1", commit).decode().split()
    if parents != [commit]:
        raise Arret(f"{ref} : commit {commit[:12]} avec parent(s) {parents[1:]} : une branche orpheline est exigée")
    if git(depot, "rev-list", "--count", commit).decode().strip() != "1":
        raise Arret(f"{ref} : plus d'un commit dans l'histoire")
    noms = git(depot, "ls-tree", "-r", "--name-only", "-z", commit).decode().split("\0")
    noms = sorted(n for n in noms if n)
    attendus = sorted(p["fichiers"])
    if noms != attendus:
        raise Arret(f"{ref} : fichiers ≠ liste blanche (en trop {sorted(set(noms) - set(attendus))[:5]}, "
                    f"manquants {sorted(set(attendus) - set(noms))[:5]})")
    for n in noms:
        if nom_interdit(n):
            raise Arret(f"{ref} : {n} porte le motif interdit {nom_interdit(n)!r}")
        if blob(depot, commit, n) != p["fichiers"][n]["blob"]:
            raise Arret(f"{ref} : {n} n'est pas la copie à l'octet de sa source")
        if hashlib.sha256(git(depot, "cat-file", "blob", p["fichiers"][n]["blob"])).hexdigest() != p["fichiers"][n]["sha256"]:
            raise Arret(f"{ref} : {n} : empreinte ≠ celle de la liste blanche")
    objets = git(depot, "rev-list", "--objects", commit).decode().splitlines()
    blobs = {l.split(" ", 1)[0] for l in objets if " " in l and l.split(" ", 1)[1] in p["fichiers"]}
    arbres = set(git(depot, "rev-list", "--objects", "--no-object-names", "--filter=blob:none", commit).decode().split())
    hors = {l.split(" ", 1)[0] for l in objets} - blobs - arbres
    if hors:
        raise Arret(f"{ref} : {len(hors)} objet(s) de l'histoire hors de la liste blanche (ni le commit, ni ses arbres, "
                    "ni les blobs de la liste)")
    for l in objets:
        if " " in l and nom_interdit(l.split(" ", 1)[1]):
            raise Arret(f"{ref} : objet git {l.split(' ', 1)[1]} interdit")
    return {"ref": ref, "commit": commit, "fichiers": {n: p["fichiers"][n]["sha256"] for n in noms},
            "nombre": len(noms), "objets": len(objets)}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="construire_branche_entree_t08_v1.py")
    sous = ap.add_subparsers(dest="quoi", required=True)
    for q in ("construire", "verifier"):
        a = sous.add_parser(q)
        a.add_argument("--depot", required=True)
        a.add_argument("--commit-7b", required=q == "construire")
        a.add_argument("--commit-code", required=q == "construire")
        a.add_argument("--commit-texte", required=True)
        a.add_argument("--texte", required=True)
        a.add_argument("--config", required=True)
        if q == "construire":
            a.add_argument("--branche", required=True)
        else:
            a.add_argument("--ref", required=True)
    a = ap.parse_args(argv)
    try:
        if a.quoi == "verifier" and not (a.commit_7b and a.commit_code):
            # vérification seule, sans la branche de 7b : sources lues dans la branche d'entrée elle-même ; le commit de 7b
            # consigné par son message doit être cité par le texte, le commit du code consigné doit être celui du marqueur
            cm = commits_du_message(Path(a.depot), a.ref)
            if cm["texte"] != a.commit_texte:
                raise Arret(f"{a.ref} : commit du texte consigné {cm['texte'][:12]} ≠ --commit-texte {a.commit_texte[:12]}")
            rc = git(Path(a.depot), "rev-parse", "--verify", f"{a.ref}^{{commit}}").decode().strip()
            p = plan(Path(a.depot), rc, rc, a.commit_texte, a.texte, a.config, cite_7b=cm["7b"])
            if cm["code"] != p["commit_code_config"]:
                raise Arret(f"{a.ref} : commit du code consigné {cm['code'][:12]} ≠ COMMIT_CODE_T08 de la configuration")
        else:
            p = plan(Path(a.depot), a.commit_7b, a.commit_code, a.commit_texte, a.texte, a.config)
            if a.quoi == "construire" and p["commit_code_config"] != a.commit_code:   # contre-lecture m-1
                raise Arret(f"--commit-code {a.commit_code[:12]} ≠ COMMIT_CODE_T08 de la configuration "
                            f"({str(p['commit_code_config'])[:12]}) : arrêt, rien d'écrit")
        if a.quoi == "construire":
            commit = ecrire(Path(a.depot), a.branche, p, {"7b": a.commit_7b, "code": a.commit_code, "texte": a.commit_texte})
            try:
                r = verifier_ref(Path(a.depot), f"refs/heads/{a.branche}", p)
                if r["commit"] != commit:
                    raise Arret("branche écrite ≠ commit relu")
            except Arret:            # contrôle final en échec : la branche écrite est retirée (aucune branche fautive ne reste)
                subprocess.run(["git", "-C", a.depot, "update-ref", "-d", f"refs/heads/{a.branche}", commit],
                               capture_output=True)
                raise
            r["branche"] = a.branche
        else:
            r = verifier_ref(Path(a.depot), a.ref, p)
    except (Arret, json.JSONDecodeError, KeyError, UnicodeDecodeError) as e:
        print(f"ARRÊT ({VERSION}) : {type(e).__name__ if not isinstance(e, Arret) else ''}{e}", file=sys.stderr)
        return 1
    print(json.dumps({"version": VERSION, **r}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
