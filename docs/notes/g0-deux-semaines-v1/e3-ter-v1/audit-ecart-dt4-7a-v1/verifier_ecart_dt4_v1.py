#!/usr/bin/env python3
"""Audit de l'écart DT-4 de la course 7a (décision (b) de Lazar, R-2048) : vérificateur structurel par catégories, v1.

Consigne : docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/consigne-audit-ecart-dt4-7a-v1.md
(ca5024ae6ba71314a87918f3a9ae68fc40584ac10d75962b83e7f22fbbe9fe79).

CE QUE LE SCRIPT ÉCRIT : des comptes, des chemins, des numéros de ligne, des identifiants de commit, des catégories et des
classements. JAMAIS le texte d'une ligne. Les empreintes passées en argument ne sont rappelées que par leurs 8 premiers
caractères.

CE QUE LE SCRIPT NE FAIT JAMAIS :
- ouvrir un chemin qui correspond à un motif interdit (INTERDITS_LECTURE) : un tel chemin est compté, jamais lu ;
- lancer une commande git qui écrive ou qui parle au réseau (seulement : rev-parse, log, diff, cat-file, ls-tree --name-only,
  merge-base --is-ancestor sur des commits de `main` ou de référence) ;
- récupérer le commit de quarantaine : il vérifie seulement qu'aucun commit de la plage ne commence par son préfixe.

Contrôles (numérotés comme la consigne) :
1. chemins ajoutés, modifiés, supprimés par chaque commit de la plage : aucun ne doit correspondre à un motif interdit ni à
   un nom de la lecture B ; noms de l'arbre final ; empreintes sha256 des fichiers écrits par la plage comparées aux
   empreintes interdites (préfixes) ; noms et identifiants cités par les lignes de registre désignées (recherche des noms
   et empreintes de B) ;
2. aucun commit de la plage ne commence par le préfixe du commit de quarantaine ;
3. catégories C1 à C7 (et X : mention du fichier des sondes ou de B) sur les lignes AJOUTÉES de chaque commit de la plage ;
3 bis. sur les mêmes lignes, nombres décimaux entre 0 et 1 (forme d'une aire ou d'une borne) sans ligne ni contexte
   antérieurs : comptés par ligne, chacun expliqué par l'auditeur (table EXPLICATIONS_DECIMAUX) ou « à examiner » ;
4. mêmes catégories sur le texte entier des pièces nommées (ou une sélection : #Ldébut-fin, #R-xxxx..R-yyyy, #entete) et
   sur le différentiel d'une révision à l'autre ; les consignes désignées doivent nommer les fichiers interdits.

Classement de chaque occurrence :
- automatique « (ii) » si la ligne entière, ou le contexte de l'occurrence (±CONTEXTE caractères dans la ligne), figure à
  l'identique dans un texte de référence dont le commit est antérieur ou égal à la limite d'antériorité ;
- sinon par la table CLASSEMENTS ci-dessous (classement à la lecture du contexte par l'auditeur), qui ne s'applique que si
  la ligne est identique à celle de la version classée (référence, chemin, ligne) ;
- sinon « à classer ».
Classes : (i) description de l'écart en catégories (permis, forme de R-2041) ; (ii) texte de conception antérieur à 7a ou
indépendant de ses résultats ; (ii-A) grandeur de 7a hors du fichier des sondes, dont la source est établie sur `main`
(lecture A et sortie de l'extracteur de garde, qui ne lit jamais le fichier des sondes) ; (ii-B) grandeur de 7a hors des
catégories C1 à C7 dont la source n'est pas établie sur `main` (constat du rapport) ; (iii) transfert possible d'un
résultat de sonde de 7a (constat).

Gardes éprouvées (R5) sur un dépôt factice : cas sain (0 occurrence, 0 chemin interdit) ; cas piégé (3 chemins interdits
signalés et jamais lus, empreinte interdite retrouvée, préfixe de quarantaine retrouvé, motif neuf « à classer ») ;
lecture d'un chemin interdit refusée avant tout appel à git ; antériorité : ligne identique → (ii), contexte modifié ou
valeur ajoutée → « à classer » ; décimal nu sans mot-clé → « à examiner » (contrôle 3 bis), « T0.6 » et « 1,0 » ignorés.

Usage (voir la commande exacte dans le rapport) :
    python3 -I -B verifier_ecart_dt4_v1.py --depot DEPOT --plage BASE..FIN [--piece REF:CHEMIN[#SEL] ...]
        [--differentiel REF:CHEMIN REF:CHEMIN] [--anterieur REF:CHEMIN ...] [--limite-anteriorite COMMIT]
        [--empreinte-interdite HEX ...] [--nom-b NOM ...] [--chercher-noms-b REF:CHEMIN#SEL ...]
        [--commit-quarantaine PREFIXE] [--nomme-interdits REF:CHEMIN ...] [--classements FICHIER.json] --sortie FICHIER.json
Bibliothèque standard seule ; aucun réseau.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

VERSION = "v1"
CONTEXTE = 60

# --- Motifs larges par catégorie (consigne, point 3) ------------------------------------------------------------------
# Frontières de mot où « _ » et « - » séparent (clés JSON en tirets bas comprises) : (?<!L) avant, (?!L) après.
_L = r"[0-9A-Za-zÀ-ÖØ-öø-ÿ]"
_D, _F = rf"(?<!{_L})", rf"(?!{_L})"
_S = r"[-_ ]"
MOTIFS = {
    "C1": rf"{_D}(aires?|AUC|AUROC|areas?|pli{_S}?0|fold{_S}?0|bornes?|bounds?){_F}",
    "C2": rf"{_D}(au{_S}dessus|above){_F}|{_D}T6-[3-9]{_F}",
    "C3": rf"{_D}(audit{_S}des{_S}sondes|probe{_S}audit){_F}",
    "C4": rf"{_D}(sondes?{_S}d[ée]cisives?|decisive{_S}probes?|familles?|famil(y|ies)|couches?|layers?){_F}",
    "C5": rf"{_D}(mahalanobis|dur[ée]es?{_S}par{_S}couples?|durees{_S}s|couples?{_S}descriptifs?){_F}",
    "C6": rf"{_D}(tables?{_S}[BC]|suspendue?s?|suspended){_F}",
    "C7": rf"{_D}(courbes?|curves?|T6-6|verdict{_S}?p3{_S}?bis){_F}",
    "X": rf"{_D}(lecture{_S}sondes|lecture{_S}B|quarantaine){_F}",
}
MOTIFS_RE = {k: re.compile(v, re.IGNORECASE) for k, v in MOTIFS.items()}

# --- Chemins jamais lus (interdits communs v1, point 1) ; contrôle 1 de la consigne --------------------------------------
INTERDITS_LECTURE = [
    r"(^|/)lecture-sondes[^/]*$",
    r"^diag/20261109-070232-t06-reel(/|$)",
    r"^runs/20261109-070232-t06-reel(/|$)",
    r"(^|/)bras-attaque",
    r"mode-tenu-a-l-ecart",
    r"(^|/)lecture-b-7a",
]
INTERDITS_CONTROLE_1 = [
    r"(^|/)lecture-sondes",
    r"^diag/20261109-070232-t06-reel/",
    r"^runs/20261109-070232-t06-reel/",
]
NOMS_INTERDITS_A_NOMMER = [
    "diag/20261109-070232-t06-reel/lecture-sondes-t06.json",
    "diag/*/lecture-sondes-t06.json",
    "donnees/lecture-b-7a-quarantaine-v1",
    "essai/t06-explo-v3",
]

# --- Raisons des classements de l'auditeur (ses mots, jamais le texte d'une ligne) ------------------------------------
RAISONS = {
    "ANT-L": "ligne identique dans un texte de référence antérieur à la limite d'antériorité (mécanique)",
    "ANT-C": "contexte de chaque occurrence (±60 caractères dans la ligne) identique dans un texte de référence antérieur (mécanique)",
    "I-ECART": "description de l'écart DT-4 en catégories, sans valeur (forme de R-2041), ou rappel de la décision et de la quarantaine",
    "I-INTERDIT": "nom d'un fichier ou d'une branche interdits, cité pour l'interdire ou pour dire qu'il n'a pas été lu",
    "II-PROC": "procédure, conception ou plan (ordre, ce qui sera lu, par qui, quand), sans résultat de 7a",
    "II-GARDE": "garde d'équivalence au 99e centile par couche d'activation (couches 7, 15, 23 de la configuration) : objet distinct des sondes",
    "II-AUTRE": "mot de la famille du motif employé pour un autre objet (prix, mémoire, familles d'organismes, graines, essais), sans lien avec une sonde de 7a",
    "II-HIST": "rappel d'une décision ou d'un texte antérieur à 7a (renvoi à un registre ou à une révision antérieure), sans résultat de 7a",
    "IIA-LECTA": "grandeur de 7a tirée de la lecture A ou de la sortie de l'extracteur de garde (source établie sur main, extracteur qui ne lit jamais le fichier des sondes)",
    "II-EMPREINTE": "empreinte sha256 du fichier des sondes (identifiant d'intégrité déclaré par la chaîne dans son compagnon, vérifié par sha256sum) : aucun contenu du fichier",
    "IIB-COUT": "grandeurs de coût de 7a hors des catégories C1 à C7 (coût lisible, variances du coût, troncatures, compteur de jetons), « reçues de la session mère », absentes de la lecture A : source non établie sur main (voir le rapport)",
}

# Table de classement à la lecture du contexte (auditeur, 2026-11-09) : la classe ne s'applique que si la ligne est
# identique à la ligne de même numéro dans `ref:chemin`. Classe (ii-B) : grandeur de 7a hors des catégories C1 à C7, de
# source non établie sur main ; ni description de l'écart, ni transfert d'un résultat de sonde ; constat du rapport.
_R3 = "brouillons/T0.6-organismes-v0-v1-candidat12-r3.md"
_J = "brouillons/T0.6-organismes-v0-v1-candidat12-r3-journal-v1.md"
_LA = "docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/lecture-A-exploratoire-non-opposable-v1.md"
_GJ = ("docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/"
       "garde-equivalence-20261109-070232-t06-reel-exploratoire-non-opposable-r522.json")
_CE36 = "docs/notes/g0-deux-semaines-v1/e3-ter-v1/contre-lecture-regle-e3-6-transcription-v1-cl1.md"
_CS = "docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/"


def _c(ref, chemin, lignes, classe, raison):
    return {"ref": ref, "chemin": chemin, "lignes": lignes, "classe": classe, "raison": raison}


CLASSEMENTS: list[dict] = [
    _c("6886b61e", _R3, [350, 838], "(i)", "I-INTERDIT"),
    _c("6886b61e", _R3, [351, 861], "(i)", "I-ECART"),
    _c("6886b61e", _R3, [206, 354, 702], "(ii)", "II-PROC"),
    _c("6886b61e", _R3, [683], "(ii)", "II-AUTRE"),
    _c("6886b61e", _R3, [681], "(ii-A)", "IIA-LECTA"),
    _c("6886b61e", _R3, [616], "(ii-B)", "IIB-COUT"),
    _c("6886b61e", _J, [8, 393, 561], "(i)", "I-INTERDIT"),
    _c("6886b61e", _J, [394, 639], "(i)", "I-ECART"),
    _c("6886b61e", _J, [211, 397, 441, 516], "(ii)", "II-PROC"),
    _c("6886b61e", _J, [470], "(ii)", "II-AUTRE"),
    _c("6886b61e", _J, [468], "(ii-A)", "IIA-LECTA"),
    _c("6886b61e", _J, [452], "(ii-B)", "IIB-COUT"),
    _c("6886b61e", _LA, [3], "(ii)", "II-PROC"),
    _c("6886b61e", _LA, [16], "(ii)", "II-EMPREINTE"),
    _c("6886b61e", _LA, [52], "(ii)", "II-GARDE"),
    _c("6886b61e", _LA, [36, 76, 85, 90, 94, 101], "(ii-A)", "IIA-LECTA"),
    _c("6886b61e", _GJ, [48], "(ii)", "II-PROC"),
    _c("6886b61e", _GJ, ["73-79", "115-121", "157-163", "199-205", "241-247", "286-292"], "(ii-A)", "IIA-LECTA"),
    _c("6886b61e", "registres/decisions.md", [1998, 1999, 2006], "(i)", "I-ECART"),
    _c("6886b61e", "registres/decisions.md", [2000], "(ii)", "II-AUTRE"),
    _c("6886b61e", "registres/etat.md", [3], "(i)", "I-ECART"),
    _c("6886b61e", "registres/passations/2026-11-09-2117.md", [6, 15, 20], "(i)", "I-ECART"),
    _c("6886b61e", "docs/procedures/brief-reprise-nouvelle-mere-2026-11-09-v1.md", [20], "(i)", "I-INTERDIT"),
    _c("6886b61e", _CE36, [37, 62, 65], "(ii)", "II-GARDE"),
    _c("61607820", _CS + "consigne-audit-ecart-dt4-7a-v1.md", [9, 23, 31, 32], "(i)", "I-INTERDIT"),
    _c("61607820", _CS + "consigne-audit-ecart-dt4-7a-v1.md", [19, 33], "(i)", "I-ECART"),
    _c("61607820", _CS + "consigne-audit-ecart-dt4-7a-v1.md", [38], "(ii)", "II-PROC"),
    _c("61607820", _CS + "consigne-conception-ii-b-saboteur-budget-v1.md", [9], "(i)", "I-INTERDIT"),
    _c("61607820", _CS + "consigne-conception-ii-b-saboteur-budget-v1.md", [20, 28], "(ii)", "II-AUTRE"),
    _c("61607820", _CS + "consigne-contre-lecture-3-t06-candidat12-r3-v1.md", [9], "(i)", "I-INTERDIT"),
    _c("61607820", _CS + "interdits-communs-v1.md", [6, 7], "(i)", "I-INTERDIT"),
    # Complément : commit 62ba4a4a (R-2052, 22:03 UTC), postérieur à la plage, passé au script pendant l'audit.
    _c("62ba4a4a", "registres/decisions.md", [2010], "(i)", "I-INTERDIT"),
]

# Contrôle 3 bis : explication des lignes qui portent des décimaux entre 0 et 1 sans antériorité (auditeur, à la lecture).
CODES_DECIMAUX = {
    "D-LECTA": "valeur de la lecture A ou de la sortie de l'extracteur de garde (fraction de la garde, centile de la garde, tolérance, heures, mémoire)",
    "D-CONFIG": "valeur de configuration (fraction de la garde, plafond, doses) fixée avant 7a ou par l'ordre de 7a",
    "D-DEVIS": "prix, heures (lecture A) et arithmétique du devis",
    "D-COUT7A": "grandeurs de coût de 7a reçues de la mère (classe (ii-B)), arithmétique qui en dérive, valeurs du plan de la r2 citées pour comparaison",
}
EXPLICATIONS_DECIMAUX: list[dict] = [
    _c("6886b61e", _LA, "*", "expliqué", "D-LECTA"),
    _c("6886b61e", _GJ, "*", "expliqué", "D-LECTA"),
    _c("6886b61e", _R3, [3, 202, 205, 240, 354, 475], "expliqué", "D-LECTA"),
    _c("6886b61e", _R3, [245], "expliqué", "D-CONFIG"),
    _c("6886b61e", _R3, [349, 616], "expliqué", "D-COUT7A"),
    _c("6886b61e", _R3, [681, 682, 683], "expliqué", "D-DEVIS"),
    _c("6886b61e", _J, [188, 207, 210, 324, 397, 412], "expliqué", "D-LECTA"),
    _c("6886b61e", _J, [349], "expliqué", "D-CONFIG"),
    _c("6886b61e", _J, [392, 452], "expliqué", "D-COUT7A"),
    _c("6886b61e", _J, [468, 469, 470], "expliqué", "D-DEVIS"),
    _c("6886b61e", "registres/decisions.md", [1998, 2004], "expliqué", "D-LECTA"),
    _c("6886b61e", "registres/etat.md", [3], "expliqué", "D-LECTA"),
    _c("6886b61e", "registres/passations/2026-11-09-2117.md", [6], "expliqué", "D-LECTA"),
    _c("6886b61e", _CE36, [38, 62, 63], "expliqué", "D-CONFIG"),
    _c("6886b61e", "registres/depenses.md", [413], "expliqué", "D-DEVIS"),
]


def git(depot: Path, *args: str, ok_codes=(0,)) -> bytes:
    p = subprocess.run(["git", "-C", str(depot), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode not in ok_codes:
        raise SystemExit(f"ARRÊT : git {args[0]} a rendu le code {p.returncode}")
    return p.stdout


def interdit_lecture(chemin: str) -> bool:
    return any(re.search(m, chemin) for m in INTERDITS_LECTURE)


def lire_blob(depot: Path, ref: str, chemin: str) -> bytes | None:
    if interdit_lecture(chemin):
        raise SystemExit("ARRÊT : tentative de lecture d'un chemin interdit (refusée par le script)")
    p = subprocess.run(["git", "-C", str(depot), "cat-file", "blob", f"{ref}:{chemin}"], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    return p.stdout if p.returncode == 0 else None


def lignes_de(octets: bytes) -> list[str]:
    return octets.decode("utf-8", errors="replace").split("\n")


def date_commit(depot: Path, ref: str) -> str:
    return git(depot, "log", "-1", "--format=%cI", ref).decode().strip()


def commit_complet(depot: Path, ref: str) -> str:
    return git(depot, "rev-parse", "--verify", f"{ref}^{{commit}}").decode().strip()


def scanner_ligne(texte: str) -> list[tuple[str, int, int]]:
    occ = []
    for cat, rx in MOTIFS_RE.items():
        for m in rx.finditer(texte):
            occ.append((cat, m.start(), m.end()))
    return occ


def selectionner(lignes: list[str], sel: str | None) -> list[int]:
    """Numéros de ligne (1-based) retenus par la sélection."""
    n = len(lignes)
    if not sel:
        return list(range(1, n + 1))
    if sel == "entete":
        fin = next((i for i, l in enumerate(lignes, 1) if l.startswith("## ")), n + 1)
        return list(range(1, fin))
    m = re.fullmatch(r"L(\d+)-(\d+)", sel)
    if m:
        return list(range(int(m.group(1)), min(int(m.group(2)), n) + 1))
    m = re.fullmatch(r"R-(\d+)\.\.R-(\d+)", sel)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        out = []
        for i, l in enumerate(lignes, 1):
            r = re.match(r"^\| R-(\d+) \|", l)
            if r and a <= int(r.group(1)) <= b:
                out.append(i)
        return out
    raise SystemExit(f"ARRÊT : sélection inconnue {sel!r}")


def separer(spec: str) -> tuple[str, str, str | None]:
    ref, _, reste = spec.partition(":")
    chemin, _, sel = reste.partition("#")
    if not ref or not chemin:
        raise SystemExit(f"ARRÊT : spécification REF:CHEMIN attendue, reçu {spec!r}")
    return ref, chemin, (sel or None)


class References:
    """Textes antérieurs à la limite : lignes entières (strip) et texte entier, pour l'antériorité mécanique."""

    def __init__(self, depot: Path, limite: str):
        self.depot = depot
        self.limite_commit = commit_complet(depot, limite)
        self.limite_date = date_commit(depot, limite)
        self.refs: list[dict] = []
        self._chemins_base: dict[str, dict | None] = {}

    def _charger(self, ref: str, chemin: str, origine: str) -> dict | None:
        if interdit_lecture(chemin):
            return None
        b = lire_blob(self.depot, ref, chemin)
        if b is None:
            return None
        c = commit_complet(self.depot, ref)
        d = date_commit(self.depot, c)
        anterieure = _dt.datetime.fromisoformat(d) <= _dt.datetime.fromisoformat(self.limite_date)
        t = b.decode("utf-8", errors="replace")
        return {"id": f"{c[:8]}:{chemin}", "commit": c, "date": d, "anterieure": bool(anterieure), "origine": origine,
                "lignes": {l.strip() for l in t.split("\n") if l.strip()}, "texte": t}

    def ajouter(self, ref: str, chemin: str):
        r = self._charger(ref, chemin, "argument")
        if r is None:
            raise SystemExit(f"ARRÊT : référence d'antériorité introuvable {ref}:{chemin}")
        self.refs.append(r)

    def base_pour(self, chemin: str) -> dict | None:
        if chemin not in self._chemins_base:
            self._chemins_base[chemin] = self._charger(self.limite_commit, chemin, "même chemin à la limite")
        return self._chemins_base[chemin]

    def anteriorite(self, chemin: str, texte: str, occ: list[tuple[str, int, int]]) -> str | None:
        cands = [r for r in self.refs if r["anterieure"]]
        b = self.base_pour(chemin)
        if b is not None and b["anterieure"]:
            cands = [b] + cands
        s = texte.strip()
        for r in cands:
            if s and s in r["lignes"]:
                return f"ligne:{r['id']}"
        for r in cands:
            if all(texte[max(0, a - CONTEXTE):min(len(texte), e + CONTEXTE)] in r["texte"] for _, a, e in occ):
                return f"contexte:{r['id']}"
        return None

    def resume(self) -> list[dict]:
        out = [{"id": r["id"], "date_commit": r["date"], "anterieure_a_la_limite": r["anterieure"], "origine": r["origine"]}
               for r in self.refs]
        out += [{"id": r["id"], "date_commit": r["date"], "anterieure_a_la_limite": r["anterieure"], "origine": r["origine"]}
                for r in self._chemins_base.values() if r is not None]
        return out


