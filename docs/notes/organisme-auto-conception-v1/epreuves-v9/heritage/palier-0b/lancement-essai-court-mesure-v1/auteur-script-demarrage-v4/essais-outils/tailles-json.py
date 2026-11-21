"""Tailles d'un texte de données de démarrage selon plusieurs lectures de la limite « 32KiB » du champ user_data
(voie indépendante du calcul du fabricant, qui est en bash). Le jeton de la ligne 3 est d'abord remplacé par un jeton
de LONGUEUR signes (le plus long admis).

Lectures : (a) octets UTF-8 du texte ; (b) chaîne JSON UTF-8 (json.dumps, ensure_ascii=False), guillemets compris ;
(c) chaîne JSON échappée en ASCII (json.dumps, ensure_ascii=True), guillemets compris ; (d) comme (c), plus l'échappement
HTML de Go (<, >, & en \\u003c…) ; (e) comme (d), plus « / » échappé en « \\/ ». Marges sous 32 768.

Emploi : python tailles-json.py FICHIER LONGUEUR
"""
import json
import sys

texte = open(sys.argv[1], encoding="utf-8").read()
n = int(sys.argv[2])
lignes = texte.split("\n")
assert lignes[2].startswith("JETON_DEMARRAGE='"), lignes[2][:20]
lignes[2] = "JETON_DEMARRAGE='" + "J" * n + "'"
t = "\n".join(lignes)
a = len(t.encode("utf-8"))
b = len(json.dumps(t, ensure_ascii=False).encode("utf-8"))
c = len(json.dumps(t, ensure_ascii=True))
d = c + 5 * sum(t.count(x) for x in "<>&")
e = d + t.count("/")
for nom, v in (("a octets", a), ("b JSON UTF-8", b), ("c JSON ASCII", c), ("d JSON ASCII + HTML de Go", d),
               ("e JSON ASCII + HTML + barres", e)):
    print(f"{nom} : {v} ; marge {32768 - v}")
print(f"signes hors ASCII : {sum(1 for ch in t if ord(ch) > 127)} ; jeton de {n} signes")
