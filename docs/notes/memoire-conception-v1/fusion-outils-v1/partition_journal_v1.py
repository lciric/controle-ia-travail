"""Partition du journal des idées et extrait commun, version 1 (22 novembre 2026).

Pièce d'instrument (classe B), session bibliothécaire (Claude Opus 5.5). Applique le § 3 de l'étape 2 de la fusion
(fusion-etape-2-deux-listes-deux-partitions-v1.md, f859d691…), acceptée par la mère.

Un événement est « commune » si et seulement si :
  1. source.chemin est autorisé par la liste stricte v4 (listes_lecture_v1.autorise_stricte) ;
  2. source.extrait se retrouve mot pour mot (espaces normalisés) au chemin, au commit cité (résolu en SHA complet) ;
  3. la fiche est née « commune » (sa ligne de naissance remplit 1 et 2) ;
  4. la fiche n'est pas marquée « mère » par la mère (fichier optionnel --marquees, un identifiant de fiche par ligne) ;
  5. ni `nom` ni `mots` ne portent un nom exclu (mots exclus de la v3, « ne-pas-lire », « transcription »).
Sinon « mère ». Toute ligne illisible ou mal formée : « mère », comptée. Dans le doute, « mère ».
L'extrait ne garde que les champs CHAMPS_COMMUNS ; il est écrit en création exclusive (R12), avec son compagnon d'empreinte,
et un rapport de comptes (sans contenu) est imprimé.
Usage : python -I partition_journal_v1.py SORTIE.jsonl JOURNAL.jsonl [JOURNAL2.jsonl …] [--marquees F] [--depot .]
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

CHAMPS_COMMUNS = ("quand", "fiche", "evenement", "nom", "etat", "source", "sert", "issue", "raison", "reveil", "mots",
                  "partition")
CHAMPS_SOURCE = ("chemin", "commit", "repere", "extrait")
RAISONS = ("réfutée", "occupée", "trop chère", "remplacée", "hors cap", "risque", "mot du directeur")
MOTS_INTERDITS = tuple(ll1.vc6.EXCLUS_MOTS) + ("ne-pas-lire", "transcription")


def resoudre(depot, commit, cache):
    if commit in cache:
        return cache[commit]
    sha = None
    if isinstance(commit, str) and re.fullmatch(r"[0-9a-f]{7,40}", commit):
        r = subprocess.run(["git", "-C", depot, "rev-parse", "--verify", "--quiet", f"{commit}^{{commit}}"],
                           capture_output=True, text=True)
        if r.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", r.stdout.strip()):
            sha = r.stdout.strip()
    cache[commit] = sha
    return sha


def extrait_retrouve(depot, ev, cache_c, cache_t):
    src = ev.get("source")
    if not isinstance(src, dict):
        return False, "source absente"
    chemin = ll1.normaliser_chemin(src.get("chemin", ""))
    ok, motif = ll1.autorise_stricte(chemin)
    if not ok:
        return False, "source hors liste stricte"
    sha = resoudre(depot, src.get("commit"), cache_c)
    if not sha:
        return False, "commit introuvable"
    cle = (sha, chemin)
    if cle not in cache_t:
        b = ll1.vc6.lire_au_commit(depot, sha, chemin)
        cache_t[cle] = None if b is None else ll1.vc6.normaliser_texte(b.decode("utf-8", "replace"))
    texte = cache_t[cle]
    if texte is None:
        return False, "chemin absent au commit"
    ext = ll1.vc6.normaliser_texte(src.get("extrait", ""))
    if len(ext) < 10 or ext not in texte:
        return False, "extrait introuvable mot pour mot"
    return True, ""


def champ_libre_propre(ev):
    morceaux = [str(ev.get("nom", ""))] + [str(m) for m in (ev.get("mots") or [])]
    bas = ll1.sans_accents(" ".join(morceaux)).lower()
    return not any(m in bas for m in MOTS_INTERDITS)


def reduire(ev):
    r = {k: ev.get(k) for k in CHAMPS_COMMUNS}
    r["source"] = {k: ev["source"].get(k) for k in CHAMPS_SOURCE}
    if r.get("raison") not in RAISONS:
        r["raison"] = None
    r["partition"] = "commune"
    return r


def partitionner(evenements, depot, marquees=()):
    """evenements : liste de dict (ou None pour une ligne illisible). Rend (communs réduits, comptes)."""
    cache_c, cache_t = {}, {}
    nees_communes, nees_meres = set(), set()
    comptes = {"lignes": 0, "commune": 0, "mere": 0, "illisibles": 0, "motifs": {}}
    sortie = []
    for ev in evenements:
        comptes["lignes"] += 1
        if not isinstance(ev, dict) or not isinstance(ev.get("fiche"), str):
            comptes["illisibles"] += 1
            comptes["mere"] += 1
            continue
        fiche = ev["fiche"]
        ok, motif = extrait_retrouve(depot, ev, cache_c, cache_t)
        if ok and not champ_libre_propre(ev):
            ok, motif = False, "nom exclu dans nom ou mots"
        if ev.get("evenement") == "naissance":
            if ok and fiche not in nees_meres:
                nees_communes.add(fiche)
            else:
                nees_meres.add(fiche)
                nees_communes.discard(fiche)
        if ok and fiche not in nees_communes:
            ok, motif = False, "fiche née « mère » ou sans naissance commune"
        if ok and fiche in marquees:
            ok, motif = False, "fiche marquée par la mère"
        if ok:
            sortie.append(reduire(ev))
            comptes["commune"] += 1
        else:
            comptes["mere"] += 1
            comptes["motifs"][motif] = comptes["motifs"].get(motif, 0) + 1
    # Une fiche dont une seconde naissance est « mère » sort entièrement de l'extrait.
    sortie = [e for e in sortie if e["fiche"] not in nees_meres]
    comptes["commune"] = len(sortie)
    comptes["mere"] = comptes["lignes"] - comptes["commune"]
    return sortie, comptes


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("sortie")
    p.add_argument("journaux", nargs="+")
    p.add_argument("--marquees", default=None)
    p.add_argument("--depot", default=".")
    a = p.parse_args(argv)
    if os.path.exists(a.sortie) or os.path.exists(a.sortie + ".sha256"):
        print(f"ARRET : {a.sortie} existe déjà (R12)", file=sys.stderr)
        return 1
    if not ll1.normaliser_chemin(os.path.relpath(os.path.abspath(a.sortie), os.path.realpath(a.depot))).startswith(
            ll1.VEILLE_COMMUNE) and not os.environ.get("PARTITION_SORTIE_LIBRE"):
        print(f"ARRET : la sortie doit être sous {ll1.VEILLE_COMMUNE}", file=sys.stderr)
        return 1
    marquees = set()
    if a.marquees:
        marquees = {l.strip() for l in open(a.marquees, encoding="utf-8") if l.strip()}
    evs = []
    for j in a.journaux:
        for l in open(j, encoding="utf-8"):
            if not l.strip():
                continue
            try:
                evs.append(json.loads(l))
            except ValueError:
                evs.append(None)
    sortie, comptes = partitionner(evs, a.depot, marquees)
    with open(a.sortie, "x", encoding="utf-8") as f:
        for e in sortie:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    h = hashlib.sha256(open(a.sortie, "rb").read()).hexdigest()
    with open(a.sortie + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {os.path.basename(a.sortie)}\n")
    print(json.dumps(comptes, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
