"""Écarts de la v8 au brouillon 29 : égalité de la famille sur les fractions ; piece_source."""
import json, sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v8 as A
from controle_ia.organismes_discrets import analyse_bras_a_v8 as an, arrets_bras_a_v8 as ar, configuration_bras_a_v8 as cf
from controle_ia.gardes import GardeArret
T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try: print("PASSE  ", nom, "->", f())
    except ar.ArretDeLaLectureDeLaDiscretion as e: print("ARRET  ", nom, "->", e.constat())
    except GardeArret as e: print("GARDE  ", nom, "->", str(e)[:120])
e = A.cas_a("juge", 1.0, egales=99)           # 100/2001 = 0.049975…
s = json.dumps(A.sortie({("juge", 1.0): e}))
v = json.dumps(e["valeur_p_haut"])
t = s.replace(f'"valeur_p_haut": {v}', '"valeur_p_haut": 0.04997501249375312', 1).replace(f'"valeur_p_pour_la_famille": {v}', '"valeur_p_pour_la_famille": 0.049975012493753120', 1)
c = A.fichier_de_configuration(T); A.constat(T, c)
essai("famille = valeur p haute, même fraction, écriture différente (zéro final)", lambda: an.regle_de_discretion(A.piece(T, t), c, go_de_la_reprise=None, registre_fige=None)["etats"][1.0]["juge"])
s2 = A.sortie(); s2["piece_source"] = {"module": "d" * 64}
c2 = A.fichier_de_configuration(T, cle_du_module_dans_piece_source="module"); A.constat(T, c2)
essai("piece_source qui porte un autre module", lambda: an.regle_de_discretion(A.piece(T, s2), c2, go_de_la_reprise=None, registre_fige=None))