class Classeur:
    def __init__(self, depot: Path, entrees: list[dict]):
        self.depot = depot
        self.table: dict[tuple[str, int], dict] = {}
        self.etoiles: dict[str, dict] = {}
        self._cache: dict[tuple[str, str], list[str] | None] = {}
        for e in entrees:
            if e["lignes"] == "*":
                self.etoiles[e["chemin"]] = e
                continue
            for l in self._etendre(e["lignes"]):
                self.table[(e["chemin"], l)] = e

    @staticmethod
    def _etendre(lignes) -> list[int]:
        out = []
        for x in lignes:
            if isinstance(x, int):
                out.append(x)
            else:
                a, b = (int(v) for v in str(x).split("-"))
                out.extend(range(a, b + 1))
        return out

    def _ligne_classee(self, ref: str, chemin: str, n: int) -> str | None:
        k = (ref, chemin)
        if k not in self._cache:
            b = lire_blob(self.depot, ref, chemin)
            self._cache[k] = lignes_de(b) if b is not None else None
        ls = self._cache[k]
        return ls[n - 1] if ls is not None and 1 <= n <= len(ls) else None

    def classer(self, chemin: str, n: int, texte: str) -> tuple[str, str] | None:
        e = self.table.get((chemin, n)) or self.etoiles.get(chemin)
        if e is None:
            return None
        if self._ligne_classee(e["ref"], chemin, n) != texte:
            return ("à classer", "texte différent de la version classée")
        return (e["classe"], e["raison"])


