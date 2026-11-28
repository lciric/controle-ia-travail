"""Assemble le projet de traitement : recopie, par numéros de ligne, les corrections des deux contre-lectures empreintées.

Usage : python3 -B -I assembler_projet_v1.py <gabarit> <sortie> [--montrer]
Aucune donnée de P3 n'est lue ; seuls les deux rapports de contre-lecture et le gabarit.
"""
import hashlib
import pathlib
import re
import sys

P3B = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3b")
RAPPORTS = {
    "M": (P3B / "contre-lectures-brouillon1/methode/contre-lecture-R2-P3b-brouillon1-methode-v1.md",
          "a4f6a7d8b358651717ba9799c524f5d6b26d851ded7eb4496015dd8444ecc6ce"),
    "T": (P3B / "contre-lectures-brouillon1/texte/contre-lecture-R2-P3b-brouillon1-texte-v1.md",
          "5138203119cca20699d8080b4909d72bfcba36c0c7d4d043d11b68971ac42c18"),
}
# repère -> (rapport, première ligne, dernière ligne), numérotation à partir de 1, bornes incluses
PLAGES = {
    "M01": ("M", 87, 101), "M02": ("M", 110, 114), "M03": ("M", 137, 154), "M04": ("M", 166, 176),
    "M05": ("M", 186, 192), "M06": ("M", 201, 209), "M07": ("M", 222, 227), "M08": ("M", 241, 249),
    "M09": ("M", 258, 262), "M10": ("M", 271, 280), "M11": ("M", 289, 293), "M12": ("M", 301, 304),
    "M13": ("M", 315, 322), "M14": ("M", 329, 331), "M15": ("M", 342, 350), "M16": ("M", 361, 365),
    "M17": ("M", 373, 376), "M18": ("M", 384, 385), "M20": ("M", 407, 409),
    "T01": ("T", 90, 94), "T02": ("T", 111, 122), "T03": ("T", 133, 138), "T04": ("T", 146, 149),
    "T05": ("T", 159, 165), "T06": ("T", 175, 180), "T07": ("T", 190, 194), "T08": ("T", 204, 208),
    "T09": ("T", 218, 224), "T10": ("T", 232, 234), "T11": ("T", 241, 242), "T12": ("T", 254, 258),
    "T13": ("T", 265, 267), "T14": ("T", 277, 279), "T15": ("T", 286, 288), "T16": ("T", 295, 297),
    "T17": ("T", 307, 312), "T18": ("T", 319, 322), "T19": ("T", 332, 337), "T20": ("T", 347, 351),
    "T21": ("T", 359, 360), "T22": ("T", 366, 380),
}


def lire_verifie(chemin, empreinte):
    octets = chemin.read_bytes()
    vue = hashlib.sha256(octets).hexdigest()
    if vue != empreinte:
        raise SystemExit(f"empreinte autre pour {chemin} : {vue}")
    return octets.decode("utf-8").split("\n")


def main():
    gabarit, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    montrer = "--montrer" in sys.argv
    lignes = {cle: lire_verifie(*val) for cle, val in RAPPORTS.items()}
    texte = gabarit.read_text(encoding="utf-8")
    for repere, (rap, debut, fin) in PLAGES.items():
        bloc = lignes[rap][debut - 1:fin]
        if not bloc or any("```" in l for l in bloc):
            raise SystemExit(f"bloc vide ou clôture de code dans {repere}")
        marque = f"@@{repere}@@"
        if texte.count(marque) != 1:
            raise SystemExit(f"repère {marque} présent {texte.count(marque)} fois")
        texte = texte.replace(marque, "\n".join(bloc))
        if montrer:
            print(f"{repere} l.{debut} : {bloc[0][:110]}")
            print(f"{repere} l.{fin} : {bloc[-1][:110]}")
    restants = re.findall(r"@@[A-Z0-9]+@@", texte)
    if restants:
        raise SystemExit(f"repères restants : {restants}")
    sortie.write_text(texte, encoding="utf-8")
    empreinte = hashlib.sha256(sortie.read_bytes()).hexdigest()
    (sortie.parent / (sortie.name + ".sha256")).write_text(f"{empreinte}  {sortie.name}\n", encoding="utf-8")
    print(empreinte, sortie.name)


if __name__ == "__main__":
    main()
