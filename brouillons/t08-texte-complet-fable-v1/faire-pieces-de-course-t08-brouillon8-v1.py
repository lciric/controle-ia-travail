#!/usr/bin/env python3
"""Écrit le brouillon 8 de l'ordre de course de la base boîte noire (T0.8) à partir du brouillon 7. Cause unique : le
majeur q-1 de la vérification du brouillon 6 — l'admission du fichier recomposé demande le mot de Lazar, et sa
condition est resserrée à l'empreinte que donne la sortie scellée. Chaque texte ancien est trouvé une fois ; rien
n'est écrasé (R12).
Usage, depuis la racine : python3 brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon8-v1.py
"""
import hashlib
import sys
from pathlib import Path

D = Path("docs/procedures/t08-course-v1")
ENTREE, SHA_E = "ordre-course-t08-v1-brouillon7.md", "eaec9c7ecf5535d9aa842b5041d19ba1654fafb2a40548046ac6918f796d653d"
SORTIE, JOURNAL = "ordre-course-t08-v1-brouillon8.md", "journal-pieces-de-course-t08-brouillon8-v1.md"
RAPPORT = ("`prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon6-verification-cl1.md` "
           "(`5e426cb19fbaab2a083fb283e14adda4d70547fb20397c4294ff4b163aaeee47`)")
OPS = [
    ("renvoi", "sur une machine louée — v1 — brouillon 7", "sur une machine louée — v1 — brouillon 8"),
    ("renvoi", "- **Statut** : **brouillon 7**, pièce de classe A, qui porte les commandes. Il ajoute au brouillon 6",
     "- **Statut** : **brouillon 8**, pièce de classe A, qui porte les commandes. Il applique au brouillon 7 (`" + SHA_E +
     "`) le majeur q-1 de la vérification du brouillon 6 (" + RAPPORT + ") : l'admission du fichier recomposé attend "
     "le mot de Lazar, et sa condition est resserrée (étape 9). **Tant que ce mot n'est pas inscrit, cette admission "
     "ne vaut pas.** Le brouillon 7 ajoutait au brouillon 6"),
    ("q-1",
     "**Admission du fichier recomposé** (décision de la session mère, R-5060 ; cette ligne est le texte contre-lu que "
     "veut la section 8) :",
     "**Admission du fichier recomposé** (recommandée par la session mère, R-5060 ; cette ligne est le texte contre-lu "
     "que veut la section 8, qui demande aussi le mot de Lazar : **elle ne vaut qu'une fois ce mot inscrit au "
     "registre, avant toute course, et cité ici par sa ligne** ; sans lui, le fichier versé n'entre dans aucune "
     "lecture, et une lecture qui en a besoin s'arrête sur une entrée manquante, ligne D1) :"),
    ("q-1",
     "son empreinte est égale à celle du fichier entier, calculée sur la machine avant le découpage, et chaque morceau "
     "a gardé la sienne ; s'il a un compagnon ou une empreinte consignée par la course, c'est la même.",
     "son empreinte est égale à celle que lui donne la sortie scellée de la course (`course-t08.json`, ou son "
     "compagnon scellé par la course), et à celle du fichier entier calculée sur la machine avant le découpage ; "
     "chaque morceau a gardé la sienne. Si la sortie scellée ne donne pas d'empreinte à ce fichier, il n'entre pas."),
]
o = (D / ENTREE).read_bytes()
if hashlib.sha256(o).hexdigest() != SHA_E or (D / SORTIE).exists() or (D / JOURNAL).exists():
    sys.exit("ARRET : empreinte d'entrée différente, ou sortie déjà là (R12)")
t = o.decode("utf-8")
for n, (c, a, b) in enumerate(OPS, 1):
    if t.count(a) != 1:
        sys.exit(f"ARRET : opération {n} ({c}) : texte ancien trouvé {t.count(a)} fois")
    t = t.replace(a, b)
(D / SORTIE).write_text(t, encoding="utf-8")
s = hashlib.sha256(t.encode("utf-8")).hexdigest()
(D / JOURNAL).write_text("# Journal — brouillon 8 de l'ordre de course (T0.8)\n\nÉcrit par "
                         "`brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon8-v1.py`. Quatre "
                         "opérations : titre, statut, et le majeur q-1 de " + RAPPORT + " en deux remplacements à "
                         "l'étape 9 (mot de Lazar exigé ; condition resserrée, au texte du rapport).\n\n"
                         f"Entrée : `{SHA_E}`. Sortie : `{s}`.\n\n**Reste** : la ligne du registre qui porte le mot de "
                         "Lazar, à citer dans l'ordre par un brouillon neuf ou un erratum, avant toute course.\n",
                         encoding="utf-8")
print(s)
