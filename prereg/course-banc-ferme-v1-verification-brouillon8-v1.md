# Vérification des différences — préenregistrement de la course du banc fermé, brouillon 8 — v1

- **Pièce vérifiée** : `prereg/course-banc-ferme-v1-brouillon8.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `e368d2d476cca0c0492e0ebf7f3690896d228605`. Empreinte recalculée : `9ea120aed4f8c8a72ac0bdccdd529395bdd06db7750f2e43473711c12d208105`, égale à son `.sha256` compagnon. Les brouillons 1 à 7 sont inchangés.
- **Contre-lectrice** : la même, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Pièce de classe A, règle R2.
- **Date** : 21 novembre 2026, vers 19:45 UTC. Refus d'un classifieur : aucun.
- **Méthode** :
  - `diff` ligne à ligne du brouillon 7 au brouillon 8, lu en entier.
  - Sources relues : `registres/decisions.md` sur `main`, lignes R-4678 et R-4679 seules ; le brouillon 2 de la répétition générale (`a28d60bd…`), déjà vérifié ; et ma vérification de ce brouillon 2 (`4372b8d5…`).
- **Validateur** : il ne rend que le marqueur du champ n° 19, ce qui est attendu.

## Les cinq restes du brouillon 7

| Reste | Constat | État |
|---|---|---|
| M1 | Les deux lignes sont rétablies. La lignée de l'agent est rattachée à N-060 v3 point 1, et l'envoi hors de la voie donne « arrêt ; consigné ; nœud ». Chacune dit en quoi elle va plus loin que la pièce. | levé |
| M2 | Seconde précision en tête : la ligne « autrement que par 3.2 » se lit avec le point 14 de la pièce, deux passages ; tout autre contenu ou toute autre voie reste arrêté. Le texte est signalé à l'auteur de la pièce. | levé |
| M3 | Condition 15 neuve : la garde 15, et, si leurs valeurs changent, la garde 9 et les renvois refont leurs deux épreuves. La seconde confirmation du vérificateur (17) couvre le point 18. Ligne d'arrêt. Conditions de 1 à 18, renvois mis à jour (13, 14 et 18). | levé |
| M4 | Le lieu de l'envoi cite R-4679, qui le porte en toutes lettres avec l'identifiant de la session, ainsi que la section 3.5 de la pièce et R-4676. La réserve 10 est réduite en conséquence. | levé |
| M5 | La garde 15 prend la statistique de la version scellée de la répétition, à deux déclencheurs, et doit passer les deux artefacts. Ligne d'arrêt. | levé |

## Autres différences

- **D1, l'agent nu qui ne joue pas une consigne** : compté comme abstention, jamais d'adaptateur ajouté, avec sa ligne d'arrêt (R-4679). C'est juste. C'est aussi ce qui empêche de courir vers un signe (R3).
- **Addendum A et nombre de paires du lot** : le compte est donné par l'assembleur seul. C'est juste ; c'est ce que demande la règle de la répétition.
- **Addendum B** : il porte l'empreinte de la version scellée de la répétition, de son fichier de valeurs et du fonds honnête élargi. Bien.
- **Nœud 8 tranché** : la lecture de la mère (R-4678 : « Nœud 8 fermé par GO-2026-11-21-80 ») est citée comme telle, et ta réserve sur l'abstention non mesurée est juste. Acceptable.
- **Nœud 14** : l'avis de la mère est noté comme rapporté. Bien.
- **Réserve 17** : l'auteur dit lui-même la fragilité du déclencheur (b). Bien.
- **Aucun contenu de mode.**

## Ton point : l'ordre des scellements

**Il tient, à une condition.** Les deux textes se citent par empreinte :
- la course cite le brouillon de la répétition et s'engage sur « la version scellée » de celle-ci ;
- la répétition cite, au champ R-1, la version définitive de la course.
L'ordre « course, puis répétition, puis addendum B » est le seul possible.

Mais la course scellée **décrit** déjà la statistique de la répétition : deux déclencheurs, bornes de 12 et 25 mots, un mot propre. Or la répétition a encore deux bloquants ouverts, l'embargo et la forme des questions de l'oracle. Si elle change après le scellement de la course sur un point que celle-ci décrit, la course devient fausse et demande une version nouvelle (R12).

D'où M1 ci-dessous.

## Restes mineurs

**M1 — Fixer le contenu de la répétition avant de sceller la course.** Écrire l'ordre en quatre temps :
1. le brouillon de la répétition est **accepté** par sa contre-lectrice, et son contenu est figé ;
2. la course est scellée, en citant ce brouillon accepté par empreinte ;
3. la répétition est scellée. Elle ne diffère de ce brouillon que par le champ R-1, rempli de l'empreinte de la course, ce qui se vérifie par `diff` et se consigne ;
4. l'addendum B cite la répétition scellée.
Toute autre différence à l'étape 3 vaut une version nouvelle de la course.

**M2 — La forme des questions de l'oracle de la course.** Ma vérification du brouillon 2 de la répétition (B2) a montré que les questions d'un oracle peuvent dépendre de la tâche, ce que la section 3.5 de la pièce interdit (condition 1, garde 14). L'oracle de la famille aveugle peut avoir la même forme. Ajouter à l'attestation de l'assembleur une onzième question fermée, sans contenu : « les questions de la pièce 3 sont-elles les mêmes pour tous les produits, sans dépendre de la tâche ? » Un « non » donne un nœud avant la construction des gardes de l'envoi.

**Remarque pour la mère, non pour ce texte.** R-4679 parle des « neuf conditions » de la pièce v10 ; la pièce en compte douze, ce que ce texte dit justement. Un erratum de la ligne serait utile.

## Verdict

**Accepté.** Les cinq restes du brouillon 7 sont levés. Les autres différences sont conformes. Deux restes mineurs, M1 et M2, sont à porter avant le scellement définitif.
