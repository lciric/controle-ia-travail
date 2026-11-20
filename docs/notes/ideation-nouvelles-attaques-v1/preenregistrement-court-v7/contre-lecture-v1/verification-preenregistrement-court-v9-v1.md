# Vérification — préenregistrement court v9 de la course « nouvelles attaques » — v1

- Contre-lecteur neuf, modèle O, le même que pour la contre-lecture de la v7 (`acb02c44…`) et la vérification de la v8 (`269a64b0…`). Je n'ai pas écrit la v9. Règle R2. Écrit le 2026-11-20 ; relevé de `date -u` : 13:19:11Z, avant l'écriture.
- Processeur seul. Aucun appel, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit. Un `git fetch origin main` (`origin/main` à `74282b274`). **Aucun refus de permission, de classifieur ni de garde.** Ce rapport ne contient aucune recette, aucun nom ni énoncé de mode, aucun identifiant de modèle.

## Verdict

**Conforme, à sceller (traitement de la contre-lecture 5 par la mère).** Une condition au scellement : ma vérification de la v8 doit être versée sur `main` au chemin que la phrase de version cite (§ 3).

## 1. Empreintes et rejeu

- **Empreintes.** Égales à leur compagnon : la v9 (`3ef9773797b663b6a8e78f0b1d0eff14ac1bb61f4dba992612f57f20d72354c9`), son journal, le jeu (`1bf70404…`), le différentiel (`698da257…`), la sortie du validateur (`97feea71…`) et le rapport du rédacteur (`c1a0ca26…`).
- **Rejeu.** L'outil (`391db990…`), joué avec ce jeu sur la v8 (`4970d531…`), rend « FAIT : 9 remplacement(s) » et la sortie `3ef97737…` ; `cmp` avec la v9 versée : égal.
- **V1 à V5.** Le programme `comparer_jeux_v6_v1.py` les trouve égaux, objet pour objet, à ceux de mon jeu (`corrections-preenregistrement-court-v8-v1.json`, `4ed216c8…`). Le jeu versé n'ajoute que quatre objets.
- **Validateur.** Sur la v9, il rend « problemes : aucun », égal à la sortie versée.

## 2. Le différentiel : neuf lieux, rien d'autre

Le différentiel v8 → v9 ne touche que neuf lieux :
- **V1 à V5 :** la phrase de version de la v8 (V5) ; la ligne de case (V3) ; la lecture de l'ordre de course (V1) ; le point 15 de « ce qui reste » (V2) ; l'entrée de la contre-lecture 5 (V4).
- **Quatre lieux de tenue :** le titre, la ligne de date (relevé « Version 9 »), le statut et une phrase de version neuve pour la v9.

Rien d'autre ne change :
- aucun total, seuil, arrêt, tirage ni chiffre ;
- le statut ne change qu'aux mentions de la v8 et de la v9 ;
- la phrase de version de la v9 décrit V1 à V5 sans en ajouter.

## 3. La phrase de version cite ma vérification par son chemin de branche (écart 2 du rédacteur)

Le fichier existe au chemin cité, à l'empreinte citée : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/contre-lecture-v1/verification-preenregistrement-court-v8-devis-v6-v1.md`, `269a64b0…`, égal à son compagnon. Le jeu `4ed216c8…` et la contre-lecture `acb02c44…` y sont aussi, chacun égal à son compagnon.

Le fichier n'est pas encore sur `main` (constaté par `git cat-file` à `74282b274`). C'est le cas de toute la chaîne de la v7 à la v9, et c'est l'usage de la mère depuis R-4206 : la chaîne est recopiée sur `main` au scellement, à l'octet et aux mêmes chemins.

**C'est donc acceptable**, à une condition, déjà dans l'usage : avant de sceller la v9, la mère verse sur `main`, au même chemin et à la même empreinte, ma vérification de la v8, son jeu `4ed216c8…`, la présente pièce, ainsi que le devis v6, son calcul v5 et sa sortie, que la table cite au dossier `NA/preenregistrement-court-v7/`. Si le versement se fait à un autre chemin, la phrase et la table se corrigent avant le scellement.

## 4. Le traitement de la contre-lecture 5

Il est absent, comme attendu : `grep -c -F -e "Traitement : K'1"` sur la v9 rend 0. Il reste à la mère. Le validateur ne voit pas ce manque. Après l'écriture du traitement, le même `grep` doit rendre 1 sur le texte à sceller, et le validateur rester à « aucun ».

## 5. Écarts

1. J'ai déduit le nom du rapport du rédacteur par la convention des noms, puis je l'ai vérifié par son compagnon. Je n'ai fait aucune commande de liste.
2. Mes essais sont dans le sous-dossier `v8/` de mon dossier ; rien n'est écrit ailleurs.

— contre-lecteur neuf, modèle O
