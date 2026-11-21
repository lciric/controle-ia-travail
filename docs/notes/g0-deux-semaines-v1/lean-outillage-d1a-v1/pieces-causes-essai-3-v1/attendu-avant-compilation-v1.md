# Ce que je m'attends à lire avant de compiler les cinq items sondes (écrit le 2026-11-21, avant toute compilation)

Faits lus avant (pièce epreuve-isolement-v6.json et sources) :
- les cinq items sondes `iso_*_v2.lean` n'ont **pas** `import Mathlib` (prélude seul) ; les 21 items des gardes l'ont.
  Le module « prelude sans import » du pas noyau compile en 0,06 à 0,09 s. Donc 0,34 à 0,40 s n'est pas « avant la fin des
  imports » : c'est le temps normal d'un fichier sans Mathlib ; l'échec est dans l'élaboration du fichier lui-même.
- le bac compile `lean --json --root=/item -o /item/Item.olean -i /item/Item.ilean /item/Item.lean` ; il ne lit que la
  sortie standard (`compilation.out`), jamais `compilation.err`.

Attente principale (confiance 0,6) : erreur d'élaboration dans la fonction commune `tenter`, sous Lean 4.35.0 :
`r.take 120` ne rend plus un `String` (API des chaînes refondue : `String.take` rend une tranche `String.Slice`), donc
`String.append ... (r.take 120)` est mal typé ; `tenter` n'est pas définie, et chaque `#eval tenter …` échoue
(« unknown identifier tenter » ou erreur de type) : aucune ligne « ISOLEMENT », code 1.
Attentes secondaires : `(d.map (·.fileName)).toList` ou `toString` sur un tableau mal résolus (item lecture) ; un
avertissement de dépréciation n'expliquerait pas le code 1.
Ce qui me ferait changer : une erreur d'accès au fichier ou d'import (refus du bac), qui serait un fait d'isolement.
Pour le pic de mémoire : systemd 255 ; je m'attends à ce que `Memory peak` de `systemd-run --wait` soit une valeur en
cache lue tôt (au passage de l'unité à « active »), parce que le cgroupe est déjà retiré quand systemd-run lit les
propriétés finales ; le temps de processeur, lui, serait mis en cache au retrait du cgroupe.
