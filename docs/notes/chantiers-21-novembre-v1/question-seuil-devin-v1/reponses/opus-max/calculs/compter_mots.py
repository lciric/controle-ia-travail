import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
# jetons séparés par les blancs ordinaires seulement (l'espace insécable joint)
jetons = re.split(r"[ \t\n\r]+", t)
mots = [j for j in jetons if re.search(r"[0-9A-Za-zÀ-ÿŒœ]", j)]
print("jetons avec lettre ou chiffre :", len(mots))
# sans le bloc d'empreintes
corps = t.split("## Empreintes des calculs")[0]
jetons = re.split(r"[ \t\n\r]+", corps)
print("corps sans empreintes :", len([j for j in jetons if re.search(r"[0-9A-Za-zÀ-ÿŒœ]", j)]))
