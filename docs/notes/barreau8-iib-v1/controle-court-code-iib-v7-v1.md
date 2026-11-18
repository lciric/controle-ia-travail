# Contrôle court du code du saboteur à budget (ii-b), différence 6e05a9d9..ec3b0329 — v1

> Même contrôleur que les contrôles précédents (Claude Opus 5.5, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`). Code de course **exploratoire, non opposable (R-522)**. Processeur seulement : aucune dépense, aucun modèle réel chargé, aucune clé lue. Seul appel réseau : `git fetch origin prep/iib-code-v3 lot/compte-4-v1`.
>
> Je n'ai rien ouvert sous `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`. Je n'ai pas ouvert la pièce inscrite : elle est chargée et appelée par programme, son empreinte est calculée par programme. Je n'ai pas ouvert l'enveloppe de la huitième tâche. Ni commit, ni poussée.
>
> J'ai lu la consigne privée par programme : je reste exclu de tout rôle de lecteur des sondes du barreau 8.

## 0. Identité

- Tête contrôlée : `origin/prep/iib-code-v3` = `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`. Elle ajoute deux commits à `6e05a9d9` : `5cdd01e52` et `ec3b0329c`.
- Rapport v7 : `brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-corrections-iib-v7.md`, empreinte `46584a845bd0ddff6e7391ac229679fa9c0a79686b0e3f044b548fd449e6f182`, égale à celle annoncée. Lu en entier.
- Pièce inscrite dans l'arbre : empreinte `9dbcc55ca47b…`, inchangée.
- Différence : 5 fichiers. Ce sont `bases_textuelles_v1.py`, `lecture_v1.py`, `tests/test_iib_lectures_v1.py`, le rapport v7 et son compagnon. Rien d'autre.
- Extraction à moi (`/tmp/ctl-iib-v7/x`), dossiers d'essais et dépôt jouet : supprimés à la fin.

## 1. Verdict

**Autorisable.**

Il y a 0 bloquant, 0 majeur, 0 mineur et une réserve de sens (P7-R1, § 3).

- **P6-01 est levé.** J'ai retiré l'appel à la fonction d'état de la pièce dans ma copie : les essais échouent. Je l'ai remis : ils passent.
- **Les deux cas déclarés sont les seuls écarts.** Sur une grille de 3 698 combinaisons, bornes comprises, ce sont les seuls où l'état change.
- **P6-02 : la garde est écrite et protège.** Son sens exact par rapport à l'enveloppe ne se tranche pas sans l'enveloppe (P7-R1).
- **Aucune fuite.**
- **456 essais réussis**, et la répétition jouet est identique à l'octet.

## 2. P6-01

### Retrait de l'appel à la pièce

Dans ma copie, j'ai remplacé dans `lecture_2` l'appel `bases.etat_unite(...)` par l'ancienne règle du paquet, mot pour mot. Résultat de `tests/test_iib_lectures_v1.py` : **`14 failed, 42 passed`**.

J'ai aussi gardé `etat_unite`, mais avec une règle locale à la place de l'appel à la fonction de la pièce : **`15 failed`**. Je retiens ce second résultat avec prudence : une partie des échecs peut venir de la forme du retour (base décisive, aires) plutôt que de l'état.

Fichiers remis et comparés à l'octet à ceux de la branche : **`56 passed`**.

### Les seuls écarts

Le script de la grille est hors dépôt. Il appelle la vraie fonction par `Bases("jouet").etat_unite`, et l'ancienne règle recopiée telle qu'elle était à `6e05a9d9`.

La grille croise :
- sept aires (0,5 ; 0,69 ; 0,6999999 ; 0,70 ; 0,7000001 ; 0,75 ; 0,9) ;
- six bornes basses, dont l'égalité stricte au quantile du plancher et son voisin ;
- deux quantiles de plancher ;
- l'état « non calculable » pour chacune des deux bases.

Cela fait 3 698 paires. Résultat :
- 3 386 accords ;
- 168 écarts du cas (a), une seule base non calculable ;
- 144 écarts du cas (b), aires égales et états différents ;
- **aucun autre écart**.

Limite : la borne haute de l'intervalle n'a pas varié dans la grille (aire + 0,05). L'ancienne règle ne la lit pas. Si la fonction de la pièce la lisait, un écart de plus resterait possible pour d'autres valeurs.

### Le champ descriptif reste hors de la phrase

L'état « mots et coût » de la lecture est celui de l'unité décisive (B100 contre H), rendu par la fonction de la pièce. La phrase « diffus réalisé » ne lit que cet état (`lecture_v1.py`, bloc des `etats`).

Le champ `etat` de chaque base prise seule n'y entre pas sous sa forme « réussit » ou « échoue ». Il ne sert qu'à écarter une base « non calculable » du choix de la meilleure base par action. Or cette valeur ne vient pas du seuil descriptif : elle vient du modèle déclaré non calculable par la pièce, ou d'une garde. Les seuils de ce champ sont exigés égaux à ceux de la pièce (`exiger_piece_citee`).

## 3. P6-02

### Ce que dit le relevé

Le relevé ne définit pas « lecture de transfert ». Il la nomme seulement parmi les gardes de l'enveloppe de la huitième tâche à reprendre (l. 36). Ailleurs, il signale des « contrôles et transferts » propres à la course d'origine, non réemployables tels quels (l. 136).

### Ce que fait le code

La garde (`exiger_aucun_transfert`, appelée à chaque notation) **refuse tout transfert** :
- un jeu noté différent du jeu appris ;
- une condition lue hors du jeu appris ;
- un modèle qui n'a pas été appris par le chargeur.

Les conditions ne sont jamais passées à la pièce. J'ai neutralisé la comparaison des jeux dans ma copie : les deux essais de transfert **échouent**. Fichier remis : ils passent.

### Réserve P7-R1

Le sens ne se tranche pas sans l'enveloppe. Si la garde de l'enveloppe encadre une lecture de transfert permise (un modèle appris sur un jeu, appliqué à un autre sous conditions), la garde du paquet est **plus stricte** : elle interdit tout transfert. Elle ne peut donc rien laisser passer que l'enveloppe refuserait.

La lecture de la diffusion n'a d'ailleurs aucun jeu de transfert, ce que la garde fait respecter. Je ne la tiens pas pour un défaut. Si l'on veut l'égalité de sens avec l'enveloppe, quelqu'un qui peut lire l'enveloppe doit le confirmer.

## 4. Non-fuite, essais, répétition, règles

- **Non-fuite.** Le script hors dépôt a lu la consigne par `git show`, empreinte `9f8bbdef…90c1`, égale à son compagnon. Il a parcouru :
  - les 47 fichiers ajoutés ou modifiés par la branche depuis `a3adf4128`, hors les fichiers de consigne ;
  - les messages de **tous** les commits de la branche, dont `5cdd01e52` et `ec3b0329c` ;
  - l'ensemble des lignes ajoutées.

  Résultats :
  - triplets communs : **0** ;
  - motifs réels à la lettre, sans tenir compte de la casse : **aucun** ;
  - motifs qui trouvent quelque chose : **aucun** ;
  - plus longue suite commune : 2 mots au plus ;
  - plus longue sous-chaîne commune : 10 caractères au plus.

  La méthode a été validée sur la consigne elle-même : 93 et 10 triplets, et les 9 motifs.
- **Suite ciblée** : **`456 passed in 387.66s (0:06:27)`**, fin à 2026-11-18T22:38:48Z, aucun saut. La liste garde l'empreinte `847676ef…e3b6`.
- **Répétition jouet** (entropie 20261118, configuration `2e65c31b…`, inchangée) : **48 fichiers comparés, 0 différent**, code 0.
- **R9** : le diff n'ajoute ni aléa, ni graine, ni générateur.
- **Moyenne ou médiane sur des jetons** : aucune n'est ajoutée.
- **R5** : le banc du développeur compte 12 mutations sur 12 vues. Je l'ai recoupé par trois mutations à moi, toutes vues.

## 5. Ce qui reste avant la course

- **P7-R1** : à confirmer par un lecteur de l'enveloppe, si l'égalité de sens est voulue.
- Les points du rapport v6 que le développeur renvoie au directeur ou à la session mère, et que ce code ne touche pas.
- Les points de la session mère : forme de la ligne de création de 7b ; compléments de l'ordre et rapatriement ; ordre et devis.

## 6. Lectures hors mandat, refus

- **Lus** :
  - le rapport v7 en entier ;
  - la différence des deux fichiers de `src/` ;
  - dans le relevé, les lignes qui nomment le transfert (l. 36 et l. 136).
- **Exécuté sans lecture** : la fonction d'état de la pièce, appelée par la grille.
- **Non ouverts** : la pièce, l'enveloppe de la huitième tâche, et `tests/test_iib_lectures_v1.py` en dehors de ses résultats.
- **Refus** : aucun.
