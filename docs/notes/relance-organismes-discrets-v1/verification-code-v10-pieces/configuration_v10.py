"""Question 2 : les rédactions retirées sont-elles refusées à la LECTURE de la configuration scellée ?"""
import sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v10 as A
from controle_ia.organismes_discrets import configuration_bras_a_v10 as cf, analyse_bras_a_v10 as an
from controle_ia.gardes import GardeArret
T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try: print("PASSE  ", nom, "->", f())
    except GardeArret as e: print("GARDE  ", nom, "->", str(e)[:140])
for nom, val in ((cf.CHOIX_SCHEMA, cf.SCHEMA_LIBRE), (cf.CHOIX_SEUIL, cf.SEUIL_SUR_LES_CALCULES), (cf.CHOIX_INTERVALLE_IMPOSSIBLE, cf.INTERVALLE_INDECIS_D_OFFICE),
                 (cf.CHOIX_NON_AJUSTABLE, cf.NON_AJUSTABLE_ANOMALIE), (cf.CHOIX_ISSUE, cf.ISSUE_LIGNE_D_ARRET_DE_LA_COURSE), (cf.CHOIX_ISSUE, cf.ISSUE_DISCRETION_NON_LUE),
                 (cf.CHOIX_INTERVALLE_IMPOSSIBLE, cf.INTERVALLE_ANOMALIE), (cf.CHOIX_NON_AJUSTABLE, cf.NON_AJUSTABLE_MODULE_CORRIGE),
                 (cf.CHOIX_NON_AJUSTABLE, cf.NON_AJUSTABLE_EN_ATTENTE), (cf.CHOIX_SCHEMA, "echange dans chaque paire "), (cf.CHOIX_ISSUE, None)):
    essai(f"lecture d'une configuration « {nom} = {val!r} »", lambda: cf.lire_la_configuration_scellee(A.fichier_de_configuration(T, choix={nom: val}))["choix"][nom])
c = A.configuration(); del c["choix"][cf.CHOIX_SEUIL]
essai("lecture d'une configuration sans le choix du seuil", lambda: cf.lire_la_configuration_scellee(A.ecrire_scelle(A.nouvelle_course(T) / "livraison-1" / cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION, c))["choix"])
c = A.configuration(); c["chaines_du_module"][cf.CHAINE_DE_LA_CLE_DU_MODULE] = None
essai("clé de provenance nulle", lambda: cf.lire_la_configuration_scellee(A.ecrire_scelle(A.nouvelle_course(T) / "livraison-1" / cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION, c))["choix"])
print("gabarit = mot de Lazar :", cf.CHOIX_DU_MOT_DE_LAZAR_DU_19_NOVEMBRE_2026)
import inspect
src = "".join(inspect.getsource(m) for m in (an, cf))
print("le gabarit est-il lu ailleurs que dans sa définition et `contenu_de_la_configuration` ?",
      [l.strip()[:90] for l in src.splitlines() if "CHOIX_DU_MOT_DE_LAZAR" in l and not l.strip().startswith("#")])
