#!/usr/bin/env python3
"""Vérification par programme des citations de la lecture du code de DiscoveryAgent (v1).

Écrit par le lecteur Opus 5.5 (mandat 129714fa…). Bibliothèque standard seulement.
Lancement : python3 -I verifier_citations_v1.py --depot … --commit … --lecture … --registre …
            --controles … --papier … --annexe … --sortie …

Ce que le programme vérifie :
1. Citations de code en bloc : une ligne « Source : `chemin:L1-L2` » suivie d'un bloc clôturé ;
   le contenu du bloc doit figurer dans les lignes L1 à L2 du fichier, au commit donné.
2. Citations de code en ligne : `chemin:L1-L2` suivies de « extrait » (ou « `extrait` ») ;
   l'extrait doit figurer dans les lignes L1 à L2 du fichier, au commit donné.
   Une référence `chemin:L1-L2` sans extrait est contrôlée en portée seulement (fichier présent,
   lignes dans le fichier) et comptée à part.
3. Citations du papier et de l'annexe : « papier p. N « extrait » » ou « annexe p. N « extrait » » ;
   l'extrait doit figurer à la page N du texte extrait (pages séparées par un saut de page).
4. Registre de couverture : chaque fichier suivi au commit y figure une fois, avec son nombre de
   lignes (nombre de fins de ligne, comme wc -l) ; « parcouru » n'est permis que pour acs_agent/,
   inputs/*/README.txt et uv.lock.
5. Contrôles de recherche : pour chaque motif, la liste exacte des lignes qui le portent au commit
   (dans la portée donnée) doit égaler la liste attendue (sert aux affirmations « jamais appelé »).

Normalisation commune avant comparaison : NFKC, apostrophes et guillemets typographiques ramenés
à ' et ", espaces insécables en espaces, suites de blancs réduites à une espace.
Le fichier de sortie ne recopie pas les extraits réussis ; il recopie ceux qui échouent.
"""

import argparse
import fnmatch
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from datetime import datetime, timezone

GIT_BASE = ["git", "-c", "core.fsmonitor=false"]

BLOCK_RE = re.compile(
    r"Source : `(?P<path>[^`:\s]+):(?P<l1>\d+)-(?P<l2>\d+)`[ \t]*\n+```[A-Za-z0-9_-]*\n(?P<body>.*?)\n```",
    re.DOTALL,
)
INLINE_RE = re.compile(
    r"`(?P<path>[A-Za-z0-9_./-]+\.[A-Za-z0-9]+):(?P<l1>\d+)(?:-(?P<l2>\d+))?`"
    r"(?:[ ]?«[ ](?:`(?P<extc>[^`\n]+)`|(?P<ext>[^»\n]+?))[ ]»)?"
)
PAPER_RE = re.compile(
    r"(?P<doc>papier|annexe) p\. (?P<page>\d+) «[ ](?P<ext>[^»\n]+?)[ ]»"
)
SKIM_ALLOWED = ("acs_agent/*", "inputs/*/README.txt", "uv.lock")


def normaliser(texte):
    texte = unicodedata.normalize("NFKC", texte)
    for avant, apres in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), (" ", " ")):
        texte = texte.replace(avant, apres)
    return re.sub(r"\s+", " ", texte).strip()


def empreinte(chemin):
    with open(chemin, "rb") as flux:
        return hashlib.sha256(flux.read()).hexdigest()


class Depot:
    def __init__(self, depot, commit):
        self.depot = depot
        self.commit = commit
        sortie = subprocess.run(
            GIT_BASE + ["-C", depot, "rev-parse", "--verify", commit + "^{commit}"],
            capture_output=True, text=True, check=True,
        )
        self.commit_complet = sortie.stdout.strip()
        sortie = subprocess.run(
            GIT_BASE + ["-C", depot, "ls-tree", "-r", "--name-only", "-z", self.commit_complet],
            capture_output=True, check=True,
        )
        self.fichiers = [p for p in sortie.stdout.decode("utf-8").split("\0") if p]
        self._cache = {}

    def contenu(self, chemin):
        if chemin not in self._cache:
            if chemin not in self.fichiers:
                self._cache[chemin] = None
            else:
                sortie = subprocess.run(
                    GIT_BASE + ["-C", self.depot, "cat-file", "-p", self.commit_complet + ":" + chemin],
                    capture_output=True, check=True,
                )
                self._cache[chemin] = sortie.stdout
        return self._cache[chemin]

    def lignes(self, chemin):
        brut = self.contenu(chemin)
        if brut is None:
            return None
        return brut.decode("utf-8", errors="replace").split("\n")


