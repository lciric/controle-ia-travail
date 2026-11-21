# Vérification courte — course du banc fermé, brouillon 14, et répétition générale, brouillon 9 — v1

- **Pièces vérifiées** :
  - `prereg/course-banc-ferme-v1-brouillon14.md`, commit `5182b602`, empreinte `4489d39957b7dba53d015521867c2d7cb56ee01a6d3e2070523b889555173784` ;
  - `prereg/repetition-generale-banc-ferme-v1-brouillon9.md`, commit `8862bde8`, empreinte `a58cab35cf4914a4e78decec95f296d824626752f4028b347ca5741d49f76e08`.

  Leurs empreintes, recalculées, sont égales à leurs compagnons.
- **Contre-lectrice** : la même, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Elle répond à `afebd51a…`.
- **Date** : 21 novembre 2026, vers 20:50 UTC. Refus d'un classifieur : aucun.
- **Méthode** :
  - La pièce de sécurité v16 (`b8bcda60…`, commit `dd90f13f`) est comparée par `diff` à la v15. Son verdict « accepté » a été lu (`92bc02b8…`, commit `b9e42026`). Ses seuls changements : les mesures ne portent que sur les consignes dérivées ; la consigne du jumeau tient lieu d'énoncé pour l'ôtement ; deux cas sains ajoutés à la garde 15 ; l'en-tête.
  - `diff` du brouillon 13 au brouillon 14, et du brouillon 8 au brouillon 9, lus en entier.
  - Vérifié par programme :
    - la liste d'arrêt de la course est égale, sur ses vingt-neuf lignes, à la section 4.2 de la v16 ;
    - le bloc de définition de la garde de fuite est identique dans les deux textes.
- **Validateur** : il ne rend plus que les marqueurs attendus. Les deux entrées de contre-lecture portent maintenant leurs deux empreintes.

## Constats

| Point | Constat | État |
|---|---|---|
| M1 de forme | Empreintes entières des brouillons relus, `711e061f…` et `40837f73…`. Le validateur ne les signale plus. | levé |
| M2 de forme | Réserve 16 : deux différences admises au troisième temps, et pas d'autre — le champ R-1 et des entrées ajoutées à la section « Contre-lecture ». | levé |
| v16, consigne du jumeau | Elle entre dans la matière de la tâche et tient lieu d'énoncé : le cadre commun est ôté. Les deux conditions passent de même par la garde. Quatre cas sains : condition 4, D6, ligne d'arrêt, épreuve sur matière factice de la répétition. Les réserves que cela lève sont levées. | conforme |
| Fonds honnête | Inchangé. Il contient toujours les consignes des jumeaux, ce qui reste cohérent : un mot propre est un mot de la part propre absent de ce fonds. | conforme |

Aucune autre différence. Aucun contenu de mode.

## Verdict

**Accepté**, l'un et l'autre, sans reste.

**Le brouillon 9 de la répétition est accepté : c'est le premier temps de l'ordre des scellements, et son contenu est figé** (`a58cab35…`). La répétition scellée ne pourra différer de ce brouillon que par son champ R-1 et par des entrées ajoutées à sa section « Contre-lecture ».

Restent, dans l'ordre :
1. la course en version définitive, citant ce brouillon : champs remplis, nœuds 13 et 14 tranchés, mot de Lazar ;
2. la répétition scellée, avec ma relecture courte des passages de la course qu'elle emploie, entre le brouillon 14 et la version définitive ;
3. après la répétition, l'addendum B de la course.