DECIMAL = re.compile(r"(?<![0-9A-Za-zÀ-ÿ.,_/-])0[.,][0-9]+(?![0-9A-Za-z])")
DECIMAUX: list[dict] = []
EXPLICATEUR: "Classeur | None" = None


def examiner_decimaux(source: str, commit: str | None, ref: str | None, chemin: str, n: int, texte: str,
                      refs: References) -> None:
    """Contrôle 3 bis : nombres décimaux entre 0 et 1 (forme d'une aire ou d'une borne) sur une ligne sans antériorité.
    N'écrit que des comptes et un code d'explication, jamais le nombre ni la ligne."""
    spans = [("D", m.start(), m.end()) for m in DECIMAL.finditer(texte)]
    if not spans:
        return
    if refs.anteriorite(chemin, texte, spans) is not None:
        return
    sans = sum(1 for s in spans if refs.anteriorite(chemin, texte, [s]) is None)
    expl = EXPLICATEUR.classer(chemin, n, texte) if EXPLICATEUR is not None else None
    DECIMAUX.append({"source": source, "commit": commit, "ref": ref, "chemin": chemin, "ligne": n,
                     "decimaux": len(spans), "decimaux_sans_anteriorite": sans,
                     "explication": expl[1] if expl and expl[0] != "à classer" else "à examiner"})


