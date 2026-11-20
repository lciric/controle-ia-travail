# Outil d'écriture du rédacteur du brouillon 6 (bloc-notes ; n'est pas une pièce de fabrication).
# Il relève dans le brouillon 5 chaque texte « avant » par deux ancres (début, fin), vérifie que l'ancre de début est unique,
# et écrit le script des couples, où chaque texte « avant » et chaque texte « après » figure en toutes lettres.
# Usage : python -I fabrique.py BROUILLON5 SCRIPT_SORTIE MAIN ECRITURE FIN
import sys

import textes

source, sortie, MAIN, ECRITURE, FIN, INS, MAINDATE = sys.argv[1:8]
texte = open(source, encoding="utf-8").read()


def remplir(s):
    return (s.replace("@@MAIN@@", MAIN).replace("@@ECRITURE@@", ECRITURE).replace("@@FIN@@", FIN)
            .replace("@@CONTROLE_PIED@@", textes.CONTROLE_PIED).replace("@@CONTROLE@@", textes.CONTROLE)
            .replace("@@REFUS@@", textes.REFUS).replace("@@INS@@", INS).replace("@@MAINDATE@@", MAINDATE))


couples = []
for ident, sert, lieu, debut, fin, apres in textes.ENTREES:
    n = texte.count(debut)
    if n != 1:
        raise SystemExit(f"{ident} : ancre de début trouvée {n} fois")
    d = texte.index(debut)
    if fin is None:
        f = d + len(debut)
    else:
        k = texte.find(fin, d)
        if k < 0:
            raise SystemExit(f"{ident} : ancre de fin introuvable")
        f = k + len(fin)
    avant = texte[d:f]
    if texte.count(avant) != 1:
        raise SystemExit(f"{ident} : texte avant non unique")
    apres = remplir(remplir(apres)).replace("@@AVANT@@", avant)
    for s in (avant, apres, sert, lieu):
        if "'''" in s or s.endswith("'") or "\\" in s and False:
            raise SystemExit(f"{ident} : guillemets triples")
    couples.append((ident, sert, lieu, avant, apres))

corps = []
for ident, sert, lieu, avant, apres in couples:
    corps.append("    # " + "-" * 96 + "\n"
                 f"    ({ident!r}, {sert!r}, {lieu!r},\n"
                 f"r'''{avant}''',\n"
                 f"r'''{apres}'''),\n")
script = textes.TETE_SCRIPT + "COUPLES = [\n" + "".join(corps) + "]\n" + textes.PIED_SCRIPT
open(sortie, "w", encoding="utf-8").write(script)
print("couples :", len(couples))
