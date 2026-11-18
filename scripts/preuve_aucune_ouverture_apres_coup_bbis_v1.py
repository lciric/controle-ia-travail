#!/usr/bin/env python3
"""Preuve « aucune donnée ouverte », faite **après coup**, pour la lecture de l'apprentissage des sondes sur la tâche (étape B bis
de T0.7) — complément au quatrième addendum d'écart (`prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, empreinte
scellée `12c908732c329e61b57fe435e430464cb8033d0db708d4432076c62b4c9aa419`), § 2 « Arrêt avant le seuil, sans rien écrire » et
§ 6 « Programme de la preuve après coup » ; décision GO-2026-11-18-64.

À quoi il sert : quand le module de lecture s'est arrêté (code 2) sans imprimer la ligne `BBIS LECTURE ENTREES OUVERTES` et sans
écrire ni fichier de lecture ni pièce de preuve, ce programme relève, dans l'arbre de lecture, l'état du disque et de l'histoire
git, en trois points, et vérifie les sorties imprimées gardées de tous les lancements antérieurs :

- (A1) journal : le journal des ouvertures est absent du disque, ou présent sans aucune ligne `OUVERTURE-BBIS` (nombre de
  lignes et empreinte relevés) ; aucun commit de l'histoire du journal n'en porte une ;
- (A2) aucun run de lecture : sur le disque et dans toutes les références du dépôt, aucun dossier `runs/<run>` ni `diag/<run>`
  au nom donné pour la lecture, aucun fichier nommé `lecture-bbis.json` ni `preuve-aucune-ouverture-bbis.json` hors de ceux que
  citent, par chemin et empreinte, les lignes `PANNE-MISE-EN-PLACE-BBIS-<n>` déjà inscrites, chacun à l'empreinte citée ;
  relevé par les noms seulement ;
- (A3) fichiers de scores et de sondes inchangés, sans voisin : l'empreinte de `sondes-bbis.json` est celle de la ligne
  `SCORES-BBIS` ; chaque fichier de `diag/<run de la course>`, `donnees/<run de la course>` et `runs/<run de la course>` a les
  octets du même fichier au commit des sorties de la course, où `sondes-bbis.json` a l'empreinte de la ligne `SCORES-BBIS` ; la
  liste des noms est celle de ce commit, sans fichier de plus ni de moins, suivi ou non ;
- sorties : chaque sortie imprimée gardée (chemin et empreinte donnés) est présente, scellée, à l'empreinte donnée, et ne porte
  pas la ligne du seuil.

Ce qu'il ne fait pas : il n'importe aucun module de `controle_ia`, n'appelle aucune garde, ne **décode** aucun fichier de
résultat (les fichiers des dossiers de la course sont lus octet par octet pour leur empreinte ; `sondes-bbis.json` n'est pas
ouvert autrement), ne lance que des commandes git en lecture, ne corrige rien. Il refuse de partir, avant toute commande git et
sans rien écrire, si une variable d'environnement dont le nom commence par `GIT_` est posée (même garde que la huitième
différence du module de lecture ; noms seulement, jamais une valeur).

Sortie, scellée, jamais écrasée (R12) :
`registres/t07-etape-b-bis/lecture-v1/preuve-aucune-ouverture-apres-coup-bbis-<n>-v1.json` : `conforme` vrai ou faux, point par
point, et un classement — « relance permise sur preuve » ; « lecture consommée » (une sortie absente, non scellée, d'une autre
empreinte ou portant la ligne du seuil ; aucune sortie donnée) ; « nœud » (un point (A1) à (A3) non conforme ou non faisable).

Usage : `python scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py --racine R --run-lecture RUNL --run-bbis RUNB --numero N
--sortie-lancement CHEMIN EMPREINTE [--sortie-lancement CHEMIN EMPREINTE …]`. Codes de sortie : 0, pièce écrite, conforme ;
1, pièce écrite, non conforme ; 2, arrêt, rien d'écrit. N'imprime que des chemins, des empreintes et des états.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

COMMIT_SORTIES = "7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9"     # tête de la branche des sorties `donnees/t07-etape-b-bis-v2`
REGISTRE_PROPRE = "registres/t07-etape-b-bis-v1.md"
JOURNAL = REGISTRE_PROPRE + ".ouvertures.md"
REGISTRE_VOISIN = "registres/t07-etape-b-bis-v1-addenda-v1.md"
SORTIE = "registres/t07-etape-b-bis/lecture-v1/preuve-aucune-ouverture-apres-coup-bbis-{n}-v1.json"
SEUIL = "BBIS LECTURE ENTREES OUVERTES"
CLE_OUVERTURE = "OUVERTURE-BBIS"
NOMS_DE_LECTURE = ("lecture-bbis.json", "preuve-aucune-ouverture-bbis.json")
CLE_PANNE = re.compile(r"PANNE-MISE-EN-PLACE-BBIS-[1-9][0-9]*")
RUN = re.compile(r"[0-9]{8}-[0-9]{6}-[a-z0-9][a-z0-9-]{0,62}")
SHA = re.compile(r"[0-9a-f]{64}")
COMMIT = re.compile(r"[0-9a-f]{40}")
PERMISE, CONSOMMEE, NOEUD = "relance permise sur preuve", "lecture consommée", "nœud"


class Arret(Exception):
    """Arrêt avant tout relevé : rien n'est écrit (code 2)."""


