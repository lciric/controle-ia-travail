"""Fabrique le brouillon 7 de l'ordre exploratoire du saboteur à budget (ii-b) — v1.

Usage (depuis la racine du dépôt) :
    python3 -I -B brouillons/ii-b-saboteur-budget-v1/appliquer-brouillon7-ii-b-v1.py

Ce que fait ce programme, et rien d'autre :
1. il vérifie l'empreinte du brouillon 6 de l'ordre et celle du rapport de vérification des brouillons 6 ;
2. il lit dans le § 7 du rapport les 14 couples « avant » / « après », V-1 à V-14 (pour V-2 : le couple
   complet, pas le couple réduit dit en tête du § 7) ;
3. il les applique dans l'ordre au brouillon 6 ; chaque « avant » doit être présent exactement une fois au
   moment de son application, sinon arrêt sans rien écrire ;
4. il contrôle : chaque « après » présent exactement une fois à la fin ; application inverse égale au
   brouillon 6 à l'octet ; 14 marqueurs distincts `<<NOM>>` restants ; sinon arrêt sans rien écrire ;
5. il écrit `ordre-exploratoire-ii-b-v1-brouillon7.md` et `differences-brouillon6-vers-7-v1.md`
   (chaque hunk de `diff -u` rattaché à son ou ses couples, puis la sortie entière de `diff -u`).

Il n'écrase jamais (R12) : arrêt si l'un des deux fichiers de sortie existe. Il n'ouvre que le brouillon 6
de l'ordre, le rapport de vérification, et lui-même (pour son empreinte). Aucun repli silencieux (R5).
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
RACINE = DOSSIER.parent.parent
SOURCE = DOSSIER / "ordre-exploratoire-ii-b-v1-brouillon6.md"
EMPREINTE_SOURCE = "1f65acf781638bfa786c928a7927be8f730c646b55f3b7a3e3676c6d71277db0"
RAPPORT = RACINE / "docs/notes/barreau8-iib-v1/verification-ordre-et-devis-iib-brouillon6-v1.md"
EMPREINTE_RAPPORT = "bd7941ecec095fec470df9cb07e7ba488ac5a6a3060b7c6e5a115b3f435a9127"
SORTIE = DOSSIER / "ordre-exploratoire-ii-b-v1-brouillon7.md"
NOTE = DOSSIER / "differences-brouillon6-vers-7-v1.md"

NOMBRE_COUPLES = 14
MARQUEURS_ATTENDUS = 14
MOTIF_MARQUEUR = re.compile(r"<<([A-Z0-9_]+)>>")
MOTIF_COUPLE = re.compile(
    r"^#### (V-(\d+)) \(([^\n]*?)\) — ([^\n]*)\n\n"
    r"Avant :\n\n~~~text\n(.*?)\n~~~\n\n"
    r"Après :\n\n~~~text\n(.*?)\n~~~\n",
    re.S | re.M,
)
MOTIF_HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


class Arret(Exception):
    """Arrêt sans rien écrire."""


def empreinte(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def lire_verifie(chemin: Path, attendue: str) -> str:
    octets = chemin.read_bytes()
    if empreinte(octets) != attendue:
        raise Arret(f"empreinte inattendue pour {chemin.name} : {empreinte(octets)}")
    return octets.decode("utf-8")


def lire_couples(rapport: str) -> list[dict]:
    debut = rapport.index("\n## 7. Point 6 et couples exacts\n")
    fin = rapport.index("\n## 8. ", debut)
    section = rapport[debut:fin]
    couples = [
        {"nom": m.group(1), "rang": int(m.group(2)), "poids": m.group(3), "lieu": m.group(4),
         "avant": m.group(5), "apres": m.group(6)}
        for m in MOTIF_COUPLE.finditer(section)
    ]
    if len(couples) != NOMBRE_COUPLES or section.count("\n#### V-") != NOMBRE_COUPLES:
        raise Arret(f"{len(couples)} couples lus au § 7 du rapport, {NOMBRE_COUPLES} attendus")
    if [c["rang"] for c in couples] != list(range(1, NOMBRE_COUPLES + 1)):
        raise Arret("les couples du § 7 ne sont pas V-1 à V-14 dans l'ordre")
    for c in couples:
        if not c["avant"] or c["avant"] == c["apres"]:
            raise Arret(f"{c['nom']} : couple vide ou sans changement")
    return couples


def appliquer(texte: str, couples: list[dict]) -> str:
    for c in couples:
        n = texte.count(c["avant"])
        if n != 1:
            raise Arret(f"{c['nom']} : texte « avant » trouvé {n} fois, une attendue")
        texte = texte.replace(c["avant"], c["apres"])
    return texte


def controler(source: str, resultat: str, couples: list[dict]) -> Counter:
    for c in couples:
        n = resultat.count(c["apres"])
        if n != 1:
            raise Arret(f"{c['nom']} : texte « après » trouvé {n} fois à la fin, une attendue")
    retour = resultat
    for c in reversed(couples):
        if retour.count(c["apres"]) != 1:
            raise Arret(f"{c['nom']} : application inverse impossible")
        retour = retour.replace(c["apres"], c["avant"])
    if retour != source:
        raise Arret("l'application inverse ne rend pas le brouillon 6 à l'octet")
    marqueurs = Counter(MOTIF_MARQUEUR.findall(resultat))
    if len(marqueurs) != MARQUEURS_ATTENDUS:
        raise Arret(f"{len(marqueurs)} marqueurs distincts restants, {MARQUEURS_ATTENDUS} attendus")
    return marqueurs


def ligne_de(texte: str, extrait: str) -> tuple[int, int]:
    """Première et dernière ligne (à partir de 1) qu'occupe l'extrait, présent une fois."""
    position = texte.index(extrait)
    premiere = texte.count("\n", 0, position) + 1
    return premiere, premiere + extrait.count("\n")


def sortie_diff(resultat: str) -> str:
    # `diff -u` compare le brouillon 6 sur disque au texte obtenu, passé par l'entrée standard.
    p = subprocess.run(
        ["diff", "-u", "--label", SOURCE.name, "--label", SORTIE.name, str(SOURCE), "-"],
        input=resultat.encode("utf-8"), capture_output=True, check=False,
    )
    if p.returncode != 1 or p.stderr:
        raise Arret(f"diff : code {p.returncode}, {p.stderr.decode('utf-8', 'replace')}")
    return p.stdout.decode("utf-8")


def decouper_hunks(diff: str) -> list[dict]:
    hunks: list[dict] = []
    for ligne in diff.splitlines():
        m = MOTIF_HUNK.match(ligne)
        if m:
            hunks.append({"entete": ligne, "debut": int(m.group(3)), "lignes": [], "courante": int(m.group(3)),
                          "ajoutees": []})
            continue
        if not hunks:
            continue
        h = hunks[-1]
        h["lignes"].append(ligne)
        if ligne.startswith("+"):
            h["ajoutees"].append(h["courante"])
            h["courante"] += 1
        elif ligne.startswith(" "):
            h["courante"] += 1
    return hunks


def rattacher(hunks: list[dict], resultat: str, couples: list[dict]) -> None:
    for h in hunks:
        h["couples"] = []
    for c in couples:
        premiere, derniere = ligne_de(resultat, c["apres"])
        touches = [h for h in hunks if any(premiere <= n <= derniere for n in h["ajoutees"])]
        if len(touches) != 1:
            raise Arret(f"{c['nom']} : rattaché à {len(touches)} hunks, un attendu")
        touches[0]["couples"].append(c)
        c["ligne"] = premiere
    for h in hunks:
        if not h["couples"]:
            raise Arret(f"hunk {h['entete']} : aucun couple, changement hors mandat")


def ecrire_note(resultat: str, couples: list[dict], marqueurs: Counter, diff: str, hunks: list[dict]) -> str:
    cloture = "~~~~"
    if cloture in diff:
        raise Arret("la sortie de diff contient la clôture de la note")
    t: list[str] = []
    t.append("# Différences du brouillon 6 au brouillon 7 de l'ordre exploratoire du saboteur à budget — v1\n")
    t.append("Note fabriquée par programme (`appliquer-brouillon7-ii-b-v1.py`, dans ce dossier), en même temps que le "
             "brouillon 7. Aucun sujet ni mécanisme n'y est écrit. Le devis reste au brouillon 6, intact : aucun couple "
             "ne le touche.\n")
    t.append("## 1. Pièces\n")
    t.append(f"- Brouillon 6 de l'ordre (intact, R12) : `{SOURCE.name}`, `{EMPREINTE_SOURCE}`.")
    t.append(f"- Brouillon 7 de l'ordre : `{SORTIE.name}`, `{empreinte(resultat.encode('utf-8'))}`.")
    t.append(f"- Rapport de vérification des brouillons 6, dont le § 7 porte les couples : "
             f"`{RAPPORT.relative_to(RACINE)}`, `{EMPREINTE_RAPPORT}`.")
    t.append(f"- Programme : `{Path(__file__).name}`, `{empreinte(Path(__file__).read_bytes())}`.")
    t.append("- Décision qui commande ce brouillon : registre des décisions, lignes `R-3509` et `R-3518`.\n")
    t.append("## 2. Ce qui est appliqué\n")
    t.append(f"Les {NOMBRE_COUPLES} couples du § 7 du rapport, V-1 à V-14, lus dans le rapport même (aucun texte "
             "recopié à la main), appliqués dans l'ordre. Pour V-2, le couple complet (retrait de la phrase périmée "
             "et marqueur des tirages et permutations rempli), pas le couple réduit. Contrôles passés par programme : "
             "chaque « avant » présent exactement une fois au moment de son application ; chaque « après » présent "
             "exactement une fois à la fin ; application inverse égale au brouillon 6 à l'octet ; chaque hunk de "
             "`diff -u` rattaché à au moins un couple, chaque couple à un seul hunk. Rien d'autre n'est changé.\n")
    t.append("| couple | poids dit au rapport | lieu dit au rapport | ligne du brouillon 7 | hunk |")
    t.append("|---|---|---|---|---|")
    for c in couples:
        rang = next(i for i, h in enumerate(hunks, 1) if c in h["couples"])
        t.append(f"| {c['nom']} | {c['poids']} | {c['lieu']} | {c['ligne']} | {rang} |")
    t.append("")
    t.append("## 3. Marqueurs restants\n")
    t.append(f"Compté par ce programme, par le seul motif des marqueurs (`<<[A-Z0-9_]+>>`) : "
             f"**{sum(marqueurs.values())} occurrences, {len(marqueurs)} marqueurs distincts** dans le brouillon 7 "
             "(brouillon 6 : 15 distincts ; le marqueur des tirages et permutations de la lecture (2) est rempli par "
             "V-2).\n")
    t.append("| marqueur restant | occurrences |")
    t.append("|---|---|")
    for nom in sorted(marqueurs):
        t.append(f"| `{nom}` | {marqueurs[nom]} |")
    t.append("")
    t.append("## 4. Écarts déclarés\n")
    t.append("- **En-tête non mis à jour.** Aucun couple ne prévoit de changer le titre ni la ligne « Statut » : le "
             "brouillon 7 porte encore « brouillon 6 » dans son titre et son statut, et n'a pas de section « Ce que "
             "le brouillon 7 change ». Le § 7 du rapport dit que le rédacteur du brouillon 7 les ajoute ; le mandat "
             "de la session mère dit de ne rien changer hors des couples : le mandat est suivi, l'écart est à lever "
             "par la mère.")
    t.append("- **Sortie du compte des marqueurs citée, non écrite.** V-5 fait citer au brouillon 7 le fichier "
             "`sortie-compter-marqueurs-ii-b-v3.txt` ; ce fichier n'existe pas : le mandat ne commande que trois "
             "fichiers. Le compte est au § 3 de cette note ; le rejeu de `compter-marqueurs-ii-b-v1.py` sous ce nom "
             "neuf reste à faire.\n")
    t.append("## 5. Chaque hunk, rattaché à son ou ses couples\n")
    for i, h in enumerate(hunks, 1):
        noms = ", ".join(c["nom"] for c in h["couples"])
        t.append(f"### Hunk {i} — {noms}\n")
        for c in h["couples"]:
            t.append(f"- {c['nom']} ({c['poids']}) : {c['lieu']}")
        t.append("")
        t.append(f"{cloture}diff")
        t.append(h["entete"])
        t.extend(h["lignes"])
        t.append(f"{cloture}\n")
    t.append("## 6. Sortie entière de `diff -u`\n")
    t.append(f"Commande : `diff -u {SOURCE.name} {SORTIE.name}` (étiquettes des deux fichiers sans date).\n")
    t.append(f"{cloture}diff")
    t.append(diff.rstrip("\n"))
    t.append(f"{cloture}")
    return "\n".join(t) + "\n"


def main() -> int:
    try:
        for chemin in (SORTIE, NOTE):
            if chemin.exists():
                raise Arret(f"{chemin.name} existe déjà : on n'écrase jamais (R12)")
        source = lire_verifie(SOURCE, EMPREINTE_SOURCE)
        couples = lire_couples(lire_verifie(RAPPORT, EMPREINTE_RAPPORT))
        resultat = appliquer(source, couples)
        marqueurs = controler(source, resultat, couples)
        diff = sortie_diff(resultat)
        hunks = decouper_hunks(diff)
        rattacher(hunks, resultat, couples)
        note = ecrire_note(resultat, couples, marqueurs, diff, hunks)
    except Arret as arret:
        print(f"ARRÊT, rien n'est écrit : {arret}", file=sys.stderr)
        return 1
    SORTIE.write_bytes(resultat.encode("utf-8"))
    NOTE.write_bytes(note.encode("utf-8"))
    print(f"{SORTIE.name}  {empreinte(SORTIE.read_bytes())}")
    print(f"{NOTE.name}  {empreinte(NOTE.read_bytes())}")
    print(f"couples appliqués : {len(couples)} ; hunks : {len(hunks)}")
    print(f"marqueurs : occurrences {sum(marqueurs.values())} ; distincts {len(marqueurs)}")
    for nom in sorted(marqueurs):
        print(f"  {nom} {marqueurs[nom]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
