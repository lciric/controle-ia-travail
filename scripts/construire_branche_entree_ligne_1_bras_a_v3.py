"""Construit la branche d'entrée de la machine autonome de la ligne 1 de carte du bras A, version 3 (23 novembre 2026 ;
les versions 1 et 2 restent telles quelles, jamais jouées).

Différences avec la version 2 (contre-lecture de la machine v2) : l'amorce complète portée est la v3
(`scripts/amorce_ligne_1_bras_a_v3.sh`) ; `git fetch origin main` avant de prendre les quatre fichiers du guide à
`origin/main` (m7 ; `--sans-fetch` pour les essais hors réseau).

Différence de la version 2 avec la version 1 : la branche porte aussi **l'amorce complète de la machine**, prise au commit comme les autres fichiers et empreintée dans
`empreintes-posees.txt` : 58 fichiers. L'amorce d'appel courte (onstart de Vast, limité à environ 4 Ko) clone cette
branche, vérifie le commit et l'empreinte de l'amorce complète, puis l'exécute. Ce qui suit décrit la version 1.

La machine louée n'a pas de SSH : elle clone, à profondeur 1, une **branche orpheline qui ne porte que la liste
blanche** (`git clone --depth 1 --single-branch --branch <entrée>`). C'est cette branche qui tient le cloisonnement :
aucun autre fichier du dépôt n'atteint la machine. Ce programme la construit **dans un dépôt git temporaire, hors de
l'arbre de travail** ; il ne pousse rien par défaut (`--pousser` pousse la seule branche d'entrée, refuse si elle
existe déjà sur le dépôt distant à un autre commit).

Contenu de la branche (et rien d'autre, contrôlé après le commit par `git ls-tree`) :
- la liste blanche v2 calculée par programme (`scripts/liste_blanche_ligne_1_bras_a_v2.py`, appelée ici) : 36 modules
  et 12 fichiers de données avec compagnons, pris **un par un** au commit source (`git show <commit>:<chemin>`,
  jamais de copie de dossier) ; l'arbre de travail doit être propre sur ces chemins ;
- les quatre fichiers du guide « H1-classification » sous `docs/sources/` : **cloisonnés pour qui écrit ce programme**.
  Leurs octets sont pris par `git show <référence du guide>:<chemin>` redirigé **directement dans le fichier** (rien
  n'est affiché, rien n'est lu ni empreinté ici) ; leurs empreintes sont **données** (constantes ci-dessous, égales à
  celles de la liste blanche v2 et du lanceur v8) et écrites telles quelles dans `empreintes-posees.txt`. La machine
  les recontrôle par `sha256sum -c` avant tout ; un écart arrête ;
- `requirements-gpu.txt`, `requirements-cpu.txt`, `requirements-donnees.txt` ;
- le constat de départ, sous le nom `constat-ligne-1.json` ;
- `empreintes-posees.txt` (format `sha256sum`, une ligne par fichier ci-dessus, triées par chemin).

Contrôle de cloisonnement : tout chemin de la branche est confronté à `est_cloisonne_ici` de la liste blanche v2
(garde statique du bras A, plus les chemins cloisonnés de la session) ; seuls les quatre chemins du guide y échappent,
et seulement s'ils sont exactement ceux-là. Le message du commit porte `Commit-source: <commit>` (l'amorce le lit et le
passe à `--commit` de la course).

Usage : `PYTHONPATH=src python scripts/construire_branche_entree_ligne_1_bras_a_v3.py [--pousser]` ; écrit un compte
rendu JSON sur la sortie standard (dossier temporaire, branche, commit d'entrée, commit source, nombre de fichiers,
empreinte d'`empreintes-posees.txt`).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
LISTE_BLANCHE = "scripts/liste_blanche_ligne_1_bras_a_v2.py"
CONFIGURATION = "prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v2.json"
LANCEUR = "src/controle_ia/organismes_discrets/lanceur_bras_a_v8.py"
PLAN_SCELLE = "docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v2.json"
CONSTAT = "docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/constat-ligne-1-20261123T024626Z.json"
NOM_DU_CONSTAT = "constat-ligne-1.json"
EXIGENCES = ("requirements-gpu.txt", "requirements-cpu.txt", "requirements-donnees.txt")
AMORCE_COMPLETE = "scripts/amorce_ligne_1_bras_a_v3.sh"
NOM_DES_EMPREINTES = "empreintes-posees.txt"
BRANCHE_ENTREE = "entree/bras-a-ligne-1-v1"
REFERENCE_DU_GUIDE = "origin/main"
# Empreintes DONNÉES des quatre fichiers du guide (jamais recalculées ici : chemins cloisonnés pour l'auteur)
GUIDE_DONNE = (
    ("docs/sources/invites-2606.08892-v1/invites/H1-classification.txt",
     "69d50fb972f3255c94430205ab09c4f21054185d7def25b061c7255d71cc5540"),
    ("docs/sources/invites-2606.08892-v1/invites/H1-classification.txt.sha256",
     "fb943fdb29aa2d2c04bfa14a6da15ad6f9ccb315292194e866527cc09835b266"),
    ("docs/sources/invites-2606.08892-v1/index.json",
     "adb4b8bca7788baf2c4714df96dcdcc2c5043e8f1943542d0fbe1863491ae2d9"),
    ("docs/sources/invites-2606.08892-v1/index.json.sha256",
     "ba9648b15ae45edce2933b00977e17cc37ef5282ab4e08e49f5b41463788316c"),
)
_SHA = re.compile(r"[0-9a-f]{64}")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_BRANCHE = re.compile(r"[a-z0-9][a-z0-9/._-]*[a-z0-9]")
IDENTITE = {"GIT_AUTHOR_NAME": "construction de la branche d'entree", "GIT_AUTHOR_EMAIL": "construction@invalid",
            "GIT_COMMITTER_NAME": "construction de la branche d'entree", "GIT_COMMITTER_EMAIL": "construction@invalid"}


class Refus(Exception):
    pass


def charger_la_liste_blanche():
    spec = importlib.util.spec_from_file_location("liste_blanche_ligne_1_bras_a_v2", ICI / "liste_blanche_ligne_1_bras_a_v2.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _git(depot: Path, *args: str, env: dict | None = None, **kw) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(depot), *args], env=dict(os.environ, **(env or {})), **kw)


def _git_sortie(depot: Path, *args: str, env: dict | None = None) -> str:
    r = _git(depot, *args, env=env, capture_output=True, text=True)
    if r.returncode != 0:
        raise Refus(f"git {' '.join(args[:2])} : code {r.returncode} ({r.stderr.strip()[:300]})")
    return r.stdout


def _poser_depuis_git(source: Path, reference: str, chemin: str, destination: Path) -> None:
    """Octets de `<référence>:<chemin>` écrits directement dans le fichier (stdout redirigé, jamais affiché)."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    with open(destination, "xb") as f:
        r = _git(source, "show", f"{reference}:{chemin}", stdout=f, stderr=subprocess.PIPE)
    if r.returncode != 0:
        raise Refus(f"{chemin} absent de {reference} (git show : code {r.returncode})")


