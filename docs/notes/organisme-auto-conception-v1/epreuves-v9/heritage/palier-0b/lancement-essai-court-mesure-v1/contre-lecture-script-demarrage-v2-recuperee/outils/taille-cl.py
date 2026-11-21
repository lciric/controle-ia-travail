"""Mesure CL des tailles d'un texte de donnees de demarrage, par une voie independante de celle de l'auteur.
Emploi : python -I taille-cl.py FICHIER LONGUEUR_JETON
Le jeton de la ligne 3 est remplace par LONGUEUR_JETON signes 'J'. Trois voies de comptage de la chaine JSON ASCII :
(1) json.dumps ; (2) comptage manuel octet par octet ; (3) comptage par encodage de chaque signe (unicode_escape).
"""
import json
import sys

octets = open(sys.argv[1], "rb").read()
n = int(sys.argv[2])
lignes = octets.split(b"\n")
assert lignes[2].startswith(b"JETON_DEMARRAGE='"), lignes[2][:20]
lignes[2] = b"JETON_DEMARRAGE='" + b"J" * n + b"'"
t = b"\n".join(lignes)

brut = len(t)
# voie 2 : manuel
manuel = 2  # guillemets
inconnus = 0
for b in t:
    if b in b'"\\\n\t':
        manuel += 2
    elif 0x20 <= b <= 0x7E:
        manuel += 1
    else:
        inconnus += 1
        manuel += 6 if b < 0x80 else 0
# voie 1 : json.dumps
txt = t.decode("utf-8")
v1 = len(json.dumps(txt, ensure_ascii=True))
# voie 3 : chaque signe encode seul
v3 = 2
for ch in txt:
    s = json.dumps(ch, ensure_ascii=True)
    v3 += len(s) - 2
html = sum(txt.count(x) for x in "<>&")
barres = txt.count("/")
print(f"jeton de {n} signes")
print(f"octets bruts : {brut} ; marge {32768 - brut}")
print(f"JSON ASCII voie 1 (json.dumps) : {v1} ; marge {32768 - v1}")
print(f"JSON ASCII voie 2 (manuel) : {manuel} ; marge {32768 - manuel} ; signes hors 0x20-0x7E et hors \\n \\t \\\" \\\\ : {inconnus}")
print(f"JSON ASCII voie 3 (signe par signe) : {v3} ; marge {32768 - v3}")
print(f"signes < > & : {html} ; JSON ASCII + HTML de Go : {v1 + 5 * html} ; marge {32768 - v1 - 5 * html}")
print(f"signes / : {barres} ; avec / echappe en plus : {v1 + 5 * html + barres} ; marge {32768 - v1 - 5 * html - barres}")
NL, TAB, GUIL, BS, CR, DEL = (bytes([c]) for c in (10, 9, 34, 92, 13, 127))
print(f"sauts de ligne : {t.count(NL)} ; tabulations : {t.count(TAB)} ; guillemets : {t.count(GUIL)} ; barres inverses : {t.count(BS)} ; retours chariot : {t.count(CR)} ; DEL : {t.count(DEL)}")
print(f"corps minimal {{\"user_data\":...}} : {v1 + 14} ; avec autres champs de 300 octets : {v1 + 14 + 300}")
