#!/usr/bin/env python3
"""Écrit le brouillon 7 de l'ordre de course de la base boîte noire (T0.8) à partir du brouillon 6. Cause unique : le
mineur p-1 de la vérification du brouillon 5 (forme de la ligne de course en fin sur anomalie de taille), demandé par
la session mère. Chaque texte ancien est trouvé une fois ; rien n'est écrasé (R12).
Usage, depuis la racine : python3 brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon7-v1.py
"""
import hashlib
import sys
from pathlib import Path

D = Path("docs/procedures/t08-course-v1")
ENTREE, SHA_E = "ordre-course-t08-v1-brouillon6.md", "06127b1810973100b22f01d8690fb062bbf4f69c2909d091e0bd3976026ad2dc"
SORTIE, JOURNAL = "ordre-course-t08-v1-brouillon7.md", "journal-pieces-de-course-t08-brouillon7-v1.md"
OPS = [
    ("renvoi", "sur une machine louée — v1 — brouillon 6", "sur une machine louée — v1 — brouillon 7"),
    ("renvoi", "- **Statut** : **brouillon 6**, pièce de classe A, qui porte les commandes. Il ajoute au brouillon 5",
     "- **Statut** : **brouillon 7**, pièce de classe A, qui porte les commandes. Il ajoute au brouillon 6 (`" + SHA_E +
     "`) le mineur p-1 de la vérification du brouillon 5 (étape 9 : ce que la ligne de course nomme en fin sur "
     "anomalie de taille). Le brouillon 6 ajoutait au brouillon 5"),
    ("renvoi", "la différence des brouillons 5 et 6 est à vérifier de même.",
     "le brouillon 5 l'a été aussi (`prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon5-verification-cl1.md`) ; "
     "la différence des brouillons 6 et 7 est à vérifier de même."),
    ("p-1", "alors seulement viennent la destruction par l'identifiant (étape 11) et la ligne `COURSE-T08`.",
     "alors seulement viennent la destruction par l'identifiant (étape 11) et la ligne `COURSE-T08` ; cette ligne, ou "
     "le journal de la session mère à côté d'elle, nomme la fin en anomalie de taille, la branche des morceaux et "
     "l'empreinte du fichier entier."),
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
(D / JOURNAL).write_text("# Journal — brouillon 7 de l'ordre de course (T0.8)\n\nÉcrit par "
                         "`brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon7-v1.py`. Quatre "
                         "opérations : titre, statut, ligne de contre-lecture, et le mineur p-1 à l'étape 9.\n\n"
                         f"Entrée : `{SHA_E}`. Sortie : `{s}`.\n", encoding="utf-8")
print(s)
