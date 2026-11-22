#!/usr/bin/env python3
"""Écrit le brouillon 6 de l'ordre de course de la base boîte noire (T0.8) à partir du brouillon 5, par opérations
déclarées. Causes : la décision de la session mère qui admet à la lecture le fichier recomposé (R-5060 de
`registres/decisions.md`) ; trois changements de la chaîne de lancement après sa contre-lecture, transmis par son
développeur le 22 novembre (texte et configuration dans le même commit ; destruction par la machine ; échéance).
Chaque texte ancien est trouvé une fois ; rien n'est écrasé (R12).
Usage, depuis la racine : python3 brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon6-v1.py
"""
import hashlib
import sys
from pathlib import Path

D = Path("docs/procedures/t08-course-v1")
ENTREE, SHA_E = "ordre-course-t08-v1-brouillon5.md", "c029aca9dc9b62e43e5e23be2fda2f13728deb3c73b4e4d0ed137f28ac8725b4"
SORTIE, JOURNAL = "ordre-course-t08-v1-brouillon6.md", "journal-pieces-de-course-t08-brouillon6-v1.md"

OPS = [
    ("renvoi", "sur une machine louée — v1 — brouillon 5", "sur une machine louée — v1 — brouillon 6"),
    ("renvoi",
     "- **Statut** : **brouillon 5**, pièce de classe A, qui porte les commandes. Il applique au brouillon 4",
     "- **Statut** : **brouillon 6**, pièce de classe A, qui porte les commandes. Il ajoute au brouillon 5 (`" + SHA_E +
     "`) l'admission du fichier recomposé à la lecture (décision de la session mère, R-5060 de "
     "`registres/decisions.md` : étape 9) et trois changements de la chaîne de lancement après sa contre-lecture, "
     "transmis par son développeur (étape 11, section 13) ; opérations : "
     "`journal-pieces-de-course-t08-brouillon6-v1.md`. Le brouillon 5 appliquait au brouillon 4"),
    ("renvoi", "la différence de ce brouillon 5 est à vérifier de même.",
     "la différence des brouillons 5 et 6 est à vérifier de même."),
    ("R-5060",
     "Le fichier ainsi versé n'entre dans aucune lecture sans un texte contre-lu (section 8) : si la lecture en a "
     "besoin, elle s'arrête sur une entrée manquante (ligne D1) tant que ce texte n'existe pas.",
     "**Admission du fichier recomposé** (décision de la session mère, R-5060 ; cette ligne est le texte contre-lu que "
     "veut la section 8) : le fichier recomposé de ses morceaux entre dans la lecture, à son chemin d'origine, à une "
     "condition, contrôlée par programme et journalisée — son empreinte est égale à celle du fichier entier, calculée "
     "sur la machine avant le découpage, et chaque morceau a gardé la sienne ; s'il a un compagnon ou une empreinte "
     "consignée par la course, c'est la même. C'est alors, à l'octet, la sortie que la course a scellée, portée "
     "autrement : ce n'est pas un résultat partiel, et rien d'autre ne change dans la lecture, qui garde ses propres "
     "contrôles d'empreinte. Une seule empreinte qui diffère : le fichier n'entre pas, la lecture s'arrête sur une "
     "entrée manquante (ligne D1), nœud."),
    ("chaîne",
     "11. **Destruction par l'identifiant** (R10), après la vérification de la poussée ;",
     "11. **Destruction par l'identifiant** (R10), après la vérification de la poussée — la machine se détruit "
     "elle-même, par son identifiant, en fin normale une fois le versement prouvé, et à l'épuisement du plafond "
     "restant ; l'exécutante vérifie à l'inventaire qu'elle n'y est plus, et la détruit si elle y est encore, jamais "
     "avant le versement des morceaux d'une fin en anomalie de taille ;"),
    ("chaîne",
     "Avant l'étape 2, par la session mère, au scellement (rappel ; ce n'est pas un geste de l'exécutante) : la "
     "configuration réelle de la course (`scripts/ecrire_configuration_course_t08_v1.py`), puis la branche d'entrée "
     "(`scripts/construire_branche_entree_t08_v1.py construire`), aux commandes du rapport, § 8.",
     "Avant l'étape 2, par la session mère, au scellement (rappel ; ce n'est pas un geste de l'exécutante) : la "
     "configuration réelle de la course (`scripts/ecrire_configuration_course_t08_v1.py`), puis la branche d'entrée "
     "(`scripts/construire_branche_entree_t08_v1.py construire`), aux commandes du rapport, § 8. **Le texte scellé, la "
     "configuration réelle de la course et leurs compagnons entrent sur `main` dans le même commit `S`** : le lanceur "
     "relit la configuration à ce commit, et une configuration commise à part fait échouer les contrôles (course "
     "bloquée, sans dommage)."),
    ("chaîne",
     "L'amorce laisse la machine à l'état arrêté en fin de course ; elle n'est détruite que par ce geste, après "
     "l'étape 9.",
     "Depuis la contre-lecture de la chaîne, la machine se détruit elle-même en fin normale, après le versement "
     "prouvé, et à l'épuisement du plafond restant ; son échéance chez le loueur est l'heure du plafond restant. Ce "
     "geste ne sert que si elle est encore à l'inventaire. **Ces changements sont postérieurs au rapport cité plus "
     "haut : à confirmer sur le commit `C` par le contre-lecteur de la chaîne, avec les commandes de P7.**"),
]