class NonFaisable(Exception):
    """Un relevé ne peut pas être fait : le point est non conforme, « non faisable » (nœud)."""


def exiger_environnement_git_propre() -> None:
    """Même garde que la huitième différence du module de lecture : refus, sans nettoyage, noms seulement."""
    posees = sorted(k for k in os.environ if k.startswith("GIT_"))
    if posees:
        raise Arret(f"variable(s) d'environnement de git posée(s) ({', '.join(posees)}) : refus ; aucune commande git n'est "
                    "lancée sous une variable GIT_*")


def empreinte_fichier(chemin: Path) -> str:
    """Empreinte du fichier, lu octet par octet, jamais décodé."""
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def git(racine: Path, *args, codes=(0,)) -> subprocess.CompletedProcess:
    """Commande git en lecture ; code de retour hors de `codes`, ou git introuvable : relevé non faisable."""
    try:
        r = subprocess.run(["git", "-C", str(racine), *args], capture_output=True)
    except OSError as e:
        raise NonFaisable(f"git {' '.join(args[:2])} : échec de git ({type(e).__name__})") from None
    if r.returncode not in codes:
        raise NonFaisable(f"git {' '.join(args[:2])} : échec de git (code {r.returncode} ; "
                          f"{r.stderr.decode('utf-8', 'replace').strip()[:200]})")
    return r


def texte_git(racine: Path, *args) -> str:
    return git(racine, *args).stdout.decode("utf-8", "replace")


def noms_git(racine: Path, ref: str, *chemins) -> list[str]:
    """Noms des fichiers de l'arbre de `ref` (sous `chemins` s'ils sont donnés), relatifs à la racine du dépôt."""
    brut = git(racine, "ls-tree", "-r", "--name-only", "--full-tree", "-z", ref, "--", *chemins).stdout
    return [x.decode("utf-8", "surrogateescape") for x in brut.split(b"\0") if x]


def empreinte_git(racine: Path, ref: str, chemin: str) -> str:
    """Empreinte des octets du fichier `chemin` dans l'arbre de `ref`, lus en flux, jamais décodés."""
    try:
        p = subprocess.Popen(["git", "-C", str(racine), "cat-file", "blob", f"{ref}:{chemin}"], stdout=subprocess.PIPE,
                             stderr=subprocess.DEVNULL)
    except OSError as e:
        raise NonFaisable(f"git cat-file blob : échec de git ({type(e).__name__})") from None
    h = hashlib.sha256()
    for bloc in iter(lambda: p.stdout.read(1 << 20), b""):
        h.update(bloc)
    p.stdout.close()
    if p.wait() != 0:
        raise NonFaisable(f"git cat-file blob : échec de git (code {p.returncode}) pour {chemin} à {ref[:12]}")
    return h.hexdigest()


def exiger_histoire_complete(racine: Path) -> None:
    etat = texte_git(racine, "rev-parse", "--is-shallow-repository").strip()
    if etat != "false":
        raise NonFaisable("dépôt superficiel : histoire git incomplète" if etat == "true"
                          else "git rev-parse --is-shallow-repository : sortie inattendue")


def cle_de(ligne: str) -> str:
    return [x.strip() for x in ligne.strip().strip("|").split("|")][0]


def fichiers_du_disque(dossier: Path, racine: Path) -> list[str]:
    """Tous les fichiers (et liens) sous `dossier`, suivis par git ou non, relatifs à `racine` ; le dossier de git est sauté."""
    noms = []
    for base, sous, fichiers in os.walk(dossier, followlinks=False):
        sous[:] = [s for s in sous if not (Path(base) == racine and s == ".git")]
        for s in list(sous):
            if (Path(base) / s).is_symlink():
                noms.append((Path(base) / s).relative_to(racine).as_posix())
        noms += [(Path(base) / f).relative_to(racine).as_posix() for f in fichiers]
    return sorted(noms)


