"""Applique les remplacements déclarés (fichier précédent -> fichier neuf) ; chaque « ancien » doit figurer le nombre de fois
exigé. Usage : python appliquer_v4.py DEPOT SORTIE NOM... (NOM parmi les clés de COUPLES)."""
import sys
from pathlib import Path

PREC = {
    "src/controle_ia/t07bbis/marche_v4.py": "src/controle_ia/t07bbis/marche_v3.py",
    "src/controle_ia/t07bbis/lecture_v3.py": "src/controle_ia/t07bbis/lecture_v2.py",
    "src/controle_ia/t07bbis/registre_bbis_v2.py": "src/controle_ia/t07bbis/registre_bbis_v1.py",
    "scripts/lancer_bbis_v4.sh": "scripts/lancer_bbis_v3.sh",
    "scripts/amorce_bbis_v4.sh": "scripts/amorce_bbis_v3.sh",
}


def appliquer(texte, couples):
    for ancien, nouveau, n in couples:
        assert texte.count(ancien) == n, (ancien[:90], texte.count(ancien), n)
        texte = texte.replace(ancien, nouveau)
    return texte


def main():
    depot, sortie, couples_py = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    ns = {}
    exec(couples_py.read_text(encoding="utf-8"), ns)
    for nom in sys.argv[4:]:
        t = (depot / PREC[nom]).read_text(encoding="utf-8")
        neuf = appliquer(t, ns["COUPLES"][nom])
        (sortie / nom).write_text(neuf, encoding="utf-8")
        print("écrit", nom)


main()
