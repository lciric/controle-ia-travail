"""Aide de travail : écrit `papier_c_schema_config_v1.py` (noms et types de tous les champs) depuis la configuration
construite par `ecrire_config_brouillon5_v1.construire`. Lancé une fois ; le fichier produit est ensuite un fichier
statique du module, gelé par son empreinte et relu à la main. Usage : python3 generer_schema_config_v1.py B4 SORTIE"""
import json, pprint, sys
sys.path.insert(0, sys.argv[3])
import ecrire_config_brouillon5_v1 as e
from papier_c_configuration_v1 import longueurs_mesurees
NULLABLES = {"controlabilite.concept", "controlabilite.consignes.pense", "controlabilite.consignes.ne_pense_pas",
             "controlabilite.banc.version", "controlabilite.banc.licence", "controlabilite.banc.sha256",
             "stabilite_rang.rapport_grille.chemin", "stabilite_rang.rapport_grille.sha256"}
FLOTTANTS = {"raisonne.temperature"}
def schema(v, chemin):
    if isinstance(v, dict):
        return {k: schema(x, f"{chemin}.{k}".lstrip(".")) for k, x in v.items()}
    if isinstance(v, list):
        if not v:
            return ["str"]
        s = [schema(x, chemin + "[]") for x in v]
        if all(isinstance(x, str) for x in s):
            return ["float" if "float" in s else s[0]] if set(s) <= {"int", "float"} else [s[0]]
        assert all(x == s[0] for x in s), chemin
        return [s[0]]
    if chemin in NULLABLES:
        return "str?"
    if isinstance(v, bool): return "bool"
    if isinstance(v, int): return "float" if chemin in FLOTTANTS else "int"
    if isinstance(v, float): return "float"
    if isinstance(v, str): return "str"
    raise SystemExit(f"type inattendu à {chemin}")
b4 = json.load(open(sys.argv[1], encoding="utf-8"))
b5 = e.construire(b4); b5["controle_redaction"] = longueurs_mesurees(b5)
s = schema(b5, "")
texte = ('"""Papier C — schéma de la configuration : nom et type de chaque champ (v1).\n\n'
         'Fichier statique du module, lu par `papier_c_configuration_v1`. Un champ absent d\'ici est « inconnu », un champ\n'
         'd\'ici absent de la configuration est « manquant » : les deux arrêtent (`ConfigurationInvalide`). Types : « str »,\n'
         '« int », « float » (un entier est admis), « bool » ; le suffixe « ? » admet la valeur vide (null), refusée en mode\n'
         '« scelle » pour les champs du bras « contrôlabilité » ; une liste donne le type de ses éléments.\n'
         'Écrit une fois à partir du brouillon 5 de la configuration, puis relu à la main ; toute évolution de la\n'
         'configuration demande une nouvelle version de ce fichier (R12).\n"""\n'
         "SCHEMA = " + pprint.pformat(s, width=118, sort_dicts=False) + "\n")
open(sys.argv[2], "w", encoding="utf-8").write(texte)
print("champs feuilles :", sum(1 for _ in __import__("papier_c_configuration_v1")._feuilles(s)))
