#!/usr/bin/env python3
"""Écrit le brouillon 5 de l'ordre de course de la base boîte noire (T0.8) à partir du brouillon 4, par opérations
déclarées. Causes : la décision de la session mère sur le mineur n-4 de la vérification du brouillon 4 (R-5059 de
`registres/decisions.md`), et les mineurs n-2 et n-3 de cette vérification. Chaque texte ancien est trouvé une fois ;
rien n'est écrasé (R12). Usage, depuis la racine : python3 brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon5-v1.py
"""
import hashlib
import sys
from pathlib import Path

D = Path("docs/procedures/t08-course-v1")
ENTREE, SHA_E = "ordre-course-t08-v1-brouillon4.md", "553be7d1ce6f0eb5090aa97e529f3d86189625122e60564516c773dc926e1d7d"
SORTIE, JOURNAL = "ordre-course-t08-v1-brouillon5.md", "journal-pieces-de-course-t08-brouillon5-v1.md"
VERIF4 = ("`prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon4-verification-cl1.md`")

OPS = [
    ("renvoi", "sur une machine louée — v1 — brouillon 4", "sur une machine louée — v1 — brouillon 5"),
    ("renvoi",
     "- **Statut** : **brouillon 4**, pièce de classe A : **le brouillon des commandes**. Il ajoute au brouillon 3",
     "- **Statut** : **brouillon 5**, pièce de classe A, qui porte les commandes. Il applique au brouillon 4 (`" + SHA_E +
     "`, vérifié conforme : " + VERIF4 + ") ses trois mineurs — n-4, tranché par la session mère (R-5059 de "
     "`registres/decisions.md` : étape 9) ; n-2 et n-3 (section 13, P7 et P2) ; opérations : "
     "`journal-pieces-de-course-t08-brouillon5-v1.md`. Le brouillon 4 ajoutait au brouillon 3"),
    ("renvoi", "la différence de ce brouillon 4 est à vérifier de même.",
     "le brouillon 4 l'a été aussi ; la différence de ce brouillon 5 est à vérifier de même."),
    ("n-4",
     "**Fin en anomalie de taille** (rapport de la chaîne, réserve 5 : un fichier de plus de 90 Mo est retiré du "
     "commit et reste sur la machine) : aucune destruction, aucune ligne `COURSE-T08` ; nœud pour la session mère, qui "
     "décide du versement (section 8).",
     "**Fin en anomalie de taille** (rapport de la chaîne, réserve 5 : un fichier de plus de 90 Mo est retiré du "
     "commit et reste sur la machine ; décision de la session mère, R-5059) : l'exécutante découpe ce fichier, sur la "
     "machine, en morceaux de moins de 90 Mo, relève l'empreinte de chaque morceau et celle du fichier entier, pousse "
     "les morceaux sur une branche dont le nom dit ce qu'elle est, sans rien ouvrir, et vérifie ces empreintes sur la "
     "branche ; alors seulement viennent la destruction par l'identifiant (étape 11) et la ligne `COURSE-T08`. Si le "
     "versement échoue, la machine reste arrêtée 24 heures au plus — son stockage, environ 2 USD par jour, compte dans "
     "le plafond cumulé — ; au-delà, nœud pour la session mère. Le fichier ainsi versé n'entre dans aucune lecture "
     "sans un texte contre-lu (section 8) : si la lecture en a besoin, elle s'arrête sur une entrée manquante (ligne "
     "D1) tant que ce texte n'existe pas."),
    ("n-3",
     "- **P2** : `grep '^| CODE-T08 ' registres/scellements-v1.md && git merge-base --is-ancestor $C origin/$BC`.",
     "- **P2** : `grep '^| CODE-T08 ' registres/scellements-v1.md && git merge-base --is-ancestor $C origin/$BC` ; "
     "puis les empreintes de l'arbre au commit `C` contre la pièce d'empreintes du code que cite le texte scellé : la "
     "session mère donne, avec `C`, le chemin de cette pièce et la commande qui la rejoue (code 0 exigé). Sans cette "
     "commande, P2 n'est pas tenu."),
    ("n-2",
     "- **P7** : `sha256sum",
     "- **P7** (ces deux commandes ne sont pas dans le § 8 du rapport : l'auteur de l'ordre les a composées d'après "
     "ses §§ 3 et 6 ; **à confirmer par le contre-lecteur de la chaîne de lancement**, sans quoi P7 n'est pas tenu) : "
     "`sha256sum"),
]


def sha(o: bytes) -> str:
    return hashlib.sha256(o).hexdigest()


def main() -> int:
    if (D / SORTIE).exists() or (D / JOURNAL).exists():
        print("ARRET : sortie déjà là (R12)", file=sys.stderr)
        return 2
    o = (D / ENTREE).read_bytes()
    if sha(o) != SHA_E:
        print("ARRET : empreinte du brouillon 4 différente", file=sys.stderr)
        return 2
    t = o.decode("utf-8")
    j = ["# Journal — brouillon 5 de l'ordre de course (T0.8)", "",
         "Écrit par `brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon5-v1.py`. Causes : les "
         "mineurs n-2, n-3 et n-4 de " + VERIF4 + " ; n-4 tranché par la session mère (R-5059). La consigne du lecteur "
         "reste au brouillon 4, celle du juge de verdict au brouillon 3.", "",
         "| n° | cause | ancien (début) | nouveau (début) |", "|---|---|---|---|"]
    for n, (c, a, b) in enumerate(OPS, 1):
        if t.count(a) != 1:
            print(f"ARRET : opération {n} ({c}) : texte ancien trouvé {t.count(a)} fois", file=sys.stderr)
            return 2
        t = t.replace(a, b)
        j.append(f"| {n} | {c} | {a[:100].replace('|', '¦')}… | {b[:100].replace('|', '¦')}… |")
    j += ["", f"Entrée : `{SHA_E}`. Sortie : `{sha(t.encode('utf-8'))}`. Opérations : {len(OPS)}.", "",
          "**Ce que l'auteur ajoute à la lettre de R-5059** : la dernière phrase de l'étape 9 — un fichier versé en "
          "morceaux n'entre dans aucune lecture sans un texte contre-lu, donc une lecture qui en a besoin s'arrête sur "
          "une entrée manquante (ligne D1). C'est la conséquence de la section 8 et de la table D, dite pour que la "
          "ligne `COURSE-T08` ne soit pas prise pour une course lisible."]
    (D / SORTIE).write_text(t, encoding="utf-8")
    (D / JOURNAL).write_text("\n".join(j) + "\n", encoding="utf-8")
    print(sha((D / SORTIE).read_bytes()), D / SORTIE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
