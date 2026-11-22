#!/usr/bin/env python3
"""Vérification par programme des couples (ancien, nouveau) de l'erratum 1 de la
conception 2 (les épreuves du devin), v3 consolidée. Classe C ; aucun appel réseau ;
ne réécrit ni la v3 consolidée ni l'erratum.

Usage :
    python verification-couples-erratum-1-v3-consolidee-v1.py [--sortie CHEMIN.txt] [--consolide CHEMIN.md]

Contrôles :
1. l'empreinte de la v3 consolidée est celle que l'erratum dit corriger ;
2. tout titre « ## » de l'erratum est un couple lisible, au format des errata de la v2
   (« ## identifiant — lieu », « Ancien : », bloc ```text, « Nouveau : », bloc ```text) ;
   les identifiants sont distincts et dans l'ordre annoncé en tête ;
3. chaque ancien figure une seule fois dans la v3 consolidée (fichier entier) ;
4. appliqués dans l'ordre, chaque ancien est unique à son tour et chaque nouveau est
   présent après son application ; aucun nouveau ne laisse en double un ancien à venir ;
5. défaire dans l'ordre inverse redonne exactement la v3 consolidée ;
6. aucun ancien n'est égal à son nouveau ; l'en-tête de la consolidation n'est pas touché.

Un écart : arrêt, code de retour 1, rien n'est écrit. « --consolide » écrit le texte
corrigé (lecture seule, sans valeur de pièce) ; « --sortie » écrit le compte rendu ;
aucun fichier existant n'est écrasé (R12).
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
BASE = ICI.parent
V3 = BASE / "conception-2-epreuves-du-devin-v3-consolidee.md"
ERRATUM = BASE / "conception-2-epreuves-du-devin-v3-consolidee-erratum-1.md"
EMPREINTE_V3 = "e45bb77049937162cf3ee9608b8883b104129b42eaa3215abfcd474848687bd9"
MARQUE = "<!-- fin de l'en-tête de la consolidation ; le texte consolidé suit -->"
MOTIF = re.compile(r"^## (\S+)([^\n]*)\n\nAncien :\n(`{3,})text\n(.*?)\n\3\n\nNouveau :\n(`{3,})text\n(.*?)\n\5\n", re.S | re.M)


class Arret(Exception):
    pass


def sha256(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def lire_couples(texte: str) -> list[dict]:
    couples = [{"id": m.group(1), "lieu": m.group(2).strip(" —"), "ancien": m.group(4), "nouveau": m.group(6)}
               for m in MOTIF.finditer(texte)]
    titres = re.findall(r"^## (\S+)", texte, re.M)
    if not couples or len(couples) != len(titres):
        lus = {c["id"] for c in couples}
        raise Arret(f"couples non tous lisibles : {len(couples)} lus pour {len(titres)} titres « ## » ; illisibles : {[t for t in titres if t not in lus]}")
    ids = [c["id"] for c in couples]
    if len(set(ids)) != len(ids):
        raise Arret(f"identifiants en double : {ids}")
    return couples


def ordre_annonce(texte: str) -> list[str]:
    m = re.search(r"^- Couples \((\d+)\), dans l'ordre d'application[^:\n]*: ([^\n]+)$", texte, re.M)
    if not m:
        raise Arret("ligne « - Couples (N), dans l'ordre d'application … : … » absente de l'en-tête")
    ids = [x.strip().rstrip(".") for x in m.group(2).split(";")]
    if int(m.group(1)) != len(ids):
        raise Arret(f"l'en-tête annonce {m.group(1)} couples et en nomme {len(ids)}")
    return ids


def verifier() -> tuple[list[str], str]:
    lignes: list[str] = []
    dire = lignes.append
    if not V3.exists() or not ERRATUM.exists():
        raise Arret(f"fichier absent : {V3 if not V3.exists() else ERRATUM}")
    e_v3 = sha256(V3)
    if e_v3 != EMPREINTE_V3:
        raise Arret(f"empreinte de la v3 consolidée {e_v3} ≠ {EMPREINTE_V3}")
    v3 = V3.read_text(encoding="utf-8")
    erratum = ERRATUM.read_text(encoding="utf-8")
    if EMPREINTE_V3 not in erratum:
        raise Arret("l'erratum ne cite pas l'empreinte de la v3 consolidée qu'il corrige")
    couples = lire_couples(erratum)
    annonce = ordre_annonce(erratum)
    if annonce != [c["id"] for c in couples]:
        raise Arret(f"ordre annoncé {annonce} ≠ ordre des couples {[c['id'] for c in couples]}")
    if v3.count(MARQUE) != 1:
        raise Arret("marque de fin d'en-tête de la consolidation absente ou en double")
    fin_entete = v3.index(MARQUE) + len(MARQUE)

    dire("Vérification des couples de l'erratum 1 de la conception 2, v3 consolidée")
    dire(f"- v3 consolidée : {V3.relative_to(BASE.parents[3])} — sha256 {e_v3} (conforme)")
    dire(f"- erratum : {ERRATUM.relative_to(BASE.parents[3])} — sha256 {sha256(ERRATUM)}")
    dire(f"- programme : {Path(__file__).name} — sha256 {sha256(Path(__file__))}")
    dire(f"- couples lus : {len(couples)} ; tout titre « ## » est un couple ; ordre conforme à l'en-tête")
    dire("")
    dire("identifiant | lieu | ligne de l'ancien dans la v3 | lignes de l'ancien | lignes du nouveau | signes ancien → nouveau")

    # 3. unicité dans la v3 entière
    for c in couples:
        n = v3.count(c["ancien"])
        if n != 1:
            raise Arret(f"{c['id']} : l'ancien figure {n} fois dans la v3 consolidée (une seule attendue) : « {c['ancien'][:80]}… »")
        if c["ancien"] == c["nouveau"]:
            raise Arret(f"{c['id']} : ancien et nouveau identiques")
        pos = v3.index(c["ancien"])
        if pos < fin_entete:
            raise Arret(f"{c['id']} : l'ancien touche l'en-tête de la consolidation")
        ligne = v3.count("\n", 0, pos) + 1
        dire(f"{c['id']} | {c['lieu']} | {ligne} | {c['ancien'].count(chr(10)) + 1} | {c['nouveau'].count(chr(10)) + 1} | {len(c['ancien'])} → {len(c['nouveau'])}")

    # 4. application dans l'ordre
    texte = v3
    for i, c in enumerate(couples):
        n = texte.count(c["ancien"])
        if n != 1:
            raise Arret(f"{c['id']} : à son tour, l'ancien figure {n} fois")
        texte = texte.replace(c["ancien"], c["nouveau"])
        if c["nouveau"] not in texte:
            raise Arret(f"{c['id']} : nouveau absent après application")
        for suivant in couples[i + 1:]:
            if texte.count(suivant["ancien"]) != 1:
                raise Arret(f"{c['id']} : après son application, l'ancien de {suivant['id']} figure {texte.count(suivant['ancien'])} fois")
    consolide = texte

    # 5. défaire dans l'ordre inverse
    for c in reversed(couples):
        n = texte.count(c["nouveau"])
        if n != 1:
            raise Arret(f"{c['id']} : en défaisant, le nouveau figure {n} fois")
        texte = texte.replace(c["nouveau"], c["ancien"])
    if texte != v3:
        raise Arret("défaire dans l'ordre inverse ne redonne pas la v3 consolidée")

    dire("")
    dire("Contrôles tenus : chaque ancien figure une seule fois dans la v3 consolidée ; appliqués dans l'ordre, chacun est unique à son tour")
    dire("et chaque nouveau est présent ; aucun nouveau ne met en double un ancien à venir ; défaire dans l'ordre inverse redonne exactement")
    dire("la v3 consolidée ; l'en-tête de la consolidation n'est pas touché.")
    dire(f"- texte corrigé (non écrit, sauf « --consolide ») : {len(consolide)} signes, sha256 {hashlib.sha256(consolide.encode('utf-8')).hexdigest()}")
    return lignes, consolide


def ecrire(chemin: Path, contenu: str) -> None:
    if chemin.exists():
        raise Arret(f"{chemin} existe déjà : on n'écrase jamais")
    chemin.write_text(contenu, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie")
    ap.add_argument("--consolide")
    args = ap.parse_args()
    try:
        lignes, consolide = verifier()
        if args.sortie:
            ecrire(Path(args.sortie), "\n".join(lignes) + "\n")
        if args.consolide:
            ecrire(Path(args.consolide), consolide)
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 1
    print("\n".join(lignes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
