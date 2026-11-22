"""DOUBLURE D'ESSAI du module `tirage_na_v4` (lot 2 v5), déclarée comme telle — ce n'est PAS le module du lot 2.

Seuls les noms que lisent `contrat_fiche_na_v1` et `registre_na_v1` : la racine écrite (factice), la forme de la ligne de
case, et une permutation déterministe tirée d'une empreinte (non celle de la clé 12 ou 13 du lot 2). Les essais du lot 5 v2
doivent être rejoués sur une copie où le lot 2 v5 est posé.
"""

import hashlib

RACINE_ECRITE = "racine-factice-de-la-doublure"
PREFIXE_LIGNE = "case : "
SEPARATEUR_LIGNE = " ; "


class TirageRefuse(RuntimeError):
    pass


def permutation_registre(generation, n, racine, racine_attendue):
    if racine != racine_attendue:
        raise TirageRefuse("racine autre que la racine attendue")
    if generation not in (2, 3) or type(n) is not int or n < 0:
        raise TirageRefuse("génération 2 ou 3, taille entière")
    ordre = list(range(n))
    graine = hashlib.sha256(f"{racine}|{generation}|{n}".encode("utf-8")).digest()
    for i in range(n - 1, 0, -1):
        graine = hashlib.sha256(graine).digest()
        j = int.from_bytes(graine[:8], "big") % (i + 1)
        ordre[i], ordre[j] = ordre[j], ordre[i]
    return ordre
