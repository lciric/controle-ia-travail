"""A.1 : configuration inscrite puis abandonnée ; ce qui débloque le constat de la suivante."""
import sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v11 as A
from controle_ia.organismes_discrets import graines_bras_a_v11 as g
from controle_ia.gardes import GardeArret
T = Path(tempfile.mkdtemp())
c_ab = A.fichier_de_configuration(A.nouvelle_course(T), rang=1)
c_ok = A.fichier_de_configuration(A.nouvelle_course(T), rang=1, statistique_agregateur="autre (essai)")
assert A.empreinte(c_ab) != A.empreinte(c_ok)
ins_ab = A.ligne_d_inscription(c_ab, go="GO-2099-12-30-01")
P = g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE
for nom, plus in (("inscription abandonnée seule", [ins_ab]),
                  ("+ ligne de reprise quelconque après", [ins_ab, f"| GO-2099-12-30-02 | 2099 | décision | {P} |"]),
                  ("+ ligne de reprise quelconque AVANT l'inscription abandonnée", [f"| GO-2099-12-30-02 | 2099 | décision | {P} |", ins_ab]),
                  ("+ ligne qui retire l'inscription abandonnée", [ins_ab, f"| GO-2099-12-30-03 | 2099 | révocation | {A.empreinte(c_ab)} retirée |"])):
    try:
        cst, chemin, causes = A.constat_et_causes(T, c_ok, lignes_de_plus=plus)
        print(f"{nom} : sain={chemin is not None} | causes={causes}")
    except GardeArret as e:
        print(f"{nom} : ARRÊT — {str(e)[:220]}")