# ------------------------------------------------------------------------------------------------------- (A1) journal

def point_a1(racine: Path) -> dict:
    journal = racine / JOURNAL
    if journal.is_file():
        octets = journal.read_bytes()
        lignes = octets.decode("utf-8", "replace").splitlines()
        disque = {"etat": "présent", "lignes": len(lignes), "lignes_ouverture": sum(CLE_OUVERTURE in l for l in lignes),
                  "sha256": hashlib.sha256(octets).hexdigest()}
    elif journal.exists() or journal.is_symlink():
        disque = {"etat": "présent, ni fichier ni absent", "lignes_ouverture": None}
    else:
        disque = {"etat": "absent du disque", "lignes_ouverture": 0}
    exiger_histoire_complete(racine)
    commits = texte_git(racine, "log", "--all", "--format=%H", "--", JOURNAL).split()
    fautifs = []
    for c in commits:
        if not COMMIT.fullmatch(c):
            raise NonFaisable("git log : sortie inattendue")
        if noms_git(racine, c, JOURNAL) and CLE_OUVERTURE in texte_git(racine, "show", f"{c}:{JOURNAL}"):
            fautifs.append(c)
    return {"conforme": disque["lignes_ouverture"] == 0 and not fautifs, "journal": JOURNAL, "disque": disque,
            "commits_de_l_histoire_du_journal": len(commits), "commits_portant_une_ligne_d_ouverture": fautifs}


# ------------------------------------------------------------------------------------------- (A2) aucun run de lecture

def citations_des_pannes(racine: Path) -> tuple[list[str], list[dict]]:
    """Textes qui citent, par chemin et empreinte, les fichiers gardés : chaque ligne `PANNE-MISE-EN-PLACE-BBIS-<n>` inscrite au
    registre voisin (lu sur le disque de l'arbre), et la déclaration scellée qu'elle cite, si elle est à l'empreinte de la
    ligne. Rend ces textes et le relevé de chaque ligne."""
    voisin = racine / REGISTRE_VOISIN
    textes, releve = [], []
    if not voisin.is_file():
        return textes, releve
    for l in voisin.read_text(encoding="utf-8", errors="replace").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if not CLE_PANNE.fullmatch(c[0]):
            continue
        x = {"cle": c[0], "declaration": c[2] if len(c) > 2 else None, "etat": "ligne mal formée"}
        if len(c) >= 4 and SHA.fullmatch(c[3]) and c[2] and not c[2].startswith("/") and ".." not in Path(c[2]).parts:
            d = racine / c[2]
            if not d.is_file():
                x["etat"] = "déclaration absente du disque"
            elif empreinte_fichier(d) != c[3]:
                x["etat"] = "déclaration d'une autre empreinte que la ligne"
            else:
                x["etat"] = "déclaration à l'empreinte de la ligne"
                textes += [l, d.read_text(encoding="utf-8", errors="replace")]
        releve.append(x)
    return textes, releve


def point_a2(racine: Path, run_lecture: str) -> dict:
    textes, pannes = citations_des_pannes(racine)
    cite = lambda chemin, sha: any(chemin in t and sha in t for t in textes)
    dossiers = [f"{d}/{run_lecture}" for d in ("runs", "diag")]
    fautes, toleres = [], []
    for d in dossiers:
        if (racine / d).exists() or (racine / d).is_symlink():
            fautes.append({"ou": "disque", "nom": d, "motif": "dossier du run de lecture présent"})
    for nom in fichiers_du_disque(racine, racine):
        if Path(nom).name in NOMS_DE_LECTURE:
            p = racine / nom
            sha = empreinte_fichier(p) if p.is_file() and not p.is_symlink() else None
            if sha is not None and cite(nom, sha):
                toleres.append({"ou": "disque", "nom": nom, "sha256": sha})
            else:
                fautes.append({"ou": "disque", "nom": nom, "motif": "non cité, à cette empreinte, par une ligne de panne inscrite"})
    exiger_histoire_complete(racine)
    references = ["HEAD"] + [r for r in texte_git(racine, "for-each-ref", "--format=%(refname)").split("\n") if r]
    for ref in references:
        for nom in noms_git(racine, ref):
            if any(nom == d or nom.startswith(d + "/") for d in dossiers):
                fautes.append({"ou": ref, "nom": nom, "motif": "fichier du run de lecture dans une référence"})
            elif Path(nom).name in NOMS_DE_LECTURE:
                sha = empreinte_git(racine, ref, nom)
                if cite(nom, sha):
                    toleres.append({"ou": ref, "nom": nom, "sha256": sha})
                else:
                    fautes.append({"ou": ref, "nom": nom,
                                   "motif": "non cité, à cette empreinte, par une ligne de panne inscrite"})
    mal_citees = [x for x in pannes if x["etat"] != "déclaration à l'empreinte de la ligne"]
    return {"conforme": not fautes and not mal_citees, "run_de_lecture": run_lecture, "references_relevees": len(references),
            "lignes_de_panne": pannes, "fichiers_gardes_cites": toleres, "fautes": fautes}


