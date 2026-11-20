# Contre-lecture de l'additif 3 « branches de sortie qui ne portent que des traces » — v1

- **Pièce lue** : `additif-3-branches-de-traces-seules-v1.md`, sha256 0ae5da101827ee6675569c3663fb2cfa1719bbf4f90c44dfa7aaa471dd5e79c1 (vérifiée).
- **Code relu** : `lecture_v1._familles_formees` et `instance_de` dans `lecture-figee-neuve`.
- **Faits** : ceux qu'atteste la mère.

**Verdict : scellable après ces couples.** Aucun n'est bloquant ; un seul est important.

## Ce qui tient

- **Règle mécanique.** Elle ne porte que sur des noms de chemins et des commits, sans ouvrir aucun fichier, et respecte donc le point 12. Ses quatre conditions sont les bonnes : la chute et la marche jamais commencée selon l'additif 2, la filiation, l'absence de tout chemin hors de `traces-b5f/`, la copie à la même tête, et la destruction de la première tentative.
- **Ordre.** Copie prouvée, puis destruction, vérification, suppression, relevé, recréation : c'est juste. Je ne vois aucun pas à déplacer.
- **Les quatre ajouts du rédacteur.**
  - « Condition 3 et non 2 » : exact. Dans l'additif 2 v6, l'absence de la branche de sortie est la condition 3 ; c'était la condition 2 dans les versions 1 à 3.
  - La filiation : nécessaire. Sans elle, le différentiel contre `4bdf0d22…` ne dirait rien de sûr.
  - La destruction avant la suppression : nécessaire. Sans elle, une tentative relancée pourrait pousser de nouveau sa branche.
  - La copie jamais supprimée ni réunie : nécessaire, et conforme à « récupérer ce qui est récupérable ».
- **Le code de lecture figé, sans ambiguïté.** `_familles_formees` ne regarde que les dossiers `donnees/<AAAAMMJJ-HHMMSS>-b5f-formation-<n>-x1` de la branche réunie de la formation, et en exige exactement un.
  - Les branches supprimées ne portent aucun chemin sous `donnees/`. Même déjà réunies, elles n'ajouteraient donc aucune marche.
  - Les copies sous `traces/…` ne sont jamais réunies.
  - La recréation écrit un seul dossier de marche, sous un horodatage neuf.

  Il n'y a ni deux marches, ni zéro marche pour une instance recréée et versée. La suppression et la reprise du nom de branche ne changent rien à ce que lit ce code.

## Couples

**1. Le différentiel doit être lu sans détection des renommages (important).**
- Constat. `git diff --name-only 4bdf0d22… <tête>` suit par défaut les renommages et n'affiche alors que le chemin d'arrivée. Prenons un fichier suivi déplacé hors de `registres/`, de `src/` ou de `donnees/` vers `traces-b5f/`. Il n'apparaîtrait que sous `traces-b5f/`, et la condition 2 passerait alors qu'un chemin hors de `traces-b5f/` a changé.
- Correction. À la condition 2, écrire `git diff --no-renames --name-only 4bdf0d22e4246b4fe431bd8754e26fea4ccd037f <tête>`. Ajouter : « chaque chemin rendu, ajouté, modifié ou retiré, commence par `traces-b5f/` ».

**2. Supprimer seulement si la tête n'a pas bougé (mineur).**
- Constat. Entre le relevé de la condition 3 et la suppression, rien ne garantit que la tête de `B` est encore celle qu'on a comparée à la copie. La destruction rend ce cas très improbable, mais la commande peut le refuser d'elle-même.
- Correction. Écrire : « suppression par `git push origin --force-with-lease=refs/heads/B:<tête relevée> :refs/heads/B`, `B` écrit en entier ; refus de la poussée : nœud ».

**3. L'exception à R12 est une règle gelée du programme, non un passage du texte (mineur).**
- Constat. La table range la règle des noms versionnés (R12) parmi les passages remplacés. R12 est une règle gelée du dépôt, que l'amorce applique (ligne 282). Un additif ne peut pas en faire l'exception de lui-même : seul le mot de Lazar le peut. L'en-tête nomme les trois suppressions, mais pas cette exception.
- Correction.
  - Dans la ligne de la table consacrée à R12, écrire : « exception à la règle gelée R12, accordée par le même mot de Lazar et consignée par la session mère au registre des décisions ».
  - Dans l'en-tête, ajouter à ce que couvre le mot de Lazar : « et l'exception à R12 que porte la reprise des trois noms de branche ».

**4. La ligne des sorties doit citer la branche recréée (mineur).**
- Constat. Le nom `…-instance-<n>-x1` désignera deux têtes successives. La ligne `SORTIES-FORMATION-B5F` et la réunion de la branche de la formation doivent prendre la tête de la recréation, jamais celle qui a été supprimée.
- Correction. En section 5, ajouter pour la session mère : « la réunion de la branche de la formation et la ligne `SORTIES-FORMATION-B5F` citent, pour les instances 2, 3 et 4, la tête de la branche de la recréation ; les têtes supprimées (`4fef6073…`, `b35dfe17…`, `77fd59da…`) ne sont citées que dans le registre des suppressions et sous `traces/…` ». Facultatif : vérifier par `git merge-base --is-ancestor` qu'aucune de ces trois têtes n'est déjà dans la branche réunie de la formation.

**5. Les identifiants de commit sont tronqués dans les faits (mineur).**
- Constat. La section 1 écrit les têtes sur huit signes. La règle compare des identifiants entiers, et le registre des suppressions les écrira entiers.
- Correction. Écrire les têtes en 40 signes, telles que la mère les atteste :
  - instance 2 : `4fef60738d5bc05fee4f249ab0396c026ff56eab` ;
  - instance 3 : `b35dfe177d970aa205d4fd7b9f73bf6859b75d9a` ;
  - instance 4 : `77fd59da60ddc39b24736a3353ad8fb1113c388d`.
