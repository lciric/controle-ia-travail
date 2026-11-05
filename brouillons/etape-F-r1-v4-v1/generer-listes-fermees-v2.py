"""Engendre `listes-fermees-generees-v2.md` depuis les modules neufs (code v8, v9, v5) : même forme que la v1 (blocs de
l'addendum, un par analyse : empreinte des constantes, titre gelé, paquet, essais, modules réutilisés ; « (neuf) » sur
les fichiers de cet addendum). Lancement, depuis la racine de l'arbre :
    PYTHONPATH=src python brouillons/etape-F-r1-v4-v1/generer-listes-fermees-v2.py > brouillons/etape-F-r1-v4-v1/listes-fermees-generees-v2.md
"""
from controle_ia.analyse_blanche_noire import constantes_v5 as C5
from controle_ia.analyse_blanche_noire import lecture_v3 as LB3
from controle_ia.analyse_blanche_noire import lecture_v5 as LB5
from controle_ia.analyse_principale_r1_r2 import constantes_v8 as K8
from controle_ia.analyse_principale_r1_r2 import constantes_v9 as K9
from controle_ia.analyse_principale_r1_r2 import lecture_v2 as L2
from controle_ia.analyse_principale_r1_r2 import lecture_v5 as L5
from controle_ia.analyse_principale_r1_r2 import lecture_v8 as L8
from controle_ia.analyse_principale_r1_r2 import lecture_v9 as L9
from controle_ia.scellement import empreinte

BLOCS = (("analyse principale, code v8", K8, L8, L2), ("analyse par épisode, code v9", K9, L9, L5),
         ("analyse secondaire, code v5", C5, LB5, LB3))
sortie = []
for nom, K, L, L_prec in BLOCS:
    anciens = set(L_prec.FICHIERS_PAQUET) | set(L_prec.FICHIERS_ESSAIS) | set(L_prec.FICHIERS_REUTILISES)
    sortie += [f"Empreinte des constantes ({nom}) : `{K.empreinte_constantes()}`", "", K.TITRE_LISTE, ""]
    for titre, fichiers in (("paquet", L.FICHIERS_PAQUET), ("essais", L.FICHIERS_ESSAIS),
                            ("modules gelés réutilisés sans modification", L.FICHIERS_REUTILISES)):
        sortie.append(f"- {titre} :")
        for c in fichiers:
            sortie.append(f"  - `{c}` : `{empreinte(c)}`" + ("" if c in anciens else "  (neuf)"))
    sortie.append("")
print("\n".join(sortie))
