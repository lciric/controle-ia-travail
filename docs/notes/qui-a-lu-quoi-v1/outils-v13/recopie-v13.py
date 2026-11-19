"""Recopie à l'octet de la version 12 de la liste « qui a lu quoi » en version 13 — v1.

Usage (depuis la racine du dépôt) :
    python3 -I docs/notes/qui-a-lu-quoi-v1/outils-v13/recopie-v13.py .

Ce que fait le programme, et rien d'autre :
1. il lit `registres/qui-a-lu-quoi-v12.md` et s'arrête si son empreinte n'est pas celle
   de la version en vigueur (R-3552) ;
2. il vérifie les repères de structure de la version 12 (titre, puce de la version 12,
   ligne 261 du tableau, réserve 23, dernière ligne de fin) ;
3. il lit les pièces neuves `pieces-neuves-v13.md` (même dossier), écrites par le
   rédacteur : la puce de la version 13, les lignes 262 à 312 du tableau, la réserve 24 ;
4. il relève l'heure unique par `date -u` et la porte à la place du marqueur
   `<<HEURE_V13>>` ;
5. il écrit `registres/qui-a-lu-quoi-v13.md` : titre changé, puce neuve en tête,
   « (ce fichier) » de la puce de la version 12 changé en « (version précédente) »,
   lignes neuves après la ligne 261, réserve 24 après la réserve 23 (précédée d'une
   ligne vide), ligne de fin de la version 13 ; toutes les autres lignes de la
   version 12 sont recopiées à l'octet ;
6. il refuse d'écrire si la version 13 existe déjà (R12) ; tout écart arrête en code 2,
   sans rien écrire (R5).
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

EMPREINTE_V12 = "accfabe38a1e71fea36da38749c6be5f77b83c66e757a243c7ce7a042c8e1eca"
TITRE_V12 = "# Liste « qui a lu quoi » du programme — version 12\n"
TITRE_V13 = "# Liste « qui a lu quoi » du programme — version 13\n"
AVANT_PUCE_V12 = "- **Version 12** (ce fichier) :"
APRES_PUCE_V12 = "- **Version 12** (version précédente) :"
MARQUEUR = "<<HEURE_V13>>"
PREMIERE_LIGNE_NEUVE = 262


def arret(motif: str) -> None:
    print(f"ARRÊT : {motif}")
    sys.exit(2)


def lire_pieces(chemin: Path) -> tuple[str, list[str], str]:
    sections: dict[str, list[str]] = {}
    courante = None
    for ligne in chemin.read_text(encoding="utf-8").split("\n"):
        m = re.fullmatch(r"=== (PUCE|LIGNES|RESERVE|FIN) ===", ligne)
        if m:
            courante = m.group(1)
            if courante in sections:
                arret(f"section {courante} en double dans les pièces")
            sections[courante] = []
            continue
        if courante is None:
            if ligne.strip():
                arret("texte avant la première section des pièces")
            continue
        if courante == "FIN":
            if ligne.strip():
                arret("texte après la section FIN des pièces")
            continue
        if ligne.strip():
            sections[courante].append(ligne)
    for nom in ("PUCE", "LIGNES", "RESERVE", "FIN"):
        if nom not in sections:
            arret(f"section {nom} absente des pièces")
    if len(sections["PUCE"]) != 1 or not sections["PUCE"][0].startswith("- **Version 13** (ce fichier) :"):
        arret("la section PUCE doit porter une seule ligne, la puce de la version 13")
    if len(sections["RESERVE"]) != 1 or not sections["RESERVE"][0].startswith("24. **Version 13"):
        arret("la section RESERVE doit porter une seule ligne, la réserve 24")
    lignes = sections["LIGNES"]
    for i, ligne in enumerate(lignes):
        attendu = f"| {PREMIERE_LIGNE_NEUVE + i} | "
        if not ligne.startswith(attendu):
            arret(f"ligne neuve {i + 1} : début attendu {attendu!r}")
        if not ligne.endswith(" |"):
            arret(f"ligne neuve {PREMIERE_LIGNE_NEUVE + i} : fin de ligne de tableau attendue")
        if ligne.count("|") != 9:
            arret(f"ligne neuve {PREMIERE_LIGNE_NEUVE + i} : {ligne.count('|')} barres au lieu de 9")
    return sections["PUCE"][0], lignes, sections["RESERVE"][0]


def heure_date_u() -> str:
    sortie = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True)
    heure = sortie.stdout.strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", heure):
        arret(f"heure illisible : {heure!r}")
    return heure


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        arret("un seul argument : la racine du dépôt")
    racine = Path(argv[0])
    chemin_v12 = racine / "registres" / "qui-a-lu-quoi-v12.md"
    chemin_v13 = racine / "registres" / "qui-a-lu-quoi-v13.md"
    chemin_pieces = Path(__file__).resolve().parent / "pieces-neuves-v13.md"

    octets_v12 = chemin_v12.read_bytes()
    if hashlib.sha256(octets_v12).hexdigest() != EMPREINTE_V12:
        arret("empreinte de la version 12 différente de celle de R-3552")
    v12 = octets_v12.decode("utf-8").splitlines(keepends=True)
    if len(v12) != 411:
        arret(f"la version 12 a {len(v12)} lignes au lieu de 411")
    if v12[0] != TITRE_V12:
        arret("titre de la version 12 inattendu")
    if not v12[2].startswith(AVANT_PUCE_V12):
        arret("la ligne 3 n'est pas la puce de la version 12")
    if not v12[335].startswith("| 261 | ") or v12[336] != "\n":
        arret("la ligne 336 n'est pas la ligne 261 du tableau suivie d'une ligne vide")
    if not v12[400].startswith("23. **Version 11") or v12[401] != "\n":
        arret("la ligne 401 n'est pas la réserve 23 suivie d'une ligne vide")
    if not v12[410].startswith("Version 11 : ") or not v12[410].endswith("\n"):
        arret("la dernière ligne n'est pas la ligne de fin de la version 11")

    puce, lignes_neuves, reserve = lire_pieces(chemin_pieces)
    heure = heure_date_u()
    puce = puce.replace(MARQUEUR, heure)
    lignes_neuves = [l.replace(MARQUEUR, heure) for l in lignes_neuves]
    reserve = reserve.replace(MARQUEUR, heure)
    for texte in [puce, reserve, *lignes_neuves]:
        if "<<" in texte or ">>" in texte:
            arret("marqueur non rempli dans les pièces")

    puce_v12 = v12[2].replace(AVANT_PUCE_V12, APRES_PUCE_V12, 1)
    if puce_v12 == v12[2]:
        arret("la puce de la version 12 n'a pas changé")

    sortie: list[str] = []
    sortie.append(TITRE_V13)                    # ligne 1 : titre
    sortie.append(v12[1])                       # ligne 2 : ligne vide, recopiée
    sortie.append(puce + "\n")                  # ligne 3 : puce de la version 13
    sortie.append(puce_v12)                     # ligne 4 : puce de la version 12, « (version précédente) »
    sortie.extend(v12[3:336])                   # lignes 4 à 336 de la version 12, jusqu'à la ligne 261
    sortie.extend(l + "\n" for l in lignes_neuves)
    sortie.extend(v12[336:401])                 # lignes 337 à 401 de la version 12, jusqu'à la réserve 23
    sortie.append("\n")
    sortie.append(reserve + "\n")
    sortie.extend(v12[401:411])                 # lignes 402 à 411 de la version 12
    sortie.append(f"Version 13 : {heure}, heure unique relevée par `date -u` à l'écriture du fichier.\n")

    octets_v13 = "".join(sortie).encode("utf-8")
    if chemin_v13.exists():
        arret(f"{chemin_v13} existe déjà : R12 interdit d'écraser")
    with open(chemin_v13, "xb") as f:
        f.write(octets_v13)

    print(f"heure relevée par date -u : {heure}")
    print(f"version 12 : {len(v12)} lignes, sha256 {EMPREINTE_V12}")
    print(f"pièces neuves : sha256 {hashlib.sha256(chemin_pieces.read_bytes()).hexdigest()}")
    print(f"lignes neuves du tableau : {len(lignes_neuves)} ({PREMIERE_LIGNE_NEUVE} à {PREMIERE_LIGNE_NEUVE + len(lignes_neuves) - 1})")
    print(f"version 13 : {len(sortie)} lignes, sha256 {hashlib.sha256(octets_v13).hexdigest()}")
    print(f"écrite : {chemin_v13}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
