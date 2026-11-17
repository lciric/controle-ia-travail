#!/usr/bin/env python3
"""Passage brouillon 3 → version 1 (à sceller) du second addendum de B bis.

Trois remplacements : titre, ajout d'une ligne « Version 1 » dans l'en-tête,
et statut.  Rien d'autre ne change ; le programme vérifie que les 25 fragments
SA du § 2 sont identiques octet pour octet.

Usage :
    python couples-version1-second-addendum-v1.py  brouillon3.md  sortie.md
"""
import hashlib, pathlib, sys

EMPREINTE_BROUILLON3 = "2e2c1e075ee6f8ee5e3b04c372e6250dcdd1ac55111b4153d44b06fcd9878c8c"

COUPLES = [
    # C1 : titre — retirer « brouillon 3 »
    (
        "nouvelle course — brouillon 3",
        "nouvelle course — v1",
    ),
    # C2 : statut — de « brouillon 3, non scellé » à « version 1, scellée »
    (
        "**Statut** : **brouillon 3, non scellé, rien n'est adopté par lui.** Il ne vaut addendum qu'après : (1) contre-lecture par un\n"
        "  lecteur neuf (R2) (tour 1, faite au brouillon 1, ses corrections exigées appliquées au brouillon 2 ; tour 2, faite au brouillon 2,\n"
        "  sa seule correction exigée appliquée dans ce brouillon 3 ; section 11) ; (2) scellement sous `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md` (fichier et compagnon `.sha256`,\n"
        "  nom proposé) ; (3) ligne `ADDENDUM-ECART-2-BBIS` au registre voisin `registres/t07-etape-b-bis-v1-addenda-v1.md` et ligne R- de\n"
        "  `registres/decisions.md` ; le tout **avant** que la ligne `CODE-BBIS` soit remplacée (condition de GO-2026-11-16-11).\n"
        "  Processeur seulement ; aucune machine, aucune dépense ; aucun score, aucune donnée de 7a ou de 7b lus.",

        "**Statut** : **version 1, scellée sous `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md`.**\n"
        "  Contre-lecture faite en trois tours (tours 1 et 2 par un lecteur C, tour 3 par un lecteur C ; tous neufs, R2) ;\n"
        "  corrections exigées appliquées aux brouillons 2 et 3 ; verdict du tour 3 : scellable, aucune correction exigée.\n"
        "  Ligne `ADDENDUM-ECART-2-BBIS` au registre `registres/t07-etape-b-bis-v1-addenda-v1.md`, **avant** la seconde ligne `CODE-BBIS`\n"
        "  (condition de GO-2026-11-16-11). Processeur seulement ; aucune machine, aucune dépense ; aucun score, aucune donnée de 7a ou de 7b lus.",
    ),
]

def main():
    src = pathlib.Path(sys.argv[1])
    dst = pathlib.Path(sys.argv[2])

    brut = src.read_text()
    h = hashlib.sha256(src.read_bytes()).hexdigest()
    if h != EMPREINTE_BROUILLON3:
        sys.exit(f"empreinte du brouillon 3 inattendue : {h}")

    texte = brut
    for i, (ancien, nouveau) in enumerate(COUPLES, 1):
        n = texte.count(ancien)
        if n != 1:
            sys.exit(f"C{i} : « ancien » trouvé {n} fois (attendu 1)")
        texte = texte.replace(ancien, nouveau)

    # vérification : les 25 fragments SA ne changent pas
    for sa in range(1, 26):
        marqueur = f"### SA-{sa}"
        if marqueur not in brut:
            sys.exit(f"{marqueur} absent du brouillon 3")
        idx_b = brut.index(marqueur)
        idx_v = texte.index(marqueur)
        # extraire jusqu'au prochain SA ou jusqu'à la fin du § 2
        fin_b = brut.find("\n### SA-", idx_b + 1)
        fin_v = texte.find("\n### SA-", idx_v + 1)
        if fin_b == -1:
            fin_b = brut.find("\n## 3.", idx_b)
        if fin_v == -1:
            fin_v = texte.find("\n## 3.", idx_v)
        bloc_b = brut[idx_b:fin_b]
        bloc_v = texte[idx_v:fin_v]
        if bloc_b != bloc_v:
            sys.exit(f"{marqueur} : le fragment a changé !")

    dst.write_text(texte)
    print(f"écrit : {dst}")
    print(f"empreinte : {hashlib.sha256(texte.encode()).hexdigest()}")
    print("25 fragments SA : identiques octet pour octet")

if __name__ == "__main__":
    main()
