"""Écrit tests/echecs-connus-v2.txt : en-tête adapté, 4 lignes de la v1 recopiées octet pour octet, 10 lignes du v11."""
import sys
from pathlib import Path

arbre = Path(sys.argv[1])
v1 = (arbre / "tests/echecs-connus-v1.txt").read_text(encoding="utf-8").splitlines(keepends=True)
lignes_v1 = [l for l in v1 if l.strip() and not l.startswith("#")]
assert len(lignes_v1) == 4, lignes_v1

ENTETE = """# Liste des échecs connus de la suite d'essais — v2
#
# Lue par tests/greffon_echecs_connus_v2.py (chargé par une ligne de tests/conftest.py) ; seule liste lue par ce greffon.
# Remplace pour la suite la v1 (tests/echecs-connus-v1.txt, gardée intacte) : ses 4 lignes sont recopiées ici à l'identique.
# Chaque essai listé est marqué « échec attendu » strict : s'il se met à passer, la suite échoue et le dit.
# Une ligne qui ne correspond à aucun essai collecté de son fichier, dont le fichier n'existe pas, ou dont le fichier
# est joué mais sauté en bloc (aucun essai collecté), refuse la suite. L'option --runxfail est refusée.
# Aucun motif par expression : identifiants complets et exacts seulement (chemin depuis la racine du dépôt, « :: », nom de l'essai,
# paramètres compris entre crochets s'il y en a).
#
# Format : une ligne par essai, trois champs séparés par une tabulation :
#   identifiant complet de l'essai <TAB> motif en une phrase <TAB> référence de la décision
# Les lignes vides et celles qui commencent par « # » sont ignorées.
# Liste scellée (compagnon .sha256, vérifié par le greffon) ; une nouvelle version prend un nouveau nom (R12).
"""

V11 = """test_artefact_autre_lien_vers_le_meme_interprete
test_artefact_autre_programme_non_epingle
test_artefact_commande_sans_programme
test_artefact_script_non_epingle
test_cas_sain_cible_resolue_de_l_interprete
test_cas_sain_interprete_lien_hors_usr
test_cas_sain_interprete_reel
test_essai_a_blanc_eteint_v11
test_mutation_filtre_v10_remis_attrape
test_v10_refuse_le_meme_cas""".split()
MOTIF = "pièces de l'organisme absentes de main"
REF = "décision de la mère du 22 novembre 2026, R-4755"
lignes_v11 = [f"tests/test_lancer_course_auto_conception_v11.py::{n}\t{MOTIF}\t{REF}\n" for n in V11]

sortie = arbre / "tests/echecs-connus-v2.txt"
assert not sortie.exists(), "R12 : on n'écrase jamais"
sortie.write_text(ENTETE + "".join(lignes_v1) + "".join(lignes_v11), encoding="utf-8")
print(f"{sortie} : {len(lignes_v1)} + {len(lignes_v11)} lignes")