def _sha(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def exiger_le_guide_donne(lb) -> None:
    """Les empreintes données ici sont celles de la liste blanche v2 (invite et index) : un écart arrête."""
    donnees = dict(GUIDE_DONNE)
    for chemin, sha in lb.GUIDE_FICHIERS:
        if donnees.get(chemin) != sha:
            raise Refus(f"empreinte donnée de {chemin} différente de celle de la liste blanche v2")
    for chemin, sha in GUIDE_DONNE:
        if _SHA.fullmatch(sha) is None:
            raise Refus(f"empreinte donnée de {chemin} illisible")


def construire(source: Path, commit: str, fichiers: list[str], renommes: dict[str, str], guide: list[tuple[str, str]],
               reference_guide: str, branche: str, dossier: Path, est_cloisonne) -> dict:
    """Cœur, sans liste imposée (les essais l'appellent sur un dépôt jouet). `fichiers` : chemins pris au commit et posés
    au même chemin ; `renommes` : {chemin posé: chemin au commit} ; `guide` : (chemin, empreinte donnée) pris à
    `reference_guide`, jamais lus ni empreintés ; `est_cloisonne(chemin)` : vrai si le chemin est cloisonné."""
    if _COMMIT.fullmatch(commit or "") is None:
        raise Refus("commit source entier exigé")
    if _BRANCHE.fullmatch(branche or "") is None or ".." in branche:
        raise Refus(f"nom de branche {branche!r} illisible")
    chemins_du_guide = [c for c, _ in guide]
    tout = list(fichiers) + list(renommes) + chemins_du_guide
    if len(set(tout)) != len(tout) or NOM_DES_EMPREINTES in tout:
        raise Refus("chemin posé deux fois, ou qui porte le nom du fichier des empreintes")
    for c in tout:
        if c.startswith("/") or ".." in Path(c).parts or c != Path(c).as_posix():
            raise Refus(f"chemin {c!r} : relatif et sans détour exigé")
    cloisonnes = [c for c in list(fichiers) + list(renommes) + list(renommes.values()) if est_cloisonne(c)]
    if cloisonnes:
        raise Refus(f"chemins cloisonnés hors des quatre fichiers du guide : {cloisonnes}")
    for c, sha in guide:
        if _SHA.fullmatch(sha or "") is None:
            raise Refus(f"empreinte donnée de {c} illisible")
    dossier = Path(dossier)
    if dossier.exists() and any(dossier.iterdir()):
        raise Refus(f"{dossier} existe et n'est pas vide (R12)")
    dossier.mkdir(parents=True, exist_ok=True)
    _git_sortie(dossier, "init", "-q", "-b", branche)
    empreintes: dict[str, str] = {}
    for c in fichiers:
        _poser_depuis_git(source, commit, c, dossier / c)
        empreintes[c] = _sha(dossier / c)
    for pose, origine in renommes.items():
        _poser_depuis_git(source, commit, origine, dossier / pose)
        empreintes[pose] = _sha(dossier / pose)
    for c, sha in guide:
        _poser_depuis_git(source, reference_guide, c, dossier / c)      # octets non lus, empreinte donnée
        empreintes[c] = sha
    texte = "".join(f"{empreintes[c]}  {c}\n" for c in sorted(empreintes))
    (dossier / NOM_DES_EMPREINTES).write_text(texte, encoding="utf-8")
    attendus = sorted(list(empreintes) + [NOM_DES_EMPREINTES])
    for c in attendus:
        _git_sortie(dossier, "add", "--", c)
    message = (f"Branche d'entrée de la ligne 1 de carte du bras A ({len(attendus)} fichiers, liste blanche seule)\n\n"
               f"Commit-source: {commit}\nReference-du-guide: {reference_guide}\n")
    _git_sortie(dossier, "commit", "-q", "-m", message, env=IDENTITE)
    poses = sorted(_git_sortie(dossier, "ls-tree", "-r", "--name-only", "HEAD").split("\n")[:-1])
    if poses != attendus:
        raise Refus(f"la branche porte {len(poses)} chemins, {len(attendus)} attendus — refusé")
    hors_guide = [c for c in poses if est_cloisonne(c) and c not in chemins_du_guide]
    if hors_guide:
        raise Refus(f"chemins cloisonnés sur la branche hors des quatre du guide : {hors_guide}")
    if _git_sortie(dossier, "rev-list", "--parents", "-n", "1", "HEAD").split()[1:]:
        raise Refus("la branche d'entrée doit être orpheline")
    return {"dossier": str(dossier), "branche": branche, "commit_entree": _git_sortie(dossier, "rev-parse", "HEAD").strip(),
            "commit_source": commit, "nombre_de_fichiers": len(poses),
            "empreintes_posees_sha256": _sha(dossier / NOM_DES_EMPREINTES), "fichiers": poses}


def pousser(dossier: Path, branche: str, distant: str) -> dict:
    """Pousse la seule branche d'entrée (refspec explicite, jamais de force). Existante au même commit : rien à faire ;
    à un autre commit : refus (R12, nouvelle version = nouveau nom)."""
    local = _git_sortie(dossier, "rev-parse", "HEAD").strip()
    r = _git(dossier, "ls-remote", distant, f"refs/heads/{branche}", capture_output=True, text=True)
    if r.returncode != 0:
        raise Refus(f"dépôt distant injoignable (ls-remote : code {r.returncode})")
    present = r.stdout.split()[0] if r.stdout.strip() else None
    if present is not None and present != local:
        raise Refus(f"branche {branche} déjà sur le dépôt distant à un autre commit — refusé (R12)")
    if present is None:
        p = _git(dossier, "push", "-q", distant, f"HEAD:refs/heads/{branche}", capture_output=True, text=True)
        if p.returncode != 0:
            raise Refus(f"poussée refusée (code {p.returncode})")
    r = _git(dossier, "ls-remote", distant, f"refs/heads/{branche}", capture_output=True, text=True)
    lu = r.stdout.split()[0] if r.returncode == 0 and r.stdout.strip() else None
    if lu != local:
        raise Refus("poussée non prouvée : la branche distante ne répond pas au commit local")
    return {"poussee": True, "commit_distant": lu}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--racine", default=".")
    p.add_argument("--branche", default=BRANCHE_ENTREE)
    p.add_argument("--constat", default=CONSTAT)
    p.add_argument("--reference-du-guide", default=REFERENCE_DU_GUIDE)
    p.add_argument("--dossier", help="dossier neuf du dépôt temporaire (défaut : un dossier temporaire neuf)")
    p.add_argument("--sans-fetch", action="store_true", help="essais hors réseau : pas de fetch avant le guide")
    p.add_argument("--pousser", action="store_true", help="pousse la seule branche d'entrée vers `origin`")
    p.add_argument("--distant", default="origin", help="dépôt distant (essais : chemin d'un dépôt nu)")
    a = p.parse_args(argv)
    racine = Path(a.racine).resolve()
    try:
        lb = charger_la_liste_blanche()
        exiger_le_guide_donne(lb)
        liste = lb.liste_blanche(racine, CONFIGURATION, LANCEUR, PLAN_SCELLE)
        guide_de_la_liste = {g["chemin"] for g in liste["guide"]}
        if guide_de_la_liste != {c for c, _ in GUIDE_DONNE}:
            raise Refus("les chemins du guide de la liste blanche ne sont pas les quatre attendus")
        fichiers = list(liste["modules"]) + list(liste["donnees"]) + list(EXIGENCES) + [AMORCE_COMPLETE]
        commit = _git_sortie(racine, "rev-parse", "HEAD").strip()
        a_comparer = fichiers + [a.constat]
        if _git(racine, "diff", "--quiet", "HEAD", "--", *a_comparer).returncode != 0:
            raise Refus("l'arbre de travail diffère de HEAD sur un fichier posé : committer d'abord")
        absents = [c for c in a_comparer if _git(racine, "cat-file", "-e", f"HEAD:{c}", capture_output=True).returncode != 0]
        if absents:
            raise Refus(f"l'arbre de travail porte des fichiers posés absents de HEAD ({absents}) : committer d'abord")
        pousse = bool(_git_sortie(racine, "branch", "-r", "--contains", commit).strip())
        if not a.sans_fetch and a.reference_du_guide.startswith("origin/"):
            f = _git(racine, "fetch", "-q", "origin", a.reference_du_guide.split("/", 1)[1], capture_output=True)
            if f.returncode != 0:
                raise Refus(f"git fetch de {a.reference_du_guide} en échec (code {f.returncode})")
        dossier = Path(a.dossier) if a.dossier else Path(tempfile.mkdtemp(prefix="branche-entree-ligne-1-")) / "depot"
        compte = construire(racine, commit, fichiers, {NOM_DU_CONSTAT: a.constat}, list(GUIDE_DONNE),
                            a.reference_du_guide, a.branche, dossier, lb.est_cloisonne_ici)
        compte.update(commit_source_present_sur_une_branche_distante=pousse, liste_blanche=liste["nombre"],
                      amorce_complete_sha256=_sha(dossier / AMORCE_COMPLETE))
        if a.pousser:
            compte.update(pousser(dossier, a.branche, a.distant if a.distant != "origin"
                                  else _git_sortie(racine, "remote", "get-url", "origin").strip()))
        else:
            compte["poussee"] = False
    except (Refus, OSError) as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    print(json.dumps(compte, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
