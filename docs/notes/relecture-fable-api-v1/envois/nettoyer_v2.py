"""Copies nettoyées pour la relecture par Fable 5.2 appelé par l'interface d'Anthropic (GO-2026-11-21-84) — version 2.

Écrit par Claude Opus 5.5, opérateur des relectures, le 21 novembre 2026. Pièce de travail (classe C).

v2 : copie de `nettoyer_v1.py` (92280be3…, inchangé, R12), deux changements seulement : (1) le nom écrit en
minuscules dans un identifiant (clé JSON `mot_de_lazar`, que la règle de la v1, sensible à la casse de l'initiale,
laissait passer et que la garde refusait) est remplacé : « de_lazar » → « du_directeur », sinon « lazar » →
« directeur » ; (2) la garde est importée de `controle_ia.relecture_fable_api_v3` (fonction identique à la v2) et la
table s'écrit `<nom>.table-remplacement-v2.json`.

L'outil `controle_ia.relecture_fable_api_v2` ne nettoie jamais : il refuse. Ce programme écrit, pour chaque fichier
source, une copie de même nom de base dans le dossier de destination, avec les seuls remplacements suivants (ordre de la
mère) :
  - « Lazar » → « le directeur » (contractions : « de Lazar » → « du directeur », « à Lazar » → « au directeur ») ;
  - « Ciric » (sans casse ni accent) → « [nom] » ;
  - identifiant de session (`session_…`, UUID) → « [session] » ;
  - adresse de courriel → « [courriel] » ;
  - chemin ou terme interdit (« consigne-privee », « conception-ii-b », « donnees/ », et « verite », « rendu »,
    « scores » dans un chemin ou un nom) → « [chemin réservé] » : le texte entre accents graves qui en porte un est
    remplacé en entier ; hors accents graves, le jeton de chemin entier, ou le terme seul.
Puis il passe la copie à la garde de motifs de l'outil (même fonction, importée) : elle doit être vide, sinon arrêt
(code 1), rien n'est laissé à demi. Chaque copie reçoit son compagnon `.sha256` ; la table de remplacement de la
copie (JSON : source, empreintes, chaque remplacement avec ligne, règle, texte d'avant et d'après) est écrite à côté,
`<nom>.table-remplacement-v2.json`, scellée elle aussi. N'écrase jamais (mode « x »).

Emploi (depuis la racine du dépôt, PYTHONPATH=src) :
    python docs/notes/relecture-fable-api-v1/envois/nettoyer_v2.py DOSSIER_DESTINATION SOURCE [SOURCE …]
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys

from controle_ia.relecture_fable_api_v3 import garde_motifs_ligne, sans_accents

VERSION = "nettoyer_v2"
RESERVE = "[chemin réservé]"

# Termes de chemin, sur le texte d'origine (accents et casse admis)
A = r"[aàâ]"
E = r"[eéèê]"
TERME_PARTOUT = re.compile(
    rf"consigne[\s_\-]*priv{E}{E}|conception[\s_\-.()]*ii[\s_\-.()]*b|donn{E}{E}s\s*[/\\]", re.IGNORECASE)
TERME_CHEMIN = re.compile(rf"v{E}rit{E}|rendu|scores", re.IGNORECASE)
CODE_EN_LIGNE = re.compile(r"`([^`\n]+)`")
JETON_CHEMIN = re.compile(r"[^\s`«»\"'()\[\],;]+")
SESSION = re.compile(r"session[_\-][0-9A-Za-z]{20,}", re.IGNORECASE)
UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.IGNORECASE)
COURRIEL = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}")
LAZAR = re.compile(r"(?:(?P<prep>\b[Dd]e|(?<![\w])[àÀ])\s+)?L[Aa][Zz][Aa][Rr]")
LAZAR_MINUSCULE = re.compile(r"(?P<prep>de_)?lazar")
CIRIC = re.compile(r"[CcĆćČč][Ii][Rr][Ii][CcĆćČč]")


def empreinte(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def _jeton_de_chemin(j: str) -> bool:
    return any(s in j for s in "/\\_-") or bool(re.search(r"\.[A-Za-z0-9]{1,8}$", j))


def nettoyer_ligne(ligne: str, n: int, journal: list) -> str:
    def note(regle, avant, apres):
        journal.append({"ligne": n, "regle": regle, "avant": avant, "apres": apres})

    # 1. texte entre accents graves qui porte un chemin ou un terme interdit : remplacé en entier
    def code(m):
        c = m.group(1)
        if TERME_PARTOUT.search(c) or TERME_CHEMIN.search(c):
            note("chemin entre accents graves", m.group(0), f"`{RESERVE}`")
            return f"`{RESERVE}`"
        return m.group(0)
    ligne = CODE_EN_LIGNE.sub(code, ligne)

    # 2. hors accents graves : jeton de chemin entier qui porte un terme ; puis le terme seul (prose)
    def jeton(m):
        j = m.group(0)
        if RESERVE in j:
            return j
        if _jeton_de_chemin(j) and (TERME_PARTOUT.search(j) or TERME_CHEMIN.search(j)):
            if TERME_PARTOUT.fullmatch(j):
                return j  # le terme seul : traité en 3
            note("jeton de chemin", j, RESERVE)
            return RESERVE
        return j
    ligne = JETON_CHEMIN.sub(jeton, ligne)

    def terme(m):
        note("terme interdit", m.group(0), RESERVE)
        return RESERVE
    ligne = TERME_PARTOUT.sub(terme, ligne)

    # 3. identifiants, courriels
    for motif, regle, remplacement in ((SESSION, "identifiant de session", "[session]"),
                                       (UUID, "identifiant (UUID)", "[session]"),
                                       (COURRIEL, "courriel", "[courriel]")):
        def rep(m, regle=regle, remplacement=remplacement):
            note(regle, m.group(0), remplacement)
            return remplacement
        ligne = motif.sub(rep, ligne)

    # 4. noms
    def lazar(m):
        prep = m.group("prep")
        if prep is None:
            apres = "le directeur"
        elif prep in ("de",):
            apres = "du directeur"
        elif prep == "De":
            apres = "Du directeur"
        elif prep == "à":
            apres = "au directeur"
        else:  # « À »
            apres = "Au directeur"
        note("nom « Lazar »", m.group(0), apres)
        return apres
    ligne = LAZAR.sub(lazar, ligne)

    def lazar_minuscule(m):
        apres = "du_directeur" if m.group("prep") else "directeur"
        note("nom « lazar » en minuscules (identifiant)", m.group(0), apres)
        return apres
    ligne = LAZAR_MINUSCULE.sub(lazar_minuscule, ligne)

    def ciric(m):
        note("nom « Ciric »", m.group(0), "[nom]")
        return "[nom]"
    ligne = CIRIC.sub(ciric, ligne)
    return ligne


def ecrire_x(chemin: str, octets: bytes) -> None:
    with open(chemin, "xb") as f:
        f.write(octets)
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{empreinte(octets)}  {os.path.basename(chemin)}\n")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    dest, sources = argv[0], argv[1:]
    os.makedirs(dest, exist_ok=True)
    for src in sources:
        with open(src, "rb") as f:
            octets = f.read()
        texte = octets.decode("utf-8")
        journal: list = []
        lignes = [nettoyer_ligne(l, i, journal) for i, l in enumerate(texte.split("\n"), start=1)]
        copie = "\n".join(lignes)
        restes = [(i, m) for i, l in enumerate(copie.split("\n"), start=1) for m in garde_motifs_ligne(l)]
        if restes:
            print(f"ARRÊT : la copie de {src} ne passe pas la garde : {restes[:10]}", file=sys.stderr)
            return 1
        cible = os.path.join(dest, os.path.basename(src))
        oc = copie.encode("utf-8")
        ecrire_x(cible, oc)
        table = {"programme": VERSION, "source": src, "sha256_source": empreinte(octets), "copie": cible,
                 "sha256_copie": empreinte(oc), "nombre_de_remplacements": len(journal),
                 "par_regle": {r: sum(1 for j in journal if j["regle"] == r) for r in sorted({j["regle"] for j in journal})},
                 "remplacements": journal}
        ecrire_x(cible + ".table-remplacement-v2.json",
                 (json.dumps(table, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))
        print(f"{cible} : {len(journal)} remplacements {table['par_regle']} ; sha256 {table['sha256_copie']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