def verifier_code(depot, chemin, l1, l2, extrait):
    lignes = depot.lignes(chemin)
    if lignes is None:
        return False, "fichier absent du commit"
    nb = depot.contenu(chemin).count(b"\n")
    nb_effectif = max(nb, len(lignes) - (1 if lignes and lignes[-1] == "" else 0))
    if l1 < 1 or l2 < l1 or l2 > nb_effectif:
        return False, f"lignes {l1}-{l2} hors du fichier ({nb_effectif} lignes)"
    if extrait is None:
        return True, "portée"
    fenetre = "\n".join(lignes[l1 - 1:l2])
    if normaliser(extrait) in normaliser(fenetre):
        return True, "extrait trouvé"
    return False, "extrait absent de ces lignes"


def main():
    analyseur = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    for nom in ("depot", "commit", "lecture", "registre", "controles", "papier", "annexe", "sortie"):
        analyseur.add_argument("--" + nom, required=True)
    args = analyseur.parse_args()

    depot = Depot(args.depot, args.commit)
    with open(args.lecture, encoding="utf-8") as flux:
        lecture = flux.read()
    pages = {}
    for doc, chemin in (("papier", args.papier), ("annexe", args.annexe)):
        with open(chemin, encoding="utf-8") as flux:
            pages[doc] = flux.read().split("\f")

    rapport = []
    echecs = []
    compte = {
        "bloc_ok": 0, "bloc_echec": 0,
        "ligne_ok": 0, "ligne_echec": 0,
        "portee_ok": 0, "portee_echec": 0,
        "papier_ok": 0, "papier_echec": 0,
        "annexe_ok": 0, "annexe_echec": 0,
    }

    # 1. Citations en bloc (retirées du texte avant la recherche des citations en ligne).
    reste = lecture
    numero = 0
    for m in BLOCK_RE.finditer(lecture):
        numero += 1
        ident = f"B{numero:03d}"
        chemin, l1, l2 = m.group("path"), int(m.group("l1")), int(m.group("l2"))
        ok, motif = verifier_code(depot, chemin, l1, l2, m.group("body"))
        compte["bloc_ok" if ok else "bloc_echec"] += 1
        rapport.append(f"{ident} {'OK   ' if ok else 'ECHEC'} bloc  {chemin}:{l1}-{l2} ({motif})")
        if not ok:
            echecs.append(f"{ident} {chemin}:{l1}-{l2} : {motif}\n---\n{m.group('body')}\n---")
    reste = BLOCK_RE.sub(lambda m: " " * len(m.group(0)), lecture)

    # 2. Citations de code en ligne.
    numero = 0
    for m in INLINE_RE.finditer(reste):
        numero += 1
        ident = f"C{numero:03d}"
        chemin = m.group("path")
        l1 = int(m.group("l1"))
        l2 = int(m.group("l2")) if m.group("l2") else l1
        extrait = m.group("extc") if m.group("extc") is not None else m.group("ext")
        ok, motif = verifier_code(depot, chemin, l1, l2, extrait)
        if extrait is None:
            compte["portee_ok" if ok else "portee_echec"] += 1
            genre = "portee"
        else:
            compte["ligne_ok" if ok else "ligne_echec"] += 1
            genre = "ligne"
        rapport.append(f"{ident} {'OK   ' if ok else 'ECHEC'} {genre:6s}{chemin}:{l1}-{l2} ({motif})")
        if not ok:
            echecs.append(f"{ident} {chemin}:{l1}-{l2} : {motif}\n---\n{extrait}\n---")

    # 3. Citations du papier et de l'annexe.
    numero = 0
    for m in PAPER_RE.finditer(reste):
        numero += 1
        ident = f"P{numero:03d}"
        doc, page, extrait = m.group("doc"), int(m.group("page")), m.group("ext")
        if 1 <= page <= len(pages[doc]):
            ok = normaliser(extrait) in normaliser(pages[doc][page - 1])
            motif = "extrait trouvé" if ok else "extrait absent de la page"
        else:
            ok, motif = False, "page hors du texte"
        compte[f"{doc}_ok" if ok else f"{doc}_echec"] += 1
        rapport.append(f"{ident} {'OK   ' if ok else 'ECHEC'} {doc:6s} p. {page} ({motif})")
        if not ok:
            echecs.append(f"{ident} {doc} p. {page} : {motif}\n---\n{extrait}\n---")
    # Une citation sur une plage de pages ne serait pas vérifiée : elle compte comme échec.
    for m in re.finditer(r"(?P<doc>papier|annexe) p\. \d+\s*[-–]\s*\d+ «", reste):
        numero += 1
        compte[f"{m.group('doc')}_echec"] += 1
        rapport.append(f"P{numero:03d} ECHEC {m.group('doc'):6s} plage de pages non vérifiable : {m.group(0)}")
        echecs.append(f"P{numero:03d} {m.group(0)} : citer une seule page par extrait")

    # 4. Registre de couverture.
    with open(args.registre, encoding="utf-8") as flux:
        registre = json.load(flux)
    entrees = registre["fichiers"] if isinstance(registre, dict) else registre
    vus = {}
    registre_echecs = []
    for entree in entrees:
        chemin = entree["chemin"]
        vus[chemin] = vus.get(chemin, 0) + 1
        brut = depot.contenu(chemin)
        if brut is None:
            registre_echecs.append(f"{chemin} : absent du commit")
            continue
        nb_lignes_commit = brut.count(b"\n")
        if entree["lignes"] != nb_lignes_commit:
            registre_echecs.append(f"{chemin} : {entree['lignes']} lignes inscrites, {nb_lignes_commit} au commit")
        if entree["statut"] not in ("lu en entier", "parcouru"):
            registre_echecs.append(f"{chemin} : statut inconnu {entree['statut']!r}")
        if entree["statut"] == "parcouru" and not any(fnmatch.fnmatch(chemin, motif) for motif in SKIM_ALLOWED):
            registre_echecs.append(f"{chemin} : « parcouru » non permis par le mandat")
        if not entree.get("role", "").strip():
            registre_echecs.append(f"{chemin} : rôle vide")
    for chemin, fois in vus.items():
        if fois > 1:
            registre_echecs.append(f"{chemin} : inscrit {fois} fois")
    manquants = sorted(set(depot.fichiers) - set(vus))
    for chemin in manquants:
        registre_echecs.append(f"{chemin} : manque au registre")
    nb_entier = sum(1 for e in entrees if e["statut"] == "lu en entier")
    nb_parcouru = sum(1 for e in entrees if e["statut"] == "parcouru")

    # 5. Contrôles de recherche.
    with open(args.controles, encoding="utf-8") as flux:
        controles = json.load(flux)
    controle_lignes = []
    controle_echecs = 0
    for controle in controles:
        motif = re.compile(controle["motif"])
        trouves = []
        for chemin in depot.fichiers:
            if not any(fnmatch.fnmatch(chemin, portee) for portee in controle["portee"]):
                continue
            for i, ligne in enumerate(depot.lignes(chemin), start=1):
                if motif.search(ligne):
                    trouves.append(f"{chemin}:{i}")
        attendu = sorted(controle["attendu"])
        ok = sorted(trouves) == attendu
        if not ok:
            controle_echecs += 1
        controle_lignes.append(
            f"{controle['id']} {'OK   ' if ok else 'ECHEC'} motif {controle['motif']!r} : "
            f"{len(trouves)} ligne(s) trouvée(s), {len(attendu)} attendue(s)"
            + ("" if ok else f"\n    trouvées : {sorted(trouves)}\n    attendues : {attendu}")
        )

    total_echecs = (
        compte["bloc_echec"] + compte["ligne_echec"] + compte["portee_echec"]
        + compte["papier_echec"] + compte["annexe_echec"] + len(registre_echecs) + controle_echecs
    )
    entete = [
        "Vérification des citations — lecture du code de DiscoveryAgent v1",
        f"Date (UTC) : {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"Commit vérifié : {depot.commit_complet} ({len(depot.fichiers)} fichiers suivis)",
        f"Lecture : {args.lecture} sha256 {empreinte(args.lecture)}",
        f"Registre : {args.registre} sha256 {empreinte(args.registre)}",
        f"Contrôles : {args.controles} sha256 {empreinte(args.controles)}",
        f"Papier : {args.papier} sha256 {empreinte(args.papier)} ({len(pages['papier'])} morceaux)",
        f"Annexe : {args.annexe} sha256 {empreinte(args.annexe)} ({len(pages['annexe'])} morceaux)",
        "",
        "Bilan :",
        f"  citations de code en bloc     : {compte['bloc_ok']} vérifiées, {compte['bloc_echec']} échecs",
        f"  citations de code en ligne    : {compte['ligne_ok']} vérifiées, {compte['ligne_echec']} échecs",
        f"  références de code sans extrait (portée) : {compte['portee_ok']} vérifiées, {compte['portee_echec']} échecs",
        f"  citations du papier           : {compte['papier_ok']} vérifiées, {compte['papier_echec']} échecs",
        f"  citations de l'annexe         : {compte['annexe_ok']} vérifiées, {compte['annexe_echec']} échecs",
        f"  registre de couverture        : {len(entrees)} entrées ({nb_entier} lues en entier, {nb_parcouru} parcourues), {len(registre_echecs)} échecs",
        f"  contrôles de recherche        : {len(controles) - controle_echecs} vérifiés, {controle_echecs} échecs",
        f"  TOTAL DES ÉCHECS              : {total_echecs}",
        "",
    ]
    corps = entete + ["Détail des citations :"] + rapport + ["", "Contrôles de recherche :"] + controle_lignes
    corps += ["", "Registre de couverture :"] + (registre_echecs or ["  aucun écart"])
    if echecs:
        corps += ["", "Extraits en échec :"] + echecs
    texte = "\n".join(corps) + "\n"
    with open(args.sortie, "w", encoding="utf-8") as flux:
        flux.write(texte)
    print("\n".join(entete))
    return 0 if total_echecs == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
