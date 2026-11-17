"""Écrit tests/aide_t07bbis_differentiels_v4.py depuis les programmes de couples (mêmes couples que ceux qui ont produit les
fichiers neufs)."""
import sys, pprint
from pathlib import Path
S = Path(sys.argv[1]); sortie = Path(sys.argv[2]); mini = int(sys.argv[3])
exec((S / "appliquer_v4.py").read_text(encoding="utf-8").split("def main")[0])
tout = {}
for f in ("couples_marche.py", "couples_lecture.py", "couples_registre.py", "couples_scripts.py"):
    ns = {}
    exec((S / f).read_text(encoding="utf-8"), ns)
    for neuf, cs in ns["COUPLES"].items():
        cs = [(a, b.replace("@MIN@", str(mini)), n) for a, b, n in cs]
        tout[neuf] = (PREC[neuf], cs)
entete = ('"""Différentiels déclarés des fichiers neufs du second addendum de B bis (marche v4, lecture v3, registre v2, lanceur et\n'
          'amorce v4) : pour chaque fichier neuf, (fichier précédent, couples « ancien, nouveau, nombre d\'occurrences exigé »). Ce\n'
          'sont les couples mêmes qui ont produit les fichiers neufs (programme de la rédaction) ; les essais refont chaque fichier neuf\n'
          'depuis le précédent et exigent l\'égalité exacte : aucun autre changement n\'existe. `validation_imbriquee_v4` est un module\n'
          'neuf (il importe la v3) : son différentiel avec la proposition du diagnostic est écrit dans `diff-v3-v4.txt`."""\n\n')
corps = f"MIN_ESSAIS_V4 = {mini}\n\n\ndef appliquer(texte: str, couples) -> str:\n    for ancien, nouveau, n in couples:\n        assert texte.count(ancien) == n, (ancien[:70], texte.count(ancien), n)\n        texte = texte.replace(ancien, nouveau)\n    return texte\n\n\nCOUPLES = " + pprint.pformat(tout, width=130) + "\n"
sortie.write_text(entete + corps, encoding="utf-8")
print("écrit", sortie, len(tout))