# ------------------------------------------------------- (A3) fichiers de scores et de sondes inchangés, sans voisin

def point_a3(racine: Path, run_bbis: str, commit: str) -> dict:
    propre = racine / REGISTRE_PROPRE
    if not propre.is_file():
        raise NonFaisable(f"registre propre {REGISTRE_PROPRE} absent du disque")
    lignes = [[x.strip() for x in l.strip().strip("|").split("|")] for l in
              propre.read_text(encoding="utf-8", errors="replace").splitlines() if cle_de(l) == "SCORES-BBIS"]
    if len(lignes) != 1 or len(lignes[0]) != 4 or not SHA.fullmatch(lignes[0][3]):
        raise NonFaisable(f"ligne SCORES-BBIS : {len(lignes)} ligne(s) lisible(s) au registre propre, une exigée, bien formée")
    sondes, sha_ligne = lignes[0][2], lignes[0][3]
    if sondes != f"diag/{run_bbis}/sondes-bbis.json":
        raise NonFaisable("ligne SCORES-BBIS : chemin autre que diag/<run de la course>/sondes-bbis.json")
    exiger_histoire_complete(racine)
    if not COMMIT.fullmatch(commit) or git(racine, "cat-file", "-e", f"{commit}^{{commit}}", codes=tuple(range(256))).returncode:
        raise NonFaisable(f"commit des sorties de la course {commit[:12]} absent du dépôt")
    fautes = []
    if not noms_git(racine, commit, sondes):
        fautes.append({"nom": sondes, "motif": "absent du commit des sorties"})
    elif empreinte_git(racine, commit, sondes) != sha_ligne:
        fautes.append({"nom": sondes, "motif": "au commit des sorties, empreinte autre que celle de la ligne SCORES-BBIS"})
    if not (racine / sondes).is_file():
        fautes.append({"nom": sondes, "motif": "absent du disque"})
    elif empreinte_fichier(racine / sondes) != sha_ligne:
        fautes.append({"nom": sondes, "motif": "sur le disque, empreinte autre que celle de la ligne SCORES-BBIS"})
    comptes = {}
    for dossier in (f"diag/{run_bbis}", f"donnees/{run_bbis}", f"runs/{run_bbis}"):
        au_commit = set(noms_git(racine, commit, dossier))
        d = racine / dossier
        if d.is_symlink() or (d.exists() and not d.is_dir()):
            fautes.append({"nom": dossier, "motif": "ni dossier ni absent"})
            continue
        disque = set(fichiers_du_disque(d, racine)) if d.is_dir() else set()
        fautes += [{"nom": n, "motif": "fichier de plus que le commit des sorties"} for n in sorted(disque - au_commit)]
        fautes += [{"nom": n, "motif": "fichier de moins que le commit des sorties"} for n in sorted(au_commit - disque)]
        for n in sorted(disque & au_commit):
            p = racine / n
            if p.is_symlink() or not p.is_file():
                fautes.append({"nom": n, "motif": "ni fichier ordinaire ni absent"})
            elif empreinte_fichier(p) != empreinte_git(racine, commit, n):
                fautes.append({"nom": n, "motif": "octets autres que ceux du commit des sorties"})
        comptes[dossier] = {"fichiers_au_commit": len(au_commit), "fichiers_sur_le_disque": len(disque)}
    return {"conforme": not fautes, "commit_des_sorties": commit, "sondes": sondes, "sha256_de_la_ligne_SCORES-BBIS": sha_ligne,
            "dossiers": comptes, "fautes": fautes}


# --------------------------------------------------------------------- sorties imprimées gardées des lancements antérieurs

