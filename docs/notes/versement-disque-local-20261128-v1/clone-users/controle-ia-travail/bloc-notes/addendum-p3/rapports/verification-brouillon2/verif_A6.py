"""A6 du brouillon 2 : expression _MILLIERS_ESPACE_V2 recopiée du brouillon (octets compris), appliquée comme
conditions.cout_groupes_joints ; cas cités par le brouillon, plus l'espace fine U+2009."""
import re, sys
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.environnements.propositions import _NOMBRE, heures_declarees
from controle_ia.premier_test_ia.conditions import cout_groupes_joints
ligne = open(sys.argv[1], encoding="utf-8").read().splitlines()[146]
expr = re.search(r"_MILLIERS_ESPACE_V2 = (.+?)`", ligne).group(1)
V2 = re.compile(expr)
def lecteur(champ):
    if not champ:
        return None
    m, n = V2.search(champ), _NOMBRE.search(champ)
    if m is not None and n is not None and m.start() <= n.start():
        k = re.match(r"\s*[kK](?![A-Za-z])", champ[m.end():])
        v = float(re.sub(r"[    ]", "", m.group(0)))
        return v * 1000 if k else v
    return heures_declarees(champ)
print("points de code de la classe :", [hex(ord(c)) for c in re.search(r"\[(.*?)\]", expr.split("(?:")[1]).group(1)])
for c in ["1 000 GPU-hours", "1 000 hours", "1 000 hours", "1 000 hours", "1 000.5 hours", "1,000 hours",
          "3 500-hour blocks", "2 500k", "about 40 hours"]:
    print(f"{c!r:22s} gelé={heures_declarees(c)!s:10s} joints={cout_groupes_joints(c)!s:10s} V2={lecteur(c)}")
