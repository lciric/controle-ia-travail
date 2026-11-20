"""Extraction du cas X6 (cartes retenues par l'aiguilleur de la course v9) — v1.

Écrit par la mère (session_01XJ6Mgr8BN6UanALsQatc5E) le 20 novembre 2026, sous GO-2026-11-20-15
(option (a) de R-4090) : un agent neuf, qui ne lit aucune carte, joue ce programme sur le seul
journal de l'aiguilleur versé sous le dossier d'archives du commit de versement ; il ne rend que
des identifiants de cartes et des comptes.

Ce que fait le programme :
1. Il lit en mémoire la liste des noms du commit donné et n'en garde que ceux qui finissent par le
   suffixe donné. Il n'affiche jamais cette liste. Il exige exactement un nom ; sinon il s'arrête
   en ne disant que le nombre trouvé.
2. Il lit ce seul fichier par `git show`, calcule son empreinte et le décode comme JSON.
3. Il cherche les objets qui portent une clé `classe`. Pour chacun, il prend l'identifiant de la
   carte dans une clé de la liste CLES_ID, ou, à défaut, la clé de l'objet parent.
4. Il n'écrit que : les noms de clés vus, les comptes par classe, les identifiants par classe, les
   doublons. Aucune autre valeur n'est écrite : ni `categorie`, ni texte, ni motif.

Un identifiant ou une classe qui ne passe pas son motif n'est pas écrit : il est compté comme
illisible et le programme s'arrête par un code non nul. Aucun repli silencieux.

Codes de sortie : 0 conforme ; 2 nombre de fichiers différent de 1 ; 3 aucun objet à `classe` ;
4 identifiant absent, ambigu ou illisible ; 5 classe illisible ; 6 JSON illisible.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

VERSION = "extraire_x6_journal_aiguilleur_v1"
CLES_ID = ("id", "fiche_id", "id_fiche", "carte_id", "id_carte", "identifiant", "carte", "fiche")
MOTIF_ID = re.compile(r"^[A-Za-z0-9._:/-]{1,120}$")
MOTIF_CLASSE = re.compile(r"^[a-z_]{1,40}$")
PROFONDEUR_MAX = 12


class Arret(Exception):
    def __init__(self, code: int, motif: str, details: dict | None = None):
        super().__init__(motif)
        self.code = code
        self.motif = motif
        self.details = details or {}


def _objets_a_classe(noeud, cle_parente=None, profondeur=0):
    """Rend la liste des couples (objet, clé parente) dont l'objet porte une clé `classe`."""
    if profondeur > PROFONDEUR_MAX:
        raise Arret(6, "profondeur du JSON au-delà de la borne")
    trouves = []
    if isinstance(noeud, dict):
        if "classe" in noeud:
            trouves.append((noeud, cle_parente))
        for k, v in noeud.items():
            if isinstance(v, (dict, list)):
                trouves.extend(_objets_a_classe(v, k if isinstance(k, str) else None, profondeur + 1))
    elif isinstance(noeud, list):
        for v in noeud:
            if isinstance(v, (dict, list)):
                trouves.extend(_objets_a_classe(v, None, profondeur + 1))
    return trouves


def _forme(noeud, profondeur=0):
    """Forme du JSON : noms de clés et types seulement, jamais une valeur."""
    if profondeur >= 3:
        return type(noeud).__name__
    if isinstance(noeud, dict):
        return {str(k): _forme(v, profondeur + 1) for k, v in list(noeud.items())[:40]}
    if isinstance(noeud, list):
        return [f"liste de {len(noeud)}"] + ([_forme(noeud[0], profondeur + 1)] if noeud else [])
    return type(noeud).__name__


def extraire(donnees) -> dict:
    objets = _objets_a_classe(donnees)
    if not objets:
        raise Arret(3, "aucun objet ne porte de clé « classe »", {"forme": _forme(donnees)})
    noms_cles = sorted({str(k) for o, _ in objets for k in o})
    par_classe: dict[str, list[str]] = {}
    illisibles_id = 0
    ambigus = 0
    illisibles_classe = 0
    source_id = {"cle": 0, "parent": 0}
    for o, parent in objets:
        candidats = [k for k in CLES_ID if k in o and isinstance(o[k], str)]
        if len(candidats) > 1:
            valeurs = {o[k] for k in candidats}
            if len(valeurs) > 1:
                ambigus += 1
                continue
        if candidats:
            ident = o[candidats[0]]
            source_id["cle"] += 1
        elif isinstance(parent, str):
            ident = parent
            source_id["parent"] += 1
        else:
            illisibles_id += 1
            continue
        if not MOTIF_ID.match(ident):
            illisibles_id += 1
            continue
        classe = o["classe"]
        if not (isinstance(classe, str) and MOTIF_CLASSE.match(classe)):
            illisibles_classe += 1
            continue
        par_classe.setdefault(classe, []).append(ident)
    if ambigus or illisibles_id:
        raise Arret(4, "identifiant absent, ambigu ou illisible",
                    {"noms_cles": noms_cles, "ambigus": ambigus, "illisibles": illisibles_id,
                     "objets": len(objets)})
    if illisibles_classe:
        raise Arret(5, "classe illisible", {"noms_cles": noms_cles, "illisibles": illisibles_classe,
                                            "objets": len(objets)})
    tous = [i for ids in par_classe.values() for i in ids]
    doublons = sorted({i for i in tous if tous.count(i) > 1})
    return {
        "objets_a_classe": len(objets),
        "noms_cles": noms_cles,
        "source_identifiant": source_id,
        "comptes_par_classe": {c: len(v) for c, v in sorted(par_classe.items())},
        "identifiants_par_classe": {c: sorted(v) for c, v in sorted(par_classe.items())},
        "doublons": doublons,
    }


def _git(depot: Path, *args) -> bytes:
    return subprocess.run(["git", "-C", str(depot), *args], check=True, capture_output=True).stdout


def principal(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--depot", required=True, type=Path)
    p.add_argument("--commit", required=True)
    p.add_argument("--suffixe", required=True)
    p.add_argument("--sortie", required=True, type=Path)
    a = p.parse_args(argv)
    rapport = {"version": VERSION, "commit": a.commit, "suffixe": a.suffixe}
    code = 0
    try:
        noms = _git(a.depot, "show", "--name-only", "--format=", a.commit).decode("utf-8").splitlines()
        retenus = [n for n in noms if n.endswith(a.suffixe)]
        rapport["fichiers_trouves"] = len(retenus)
        if len(retenus) != 1:
            raise Arret(2, "le suffixe ne désigne pas exactement un fichier")
        chemin = retenus[0]
        brut = _git(a.depot, "show", f"{a.commit}:{chemin}")
        rapport["chemin"] = chemin
        rapport["sha256_journal"] = hashlib.sha256(brut).hexdigest()
        rapport["octets_journal"] = len(brut)
        try:
            donnees = json.loads(brut.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            raise Arret(6, f"JSON illisible ({type(e).__name__})")
        rapport["extraction"] = extraire(donnees)
        rapport["issue"] = "conforme"
    except Arret as e:
        code = e.code
        rapport["issue"] = "arret"
        rapport["code"] = e.code
        rapport["motif"] = e.motif
        rapport["details"] = e.details
    a.sortie.parent.mkdir(parents=True, exist_ok=True)
    a.sortie.write_text(json.dumps(rapport, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{rapport['issue']} code={code} sortie={a.sortie}")
    if code == 0:
        print("comptes_par_classe=" + json.dumps(rapport["extraction"]["comptes_par_classe"], ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(principal())