def sorties_gardees(racine: Path, sorties) -> dict:
    releve = []
    for chemin, sha in sorties:
        p = Path(chemin) if Path(chemin).is_absolute() else racine / chemin
        x = {"chemin": chemin, "sha256_donnee": sha, "etat": "conforme"}
        comp = Path(str(p) + ".sha256")
        if not SHA.fullmatch(sha):
            x["etat"] = "empreinte donnée mal formée"
        elif not p.is_file() or p.is_symlink():
            x["etat"] = "sortie absente"
        elif empreinte_fichier(p) != sha:
            x["etat"] = "sortie d'une autre empreinte que celle donnée"
        elif not comp.is_file():
            x["etat"] = "sortie non scellée (compagnon absent)"
        elif (comp.read_text(encoding="utf-8", errors="replace").split() or [""])[0] != sha:
            x["etat"] = "sortie non scellée (compagnon différent)"
        elif SEUIL in p.read_text(encoding="utf-8", errors="replace"):
            x["etat"] = "la sortie porte la ligne du seuil"
        releve.append(x)
    return {"conforme": bool(releve) and all(x["etat"] == "conforme" for x in releve), "sorties": releve,
            **({} if releve else {"motif": "aucune sortie gardée donnée"})}


# ------------------------------------------------------------------------------------------------------------ programme

def relever(racine: Path, run_lecture: str, run_bbis: str, sorties) -> dict:
    points = {}
    for nom, f in (("A1", lambda: point_a1(racine)), ("A2", lambda: point_a2(racine, run_lecture)),
                   ("A3", lambda: point_a3(racine, run_bbis, COMMIT_SORTIES))):
        try:
            points[nom] = f()
        except NonFaisable as e:
            points[nom] = {"conforme": False, "non_faisable": str(e)}
        except OSError as e:
            points[nom] = {"conforme": False, "non_faisable": f"lecture du disque en échec ({type(e).__name__})"}
    points["sorties"] = sorties_gardees(racine, sorties)
    conforme = all(p["conforme"] is True for p in points.values())
    classement = (CONSOMMEE if not points["sorties"]["conforme"] else PERMISE if conforme else NOEUD)
    return {**points, "conforme": conforme, "classement": classement}


def main(argv=None) -> int:
    try:
        exiger_environnement_git_propre()
    except Arret as e:
        print(f"BBIS PREUVE APRES COUP ARRET : {e}")
        return 2
    ap = argparse.ArgumentParser(description="preuve « aucune donnée ouverte », après coup (lecture de l'étape B bis)")
    for a in ("--racine", "--run-lecture", "--run-bbis", "--numero"):
        ap.add_argument(a, required=True)
    ap.add_argument("--sortie-lancement", nargs=2, action="append", default=[], metavar=("CHEMIN", "EMPREINTE"),
                    help="sortie imprimée, gardée et scellée, d'un lancement antérieur ; à répéter pour chacun")
    a = ap.parse_args(argv)
    racine = Path(a.racine)
    try:
        if not re.fullmatch(r"[1-9][0-9]*", a.numero):
            raise Arret(f"numéro {a.numero!r} : entier à partir de 1 attendu")
        if not RUN.fullmatch(a.run_lecture) or not RUN.fullmatch(a.run_bbis):
            raise Arret("nom de run : format AAAAMMJJ-HHMMSS-nom attendu")
        if not racine.is_dir():
            raise Arret(f"racine {racine} : dossier absent")
        rel = SORTIE.format(n=a.numero)
        piece = racine / rel
        if piece.exists() or Path(str(piece) + ".sha256").exists():
            raise Arret(f"{rel} existe déjà : on n'écrase jamais (R12)")
    except Arret as e:
        print(f"BBIS PREUVE APRES COUP ARRET : {e}")
        return 2
    doc = {"piece": "preuve « aucune donnée ouverte », faite après coup (complément au quatrième addendum, GO-2026-11-18-64)",
           "numero": int(a.numero), "releve_le": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "run_de_lecture": a.run_lecture, "run_de_la_course": a.run_bbis,
           **relever(racine, a.run_lecture, a.run_bbis, a.sortie_lancement)}
    piece.parent.mkdir(parents=True, exist_ok=True)
    piece.write_text(json.dumps(doc, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sha = empreinte_fichier(piece)
    Path(str(piece) + ".sha256").write_text(f"{sha}  {piece.name}\n", encoding="utf-8")
    print(f"BBIS PREUVE APRES COUP ECRITE {rel} {sha} conforme={'oui' if doc['conforme'] else 'non'} "
          f"classement={doc['classement']}")
    return 0 if doc["conforme"] else 1


if __name__ == "__main__":
    sys.exit(main())
