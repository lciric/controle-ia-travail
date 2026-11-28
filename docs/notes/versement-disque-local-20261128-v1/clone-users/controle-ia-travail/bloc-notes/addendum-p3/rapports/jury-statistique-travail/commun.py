"""Chargement des trois candidats sous des noms distincts (aucune écriture hors du dossier du juge)."""
import importlib.util, sys
sys.dont_write_bytecode = True
BASE = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3"
W = BASE + "/rapports/jury-statistique-travail"
sys.path.insert(0, "/home/user/controle-ia-travail/tests")

def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m

A = charger("cand_a", BASE + "/candidat-a/complements_p3_v1.py")
B = charger("cand_b", BASE + "/candidat-b/complements_p3_v1.py")
GE = charger("cand_gemini", W + "/gemini_copie/noyau_gemini_corrige_indentation.py")