def sha(o: bytes) -> str:
    return hashlib.sha256(o).hexdigest()


def main() -> int:
    if (D / SORTIE).exists() or (D / JOURNAL).exists():
        print("ARRET : sortie déjà là (R12)", file=sys.stderr)
        return 2
    o = (D / ENTREE).read_bytes()
    if sha(o) != SHA_E:
        print("ARRET : empreinte du brouillon 5 différente", file=sys.stderr)
        return 2
    t = o.decode("utf-8")
    j = ["# Journal — brouillon 6 de l'ordre de course (T0.8)", "",
         "Écrit par `brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon6-v1.py`. Causes : "
         "« R-5060 », décision de la session mère (admission du fichier recomposé) ; « chaîne », message du développeur "
         "de la chaîne de lancement du 22 novembre vers 21:19 UTC, après la contre-lecture de la chaîne.", "",
         "| n° | cause | ancien (début) | nouveau (début) |", "|---|---|---|---|"]
    for n, (c, a, b) in enumerate(OPS, 1):
        if t.count(a) != 1:
            print(f"ARRET : opération {n} ({c}) : texte ancien trouvé {t.count(a)} fois", file=sys.stderr)
            return 2
        t = t.replace(a, b)
        j.append(f"| {n} | {c} | {a[:100].replace('|', '¦')}… | {b[:100].replace('|', '¦')}… |")
    j += ["", f"Entrée : `{SHA_E}`. Sortie : `{sha(t.encode('utf-8'))}`. Opérations : {len(OPS)}.", "",
          "**À juger par le contre-lecteur** : la section 8 demande, pour ce qui est récupéré d'une machine en échec, "
          "un texte contre-lu et le mot de Lazar. L'auteur lit le fichier recomposé, égal à l'octet à la sortie "
          "scellée, comme la sortie elle-même et non comme un résultat récupéré ; la session mère l'a décidé à son "
          "étage (R-5060). Si cette lecture ne tient pas, le mot de Lazar est requis.", "",
          "**Non vérifié par l'auteur** : les trois changements de la chaîne, connus par un message ; le code n'a pas "
          "été relu."]
    (D / SORTIE).write_text(t, encoding="utf-8")
    (D / JOURNAL).write_text("\n".join(j) + "\n", encoding="utf-8")
    print(sha((D / SORTIE).read_bytes()), D / SORTIE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
