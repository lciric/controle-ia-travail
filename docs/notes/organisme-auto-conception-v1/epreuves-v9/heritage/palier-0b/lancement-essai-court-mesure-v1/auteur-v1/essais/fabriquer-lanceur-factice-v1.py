"""Fabrique un lanceur factice à partir du vrai lanceur, en ne changeant que les cinq constantes de départ et la ligne de
commande (chacune trouvée exactement une fois) ; tout le reste (contrôles, piège, écriture du code) est gardé à l'octet.

Usage : fabriquer-lanceur-factice-v1.py VRAI_LANCEUR SORTIE RACINE TETE EMPREINTE PROGRAMME SORTIES COMMANDE
"""
import sys


def main(args):
    if len(args) != 8:
        print(__doc__)
        return 2
    vrai, sortie, racine, tete, empreinte, programme, sorties, commande = args
    with open(vrai, encoding="utf-8") as fh:
        lignes = fh.read().split("\n")
    remplacements = {"RACINE=/": f"RACINE={racine}", "TETE_ATTENDUE=": f"TETE_ATTENDUE={tete}",
                     "EMPREINTE_ATTENDUE=": f"EMPREINTE_ATTENDUE={empreinte}", "PROGRAMME=/": f"PROGRAMME={programme}",
                     "SORTIES=/": f"SORTIES={sorties}", "env -C ": commande}
    changees = 0
    for debut, nouvelle in remplacements.items():
        idx = [i for i, l in enumerate(lignes) if l.startswith(debut) and not l.startswith(debut + "$")]
        if len(idx) != 1:
            print(f"ÉCHEC : « {debut} » trouvé {len(idx)} fois")
            return 1
        print(f"ligne {idx[0] + 1} : « {lignes[idx[0]][:90]}… » → « {nouvelle[:90]}… »")
        lignes[idx[0]] = nouvelle
        changees += 1
    with open(sortie, "x", encoding="utf-8") as fh:
        fh.write("\n".join(lignes))
    print(f"{changees} lignes changées ; lanceur factice écrit : {sortie}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