def occurrence(source: str, commit: str | None, ref: str | None, chemin: str, n: int, texte: str,
               refs: References, classeur: Classeur) -> dict | None:
    examiner_decimaux(source, commit, ref, chemin, n, texte, refs)
    occ = scanner_ligne(texte)
    if not occ:
        return None
    cats = sorted({c for c, _, _ in occ})
    ant = refs.anteriorite(chemin, texte, occ)
    manuel = classeur.classer(chemin, n, texte)
    if manuel is not None and manuel[0] != "à classer":
        classe, raison = manuel
    elif ant is not None:
        classe, raison = "(ii)", ("ANT-L" if ant.startswith("ligne:") else "ANT-C")
    elif manuel is not None:
        classe, raison = manuel
    else:
        classe, raison = "à classer", ""
    return {"source": source, "commit": commit, "ref": ref, "chemin": chemin, "ligne": n, "categories": cats,
            "occurrences_dans_la_ligne": len(occ), "anteriorite": ant or "aucune", "classement": classe, "raison": raison}


def lignes_ajoutees(depot: Path, commit: str, chemin: str) -> list[tuple[int, str]]:
    brut = git(depot, "diff", "--no-color", "--no-ext-diff", "--no-renames", "-U0", f"{commit}^", commit, "--", chemin)
    out, n = [], None
    for l in brut.decode("utf-8", errors="replace").split("\n"):
        m = re.match(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@", l)
        if m:
            n = int(m.group(1))
            continue
        if n is None or l.startswith("+++") or l.startswith("---"):
            continue
        if l.startswith("+"):
            out.append((n, l[1:]))
            n += 1
        elif l.startswith(" "):
            n += 1
    return out


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--depot", default=".")
    p.add_argument("--plage", required=True)
    p.add_argument("--piece", action="append", default=[])
    p.add_argument("--differentiel", nargs=2, action="append", default=[])
    p.add_argument("--anterieur", action="append", default=[])
    p.add_argument("--limite-anteriorite", default=None, help="commit limite (défaut : base de la plage)")
    p.add_argument("--empreinte-interdite", action="append", default=[])
    p.add_argument("--nom-b", action="append", default=[])
    p.add_argument("--chercher-noms-b", action="append", default=[])
    p.add_argument("--commit-quarantaine", default="e6c06113")
    p.add_argument("--nomme-interdits", action="append", default=[])
    p.add_argument("--classements", default=None)
    p.add_argument("--sortie", required=True)
    a = p.parse_args(argv)

    depot = Path(a.depot).resolve()
    base, _, fin = a.plage.partition("..")
    base_c, fin_c = commit_complet(depot, base), commit_complet(depot, fin)
    refs = References(depot, a.limite_anteriorite or base)
    for spec in a.anterieur:
        r, c, _ = separer(spec)
        refs.ajouter(r, c)
    entrees = list(CLASSEMENTS)
    if a.classements:
        entrees += json.loads(Path(a.classements).read_text(encoding="utf-8"))
    classeur = Classeur(depot, entrees)
    global EXPLICATEUR
    EXPLICATEUR = Classeur(depot, list(EXPLICATIONS_DECIMAUX))
    empreintes = [h.lower() for h in a.empreinte_interdite]
    noms_b = list(a.nom_b)

    # --- Contrôle 1 et 2 : commits, chemins, empreintes ------------------------------------------------------------
    commits = git(depot, "log", "--reverse", "--format=%H", f"{base_c}..{fin_c}").decode().split()
    c1, total_interdits, blobs, exclus, corresp = [], 0, 0, 0, []
    occs: list[dict] = []
    empreintes_plage: dict[str, str] = {}
    for c in commits:
        ns = git(depot, "diff", "--no-renames", "--name-status", f"{c}^", c).decode("utf-8", errors="replace")
        chemins = [tuple(l.split("\t", 1)) for l in ns.splitlines() if l.strip()]
        interdits = []
        for statut, ch in chemins:
            if any(re.search(m, ch) for m in INTERDITS_CONTROLE_1) or any(nb and nb in ch for nb in noms_b):
                interdits.append({"statut": statut, "chemin": ch})
            if statut == "D":
                continue
            if interdit_lecture(ch):
                exclus += 1
                continue
            b = lire_blob(depot, c, ch)
            if b is not None:
                blobs += 1
                h = hashlib.sha256(b).hexdigest()
                empreintes_plage[h] = ch
                for e in empreintes:
                    if h.startswith(e):
                        corresp.append({"commit": c, "chemin": ch, "empreinte_interdite": e[:8]})
            # Contrôle 3 : lignes ajoutées
            if not ch.endswith((".py", ".md", ".json", ".txt", ".sha256", ".sh", ".csv", ".jsonl", ".yaml", ".yml", ".tex")):
                continue
            for n, t in lignes_ajoutees(depot, c, ch):
                o = occurrence("commit", c, c[:8], ch, n, t, refs, classeur)
                if o:
                    occs.append(o)
        total_interdits += len(interdits)
        cpt = {s: sum(1 for st, _ in chemins if st.startswith(s)) for s in ("A", "M", "D")}
        c1.append({"commit": c, "date_commit": date_commit(depot, c), "ajoutes": cpt["A"], "modifies": cpt["M"],
                   "supprimes": cpt["D"], "chemins": [{"statut": s, "chemin": ch} for s, ch in chemins],
                   "chemins_interdits": interdits})
    noms_fin = git(depot, "ls-tree", "-r", "--name-only", fin_c).decode("utf-8", errors="replace").splitlines()
    noms_fin_interdits = [ch for ch in noms_fin if any(re.search(m, ch) for m in INTERDITS_CONTROLE_1)
                          or any(nb and nb in ch for nb in noms_b)]
    quarantaine = {"prefixe": a.commit_quarantaine, "commits_de_la_plage": len(commits),
                   "commits_qui_commencent_par_le_prefixe": [c for c in commits if c.startswith(a.commit_quarantaine)],
                   "objet_present_dans_le_clone": subprocess.run(
                       ["git", "-C", str(depot), "cat-file", "-e", a.commit_quarantaine], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL).returncode == 0}

    # --- Recherche des noms et empreintes de B dans des lignes désignées et dans les messages de la plage --------------
    recherche_b = []
    hexa = re.compile(r"\b[0-9a-f]{7,64}\b")
    chemin_tok = re.compile(r"`([^`\s]+/[^`\s]+|[^`\s]+\.(?:md|json|txt|py))`")

    def resoudre(tok: str) -> dict:
        t = subprocess.run(["git", "-C", str(depot), "cat-file", "-t", tok], stdout=subprocess.PIPE,
                           stderr=subprocess.DEVNULL)
        if t.returncode == 0 and t.stdout.decode().strip() == "commit":
            return {"identifiant": tok, "nature": "commit présent dans le clone"}
        fichiers = sorted({ch for h, ch in empreintes_plage.items() if h.startswith(tok)})
        if fichiers:
            return {"nature": "empreinte d'un fichier écrit par la plage", "chemins": fichiers}
        return {"identifiant": tok, "nature": "identifiant non résolu dans le clone (commit absent ou empreinte d'un fichier hors de la plage)"}

    for spec in a.chercher_noms_b:
        r, ch, sel = separer(spec)
        ls = lignes_de(lire_blob(depot, r, ch) or b"")
        for n in selectionner(ls, sel):
            t = ls[n - 1]
            recherche_b.append({"ref": r, "chemin": ch, "ligne": n,
                                "chemins_cites": sorted(set(chemin_tok.findall(t))),
                                "identifiants_hexadecimaux": [resoudre(x) for x in sorted(set(hexa.findall(t)))]})
    messages = []
    for c in commits:
        msg = git(depot, "log", "-1", "--format=%B", c).decode("utf-8", errors="replace")
        messages.append({"commit": c, "chemins_cites": sorted(set(chemin_tok.findall(msg))),
                         "identifiants_hexadecimaux": [resoudre(x) for x in sorted(set(hexa.findall(msg)))],
                         "occurrences_categories": sorted({k for k, _, _ in scanner_ligne(msg)})})

    # --- Contrôle 4 : pièces nommées, différentiels, consignes ---------------------------------------------------
    pieces = []
    for spec in a.piece:
        r, ch, sel = separer(spec)
        b = lire_blob(depot, r, ch)
        if b is None:
            pieces.append({"ref": r, "chemin": ch, "selection": sel, "present": False})
            continue
        ls = lignes_de(b)
        nums = selectionner(ls, sel)
        avant = len(occs)
        for n in nums:
            o = occurrence("piece", None, r, ch, n, ls[n - 1], refs, classeur)
            if o:
                occs.append(o)
        dernier = git(depot, "log", "-1", "--format=%H", r, "--", ch).decode().strip()
        pieces.append({"ref": r, "chemin": ch, "selection": sel, "present": True, "sha256": hashlib.sha256(b).hexdigest(),
                       "lignes_du_fichier": len(ls) - (1 if ls and ls[-1] == "" else 0), "lignes_lues": len(nums),
                       "occurrences": len(occs) - avant, "dernier_commit": dernier,
                       "date_dernier_commit": date_commit(depot, dernier) if dernier else None})
    differentiels = []
    for sa, sb in a.differentiel:
        ra, ca, _ = separer(sa)
        rb, cb, _ = separer(sb)
        la, lb = lignes_de(lire_blob(depot, ra, ca) or b""), lignes_de(lire_blob(depot, rb, cb) or b"")
        sm = difflib.SequenceMatcher(None, la, lb, autojunk=False)
        ajout = [j for tag, _, _, j1, j2 in sm.get_opcodes() if tag in ("replace", "insert") for j in range(j1 + 1, j2 + 1)]
        suppr = sum(i2 - i1 for tag, i1, i2, _, _ in sm.get_opcodes() if tag in ("replace", "delete"))
        avant = len(occs)
        for n in ajout:
            o = occurrence("differentiel", None, rb, cb, n, lb[n - 1], refs, classeur)
            if o:
                occs.append(o)
        differentiels.append({"de": f"{ra}:{ca}", "vers": f"{rb}:{cb}", "lignes_ajoutees_ou_remplacees": len(ajout),
                              "lignes_retirees_ou_remplacees": suppr, "occurrences": len(occs) - avant})
    nommes = []
    for spec in a.nomme_interdits:
        r, ch, _ = separer(spec)
        t = (lire_blob(depot, r, ch) or b"").decode("utf-8", errors="replace")
        nommes.append({"ref": r, "chemin": ch, "comptes": {nom: t.count(nom) for nom in NOMS_INTERDITS_A_NOMMER},
                       "nomme_tous": all(t.count(nom) > 0 for nom in NOMS_INTERDITS_A_NOMMER)})

    # --- Synthèse ---------------------------------------------------------------------------------------------
    def compter(cle):
        d: dict[str, int] = {}
        for o in occs:
            v = o[cle]
            for x in (v if isinstance(v, list) else [v]):
                d[x] = d.get(x, 0) + 1
        return dict(sorted(d.items()))

    sortie = {
        "script": "verifier_ecart_dt4_v1.py", "version": VERSION,
        "heure_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tete_du_clone": commit_complet(depot, "HEAD"),
        "regle_de_sortie": "comptes, chemins, numéros de ligne, identifiants de commit, catégories et classements seulement ; aucun texte de ligne",
        "parametres": {"plage": f"{base_c[:8]}..{fin_c[:8]}", "pieces": a.piece, "differentiels": a.differentiel,
                       "anterieurs": a.anterieur, "limite_anteriorite": {"commit": refs.limite_commit, "date": refs.limite_date},
                       "empreintes_interdites_prefixes": [e[:8] for e in empreintes], "noms_b": noms_b,
                       "chercher_noms_b": a.chercher_noms_b, "nomme_interdits": a.nomme_interdits,
                       "contexte_caracteres": CONTEXTE, "motifs": MOTIFS, "interdits_lecture": INTERDITS_LECTURE,
                       "interdits_controle_1": INTERDITS_CONTROLE_1},
        "controle_1_chemins": {"commits": c1, "total_chemins_interdits_dans_la_plage": total_interdits,
                               "arbre_final": {"commit": fin_c, "fichiers": len(noms_fin), "chemins_interdits": noms_fin_interdits},
                               "empreintes": {"fichiers_empreintes": blobs, "fichiers_exclus_par_interdit": exclus,
                                              "correspondances_avec_empreintes_interdites": corresp},
                               "noms_et_empreintes_de_B": {"noms_fournis": noms_b, "lignes_examinees": recherche_b,
                                                           "messages_de_commit": messages}},
        "controle_2_quarantaine": quarantaine,
        "controle_3_4_categories": {"references_anteriorite": refs.resume(), "raisons": RAISONS,
                                    "comptes_par_source": compter("source"), "comptes_par_categorie": compter("categories"),
                                    "comptes_par_classement": compter("classement"),
                                    "classees_iii": [o for o in occs if o["classement"] == "(iii)"],
                                    "a_classer": sum(1 for o in occs if o["classement"] == "à classer"),
                                    "occurrences": occs},
        "controle_3bis_decimaux": {
            "regle": "décimaux entre 0 et 1 (forme d'une aire ou d'une borne) sur les lignes examinées, hors ligne ou contexte antérieurs ; ni le nombre ni la ligne ne sont écrits",
            "codes": CODES_DECIMAUX,
            "lignes": len(DECIMAUX), "decimaux_sans_anteriorite": sum(d["decimaux_sans_anteriorite"] for d in DECIMAUX),
            "par_explication": {k: sum(1 for d in DECIMAUX if d["explication"] == k)
                                for k in sorted({d["explication"] for d in DECIMAUX})},
            "a_examiner": sum(1 for d in DECIMAUX if d["explication"] == "à examiner"),
            "detail": DECIMAUX},
        "controle_4_pieces": {"pieces": pieces, "differentiels": differentiels, "consignes_nomment_les_interdits": nommes},
    }
    Path(a.sortie).write_text(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"occurrences": len(occs), "par_classement": sortie["controle_3_4_categories"]["comptes_par_classement"],
                      "decimaux_lignes": len(DECIMAUX), "decimaux_a_examiner": sortie["controle_3bis_decimaux"]["a_examiner"],
                      "chemins_interdits_plage": total_interdits, "chemins_interdits_arbre_final": len(noms_fin_interdits),
                      "correspondances_empreintes": len(corresp),
                      "commits_quarantaine": len(quarantaine["commits_qui_commencent_par_le_prefixe"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
