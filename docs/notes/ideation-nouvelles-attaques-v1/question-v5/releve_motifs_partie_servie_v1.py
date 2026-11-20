#!/usr/bin/env python3
"""Relevé des motifs internes sur les § 2 à § 7 d'une question — v1 (bibliothèque standard seulement).

Usage : python3 -B releve_motifs_partie_servie_v1.py QUESTION.md SORTIE.txt

La zone relevée va de la ligne qui commence par « ## 2. » à la fin du fichier. Elle doit porter les titres « ## 2. » à
« ## 7. », chacun une fois, dans l'ordre. Témoin : les mêmes motifs sont comptés sur l'en-tête et le § 1 (tout ce qui
précède « ## 2. »), où ils sont attendus non nuls ; un témoin à zéro signale un relevé aveugle.
Code de sortie : 0 si le total de la zone est 0 et le témoin non nul ; 1 sinon ; 2 si la forme du fichier est inattendue.
La sortie n'est jamais réécrite (création exclusive).
"""
import hashlib
import re
import sys
from pathlib import Path

MOTIFS = [
    ("prénom du directeur", re.compile(r"lazar", re.IGNORECASE)),
    ("nom du directeur", re.compile(r"[cć]iri[cć]", re.IGNORECASE)),
    ("session_", re.compile(r"session_")),
    ("@", re.compile(r"@")),
    ("R- suivi de chiffres", re.compile(r"(?<![A-Za-z])R-[0-9]")),
    ("N- suivi de chiffres", re.compile(r"(?<![A-Za-z])N-[0-9]")),
    ("GO-20", re.compile(r"GO-20")),
    ("lciric", re.compile(r"lciric", re.IGNORECASE)),
    ("github", re.compile(r"github", re.IGNORECASE)),
    ("controle-ia", re.compile(r"controle-ia", re.IGNORECASE)),
    ("docs/", re.compile(r"docs/")),
    ("prereg/", re.compile(r"prereg/")),
    ("registres/", re.compile(r"registres/")),
    ("donnees/", re.compile(r"donnees/")),
    ("hexadécimal de 16 caractères et plus", re.compile(r"[0-9a-fA-F]{16,}")),
    ("CLAUDE.md", re.compile(r"CLAUDE\.md")),
    ("nom de clé en _KEY", re.compile(r"_KEY")),
    ("nom de clé en _TOKEN", re.compile(r"_TOKEN")),
]


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    octets = Path(argv[1]).read_bytes()
    texte = octets.decode("utf-8", errors="strict")
    lignes = texte.split("\n")
    titres = [(i, l) for i, l in enumerate(lignes) if l.startswith("## ")]
    numeros = [l[3:5] for _, l in titres]
    if numeros != ["1.", "2.", "3.", "4.", "5.", "6.", "7."]:
        print(f"FORME INATTENDUE : titres de niveau 2 trouvés : {numeros}", file=sys.stderr)
        return 2
    debut = titres[1][0]
    zone = "\n".join(lignes[debut:])
    temoin = "\n".join(lignes[:debut])
    out = []
    out.append("Relevé des motifs internes — partie qui peut être servie (§ 2 à § 7)")
    out.append(f"fichier : {Path(argv[1]).name}")
    out.append(f"sha256 du fichier : {hashlib.sha256(octets).hexdigest()}")
    out.append(f"zone : lignes {debut + 1} à {len(lignes)} (de « {lignes[debut]} » à la fin), "
               f"{len(zone.encode('utf-8'))} octets")
    out.append(f"témoin : lignes 1 à {debut} (en-tête et § 1), {len(temoin.encode('utf-8'))} octets")
    out.append("")
    out.append("motif | occurrences dans la zone | occurrences dans le témoin")
    total_zone, total_temoin = 0, 0
    for nom, rx in MOTIFS:
        nz, nt = len(rx.findall(zone)), len(rx.findall(temoin))
        total_zone += nz
        total_temoin += nt
        out.append(f"{nom} | {nz} | {nt}")
        if nz:
            for i, l in enumerate(lignes[debut:], debut + 1):
                if rx.search(l):
                    out.append(f"    ligne {i}")
    out.append("")
    out.append(f"TOTAL zone : {total_zone} (0 attendu)")
    out.append(f"TOTAL témoin : {total_temoin} (non nul attendu)")
    verdict = "CONFORME" if total_zone == 0 and total_temoin > 0 else "NON CONFORME"
    out.append(f"VERDICT : {verdict}")
    corps = "\n".join(out) + "\n"
    with open(argv[2], "x", encoding="utf-8") as f:
        f.write(corps)
    sys.stdout.write(corps)
    return 0 if verdict == "CONFORME" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
