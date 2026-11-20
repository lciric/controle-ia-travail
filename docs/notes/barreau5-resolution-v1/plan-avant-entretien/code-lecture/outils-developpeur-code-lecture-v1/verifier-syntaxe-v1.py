"""Compile, sans rien écrire, les fichiers donnés avec l'interpréteur qui joue ce script (ici Python 3.11, celui de l'image
des instances) : refus de toute syntaxe propre à une version plus récente (par exemple, guillemets semblables imbriqués dans
une f-chaîne). Usage : python3.11 -B verifier-syntaxe-v1.py FICHIER…"""
import sys

erreurs = 0
for chemin in sys.argv[1:]:
    with open(chemin, encoding="utf-8") as f:
        source = f.read()
    try:
        compile(source, chemin, "exec")
        print(f"OK {sys.version.split()[0]} {chemin}")
    except SyntaxError as e:
        erreurs += 1
        print(f"ERREUR {chemin}:{e.lineno}: {e.msg}")
sys.exit(1 if erreurs else 0)
