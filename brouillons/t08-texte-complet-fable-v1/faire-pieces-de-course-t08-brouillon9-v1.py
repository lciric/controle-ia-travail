#!/usr/bin/env python3
"""Écrit le brouillon 9 de l'ordre de course de la base boîte noire (T0.8) à partir du brouillon 8. Cause unique : le
mot de Lazar sur l'admission du fichier recomposé, inscrit en GO-2026-11-22-134 (`registres/go.md`), à citer.
Chaque texte ancien est trouvé une fois ; rien n'est écrasé (R12).
Usage, depuis la racine : python3 brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon9-v1.py
"""
import hashlib
import sys
from pathlib import Path

D = Path("docs/procedures/t08-course-v1")
ENTREE, SHA_E = "ordre-course-t08-v1-brouillon8.md", "82a07ecef4c0f62f45e913ca456f3f95281be88f52ffa3fe447c4eb5e22b9368"
SORTIE, JOURNAL = "ordre-course-t08-v1-brouillon9.md", "journal-pieces-de-course-t08-brouillon9-v1.md"
OPS = [
    ("renvoi", "sur une machine louée — v1 — brouillon 8", "sur une machine louée — v1 — brouillon 9"),
    ("mot de Lazar",
     "- **Statut** : **brouillon 8**, pièce de classe A, qui porte les commandes. Il applique au brouillon 7",
     "- **Statut** : **brouillon 9**, pièce de classe A, qui porte les commandes. Il cite, au brouillon 8 (`" + SHA_E +
     "`, vérifié conforme : `prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon8-verification-cl1.md`), le mot "
     "de Lazar sur l'admission du fichier recomposé (`GO-2026-11-22-134` ; étape 9). Le brouillon 8 appliquait au "
     "brouillon 7"),
    ("mot de Lazar",
     "**Tant que ce mot n'est pas inscrit, cette admission ne vaut pas.**",
     "Ce mot est inscrit : `GO-2026-11-22-134`."),
    ("mot de Lazar",
     "**elle ne vaut qu'une fois ce mot inscrit au registre, avant toute course, et cité ici par sa ligne** ; sans "
     "lui, le fichier versé n'entre dans aucune lecture, et une lecture qui en a besoin s'arrête sur une entrée "
     "manquante, ligne D1) :",
     "**ce mot est donné : « go oui », le 22 novembre, ligne `GO-2026-11-22-134` de `registres/go.md`, exception "
     "nommée à la règle « récupérer ce qui est récupérable » pour ce seul cas** ; hors de la condition qui suit, le "
     "fichier versé n'entre dans aucune lecture, et une lecture qui en a besoin s'arrête sur une entrée manquante, "
     "ligne D1) :"),
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
(D / JOURNAL).write_text("# Journal — brouillon 9 de l'ordre de course (T0.8)\n\nÉcrit par "
                         "`brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon9-v1.py`. Quatre "
                         "opérations : titre, statut (deux), et la citation du mot de Lazar à l'étape 9. Ligne "
                         "`GO-2026-11-22-134` relue par l'auteur sur `main` avant l'écriture.\n\n"
                         f"Entrée : `{SHA_E}`. Sortie : `{s}`.\n", encoding="utf-8")
print(s)
