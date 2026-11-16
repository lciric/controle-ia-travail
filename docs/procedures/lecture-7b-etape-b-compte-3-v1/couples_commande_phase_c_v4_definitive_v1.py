"""Mise au propre de la commande phase C v4 du compte 3 : brouillon 1 → nom définitif — v1.

Raison unique : la contre-lecture du brouillon 1 (`contre-lecture-commande-phase-c-v4-tour1-v1.md`,
ea92ff95696e57a9488a3bc799e3da4bd5e107b66220ecd233c72a354c2a44fd, même dossier) le juge scellable, sans correction, et
demande (points pour la mère, 2) la copie à l'octet sous `commande-compte-3-phase-c-v4.md`, l'empreinte f4bcf406… gardée.
Le brouillon ne porte aucune mention d'état de brouillon (son mot « brouillon » n'y apparaît que dans le nom réel d'une
sortie scellée, l. 48 et 573, et dans « brouillons des papiers », l. 162) : la liste des couples est donc **vide**, et la
cible est une copie à l'octet. Aucun bloc de commande ne change.

Usage : python3 -I -B couples_commande_phase_c_v4_definitive_v1.py [--cible CHEMIN]
(`--cible` : pour un essai dans un dossier jetable seulement ; par défaut, `commande-compte-3-phase-c-v4.md`, même dossier.)
Gardes : empreinte du brouillon 1 égale à l'attendue ; chaque « ancien » (aucun ici) présent exactement une fois ; aucune
ligne du brouillon ne commence par une mention d'état (« État du fichier », « Brouillon ») ; cible absente (création
exclusive : jamais d'écrasement) ; empreinte de la cible égale à celle de la source (copie à l'octet). Tout écart : code 1,
rien n'est écrit. Le sceau (compagnon `.sha256`) est posé ensuite par `controle_ia.scellement sceller`.
"""
import hashlib
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "commande-compte-3-phase-c-v4-brouillon1.md"
EMPREINTE_SOURCE = "f4bcf4064e7ab7d53538ce998c2d4745a1ac4387443505d82e8f7a01aec7c755"
CIBLE = ICI / "commande-compte-3-phase-c-v4.md"

COUPLES = []  # aucune mention d'état de brouillon : copie à l'octet

ETAT = re.compile(r"^\s*(- )?\*\*(État du fichier|Brouillon)\b", re.M)


def arret(motif: str) -> None:
    print(f"ARRÊT : {motif} ; rien n'est écrit")
    sys.exit(1)


def main(argv: list) -> int:
    cible = CIBLE
    if argv:
        if len(argv) != 2 or argv[0] != "--cible":
            print("usage : couples_commande_phase_c_v4_definitive_v1.py [--cible CHEMIN]")
            return 2
        cible = pathlib.Path(argv[1]).resolve()
    octets = SOURCE.read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if h != EMPREINTE_SOURCE:
        arret(f"empreinte du brouillon 1 {h} différente de l'attendue")
    texte = octets.decode("utf-8")
    if ETAT.search(texte):
        arret("mention d'état de brouillon trouvée : la copie à l'octet n'est pas permise")
    for ancien, nouveau in COUPLES:
        n = texte.count(ancien)
        if n != 1 or ancien == nouveau:
            arret(f"« ancien » trouvé {n} fois")
        texte = texte.replace(ancien, nouveau, 1)
    sortie = texte.encode("utf-8")
    if not COUPLES and sortie != octets:
        arret("la copie diffère de la source")
    try:
        with open(cible, "xb") as f:
            f.write(sortie)
    except FileExistsError:
        arret(f"{cible} existe déjà (jamais d'écrasement)")
    hc = hashlib.sha256(cible.read_bytes()).hexdigest()
    print(f"source {SOURCE.name} : {h}")
    print(f"couples appliqués : {len(COUPLES)} (copie à l'octet)")
    print(f"cible {cible.name} : {hc} ; égale à la source : {hc == h}")
    return 0 if hc == h else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
